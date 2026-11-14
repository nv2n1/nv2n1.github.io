---
title: "strongimcv_pki-issue(1)"
name: "strongimcv_pki-issue"
section: "1"
letter: "s"
url: "/docs/linux/man/1-strongimcv_pki-issue/"
description: "pki –issue – Issue a certificate using a CA certificate and key"
---

<p>pki &#8211;issue &#8211; Issue a certificate using a CA certificate and key</p>
<h2>Synopsis</h2>
<p>[ <code>&#8211;in </code><i>file</i> ] [ <code>&#8211;type </code><i>type</i> ] <code>&#8211;cakey~</code><i>file</i><code>|&#8211;cakeyid~</code><i>hex</i> <code>&#8211;cacert~</code><i>file</i> [ <code>&#8211;dn </code><i>subject-dn</i> ] [ <code>&#8211;san </code><i>subjectAltName</i> ] [ <code>&#8211;lifetime </code><i>days</i> ] [ <code>&#8211;not-before </code><i>datetime</i> ] [ <code>&#8211;not-after </code><i>datetime</i> ] [ <code>&#8211;serial </code><i>hex</i> ] [ <code>&#8211;flag </code><i>flag</i> ] [ <code>&#8211;digest </code><i>digest</i> ] [ <code>&#8211;ca</code> ] [ <code>&#8211;crl </code><i>uri&nbsp;<wbr></i>[<code>&#8211;crlissuer&nbsp;<wbr></code><i>issuer</i>] ] [ <code>&#8211;ocsp </code><i>uri</i> ] [ <code>&#8211;pathlen </code><i>len</i> ] [ <code>&#8211;nc-permitted </code><i>name</i> ] [ <code>&#8211;nc-excluded </code><i>name</i> ] [ <code>&#8211;policy-mapping </code><i>mapping</i> ] [ <code>&#8211;policy-explicit </code><i>len</i> ] [ <code>&#8211;policy-inhibit </code><i>len</i> ] [ <code>&#8211;policy-any </code><i>len</i> ] [ <code>&#8211;cert-policy </code><i>oid&nbsp;<wbr></i>[<code>&#8211;cps-uri&nbsp;<wbr></code><i>uri</i>]&nbsp;<wbr>[<code>&#8211;user-notice&nbsp;<wbr></code><i>text</i>] ] [ <code>&#8211;outform </code><i>encoding</i> ] [ <code>&#8211;debug </code><i>level</i> ] <code>&#8211;options~</code><i>file</i> <code>-h</code> | <code>&#8211;help</code></p>
<h2>Description</h2>
<p>This sub-command of <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1) is used to issue a certificate using a CA certificate and private key.</p>
<h2>Options</h2>
<dl COMPACT>
<dt><code>-h, &#8211;help</code></p>
<dd>Print usage information with a summary of the available options.</p>
<dt><code>-v, &#8211;debug </code><i>level</i></p>
<dd>Set debug level, default: 1.</p>
<dt><code>-+, &#8211;options </code><i>file</i></p>
<dd>Read command line options from <i>file</i>.</p>
<dt><code>-i, &#8211;in </code><i>file</i></p>
<dd>Public key or PKCS#10 certificate request file to issue. If not given the key/request is read from <i>STDIN</i>.</p>
<dt><code>-t, &#8211;type </code><i>type</i></p>
<dd>Type of the input. Either <i>pub</i> for a public key, or <i>pkcs10</i> for a PKCS#10 certificate request, defaults to <i>pub</i>.</p>
<dt><code>-k, &#8211;cakey </code><i>file</i></p>
<dd>CA private key file. Either this or <code>&#8211;cakeyid</code> is required.</p>
<dt><code>-x, &#8211;cakeyid </code><i>hex</i></p>
<dd>Key ID of a CA private key on a smartcard. Either this or <code>&#8211;cakey</code> is required.</p>
<dt><code>-c, &#8211;cacert </code><i>file</i></p>
<dd>CA certificate file. Required.</p>
<dt><code>-d, &#8211;dn </code><i>subject-dn</i></p>
<dd>Subject distinguished name (DN) of the issued certificate.</p>
<dt><code>-a, &#8211;san </code><i>subjectAltName</i></p>
<dd>subjectAltName extension to include in certificate. Can be used multiple times.</p>
<dt><code>-l, &#8211;lifetime </code><i>days</i></p>
<dd>Days the certificate is valid, default: 1095. Ignored if both an absolute start and end time are given.</p>
<dt><code>-F, &#8211;not-before </code><i>datetime</i></p>
<dd>Absolute time when the validity of the certificate begins. The datetime format is defined by the <code>&#8211;dateform</code> option.</p>
<dt><code>-T, &#8211;not-after </code><i>datetime</i></p>
<dd>Absolute time when the validity of the certificate ends. The datetime format is defined by the <code>&#8211;dateform</code> option.</p>
<dt><code>-D, &#8211;dateform </code><i>form</i></p>
<dd><a href="/docs/linux/man/3-strptime/">strptime</a>(3) format for the <code>&#8211;not-before</code> and <code>&#8211;not-after</code> options, default: <code>%d.%m.%y %T</code></p>
<dt><code>-s, &#8211;serial </code><i>hex</i></p>
<dd>Serial number in hex. It is randomly allocated by default.</p>
<dt><code>-e, &#8211;flag </code><i>flag</i></p>
<dd>Add extendedKeyUsage flag. One of <i>serverAuth</i>, <i>clientAuth</i>, <i>crlSign</i>, or <i>ocspSigning</i>. Can be used multiple times.</p>
<dt><code>-g, &#8211;digest </code><i>digest</i></p>
<dd>Digest to use for signature creation. One of <i>md5</i>, <i>sha1</i>, <i>sha224</i>, <i>sha256</i>, <i>sha384</i>, or <i>sha512</i>. Defaults to <i>sha1</i>.</p>
<dt><code>-f, &#8211;outform </code><i>encoding</i></p>
<dd>Encoding of the created certificate file. Either <i>der</i> (ASN.1 DER) or <i>pem</i> (Base64 PEM), defaults to <i>der</i>.</p>
<dt><code>-b, &#8211;ca</code></p>
<dd>Include CA basicConstraint extension in certificate.</p>
<dt><code>-u, &#8211;crl </code><i>uri</i></p>
<dd>CRL distribution point URI to include in certificate. Can be used multiple times.</p>
<dt><code>-I, &#8211;crlissuer </code><i>issuer</i></p>
<dd>Optional CRL issuer for the CRL at the preceding distribution point.</p>
<dt><code>-o, &#8211;ocsp </code><i>uri</i></p>
<dd>OCSP AuthorityInfoAccess URI to include in certificate. Can be used multiple times.</p>
<dt><code>-p, &#8211;pathlen </code><i>len</i></p>
<dd>Set path length constraint.</p>
<dt><code>-n, &#8211;nc-permitted </code><i>name</i></p>
<dd>Add permitted NameConstraint extension to certificate.</p>
<dt><code>-N, &#8211;nc-excluded </code><i>name</i></p>
<dd>Add excluded NameConstraint extension to certificate.</p>
<dt><code>-M, &#8211;policy-mapping </code><i>issuer-oid:subject-oid</i></p>
<dd>Add policyMapping from issuer to subject OID.</p>
<dt><code>-E, &#8211;policy-explicit </code><i>len</i></p>
<dd>Add requireExplicitPolicy constraint.</p>
<dt><code>-H, &#8211;policy-inhibit </code><i>len</i></p>
<dd>Add inhibitPolicyMapping constraint.</p>
<dt><code>-A, &#8211;policy-any </code><i>len</i></p>
<dd>Add inhibitAnyPolicy constraint.</dl>
<h3>Certificate Policy</h3>
<p>Multiple certificatePolicy extensions can be added. Each with the following information:</p>
<dl COMPACT>
<dt><code>-P, &#8211;cert-policy </code><i>oid</i></p>
<dd>OID to include in certificatePolicy extension. Required.</p>
<dt><code>-C, &#8211;cps-uri </code><i>uri</i></p>
<dd>Certification Practice statement URI for certificatePolicy.</p>
<dt><code>-U, &#8211;user-notice </code><i>text</i></p>
<dd>User notice for certificatePolicy.</dl>
<h2>Examples</h2>
<p>To save repetitive typing, command line options can be stored in files. Lets assume <i>pki.opt</i> contains the following contents: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;cacert ca_cert.der &#8211;cakey ca_key.der &#8211;digest sha256<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;flag serverAuth &#8211;lifetime 1460 &#8211;type pkcs10 </p>
<p> Then the following command can be used to issue a certificate based on a given PKCS#10 certificate request and the options above: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pki &#8211;issue &#8211;options pki.opt &#8211;in req.der&nbsp;<wbr>&gt;&nbsp;<wbr>cert.der </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pki/">pki</a></code>(1)</p>
