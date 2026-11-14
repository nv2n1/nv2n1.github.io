---
title: "shorewall6-interfaces(5)"
name: "shorewall6-interfaces"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall6-interfaces/"
description: "interfaces – shorewall6 interfaces file"
---

<p>interfaces &#8211; shorewall6 interfaces file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall6/interfaces</code></dl>
<h2>Description</h2>
<dd>The interfaces file serves to define the firewall&#8217;s network interfaces to shorewall6. The order of entries in this file is not significant in determining zone composition. Beginning with Shorewall 4.5.3, the interfaces file supports two different formats: FORMAT 1 (default &#8211; deprecated)</p>
<dl>
<dd>There is a ANYCAST column which provides compatibility with older versions of Shorewall..</dl>
<p> FORMAT 2</p>
<dl>
<dd>The BROADCAST column is omitted.</dl>
<p> The format is specified by a line as follows: <code>?FORMAT {1|2}</code> The columns in the file are as follows. <code>ZONE</code> &#8211; <i>zone-name</i></p>
<dl>
<dd>Zone for this interface. Must match the name of a zone declared in /etc/shorewall6/zones. You may not list the firewall zone in this column. If the interface serves multiple zones that will be defined in the m[blue]<code>shorewall6-hosts</code>m[]<font SIZE="-2">[1]</font>(5) file, you should place &quot;-&quot; in this column. If there are multiple interfaces to the same zone, you must list them in separate entries. Example:</p>
<dl>
<dd>
<pre>#ZONE INTERFACE BROADCAST
loc eth1 -
loc eth2 -</pre>
</dl>
<p> Beginning with Shorewall 4.5.17, if you specify a zone for the &#8216;lo&#8217; interface, then that zone must be defined as type <code>local</code> in m[blue]<code>shorewall6-zones</code>m[]<font SIZE="-2">[2]</font>(5).</dl>
<p> <code>INTERFACE</code> &#8211; <i>interface</i><code>[:</code><i>port</i><code>]</code></p>
<dl>
<dd>Logical name of interface. Each interface may be listed only once in this file. You may NOT specify the name of a &quot;virtual&quot; interface (e.g., eth0:0) here; see m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/FAQ.htm#faq18">http://www.shorewall.net/FAQ.htm#faq18</a></code>m[]<font SIZE="-2">[3]</font>. If the <code>physical</code> option is not specified, then the logical name is also the name of the actual interface. You may use wildcards here by specifying a prefix followed by the plus sign (&quot;+&quot;). For example, if you want to make an entry that applies to all PPP interfaces, use &#8216;ppp+&#8217;; that would match ppp0, ppp1, ppp2, &#8230;Please note that the &#8216;+&#8217; means &#8216;<code>one</code> or more additional characters&#8217; so &#8216;ppp&#8217; does not match &#8216;ppp+&#8217;. Care must be exercised when using wildcards where there is another zone that uses a matching specific interface. See m[blue]<code>shorewall6-nesting</code>m[]<font SIZE="-2">[4]</font>(5) for a discussion of this problem. Shorewall6 allows &#8216;+&#8217; as an interface name. There is no need to define the loopback interface (lo) in this file. If a <i>port</i> is given, then the <i>interface</i> must have been defined previously with the <code>bridge</code> option. The OPTIONS column must be empty when a <i>port</i> is given.</dl>
<p> <code>ANYCAST</code> &#8211; <code>&#8211;</code></p>
<dl>
<dd>Enter &#8216;<code>-&#8216;</code> in this column. It is here for compatibility between Shorewall6 and Shorewall and is omitted if FORMAT is 2.</dl>
<p> <code>OPTIONS</code> (Optional) &#8211; [<i>option</i>[<code>,</code><i>option</i>]&#8230;]</p>
<dl>
<dd>A comma-separated list of options from the following list. The order in which you list the options is not significant but the list should have no embedded white-space. <code>accept_ra</code>[={0|1|2}]</p>
<dl>
<dd>Added in Shorewall 4.5.16. Values are: 0</p>
<dl>
<dd>Do not accept Router Advertisements.</dl>
<p> 1</p>
<dl>
<dd>Accept Route Advertisements if forwarding is disabled.</dl>
<p> 2</p>
<dl>
<dd>Overrule forwarding behavior. Accept Route Advertisements even if forwarding is enabled.</dl>
<p> If the option is specified without a value, then the value 1 is assumed.</dl>
<p> <code>blacklist</code></p>
<dl>
<dd>Check packets arriving on this interface against the m[blue]<code>shorewall6-blacklist</code>m[]<font SIZE="-2">[5]</font>(5) file. Beginning with Shorewall 4.4.13:</p>
<dl>
<dd>&bull; If a <i>zone</i> is given in the ZONES column, then the behavior is as if <code>blacklist</code> had been specified in the IN_OPTIONS column of m[blue]<code>shorewall6-zones</code>m[]<font SIZE="-2">[2]</font>(5).</dl>
<dl>
<dd>&bull; Otherwise, the option is ignored with a warning: <code>WARNING: The &#8216;blacklist&#8217; option is ignored on multi-zone interfaces</code></dl>
</dl>
<p> <code>bridge</code></p>
<dl>
<dd>Designates the interface as a bridge. Beginning with Shorewall 4.4.7, setting this option also sets <code>routeback</code>.</dl>
<p> <code>dbl={none|src|dst|src-dst}</code></p>
<dl>
<dd>Added in Shorewall 5.0.10. This option defined whether or not dynamic blacklisting is applied to packets entering the firewall through this interface and whether the source address and/or destination address is to be compared against the ipset-based dynamic blacklist (DYNAMIC_BLACKLIST=ipset&#8230; in m[blue]<code><a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5)</code>m[]<font SIZE="-2">[6]</font>). The default is determine by the setting of DYNAMIC_BLACKLIST: DYNAMIC_BLACKLIST=No</p>
<dl>
<dd>Default is <code>none</code> (e.g., no dynamic blacklist checking).</dl>
<p> DYNAMIC_BLACKLIST=Yes</p>
<dl>
<dd>Default is <code>src</code> (e.g., the source IP address is checked against the ipset).</dl>
<p> DYNAMIC_BLACKLIST=ipset[-only]</p>
<dl>
<dd>Default is <code>src</code>.</dl>
<p> DYNAMIC_BLACKLIST=ipset[-only],src-dst&#8230;</p>
<dl>
<dd>Default is <code>src-dst</code> (e.g., the source IP addresses in checked against the ipset on input and the destination IP address is checked against the ipset on packets originating from the firewall and leaving through this interface).</dl>
</dl>
<p> <code>destonly</code></p>
<dl>
<dd>Added in Shorewall 4.5.17. Causes the compiler to omit rules to handle traffic from this interface.</dl>
<p> <code>dhcp</code></p>
<dl>
<dd>Specify this option when any of the following are true:</p>
<dl>
<dd>1. the interface gets its IP address via DHCP</dl>
<dl>
<dd>2. the interface is used by a DHCP server running on the firewall</dl>
<dl>
<dd>3. the interface has a static IP but is on a LAN segment with lots of DHCP clients.</dl>
<dl>
<dd>4. the interface is a m[blue]<code>simple bridge</code>m[]<font SIZE="-2">[7]</font> with a DHCP server on one port and DHCP clients on another port.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 If you use m[blue]<code>Shorewall-perl for firewall/bridging</code>m[]<font SIZE="-2">[8]</font>, then you need to include DHCP-specific rules in m[blue]<code>shorewall-rules</code>m[]<font SIZE="-2">[9]</font>(8). DHCP uses UDP ports 546 and 547.  This option allows DHCP datagrams to enter and leave the interface.</dl>
<p> <code>forward</code>[={0|1}]</p>
<dl>
<dd>Sets the /proc/sys/net/ipv6/conf/interface/forwarding option to the specified value. If no value is supplied, then 1 is assumed.</dl>
<p> <code>ignore[=1]</code></p>
<dl>
<dd>When specified, causes the generated script to ignore up/down events from Shorewall-init for this device. Additionally, the option exempts the interface from hairpin filtering. When &#8216;=1&#8217; is omitted, the ZONE column must contain &#8216;-&#8216; and <code>ignore</code> must be the only OPTION. Beginning with Shorewall 4.5.5, may be specified as &#8216;<code>ignore=1</code>&#8216; which only causes the generated script to ignore up/down events from Shorewall-init; hairpin filtering is still applied. In this case, the above restrictions on the ZONE and OPTIONS columns are lifted.</dl>
<p> <code>loopback</code></p>
<dl>
<dd>Added in Shorewall 4.6.6. Designates the interface as the loopback interface. This option is assumed if the interface&#8217;s physical name is &#8216;lo&#8217;. Only one interface man have the <code>loopback</code> option specified.</dl>
<p> <code>mss</code>=<i>number</i></p>
<dl>
<dd>Causes forwarded TCP SYN packets entering or leaving on this interface to have their MSS field set to the specified <i>number</i>.</dl>
<p> <code>nets=(</code><i>net</i><code>[,&#8230;])</code></p>
<dl>
<dd>Limit the zone named in the ZONE column to only the listed networks. If you specify this option, be sure to include the link-local network (ff80::/10).</dl>
<p> <code>nets=dynamic</code></p>
<dl>
<dd>Added in Shorewall 4.4.21. Defines the zone as dynamic. Requires ipset match support in your iptables and kernel. See m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/Dynamic.html">http://www.shorewall.net/Dynamic.html</a></code>m[]<font SIZE="-2">[10]</font> for further information.</dl>
<p> <code>nodbl</code></p>
<dl>
<dd>Added in Shorewall 5.0.8. When specified, dynamic blacklisting is disabled on the interface. Beginning with Shorewall 5.0.10, <code>nodbl</code> is equivalent to <code>dbl=none</code>.</dl>
<p> <code>optional</code></p>
<dl>
<dd>When <code>optional</code> is specified for an interface, shorewall6 will be silent when:</p>
<dl>
<dd>&bull; a /proc/sys/net/ipv6/conf/ entry for the interface cannot be modified.</dl>
<dl>
<dd>&bull; The first global IPv6 address of the interface cannot be obtained.</dl>
<p> This option may not be specified together with <code>required</code>.</dl>
<p> <code>physical</code>=<i>name</i></p>
<dl>
<dd>Added in Shorewall 4.4.4. When specified, the interface or port name in the INTERFACE column is a logical name that refers to the name given in this option. It is useful when you want to specify the same wildcard port name on two or more bridges. See m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/bridge-Shorewall-perl.html#Multiple">http://www.shorewall.net/bridge-Shorewall-perl.html#Multiple</a></code>m[]<font SIZE="-2">[11]</font>. If the <i>interface</i> name is a wildcard name (ends with &#8216;+&#8217;), then the physical <i>name</i> must also end in &#8216;+&#8217;. If <code>physical</code> is not specified, then it&#8217;s value defaults to the <i>interface</i> name.</dl>
<p> <code>required</code></p>
<dl>
<dd>Added in Shorewall 4.4.10. When specified, the firewall will fail to start if the interface named in the INTERFACE column is not usable. May not be specified together with <code>optional</code>.</dl>
<p> <code>routeback[={0|1}]</code></p>
<dl>
<dd>If specified, indicates that shorewall6 should include rules that allow traffic arriving on this interface to be routed back out that same interface. This option is also required when you have used a wildcard in the INTERFACE column if you want to allow traffic between the interfaces that match the wildcard. If you specify this option, then you should also specify <code>rpfilter</code> (see below) if you are running Shorewall 4.5.7 or later; otherwise, you should specify <code>sfilter</code> (see below). Beginning with Shorewall 4.5.18, you may specify this option to explicitly reset (e.g., <code>routeback=0</code>). This can be used to override Shorewall&#8217;s default setting for bridge devices which is <code>routeback=1</code>.</dl>
<p> <code>rpfilter</code></p>
<dl>
<dd>Added in Shorewall 4.5.7. This is an anti-spoofing measure that requires the &#8216;RPFilter Match&#8217; capability in your iptables and kernel. It provides a more efficient alternative to the <code>sfilter</code> option below.</dl>
<p> <code>sourceroute[={0|1}]</code></p>
<dl>
<dd>If this option is not specified for an interface, then source-routed packets will not be accepted from that interface unless explicitly enabled via sysconf. Only set this option to 1 (enable source routing) if you know what you are doing. This might represent a security risk and is not usually needed. Only those interfaces with the <code>sourceroute</code> option will have their setting changed; the value assigned to the setting will be the value specified (if any) or 1 if no value is given.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 This option does not work with a wild-card <i>interface</i> name (e.g., eth0.+) in the INTERFACE column.  <code>sfilter=(</code><i>net</i><code>[,&#8230;])</code></p>
<dl>
<dd>Added in Shorewall 4.4.20. At this writing (spring 2011), Linux does not support reverse path filtering (RFC3704) for IPv6. In its absence, <code>sfilter</code> may be used as an anti-spoofing measure. This option should be used on bridges or other interfaces with the <code>routeback</code> option. On these interfaces, <code>sfilter</code> should list those local networks that are connected to the firewall through other interfaces.</dl>
<p> <code>tcpflags[={0|1}]</code></p>
<dl>
<dd>Packets arriving on this interface are checked for certain illegal combinations of TCP flags. Packets found to have such a combination of flags are handled according to the setting of TCP_FLAGS_DISPOSITION after having been logged according to the setting of TCP_FLAGS_LOG_LEVEL. Beginning with Shorewall 4.6.0, tcpflags=1 is the default. To disable this option, specify tcpflags=0.</dl>
<p> <code>proxyndp</code>[={0|1}]</p>
<dl>
<dd>Sets /proc/sys/net/ipv6/conf/<i>interface</i>/proxy_ndp. <code>Note</code>: This option does not work with a wild-card <i>interface</i> name (e.g., eth0.+) in the INTERFACE column. Only those interfaces with the <code>proxyndp</code> option will have their setting changed; the value assigned to the setting will be the value specified (if any) or 1 if no value is given.</dl>
<p> <code>unmanaged</code></p>
<dl>
<dd>Added in Shorewall 4.5.18. Causes all traffic between the firewall and hosts on the interface to be accepted. When this option is given:</p>
<dl>
<dd>&bull; The ZONE column must contain &#8216;-&#8216;.</dl>
<dl>
<dd>&bull; Only the following other options are allowed with <code>unmanaged</code>:</p>
<dl>
<dd><code>accept_ra</code></dl>
<dl>
<dd><code>forward</code></dl>
<dl>
<dd><code>ignore</code></dl>
<dl>
<dd><code>optional</code></dl>
<dl>
<dd><code>physical</code></dl>
<dl>
<dd><code>sourceroute</code></dl>
<dl>
<dd><code>proxyndp</code></dl>
</dl>
</dl>
<p> <code>wait</code>=<i>seconds</i></p>
<dl>
<dd>Added in Shorewall 4.4.10. Causes the generated script to wait up to <i>seconds</i> seconds for the interface to become usable before applying the <code>required</code> or <code>optional</code> options.</dl>
</dl>
<h2>Example</h2>
<p>Example 1:</p>
<dl>
<dd>Suppose you have eth0 connected to a DSL modem and eth1 connected to your local network You have a DMZ using eth2. </p>
<p> Your entries for this setup would look like: </p>
<dl>
<dd>
<pre>FORMAT 2
#ZONE INTERFACE OPTIONS
net eth0 -
loc eth1 -
dmz eth2 -</pre>
</dl>
</dl>
<p> Example 4 (Shorewall 4.4.9 and later):</p>
<dl>
<dd>You have a bridge with no IP address and you want to allow traffic through the bridge. </p>
<dl>
<dd>
<pre>FORMAT 2
#ZONE INTERFACE OPTIONS
- br0 bridge</pre>
</dl>
</dl>
<h2>Files</h2>
<p>/etc/shorewall6/interfaces</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[]<font SIZE="-2">[12]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall6/">shorewall6</a>(8), <a href="/docs/linux/man/5-shorewall6-accounting/">shorewall6-accounting</a>(5), <a href="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5), <a href="/docs/linux/man/5-shorewall6-blacklist/">shorewall6-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall6-hosts/">shorewall6-hosts</a>(5), <a href="/docs/linux/man/5-shorewall6-maclist/">shorewall6-maclist</a>(5), <a href="/docs/linux/man/5-shorewall6-netmap/">shorewall6-netmap</a>(5),<a href="/docs/linux/man/5-shorewall6-params/">shorewall6-params</a>(5), <a href="/docs/linux/man/5-shorewall6-policy/">shorewall6-policy</a>(5), <a href="/docs/linux/man/5-shorewall6-providers/">shorewall6-providers</a>(5), <a href="/docs/linux/man/5-shorewall6-rtrules/">shorewall6-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall6-routestopped/">shorewall6-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall6-rules/">shorewall6-rules</a>(5), <a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5), <a href="/docs/linux/man/5-shorewall6-secmarks/">shorewall6-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall6-tcclasses/">shorewall6-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall6-tcdevices/">shorewall6-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall6-mangle/">shorewall6-mangle</a>(5), <a href="/docs/linux/man/5-shorewall6-tos/">shorewall6-tos</a>(5), <a href="/docs/linux/man/5-shorewall6-tunnels/">shorewall6-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall6-zones/">shorewall6-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall6-hosts</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-hosts.html">http://www.shorewall.net/manpages6/shorewall6-hosts.html</a></dl>
<dt> 2.</p>
<dd>shorewall6-zones</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-zones.html">http://www.shorewall.net/manpages6/shorewall6-zones.html</a></dl>
<dt> 3.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/FAQ.htm#faq18">http://www.shorewall.net/FAQ.htm#faq18</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/FAQ.htm#faq18">http://www.shorewall.net/FAQ.htm#faq18</a></dl>
<dt> 4.</p>
<dd>shorewall6-nesting</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-nesting.html">http://www.shorewall.net/manpages6/shorewall6-nesting.html</a></dl>
<dt> 5.</p>
<dd>shorewall6-blacklist</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-blacklist.html">http://www.shorewall.net/manpages6/shorewall6-blacklist.html</a></dl>
<dt> 6.</p>
<dd><a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5)</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netmanpages6/shorewall6.conf.html">http://www.shorewall.netmanpages6/shorewall6.conf.html</a></dl>
<dt> 7.</p>
<dd>simple bridge</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/SimpleBridge.html">http://www.shorewall.net/SimpleBridge.html</a></dl>
<dt> 8.</p>
<dd>Shorewall-perl for firewall/bridging</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/bridge-Shorewall-perl.html">http://www.shorewall.net/bridge-Shorewall-perl.html</a></dl>
<dt> 9.</p>
<dd>shorewall-rules</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-rules.html">http://www.shorewall.net/manpages/shorewall-rules.html</a></dl>
<dt>10.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/Dynamic.html">http://www.shorewall.net/Dynamic.html</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/Dynamic.html">http://www.shorewall.net/Dynamic.html</a></dl>
<dt>11.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/bridge-Shorewall-perl.html#Multiple">http://www.shorewall.net/bridge-Shorewall-perl.html#Multiple</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/bridge-Shorewall-perl.html#Multiple">http://www.shorewall.net/bridge-Shorewall-perl.html#Multiple</a></dl>
<dt>12.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dl>
