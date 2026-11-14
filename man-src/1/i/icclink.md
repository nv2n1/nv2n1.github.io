---
title: "icclink(1)"
name: "icclink"
section: "1"
letter: "i"
url: "/docs/linux/man/1-icclink/"
description: "icclink – little cms device link generator."
---

<h2>NAME</h2>
<p> icclink &#8211; little cms device link generator.</p>
<h2>SYNOPSIS</h2>
<p> <code>icclink</code> [<i>options</i>]<i> &lt;profiles&gt;</i></p>
<h2>DESCRIPTION</h2>
<p> lcms is a standalone CMM engine, which deals with the color management. It implements a fast transformation between ICC profiles. <code>icclink </code> is little cms device link generator. </p>
<p> Links two or more profiles into a single devicelink profile. Colorspaces must be paired except Lab/XYZ, that can be interchanged.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-8</code></p>
<dd> Creates 8-bit devicelink.</p>
<dt><code>-b </code></p>
<dd> Black point compensation.</p>
<dt><code>-c &lt;0,1,2,3&gt;</code></p>
<dd> Precision (0=LowRes, 1=Normal, 2=Hi-res). [defaults to 1]</p>
<dt><code>-d&nbsp;<wbr></code><i>description</i></p>
<dd> Description text (quotes can be used).</p>
<dt><code>-h &lt;0,1,2,3&gt;</code></p>
<dd> Show summary of options and examples.</p>
<dt><code>-i&nbsp;<wbr></code><i>profile</i></p>
<dd> Input profile (defaults to sRGB).</p>
<dt><code>-k &lt;0..400&gt; </code></p>
<dd> Ink-limiting in % (CMYK only)</p>
<dt><code>-o&nbsp;<wbr></code><i>profile</i></p>
<dd> Output devicelink profile. [defaults to &#8216;devicelink.icm&#8217;]</p>
<dt><code>-t &lt;0,1,2,3&gt;</code></p>
<dd> Intent (0=Perceptual, 1=Colorimetric, 2=Saturation, 3=Absolute).</p>
<dt><code>-x </code></p>
<dd> Creatively, guess deviceclass of resulting profile.</p>
<dt>
<pre>
<dd>Built-in profiles:
        *Lab  -- D50-based CIEL*a*b (PCS)
        *XYZ  -- CIE XYZ (PCS)
        *sRGB -- sRGB color space
        *Gray22- Monochrome of Gamma 2.2
        *Lin2222- CMYK linearization of gamma 2.2 on each channel
</pre>
</dl>
<h2>EXAMPLES</h2>
<pre>
To create 'devicelink.icm' from a.icc to b.icc:
        icclink a.icc b.icc
To create 'out.icc' from sRGB to cmyk.icc:
        icclink -o out.icc *sRGB cmyk.icc
To create a sRGB input profile working in Lab:
        icclink -x -o sRGBLab.icc *sRGB *Lab
To create a XYZ -&gt; sRGB output profile:
        icclink -x -o sRGBLab.icc *XYZ *sRGB
To create a abstract profile doing softproof for cmyk.icc:
        icclink -t1 -x -o softproof.icc *Lab cmyk.icc cmyk.icc *Lab
To create a 'grayer' sRGB input profile:
        icclink -x -o grayer.icc *sRGB gray.icc gray.icc *Lab
To embed ink limiting into a cmyk output profile:
        icclink -x -o cmyklimited.icc -k 250 cmyk.icc *Lab
</pre>
<h2>NOTES</h2>
<p> For suggestions, comments, bug reports etc. send mail to info [at] littlecms.com.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-jpegicc/">jpegicc</a></code>(1), <code><a href="/docs/linux/man/1-tifficc/">tifficc</a></code>(1), <code><a href="/docs/linux/man/1-icc2ps/">icc2ps</a></code>(1), <code><a href="/docs/linux/man/1-icctrans/">icctrans</a></code>(1), <code><a href="/docs/linux/man/1-wtpt/">wtpt</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Shiju p. Nair &lt;shiju.p [at] gmail.com&gt;, for the Debian project. </p>
<h2>Index</h2>
