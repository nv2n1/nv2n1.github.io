---
title: "pyflakes-2-7(1)"
name: "pyflakes-2-7"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pyflakes-2-7/"
description: "pyflakes – simple Python 2 source checker"
---

<p>pyflakes &#8211; simple Python 2 source checker </p>
<h2>Synopsis</h2>
<p><code>pyflakes</code> [<i>file-or-directory</i> &#8230;]</p>
<h2>Description</h2>
<p>pyflakes is a simple program which checks Python source files for errors. It is similar to PyChecker in scope, but differs in that it does not execute the modules to check them. This is both safer and faster, although it does not perform as many checks. Unlike PyLint, Pyflakes checks only for logical errors in programs; it does not perform any checks on style. </p>
<p> All commandline arguments are checked, which have to be either regular files or directories. If a directory is given, every <code>.py</code> file within will be checked. </p>
<p> When no commandline arguments are given, data will be read from standard input.</p>
<h2>Output</h2>
<p>Found warnings including unused imports, undefined variables and unnecessary reimports, are printed on standard output. Found errors including compile or encoding errors, are printed on standard error.</p>
<h2>Exit Status</h2>
<p>The exit status is 0 when no warnings or errors are found. Otherwise the exit status is 1.</p>
<h2>Author</h2>
<p>This manual page was originally written by Bastian Kleineidam &lt;calvin [at] debian.org&gt; for the Debian distribution of pyflakes (but can be used by others).</p>
