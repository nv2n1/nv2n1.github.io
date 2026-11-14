---
title: "makepattern(1)"
name: "makepattern"
section: "1"
letter: "m"
url: "/docs/linux/man/1-makepattern/"
description: "makepattern – make GMT color pattern from b/w pattern or icon"
---

<h2>NAME</h2>
<p> makepattern &#8211; make GMT color pattern from b/w pattern or icon</p>
<h2>SYNOPSIS</h2>
<p> <code>makepattern</code> <i>1bit.ras</i> | <i>iconfile</i> <code>-Cf</code><i>r/g/b</i> <code>-Cb</code><i>r/g/b</i></p>
<h2>DESCRIPTION</h2>
<p> <code>makepattern</code> reads either a Sun 1-bit rasterfile OR a Sun icon file. It then accepts color choices for the foreground and background pixels and colorizes the pattern, writing it as a 8-bit Sun rasterfile on stdout. These patterns may then be used in <code>GMT</code> (3.1 or later) <code>-Gp</code> settings or by <code>psimage</code>.</p>
<dl>
<dt><i>1bit.ras</i> | <i>iconfile</i></p>
<dd> Either a 1-bit Sun rasterfile (standard format, no RLE) or a Sun icon file (as used in <code>GMT</code> 3.0).</p>
<dt><code>-Cf</code></p>
<dd> Sets the color for the foreground pixels (the ones) [black].</p>
<dt><code>-Cb</code></p>
<dd> Sets the color for the background pixels (the zeros) [white].</dl>
<h2>WIN32 fix</h2>
<p> Since binary redirection under WIN32 does not work, you must specify the output file with <code>-G</code><i>newfile.ras</i>. This option is only available under WIN32.</p>
<h2>EXAMPLES</h2>
<p> To create a colorized red/blue 8-bit Sun rasterfile pattern from the old 3.0-style iconpattern stored in file custom.icon, run </p>
<p> <code>makepattern</code> custom.icon <code>-Cf</code>red <code>-Cb</code>blue &gt; custom.ras </p>
<p> To create a green/blue 8-bit Sun rasterfile pattern from a 1-bit Sun raster called bits.ras, run </p>
<p> <code>makepattern</code> bits.ras <code>-Cf</code>green <code>-Cb</code>blue &gt; colorbits.ras</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-psimage/">psimage</a></i>(1) </p>
<h2>Index</h2>
