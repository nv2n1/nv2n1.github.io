---
title: "mispipe(1)"
name: "mispipe"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mispipe/"
description: "mispipe – pipe two commands, returning the exit status of the first"
---

<h2 class="name">NAME</h2>
<p> mispipe &#8211; pipe two commands, returning the exit status of the first </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mispipe</code> [<i>&quot;command1&quot;</i>] [<i>&quot;command2&quot;</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>mispipe</code></p>
<dd>pipes two commands together like the shell does, but unlike piping in the shell, which returns the exit status of the last command; when using mispipe, the exit status of the first command is returned. </p>
<p> Note that some shells, notably <code>bash</code>, do offer a pipefail option, however, that option does not behave the same since it makes a failure of any command in the pipeline be returned, not just the exit status of the first.</p>
<h2>EXIT STATUS</h2>
<p> The exit status of the first command. If the process terminated abnormally (due to a signal), 128 will be added to its exit status.</p>
<h2>AUTHOR</h2>
<p> Nathanael Nerode </p>
<h2>Index</h2>
