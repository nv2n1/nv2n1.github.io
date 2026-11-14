---
title: "firewalld-zones(5)"
name: "firewalld-zones"
section: "5"
letter: "f"
url: "/docs/linux/man/5-firewalld-zones/"
description: "firewalld.zones – firewalld zones"
---

<p>firewalld.zones &#8211; firewalld zones</p>
<h2>Description</h2>
<h3>What is a zone?</h3>
<p>A network zone defines the level of trust for network connections. This is a one to many relation, which means that a connection can only be part of one zone, but a zone can be used for many network connections. </p>
<p> The zone defines the firewall features that are enabled in this zone: </p>
<p> <font SIZE="+1"> <code>Predefined services</code></p>
<dl>
<dd>A service is a combination of port and/or protocol entries. Optionally netfilter helper modules can be added and also a IPv4 and IPv6 destination address.</dl>
<p> </font><font SIZE="+2"> <code>Ports and protocols</code></p>
<dl>
<dd>Definition of <i>tcp</i> or <i>udp</i> ports, where ports can be a single port or a port range.</dl>
<p> </font><font SIZE="+3"> <code>ICMP blocks</code></p>
<dl>
<dd>Blocks selected Internet Control Message Protocol (ICMP) messages. These messages are either information requests or created as a reply to information requests or in error conditions.</dl>
<p> </font><font SIZE="+4"> <code>Masquerading</code></p>
<dl>
<dd>The addresses of a private network are mapped to and hidden behind a public IP address. This is a form of address translation.</dl>
<p> </font><font SIZE="+5"> <code>Forward ports</code></p>
<dl>
<dd>A forward port is either mapped to the same port on another host or to another port on the same host or to another port on another host.</dl>
<p> </font><font SIZE="+6"> <code>Rich language rules</code></p>
<dl>
<dd>The rich language extends the elements (service, port, icmp-block, masquerade, forward-port and source-port) with additional source and destination addresses, logging, actions and limits for logs and actions. It can also be used for host or network white and black listing (for more information, please have a look at <code><a href="/docs/linux/man/5-firewalld-richlanguage/">firewalld.richlanguage</a></code>(5)).</dl>
<p> For more information on the zone file format, please have a look at <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). </font></p>
<h3>Which zones are available?</h3>
<p>Here are the zones provided by firewalld sorted according to the default trust level of the zones from untrusted to trusted: </p>
<p> drop</p>
<dl>
<dd>Any incoming network packets are dropped, there is no reply. Only outgoing network connections are possible.</dl>
<p> block</p>
<dl>
<dd>Any incoming network connections are rejected with an <i>icmp-host-prohibited</i> message for IPv4 and <i>icmp6-adm-prohibited</i> for IPv6. Only network connections initiated within this system are possible.</dl>
<p> public</p>
<dl>
<dd>For use in public areas. You do not trust the other computers on networks to not harm your computer. Only selected incoming connections are accepted.</dl>
<p> external</p>
<dl>
<dd>For use on external networks with masquerading enabled especially for routers. You do not trust the other computers on networks to not harm your computer. Only selected incoming connections are accepted.</dl>
<p> dmz</p>
<dl>
<dd>For computers in your demilitarized zone that are publicly-accessible with limited access to your internal network. Only selected incoming connections are accepted.</dl>
<p> work</p>
<dl>
<dd>For use in work areas. You mostly trust the other computers on networks to not harm your computer. Only selected incoming connections are accepted.</dl>
<p> home</p>
<dl>
<dd>For use in home areas. You mostly trust the other computers on networks to not harm your computer. Only selected incoming connections are accepted.</dl>
<p> internal</p>
<dl>
<dd>For use on internal networks. You mostly trust the other computers on the networks to not harm your computer. Only selected incoming connections are accepted.</dl>
<p> trusted</p>
<dl>
<dd>All network connections are accepted.</dl>
<h3>Which zone should be used?</h3>
<p>A public WIFI network connection for example should be mainly untrusted, a wired home network connection should be fairly trusted. Select the zone that best matches the network you are using.</p>
<h3>How to configure or add zones?</h3>
<p>To configure or add zones you can either use one of the firewalld interfaces to handle and change the configuration: These are the graphical configuration tool firewall-config, the command line tool <code>firewall-cmd</code> or the D-Bus interface. Or you can create or copy a zone file in one of the configuration directories. <i>/usr/lib/firewalld/zones</i> is used for default and fallback configurations and <i>/etc/firewalld/zones</i> is used for user created and customized configuration files.</p>
<h3>How to set or change a zone for a connection?</h3>
<p>The zone is stored into the ifcfg of the connection with <code>ZONE=</code> option. If the option is missing or empty, the default zone set in firewalld is used. </p>
<p> If the connection is controlled by NetworkManager, you can also use <code>nm-connection-editor</code> to change the zone. </p>
<p> For the addion or change of interfaces that are not under control of NetworkManager: firewalld tries to change the ZONE setting in the ifcfg file, if an ifcfg file exists that is using the interface. </p>
<p> Only for the removal of interfaces that are not under control of NetworkManager: firewalld is not trying to change the ZONE setting in the ifcfg file. This is needed to make sure that an ifdown of the interface will not result in a reset of the zone setting to the default zone. Only the zone binding is then removed in firewalld then.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-firewall-applet/">firewall-applet</a></code>(1), <code><a href="/docs/linux/man/1-firewalld/">firewalld</a></code>(1), <code><a href="/docs/linux/man/1-firewall-cmd/">firewall-cmd</a></code>(1), <code><a href="/docs/linux/man/1-firewall-config/">firewall-config</a></code>(1), <code><a href="/docs/linux/man/5-firewalld-conf/">firewalld.conf</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-direct/">firewalld.direct</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-dbus/">firewalld.dbus</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5), <code><a href="/docs/linux/man/1-firewall-offline-cmd/">firewall-offline-cmd</a></code>(1), <code><a href="/docs/linux/man/5-firewalld-richlanguage/">firewalld.richlanguage</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-zones/">firewalld.zones</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5)</p>
<h2>Notes</h2>
<p>firewalld home page:</p>
<dl>
<dd>m[blue]<code><a rel="nofollow" href="http://www.firewalld.org">http://www.firewalld.org</a></code>m[]</dl>
<p> More documentation with examples:</p>
<dl>
<dd>m[blue]<code><a rel="nofollow" href="http://fedoraproject.org/wiki/FirewallD">http://fedoraproject.org/wiki/FirewallD</a></code>m[]</dl>
<h2>Authors</h2>
<p><code>Thomas Woerner</code> &lt;twoerner [at] redhat.com&gt;</p>
<dl>
<dd>Developer</dl>
<p> <code>Jiri Popelka</code> &lt;jpopelka [at] redhat.com&gt;</p>
<dl>
<dd>Developer</dl>
