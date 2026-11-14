---
title: "ecore_config_struct_group(3)"
name: "ecore_config_struct_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_config_struct_group/"
description: "Ecore Config Structures – Functions that are used to create structures of properties."
---

<p>Ecore Config Structures &#8211; Functions that are used to create structures of properties. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_config_struct_create</code> (const char *key)<br />
 <i>Sets the indicated property to a structure if the property has not yet been set. </i><br />
 EAPI int <code>ecore_config_struct_int_add</code> (const char *key, const char *name, int val)<br />
 <i>Add an int property to the named structure. </i><br />
 EAPI int <code>ecore_config_struct_float_add</code> (const char *key, const char *name, float val)<br />
 <i>Add a float property to the named structure. </i><br />
 EAPI int <code>ecore_config_struct_string_add</code> (const char *key, const char *name, const char *val)<br />
 <i>Add a string property to the named structure. </i><br />
 EAPI int <code>ecore_config_struct_argb_add</code> (const char *key, const char *name, int a, int r, int g, int b)<br />
 <i>Add an argb property to the named structure. </i><br />
 EAPI int <code>ecore_config_struct_theme_add</code> (const char *key, const char *name, const char *val)<br />
 <i>Add a theme property to the named structure. </i><br />
 EAPI int <code>ecore_config_struct_boolean_add</code> (const char *key, const char *name, int val)<br />
 <i>Add a boolean property to the named structure. </i><br />
 EAPI int <code>ecore_config_struct_get</code> (const char *key, void *data)<br />
 <i>Get the contents of a defined structure property and load it into the passed C struct. </i></p>
<h2>Detailed Description</h2>
<p>Functions that are used to create structures of properties.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_config_struct_argb_add (const char * key, const char * name, int a, int r, int g, int b)</h3>
<p>Add an argb property to the named structure. </p>
<p> The property is set if it has not yet been set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The key of the structure to add to.<br />
 <i>name</i> The name of the item to add &#8211; this will be appended to the key<br />
 <i>a</i> The alpha to default to<br />
 <i>r</i> The red to default to<br />
 <i>g</i> The green to default to<br />
 <i>b</i> The blue to default to</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if the property is set successfully.</dl>
<p> References ECORE_CONFIG_RGB.</p>
<h3>EAPI int ecore_config_struct_boolean_add (const char * key, const char * name, int val)</h3>
<p>Add a boolean property to the named structure. </p>
<p> The property is set if it has not yet been set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The key of the structure to add to.<br />
 <i>name</i> The name of the item to add &#8211; this will be appended to the key<br />
 <i>val</i> The boolean to default to</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if the property is set successfully.</dl>
<p> References ECORE_CONFIG_BLN.</p>
<h3>EAPI int ecore_config_struct_create (const char * key)</h3>
<p>Sets the indicated property to a structure if the property has not yet been set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if the property is set successfully.</dl>
<p> References ECORE_CONFIG_SCT.</p>
<h3>EAPI int ecore_config_struct_float_add (const char * key, const char * name, float val)</h3>
<p>Add a float property to the named structure. </p>
<p> The property is set if it has not yet been set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The key of the structure to add to.<br />
 <i>name</i> The name of the item to add &#8211; this will be appended to the key<br />
 <i>val</i> The float to default to</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if the property is set successfully.</dl>
<p> References ECORE_CONFIG_FLT.</p>
<h3>EAPI int ecore_config_struct_get (const char * key, void * data)</h3>
<p>Get the contents of a defined structure property and load it into the passed C struct. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The name of the structure property to look up.<br />
 <i>data</i> The struct to write into.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if the structure is written successfully.</dl>
<p> References ECORE_CONFIG_BLN, ECORE_CONFIG_FLT, ecore_config_get(), ECORE_CONFIG_INT, ECORE_CONFIG_RGB, ECORE_CONFIG_STR, and ECORE_CONFIG_THM.</p>
<h3>EAPI int ecore_config_struct_int_add (const char * key, const char * name, int val)</h3>
<p>Add an int property to the named structure. </p>
<p> The property is set if it has not yet been set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The key of the structure to add to.<br />
 <i>name</i> The name of the item to add &#8211; this will be appended to the key<br />
 <i>val</i> the int to default to</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if the property is set successfully.</dl>
<p> References ECORE_CONFIG_INT.</p>
<h3>EAPI int ecore_config_struct_string_add (const char * key, const char * name, const char * val)</h3>
<p>Add a string property to the named structure. </p>
<p> The property is set if it has not yet been set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The key of the structure to add to.<br />
 <i>name</i> The name of the item to add &#8211; this will be appended to the key<br />
 <i>val</i> The string to default to</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if the property is set successfully.</dl>
<p> References ECORE_CONFIG_STR.</p>
<h3>EAPI int ecore_config_struct_theme_add (const char * key, const char * name, const char * val)</h3>
<p>Add a theme property to the named structure. </p>
<p> The property is set if it has not yet been set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The key of the structure to add to.<br />
 <i>name</i> The name of the item to add &#8211; this will be appended to the key<br />
 <i>val</i> The theme name to default to</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if the property is set successfully.</dl>
<p> References ECORE_CONFIG_THM.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
