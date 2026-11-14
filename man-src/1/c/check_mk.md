---
title: "check_mk(1)"
name: "check_mk"
section: "1"
letter: "c"
url: "/docs/linux/man/1-check_mk/"
description: "check_mk – command line utility for managing Check_MK"
---

<h2 class="name">NAME</h2>
<p> check_mk &#8211; command line utility for managing Check_MK</p>
<h2>SYNOPSIS</h2>
<p> <code>check_mk</code> [<i>GLOBAL OPTIONS</i>] [<i>MODE</i>] [<i>MODE OPTIONS</i>] [<i>ARGUMENTS&#8230;</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>check_mk</code> (or its alias <code>cmk</code>) is a command line utility for managing some aspects of the Check_MK Monitoring System. It can be used for diagnosis, for automating things in scripts and for doing some tasks more efficiently than with the web based WATO. </p>
<h2>GENERIC OPTIONS</h2>
<p> The following options work in all modes and all situations. </p>
<dl>
<dt><code>-v</code></p>
<dd> More verbose output. In good old Unix tradition check_mk only outputs texts if something goes wrong. By using <code>-v</code> you can get some more information about what&#8217;s going on. </p>
<dt><code>-vv</code></p>
<dd> Even more vebose output. Some operations give even more details when this options is used. </p>
<dt><code>&#8211;debug</code></p>
<dd> Disables the intern exception handling in Check_MK and let all Python exceptions through. That way you can see the exact location in the code where the actual problem is. This helps finding problems in self written check plugins. </p>
</dl>
<h2>SERVICE DISCOVERY</h2>
<p> <code>cmk [&#8211;checks=CHECK_TYPE1,CHECK_TYPE2,&#8230;] -I|-II [HOSTS&#8230;]</code> </p>
<p> The options <code>-I</code> and <code>-II</code> do service discovery. Check_MK will analyse the agent output of the specified hosts (or all hosts if none are specified) and automatically create monitored services where it does make sense. While <code>-I</code> only creates new services and keeps the existing ones untouched, <code>-II</code> first removes all existing services before staring the discovery. </p>
<p> The option <code>&#8211;checks=</code> restricts the option to a list of check types (e.g. <code>&#8211;checks=Bdf,diskstat</code>). When combined with the mode <code>-II</code> only checks of the specified types are be removed and rediscovered. </p>
<p> When no hosts are specified then Check_MK will do a discovery for <code>all</code> hosts that are defined in your configuration. In order to speed this operation up no actual data is being fetched from the hosts but cached agent data will be used. When you specify host names then fresh data is fetched from these. </p>
<h2>AD HOC CHECKING</h2>
<p> <code>cmk [-n] [-p] [&#8211;checks=CHECK_TYPE1,CHECK_TYPE2,&#8230;] -v HOST</code> </p>
<p> This does an ad hoc checking of the host HOST via Check_MK. HOST must be a host that is configured in Check_MK. Check_MK does the same like in real monitoring &#8211; it fetches data from the agent and computes the result of all services. Then it outputs each result and sends the result to the monitoring core. </p>
<p> <code>-p</code> Also prints metrics data of the services. </p>
<p> <code>-n</code> Prevents the check results from being sent to the monitoring core. That way </p>
<p> <code>-v</code> Outputs the results of the passive checks on the terminal. Without this option Check_MK behaves like a classical monitoring plugin: it outputs one line of text (essentially the output of the <i>Check_MK</i> service) and exists with 0, 1, 2 or 3 (OK, WARN, CRIT, UNKNOWN). This was how Nagios called Check_MK in ancient times. </p>
<p> The option <code>&#8211;checks=</code> restricts the option to a list of check types (e.g. <code>&#8211;checks=Bdf,diskstat</code>). That way only a reduced set of service is being checked. This is useful for testing and debugging a check plugin. </p>
<h2>check_mk</h2>
<p>&nbsp;<wbr>cmk&nbsp;<wbr>[-n]&nbsp;<wbr>[-v]&nbsp;<wbr>[-p]&nbsp;<wbr>HOST&nbsp;<wbr>[IPADDRESS]&nbsp;<wbr>&nbsp;<wbr>check all services on HOST<br />
&nbsp;<wbr>cmk -I&nbsp;<wbr>[HOST ..]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>inventory &#8211; find new services<br />
&nbsp;<wbr>cmk -II &#8230;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>renew inventory, drop old services<br />
&nbsp;<wbr>cmk -N&nbsp;<wbr>[HOSTS&#8230;]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>output Nagios configuration<br />
&nbsp;<wbr>cmk -B&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>create configuration for core<br />
&nbsp;<wbr>cmk -C, &#8211;compile&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>precompile host checks<br />
&nbsp;<wbr>cmk -U, &#8211;update&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>precompile&nbsp;<wbr>+&nbsp;<wbr>create config for core<br />
&nbsp;<wbr>cmk -O, &#8211;reload&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>precompile&nbsp;<wbr>+&nbsp;<wbr>config&nbsp;<wbr>+&nbsp;<wbr>core reload<br />
&nbsp;<wbr>cmk -R, &#8211;restart&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>precompile&nbsp;<wbr>+&nbsp;<wbr>config&nbsp;<wbr>+&nbsp;<wbr>core restart<br />
&nbsp;<wbr>cmk -D, &#8211;dump&nbsp;<wbr>[H1 H2 ..]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>dump all or some hosts<br />
&nbsp;<wbr>cmk -d HOSTNAME|IPADDRESS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show raw information from agent<br />
&nbsp;<wbr>cmk &#8211;check-discovery HOSTNAME&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>check for items not yet checked<br />
&nbsp;<wbr>cmk &#8211;discover-marked-hosts&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>run discovery for hosts known to have changed services<br />
&nbsp;<wbr>cmk &#8211;update-dns-cache&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>update IP address lookup cache<br />
&nbsp;<wbr>cmk -l, &#8211;list-hosts&nbsp;<wbr>[G1 G2 &#8230;]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print list of all hosts<br />
&nbsp;<wbr>cmk &#8211;list-tag TAG1 TAG2 &#8230;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list hosts having certain tags<br />
&nbsp;<wbr>cmk -L, &#8211;list-checks&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list all available check types<br />
&nbsp;<wbr>cmk -M, &#8211;man&nbsp;<wbr>[CHECKTYPE]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show manpage for check CHECKTYPE<br />
&nbsp;<wbr>cmk -m, &#8211;browse-man&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>open interactive manpage browser<br />
&nbsp;<wbr>cmk &#8211;paths&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list all pathnames and directories<br />
&nbsp;<wbr>cmk -X, &#8211;check-config&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>check configuration for invalid vars<br />
&nbsp;<wbr>cmk &#8211;backup BACKUPFILE.tar.gz&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>make backup of configuration and data<br />
&nbsp;<wbr>cmk &#8211;restore BACKUPFILE.tar.gz&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>restore configuration and data<br />
&nbsp;<wbr>cmk &#8211;flush&nbsp;<wbr>[HOST1 HOST2&#8230;]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>flush all data of some or all hosts<br />
&nbsp;<wbr>cmk &#8211;donate&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Email data of configured hosts to MK<br />
&nbsp;<wbr>cmk &#8211;snmpwalk HOST1 HOST2 &#8230;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Do snmpwalk on one or more hosts<br />
&nbsp;<wbr>cmk &#8211;snmptranslate HOST&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Do snmptranslate on walk<br />
&nbsp;<wbr>cmk &#8211;snmpget OID HOST1 HOST2 &#8230;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Fetch single OIDs and output them<br />
&nbsp;<wbr>cmk &#8211;scan-parents&nbsp;<wbr>[HOST1 HOST2&#8230;]&nbsp;<wbr>&nbsp;<wbr>autoscan parents, create conf.d/parents.mk<br />
&nbsp;<wbr>cmk -P, &#8211;package COMMAND&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>do package operations<br />
&nbsp;<wbr>cmk &#8211;localize COMMAND&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>do localization operations<br />
&nbsp;<wbr>cmk &#8211;handle-alerts&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>used to handle alerts from core<br />
&nbsp;<wbr>cmk &#8211;notify&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>used to send notifications from core<br />
&nbsp;<wbr>cmk &#8211;create-rrd&nbsp;<wbr>[&#8211;keepalive|SPEC]&nbsp;<wbr>&nbsp;<wbr>create round robin database&nbsp;<wbr>(only CEE)<br />
&nbsp;<wbr>cmk &#8211;convert-rrds&nbsp;<wbr>[&#8211;split]&nbsp;<wbr>[H&#8230;]&nbsp;<wbr>&nbsp;<wbr>convert exiting RRD to new format&nbsp;<wbr>(only CEE)<br />
&nbsp;<wbr>cmk &#8211;compress-history FILES&#8230;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>optimize monitoring history files for CMC<br />
&nbsp;<wbr>cmk &#8211;handle-alerts&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>alert handling, always in keepalive mode&nbsp;<wbr>(only CEE)<br />
&nbsp;<wbr>cmk -i, &#8211;inventory&nbsp;<wbr>[HOST1 HOST2&#8230;]&nbsp;<wbr>Do a HW/SW-Inventory of some ar all hosts<br />
&nbsp;<wbr>cmk &#8211;inventory-as-check HOST&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Do HW/SW-Inventory, behave like check plugin<br />
&nbsp;<wbr>cmk -A, &#8211;bake-agents&nbsp;<wbr>[-f]&nbsp;<wbr>[H1 H2..]&nbsp;<wbr>Bake agents for hosts&nbsp;<wbr>(not in all versions)<br />
&nbsp;<wbr>cmk &#8211;cap pack|unpack|list FILE.cap&nbsp;<wbr>&nbsp;<wbr>Pack/unpack agent packages&nbsp;<wbr>(not in all versions)<br />
&nbsp;<wbr>cmk &#8211;show-snmp-stats&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Analyzes recorded Inline SNMP statistics<br />
&nbsp;<wbr>cmk -V, &#8211;version&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print version<br />
&nbsp;<wbr>cmk -h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print this help </p>
<p> OPTIONS:<br />
&nbsp;<wbr>&nbsp;<wbr>-v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show what&#8217;s going on<br />
&nbsp;<wbr>&nbsp;<wbr>-p&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>also show performance data&nbsp;<wbr>(use with -v)<br />
&nbsp;<wbr>&nbsp;<wbr>-n&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>do not submit results to core, do not save counters<br />
&nbsp;<wbr>&nbsp;<wbr>-c FILE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>read config file FILE instead of&nbsp;<wbr>%s<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;cache&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>read info from cache file is present and fresh, use TCP<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>only, if cache file is absent or too old<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;no-cache&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>never use cached information<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;no-tcp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>for -I: only use cache files. Skip hosts without<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cache files.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;fake-dns IP&nbsp;<wbr>&nbsp;<wbr>fake IP addresses of all hosts to be IP. This<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>prevents DNS lookups.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;usewalk&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use snmpwalk stored with &#8211;snmpwalk<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;debug&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>never catch Python exceptions<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;interactive&nbsp;<wbr>&nbsp;<wbr>Some errors are only reported in interactive mode, i.e. if stdout<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>is a TTY. This option forces interactive mode even if the output<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>is directed into a pipe or file.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;procs N&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>start up to N processes in parallel during &#8211;scan-parents<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;checks A,..&nbsp;<wbr>&nbsp;<wbr>restrict checks/inventory to specified checks&nbsp;<wbr>(tcp/snmp/check type)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;keepalive&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>used by Check_MK Mirco Core: run check and &#8211;notify<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>in continous mode. Read data from stdin and from cmd line.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;cmc-file=X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>relative filename for CMC config file&nbsp;<wbr>(used by -B/-U)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;extraoid A&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Do &#8211;snmpwalk also on this OID, in addition to mib-2 and enterprises.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>You can specify this option multiple times.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;oid A&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Do &#8211;snmpwalk on this OID instead of mib-2 and enterprises.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>You can specify this option multiple times.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;hw-changes=S &#8211;inventory-as-check: Use monitoring state S for HW changes<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;sw-changes=S &#8211;inventory-as-check: Use monitoring state S for SW changes </p>
<p> NOTES:<br />
&nbsp;<wbr>&nbsp;<wbr>-I can be restricted to certain check types. Write&nbsp;<wbr>&#8216;&#8211;checks df -I&#8217;&nbsp;<wbr>if you<br />
&nbsp;<wbr>&nbsp;<wbr>just want to look for new filesystems. Use&nbsp;<wbr>&#8216;check_mk -L&#8217;&nbsp;<wbr>for a list<br />
&nbsp;<wbr>&nbsp;<wbr>of all check types. Use&nbsp;<wbr>&#8216;tcp&#8217;&nbsp;<wbr>for all TCP based checks and&nbsp;<wbr>&#8216;snmp&#8217;&nbsp;<wbr>for<br />
&nbsp;<wbr>&nbsp;<wbr>all SNMP based checks. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-II does the same as -I but deletes all existing checks of the<br />
&nbsp;<wbr>&nbsp;<wbr>specified types and hosts. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-N outputs the Nagios configuration. You may optionally add a list<br />
&nbsp;<wbr>&nbsp;<wbr>of hosts. In that case the configuration is generated only for<br />
&nbsp;<wbr>&nbsp;<wbr>that hosts&nbsp;<wbr>(useful for debugging). </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-U redirects both the output of -S and -H to the file&nbsp;<wbr>%s<br />
&nbsp;<wbr>&nbsp;<wbr>and also calls check_mk -C. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-D, &#8211;dump dumps out the complete configuration and information<br />
&nbsp;<wbr>&nbsp;<wbr>about one, several or all hosts. It shows all services, hostgroups,<br />
&nbsp;<wbr>&nbsp;<wbr>contacts and other information about that host. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-d does not work on clusters&nbsp;<wbr>(such defined in main.mk)&nbsp;<wbr>but only on<br />
&nbsp;<wbr>&nbsp;<wbr>real hosts. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;check-discovery make check_mk behave as monitoring plugins that<br />
&nbsp;<wbr>&nbsp;<wbr>checks if an inventory would find new or vanished services for the host.<br />
&nbsp;<wbr>&nbsp;<wbr>If configured to do so, this will queue those hosts for automatic<br />
&nbsp;<wbr>&nbsp;<wbr>discover-marked-hosts </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;discover-marked-hosts run actual service discovery on all hosts that<br />
&nbsp;<wbr>&nbsp;<wbr>are known to have new/vanished services due to an earlier run of<br />
&nbsp;<wbr>&nbsp;<wbr>check-discovery. The results of this discovery may be activated<br />
&nbsp;<wbr>&nbsp;<wbr>automatically if that was discovered. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;list-hosts called without argument lists all hosts. You may<br />
&nbsp;<wbr>&nbsp;<wbr>specify one or more host groups to restrict the output to hosts<br />
&nbsp;<wbr>&nbsp;<wbr>that are in at least one of those groups. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;list-tag prints all hosts that have all of the specified tags<br />
&nbsp;<wbr>&nbsp;<wbr>at once. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-M, &#8211;man shows documentation about a check type. If<br />
&nbsp;<wbr>&nbsp;<wbr>/usr/bin/less is available it is used as pager. Exit by pressing<br />
&nbsp;<wbr>&nbsp;<wbr>Q. Use -M without an argument to show a list of all manual pages. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;backup saves all configuration and runtime data to a gzip<br />
&nbsp;<wbr>&nbsp;<wbr>compressed tar file. &#8211;restore&nbsp;<wbr>*erases*&nbsp;<wbr>the current configuration<br />
&nbsp;<wbr>&nbsp;<wbr>and data and replaces it with that from the backup file. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;flush deletes all runtime data belonging to a host. This includes<br />
&nbsp;<wbr>&nbsp;<wbr>the inventorized checks, the state of performance counters,<br />
&nbsp;<wbr>&nbsp;<wbr>cached agent output, and logfiles. Precompiled host checks<br />
&nbsp;<wbr>&nbsp;<wbr>are not deleted. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-P, &#8211;package brings you into packager mode. Packages are<br />
&nbsp;<wbr>&nbsp;<wbr>used to ship inofficial extensions of Check_MK. Call without<br />
&nbsp;<wbr>&nbsp;<wbr>arguments for a help on packaging. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;localize brings you into localization mode. You can create<br />
&nbsp;<wbr>&nbsp;<wbr>and/or improve the localization of Check_MKs Multisite.&nbsp;<wbr>&nbsp;<wbr>Call without<br />
&nbsp;<wbr>&nbsp;<wbr>arguments for a help on localization. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;donate is for those who decided to help the Check_MK project<br />
&nbsp;<wbr>&nbsp;<wbr>by donating live host data. It tars the cached agent data of<br />
&nbsp;<wbr>&nbsp;<wbr>those host which are configured in main.mk:donation_hosts and sends<br />
&nbsp;<wbr>&nbsp;<wbr>them via email to donatehosts [at] mathias-kettner.de. The host data<br />
&nbsp;<wbr>&nbsp;<wbr>is then publicly available for others and can be used for setting<br />
&nbsp;<wbr>&nbsp;<wbr>up demo sites, implementing checks and so on.<br />
&nbsp;<wbr>&nbsp;<wbr>Do this only with test data from test hosts &#8211; not with productive<br />
&nbsp;<wbr>&nbsp;<wbr>data!&nbsp;<wbr>By donating real-live host data you help others trying out<br />
&nbsp;<wbr>&nbsp;<wbr>Check_MK and developing checks by donating hosts. This is completely<br />
&nbsp;<wbr>&nbsp;<wbr>voluntary and turned off by default. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;snmpwalk does a complete snmpwalk for the specified hosts both<br />
&nbsp;<wbr>&nbsp;<wbr>on the standard MIB and the enterprises MIB and stores the<br />
&nbsp;<wbr>&nbsp;<wbr>result in the directory&nbsp;<wbr>%s. Use the option &#8211;oid one or several<br />
&nbsp;<wbr>&nbsp;<wbr>times in order to specify alternative OIDs to walk. You need to<br />
&nbsp;<wbr>&nbsp;<wbr>specify numeric OIDs. If you want to keep the two standard OIDS<br />
&nbsp;<wbr>&nbsp;<wbr>.1.3.6.1.2.1&nbsp;<wbr>&nbsp;<wbr>and .1.3.6.1.4.1 then use &#8211;extraoid for just adding<br />
&nbsp;<wbr>&nbsp;<wbr>additional OIDs to walk. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;snmptranslate does not contact the host again, but reuses the hosts<br />
&nbsp;<wbr>&nbsp;<wbr>walk from the directory&nbsp;<wbr>%s.%s </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;scan-parents uses traceroute in order to automatically detect<br />
&nbsp;<wbr>&nbsp;<wbr>hosts&#8217;s parents. It creates the file conf.d/parents.mk which<br />
&nbsp;<wbr>&nbsp;<wbr>defines gateway hosts and parent declarations. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-A, &#8211;bake-agents creates RPM/DEB/MSI packages with host-specific<br />
&nbsp;<wbr>&nbsp;<wbr>monitoring agents. If you add the option -f, &#8211;force then all<br />
&nbsp;<wbr>&nbsp;<wbr>agents are renewed, even if an uptodate version for a configuration<br />
&nbsp;<wbr>&nbsp;<wbr>already exists. Note: baking agents is only contained in the<br />
&nbsp;<wbr>&nbsp;<wbr>subscription version of Check_MK. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;show-snmp-stats analyzes and shows a summary of the Inline SNMP<br />
&nbsp;<wbr>&nbsp;<wbr>statistics which might have been recorded on your system before.<br />
&nbsp;<wbr>&nbsp;<wbr>Note: This is only contained in the subscription version of Check_MK. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;convert-rrds converts the internal structure of existing RRDs<br />
&nbsp;<wbr>&nbsp;<wbr>to the new structure as configured via the rulesets cmc_host_rrd_config<br />
&nbsp;<wbr>&nbsp;<wbr>and cmc_service_rrd_config. If you do not specify hosts, then all<br />
&nbsp;<wbr>&nbsp;<wbr>RRDs will be converted. Conversion just takes place if the configuration<br />
&nbsp;<wbr>&nbsp;<wbr>of the RRDs has changed. The option &#8211;split will activate conversion<br />
&nbsp;<wbr>&nbsp;<wbr>from exising RRDs in PNP storage type SINGLE to MULTIPLE. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-i, &#8211;inventory does a HW/SW-Inventory for all, one or several<br />
&nbsp;<wbr>&nbsp;<wbr>hosts. If you add the option -f, &#8211;force then persisted sections<br />
&nbsp;<wbr>&nbsp;<wbr>will be used even if they are outdated. </p>
<h2>Index</h2>
