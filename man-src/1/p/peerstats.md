---
title: "peerstats(1)"
name: "peerstats"
section: "1"
letter: "p"
url: "/docs/linux/man/1-peerstats/"
description: "peerStats — show cjdns peers"
---

<p><code>peerStats</code> &#8212; show cjdns peers</p>
<h2>Synopsis</h2>
<p><code>peerStats</code></p>
<h2>Description</h2>
<p>Cjdroute talks to a number of immediate peers configured in <code>/etc/cjdroute.conf</code>. These can be discovered dynamically on local networks if &quot;beacon&quot; is enabled. Peers are enabled to connect to cjdroute by adding a login in &quot;authorizedPasswords&quot;. Connecting out to peers is configured in &quot;connectTo&quot; in either the IPv4 or IPv6 section. </p>
<p> No admin privilege is needed to run peerStats, but it looks in <code>~/.cjdnsadmin</code> for the IP and admin port of cjdroute.</p>
<h2>Files</h2>
<p><code>~/.cjdnsadmin</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-cjdroute/">cjdroute</a>(1), <a href="/docs/linux/man/1-sessionstats/">sessionStats</a>(1) <a href="/docs/linux/man/1-peerstats/">peerStats</a>(1) &#8212; show cjdns peers =============================================</p>
<h2>Synopsis</h2>
<p><code>peerStats</code></p>
<h2>Description</h2>
<p>Cjdroute talks to a number of immediate peers configured in <code>/etc/cjdroute.conf</code>. These can be discovered dynamically on local networks if &quot;beacon&quot; is enabled. Peers are enabled to connect to cjdroute by adding a login in &quot;authorizedPasswords&quot;. Connecting out to peers is configured in &quot;connectTo&quot; in either the IPv4 or IPv6 section. </p>
<p> No admin privilege is needed to run peerStats, but it looks in <code>~/.cjdnsadmin</code> for the IP and admin port of cjdroute.</p>
<h2>Files</h2>
<p><code>~/.cjdnsadmin</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-cjdroute/">cjdroute</a>(1), <a href="/docs/linux/man/1-sessionstats/">sessionStats</a>(1)</p>
