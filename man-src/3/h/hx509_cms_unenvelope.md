---
title: "hx509_cms_unenvelope(3)"
name: "hx509_cms_unenvelope"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hx509_cms_unenvelope/"
description: "hx509 CMS/pkcs7 functions –"
---

<h2 class="name">NAME</h2>
<p> hx509 CMS/pkcs7 functions &#8211; </p>
<h3>Functions</h3>
<p> int <code>hx509_cms_wrap_ContentInfo</code> (const heim_oid *oid, const heim_octet_string *buf, heim_octet_string *res) </p>
<p> int <code>hx509_cms_unwrap_ContentInfo</code> (const heim_octet_string *in, heim_oid *oid, heim_octet_string *out, int *have_data) </p>
<p> int <code>hx509_cms_unenvelope</code> (hx509_context context, hx509_certs certs, int flags, const void *data, size_t length, const heim_octet_string *encryptedContent, time_t time_now, heim_oid *contentType, heim_octet_string *content) </p>
<p> int <code>hx509_cms_envelope_1</code> (hx509_context context, int flags, hx509_cert cert, const void *data, size_t length, const heim_oid *encryption_type, const heim_oid *contentType, heim_octet_string *content) </p>
<p> int <code>hx509_cms_verify_signed</code> (hx509_context context, hx509_verify_ctx ctx, unsigned int flags, const void *data, size_t length, const heim_octet_string *signedContent, hx509_certs pool, heim_oid *contentType, heim_octet_string *content, hx509_certs *signer_certs) </p>
<p> int <code>hx509_cms_create_signed_1</code> (hx509_context context, int flags, const heim_oid *eContentType, const void *data, size_t length, const AlgorithmIdentifier *digest_alg, hx509_cert cert, hx509_peer_info peer, hx509_certs anchors, hx509_certs pool, heim_octet_string *signed_data) </p>
<h2>Detailed Description</h2>
<p> See the <code>CMS/PKCS7 message functions.</code> for description and examples.</p>
<h2>Function Documentation</h2>
<h3>int hx509_cms_create_signed_1 (hx509_contextcontext, intflags, const heim_oid *eContentType, const void *data, size_tlength, const AlgorithmIdentifier *digest_alg, hx509_certcert, hx509_peer_infopeer, hx509_certsanchors, hx509_certspool, heim_octet_string *signed_data)</h3>
<p> Decode SignedData and verify that the signature is correct. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>flags</i><br />
 <i>eContentType</i> the type of the data.<br />
 <i>data</i> data to sign<br />
 <i>length</i> length of the data that data point to.<br />
 <i>digest_alg</i> digest algorithm to use, use NULL to get the default or the peer determined algorithm.<br />
 <i>cert</i> certificate to use for sign the data.<br />
 <i>peer</i> info about the peer the message to send the message to, like what digest algorithm to use.<br />
 <i>anchors</i> trust anchors that the client will use, used to polulate the certificates included in the message<br />
 <i>pool</i> certificates to use in try to build the path to the trust anchors.<br />
 <i>signed_data</i> the output of the function, free with der_free_octet_string().</dl>
<h3>int hx509_cms_envelope_1 (hx509_contextcontext, intflags, hx509_certcert, const void *data, size_tlength, const heim_oid *encryption_type, const heim_oid *contentType, heim_octet_string *content)</h3>
<p> Encrypt end encode EnvelopedData. </p>
<p> Encrypt and encode EnvelopedData. The data is encrypted with a random key and the the random key is encrypted with the certificates private key. This limits what private key type can be used to RSA. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>flags</i> flags to control the behavior.</p>
<dl>
<dt>&bull;</p>
<dd> HX509_CMS_EV_NO_KU_CHECK &#8211; Dont check KU on certificate</p>
<dt>&bull;</p>
<dd> HX509_CMS_EV_ALLOW_WEAK &#8211; Allow weak crytpo</p>
<dt>&bull;</p>
<dd> HX509_CMS_EV_ID_NAME &#8211; prefer issuer name and serial number</dl>
<p> <i>cert</i> Certificate to encrypt the EnvelopedData encryption key with.<br />
 <i>data</i> pointer the data to encrypt.<br />
 <i>length</i> length of the data that data point to.<br />
 <i>encryption_type</i> Encryption cipher to use for the bulk data, use NULL to get default.<br />
 <i>contentType</i> type of the data that is encrypted<br />
 <i>content</i> the output of the function, free with der_free_octet_string().</dl>
