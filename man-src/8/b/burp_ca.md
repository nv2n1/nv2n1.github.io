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
<dt><code>-h|&#8211;help</code></dt>
<dd>show help</dd>
<dt><code>-i|&#8211;init</code></dt>
<dd>inititalize CA</dd>
<dt><code>-k|&#8211;key</code></dt>
<dd>generate new key</dd>
<dt><code>-r|&#8211;request </code></dt>
<dd>generate certificate sign request</dd>
<dt><code>-s|&#8211;sign</code></dt>
<dd>sign csr (use &#8211;ca &lt;ca&gt; and &#8211;name &lt;name&gt;)</dd>
<dd><code>&#8211;batch</code> do not prompt for anything</dd>
<dd><code>&#8211;revoke</code> <code>&lt;number&gt;</code> revoke certificate with serial number</dd>
<dd><code>&#8211;crl</code> generate certificate revoke list</dd>
<dt><code>-d|&#8211;dir</code> <code>&lt;dir&gt;</code></dt>
<dd>ca output dir (default: /etc/burp/CA)</dd>
<dt><code>-c|&#8211;config</code></dt>
<dd>config file (default: /etc/burp/CA.cnf)</dd>
<dt><code>-n|&#8211;name</code></dt>
<dd>name (default: builder)</dd>
<dt><code>-D|&#8211;days</code></dt>
<dd>valid days for certificate (default in config file)</dd>
<dd><code>&#8211;ca_days</code> valid days for CA certificate (default: 3650)</dd>
<dt><code>-S|&#8211;size</code></dt>
<dd>key size (default: 2048)</dd>
<dt><code>-a|&#8211;ca</code></dt>
<dd>ca name if different from name</dd>
<dt><code>-f|&#8211;dhfile</code> <code>&lt;path&gt;</code></dt>
<dd>generate a new dhfile</dd></dl>
<h2></h2>
<h2>Bugs</h2>
<p>If you find bugs, please report them to the email list. See the website &lt;<a rel="nofollow" href="http://burp.grke.net/">http://burp.grke.net/</a>&gt; for details. </p>
<h2>Author</h2>
<p>The main author of Burp is Graham Keeling.</p>
<h2>Copyright</h2>
<p>See the LICENCE file included with the source distribution.</p>
