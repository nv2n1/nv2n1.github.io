---

title: "strongswan_pki(1)"
name: "strongswan_pki"
section: "1"
letter: "s"
url: "/docs/linux/man/1-strongswan_pki/"
description: "pki – Simple public key infrastructure (PKI) management tool"
---

<p> pki &#8211; Simple public key infrastructure (PKI) management tool</p>
<h2>SYNOPSIS</h2>
<p> <i>command</i> [<i>option~</i>&#8230;] <code>-h</code> | <code>&#8211;help</code></p>
<h2>DESCRIPTION</h2>
<p> <code>pki</code> is a suite of commands that allow you to manage a simple public key infrastructure (PKI). </p>
<p> Generate RSA and ECDSA key pairs, create PKCS#10 certificate requests containing subjectAltNames, create X.509 self-signed end-entity and root CA certificates, issue end-entity and intermediate CA certificates signed by the private key of a CA and containing subjectAltNames, CRL distribution points and URIs of OCSP servers. You can also extract raw public keys from private keys, certificate requests and certificates and compute two kinds of SHA-1-based key IDs.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Prints usage information and a short summary of the available commands.</dd>
<dt><code>-g, &#8211;gen</code></dt>
<dd> Generate a new private key.</dd>
<dt><code>-s, &#8211;self</code></dt>
<dd> Create a self-signed certificate.</dd>
<dt><code>-i, &#8211;issue</code></dt>
<dd> Issue a certificate using a CA certificate and key.</dd>
<dt><code>-c, &#8211;signcrl</code></dt>
<dd> Issue a CRL using a CA certificate and key.</dd>
<dt><code>-z, &#8211;acert</code></dt>
<dd> Issue an attribute certificate.</dd>
<dt><code>-r, &#8211;req</code></dt>
<dd> Create a PKCS#10 certificate request.</dd>
<dt><code>-7, &#8211;pkcs7</code></dt>
<dd> Provides PKCS#7 wrap/unwrap functions.</dd>
<dt><code>-k, &#8211;keyid</code></dt>
<dd> Calculate key identifiers of a key or certificate.</dd>
<dt><code>-a, &#8211;print</code></dt>
<dd> Print a credential (key, certificate etc.) in human readable form.</dd>
<dt><code>-d, &#8211;dn</code></dt>
<dd> Extract the subject DN of an X.509 certificate.</dd>
<dt><code>-p, &#8211;pub</code></dt>
<dd> Extract a public key from a private key or certificate.</dd>
<dt><code>-v, &#8211;verify</code></dt>
<dd> Verify a certificate using a CA certificate.</dd></dl>
<h2>EXAMPLES</h2>
<h3>Generating a CA Certificate</h3>
<p> The first step is to generate a private key using the <code>&#8211;gen</code> command. By default this generates a 2048-bit RSA key. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pki &#8211;gen&nbsp;<wbr>&gt;&nbsp;<wbr>ca_key.der </p>
<p> This key is used to create the self-signed CA certificate, using the <code>&#8211;self</code> command. The distinguished name should be adjusted to your needs. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pki &#8211;self &#8211;ca &#8211;in ca_key.der&nbsp;<wbr>\<br/>
&#8211;dn&nbsp;<wbr>&quot;C=CH, O=strongSwan, CN=strongSwan CA&quot;&nbsp;<wbr>&gt;&nbsp;<wbr>ca_cert.der </p>
<h3>Generating End-Entity Certificates</h3>
<p> With the root CA certificate and key at hand end-entity certificates for clients and servers can be issued. Similarly intermediate CA certificates can be issued, which in turn can issue other certificates. To generate a certificate for a server, we start by generating a private key. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pki &#8211;gen&nbsp;<wbr>&gt;&nbsp;<wbr>server_key.der </p>
<p> The public key will be included in the certificate so lets extract that from the private key. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pki &#8211;pub &#8211;in server_key.der&nbsp;<wbr>&gt;&nbsp;<wbr>server_pub.der </p>
<p> The following command will use the CA certificate and private key to issue the certificate for this server. Adjust the distinguished name, subjectAltName(s) and flags as needed (check <code>pki&nbsp;<wbr>&#8211;issue</code>(8) for more options). </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pki &#8211;issue &#8211;in server_pub.der &#8211;cacert ca_cert.der&nbsp;<wbr>\<br/>
&#8211;cakey ca_key.der &#8211;dn&nbsp;<wbr>&quot;C=CH, O=strongSwan, CN=VPN Server&quot;&nbsp;<wbr>\<br/>
&#8211;san vpn.strongswan.org &#8211;flag serverAuth&nbsp;<wbr>&gt;&nbsp;<wbr>server_cert.der </p>
<p> Instead of storing the public key in a separate file, the output of <code>&#8211;pub</code> may also be piped directly into the above command.</p>
<h3>Generating Certificate Revocation Lists (CRL)</h3>
<p> If end-entity certificates have to be revoked, CRLs may be generated using the <code>&#8211;signcrl</code> command. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pki &#8211;signcrl &#8211;cacert ca_cert.der &#8211;cakey ca_key.der&nbsp;<wbr>\<br/>
&#8211;reason superseded &#8211;cert server_cert.der&nbsp;<wbr>&gt;&nbsp;<wbr>crl.der </p>
<p> The certificate given with &#8211;cacert must be either a CA certificate or a certificate with the <i>crlSign</i> extended key usage (&#8211;flag crlSign). URIs to CRLs may be included in issued certificates with the &#8211;crl option.</p>
<h2>SEE ALSO</h2>
<p> <code>pki&nbsp;<wbr>&#8211;gen</code>(1), <code>pki&nbsp;<wbr>&#8211;self</code>(1), <code>pki&nbsp;<wbr>&#8211;issue</code>(1), <code>pki&nbsp;<wbr>&#8211;signcrl</code>(1), <code>pki&nbsp;<wbr>&#8211;acert</code>(1), <code>pki&nbsp;<wbr>&#8211;req</code>(1), <code>pki&nbsp;<wbr>&#8211;pkcs7</code>(1), <code>pki&nbsp;<wbr>&#8211;keyid</code>(1), <code>pki&nbsp;<wbr>&#8211;print</code>(1), <code>pki&nbsp;<wbr>&#8211;dn</code>(1), <code>pki&nbsp;<wbr>&#8211;pub</code>(1), <code>pki&nbsp;<wbr>&#8211;verify</code>(1) </p>
