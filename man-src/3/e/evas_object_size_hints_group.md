---
title: "evas_object_size_hints_group(3)"
name: "evas_object_size_hints_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_object_size_hints_group/"
description: "Generic Object Size Hints Functions – Functions that deals with hints about object size."
---

<p>Generic Object Size Hints Functions &#8211; Functions that deals with hints about object size. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_object_size_hint_min_get</code> (const <code>Evas_Object</code> *obj, Evas_Coord *w, Evas_Coord *h)<br />
 <i>Retrieves the size hint for the minimum size. </i><br />
 EAPI void <code>evas_object_size_hint_min_set</code> (<code>Evas_Object</code> *obj, Evas_Coord w, Evas_Coord h)<br />
 <i>Sets the size hint for the minimum size. </i><br />
 EAPI void <code>evas_object_size_hint_max_get</code> (const <code>Evas_Object</code> *obj, Evas_Coord *w, Evas_Coord *h)<br />
 <i>Retrieves the size hint for the maximum size. </i><br />
 EAPI void <code>evas_object_size_hint_max_set</code> (<code>Evas_Object</code> *obj, Evas_Coord w, Evas_Coord h)<br />
 <i>Sets the size hint for the maximum size. </i><br />
 EAPI void <code>evas_object_size_hint_request_get</code> (const <code>Evas_Object</code> *obj, Evas_Coord *w, Evas_Coord *h)<br />
 <i>Retrieves the size request hint. </i><br />
 EAPI void <code>evas_object_size_hint_request_set</code> (<code>Evas_Object</code> *obj, Evas_Coord w, Evas_Coord h)<br />
 <i>Sets the requested size hint. </i><br />
 EAPI void <code>evas_object_size_hint_aspect_get</code> (const <code>Evas_Object</code> *obj, Evas_Aspect_Control *aspect, Evas_Coord *w, Evas_Coord *h)<br />
 <i>Retrieves the size aspect control hint. </i><br />
 EAPI void <code>evas_object_size_hint_aspect_set</code> (<code>Evas_Object</code> *obj, Evas_Aspect_Control aspect, Evas_Coord w, Evas_Coord h)<br />
 <i>Sets the size aspect control hint. </i></p>
<h2>Detailed Description</h2>
<p>Functions that deals with hints about object size.</p>
<h2>Function Documentation</h2>
<h3>EAPI void evas_object_size_hint_aspect_get (const <code>Evas_Object</code> * obj, Evas_Aspect_Control * aspect, Evas_Coord * w, Evas_Coord * h)</h3>
<p>Retrieves the size aspect control hint. </p>
<p> This is not a size enforcement in any way, it&#8217;s just a hint that should be used whenever appropriate. </p>
<p> Note that if any of aspect, w or h are NULL, the NULL parameters are ignored. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.<br />
 <i>aspect</i> Returns the hint on how size should be calculated.<br />
 <i>w</i> Pointer to an integer in which to store the aspect width.<br />
 <i>h</i> Pointer to an integer in which to store the aspect height.</dl>
<h3>EAPI void evas_object_size_hint_aspect_set (<code>Evas_Object</code> * obj, Evas_Aspect_Control aspect, Evas_Coord w, Evas_Coord h)</h3>
<p>Sets the size aspect control hint. </p>
<p> This is not a size enforcement in any way, it&#8217;s just a hint that should be used whenever appropriate. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.<br />
 <i>aspect</i> Hint on how to calculate size.<br />
 <i>w</i> Integer to use as aspect width hint.<br />
 <i>h</i> Integer to use as aspect height hint.</dl>
<h3>EAPI void evas_object_size_hint_max_get (const <code>Evas_Object</code> * obj, Evas_Coord * w, Evas_Coord * h)</h3>
<p>Retrieves the size hint for the maximum size. </p>
<p> This is not a size enforcement in any way, it&#8217;s just a hint that should be used whenever appropriate. </p>
<p> Note that if any of w or h are NULL, the NULL parameters are ignored. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.<br />
 <i>w</i> Pointer to an integer in which to store the maximum width.<br />
 <i>h</i> Pointer to an integer in which to store the maximum height.</dl>
<h3>EAPI void evas_object_size_hint_max_set (<code>Evas_Object</code> * obj, Evas_Coord w, Evas_Coord h)</h3>
<p>Sets the size hint for the maximum size. </p>
<p> This is not a size enforcement in any way, it&#8217;s just a hint that should be used whenever appropriate. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.<br />
 <i>w</i> Integer to use as the maximum width hint.<br />
 <i>h</i> Integer to use as the maximum height hint.</dl>
<h3>EAPI void evas_object_size_hint_min_get (const <code>Evas_Object</code> * obj, Evas_Coord * w, Evas_Coord * h)</h3>
<p>Retrieves the size hint for the minimum size. </p>
<p> This is not a size enforcement in any way, it&#8217;s just a hint that should be used whenever appropriate. </p>
<p> Note that if any of w or h are NULL, the NULL parameters are ignored. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.<br />
 <i>w</i> Pointer to an integer in which to store the minimum width.<br />
 <i>h</i> Pointer to an integer in which to store the minimum height.</dl>
<h3>EAPI void evas_object_size_hint_min_set (<code>Evas_Object</code> * obj, Evas_Coord w, Evas_Coord h)</h3>
<p>Sets the size hint for the minimum size. </p>
<p> This is not a size enforcement in any way, it&#8217;s just a hint that should be used whenever appropriate. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.<br />
 <i>w</i> Integer to use as the minimum width hint.<br />
 <i>h</i> Integer to use as the minimum height hint.</dl>
<h3>EAPI void evas_object_size_hint_request_get (const <code>Evas_Object</code> * obj, Evas_Coord * w, Evas_Coord * h)</h3>
<p>Retrieves the size request hint. </p>
<p> This is not a size enforcement in any way, it&#8217;s just a hint that should be used whenever appropriate. </p>
<p> Note that if any of w or h are NULL, the NULL parameters are ignored. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.<br />
 <i>w</i> Pointer to an integer in which to store the requested width.<br />
 <i>h</i> Pointer to an integer in which to store the requested height.</dl>
<h3>EAPI void evas_object_size_hint_request_set (<code>Evas_Object</code> * obj, Evas_Coord w, Evas_Coord h)</h3>
<p>Sets the requested size hint. </p>
<p> This is not a size enforcement in any way, it&#8217;s just a hint that should be used whenever appropriate. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>obj</i> The given evas object.<br />
 <i>w</i> Integer to use as the preferred width hint.<br />
 <i>h</i> Integer to use as the preferred height hint.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
