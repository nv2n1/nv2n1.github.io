---
title: "router(8)"
name: "router"
section: "8"
letter: "r"
url: "/docs/linux/man/8-router/"
description: "router – XML packet distributor"
---

<p>router &#8211; XML packet distributor</p>
<h2>Synopsis</h2>
<p><code>router</code> <i>[-h] [-c config] [-D]</i></p>
<h2>Description</h2>
<p><code>router</code> is the core component of the jabberd system. It passes XML packets between the components, and manages the entry and exit of components onto the network.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Show summary of options.</p>
<dt><code>-c</code></p>
<dd>Alternate configuration file to use. The compiled-in default is /etc/jabberd/router.xml.</p>
<dt><code>-D</code></p>
<dd>Print debugging output. You should configure jabberd with the &#8211;enable-debug switch to enable this.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-jabberd/">jabberd</a></code>(8) <code><a href="/docs/linux/man/8-c2s/">c2s</a></code>(8) <code><a href="/docs/linux/man/8-s2s/">s2s</a></code>(8) <code><a href="/docs/linux/man/8-sm/">sm</a></code>(8)</p>
<h2>Author</h2>
<p>Robert Norris &lt;rob [at] cataclysm.cx&gt;</p>
