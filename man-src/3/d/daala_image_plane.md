---
title: "daala_image_plane(3)"
name: "daala_image_plane"
section: "3"
letter: "d"
url: "/docs/linux/man/3-daala_image_plane/"
description: "daala_image_plane –"
---

<h2 class="name">NAME</h2>
<p> daala_image_plane &#8211; </p>
<p> Representation of a single component within an image or frame.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;codec.h&gt;</p>
<h3>Data Fields</h3>
<p> unsigned char * <code>data</code><br />
 <i>Image data is stored as an unsigned octet type whether it&#8217;s actually 8 bit or a multi-byte depth. </i><br />
 unsigned char <code>xdec</code><br />
 <i>The decimation factor in the x and y direction. </i><br />
 unsigned char <code>ydec</code> </p>
<p> int <code>xstride</code><br />
 <i>Distance in memory between two pixels horizontally next to each other. </i><br />
 int <code>ystride</code><br />
 <i>Distance in memory between two pixels vertically next to each other. </i><br />
 int <code>bitdepth</code><br />
 <i>8 for &#8216;normal&#8217; video precision; data is unsigned bytes centered on 128. </i></p>
<h2>Detailed Description</h2>
<p> Representation of a single component within an image or frame. </p>
<h2>Field Documentation</h2>
<h3>unsigned char* daala_image_plane::data</h3>
<p> Image data is stored as an unsigned octet type whether it&#8217;s actually 8 bit or a multi-byte depth.</p>
<h3>unsigned char daala_image_plane::xdec</h3>
<p> The decimation factor in the x and y direction. Pixels are reduced by a factor of 2^xdec so 0 is none, 1 is decimated by a factor of 2. ( YUV420 will have xdec of 1 and ydec also of 1. YUV444 will have xdec and ydec set to zero ).</p>
<h3>int daala_image_plane::xstride</h3>
<p> Distance in memory between two pixels horizontally next to each other. The value is in bytes regardless of the &#8216;actual&#8217; underlying depth (either unsigned bytes for 8 bit video or unsigned 16 bit shorts for high-depth video). The xstride may be larger than the actual data width calculated from the bitdepth; this implies packed rather than planar data.</p>
<h3>int daala_image_plane::ystride</h3>
<p> Distance in memory between two pixels vertically next to each other. As with xstride, this value is always in bytes.</p>
<h3>int daala_image_plane::bitdepth</h3>
<p> 8 for &#8216;normal&#8217; video precision; data is unsigned bytes centered on 128. Greater-than-8 indicates high-depth video; data is unnormalized host-endian order unsigned signed 16-bit shorts (two octets). For example, 10 bit video would declare a bit depth of 10, use the lower 10 bits of each 16 bit short, and center on 512. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for daala from the source code. </p>
<h2>Index</h2>
