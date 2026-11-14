---
title: "strongimcv_pki(1)"
name: "strongimcv_pki"
section: "1"
letter: "s"
url: "/docs/linux/man/1-strongimcv_pki/"
description: "pki – Simple public key infrastructure (PKI) management tool"
---

<h2>NAME</h2>
<p> pki &#8211; Simple public key infrastructure (PKI) management tool</p>
<h2>SYNOPSIS</h2>
<p> <i>command</i> [<i>option~</i>&#8230;] <code>-h</code> | <code>&#8211;help</code></p>
<h2>DESCRIPTION</h2>
<p> <code>pki</code> is a suite of commands that allow you to manage a simple public key infrastructure (PKI). </p>
<p> Generate RSA and ECDSA key pairs, create PKCS#10 certificate requests containing subjectAltNames, create X.509 self-signed end-entity and root CA certificates, issue end-entity and intermediate CA certificates signed by the private key of a CA and containing subjectAltNames, CRL distribution points and URIs of OCSP servers. You can also extract raw public keys from private keys, certificate requests and certificates and compute two kinds of SHA-1-based key IDs.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Prints usage information and a short summary of the available commands.</p>
<dt><code>-g, &#8211;gen</code></p>
<dd> Generate a new private key.</p>
<dt><code>-s, &#8211;self</code></p>
<dd> Create a self-signed certificate.</p>
<dt><code>-i, &#8211;issue</code></p>
<dd> Issue a certificate using a CA certificate and key.</p>
<dt><code>-c, &#8211;signcrl</code></p>
<dd> Issue a CRL using a CA certificate and key.</p>
<dt><code>-z, &#8211;acert</code></p>
<dd> Issue an attribute certificate.</p>
<dt><code>-r, &#8211;req</code></p>
<dd> Create a PKCS#10 certificate request.</p>
<dt><code>-7, &#8211;pkcs7</code></p>
<dd> Provides PKCS#7 wrap/unwrap functions.</p>
<dt><code>-k, &#8211;keyid</code></p>
<dd> Calculate key identifiers of a key or certificate.</p>
<dt><code>-a, &#8211;print</code></p>
<dd> Print a credential (key, certificate etc.) in human readable form.</p>
<dt><code>-p, &#8211;pub</code></p>
<dd> Extract a public key from a private key or certificate.</p>
<dt><code>-v, &#8211;verify</code></p>
<dd> Verify a certificate using a CA certificate.</dl>
<h2>EXAMPLES</h2>
<h3>Generating a CA Certificate</h3>
<p> The first step is to generate a private key using the <code>&#8211;gen</code> command. By default this generates a 2048-bit RSA key. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pki &#8211;gen&nbsp;<wbr>&gt;&nbsp;<wbr>ca_key.der </p>
<p> This key is used to create the self-signed CA certificate, using the <code>&#8211;self</code> command. The distinguished name should be adjusted to your needs. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pki &#8211;self &#8211;ca &#8211;in ca_key.der&nbsp;<wbr>\<br />
&#8211;dn&nbsp;<wbr>&quot;C=CH, O=strongSwan, CN=strongSwan CA&quot;&nbsp;<wbr>&gt;&nbsp;<wbr>ca_cert.der </p>
<h3>Generating End-Entity Certificates</h3>
<p> With the root CA certificate and key at hand end-entity certificates for clients and servers can be issued. Similarly intermediate CA certificates can be issued, which in turn can issue other certificates. To generate a certificate for a server, we start by generating a private key. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pki &#8211;gen&nbsp;<wbr>&gt;&nbsp;<wbr>server_key.der </p>
<p> The public key will be included in the certificate so lets extract that from the private key. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pki &#8211;pub &#8211;in server_key.der&nbsp;<wbr>&gt;&nbsp;<wbr>server_pub.der </p>
<p> The following command will use the CA certificate and private key to issue the certificate for this server. Adjust the distinguished name, subjectAltName(s) and flags as needed (check <code>pki&nbsp;<wbr><a href="/docs/linux/man/8---issue/">&#8211;issue</a></code>(8) for more options). </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pki &#8211;issue &#8211;in server_pub.der &#8211;cacert ca_cert.der&nbsp;<wbr>\<br />
&#8211;cakey ca_key.der &#8211;dn&nbsp;<wbr>&quot;C=CH, O=strongSwan, CN=VPN Server&quot;&nbsp;<wbr>\<br />
&#8211;san vpn.strongswan.org &#8211;flag serverAuth&nbsp;<wbr>&gt;&nbsp;<wbr>server_cert.der </p>
<p> Instead of storing the public key in a separate file, the output of <code>&#8211;pub</code> may also be piped directly into the above command.</p>
<h3>Generating Certificate Revocation Lists (CRL)</h3>
<p> If end-entity certificates have to be revoked, CRLs may be generated using the <code>&#8211;signcrl</code> command. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pki &#8211;signcrl &#8211;cacert ca_cert.der &#8211;cakey ca_key.der&nbsp;<wbr>\<br />
&#8211;reason superseded &#8211;cert server_cert.der&nbsp;<wbr>&gt;&nbsp;<wbr>crl.der </p>
<p> The certificate given with &#8211;cacert must be either a CA certificate or a certificate with the <i>crlSign</i> extended key usage (&#8211;flag crlSign). URIs to CRLs may be included in issued certificates with the &#8211;crl option.</p>
<h2>SEE ALSO</h2>
<p> <code>pki&nbsp;<wbr><a href="/docs/linux/man/1---gen/">&#8211;gen</a></code>(1), <code>pki&nbsp;<wbr><a href="/docs/linux/man/1---self/">&#8211;self</a></code>(1), <code>pki&nbsp;<wbr><a href="/docs/linux/man/1---issue/">&#8211;issue</a></code>(1), <code>pki&nbsp;<wbr><a href="/docs/linux/man/1---signcrl/">&#8211;signcrl</a></code>(1), <code>pki&nbsp;<wbr><a href="/docs/linux/man/1---acert/">&#8211;acert</a></code>(1), <code>pki&nbsp;<wbr><a href="/docs/linux/man/1---req/">&#8211;req</a></code>(1), <code>pki&nbsp;<wbr><a href="/docs/linux/man/1---pkcs7/">&#8211;pkcs7</a></code>(1), <code>pki&nbsp;<wbr><a href="/docs/linux/man/1---keyid/">&#8211;keyid</a></code>(1), <code>pki&nbsp;<wbr><a href="/docs/linux/man/1---print/">&#8211;print</a></code>(1), <code>pki&nbsp;<wbr><a href="/docs/linux/man/1---pub/">&#8211;pub</a></code>(1), <code>pki&nbsp;<wbr><a href="/docs/linux/man/1---verify/">&#8211;verify</a></code>(1) </p>
<h2>Index</h2>
