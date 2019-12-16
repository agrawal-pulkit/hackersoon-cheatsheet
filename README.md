# hackersoon-cheatsheet

```
brew install go

brew install hugo

git submodule init

git submodule update

```

run hugo server in local
```
hugo server -D
```

before pushing to git generate public folder
```
hugo -D
```

create a new chapter
```
hugo new --kind chapter <name>/_index.md
```

create a new page
```
hugo new <chapter>/<name>/_index.md
```
