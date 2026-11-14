---
title: "accept(8)"
name: "accept"
section: "8"
letter: "a"
url: "/docs/linux/man/8-accept/"
description: "cupsaccept/cupsreject – accept/reject jobs sent to a destination"
---

<p>cupsaccept/cupsreject &#8211; accept/reject jobs sent to a destination</p>
<h2>Synopsis</h2>
<p><code>cupsaccept</code> [ <code>-E</code> ] [ <code>-U</code> <i>username</i> ] [ <code>-h</code> <i>hostname[:port]</i> ] <i>destination(s)</i><br />
 <code>cupsreject</code> [ <code>-E</code> ] [ <code>-U</code> <i>username</i> ] [ <code>-h</code> <i>hostname[:port]</i> ] [ <code>-r</code> <i>reason</i> ] <i>destination(s)</i></p>
<h2>Description</h2>
<p>The <code>cupsaccept</code> command instructs the printing system to accept print jobs to the specified destinations. </p>
<p> The <code>cupsreject</code> command instructs the printing system to reject print jobs to the specified destinations. The <i>-r</i> option sets the reason for rejecting print jobs. If not specified, the reason defaults to &quot;Reason Unknown&quot;.</p>
<h2>Options</h2>
<p>The following options are supported by both <code>cupsaccept</code> and <code>cupsreject</code>:</p>
<dl>
<dt><code>-E</code></p>
<dd>Forces encryption when connecting to the server.</p>
<dt><code>-U </code><i>username</i></p>
<dd>Sets the username that is sent when connecting to the server.</p>
<dt><code>-h </code><i>hostname[:port]</i></p>
<dd>Chooses an alternate server.</p>
<dt><code>-r </code>&quot;<i>reason</i>&quot;</p>
<dd>Sets the reason string that is shown for a printer that is rejecting jobs.</dl>
<h2>Conforming To</h2>
<p>The <code>cupsaccept</code> and <code>cupsreject</code> commands correspond to the System V printing system commands &quot;accept&quot; and &quot;reject&quot;, respectively. Unlike the System V printing system, CUPS allows printer names to contain any printable character except SPACE, TAB, &quot;/&quot;, or &quot;#&quot;. Also, printer and class names are <i>not</i> case-sensitive. </p>
<p> Finally, the CUPS versions may ask the user for an access password depending on the printing system configuration.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-cancel/">cancel</a></code>(1), <code><a href="/docs/linux/man/8-cupsenable/">cupsenable</a></code>(8), <code><a href="/docs/linux/man/1-lp/">lp</a></code>(1), <code><a href="/docs/linux/man/8-lpadmin/">lpadmin</a></code>(8), <code><a href="/docs/linux/man/1-lpstat/">lpstat</a></code>(1),<br />
 CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2007-2017 by Apple Inc.</p>
