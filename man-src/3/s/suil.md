---
title: "suil(3)"
name: "suil"
section: "3"
letter: "s"
url: "/docs/linux/man/3-suil/"
description: "Suil –"
---

<p>Suil &#8211;</p>
<h2>Detailed Description</h2>
<p>Suil is a library for loading and wrapping LV2 plugin UIs. </p>
<p> With Suil, a host written in one supported toolkit can embed a plugin UI written in a different supported toolkit. Suil insulates hosts from toolkit libraries used by plugin UIs. For example, a Gtk host can embed a Qt UI without linking against Qt at compile time. </p>
<p> Visit <a rel="nofollow" href="http://drobilla.net/software/suil">http://drobilla.net/software/suil</a> for more information.</p>
<h3>Typedefs</h3>
<p>typedef struct SuilHostImpl <code>SuilHost</code> </p>
<p> typedef struct SuilInstanceImpl <code>SuilInstance</code> </p>
<p> typedef void * <code>SuilHandle</code> </p>
<p> typedef void * <code>SuilWidget</code> </p>
<p> typedef void * <code>SuilController</code> </p>
<p> typedef void(* <code>SuilPortWriteFunc</code> )(<code>SuilController</code> controller, uint32_t port_index, uint32_t buffer_size, uint32_t protocol, void const *buffer) </p>
<p> typedef uint32_t(* <code>SuilPortIndexFunc</code> )(<code>SuilController</code> controller, const char *port_symbol) </p>
<p> typedef uint32_t(* <code>SuilPortSubscribeFunc</code> )(<code>SuilController</code> controller, uint32_t port_index, uint32_t protocol, const LV2_Feature *const *features) </p>
<p> typedef uint32_t(* <code>SuilPortUnsubscribeFunc</code> )(<code>SuilController</code> controller, uint32_t port_index, uint32_t protocol, const LV2_Feature *const *features) </p>
<p> typedef void(* <code>SuilTouchFunc</code> )(<code>SuilController</code> controller, uint32_t port_index, bool grabbed)</p>
<h3>Functions</h3>
<p><code>SuilHost</code> * <code>suil_host_new</code> (<code>SuilPortWriteFunc</code> write_func, <code>SuilPortIndexFunc</code> index_func, <code>SuilPortSubscribeFunc</code> subscribe_func, <code>SuilPortUnsubscribeFunc</code> unsubscribe_func) </p>
<p> void <code>suil_host_set_touch_func</code> (<code>SuilHost</code> *host, <code>SuilTouchFunc</code> touch_func) </p>
<p> void <code>suil_host_free</code> (<code>SuilHost</code> *host) </p>
<p> unsigned <code>suil_ui_supported</code> (const char *host_type_uri, const char *ui_type_uri) </p>
<p> <code>SuilInstance</code> * <code>suil_instance_new</code> (<code>SuilHost</code> *host, <code>SuilController</code> controller, const char *container_type_uri, const char *plugin_uri, const char *ui_uri, const char *ui_type_uri, const char *ui_bundle_path, const char *ui_binary_path, const LV2_Feature *const *features) </p>
<p> void <code>suil_instance_free</code> (<code>SuilInstance</code> *instance) </p>
<p> <code>SuilHandle</code> <code>suil_instance_get_handle</code> (<code>SuilInstance</code> *instance) </p>
<p> <code>SuilWidget</code> <code>suil_instance_get_widget</code> (<code>SuilInstance</code> *instance) </p>
<p> void <code>suil_instance_port_event</code> (<code>SuilInstance</code> *instance, uint32_t port_index, uint32_t buffer_size, uint32_t format, const void *buffer) </p>
<p> const void * <code>suil_instance_extension_data</code> (<code>SuilInstance</code> *instance, const char *uri)</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct SuilHostImpl <code>SuilHost</code></h3>
<p>UI host descriptor. This contains the various functions that a plugin UI may use to communicate with the plugin. It is passed to <code>suil_instance_new()</code> to provide these functions to the UI.</p>
<h3>typedef struct SuilInstanceImpl <code>SuilInstance</code></h3>
<p>An instance of an LV2 plugin UI.</p>
<h3>typedef void* <code>SuilHandle</code></h3>
<p>Opaque pointer to a UI handle.</p>
<h3>typedef void* <code>SuilWidget</code></h3>
<p>Opaque pointer to a UI widget.</p>
<h3>typedef void* <code>SuilController</code></h3>
<p>UI controller. This is an opaque pointer passed by the user which is passed to the various UI control functions (e.g. SuilPortWriteFunc). It is typically used to pass a pointer to some controller object the host uses to communicate with plugins.</p>
<h3>typedef void(* SuilPortWriteFunc)(<code>SuilController</code> controller, uint32_t port_index, uint32_t buffer_size, uint32_t protocol, void const *buffer)</h3>
<p>Function to write/send a value to a port.</p>
<h3>typedef uint32_t(* SuilPortIndexFunc)(<code>SuilController</code> controller, const char *port_symbol)</h3>
<p>Function to return the index for a port by symbol.</p>
<h3>typedef uint32_t(* SuilPortSubscribeFunc)(<code>SuilController</code> controller, uint32_t port_index, uint32_t protocol, const LV2_Feature *const *features)</h3>
<p>Function to subscribe to notifications for a port.</p>
<h3>typedef uint32_t(* SuilPortUnsubscribeFunc)(<code>SuilController</code> controller, uint32_t port_index, uint32_t protocol, const LV2_Feature *const *features)</h3>
<p>Function to unsubscribe from notifications for a port.</p>
<h3>typedef void(* SuilTouchFunc)(<code>SuilController</code> controller, uint32_t port_index, bool grabbed)</h3>
<p>Function called when a control is grabbed or released.</p>
<h2>Function Documentation</h2>
<h3><code>SuilHost</code>* suil_host_new (<code>SuilPortWriteFunc</code>write_func, <code>SuilPortIndexFunc</code>index_func, <code>SuilPortSubscribeFunc</code>subscribe_func, <code>SuilPortUnsubscribeFunc</code>unsubscribe_func)</h3>
<p>Create a new UI host descriptor. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>write_func</i> Function to send a value to a plugin port.<br />
 <i>index_func</i> Function to get the index for a port by symbol.<br />
 <i>subscribe_func</i> Function to subscribe to port updates.<br />
 <i>unsubscribe_func</i> Function to unsubscribe from port updates.</dl>
