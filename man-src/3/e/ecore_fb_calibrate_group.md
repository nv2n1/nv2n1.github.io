---
title: "ecore_fb_calibrate_group(3)"
name: "ecore_fb_calibrate_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_fb_calibrate_group/"
description: "Framebuffer Calibration Functions – Functions that calibrate the screen."
---

<p>Framebuffer Calibration Functions &#8211; Functions that calibrate the screen. </p>
<h3>Functions</h3>
<p>EAPI void <code>ecore_fb_touch_screen_calibrate_set</code> (int xscale, int xtrans, int yscale, int ytrans, int xyswap)<br />
 <i>Calibrates the touschreen using the given parameters. </i><br />
 EAPI void <code>ecore_fb_touch_screen_calibrate_get</code> (int *xscale, int *xtrans, int *yscale, int *ytrans, int *xyswap)<br />
 <i>Retrieves the calibration parameters of the touchscreen. </i></p>
<h2>Detailed Description</h2>
<p>Functions that calibrate the screen.</p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_fb_touch_screen_calibrate_get (int * xscale, int * xtrans, int * yscale, int * ytrans, int * xyswap)</h3>
<p>Retrieves the calibration parameters of the touchscreen. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xscale</i> Pointer to an integer in which to store the X scaling. Note that 256 = 1.0.<br />
 <i>xtrans</i> Pointer to an integer in which to store the X translation.<br />
 <i>yscale</i> Pointer to an integer in which to store the Y scaling.<br />
 <i>ytrans</i> Pointer to an integer in which to store the Y translation.<br />
 <i>xyswap</i> Pointer to an integer in which to store the Swap X &amp; Y flag.</dl>
<h3>EAPI void ecore_fb_touch_screen_calibrate_set (int xscale, int xtrans, int yscale, int ytrans, int xyswap)</h3>
<p>Calibrates the touschreen using the given parameters. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xscale</i> X scaling, where 256 = 1.0<br />
 <i>xtrans</i> X translation.<br />
 <i>yscale</i> Y scaling.<br />
 <i>ytrans</i> Y translation.<br />
 <i>xyswap</i> Swap X &amp; Y flag.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
