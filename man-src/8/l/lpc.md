---
title: "lpc(8)"
name: "lpc"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lpc/"
description: "lpc – line printer control program (deprecated)"
---

<p>lpc &#8211; line printer control program (deprecated)</p>
<h2>Synopsis</h2>
<p><code>lpc</code> [ <i>command</i> [ <i>parameter(s)</i> ] ]</p>
<h2>Description</h2>
<p><code>lpc</code> provides limited control over printer and class queues provided by CUPS. It can also be used to query the state of queues. </p>
<p> If no command is specified on the command-line, <code>lpc</code> displays a prompt and accepts commands from the standard input.</p>
<h3>Commands</h3>
<p>The <code>lpc</code> program accepts a subset of commands accepted by the Berkeley <code>lpc</code> program of the same name:</p>
<dl>
<dt><code>exit</code></p>
<dd>Exits the command interpreter.</p>
<dt><code>help </code>[<i>command</i>]</p>
<dd>
<dt><code>? </code>[<i>command</i>]</p>
<dd>Displays a short help message.</p>
<dt><code>quit</code></p>
<dd>Exits the command interpreter.</p>
<dt><code>status </code>[<i>queue</i>]</p>
<dd>Displays the status of one or more printer or class queues.</dl>
<h2>Notes</h2>
<p>This program is deprecated and will be removed in a future feature release of CUPS. </p>
<p> Since <code>lpc</code> is geared towards the Berkeley printing system, it is impossible to use <code>lpc</code> to configure printer or class queues provided by CUPS. To configure printer or class queues you must use the <code><a href="/docs/linux/man/8-lpadmin/">lpadmin</a></code>(8) command or another CUPS-compatible client with that functionality.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-cancel/">cancel</a></code>(1), <code><a href="/docs/linux/man/8-cupsaccept/">cupsaccept</a></code>(8), <code><a href="/docs/linux/man/8-cupsenable/">cupsenable</a></code>(8), <code><a href="/docs/linux/man/1-lp/">lp</a></code>(1), <code><a href="/docs/linux/man/8-lpadmin/">lpadmin</a></code>(8), <code><a href="/docs/linux/man/1-lpr/">lpr</a></code>(1), <code><a href="/docs/linux/man/1-lprm/">lprm</a></code>(1), <code><a href="/docs/linux/man/1-lpstat/">lpstat</a></code>(1), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2021-2022 by OpenPrinting.</p>
