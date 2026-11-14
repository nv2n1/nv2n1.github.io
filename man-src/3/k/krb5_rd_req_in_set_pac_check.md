---
title: "krb5_rd_req_in_set_pac_check(3)"
name: "krb5_rd_req_in_set_pac_check"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_rd_req_in_set_pac_check/"
description: "Heimdal Kerberos 5 authentication functions –"
---

<h2 class="name">NAME</h2>
<p> Heimdal Kerberos 5 authentication functions &#8211; </p>
<h3>Functions</h3>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_rd_req_ctx</code> (krb5_context, krb5_auth_context *, const krb5_data *, krb5_const_principal, krb5_rd_req_in_ctx, krb5_rd_req_out_ctx *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_rd_req_in_ctx_alloc</code> (krb5_context, krb5_rd_req_in_ctx *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_rd_req_in_set_keytab</code> (krb5_context, krb5_rd_req_in_ctx, krb5_keytab)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_rd_req_in_set_pac_check</code> (krb5_context, krb5_rd_req_in_ctx, krb5_boolean)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_rd_req_out_ctx_free</code> (krb5_context, krb5_rd_req_out_ctx)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_rd_req_out_get_server</code> (krb5_context, krb5_rd_req_out_ctx, krb5_principal *)&quot; </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_rd_req_ctx (krb5_contextcontext, krb5_auth_context *auth_context, const krb5_data *inbuf, krb5_const_principalserver, krb5_rd_req_in_ctxinctx, krb5_rd_req_out_ctx *outctx)</h3>
<p> The core server function that verify application authentication requests from clients. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Keberos 5 context.<br />
 <i>auth_context</i> the authentication context, can be NULL, then default values for the authentication context will used.<br />
 <i>inbuf</i> the (AP-REQ) authentication buffer<br />
 <i>server</i> the server to authenticate to. If NULL the function will try to find any available credential in the keytab that will verify the reply. The function will prefer the server specified in the AP-REQ, but if there is no mach, it will try all keytab entries for a match. This has serious performance issues for large keytabs.<br />
 <i>inctx</i> control the behavior of the function, if NULL, the default behavior is used.<br />
 <i>outctx</i> the return outctx, free with <code>krb5_rd_req_out_ctx_free()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Kerberos 5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_rd_req_in_ctx_alloc (krb5_contextcontext, krb5_rd_req_in_ctx *ctx)</h3>
<p> Allocate a krb5_rd_req_in_ctx as an input parameter to <code>krb5_rd_req_ctx()</code>. The caller should free the context with krb5_rd_req_in_ctx_free() when done with the context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Keberos 5 context.<br />
 <i>ctx</i> in ctx to <code>krb5_rd_req_ctx()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Kerberos 5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_rd_req_in_set_keytab (krb5_contextcontext, krb5_rd_req_in_ctxin, krb5_keytabkeytab)</h3>
<p> Set the keytab that <code>krb5_rd_req_ctx()</code> will use. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Keberos 5 context.<br />
 <i>in</i> in ctx to <code>krb5_rd_req_ctx()</code>.<br />
 <i>keytab</i> keytab that <code>krb5_rd_req_ctx()</code> will use, only copy the pointer, so the caller must free they keytab after krb5_rd_req_in_ctx_free() is called.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Kerberos 5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_rd_req_in_set_pac_check (krb5_contextcontext, krb5_rd_req_in_ctxin, krb5_booleanflag)</h3>
<p> Set if krb5_rq_red() is going to check the Windows PAC or not </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Keberos 5 context.<br />
 <i>in</i> krb5_rd_req_in_ctx to check the option on.<br />
 <i>flag</i> flag to select if to check the pac (TRUE) or not (FALSE).</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Kerberos 5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_rd_req_out_ctx_free (krb5_contextcontext, krb5_rd_req_out_ctxctx)</h3>
<p> Free the krb5_rd_req_out_ctx. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Keberos 5 context.<br />
 <i>ctx</i> krb5_rd_req_out_ctx context to free.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_rd_req_out_get_server (krb5_contextcontext, krb5_rd_req_out_ctxout, krb5_principal *principal)</h3>
<p> Get the principal that was used in the request from the client. Might not match whats in the ticket if <code>krb5_rd_req_ctx()</code> searched in the keytab for a matching key. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Kerberos 5 context.<br />
 <i>out</i> a krb5_rd_req_out_ctx from <code>krb5_rd_req_ctx()</code>.<br />
 <i>principal</i> return principal, free with <code>krb5_free_principal()</code>.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for HeimdalKerberos5library from the source code. </p>
<h2>Index</h2>
