---
title: "any-h(3)"
name: "any-h"
section: "3"
letter: "a"
url: "/docs/linux/man/3-any-h/"
description: "any.h – Opaque handler to pass different types of values to the API."
---

<p>any.h &#8211; Opaque handler to pass different types of values to the API.</p>
<h2>Synopsis</h2>
<p>#include &#8216;dmlite/common/config.h&#8217;<br />
 #include &lt;stddef.h&gt;<br />
 #include &lt;stdint.h&gt; </p>
<h3>Typedefs</h3>
<p>typedef struct <code>dmlite_any</code> <code>dmlite_any</code><br />
 <i>Used to pass configuration values. </i><br />
 typedef struct <code>dmlite_any_dict</code> <code>dmlite_any_dict</code><br />
 <i>Handles key-&gt;value pairs. </i></p>
<h3>Functions</h3>
<p><code>dmlite_any</code> * <code>dmlite_any_new_string</code> (const char *str)<br />
 <i>Creates a new dmlite_any. </i><br />
 <code>dmlite_any</code> * <code>dmlite_any_new_long</code> (long l)<br />
 <i>Creates a new dmlite_any. </i><br />
 <code>dmlite_any</code> * <code>dmlite_any_new_s64</code> (int64_t i)<br />
 <i>Creates a new dmlite_any from an int64_t type. </i><br />
 <code>dmlite_any</code> * <code>dmlite_any_new_u64</code> (uint64_t i)<br />
 <i>Creates a new dmlite_any from an uint64_t type. </i><br />
 <code>dmlite_any</code> * <code>dmlite_any_new_string_array</code> (unsigned n, const char **strv)<br />
 <i>Creates a new dmlite_any. </i><br />
 <code>dmlite_any</code> * <code>dmlite_any_new_long_array</code> (unsigned n, long *lv)<br />
 <i>Creates a new dmlite_any. </i><br />
 void <code>dmlite_any_free</code> (<code>dmlite_any</code> *any)<br />
 <i>Frees a dmlite_any. </i><br />
 void <code>dmlite_any_to_string</code> (const <code>dmlite_any</code> *any, char *buffer, size_t bsize)<br />
 <i>Gets the string interpretation of the dmlite_any. </i><br />
 long <code>dmlite_any_to_long</code> (const <code>dmlite_any</code> *any)<br />
 <i>Returns the long interpretation of they dmlite_any. </i><br />
 int64_t <code>dmlite_any_to_s64</code> (const <code>dmlite_any</code> *any)<br />
 <i>Returns the int64_t interpretation of they dmlite_any. </i><br />
 uint64_t <code>dmlite_any_to_u64</code> (const <code>dmlite_any</code> *any)<br />
 <i>Returns the uint64_t interpretation of they dmlite_any. </i><br />
 <code>dmlite_any_dict</code> * <code>dmlite_any_dict_new</code> ()<br />
 <i>Created a new generic dictionary. </i><br />
 <code>dmlite_any_dict</code> * <code>dmlite_any_dict_copy</code> (const <code>dmlite_any_dict</code> *dict)<br />
 <i>Make a copy of the dictionary. </i><br />
 void <code>dmlite_any_dict_free</code> (<code>dmlite_any_dict</code> *d)<br />
 <i>Frees a dmlite_any_dict. </i><br />
 void <code>dmlite_any_dict_clear</code> (<code>dmlite_any_dict</code> *d)<br />
 <i>Clears the dictionary. </i><br />
 void <code>dmlite_any_dict_insert</code> (<code>dmlite_any_dict</code> *d, const char *k, const <code>dmlite_any</code> *v)<br />
 <i>Insert a new dmlite_any value into the dictionary. </i><br />
 unsigned long <code>dmlite_any_dict_count</code> (const <code>dmlite_any_dict</code> *d)<br />
 <i>Returns how many elements there are in a specific dictionary. </i><br />
 <code>dmlite_any</code> * <code>dmlite_any_dict_get</code> (const <code>dmlite_any_dict</code> *d, const char *k)<br />
 <i>Returns the value associated with the key k. </i><br />
 void <code>dmlite_any_dict_erase</code> (<code>dmlite_any_dict</code> *d, const char *k)<br />
 <i>Removes a key-value from the dictionary. </i><br />
 char * <code>dmlite_any_dict_to_json</code> (const <code>dmlite_any_dict</code> *d, char *buffer, size_t bsize)<br />
 <i>Generates a JSON serialization of the dictionary. </i><br />
 <code>dmlite_any_dict</code> * <code>dmlite_any_dict_from_json</code> (const char *json)<br />
 <i>Populates a dmlite_any_dict from a JSON string. </i><br />
 void <code>dmlite_any_dict_keys</code> (const <code>dmlite_any_dict</code> *d, unsigned *nkeys, char ***keys)<br />
 <i>Puts in keys a pointer to an array of strings with all the available keys in d. </i><br />
 void <code>dmlite_any_dict_keys_free</code> (unsigned n, char **keys)<br />
 <i>Frees an array of strings allocated by dmlite_any_dict_keys. </i></p>
