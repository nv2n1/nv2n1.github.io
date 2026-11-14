---
title: "firewalld-conf(5)"
name: "firewalld-conf"
section: "5"
letter: "f"
url: "/docs/linux/man/5-firewalld-conf/"
description: "firewalld.conf – firewalld configuration file"
---

<p>firewalld.conf &#8211; firewalld configuration file</p>
<h2>Synopsis</h2>
<pre><i>/etc/firewalld/firewalld.conf</i></pre>
<h2>Description</h2>
<p>firewalld.conf is loaded by firewalld during the initialization process. The file contains the basic configuration options for firewalld.</p>
<h2>Options</h2>
<p>These are the options that can be set in the config file: </p>
<p> <code>DefaultZone</code></p>
<dl>
<dd>This sets the default zone for connections or interfaces if the zone is not selected or specified by NetworkManager, initscripts or command line tool. The default zone is public.</dl>
<p> <code>MinimalMark</code></p>
<dl>
<dd>For some firewall settings several rules are needed in different tables to be able to handle packets in the correct way. To achieve that these packets are marked using the MARK target <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8) and <code><a href="/docs/linux/man/8-ip6tables/">ip6tables</a></code>(8). With the MinimalMark option a block of marks can be reserved for private use; only marks over this value are used. The default MinimalMark value is 100.</dl>
<p> <code>CleanupOnExit</code></p>
<dl>
<dd>If firewalld stops, it cleans up all firewall rules. Setting this option to no or false leaves the current firewall rules untouched. The default value is yes or true.</dl>
<p> <code>Lockdown</code></p>
<dl>
<dd>If this option is enabled, firewall changes with the D-Bus interface will be limited to applications that are listed in the lockdown whitelist (see <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5)). The default value is no or false.</dl>
<p> <code>IPv6_rpfilter</code></p>
<dl>
<dd>If this option is enabled (it is by default), reverse path filter test on a packet for IPv6 is performed. If a reply to the packet would be sent via the same interface that the packet arrived on, the packet will match and be accepted, otherwise dropped. For IPv4 the rp_filter is controlled using sysctl.</dl>
<p> <code>IndividualCalls</code></p>
<dl>
<dd>If this option is disabled (it is by default), combined -restore calls are used and not individual calls to apply changes to the firewall. The use of individiual calls increases the time that is needed to apply changes and to start the daemon, but is good for debugging as error messages are more specific.</dl>
<p> <code>LogDenied</code></p>
<dl>
<dd>Add logging rules right before reject and drop rules in the INPUT, FORWARD and OUTPUT chains for the default rules and also final reject and drop rules in zones for the configured link-layer packet type. The possible values are: <i>all</i>, <i>unicast</i>, <i>broadcast</i>, <i>multicast</i> and <i>off</i>. The default setting is <i>off</i>, which disables the logging.</dl>
<p> <code>AutomaticHelpers</code></p>
<dl>
<dd>For the secure use of iptables and connection tracking helpers it is recommended to turn AutomaticHelpers off. But this might have side effects on other services using the netfilter helpers as the sysctl setting in /proc/sys/net/netfilter/nf_conntrack_helper will be changed. With the system setting, the default value set in the kernel or with sysctl will be used. Possible values are: <i>yes</i>, <i>no</i> and <i>system</i>. The default setting is <i>system</i>.</dl>
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
