---
title: "ecore_config_create_group(3)"
name: "ecore_config_create_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_config_create_group/"
description: "Ecore Config Create Functions – Convenience functions that set default values, bounds, option values and descriptions in one call."
---

<p>Ecore Config Create Functions &#8211; Convenience functions that set default values, bounds, option values and descriptions in one call. </p>
<h3>Functions</h3>
<p>int <code>ecore_config_create</code> (const char *key, void *val, char short_opt, char *long_opt, char *desc)<br />
 <i>Creates a new property, if it does not already exist, and sets its attributes to those given. </i><br />
 int <code>ecore_config_typed_create</code> (const char *key, void *val, int type, char short_opt, char *long_opt, char *desc)<br />
 <i>Creates a new property, if it does not already exist, and sets its attributes to those given. </i><br />
 int <code>ecore_config_boolean_create</code> (const char *key, int val, char short_opt, char *long_opt, char *desc)<br />
 <i>Creates a new boolean property, if it does not already exist, and sets its attributes to those given. </i><br />
 int <code>ecore_config_int_create</code> (const char *key, int val, char short_opt, char *long_opt, char *desc)<br />
 <i>Creates a new integer property, if it does not already exist, and sets its attributes to those given. </i><br />
 int <code>ecore_config_int_create_bound</code> (const char *key, int val, int low, int high, int step, char short_opt, char *long_opt, char *desc)<br />
 <i>Creates a new integer property, if it does not already exist, and sets its attributes to those given. </i><br />
 int <code>ecore_config_string_create</code> (const char *key, char *val, char short_opt, char *long_opt, char *desc)<br />
 <i>Creates a new string property, if it does not already exist, and sets its attributes to those given. </i><br />
 int <code>ecore_config_float_create</code> (const char *key, float val, char short_opt, char *long_opt, char *desc)<br />
 <i>Creates a new float property, if it does not already exist, and sets its attributes to those given. </i><br />
 int <code>ecore_config_float_create_bound</code> (const char *key, float val, float low, float high, float step, char short_opt, char *long_opt, char *desc)<br />
 <i>Creates a new float property, if it does not already exist, and sets its attributes to those given. </i><br />
 int <code>ecore_config_argb_create</code> (const char *key, char *val, char short_opt, char *long_opt, char *desc)<br />
 <i>Creates a new color property, if it does not already exist, and sets its attributes to those given. </i><br />
 int <code>ecore_config_theme_create</code> (const char *key, char *val, char short_opt, char *long_opt, char *desc)<br />
 <i>Creates a new theme property, if it does not already exist, and sets its attributes to those given. </i></p>
<h2>Detailed Description</h2>
<p>Convenience functions that set default values, bounds, option values and descriptions in one call.</p>
<h2>Function Documentation</h2>
<h3>int ecore_config_argb_create (const char * key, char * val, char short_opt, char * long_opt, char * desc)</h3>
<p>Creates a new color property, if it does not already exist, and sets its attributes to those given. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> Default color value of key, as a hexadecimal string.<br />
 <i>short_opt</i> Short option used to set the property from command line.<br />
 <i>long_opt</i> Long option used to set the property from command line.<br />
 <i>desc</i> String description of property.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC on success.</dl>
<p> References ECORE_CONFIG_RGB, and ecore_config_typed_create().</p>
<h3>int ecore_config_boolean_create (const char * key, int val, char short_opt, char * long_opt, char * desc)</h3>
<p>Creates a new boolean property, if it does not already exist, and sets its attributes to those given. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> Default boolean value of key.<br />
 <i>short_opt</i> Short option used to set the property from command line.<br />
 <i>long_opt</i> Long option used to set the property from command line.<br />
 <i>desc</i> String description of property.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC on success.</dl>
<p> References ECORE_CONFIG_BLN, and ecore_config_typed_create().</p>
<h3>int ecore_config_create (const char * key, void * val, char short_opt, char * long_opt, char * desc)</h3>
<p>Creates a new property, if it does not already exist, and sets its attributes to those given. </p>
<p> The type of the property is guessed from the key and the value given. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> Pointer to default value of key.<br />
 <i>short_opt</i> Short option used to set the property from command line.<br />
 <i>long_opt</i> Long option used to set the property from command line.<br />
 <i>desc</i> String description of property.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC on success.</dl>
