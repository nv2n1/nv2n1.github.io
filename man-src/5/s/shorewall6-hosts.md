---

title: "shorewall6-hosts(5)"
name: "shorewall6-hosts"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall6-hosts/"
---

<p> hosts &#8211; shorewall6 file </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>/etc/shorewall6/hosts</code></dt>
</dl>
<h2>DESCRIPTION</h2>
<dd> <p> This file is used to define zones in terms of subnets and/or individual IP addresses. Most simple setups don&#8217;t need to (should not) place anything in this file. </p>
<p> The order of entries in this file is not significant in determining zone composition. Rather, the order that the zones are declared in m[blue]<code>shorewall6-zones</code>m[]<font SIZE="-2">[1]</font>(5) determines the order in which the records in this file are interpreted. </p>
 </dd>
<dl>
<dd> <p> <br />
 <font SIZE="+1"> <code>Warning</code> </font> <br />
 </p>
<p> The only time that you need this file is when you have more than one zone connected through a single interface. </p>
 </dd></dl>
<dl>
<dd> <p> <br />
 <font SIZE="+1"> <code>Warning</code> </font> <br />
 </p>
<p> If you have an entry for a zone and interface in m[blue]<code>shorewall6-interfaces</code>m[]<font SIZE="-2">[2]</font>(5) then do not include any entries in this file for that same (zone, interface) pair. </p>
 </dd></dl>
<p> The columns in the file are as follows (where the column name is followed by a different name in parentheses, the different name is used in the alternate specification syntax). </p>
<p> <code>ZONE</code> &#8211; <i>zone-name</i> </p>
<dl>
<dd> <p> The name of a zone declared in m[blue]<code>shorewall6-zones</code>m[]<font SIZE="-2">[1]</font>(5). You may not list the firewall zone in this column. </p>
 </dd></dl>
<p> <code>HOST(S)</code> (hosts)- <i>interface</i>:{<i>address-or-range</i>[,<i>address-or-range</i>]...|+<i>ipset</i>|<code>dynamic</code>}[<i>exclusion</i>] </p>
<dl>
<dd> <p> The name of an interface defined in the m[blue]<code>shorewall6-interfaces</code>m[]<font SIZE="-2">[2]</font>(5) file followed by a colon (&quot;:&quot;) and a comma-separated list whose elements are either: </p>
 </dd>
<dl>
<dd> <p> 1. The IPv6 <i>address</i> of a host. </p>
 </dd></dl>
<dl>
<dd> <p> 2. A network in CIDR format. </p>
 </dd></dl>
<dl>
<dd> <p> 3. An IP address range of the form [<i>low.address</i>]-[<i>high.address</i>]. Your kernel and ip6tables must have iprange match support. </p>
 </dd></dl>
<dl>
<dd> <p> 4. The name of an <i>ipset</i>. </p>
 </dd></dl>
<dl>
<dd> <p> 5. The word <code>dynamic</code> which makes the zone dynamic in that you can use the <code>shorewall add</code> and <code>shorewall delete</code> commands to change to composition of the zone. This capability was added in Shorewall 4.4.21. </p>
 </dd></dl>
