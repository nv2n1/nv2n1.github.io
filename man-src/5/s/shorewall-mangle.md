---
title: "shorewall-mangle(5)"
name: "shorewall-mangle"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-mangle/"
description: "mangle – Shorewall Packet marking/mangling rules file"
---

<p>mangle &#8211; Shorewall Packet marking/mangling rules file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/mangle</code></dl>
<h2>Description</h2>
<dd>This file was introduced in Shorewall 4.6.0 and is intended to replace m[blue]<code><a href="/docs/linux/man/5-shorewall-tcrules/">shorewall-tcrules</a>(5)</code>m[]<font SIZE="-2">[1]</font>. This file is only processed by the compiler if:</p>
<dl>
<dd>1. No file named &#8216;tcrules&#8217; exists on the current CONFIG_PATH (see m[blue]<code><a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5)</code>m[]<font SIZE="-2">[2]</font>); or</dl>
<dl>
<dd>2. The first file named &#8216;tcrules&#8217; found on the CONFIG_PATH contains no non-commentary entries.</dl>
<p> Entries in this file cause packets to be marked as a means of classifying them for traffic control or policy routing.</p>
<dl>
<dd><font SIZE="+1"> <code>Important</code> </font><br />
 Unlike rules in the m[blue]<code>shorewall-rules</code>m[]<font SIZE="-2">[3]</font>(5) file, evaluation of rules in this file will continue after a match. So the final mark for each packet will be the one assigned by the LAST tcrule that matches. If you use multiple internet providers with the &#8216;track&#8217; option, in /etc/shorewall/providers be sure to read the restrictions at m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/MultiISP.html">http://www.shorewall.net/MultiISP.html</a></code>m[]<font SIZE="-2">[4]</font>.  The columns in the file are as follows (where the column name is followed by a different name in parentheses, the different name is used in the alternate specification syntax). <code>ACTION</code> &#8211; <i>command</i>[(<i>parameters</i>)][:<i>chain-designator</i>]</p>
<dl>
<dd>The <i>chain-designator </i>indicates the Netfilter chain that the entry applies to and may be one of the following: P</p>
<dl>
<dd>PREROUTING chain.</dl>
<p> F</p>
<dl>
<dd>FORWARD chain.</dl>
<p> T</p>
<dl>
<dd>POSTROUTING chain.</dl>
<p> I</p>
<dl>
<dd>INPUT chain.</dl>
<p> Unless otherwise specified for the particular <i>command</i>, the default chain is PREROUTING when MARK_IN_FORWARD_CHAIN=No in m[blue]<code><a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5)</code>m[]<font SIZE="-2">[2]</font>, and FORWARD when MARK_IN_FORWARD_CHAIN=Yes. A <i>chain-designator</i> may not be specified if the SOURCE or DEST columns begin with &#8216;$FW&#8217;. When the SOURCE is $FW, the generated rule is always placed in the OUTPUT chain. If DEST is &#8216;$FW&#8217;, then the rule is placed in the INPUT chain. Additionally, a <i>chain-designator</i> may not be specified in an action body unless the action is declared as <code>inline</code> in m[blue]<code>shorewall-actions</code>m[]<font SIZE="-2">[5]</font>(5). Where a command takes parameters, those parameters are enclosed in parentheses (&quot;(&#8230;.)&quot;) and separated by commas. The <i>command</i> may be one of the following. <i>action</i><code>[([</code><i>param</i><code>[,&#8230;])]</code></p>
<dl>
<dd>Added in Shorewall 5.0.7. <i>action</i> must be an action declared with the <code>mangle</code> option in m[blue]<code><a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5)</code>m[]<font SIZE="-2">[6]</font>. If the action accepts parameters, they are specified as a comma-separated list within parentheses following the <i>action</i> name.</dl>
<p> <code>ADD(</code><i>ipset</i><code>:</code><i>flags</i><code>)</code></p>
<dl>
<dd>Added in Shorewall 4.6.7. Causes addresses and/or port numbers to be added to the named <i>ipset</i>. The <i>flags</i> specify the address or tuple to be added to the set and must match the type of ipset involved. For example, for an iphash ipset, either the SOURCE or DESTINATION address can be added using <i>flags</i><code>src</code> or <code>dst</code> respectively (see the -A command in ipset (8)). ADD is non-terminating. Even if a packet matches the rule, it is passed on to the next rule.</dl>
<p> <code>CHECKSUM</code></p>
<dl>
<dd>Compute and fill in the checksum in a packet that lacks a checksum. This is particularly useful if you need to work around old applications, such as dhcp clients, that do not work well with checksum offloads, but you don&#8217;t want to disable checksum offload in your device. Requires &#8216;Checksum Target&#8217; support in your kernel and iptables.</dl>
<p> <code>CLASSIFY(</code><i>classid</i><code>)</code></p>
<dl>
<dd>A classification Id (classid) is of the form <i>major</i>:<i>minor</i> where <i>major</i> and <i>minor</i> are integers. Corresponds to the &#8216;class&#8217; specification in these traffic shaping modules:</p>
<dl>
<dd>
<pre> atm
 cbq
 dsmark
 pfifo_fast
 htb
 prio</pre>
