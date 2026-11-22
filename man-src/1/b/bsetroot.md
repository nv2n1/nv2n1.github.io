---

title: "bsetroot(1)"
name: "bsetroot"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bsetroot/"
description: "bsetroot – blackbox utility to change root window appearance"
---

<p> bsetroot &#8211; blackbox utility to change root window appearance</p>
<h2>SYNOPSIS</h2>
<p> <code>bsetroot</code> -help<br/>
 <code>bsetroot</code> [ -display <i>display</i> ] -solid <i>color</i><br/>
 <code>bsetroot</code> [ -display <i>display</i> ] -mod <i>x y</i> -fg <i>color</i> -bg <i>color</i><br/>
 <code>bsetroot</code> [ -display <i>display</i> ] -gradient <i>texture</i> -from <i>color</i> -to <i>color</i></p>
<h2>DESCRIPTION</h2>
<p> Bsetroot is a utility that can control the appearance of the root window in three ways: Either give it a solid color, or write a two color modula pattern to it, or render a gradient texture, based on two different colors. </p>
<p> Bsetroot resembles <i><a href="/docs/linux/man/1-xsetroot/">xsetroot</a></i>(1) in this functionality but it supports multiple screen displays, and gradient textures the same way as Blackbox does. It doesn&#8217;t handle cursors etc. Bsetroot is part of the Blackbox package.</p>
<h2>OPTIONS</h2>
<p> Bsetroot operates in three ways, you must choose one of the first 3 options:</p>
<dl>
<dt><code>-solid</code><i> color</i></dt>
<dd> Sets the root window to specified color.</dd>
<dt><code>-mod</code><i> x y</i></dt>
<dd> Creates a modula pattern. You must specify <code>-bg</code> and <code>-fg</code> colors.</dd>
<dt><code>-gradient</code><i> texturestring</i></dt>
<dd> Renders the specified texture string to the root window. For possible texture strings, please refer to <i><a href="/docs/linux/man/1-blackbox/">blackbox</a></i>(1). You must also specify both a <code>-from</code> and a <code>-to</code> color.</dd>
<dt><code>-display</code><i> display</i></dt>
<dd> Tells Bsetroot to connect to the specified display.</dd>
<dt><code>-bg, -background </code><i>color</i></dt>
<dd> Background color. Needed for <code>-mod</code> patterns.</dd>
<dt><code>-fg, -foreground </code><i>color</i></dt>
<dd> Foreground color. Needed for <code>-mod</code> patterns.</dd>
<dt><code>-from</code><i> color</i></dt>
<dd> Start color for rendering textures. Needed for <code>-gradient</code> operation mode.</dd>
<dt><code>-to</code><i> color</i></dt>
<dd> Ending color for rendering textures. Needed for <code>-gradient</code> operation mode.</dd>
<dt><code>-help</code></dt>
<dd> Prints version info and short help text.</dd></dl>
<h2>AUTHOR</h2>
<p> Bsetroot was written and maintained by Brad Hughes (blackbox [at] alug.org) and Jeff Raven (jraven [at] psu.edu).</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-blackbox/">blackbox</a></i>(1) </p>
