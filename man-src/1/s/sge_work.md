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
<dt><code>-f</code> <i>n</i></dt>
<dd> Do work <i>n</i> times using <i>n</i> processes, default 1 process</dd>
<dt><code>-w</code> <i>n</i></dt>
<dd> Work <i>n</i> seconds, default 100 seconds</dd>
<dt><code>-in</code> <i>fname</i></dt>
<dd> Read from file <i>fname</i></dd>
<dt><code>-out</code> <i>fname</i></dt>
<dd> Write to file <i>fname</i></dd>
<dt><code>-stackK</code> <i>n</i></dt>
<dd> Force stack size with at least <i>n</i> KB</dd>
<dt><code>-stackM</code> <i>n</i></dt>
<dd> Force stack size with at least <i>n</i> MB</dd>
<dt><code>-mallocK</code> <i>n</i></dt>
<dd> Force <i><a href="/docs/linux/man/3-malloc/">malloc</a></i>(3) with <i>n</i> KB</dd>
<dt><code>-mallocM</code> <i>n</i></dt>
<dd> Force <i><a href="/docs/linux/man/3-malloc/">malloc</a></i>(3) with <i>n</i> MB</dd>
<dt><code>-block_sigxcpu</code></dt>
<dd> Ignore signal SIGXCPU</dd>
<dt><code>-block_sigxfsz</code></dt>
<dd> Ignore signal SIGXFSZ</dd>
<dt><code>-change_pgrp</code></dt>
<dd> Change process group</dd>
<dt><code>-daemonize</code></dt>
<dd> Daemonize</dd></dl>
<h2>SEE ALSO</h2>
