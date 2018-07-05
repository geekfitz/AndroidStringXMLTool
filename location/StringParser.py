# -*-coding:utf-8-*-
import collections
import re


class StringParser(object):

    def __init__(self):
        super(StringParser, self).__init__()

    pattern = re.compile("\{\{[^\}]*\}\}")

    def parse(self, input_str):
        match = self.pattern.finditer(input_str)
        if match:
            if isinstance(match, collections.Iterator):
                for element in match:
                    m_str = element.group()
                    if m_str.startswith("{{!CDATA"):
                        input_str = "<![CDATA[ " + input_str.replace(m_str, "") + "]]>"
                    else:
                        input_str = input_str.replace(m_str, m_str.replace("{{", "").replace("}}", ""))
                return input_str
        else:
            return input_str
