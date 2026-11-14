---
title: "cidr_table(5)"
name: "cidr_table"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cidr_table/"
description: "cidr_table – format of Postfix CIDR tables"
---

<p>cidr_table &#8211; format of Postfix CIDR tables</p>
<h2>Synopsis</h2>
<pre><code>postmap -q &quot;</code><i>string</i><code>&quot; cidr:/etc/postfix/</code><i>filename</i>
<code>postmap -q - cidr:/etc/postfix/</code><i>filename</i><code> &lt;</code><i>inputfile</i></pre>
<h2>Description</h2>
<p>The Postfix mail system uses optional lookup tables. These tables are usually in <code>dbm</code> or <code>db</code> format. Alternatively, lookup tables can be specified in CIDR (Classless Inter-Domain Routing) form. In this case, each input is compared against a list of patterns. When a match is found, the corresponding result is returned and the search is terminated. </p>
<p> To find out what types of lookup tables your Postfix system supports use the &quot;<code>postconf -m</code>&quot; command. </p>
<p> To test lookup tables, use the &quot;<code>postmap -q</code>&quot; command as described in the SYNOPSIS above.</p>
<h2>Table Format</h2>
<p>The general form of a Postfix CIDR table is:</p>
<dl>
<dt><i>pattern result</i></p>
<dd>When a search string matches the specified <i>pattern</i>, use the corresponding <i>result</i> value. The <i>pattern</i> must be in <i>network/prefix</i> or <i>network_address</i> form (see ADDRESS PATTERN SYNTAX below).</p>
<dt><code>!</code><i>pattern result</i></p>
<dd>When a search string does not match the specified <i>pattern</i>, use the specified <i>result</i> value. The <i>pattern</i> must be in <i>network/prefix</i> or <i>network_address</i> form (see ADDRESS PATTERN SYNTAX below). </p>
<p> This feature is available in Postfix 3.2 and later.</p>
<dt><code>if </code><i>pattern</i></p>
<dd>
<dt><code>endif</code></p>
<dd>When a search string matches the specified <i>pattern</i>, match that search string against the patterns between <code>if</code> and <code>endif</code>. The <i>pattern</i> must be in <i>network/prefix</i> or <i>network_address</i> form (see ADDRESS PATTERN SYNTAX below). The <code>if</code>..<code>endif</code> can nest. </p>
<p> Note: do not prepend whitespace to text between <code>if</code>..<code>endif</code>. </p>
<p> This feature is available in Postfix 3.2 and later.</p>
<dt><code>if !</code><i>pattern</i></p>
<dd>
<dt><code>endif</code></p>
<dd>When a search string does not match the specified <i>pattern</i>, match that search string against the patterns between <code>if</code> and <code>endif</code>. The <i>pattern</i> must be in <i>network/prefix</i> or <i>network_address</i> form (see ADDRESS PATTERN SYNTAX below). The <code>if</code>..<code>endif</code> can nest. </p>
<p> Note: do not prepend whitespace to text between <code>if</code>..<code>endif</code>. </p>
<p> This feature is available in Postfix 3.2 and later.</p>
<dt>blank lines and comments</p>
<dd>Empty lines and whitespace-only lines are ignored, as are lines whose first non-whitespace character is a `#&#8217;.</p>
<dt>multi-line text</p>
<dd>A logical line starts with non-whitespace text. A line that starts with whitespace continues a logical line.</dl>
<h2>Table Search Order</h2>
<p>Patterns are applied in the order as specified in the table, until a pattern is found that matches the search string.</p>
<h2>Address Pattern Syntax</h2>
<p>Postfix CIDR tables are pattern-based. A pattern is either a <i>network_address</i> which requires an exact match, or a <i>network_address/prefix_length</i> where the <i>prefix_length</i> part specifies the length of the <i>network_address</i> prefix that must be matched (the other bits in the <i>network_address</i> part must be zero). </p>
<p> An IPv4 network address is a sequence of four decimal octets separated by &quot;.&quot;, and an IPv6 network address is a sequence of three to eight hexadecimal octet pairs separated by &quot;:&quot; or &quot;::&quot;, where the latter is short-hand for a sequence of one or more all-zero octet pairs. The pattern 0.0.0.0/0 matches every IPv4 address, and ::/0 matches every IPv6 address. IPv6 support is available in Postfix 2.2 and later. </p>
<p> Before comparisons are made, lookup keys and table entries are converted from string to binary. Therefore, IPv6 patterns will be matched regardless of leading zeros (a leading zero in an IPv4 address octet indicates octal notation). </p>
<p> Note: address information may be enclosed inside &quot;[]&quot; but this form is not required.</p>
<h2>Example Smtpd Access Map</h2>
<pre>/etc/postfix/main.cf:
 smtpd_client_restrictions = ... cidr:/etc/postfix/client.cidr ...
/etc/postfix/client.cidr:
 # Rule order matters. Put more specific whitelist entries
 # before more general blacklist entries.
 192.168.1.1 OK
 192.168.0.0/16 REJECT
 2001:db8::1 OK
 2001:db8::/32 REJECT</pre>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/1-postmap/">postmap</a>(1), Postfix lookup table manager
<a href="//www.systutorials.com/docs/linux/man/5-regexp_table/">regexp_table</a>(5), format of regular expression tables
<a href="//www.systutorials.com/docs/linux/man/5-pcre_table/">pcre_table</a>(5), format of PCRE tables</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>DATABASE_README, Postfix lookup table overview</pre>
<h2>History</h2>
<p>CIDR table support was introduced with Postfix version 2.1.</p>
<h2>Author(S)</h2>
<pre>The CIDR table lookup code was originally written by:
Jozsef Kadlecsik
KFKI Research Institute for Particle and Nuclear Physics
POB. 49
1525 Budapest, Hungary
Adopted and adapted by:
Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Wietse Venema
Google, Inc.
111 8th Avenue
New York, NY 10011, USA</pre>
