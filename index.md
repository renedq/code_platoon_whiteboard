% Tips on Whiteboarding 
% Rene Duquesnoy 
% 

### Terminal/Shell

MacOS

- iTerm2

---

##### zsh

Alternative to bash

- Consolidated history
  - (Many terminals, one history)
- Visual tab completion
- Command autocorrection
- Many more features

http://go/whyz

http://zsh.sourceforge.net/

---

##### oh my zsh

A community-driven framework for managing your zsh configuration.

Hundreds of plugins to add features and functionality.

![](ohmy.png)

https://ohmyz.sh/

---

##### powerlevel10k

A theme for zsh that emphasizes **speed**, **flexibility**, and
**out-of-the-box experience**. Plus cools icons.

![](p10k.png)

https://github.com/romkatv/powerlevel10k

---

Vim:

1. is everywhere
2. is well documented
3. is very customizable and extensible
4. has portable configurations
5. isn't (system) resource intensive
6. supports all programming languages and file formats

---

Vim configuration basics:

1. Store all of your configuration files in source control
2. ...
3. Profit!

---

###### .vimrc

```vimrc
set nocompatible
filetype off    " Required

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'scrooloose/nerdtree'
Plugin 'tpope/vim-fugitive'
Plugin 'Xuyuanp/nerdtree-git-plugin'
Plugin 'ryanoasis/vim-devicons' " keep this one last
call vundle#end()            " required

filetype plugin indent on " Required
set nu
```

---

###### .vimrc

```vim
" persistent undo, save undo files in ~/.vim/undo
set undofile
set undodir=~/.vim/undo/
```

---

###### .vimrc

```vim
map <leader>b :buffers<cr>
" set some easy key mappings for switching buffers: when switching to a buffer
" above or below, completely expand it, shrinking all others maximally
nmap <c-k> <c-w>k<c-w>_
nmap <c-j> <c-w>j<c-w>_
" shorthand for switching to right/left buffers and maximizing vertically
nmap <c-l> <c-w>l<c-w>\|
nmap <c-h> <c-w>h<c-w>\|
" set a min window height/width for stacking windows
set wmh=0
set wmw=0
```

