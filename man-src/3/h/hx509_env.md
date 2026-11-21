---

title: "hx509_env(3)"
name: "hx509_env"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hx509_env/"
description: "hx509 enviroment functions –"
---

<p> hx509 enviroment functions &#8211; </p>
<h3>Functions</h3>
<p> int <code>hx509_env_add</code> (hx509_context context, hx509_env *env, const char *key, const char *value) </p>
<p> int <code>hx509_env_add_binding</code> (hx509_context context, hx509_env *env, const char *key, hx509_env list) </p>
<p> const char * <code>hx509_env_lfind</code> (hx509_context context, hx509_env env, const char *key, size_t len) </p>
<p> const char * <code>hx509_env_find</code> (hx509_context context, hx509_env env, const char *key) </p>
<p> hx509_env <code>hx509_env_find_binding</code> (hx509_context context, hx509_env env, const char *key) </p>
<p> void <code>hx509_env_free</code> (hx509_env *env) </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>int hx509_env_add (hx509_contextcontext, hx509_env *env, const char *key, const char *value)</h3>
<p> Add a new key/value pair to the hx509_env. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
</dt><dd> <i>context</i> A hx509 context.<br />
 <i>env</i> enviroment to add the enviroment variable too.<br />
 <i>key</i> key to add<br />
 <i>value</i> value to add</dd></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
</dt><dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dd></dl>
<h3>int hx509_env_add_binding (hx509_contextcontext, hx509_env *env, const char *key, hx509_envlist)</h3>
<p> Add a new key/binding pair to the hx509_env. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
</dt><dd> <i>context</i> A hx509 context.<br />
 <i>env</i> enviroment to add the enviroment variable too.<br />
 <i>key</i> key to add<br />
 <i>list</i> binding list to add</dd></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
</dt><dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dd></dl>
<h3>const char * hx509_env_find (hx509_contextcontext, hx509_envenv, const char *key)</h3>
<p> Search the hx509_env for a key. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
</dt><dd> <i>context</i> A hx509 context.<br />
 <i>env</i> enviroment to add the enviroment variable too.<br />
 <i>key</i> key to search for.</dd></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
</dt><dd> the value if the key is found, NULL otherwise.</dd></dl>
<h3>hx509_env hx509_env_find_binding (hx509_contextcontext, hx509_envenv, const char *key)</h3>
<p> Search the hx509_env for a binding. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
</dt><dd> <i>context</i> A hx509 context.<br />
 <i>env</i> enviroment to add the enviroment variable too.<br />
 <i>key</i> key to search for.</dd></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
</dt><dd> the binding if the key is found, NULL if not found.</dd></dl>
<h3>void hx509_env_free (hx509_env *env)</h3>
<p> Free an hx509_env enviroment context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
</dt><dd> <i>env</i> the enviroment to free.</dd></dl>
<h3>const char * hx509_env_lfind (hx509_contextcontext, hx509_envenv, const char *key, size_tlen)</h3>
<p> Search the hx509_env for a length based key. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
</dt><dd> <i>context</i> A hx509 context.<br />
 <i>env</i> enviroment to add the enviroment variable too.<br />
 <i>key</i> key to search for.<br />
 <i>len</i> length of key.</dd></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
</dt><dd> the value if the key is found, NULL otherwise.</dd></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Heimdalx509library from the source code. </p>
