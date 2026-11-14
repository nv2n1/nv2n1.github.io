---
title: "lpq-cups(1)"
name: "lpq-cups"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lpq-cups/"
description: "lpq – show printer queue status"
---

<h2>NAME</h2>
<p> lpq &#8211; show printer queue status</p>
<h2>SYNOPSIS</h2>
<p> <code>lpq</code> [ -E ] [ -U <i>username</i> ] [ -h <i>server[:port]</i> ] [ -P <i>destination[/instance]</i> ] [ -a ] [ -l ] [ <i>+interval</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>lpq</i> shows the current print queue status on the named printer. Jobs queued on the default destination will be shown if no printer or class is specified on the command-line. </p>
<p> The <i>+interval</i> option allows you to continuously report the jobs in the queue until the queue is empty; the list of jobs is shown once every <i>interval</i> seconds.</p>
<h2>OPTIONS</h2>
<p> <i>lpq</i> supports the following options:</p>
<dl>
<dt>-E</p>
<dd>
 Forces encryption when connecting to the server.</p>
<dt>-P destination[/instance]</p>
<dd>
 Specifies an alternate printer or class name.</p>
<dt>-U username</p>
<dd>
 Specifies an alternate username.</p>
<dt>-a</p>
<dd>
 Reports jobs on all printers.</p>
<dt>-h server[:port]</p>
<dd>
 Specifies an alternate server.</p>
<dt>-l</p>
<dd>
 Requests a more verbose (long) reporting format.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-cancel/">cancel</a>(1)</i>, <i><a href="/docs/linux/man/1-lp/">lp</a>(1)</i>, <i><a href="/docs/linux/man/1-lpr/">lpr</a>(1)</i>, <i><a href="/docs/linux/man/1-lprm/">lprm</a>(1)</i>, <i><a href="/docs/linux/man/1-lpstat/">lpstat</a>(1)</i>,<br />
 <a rel="nofollow" href="http://localhost:631/help">http://localhost:631/help</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright 2007-2013 by Apple Inc. </p>
<h2>Index</h2>
