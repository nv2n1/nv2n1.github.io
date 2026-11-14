---
title: "yp-conf(5)"
name: "yp-conf"
section: "5"
letter: "y"
url: "/docs/linux/man/5-yp-conf/"
description: "yp.conf – NIS binding configuration file"
---

<p>yp.conf &#8211; NIS binding configuration file</p>
<h2>Description</h2>
<p>The file /etc/yp.conf is read from <code><a href="/docs/linux/man/8-ypbind/">ypbind</a></code>(8) at startup or when receiving signal SIGHUP. The entries are used for the initial binding. Valid entries are </p>
<p> <code>domain</code> <i>nisdomain</i> <code>server</code> <i>hostname</i></p>
<dl>
<dd>Use server <i>hostname</i> for the domain <i>nisdomain</i>. You could have more then one entry of this type for a single domain.</dl>
<p> <code>domain</code> <i>nisdomain</i> <code>broadcast</code></p>
<dl>
<dd>Use broadcast on the local net for domain <i>nisdomain</i>.</dl>
<p> <code>domain</code> <i>nisdomain</i> <code>slp</code></p>
<dl>
<dd>Query the local running SLP server for hosts running ypserv and distributing <i>nisdomain</i>. This option is only available, if <code>ypbind</code> was compiled with SLP support.</dl>
<p> <code>ypserver</code> <i>hostname</i></p>
<dl>
<dd>Use server <i>hostname</i> for the local domain.</dl>
<p> <code>broadcast</code></p>
<dl>
<dd>If no other server is given or all of them are not reachable, try a broadcast call for the default domain to find a server.</dl>
<p> If for a specific domain the broadcast option and fixed server are given, <code>ypbind-mt</code> tries at first the given servers before falling back to broadcasting for a running server.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ypbind/">ypbind</a></code>(8)</p>
<h2>Author</h2>
<p><code>ypbind-mt</code> was written by Thorsten Kukuk &lt;kukuk [at] thkukuk.de&gt;.</p>
