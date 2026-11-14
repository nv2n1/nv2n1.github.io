---
title: "siggen(8)"
name: "siggen"
section: "8"
letter: "s"
url: "/docs/linux/man/8-siggen/"
description: "siggen – signature gathering routine for Tripwire"
---

<p>siggen &#8211; signature gathering routine for Tripwire</p>
<h2>Synopsis</h2>
<p><code>siggen</code> [ <code>-t</code>|<code>&#8211;terse</code> ] [ <code>-h</code>|<code>&#8211;hexadecimal</code> ] [ <code>-a</code>|<code>&#8211;all</code> ] [ <code>-C</code>|<code>&#8211;CRC32</code> ] [ <code>-S</code>|<code>&#8211;SHA</code> ] [ <code>-h</code>|<code>&#8211;HAVAL</code> ] <i>file1</i>,,,</p>
<h2>Description</h2>
<p><code>siggen</code> is a utility that displays the hash function values for the specified files.</p>
<h2>Options</h2>
<dl>
<dt><code>-t</code><i>, </i><code>&#8211;terse</code></p>
<dd>Terse mode. Prints requested hashes for a given file on one line, delimited by spaces, with no extraneous information.</p>
<dt><code>-h</code><i>, </i><code>&#8211;hexadecimal</code></p>
<dd>Display results in hexadecimal rather than base64 notation.</p>
<dt><code>-a</code><i>, </i><code>&#8211;all</code></p>
<dd>Display all hash function values (default).</p>
<dt><code>-C</code><i>, </i><code>&#8211;CRC32</code></p>
<dd>Display CRC-32, POSIX 1003.2 compliant 32-bit Cyclic Redundancy Check.</p>
<dt><code>-M</code><i>, </i><code>&#8211;MD5</code></p>
<dd>Display MD5, the RSA Data Security, Inc. Message Digest Algorithm.</p>
<dt><code>-S</code><i>, </i><code>&#8211;SHA</code></p>
<dd>Display SHA, <i>Tripwire</i>&#8216;s implementation of the NIST Secure Hash Standard, SHS (NIST FIPS 180).</p>
<dt><code>-H</code><i>, </i><code>&#8211;HAVAL</code></p>
<dd>Display Haval value, a 128-bit hash code.</p>
<dt><i>file1</i> [ <i>file2&#8230; </i>]</p>
<dd>List of filesystem objects for which to display values.</dl>
<h2>Version Information</h2>
<p>This man page describes <code>siggen</code> version 2.4.</p>
<h2>Authors</h2>
<p>Tripwire, Inc.</p>
<h2>Copying Permissions</h2>
<p>Permission is granted to make and distribute verbatim copies of this man page provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this man page under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this man page into another language, under the above conditions for modified versions, except that this permission notice may be stated in a translation approved by Tripwire, Inc. </p>
<p> Copyright 2000-2017 Tripwire, Inc. Tripwire is a registered trademark of Tripwire, Inc. in the United States and other countries. All rights reserved.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-twintro/">twintro</a></code>(8), <code><a href="/docs/linux/man/8-tripwire/">tripwire</a></code>(8), <code><a href="/docs/linux/man/8-twadmin/">twadmin</a></code>(8), <code><a href="/docs/linux/man/8-twprint/">twprint</a></code>(8), <code><a href="/docs/linux/man/4-twconfig/">twconfig</a></code>(4), <code><a href="/docs/linux/man/4-twpolicy/">twpolicy</a></code>(4), <code><a href="/docs/linux/man/5-twfiles/">twfiles</a></code>(5) </p>
