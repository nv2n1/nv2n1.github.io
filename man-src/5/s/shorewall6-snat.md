---
title: "shorewall6-snat(5)"
name: "shorewall6-snat"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall6-snat/"
description: "snat – Shorewall6 SNAT/Masquerade definition file"
---

<p>snat &#8211; Shorewall6 SNAT/Masquerade definition file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall6/snat</code></dl>
<h2>Description</h2>
<dd>This file is used to define dynamic NAT (Masquerading) and to define Source NAT (SNAT). While still supported, its use is deprecated in favor of m[blue]<code>shorewall6-snat</code>m[]<font SIZE="-2">[1]</font>(5) which was introduced in Shorewall 5.0.14.</p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 The entries in this file are order-sensitive. The first entry that matches a particular connection will be the one that is used. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 If you have more than one ISP link, adding entries to this file will <code>not</code> force connections to go out through a particular link. You must use entries in m[blue]<code>shorewall6-rtrules</code>m[]<font SIZE="-2">[2]</font>(5) or PREROUTING entries in m[blue]<code>shorewall-tcrules</code>m[]<font SIZE="-2">[3]</font>(5) to do that.  The columns in the file are as follows. <code>ACTION</code></p>
<dl>
<dd>Defines the type of rule to generate. Choices are: <code>MASQUERADE</code>[+][([<i>lowport</i>&#8211;<i>highport</i>][<code>random</code>])]</p>
<dl>
<dd>Causes matching outgoing packages to have their source IP address set to the primary IP address of the interface specified in the DEST column. if <i>lowport</i>&#8211;<i>highport</i> is given, that port range will be used to assign a source port. If option <code>random</code> is used then port mapping will be randomized. MASQUERADE should only be used when the DEST interface has a dynamic IP address. Otherwise, SNAT should be used and should specify the interface&#8217;s static address.</dl>
<p> <code>SNAT</code>[+]([<i>address-or-address-range</i>][:<i>lowport</i><code>&#8211;</code><i>highport</i>][<code>:random</code>][:<code>persistent</code>]|<code>detect</code>|</p>
<dl>
<dd>If you specify an address here, matching packets will have their source address set to that address. If ADD_SNAT_ALIASES is set to Yes or yes in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[4]</font>(5) then Shorewall will automatically add this address to the INTERFACE named in the first column. You may also specify a range of up to 256 IP addresses if you want the SNAT address to be assigned from that range in a round-robin fashion by connection. The range is specified by <i>first.ip.in.range</i>&#8211;<i>last.ip.in.range</i>. You may follow the port range with<code> :random</code> in which case assignment of ports from the list will be random. <code>random</code> may also be specified by itself in this column in which case random local port assignments are made for the outgoing connections. Example: 206.124.146.177-206.124.146.180 You may follow the port range (or <code>:random</code>) with <code>:persistent</code>. This is only useful when an address range is specified and causes a client to be given the same source/destination IP pair. This feature replaces the SAME modifier which was removed from Shorewall in version 4.4.0. You may also use the special value <code>detect</code> which causes Shorewall to determine the IP addresses configured on the interface named in the DEST column and substitute them in this column. Finally, you may also specify a comma-separated list of ranges and/or addresses in this column. DNS Names names are not allowed. Normally, Netfilter will attempt to retain the source port number. You may cause netfilter to remap the source port by following an address or range (if any) by &quot;:&quot; and a port range with the format <i>lowport</i>&#8211;<i>highport</i>. If this is done, you must specify &quot;tcp&quot;, &quot;udp&quot;, &quot;dccp&quot; or &quot;stcp&quot; in the PROTO column. Example:</p>
<dl>
<dd>
<pre> [2001:470:a:787::2]:5000-6000</pre>
</dl>
</dl>
<p> CONTINUE[+]</p>
<dl>
<dd>Causes matching packets to be exempted from any following rules in the file.</dl>
<p> <i>action</i>[+][(<i>parameter</i>,&#8230;)]</p>
<dl>
<dd>where <i>action</i> is an action declared in m[blue]<code><a href="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5)</code>m[]<font SIZE="-2">[5]</font> with the <code>nat</code> option. See m[blue]<code><a rel="nofollow" href="http://www.shorewall.net">www.shorewall.net</a>/Actions.html</code>m[]<font SIZE="-2">[6]</font> for further information.</dl>
<p> Normally Masq/SNAT rules are evaluated after those for one-to-one NAT (defined in m[blue]<code>shorewall6-nat</code>m[]<font SIZE="-2">[7]</font>(5)). If you want the rule to be applied before one-to-one NAT rules, follow the action name with &quot;+&quot;: This feature should only be required if you need to insert rules in this file that preempt entries in m[blue]<code>shorewall6-nat</code>m[]<font SIZE="-2">[7]</font>(5).</dl>
<p> <code>SOURCE</code> (Optional) &#8211; [<i>interface</i>|<i>address</i>[<code>,</code><i>address</i>][<i>exclusion</i>]]</p>
<dl>
<dd>Set of hosts that you wish to SNAT; one or more host or network addresses separated by comma. You may use ipset names preceded by a plus sign (+) to specify a set of hosts.</dl>
<p> <code>DEST</code> &#8211; {<i>interface</i>|[<code>:</code>[<i>dest-address</i>[<code>,</code><i>dest-address</i>]&#8230;[<i>exclusion</i>]]|?COMMENT}</p>
<dl>
<dd>Outgoing <i>interface</i>. This is usually your internet interface. The <i>interface</i> must match an entry in m[blue]<code>shorewall6-interfaces</code>m[]<font SIZE="-2">[8]</font>(5). Shorewall allows loose matches to wildcard entries in m[blue]<code>shorewall6-interfaces</code>m[]<font SIZE="-2">[8]</font>(5). For example, ppp0 in this file will match a m[blue]<code>shorewall6-interfaces</code>m[]<font SIZE="-2">[8]</font>(5) entry that defines ppp+. Where m[blue]<code>more that one internet provider share a single interface</code>m[]<font SIZE="-2">[9]</font>, the provider is specified by including the provider name or number in parentheses:</p>
<dl>
<dd>
<pre> eth0(Avvanta)</pre>
</dl>
<p> In that case, you will want to specify the interface&#8217;s address for that provider as the SNAT parameter. The interface may be qualified by adding the character &quot;:&quot; followed by a comma-separated list of destination host or subnet addresses to indicate that you only want to change the source IP address for packets being sent to those particular destinations. Exclusion is allowed (see m[blue]<code>shorewall6-exclusion</code>m[]<font SIZE="-2">[10]</font>(5)) as are ipset names preceded by a plus sign &#8216;+&#8217;. Comments may be attached to Netfilter rules generated from entries in this file through the use of ?COMMENT lines. These lines begin with ?COMMENT; the remainder of the line is treated as a comment which is attached to subsequent rules until another ?COMMENT line is found or until the end of the file is reached. To stop adding comments to rules, use a line containing only ?COMMENT.</dl>
<p> <code>PROTO</code> (Optional) &#8211; {<code>&#8211;</code>|[!]{<i>protocol-name</i>|<i>protocol-number</i>}[,&#8230;]|+<i>ipset</i>}</p>
<dl>
<dd>If you wish to restrict this entry to a particular protocol then enter the protocol name (from <a href="/docs/linux/man/5-protocols/">protocols</a>(5)) or number here. Beginning with Shorewall 4.5.12, this column can accept a comma-separated list of protocols. Beginning with Shorewall 4.6.0, an <i>ipset</i> name can be specified in this column. This is intended to be used with bitmap:port ipsets.</dl>
<p> <code>DPORT</code> (Optional) &#8211; {-|[!]<i>port-name-or-number</i>[,<i>port-name-or-number</i>]&#8230;|+<i>ipset</i>}</p>
<dl>
<dd>If the PROTO column specifies TCP (6), UDP (17), DCCP (33), SCTP (132) or UDPLITE (136) then you may list one or more port numbers (or names from <a href="/docs/linux/man/5-services/">services</a>(5)) or port ranges separated by commas. Port ranges are of the form <i>lowport</i>:<i>highport</i>. Beginning with Shorewall 4.6.0, an <i>ipset</i> name can be specified in this column. This is intended to be used with bitmap:port ipsets.</dl>
<p> <code>IPSEC</code> (Optional) &#8211; [<i>option</i>[<code>,</code><i>option</i>]&#8230;]</p>
<dl>
<dd>If you specify a value other than &quot;-&quot; in this column, you must be running kernel 2.6 and your kernel and iptables must include policy match support. Comma-separated list of options from the following. Only packets that will be encrypted via an SA that matches these options will have their source address changed. <code>reqid=</code><i>number</i></p>
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
<dd>sets the MSS field in TCP packets</dl>
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
<p> <code>yes</code></p>
<dl>
<dd>When used by itself, causes all traffic that will be encrypted/encapsulated to match the rule.</dl>
</dl>
<p> <code>MARK</code> &#8211; [<code>!</code>]<i>value</i>[/<i>mask</i>][<code>:C</code>]</p>
<dl>
<dd>Defines a test on the existing packet or connection mark. The rule will match only if the test returns true. If you don&#8217;t want to define a test but need to specify anything in the following columns, place a &quot;-&quot; in this field. !</p>
<dl>
<dd>Inverts the test (not equal)</dl>
<p> <i>value</i></p>
<dl>
<dd>Value of the packet or connection mark.</dl>
<p> <i>mask</i></p>
<dl>
<dd>A mask to be applied to the mark before testing.</dl>
<p> <code>:C</code></p>
<dl>
<dd>Designates a connection mark. If omitted, the packet mark&#8217;s value is tested.</dl>
</dl>
<p> <code>USER</code> (Optional) &#8211; [<code>!</code>][<i>user-name-or-number</i>][<code>:</code><i>group-name-or-number</i>][<code>+</code><i>program-name</i>]</p>
<dl>
<dd>Only locally-generated connections will match if this column is non-empty. When this column is non-empty, the rule matches only if the program generating the output is running under the effective <i>user</i> and/or <i>group</i> specified (or is NOT running under that id if &quot;!&quot; is given). Examples: joe</p>
<dl>
<dd>program must be run by joe</dl>
<p> :kids</p>
<dl>
<dd>program must be run by a member of the &#8216;kids&#8217; group</dl>
<p> !:kids</p>
<dl>
<dd>program must not be run by a member of the &#8216;kids&#8217; group</dl>
<p> +upnpd</p>
<dl>
<dd>#program named upnpd</p>
<dl>
<dd><font SIZE="+1"> <code>Important</code> </font><br />
 The ability to specify a program name was removed from Netfilter in kernel version 2.6.14.  <code>SWITCH &#8211; [!]</code><i>switch-name</i><code>[={0|1}]</code></p>
<dl>
<dd>Added in Shorewall 4.5.1 and allows enabling and disabling the rule without requiring <code>shorewall restart</code>. The rule is enabled if the value stored in /proc/net/nf_condition/<i>switch-name</i> is 1. The rule is disabled if that file contains 0 (the default). If &#8216;!&#8217; is supplied, the test is inverted such that the rule is enabled if the file contains 0. Within the <i>switch-name</i>, &#8216;@0&#8217; and &#8216;@{0}&#8217; are replaced by the name of the chain to which the rule is a added. The <i>switch-name</i> (after &#8216;@&#8230;&#8217; expansion) must begin with a letter and be composed of letters, decimal digits, underscores or hyphens. Switch names must be 30 characters or less in length. Switches are normally <code>off</code>. To turn a switch <code>on</code>:</p>
<dl>
<dd><code>echo 1 &gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/proc/net/nf_condition/</code><i>switch-name</i></dl>
<p> To turn it <code>off</code> again:</p>
<dl>
<dd><code>echo 0 &gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/proc/net/nf_condition/</code><i>switch-name</i></dl>
<p> Switch settings are retained over <code>shorewall restart</code>. Beginning with Shorewall 4.5.10, when the <i>switch-name</i> is followed by <code>=0</code> or <code>=1</code>, then the switch is initialized to off or on respectively by the <code>start</code> command. Other commands do not affect the switch setting.</dl>
<p> <code>ORIGDEST</code> &#8211; [<code>&#8211;</code>|<i>address</i>[,<i>address</i>]&#8230;[<i>exclusion</i>]|<i>exclusion</i>]</p>
<dl>
<dd>(Optional) This column may be included and may contain one or more addresses (host or network) separated by commas. Address ranges are not allowed. When this column is supplied, rules are generated that require that the original destination address matches one of the listed addresses. It is useful for specifying that SNAT should occur only for connections that were acted on by a DNAT when they entered the firewall. This column was formerly labelled ORIGINAL DEST.</dl>
<p> <code>PROBABILITY</code> &#8211; [<i>probability</i>]</p>
<dl>
<dd>Added in Shorewall 5.0.0. When non-empty, requires the Statistics Match capability in your kernel and ip6tables and causes the rule to match randomly but with the given <i>probability</i>. The <i>probability</i> is a number 0 &lt; <i>probability</i> &lt;= 1 and may be expressed at up to 8 decimal points of precision.</dl>
<h2>Examples</h2>
<p>Example 1:</p>
<dl>
<dd>You have a simple &#8216;masquerading&#8217; setup where eth0 connects to a DSL or cable modem and eth1 connects to your local network with subnet 2001:470:b:787::0/64 </p>
<p> Your entry in the file will be: </p>
<dl>
<dd>
<pre> #ACTION SOURCE DEST
 MASQUERADE 2001:470:b:787::0/64 eth0</pre>
</dl>
</dl>
<p> Example 2:</p>
<dl>
<dd>Your sit1 interface has two public IP addresses: 2001:470:a:227::1 and 2001:470:b:227::1. You want to use the iptables statistics match to masquerade outgoing connections evenly between these two addresses. </p>
<dl>
<dd>
<pre>/etc/shorewall/snat:
 #ACTION SOURCE DEST
 SNAT(2001:470:a:227::1) ::/0 sit1 { probability=0.50 }
 SNAT(2001:470:a:227::2) ::/0 sit</pre>
</dl>
</dl>
<h2>Files</h2>
<p>/etc/shorewall6/snat</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall6-snat</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netshorewall6-snat.html">http://www.shorewall.netshorewall6-snat.html</a></dl>
<dt> 2.</p>
<dd>shorewall6-rtrules</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-rtrules.html">http://www.shorewall.net/manpages6/shorewall6-rtrules.html</a></dl>
<dt> 3.</p>
<dd>shorewall-tcrules</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-tcrules.html">http://www.shorewall.net/manpages6/shorewall6-tcrules.html</a></dl>
<dt> 4.</p>
<dd>shorewall6.conf</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netshorewall6.conf.html">http://www.shorewall.netshorewall6.conf.html</a></dl>
<dt> 5.</p>
<dd><a href="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5)</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netshorewall6-actions.html">http://www.shorewall.netshorewall6-actions.html</a></dl>
<dt> 6.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net">www.shorewall.net</a>/Actions.html</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/Actions.html">http://www.shorewall.net/Actions.html</a></dl>
<dt> 7.</p>
<dd>shorewall6-nat</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-nat.html">http://www.shorewall.net/manpages6/shorewall6-nat.html</a></dl>
<dt> 8.</p>
<dd>shorewall6-interfaces</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-interfaces.html">http://www.shorewall.net/manpages6/shorewall6-interfaces.html</a></dl>
<dt> 9.</p>
<dd>more that one internet provider share a single interface</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/4.4/MultiISP.html#Shared">http://www.shorewall.net/4.4/MultiISP.html#Shared</a></dl>
<dt>10.</p>
<dd>shorewall6-exclusion</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-exclusion.html">http://www.shorewall.net/manpages6/shorewall6-exclusion.html</a></dl>
