---
title: "heimdal-rshd(8)"
name: "heimdal-rshd"
section: "8"
letter: "h"
url: "/docs/linux/man/8-heimdal-rshd/"
description: "rshd – remote shell server"
---

<p><code>rshd</code> &#8211; remote shell server</p>
<h2>Synopsis</h2>
<p>[-<code>aiklnvxPL</code> ] [-<code>p </code><i>port</i> ]</p>
<h2>Description</h2>
<p>is the server for the <a href="/docs/linux/man/1-rsh/">rsh</a>(1) program. It provides an authenticated remote command execution service. Supported options are:</p>
<dl>
<dt> &#8211;<code>n</code> &#8211;<code>-no-keepalive</code></p>
<dd>
<dd>Disables keep-alive messages. Keep-alives are packets sent at certain intervals to make sure that the client is still there, even when it doesn&#8217;t send any data.</p>
<dt> &#8211;<code>k</code> &#8211;<code>-kerberos</code></p>
<dd>
<dd>Assume that clients connecting to this server will use some form of Kerberos authentication. See the Sx EXAMPLES section for a sample inetd.conf5 configuration.</p>
<dt> &#8211;<code>x</code> &#8211;<code>-encrypt</code></p>
<dd>
<dd>For Kerberos 4 this means that the connections are encrypted. Kerberos 5 can negotiate encryption even without this option, but if it&#8217;s present will deny unencrypted connections. This option implies &#8211;<code>k</code></p>
<dt> &#8211;<code>v</code> &#8211;<code>-vacuous</code></p>
<dd>
<dd>If the connecting client does not use any Kerberised authentication, print a message that complains about this fact, and exit. This is helpful if you want to move away from old port-based authentication.</p>
<dt> &#8211;<code>P</code></p>
<dd>
<dd>When using the AFS filesystem, users&#8217; authentication tokens are put in something called a PAG (Process Authentication Group). Multiple processes can share a PAG, but normally each login session has its own PAG. This option disables the Fn setpag call, so all tokens will be put in the default (uid-based) PAG, making it possible to share tokens between sessions. This is only useful in peculiar environments, such as some batch systems.</p>
<dt> &#8211;<code>i</code> &#8211;<code>-no-inetd</code></p>
<dd>
<dd>The &#8211;<code>i</code> option will cause to create a socket, instead of assuming that its stdin came from <a href="/docs/linux/man/8-inetd/">inetd</a>(8). This is mostly useful for debugging.</p>
<dt> &#8211;<code>p </code><i>port</i> &#8211;<code>-port= </code><i>port</i></p>
<dd>
<dd>Port to use with &#8211;<code>i</code></p>
<dt> &#8211;<code>a</code></p>
<dd>
<dd>This flag is for backwards compatibility only.</p>
<dt> &#8211;<code>L</code></p>
<dd>
<dd>This flag enables logging of connections to <a href="/docs/linux/man/8-syslogd/">syslogd</a>(8). This option is always on in this implementation.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/hosts.equiv </code></p>
<dd>
<dt><code>~/.rhosts </code></p>
<dd></dl>
<h2>Examples</h2>
<p>The following can be used to enable Kerberised rsh in inetd.cond5, while disabling non-Kerberised connections: </p>
<pre>shell stream tcp nowait root /usr/libexec/rshd rshd -v
kshell stream tcp nowait root /usr/libexec/rshd rshd -k
ekshell stream tcp nowait root /usr/libexec/rshd rshd -kx</pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-rsh/">rsh</a>(1), <a href="/docs/linux/man/3-iruserok/">iruserok</a>(3)</p>
<h2>History</h2>
<p>The command appeared in BSD 4.2</p>
<h2>Authors</h2>
<p>This implementation of was written as part of the Heimdal Kerberos 5 implementation.</p>
