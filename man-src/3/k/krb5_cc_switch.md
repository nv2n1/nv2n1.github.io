---
title: "krb5_cc_switch(3)"
name: "krb5_cc_switch"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_cc_switch/"
---

<h2 class="name">NAME</h2>
 

 Heimdal Kerberos 5 credential cache functions - 

<h3>Functions</h3>

 

 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_register</b> (krb5_context context, const krb5_cc_ops *ops, krb5_boolean override)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_resolve</b> (krb5_context context, const char *name, krb5_ccache *id)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_new_unique</b> (krb5_context context, const char *type, const char *hint, krb5_ccache *id)&quot; 
 
 KRB5_LIB_FUNCTION const char 
 *KRB5_LIB_CALL <b>krb5_cc_get_name</b> (krb5_context context, krb5_ccache id)&quot; 
 
 KRB5_LIB_FUNCTION const char 
 *KRB5_LIB_CALL <b>krb5_cc_get_type</b> (krb5_context context, krb5_ccache id)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_get_full_name</b> (krb5_context context, krb5_ccache id, char **str)&quot; 
 
 KRB5_LIB_FUNCTION const 
 krb5_cc_ops *KRB5_LIB_CALL <b>krb5_cc_get_ops</b> (krb5_context context, krb5_ccache id)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_switch</b> (krb5_context context, krb5_ccache id)&quot; 
 
 KRB5_LIB_FUNCTION krb5_boolean 
 KRB5_LIB_CALL <b>krb5_cc_support_switch</b> (krb5_context context, const char *type)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_set_default_name</b> (krb5_context context, const char *name)&quot; 
 
 KRB5_LIB_FUNCTION const char 
 *KRB5_LIB_CALL <b>krb5_cc_default_name</b> (krb5_context context)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_default</b> (krb5_context context, krb5_ccache *id)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_initialize</b> (krb5_context context, krb5_ccache id, krb5_principal primary_principal)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_destroy</b> (krb5_context context, krb5_ccache id)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_close</b> (krb5_context context, krb5_ccache id)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_store_cred</b> (krb5_context context, krb5_ccache id, krb5_creds *creds)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_retrieve_cred</b> (krb5_context context, krb5_ccache id, krb5_flags whichfields, const krb5_creds *mcreds, krb5_creds *creds)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_get_principal</b> (krb5_context context, krb5_ccache id, krb5_principal *principal)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_start_seq_get</b> (krb5_context context, const krb5_ccache id, krb5_cc_cursor *cursor)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_next_cred</b> (krb5_context context, const krb5_ccache id, krb5_cc_cursor *cursor, krb5_creds *creds)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_end_seq_get</b> (krb5_context context, const krb5_ccache id, krb5_cc_cursor *cursor)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_remove_cred</b> (krb5_context context, krb5_ccache id, krb5_flags which, krb5_creds *cred)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_set_flags</b> (krb5_context context, krb5_ccache id, krb5_flags flags)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_get_flags</b> (krb5_context context, krb5_ccache id, krb5_flags *flags)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_copy_match_f</b> (krb5_context context, const krb5_ccache from, krb5_ccache to, krb5_boolean(*match)(krb5_context, void *, const krb5_creds *), void *matchctx, unsigned int *matched)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_copy_cache</b> (krb5_context context, const krb5_ccache from, krb5_ccache to)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_get_version</b> (krb5_context context, const krb5_ccache id)&quot; 
 
 KRB5_LIB_FUNCTION void 
 KRB5_LIB_CALL <b>krb5_cc_clear_mcred</b> (krb5_creds *mcred)&quot; 
 
 KRB5_LIB_FUNCTION const 
 krb5_cc_ops *KRB5_LIB_CALL <b>krb5_cc_get_prefix_ops</b> (krb5_context context, const char *prefix)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_cache_get_first</b> (krb5_context context, const char *type, krb5_cc_cache_cursor *cursor)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_cache_next</b> (krb5_context context, krb5_cc_cache_cursor cursor, krb5_ccache *id)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_cache_end_seq_get</b> (krb5_context context, krb5_cc_cache_cursor cursor)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_cache_match</b> (krb5_context context, krb5_principal client, krb5_ccache *id)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_move</b> (krb5_context context, krb5_ccache from, krb5_ccache to)&quot; 
 
 KRB5_LIB_FUNCTION krb5_boolean 
 KRB5_LIB_CALL <b>krb5_is_config_principal</b> (krb5_context context, krb5_const_principal principal)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_set_config</b> (krb5_context context, krb5_ccache id, krb5_const_principal principal, const char *name, krb5_data *data)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_get_config</b> (krb5_context context, krb5_ccache id, krb5_const_principal principal, const char *name, krb5_data *data)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cccol_cursor_new</b> (krb5_context context, krb5_cccol_cursor *cursor)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cccol_cursor_next</b> (krb5_context context, krb5_cccol_cursor cursor, krb5_ccache *cache)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cccol_cursor_free</b> (krb5_context context, krb5_cccol_cursor *cursor)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_last_change_time</b> (krb5_context context, krb5_ccache id, krb5_timestamp *mtime)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cccol_last_change_time</b> (krb5_context context, const char *type, krb5_timestamp *mtime)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_get_friendly_name</b> (krb5_context context, krb5_ccache id, char **name)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_set_friendly_name</b> (krb5_context context, krb5_ccache id, const char *name)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_get_lifetime</b> (krb5_context context, krb5_ccache id, time_t *t)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_set_kdc_offset</b> (krb5_context context, krb5_ccache id, krb5_deltat offset)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_get_kdc_offset</b> (krb5_context context, krb5_ccache id, krb5_deltat *offset)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_gen_new</b> (krb5_context context, const krb5_cc_ops *ops, krb5_ccache *id) <b>KRB5_DEPRECATED_FUNCTION</b>('Use X instead')&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_cc_copy_creds</b> (krb5_context, const krb5_ccache, krb5_ccache)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_free_kdc_rep</b> (krb5_context, krb5_kdc_rep *)&quot; 
 
 KRB5_LIB_FUNCTION 
 krb5_error_code KRB5_LIB_CALL <b>krb5_get_validated_creds</b> (krb5_context, krb5_creds *, krb5_principal, krb5_ccache, char *)&quot; 

