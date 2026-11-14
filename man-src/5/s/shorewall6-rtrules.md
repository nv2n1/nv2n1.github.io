---
title: "shorewall6-rtrules(5)"
name: "shorewall6-rtrules"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall6-rtrules/"
description: "rtrules – Shorewall6 Routing Rules file"
---

<p>rtrules &#8211; Shorewall6 Routing Rules file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall6/rtrules</code></dl>
<h2>Description</h2>
<dd>Entries in this file cause traffic to be routed to one of the providers listed in m[blue]<code>shorewall6-providers</code>m[]<font SIZE="-2">[1]</font>(5). </p>
<p> The columns in the file are as follows. </p>
<p> <code>SOURCE</code> (Optional) &#8211; {<code>&#8211;</code>|<i>interface</i>|<i>address</i>|<i>interface</i>:<i>&lt;address</i>&gt;}</p>
<dl>
<dd>An ip <i>address</i> (network or host) that matches the source IP address in a packet. May also be specified as an <i>interface</i> name optionally followed by &quot;:&quot; and an address. If the device <code>lo</code> is specified, the packet must originate from the firewall itself. </p>
<p> Beginning with Shorewall 4.5.0, you may specify &amp;<i>interface</i> in this column to indicate that the source is the primary IP address of the named interface. </p>
<p> Beginning with Shorewall 4.6.8, you may specify a comma-separated list of addresses in this column.</dl>
<p> <code>DEST</code> (Optional) &#8211; {<code>&#8211;</code>|<i>address</i>}</p>
<dl>
<dd>An ip address (network or host) that matches the destination IP address in a packet. </p>
<p> If you choose to omit either <code>SOURCE</code> or <code>DEST</code>, place &quot;-&quot; in that column. Note that you may not omit both <code>SOURCE</code> and <code>DEST</code>. </p>
<p> Beginning with Shorewall 4.6.8, you may specify a comma-separated list of addresses in this column.</dl>
<p> <code>PROVIDER</code> &#8211; {<i>provider-name</i>|<i>provider-number</i>|<code>main</code>}</p>
<dl>
<dd>The provider to route the traffic through. May be expressed either as the provider name or the provider number. May also be <code>main</code> or 254 for the main routing table. This can be used in combination with VPN tunnels, see example 2 below.</dl>
<p> <code>PRIORITY</code> &#8211; <i>priority</i><code>[!]</code></p>
<dl>
<dd>The rule&#8217;s numeric <i>priority</i> which determines the order in which the rules are processed. Rules with equal priority are applied in the order in which they appear in the file. </p>
<p> 1000-1999</p>
<dl>
<dd>Before Shorewall-generated &#8216;MARK&#8217; rules</dl>
<p> 11000-11999</p>
<dl>
<dd>After &#8216;MARK&#8217; rules but before Shorewall-generated rules for ISP interfaces.</dl>
<p> 26000-26999</p>
<dl>
<dd>After ISP interface rules but before &#8216;default&#8217; rule.</dl>
<p> Beginning with Shorewall 5.0.2, the priority may be followed optionally by an exclaimation mark (&quot;!&quot;). This causes the rule to remain in place if the interface is disabled.</dl>
<p> <code>MARK &#8211; {-|</code><i>mark</i><code>[/</code><i>mask</i><code>]}</code></p>
<dl>
<dd>Optional &#8212; added in Shorewall 4.4.25. For this rule to be applied to a packet, the packet&#8217;s mark value must match the <i>mark</i> when logically anded with the <i>mask</i>. If a <i>mask</i> is not supplied, Shorewall supplies a suitable provider mask.</dl>
<h2>Examples</h2>
<p>Example 1:</p>
<dl>
<dd>You want all traffic coming in on eth1 to be routed to the ISP1 provider. </p>
<dl>
<dd>
<pre> #SOURCE DEST PROVIDER PRIORITY MASK
 eth1 - ISP1 1000</pre>
</dl>
</dl>
<h2>Files</h2>
<p>/etc/shorewall6/rtrules</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/MultiISP.html">http://www.shorewall.net/MultiISP.html</a></code>m[]<font SIZE="-2">[2]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall6/">shorewall6</a>(8), <a href="/docs/linux/man/5-shorewall6-accounting/">shorewall6-accounting</a>(5), <a href="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5), <a href="/docs/linux/man/5-shorewall6-blacklist/">shorewall6-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall6-hosts/">shorewall6-hosts</a>(5), <a href="/docs/linux/man/5-shorewall6-interfaces/">shorewall6-interfaces</a>(5), <a href="/docs/linux/man/5-shorewall6-maclist/">shorewall6-maclist</a>(5), <a href="/docs/linux/man/5-shorewall6-netmap/">shorewall6-netmap</a>(5),<a href="/docs/linux/man/5-shorewall6-params/">shorewall6-params</a>(5), <a href="/docs/linux/man/5-shorewall6-policy/">shorewall6-policy</a>(5), <a href="/docs/linux/man/5-shorewall6-providers/">shorewall6-providers</a>(5), <a href="/docs/linux/man/5-shorewall6-routestopped/">shorewall6-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall6-rules/">shorewall6-rules</a>(5), <a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5), <a href="/docs/linux/man/5-shorewall6-secmarks/">shorewall6-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall6-tcclasses/">shorewall6-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall6-tcdevices/">shorewall6-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall6-mangle/">shorewall6-mangle</a>(5), <a href="/docs/linux/man/5-shorewall6-tos/">shorewall6-tos</a>(5), <a href="/docs/linux/man/5-shorewall6-tunnels/">shorewall6-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall6-zones/">shorewall6-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall6-providers</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-providers.html">http://www.shorewall.net/manpages6/shorewall6-providers.html</a></dl>
<dt> 2.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/MultiISP.html">http://www.shorewall.net/MultiISP.html</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/MultiISP.html">http://www.shorewall.net/MultiISP.html</a></dl>
