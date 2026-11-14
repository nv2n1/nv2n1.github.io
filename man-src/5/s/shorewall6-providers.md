---
title: "shorewall6-providers(5)"
name: "shorewall6-providers"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall6-providers/"
description: "providers – Shorewall6 Providers file"
---

<p>providers &#8211; Shorewall6 Providers file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall6/providers</code></dl>
<h2>Description</h2>
<dd>This file is used to define additional routing tables. You will want to define an additional table if:</p>
<dl>
<dd>&bull; You have connections to more than one ISP or multiple connections to the same ISP</dl>
<dl>
<dd>&bull; You run Squid as a transparent proxy on a host other than the firewall.</dl>
<dl>
<dd>&bull; You have other requirements for policy routing.</dl>
<p> Each entry in the file defines a single routing table. If you wish to omit a column entry but want to include an entry in the next column, use &quot;-&quot; for the omitted entry. The columns in the file are as follows. <code>NAME</code> &#8211; <i>name</i></p>
<dl>
<dd>The provider <i>name</i>. Must be a valid shell variable name. The names &#8216;local&#8217;, &#8216;main&#8217;, &#8216;default&#8217; and &#8216;unspec&#8217; are reserved and may not be used as provider names.</dl>
<p> <code>NUMBER</code> &#8211; <i>number</i></p>
<dl>
<dd>The provider number &#8212; a number between 1 and 15. Each provider must be assigned a unique value.</dl>
<p> <code>MARK</code> (Optional) &#8211; <i>value</i></p>
<dl>
<dd>A FWMARK <i>value</i> used in your m[blue]<code>shorewall6-mangle</code>m[]<font SIZE="-2">[1]</font>(5) file to direct packets to this provider. If HIGH_ROUTE_MARKS=Yes in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5), then the value must be a multiple of 256 between 256 and 65280 or their hexadecimal equivalents (0x0100 and 0xff00 with the low-order byte of the value being zero). Otherwise, the value must be between 1 and 255. Each provider must be assigned a unique mark value. This column may be omitted if you don&#8217;t use packet marking to direct connections to a particular provider.</dl>
<p> <code>DUPLICATE</code> &#8211; <i>routing-table-name</i></p>
<dl>
<dd>The name of an existing table to duplicate to create this routing table. May be <code>main</code> or the name of a previously listed provider. You may select only certain entries from the table to copy by using the COPY column below.</dl>
<p> <code>INTERFACE</code> &#8211; <i>interface</i></p>
<dl>
<dd>The name of the network interface to the provider. Must be listed in m[blue]<code>shorewall6-interfaces</code>m[]<font SIZE="-2">[3]</font>(5).</dl>
<p> <code>GATEWAY</code> &#8211; {<code>&#8211;</code>|<i>address</i>|<code>detect|none</code>}</p>
<dl>
<dd>The IP address of the provider&#8217;s gateway router. You can enter <code>detect</code> here and Shorewall6 will attempt to detect the gateway automatically. Beginning with Shorewall 5.0.6, you may also enter <code>none</code>. This causes creation of a routing table with no default route in it. For PPP devices, you may omit this column.</dl>
<p> <code>OPTIONS</code> (Optional) &#8211; [<code>&#8211;</code>|<i>option</i>[<code>,</code><i>option</i>]&#8230;]</p>
<dl>
<dd>A comma-separated list selected from the following. The order of the options is not significant but the list may contain no embedded white-space. autosrc</p>
<dl>
<dd>Added in Shorewall 4.5.17. Causes a host route to the provider&#8217;s gateway router to be added to the provider&#8217;s routing table. This is the default behavior unless overridden by a following <code>noautosrc</code> option.</dl>
<p> <code>balance[=</code><i>weight</i><code>]</code></p>
<dl>
<dd>Added in Shorewall 4.4.25. The providers that have <code>balance</code> specified will get outbound traffic load-balanced among them. By default, all interfaces with <code>balance</code> specified will have the same weight (1). Beginning with Shorewall 5.0.13, you can change the weight of an interface by specifying <code>balance=</code><i>weight</i> where <i>weight</i> is the weight of the route out of this interface. Prior to Shorewall 5.0.13, only one provider can specify this option.</dl>
<p> <code>fallback[=</code><i>weight</i><code>]</code></p>
<dl>
<dd>Added in Shorewall 4.4.25. Indicates that a default route through the provider should be added to the default routing table (table 253). If a <i>weight</i> is given, a balanced route is added with the weight of this provider equal to the specified <i>weight</i>. If the option is given without a <i>weight</i>, an separate default route is added through the provider&#8217;s gateway; the route has a metric equal to the provider&#8217;s NUMBER. Prior to Shorewall 5.0.13, at most one provider can specify this option and a <i>weight</i> may not be given.</dl>
<p> <code>track</code></p>
<dl>
<dd>If specified, inbound connections on this interface are to be tracked so that responses may be routed back out this same interface. You want to specify <code>track</code> if internet hosts will be connecting to local servers through this provider. Beginning with Shorewall 4.4.3, <code>track</code> defaults to the setting of the TRACK_PROVIDERS option in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[4]</font> (5). If you set TRACK_PROVIDERS=Yes and want to override that setting for an individual provider, then specify <code>notrack</code> (see below).</dl>
<p> <code>loose</code></p>
<dl>
<dd>Shorewall6 normally adds a routing rule for each IP address on an interface which forces traffic whose source is that IP address to be sent using the routing table for that interface. Setting <code>loose</code> prevents creation of such rules on this interface.</dl>
<p> <code>load=</code><i>probability</i></p>
<dl>
<dd>Added in Shorewall 4.6.0. This option provides an alternative method of load balancing based on probabilities. Providers to be balanced are given a <i>probability</i> (a number 0 &gt; n &gt;= 1) with up to 8 digits to the right of the decimal point. Beginning with Shorewall 4.6.10, a warning is issued if the sum of the probabilities is not 1.00000000.</dl>
<p> <code>noautosrc</code></p>
<dl>
<dd>Added in Shorewall 4.5.17. Prevents the addition of a host route to the provider&#8217;s gateway router from being added to the provider&#8217;s routing table. This option must be used with caution as it can cause start and restart failures.</dl>
<p> <code>notrack</code></p>
<dl>
<dd>Added in Shorewall 4.4.3. When specified, turns off <code>track</code>.</dl>
<p> <code>optional</code> (deprecated for use with providers that do not share an interface)</p>
<dl>
<dd>If the interface named in the INTERFACE column is not up and configured with an IPv4 address then ignore this provider. If not specified, the value of the <code>optional</code> option for the INTERFACE in m[blue]<code><a href="/docs/linux/man/5-shorewall6-interfaces/">shorewall6-interfaces</a>(5)</code>m[]<font SIZE="-2">[3]</font> is assumed. Use of that option is preferred to this one, unless an <i>address</i> is provider in the INTERFACE column.</dl>
<p> <code>primary</code></p>
<dl>
<dd>Added in Shorewall 4.6.6, <code>primary</code> is a synonym for <code>balance</code> (see above) and is preferred when the remaining providers specify <code>fallback</code> or <code>tproxy</code>.</dl>
<p> src=<i>source-address</i></p>
<dl>
<dd>Specifies the source address to use when routing to this provider and none is known (the local client has bound to the 0 address). May not be specified when an <i>address</i> is given in the INTERFACE column. If this option is not used, Shorewall6 substitutes the primary IP address on the interface named in the INTERFACE column.</dl>
<p> mtu=<i>number</i></p>
<dl>
<dd>Specifies the MTU when forwarding through this provider. If not given, the MTU of the interface named in the INTERFACE column is assumed.</dl>
<p> <code>tproxy</code></p>
<dl>
<dd>Added in Shorewall 4.5.4. Used for supporting the TPROXY action in <a href="/docs/linux/man/5-shorewall-tcrules/">shorewall-tcrules</a>(5). See m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/Shorewall_Squid_Usage.html">http://www.shorewall.net/Shorewall_Squid_Usage.html</a></code>m[]<font SIZE="-2">[5]</font>. When specified, the MARK, DUPLICATE and GATEWAY columns should be empty, INTERFACE should be set to &#8216;lo&#8217; and <code>tproxy</code> should be the only OPTION. Only one <code>tproxy</code> provider is allowed.</dl>
<p> <code>hostroute</code></p>
<dl>
<dd>Added in Shorewall 4.5.21. This is the default behavior that results in a host route to the defined <code>GATEWAY</code> being inserted into the main routing table and into the provider&#8217;s routing table. <code>hostroute</code> is required for older distributions but <code>nohostroute</code> (below) is appropriate for recent distributions. <code>hostroute</code> may interfere with Zebra&#8217;s ability to add routes on some distributions such as Debian 7.</dl>
<p> <code>nohostroute</code></p>
<dl>
<dd>Added in Shorewall 4.5.21. nohostroute inhibits addition of a host route to the defined <code>GATEWAY</code> being inserted into the main routing table and into the provider&#8217;s routing table. <code>nohostroute</code> is not appropriate for older distributions but is appropriate for recent distributions. <code>nohostroute</code> allows Zebra&#8217;s to correctly add routes on some distributions such as Debian 7.</dl>
<p> <code>persistent</code></p>
<dl>
<dd>Added in Shorewall 5.0.2 and alters the behavior of the <code>disable</code> command:</p>
<dl>
<dd>&bull; The provider&#8217;s routing table still contains the apprioriate default route.</dl>
<dl>
<dd>&bull; Unless the <code>noautosrc</code> option is specified, routing rules are generated to route traffic from the interfaces address(es) out of the provider&#8217;s routing table.</dl>
<dl>
<dd>&bull; Persistent routing rules in m[blue]<code><a href="/docs/linux/man/5-shorewall6-rtrules/">shorewall6-rtrules</a>(5)</code>m[]<font SIZE="-2">[6]</font> are present.</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 The generated script will attempt to reenable a disabled persistent provider during execution of the <code>start</code>, <code>restart</code> and <code>reload</code> commands. When <code>persistent</code> is not specified, only the <code>enable</code> and <code>reenable</code> commands can reenable the provider.  <code>COPY</code> &#8211; [{<code>none</code>|<i>interface</i><code>[,</code><i>interface</i>]&#8230;}]</p>
<dl>
<dd>A comma-separated list of other interfaces on your firewall. Wildcards specified using an asterisk (&quot;*&quot;) are permitted (e.g., tun* ). Usually used only when DUPLICATE is <code>main</code>. Only copy routes through INTERFACE and through interfaces listed here. If you only wish to copy routes through INTERFACE, enter <code>none</code> in this column. Beginning with Shorewall 4.5.17, blackhole, unreachable and prohibit routes are no longer copied by default but may be copied by including <code>blackhole</code>,<code>unreachable</code> and <code>prohibit</code> respectively in the COPY list.</dl>
<h2>Examples</h2>
<p>Example 1:</p>
<dl>
<dd>You run squid in your DMZ on IP address 2002:ce7c:92b4:1::2. Your DMZ interface is eth2 </p>
<dl>
<dd>
<pre> #NAME NUMBER MARK DUPLICATE INTERFACE GATEWAY OPTIONS
 Squid 1 1 - eth2 2002:ce7c:92b4:1::2 -</pre>
