---
title: "Setting Your Default Text Editor on Linux"
date: 2018-03-24 08:20:51 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-change-the-default-text-editor-on-linux/
---

When you run `crontab -e`, `git commit`, `visudo`, or similar commands, Linux applications need to know which text editor to launch. This is controlled by environment variables and system configuration, with several methods available depending on your needs.

## Understanding EDITOR and VISUAL

The `EDITOR` environment variable tells applications which text editor to use. A related variable, `VISUAL`, takes precedence in many tools (git, less, man). If neither is set, most tools fall back to `vi` or `nano`.

Check your current settings:

``` bash
echo $EDITOR
echo $VISUAL
```

If nothing prints, no explicit default is set.

## Set the Editor for Your Current Session

For temporary changes that last only until you close the terminal:

``` bash
export EDITOR=vim
export VISUAL=vim
```

Replace `vim` with your preferred editor (`nano`, `emacs`, `code`, `neovim`, etc.).

## Set the Editor Permanently for Your User

Add the export lines to your shell configuration file. For bash:

``` bash
echo 'export EDITOR=vim' >> ~/.bashrc
echo 'export VISUAL=vim' >> ~/.bashrc
```

For zsh (default on macOS and increasingly on Linux):

``` bash
echo 'export EDITOR=vim' >> ~/.zshrc
echo 'export VISUAL=vim' >> ~/.zshrc
```

Reload your shell configuration:

``` bash
source ~/.bashrc
# or
source ~/.zshrc
```

Or close and reopen your terminal.

If you use fish shell:

``` bash
set -Ux EDITOR vim
set -Ux VISUAL vim
```

The `-U` flag makes it universal (persistent across sessions).

## Set the Editor System-Wide

To set the default for all users, add it to `/etc/profile.d/` (the modular approach):

``` bash
sudo tee /etc/profile.d/editor.sh > /dev/null << EOF
export EDITOR=vim
export VISUAL=vim
EOF
```

This is cleaner than editing `/etc/profile` or `/etc/bashrc` directly, as it isolates the setting and doesn’t interfere with distribution updates.

## Using update-alternatives (Debian/Ubuntu)

Debian-based distributions provide `update-alternatives` for managing default programs:

``` bash
sudo update-alternatives --install /usr/bin/editor editor /usr/bin/vim 100
sudo update-alternatives --install /usr/bin/editor editor /usr/bin/nano 50
sudo update-alternatives --install /usr/bin/editor editor /usr/bin/code 90
```

The number at the end is the priority (higher wins in automatic mode). View the current selection:

``` bash
sudo update-alternatives --config editor
```

This method is cleaner than environment variables for system-wide defaults and integrates with package management — if you remove a package, the alternative is automatically cleaned up.

## Override the Editor for a Single Command

Test a different editor without changing your configuration:

``` bash
EDITOR=nano crontab -e
EDITOR=code git commit
```

This is useful for quick one-off changes or troubleshooting.

## Editors That Need Additional Flags

Some editors require flags to work correctly. VSCode and other GUI editors need the `--wait` flag to pause until you close the file:

``` bash
export EDITOR='code --wait'
export VISUAL='code --wait'
```

Without `--wait`, the editor launches and immediately returns control, causing issues with tools like git that expect the editor to block until you’re done.

For gedit:

``` bash
export EDITOR='gedit --standalone'
```

For emacs in terminal mode:

``` bash
export EDITOR='emacs -nw'
```

## Using Custom or Non-Standard Paths

If your editor isn’t in the system PATH, use the full path:

``` bash
export EDITOR=/opt/editors/myeditor/bin/editor
export VISUAL=/opt/editors/myeditor/bin/editor
```

Verify the path exists:

``` bash
which vim
# or
ls -l /usr/bin/vim
```

## Common Editors and Their Paths

| Editor  | Path                                     |
|---------|------------------------------------------|
| vim     | `/usr/bin/vim`                           |
| neovim  | `/usr/bin/nvim`                          |
| nano    | `/usr/bin/nano`                          |
| emacs   | `/usr/bin/emacs`                         |
| gedit   | `/usr/bin/gedit`                         |
| VS Code | `/usr/bin/code`                          |
| vi      | `/usr/bin/vi` (usually symlinked to vim) |

## Setting Both EDITOR and VISUAL

For maximum compatibility, set both variables. Some tools check `VISUAL` first (git, less, man), while others check `EDITOR`. Setting both ensures you get your preferred editor regardless:

``` bash
export VISUAL=vim
export EDITOR=vim
```

## Debugging Editor Issues

If your editor isn’t launching when expected:

1.  Verify the variable is set: `echo $EDITOR`
2.  Test the editor directly with an empty file: `$EDITOR /tmp/test.txt`
3.  Check that the path exists: `which $EDITOR` or `ls -l $(which $EDITOR)`
4.  Try setting `VISUAL` explicitly if `EDITOR` doesn’t work
5.  Some tools (like git) read from config files instead — check `git config core.editor`

For git specifically, configure it directly:

``` bash
git config --global core.editor vim
# or for a single repo
git config core.editor vim
```
