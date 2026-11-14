---
title: "daala_info(3)"
name: "daala_info"
section: "3"
letter: "d"
url: "/docs/linux/man/3-daala_info/"
description: "daala_info –"
---

<h2 class="name">NAME</h2>
<p> daala_info &#8211; </p>
<p> Configuration parameters for a codec instance.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;codec.h&gt;</p>
<h3>Data Fields</h3>
<p> unsigned char <code>version_major</code> </p>
<p> unsigned char <code>version_minor</code> </p>
<p> unsigned char <code>version_sub</code> </p>
<p> int32_t <code>pic_width</code><br />
 <i>pic_width,_height form a region of interest to encode </i><br />
 int32_t <code>pic_height</code> </p>
<p> uint32_t <code>pixel_aspect_numerator</code> </p>
<p> uint32_t <code>pixel_aspect_denominator</code> </p>
<p> uint32_t <code>timebase_numerator</code> </p>
<p> uint32_t <code>timebase_denominator</code> </p>
<p> uint32_t <code>frame_duration</code> </p>
<p> int <code>keyframe_granule_shift</code><br />
 <i>The amount to shift to extract the last keyframe number from the granule position. </i><br />
 int <code>bitdepth_mode</code><br />
 <i>bitdepth_mode is one of the three OD_BITDEPTH_MODE_X choices allowed above. </i><br />
 int <code>full_precision_references</code><br />
 <i>FPR must be on for high-depth, including lossless high-depth. </i><br />
 int <code>nplanes</code> </p>
<p> <code>daala_plane_info</code> <code>plane_info</code> [<code>OD_NPLANES_MAX</code>] </p>
<p> int <code>keyframe_rate</code><br />
 <i>key frame rate defined how often a key frame is emitted by encoder in number of frames. </i></p>
<h2>Detailed Description</h2>
<p> Configuration parameters for a codec instance. </p>
<h2>Field Documentation</h2>
<h3>int daala_info::keyframe_granule_shift</h3>
<p> The amount to shift to extract the last keyframe number from the granule position.</p>
<h3>int daala_info::bitdepth_mode</h3>
<p> bitdepth_mode is one of the three OD_BITDEPTH_MODE_X choices allowed above.</p>
<h3>int daala_info::full_precision_references</h3>
<p> FPR must be on for high-depth, including lossless high-depth. When FPR is on for 8-bit or 10-bit content, lossless frames are still stored in reference buffers (and input buffers) with 8 + OD_COEFF_SHIFT bit depth to allow streams with mixed lossy and lossless frames. Having a mix of reference buffers stored in 10-bit and 12-bit precisions would be a disaster, so we keep them all at 12-bit internally.</p>
<h3>int daala_info::keyframe_rate</h3>
<p> key frame rate defined how often a key frame is emitted by encoder in number of frames. So 10 means every 10th frame is a keyframe. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for daala from the source code. </p>
<h2>Index</h2>
