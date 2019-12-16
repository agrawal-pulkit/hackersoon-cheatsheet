---
title: "Tumx+iterm"
date: 2019-12-11T11:38:14+05:30
 
weight: 60
---

{{% children depth="3" sort="weight" %}}

#### Tmux 
to use Tmux with Iterm2, you only need to provide an extra option (-CC) for Tmux commands:

    # create a new session*
    tmux -CC 
    
    # create a new tmux session*
    tmux new -s <session-name>
    
    # attach to a session*
    tmux -CC a -t <session-name> 
    
#### iterm2 best cheat sheet
 [https://gist.github.com/squarism/ae3613daf5c01a98ba3a](https://gist.github.com/squarism/ae3613daf5c01a98ba3a)
 
 
#### tmux cheatsheet
 [https://devhints.io/tmux](https://devhints.io/tmux)
