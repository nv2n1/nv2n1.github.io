---
title: "relevation(1)"
name: "relevation"
section: "1"
letter: "r"
url: "/docs/linux/man/1-relevation/"
description: "relevation — command-line searcher for Revelation files"
---

<h2>NAME</h2>
<p> relevation &#8212; command-line searcher for <code>Revelation</code> files</p>
<h2>SYNOPSIS</h2>
<p> <code>relevation</code> [<code>options</code>] [<i>search string</i> [<i>&#8230;</i>] ]</p>
<h2>DESCRIPTION</h2>
<p> Access and print or search passwords in a <code>Revelation</code> password file. </p>
<p> Only read access is provided, to edit the files <code>Revelation</code> must be used. </p>
<p> With a search string, only entries that match the search string in any of its fields will be printed. </p>
<p> When no search string is provided the whole list of entries will be printed.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-f </code><i>file.revelation</i>, <code>&#8211;file=</code><i>file.revelation</i></p>
<dd> File name of the <code>revelation</code> file (the file containing the list of stored credentials).</p>
<dt><code>-p </code><i>password</i>, <code>&#8211;password=</code><i>password</i></p>
<dd> Decryption password.</p>
<dt><code>-a</code>, <code>&#8211;ask</code>, <code>-0</code>, <code>&#8211;stdin</code></p>
<dd> Ask interactively for password.</p>
<dt>
<dd> When <code>-a</code> or <code>&#8211;ask</code> is used a prompt will be printed.</p>
<dt>
<dd> Use either one of this variants or <code>&#8211;password</code>.</p>
<dt><code>-t </code><i>type</i>, <code>&#8211;type=</code><i>type</i></p>
<dd> Print only entries of a certain type.</p>
<dt>
<dd> Known types: creditcard, cryptokey, database, door, email, folder, ftp, generic, phone, shell, website.</p>
<dt>
<dd> If preceded by a slash it will be negated, i.e. `-website&#8217; will select entries that are not of type website.</p>
<dt>
<dd> When searching for a string, folders are skipped (equivalent to `&#8211;type=-folder&#8217;).</p>
<dt><code>-i</code>, <code>&#8211;case-insensitive</code></p>
<dd> When searching for text, disregard case.</p>
<dt>
<dd> This is the default behaviour.</p>
<dt>
<dd> If the search string contains special/non-English characters this is likely to fail.</p>
<dt><code>-c</code>, <code>&#8211;case-sensitive</code></p>
<dd> When searching for text, obey case.</p>
<dt><code>-A</code>, <code>&#8211;and</code></p>
<dd> When multiple search terms are used, use an AND operator to combine them. All search terms will be combined in a single search, only entries that match every search term will be selected.</p>
<dt><code>-O</code>, <code>&#8211;or</code></p>
<dd> When multiple search terms are used, use an OR operator to combine them. A different search will be issued for each search term. This is the default and the original mode of operation.</p>
<dt><code>-s </code><i>search string</i>, <code>&#8211;search=</code><i>search string</i>, <i>search string</i></p>
<dd> Search the file for a pice of text. All fields will be searched. There&#8217;s no need to use the <code>-s</code> or <code>&#8211;search</code> option names, any unnamed argument will be considered a search term.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version information for relevation.</dl>
<h2>CONFIGURATION FILE</h2>
<p> A configuration file `.relevation.conf&#8217; located at the user&#8217;s home directory can be used to avoid having to provide the filename and/or password on each run. </p>
<p> Example `~/.relevation.conf&#8217;: </p>
<pre><code>
&amp;nbsp;
[relevation] &amp; nbsp;
file = ~ / passwords.revelation &amp; nbsp;
password = my secret password &amp; nbsp;
mode = and
</code></pre>
<p> Both <code>file</code> and <code>password</code> are optional, so you can store the filename without storing the password. </p>
<p> Please understand your password is stored in this file in clear text, modify the file permissions appropriately so that only your user can read it, otherwise your master password might be compromised and hence all your stored password will be too. </p>
<p> <code>mode</code> is optional (&quot;<i>or</i>&quot; by default), only the values <i>and</i> and <i>or</i> are recognized, corresponding to the matching <code>&#8211;and</code> and <code>&#8211;or</code> options (any other value will be ignored).</p>
<h2>SEE ALSO</h2>
<p> revelation (1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Toni Corvera &lt;outlyer [at] gmail.com&gt;. Permission is granted to copy, distribute and/or modify this document under the terms of a BSD 2-clause license.<br />
&nbsp;<wbr> </p>
<h2>Index</h2>
