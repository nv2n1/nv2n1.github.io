---
title: "ppmtowinicon(1)"
name: "ppmtowinicon"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtowinicon/"
description: "ppmtowinicon – convert 1 or more portable pixmaps into a Windows .ico file"
---

<h2 class="name">NAME</h2>
<p> ppmtowinicon &#8211; convert 1 or more portable pixmaps into a Windows .ico file</p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtowinicon</code> [<i>-andpgms</i>] [<i>-output output.ico</i>] [<i>ppmfiles</i>&#8230;<i>]</i> </p>
<h2>DESCRIPTION</h2>
<p> Reads one or more portable pixmaps as input. Produces a Microsoft Windows .ico file as output. </p>
<p> A Windows icon contains 1 or more images, at different resolutions and color depths. </p>
<p> Microsoft recommends including at least the following formats in each icon (size and bits-per-pixel): </p>
<p> 16 x 16 &#8211; 4 bpp </p>
<p> 32 x 32 &#8211; 4 bpp </p>
<p> 48 x 48 &#8211; 8 bpp </p>
<p> Default I/O is STDIN/STDOUT.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-andpgms</code></p>
<dd> If this option is given, every second file is read as an &quot;and mask&quot; to be used by windows for transparency data for the previous image. (These are set to fully opaque by default). The and mask is a PGM image, where any pixel with maxval intensity means opaque and any other pixel means not opaque. Note that as with all Netpbm programs, you may use a PBM file here and it will be used as if it were the equivalent PGM. </p>
<p> The and mask is like an alpha mask, except for what it signifies in the &quot;not opaque&quot; areas. In the usual case, the foreground image is black in those areas, and in that case the areas are fully transparent &#8212; the background shows through the icon. But in general, a not opaque pixel signifies that the background and foreground should be merged as follows: The intensities of the color components in the forgeground and background are represented as binary numbers, then corresponding bits of the background and foreground intensities are exlusive-or&#8217;ed together. So there is a sort of reverse video effect. </p>
<dt><code>-output output.ico</code></p>
<dd> File to write. By default, the icon is written to stdout. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-winicontoppm/">winicontoppm</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2000 by Lee Benfield. </p>
<h2>Index</h2>