</dl>
<p> Classification occurs in the POSTROUTING chain except when the <code>SOURCE</code> is <code>$FW</code>[:<i>address</i>] in which case classification occurs in the OUTPUT chain. When using Shorewall&#8217;s built-in traffic shaping tool, the <i>major</i> class is the device number (the first device in m[blue]<code>shorewall-tcdevices</code>m[]<font SIZE="-2">[7]</font>(5) is major class 1, the second device is major class 2, and so on) and the <i>minor</i> class is the class&#8217;s MARK value in m[blue]<code>shorewall-tcclasses</code>m[]<font SIZE="-2">[8]</font>(5) preceded by the number 1 (MARK 1 corresponds to minor class 11, MARK 5 corresponds to minor class 15, MARK 22 corresponds to minor class 122, etc.).</dl>
<p> <code>?COMMENT</code></p>
<dl>
<dd>The rest of the line will be attached as a comment to the Netfilter rule(s) generated by the following entries. The comment will appear delimited by &quot;/* &#8230; */&quot; in the output of <code>shorewall show mangle</code> To stop the comment from being attached to further rules, simply include ?COMMENT on a line by itself.</dl>
<p> <code>CONMARK({mark|range})</code></p>
<dl>
<dd>Identical to MARK with the exception that the mark is assigned to connection to which the packet belongs is marked rather than to the packet itself.</dl>
<p> <code>CONTINUE</code></p>
<dl>
<dd>Don&#8217;t process any more marking rules in the table. Currently, CONTINUE may not be used with <i>exclusion</i> (see the SOURCE and DEST columns below); that restriction will be removed when iptables/Netfilter provides the necessary support.</dl>
<p> <code>DEL(</code><i>ipset</i><code>:</code><i>flags</i><code>)</code></p>
<dl>
<dd>Added in Shorewall 4.6.7. Causes an entry to be deleted from the named <i>ipset</i>. The <i>flags</i> specify the address or tuple to be deleted from the set and must match the type of ipset involved. For example, for an iphash ipset, either the SOURCE or DESTINATION address can be deleted using <i>flags</i><code>src</code> or <code>dst</code> respectively (see the -D command in ipset (8)). DEL is non-terminating. Even if a packet matches the rule, it is passed on to the next rule.</dl>
<p> <code>DIVERT</code></p>
<dl>
<dd>Two DIVERT rule should precede the TPROXY rule and should select DEST PORT tcp 80 and SOURCE PORT tcp 80 respectively (assuming that tcp port 80 is being proxied). DIVERT avoids sending packets to the TPROXY target once a socket connection to Squid3 has been established by TPROXY. DIVERT marks the packet with a unique mark and exempts it from any rules that follow.</dl>
<p> <code>DIVERTHA</code></p>
<dl>
<dd>Added in Shorewall 5.0.4. To setup the HAProxy configuration described at m[blue]<code><a rel="nofollow" href="http://www.loadbalancer.org/blog/setting-up-haproxy-with-transparent-mode-on-centos-6-x">http://www.loadbalancer.org/blog/setting-up-haproxy-with-transparent-mode-on-centos-6-x</a></code>m[], place this entry in m[blue]<code><a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5)</code>m[]<font SIZE="-2">[9]</font>:</p>
<dl>
<dd>
<pre>#NAME NUMBER MARK DUPLICATE INTERFACE GATEWAY OPTIONS COPY
TProxy 1 - - lo - tproxy</pre>
</dl>
<p> and use this DIVERTHA entry:</p>
<dl>
<dd>
<pre>#ACTION SOURCE DEST PROTO DPORT SPORT USER TEST LENGTH TOS CONNBYTES HELPER PROBABILITY DSCP
DIVERTHA - - tcp</pre>
</dl>
</dl>
<p> <code>DROP</code></p>
<dl>
<dd>Causes matching packets to be discarded.</dl>
<p> <code>DSCP</code>(<i>dscp</i>)</p>
<dl>
<dd>Sets the Differentiated Services Code Point field in the IP header. The <i>dscp</i> value may be given as an even number (hex or decimal) or as the name of a DSCP class. Valid class names and their associated hex numeric values are:</p>
<dl>
<dd>
<pre> CS0 =&gt; 0x00
 CS1 =&gt; 0x08
 CS2 =&gt; 0x10
 CS3 =&gt; 0x18
 CS4 =&gt; 0x20
 CS5 =&gt; 0x28
 CS6 =&gt; 0x30
 CS7 =&gt; 0x38
 BE =&gt; 0x00
 AF11 =&gt; 0x0a
 AF12 =&gt; 0x0c
 AF13 =&gt; 0x0e
 AF21 =&gt; 0x12
 AF22 =&gt; 0x14
 AF23 =&gt; 0x16
 AF31 =&gt; 0x1a
 AF32 =&gt; 0x1c
 AF33 =&gt; 0x1e
 AF41 =&gt; 0x22
 AF42 =&gt; 0x24
 AF43 =&gt; 0x26
 EF =&gt; 0x2e</pre>
