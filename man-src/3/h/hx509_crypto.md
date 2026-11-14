---
title: "hx509_crypto(3)"
name: "hx509_crypto"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hx509_crypto/"
description: "hx509 crypto functions –"
---

<h2 class="name">NAME</h2>
<p> hx509 crypto functions &#8211; </p>
<h3>Functions</h3>
<p> int <code>hx509_verify_signature</code> (hx509_context context, const hx509_cert signer, const AlgorithmIdentifier *alg, const heim_octet_string *data, const heim_octet_string *sig) </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>int hx509_verify_signature (hx509_contextcontext, const hx509_certsigner, const AlgorithmIdentifier *alg, const heim_octet_string *data, const heim_octet_string *sig)</h3>
<p> Verify a signature made using the private key of an certificate. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>signer</i> the certificate that made the signature.<br />
 <i>alg</i> algorthm that was used to sign the data.<br />
 <i>data</i> the data that was signed.<br />
 <i>sig</i> the sigature to verify.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Heimdalx509library from the source code. </p>
<h2>Index</h2>
