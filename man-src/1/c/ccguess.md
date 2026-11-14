---
title: "ccguess(1)"
name: "ccguess"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ccguess/"
description: "ccguess – search for ccrypt encryption keys"
---

<h2>NAME</h2>
<p> ccguess &#8211; search for ccrypt encryption keys</p>
<h2>SYNOPSIS</h2>
<pre>
<code>ccguess [</code><i>options</i>] <i>file</i>...
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>ccguess</code> program attempts to guess <code><a href="/docs/linux/man/1-ccrypt/">ccrypt</a></code>(1) encryption keys by searching the relevant part of the key space. This is done by prompting the user for an <i>approximate key</i> and then trying many variations of this key. This is intended to assist <code>ccrypt</code> users in recovering mistyped or forgotten keys, provided that they remember at least part of the key. </p>
<p> Note that <code>ccrypt</code> provides strong cryptographic security: there are no special back doors or shortcuts to recovering forgotten keys. Therefore, the <code>ccguess</code> program does not have any special powers. It simply works by trying different keys until a possible match is found. </p>
<p> A search of the entire key space is not usually a practical option. <code>ccguess</code> therefore works by prompting the user for an approximate key. It then tries all variations that can be obtained by applying a small number of changes. Here, each change is either a deletion of one letter, an insertion of one letter, a replacement of one letter by another, or a transposition of two adjacent letters. By default, <code>ccguess</code> searches all keys that differ from the approximate key by up to 5 changes. The number of changes searched can be adjusted with the <code>&#8211;depth</code> option. </p>
<p> The mechanism by which <code>ccguess</code> determines whether a key is a &quot;possible match&quot; is the same as that used by <code>ccrypt</code> to reject non-matching decryption keys. There is a small chance of a false match, i.e., <code>ccguess</code> may find a key that turns out not to be the true encryption key and does not decrypt the file correctly. A false match happens approximately once for every 4.3 billion keywords tried, so the longer your search goes on, the higher the likelihood that a false match is found. Normally, <code>ccguess</code> stops after the first possible match is found, but the <code>-c</code> option can be used to search for additional keys. The possibility of a false match can be further reduced by supplying multiple files that have been encrypted with the same key. In this case, <code>ccguess</code> will search for keys that match <i>any</i> of the files, but will print a warning for keys that do not match <i>all</i> of the files.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Help. Print usage information and exit.</p>
<dt><code>-L, &#8211;license</code></p>
<dd> Print license info and exit.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Print version info and exit.</p>
<dt><code>-K </code><i>key</i>, &#8211;key <i>key</i></p>
<dd> Specify the approximate key on the command line, rather than prompting the user for it.</p>
<dt><code>-d </code><i>n</i>, &#8211;depth <i>n</i></p>
<dd> Search keys that contain up to <i>n</i> changes. The default is 5.</p>
<dt><code>-c, &#8211;continue</code></p>
<dd> Keep trying more keys even after the first match is found. By default, <code>ccguess</code> will stop after the first key is found that matches all input files.</p>
<dt><code>-t </code><i>chars</i>, &#8211;chartable <i>chars</i></p>
<dd> Specify the list of characters to try for replacements and insertions. By default, <code>ccguess</code> will try all printable ASCII characters. If you know, for example, that your key only used lowercase letters and numbers, you can speed up the search by specifying a list of characters explicitly. This option is mutually exclusive with <code>-n</code>.</p>
<dt><code>-n, &#8211;non-printable</code></p>
<dd> Allow non-printable characters in keys. By default, <code>ccguess</code> will only try printable ASCII characters. Note that the use of this option slows down the search significantly. This option is mutually exclusive with <code>-t</code>.</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>file</i></p>
<dd> The name of a file that has been encrypted with the unknown key. This file is only read from, not written to. The special filename &quot;-&quot; is used to denote standard input. </p>
<p> If multiple files are specified, <code>ccguess</code> will search for keys that match <i>any</i> of the files, but will print a warning for keys that do not match <i>all</i> of the files.</dl>
<h2>EXAMPLE</h2>
<p> Suppose the file <i>myfile.cpt</i> has been encrypted with the key &quot;gardenhouse&quot;, but the user remembers &quot;gardenhose&quot;. The command </p>
<pre>
   ccguess -K gardenhose myfile.cpt
</pre>
<p> will find the correct key after 2318 guesses.</p>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 if at least one possible match is found, 1 if no matches are found, and &gt;=2 if an error occurred.</p>
<h2>VERSION</h2>
<p> 1.10</p>
<h2>AUTHOR</h2>
<p> Peter Selinger &lt;selinger at users.sourceforge.net&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2000-2012 Peter Selinger </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA. See also <a rel="nofollow" href="http://www.gnu.org/.">http://www.gnu.org/.</a> </p>
<h2>Index</h2>
