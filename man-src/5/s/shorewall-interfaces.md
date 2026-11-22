---
title: "shorewall-interfaces(5)"
name: "shorewall-interfaces"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-interfaces/"
description: "interfaces – Shorewall interfaces file"
---

<p>interfaces &#8211; Shorewall interfaces file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/interfaces</code></dt></dl>
<h2>Description</h2>
<dd>The interfaces file serves to define the firewall&#8217;s network interfaces to Shorewall. The order of entries in this file is not significant in determining zone composition. Beginning with Shorewall 4.5.3, the interfaces file supports two different formats: FORMAT 1 (default &#8211; deprecated)</dd>
<dl>
<dd>There is a BROADCAST column which can be used to specify the broadcast address associated with the interface.</dd></dl>
<p> FORMAT 2</p>
<dl>
<dd>The BROADCAST column is omitted.</dd></dl>
<p> The format is specified by a line as follows: <code>?FORMAT {1|2}</code> The columns in the file are as follows. <code>ZONE</code> &#8211; <i>zone-name</i></p>
<dl>
<dd>Zone for this interface. Must match the name of a zone declared in /etc/shorewall/zones. You may not list the firewall zone in this column. If the interface serves multiple zones that will be defined in the m[blue]<code>shorewall-hosts</code>m[][1](5) file, you should place &quot;-&quot; in this column. If there are multiple interfaces to the same zone, you must list them in separate entries. Example:</dd>
<dl>
<dd>
<pre>#ZONE INTERFACE BROADCAST
loc eth1 -
loc eth2 -</pre>
</dd></dl>
</dl>
<p> <code>INTERFACE</code> &#8211; <i>interface</i><code>[:</code><i>port</i><code>]</code></p>
<dl>
<dd>Logical name of interface. Each interface may be listed only once in this file. You may NOT specify the name of a &quot;virtual&quot; interface (e.g., eth0:0) here; see m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/FAQ.htm#faq18">http://www.shorewall.net/FAQ.htm#faq18</a></code>m[][2]. If the <code>physical</code> option is not specified, then the logical name is also the name of the actual interface. You may use wildcards here by specifying a prefix followed by the plus sign (&quot;+&quot;). For example, if you want to make an entry that applies to all PPP interfaces, use &#8216;ppp+&#8217;; that would match ppp0, ppp1, ppp2, &#8230; Please note that the &#8216;+&#8217; means &#8216;<code>one</code> or more additional characters&#8217; so &#8216;ppp&#8217; does not match &#8216;ppp+&#8217;. When using Shorewall versions before 4.1.4, care must be exercised when using wildcards where there is another zone that uses a matching specific interface. See m[blue]<code>shorewall-nesting</code>m[][3](5) for a discussion of this problem. Shorewall allows &#8216;+&#8217; as an interface name. There is no need to define the loopback interface (lo) in this file. If a <i>port</i> is given, then the <i>interface</i> must have been defined previously with the <code>bridge</code> option. The OPTIONS column may not contain the following options when a <i>port</i> is given.</dd>
<dl>
<dd>arp_filter</dd></dl>
<dl>
<dd>arp_ignore</dd></dl>
<dl>
<dd>bridge</dd></dl>
<dl>
<dd>log_martians</dd></dl>
<dl>
<dd>mss</dd></dl>
<dl>
<dd>optional</dd></dl>
<dl>
<dd>proxyarp</dd></dl>
<dl>
<dd>required</dd></dl>
<dl>
<dd>routefilter</dd></dl>
<dl>
<dd>sourceroute</dd></dl>
<dl>
<dd>upnp</dd></dl>
<dl>
<dd>wait</dd></dl>
<p> Beginning with Shorewall 4.5.17, if you specify a zone for the &#8216;lo&#8217; interface, then that zone must be defined as type <code>local</code> in m[blue]<code>shorewall6-zones</code>m[][4](5).</dl>
<p> <code>BROADCAST</code> (Optional) &#8211; {<code>&#8211;</code>|<code>detect</code>|<i>address</i>[,<i>address</i>]&#8230;}</p>
<dl>
<dd>Only available if FORMAT 1. If you use the special value <code>detect</code>, Shorewall will detect the broadcast address(es) for you if your iptables and kernel include Address Type Match support. If your iptables and/or kernel lack Address Type Match support then you may list the broadcast address(es) for the network(s) to which the interface belongs. For P-T-P interfaces, this column is left blank. If the interface has multiple addresses on multiple subnets then list the broadcast addresses as a comma-separated list. If you don&#8217;t want to give a value for this column but you want to enter a value in the OPTIONS column, enter <code>&#8211;</code> in this column.</dd></dl>
<p> <code>OPTIONS</code> (Optional) &#8211; [<i>option</i>[<code>,</code><i>option</i>]&#8230;]</p>
<dl>
<dd>A comma-separated list of options from the following list. The order in which you list the options is not significant but the list should have no embedded white-space. <code>arp_filter[={0|1}]</code></dd>
<dl>
<dd>If specified, this interface will only respond to ARP who-has requests for IP addresses configured on the interface. If not specified, the interface can respond to ARP who-has requests for IP addresses on any of the firewall&#8217;s interface. The interface must be up when Shorewall is started. Only those interfaces with the <code>arp_filter</code> option will have their setting changed; the value assigned to the setting will be the value specified (if any) or 1 if no value is given.</dd>
<dl>
<dd> <code>Note</code> <br/>
 This option does not work with a wild-card <i>interface</i> name (e.g., eth0.+) in the INTERFACE column.  <code>arp_ignore</code>[=<i>number</i>]</dd>
