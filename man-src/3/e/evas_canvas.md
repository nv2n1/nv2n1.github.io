---
title: "evas_canvas(3)"
name: "evas_canvas"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_canvas/"
description: "Evas Canvas – Functions that deal with the basic evas object."
---

<p>Evas Canvas &#8211; Functions that deal with the basic evas object. </p>
<h3>Functions</h3>
<p>EAPI <code>Evas</code> * <code>evas_new</code> (void)<br />
 <i>Creates a new empty evas. </i><br />
 EAPI void <code>evas_free</code> (<code>Evas</code> *e)<br />
 <i>Frees the given evas and any objects created on it. </i></p>
<h2>Detailed Description</h2>
<p>Functions that deal with the basic evas object. </p>
<p> They are the functions you need to use at a minimum to get a working evas, and to destroy it.</p>
<h2>Function Documentation</h2>
<h3>EAPI void evas_free (<code>Evas</code> * e)</h3>
<p>Frees the given evas and any objects created on it. </p>
<p> Any objects with &#8216;free&#8217; callbacks will have those callbacks called in this function. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The given evas.</dl>
<p> References evas_font_path_clear(), evas_hash_free(), evas_list_free(), and evas_list_remove().</p>
<h3>EAPI <code>Evas</code>* evas_new (void)</h3>
<p>Creates a new empty evas. </p>
<p> Note that before you can use the evas, you will to at a minimum: </p>
<dl COMPACT>
<dt>*</p>
<dd>Set its render method with <code>evas_output_method_set</code> .</p>
<dt>*</p>
<dd>Set its viewport size with <code>evas_output_viewport_set</code> .</p>
<dt>*</p>
<dd>Set its size of the canvas with <code>evas_output_size_set</code> .</p>
<dt>*</p>
<dd>Ensure that the render engine is given the correct settings with <code>evas_engine_info_set</code> .</dl>
<p> This function should only fail if the memory allocation fails. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new uninitialised Evas canvas on success. Otherwise, NULL.</dl>
<p> References EVAS_FONT_HINTING_BYTECODE.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
