---
title: "shorewall-conntrack(5)"
name: "shorewall-conntrack"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-conntrack/"
description: "conntrack – shorewall conntrack file"
---

<p>conntrack &#8211; shorewall conntrack file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/conntrack</code></dl>
<h2>Description</h2>
<dd>The original intent of the <code>notrack</code> file was to exempt certain traffic from Netfilter connection tracking. Traffic matching entries in the file were not to be tracked. </p>
<p> The role of the file was expanded in Shorewall 4.4.27 to include all rules that can be added in the Netfilter <code>raw</code> table. In 4.5.7, the file&#8217;s name was changed to <code>conntrack</code>. </p>
<p> The file supports three different column layouts: FORMAT 1, FORMAT 2, and FORMAT 3, FORMAT 1 being the default. The three differ as follows: </p>
<dl>
<dd>&bull; in FORMAT 2 and 3, there is an additional leading ACTION column.</dl>
<dl>
<dd>&bull; in FORMAT 3, the SOURCE column accepts no zone name; rather the ACTION column allows a SUFFIX that determines the chain(s) that the generated rule will be added to.</dl>
<p> When an entry in the following form is encountered, the format of the following entries are assumed to be of the specified <i>format</i>.</p>
<dl>
<dd><code>?FORMAT</code><br />
<i>format</i></dl>
<p> where <i>format</i> is either <code>1</code>,<code>2</code> or <code>3</code>. </p>
<p> Format 3 was introduced in Shorewall 4.5.10. </p>
<p> Comments may be attached to Netfilter rules generated from entries in this file through the use of ?COMMENT lines. These lines begin with ?COMMENT; the remainder of the line is treated as a comment which is attached to subsequent rules until another ?COMMENT line is found or until the end of the file is reached. To stop adding comments to rules, use a line containing only ?COMMENT. </p>
<p> The columns in the file are as follows (where the column name is followed by a different name in parentheses, the different name is used in the alternate specification syntax). </p>
<p> <code>ACTION</code> &#8211; {<code>NOTRACK</code>|<code>CT</code>:<code>helper</code>:<i>name</i>[(<i>arg</i>=<i>val</i>[,&#8230;])|<code>CT:ctevents:</code><i>event</i><code>[,&#8230;]|CT:expevents:new</code><code>|CT:notrack</code>|DROP|LOG|ULOG(<i>ulog-parameters</i>):NFLOG(<i>nflog-parameters</i>)|IPTABLES(<i>target</i>)}[<i>log-level</i>[:<i>log-tag</i>]][:<i>chain-designator</i>]</p>
<dl>
<dd>This column is only present when FORMAT &gt;= 2. Values other than NOTRACK or DROP require CT Targetsupport in your iptables and kernel. </p>
<dl>
<dd>&bull; <code>NOTRACK</code> or <code>CT:notrack</code> </p>
<p> Disables connection tracking for this packet. If a <i>log-level</i> is specified, the packet will also be logged at that level.</dl>
<dl>
<dd>&bull; <code>CT:helper</code>:<i>name</i> </p>
<p> Attach the helper identified by the <i>name</i> to this connection. This is more flexible than loading the conntrack helper with preset ports. If a <i>log-level</i> is specified, the packet will also be logged at that level. Beginning with Shorewall 4.6.10, the helper name is optional </p>
<p> At this writing, the available helpers are: </p>
<p> amanda</p>
<dl>
<dd>Requires that the amanda netfilter helper is present.</dl>
<p> ftp</p>
<dl>
<dd>Requires that the FTP netfilter helper is present.</dl>
<p> irc</p>
<dl>
<dd>Requires that the IRC netfilter helper is present.</dl>
<p> netbios-ns</p>
<dl>
<dd>Requires that the netbios_ns (sic) helper is present.</dl>
<p> RAS and Q.931</p>
<dl>
<dd>These require that the H323 netfilter helper is present.</dl>
<p> pptp</p>
<dl>
<dd>Requires that the pptp netfilter helper is present.</dl>
<p> sane</p>
<dl>
<dd>Requires that the SANE netfilter helper is present.</dl>
<p> sip</p>
<dl>
<dd>Requires that the SIP netfilter helper is present.</dl>
<p> snmp</p>
<dl>
<dd>Requires that the SNMP netfilter helper is present.</dl>
<p> tftp</p>
<dl>
<dd>Requires that the TFTP netfilter helper is present.</dl>
<p> May be followed by an option list of <i>arg</i>=<i>val</i> pairs in parentheses: </p>
<dl>
<dd>&bull; <code>ctevents</code>=<i>event</i>[,&#8230;] </p>
<p> Only generate the specified conntrack events for this connection. Possible event types are: <code>new</code>, <code>related</code>, <code>destroy</code>, <code>reply</code>, <code>assured</code>, <code>protoinfo</code>, <code>helper</code>, <code>mark</code> (this is connection mark, not packet mark), <code>natseqinfo</code>, and <code>secmark</code>. If more than one <i>event</i> is listed, the <i>event</i> list must be enclosed in parentheses (e.g., ctevents=(new,related)).</dl>
<dl>
<dd>&bull; <code>expevents</code><code>=new</code> </p>
<p> Only generate a <code>new</code> expectation events for this connection.</dl>
</dl>
<dl>
<dd>&bull; ctevents:<i>event</i>[,&#8230;] </p>
<p> Added in Shorewall 4.6.10. Only generate the specified conntrack events for this connection. Possible event types are: <code>new</code>, <code>related</code>, <code>destroy</code>, <code>reply</code>, <code>assured</code>, <code>protoinfo</code>, <code>helper</code>, <code>mark</code> (this is connection mark, not packet mark), <code>natseqinfo</code>, and <code>secmark</code>.</dl>
<dl>
<dd>&bull; expevents=new </p>
<p> Added in Shorewall 4.6.10. Only generate <code>new</code> expectation events for this connection.</dl>
<dl>
<dd>&bull; <code>DROP</code> </p>
<p> Added in Shorewall 4.5.10. Silently discard the packet. If a <i>log-level</i> is specified, the packet will also be logged at that level.</dl>
<dl>
<dd>&bull; <code>IPTABLES</code>(<i>target</i>) </p>
<p> Added in Shorewall 4.6.0. Allows you to specify any iptables <i>target</i> with target options (e.g., &quot;IPTABLES(AUDIT &#8211;type drop)&quot;). If the target is not one recognized by Shorewall, the following error message will be issued:</p>
<dl>
<dd>ERROR: Unknown target<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(<i>target</i>)</dl>
<p> This error message may be eliminated by adding <i>target</i> as a builtin action in m[blue]<code>shorewall-actions</code>m[]<font SIZE="-2">[1]</font>(5).</dl>
<dl>
<dd>&bull; <code>LOG</code> </p>
<p> Added in Shoreawll 4.6.0. Logs the packet using the specified <i>log-level</i> and<i> log-tag </i>(if any). If no log-level is specified, then &#8216;info&#8217; is assumed.</dl>
<dl>
<dd>&bull; <code>NFLOG</code> </p>
<p> Added in Shoreawll 4.6.0. Queues the packet to a backend logging daemon using the NFLOG netfilter target with the specified <i>nflog-parameters</i>.</dl>
<dl>
<dd>&bull; <code>ULOG</code> </p>
<p> Added in Shoreawll 4.6.0. Queues the packet to a backend logging daemon using the ULOG netfilter target with the specified <i>ulog-parameters</i>.</dl>
<p> When FORMAT = 1, this column is not present and the rule is processed as if NOTRACK had been entered in this column. </p>
<p> Beginning with Shorewall 4.5.10, when FORMAT = 3, this column can end with a colon followed by a <i>chain-designator</i>. The <i>chain-designator</i> can be one of the following: </p>
<p> P</p>
<dl>
<dd>The rule is added to the raw table PREROUTING chain. This is the default if no <i>chain-designator</i> is present.</dl>
<p> O</p>
<dl>
<dd>The rule is added to the raw table OUTPUT chain.</dl>
<p> PO or OP</p>
<dl>
<dd>The rule is added to the raw table PREROUTING and OUTPUT chains.</dl>
</dl>
<p> SOURCE (formats 1 and 2) &#8211; {<i>zone</i>[:<i>interface</i>][:<i>address-list</i>]}</p>
<dl>
<dd>where <i>zone</i> is the name of a zone, <i>interface</i> is an interface to that zone, and <i>address-list</i> is a comma-separated list of addresses (may contain exclusion &#8211; see m[blue]<code>shorewall-exclusion</code>m[]<font SIZE="-2">[2]</font> (5)). </p>
<p> Beginning with Shorewall 4.5.7, <code>all</code> can be used as the <i>zone</i> name to mean all zones. </p>
<p> Beginning with Shorewall 4.5.10, <code>all-</code> can be used as the <i>zone</i> name to mean all off-firewall zones.</dl>
<p> SOURCE (format 3) &#8211; {-|<i>interface</i>[:<i>address-list</i>]|<i>address-list</i>}</p>
<dl>
<dd>Where <i>interface</i> is an interface to that zone, and <i>address-list</i> is a comma-separated list of addresses (may contain exclusion &#8211; see m[blue]<code>shorewall-exclusion</code>m[]<font SIZE="-2">[2]</font> (5)).</dl>
<p> DEST &#8211; {-|<i>interface</i>[:<i>address-list</i>]|<i>address-list</i>}</p>
<dl>
<dd>where <i>address-list</i> is a comma-separated list of addresses (may contain exclusion &#8211; see m[blue]<code>shorewall-exclusion</code>m[]<font SIZE="-2">[2]</font> (5)).</dl>
<p> PROTO &#8211; <i>protocol-name-or-number</i>[,&#8230;]</p>
<dl>
<dd>A protocol name from /etc/protocols or a protocol number. </p>
<p> Beginning with Shorewall 4.5.12, this column is labeled <code>PROTOS</code> and can accept a comma-separated list of protocols. Either <code>proto</code> or <code>protos</code> is accepted in the alternate input format.</dl>
<p> DPORT &#8211; port-number/service-name-list</p>
<dl>
<dd>A comma-separated list of port numbers and/or service names from /etc/services. May also include port ranges of the form <i>low-port</i>:<i>high-port</i> if your kernel and iptables include port range support. </p>
<p> This column was formerly labelled DEST PORT(S).</dl>
<p> SPORT &#8211; port-number/service-name-list</p>
<dl>
<dd>A comma-separated list of port numbers and/or service names from /etc/services. May also include port ranges of the form <i>low-port</i>:<i>high-port</i> if your kernel and iptables include port range support. </p>
<p> Beginning with Shorewall 4.5.15, you may place &#8216;=&#8217; in this column, provided that the DPORT column is non-empty. This causes the rule to match when either the source port or the destination port in a packet matches one of the ports specified in DPORT. Use of &#8216;=&#8217; requires multi-port match in your iptables and kernel. </p>
<p> This column was formerly labelled SOURCE PORT(S).</dl>
<p> USER &#8211; [<i>user</i>][:<i>group</i>]</p>
<dl>
<dd>This column was formerly named USER/GROUP and may only be specified if the SOURCE <i>zone</i> is $FW. Specifies the effective user id and or group id of the process sending the traffic.</dl>
<p> <code>SWITCH &#8211; [!]</code><i>switch-name</i><code>[={0|1}]</code></p>
<dl>
<dd>Added in Shorewall 4.5.10 and allows enabling and disabling the rule without requiring <code>shorewall restart</code>. </p>
<p> The rule is enabled if the value stored in /proc/net/nf_condition/<i>switch-name</i> is 1. The rule is disabled if that file contains 0 (the default). If &#8216;!&#8217; is supplied, the test is inverted such that the rule is enabled if the file contains 0. </p>
<p> Within the <i>switch-name</i>, &#8216;@0&#8217; and &#8216;@{0}&#8217; are replaced by the name of the chain to which the rule is a added. The <i>switch-name</i> (after &#8216;&#8230;&#8217; expansion) must begin with a letter and be composed of letters, decimal digits, underscores or hyphens. Switch names must be 30 characters or less in length. </p>
<p> Switches are normally <code>off</code>. To turn a switch <code>on</code>:</p>
<dl>
<dd><code>echo 1 &gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/proc/net/nf_condition/</code><i>switch-name</i></dl>
<p> To turn it <code>off</code> again:</p>
<dl>
<dd><code>echo 0 &gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/proc/net/nf_condition/</code><i>switch-name</i></dl>
<p> Switch settings are retained over <code>shorewall restart</code>. </p>
<p> When the <i>switch-name</i> is followed by <code>=0</code> or <code>=1</code>, then the switch is initialized to off or on respectively by the <code>start</code> command. Other commands do not affect the switch setting.</dl>
<h2>Example</h2>
<p>Example 1: </p>
<dl>
<dd>
<pre>#ACTION SOURCE DEST PROTO DPORT SPORT USER
CT:helper:ftp(expevents=new) fw - tcp 21 </pre>
</dl>
<p> Example 2 (Shorewall 4.5.10 or later): </p>
<p> Drop traffic to/from all zones to IP address 1.2.3.4 </p>
<dl>
<dd>
<pre>FORMAT 2
#ACTION SOURCE DEST PROTO DPORT SPORT USER
DROP all-:1.2.3.4 -
DROP all 1.2.3.4</pre>
</dl>
<p> or </p>
<dl>
<dd>
<pre>FORMAT 3
#ACTION SOURCE DEST PROTO DPORT SPORT USER
DROP:P 1.2.3.4 -
DROP:PO - 1.2.3.4</pre>
</dl>
<h2>Files</h2>
<p>/etc/shorewall/conntrack</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[]<font SIZE="-2">[3]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall_interfaces/">shorewall_interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-rtrules/">shorewall-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-secmarks/">shorewall-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-mangle/">shorewall-mangle</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall-actions</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-actions.html">http://www.shorewall.net/manpages/shorewall-actions.html</a></dl>
<dt> 2.</p>
<dd>shorewall-exclusion</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-exclusion.html">http://www.shorewall.net/manpages/shorewall-exclusion.html</a></dl>
<dt> 3.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dl>
