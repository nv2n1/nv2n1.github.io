---
title: "shorewall6(8)"
name: "shorewall6"
section: "8"
letter: "s"
url: "/docs/linux/man/8-shorewall6/"
description: "shorewall6 – Administration tool for Shoreline Firewall 6 (Shorewall6)"
---

<p>shorewall6 &#8211; Administration tool for Shoreline Firewall 6 (Shorewall6)</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>add&nbsp;<wbr>{</code> <i>interface</i>[:<i>host-list</i>]&#8230; <i>zone | zone host-list&nbsp;<wbr></i><code>}</code></p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>allow</code></p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>blacklist</code> <i>address</i>&nbsp;<wbr>[<i>option &#8230;</i>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>call</code> <i>function</i>&nbsp;<wbr>[<i>parameter</i>&nbsp;<wbr>&#8230;]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] [<code>check | ck&nbsp;<wbr></code>] [<code>-e</code>] [<code>-d</code>] [<code>-p</code>] [<code>-r</code>] [<code>-T</code>] [<code>-i</code>] [<i>directory</i>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>clear</code></p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>close</code>&nbsp;<wbr>{&nbsp;<wbr><i>open-number</i>&nbsp;<wbr>|&nbsp;<wbr><i>source</i><i>dest</i>&nbsp;<wbr>[<i>protocol</i>&nbsp;<wbr>[&nbsp;<wbr><i>port</i>&nbsp;<wbr>]]}<i>&nbsp;<wbr></i></p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] [<code>compile | co&nbsp;<wbr></code>] [<code>-e</code>] [<code>-d</code>] [<code>-T</code>] [<code>-i</code>] [<i>directory</i>] [<i>pathname</i>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>delete&nbsp;<wbr>{</code> <i>interface</i>[:<i>host-list</i>]&#8230; <i>zone | zone host-list&nbsp;<wbr></i><code>}</code></p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>disable</code> {&nbsp;<wbr><i>interface</i>&nbsp;<wbr>|&nbsp;<wbr><i>provider</i>&nbsp;<wbr>}</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>drop</code> <i>address</i></p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] <code>dump</code> [<code>-x</code>] [<code>-l</code>] [<code>-m</code>] [<code>-c</code>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>enable</code> {&nbsp;<wbr><i>interface</i>&nbsp;<wbr>|&nbsp;<wbr><i>provider</i>&nbsp;<wbr>}</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>export</code> [<i>directory1</i>] [<i>user</i>@]<i>system</i>[<code>:</code><i>directory2</i>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>forget</code> [<i>filename</i>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] <code>help</code></p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] <code>iptrace</code> <i>iptables match expression</i></p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>logdrop</code> <i>address</i></p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] <code>logwatch</code> [<code>-m</code>] [<i>refresh-interval</i>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>logreject</code> <i>address</i></p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] <code>noiptrace</code> <i>iptables match expression</i></p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>open</code><i>&nbsp;<wbr>source</i><i>&nbsp;<wbr>dest</i>&nbsp;<wbr>[&nbsp;<wbr><i>protocol</i>&nbsp;<wbr>[&nbsp;<wbr><i>port</i>&nbsp;<wbr>]&nbsp;<wbr>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>reenable</code> {&nbsp;<wbr><i>interface</i>&nbsp;<wbr>|&nbsp;<wbr><i>provider</i>&nbsp;<wbr>}</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>refresh</code>&nbsp;<wbr>[<code>-n</code>]&nbsp;<wbr>[<code>-d</code>]&nbsp;<wbr>[<code>-T</code>]&nbsp;<wbr>[<code>-i</code>]&nbsp;<wbr>[-<code>D</code>&nbsp;<wbr><i>directory</i>&nbsp;<wbr>]&nbsp;<wbr>[<i>chain</i>&#8230;]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>reject</code> <i>address</i></p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] <code>remote-start</code> [<code>-s</code>] [<code>-c</code>] [<code>-r</code>&nbsp;<wbr><i>root-user-name</i>] [<code>-T</code>] [<code>-i</code>] [[<code>-D</code>]<i>directory</i>] [<i>system</i>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] <code>remote-reload</code> [<code>-s</code>] [<code>-c</code>] [<code>-r</code>&nbsp;<wbr><i>root-user-name</i>] [<code>-T</code>] [<code>-i</code>] [[<code>-D</code>]<i>directory</i>] [<i>system</i>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] <code>remote-restart</code> [<code>-s</code>] [<code>-c</code>] [<code>-r</code>&nbsp;<wbr><i>root-user-name</i>] [<code>-T</code>] [<code>-i</code>] [[<code>-D</code>]<i>directory</i>] [<i>system</i>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>reset</code>&nbsp;<wbr>[<i>chain</i>&nbsp;<wbr>&#8230;]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>reload</code> [<code>-n</code>] [<code>-f</code>] [<code>-c</code>] [<code>-T</code>] [<code>-i</code>&nbsp;<wbr>[<code>-C</code>]] [<i>directory</i>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>restart</code> [<code>-n</code>] [<code>-f</code>] [<code>-c</code>] [<code>-T</code>] [<code>-i</code>&nbsp;<wbr>[<code>-C</code>]] [<i>directory</i>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>restore</code>&nbsp;<wbr>[<code>-C</code>] [<i>filename</i>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>run</code> <i>command</i> [<i>parameter &#8230;</i>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>safe-reload</code> [<code>-d</code>] [<code>-t</code>&nbsp;<wbr><i>timeout</i>] [<i>directory</i>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>safe-restart</code> [<code>-d</code>] [<code>-t</code>&nbsp;<wbr><i>timeout</i>] [<i>directory</i>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] <code>safe-start</code> [<code>-d</code>] [<code>-t</code>&nbsp;<wbr><i>timeout</i>] [<i>directory</i>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>save</code>&nbsp;<wbr>[<code>-C</code>] [<i>filename</i>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>savesets</code></p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] {<code>show | list | ls&nbsp;<wbr></code>} [<code>-x</code>] <code>{bl|blacklists}</code></p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] {<code>show | list | ls&nbsp;<wbr></code>} [<code>-b</code>] [<code>-x</code>] [<code>-l</code>] [<code>-t</code>&nbsp;<wbr>{<code>filter</code>|<code>mangle</code>|<code>raw</code>}] [[<code>chain</code>]&nbsp;<wbr><i>chain</i>&#8230;]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] {<code>show | list | ls&nbsp;<wbr></code>} [<code>-f</code>] <code>capabilities</code></p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] {<code>show | list | ls&nbsp;<wbr></code>} {<code>actions|classifiers|connections|config|events|filters|ip|macros|zones|policies|tc|marks</code>}</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] {<code>show | list | ls&nbsp;<wbr></code>} <code>event</code>&nbsp;<wbr><i>event</i></p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] {<code>show | list | ls&nbsp;<wbr></code>} [<code>-c</code>] <code>routing</code></p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] {<code>show | list | ls&nbsp;<wbr></code>} [<code>-x</code>] {<code>mangle|nat|raw|rawpost</code>}</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] {<code>show | list | ls&nbsp;<wbr></code>} <code>tc</code></p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] {<code>show | list | ls&nbsp;<wbr></code>} [<code>-m</code>] <code>log</code></p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>start</code> [<code>-n</code>] [<code>-f</code>] [<code>-c</code>] [<code>-T</code>] [<code>-i</code>&nbsp;<wbr>[<code>-C</code>]] [<i>directory</i>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>stop</code></p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] <code>status</code>&nbsp;<wbr>[<code>-i</code>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>&nbsp;<wbr>[<code>nolock</code>]] [-<i>options</i>] <code>try</code> <i>directory</i> [<i>timeout</i>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] <code>update</code> [<code>-d</code>] [<code>-r</code>] [<code>-T</code>] [<code>-a</code>] [<code>-i</code>] [<code>-A</code>] [<i>directory</i>]</p>
<dt> <code>shorewall6</code> [<code>trace</code>|<code>debug</code>] [-<i>options</i>] <code>version</code>&nbsp;<wbr>[<code>-a</code>]</dl>
<h2>Description</h2>
<dd>The shorewall6 utility is used to control the Shoreline Firewall 6 (Shorewall6).</p>
<h2>Options</h2>
<p>The <code>trace</code> and <code>debug</code> options are used for debugging. See m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/starting_and_stopping_shorewall.htm#Trace">http://www.shorewall.net/starting_and_stopping_shorewall.htm#Trace</a></code>m[]<font SIZE="-2">[1]</font>. </p>
<p> The <code>nolock</code> option prevents the command from attempting to acquire the Shorewall6 lockfile. It is useful if you need to include <code>shorewall6</code> commands in /etc/shorewall6/started. </p>
<p> The <i>options</i> control the amount of output that the command produces. They consist of a sequence of the letters <code>v</code> and <code>q</code>. If the options are omitted, the amount of output is determined by the setting of the VERBOSITY parameter in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5). Each <code>v</code> adds one to the effective verbosity and each <code>q</code> subtracts one from the effective VERBOSITY. Alternatively, <code>v</code> may be followed immediately with one of -1,0,1,2 to specify a specify VERBOSITY. There may be no white-space between <code>v</code> and the VERBOSITY. </p>
<p> The <i>options</i> may also include the letter <code>t</code> which causes all progress messages to be timestamped.</p>
<h2>Commands</h2>
<p>The available commands are listed below. </p>
<p> <code>add </code>{ <i>interface</i>[:<i>host-list</i>]&#8230; <i>zone</i> | <i>zone</i> <i>host-list</i> }</p>
<dl>
<dd>Added in Shorewall 4.4.21. Adds a list of hosts or subnets to a dynamic zone usually used with VPN&#8217;s. </p>
<p> The <i>interface</i> argument names an interface defined in the m[blue]<code>shorewall6-interfaces</code>m[]<font SIZE="-2">[3]</font>(5) file. A <i>host-list</i> is comma-separated list whose elements are host or network addresses..if n </p>
<dl>
<dd><font SIZE="+1"> <code>Caution</code> </font><br />
 The <code>add</code> command is not very robust. If there are errors in the <i>host-list</i>, you may see a large number of error messages yet a subsequent <code>shorewall show zones</code> command will indicate that all hosts were added. If this happens, replace <code>add</code> by <code>delete</code> and run the same command again. Then enter the correct command. </p>
</dl>
<p> Beginning with Shorewall 4.5.9, the <code>dynamic_shared</code> zone option (m[blue]<code>shorewall6-zones</code>m[]<font SIZE="-2">[4]</font>(5)) allows a single ipset to handle entries for multiple interfaces. When that option is specified for a zone, the <code>add</code> command has the alternative syntax in which the <i>zone</i> name precedes the <i>host-list</i>.</dl>
<p> <code>allow </code><i>address</i></p>
<dl>
<dd>Re-enables receipt of packets from hosts previously blacklisted by a <code>drop</code>, <code>logdrop</code>, <code>reject</code>, or <code>logreject</code> command. Beginning with Shorewall 5.0.10, this command can also re-enable addresses blacklisted using the <code>blacklist</code> command.</dl>
<p> <code>blacklist</code> <i>address</i> [ <i>option</i> &#8230; ]</p>
<dl>
<dd>Added in Shorewall 5.0.8 and requires DYNAMIC_BLACKLIST=ipset.. in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5). Causes packets from the given host or network <i>address</i> to be dropped, based on the setting of BLACKLIST in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5). The <i>address</i> along with any <i>option</i>s are passed to the <code>ipset add</code> command. </p>
<p> If the <code>disconnect</code> option is specified in the DYNAMIC_BLACKLISTING setting, then the effective VERBOSITY determines the amount of information displayed: </p>
<dl>
<dd>&bull; If the effective verbosity is &gt; 0, then a message giving the number of conntrack flows deleted by the command is displayed.</dl>
<dl>
<dd>&bull; If the effective verbosity is &gt; 1, then the conntrack table entries deleted by the command are also displayed.</dl>
</dl>
<p> <code>call </code><i>function</i><code> [ </code><i>parameter</i><code> &#8230; ]</code></p>
<dl>
<dd>Added in Shorewall 4.6.10. Allows you to call a function in one of the Shorewall libraries or in your compiled script. function must name the shell function to be called. The listed parameters are passed to the function. </p>
<p> The function is first searched for in lib.base, lib.common, lib.cli and lib.cli-std. If it is not found, the call command is passed to the generated script to be executed.</dl>
<p> <code>check </code>[-<code>e</code>] [-<code>d</code>] [-<code>p</code>] [-<code>r</code>] [-<code>T</code>] [-<code>i</code>] [<i>directory</i>]</p>
<dl>
<dd>Compiles the configuration in the specified <i>directory</i> and discards the compiled output script. If no <i>directory</i> is given, then /etc/shorewall6 is assumed. </p>
<p> The <code>-e</code> option causes the compiler to look for a file named capabilities. This file is produced using the command <code>shorewall6-lite show -f capabilities &gt; capabilities</code> on a system with Shorewall6 Lite installed. </p>
<p> The <code>-d</code> option causes the compiler to be run under control of the Perl debugger. </p>
<p> The <code>-p</code> option causes the compiler to be profiled via the Perl <code>-wd:DProf</code> command-line option. </p>
<p> The <code>-r</code> option was added in Shorewall 4.5.2 and causes the compiler to print the generated ruleset to standard out. </p>
<p> The <code>-T</code> option was added in Shorewall 4.4.20 and causes a Perl stack trace to be included with each compiler-generated error and warning message. </p>
<p> The <code>-i</code> option was added in Shorewall 4.6.0 and causes a warning message to be issued if the current line contains alternative input specifications following a semicolon (&quot;;&quot;). Such lines will be handled incorrectly if INLINE_MATCHES is set to Yes in m[blue]<code><a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5)</code>m[]<font SIZE="-2">[2]</font>.</dl>
<p> <code>clear </code>[-<code>f</code>]</p>
<dl>
<dd>Clear will remove all rules and chains installed by Shorewall6. The firewall is then wide open and unprotected. Existing connections are untouched. Clear is often used to see if the firewall is causing connection problems.</dl>
<p> <code>close</code> { <i>open-number</i> | <i>source</i> <i>dest</i> [ <i>protocol</i> [ <i>port</i> ] ] }</p>
<dl>
<dd>Added in Shorewall 4.5.8. This command closes a temporary open created by the <code>open</code> command. In the first form, an <i>open-number</i> specifies the open to be closed. Open numbers are displayed in the <code>num</code> column of the output of the <code>shorewall6 show opens </code>command. </p>
<p> When the second form of the command is used, the parameters must match those given in the earlier <code>open</code> command.</dl>
<p> <code>compile </code>[-<code>e</code>] [-<code>c</code>] [-<code>d</code>] [-<code>p</code>] [-<code>T</code>] [-<code>i</code>] [<i>directory</i>] [<i>pathname</i> ]</p>
<dl>
<dd>Compiles the current configuration into the executable file <i>pathname</i>. If a directory is supplied, Shorewall6 will look in that directory first for configuration files. If the <i>pathname</i> is omitted, the file firewall in the VARDIR (normally /var/lib/shorewall/) is assumed. A <i>pathname</i> of &#8216;-&#8216; causes the compiler to send the generated script to it&#8217;s standard output file. Note that &#8216;-v-1&#8217; is usually specified in this case (e.g., <code>shorewall6 -v-1 compile &#8212; &#8211;</code>) to suppress the &#8216;Compiling&#8230;&#8217; message normally generated by /sbin/shorewall6. </p>
<p> When <code>-e</code> is specified, the compilation is being performed on a system other than where the compiled script will run. This option disables certain configuration options that require the script to be compiled where it is to be run. The use of <code>-e</code> requires the presence of a configuration file named capabilities which may be produced using the command <code>shorewall6-lite show -f capabilities &gt; capabilities</code> on a system with Shorewall6 Lite installed. </p>
<p> The <code>-c</code> option was added in Shorewall 4.5.17 and causes conditional compilation of a script. The script specified by <i>pathname</i> (or implied if <code>pathname</code> is omitted) is compiled if it doesn&#8217;t exist or if there is any file in the <i>directory</i> or in a directory on the CONFIG_PATH that has a modification time later than the file to be compiled. When no compilation is needed, a message is issued and an exit status of zero is returned. </p>
<p> The <code>-d</code> option causes the compiler to be run under control of the Perl debugger. </p>
<p> The <code>-p</code> option causes the compiler to be profiled via the Perl <code>-wd:DProf</code> command-line option. </p>
<p> The <code>-T</code> option was added in Shorewall 4.4.20 and causes a Perl stack trace to be included with each compiler-generated error and warning message. </p>
<p> The <code>-i</code> option was added in Shorewall 4.6.0 and causes a warning message to be issued if the current line contains alternative input specifications following a semicolon (&quot;;&quot;). Such lines will be handled incorrectly if INLINE_MATCHES is set to Yes in m[blue]<code><a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5)</code>m[]<font SIZE="-2">[2]</font>.</dl>
<p> <code>delete </code>{ <i>interface</i>[:<i>host-list</i>]&#8230; <i>zone</i> | <i>zone</i> <i>host-list</i> }</p>
<dl>
<dd>Added in Shorewall 4.4.21. The delete command reverses the effect of an earlier <code>add</code> command. </p>
<p> The <i>interface</i> argument names an interface defined in the m[blue]<code>shorewall6-interfaces</code>m[]<font SIZE="-2">[3]</font>(5) file. A <i>host-list</i> is comma-separated list whose elements are a host or network address. </p>
<p> Beginning with Shorewall 4.5.9, the <code>dynamic_shared</code> zone option (m[blue]<code>shorewall6-zones</code>m[]<font SIZE="-2">[4]</font>(5)) allows a single ipset to handle entries for multiple interfaces. When that option is specified for a zone, the <code>delete</code> command has the alternative syntax in which the <i>zone</i> name precedes the <i>host-list</i>.</dl>
<p> <code>disable </code>{ <i>interface</i> | <i>provider</i> }</p>
<dl>
<dd>Added in Shorewall 4.4.26. Disables the optional provider associated with the specified <i>interface</i> or <i>provider</i>. Where more than one provider share a single network interface, a <i>provider</i> name must be given. </p>
<p> Beginning with Shorewall 4.5.10, this command may be used with any optional network interface. <i>interface</i> may be either the logical or physical name of the interface. The command removes any routes added from m[blue]<code>shorewall6-routes</code>m[]<font SIZE="-2">[5]</font>(5) and any traffic shaping configuration for the interface.</dl>
<p> <code>drop </code><i>address</i></p>
<dl>
<dd>Causes traffic from the listed <i>address</i>es to be silently dropped.</dl>
<p> <code>dump </code>[-<code>x</code>] [-<code>l</code>] [-<code>m</code>] [-<code>c</code>]</p>
<dl>
<dd>Produces a verbose report about the firewall configuration for the purpose of problem analysis. </p>
<p> The <code>-x</code> option causes actual packet and byte counts to be displayed. Without that option, these counts are abbreviated. </p>
<p> The <code>-m</code> option causes any MAC addresses included in Shorewall6 log messages to be displayed. </p>
<p> The <code>-l</code> option causes the rule number for each Netfilter rule to be displayed. </p>
<p> The <code>-c</code> option causes the route cache to be dumped in addition to the other routing information.</dl>
<p> <code>enable </code>{ <i>interface</i> | <i>provider</i> }</p>
<dl>
<dd>Added in Shorewall 4.4.26. Enables the optional provider associated with the specified <i>interface</i> or <i>provider</i>. Where more than one provider share a single network interface, a <i>provider</i> name must be given. </p>
<p> Beginning with Shorewall 4.5.10, this command may be used with any optional network interface. <i>interface</i> may be either the logical or physical name of the interface. The command sets /proc entries for the interface, adds any route specified in m[blue]<code>shorewall6-routes</code>m[]<font SIZE="-2">[5]</font>(5) and installs the interface&#8217;s traffic shaping configuration, if any.</dl>
<p> <code>export </code>[<i>directory1</i> ] [<i>user</i>@]<i>system</i>[:<i>directory2</i> ]</p>
<dl>
<dd>If <i>directory1</i> is omitted, the current working directory is assumed. </p>
<p> Allows a non-root user to compile a shorewall6 script and stage it on a system (provided that the user has access to the system via ssh). The command is equivalent to: </p>
<dl>
<dd>
<pre> <code>/sbin/shorewall6 compile -e</code> <i>directory1</i> <i>directory1</i><code>/firewall &amp;&amp;\</code>
 <code>scp</code> directory1<code>/firewall</code> <i>directory1</i><code>/firewall.conf</code> [<i>user</i>@]<code>system</code>:[<i>directory2</i>]</pre>
</dl>
<p> In other words, the configuration in the specified (or defaulted) directory is compiled to a file called firewall in that directory. If compilation succeeds, then firewall and firewall.conf are copied to <i>system</i> using scp.</dl>
<p> <code>forget </code>[ <i>filename</i> ]</p>
<dl>
<dd>Deletes /var/lib/shorewall6/<i>filename </i> and /var/lib/shorewall6/save. If no <i>filename</i> is given then the file specified by RESTOREFILE in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5) is assumed.</dl>
<p> <code>help</code></p>
<dl>
<dd>Displays a syntax summary.</dl>
<p> <code>iptrace </code><i>ip6tables match expression</i></p>
<dl>
<dd>This is a low-level debugging command that causes iptables TRACE log records to be created. See <a href="/docs/linux/man/8-ip6tables/">ip6tables</a>(8) for details. </p>
<p> The <i>ip6tables match expression</i> must be one or more matches that may appear in both the raw table OUTPUT and raw table PREROUTING chains. </p>
<p> The log message destination is determined by the currently-selected IPv6 m[blue]<code>logging backend</code>m[]<font SIZE="-2">[6]</font>.</dl>
<p> <code>list</code></p>
<dl>
<dd><code>list</code> is a synonym for <code>show</code> &#8212; please see below.</dl>
<p> <code>logdrop </code><i>address</i></p>
<dl>
<dd>Causes traffic from the listed <i>address</i>es to be logged then discarded. Logging occurs at the log level specified by the BLACKLIST_LOGLEVEL setting in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font> (5).</dl>
<p> <code>logwatch </code>[-<code>m</code>] [<i>refresh-interval</i>]</p>
<dl>
<dd>Monitors the log file specified by the LOGFILE option in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5) and produces an audible alarm when new Shorewall6 messages are logged. The <code>-m</code> option causes the MAC address of each packet source to be displayed if that information is available. The <i>refresh-interval</i> specifies the time in seconds between screen refreshes. You can enter a negative number by preceding the number with &quot;&#8211;&quot; (e.g., <code>shorewall6 logwatch &#8212; -30</code>). In this case, when a packet count changes, you will be prompted to hit any key to resume screen refreshes.</dl>
<p> <code>logreject</code> <i>address</i></p>
<dl>
<dd>Causes traffic from the listed <i>address</i>es to be logged then rejected. Logging occurs at the log level specified by the BLACKLIST_LOGLEVEL setting in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font> (5).</dl>
<p> <code>ls</code></p>
<dl>
<dd><code>ls</code> is a synonym for <code>show</code> &#8212; please see below.</dl>
<p> <code>noiptrace </code><i>ip6tables match expression</i></p>
<dl>
<dd>This is a low-level debugging command that cancels a trace started by a preceding <code>iptrace</code> command. </p>
<p> The <i>iptables match expression</i> must be one given in the <code>iptrace</code> command being canceled.</dl>
<p> <code>open</code> <i>source</i> <i>dest</i> [ <i>protocol</i> [ <i>port</i> ] ]</p>
<dl>
<dd>Added in Shorewall 4.6.8. This command requires that the firewall be in the started state and that DYNAMIC_BLACKLIST=Yes in m[blue]<code>shorewall6.conf (5)</code>m[]<font SIZE="-2">[2]</font>. The effect of the command is to temporarily open the firewall for connections matching the parameters. </p>
<p> The <i>source</i> and <i>dest</i> parameters may each be specified as <code>all</code> if you don&#8217;t wish to restrict the connection source or destination respectively. Otherwise, each must contain a host or network address or a valid DNS name. </p>
<p> The <i>protocol</i> may be specified either as a number or as a name listed in /etc/protocols. The <i>port</i> may be specified numerically or as a name listed in /etc/services. </p>
<p> To reverse the effect of a successful <code>open</code> command, use the <code>close</code> command with the same parameters or simply restart the firewall. </p>
<p> Example: To open the firewall for SSH connections to address 2001:470:b:227::1, the command would be: </p>
<dl>
<dd>
<pre> shorewall6 open all 2001:470:b:227::1 tcp 22</pre>
</dl>
<p> To reverse that command, use: </p>
<dl>
<dd>
<pre> shorewall6 close all 2001:470:b:227::1 tcp 22</pre>
</dl>
</dl>
<p> <code>reenable</code>{ <i>interface</i> | <i>provider</i> }</p>
<dl>
<dd>Added in Shorewall 4.6.9. This is equivalent to a <code>disable</code> command followed by an <code>enable</code> command on the specified <i>interface</i> or <i>provider</i>.</dl>
<p> <code>refresh </code>[-<code>n</code>] [-<code>d</code>] [-<code>T</code>] [-i] [-<code>D</code><i>directory</i> ] [ <i>chain</i>&#8230; ]</p>
<dl>
<dd>All steps performed by <code>restart</code> are performed by <code>refresh</code> with the exception that <code>refresh</code> only recreates the chains specified in the command while <code>restart</code> recreates the entire Netfilter ruleset.When no chain name is given to the <code>refresh</code> command, the mangle table is refreshed along with the blacklist chain (if any). This allows you to modify /etc/shorewall6/tcrulesand install the changes using <code>refresh</code>. </p>
<p> The listed chains are assumed to be in the filter table. You can refresh chains in other tables by prefixing the chain name with the table name followed by &quot;:&quot; (e.g., nat:net_dnat). Chain names which follow are assumed to be in that table until the end of the list or until an entry in the list names another table. Built-in chains such as FORWARD may not be refreshed. </p>
<p> The <code>-n</code> option was added in Shorewall 4.5.3 causes Shorewall to avoid updating the routing table(s). </p>
<p> The <code>-d</code> option was added in Shorewall 4.5.3 causes the compiler to run under the Perl debugger. </p>
<p> The <code>-T</code> option was added in Shorewall 4.5.3 and causes a Perl stack trace to be included with each compiler-generated error and warning message. </p>
<p> The <code>-i</code> option was added in Shorewall 4.6.0 and causes a warning message to be issued if the current line contains alternative input specifications following a semicolon (&quot;;&quot;). Such lines will be handled incorrectly if INLINE_MATCHES is set to Yes in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5). </p>
<p> The &#8211;<code>D</code> option was added in Shorewall 4.5.3 and causes Shorewall to look in the given <i>directory</i> first for configuration files. </p>
<p> <code>Example 1. Refresh the &#8216;net-fw&#8217; chain in the filter table and the &#8216;net_dnat&#8217; chain in the nat table</code> </p>
<dl>
<dd>
<pre><code>shorewall6 refresh net-fw nat:net_dnat
 </code></pre>
