---
title: "dropbearconvert(1)"
name: "dropbearconvert"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dropbearconvert/"
description: "dropbearconvert – convert between Dropbear and OpenSSH private key formats"
---

<h2>NAME</h2>
<p> dropbearconvert &#8211; convert between Dropbear and OpenSSH private key formats</p>
<h2>SYNOPSIS</h2>
<p> <code>dropbearconvert</code> <i>input_type</i> <i>output_type</i> <i>input_file</i> <i>output_file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>Dropbear</code> and <code>OpenSSH</code> SSH implementations have different private key formats. <code>dropbearconvert</code> can convert between the two. </p>
<p> Dropbear uses the same SSH public key format as OpenSSH, it can be extracted from a private key by using <code>dropbearkey -y</code> </p>
<p> Encrypted private keys are not supported, use <a href="/docs/linux/man/1-ssh-keygen/">ssh-keygen</a>(1) to decrypt them first.</p>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>input_type</i></p>
<dd> Either <i>dropbear</i> or <i>openssh</i></p>
<dt><i>output_type</i></p>
<dd> Either <i>dropbear</i> or <i>openssh</i></p>
<dt><i>input_file</i></p>
<dd> An existing Dropbear or OpenSSH private key file</p>
<dt><i>output_file</i></p>
<dd> The path to write the converted private key file. For client authentication ~/.ssh/id_dropbear is loaded by default</dl>
<h2>EXAMPLE</h2>
<p>&nbsp;<wbr>#&nbsp;<wbr>dropbearconvert openssh dropbear&nbsp;<wbr>~/.ssh/id_rsa&nbsp;<wbr>~/.ssh/id_dropbear</p>
<h2>AUTHOR</h2>
<p> Matt Johnston (matt [at] ucc.asn.au).</p>
<h2>SEE ALSO</h2>
<p>&nbsp;<wbr><a href="/docs/linux/man/1-dropbearkey/">dropbearkey</a>(1),&nbsp;<wbr><a href="/docs/linux/man/1-ssh-keygen/">ssh-keygen</a>(1) </p>
<p> <a rel="nofollow" href="https://matt.ucc.asn.au/dropbear/dropbear.html">https://matt.ucc.asn.au/dropbear/dropbear.html</a> </p>
<h2>Index</h2>
