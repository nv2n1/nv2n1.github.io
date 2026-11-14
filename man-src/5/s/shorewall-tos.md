---
title: "shorewall-tos(5)"
name: "shorewall-tos"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-tos/"
description: "tos – Shorewall Type of Service rules file"
---

<p>tos &#8211; Shorewall Type of Service rules file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/tos</code></dl>
<h2>Description</h2>
<dd>This file defines rules for setting Type Of Service (TOS) </p>
<p> The columns in the file are as follows. </p>
<p> <code>SOURCE</code> &#8211; {<code>all</code>|<i>address</i>]|<code>all</code>:<i>address</i>|<code>$FW</code>}</p>
<dl>
<dd>If <code>all</code>, may optionally be followed by &quot;:&quot; and an IP address, a MAC address, a subnet specification or the name of an interface. </p>
<p> Example: all:192.168.2.3 </p>
<p> MAC addresses must be prefixed with &quot;~&quot; and use &quot;-&quot; as a separator. </p>
<p> Example: ~00-A0-C9-15-39-78</dl>
<p> <code>DEST</code> &#8211; {<code>all</code>|<i>address</i>]|<code>all</code>:<i>address</i>}</p>
<dl>
<dd>Example: 192.168.2.3</dl>
<p> <code>PROTOCOL</code> &#8211; <i>proto-name-or-number</i></p>
<dl>
<dd>Protocol name or number.</dl>
<p> <code>SOURCE PORT(S)</code> &#8211; {-|<i>port</i>|<i>lowport</i><code>:</code><i>highport</i>}</p>
<dl>
<dd>Source port or port range. If all ports, use &quot;-&quot;.</dl>
<p> <code>DEST PORT(S)</code> &#8211; {-|<i>port</i>|<i>lowport</i><code>:</code><i>highport</i>}</p>
<dl>
<dd>Destination port or port range. If all ports, use &quot;-&quot;</dl>
<p> <code>TOS</code> &#8211; <i>tos</i></p>
<dl>
<dd>Must be one of the following; </p>
<dl>
<dd>
<pre> <code>tos-minimize-delay</code> (16)
 <code>tos-maximize-throughput</code> (8)
 <code>tos-maximize-reliability</code> (4)
 <code>tos-minimize-cost</code> (2)
 <code>tos-normal-service</code> (0)</pre>
</dl>
</dl>
<p> <code>MARK</code> &#8211; [<code>!</code>]<i>value</i>[/<i>mask</i>][<code>:C</code>]</p>
<dl>
<dd>If you don&#8217;t want to define a test but need to specify anything in the following columns, place a &quot;-&quot; in this field. </p>
<p> !</p>
<dl>
<dd>Inverts the test (not equal)</dl>
<p> <i>value</i></p>
<dl>
<dd>Value of the packet or connection mark.</dl>
<p> <i>mask</i></p>
<dl>
<dd>A mask to be applied to the mark before testing.</dl>
<p> <code>:C</code></p>
<dl>
<dd>Designates a connection mark. If omitted, the packet mark&#8217;s value is tested.</dl>
</dl>
<h2>Files</h2>
<p>/etc/shorewall/tos</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall-interfaces/">shorewall-interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsec/">shorewall-ipsec</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-route_rules/">shorewall-route_rules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-tcrules/">shorewall-tcrules</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5) </p>
