---
title: "ecore_config_default_group(3)"
name: "ecore_config_default_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_config_default_group/"
description: "Ecore Config Defaults – Functions that are used to set the default values of properties."
---

<p>Ecore Config Defaults &#8211; Functions that are used to set the default values of properties. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_config_default</code> (const char *key, const char *val, float lo, float hi, float step)<br />
 <i>Sets the indicated property if it has not already been set or loaded. </i><br />
 EAPI int <code>ecore_config_boolean_default</code> (const char *key, int val)<br />
 <i>Sets the indicated property to the given boolean if the property has not yet been set. </i><br />
 EAPI int <code>ecore_config_int_default</code> (const char *key, int val)<br />
 <i>Sets the indicated property to the given integer if the property has not yet been set. </i><br />
 EAPI int <code>ecore_config_int_default_bound</code> (const char *key, int val, int low, int high, int step)<br />
 <i>Sets the indicated property to the given integer if the property has not yet been set. </i><br />
 EAPI int <code>ecore_config_string_default</code> (const char *key, const char *val)<br />
 <i>Sets the indicated property to the given string if the property has not yet been set. </i><br />
 EAPI int <code>ecore_config_float_default</code> (const char *key, float val)<br />
 <i>Sets the indicated property to the given float if the property has not yet been set. </i><br />
 EAPI int <code>ecore_config_float_default_bound</code> (const char *key, float val, float low, float high, float step)<br />
 <i>Sets the indicated property to the given float if the property has not yet been set. </i><br />
 EAPI int <code>ecore_config_argb_default</code> (const char *key, int a, int r, int g, int b)<br />
 <i>Sets the indicated property to a color value if the property has not yet been set. </i><br />
 EAPI int <code>ecore_config_argbint_default</code> (const char *key, long argb)<br />
 <i>Sets the indicated property to a color value if the property has not yet been set. </i><br />
 EAPI int <code>ecore_config_argbstr_default</code> (const char *key, const char *val)<br />
 <i>Sets the indicated property to a color value if the property has not yet been set. </i><br />
 EAPI int <code>ecore_config_theme_default</code> (const char *key, const char *val)<br />
 <i>Sets the indicated property to a theme name if the property has not yet been set. </i></p>
<h2>Detailed Description</h2>
<p>Functions that are used to set the default values of properties.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_config_argb_default (const char * key, int a, int r, int g, int b)</h3>
<p>Sets the indicated property to a color value if the property has not yet been set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>a</i> integer 0..255<br />
 <i>r</i> integer 0..255<br />
 <i>g</i> integer 0..255<br />
 <i>b</i> integer 0..255</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if there are no problems.</dl>
<p> References ECORE_CONFIG_RGB.</p>
<h3>EAPI int ecore_config_argbint_default (const char * key, long argb)</h3>
<p>Sets the indicated property to a color value if the property has not yet been set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>argb</i> ARGB data as long</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if there are no problems.</dl>
<p> References ECORE_CONFIG_RGB.</p>
<h3>EAPI int ecore_config_argbstr_default (const char * key, const char * val)</h3>
<p>Sets the indicated property to a color value if the property has not yet been set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> Color value in ARGB format.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if there are no problems.</dl>
<p> References ECORE_CONFIG_RGB.</p>
<h3>EAPI int ecore_config_boolean_default (const char * key, int val)</h3>
<p>Sets the indicated property to the given boolean if the property has not yet been set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> Boolean Integer to set the value to.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if there are no problems.</dl>
<p> References ECORE_CONFIG_BLN.</p>
<h3>EAPI int ecore_config_default (const char * key, const char * val, float lo, float hi, float step)</h3>
<p>Sets the indicated property if it has not already been set or loaded. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> Default value of the key.<br />
 <i>lo</i> Lowest valid value for the key.<br />
 <i>hi</i> Highest valid value for the key.<br />
 <i>step</i> Used by integer and float values.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if there are no errors.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The lo, hi and step parameters are only used when storing integer and float properties.</dl>
<p> References ECORE_CONFIG_FLT, ecore_config_get(), and ECORE_CONFIG_INT.</p>
<h3>EAPI int ecore_config_float_default (const char * key, float val)</h3>
<p>Sets the indicated property to the given float if the property has not yet been set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> Float to set the property to.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if there were no problems.</dl>
<p> References ECORE_CONFIG_FLT.</p>
<h3>EAPI int ecore_config_float_default_bound (const char * key, float val, float low, float high, float step)</h3>
<p>Sets the indicated property to the given float if the property has not yet been set. </p>
<p> The bounds and step values are set regardless. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> Float to set the property to.<br />
 <i>low</i> Lowest valid integer value for the property.<br />
 <i>high</i> Highest valid float value for the property.<br />
 <i>step</i> Increment value for the property.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if there were no problems.</dl>
<p> References ECORE_CONFIG_FLT, and ecore_config_get().</p>
<h3>EAPI int ecore_config_int_default (const char * key, int val)</h3>
<p>Sets the indicated property to the given integer if the property has not yet been set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> Integer to set the value to.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if there are no problems.</dl>
<p> References ECORE_CONFIG_INT.</p>
<h3>EAPI int ecore_config_int_default_bound (const char * key, int val, int low, int high, int step)</h3>
<p>Sets the indicated property to the given integer if the property has not yet been set. </p>
<p> The bounds and step values are set regardless. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> Integer to set the property to.<br />
 <i>low</i> Lowest valid integer value for the property.<br />
 <i>high</i> Highest valid integer value for the property.<br />
 <i>step</i> Increment value for the property.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if there were no problems.</dl>
<p> References ecore_config_get(), and ECORE_CONFIG_INT.</p>
<h3>EAPI int ecore_config_string_default (const char * key, const char * val)</h3>
<p>Sets the indicated property to the given string if the property has not yet been set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> String to set the property to.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if there were no problems.</dl>
<p> References ECORE_CONFIG_STR. </p>
<p> Referenced by ecore_config_init(), and ecore_config_theme_search_path_get().</p>
<h3>EAPI int ecore_config_theme_default (const char * key, const char * val)</h3>
<p>Sets the indicated property to a theme name if the property has not yet been set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> String giving the name of the theme.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if the property is set successfully.</dl>
<p> References ECORE_CONFIG_THM.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
