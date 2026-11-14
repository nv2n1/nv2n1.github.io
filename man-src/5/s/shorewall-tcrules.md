---
title: "shorewall-tcrules(5)"
name: "shorewall-tcrules"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-tcrules/"
description: "tcrules – Shorewall Packet Marking rules file"
---

<p>tcrules &#8211; Shorewall Packet Marking rules file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/tcrules</code></dl>
<h2>Description</h2>
<dd>Entries in this file cause packets to be marked as a means of classifying them for traffic control or policy routing. </p>
<p> Important </p>
<p> Unlike rules in the <i>shorewall-rules</i>[1](5) file, evaluation of rules in this file will continue after a match. So the final mark for each packet will be the one assigned by the LAST tcrule that matches. </p>
<p> If you use multiple internet providers with the &#8216;track&#8217; option, in /etc/shorewall/providers be sure to read the restrictions at <i><a rel="nofollow" href="http://shorewall.net/MultiISP.html">http://shorewall.net/MultiISP.html</a></i>. </p>
<p> The columns in the file are as follows. </p>
<p> <code>MARK/CLASSIFY</code> &#8211; {<i>value</i>|<i>major</i><code>:</code><i>minor</i>|<code>RESTORE</code>[<code>/</code><i>mask</i>]|<code>SAVE</code>[<code>/</code><i>mask</i>]|<code>CONTINUE</code>|<code>SAME</code>|<code>COMMENT</code>|<code>IPMARK</code>[([(<code>src</code>|<code>dst</code>}][,[<i>mask1</i>][,[<i>mask2</i>][,[<i>shift</i>]]]]])]}[<code>:</code>{<code>C</code>|<code>F</code>|<code>P</code>|<code>T</code>|<code>CF</code>|<code>CP</code>|<code>CT</code>}]</p>
<dl>
<dd>May assume one of the following values. </p>
<dl>
<dd>1.A mark <i>value</i> which is an integer in the range 1-255. </p>
<p> Normally will set the mark value. If preceded by a vertical bar (&quot;|&quot;), the mark value will be logically ORed with the current mark value to produce a new mark value. If preceded by an ampersand (&quot;&amp;&quot;), will be logically ANDed with the current mark value to produce a new mark value. </p>
<p> Both &quot;|&quot; and &quot;&amp;&quot; require Extended MARK Target support in your kernel and iptables; neither may be used with connection marks (see below). </p>
<p> May optionally be followed by <code>:P</code>, <code>:F</code> or <code>:T</code> where<code> :P</code> indicates that marking should occur in the PREROUTING chain, <code>:F</code> indicates that marking should occur in the FORWARD chain and <code>:T</code> indicates that marking should occur in the POSTROUTING chain. If neither <code>:P</code>, <code>:F</code> nor <code>:T</code> follow the mark value then the chain is determined as follows: </p>
<p> &#8211; If the SOURCE is <code>$FW</code>[<code>:</code><i>address-or-range</i>[,<i>address-or-range</i>]&#8230;], then the rule is inserted into the OUTPUT chain. When HIGH_ROUTE_MARKS=Yes, only high mark values may be assigned there. Packet marking rules for traffic shaping of packets originating on the firewall must be coded in the POSTROUTING chain (see below). </p>
<p> &#8211; Otherwise, the chain is determined by the setting of MARK_IN_FORWARD_CHAIN in <i>shorewall.conf</i>[2](5). </p>
<p> If your kernel and iptables include CONNMARK support then you can also mark the connection rather than the packet. </p>
<p> The mark value may be optionally followed by &quot;/&quot; and a mask value (used to determine those bits of the connection mark to actually be set). The mark and optional mask are then followed by one of:+ </p>
<p> <code>C</code></p>
<dl>
<dd>Mark the connection in the chain determined by the setting of MARK_IN_FORWARD_CHAIN</dl>
<p> <code>CF</code></p>
<dl>
<dd>Mark the connection in the FORWARD chain</dl>
<p> <code>CP</code></p>
<dl>
<dd>Mark the connection in the PREROUTING chain.</dl>
<p> CT</p>
<dl>
<dd>Mark the connecdtion in the POSTROUTING chain</dl>
<p> <code>Special considerations for If HIGH_ROUTE_MARKS=Yes in </code><i>shorewall.conf</i>[2]<code>(5</code>). </p>
<p> If HIGH_ROUTE_MARKS=Yes, then you may also specify a value in the range 0x0100-0xFF00 with the low-order byte being zero. Such values may only be used in the PREROUTING chain (value followed by <code>:P</code> or you have set MARK_IN_FORWARD_CHAIN=No in <i>shorewall.conf</i>[2](5) and have not followed the value with <code>:F</code>) or the OUTPUT chain (SOURCE is <code>$FW</code>). With HIGH_ROUTE_MARKS=Yes, non-zero mark values less that 256 are not permitted. Shorewall prohibits non-zero mark values less that 256 in the OUTPUT chain when HIGH_ROUTE_MARKS=Yes. While earlier versions allow such values in the OUTPUT chain, it is strongly recommended that with HIGH_ROUTE_MARKS=Yes, you use the POSTROUTING chain to apply traffic shaping marks/classification.</dl>
<dl>
<dd>2.A classification Id (classid) of the form <i>major</i>:<i>minor</i> where <i>major</i> and <i>minor</i> are integers. Corresponds to the &#8216;class&#8217; specification in these traffic shaping modules: </p>
<dl>
<dd>
<pre> atm
 cbq
 dsmark
 pfifo_fast
 htb
 prio</pre>
