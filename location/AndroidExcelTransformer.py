# -*-coding:utf-8-*-

import os
import xlrd

from FileUtil import FileUtil
from StringParser import StringParser

# excel = "sample.xlsx"
excel = "translate.xls"
OUT_PROJECT = os.path.expanduser("AndroidLanguagePackage")

book = xlrd.open_workbook(excel)
sheet = book.sheet_by_index(0)

FileUtil.make_dir(OUT_PROJECT)
string_parser = StringParser()

for col in range(sheet.ncols):

    if col == 0:
        continue

    cells = sheet.col(col)
    string_keys = sheet.col(0)
    lang_list = list()

    lang = cells[0].value

    if isinstance(lang, unicode):
        lang = lang.encode('utf-8')

    for i in range(0, len(cells)):

        key = string_keys[i].value
        value = string_parser.parse(cells[i].value)

        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')

        if i > 0 and value != "":
            if i == 1:
                s = '\t<string name="%s">%s</string>' % (key, value)
            else:
                s = '<string name="%s">%s</string>' % (key, value)
            lang_list.append(s)

    print "language: %s" % lang

    language_dir = "%s/%s" % (OUT_PROJECT, lang)
    FileUtil.make_dir(language_dir)
    lang_file_path = "%s/strings.xml" % language_dir
    fileHandler = open(lang_file_path, "w")

    fileHandler.write("""<?xml version="1.0" encoding="utf-8"?>""")
    fileHandler.write("\n<resources>\n")
    fileHandler.write("\n	".join(lang_list))
    fileHandler.write(" \n</resources>")
    fileHandler.close()
