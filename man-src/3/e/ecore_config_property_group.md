---
title: "ecore_config_property_group(3)"
name: "ecore_config_property_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_config_property_group/"
description: "Ecore Config Property Functions – Functions that retrieve or set the attributes relating to a property."
---

<p>Ecore Config Property Functions &#8211; Functions that retrieve or set the attributes relating to a property. </p>
<h3>Functions</h3>
<p>EAPI <code>Ecore_Config_Prop</code> * <code>ecore_config_dst</code> (<code>Ecore_Config_Prop</code> *e)<br />
 <i>Removes the given property from the local configuration and destroys it. </i><br />
 EAPI const char * <code>ecore_config_type_get</code> (const <code>Ecore_Config_Prop</code> *e)<br />
 <i>Returns the type of the property. </i><br />
 EAPI int <code>ecore_config_describe</code> (const char *key, const char *desc)<br />
 <i>Sets the description field of the indicated property. </i><br />
 EAPI int <code>ecore_config_short_opt_set</code> (const char *key, char short_opt)<br />
 <i>Set the short option character of a property. </i><br />
 EAPI int <code>ecore_config_long_opt_set</code> (const char *key, const char *long_opt)<br />
 <i>Set the long option string of the property. </i><br />
 EAPI int <code>ecore_config_typed_set</code> (const char *key, const void *val, int type)<br />
 <i>Sets the indicated property to the given value and type. </i></p>
<h2>Detailed Description</h2>
<p>Functions that retrieve or set the attributes relating to a property.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_config_describe (const char * key, const char * desc)</h3>
<p>Sets the description field of the indicated property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>desc</i> Description string.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The description string is copied for the property&#8217;s use. You can free desc once this function is called.</dl>
<p> References ecore_config_get(). </p>
<p> Referenced by ecore_config_typed_create().</p>
<h3>EAPI <code>Ecore_Config_Prop</code>* ecore_config_dst (<code>Ecore_Config_Prop</code> * e)</h3>
<p>Removes the given property from the local configuration and destroys it. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> Property to destroy.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>NULL</dl>
<p> References ECORE_CONFIG_STR, ECORE_CONFIG_THM, and Ecore_Config_Prop::listeners. </p>
<p> Referenced by ecore_config_system_shutdown().</p>
<h3>EAPI int ecore_config_long_opt_set (const char * key, const char * long_opt)</h3>
<p>Set the long option string of the property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>long_opt</i> String used to indicate the value of a property given on the command line.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC on success. ECORE_CONFIG_ERR_NODATA is returned if the property does not exist.</dl>
<p> References ecore_config_get(). </p>
<p> Referenced by ecore_config_typed_create().</p>
<h3>EAPI int ecore_config_short_opt_set (const char * key, char short_opt)</h3>
<p>Set the short option character of a property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>short_opt</i> Character used to indicate the value of a property given on the command line.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC on success. ECORE_CONFIG_ERR_NODATA is returned if the property does not exist.</dl>
<p> References ecore_config_get(). </p>
<p> Referenced by ecore_config_typed_create().</p>
<h3>EAPI const char* ecore_config_type_get (const <code>Ecore_Config_Prop</code> * e)</h3>
<p>Returns the type of the property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> Property to get the type of.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The type of the property. If the property is invalid, then the string &#8216;not found&#8217; is returned.</dl>
<h3>EAPI int ecore_config_typed_set (const char * key, const void * val, int type)</h3>
<p>Sets the indicated property to the given value and type. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> A pointer to the value to set the property to.<br />
 <i>type</i> The type of the property.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if the property is set successfully.</dl>
<p> References ecore_config_get(). </p>
<p> Referenced by ecore_config_argb_set(), ecore_config_argbint_set(), ecore_config_argbstr_set(), ecore_config_boolean_set(), ecore_config_float_set(), ecore_config_int_set(), ecore_config_set(), ecore_config_string_set(), and ecore_config_theme_set().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
