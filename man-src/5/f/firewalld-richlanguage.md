---
title: "firewalld-richlanguage(5)"
name: "firewalld-richlanguage"
section: "5"
letter: "f"
url: "/docs/linux/man/5-firewalld-richlanguage/"
description: "firewalld.richlanguage – Rich Language Documentation"
---

<p>firewalld.richlanguage &#8211; Rich Language Documentation</p>
<h2>Description</h2>
<p>With the rich language more complex firewall rules can be created in an easy to understand way. The language uses keywords with values and is an abstract representation of ip*tables rules. The rich language extends the current zone elements (service, port, icmp-block, icmp-type, masquerade, forward-port and source-port) with additional source and destination addresses, logging, actions and limits for logs and actions. This page describes the rich language used in the command line client and D-Bus interface. For information about the rich language representation used in the zone configuration files, please have a look at <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). A rule is part of a zone. One zone can contain several rules. If some rules interact/contradict, the first rule that matches &quot;wins&quot;. <code>General rule structure</code></p>
<dl>
<dd>
<pre>rule
 [source]
 [destination]
 service|port|protocol|icmp-block|icmp-type|masquerade|forward-port|source-port
 [log]
 [audit]
 [accept|reject|drop|mark]</pre>
</dl>
<p> The complete rule is provided as a single line string. A destination is allowed here as long as it does not conflict with the destination of a service. <code>Rule structure for source black or white listing</code></p>
<dl>
<dd>
<pre>rule
 source
 [log]
 [audit]
 accept|reject|drop|mark</pre>