</dl>
</dl>
<p> <code>reject</code><i> address</i></p>
<dl>
<dd>Causes traffic from the listed <i>address</i>es to be silently rejected.</dl>
<p> <code>reload </code>[-<code>n</code>] [-<code>p</code>] [-<code>d</code>] [-<code>f</code>] [-<code>c</code>] [-<code>T</code>] [-<code>i</code>] [-<code>C</code>] [ <i>directory</i> ]</p>
<dl>
<dd>This command was re-implemented in Shorewall 5.0.0. The pre-5.0.0 <code>reload</code> command is now called <code>remote-restart</code> (see below). </p>
<p> Reload is similar to <code>shorewall6 start</code> except that it assumes that the firewall is already started. Existing connections are maintained. If a <i>directory</i> is included in the command, Shorewall6 will look in that <i>directory</i> first for configuration files. </p>
<p> The <code>-n</code> option causes Shorewall6 to avoid updating the routing table(s). </p>
<p> The <code>-p</code> option causes the connection tracking table to be flushed; the <code>conntrack</code> utility must be installed to use this option. </p>
<p> The <code>-d</code> option causes the compiler to run under the Perl debugger. </p>
<p> The <code>-f</code> option suppresses the compilation step and simply reused the compiled script which last started/restarted Shorewall, provided that /etc/shorewall6 and its contents have not been modified since the last start/restart. </p>
<p> The <code>-c</code> option was added in Shorewall 4.4.20 and performs the compilation step unconditionally, overriding the AUTOMAKE setting in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5). When both <code>-f</code> and <code>-c</code> are present, the result is determined by the option that appears last. </p>
<p> The <code>-T</code> option was added in Shorewall 4.5.3 and causes a Perl stack trace to be included with each compiler-generated error and warning message. </p>
<p> The <code>-i</code> option was added in Shorewall 4.6.0 and causes a warning message to be issued if the current line contains alternative input specifications following a semicolon (&quot;;&quot;). Such lines will be handled incorrectly if INLINE_MATCHES is set to Yes in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5). </p>
<p> The <code>-C</code> option was added in Shorewall 4.6.5 and is only meaningful when AUTOMAKE=Yes in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5). If an existing firewall script is used and if that script was the one that generated the current running configuration, then the running netfilter configuration will be reloaded as is so as to preserve the iptables packet and byte counters.</dl>
<p> <code>remote-reload </code>[-<code>s</code>] [-<code>c</code>] [-<code>r</code> <i>root-user-name</i>] [-<code>T</code>] [-<code>i</code>] [ [ -D ] <i>directory</i> ] [ <i>system</i> ],</p>
<dl>
<dd>This command was added in Shorewall 5.0.0. </p>
<p> If <i>directory</i> is omitted, the current working directory is assumed. Allows a non-root user to compile a shorewall6 script and install it on a system (provided that the user has root access to the system via ssh). The command is equivalent to: </p>
<dl>
<dd>
<pre> <code>/sbin/shorewall6 compile -e</code> <i>directory</i> <i>directory</i><code>/firewall &amp;&amp;\</code>
 <code>scp</code> <i>directory</i><code>/firewall</code> <i>directory</i><code>/firewall.conf</code> <code>root@</code><i>system</i><code>:/var/lib/shorewall6-lite/ &amp;&amp;\</code>
 <code>ssh root@</code><i>system</i> <code>'/sbin/shorewall6-lite reload'</code></pre>
