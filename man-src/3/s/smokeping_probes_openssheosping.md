---
title: "smokeping_probes_openssheosping(3)"
name: "smokeping_probes_openssheosping"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_openssheosping/"
---

Smokeping::probes::OpenSSHEOSPing - Arista EOS SSH Probe for SmokePing 

<h2>Synopsis</h2><pre> *** Probes ***
 +OpenSSHEOSPing
 forks = 5
 offset = 50%
 packetsize = 100
 step = 300
 timeout = 15
 # The following variables can be overridden in each target section
 eospass = password # mandatory
 eosuser = user # mandatory
 pings = 5
 psource = 192.168.2.129
 source = 192.168.2.1 # mandatory
 unpriv = 1
 # [...]
 *** Targets ***
 probe = OpenSSHEOSPing # if this should be the default probe
 # [...]
 + mytarget
 # probe = OpenSSHEOSPing # if the default probe is something else
 host = my.host
 eospass = password # mandatory
 eosuser = user # mandatory
 pings = 5
 psource = 192.168.2.129
 source = 192.168.2.1 # mandatory
 unpriv = 1</pre><h2>Description</h2>Connect to Arista EOS via OpenSSH to run ping commands. This probe uses the ``ping'' cli of the Arista EOS.  You have the option to specify which interface the ping is sourced from as well.
<h2>Variables</h2>Supported probe-specific variables:
<dl COMPACT><dt>forks
</dt><dd>Run this many concurrent processes at maximum 
 Example value: 5 
 Default value: 5
</dd><dt>offset
</dt><dd>If you run many probes concurrently you may want to prevent them from hitting your network all at the same time. Using the probe-specific offset parameter you can change the point in time when each probe will be run. Offset is specified in % of total interval, or alternatively as 'random', and the offset from the 'General' section is used if nothing is specified here. Note that this does NOT influence the rrds itself, it is just a matter of when data acqusition is initiated. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 
 Example value: 50%
</dd><dt>packetsize
</dt><dd>The (optional) packetsize option lets you configure the packetsize for the pings sent. 
 Default value: 100
</dd><dt>step
</dt><dd>Duration of the base interval that this probe should use, if different from the one specified in the 'Database' section. Note that the step in the RRD files is fixed when they are originally generated, and if you change the step parameter afterwards, you'll have to delete the old RRD files or somehow convert them. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 
 Example value: 300
</dd><dt>timeout
</dt><dd>How long a single 'ping' takes at maximum 
 Example value: 15 
 Default value: 5</dd></dl>
 

 Supported target-specific variables:
<dl COMPACT><dt>eospass
</dt><dd>The eospass option allows you to specify the password for the username specified with the option eosuser. 
 Example value: password 
 This setting is mandatory.
</dd><dt>eosuser
</dt><dd>The eosuser option allows you to specify a username that has ping capability on the EOS Device. 
 Example value: user 
 This setting is mandatory.
</dd><dt>pings
</dt><dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the RRD files is fixed when they are originally generated, and if you change this parameter afterwards, you'll have to delete the old RRD files or somehow convert them. 
 Example value: 5
</dd><dt>psource
</dt><dd>The (optional) psource option specifies an alternate IP address or Interface from which you wish to source your pings from. Routers can have many many IP addresses, and interfaces. When you ping from a router you have the ability to choose which interface and/or which IP address the ping is sourced from. Specifying an IP/interface does not necessarily specify the interface from which the ping will leave, but will specify which address the packet(s) appear to come from. If this option is left out the EOS Device will source the packet automatically based on routing and/or metrics. If this doesn't make sense to you then just leave it out. 
 Example value: 192.168.2.129
</dd><dt>source
</dt><dd>The source option specifies the EOS device that is going to run the ping commands. This address will be used for the ssh connection. 
 Example value: 192.168.2.1 
 This setting is mandatory.
</dd><dt>unpriv
</dt><dd>If the account is unprivileged, specify the 'unpriv' option. You must also configure ``pings = 5'', since that is the only value supported, and values specified for packetsize or psource are ignored. 
 Example value: 1</dd></dl><h2>Authors</h2>Bill Fenner &lt;fenner [at] aristanetworks.com&gt; 

 based on Smokeping::Probes::OpenSSHJunOSPing by Tobias Oetiker &lt;tobi [at] oetiker.ch&gt;, which itself is based on Smokeping::probes::TelnetJunOSPing by S H A N &lt;shanali [at] yahoo.com&gt;.
<h2>Notes</h2><h3>EOS configuration</h3>The EOS device should have a username/password configured, and the ssh server must not be disabled. 

 Make sure to connect to the remote host once from the commmand line as the user who is running smokeping. On the first connect ssh will ask to add the new host to its known_hosts file. This will not happen automatically so the script will fail to login until the ssh key of your EOS box is in the known_hosts file.
<h3>Requirements</h3>This module requires the Net::OpenSSH and IO::Pty perl modules.
