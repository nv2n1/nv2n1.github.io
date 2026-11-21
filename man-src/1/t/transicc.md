---

title: "transicc(1)"
name: "transicc"
section: "1"
letter: "t"
url: "/docs/linux/man/1-transicc/"
description: "transicc – little cms ColorSpace conversion calculator."
---

<p> transicc &#8211; little cms ColorSpace conversion calculator. </p>
<h2>SYNOPSIS</h2>
<p> <code>transicc</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> lcms is a standalone CMM engine, which deals with the color management. It implements a fast transformation between ICC profiles. <code>transicc </code> is lcms ColorSpace conversion calculator.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-%</code></dt>
<dd> use percent % of ink.</dd>
<dt><code>-b </code></dt>
<dd> Black point compensation.</dd>
<dt><code>-c &lt;0,1,2,3&gt;</code></dt>
<dd> Precalculates transform. (0=Off, 1=Normal, 2=Hi-res, 3=LoRes) [defaults to 1]</dd>
<dt><code>-i&nbsp;</code><i>profile</i></dt>
<dd> Input profile (defaults to sRGB).</dd>
<dt><code>-l</code></dt>
<dd> Transform by device-link profile.</dd>
<dt><code>-n</code></dt>
<dd> Terse output, intended for pipe usage.</dd>
<dt><code>-o&nbsp;</code><i>profile</i></dt>
<dd>
</dd><dt>Output profile (defaults to sRGB).</dt>
<dd>
</dd><dt><code>-t &lt;0,1,2,3&gt;</code></dt>
<dd> Intent (0=Perceptual, 1=Colorimetric, 2=Saturation, 3=Absolute).</dd>
<dt><code>-v</code></dt>
<dd> Verbose.</dd>
<dt><code>-w</code></dt>
<dd> Use 16 bits.</dd>
<dt><code>-x</code></dt>
<dd> Hexadecimal.</dd>
<dt>You can use &#8216;*Lab&#8217; and &#8216;*xyz&#8217; as built-in profiles.</dt>
<dd></dd></dl>
<h2>NOTES</h2>
<p> For suggestions, comments, bug reports etc. send mail to info [at] littlecms.com.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-jpgicc/">jpgicc</a></code>(1), <code><a href="/docs/linux/man/1-tificc/">tificc</a></code>(1), <code><a href="/docs/linux/man/1-psicc/">psicc</a></code>(1), <code><a href="/docs/linux/man/1-linkicc/">linkicc</a></code>(1),</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Shiju p. Nair &lt;shiju.p [at] gmail.com&gt;, for the Debian project. </p>
