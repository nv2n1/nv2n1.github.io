---
title: "globus_module_get_module_pointer(3)"
name: "globus_module_get_module_pointer"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_module_get_module_pointer/"
description: "globus_module.h –"
---

<h2 class="name">NAME</h2>
<p> globus_module.h &#8211; </p>
<p> Reference Counting Module Activation and Deactivation.</p>
<h2>SYNOPSIS</h2>
<p> #include &#8216;globus_error_generic.h&#8217;<br />
 #include &lt;stdio.h&gt; </p>
<h3>Data Structures</h3>
<p> struct <code>globus_module_descriptor_s</code><br />
 <i>Module Descriptor. </i></p>
<h3>Typedefs</h3>
<p> typedef int(* <code>globus_module_deactivate_proxy_cb_t</code> )(<code>globus_module_descriptor_t</code> *module_descriptor, void *user_arg) </p>
<h3>Functions</h3>
<p> int <code>globus_module_activate</code> (<code>globus_module_descriptor_t</code> *module_descriptor)<br />
 <i>Activate a module. </i><br />
 int <code>globus_module_activate_array</code> (<code>globus_module_descriptor_t</code> *modules[], <code>globus_module_descriptor_t</code> **failed_module)<br />
 <i>Activate a group of modules. </i><br />
 int <code>globus_module_deactivate</code> (<code>globus_module_descriptor_t</code> *module_descriptor)<br />
 <i>Deactivate a module. </i><br />
 int <code>globus_module_activate_proxy</code> (<code>globus_module_descriptor_t</code> *module_descriptor, <code>globus_module_deactivate_proxy_cb_t</code> deactivate_cb, void *user_arg) </p>
<p> void <code>globus_module_setenv</code> (const char *name, const char *value) </p>
<p> char * <code>globus_module_getenv</code> (const char *name) </p>
<p> void * <code>globus_module_get_module_pointer</code> (<code>globus_module_descriptor_t</code> *) </p>
<p> int <code>globus_module_get_version</code> (<code>globus_module_descriptor_t</code> *module_descriptor, globus_version_t *version) </p>
<p> void <code>globus_module_print_version</code> (<code>globus_module_descriptor_t</code> *module_descriptor, FILE *stream, <code>globus_bool_t</code> verbose) </p>
<p> void <code>globus_module_print_activated_versions</code> (FILE *stream, <code>globus_bool_t</code> verbose) </p>
<p> void <code>globus_version_print</code> (const char *name, const globus_version_t *version, FILE *stream, <code>globus_bool_t</code> verbose) </p>
<h2>Detailed Description</h2>
<p> Reference Counting Module Activation and Deactivation. </p>
<h2>Typedef Documentation</h2>
<h3>typedef int(* globus_module_deactivate_proxy_cb_t)(<code>globus_module_descriptor_t</code> *module_descriptor, void *user_arg)</h3>
<p> module must be deactivated in this call with module_descriptor-&gt;deactivation_func(); (be sure module_descriptor-&gt;deactivation_func is !NULL)</p>
<h2>Function Documentation</h2>
<h3>int globus_module_activate_proxy (<code>globus_module_descriptor_t</code> *module_descriptor, <code>globus_module_deactivate_proxy_cb_t</code>deactivate_cb, void *user_arg)</h3>
<p> this call registers a callback to be called to handle deactivation when <code>globus_module_deactivate()</code> or globus_module_deactivate_all() is called </p>
<p> The callback is only respected for the first call to activate this module. The purpose of these proxy calls is to allow &#8216;private&#8217; module descriptors that are activated by some other user function, but may still be affected by deactivate_all().</p>
<h3>void* globus_module_get_module_pointer (<code>globus_module_descriptor_t</code> *)</h3>
<p> Get a module pointer</p>
<h3>int globus_module_get_version (<code>globus_module_descriptor_t</code> *module_descriptor, globus_version_t *version)</h3>
<p> get version associated with module </p>
<p> This function copies the version structure associated with the module into &#8216;version&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>module_descriptor</i> pointer to a module descriptor (module does NOT need to be activated)<br />
 <i>version</i> pointer to storage for a globus_version_t. The version will be copied into this</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_SUCCESS</p>
<dt>&bull;</p>
<dd> GLOBUS_FAILURE if there is no version associated with this module (module-&gt;version == null)</dl>
</dl>
<h3>char* globus_module_getenv (const char *name)</h3>
<p> Get the value of an environment variable</p>
<h3>void globus_module_print_activated_versions (FILE *stream, <code>globus_bool_t</code>verbose)</h3>
<p> print all activated modules&#8217; versions </p>
<p> This function prints all activated modules&#8217; version info using the standard form provided by globus_version_print </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>stream</i> stream to print on (stdout, stderr, etc)<br />
 <i>verbose</i> If GLOBUS_TRUE, then all available version info is printed (ex: globus_module: 1.1 (1013708618-5)) else, only the major.minor is printed (ex: globus_module: 1.1)</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> void</dl>
</dl>
<h3>void globus_module_print_version (<code>globus_module_descriptor_t</code> *module_descriptor, FILE *stream, <code>globus_bool_t</code>verbose)</h3>
<p> print module&#8217;s version </p>
<p> This function prints a modules version info using the standard form provided by globus_version_print </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>module_descriptor</i> pointer to a module descriptor (module does NOT need to be activated)<br />
 <i>stream</i> stream to print on (stdout, stderr, etc)<br />
 <i>verbose</i> If GLOBUS_TRUE, then all available version info is printed (ex: globus_module: 1.1 (1013708618-5)) else, only the major.minor is printed (ex: globus_module: 1.1)</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> void</dl>
</dl>
<h3>void globus_module_setenv (const char *name, const char *value)</h3>
<p> set an environment variable</p>
<h3>void globus_version_print (const char *name, const globus_version_t *version, FILE *stream, <code>globus_bool_t</code>verbose)</h3>
<p> print version structure </p>
<p> This function provides a stand way of printing version information The version is printed to stream with the following form: name: major.minor if verbose = false name: major.minor.timestamp-branch_id if verbose = true </p>
<p> In either case, if name is NULL, then only the numerical version will be printed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>name</i> A string to prefix the version. May be NULL<br />
 <i>version</i> The version structure containing the info to print. (May be NULL, although pointless to do so)<br />
 <i>stream</i> stream to print on (stdout, stderr, etc)<br />
 <i>verbose</i> If GLOBUS_TRUE, then all available version info is printed (ex: globus_module: 1.1 (1013708618-5)) else, only the major.minor is printed (ex: globus_module: 1.1)</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> void</dl>
</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAJ">Function Documentation</a></p>
<dd>
<dt><a href="#lbAS">Author</a></p>
<dd></dl>
