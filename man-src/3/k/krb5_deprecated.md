---
title: "krb5_deprecated(3)"
name: "krb5_deprecated"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_deprecated/"
description: "Heimdal Kerberos 5 deprecated functions –"
---

<h2 class="name">NAME</h2>
<p> Heimdal Kerberos 5 deprecated functions &#8211; </p>
<h3>Functions</h3>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_change_password</code> (krb5_context context, krb5_creds *creds, const char *newpw, int *result_code, krb5_data *result_code_string, krb5_data *result_string) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_config_parse_string_multi</code> (krb5_context context, const char *string, krb5_config_section **res) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_keytype_to_enctypes</code> (krb5_context context, krb5_keytype keytype, unsigned *len, krb5_enctype **val) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_enctypes_compatible_keys</code> (krb5_context context, krb5_enctype etype1, krb5_enctype etype2) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>KRB5_DEPRECATED_FUNCTION</code> (&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_keytype_to_enctypes_default</code> (krb5_context context, krb5_keytype keytype, unsigned *len, krb5_enctype **val) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_keytype_to_string</code> (krb5_context context, krb5_keytype keytype, char **string) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_string_to_keytype</code> (krb5_context context, const char *string, krb5_keytype *keytype) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_CALLCONV <code>krb5_password_key_proc</code> (krb5_context context, krb5_enctype type, krb5_salt salt, krb5_const_pointer keyseed, krb5_keyblock **key) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_get_in_tkt_with_password</code> (krb5_context context, krb5_flags options, krb5_addresses *addrs, const krb5_enctype *etypes, const krb5_preauthtype *pre_auth_types, const char *password, krb5_ccache ccache, krb5_creds *creds, krb5_kdc_rep *ret_as_reply) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_get_in_tkt_with_skey</code> (krb5_context context, krb5_flags options, krb5_addresses *addrs, const krb5_enctype *etypes, const krb5_preauthtype *pre_auth_types, const krb5_keyblock *key, krb5_ccache ccache, krb5_creds *creds, krb5_kdc_rep *ret_as_reply) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_CALLCONV <code>krb5_keytab_key_proc</code> (krb5_context context, krb5_enctype enctype, krb5_salt salt, krb5_const_pointer keyseed, krb5_keyblock **key) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_get_in_tkt_with_keytab</code> (krb5_context context, krb5_flags options, krb5_addresses *addrs, const krb5_enctype *etypes, const krb5_preauthtype *pre_auth_types, krb5_keytab keytab, krb5_ccache ccache, krb5_creds *creds, krb5_kdc_rep *ret_as_reply) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_realm<br />
 *KRB5_LIB_CALL <code>krb5_princ_realm</code> (krb5_context context, krb5_principal principal) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_princ_set_realm</code> (krb5_context context, krb5_principal principal, krb5_realm *realm) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>__attribute__</code> ((format(printf, 2, 3)))&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>__attribute__</code> ((format(printf, 2, 0)))&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_get_cred_from_kdc_opt</code> (krb5_context context, krb5_ccache ccache, krb5_creds *in_creds, krb5_creds **out_creds, krb5_creds ***ret_tgts, krb5_flags flags) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_get_cred_from_kdc</code> (krb5_context context, krb5_ccache ccache, krb5_creds *in_creds, krb5_creds **out_creds, krb5_creds ***ret_tgts) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_generate_subkey</code> (krb5_context context, const krb5_keyblock *key, krb5_keyblock **subkey) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_auth_getremoteseqnumber</code> (krb5_context context, krb5_auth_context auth_context, int32_t *seqnumber) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_get_init_creds_opt_get_error</code> (krb5_context context, krb5_get_init_creds_opt *opt, KRB_ERROR **error) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_c_enctype_compare</code> (krb5_context, krb5_enctype, krb5_enctype, krb5_boolean *) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_free_creds_contents</code> (krb5_context, krb5_creds *) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_free_data_contents</code> (krb5_context, krb5_data *) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_free_error_string</code> (krb5_context, char *) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_free_unparsed_name</code> (krb5_context, char *) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL<br />
 KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_set_error_string</code> (krb5_context, const char *,&#8230;) <code>__attribute__</code>((format(printf&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL<br />
 KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL<br />
 KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL<br />
 KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL<br />
 KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_vset_error_string</code> (krb5_context, const char *, va_list) <code>__attribute__</code>((format(printf&quot; </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL __attribute__ ((format(printf, 2, 3)))</h3>
<p> Set the error message returned by krb5_get_error_string(). </p>
<p> Deprecated: use <code>krb5_get_error_message()</code> </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos context<br />
 <i>fmt</i> error message to free</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL __attribute__ ((format(printf, 2, 0)))</h3>
<p> Set the error message returned by krb5_get_error_string(), deprecated, use <code>krb5_set_error_message()</code>. </p>
<p> Deprecated: use <code>krb5_vset_error_message()</code> </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos context<br />
 <i>msg</i> error message to free</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_auth_getremoteseqnumber (krb5_contextcontext, krb5_auth_contextauth_context, int32_t *seqnumber)</h3>
<p> Deprecated: use krb5_auth_con_getremoteseqnumber()</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_c_enctype_compare (krb5_contextcontext, krb5_enctypee1, krb5_enctypee2, krb5_boolean *similar)</h3>
<p> Deprecated: keytypes doesn&#8217;t exists, they are really enctypes.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_change_password (krb5_contextcontext, krb5_creds *creds, const char *newpw, int *result_code, krb5_data *result_code_string, krb5_data *result_string)</h3>
<p> Deprecated: <code>krb5_change_password()</code> is deprecated, use <code>krb5_set_password()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>creds</i><br />
 <i>newpw</i><br />
 <i>result_code</i><br />
 <i>result_code_string</i><br />
 <i>result_string</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On sucess password is changed.</dl>
<p> @</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_config_parse_string_multi (krb5_contextcontext, const char *string, krb5_config_section **res)</h3>
<p> Deprecated: configuration files are not strings</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL KRB5_LIB_FUNCTION void KRB5_LIB_CALL KRB5_LIB_FUNCTION void KRB5_LIB_CALL KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL KRB5_DEPRECATED_FUNCTION (&#8216;Use X instead&#8217;)</h3>
<p> Same as <code>krb5_data_free()</code>. MIT compat. </p>
<p> Deprecated: use <code>krb5_data_free()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>data</i> krb5_data to free.</dl>
<p> Deprecated: use <code>krb5_free_cred_contents()</code> </p>
<p> Free the error message returned by krb5_get_error_string(). </p>
<p> Deprecated: use <code>krb5_free_error_message()</code> </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos context<br />
 <i>str</i> error message to free</dl>
<p> Clear the error message returned by krb5_get_error_string(). </p>
<p> Deprecated: use <code>krb5_clear_error_message()</code> </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos context</dl>
<p> Deprecated: use krb5_xfree(). </p>
<p> Deprecated: use <code>krb5_get_init_creds_opt_alloc()</code>. </p>
<p> The reason krb5_get_init_creds_opt_init() is deprecated is that krb5_get_init_creds_opt is a static structure and for ABI reason it can&#8217;t grow, ie can&#8217;t add new functionality.</p>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_enctypes_compatible_keys (krb5_contextcontext, krb5_enctypeetype1, krb5_enctypeetype2)</h3>
<p> Deprecated: keytypes doesn&#8217;t exists, they are really enctypes.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_free_creds_contents (krb5_context, krb5_creds *)</h3>
<p> Deprecated: use <code>krb5_free_cred_contents()</code></p>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_free_data_contents (krb5_context, krb5_data *)</h3>
<p> Same as <code>krb5_data_free()</code>. MIT compat. </p>
<p> Deprecated: use <code>krb5_data_free()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>data</i> krb5_data to free.</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_free_error_string (krb5_context, char *)</h3>
<p> Free the error message returned by krb5_get_error_string(). </p>
<p> Deprecated: use <code>krb5_free_error_message()</code> </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos context<br />
 <i>str</i> error message to free</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_free_unparsed_name (krb5_context, char *)</h3>
<p> Deprecated: use krb5_xfree().</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_generate_subkey (krb5_contextcontext, const krb5_keyblock *key, krb5_keyblock **subkey)</h3>
<p> Deprecated: use <code>krb5_generate_subkey_extended()</code></p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_get_cred_from_kdc (krb5_contextcontext, krb5_ccacheccache, krb5_creds *in_creds, krb5_creds **out_creds, krb5_creds ***ret_tgts)</h3>
<p> Deprecated: use krb5_get_credentials_with_flags().</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_get_cred_from_kdc_opt (krb5_contextcontext, krb5_ccacheccache, krb5_creds *in_creds, krb5_creds **out_creds, krb5_creds ***ret_tgts, krb5_flagsflags)</h3>
<p> Deprecated: use krb5_get_credentials_with_flags().</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_get_in_tkt_with_keytab (krb5_contextcontext, krb5_flagsoptions, krb5_addresses *addrs, const krb5_enctype *etypes, const krb5_preauthtype *pre_auth_types, krb5_keytabkeytab, krb5_ccacheccache, krb5_creds *creds, krb5_kdc_rep *ret_as_reply)</h3>
<p> Deprecated: use krb5_get_init_creds() and friends.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_get_in_tkt_with_password (krb5_contextcontext, krb5_flagsoptions, krb5_addresses *addrs, const krb5_enctype *etypes, const krb5_preauthtype *pre_auth_types, const char *password, krb5_ccacheccache, krb5_creds *creds, krb5_kdc_rep *ret_as_reply)</h3>
<p> Deprecated: use krb5_get_init_creds() and friends.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_get_in_tkt_with_skey (krb5_contextcontext, krb5_flagsoptions, krb5_addresses *addrs, const krb5_enctype *etypes, const krb5_preauthtype *pre_auth_types, const krb5_keyblock *key, krb5_ccacheccache, krb5_creds *creds, krb5_kdc_rep *ret_as_reply)</h3>
<p> Deprecated: use krb5_get_init_creds() and friends.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_get_init_creds_opt_get_error (krb5_contextcontext, krb5_get_init_creds_opt *opt, KRB_ERROR **error)</h3>
<p> Deprecated: use the new <code>krb5_init_creds_init()</code> and <code>krb5_init_creds_get_error()</code>.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_CALLCONV krb5_keytab_key_proc (krb5_contextcontext, krb5_enctypeenctype, krb5_saltsalt, krb5_const_pointerkeyseed, krb5_keyblock **key)</h3>
<p> Deprecated: use krb5_get_init_creds() and friends.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_keytype_to_enctypes (krb5_contextcontext, krb5_keytypekeytype, unsigned *len, krb5_enctype **val)</h3>
<p> Deprecated: keytypes doesn&#8217;t exists, they are really enctypes.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_keytype_to_enctypes_default (krb5_contextcontext, krb5_keytypekeytype, unsigned *len, krb5_enctype **val)</h3>
<p> Deprecated: keytypes doesn&#8217;t exists, they are really enctypes.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_keytype_to_string (krb5_contextcontext, krb5_keytypekeytype, char **string)</h3>
<p> Deprecated: keytypes doesn&#8217;t exists, they are really enctypes in most cases, use krb5_enctype_to_string().</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_CALLCONV krb5_password_key_proc (krb5_contextcontext, krb5_enctypetype, krb5_saltsalt, krb5_const_pointerkeyseed, krb5_keyblock **key)</h3>
<p> Deprecated: use krb5_get_init_creds() and friends.</p>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL KRB5_LIB_FUNCTION krb5_realm *KRB5_LIB_CALL krb5_princ_realm (krb5_contextcontext, krb5_principalprincipal)</h3>
<p> Deprecated: use <code>krb5_principal_get_realm()</code></p>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_princ_set_realm (krb5_contextcontext, krb5_principalprincipal, krb5_realm *realm)</h3>
<p> Deprecated: use <code>krb5_principal_set_realm()</code></p>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_set_error_string (krb5_context, const char *, &#8230;)</h3>
<p> Set the error message returned by krb5_get_error_string(). </p>
<p> Deprecated: use <code>krb5_get_error_message()</code> </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos context<br />
 <i>fmt</i> error message to free</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_string_to_keytype (krb5_contextcontext, const char *string, krb5_keytype *keytype)</h3>
<p> Deprecated: keytypes doesn&#8217;t exists, they are really enctypes in most cases, use krb5_string_to_enctype().</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL KRB5_LIB_FUNCTION void KRB5_LIB_CALL KRB5_LIB_FUNCTION void KRB5_LIB_CALL KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_vset_error_string (krb5_context, const char *, va_list)</h3>
<p> Set the error message returned by krb5_get_error_string(), deprecated, use <code>krb5_set_error_message()</code>. </p>
<p> Deprecated: use <code>krb5_vset_error_message()</code> </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos context<br />
 <i>msg</i> error message to free</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for HeimdalKerberos5library from the source code. </p>
<h2>Index</h2>
