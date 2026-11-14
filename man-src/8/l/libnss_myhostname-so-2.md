---
title: "libnss_myhostname-so-2(8)"
name: "libnss_myhostname-so-2"
section: "8"
letter: "l"
url: "/docs/linux/man/8-libnss_myhostname-so-2/"
description: "nss-myhostname, libnss_myhostname.so.2 – Provide hostname resolution for the locally configured system hostname."
---

<p>nss-myhostname, libnss_myhostname.so.2 &#8211; Provide hostname resolution for the locally configured system hostname.</p>
<h2>Synopsis</h2>
<p>libnss_myhostname.so.2</p>
<h2>Description</h2>
<p><code>nss-myhostname</code> is a plug-in module for the GNU Name Service Switch (NSS) functionality of the GNU C Library (<code>glibc</code>), primarily providing hostname resolution for the locally configured system hostname as returned by <code><a href="/docs/linux/man/2-gethostname/">gethostname</a></code>(2). The precise hostnames resolved by this module are: </p>
<dl>
<dd>&bull; The local, configured hostname is resolved to all locally configured IP addresses ordered by their scope, or &#8212; if none are configured &#8212; the IPv4 address 127.0.0.2 (which is on the local loopback) and the IPv6 address ::1 (which is the local host).</dl>
<dl>
<dd>&bull; The hostnames &quot;localhost&quot; and &quot;localhost.localdomain&quot; (as well as any hostname ending in &quot;.localhost&quot; or &quot;.localhost.localdomain&quot;) are resolved to the IP addresses 127.0.0.1 and ::1.</dl>
<dl>
<dd>&bull; The hostname &quot;_gateway&quot; is resolved to all current default routing gateway addresses, ordered by their metric. This assigns a stable hostname to the current gateway, useful for referencing it independently of the current network configuration state.</dl>
<p> Various software relies on an always-resolvable local hostname. When using dynamic hostnames, this is traditionally achieved by patching /etc/hosts at the same time as changing the hostname. This is problematic since it requires a writable /etc file system and is fragile because the file might be edited by the administrator at the same time. With <code>nss-myhostname</code> enabled, changing /etc/hosts is unnecessary, and on many systems, the file becomes entirely optional. </p>
<p> To activate the NSS modules, add &quot;myhostname&quot; to the line starting with &quot;hosts:&quot; in /etc/nsswitch.conf. </p>
<p> It is recommended to place &quot;myhostname&quot; last in the nsswitch.conf&#8217; &quot;hosts:&quot; line to make sure that this mapping is only used as fallback, and that any DNS or /etc/hosts based mapping takes precedence.</p>
<h2>Example</h2>
<p>Here is an example /etc/nsswitch.conf file that enables <code>nss-myhostname</code> correctly: </p>
<pre><code>passwd:         compat mymachines systemd
group:          compat mymachines systemd
shadow:         compat

hosts:          files mymachines resolve [!UNAVAIL=return] dns myhostname
networks:       files

protocols:      db files
services:       db files
ethers:         db files
rpc:            db files

netgroup:       nis</code></pre>
<p> To test, use <code>glibc</code>&#8216;s <code>getent</code> tool:</p>
<dl>
<dd>
<pre>$ getent ahosts `hostname`
::1 STREAM omega
::1 DGRAM
::1 RAW
127.0.0.2 STREAM
127.0.0.2 DGRAM
127.0.0.2 RAW</pre>
</dl>
<p> In this case, the local hostname is <i>omega</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-nss-systemd/">nss-systemd</a></code>(8), <code><a href="/docs/linux/man/8-nss-resolve/">nss-resolve</a></code>(8), <code><a href="/docs/linux/man/8-nss-mymachines/">nss-mymachines</a></code>(8), <code><a href="/docs/linux/man/5-nsswitch-conf/">nsswitch.conf</a></code>(5), <code><a href="/docs/linux/man/1-getent/">getent</a></code>(1) </p>
