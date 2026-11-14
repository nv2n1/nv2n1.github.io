---
title: "yubico-piv-tool(1)"
name: "yubico-piv-tool"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yubico-piv-tool/"
description: "yubico-piv-tool – Yubico PIV tool"
---

<h2>NAME</h2>
<p> yubico-piv-tool &#8211; Yubico PIV tool</p>
<h2>SYNOPSIS</h2>
<p> <code>yubico-piv-tool</code> [<i>,OPTIONS/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> yubico-piv-tool 1.1.1</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print help and exit</p>
<dt><code>&#8211;full-help</code></p>
<dd> Print help, including hidden options, and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version and exit</p>
<dt><code>-v</code>, <code>&#8211;verbose</code>[=<i>,INT/</i>]</p>
<dd> Print more information (default=`0&#8242;)</p>
<dt><code>-r</code>, <code>&#8211;reader</code>=<i>,STRING/</i></p>
<dd> Only use a matching reader (default=`Yubikey&#8217;)</p>
<dt><code>-k</code>, <code>&#8211;key</code>[=<i>,STRING/</i>]</p>
<dd> Authentication key to use (default=`010203040506070801020304050607080102030405060708&#8242;)</p>
<dt><code>-a</code>, <code>&#8211;action</code>=<i>,ENUM/</i></p>
<dd> Action to take (possible values=&quot;version&quot;, &quot;generate&quot;, &quot;set-mgm-key&quot;, &quot;reset&quot;, &quot;pin-retries&quot;, &quot;import-key&quot;, &quot;import-certificate&quot;, &quot;set-chuid&quot;, &quot;request-certificate&quot;, &quot;verify-pin&quot;, &quot;change-pin&quot;, &quot;change-puk&quot;, &quot;unblock-pin&quot;, &quot;selfsign-certificate&quot;, &quot;delete-certificate&quot;, &quot;read-certificate&quot;, &quot;status&quot;, &quot;test-signature&quot;, &quot;test-decipher&quot;, &quot;list-readers&quot;)</p>
<dt>
<dd> Multiple actions may be given at once and will be executed in order for example <code>&#8211;action</code>=<i>,verify-pin/</i> <code>&#8211;action</code>=<i>,request-certificate/</i></p>
<dt><code>-s</code>, <code>&#8211;slot</code>=<i>,ENUM/</i></p>
<dd> What key slot to operate on (possible values=&quot;9a&quot;, &quot;9c&quot;, &quot;9d&quot;, &quot;9e&quot;, &quot;82&quot;, &quot;83&quot;, &quot;84&quot;, &quot;85&quot;, &quot;86&quot;, &quot;87&quot;, &quot;88&quot;, &quot;89&quot;, &quot;8a&quot;, &quot;8b&quot;, &quot;8c&quot;, &quot;8d&quot;, &quot;8e&quot;, &quot;8f&quot;, &quot;90&quot;, &quot;91&quot;, &quot;92&quot;, &quot;93&quot;, &quot;94&quot;, &quot;95&quot;)</p>
<dt>
<dd> 9a is for PIV Authentication 9c is for Digital Signature (PIN always checked) 9d is for Key Management 9e is for Card Authentication (PIN never checked) 82-95 is for Retired Key Management</p>
<dt><code>-A</code>, <code>&#8211;algorithm</code>=<i>,ENUM/</i></p>
<dd> What algorithm to use (possible values=&quot;RSA1024&quot;, &quot;RSA2048&quot;, &quot;ECCP256&quot;, &quot;ECCP384&quot; default=`RSA2048&#8242;)</p>
<dt><code>-H</code>, <code>&#8211;hash</code>=<i>,ENUM/</i></p>
<dd> Hash to use for signatures (possible values=&quot;SHA1&quot;, &quot;SHA256&quot;, &quot;SHA384&quot;, &quot;SHA512&quot; default=`SHA256&#8242;)</p>
<dt><code>-n</code>, <code>&#8211;new-key</code>=<i>,STRING/</i></p>
<dd> New authentication key to use</p>
<dt><code>&#8211;pin-retries</code>=<i>,INT/</i></p>
<dd> Number of retries before the pin code is blocked</p>
<dt><code>&#8211;puk-retries</code>=<i>,INT/</i></p>
<dd> Number of retries before the puk code is blocked</p>
<dt><code>-i</code>, <code>&#8211;input</code>=<i>,STRING/</i></p>
<dd> Filename to use as input, &#8211; for stdin (default=`-&#8216;)</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,STRING/</i></p>
<dd> Filename to use as output, &#8211; for stdout (default=`-&#8216;)</p>
<dt><code>-K</code>, <code>&#8211;key-format</code>=<i>,ENUM/</i></p>
<dd> Format of the key being read/written (possible values=&quot;PEM&quot;, &quot;PKCS12&quot;, &quot;GZIP&quot;, &quot;DER&quot; default=`PEM&#8217;)</p>
<dt><code>-p</code>, <code>&#8211;password</code>=<i>,STRING/</i></p>
<dd> Password for decryption of private key file</p>
<dt><code>-S</code>, <code>&#8211;subject</code>=<i>,STRING/</i></p>
<dd> The subject to use for certificate request</p>
<dt>
<dd> The subject must be written as: /CN=host.example.com/OU=test/O=example.com/</p>
<dt><code>-P</code>, <code>&#8211;pin</code>=<i>,STRING/</i></p>
<dd> Pin/puk code for verification</p>
<dt><code>-N</code>, <code>&#8211;new-pin</code>=<i>,STRING/</i></p>
<dd> New pin/puk code for changing</p>
<dt><code>&#8211;pin-policy</code>=<i>,ENUM/</i></p>
<dd> Set pin policy for action generate or import-key (possible values=&quot;never&quot;, &quot;once&quot;, &quot;always&quot;)</p>
<dt><code>&#8211;touch-policy</code>=<i>,ENUM/</i></p>
<dd> Set touch policy for action generate, import-key or set-mgm-key (possible values=&quot;never&quot;, &quot;always&quot;)</dl>
<h2>EXAMPLES</h2>
<p> For more information about what&#8217;s happening &#8211;verbose can be added to any command. For much more information &#8211;verbose=2 may be used. </p>
<p> Display what version of the application is running on the YubiKey: </p>
<p>yubico-piv-tool -a version </p>
<p> Generate a new ECC-P256 key on device in slot 9a, will print the public key on stdout: </p>
<p>yubico-piv-tool -s 9a -A ECCP256 -a generate </p>
<p> Generate a certificate request with public key from stdin, will print the resulting request on stdout: </p>
<p>yubico-piv-tool -s 9a -S&nbsp;<wbr>&#8216;/CN=foo/OU=test/O=example.com/&#8217;&nbsp;<wbr>-P 123456&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>-a verify -a request </p>
<p> Generate a self-signed certificate with public key from stdin, will print the certificate, for later import, on stdout: </p>
<p>yubico-piv-tool -s 9a -S&nbsp;<wbr>&#8216;/CN=bar/OU=test/O=example.com/&#8217;&nbsp;<wbr>-P 123456&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>-a verify -a selfsign </p>
<p> Import a certificate from stdin: </p>
<p>yubico-piv-tool -s 9a -a import-certificate </p>
<p> Set a random chuid, import a key and import a certificate from a PKCS12 file with password test, into slot 9c: </p>
<p>yubico-piv-tool -s 9c -i test.pfx -K PKCS12 -p test -a set-chuid&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>-a import-key -a import-cert </p>
<p> Import a certificate which is larger than 2048 bytes and thus requires compression in order to fit: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>openssl x509 -in cert.pem -outform DER | gzip -9&nbsp;<wbr>&gt;&nbsp;<wbr>der.gz<br />
&nbsp;<wbr>&nbsp;<wbr>yubico-piv-tool -s 9c -i der.gz -K GZIP -a import-cert </p>
<p> Change the management key used for administrative authentication: </p>
<p>yubico-piv-tool -n 0807605403020108070605040302010807060504030201&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>-a set-mgm-key </p>
<p> Delete a certificate in slot 9a: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>yubico-piv-tool -a delete-certificate -s 9a </p>
<p> Show some information on certificates and other data: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>yubico-piv-tool -a status </p>
<p> Read out the certificate from a slot and then run a signature test: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>yubico-piv-tool -a read-cert -s 9a<br />
&nbsp;<wbr>&nbsp;<wbr>yubico-piv-tool -a verify-pin -P 123456 -a test-signature -s 9a </p>
<h2>Index</h2>