</dl>
<p> In other words, the configuration in the specified (or defaulted) directory is compiled to a file called firewall in that directory. If compilation succeeds, then firewall is copied to <i>system</i> using scp. If the copy succeeds, Shorewall6 Lite on <i>system</i> is restarted via ssh. Beginning with Shorewall 5.0.13, if <i>system</i> is omitted, then the FIREWALL option setting in m[blue]<code><a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5)</code>m[]<font SIZE="-2">[7]</font> is assumed. In that case, if you want to specify a <i>directory</i>, then the <code>-D</code> option must be given. </p>
<p> If <code>-s</code> is specified and the <code>restart</code> command succeeds, then the remote Shorewall6-lite configuration is saved by executing <code>shorewall6-lite save</code> via ssh. </p>
<p> if <code>-c</code> is included, the command <code>shorewall6-lite show capabilities -f &gt; /var/lib/shorewall6-lite/capabilities</code> is executed via ssh then the generated file is copied to <i>directory</i> using scp. This step is performed before the configuration is compiled. </p>
<p> If <code>-r</code> is included, it specifies that the root user on <i>system</i> is named <i>root-user-name</i> rather than &quot;root&quot;. </p>
<p> The <code>-T</code> option was added in Shorewall 4.5.3 and causes a Perl stack trace to be included with each compiler-generated error and warning message. </p>
<p> The <code>-i</code> option was added in Shorewall 4.6.0 and causes a warning message to be issued if the current line contains alternative input specifications following a semicolon (&quot;;&quot;). Such lines will be handled incorrectly if INLINE_MATCHES is set to Yes in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5).</dl>
<p> <code>remote- restart </code>[-<code>s</code>] [-<code>c</code>] [-<code>r</code> <i>root-user-name</i>] [-<code>T</code>] [-<code>i</code>] [ [ -D ] <i>directory</i> ] [ <i>system</i> ]</p>
<dl>
<dd>This command was renamed from <code>reload</code> in Shorewall 5.0.0. </p>
<p> If <i>directory</i> is omitted, the current working directory is assumed. Allows a non-root user to compile a shorewall6 script and install it on a system (provided that the user has root access to the system via ssh). The command is equivalent to: </p>
<dl>
<dd>
<pre> <code>/sbin/shorewall6 compile -e</code> <i>directory</i> <i>directory</i><code>/firewall &amp;&amp;\</code>
 <code>scp</code> <i>directory</i><code>/firewall</code> <i>directory</i><code>/firewall.conf</code> <code>root@</code><i>system</i><code>:/var/lib/shorewall6-lite/ &amp;&amp;\</code>
 <code>ssh root@</code><i>system</i> <code>'/sbin/shorewall6-lite restart'</code></pre>
