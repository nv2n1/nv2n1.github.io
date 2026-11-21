---
title: "gpg-check-pattern(1)"
name: "gpg-check-pattern"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpg-check-pattern/"
description: "gpg-check-pattern – Check a passphrase on stdin against the patternfile"
---

<h2>SYNOPSIS</h2>
<p> <code>gpg-check-pattern</code> [<i>options</i>] <i>patternfile</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>gpg-check-pattern</code> checks a passphrase given on stdin against a specified patternfile. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Produce verbose output</dd>
<dt><code>&#8211;check</code></dt>
<dd> run only a syntax check on the patternfile</dd>
<dt><code>-0</code>, <code>&#8211;null</code></dt>
<dd> input is expected to be null delimited</dd></dl>
<p> Please report bugs to &lt;<a rel="nofollow" href="https://dev.gnupg.org">https://dev.gnupg.org</a>&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2016 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt; </p>
<p> This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law. </p>
<p> This manpage was written by <code>Daniel Kahn Gillmor</code> for the Debian distribution (but may be used by others). </p>
