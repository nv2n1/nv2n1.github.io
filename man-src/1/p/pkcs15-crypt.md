---
title: "pkcs15-crypt(1)"
name: "pkcs15-crypt"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pkcs15-crypt/"
description: "pkcs15-crypt – perform crypto operations using pkcs15 smart card"
---

<h2 class="name">NAME</h2>
<p> pkcs15-crypt &#8211; perform crypto operations using pkcs15 smart card </p>
<h2>SYNOPSIS</h2>
<p> <code>pkcs15-crypt</code> [OPTIONS]</p>
<h2>DESCRIPTION</h2>
<p> The <code>pkcs15-crypt</code> utility can be used from the command line to perform cryptographic operations such as computing digital signatures or decrypting data, using keys stored on a PKCS #15 compliant smart card.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;sign, -s</code></p>
<dl>
<dt>
<dd> Perform digital signature operation on the data read from a file specified using the <code>input</code> option. By default, the contents of the file are assumed to be the result of an MD5 hash operation. Note that <code>pkcs15-crypt</code> expects the data in binary representation, not ASCII. </p>
<p> The digital signature is stored, in binary representation, in the file specified by the <code>output</code> option. If this option is not given, the signature is printed on standard output, displaying non-printable characters using their hex notation xNN (see also <code>&#8211;raw</code>).</dl>
<p> <code>&#8211;pkcs1</code></p>
<dl>
<dt>
<dd> By default, <code>pkcs15-crypt</code> assumes that input data has been padded to the correct length (i.e. when computing an RSA signature using a 1024 bit key, the input must be padded to 128 bytes to match the modulus length). When giving the <code>&#8211;pkcs1</code> option, however, <code>pkcs15-crypt</code> will perform the required padding using the algorithm outlined in the PKCS #1 standard version 1.5.</dl>
<p> <code>&#8211;sha-1</code></p>
<dl>
<dt>
<dd> This option tells <code>pkcs15-crypt</code> that the input file is the result of an SHA1 hash operation, rather than an MD5 hash. Again, the data must be in binary representation.</dl>
<p> <code>&#8211;decipher, -c</code></p>
<dl>
<dt>
<dd> Decrypt the contents of the file specified by the <code>&#8211;input</code> option. The result of the decryption operation is written to the file specified by the <code>&#8211;output</code> option. If this option is not given, the decrypted data is printed to standard output, displaying non-printable characters using their hex notation xNN (see also <code>&#8211;raw</code>).</dl>
<p> <code>&#8211;key</code> <i>id</i>, <code>-k</code> <i>id</i></p>
<dl>
<dt>
<dd> Selects the ID of the key to use.</dl>
<p> <code>&#8211;reader</code> <i>N</i>, <code>-r</code> <i>N</i></p>
<dl>
<dt>
<dd> Selects the <i>N</i>-th smart card reader configured by the system. If unspecified, <code>pkcs15-crypt</code> will use the first reader found.</dl>
<p> <code>&#8211;input</code> <i>file</i>, <code>-i</code> <i>file</i></p>
<dl>
<dt>
<dd> Specifies the input file to use.</dl>
<p> <code>&#8211;output</code> <i>file</i>, <code>-o</code> <i>file</i></p>
<dl>
<dt>
<dd> Any output will be sent to the specified file.</dl>
<p> <code>&#8211;raw, -R</code></p>
<dl>
<dt>
<dd> Outputs raw 8 bit data.</dl>
<p> <code>&#8211;pin</code> <i>pin</i>, <code>-p</code> <i>pin</i></p>
<dl>
<dt>
<dd> When the cryptographic operation requires a PIN to access the key, <code>pkcs15-crypt</code> will prompt the user for the PIN on the terminal. Using this option allows you to specify the PIN on the command line. </p>
<p> Note that on most operating systems, the command line of a process can be displayed by any user using the <a href="/docs/linux/man/1-ps/">ps</a>(1) command. It is therefore a security risk to specify secret information such as PINs on the command line. If you specify &#8216;-&#8216; as PIN, it will be read from STDIN.</dl>
<p> <code>&#8211;verbose, -v</code></p>
<dl>
<dt>
<dd> Causes <code>pkcs15-crypt</code> to be more verbose. Specify this flag several times to enable debug output in the OpenSC library.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pkcs15-init/">pkcs15-init</a>(1), <a href="/docs/linux/man/1-pkcs15-tool/">pkcs15-tool</a>(1) </p>
<h2>Index</h2>
