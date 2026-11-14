---
title: "firewalld-zone(5)"
name: "firewalld-zone"
section: "5"
letter: "f"
url: "/docs/linux/man/5-firewalld-zone/"
description: "firewalld.zone – firewalld zone configuration files"
---

<p>firewalld.zone &#8211; firewalld zone configuration files</p>
<h2>Synopsis</h2>
<pre><i>/etc/firewalld/zones/zone.xml</i>
<i>/usr/lib/firewalld/zones/zone.xml</i></pre>
<h2>Description</h2>
<p>A firewalld zone configuration file contains the information for a zone. These are the zone description, services, ports, protcols, icmp-blocks, masquerade, forward-ports and rich language rules in an XML file format. The file name has to be <i>zone_name</i>.xml where length of <i>zone_name</i> is currently limited to 17 chars. </p>
<p> This is the structure of a zone configuration file: </p>
<dl>
<dd>
<pre>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;zone [version=&quot;<i>versionstring</i>&quot;] [target=&quot;<i>ACCEPT</i>|<i>%%REJECT%%</i>|<i>DROP</i>&quot;]&gt;
 [ &lt;short&gt;<i>short description</i>&lt;/short&gt; ]
 [ &lt;description&gt;<i>description</i>&lt;/description&gt; ]
 [ &lt;interface name=&quot;<i>string</i>&quot;/&gt; ]
 [ &lt;source address=&quot;<i>address</i>[/<i>mask</i>]&quot;|mac=&quot;<i>MAC</i>&quot;|ipset=&quot;<i>ipset</i>&quot;/&gt; ]
 [ &lt;service name=&quot;<i>string</i>&quot;/&gt; ]
 [ &lt;port port=&quot;<i>portid</i>[-<i>portid</i>]&quot; protocol=&quot;<i>tcp</i>|<i>udp</i>|<i>sctp</i>|<i>dccp</i>&quot;/&gt; ]
 [ &lt;protcol value=&quot;<i>protocol</i>&quot;/&gt; ]
 [ &lt;icmp-block name=&quot;<i>string</i>&quot;/&gt; ]
 [ &lt;icmp-block-inversion/&gt; ]
 [ &lt;masquerade/&gt; ]
 [ &lt;forward-port port=&quot;<i>portid</i>[-<i>portid</i>]&quot; protocol=&quot;<i>tcp</i>|<i>udp</i>|<i>sctp</i>|<i>dccp</i>&quot; [to-port=&quot;<i>portid</i>[-<i>portid</i>]&quot;] [to-addr=&quot;<i>ipv4address</i>&quot;]/&gt; ]
 [ &lt;source-port port=&quot;<i>portid</i>[-<i>portid</i>]&quot; protocol=&quot;<i>tcp</i>|<i>udp</i>|<i>sctp</i>|<i>dccp</i>&quot;/&gt; ]
 [
 &lt;rule [family=&quot;<i>ipv4</i>|<i>ipv6</i>&quot;]&gt;
 [ &lt;source address=&quot;<i>address</i>[/<i>mask</i>]&quot;|mac=&quot;<i>MAC</i>&quot;|ipset=&quot;<i>ipset</i>&quot; [invert=&quot;<i>True</i>&quot;]/&gt; ]
 [ &lt;destination address=&quot;<i>address</i>[/<i>mask</i>]&quot; [invert=&quot;<i>True</i>&quot;]/&gt; ]
 [
 &lt;service name=&quot;<i>string</i>&quot;/&gt; |
 &lt;port port=&quot;<i>portid</i>[-<i>portid</i>]&quot; protocol=&quot;<i>tcp</i>|<i>udp</i>|<i>sctp</i>|<i>dccp</i>&quot;/&gt; |
 &lt;protocol value=&quot;<i>protocol</i>&quot;/&gt; |
 &lt;icmp-block name=&quot;<i>icmptype</i>&quot;/&gt; |
 &lt;icmp-type name=&quot;<i>icmptype</i>&quot;/&gt; |
 &lt;masquerade/&gt; |
 &lt;forward-port port=&quot;<i>portid</i>[-<i>portid</i>]&quot; protocol=&quot;<i>tcp</i>|<i>udp</i>|<i>sctp</i>|<i>dccp</i>&quot; [to-port=&quot;<i>portid</i>[-<i>portid</i>]&quot;] [to-addr=&quot;<i>address</i>&quot;]/&gt;
 ]
 [ &lt;log [prefix=&quot;<i>prefixtext</i>&quot;] [level=&quot;<i>emerg</i>|<i>alert</i>|<i>crit</i>|<i>err</i>|<i>warn</i>|<i>notice</i>|<i>info</i>|<i>debug</i>&quot;]&gt; [&lt;limit value=&quot;<i>rate</i>/<i>duration</i>&quot;/&gt;] &lt;/log&gt; ]
 [ &lt;audit&gt; [&lt;limit value=&quot;<i>rate</i>/<i>duration</i>&quot;/&gt;] &lt;/audit&gt; ]
 [
 &lt;accept&gt; [&lt;limit value=&quot;<i>rate</i>/<i>duration</i>&quot;/&gt;] &lt;/accept&gt; |
 &lt;reject [type=&quot;<i>rejecttype</i>&quot;]&gt; [&lt;limit value=&quot;<i>rate</i>/<i>duration</i>&quot;/&gt;] &lt;/reject&gt; |
 &lt;drop&gt; [&lt;limit value=&quot;<i>rate</i>/<i>duration</i>&quot;/&gt;] &lt;/drop&gt; |
 &lt;mark set=&quot;<i>mark</i>[/<i>mask</i>]&quot;&gt; [&lt;limit value=&quot;<i>rate</i>/<i>duration</i>&quot;/&gt;] &lt;/mark&gt;
 ]
 &lt;/rule&gt;
 ]
