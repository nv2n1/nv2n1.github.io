---
title: "lpc-cups(8)"
name: "lpc-cups"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lpc-cups/"
description: "lpc – line printer control program"
---

<p>lpc &#8211; line printer control program</p>
<h2>Synopsis</h2>
<p><code>lpc</code> [ <i>command</i> [ <i>parameter(s)</i> ] ]</p>
<h2>Description</h2>
<p><i>lpc</i> provides limited control over printer and class queues provided by CUPS. It can also be used to query the state of queues. </p>
<p> If no command is specified on the command-line, lpc will display a prompt and accept commands from the standard input.</p>
<h2>Commands</h2>
<p>The <i>lpc</i> program accepts a subset of commands accepted by the Berkeley <i>lpc</i> program of the same name:</p>
<dl>
<dt>exit</p>
<dd>Exits the command interpreter.</p>
<dt>help [command]</p>
<dd>
<dt>? [command]</p>
<dd>Displays a short help message.</p>
<dt>quit</p>
<dd>Exits the command interpreter.</p>
<dt>status [queue]</p>
<dd>Displays the status of one or more printer or class queues.</dl>
<h2>Limitations</h2>
<p>Since <i>lpc</i> is geared towards the Berkeley printing system, it is impossible to use <i>lpc</i> to configure printer or class queues provided by CUPS. To configure printer or class queues you must use the <i><a href="/docs/linux/man/8-lpadmin/">lpadmin</a>(8)</i> command or another CUPS-compatible client with that functionality.</p>
<h2>Compatibility</h2>
<p>The CUPS version of <i>lpc</i> does not implement all of the standard Berkeley or LPRng commands.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-cancel/">cancel</a>(1)</i>, <i><a href="/docs/linux/man/8-cupsaccept/">cupsaccept</a>(8)</i>, <i><a href="/docs/linux/man/8-cupsenable/">cupsenable</a>(8)</i>, <i><a href="/docs/linux/man/1-lp/">lp</a>(1)</i>, <i><a href="/docs/linux/man/1-lpr/">lpr</a>(1)</i>, <i><a href="/docs/linux/man/1-lprm/">lprm</a>(1)</i>, <i><a href="/docs/linux/man/1-lpstat/">lpstat</a>(1)</i>,<br />
 <a rel="nofollow" href="http://localhost:631/help">http://localhost:631/help</a></p>
<h2>Copyright</h2>
<p>Copyright 2007-2013 by Apple Inc.</p>
