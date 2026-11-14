---
title: "hx509_verify_path(3)"
name: "hx509_verify_path"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hx509_verify_path/"
description: "hx509 verification functions –"
---

<h2 class="name">NAME</h2>
<p> hx509 verification functions &#8211; </p>
<h3>Functions</h3>
<p> void <code>hx509_context_set_missing_revoke</code> (hx509_context context, int flag) </p>
<p> int <code>hx509_verify_init_ctx</code> (hx509_context context, hx509_verify_ctx *ctx) </p>
<p> void <code>hx509_verify_destroy_ctx</code> (hx509_verify_ctx ctx) </p>
<p> void <code>hx509_verify_attach_anchors</code> (hx509_verify_ctx ctx, hx509_certs set) </p>
<p> void <code>hx509_verify_attach_revoke</code> (hx509_verify_ctx ctx, hx509_revoke_ctx revoke_ctx) </p>
<p> void <code>hx509_verify_set_time</code> (hx509_verify_ctx ctx, time_t t) </p>
<p> void <code>hx509_verify_set_max_depth</code> (hx509_verify_ctx ctx, unsigned int max_depth) </p>
<p> void <code>hx509_verify_set_proxy_certificate</code> (hx509_verify_ctx ctx, int boolean) </p>
<p> void <code>hx509_verify_set_strict_rfc3280_verification</code> (hx509_verify_ctx ctx, int boolean) </p>
<p> int <code>hx509_verify_path</code> (hx509_context context, hx509_verify_ctx ctx, hx509_cert cert, hx509_certs pool) </p>
<p> int <code>hx509_crl_add_revoked_certs</code> (hx509_context, hx509_crl, hx509_certs) </p>
<p> int <code>hx509_crl_alloc</code> (hx509_context, hx509_crl *) </p>
<p> void <code>hx509_crl_free</code> (hx509_context, hx509_crl *) </p>
<p> int <code>hx509_crl_lifetime</code> (hx509_context, hx509_crl, int) </p>
<p> int <code>hx509_crl_sign</code> (hx509_context, hx509_cert, hx509_crl, heim_octet_string *) </p>
<p> int <code>hx509_ocsp_verify</code> (hx509_context, time_t, hx509_cert, int, const void *, size_t, time_t *) </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>void hx509_context_set_missing_revoke (hx509_contextcontext, intflag)</h3>
<p> Selects if the <code>hx509_revoke_verify()</code> function is going to require the existans of a revokation method (OCSP, CRL) or not. Note that <code>hx509_verify_path()</code>, <code>hx509_cms_verify_signed()</code>, and other function call <code>hx509_revoke_verify()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> hx509 context to change the flag for.<br />
 <i>flag</i> zero, revokation method required, non zero missing revokation method ok</dl>
<h3>int hx509_crl_add_revoked_certs (hx509_contextcontext, hx509_crlcrl, hx509_certscerts)</h3>
<p> Add revoked certificate to an CRL context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context.<br />
 <i>crl</i> the CRL to add the revoked certificate to.<br />
 <i>certs</i> keyset of certificate to revoke.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_crl_alloc (hx509_contextcontext, hx509_crl *crl)</h3>
<p> Create a CRL context. Use <code>hx509_crl_free()</code> to free the CRL context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context.<br />
 <i>crl</i> return pointer to a newly allocated CRL context.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>void hx509_crl_free (hx509_contextcontext, hx509_crl *crl)</h3>
<p> Free a CRL context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context.<br />
 <i>crl</i> a CRL context to free.</dl>
<h3>int hx509_crl_lifetime (hx509_contextcontext, hx509_crlcrl, intdelta)</h3>
<p> Set the lifetime of a CRL context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context.<br />
 <i>crl</i> a CRL context<br />
 <i>delta</i> delta time the certificate is valid, library adds the current time to this.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_crl_sign (hx509_contextcontext, hx509_certsigner, hx509_crlcrl, heim_octet_string *os)</h3>
