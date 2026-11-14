---
title: "fixup_datafile-2(3)"
name: "fixup_datafile-2"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fixup_datafile-2/"
description: "fixup_datafile – Fixes truecolor images in compiled datafiles. Allegro game programming library."
---

<p>fixup_datafile &#8211; Fixes truecolor images in compiled datafiles. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void fixup_datafile(DATAFILE *data);</code></p>
<h2>Description</h2>
<p>If you are using compiled datafiles (produced by the dat2s and dat2c utilities) on a platform that doesn&#8217;t support constructors (currently any non GCC-based platform), or if the datafiles contain truecolor images, you must call this function once after your set the video mode that you will be using. This will ensure the datafiles are properly initialised in the first case and convert the color values into the appropriate format in the second case. It handles flipping between RGB and BGR formats, and converting between different color depths whenever that can be done without changing the size of the image (ie. changing 15&lt;-&gt;16-bit hicolor for both bitmaps and RLE sprites, and 24&lt;-&gt;32-bit truecolor for RLE sprites). </p>
<p> Note that you can only call this once and expect it to work correctly, because after the call the DATAFILE you fixed up is permanently converted to whatever is the current component ordering for your screen mode. If you call fixup_datafile again, the function assumes you have a freshly loaded datafile. It cannot &quot;undo&quot; the previous conversion. </p>
<p> If your program supports changing resolution and/or color depth during runtime, you have two choices: either call fixup_datafile() just once and hope that the component ordering and bit depth doesn&#8217;t change when the screen mode changes (unlikely). Or, you can reload your datafiles when the screen mode changes. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_gfx_mode/">set_gfx_mode</a></code>(3), <code><a href="/docs/linux/man/3-set_color_conversion/">set_color_conversion</a></code>(3)</p>
