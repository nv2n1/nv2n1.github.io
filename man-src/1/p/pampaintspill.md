---
title: "pampaintspill(1)"
name: "pampaintspill"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pampaintspill/"
description: "pampaintspill – smoothly spill colors into the background"
---

<h2 class="name">NAME</h2>
<p> pampaintspill &#8211; smoothly spill colors into the background</p>
<h2>SYNOPSIS</h2>
<p> <code>pampaintspill</code> [<code>&#8211;bgcolor</code>=<i>color</i>] [<code>&#8211;wrap</code>] [<code>&#8211;all</code>] [<code>&#8211;downsample</code>=<i>number</i>] [<code>&#8211;power</code>=<i>number</i>] [<i>filename</i>] </p>
<p> Minimum unique abbreviations of option are acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pampaintspill</code> produces a smooth color gradient from all of the non-background-colored pixels in an input image, effectively &lt;q&gt;spilling paint&lt;/q&gt; onto the background. <code>pampaintspill</code> is similar to <code>pamgradient</code> but differs in the following characteristics: </p>
<dl>
<dt>&bull;</p>
<dd> <code>pampaintspill</code> accepts any number of paint<br />
sources&nbsp;<wbr>(non-background-colored pixels), which can lie anywhere<br />
on the canvas.&nbsp;<wbr>&nbsp;<wbr><code>pamgradient</code>&nbsp;<wbr>accepts exactly<br />
four paint sources, one in each corner of the image. </p>
<dt>&bull;</p>
<dd> <code>pampaintspill</code> requires an input image while<br />
<code>pamgradient</code>&nbsp;<wbr>generates a new image from<br />
scratch. </p>
<dt>&bull;</p>
<dd> <code>pampaintspill</code> can produce tileable output and<br />
can control how tightly the gradient colors bind to their source<br />
pixels. </p>
</dl>
<p> Results are generally best when the input image contains just a few, crisp spots of color. Use your drawing program&#8217;s pencil tool &amp;mdash; as opposed to a paintbrush or airbrush tool &amp;mdash; with a small nib. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;bgcolor</code>=<i>color</i></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr> Explicitly specify the background color. <i>color</i> can be<br />
specified using any of the formats accepted by the&nbsp;<wbr> <tt>ppm_parsecolor()</tt> library routine such as <tt>red</tt> or <tt>#ff0000</tt>. If<br />
<code>&#8211;bgcolor</code>&nbsp;<wbr>is not specified,&nbsp;<wbr><code>pampaintspill</code>&nbsp;<wbr>makes an<br />
educated guess about the background color based on the colors in the<br />
image&#8217;s corners. </p>
<dt><code>&#8211;wrap</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr> Allow gradients to wrap around image borders. That is, colors<br />
that spill off the right side of the image reappear on the left side of<br />
the image and likewise for left/right, top/bottom, and<br />
bottom/top.&nbsp;<wbr><code>&#8211;wrap</code>&nbsp;<wbr>makes images tileable, which is nice for<br />
producing desktop backgrounds. </p>
<dt><code>&#8211;all</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr> Recolor all pixels, not just background pixels. Normally,<br />
non-background-colored pixels in the input image appear unmodified in<br />
the output image. With&nbsp;<wbr><code>&#8211;all</code>,&nbsp;<wbr><i>all</i>&nbsp;<wbr>pixels are colored<br />
based on their distance from all of the&nbsp;<wbr>(other)&nbsp;<wbr>non-background-colored<br />
pixels. </p>
<dt><code>&#8211;downsample</code>=<i>number</i></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr> Ignore all but <i>number</i> non-background-colored pixels.<br />
When a large number of pixels in the input image differ in color from<br />
the background,&nbsp;<wbr><code>pampaintspill</code>&nbsp;<wbr>runs very slowly. The<br />
<code>&#8211;downsample</code>&nbsp;<wbr>option randomly selects a given number of colored<br />
pixels to use as paint sources for the gradients and ignores the rest,<br />
thereby trading off image quality for speed of execution. </p>
<dt><code>&#8211;power</code>=<i>number</i></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr> Control how color intensity changes as a function of the<br />
distance from a paint source. The default value for&nbsp;<wbr><i>number</i>&nbsp;<wbr>is<br />
-2.0, which means that intensity drops&nbsp;<wbr>(because of the minus sign)&nbsp;<wbr>with<br />
the square&nbsp;<wbr>(because of the 2.0)&nbsp;<wbr>of the distance from each paint<br />
source. -2.0 generally works well in practice, but other values can be<br />
specified for various special effects. With very small numbers of paint<br />
sources, -1.0 may produce subtler gradients, but these get muddier as<br />
the number of paint sources increases. Positive numbers&nbsp;<wbr>(e.g., 1.0 and<br />
2.0)&nbsp;<wbr>make the paint sources stand out in the output image by pushing the<br />
gradients away from them. </p>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pamgradient/">pamgradient</a></code>(1) </p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-ppmmake/">ppmmake</a></code>(1) ,</p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-ppmrainbow/">ppmrainbow</a></code>(1) ,</p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pgmramp/">pgmramp</a></code>(1) ,</p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-ppmpat/">ppmpat</a></code>(1) ,</p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
</dl>
<h2>HISTORY</h2>
<p> <code>pampaintspill</code> was new in Netpbm 10.50 (March 2010). </p>
<h2>COPYRIGHT</h2>
<p> Copyright&nbsp;<wbr>&#169; 2010 Scott Pakin, &lt;a href= &quot;mailto:scott+pbm [at] pakin.org&quot;&gt;<i>scott+pbm [at] pakin.org</i>&lt;/a&gt;. </p>
<h2>Index</h2>
