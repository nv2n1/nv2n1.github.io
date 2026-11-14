---
title: "evas_object_name_group(3)"
name: "evas_object_name_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_object_name_group/"
description: "Object Name Function – Functions that retrieve and set the name of an evas object."
---

<p>Object Name Function &#8211; Functions that retrieve and set the name of an evas object. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_object_name_set</code> (<code>Evas_Object</code> *obj, const char *name)<br />
 <i>Sets the name of the given evas object to the given name. </i><br />
 EAPI const char * <code>evas_object_name_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves the name of the given evas object. </i><br />
 EAPI <code>Evas_Object</code> * <code>evas_object_name_find</code> (const <code>Evas</code> *e, const char *name)<br />
 <i>Retrieves the object on the given evas with the given name. </i></p>
<h2>Detailed Description</h2>
<p>Functions that retrieve and set the name of an evas object.</p>
<h2>Function Documentation</h2>
<h3>EAPI <code>Evas_Object</code>* evas_object_name_find (const <code>Evas</code> * e, const char * name)</h3>
<p>Retrieves the object on the given evas with the given name. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The given evas.<br />
 <i>name</i> The given name.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>If successful, the evas object with the given name. Otherwise, NULL.</dl>
<p> References evas_hash_find().</p>
<h3>EAPI const char* evas_object_name_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves the name of the given evas object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The name of the object. NULL if no name has been given to the object.</dl>
<h3>EAPI void evas_object_name_set (<code>Evas_Object</code> * obj, const char * name)</h3>
<p>Sets the name of the given evas object to the given name. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given object.<br />
 <i>name</i> The given name.</dl>
<p> References evas_hash_add(), and evas_hash_del(). </p>
<p> Referenced by evas_object_del().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
