---
title: "dropbearkey(1)"
name: "dropbearkey"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dropbearkey/"
description: "dropbearkey – create private keys for the use with dropbear(8) or dbclient(1)"
---

<h2>NAME</h2>
<p> dropbearkey &#8211; create private keys for the use with <a href="/docs/linux/man/8-dropbear/">dropbear</a>(8) or <a href="/docs/linux/man/1-dbclient/">dbclient</a>(1)</p>
<h2>SYNOPSIS</h2>
<p> <code>dropbearkey</code> -t <i>type</i> -f <i>file</i> [-s <i>bits</i>] [-y]</p>
<h2>DESCRIPTION</h2>
<p> <code>dropbearkey</code> generates a <i>RSA</i>, <i>DSS</i>, or <i>ECDSA</i> format SSH private key, and saves it to a file for the use with the Dropbear client or server. Note that some SSH implementations use the term &quot;DSA&quot; rather than &quot;DSS&quot;, they mean the same thing.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t </code><i>type</i></p>
<dd> Type of key to generate. Must be one of <i>rsa</i> <i>ecdsa</i> or <i>dss</i>.</p>
<dt><code>-f </code><i>file</i></p>
<dd> Write the secret key to the file <i>file</i>. For client authentication ~/.ssh/id_dropbear is loaded by default</p>
<dt><code>-s </code><i>bits</i></p>
<dd> Set the key size to <i>bits</i> bits, should be multiple of 8 (optional).</p>
<dt><code>-y</code></p>
<dd> Just print the publickey and fingerprint for the private key in <i>file</i>.</dl>
<h2>NOTES</h2>
<p> The program <a href="/docs/linux/man/1-dropbearconvert/">dropbearconvert</a>(1) can be used to convert between Dropbear and OpenSSH key formats. </p>
<p> Dropbear does not support encrypted keys.</p>
<h2>EXAMPLE</h2>
<p> generate a host-key:<br />
&nbsp;<wbr>#&nbsp;<wbr>dropbearkey -t rsa -f&nbsp;<wbr>/etc/dropbear/dropbear_rsa_host_key </p>
<p> extract a public key suitable for authorized_keys from private key:<br />
&nbsp;<wbr>#&nbsp;<wbr>dropbearkey -y -f id_rsa | grep&nbsp;<wbr>&quot;^ssh-rsa&nbsp;<wbr>&quot;&nbsp;<wbr>&gt;&gt;&nbsp;<wbr>authorized_keys</p>
<h2>AUTHOR</h2>
<p> Matt Johnston (matt [at] ucc.asn.au).<br />
 Gerrit Pape (pape [at] smarden.org) wrote this manual page.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-dropbear/">dropbear</a>(8), <a href="/docs/linux/man/1-dbclient/">dbclient</a>(1), <a href="/docs/linux/man/1-dropbearconvert/">dropbearconvert</a>(1) </p>
<p> <a rel="nofollow" href="https://matt.ucc.asn.au/dropbear/dropbear.html">https://matt.ucc.asn.au/dropbear/dropbear.html</a> </p>
<h2>Index</h2>
