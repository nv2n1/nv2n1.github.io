---
title: "xmlsec1(1)"
name: "xmlsec1"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmlsec1/"
description: "xmlsec1 – sign, verify, encrypt and decrypt XML documents"
---

<h2>NAME</h2>
<p> xmlsec1 &#8211; sign, verify, encrypt and decrypt XML documents</p>
<h2>SYNOPSIS</h2>
<p> <code>xmlsec</code> <i>&lt;command&gt; </i>[<i>&lt;options&gt;</i>] [<i>&lt;files&gt;</i>]</p>
<h2>DESCRIPTION</h2>
<p> xmlsec is a command line tool for signing, verifying, encrypting and decrypting XML documents. The allowed &lt;command&gt; values are:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> display this help information and exit</p>
<dt><code>&#8211;help-all</code></p>
<dd> display help information for all commands/options and exit</p>
<dt><code>&#8211;help-</code>&lt;cmd&gt;</p>
<dd> display help information for command &lt;cmd&gt; and exit</p>
<dt><code>&#8211;version</code></p>
<dd> print version information and exit</p>
<dt><code>&#8211;keys</code></p>
<dd> keys XML file manipulation</p>
<dt><code>&#8211;sign</code></p>
<dd> sign data and output XML document</p>
<dt><code>&#8211;verify</code></p>
<dd> verify signed document</p>
<dt><code>&#8211;sign-tmpl</code></p>
<dd> create and sign dynamicaly generated signature template</p>
<dt><code>&#8211;encrypt</code></p>
<dd> encrypt data and output XML document</p>
<dt><code>&#8211;decrypt</code></p>
<dd> decrypt data from XML document</dl>
<h2>OPTIONS</h2>
<dl>
<dt> <code>&#8211;ignore-manifests</code></p>
<dt>
<dd>
<dd>do not process &lt;dsig:Manifest&gt; elements</p>
<dt> <code>&#8211;store-references</code></p>
<dt>
<dd>
<dd>store and print the result of &lt;dsig:Reference/&gt; element processing just before calculating digest</p>
<dt> <code>&#8211;store-signatures</code></p>
<dt>
<dd>
<dd>store and print the result of &lt;dsig:Signature&gt; processing just before calculating signature</p>
<dt> <code>&#8211;enabled-reference-uris</code> &lt;list&gt;</p>
<dt>
<dd>
<dd>comma separated list of of the following values: &quot;empty&quot;, &quot;same-doc&quot;, &quot;local&quot;,&quot;remote&quot; to restrict possible URI attribute values for the &lt;dsig:Reference&gt; element</p>
<dt> <code>&#8211;enable-visa3d-hack</code></p>
<dt>
<dd>
<dd>enables Visa3D protocol specific hack for URI attributes processing when we are trying not to use XPath/XPointer engine; this is a hack and I don&#8217;t know what else might be broken in your application when you use it (also check &quot;&#8211;id-attr&quot; option because you might need it)</p>
<dt> <code>&#8211;binary-data</code> &lt;file&gt;</p>
<dt>
<dd>
<dd>binary &lt;file&gt; to encrypt</p>
<dt> <code>&#8211;xml-data</code> &lt;file&gt;</p>
<dt>
<dd>
<dd>XML &lt;file&gt; to encrypt</p>
<dt> <code>&#8211;enabled-cipher-reference-uris</code> &lt;list&gt;</p>
<dt>
<dd>
<dd>comma separated list of of the following values: &quot;empty&quot;, &quot;same-doc&quot;, &quot;local&quot;,&quot;remote&quot; to restrict possible URI attribute values for the &lt;enc:CipherReference&gt; element</p>
<dt> <code>&#8211;session-key</code> &lt;keyKlass&gt;-&lt;keySize&gt;</p>
<dt>
<dd>
<dd>generate new session &lt;keyKlass&gt; key of &lt;keySize&gt; bits size (for example, &quot;&#8211;session des-192&quot; generates a new 192 bits DES key for DES3 encryption)</p>
<dt> <code>&#8211;output</code> &lt;filename&gt;</p>
<dt>
<dd>
<dd>write result document to file &lt;filename&gt;</p>
<dt> <code>&#8211;print-debug</code></p>
<dt>
<dd>
<dd>print debug information to stdout</p>
<dt> <code>&#8211;print-xml-debug</code></p>
<dt>
<dd>
<dd>print debug information to stdout in xml format</p>
<dt> <code>&#8211;dtd-file</code> &lt;file&gt;</p>
<dt>
<dd>
<dd>load the specified file as the DTD</p>
<dt> <code>&#8211;node-id</code> &lt;id&gt;</p>
<dt>
<dd>
<dd>set the operation start point to the node with given &lt;id&gt;</p>
<dt> <code>&#8211;node-name</code> [&lt;namespace-uri&gt;:]&lt;name&gt;</p>
<dt>
<dd>
<dd>set the operation start point to the first node with given &lt;name&gt; and &lt;namespace&gt; URI</p>
<dt> <code>&#8211;node-xpath</code> &lt;expr&gt;</p>
<dt>
<dd>
<dd>set the operation start point to the first node selected by the specified XPath expression</p>
<dt> <code>&#8211;id-attr[</code>:&lt;attr-name&gt;] [&lt;node-namespace-uri&gt;:]&lt;node-name&gt;</p>
<dt>
<dd>
<dd>adds attributes &lt;attr-name&gt; (default value &quot;id&quot;) from all nodes with&lt;node-name&gt; and namespace &lt;node-namespace-uri&gt; to the list of known ID attributes; this is a hack and if you can use DTD or schema to declare ID attributes instead (see &quot;&#8211;dtd-file&quot; option), I don&#8217;t know what else might be broken in your application when you use this hack</p>
<dt> <code>&#8211;enabled-key-data</code> &lt;list&gt;</p>
<dt>
<dd>
<dd>comma separated list of enabled key data (list of registered key data klasses is available with &quot;&#8211;list-key-data&quot; command); by default, all registered key data are enabled</p>
<dt> <code>&#8211;enabled-retrieval-uris</code> &lt;list&gt;</p>
<dt>
<dd>
<dd>comma separated list of of the following values: &quot;empty&quot;, &quot;same-doc&quot;, &quot;local&quot;,&quot;remote&quot; to restrict possible URI attribute values for the &lt;dsig:RetrievalMethod&gt; element.</p>
<dt> <code>&#8211;gen-key[</code>:&lt;name&gt;] &lt;keyKlass&gt;-&lt;keySize&gt;</p>
<dt>
<dd>
<dd>generate new &lt;keyKlass&gt; key of &lt;keySize&gt; bits size, set the key name to &lt;name&gt; and add the result to keys manager (for example, &quot;&#8211;gen:mykey rsa-1024&quot; generates a new 1024 bits RSA key and sets it&#8217;s name to &quot;mykey&quot;)</p>
<dt> <code>&#8211;keys-file</code> &lt;file&gt;</p>
<dt>
<dd>
<dd>load keys from XML file</p>
<dt> <code>&#8211;privkey-pem[</code>:&lt;name&gt;] &lt;file&gt;[,&lt;cafile&gt;[,&lt;cafile&gt;[&#8230;]]]</p>
<dt>
<dd>
<dd>load private key from PEM file and certificates that verify this key</p>
<dt> <code>&#8211;privkey-der[</code>:&lt;name&gt;] &lt;file&gt;[,&lt;cafile&gt;[,&lt;cafile&gt;[&#8230;]]]</p>
<dt>
<dd>
<dd>load private key from DER file and certificates that verify this key</p>
<dt> <code>&#8211;pkcs8-pem[</code>:&lt;name&gt;] &lt;file&gt;[,&lt;cafile&gt;[,&lt;cafile&gt;[&#8230;]]]</p>
<dt>
<dd>
<dd>load private key from PKCS8 PEM file and PEM certificates that verify this key</p>
<dt> <code>&#8211;pkcs8-der[</code>:&lt;name&gt;] &lt;file&gt;[,&lt;cafile&gt;[,&lt;cafile&gt;[&#8230;]]]</p>
<dt>
<dd>
<dd>load private key from PKCS8 DER file and DER certificates that verify this key</p>
<dt> <code>&#8211;pubkey-pem[</code>:&lt;name&gt;] &lt;file&gt;</p>
<dt>
<dd>
<dd>load public key from PEM file</p>
<dt> <code>&#8211;pubkey-der[</code>:&lt;name&gt;] &lt;file&gt;</p>
<dt>
<dd>
<dd>load public key from DER file</p>
<dt> <code>&#8211;aeskey[</code>:&lt;name&gt;] &lt;file&gt;</p>
<dt>
<dd>
<dd>load AES key from binary file &lt;file&gt;</p>
<dt> <code>&#8211;deskey[</code>:&lt;name&gt;] &lt;file&gt;</p>
<dt>
<dd>
<dd>load DES key from binary file &lt;file&gt;</p>
<dt> <code>&#8211;hmackey[</code>:&lt;name&gt;] &lt;file&gt;</p>
<dt>
<dd>
<dd>load HMAC key from binary file &lt;file&gt;</p>
<dt> <code>&#8211;pwd</code> &lt;password&gt;</p>
<dt>
<dd>
<dd>the password to use for reading keys and certs</p>
<dt> <code>&#8211;pkcs12[</code>:&lt;name&gt;] &lt;file&gt;</p>
<dt>
<dd>
<dd>load load private key from pkcs12 file &lt;file&gt;</p>
<dt> <code>&#8211;pubkey-cert-pem[</code>:&lt;name&gt;] &lt;file&gt;</p>
<dt>
<dd>
<dd>load public key from PEM cert file</p>
<dt> <code>&#8211;pubkey-cert-der[</code>:&lt;name&gt;] &lt;file&gt;</p>
<dt>
<dd>
<dd>load public key from DER cert file</p>
<dt> <code>&#8211;trusted-pem</code> &lt;file&gt;</p>
<dt>
<dd>
<dd>load trusted (root) certificate from PEM file &lt;file&gt;</p>
<dt> <code>&#8211;untrusted-pem</code> &lt;file&gt;</p>
<dt>
<dd>
<dd>load untrusted certificate from PEM file &lt;file&gt;</p>
<dt> <code>&#8211;trusted-der</code> &lt;file&gt;</p>
<dt>
<dd>
<dd>load trusted (root) certificate from DER file &lt;file&gt;</p>
<dt> <code>&#8211;untrusted-der</code> &lt;file&gt;</p>
<dt>
<dd>
<dd>load untrusted certificate from DER file &lt;file&gt;</p>
<dt> <code>&#8211;verification-time</code> &lt;time&gt;</p>
<dt>
<dd>
<dd>the local time in &quot;YYYY-MM-DD HH:MM:SS&quot; format used certificates verification</p>
<dt> <code>&#8211;depth</code> &lt;number&gt;</p>
<dt>
<dd>
<dd>maximum certificates chain depth</p>
<dt> <code>&#8211;X509-skip-strict-checks</code></p>
<dt>
<dd>
<dd>skip strict checking of X509 data</p>
<dt> <code>&#8211;crypto</code> &lt;name&gt;</p>
<dt>
<dd>
<dd>the name of the crypto engine to use from the following list: openssl, mscrypto, nss, gnutls, gcrypt (if no crypto engine is specified then the default one is used)</p>
<dt> <code>&#8211;crypto-config</code> &lt;path&gt;</p>
<dt>
<dd>
<dd>path to crypto engine configuration</p>
<dt> <code>&#8211;repeat</code> &lt;number&gt;</p>
<dt>
<dd>
<dd>repeat the operation &lt;number&gt; times</p>
<dt> <code>&#8211;disable-error-msgs</code></p>
<dt>
<dd>
<dd>do not print xmlsec error messages</p>
<dt> <code>&#8211;print-crypto-error-msgs</code></p>
<dt>
<dd>
<dd>print errors stack at the end</p>
<dt> <code>&#8211;help</code></p>
<dt>
<dd>
<dd>print help information about the command</dl>
<h2>AUTHOR</h2>
<p> Written by Aleksey Sanin &lt;aleksey [at] aleksey.com&gt;.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="http://www.aleksey.com/xmlsec/bugs.html">http://www.aleksey.com/xmlsec/bugs.html</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002-2003 Aleksey Sanin.<br />
 This is free software: see the source for copying information. </p>
<h2>Index</h2>
