---
title: "dmlite-h(3)"
name: "dmlite-h"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dmlite-h/"
description: "dmlite.h –"
---

<p>dmlite.h &#8211; </p>
<p> C wrapper for DMLite.</p>
<h2>Synopsis</h2>
<p>#include &#8216;dmlite/common/config.h&#8217;<br />
 #include &#8216;dmlite/common/errno.h&#8217;<br />
 #include &#8216;any.h&#8217;<br />
 #include &lt;stdlib.h&gt;<br />
 #include &lt;sys/stat.h&gt;<br />
 #include &lt;utime.h&gt; </p>
<h3>Data Structures</h3>
<p>struct <code>dmlite_credentials</code><br />
 <i>Security credentials. </i><br />
 struct <code>dmlite_security_ent</code><br />
 <i>Used to handle user and group information. </i><br />
 struct <code>dmlite_security_context</code><br />
 <i>Security context. </i></p>
<h3>Typedefs</h3>
<p>typedef struct <code>dmlite_manager</code> <code>dmlite_manager</code><br />
 <i>Handle for the plugin manager. </i><br />
 typedef struct <code>dmlite_context</code> <code>dmlite_context</code><br />
 <i>Handle for a initialized context. </i><br />
 typedef struct <code>dmlite_credentials</code> <code>dmlite_credentials</code><br />
 <i>Security credentials. </i><br />
 typedef struct <code>dmlite_security_ent</code> <code>dmlite_security_ent</code><br />
 <i>Used to handle user and group information. </i><br />
 typedef struct<br />
 <code>dmlite_security_context</code> <code>dmlite_security_context</code>&quot;<br />
 <i>Security context. </i></p>
<h3>Functions</h3>
<p>unsigned <code>dmlite_api_version</code> (void)<br />
 <i>Gets the API version. </i><br />
 <code>dmlite_manager</code> * <code>dmlite_manager_new</code> (void)<br />
 <i>Initializes a dmlite_manager. </i><br />
 int <code>dmlite_manager_free</code> (<code>dmlite_manager</code> *manager)<br />
 <i>Destroys the manager. </i><br />
 int <code>dmlite_manager_load_plugin</code> (<code>dmlite_manager</code> *manager, const char *lib, const char *id)<br />
 <i>Loads a library. </i><br />
 int <code>dmlite_manager_set</code> (<code>dmlite_manager</code> *manager, const char *key, const char *value)<br />
 <i>Sets a configuration parameter. </i><br />
 int <code>dmlite_manager_load_configuration</code> (<code>dmlite_manager</code> *manager, const char *file)<br />
 <i>Loads a configuration file. </i><br />
 int <code>dmlite_manager_get</code> (<code>dmlite_manager</code> *handle, const char *key, char *buffer, size_t bufsize)<br />
 <i>Returns the associated value with the given key. </i><br />
 int <code>dmlite_manager_errno</code> (<code>dmlite_manager</code> *manager)<br />
 <i>Returns the last error code. </i><br />
 int <code>dmlite_manager_errtype</code> (<code>dmlite_manager</code> *manager)<br />
 <i>Returns the type of the last error. </i><br />
 const char * <code>dmlite_manager_error</code> (<code>dmlite_manager</code> *manager)<br />
 <i>Returns the string that describes the last error. </i><br />
 <code>dmlite_context</code> * <code>dmlite_context_new</code> (<code>dmlite_manager</code> *manager)<br />
 <i>Returns a usable context from the loaded libraries. </i><br />
 int <code>dmlite_context_free</code> (<code>dmlite_context</code> *context)<br />
 <i>Destroys the context. </i><br />
 int <code>dmlite_errno</code> (<code>dmlite_context</code> *context)<br />
 <i>Returns the error code from the last failure. </i><br />
 int <code>dmlite_errtype</code> (<code>dmlite_context</code> *context)<br />
 <i>Returns the type of the last error. </i><br />
 const char * <code>dmlite_error</code> (<code>dmlite_context</code> *context)<br />
 <i>Error string from the last failed function. </i><br />
 int <code>dmlite_setcredentials</code> (<code>dmlite_context</code> *context, const <code>dmlite_credentials</code> *cred)<br />
 <i>Sets the user security credentials. </i><br />
 const <code>dmlite_security_context</code> * <code>dmlite_get_security_context</code> (<code>dmlite_context</code> *context)<br />
 <i>Returns the security context. There is no need to free. </i><br />
 int <code>dmlite_set</code> (<code>dmlite_context</code> *context, const char *k, const <code>dmlite_any</code> *v)<br />
 <i>Sets a configuration parameter tied to a context. </i><br />
 int <code>dmlite_set_array</code> (<code>dmlite_context</code> *context, const char *k, unsigned n, <code>dmlite_any</code> *const *v)<br />
 <i>Sets a configuration parameter tied to a context (array version). </i><br />
 int <code>dmlite_unset</code> (<code>dmlite_context</code> *context, const char *k)<br />
 <i>Removes a configuration parameter. </i><br />
 int <code>dmlite_unset_all</code> (<code>dmlite_context</code> *context)<br />
 <i>Removes all configuration parameters previously set. </i></p>