</dl>
<p> In other words, the configuration in the specified (or defaulted) directory is compiled to a file called firewall in that directory. If compilation succeeds, then firewall is copied to <i>system</i> using scp. If the copy succeeds, Shorewall6 Lite on <i>system</i> is restarted via ssh. </p>
<p> Beginning with Shorewall 5.0.13, if <i>system</i> is omitted, then the FIREWALL option setting in m[blue]<code><a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5)</code>m[]<font SIZE="-2">[7]</font> is assumed. In that case, if you want to specify a <i>directory</i>, then the <code>-D</code> option must be given. </p>
<p> If <code>-s</code> is specified and the <code>restart</code> command succeeds, then the remote Shorewall6-lite configuration is saved by executing <code>shorewall6-lite save</code> via ssh. </p>
<p> if <code>-c</code> is included, the command <code>shorewall6-lite show capabilities -f &gt; /var/lib/shorewall6-lite/capabilities</code> is executed via ssh then the generated file is copied to <i>directory</i> using scp. This step is performed before the configuration is compiled. </p>
<p> If <code>-r</code> is included, it specifies that the root user on <i>system</i> is named <i>root-user-name</i> rather than &quot;root&quot;. </p>
<p> The <code>-T</code> option was added in Shorewall 4.5.3 and causes a Perl stack trace to be included with each compiler-generated error and warning message. </p>
<p> The <code>-i</code> option was added in Shorewall 4.6.0 and causes a warning message to be issued if the current line contains alternative input specifications following a semicolon (&quot;;&quot;). Such lines will be handled incorrectly if INLINE_MATCHES is set to Yes in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5).</dl>
<p> <code>remote-start </code> [-<code>s</code>] [-<code>c</code>] [-<code>r</code> <i>root-user-name</i>] [-<code>T</code>] [-<code>i</code>] [ [-D ] <i>directory</i> ] [ <i>system</i> ]</p>
<dl>
<dd>This command was added in Shorewall 5.0.0. </p>
<p> If <i>directory</i> is omitted, the current working directory is assumed. Allows a non-root user to compile a shorewall6 script and install it on a system (provided that the user has root access to the system via ssh). The command is equivalent to: </p>
<dl>
<dd>
<pre> <code>/sbin/shorewall6 compile -e</code> <i>directory</i> <i>directory</i><code>/firewall &amp;&amp;\</code>
 <code>scp</code> <i>directory</i><code>/firewall</code> <i>directory</i><code>/firewall.conf</code> <code>root@</code><i>system</i><code>:/var/lib/shorewall6-lite/ &amp;&amp;\</code>
 <code>ssh root@</code><i>system</i> <code>'/sbin/shorewall6-lite start'</code></pre>
