---
title: "tifficc(1)"
name: "tifficc"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tifficc/"
description: "tifficc – little cms ICC profile applier for TIFF."
---

<h2>NAME</h2>
<p> tifficc &#8211; little cms ICC profile applier for TIFF.</p>
<h2>SYNOPSIS</h2>
<p> <code>tifficc</code> [<i>options</i>]<i> input.tif output.tif</i></p>
<h2>DESCRIPTION</h2>
<p> lcms is a standalone CMM engine, which deals with the color management. It implements a fast transformation between ICC profiles. <code>tifficc </code> is little cms ICC profile applier for TIFF.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Handle channels &gt; 4 as alpha.</p>
<dt><code>-b </code></p>
<dd> Black point compensation.</p>
<dt><code>-c &lt;0,1,2,3&gt;</code></p>
<dd> Precalculates transform. (0=Off, 1=Normal, 2=Hi-res, 3=LoRes) [defaults to 1]</p>
<dt><code>-e</code></p>
<dd> Embed destination profile.</p>
<dt><code>-g</code></p>
<dd> Marks out-of-gamut colors on softproof.</p>
<dt><code>-h &lt;0,1,2&gt;</code></p>
<dd> Show summary of options and examples.</p>
<dt><code>-i profile</code></p>
<dd> Input profile (defaults to sRGB).</p>
<dt><code>-k &lt;0..400&gt; </code></p>
<dd> Ink-limiting in % (CMYK only).</p>
<dt><code>-l profile</code></p>
<dd> Transform by device-link profile.</p>
<dt><code>-m &lt;0,1,2,3&gt;</code></p>
<dd> SoftProof intent.</p>
<dt><code>-n</code></p>
<dd> Ignore embedded profile on input.</p>
<dt><code>-p&nbsp;<wbr></code><i>profile</i></p>
<dd> Soft proof profile.</p>
<dt><code>-o&nbsp;<wbr></code><i>profile</i></p>
<dd> Output profile (defaults to sRGB).</p>
<dt><code>-s&nbsp;<wbr></code><i>profile</i></p>
<dd> Save embedded profile as &lt;new profile&gt;</p>
<dt><code>-t &lt;0,1,2,3&gt;</code></p>
<dd> Intent (0=Perceptual, 1=Colorimetric, 2=Saturation, 3=Absolute).</p>
<dt><code>-v</code></p>
<dd> Verbose.</p>
<dt><code>-w</code></p>
<dd> Wide output (generates 16 bps tiff).</p>
<dt>You can also use following builtins</p>
<dd> *Lab &#8211; CIE Lab D50 based *XYZ &#8211; XYZ *adobe1998RBB &#8211; AdobeRGB *colormatchrgb &#8211; ColorMatch RGB *applergb &#8211; Apple RGB</dl>
<h2>EXAMPLES</h2>
<pre>
To color correct from scanner to sRGB:
        tifficc -iscanner.icm in.tif out.tif
To convert from monitor1 to monitor2:
        tifficc -imon1.icm -omon2.icm in.tif out.tif
        
To make a CMYK separation:
        tifficc -oprinter.icm inrgb.tif outcmyk.tif
        
To recover sRGB from a CMYK separation:
        tifficc -iprinter.icm incmyk.tif outrgb.tif
To convert from CIELab TIFF to sRGB
        tifficc -iTiffLab8Spac.icm in.tif out.tif
</pre>
<h2>NOTES</h2>
<p> For suggestions, comments, bug reports etc. send mail to info [at] littlecms.com.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-jpegicc/">jpegicc</a></code>(1), <code><a href="/docs/linux/man/1-icc2ps/">icc2ps</a></code>(1), <code><a href="/docs/linux/man/1-icclink/">icclink</a></code>(1), <code><a href="/docs/linux/man/1-icctrans/">icctrans</a></code>(1), <code><a href="/docs/linux/man/1-wtpt/">wtpt</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was originally written by Shiju p. Nair &lt;shiju.p [at] gmail.com&gt;, for the Debian project. Modified by Marti Maria to reflect further changes. </p>
<h2>Index</h2>
