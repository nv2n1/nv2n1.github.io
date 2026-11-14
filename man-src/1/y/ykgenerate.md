---
title: "ykgenerate(1)"
name: "ykgenerate"
section: "1"
letter: "y"
url: "/docs/linux/man/1-ykgenerate/"
description: "ykgenerate – construct and encrypt an OTP from given data"
---

<h2 class="name">NAME</h2>
<p> ykgenerate &#8211; construct and encrypt an OTP from given data </p>
<h2>SYNOPSIS</h2>
<p> <code>ykgenerate</code> <i>AESKEY</i> <i>YK_INTERNALNAME</i> <i>YK_COUNTER</i> <i>YK_LOW</i> <i>YK_HIGH</i> <i>YK_USE</i></p>
<h2>DESCRIPTION</h2>
<p> Generate OTPs by encrypting given values under the given encryption key.</p>
<h2>OPTIONS</h2>
<p> <code>AESKEY</code></p>
<dl>
<dt>
<dd> The 16-character AES-128 key to use in hex.</dl>
<p> <code>YK_INTERNALNAME</code></p>
<dl>
<dt>
<dd> Hex encoded internal identity (48 bit).</dl>
<p> <code>YK_COUNTER</code></p>
<dl>
<dt>
<dd> Hex encoded counter (16 bit).</dl>
<p> <code>YK_LOW</code></p>
<dl>
<dt>
<dd> Hex encoded timestamp low (16 bit).</dl>
<p> <code>YK_HIGH</code></p>
<dl>
<dt>
<dd> Hex encoded timestamp high (8bit).</dl>
<p> <code>YK_USE</code></p>
<dl>
<dt>
<dd> Hex encoded use (8 bit).</dl>
<h2>EXAMPLES</h2>
<p> Typical usage of the tool is as follows. </p>
<dl>
<dt>
<dd>
<pre>
ykgenerate ecde18dbe76fbd0c33330f1c354871db 8792ebfe26cc 0013 c0a8 00 10
</pre>
</dl>
<p> Use <a href="/docs/linux/man/1-ykparse/">ykparse</a>(1) to decode the resulting OTP.</p>
<h2>SEE ALSO</h2>
<p> YubiKeys can be obtained from Yubico: <a rel="nofollow" href="http://www.yubico.com/">http://www.yubico.com/</a> </p>
<h2>Index</h2>
