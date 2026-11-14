---
title: "shorewall-policy(5)"
name: "shorewall-policy"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-policy/"
description: "policy – Shorewall policy file"
---

<p>policy &#8211; Shorewall policy file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/policy</code></dl>
<h2>Description</h2>
<dd>This file defines the high-level policy for connections between zones defined in m[blue]<code>shorewall-zones</code>m[]<font SIZE="-2">[1]</font>(5).</p>
<dl>
<dd><font SIZE="+1"> <code>Important</code> </font><br />
 The order of entries in this file is important This file determines what to do with a new connection request if we don&#8217;t get a match from the /etc/shorewall/rules file . For each source/destination pair, the file is processed in order until a match is found (&quot;all&quot; will match any source or destination). </p>
<dl>
<dd><font SIZE="+1"> <code>Important</code> </font><br />
 Intra-zone policies are pre-defined For $FW and for all of the zones defined in /etc/shorewall/zones, the POLICY for connections from the zone to itself is ACCEPT (with no logging or TCP connection rate limiting) but may be overridden by an entry in this file. The overriding entry must be explicit (specifying the zone name in both SOURCE and DEST) or it must use &quot;all+&quot; (Shorewall 4.5.17 or later). Similarly, if you have IMPLICIT_CONTINUE=Yes in shorewall.conf, then the implicit policy to/from any sub-zone is CONTINUE. These implicit CONTINUE policies may also be overridden by an explicit entry in this file.  The columns in the file are as follows (where the column name is followed by a different name in parentheses, the different name is used in the alternate specification syntax). <code>SOURCE</code> &#8211; <i>zone</i>[,&#8230;[+]]|<code>$FW</code>|<code>all</code>|<code>all+</code></p>
