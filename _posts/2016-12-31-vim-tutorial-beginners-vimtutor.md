---
title: "Mastering Vim: A Practical Guide to vimtutor"
date: 2016-12-31 02:49:42 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/vim-tutorial-beginners-vimtutor/
---

vimtutor is the most practical way to learn Vim. It’s an interactive lesson built directly into your editor that teaches through practice rather than passive reading. You launch it from the terminal with no setup required, and you get immediate feedback on every command you type.

## Running vimtutor

From any terminal:

``` bash
vimtutor
```

This opens an interactive tutorial inside Vim itself. Budget 25–30 minutes to work through it, though actual time varies depending on how much you experiment with each lesson.

For a tutorial in a different language:

``` bash
vimtutor de     # German
vimtutor fr     # French
vimtutor zh     # Chinese (simplified)
vimtutor ru     # Russian
```

Run `vimtutor --help` to see all available languages on your system. The language codes follow your system’s locale settings.

## What You’ll Learn: Seven Lessons

The tutorial builds sequentially—each lesson assumes you’ve completed the previous one. Critical point: you must actually execute the commands. Reading alone doesn’t build muscle memory.

### Lesson 1: Movement and Basic Editing

Master cursor movement using `hjkl` (left, down, up, right). These keys keep your hands on the home row, though Vim accepts arrow keys too.

Essential editing commands:

    x              delete character under cursor
    i              insert before cursor
    a              append after cursor
    A              append at end of line
    :wq            write and quit
    :q!            quit without saving

### Lesson 2: Operators and Motions

Vim’s power comes from combining operators with motions. The pattern is `[operator][count][motion]`.

Common combinations:

    dw             delete word
    d$             delete to end of line
    dd             delete entire line
    2w             move forward two words
    d2w            delete two words
    cw             change word (delete and insert)
    c$             change to end of line
    yw             yank (copy) word
    y$             yank to end of line

Undo with `u`, redo with `Ctrl-R`. Vim maintains a full undo history—you can undo multiple times or navigate with `:undolist` for complex undo trees.

### Lesson 3: Putting and Replacing

After deleting or copying text, paste it back:

    p              paste after cursor
    P              paste before cursor
    r              replace single character
    R              replace mode (overwrite characters)

When you delete something with `d`, Vim stores it in a register. Paste it with `p` or `P`. The same applies to yanked text—copy with `y`, paste with `p`. Each register is independent, so you can store multiple text blocks simultaneously.

### Lesson 4: Navigation and Search

Jump around files efficiently:

    Ctrl-G         show file position and status
    G              jump to end of file
    gg             jump to start of file
    10G            jump to line 10
    :10            alternative: go to line 10
    /pattern       search forward
    ?pattern       search backward
    n              next match
    N              previous match
    %              jump to matching bracket or parenthesis
    *              search for word under cursor (forward)
    #              search for word under cursor (backward)

Search is case-sensitive by default. Make searches case-insensitive with `:set ignorecase` or use `/pattern\c` for a single case-insensitive search. The `:set smartcase` option makes searches case-sensitive only if your search pattern contains uppercase letters.

### Lesson 5: External Commands and File Operations

Run shell commands without leaving Vim:

    :!ls                    execute shell command
    :!rm filename           delete file via shell
    :w newfile.txt          write to new file
    :w !cat > output.txt    pipe buffer to command
    :r filename.txt         insert file contents
    :r !ls                  insert command output

Visual mode lets you select and work with text ranges. Press `v` to enter Visual mode, select text using motions, then perform an action:

    v{motion}:w file.txt    write selection to file
    v{motion}d              delete selection
    v{motion}y              copy selection
    v{motion}c              change selection

### Lesson 6: Text Manipulation

Insert new lines and switch modes:

    o              open line below, enter Insert mode
    O              open line above, enter Insert mode
    a              append after cursor
    R              Replace mode (overwrites as you type)
    v              Visual mode (character selection)
    V              Visual Line mode (full lines)
    Ctrl-V         Visual Block mode (rectangular regions)

Copy text with `y` (yank). It works with motions just like `d`:

    yw             yank word
    y$             yank to end of line
    yy             yank entire line

### Lesson 7: Help and Configuration

Access Vim’s built-in help:

    :help                  open help index
    :help subject          search help for topic
    :help motion           learn about motions
    :help operator         learn about operators
    Ctrl-W Ctrl-W          switch between help and buffer
    :q                     close help window

Create a `.vimrc` configuration file in your home directory to customize Vim:

``` bash
# Linux/macOS
~/.vimrc

# Windows
~/_vimrc
```

A minimal practical `.vimrc`:

```vim
set nocompatible       " disable legacy compatibility
set number             " show line numbers
set relativenumber     " show relative line numbers
set expandtab          " use spaces instead of tabs
set shiftwidth=4       " indent with 4 spaces
set tabstop=4          " display tabs as 4 spaces
set autoindent         " copy indent to new lines
set ignorecase         " ignore case in searches
set smartcase          " unless search contains uppercase
set hlsearch           " highlight search matches
set incsearch          " show matches while typing
syntax on              " enable syntax highlighting
set ruler              " show cursor position
set showcmd            " show incomplete commands
```

Use `:set option` to enable a setting, `:set nooption` to disable it. Changes made with `:set` apply only to the current session; add them to `.vimrc` to persist them across sessions.

## After Completing vimtutor

Explore deeper topics with these help commands:

    :help user-manual      comprehensive user guide
    :help motion           all movement commands
    :help operator         all operators
    :help cmdline          command-line features
    :help registers        understanding Vim's registers
    :help visual-mode      advanced visual mode usage
    :help macros           recording and playing macros

View example configurations:

    :echo $VIMRUNTIME      show Vim runtime directory

Then examine `$VIMRUNTIME/defaults.vim` for additional configuration ideas.

## Essential Commands for Productivity

Once comfortable with basics, these commands significantly boost your efficiency:

    .              repeat last command
    qa             start recording macro in register a
    q              stop recording
    @a             play macro from register a
    @@             repeat last macro
    Ctrl-A         increment number under cursor
    Ctrl-X         decrement number under cursor
    >              indent lines
    <              unindent lines
    J              join line below to current line
    ~              toggle case of character
    :set list      show invisible characters (tabs, line endings)
    :set wrap      enable word wrapping

Macros are particularly powerful. Record a sequence with `qa`, type your commands, then press `q` to stop. Play it back with `@a` or repeat with `@@`. This is how you automate repetitive editing tasks.

## Building Muscle Memory

The tutorial intentionally focuses on essentials. Vim has enormous depth—`man vim` and `:help` will keep you learning for years. The approach that actually works: learn one new command daily, use it in real work, and let repetition build automaticity. Vim rewards consistent daily use far more than cramming knowledge.

Start with vimtutor today. Spend 30 minutes on it. Then use Vim for actual work, consulting the help system as needed. Consistency matters more than comprehensiveness.
