---
title: "pskctool(1)"
name: "pskctool"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pskctool/"
description: "pskctool – Portable Symmetric Key Container (PSKC) tool"
---

<h2>NAME</h2>
<p> pskctool &#8211; Portable Symmetric Key Container (PSKC) tool</p>
<h2>SYNOPSIS</h2>
<p> <code>pskctool</code> [<i>OPTIONS</i>]&#8230; [<i>FILE</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> pskctool 2.4.1 </p>
<p> Manipulate Portable Symmetric Key Container (PSKC) data. </p>
<p> This tool allows you to parse, print, validate, sign and verify PSKC data. The input is provided in FILE or on standard input.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Print help and exit</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print version and exit</dd>
<dt><code>&#8211;strict</code></dt>
<dd> Fail hard on PSKC parse error (default=off)</dd>
<dt><code>-d</code>, <code>&#8211;debug</code></dt>
<dd> Show debug mesages on stderr (default=off)</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> Quiet operation (default=off)</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Produce more output (default=off)</dd></dl>
<p> Selecting one of the following modes is required:</p>
<dl>
<dt>
</dt><dd> Mode: info</dd>
<dt><code>-i</code>, <code>&#8211;info</code></dt>
<dd> Parse and print human readable summary of PSKC input (default=off)</dd>
<dt>
</dt><dd> Mode: validate</dd>
<dt><code>-e</code>, <code>&#8211;validate</code></dt>
<dd> Validate PSKC input against XML Schema (default=off)</dd>
<dt>
</dt><dd> Mode: sign</dd>
<dt>
</dt><dd> Digitally sign PSKC data</dd>
<dt><code>&#8211;sign</code></dt>
<dd> Sign PSKC input (default=off)</dd>
<dt><code>&#8211;sign-key</code>=<i>FILE</i></dt>
<dd> Private key to sign with</dd>
<dt><code>&#8211;sign-crt</code>=<i>FILE</i></dt>
<dd> X.509 certificate to sign with</dd>
<dt>
</dt><dd> Mode: verify</dd>
<dt>
</dt><dd> Verify digitally signed PSKC data</dd>
<dt><code>&#8211;verify</code></dt>
<dd> Verify signed PSKC input (default=off)</dd>
<dt><code>&#8211;verify-crt</code>=<i>FILE</i></dt>
<dd> Trusted X.509 certificate for verification</dd></dl>
<h2>EXAMPLES</h2>
<p> See &lt;<a rel="nofollow" href="http://www.nongnu.org/oath-toolkit/libpskc-api/pskc-tutorial-pskctool.html">http://www.nongnu.org/oath-toolkit/libpskc-api/pskc-tutorial-pskctool.html</a>&gt;.</p>
<h2>AUTHOR</h2>
<p> Written by Simon Josefsson.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to: oath-toolkit-help [at] nongnu.org pskctool home page: &lt;<a rel="nofollow" href="http://www.nongnu.org/oath-toolkit/">http://www.nongnu.org/oath-toolkit/</a>&gt;<br />
 General help using GNU software: &lt;<a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2013 Simon Josefsson. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law. </p>
