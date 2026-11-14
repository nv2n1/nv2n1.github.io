---
title: "firewalld-direct(5)"
name: "firewalld-direct"
section: "5"
letter: "f"
url: "/docs/linux/man/5-firewalld-direct/"
description: "firewalld.direct – firewalld direct configuration file"
---

<p>firewalld.direct &#8211; firewalld direct configuration file</p>
<h2>Synopsis</h2>
<pre><i>/etc/firewalld/direct.xml</i></pre>
<h2>Description</h2>
<p>Direct configuration gives a more direct access to the firewall. It requires user to know basic <a href="/docs/linux/man/6-ip/">ip</a>(6)tables/ebtables concepts, i.e. <i>table</i> (filter/mangle/nat/&#8230;), <i>chain</i> (INPUT/OUTPUT/FORWARD/&#8230;), <i>commands</i> (-A/-D/-I/&#8230;), <i>parameters</i> (-p/-s/-d/-j/&#8230;) and <i>targets</i> (ACCEPT/DROP/REJECT/&#8230;). Direct configuration should be used only as a last resort when it&#8217;s not possible to use <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). See also <i>Direct Options</i> in <code><a href="/docs/linux/man/1-firewall-cmd/">firewall-cmd</a></code>(1). </p>
<p> A firewalld direct configuration file contains informations about permanent direct chains, rules and passthrough &#8230; </p>
<p> This is the structure of a direct configuration file: </p>
<dl>
<dd>
<pre>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;direct&gt;
 [ &lt;chain ipv=&quot;<i>ipv4</i>|<i>ipv6</i>|<i>eb</i>&quot; table=&quot;<i>table</i>&quot; chain=&quot;<i>chain</i>&quot;/&gt; ]
 [ &lt;rule ipv=&quot;<i>ipv4</i>|<i>ipv6</i>|<i>eb</i>&quot; table=&quot;<i>table</i>&quot; chain=&quot;<i>chain</i>&quot; priority=&quot;<i>priority</i>&quot;&gt; args &lt;/rule&gt; ]
 [ &lt;passthrough ipv=&quot;<i>ipv4</i>|<i>ipv6</i>|<i>eb</i>&quot;&gt; args &lt;/passthrough&gt; ]
&lt;/direct&gt;</pre>
</dl>
<h3>direct</h3>
<p>The mandatory direct start and end tag defines the direct. This tag can only be used once in a direct configuration file. There are no attributes for direct.</p>
<h3>chain</h3>
<p>Is an optional empty-element tag and can be used several times. It can be used to define names for additional chains. A chain entry has exactly three attributes: </p>
<p> ipv=&quot;<i>ipv4</i>|<i>ipv6</i>|<i>eb</i>&quot;</p>
<dl>
<dd>The IP family where the chain will be created. This can be either <i>ipv4</i>, <i>ipv6</i> or <i>eb</i>.</dl>
<p> table=&quot;<i>table</i>&quot;</p>
<dl>
<dd>The table name where the chain will be created. This can be one of the tables that can be used for iptables, ip6tables or ebtables. For the possible values, see TABLES section in the iptables, ip6tables or ebtables man pages.</dl>
<p> chain=&quot;<i>chain</i>&quot;</p>
<dl>
<dd>The name of the chain, that will be created. Please make sure that there is no other chain with this name already.</dl>
<p> Please remember to add a rule or passthrough rule with an <code>&#8211;jump</code> or <code>&#8211;goto</code> option to connect the chain to another one.</p>
<h3>rule</h3>
<p>Is an optional element tag and can be used several times. It can be used to add rules to a built-in or added chain. A rule entry has exactly four attributes: </p>
<p> ipv=&quot;<i>ipv4</i>|<i>ipv6</i>|<i>eb</i>&quot;</p>
<dl>
<dd>The IP family where the rule will be added. This can be either <i>ipv4</i>, <i>ipv6</i> or <i>eb</i>.</dl>
<p> table=&quot;<i>table</i>&quot;</p>
<dl>
<dd>The table name where the rule will be added. This can be one of the tables that can be used for iptables, ip6tables or ebtables. For the possible values, see TABLES section in the iptables, ip6tables or ebtables man pages.</dl>
<p> chain=&quot;<i>chain</i>&quot;</p>
<dl>
<dd>The name of the chain where the rule will be added. This can be either a built-in chain or a chain that has been created with the chain tag. If the chain name is a built-in chain, then the rule will be added to <i>chain</i>_direct, else the supplied chain name is used. <i>chain</i>_direct is created internally for all built-in chains to make sure that the added rules do not conflict with the rules created by firewalld.</dl>
<p> priority=&quot;<i>priority</i>&quot;</p>
<dl>
<dd>The priority is used to order rules. Priority 0 means add rule on top of the chain, with a higher priority the rule will be added further down. Rules with the same priority are on the same level and the order of these rules is not fixed and may change. If you want to make sure that a rule will be added after another one, use a low priority for the first and a higher for the following.</dl>
<p> The <i>args</i> can be any arguments of iptables or ip6tables, that do not conflict with the table or chain attributes.</p>
<h3>passthrough</h3>
<p>Is an optional element tag and can be used several times. It can be used to add rules to a built-in or added chain. A rule entry has exactly one attribute: </p>
<p> ipv=&quot;<i>ipv4</i>|<i>ipv6</i>|<i>eb</i>&quot;</p>
<dl>
<dd>The IP family where the passthrough rule will be added. This can be either <i>ipv4</i>, <i>ipv6</i> or <i>eb</i>.</dl>
<p> The <i>args</i> can be any arguments of iptables or ip6tables. </p>
<p> The passthrough rule will be added to the chain directly. There is no mechanism like for the direct <code>rule</code> above. The user of the passthrough rule has to make sure that there will be no conflict with the rules created by firewalld.</p>
<h2>Example</h2>
<p>Blacklisting of the networks 192.168.1.0/24 and 192.168.5.0/24 with logging and dropping early in the raw table:</p>
<dl>
<dd>
<pre>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;direct&gt;
 &lt;chain ipv=&quot;ipv4&quot; table=&quot;raw&quot; chain=&quot;blacklist&quot;/&gt;
 &lt;rule ipv=&quot;ipv4&quot; table=&quot;raw&quot; chain=&quot;PREROUTING&quot; priority=&quot;0&quot;&gt;-s 192.168.1.0/24 -j blacklist&lt;/rule&gt;
 &lt;rule ipv=&quot;ipv4&quot; table=&quot;raw&quot; chain=&quot;PREROUTING&quot; priority=&quot;1&quot;&gt;-s 192.168.5.0/24 -j blacklist&lt;/rule&gt;
 &lt;rule ipv=&quot;ipv4&quot; table=&quot;raw&quot; chain=&quot;blacklist&quot; priority=&quot;0&quot;&gt;-m limit --limit 1/min -j LOG --log-prefix &quot;blacklisted: &quot;&lt;/rule&gt;
 &lt;rule ipv=&quot;ipv4&quot; table=&quot;raw&quot; chain=&quot;blacklist&quot; priority=&quot;1&quot;&gt;-j DROP&lt;/rule&gt;
&lt;/direct&gt;</pre>
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