<p> Sign a CRL and return an encode certificate. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context.<br />
 <i>signer</i> certificate to sign the CRL with<br />
 <i>crl</i> the CRL to sign<br />
 <i>os</i> return the signed and encoded CRL, free with free_heim_octet_string()</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_ocsp_verify (hx509_contextcontext, time_tnow, hx509_certcert, intflags, const void *data, size_tlength, time_t *expiration)</h3>
<p> Verify that the certificate is part of the OCSP reply and it&#8217;s not expired. Doesn&#8217;t verify signature the OCSP reply or it&#8217;s done by a authorized sender, that is assumed to be already done. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a hx509 context<br />
 <i>now</i> the time right now, if 0, use the current time.<br />
 <i>cert</i> the certificate to verify<br />
 <i>flags</i> flags control the behavior<br />
 <i>data</i> pointer to the encode ocsp reply<br />
 <i>length</i> the length of the encode ocsp reply<br />
 <i>expiration</i> return the time the OCSP will expire and need to be rechecked.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>void hx509_verify_attach_anchors (hx509_verify_ctxctx, hx509_certsset)</h3>
<p> Set the trust anchors in the verification context, makes an reference to the keyset, so the consumer can free the keyset independent of the destruction of the verification context (ctx). If there already is a keyset attached, it&#8217;s released. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ctx</i> a verification context<br />
 <i>set</i> a keyset containing the trust anchors.</dl>
<h3>void hx509_verify_attach_revoke (hx509_verify_ctxctx, hx509_revoke_ctxrevoke_ctx)</h3>
<p> Attach an revocation context to the verfication context, , makes an reference to the revoke context, so the consumer can free the revoke context independent of the destruction of the verification context. If there is no revoke context, the verification process is NOT going to check any verification status. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ctx</i> a verification context.<br />
 <i>revoke_ctx</i> a revoke context.</dl>
<h3>void hx509_verify_destroy_ctx (hx509_verify_ctxctx)</h3>
<p> Free an hx509 verification context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ctx</i> the context to be freed.</dl>
<h3>int hx509_verify_init_ctx (hx509_contextcontext, hx509_verify_ctx *ctx)</h3>
<p> Allocate an verification context that is used fo control the verification process. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>ctx</i> returns a pointer to a hx509_verify_ctx object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_verify_path (hx509_contextcontext, hx509_verify_ctxctx, hx509_certcert, hx509_certspool)</h3>
<p> Build and verify the path for the certificate to the trust anchor specified in the verify context. The path is constructed from the certificate, the pool and the trust anchors. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>ctx</i> A hx509 verification context.<br />
 <i>cert</i> the certificate to build the path from.<br />
 <i>pool</i> A keyset of certificates to build the chain from.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>void hx509_verify_set_max_depth (hx509_verify_ctxctx, unsigned intmax_depth)</h3>
<p> Set the maximum depth of the certificate chain that the path builder is going to try. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ctx</i> a verification context<br />
 <i>max_depth</i> maxium depth of the certificate chain, include trust anchor.</dl>
<h3>void hx509_verify_set_proxy_certificate (hx509_verify_ctxctx, intboolean)</h3>
<p> Allow or deny the use of proxy certificates </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ctx</i> a verification context<br />
 <i>boolean</i> if non zero, allow proxy certificates.</dl>
<h3>void hx509_verify_set_strict_rfc3280_verification (hx509_verify_ctxctx, intboolean)</h3>
<p> Select strict RFC3280 verification of certificiates. This means checking key usage on CA certificates, this will make version 1 certificiates unuseable. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ctx</i> a verification context<br />
 <i>boolean</i> if non zero, use strict verification.</dl>
<h3>void hx509_verify_set_time (hx509_verify_ctxctx, time_tt)</h3>
<p> Set the clock time the the verification process is going to use. Used to check certificate in the past and future time. If not set the current time will be used. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ctx</i> a verification context.<br />
 <i>t</i> the time the verifiation is using.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Heimdalx509library from the source code. </p>
<h2>Index</h2>
