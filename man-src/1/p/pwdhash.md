---
title: "pwdhash(1)"
name: "pwdhash"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pwdhash/"
description: "pwdhash – Generator of password hashes"
---

<h2 class="name">NAME</h2>
<p> pwdhash &#8211; Generator of password hashes </p>
<h2>SYNOPSIS</h2>
<p> <code>pwdhash</code> [<i>-D config-dir</i>] [<i>-H</i>] [<i>-s scheme | -c comparepwd</i>] password </p>
<h2>DESCRIPTION</h2>
<p> Generates password hashes which can also be used in LDIF password fields. This uses the Directory Server password generator. </p>
<h2>OPTIONS</h2>
<p> A summary of options is included below:</p>
<dl>
<dt><code>-H</code></p>
<dd> Show summary of options.</p>
<dt><code>-s scheme</code></p>
<dd> Password scheme to be used (e.g. MD5, SHA1, SHA256, SHA512, SSHA, SSHA256, SSHA512)</p>
<dt><code>-c comparepassword</code></p>
<dd> Password to be compared against</p>
<dt><code>-D configdir</code></p>
<dd> Takes the password schema directly from the ns-slapd configuration
</dl>
<h2>AUTHOR</h2>
<p> dbscan was written by the 389 Project.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001 Sun Microsystems, Inc. Used by permission.<br />
 Copyright &#169; 2008 Red Hat, Inc.<br />
 This manual page was written by Michele Baldessari &lt;michele [at] pupazzo.org&gt;, for the Debian project (but may be used by others).<br />
 This is free software. You may redistribute copies of it under the terms of the Directory Server license found in the LICENSE file of this software distribution. This license is essentially the GNU General Public License version 2 with an exception for plug-in distribution. </p>
<h2>Index</h2>
