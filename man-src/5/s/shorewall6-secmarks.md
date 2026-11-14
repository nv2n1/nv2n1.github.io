---
title: "shorewall6-secmarks(5)"
name: "shorewall6-secmarks"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall6-secmarks/"
description: "secmarks – Shorewall6 file"
---

<p>secmarks &#8211; Shorewall6 file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall6/secmarks</code></dl>
<h2>Description</h2>
<dl>
<dd>
<dd><font SIZE="+1"> <code>Important</code> </font></p>
<dd>
<dd>Unlike rules in the m[blue]<code>shorewall6-rules</code>m[]<font SIZE="-2">[1]</font>(5) file, evaluation of rules in this file will continue after a match. So the final secmark for each packet will be the one assigned by the LAST rule that matches.  The secmarks file is used to associate an SELinux context with packets. It was added in Shorewall6 version 4.4.13. The columns in the file are as follows (where the column name is followed by a different name in parentheses, the different name is used in the alternate specification syntax). <code>SECMARK &#8211; {SAVE|RESTORE|</code><i>context</i><code>|?COMMENT}</code></p>
<dl>
<dd><code>SAVE</code></p>
<dl>
<dd>If an SELinux context is associated with the packet, the context is saved in the connection. Normally, the remaining columns should be left blank.</dl>
<p> <code>RESTORE</code></p>
<dl>
<dd>If an SELinux context is not currently associated with the packet, then the saved context (if any) is associated with the packet. Normally, the remaining columns should be left blank.</dl>
<p> <i>context</i></p>
<dl>
<dd>An SELinux context.</dl>
<p> ?COMMENT</p>
<dl>
<dd>The remainder of the line is treated as a comment which is attached to subsequent rules until another ?COMMENT line is found or until the end of the file is reached. To stop adding comments to rules, use a line with only the word ?COMMENT.</dl>
</dl>
<p> <code>CHAIN &#8211; {P|I|F|O|T}[:{N|I|U|IU|NI|NU|NIU|NUI:E|ER}]</code></p>
<dl>
<dd>This column determines the CHAIN where the SELinux context is to be applied:</p>
<dl>
<dd>P &#8211; PREROUTING</dl>
<dl>
<dd>I &#8211; INPUT</dl>
<dl>
<dd>F &#8211; FORWARD</dl>
<dl>
<dd>O &#8211; OUTPUT</dl>
<dl>
<dd>T &#8211; POSTROUTING</dl>
<p> It may be optionally followed by a colon and an indication of the Netfilter connection state(s) at which the context is to be applied:</p>
<dl>
<dd>:N &#8211; NEW connection</dl>
<dl>
<dd>:I &#8211; INVALID connection</dl>
<dl>
<dd>:NI &#8211; NEW or INVALID connection</dl>
<dl>
<dd>:E &#8211; ESTABLISHED connection</dl>
<dl>
<dd>:ER &#8211; ESTABLISHED or RELATED connection</dl>
<p> Beginning with Shorewall 4.5.10, the following additional options are available</p>
<dl>
<dd>:U &#8211; UNTRACKED connection</dl>
<dl>
<dd>:IU &#8211; INVALID or UNTRACKED connection</dl>
<dl>
<dd>:NU &#8211; NEW or UNTRACKED connection</dl>
<dl>
<dd>:NIU &#8211; NEW, INVALID or UNTRACKED connection.</dl>
<p> This column was formerly labelled CHAIN:STATE.</dl>
<p> <code>SOURCE</code> &#8211; {<code>&#8211;</code><i>interface</i>|[<i>interface</i>:]<i>address-or-range</i>[<code>,</code><i>address-or-range</i>]&#8230;}[<i>exclusion</i>]</p>
<dl>
<dd>May be:</p>
<dl>
<dd>1. An interface name &#8211; matches traffic entering the firewall on the specified interface. May not be used in classify rules or in rules using the T in the CHAIN column.</dl>
<dl>
<dd>2. A comma-separated list of host or network IP addresses or MAC addresses.</dl>
<dl>
<dd>3. An interface name followed by a colon (&quot;:&quot;) followed by a comma-separated list of host or network IP addresses or MAC addresses.</dl>
<p> MAC addresses must be prefixed with &quot;~&quot; and use &quot;-&quot; as a separator. Example: ~00-A0-C9-15-39-78 You may exclude certain hosts from the set already defined through use of an <i>exclusion</i> (see m[blue]<code>shorewall6-exclusion</code>m[]<font SIZE="-2">[2]</font>(5)).</dl>
<p> <code>DEST</code> &#8211; {<code>&#8211;</code>|{<i>interface</i>|[<i>interface</i>:]<i>address-or-range</i>[<code>,</code><i>address-or-range</i>]&#8230;}[<i>exclusion</i>]</p>
<dl>
<dd>May be:</p>
<dl>
<dd>1. An interface name. May not be used in the PREROUTING or INPUT chains. The interface name may be optionally followed by a colon (&quot;:&quot;) and an IP address list.</dl>
<dl>
<dd>2. A comma-separated list of host or network IP addresses. The list may include ip address ranges if your kernel and iptables include iprange support.</dl>
<p> You may exclude certain hosts from the set already defined through use of an <i>exclusion</i> (see m[blue]<code>shorewall6-exclusion</code>m[]<font SIZE="-2">[2]</font>(5)).</dl>
<p> <code>PROTO</code> &#8211; {<code>&#8211;</code>|<code>tcp:syn</code>|<code>ipp2p</code>|<code>ipp2p:udp</code>|<code>ipp2p:all</code>|<i>protocol-number</i>|<i>protocol-name</i>|<code>all}</code></p>
<dl>
<dd>Protocol &#8211; <code>ipp2p</code> requires ipp2p match support in your kernel and iptables. Beginning with Shorewall 4.5.12, this column can accept a comma-separated list of protocols.</dl>
<p> <code>DPORT</code> &#8211; [<code>&#8211;</code>|<i>port-name-number-or-range</i>[<code>,</code><i>port-name-number-or-range</i>]&#8230;]</p>
<dl>
<dd>Optional destination Ports. A comma-separated list of Port names (from <a href="/docs/linux/man/5-services/">services</a>(5)), <i>port number</i>s or <i>port range</i>s; if the protocol is <code>icmp</code>, this column is interpreted as the destination icmp-type(s). ICMP types may be specified as a numeric type, a numeric type and code separated by a slash (e.g., 3/4), or a typename. See m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#ICMP">http://www.shorewall.net/configuration_file_basics.htm#ICMP</a></code>m[]<font SIZE="-2">[3]</font>. If the protocol is <code>ipp2p</code>, this column is interpreted as an ipp2p option without the leading &quot;&#8211;&quot; (example <code>bit</code> for bit-torrent). If no PORT is given, <code>ipp2p</code> is assumed. This column is ignored if PROTO = all but must be entered if any of the following field is supplied. In that case, it is suggested that this field contain &quot;-&quot;</dl>
<p> <code>SPORT</code> &#8211; [<code>&#8211;</code>|<i>port-name-number-or-range</i>[<code>,</code><i>port-name-number-or-range</i>]&#8230;]</p>
<dl>
<dd>Optional source port(s). If omitted, any source port is acceptable. Specified as a comma-separated list of port names, port numbers or port ranges. Beginning with Shorewall 4.5.15, you may place &#8216;=&#8217; in this column, provided that the DPORT column is non-empty. This causes the rule to match when either the source port or the destination port in a packet matches one of the ports specified in DPORT. Use of &#8216;=&#8217; requires multi-port match in your iptables and kernel.</dl>
<p> <code>USER</code> &#8211; [<code>!</code>][<i>user-name-or-number</i>][<code>:</code><i>group-name-or-number</i>]</p>
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
<p> This column was formerly labelled USER/GROUP.</dl>
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
<h2>Example</h2>
<p>Mark the first incoming packet of a connection on the loopback interface and destined for address ::1 and tcp port 3306 with context system_u:object_r:mysqld_t:s0 and save that context in the conntrack table. On subsequent input packets in the connection, set the context from the conntrack table. </p>
<p> /etc/shorewall6/interfaces: </p>
<dl>
<dd>
<pre>#ZONE INTERFACE BROADCAST OPTIONS
- lo - ignore</pre>
</dl>
<p> /etc/shorewall6/secmarks: </p>
<dl>
<dd>
<pre>#SECMARK CHAIN SOURCE DEST PROTO DPORT SPORT USER MARK
system_u:object_r:mysqld_packet_t:s0 I:N lo ::1 tcp 3306
SAVE I:N
RESTORE I:ER</pre>
</dl>
<h2>Files</h2>
<p>/etc/shorewall6/secmarks</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://james-morris.livejournal.com/11010.html">http://james-morris.livejournal.com/11010.html</a></code>m[] </p>
<p> m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[]<font SIZE="-2">[4]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall6/">shorewall6</a>(8), <a href="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5), <a href="/docs/linux/man/5-shorewall6-blacklist/">shorewall6-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall6-hosts/">shorewall6-hosts</a>(5), <a href="/docs/linux/man/5-shorewall6-interfaces/">shorewall6-interfaces</a>(5), <a href="/docs/linux/man/5-shorewall6-maclist/">shorewall6-maclist</a>(5), <a href="/docs/linux/man/5-shorewall6-netmap/">shorewall6-netmap</a>(5),<a href="/docs/linux/man/5-shorewall6-params/">shorewall6-params</a>(5), <a href="/docs/linux/man/5-shorewall6-policy/">shorewall6-policy</a>(5), <a href="/docs/linux/man/5-shorewall6-providers/">shorewall6-providers</a>(5), <a href="/docs/linux/man/5-shorewall6-rtrules/">shorewall6-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall6-routestopped/">shorewall6-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall6-rules/">shorewall6-rules</a>(5), <a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5), <a href="/docs/linux/man/5-shorewall6-tcclasses/">shorewall6-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall6-tcdevices/">shorewall6-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall6-mangle/">shorewall6-mangle</a>(5), <a href="/docs/linux/man/5-shorewall6-tos/">shorewall6-tos</a>(5), <a href="/docs/linux/man/5-shorewall6-tunnels/">shorewall6-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall6-zones/">shorewall6-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall6-rules</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-rules.html">http://www.shorewall.net/manpages6/shorewall6-rules.html</a></dl>
<dt> 2.</p>
<dd>shorewall6-exclusion</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-exclusion.html">http://www.shorewall.net/manpages6/shorewall6-exclusion.html</a></dl>
<dt> 3.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#ICMP">http://www.shorewall.net/configuration_file_basics.htm#ICMP</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#ICMP">http://www.shorewall.net/configuration_file_basics.htm#ICMP</a></dl>
<dt> 4.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dl>
