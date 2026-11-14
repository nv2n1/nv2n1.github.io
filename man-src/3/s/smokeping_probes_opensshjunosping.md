---
title: "smokeping_probes_opensshjunosping(3)"
name: "smokeping_probes_opensshjunosping"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_opensshjunosping/"
---

Smokeping::probes::OpenSSHJunOSPing - Juniper SSH JunOS Probe for SmokePing 

<h2>Synopsis</h2><pre> *** Probes ***
 +OpenSSHJunOSPing
 forks = 5
 offset = 50%
 packetsize = 100
 step = 300
 timeout = 15
 # The following variables can be overridden in each target section
 junospass = password # mandatory
 junosuser = user # mandatory
 pings = 5
 psource = 192.168.2.129
 source = 192.168.2.1 # mandatory
 # [...]
 *** Targets ***
 probe = OpenSSHJunOSPing # if this should be the default probe
 # [...]
 + mytarget
 # probe = OpenSSHJunOSPing # if the default probe is something else
 host = my.host
 junospass = password # mandatory
 junosuser = user # mandatory
 pings = 5
 psource = 192.168.2.129
 source = 192.168.2.1 # mandatory</pre><h2>Description</h2>Connect to Juniper JunOS via OpenSSH to run ping commands. This probe uses the ``extended ping'' of the Juniper JunOS. You have the option to specify which interface the ping is sourced from as well.
<h2>Variables</h2>Supported probe-specific variables:
<dl COMPACT><dt>forks
<dd>Run this many concurrent processes at maximum 

 Example value: 5 

 Default value: 5
<dt>offset
<dd>If you run many probes concurrently you may want to prevent them from hitting your network all at the same time. Using the probe-specific offset parameter you can change the point in time when each probe will be run. Offset is specified in % of total interval, or alternatively as 'random', and the offset from the 'General' section is used if nothing is specified here. Note that this does <font SIZE="-1">NOT</font> influence the rrds itself, it is just a matter of when data acqusition is initiated. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 

 Example value: 50%
<dt>packetsize
<dd>The (optional) packetsize option lets you configure the packetsize for the pings sent. 

 Default value: 100
<dt>step
<dd>Duration of the base interval that this probe should use, if different from the one specified in the 'Database' section. Note that the step in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change the step parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 

 Example value: 300
<dt>timeout
<dd>How long a single 'ping' takes at maximum 

 Example value: 15 

 Default value: 5</dl>
 

 Supported target-specific variables:
<dl COMPACT><dt>junospass
<dd>The junospass option allows you to specify the password for the username specified with the option junosuser. 

 Example value: password 

 This setting is mandatory.
<dt>junosuser
<dd>The junosuser option allows you to specify a username that has ping capability on the JunOS Device. 

 Example value: user 

 This setting is mandatory.
<dt>pings
<dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. 

 Example value: 5
<dt>psource
<dd>The (optional) psource option specifies an alternate <font SIZE="-1">IP</font> address or Interface from which you wish to source your pings from. Routers can have many many <font SIZE="-1">IP</font> addresses, and interfaces. When you ping from a router you have the ability to choose which interface and/or which <font SIZE="-1">IP</font> address the ping is sourced from. Specifying an IP/interface does not necessarily specify the interface from which the ping will leave, but will specify which address the packet(s) appear to come from. If this option is left out the JunOS Device will source the packet automatically based on routing and/or metrics. If this doesn't make sense to you then just leave it out. 

 Example value: 192.168.2.129
<dt>source
<dd>The source option specifies the JunOS device that is going to run the ping commands. This address will be used for the ssh connection. 

 Example value: 192.168.2.1 

 This setting is mandatory.</dl><h2>Authors</h2>Tobias Oetiker lttobi [at] oetiker.chgt 

 based on Smokeping::probes::TelnetJunOSPing by S H A N ltshanali [at] yahoo.comgt.
<h2>Notes</h2><h3>JunOS configuration</h3>The JunOS device should have a username/password configured, as well as the ability to connect to the <font SIZE="-1">VTY</font>(s). 

 Make sure to connect to the remote host once from the commmand line as the user who is running smokeping. On the first connect ssh will ask to add the new host to its known_hosts file. This will not happen automatically so the script will fail to login until the ssh key of your juniper box is in the known_hosts file. 

 Some JunOS devices have a maximum of 5 VTYs available, so be careful not to hit a limit with the 'forks' variable.
<h3>Requirements</h3>This module requires the Net::OpenSSH and IO::Pty.
