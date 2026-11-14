---
title: "ykchalresp(1)"
name: "ykchalresp"
section: "1"
letter: "y"
url: "/docs/linux/man/1-ykchalresp/"
description: "ykchalresp – Perform challenge-response operation with YubiKey"
---

<h2>NAME</h2>
<p> ykchalresp &#8211; Perform challenge-response operation with YubiKey</p>
<h2>SYNOPSIS</h2>
<p> <code>ykchalresp</code> [<i>-1</i> | <i>-2</i>] [<i>-H</i>] [<i>-Y</i>] [<i>-N</i>] [<i>-x</i>] [<i>-v</i>] [<i>-6</i>] [<i>-8</i>] [<i>-t</i>] [<i>-V</i>] [<i>-h</i>]</p>
<h2>DESCRIPTION</h2>
<p> Send a challenge to a YubiKey, and read the response. The YubiKey can be configured with two different C/R modes &#8212; the standard one is a 160 bits HMAC-SHA1, and the other is a YubiKey OTP mimicing mode, meaning two subsequent calls with the same challenge will result in different responses.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-1</code></p>
<dd> send the challenge to slot 1. This is the default.</p>
<dt><code>-2</code></p>
<dd> send the challenge to slot 2.</p>
<dt><code>-H</code></p>
<dd> send a 64 byte HMAC challenge. This is the default.</p>
<dt><code>-Y</code></p>
<dd> send a 6 byte Yubico OTP challenge.</p>
<dt><code>-N</code></p>
<dd> non-blocking mode &#8212; abort if the YubiKey is configured to require a key press before sending the response.</p>
<dt><code>-x</code></p>
<dd> challenge is hex encoded.</p>
<dt><code>-v</code></p>
<dd> enable verbose mode.</p>
<dt><code>-6</code></p>
<dd> output the response in OATH format, 6 digits.</p>
<dt><code>-8</code></p>
<dd> output the response in OATH format, 8 digits.</p>
<dt><code>-t</code></p>
<dd> use current time as challenge instead of reading challenge from command line (as in default TOTP mode, seconds since 1970-01-01 00:00:00 / 30 encoded as an 8 byte challenge).</p>
<dt><code>-V</code></p>
<dd> print tool version and exit. </p>
</dl>
<h2>EXAMPLE</h2>
<p> The YubiKey challenge-response operation can be demonstrated using the <code>NIST PUB 198 A.2</code> test vector. </p>
<p> First, program a YubiKey with the test vector :</p>
<dl>
<dt>
<pre>
$ <code>ykpersonalize -2 -ochal-resp -ochal-hmac -ohmac-lt64 -a 303132333435363738393a3b3c3d3e3f40414243</code>
 ...
<dd>Commit? (y/n) [n]: y
$
</pre>
<dt>
<dd>Now, send the NIST test challenge to the YubiKey and verify the result matches the expected :</p>
<dt>
<pre>
$ <code>ykchalresp -2 'Sample #2'</code>
<dd>0922d3405faa3d194f82a45830737d5cc6c75d24
$
</pre>
</dl>
<h2>BUGS</h2>
<p> Report ykchalresp bugs in the issue tracker &lt;URL: <a rel="nofollow" href="https://github.com/Yubico/yubikey-personalization/issues">https://github.com/Yubico/yubikey-personalization/issues</a> &gt;</p>
<h2>SEE ALSO</h2>
<p> The ykpersonalize home page &lt;URL: <a rel="nofollow" href="https://developers.yubico.com/yubikey-personalization/">https://developers.yubico.com/yubikey-personalization/</a> &gt; </p>
<p> YubiKeys can be obtained from Yubico &lt;URL: <a rel="nofollow" href="http://www.yubico.com/">http://www.yubico.com/</a> &gt;. </p>
<h2>Index</h2>
