---
title: "evas_object_gradient_linear_fill_group(3)"
name: "evas_object_gradient_linear_fill_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_object_gradient_linear_fill_group/"
description: "Linear_Gradient Object Fill Functions – Functions that deal with the fill geometry of the linear gradient object."
---

<p>Linear_Gradient Object Fill Functions &#8211; Functions that deal with the fill geometry of the linear gradient object. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_object_gradient2_linear_fill_set</code> (<code>Evas_Object</code> *obj, float x0, float y0, float x1, float y1)<br />
 <i>Sets the start and end points of the linear gradient geometry for the object. </i></p>
<h2>Detailed Description</h2>
<p>Functions that deal with the fill geometry of the linear gradient object.</p>
<h2>Function Documentation</h2>
<h3>EAPI void evas_object_gradient2_linear_fill_set (<code>Evas_Object</code> * obj, float x0, float y0, float x1, float y1)</h3>
<p>Sets the start and end points of the linear gradient geometry for the object. </p>
<p> Note that the gradient may extend beyond these, according to its spread value &#8211; restrict, repeat, or reflect. To have only one &#8216;cycle&#8217; of the gradient drawn, the spread value must be set to restrict. The default values for the fill parameters is x0 = 0, y0 = 0, x1 = 0 and y1 = 0. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas linear gradient object.<br />
 <i>x0</i> The X coordinate of the start point.<br />
 <i>y0</i> The Y coordinate of the start point.<br />
 <i>x1</i> The X coordinate of the end point.<br />
 <i>y1</i> The Y coordinate of the end point</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
