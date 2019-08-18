# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 00:01:50 2019

@author: takah
"""


class do2stmd:

    def __init__(self):
        pass

    def export(self, infile, outfile=''):
        importer = Importer(infile)
        database = DatabaseFactory().create(*importer.extractInfo())

        if outfile == '':
            outfile = infile.replace('.do', '_converted.stmd')

        with open(outfile, mode='w') as f:
            indent = ' ' * 4
            for code_block in database.get():
                if code_block.flag_stata and not code_block.isEmpty():
                    f.write('```s\n')
                    for l in code_block.getContent():
                        f.write(indent + l + '\n')
                    f.write('```\n')
                else:
                    for l in code_block.getContent():
                        f.write(l + '\n')
                f.write('\n')


class Importer:

    def __init__(self, do_file):
        self._setContent(do_file)
        self._setIndexList()

    def _setContent(self, do_file):
        with open(do_file) as f:
            self.content = [l.rstrip() for l in f]

    def _setIndexList(self):
        self.index_list_s = [i for i, l in enumerate(self.content) if l.strip() == '/*md']
        self.index_list_e = [i for i, l in enumerate(self.content) if l.strip() == 'md*/']

    def extractInfo(self):
        markdown_list = []
        stata_list = []
        if self.index_list_s[0] != 0:
            stata_list.append([0, self.index_list_s[0] - 1])

        for i in range(len(self.index_list_s)):
            markdown_list.append([self.index_list_s[i], self.index_list_e[i]])
            try:
                stata_list.append([self.index_list_e[i] + 1, self.index_list_s[i+1] - 1])
            except IndexError:
                pass

        if self.index_list_e[-1] < len(self.content) - 1:
            stata_list.append([self.index_list_e[-1] + 1, len(self.content) - 1])

        return self.content, markdown_list, stata_list


class CodeBlock:

    def __init__(self, code, flag_stata, line_s, line_e):
        self.flag_stata = flag_stata
        self._line_s = line_s
        self._line_e = line_e
        self._setContent(code)

    def _setContent(self, code):
        try:
            while code[self._line_s].strip() == '':
                self._line_s = self._line_s + 1
            while code[self._line_e].strip() == '':
                self._line_e = self._line_e - 1
            self._content = code[self._line_s:self._line_e+1]
        except IndexError:
            self._content = None

    def getOrder(self):
        return self._line_s

    def isEmpty(self):
        return self._content is None

    def getContent(self):
        if self.isEmpty():
            return None
        return [l for l in self._content if l.strip() not in ['/*md', 'md*/']]


class Database:

    def __init__(self):
        self._content = []

    def add(self, code_block):
        self._content.append(code_block)

    def sort(self):
        self._content = sorted(self._content, key=CodeBlock.getOrder)

    def get(self):
        return [data for data in self._content if data.getContent() is not None]


class DatabaseFactory:

    def __init__(self):
        pass

    def create(self, source, markdown_list, stata_list):
        database = Database()
        for indexes in markdown_list:
            database.add(CodeBlock(source, 0, *indexes))

        for indexes in stata_list:
            database.add(CodeBlock(source, 1, *indexes))

        database.sort()
        return database
