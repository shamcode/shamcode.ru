Title: npm pack
Date: 2019-01-03 19:24
Tags: js, npm
Slug: npm-pack
Lang: ru
Category: Tips
Authors: shamcode
Summary: Полезная команда перед `npm publish`

Уже неоднакратно я косячу при деплое пакетов в `npm`, а если точнее, то забываю поправить `.npmignore` и
постоянно лью кучу файлов нужных исключительно в dev окружении (тесты, coverage и т.п.).
Но наконец-то я загуглил как получить список файлов перед публикацией и нашёл вот это (кликабельно):
[`npm pack --dry-run`](https://docs.npmjs.com/cli/pack.html)

Т.е. команда собирает Tarball, а с аргументом `--dry-run` только выводит список файлов, которые в него попадут, без его реального создания.
И что приятно, при этом выполняется скрипт `npm prepublish`.

Например на одном моём пакете она выдает такое (не считая вывода `npm prepublish`):
```
npm notice
npm notice 📦  sham-ui@2.0.3
npm notice === Tarball Contents ===
npm notice 2.6kB   package.json
npm notice 1.7kB   CHANGELOG.md
npm notice 1.1kB   LICENSE
npm notice 1.2kB   README.md
npm notice 191.1kB yarn.lock
npm notice 21.7kB  lib/sham-ui.js
npm notice === Tarball Details ===
npm notice name:          sham-ui
npm notice version:       2.0.3
npm notice filename:      sham-ui-2.0.3.tgz
npm notice package size:  58.9 kB
npm notice unpacked size: 219.4 kB
npm notice shasum:        775fced5e6afdb1c20a962b5b833695a4da7dbc4
npm notice integrity:     sha512-OGZvHGDrJkR50[...]mHIrDL/KOhPrg==
npm notice total files:   6
npm notice
sham-ui-2.0.3.tgz
```
Т.е. теперь главное не забывать её выполнять перед `npm publish`.


