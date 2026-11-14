---
title: "hosts-conf(5)"
name: "hosts-conf"
section: "5"
letter: "h"
url: "/docs/linux/man/5-hosts-conf/"
description: "hosts.conf – Access control for Network UPS Tools CGI programs"
---

<p>hosts.conf &#8211; Access control for Network UPS Tools CGI programs</p>
<h2>Description</h2>
<p>The CGI programs (<code><a href="/docs/linux/man/8-upsset-cgi/">upsset.cgi</a></code>(8), <code><a href="/docs/linux/man/8-upsstats-cgi/">upsstats.cgi</a></code>(8), <code><a href="/docs/linux/man/8-upsimage-cgi/">upsimage.cgi</a></code>(8)) use this file to determine if they are allowed to talk to a host. This keeps random visitors from using your web server to annoy others by creating outgoing connections.</p>
<h2>Directives</h2>
<p><code>MONITOR</code> <i>ups</i> <i>description</i></p>
<dl>
<dd>The <i>ups</i> element is in the form upsname[@hostname[:port]]. To allow connections to a UPS called &quot;snoopy&quot; on a system called &quot;doghouse&quot; that runs upsd on port 7877, it would look like this: </p>
<dl>
<dd>
<pre>MONITOR snoopy [at] doghouse:7877 &quot;Joe Cool&quot;</pre>
</dl>
<p> The description must be one element, so if it has spaces, then it must be wrapped with quotes as shown above. The default hostname is &quot;localhost&quot;.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-upsset-cgi/">upsset.cgi</a></code>(8), <code><a href="/docs/linux/man/8-upsstats-cgi/">upsstats.cgi</a></code>(8), <code><a href="/docs/linux/man/8-upsimage-cgi/">upsimage.cgi</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
