---
title: "softhsm2-keyconv(1)"
name: "softhsm2-keyconv"
section: "1"
letter: "s"
url: "/docs/linux/man/1-softhsm2-keyconv/"
description: "softhsm2-keyconv – converting from BIND to PKCS#8 key file format"
---

<h2>NAME</h2>
<p> softhsm2-keyconv &#8211; converting from BIND to PKCS#8 key file format</p>
<h2>SYNOPSIS</h2>
<p> <code>softhsm2-keyconv</code> <code>&#8211;in</code> <i>path</i> <code>&#8211;out</code> <i>path</i> [<code>&#8211;pin</code> <i>PIN</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>softhsm2-keyconv</code> can convert BIND .private-key files to the PKCS#8 file format. This is so that you can import the PKCS#8 file into libsofthsm using the command <code>softhsm2-util</code>. If you have another file format, then <code>openssl</code> probably can help you to convert it into the PKCS#8 file format.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code>, <code>-h</code> Shows the help screen.</p>
<dl>
<dt><code>&#8211;in </code><i>path</i></p>
<dd> The <i>path</i> to the input file.</p>
<dt><code>&#8211;out </code><i>path</i></p>
<dd> The <i>path</i> to the output file.</p>
<dt><code>&#8211;pin </code><i>PIN</i></p>
<dd> The <i>PIN</i> will be used to encrypt the PKCS#8 file. If not given then the PKCS#8 file will be unencrypted.</p>
<dt><code>&#8211;version</code>, <code>-v</code></p>
<dd> Show the version info.</dl>
<h2>EXAMPLES</h2>
<p> The following command can be used to convert a BIND .private-key file to a PKCS#8 file: </p>
<dl>
<dt>
<dd>
<pre><code>
softhsm2 - keyconv-- in Kexample.com.+ 007 + 05474.private

    &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
--out rsa.pem
</code></pre>
</dl>
<h2>AUTHORS</h2>
<p> Written by Rickard Bellgrim, Francis Dupont, René Post, and Roland van Rijswijk.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-softhsm2-migrate/">softhsm2-migrate</a></i>(1), <i><a href="/docs/linux/man/1-softhsm2-util/">softhsm2-util</a></i>(1), <i><a href="/docs/linux/man/5-softhsm2-conf/">softhsm2.conf</a></i>(5), <i><a href="/docs/linux/man/1-openssl/">openssl</a></i>(1), <i><a href="/docs/linux/man/1-named/">named</a></i>(1), <i><a href="/docs/linux/man/1-dnssec-keygen/">dnssec-keygen</a></i>(1), <i><a href="/docs/linux/man/1-dnssec-signzone/">dnssec-signzone</a></i>(1) </p>
<h2>Index</h2>
