---
title: "slv2_collections(3)"
name: "slv2_collections"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slv2_collections/"
description: "Collections of values/objects –"
---

<p>Collections of values/objects &#8211;</p>
<h3>Functions</h3>
<pre><code>void slv2_plugins_free (SLV2World world, SLV2Plugins plugins)



unsigned slv2_plugins_size (SLV2Plugins plugins)



SLV2Plugin slv2_plugins_get_by_uri (SLV2Plugins plugins, SLV2Value uri)



SLV2Plugin slv2_plugins_get_at (SLV2Plugins plugins, unsigned index)



SLV2PluginClass slv2_plugin_classes_get_by_uri (SLV2PluginClasses classes, SLV2Value uri)



bool slv2_values_contains (SLV2Values values, SLV2Value value)



SLV2UI slv2_uis_get_by_uri (SLV2UIs list, SLV2Value uri)</code></pre>
<h2>Detailed Description</h2>
<p>a fancy array).</p>
<h2>Function Documentation</h2>
<h3>void slv2_plugins_free (SLV2Worldworld, SLV2Pluginsplugins)</h3>
<p>Free a plugin collection. Freeing a plugin collection does not destroy the plugins it contains (plugins are owned by the world). <i>plugins</i> is invalid after this call. Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>unsigned slv2_plugins_size (SLV2Pluginsplugins)</h3>
<p>Get the number of plugins in the collection. Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>SLV2Plugin slv2_plugins_get_by_uri (SLV2Pluginsplugins, SLV2Valueuri)</h3>
<p>Get a plugin from the collection by URI. Return value is shared (stored in <i>plugins</i>) and must not be freed or modified by the caller in any way. </p>
<p> Time = O(<a href="/docs/linux/man/n-log2/">log2</a>(n)) </p>
<p> <code>Returns:</code></p>
<dl>
<dd>NULL if plugin with <i>url</i> not found in <i>plugins</i>.</dl>
<h3>SLV2Plugin slv2_plugins_get_at (SLV2Pluginsplugins, unsignedindex)</h3>
<p>Get a plugin from the plugins by index. <i>index</i> has no significance other than as an index into this plugins. Any <i>index</i> not less than slv2_plugins_get_length(plugins) will return NULL, so all plugins in a plugins can be enumerated by repeated calls to this function starting with <i>index</i> = 0. </p>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1) </p>
<p> <code>Returns:</code></p>
<dl>
<dd>NULL if <i>index</i> out of range.</dl>
<h3>SLV2PluginClass slv2_plugin_classes_get_by_uri (SLV2PluginClassesclasses, SLV2Valueuri)</h3>
<p>Get a plugin class from the collection by URI. Return value is shared (stored in <i>classes</i>) and must not be freed or modified by the caller in any way. </p>
<p> Time = O(<a href="/docs/linux/man/n-log2/">log2</a>(n)) </p>
<p> <code>Returns:</code></p>
<dl>
<dd>NULL if plugin with <i>url</i> not found in <i>classes</i>.</dl>
<h3>bool slv2_values_contains (SLV2Valuesvalues, SLV2Valuevalue)</h3>
<p>Return whether <i>values</i> contains <i>value</i>. Time = <a href="/docs/linux/man/n-o/">O</a>(n)</p>
<h3>SLV2UI slv2_uis_get_by_uri (SLV2UIslist, SLV2Valueuri)</h3>
<p>Get a plugin from the list by URI. Return value is shared (stored in <i>list</i>) and must not be freed or modified by the caller in any way. </p>
<p> Time = O(<a href="/docs/linux/man/n-log2/">log2</a>(n)) </p>
<p> <code>Returns:</code></p>
<dl>
<dd>NULL if plugin with <i>url</i> not found in <i>list</i>.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for SLV2 from the source code.</p>
