---
title: "ecore_config(3)"
name: "ecore_config"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_config/"
description: "Ecore_Config.h – Provides the Enlightened Property Library."
---

<p>Ecore_Config.h &#8211; Provides the Enlightened Property Library. </p>
<h2>Synopsis</h2>
<h3>Data Structures</h3>
<p>struct <code>Ecore_Config_Prop</code><br />
 <i>The actual property for storing a key-value pair. </i></p>
<h3>Typedefs</h3>
<p>typedef int(* <code>Ecore_Config_Listener</code> )(const char *key, const <code>Ecore_Config_Type</code> type, const int tag, void *data)<br />
 <i>Property change callback function prototype. </i></p>
<h3>Enumerations</h3>
<p>enum <code>Ecore_Config_Type</code> { <code>ECORE_CONFIG_NIL</code> = 0, <code>ECORE_CONFIG_INT</code> = 1, <code>ECORE_CONFIG_FLT</code> = 2, <code>ECORE_CONFIG_STR</code> = 3, <code>ECORE_CONFIG_RGB</code> = 4, <code>ECORE_CONFIG_THM</code> = 5, <code>ECORE_CONFIG_BLN</code> = 6, <code>ECORE_CONFIG_SCT</code> = 7 }<br />
 <i>Valid configuration property types. </i></p>
