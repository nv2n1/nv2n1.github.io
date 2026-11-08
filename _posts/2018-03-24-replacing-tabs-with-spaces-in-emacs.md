---
title: "Converting Tabs to Spaces in Emacs"
date: 2018-03-24 11:40:31 +0000
layout: post
canonical: https://www.systutorials.com/replacing-tabs-with-spaces-in-emacs/
---

The simplest approach is to select text and run `untabify`:

    M-x untabify

This replaces all tabs in the selected region with spaces, preserving column alignment. If no region is active, Emacs prompts you to define one.

## Convert the Entire Buffer

Select all content, then run `untabify`:

    C-x h M-x untabify

`C-x h` selects the whole buffer. If you prefer `C-a`, note that it moves point to the start without selecting—use `C-a C-x C-x` to mark from start to end instead.

## Convert Spaces Back to Tabs

Use `tabify` to reverse the process:

    M-x tabify

This converts runs of consecutive spaces into tabs when it won’t alter indentation. It’s useful if you need to restore tabs for compatibility with legacy codebases, though most modern projects prefer spaces.

## Default to Spaces for All New Files

Add this to your Emacs config (`~/.emacs.d/init.el` or `~/.emacs`):

```elisp
(setq-default indent-tabs-mode nil)
```

This globally sets indentation to spaces. For specific modes, use a hook:

```elisp
(add-hook 'python-mode-hook (lambda () (setq indent-tabs-mode nil)))
(add-hook 'rust-mode-hook (lambda () (setq indent-tabs-mode nil)))
```

## Visualize Tabs and Spaces

Enable `whitespace-mode` to see which whitespace characters are in use:

    M-x whitespace-mode

Tabs appear as arrows or block markers; spaces remain invisible by default. Toggle it on and off as needed. For persistent visualization, add to your config:

```elisp
(add-hook 'prog-mode-hook #'whitespace-mode)
```

## Set Indentation Per File

Use file-local variables at the end of your file to override global settings:

    # Local Variables:
    # indent-tabs-mode: nil
    # tab-width: 4
    # End:

(Use the appropriate comment syntax for your language—`//` for C, `--` for Lua, etc.)

Emacs prompts you to apply these settings when opening or saving. This is essential when collaborating on projects with mixed indentation standards.

## Batch Convert Files Outside Emacs

For multiple files, use `expand` or `sed` from the command line:

``` bash
expand -t 4 input.txt > output.txt
```

The `-t` flag sets tab width (default is 8). For in-place conversion across multiple files:

``` bash
find . -name "*.py" -type f -exec sed -i 's/\t/    /g' {} +
```

This replaces each tab with four spaces in all Python files recursively. Adjust the pattern and spaces to match your project’s style guide.

For more complex scenarios—like preserving indentation consistency across a codebase—consider using tools like `black` (Python) or `rustfmt` (Rust), which handle formatting automatically and eliminate tab-versus-space debates altogether.

## Essential Editor Configuration

A well-configured editor dramatically improves productivity. For Vim users, invest time in crafting a solid vimrc. For Emacs users, use use-package for cleaner configuration management. Both editors support extensive plugin ecosystems that can transform them into full IDEs.

Learn the navigation commands thoroughly before adding plugins. Mastery of core movement commands (word, paragraph, search motions in Vim; mark, isearch, ace-jump in Emacs) provides more productivity gains than any single plugin.

## Performance Tips

Large files can slow down both editors. For Vim, set lazyredraw and disable syntax highlighting for files over a certain size. For Emacs, use so-long-mode for files with long lines. Both editors benefit from disabling line numbers on very large files to improve scrolling performance.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
