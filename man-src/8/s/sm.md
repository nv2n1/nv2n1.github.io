---
title: "sm(8)"
name: "sm"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sm/"
description: "sm – Jabber IM session manager"
---

<p>sm &#8211; Jabber IM session manager</p>
<h2>Synopsis</h2>
<p><code>sm</code> <i>[-h] [-c config] [-D]</i></p>
<h2>Description</h2>
<p><code>sm</code> provides instant messaging services to Jabber clients. It performs all the essential instant messaging services like rosters, presence tracking, message distribution and subscriptions, plus more advanced features.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Show summary of options.</p>
<dt><code>-c</code></p>
<dd>Alternate configuration file to use. The compiled-in default is /etc/jabberd/sm.xml.</p>
<dt><code>-D</code></p>
<dd>Print debugging output. You should configure jabberd with the &#8211;enable-debug switch to enable this.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-jabberd/">jabberd</a></code>(8) <code><a href="/docs/linux/man/8-c2s/">c2s</a></code>(8) <code><a href="/docs/linux/man/8-router/">router</a></code>(8) <code><a href="/docs/linux/man/8-s2s/">s2s</a></code>(8)</p>
<h2>Author</h2>
<p>Robert Norris &lt;rob [at] cataclysm.cx&gt;</p>