</dl>
<p> In other words, the configuration in the specified (or defaulted) directory is compiled to a file called firewall in that directory. If compilation succeeds, then firewall is copied to <i>system</i> using scp. If the copy succeeds, Shorewall6 Lite on <i>system</i> is started via ssh. Beginning with Shorewall 5.0.13, if <i>system</i> is omitted, then the FIREWALL option setting in m[blue]<code><a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5)</code>m[]<font SIZE="-2">[7]</font> is assumed. In that case, if you want to specify a <i>directory</i>, then the <code>-D</code> option must be given. </p>
<p> If <code>-s</code> is specified and the <code>start</code> command succeeds, then the remote Shorewall6-lite configuration is saved by executing <code>shorewall6-lite save</code> via ssh. </p>
<p> if <code>-c</code> is included, the command <code>shorewall6-lite show capabilities -f &gt; /var/lib/shorewall6-lite/capabilities</code> is executed via ssh then the generated file is copied to <i>directory</i> using scp. This step is performed before the configuration is compiled. </p>
<p> If <code>-r</code> is included, it specifies that the root user on <i>system</i> is named <i>root-user-name</i> rather than &quot;root&quot;. </p>
<p> The <code>-T</code> option was added in Shorewall 4.5.3 and causes a Perl stack trace to be included with each compiler-generated error and warning message. </p>
<p> The <code>-i</code> option was added in Shorewall 4.6.0 and causes a warning message to be issued if the current line contains alternative input specifications following a semicolon (&quot;;&quot;). Such lines will be handled incorrectly if INLINE_MATCHES is set to Yes in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5).</dl>
<p> <code>reset [</code><i>chain</i><code>, &#8230;]</code></p>
<dl>
<dd>Resets the packet and byte counters in the specified <i>chain</i>(s). If no <i>chain</i> is specified, all the packet and byte counters in the firewall are reset. </p>
<p> Beginning with Shorewall 5.0.0, <i>chain</i> may be composed of both a table name and a chain name separated by a colon (e.g., mangle:PREROUTING). Chain names following that don&#8217;t include a table name are assumed to be in that same table. If no table name is given in the command, the filter table is assumed.</dl>
<p> <code>restart </code>[-<code>n</code>] [-<code>p</code>] [-<code>d</code>] [-<code>f</code>] [-<code>c</code>] [-<code>T</code>] [-<code>i</code>] [-<code>C</code>] [ <i>directory</i> ]</p>
<dl>
<dd>Beginning with Shorewall 5.0.0, this command performs a true restart. The firewall is completely stopped as if a <code>stop</code> command had been issued then it is started again. </p>
<p> If a <i>directory</i> is included in the command, Shorewall6 will look in that <i>directory</i> first for configuration files. </p>
<p> The <code>-n</code> option causes Shorewall6 to avoid updating the routing table(s). </p>
<p> The <code>-p</code> option causes the connection tracking table to be flushed; the <code>conntrack</code> utility must be installed to use this option. </p>
<p> The <code>-d</code> option causes the compiler to run under the Perl debugger. </p>
<p> The <code>-f</code> option suppresses the compilation step and simply reused the compiled script which last started/restarted Shorewall, provided that /etc/shorewall6 and its contents have not been modified since the last start/restart. </p>
<p> The <code>-c</code> option was added in Shorewall 4.4.20 and performs the compilation step unconditionally, overriding the AUTOMAKE setting in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5). When both <code>-f</code> and <code>-c</code> are present, the result is determined by the option that appears last. </p>
<p> The <code>-T</code> option was added in Shorewall 4.5.3 and causes a Perl stack trace to be included with each compiler-generated error and warning message. </p>
<p> The <code>-i</code> option was added in Shorewall 4.6.0 and causes a warning message to be issued if the current line contains alternative input specifications following a semicolon (&quot;;&quot;). Such lines will be handled incorrectly if INLINE_MATCHES is set to Yes in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5). </p>
<p> The <code>-C</code> option was added in Shorewall 4.6.5 and is only meaningful when AUTOMAKE=Yes in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5). If an existing firewall script is used and if that script was the one that generated the current running configuration, then the running netfilter configuration will be reloaded as is so as to preserve the iptables packet and byte counters.</dl>
<p> <code>restore </code>[-<code>n</code>] [-<code>p</code>] [-<code>C</code>] [ <i>filename</i> ]</p>
<dl>
<dd>Restore Shorewall6 to a state saved using the <code>shorewall6 save</code> command. Existing connections are maintained. The <i>filename</i> names a restore file in /var/lib/shorewall6 created using <code>shorewall6 save</code>; if no <i>filename</i> is given then Shorewall6 will be restored from the file specified by the RESTOREFILE option in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5). </p>
<dl>
<dd><font SIZE="+1"> <code>Caution</code> </font><br />
 If your ip6tables ruleset depends on variables that are detected at run-time, either in your params file or by Shorewall-generated code, <code>restore</code> will use the values that were current when the ruleset was saved, which may be different from the current values. </p>
