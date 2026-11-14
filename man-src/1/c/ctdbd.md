---
title: "ctdbd(1)"
name: "ctdbd"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ctdbd/"
description: "ctdbd – The CTDB cluster daemon"
---

<h2 class="name">NAME</h2>
<p> ctdbd &#8211; The CTDB cluster daemon </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ctdbd</code> [<i>OPTION</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>ctdbd is the main CTDB daemon. </p>
<p> Note that ctdbd is not usually invoked directly. It is invoked via <code><a href="/docs/linux/man/1-ctdbd_wrapper/">ctdbd_wrapper</a></code>(1) or via the initscript. </p>
<p> See <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7) for an overview of CTDB.</p>
<h2>GENERAL OPTIONS</h2>
<p> -d, &#8211;debug=<i>DEBUGLEVEL</i></p>
<dl>
<dt>
<dd> This option sets the debug level to DEBUGLEVEL, which controls what will be written by the logging subsystem. The default is 2. </p>
<p> See the DEBUG LEVELS section in <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7) for more information.</dl>
<p> &#8211;dbdir=<i>DIRECTORY</i></p>
<dl>
<dt>
<dd> DIRECTORY on local storage where ctdbd keeps a local copy of TDB databases. This directory is local for each node and should not be stored on the shared cluster filesystem. </p>
<p> Defaults to /var/lib/ctdb.</dl>
<p> &#8211;dbdir-persistent=<i>DIRECTORY</i></p>
<dl>
<dt>
<dd> DIRECTORY on local storage where ctdbd keeps a local copy of persistent TDB databases. This directory is local for each node and should not be stored on the shared cluster filesystem. </p>
<p> Defaults to /var/lib/ctdb/persistent.</dl>
<p> &#8211;dbdir-state=<i>DIRECTORY</i></p>
<dl>
<dt>
<dd> DIRECTORY on local storage where ctdbd keep internal state TDB files. This directory is local for each node and should not be stored on the shared cluster filesystem. </p>
<p> Defaults to /var/lib/ctdb/state.</dl>
<p> &#8211;event-script-dir=<i>DIRECTORY</i></p>
<dl>
<dt>
<dd> DIRECTORY where the CTDB event scripts are stored. See the EVENT SCRIPTS section in <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7) for more information. </p>
<p> Default is <code>CTDB_BASE</code>/events.d, so usually /etc/ctdb/events.d, which is part of the CTDB installation.</dl>
<p> &#8211;listen=<i>IPADDR</i></p>
<dl>
<dt>
<dd> IPADDR is the private IP address that ctdbd will bind to. </p>
<p> By default ctdbd will select the first address from the nodes list that in can bind to. See also &#8211;nlist. </p>
<p> This option is only required when automatic address detection can not be used. This can be the case when running multiple ctdbd daemons/nodes on the same physical host (usually for testing), using InfiniBand for the private network or on Linux when sysctl net.ipv4.ip_nonlocal_bind=1.</dl>
<p> &#8211;logging=<i>STRING</i></p>
<dl>
<dt>
<dd> STRING specifies where ctdbd will write its log. The default is file:/var/log/log.ctdb. </p>
<p> Valid values are: </p>
<p> file:<i>FILENAME</i></p>
<dl>
<dt>
<dd> FILENAME where ctdbd will write its log. This is usually /var/log/log.ctdb.</dl>
<p> syslog[:<i>METHOD</i>]</p>
<dl>
<dt>
<dd> CTDB will log to syslog. By default this will use the <a href="/docs/linux/man/3-syslog/">syslog</a>(3) API. </p>
<p> Under heavy loads <a href="/docs/linux/man/3-syslog/">syslog</a>(3) can block if the syslog daemon processes messages too slowly. This can cause CTDB to block when logging. </p>
<p> If METHOD is specified then it specifies an extension that causes logging to be done in a non-blocking mode. Note that <i>this may cause messages to be dropped</i>. METHOD must be one of: </p>
<p> nonblocking</p>
<dl>
<dt>
<dd> CTDB will log to syslog via /dev/log in non-blocking mode.</dl>
<p> udp</p>
<dl>
<dt>
<dd> CTDB will log to syslog via UDP to localhost:514. The syslog daemon must be configured to listen on (at least) localhost:514. Most syslog daemons will log the messages with hostname &quot;localhost&quot; &#8211; this is a limitation of the implementation, for compatibility with more syslog daemons.</dl>
<p> udp-rfc5424</p>
<dl>
<dt>
<dd> As with &quot;udp&quot; but messages are sent in RFC5424 format. This method will log the correct hostname but is not as widely implemented in syslog daemons.</dl>
</dl>
</dl>
<p> &#8211;lvs</p>
<dl>
<dt>
<dd> This option is used to activate the LVS capability on a CTDB node. Please see the LVS section in <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7) for more information.</dl>
<p> &#8211;max-persistent-check-errors=<i>NUM</i></p>
<dl>
<dt>
<dd> NUM specifies the maximum number of health check failures allowed for persistent databases during startup. </p>
<p> The default value is 0. Setting this to non-zero allows a node with unhealthy persistent databases to startup and join the cluster as long as there is another node with healthy persistent databases.</dl>
<p> &#8211;nlist=<i>FILENAME</i></p>
<dl>
<dt>
<dd> FILENAME containing a list of the private IP addresses, one per line, for each node in the cluster. This file <i>must be the same on each node</i> in the cluster. </p>
<p> Default is <code>CTDB_BASE</code>/nodes, so usually /etc/ctdb/nodes.</dl>
<p> &#8211;no-lmaster</p>
<dl>
<dt>
<dd> This argument specifies that this node can NOT become an lmaster for records in the database. This means that it will never show up in the vnnmap. This feature is primarily used for making a cluster span across a WAN link and use CTDB as a WAN-accelerator. </p>
<p> Please see the REMOTE CLUSTER NODES section in <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7) for more information.</dl>
<p> &#8211;no-recmaster</p>
<dl>
<dt>
<dd> This argument specifies that this node can NOT become a recmaster for the database. This feature is primarily used for making a cluster span across a WAN link and use CTDB as a WAN-accelerator. </p>
<p> Please see the REMOTE CLUSTER NODES section in <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7) for more information.</dl>
<p> &#8211;notification-script=<i>FILENAME</i></p>
<dl>
<dt>
<dd> FILENAME specifying a script to be invoked by ctdbd when certain state changes occur. </p>
<p> This file is usually /etc/ctdb/notify.sh. </p>
<p> Please see the NOTIFICATION SCRIPT section in <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7) for more information.</dl>
<p> &#8211;pidfile=<i>FILENAME</i></p>
<dl>
<dt>
<dd> FILENAME for file containing process ID of main CTDB daemon. This file is automatically created and removed by CTDB. </p>
<p> The default is to not create a PID file.</dl>
<p> &#8211;public_addresses=<i>FILENAME</i></p>
<dl>
<dt>
<dd> FILENAME specifying a file containing the public IP addresses to use on the cluster when CTDB should use IP takeover. This file contains a list of IP addresses, netmasks and interfaces. CTDB will distribute these public IP addresses appropriately across the available nodes. </p>
<p> The IP addresses specified in this file can differ across nodes. </p>
<p> This is usually the file /etc/ctdb/public_addresses</dl>
<p> &#8211;public-interface=<i>INTERFACE</i></p>
<dl>
<dt>
<dd> INTERFACE on which to attach public IP addresses or on which to attach the single-public-ip when used. </p>
<p> When using public IP addresses, this is only required if interfaces are not explicitly specified in the public addresses file.</dl>
<p> &#8211;reclock=<i>FILE</i></p>
<dl>
<dt>
<dd> FILE is the name of the recovery lock file, stored in <i>shared storage</i>, that CTDB uses to prevent split brains. </p>
<p> For information about the recovery lock please see the RECOVERY LOCK section in <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7).</dl>
<p> &#8211;single-public-ip=<i>IPADDR</i></p>
<dl>
<dt>
<dd> IPADDR specifies the single IP that CTDB will use in conjunction with LVS. </p>
<p> Please see the LVS section in <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7) for more information.</dl>
<p> &#8211;start-as-disabled</p>
<dl>
<dt>
<dd> This makes ctdbd start in the DISABLED state. </p>
<p> To allow the node to host public IP addresses and services, it must be manually enabled using the <code>ctdb enable</code> command. </p>
<p> Please see the NODE STATES section in <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7) for more information about the DISABLED state.</dl>
<p> &#8211;start-as-stopped</p>
<dl>
<dt>
<dd> This makes ctdbd start in the STOPPED state. </p>
<p> To allow the node to take part in the cluster it must be manually continued with the the <code>ctdb enable</code> command. </p>
<p> Please see the NODE STATES section in <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7) for more information about the STOPPED state.</dl>
<p> &#8211;transport=tcp|infiniband</p>
<dl>
<dt>
<dd> This option specifies which transport to use for ctdbd internode communications. The default is &quot;tcp&quot;. </p>
<p> The &quot;infiniband&quot; support is not regularly tested.</dl>
<p> -?, &#8211;help</p>
<dl>
<dt>
<dd> Display a summary of options.</dl>
<h2>DEBUGGING OPTIONS</h2>
<p> -i, &#8211;interactive</p>
<dl>
<dt>
<dd> Enable interactive mode. This will make ctdbd run in the foreground and not detach from the terminal. By default ctdbd will detach itself and run in the background as a daemon.</dl>
<p> &#8211;nopublicipcheck</p>
<dl>
<dt>
<dd> This option is used when testing with multiple local daemons on a single machine. It disables checks related to public IP addresses.</dl>
<p> &#8211;nosetsched</p>
<dl>
<dt>
<dd> This is a debugging option. This option is only used when debugging ctdbd. </p>
<p> Normally ctdbd will change its scheduler to run as a real-time process. This is the default mode for a normal ctdbd operation to gurarantee that ctdbd always gets the CPU cycles that it needs. </p>
<p> This option is used to tell ctdbd to <i>not</i> run as a real-time process and instead run ctdbd as a normal userspace process. This is useful for debugging and when you want to run ctdbd under valgrind or gdb. (You don&#8217;t want to attach valgrind or gdb to a real-time process.)</dl>
<p> &#8211;socket=<i>FILENAME</i></p>
<dl>
<dt>
<dd> FILENAME specifies the name of the Unix domain socket that ctdbd will create. This socket is used by local clients to communicate with ctdbd. </p>
<p> The default is /var/run/ctdb/ctdbd.socket. You only need to use this option if you plan to run multiple ctdbd daemons on the same physical host, usually for testing.</dl>
<p> &#8211;script-log-level=<i>DEBUGLEVEL</i></p>
<dl>
<dt>
<dd> This option sets the debug level of event script output to DEBUGLEVEL. The default is ERR (0). </p>
<p> See the DEBUG LEVELS section in <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7) for more information.</dl>
<p> &#8211;sloppy-start</p>
<dl>
<dt>
<dd> This is debugging option. This speeds up the initial recovery during startup at the expense of some consistency checking. <i>Don&#8217;t use this option in production</i>.</dl>
<p> &#8211;torture</p>
<dl>
<dt>
<dd> This option is only used for development and testing of CTDB. It adds artificial errors and failures to the common codepaths in ctdbd to verify that ctdbd can recover correctly from failures. </p>
<p> <i>Do not use this option</i> unless you are developing and testing new functionality in CTDB.</dl>
<p> &#8211;valgrinding</p>
<dl>
<dt>
<dd> This is a debugging option. This option is only used when debugging ctdbd. This enables additional debugging capabilities and implies &#8211;nosetsched.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ctdb/">ctdb</a></code>(1), <code><a href="/docs/linux/man/1-ctdbd_wrapper/">ctdbd_wrapper</a></code>(1), <code><a href="/docs/linux/man/1-onnode/">onnode</a></code>(1), <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7), <code><a href="/docs/linux/man/7-ctdb-tunables/">ctdb-tunables</a></code>(7), m[blue]<code><a rel="nofollow" href="http://ctdb.samba.org/">http://ctdb.samba.org/</a></code>m[]</p>
<h2>AUTHOR</h2>
<p> This documentation was written by Ronnie Sahlberg, Amitay Isaacs, Martin Schwenke</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2007 Andrew Tridgell, Ronnie Sahlberg </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, see m[blue]<code><a rel="nofollow" href="http://www.gnu.org/licenses">http://www.gnu.org/licenses</a></code>m[]. </p>
<h2>Index</h2>
