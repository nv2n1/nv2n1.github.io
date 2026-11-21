---

title: "xvinfo(1)"
name: "xvinfo"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xvinfo/"
description: "xvinfo – Print out X-Video extension adaptor information"
---

<p> xvinfo &#8211; Print out X-Video extension adaptor information </p>
<h2>SYNOPSIS</h2>
<p> <code>xvinfo</code> [-display <i>displayname</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>xvinfo</code> prints out the capabilities of any video adaptors associated with the display that are accessible through the X-Video extension.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-display </code><i>display</i></dt>
<dd> This argument allows you to specify the server to query; see <i><a href="/docs/linux/man/7-x/">X</a>(7)</i>.</dd>
<dt><code>-short</code></dt>
<dd> Output less details, to reduce the amount of text.</dd>
<dt><code>-version</code></dt>
<dd> Output program version, then exit.</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></dt>
<dd> This variable may be used to specify the server to query. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xdpyinfo/">xdpyinfo</a>(1), <a href="/docs/linux/man/1-xwininfo/">xwininfo</a>(1), <a href="/docs/linux/man/1-xdriinfo/">xdriinfo</a>(1), <a href="/docs/linux/man/1-glxinfo/">glxinfo</a>(1), <a href="/docs/linux/man/1-xprop/">xprop</a>(1)</p>
<h2>AUTHORS</h2>
<p> Mark Vojkovich </p>
