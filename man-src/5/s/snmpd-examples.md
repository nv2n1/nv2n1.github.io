---
title: "snmpd-examples(5)"
name: "snmpd-examples"
section: "5"
letter: "s"
url: "/docs/linux/man/5-snmpd-examples/"
description: "snmpd.examples – example configuration for the Net-SNMP agent"
---

<p>snmpd.examples &#8211; example configuration for the Net-SNMP agent</p>
<h2>Description</h2>
<p>The <i><a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5)</i> man page defines the syntax and behaviour of the various configuration directives that can be used to control the operation of the Net-SNMP agent, and the management information it provides. </p>
<p> This companion man page illustrates these directives, showing some practical examples of how they might be used.</p>
<h2>Agent Behaviour</h2>
<h3>Listening addresses</h3>
<p>The default agent behaviour (listing on the standard SNMP UDP port on all interfaces) is equivalent to the directive:</p>
<dl>
<dd>agentaddress udp:161</dl>
<p> or simply</p>
<dl>
<dd>agentaddress 161</dl>
<p> The agent can be configured to <i>only</i> accept requests sent to the local loopback interface (again listening on the SNMP UDP port), using:</p>
<dl>
<dd>agentaddress localhost:161 <i># (udp implicit)</i></dl>
<p> or</p>
<dl>
<dd>agentaddress 127.0.0.1 <i># (udp and standard port implicit)</i></dl>
<p> It can be configured to accept both UDP and TCP requests (over both IPv4 and IPv6), using:</p>
<dl>
<dd>agentaddress udp:161,tcp:161,udp6:161,tcp6:161</dl>
<p> Other combinations are also valid.</p>
<h3>Run-time privileges</h3>
<p>The agent can be configured to relinquish any privileged access once it has opened the initial listening ports. Given a suitable &quot;snmp&quot; group (defined in <i>/etc/group</i>), this could be done using the directives:</p>
<dl>
<dd>
<pre>agentuser nobody
agentgroup snmp</pre>
</dl>
<p> A similar effect could be achieved using numeric UID and/or GID values:</p>
<dl>
<dd>
<pre>agentuser #10
agentgroup #10</pre>
</dl>
<h3>SNMPv3 Configuration</h3>
<p>Rather than being generated pseudo-randomly, the engine ID for the agent could be calculated based on the MAC address of the second network interface (<i>eth1</i>), using the directives:</p>
<dl>
<dd>engineIDType 3 engineIDNic eth1</dl>
<p> or it could be calculated from the (first) IP address, using:</p>
<dl>
<dd>engineIDType 1</dl>
<p> or it could be specified explicitly, using:</p>
<dl>
<dd>engineID &quot;XXX &#8211; WHAT FORMAT&quot;</dl>
<h2>Access Control</h2>
<h3>SNMPv3 Users</h3>
<p>The following directives will create three users, all using exactly the same authentication and encryption settings:</p>
<dl>
<dd>
<pre>createUser me MD5 &quot;single pass phrase&quot;
createUser myself MD5 &quot;single pass phrase&quot; DES
createUser andI MD5 &quot;single pass phrase&quot; DES &quot;single pass phrase&quot;</pre>
</dl>
<p> Note that this defines three <i>distinct</i> users, who could be granted different levels of access. Changing the passphrase for any one of these would not affect the other two. </p>
<p> Separate pass phrases can be specified for authentication and encryption:</p>
<dl>
<dd>createUser onering SHA &quot;to rule them all&quot; AES &quot;to bind them&quot;</dl>
<p> Remember that these <i>createUser</i> directives should be defined in the /var/lib/snmp/snmpd.conf file, rather than the usual location.</p>
<h3>Traditional Access Control</h3>
<p>The SNMPv3 users defined above can be granted access to the full MIB tree using the directives:</p>
<dl>
<dd>
<pre>rouser me
rwuser onering</pre>
</dl>
<p> Or selective access to individual subtrees using:</p>
<dl>
<dd>
<pre>rouser myself .1.3.6.1.2
rwuser andI system</pre>
</dl>
<p> Note that a combination repeating the same user, such as:</p>
<dl>
<dd>
<pre>rouser onering
rwuser onering</pre>
</dl>
<p> should <code>not</code> be used. This would configure the user <i>onering</i> with read-only access (and ignore the <i>rwuser</i> entry altogether). The same holds for the community-based directives. </p>
<p> The directives:</p>
<dl>
<dd>
<pre>rocommunity public
rwcommunity private</pre>
</dl>
<p> would define the commonly-expected read and write community strings for SNMPv1 and SNMPv2c requests. This behaviour is <code>not</code> configured by default, and would need to be set up explicitly.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>It would also be a very good idea to change <i>private</i> to something a little less predictable!</dl>
</dl>
<p> A slightly less vulnerable configuration might restrict what information could be retrieved:</p>
<dl>
<dd>rocommunity public default system</dl>
<p> or the management systems that settings could be manipulated from:</p>
<dl>
<dd>rwcommunity private 10.10.10.0/24</dl>
<p> or a combination of the two.</p>
<h3>VACM Configuration</h3>
<p>This last pair of settings are equivalent to the full VACM definitions:</p>
<dl>
<dd>
<pre><i># sec.name source community</i>
com2sec public default public
com2sec mynet 10.10.10.0/24 private
com2sec6 mynet fec0::/64 private
<i># sec.model sec.name</i>
group worldGroup v1 public
group worldGroup v2c public
group myGroup v1 mynet
group myGroup v2c mynet
<i># incl/excl subtree [mask]</i>
view all included .1
view sysView included system
<i># context model level prefix read write notify (unused)</i>
access worldGroup &quot;&quot; any noauth exact system none none
access myGroup &quot;&quot; any noauth exact all all none</pre>
</dl>
<p> There are several points to note in this example: </p>
<p> The <i>group</i> directives must be repeated for both SNMPv1 and SNMPv2c requests. </p>
<p> The <i>com2sec</i> security name is distinct from the community string that is mapped to it. They can be the same (&quot;public&quot;) or different (&quot;mynet&quot;/&quot;private&quot;) &#8211; but what appears in the <i>group</i> directive is the security name, regardless of the original community string. </p>
<p> Both of the <i>view</i> directives are defining simple OID subtrees, so neither of these require an explicit mask. The same holds for the &quot;combined subtree2 view defined below. In fact, a mask field is only needed when defining row slices across a table (or similar views), and can almost always be omitted. </p>
<p> In general, it is advisible not to mix traditional and VACM-based access configuration settings, as these can sometimes interfere with each other in unexpected ways. Choose a particular style of access configuration, and stick to it.</p>
<h3>Typed-View Configuration</h3>
<p>A similar configuration could also be configured as follows:</p>
<dl>
<dd>
<pre>view sys2View included system
view sys2View included .1.3.6.1.2.1.25.1
authcommunity read public default -v sys2View
authcommunity read,write private 10.10.10.0/8</pre>
</dl>
<p> This mechanism allows multi-subtree (or other non-simple) views to be used with the one-line <i>rocommunity</i> style of configuration. </p>
<p> It would also support configuring &quot;write-only&quot; access, should this be required.</p>
<h2>System Information</h2>
<h3>System Group</h3>
<p>The full contents of the &#8216;system&#8217; group (with the exception of sysUpTime) can be explicitly configured using:</p>
<dl>
<dd>
<pre><i># Override 'uname -a' and hardcoded system OID - inherently read-only values</i>
sysDescr Universal Turing Machine mk I
sysObjectID .1.3.6.1.4.1.8072.3.2.1066
<i># Override default values from 'configure' - makes these objects read-only</i>
sysContact Alan.Turing [at] pre-cs.man.ac.uk
sysName tortoise.turing.com
sysLocation An idea in the mind of AT
<i># Standard end-host behaviour</i>
sysServices 72</pre>
</dl>
<h3>Host Resources Group</h3>
<p>The list of devices probed for potential inclusion in the hrDiskStorageTable (and hrDeviceTable) can be amended using any of the following directives:</p>
<dl>
<dd>ignoredisk /dev/rdsk/c0t2d0</dl>
<p> which prevents the device <i>/dev/rdsk/c0t2d0</i> from being scanned,</p>
<dl>
<dd>
<pre>ignoredisk /dev/rdsk/c0t[!6]d0
ignoredisk /dev/rdsk/c0t[0-57-9a-f]d0</pre>
</dl>
<p> either of which prevents all devices <i>/dev/rdsk/c0t</i>X<i>d0</i> (except &#8230;/<i>c0t6d0</i>) from being scanned,</p>
<dl>
<dd>ignoredisk /dev/rdsk/c1*</dl>
<p> which prevents all devices whose device names start with <i>/dev/rdsk/c1</i> from being scanned, or</p>
<dl>
<dd>ignoredisk /dev/rdsk/c?t0d0</dl>
<p> which prevents all devices <i>/dev/rdsk/c</i>X<i>t0d0</i> (where &#8216;X&#8217; is any single character) from being scanned.</p>
<h3>Process Monitoring</h3>
<p>The list of services running on a system can be monitored (and provision made for correcting any problems), using:</p>
<dl>
<dd>
<pre><i># At least one web server process must be running at all times</i>
proc httpd
procfix httpd /etc/rc.d/init.d/httpd restart
<i># There should never be more than 10 mail processes running
# (more implies a probable mail storm, so shut down the mail system)</i>
proc sendmail 10
procfix sendmail /etc/rc.d/init.d/sendmail stop
<i># There should be a single network management agent running
# (&quot;There can be only one&quot;)</i>
proc snmpd 1 1</pre>
</dl>
<p> Also see the &quot;DisMan Event MIB&quot; section later on.</p>
<h3>Disk Usage Monitoring</h3>
<p>The state of disk storage can be monitored using:</p>
<dl>
<dd>
<pre>includeAllDisks 10%
disk /var 20%
disk /usr 3%
<i># Keep 100 MB free for crash dumps</i>
disk /mnt/crash 100000</pre>
</dl>
<h3>System Load Monitoring</h3>
<p>A simple check for an overloaded system might be:</p>
<dl>
<dd>load 10</dl>
<p> A more refined check (to allow brief periods of heavy use, but recognise sustained medium-heavy load) might be:</p>
<dl>
<dd>load 30 10 5</dl>
<h3>Log File Monitoring</h3>
<p><i>TODO</i></p>
<dl>
<dd>file FILE [MAXSIZE]</dl>
<dl>
<dd>logmatch NAME PATH CYCLETIME REGEX</dl>
<h2>Active Monitoring</h2>
<h3>Notification Handling</h3>
<p>Configuring the agent to report invalid access attempts might be done by:</p>
<dl>
<dd>
<pre>authtrapenable 1
trapcommunity public
trap2sink localhost</pre>
</dl>
<p> Alternatively, the second and third directives could be combined (and an acknowledgement requested) using:</p>
<dl>
<dd>informsink localhost public</dl>
<p> A configuration with repeated sink destinations, such as:</p>
<dl>
<dd>
<pre>trapsink localhost
trap2sink localhost
informsink localhost</pre>
</dl>
<p> should <code>NOT</code> be used, as this will cause multiple copies of each trap to be sent to the same trap receiver. </p>
<p> <i>TODO &#8211; discuss SNMPv3 traps</i></p>
<dl>
<dd>trapsess <i>snmpv3 options</i> localhost:162</dl>
<p> <i>TODO &#8211; mention trapd access configuration</i></p>
<h3>DisMan Event MIB</h3>
<p>The simplest configuration for active self-monitoring of the agent, by the agent, for the agent, is probably:</p>
<dl>
<dd>
<pre><i># Set up the credentials to retrieve monitored values</i>
createUser _internal MD5 &quot;the first sign of madness&quot;
iquerySecName _internal
rouser _internal
<i># Active the standard monitoring entries</i>
defaultMonitors yes
linkUpDownNotifications yes
<i># If there's a problem, then tell someone!</i>
trap2sink localhost</pre>
</dl>
<p> The first block sets up a suitable user for retrieving the information to by monitored, while the following pair of directives activates various built-in monitoring entries. </p>
<p> Note that the DisMan directives are not themselves sufficient to actively report problems &#8211; there also needs to be a suitable destination configured to actually send the resulting notifications to. </p>
<p> A more detailed monitor example is given by:</p>
<dl>
<dd>monitor -u me -o hrSWRunName &quot;high process memory&quot; hrSWRunPerfMem &gt; 10000</dl>
<p> This defines an explicit boolean monitor entry, looking for any process using more than 10MB of active memory. Such processes will be reported using the (standard) DisMan trap mteTriggerFired, but adding an extra (wildcarded) varbind hrSWRunName. </p>
<p> This entry also specifies an explicit user (<i>me</i>, as defined earlier) for retrieving the monitored values, and building the trap. </p>
<p> Objects that could potentially fluctuate around the specified level are better monitored using a threshold monitor entry:</p>
<dl>
<dd>monitor -D -r 10 &quot;network traffic&quot; ifInOctets 1000000 5000000</dl>
<p> This will send a mteTriggerRising trap whenever the incoming traffic rises above (roughly) 500 kB/s on any network interface, and a corresponding mteTriggerFalling trap when it falls below 100 kB/s again. </p>
<p> Note that this monitors the deltas between successive samples (<i>-D</i>) rather than the actual sample values themselves. The same effect could be obtained using:</p>
<dl>
<dd>monitor -r 10 &quot;network traffic&quot; ifInOctets &#8211; &#8211; 1000000 5000000</dl>
<p> The <i>linkUpDownNotifications</i> directive above is broadly equivalent to:</p>
<dl>
<dd>
<pre>notificationEvent linkUpTrap linkUp ifIndex ifAdminStatus ifOperStatus
notificationEvent linkDownTrap linkDown ifIndex ifAdminStatus ifOperStatus
monitor -r 60 -e linkUpTrap &quot;Generate linkUp&quot; ifOperStatus != 2
monitor -r 60 -e linkDownTrap &quot;Generate linkDown&quot; ifOperStatus == 2</pre>
</dl>
<p> This defines the traps to be sent (using <i>notificationEvent</i>), and explicitly references the relevant notification in the corresponding monitor entry (rather than using the default DisMan traps). </p>
<p> The <i>defaultMonitors</i> directive above is equivalent to a series of (boolean) monitor entries:</p>
<dl>
<dd>
<pre>monitor -o prNames -o prErrMessage &quot;procTable&quot; prErrorFlag != 0
monitor -o memErrorName -o memSwapErrorMsg &quot;memory&quot; memSwapError != 0
monitor -o extNames -o extOutput &quot;extTable&quot; extResult != 0
monitor -o dskPath -o dskErrorMsg &quot;dskTable&quot; dskErrorFlag != 0
monitor -o laNames -o laErrMessage &quot;laTable&quot; laErrorFlag != 0
monitor -o fileName -o fileErrorMsg &quot;fileTable&quot; fileErrorFlag != 0</pre>
</dl>
<p> and will send a trap whenever any of these entries indicate a problem. </p>
<p> An alternative approach would be to automatically invoke the corresponding &quot;fix&quot; action:</p>
<dl>
<dd>
<pre>setEvent prFixIt prErrFix = 1
monitor -e prFixIt &quot;procTable&quot; prErrorFlag != 0</pre>
</dl>
<p> (and similarly for any of the other <i>defaultMonitor</i> entries).</p>
<h3>DisMan Schedule MIB</h3>
<p>The agent could be configured to reload its configuration once an hour, using:</p>
<dl>
<dd>repeat 3600 versionUpdateConfig.0 = 1</dl>
<p> Alternatively this could be configured to be run at specific times of day (perhaps following rotation of the logs):</p>
<dl>
<dd>cron 10 0 * * * versionUpdateConfig.0 = 1</dl>
<p> The one-shot style of scheduling is rather less common, but the secret SNMP virus could be activated on the next occurance of Friday 13th using:</p>
<dl>
<dd>at 13 13 13 * 5 snmpVirus.0 = 1</dl>
<h2>Extending Agent Functionality</h2>
<h3>Arbitrary Extension Commands</h3>
<p><i>Old Style</i></p>
<dl>
<dd>
<pre>exec [MIBOID] NAME PROG ARGS&quot;
sh [MIBOID] NAME PROG ARGS&quot;
execfix NAME PROG ARGS&quot;</pre>
</dl>
<p> <i>New Style</i></p>
<dl>
<dd>
<pre>extend [MIBOID] NAME PROG ARGS&quot;
extendfix [MIBOID] NAME PROG ARGS&quot;</pre>
</dl>
<h3>MIB-Specific Extension Commands</h3>
<p><i>One-Shot</i></p>
<dl>
<dd>&quot;pass [-p priority] MIBOID PROG&quot;</dl>
<dl>
<dd><i>Persistent</i></p>
<dl>
<dd>&quot;pass_persist [-p priority] MIBOID PROG&quot;</dl>
</dl>
<h3>Embedded Perl Support</h3>
<p>If embedded perl support is enabled in the agent, the default initialisation is equivalent to the directives:</p>
<dl>
<dd>
<pre>disablePerl false
perlInitFile /usr/share/snmp/snmp_perl.pl</pre>
</dl>
<p> The main mechanism for defining embedded perl scripts is the <i>perl</i> directive. A very simple (if somewhat pointless) MIB handler could be registered using:</p>
<dl>
<dd>
<pre>perl use Data::Dumper;
perl sub myroutine { print &quot;got called: &quot;,Dumper(@_),&quot;
&quot;; }
perl $agent-&gt;register('mylink', '.1.3.6.1.8765', \&amp;myroutine);</pre>
</dl>
<p> This relies on the <i>$agent</i> object, defined in the example snmp_perl.pl file. </p>
<p> A more realistic MIB handler might be:</p>
<dl>
<dd>
<pre><i>XXX - WHAT ???</i></pre>
</dl>
<p> Alternatively, this code could be stored in an external file, and loaded using:</p>
<dl>
<dd>perl &#8216;do /usr/share/snmp/perl_example.pl&#8217;;</dl>
<h3>Dynamically Loadable Modules</h3>
<p><i>TODO</i></p>
<dl>
<dd>dlmod NAME PATH&quot;</dl>
<h3>Proxy Support</h3>
<p>A configuration for acting as a simple proxy for two other SNMP agents (running on remote systems) might be:</p>
<dl>
<dd>
<pre>com2sec -Cn rem1context rem1user default remotehost1
com2sec -Cn rem2context rem2user default remotehost2
proxy -Cn rem1context -v 1 -c public remotehost1 .1.3
proxy -Cn rem2context -v 1 -c public remotehost2 .1.3</pre>
</dl>
<p> (plus suitable access control entries). </p>
<p> The same <i>proxy</i> directives would also work with (incoming) SNMPv3 requests, which can specify a context directly. It would probably be more sensible to use contexts of <i>remotehost1</i> and <i>remotehost2</i> &#8211; the names above were chosen to indicate how these directives work together. </p>
<p> Note that the administrative settings for the proxied request are specified explicitly, and are independent of the settings from the incoming request. </p>
<p> An alternative use for the <i>proxy</i> directive is to pass part of the OID tree to another agent (either on a remote host or listening on a different port on the same system), while handling the rest internally:</p>
<dl>
<dd>proxy -v 1 -c public localhost:6161 .1.3.6.1.4.1.99</dl>
<p> This mechanism can be used to link together two separate SNMP agents. </p>
<p> A less usual approach is to map one subtree into a different area of the overall MIB tree (either locally or on a remote system):</p>
<dl>
<dd>
<pre><i># uses SNMPv3 to access the MIB tree .1.3.6.1.2.1.1 on 'remotehost'
# and maps this to the local tree .1.3.6.1.3.10</i>
proxy -v 3 -l noAuthNoPriv -u user remotehost .1.3.6.1.3.10 .1.3.6.1.2.1.1</pre>
</dl>
<h3>SMUX Sub-Agents</h3>
<dl>
<dd>
<pre>smuxsocket 127.0.0.1
smuxpeer .1.3.6.1.2.1.14 ospf_pass</pre>
</dl>
<h3>AgentX Sub-Agents</h3>
<p>The Net-SNMP agent could be configured to operate as an AgentX master agent (listening on a non-standard named socket, and running using the access privileges defined earlier), using:</p>
<dl>
<dd>
<pre>master agentx
agentXSocket /tmp/agentx/master
agentXPerms 0660 0550 nobody snmp</pre>
</dl>
<p> A sub-agent wishing to connect to this master agent would need the same <i>agentXSocket</i> directive, or the equivalent code:</p>
<dl>
<dd>
<pre>netsnmp_ds_set_string(NETSNMP_DS_APPLICATION_ID, NETSNMP_DS_AGENT_X_SOCKET, 
 &quot;/tmp/agentx/master&quot;);</pre>
</dl>
<p> A loopback networked AgentX configuration could be set up using:</p>
<dl>
<dd>
<pre>agentXSocket tcp:localhost:705
agentXTimeout 5
agentXRetries 2</pre>
</dl>
<p> on the master side, and:</p>
<dl>
<dd>
<pre>agentXSocket tcp:localhost:705
agentXTimeout 10
agentXRetries 1
agentXPingInterval 600</pre>
</dl>
<p> on the client. </p>
<p> Note that the timeout and retry settings can be asymmetric for the two directions, and the sub-agent can poll the master agent at regular intervals (600s = every 10 minutes), to ensure the connection is still working.</p>
<h2>Other Configuration</h2>
<dl>
<dd>override sysDescr.0 octet_str &quot;my own sysDescr&quot;</dl>
<dl>
<dd>injectHandler stash_cache NAME table_iterator</dl>
<h2>Files</h2>
<p>/etc/snmp/snmpd.conf</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-snmpconf/">snmpconf</a>(1), <a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5), <a href="/docs/linux/man/5-snmp-conf/">snmp.conf</a>(5), <a href="/docs/linux/man/5-snmp_config/">snmp_config</a>(5), <a href="/docs/linux/man/8-snmpd/">snmpd</a>(8), EXAMPLE.conf, <a href="/docs/linux/man/3-netsnmp_config_api/">netsnmp_config_api</a>(3). </p>