<p> You may also exclude certain hosts through use of an <i>exclusion</i> (see m[blue]<code>shorewall6-exclusion</code>m[]<font SIZE="-2">[3]</font>(5). </dl>
 </p>
<p> OPTIONS &#8211; [<i>option</i>[<code>,</code><i>option</i>]...] </p>
<dl>
<dd> <p> An optional comma-separated list of options from the following list. The order in which you list the options is not significant but the list must have no embedded white-space. </p>
<p> <code>blacklist</code> </p>
 </dd>
<dl>
<dd> <p> Check packets arriving on this port against the m[blue]<code>shorewall6-blacklist</code>m[]<font SIZE="-2">[4]</font>(5) file. </p>
 </dd></dl>
<p> <code>ipsec</code> </p>
<dl>
<dd> <p> The zone is accessed via a kernel 2.6 ipsec SA. Note that if the zone named in the ZONE column is specified as an IPSEC zone in the m[blue]<code>shorewall6-zones</code>m[]<font SIZE="-2">[1]</font>(5) file then you do NOT need to specify the &#8216;ipsec&#8217; option here. </p>
 </dd></dl>
<p> <code>mss</code>=<i>mss</i> </p>
<dl>
<dd> <p> Added in Shorewall 4.5.2. When present, causes the TCP mss for new connections to/from the hosts given in the HOST(S) column to be clamped at the specified <i>mss</i>. </p>
 </dd></dl>
<p> <code>routeback</code> </p>
<dl>
<dd> <p> shorewall6 should set up the infrastructure to pass packets from this/these address(es) back to themselves. This is necessary if hosts in this group use the services of a transparent proxy that is a member of the group or if DNAT is used to send requests originating from this group to a server in the group. </p>
 </dd></dl>
<p> <code>tcpflags</code> </p>
<dl>
<dd> <p> Packets arriving from these hosts are checked for certain illegal combinations of TCP flags. Packets found to have such a combination of flags are handled according to the setting of TCP_FLAGS_DISPOSITION after having been logged according to the setting of TCP_FLAGS_LOG_LEVEL. </p>
 </dd></dl>
</dl>
<h2>FILES</h2>
<p> /etc/shorewall6/hosts  </p>
<h2>SEE ALSO</h2>
<p> m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[]<font SIZE="-2">[5]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall6/">shorewall6</a>(8), <a href="/docs/linux/man/5-shorewall6-accounting/">shorewall6-accounting</a>(5), <a href="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5), <a href="/docs/linux/man/5-shorewall6-blacklist/">shorewall6-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall6-interfaces/">shorewall6-interfaces</a>(5), <a href="/docs/linux/man/5-shorewall6-maclist/">shorewall6-maclist</a>(5), <a href="/docs/linux/man/5-shorewall6-netmap/">shorewall6-netmap</a>(5),<a href="/docs/linux/man/5-shorewall6-params/">shorewall6-params</a>(5), <a href="/docs/linux/man/5-shorewall6-policy/">shorewall6-policy</a>(5), <a href="/docs/linux/man/5-shorewall6-providers/">shorewall6-providers</a>(5), <a href="/docs/linux/man/5-shorewall6-rtrules/">shorewall6-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall6-routestopped/">shorewall6-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall6-rules/">shorewall6-rules</a>(5), <a href="/docs/linux/man/5-shorewall6.conf/">shorewall6.conf</a>(5), <a href="/docs/linux/man/5-shorewall6-secmarks/">shorewall6-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall6-tcclasses/">shorewall6-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall6-tcdevices/">shorewall6-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall6-mangle/">shorewall6-mangle</a>(5), <a href="/docs/linux/man/5-shorewall6-tos/">shorewall6-tos</a>(5), <a href="/docs/linux/man/5-shorewall6-tunnels/">shorewall6-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)  </p>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> <p> shorewall6-zones </p>
 </dd>
<dl>
<dd> <p> <a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-zones.html">http://www.shorewall.net/manpages6/shorewall6-zones.html</a> </p>
 </dd></dl>
<dt> 2.</dt>
<dd> <p> shorewall6-interfaces </p>
 </dd>
<dl>
<dd> <p> <a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-interfaces.html">http://www.shorewall.net/manpages6/shorewall6-interfaces.html</a> </p>
 </dd></dl>
<dt> 3.</dt>
<dd> <p> shorewall6-exclusion </p>
 </dd>
<dl>
<dd> <p> <a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-exclusion.html">http://www.shorewall.net/manpages6/shorewall6-exclusion.html</a> </p>
 </dd></dl>
<dt> 4.</dt>
<dd> <p> shorewall6-blacklist </p>
 </dd>
<dl>
<dd> <p> <a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-blacklist.html">http://www.shorewall.net/manpages6/shorewall6-blacklist.html</a> </p>
 </dd></dl>
<dt> 5.</dt>
<dd> <p> <a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a> </p>
 </dd>
<dl>
<dd> <p> <a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a> </p>
 </dd></dl>
