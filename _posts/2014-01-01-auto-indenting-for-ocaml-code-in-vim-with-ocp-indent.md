---
title: "Setting Up OCaml Indentation in Vim with ocp-indent"
date: 2014-01-01 03:28:49 +0000
modified: 2026-04-12 16:31:23 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /auto-indenting-for-ocaml-code-in-vim-with-ocp-indent/
---

Vim’s default OCaml indentation is mediocre at best. The `ocp-indent` tool provides intelligent, syntax-aware indentation that respects OCaml conventions and integrates cleanly with Vim and Neovim.

## Installing ocp-indent

Install via opam:

``` bash
opam install ocp-indent
```

This installs the indentation engine and Vim plugin support. Verify the installation:

``` bash
which ocp-indent
```

## Configuring Vim

Add this to your `~/.vimrc` or `~/.config/nvim/init.vim`:

```vim
augroup ocaml_config
  autocmd!
  autocmd BufNewFile,BufRead *.ml,*.mli setfiletype ocaml
  autocmd FileType ocaml call SetupOCaml()
augroup END

function! SetupOCaml()
  setlocal textwidth=80
  setlocal colorcolumn=80
  setlocal shiftwidth=2
  setlocal tabstop=2
  setlocal softtabstop=2
  setlocal expandtab
  filetype indent on
  filetype plugin indent on

  " Load ocp-indent
  let opamshare = system('opam var share | tr -d "\n"')
  if isdirectory(opamshare)
    let ocp_indent_path = opamshare . '/vim/syntax/ocp-indent.vim'
    if filereadable(ocp_indent_path)
      execute 'source ' . ocp_indent_path
    endif
  endif
endfunction
```

Key points:

- Sets filetype detection for `.ml` and `.mli` files
- Uses 2-space indentation (OCaml standard)
- Expands tabs to spaces with `expandtab`
- Safely loads ocp-indent only if the file exists
- Uses `augroup` to prevent duplicate autocommands on reload

### For Neovim with plugin managers

If using `lazy.nvim`:

``` lua
{
  'ocaml/vim-ocaml',
  ft = { 'ocaml' },
  config = function()
    vim.opt_local.shiftwidth = 2
    vim.opt_local.tabstop = 2
    vim.opt_local.expandtab = true
  end,
}
```

Or with `vim-plug`:

```vim
Plug 'ocaml/vim-ocaml'
```

## Using ocp-indent

Once configured, indentation works automatically:

| Action | Command |
|----|----|
| Current line | `==` in normal mode |
| Visual selection | Select + `=` |
| Entire file | `gg=G` |
| Paragraph | `=ap` |
| Automatic | Triggers when you press Enter or type structural keywords (`if`, `let`, `match`, etc.) |

You can also reindent the entire buffer with:

```vim
:0,$!ocp-indent
```

This pipes the buffer through `ocp-indent` directly, useful for reformatting imported code.

## Configuring ocp-indent behavior

Create `~/.ocp/ocp-indent.conf` to customize rules:

    JaneStreet
    indent_with_tabs = false
    indent_comments = true
    strict_comments = false

Available profiles:

- `normal` — Standard OCaml indentation
- `apprentice` — Conservative indentation
- `JaneStreet` — Jane Street style guide (good default for most projects)

## Troubleshooting

**ocp-indent not loading:**

Check that opam is initialized:

``` bash
eval $(opam env)
```

Verify the opam share path exists:

``` bash
opam var share
```

If empty, run:

``` bash
opam init
```

**Conflicting indentation settings:**

Remove any duplicate indentation configs in your vimrc. Ensure `filetype plugin indent on` appears after loading ocp-indent. Check for conflicting plugins with:

```vim
:scriptnames
```

**Indentation still looks wrong:**

Verify ocp-indent is being sourced:

```vim
:echo exists('*ocp_indent#indent')
```

Should return `1`. If `0`, the plugin didn’t load. Check the file exists at:

``` bash
cat $(opam var share)/vim/syntax/ocp-indent.vim
```

**For Neovim specifically:**

If using a plugin manager, ensure the `vim-ocaml` plugin loads before other OCaml-related plugins. Check LSP client settings aren’t overriding indentation behavior.

## 2026 Best Practices and Advanced Techniques

For Setting Up OCaml Indentation in Vim with ocp-indent, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
