---
title: "firewalld-helper(5)"
name: "firewalld-helper"
section: "5"
letter: "f"
url: "/docs/linux/man/5-firewalld-helper/"
description: "firewalld.helper – firewalld helper configuration files"
---

<p>firewalld.helper &#8211; firewalld helper configuration files</p>
<h2>Synopsis</h2>
<pre><i>/etc/firewalld/helpers/helper.xml</i>
<i>/usr/lib/firewalld/helpers/helper.xml</i></pre>
<h2>Description</h2>
<p>A firewalld helper configuration file provides the information of a helper entry for firewalld. The most important configuration options are ports, family and module. This example configuration file shows the structure of a helper configuration file:</p>
<dl>
<dd>
<pre>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;helper module=&quot;<i>nf_conntrack_module</i>&quot; [family=&quot;<i>ipv4</i>|<i>ipv6</i>&quot;]&gt;
 &lt;short&gt;<i>short</i>&lt;/short&gt;
 &lt;description&gt;<i>description</i>&lt;/description&gt;
 &lt;port <i>portid</i>[-<i>portid</i>]&quot; protocol=&quot;<i>tcp</i>|<i>udp</i>|<i>sctp</i>|<i>dccp</i>&quot;/&gt;
&lt;/helper&gt;</pre>
</dl>
<h2>Options</h2>
<p>The config can contain these tags and attributes. Some of them are mandatory, others optional.</p>
<h3>helper</h3>
<p>The mandatory helper start and end tag defines the helper. This tag can only be used once in a helper configuration file. There is one mandatory and also optional attributes for helper: </p>
<p> module=&quot;<i>string</i>&quot;</p>
<dl>
<dd>The mandatory module of the helper. This is one of the netfilter conntrack helper modules. The name starts with <i>nf_conntrack_</i>.</dl>
<p> family=&quot;<i>ipv4</i>|<i>ipv6</i>&quot;</p>
<dl>
<dd>The optional family of the helper. This can be one of these ipv types: <i>ipv4</i> or <i>ipv6</i>. If the family is not specified, then the helper is usable for <i>IPv4</i> and <i>IPv6</i>.</dl>
<p> version=&quot;<i>string</i>&quot;</p>
<dl>
<dd>To give the helper a version.</dl>
<h3>short</h3>
<p>Is an optional start and end tag and is used to give an icmptype a more readable name.</p>
<h3>description</h3>
<p>Is an optional start and end tag to have a description for a icmptype.</p>
<h3>port</h3>
<p>Is an mandatory empty-element tag and can be used several times to have more than one port entry. All attributes of a port entry are mandatory: </p>
<p> port=&quot;<i>string</i>&quot;</p>
<dl>
<dd>The port <i>string</i> can be a single port number or a port range <i>portid</i>&#8211;<i>portid</i> or also empty to match a protocol only.</dl>
<p> protocol=&quot;<i>string</i>&quot;</p>
<dl>
<dd>The protocol value can either be <code>tcp</code>, <code>udp</code>, <code>sctp</code> or <code>dccp</code>.</dl>
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
