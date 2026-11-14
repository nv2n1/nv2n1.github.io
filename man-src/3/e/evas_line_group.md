---
title: "evas_line_group(3)"
name: "evas_line_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_line_group/"
description: "Line Functions – Functions used to deal with evas line objects."
---

<p>Line Functions &#8211; Functions used to deal with evas line objects. </p>
<h3>Functions</h3>
<p>EAPI <code>Evas_Object</code> * <code>evas_object_line_add</code> (<code>Evas</code> *e)<br />
 <i>Adds a new evas line object to the given evas. </i><br />
 EAPI void <code>evas_object_line_xy_set</code> (<code>Evas_Object</code> *obj, Evas_Coord x1, Evas_Coord y1, Evas_Coord x2, Evas_Coord y2)<br />
 <i>Sets the coordinates of the end points of the given evas line object. </i><br />
 EAPI void <code>evas_object_line_xy_get</code> (const <code>Evas_Object</code> *obj, Evas_Coord *x1, Evas_Coord *y1, Evas_Coord *x2, Evas_Coord *y2)<br />
 <i>Retrieves the coordinates of the end points of the given evas line object. </i></p>
<h2>Detailed Description</h2>
<p>Functions used to deal with evas line objects.</p>
<h2>Function Documentation</h2>
<h3>EAPI <code>Evas_Object</code>* evas_object_line_add (<code>Evas</code> * e)</h3>
<p>Adds a new evas line object to the given evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The given evas.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The new evas line object.</dl>
<h3>EAPI void evas_object_line_xy_get (const <code>Evas_Object</code> * obj, Evas_Coord * x1, Evas_Coord * y1, Evas_Coord * x2, Evas_Coord * y2)</h3>
<p>Retrieves the coordinates of the end points of the given evas line object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given line object.<br />
 <i>x1</i> Pointer to an integer in which to store the X coordinate of the first end point.<br />
 <i>y1</i> Pointer to an integer in which to store the Y coordinate of the first end point.<br />
 <i>x2</i> Pointer to an integer in which to store the X coordinate of the second end point.<br />
 <i>y2</i> Pointer to an integer in which to store the Y coordinate of the second end point.</dl>
<h3>EAPI void evas_object_line_xy_set (<code>Evas_Object</code> * obj, Evas_Coord x1, Evas_Coord y1, Evas_Coord x2, Evas_Coord y2)</h3>
<p>Sets the coordinates of the end points of the given evas line object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas line object.<br />
 <i>x1</i> The X coordinate of the first point.<br />
 <i>y1</i> The Y coordinate of the first point.<br />
 <i>x2</i> The X coordinate of the second point.<br />
 <i>y2</i> The Y coordinate of the second point.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
