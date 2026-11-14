---
title: "jpegicc(1)"
name: "jpegicc"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jpegicc/"
description: "jpegicc – little cms ICC profile applier for JPEG."
---

<h2>NAME</h2>
<p> jpegicc &#8211; little cms ICC profile applier for JPEG.</p>
<h2>SYNOPSIS</h2>
<p> <code>jpegicc</code> [<i>options</i>]<i> input.jpg output.jpg</i></p>
<h2>DESCRIPTION</h2>
<p> lcms is a standalone CMM engine, which deals with the color management. It implements a fast transformation between ICC profiles. <code>jpegicc </code> is little cms ICC profile applier for JPEG.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b </code></p>
<dd> Black point compensation.</p>
<dt><code>-c &lt;0,1,2,3&gt;</code></p>
<dd> Precalculates transform. (0=Off, 1=Normal, 2=Hi-res, 3=LoRes) [defaults to 1]</p>
<dt><code>-g</code></p>
<dd> Marks out-of-gamut colors on softproof.</p>
<dt><code>-h &lt;0,1,2&gt;</code></p>
<dd> Show summary of options and examples.</p>
<dt><code>-i&nbsp;<wbr></code><i>profile</i></p>
<dd> Input profile (defaults to sRGB).</p>
<dt><code>-m &lt;0,1,2,3&gt;</code></p>
<dd> SoftProof intent.</p>
<dt><code>-n</code></p>
<dd> Ignore embedded profile.</p>
<dt><code>-p&nbsp;<wbr></code><i>profile</i></p>
<dd> Soft proof profile</p>
<dt><code>-o&nbsp;<wbr></code><i>profile</i></p>
<dd> Output profile (defaults to sRGB).</p>
<dt><code>-q &lt;0..100&gt;</code></p>
<dd> Output JPEG quality.</p>
<dt><code>-t &lt;0,1,2,3&gt;</code></p>
<dd> Intent (0=Perceptual, 1=Colorimetric, 2=Saturation, 3=Absolute).</p>
<dt><code>-v</code></p>
<dd> Verbose.</dl>
<h2>EXAMPLES</h2>
<pre>
To color correct from scanner to sRGB:
        jpegicc -iscanner.icm in.jpg out.jpg
        
To convert from monitor1 to monitor2:
        jpegicc -imon1.icm -omon2.icm in.jpg out.jpg
To make a CMYK separation:
        jpegicc -oprinter.icm inrgb.jpg outcmyk.jpg
To recover sRGB from a CMYK separation:
        jpegicc -iprinter.icm incmyk.jpg outrgb.jpg
To convert from CIELab ITU/Fax JPEG to sRGB
        jpegicc -iitufax.icm in.jpg out.jpg
</pre>
<h2>NOTES</h2>
<p> For suggestions, comments, bug reports etc. send mail to info [at] littlecms.com.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tifficc/">tifficc</a></code>(1), <code><a href="/docs/linux/man/1-icc2ps/">icc2ps</a></code>(1), <code><a href="/docs/linux/man/1-icclink/">icclink</a></code>(1), <code><a href="/docs/linux/man/1-icctrans/">icctrans</a></code>(1), <code><a href="/docs/linux/man/1-wtpt/">wtpt</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Shiju p. Nair &lt;shiju.p [at] gmail.com&gt;, for the Debian project. </p>
<h2>Index</h2>
