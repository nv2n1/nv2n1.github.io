---
title: "nisplus_table(5)"
name: "nisplus_table"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nisplus_table/"
description: "nisplus_table – Postfix NIS+ client"
---

<p>nisplus_table &#8211; Postfix NIS+ client</p>
<h2>Synopsis</h2>
<pre><code>postmap -q &quot;</code><i>string</i><code>&quot; &quot;nisplus:[</code><i>name</i><code>=%s];</code><i>name.name.</i><code>&quot;</code>
<code>postmap -q - &quot;nisplus:[</code><i>name</i><code>=%s];</code><i>name.name.</i><code>&quot; &lt;</code><i>inputfile</i></pre>
<h2>Description</h2>
<p>The Postfix mail system uses optional lookup tables. These tables are usually in <code>dbm</code> or <code>db</code> format. Alternatively, lookup tables can be specified as NIS+ databases. </p>
<p> To find out what types of lookup tables your Postfix system supports use the &quot;<code>postconf -m</code>&quot; command. </p>
<p> To test Postfix NIS+ lookup tables, use the &quot;<code>postmap -q</code>&quot; command as described in the SYNOPSIS above.</p>
<h2>Query Syntax</h2>
<p>Most of the NIS+ query is specified via the NIS+ map name. The general format of a Postfix NIS+ map name is as follows: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>nisplus:[</code><i>name</i><code>=%s];</code><i>name.name.name</i><code>.:</code><i>column</i> </p>
<p> Postfix NIS+ map names differ from what one normally would use with commands such as <code>niscat</code>:</p>
<dl>
<dt>&bull;</p>
<dd>With each NIS+ table lookup, &quot;<code>%s</code>&quot; is replaced by a version of the lookup string. There can be only one &quot;<code>%s</code>&quot; instance in a Postfix NIS+ map name.</p>
<dt>&bull;</p>
<dd>Postfix NIS+ map names use &quot;<code>;</code>&quot; instead of &quot;<code>,</code>&quot;, because the latter character is special in the Postfix main.cf file. Postfix replaces &quot;<code>;</code>&quot; characters in the map name by &quot;<code>,</code>&quot; before making NIS+ queries.</p>
<dt>&bull;</p>
<dd>The &quot;:<i>column</i>&quot; part in the NIS+ map name is not part of the actual NIS+ query. Instead, it specifies the number of the table column that provides the lookup result. When no &quot;:<i>column</i>&quot; is specified the first column (1) is used.</dl>
<h2>Example</h2>
<p>A NIS+ aliases map might be queried as follows: </p>
<pre> alias_maps = dbm:/etc/mail/aliases,
 nisplus:[alias=%s];mail_aliases.org_dir.$mydomain.:1</pre>
<p>This queries the local aliases file before the NIS+ file.</p>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/1-postmap/">postmap</a>(1), Postfix lookup table manager</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>DATABASE_README, Postfix lookup table overview</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>Author(S)</h2>
<pre>Geoff Gibbs
UK-HGMP-RC
Hinxton
Cambridge
CB10 1SB, UK
Adopted and adapted by:
Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Wietse Venema
Google, Inc.
111 8th Avenue
New York, NY 10011, USA</pre>
