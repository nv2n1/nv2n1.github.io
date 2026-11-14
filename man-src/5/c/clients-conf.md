---
title: "clients-conf(5)"
name: "clients-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-clients-conf/"
description: "clients.conf – FreeRADIUS client configuration"
---

<p>clients.conf &#8211; FreeRADIUS client configuration</p>
<h2>Description</h2>
<p>The <i>clients.conf</i> file contains definitions of RADIUS clients. </p>
<p> The information in this file overrides any information provided in the deprecated <code>clients</code> and <code>naslist</code> files. </p>
<p> The file format is the same as that used for <i>radiusd.conf.</i> See <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5) for more details. </p>
<p> Each RADIUS client entry has the following basic form:</p>
<dl>
<dd>
<pre>client &lt;short-name&gt; {
 &lt;attribute&gt; = &lt;value&gt;
 }</pre>
</dl>
<p> Clients have many configuration parameters. Most are documented in the file itself as comments. This page documents only the format of the file. Please read the <code>clients.conf</code> file itself for more information. </p>
<p> The old-style format from 1.x is still accepted by the server, but that form is deprecated.</p>
<h2>Files</h2>
<p><i>/etc/raddb/clients.conf</i> </p>
<p> <i>/etc/raddb/radiusd.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5) </p>
<h2>Author</h2>
<p>FreeRADIUS is authored by the FreeRADIUS team. <a rel="nofollow" href="http://freeradius.org/">http://freeradius.org/</a></p>
