---
title: "shorewall6-accounting(5)"
name: "shorewall6-accounting"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall6-accounting/"
description: "accounting – Shorewall6 Accounting file"
---

<p>accounting &#8211; Shorewall6 Accounting file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall6/accounting</code></dl>
<h2>Description</h2>
<dd>Accounting rules exist simply to count packets and bytes in categories that you define in this file. You may display these rules and their packet and byte counters using the <code>shorewall6 show accounting</code> command. Beginning with Shorewall 4.4.18, the accounting structure can be created with three root chains:</p>
<dl>
<dd>&bull; <code>accountin</code>: Rules that are valid in the <code>INPUT</code> chain (may not specify an output interface).</dl>
<dl>
<dd>&bull; <code>accountout</code>: Rules that are valid in the OUTPUT chain (may not specify an input interface or a MAC address).</dl>
<dl>
<dd>&bull; <code>accounting</code>: Other rules.</dl>
<p> The new structure is enabled by sectioning the accounting file in a manner similar to the m[blue]<code>rules file</code>m[]<font SIZE="-2">[1]</font>. The sections are <code>INPUT</code>, <code>OUTPUT</code> and <code>FORWARD</code> and must appear in that order (although any of them may be omitted). The first non-commentary record in the accounting file must be a section header when sectioning is used.</p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 If sections are not used, the Shorewall rules compiler cannot detect certain violations of netfilter restrictions. These violations can result in run-time errors such as the following: <code>ip6tables-restore v1.4.13: Can&#8217;t use -o with INPUT</code>  Beginning with Shorewall 4.4.20, the ACCOUNTING_TABLE setting was added to shorewall.conf and shorewall6.conf. That setting determines the Netfilter table (filter or mangle) where the accounting rules are added. When ACCOUNTING_TABLE=mangle is specified, the available sections are <code>PREROUTING</code>, <code>INPUT</code>, <code>OUTPUT</code>, <code>FORWARD</code> and <code>POSTROUTING</code>. Section headers have the form: <code>[?]SECTION</code><i>section-name</i> The optional &quot;?&quot; was added in Shorewalll 4.6.0 and is preferred. Existing configurations may be converted to use this form using the <code>shorewall6 update</code> command. When sections are enabled:</p>
<dl>
<dd>&bull; A jump to a user-defined accounting chain must appear before entries that add rules to that chain. This eliminates loops and unreferenced chains.</dl>
<dl>
<dd>&bull; An output interface may not be specified in the <code>PREROUTING</code> and <code>INPUT</code> sections.</dl>
<dl>
<dd>&bull; In the <code>OUTPUT</code> and <code>POSTROUTING</code> sections:</p>
<dl>
<dd>&bull; An input interface may not be specified</dl>
<dl>
<dd>&bull; Jumps to a chain defined in the <code>INPUT</code> or <code>PREROUTING</code> sections that specifies an input interface are prohibited</dl>
<dl>
<dd>&bull; MAC addresses may not be used</dl>
<dl>
<dd>&bull; Jump to a chain defined in the <code>INPUT</code> or <code>PREROUTING</code> section that specifies a MAC address are prohibited.</dl>
</dl>
<dl>
<dd>&bull; The default value of the CHAIN column is:</p>
<dl>
<dd>&bull; <code>accountin</code> in the <code>INPUT</code> section</dl>
<dl>
<dd>&bull; <code>accountout</code> in the <code>OUTPUT</code> section</dl>
<dl>
<dd>&bull; <code>accountfwd</code> in the <code>FORWARD</code> section</dl>
<dl>
<dd>&bull; <code>accountpre</code> in the <code>PREROUTING</code> section</dl>
<dl>
<dd>&bull; <code>accountpost</code> in the <code>POSTROUTING</code> section</dl>
</dl>
<dl>
<dd>&bull; Traffic addressed to the firewall goes through the rules defined in the INPUT section.</dl>
<dl>
<dd>&bull; Traffic originating on the firewall goes through the rules defined in the OUTPUT section.</dl>
<dl>
<dd>&bull; Traffic being forwarded through the firewall goes through the rules from the FORWARD sections.</dl>
<p> The columns in the file are as follows (where the column name is followed by a different name in parentheses, the different name is used in the alternate specification syntax). <code>ACTION</code> &#8211; {<code>COUNT</code>|<code>DONE</code>|<i>chain</i>[:<code>{COUNT|JUMP}</code>]|[?]COMMENT <i>comment</i>}</p>
<dl>
<dd>What to do when a matching packet is found. <code>COUNT</code></p>
<dl>
<dd>Simply count the match and continue with the next rule</dl>
<p> <code>DONE</code></p>
<dl>
<dd>Count the match and don&#8217;t attempt to match any other accounting rules in the chain specified in the <code>CHAIN</code> column.</dl>
<p> <i>chain</i>[<code>:</code><code>COUNT</code>]</p>
<dl>
<dd>Where <i>chain</i> is the name of a chain; shorewall6 will create the chain automatically if it doesn&#8217;t already exist. If a second chain is mentioned in the CHAIN column, then a jump from this second chain to <i>chain</i> is created. If no chain is named in the CHAIN column, then a jump from the default chain to <i>chain</i> is created. If <code>:COUNT</code> is included, a counting rule matching this entry will be added to <i>chain</i>. The <i>chain</i> may not exceed 29 characters in length and may be composed of letters, digits, dash (&#8216;-&#8216;) and underscore (&#8216;_&#8217;).</dl>
<p> <i>chain</i>:JUMP</p>
<dl>
<dd>Like the previous option without the <code>:COUNT</code> part.</dl>
<p> <code>INLINE</code></p>
<dl>
<dd>Added in Shorewall 4.5.16. Allows free form ip6tables matches to be specified following a &#8216;;&#8217;. In the generated ip6tables rule(s), the free form matches will follow any matches that are generated by the column contents.</dl>
<p> <code>NFACCT</code>({<i>object</i>[!]}[,&#8230;])</p>
<dl>
<dd>Added in Shorewall 4.5.7. Provides a form of accounting that survives <code>shorewall stop/shorewall</code> start and <code>shorewall restart</code>. Requires the NFaccnt Match capability in your kernel and iptables. <i>object</i> names an nfacct object (see man <a href="/docs/linux/man/8-nfaccnt/">nfaccnt</a>(8)). Multiple rules can specify the same <i>object</i>; all packets that match any of the rules increment the packet and bytes count of the object. Prior to Shorewall 4.5.16, only one <i>object</i> could be specified. Beginning with Shorewall 4.5.16, an arbitrary number of objects may be given. With Shorewall 4.5.16 or later, an nfacct <i>object</i> in the list may optionally be followed by <code>!</code> to indicate that the nfacct <i>object</i> will be incremented unconditionally for each packet. When <code>!</code> is omitted, the <i>object</i> will be incremented only if all of the matches in the rule succeed.</dl>
<p> <code>NFLOG</code>[(nflog-parameters)] &#8211; Added in Shorewall-4.4.20.</p>
<dl>
<dd>Causes each matching packet to be sent via the currently loaded logging back end (usually nfnetlink_log) where it is available to accounting daemons through a netlink socket.</dl>
<p> <code>?COMMENT</code></p>
<dl>
<dd>The remainder of the line is treated as a comment which is attached to subsequent rules until another ?COMMENT line is found or until the end of the file is reached. To stop adding comments to rules, use a line with only the word ?COMMENT.</dl>
</dl>
<p> <code>CHAIN</code> &#8211; {<code>&#8211;</code>|<i>chain</i>}</p>
<dl>
<dd>The name of a <i>chain</i>. If specified as <code>&#8211;</code> the <code>accounting</code> chain is assumed when the file is un-sectioned. When the file is sectioned, the default is one of accountin, accountout, etc. depending on the section. This is the chain where the accounting rule is added. The <i>chain</i> will be created if it doesn&#8217;t already exist. The <i>chain</i> may not exceed 29 characters in length.</dl>
<p> <code>SOURCE</code> &#8211; {<code>&#8211;</code>|<code>any</code>|<code>all</code>|<i>interface</i>|<i>interface</i><code>:</code><code>[</code><i>address</i><code>]</code>|<i>address</i>}</p>
<dl>
<dd>Packet Source. The name of an <i>interface</i>, an <i>address</i> (host or net) or an <i>interface</i> name followed by &quot;:&quot; and a host or net <i>address</i>. An ipset name is also accepted as an <i>address</i>.</dl>
<p> <code>DEST</code> &#8211; {<code>&#8211;</code>|<code>any</code>|<code>all</code>|<i>interface</i>|<i>interface</i><code>:[</code><i>address</i><code>]</code>|<i>address</i>}</p>
<dl>
<dd>Packet Destination. Format same as <code>SOURCE</code> column. This column was formerly labelled DESTINATION.</dl>
<p> <code>PROTO</code> &#8211; {<code>&#8211;</code>|<code>any</code>|<code>all</code>|<i>protocol-name</i>|<i>protocol-number</i>|<code>ipp2p</code>[<code>:</code>{<code>udp</code>|<code>all</code>}]}</p>
<dl>
<dd>A <i>protocol-name</i> (from <a href="/docs/linux/man/5-protocols/">protocols</a>(5)), a <i>protocol-number</i>, <code>ipp2p</code>, <code>ipp2p:udp</code> or <code>ipp2p:all</code> Beginning with Shorewall 4.5.12, this column can accept a comma-separated list of protocols. This column was formerly labelled PROTOCOL.</dl>
<p> <code>DPORT</code> &#8211; {<code>&#8211;</code>|<code>any</code>|<code>all</code>|<i>ipp2p-option</i>|<i>port-name-or-number</i>[,<i>port-name-or-number</i>]&#8230;}</p>
<dl>
<dd>Destination Port number. Service name from <a href="/docs/linux/man/5-services/">services</a>(5) or <i>port number</i>. May only be specified if the protocol is TCP (6), UDP (17), DCCP (33), SCTP (132) or UDPLITE (136). You may place a comma-separated list of port names or numbers in this column if your kernel and ip6tables include multi-port match support. If the PROTOCOL is <code>ipp2p</code> then this column must contain an <i>ipp2p-option</i> (&quot;ip6tables -m ipp2p &#8211;help&quot;) without the leading &quot;&#8211;&quot;. If no option is given in this column, <code>ipp2p</code> is assumed. This column was formerly labelled DEST PORT(S).</dl>
<p> <code>SPORT</code> &#8211; {<code>&#8211;</code>|<code>any</code>|<code>all</code>|<i>port-name-or-number</i>[,<i>port-name-or-number</i>]&#8230;}</p>
<dl>
<dd>Service name from <a href="/docs/linux/man/5-services/">services</a>(5) or <i>port number</i>. May only be specified if the protocol is TCP (6), UDP (17), DCCP (33), SCTP (132) or UDPLITE (136). You may place a comma-separated list of port numbers in this column if your kernel and ip6tables include multi-port match support. Beginning with Shorewall 4.5.15, you may place &#8216;=&#8217; in this column, provided that the DPORT column is non-empty. This causes the rule to match when either the source port or the destination port in a packet matches one of the ports specified in DPORT. Use of &#8216;=&#8217; requires multi-port match in your iptables and kernel. This column was formerly labelled SOURCE PORT(S).</dl>
<p> <code>USER</code> &#8211; [<code>!</code>][<i>user-name-or-number</i>][<code>:</code><i>group-name-or-number</i>][<code>+</code><i>program-name</i>]</p>
<dl>
<dd>This column may only be non-empty if the <code>CHAIN</code> is <code>OUTPUT</code>. When this column is non-empty, the rule applies only if the program generating the output is running under the effective <i>user</i> and/or <i>group</i> specified (or is NOT running under that id if &quot;!&quot; is given). Examples: joe</p>
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
 The ability to specify a program name was removed from Netfilter in kernel version 2.6.14.  This column was formerly labelled USER/GROUP.</dl>
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
<p> <code>IPSEC &#8211; </code><i>option-list</i><code> (Optional &#8211; Added in Shorewall 4.4.13 but broken until 4.5.4.1 )</code></p>
<dl>
<dd>The option-list consists of a comma-separated list of options from the following list. Only packets that will be encrypted or have been decrypted via an SA that matches these options will have their source address changed. May only be specified when sections are used. <code>reqid=</code><i>number</i></p>
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
<p> <code>yes</code> or <code>ipsec</code></p>
<dl>
<dd>When used by itself, causes all traffic that will be encrypted/encapsulated or has been decrypted/un-encapsulated to match the rule.</dl>
<p> <code>no</code> or <code>none</code></p>
<dl>
<dd>When used by itself, causes all traffic that will not be encrypted/encapsulated or has been decrypted/un-encapsulated to match the rule.</dl>
<p> <code>in</code></p>
<dl>
<dd>May only be used in the FORWARD section and must be the first or the only item the list. Indicates that matching packets have been decrypted in input.</dl>
<p> <code>out</code></p>
<dl>
<dd>May only be used in the FORWARD section and must be the first or the only item in the list. Indicates that matching packets will be encrypted on output.</dl>
<p> If this column is non-empty and sections are not used, then:</p>
<dl>
<dd>&bull; A chain NAME appearing in the ACTION column must be a chain branched either directly or indirectly from the <code>accipsecin</code> or <code>accipsecout</code> chain.</dl>
<dl>
<dd>&bull; The CHAIN column must contain either <code>accipsecin</code> or <code>accipsecout</code> or a chain branched either directly or indirectly from those chains.</dl>
<dl>
<dd>&bull; These rules will NOT appear in the <code>accounting</code> chain.</dl>
</dl>
<p> <code>HEADERS &#8211; [!][any:|exactly:]</code><i>header-list </i>(Optional &#8211; Added in Shorewall 4.4.15)</p>
<dl>
<dd>The <i>header-list</i> consists of a comma-separated list of headers from the following list. <code>auth</code>, <code>ah</code>, or <code>51</code></p>
<dl>
<dd>Authentication Headers extension header.</dl>
<p> <code>esp</code>, or <code>50</code></p>
<dl>
<dd>Encrypted Security Payload extension header.</dl>
<p> <code>hop</code>, <code>hop-by-hop</code> or <code>0</code></p>
<dl>
<dd>Hop-by-hop options extension header.</dl>
<p> <code>route</code>, <code>ipv6-route</code> or <code>41</code></p>
<dl>
<dd>IPv6 Route extension header.</dl>
<p> <code>frag</code>, <code>ipv6-frag</code> or <code>44</code></p>
<dl>
<dd>IPv6 fragmentation extension header.</dl>
<p> <code>none</code>, <code>ipv6-nonxt</code> or <code>59</code></p>
<dl>
<dd>No next header</dl>
<p> <code>proto</code>, <code>protocol</code> or <code>255</code></p>
<dl>
<dd>Any protocol header.</dl>
<p> If <code>any:</code> is specified, the rule will match if any of the listed headers are present. If <code>exactly:</code> is specified, the will match packets that exactly include all specified headers. If neither is given, <code>any:</code> is assumed. If <code>!</code> is entered, the rule will match those packets which would not be matched when <code>!</code> is omitted.</dl>
<p> In all of the above columns except <code>ACTION</code> and <code>CHAIN</code>, the values <code>&#8211;</code>, <code>any</code> and <code>all</code> may be used as wildcards. Omitted trailing columns are also treated as wildcards.</p>
<h2>Files</h2>
<p>/etc/shorewall6/accounting</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/Accounting.html">http://www.shorewall.net/Accounting.html</a></code>m[]<font SIZE="-2">[2]</font> </p>
<p> m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/shorewall_logging.html">http://www.shorewall.net/shorewall_logging.html</a></code>m[]<font SIZE="-2">[3]</font> </p>
<p> m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[]<font SIZE="-2">[4]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall6/">shorewall6</a>(8), <a href="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5), <a href="/docs/linux/man/5-shorewall6-blacklist/">shorewall6-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall6-hosts/">shorewall6-hosts</a>(5), <a href="/docs/linux/man/5-shorewall6-interfaces/">shorewall6-interfaces</a>(5), <a href="/docs/linux/man/5-shorewall6-maclist/">shorewall6-maclist</a>(5), <a href="/docs/linux/man/5-shorewall6-netmap/">shorewall6-netmap</a>(5),<a href="/docs/linux/man/5-shorewall6-params/">shorewall6-params</a>(5), <a href="/docs/linux/man/5-shorewall6-policy/">shorewall6-policy</a>(5), <a href="/docs/linux/man/5-shorewall6-providers/">shorewall6-providers</a>(5), <a href="/docs/linux/man/5-shorewall6-rtrules/">shorewall6-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall6-routestopped/">shorewall6-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall6-rules/">shorewall6-rules</a>(5), <a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5), <a href="/docs/linux/man/5-shorewall6-secmarks/">shorewall6-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall6-tcclasses/">shorewall6-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall6-tcdevices/">shorewall6-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall6-mangle/">shorewall6-mangle</a>(5), <a href="/docs/linux/man/5-shorewall6-tos/">shorewall6-tos</a>(5), <a href="/docs/linux/man/5-shorewall6-tunnels/">shorewall6-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall6-zones/">shorewall6-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>rules file</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-rules.html">http://www.shorewall.net/manpages6/shorewall6-rules.html</a></dl>
<dt> 2.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/Accounting.html">http://www.shorewall.net/Accounting.html</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/Accounting.html">http://www.shorewall.net/Accounting.html</a></dl>
<dt> 3.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/shorewall_logging.html">http://www.shorewall.net/shorewall_logging.html</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/shorewall_logging.html">http://www.shorewall.net/shorewall_logging.html</a></dl>
<dt> 4.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dl>
