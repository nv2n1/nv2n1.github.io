---
title: "shorewall-lite(8)"
name: "shorewall-lite"
section: "8"
letter: "s"
url: "/docs/linux/man/8-shorewall-lite/"
description: "shorewall-lite – Administration tool for Shoreline Firewall Lite (Shorewall Lite)"
---

<p>shorewall-lite &#8211; Administration tool for Shoreline Firewall Lite (Shorewall Lite)</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>add</code> <i>interface</i>[:<i>host-list</i>]&#8230; <i>zone</i></p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>allow</code> <i>address</i></p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>blacklist</code> <i>address</i></p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>allow</code> <i>address</i></p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>clear</code>&nbsp;<wbr>[<code>-f</code>]</p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>close</code>&nbsp;<wbr>{&nbsp;<wbr><i>open-number</i>&nbsp;<wbr>|&nbsp;<wbr><i>source</i><i>dest</i>&nbsp;<wbr>[<i>protocol</i>&nbsp;<wbr>[&nbsp;<wbr><i>port</i>&nbsp;<wbr>]]}<i>&nbsp;<wbr></i></p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>delete</code> <i>interface</i>[:<i>host-list</i>]&#8230; <i>zone</i></p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>disable</code> {&nbsp;<wbr><i>interface</i>&nbsp;<wbr>|&nbsp;<wbr><i>provider</i>&nbsp;<wbr>}</p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>drop</code> <i>address</i></p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] <code>dump</code> [<code>-x</code>] [<code>-l</code>] [<code>-m</code>] [<code>-c</code>]</p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>enable</code> {&nbsp;<wbr><i>interface</i>&nbsp;<wbr>|&nbsp;<wbr><i>provider</i>&nbsp;<wbr>}</p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>forget</code> [<i>filename</i>]</p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] <code>help</code></p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] <code>hits</code>&nbsp;<wbr>[<code>-t</code>]</p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] <code>ipcalc</code> {<i>address</i>&nbsp;<wbr><i>mask</i> | <i>address</i>/<i>vlsm</i>}</p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] <code>iprange</code> <i>address1</i><code>&#8211;</code><i>address2</i></p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] <code>iptrace</code> <i>iptables match expression</i></p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>logdrop</code> <i>address</i></p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] <code>logwatch</code> [<code>-m</code>] [<i>refresh-interval</i>]</p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>logreject</code> <i>address</i></p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] <code>noiptrace</code> <i>iptables match expression</i></p>
<dt> <code>shorewall-lite</code> <code>open</code><i>&nbsp;<wbr>source</i><i>&nbsp;<wbr>dest</i>&nbsp;<wbr>[&nbsp;<wbr><i>protocol</i>&nbsp;<wbr>[&nbsp;<wbr><i>port</i>&nbsp;<wbr>]&nbsp;<wbr>]</p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>reenable</code> {&nbsp;<wbr><i>interface</i>&nbsp;<wbr>|&nbsp;<wbr><i>provider</i>&nbsp;<wbr>}</p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>reject</code> <i>address</i></p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>reload</code> [<code>-n</code>] [<code>-p</code>&nbsp;<wbr>[<code>-C</code>]]</p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>reset</code></p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>restart</code> [<code>-n</code>] [<code>-p</code>&nbsp;<wbr>[<code>-C</code>]]</p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>restore</code> [<code>-C</code>] [<i>filename</i>]</p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>run</code> function [<i>parameter &#8230;</i>]</p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>save</code>&nbsp;<wbr>[<code>-C</code>] [<i>filename</i>]</p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>savesets</code></p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] {<code>show | list | ls&nbsp;<wbr></code>} [<code>-b</code>] [<code>-x</code>] [<code>-l</code>] [<code>-t</code>&nbsp;<wbr>{<code>filter</code>|<code>mangle</code>|<code>nat</code>|<code>raw|rawpost</code>}] [[<code>chain</code>]&nbsp;<wbr><i>chain</i>&#8230;]</p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] {<code>show | list | ls&nbsp;<wbr></code>} [<code>-x</code>] <code>{bl|blacklists}</code></p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] {<code>show | list | ls&nbsp;<wbr></code>} [<code>-f</code>] <code>capabilities</code></p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] {<code>show | list | ls&nbsp;<wbr></code>} {<code>classifiers|connections|config|events|filters|ip|ipa|zones|policies|marks</code>}</p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] {<code>show | list | ls&nbsp;<wbr></code>} <code>event</code>&nbsp;<wbr><i>event</i></p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] {<code>show | list | ls&nbsp;<wbr></code>} [<code>-c</code>] <code>routing</code></p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] {<code>show | list | ls&nbsp;<wbr></code>} [<code>-x</code>] {<code>mangle|nat|raw|rawpost</code>}</p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] {<code>show | list | ls&nbsp;<wbr></code>} <code>tc</code></p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] {<code>show | list | ls&nbsp;<wbr></code>} [<code>-m</code>] <code>log</code></p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>start</code> [<code>-n</code>] [<code>-p</code>] [<code>-f</code>] [<code>-C</code>]</p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>stop</code></p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] <code>status</code>&nbsp;<wbr>[<code>-i</code>]</p>
<dt> <code>shorewall-lite</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] <code>version</code>&nbsp;<wbr>[<code>-a</code>]</dl>
<h2>Description</h2>
<dd>The shorewall-lite utility is used to control the Shoreline Firewall Lite (Shorewall Lite).</p>
<h2>Options</h2>
<p>The <code>trace</code> and <code>debug</code> options are used for debugging. See m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/starting_and_stopping_shorewall.htm#Trace">http://www.shorewall.net/starting_and_stopping_shorewall.htm#Trace</a></code>m[]. </p>
<p> The nolock <code>option</code> prevents the command from attempting to acquire the Shorewall-lite lockfile. It is useful if you need to include <code>shorewall</code> commands in the startedm[blue]<code>extension script</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> The <i>options</i> control the amount of output that the command produces. They consist of a sequence of the letters <code>v</code> and <code>q</code>. If the options are omitted, the amount of output is determined by the setting of the VERBOSITY parameter in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font>(5). Each <code>v</code> adds one to the effective verbosity and each <code>q</code> subtracts one from the effective VERBOSITY. Alternately, <code>v</code> may be followed immediately with one of -1,0,1,2 to specify VERBOSITY. There may be no white-space between <code>v</code> and the VERBOSITY. </p>
<p> The <i>options</i> may also include the letter <code>t</code> which causes all progress messages to be timestamped.</p>
<h2>Commands</h2>
<p>The available commands are listed below. </p>
<p> <code>add </code>{ <i>interface</i>[:<i>host-list</i>]&#8230; <i>zone</i> | <i>zone</i> <i>host-list</i> }</p>
<dl>
<dd>Adds a list of hosts or subnets to a dynamic zone usually used with VPN&#8217;s. </p>
<p> The <i>interface</i> argument names an interface defined in the m[blue]<code>shorewall-interfaces</code>m[]<font SIZE="-2">[3]</font>(5) file. A <i>host-list</i> is comma-separated list whose elements are host or network addresses. </p>
<dl>
<dd><font SIZE="+1"> <code>Caution</code> </font><br />
 The <code>add</code> command is not very robust. If there are errors in the <i>host-list</i>, you may see a large number of error messages yet a subsequent <code>shorewall-lite show zones</code> command will indicate that all hosts were added. If this happens, replace <code>add</code> by <code>delete</code> and run the same command again. Then enter the correct command. </p>
</dl>
</dl>
<p> <code>allow </code><i>address</i></p>
<dl>
<dd>Re-enables receipt of packets from hosts previously blacklisted by a <code>drop</code>, <code>logdrop</code>, <code>reject</code>, or <code>logreject</code> command. Beginning with Shorewall 5.0.10, this command can also re-enable addresses blacklisted using the <code>blacklist</code> command.</dl>
<p> <code>blacklist</code> <i>address</i> [ <i>option</i> &#8230; ]</p>
<dl>
<dd>Added in Shorewall 5.0.8 and requires DYNAMIC_BLACKLIST=ipset.. in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[4]</font>(5). Causes packets from the given host or network <i>address</i> to be dropped, based on the setting of BLACKLIST in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[4]</font>(5). The <i>address</i> along with any <i>option</i>s are passed to the <code>ipset add</code> command. </p>
<p> If the <code>disconnect</code> option is specified in the DYNAMIC_BLACKLISTING setting, then the effective VERBOSITY determines the amount of information displayed: </p>
<dl>
<dd>&bull; If the effective verbosity is &gt; 0, then a message giving the number of conntrack flows deleted by the command is displayed.</dl>
<dl>
<dd>&bull; If the effective verbosity is &gt; 1, then the conntrack table entries deleted by the command are also displayed.</dl>
</dl>
<p> <code>call </code><i>function</i><code> [ </code><i>parameter</i><code> &#8230; ]</code></p>
<dl>
<dd>Added in Shorewall 4.6.10. Allows you to call a function in one of the Shorewall libraries or in your compiled script. function must name the shell function to be called. The listed parameters are passed to the function. </p>
<p> The function is first searched for in lib.base, lib.common and lib.cli. If it is not found, the call command is passed to the generated script to be executed.</dl>
<p> <code>clear </code>[-<code>f</code>]</p>
<dl>
<dd>Clear will remove all rules and chains installed by Shorewall-lite. The firewall is then wide open and unprotected. Existing connections are untouched. Clear is often used to see if the firewall is causing connection problems. </p>
<p> If <code>-f</code> is given, the command will be processed by the compiled script that executed the last successful <code>start</code>, <code>reload</code>, <code>restart</code> or <code>refresh</code> command if that script exists.</dl>
<p> <code>close</code> { <i>open-number</i> | <i>source</i> <i>dest</i> [ <i>protocol</i> [ <i>port</i> ] ] }</p>
<dl>
<dd>Added in Shorewall 4.5.8. This command closes a temporary open created by the <code>open</code> command. In the first form, an <i>open-number</i> specifies the open to be closed. Open numbers are displayed in the <code>num</code> column of the output of the <code>shorewall-lite show opens </code>command. </p>
<p> When the second form of the command is used, the parameters must match those given in the earlier <code>open</code> command.</dl>
<p> <code>delete </code>{ <i>interface</i>[:<i>host-list</i>]&#8230; <i>zone</i> | <i>zone</i> <i>host-list</i> }</p>
<dl>
<dd>The delete command reverses the effect of an earlier <code>add</code> command. </p>
<p> The <i>interface</i> argument names an interface defined in the m[blue]<code>shorewall-interfaces</code>m[]<font SIZE="-2">[3]</font>(5) file. A <i>host-list</i> is comma-separated list whose elements are a host or network address.</dl>
<p> <code>disable </code>{ <i>interface</i> | <i>provider</i> }</p>
<dl>
<dd>Added in Shorewall 4.4.26. Disables the optional provider associated with the specified <i>interface</i> or <i>provider</i>. Where more than one provider share a single network interface, a <i>provider</i> name must be given.</dl>
<p> <code>drop </code><i>address</i></p>
<dl>
<dd>Causes traffic from the listed <i>address</i>es to be silently dropped.</dl>
<p> <code>dump </code>[-<code>x</code>] [-<code>l</code>] [-<code>m</code>] [-<code>c</code>]</p>
<dl>
<dd>Produces a verbose report about the firewall configuration for the purpose of problem analysis. </p>
<p> The <code>-x</code> option causes actual packet and byte counts to be displayed. Without that option, these counts are abbreviated. The <code>-m</code> option causes any MAC addresses included in Shorewall-lite log messages to be displayed. </p>
<p> The <code>-l</code> option causes the rule number for each Netfilter rule to be displayed. </p>
<p> The <code>-c</code> option causes the route cache to be dumped in addition to the other routing information.</dl>
<p> <code>enable </code>{ <i>interface</i> | <i>provider</i> }</p>
<dl>
<dd>Added in Shorewall 4.4.26. Enables the optional provider associated with the specified <i>interface</i> or <i>provider</i>. Where more than one provider share a single network interface, a <i>provider</i> name must be given.</dl>
<p> <code>forget </code>[ <i>filename</i> ]</p>
<dl>
<dd>Deletes /var/lib/shorewall-lite/<i>filename</i> and /var/lib/shorewall-lite/save. If no <i>filename</i> is given then the file specified by RESTOREFILE in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font>(5) is assumed.</dl>
<p> <code>help</code></p>
<dl>
<dd>Displays a syntax summary.</dl>
<p> <code>hits </code> [-<code>t</code>]</p>
<dl>
<dd>Generates several reports from Shorewall-lite log messages in the current log file. If the <code>-t</code> option is included, the reports are restricted to log messages generated today.</dl>
<p> <code>ipcalc </code>{ address mask | address/vlsm }</p>
<dl>
<dd>Ipcalc displays the network address, broadcast address, network in CIDR notation and netmask corresponding to the input[s].</dl>
<p> <code>iprange </code><i>address1</i>&#8211;<i>address2</i></p>
<dl>
<dd>Iprange decomposes the specified range of IP addresses into the equivalent list of network/host addresses.</dl>
<p> <code>iptrace </code><i>iptables match expression</i></p>
<dl>
<dd>This is a low-level debugging command that causes iptables TRACE log records to be created. See <a href="/docs/linux/man/8-iptables/">iptables</a>(8) for details. </p>
<p> The <i>iptables match expression</i> must be one or more matches that may appear in both the raw table OUTPUT and raw table PREROUTING chains. </p>
<p> The trace records are written to the kernel&#8217;s log buffer with facility = kernel and priority = warning, and they are routed from there by your logging daemon (syslogd, rsyslog, syslog-ng, &#8230;) &#8212; Shorewall-lite has no control over where the messages go; consult your logging daemon&#8217;s documentation.</dl>
<p> <code>list</code></p>
<dl>
<dd><code>list</code> is a synonym for <code>show</code> &#8212; please see below.</dl>
<p> <code>logdrop </code><i>address</i></p>
<dl>
<dd>Causes traffic from the listed <i>address</i>es to be logged then discarded. Logging occurs at the log level specified by the BLACKLIST_LOGLEVEL setting in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font> (5).</dl>
<p> <code>logwatch </code>[-<code>m</code>] [<i>refresh-interval</i>]</p>
<dl>
<dd>Monitors the log file specified by the LOGFILE option in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font>(5) and produces an audible alarm when new Shorewall-lite messages are logged. The <code>-m</code> option causes the MAC address of each packet source to be displayed if that information is available. The <i>refresh-interval</i> specifies the time in seconds between screen refreshes. You can enter a negative number by preceding the number with &quot;&#8211;&quot; (e.g., <code>shorewall-lite logwatch &#8212; -30</code>). In this case, when a packet count changes, you will be prompted to hit any key to resume screen refreshes.</dl>
<p> <code>logreject </code><i>address</i></p>
<dl>
<dd>Causes traffic from the listed <i>address</i>es to be logged then rejected. Logging occurs at the log level specified by the BLACKLIST_LOGLEVEL setting in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font> (5).</dl>
<p> <code>ls</code></p>
<dl>
<dd><code>ls</code> is a synonym for <code>show</code> &#8212; please see below.</dl>
<p> <code>noiptrace </code><i>iptables match expression</i></p>
<dl>
<dd>This is a low-level debugging command that cancels a trace started by a preceding <code>iptrace</code> command. </p>
<p> The <i>iptables match expression</i> must be one given in the <code>iptrace</code> command being canceled.</dl>
<p> <code>open</code> <i>source</i> <i>dest</i> [ <i>protocol</i> [ <i>port</i> ] ]</p>
<dl>
<dd>Added in Shorewall 4.6.8. This command requires that the firewall be in the started state and that DYNAMIC_BLACKLIST=Yes in m[blue]<code>shorewall.conf (5)</code>m[]<font SIZE="-2">[4]</font>. The effect of the command is to temporarily open the firewall for connections matching the parameters. </p>
<p> The <i>source</i> and <i>dest</i> parameters may each be specified as <code>all</code> if you don&#8217;t wish to restrict the connection source or destination respectively. Otherwise, each must contain a host or network address or a valid DNS name. </p>
<p> The <i>protocol</i> may be specified either as a number or as a name listed in /etc/protocols. The <i>port</i> may be specified numerically or as a name listed in /etc/services. </p>
<p> To reverse the effect of a successful <code>open</code> command, use the <code>close</code> command with the same parameters or simply restart the firewall. </p>
<p> Example: To open the firewall for SSH connections to address 192.168.1.1, the command would be: </p>
<dl>
<dd>
<pre> shorewall-lite open all 192.168.1.1 tcp 22</pre>
</dl>
<p> To reverse that command, use: </p>
<dl>
<dd>
<pre> shorewall-lite close all 192.168.1.1 tcp 22</pre>
</dl>
</dl>
<p> <code>reenable</code>{ <i>interface</i> | <i>provider</i> }</p>
<dl>
<dd>Added in Shorewall 4.6.9. This is equivalent to a <code>disable</code> command followed by an <code>enable</code> command on the specified <i>interface</i> or <i>provider</i>.</dl>
<p> <code>reject</code><i> address</i></p>
<dl>
<dd>Causes traffic from the listed <i>address</i>es to be silently rejected.</dl>
<p> <code>reload </code>[-n] [-p] [-<code>C</code>]</p>
<dl>
<dd>Added in Shorewall 5.0.0, <code>reload</code> is similar to <code>shorewall-lite start</code> except that it assumes that the firewall is already started. Existing connections are maintained. </p>
<p> The <code>-n</code> option causes Shorewall-lite to avoid updating the routing table(s). </p>
<p> The <code>-p</code> option causes the connection tracking table to be flushed; the <code>conntrack</code> utility must be installed to use this option. </p>
<p> The <code>-C</code> option was added in Shorewall 4.6.5. If the specified (or implicit) firewall script is the one that generated the current running configuration, then the running netfilter configuration will be reloaded as is so as to preserve the iptables packet and byte counters.</dl>
<p> <code>reset [</code><i>chain</i><code>, &#8230;]</code></p>
<dl>
<dd>Resets the packet and byte counters in the specified <i>chain</i>(s). If no <i>chain</i> is specified, all the packet and byte counters in the firewall are reset.</dl>
<p> <code>restart </code>[-n] [-p] [-<code>C</code>]</p>
<dl>
<dd>Beginning with Shorewall 5.0.0, this command performs a true restart. The firewall is completely stopped as if a <code>stop</code> command had been issued then it is started again. </p>
<p> The <code>-n</code> option causes Shorewall-lite to avoid updating the routing table(s). </p>
<p> The <code>-p</code> option causes the connection tracking table to be flushed; the <code>conntrack</code> utility must be installed to use this option. </p>
<p> The <code>-C</code> option was added in Shorewall 4.6.5. If the specified (or implicit) firewall script is the one that generated the current running configuration, then the running netfilter configuration will be reloaded as is so as to preserve the iptables packet and byte counters.</dl>
<p> <code>restore </code>[-<code>n</code>] [-<code>p</code>] [-<code>C</code>] [ <i>filename</i> ]</p>
<dl>
<dd>Restore Shorewall-lite to a state saved using the <code>shorewall-lite save</code> command. Existing connections are maintained. The <i>filename</i> names a restore file in /var/lib/shorewall-lite created using <code>shorewall-lite save</code>; if no <i>filename</i> is given then Shorewall-lite will be restored from the file specified by the RESTOREFILE option in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font>(5). </p>
<dl>
<dd><font SIZE="+1"> <code>Caution</code> </font><br />
 If your iptables ruleset depends on variables that are detected at run-time, either in your params file or by Shorewall-generated code, <code>restore</code> will use the values that were current when the ruleset was saved, which may be different from the current values. </p>
</dl>
<p> The <code>-n</code> option causes Shorewall to avoid updating the routing table(s). </p>
<p> The <code>-p</code> option, added in Shorewall 4.6.5, causes the connection tracking table to be flushed; the <code>conntrack</code> utility must be installed to use this option. </p>
<p> The <code>-C</code> option was added in Shorewall 4.6.5. If the <code>-C</code> option was specified during <code>shorewall save</code>, then the counters saved by that operation will be restored.</dl>
<p> <code>run </code><i>command</i> [ <i>parameter</i> &#8230; ]</p>
<dl>
<dd>Added in Shorewall 4.6.3. Executes <i>command</i> in the context of the generated script passing the supplied <i>parameter</i>s. Normally, the <i>command</i> will be a function declared in lib.private. </p>
<p> Before executing the <i>command</i>, the script will detect the configuration, setting all SW_* variables and will run your init extension script with $COMMAND = &#8216;run&#8217;.</dl>
<p> <code>save </code>[-<code>C</code>] [ <i>filename</i> ]</p>
<dl>
<dd>The dynamic blacklist is stored in /var/lib/shorewall-lite/save. The state of the firewall is stored in /var/lib/shorewall-lite/<i>filename</i> for use by the <code>shorewall-lite restore</code>. If <i>filename</i> is not given then the state is saved in the file specified by the RESTOREFILE option in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font>(5). </p>
<p> The <code>-C</code> option, added in Shorewall 4.6.5, causes the iptables packet and byte counters to be saved along with the chains and rules.</dl>
<p> <code>savesets</code></p>
<dl>
<dd>Added in shorewall 4.6.8. Performs the same action as the <code>stop</code> command with respect to saving ipsets (see the SAVE_IPSETS option in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[4]</font> (5)). This command may be used to proactively save your ipset contents in the event that a system failure occurs prior to issuing a <code>stop</code> command.</dl>
<p> <code>show</code></p>
<dl>
<dd>The show command can have a number of different arguments: </p>
<p> <code>bl|blacklists </code>[-<code>x</code>]</p>
<dl>
<dd>Added in Shorewall 4.6.2. Displays the dynamic chain along with any chains produced by entries in <a href="/docs/linux/man/5-shorewall-blrules/">shorewall-blrules</a>(5).The <code>-x</code> option is passed directly through to iptables and causes actual packet and byte counts to be displayed. Without this option, those counts are abbreviated.</dl>
<p> [-<code>f</code>] <code>capabilities</code></p>
<dl>
<dd>Displays your kernel/iptables capabilities. The <code>-f</code> option causes the display to be formatted as a capabilities file for use with <code>compile -e</code>.</dl>
<p> [-<code>b</code>] [-<code>x</code>] [-<code>l</code>] [-<code>t</code> {<code>filter</code>|<code>mangle</code>|<code>nat</code>|<code>raw</code>|<code>rawpost</code>}] [ <i>chain</i>&#8230; ]</p>
<dl>
<dd>The rules in each <i>chain</i> are displayed using the <code>iptables -L</code><i>chain</i><code>-n -v</code> command. If no <i>chain</i> is given, all of the chains in the filter table are displayed. The <code>-x</code> option is passed directly through to iptables and causes actual packet and byte counts to be displayed. Without this option, those counts are abbreviated. The <code>-t</code> option specifies the Netfilter table to display. The default is <code>filter</code>. </p>
<p> The <code>-b</code> (&#8216;brief&#8217;) option causes rules which have not been used (i.e. which have zero packet and byte counts) to be omitted from the output. Chains with no rules displayed are also omitted from the output. </p>
<p> The <code>-l</code> option causes the rule number for each Netfilter rule to be displayed. </p>
<p> If the <code>t</code> option and the <code>chain</code> keyword are both omitted and any of the listed <i>chain</i>s do not exist, a usage message is displayed.</dl>
<p> <code>classifiers|filters</code></p>
<dl>
<dd>Displays information about the packet classifiers defined on the system as a result of traffic shaping configuration.</dl>
<p> <code>config</code></p>
<dl>
<dd>Displays distribution-specific defaults.</dl>
<p> <code>connections [</code><i>filter_parameter</i><code> &#8230;]</code></p>
<dl>
<dd>Displays the IP connections currently being tracked by the firewall. </p>
<p> If the <code>conntrack</code> utility is installed, beginning with Shorewall 4.6.11 the set of connections displayed can be limited by including conntrack filter parameters (-p , -s, &#8211;dport, etc). See <a href="/docs/linux/man/8-conntrack/">conntrack</a>(8) for details.</dl>
<p> <code>event</code><i> event</i></p>
<dl>
<dd>Added in Shorewall 4.5.19. Displays the named event.</dl>
<p> <code>events</code></p>
<dl>
<dd>Added in Shorewall 4.5.19. Displays all events.</dl>
<p> <code>ip</code></p>
<dl>
<dd>Displays the system&#8217;s IPv4 configuration.</dl>
<p> <code>ipa</code></p>
<dl>
<dd>Added in Shorewall 4.4.17. Displays the per-IP accounting counters (m[blue]<code>shorewall-accounting</code>m[]<font SIZE="-2">[5]</font> (5)).</dl>
<p> [-<code>m</code>] <code>log</code></p>
<dl>
<dd>Displays the last 20 Shorewall-lite messages from the log file specified by the LOGFILE option in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font>(5). The <code>-m</code> option causes the MAC address of each packet source to be displayed if that information is available.</dl>
<p> [-<code>x</code>] <code>mangle</code></p>
<dl>
<dd>Displays the Netfilter mangle table using the command <code>iptables -t mangle -L -n -v</code>. The <code>-x</code> option is passed directly through to iptables and causes actual packet and byte counts to be displayed. Without this option, those counts are abbreviated.</dl>
<p> <code>marks</code></p>
<dl>
<dd>Added in Shorewall 4.4.26. Displays the various fields in packet marks giving the min and max value (in both decimal and hex) and the applicable mask (in hex).</dl>
<p> <code>nat</code></p>
<dl>
<dd>Displays the Netfilter nat table using the command <code>iptables -t nat -L -n -v</code>.The <code>-x</code> option is passed directly through to iptables and causes actual packet and byte counts to be displayed. Without this option, those counts are abbreviated.</dl>
<p> <code>opens</code></p>
<dl>
<dd>Added in Shorewall 4.5.8. Displays the iptables rules in the &#8216;dynamic&#8217; chain created through use of the <code>open </code>command..</dl>
<p> <code>policies</code></p>
<dl>
<dd>Added in Shorewall 4.4.4. Displays the applicable policy between each pair of zones. Note that implicit intrazone ACCEPT policies are not displayed for zones associated with a single network where that network doesn&#8217;t specify <code>routeback</code>.</dl>
<p> <code>routing</code></p>
<dl>
<dd>Displays the system&#8217;s IPv4 routing configuration. The -c option causes the route cache to be displayed in addition to the other routing information.</dl>
<p> <code>raw</code></p>
<dl>
<dd>Displays the Netfilter raw table using the command <code>iptables -t raw -L -n -v</code>.The <code>-x</code> option is passed directly through to iptables and causes actual packet and byte counts to be displayed. Without this option, those counts are abbreviated.</dl>
<p> <code>tc</code></p>
<dl>
<dd>Displays information about queuing disciplines, classes and filters.</dl>
<p> <code>zones</code></p>
<dl>
<dd>Displays the current composition of the Shorewall zones on the system.</dl>
</dl>
<p> <code>start</code> [-<code>p</code>] [-<code>n</code>] [<code>-f</code>] [-<code>C</code>]</p>
<dl>
<dd>Start Shorewall Lite. Existing connections through shorewall-lite managed interfaces are untouched. New connections will be allowed only if they are allowed by the firewall rules or policies. </p>
<p> The <code>-p</code> option causes the connection tracking table to be flushed; the <code>conntrack</code> utility must be installed to use this option. </p>
<p> The <code>-n</code> option prevents the firewall script from modifying the current routing configuration. </p>
<p> The <code>-f</code> option was added in Shorewall 4.6.5. If the RESTOREFILE named in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font>(5) exists, is executable and is not older than the current filewall script, then that saved configuration is restored. </p>
<p> The <code>-C</code> option was added in Shorewall 4.6.5 and is only meaningful when the <code>-f</code> option is also specified. If the previously-saved configuration is restored, and if the <code>-C</code> option was also specified in the <code>save</code> command, then the packet and byte counters will be restored.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the firewall. All existing connections, except those listed in m[blue]<code>shorewall-routestopped</code>m[]<font SIZE="-2">[6]</font>(5) or permitted by the ADMINISABSENTMINDED option in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[2]</font>(5), are taken down. The only new traffic permitted through the firewall is from systems listed in m[blue]<code>shorewall-routestopped</code>m[]<font SIZE="-2">[6]</font>(5) or by ADMINISABSENTMINDED. </p>
<p> If <code>-f</code> is given, the command will be processed by the compiled script that executed the last successful <code>start</code>, <code>restart</code> or <code>refresh</code> command if that script exists.</dl>
<p> <code>status</code></p>
<dl>
<dd>Produces a short report about the state of the Shorewall-configured firewall. </p>
<p> The <code>-i </code>option was added in Shorewall 4.6.2 and causes the status of each optional or provider interface to be displayed.</dl>
<p> <code>version</code></p>
<dl>
<dd>Displays Shorewall&#8217;s version. The <code>-a</code> option is included for compatibility with earlier Shorewall releases and is ignored.</dl>
<h2>Exit Status</h2>
<p>In general, when a command succeeds, status 0 is returned; when the command fails, a non-zero status is returned. </p>
<p> The <code>status</code> command returns exit status as follows: </p>
<p> 0 &#8211; Firewall is started. </p>
<p> 3 &#8211; Firewall is stopped or cleared </p>
<p> 4 &#8211; Unknown state; usually means that the firewall has never been started.</p>
<h2>Environment</h2>
<p>Two environmental variables are recognized by Shorewall-lite: </p>
<p> SHOREWALL_INIT_SCRIPT</p>
<dl>
<dd>When set to 1, causes Std out to be redirected to the file specified in the STARTUP_LOG option in m[blue]<code><a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5)</code>m[]<font SIZE="-2">[2]</font>.</dl>
<p> SW_LOGGERTAG</p>
<dl>
<dd>Added in Shorewall 5.0.8. When set to a non-empty value, that value is passed to the logger utility in its -t (&#8211;tag) option.</dl>
<h2>Files</h2>
<p>/etc/shorewall-lite/</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/starting_and_stopping_shorewall.htm">http://www.shorewall.net/starting_and_stopping_shorewall.htm</a></code>m[] </p>
<p> <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall_interfaces/">shorewall_interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-rtrules/">shorewall-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-secmarks/">shorewall-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-tcrules/">shorewall-tcrules</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>extension script</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net../shorewall_extension_scripts.html">http://www.shorewall.net../shorewall_extension_scripts.html</a></dl>
<dt> 2.</p>
<dd>shorewall.conf</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netshorewall.conf.html">http://www.shorewall.netshorewall.conf.html</a></dl>
<dt> 3.</p>
<dd>shorewall-interfaces</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netshorewall-interfaces.html">http://www.shorewall.netshorewall-interfaces.html</a></dl>
<dt> 4.</p>
<dd>shorewall.conf</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall.conf.html">http://www.shorewall.net/manpages/shorewall.conf.html</a></dl>
<dt> 5.</p>
<dd>shorewall-accounting</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netmanpages/shorewall-accounting.html">http://www.shorewall.netmanpages/shorewall-accounting.html</a></dl>
<dt> 6.</p>
<dd>shorewall-routestopped</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netshorewall-routestopped.html">http://www.shorewall.netshorewall-routestopped.html</a></dl>
