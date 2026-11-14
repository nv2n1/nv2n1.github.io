---
title: "libnss_mymachines-so-2(8)"
name: "libnss_mymachines-so-2"
section: "8"
letter: "l"
url: "/docs/linux/man/8-libnss_mymachines-so-2/"
description: "nss-mymachines, libnss_mymachines.so.2 – Provide hostname resolution for local container instances."
---

<p>nss-mymachines, libnss_mymachines.so.2 &#8211; Provide hostname resolution for local container instances.</p>
<h2>Synopsis</h2>
<p>libnss_mymachines.so.2</p>
<h2>Description</h2>
<p><code>nss-mymachines</code> is a plugin for the GNU Name Service Switch (NSS) functionality of the GNU C Library (<code>glibc</code>) providing hostname resolution for containers running locally, that are registered with <code><a href="/docs/linux/man/8-systemd-machined-service/">systemd-machined.service</a></code>(8). The container names are resolved to IP addresses of the specific container, ordered by their scope. </p>
<p> To activate the NSS modules, &quot;mymachines&quot; has to be added to the line starting with &quot;hosts:&quot; in /etc/nsswitch.conf. </p>
<p> It is recommended to place &quot;mymachines&quot; near the end of the nsswitch.conf line to make sure that this mapping is only used as fallback, and any DNS or /etc/hosts based mapping takes precedence.</p>
<h2>Example</h2>
<p>Here&#8217;s an example /etc/nsswitch.conf file, that enables <code>mymachines</code> correctly: </p>
<dl>
<dd>
<pre>passwd: compat
group: compat
shadow: compat
hosts: files dns <code>mymachines</code> myhostname
networks: files
protocols: db files
services: db files
ethers: db files
rpc: db files
netgroup: nis</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-machined-service/">systemd-machined.service</a></code>(8), <code><a href="/docs/linux/man/8-nss-myhostname/">nss-myhostname</a></code>(8), <code><a href="/docs/linux/man/5-nsswitch-conf/">nsswitch.conf</a></code>(5), <code><a href="/docs/linux/man/1-getent/">getent</a></code>(1) </p>
