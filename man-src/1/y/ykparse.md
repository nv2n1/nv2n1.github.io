---

title: "ykparse(1)"
name: "ykparse"
section: "1"
letter: "y"
url: "/docs/linux/man/1-ykparse/"
description: "ykparse – decrypt and show information inside a YubiKey OTP"
---

<p> ykparse &#8211; decrypt and show information inside a YubiKey OTP </p>
<h2>SYNOPSIS</h2>
<p> <code>ykparse</code> <i>AESKEY</i> <i>TOKEN</i></p>
<h2>DESCRIPTION</h2>
<p> Decrypt and display information inside a YubiKey OTP.</p>
<h2>OPTIONS</h2>
<p> <code>AESKEY</code></p>
<dl>
<dt>
</dt><dd> The 16-character AES-128 key to use in hex.</dd></dl>
<p> <code>TOKEN</code></p>
<dl>
<dt>
</dt><dd> The modhex encoded One-Time Password (OTP).</dd></dl>
<h2>EXAMPLES</h2>
<p> Typical usage of the tool is as follows. </p>
<dl>
<dt>
</dt><dd>
<pre>
ykparse ecde18dbe76fbd0c33330f1c354871db dteffujedcflcindvdbrblehecuitvjkjevvehjd
</pre>
</dd></dl>
<h2>SEE ALSO</h2>
<p> YubiKeys can be obtained from Yubico: <a rel="nofollow" href="http://www.yubico.com/">http://www.yubico.com/</a> </p>