<h3>Variables</h3>

 

 
 KRB5_LIB_VARIABLE const krb5_cc_ops <b>krb5_acc_ops</b> 
 
 KRB5_LIB_VARIABLE const krb5_cc_ops <b>krb5_dcc_ops</b> 
 
 KRB5_LIB_VARIABLE const krb5_cc_ops <b>krb5_fcc_ops</b> 
 
 KRB5_LIB_VARIABLE const krb5_cc_ops <b>krb5_mcc_ops</b> 

<h2>Detailed Description</h2>

 

 

<h2>Function Documentation</h2>

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_cache_end_seq_get (krb5_contextcontext, krb5_cc_cache_cursorcursor)</h3>

 Destroy the cursor `cursor'. 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return an error code or 0, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_cache_get_first (krb5_contextcontext, const char *type, krb5_cc_cache_cursor *cursor)</h3>

 Start iterating over all caches of specified type. See also <b>krb5_cccol_cursor_new()</b>. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context 
 <i>type</i> optional type to iterate over, if NULL, the default cache is used. 
 <i>cursor</i> cursor should be freed with <b>krb5_cc_cache_end_seq_get()</b>.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return an error code or 0, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_cache_match (krb5_contextcontext, krb5_principalclient, krb5_ccache *id)</h3>

 Search for a matching credential cache that have the `principal' as the default principal. On success, `id' needs to be freed with <b>krb5_cc_close()</b> or <b>krb5_cc_destroy()</b>. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context 
 <i>client</i> The principal to search for 
 <i>id</i> the returned credential cache</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> On failure, error code is returned and `id' is set to NULL.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_cache_next (krb5_contextcontext, krb5_cc_cache_cursorcursor, krb5_ccache *id)</h3>

 Retrieve the next cache pointed to by (`cursor') in `id' and advance `cursor'. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context 
 <i>cursor</i> the iterator cursor, returned by <b>krb5_cc_cache_get_first()</b> 
 <i>id</i> next ccache</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return 0 or an error code. Returns KRB5_CC_END when the end of caches is reached, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_cc_clear_mcred (krb5_creds *mcred)</h3>

 Clear `mcreds' so it can be used with krb5_cc_retrieve_cred

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_close (krb5_contextcontext, krb5_ccacheid)</h3>

 Stop using the ccache `id' and free the related resources. 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return an error code or 0, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_copy_cache (krb5_contextcontext, const krb5_ccachefrom, krb5_ccacheto)</h3>

 Just like <b>krb5_cc_copy_match_f()</b>, but copy everything. 

 @

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_copy_creds (krb5_contextcontext, const krb5_ccachefrom, krb5_ccacheto)</h3>

 MIT compat glue

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_copy_match_f (krb5_contextcontext, const krb5_ccachefrom, krb5_ccacheto, krb5_boolean(*)(krb5_context, void *, const krb5_creds *)match, void *matchctx, unsigned int *matched)</h3>

 Copy the contents of `from' to `to' if the given match function return true. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context. 
 <i>from</i> the cache to copy data from. 
 <i>to</i> the cache to copy data to. 
 <i>match</i> a match function that should return TRUE if cred argument should be copied, if NULL, all credentials are copied. 
 <i>matchctx</i> context passed to match function. 
 <i>matched</i> set to true if there was a credential that matched, may be NULL.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return an error code or 0, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_default (krb5_contextcontext, krb5_ccache *id)</h3>

 Open the default ccache in `id'. 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return an error code or 0, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION const char *KRB5_LIB_CALL krb5_cc_default_name (krb5_contextcontext)</h3>

 Return a pointer to a context static string containing the default ccache name. 

 <b>Returns:</b>
<dl>
<dt>
<dd> String to the default credential cache name.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_destroy (krb5_contextcontext, krb5_ccacheid)</h3>

 Remove the ccache `id'. 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return an error code or 0, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_end_seq_get (krb5_contextcontext, const krb5_ccacheid, krb5_cc_cursor *cursor)</h3>

 Destroy the cursor `cursor'.

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_gen_new (krb5_contextcontext, const krb5_cc_ops *ops, krb5_ccache *id)</h3>

 Generate a new ccache of type `ops' in `id'. 

 Deprecated: use <b>krb5_cc_new_unique()</b> instead. 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return an error code or 0, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_get_config (krb5_contextcontext, krb5_ccacheid, krb5_const_principalprincipal, const char *name, krb5_data *data)</h3>

 Get some configuration for the credential cache in the cache. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> a Keberos context 
 <i>id</i> the credential cache to store the data for 
 <i>principal</i> configuration for a specific principal, if NULL, global for the whole cache. 
 <i>name</i> name under which the configuraion is stored. 
 <i>data</i> data to fetched, free with <b>krb5_data_free()</b></dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_get_flags (krb5_contextcontext, krb5_ccacheid, krb5_flags *flags)</h3>

 Get the flags of `id', store them in `flags'.

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_get_friendly_name (krb5_contextcontext, krb5_ccacheid, char **name)</h3>

 Return a friendly name on credential cache. Free the result with krb5_xfree(). 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return an error code or 0, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_get_full_name (krb5_contextcontext, krb5_ccacheid, char **str)</h3>

 Return the complete resolvable name the cache 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> a Keberos context 
 <i>id</i> return pointer to a found credential cache 
 <i>str</i> the returned name of a credential cache, free with krb5_xfree()</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> Returns 0 or an error (and then *str is set to NULL).</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_get_kdc_offset (krb5_contextcontext, krb5_ccacheid, krb5_deltat *offset)</h3>

 Get the time offset betwen the client and the KDC 

 If the backend doesn't support KDC offset, use the context global setting. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context. 
 <i>id</i> a credential cache 
 <i>offset</i> the offset in seconds</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return an error code or 0, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_get_lifetime (krb5_contextcontext, krb5_ccacheid, time_t *t)</h3>

 Get the lifetime of the initial ticket in the cache 

 Get the lifetime of the initial ticket in the cache, if the initial ticket was not found, the error code KRB5_CC_END is returned. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context. 
 <i>id</i> a credential cache 
 <i>t</i> the relative lifetime of the initial ticket</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return an error code or 0, see <b>krb5_get_error_message()</b>.</dl>
 

 If we find a krbtgt in the cache, use that as the lifespan. 

 If there was no krbtgt, use the shortest lifetime of service tickets that have yet to expire. If all credentials are expired, <b>krb5_cc_get_lifetime()</b> will fail.

