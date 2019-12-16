---
title: "Git"
date: 2019-12-12T22:57:44+05:30
 
weight: 999
---

{{% children depth="3" sort="weight" %}}

#### 1. Squash multiple git commit into one

- check how much commit you want to squash.
```
    git log -<n>
```
- rebase head with particular commit.
```
    git rebase -i HEAD~<n>
```
- change n-1 commit from  pick to squash(s).
- save file and again add commit message.
- force push head branch
```
    git push -f origin head
```

#### 2. amend a new commit in last commit
- amend a new changes in last commit
```
    git commit --amend
    git push -u origin head
```

#### 3. cherry pick 
* Cherry picking in Git means to choose a commit from one branch and apply it onto another.
- Make sure you are on the branch you want to apply the commit to.
```
git checkout master
```
Execute the following:
```
git cherry-pick <commit-hash>
```
