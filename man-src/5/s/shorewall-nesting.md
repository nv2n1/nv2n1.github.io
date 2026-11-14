---
title: "shorewall-nesting(5)"
name: "shorewall-nesting"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-nesting/"
description: "nesting – Shorewall Nested Zones"
---

<p>nesting &#8211; Shorewall Nested Zones</p>
<h2>Synopsis</h2>
<dl>
<dt> <i>child-zone</i>[:<i>parent-zone</i>[,<i>parent-zone</i>]&#8230;]</dl>
<h2>Description</h2>
<dd>In m[blue]<code>shorewall-zones</code>m[]<font SIZE="-2">[1]</font>(5), a zone may be declared to be a sub-zone of one or more other zones using the above syntax. The <i>child-zone</i> may be neither the firewall zone nor a vserver zone. The firewall zone may not appear as a parent zone, although all vserver zones are handled as sub-zones of the firewall zone. </p>
<p> Where zones are nested, the CONTINUE policy in m[blue]<code>shorewall-policy</code>m[]<font SIZE="-2">[2]</font>(5) allows hosts that are within multiple zones to be managed under the rules of all of these zones.</p>
<h2>Example</h2>
<p>/etc/shorewall/zones: </p>
<dl>
<dd>
<pre> #ZONE TYPE OPTION
 fw firewall
 net ipv4
 sam:net ipv4
 loc ipv4</pre>
</dl>
<p> /etc/shorewall/interfaces: </p>
<dl>
<dd>
<pre> #ZONE INTERFACE BROADCAST OPTIONS
 - eth0 detect dhcp,norfc1918
 loc eth1 detect</pre>
</dl>
<p> /etc/shorewall/hosts: </p>
<dl>
<dd>
<pre> #ZONE HOST(S) OPTIONS
 net eth0:0.0.0.0/0
 sam eth0:206.191.149.197</pre>
</dl>
<p> /etc/shorewall/policy: </p>
<dl>
<dd>
<pre> #SOURCE DEST POLICY LOG LEVEL
 loc net ACCEPT
 sam all CONTINUE
 net all DROP info
 all all REJECT info</pre>
</dl>
<p> The second entry above says that when Sam is the client, connection requests should first be processed under rules where the source zone is sam and if there is no match then the connection request should be treated under rules where the source zone is net. It is important that this policy be listed BEFORE the next policy (net to all). You can have this policy generated for you automatically by using the IMPLICIT_CONTINUE option in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[3]</font>(5). </p>
<p> Partial /etc/shorewall/rules: </p>
<dl>
<dd>
<pre> #ACTION SOURCE DEST PROTO DPORT
 ...
 DNAT sam loc:192.168.1.3 tcp ssh
 DNAT net loc:192.168.1.5 tcp www
 ...</pre>
</dl>
<p> Given these two rules, Sam can connect to the firewall&#8217;s internet interface with ssh and the connection request will be forwarded to 192.168.1.3. Like all hosts in the net zone, Sam can connect to the firewall&#8217;s internet interface on TCP port 80 and the connection request will be forwarded to 192.168.1.5. The order of the rules is not significant. Sometimes it is necessary to suppress port forwarding for a sub-zone. For example, suppose that all hosts can SSH to the firewall and be forwarded to 192.168.1.5 EXCEPT Sam. When Sam connects to the firewall&#8217;s external IP, he should be connected to the firewall itself. Because of the way that Netfilter is constructed, this requires two rules as follows: </p>
<dl>
<dd>
<pre> #ACTION SOURCE DEST PROTO DPORT
 ...
 ACCEPT+ sam $FW tcp ssh
 DNAT net loc:192.168.1.3 tcp ssh
 ...</pre>
</dl>
<p> The first rule allows Sam SSH access to the firewall. The second rule says that any clients from the net zone with the exception of those in the &#8220;sam&#8221; zone should have their connection port forwarded to 192.168.1.3. If you need to exclude more than one zone, simply use multiple ACCEPT+ rules. This technique also may be used when the ACTION is REDIRECT. </p>
<p> Care must be taken when nesting occurs as a result of the use of wildcard interfaces (interface names ends in &#8216;+&#8217;). </p>
<p> Here&#8217;s an example. /etc/shorewall/zones: </p>
<p> /etc/shorewall/interfaces: </p>
<dl>
<dd>
<pre> #ZONE INTERFACE BROADCAST OPTIONS
 net ppp0
 loc eth1
 loc ppp+
 dmz eth2</pre>
</dl>
<p> Because the net zone is declared before the loc zone, net is an implicit sub-zone of loc and in the absence of a net-&gt;&#8230; CONTINUE policy, traffic from the net zone will not be passed through loc-&gt;&#8230; rules. But DNAT and REDIRECT rules are an exception! </p>
<dl>
<dd>&bull; DNAT and REDIRECT rules generate two Netfilter rules: a &#8216;nat&#8217; table rule that rewrites the destination IP address and/or port number, and a &#8216;filter&#8217; table rule that ACCEPTs the rewritten connection.</dl>
<dl>
<dd>&bull; Policies only affect the &#8216;filter&#8217; table.</dl>
<p> As a consequence, the following rules will have unexpected behavior: </p>
<dl>
<dd>
<pre> #ACTION SOURCE DEST PROTO DPORT
 ACCEPT net dmz tcp 80
 REDIRECT loc 3128 tcp 80</pre>
</dl>
<p> The second rule is intended to redirect local web requests to a proxy running on the firewall and listening on TCP port 3128. But the &#8216;nat&#8217; part of that rule will cause all connection requests for TCP port 80 arriving on interface ppp+ (including ppp0!) to have their destination port rewritten to 3128. Hence, the web server running in the DMZ will be inaccessible from the web. </p>
<p> The above problem can be corrected in several ways. </p>
<p> The preferred way is to use the <code>ifname</code> pppd option to change the &#8216;net&#8217; interface to something other than ppp0. That way, it won&#8217;t match ppp+. </p>
<p> If you are running Shorewall version 4.1.4 or later, a second way is to simply make the nested zones explicit: </p>
<dl>
<dd>
<pre> #ZONE TYPE OPTION
 fw firewall
 loc ipv4
 net:loc ipv4
 dmz ipv4</pre>
</dl>
<p> If you take this approach, be sure to set IMPLICIT_CONTINUE=No in shorewall.conf. </p>
<p> When using other Shorewall versions, another way is to rewrite the DNAT rule (assume that the local zone is entirely within 192.168.2.0/23): </p>
<dl>
<dd>
<pre> #ACTION SOURCE DEST PROTO DPORT
 ACCEPT net dmz tcp 80
 REDIRECT loc:192.168.2.0/23 3128 tcp 80</pre>
</dl>
<p> Another way is to restrict the definition of the loc zone: </p>
<p> /etc/shorewall/interfaces: </p>
<dl>
<dd>
<pre> #ZONE INTERFACE BROADCAST OPTIONS
 net ppp0
 loc eth1
 - ppp+
 dmz eth2</pre>
</dl>
<p> /etc/shorewall/hosts: </p>
<dl>
<dd>
<pre> #ZONE HOST(S) OPTIONS
 loc ppp+:192.168.2.0/23</pre>
</dl>
<h2>Files</h2>
<p>/etc/shorewall/zones </p>
<p> /etc/shorewall/interfaces </p>
<p> /etc/shorewall/hosts </p>
<p> /etc/shorewall/policy </p>
<p> /etc/shorewall/rules</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall_interfaces/">shorewall_interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-rtrules/">shorewall-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-secmarks/">shorewall-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-mangle/">shorewall-mangle</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall-zones</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-zones.html">http://www.shorewall.net/manpages/shorewall-zones.html</a></dl>
<dt> 2.</p>
<dd>shorewall-policy</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-policy.html">http://www.shorewall.net/manpages/shorewall-policy.html</a></dl>
<dt> 3.</p>
<dd>shorewall.conf</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall.conf.html">http://www.shorewall.net/manpages/shorewall.conf.html</a></dl>
