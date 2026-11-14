---
title: "slv2_data(3)"
name: "slv2_data"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slv2_data/"
description: "Plugin data access –"
---

<p>Plugin data access &#8211;</p>
<h3>Functions</h3>
<p>bool <code>slv2_plugin_verify</code> (SLV2Plugin plugin) </p>
<p> SLV2Value <code>slv2_plugin_get_uri</code> (SLV2Plugin plugin) </p>
<p> SLV2Value <code>slv2_plugin_get_bundle_uri</code> (SLV2Plugin plugin) </p>
<p> SLV2Values <code>slv2_plugin_get_data_uris</code> (SLV2Plugin plugin) </p>
<p> SLV2Value <code>slv2_plugin_get_library_uri</code> (SLV2Plugin plugin) </p>
<p> SLV2Value <code>slv2_plugin_get_name</code> (SLV2Plugin plugin) </p>
<p> SLV2Values <code>slv2_plugin_get_value</code> (SLV2Plugin p, SLV2Value predicate) </p>
<p> SLV2Values <code>slv2_plugin_get_value_by_qname</code> (SLV2Plugin p, const char *predicate) </p>
<p> SLV2Values <code>slv2_plugin_get_value_by_qname_i18n</code> (SLV2Plugin p, const char *predicate) </p>
<p> SLV2Values <code>slv2_plugin_get_value_for_subject</code> (SLV2Plugin p, SLV2Value subject_uri, SLV2Value predicate_uri) </p>
<p> bool <code>slv2_plugin_has_feature</code> (SLV2Plugin p, SLV2Value feature_uri) </p>
<p> SLV2Values <code>slv2_plugin_get_supported_features</code> (SLV2Plugin p) </p>
<p> SLV2Values <code>slv2_plugin_get_required_features</code> (SLV2Plugin p) </p>
<p> SLV2Values <code>slv2_plugin_get_optional_features</code> (SLV2Plugin p) </p>
<p> uint32_t <code>slv2_plugin_get_num_ports</code> (SLV2Plugin p) </p>
<p> void <code>slv2_plugin_get_port_ranges_float</code> (SLV2Plugin p, float *min_values, float *max_values, float *def_values) </p>
<p> uint32_t <code>slv2_plugin_get_num_ports_of_class</code> (SLV2Plugin p, SLV2Value class_1,&#8230;) </p>
<p> bool <code>slv2_plugin_has_latency</code> (SLV2Plugin p) </p>
<p> uint32_t <code>slv2_plugin_get_latency_port_index</code> (SLV2Plugin p) </p>
<p> SLV2Values <code>slv2_plugin_query_variable</code> (SLV2Plugin plugin, const char *sparql_str, unsigned variable) </p>
<p> unsigned <code>slv2_plugin_query_count</code> (SLV2Plugin plugin, const char *sparql_str) </p>
<p> SLV2Port <code>slv2_plugin_get_port_by_index</code> (SLV2Plugin plugin, uint32_t index) </p>
<p> SLV2Port <code>slv2_plugin_get_port_by_symbol</code> (SLV2Plugin plugin, SLV2Value symbol) </p>
<p> SLV2UIs <code>slv2_plugin_get_uis</code> (SLV2Plugin plugin) </p>
<p> SLV2Value <code>slv2_plugin_get_author_name</code> (SLV2Plugin plugin) </p>
<p> SLV2Value <code>slv2_plugin_get_author_email</code> (SLV2Plugin plugin) </p>
<p> SLV2Value <code>slv2_plugin_get_author_homepage</code> (SLV2Plugin plugin) </p>
<p> SLV2Value <code>slv2_plugin_class_get_parent_uri</code> (SLV2PluginClass plugin_class) </p>
<p> SLV2Value <code>slv2_plugin_class_get_uri</code> (SLV2PluginClass plugin_class) </p>
<p> SLV2Value <code>slv2_plugin_class_get_label</code> (SLV2PluginClass plugin_class) </p>
<p> SLV2PluginClasses <code>slv2_plugin_class_get_children</code> (SLV2PluginClass plugin_class) </p>
<p> SLV2Value <code>slv2_ui_get_uri</code> (SLV2UI ui) </p>
<p> SLV2Values <code>slv2_ui_get_classes</code> (SLV2UI ui) </p>
<p> bool <code>slv2_ui_is_a</code> (SLV2UI ui, SLV2Value class_uri) </p>
<p> SLV2Value <code>slv2_ui_get_bundle_uri</code> (SLV2UI ui) </p>
<p> SLV2Value <code>slv2_ui_get_binary_uri</code> (SLV2UI ui) </p>
<p> SLV2Values <code>slv2_port_get_value</code> (SLV2Plugin plugin, SLV2Port port, SLV2Value predicate) </p>
<p> SLV2Values <code>slv2_port_get_value_by_qname</code> (SLV2Plugin plugin, SLV2Port port, const char *property_uri) </p>
<p> SLV2Values <code>slv2_port_get_value_by_qname_i18n</code> (SLV2Plugin plugin, SLV2Port port, const char *property_uri) </p>
<p> SLV2Values <code>slv2_port_get_properties</code> (SLV2Plugin plugin, SLV2Port port) </p>
<p> bool <code>slv2_port_has_property</code> (SLV2Plugin p, SLV2Port port, SLV2Value property_uri) </p>
<p> bool <code>slv2_port_supports_event</code> (SLV2Plugin p, SLV2Port port, SLV2Value event_uri) </p>
<p> SLV2Value <code>slv2_port_get_symbol</code> (SLV2Plugin plugin, SLV2Port port) </p>
<p> SLV2Value <code>slv2_port_get_name</code> (SLV2Plugin plugin, SLV2Port port) </p>
<p> SLV2Values <code>slv2_port_get_classes</code> (SLV2Plugin plugin, SLV2Port port) </p>
<p> bool <code>slv2_port_is_a</code> (SLV2Plugin plugin, SLV2Port port, SLV2Value port_class) </p>
<p> void <code>slv2_port_get_range</code> (SLV2Plugin plugin, SLV2Port port, SLV2Value *def, SLV2Value *min, SLV2Value *max) </p>
<p> SLV2ScalePoints <code>slv2_port_get_scale_points</code> (SLV2Plugin plugin, SLV2Port port) </p>
<p> unsigned <code>slv2_results_size</code> (SLV2Results results) </p>
<p> SLV2Value <code>slv2_results_get_binding_value</code> (SLV2Results results, unsigned index) </p>
<p> SLV2Value <code>slv2_results_get_binding_value_by_name</code> (SLV2Results results, const char *name) </p>
<p> const char * <code>slv2_results_get_binding_name</code> (SLV2Results results, unsigned index) </p>
<p> SLV2Value <code>slv2_scale_point_get_label</code> (SLV2ScalePoint point) </p>
<p> SLV2Value <code>slv2_scale_point_get_value</code> (SLV2ScalePoint point) </p>
<p> SLV2Value <code>slv2_value_new_uri</code> (SLV2World world, const char *uri) </p>
<p> SLV2Value <code>slv2_value_new_string</code> (SLV2World world, const char *str) </p>
<p> SLV2Value <code>slv2_value_new_int</code> (SLV2World world, int val) </p>
<p> SLV2Value <code>slv2_value_new_float</code> (SLV2World world, float val) </p>
<p> char * <code>slv2_value_get_turtle_token</code> (SLV2Value value) </p>
<p> bool <code>slv2_value_is_uri</code> (SLV2Value value) </p>
<p> const char * <code>slv2_value_as_uri</code> (SLV2Value value) </p>
<p> bool <code>slv2_value_is_literal</code> (SLV2Value value) </p>
<p> bool <code>slv2_value_is_string</code> (SLV2Value value) </p>
<p> const char * <code>slv2_value_as_string</code> (SLV2Value value) </p>
<p> bool <code>slv2_value_is_float</code> (SLV2Value value) </p>
<p> float <code>slv2_value_as_float</code> (SLV2Value value) </p>
<p> bool <code>slv2_value_is_int</code> (SLV2Value value) </p>
<p> int <code>slv2_value_as_int</code> (SLV2Value value)</p>
<h2>Detailed Description</h2>
<p>An SLV2Plugin contains an in-memory cache of the plugin data, loaded on demand. Duplicating plugins should be avoided when possible for performance reasons.</p>
<h2>Function Documentation</h2>
<h3>bool slv2_plugin_verify (SLV2Pluginplugin)</h3>
<p>Check if this plugin is valid. This is used by plugin lists to avoid loading plugins that are not valid and will not work with libslv2 (eg plugins missing required fields, or having multiple values for mandatory single-valued fields, etc. </p>
<p> Note that normal hosts do NOT need to use this &#8211; slv2 does not load invalid plugins into plugin lists. This is included for plugin testing utilities, etc. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>true if <i>plugin</i> is valid.</dl>
<p> Time = Query</p>
<h3>SLV2Value slv2_plugin_get_uri (SLV2Pluginplugin)</h3>
<p>Get the URI of <i>plugin</i>. Any serialization that refers to plugins should refer to them by this. Hosts SHOULD NOT save any filesystem paths, plugin indexes, etc. in saved files; save only the URI. </p>
<p> The URI is a globally unique identifier for one specific plugin. Two plugins with the same URI are compatible in port signature, and should be guaranteed to work in a compatible and consistent way. If a plugin is upgraded in an incompatible way (eg if it has different ports), it MUST have a different URI than it&#8217;s predecessor. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>a shared string which must not be modified or free()&#8217;d.</dl>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>SLV2Value slv2_plugin_get_bundle_uri (SLV2Pluginplugin)</h3>
<p>Get the (resolvable) URI of the plugins &#8216;main&#8217; bundle. This returns the URI of the bundle where the plugin itself was found. Note that the data for a plugin may be spread over many bundles, that is, slv2_plugin_get_data_uris may returns URIs which are not below this one. </p>
<p> Typical hosts should not need to use this function. </p>
<p> Note this always returns a fully qualified URI. If you want a local filesystem path, use slv2_uri_to_path. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>a shared string which must not be modified or freed.</dl>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>SLV2Values slv2_plugin_get_data_uris (SLV2Pluginplugin)</h3>
<p>Get the (resolvable) URIs of the RDF data files that define a plugin. Typical hosts should not need to use this function. </p>
<p> Note this always returns fully qualified URIs. If you want local filesystem paths, use slv2_uri_to_path. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>a list of complete URLs eg. &#8216;file:///foo/ABundle.lv2/aplug.ttl&#8217;, which is shared and must not be modified or freed.</dl>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>SLV2Value slv2_plugin_get_library_uri (SLV2Pluginplugin)</h3>
<p>Get the (resolvable) URI of the shared library for <i>plugin</i>. Note this always returns a fully qualified URI. If you want a local filesystem path, use slv2_uri_to_path. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>a shared string which must not be modified or freed.</dl>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>SLV2Value slv2_plugin_get_name (SLV2Pluginplugin)</h3>
<p>Get the name of <i>plugin</i>. This is guaranteed to return the untranslated name (the doap:name in the data file without a language tag). Returned value must be freed by the caller. </p>
<p> Time = Query</p>
<h3>SLV2Values slv2_plugin_get_value (SLV2Pluginp, SLV2Valuepredicate)</h3>
<p>Get a value associated with the plugin in a plugin&#8217;s data files. Returns the ?object of all triples found of the form: </p>
<p> &lt;plugin-uri&gt; predicate ?object </p>
<p> May return NULL if the property was not found, or if object(s) is not sensibly represented as an SLV2Values (e.g. blank nodes). </p>
<p> Return value must be freed by caller with slv2_values_free. </p>
<p> <i>predicate</i> must be either a URI or a QName. See SLV2URIType documentation for examples. </p>
<p> Time = Query</p>
<h3>SLV2Values slv2_plugin_get_value_by_qname (SLV2Pluginp, const char *predicate)</h3>
<p>Get a value associated with the plugin in a plugin&#8217;s data files. This function is identical to slv2_plugin_get_value, but takes a QName string parameter for a predicate instead of an SLV2Value, which may be more convenient.</p>
<h3>SLV2Values slv2_plugin_get_value_by_qname_i18n (SLV2Pluginp, const char *predicate)</h3>
<p>Get a translated value associated with the plugin in a plugin&#8217;s data files. This function is identical to slv2_plugin_get_value, but takes a QName string parameter for a predicate instead of an SLV2Value, which may be more convenient. It returns the value translated to the current language if possible.</p>
<h3>SLV2Values slv2_plugin_get_value_for_subject (SLV2Pluginp, SLV2Valuesubject_uri, SLV2Valuepredicate_uri)</h3>
<p>Get a value associated with some subject in a plugin&#8217;s data files. Returns the ?object of all triples found of the form: </p>
<p> subject predicate ?object </p>
<p> This can be used to investigate URIs returned by slv2_plugin_get_value (if information about it is contained in the plugin&#8217;s data files). </p>
<p> May return NULL if the property was not found, or if object is not sensibly represented as an SLV2Values (e.g. blank nodes). </p>
<p> <i>predicate</i> must be either a URI or a QName. See SLV2URIType documentation for examples. </p>
<p> Return value must be freed by caller with slv2_values_free. </p>
<p> Time = Query</p>
<h3>bool slv2_plugin_has_feature (SLV2Pluginp, SLV2Valuefeature_uri)</h3>
<p>Return whether a feature is supported by a plugin. This will return true if the feature is an optional or required feature of the plugin. </p>
<p> Time = Query</p>
<h3>SLV2Values slv2_plugin_get_supported_features (SLV2Pluginp)</h3>
<p>Get the LV2 Features supported (required or optionally) by a plugin. A feature is &#8216;supported&#8217; by a plugin if it is required OR optional. </p>
<p> Since required features have special rules the host must obey, this function probably shouldn&#8217;t be used by normal hosts. Using slv2_plugin_get_optional_features and slv2_plugin_get_required_features separately is best in most cases. </p>
<p> Returned value must be freed by caller with slv2_values_free. </p>
<p> Time = Query</p>
<h3>SLV2Values slv2_plugin_get_required_features (SLV2Pluginp)</h3>
<p>Get the LV2 Features required by a plugin. If a feature is required by a plugin, hosts MUST NOT use the plugin if they do not understand (or are unable to support) that feature. </p>
<p> All values returned here MUST be passed to the plugin&#8217;s instantiate method (along with data, if necessary, as defined by the feature specification) or plugin instantiation will fail. </p>
<p> Return value must be freed by caller with slv2_values_free. </p>
<p> Time = Query</p>
<h3>SLV2Values slv2_plugin_get_optional_features (SLV2Pluginp)</h3>
<p>Get the LV2 Features optionally supported by a plugin. Hosts MAY ignore optional plugin features for whatever reasons. Plugins MUST operate (at least somewhat) if they are instantiated without being passed optional features. </p>
<p> Return value must be freed by caller with slv2_values_free. </p>
<p> Time = Query</p>
<h3>uint32_t slv2_plugin_get_num_ports (SLV2Pluginp)</h3>
<p>Get the number of ports on this plugin. Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>void slv2_plugin_get_port_ranges_float (SLV2Pluginp, float *min_values, float *max_values, float *def_values)</h3>
<p>Get the port ranges (minimum, maximum and default values) for all ports. <i>min_values</i>, <i>max_values</i> and <i>def_values</i> must either point to an array of N floats, where N is the value returned by <code>slv2_plugin_get_num_ports()</code> for this plugin, or NULL. The elements of the array will be set to the the minimum, maximum and default values of the ports on this plugin, with array index corresponding to port index. If a port doesn&#8217;t have a minimum, maximum or default value, or the port&#8217;s type is not float, the corresponding array element will be set to NAN. </p>
<p> This is a convenience method for the common case of getting the range of all float ports on a plugin, and may be significantly faster than repeated calls to slv2_port_get_range.</p>
<h3>uint32_t slv2_plugin_get_num_ports_of_class (SLV2Pluginp, SLV2Valueclass_1, &#8230;)</h3>
<p>Get the number of ports on this plugin that are members of some class(es). Note that this is a varargs function so ports fitting any type &#8216;profile&#8217; desired can be found quickly. REMEMBER TO TERMINATE THE PARAMETER LIST OF THIS FUNCTION WITH NULL OR VERY NASTY THINGS WILL HAPPEN. </p>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>bool slv2_plugin_has_latency (SLV2Pluginp)</h3>
<p>Return whether or not the plugin introduces (and reports) latency. The index of the latency port can be found with slv2_plugin_get_latency_port ONLY if this function returns true. </p>
<p> Time = Query</p>
<h3>uint32_t slv2_plugin_get_latency_port_index (SLV2Pluginp)</h3>
<p>Return the index of the plugin&#8217;s latency port. It is a fatal error to call this on a plugin without checking if the port exists by first calling slv2_plugin_has_latency. </p>
<p> Any plugin that introduces unwanted latency that should be compensated for (by hosts with the ability/need) MUST provide this port, which is a control rate output port that reports the latency for each cycle in frames. </p>
<p> Time = Query</p>
<h3>SLV2Values slv2_plugin_query_variable (SLV2Pluginplugin, const char *sparql_str, unsignedvariable)</h3>
<p>Query a plugin for a single variable (i.e. SELECT a single ?value). </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>plugin</i> The plugin to query.<br />
 <i>sparql_str</i> A SPARQL SELECT query.<br />
 <i>variable</i> The index of the variable to return results for (e.g. with &#8216;&lt;code&gt;SELECT ?foo ?bar&lt;/code&gt;&#8217; foo=0, bar=1).</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>All matches for <i>variable</i>.</dl>
<p> Time = Query</p>
<h3>unsigned slv2_plugin_query_count (SLV2Pluginplugin, const char *sparql_str)</h3>
<p>Query a plugin and return the number of results found. Note that this function will work, but is mostly meaningless for queries that are not SELECT DISTINCT. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>plugin</i> The plugin to query.<br />
 <i>sparql_str</i> A SPARQL SELECT DISTINCT query.</dl>
<p> Time = Query</p>
<h3>SLV2Port slv2_plugin_get_port_by_index (SLV2Pluginplugin, uint32_tindex)</h3>
<p>Get a port on this plugin by <i>index</i>. To perform multiple calls on a port, the returned value should be cached and used repeatedly. </p>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>SLV2Port slv2_plugin_get_port_by_symbol (SLV2Pluginplugin, SLV2Valuesymbol)</h3>
<p>Get a port on this plugin by <i>symbol</i>. To perform multiple calls on a port, the returned value should be cached and used repeatedly. Note this function is slower than slv2_plugin_get_port_by_index, especially on plugins with a very large number of ports. </p>
<p> Time = <a href="/docs/linux/man/n-o/">O</a>(n)</p>
<h3>SLV2UIs slv2_plugin_get_uis (SLV2Pluginplugin)</h3>
<p>Get a list of all UIs available for this plugin. Note this returns the URI of the UI, and not the path/URI to its shared library, use slv2_ui_get_library_uri with the values returned here for that. </p>
<p> Returned value must be freed by caller using slv2_uis_free. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>plugin</i> The plugin to get the UIs for.</dl>
<p> Time = Query</p>
<h3>SLV2Value slv2_plugin_get_author_name (SLV2Pluginplugin)</h3>
<p>Get the full name of the plugin&#8217;s author. Returns NULL if author name is not present. Returned value must be freed by caller. </p>
<p> Time = Query</p>
<h3>SLV2Value slv2_plugin_get_author_email (SLV2Pluginplugin)</h3>
<p>Get the email address of the plugin&#8217;s author. Returns NULL if author email address is not present. Returned value must be freed by caller. </p>
<p> Time = Query</p>
<h3>SLV2Value slv2_plugin_get_author_homepage (SLV2Pluginplugin)</h3>
<p>Get the email address of the plugin&#8217;s author. Returns NULL if author homepage is not present. Returned value must be freed by caller. </p>
<p> Time = Query</p>
<h3>SLV2Value slv2_plugin_class_get_parent_uri (SLV2PluginClassplugin_class)</h3>
<p>Get the URI of this class&#8217; superclass. Returned value is owned by <i>plugin_class</i> and must not be freed by caller. Returned value may be NULL, if class has no parent. </p>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>SLV2Value slv2_plugin_class_get_uri (SLV2PluginClassplugin_class)</h3>
<p>Get the URI of this plugin class. Returned value is owned by <i>plugin_class</i> and must not be freed by caller. </p>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>SLV2Value slv2_plugin_class_get_label (SLV2PluginClassplugin_class)</h3>
<p>Get the label of this plugin class, ie &#8216;Oscillators&#8217;. Returned value is owned by <i>plugin_class</i> and must not be freed by caller. </p>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>SLV2PluginClasses slv2_plugin_class_get_children (SLV2PluginClassplugin_class)</h3>
<p>Get the subclasses of this plugin class. Returned value must be freed by caller with slv2_plugin_classes_free. </p>
<p> Time = O(nclasses)</p>
<h3>SLV2Value slv2_ui_get_uri (SLV2UIui)</h3>
<p>Get the URI of a Plugin UI. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ui</i> The Plugin UI</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>a shared value which must not be modified or freed.</dl>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>SLV2Values slv2_ui_get_classes (SLV2UIui)</h3>
<p>Get the types (URIs of RDF classes) of a Plugin UI. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ui</i> The Plugin UI</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>a shared value which must not be modified or freed.</dl>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>bool slv2_ui_is_a (SLV2UIui, SLV2Valueclass_uri)</h3>
<p>Check whether a plugin UI is a given type. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ui</i> The Plugin UI<br />
 <i>class_uri</i> The URI of the LV2 UI type to check this UI against</dl>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>SLV2Value slv2_ui_get_bundle_uri (SLV2UIui)</h3>
<p>Get the URI for a Plugin UI&#8217;s bundle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ui</i> The Plugin UI</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>a shared value which must not be modified or freed.</dl>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>SLV2Value slv2_ui_get_binary_uri (SLV2UIui)</h3>
<p>Get the URI for a Plugin UI&#8217;s shared library. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ui</i> The Plugin UI</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>a shared value which must not be modified or freed.</dl>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>SLV2Values slv2_port_get_value (SLV2Pluginplugin, SLV2Portport, SLV2Valuepredicate)</h3>
<p>Port analog of slv2_plugin_get_value. Time = Query</p>
<h3>SLV2Values slv2_port_get_value_by_qname (SLV2Pluginplugin, SLV2Portport, const char *property_uri)</h3>
<p>Port analog of slv2_plugin_get_value_by_qname. Time = Query</p>
<h3>SLV2Values slv2_port_get_value_by_qname_i18n (SLV2Pluginplugin, SLV2Portport, const char *property_uri)</h3>
<p>Port analog of slv2_plugin_get_value_by_qname_i18n. Time = Query</p>
<h3>SLV2Values slv2_port_get_properties (SLV2Pluginplugin, SLV2Portport)</h3>
<p>Return the LV2 port properties of a port. Time = Query</p>
<h3>bool slv2_port_has_property (SLV2Pluginp, SLV2Portport, SLV2Valueproperty_uri)</h3>
<p>Return whether a port has a certain property. Time = Query</p>
<h3>bool slv2_port_supports_event (SLV2Pluginp, SLV2Portport, SLV2Valueevent_uri)</h3>
<p>Return whether a port is an event port and supports a certain event type. Time = Query</p>
<h3>SLV2Value slv2_port_get_symbol (SLV2Pluginplugin, SLV2Portport)</h3>
<p>Get the symbol of a port. The &#8216;symbol&#8217; is a short string, a valid C identifier. Returned value is owned by <i>port</i> and must not be freed. </p>
<p> Time = Query</p>
<h3>SLV2Value slv2_port_get_name (SLV2Pluginplugin, SLV2Portport)</h3>
<p>Get the name of a port. This is guaranteed to return the untranslated name (the doap:name in the data file without a language tag). Returned value must be freed by the caller. </p>
<p> Time = Query</p>
<h3>SLV2Values slv2_port_get_classes (SLV2Pluginplugin, SLV2Portport)</h3>
<p>Get all the classes of a port. This can be used to determine if a port is an input, output, audio, control, midi, etc, etc, though it&#8217;s simpler to use slv2_port_is_a. The returned list does not include lv2:Port, which is implied. </p>
<p> Returned value is shared and must not be destroyed by caller. </p>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>bool slv2_port_is_a (SLV2Pluginplugin, SLV2Portport, SLV2Valueport_class)</h3>
<p>Determine if a port is of a given class (input, output, audio, etc). For convenience/performance/extensibility reasons, hosts are expected to create an SLV2Value for each port class they &#8216;care about&#8217;. Well-known type URI strings are defined (e.g. SLV2_PORT_CLASS_INPUT) for convenience, but this function is designed so that SLV2 is usable with any port types without requiring explicit support in SLV2. </p>
<p> Time = <a href="/docs/linux/man/n-o/">O</a>(n) (n pointer comparisons where n is the number of classes of this port, so this method is suitable for realtime use on any sane port).</p>
<h3>void slv2_port_get_range (SLV2Pluginplugin, SLV2Portport, SLV2Value *def, SLV2Value *min, SLV2Value *max)</h3>
<p>Get the default, minimum, and maximum values of a port. <i>def</i>, <i>min</i>, and <i>max</i> are outputs, pass pointers to uninitialized (i.e. NOT created with slv2_value_new) SLV2Value variables. These will be set to point at new values (which must be freed by the caller using slv2_value_free), or NULL if the value does not exist. </p>
<p> Time = Query</p>
<h3>SLV2ScalePoints slv2_port_get_scale_points (SLV2Pluginplugin, SLV2Portport)</h3>
<p>Get the scale points (enumeration values) of a port. This returns a collection of &#8216;interesting&#8217; named values of a port (e.g. appropriate entries for a UI selector associated with this port). </p>
<p> Returned value may be NULL if <i>port</i> has no scale points, otherwise it must be freed by caller with slv2_scale_points_free.</p>
<h3>unsigned slv2_results_size (SLV2Resultsresults)</h3>
<p>Return the number of matches in <i>results</i>. Note this should not be used to iterate over a result set (since it will iterate to the end of <i>results</i> and rewinding is impossible). Instead, use slv2_results_next and slv2_results_finished repeatedly.</p>
<h3>SLV2Value slv2_results_get_binding_value (SLV2Resultsresults, unsignedindex)</h3>
<p>Return a binding in <i>results</i> by index. Indices correspond to selected variables in the query in order of appearance. Returned value must be freed by caller with slv2_value_free. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>NULL if binding value can not be expressed as an SLV2Value.</dl>
<h3>SLV2Value slv2_results_get_binding_value_by_name (SLV2Resultsresults, const char *name)</h3>
<p>Return a binding in <i>results</i> by name. <i>name</i> corresponds to the name of the SPARQL variable (without the &#8216;?&#8217;). Returned value must be freed by caller with slv2_value_free. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>NULL if binding value can not be expressed as an SLV2Value.</dl>
<h3>const char* slv2_results_get_binding_name (SLV2Resultsresults, unsignedindex)</h3>
<p>Return the name of a binding in <i>results</i>. Returned value is shared and must not be freed by caller. Indices correspond to selected variables in the query in order of appearance.</p>
<h3>SLV2Value slv2_scale_point_get_label (SLV2ScalePointpoint)</h3>
<p>Get the label of this scale point (enumeration value) Returned value is owned by <i>point</i> and must not be freed.</p>
<h3>SLV2Value slv2_scale_point_get_value (SLV2ScalePointpoint)</h3>
<p>Get the value of this scale point (enumeration value) Returned value is owned by <i>point</i> and must not be freed.</p>
<h3>SLV2Value slv2_value_new_uri (SLV2Worldworld, const char *uri)</h3>
<p>Create a new URI value. Returned value must be freed by caller with slv2_value_free.</p>
<h3>SLV2Value slv2_value_new_string (SLV2Worldworld, const char *str)</h3>
<p>Create a new string value (with no language). Returned value must be freed by caller with slv2_value_free.</p>
<h3>SLV2Value slv2_value_new_int (SLV2Worldworld, intval)</h3>
<p>Create a new integer value. Returned value must be freed by caller with slv2_value_free.</p>
<h3>SLV2Value slv2_value_new_float (SLV2Worldworld, floatval)</h3>
<p>Create a new floating point value. Returned value must be freed by caller with slv2_value_free.</p>
<h3>char* slv2_value_get_turtle_token (SLV2Valuevalue)</h3>
<p>Return this value as a Turtle/SPARQL token. Examples: <a rel="nofollow" href="http://example.org/foo">http://example.org/foo</a> doap:name &#8216;this is a string&#8217; 1.0 1 </p>
<p> Returned string is newly allocated and must be freed by caller.</p>
<h3>bool slv2_value_is_uri (SLV2Valuevalue)</h3>
<p>Return whether the value is a URI (resource). Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>const char* slv2_value_as_uri (SLV2Valuevalue)</h3>
<p>Return this value as a URI string, e.g. &#8216;<a rel="nofollow" href="http://example.org/foo'.">http://example.org/foo&#8217;.</a> </p>
<p> Valid to call only if slv2_value_is_uri(<i>value</i>) returns true. Returned value is owned by <i>value</i> and must not be freed by caller. </p>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>bool slv2_value_is_literal (SLV2Valuevalue)</h3>
<p>Return whether this value is a literal (i.e. not a URI). </p>
<p> Returns true if <i>value</i> is a string or numeric value. </p>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>bool slv2_value_is_string (SLV2Valuevalue)</h3>
<p>Return whether this value is a string literal. Returns true if <i>value</i> is a string (but not numeric) value. </p>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>const char* slv2_value_as_string (SLV2Valuevalue)</h3>
<p>Return <i>value</i> as a string. Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>bool slv2_value_is_float (SLV2Valuevalue)</h3>
<p>Return whether this value is a decimal literal. Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>float slv2_value_as_float (SLV2Valuevalue)</h3>
<p>Return <i>value</i> as a float. Valid to call only if slv2_value_is_float(<i>value</i>) or slv2_value_is_int(<i>value</i>) returns true. </p>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>bool slv2_value_is_int (SLV2Valuevalue)</h3>
<p>Return whether this value is an integer literal. Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>int slv2_value_as_int (SLV2Valuevalue)</h3>
<p>Return <i>value</i> as an integer. Valid to call only if slv2_value_is_int(<i>value</i>) returns true. </p>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for SLV2 from the source code.</p>
