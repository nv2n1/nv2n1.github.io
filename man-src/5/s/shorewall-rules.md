---
title: "shorewall-rules(5)"
name: "shorewall-rules"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-rules/"
description: "rules – Shorewall rules file"
---

<p>rules &#8211; Shorewall rules file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/rules</code></dl>
<h2>Description</h2>
<dd>Entries in this file govern connection establishment by defining exceptions to the policies laid out in m[blue]<code>shorewall-policy</code>m[]<font SIZE="-2">[1]</font>(5). By default, subsequent requests and responses are automatically allowed using connection tracking. For any particular (source,dest) pair of zones, the rules are evaluated in the order in which they appear in this file and the first terminating match is the one that determines the disposition of the request. All rules are terminating except LOG and COUNT rules.</p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 If you masquerade or use SNAT from a local system to the internet, you cannot use an ACCEPT rule to allow traffic from the internet to that system. You <code>must</code> use a DNAT rule instead.  The rules file is divided into sections. Each section is introduced by a &quot;Section Header&quot; which is a line beginning with ?SECTION and followed by the section name. Sections are as follows and must appear in the order listed: <code>ALL</code></p>
<dl>
<dd>This section was added in Shorewall 4.4.23. Rules in this section are applied, regardless of the connection tracking state of the packet.</dl>
<p> <code>ESTABLISHED</code></p>
<dl>
<dd>Packets in the ESTABLISHED state are processed by rules in this section. The only ACTIONs allowed in this section are ACCEPT, DROP, REJECT, LOG and QUEUE There is an implicit ACCEPT rule inserted at the end of this section.</dl>
<p> <code>RELATED</code></p>
<dl>
<dd>Packets in the RELATED state are processed by rules in this section. The only ACTIONs allowed in this section are ACCEPT, DROP, REJECT, LOG and QUEUE There is an implicit rule added at the end of this section that invokes the RELATED_DISPOSITION (m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font>(5)).</dl>
<p> <code>INVALID</code></p>
<dl>
<dd>Added in Shorewall 4.5.13. Packets in the INVALID state are processed by rules in this section. The only Actions allowed in this section are ACCEPT, DROP, REJECT, LOG and QUEUE. There is an implicit rule added at the end of this section that invokes the INVALID_DISPOSITION (m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font>(5)).</dl>
<p> <code>UNTRACKED</code></p>
<dl>
<dd>Added in Shorewall 4.5.13. Packets in the UNTRACKED state are processed by rules in this section. The only Actions allowed in this section are ACCEPT, DROP, REJECT, LOG and QUEUE. There is an implicit rule added at the end of this section that invokes the UNTRACKED_DISPOSITION (m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font>(5)).</dl>
<p> <code>NEW</code></p>
<dl>
<dd>Packets in the NEW state are processed by rules in this section. If the INVALID and/or UNTRACKED sections are empty or not included, then the packets in the corresponding state(s) are also processed in this section.</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 If you are not familiar with Netfilter to the point where you are comfortable with the differences between the various connection tracking states, then it is suggested that you omit the <code>ESTABLISHED</code> and <code>RELATED</code> sections and place all of your non-blacklisting rules in the NEW section (That&#8217;s after the line that reads ?SECTION NEW&#8217;). </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 If you specify FASTACCEPT=Yes in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font>(5) then the <code>ALL, ESTABLISHED</code> and <code>RELATED</code> sections must be empty. An except is made if you are running Shorewall 4.4.27 or later and you have specified a non-default value for RELATED_DISPOSITION or RELATED_LOG_LEVEL. In that case, you may have rules in the RELATED section of this file.  You may omit any section that you don&#8217;t need. If no Section Headers appear in the file then all rules are assumed to be in the NEW section. When defining rules that rewrite the destination IP address and/or port number (namely DNAT and REDIRECT rules), it is important to keep straight which columns in the file specify the packet before rewriting and which specify how the packet will look after rewriting.</p>
<dl>
<dd>&bull; The DEST column specifies the final destination for the packet after rewriting and can include the final IP address and/or port number.</dl>
<dl>
<dd>&bull; The remaining columns specify characteristics of the packet before rewriting. In particular, the ORIGDEST column gives the original destination IP address of the packet and the DPORT column give the original destination port(s).</dl>
<p> The columns in the file are as follows (where the column name is followed by a different name in parentheses, the different name is used in the alternate specification syntax). <code>ACTION</code> &#8211; <i>target</i><code>[:</code>{<i>log-level</i>|<code>none</code>}[<code>!</code>][<code>:</code><i>tag</i>]]</p>
<dl>
<dd>Specifies the action to be taken if the connection request matches the rule. <i>target</i> must be one of the following. <code>ACCEPT</code></p>
<dl>
<dd>Allow the connection request.</dl>
<p> <code>ACCEPT+</code></p>
<dl>
<dd>like ACCEPT but also excludes the connection from any subsequent matching <code>DNAT</code>[<code>&#8211;</code>] or <code>REDIRECT</code>[<code>&#8211;</code>] rules.</dl>
<p> <code>ACCEPT!</code></p>
<dl>
<dd>like ACCEPT but exempts the rule from being suppressed by OPTIMIZE=1 in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font>(5).</dl>
<p> <i>action</i></p>
<dl>
<dd>The name of an <i>action</i> declared in m[blue]<code>shorewall-actions</code>m[]<font SIZE="-2">[3]</font>(5) or in /usr/share/shorewall/actions.std.</dl>
<p> <code>ADD(</code><i>ipset</i><code>:</code><i>flags</i><code>[:</code><i>timeout</i><code>])</code></p>
<dl>
<dd>Added in Shorewall 4.4.12. Causes addresses and/or port numbers to be added to the named <i>ipset</i>. The <i>flags</i> specify the address or tuple to be added to the set and must match the type of ipset involved. For example, for an iphash ipset, either the SOURCE or DESTINATION address can be added using <i>flags</i><code>src</code> or <code>dst</code> respectively (see the -A command in ipset (8)). Beginning with Shorewall 5.0.3, an optional <i>timeout</i> can be specified. This is the number of seconds that the new entry in the ipset is to remain valid and overrides any timeout specified when the ipset was created. ADD is non-terminating. Even if a packet matches the rule, it is passed on to the next rule.</dl>
<p> <code>AUDIT</code>[(accept|drop|reject)]</p>
<dl>
<dd>Added in Shorewall 4.5.10. Audits the packet with the specified type; if the type is omitted, then <code>drop</code> is assumed. Require AUDIT_TARGET support in the kernel and iptables.</dl>
<p> <code>A_ACCEPT</code>, <code>A_ACCEPT</code><code>+</code> and <code>A_ACCEPT</code><code>!</code></p>
<dl>
<dd>Added in Shorewall 4.4.20. Audited versions of ACCEPT, ACCEPT+ and ACCEPT! respectively. Require AUDIT_TARGET support in the kernel and iptables.</dl>
<p> <code>A_DROP</code> and<code> A_DROP!</code></p>
<dl>
<dd>Added in Shorewall 4.4.20. Audited versions of DROP and DROP! respectively. Require AUDIT_TARGET support in the kernel and iptables.</dl>
<p> <code>A_REJECT</code> AND <code>A_REJECT!</code></p>
<dl>
<dd>Added in Shorewall 4.4.20. Audited versions of REJECT and REJECT! respectively. Require AUDIT_TARGET support in the kernel and iptables.</dl>
<p> <code>?COMMENT</code></p>
<dl>
<dd>the rest of the line will be attached as a comment to the Netfilter rule(s) generated by the following entries. The comment will appear delimited by &quot;/* &#8230; */&quot; in the output of &quot;shorewall show &lt;chain&gt;&quot;. To stop the comment from being attached to further rules, simply include ?COMMENT on a line by itself.</dl>
<p> <code>CONMARK({</code><i>mark</i><code>})</code></p>
<dl>
<dd>Added in Shorewall 5.0.7, CONNMARK is identical to MARK with the exception that the mark is assigned to connection to which the packet belongs is marked rather than to the packet itself.</dl>
<p> <code>CONTINUE</code></p>
<dl>
<dd>For experts only. Do not process any of the following rules for this (source zone,destination zone). If the source and/or destination IP address falls into a zone defined later in m[blue]<code>shorewall-zones</code>m[]<font SIZE="-2">[4]</font>(5) or in a parent zone of the source or destination zones, then this connection request will be passed to the rules defined for that (those) zone(s). See m[blue]<code>shorewall-nesting</code>m[]<font SIZE="-2">[5]</font>(5) for additional information.</dl>
<p> <code>CONTINUE!</code></p>
<dl>
<dd>like CONTINUE but exempts the rule from being suppressed by OPTIMIZE=1 in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font>(5).</dl>
<p> <code>COUNT</code></p>
<dl>
<dd>Simply increment the rule&#8217;s packet and byte count and pass the packet to the next rule.</dl>
<p> <code>DEL(</code><i>ipset</i><code>:</code><i>flags</i><code>)</code></p>
<dl>
<dd>Added in Shorewall 4.4.12. Causes an entry to be deleted from the named <i>ipset</i>. The <i>flags</i> specify the address or tuple to be deleted from the set and must match the type of ipset involved. For example, for an iphash ipset, either the SOURCE or DESTINATION address can be deleted using <i>flags</i><code>src</code> or <code>dst</code> respectively (see the -D command in ipset (8)). DEL is non-terminating. Even if a packet matches the rule, it is passed on to the next rule.</dl>
<p> <code>DNAT</code></p>
<dl>
<dd>Forward the request to another system (and optionally another port).</dl>
<p> <code>DNAT-</code></p>
<dl>
<dd>Advanced users only. Like <code>DNAT</code> but only generates the <code>DNAT</code> iptables rule and not the companion <code>ACCEPT</code> rule.</dl>
<p> <code>DROP</code></p>
<dl>
<dd>Ignore the request.</dl>
<p> <code>DROP!</code></p>
<dl>
<dd>like DROP but exempts the rule from being suppressed by OPTIMIZE=1 in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font>(5).</dl>
<p> <code>HELPER</code></p>
<dl>
<dd>Added in Shorewall 4.5.7. This action requires that the HELPER column contains the name of the Netfilter helper to be associated with connections matching this connection. May only be specified in the NEW section and is useful for being able to specify a helper when the applicable policy is ACCEPT. No destination zone should be specified in HELPER rules.</dl>
<p> <code>INLINE</code>[(<i>action</i>)]</p>
<dl>
<dd>Added in Shorewall 4.5.16. This action allows you to construct most of the rule yourself using iptables syntax. The part that you specify must follow a semicolon (&#8216;;&#8217;) and is completely free-form. If the target of the rule (the part following &#8216;j&#8217;) is something that Shorewall supports in the ACTION column, then you may enclose it in parentheses (e.g., INLINE(ACCEPT)). Otherwise, you can include it after the semicolon. In this case, you must declare the target as a builtin action in m[blue]<code>shorewall-actions</code>m[]<font SIZE="-2">[3]</font>(5). Some considerations when using INLINE:</p>
<dl>
<dd>&bull; The <code>p</code>, <code>s</code>, <code>d</code>, <code>i</code>, <code>o</code>, <code>policy</code>, and state match (<code>state</code> or <code>conntrack &#8211;ctstate</code>) matches will always appear in the front of the rule in that order.</dl>
<dl>
<dd>&bull; When multiple matches are specified, the compiler will keep them in the order in which they appear (excluding the above listed ones), but they will not necessarily be at the end of the generated rule. For example, if addresses are specified in the SOURCE and/or DEST columns, their generated matches will appear after those specified using &#8216;;&#8217;.</dl>
</dl>
<p> <code>IPTABLES</code>({<i>iptables-target</i> [<i>option</i> &#8230;])</p>
<dl>
<dd>This action allows you to specify an iptables target with options (e.g., &#8216;IPTABLES(MARK &#8211;set-xmark 0x01/0xff)&#8217;. If the <i>iptables-target</i> is not one recognized by Shorewall, the following error message will be issued:</p>
<dl>
<dd>
<pre> ERROR: Unknown target (<i>iptables-target</i>)</pre>
</dl>
<p> This error message may be eliminated by adding the <i>iptables-</i><i>target</i> as a builtin action in m[blue]<code>shorewall-actions</code>m[]<font SIZE="-2">[3]</font>(5).</p>
<dl>
<dd><font SIZE="+1"> <code>Important</code> </font><br />
 If you specify REJECT as the <i>iptables-target</i>, the target of the rule will be the iptables REJECT target and not Shorewall&#8217;s builtin &#8216;reject&#8217; chain which is used when REJECT (see below) is specified as the <i>target</i> in the ACTION column.  <code>LOG:</code><i>level</i></p>
<dl>
<dd>Simply log the packet and continue with the next rule.</dl>
<p> <i>macro</i><code>[(</code><i>macrotarget</i><code>)]</code></p>
<dl>
<dd>The name of a macro defined in a file named macro.<i>macro</i>. If the macro accepts an action parameter (Look at the macro source to see if it has PARAM in the TARGET column) then the <i>macro</i> name is followed by the parenthesized <i>macrotarget</i> (<code>ACCEPT</code>, <code>DROP</code>, <code>REJECT</code>, &#8230;) to be substituted for the parameter. Example: FTP(ACCEPT). The older syntax where the macro name and the target are separated by a slash (e.g. FTP/ACCEPT) is still allowed but is deprecated.</dl>
<p> <code>MARK({</code><i>mark</i><code>})</code></p>
<dl>
<dd>where <i>mark</i> is a packet mark value. Added in Shorewall 5.0.7, MARK requires &quot;Mark in filter table&quot; support in your kernel and iptables. Normally will set the mark value of the current packet. If preceded by a vertical bar (&quot;|&quot;), the mark value will be logically ORed with the current mark value to produce a new mark value. If preceded by an ampersand (&quot;&amp;&quot;), will be logically ANDed with the current mark value to produce a new mark value. Both &quot;|&quot; and &quot;&amp;&quot; require Extended MARK Target support in your kernel and iptables. The mark value may be optionally followed by &quot;/&quot; and a mask value (used to determine those bits of the connection mark to actually be set). When a mask is specified, the result of logically ANDing the mark value with the mask must be the same as the mark value.</dl>
<p> <code>NFLOG</code>[(<i>nflog-parameters</i>)]</p>
<dl>
<dd>Added in Shorewall 4.5.9.3. Queues matching packets to a back end logging daemon via a netlink socket then continues to the next rule. See m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/shorewall_logging.html">http://www.shorewall.net/shorewall_logging.html</a></code>m[]<font SIZE="-2">[6]</font>. The <i>nflog-parameters</i> are a comma-separated list of up to 3 numbers:</p>
<dl>
<dd>&bull; The first number specifies the netlink group (0-65535). If omitted (e.g., NFLOG(,0,10)) then a value of 0 is assumed.</dl>
<dl>
<dd>&bull; The second number specifies the maximum number of bytes to copy. If omitted, 0 (no limit) is assumed.</dl>
<dl>
<dd>&bull; The third number specifies the number of log messages that should be buffered in the kernel before they are sent to user space. The default is 1.</dl>
<p> NFLOG is similar to<code> LOG:NFLOG</code>[(<i>nflog-parameters</i>)], except that the log level is not changed when this ACTION is used in an action or macro body and the invocation of that action or macro specifies a log level.</dl>
<p> <code>NFQUEUE</code>[([<i>queuenumber</i>1[:<i>queuenumber2</i>][,bypass]]|bypass)]</p>
<dl>
<dd>Queues the packet to a user-space application using the nfnetlink_queue mechanism. If a <i>queuenumber</i>1 is not specified, queue zero (0) is assumed. Beginning with Shorewall 4.6.10, the keyword <code>bypass</code> can be given. By default, if no userspace program is listening on an NFQUEUE, then all packets that are to be queued are dropped. When this option is used, the NFQUEUE rule is silently bypassed instead. The packet will move on to the next rule. Also beginning in Shorewall 4.6.10, a second queue number (<i>queuenumber2</i>) may be specified. This specifies a range of queues to use. Packets are then balanced across the given queues. This is useful for multicore systems: start multiple instances of the userspace program on queues x, x+1, .. x+n and use &quot;x:x+n&quot;. Packets belonging to the same connection are put into the same nfqueue.</dl>
<p> <code>NFQUEUE!</code><code>[([</code><i>queuenumber1</i><code>[,</code><i>queuenumber2</i><code>][,bypass]]|bypass)]</code></p>
<dl>
<dd>like NFQUEUE but exempts the rule from being suppressed by OPTIMIZE=1 in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font>(5).</dl>
<p> <code>NONAT</code></p>
<dl>
<dd>Excludes the connection from any subsequent <code>DNAT</code>[-] or <code>REDIRECT</code>[-] rules but doesn&#8217;t generate a rule to accept the traffic.</dl>
<p> <code>QUEUE</code></p>
<dl>
<dd>Queue the packet to a user-space application such as ftwall (<a rel="nofollow" href="http://p2pwall.sf.net">http://p2pwall.sf.net</a>). The application may reinsert the packet for further processing.</dl>
<p> <code>QUEUE!</code></p>
<dl>
<dd>like QUEUE but exempts the rule from being suppressed by OPTIMIZE=1 in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font>(5).</dl>
<p> <code>REJECT[(</code><i>option</i><code>)]</code></p>
<dl>
<dd>disallow the request and return an icmp-unreachable or an RST packet. If no option is passed, Shorewall selects the appropriate option based on the protocol of the packet. Beginning with Shorewall 5.0.8, the type of reject may be specified in the <i>option</i> paramater. Valid <i>option</i> values are:</p>
<dl>
<dd><code>icmp-net-unreachable</code></dl>
<dl>
<dd><code>icmp-host-unreachable</code></dl>
<dl>
<dd><code>i</code><code>cmp-port-unreachable</code></dl>
<dl>
<dd><code>icmp-proto-unreachable</code></dl>
<dl>
<dd><code>icmp-net-prohibited</code></dl>
<dl>
<dd><code>icmp-host-prohibited</code></dl>
<dl>
<dd><code>icmp-admin-prohibited</code></dl>
<dl>
<dd><code>icmp-tcp-reset</code> (the PROTO column<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>must specify TCP)</dl>
</dl>
<p> <code>REJECT!</code></p>
<dl>
<dd>like REJECT but exempts the rule from being suppressed by OPTIMIZE=1 in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font>(5).</dl>
<p> <code>REDIRECT</code></p>
<dl>
<dd>Redirect the request to a server running on the firewall.</dl>
<p> <code>REDIRECT-</code></p>
<dl>
<dd>Advanced users only. Like <code>REDIRECT</code> but only generates the <code>REDIRECT</code> iptables rule and not the companion <code>ACCEPT</code> rule.</dl>
<p> <code>TARPIT</code> [(<code>tarpit</code> | <code>honeypot</code> | <code>reset</code>)]</p>
<dl>
<dd>Added in Shorewall 4.6.6. TARPIT captures and holds incoming TCP connections using no local per-connection resources. TARPIT only works with the PROTO column set to tcp (6), and is totally application agnostic. This module will answer a TCP request and play along like a listening server, but aside from sending an ACK or RST, no data is sent. Incoming packets are ignored and dropped. The attacker will terminate the session eventually. This module allows the initial packets of an attack to be captured by other software for inspection. In most cases this is sufficient to determine the nature of the attack. This offers similar functionality to LaBrea &lt;<a rel="nofollow" href="http://www.hackbusters.net/LaBrea/">http://www.hackbusters.net/LaBrea/</a>&gt; but does not require dedicated hardware or IPs. Any TCP port that you would normally DROP or REJECT can instead become a tarpit. The target accepts a single optional parameter: tarpit</p>
<dl>
<dd>This mode is the default and completes a connection with the attacker but limits the window size to 0, thus keeping the attacker waiting long periods of time. While he is maintaining state of the connection and trying to continue every 60-240 seconds, we keep none, so it is very lightweight. Attempts to close the connection are ignored, forcing the remote side to time out the connection in 12-24 minutes.</dl>
<p> honeypot</p>
<dl>
<dd>This mode completes a connection with the attacker, but signals a normal window size, so that the remote side will attempt to send data, often with some very nasty exploit attempts. We can capture these packets for decoding and further analysis. The module does not send any data, so if the remote expects an application level response, the game is up.</dl>
<p> reset</p>
<dl>
<dd>This mode is handy because we can send an inline RST (reset). It has no other function.</dl>
</dl>
<p> <code>ULOG</code>[(<i>ulog-parameters</i>)]</p>
<dl>
<dd>Added in Shorewall 4.5.10. Queues matching packets to a back end logging daemon via a netlink socket then continues to the next rule. See m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/shorewall_logging.html">http://www.shorewall.net/shorewall_logging.html</a></code>m[]<font SIZE="-2">[6]</font>. Similar to<code> LOG:ULOG</code>[(<i>ulog-parameters</i>)], except that the log level is not changed when this ACTION is used in an action or macro body and the invocation of that action or macro specifies a log level.</dl>
<p> The <i>target</i> may optionally be followed by &quot;:&quot; and a syslog log level (e.g, REJECT:info or Web(ACCEPT):debug). This causes the packet to be logged at the specified level. Note that if the <code>ACTION</code> involves destination network address translation (DNAT, REDIRECT, etc.) then the packet is logged <code>before</code> the destination address is rewritten. If the <code>ACTION</code> names an <i>action</i> declared in m[blue]<code>shorewall-actions</code>m[]<font SIZE="-2">[3]</font>(5) or in /usr/share/shorewall/actions.std then:</p>
<dl>
<dd>&bull; If the log level is followed by &quot;!&#8217; then all rules in the action are logged at the log level.</dl>
<dl>
<dd>&bull; If the log level is not followed by &quot;!&quot; then only those rules in the action that do not specify logging are logged at the specified level.</dl>
<dl>
<dd>&bull; The special log level <code>none!</code> suppresses logging by the action.</dl>
<p> You may also specify <code>ULOG</code> or <code>NFLOG</code> (must be in upper case) as a log level.This will log to the ULOG or NFLOG target for routing to a separate log through use of ulogd (m[blue]<code><a rel="nofollow" href="http://www.netfilter.org/projects/ulogd/index.html">http://www.netfilter.org/projects/ulogd/index.html</a></code>m[]). Actions specifying logging may be followed by a log tag (a string of alphanumeric characters) which is appended to the string generated by the LOGPREFIX (in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font>(5)). Example: ACCEPT:info:ftp would include &#8216;ftp &#8216; at the end of the log prefix generated by the LOGPREFIX setting.</dl>
<p> <code>SOURCE</code> &#8211; {<i>zone</i>|<i>zone-list</i>[+]|{<code>all</code>|<code>any</code>}[<code>+</code>][<code>&#8211;</code>]}<code>[:</code><i>interface</i>][<code>:</code>{<i>address-or-range</i>[,<i>address-or-range</i>]&#8230;[<i>exclusion</i>]|<i>exclusion</i>|<code>+</code><i>ipset</i>|<i>^countrycode-list</i>}</p>
<dl>
<dd>Source hosts to which the rule applies. May be a <i>zone</i> declared in /etc/shorewall/zones, <code>$FW</code> to indicate the firewall itself, <code>all</code>, <code>all+</code>, <code>all-</code>, <code>all+-</code> or <code>none</code>. Beginning with Shorewall 4.4.13, you may use a <i>zone-list </i>which consists of a comma-separated list of zones declared in m[blue]<code>shorewall-zones</code>m[]<font SIZE="-2">[4]</font> (5). This <i>zone-list</i> may be optionally followed by &quot;+&quot; to indicate that the rule is to apply to intra-zone traffic as well as inter-zone traffic. When <code>none</code> is used either in the <code>SOURCE</code> or <code>DEST</code> column, the rule is ignored. <code>all</code> means &quot;All Zones&quot;, including the firewall itself. <code>all-</code> means &quot;All Zones, except the firewall itself&quot;. When <code>all</code>[<code>&#8211;</code>] is used either in the <code>SOURCE</code> or <code>DEST</code> column intra-zone traffic is not affected. When <code>all+</code>[<code>&#8211;</code>] is &quot;used, intra-zone traffic is affected. Beginning with Shorewall 4.4.13, exclusion is supported &#8212; see see m[blue]<code>shorewall-exclusion</code>m[]<font SIZE="-2">[7]</font>(5). Except when <code>all</code>[<code>+</code>][<code>&#8211;</code>] or <code>any</code>[<code>+</code>][<code>&#8211;</code>] is specified, clients may be further restricted to a list of networks and/or hosts by appending &quot;:&quot; and a comma-separated list of network and/or host addresses. Hosts may be specified by IP or MAC address; mac addresses must begin with &quot;~&quot; and must use &quot;-&quot; as a separator. The above restriction on <code>all</code>[<code>+</code>][<code>&#8211;</code>] and <code>any</code>[<code>+</code>][<code>&#8211;</code>] is removed in Shorewall-4.4.13. <code>any</code> is equivalent to <code>all</code> when there are no nested zones. When there are nested zones, <code>any</code> only refers to top-level zones (those with no parent zones). Note that <code>any</code> excludes all vserver zones, since those zones are nested within the firewall zone. Beginning with Shorewall 4.4.13, exclusion is supported with <code>any</code> &#8212; see see m[blue]<code>shorewall-exclusion</code>m[]<font SIZE="-2">[7]</font>(5). Hosts may also be specified as an IP address range using the syntax <i>lowaddress</i>&#8211;<i>highaddress</i>. This requires that your kernel and iptables contain iprange match support. If your kernel and iptables have ipset match support then you may give the name of an ipset prefaced by &quot;+&quot;. The ipset name may be optionally followed by a number from 1 to 6 enclosed in square brackets ([]) to indicate the number of levels of source bindings to be matched. Beginning with Shorewall 4.4.17, the primary IP address of a firewall interface can be specified by an ampersand (&#8216;&amp;&#8217;) followed by the logical name of the interface as found in the INTERFACE column of m[blue]<code>shorewall-interfaces</code>m[]<font SIZE="-2">[8]</font> (5). Beginning with Shorewall 4.5.4, A <i>countrycode-list</i> may be specified. A countrycode-list is a comma-separated list of up to 15 two-character ISO-3661 country codes enclosed in square brackets (&#8216;[&#8230;]&#8217;) and preceded by a caret (&#8216;^&#8217;). When a single country code is given, the square brackets may be omitted. A list of country codes supported by Shorewall may be found at m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/ISO-3661.html">http://www.shorewall.net/ISO-3661.html</a></code>m[]<font SIZE="-2">[9]</font>. Specifying a <i>countrycode-list</i> requires GeoIP Match support in your iptables and Kernel. You may exclude certain hosts from the set already defined through use of an <i>exclusion</i> (see m[blue]<code>shorewall-exclusion</code>m[]<font SIZE="-2">[7]</font>(5)). Examples: dmz:192.168.2.2</p>
<dl>
<dd>Host 192.168.2.2 in the DMZ</dl>
<p> net:155.186.235.0/24</p>
<dl>
<dd>Subnet 155.186.235.0/24 on the Internet</dl>
<p> loc:192.168.1.1,192.168.1.2</p>
<dl>
<dd>Hosts 192.168.1.1 and 192.168.1.2 in the local zone.</dl>
<p> loc:~00-A0-C9-15-39-78</p>
<dl>
<dd>Host in the local zone with MAC address 00:A0:C9:15:39:78.</dl>
<p> net:192.0.2.11-192.0.2.17</p>
<dl>
<dd>Hosts 192.0.2.11-192.0.2.17 in the net zone.</dl>
<p> net:!192.0.2.11-192.0.2.17</p>
<dl>
<dd>All hosts in the net zone except for 192.0.2.11-192.0.2.17.</dl>
<p> net:155.186.235.0/24!155.186.235.16/28</p>
<dl>
<dd>Subnet 155.186.235.0/24 on the Internet except for 155.186.235.16/28</dl>
<p> $FW:&amp;eth0</p>
<dl>
<dd>The primary IP address of eth0 in the firewall zone (Shorewall 4.4.17 and later).</dl>
<p> loc,dmz</p>
<dl>
<dd>Both the <code>loc</code> and <code>dmz</code> zones.</dl>
<p> all!dmz</p>
<dl>
<dd>All but the <code>dmz</code> zone.</dl>
</dl>
<p> <code>DEST</code> &#8211; {<i>zone</i>|<i>zone-list</i>[+]|{<code>all</code>|<code>any</code>}[<code>+</code>][<code>&#8211;</code>]}<code>[:{</code><i>interface</i>|<i>address-or-range</i>[,<i>address-or-range</i>]&#8230;[<i>exclusion</i>]|<i>exclusion</i>|<code>+</code><i>ipset</i>|<i>^countrycode-list</i>}][<code>:</code><i>port</i>[:<code>random</code>]]</p>
<dl>
<dd>Location of Server. May be a zone declared in m[blue]<code>shorewall-zones</code>m[]<font SIZE="-2">[4]</font>(5), $<code>FW</code> to indicate the firewall itself, <code>all</code>. <code>all+</code> or <code>none</code>. Beginning with Shorewall 4.4.13, you may use a <i>zone-list </i>which consists of a comma-separated list of zones declared in m[blue]<code>shorewall-zones</code>m[]<font SIZE="-2">[4]</font> (5). This <i>zone-list</i> may be optionally followed by &quot;+&quot; to indicate that the rule is to apply to intra-zone traffic as well as inter-zone traffic. Beginning with Shorewall 4.5.4, A <i>countrycode-list</i> may be specified. A countrycode-list is a comma-separated list of up to 15 two-character ISO-3661 country codes enclosed in square brackets (&#8216;[&#8230;]&#8217;) and preceded by a caret (&#8216;^&#8217;). When a single country code is given, the square brackets may be omitted. A list of country codes supported by Shorewall may be found at m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/ISO-3661.html">http://www.shorewall.net/ISO-3661.html</a></code>m[]<font SIZE="-2">[9]</font>. Specifying a <i>countrycode-list</i> requires GeoIP Match support in your iptables and Kernel. When <code>none</code> is used either in the <code>SOURCE</code> or <code>DEST</code> column, the rule is ignored. <code>all</code> means &quot;All Zones&quot;, including the firewall itself. <code>all-</code> means &quot;All Zones, except the firewall itself&quot;. When <code>all</code>[<code>&#8211;</code>] is used either in the <code>SOURCE</code> or <code>DEST</code> column intra-zone traffic is not affected. When <code>all+</code>[<code>&#8211;</code>] is &quot;used, intra-zone traffic is affected. Beginning with Shorewall 4.4.13, exclusion is supported &#8212; see see m[blue]<code>shorewall6-exclusion</code>m[]<font SIZE="-2">[10]</font>(5). <code>any</code> is equivalent to <code>all</code> when there are no nested zones. When there are nested zones, <code>any</code> only refers to top-level zones (those with no parent zones). Note that <code>any</code> excludes all vserver zones, since those zones are nested within the firewall zone. Except when <code>all</code>[<code>+</code>][<code>&#8211;</code>] or <code>any</code>[<code>+</code>][<code>&#8211;</code>] is specified, clients may be further restricted to a list of networks and/or hosts by appending &quot;:&quot; and a comma-separated list of network and/or host addresses. Hosts may be specified by IP or MAC address; mac addresses must begin with &quot;~&quot; and must use &quot;-&quot; as a separator. When <code>all</code> is used either in the <code>SOURCE</code> or <code>DEST</code> column intra-zone traffic is not affected. When <code>all+</code> is used, intra-zone traffic is affected. Beginning with Shorewall 4.4.13, exclusion is supported &#8212; see see m[blue]<code>shorewall-exclusion</code>m[]<font SIZE="-2">[7]</font>(5). The <i>zone</i> should be omitted in DNAT-, REDIRECT- and NONAT rules. If the DEST <i>zone</i> is a bport zone, then either:</p>
<dl>
<dd>1. the SOURCE must be <code>all[+][-]</code>, or</dl>
<dl>
<dd>2. the SOURCE <i>zone</i> must be another bport zone associated with the same bridge, or</dl>
<dl>
<dd>3. the SOURCE <i>zone</i> must be an ipv4 zone that is associated with only the same bridge.</dl>
<p> Except when <code>{all|any}</code>[<code>+]|[-</code>] is specified, the server may be further restricted to a particular network, host or interface by appending &quot;:&quot; and the network, host or interface. See <code>SOURCE</code> above. You may exclude certain hosts from the set already defined through use of an <i>exclusion</i> (see m[blue]<code>shorewall-exclusion</code>m[]<font SIZE="-2">[7]</font>(5)). Restriction: MAC addresses are not allowed (this is a Netfilter restriction). Like in the <code>SOURCE</code> column, you may specify a range of IP addresses using the syntax <i>lowaddress</i>&#8211;<i>highaddress</i>. When the <code>ACTION</code> is <code>DNAT</code> or <code>DNAT-</code>, the connections will be assigned to addresses in the range in a round-robin fashion. If your kernel and iptables have ipset match support then you may give the name of an ipset prefaced by &quot;+&quot;. The ipset name may be optionally followed by a number from 1 to 6 enclosed in square brackets ([]) to indicate the number of levels of destination bindings to be matched. Only one of the <code>SOURCE</code> and <code>DEST</code> columns may specify an ipset name. Beginning with Shorewall 4.4.17, the primary IP address of a firewall interface can be specified by an ampersand (&#8216;&amp;&#8217;) followed by the logical name of the interface as found in the INTERFACE column of m[blue]<code>shorewall-interfaces</code>m[]<font SIZE="-2">[8]</font> (5). The <i>port</i> that the server is listening on may be included and separated from the server&#8217;s IP address by &quot;:&quot;. If omitted, the firewall will not modify the destination port. A destination port may only be included if the <code>ACTION</code> is <code>DNAT</code> or <code>REDIRECT</code>. Example:</p>
<dl>
<dd><code>loc:192.168.1.3:3128</code> specifies a local server at IP address 192.168.1.3 and listening on port 3128.</dl>
<p> The <i>port</i> may be specified as a service name. You may specify a port range in the form <i>lowport-highport</i> to cause connections to be assigned to ports in the range in round-robin fashion. When a port range is specified, <i>lowport</i> and <i>highport</i> must be given as integers; service names are not permitted. Additionally, the port range may be optionally followed by <code>:random</code> which causes assignment to ports in the list to be random. If the <code>ACTION</code> is <code>REDIRECT</code> or <code>REDIRECT-</code>, this column needs only to contain the port number on the firewall that the request should be redirected to. That is equivalent to specifying <code>$FW</code>::<i>port</i>.</dl>
<p> <code>PROTO</code>&#8211; {<code>&#8211;</code>|<code>tcp:syn</code>|<code>ipp2p</code>|<code>ipp2p:udp</code>|<code>ipp2p:all</code>|<i>protocol-number</i>|<i>protocol-name</i>|<code>all}</code></p>
<dl>
<dd>Optional Protocol &#8211; <code>ipp2p</code>* requires ipp2p match support in your kernel and iptables. <code>tcp:syn</code> implies <code>tcp</code> plus the SYN flag must be set and the RST,ACK and FIN flags must be reset. Beginning with Shorewall 4.4.19, this column can contain a comma-separated list of protocol-numbers and/or protocol names.</dl>
<p> <code>DPORT</code> &#8211; {<code>&#8211;</code>|<i>port-name-number-or-range</i>[<code>,</code><i>port-name-number-or-range</i>]&#8230;|+<i>ipset</i>}</p>
<dl>
<dd>Optional destination Ports. A comma-separated list of Port names (from <a href="/docs/linux/man/5-services/">services</a>(5)), port numbers or port ranges; if the protocol is <code>icmp</code>, this column is interpreted as the destination icmp-type(s). ICMP types may be specified as a numeric type, a numeric type and code separated by a slash (e.g., 3/4), or a typename. See m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#ICMP">http://www.shorewall.net/configuration_file_basics.htm#ICMP</a></code>m[]<font SIZE="-2">[11]</font>. Note that prior to Shorewall 4.4.19, only a single ICMP type may be listed. If the protocol is <code>ipp2p</code>, this column is interpreted as an ipp2p option without the leading &quot;&#8211;&quot; (example <code>bit</code> for bit-torrent). If no port is given, <code>ipp2p</code> is assumed. A port range is expressed as <i>lowport</i>:<i>highport</i>. This column is ignored if <code>PROTO</code> = <code>all</code> but must be entered if any of the following columns are supplied. In that case, it is suggested that this field contain a dash (<code>&#8211;</code>). If your kernel contains multi-port match support, then only a single Netfilter rule will be generated if in this list and the <code>SPORT</code> list below: 1. There are 15 or less ports listed. 2. No port ranges are included or your kernel and iptables contain extended multi-port match support. Beginning with Shorewall 4.6.0, an <i>ipset</i> name can be specified in this column. This is intended to be used with bitmap:port ipsets. This column was formerly labelled DEST PORT(S).</dl>
<p> <code>SPORT</code> &#8211; {<code>&#8211;</code>|<i>port-name-number-or-range</i>[<code>,</code><i>port-name-number-or-range</i>]&#8230;|+<i>ipset</i>}</p>
<dl>
<dd>Optional port(s) used by the client. If omitted, any source port is acceptable. Specified as a comma- separated list of port names, port numbers or port ranges. Beginning with Shorewall 4.5.15, you may place &#8216;=&#8217; in this column, provided that the DPORT column is non-empty. This causes the rule to match when either the source port or the destination port in a packet matches one of the ports specified in DEST PORTS(S). Use of &#8216;=&#8217; requires multi-port match in your iptables and kernel.</p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 Unless you really understand IP, you should leave this column empty or place a dash (<code>&#8211;</code>) in the column. Most people who try to use this column get it wrong.</dl>
<p> If you don&#8217;t want to restrict client ports but need to specify an <code>ORIGDEST</code> in the next column, then place &quot;-&quot; in this column. If your kernel contains multi-port match support, then only a single Netfilter rule will be generated if in this list and the <code>DPORT</code> list above: 1. There are 15 or less ports listed. 2. No port ranges are included or your kernel and iptables contain extended multi-port match support. Beginning with Shorewall 4.6.0, an <i>ipset</i> name can be specified in this column. This is intended to be used with bitmap:port ipsets. This column was formerly labelled SOURCE PORT(S).</dl>
<p> <code>ORIGDEST</code> &#8211; [<code>&#8211;</code>|<i>address</i>[,<i>address</i>]&#8230;[<i>exclusion</i>]|<i>exclusion</i>]</p>
<dl>
<dd>Optional. If ACTION is <code>DNAT</code>[<code>&#8211;</code>] or <code>REDIRECT</code>[<code>&#8211;</code>] then if this column is included and is different from the IP address given in the <code>DEST</code> column, then connections destined for that address will be forwarded to the IP and port specified in the <code>DEST</code> column. A comma-separated list of addresses may also be used. This is most useful with the <code>REDIRECT</code> target where you want to redirect traffic destined for particular set of hosts. Finally, if the list of addresses begins with &quot;!&quot; (<i>exclusion</i>) then the rule will be followed only if the original destination address in the connection request does not match any of the addresses listed. Beginning with Shorewall 4.4.17, the primary IP address of a firewall interface can be specified by an ampersand (&#8216;&amp;&#8217;) followed by the logical name of the interface as found in the INTERFACE column of m[blue]<code>shorewall-interfaces</code>m[]<font SIZE="-2">[8]</font> (5). For other actions, this column may be included and may contain one or more addresses (host or network) separated by commas. Address ranges are not allowed. When this column is supplied, rules are generated that require that the original destination address matches one of the listed addresses. This feature is most useful when you want to generate a filter rule that corresponds to a <code>DNAT-</code> or <code>REDIRECT-</code> rule. In this usage, the list of addresses should not begin with &quot;!&quot;. It is also possible to specify a set of addresses then exclude part of those addresses. For example, <code>192.168.1.0/24!192.168.1.16/28</code> specifies the addresses 192.168.1.0-182.168.1.15 and 192.168.1.32-192.168.1.255. See m[blue]<code>shorewall-exclusion</code>m[]<font SIZE="-2">[7]</font>(5). See m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/PortKnocking.html">http://www.shorewall.net/PortKnocking.html</a></code>m[]<font SIZE="-2">[12]</font> for an example of using an entry in this column with a user-defined action rule. This column was formerly labelled ORIGINAL DEST.</dl>
<p> <code>RATE</code> &#8211; <i>limit</i></p>
<dl>
<dd>where <i>limit</i> is one of:</p>
<dl>
<dd>[<code>&#8211;</code>|[{<code>s</code>|<code>d</code>}:[[<i>name</i>]:]]]<i>rate</i><code>/</code>{<code>sec</code>|<code>min</code>|<code>hour</code>|<code>day</code>}[:<i>burst</i>]</dl>
<dl>
<dd>[<i>name</i>1]:<i>rate1</i><code>/</code>{<code>sec</code>|<code>min</code>|<code>hour</code>|<code>day</code>}[:<i>burst1</i>],[<i>name</i>2]:<i>rate2</i><code>/</code>{<code>sec</code>|<code>min</code>|<code>hour</code>|<code>day</code>}[:<i>burst2</i>]</dl>
<p> You may optionally rate-limit the rule by placing a value in this column: <i>rate*</i> is the number of connections per interval (<code>sec</code> or <code>min</code>) and <i>burst</i>* is the largest burst permitted. If no <i>burst</i> is given, a value of 5 is assumed. There may be no no white-space embedded in the specification. Example: <code>10/sec:20</code> When <code>s:</code> or <code>d:</code> is specified, the rate applies per source IP address or per destination IP address respectively. The <i>name</i>s may be chosen by the user and specify a hash table to be used to count matching connections. If not given, the name <code>shorewallN</code> (where N is a unique integer) is assumed. Where more than one rule or POLICY specifies the same name, the connections counts for the rules are aggregated and the individual rates apply to the aggregated count. Beginning with Shorewall 4.6.5, two<i> limit</i>s may be specified, separated by a comma. In this case, the first limit (<i>name1</i>, <i>rate1</i>, burst1) specifies the per-source IP limit and the second limit specifies the per-destination IP limit. Example: <code>client:10/sec:20,:60/sec:100</code> In this example, the &#8216;client&#8217; hash table will be used to enforce the per-source limit and the compiler will pick a unique name for the hash table that tracks the per-destination limit. This column was formerly labelled RATE LIMIT.</dl>
<p> <code>USER</code> &#8211; [<code>!</code>][<i>user-name-or-number</i>][<code>:</code><i>group-name-or-number</i>][,&#8230;]</p>
<dl>
<dd>This optional column may only be non-empty if the SOURCE is the firewall itself. When this column is non-empty, the rule applies only if the program generating the output is running under the effective <i>user</i> and/or <i>group</i> specified (or is NOT running under that id if &quot;!&quot; is given). Beginning with Shorewall 4.5.8, multiple user or group names/ids separated by commas may be specified. Examples: joe</p>
<dl>
<dd>program must be run by joe</dl>
<p> :kids</p>
<dl>
<dd>program must be run by a member of the &#8216;kids&#8217; group</dl>
<p> !:kids</p>
<dl>
<dd>program must not be run by a member of the &#8216;kids&#8217; group</dl>
<p> 2001-2099</p>
<dl>
<dd>UIDs 2001 through 2099 (Shorewall 4.5.6 and later)</dl>
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
<p> <code>CONNLIMIT</code> &#8211; [d:][<code>!</code>]<i>limit</i>[:<i>mask</i>]</p>
<dl>
<dd>May be used to limit the number of simultaneous connections to/from each individual host or network to <i>limit</i> connections. Requires connlimit match in your kernel and iptables. While the limit is only checked on rules specifying CONNLIMIT, the number of current connections is calculated over all current connections from the SOURCE or DESTINATION host. By default, limiting is done by SOURCE host or net, but if the specification begins with <code>d:</code>, then limiting will be donw by destination host or net. By default, the limit is applied to each host but can be made to apply to networks of hosts by specifying a <i>mask</i>. The <i>mask</i> specifies the width of a VLSM mask to be applied to the source address; the number of current connections is then taken over all hosts in the subnet <i>source-address</i>/<i>mask</i>. When<code> !</code> is specified, the rule matches when the number of connection exceeds the <i>limit</i>.</dl>
<p> <code>TIME</code> &#8211; <i>timeelement</i>[&amp;<i>timeelement</i>&#8230;]</p>
<dl>
<dd>May be used to limit the rule to a particular time period each day, to particular days of the week or month, or to a range defined by dates and times. Requires time match support in your kernel and iptables. <i>timeelement</i> may be: timestart=<i>hh</i>:<i>mm</i>[:<i>ss</i>]</p>
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
<dd>where <i>dd</i> is an ordinal day of the month  datestart=<i>yyyy</i>[-<i>mm</i>[-<i>dd</i>[<code>T</code><i>hh</i>[:<i>mm</i>[:<i>ss</i>]]]]]</p>
<dl>
<dd>Defines the starting date and time.</dl>
<p> datestop=<i>yyyy</i>[-<i>mm</i>[-<i>dd</i>[<code>T</code><i>hh</i>[:<i>mm</i>[:<i>ss</i>]]]]]</p>
<dl>
<dd>Defines the ending date and time.</dl>
</dl>
<p> <code>HEADERS</code></p>
<dl>
<dd>Added in Shorewall 4.4.15. Not used in IPv4 configurations. If you with to supply a value for one of the later columns, enter &#8216;-&#8216; in this column.</dl>
<p> <code>SWITCH &#8211; [!]</code><i>switch-name</i><code>[={0|1}]</code></p>
<dl>
<dd>Added in Shorewall 4.4.24 and allows enabling and disabling the rule without requiring <code>shorewall restart</code>. The rule is enabled if the value stored in /proc/net/nf_condition/<i>switch-name</i> is 1. The rule is disabled if that file contains 0 (the default). If &#8216;!&#8217; is supplied, the test is inverted such that the rule is enabled if the file contains 0. Within the <i>switch-name</i>, &#8216;@0&#8217; and &#8216;@{0}&#8217; are replaced by the name of the chain to which the rule is a added. The <i>switch-name</i> (after &#8216;@&#8230;&#8217; expansion) must begin with a letter and be composed of letters, decimal digits, underscores or hyphens. Switch names must be 30 characters or less in length. Switches are normally <code>off</code>. To turn a switch <code>on</code>:</p>
<dl>
<dd><code>echo 1 &gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/proc/net/nf_condition/</code><i>switch-name</i></dl>
<p> To turn it <code>off</code> again:</p>
<dl>
<dd><code>echo 0 &gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/proc/net/nf_condition/</code><i>switch-name</i></dl>
<p> Switch settings are retained over <code>shorewall restart</code>. Beginning with Shorewall 4.5.10, when the <i>switch-name</i> is followed by <code>=0</code> or <code>=1</code>, then the switch is initialized to off or on respectively by the <code>start</code> command. Other commands do not affect the switch setting.</dl>
<p> <code>HELPER</code> &#8211; [helper]</p>
<dl>
<dd>Added in Shorewall 4.5.7. In the NEW section, causes the named conntrack <i>helper</i> to be associated with this connection; the contents of this column are ignored unless ACTION is ACCEPT*, DNAT* or REDIRECT*. In the RELATED section, will only match if the related connection has the named <i>helper</i> associated with it. The <i>helper</i> may be one of:</p>
<dl>
<dd><code>amanda</code></dl>
<dl>
<dd><code>ftp</code></dl>
<dl>
<dd><code>irc</code></dl>
<dl>
<dd><code>netbios-ns</code></dl>
<dl>
<dd><code>pptp</code></dl>
<dl>
<dd><code>Q.931</code></dl>
<dl>
<dd><code>RAS</code></dl>
<dl>
<dd><code>sane</code></dl>
<dl>
<dd><code>sip</code></dl>
<dl>
<dd><code>snmp</code></dl>
<dl>
<dd><code>tftp</code></dl>
<p> If the HELPERS option is specified in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font>(5), then any module specified in this column must be listed in the HELPERS setting.</dl>
<h2>Examples</h2>
<p>Example 1:</p>
<dl>
<dd>Accept SMTP requests from the DMZ to the internet </p>
<dl>
<dd>
<pre> #ACTION SOURCE DEST PROTO DPORT SPORT ORIGDEST
 ACCEPT dmz net tcp smtp</pre>
</dl>
</dl>
<p> Example 2:</p>
<dl>
<dd>Forward all ssh and http connection requests from the internet to local system 192.168.1.3 </p>
<dl>
<dd>
<pre> #ACTION SOURCE DEST PROTO DPORT SPORT ORIGDEST
 DNAT net loc:192.168.1.3 tcp ssh,http</pre>
</dl>
</dl>
<p> Example 3:</p>
<dl>
<dd>Forward all http connection requests from the internet to local system 192.168.1.3 with a limit of 3 per second and a maximum burst of 10 </p>
<dl>
<dd>
<pre> #ACTION SOURCE DEST PROTO DPORT SPORT ORIGDEST RATE
 DNAT net loc:192.168.1.3 tcp http - - 3/sec:10</pre>
</dl>
</dl>
<p> Example 4:</p>
<dl>
<dd>Redirect all locally-originating www connection requests to port 3128 on the firewall (Squid running on the firewall system) except when the destination address is 192.168.2.2 </p>
<dl>
<dd>
<pre> #ACTION SOURCE DEST PROTO DPORT SPORT ORIGDEST
 REDIRECT loc 3128 tcp www - !192.168.2.2</pre>
</dl>
</dl>
<p> Example 5:</p>
<dl>
<dd>All http requests from the internet to address 130.252.100.69 are to be forwarded to 192.168.1.3 </p>
<dl>
<dd>
<pre> #ACTION SOURCE DEST PROTO DPORT SPORT ORIGDEST
 DNAT net loc:192.168.1.3 tcp 80 - 130.252.100.69</pre>
</dl>
</dl>
<p> Example 6:</p>
<dl>
<dd>You want to accept SSH connections to your firewall only from internet IP addresses 130.252.100.69 and 130.252.100.70 </p>
<dl>
<dd>
<pre> #ACTION SOURCE DEST PROTO DPORT SPORT ORIGDEST
 ACCEPT net:130.252.100.69,130.252.100.70 \
 $FW tcp 22</pre>
</dl>
</dl>
<p> Example 7:</p>
<dl>
<dd>You wish to accept connections from the internet to your firewall on port 2222 and you want to forward them to local system 192.168.1.3, port 22 </p>
<dl>
<dd>
<pre> #ACTION SOURCE DEST PROTO DPORT SPORT ORIGDEST
 DNAT net loc:192.168.1.3:22 tcp 2222</pre>
</dl>
</dl>
<p> Example 8:</p>
<dl>
<dd>You want to redirect connection requests to port 80 randomly to the port range 81-90. </p>
<dl>
<dd>
<pre> #ACTION SOURCE DEST PROTO DPORT SPORT ORIGDEST
 REDIRECT net $FW::81-90:random tcp www</pre>
</dl>
</dl>
<p> Example 9:</p>
<dl>
<dd>Shorewall does not impose as much structure on the Netfilter rules in the &#8216;nat&#8217; table as it does on those in the filter table. As a consequence, when using Shorewall versions before 4.1.4, care must be exercised when using DNAT and REDIRECT rules with zones defined with wildcard interfaces (those ending with &#8216;+&#8217;. Here is an example: </p>
<p> m[blue]<code>shorewall-zones</code>m[]<font SIZE="-2">[4]</font>(5): </p>
<dl>
<dd>
<pre> #ZONE TYPE OPTIONS
 fw firewall
 net ipv4
 dmz ipv4
 loc ipv4</pre>
</dl>
<p> m[blue]<code>shorewall-interfaces</code>m[]<font SIZE="-2">[8]</font>(5): </p>
<dl>
<dd>
<pre> #ZONE INTERFACE BROADCAST OPTIONS
 net ppp0
 loc eth1 detect
 dmz eth2 detect
 - ppp+ # Addresses are assigned from 192.168.3.0/24</pre>
</dl>
<p> m[blue]<code>shorewall-host</code>m[]<font SIZE="-2">[13]</font>(5): </p>
<dl>
<dd>
<pre> #ZONE HOST(S) OPTIONS
 loc ppp+:192.168.3.0/24</pre>
</dl>
<p> rules: </p>
<dl>
<dd>
<pre> #ACTION SOURCE DEST PROTO DPORT
 REDIRECT loc 3128 tcp 80 </pre>
</dl>
<p> Note that it would have been tempting to simply define the loc zone entirely in <a href="/docs/linux/man/8-shorewall-interfaces/">shorewall-interfaces</a>(8): </p>
<dl>
<dd>
<pre> #******************* INCORRECT *****************
 #ZONE INTERFACE BROADCAST OPTIONS
 net ppp0
 loc eth1 detect
 loc ppp+
 dmz eth2</pre>
</dl>
<p> This would have made it impossible to run a internet-accessible web server in the DMZ because all traffic entering ppp+ interfaces would have been redirected to port 3128 on the firewall and there would have been no net-&gt;fw ACCEPT rule for that traffic.</dl>
<p> Example 10:</p>
<dl>
<dd>Add the tuple (source IP, dest port, dest IP) of an incoming SSH connection to the ipset S: </p>
<dl>
<dd>
<pre> #ACTION SOURCE DEST PROTO DPORT
 ADD(+S:dst,src,dst) net fw tcp 22</pre>
</dl>
</dl>
<p> Example 11:</p>
<dl>
<dd>You wish to limit SSH connections from remote systems to 1/min with a burst of three (to allow for limited retry): </p>
<dl>
<dd>
<pre> #ACTION SOURCE DEST PROTO DPORT SPORT ORIGDEST RATE
 SSH(ACCEPT) net all - - - - s:1/min:3</pre>
</dl>
</dl>
<p> Example 12:</p>
<dl>
<dd>Forward port 80 to dmz host $BACKUP if switch &#8216;primary_down&#8217; is on. </p>
<dl>
<dd>
<pre> #ACTION SOURCE DEST PROTO DPORT SPORT ORIGDEST RATE USER MARK CONNLIMIT TIME HEADERS SWITCH
 DNAT net dmz:$BACKUP tcp 80 - - - - - - - - primary_down</pre>
</dl>
</dl>
<p> Example 13:</p>
<dl>
<dd>Drop all email from the <i>Anonymous Proxy</i> and <i>Satellite Provider</i> address ranges: </p>
<dl>
<dd>
<pre> #ACTION SOURCE DEST PROTO DPORT
 DROP net:^A1,A2 fw tcp 25</pre>
</dl>
</dl>
<p> Example 14:</p>
<dl>
<dd>You want to generate your own rule involving iptables targets and matches not supported by Shorewall. </p>
<dl>
<dd>
<pre> #ACTION SOURCE DEST PROTO DPORT
 INLINE $FW net ; -p 6 -m mickey-mouse --name test -m set --match-set set1 src -m mickey-mouse --name test2 -j SECCTX --name test3</pre>
</dl>
<p> The above will generate the following iptables-restore input: </p>
<dl>
<dd>
<pre> -A fw2net -p 6 -m mickey-mouse --name test -m set --match-set set1 src -m mickey-mouse --name test2 -j SECCTX --name test3</pre>
</dl>
<p> Note that SECCTX must be defined as a builtin action in m[blue]<code>shorewall-actions</code>m[]<font SIZE="-2">[3]</font>(5): </p>
<dl>
<dd>
<pre> #ACTION OPTIONS
 SECCTX builtin</pre>
</dl>
</dl>
<h2>Files</h2>
<p>/etc/shorewall/rules</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/ipsets.html">http://www.shorewall.net/ipsets.html</a></code>m[]<font SIZE="-2">[14]</font> </p>
<p> m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[]<font SIZE="-2">[15]</font> </p>
<p> m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/shorewall_logging.html">http://www.shorewall.net/shorewall_logging.html</a></code>m[]<font SIZE="-2">[16]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-blrules/">shorewall-blrules</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall_interfaces/">shorewall_interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-rtrules/">shorewall-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-secmarks/">shorewall-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-mangle/">shorewall-mangle</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall-policy</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-policy.html">http://www.shorewall.net/manpages/shorewall-policy.html</a></dl>
<dt> 2.</p>
<dd>shorewall.conf</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall.conf.html">http://www.shorewall.net/manpages/shorewall.conf.html</a></dl>
<dt> 3.</p>
<dd>shorewall-actions</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-actions.html">http://www.shorewall.net/manpages/shorewall-actions.html</a></dl>
<dt> 4.</p>
<dd>shorewall-zones</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-zones.html">http://www.shorewall.net/manpages/shorewall-zones.html</a></dl>
<dt> 5.</p>
<dd>shorewall-nesting</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-nesting.html">http://www.shorewall.net/manpages/shorewall-nesting.html</a></dl>
<dt> 6.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/shorewall_logging.html">http://www.shorewall.net/shorewall_logging.html</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/shorewall.logging.html">http://www.shorewall.net/shorewall.logging.html</a></dl>
<dt> 7.</p>
<dd>shorewall-exclusion</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-exclusion.html">http://www.shorewall.net/manpages/shorewall-exclusion.html</a></dl>
<dt> 8.</p>
<dd>shorewall-interfaces</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-interfaces.html">http://www.shorewall.net/manpages/shorewall-interfaces.html</a></dl>
<dt> 9.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/ISO-3661.html">http://www.shorewall.net/ISO-3661.html</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/ISO-3661.html">http://www.shorewall.net/ISO-3661.html</a></dl>
<dt>10.</p>
<dd>shorewall6-exclusion</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-exclusion.html">http://www.shorewall.net/manpages6/shorewall6-exclusion.html</a></dl>
<dt>11.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#ICMP">http://www.shorewall.net/configuration_file_basics.htm#ICMP</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#ICMP">http://www.shorewall.net/configuration_file_basics.htm#ICMP</a></dl>
<dt>12.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/PortKnocking.html">http://www.shorewall.net/PortKnocking.html</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/PortKnocking.html">http://www.shorewall.net/PortKnocking.html</a></dl>
<dt>13.</p>
<dd>shorewall-host</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-hosts.html">http://www.shorewall.net/manpages/shorewall-hosts.html</a></dl>
<dt>14.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/ipsets.html">http://www.shorewall.net/ipsets.html</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/ipsets.html">http://www.shorewall.net/ipsets.html</a></dl>
<dt>15.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dl>
<dt>16.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/shorewall_logging.html">http://www.shorewall.net/shorewall_logging.html</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/shorewall_logging.html">http://www.shorewall.net/shorewall_logging.html</a></dl>
