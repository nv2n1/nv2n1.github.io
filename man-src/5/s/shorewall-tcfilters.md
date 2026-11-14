---
title: "shorewall-tcfilters(5)"
name: "shorewall-tcfilters"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-tcfilters/"
description: "tcfilters – Shorewall u32/basic classifier rules file"
---

<p>tcfilters &#8211; Shorewall u32/basic classifier rules file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/tcfilters</code></dl>
<h2>Description</h2>
<dd>Entries in this file cause packets to be classified for traffic shaping. </p>
<p> Beginning with Shorewall 4.4.15, the file may contain entries for both IPv4 and IPv6. By default, all rules apply to IPv4 but that can be changed by inserting a line as follows: </p>
<p> IPV4</p>
<dl>
<dd>Following entries apply to IPv4.</dl>
<p> IPV6</p>
<dl>
<dd>Following entries apply to IPv6</dl>
<p> ALL</p>
<dl>
<dd>Following entries apply to both IPv4 and IPv6. Each entry is processed twice; once for IPv4 and once for IPv6.</dl>
<p> The columns in the file are as follows (where the column name is followed by a different name in parentheses, the different name is used in the alternate specification syntax). </p>
<p> <code>CLASS</code> &#8211; <i>interface</i><code>:</code><i>class</i></p>
<dl>
<dd>The name or number of an interface defined in m[blue]<code>shorewall-tcdevices</code>m[]<font SIZE="-2">[1]</font>(5) followed by a <i>class</i> number defined for that interface in m[blue]<code>shorewall-tcclasses</code>m[]<font SIZE="-2">[2]</font>(5).</dl>
<p> <code>SOURCE</code> &#8211; {<code>&#8211;</code>|<i>address</i>|+<i>ipset</i>}</p>
<dl>
<dd>Source of the packet. May be a host or network <i>address</i>. DNS names are not allowed. Beginning with Shorewall 4.6.0, an ipset name (prefixed with &#8216;+&#8217;) may be used if your kernel and ip6tables have the Basic Ematch capability and you set BASIC_FILTERS=Yes in m[blue]<code>shorewall.conf (5)</code>m[]<font SIZE="-2">[3]</font>. The ipset name may optionally be followed by a number or a comma separated list of src and/or dst enclosed in square brackets ([&#8230;]). See m[blue]<code><a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5)</code>m[]<font SIZE="-2">[4]</font> for details.</dl>
<p> <code>DEST</code> &#8211; {<code>&#8211;</code>|<i>address</i>|+<i>ipset</i>}</p>
<dl>
<dd>Destination of the packet. May be a host or network <i>address</i>. DNS names are not allowed. Beginning with Shorewall 4.6.0, an ipset name (prefixed with &#8216;+&#8217;) may be used if your kernel and ip6tables have the Basic Ematch capability and you set BASIC_FILTERS=Yes in m[blue]<code>shorewall.conf (5)</code>m[]<font SIZE="-2">[3]</font>. The ipset name may optionally be followed by a number or a comma separated list of src and/or dst enclosed in square brackets ([&#8230;]). See m[blue]<code><a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5)</code>m[]<font SIZE="-2">[4]</font> for details. </p>
<p> You may exclude certain hosts from the set already defined through use of an <i>exclusion</i> (see m[blue]<code>shorewall-exclusion</code>m[]<font SIZE="-2">[5]</font>(5)).</dl>
<p> <code>PROTO</code> &#8211; {<code>&#8211;</code>|{<i>protocol-number</i>|<i>protocol-name</i>|<code>all}[,&#8230;]}</code></p>
<dl>
<dd>Protocol. </p>
<p> Beginning with Shorewall 4.5.12, this column can accept a comma-separated list of protocols.</dl>
<p> <code>DPORT</code> &#8211; [<code>&#8211;</code>|<i>port-name-or-number</i>]</p>
<dl>
<dd>Optional destination Ports. A Port name (from <a href="/docs/linux/man/5-services/">services</a>(5)) or a <i>port number</i>; if the protocol is <code>icmp</code>, this column is interpreted as the destination icmp-type(s). </p>
<p> This column was previously labelled DEST PORT(S).</dl>
<p> <code>SPORT</code> &#8211; [<code>&#8211;</code>|<i>port-name-or-number</i>]</p>
<dl>
<dd>Optional source port. </p>
<p> This column was previously labelled SOURCE PORT(S).</dl>
<p> <code>TOS</code> (Optional) &#8211; [<code>&#8211;</code>|<i>tos</i>]</p>
<dl>
<dd>Specifies the value of the TOS field. The <i>tos</i> value can be any of the following: </p>
<dl>
<dd>&bull; <code>tos-minimize-delay</code></dl>
<dl>
<dd>&bull; <code>tos-maximize-throughput</code></dl>
<dl>
<dd>&bull; <code>tos-maximize-reliability</code></dl>
<dl>
<dd>&bull; <code>tos-minimize-cost</code></dl>
<dl>
<dd>&bull; <code>tos-normal-service</code></dl>
<dl>
<dd>&bull; <i>hex-number</i></dl>
<dl>
<dd>&bull; <i>hex-number</i>/<i>hex-number</i></dl>
<p> The <i>hex-number</i>s must be exactly two digits (e.g., 0x04)x.</dl>
<p> <code>LENGTH</code> &#8211; [<code>&#8211;</code>|<i>number</i>]</p>
<dl>
<dd>Optional &#8211; Must be a power of 2 between 32 and 8192 inclusive. Packets with a total length that is strictly less than the specified <i>number</i> will match the rule.</dl>
<p> <code>PRIORITY</code> &#8211; [<code>&#8211;</code>|<i>priority</i>]</p>
<dl>
<dd>Added in Shorewall 4.5.8. Specifies the rule <i>priority</i>. The <i>priority</i> value must be &gt; 0 and &lt;= 65535. </p>
<p> When a <i>priority</i> is not given: </p>
<dl>
<dd>&bull; For Shorewall versions prior to 4.5.8 &#8211; all filters have priority 10.</dl>
<dl>
<dd>&bull; For Shorewall 4.5.8 and later &#8211; for each device, the compiler maintains a high-water priority with an initial value of 0. When a filter has no <i>priority</i>, the high-water priority is incremented by 1 and assigned to the filter. When a <i>priority</i> greater than the high-water priority is entered in this column, the high-water priority is set to the specified <i>priority</i>. An attempt to assign a priority value greater than 65535 (explicitly or implicitly) raises an error.</dl>
<p> The default priority values used by other Shorewall-generated filters are as follows: </p>
<dl>
<dd>&bull; Classify by packet mark &#8211; ( <i>class priority</i> &lt;&lt; 8 ) | 20.</dl>
<dl>
<dd>&bull; Ingress policing &#8211; 10</dl>
<dl>
<dd>&bull; Simple TC ACK packets &#8211; 1</dl>
<dl>
<dd>&bull; Complex TC ACK packets &#8211; ( <i>class priority</i> &lt;&lt; 8 ) | 10.</dl>
<dl>
<dd>&bull; Classify by TOS &#8211; ( <i>class priority</i> &lt;&lt; 8 ) | 15.</dl>
<dl>
<dd>&bull; Class with &#8216;occurs&#8217; &#8211; 65535</dl>
</dl>
<h2>Example</h2>
<p>Example 1:</p>
<dl>
<dd>Place all &#8216;ping&#8217; traffic on interface 1 in class 10. Note that ALL cannot be used because IPv4 ICMP and IPv6 ICMP are two different protocols. </p>
<dl>
<dd>
<pre> #CLASS SOURCE DEST PROTO DPORT
 IPV4
 1:10 0.0.0.0/0 0.0.0.0/0 icmp echo-request
 1:10 0.0.0.0/0 0.0.0.0/0 icmp echo-reply
 IPV6
 1:10 ::/0 ::/0 icmp6 echo-request
 1:10 ::/0 ::/0 icmp6 echo-reply</pre>
</dl>
</dl>
<p> Example 2:</p>
<dl>
<dd>Add two filters with priority 10 (Shorewall 4.5.8 or later). </p>
<dl>
<dd>
<pre> #CLASS SOURCE DEST PROTO DPORT PRIORITY
 IPV4
 1:10 0.0.0.0/0 0.0.0.0/0 icmp echo-request 10
 1:10 0.0.0.0/0 0.0.0.0/0 icmp echo-reply 10</pre>
</dl>
</dl>
<h2>Files</h2>
<p>/etc/shorewall/tcfilters</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/traffic_shaping.htm">http://www.shorewall.net/traffic_shaping.htm</a></code>m[]<font SIZE="-2">[6]</font> </p>
<p> m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/MultiISP.html">http://www.shorewall.net/MultiISP.html</a></code>m[]<font SIZE="-2">[7]</font> </p>
<p> m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/PacketMarking.html">http://www.shorewall.net/PacketMarking.html</a></code>m[]<font SIZE="-2">[8]</font> </p>
<p> m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[]<font SIZE="-2">[9]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-ecn/">shorewall-ecn</a>(5), <a href="/docs/linux/man/5-shorewall-exclusion/">shorewall-exclusion</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall_interfaces/">shorewall_interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-rtrules/">shorewall-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-secmarks/">shorewall-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall-tcdevices</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-tcdevices.html">http://www.shorewall.net/manpages/shorewall-tcdevices.html</a></dl>
<dt> 2.</p>
<dd>shorewall-tcclasses</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-tcclasses.html">http://www.shorewall.net/manpages/shorewall-tcclasses.html</a></dl>
<dt> 3.</p>
<dd>shorewall.conf (5)</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netshorewall.conf.html">http://www.shorewall.netshorewall.conf.html</a></dl>
<dt> 4.</p>
<dd><a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5)</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netshorewall-ipsets.html">http://www.shorewall.netshorewall-ipsets.html</a></dl>
<dt> 5.</p>
<dd>shorewall-exclusion</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-exclusion.html">http://www.shorewall.net/manpages/shorewall-exclusion.html</a></dl>
<dt> 6.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/traffic_shaping.htm">http://www.shorewall.net/traffic_shaping.htm</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/traffic_shaping.htm">http://www.shorewall.net/traffic_shaping.htm</a></dl>
<dt> 7.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/MultiISP.html">http://www.shorewall.net/MultiISP.html</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/MultiISP.html">http://www.shorewall.net/MultiISP.html</a></dl>
<dt> 8.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/PacketMarking.html">http://www.shorewall.net/PacketMarking.html</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/PacketMarking.html">http://www.shorewall.net/PacketMarking.html</a></dl>
<dt> 9.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dl>
