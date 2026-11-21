---
title: "shorewall6-nesting(5)"
name: "shorewall6-nesting"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall6-nesting/"
---


 </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><i>child-zone</i>[:<i>parent-zone</i>[,<i>parent-zone</i>]...] </dt>
</dl>
<h2>DESCRIPTION</h2>
<dd> <p> In m[blue]<code>shorewall6-zones</code>m[]<font SIZE="-2">[1]</font>(5), a zone may be declared to be a sub-zone of one or more other zones using the above syntax. The <i>child-zone</i> may be neither the firewall zone nor a vserver zone. The firewall zone may not appear as a parent zone, although all vserver zones are handled as sub-zones of the firewall zone. </p>
<p> Where zones are nested, the CONTINUE policy in m[blue]<code>shorewall6-policy</code>m[]<font SIZE="-2">[2]</font>(5) allows hosts that are within multiple zones to be managed under the rules of all of these zones.  </p>
<h2>EXAMPLE</h2>
<p> /etc/shorewall6/zones: </p>
 </dd>
<dl>
<dd> <pre><code>        #ZONE TYPE OPTION
        fw firewall
        net ipv6
        sam:net ipv6
        loc ipv6
</code></pre>
 </dd></dl>
<p> /etc/shorewall6/interfaces: </p>
<dl>
<dd> <pre><code>        #ZONE INTERFACE BROADCAST OPTIONS
        - eth0 detect blacklist
        loc eth1 detect
</code></pre>
 </dd></dl>
<p> /etc/shorewall6/hosts: </p>
<dl>
<dd> <pre><code>        #ZONE HOST(S) OPTIONS
        net eth0:[::\]
        sam eth0:[2001:19f0:feee::dead:beef:cafe]
</code></pre>
 </dd></dl>
<p> /etc/shorewall6/policy: </p>
<dl>
<dd> <pre><code>        #SOURCE DEST POLICY LOG LEVEL
        loc net ACCEPT
        sam all CONTINUE
        net all DROP info
        all all REJECT info
</code></pre>
 </dd></dl>
<p> The second entry above says that when Sam is the client, connection requests should first be processed under rules where the source zone is sam and if there is no match then the connection request should be treated under rules where the source zone is net. It is important that this policy be listed BEFORE the next policy (net to all). You can have this policy generated for you automatically by using the IMPLICIT_CONTINUE option in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[3]</font>(5). </p>
<p> Partial /etc/shorewall6/rules: </p>
<dl>
<dd> <pre><code>        #ACTION SOURCE DEST PROTO DPORT
        ...
        ACCEPT sam loc:2001:19f0:feee::3 tcp ssh
        ACCEPT net loc:2001:19f0:feee::5 tcp www
        ...
</code></pre>
 </dd></dl>
<p> Given these two rules, Sam can connect with ssh to 2001:19f0:feee::3. Like all hosts in the net zone, Sam can connect to TCP port 80 on 2001:19f0:feee::5. The order of the rules is not significant.  </p>
<h2>FILES</h2>
<p> /etc/shorewall6/zones </p>
<p> /etc/shorewall6/interfaces </p>
<p> /etc/shorewall6/hosts </p>
<p> /etc/shorewall6/policy </p>
<p> /etc/shorewall6/rules  </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-shorewall6/">shorewall6</a>(8), <a href="/docs/linux/man/5-shorewall6-accounting/">shorewall6-accounting</a>(5), <a href="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5), <a href="/docs/linux/man/5-shorewall6-blacklist/">shorewall6-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall6-hosts/">shorewall6-hosts</a>(5), <a href="/docs/linux/man/5-shorewall6-interfaces/">shorewall6-interfaces</a>(5), <a href="/docs/linux/man/5-shorewall6-maclist/">shorewall6-maclist</a>(5), <a href="/docs/linux/man/5-shorewall6-netmap/">shorewall6-netmap</a>(5),<a href="/docs/linux/man/5-shorewall6-params/">shorewall6-params</a>(5), <a href="/docs/linux/man/5-shorewall6-policy/">shorewall6-policy</a>(5), <a href="/docs/linux/man/5-shorewall6-providers/">shorewall6-providers</a>(5), <a href="/docs/linux/man/5-shorewall6-rtrules/">shorewall6-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall6-routestopped/">shorewall6-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall6-rules/">shorewall6-rules</a>(5), <a href="/docs/linux/man/5-shorewall6.conf/">shorewall6.conf</a>(5), <a href="/docs/linux/man/5-shorewall6-secmarks/">shorewall6-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall6-tcclasses/">shorewall6-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall6-tcdevices/">shorewall6-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall6-mangle/">shorewall6-mangle</a>(5), <a href="/docs/linux/man/5-shorewall6-tos/">shorewall6-tos</a>(5), <a href="/docs/linux/man/5-shorewall6-tunnels/">shorewall6-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall6-zones/">shorewall6-zones</a>(5)  </p>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> <p> shorewall6-zones </p>
 </dd>
<dl>
<dd> <p> <a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-zones.html">http://www.shorewall.net/manpages6/shorewall6-zones.html</a> </p>
 </dd></dl>
<dt> 2.</dt>
<dd> <p> shorewall6-policy </p>
 </dd>
<dl>
<dd> <p> <a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-policy.html">http://www.shorewall.net/manpages6/shorewall6-policy.html</a> </p>
 </dd></dl>
<dt> 3.</dt>
<dd> <p> shorewall6.conf </p>
 </dd>
<dl>
<dd> <p> <a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6.conf.html">http://www.shorewall.net/manpages6/shorewall6.conf.html</a> </p>
 </dd></dl>
