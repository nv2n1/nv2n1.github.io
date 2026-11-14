---
title: "pbmtonokia(1)"
name: "pbmtonokia"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmtonokia/"
description: "pbmtonokia – convert a portable bitmap to Nokia Smart Messaging Formats"
---

<h2 class="name">NAME</h2>
<p> pbmtonokia &#8211; convert a portable bitmap to Nokia Smart Messaging Formats </p>
<h2>SYNOPSIS</h2>
<p> <code>pbmtonokia [options]</code> [<i>pbmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable bitmap as input. Produces a Nokia Smart Messaging (hexcode, .nok, .ngg) file as output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-fmt</code></p>
<dd> Specifies the output format (default is HEX_NOL).</p>
<dt>HEX_NOL</p>
<dd> Nokia Operator Logo as (uploadable) hexcode. Use option -net to specify network code.</p>
<dt>HEX_NGG</p>
<dd> Nokia Group Graphic as (uploadable) hexcode.</p>
<dt>HEX_NMP</p>
<dd> Nokia Picture Message as (uploadable) hexcode. Use option -txt to specify optional text message.</p>
<dt>NOL</p>
<dd> Nokia Operator Logo as .nol format. This is editable by the Group-Graphic Editor from Kessler Wireless Design (<a rel="nofollow" href="http://www.kessler-design.com">www.kessler-design.com</a>)</p>
<dt>NGG</p>
<dd> Nokia Group Graphic as .ngg format. This is editable by the Group-Graphic Editor from Kessler Wireless Design (<a rel="nofollow" href="http://www.kessler-design.com">www.kessler-design.com</a>)</p>
<dt><code>-net</code></p>
<dd> Specifies the 6 hex-digit operator network code for Operator Logos (Default is 62F210 = D1,Germany).</p>
<dt><code>-txt</code></p>
<dd> Specifies the text message for Picture Messages. Default is no text message.</dl>
<h2>LIMITATIONS</h2>
<p> Currently limited to rows&lt;=255 and columns&lt;=255. Supports only b/w graphics, not animated.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5), <code>Nokia Smart Messaging Specification (<a rel="nofollow" href="http://forum.nokia.com)">http://forum.nokia.com)</a></code></p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2001 Tim Ruehsen &lt;tim.ruehsen [at] openmediasystem.de&gt;. </p>
<h2>Index</h2>
