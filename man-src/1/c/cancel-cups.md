---
title: "cancel-cups(1)"
name: "cancel-cups"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cancel-cups/"
description: "cancel – cancel jobs"
---

<h2>NAME</h2>
<p> cancel &#8211; cancel jobs</p>
<h2>SYNOPSIS</h2>
<p> <code>cancel</code> [ -E ] [ -U <i>username</i> ] [ -a ] [ -h <i>hostname[:port]</i> ] [ -u <i>username</i> ] [ <i>id</i> ] [ <i>destination</i> ] [ <i>destination-id</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>cancel</i> cancels existing print jobs. The <i>-a</i> option will remove all jobs from the specified destination.</p>
<h2>OPTIONS</h2>
<p> The following options are recognized by <i>cancel</i>:</p>
<dl>
<dt>-E</p>
<dd>
 Forces encryption when connecting to the server.</p>
<dt>-U username</p>
<dd>
 Specifies the username to use when connecting to the server.</p>
<dt>-a</p>
<dd>
 Cancel all jobs on the named destination, or all jobs on all destinations if none is provided.</p>
<dt>-h hostname[:port]</p>
<dd>
 Chooses an alternate server.</p>
<dt>-u username</p>
<dd>
 Cancels jobs owned by <i>username</i>.</dl>
<h2>COMPATIBILITY</h2>
<p> Unlike the System V printing system, CUPS allows printer names to contain any printable character except SPACE, TAB, &quot;/&quot;, or &quot;#&quot;. Also, printer and class names are <i>not</i> case-sensitive.</p>
<h2>NOTES</h2>
<p> Administrators wishing to prevent unauthorized cancellation of jobs via the <i>-u</i> option should require authentication for Cancel-Jobs operations in <i><a href="/docs/linux/man/5-cupsd-conf/">cupsd.conf</a>(5)</i>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-lp/">lp</a>(1)</i>, <i><a href="/docs/linux/man/8-lpmove/">lpmove</a>(8)</i>, <i><a href="/docs/linux/man/1-lpstat/">lpstat</a>(1)</i>,<br />
 <a rel="nofollow" href="http://localhost:631/help">http://localhost:631/help</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright 2007-2013 by Apple Inc. </p>
<h2>Index</h2>
