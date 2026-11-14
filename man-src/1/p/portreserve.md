---
title: "portreserve(1)"
name: "portreserve"
section: "1"
letter: "p"
url: "/docs/linux/man/1-portreserve/"
description: "portreserve – reserve ports to prevent portmap mapping them"
---

<h2 class="name">NAME</h2>
<p> portreserve &#8211; reserve ports to prevent portmap mapping them </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>portreserve</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>portreserve</code> program aims to help services with well-known ports that lie in the <code>bindresvport</code> range. It prevents portmap (or other programs using <code>bindresvport</code>) from occupying a real service&#8217;s port by occupying it itself, until the real service tells it to release the port (generally in its init script). </p>
<p> It is intended that <code>portreserve</code> runs from an initscript of its own, and services wishing to interact with it should use <code>portrelease</code>. </p>
<p> When the <code>portreserve</code> daemon is started, it examines the /etc/portreserve/ directory. Each file not containing &#8220;.&#8221; or &#8220;~&#8221; in its name is considered to be a service configuration file, and must contain a service name (as listed in /etc/services) or a port number. UDP services may be specified by appending &quot;/udp&quot; to the service name, and TCP services by &quot;/tcp&quot;. Several services may be specified, one per line. </p>
<p> For example, /etc/portreserve/cups might contain the string &#8220;ipp&#8221; or, equivalently, &#8220;ipp/tcp&#8221; and &#8220;ipp/udp&#8221; on separate lines. </p>
<p> For each service configuration file, a socket is created and bound to the appropriate port. A service wishing to bind to its port must first run <code>portrelease</code>, which instructs <code>portreserve</code> to release the port associated with the service. </p>
<p> Once all the reserved ports have been released, the daemon exits.</p>
<h2>FILES</h2>
<p> /etc/portreserve/*</p>
<dl>
<dt>
<dd> Service configuration files</dl>
<p> /var/run/portreserve/socket</p>
<dl>
<dt>
<dd> communication socket for <code>portrelease</code></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-portrelease/">portrelease</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
