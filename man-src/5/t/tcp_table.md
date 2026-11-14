---
title: "tcp_table(5)"
name: "tcp_table"
section: "5"
letter: "t"
url: "/docs/linux/man/5-tcp_table/"
description: "tcp_table – Postfix client/server table lookup protocol"
---

<p>tcp_table &#8211; Postfix client/server table lookup protocol</p>
<h2>Synopsis</h2>
<pre><code>postmap -q &quot;</code><i>string</i><code>&quot; tcp:</code><i>host:port</i>
<code>postmap -q - tcp:</code><i>host:port</i><code> &lt;</code><i>inputfile</i></pre>
<h2>Description</h2>
<p>The Postfix mail system uses optional tables for address rewriting or mail routing. These tables are usually in <code>dbm</code> or <code>db</code> format. Alternatively, table lookups can be directed to a TCP server. </p>
<p> To find out what types of lookup tables your Postfix system supports use the &quot;<code>postconf -m</code>&quot; command. </p>
<p> To test lookup tables, use the &quot;<code>postmap -q</code>&quot; command as described in the SYNOPSIS above.</p>
<h2>Protocol Description</h2>
<p>The TCP map class implements a very simple protocol: the client sends a request, and the server sends one reply. Requests and replies are sent as one line of ASCII text, terminated by the ASCII newline character. Request and reply parameters (see below) are separated by whitespace. </p>
<p> Send and receive operations must complete in 100 seconds.</p>
<h2>Request Format</h2>
<p>The tcp_table protocol supports only the lookup request. The request has the following form:</p>
<dl>
<dt><code>get</code> SPACE <i>key</i> NEWLINE</p>
<dd>Look up data under the specified key.</dl>
<p> Postfix will not generate partial search keys such as domain names without one or more subdomains, network addresses without one or more least-significant octets, or email addresses without the localpart, address extension or domain portion. This behavior is also found with cidr:, pcre:, and regexp: tables.</p>
<h2>Reply Format</h2>
<p>Each reply specifies a status code and text. Replies must be no longer than 4096 characters including the newline terminator.</p>
<dl>
<dt><code>500</code> SPACE <i>text</i> NEWLINE</p>
<dd>In case of a lookup request, the requested data does not exist. The text describes the nature of the problem.</p>
<dt><code>400</code> SPACE <i>text</i> NEWLINE</p>
<dd>This indicates an error condition. The text describes the nature of the problem. The client should retry the request later.</p>
<dt><code>200</code> SPACE <i>text</i> NEWLINE</p>
<dd>The request was successful. In the case of a lookup request, the text contains an encoded version of the requested data.</dl>
<h2>Encoding</h2>
<p>In request and reply parameters, the character %, each non-printing character, and each whitespace character must be replaced by %XX, where XX is the corresponding ASCII hexadecimal character value. The hexadecimal codes can be specified in any case (upper, lower, mixed). </p>
<p> The Postfix client always encodes a request. The server may omit the encoding as long as the reply is guaranteed to not contain the % or NEWLINE character.</p>
<h2>Security</h2>
<p>Do not use TCP lookup tables for security critical purposes. The client-server connection is not protected and the server is not authenticated.</p>
<h2>Bugs</h2>
<p>Only the lookup method is currently implemented. </p>
<p> The client does not hang up when the connection is idle for a long time.</p>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/1-postmap/">postmap</a>(1), Postfix lookup table manager
<a href="//www.systutorials.com/docs/linux/man/5-regexp_table/">regexp_table</a>(5), format of regular expression tables
<a href="//www.systutorials.com/docs/linux/man/5-pcre_table/">pcre_table</a>(5), format of PCRE tables
<a href="//www.systutorials.com/docs/linux/man/5-cidr_table/">cidr_table</a>(5), format of CIDR tables</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>DATABASE_README, Postfix lookup table overview</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Wietse Venema
Google, Inc.
111 8th Avenue
New York, NY 10011, USA</pre>
