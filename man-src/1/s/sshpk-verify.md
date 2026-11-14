---
title: "sshpk-verify(1)"
name: "sshpk-verify"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sshpk-verify/"
description: "sshpk-verify – verify a signature on data using an SSH key"
---

<h2 class="name">NAME</h2>
<p> sshpk-verify &#8211; verify a signature on data using an SSH key </p>
<h2>SYNOPSYS</h2>
<p> <code>sshpk-verify</code> -i KEYPATH -s SIGNATURE [OPTION&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Takes in arbitrary bytes and a Base64-encoded signature, and verifies that the signature was produced by the private half of the given SSH public key.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
$ printf 'foo' | sshpk-verify -i ~/.ssh/id_ecdsa -s MEUCIQCYp...
OK
$ printf 'foo' | sshpk-verify -i ~/.ssh/id_ecdsa -s GARBAGE...
NOT OK
</pre>
</dl>
<h2>EXIT STATUS</h2>
<p> <code>0</code><br />
&nbsp;<wbr>&nbsp;Signature validates and matches the key. </p>
<p> <code>1</code><br />
&nbsp;<wbr>&nbsp;Signature is parseable and the correct length but does not match the key or<br />
&nbsp;<wbr>&nbsp;otherwise is invalid. </p>
<p> <code>2</code><br />
&nbsp;<wbr>&nbsp;The signature or key could not be parsed. </p>
<p> <code>3</code><br />
&nbsp;<wbr>&nbsp;Invalid commandline options were supplied.</p>
<h2>OPTIONS</h2>
<p> <code>-v, &#8211;verbose</code><br />
&nbsp;<wbr>&nbsp;Print extra information about the key and signature to stderr when verifying. </p>
<p> <code>-i KEY, &#8211;identity=KEY</code><br />
&nbsp;<wbr>&nbsp;Select the key to be used for verification.&nbsp;<code>KEY</code>&nbsp;must be a relative or<br />
&nbsp;<wbr>&nbsp;absolute filesystem path to the key file. Any format supported by the&nbsp;<code>sshpk</code><br />
&nbsp;<wbr>&nbsp;library is supported, including OpenSSH formats and standard PEM PKCS. </p>
<p> <code>-s BASE64, &#8211;signature=BASE64</code><br />
&nbsp;<wbr>&nbsp;Supplies the base64-encoded signature to be verified. </p>
<p> <code>-f PATH, &#8211;file=PATH</code><br />
&nbsp;<wbr>&nbsp;Input file to verify instead of stdin. </p>
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
<p> <a href="/docs/linux/man/1-sshpk-sign/">sshpk-sign</a>(1)</p>
<h2>BUGS</h2>
<p> Report bugs at Github <i><a rel="nofollow" href="https://github.com/arekinath/node-sshpk/issues">https://github.com/arekinath/node-sshpk/issues</a></i> </p>
<h2>Index</h2>
