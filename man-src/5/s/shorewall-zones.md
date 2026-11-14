---
title: "shorewall-zones(5)"
name: "shorewall-zones"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-zones/"
description: "zones – Shorewall zone declaration file"
---

<p>zones &#8211; Shorewall zone declaration file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/zones</code></dl>
<h2>Description</h2>
<dd>The /etc/shorewall/zones file declares your network zones. You specify the hosts in each zone through entries in /etc/shorewall/interfaces or /etc/shorewall/hosts. </p>
<p> The columns in the file are as follows (where the column name is followed by a different name in parentheses, the different name is used in the alternate specification syntax). </p>
<p> <code>ZONE</code> &#8211; <i>zone</i>[<code>:</code><i>parent-zone</i>[<code>,</code><i>parent-zone</i>]&#8230;]</p>
<dl>
<dd>Name of the <i>zone</i>. Must start with a letter and consist of letters, digits or &#8216;_&#8217;. The names &quot;all&quot;, &quot;none&quot;, &quot;any&quot;, &quot;SOURCE&quot; and &quot;DEST&quot; are reserved and may not be used as zone names. The maximum length of a zone name is determined by the setting of the LOGFORMAT option in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[1]</font>(5). With the default LOGFORMAT, zone names can be at most 5 characters long. The maximum length of an iptables log prefix is 29 bytes. As explained in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[1]</font> (5), the default LOGPREFIX formatting string is &#8220;Shorewall:%s:%s:&#8221; where the first %s is replaced by the chain name and the second is replaced by the disposition. </p>
<dl>
<dd>&bull; The default formatting string has 12 fixed characters (&quot;Shorewall&quot; and three colons).</dl>
<dl>
<dd>&bull; The longest of the standard dispositions are ACCEPT and REJECT which have 6 characters each.</dl>
<dl>
<dd>&bull; The canonical name for the chain containing the rules for traffic going from zone 1 to zone 2 is &quot;&lt;zone 1&gt;2&lt;zone 2&gt;&quot; or &quot;&lt;zone 1&gt;-&lt;zone 2&gt;&quot;.</dl>
<dl>
<dd>&bull; So if M is the maximum zone name length, such chains can have length 2*M + 1.</p>
<dl>
<dd>12 + 6 + 2*M + 1 = 29 which reduces to</dl>
<dl>
<dd>2*M = 29 &#8211; 12 &#8211; 6 &#8211; 1 = 10 or</dl>
<dl>
<dd>M = 5</dl>
</dl>
<p> The order in which Shorewall matches addresses from packets to zones is determined by the order of zone declarations. Where a zone is nested in one or more other zones, you may either ensure that the nested zone precedes its parents in this file, or you may follow the (sub)zone name by &quot;:&quot; and a comma-separated list of the parent zones. The parent zones must have been declared in earlier records in this file. See m[blue]<code>shorewall-nesting</code>m[]<font SIZE="-2">[2]</font>(5) for additional information. </p>
<p> Example: </p>
<dl>
<dd>
<pre>#ZONE TYPE OPTIONS IN OPTIONS OUT OPTIONS
a ipv4
b ipv4
c:a,b ipv4</pre>
</dl>
<p> Currently, Shorewall uses this information to reorder the zone list so that parent zones appear after their subzones in the list. The IMPLICIT_CONTINUE option in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[1]</font>(5) can also create implicit CONTINUE policies to/from the subzone. </p>
<p> Where an <code>ipsec</code> zone is explicitly included as a child of an <code>ipv4</code> zone, the ruleset allows CONTINUE policies (explicit or implicit) to work as expected. </p>
<p> In the future, Shorewall may make additional use of nesting information.</dl>
<p> <code>TYPE</code></p>
<dl>
<dd><code>ipv4</code></p>
<dl>
<dd>This is the standard Shorewall zone type and is the default if you leave this column empty or if you enter &quot;-&quot; in the column. Communication with some zone hosts may be encrypted. Encrypted hosts are designated using the &#8216;ipsec&#8217; option in m[blue]<code>shorewall-hosts</code>m[]<font SIZE="-2">[3]</font>(5).</dl>
<p> <code>ipsec</code> (or <code>ipsec4</code>)</p>
<dl>
<dd>Communication with all zone hosts is encrypted. Your kernel and iptables must include policy match support.</dl>
<p> <code>firewall</code></p>
<dl>
<dd>Designates the firewall itself. You must have exactly one &#8216;firewall&#8217; zone. No options are permitted with a &#8216;firewall&#8217; zone. The name that you enter in the ZONE column will be stored in the shell variable $FW which you may use in other configuration files to designate the firewall zone.</dl>
<p> <code>bport</code> (or <code>bport4</code>)</p>
<dl>
<dd>The zone is associated with one or more ports on a single bridge.</dl>
<p> <code>vserver</code></p>
<dl>
<dd>Added in Shorewall 4.4.11 Beta 2 &#8211; A zone composed of Linux-vserver guests. The zone contents must be defined in m[blue]<code>shorewall-hosts</code>m[]<font SIZE="-2">[3]</font> (5). </p>
<p> Vserver zones are implicitly handled as subzones of the firewall zone.</dl>
<p> <code>loopback</code></p>
<dl>
<dd>Added in Shorewall 4.5.17. </p>
<p> Normally, Shorewall treats the loopback interface (lo) in the following way: </p>
<dl>
<dd>&bull; By default, all traffic through the interface is ACCEPTed.</dl>
<dl>
<dd>&bull; If a $FW -&gt; $FW policy is defined or $FW -&gt; $FW rules are defined, they are placed in a chain named ${FW}2${F2} or ${FW}-${FW} (e.g., &#8216;fw2fw&#8217; or &#8216;fw-fw&#8217; ) depending on the ZONE2ZONE setting in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[1]</font>(5).</dl>
<dl>
<dd>&bull; $FW -&gt; $FW traffic is only filtered in the OUTPUT chain.</dl>
<p> By defining a <code>loopback</code> zone and associating it with the loopback interface in <a href="/docs/linux/man/5-shorewall-interfaces/">shorewall-interfaces</a>(5), you can effect a slightly different model. Suppose that the <code>loopback</code> zone name is &#8216;local&#8217;; then: </p>
<dl>
<dd>&bull; Both $FW -&gt; local and local -&gt; $FW chains are created.</dl>
<dl>
<dd>&bull; The $FW -&gt; local and local -&gt; $FW policies may be different.</dl>
<dl>
<dd>&bull; Both $FW -&gt; local and local -&gt; $FW rules may be specified.</dl>
<p> Rules to/from the <code>loopback</code> zone and any zone other than the firewall zone are ignored with a warning. </p>
<p> <code>loopback</code> zones may be nested within other <code>loopback</code> zones.</dl>
<p> local</p>
<dl>
<dd>Added in Shorewall 4.5.17. <code>local</code> is the same as <code>ipv4</code> with the exception that the zone is only accessible from the <code>firewall</code> and <code>vserver</code> zones.</dl>
</dl>
<p> <code>OPTIONS, IN OPTIONS and OUT OPTIONS</code> (options, in_options, out_options) &#8211; [<i>option</i>[<code>,</code><i>option</i>]&#8230;]</p>
<dl>
<dd>A comma-separated list of options. With the exception of the <code>mss</code> and <code>blacklist</code> options, these only apply to TYPE <code>ipsec</code> zones. </p>
<p> <code>dynamic_shared</code></p>
<dl>
<dd>Added in Shorewall 4.5.9. May only be specified in the OPTIONS column and indicates that only a single ipset should be created for this zone if it has multiple dynamic entries in m[blue]<code>shorewall-hosts</code>m[]<font SIZE="-2">[3]</font>(5). Without this option, a separate ipset is created for each interface.</dl>
<p> <code>reqid=</code><i>number</i></p>
<dl>
<dd>where <i>number</i> is specified using <a href="/docs/linux/man/8-setkey/">setkey</a>(8) using the &#8216;unique:<i>number</i> option for the SPD level.</dl>
<p> <code>spi=</code>&lt;number&gt;</p>
<dl>
<dd>where <i>number</i> is the SPI of the SA used to encrypt/decrypt packets.</dl>
<p> <code>proto=</code><code>ah</code>|<code>esp</code>|<code>ipcomp</code></p>
<dl>
<dd>IPSEC Encapsulation Protocol</dl>
<p> <code>mss=</code><i>number</i></p>
<dl>
<dd>sets the MSS field in TCP packets. If you supply this option, you should also set FASTACCEPT=No in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[1]</font>(5) to insure that both the SYN and SYN,ACK packets have their MSS field adjusted.</dl>
<p> <code>mode=</code><code>transport</code>|<code>tunnel</code></p>
<dl>
<dd>IPSEC mode</dl>
<p> <code>tunnel-src=</code><i>address</i>[/<i>mask</i>]</p>
<dl>
<dd>only available with mode=tunnel</dl>
<p> <code>tunnel-dst=</code><i>address</i>[/<i>mask</i>]</p>
<dl>
<dd>only available with mode=tunnel</dl>
<p> <code>strict</code></p>
<dl>
<dd>Means that packets must match all rules.</dl>
<p> <code>next</code></p>
<dl>
<dd>Separates rules; can only be used with strict</dl>
<p> The options in the OPTIONS column are applied to both incoming and outgoing traffic. The IN OPTIONS are applied to incoming traffic (in addition to OPTIONS) and the OUT OPTIONS are applied to outgoing traffic. </p>
<p> If you wish to leave a column empty but need to make an entry in a following column, use &quot;-&quot;.</dl>
<h2>Files</h2>
<p>/etc/shorewall/zones</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/Multiple_Zones.html">http://www.shorewall.net/Multiple_Zones.html</a></code>m[]<font SIZE="-2">[4]</font>. </p>
<p> m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[]<font SIZE="-2">[5]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall_interfaces/">shorewall_interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/8-shorewall-nesting/">shorewall-nesting</a>(8), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-rtrules/">shorewall-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-secmarks/">shorewall-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-mangle/">shorewall-mangle</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall.conf</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall.conf.html">http://www.shorewall.net/manpages/shorewall.conf.html</a></dl>
<dt> 2.</p>
<dd>shorewall-nesting</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-nesting.html">http://www.shorewall.net/manpages/shorewall-nesting.html</a></dl>
<dt> 3.</p>
<dd>shorewall-hosts</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-hosts.html">http://www.shorewall.net/manpages/shorewall-hosts.html</a></dl>
<dt> 4.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/Multiple_Zones.html">http://www.shorewall.net/Multiple_Zones.html</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/Multiple_Zones.html">http://www.shorewall.net/Multiple_Zones.html</a></dl>
<dt> 5.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dl>
