---
title: "evas_object_visibility_group(3)"
name: "evas_object_visibility_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_object_visibility_group/"
description: "Generic Object Visibility Functions – Functions that deal with the visibility of evas objects."
---

<p>Generic Object Visibility Functions &#8211; Functions that deal with the visibility of evas objects. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_object_show</code> (<code>Evas_Object</code> *obj)<br />
 <i>Makes the given evas object visible. </i><br />
 EAPI void <code>evas_object_hide</code> (<code>Evas_Object</code> *obj)<br />
 <i>Makes the given evas object invisible. </i><br />
 EAPI Evas_Bool <code>evas_object_visible_get</code> (const <code>Evas_Object</code> *obj)<br />
 <i>Retrieves whether or not the given evas object is visible. </i></p>
<h2>Detailed Description</h2>
<p>Functions that deal with the visibility of evas objects.</p>
<h2>Function Documentation</h2>
<h3>EAPI void evas_object_hide (<code>Evas_Object</code> * obj)</h3>
<p>Makes the given evas object invisible. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.</dl>
<p> References _Evas_Event_Mouse_Out::buttons, EVAS_CALLBACK_MOUSE_OUT, and evas_list_remove(). </p>
<p> Referenced by evas_object_del(), and evas_object_smart_clipped_member_del().</p>
<h3>EAPI void evas_object_show (<code>Evas_Object</code> * obj)</h3>
<p>Makes the given evas object visible. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.</dl>
<p> Referenced by evas_object_smart_clipped_member_add().</p>
<h3>EAPI Evas_Bool evas_object_visible_get (const <code>Evas_Object</code> * obj)</h3>
<p>Retrieves whether or not the given evas object is visible. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if the object is visible. 0 otherwise.</dl>
<p> Referenced by evas_object_smart_clipped_member_add().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
