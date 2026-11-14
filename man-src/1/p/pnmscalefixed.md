---
title: "pnmscalefixed(1)"
name: "pnmscalefixed"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmscalefixed/"
description: "pnmscalefixed – scale a portable anymap quickly, but less accurate"
---

<h2 class="name">NAME</h2>
<p> pnmscalefixed &#8211; scale a portable anymap quickly, but less accurate</p>
<h2>DESCRIPTION</h2>
<p> <code>pnmscalefixed</code> is the same thing as <code>pnmscale</code> except that it uses fixed point arithmetic internally instead of floating point, which makes it run faster. In turn, it is less accurate and may distort the image. </p>
<p> Use the <code>pnmscale</code> man page with <code>pnmscalefixed</code>. This man page only describes the difference. </p>
<p> <code>pnmscalefixed</code> uses fixed point 12 bit arithmetic. By contrast, <code>pnmscale</code> uses floating point arithmetic which on most machines is probably 24 bit precision. This makes <code>pnmscalefixed</code> run faster (30% faster in one experiment), but the imprecision can cause distortions at the right and bottom edges. </p>
<p> The distortion takes the following form: One pixel from the edge of the input is rendered larger in the output than the scaling factor requires. Consequently, the rest of the image is smaller than the scaling factor requires, because the overall dimensions of the image are always as requested. This distortion will usually be very hard to see. </p>
<p> <code>pnmscalefixed</code> with the <code>-verbose</code> option tells you how much distortion there is. </p>
<p> The amount of distortion depends on the size of the input image and how close the scaling factor is to an integral 1/4096th. </p>
<p> If the scaling factor is an exact multiple of 1/4096, there is no distortion. So, for example doubling or halving an image causes no distortion. But reducing it or enlarging it by a third would cause some distortion. To consider an extreme case, scaling a 100,000 row image down to 50,022 rows would create an output image with all of the input squeezed into the top 50,000 rows, and the last row of the input copied into the bottom 22 rows of output. </p>
<p> <code>pnmscalefixed</code> could probably be modified to use 16 bit or better arithmetic without losing anything. The modification would consist of a single constant in the source code. Until there is a demonstrated need for that, though, the Netpbm maintainer wants to keep the safety cushion afforded by the original 12 bit precision. </p>
<p> <code>pnmscalefixed</code> does not have <code>pnmscale &#8216;s</code> <code>-nomix</code> option. </p>
<h2>Index</h2>
