---
title: "ecore_config_get_group(3)"
name: "ecore_config_get_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_config_get_group/"
description: "Configuration Retrieve Functions – Functions that retrieve configuration values, based on type."
---

<p>Configuration Retrieve Functions &#8211; Functions that retrieve configuration values, based on type. </p>
<h3>Functions</h3>
<p>EAPI <code>Ecore_Config_Prop</code> * <code>ecore_config_get</code> (const char *key)<br />
 <i>Returns the property with the given key. </i><br />
 EAPI char * <code>ecore_config_string_get</code> (const char *key)<br />
 <i>Returns the specified property as a string. </i><br />
 EAPI int <code>ecore_config_boolean_get</code> (const char *key)<br />
 <i>Returns the specified property as an integer. </i><br />
 EAPI long <code>ecore_config_int_get</code> (const char *key)<br />
 <i>Returns the specified property as a long integer. </i><br />
 EAPI float <code>ecore_config_float_get</code> (const char *key)<br />
 <i>Returns the specified property as a float. </i><br />
 EAPI int <code>ecore_config_argb_get</code> (const char *key, int *a, int *r, int *g, int *b)<br />
 <i>Finds the alpha, red, green and blue values of a color property. </i><br />
 EAPI long <code>ecore_config_argbint_get</code> (const char *key)<br />
 <i>Returns a color property as a long. </i><br />
 EAPI char * <code>ecore_config_argbstr_get</code> (const char *key)<br />
 <i>Returns a color property as a string of hexadecimal characters. </i><br />
 EAPI char * <code>ecore_config_theme_get</code> (const char *key)<br />
 <i>Returns a theme property. </i><br />
 EAPI char * <code>ecore_config_as_string_get</code> (const char *key)<br />
 <i>Retrieves the key as a string. </i></p>
<h2>Detailed Description</h2>
<p>Functions that retrieve configuration values, based on type.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_config_argb_get (const char * key, int * a, int * r, int * g, int * b)</h3>
<p>Finds the alpha, red, green and blue values of a color property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>a</i> A pointer to an integer to store the alpha value into.<br />
 <i>r</i> A pointer to an integer to store the red value into.<br />
 <i>g</i> A pointer to an integer to store the green value into.<br />
 <i>b</i> A pointer to an integer to store the blue value into.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC on success. ECORE_CONFIG_ERR_FAIL otherwise.</dl>
<p> References ecore_config_get().</p>
<h3>EAPI long ecore_config_argbint_get (const char * key)</h3>
<p>Returns a color property as a long. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ARGB data as long</dl>
<p> References ecore_config_get().</p>
<h3>EAPI char* ecore_config_argbstr_get (const char * key)</h3>
<p>Returns a color property as a string of hexadecimal characters. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A string of hexadecimal characters in the format aarrggbb.</dl>
<p> References ecore_config_get().</p>
<h3>EAPI char* ecore_config_as_string_get (const char * key)</h3>
<p>Retrieves the key as a string. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns a character array in the form of &#8216;key:type=value&#8217;. NULL is returned if the property does not exist.</dl>
<p> References ECORE_CONFIG_BLN, ECORE_CONFIG_FLT, ecore_config_get(), ECORE_CONFIG_INT, ECORE_CONFIG_NIL, ECORE_CONFIG_RGB, ECORE_CONFIG_SCT, ECORE_CONFIG_STR, and ECORE_CONFIG_THM.</p>
<h3>EAPI int ecore_config_boolean_get (const char * key)</h3>
<p>Returns the specified property as an integer. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The value of the property. The function returns -1 if the property is not an integer or is not set.</dl>
<p> References ecore_config_get().</p>
<h3>EAPI float ecore_config_float_get (const char * key)</h3>
<p>Returns the specified property as a float. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The float value of the property. The function returns 0.0 if the property is not a float or is not set.</dl>
<p> References ecore_config_get().</p>
<h3>EAPI <code>Ecore_Config_Prop</code>* ecore_config_get (const char * key)</h3>
<p>Returns the property with the given key. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The unique name of the wanted property.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The property that corresponds to the given key. NULL if the key could not be found.</dl>
<p> Referenced by ecore_config_argb_get(), ecore_config_argbint_get(), ecore_config_argbstr_get(), ecore_config_as_string_get(), ecore_config_boolean_get(), ecore_config_deaf(), ecore_config_default(), ecore_config_describe(), ecore_config_float_create_bound(), ecore_config_float_default_bound(), ecore_config_float_get(), ecore_config_init(), ecore_config_int_create_bound(), ecore_config_int_default_bound(), ecore_config_int_get(), ecore_config_listen(), ecore_config_long_opt_set(), ecore_config_short_opt_set(), ecore_config_string_get(), ecore_config_struct_get(), ecore_config_theme_get(), ecore_config_theme_preview_group_set(), ecore_config_theme_search_path_append(), ecore_config_type_guess(), and ecore_config_typed_set().</p>
<h3>EAPI long ecore_config_int_get (const char * key)</h3>
<p>Returns the specified property as a long integer. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The integer value of the property. The function returns 0 if the property is not an integer or is not set.</dl>
<p> References ecore_config_get().</p>
<h3>EAPI char* ecore_config_string_get (const char * key)</h3>
<p>Returns the specified property as a string. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The string value of the property. The function returns NULL if the property is not a string or is not set.</dl>
<p> References ecore_config_get(). </p>
<p> Referenced by ecore_config_evas_font_path_apply(), and ecore_config_theme_search_path_get().</p>
<h3>EAPI char* ecore_config_theme_get (const char * key)</h3>
<p>Returns a theme property. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The name of the theme the property refers to. The function returns NULL if the property is not a theme or is not set.</dl>
<p> References ecore_config_get(). </p>
<p> Referenced by ecore_config_theme_with_path_get().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