<h3>KRB5_LIB_FUNCTION const char *KRB5_LIB_CALL krb5_cc_get_name (krb5_contextcontext, krb5_ccacheid)</h3>

 Return the name of the ccache `id'

<h3>KRB5_LIB_FUNCTION const krb5_cc_ops *KRB5_LIB_CALL krb5_cc_get_ops (krb5_contextcontext, krb5_ccacheid)</h3>

 Return krb5_cc_ops of a the ccache `id'.

<h3>KRB5_LIB_FUNCTION const krb5_cc_ops *KRB5_LIB_CALL krb5_cc_get_prefix_ops (krb5_contextcontext, const char *prefix)</h3>

 Get the cc ops that is registered in `context' to handle the prefix. prefix can be a complete credential cache name or a prefix, the function will only use part up to the first colon (:) if there is one. If prefix the argument is NULL, the default ccache implemtation is returned. 

 <b>Returns:</b>
<dl>
<dt>
<dd> Returns NULL if ops not found.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_get_principal (krb5_contextcontext, krb5_ccacheid, krb5_principal *principal)</h3>

 Return the principal of `id' in `principal'. 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return an error code or 0, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION const char *KRB5_LIB_CALL krb5_cc_get_type (krb5_contextcontext, krb5_ccacheid)</h3>

 Return the type of the ccache `id'.

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_get_version (krb5_contextcontext, const krb5_ccacheid)</h3>

 Return the version of `id'.

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_initialize (krb5_contextcontext, krb5_ccacheid, krb5_principalprimary_principal)</h3>

 Create a new ccache in `id' for `primary_principal'. 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return an error code or 0, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_last_change_time (krb5_contextcontext, krb5_ccacheid, krb5_timestamp *mtime)</h3>

 Return the last time the credential cache was modified. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context 
 <i>id</i> The credential cache to probe 
 <i>mtime</i> the last modification time, set to 0 on error.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return 0 or and error. See <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_move (krb5_contextcontext, krb5_ccachefrom, krb5_ccacheto)</h3>

 Move the content from one credential cache to another. The operation is an atomic switch. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> a Keberos context 
 <i>from</i> the credential cache to move the content from 
 <i>to</i> the credential cache to move the content to</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> On sucess, from is freed. On failure, error code is returned and from and to are both still allocated, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_new_unique (krb5_contextcontext, const char *type, const char *hint, krb5_ccache *id)</h3>

 Generates a new unique ccache of type in `id'. If `type' is NULL, the library chooses the default credential cache type. The supplied `hint' (that can be NULL) is a string that the credential cache type can use to base the name of the credential on, this is to make it easier for the user to differentiate the credentials. 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return an error code or 0, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_next_cred (krb5_contextcontext, const krb5_ccacheid, krb5_cc_cursor *cursor, krb5_creds *creds)</h3>

 Retrieve the next cred pointed to by (`id', `cursor') in `creds' and advance `cursor'. 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return an error code or 0, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_register (krb5_contextcontext, const krb5_cc_ops *ops, krb5_booleanoverride)</h3>

 Add a new ccache type with operations `ops', overwriting any existing one if `override'. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> a Keberos context 
 <i>ops</i> type of plugin symbol 
 <i>override</i> flag to select if the registration is to overide an existing ops with the same name.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return an error code or 0, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_remove_cred (krb5_contextcontext, krb5_ccacheid, krb5_flagswhich, krb5_creds *cred)</h3>

 Remove the credential identified by `cred', `which' from `id'.

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_resolve (krb5_contextcontext, const char *name, krb5_ccache *id)</h3>

 Find and allocate a ccache in `id' from the specification in `residual'. If the ccache name doesn't contain any colon, interpret it as a file name. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> a Keberos context. 
 <i>name</i> string name of a credential cache. 
 <i>id</i> return pointer to a found credential cache.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return 0 or an error code. In case of an error, id is set to NULL, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_retrieve_cred (krb5_contextcontext, krb5_ccacheid, krb5_flagswhichfields, const krb5_creds *mcreds, krb5_creds *creds)</h3>

 Retrieve the credential identified by `mcreds' (and `whichfields') from `id' in `creds'. 'creds' must be free by the caller using krb5_free_cred_contents. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context 
 <i>id</i> a Kerberos 5 credential cache 
 <i>whichfields</i> what fields to use for matching credentials, same flags as whichfields in <b>krb5_compare_creds()</b> 
 <i>mcreds</i> template credential to use for comparing 
 <i>creds</i> returned credential, free with <b>krb5_free_cred_contents()</b></dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return an error code or 0, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_set_config (krb5_contextcontext, krb5_ccacheid, krb5_const_principalprincipal, const char *name, krb5_data *data)</h3>

 Store some configuration for the credential cache in the cache. Existing configuration under the same name is over-written. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> a Keberos context 
 <i>id</i> the credential cache to store the data for 
 <i>principal</i> configuration for a specific principal, if NULL, global for the whole cache. 
 <i>name</i> name under which the configuraion is stored. 
 <i>data</i> data to store, if NULL, configure is removed.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_set_default_name (krb5_contextcontext, const char *name)</h3>

 Set the default cc name for `context' to `name'.

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_set_flags (krb5_contextcontext, krb5_ccacheid, krb5_flagsflags)</h3>

 Set the flags of `id' to `flags'.

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_set_friendly_name (krb5_contextcontext, krb5_ccacheid, const char *name)</h3>

 Set the friendly name on credential cache. 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return an error code or 0, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_set_kdc_offset (krb5_contextcontext, krb5_ccacheid, krb5_deltatoffset)</h3>

 Set the time offset betwen the client and the KDC 

 If the backend doesn't support KDC offset, use the context global setting. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context. 
 <i>id</i> a credential cache 
 <i>offset</i> the offset in seconds</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return an error code or 0, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_start_seq_get (krb5_contextcontext, const krb5_ccacheid, krb5_cc_cursor *cursor)</h3>

 Start iterating over `id', `cursor' is initialized to the beginning. Caller must free the cursor with <b>krb5_cc_end_seq_get()</b>. 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return an error code or 0, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_store_cred (krb5_contextcontext, krb5_ccacheid, krb5_creds *creds)</h3>

 Store `creds' in the ccache `id'. 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return an error code or 0, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_cc_support_switch (krb5_contextcontext, const char *type)</h3>

 Return true if the default credential cache support switch

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cc_switch (krb5_contextcontext, krb5_ccacheid)</h3>

 Switch the default default credential cache for a specific credcache type (and name for some implementations). 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return an error code or 0, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cccol_cursor_free (krb5_contextcontext, krb5_cccol_cursor *cursor)</h3>

 End an iteration and free all resources, can be done before end is reached. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context 
 <i>cursor</i> the iteration cursor to be freed.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return 0 or and error, KRB5_CC_END is returned at the end of iteration. See <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cccol_cursor_new (krb5_contextcontext, krb5_cccol_cursor *cursor)</h3>

 Get a new cache interation cursor that will interate over all credentials caches independent of type. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> a Keberos context 
 <i>cursor</i> passed into <b>krb5_cccol_cursor_next()</b> and free with <b>krb5_cccol_cursor_free()</b>.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> Returns 0 or and error code, see <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cccol_cursor_next (krb5_contextcontext, krb5_cccol_cursorcursor, krb5_ccache *cache)</h3>

 Get next credential cache from the iteration. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context 
 <i>cursor</i> the iteration cursor 
 <i>cache</i> the returned cursor, pointer is set to NULL on failure and a cache on success. The returned cache needs to be freed with <b>krb5_cc_close()</b> or destroyed with <b>krb5_cc_destroy()</b>. MIT Kerberos behavies slightly diffrent and sets cache to NULL when all caches are iterated over and return 0.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return 0 or and error, KRB5_CC_END is returned at the end of iteration. See <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_cccol_last_change_time (krb5_contextcontext, const char *type, krb5_timestamp *mtime)</h3>

 Return the last modfication time for a cache collection. The query can be limited to a specific cache type. If the function return 0 and mtime is 0, there was no credentials in the caches. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context 
 <i>type</i> The credential cache to probe, if NULL, all type are traversed. 
 <i>mtime</i> the last modification time, set to 0 on error.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> Return 0 or and error. See <b>krb5_get_error_message()</b>.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_free_kdc_rep (krb5_context, krb5_kdc_rep *)</h3>

 Variable containing the FILE based credential cache implemention.

<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_get_validated_creds (krb5_contextcontext, krb5_creds *creds, krb5_principalclient, krb5_ccacheccache, char *service)</h3>

 Validate the newly fetch credential, see also krb5_verify_init_creds(). 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> a Kerberos 5 context 
 <i>creds</i> the credentials to verify 
 <i>client</i> the client name to match up 
 <i>ccache</i> the credential cache to use 
 <i>service</i> a service name to use, used with <b>krb5_sname_to_principal()</b> to build a hostname to use to verify.</dl>
 

 

<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_is_config_principal (krb5_contextcontext, krb5_const_principalprincipal)</h3>

 Return TRUE (non zero) if the principal is a configuration principal (generated part of <b>krb5_cc_set_config()</b>). Returns FALSE (zero) if not a configuration principal. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> a Keberos context 
 <i>principal</i> principal to check if it a configuration principal</dl>
 

 

<h2>Variable Documentation</h2>

 

<h3>KRB5_LIB_VARIABLE const krb5_cc_ops krb5_acc_ops</h3>

 <b>Initial value:</b> 

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
</code></pre> Variable containing the API based credential cache implemention.

<h3>KRB5_LIB_VARIABLE const krb5_cc_ops krb5_dcc_ops</h3>

 <b>Initial value:</b> 

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
</pre> Variable containing the DIR based credential cache implemention.

<h3>KRB5_LIB_VARIABLE const krb5_cc_ops krb5_fcc_ops</h3>

 <b>Initial value:</b> 

 
= {
    KRB5_CC_OPS_VERSION,
    "FILE",
    fcc_get_name,
    fcc_resolve,
    fcc_gen_new,
    fcc_initialize,
    fcc_destroy,
    fcc_close,
    fcc_store_cred,
    NULL,
    fcc_get_principal,
    fcc_get_first,
    fcc_get_next,
    fcc_end_get,
    fcc_remove_cred,
    fcc_set_flags,
    fcc_get_version,
    fcc_get_cache_first,
    fcc_get_cache_next,
    fcc_end_cache_get,
    fcc_move,
    fcc_get_default_name,
    NULL,
    fcc_lastchange,
    fcc_set_kdc_offset,
    fcc_get_kdc_offset}
 Variable containing the FILE based credential cache implemention.

<h3>KRB5_LIB_VARIABLE const krb5_cc_ops krb5_mcc_ops</h3>

 <b>Initial value:</b> 

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
</code></pre> Variable containing the MEMORY based credential cache implemention.

<h2>Author</h2>

 

 Generated automatically by Doxygen for HeimdalKerberos5library from the source code. 

<h2>Index</h2>


