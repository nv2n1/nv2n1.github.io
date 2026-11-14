---
title: "krb5_get_init_creds_keytab(3)"
name: "krb5_get_init_creds_keytab"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_get_init_creds_keytab/"
description: "Heimdal Kerberos 5 credential handing functions –"
---

<h2 class="name">NAME</h2>
<p> Heimdal Kerberos 5 credential handing functions &#8211; </p>
<h3>Functions</h3>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_fwd_tgt_creds</code> (krb5_context context, krb5_auth_context auth_context, const char *hostname, krb5_principal client, krb5_principal server, krb5_ccache ccache, int forwardable, krb5_data *out_data)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_get_forwarded_creds</code> (krb5_context context, krb5_auth_context auth_context, krb5_ccache ccache, krb5_flags flags, const char *hostname, krb5_creds *in_creds, krb5_data *out_data)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_get_init_creds_opt_alloc</code> (krb5_context context, krb5_get_init_creds_opt **opt)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_get_init_creds_opt_free</code> (krb5_context context, krb5_get_init_creds_opt *opt)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_init_creds_init</code> (krb5_context context, krb5_principal client, krb5_prompter_fct prompter, void *prompter_data, krb5_deltat start_time, krb5_get_init_creds_opt *options, krb5_init_creds_context *rctx)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_init_creds_set_service</code> (krb5_context context, krb5_init_creds_context ctx, const char *service)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_init_creds_set_password</code> (krb5_context context, krb5_init_creds_context ctx, const char *password)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_init_creds_set_keytab</code> (krb5_context context, krb5_init_creds_context ctx, krb5_keytab keytab)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_init_creds_step</code> (krb5_context context, krb5_init_creds_context ctx, krb5_data *in, krb5_data *out, krb5_krbhst_info *hostinfo, unsigned int *flags)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_init_creds_get_error</code> (krb5_context context, krb5_init_creds_context ctx, KRB_ERROR *error)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_init_creds_free</code> (krb5_context context, krb5_init_creds_context ctx)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_init_creds_get</code> (krb5_context context, krb5_init_creds_context ctx)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_get_init_creds_password</code> (krb5_context context, krb5_creds *creds, krb5_principal client, const char *password, krb5_prompter_fct prompter, void *data, krb5_deltat start_time, const char *in_tkt_service, krb5_get_init_creds_opt *options)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_get_init_creds_keyblock</code> (krb5_context context, krb5_creds *creds, krb5_principal client, krb5_keyblock *keyblock, krb5_deltat start_time, const char *in_tkt_service, krb5_get_init_creds_opt *options)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_get_init_creds_keytab</code> (krb5_context context, krb5_creds *creds, krb5_principal client, krb5_keytab keytab, krb5_deltat start_time, const char *in_tkt_service, krb5_get_init_creds_opt *options)&quot; </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_fwd_tgt_creds (krb5_contextcontext, krb5_auth_contextauth_context, const char *hostname, krb5_principalclient, krb5_principalserver, krb5_ccacheccache, intforwardable, krb5_data *out_data)</h3>
<p> Forward credentials for client to host hostname , making them forwardable if forwardable, and returning the blob of data to sent in out_data. If hostname == NULL, pick it from server. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A kerberos 5 context.<br />
 <i>auth_context</i> the auth context with the key to encrypt the out_data.<br />
 <i>hostname</i> the host to forward the tickets too.<br />
 <i>client</i> the client to delegate from.<br />
 <i>server</i> the server to delegate the credential too.<br />
 <i>ccache</i> credential cache to use.<br />
 <i>forwardable</i> make the forwarded ticket forwabledable.<br />
 <i>out_data</i> the resulting credential.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_get_forwarded_creds (krb5_contextcontext, krb5_auth_contextauth_context, krb5_ccacheccache, krb5_flagsflags, const char *hostname, krb5_creds *in_creds, krb5_data *out_data)</h3>
<p> Gets tickets forwarded to hostname. If the tickets that are forwarded are address-less, the forwarded tickets will also be address-less. </p>
<p> If the ticket have any address, hostname will be used for figure out the address to forward the ticket too. This since this might use DNS, its insecure and also doesn&#8217;t represent configured all addresses of the host. For example, the host might have two adresses, one IPv4 and one IPv6 address where the later is not published in DNS. This IPv6 address might be used communications and thus the resulting ticket useless. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A kerberos 5 context.<br />
 <i>auth_context</i> the auth context with the key to encrypt the out_data.<br />
 <i>ccache</i> credential cache to use<br />
 <i>flags</i> the flags to control the resulting ticket flags<br />
 <i>hostname</i> the host to forward the tickets too.<br />
 <i>in_creds</i> the in client and server ticket names. The client and server components forwarded to the remote host.<br />
 <i>out_data</i> the resulting credential.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<p> Some older of the MIT gssapi library used clear-text tickets (warped inside AP-REQ encryption), use the krb5_auth_context flag KRB5_AUTH_CONTEXT_CLEAR_FORWARDED_CRED to support those tickets. The session key is used otherwise to encrypt the forwarded ticket.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_get_init_creds_keyblock (krb5_contextcontext, krb5_creds *creds, krb5_principalclient, krb5_keyblock *keyblock, krb5_deltatstart_time, const char *in_tkt_service, krb5_get_init_creds_opt *options)</h3>
