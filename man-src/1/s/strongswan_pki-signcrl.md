---
title: "strongswan_pki-signcrl(1)"
name: "strongswan_pki-signcrl"
section: "1"
letter: "s"
url: "/docs/linux/man/1-strongswan_pki-signcrl/"
description: "pki –signcrl – Issue a Certificate Revocation List (CRL) using a CA certificate and key"
---

<p>pki &#8211;signcrl &#8211; Issue a Certificate Revocation List (CRL) using a CA certificate and key</p>
<h2>Synopsis</h2>
<p><code>&#8211;cakey~</code><i>file</i><code>|&#8211;cakeyid~</code><i>hex</i> <code>&#8211;cacert~</code><i>file</i> [ <code>&#8211;lifetime </code><i>days</i> ] [ <code>&#8211;this-update </code><i>datetime</i> ] [ <code>&#8211;next-update </code><i>datetime</i> ] [ <code>&#8211;lastcrl </code><i>crl</i> ] [ <code>&#8211;basecrl </code><i>crl</i> ] [ <code>&#8211;crluri </code><i>uri</i> ] [ <code>&#8211;digest </code><i>digest</i> ] [ [<code>&#8211;reason&nbsp;<wbr></code><i>reason</i>]&nbsp;<wbr>[<code>&#8211;date&nbsp;<wbr></code><i>ts</i>]&nbsp;<wbr><code>&#8211;cert&nbsp;<wbr></code><i>file</i><code>|&#8211;serial&nbsp;<wbr></code><i>hex</i> ] [ <code>&#8211;outform </code><i>encoding</i> ] [ <code>&#8211;debug </code><i>level</i> ] <code>&#8211;options~</code><i>file</i> <code>-h</code> | <code>&#8211;help</code></p>
<h2>Description</h2>
<p>This sub-command of <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1) is used to issue a Certificate Revocation List (CRL) using a CA certificate and private key.</p>
<h2>Options</h2>
<dl COMPACT>
<dt><code>-h, &#8211;help</code></p>
<dd>Print usage information with a summary of the available options.</p>
<dt><code>-v, &#8211;debug </code><i>level</i></p>
<dd>Set debug level, default: 1.</p>
<dt><code>-+, &#8211;options </code><i>file</i></p>
<dd>Read command line options from <i>file</i>.</p>
<dt><code>-k, &#8211;cakey </code><i>file</i></p>
<dd>CA private key file. Either this or <code>&#8211;cakeyid</code> is required.</p>
<dt><code>-x, &#8211;cakeyid </code><i>hex</i></p>
<dd>Smartcard or TPM CA private key object handle in hex format with an optional 0x prefix. Either this or <code>&#8211;cakey</code> is required.</p>
<dt><code>-c, &#8211;cacert </code><i>file</i></p>
<dd>CA certificate file. Required.</p>
<dt><code>-l, &#8211;lifetime </code><i>days</i></p>
<dd>Days until the CRL gets a nextUpdate, default: 15. Ignored if both an absolute start and end time are given.</p>
<dt><code>-F, &#8211;this-update </code><i>datetime</i></p>
<dd>Absolute time when the validity of the CRL begins. The datetime format is defined by the <code>&#8211;dateform</code> option.</p>
<dt><code>-T, &#8211;next-update </code><i>datetime</i></p>
<dd>Absolute time when the validity of the CRL end. The datetime format is defined by the <code>&#8211;dateform</code> option.</p>
<dt><code>-D, &#8211;dateform </code><i>form</i></p>
<dd><a href="/docs/linux/man/3-strptime/">strptime</a>(3) format for the <code>&#8211;this-update</code> and <code>&#8211;next-update</code> options, default: <code>%d.%m.%y %T</code></p>
<dt><code>-a, &#8211;lastcrl </code><i>crl</i></p>
<dd>CRL of lastUpdate to copy revocations from.</p>
<dt><code>-b, &#8211;basecrl </code><i>crl</i></p>
<dd>Base CRL to create a delta CRL for.</p>
<dt><code>-u, &#8211;crluri </code><i>uri</i></p>
<dd>Freshest delta CRL URI to include in CRL. Can be used multiple times.</p>
<dt><code>-g, &#8211;digest </code><i>digest</i></p>
<dd>Digest to use for signature creation. One of <i>md5</i>, <i>sha1</i>, <i>sha224</i>, <i>sha256</i>, <i>sha384</i>, or <i>sha512</i>. The default is determined based on the type and size of the signature key.</p>
<dt><code>-f, &#8211;outform </code><i>encoding</i></p>
<dd>Encoding of the created certificate file. Either <i>der</i> (ASN.1 DER) or <i>pem</i> (Base64 PEM), defaults to <i>der</i>.</dl>
<h3>Revoked Certificates</h3>
<p>Multiple revoked certificates can be added to the CRL by either providing the certificate file or the respective serial number directly. A reason and a timestamp can be configured for each revocation (they have to be given before each certificate/serial on the command line).</p>
<dl COMPACT>
<dt><code>-r, &#8211;reason </code><i>reason</i></p>
<dd>The reason why the certificate was revoked. One of <i>key-compromise</i>, <i>ca-compromise</i>, <i>affiliation-changed</i>, <i>superseded</i>, <i>cessation-of-operation</i>, or <i>certificate-hold</i>.</p>
<dt><code>-d, &#8211;date </code><i>ts</i></p>
<dd>Revocation date as Unix timestamp. Defaults to the current time.</p>
<dt><code>-z, &#8211;cert </code><i>file</i></p>
<dd>Certificate file to revoke.</p>
<dt><code>-s, &#8211;serial </code><i>hex</i></p>
<dd>Hexadecimal encoded serial number of the certificate to revoke.</dl>
<h2>Examples</h2>
<p>Revoke a certificate: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pki &#8211;signcrl &#8211;cacert ca_cert.der &#8211;cakey ca_key.der&nbsp;<wbr>\<br />
&#8211;reason superseded &#8211;cert cert.der&nbsp;<wbr>&gt;&nbsp;<wbr>crl.der </p>
<p> Update an existing CRL with two new revocations, using the certificate&#8217;s serial number, but no reason: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pki &#8211;signcrl &#8211;cacert ca_cert.der &#8211;cakey ca_key.der&nbsp;<wbr>\<br />
&#8211;lastcrl old_crl.der &#8211;serial 0123 &#8211;serial 0345&nbsp;<wbr>&gt;&nbsp;<wbr>crl.der </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pki/">pki</a></code>(1)</p>