<h3>Functions</h3>
<p>EAPI <code>Ecore_Config_Prop</code> * <code>ecore_config_get</code> (const char *key)<br />
 <i>Returns the property with the given key. </i><br />
 EAPI const char * <code>ecore_config_type_get</code> (const <code>Ecore_Config_Prop</code> *e)<br />
 <i>Returns the type of the property. </i><br />
 EAPI int <code>ecore_config_boolean_get</code> (const char *key)<br />
 <i>Returns the specified property as an integer. </i><br />
 EAPI char * <code>ecore_config_string_get</code> (const char *key)<br />
 <i>Returns the specified property as a string. </i><br />
 EAPI long <code>ecore_config_int_get</code> (const char *key)<br />
 <i>Returns the specified property as a long integer. </i><br />
 EAPI int <code>ecore_config_argb_get</code> (const char *key, int *a, int *r, int *g, int *b)<br />
 <i>Finds the alpha, red, green and blue values of a color property. </i><br />
 EAPI long <code>ecore_config_argbint_get</code> (const char *key)<br />
 <i>Returns a color property as a long. </i><br />
 EAPI char * <code>ecore_config_argbstr_get</code> (const char *key)<br />
 <i>Returns a color property as a string of hexadecimal characters. </i><br />
 EAPI float <code>ecore_config_float_get</code> (const char *key)<br />
 <i>Returns the specified property as a float. </i><br />
 EAPI char * <code>ecore_config_theme_get</code> (const char *key)<br />
 <i>Returns a theme property. </i><br />
 EAPI char * <code>ecore_config_as_string_get</code> (const char *key)<br />
 <i>Retrieves the key as a string. </i><br />
 EAPI int <code>ecore_config_describe</code> (const char *key, const char *desc)<br />
 <i>Sets the description field of the indicated property. </i><br />
 EAPI int <code>ecore_config_short_opt_set</code> (const char *key, char short_opt)<br />
 <i>Set the short option character of a property. </i><br />
 EAPI int <code>ecore_config_long_opt_set</code> (const char *key, const char *long_opt)<br />
 <i>Set the long option string of the property. </i><br />
 EAPI int <code>ecore_config_set</code> (const char *key, const char *val)<br />
 <i>Sets the indicated property to the value indicated by val</i>.<br />
 EAPI int <code>ecore_config_typed_set</code> (const char *key, const void *val, int type)<br />
 <i>Sets the indicated property to the given value and type. </i><br />
 EAPI int <code>ecore_config_boolean_set</code> (const char *key, int val)<br />
 <i>Sets the indicated property to the given boolean. </i><br />
 EAPI int <code>ecore_config_string_set</code> (const char *key, const char *val)<br />
 <i>Sets the indicated property to the given string. </i><br />
 EAPI int <code>ecore_config_int_set</code> (const char *key, int val)<br />
 <i>Sets the indicated property to the given integer. </i><br />
 EAPI int <code>ecore_config_argb_set</code> (const char *key, int a, int r, int g, int b)<br />
 <i>Sets the indicated property to a color value. </i><br />
 EAPI int <code>ecore_config_argbint_set</code> (const char *key, long argb)<br />
 <i>Sets the indicated property to a color value. </i><br />
 EAPI int <code>ecore_config_argbstr_set</code> (const char *key, const char *val)<br />
 <i>Sets the indicated property to a color value. </i><br />
 EAPI int <code>ecore_config_float_set</code> (const char *key, float val)<br />
 <i>Sets the indicated property to the given float value. </i><br />
 EAPI int <code>ecore_config_theme_set</code> (const char *key, const char *val)<br />
 <i>Sets the indicated property to a theme name. </i><br />
 EAPI int <code>ecore_config_theme_preview_group_set</code> (const char *key, const char *group)<br />
 <i>Sets the theme preview group of an indicated property. </i><br />
 EAPI int <code>ecore_config_as_string_set</code> (const char *key, const char *val)<br />
 <i>Sets the indicated property to the value given in the string. </i><br />
 EAPI int <code>ecore_config_default</code> (const char *key, const char *val, float lo, float hi, float step)<br />
 <i>Sets the indicated property if it has not already been set or loaded. </i><br />
 EAPI int <code>ecore_config_boolean_default</code> (const char *key, int val)<br />
 <i>Sets the indicated property to the given boolean if the property has not yet been set. </i><br />
 EAPI int <code>ecore_config_int_default</code> (const char *key, int val)<br />
 <i>Sets the indicated property to the given integer if the property has not yet been set. </i><br />
 EAPI int <code>ecore_config_int_default_bound</code> (const char *key, int val, int lo, int hi, int step)<br />
 <i>Sets the indicated property to the given integer if the property has not yet been set. </i><br />
 EAPI int <code>ecore_config_string_default</code> (const char *key, const char *val)<br />
 <i>Sets the indicated property to the given string if the property has not yet been set. </i><br />
 EAPI int <code>ecore_config_float_default</code> (const char *key, float val)<br />
 <i>Sets the indicated property to the given float if the property has not yet been set. </i><br />
 EAPI int <code>ecore_config_float_default_bound</code> (const char *key, float val, float lo, float hi, float step)<br />
 <i>Sets the indicated property to the given float if the property has not yet been set. </i><br />
 EAPI int <code>ecore_config_argb_default</code> (const char *key, int a, int r, int g, int b)<br />
 <i>Sets the indicated property to a color value if the property has not yet been set. </i><br />
 EAPI int <code>ecore_config_argbint_default</code> (const char *key, long argb)<br />
 <i>Sets the indicated property to a color value if the property has not yet been set. </i><br />
 EAPI int <code>ecore_config_argbstr_default</code> (const char *key, const char *val)<br />
 <i>Sets the indicated property to a color value if the property has not yet been set. </i><br />
 EAPI int <code>ecore_config_theme_default</code> (const char *key, const char *val)<br />
 <i>Sets the indicated property to a theme name if the property has not yet been set. </i><br />
 EAPI int <code>ecore_config_struct_int_add</code> (const char *key, const char *name, int val)<br />
 <i>Add an int property to the named structure. </i><br />
 EAPI int <code>ecore_config_struct_float_add</code> (const char *key, const char *name, float val)<br />
 <i>Add a float property to the named structure. </i><br />
 EAPI int <code>ecore_config_struct_create</code> (const char *key)<br />
 <i>Sets the indicated property to a structure if the property has not yet been set. </i><br />
 EAPI int <code>ecore_config_struct_string_add</code> (const char *key, const char *name, const char *val)<br />
 <i>Add a string property to the named structure. </i><br />
 EAPI int <code>ecore_config_struct_theme_add</code> (const char *key, const char *name, const char *val)<br />
 <i>Add a theme property to the named structure. </i><br />
 EAPI int <code>ecore_config_struct_argb_add</code> (const char *key, const char *name, int a, int r, int g, int b)<br />
 <i>Add an argb property to the named structure. </i><br />
 EAPI int <code>ecore_config_struct_boolean_add</code> (const char *key, const char *name, int val)<br />
 <i>Add a boolean property to the named structure. </i><br />
 EAPI int <code>ecore_config_struct_get</code> (const char *key, void *data)<br />
 <i>Get the contents of a defined structure property and load it into the passed C struct. </i><br />
 EAPI int <code>ecore_config_listen</code> (const char *name, const char *key, <code>Ecore_Config_Listener</code> listener, int tag, void *data)<br />
 <i>Adds a callback function to the list of functions called when a property changes. </i><br />
 EAPI int <code>ecore_config_deaf</code> (const char *name, const char *key, <code>Ecore_Config_Listener</code> listener)<br />
 <i>Removes a listener callback. </i><br />
 EAPI <code>Ecore_Config_Prop</code> * <code>ecore_config_dst</code> (<code>Ecore_Config_Prop</code> *e)<br />
 <i>Removes the given property from the local configuration and destroys it. </i><br />
 EAPI int <code>ecore_config_type_guess</code> (const char *key, const char *val)<br />
 <i>Tries to guess the type of a property. </i><br />
 EAPI Ecore_Config_Bundle * <code>ecore_config_bundle_new</code> (Ecore_Config_Server *srv, const char *id)<br />
 <i>Creates a new Ecore_Config_Bundle. </i><br />
 EAPI Ecore_Config_Bundle * <code>ecore_config_bundle_1st_get</code> (Ecore_Config_Server *srv)<br />
 <i>Locates the first configuration bundle on the given server. </i><br />
 EAPI Ecore_Config_Bundle * <code>ecore_config_bundle_next_get</code> (Ecore_Config_Bundle *ns)<br />
 <i>Locates the configuration bundle after the given one. </i><br />
 EAPI Ecore_Config_Bundle * <code>ecore_config_bundle_by_serial_get</code> (Ecore_Config_Server *srv, long serial)<br />
 <i>Locates a configuration bundle on a configuration server based on its serial number. </i><br />
 EAPI Ecore_Config_Bundle * <code>ecore_config_bundle_by_label_get</code> (Ecore_Config_Server *srv, const char *label)<br />
 <i>Gets the Ecore_Config_Bundle with the given identifier from the given server. </i><br />
 EAPI long <code>ecore_config_bundle_serial_get</code> (Ecore_Config_Bundle *ns)<br />
 <i>Retrieves the bundle&#8217;s serial number. </i><br />
 EAPI char * <code>ecore_config_bundle_label_get</code> (Ecore_Config_Bundle *ns)<br />
 <i>Retrieves the bundle&#8217;s identifier. </i><br />
 EAPI int <code>ecore_config_init</code> (const char *name)<br />
 <i>Initializes the Enlightened Property Library. </i><br />
 EAPI int <code>ecore_config_shutdown</code> (void)<br />
 <i>Frees memory and shuts down the library for an application. </i><br />
 EAPI int <code>ecore_config_system_init</code> (void)<br />
 <i>Initializes the Enlightened Property Library. </i><br />
 EAPI int <code>ecore_config_system_shutdown</code> (void)<br />
 <i>Frees memory and shuts down the library for other programming libraries. </i><br />
 EAPI int <code>ecore_config_load</code> (void)<br />
 <i>Loads the default configuration. </i><br />
 EAPI int <code>ecore_config_file_load</code> (const char *file)<br />
 <i>Load the given configuration file to the local configuration. </i><br />
 EAPI int <code>ecore_config_save</code> (void)<br />
 <i>Saves the current configuration to the default file. </i><br />
 EAPI int <code>ecore_config_file_save</code> (const char *file)<br />
 <i>Saves the local configuration to the given file. </i><br />
 EAPI int <code>ecore_config_evas_font_path_apply</code> (Evas *evas)<br />
 <i>Calls evas_font_path_append on </i>evas for each of the font names stored in the property &#8216;/e/font/path&#8217;.<br />
 EAPI char * <code>ecore_config_theme_search_path_get</code> (void)<br />
 <i>Retrieves the search path used to find themes. </i><br />
 EAPI int <code>ecore_config_theme_search_path_append</code> (const char *append)<br />
 <i>Adds the given path to the search path used to find themes. </i><br />
 EAPI char * <code>ecore_config_theme_default_path_get</code> (void)<br />
 <i>Retrieves the default theme search path. </i><br />
 EAPI char * <code>ecore_config_theme_with_path_from_name_get</code> (char *name)<br />
 <i>Retrieve a theme file&#8217;s full path. </i><br />
 EAPI char * <code>ecore_config_theme_with_path_get</code> (const char *key)<br />
 <i>Retrieves the full path to the theme file of the theme stored in the given property. </i><br />
 EAPI void <code>ecore_config_args_display</code> (void)<br />
 <i>Prints the property list of the local configuration bundle to output. </i><br />
 EAPI int <code>ecore_config_args_parse</code> (void)<br />
 <i>Parse the arguments set by </i><code>ecore_app_args_set</code> and set properties accordingly.<br />
 EAPI void <code>ecore_config_app_describe</code> (char *description)<br />
 <i>Sets the description string used by </i><code>ecore_config_args_display</code> .<br />
 EAPI int <code>ecore_config_create</code> (const char *key, void *val, char short_opt, char *long_opt, char *desc)<br />
 <i>Creates a new property, if it does not already exist, and sets its attributes to those given. </i><br />
 EAPI int <code>ecore_config_typed_create</code> (const char *key, void *val, int type, char short_opt, char *long_opt, char *desc)<br />
 <i>Creates a new property, if it does not already exist, and sets its attributes to those given. </i><br />
 EAPI int <code>ecore_config_boolean_create</code> (const char *key, int val, char short_opt, char *long_opt, char *desc)<br />
 <i>Creates a new boolean property, if it does not already exist, and sets its attributes to those given. </i><br />
 EAPI int <code>ecore_config_int_create</code> (const char *key, int val, char short_opt, char *long_opt, char *desc)<br />
 <i>Creates a new integer property, if it does not already exist, and sets its attributes to those given. </i><br />
 EAPI int <code>ecore_config_int_create_bound</code> (const char *key, int val, int low, int high, int step, char short_opt, char *long_opt, char *desc)<br />
 <i>Creates a new integer property, if it does not already exist, and sets its attributes to those given. </i><br />
 EAPI int <code>ecore_config_string_create</code> (const char *key, char *val, char short_opt, char *long_opt, char *desc)<br />
 <i>Creates a new string property, if it does not already exist, and sets its attributes to those given. </i><br />
 EAPI int <code>ecore_config_float_create</code> (const char *key, float val, char short_opt, char *long_opt, char *desc)<br />
 <i>Creates a new float property, if it does not already exist, and sets its attributes to those given. </i><br />
 EAPI int <code>ecore_config_float_create_bound</code> (const char *key, float val, float low, float high, float step, char short_opt, char *long_opt, char *desc)<br />
 <i>Creates a new float property, if it does not already exist, and sets its attributes to those given. </i><br />
 EAPI int <code>ecore_config_argb_create</code> (const char *key, char *val, char short_opt, char *long_opt, char *desc)<br />
 <i>Creates a new color property, if it does not already exist, and sets its attributes to those given. </i><br />
 EAPI int <code>ecore_config_theme_create</code> (const char *key, char *val, char short_opt, char *long_opt, char *desc)<br />
 <i>Creates a new theme property, if it does not already exist, and sets its attributes to those given. </i></p>
