---
title: "ldns-keygen(1)"
name: "ldns-keygen"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldns-keygen/"
description: "ldns-keygen – generate a DNSSEC key pair"
---

<h2>NAME</h2>
<p> ldns-keygen &#8211; generate a DNSSEC key pair</p>
<h2>SYNOPSIS</h2>
<p> <code>ldns-keygen </code> [ <i>OPTION</i> ] <i>DOMAIN</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>ldns-keygen</code> is used to generate a private/public keypair. When run, it will create 3 files; a .key file with the public DNSKEY, a .private file with the private keydata and a .ds with the DS record of the DNSKEY record. </p>
<p> <code>ldns-keygen</code> can also be used to create symmetric keys (for TSIG) by selecting the appropriate algorithm: <i>hmac-md5.sig-alg.reg.int</i>, <i>hmac-sha1</i> or <i>hmac-sha256</i>. In that case no DS record will be created and no .ds file. </p>
<p> <code>ldns-keygen</code> prints the basename for the key files: K&lt;name&gt;+&lt;alg&gt;+&lt;id&gt; </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a </code><i>&lt;algorithm&gt;</i></dt>
<dd> Create a key with this algorithm. Specifying &#8216;list&#8217; here gives a list of supported algorithms. Several alias names are also accepted (from older versions and other software), the list gives names from the RFC. Also the plain algo number is accepted. </dd>
<dt><code>-b </code><i>&lt;bits&gt;</i></dt>
<dd> Use this many bits for the key length. </dd>
<dt><code>-k</code></dt>
<dd> When given, generate a key signing key. This just sets the flag field to 257 instead of 256 in the DNSKEY RR in the .key file. </dd>
<dt><code>-r </code><i>device</i></dt>
<dd> Make ldns-keygen use this file to seed the random generator with. This will default to /dev/random. </dd>
<dt><code>-v</code></dt>
<dd> Show the version and exit </dd>
</dl>
<h2>AUTHOR</h2>
<p> Written by the ldns team as an example for ldns usage. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ldns-team [at] nlnetlabs.nl&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005-2008 NLnet Labs. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