<h3>void suil_host_set_touch_func (<code>SuilHost</code> *host, <code>SuilTouchFunc</code>touch_func)</h3>
<p>Set a touch function for a host descriptor. Note this function will only be called if the UI supports it.</p>
<h3>void suil_host_free (<code>SuilHost</code> *host)</h3>
<p>Free host.</p>
<h3>unsigned suil_ui_supported (const char *host_type_uri, const char *ui_type_uri)</h3>
<p>Check if suil can wrap a UI type. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>host_type_uri</i> The URI of the desired widget type of the host, corresponding to the type_uri parameter of <code>suil_instance_new()</code>.<br />
 <i>ui_type_uri</i> The URI of the UI widget type.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 if wrapping is unsupported, otherwise the quality of the wrapping where 1 is the highest quality (direct native embedding with no wrapping) and increasing values are of a progressively lower quality and/or stability.</dl>
<h3><code>SuilInstance</code>* suil_instance_new (<code>SuilHost</code> *host, <code>SuilController</code>controller, const char *container_type_uri, const char *plugin_uri, const char *ui_uri, const char *ui_type_uri, const char *ui_bundle_path, const char *ui_binary_path, const LV2_Feature *const *features)</h3>
<p>Instantiate a UI for an LV2 plugin. This funcion may load a suil module to adapt the UI to the desired toolkit. Suil is configured at compile time to load modules from the appropriate place, but this can be changed at run-time via the environment variable SUIL_MODULE_DIR. This makes it possible to bundle suil with an application. </p>
<p> Note that some situations (Gtk in Qt, Windows in Gtk) require a parent container to be passed as a feature with URI LV2_UI__parent (<a rel="nofollow" href="http://lv2plug.in/ns/extensions/ui#ui)">http://lv2plug.in/ns/extensions/ui#ui)</a> in order to work correctly. The data must point to a single child container of the host widget set. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>host</i> Host descriptor.<br />
 <i>controller</i> Opaque host controller pointer.<br />
 <i>container_type_uri</i> URI of the desired host container widget type.<br />
 <i>plugin_uri</i> URI of the plugin to instantiate this UI for.<br />
 <i>ui_uri</i> URI of the specifically desired UI.<br />
 <i>ui_type_uri</i> URI of the actual UI widget type.<br />
 <i>ui_bundle_path</i> Path of the UI bundle.<br />
 <i>ui_binary_path</i> Path of the UI binary.<br />
 <i>features</i> NULL-terminated array of supported features, or NULL.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A new UI instance, or NULL if instantiation failed.</dl>
<h3>void suil_instance_free (<code>SuilInstance</code> *instance)</h3>
<p>Free a plugin UI instance. The caller must ensure all references to the UI have been dropped before calling this function (e.g. it has been removed from its parent).</p>
<h3><code>SuilHandle</code> suil_instance_get_handle (<code>SuilInstance</code> *instance)</h3>
<p>Get the handle for a UI instance. Returns the handle to the UI instance. The returned handle has opaque type to insulate the Suil API from LV2 extensions, but in pactice it is currently of type LV2UI_Handle. This should not normally be needed. </p>
<p> The returned handle is shared and must not be deleted.</p>
<h3><code>SuilWidget</code> suil_instance_get_widget (<code>SuilInstance</code> *instance)</h3>
<p>Get the widget for a UI instance. Returns an opaque pointer to a widget, the type of which matches the container_type_uri parameter of <code>suil_instance_new()</code>. Note this may be a wrapper widget created by Suil, and not necessarily the widget directly implemented by the UI.</p>
<h3>void suil_instance_port_event (<code>SuilInstance</code> *instance, uint32_tport_index, uint32_tbuffer_size, uint32_tformat, const void *buffer)</h3>
<p>Notify the UI about a change in a plugin port. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>instance</i> UI instance.<br />
 <i>port_index</i> Index of the port which has changed.<br />
 <i>buffer_size</i> Size of buffer in bytes.<br />
 <i>format</i> Format of buffer (mapped URI, or 0 for float).<br />
 <i>buffer</i> Change data, e.g. the new port value.</dl>
<p> This function can be used to notify the UI about any port change, but in the simplest case is used to set the value of lv2:ControlPort ports. For simplicity, this is a special case where format is 0, buffer_size is 4, and buffer should point to a single float. </p>
<p> The buffer must be valid only for the duration of this call, the UI must not keep a reference to it.</p>
<h3>const void* suil_instance_extension_data (<code>SuilInstance</code> *instance, const char *uri)</h3>
<p>Return a data structure defined by some LV2 extension URI.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Suil from the source code.</p>
