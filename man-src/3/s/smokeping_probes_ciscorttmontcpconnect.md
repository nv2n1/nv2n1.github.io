---
title: "smokeping_probes_ciscorttmontcpconnect(3)"
name: "smokeping_probes_ciscorttmontcpconnect"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_ciscorttmontcpconnect/"
---

Smokeping::probes::CiscoRTTMonTcpConnect - Probe for SmokePing 

<h2>Synopsis</h2><pre> *** Probes ***
 +CiscoRTTMonTcpConnect
 forks = 5
 offset = 50%
 step = 300
 timeout = 15
 # The following variables can be overridden in each target section
 ioshost = RTTcommunity [at] Myrouter.foobar.com.au # mandatory
 iosint = 10.33.22.11
 pings = 5
 port = 80
 timeout = 15
 tos = 160
 # [...]
 *** Targets ***
 probe = CiscoRTTMonTcpConnect # if this should be the default probe
 # [...]
 + mytarget
 # probe = CiscoRTTMonTcpConnect # if the default probe is something else
 host = my.host
 ioshost = RTTcommunity [at] Myrouter.foobar.com.au # mandatory
 iosint = 10.33.22.11
 pings = 5
 port = 80
 timeout = 15
 tos = 160</pre><h2>Description</h2>A probe for smokeping, which uses the ciscoRttMon MIB functionality (``Service Assurance Agent'', ``SAA'') of Cisco IOS to measure TCP connect times between a Cisco router and a TCP server. The measured value is the time is the time to establish a TCP session, i.e. the time between the initial ``SYN'' TCP packet of the router and the ``SYN ACK'' packet of the host. The router terminates the TCP session immediately after the reception of ``SYN ACK'' with a ``FIN'' packet.
<h2>Variables</h2>Supported probe-specific variables:
<dl COMPACT><dt>forks
</dt><dd>Run this many concurrent processes at maximum 
 Example value: 5 
 Default value: 5
</dd><dt>offset
</dt><dd>If you run many probes concurrently you may want to prevent them from hitting your network all at the same time. Using the probe-specific offset parameter you can change the point in time when each probe will be run. Offset is specified in % of total interval, or alternatively as 'random', and the offset from the 'General' section is used if nothing is specified here. Note that this does NOT influence the rrds itself, it is just a matter of when data acqusition is initiated. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 
 Example value: 50%
</dd><dt>step
</dt><dd>Duration of the base interval that this probe should use, if different from the one specified in the 'Database' section. Note that the step in the RRD files is fixed when they are originally generated, and if you change the step parameter afterwards, you'll have to delete the old RRD files or somehow convert them. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 
 Example value: 300
</dd><dt>timeout
</dt><dd>How long a single 'ping' takes at maximum 
 Example value: 15 
 Default value: 5</dd></dl>
 

 Supported target-specific variables:
<dl COMPACT><dt>ioshost
</dt><dd>The (mandatory) ioshost parameter specifies the Cisco router, which will establish the TCP connections as well as the SNMP community string on the router. 
 Example value: RTTcommunity [at] Myrouter.foobar.com.au 
 This setting is mandatory.
</dd><dt>iosint
</dt><dd>The (optional) iosint parameter is the source address for the TCP connections. This should be one of the active (!) IP addresses of the router to get results. IOS looks up the target host address in the forwarding table and then uses the interface(s) listed there to send the TCP packets. By default IOS uses the (primary) IP address on the sending interface as source address for a connection. 
 Example value: 10.33.22.11
</dd><dt>pings
</dt><dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the RRD files is fixed when they are originally generated, and if you change this parameter afterwards, you'll have to delete the old RRD files or somehow convert them. 
 Example value: 5
</dd><dt>port
</dt><dd>The (optional) port parameter lets you configure the destination TCP port on the host. The default is the http port 80. 
 Default value: 80
</dd><dt>timeout
</dt><dd>How long a single RTTMon TcpConnect 'ping' take at maximum plus 10 seconds to spare. Since we control our own timeout the only purpose of this is to not have us killed by the ping method from basefork. 
 Example value: 15 
 Default value: 15
</dd><dt>tos
</dt><dd>The (optional) tos parameter specifies the value of the ToS byte in the IP header of the packets from the router. Multiply DSCP values times 4 and Precedence values times 32 to calculate the ToS values to configure, e.g. ToS 160 corresponds to a DSCP value 40 and a Precedence value of 5. Please note that this will not influence the ToS value in the packets sent by the the host. 
 Example value: 160 
 Default value: 0</dd></dl><h2>Authors</h2>Joerg.Kummer at Roche.com
<h2>Notes</h2><h3>IOS VERSIONS</h3>This probe only works with Cisco IOS 12.0\fIs0(3)T or higher. It is recommended to test it on less critical routers first. 
<h3>INSTALLATION</h3>To install this probe copy ciscoRttMonMIB.pm to ($SMOKEPINGINSTALLDIR)/Smokeping/lib and CiscoRTTMonTcpConnect.pm to ($SMOKEPINGINSTALLDIR)/lib/Smokeping/probes. V0.97 or higher of Simon Leinen's SNMP_Session.pm is required. 

 The router(s) must be configured to allow read/write SNMP access. Sufficient is: 

 <pre> snmp-server community RTTCommunity RW</pre>If you want to be a bit more restrictive with SNMP write access to the router, then consider configuring something like this 

 <pre> access-list 2 permit 10.37.3.5
 snmp-server view RttMon ciscoRttMonMIB included
 snmp-server community RTTCommunity view RttMon RW 2</pre>The above configuration grants SNMP read-write only to 10.37.3.5 (the smokeping host) and only to the ciscoRttMon MIB tree. The probe does not need access to SNMP variables outside the RttMon tree.
<h2>Bugs</h2>The probe establishes unnecessary connections, i.e. more than configured in the ``pings'' variable, because the RTTMon MIB only allows to set a total time for all connections in one measurement run (one ``life''). Currently the probe sets the life duration to ``pings''*5+3 seconds (5 secs is the timeout value hardcoded into this probe).
<h2>See Also</h2>&lt;<a rel="nofollow" HREF="http://oss.oetiker.ch/smokeping/">http://oss.oetiker.ch/smokeping/</a>&gt; 

 &lt;<a rel="nofollow" HREF="http://www.switch.ch/misc/leinen/snmp/perl/">http://www.switch.ch/misc/leinen/snmp/perl/</a>&gt; 

 The best source for background info on SAA is Cisco's documentation on &lt;<a rel="nofollow" HREF="http://www.cisco.com">http://www.cisco.com</a>&gt; and the CISCO-RTTMON-MIB documentation, which is available at: &lt;<a HREF="ftp://ftp.cisco.com/pub/mibs/v2/CISCO-RTTMON-MIB.my">ftp://ftp.cisco.com/pub/mibs/v2/CISCO-RTTMON-MIB.my</a>&gt;