<p> Get new credentials using keyblock.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_get_init_creds_keytab (krb5_contextcontext, krb5_creds *creds, krb5_principalclient, krb5_keytabkeytab, krb5_deltatstart_time, const char *in_tkt_service, krb5_get_init_creds_opt *options)</h3>
<p> Get new credentials using keytab.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_get_init_creds_opt_alloc (krb5_contextcontext, krb5_get_init_creds_opt **opt)</h3>
<p> Allocate a new krb5_get_init_creds_opt structure, free with <code>krb5_get_init_creds_opt_free()</code>.</p>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_get_init_creds_opt_free (krb5_contextcontext, krb5_get_init_creds_opt *opt)</h3>
<p> Free krb5_get_init_creds_opt structure.</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_get_init_creds_password (krb5_contextcontext, krb5_creds *creds, krb5_principalclient, const char *password, krb5_prompter_fctprompter, void *data, krb5_deltatstart_time, const char *in_tkt_service, krb5_get_init_creds_opt *options)</h3>
<p> Get new credentials using password.</p>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_init_creds_free (krb5_contextcontext, krb5_init_creds_contextctx)</h3>
<p> Free the krb5_init_creds_context allocated by <code>krb5_init_creds_init()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>ctx</i> The krb5_init_creds_context to free.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_init_creds_get (krb5_contextcontext, krb5_init_creds_contextctx)</h3>
<p> Get new credentials as setup by the krb5_init_creds_context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>ctx</i> The krb5_init_creds_context to process.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_init_creds_get_error (krb5_contextcontext, krb5_init_creds_contextctx, KRB_ERROR *error)</h3>
<p> Get the last error from the transaction. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 or an error code</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_init_creds_init (krb5_contextcontext, krb5_principalclient, krb5_prompter_fctprompter, void *prompter_data, krb5_deltatstart_time, krb5_get_init_creds_opt *options, krb5_init_creds_context *rctx)</h3>
<p> Start a new context to get a new initial credential. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>client</i> The Kerberos principal to get the credential for, if NULL is given, the default principal is used as determined by krb5_get_default_principal().<br />
 <i>prompter</i><br />
 <i>prompter_data</i><br />
 <i>start_time</i> the time the ticket should start to be valid or 0 for now.<br />
 <i>options</i> a options structure, can be NULL for default options.<br />
 <i>rctx</i> A new allocated free with <code>krb5_init_creds_free()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 for success or an Kerberos 5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_init_creds_set_keytab (krb5_contextcontext, krb5_init_creds_contextctx, krb5_keytabkeytab)</h3>
<p> Set the keytab to use for authentication. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Kerberos 5 context.<br />
 <i>ctx</i> ctx krb5_init_creds_context context.<br />
 <i>keytab</i> the keytab to read the key from.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 for success, or an Kerberos 5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_init_creds_set_password (krb5_contextcontext, krb5_init_creds_contextctx, const char *password)</h3>
<p> Sets the password that will use for the request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Kerberos 5 context.<br />
 <i>ctx</i> ctx krb5_init_creds_context context.<br />
 <i>password</i> the password to use.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 for success, or an Kerberos 5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_init_creds_set_service (krb5_contextcontext, krb5_init_creds_contextctx, const char *service)</h3>
<p> Sets the service that the is requested. This call is only neede for special initial tickets, by default the a krbtgt is fetched in the default realm. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Kerberos 5 context.<br />
 <i>ctx</i> a krb5_init_creds_context context.<br />
 <i>service</i> the service given as a string, for example &#8216;kadmind/admin&#8217;. If NULL, the default krbtgt in the clients realm is set.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 for success, or an Kerberos 5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_init_creds_step (krb5_contextcontext, krb5_init_creds_contextctx, krb5_data *in, krb5_data *out, krb5_krbhst_info *hostinfo, unsigned int *flags)</h3>
<p> The core loop if krb5_get_init_creds() function family. Create the packets and have the caller send them off to the KDC. </p>
<p> If the caller want all work been done for them, use <code>krb5_init_creds_get()</code> instead. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Kerberos 5 context.<br />
 <i>ctx</i> ctx krb5_init_creds_context context.<br />
 <i>in</i> input data from KDC, first round it should be reset by krb5_data_zer().<br />
 <i>out</i> reply to KDC.<br />
 <i>hostinfo</i> KDC address info, first round it can be NULL.<br />
 <i>flags</i> status of the round, if KRB5_INIT_CREDS_STEP_FLAG_CONTINUE is set, continue one more round.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 for success, or an Kerberos 5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for HeimdalKerberos5library from the source code. </p>
<h2>Index</h2>
