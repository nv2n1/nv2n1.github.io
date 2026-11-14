---
title: "evas_object_gradient_type_group(3)"
name: "evas_object_gradient_type_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_object_gradient_type_group/"
description: "Gradient Object Type Functions – Functions that set or get a gradient’s geometric type."
---

<p>Gradient Object Type Functions &#8211; Functions that set or get a gradient&#8217;s geometric type. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_object_gradient_type_set</code> (<code>Evas_Object</code> *obj, const char *name, const char *params)<br />
 <i>Sets the geometric type displayed by the given gradient object. </i><br />
 EAPI void <code>evas_object_gradient_type_get</code> (const <code>Evas_Object</code> *obj, char **name, char **params)<br />
 <i>Retrieves the type name and params of the given gradient object. </i></p>
<h2>Detailed Description</h2>
<p>Functions that set or get a gradient&#8217;s geometric type. </p>
<p> Examples are &#8216;linear&#8217;, &#8216;linear.diag&#8217;, &#8216;linear.codiag&#8217;, &#8216;radial&#8217;, &#8216;rectangular&#8217;, &#8216;angular&#8217;, &#8216;sinusoidal&#8217;, &#8230; Some types may accept additional parameters to further specify the look.</p>
<h2>Function Documentation</h2>
<h3>EAPI void evas_object_gradient_type_get (const <code>Evas_Object</code> * obj, char ** name, char ** params)</h3>
<p>Retrieves the type name and params of the given gradient object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given gradient object.<br />
 <i>name</i> Pointer to a character pointer to store the pointer to the type name in.<br />
 <i>params</i> Pointer to a character pointer to store the pointer to the type params string in.</dl>
<h3>EAPI void evas_object_gradient_type_set (<code>Evas_Object</code> * obj, const char * name, const char * params)</h3>
<p>Sets the geometric type displayed by the given gradient object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given gradient object.<br />
 <i>name</i> Name of the geometric type that the gradient is to be drawn as.<br />
 <i>params</i> List of allowable params that the given gradient type allows. Can be NULL.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