</dl>
<p> To indicate more than one class, add their hex values together and specify the result. By default, DSCP rules are placed in the POSTROUTING chain.</dl>
<p> <code>ECN</code></p>
<dl>
<dd>Added in Shorewall 5.0.6 as an alternative to entries in m[blue]<code><a href="/docs/linux/man/5-shorewall-ecn/">shorewall-ecn</a>(5)</code>m[]<font SIZE="-2">[10]</font>. If a PROTO is specified, it must be &#8216;tcp&#8217; (6). If no PROTO is supplied, TCP is assumed. This action causes all ECN bits in the TCP header to be cleared.</dl>
<p> <code>IMQ</code>(<i>number</i>)</p>
<dl>
<dd>Specifies that the packet should be passed to the IMQ identified by <i>number</i>. Requires IMQ Target support in your kernel and iptables.</dl>
<p> <code>INLINE</code>[(<i>action</i>)]</p>
<dl>
<dd>Allows you to place your own ip[6]tables matches at the end of the line following a semicolon (&quot;;&quot;). If an <i>action</i> is specified, the compiler proceeds as if that <i>action</i> had been specified in this column. If no action is specified, then you may include your own jump (&quot;-j <i>target</i> [<i>option</i>] &#8230;&quot;) after any matches specified at the end of the rule. If the target is not one known to Shorewall, then it must be defined as a builtin action in m[blue]<code>shorewall-actions</code>m[]<font SIZE="-2">[11]</font> (5). The following rules are equivalent:</p>
<dl>
<dd>
<pre>2:P eth0 - tcp 22
INLINE(<a href="//www.systutorials.com/docs/linux/man/2-MARK/">MARK</a>(2)):P eth0 - tcp 22
INLINE(<a href="//www.systutorials.com/docs/linux/man/2-MARK/">MARK</a>(2)):P eth0 - ; -p tcp
INLINE eth0 - tcp 22 ; -j MARK --set-mark 2
INLINE eth0 - ; -p tcp -j MARK --set-mark 2</pre>
</dl>
<p> If INLINE_MATCHES=Yes in m[blue]<code><a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5)</code>m[]<font SIZE="-2">[2]</font> then the third rule above can be specified as follows:</p>
<dl>
<dd>
<pre><a href="//www.systutorials.com/docs/linux/man/2-MARK/">MARK</a>(2):P eth0 - ; -p tcp</pre>
</dl>
<p> Beginning with Shorewall 5.0.0, the rule may also be written this way, irrespective of the setting of INLINE_MATCHES:</p>
<dl>
<dd>
<pre><a href="//www.systutorials.com/docs/linux/man/2-MARK/">MARK</a>(2):P eth0 - ;; -p tcp</pre>
</dl>
</dl>
<p> <code>IPMARK</code></p>
<dl>
<dd>Assigns a mark to each matching packet based on the either the source or destination IP address. By default, it assigns a mark value equal to the low-order 8 bits of the source address. Default values are:</p>
<dl>
<dd>src</dl>
<dl>
<dd><i>mask1</i> = 0xFF</dl>
<dl>
<dd><i>mask2</i> = 0x00</dl>
<dl>
<dd><i>shift</i> = 0</dl>
<p> &#8216;src&#8217; and &#8216;dst&#8217; specify whether the mark is to be based on the source or destination address respectively. The selected address is first shifted to the right by <i>shift</i> bits. The result is then LANDed with <i>mask1</i> then LORed with <i>ma</i><i>s</i><i>k2</i>. In a sense, the IPMARK target is more like an IPCLASSIFY target in that the mark value is later interpreted as a class ID. A packet mark is 32 bits wide; so is a class ID. The &lt;major&gt; class occupies the high-order 16 bits and the &lt;minor&gt; class occupies the low-order 16 bits. So the class ID 1:4ff (remember that class IDs are always in hex) is equivalent to a mark value of 0x104ff. Remember that Shorewall uses the interface number as the &lt;major&gt; number where the first interface in tcdevices has &lt;major&gt; number 1, the second has &lt;major&gt; number 2, and so on. The IPMARK target assigns a mark to each matching packet based on the either the source or destination IP address. By default, it assigns a mark value equal to the low-order 8 bits of the source address. The syntax is as follows: <code>IPMARK</code>[([{<code>src</code>|<code>dst</code>}][,[<i>mask1</i>][,[<i>mask2</i>][,[<i>shift</i>]]]])] Default values are:</p>
<dl>
<dd><code>src</code></dl>
<dl>
<dd><i>mask1</i> = 0xFF</dl>
<dl>
<dd><i>mask2</i> = 0x00</dl>
<dl>
<dd><i>shift</i> = 0</dl>
<p> <code>src</code> and <code>dst</code> specify whether the mark is to be based on the source or destination address respectively. The selected address is first shifted right by <i>shift</i>, then LANDed with <i>mask1</i> and then LORed with <i>mask2</i>. The <i>shift</i> argument is intended to be used primarily with IPv6 addresses. Example: IPMARK(src,0xff,0x10100)</p>
<dl>
<dd>Suppose that the source IP address is 192.168.4.3<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>0xc0a80403;&nbsp;<wbr>then</dl>
<dl>
<dd>0xc0a80403 &gt;&gt; 0 = 0xc0a80403</dl>
<dl>
<dd>0xc0a80403 LAND 0xFF = 0x03</dl>
<dl>
<dd>0x03 LOR 0x10100 = 0x10103 or class ID<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1:103</dl>
<p> It is important to realize that, while class IDs are composed of a <i>major</i> and a <i>minor</i> value, the set of values must be unique. That is, the same numeric value cannot be used as both a <i>major</i> and a <i>minor</i> number for the same interface unless class nesting occurs (which is not currently possible with Shorewall). You should keep this in mind when deciding how to map IP addresses to class IDs. For example, suppose that your internal network is 192.168.1.0/29 (host IP addresses 192.168.1.1 &#8211; 192.168.1.6). Your first notion might be to use IPMARK(src,0xFF,0x10000) so as to produce class IDs 1:1 through 1:6. But 1:1 is an invalid class ID since the <i>major</i> and <i>minor</i> classes are equal. So you might choose instead to use IPMARK(src,0xFF,0x10100) as in the example above so that all of your <i>minor</i> classes will have a value &gt; 256.</dl>
<p> <code>IPTABLES({</code><i>target</i><code> [</code><i>option</i><code> &#8230;])</code></p>
<dl>
<dd>This action allows you to specify an iptables target with options (e.g., &#8216;IPTABLES(MARK &#8211;set-xmark 0x01/0xff)&#8217;. If the target is not one recognized by Shorewall, the following error message will be issued:</p>
<dl>
<dd>ERROR: Unknown target<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(<i>target</i>)</dl>
<p> This error message may be eliminated by adding the <i>target</i> as a builtin action in m[blue]<code><a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5)</code>m[]<font SIZE="-2">[11]</font>.</dl>
<p> <code>MARK({</code><i>mark</i><code>|</code><i>range</i><code>})</code></p>
<dl>
<dd>where <i>mark</i> is a packet mark value. Normally will set the mark value. If preceded by a vertical bar (&quot;|&quot;), the mark value will be logically ORed with the current mark value to produce a new mark value. If preceded by an ampersand (&quot;&amp;&quot;), will be logically ANDed with the current mark value to produce a new mark value. Both &quot;|&quot; and &quot;&amp;&quot; require Extended MARK Target support in your kernel and iptables. The mark value may be optionally followed by &quot;/&quot; and a mask value (used to determine those bits of the connection mark to actually be set). When a mask is specified, the result of logically ANDing the mark value with the mask must be the same as the mark value. A mark <i>range</i> is a pair of integers separated by a dash (&quot;-&quot;). May be optionally followed by a slash (&quot;/&quot;) and a mask and requires the Statistics Match capability in iptables and kernel. Marks in the specified range are assigned to packets on a round-robin fashion. When a mask is specified, the result of logically ANDing each mark value with the mask must be the same as the mark value. The least significant bit in the mask is used as an increment. For example, if &#8216;0x200-0x400/0xff00&#8217; is specified, then the assigned mark values are 0x200, 0x300 and 0x400 in equal proportions. If no mask is specified, then ( 2 ** MASK_BITS ) &#8211; 1 is assumed (MASK_BITS is set in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font>(5)).</dl>
<p> <code>NFLOG</code>[(<i>nflog-parameters</i>)]</p>
<dl>
<dd>Added in Shorewall 5.0.9. Logs matching packets using NFLOG. The <i>nflog-parameters</i> are a comma-separated list of up to 3 numbers:</p>
<dl>
<dd>&bull; The first number specifies the netlink group (0-65535). If omitted (e.g., NFLOG(,0,10)) then a value of 0 is assumed.</dl>
<dl>
<dd>&bull; The second number specifies the maximum number of bytes to copy. If omitted, 0 (no limit) is assumed.</dl>
<dl>
<dd>&bull; The third number specifies the number of log messages that should be buffered in the kernel before they are sent to user space. The default is 1.</dl>
</dl>
<p> <code>RESTORE</code>[(<i>mask</i>)]</p>
<dl>
<dd>Restore the packet&#8217;s mark from the connection&#8217;s mark using the supplied mask if any. Your kernel and iptables must include CONNMARK support.</dl>
<p> <code>SAME[(</code><i>timeout</i><code>)]</code></p>
<dl>
<dd>Some websites run applications that require multiple connections from a client browser. Where multiple &#8216;balanced&#8217; providers are configured, this can lead to problems when some of the connections are routed through one provider and some through another. The SAME target allows you to work around that problem. SAME may be used in the PREROUTING and OUTPUT chains. When used in PREROUTING, it causes matching connections from an individual local system to all use the same provider. For example:</p>
<dl>
<dd>
<pre>#ACTION SOURCE DEST PROTO DPORT
SAME:P 192.168.1.0/24 0.0.0.0/0 tcp 80,443</pre>
</dl>
<p> If a host in 192.168.1.0/24 attempts a connection on TCP port 80 or 443 and it has sent a packet on either of those ports in the last five minutes then the new connection will use the same provider as the connection over which that last packet was sent. When used in the OUTPUT chain, it causes all matching connections to an individual remote system to all use the same provider. For example:</p>
<dl>
<dd>
<pre>#ACTION SOURCE DEST PROTO DPORT
SAME $FW 0.0.0.0/0 tcp 80,443</pre>
</dl>
<p> The optional <i>timeout</i> parameter was added in Shorewall 4.6.7 and specifies a number of seconds . When not specified, a value of 300 seconds (5 minutes) is assumed. If the firewall attempts a connection on TCP port 80 or 443 and it has sent a packet on either of those ports in the last <i>timeout</i> seconds to the same remote system then the new connection will use the same provider as the connection over which that last packet was sent.</dl>
<p> <code>SAVE[(</code><i>mask</i><i>)</i><code>] </code></p>
<dl>
<dd>Save the packet&#8217;s mark to the connection&#8217;s mark using the supplied mask if any. Your kernel and iptables must include CONNMARK support.</dl>
<p> <code>TOS</code>(<i>tos</i>[/<i>mask</i>])</p>
<dl>
<dd>Sets the Type of Service field in the IP header. The <i>tos</i> value may be given as an number (hex or decimal) or as the name of a TOS type. Valid type names and their associated hex numeric values are:</p>
<dl>
<dd>
<pre>Minimize-Delay =&gt; 0x10,
Maximize-Throughput =&gt; 0x08,
Maximize-Reliability =&gt; 0x04,
Minimize-Cost =&gt; 0x02,
Normal-Service =&gt; 0x00</pre>
</dl>
<p> To indicate more than one class, add their hex values together and specify the result. When <i>tos</i> is given as a number, it may be optionally followed by &#8216;/&#8217; and a <i>mask</i>. When no <i>mask</i> is given, the value 0xff is assumed. When <i>tos</i> is given as a type name, the <i>mask</i> 0x3f is assumed. The action performed is to zero out the bits specified by the <i>mask</i>, then set the bits specified by <i>tos</i>.</dl>
<p> <code>TPROXY</code>([<i>port</i>][,<i>address</i>])</p>
<dl>
<dd>Transparently redirects a packet without altering the IP header. Requires a tproxy provider to be defined in m[blue]<code>shorewall-providers</code>m[]<font SIZE="-2">[12]</font>(5). There are three parameters to TPROXY &#8211; neither is required:</p>
<dl>
<dd>&bull; <i>port</i> &#8211; the port on which the proxy server is listening. If omitted, the original destination port.</dl>
<dl>
<dd>&bull; <i>address</i> &#8211; a local (to the firewall) IP address on which the proxy server is listening. If omitted, the IP address of the interface on which the request arrives.</dl>
</dl>
<p> <code>TTL</code>([<code>&#8211;</code>|<code>+</code>]<i>number</i>)</p>
<dl>
<dd>If <code>+</code> is included, packets matching the rule will have their TTL incremented by <i>number</i>. Similarly, if <code>&#8211;</code> is included, matching packets have their TTL decremented by <i>number</i>. If neither <code>+</code> nor <code>&#8211;</code> is given, the TTL of matching packets is set to <i>number</i>. The valid range of values for <i>number</i> is 1-255.</dl>
</dl>
<p> <code>SOURCE</code> &#8211; {<code>&#8211;</code>|{<i>interface</i>|<code>$FW</code>}|[{<i>interface</i>|<code>$FW</code>}:]<i>address-or-range</i>[<code>,</code><i>address-or-range</i>]&#8230;}[<i>exclusion</i>]</p>
<dl>
<dd>May be:</p>
<dl>
<dd>1. An interface name &#8211; matches traffic entering the firewall on the specified interface. May not be used in classify rules or in rules using the :T chain qualifier.</dl>
<dl>
<dd>2. A comma-separated list of host or network IP addresses or MAC addresses. <code>This form will not match traffic that originates on the firewall itself unless either &lt;major&gt;&lt;minor&gt; or the :T chain qualifier is used in the ACTION column.</code> Examples:.RS 4 0.0.0.0/0</dl>
<dl>
<dd>192.168.1.0/24, 172.20.4.0/24</dl>
</dl>
<dl>
<dd>3. An interface name followed by a colon (&quot;:&quot;) followed by a comma-separated list of host or network IP addresses or MAC addresses. May not be used in classify rules or in rules using the :T chain qualifier.</dl>
<dl>
<dd>4. $FW optionally followed by a colon (&quot;:&quot;) and a comma-separated list of host or network IP addresses. Matches packets originating on the firewall. May not be used with a chain qualifier (:P, :F, etc.) in the ACTION column.</dl>
<p> MAC addresses must be prefixed with &quot;~&quot; and use &quot;-&quot; as a separator. Example: ~00-A0-C9-15-39-78 You may exclude certain hosts from the set already defined through use of an <i>exclusion</i> (see m[blue]<code>shorewall-exclusion</code>m[]<font SIZE="-2">[13]</font>(5)). <code>DEST</code> &#8211; {<code>&#8211;</code>|{<i>interface</i>|$FW}|[<i>{interface</i>|$FW}:]<i>address-or-range</i>[<code>,</code><i>address-or-range</i>]&#8230;}[<i>exclusion</i>]</p>
<dl>
<dd>May be:</p>
<dl>
<dd>1. An interface name. May not be used in the PREROUTING chain (:P in the mark column or no chain qualifier and MARK_IN_FORWARD_CHAIN=No in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[14]</font> (5)). The interface name may be optionally followed by a colon (&quot;:&quot;) and an IP address list.</dl>
<dl>
<dd>2. A comma-separated list of host or network IP addresses. The list may include ip address ranges if your kernel and iptables include iprange support.</dl>
<dl>
<dd>3. Beginning with Shorewall 4.4.13, $FW may be specified by itself or qualified by an address list. This causes marking to occur in the INPUT chain.</dl>
<p> You may exclude certain hosts from the set already defined through use of an <i>exclusion</i> (see m[blue]<code>shorewall-exclusion</code>m[]<font SIZE="-2">[13]</font>(5)).</dl>
<p> <code>PROTO</code> &#8211; {<code>&#8211;</code>|<code>{tcp:syn</code>|<code>ipp2p</code>|<code>ipp2p:udp</code>|<code>ipp2p:all</code>|<i>protocol-number</i>|<i>protocol-name</i>|<code>all}[,&#8230;]}</code></p>
<dl>
<dd>Protocol &#8211; <code>ipp2p</code> requires ipp2p match support in your kernel and iptables. Beginning with Shorewall 4.5.12, this column can accept a comma-separated list of protocols.</dl>
<p> <code>DPORT</code>&#8211; {<code>&#8211;</code>|<i>port-name-number-or-range</i>[<code>,</code><i>port-name-number-or-range</i>]&#8230;|+<i>ipset</i>}</p>
<dl>
<dd>Optional destination Ports. A comma-separated list of Port names (from <a href="/docs/linux/man/5-services/">services</a>(5)), <i>port number</i>s or <i>port range</i>s; if the protocol is <code>icmp</code>, this column is interpreted as the destination icmp-type(s). ICMP types may be specified as a numeric type, a numeric type and code separated by a slash (e.g., 3/4), or a typename. See m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#ICMP">http://www.shorewall.net/configuration_file_basics.htm#ICMP</a></code>m[]<font SIZE="-2">[15]</font>. If the protocol is <code>ipp2p</code>, this column is interpreted as an ipp2p option without the leading &quot;&#8211;&quot; (example <code>bit</code> for bit-torrent). If no PORT is given, <code>ipp2p</code> is assumed. An entry in this field requires that the PROTO column specify icmp (1), tcp (6), udp (17), sctp (132) or udplite (136). Use &#8216;-&#8216; if any of the following field is supplied. Beginning with Shorewall 4.6.0, an <i>ipset</i> name can be specified in this column. This is intended to be used with bitmap:port ipsets. This column was formerly named DEST PORT(S).</dl>
<p> <code>SPORT</code> &#8211; {<code>&#8211;</code>|<i>port-name-number-or-range</i>[<code>,</code><i>port-name-number-or-range</i>]&#8230;|+<i>ipset</i>}</p>
<dl>
<dd>Optional source port(s). If omitted, any source port is acceptable. Specified as a comma-separated list of port names, port numbers or port ranges. An entry in this field requires that the PROTO column specify tcp (6), udp (17), sctp (132) or udplite (136). Use &#8216;-&#8216; if any of the following fields is supplied. Beginning with Shorewall 4.5.15, you may place &#8216;=&#8217; in this column, provided that the DPORT column is non-empty. This causes the rule to match when either the source port or the destination port in a packet matches one of the ports specified in DEST PORTS(S). Use of &#8216;=&#8217; requires multi-port match in your iptables and kernel. Beginning with Shorewall 4.6.0, an <i>ipset</i> name can be specified in this column. This is intended to be used with bitmap:port ipsets. This column was formerly labelled SOURCE PORT(S).</dl>
<p> <code>USER</code> &#8211; [<code>!</code>][<i>user-name-or-number</i>][<code>:</code><i>group-name-or-number</i>][<code>+</code><i>program-name</i>]</p>
<dl>
<dd>This optional column may only be non-empty if the SOURCE is the firewall itself. When this column is non-empty, the rule applies only if the program generating the output is running under the effective <i>user</i> and/or <i>group</i> specified (or is NOT running under that id if &quot;!&quot; is given). Examples: joe</p>
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
 The ability to specify a program name was removed from Netfilter in kernel version 2.6.14.  <code>TEST</code> &#8211; [<code>!</code>]<i>value</i>[/<i>mask</i>][<code>:C</code>]</p>
<dl>
<dd>Optional &#8211; Defines a test on the existing packet or connection mark. The rule will match only if the test returns true. If you don&#8217;t want to define a test but need to specify anything in the following columns, place a &quot;-&quot; in this field. !</p>
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
<p> <code>LENGTH</code> &#8211; [<i>length</i>|[<i>min</i>]<code>:</code>[<i>max</i>]]</p>
<dl>
<dd>Optional &#8211; packet payload length. This field, if present allow you to match the length of a packet payload (Layer 4 data ) against a specific value or range of values. You must have iptables length support for this to work. A range is specified in the form <i>min</i>:<i>max</i> where either <i>min</i> or <i>max</i> (but not both) may be omitted. If <i>min</i> is omitted, then 0 is assumed; if <i>max</i> is omitted, than any packet that is <i>min</i> or longer will match.</dl>
<p> <code>TOS</code> &#8211; <i>tos</i></p>
<dl>
<dd>Type of service. Either a standard name, or a numeric value to match.</p>
<dl>
<dd>
<pre> <code>Minimize-Delay</code> (16)
 <code>Maximize-Throughput</code> (8)
 <code>Maximize-Reliability</code> (4)
 <code>Minimize-Cost</code> (2)
 <code>Normal-Service</code> (0)</pre>
</dl>
</dl>
<p> <code>CONNBYTES</code> &#8211; [!]<i>min</i>:[<i>max</i>[:{<code>O</code>|<code>R</code>|<code>B</code>}[:{<code>B</code>|<code>P</code>|<code>A</code>}]]]</p>
<dl>
<dd>Optional connection Bytes; defines a byte or packet range that the connection must fall within in order for the rule to match. A packet matches if the the packet/byte count is within the range defined by <i>min</i> and <i>max</i> (unless ! is given in which case, a packet matches if the packet/byte count is not within the range). <i>min</i> is an integer which defines the beginning of the byte/packet range. <i>max</i> is an integer which defines the end of the byte/packet range; if omitted, only the beginning of the range is checked. The first letter gives the direction which the range refers to:<code>O</code> &#8211; The original direction of the connection. .sp &#8211; The opposite direction from the original connection. .sp <code>B</code> &#8211; The total of both directions. If omitted, <code>B</code> is assumed. The second letter determines what the range refers to.<code>B</code> &#8211; Bytes .sp <code>P</code> &#8211; Packets .sp <code>A</code> &#8211; Average packet size.If omitted, <code>B</code> is assumed.</dl>
<p> <code>HELPER &#8211; </code><i>helper</i></p>
<dl>
<dd>Names a Netfilter protocol helper module such as <code>ftp</code>, <code>sip</code>, <code>amanda</code>, etc. A packet will match if it was accepted by the named helper module. Example: Mark all FTP data connections with mark 4:</p>
<dl>
<dd>
<pre>#ACTION SOURCE DEST PROTO DPORT SPORT USER TEST LENGTH TOS CONNBYTES HELPER
4:T 0.0.0.0/0 0.0.0.0/0 TCP - - - - - - - ftp</pre>
</dl>
</dl>
<p> <code>PROBABILITY</code> &#8211; [<i>probability</i>]</p>
<dl>
<dd>Added in Shorewall 4.5.0. When non-empty, requires the Statistics Match capability in your kernel and ip6tables and causes the rule to match randomly but with the given <i>probability</i>. The <i>probability</i> is a number 0 &lt; <i>probability</i> &lt;= 1 and may be expressed at up to 8 decimal points of precision.</dl>
<p> <code>DSCP &#8211;</code> [[!]<i>dscp</i>]</p>
<dl>
<dd>Added in Shorewall 4.5.1. When non-empty, match packets whose Differentiated Service Code Point field matches the supplied value (when &#8216;!&#8217; is given, the rule matches packets whose DSCP field does not match the supplied value). The <i>dscp</i> value may be given as an even number (hex or decimal) or as the name of a DSCP class. Valid class names and their associated hex numeric values are:</p>
<dl>
<dd>
<pre> CS0 =&gt; 0x00
 CS1 =&gt; 0x08
 CS2 =&gt; 0x10
 CS3 =&gt; 0x18
 CS4 =&gt; 0x20
 CS5 =&gt; 0x28
 CS6 =&gt; 0x30
 CS7 =&gt; 0x38
 BE =&gt; 0x00
 AF11 =&gt; 0x0a
 AF12 =&gt; 0x0c
 AF13 =&gt; 0x0e
 AF21 =&gt; 0x12
 AF22 =&gt; 0x14
 AF23 =&gt; 0x16
 AF31 =&gt; 0x1a
 AF32 =&gt; 0x1c
 AF33 =&gt; 0x1e
 AF41 =&gt; 0x22
 AF42 =&gt; 0x24
 AF43 =&gt; 0x26
 EF =&gt; 0x2e</pre>
</dl>
</dl>
<p> <code>STATE</code> &#8212; {<code>NEW</code>|<code>RELATED</code>|<code>ESTABLISHED</code>|<code>INVALID</code>} [,&#8230;]</p>
<dl>
<dd>The rule will only match if the packet&#8217;s connection is in one of the listed states.</dl>
<p> <code>TIME</code> &#8211; <i>timeelement</i>[&amp;<i>timeelement</i>&#8230;]</p>
<dl>
<dd>Added in Shorewall 4.6.2. May be used to limit the rule to a particular time period each day, to particular days of the week or month, or to a range defined by dates and times. Requires time match support in your kernel and ip6tables. <i>timeelement</i> may be: timestart=<i>hh</i>:<i>mm</i>[:<i>ss</i>]</p>
<dl>
<dd>Defines the starting time of day.</dl>
<p> timestop=<i>hh</i>:<i>mm</i>[:<i>ss</i>]</p>
<dl>
<dd>Defines the ending time of day.</dl>
<p> contiguous</p>
<dl>
<dd>Added in Shoreawll 5.0.12. When <code>timestop</code> is smaller than <code>timestart</code> value, match this as a single time period instead of distinct intervals.</dl>
<p> utc</p>
<dl>
<dd>Times are expressed in Greenwich Mean Time.</dl>
<p> localtz</p>
<dl>
<dd>Deprecated by the Netfilter team in favor of <code>kerneltz</code>. Times are expressed in Local Civil Time (default).</dl>
<p> kerneltz</p>
<dl>
<dd>Added in Shorewall 4.5.2. Times are expressed in Local Kernel Time (requires iptables 1.4.12 or later).</dl>
<p> weekdays=ddd[,ddd]&#8230;</p>
<dl>
<dd>where <i>ddd</i> is one of <code>Mon</code>, <code>Tue</code>, <code>Wed</code>, <code>Thu</code>, <code>Fri</code>, <code>Sat</code> or <code>Sun</code></dl>
<p> monthdays=dd[,dd],&#8230;</p>
<dl>
<dd>where <i>dd</i> is an ordinal day of the month</dl>
<p> datestart=<i>yyyy</i>[-<i>mm</i>[-<i>dd</i>[<code>T</code><i>hh</i>[:<i>mm</i>[:<i>ss</i>]]]]]</p>
<dl>
<dd>Defines the starting date and time.</dl>
<p> datestop=<i>yyyy</i>[-<i>mm</i>[-<i>dd</i>[<code>T</code><i>hh</i>[:<i>mm</i>[:<i>ss</i>]]]]]</p>
<dl>
<dd>Defines the ending date and time.</dl>
</dl>
<h2>Example</h2>
<p>Example 1:</p>
<dl>
<dd>Mark all ICMP echo traffic with packet mark 1. Mark all peer to peer traffic with packet mark 4. </p>
<p> This is a little more complex than otherwise expected. Since the ipp2p module is unable to determine all packets in a connection are P2P packets, we mark the entire connection as P2P if any of the packets are determined to match. </p>
<p> We assume packet/connection mark 0 means unclassified. </p>
<dl>
<dd>
<pre> #ACTION SOURCE DEST PROTO DPORT SPORT USER TEST
 <a href="//www.systutorials.com/docs/linux/man/1-MARK/">MARK</a>(1):T 0.0.0.0/0 0.0.0.0/0 icmp echo-request
 <a href="//www.systutorials.com/docs/linux/man/1-MARK/">MARK</a>(1):T 0.0.0.0/0 0.0.0.0/0 icmp echo-reply
 RESTORE:T 0.0.0.0/0 0.0.0.0/0 all - - - 0
 CONTINUE:T 0.0.0.0/0 0.0.0.0/0 all - - - !0
 <a href="//www.systutorials.com/docs/linux/man/4-MARK/">MARK</a>(4):T 0.0.0.0/0 0.0.0.0/0 ipp2p:all
 SAVE:T 0.0.0.0/0 0.0.0.0/0 all - - - !0</pre>
</dl>
<p> If a packet hasn&#8217;t been classified (packet mark is 0), copy the connection mark to the packet mark. If the packet mark is set, we&#8217;re done. If the packet is P2P, set the packet mark to 4. If the packet mark has been set, save it to the connection mark.</dl>
<p> Example 2:</p>
<dl>
<dd>SNAT outgoing connections on eth0 from 192.168.1.0/24 in round-robin fashion between addresses 1.1.1.1, 1.1.1.3, and 1.1.1.9 (Shorewall 4.5.9 and later). </p>
<dl>
<dd>
<pre>/etc/shorewall/mangle:
 #ACTION SOURCE DEST PROTO DPORT SPORT USER TEST
 CONNMARK(1-3):F 192.168.1.0/24 eth0 ; state=NEW
/etc/shorewall/masq:
 #INTERFACE SOURCE ADDRESS ...
 eth0 192.168.1.0/24 1.1.1.1 ; mark=1:C
 eth0 192.168.1.0/24 1.1.1.3 ; mark=2:C
 eth0 192.168.1.0/24 1.1.1.4 ; mark=3:C</pre>
</dl>
</dl>
<h2>Files</h2>
<p>/etc/shorewall/mangle</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/traffic_shaping.htm">http://www.shorewall.net/traffic_shaping.htm</a></code>m[]<font SIZE="-2">[16]</font> </p>
<p> m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/MultiISP.html">http://www.shorewall.net/MultiISP.html</a></code>m[]<font SIZE="-2">[4]</font> </p>
<p> m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/PacketMarking.html">http://www.shorewall.net/PacketMarking.html</a></code>m[]<font SIZE="-2">[17]</font> </p>
<p> m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[]<font SIZE="-2">[18]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-ecn/">shorewall-ecn</a>(5), <a href="/docs/linux/man/5-shorewall-exclusion/">shorewall-exclusion</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall_interfaces/">shorewall_interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-rtrules/">shorewall-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-secmarks/">shorewall-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd><a href="/docs/linux/man/5-shorewall-tcrules/">shorewall-tcrules</a>(5)</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-tcrules.html">http://www.shorewall.net/manpages/shorewall-tcrules.html</a></dl>
<dt> 2.</p>
<dd><a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5)</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall.conf.html">http://www.shorewall.net/manpages/shorewall.conf.html</a></dl>
<dt> 3.</p>
<dd>shorewall-rules</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-rules.html">http://www.shorewall.net/manpages/shorewall-rules.html</a></dl>
<dt> 4.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/MultiISP.html">http://www.shorewall.net/MultiISP.html</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/MultiISP.html">http://www.shorewall.net/MultiISP.html</a></dl>
<dt> 5.</p>
<dd>shorewall-actions</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netshorewall6-actions.html">http://www.shorewall.netshorewall6-actions.html</a></dl>
<dt> 6.</p>
<dd><a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5)</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netmanpages/shorewall-actions.html">http://www.shorewall.netmanpages/shorewall-actions.html</a></dl>
<dt> 7.</p>
<dd>shorewall-tcdevices</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-tcdevices.html">http://www.shorewall.net/manpages/shorewall-tcdevices.html</a></dl>
<dt> 8.</p>
<dd>shorewall-tcclasses</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-tcclasses.html">http://www.shorewall.net/manpages/shorewall-tcclasses.html</a></dl>
<dt> 9.</p>
<dd><a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5)</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netmanpages/shorewall-providers.html">http://www.shorewall.netmanpages/shorewall-providers.html</a></dl>
<dt>10.</p>
<dd><a href="/docs/linux/man/5-shorewall-ecn/">shorewall-ecn</a>(5)</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netshorewall-ecn.html">http://www.shorewall.netshorewall-ecn.html</a></dl>
<dt>11.</p>
<dd>shorewall-actions</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-actions.html">http://www.shorewall.net/manpages/shorewall-actions.html</a></dl>
<dt>12.</p>
<dd>shorewall-providers</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-providers.html">http://www.shorewall.net/manpages/shorewall-providers.html</a></dl>
<dt>13.</p>
<dd>shorewall-exclusion</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-exclusion.html">http://www.shorewall.net/manpages/shorewall-exclusion.html</a></dl>
<dt>14.</p>
<dd>shorewall.conf</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netmanpages/shorewall.conf">http://www.shorewall.netmanpages/shorewall.conf</a></dl>
<dt>15.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#ICMP">http://www.shorewall.net/configuration_file_basics.htm#ICMP</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#ICMP">http://www.shorewall.net/configuration_file_basics.htm#ICMP</a></dl>
<dt>16.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/traffic_shaping.htm">http://www.shorewall.net/traffic_shaping.htm</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/traffic_shaping.htm">http://www.shorewall.net/traffic_shaping.htm</a></dl>
<dt>17.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/PacketMarking.html">http://www.shorewall.net/PacketMarking.html</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/PacketMarking.html">http://www.shorewall.net/PacketMarking.html</a></dl>
<dt>18.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dl>
