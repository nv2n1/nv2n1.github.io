---
title: "sge_work(1)"
name: "sge_work"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sge_work/"
description: "work – do some work for testing purposes"
---

<h2 class="name">NAME</h2>
<p> work &#8211; do some work for testing purposes</p>
<h2>SYNTAX</h2>
<p> <code>$SGE_ROOT/utilbin/$ARCH/work</code> [<code>-f</code> <i>n</i>] [<code>-w</code> <i>n</i>] [<code>-in</code> <i>fname</i>] [<code>-out</code> <i>fname</i>] [<code>-stackK</code> <i>n</i>] [<code>-stackM</code> <i>n</i>] [<code>-mallocK</code> <i>n</i>] [<code>-mallocM</code> <i>n</i>] [<code>-block_sigxcpu</code>] [<code>-block_sigxfsz</code>] [<code>-change_pgrp</code>] [<code>-daemonize</code>] <code>-daemonize</code> ]</p>
<h2>DESCRIPTION</h2>
<p> This is a utility program intended to be run under xxQS_NAMExx for testing purposes. It can, for instance, run for a certain amount of time, allocate a certain amount of memory, fork, and daemonize.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code> <i>n</i></p>
<dd> Do work <i>n</i> times using <i>n</i> processes, default 1 process</p>
<dt><code>-w</code> <i>n</i></p>
<dd> Work <i>n</i> seconds, default 100 seconds</p>
<dt><code>-in</code> <i>fname</i></p>
<dd> Read from file <i>fname</i></p>
<dt><code>-out</code> <i>fname</i></p>
<dd> Write to file <i>fname</i></p>
<dt><code>-stackK</code> <i>n</i></p>
<dd> Force stack size with at least <i>n</i> KB</p>
<dt><code>-stackM</code> <i>n</i></p>
<dd> Force stack size with at least <i>n</i> MB</p>
<dt><code>-mallocK</code> <i>n</i></p>
<dd> Force <i><a href="/docs/linux/man/3-malloc/">malloc</a></i>(3) with <i>n</i> KB</p>
<dt><code>-mallocM</code> <i>n</i></p>
<dd> Force <i><a href="/docs/linux/man/3-malloc/">malloc</a></i>(3) with <i>n</i> MB</p>
<dt><code>-block_sigxcpu</code></p>
<dd> Ignore signal SIGXCPU</p>
<dt><code>-block_sigxfsz</code></p>
<dd> Ignore signal SIGXFSZ</p>
<dt><code>-change_pgrp</code></p>
<dd> Change process group</p>
<dt><code>-daemonize</code></p>
<dd> Daemonize</dl>
<h2>SEE ALSO</h2>
<h2>Index</h2>
