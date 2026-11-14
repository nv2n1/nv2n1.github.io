---
title: "smbencrypt(1)"
name: "smbencrypt"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smbencrypt/"
description: "smbencrypt – produce LM & NT password hashes from cleartext passwords"
---

<h2>NAME</h2>
<p> smbencrypt &#8211; produce LM &amp; NT password hashes from cleartext passwords</p>
<h2>SYNOPSIS</h2>
<p> <code>smbencrypt </code><i>password</i> [<i>password &#8230;</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>smbencrypt</code> For each cleartext password passed on the command line emit the LM-Password and NT-Password hashes for that password. </p>
<h2>EXAMPLE</h2>
<pre><code>
$ smbencrypt foo bar
    LM Hash NT Hash-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --5BFAFBEBFB6A0942AAD3B435B51404EE AC8E657F83DF82BEEA5D43BDAF7800CC
        A6428F2551EDEE1BAAD3B435B51404EE 86C156FC198B358CCCF6278D8BD49B6A
</code></pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-radiusd/">radiusd</a>(8)</p>
<h2>AUTHORS</h2>
<h2>Index</h2>
