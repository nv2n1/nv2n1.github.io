---
title: "smokeping_master_slave(7)"
name: "smokeping_master_slave"
section: "7"
letter: "s"
url: "/docs/linux/man/7-smokeping_master_slave/"
---

smokeping_master_slave - How to run multiple distributed instances of SmokePing

<h2>Overview</h2>

Normally smokeping probes run their tests from the host where smokeping runs to some target host and monitor the latency of the connection between the two. 

 The Master/Slave concept enables all smokeping probes to run remotely. The use case for this is to measure the overall connectivity in a network. If you are interested in checking that your central <font SIZE="-1">DNS</font> server or your file server works for everyone, you could setup several smokeping instances checking up on on the two servers from multiple locations within your network. With the Master/Slave smokeping configuration this process becomes much simpler, as one smokeping master server can control multiple slaves. 

 All monitoring data is stored and presented on the server, but collected by the slaves. The slaves will also get their configuration information from the master, so that you just have to maintain the master server configuration file and the rest is taken care of automatically.

<h2>Description</h2>

<h3>Architecture</h3>

The slaves communicate with the master smokeping server via the normal smokeping web interface. On initial startup each slave connects to the master server and asks for its assignments. When the slave has done a round of probing it connects to the master again to deliver the results. 

 If the assignment for a slave changes, the master will tell the slave after the slave has delivered its results. 

 The master and the slaves sign their messages by supplying an <font SIZE="-1">HMAC-MD5</font> code (<font SIZE="-1">RFC 2104</font>) of the message and a shared secret. Optionally the whole communication can run over ssl. 

 <pre> [slave 1] [slave 2] [slave 3]
 | | |
 +-------+ | +--------+
 | | |
 v v v
 +---------------+
 | master |
 +---------------+</pre>The slave is a normal smokeping instance setup where the configuration comes from the master instead of a local configuration file. The slave tries to contact the master server after every round of probing, supplying its results. If the master server can not be reached, the results will be sent to the server together with the next round of results. Results will be stored in a file in Perl storable form so that they survive a restart of the smokeping instance.

<h3>Master Configuration</h3>

To configure a master/slave setup, add a slaves section to your smokeping configuration file. Each slave has a section in the slaves part of the master configuration file. The section name must match the hostname of the slave. If some configuration parameter must be set to a special value for the slave, use an override section to configure this. 

 The slave names must be the names the hosts think they have, not their outside hostnames or ip addresses or anything like that. When the slave calls the master to get its config or report its measurements it will tell the master its 'hostname'. This together with the shared secret is used to authenticate and identify who is who. 

 <pre> *** Slaves ***
 secrets=/etc/smokeping/slavesecrets.conf 
 +slave1
 display_name=erul22
 location=India
 color=ff0000
 ++override
 Probes.FPing.binary = /usr/bin/fping
 ...</pre>Then in the targets section you can define slaves at every level. Again the settings get inherited by lower order targets and can be overwritten anywhere in the tree. 

 A slave will then get the appropriate configuration assigned by the server. 

 <pre> *** Targets ***
 slaves = slave1 slave2
 ...
 +dest1
 slaves =
 ...
 +dest2
 slaves = slave1
 ...
 +dest3
 ...</pre>The data from the slaves will be stored in <i>TargetName~SlaveName.rrd</i>. So the example above would create the following files: 

 <pre> dest1.rrd
 dest2.rrd
 dest2~slave1.rrd
 dest3.rrd
 dest3~slave1.rrd
 dest3~slave2.rrd</pre>The <i>slavesecrets.conf</i> file contains a colon separated list of hostnames and secrets. 

 <pre> host1:secret1
 host2:secret2</pre>

<h3>Slave Configuration</h3>

A smokeping slave setup has no configuration file. It just needs to know that it runs in slave-mode and its secret. The secret is stored in a file for optimal protection. By default the persistent data cache will be located in <i>/tmp/smokeping.$USER.cache</i>. 

 <pre> ./smokeping --master-url=<a rel="nofollow" HREF="http://smokeping/smokeping.cgi">http://smokeping/smokeping.cgi</a> \
 --cache-dir=/var/smokeping/ \
 --shared-secret=/var/smokeping/secret.txt</pre>The <i>secret.txt</i> file contains a single word, the secret of this slave. It is <font SIZE="-1">NOT</font> the same as the <i>slavesecrets.conf</i> file the master uses.

<h2>Security Considerations</h2>

The master effectively has full access to slave hosts as the user running the slave smokeping instance. The configuration is transferred as Perl code that is evaluated on the slave. While this is done inside a restricted <tt>&quot;Safe&quot;</tt> compartment, there are various ways that a malicious master could embed arbitrary commands in the configuration and get them to run when the slave probes its targets. 

 The strength of the shared secret is thus of paramount importance. Brute forcing the secret would enable a man-in-the-middle to inject a malicious new configuration and compromise the slave.

<h2>Copyright</h2>

Copyright (c) 2007 by Tobias Oetiker, <font SIZE="-1">OETIKER+PARTNER AG.</font> All right reserved.

<h2>License</h2>

This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. 

 You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font>

<h2>Author</h2>

Tobias Oetiker &lt;tobi [at] oetiker.ch&gt;