<p> References ecore_config_typed_create().</p>
<h3>int ecore_config_float_create (const char * key, float val, char short_opt, char * long_opt, char * desc)</h3>
<p>Creates a new float property, if it does not already exist, and sets its attributes to those given. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> Default float value of key.<br />
 <i>short_opt</i> Short option used to set the property from command line.<br />
 <i>long_opt</i> Long option used to set the property from command line.<br />
 <i>desc</i> String description of property.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC on success.</dl>
<p> References ECORE_CONFIG_FLT, and ecore_config_typed_create().</p>
<h3>int ecore_config_float_create_bound (const char * key, float val, float low, float high, float step, char short_opt, char * long_opt, char * desc)</h3>
<p>Creates a new float property, if it does not already exist, and sets its attributes to those given. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> Default float value of key.<br />
 <i>low</i> Lowest valid float value for the property.<br />
 <i>high</i> Highest valid float value for the property.<br />
 <i>step</i> Increment value for the property.<br />
 <i>short_opt</i> Short option used to set the property from command line.<br />
 <i>long_opt</i> Long option used to set the property from command line.<br />
 <i>desc</i> String description of property.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC on success.</dl>
<p> References ECORE_CONFIG_FLT, ecore_config_get(), and ecore_config_typed_create().</p>
<h3>int ecore_config_int_create (const char * key, int val, char short_opt, char * long_opt, char * desc)</h3>
<p>Creates a new integer property, if it does not already exist, and sets its attributes to those given. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> Default integer value of key.<br />
 <i>short_opt</i> Short option used to set the property from command line.<br />
 <i>long_opt</i> Long option used to set the property from command line.<br />
 <i>desc</i> String description of property.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC on success.</dl>
<p> References ECORE_CONFIG_INT, and ecore_config_typed_create().</p>
<h3>int ecore_config_int_create_bound (const char * key, int val, int low, int high, int step, char short_opt, char * long_opt, char * desc)</h3>
<p>Creates a new integer property, if it does not already exist, and sets its attributes to those given. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> Default integer value of key.<br />
 <i>low</i> Lowest valid integer value for the property.<br />
 <i>high</i> Highest valid integer value for the property.<br />
 <i>step</i> Increment value for the property.<br />
 <i>short_opt</i> Short option used to set the property from command line.<br />
 <i>long_opt</i> Long option used to set the property from command line.<br />
 <i>desc</i> String description of property.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC on success.</dl>
<p> References ecore_config_get(), ECORE_CONFIG_INT, and ecore_config_typed_create().</p>
<h3>int ecore_config_string_create (const char * key, char * val, char short_opt, char * long_opt, char * desc)</h3>
<p>Creates a new string property, if it does not already exist, and sets its attributes to those given. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> Default value of key.<br />
 <i>short_opt</i> Short option used to set the property from command line.<br />
 <i>long_opt</i> Long option used to set the property from command line.<br />
 <i>desc</i> String description of property.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC on success.</dl>
<p> References ECORE_CONFIG_STR, and ecore_config_typed_create().</p>
<h3>int ecore_config_theme_create (const char * key, char * val, char short_opt, char * long_opt, char * desc)</h3>
<p>Creates a new theme property, if it does not already exist, and sets its attributes to those given. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> Default theme name for the property.<br />
 <i>short_opt</i> Short option used to set the property from command line.<br />
 <i>long_opt</i> Long option used to set the property from command line.<br />
 <i>desc</i> String description of property.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC on success.</dl>
<p> References ECORE_CONFIG_THM, and ecore_config_typed_create().</p>
<h3>int ecore_config_typed_create (const char * key, void * val, int type, char short_opt, char * long_opt, char * desc)</h3>
<p>Creates a new property, if it does not already exist, and sets its attributes to those given. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> Pointer to default value of key.<br />
 <i>type</i> Type of the property.<br />
 <i>short_opt</i> Short option used to set the property from command line.<br />
 <i>long_opt</i> Long option used to set the property from command line.<br />
 <i>desc</i> String description of property.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC on success.</dl>
<p> References ecore_config_describe(), ecore_config_long_opt_set(), and ecore_config_short_opt_set(). </p>
<p> Referenced by ecore_config_argb_create(), ecore_config_boolean_create(), ecore_config_create(), ecore_config_float_create(), ecore_config_float_create_bound(), ecore_config_int_create(), ecore_config_int_create_bound(), ecore_config_string_create(), and ecore_config_theme_create().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