&lt;/zone&gt;</pre>
</dl>
<p> The config can contain these tags and attributes. Some of them are mandatory, others optional.</p>
<h3>zone</h3>
<p>The mandatory zone start and end tag defines the zone. This tag can only be used once in a zone configuration file. There are optional attributes for zones: </p>
<p> version=&quot;<i>string</i>&quot;</p>
<dl>
<dd>To give the zone a version.</dl>
<p> target=&quot;<i>ACCEPT</i>|<i>%%REJECT%%</i>|<i>DROP</i>&quot;</p>
<dl>
<dd>Can be used to accept, reject or drop every packet that doesn&#8217;t match any rule (port, service, etc.). The <i>ACCEPT</i> target is used in <i>trusted</i> zone to accept every packet not matching any rule. The <i>%%REJECT%%</i> target is used in <i>block</i> zone to reject (with default firewalld reject type) every packet not matching any rule. The <i>DROP</i> target is used in <i>drop</i> zone to drop every packet not matching any rule. If the target is not specified, every packet not matching any rule will be rejected.</dl>
<h3>short</h3>
<p>Is an optional start and end tag and is used to give a zone a more readable name.</p>
<h3>description</h3>
<p>Is an optional start and end tag to have a description for a zone.</p>
<h3>interface</h3>
<p>Is an optional empty-element tag and can be used several times. It can be used to bind an interface to a zone. You don&#8217;t need this for NetworkManager-managed interfaces, because NetworkManager binds interfaces to zones automatically. See also &#8216;How to set or change a zone for a connection?&#8217; in <code><a href="/docs/linux/man/5-firewalld-zones/">firewalld.zones</a></code>(5). You can use it as a fallback mechanism for interfaces that can&#8217;t be managed via NetworkManager. An interface entry has exactly one attribute: </p>
<p> name=&quot;<i>string</i>&quot;</p>
<dl>
<dd>The name of the interface to be bound to the zone.</dl>
<h3>source</h3>
<p>Is an optional empty-element tag and can be used several times. It can be used to bind a source address, address range, a MAC address or an ipset to a zone. A source entry has exactly one of these attributes: </p>
<p> address=&quot;<i>address</i>[/<i>mask</i>]&quot;</p>
<dl>
<dd>The source is either an IP address or a network IP address with a mask for IPv4 or IPv6. The network family (IPv4/IPv6) will be automatically discovered. For IPv4, the mask can be a network mask or a plain number. For IPv6 the mask is a plain number. The use of host names is not supported.</dl>
<p> mac=&quot;<i>MAC</i>&quot;</p>
<dl>
<dd>The source is a MAC address. It must be of the form XX:XX:XX:XX:XX:XX.</dl>
<p> ipset=&quot;<i>ipset</i>&quot;</p>
<dl>
<dd>The source is an ipset.</dl>
<h3>service</h3>
<p>Is an optional empty-element tag and can be used several times to have more than one service entry enabled. A service entry has exactly one attribute: </p>
<p> name=&quot;<i>string</i>&quot;</p>
<dl>
<dd>The name of the service to be enabled. To get a list of valid service names <code>firewall-cmd &#8211;list=services</code> can be used.</dl>
<h3>port</h3>
<p>Is an optional empty-element tag and can be used several times to have more than one port entry. All attributes of a port entry are mandatory: </p>
<p> port=&quot;<i>portid</i>[-<i>portid</i>]&quot;</p>
<dl>
<dd>The port can either be a single port number <i>portid</i> or a port range <i>portid</i>&#8211;<i>portid</i>.</dl>
<p> protocol=&quot;<i>tcp</i>|<i>udp</i>|<i>sctp</i>|<i>dccp</i>&quot;</p>
<dl>
<dd>The protocol can either be <i>tcp</i>, <i>udp</i>, <i>sctp</i> or <i>dccp</i>.</dl>
<h3>protocol</h3>
<p>Is an optional empty-element tag and can be used several times to have more than one protocol entry. All protocol has exactly one attribute: </p>
<p> value=&quot;<i>string</i>&quot;</p>
<dl>
<dd>The protocol can be any protocol supported by the system. Please have a look at <i>/etc/protocols</i> for supported protocols.</dl>
<h3>icmp-block</h3>
<p>Is an optional empty-element tag and can be used several times to have more than one icmp-block entry. Each icmp-block tag has exactly one mandatory attribute: </p>
<p> name=&quot;<i>string</i>&quot;</p>
<dl>
<dd>The name of the Internet Control Message Protocol (ICMP) type to be blocked. To get a list of valid ICMP types <code>firewall-cmd &#8211;list=icmptypes</code> can be used.</dl>
<h3>icmp-block-inversion</h3>
<p>Is an optional empty-element tag and can be used only once in a zone configuration. This flag inverts the icmp block handling. Only enabled ICMP types are accepted and all others are rejected in the zone.</p>
<h3>masquerade</h3>
<p>Is an optional empty-element tag. It can be used only once in a zone configuration and is not usable for IPv6. If it&#8217;s present masquerading is enabled for the zone. If you want to enable masquerading, you should enable it in the zone bound to the external interface.</p>
<h3>forward-port</h3>
<p>Is an optional empty-element tag and can be used several times to have more than one port or packet forward entry. This is for IPv4 only. Use rich language rules for IPv6. There are mandatory and also optional attributes for forward ports: </p>
<p> <font SIZE="+1"> <code>Mandatory attributes:</code></p>
<dl>
<dd>The local port and protocol to be forwarded. </p>
<p> port=&quot;<i>portid</i>[-<i>portid</i>]&quot;</p>
<dl>
<dd>The port can either be a single port number <i>portid</i> or a port range <i>portid</i>&#8211;<i>portid</i>.</dl>
<p> protocol=&quot;<i>tcp</i>|<i>udp</i>|<i>sctp</i>|<i>dccp</i>&quot;</p>
<dl>
<dd>The protocol can either be <i>tcp</i>, <i>udp</i>, <i>sctp</i> or <i>dccp</i>.</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Optional attributes:</code></p>
<dl>
<dd>The destination of the forward. For local forwarding add <code>to-port</code> only. For remote forwarding add <code>to-addr</code> and use <code>to-port</code> optionally if the destination port on the destination machine should be different. </p>
<p> to-port=&quot;<i>portid</i>[-<i>portid</i>]&quot;</p>
<dl>
<dd>The destination port or port range to forward to. If omitted, the value of the port= attribute will be used altogether with the to-addr attribute.</dl>
<p> to-addr=&quot;<i>address</i>&quot;</p>
<dl>
<dd>The destination IPv4 IP address.</dl>
</dl>
<p> </font></p>
<h3>source-port</h3>
<p>Is an optional empty-element tag and can be used several times to have more than one source port entry. All attributes of a source port entry are mandatory: </p>
<p> port=&quot;<i>portid</i>[-<i>portid</i>]&quot;</p>
<dl>
<dd>The port can either be a single port number <i>portid</i> or a port range <i>portid</i>&#8211;<i>portid</i>.</dl>
<p> protocol=&quot;<i>tcp</i>|<i>udp</i>|<i>sctp</i>|<i>dccp</i>&quot;</p>
<dl>
<dd>The protocol can either be <i>tcp</i>, <i>udp</i>, <i>sctp</i> or <i>dccp</i>.</dl>
<h3>rule</h3>
<p>Is an optional element tag and can be used several times to have more than one rich language rule entry. </p>
<p> The general rule structure: </p>
<dl>
<dd>
<pre>&lt;rule [family=&quot;<i>ipv4</i>|<i>ipv6</i>&quot;]&gt;
 [ &lt;source address=&quot;<i>address</i>[/<i>mask</i>]&quot; [invert=&quot;<i>True</i>&quot;]/&gt; ]
 [ &lt;destination address=&quot;<i>address</i>[/<i>mask</i>]&quot; [invert=&quot;<i>True</i>&quot;]/&gt; ]
 [
 &lt;service name=&quot;<i>string</i>&quot;/&gt; |
 &lt;port port=&quot;<i>portid</i>[-<i>portid</i>]&quot; protocol=&quot;<i>tcp</i>|<i>udp</i>|<i>sctp</i>|<i>dccp</i>&quot;/&gt; |
 &lt;protocol value=&quot;<i>protocol</i>&quot;/&gt; |
 &lt;icmp-block name=&quot;<i>icmptype</i>&quot;/&gt; |
 &lt;icmp-type name=&quot;<i>icmptype</i>&quot;/&gt; |
 &lt;masquerade/&gt; |
 &lt;forward-port port=&quot;<i>portid</i>[-<i>portid</i>]&quot; protocol=&quot;<i>tcp</i>|<i>udp</i>|<i>sctp</i>|<i>dccp</i>&quot; [to-port=&quot;<i>portid</i>[-<i>portid</i>]&quot;] [to-addr=&quot;<i>address</i>&quot;]/&gt; |
 &lt;source-port port=&quot;<i>portid</i>[-<i>portid</i>]&quot; protocol=&quot;<i>tcp</i>|<i>udp</i>|<i>sctp</i>|<i>dccp</i>&quot;/&gt; |
 ]
 [ &lt;log [prefix=&quot;<i>prefixtext</i>&quot;] [level=&quot;<i>emerg</i>|<i>alert</i>|<i>crit</i>|<i>err</i>|<i>warn</i>|<i>notice</i>|<i>info</i>|<i>debug</i>&quot;]/&gt; [&lt;limit value=&quot;<i>rate</i>/<i>duration</i>&quot;/&gt;] &lt;/log&gt; ]
 [ &lt;audit&gt; [&lt;limit value=&quot;<i>rate</i>/<i>duration</i>&quot;/&gt;] &lt;/audit&gt; ]
 [
 &lt;accept&gt; [&lt;limit value=&quot;<i>rate</i>/<i>duration</i>&quot;/&gt;] &lt;/accept&gt; |
 &lt;reject [type=&quot;<i>rejecttype</i>&quot;]&gt; [&lt;limit value=&quot;<i>rate</i>/<i>duration</i>&quot;/&gt;] &lt;/reject&gt; |
 &lt;drop&gt; [&lt;limit value=&quot;<i>rate</i>/<i>duration</i>&quot;/&gt;] &lt;/drop&gt; |
 &lt;mark set=&quot;<i>mark</i>[/<i>mask</i>]&quot;&gt; [&lt;limit value=&quot;<i>rate</i>/<i>duration</i>&quot;/&gt;] &lt;/mark&gt;
 ]
