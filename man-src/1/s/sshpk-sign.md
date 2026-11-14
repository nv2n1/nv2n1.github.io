---
title: "sshpk-sign(1)"
name: "sshpk-sign"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sshpk-sign/"
description: "sshpk-sign – sign data using an SSH key"
---

<h2 class="name">NAME</h2>
<p> sshpk-sign &#8211; sign data using an SSH key </p>
<h2>SYNOPSYS</h2>
<p> <code>sshpk-sign</code> -i KEYPATH [OPTION&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Takes in arbitrary bytes, and signs them using an SSH private key. The key can be of any type or format supported by the <code>sshpk</code> library, including the standard OpenSSH formats, as well as PEM PKCS#1 and PKCS#8. </p>
<p> The signature is printed out in Base64 encoding, unless the <code>&#8211;binary</code> or <code>-b</code> option is given.</p>
<h2>EXAMPLES</h2>
<p> Signing with default settings: </p>
<dl>
<dt>
<dd>
<pre>
$ printf 'foo' | sshpk-sign -i ~/.ssh/id_ecdsa
MEUCIAMdLS/vXrrtWFepwe...
</pre>
</dl>
<p> Signing in SSH (RFC 4253) format (rather than the default ASN.1): </p>
<dl>
<dt>
<dd>
<pre>
$ printf 'foo' | sshpk-sign -i ~/.ssh/id_ecdsa -t ssh
AAAAFGVjZHNhLXNoYTIt...
</pre>
</dl>
<p> Saving the binary signature to a file: </p>
<dl>
<dt>
<dd>
<pre>
$ printf 'foo' | sshpk-sign -i ~/.ssh/id_ecdsa \
                            -o signature.bin -b
$ cat signature.bin | base64
MEUCIAMdLS/vXrrtWFepwe...
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-v, &#8211;verbose</code><br />
&nbsp;<wbr>&nbsp;Print extra information about the key and signature to stderr when signing. </p>
<p> <code>-b, &#8211;binary</code><br />
&nbsp;<wbr>&nbsp;Don&#8217;t base64-encode the signature before outputting it. </p>
<p> <code>-i KEY, &#8211;identity=KEY</code><br />
&nbsp;<wbr>&nbsp;Select the key to be used for signing.&nbsp;<code>KEY</code>&nbsp;must be a relative or absolute<br />
&nbsp;<wbr>&nbsp;filesystem path to the key file. Any format supported by the&nbsp;<code>sshpk</code>&nbsp;library<br />
&nbsp;<wbr>&nbsp;is supported, including OpenSSH formats and standard PEM PKCS. </p>
<p> <code>-f PATH, &#8211;file=PATH</code><br />
&nbsp;<wbr>&nbsp;Input file to sign instead of stdin. </p>
<p> <code>-o PATH, &#8211;out=PATH</code><br />
&nbsp;<wbr>&nbsp;Output file to save signature in instead of stdout. </p>
<p> <code>-H HASH, &#8211;hash=HASH</code><br />
&nbsp;<wbr>&nbsp;Set the hash algorithm to be used for signing. This should be one of&nbsp;<code>sha1</code>,<br />
&nbsp;<wbr>&nbsp;<code>sha256</code>&nbsp;or&nbsp;<code>sha512</code>. Some key types may place restrictions on which hash<br />
&nbsp;<wbr>&nbsp;algorithms may be used&nbsp;(e.g. ED25519 keys can only use SHA-512). </p>
<p> <code>-t FORMAT, &#8211;format=FORMAT</code><br />
&nbsp;<wbr>&nbsp;Choose the signature format to use, from&nbsp;<code>asn1</code>,&nbsp;<code>ssh</code>&nbsp;or&nbsp;<code>raw</code>&nbsp;(only for<br />
&nbsp;<wbr>&nbsp;ED25519 signatures). The&nbsp;<code>asn1</code>&nbsp;format is the default, as it is the format<br />
&nbsp;<wbr>&nbsp;used with TLS and typically the standard in most non-SSH libraries&nbsp;(e.g.<br />
&nbsp;<wbr>&nbsp;OpenSSL). The&nbsp;<code>ssh</code>&nbsp;format is used in the SSH protocol and by the ssh-agent.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-sshpk-verify/">sshpk-verify</a>(1)</p>
<h2>BUGS</h2>
<p> Report bugs at Github <i><a rel="nofollow" href="https://github.com/arekinath/node-sshpk/issues">https://github.com/arekinath/node-sshpk/issues</a></i> </p>
<h2>Index</h2>
