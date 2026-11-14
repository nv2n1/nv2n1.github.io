---
title: "clients(5)"
name: "clients"
section: "5"
letter: "c"
url: "/docs/linux/man/5-clients/"
description: "clients.conf – FreeRADIUS client configuration"
---

<p>clients.conf &#8211; FreeRADIUS client configuration</p>
<h2>Description</h2>
<p>The <i>clients.conf</i> file contains definitions of RADIUS clients. </p>
<p> The information in this file overrides any information provided in the deprecated <code><a href="/docs/linux/man/5-clients/">clients</a></code>(5) and <code><a href="/docs/linux/man/5-naslist/">naslist</a></code>(5) files. </p>
<p> The file format is the same as that used for <i>radiusd.conf.</i> See <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5) for more details. </p>
<p> Each RADIUS client entry has the following basic form:</p>
<dl>
<dd>
<pre>client &lt;short-name&gt; {
 &lt;attribute&gt; = &lt;value&gt;
 }</pre>
</dl>
<h2>Attributes</h2>
<p>The attributes that can appear in a <code>client</code> section are listed below. Required attributes are labelled as such. All other attributes are optional.</p>
<dl>
<dt><code>ipaddr [Required]</code></p>
<dd>The IP address of the client. For IPv6, use &quot;ipv6addr&quot;</p>
<dt><code>secret [Required]</code></p>
<dd>The RADIUS shared secret used for communication between the client/NAS and the RADIUS server.</p>
<dt><code>shortname [optional]</code></p>
<dd>A short alias that can be used in place of the IP address or fully qualified hostname provided in the first line of the section.</p>
<dt><code>nastype</code></p>
<dd>The nastype attribute is used to tell the <code>checkrad.pl</code> script which NAS-specific method it should use when checking simultaneous use. </p>
<p> The following values are currently recognized: </p>
<pre>cisco
computone
livingston
max40xx
multitech
netserver
pathras
patton
portslave
tc
usrhiper
other</pre>
<dt><code>login</code></p>
<dd>Reserved for future use.</p>
<dt><code>password</code></p>
<dd>Reserved for future use.</dl>
<h2>Examples</h2>
<pre><code>client localhost {
    ipaddr          = 127.0.0.1
    secret          = testing123
    shortname       = localhost
    nastype         = other
}</code></pre>
<p> This adds a client for the loopback address. This is useful in testing the server locally, for example with <code><a href="/docs/linux/man/1-radclient/">radclient</a></code>(1).</p>
<dl>
<dd>
<pre>client private-network-1 {
 ipaddr = 192.168.0.0
 netmask = 24
 secret = testing123-1
 shortname = private-network-1
}</pre>
</dl>
<p> This entry represents any client from the 192.168.0.0/24 network. The old-style format from 1.x is still accepted by the server, but that form is deprecated.</p>
<h2>Files</h2>
<p><i>/etc/raddb/clients.conf</i> </p>
<p> <i>/etc/raddb/radiusd.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5), <code><a href="/docs/linux/man/5-clients/">clients</a></code>(5), <code><a href="/docs/linux/man/5-naslist/">naslist</a></code>(5) </p>
<h2>Author</h2>
<p>FreeRADIUS is authored by the FreeRADIUS team. <a rel="nofollow" href="http://freeradius.org/">http://freeradius.org/</a></p>
