yaslov
=========
Yaslov is a simple command-line client for https://tech.yandex.ru/dictionary/

Its interface is as dumb as possible, you just give it a word to translate and
it gives you translations, just like this:

```
$ yaslov -l en-ru hello
hello: привет
big hello: большой привет
hello: поздороваться
$ 
```

You'll need a config file with the API key configure. A minimal config file looks like this:

```
$ cat ~/.config/.yaslov.conf 
[api]
key = YourAPIKey
$
```

You can obtain an API key [here](https://tech.yandex.ru/keys/get/?service=dict).

Hope you'll find it useful.
