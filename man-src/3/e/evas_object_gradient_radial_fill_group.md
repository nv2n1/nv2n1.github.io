---
title: "evas_object_gradient_radial_fill_group(3)"
name: "evas_object_gradient_radial_fill_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_object_gradient_radial_fill_group/"
description: "Radial_Gradient Object Fill Functions – Functions that deal with the fill geometry of the radial gradient object."
---

<p>Radial_Gradient Object Fill Functions &#8211; Functions that deal with the fill geometry of the radial gradient object. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_object_gradient2_radial_fill_set</code> (<code>Evas_Object</code> *obj, float cx, float cy, float rx, float ry)<br />
 <i>Sets the center and radii of the radial gradient geometry for the object. </i></p>
<h2>Detailed Description</h2>
<p>Functions that deal with the fill geometry of the radial gradient object.</p>
<h2>Function Documentation</h2>
<h3>EAPI void evas_object_gradient2_radial_fill_set (<code>Evas_Object</code> * obj, float cx, float cy, float rx, float ry)</h3>
<p>Sets the center and radii of the radial gradient geometry for the object. </p>
<p> Note that the gradient may extend beyond these, according to its spread value &#8211; restrict, repeat, or reflect. To have only one &#8216;cycle&#8217; of the gradient drawn, the spread value must be set to restrict. The default values for the fill parameters is cx = 0, cy = 0, rx = 0 and ry = 0. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas radial gradient object.<br />
 <i>cx</i> The X coordinate of the start point.<br />
 <i>cy</i> The Y coordinate of the start point.<br />
 <i>rx</i> The length of the x-cordinate radius.<br />
 <i>ry</i> The length of the y-coordinate radius.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
