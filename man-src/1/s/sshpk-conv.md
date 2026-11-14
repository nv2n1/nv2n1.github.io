---
title: "sshpk-conv(1)"
name: "sshpk-conv"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sshpk-conv/"
description: "sshpk-conv – convert between key formats"
---

<h2 class="name">NAME</h2>
<p> sshpk-conv &#8211; convert between key formats </p>
<h2>SYNOPSYS</h2>
<p> <code>sshpk-conv</code> -t FORMAT [FILENAME] [OPTIONS&#8230;] </p>
<p> <code>sshpk-conv</code> -i [FILENAME] [OPTIONS&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Reads in a public or private key and converts it between different formats, particularly formats used in the SSH protocol and the well-known PEM PKCS#1/7 formats. </p>
<p> In the second form, with the <code>-i</code> option given, identifies a key and prints to stderr information about its nature, size and fingerprint.</p>
<h2>EXAMPLES</h2>
<p> Assume the following SSH-format public key in <code>id_ecdsa.pub</code>: </p>
<dl>
<dt>
<dd>
<pre>
ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTI...9M/4c4= user [at] host
</pre>
</dl>
<p> Identify it with <code>-i</code>: </p>
<dl>
<dt>
<dd>
<pre>
$ sshpk-conv -i id_ecdsa.pub
id_ecdsa: a 256 bit ECDSA public key
ECDSA curve: nistp256
Comment: user [at] host
Fingerprint:
  SHA256:vCNX7eUkdvqqW0m4PoxQAZRv+CM4P4fS8+CbliAvS4k
  81:ad:d5:57:e5:6f:7d:a2:93:79:56:af:d7:c0:38:51
</pre>
</dl>
<p> Convert it to <code>pkcs8</code> format, for use with e.g. OpenSSL: </p>
<dl>
<dt>
<dd>
<pre><code>
$ sshpk - conv - t pkcs8 id_ecdsa-- -- -BEGIN PUBLIC KEY-- -- -MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEAsA4R6N6AS3gzaPBeLjG2ObSgUsR zOt + kWJoijLnw3ZMYUKmAx + lD0I5XUxdrPcs1vH5f3cn9TvRvO9L0z / hzg ==
    -- -- -END PUBLIC KEY-- -- -
</code></pre>
</dl>
<p> Retrieve the public half of a private key: </p>
<dl>
<dt>
<dd>
<pre>
$ openssl genrsa 2048 | sshpk-conv -t ssh -c foo@bar
ssh-rsa AAAAB3NzaC1yc2EAAA...koK7 foo@bar
</pre>
</dl>
<p> Convert a private key to PKCS#1 (OpenSSL) format from a new-style OpenSSH key format (the <code>ssh-keygen -o</code> format): </p>
<dl>
<dt>
<dd>
<pre><code>
$ ssh - keygen - o - f foobar... $ sshpk - conv - p - t pkcs1 foobar-- -- -BEGIN RSA PRIVATE KEY-- -- -MIIDpAIBAAKCAQEA6T / GYJndb1TRH3 + NL....-- -- -END RSA PRIVATE KEY-- -- -
</code></pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-i, &#8211;identify</code><br />
&nbsp;<wbr>&nbsp;Instead of converting the key, output identifying information about it to&nbsp;<br />
&nbsp;<wbr>&nbsp;stderr, including its type, size and fingerprints. </p>
<p> <code>-p, &#8211;private</code><br />
&nbsp;<wbr>&nbsp;Treat the key as a private key instead of a public key&nbsp;(the default). If you<br />
&nbsp;<wbr>&nbsp;supply&nbsp;<code>sshpk-conv</code>&nbsp;with a private key and do not give this option, it will<br />
&nbsp;<wbr>&nbsp;extract only the public half of the key from it and work with that. </p>
<p> <code>-f PATH, &#8211;file=PATH</code><br />
&nbsp;<wbr>&nbsp;Input file to take the key from instead of stdin. If a filename is supplied<br />
&nbsp;<wbr>&nbsp;as a positional argument, it is equivalent to using this option. </p>
<p> <code>-o PATH, &#8211;out=PATH</code><br />
&nbsp;<wbr>&nbsp;Output file name to use instead of stdout. </p>
<p> <code>-T FORMAT, &#8211;informat=FORMAT</code> </p>
<p> <code>-t FORMAT, &#8211;outformat=FORMAT</code><br />
&nbsp;<wbr>&nbsp;Selects the input and output formats to be used&nbsp;(see FORMATS, below). </p>
<p> <code>-c TEXT, &#8211;comment=TEXT</code><br />
&nbsp;<wbr>&nbsp;Sets the key comment for the output file, if supported.</p>
<h2>FORMATS</h2>
<p> Currently supported formats: </p>
<p> <code>pem, pkcs1</code><br />
&nbsp;<wbr>&nbsp;The standard PEM format used by older OpenSSH and most TLS libraries such as<br />
&nbsp;<wbr>&nbsp;OpenSSL. The classic&nbsp;<code>id_rsa</code>&nbsp;file is usually in this format. It is an ASN.1<br />
&nbsp;<wbr>&nbsp;encoded structure, base64-encoded and placed between PEM headers. </p>
<p> <code>ssh</code><br />
&nbsp;<wbr>&nbsp;The SSH public key text format&nbsp;(the format of an&nbsp;<code>id_rsa.pub</code>&nbsp;file). A single<br />
&nbsp;<wbr>&nbsp;line, containing 3 space separated parts: the key type, key body and optional<br />
&nbsp;<wbr>&nbsp;key comment. </p>
<p> <code>pkcs8</code><br />
&nbsp;<wbr>&nbsp;A newer PEM format, usually used only for public keys by TLS libraries such<br />
&nbsp;<wbr>&nbsp;as OpenSSL. The ASN.1 structure is more generic than that of&nbsp;<code>pkcs1</code>. </p>
<p> <code>openssh</code><br />
&nbsp;<wbr>&nbsp;The new&nbsp;<code>ssh-keygen -o</code>&nbsp;format from OpenSSH. This can be mistaken for a PEM<br />
&nbsp;<wbr>&nbsp;encoding but is actually an OpenSSH internal format. </p>
<p> <code>rfc4253</code><br />
&nbsp;<wbr>&nbsp;The internal binary format of keys when sent over the wire in the SSH<br />
&nbsp;<wbr>&nbsp;protocol. This is also the format that the&nbsp;<code>ssh-agent</code>&nbsp;uses in its protocol.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ssh-keygen/">ssh-keygen</a>(1), <a href="/docs/linux/man/1-openssl/">openssl</a>(1)</p>
<h2>BUGS</h2>
<p> Encrypted (password-protected) keys are not supported. </p>
<p> Report bugs at Github <i><a rel="nofollow" href="https://github.com/arekinath/node-sshpk/issues">https://github.com/arekinath/node-sshpk/issues</a></i> </p>
<h2>Index</h2>