</dl>
</dl>
<p> Example 2:</p>
<dl>
<dd>eth0 connects to ISP 1. The ISP&#8217;s gateway router has IP address 2001:ce7c:92b4:1::2. </p>
<p> eth1 connects to ISP 2. The ISP&#8217;s gateway router has IP address 2001:d64c:83c9:12::8b. </p>
<p> eth2 connects to a local network. </p>
<dl>
<dd>
<pre> #NAME NUMBER MARK DUPLICATE INTERFACE GATEWAY OPTIONS COPY
 ISP1 1 1 main eth0 2001:ce7c:92b4:1::2 track eth2
 ISP2 2 2 main eth1 2001:d64c:83c9:12::8b track eth2</pre>
</dl>
</dl>
<h2>Files</h2>
<p>/etc/shorewall6/providers</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/MultiISP.html">http://www.shorewall.net/MultiISP.html</a></code>m[]<font SIZE="-2">[7]</font> </p>
<p> m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[]<font SIZE="-2">[8]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall6/">shorewall6</a>(8), <a href="/docs/linux/man/5-shorewall6-accounting/">shorewall6-accounting</a>(5), <a href="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5), <a href="/docs/linux/man/5-shorewall6-blacklist/">shorewall6-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall6-hosts/">shorewall6-hosts</a>(5), <a href="/docs/linux/man/5-shorewall6-interfaces/">shorewall6-interfaces</a>(5), <a href="/docs/linux/man/5-shorewall6-maclist/">shorewall6-maclist</a>(5), <a href="/docs/linux/man/5-shorewall6-netmap/">shorewall6-netmap</a>(5),<a href="/docs/linux/man/5-shorewall6-params/">shorewall6-params</a>(5), <a href="/docs/linux/man/5-shorewall6-policy/">shorewall6-policy</a>(5), <a href="/docs/linux/man/5-shorewall6-rtrules/">shorewall6-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall6-routestopped/">shorewall6-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall6-rules/">shorewall6-rules</a>(5), <a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5), <a href="/docs/linux/man/5-shorewall6-secmarks/">shorewall6-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall6-tcclasses/">shorewall6-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall6-tcdevices/">shorewall6-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall6-mangle/">shorewall6-mangle</a>(5), <a href="/docs/linux/man/5-shorewall6-tos/">shorewall6-tos</a>(5), <a href="/docs/linux/man/5-shorewall6-tunnels/">shorewall6-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall6-zones/">shorewall6-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall6-mangle</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-mangle.html">http://www.shorewall.net/manpages6/shorewall6-mangle.html</a></dl>
<dt> 2.</p>
<dd>shorewall6.conf</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6.conf.html">http://www.shorewall.net/manpages6/shorewall6.conf.html</a></dl>
<dt> 3.</p>
<dd>shorewall6-interfaces</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-interfaces.html">http://www.shorewall.net/manpages6/shorewall6-interfaces.html</a></dl>
<dt> 4.</p>
<dd>shorewall6.conf</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorwewall6.conf.html">http://www.shorewall.net/manpages6/shorwewall6.conf.html</a></dl>
<dt> 5.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/Shorewall_Squid_Usage.html">http://www.shorewall.net/Shorewall_Squid_Usage.html</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/Shorewall_Squid_Usage.html">http://www.shorewall.net/Shorewall_Squid_Usage.html</a></dl>
<dt> 6.</p>
<dd><a href="/docs/linux/man/5-shorewall6-rtrules/">shorewall6-rtrules</a>(5)</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netshorewall-rtrules.html">http://www.shorewall.netshorewall-rtrules.html</a></dl>
<dt> 7.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/MultiISP.html">http://www.shorewall.net/MultiISP.html</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/MultiISP.html">http://www.shorewall.net/MultiISP.html</a></dl>
<dt> 8.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dl>
