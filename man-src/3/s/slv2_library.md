---
title: "slv2_library(3)"
name: "slv2_library"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slv2_library/"
description: "Plugin library access –"
---

<p>Plugin library access &#8211;</p>
<h3>Functions</h3>
<p>SLV2Instance <code>slv2_plugin_instantiate</code> (SLV2Plugin plugin, double sample_rate, const LV2_Feature *const *features) </p>
<p> void <code>slv2_instance_free</code> (SLV2Instance instance) </p>
<p> static const char * <code>slv2_instance_get_uri</code> (SLV2Instance instance) </p>
<p> static void <code>slv2_instance_connect_port</code> (SLV2Instance instance, uint32_t port_index, void *data_location) </p>
<p> static void <code>slv2_instance_activate</code> (SLV2Instance instance) </p>
<p> static void <code>slv2_instance_run</code> (SLV2Instance instance, uint32_t sample_count) </p>
<p> static void <code>slv2_instance_deactivate</code> (SLV2Instance instance) </p>
<p> static const void * <code>slv2_instance_get_extension_data</code> (SLV2Instance instance, const char *uri) </p>
<p> static const LV2_Descriptor * <code>slv2_instance_get_descriptor</code> (SLV2Instance instance) </p>
<p> static LV2_Handle <code>slv2_instance_get_handle</code> (SLV2Instance instance) </p>
<p> SLV2UIInstance <code>slv2_ui_instantiate</code> (SLV2Plugin plugin, SLV2UI ui, LV2UI_Write_Function write_function, LV2UI_Controller controller, const LV2_Feature *const *features) </p>
<p> void <code>slv2_ui_instance_free</code> (SLV2UIInstance instance) </p>
<p> const LV2UI_Descriptor * <code>slv2_ui_instance_get_descriptor</code> (SLV2UIInstance instance) </p>
<p> LV2UI_Handle <code>slv2_ui_instance_get_handle</code> (SLV2UIInstance instance)</p>
<h2>Detailed Description</h2>
<p>These functions interact with the binary library code only, they do not read data files in any way.</p>
<h2>Function Documentation</h2>
<h3>SLV2Instance slv2_plugin_instantiate (SLV2Pluginplugin, doublesample_rate, const LV2_Feature *const *features)</h3>
<p>Instantiate a plugin. The returned object represents shared library objects loaded into memory, it must be cleaned up with slv2_instance_free when no longer needed. </p>
<p> <i>plugin</i> is not modified or directly referenced by the returned object (instances store only a copy of the plugin&#8217;s URI). </p>
<p> <i>host_features</i> NULL-terminated array of features the host supports. NULL may be passed if the host supports no additional features (unlike the LV2 specification &#8211; SLV2 takes care of it). </p>
<p> <code>Returns:</code></p>
<dl>
<dd>NULL if instantiation failed.</dl>
<h3>void slv2_instance_free (SLV2Instanceinstance)</h3>
<p>Free a plugin instance. <i>instance</i> is invalid after this call.</p>
<h3>static const char* slv2_instance_get_uri (SLV2Instanceinstance) [inline], [static]</h3>
<p>Get the URI of the plugin which <i>instance</i> is an instance of. Returned string is shared and must not be modified or deleted.</p>
<h3>static void slv2_instance_connect_port (SLV2Instanceinstance, uint32_tport_index, void *data_location) [inline], [static]</h3>
<p>Connect a port to a data location. This may be called regardless of whether the plugin is activated, activation and deactivation does not destroy port connections.</p>
<h3>static void slv2_instance_activate (SLV2Instanceinstance) [inline], [static]</h3>
<p>Activate a plugin instance. This resets all state information in the plugin, except for port data locations (as set by slv2_instance_connect_port). This MUST be called before calling slv2_instance_run.</p>
<h3>static void slv2_instance_run (SLV2Instanceinstance, uint32_tsample_count) [inline], [static]</h3>
<p>Run <i>instance</i> for <i>sample_count</i> frames. If the hint lv2:hardRtCapable is set for this plugin, this function is guaranteed not to block.</p>
<h3>static void slv2_instance_deactivate (SLV2Instanceinstance) [inline], [static]</h3>
<p>Deactivate a plugin instance. Note that to run the plugin after this you must activate it, which will reset all state information (except port connections).</p>
<h3>static const void* slv2_instance_get_extension_data (SLV2Instanceinstance, const char *uri) [inline], [static]</h3>
<p>Get extension data from the plugin instance. The type and semantics of the data returned is specific to the particular extension, though in all cases it is shared and must not be deleted.</p>
<h3>static const LV2_Descriptor* slv2_instance_get_descriptor (SLV2Instanceinstance) [inline], [static]</h3>
<p>Get the LV2_Descriptor of the plugin instance. Normally hosts should not need to access the LV2_Descriptor directly, use the slv2_instance_* functions. </p>
<p> The returned descriptor is shared and must not be deleted.</p>
<h3>static LV2_Handle slv2_instance_get_handle (SLV2Instanceinstance) [inline], [static]</h3>
<p>Get the LV2_Handle of the plugin instance. Normally hosts should not need to access the LV2_Handle directly, use the slv2_instance_* functions. </p>
<p> The returned handle is shared and must not be deleted.</p>
<h3>SLV2UIInstance slv2_ui_instantiate (SLV2Pluginplugin, SLV2UIui, LV2UI_Write_Functionwrite_function, LV2UI_Controllercontroller, const LV2_Feature *const *features)</h3>
<p>Instantiate a plugin UI. The returned object represents shared library objects loaded into memory, it must be cleaned up with slv2_ui_instance_free when no longer needed. </p>
<p> <i>plugin</i> is not modified or directly referenced by the returned object (instances store only a copy of the plugin&#8217;s URI). </p>
<p> <i>host_features</i> NULL-terminated array of features the host supports. NULL may be passed if the host supports no additional features (unlike the LV2 specification &#8211; SLV2 takes care of it). </p>
<p> <code>Returns:</code></p>
<dl>
<dd>NULL if instantiation failed.</dl>
<h3>void slv2_ui_instance_free (SLV2UIInstanceinstance)</h3>
<p>Free a plugin UI instance. It is the caller&#8217;s responsibility to ensure all references to the UI instance (including any returned widgets) are cut before calling this function. </p>
<p> <i>instance</i> is invalid after this call.</p>
<h3>const LV2UI_Descriptor* slv2_ui_instance_get_descriptor (SLV2UIInstanceinstance)</h3>
<p>Get the LV2UI_Descriptor of the plugin UI instance. Normally hosts should not need to access the LV2UI_Descriptor directly, use the slv2_ui_instance_* functions. </p>
<p> The returned descriptor is shared and must not be deleted.</p>
<h3>LV2UI_Handle slv2_ui_instance_get_handle (SLV2UIInstanceinstance)</h3>
<p>Get the LV2UI_Handle of the plugin UI instance. Normally hosts should not need to access the LV2UI_Handle directly, use the slv2_ui_instance_* functions. </p>
<p> The returned handle is shared and must not be deleted.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for SLV2 from the source code.</p>
