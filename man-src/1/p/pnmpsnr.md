---
title: "pnmpsnr(1)"
name: "pnmpsnr"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmpsnr/"
description: "pnmpsnr – compute the difference between two portable anymaps"
---

<h2 class="name">NAME</h2>
<p> pnmpsnr &#8211; compute the difference between two portable anymaps </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmpsnr</code> [<i>pnmfile1</i>] [<i>pnmfile2</i>] </p>
<h2>DESCRIPTION</h2>
<p> Reads two PBM, PGM, or PPM files, or PAM equivalents, as input. Prints the peak signal-to-noise ratio (PSNR) difference between the two images. This metric is typically used in image compression papers to rate the distortion between original and decoded image. </p>
<p> If the inputs are PBM or PGM, <code>pnmpsnr</code> prints the PSNR of the luminance only. Otherwise, it prints the separate PSNRs of the luminance, and chrominance (Cb and Cr) components of the colors. </p>
<p> The PSNR of a given component is the ratio of the mean square difference of the component for the two images to the maximum mean square difference that can exist betwee any two images. It is expressed as a decibel value. </p>
<p> The mean square difference of a component for two images is the mean square difference of the component value, comparing each pixel with the pixel in the same position of the other image. For the purposes of this computation, components are normalized to the scale [0..1]. </p>
<p> The maximum mean square difference is identically 1. </p>
<p> So the higher the PSNR, the closer the images are. A luminance PSNR of 20 means the mean square difference of the luminances of the pixels is 100 times less than the maximum possible difference, i.e. 0.01. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5) </p>
<h2>Index</h2>