</dl>
<p> This is used to grant or limit access from a source to this machine or machines that are reachable by this machine. A destination is not allowed here. <code>Important information about element options:</code> Options for elements in a rule need to be added exactly after the element. If the option is placed somewhere else it might be used for another element as far as it matches the options of the other element or will result in a rule error.</p>
<h3>Rule</h3>
<dl>
<dd>
<pre>rule [family=&quot;ipv4|ipv6&quot;]</pre>
</dl>
<p> If the rule family is provided, it can be either &quot;ipv4&quot; or &quot;ipv6&quot;, which limits the rule to IPv4 or IPv6. If the rule family is not provided, the rule will be added for IPv4 and IPv6. If source or destination addresses are used in a rule, then the rule family need to be provided. This is also the case for port/packet forwarding.</p>
<h3>Source</h3>
<pre><code>source [not] address=&quot;address[/mask]&quot;|mac=&quot;mac-address&quot;|ipset=&quot;ipset&quot;</code></pre>
<p> With the source address the origin of a connection attempt can be limited to the source address. An address is either a single IP address, or a network IP address, a MAC address or an IPSet. The address has to match the rule family (IPv4/IPv6). Subnet mask is expressed in either dot-decimal (/x.x.x.x) or prefix (/x) notations for IPv4, and in prefix notation (/x) for IPv6 network addresses. It is possible to invert the sense of an address by adding <code>not</code> before <code>address</code>. All but the specified address will match then.</p>
<h3>Destination</h3>
<p>destination [not] address=&quot;address[/mask]&quot; With the destination address the target can be limited to the destination address. The destination address is using the same syntax as the source address. The use of source and destination addresses is optional and the use of a destination addresses is not possible with all elements. This depends on the use of destination addresses for example in service entries.</p>
<h3>Service</h3>
<p>service name=&quot;service name&quot; The service <i>service name</i> will be added to the rule. The service name is one of the firewalld provided services. To get a list of the supported services, use <code>firewall-cmd &#8211;get-services</code>. If a service provides a destination address, it will conflict with a destination address in the rule and will result in an error. The services using destination addresses internally are mostly services using multicast.</p>
<h3>Port</h3>
<p>port port=&quot;port value&quot; protocol=&quot;tcp|udp&quot; The port <i>port value</i> can either be a single port number <i>portid</i> or a port range <i>portid</i>&#8211;<i>portid</i>. The protocol can either be <i>tcp</i> or <i>udp</i>.</p>
<h3>Protocol</h3>
<p>protocol value=&quot;protocol value&quot; The protocol value can be either a protocol id number or a protocol name. For allowed protocol entries, please have a look at <i>/etc/protocols</i>.</p>
<h3>ICMP-Block</h3>
<p>icmp-block name=&quot;icmptype name&quot; The icmptype is the one of the icmp types firewalld supports. To get a listing of supported icmp types: <code>firewall-cmd &#8211;get-icmptypes</code> It is not allowed to specify an action here. icmp-block uses the action reject internally.</p>
<h3>Masquerade</h3>
<dl>
<dd>
<pre>masquerade</pre>
</dl>
<p> Turn on masquerading in the rule. A source and also a destination address can be provided to limit masquerading to this area. It is not allowed to specify an action here.</p>
<h3>ICMP-Type</h3>
<p>icmp-type name=&quot;icmptype name&quot; The icmptype is the one of the icmp types firewalld supports. To get a listing of supported icmp types: <code>firewall-cmd &#8211;get-icmptypes</code></p>
<h3>Forward-Port</h3>
<p>forward-port port=&quot;port value&quot; protocol=&quot;tcp|udp&quot; to-port=&quot;port value&quot; to-addr=&quot;address&quot; Forward port/packets from local port value with protocol &quot;tcp&quot; or &quot;udp&quot; to either another port locally or to another machine or to another port on another machine. The port value can either be a single port number or a port range <i>portid-portid</i>. The <code>to-addr</code> is an IP address. It is not allowed to specify an action here. forward-port uses the action accept internally.</p>
<h3>Source-Port</h3>
<p>source-port port=&quot;port value&quot; protocol=&quot;tcp|udp&quot; The source-port <i>port value</i> can either be a single port number <i>portid</i> or a port range <i>portid</i>&#8211;<i>portid</i>. The protocol can either be <i>tcp</i> or <i>udp</i>.</p>
<h3>Log</h3>
<dl>
<dd>
<pre>log [prefix=&quot;prefix text&quot;] [level=&quot;log level&quot;] [limit value=&quot;rate/duration&quot;]</pre>
</dl>
<p> Log new connection attempts to the rule with kernel logging for example in syslog. You can define a prefix text that will be added to the log message as a prefix. Log level can be one of &quot;<code>emerg</code>&quot;, &quot;<code>alert</code>&quot;, &quot;<code>crit</code>&quot;, &quot;<code>error</code>&quot;, &quot;<code>warning</code>&quot;, &quot;<code>notice</code>&quot;, &quot;<code>info</code>&quot; or &quot;<code>debug</code>&quot;, where default (i.e. if there&#8217;s no one specified) is &quot;<code>warning</code>&quot;. See <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) for description of levels. See Limit section for description of <code>limit</code> tag.</p>
<h3>Audit</h3>
<dl>
<dd>
<pre>audit [limit value=&quot;rate/duration&quot;]</pre>
</dl>
<p> Audit provides an alternative way for logging using audit records sent to the service auditd. Audit type will be discovered from the rule action automatically. Use of audit is optional. See Limit section for description of <code>limit</code> tag.</p>
<h3>Action</h3>
<p>An action can be one of <code>accept</code>, <code>reject</code>, <code>drop</code> or <code>mark</code>. The rule can either contain an element or also a source only. If the rule contains an element, then new connection matching the element will be handled with the action. If the rule does not contain an element, then everything from the source address will be handled with the action.</p>
<dl>
<dd>
<pre>accept [limit value=&quot;rate/duration&quot;]</pre>
</dl>
<dl>
<dd>
<pre>reject [type=&quot;reject type&quot;] [limit value=&quot;rate/duration&quot;]</pre>
</dl>
<dl>
<dd>
<pre>drop [limit value=&quot;rate/duration&quot;]</pre>
</dl>
<dl>
<dd>
<pre>mark set=&quot;mark[/mask]&quot; [limit value=&quot;rate/duration&quot;]</pre>
</dl>
<p> With <code>accept</code> all new connection attempts will be granted. With <code>reject</code> they will not be accepted and their source will get a reject ICMP(v6) message. The reject type can be set to specify appropriate ICMP(v6) error message. For valid reject types see <code>&#8211;reject-with type</code> in <code><a href="/docs/linux/man/8-iptables-extensions/">iptables-extensions</a></code>(8) man page. Because reject types are different for IPv4 and IPv6 you have to specify rule family when using reject type. With <code>drop</code> all packets will be dropped immediately, there is no information sent to the source. With <code>mark</code> all packets will be marked in the <code>PREROUTING</code> chain in the <code>mangle</code> table with the mark and mask combination. See Limit section for description of <code>limit</code> tag.</p>
<h3>Limit</h3>
<p>limit value=&quot;rate/duration&quot; It is possible to limit Log, Audit and Action. A rule using this tag will match until this limit is reached. The rate is a natural positive number [1, ..] The duration is of &quot;s&quot;, &quot;m&quot;, &quot;h&quot;, &quot;d&quot;. &quot;s&quot; means seconds, &quot;m&quot; minutes, &quot;h&quot; hours and &quot;d&quot; days. Maximum limit value is &quot;2/d&quot;, which means at maximum two matches per day.</p>
<h3>Information about logging and actions</h3>
<p>Logging can be done with the log and also with audit. A new chain is added to all zones: zone_log. This will be jumped into before the deny chain to be able to have a proper ordering. The rules or parts of them are placed in separate chains according to the action of the rule:</p>
<dl>
<dd>
<pre><i>zone</i>_log
<i>zone</i>_deny
<i>zone</i>_allow</pre>
</dl>
<p> Then all logging rules will be placed in the zone_log chain, which will be walked first. All reject and drop rules will be placed in the zone_deny chain, which will be walked after the log chain. All accept rules will be placed in the zone_allow chain, which will be walked after the deny chain. If a rule contains log and also deny or allow actions, the parts are placed in the matching chains.</p>
<h2>Examples</h2>
<p>These are examples of how to specify rich language rules. This format (i.e. one string that specifies whole rule) uses for example <code>firewall-cmd &#8211;add-rich-rule</code> (see <code><a href="/docs/linux/man/1-firewall-cmd/">firewall-cmd</a></code>(1)) as well as D-Bus interface.</p>
<h3>Example 1</h3>
<p>Enable new IPv4 and IPv6 connections for protocol &#8216;ah&#8217;</p>
<dl>
<dd>
<pre>rule protocol value=&quot;ah&quot; accept</pre>
</dl>
<h3>Example 2</h3>
<p>Allow new IPv4 and IPv6 connections for service ftp and log 1 per minute using audit</p>
<dl>
<dd>
<pre>rule service name=&quot;ftp&quot; log limit value=&quot;1/m&quot; audit accept</pre>
</dl>
<h3>Example 3</h3>
<p>Allow new IPv4 connections from address 192.168.0.0/24 for service tftp and log 1 per minutes using syslog</p>
<dl>
<dd>
<pre>rule family=&quot;ipv4&quot; source address=&quot;192.168.0.0/24&quot; service name=&quot;tftp&quot; log prefix=&quot;tftp&quot; level=&quot;info&quot; limit value=&quot;1/m&quot; accept</pre>
</dl>
<h3>Example 4</h3>
<p>New IPv6 connections from 1:2:3:4:6:: to service radius are all rejected and logged at a rate of 3 per minute. New IPv6 connections from other sources are accepted.</p>
<dl>
<dd>
<pre>rule family=&quot;ipv6&quot; source address=&quot;1:2:3:4:6::&quot; service name=&quot;radius&quot; log prefix=&quot;dns&quot; level=&quot;info&quot; limit value=&quot;3/m&quot; reject
rule family=&quot;ipv6&quot; service name=&quot;radius&quot; accept</pre>
</dl>
<h3>Example 5</h3>
<p>Forward IPv6 port/packets receiving from 1:2:3:4:6:: on port 4011 with protocol tcp to 1::2:3:4:7 on port 4012 rule family=&quot;ipv6&quot; source address=&quot;1:2:3:4:6::&quot; forward-port to-addr=&quot;1::2:3:4:7&quot; to-port=&quot;4012&quot; protocol=&quot;tcp&quot; port=&quot;4011&quot;</p>
<h3>Example 6</h3>
<p>White-list source address to allow all connections from 192.168.2.2</p>
<dl>
<dd>
<pre>rule family=&quot;ipv4&quot; source address=&quot;192.168.2.2&quot; accept</pre>
</dl>
<h3>Example 7</h3>
<p>Black-list source address to reject all connections from 192.168.2.3 </p>
<pre><code>rule family=&quot;ipv4&quot; source address=&quot;192.168.2.3&quot; reject type=&quot;icmp-admin-prohibited&quot;</code></pre>
<h3>Example 8</h3>
<p>Black-list source address to drop all connections from 192.168.2.4</p>
<dl>
<dd>
<pre>rule family=&quot;ipv4&quot; source address=&quot;192.168.2.4&quot; drop</pre>
</dl>
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