<h2>Detailed Description</h2>
<p>C wrapper for DMLite. </p>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Alejandro Álvarez Ayllon aalvarez [at] cern.ch</dl>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>dmlite_context</code> <code>dmlite_context</code></h3>
<p>Handle for a initialized context.</p>
<h3>typedef struct <code>dmlite_credentials</code> <code>dmlite_credentials</code></h3>
<p>Security credentials. It is up to the caller to allocate and free this pointers. DMLite will keep a copy internaly. Non used values MUST be NULL.</p>
<h3>typedef struct <code>dmlite_manager</code> <code>dmlite_manager</code></h3>
<p>Handle for the plugin manager.</p>
<h3>typedef struct <code>dmlite_security_context</code> <code>dmlite_security_context</code></h3>
<p>Security context.</p>
<h3>typedef struct <code>dmlite_security_ent</code> <code>dmlite_security_ent</code></h3>
<p>Used to handle user and group information.</p>
<h2>Function Documentation</h2>
<h3>unsigned dmlite_api_version (void)</h3>
<p>Gets the API version.</p>
<h3>int dmlite_context_free (<code>dmlite_context</code> *context)</h3>
<p>Destroys the context. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The context to free.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3><code>dmlite_context</code>* dmlite_context_new (<code>dmlite_manager</code> *manager)</h3>
<p>Returns a usable context from the loaded libraries. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>manager</i> The plugin manager.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>NULL on failure. The error code can be checked with dmlite_manager_error.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>A context is NOT thread safe.</dl>
<h3>int dmlite_errno (<code>dmlite_context</code> *context)</h3>
<p>Returns the error code from the last failure. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The context that was used in the failed function.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The error code.</dl>
<h3>const char* dmlite_error (<code>dmlite_context</code> *context)</h3>
<p>Error string from the last failed function. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The context that was used in the failed function.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A string with the error description. Do NOT free it.</dl>
<h3>int dmlite_errtype (<code>dmlite_context</code> *context)</h3>
<p>Returns the type of the last error. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The context that was used in the failed function.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The error type.</dl>
<h3>const <code>dmlite_security_context</code>* dmlite_get_security_context (<code>dmlite_context</code> *context)</h3>
<p>Returns the security context. There is no need to free. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The security context.</dl>
<h3>int dmlite_manager_errno (<code>dmlite_manager</code> *manager)</h3>
<p>Returns the last error code. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>manager</i> The plugin manager used in the failing function.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The last error code, WITHOUT the error type byte.</dl>
<h3>const char* dmlite_manager_error (<code>dmlite_manager</code> *manager)</h3>
<p>Returns the string that describes the last error. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>manager</i> The plugin manager used in the failing function.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to the error string. Do NOT free it.</dl>
<h3>int dmlite_manager_errtype (<code>dmlite_manager</code> *manager)</h3>
<p>Returns the type of the last error. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>manager</i> The plugin manager used in the failing function.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The last error type byte.</dl>
<h3>int dmlite_manager_free (<code>dmlite_manager</code> *manager)</h3>
<p>Destroys the manager. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>manager</i> The manager to be destroyed.</dl>
<h3>int dmlite_manager_get (<code>dmlite_manager</code> *handle, const char *key, char *buffer, size_tbufsize)</h3>
<p>Returns the associated value with the given key. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>manager</i> The plugin manager.<br />
 <i>key</i> The configuration parameter.<br />
 <i>buffer</i> Where to leave the string.<br />
 <i>bufsize</i> The buffer size.</dl>
<h3>int dmlite_manager_load_configuration (<code>dmlite_manager</code> *manager, const char *file)</h3>
<p>Loads a configuration file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>manager</i> The plugin manager.<br />
 <i>file</i> The configuration file</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_manager_load_plugin (<code>dmlite_manager</code> *manager, const char *lib, const char *id)</h3>
<p>Loads a library. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>manager</i> The plugin manager.<br />
 <i>lib</i> The .so file. Usually, (path)/plugin_name.so.<br />
 <i>id</i> The plugin ID. Usually, plugin_name.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3><code>dmlite_manager</code>* dmlite_manager_new (void)</h3>
<p>Initializes a dmlite_manager. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>NULL on failure.</dl>
<h3>int dmlite_manager_set (<code>dmlite_manager</code> *manager, const char *key, const char *value)</h3>
<p>Sets a configuration parameter. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>manager</i> The plugin manager.<br />
 <i>key</i> The parameter to set.<br />
 <i>value</i> The value.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_set (<code>dmlite_context</code> *context, const char *k, const <code>dmlite_any</code> *v)</h3>
<p>Sets a configuration parameter tied to a context. This can be used to pass advanced parameters to a plugin. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>k</i> The configuration key.<br />
 <i>v</i> Value.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_set_array (<code>dmlite_context</code> *context, const char *k, unsignedn, <code>dmlite_any</code> *const *v)</h3>
<p>Sets a configuration parameter tied to a context (array version). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>k</i> The configuration key.<br />
 <i>n</i> The configuration key.<br />
 <i>v</i> Array of values.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_setcredentials (<code>dmlite_context</code> *context, const <code>dmlite_credentials</code> *cred)</h3>
<p>Sets the user security credentials. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>cred</i> The security credentials.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_unset (<code>dmlite_context</code> *context, const char *k)</h3>
<p>Removes a configuration parameter. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>k</i> The configuration key.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_unset_all (<code>dmlite_context</code> *context)</h3>
<p>Removes all configuration parameters previously set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for dmlite from the source code.</p>
