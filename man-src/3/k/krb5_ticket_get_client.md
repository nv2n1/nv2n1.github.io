---
title: "krb5_ticket_get_client(3)"
name: "krb5_ticket_get_client"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_ticket_get_client/"
description: "Heimdal Kerberos 5 library –"
---

<h2 class="name">NAME</h2>
<p> Heimdal Kerberos 5 library &#8211; </p>
<h3>Functions</h3>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_add_et_list</code> (krb5_context context, void(*func)(struct et_list **))&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_set_password</code> (krb5_context context, krb5_creds *creds, const char *newpw, krb5_principal targprinc, int *result_code, krb5_data *result_code_string, krb5_data *result_string)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_init_context</code> (krb5_context *context)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_copy_context</code> (krb5_context context, krb5_context *out)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_free_context</code> (krb5_context context)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_set_config_files</code> (krb5_context context, char **filenames)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_prepend_config_files_default</code> (const char *filelist, char ***pfilenames)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_get_default_config_files</code> (char ***pfilenames)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_free_config_files</code> (char **filenames)&quot; </p>
<p> KRB5_LIB_FUNCTION const<br />
 krb5_enctype *KRB5_LIB_CALL <code>krb5_kerberos_enctypes</code> (krb5_context context)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_set_default_in_tkt_etypes</code> (krb5_context context, const krb5_enctype *etypes)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_get_default_in_tkt_etypes</code> (krb5_context context, krb5_pdu pdu_type, krb5_enctype **etypes)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_init_ets</code> (krb5_context context)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_set_use_admin_kdc</code> (krb5_context context, krb5_boolean flag)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_get_use_admin_kdc</code> (krb5_context context)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_add_extra_addresses</code> (krb5_context context, krb5_addresses *addresses)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_set_extra_addresses</code> (krb5_context context, const krb5_addresses *addresses)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_get_extra_addresses</code> (krb5_context context, krb5_addresses *addresses)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_add_ignore_addresses</code> (krb5_context context, krb5_addresses *addresses)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_set_ignore_addresses</code> (krb5_context context, const krb5_addresses *addresses)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_get_ignore_addresses</code> (krb5_context context, krb5_addresses *addresses)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_set_fcache_version</code> (krb5_context context, int version)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_get_fcache_version</code> (krb5_context context, int *version)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_is_thread_safe</code> (void)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_set_dns_canonicalize_hostname</code> (krb5_context context, krb5_boolean flag)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_get_dns_canonicalize_hostname</code> (krb5_context context)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_get_kdc_sec_offset</code> (krb5_context context, int32_t *sec, int32_t *usec)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_set_kdc_sec_offset</code> (krb5_context context, int32_t sec, int32_t usec)&quot; </p>
<p> KRB5_LIB_FUNCTION time_t<br />
 KRB5_LIB_CALL <code>krb5_get_max_time_skew</code> (krb5_context context)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_set_max_time_skew</code> (krb5_context context, time_t t)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_set_home_dir_access</code> (krb5_context context, krb5_boolean allow)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_copy_host_realm</code> (krb5_context context, const krb5_realm *from, krb5_realm **to)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_free_cred_contents</code> (krb5_context context, krb5_creds *c)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_copy_creds_contents</code> (krb5_context context, const krb5_creds *incred, krb5_creds *c)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_copy_creds</code> (krb5_context context, const krb5_creds *incred, krb5_creds **outcred)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_free_creds</code> (krb5_context context, krb5_creds *c)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_compare_creds</code> (krb5_context context, krb5_flags whichfields, const krb5_creds *mcreds, const krb5_creds *creds)&quot; </p>
<p> KRB5_LIB_FUNCTION unsigned<br />
 long KRB5_LIB_CALL <code>krb5_creds_get_ticket_flags</code> (krb5_creds *creds)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_data_zero</code> (krb5_data *p)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_data_free</code> (krb5_data *p)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_free_data</code> (krb5_context context, krb5_data *p)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_data_alloc</code> (krb5_data *p, int len)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_data_realloc</code> (krb5_data *p, int len)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_data_copy</code> (krb5_data *p, const void *data, size_t len)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_copy_data</code> (krb5_context context, const krb5_data *indata, krb5_data **outdata)&quot; </p>
