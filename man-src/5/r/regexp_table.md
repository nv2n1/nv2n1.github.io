---
title: "regexp_table(5)"
name: "regexp_table"
section: "5"
letter: "r"
url: "/docs/linux/man/5-regexp_table/"
description: "regexp_table – format of Postfix regular expression tables"
---

<p>regexp_table &#8211; format of Postfix regular expression tables</p>
<h2>Synopsis</h2>
<pre><code>postmap -q &quot;</code><i>string</i><code>&quot; regexp:/etc/postfix/</code><i>filename</i>
<code>postmap -q - regexp:/etc/postfix/</code><i>filename</i><code> &lt;</code><i>inputfile</i></pre>
<h2>Description</h2>
<p>The Postfix mail system uses optional tables for address rewriting, mail routing, or access control. These tables are usually in <code>dbm</code> or <code>db</code> format. </p>
<p> Alternatively, lookup tables can be specified in POSIX regular expression form. In this case, each input is compared against a list of patterns. When a match is found, the corresponding result is returned and the search is terminated. </p>
<p> To find out what types of lookup tables your Postfix system supports use the &quot;<code>postconf -m</code>&quot; command. </p>
<p> To test lookup tables, use the &quot;<code>postmap -q</code>&quot; command as described in the SYNOPSIS above. Use &quot;<code>postmap -hmq &#8211;</code> &lt;<i>file</i>&quot; for <a href="/docs/linux/man/5-header_checks/">header_checks</a>(5) patterns, and &quot;<code>postmap -bmq &#8211;</code> &lt;<i>file</i>&quot; for <a href="/docs/linux/man/5-body_checks/">body_checks</a>(5) (Postfix 2.6 and later).</p>
<h2>Compatibility</h2>
<p>With Postfix version 2.2 and earlier specify &quot;<code>postmap -fq</code>&quot; to query a table that contains case sensitive patterns. Patterns are case insensitive by default.</p>
<h2>Table Format</h2>
<p>The general form of a Postfix regular expression table is:</p>
<dl>
<dt><code>/</code><i>pattern</i><code>/</code><i>flags result</i></p>
<dd>When <i>pattern</i> matches the input string, use the corresponding <i>result</i> value.</p>
<dt><code>!/</code><i>pattern</i><code>/</code><i>flags result</i></p>
<dd>When <i>pattern</i> does <code>not</code> match the input string, use the corresponding <i>result</i> value.</p>
<dt><code>if /</code><i>pattern</i><code>/</code><i>flags</i></p>
<dd>
<dt><code>endif</code></p>
<dd>If the input string matches /<i>pattern</i>/, then match that input string against the patterns between <code>if</code> and <code>endif</code>. The <code>if</code>..<code>endif</code> can nest. </p>
<p> Note: do not prepend whitespace to patterns inside <code>if</code>..<code>endif</code>. </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<dt><code>if !/</code><i>pattern</i><code>/</code><i>flags</i></p>
<dd>
<dt><code>endif</code></p>
<dd>If the input string does not match /<i>pattern</i>/, then match that input string against the patterns between <code>if</code> and <code>endif</code>. The <code>if</code>..<code>endif</code> can nest. </p>
<p> Note: do not prepend whitespace to patterns inside <code>if</code>..<code>endif</code>. </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<dt>blank lines and comments</p>
<dd>Empty lines and whitespace-only lines are ignored, as are lines whose first non-whitespace character is a `#&#8217;.</p>
<dt>multi-line text</p>
<dd>A logical line starts with non-whitespace text. A line that starts with whitespace continues a logical line.</dl>
<p> Each pattern is a POSIX regular expression enclosed by a pair of delimiters. The regular expression syntax is documented in <code><a href="/docs/linux/man/7-re_format/">re_format</a></code>(7) with 4.4BSD, in <code><a href="/docs/linux/man/5-regex/">regex</a></code>(5) with Solaris, and in <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7) with Linux. Other systems may use other document names. </p>
<p> The expression delimiter can be any non-alphanumerical character, except whitespace or characters that have special meaning (traditionally the forward slash is used). The regular expression can contain whitespace. </p>
<p> By default, matching is case-insensitive, and newlines are not treated as special characters. The behavior is controlled by flags, which are toggled by appending one or more of the following characters after the pattern:</p>
<dl>
<dt><code>i</code> (default: on)</p>
<dd>Toggles the case sensitivity flag. By default, matching is case insensitive.</p>
<dt><code>m</code> (default: off)</p>
<dd>Toggle the multi-line mode flag. When this flag is on, the <code>^</code> and <code>$</code> metacharacters match immediately after and immediately before a newline character, respectively, in addition to matching at the start and end of the input string.</p>
<dt><code>x</code> (default: on)</p>
<dd>Toggles the extended expression syntax flag. By default, support for extended expression syntax is enabled.</dl>
<h2>Table Search Order</h2>
<p>Patterns are applied in the order as specified in the table, until a pattern is found that matches the input string. </p>
<p> Each pattern is applied to the entire input string. Depending on the application, that string is an entire client hostname, an entire client IP address, or an entire mail address. Thus, no parent domain or parent network search is done, and <i>user [at] domain</i> mail addresses are not broken up into their <i>user</i> and <i>domain</i> constituent parts, nor is <i>user+foo</i> broken up into <i>user</i> and <i>foo</i>.</p>
<h2>Text Substitution</h2>
<p>Substitution of substrings (text that matches patterns inside &quot;()&quot;) from the matched expression into the result string is requested with $1, $2, etc.; specify $$ to produce a $ character as output. The macros in the result string may need to be written as ${n} or $(n) if they aren&#8217;t followed by whitespace. </p>
<p> Note: since negated patterns (those preceded by <code>!</code>) return a result when the expression does not match, substitutions are not available for negated patterns.</p>
<h2>Example Smtpd Access Map</h2>
<pre># Disallow sender-specified routing. This is a must if you relay mail
# for other domains.
/[%!@].*[%!@]/ 550 Sender-specified routing rejected
# Postmaster is OK, that way they can talk to us about how to fix
# their problem.
/^postmaster@/ OK
# Protect your outgoing majordomo exploders
if !/^owner-/
/^(.*)-outgoing@(.*)$/ 550 Use ${1}@${2} instead
endif</pre>
<h2>Example Header Filter Map</h2>
<pre># These were once common in junk mail.
/^Subject: make money fast/ REJECT
/^To: friend [at] public\.com/ REJECT</pre>
<h2>Example Body Filter Map</h2>
<pre># First skip over base 64 encoded text to save CPU cycles.
~^[[:alnum:]+/]{60,}$~ OK
# Put your own body patterns here.</pre>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/1-postmap/">postmap</a>(1), Postfix lookup table manager
<a href="//www.systutorials.com/docs/linux/man/5-pcre_table/">pcre_table</a>(5), format of PCRE tables
<a href="//www.systutorials.com/docs/linux/man/5-cidr_table/">cidr_table</a>(5), format of CIDR tables</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>DATABASE_README, Postfix lookup table overview</pre>
<h2>Author(S)</h2>
<pre>The regexp table lookup code was originally written by:
LaMont Jones
lamont [at] hp.com
That code was based on the PCRE dictionary contributed by:
Andrew McNamara
andrewm [at] connect.com.au
connect.com.au Pty. Ltd.
Level 3, 213 Miller St
North Sydney, NSW, Australia
Adopted and adapted by:
Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Wietse Venema
Google, Inc.
111 8th Avenue
New York, NY 10011, USA</pre>
