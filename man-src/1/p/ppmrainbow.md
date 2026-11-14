---
title: "ppmrainbow(1)"
name: "ppmrainbow"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmrainbow/"
description: "ppmrainbow – Generate a rainbow"
---

<h2 class="name">NAME</h2>
<p> ppmrainbow &#8211; Generate a rainbow</p>
<h2>SYNOPSIS</h2>
<p> <code>ppmrainbow</code> [<code>-width=</code><i>number</i>] [<code>-height=</code><i>number</i>]<br />
 [<code>-tmpdir=</code><i>directory</i>] [<code>-verbose</code>] <i>color</i> &#8230; </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one to designate an option. You may use either white space or equals signs between an option name and its value. </p>
<h2>DESCRIPTION</h2>
<p> <code>ppmrainbow</code> generates a PPM image that fades from one color to another to another from left to right, like a rainbow. The colors are those you specify on the command line, in that order. The first color is added again on the right end of the image. </p>
<p> If you want a vertical or other non-horizontal rainbow, run the output through <code>pnmrotate</code>. </p>
<p> One use for such a rainbow is to compose it with another image under an alpha mask in order to add a rainbow area to another image. In fact, you can make rainbow-colored text by using <code>pbmtext</code>, <code>pnmcomp</code>, and <code>ppmrainbow</code>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-width </code><i>number</i></p>
<dd> The width in pixels of the output image. </p>
<p> Default is 600.</p>
<dt><code>-height </code><i>number</i></p>
<dd> The height in pixels of the output image. </p>
<p> Default is 8.</p>
<dt><code>-tmpdir</code></p>
<dd> The directory specification of the directory <code>ppmrainbow</code> is to use for temporary files. </p>
<p> Default is the value of the <code>TMPDIR </code> environment variable, or <i>/tmp</i> if <code>TMPDIR </code> is not set.</p>
<dt><code>-verbose</code></p>
<dd> Print the &quot;commands&quot; (invocations of other Netpbm programs) that <code>ppmrainbow</code> uses to create the image. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmmake/">ppmmake</a></code>(1), <code><a href="/docs/linux/man/1-pnmcomp/">pnmcomp</a></code>(1), <code><a href="/docs/linux/man/1-pbmtext/">pbmtext</a></code>(1), <code><a href="/docs/linux/man/1-ppmfade/">ppmfade</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5). </p>
<h2>AUTHOR</h2>
<p> Arjen Bax wrote <code>ppmrainbow</code> in June 2001 and contributed it to the Netpbm package. Bryan Henderson wrote this man page in July 2001. </p>
<h2>Index</h2>
