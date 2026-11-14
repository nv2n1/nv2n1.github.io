---
title: "sxpm(1)"
name: "sxpm"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sxpm/"
description: "sxpm – Show an XPM (X PixMap) file and/or convert XPM 1 or 2 files to XPM 3."
---

<h2 class="name">NAME</h2>
<p> sxpm &#8211; Show an XPM (X PixMap) file and/or convert XPM 1 or 2 files to XPM 3. </p>
<h2>SYNOPSIS</h2>
<p> <code>sxpm</code> [<code>-d</code> displayname] [<code>-g</code> geometry] [<code>-hints</code>] [<code>-icon</code> filename] [<code>-plaid | </code>filename | -] [<code>-o</code> filename | <code>-o</code> -] [<code>-pcmap</code>] [<code>-closecolors</code>] [<code>-nod</code>] [<code>-nom</code>] [<code>-mono | -grey4 | -grey | -color</code>] [<code>-sc</code> symbol color] [<code>-sp</code> symbol pixel] [<code>-cp</code> color pixel] [<code>-rgb</code> filename] [<code>-v</code>]</p>
<h2>DESCRIPTION</h2>
<p> The <i>sxpm</i> program can be used to view any XPM (version 1, 2, or 3) file and/or to convert a file from XPM1 or XPM2 to XPM version 3. If <i>sxpm</i> is run with any dummy option specified, the usage is displayed. If no geometry is specified, the show window will have the size of the read pixmap. Pressing the key Q in the window will quit the program.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d </code><i>display</i></p>
<dd> Specifies the display to connect to.</p>
<dt><code>-g </code><i>geom</i></p>
<dd> Window geometry (default is pixmap&#8217;s size).</p>
<dt><code>-hints</code></p>
<dd> Set ResizeInc for window.</p>
<dt><code>-icon </code><i>filename</i></p>
<dd> Set icon to pixmap created from the file <i>filename</i>.</p>
<dt><code>-plaid</code></p>
<dd> Show the plaid pixmap which is stored as data.</p>
<dt><i>filename</i></p>
<dd> Read from the file <i>filename</i> and from standard input if <i>filename</i> is &#8216;-&#8216;. If no input is specified sxpm reads from standard input.</p>
<dt><code>-o </code><i>filename</i></p>
<dd> Write to the file <i>filename</i> (overwrite if it already exists) and to standard output if <i>filename</i> is &#8216;-&#8216;.</p>
<dt><code>-mono</code></p>
<dd> Use the colors specified for a monochrome visual.</p>
<dt><code>-grey4</code></p>
<dd> Use the colors specified for a 4 color greyscale visual.</p>
<dt><code>-grey</code></p>
<dd> Use the colors specified for a greyscale visual.</p>
<dt><code>-color</code></p>
<dd> Use the colors specified for a color visual.</p>
<dt><code>-pcmap</code></p>
<dd> Use a private colormap.</p>
<dt><code>-closecolors</code></p>
<dd> Try to use &quot;close colors&quot; before reverting to other visuals.</p>
<dt><code>-nod</code></p>
<dd> Do not display the pixmap in a window. (Useful when using as converter)</p>
<dt><code>-nom</code></p>
<dd> Do not use the clipmask if there is any.</p>
<dt><code>-sc </code><i>symbol colorname</i></p>
<dd> Override default color to <i>symbol</i> to <i>colorname</i>.</p>
<dt><code>-sp </code><i>symbol pixelvalue</i></p>
<dd> Override default color to <i>symbol</i> to <i>pixelvalue</i>.</p>
<dt><code>-cp </code><i>colorname pixelvalue</i></p>
<dd> Override default color to <i>colorname</i> to <i>pixelvalue</i>.</p>
<dt><code>-rgb </code><i>filename</i></p>
<dd> Search color names in the file <i>filename</i> and write them out instead of the rgb values.</p>
<dt><code>-v</code></p>
<dd> Verbose &#8211; to print out extensions (stderr). </p>
</dl>
<h2>KNOWN BUGS</h2>
<p> Some window managers may not accept a pixmap which is not a bitmap as icon because this does not respect ICCCM, many of the well known ones will accept it though. </p>
<h2>AUTHOR</h2>
<p> Arnaud Le Hors (lehors [at] sophia.inria.fr)<br />
 Bull Research France<br />
 Copyright (C) 1989-95 by Groupe Bull. </p>
<h2>Index</h2>
