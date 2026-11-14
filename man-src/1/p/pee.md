---
title: "pee(1)"
name: "pee"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pee/"
description: "pee – tee standard input to pipes"
---

<h2 class="name">NAME</h2>
<p> pee &#8211; tee standard input to pipes </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pee</code> [&#8211;[no-]ignore-sigpipe] [&#8211;[no-]ignore-write-errors] [[<i>&quot;command&quot;</i>&#8230;]]</dl>
<h2>DESCRIPTION</h2>
<p> <code>pee</code></p>
<dd>is like <code>tee</code> but for pipes. Each command is run and fed a copy of the standard input. The output of all commands is sent to stdout. </p>
<p> Note that while this is similar to <code>tee</code>, a copy of the input is not sent to stdout, like tee does. If that is desired, use <code>pee cat &#8230;</code></p>
<h2>OPTIONS</h2>
<p> <code>&#8211;ignore-sigpipe</code>, <code>&#8211;no-ignore-sigpipe</code></p>
<dl>
<dt>
<dd> Do (not) ignore SIGPIPE. Any command started by <code>pee</code> might cause a SIGPIPE when it exists. If you ignore SIGPIPE, you probably also want to ignore write errors (see below). Ignoring SIGPIPE is the default behaviour.</dl>
<p> <code>&#8211;ignore-write-errors</code>, <code>&#8211;no-ignore-write-errors</code></p>
<dl>
<dt>
<dd> Do (not) ignore write errors. When a command started by <code>pee</code> is no more accepting data via the pipe between itself and <code>pee</code>, a write error occurs in <code>pee</code>. If this error is not ignored, <code>pee</code> is going to terminate all child processes and exists. Ignoring write errors is the default behaviour.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tee/">tee</a></code>(1), <code><a href="/docs/linux/man/7-pipe/">pipe</a></code>(7)</p>
<h2>AUTHOR</h2>
<p> Miek Gieben </p>
<h2>Index</h2>