</dl>
<p> Classification occurs in the POSTROUTING chain except when the <code>SOURCE</code> is <code>$FW</code>[:<i>address</i>] in which case classification occurs in the OUTPUT chain. </p>
<p> When using Shorewall&#8217;s built-in traffic shaping tool, the <i>major</i> class is the device number (the first device in <i>shorewall-tcdevices</i>[3](5) is major class 1, the second device is major class 2, and so on) and the <i>minor</i> class is the class&#8217;s MARK value in <i>shorewall-tcclasses</i>[4](5) preceded by the number 1 (MARK 1 corresponds to minor class 11, MARK 5 corresponds to minor class 15, MARK 22 corresponds to minor class 122, etc.).</dl>
<dl>
<dd>3.<code>RESTORE</code>[/<i>mask</i>] &#8212; restore the packet&#8217;s mark from the connection&#8217;s mark using the supplied mask if any. Your kernel and iptables must include CONNMARK support. </p>
<p> As in 1) above, may be followed by <code>:P</code> or <code>:F</code></dl>
<dl>
<dd>4.<code>SAVE</code>[/<i>mask</i>] &#8212; save the packet&#8217;s mark to the connection&#8217;s mark using the supplied mask if any. Your kernel and iptables must include CONNMARK support. </p>
<p> As in 1) above, may be followed by <code>:P</code> or <code>:F</code></dl>
<dl>
<dd>5.<code>CONTINUE</code> Don&#8217;t process any more marking rules -in the table. </p>
<p> As in 1) above, may be followed by <code>:P</code> or <code>:F</code>. Currently, CONTINUE may not be used with <i>exclusion</i> (see the SOURCE and DEST columns below); that restriction will be removed when iptables/Netfilter provides the necessary support.</dl>
<dl>
<dd>6.<code>SAME</code> Some websites run applications that require multiple connections from a client browser. Where multiple &#8216;balanced&#8217; providers are configured, this can lead to problems when some of the connections are routed through one provider and some through another. The SAME target allows you to work around that problem. SAME may be used in the PREROUTING and OUTPUT chains. When used in PREROUTING, it causes matching connections from an individual local system to all use the same provider. For example: </p>
<dl>
<dd>
<pre>#MARK/ SOURCE DEST PROTO DEST
#CLASSIFY PORT(S)
SAME:P 192.168.1.0/24 0.0.0.0/0 tcp 80,443</pre>
</dl>
<p> If a host in 192.168.1.0/24 attempts a connection on TCP port 80 or 443 and it has sent a packet on either of those ports in the last five minutes then the new connection will use the same provider as the connection over which that last packet was sent. </p>
<p> When used in the OUTPUT chain, it causes all matching connections to an individual remote system to all use the same provider. For example: </p>
<dl>
<dd>
<pre>#MARK/ SOURCE DEST PROTO DEST
#CLASSIFY PORT(S)
SAME $FW 0.0.0.0/0 tcp 80,443</pre>
</dl>
<p> If the firewall attempts a connection on TCP port 80 or 443 and it has sent a packet on either of those ports in the last five minutes to the same remote system then the new connection will use the same provider as the connection over which that last packet was sent.</dl>
<dl>
<dd>7.<code>COMMENT</code> &#8212; the rest of the line will be attached as a comment to the Netfilter rule(s) generated by the following entries. The comment will appear delimited by &quot;/* &#8230; */&quot; in the output of <code>shorewall show mangle</code> </p>
<p> To stop the comment from being attached to further rules, simply include COMMENT on a line by itself.</dl>
<dl>
<dd>8.<code>IPMARK</code> &#8211; Assigns a mark to each matching packet based on the either the source or destination IP address. By default, it assigns a mark value equal to the low-order 8 bits of the source address. Default values are:</p>
<dl>
<dd>src</p>
<dd><i>mask1</i> = 0xFF</p>
<dd><i>mask2</i> = 0x00</p>
<dd><i>shift</i> = 0 &#8216;src&#8217; and &#8216;dst&#8217; specify whether the mark is to be based on the source or destination address respectively. The selected address is first shifted to the right by <i>shift</i> bits. The result is then LANDed with <i>mask1</i> then LORed with <i>ma</i><i>s</i><i>k2</i>. </p>
<p> In a sense, the IPMARK target is more like an IPCLASSIFY target in that the mark value is later interpreted as a class ID. A packet mark is 32 bits wide; so is a class ID. The &lt;major&gt; class occupies the high-order 16 bits and the &lt;minor&gt; class occupies the low-order 16 bits. So the class ID 1:4ff (remember that class IDs are always in hex) is equivalent to a mark value of 0x104ff. Remember that Shorewall uses the interface number as the &lt;major&gt; number where the first interface in tcdevices has &lt;major&gt; number 1, the second has &lt;major&gt; number 2, and so on. </p>
<p> The IPMARK target assigns a mark to each matching packet based on the either the source or destination IP address. By default, it assigns a mark value equal to the low-order 8 bits of the source address. The syntax is as follows: <code>IPMARK</code>[([{<code>src</code>|<code>dst</code>}][,[<i>mask1</i>][,[<i>mask2</i>][,[<i>shift</i>]]]])] Default values are:</p>
<dd><code>src</code></p>
<dd><i>mask1</i> = 0xFF</p>
<dd><i>mask2</i> = 0x00</p>
<dd><i>shift</i> = 0 <code>src</code> and <code>dst</code> specify whether the mark is to be based on the source or destination address respectively. The selected address is first shifted right by <i>shift</i>, then LANDed with <i>mask1</i> and then LORed with <i>mask2</i>. The <i>shift</i> argument is intended to be used primarily with IPv6 addresses. </p>
<p> Example: IPMARK(src,0xff,0x10100)</p>
<dd>Suppose that the source IP address is 192.168.4.3 =<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0xc0a80403;&nbsp;<wbr>then</p>
<dd>0xc0a80403 &gt;&gt; 0 = 0xc0a80403</p>
<dd>0xc0a80403 LAND 0xFF = 0x03</p>
<dd>0x03 LOR 0x0x10100 = 0x10103 or class ID<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1:103 It is important to realize that, while class IDs are composed of a <i>major</i> and a <i>minor</i> value, the set of values must be unique. That is, the same numeric value cannot be used as both a <i>major</i> and a <i>minor</i> number for the same interface unless class nesting occurs (which is not currently possible with Shorewall). You should keep this in mind when deciding how to map IP addresses to class IDs. </p>
<p> For example, suppose that your internal network is 192.168.1.0/29 (host IP addresses 192.168.1.1 &#8211; 192.168.1.6). Your first notion might be to use IPMARK(src,0xFF,0x10000) so as to produce class IDs 1:1 through 1:6. But 1:1 is an invalid class ID since the <i>major</i> and <i>minor</i> classes are equal. So you might chose instent to use IPMARK(src,0xFF,0x10100) as in the example above so that all of your <i>minor</i> classes will have a value &gt; 256.</dl>
</dl>
</dl>
<p> <code>SOURCE</code> &#8211; {<code>&#8211;</code>|{<i>interface</i>|<code>$FW</code>}|[{<i>interface</i>|<code>$FW</code>}:]<i>address-or-range</i>[<code>,</code><i>address-or-range</i>]&#8230;}[<i>exclusion</i>]</p>
<dl>
<dd>May be: </p>
<dl>
<dd>1.An interface name &#8211; matches traffic entering the firewall on the specified interface. May not be used in classify rules or in rules using the :T chain qualifier.</dl>
<dl>
<dd>2.A comma-separated list of host or network IP addresses or MAC addresses. <code>This form will not match traffic that originates on the firewall itself unless either &lt;major&gt;&lt;minor&gt; or the :T chain qualifier is used in the MARK column.</code> </p>
<p> Examples:.IP &quot;&quot; 4 0.0.0.0/0 </p>
<dl>
<dd>192.168.1.0/24, 172.20.4.0/24</dl>
</dl>
<dl>
<dd>3.An interface name followed by a colon (&quot;:&quot;) followed by a comma-separated list of host or network IP addresses or MAC addresses. May not be used in classify rules or in rules using the :T chain qualifier.</dl>
<dl>
<dd>4.$FW optionally followed by a colon (&quot;:&quot;) and a comma-separated list of host or network IP addresses. Matches packets originating on the firewall. May not be used with a chain qualifier (:P, :F, etc.) in the MARK column.</dl>
<dl>
<dd>MAC addresses must be prefixed with &quot;~&quot; and use &quot;-&quot; as a separator. </p>
<p> Example: ~00-A0-C9-15-39-78 </p>
<p> You may exclude certain hosts from the set already defined through use of an <i>exclusion</i> (see <i>shorewall-exclusion</i>[5](5)).</dl>
</dl>
<p> <code>DEST</code> &#8211; {<code>&#8211;</code>|{<i>interface</i>|[<i>interface</i>:]<i>address-or-range</i>[<code>,</code><i>address-or-range</i>]&#8230;}[<i>exclusion</i>]</p>
<dl>
<dd>May be: </p>
<dl>
<dd>1.An interface name. May not be used in the PREROUTING chain (:P in the mark column or no chain qualifier and MARK_IN_FORWARD_CHAIN=No in <i>shorewall.conf</i>[6] (5)). The interface name may be optionally followed by a colon (&quot;:&quot;) and an IP address list.</dl>
<dl>
<dd>2.A comma-separated list of host or network IP addresses. The list may include ip address ranges if your kernel and iptables include iprange support.</dl>
<dl>
<dd>You may exclude certain hosts from the set already defined through use of an <i>exclusion</i> (see <i>shorewall-exclusion</i>[5](5)).</dl>
</dl>
<p> <code>PROTO</code> &#8211; {<code>&#8211;</code>|<code>tcp:syn</code>|<code>ipp2p</code>|<code>ipp2p:udp</code>|<code>ipp2p:all</code>|<i>protocol-number</i>|<i>protocol-name</i>|<code>all}</code></p>
<dl>
<dd>Protocol &#8211; <code>ipp2p</code> requires ipp2p match support in your kernel and iptables.</dl>
<p> <code>PORT(S)</code> (Optional) &#8211; [<code>&#8211;</code>|<i>port-name-number-or-range</i>[<code>,</code><i>port-name-number-or-range</i>]&#8230;]</p>
<dl>
<dd>Destination Ports. A comma-separated list of Port names (from <a href="/docs/linux/man/5-services/">services</a>(5)), <i>port number</i>s or <i>port range</i>s; if the protocol is <code>icmp</code>, this column is interpreted as the destination icmp-type(s). ICMP types may be specified as a numeric type, a numberic type and code separated by a slash (e.g., 3/4), or a typename. See <i><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#ICMP">http://www.shorewall.net/configuration_file_basics.htm#ICMP</a></i>. </p>
<p> If the protocol is <code>ipp2p</code>, this column is interpreted as an ipp2p option without the leading &quot;&#8211;&quot; (example <code>bit</code> for bit-torrent). If no PORT is given, <code>ipp2p</code> is assumed. </p>
<p> This column is ignored if PROTOCOL = all but must be entered if any of the following field is supplied. In that case, it is suggested that this field contain &quot;-&quot;</dl>
<p> <code>SOURCE PORT(S)</code> (Optional) &#8211; [<code>&#8211;</code>|<i>port-name-number-or-range</i>[<code>,</code><i>port-name-number-or-range</i>]&#8230;]</p>
<dl>
<dd>Source port(s). If omitted, any source port is acceptable. Specified as a comma-separated list of port names, port numbers or port ranges.</dl>
<p> <code>USER</code> (Optional) &#8211; [<code>!</code>][<i>user-name-or-number</i>][<code>:</code><i>group-name-or-number</i>][<code>+</code><i>program-name</i>]</p>
<dl>
<dd>This column may only be non-empty if the SOURCE is the firewall itself. </p>
<p> When this column is non-empty, the rule applies only if the program generating the output is running under the effective <i>user</i> and/or <i>group</i> specified (or is NOT running under that id if &quot;!&quot; is given). </p>
<p> Examples: </p>
<p> joe</p>
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
<dd>#program named upnpd </p>
<p> Important The ability to specify a program name was removed from Netfilter in kernel version 2.6.14.</dl>
</dl>
<p> <code>TEST</code> &#8211; [<code>!</code>]<i>value</i>[/<i>mask</i>][<code>:C</code>]</p>
<dl>
<dd>Defines a test on the existing packet or connection mark. The rule will match only if the test returns true. </p>
<p> If you don&#8217;t want to define a test but need to specify anything in the following columns, place a &quot;-&quot; in this field. </p>
<p> !</p>
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
<p> <code>LENGTH</code> (Optional) &#8211; [<i>length</i>|[<i>min</i>]<code>:</code>[<i>max</i>]]</p>
<dl>
<dd>Packet Length. This field, if present allow you to match the length of a packet against a specific value or range of values. You must have iptables length support for this to work. A range is specified in the form <i>min</i>:<i>max</i> where either <i>min</i> or <i>max</i> (but not both) may be omitted. If <i>min</i> is omitted, then 0 is assumed; if <i>max</i> is omitted, than any packet that is <i>min</i> or longer will match.</dl>
<p> <code>TOS</code> &#8211; <i>tos</i></p>
<dl>
<dd>Type of service. Either a standard name, or a numeric value to match. </p>
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
<dd>Connection Bytes; defines a byte or packet range that the connection must fall within in order for the rule to match. </p>
<p> A packet matches if the the packet/byte count is within the range defined by <i>min</i> and <i>max</i> (unless ! is given in which case, a packet matches if the packet/byte count is not within the range). <i>min</i> is an integer which defines the beginning of the byte/packet range. <i>max</i> is an integer which defines the end of the byte/packet range; if omitted, only the beginning of the range is checked. The first letter gives the direction which the range refers to:<code>O</code> &#8211; The original direction of the connection. .sp &#8211; The opposite direction from the original connection. .sp <code>B</code> &#8211; The total of both directions. </p>
<p> If omitted, <code>B</code> is assumed. </p>
<p> The second letter determines what the range refers to.<code>B</code> &#8211; Bytes .sp <code>P</code> &#8211; Packets .sp <code>A</code> &#8211; Average packet size.If omitted, <code>B</code> is assumed.</dl>
<p> <code>HELPER &#8211; </code><i>helper</i></p>
<dl>
<dd>Names a Netfiler protocol helper module such as <code>ftp</code>, <code>sip</code>, <code>amanda</code>, etc. A packet will match if it was accepted by the named helper module. You can also append &quot;-&quot; and a port number to the helper module name (e.g., <code>ftp-21</code>) to specify the port number that the original connection was made on. </p>
<p> Example: Mark all FTP data connections with mark 4: </p>
<dl>
<dd>
<pre>#MARK/ SOURCE DEST PROTO PORT(S) SOURCE USER TEST LENGTH TOS CONNBYTES HELPER
#CLASSIFY PORT(S)
4:T 0.0.0.0/0 0.0.0.0/0 TCP - - - - - - - ftp</pre>
</dl>
</dl>
<h2>Example</h2>
<p>Example 1:</p>
<dl>
<dd>Mark all ICMP echo traffic with packet mark 1. Mark all peer to peer traffic with packet mark 4. </p>
<p> This is a little more complex than otherwise expected. Since the ipp2p module is unable to determine all packets in a connection are P2P packets, we mark the entire connection as P2P if any of the packets are determined to match. </p>
<p> We assume packet/connection mark 0 means unclassified. </p>
<dl>
<dd>
<pre> #MARK/ SOURCE DEST PROTO PORT(S) SOURCE USER TEST
 #CLASSIFY PORT(S)
 1:T 0.0.0.0/0 0.0.0.0/0 icmp echo-request
 1:T 0.0.0.0/0 0.0.0.0/0 icmp echo-reply
 RESTORE:T 0.0.0.0/0 0.0.0.0/0 all - - - 0
 CONTINUE:T 0.0.0.0/0 0.0.0.0/0 all - - - !0
 4:T 0.0.0.0/0 0.0.0.0/0 ipp2p:all
 SAVE:T 0.0.0.0/0 0.0.0.0/0 all - - - !0</pre>
</dl>
<p> If a packet hasn&#8217;t been classifed (packet mark is 0), copy the connection mark to the packet mark. If the packet mark is set, we&#8217;re done. If the packet is P2P, set the packet mark to 4. If the packet mark has been set, save it to the connection mark.</dl>
<h2>Files</h2>
<p>/etc/shorewall/tcrules</p>
<h2>See Also</h2>
<p><i><a rel="nofollow" href="http://shorewall.net/traffic_shaping.htm">http://shorewall.net/traffic_shaping.htm</a></i> </p>
<p> <i><a rel="nofollow" href="http://shorewall.net/MultiISP.html">http://shorewall.net/MultiISP.html</a></i> </p>
<p> <i><a rel="nofollow" href="http://shorewall.net/PacketMarking.html">http://shorewall.net/PacketMarking.html</a></i> </p>
<p> <a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-ecn/">shorewall-ecn</a>(5), <a href="/docs/linux/man/5-shorewall-exclusion/">shorewall-exclusion</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall-interfaces/">shorewall-interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsec/">shorewall-ipsec</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-route_rules/">shorewall-route_rules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall-rules</p>
<dl>
<dd>shorewall-rules.html</dl>
<dt> 2.</p>
<dd>shorewall.conf</p>
<dl>
<dd>shorewall.conf.html</dl>
<dt> 3.</p>
<dd>shorewall-tcdevices</p>
<dl>
<dd>shorewall-tcdevices.html</dl>
<dt> 4.</p>
<dd>shorewall-tcclasses</p>
<dl>
<dd>shorewall-tcclasses.html</dl>
<dt> 5.</p>
<dd>shorewall-exclusion</p>
<dl>
<dd>shorewall-exclusion.html</dl>
<dt> 6.</p>
<dd>shorewall.conf</p>
<dl>
<dd>manpages/shorewall.conf</dl>
