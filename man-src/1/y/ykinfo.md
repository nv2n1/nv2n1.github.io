---
title: "ykinfo(1)"
name: "ykinfo"
section: "1"
letter: "y"
url: "/docs/linux/man/1-ykinfo/"
description: "ykinfo – Get basic information from a YubiKey"
---

<h2>NAME</h2>
<p> ykinfo &#8211; Get basic information from a YubiKey</p>
<h2>SYNOPSIS</h2>
<p> <code>ykinfo</code> [<i>-s</i>] [<i>-m</i>] [<i>-H</i>] [<i>-v</i>] [<i>-t</i>] [<i>-p</i>] [<i>-1</i>] [<i>-2</i>] [<i>-q</i>] [<i>-V</i>] [<i>-h</i>]</p>
<h2>DESCRIPTION</h2>
<p> Get basic information from a YubiKey. Can get serial number, version and current touch level. Can get all parameters at once or one at a time. If <code>-q</code> is given only the relevant string from the YubiKey is written to screen.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s</code></p>
<dd> get the serial number and output it.</p>
<dt><code>-m</code></p>
<dd> get the serial number and output it as modhex.</p>
<dt><code>-H</code></p>
<dd> get the serial number and output it as hex.</p>
<dt><code>-v</code></p>
<dd> get the version and output it.</p>
<dt><code>-t</code></p>
<dd> get the touch level and output it.</p>
<dt><code>-p</code></p>
<dd> get the programming sequence and output it.</p>
<dt><code>-1</code></p>
<dd> get the status of slot 1, 1 for programmed and 0 for empty.</p>
<dt><code>-2</code></p>
<dd> get the status of slot 2, 1 for programmed and 0 for empty.</p>
<dt><code>-a</code></p>
<dd> get all the information above.</p>
<dt><code>-c</code></p>
<dd> get YubiKey capability information. <code>-q</code> modifier, only show the relevant data from the YubiKey, no extra information.</p>
<dt><code>-V</code></p>
<dd> print tool version and exit </p>
</dl>
<h2>EXAMPLE</h2>
<p> Output of all information from a YubiKey </p>
<pre>
$ <code>ykinfo -s -m -H -v -t -p</code>
serial: 1077254
serial_hex: 107006
serial_modhex: bcicch
version: 2.2.3
touch_level: 1793
programming_sequence: 1
$
</pre>
<h2>BUGS</h2>
<p> Report ykinfo bugs in the issue tracker &lt;URL: <a rel="nofollow" href="https://github.com/Yubico/yubikey-personalization/issues">https://github.com/Yubico/yubikey-personalization/issues</a> &gt;</p>
<h2>SEE ALSO</h2>
<p> The ykpersonalize home page &lt;URL: <a rel="nofollow" href="https://developers.yubico.com/yubikey-personalization/">https://developers.yubico.com/yubikey-personalization/</a> &gt; </p>
<p> YubiKeys can be obtained from Yubico &lt;URL: <a rel="nofollow" href="http://www.yubico.com/">http://www.yubico.com/</a> &gt;. </p>
<h2>Index</h2>