<dl>
<dd>Source zone. Must be the name of a zone defined in m[blue]<code>shorewall-zones</code>m[]<font SIZE="-2">[1]</font>(5), $FW, &quot;all&quot; or &quot;all+&quot;. Support for &quot;all+&quot; was added in Shorewall 4.5.17. &quot;all&quot; does not override the implicit intra-zone ACCEPT policy while &quot;all+&quot; does. Beginning with Shorewall 5.0.12, multiple zones may be listed separated by commas. As above, if &#8216;+&#8217; is specified after two or more zone names, then the policy overrides the implicit intra-zone ACCEPT policy if the same <i>zone</i> appears in both the SOURCE and DEST columns.</dl>
<p> <code>DEST</code> &#8211; <i>zone</i>[,&#8230;[+]]|<code>$FW</code>|<code>all</code>|<code>all+</code></p>
<dl>
<dd>Destination zone. Must be the name of a zone defined in m[blue]<code>shorewall-zones</code>m[]<font SIZE="-2">[1]</font>(5), $FW, &quot;all&quot; or &quot;all+&quot;. If the DEST is a bport zone, then the SOURCE must be &quot;all&quot;, &quot;all+&quot;, another bport zone associated with the same bridge, or it must be an ipv4 zone that is associated with only the same bridge. Support for &quot;all+&quot; was added in Shorewall 4.5.17. &quot;all&quot; does not override the implicit intra-zone ACCEPT policy while &quot;all+&quot; does. Beginning with Shorewall 5.0.12, multiple zones may be listed separated by commas. As above, if &#8216;+&#8217; is specified after two or more zone names, then the policy overrides the implicit intra-zone ACCEPT policy if the same <i>zone</i> appears in both the SOURCE and DEST columns.</dl>
<p> <code>POLICY</code> &#8211; {<code>ACCEPT</code>|<code>DROP</code>|<code>REJECT</code>|<code>CONTINUE</code>|<code>QUEUE</code>|<code>NFQUEUE</code>[(<i>queuenumber1</i>[:<i>queuenumber2</i>])]|<code>NONE</code>}[<code>:</code>{<i>default-action-or-macro</i>[:level]|<code>None</code>}]</p>
<dl>
<dd>Policy if no match from the rules file is found. If the policy is neither CONTINUE nor NONE then the policy may be followed by &quot;:&quot; and one of the following:</p>
<dl>
<dd>1. The word &quot;None&quot; or &quot;none&quot;. This causes any default action defined in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font>(5) to be omitted for this policy.</dl>
<dl>
<dd>2. The name of an action. The action will be invoked before the policy is enforced.</dl>
<p> Actions can have parameters specified. Beginning with Shorewall 4.5.10, the action name can be followed optionally by a colon and a log level. The level will be applied to each rule in the action or body that does not already have a log level. Possible actions are: <code>ACCEPT</code></p>
<dl>
<dd>Accept the connection.</dl>
<p> <code>DROP</code></p>
<dl>
<dd>Ignore the connection request.</dl>
<p> <code>REJECT</code></p>
<dl>
<dd>For TCP, send RST. For all other, send an &quot;unreachable&quot; ICMP.</dl>
<p> <code>QUEUE</code></p>
<dl>
<dd>Queue the request for a user-space application such as Snort-inline.</dl>
<p> <code>NFQUEUE</code></p>
<dl>
<dd>Queue the request for a user-space application using the nfnetlink_queue mechanism. If a <i>queuenumber1</i> is not given, queue zero (0) is assumed. Beginning with Shorewall 4.6.10, a second queue number (queuenumber2) may be given. This specifies a range of queues to use. Packets are then balanced across the given queues. This is useful for multicore systems: start multiple instances of the userspace program on queues x, x+1, .. x+n and use &quot;x:x+n&quot;. Packets belonging to the same connection are put into the same nfqueue.</dl>
<p> <code>CONTINUE</code></p>
<dl>
<dd>Pass the connection request past any other rules that it might also match (where the source or destination zone in those rules is a superset of the SOURCE or DEST in this policy). See m[blue]<code>shorewall-nesting</code>m[]<font SIZE="-2">[3]</font>(5) for additional information.</dl>
<p> <code>NONE</code></p>
<dl>
<dd>Assume that there will never be any packets from this SOURCE to this DEST. Shorewall will not create any infrastructure to handle such packets and you may not have any rules with this SOURCE and DEST in the /etc/shorewall/rules file. If such a packet <code>is</code> received, the result is undefined. NONE may not be used if the SOURCE or DEST columns contain the firewall zone ($FW) or &quot;all&quot;.</dl>
</dl>
<p> <code>LOG LEVEL</code> (loglevel) &#8211; [<i>log-level</i>|<code>ULOG|NFLOG</code>]</p>
<dl>
<dd>Optional &#8211; if supplied, each connection handled under the default POLICY is logged at that level. If not supplied, no log message is generated. See <a href="/docs/linux/man/5-syslog-conf/">syslog.conf</a>(5) for a description of log levels. You may also specify ULOG or NFLOG (must be in upper case). This will log to the ULOG or NFLOG target and will send to a separate log through use of ulogd (m[blue]<code><a rel="nofollow" href="http://www.netfilter.org/projects/ulogd/index.html">http://www.netfilter.org/projects/ulogd/index.html</a></code>m[]). For a description of log levels, see m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/shorewall_logging.html">http://www.shorewall.net/shorewall_logging.html</a></code>m[]<font SIZE="-2">[4]</font>. If you don&#8217;t want to log but need to specify the following column, place &quot;-&quot; here.</dl>
<p> <code>BURST:LIMIT</code> (limit) &#8211; [-|<i>limit</i>]</p>
<dl>
<dd>where limit is one of:</p>
<dl>
<dd>[<code>&#8211;</code>|[{<i>s</i>|<code>d</code>}:[[<i>name</i>]:]]]<i>rate</i><code>/</code>{<code>sec</code>|<code>min</code>|<code>hour</code>|<code>day</code>}[:<i>burst</i>]</dl>
<dl>
<dd>[<i>name</i>1]:<i>rate1</i><code>/</code>{<code>sec</code>|<code>min</code>|<code>hour</code>|<code>day</code>}[:<i>burst1</i>],[<i>name</i>2]:<i>rate2</i><code>/</code>{<code>sec</code>|<code>min</code>|<code>hour</code>|<code>day</code>}[:<i>burst2</i>]</dl>
<p> If passed, specifies the maximum TCP connection <i>rate</i> and the size of an acceptable <i>burst</i>. If not specified, TCP connections are not limited. If the <i>burst</i> parameter is omitted, a value of 5 is assumed. When <code>s:</code> or <code>d:</code> is specified, the rate applies per source IP address or per destination IP address respectively. The <i>name</i> may be chosen by the user and specifies a hash table to be used to count matching connections. If not give, the name <code>shorewall</code> is assumed. Where more than one POLICY or rule specifies the same name, the connections counts for the policies are aggregated and the individual rates apply to the aggregated count. Beginning with Shorewall 4.6.5, two<i> limit</i>s may be specified, separated by a comma. In this case, the first limit (<i>name1</i>, <i>rate1</i>, burst1) specifies the per-source IP limit and the second limit specifies the per-destination IP limit. Example: <code>client:10/sec:20,:60/sec:100</code></dl>
<p> <code>CONNLIMIT</code> &#8211; <i>limit</i>[:<i>mask</i>]</p>
<dl>
<dd>May be used to limit the number of simultaneous connections from each individual host to <i>limit</i> connections. While the limit is only checked on connections to which this policy could apply, the number of current connections is calculated over all current connections from the SOURCE host. By default, the limit is applied to each host individually but can be made to apply to networks of hosts by specifying a <i>mask</i>. The <i>mask</i> specifies the width of a VLSM mask to be applied to the source address; the number of current connections is then taken over all hosts in the subnet <i>source-address</i>/<i>mask</i>.</dl>
<h2>Example</h2>
<dl>
<dd>1. All connections from the local network to the internet are allowed</dl>
<dl>
<dd>2. All connections from the internet are ignored but logged at syslog level KERNEL.INFO.</dl>
<dl>
<dd>3. All other connection requests are rejected and logged at level KERNEL.INFO.</dl>
<dl>
<dd>
<pre> #SOURCE DEST POLICY LOG BURST:LIMIT
 # LEVEL
 loc net ACCEPT
 net all DROP info
 #
 # THE FOLLOWING POLICY MUST BE LAST
 #
 all all REJECT info</pre>
</dl>
<h2>Files</h2>
<p>/etc/shorewall/policy</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[]<font SIZE="-2">[5]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall_interfaces/">shorewall_interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-rtrules/">shorewall-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-secmarks/">shorewall-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-mangle/">shorewall-mangle</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall-zones</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-zones.html">http://www.shorewall.net/manpages/shorewall-zones.html</a></dl>
<dt> 2.</p>
<dd>shorewall.conf</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall.conf.html">http://www.shorewall.net/manpages/shorewall.conf.html</a></dl>
<dt> 3.</p>
<dd>shorewall-nesting</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-nesting.html">http://www.shorewall.net/manpages/shorewall-nesting.html</a></dl>
<dt> 4.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/shorewall_logging.html">http://www.shorewall.net/shorewall_logging.html</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/shorewall_logging.html">http://www.shorewall.net/shorewall_logging.html</a></dl>
<dt> 5.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dl>
