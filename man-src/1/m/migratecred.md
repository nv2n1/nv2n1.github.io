---
title: "migratecred(1)"
name: "migratecred"
section: "1"
letter: "m"
url: "/docs/linux/man/1-migratecred/"
description: "migratecred – Migrate credentials from one instance of Directory Server to another"
---

<h2 class="name">NAME</h2>
<p> migratecred &#8211; Migrate credentials from one instance of Directory Server to another </p>
<h2>SYNOPSIS</h2>
<p> <code>migratecred </code> -o OldInstancePath -n NewInstancePath -c OldCredential [<i>-p NewPluginPath</i>]</p>
<h2>DESCRIPTION</h2>
<p> migratecred migrates credentials from one Directory Server instance to the other. </p>
<p> New plugin path defaults to [<code>libdir</code>/dirsrv/plugins] if not given </p>
<p> <code>migratecred</code> is a program that migrates credentials used for replication and chaining. That is the password used by the server to perform the simple BIND operation for server to server communications.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below:</p>
<dl>
<dt><code>-o OldInstancePath</code></p>
<dd> Path to the source instance</p>
<dt><code>-n NewInstancePath</code></p>
<dd> Path to the destination instance</p>
<dt><code>-c OldCredential</code></p>
<dd> Old credential</p>
<dt><code>-p NewPluginPath</code></p>
<dd> New plugin path (of the new instance)
</dl>
<h2>AUTHOR</h2>
<p> migratecred was written by the 389 Project.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001 Sun Microsystems, Inc. Used by permission.<br />
 Copyright &#169; 2008 Red Hat, Inc.<br />
 This manual page was written by Michele Baldessari &lt;michele [at] pupazzo.org&gt;, for the Debian project (but may be used by others).<br />
 This is free software. You may redistribute copies of it under the terms of the Directory Server license found in the LICENSE file of this software distribution. This license is essentially the GNU General Public License version 2 with an exception for plug-in distribution. </p>
<h2>Index</h2>
