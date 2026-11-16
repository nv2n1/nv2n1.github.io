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
<dt><code>-h, &#8211;help</code></dt>
<dd> Display a help with all available command line options and exit.</dd>
<dt><code>-l &lt;LAYOUT&gt;, &#8211;layout=&lt;LAYOUT&gt;</code></dt>
<dd> Layout file (.onboard) or name</dd>
<dt><code>-t &lt;THEME&gt;, &#8211;theme=&lt;THEME&gt;</code></dt>
<dd> Theme file (.theme) or name</dd>
<dt><code>-x &lt;X&gt;</code></dt>
<dd> Window x position</dd>
<dt><code>-y &lt;Y&gt;</code></dt>
<dd> Window y position</dd>
<dt><code>-s &lt;SIZE&gt;, &#8211;size=&lt;SIZE&gt;</code></dt>
<dd> Window size, widthxheight</dd>
<dt><code>-e, &#8211;xid</code></dt>
<dd> Start in XEmbed mode, e.g. for gnome-screensaver</dd>
<dt><code>-a, &#8211;keep-aspect</code></dt>
<dd> Keep aspect ratio when resizing the window</dd>
<dt><code>-d &lt;DEBUG&gt;, &#8211;debug=&lt;DEBUG&gt;</code></dt>
<dd> &lt;DEBUG&gt;={notset|debug|info|warning|error|critical}</dd>
<dt><code>-m, &#8211;allow-multiple-instances</code></dt>
<dd> Allow multiple Onboard instances</dd>
<dt><code>-q &lt;QUIRKS&gt;, &#8211;quirks=&lt;QUIRKS&gt;</code></dt>
<dd> Override auto-detection and manually select quirks QUIRKS={metacity|compiz|mutter}</dd>
<dt><code>&#8211;not-show-in=&lt;DESKTOPS&gt;</code></dt>
<dd> Silently fail to start in the given desktop environments. &lt;DESKTOPS&gt; is a comma-separated list of XDG desktop names, e.g. GNOME for GNOME Shell.</dd>
<dt><code>-g, &#8211;log-learning</code></dt>
<dd> log all learned text; off by default</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>/usr/share/doc/onboard</code></p>
<h2>AUTHOR</h2>
<p> This manual has been written by Mike Gabriel &lt;mike.gabriel [at] das-netzwerkteam.de&gt; by using the options from Config.py (see COPYING file for authors of options). It is distributed under the GPL-3+ license. </p>
<h2>Index</h2>
