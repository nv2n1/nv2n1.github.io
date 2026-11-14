---
title: "krb5_kt_register(3)"
name: "krb5_kt_register"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_kt_register/"
description: "Heimdal Kerberos 5 keytab handling functions –"
---

<h2 class="name">NAME</h2>
<p> Heimdal Kerberos 5 keytab handling functions &#8211; </p>
<h3>Functions</h3>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_kt_register</code> (krb5_context context, const krb5_kt_ops *ops)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_kt_resolve</code> (krb5_context context, const char *name, krb5_keytab *id)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_kt_default_name</code> (krb5_context context, char *name, size_t namesize)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_kt_default_modify_name</code> (krb5_context context, char *name, size_t namesize)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_kt_default</code> (krb5_context context, krb5_keytab *id)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_kt_read_service_key</code> (krb5_context context, krb5_pointer keyprocarg, krb5_principal principal, krb5_kvno vno, krb5_enctype enctype, krb5_keyblock **key)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_kt_get_type</code> (krb5_context context, krb5_keytab keytab, char *prefix, size_t prefixsize)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_kt_get_name</code> (krb5_context context, krb5_keytab keytab, char *name, size_t namesize)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_kt_get_full_name</code> (krb5_context context, krb5_keytab keytab, char **str)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_kt_close</code> (krb5_context context, krb5_keytab id)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_kt_destroy</code> (krb5_context context, krb5_keytab id)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_kt_compare</code> (krb5_context context, krb5_keytab_entry *entry, krb5_const_principal principal, krb5_kvno vno, krb5_enctype enctype)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_kt_get_entry</code> (krb5_context context, krb5_keytab id, krb5_const_principal principal, krb5_kvno kvno, krb5_enctype enctype, krb5_keytab_entry *entry)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_kt_copy_entry_contents</code> (krb5_context context, const krb5_keytab_entry *in, krb5_keytab_entry *out)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_kt_free_entry</code> (krb5_context context, krb5_keytab_entry *entry)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_kt_start_seq_get</code> (krb5_context context, krb5_keytab id, krb5_kt_cursor *cursor)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_kt_next_entry</code> (krb5_context context, krb5_keytab id, krb5_keytab_entry *entry, krb5_kt_cursor *cursor)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_kt_end_seq_get</code> (krb5_context context, krb5_keytab id, krb5_kt_cursor *cursor)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_kt_add_entry</code> (krb5_context context, krb5_keytab id, krb5_keytab_entry *entry)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_kt_remove_entry</code> (krb5_context context, krb5_keytab id, krb5_keytab_entry *entry)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_kt_have_content</code> (krb5_context context, krb5_keytab id)&quot; </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_kt_add_entry (krb5_contextcontext, krb5_keytabid, krb5_keytab_entry *entry)</h3>
<p> Add the entry in `entry&#8217; to the keytab `id&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>id</i> a keytab.<br />
 <i>entry</i> the entry to add</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_kt_close (krb5_contextcontext, krb5_keytabid)</h3>
<p> Finish using the keytab in `id&#8217;. All resources will be released, even on errors. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>id</i> keytab to close.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_kt_compare (krb5_contextcontext, krb5_keytab_entry *entry, krb5_const_principalprincipal, krb5_kvnovno, krb5_enctypeenctype)</h3>
<p> Compare `entry&#8217; against `principal, vno, enctype&#8217;. Any of `principal, vno, enctype&#8217; might be 0 which acts as a wildcard. Return TRUE if they compare the same, FALSE otherwise. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>entry</i> an entry to match with.<br />
 <i>principal</i> principal to match, NULL matches all principals.<br />
 <i>vno</i> key version to match, 0 matches all key version numbers.<br />
 <i>enctype</i> encryption type to match, 0 matches all encryption types.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return TRUE or match, FALSE if not matched.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_kt_copy_entry_contents (krb5_contextcontext, const krb5_keytab_entry *in, krb5_keytab_entry *out)</h3>
<p> Copy the contents of `in&#8217; into `out&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>in</i> the keytab entry to copy.<br />
 <i>out</i> the copy of the keytab entry, free with <code>krb5_kt_free_entry()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_kt_default (krb5_contextcontext, krb5_keytab *id)</h3>
<p> Set `id&#8217; to the default keytab. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>id</i> the new default keytab.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_kt_default_modify_name (krb5_contextcontext, char *name, size_tnamesize)</h3>
<p> Copy the name of the default modify keytab into `name&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>name</i> buffer where the name will be written<br />
 <i>namesize</i> length of name</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_kt_default_name (krb5_contextcontext, char *name, size_tnamesize)</h3>
