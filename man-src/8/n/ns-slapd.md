---
title: "ns-slapd(8)"
name: "ns-slapd"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ns-slapd/"
description: "ns-slapd – The main Directory Server daemon"
---

<p>ns-slapd &#8211; The main Directory Server daemon</p>
<h2>Synopsis</h2>
<p><code>ns-slapd</code> -D configdir [<i>-d debuglevel</i>] [<i>-i pidlogfile</i>] [<i>-v</i>] [<i>-V</i>]</p>
<h2>Description</h2>
<p>ns-slapd launches the LDAP Directory Server </p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-v</code></p>
<dd>Show version of program.</p>
<dt><code>-D configdir</code></p>
<dd>Specifies the configuration directory pointing at the instance to be started (e.g. /etc/dirsrv/slapd-localhost)</p>
<dt><code>-d debuglevel</code></p>
<dd>Specifies the debuglevel to be used</p>
<dt><code>-i pidlogfile</code></p>
<dd>Specifies file where the pid of the process will be stored
</dl>
<h2>Author</h2>
<p>ns-slapd was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2001 Sun Microsystems, Inc. Used by permission.<br />
 Copyright &#169; 2008 Red Hat, Inc.<br />
 This manual page was written by Michele Baldessari &lt;michele [at] pupazzo.org&gt;, for the Debian project (but may be used by others).<br />
 This is free software. You may redistribute copies of it under the terms of the Directory Server license found in the LICENSE file of this software distribution. This license is essentially the GNU General Public License version 2 with an exception for plug-in distribution.</p>
