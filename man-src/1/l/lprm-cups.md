---
title: "lprm-cups(1)"
name: "lprm-cups"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lprm-cups/"
description: "lprm – cancel print jobs"
---

<h2>NAME</h2>
<p> lprm &#8211; cancel print jobs</p>
<h2>SYNOPSIS</h2>
<p> <code>lprm</code> [ -E ] [ -U <i>username</i> ] [ -h <i>server[:port]</i> ] [ -P <i>destination[/instance]</i> ] [ &#8211; ] [ <i>job ID(s)</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>lprm</i> cancels print jobs that have been queued for printing. If no arguments are supplied, the current job on the default destination is cancelled. You can specify one or more job ID numbers to cancel those jobs or use the <i>&#8211;</i> option to cancel all jobs.</p>
<h2>OPTIONS</h2>
<p> The <i>lprm</i> command supports the following options:</p>
<dl>
<dt>-E</p>
<dd>
 Forces encryption when connecting to the server.</p>
<dt>-P destination[/instance]</p>
<dd>
 Specifies the destination printer or class.</p>
<dt>-U username</p>
<dd>
 Specifies an alternate username.</p>
<dt>-h server[:port]</p>
<dd>
 Specifies an alternate server.</dl>
<h2>COMPATIBILITY</h2>
<p> The CUPS version of <i>lprm</i> is compatible with the standard Berkeley <i>lprm</i> command.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-cancel/">cancel</a>(1)</i>, <i><a href="/docs/linux/man/1-lp/">lp</a>(1)</i>, <i><a href="/docs/linux/man/1-lpq/">lpq</a>(1)</i>, <i><a href="/docs/linux/man/1-lpr/">lpr</a>(1)</i>, <i><a href="/docs/linux/man/1-lpstat/">lpstat</a>(1)</i>,<br />
 <a rel="nofollow" href="http://localhost:631/help">http://localhost:631/help</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright 2007-2013 by Apple Inc. </p>
<h2>Index</h2>
