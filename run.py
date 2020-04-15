# -*- coding: utf-8 -*-

import os
from wox import Wox

class Mock(Wox):

    def copyToClipboard(self, value):
        os.system('echo | set /p nul="' + value.strip() + '"| clip')

    def query(self, query):
        results = []
        irony = ""
        i = False
        for char in query:
            if char == '\\' or char == '"':
                continue
            if i:
                irony += char.upper()
            else:
                irony += char.lower()
            if char != ' ':
                i = not i

        results.append({
            "Title": irony,
            "SubTitle": "Original: \"{}\"".format(query),
            "IcoPath":"irony.png",
            "JsonRPCAction":{
                "method": "copyToClipboard",
                "parameters":[irony],
                "dontHideAfterAction":False
            }
        })


        return results

if __name__ == "__main__":
    Mock()
