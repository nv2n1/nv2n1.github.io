---
title: "globus_extension_register_builtin(3)"
name: "globus_extension_register_builtin"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_extension_register_builtin/"
description: "globus_extension.h –"
---

<h2 class="name">NAME</h2>
<p> globus_extension.h &#8211; </p>
<p> Globus Extension Modules.</p>
<h2>SYNOPSIS</h2>
<p> #include &#8216;globus_common_include.h&#8217;<br />
 #include &#8216;globus_module.h&#8217;<br />
 #include &#8216;globus_hashtable.h&#8217; </p>
<h3>Macros</h3>
<p> #define <code>GlobusExtensionDefineModule</code>(name) <code>globus_module_descriptor_t</code> name##_module </p>
<h3>Functions</h3>
<p> int <code>globus_extension_activate</code> (const char *extension_name) </p>
<p> void * <code>globus_extension_lookup</code> (globus_extension_handle_t *handle, globus_extension_registry_t *registry, void *symbol) </p>
<p> int <code>globus_extension_register_builtin</code> (const char *extension_name, <code>globus_module_descriptor_t</code> *module_descriptor) </p>
<h2>Detailed Description</h2>
<p> Globus Extension Modules. </p>
<h2>Macro Definition Documentation</h2>
<h3>#define GlobusExtensionDefineModule(name) <code>globus_module_descriptor_t</code> name##_module</h3>
<p> Declare your module with the following. </p>
<p> Ex: <code>GlobusExtensionDefineModule(my_module)</code> = { &#8216;my_module&#8217;, globus_l_my_module_activate, globus_l_my_module_deactivate, NULL, NULL, &amp;local_version };</p>
<h2>Function Documentation</h2>
<h3>int globus_extension_activate (const char *extension_name)</h3>
<p> loads the shared library &#8216;lib<code>extension_name</code>_<code>flavor</code>.so&#8217; from $GLOBUS_LOCATION/lib (or other location in LD_LIBRARY_PATH and activates the module defined within. </p>
<p> In the future, a configuration file will be supported allowing arbitrary extension names to be mapped to a specific library name. </p>
<p> Also, when builtin (compiled in) extensions are supported, this will activate those directly without needing to load the library. </p>
<p> Search order:</p>
<dl>
<dt>&bull;</p>
<dd> <code>extension_name</code> in mappings hash XXX not implemented</p>
<dt> &bull;</p>
<dd> mapped name in builtin hash XXX not implemented</p>
<dt> &bull;</p>
<dd> mapped name in dll hash XXX not implemented</p>
<dt> &bull;</p>
<dd> load mapped name XXX not implemented</dl>
<dl>
<dt>&bull;</p>
<dd> <code>extension_name</code> in builtin hash</p>
<dt>&bull;</p>
<dd> <code>extension_name</code> in dll hash</p>
<dt>&bull;</p>
<dd> load library if(strchr(<code>extension_name</code>, &#8216;/&#8217;))</p>
<dt> &bull;</p>
<dd> concatenate / + dirname(<code>extension_name</code>) + /lib + basename(<code>extension_name</code>) + _&lt;flavor&gt;.so to $GLOBUS_LOCATION/lib and each search path in mappings file XXX not implemented (eg, for <code>extension_name</code> == wsrf/services/CounterService, load $GLOBUS_LOCATION/lib/wsrf/services/libCounterService_gcc32dbg.so)</p>
<dt> &bull;</p>
<dd> lib + basename(<code>entension_name</code>) + _<code>flavor</code>.so subject to LD_LIBRARY_PATH else</p>
<dt> &bull;</p>
<dd> load lib<code>extension_name</code>_<code>build_flavor</code> subject to LD_LIBRARY_PATH</dl>
<h3>void* globus_extension_lookup (globus_extension_handle_t *handle, globus_extension_registry_t *registry, void *symbol)</h3>
<p> Get the datum associated with symbol in this registry. </p>
<p> You MUST call globus_extension_release() when you are done using the data. the lookup() and release() calls handle the reference counting that prevents an extension from being unloaded while things it provides are being used. Do NOT call release() until you are done accessing the data from * the lookup() call. </p>
<p> release() could potentially block as a result of module deactivation and unloading. ensuring that globus_extension_deactivate() is not called with outstanding references will prevent that. </p>
<p> symbol is a char * by default. the key can be changed by calling globus_extension_registry_set_hashing() before it is accessed.</p>
<h3>int globus_extension_register_builtin (const char *extension_name, <code>globus_module_descriptor_t</code> *module_descriptor)</h3>
<p> hopefully in the future, these functions will only be needed by generated code</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Function Documentation</a></p>
<dd>
<dt><a href="#lbAM">Author</a></p>
<dd></dl>
