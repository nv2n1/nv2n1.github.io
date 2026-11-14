---
title: "pnmshear(1)"
name: "pnmshear"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmshear/"
description: "pnmshear – shear a portable anymap by some angle"
---

<h2 class="name">NAME</h2>
<p> pnmshear &#8211; shear a portable anymap by some angle </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmshear</code> [<code>-noantialias</code>] <i>angle</i> [<i>pnmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable anymap as input. Shears it by the specified angle and produces a portable anymap as output. If the input file is in color, the output will be too, otherwise it will be grayscale. The angle is in degrees (floating point), and measures this: </p>
<pre><code>
+ -- -- -- -+ +-- -- -- -+ | | |\ | OLD | | \ NEW | | | an\ + -- -- -- -+ | gle + -- -- -- -+
</code></pre>
<p> If the angle is negative, it shears the other way: </p>
<pre><code>
+ -- -- -- -+ | -an + -- -- -- -+ | | | gl / /
    | OLD | | e / NEW /
    | | | / /
              +-- -- -- -+ +-- -- -- -+
</code></pre>
<p> The angle should not get too close to 90 or -90, or the resulting anymap will be unreasonably wide. </p>
<p> The shearing is implemented by looping over the source pixels and distributing fractions to each of the destination pixels. This has an &quot;anti-aliasing&quot; effect &#8211; it avoids jagged edges and similar artifacts. However, it also means that the original colors or gray levels in the image are modified. If you need to keep precisely the same set of colors, you can use the <code>-noantialias</code> flag. This does the shearing by moving pixels without changing their values. If you want anti-aliasing and don&#8217;t care about the precise colors, but still need a limited *number* of colors, you can run the result through <i>ppmquant</i>. </p>
<p> All flags can be abbreviated to their shortest unique prefix.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pnmrotate/">pnmrotate</a>(1), <a href="/docs/linux/man/1-pnmflip/">pnmflip</a>(1), <a href="/docs/linux/man/5-pnm/">pnm</a>(5), <a href="/docs/linux/man/1-ppmquant/">ppmquant</a>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989, 1991 by Jef Poskanzer. </p>
<h2>Index</h2>
