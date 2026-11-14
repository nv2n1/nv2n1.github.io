---
title: "onboard(1)"
name: "onboard"
section: "1"
letter: "o"
url: "/docs/linux/man/1-onboard/"
description: "onboard – On-screen Keyboard"
---

<h2 class="name">NAME</h2>
<p> onboard &#8211; On-screen Keyboard </p>
<h2>SYNOPSIS</h2>
<p> <code>onboard</code> [ <i>options</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>onboard</code> is an on-screen keyboard that can be useful for tablet PC users, as well as for mobility impaired people. </p>
<p> <code>onboard</code> supports macros, easy layout creation and word suggestion. </p>
<h2>OPTIONS</h2>
<p> <code>onboard</code> accepts the following command-line options:</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display a help with all available command line options and exit.</p>
<dt><code>-l &lt;LAYOUT&gt;, &#8211;layout=&lt;LAYOUT&gt;</code></p>
<dd> Layout file (.onboard) or name</p>
<dt><code>-t &lt;THEME&gt;, &#8211;theme=&lt;THEME&gt;</code></p>
<dd> Theme file (.theme) or name</p>
<dt><code>-x &lt;X&gt;</code></p>
<dd> Window x position</p>
<dt><code>-y &lt;Y&gt;</code></p>
<dd> Window y position</p>
<dt><code>-s &lt;SIZE&gt;, &#8211;size=&lt;SIZE&gt;</code></p>
<dd> Window size, widthxheight</p>
<dt><code>-e, &#8211;xid</code></p>
<dd> Start in XEmbed mode, e.g. for gnome-screensaver</p>
<dt><code>-a, &#8211;keep-aspect</code></p>
<dd> Keep aspect ratio when resizing the window</p>
<dt><code>-d &lt;DEBUG&gt;, &#8211;debug=&lt;DEBUG&gt;</code></p>
<dd> &lt;DEBUG&gt;={notset|debug|info|warning|error|critical}</p>
<dt><code>-m, &#8211;allow-multiple-instances</code></p>
<dd> Allow multiple Onboard instances</p>
<dt><code>-q &lt;QUIRKS&gt;, &#8211;quirks=&lt;QUIRKS&gt;</code></p>
<dd> Override auto-detection and manually select quirks QUIRKS={metacity|compiz|mutter}</p>
<dt><code>&#8211;not-show-in=&lt;DESKTOPS&gt;</code></p>
<dd> Silently fail to start in the given desktop environments. &lt;DESKTOPS&gt; is a comma-separated list of XDG desktop names, e.g. GNOME for GNOME Shell.</p>
<dt><code>-g, &#8211;log-learning</code></p>
<dd> log all learned text; off by default</dl>
<h2>SEE ALSO</h2>
<p> <code>/usr/share/doc/onboard</code></p>
<h2>AUTHOR</h2>
<p> This manual has been written by Mike Gabriel &lt;mike.gabriel [at] das-netzwerkteam.de&gt; by using the options from Config.py (see COPYING file for authors of options). It is distributed under the GPL-3+ license. </p>
<h2>Index</h2>
