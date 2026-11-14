---
title: "firewalld-icmptype(5)"
name: "firewalld-icmptype"
section: "5"
letter: "f"
url: "/docs/linux/man/5-firewalld-icmptype/"
description: "firewalld.icmptype – firewalld icmptype configuration files"
---

<p>firewalld.icmptype &#8211; firewalld icmptype configuration files</p>
<h2>Synopsis</h2>
<pre><i>/etc/firewalld/icmptypes/icmptype.xml</i>
<i>/usr/lib/firewalld/icmptypes/icmptype.xml</i></pre>
<h2>Description</h2>
<p>A firewalld icmptype configuration file provides the information for an Internet Control Message Protocol (ICMP) type for firewalld. This example configuration file shows the structure of an icmptype configuration file:</p>
<dl>
<dd>
<pre>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;icmptype&gt;
 &lt;short&gt;<i>My Icmptype</i>&lt;/short&gt;
 &lt;description&gt;<i>description</i>&lt;/description&gt;
 &lt;destination ipv4=&quot;<i>yes</i>&quot; ipv6=&quot;<i>yes</i>&quot;/&gt;
&lt;/icmptype&gt;</pre>
</dl>
<h2>Options</h2>
<p>The config can contain these tags and attributes. Some of them are mandatory, others optional.</p>
<h3>icmptype</h3>
<p>The mandatory icmptype start and end tag defines the icmptype. This tag can only be used once in an icmptype configuration file. This tag has optional attributes: </p>
<p> version=&quot;<i>string</i>&quot;</p>
<dl>
<dd>To give the icmptype a version.</dl>
<h3>short</h3>
<p>Is an optional start and end tag and is used to give an icmptype a more readable name.</p>
<h3>description</h3>
<p>Is an optional start and end tag to have a description for a icmptype.</p>
<h3>destination</h3>
<p>Is an optional empty-element tag and can be used only once. The destination tag specifies if an icmptype entry is available for IPv4 and/or IPv6. The default is IPv4 and IPv6, where this tag can be missing. </p>
<p> ipv4=&quot;<i>bool</i>&quot;</p>
<dl>
<dd>Describes if the icmptype is available for IPv4.</dl>
<p> ipv6=&quot;<i>bool</i>&quot;</p>
<dl>
<dd>Describes if the icmptype is available for IPv6.</dl>
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
