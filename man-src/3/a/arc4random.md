---
title: "arc4random(3)"
name: "arc4random"
section: "3"
letter: "a"
url: "/docs/linux/man/3-arc4random/"
description: "arc4random arc4random_buf arc4random_uniform arc4random_stir arc4random_addrandom – arc4 random number generator"
---

<h2 class="name">NAME</h2>
<p> <code>arc4random</code> <code>arc4random_buf</code> <code>arc4random_uniform</code> <code>arc4random_stir</code> <code>arc4random_addrandom</code> &#8211; arc4 random number generator </p>
<h2>LIBRARY</h2>
<p> Lb libbsd</p>
<h2>SYNOPSIS</h2>
<p> In bsd/stdlib.h Ft u_int32_t Fn arc4random void Ft void Fn arc4random_buf void *buf size_t nbytes Ft u_int32_t Fn arc4random_uniform u_int32_t upper_bound Ft void Fn arc4random_stir void Ft void Fn arc4random_addrandom unsigned char *dat int datlen</p>
<h2>DESCRIPTION</h2>
<p> The Fn arc4random function uses the key stream generator employed by the arc4 cipher, which uses 8*8 8 bit S-Boxes. The S-Boxes can be in about (2**1700) states. The Fn arc4random function returns pseudo-random numbers in the range of 0 to (2**32)-1, and therefore has twice the range of <a href="/docs/linux/man/3-rand/">rand</a>(3) and <a href="/docs/linux/man/3-random/">random</a>(3). </p>
<p> Fn arc4random_buf function fills the region Fa buf of length Fa nbytes with ARC4-derived random data. </p>
<p> Fn arc4random_uniform will return a uniformly distributed random number less than Fa upper_bound . Fn arc4random_uniform is recommended over constructions like &#8220;<code>arc4random() % upper_bound</code> &#8221; as it avoids &quot;modulo bias&quot; when the upper bound is not a power of two. </p>
<p> The Fn arc4random_stir function reads data from /dev/urandom and uses it to permute the S-Boxes via Fn arc4random_addrandom . </p>
<p> There is no need to call Fn arc4random_stir before using Fn arc4random functions family, since they automatically initialize themselves.</p>
<h2>EXAMPLES</h2>
<p> The following produces a drop-in replacement for the traditional Fn rand and Fn random functions using Fn arc4random : </p>
<blockquote><p><tt>&quot;#define foo4random() (arc4random() % ((unsigned)RAND_MAX + 1))&quot;</tt></p></blockquote>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-rand/">rand</a>(3), <a href="/docs/linux/man/3-random/">random</a>(3), <a href="/docs/linux/man/3-srandomdev/">srandomdev</a>(3)</p>
<h2>HISTORY</h2>
<p> RC4 has been designed by RSA Data Security, Inc. It was posted anonymously to the USENET and was confirmed to be equivalent by several sources who had access to the original cipher. Since RC4 used to be a trade secret, the cipher is now referred to as ARC4 </p>
<h2>Index</h2>
