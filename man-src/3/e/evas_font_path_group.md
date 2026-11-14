---
title: "evas_font_path_group(3)"
name: "evas_font_path_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_font_path_group/"
description: "Font Path Functions – Functions that edit the paths being used to load fonts."
---

<p>Font Path Functions &#8211; Functions that edit the paths being used to load fonts. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_font_path_clear</code> (<code>Evas</code> *e)<br />
 <i>Removes all font paths loaded into memory for the given evas. </i><br />
 EAPI void <code>evas_font_path_append</code> (<code>Evas</code> *e, const char *path)<br />
 <i>Appends a font path to the list of font paths used by the given evas. </i><br />
 EAPI void <code>evas_font_path_prepend</code> (<code>Evas</code> *e, const char *path)<br />
 <i>Prepends a font path to the list of font paths used by the given evas. </i><br />
 EAPI const <code>Evas_List</code> * <code>evas_font_path_list</code> (const <code>Evas</code> *e)<br />
 <i>Retrieves the list of font paths used by the given evas. </i></p>
<h2>Detailed Description</h2>
<p>Functions that edit the paths being used to load fonts.</p>
<h2>Function Documentation</h2>
<h3>EAPI void evas_font_path_append (<code>Evas</code> * e, const char * path)</h3>
<p>Appends a font path to the list of font paths used by the given evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The given evas.<br />
 <i>path</i> The new font path.</dl>
<p> References evas_list_append().</p>
<h3>EAPI void evas_font_path_clear (<code>Evas</code> * e)</h3>
<p>Removes all font paths loaded into memory for the given evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The given evas.</dl>
<p> References evas_list_remove(). </p>
<p> Referenced by evas_free().</p>
<h3>EAPI const <code>Evas_List</code>* evas_font_path_list (const <code>Evas</code> * e)</h3>
<p>Retrieves the list of font paths used by the given evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The given evas.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The list of font paths used.</dl>
<h3>EAPI void evas_font_path_prepend (<code>Evas</code> * e, const char * path)</h3>
<p>Prepends a font path to the list of font paths used by the given evas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The given evas.<br />
 <i>path</i> The new font path.</dl>
<p> References evas_list_prepend().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
