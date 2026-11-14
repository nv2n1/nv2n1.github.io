---
title: "slv2_world(3)"
name: "slv2_world"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slv2_world/"
description: "Global library state –"
---

<p>Global library state &#8211;</p>
<h3>Functions</h3>
<p>SLV2World <code>slv2_world_new</code> () </p>
<p> void <code>slv2_world_free</code> (SLV2World world) </p>
<p> void <code>slv2_world_load_all</code> (SLV2World world) </p>
<p> void <code>slv2_world_load_bundle</code> (SLV2World world, SLV2Value bundle_uri) </p>
<p> SLV2PluginClass <code>slv2_world_get_plugin_class</code> (SLV2World world) </p>
<p> SLV2PluginClasses <code>slv2_world_get_plugin_classes</code> (SLV2World world) </p>
<p> SLV2Plugins <code>slv2_world_get_all_plugins</code> (SLV2World world) </p>
<p> SLV2Plugins <code>slv2_world_get_plugins_by_filter</code> (SLV2World world, bool(*include)(SLV2Plugin))</p>
<h2>Detailed Description</h2>
<p>Plugins (and plugin extensions) and the LV2 specification (and LV2 extensions) itself can be queried from the world for use. </p>
<p> Normal hosts which just want to easily load plugins by URI are strongly recommended to simply call <code>slv2_world_load_all</code> to find all installed data in the recommended way. </p>
<p> Normal hosts should NOT have to refer to bundles directly under normal circumstances. However, functions are provided to load individual bundles explicitly, intended for hosts which depend on a specific bundle (which is shipped with the application).</p>
<h2>Function Documentation</h2>
<h3>SLV2World slv2_world_new ()</h3>
<p>Initialize a new, empty world. If initialization fails, NULL is returned.</p>
<h3>void slv2_world_free (SLV2Worldworld)</h3>
<p>Destroy the world, mwahaha. NB: Destroying the world will leave dangling references in any plugin lists, plugins, etc. Do not destroy the world until you are finished with all objects that came from it.</p>
<h3>void slv2_world_load_all (SLV2Worldworld)</h3>
<p>Load all installed LV2 bundles on the system. This is the recommended way for hosts to load LV2 data. It does the most reasonable thing to find all installed plugins, extensions, etc. on the system. The environment variable LV2_PATH may be used to set the directories inside which this function will look for bundles. Otherwise a sensible, standard default will be used. </p>
<p> Use of other functions for loading bundles is <i>highly</i> discouraged without a special reason to do so &#8211; use this one. </p>
<p> Time = Query</p>
<h3>void slv2_world_load_bundle (SLV2Worldworld, SLV2Valuebundle_uri)</h3>
<p>Load a specific bundle. </p>
<dl>
<dt>&bull;</p>
<dd>bundle_uri A fully qualified URI to the bundle directory, with the trailing slash, eg. file:///usr/lib/lv2/someBundle/</dl>
<p> Normal hosts should not use this function. </p>
<p> Hosts should <code>never</code> attach any long-term significance to bundle paths as there are no guarantees they will remain consistent whatsoever. Plugins (and other things) are identified by URIs, <code>not</code> bundle or file names. </p>
<p> This function should only be used by apps which ship with a special bundle (which it knows exists at some path because the bundle is shipped with the application). </p>
<p> Time = Query</p>
<h3>SLV2PluginClass slv2_world_get_plugin_class (SLV2Worldworld)</h3>
<p>Get the parent of all other plugin classes, lv2:Plugin. Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>SLV2PluginClasses slv2_world_get_plugin_classes (SLV2Worldworld)</h3>
<p>Return a list of all found plugin classes. Returned list is owned by world and must not be freed by the caller. </p>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>SLV2Plugins slv2_world_get_all_plugins (SLV2Worldworld)</h3>
<p>Return a list of all found plugins. The returned list contains just enough references to query or instantiate plugins. The data for a particular plugin will not be loaded into memory until a call to an slv2_plugin_* function results in a query (at which time the data is cached with the SLV2Plugin so future queries are very fast). </p>
<p> Returned list must be freed by user with slv2_plugins_free. The contained plugins are owned by <i>world</i> and must not be freed by caller. </p>
<p> Time = <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<h3>SLV2Plugins slv2_world_get_plugins_by_filter (SLV2Worldworld, bool(*)(SLV2Plugin)include)</h3>
<p>Return a list of found plugins filtered by a user-defined filter function. All plugins currently found in <i>world</i> that return true when passed to <i>include</i> (a pointer to a function which takes an SLV2Plugin and returns a bool) will be in the returned list. </p>
<p> Returned list must be freed by user with slv2_plugins_free. The contained plugins are owned by <i>world</i> and must not be freed by caller. </p>
<p> Time = O(n * Time(include))</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for SLV2 from the source code.</p>
