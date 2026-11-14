---
title: "mydns-conf(8)"
name: "mydns-conf"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mydns-conf/"
description: "mydns-conf – Sets up a MyDNS service"
---

<p>mydns-conf &#8211; Sets up a MyDNS service</p>
<h2>Synopsis</h2>
<p><code>mydns-conf</code> <i>logacct</i> <i>D</i></p>
<h2>Description</h2>
<p><code>mydns-conf</code> creates a service directory <i>D</i> that runs <code><a href="/docs/linux/man/8-mydns/">mydns</a></code>(8). The name <i>D</i> must start with a slash and must not contain any special characters. Normally <i>D</i> is <i>/etc/mydns</i>. </p>
<p> You can run the service under <code><a href="/docs/linux/man/8-svscan/">svscan</a></code>(8) by creating a symbolic link in the <code><a href="/docs/linux/man/8-svscan/">svscan</a></code>(8) directory: </p>
<p> ln -s <i>D</i> /service </p>
<p> The service will start within five seconds, and will be restarted upon reboot. You can use <code><a href="/docs/linux/man/8-svc/">svc</a></code>(8) to control the service. </p>
<p> <code>mydns-conf</code> creates an automatically rotated log directory in <i>D</i>/log/main. The logs are owned by <i>logacct</i>. The corresponding <code><a href="/docs/linux/man/8-multilog/">multilog</a></code>(8) processes run under the uid and gid of <i>logacct</i>. The name <i>logacct</i> must not contain any special characters.</p>
<h2>Author</h2>
<p>Don Moore &lt;bboy [at] bboy.net&gt; Howard Wilkinson &lt;howard [at] cohtech.com&gt;</p>
<h2>Homepage</h2>
<p><a rel="nofollow" href="http://mydns.bboy.net">http://mydns.bboy.net</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mydns/">mydns</a></code>(8), <code><a href="/docs/linux/man/5-mydns-conf/">mydns.conf</a></code>(5), <code><a href="/docs/linux/man/8-mydnsexport/">mydnsexport</a></code>(8), <code><a href="/docs/linux/man/8-mydnsimport/">mydnsimport</a></code>(8), <code><a href="/docs/linux/man/8-svscan/">svscan</a></code>(8), <code><a href="/docs/linux/man/8-svc/">svc</a></code>(8), <code><a href="/docs/linux/man/8-multilog/">multilog</a></code>(8) </p>
