---
title: "pamarith(1)"
name: "pamarith"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamarith/"
description: "pamarith – perform arithmetic on two Netpbm images"
---

<h2 class="name">NAME</h2>
<p> pamarith &#8211; perform arithmetic on two Netpbm images</p>
<h2>SYNOPSIS</h2>
<p> <code>pamarith</code> <code>-add</code> | <code>-subtract</code> | <code>-multiply</code> | <code>-divide</code> | <code>-difference</code> | <code>-minimum</code> | <code>-maximum</code> | <code>-mean</code> | <code>-compare</code> | <code>-and</code> | <code>-or</code> | <code>-nand</code> | <code>-nor</code> | <code>-xor</code> | <code>-shiftleft</code> | <code>-shiftright</code> <i>pamfile1</i> <i>pamfile2</i> </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one. You may separate an option name and its value with white space instead of an equals sign. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamarith</code> reads two PBM, PGM, PPM, or PAM images as input. It performs the specified binary arithmetic operation on their sample values and produces an output of a format which is the more general of the two input formats. The two input images must be of the same width and height. The arithmetic is performed on each pair of identically located tuples to generate the identically located tuple of the output. </p>
<p> For the purpose of the calculation, it assumes any PBM, PGM, or PPM input image is the equivalent PAM image of tuple type <code>BLACKANDWHITE</code>, <code>GRAYSCALE</code>, or <code>RGB</code>, respectively, and if it produces a PBM, PGM, or PPM output, produces the equivalent of the PAM image which is the result of the calculation. </p>
<p> The first <i>pamfile</i> argument identifies the &#8216;left&#8217; argument image; the second <i>pamfile</i> argument identifies the &#8216;right&#8217; one. </p>
<p> If the output is PAM, the tuple type is the same as the tuple type of the left input image. </p>
<p> <code>pamarith</code> performs the arithmetic on each pair of identically located tuples in the two input images. </p>
<p> The arithmetic operation is in all cases fundamentally a function from two integers to an integer. The operation is performed on two tuples as follows. The two input images must have the same depth, or one of them must have depth one. <code>pamarith</code> fails if one of these is not the case. </p>
<p> If they have the same depth, <code>pamarith</code> simply carries out the arithmetic one sample at a time. I.e. if at a particular position the left input image contains the tuple (s1,s2,&#8230;,sN) and the right input image contains the tuple (t1,t2,&#8230;tN), and the function is f, then the output image contains the tuple (f(s1,t1),f(s2,t2),&#8230;,f(sN,tN)). </p>
<p> If one of the images has depth 1, the arithmetic is performed between the one sample in that image and each of the samples in the other. I.e. if at a particular position the left input image contains the tuple (s) and the right input image contains the tuple (t1,t2,&#8230;tN), and the function is f, then the output image contains the tuple (f(s,t1),f(s,t2),&#8230;,f(s,tN)). </p>
<h3>Maxval</h3>
<p> The meanings of the samples with respect to the maxval varies according to the function you select. </p>
<p> In PAM images in general, the most usual meaning of a sample (the one that applies when a PAM image represents a visual image), is that it represents a fraction of some maximum. The maxval of the image corresponds to some maximum value (in the case of a visual image, it corresponds to &#8216;full intensity.&#8217;), and a sample value divided by the maxval gives the fraction. </p>
<p> For <code>pamarith</code>, this interpretation applies to the regular arithmetic functions: <code>-add</code>, <code>-subtract</code>, <code>-multiply</code>, <code>-divide</code>, <code>-difference</code>, <code>-minimum</code>, <code>-maximum</code>, <code>-mean</code>, and <code>-compare</code>. For those, you should think of the arguments and result as numbers in the range [0,1). For example, if the maxval of the left argument image is 100 and the maxval of the right argument image is 200 and the maxval of the output image is 200, and the left sample value in an <code>-add</code> calculation is 50 and the right sample is 60, the actual calculation is 50/100 + 60/200 = 160/200, and the output sample value is 160. </p>
<p> For these functions, <code>pamarith</code> makes the output image&#8217;s maxval the maximum of the two input maxvals, except with <code>-compare</code>, where <code>pamarith</code> uses an output maxval of 2. (Before Netpbm 10.14 (February 2003), there was no exception for <code>-compare</code>; in 10.14, the exception was just that the maxval was <i>at least</i> 2, and sometime between 10.18 and 10.26 (January 2005), it changed to being exactly 2). </p>
<p> If the result of a calculation falls outside the range [0, 1), <code>pamarith</code> clips it &#8212; i.e. considers it to be zero or 1-. </p>
<p> In many cases, where both your input maxvals are the same, you can just think of the operation as taking place between the sample values directly, with no consideration of the maxval except for the clipping. E.g. an <code>-add</code> of sample value 5 to sample value 8 yields sample value 13. </p>
<p> But with <code>-multiply</code>, this doesn&#8217;t work. Say your two input images have maxval 255, which means the output image also has maxval 255. Consider a location in the image where the input sample values are 5 and 10. You might think the multiplicative product of those would yield 50 in the output. But <code>pamarith</code> carries out the arithmetic on the fractions 5/255 and 10/255. It multiplies those together and then rescales to the output maxval, giving a sample value in the output PAM of 50/255 rounded to the nearest integer: 0. </p>
<p> With the bit string operations, the maxval has a whole different meaning. The operations in question are: <code>-and</code>, <code>-or</code>, <code>-nand</code>, <code>-nor</code>, <code>-xor</code>, and <code>-shiftleft</code>, <code>-shiftright</code>. </p>
<p> With these, each sample value in one or both input images, and in the output image, represents a bit string, not a number. The maxval tells how wide the bit string is. The maxval must be a full binary count (a power of two minus one, such as 0xff) and the number of ones in it is the width of the bit string. For the dyadic bit string operations (that&#8217;s everything but the shift functions), the maxvals of the input images must be the same and <code>pamarith</code> makes the maxval of the output image the same. </p>
<p> For the bit shift operations, the output maxval is the same as the left input maxval. The right input image (which contains the shift counts) can have any maxval and the maxval is irrelevant to the interpretation of the samples. The sample value is the actual shift count. But it&#8217;s still required that no sample value exceed the maxval. </p>
<h3>The Operations</h3>
<p> Most of the operations are obvious from the option name. The following paragraphs cover those that aren&#8217;t. </p>
<p> <code>-subtract</code> subtracts a value in the right input image from a value in the left input image. </p>
<p> <code>-difference</code> calculates the absolute value of the difference. </p>
<p> <code>-multiply</code> does an ordinary arithmetic multiplication, but tends to produce nonobvious results because of the way <code>pamarith</code> interprets sample values. See Maxval . </p>
<p> <code>-divide</code> divides a value in the left input image by the value in the left input image. But like <code>-multiply</code>, it tends to produce nonobvious results. Note that <code>pamarith</code> clipping behavior makes this of little use when the left argument (dividend) is greater than the right argument (divisor) &#8212; the result in that case is always the maxval. If the divisor is 0, the result is the maxval. This option was new in Netpbm 10.30 (October 2005). </p>
<p> <code>-compare</code> produces the value <code>0</code> when the value in the left input image is less than the value in the right input image, <code>1</code> when the values are equal, and <code>2</code> when the left is greater than the right. </p>
<p> If the maxvals of the input images are not identical, <code>pamarith</code> may claim two values are not equal when in fact they are, due to the precision with which it does the arithmetic. However, it will never say A is greater than B if A is less than B. </p>
<p> <code>-compare</code> was new in Netpbm 10.13 (December 2002). </p>
<p> <code>-and</code>, <code>-nand</code>, <code>-or</code>, <code>-nor</code>, and <code>-xor</code> consider the input and output images to contain bit strings; they compute bitwise logic operations. Note that if the maxval is 1, you can also look at these as logic operations on boolean input values. See section Maxval for the special meaning of maxval with respect to bit string operations such as these. </p>
<p> <code>-shiftleft</code> and <code>-shiftright</code> consider the left input image and output image to contain bit strings. They compute a bit shift operation, with bits falling off the left or right end and zeroes shifting in, as opposed to bits off one end to the other. The right input image sample value is the number of bit positions to shift. </p>
<p> Note that the maxval (see Maxval ) determines the width of the frame within which you are shifting. </p>
<h3>Notes</h3>
<p> If you want to apply a unary function, e.g. &quot;halve&quot;, to a single image, use <code>pamfunc</code>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamfunc/">pamfunc</a></code>(1) , <code><a href="/docs/linux/man/1-pamsummcol/">pamsummcol</a></code>(1) , <code><a href="/docs/linux/man/1-pamsumm/">pamsumm</a></code>(1) , <code><a href="/docs/linux/man/1-pnminvert/">pnminvert</a></code>(1) , <code><a href="/docs/linux/man/1-ppmbrighten/">ppmbrighten</a></code>(1) , <code><a href="/docs/linux/man/1-ppmdim/">ppmdim</a></code>(1) , <code><a href="/docs/linux/man/1-pnmconvol/">pnmconvol</a></code>(1) , <code><a href="/docs/linux/man/1-pamdepth/">pamdepth</a></code>(1) , <code><a href="/docs/linux/man/1-pnmpsnr/">pnmpsnr</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pamarith</code> replaced <code>pnmarith</code> in Netpbm 10.3 (June 2002). </p>
<p> In Netpbm 10.3 through 10.8, though, <code>pamarith</code> was not backward compatible because it required the input images to be of the same depth, so you could not multiply a PBM by a PPM as is often done for masking. (It was not intended at the time that <code>pnmarith</code> would be removed from Netpbm &#8212; the plan was just to rewrite it to use <code>pamarith</code>; it was removed by mistake). </p>
<p> But starting with Netpbm 10.9 (September 2002), <code>pamarith</code> allows the images to have different depths as long as one of them has depth 1, and that made it backward compatible with <code>pnmarith</code>. </p>
<p> The original <code>pnmarith</code> did not have the <code>-mean</code> option. </p>
<p> The <code>-compare</code> option was added in Netpbm 10.13 (December 2002). </p>
<p> The bit string operations were added in Netpbm 10.27 (March 2005). </p>
<p> The <code>-divide</code> option was added in Netpbm 10.30 (October 2005). </p>
<h2>Index</h2>
