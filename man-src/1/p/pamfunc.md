---
title: "pamfunc(1)"
name: "pamfunc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamfunc/"
description: "pamfunc – Apply a simple monadic arithmetic function to a Netpbm image"
---

<h2 class="name">NAME</h2>
<p> pamfunc &#8211; Apply a simple monadic arithmetic function to a Netpbm image</p>
<h2>SYNOPSIS</h2>
<p> <code>pamfunc</code> { <code>-multiplier=</code><i>realnum</i> | <code>-divisor=</code><i>realnum</i> | <code>-adder=</code><i>integer</i> | <code>-subtractor=</code><i>integer</i> | <code>-min=</code><i>wholenum</i> | <code>-max=</code><i>wholenum</i> <code>-andmask=</code><i>hexmask</i> <code>-ormask=</code><i>hexmask</i> <code>-xormask=</code><i>hexmask</i> <code>-not</code> <code>-shiftleft=</code><i>count</i> <code>-shiftright=</code><i>count</i> } [<i>filespec</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one. You may separate an option name and its value with white space instead of an equals sign. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamfunc</code> reads a Netpbm image as input and produces a Netpbm image as output, with the same format, maxval, and dimensions as the input. <code>pamfunc</code> applies a simple transfer function to each sample in the input to generate the corresponding sample in the output. The options determine what function. </p>
<p> <code>pamarith</code> is the same thing for binary functions &#8212; it takes two images as input and applies a specified simple arithmetic function (e.g. addition) on pairs of samples from the two to produce the single output image. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-multiplier=</code><i>realnum</i></p>
<dd>
<p> This option makes the transfer function that of multiplying by<br />
&nbsp;<wbr>&nbsp;<wbr><i>realnum</i>.&nbsp;<wbr>&nbsp;<wbr><i>realnum</i>&nbsp;<wbr>must be nonnegative.&nbsp;<wbr>&nbsp;<wbr>If the result<br />
&nbsp;<wbr>&nbsp;<wbr>is greater than the image maxval, it is clipped to the maxval. </p>
<p> Where the input is a PGM or PPM image, this has the effect of<br />
&nbsp;<wbr>&nbsp;<wbr>dimming or brightening it.&nbsp;<wbr>&nbsp;<wbr>For a different kind of brightening,<br />
&nbsp;<wbr>&nbsp;<wbr>see <code><a href="/docs/linux/man/1-ppmbrighten/">ppmbrighten</a></code>(1)<br />
&nbsp;<wbr>and <code><a href="/docs/linux/man/1-ppmflash/">ppmflash</a></code>(1) </p>
<p> Also, see <code><a href="/docs/linux/man/1-ppmdim/">ppmdim</a></code>(1) , which does the<br />
&nbsp;<wbr>&nbsp;<wbr>same thing as&nbsp;<wbr><code>pamfunc -multiplier</code>&nbsp;<wbr>on a PPM image with a<br />
&nbsp;<wbr>&nbsp;<wbr>multiplier between 0 and 1,<br />
&nbsp;<wbr>&nbsp;<wbr>except it uses integer arithmetic, so it may be faster. </p>
<p> And <code><a href="/docs/linux/man/1-ppmfade/">ppmfade</a></code>(1)<br />
&nbsp;<wbr>can generate a whole<br />
&nbsp;<wbr>&nbsp;<wbr>sequence of images of brightness declining to black or increasing to<br />
&nbsp;<wbr>&nbsp;<wbr>white, if that&#8217;s what you want.<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<dt><code>-divisor=</code><i>realnum</i></p>
<dd>
<p> This option makes the transfer function that of dividing by<br />
&nbsp;<wbr>&nbsp;<wbr><i>realnum</i>.&nbsp;<wbr>&nbsp;<wbr><i>realnum</i>&nbsp;<wbr>must be nonnegative.&nbsp;<wbr>&nbsp;<wbr>If the result<br />
&nbsp;<wbr>&nbsp;<wbr>is greater than the image maxval, it is clipped to the maxval. </p>
<p> This is the same function as you would get with <code>-multiplier</code>,<br />
&nbsp;<wbr>&nbsp;<wbr>specifying the multiplicative inverse of&nbsp;<wbr><i>realnum</i>.<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<dt><code>-adder=</code><i>integer</i></p>
<dd>
<p> This option makes the transfer function that of adding<br />
&nbsp;<wbr>&nbsp;<wbr><i>wholenum</i>.&nbsp;<wbr>&nbsp;<wbr>If the result is greater than the image maxval,<br />
&nbsp;<wbr>&nbsp;<wbr>it is clipped to the maxval.&nbsp;<wbr>&nbsp;<wbr>If it is less than zero, it is<br />
&nbsp;<wbr>&nbsp;<wbr>clipped to zero. </p>
<p> Note that in mathematics, this entity is called an &#8216;addend,&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>and an&nbsp;<wbr>&#8216;adder&#8217;&nbsp;<wbr>is a snake.&nbsp;<wbr>&nbsp;<wbr>We use&nbsp;<wbr>&#8216;adder&#8217;&nbsp;<wbr>because<br />
&nbsp;<wbr>&nbsp;<wbr>it makes more sense.<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<dt><code>-subtractor=</code><i>integer</i></p>
<dd>
<p> This option makes the transfer function that of subtracting<br />
&nbsp;<wbr>&nbsp;<wbr><i>wholenum</i>.&nbsp;<wbr>&nbsp;<wbr>If the result is greater than the image maxval,<br />
&nbsp;<wbr>&nbsp;<wbr>it is clipped to the maxval.&nbsp;<wbr>&nbsp;<wbr>If it is less than zero, it is<br />
&nbsp;<wbr>&nbsp;<wbr>clipped to zero. </p>
<p> Note that in mathematics, this entity is called a<br />
&nbsp;<wbr>&nbsp;<wbr>&#8216;subtrahend&#8217;&nbsp;<wbr>rather than a&nbsp;<wbr>&#8216;subtractor.&#8217;&nbsp;<wbr>&nbsp;<wbr>We<br />
&nbsp;<wbr>&nbsp;<wbr>use&nbsp;<wbr>&#8216;subtractor&#8217;&nbsp;<wbr>because it makes more sense. </p>
<p> This is the same function as you would get with <code>-adder</code>,<br />
&nbsp;<wbr>&nbsp;<wbr>specifying the negative of&nbsp;<wbr><i>integer</i>.<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<dt><code>-min=</code><i>wholenum</i></p>
<dd>
<p> This option makes the transfer function that of taking the<br />
&nbsp;<wbr>&nbsp;<wbr>maximum of the argument and&nbsp;<wbr><i>wholenum</i>.&nbsp;<wbr>&nbsp;<wbr>I.e the minimum<br />
&nbsp;<wbr>&nbsp;<wbr>value in the output will be&nbsp;<wbr><i>wholenum</i>. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>If&nbsp;<wbr><i>wholenum</i>&nbsp;<wbr>is greater than the maxval, though, every sample<br />
&nbsp;<wbr>&nbsp;<wbr>in the output will be maxval. </p>
<dt><code>-max=</code><i>wholenum</i></p>
<dd>
<p> This option makes the transfer function that of taking the<br />
&nbsp;<wbr>&nbsp;<wbr>minimum of the argument and&nbsp;<wbr><i>wholenum</i>.&nbsp;<wbr>&nbsp;<wbr>I.e the maximum<br />
&nbsp;<wbr>&nbsp;<wbr>value in the output will be&nbsp;<wbr><i>wholenum</i>. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>If&nbsp;<wbr><i>wholenum</i>&nbsp;<wbr>is greater than the maxval, the function is<br />
&nbsp;<wbr>&nbsp;<wbr>idempotent &#8212; the output is identical to the input.<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<dt><code>-andmask=</code><i>hexmask</i></p>
<dd>
<p> This option makes the transfer function that of bitwise anding<br />
&nbsp;<wbr>&nbsp;<wbr>with&nbsp;<wbr><i>hexmask</i>. </p>
<p> <i>hexmask</i> is in hexadecimal. Example: <tt>0f</tt> </p>
<p> See section Maxval for the special<br />
&nbsp;<wbr>&nbsp;<wbr>meaning of maxval with respect to bit string operations such as<br />
&nbsp;<wbr>&nbsp;<wbr>this. </p>
<p> This option was new in Netpbm 10.40 (September 2007). </p>
<dt><code>-ormask=</code><i>hexmask</i></p>
<dd>
<p> This option makes the transfer function that of bitwise<br />
&nbsp;<wbr>&nbsp;<wbr>inclusive oring with&nbsp;<wbr><i>hexmask</i>. </p>
<p> This is analogous to <code>-andmask</code>. </p>
<p> This option was new in Netpbm 10.40 (September 2007). </p>
<dt><code>-xormask=</code><i>hexmask</i></p>
<dd>
<p> This option makes the transfer function that of bitwise<br />
&nbsp;<wbr>&nbsp;<wbr>exclusive oring with&nbsp;<wbr><i>hexmask</i>. </p>
<p> This is analogous to <code>-andmask</code>. </p>
<p> This option was new in Netpbm 10.40 (September 2007). </p>
<dt><code>-not</code></p>
<dd>
<p> This option makes the transfer function that of bitwise logical<br />
&nbsp;<wbr>&nbsp;<wbr>inversion&nbsp;<wbr>(e.g. sample value 0xAA becomes 0x55). </p>
<p> See section Maxval for the special<br />
&nbsp;<wbr>&nbsp;<wbr>meaning of maxval with respect to bit string operations such as<br />
&nbsp;<wbr>&nbsp;<wbr>this. </p>
<p> <code>pnminvert</code> does the same thing for a bilevel visual image<br />
&nbsp;<wbr>&nbsp;<wbr>which has maxval 1 or is of PBM type. </p>
<p> This option was new in Netpbm 10.40 (September 2007). </p>
<dt><code>-shiftleft=</code><i>count</i></p>
<dd>
<p> This option makes the transfer function that of bitwise shifting<br />
&nbsp;<wbr>&nbsp;<wbr>left by&nbsp;<wbr><i>count</i>&nbsp;<wbr>bits. </p>
<p> See section Maxval for the special<br />
&nbsp;<wbr>&nbsp;<wbr>meaning of maxval with respect to bit string operations such as<br />
&nbsp;<wbr>&nbsp;<wbr>this. </p>
<p> This option was new in Netpbm 10.40 (September 2007). </p>
<dt><code>-shiftright=</code><i>count</i></p>
<dd>
<p> This option makes the transfer function that of bitwise shifting<br />
&nbsp;<wbr>&nbsp;<wbr>right by&nbsp;<wbr><i>count</i>&nbsp;<wbr>bits. </p>
<p> This is analogous to <code>-shiftleft</code>. </p>
<p> This option was new in Netpbm 10.40 (September 2007). </p>
</dl>
<h2>MAXVAL</h2>
<p> For the arithmetic functions, the maxval has no meaning. The function applies to the sample value as an integer. (Note that this differs from the usual interpretation of PAM samples as being a fraction of a maxval, but <i>does</i> produce more intuitive result: 2 times 5 is 10. </p>
<p> But with the bit string operations, the maxval has a special meaning. The functions in question are: <code>-andmask</code>, <code>-ormask</code>, <code>-xormask</code>, <code>-not</code>, <code>-shiftleft</code>, and <code>-shiftright</code>. </p>
<p> With these, each sample value the input image, and in the output image, represents a bit string, not a number. The maxval tells how wide the bit string is. The maxval must be a full binary count (a power of two minus one, such as 0xff) and the number of ones in it is the width of the bit string. </p>
<p> For a masking function, the mask value you specify must not have more significant bits than the width indicated by the maxval. </p>
<p> For a shifting operation, the shift count you specify must not be greater than the width indicated by the maxval. </p>
<p> The maxval of the output image is the same as that of the input image. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmdim/">ppmdim</a></code>(1) , <code><a href="/docs/linux/man/1-ppmbrighten/">ppmbrighten</a></code>(1) , <code><a href="/docs/linux/man/1-pamdepth/">pamdepth</a></code>(1) , <code><a href="/docs/linux/man/1-pamarith/">pamarith</a></code>(1) , <code><a href="/docs/linux/man/1-pamsummcol/">pamsummcol</a></code>(1) , <code><a href="/docs/linux/man/1-pamsumm/">pamsumm</a></code>(1) , <code><a href="/docs/linux/man/1-ppmfade/">ppmfade</a></code>(1) , <code><a href="/docs/linux/man/1-pnminvert/">pnminvert</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , </p>
<h2>HISTORY</h2>
<p> This program was added to Netpbm in Release 10.3 (June 2002). </p>
<h2>Index</h2>
