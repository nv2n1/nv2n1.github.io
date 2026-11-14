---
title: "krb5_cc_move(3)"
name: "krb5_cc_move"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_cc_move/"
description: "Heimdal Kerberos 5 credential cache functions –"
---

<h2 class="name">NAME</h2>
<p> Heimdal Kerberos 5 credential cache functions &#8211; </p>
<h3>Functions</h3>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_register</code> (krb5_context context, const krb5_cc_ops *ops, krb5_boolean override)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_resolve</code> (krb5_context context, const char *name, krb5_ccache *id)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_new_unique</code> (krb5_context context, const char *type, const char *hint, krb5_ccache *id)&quot; </p>
<p> KRB5_LIB_FUNCTION const char<br />
 *KRB5_LIB_CALL <code>krb5_cc_get_name</code> (krb5_context context, krb5_ccache id)&quot; </p>
<p> KRB5_LIB_FUNCTION const char<br />
 *KRB5_LIB_CALL <code>krb5_cc_get_type</code> (krb5_context context, krb5_ccache id)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_get_full_name</code> (krb5_context context, krb5_ccache id, char **str)&quot; </p>
<p> KRB5_LIB_FUNCTION const<br />
 krb5_cc_ops *KRB5_LIB_CALL <code>krb5_cc_get_ops</code> (krb5_context context, krb5_ccache id)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_switch</code> (krb5_context context, krb5_ccache id)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_cc_support_switch</code> (krb5_context context, const char *type)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_set_default_name</code> (krb5_context context, const char *name)&quot; </p>
<p> KRB5_LIB_FUNCTION const char<br />
 *KRB5_LIB_CALL <code>krb5_cc_default_name</code> (krb5_context context)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_default</code> (krb5_context context, krb5_ccache *id)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_initialize</code> (krb5_context context, krb5_ccache id, krb5_principal primary_principal)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_destroy</code> (krb5_context context, krb5_ccache id)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_close</code> (krb5_context context, krb5_ccache id)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_store_cred</code> (krb5_context context, krb5_ccache id, krb5_creds *creds)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_retrieve_cred</code> (krb5_context context, krb5_ccache id, krb5_flags whichfields, const krb5_creds *mcreds, krb5_creds *creds)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_get_principal</code> (krb5_context context, krb5_ccache id, krb5_principal *principal)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_start_seq_get</code> (krb5_context context, const krb5_ccache id, krb5_cc_cursor *cursor)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_next_cred</code> (krb5_context context, const krb5_ccache id, krb5_cc_cursor *cursor, krb5_creds *creds)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_end_seq_get</code> (krb5_context context, const krb5_ccache id, krb5_cc_cursor *cursor)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_remove_cred</code> (krb5_context context, krb5_ccache id, krb5_flags which, krb5_creds *cred)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_set_flags</code> (krb5_context context, krb5_ccache id, krb5_flags flags)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_get_flags</code> (krb5_context context, krb5_ccache id, krb5_flags *flags)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_copy_match_f</code> (krb5_context context, const krb5_ccache from, krb5_ccache to, krb5_boolean(*match)(krb5_context, void *, const krb5_creds *), void *matchctx, unsigned int *matched)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_copy_cache</code> (krb5_context context, const krb5_ccache from, krb5_ccache to)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_get_version</code> (krb5_context context, const krb5_ccache id)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_cc_clear_mcred</code> (krb5_creds *mcred)&quot; </p>