<p> copy the name of the default keytab into `name&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>name</i> buffer where the name will be written<br />
 <i>namesize</i> length of name</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_kt_destroy (krb5_contextcontext, krb5_keytabid)</h3>
<p> Destroy (remove) the keytab in `id&#8217;. All resources will be released, even on errors, does the equvalment of <code>krb5_kt_close()</code> on the resources. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>id</i> keytab to destroy.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_kt_end_seq_get (krb5_contextcontext, krb5_keytabid, krb5_kt_cursor *cursor)</h3>
<p> Release all resources associated with `cursor&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>id</i> a keytab.<br />
 <i>cursor</i> the cursor to free.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_kt_free_entry (krb5_contextcontext, krb5_keytab_entry *entry)</h3>
<p> Free the contents of `entry&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>entry</i> the entry to free</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_kt_get_entry (krb5_contextcontext, krb5_keytabid, krb5_const_principalprincipal, krb5_kvnokvno, krb5_enctypeenctype, krb5_keytab_entry *entry)</h3>
<p> Retrieve the keytab entry for `principal, kvno, enctype&#8217; into `entry&#8217; from the keytab `id&#8217;. Matching is done like <code>krb5_kt_compare()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>id</i> a keytab.<br />
 <i>principal</i> principal to match, NULL matches all principals.<br />
 <i>kvno</i> key version to match, 0 matches all key version numbers.<br />
 <i>enctype</i> encryption type to match, 0 matches all encryption types.<br />
 <i>entry</i> the returned entry, free with <code>krb5_kt_free_entry()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_kt_get_full_name (krb5_contextcontext, krb5_keytabkeytab, char **str)</h3>
<p> Retrieve the full name of the keytab `keytab&#8217; and store the name in `str&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>keytab</i> keytab to get name for.<br />
 <i>str</i> the name of the keytab name, usee krb5_xfree() to free the string. On error, *str is set to NULL.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_kt_get_name (krb5_contextcontext, krb5_keytabkeytab, char *name, size_tnamesize)</h3>
<p> Retrieve the name of the keytab `keytab&#8217; into `name&#8217;, `namesize&#8217; </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>keytab</i> the keytab to get the name for.<br />
 <i>name</i> name buffer.<br />
 <i>namesize</i> size of name buffer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_kt_get_type (krb5_contextcontext, krb5_keytabkeytab, char *prefix, size_tprefixsize)</h3>
<p> Return the type of the `keytab&#8217; in the string prefix of length prefixsize&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>keytab</i> the keytab to get the prefix for<br />
 <i>prefix</i> prefix buffer<br />
 <i>prefixsize</i> length of prefix buffer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_kt_have_content (krb5_contextcontext, krb5_keytabid)</h3>
<p> Return true if the keytab exists and have entries </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>id</i> a keytab.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_kt_next_entry (krb5_contextcontext, krb5_keytabid, krb5_keytab_entry *entry, krb5_kt_cursor *cursor)</h3>
<p> Get the next entry from keytab, advance the cursor. On last entry the function will return KRB5_KT_END. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>id</i> a keytab.<br />
 <i>entry</i> the returned entry, free with <code>krb5_kt_free_entry()</code>.<br />
 <i>cursor</i> the cursor of the iteration.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_kt_read_service_key (krb5_contextcontext, krb5_pointerkeyprocarg, krb5_principalprincipal, krb5_kvnovno, krb5_enctypeenctype, krb5_keyblock **key)</h3>
<p> Read the key identified by `(principal, vno, enctype)&#8217; from the keytab in `keyprocarg&#8217; (the default if == NULL) into `*key&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>keyprocarg</i><br />
 <i>principal</i><br />
 <i>vno</i><br />
 <i>enctype</i><br />
 <i>key</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_kt_register (krb5_contextcontext, const krb5_kt_ops *ops)</h3>
<p> Register a new keytab backend. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>ops</i> a backend to register.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_kt_remove_entry (krb5_contextcontext, krb5_keytabid, krb5_keytab_entry *entry)</h3>
<p> Remove an entry from the keytab, matching is done using <code>krb5_kt_compare()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>id</i> a keytab.<br />
 <i>entry</i> the entry to remove</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_kt_resolve (krb5_contextcontext, const char *name, krb5_keytab *id)</h3>
<p> Resolve the keytab name (of the form `type:residual&#8217;) in `name&#8217; into a keytab in `id&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>name</i> name to resolve<br />
 <i>id</i> resulting keytab, free with <code>krb5_kt_close()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_kt_start_seq_get (krb5_contextcontext, krb5_keytabid, krb5_kt_cursor *cursor)</h3>
<p> Set `cursor&#8217; to point at the beginning of `id&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>id</i> a keytab.<br />
 <i>cursor</i> a newly allocated cursor, free with <code>krb5_kt_end_seq_get()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for HeimdalKerberos5library from the source code. </p>
<h2>Index</h2>