</dl>
<p> The <code>-C</code> option was added in Shorewall 4.6.5. If the <code>-C</code> option was specified during <code>shorewall6 save</code>, then the counters saved by that operation will be restored.</dl>
<p> <code>run</code><i>command</i> [ <i>parameter</i> &#8230; ]</p>
<dl>
<dd>Added in Shorewall 4.6.3. Executes <i>command</i> in the context of the generated script passing the supplied <i>parameter</i>s. Normally, the <i>command</i> will be a function declared in lib.private. </p>
<p> Before executing the <i>command</i>, the script will detect the configuration, setting all SW_* variables and will run your init extension script with $COMMAND = &#8216;run&#8217;. </p>
<p> If there are files in the CONFIG_PATH that were modified after the current firewall script was generated, the following warning message is issued before the script&#8217;s run command is executed: </p>
<dl>
<dd>
<pre>WARNING: /var/lib/shorewall6/firewall is not up to
 date</pre>
</dl>
</dl>
<p> <code>safe-restart </code>[-<code>d</code>] [-<code>p</code>] [-<code>t</code><i>timeout</i> ] [ <i>directory</i> ]</p>
<dl>
<dd>Only allowed if Shorewall6 is running. The current configuration is saved in /var/lib/shorewall6/safe-restart (see the <code>save</code> command below) then a <code>shorewall6 restart</code> is done. You will then be prompted asking if you want to accept the new configuration or not. If you answer &quot;n&quot; or if you fail to answer within 60 seconds (such as when your new configuration has disabled communication with your terminal), the configuration is restored from the saved configuration. If a directory is given, then Shorewall6 will look in that directory first when opening configuration files. </p>
<p> Beginning with Shorewall 4.5.0, you may specify a different <i>timeout</i> value using the <code>-t</code> option. The numeric <i>timeout</i> may optionally be followed by an <code>s</code>, <code>m</code> or <code>h</code> suffix (e.g., 5m) to specify seconds, minutes or hours respectively. If the suffix is omitted, seconds is assumed.</dl>
<p> <code>safe-start </code>[-<code>d</code>] [-<code>p</code>] [-<code>t</code><i>timeout</i> ] [ <i>directory</i> ]</p>
<dl>
<dd>Shorewall6 is started normally. You will then be prompted asking if everything went all right. If you answer &quot;n&quot; or if you fail to answer within 60 seconds (such as when your new configuration has disabled communication with your terminal), a shorewall6 clear is performed for you. If a directory is given, then Shorewall6 will look in that directory first when opening configuration files. </p>
<p> Beginning with Shorewall 4.5.0, you may specify a different <i>timeout</i> value using the <code>-t</code> option. The numeric <i>timeout</i> may optionally be followed by an <code>s</code>, <code>m</code> or <code>h</code> suffix (e.g., 5m) to specify seconds, minutes or hours respectively. If the suffix is omitted, seconds is assumed.</dl>
<p> <code>save </code>[-<code>C</code>] [ <i>filename</i> ]</p>
<dl>
<dd>The dynamic blacklist is stored in /var/lib/shorewall6/save. The state of the firewall is stored in /var/lib/shorewall6/<i>filename</i> for use by the <code>shorewall6 restore</code> and <code> shorewall6 -f start</code> commands. If <i>filename </i> is not given then the state is saved in the file specified by the RESTOREFILE option in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5). </p>
<p> The <code>-C</code> option, added in Shorewall 4.6.5, causes the ip6tables packet and byte counters to be saved along with the chains and rules.</dl>
<p> <code>savesets</code></p>
<dl>
<dd>Added in shorewall 4.6.8. Performs the same action as the <code>stop</code> command with respect to saving ipsets (see the SAVE_IPSETS option in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font> (5)). This command may be used to proactively save your ipset contents in the event that a system failure occurs prior to issuing a <code>stop</code> command.</dl>
<p> <code>show</code></p>
<dl>
<dd>The show command can have a number of different arguments: </p>
<p> <code>actions</code></p>
<dl>
<dd>Produces a report about the available actions (built-in, standard and user-defined).</dl>
<p> [-<code>x</code>] <code>bl|blacklists </code></p>
<dl>
<dd>Added in Shorewall 4.6.2. Displays the dynamic chain along with any chains produced by entries in <a href="/docs/linux/man/5-shorewall-blrules/">shorewall-blrules</a>(5).The <code>-x</code> option is passed directly through to ip6tables and causes actual packet and byte counts to be displayed. Without this option, those counts are abbreviated.</dl>
<p> [-<code>f</code>] <code>capabilities</code></p>
<dl>
<dd>Displays your kernel/ip6tables capabilities. The <code>-f</code> option causes the display to be formatted as a capabilities file for use with <code>shorewall6 compile -e</code>.</dl>
<p> [-<code>b</code>] [-<code>x</code>] [-<code>l</code>] [-<code>t</code> {<code>filter</code>|<code>mangle</code>|<code>nat</code>|<code>raw</code>|<code>rawpost</code>}][ <i>chain</i>&#8230; ]</p>
<dl>
<dd>The rules in each <i>chain</i> are displayed using the <code>ip6tables -L</code><i>chain</i><code>-n -v</code> command. If no <i>chain</i> is given, all of the chains in the filter table are displayed. The <code>-x</code> option is passed directly through to ip6tables and causes actual packet and byte counts to be displayed. Without this option, those counts are abbreviated. The <code>-t</code> option specifies the Netfilter table to display. The default is <code>filter</code>. </p>
<p> The <code>-b</code> (&#8216;brief&#8217;) option causes rules which have not been used (i.e. which have zero packet and byte counts) to be omitted from the output. Chains with no rules displayed are also omitted from the output. </p>
<p> The <code>-l</code> option causes the rule number for each Netfilter rule to be displayed. </p>
<p> If the <code>-t</code> option and the <code>chain</code> keyword are both omitted and any of the listed <i>chain</i>s do not exist, a usage message is displayed.</dl>
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
<dd>Displays the system&#8217;s IPv6 configuration.</dl>
<p> [-<code>m</code>] <code>log</code></p>
<dl>
<dd>Displays the last 20 Shorewall6 messages from the log file specified by the LOGFILE option in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5). The <code>-m</code> option causes the MAC address of each packet source to be displayed if that information is available.</dl>
<p> <code>macros</code></p>
<dl>
<dd>Displays information about each macro defined on the firewall system.</dl>
<p> <code>macro </code><i>macro</i></p>
<dl>
<dd>Added in Shorewall 4.4.6. Displays the file that implements the specified <i>macro</i> (usually /usr/share/shorewall6/macro.<i>macro</i>).</dl>
<p> [-<code>x</code>] <code>mangle</code></p>
<dl>
<dd>Displays the Netfilter mangle table using the command <code>ip6tables -t mangle -L -n -v</code>.The <code>-x</code> option is passed directly through to ip6tables and causes actual packet and byte counts to be displayed. Without this option, those counts are abbreviated.</dl>
<p> <code>marks</code></p>
<dl>
<dd>Added in Shorewall 4.4.26. Displays the various fields in packet marks giving the min and max value (in both decimal and hex) and the applicable mask (in hex).</dl>
<p> [-<code>x</code>] <code>nat</code></p>
<dl>
<dd>Displays the Netfilter nat table using the command <code>ip6tables -t nat -L -n -v</code>. The <code>-x</code> option is passed directly through to ip6tables and causes actual packet and byte counts to be displayed. Without this option, those counts are abbreviated.</dl>
<p> <code>opens</code></p>
<dl>
<dd>Added in Shorewall 4.5.8. Displays the iptables rules in the &#8216;dynamic&#8217; chain created through use of the <code>open </code>command..</dl>
<p> <code>policies</code></p>
<dl>
<dd>Added in Shorewall 4.4.4. Displays the applicable policy between each pair of zones. Note that implicit intrazone ACCEPT policies are not displayed for zones associated with a single network where that network doesn&#8217;t specify <code>routeback</code>.</dl>
<p> [-<code>x</code>] <code>raw</code></p>
<dl>
<dd>Displays the Netfilter raw table using the command <code>ip6tables -t raw -L -n -v</code>. The <code>-x</code> option is passed directly through to ip6tables and causes actual packet and byte counts to be displayed. Without this option, those counts are abbreviated.</dl>
<p> <code>[-</code><code>c</code><code>]</code><code>routing</code></p>
<dl>
<dd>Displays the system&#8217;s IPv6 routing configuration. The -c option causes the route cache to be displayed in addition to the other routing information.</dl>
<p> <code>tc</code></p>
<dl>
<dd>Displays information about queuing disciplines, classes and filters.</dl>
<p> <code>zones</code></p>
<dl>
<dd>Displays the current composition of the Shorewall6 zones on the system.</dl>
</dl>
<p> <code>start </code>[-<code>n</code>] [-<code>p</code>] [-<code>d</code>] [-<code>f</code>] [-<code>c</code>] [-<code>T</code>] [-<code>i</code>] [-<code>C</code>] [ <i>directory</i> ]</p>
<dl>
<dd>Start shorewall6. Existing connections through shorewall6 managed interfaces are untouched. New connections will be allowed only if they are allowed by the firewall rules or policies. If a <i>directory</i> is included in the command, Shorewall6 will look in that <i>directory</i> first for configuration files. If <code>-f</code> is specified, the saved configuration specified by the RESTOREFILE option in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5) will be restored if that saved configuration exists and has been modified more recently than the files in /etc/shorewall6. When <code>-f </code> is given, a <i>directory</i> may not be specified. </p>
<p> Update: In Shorewall6 4.4.20, a new LEGACY_FASTSTART option was added to m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5). When LEGACY_FASTSTART=No, the modification times of files in /etc/shorewall6 are compared with that of /var/lib/shorewall6/firewall (the compiled script that last started/restarted the firewall). </p>
<p> The <code>-n</code> option causes Shorewall6 to avoid updating the routing table(s). </p>
<p> The <code>-c</code> option was added in Shorewall 4.4.20 and performs the compilation step unconditionally, overriding the AUTOMAKE setting in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5). When both <code>-f</code> and <code>-c</code> are present, the result is determined by the option that appears last. </p>
<p> The <code>-T</code> option was added in Shorewall 4.5.3 and causes a Perl stack trace to be included with each compiler-generated error and warning message. </p>
<p> The <code>-i</code> option was added in Shorewall 4.6.0 and causes a warning message to be issued if the current line contains alternative input specifications following a semicolon (&quot;;&quot;). Such lines will be handled incorrectly if INLINE_MATCHES is set to Yes in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5). </p>
<p> The <code>-C</code> option was added in Shorewall 4.6.5 and is only meaningful when the <code>-f</code> option is also specified. If the previously-saved configuration is restored, and if the <code>-C</code> option was also specified in the <code>save</code> command, then the packet and byte counters will be restored along with the chains and rules.</dl>
<p> <code>stop </code>[-<code>f</code>]</p>
<dl>
<dd>Stops the firewall. All existing connections, except those listed in m[blue]<code>shorewall6-routestopped</code>m[]<font SIZE="-2">[8]</font>(5) or permitted by the ADMINISABSENTMINDED option in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font>(5), are taken down. The only new traffic permitted through the firewall is from systems listed in m[blue]<code>shorewall6-routestopped</code>m[]<font SIZE="-2">[8]</font>(5) or by ADMINISABSENTMINDED. </p>
<p> If <code>-f</code> is given, the command will be processed by the compiled script that executed the last successful <code>start</code>, <code>restart</code> or <code>refresh</code> command if that script exists.</dl>
<p> <code>status</code></p>
<dl>
<dd>Produces a short report about the state of the Shorewall6-configured firewall. </p>
<p> The <code>-i</code> option was added in Shorewall 4.6.2 and causes the status of each optional or provider interface to be displayed.</dl>
<p> <code>try </code><i>directory</i> [ <i>timeout</i> ]</p>
<dl>
<dd>If Shorewall6 is started then the firewall state is saved to a temporary saved configuration (/var/lib/shorewall6/.try). Next, if Shorewall6 is currently started then a <code>restart</code> command is issued using the specified configuration <i>directory</i>; otherwise, a <code>start</code> command is performed using the specified configuration <i>directory</i>. If an error occurs during the compilation phase of the <code>restart</code> or <code>start </code>, the command terminates without changing the Shorewall6 state. If an error occurs during the <code>restart </code> phase, then a <code>shorewall6 restore</code> is performed using the saved configuration. If an error occurs during the <code>start</code> phase, then Shorewall6 is cleared. If the <code>start</code>/ <code>restart</code> succeeds and a <i>timeout</i> is specified then a <code>clear</code> or <code>restore </code> is performed after <i>timeout</i> seconds. </p>
<p> Beginning with Shorewall 4.5.0, the numeric <i>timeout</i> may optionally be followed by an <code>s</code>, <code>m</code> or <code>h</code> suffix (e.g., 5m) to specify seconds, minutes or hours respectively. If the suffix is omitted, seconds is assumed.</dl>
<p> <code>update</code> [-<code>d</code>] [-<code>r</code>] [-<code>T</code>] [-<code>a</code>] [-<code>i</code>] [-<code>A</code>] [ <i>directory</i> ]</p>
<dl>
<dd>Added in Shorewall 4.4.21 and causes the compiler to update /etc/shorewall/shorewall.conf then validate the configuration. The update will add options not present in the old file with their default values, and will move deprecated options with non-defaults to a deprecated options section at the bottom of the file. Your existing shorewall.conf file is renamed shorewall.conf.bak. </p>
<p> The command was extended over the years with a set of options that caused additional configuration updates. </p>
<dl>
<dd>&bull; Convert an existing blacklist file into an equivalent blrules file.</dl>
<dl>
<dd>&bull; Convert an existing routestopped file into an equivalent stoppedrules file.</dl>
<dl>
<dd>&bull; Convert existing tcrules and tos files into an equivalent mangle file.</dl>
<dl>
<dd>&bull; Convert an existing notrack file into an equivalent conntrack file.</dl>
<dl>
<dd>&bull; Convert FORMAT, SECTION and COMMENT entries into ?FORMAT, ?SECTION and ?COMMENT directives.</dl>
<p> In each case, the old file is renamed with a .bak suffix. </p>
<p> In Shorewall 5.0.0, the options were eliminated and the <code>update</code> command performs all of the updates described above. </p>
<dl>
<dd><font SIZE="+1"> <code>Important</code> </font><br />
 There are some notable restrictions with the <code>update</code> command: </p>
