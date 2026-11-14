---
title: "hx509_revoke(3)"
name: "hx509_revoke"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hx509_revoke/"
description: "hx509 revokation checking functions –"
---

<h2 class="name">NAME</h2>
<p> hx509 revokation checking functions &#8211; </p>
<h3>Functions</h3>
<p> int <code>hx509_ocsp_request</code> (hx509_context, hx509_certs, hx509_certs, hx509_cert, const AlgorithmIdentifier *, heim_octet_string *, heim_octet_string *) </p>
<p> int <code>hx509_revoke_add_crl</code> (hx509_context, hx509_revoke_ctx, const char *) </p>
<p> int <code>hx509_revoke_add_ocsp</code> (hx509_context, hx509_revoke_ctx, const char *) </p>
<p> void <code>hx509_revoke_free</code> (hx509_revoke_ctx *) </p>
<p> int <code>hx509_revoke_init</code> (hx509_context, hx509_revoke_ctx *) </p>
<p> int <code>hx509_revoke_ocsp_print</code> (hx509_context, const char *, FILE *) </p>
<p> int <code>hx509_revoke_verify</code> (hx509_context, hx509_revoke_ctx, hx509_certs, time_t, hx509_cert, hx509_cert) </p>
<h2>Detailed Description</h2>
<p> See the <code>Revocation methods</code> for description and examples.</p>
<h2>Function Documentation</h2>
<h3>int hx509_ocsp_request (hx509_contextcontext, hx509_certsreqcerts, hx509_certspool, hx509_certsigner, const AlgorithmIdentifier *digest, heim_octet_string *request, heim_octet_string *nonce)</h3>
<p> Create an OCSP request for a set of certificates. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context<br />
 <i>reqcerts</i> list of certificates to request ocsp data for<br />
 <i>pool</i> certificate pool to use when signing<br />
 <i>signer</i> certificate to use to sign the request<br />
 <i>digest</i> the signing algorithm in the request, if NULL use the default signature algorithm,<br />
 <i>request</i> the encoded request, free with free_heim_octet_string().<br />
 <i>nonce</i> nonce in the request, free with free_heim_octet_string().</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_revoke_add_crl (hx509_contextcontext, hx509_revoke_ctxctx, const char *path)</h3>
<p> Add a CRL file to the revokation context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> hx509 context<br />
 <i>ctx</i> hx509 revokation context<br />
 <i>path</i> path to file that is going to be added to the context.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_revoke_add_ocsp (hx509_contextcontext, hx509_revoke_ctxctx, const char *path)</h3>
<p> Add a OCSP file to the revokation context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> hx509 context<br />
 <i>ctx</i> hx509 revokation context<br />
 <i>path</i> path to file that is going to be added to the context.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>void hx509_revoke_free (hx509_revoke_ctx *ctx)</h3>
<p> Free a hx509 revokation context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ctx</i> context to be freed</dl>
<h3>int hx509_revoke_init (hx509_contextcontext, hx509_revoke_ctx *ctx)</h3>
<p> Allocate a revokation context. Free with <code>hx509_revoke_free()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>ctx</i> returns a newly allocated revokation context.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_revoke_ocsp_print (hx509_contextcontext, const char *path, FILE *out)</h3>
<p> Print the OCSP reply stored in a file. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context<br />
 <i>path</i> path to a file with a OCSP reply<br />
 <i>out</i> the out FILE descriptor to print the reply on</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_revoke_verify (hx509_contextcontext, hx509_revoke_ctxctx, hx509_certscerts, time_tnow, hx509_certcert, hx509_certparent_cert)</h3>
<p> Check that a certificate is not expired according to a revokation context. Also need the parent certificte to the check OCSP parent identifier. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> hx509 context<br />
 <i>ctx</i> hx509 revokation context<br />
 <i>certs</i><br />
 <i>now</i><br />
 <i>cert</i><br />
 <i>parent_cert</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Heimdalx509library from the source code. </p>
<h2>Index</h2>
