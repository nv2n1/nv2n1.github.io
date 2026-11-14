---
title: "evas_polygon_group(3)"
name: "evas_polygon_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_polygon_group/"
description: "Polygon Functions – Functions that operate on evas polygon objects."
---

<p>Polygon Functions &#8211; Functions that operate on evas polygon objects. </p>
<h3>Functions</h3>
<p>EAPI <code>Evas_Object</code> * <code>evas_object_polygon_add</code> (<code>Evas</code> *e)<br />
 <i>Adds a new evas polygon object to the given evas. </i><br />
 EAPI void <code>evas_object_polygon_point_add</code> (<code>Evas_Object</code> *obj, Evas_Coord x, Evas_Coord y)<br />
 <i>Adds the given point to the given evas polygon object. </i><br />
 EAPI void <code>evas_object_polygon_points_clear</code> (<code>Evas_Object</code> *obj)<br />
 <i>Removes all of the points from the given evas polygon object. </i></p>
<h2>Detailed Description</h2>
<p>Functions that operate on evas polygon objects.</p>
<h2>Function Documentation</h2>
<h3>EAPI <code>Evas_Object</code>* evas_object_polygon_add (<code>Evas</code> * e)</h3>
<p>Adds a new evas polygon object to the given evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The given evas.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new evas polygon object.</dl>
<h3>EAPI void evas_object_polygon_point_add (<code>Evas_Object</code> * obj, Evas_Coord x, Evas_Coord y)</h3>
<p>Adds the given point to the given evas polygon object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas polygon object.<br />
 <i>x</i> The X coordinate of the given point.<br />
 <i>y</i> The Y coordinate of the given point.</dl>
<p> References evas_list_append().</p>
<h3>EAPI void evas_object_polygon_points_clear (<code>Evas_Object</code> * obj)</h3>
<p>Removes all of the points from the given evas polygon object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given polygon object.</dl>
<p> References evas_list_remove().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