<h3>int hx509_cms_unenvelope (hx509_contextcontext, hx509_certscerts, intflags, const void *data, size_tlength, const heim_octet_string *encryptedContent, time_ttime_now, heim_oid *contentType, heim_octet_string *content)</h3>
<p> Decode and unencrypt EnvelopedData. </p>
<p> Extract data and parameteres from from the EnvelopedData. Also supports using detached EnvelopedData. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>certs</i> Certificate that can decrypt the EnvelopedData encryption key.<br />
 <i>flags</i> HX509_CMS_UE flags to control the behavior.<br />
 <i>data</i> pointer the structure the contains the DER/BER encoded EnvelopedData stucture.<br />
 <i>length</i> length of the data that data point to.<br />
 <i>encryptedContent</i> in case of detached signature, this contains the actual encrypted data, othersize its should be NULL.<br />
 <i>time_now</i> set the current time, if zero the library uses now as the date.<br />
 <i>contentType</i> output type oid, should be freed with der_free_oid().<br />
 <i>content</i> the data, free with der_free_octet_string().</dl>
<h3>int hx509_cms_unwrap_ContentInfo (const heim_octet_string *in, heim_oid *oid, heim_octet_string *out, int *have_data)</h3>
<p> Decode an ContentInfo and unwrap data and oid it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>in</i> the encoded buffer.<br />
 <i>oid</i> type of the content.<br />
 <i>out</i> data to be wrapped.<br />
 <i>have_data</i> since the data is optional, this flags show dthe diffrence between no data and the zero length data.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns an hx509 error code.</dl>
<h3>int hx509_cms_verify_signed (hx509_contextcontext, hx509_verify_ctxctx, unsigned intflags, const void *data, size_tlength, const heim_octet_string *signedContent, hx509_certspool, heim_oid *contentType, heim_octet_string *content, hx509_certs *signer_certs)</h3>
<p> Decode SignedData and verify that the signature is correct. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>ctx</i> a hx509 verify context.<br />
 <i>flags</i> to control the behaivor of the function.</p>
<dl>
<dt>&bull;</p>
<dd> HX509_CMS_VS_NO_KU_CHECK &#8211; Don&#8217;t check KeyUsage</p>
<dt>&bull;</p>
<dd> HX509_CMS_VS_ALLOW_DATA_OID_MISMATCH &#8211; allow oid mismatch</p>
<dt>&bull;</p>
<dd> HX509_CMS_VS_ALLOW_ZERO_SIGNER &#8211; no signer, see below.</dl>
<p> <i>data</i> pointer to CMS SignedData encoded data.<br />
 <i>length</i> length of the data that data point to.<br />
 <i>signedContent</i> external data used for signature.<br />
 <i>pool</i> certificate pool to build certificates paths.<br />
 <i>contentType</i> free with der_free_oid().<br />
 <i>content</i> the output of the function, free with der_free_octet_string().<br />
 <i>signer_certs</i> list of the cerficates used to sign this request, free with <code>hx509_certs_free()</code>.</dl>
<p> If HX509_CMS_VS_NO_KU_CHECK is set, allow more liberal search for matching certificates by not considering KeyUsage bits on the certificates. </p>
<p> If HX509_CMS_VS_ALLOW_DATA_OID_MISMATCH, allow encapContentInfo mismatch with the oid in signedAttributes (or if no signedAttributes where use, pkcs7-data oid). This is only needed to work with broken CMS implementations that doesn&#8217;t follow CMS signedAttributes rules. </p>
<p> If HX509_CMS_VS_NO_VALIDATE flags is set, do not verify the signing certificates and leave that up to the caller. </p>
<p> If HX509_CMS_VS_ALLOW_ZERO_SIGNER is set, allow empty SignerInfo (no signatures). If SignedData have no signatures, the function will return 0 with signer_certs set to NULL. Zero signers is allowed by the standard, but since its only useful in corner cases, it make into a flag that the caller have to turn on.</p>
<h3>int hx509_cms_wrap_ContentInfo (const heim_oid *oid, const heim_octet_string *buf, heim_octet_string *res)</h3>
<p> Wrap data and oid in a ContentInfo and encode it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>oid</i> type of the content.<br />
 <i>buf</i> data to be wrapped. If a NULL pointer is passed in, the optional content field in the ContentInfo is not going be filled in.<br />
 <i>res</i> the encoded buffer, the result should be freed with der_free_octet_string().</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns an hx509 error code.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Heimdalx509library from the source code. </p>
<h2>Index</h2>
