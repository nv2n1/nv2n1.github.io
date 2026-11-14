---
title: "burp_ca(8)"
name: "burp_ca"
section: "8"
letter: "b"
url: "/docs/linux/man/8-burp_ca/"
description: "burp_ca – program for generating certificates for use with burp"
---

<p>burp_ca &#8211; program for generating certificates for use with burp</p>
<h2>Synopsis</h2>
<p><code>burp_ca</code> [<i>options</i>]<br />
 A script for generating certificates for use with burp. This script comes with the burp backup and restore package, and was contributed by Patrick Koppen. </p>
<h2>Options</h2>
<dl>
<dt><code>-h|&#8211;help</code></p>
<dd>show help</p>
<dt><code>-i|&#8211;init</code></p>
<dd>inititalize CA</p>
<dt><code>-k|&#8211;key</code></p>
<dd>generate new key</p>
<dt><code>-r|&#8211;request </code></p>
<dd>generate certificate sign request</p>
<dt><code>-s|&#8211;sign</code></p>
<dd>sign csr (use &#8211;ca &lt;ca&gt; and &#8211;name &lt;name&gt;)</p>
<dd><code>&#8211;batch</code> do not prompt for anything</p>
<dd><code>&#8211;revoke</code> <code>&lt;number&gt;</code> revoke certificate with serial number</p>
<dd><code>&#8211;crl</code> generate certificate revoke list</p>
<dt><code>-d|&#8211;dir</code> <code>&lt;dir&gt;</code></p>
<dd>ca output dir (default: /etc/burp/CA)</p>
<dt><code>-c|&#8211;config</code></p>
<dd>config file (default: /etc/burp/CA.cnf)</p>
<dt><code>-n|&#8211;name</code></p>
<dd>name (default: builder)</p>
<dt><code>-D|&#8211;days</code></p>
<dd>valid days for certificate (default in config file)</p>
<dd><code>&#8211;ca_days</code> valid days for CA certificate (default: 3650)</p>
<dt><code>-S|&#8211;size</code></p>
<dd>key size (default: 2048)</p>
<dt><code>-a|&#8211;ca</code></p>
<dd>ca name if different from name</p>
<dt><code>-f|&#8211;dhfile</code> <code>&lt;path&gt;</code></p>
<dd>generate a new dhfile</dl>
<h2></h2>
<h2>Bugs</h2>
<p>If you find bugs, please report them to the email list. See the website &lt;<a rel="nofollow" href="http://burp.grke.net/">http://burp.grke.net/</a>&gt; for details. </p>
<h2>Author</h2>
<p>The main author of Burp is Graham Keeling.</p>
<h2>Copyright</h2>
<p>See the LICENCE file included with the source distribution.</p>
