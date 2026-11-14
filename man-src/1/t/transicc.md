---
title: "transicc(1)"
name: "transicc"
section: "1"
letter: "t"
url: "/docs/linux/man/1-transicc/"
description: "transicc – little cms ColorSpace conversion calculator."
---

<h2 class="name">NAME</h2>
<p> transicc &#8211; little cms ColorSpace conversion calculator. </p>
<h2>SYNOPSIS</h2>
<p> <code>transicc</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> lcms is a standalone CMM engine, which deals with the color management. It implements a fast transformation between ICC profiles. <code>transicc </code> is lcms ColorSpace conversion calculator.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-%</code></p>
<dd> use percent % of ink.</p>
<dt><code>-b </code></p>
<dd> Black point compensation.</p>
<dt><code>-c &lt;0,1,2,3&gt;</code></p>
<dd> Precalculates transform. (0=Off, 1=Normal, 2=Hi-res, 3=LoRes) [defaults to 1]</p>
<dt><code>-i&nbsp;</code><i>profile</i></p>
<dd> Input profile (defaults to sRGB).</p>
<dt><code>-l</code></p>
<dd> Transform by device-link profile.</p>
<dt><code>-n</code></p>
<dd> Terse output, intended for pipe usage.</p>
<dt><code>-o&nbsp;</code><i>profile</i></p>
<dd>
<dt>Output profile (defaults to sRGB).</p>
<dd>
<dt><code>-t &lt;0,1,2,3&gt;</code></p>
<dd> Intent (0=Perceptual, 1=Colorimetric, 2=Saturation, 3=Absolute).</p>
<dt><code>-v</code></p>
<dd> Verbose.</p>
<dt><code>-w</code></p>
<dd> Use 16 bits.</p>
<dt><code>-x</code></p>
<dd> Hexadecimal.</p>
<dt>You can use &#8216;*Lab&#8217; and &#8216;*xyz&#8217; as built-in profiles.</p>
<dd></dl>
<h2>NOTES</h2>
<p> For suggestions, comments, bug reports etc. send mail to info [at] littlecms.com.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-jpgicc/">jpgicc</a></code>(1), <code><a href="/docs/linux/man/1-tificc/">tificc</a></code>(1), <code><a href="/docs/linux/man/1-psicc/">psicc</a></code>(1), <code><a href="/docs/linux/man/1-linkicc/">linkicc</a></code>(1),</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Shiju p. Nair &lt;shiju.p [at] gmail.com&gt;, for the Debian project. </p>
<h2>Index</h2>
