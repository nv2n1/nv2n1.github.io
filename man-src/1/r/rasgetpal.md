---
title: "rasgetpal(1)"
name: "rasgetpal"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rasgetpal/"
description: "rasgetpal – extract the color palette of a rasterfile and write it to standard output"
---

<h2>NAME</h2>
<p> rasgetpal &#8211; extract the color palette of a rasterfile and write it to standard output</p>
<h2>SYNOPSIS</h2>
<p> <code>rasgetpal</code> [<code>-Version</code>] <i>srcfile</i> [<i>dstfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Given <i>srcfile</i> and no <i>dstfile</i>, <code>rasgetpal</code> will extract the color palette from <i>srcfile</i> and print it in textual form to standard output. Given <i>srcfile</i> and <i>dstfile</i>, <code>rasgetpal</code> will extract the color palette from <i>srcfile</i> and save it in file <i>dstfile</i>. If the extension of <i>dstfile</i> is &quot;.txt&quot;, the color palette is saved in textual form. If it is &quot;.pal&quot;, the palette is saved in a binary HDF-compatible format. </p>
<p> Once you have a &quot;.pal&quot; color palette you can use it with NCSA&#8217;s XImage or any other application that uses this format of color palette. A textual color palette can be edited using a standard text editor and then fed back to <i>ctrans</i>, <i>rasview</i>, or <i>rascat</i> in order to get a modified color palette. It&#8217;s also useful when you simply want to know what&#8217;s in your color palette. See &quot;man ras_palette&quot; for more information on these different formats.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Print help information.</p>
<dt><code>-Version</code></p>
<dd> Print the version number. </p>
</dl>
<h2>EXAMPLE</h2>
<p> Let&#8217;s suppose you have an X Window Dump rasterfile called <i>window.xwd</i> and you&#8217;d like to get a textual copy of the color palette. </p>
<pre>
% rasgetpal window.xwd window.txt
% vi window.txt /* edit the color table */
% rasview -pal window.txt window.xwd
</pre>
<p> You could also use the command below to get the same palette file: </p>
<pre>
% rasgetpal window.xwd &gt;window.txt
</pre>
<p> Now suppose you&#8217;d like to get an HDF-compatible binary palette from &quot;window.xwd&quot;: </p>
<pre>
% rasgetpal window.xwd new.pal
</pre>
<h2>CAVEATS</h2>
<p> A color map can be extracted from indexed rasterfiles but not from direct-color rasterfiles. </p>
<h2>SEE ALSO</h2>
<p> <code>rasview</code>(1NCARG), <code>rascat</code>(1NCARG), <code>rasls</code>(1NCARG), <code>rassplit</code>(1NCARG), <code>ras_formats</code>(5NCARG), <code>ras_palette</code>(5NCARG) </p>
<p> Hardcopy: NCAR Graphics Fundamentals, UNIX Version</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research </p>
<p> The use of this Software is governed by a License Agreement. </p>
<h2>Index</h2>
