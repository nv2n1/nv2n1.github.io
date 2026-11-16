---
title: "c2s(8)"
name: "c2s"
section: "8"
letter: "c"
url: "/docs/linux/man/8-c2s/"
description: "c2s – client-to-server connector"
---

<p>c2s &#8211; client-to-server connector</p>
<h2>Synopsis</h2>
<p><code>c2s</code> <i>[-h] [-c config] [-D]</i></p>
<h2>Description</h2>
<p><code>c2s</code> accepts incoming connections from clients, performs authentication and registration functions, and communicates with the session manager on their behalf.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></dt>
<dd>Show summary of options.</dd>
<dt><code>-c</code></dt>
<dd>Alternate configuration file to use. The compiled-in default is /etc/jabberd/c2s.xml.</dd>
<dt><code>-D</code></dt>
<dd>Print debugging output. You should configure jabberd with the &#8211;enable-debug switch to enable this.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-jabberd/">jabberd</a></code>(8) <code><a href="/docs/linux/man/8-router/">router</a></code>(8) <code><a href="/docs/linux/man/8-s2s/">s2s</a></code>(8) <code><a href="/docs/linux/man/8-sm/">sm</a></code>(8)</p>
<h2>Author</h2>
<p>Robert Norris &lt;rob [at] cataclysm.cx&gt;</p>
