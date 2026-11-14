---
title: "sessionstats(1)"
name: "sessionstats"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sessionstats/"
description: "sessionStats — show cjdns crypto sessions"
---

<p><code>sessionStats</code> &#8212; show cjdns crypto sessions</p>
<h2>Synopsis</h2>
<p><code>sessionStats</code></p>
<h2>Description</h2>
<p>Cjdroute always talks to other nodes over a &quot;session&quot; similar to a TLS session. A session is required not only to talk to each peer, but also when talking to intermediate nodes to ask them about their peers when planning a route. </p>
<p> The cjdns protocol offers Perfect Forward Secrecy. Each session has a random symmetric key that encrypts that session. If a node is compromised, the attacker can get the session keys and read current and future sessions. However, the session keys are securely erased when a session is destroyed, so that past sessions (before the compromise) cannot be read. The lifetime of a session is somewhat random. Cjdroute caches recently active sessions, and destroys sessions that have not been used for a while.</p>
<h2>Usage</h2>
<p>Running sessionStats requires admin privilege. The cjdnsadmin lib will try to read <code>/etc/cjdroute.conf</code> for the admin password. This will normally succeed only for root. Otherwise, it tries <code>~/.cjdnsadmin</code></p>
<h2>Files</h2>
<p><code>~/.cjdnsadmin</code> <code>/etc/cjdroute.conf</code></p>
<h2>Bugs</h2>
<p>If you get a TypeError, you probably have the wrong admin password.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-cjdroute/">cjdroute</a>(1), <a href="/docs/linux/man/1-peerstats/">peerStats</a>(1) <a href="/docs/linux/man/1-sessionstats/">sessionStats</a>(1) &#8212; show cjdns crypto sessions =============================================</p>
<h2>Synopsis</h2>
<p><code>sessionStats</code></p>
<h2>Description</h2>
<p>Cjdroute always talks to other nodes over a &quot;session&quot; similar to a TLS session. A session is required not only to talk to each peer, but also when talking to intermediate nodes to ask them about their peers when planning a route. </p>
<p> The cjdns protocol offers Perfect Forward Secrecy. Each session has a random symmetric key that encrypts that session. If a node is compromised, the attacker can get the session keys and read current and future sessions. However, the session keys are securely erased when a session is destroyed, so that past sessions (before the compromise) cannot be read. The lifetime of a session is somewhat random. Cjdroute caches recently active sessions, and destroys sessions that have not been used for a while.</p>
<h2>Usage</h2>
<p>Running sessionStats requires admin privilege. The cjdnsadmin lib will try to read <code>/etc/cjdroute.conf</code> for the admin password. This will normally succeed only for root. Otherwise, it tries <code>~/.cjdnsadmin</code></p>
<h2>Files</h2>
<p><code>~/.cjdnsadmin</code> <code>/etc/cjdroute.conf</code></p>
<h2>Bugs</h2>
<p>If you get a TypeError, you probably have the wrong admin password.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-cjdroute/">cjdroute</a>(1), <a href="/docs/linux/man/1-peerstats/">peerStats</a>(1)</p>
