---
title: "fbsetroot(1)"
name: "fbsetroot"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fbsetroot/"
description: "fbsetroot – a simple background utility used by the"
---

<h2 class="name">NAME</h2>
<p> fbsetroot &#8211; a simple background utility used by the </p>
<p><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) window manager, originally written for and by the original <a href="/docs/linux/man/1-blackbox/">blackbox</a>(1) window manager.</p>
<h2>SYNOPSIS</h2>
<p> <code>fbsetroot</code> [-display <i>display</i>] -solid <i>color</i> </p>
<p> <code>fbsetroot</code> [-display <i>display</i>] -mod <i>x</i> <i>y</i> -fg <i>color</i> -bg <i>color</i> </p>
<p> <code>fbsetroot</code> [-display <i>display</i>] -gradient <i>texture</i> -from <i>color</i> -to <i>color</i> </p>
<p> <code>fbsetroot</code> -help</p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-fbsetroot/">fbsetroot</a>(1)</code> is a utility that can control the appearance of the root window in three ways: Either give it a solid color, or write a two color modula pattern to it, or render a gradient texture, based on two different colors. </p>
<p> fbsetroot resembles <code><a href="/docs/linux/man/1-xsetroot/">xsetroot</a>(1)</code> in this functionality but it supports multiple-screen displays, and gradient textures the same way as blackbox or fluxbox does. It doesn&#8217;t handle cursors etc. fbsetroot was originally part of the Blackbox package and was carried over with the code that became Fluxbox. It was called bsetroot back in those days. </p>
<p> If any errors are encountered, fbsetroot will use either <code><a href="/docs/linux/man/1-gxmessage/">gxmessage</a>(1)</code> or <code><a href="/docs/linux/man/1-xmessage/">xmessage</a>(1)</code> to inform the user of errors.</p>
<h2>OPTIONS</h2>
<p> fbsetroot operates in three ways, you must choose one of the first 3 options: </p>
<p> <code>-solid</code> <i>color</i></p>
<dl>
<dt>
<dd> Sets the root window to specified color.</dl>
<p> <code>-mod</code> <i>x</i> <i>y</i></p>
<dl>
<dt>
<dd> Creates a modula pattern. You must specify <code>-bg</code> and <code>-fg</code> colors.</dl>
<p> <code>-gradient</code> <i>texturestring</i></p>
<dl>
<dt>
<dd> Renders the specified texture string to the root window. </p>
<p> <i>texturestring</i> may be one of:</p>
<dl>
<dt>
<dd> <code>Horizontal / Vertical / Diagonal / Crossdiagonal / Pipecross / Elliptic / Rectangle / Pyramid</code> </p>
<p> Select one of these texture types, they only apply when <code>-gradient</code> is specified. You must also specify both a <code>-from</code> and a <code>-to</code> color.</dl>
</dl>
<p> <code>-display</code> <i>display</i></p>
<dl>
<dt>
<dd> Tells fbsetroot to connect to the specified display.</dl>
<p> <code>-bg, -background</code> <i>color</i></p>
<dl>
<dt>
<dd> Background color. Needed for <code>-mod</code> patterns.</dl>
<p> <code>-fg, -foreground</code> <i>color</i></p>
<dl>
<dt>
<dd> Foreground color. Needed for <code>-mod</code> patterns.</dl>
<p> <code>-from</code> <i>color</i></p>
<dl>
<dt>
<dd> Start color for rendering textures. Needed for <code>-gradient</code> patterns.</dl>
<p> <code>-to</code> <i>color</i></p>
<dl>
<dt>
<dd> Ending color for rendering textures. Needed for <code>-gradient</code> patterns.</dl>
<p> <code>-help</code></p>
<dl>
<dt>
<dd> Prints version info and short help text.</dl>
<h2>AUTHORS</h2>
<p> This manpage was modified by Curt &quot;Asenchi&quot; Micol &lt;asenchi at asenchi.com&gt; for the Fluxbox window manager. </p>
<p> Further updates for fluxbox-1.1.2 and conversion to asciidoc format by Jim Ramsay &lt;i.am at jimramsay.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) <a href="/docs/linux/man/1-fbsetbg/">fbsetbg</a>(1) <a href="/docs/linux/man/1-xsetroot/">xsetroot</a>(1) <a href="/docs/linux/man/1-xmessage/">xmessage</a>(1) <a href="/docs/linux/man/1-gxmessage/">gxmessage</a>(1)</p>
<h2>AUTHOR</h2>
<p> <code>Jim Ramsay</code> &lt;i.am [at] jimramsay.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