<h2>Detailed Description</h2>
<p>Provides the Enlightened Property Library. </p>
<p> This file provies all headers and structs for use with Ecore_Config. Using individual header files should not be necessary.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>Ecore_Config_Type</code></h3>
<p>Valid configuration property types. </p>
<p> <code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>ECORE_CONFIG_NIL </i></p>
<dd>Property with no value.</dl>
<dl COMPACT>
<dt><i>ECORE_CONFIG_INT </i></p>
<dd>Integer property type.</dl>
<dl COMPACT>
<dt><i>ECORE_CONFIG_FLT </i></p>
<dd>Float property type.</dl>
<dl COMPACT>
<dt><i>ECORE_CONFIG_STR </i></p>
<dd>String property type.</dl>
<dl COMPACT>
<dt><i>ECORE_CONFIG_RGB </i></p>
<dd>Colour property type.</dl>
<dl COMPACT>
<dt><i>ECORE_CONFIG_THM </i></p>
<dd>Theme property type.</dl>
<dl COMPACT>
<dt><i>ECORE_CONFIG_BLN </i></p>
<dd>Boolean property type.</dl>
<dl COMPACT>
<dt><i>ECORE_CONFIG_SCT </i></p>
<dd>Structure property type.</dl>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_config_app_describe (char * description)</h3>
<p>Sets the description string used by <code>ecore_config_args_display</code> . </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>description</i> Description of application.</dl>
<p> References ecore_config_app_describe(). </p>
<p> Referenced by ecore_config_app_describe().</p>
<h3>EAPI int ecore_config_args_parse (void)</h3>
<p>Parse the arguments set by <code>ecore_app_args_set</code> and set properties accordingly. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_PARSE_CONTINUE if successful. ECORE_CONFIG_PARSE_EXIT is returned if an unrecognised option is found. ECORE_CONFIG_PARSE_HELP is returned if help was displayed.</dl>
<p> References ecore_app_args_get(), ecore_config_args_display(), ecore_config_args_parse(), and ECORE_CONFIG_NIL. </p>
<p> Referenced by ecore_config_args_parse().</p>
<h3>EAPI Ecore_Config_Bundle* ecore_config_bundle_1st_get (Ecore_Config_Server * srv)</h3>
<p>Locates the first configuration bundle on the given server. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>srv</i> The configuration server.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Pointer to the first configuration bundle.</dl>
<h3>EAPI Ecore_Config_Bundle* ecore_config_bundle_by_label_get (Ecore_Config_Server * srv, const char * label)</h3>
<p>Gets the Ecore_Config_Bundle with the given identifier from the given server. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>srv</i> The configuration server.<br />
 <i>label</i> The bundle&#8217;s identifier string.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The bundle with the given identifier string, or NULL if it could not be found.</dl>