&lt;/rule&gt;</pre>
</dl>
<p> Rule structure for source black or white listing: </p>
<dl>
<dd>
<pre>&lt;rule [family=&quot;<i>ipv4</i>|<i>ipv6</i>&quot;]&gt;
 &lt;source address=&quot;<i>address</i>[/<i>mask</i>]&quot; [invert=&quot;<i>True</i>&quot;]/&gt;
 [ &lt;log [prefix=&quot;<i>prefixtext</i>&quot;] [level=&quot;<i>emerg</i>|<i>alert</i>|<i>crit</i>|<i>err</i>|<i>warn</i>|<i>notice</i>|<i>info</i>|<i>debug</i>&quot;]/&gt; [&lt;limit value=&quot;<i>rate</i>/<i>duration</i>&quot;/&gt;] &lt;/log&gt; ]
 [ &lt;audit&gt; [&lt;limit value=&quot;<i>rate</i>/<i>duration</i>&quot;/&gt;] &lt;/audit&gt; ]
 &lt;accept&gt; [&lt;limit value=&quot;<i>rate</i>/<i>duration</i>&quot;/&gt;] &lt;/accept&gt; |
 &lt;reject [type=&quot;<i>rejecttype</i>&quot;]&gt; [&lt;limit value=&quot;<i>rate</i>/<i>duration</i>&quot;/&gt;] &lt;/reject&gt; |
 &lt;drop&gt; [&lt;limit value=&quot;<i>rate</i>/<i>duration</i>&quot;/&gt;] &lt;/drop&gt;
&lt;/rule&gt;</pre>
</dl>
<p> For a full description on rich language rules, please have a look at <code><a href="/docs/linux/man/5-firewalld-richlanguage/">firewalld.richlanguage</a></code>(5).</p>
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
