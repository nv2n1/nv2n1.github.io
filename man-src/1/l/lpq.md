---
title: "lpq(1)"
name: "lpq"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lpq/"
description: "lpq – show printer queue status"
---

<h2 class="name">NAME</h2>
<p> lpq &#8211; show printer queue status </p>
<h2>SYNOPSIS</h2>
<p> <code>lpq</code> [ <code>-E</code> ] [ <code>-U</code> <i>username</i> ] [ <code>-h </code><i>server</i>[<code>:</code><i>port</i>] ] [ <code>-P </code><i>destination</i>[<code>/</code><i>instance</i>] ] [ <code>-a</code> ] [ <code>-l</code> ] [ <code>+</code><i>interval</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>lpq</code> shows the current print queue status on the named printer. Jobs queued on the default destination will be shown if no printer or class is specified on the command-line. </p>
<p> The <i>+interval</i> option allows you to continuously report the jobs in the queue until the queue is empty; the list of jobs is shown once every <i>interval</i> seconds.</p>
<h2>OPTIONS</h2>
<p> <code>lpq</code> supports the following options:</p>
<dl>
<dt><code>-E</code></p>
<dd> Forces encryption when connecting to the server.</p>
<dt><code>-P </code><i>destination</i>[<code>/</code><i>instance</i>]</p>
<dd> Specifies an alternate printer or class name.</p>
<dt><code>-U </code><i>username</i></p>
<dd> Specifies an alternate username.</p>
<dt><code>-a</code></p>
<dd> Reports jobs on all printers.</p>
<dt><code>-h </code><i>server</i>[<code>:</code><i>port</i>]</p>
<dd> Specifies an alternate server.</p>
<dt><code>-l</code></p>
<dd> Requests a more verbose (long) reporting format.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cancel/">cancel</a></code>(1), <code><a href="/docs/linux/man/1-lp/">lp</a></code>(1), <code><a href="/docs/linux/man/1-lpr/">lpr</a></code>(1), <code><a href="/docs/linux/man/1-lprm/">lprm</a></code>(1), <code><a href="/docs/linux/man/1-lpstat/">lpstat</a></code>(1), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021-2022 by OpenPrinting. </p>
<h2>Index</h2>