<h3>EAPI Ecore_Config_Bundle* ecore_config_bundle_by_serial_get (Ecore_Config_Server * srv, long serial)</h3>
<p>Locates a configuration bundle on a configuration server based on its serial number. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>srv</i> The configuration server.<br />
 <i>serial</i> Serial number.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The configuration bundle with the given serial number.</dl>
<h3>EAPI char* ecore_config_bundle_label_get (Ecore_Config_Bundle * ns)</h3>
<p>Retrieves the bundle&#8217;s identifier. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ns</i> The configuration bundle.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The bundle&#8217;s identifer string.</dl>
<h3>EAPI Ecore_Config_Bundle* ecore_config_bundle_new (Ecore_Config_Server * srv, const char * identifier)</h3>
<p>Creates a new Ecore_Config_Bundle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>srv</i> Config server.<br />
 <i>identifier</i> Identifier string for the new bundle.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to a new Ecore_Config_Bundle. NULL is returned if the structure couldn&#8217;t be allocated.</dl>
<h3>EAPI Ecore_Config_Bundle* ecore_config_bundle_next_get (Ecore_Config_Bundle * ns)</h3>
<p>Locates the configuration bundle after the given one. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ns</i> The configuration bundle.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The next configuration bundle.</dl>
<h3>EAPI long ecore_config_bundle_serial_get (Ecore_Config_Bundle * ns)</h3>
<p>Retrieves the bundle&#8217;s serial number. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ns</i> The configuration bundle.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The bundle&#8217;s identifier string, or -1 if ns is NULL.</dl>
<h3>EAPI int ecore_config_evas_font_path_apply (Evas * evas)</h3>
<p>Calls evas_font_path_append on evas for each of the font names stored in the property &#8216;/e/font/path&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>evas</i> Evas object to append the font names to.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC on success. ECORE_CONFIG_ERR_NODATA is returned if the property has not been set.</dl>
<p> References ecore_config_evas_font_path_apply(), and ecore_config_string_get(). </p>
<p> Referenced by ecore_config_evas_font_path_apply().</p>
<h3>EAPI char* ecore_config_theme_default_path_get (void)</h3>
<p>Retrieves the default theme search path. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The default theme search path.</dl>
<p> References ecore_config_theme_default_path_get(). </p>
<p> Referenced by ecore_config_init(), ecore_config_theme_default_path_get(), and ecore_config_theme_search_path_get().</p>
<h3>EAPI int ecore_config_theme_search_path_append (const char * path)</h3>
<p>Adds the given path to the search path used to find themes. </p>
<p> If the search path is successfully, the new search path will be saved into the property &#8216;/e/themes/search_path&#8217;. Therefore, this function should be called <code>after</code> <code>ecore_config_load</code> to allow a user to override the default search path. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>path</i> The given</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC on success. ECORE_CONFIG_ERR_FAIL will be returned if path already exists in the search path. ECORE_CONFIG_ERR_FAIL is returned if path is NULL.</dl>
<p> References ecore_config_get(), ecore_config_string_set(), ecore_config_theme_search_path_append(), and ecore_config_theme_search_path_get(). </p>
<p> Referenced by ecore_config_theme_search_path_append().</p>
<h3>EAPI char* ecore_config_theme_search_path_get (void)</h3>
<p>Retrieves the search path used to find themes. </p>
<p> The search path is stored in the property &#8216;/e/themes/search_path&#8217;. If the property has not been set, the default path used is &#8216;/usr/local/share/&lt;app_name&gt;/themes|~/.e/apps/&lt;app_name&gt;/themes&#8217;. See <code>ecore_config_theme_default_path_get</code> for more information about the default path. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The search path. NULL is returned if there is no memory left.</dl>
<p> References ecore_config_string_default(), ecore_config_string_get(), ecore_config_theme_default_path_get(), and ecore_config_theme_search_path_get(). </p>
<p> Referenced by ecore_config_theme_search_path_append(), ecore_config_theme_search_path_get(), and ecore_config_theme_with_path_from_name_get().</p>
<h3>EAPI char* ecore_config_theme_with_path_from_name_get (char * name)</h3>
<p>Retrieve a theme file&#8217;s full path. </p>
<p> The search path for theme files is given by <code>ecore_config_theme_search_path_get</code> . </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> The name of the theme.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A full path to the theme on success. NULL will be returned if name is NULL or no theme matching the given name could be found.</dl>
<p> References ecore_config_theme_search_path_get(), and ecore_config_theme_with_path_from_name_get(). </p>
<p> Referenced by ecore_config_theme_with_path_from_name_get(), and ecore_config_theme_with_path_get().</p>
<h3>EAPI char* ecore_config_theme_with_path_get (const char * key)</h3>
<p>Retrieves the full path to the theme file of the theme stored in the given property. </p>
<p> The search path for themes is given by <code>ecore_config_theme_search_path_get</code> . </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The given property.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A full path to the theme on success, or NULL on failure. This function will fail if no key is specified or not theme matching that given by the property key could be found.</dl>
<p> References ecore_config_theme_get(), ecore_config_theme_with_path_from_name_get(), and ecore_config_theme_with_path_get(). </p>
<p> Referenced by ecore_config_theme_with_path_get().</p>
<h3>EAPI int ecore_config_type_guess (const char * key, const char * val)</h3>
<p>Tries to guess the type of a property. </p>
<p> This function first checks to see if the property exists. If it does, then the type of the stored property is returned. Otherwise, the function tries to guess the type of the property based on val. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> The property key.<br />
 <i>val</i> The value in string form.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The type of the property determined by the function. Note that if val is NULL, ECORE_CONFIG_NIL will be returned.</dl>
<p> References ECORE_CONFIG_FLT, ecore_config_get(), ECORE_CONFIG_INT, ECORE_CONFIG_NIL, ECORE_CONFIG_RGB, and ECORE_CONFIG_STR.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
