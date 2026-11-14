---
title: "natspec(1)"
name: "natspec"
section: "1"
letter: "n"
url: "/docs/linux/man/1-natspec/"
description: "natspec – command line utility to access libnatspec functions"
---

<h2 class="name">NAME</h2>
<p> natspec &#8211; command line utility to access libnatspec functions </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>natspec</code> [<code>-c</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;codepage</code>] [<code>-f</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;fsenc</code>] [<code>&#8211;utf8</code>] [<code>&#8211;country-id</code>] [<code>&#8211;system-locale</code>] [<code>-i</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;info</code>] [<code>-a&nbsp;<wbr></code><i>encoding</i>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;transl&nbsp;<wbr></code><i>encoding</i>] [<code>-v</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;verbose</code>] [<code>-s&nbsp;<wbr></code><i>operating system</i>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;charset&nbsp;<wbr></code><i>operating system</i>]</p>
<dt> <code>natspec</code> [<code>-h</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;help</code> | <code>-V</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;version</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>This manual page documents briefly the <code>natspec</code> command. </p>
<p> This manual page was written for the Debian distribution because the original program does not have a manual page. </p>
<p> <code>natspec</code> is a command line utility to access libnatspec functions.</p>
<h2>OPTIONS</h2>
<p> The program follows the usual GNU command line syntax, with long options starting with two dashes (&quot;-&quot;). A summary of options is included below. </p>
<p> <code>-c</code>, <code>&#8211;codepage</code></p>
<dl>
<dt>
<dd> Print DOS codepage for current locale.</dl>
<p> <code>-f</code>, <code>&#8211;fsenc</code></p>
<dl>
<dt>
<dd> Print filename encoding for current locale.</dl>
<p> <code>&#8211;utf8</code></p>
<dl>
<dt>
<dd> Return 0 if current locale uses UTF-8.</dl>
<p> <code>&#8211;country-id</code></p>
<dl>
<dt>
<dd> Print country ID for DOS.</dl>
<p> <code>&#8211;system-locale</code></p>
<dl>
<dt>
<dd> Print system locale.</dl>
<p> <code>-i</code>, <code>&#8211;info</code></p>
<dl>
<dt>
<dd> Print summary information about current locale.</dl>
<p> <code>-a </code><i>encoding</i>, <code>&#8211;transl=</code><i>encoding</i></p>
<dl>
<dt>
<dd> Transliterate <i>ARGS</i> from <i>encoding</i> to the current encoding and print the result.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Be verbose.</dl>
<p> <code>-s </code><i>operating system</i>, <code>&#8211;charset=</code><i>operating system</i></p>
<dl>
<dt>
<dd> Print charset for the <i>operating system</i>. <i>operating system</i> can be one of unix, win, dos, mac.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show summary of options.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Show version of program.</dl>
<p> When being called without options, <code>-i</code> is implied.</p>
<h2>ENVIRONMENT</h2>
<p> <code>LC_ALL</code></p>
<dl>
<dt>
<dd> Used for detecting current locale.</dl>
<h2>AUTHOR</h2>
<p> <code>Andrew Shadoura</code> &lt;bugzilla [at] tut.by&gt;</p>
<dl>
<dt>
<dd> Wrote this manpage for the Debian system.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2009 Andrew O. Shadoura </p>
<p> This manual page was written for the Debian system (and may be used by others). </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Lesser General Public License, Version 2.1 or (at your option) any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU Lesser General Public License can be found in /usr/share/common-licenses/LGPL-2.1. </p>
<h2>Index</h2>
