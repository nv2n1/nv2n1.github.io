---
title: "wineboot-stable(1)"
name: "wineboot-stable"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wineboot-stable/"
description: "wineboot – perform Wine initialization, startup, and shutdown tasks"
---

<h2 class="name">NAME</h2>
<p> wineboot &#8211; perform Wine initialization, startup, and shutdown tasks </p>
<h2>SYNOPSIS</h2>
<p> <code>wineboot</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>wineboot</code> performs the initial creation and setup of a WINEPREFIX for <a href="/docs/linux/man/1-wine/">wine</a>(1). It can also perform a simulated reboot or shutdown to any applications running within the WINEPREFIX.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>,<code>&nbsp;&#8211;help</p>
<dd> Display help message.</p>
<dt>-e</code>,<code>&nbsp;&#8211;end-session</p>
<dd> End the current session cleanly.</p>
<dt>-f</code>,<code>&nbsp;&#8211;force</p>
<dd> Force exit for processes that don&#8217;t exit cleanly</p>
<dt>-i</code>,<code>&nbsp;&#8211;init</p>
<dd> Initialize the WINEPREFIX.</p>
<dt>-k</code>,<code>&nbsp;&#8211;kill</p>
<dd> Kill running processes without any cleanup.</p>
<dt>-r</code>,<code>&nbsp;&#8211;restart</p>
<dd> Restart only, don&#8217;t do normal startup operations.</p>
<dt>-s</code>,<code>&nbsp;&#8211;shutdown</p>
<dd> Shutdown only, don&#8217;t reboot.</p>
<dt>-u</code>,<code>&nbsp;&#8211;update</p>
<dd> Update the WINEPREFIX.</dl>
<p> </code></p>
<h2>BUGS</h2>
<p> Bugs can be reported on the <code>Wine bug tracker</code></p>
<h2>AVAILABILITY</h2>
<p> <code>wineboot</code> is part of the Wine distribution, which is available through WineHQ, the <code>Wine development headquarters</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wine/">wine</a></code>(1),<br />
 <code>Wine documentation and support</code> </p>
<h2>Index</h2>
