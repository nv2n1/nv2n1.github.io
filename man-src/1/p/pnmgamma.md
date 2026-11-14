---
title: "pnmgamma(1)"
name: "pnmgamma"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmgamma/"
description: "pnmgamma – perform gamma correction on a portable anymap"
---

<h2 class="name">NAME</h2>
<p> pnmgamma &#8211; perform gamma correction on a portable anymap</p>
<h2>SYNOPSIS</h2>
<p> <code>pnmgamma </code> [<code>-ungamma</code>] [<code>-cieramp</code>|<code>-srgbramp</code>] [<i>value</i> [<i>pnmfile</i>]]<br />
 <code>pnmgamma</code> [<code>-ungamma</code>] [<code>-cieramp</code>|<code>-srgbramp</code>] <i>redgamma greengamma bluegamma</i> [<i>pnmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> Performs gamma correction on pseudo-PNM images. </p>
<p> The PPM format specification specify that certain sample values in a file represent certain light intensities in an image. In particular, they specify that the sample values are directly proportional to gamma-corrected intensity values. The gamma correction they specify is CIE Rec. 709. </p>
<p> However, people sometimes work with approximations of PPM and PGM where the relationship between the image intensities and the sample values are something else. For example, the sample value might be directly proportional to the intensity with no gamma correction (often called &quot;linear intensity&quot;). Or a different gamma transfer function may be used. </p>
<p> <code>pnmgamma</code> allows you to manipulate the transfer function, thus working with and/or creating pseudo-PPM files that are useful for various things. </p>
<p> For example, if you feed a true PPM to <code>pnmgamma -cieramp -ungamma</code>, you get as output a file which is PPM in every respect except that the sample values are directly proportional to the light intensities in the image. If you feed such a file to <code>pnmgamma -cieramp</code>, you get out a true PPM. </p>
<p> The situation for PGM images is analogous. And <code>pnmgamma</code> treats PBM images as PGM images. </p>
<p> When you feed a linear PPM image to a display program that expects a true PPM, the display appears darker than it should, so <code>pnmgamma</code> has the effect of lightening the image. When you feed a true PPM to a display program that expects linear sample values, and therefore does a gamma correction of its own on them, the display appears lighter than it should, so <code>pnmgamma</code> with a gamma value less than one (the multiplicative inverse of whatever gamma value the display program uses) has the effect of darkening the image. </p>
<h2>PARAMETERS</h2>
<p> The only parameters are the specification of the input image file and the gamma values. Every gamma transfer function <code>pnmgamma</code> uses contains an exponent, which is the gamma value, and you can choose that value. </p>
<p> Furthermore, you can choose different values for each of the three RGB components. If you specify only one gamma value, <code>pnmgamma</code> uses that value for all three RGB components. </p>
<p> If you don&#8217;t specify any gamma parameters, <code>pnmgamma</code> chooses a default. For the transfer functions defined by standards, the default is the value defined by the standard. If you specify anything else, you will be varying from the standard. For the simple power function transfer function, the default gamma is 1/.45. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-ungamma</code></p>
<dd> Apply the inverse of the specified transfer function (i.e. go from gamma-corrected nonlinear intensities to linear intensities). </p>
<dt><code>-cieramp</code></p>
<dd> Use the CIE Rec. 709 gamma transfer function. Note that it is true CIE Rec. 709 only if you use the default gamma value (i.e. don&#8217;t specify any gamma parameters). This transfer function is a power function modified with a linear ramp near black. </p>
<p> If you specify neither <code>-cieramp</code> nor <code>-srgbramp</code>, the transfer function defaults to a simple power function.</p>
<dt><code>-srgbramp </code></p>
<dd> Use the Internation Electrotechnical Commission (IEC) SRGB gamma transfer function (as specified in the standard IEC 61966-2-1). Note that it is true SRGB only if you use the default gamma value (i.e. don&#8217;t specify any gamma parameters). This transfer function is like the one selected by <code>-cieramp</code>, but with different constants in it. </p>
<p> Note that SRGB is often spelled &quot;sRGB&quot;. In this document, we use standard English typography, though, which doesn&#8217;t allow for that kind of capitalization. </p>
<p> If you specify neither <code>-cieramp</code> nor <code>-srgbramp</code>, the transfer function defaults to a simple power function. </p>
</dl>
<h2>WHAT IS GAMMA?</h2>
<p> A good explanation of gamma is in Charles Poynton&#8217;s GammaFAQ at &lt;<a rel="nofollow" href="http://www.poynton.com/notes/colour_and_gamma/ColorFAQ.html">http://www.poynton.com/notes/colour_and_gamma/ColorFAQ.html</a>&gt; and ColorFAQ at &lt;<a rel="nofollow" href="http://www.poynton.com/notes/colour_and_gamma/GammaFAQ.html">http://www.poynton.com/notes/colour_and_gamma/GammaFAQ.html</a>&gt; </p>
<p> In brief: The simplest way to code an image is by using sample values that are directly proportional to the intensity of the color components. But that wastes the sample space because the human eye can&#8217;t discern differences between low-intensity colors as well as it can between high-intensity colors. So instead, we pass the light intensity values through a transfer function that makes it so that changing a sample value by 1 causes the same level of perceived color change anywhere in the sample range. We store those resulting values in the image file. That transfer function is called the gamma transfer function and the transformation is called gamma correcting. </p>
<p> Virtually all image formats, either specified or de facto, use gamma-corrected values for their sample values. </p>
<p> What&#8217;s really nice about gamma is that by coincidence, the inverse function that you have to do to convert the gamma-corrected values back to real light intensities is done automatically by CRTs. You just apply a voltage to the CRT&#8217;s electron gun that is proportional to the gamma-corrected sample value, and the intensity of light that comes out of the screen is close to the intensity value you had before you applied the gamma transfer function! </p>
<p> And when you consider that computer video devices usually want you to store in video memory a value proportional to the signal voltage you want to go to the monitor, which the monitor turns into a proportional drive voltage on the electron gun, it is really convenient to work with gamma-corrected sample values. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1991 by Bill Davidson and Jef Poskanzer. </p>
<h2>Index</h2>
