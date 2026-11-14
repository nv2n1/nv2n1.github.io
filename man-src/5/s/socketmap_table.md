---
title: "socketmap_table(5)"
name: "socketmap_table"
section: "5"
letter: "s"
url: "/docs/linux/man/5-socketmap_table/"
description: "socketmap_table – Postfix socketmap table lookup client"
---

<p>socketmap_table &#8211; Postfix socketmap table lookup client</p>
<h2>Synopsis</h2>
<pre><code>postmap -q &quot;</code><i>string</i><code>&quot; socketmap:inet:</code><i>host</i><code>:</code><i>port</i><code>:</code><i>name</i>
<br>
<code>postmap -q &quot;</code><i>string</i><code>&quot; socketmap:unix:</code><i>pathname</i><code>:</code><i>name</i>
<code>postmap -q - socketmap:inet:</code><i>host</i><code>:</code><i>port</i><code>:</code><i>name</i><code> &lt;</code><i>inputfile</i>
<br>
<code>postmap -q - socketmap:unix:</code><i>pathname</i><code>:</code><i>name</i><code> &lt;</code><i>inputfile</i></pre>
<h2>Description</h2>
<p>The Postfix mail system uses optional tables for address rewriting. mail routing or policy lookup. </p>
<p> The Postfix socketmap client expects TCP endpoint names of the form <code>inet:</code><i>host</i><code>:</code><i>port</i><code>:</code><i>name</i>, or UNIX-domain endpoints of the form <code>unix:</code><i>pathname</i><code>:</code><i>name</i>. In both cases, <i>name</i> specifies the name field in a socketmap client request (see &quot;REQUEST FORMAT&quot; below).</p>
<h2>Protocol</h2>
<p>Socketmaps use a simple protocol: the client sends one request, and the server sends one reply. Each request and each reply are sent as one netstring object.</p>
<h2>Request Format</h2>
<p>The socketmap protocol supports only the lookup request. The request has the following form: </p>
<dl>
<dt><i>name</i><code> &lt;space&gt; </code><i>key</i></p>
<dd>Search the named socketmap for the specified key.</dl>
<p> Postfix will not generate partial search keys such as domain names without one or more subdomains, network addresses without one or more least-significant octets, or email addresses without the localpart, address extension or domain portion. This behavior is also found with cidr:, pcre:, and regexp: tables.</p>
<h2>Reply Format</h2>
<p>The Postfix socketmap client requires that replies are not longer than 100000 characters (not including the netstring encapsulation). Replies must have the following form:</p>
<dl>
<dt><code>OK &lt;space&gt; </code><i>data</i></p>
<dd>The requested data was found.</p>
<dt><code>NOTFOUND &lt;space&gt;</p>
<dd>The requested data was not found.</p>
<dt>TEMP &lt;space&gt; </code><i>reason</i></p>
<dd>
<dt><code>TIMEOUT &lt;space&gt; </code><i>reason</i></p>
<dd>
<dt><code>PERM &lt;space&gt; </code><i>reason</i></p>
<dd>The request failed. The reason, if non-empty, is descriptive text.</dl>
<h2>Security</h2>
<pre>This map cannot be used for security-sensitive information,
because neither the connection nor the server are authenticated.</pre>
<h2>See Also</h2>
<pre><a rel="nofollow" href="http://cr.yp.to/proto/netstrings.txt,">http://cr.yp.to/proto/netstrings.txt,</a> netstring definition
<a href="//www.systutorials.com/docs/linux/man/1-postconf/">postconf</a>(1), Postfix supported lookup tables
<a href="//www.systutorials.com/docs/linux/man/1-postmap/">postmap</a>(1), Postfix lookup table manager
<a href="//www.systutorials.com/docs/linux/man/5-regexp_table/">regexp_table</a>(5), format of regular expression tables
<a href="//www.systutorials.com/docs/linux/man/5-pcre_table/">pcre_table</a>(5), format of PCRE tables
<a href="//www.systutorials.com/docs/linux/man/5-cidr_table/">cidr_table</a>(5), format of CIDR tables</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>DATABASE_README, Postfix lookup table overview</pre>
<h2>Bugs</h2>
<p>The protocol limits are not yet configurable.</p>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>History</h2>
<p>Socketmap support was introduced with Postfix version 2.10.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Wietse Venema
Google, Inc.
111 8th Avenue
New York, NY 10011, USA</pre>