<dl>
<dd>If specified, this interface will respond to arp requests based on the value of <i>number</i> (defaults to 1). 1 &#8211; reply only if the target IP address is local address configured on the incoming interface 2 &#8211; reply only if the target IP address is local address configured on the incoming interface and the sender&#8217;s IP address is part from same subnet on this interface&#8217;s address 3 &#8211; do not reply for local addresses configured with scope host, only resolutions for global and link 4-7 &#8211; reserved 8 &#8211; do not reply for all local addresses</dd>
<dl>
<dd> <code>Note</code> <br/>
 This option does not work with a wild-card <i>interface</i> name (e.g., eth0.+) in the INTERFACE column. </dd>
<dl>
<dd> <code>Warning</code> <br/>
 Do not specify <code>arp_ignore</code> for any interface involved in m[blue]<code>Proxy ARP</code>m[][5].  <code>blacklist</code></dd>
<dl>
<dd>Checks packets arriving on this interface against the m[blue]<code>shorewall-blacklist</code>m[][6](5) file. Beginning with Shorewall 4.4.13:</dd>
<dl>
<dd>&bull; If a <i>zone</i> is given in the ZONES column, then the behavior is as if <code>blacklist</code> had been specified in the IN_OPTIONS column of m[blue]<code>shorewall-zones</code>m[][7](5).</dd></dl>
<dl>
<dd>&bull; Otherwise, the option is ignored with a warning: <code>WARNING: The &#8216;blacklist&#8217; option is ignored on multi-zone interfaces</code></dd></dl>
</dl>
<p> <code>bridge</code></p>
<dl>
<dd>Designates the interface as a bridge. Beginning with Shorewall 4.4.7, setting this option also sets <code>routeback</code>.</dd></dl>
<p> <code>dbl={none|src|dst|src-dst}</code></p>
<dl>
<dd>Added in Shorewall 5.0.10. This option defined whether or not dynamic blacklisting is applied to packets entering the firewall through this interface and whether the source address and/or destination address is to be compared against the ipset-based dynamic blacklist (DYNAMIC_BLACKLIST=ipset&#8230; in m[blue]<code><a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5)</code>m[][8]). The default is determine by the setting of DYNAMIC_BLACKLIST: DYNAMIC_BLACKLIST=No</dd>
<dl>
<dd>Default is <code>none</code> (e.g., no dynamic blacklist checking).</dd></dl>
<p> DYNAMIC_BLACKLIST=Yes</p>
<dl>
<dd>Default is <code>src</code> (e.g., the source IP address is checked).</dd></dl>
<p> DYNAMIC_BLACKLIST=ipset[-only]</p>
<dl>
<dd>Default is <code>src</code>.</dd></dl>
<p> DYNAMIC_BLACKLIST=ipset[-only],src-dst&#8230;</p>
<dl>
<dd>Default is <code>src-dst</code> (e.g., the source IP addresses in checked against the ipset on input and the destination IP address is checked against the ipset on packets originating from the firewall and leaving through this interface).</dd></dl>
<p> The normal setting for this option will be <code>dst</code> or <code>none</code> for internal interfaces and <code>src</code> or <code>src-dst</code> for Internet-facing interfaces.</dl>
<p> <code>destonly</code></p>
<dl>
<dd>Added in Shorewall 4.5.17. Causes the compiler to omit rules to handle traffic from this interface.</dd></dl>
<p> <code>dhcp</code></p>
<dl>
<dd>Specify this option when any of the following are true:</dd>
<dl>
<dd>1. the interface gets its IP address via DHCP</dd></dl>
<dl>
<dd>2. the interface is used by a DHCP server running on the firewall</dd></dl>
<dl>
<dd>3. the interface has a static IP but is on a LAN segment with lots of DHCP clients.</dd></dl>
<dl>
<dd>4. the interface is a m[blue]<code>simple bridge</code>m[][9] with a DHCP server on one port and DHCP clients on another port.</dd>
<dl>
<dd> <code>Note</code> <br/>
 If you use m[blue]<code>Shorewall-perl for firewall/bridging</code>m[][10], then you need to include DHCP-specific rules in m[blue]<code>shorewall-rules</code>m[][11](5). DHCP uses UDP ports 67 and 68.  This option allows DHCP datagrams to enter and leave the interface.</dd></dl>
<p> <code>ignore[=1]</code></p>
<dl>
<dd>When specified, causes the generated script to ignore up/down events from Shorewall-init for this device. Additionally, the option exempts the interface from hairpin filtering. When &#8216;=1&#8217; is omitted, the ZONE column must contain &#8216;-&#8216; and <code>ignore</code> must be the only OPTION. Beginning with Shorewall 4.5.5, may be specified as &#8216;<code>ignore=1</code>&#8216; which only causes the generated script to ignore up/down events from Shorewall-init; hairpin filtering is still applied. In this case, the above restrictions on the ZONE and OPTIONS columns are lifted.</dd></dl>
<p> <code>loopback</code></p>
<dl>
<dd>Added in Shorewall 4.6.6. Designates the interface as the loopback interface. This option is assumed if the interface&#8217;s physical name is &#8216;lo&#8217;. Only one interface man have the <code>loopback</code> option specified.</dd></dl>
<p> <code>logmartians[={0|1}]</code></p>
<dl>
<dd>Turn on kernel martian logging (logging of packets with impossible source addresses. It is strongly suggested that if you set <code>routefilter</code> on an interface that you also set <code>logmartians</code>. Even if you do not specify the <code>routefilter</code> option, it is a good idea to specify <code>logmartians</code> because your distribution may have enabled route filtering without you knowing it. Only those interfaces with the <code>logmartians</code> option will have their setting changed; the value assigned to the setting will be the value specified (if any) or 1 if no value is given. To find out if route filtering is set on a given <i>interface</i>, check the contents of /proc/sys/net/ipv4/conf/<i>interface</i>/rp_filter &#8211; a non-zero value indicates that route filtering is enabled. Example:</dd>
<dl>
<dd>
<pre> teastep [at] lists:~$ <code>cat /proc/sys/net/ipv4/conf/eth0/rp_filter </code>
 1
 teastep [at] lists:~$ </pre>
</dd></dl>
<dl>
<dd> <code>Note</code> <br/>
 This option does not work with a wild-card <i>interface</i> name (e.g., eth0.+) in the INTERFACE column.</dd></dl>
<p> This option may also be enabled globally in the m[blue]<code>shorewall.conf</code>m[][12](5) file.</dl>
<p> <code>maclist</code></p>
<dl>
<dd>Connection requests from this interface are compared against the contents of m[blue]<code>shorewall-maclist</code>m[][13](5). If this option is specified, the interface must be an Ethernet NIC and must be up before Shorewall is started.</dd></dl>
<p> <code>mss</code><code>=</code><i>number</i></p>
<dl>
<dd>Added in Shorewall 4.0.3. Causes forwarded TCP SYN packets entering or leaving on this interface to have their MSS field set to the specified <i>number</i>.</dd></dl>
<p> <code>nets=(</code><i>net</i><code>[,&#8230;])</code></p>
<dl>
<dd>Limit the zone named in the ZONE column to only the listed networks. The parentheses may be omitted if only a single <i>net</i> is given (e.g., nets=192.168.1.0/24). Limited broadcast to the zone is supported. Beginning with Shorewall 4.4.1, multicast traffic to the zone is also supported.</dd></dl>
<p> <code>nets=dynamic</code></p>
<dl>
<dd>Defines the zone as dynamic. Requires ipset match support in your iptables and kernel. See m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/Dynamic.html">http://www.shorewall.net/Dynamic.html</a></code>m[][14] for further information.</dd></dl>
<p> <code>nodbl</code></p>
<dl>
<dd>Added in Shorewall 5.0.8. When specified, dynamic blacklisting is disabled on the interface. Beginning with Shorewall 5.0.10, <code>nodbl</code> is equivalent to <code>dbl=none</code>.</dd></dl>
<p> <code>nosmurfs</code></p>
<dl>
<dd>Filter packets for smurfs (packets with a broadcast address as the source). Smurfs will be optionally logged based on the setting of SMURF_LOG_LEVEL in m[blue]<code>shorewall.conf</code>m[][12](5). After logging, the packets are dropped.</dd></dl>
<p> <code>optional</code></p>
<dl>
<dd>When <code>optional</code> is specified for an interface, Shorewall will be silent when:</dd>
<dl>
<dd>&bull; a /proc/sys/net/ipv4/conf/ entry for the interface cannot be modified (including for proxy ARP).</dd></dl>
<dl>
<dd>&bull; The first address of the interface cannot be obtained.</dd></dl>
<p> May not be specified with <code>required</code>.</dl>
<p> <code>physical</code>=<i>name</i></p>
<dl>
<dd>Added in Shorewall 4.4.4. When specified, the interface or port name in the INTERFACE column is a logical name that refers to the name given in this option. It is useful when you want to specify the same wildcard port name on two or more bridges. See m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/bridge-Shorewall-perl.html#Multiple">http://www.shorewall.net/bridge-Shorewall-perl.html#Multiple</a></code>m[][15]. If the <i>interface</i> name is a wildcard name (ends with &#8216;+&#8217;), then the physical <i>name</i> must also end in &#8216;+&#8217;. If <code>physical</code> is not specified, then it&#8217;s value defaults to the <i>interface</i> name.</dd></dl>
<p> <code>proxyarp[={0|1}]</code></p>
<dl>
<dd>Sets /proc/sys/net/ipv4/conf/<i>interface</i>/proxy_arp. Do NOT use this option if you are employing Proxy ARP through entries in m[blue]<code>shorewall-proxyarp</code>m[][16](5). This option is intended solely for use with Proxy ARP sub-networking as described at: m[blue]<code><a rel="nofollow" href="http://tldp.org/HOWTO/Proxy-ARP-Subnet/index.html.">http://tldp.org/HOWTO/Proxy-ARP-Subnet/index.html.</a></code>m[][17] <code>Note</code>: This option does not work with a wild-card <i>interface</i> name (e.g., eth0.+) in the INTERFACE column. Only those interfaces with the <code>proxyarp</code> option will have their setting changed; the value assigned to the setting will be the value specified (if any) or 1 if no value is given.</dd></dl>
<p> <code>required</code></p>
<dl>
<dd>Added in Shorewall 4.4.10. If this option is set, the firewall will fail to start if the interface is not usable. May not be specified together with <code>optional</code>.</dd></dl>
<p> <code>routeback[={0|1}]</code></p>
<dl>
<dd>If specified, indicates that Shorewall should include rules that allow traffic arriving on this interface to be routed back out that same interface. This option is also required when you have used a wildcard in the INTERFACE column if you want to allow traffic between the interfaces that match the wildcard. Beginning with Shorewall 4.4.20, if you specify this option, then you should also specify either <code>sfilter</code> (see below) or <code>routefilter</code> on all interfaces (see below). Beginning with Shorewall 4.5.18, you may specify this option to explicitly reset (e.g., <code>routeback=0</code>). This can be used to override Shorewall&#8217;s default setting for bridge devices which is <code>routeback=1</code>.</dd></dl>
<p> <code>routefilter[={0|1|2}]</code></p>
<dl>
<dd>Turn on kernel route filtering for this interface (anti-spoofing measure). Only those interfaces with the <code>routefilter</code> option will have their setting changes; the value assigned to the setting will be the value specified (if any) or 1 if no value is given. The value 2 is only available with Shorewall 4.4.5.1 and later when the kernel version is 2.6.31 or later. It specifies a loose form of reverse path filtering.</dd>
<dl>
<dd> <code>Note</code> <br/>
 This option does not work with a wild-card <i>interface</i> name (e.g., eth0.+) in the INTERFACE column.</dd></dl>
<p> This option can also be enabled globally via the ROUTE_FILTER option in the m[blue]<code>shorewall.conf</code>m[][12](5) file.</p>
<dl>
<dd> <code>Important</code> <br/>
 If ROUTE_FILTER=Yes in m[blue]<code>shorewall.conf</code>m[][12](5), or if your distribution sets net.ipv4.conf.all.rp_filter=1 in /etc/sysctl.conf, then setting <code>routefilter</code>=0 in an <i>interface</i> entry will not disable route filtering on that <i>interface</i>! The effective setting for an <i>interface</i> is the maximum of the contents of /proc/sys/net/ipv4/conf/all/rp_filter and the routefilter setting specified in this file (/proc/sys/net/ipv4/conf/<i>interface</i>/rp_filter). </dd>
<dl>
<dd> <code>Note</code> <br/>
 There are certain cases where <code>routefilter</code> cannot be used on an interface:</dd>
<dl>
<dd>&bull; If USE_DEFAULT_RT=Yes in m[blue]<code>shorewall.conf</code>m[][12](5) and the interface is listed in m[blue]<code>shorewall-providers</code>m[][18](5).</dd></dl>
<dl>
<dd>&bull; If there is an entry for the interface in m[blue]<code>shorewall-providers</code>m[][18](5) that doesn&#8217;t specify the <code>balance</code> option.</dd></dl>
<dl>
<dd>&bull; If IPSEC is used to allow a road-warrior to have a local address, then any interface through which the road-warrior might connect cannot specify <code>routefilter</code>.</dd></dl>
<p>  <code>rpfilter</code></p>
<dl>
<dd>Added in Shorewall 4.5.7. This is an anti-spoofing measure that requires the &#8216;RPFilter Match&#8217; capability in your iptables and kernel. It provides a more efficient alternative to the <code>sfilter</code> option below. It performs a function similar to <code>routefilter</code> (see above) but works with Multi-ISP configurations that do now use balanced routes.</dd></dl>
<p> <code>sfilter=(</code><i>net</i><code>[,&#8230;])</code></p>
<dl>
<dd>Added in Shorewall 4.4.20. This option provides an anti-spoofing alternative to <code>routefilter</code> on interfaces where that option cannot be used, but where the <code>routeback</code> option is required (on a bridge, for example). On these interfaces, <code>sfilter</code> should list those local networks that are connected to the firewall through other interfaces.</dd></dl>
<p> <code>sourceroute[={0|1}]</code></p>
<dl>
<dd>If this option is not specified for an interface, then source-routed packets will not be accepted from that interface unless it has been explicitly enabled via sysconf. Only set this option to 1 (enable source routing) if you know what you are doing. This might represent a security risk and is usually unneeded. Only those interfaces with the <code>sourceroute</code> option will have their setting changed; the value assigned to the setting will be the value specified (if any) or 1 if no value is given.</dd>
<dl>
<dd> <code>Note</code> <br/>
 This option does not work with a wild-card <i>interface</i> name (e.g., eth0.+) in the INTERFACE column.  <code>tcpflags[={0|1}]</code></dd>
<dl>
<dd>Packets arriving on this interface are checked for certain illegal combinations of TCP flags. Packets found to have such a combination of flags are handled according to the setting of TCP_FLAGS_DISPOSITION after having been logged according to the setting of TCP_FLAGS_LOG_LEVEL. Beginning with Shorewall 4.6.0, tcpflags=1 is the default. To disable this option, specify tcpflags=0.</dd></dl>
<p> <code>unmanaged</code></p>
<dl>
<dd>Added in Shorewall 4.5.18. Causes all traffic between the firewall and hosts on the interface to be accepted. When this option is given:</dd>
<dl>
<dd>&bull; The ZONE column must contain &#8216;-&#8216;.</dd></dl>
<dl>
<dd>&bull; Only the following other options are allowed with <code>unmanaged</code>:</dd>
<dl>
<dd><code>arp_filter</code></dd></dl>
<dl>
<dd><code>arp_ignore</code></dd></dl>
<dl>
<dd><code>ignore</code></dd></dl>
<dl>
<dd><code>routefilter</code></dd></dl>
<dl>
<dd><code>optional</code></dd></dl>
<dl>
<dd><code>physical</code></dd></dl>
<dl>
<dd><code>routefilter</code></dd></dl>
<dl>
<dd><code>sourceroute</code></dd></dl>
<dl>
<dd><code>proxyndp</code></dd></dl>
</dl>
</dl>
<p> <code>upnp</code></p>
<dl>
<dd>Incoming requests from this interface may be remapped via UPNP (upnpd). See m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/UPnP.html">http://www.shorewall.net/UPnP.html</a></code>m[][19].</dd></dl>
<p> <code>upnpclient</code></p>
<dl>
<dd>This option is intended for laptop users who always run Shorewall on their system yet need to run UPnP-enabled client apps such as Transmission (BitTorrent client). The option causes Shorewall to detect the default gateway through the interface and to accept UDP packets from that gateway. Note that, like all aspects of UPnP, this is a security hole so use this option at your own risk.</dd></dl>
<p> <code>wait</code>=<i>seconds</i></p>
<dl>
<dd>Added in Shorewall 4.4.10. Causes the generated script to wait up to <i>seconds</i> seconds for the interface to become usable before applying the <code>required</code> or <code>optional</code> options.</dd></dl>
</dl>
<h2>Example</h2>
<p>Example 1:</p>
<dl>
<dd>Suppose you have eth0 connected to a DSL modem and eth1 connected to your local network and that your local subnet is 192.168.1.0/24. The interface gets its IP address via DHCP from subnet 206.191.149.192/27. You have a DMZ with subnet 192.168.2.0/24 using eth2. Your iptables and/or kernel do not support &quot;Address Type Match&quot; and you prefer to specify broadcast addresses explicitly rather than having Shorewall detect them. </dd>
<p> Your entries for this setup would look like: </p>
<dl>
<dd>
<pre>FORMAT 1
#ZONE INTERFACE BROADCAST OPTIONS
net eth0 206.191.149.223 dhcp
loc eth1 192.168.1.255
dmz eth2 192.168.2.255</pre>
</dd></dl>
</dl>
<p> Example 2:</p>
<dl>
<dd>The same configuration without specifying broadcast addresses is: </dd>
<dl>
<dd>
<pre>FORMAT 2
#ZONE INTERFACE OPTIONS
net eth0 dhcp
loc eth1 
dmz eth2</pre>
</dd></dl>
</dl>
<p> Example 3:</p>
<dl>
<dd>You have a simple dial-in system with no Ethernet connections. </dd>
<dl>
<dd>
<pre>FORMAT 2
#ZONE INTERFACE OPTIONS
net ppp0 -</pre>
</dd></dl>
</dl>
<p> Example 4 (Shorewall 4.4.9 and later):</p>
<dl>
<dd>You have a bridge with no IP address and you want to allow traffic through the bridge. </dd>
<dl>
<dd>
<pre>FORMAT 2
#ZONE INTERFACE OPTIONS
- br0 bridge</pre>
</dd></dl>
</dl>
<h2>Files</h2>
<p>/etc/shorewall/interfaces</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[][20] </p>
<p> <a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-rtrules/">shorewall-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-secmarks/">shorewall-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-mangle/">shorewall-mangle</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</dt>
<dd>shorewall-hosts</dd>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-hosts.html">http://www.shorewall.net/manpages/shorewall-hosts.html</a></dd></dl>
<dt> 2.</dt>
<dd><a rel="nofollow" href="http://www.shorewall.net/FAQ.htm#faq18">http://www.shorewall.net/FAQ.htm#faq18</a></dd>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/FAQ.htm#faq18">http://www.shorewall.net/FAQ.htm#faq18</a></dd></dl>
<dt> 3.</dt>
<dd>shorewall-nesting</dd>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-nesting.html">http://www.shorewall.net/manpages/shorewall-nesting.html</a></dd></dl>
<dt> 4.</dt>
<dd>shorewall6-zones</dd>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-zones.html">http://www.shorewall.net/manpages6/shorewall6-zones.html</a></dd></dl>
<dt> 5.</dt>
<dd>Proxy ARP</dd>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net../ProxyARP.htm">http://www.shorewall.net../ProxyARP.htm</a></dd></dl>
<dt> 6.</dt>
<dd>shorewall-blacklist</dd>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-blacklist.html">http://www.shorewall.net/manpages/shorewall-blacklist.html</a></dd></dl>
<dt> 7.</dt>
<dd>shorewall-zones</dd>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-zones.html">http://www.shorewall.net/manpages/shorewall-zones.html</a></dd></dl>
<dt> 8.</dt>
<dd><a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5)</dd>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netmanpages/shorewall.conf.html">http://www.shorewall.netmanpages/shorewall.conf.html</a></dd></dl>
<dt> 9.</dt>
<dd>simple bridge</dd>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net../SimpleBridge.html">http://www.shorewall.net../SimpleBridge.html</a></dd></dl>
<dt>10.</dt>
<dd>Shorewall-perl for firewall/bridging</dd>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net../bridge-Shorewall-perl.html">http://www.shorewall.net../bridge-Shorewall-perl.html</a></dd></dl>
<dt>11.</dt>
<dd>shorewall-rules</dd>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-rules.html">http://www.shorewall.net/manpages/shorewall-rules.html</a></dd></dl>
<dt>12.</dt>
<dd>shorewall.conf</dd>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall.conf.html">http://www.shorewall.net/manpages/shorewall.conf.html</a></dd></dl>
<dt>13.</dt>
<dd>shorewall-maclist</dd>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-maclist.html">http://www.shorewall.net/manpages/shorewall-maclist.html</a></dd></dl>
<dt>14.</dt>
<dd><a rel="nofollow" href="http://www.shorewall.net/Dynamic.html">http://www.shorewall.net/Dynamic.html</a></dd>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/Dynamic.html">http://www.shorewall.net/Dynamic.html</a></dd></dl>
<dt>15.</dt>
<dd><a rel="nofollow" href="http://www.shorewall.net/bridge-Shorewall-perl.html#Multiple">http://www.shorewall.net/bridge-Shorewall-perl.html#Multiple</a></dd>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/bridge-Shorewall-perl.html#Multiple">http://www.shorewall.net/bridge-Shorewall-perl.html#Multiple</a></dd></dl>
<dt>16.</dt>
<dd>shorewall-proxyarp</dd>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-proxyarp.html">http://www.shorewall.net/manpages/shorewall-proxyarp.html</a></dd></dl>
<dt>17.</dt>
<dd><a rel="nofollow" href="http://tldp.org/HOWTO/Proxy-ARP-Subnet/index.html.">http://tldp.org/HOWTO/Proxy-ARP-Subnet/index.html.</a></dd>
<dl>
<dd><a rel="nofollow" href="http://tldp.org/HOWTO/Proxy-ARP-Subnet/index.html">http://tldp.org/HOWTO/Proxy-ARP-Subnet/index.html</a></dd></dl>
<dt>18.</dt>
<dd>shorewall-providers</dd>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-providers.html">http://www.shorewall.net/manpages/shorewall-providers.html</a></dd></dl>
<dt>19.</dt>
<dd><a rel="nofollow" href="http://www.shorewall.net/UPnP.html">http://www.shorewall.net/UPnP.html</a></dd>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/UPnP.html">http://www.shorewall.net/UPnP.html</a></dd></dl>
<dt>20.</dt>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dd>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dd></dl>
</dl></dl></dl></dl></dl></dl></dl></dl></dl></dl></dl></dl></dl>