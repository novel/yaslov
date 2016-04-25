import httplib
import json
import urllib


class YaslovDict(object):

    def __init__(self, key, lang):
        self._key = key
        self._lang = lang
        super(YaslovDict, self).__init__()

    def _build_translation(self, response):
        res = []
        for defin in response["def"]:
            term = "%s (%s)" % (defin["text"], defin["pos"])
            trans = []
            examples = []
            for tr in defin["tr"]:
                trans.append(tr["text"])
                if "ex" in tr:
                    for ex in tr["ex"]:
                        ex_trans = ", ".join([i["text"] for i in ex["tr"]])
                        examples.append("%s: %s" % (ex["text"], ex_trans))

            res.append("%s: %s" % (defin["text"], ", ".join(trans)))
            for example in examples:
                res.append(example)

        return '\n'.join(res)

    def lookup(self, text):
        conn = httplib.HTTPSConnection("dictionary.yandex.net")
        params = urllib.urlencode({"key": self._key,
                                   "format": "plain",
                                   "lang": self._lang,
                                   "text": text.encode("utf-8")})

        conn.request("GET", "/api/v1/dicservice.json/lookup?" + params)
        resp = conn.getresponse()

        resp_decoded = json.loads(resp.read())

        return self._build_translation(resp_decoded)