<dl>
<dd>1. Converted rules will be appended to the existing file; if there is no existing file in the CONFIG_PATH, one will be created in the directory specified in the command or in the first entry in the CONFIG_PATH (normally /etc/shorewall6) otherwise.</dl>
<dl>
<dd>2. Existing comments in the file being converted will not be transferred to the output file.</dl>
<dl>
<dd>3. INCLUDEd files will be expanded inline in the output file.</dl>
<dl>
<dd>4. Columns in the output file will be separated by a single tab character; there is no attempt made to otherwise align the columns.</dl>
</dl>
<p> The <code>-a</code> option causes the updated shorewall.conf file to be annotated with documentation. </p>
<p> The <code>-i</code> option was added in Shorewall 4.6.0 and causes a warning message to be issued if the current line contains alternative input specifications following a semicolon (&quot;;&quot;). Such lines will be handled incorrectly if INLINE_MATCHES is set to Yes in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[9]</font>(5). </p>
<p> The <code>-A</code> option is included for compatibility with Shorewall 4.6 and is equivalent to specifying the <code>-i</code> option. </p>
<p> For a description of the other options, see the <code>check</code> command above.</dl>
<p> <code>version [-</code><code>a</code><code>]</code></p>
<dl>
<dd>Displays Shorewall6&#8217;s version. If the <code>-a</code> option is included, the version of Shorewall will also be displayed.</dl>
<h2>Exit Status</h2>
<p>In general, when a command succeeds, status 0 is returned; when the command fails, a non-zero status is returned. </p>
<p> The <code>status</code> command returns exit status as follows: </p>
<p> 0 &#8211; Firewall is started. </p>
<p> 3 &#8211; Firewall is stopped or cleared </p>
<p> 4 &#8211; Unknown state; usually means that the firewall has never been started.</p>
<h2>Environment</h2>
<p>Two environmental variables are recognized by Shorewall6: </p>
<p> SHOREWALL_INIT_SCRIPT</p>
<dl>
<dd>When set to 1, causes Std out to be redirected to the file specified in the STARTUP_LOG option in m[blue]<code><a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5)</code>m[]<font SIZE="-2">[7]</font>.</dl>
<p> SW_LOGGERTAG</p>
<dl>
<dd>Added in Shorewall 5.0.8. When set to a non-empty value, that value is passed to the logger utility in its -t (&#8211;tag) option.</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/starting_and_stopping_shorewall.htm">http://www.shorewall.net/starting_and_stopping_shorewall.htm</a></code>m[]<font SIZE="-2">[10]</font> </p>
<p> <a href="/docs/linux/man/5-shorewall6-accounting/">shorewall6-accounting</a>(5), <a href="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5), <a href="/docs/linux/man/5-shorewall6-blacklist/">shorewall6-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall6-hosts/">shorewall6-hosts</a>(5), <a href="/docs/linux/man/5-shorewall6-interfaces/">shorewall6-interfaces</a>(5), <a href="/docs/linux/man/5-shorewall6-maclist/">shorewall6-maclist</a>(5), <a href="/docs/linux/man/5-shorewall6-netmap/">shorewall6-netmap</a>(5),<a href="/docs/linux/man/5-shorewall6-params/">shorewall6-params</a>(5), <a href="/docs/linux/man/5-shorewall6-policy/">shorewall6-policy</a>(5), <a href="/docs/linux/man/5-shorewall6-providers/">shorewall6-providers</a>(5), <a href="/docs/linux/man/5-shorewall6-rtrules/">shorewall6-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall6-routestopped/">shorewall6-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall6-rules/">shorewall6-rules</a>(5), <a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5), <a href="/docs/linux/man/5-shorewall6-secmarks/">shorewall6-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall6-tcclasses/">shorewall6-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall6-tcdevices/">shorewall6-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall6-tcrules/">shorewall6-tcrules</a>(5), <a href="/docs/linux/man/5-shorewall6-tos/">shorewall6-tos</a>(5), <a href="/docs/linux/man/5-shorewall6-tunnels/">shorewall6-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall6-zones/">shorewall6-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/starting_and_stopping_shorewall.htm#Trace">http://www.shorewall.net/starting_and_stopping_shorewall.htm#Trace</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/starting_and_stopping_shorewall.htm#Trace">http://www.shorewall.net/starting_and_stopping_shorewall.htm#Trace</a></dl>
<dt> 2.</p>
<dd>shorewall6.conf</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6.conf.html">http://www.shorewall.net/manpages6/shorewall6.conf.html</a></dl>
<dt> 3.</p>
<dd>shorewall6-interfaces</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-interfaces.html">http://www.shorewall.net/manpages6/shorewall6-interfaces.html</a></dl>
<dt> 4.</p>
<dd>shorewall6-zones</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-zones.html">http://www.shorewall.net/manpages6/shorewall6-zones.html</a></dl>
<dt> 5.</p>
<dd>shorewall6-routes</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-routes.html">http://www.shorewall.net/manpages6/shorewall6-routes.html</a></dl>
<dt> 6.</p>
<dd>logging backend</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/shorewall_logging.html#Backends">http://www.shorewall.net/shorewall_logging.html#Backends</a></dl>
<dt> 7.</p>
<dd><a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5)</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.netshorewall6.conf.html">http://www.shorewall.netshorewall6.conf.html</a></dl>
<dt> 8.</p>
<dd>shorewall6-routestopped</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-routestopped.html">http://www.shorewall.net/manpages6/shorewall6-routestopped.html</a></dl>
<dt> 9.</p>
<dd>shorewall.conf</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall.conf.html">http://www.shorewall.net/manpages/shorewall.conf.html</a></dl>
<dt>10.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/starting_and_stopping_shorewall.htm">http://www.shorewall.net/starting_and_stopping_shorewall.htm</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/starting_and_stopping_shorewall.htm">http://www.shorewall.net/starting_and_stopping_shorewall.htm</a></dl>
