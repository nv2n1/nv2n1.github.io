---
title: "dfbg(1)"
name: "dfbg"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dfbg/"
description: "dfbg – DirectFB background configuration tool"
---

<h2 class="name">NAME</h2>
<p> dfbg &#8211; DirectFB background configuration tool</p>
<h2>SYNOPSIS</h2>
<p> <code>dfbg</code> [<i>options</i>] &lt;<i>filename</i>&gt;|&lt;color&gt; </p>
<h2>DESCRIPTION</h2>
<p> <code>dfbg</code> is a small utility to configure the background of the DirectFB desktop. It loads the specified image and sets it as background image. </p>
<p> <code>dfbg</code> requires DirectFB with the multi-application core enabled. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c, &#8211;color</code></p>
<dd> Set color fill mode using &lt;color&gt; in AARRGGBB format (hexadecimal). The alpha component can be omitted in most configurations. </p>
<dt><code>-t, &#8211;tile</code></p>
<dd> Set tiled mode instead of scaling the image to fit the screen size. </p>
<dt><code>-v, &#8211;version</code></p>
<dd> Output version information. </p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print brief help and exit. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Set background color to DirectFB&#8217;s default color </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>dfbg -c ff107ce8</p>
<p> Set image stretched to fit the screen </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>dfbg bg.png</p>
<p> Set image tiled </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>dfbg -t bg.png</p>
<h2>OTHER INFO</h2>
<p> The canonical place to find informations about DirectFB is at <a rel="nofollow" href="http://www.directfb.org/.">http://www.directfb.org/.</a> </p>
<h2>Index</h2>