<p> KRB5_LIB_FUNCTION const<br />
 krb5_cc_ops *KRB5_LIB_CALL <code>krb5_cc_get_prefix_ops</code> (krb5_context context, const char *prefix)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_cache_get_first</code> (krb5_context context, const char *type, krb5_cc_cache_cursor *cursor)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_cache_next</code> (krb5_context context, krb5_cc_cache_cursor cursor, krb5_ccache *id)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_cache_end_seq_get</code> (krb5_context context, krb5_cc_cache_cursor cursor)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_cache_match</code> (krb5_context context, krb5_principal client, krb5_ccache *id)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_move</code> (krb5_context context, krb5_ccache from, krb5_ccache to)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_is_config_principal</code> (krb5_context context, krb5_const_principal principal)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_set_config</code> (krb5_context context, krb5_ccache id, krb5_const_principal principal, const char *name, krb5_data *data)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_get_config</code> (krb5_context context, krb5_ccache id, krb5_const_principal principal, const char *name, krb5_data *data)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cccol_cursor_new</code> (krb5_context context, krb5_cccol_cursor *cursor)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cccol_cursor_next</code> (krb5_context context, krb5_cccol_cursor cursor, krb5_ccache *cache)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cccol_cursor_free</code> (krb5_context context, krb5_cccol_cursor *cursor)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_last_change_time</code> (krb5_context context, krb5_ccache id, krb5_timestamp *mtime)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cccol_last_change_time</code> (krb5_context context, const char *type, krb5_timestamp *mtime)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_get_friendly_name</code> (krb5_context context, krb5_ccache id, char **name)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_set_friendly_name</code> (krb5_context context, krb5_ccache id, const char *name)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_get_lifetime</code> (krb5_context context, krb5_ccache id, time_t *t)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_set_kdc_offset</code> (krb5_context context, krb5_ccache id, krb5_deltat offset)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_get_kdc_offset</code> (krb5_context context, krb5_ccache id, krb5_deltat *offset)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_gen_new</code> (krb5_context context, const krb5_cc_ops *ops, krb5_ccache *id) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_cc_copy_creds</code> (krb5_context, const krb5_ccache, krb5_ccache)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_free_kdc_rep</code> (krb5_context, krb5_kdc_rep *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_get_validated_creds</code> (krb5_context, krb5_creds *, krb5_principal, krb5_ccache, char *)&quot; </p>
<h3>Variables</h3>
<p> KRB5_LIB_VARIABLE const krb5_cc_ops <code>krb5_acc_ops</code> </p>
<p> KRB5_LIB_VARIABLE const krb5_cc_ops <code>krb5_dcc_ops</code> </p>
<p> KRB5_LIB_VARIABLE const krb5_cc_ops <code>krb5_fcc_ops</code> </p>
<p> KRB5_LIB_VARIABLE const krb5_cc_ops <code>krb5_mcc_ops</code> </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_cache_end_seq_get (krb5_contextcontext, krb5_cc_cache_cursorcursor)</h3>
<p> Destroy the cursor `cursor&#8217;. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_cache_get_first (krb5_contextcontext, const char *type, krb5_cc_cache_cursor *cursor)</h3>
<p> Start iterating over all caches of specified type. See also <code>krb5_cccol_cursor_new()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context<br />
 <i>type</i> optional type to iterate over, if NULL, the default cache is used.<br />
 <i>cursor</i> cursor should be freed with <code>krb5_cc_cache_end_seq_get()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_cache_match (krb5_contextcontext, krb5_principalclient, krb5_ccache *id)</h3>
<p> Search for a matching credential cache that have the `principal&#8217; as the default principal. On success, `id&#8217; needs to be freed with <code>krb5_cc_close()</code> or <code>krb5_cc_destroy()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context<br />
 <i>client</i> The principal to search for<br />
 <i>id</i> the returned credential cache</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On failure, error code is returned and `id&#8217; is set to NULL.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_cache_next (krb5_contextcontext, krb5_cc_cache_cursorcursor, krb5_ccache *id)</h3>
<p> Retrieve the next cache pointed to by (`cursor&#8217;) in `id&#8217; and advance `cursor&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context<br />
 <i>cursor</i> the iterator cursor, returned by <code>krb5_cc_cache_get_first()</code><br />
 <i>id</i> next ccache</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return 0 or an error code. Returns KRB5_CC_END when the end of caches is reached, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_cc_clear_mcred (krb5_creds *mcred)</h3>
<p> Clear `mcreds&#8217; so it can be used with krb5_cc_retrieve_cred</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_close (krb5_contextcontext, krb5_ccacheid)</h3>
<p> Stop using the ccache `id&#8217; and free the related resources. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_copy_cache (krb5_contextcontext, const krb5_ccachefrom, krb5_ccacheto)</h3>
<p> Just like <code>krb5_cc_copy_match_f()</code>, but copy everything. </p>
<p> @</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_copy_creds (krb5_contextcontext, const krb5_ccachefrom, krb5_ccacheto)</h3>
<p> MIT compat glue</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_copy_match_f (krb5_contextcontext, const krb5_ccachefrom, krb5_ccacheto, krb5_boolean(*)(krb5_context, void *, const krb5_creds *)match, void *matchctx, unsigned int *matched)</h3>
<p> Copy the contents of `from&#8217; to `to&#8217; if the given match function return true. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>from</i> the cache to copy data from.<br />
 <i>to</i> the cache to copy data to.<br />
 <i>match</i> a match function that should return TRUE if cred argument should be copied, if NULL, all credentials are copied.<br />
 <i>matchctx</i> context passed to match function.<br />
 <i>matched</i> set to true if there was a credential that matched, may be NULL.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_default (krb5_contextcontext, krb5_ccache *id)</h3>
<p> Open the default ccache in `id&#8217;. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION const char *KRB5_LIB_CALL krb5_cc_default_name (krb5_contextcontext)</h3>
<p> Return a pointer to a context static string containing the default ccache name. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> String to the default credential cache name.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_destroy (krb5_contextcontext, krb5_ccacheid)</h3>
<p> Remove the ccache `id&#8217;. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_end_seq_get (krb5_contextcontext, const krb5_ccacheid, krb5_cc_cursor *cursor)</h3>
<p> Destroy the cursor `cursor&#8217;.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_gen_new (krb5_contextcontext, const krb5_cc_ops *ops, krb5_ccache *id)</h3>
<p> Generate a new ccache of type `ops&#8217; in `id&#8217;. </p>
<p> Deprecated: use <code>krb5_cc_new_unique()</code> instead. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_get_config (krb5_contextcontext, krb5_ccacheid, krb5_const_principalprincipal, const char *name, krb5_data *data)</h3>
<p> Get some configuration for the credential cache in the cache. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>id</i> the credential cache to store the data for<br />
 <i>principal</i> configuration for a specific principal, if NULL, global for the whole cache.<br />
 <i>name</i> name under which the configuraion is stored.<br />
 <i>data</i> data to fetched, free with <code>krb5_data_free()</code></dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_get_flags (krb5_contextcontext, krb5_ccacheid, krb5_flags *flags)</h3>
<p> Get the flags of `id&#8217;, store them in `flags&#8217;.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_get_friendly_name (krb5_contextcontext, krb5_ccacheid, char **name)</h3>
<p> Return a friendly name on credential cache. Free the result with krb5_xfree(). </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_get_full_name (krb5_contextcontext, krb5_ccacheid, char **str)</h3>
<p> Return the complete resolvable name the cache </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>id</i> return pointer to a found credential cache<br />
 <i>str</i> the returned name of a credential cache, free with krb5_xfree()</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 or an error (and then *str is set to NULL).</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_get_kdc_offset (krb5_contextcontext, krb5_ccacheid, krb5_deltat *offset)</h3>
<p> Get the time offset betwen the client and the KDC </p>
<p> If the backend doesn&#8217;t support KDC offset, use the context global setting. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>id</i> a credential cache<br />
 <i>offset</i> the offset in seconds</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_get_lifetime (krb5_contextcontext, krb5_ccacheid, time_t *t)</h3>
<p> Get the lifetime of the initial ticket in the cache </p>
<p> Get the lifetime of the initial ticket in the cache, if the initial ticket was not found, the error code KRB5_CC_END is returned. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>id</i> a credential cache<br />
 <i>t</i> the relative lifetime of the initial ticket</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<p> If we find a krbtgt in the cache, use that as the lifespan. </p>
<p> If there was no krbtgt, use the shortest lifetime of service tickets that have yet to expire. If all credentials are expired, <code>krb5_cc_get_lifetime()</code> will fail.</p>
<h3>KRB5_LIB_FUNCTION const char *KRB5_LIB_CALL krb5_cc_get_name (krb5_contextcontext, krb5_ccacheid)</h3>
<p> Return the name of the ccache `id&#8217;</p>
<h3>KRB5_LIB_FUNCTION const krb5_cc_ops *KRB5_LIB_CALL krb5_cc_get_ops (krb5_contextcontext, krb5_ccacheid)</h3>
<p> Return krb5_cc_ops of a the ccache `id&#8217;.</p>
<h3>KRB5_LIB_FUNCTION const krb5_cc_ops *KRB5_LIB_CALL krb5_cc_get_prefix_ops (krb5_contextcontext, const char *prefix)</h3>
<p> Get the cc ops that is registered in `context&#8217; to handle the prefix. prefix can be a complete credential cache name or a prefix, the function will only use part up to the first colon (:) if there is one. If prefix the argument is NULL, the default ccache implemtation is returned. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns NULL if ops not found.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_get_principal (krb5_contextcontext, krb5_ccacheid, krb5_principal *principal)</h3>
<p> Return the principal of `id&#8217; in `principal&#8217;. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION const char *KRB5_LIB_CALL krb5_cc_get_type (krb5_contextcontext, krb5_ccacheid)</h3>
<p> Return the type of the ccache `id&#8217;.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_get_version (krb5_contextcontext, const krb5_ccacheid)</h3>
<p> Return the version of `id&#8217;.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_initialize (krb5_contextcontext, krb5_ccacheid, krb5_principalprimary_principal)</h3>
<p> Create a new ccache in `id&#8217; for `primary_principal&#8217;. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_last_change_time (krb5_contextcontext, krb5_ccacheid, krb5_timestamp *mtime)</h3>
<p> Return the last time the credential cache was modified. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context<br />
 <i>id</i> The credential cache to probe<br />
 <i>mtime</i> the last modification time, set to 0 on error.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return 0 or and error. See <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_move (krb5_contextcontext, krb5_ccachefrom, krb5_ccacheto)</h3>
<p> Move the content from one credential cache to another. The operation is an atomic switch. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>from</i> the credential cache to move the content from<br />
 <i>to</i> the credential cache to move the content to</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On sucess, from is freed. On failure, error code is returned and from and to are both still allocated, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_new_unique (krb5_contextcontext, const char *type, const char *hint, krb5_ccache *id)</h3>
<p> Generates a new unique ccache of type in `id&#8217;. If `type&#8217; is NULL, the library chooses the default credential cache type. The supplied `hint&#8217; (that can be NULL) is a string that the credential cache type can use to base the name of the credential on, this is to make it easier for the user to differentiate the credentials. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_next_cred (krb5_contextcontext, const krb5_ccacheid, krb5_cc_cursor *cursor, krb5_creds *creds)</h3>
<p> Retrieve the next cred pointed to by (`id&#8217;, `cursor&#8217;) in `creds&#8217; and advance `cursor&#8217;. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_register (krb5_contextcontext, const krb5_cc_ops *ops, krb5_booleanoverride)</h3>
<p> Add a new ccache type with operations `ops&#8217;, overwriting any existing one if `override&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>ops</i> type of plugin symbol<br />
 <i>override</i> flag to select if the registration is to overide an existing ops with the same name.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_remove_cred (krb5_contextcontext, krb5_ccacheid, krb5_flagswhich, krb5_creds *cred)</h3>
<p> Remove the credential identified by `cred&#8217;, `which&#8217; from `id&#8217;.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_resolve (krb5_contextcontext, const char *name, krb5_ccache *id)</h3>
<p> Find and allocate a ccache in `id&#8217; from the specification in `residual&#8217;. If the ccache name doesn&#8217;t contain any colon, interpret it as a file name. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context.<br />
 <i>name</i> string name of a credential cache.<br />
 <i>id</i> return pointer to a found credential cache.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return 0 or an error code. In case of an error, id is set to NULL, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_retrieve_cred (krb5_contextcontext, krb5_ccacheid, krb5_flagswhichfields, const krb5_creds *mcreds, krb5_creds *creds)</h3>
<p> Retrieve the credential identified by `mcreds&#8217; (and `whichfields&#8217;) from `id&#8217; in `creds&#8217;. &#8216;creds&#8217; must be free by the caller using krb5_free_cred_contents. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context<br />
 <i>id</i> a Kerberos 5 credential cache<br />
 <i>whichfields</i> what fields to use for matching credentials, same flags as whichfields in <code>krb5_compare_creds()</code><br />
 <i>mcreds</i> template credential to use for comparing<br />
 <i>creds</i> returned credential, free with <code>krb5_free_cred_contents()</code></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_set_config (krb5_contextcontext, krb5_ccacheid, krb5_const_principalprincipal, const char *name, krb5_data *data)</h3>
<p> Store some configuration for the credential cache in the cache. Existing configuration under the same name is over-written. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>id</i> the credential cache to store the data for<br />
 <i>principal</i> configuration for a specific principal, if NULL, global for the whole cache.<br />
 <i>name</i> name under which the configuraion is stored.<br />
 <i>data</i> data to store, if NULL, configure is removed.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_set_default_name (krb5_contextcontext, const char *name)</h3>
<p> Set the default cc name for `context&#8217; to `name&#8217;.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_set_flags (krb5_contextcontext, krb5_ccacheid, krb5_flagsflags)</h3>
<p> Set the flags of `id&#8217; to `flags&#8217;.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_set_friendly_name (krb5_contextcontext, krb5_ccacheid, const char *name)</h3>
<p> Set the friendly name on credential cache. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_set_kdc_offset (krb5_contextcontext, krb5_ccacheid, krb5_deltatoffset)</h3>
<p> Set the time offset betwen the client and the KDC </p>
<p> If the backend doesn&#8217;t support KDC offset, use the context global setting. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>id</i> a credential cache<br />
 <i>offset</i> the offset in seconds</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_start_seq_get (krb5_contextcontext, const krb5_ccacheid, krb5_cc_cursor *cursor)</h3>
<p> Start iterating over `id&#8217;, `cursor&#8217; is initialized to the beginning. Caller must free the cursor with <code>krb5_cc_end_seq_get()</code>. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_store_cred (krb5_contextcontext, krb5_ccacheid, krb5_creds *creds)</h3>
<p> Store `creds&#8217; in the ccache `id&#8217;. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_cc_support_switch (krb5_contextcontext, const char *type)</h3>
<p> Return true if the default credential cache support switch</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_switch (krb5_contextcontext, krb5_ccacheid)</h3>
<p> Switch the default default credential cache for a specific credcache type (and name for some implementations). </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cccol_cursor_free (krb5_contextcontext, krb5_cccol_cursor *cursor)</h3>
<p> End an iteration and free all resources, can be done before end is reached. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context<br />
 <i>cursor</i> the iteration cursor to be freed.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return 0 or and error, KRB5_CC_END is returned at the end of iteration. See <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cccol_cursor_new (krb5_contextcontext, krb5_cccol_cursor *cursor)</h3>
<p> Get a new cache interation cursor that will interate over all credentials caches independent of type. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>cursor</i> passed into <code>krb5_cccol_cursor_next()</code> and free with <code>krb5_cccol_cursor_free()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 or and error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cccol_cursor_next (krb5_contextcontext, krb5_cccol_cursorcursor, krb5_ccache *cache)</h3>
<p> Get next credential cache from the iteration. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context<br />
 <i>cursor</i> the iteration cursor<br />
 <i>cache</i> the returned cursor, pointer is set to NULL on failure and a cache on success. The returned cache needs to be freed with <code>krb5_cc_close()</code> or destroyed with <code>krb5_cc_destroy()</code>. MIT Kerberos behavies slightly diffrent and sets cache to NULL when all caches are iterated over and return 0.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return 0 or and error, KRB5_CC_END is returned at the end of iteration. See <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cccol_last_change_time (krb5_contextcontext, const char *type, krb5_timestamp *mtime)</h3>
<p> Return the last modfication time for a cache collection. The query can be limited to a specific cache type. If the function return 0 and mtime is 0, there was no credentials in the caches. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context<br />
 <i>type</i> The credential cache to probe, if NULL, all type are traversed.<br />
 <i>mtime</i> the last modification time, set to 0 on error.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return 0 or and error. See <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_free_kdc_rep (krb5_context, krb5_kdc_rep *)</h3>
<p> Variable containing the FILE based credential cache implemention.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_get_validated_creds (krb5_contextcontext, krb5_creds *creds, krb5_principalclient, krb5_ccacheccache, char *service)</h3>
<p> Validate the newly fetch credential, see also krb5_verify_init_creds(). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Kerberos 5 context<br />
 <i>creds</i> the credentials to verify<br />
 <i>client</i> the client name to match up<br />
 <i>ccache</i> the credential cache to use<br />
 <i>service</i> a service name to use, used with <code>krb5_sname_to_principal()</code> to build a hostname to use to verify.</dl>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_is_config_principal (krb5_contextcontext, krb5_const_principalprincipal)</h3>
<p> Return TRUE (non zero) if the principal is a configuration principal (generated part of <code>krb5_cc_set_config()</code>). Returns FALSE (zero) if not a configuration principal. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>principal</i> principal to check if it a configuration principal</dl>
<h2>Variable Documentation</h2>
<h3>KRB5_LIB_VARIABLE const krb5_cc_ops krb5_acc_ops</h3>
<p> <code>Initial value:</code> </p>
<pre><code>
= {
    KRB5_CC_OPS_VERSION,
    "API",
    acc_get_name,
    acc_resolve,
    acc_gen_new,
    acc_initialize,
    acc_destroy,
    acc_close,
    acc_store_cred,
    NULL,
    acc_get_principal,
    acc_get_first,
    acc_get_next,
    acc_end_get,
    acc_remove_cred,
    acc_set_flags,
    acc_get_version,
    acc_get_cache_first,
    acc_get_cache_next,
    acc_end_cache_get,
    acc_move,
    acc_get_default_name,
    acc_set_default,
    acc_lastchange,
    NULL,
    NULL,
}
</code></pre>
<p> Variable containing the API based credential cache implemention.</p>
<h3>KRB5_LIB_VARIABLE const krb5_cc_ops krb5_dcc_ops</h3>
<p> <code>Initial value:</code> </p>
<pre>
= {
    KRB5_CC_OPS_VERSION,
    &quot;DIR&quot;,
    dcc_get_name,
    dcc_resolve,
    dcc_gen_new,
    dcc_initialize,
    dcc_destroy,
    dcc_close,
    dcc_store_cred,
    NULL, 
    dcc_get_principal,
    dcc_get_first,
    dcc_get_next,
    dcc_end_get,
    dcc_remove_cred,
    dcc_set_flags,
    dcc_get_version,
    dcc_get_cache_first,
    dcc_get_cache_next,
    dcc_end_cache_get,
    dcc_move,
    dcc_get_default_name,
    dcc_set_default,
    dcc_lastchange,
    dcc_set_kdc_offset,
    dcc_get_kdc_offset
}
</pre>
<p> Variable containing the DIR based credential cache implemention.</p>
<h3>KRB5_LIB_VARIABLE const krb5_cc_ops krb5_fcc_ops</h3>
<p> <code>Initial value:</code> </p>
<p>= {<br />
    KRB5_CC_OPS_VERSION,<br />
    &#8220;FILE&#8221;,<br />
    fcc_get_name,<br />
    fcc_resolve,<br />
    fcc_gen_new,<br />
    fcc_initialize,<br />
    fcc_destroy,<br />
    fcc_close,<br />
    fcc_store_cred,<br />
    NULL,<br />
    fcc_get_principal,<br />
    fcc_get_first,<br />
    fcc_get_next,<br />
    fcc_end_get,<br />
    fcc_remove_cred,<br />
    fcc_set_flags,<br />
    fcc_get_version,<br />
    fcc_get_cache_first,<br />
    fcc_get_cache_next,<br />
    fcc_end_cache_get,<br />
    fcc_move,<br />
    fcc_get_default_name,<br />
    NULL,<br />
    fcc_lastchange,<br />
    fcc_set_kdc_offset,<br />
    fcc_get_kdc_offset}<br />
 Variable containing the FILE based credential cache implemention.</p>
<h3>KRB5_LIB_VARIABLE const krb5_cc_ops krb5_mcc_ops</h3>
<p> <code>Initial value:</code> </p>
<pre><code>
= {
    KRB5_CC_OPS_VERSION,
    "MEMORY",
    mcc_get_name,
    mcc_resolve,
    mcc_gen_new,
    mcc_initialize,
    mcc_destroy,
    mcc_close,
    mcc_store_cred,
    NULL,
    mcc_get_principal,
    mcc_get_first,
    mcc_get_next,
    mcc_end_get,
    mcc_remove_cred,
    mcc_set_flags,
    NULL,
    mcc_get_cache_first,
    mcc_get_cache_next,
    mcc_end_cache_get,
    mcc_move,
    mcc_default_name,
    NULL,
    mcc_lastchange,
    mcc_set_kdc_offset,
    mcc_get_kdc_offset}
</code></pre>
<p> Variable containing the MEMORY based credential cache implemention.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for HeimdalKerberos5library from the source code. </p>
<h2>Index</h2>