<h2>Detailed Description</h2>
<p>Opaque handler to pass different types of values to the API. </p>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Alejandro Álvarez Ayllon aalvarez [at] cern.ch</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Basically it wraps boost::any and dmlite::Extensible.</dl>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>dmlite_any</code> <code>dmlite_any</code></h3>
<p>Used to pass configuration values.</p>
<h3>typedef struct <code>dmlite_any_dict</code> <code>dmlite_any_dict</code></h3>
<p>Handles key-&gt;value pairs.</p>
<h2>Function Documentation</h2>
<h3>void dmlite_any_dict_clear (<code>dmlite_any_dict</code> *d)</h3>
<p>Clears the dictionary.</p>
<h3><code>dmlite_any_dict</code>* dmlite_any_dict_copy (const <code>dmlite_any_dict</code> *dict)</h3>
<p>Make a copy of the dictionary. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dict</i> The original</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A newly allocated copy of dict.</dl>
<h3>unsigned long dmlite_any_dict_count (const <code>dmlite_any_dict</code> *d)</h3>
<p>Returns how many elements there are in a specific dictionary.</p>
<h3>void dmlite_any_dict_erase (<code>dmlite_any_dict</code> *d, const char *k)</h3>
<p>Removes a key-value from the dictionary. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>d</i> The dictionary.<br />
 <i>k</i> The key to be removed.</dl>
<h3>void dmlite_any_dict_free (<code>dmlite_any_dict</code> *d)</h3>
<p>Frees a dmlite_any_dict.</p>
<h3><code>dmlite_any_dict</code>* dmlite_any_dict_from_json (const char *json)</h3>
<p>Populates a dmlite_any_dict from a JSON string.</p>
<h3><code>dmlite_any</code>* dmlite_any_dict_get (const <code>dmlite_any_dict</code> *d, const char *k)</h3>
<p>Returns the value associated with the key k. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>NULL if not found.</dl>
<h3>void dmlite_any_dict_insert (<code>dmlite_any_dict</code> *d, const char *k, const <code>dmlite_any</code> *v)</h3>
<p>Insert a new dmlite_any value into the dictionary. Replaces if already present. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>d</i> The dictionary.<br />
 <i>k</i> The key.<br />
 <i>v</i> The value.</dl>
<h3>void dmlite_any_dict_keys (const <code>dmlite_any_dict</code> *d, unsigned *nkeys, char ***keys)</h3>
<p>Puts in keys a pointer to an array of strings with all the available keys in d. Use dmlite_any_dict_keys_free to free. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>d</i> The Dictionary.<br />
 <i>nkeys</i> Will be set to the number of stored keys.</dl>
<h3>void dmlite_any_dict_keys_free (unsignedn, char **keys)</h3>
<p>Frees an array of strings allocated by dmlite_any_dict_keys. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>n</i> The number of keys in **keys<br />
 <i>keys</i> The array of keys.</dl>
<h3><code>dmlite_any_dict</code>* dmlite_any_dict_new ()</h3>
<p>Created a new generic dictionary. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A newly allocated dmlite_any_dict.</dl>
<h3>char* dmlite_any_dict_to_json (const <code>dmlite_any_dict</code> *d, char *buffer, size_tbsize)</h3>
<p>Generates a JSON serialization of the dictionary. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The same pointer as buffer.</dl>
<h3>void dmlite_any_free (<code>dmlite_any</code> *any)</h3>
<p>Frees a dmlite_any. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>any</i> The dmlite_any to destroy.</dl>
<h3><code>dmlite_any</code>* dmlite_any_new_long (longl)</h3>
<p>Creates a new dmlite_any. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>l</i> The long that will be wrapped.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A newly allocated dmlite_any.</dl>
<h3><code>dmlite_any</code>* dmlite_any_new_long_array (unsignedn, long *lv)</h3>
<p>Creates a new dmlite_any. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>n</i> The number of elements.<br />
 <i>lv</i> The longs that will be wrapped.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A newly allocated dmlite_any.</dl>
<p> <code>Deprecated</code></p>
<dl COMPACT>
<dd>Use dmlite_set_array instead.</dl>
<h3><code>dmlite_any</code>* dmlite_any_new_s64 (int64_ti)</h3>
<p>Creates a new dmlite_any from an int64_t type. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>i</i> The int64_t value.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A newly allocated dmlite_any.</dl>
<h3><code>dmlite_any</code>* dmlite_any_new_string (const char *str)</h3>
<p>Creates a new dmlite_any. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>str</i> The string that will be wrapped. It is safe to free afterwards.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A newly allocated dmlite_any.</dl>
<h3><code>dmlite_any</code>* dmlite_any_new_string_array (unsignedn, const char **strv)</h3>
<p>Creates a new dmlite_any. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>n</i> The number of elements.<br />
 <i>strv</i> The strings that will be wrapped. It is safe to free afterwards.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A newly allocated dmlite_any.</dl>
<p> <code>Deprecated</code></p>
<dl COMPACT>
<dd>Use dmlite_set_array instead.</dl>
<h3><code>dmlite_any</code>* dmlite_any_new_u64 (uint64_ti)</h3>
<p>Creates a new dmlite_any from an uint64_t type. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>i</i> The uint64_t value.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A newly allocated dmlite_any.</dl>
<h3>long dmlite_any_to_long (const <code>dmlite_any</code> *any)</h3>
<p>Returns the long interpretation of they dmlite_any. Defaults to 0. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>any</i> The dmlite_any to convert.</dl>
<h3>int64_t dmlite_any_to_s64 (const <code>dmlite_any</code> *any)</h3>
<p>Returns the int64_t interpretation of they dmlite_any. Defaults to 0. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>any</i> The dmlite_any to convert.</dl>
<h3>void dmlite_any_to_string (const <code>dmlite_any</code> *any, char *buffer, size_tbsize)</h3>
<p>Gets the string interpretation of the dmlite_any. Defaults to &#8221;. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>any</i> The dmlite_any to convert.<br />
 <i>buffer</i> Where to put the string.<br />
 <i>bsize</i> The size of the buffer.</dl>
<h3>uint64_t dmlite_any_to_u64 (const <code>dmlite_any</code> *any)</h3>
<p>Returns the uint64_t interpretation of they dmlite_any. Defaults to 0. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>any</i> The dmlite_any to convert.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for dmlite from the source code.</p>
