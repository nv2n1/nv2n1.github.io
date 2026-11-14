---
title: "evas_object_layer_group(3)"
name: "evas_object_layer_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_object_layer_group/"
description: "Object Layer Functions – Functions that retrieve and set the layer that an evas object is on."
---

<p>Object Layer Functions &#8211; Functions that retrieve and set the layer that an evas object is on. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_object_layer_set</code> (<code>Evas_Object</code> *obj, short l)<br />
 <i>Sets the layer of the evas that the given object will be part of. </i><br />
 EAPI short <code>evas_object_layer_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the layer of the evas that the given object is part of. </i></p>
<h2>Detailed Description</h2>
<p>Functions that retrieve and set the layer that an evas object is on. </p>
<p> <code>Todo</code></p>
<dl COMPACT>
<dd>Document which way layers go.</dl>
<h2>Function Documentation</h2>
<h3>EAPI short evas_object_layer_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves the layer of the evas that the given object is part of. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Number of the layer.</dl>
<h3>EAPI void evas_object_layer_set (<code>Evas_Object</code> * obj, short l)</h3>
<p>Sets the layer of the evas that the given object will be part of. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.<br />
 <i>l</i> The number of the layer to place the object on.</dl>
<p> References evas_list_find().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
