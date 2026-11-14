---
title: "firewalld-ipset(5)"
name: "firewalld-ipset"
section: "5"
letter: "f"
url: "/docs/linux/man/5-firewalld-ipset/"
description: "firewalld.ipset – firewalld ipset configuration files"
---

<p>firewalld.ipset &#8211; firewalld ipset configuration files</p>
<h2>Synopsis</h2>
<pre><i>/etc/firewalld/ipsets/ipset.xml</i>
<i>/usr/lib/firewalld/ipsets/ipset.xml</i></pre>
<h2>Description</h2>
<p>A firewalld ipset configuration file provides the information of an ip set for firewalld. The most important configuration options are type, option and entry. This example configuration file shows the structure of an ipset configuration file:</p>
<dl>
<dd>
<pre>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;ipset type=&quot;<i>hash:ip</i>&quot;&gt;
 &lt;short&gt;<i>My Ipset</i>&lt;/short&gt;
 &lt;description&gt;<i>description</i>&lt;/description&gt;
 &lt;entry&gt;<i>1.2.3.4</i>&lt;/entry&gt;
 &lt;entry&gt;<i>1.2.3.5</i>&lt;/entry&gt;
 &lt;entry&gt;<i>1.2.3.6</i>&lt;/entry&gt;
&lt;/ipset&gt;</pre>
</dl>
<h2>Options</h2>
<p>The config can contain these tags and attributes. Some of them are mandatory, others optional.</p>
<h3>ipset</h3>
<p>The mandatory ipset start and end tag defines the ipset. This tag can only be used once in a ipset configuration file. There is one mandatory and also optional attributes for ipsets: </p>
<p> type=&quot;<i>string</i>&quot;</p>
<dl>
<dd>The mandatory type of the ipset. To get the list of supported types, use <code>firewall-cmd &#8211;get-ipset-types</code>.</dl>
<p> version=&quot;<i>string</i>&quot;</p>
<dl>
<dd>To give the ipset a version.</dl>
<h3>short</h3>
<p>Is an optional start and end tag and is used to give an ipset a more readable name.</p>
<h3>description</h3>
<p>Is an optional start and end tag to have a description for a ipset.</p>
<h3>option</h3>
<p>Is an optional empty-element tag and can be used several times to have more than one option. Mostly all attributes of an option entry are mandatory: </p>
<p> name=&quot;<i>string</i>&quot;</p>
<dl>
<dd>The mandatory option name <i>string</i>.</dl>
<p> value=&quot;<i>string</i>&quot;</p>
<dl>
<dd>The optional value of the option.</dl>
<p> The supported options are: family: <i>&quot;inet&quot;</i>|<i>&quot;inet6&quot;</i>, timeout: <i>integer</i>, hashsize: <i>integer</i>, maxelem: <i>integer</i>. For more information on these options, please have a look at the ipset documentation.</p>
<h3>entry</h3>
<p>Is an optional start and end tag and can be used several times to have more than one entry entry. An entry entry does not have attributes.</p>
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
