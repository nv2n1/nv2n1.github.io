---
title: "setvtrgb(8)"
name: "setvtrgb"
section: "8"
letter: "s"
url: "/docs/linux/man/8-setvtrgb/"
description: "setvtrgb – set the virtual terminal RGB colors"
---

<p>setvtrgb &#8211; set the virtual terminal RGB colors</p>
<h2>Synopsis</h2>
<p><code>setvtrgb</code> [<i>,options/</i>] <i>vga|FILE|-</i></p>
<h2>Description</h2>
<p>The <i>setvtrgb</i> command takes a single argument, either the string <code>vga</code> , or a path to a file containing the red, green, and blue colors to be used by the Linux virtual terminals. If you use the <code>FILE</code> parameter, <code>FILE</code> should be exactly 3 lines of 16 comma-separated decimal values for RED, GREEN, and BLUE. To seed a valid <code>FILE</code> :</p>
<dl>
<dd><code>cat /sys/module/vt/parameters/default_{red,grn,blu} &gt; FILE</code></dl>
<p> And then edit the values in <code>FILE</code> </p>
<h2>Options</h2>
<dl>
<dt><code>-C</code>, <code>&#8211;console</code>=<i>,DEV/</i></p>
<dd>the console device to be used;</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Prints usage message and exits.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Prints version number and exists. </p>
</dl>
<h2>Author</h2>
<p>The utility is written by Alexey Gladkov, Seth Forshee, Dustin Kirkland.</p>
<h2>Documentation</h2>
<p>Documentation by Dustin Kirkland.</p>
