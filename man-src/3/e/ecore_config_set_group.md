---
title: "ecore_config_set_group(3)"
name: "ecore_config_set_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_config_set_group/"
description: "Ecore Config Setters – Functions that set the value of a property."
---

<p>Ecore Config Setters &#8211; Functions that set the value of a property. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_config_set</code> (const char *key, const char *val)<br />
 <i>Sets the indicated property to the value indicated by val</i>.<br />
 EAPI int <code>ecore_config_as_string_set</code> (const char *key, const char *val)<br />
 <i>Sets the indicated property to the value given in the string. </i><br />
 EAPI int <code>ecore_config_boolean_set</code> (const char *key, int val)<br />
 <i>Sets the indicated property to the given boolean. </i><br />
 EAPI int <code>ecore_config_int_set</code> (const char *key, int val)<br />
 <i>Sets the indicated property to the given integer. </i><br />
 EAPI int <code>ecore_config_string_set</code> (const char *key, const char *val)<br />
 <i>Sets the indicated property to the given string. </i><br />
 EAPI int <code>ecore_config_float_set</code> (const char *key, float val)<br />
 <i>Sets the indicated property to the given float value. </i><br />
 EAPI int <code>ecore_config_argb_set</code> (const char *key, int a, int r, int g, int b)<br />
 <i>Sets the indicated property to a color value. </i><br />
 EAPI int <code>ecore_config_argbint_set</code> (const char *key, long argb)<br />
 <i>Sets the indicated property to a color value. </i><br />
 EAPI int <code>ecore_config_argbstr_set</code> (const char *key, const char *val)<br />
 <i>Sets the indicated property to a color value. </i><br />
 EAPI int <code>ecore_config_theme_set</code> (const char *key, const char *val)<br />
 <i>Sets the indicated property to a theme name. </i><br />
 EAPI int <code>ecore_config_theme_preview_group_set</code> (const char *key, const char *group)<br />
 <i>Sets the theme preview group of an indicated property. </i></p>
<h2>Detailed Description</h2>
<p>Functions that set the value of a property.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_config_argb_set (const char * key, int a, int r, int g, int b)</h3>
<p>Sets the indicated property to a color value. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key<br />
 <i>a</i> integer 0..255<br />
 <i>r</i> integer 0..255<br />
 <i>g</i> integer 0..255<br />
 <i>b</i> integer 0..255</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if the property is set successfully.</dl>
<p> References ECORE_CONFIG_RGB, and ecore_config_typed_set().</p>
<h3>EAPI int ecore_config_argbint_set (const char * key, long argb)</h3>
<p>Sets the indicated property to a color value. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key<br />
 <i>argb</i> ARGB data as long</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if the property is set successfully.</dl>
<p> References ECORE_CONFIG_RGB, and ecore_config_typed_set().</p>
<h3>EAPI int ecore_config_argbstr_set (const char * key, const char * val)</h3>
<p>Sets the indicated property to a color value. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key<br />
 <i>val</i> Color value in ARGB format.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if the property is set successfully.</dl>
<p> References ECORE_CONFIG_RGB, and ecore_config_typed_set().</p>
<h3>EAPI int ecore_config_as_string_set (const char * key, const char * val)</h3>
<p>Sets the indicated property to the value given in the string. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> String representation of the value.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if the property is set successfully.</dl>
<p> References ecore_config_set().</p>
<h3>EAPI int ecore_config_boolean_set (const char * key, int val)</h3>
<p>Sets the indicated property to the given boolean. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> Boolean integer to set the property to.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if the property is set successfully.</dl>
<p> References ECORE_CONFIG_BLN, and ecore_config_typed_set().</p>
<h3>EAPI int ecore_config_float_set (const char * key, float val)</h3>
<p>Sets the indicated property to the given float value. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> Float to set the property to.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if the property is set successfully.</dl>
<p> References ECORE_CONFIG_FLT, and ecore_config_typed_set().</p>
<h3>EAPI int ecore_config_int_set (const char * key, int val)</h3>
<p>Sets the indicated property to the given integer. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> Integer to set the property to.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if the property is set successfully.</dl>
<p> References ECORE_CONFIG_INT, and ecore_config_typed_set().</p>
<h3>EAPI int ecore_config_set (const char * key, const char * val)</h3>
<p>Sets the indicated property to the value indicated by <i>val</i>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> String representation of value to set.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if the property is set successfully.</dl>
<p> References ECORE_CONFIG_BLN, ECORE_CONFIG_FLT, ECORE_CONFIG_INT, ECORE_CONFIG_RGB, and ecore_config_typed_set(). </p>
<p> Referenced by ecore_config_as_string_set().</p>
<h3>EAPI int ecore_config_string_set (const char * key, const char * val)</h3>
<p>Sets the indicated property to the given string. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> String to set the property to.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if the property is set successfully.</dl>
<p> References ECORE_CONFIG_STR, and ecore_config_typed_set(). </p>
<p> Referenced by ecore_config_theme_search_path_append().</p>
<h3>EAPI int ecore_config_theme_preview_group_set (const char * key, const char * group)</h3>
<p>Sets the theme preview group of an indicated property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>group</i> The group name.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC on success.</dl>
<p> References ecore_config_get(), and ECORE_CONFIG_THM.</p>
<h3>EAPI int ecore_config_theme_set (const char * key, const char * val)</h3>
<p>Sets the indicated property to a theme name. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> String giving the name of the theme.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if the property is set successfully.</dl>
<p> References ECORE_CONFIG_THM, and ecore_config_typed_set().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
