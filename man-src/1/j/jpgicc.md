---
title: "jpgicc(1)"
name: "jpgicc"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jpgicc/"
description: "jpgicc – little cms ICC profile applier for JPEG."
---

<h2 class="name">NAME</h2>
<p> jpgicc &#8211; little cms ICC profile applier for JPEG. </p>
<h2>SYNOPSIS</h2>
<p> <code>jpgicc</code> [<i>options</i>]<i> input.jpg output.jpg</i></p>
<h2>DESCRIPTION</h2>
<p> lcms is a standalone CMM engine, which deals with the color management. It implements a fast transformation between ICC profiles. <code>jpgicc</code> is a little cms ICC profile applier for JPEG.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></dt>
<dd> Black point compensation.</dd>
<dt><code>-c&nbsp;</code><i>NUM</i></dt>
<dd> Precalculates transform (0=Off, 1=Normal, 2=Hi-res, 3=LoRes) [defaults to 1].</dd>
<dt><code>-d&nbsp;</code><i>NUM</i></dt>
<dd> Observer adaptation state (abs.col. only), (0..1.0, float value) [defaults to 0.0].</dd>
<dt><code>-e</code></dt>
<dd> Embed destination profile.</dd>
<dt><code>-g</code></dt>
<dd> Marks out-of-gamut colors on softproof.</dd>
<dt><code>-h&nbsp;</code><i>NUM</i></dt>
<dd> Show summary of options and examples (0=help, 1=Examples, 2=Built-in profiles, 3=Contact information)</dd>
<dt><code>-i&nbsp;</code><i>profile</i></dt>
<dd> Input profile (defaults to sRGB).</dd>
<dt><code>-l&nbsp;</code><i>link</i></dt>
<dd> TODO: explain this option.</dd>
<dt><code>-m&nbsp;</code><i>NUM</i></dt>
<dd> SoftProof intent (0,1,2,3) [defaults to 0].</dd>
<dt><code>-n</code></dt>
<dd> Ignore embedded profile.</dd>
<dt><code>-o&nbsp;</code><i>profile</i></dt>
<dd> Output profile (defaults to sRGB).</dd>
<dt><code>-p&nbsp;</code><i>profile</i></dt>
<dd> Soft proof profile.</dd>
<dt><code>-q&nbsp;</code><i>NUM</i></dt>
<dd> Output JPEG quality, (0..100) [defaults to 75].</dd>
<dt><code>-s&nbsp;</code><i>newprofile</i></dt>
<dd> Save embedded profile as <i>newprofile</i>.</dd>
<dt><code>-t NUM</code></dt>
<dd> Rendering intent </dd>
<pre>
<dl><dt></dt><dd>0=Perceptual [default]
1=Relative colorimetric
2=Saturation
3=Absolute colorimetric
10=Perceptual preserving black ink
11=Relative colorimetric preserving black ink
12=Saturation preserving black ink
13=Perceptual preserving black plane
14=Relative colorimetric preserving black plane
15=Saturation preserving black plane
</dd></dl>
</pre>
<dt><code>-v</code></dt>
<dd> Verbose.</dd>
<dt><code>-!&nbsp;</code><i>NUM,NUM,NUM</i></dt>
<dd> Out-of-gamut marker channel values (r,g,b) [defaults: 128,128,128].</dd></dl>
<h2>BUILT-IN PROFILES</h2>
<pre><code>
        *Lab2  -- D50-based v2 CIEL*a*b
        *Lab4  -- D50-based v4 CIEL*a*b
        *Lab   -- D50-based v4 CIEL*a*b
        *XYZ   -- CIE XYZ (PCS)
        *sRGB  -- sRGB color space
        *Gray22 - Monochrome of Gamma 2.2
        *Gray30 - Monochrome of Gamma 3.0
        *null   - Monochrome black for all input
        *Lin2222- CMYK linearization of gamma 2.2 on each channel
</code></pre>
<h2>EXAMPLES</h2>
<pre>
To color correct from scanner to sRGB:
        jpgicc -iscanner.icm in.jpg out.jpg
To convert from monitor1 to monitor2:
        jpgicc -imon1.icm -omon2.icm in.jpg out.jpg
To make a CMYK separation:
        jpgicc -oprinter.icm inrgb.jpg outcmyk.jpg
To recover sRGB from a CMYK separation:
        jpgicc -iprinter.icm incmyk.jpg outrgb.jpg
To convert from CIELab ITU/Fax JPEG to sRGB
        jpgicc -iitufax.icm in.jpg out.jpg
To convert from CIELab ITU/Fax JPEG to sRGB
        jpgicc in.jpg out.jpg
</pre>
<h2>NOTES</h2>
<p> For suggestions, comments, bug reports etc. send mail to info [at] littlecms.com.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-linkicc/">linkicc</a></code>(1), <code><a href="/docs/linux/man/1-psicc/">psicc</a></code>(1), <code><a href="/docs/linux/man/1-tificc/">tificc</a></code>(1), <code><a href="/docs/linux/man/1-transicc/">transicc</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Shiju p. Nair &lt;shiju.p [at] gmail.com&gt;, for the Debian project. </p>
