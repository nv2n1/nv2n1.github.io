---
title: "firewalld-service(5)"
name: "firewalld-service"
section: "5"
letter: "f"
url: "/docs/linux/man/5-firewalld-service/"
description: "firewalld.service – firewalld service configuration files"
---

<p>firewalld.service &#8211; firewalld service configuration files</p>
<h2>Synopsis</h2>
<pre><i>/etc/firewalld/services/service.xml</i>
<i>/usr/lib/firewalld/services/service.xml</i></pre>
<h2>Description</h2>
<p>A firewalld service configuration file provides the information of a service entry for firewalld. The most important configuration options are ports, modules and destination addresses. This example configuration file shows the structure of a service configuration file:</p>
<dl>
<dd>
<pre>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;service&gt;
 &lt;short&gt;<i>My Service</i>&lt;/short&gt;
 &lt;description&gt;<i>description</i>&lt;/description&gt;
 &lt;port port=&quot;<i>137</i>&quot; protocol=&quot;<i>tcp</i>&quot;/&gt;
 &lt;protcol value=&quot;<i>igmp</i>&quot;/&gt;
 &lt;module name=&quot;<i>nf_conntrack_netbios_ns</i>&quot;/&gt;
 &lt;destination ipv4=&quot;<i>224.0.0.251</i>&quot; ipv6=&quot;<i>ff02::fb</i>&quot;/&gt;
&lt;/service&gt;</pre>
</dl>
<h2>Options</h2>
<p>The config can contain these tags and attributes. Some of them are mandatory, others optional.</p>
<h3>service</h3>
<p>The mandatory service start and end tag defines the service. This tag can only be used once in a service configuration file. There are optional attributes for services: </p>
<p> version=&quot;<i>string</i>&quot;</p>
<dl>
<dd>To give the service a version.</dl>
<h3>short</h3>
<p>Is an optional start and end tag and is used to give an icmptype a more readable name.</p>
<h3>description</h3>
<p>Is an optional start and end tag to have a description for a icmptype.</p>
<h3>port</h3>
<p>Is an optional empty-element tag and can be used several times to have more than one port entry. All attributes of a port entry are mandatory: </p>
<p> port=&quot;<i>string</i>&quot;</p>
<dl>
<dd>The port <i>string</i> can be a single port number or a port range <i>portid</i>&#8211;<i>portid</i> or also empty to match a protocol only.</dl>
<p> protocol=&quot;<i>string</i>&quot;</p>
<dl>
<dd>The protocol value can either be <i>tcp</i>, <i>udp</i>, <i>sctp</i> or <i>dccp</i>.</dl>
<p> For compatibility with older firewalld versions, it is possible to add protocols with the port option where the port is empty. With the addition of native protocol support in the service, this it not needed anymore. These entries will automatically be converted to protocols. With the next modification of the service file, the enries will be listed as protocols.</p>
<h3>protocol</h3>
<p>Is an optional empty-element tag and can be used several times to have more than one protocol entry. A protocol entry has exactly one attribute: </p>
<p> value=&quot;<i>string</i>&quot;</p>
<dl>
<dd>The protocol can be any protocol supported by the system. Please have a look at <i>/etc/protocols</i> for supported protocols.</dl>
<h3>source-port</h3>
<p>Is an optional empty-element tag and can be used several times to have more than one source port entry. All attributes of a source port entry are mandatory: </p>
<p> port=&quot;<i>string</i>&quot;</p>
<dl>
<dd>The port <i>string</i> can be a single port number or a port range <i>portid</i>&#8211;<i>portid</i>.</dl>
<p> protocol=&quot;<i>string</i>&quot;</p>
<dl>
<dd>The protocol value can either be <i>tcp</i>, <i>udp</i>, <i>sctp</i> or <i>dccp</i>.</dl>
<h3>module</h3>
<p>Is an optional empty-element tag and can be used several times to enable more than one netfilter kernel helper for the service. A module entry has exactly one attribute: </p>
<p> name=&quot;<i>string</i>&quot;</p>
<dl>
<dd>Defines the name of the kernel netfilter helper as a string.</dl>
<h3>destination</h3>
<p>Is an optional empty-element tag and can be used only once. The destination specifies the destination network as a network IP address (optional with /mask), or a plain IP address. The use of hostnames is not recommended, because these will only be resolved at service activation and transmitted to the kernel. For more information in this element, please have a look at <code>&#8211;destination</code> in <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8) and <code><a href="/docs/linux/man/8-ip6tables/">ip6tables</a></code>(8). </p>
<p> ipv4=&quot;<i>address</i>[/<i>mask</i>]&quot;</p>
<dl>
<dd>The IPv4 destination address with optional mask.</dl>
<p> ipv6=&quot;<i>address</i>[/<i>mask</i>]&quot;</p>
<dl>
<dd>The IPv6 destination address with optional mask.</dl>
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