<p> KRB5_LIB_FUNCTION int KRB5_LIB_CALL <code>krb5_data_cmp</code> (const krb5_data *data1, const krb5_data *data2) </p>
<p> KRB5_LIB_FUNCTION int KRB5_LIB_CALL <code>krb5_data_ct_cmp</code> (const krb5_data *data1, const krb5_data *data2) </p>
<p> KRB5_LIB_FUNCTION const char<br />
 *KRB5_LIB_CALL <code>KRB5_DEPRECATED_FUNCTION</code> (&#8216;Use <code>krb5_get_error_message</code> instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_copy_ticket</code> (krb5_context, const krb5_ticket *, krb5_ticket **)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_free_ticket</code> (krb5_context, krb5_ticket *)&quot; </p>
<p> KRB5_LIB_FUNCTION const char<br />
 *KRB5_LIB_CALL <code>krb5_get_err_text</code> (krb5_context, krb5_error_code) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use <code>krb5_get_error_message</code> instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_krbhst_get_addrinfo</code> (krb5_context, krb5_krbhst_info *, struct addrinfo **)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_set_real_time</code> (krb5_context, krb5_timestamp, int32_t)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_ticket_get_authorization_data_type</code> (krb5_context, krb5_ticket *, int, krb5_data *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_ticket_get_client</code> (krb5_context, const krb5_ticket *, krb5_principal *)&quot; </p>
<p> KRB5_LIB_FUNCTION time_t<br />
 KRB5_LIB_CALL <code>krb5_ticket_get_endtime</code> (krb5_context, const krb5_ticket *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_ticket_get_server</code> (krb5_context, const krb5_ticket *, krb5_principal *)&quot; </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_add_et_list (krb5_contextcontext, void(*)(struct et_list **)func)</h3>
<p> Add a specified list of error messages to the et list in context. Call func (probably a comerr-generated function) with a pointer to the current et_list. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A kerberos context.<br />
 <i>func</i> The generated com_err et function.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_add_extra_addresses (krb5_contextcontext, krb5_addresses *addresses)</h3>
<p> Add extra address to the address list that the library will add to the client&#8217;s address list when communicating with the KDC. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>addresses</i> addreses to add</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_add_ignore_addresses (krb5_contextcontext, krb5_addresses *addresses)</h3>
<p> Add extra addresses to ignore when fetching addresses from the underlaying operating system. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>addresses</i> addreses to ignore</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_compare_creds (krb5_contextcontext, krb5_flagswhichfields, const krb5_creds *mcreds, const krb5_creds *creds)</h3>
<p> Return TRUE if `mcreds&#8217; and `creds&#8217; are equal (`whichfields&#8217; determines what equal means). </p>
<p> The following flags, set in whichfields affects the comparison:</p>
<dl>
<dt>&bull;</p>
<dd> KRB5_TC_MATCH_SRV_NAMEONLY Consider all realms equal when comparing the service principal.</p>
<dt>&bull;</p>
<dd> KRB5_TC_MATCH_KEYTYPE Compare enctypes.</p>
<dt>&bull;</p>
<dd> KRB5_TC_MATCH_FLAGS_EXACT Make sure that the ticket flags are identical.</p>
<dt>&bull;</p>
<dd> KRB5_TC_MATCH_FLAGS Make sure that all ticket flags set in mcreds are also present in creds .</p>
<dt>&bull;</p>
<dd> KRB5_TC_MATCH_TIMES_EXACT Compares the ticket times exactly.</p>
<dt>&bull;</p>
<dd> KRB5_TC_MATCH_TIMES Compares only the expiration times of the creds.</p>
<dt>&bull;</p>
<dd> KRB5_TC_MATCH_AUTHDATA Compares the authdata fields.</p>
<dt>&bull;</p>
<dd> KRB5_TC_MATCH_2ND_TKT Compares the second tickets (used by user-to-user authentication).</p>
<dt>&bull;</p>
<dd> KRB5_TC_MATCH_IS_SKEY Compares the existance of the second ticket.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>whichfields</i> which fields to compare.<br />
 <i>mcreds</i> cred to compare with.<br />
 <i>creds</i> cred to compare with.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> return TRUE if mcred and creds are equal, FALSE if not.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_copy_context (krb5_contextcontext, krb5_context *out)</h3>
<p> Make a copy for the Kerberos 5 context, the new krb5_context shoud be freed with <code>krb5_free_context()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> the Kerberos context to copy<br />
 <i>out</i> the copy of the Kerberos, set to NULL error.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_copy_creds (krb5_contextcontext, const krb5_creds *incred, krb5_creds **outcred)</h3>
<p> Copy krb5_creds. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>incred</i> source credential<br />
 <i>outcred</i> destination credential, free with <code>krb5_free_creds()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_copy_creds_contents (krb5_contextcontext, const krb5_creds *incred, krb5_creds *c)</h3>
<p> Copy content of krb5_creds. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>incred</i> source credential<br />
 <i>c</i> destination credential, free with <code>krb5_free_cred_contents()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_copy_data (krb5_contextcontext, const krb5_data *indata, krb5_data **outdata)</h3>
<p> Copy the data into a newly allocated krb5_data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>indata</i> the krb5_data data to copy<br />
 <i>outdata</i> new krb5_date to copy too. Free with <code>krb5_free_data()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_copy_host_realm (krb5_contextcontext, const krb5_realm *from, krb5_realm **to)</h3>
<p> Copy the list of realms from `from&#8217; to `to&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>from</i> list of realms to copy from.<br />
 <i>to</i> list of realms to copy to, free list of <code>krb5_free_host_realm()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_copy_ticket (krb5_contextcontext, const krb5_ticket *from, krb5_ticket **to)</h3>
<p> Copy ticket and content </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Kerberos 5 context<br />
 <i>from</i> ticket to copy<br />
 <i>to</i> new copy of ticket, free with <code>krb5_free_ticket()</code></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION unsigned long KRB5_LIB_CALL krb5_creds_get_ticket_flags (krb5_creds *creds)</h3>
<p> Returns the ticket flags for the credentials in creds. See also <code>krb5_ticket_get_flags()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>creds</i> credential to get ticket flags from</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> ticket flags</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_data_alloc (krb5_data *p, intlen)</h3>
<p> Allocate data of and krb5_data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>p</i> krb5_data to allocate.<br />
 <i>len</i> size to allocate.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned.</dl>
<h3>KRB5_LIB_FUNCTION int KRB5_LIB_CALL krb5_data_cmp (const krb5_data *data1, const krb5_data *data2)</h3>
<p> Compare to data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data1</i> krb5_data to compare<br />
 <i>data2</i> krb5_data to compare</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> return the same way as memcmp(), useful when sorting.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_data_copy (krb5_data *p, const void *data, size_tlen)</h3>
<p> Copy the data of len into the krb5_data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>p</i> krb5_data to copy into.<br />
 <i>data</i> data to copy..<br />
 <i>len</i> new size.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned.</dl>
<h3>KRB5_LIB_FUNCTION int KRB5_LIB_CALL krb5_data_ct_cmp (const krb5_data *data1, const krb5_data *data2)</h3>
<p> Compare to data not exposing timing information from the checksum data </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data1</i> krb5_data to compare<br />
 <i>data2</i> krb5_data to compare</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> returns zero for same data, otherwise non zero.</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_data_free (krb5_data *p)</h3>
<p> Free the content of krb5_data structure, its ok to free a zeroed structure (with memset() or <code>krb5_data_zero()</code>). When done, the structure will be zeroed. The same function is called <code>krb5_free_data_contents()</code> in MIT Kerberos. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>p</i> krb5_data to free.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_data_realloc (krb5_data *p, intlen)</h3>
<p> Grow (or shrink) the content of krb5_data to a new size. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>p</i> krb5_data to free.<br />
 <i>len</i> new size.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned.</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_data_zero (krb5_data *p)</h3>
<p> Reset the (potentially uninitalized) krb5_data structure. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>p</i> krb5_data to reset.</dl>
<h3>KRB5_LIB_FUNCTION const char* KRB5_LIB_CALL KRB5_DEPRECATED_FUNCTION (&#8216;Use <code>krb5_get_error_message</code> instead&#8217;)</h3>
<p> Return the error string for the error code. The caller must not free the string. </p>
<p> This function is deprecated since its not threadsafe. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>code</i> Kerberos error code.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the error message matching code</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_free_config_files (char **filenames)</h3>
<p> Free a list of configuration files. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>filenames</i> list, terminated with a NULL pointer, to be freed. NULL is an valid argument.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_free_context (krb5_contextcontext)</h3>
<p> Frees the krb5_context allocated by <code>krb5_init_context()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> context to be freed.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_free_cred_contents (krb5_contextcontext, krb5_creds *c)</h3>
<p> Free content of krb5_creds. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>c</i> krb5_creds to free.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_free_creds (krb5_contextcontext, krb5_creds *c)</h3>
<p> Free krb5_creds. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>c</i> krb5_creds to free.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_free_data (krb5_contextcontext, krb5_data *p)</h3>
<p> Free krb5_data (and its content). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>p</i> krb5_data to free.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_free_ticket (krb5_contextcontext, krb5_ticket *ticket)</h3>
<p> Free ticket and content </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Kerberos 5 context<br />
 <i>ticket</i> ticket to free</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_get_default_config_files (char ***pfilenames)</h3>
<p> Get the global configuration list. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>pfilenames</i> return array of filenames, should be freed with <code>krb5_free_config_files()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_get_default_in_tkt_etypes (krb5_contextcontext, krb5_pdupdu_type, krb5_enctype **etypes)</h3>
<p> Get the default encryption types that will be use in communcation with the KDC, clients and servers. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>etypes</i> Encryption types, array terminated with ETYPE_NULL(0), caller should free array with krb5_xfree():</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_get_dns_canonicalize_hostname (krb5_contextcontext)</h3>
<p> Get if the library uses DNS to canonicalize hostnames. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> return non zero if the library uses DNS to canonicalize hostnames.</dl>
<h3>KRB5_LIB_FUNCTION const char* KRB5_LIB_CALL krb5_get_err_text (krb5_context, krb5_error_code)</h3>
<p> Return the error string for the error code. The caller must not free the string. </p>
<p> This function is deprecated since its not threadsafe. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>code</i> Kerberos error code.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the error message matching code</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_get_extra_addresses (krb5_contextcontext, krb5_addresses *addresses)</h3>
<p> Get extra address to the address list that the library will add to the client&#8217;s address list when communicating with the KDC. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>addresses</i> addreses to set</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_get_fcache_version (krb5_contextcontext, int *version)</h3>
<p> Get version of fcache that the library should use. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>version</i> version number.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_get_ignore_addresses (krb5_contextcontext, krb5_addresses *addresses)</h3>
<p> Get extra addresses to ignore when fetching addresses from the underlaying operating system. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>addresses</i> list addreses ignored</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_get_kdc_sec_offset (krb5_contextcontext, int32_t *sec, int32_t *usec)</h3>
<p> Get current offset in time to the KDC. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>sec</i> seconds part of offset.<br />
 <i>usec</i> micro seconds part of offset.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> returns zero</dl>
<h3>KRB5_LIB_FUNCTION time_t KRB5_LIB_CALL krb5_get_max_time_skew (krb5_contextcontext)</h3>
<p> Get max time skew allowed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> timeskew in seconds.</dl>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_get_use_admin_kdc (krb5_contextcontext)</h3>
<p> Make the kerberos library default to the admin KDC. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> boolean flag to telling the context will use admin KDC as the default KDC.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_init_context (krb5_context *context)</h3>
<p> Initializes the context structure and reads the configuration file /etc/krb5.conf. The structure should be freed by calling <code>krb5_free_context()</code> when it is no longer being used. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> pointer to returned context</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an errno code is returned. Failure means either that something bad happened during initialization (typically ENOMEM) or that Kerberos should not be used ENXIO. If the function returns HEIM_ERR_RANDOM_OFFLINE, the random source is not available and later Kerberos calls might fail.</dl>
<p> <code>krb5_init_context()</code> will get one random byte to make sure our random is alive. Assumption is that once the non blocking source allows us to pull bytes, its all seeded and allows us to pull more bytes. </p>
<p> Most Kerberos users calls <code>krb5_init_context()</code>, so this is useful point where we can do the checking.</p>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_init_ets (krb5_contextcontext)</h3>
<p> Init the built-in ets in the Kerberos library. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> kerberos context to add the ets too</dl>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_is_thread_safe (void)</h3>
<p> Runtime check if the Kerberos library was complied with thread support. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE if the library was compiled with thread support, FALSE if not.</dl>
<h3>KRB5_LIB_FUNCTION const krb5_enctype *KRB5_LIB_CALL krb5_kerberos_enctypes (krb5_contextcontext)</h3>
<p> Returns the list of Kerberos encryption types sorted in order of most preferred to least preferred encryption type. Note that some encryption types might be disabled, so you need to check with <code>krb5_enctype_valid()</code> before using the encryption type. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> list of enctypes, terminated with ETYPE_NULL. Its a static array completed into the Kerberos library so the content doesn&#8217;t need to be freed.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_krbhst_get_addrinfo (krb5_contextcontext, krb5_krbhst_info *host, struct addrinfo **ai)</h3>
<p> Return an `struct addrinfo *&#8217; for a KDC host. </p>
<p> Returns an the struct addrinfo in in that corresponds to the information in `host&#8217;. free:ing is handled by krb5_krbhst_free, so the returned ai must not be released. First try this as an IP address, this allows us to add a dot at the end to stop using the search domains. </p>
<p> If the hostname contains a dot, assumes it&#8217;s a FQDN and don&#8217;t use search domains since that might be painfully slow when machine is disconnected from that network.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_prepend_config_files_default (const char *filelist, char ***pfilenames)</h3>
<p> Prepend the filename to the global configuration list. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>filelist</i> a filename to add to the default list of filename<br />
 <i>pfilenames</i> return array of filenames, should be freed with <code>krb5_free_config_files()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_set_config_files (krb5_contextcontext, char **filenames)</h3>
<p> Reinit the context from a new set of filenames. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> context to add configuration too.<br />
 <i>filenames</i> array of filenames, end of list is indicated with a NULL filename.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_set_default_in_tkt_etypes (krb5_contextcontext, const krb5_enctype *etypes)</h3>
<p> Set the default encryption types that will be use in communcation with the KDC, clients and servers. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>etypes</i> Encryption types, array terminated with ETYPE_NULL (0).</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_set_dns_canonicalize_hostname (krb5_contextcontext, krb5_booleanflag)</h3>
<p> Set if the library should use DNS to canonicalize hostnames. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>flag</i> if its dns canonicalizion is used or not.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_set_extra_addresses (krb5_contextcontext, const krb5_addresses *addresses)</h3>
<p> Set extra address to the address list that the library will add to the client&#8217;s address list when communicating with the KDC. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>addresses</i> addreses to set</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_set_fcache_version (krb5_contextcontext, intversion)</h3>
<p> Set version of fcache that the library should use. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>version</i> version number.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_set_home_dir_access (krb5_contextcontext, krb5_booleanallow)</h3>
<p> Enable and disable home directory access on either the global state or the krb5_context state. By calling <code>krb5_set_home_dir_access()</code> with context set to NULL, the global state is configured otherwise the state for the krb5_context is modified. </p>
<p> For home directory access to be allowed, both the global state and the krb5_context state have to be allowed. </p>
<p> Administrator (root user), never uses the home directory. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Kerberos 5 context or NULL<br />
 <i>allow</i> allow if TRUE home directory</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the old value</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_set_ignore_addresses (krb5_contextcontext, const krb5_addresses *addresses)</h3>
<p> Set extra addresses to ignore when fetching addresses from the underlaying operating system. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>addresses</i> addreses to ignore</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_set_kdc_sec_offset (krb5_contextcontext, int32_tsec, int32_tusec)</h3>
<p> Set current offset in time to the KDC. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>sec</i> seconds part of offset.<br />
 <i>usec</i> micro seconds part of offset.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> returns zero</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_set_max_time_skew (krb5_contextcontext, time_tt)</h3>
<p> Set max time skew allowed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>t</i> timeskew in seconds.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_set_password (krb5_contextcontext, krb5_creds *creds, const char *newpw, krb5_principaltargprinc, int *result_code, krb5_data *result_code_string, krb5_data *result_string)</h3>
<p> Change password using creds. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>creds</i> The initial kadmin/passwd for the principal or an admin principal<br />
 <i>newpw</i> The new password to set<br />
 <i>targprinc</i> if unset, the default principal is used.<br />
 <i>result_code</i> Result code, KRB5_KPASSWD_SUCCESS is when password is changed.<br />
 <i>result_code_string</i> binary message from the server, contains at least the result_code.<br />
 <i>result_string</i> A message from the kpasswd service or the library in human printable form. The string is NUL terminated.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On sucess and *result_code is KRB5_KPASSWD_SUCCESS, the password is changed.</dl>
<p> @</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_set_real_time (krb5_contextcontext, krb5_timestampsec, int32_tusec)</h3>
<p> Set the absolute time that the caller knows the kdc has so the kerberos library can calculate the relative diffrence beteen the KDC time and local system time. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Keberos 5 context.<br />
 <i>sec</i> The applications new of &#8216;now&#8217; in seconds<br />
 <i>usec</i> The applications new of &#8216;now&#8217; in micro seconds</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Kerberos 5 error code, see <code>krb5_get_error_message()</code>.</dl>
<p> If the caller passes in a negative usec, its assumed to be unknown and the function will use the current time usec.</p>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_set_use_admin_kdc (krb5_contextcontext, krb5_booleanflag)</h3>
<p> Make the kerberos library default to the admin KDC. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>flag</i> boolean flag to select if the use the admin KDC or not.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_ticket_get_authorization_data_type (krb5_contextcontext, krb5_ticket *ticket, inttype, krb5_data *data)</h3>
<p> Extract the authorization data type of type from the ticket. Store the field in data. This function is to use for kerberos applications. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Kerberos 5 context<br />
 <i>ticket</i> Kerberos ticket<br />
 <i>type</i> type to fetch<br />
 <i>data</i> returned data, free with <code>krb5_data_free()</code></dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_ticket_get_client (krb5_contextcontext, const krb5_ticket *ticket, krb5_principal *client)</h3>
<p> Return client principal in ticket </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Kerberos 5 context<br />
 <i>ticket</i> ticket to copy<br />
 <i>client</i> client principal, free with <code>krb5_free_principal()</code></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION time_t KRB5_LIB_CALL krb5_ticket_get_endtime (krb5_contextcontext, const krb5_ticket *ticket)</h3>
<p> Return end time of ticket </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Kerberos 5 context<br />
 <i>ticket</i> ticket to copy</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> end time of ticket</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_ticket_get_server (krb5_contextcontext, const krb5_ticket *ticket, krb5_principal *server)</h3>
<p> Return server principal in ticket </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Kerberos 5 context<br />
 <i>ticket</i> ticket to copy<br />
 <i>server</i> server principal, free with <code>krb5_free_principal()</code></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for HeimdalKerberos5library from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbCK">Author</a></p>
<dd></dl>
