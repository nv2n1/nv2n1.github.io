---
title: "ctdb(1)"
name: "ctdb"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ctdb/"
description: "ctdb – CTDB management utility"
---

<h2 class="name">NAME</h2>
<p> ctdb &#8211; CTDB management utility </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ctdb</code> [<i>OPTION</i>&#8230;] {<i>COMMAND</i>} [<i>COMMAND-ARGS</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>ctdb is a utility to view and manage a CTDB cluster. </p>
<p> The following terms are used when referring to nodes in a cluster: </p>
<p> PNN</p>
<dl>
<dt>
<dd> Physical Node Number. The physical node number is an integer that describes the node in the cluster. The first node has physical node number 0. in a cluster.</dl>
<p> PNN-LIST</p>
<dl>
<dt>
<dd> This is either a single PNN, a comma-separate list of PNNs or &quot;all&quot;.</dl>
<p> Commands that reference a database use the following terms: </p>
<p> DB</p>
<dl>
<dt>
<dd> This is either a database name, such as locking.tdb or a database ID such as &quot;0x42fe72c5&quot;.</dl>
<p> DB-LIST</p>
<dl>
<dt>
<dd> A space separated list of at least one <i>DB</i>.</dl>
<h2>OPTIONS</h2>
<p> -n <i>PNN-LIST</i></p>
<dl>
<dt>
<dd> The nodes specified by PNN-LIST should be queried for the requested information. Default is to query the daemon running on the local host.</dl>
<p> -Y</p>
<dl>
<dt>
<dd> Produce output in machine readable form for easier parsing by scripts. This uses a field delimiter of &#8216;:&#8217;. Not all commands support this option.</dl>
<p> -x <i>SEPARATOR</i></p>
<dl>
<dt>
<dd> Use SEPARATOR to delimit fields in machine readable output. This implies -Y.</dl>
<p> -X</p>
<dl>
<dt>
<dd> Produce output in machine readable form for easier parsing by scripts. This uses a field delimiter of &#8216;|&#8217;. Not all commands support this option. </p>
<p> This is equivalent to &quot;-x|&quot; and avoids some shell quoting issues.</dl>
<p> -t <i>TIMEOUT</i></p>
<dl>
<dt>
<dd> Indicates that ctdb should wait up to TIMEOUT seconds for a response to most commands sent to the CTDB daemon. The default is 10 seconds.</dl>
<p> -T <i>TIMELIMIT</i></p>
<dl>
<dt>
<dd> Indicates that TIMELIMIT is the maximum run time (in seconds) for the ctdb command. When TIMELIMIT is exceeded the ctdb command will terminate with an error. The default is 120 seconds.</dl>
<p> -? &#8211;help</p>
<dl>
<dt>
<dd> Print some help text to the screen.</dl>
<p> &#8211;usage</p>
<dl>
<dt>
<dd> Print useage information to the screen.</dl>
<p> -d &#8211;debug=<i>DEBUGLEVEL</i></p>
<dl>
<dt>
<dd> Change the debug level for the command. Default is NOTICE (2).</dl>
<p> &#8211;socket=<i>FILENAME</i></p>
<dl>
<dt>
<dd> Specify that FILENAME is the name of the Unix domain socket to use when connecting to the local CTDB daemon. The default is /var/run/ctdb/ctdbd.socket.</dl>
<h2>ADMINISTRATIVE COMMANDS</h2>
<p> These are commands used to monitor and administer a CTDB cluster.</p>
<h3>pnn</h3>
<p> This command displays the PNN of the current node.</p>
<h3>xpnn</h3>
<p> This command displays the PNN of the current node without contacting the CTDB daemon. It parses the nodes file directly, so can produce unexpected output if the nodes file has been edited but has not been reloaded.</p>
<h3>status</h3>
<p> This command shows the current status of all CTDB nodes based on information from the queried node. </p>
<p> Note: If the the queried node is INACTIVE then the status might not be current. </p>
<p> <font SIZE="+1"> <code>Node status</code></p>
<dl>
<dt>
<dd>
<p> This includes the number of physical nodes and the status of each node. See <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7) for information about node states.</dl>
<p> </font><font SIZE="+2"> <code>Generation</code></p>
<dl>
<dt>
<dd>
<p> The generation id is a number that indicates the current generation of a cluster instance. Each time a cluster goes through a reconfiguration or a recovery its generation id will be changed. </p>
<p> This number does not have any particular meaning other than to keep track of when a cluster has gone through a recovery. It is a random number that represents the current instance of a ctdb cluster and its databases. The CTDB daemon uses this number internally to be able to tell when commands to operate on the cluster and the databases was issued in a different generation of the cluster, to ensure that commands that operate on the databases will not survive across a cluster database recovery. After a recovery, all old outstanding commands will automatically become invalid. </p>
<p> Sometimes this number will be shown as &quot;INVALID&quot;. This only means that the ctdbd daemon has started but it has not yet merged with the cluster through a recovery. All nodes start with generation &quot;INVALID&quot; and are not assigned a real generation id until they have successfully been merged with a cluster through a recovery.</dl>
<p> </font><font SIZE="+3"> <code>Virtual Node Number (VNN) map</code></p>
<dl>
<dt>
<dd>
<p> Consists of the number of virtual nodes and mapping from virtual node numbers to physical node numbers. Virtual nodes host CTDB databases. Only nodes that are participating in the VNN map can become lmaster or dmaster for database records.</dl>
<p> </font><font SIZE="+4"> <code>Recovery mode</code></p>
<dl>
<dt>
<dd>
<p> This is the current recovery mode of the cluster. There are two possible modes: </p>
<p> NORMAL &#8211; The cluster is fully operational. </p>
<p> RECOVERY &#8211; The cluster databases have all been frozen, pausing all services while the cluster awaits a recovery process to complete. A recovery process should finish within seconds. If a cluster is stuck in the RECOVERY state this would indicate a cluster malfunction which needs to be investigated. </p>
<p> Once the recovery master detects an inconsistency, for example a node becomes disconnected/connected, the recovery daemon will trigger a cluster recovery process, where all databases are remerged across the cluster. When this process starts, the recovery master will first &quot;freeze&quot; all databases to prevent applications such as samba from accessing the databases and it will also mark the recovery mode as RECOVERY. </p>
<p> When the CTDB daemon starts up, it will start in RECOVERY mode. Once the node has been merged into a cluster and all databases have been recovered, the node mode will change into NORMAL mode and the databases will be &quot;thawed&quot;, allowing samba to access the databases again.</dl>
<p> </font><font SIZE="+5"> <code>Recovery master</code></p>
<dl>
<dt>
<dd>
<p> This is the cluster node that is currently designated as the recovery master. This node is responsible of monitoring the consistency of the cluster and to perform the actual recovery process when reqired. </p>
<p> Only one node at a time can be the designated recovery master. Which node is designated the recovery master is decided by an election process in the recovery daemons running on each node.</dl>
<p> </font><font SIZE="+6"> <code>Example</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> </font></p>
<pre>
# ctdb status
Number of nodes:4
pnn:0 192.168.2.200       OK (THIS NODE)
pnn:1 192.168.2.201       OK
pnn:2 192.168.2.202       OK
pnn:3 192.168.2.203       OK
Generation:1362079228
Size:4
hash:0 lmaster:0
hash:1 lmaster:1
hash:2 lmaster:2
hash:3 lmaster:3
Recovery mode:NORMAL (0)
Recovery master:0
        
</pre>
</dl>
</dl>
<h3>nodestatus [<i>PNN-LIST</i>]</h3>
<p> This command is similar to the <code>status</code> command. It displays the &quot;node status&quot; subset of output. The main differences are: </p>
<dl>
<dt>
<dd> &bull; The exit code is the bitwise-OR of the flags for each specified node, while <code>ctdb status</code> exits with 0 if it was able to retrieve status for all nodes.</dl>
<dl>
<dt>
<dd> &bull; <code>ctdb status</code> provides status information for all nodes. <code>ctdb nodestatus</code> defaults to providing status for only the current node. If PNN-LIST is provided then status is given for the indicated node(s).</dl>
<p> A common invocation in scripts is <code>ctdb nodestatus all</code> to check whether all nodes in a cluster are healthy. </p>
<p> <font SIZE="+1"> <code>Example</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> </font></p>
<pre>
# ctdb nodestatus
pnn:0 10.0.0.30        OK (THIS NODE)
# ctdb nodestatus all
Number of nodes:2
pnn:0 10.0.0.30        OK (THIS NODE)
pnn:1 10.0.0.31        OK
        
</pre>
</dl>
</dl>
<h3>recmaster</h3>
<p> This command shows the pnn of the node which is currently the recmaster. </p>
<p> Note: If the the queried node is INACTIVE then the status might not be current.</p>
<h3>uptime</h3>
<p> This command shows the uptime for the ctdb daemon. When the last recovery or ip-failover completed and how long it took. If the &quot;duration&quot; is shown as a negative number, this indicates that there is a recovery/failover in progress and it started that many seconds ago. </p>
<p> <font SIZE="+1"> <code>Example</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> </font></p>
<pre>
# ctdb uptime
Current time of node          :                Thu Oct 29 10:38:54 2009
Ctdbd start time              : (000 16:54:28) Wed Oct 28 17:44:26 2009
Time of last recovery/failover: (000 16:53:31) Wed Oct 28 17:45:23 2009
Duration of last recovery/failover: 2.248552 seconds
        
</pre>
</dl>
</dl>
<h3>listnodes</h3>
<p> This command shows lists the ip addresses of all the nodes in the cluster. </p>
<p> <font SIZE="+1"> <code>Example</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> </font></p>
<pre>
# ctdb listnodes
192.168.2.200
192.168.2.201
192.168.2.202
192.168.2.203
        
</pre>
</dl>
</dl>
<h3>natgwlist</h3>
<p> Show the current NAT gateway master and the status of all nodes in the current NAT gateway group. See the NAT GATEWAY section in <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7) for more details. </p>
<p> <font SIZE="+1"> <code>Example</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> </font></p>
<pre>
# ctdb natgwlist
0 192.168.2.200
Number of nodes:4
pnn:0 192.168.2.200       OK (THIS NODE)
pnn:1 192.168.2.201       OK
pnn:2 192.168.2.202       OK
pnn:3 192.168.2.203       OK
        
</pre>
</dl>
</dl>
<h3>ping</h3>
<p> This command will &quot;ping&quot; specified CTDB nodes in the cluster to verify that they are running. </p>
<p> <font SIZE="+1"> <code>Example</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> </font></p>
<pre>
# ctdb ping
response from 0 time=0.000054 sec  (3 clients)
        
</pre>
</dl>
</dl>
<h3>ifaces</h3>
<p> This command will display the list of network interfaces, which could host public addresses, along with their status. </p>
<p> <font SIZE="+1"> <code>Example</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> </font></p>
<pre>
# ctdb ifaces
Interfaces on node 0
name:eth5 link:up references:2
name:eth4 link:down references:0
name:eth3 link:up references:1
name:eth2 link:up references:1
# ctdb -X ifaces
|Name|LinkStatus|References|
|eth5|1|2|
|eth4|0|0|
|eth3|1|1|
|eth2|1|1|
        
</pre>
</dl>
</dl>
<h3>ip</h3>
<p> This command will display the list of public addresses that are provided by the cluster and which physical node is currently serving this ip. By default this command will ONLY show those public addresses that are known to the node itself. To see the full list of all public ips across the cluster you must use &quot;ctdb ip all&quot;. </p>
<p> <font SIZE="+1"> <code>Example</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> </font></p>
<pre><code>
#ctdb ip - v
Public IPs on node 0 172.31.91.82 node[1] active[] available[eth2, eth3] configured[eth2, eth3] 172.31.91.83 node[0] active[eth3] available[eth2, eth3] configured[eth2, eth3] 172.31.91.84 node[1] active[] available[eth2, eth3] configured[eth2, eth3] 172.31.91.85 node[0] active[eth2] available[eth2, eth3] configured[eth2, eth3] 172.31.92.82 node[1] active[] available[eth5] configured[eth4, eth5] 172.31.92.83 node[0] active[eth5] available[eth5] configured[eth4, eth5] 172.31.92.84 node[1] active[] available[eth5] configured[eth4, eth5] 172.31.92.85 node[0] active[eth5] available[eth5] configured[eth4, eth5]
#ctdb - X ip - v
        | Public IP | Node | ActiveInterface | AvailableInterfaces | ConfiguredInterfaces |
        | 172.31.91.82 | 1 ||
    eth2,
    eth3 | eth2, eth3 | | 172.31.91.83 | 0 | eth3 | eth2, eth3 | eth2, eth3 | | 172.31.91.84 | 1 || eth2, eth3 | eth2, eth3 | | 172.31.91.85 | 0 | eth2 | eth2, eth3 | eth2, eth3 | | 172.31.92.82 | 1 || eth5 | eth4, eth5 | | 172.31.92.83 | 0 | eth5 | eth5 | eth4, eth5 | | 172.31.92.84 | 1 || eth5 | eth4, eth5 | | 172.31.92.85 | 0 | eth5 | eth5 | eth4, eth5 |
</code></pre>
</dl>
</dl>
<h3>ipinfo <i>IP</i></h3>
<p> This command will display details about the specified public addresses. </p>
<p> <font SIZE="+1"> <code>Example</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> </font></p>
<pre><code>
#ctdb ipinfo 172.31.92.85
Public IP[172.31.92.85] info on node 0 IP : 172.31.92.85 CurrentNode : 0 NumInterfaces : 2 Interface[1] : Name : eth4 Link : down References : 0 Interface[2] : Name : eth5 Link : up References : 2(active)
</code></pre>
</dl>
</dl>
<h3>scriptstatus</h3>
<p> This command displays which scripts where run in the previous monitoring cycle and the result of each script. If a script failed with an error, causing the node to become unhealthy, the output from that script is also shown. </p>
<p> <font SIZE="+1"> <code>Example</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> </font></p>
<pre>
# ctdb scriptstatus
7 scripts were executed last monitoring cycle
00.ctdb              Status:OK    Duration:0.056 Tue Mar 24 18:56:57 2009
10.interface         Status:OK    Duration:0.077 Tue Mar 24 18:56:57 2009
11.natgw             Status:OK    Duration:0.039 Tue Mar 24 18:56:57 2009
20.multipathd        Status:OK    Duration:0.038 Tue Mar 24 18:56:57 2009
31.clamd             Status:DISABLED
40.vsftpd            Status:OK    Duration:0.045 Tue Mar 24 18:56:57 2009
41.httpd             Status:OK    Duration:0.039 Tue Mar 24 18:56:57 2009
50.samba             Status:ERROR    Duration:0.082 Tue Mar 24 18:56:57 2009
OUTPUT:ERROR: Samba tcp port 445 is not responding
      
</pre>
</dl>
</dl>
<h3>disablescript <i>SCRIPT</i></h3>
<p> This command is used to disable an eventscript. </p>
<p> This will take effect the next time the eventscripts are being executed so it can take a short while until this is reflected in &#8216;scriptstatus&#8217;.</p>
<h3>enablescript <i>SCRIPT</i></h3>
<p> This command is used to enable an eventscript. </p>
<p> This will take effect the next time the eventscripts are being executed so it can take a short while until this is reflected in &#8216;scriptstatus&#8217;.</p>
<h3>listvars</h3>
<p> List all tuneable variables, except the values of the obsolete tunables like VacuumMinInterval. The obsolete tunables can be retrieved only explicitly with the &quot;ctdb getvar&quot; command. </p>
<p> <font SIZE="+1"> <code>Example</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> </font></p>
<pre>
# ctdb listvars
MaxRedirectCount        = 3
SeqnumInterval          = 1000
ControlTimeout          = 60
TraverseTimeout         = 20
KeepaliveInterval       = 5
KeepaliveLimit          = 5
RecoverTimeout          = 20
RecoverInterval         = 1
ElectionTimeout         = 3
TakeoverTimeout         = 9
MonitorInterval         = 15
TickleUpdateInterval    = 20
EventScriptTimeout      = 30
MonitorTimeoutCount     = 1
RecoveryGracePeriod     = 120
RecoveryBanPeriod       = 300
DatabaseHashSize        = 100001
DatabaseMaxDead         = 5
RerecoveryTimeout       = 10
EnableBans              = 1
DeterministicIPs        = 0
LCP2PublicIPs           = 1
ReclockPingPeriod       = 60
NoIPFailback            = 0
DisableIPFailover       = 0
VerboseMemoryNames      = 0
RecdPingTimeout         = 60
RecdFailCount           = 10
LogLatencyMs            = 0
RecLockLatencyMs        = 1000
RecoveryDropAllIPs      = 120
VacuumInterval          = 10
VacuumMaxRunTime        = 30
RepackLimit             = 10000
VacuumLimit             = 5000
VacuumFastPathCount     = 60
MaxQueueDropMsg         = 1000000
UseStatusEvents         = 0
AllowUnhealthyDBRead    = 0
StatHistoryInterval     = 1
DeferredAttachTO        = 120
AllowClientDBAttach     = 1
RecoverPDBBySeqNum      = 0
        
</pre>
</dl>
</dl>
<h3>getvar <i>NAME</i></h3>
<p> Get the runtime value of a tuneable variable. </p>
<p> <font SIZE="+1"> <code>Example</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> </font></p>
<pre>
# ctdb getvar MaxRedirectCount
MaxRedirectCount    = 3
        
</pre>
</dl>
</dl>
<h3>setvar <i>NAME</i> <i>VALUE</i></h3>
<p> Set the runtime value of a tuneable variable. </p>
<p> Example: ctdb setvar MaxRedirectCount 5</p>
<h3>lvsmaster</h3>
<p> This command shows which node is currently the LVSMASTER. The LVSMASTER is the node in the cluster which drives the LVS system and which receives all incoming traffic from clients. </p>
<p> LVS is the mode where the entire CTDB/Samba cluster uses a single ip address for the entire cluster. In this mode all clients connect to one specific node which will then multiplex/loadbalance the clients evenly onto the other nodes in the cluster. This is an alternative to using public ip addresses. See the manpage for ctdbd for more information about LVS.</p>
<h3>lvs</h3>
<p> This command shows which nodes in the cluster are currently active in the LVS configuration. I.e. which nodes we are currently loadbalancing the single ip address across. </p>
<p> LVS will by default only loadbalance across those nodes that are both LVS capable and also HEALTHY. Except if all nodes are UNHEALTHY in which case LVS will loadbalance across all UNHEALTHY nodes as well. LVS will never use nodes that are DISCONNECTED, STOPPED, BANNED or DISABLED. </p>
<p> Example output: </p>
<dl>
<dt>
<dd>
<pre>
2:10.0.0.13
3:10.0.0.14
      
</pre>
</dl>
<h3>getcapabilities</h3>
<p> This command shows the capabilities of the current node. See the CAPABILITIES section in <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7) for more details. </p>
<p> Example output: </p>
<dl>
<dt>
<dd>
<pre>
RECMASTER: YES
LMASTER: YES
LVS: NO
      
</pre>
</dl>
<h3>statistics</h3>
<p> Collect statistics from the CTDB daemon about how many calls it has served. Information about various fields in statistics can be found in <code><a href="/docs/linux/man/7-ctdb-statistics/">ctdb-statistics</a></code>(7). </p>
<p> <font SIZE="+1"> <code>Example</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> </font></p>
<pre>
# ctdb statistics
CTDB version 1
num_clients                        3
frozen                             0
recovering                         0
client_packets_sent           360489
client_packets_recv           360466
node_packets_sent             480931
node_packets_recv             240120
keepalive_packets_sent             4
keepalive_packets_recv             3
node
req_call                       2
reply_call                     2
req_dmaster                    0
reply_dmaster                  0
reply_error                    0
req_message                   42
req_control               120408
reply_control             360439
client
req_call                       2
req_message                   24
req_control               360440
timeouts
call                           0
control                        0
traverse                       0
total_calls                        2
pending_calls                      0
lockwait_calls                     0
pending_lockwait_calls             0
memory_used                     5040
max_hop_count                      0
max_call_latency                   4.948321 sec
max_lockwait_latency               0.000000 sec
        
</pre>
</dl>
</dl>
<h3>statisticsreset</h3>
<p> This command is used to clear all statistics counters in a node. </p>
<p> Example: ctdb statisticsreset</p>
<h3>dbstatistics <i>DB</i></h3>
<p> Display statistics about the database DB. Information about various fields in dbstatistics can be found in <code><a href="/docs/linux/man/7-ctdb-statistics/">ctdb-statistics</a></code>(7). </p>
<p> <font SIZE="+1"> <code>Example</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> </font></p>
<pre>
# ctdb dbstatistics locking.tdb
DB Statistics: locking.tdb
 ro_delegations                     0
 ro_revokes                         0
 locks
     total                      14356
     failed                         0
     current                        0
     pending                        0
 hop_count_buckets: 28087 2 1 0 0 0 0 0 0 0 0 0 0 0 0 0
 lock_buckets: 0 14188 38 76 32 19 3 0 0 0 0 0 0 0 0 0
 locks_latency      MIN/AVG/MAX     0.001066/0.012686/4.202292 sec out of 14356
 Num Hot Keys:     1
     Count:8 Key:ff5bd7cb3ee3822edc1f0000000000000000000000000000
        
</pre>
</dl>
</dl>
<h3>getreclock</h3>
<p> Show the name of the recovery lock file, if any. </p>
<p> Example output: </p>
<dl>
<dt>
<dd>
<pre>
        Reclock file:/clusterfs/.ctdb/recovery.lock
      
</pre>
</dl>
<h3>setreclock [<i>FILE</i>]</h3>
<p> FILE specifies the name of the recovery lock file. If the recovery lock file is changed at run-time then this will cause a recovery, which in turn causes the recovery lock to be retaken. </p>
<p> If no FILE is specified then a recovery lock file will no longer be used. </p>
<p> This command only affects the run-time setting of a single CTDB node. This setting <i>must</i> be changed on all nodes simultaneously. For information about configuring the recovery lock file please see the CTDB_RECOVERY_LOCK entry in <code><a href="/docs/linux/man/5-ctdbd-conf/">ctdbd.conf</a></code>(5) and the &#8211;reclock entry in <code><a href="/docs/linux/man/1-ctdbd/">ctdbd</a></code>(1). For information about the recovery lock please see the RECOVERY LOCK section in <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7).</p>
<h3>getdebug</h3>
<p> Get the current debug level for the node. the debug level controls what information is written to the log file. </p>
<p> The debug levels are mapped to the corresponding syslog levels. When a debug level is set, only those messages at that level and higher levels will be printed. </p>
<p> The list of debug levels from highest to lowest are : </p>
<p> ERR WARNING NOTICE INFO DEBUG</p>
<h3>setdebug <i>DEBUGLEVEL</i></h3>
<p> Set the debug level of a node. This controls what information will be logged. </p>
<p> The debuglevel is one of ERR WARNING NOTICE INFO DEBUG</p>
<h3>getpid</h3>
<p> This command will return the process id of the ctdb daemon.</p>
<h3>disable</h3>
<p> This command is used to administratively disable a node in the cluster. A disabled node will still participate in the cluster and host clustered TDB records but its public ip address has been taken over by a different node and it no longer hosts any services.</p>
<h3>enable</h3>
<p> Re-enable a node that has been administratively disabled.</p>
<h3>stop</h3>
<p> This command is used to administratively STOP a node in the cluster. A STOPPED node is connected to the cluster but will not host any public ip addresse, nor does it participate in the VNNMAP. The difference between a DISABLED node and a STOPPED node is that a STOPPED node does not host any parts of the database which means that a recovery is required to stop/continue nodes.</p>
<h3>continue</h3>
<p> Re-start a node that has been administratively stopped.</p>
<h3>addip <i>IPADDR</i>/<i>mask</i> <i>IFACE</i></h3>
<p> This command is used to add a new public ip to a node during runtime. This allows public addresses to be added to a cluster without having to restart the ctdb daemons. </p>
<p> Note that this only updates the runtime instance of ctdb. Any changes will be lost next time ctdb is restarted and the public addresses file is re-read. If you want this change to be permanent you must also update the public addresses file manually.</p>
<h3>delip <i>IPADDR</i></h3>
<p> This command is used to remove a public ip from a node during runtime. If this public ip is currently hosted by the node it being removed from, the ip will first be failed over to another node, if possible, before it is removed. </p>
<p> Note that this only updates the runtime instance of ctdb. Any changes will be lost next time ctdb is restarted and the public addresses file is re-read. If you want this change to be permanent you must also update the public addresses file manually.</p>
<h3>moveip <i>IPADDR</i> <i>PNN</i></h3>
<p> This command can be used to manually fail a public ip address to a specific node. </p>
<p> In order to manually override the &quot;automatic&quot; distribution of public ip addresses that ctdb normally provides, this command only works when you have changed the tunables for the daemon to: </p>
<p> DeterministicIPs = 0 </p>
<p> NoIPFailback = 1</p>
<h3>shutdown</h3>
<p> This command will shutdown a specific CTDB daemon.</p>
<h3>setlmasterrole on|off</h3>
<p> This command is used ot enable/disable the LMASTER capability for a node at runtime. This capability determines whether or not a node can be used as an LMASTER for records in the database. A node that does not have the LMASTER capability will not show up in the vnnmap. </p>
<p> Nodes will by default have this capability, but it can be stripped off nodes by the setting in the sysconfig file or by using this command. </p>
<p> Once this setting has been enabled/disabled, you need to perform a recovery for it to take effect. </p>
<p> See also &quot;ctdb getcapabilities&quot;</p>
<h3>setrecmasterrole on|off</h3>
<p> This command is used ot enable/disable the RECMASTER capability for a node at runtime. This capability determines whether or not a node can be used as an RECMASTER for the cluster. A node that does not have the RECMASTER capability can not win a recmaster election. A node that already is the recmaster for the cluster when the capability is stripped off the node will remain the recmaster until the next cluster election. </p>
<p> Nodes will by default have this capability, but it can be stripped off nodes by the setting in the sysconfig file or by using this command. </p>
<p> See also &quot;ctdb getcapabilities&quot;</p>
<h3>reloadnodes</h3>
<p> This command is used when adding new nodes, or removing existing nodes from an existing cluster. </p>
<p> Procedure to add nodes: </p>
<dl>
<dt>
<dd> 1. To expand an existing cluster, first ensure with <code>ctdb status</code> that all nodes are up and running and that they are all healthy. Do not try to expand a cluster unless it is completely healthy!</dl>
<dl>
<dt>
<dd> 2. On all nodes, edit /etc/ctdb/nodes and <i>add the new nodes at the end of this file</i>.</dl>
<dl>
<dt>
<dd> 3. Verify that all the nodes have identical /etc/ctdb/nodes files after adding the new nodes.</dl>
<dl>
<dt>
<dd> 4. Run <code>ctdb reloadnodes</code> to force all nodes to reload the nodes file.</dl>
<dl>
<dt>
<dd> 5. Use <code>ctdb status</code> on all nodes and verify that they now show the additional nodes.</dl>
<dl>
<dt>
<dd> 6. Install and configure the new node and bring it online.</dl>
<p> Procedure to remove nodes: </p>
<dl>
<dt>
<dd> 1. To remove nodes from an existing cluster, first ensure with <code>ctdb status</code> that all nodes, except the node to be deleted, are up and running and that they are all healthy. Do not try to remove nodes from a cluster unless the cluster is completely healthy!</dl>
<dl>
<dt>
<dd> 2. Shutdown and power off the node to be removed.</dl>
<dl>
<dt>
<dd> 3. On all other nodes, edit the /etc/ctdb/nodes file and <i>comment out</i> the nodes to be removed. <i>Do not delete the lines for the deleted nodes</i>, just comment them out by adding a &#8216;#&#8217; at the beginning of the lines.</dl>
<dl>
<dt>
<dd> 4. Run <code>ctdb reloadnodes</code> to force all nodes to reload the nodes file.</dl>
<dl>
<dt>
<dd> 5. Use <code>ctdb status</code> on all nodes and verify that the deleted nodes are no longer listed.</dl>
<h3>reloadips [<i>PNN-LIST</i>]</h3>
<p> This command reloads the public addresses configuration file on the specified nodes. When it completes addresses will be reconfigured and reassigned across the cluster as necessary.</p>
<h3>getdbmap</h3>
<p> This command lists all clustered TDB databases that the CTDB daemon has attached to. Some databases are flagged as PERSISTENT, this means that the database stores data persistently and the data will remain across reboots. One example of such a database is secrets.tdb where information about how the cluster was joined to the domain is stored. </p>
<p> If a PERSISTENT database is not in a healthy state the database is flagged as UNHEALTHY. If there&#8217;s at least one completely healthy node running in the cluster, it&#8217;s possible that the content is restored by a recovery run automaticly. Otherwise an administrator needs to analyze the problem. </p>
<p> See also &quot;ctdb getdbstatus&quot;, &quot;ctdb backupdb&quot;, &quot;ctdb restoredb&quot;, &quot;ctdb dumpbackup&quot;, &quot;ctdb wipedb&quot;, &quot;ctdb setvar AllowUnhealthyDBRead 1&quot; and (if samba or tdb-utils are installed) &quot;tdbtool check&quot;. </p>
<p> Most databases are not persistent and only store the state information that the currently running samba daemons need. These databases are always wiped when ctdb/samba starts and when a node is rebooted. </p>
<p> <font SIZE="+1"> <code>Example</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> </font></p>
<pre>
# ctdb getdbmap
Number of databases:10
dbid:0x435d3410 name:notify.tdb path:/var/lib/ctdb/notify.tdb.0
dbid:0x42fe72c5 name:locking.tdb path:/var/lib/ctdb/locking.tdb.0
dbid:0x1421fb78 name:brlock.tdb path:/var/lib/ctdb/brlock.tdb.0
dbid:0x17055d90 name:connections.tdb path:/var/lib/ctdb/connections.tdb.0
dbid:0xc0bdde6a name:sessionid.tdb path:/var/lib/ctdb/sessionid.tdb.0
dbid:0x122224da name:test.tdb path:/var/lib/ctdb/test.tdb.0
dbid:0x2672a57f name:idmap2.tdb path:/var/lib/ctdb/persistent/idmap2.tdb.0 PERSISTENT
dbid:0xb775fff6 name:secrets.tdb path:/var/lib/ctdb/persistent/secrets.tdb.0 PERSISTENT
dbid:0xe98e08b6 name:group_mapping.tdb path:/var/lib/ctdb/persistent/group_mapping.tdb.0 PERSISTENT
dbid:0x7bbbd26c name:passdb.tdb path:/var/lib/ctdb/persistent/passdb.tdb.0 PERSISTENT
# ctdb getdbmap  # example for unhealthy database
Number of databases:1
dbid:0xb775fff6 name:secrets.tdb path:/var/lib/ctdb/persistent/secrets.tdb.0 PERSISTENT UNHEALTHY
# ctdb -X getdbmap
|ID|Name|Path|Persistent|Unhealthy|
|0x7bbbd26c|passdb.tdb|/var/lib/ctdb/persistent/passdb.tdb.0|1|0|
        
</pre>
</dl>
</dl>
<h3>backupdb <i>DB</i> <i>FILE</i></h3>
<p> Copy the contents of database DB to FILE. FILE can later be read back using <code>restoredb</code>. This is mainly useful for backing up persistent databases such as secrets.tdb and similar.</p>
<h3>restoredb <i>FILE</i> [<i>DB</i>]</h3>
<p> This command restores a persistent database that was previously backed up using backupdb. By default the data will be restored back into the same database as it was created from. By specifying dbname you can restore the data into a different database.</p>
<h3>setdbreadonly <i>DB</i></h3>
<p> This command will enable the read-only record support for a database. This is an experimental feature to improve performance for contended records primarily in locking.tdb and brlock.tdb. When enabling this feature you must set it on all nodes in the cluster.</p>
<h3>setdbsticky <i>DB</i></h3>
<p> This command will enable the sticky record support for the specified database. This is an experimental feature to improve performance for contended records primarily in locking.tdb and brlock.tdb. When enabling this feature you must set it on all nodes in the cluster.</p>
<h2>INTERNAL COMMANDS</h2>
<p> Internal commands are used by CTDB&#8217;s scripts and are not required for managing a CTDB cluster. Their parameters and behaviour are subject to change.</p>
<h3>gettickles <i>IPADDR</i></h3>
<p> Show TCP connections that are registered with CTDB to be &quot;tickled&quot; if there is a failover.</p>
<h3>gratiousarp <i>IPADDR</i> <i>INTERFACE</i></h3>
<p> Send out a gratious ARP for the specified interface through the specified interface. This command is mainly used by the ctdb eventscripts.</p>
<h3>killtcp</h3>
<p> Read a list of TCP connections, one per line, from standard input and terminate each connection. A connection is specified as: </p>
<dl>
<dt>
<dd>
<pre>
        <i>SRC-IPADDR</i>:<i>SRC-PORT</i> <i>DST-IPADDR</i>:<i>DST-PORT</i>
      
</pre>
</dl>
<p> Each connection is terminated by issuing a TCP RST to the SRC-IPADDR:SRC-PORT endpoint. </p>
<p> A single connection can be specified on the command-line rather than on standard input.</p>
<h3>pdelete <i>DB</i> <i>KEY</i></h3>
<p> Delete KEY from DB.</p>
<h3>pfetch <i>DB</i> <i>KEY</i></h3>
<p> Print the value associated with KEY in DB.</p>
<h3>pstore <i>DB</i> <i>KEY</i> <i>FILE</i></h3>
<p> Store KEY in DB with contents of FILE as the associated value.</p>
<h3>ptrans <i>DB</i> [<i>FILE</i>]</h3>
<p> Read a list of key-value pairs, one per line from FILE, and store them in DB using a single transaction. An empty value is equivalent to deleting the given key. </p>
<p> The key and value should be separated by spaces or tabs. Each key/value should be a printable string enclosed in double-quotes.</p>
<h3>runstate [setup|first_recovery|startup|running]</h3>
<p> Print the runstate of the specified node. Runstates are used to serialise important state transitions in CTDB, particularly during startup. </p>
<p> If one or more optional runstate arguments are specified then the node must be in one of these runstates for the command to succeed. </p>
<p> <font SIZE="+1"> <code>Example</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> </font></p>
<pre>
# ctdb runstate
RUNNING
        
</pre>
</dl>
</dl>
<h3>setifacelink <i>IFACE</i> up|down</h3>
<p> Set the internal state of network interface IFACE. This is typically used in the 10.interface script in the &quot;monitor&quot; event. </p>
<p> Example: ctdb setifacelink eth0 up</p>
<h3>tickle <i>SRC-IPADDR</i>:<i>SRC-PORT</i> <i>DST-IPADDR</i>:<i>DST-PORT</i></h3>
<p> Send a TCP tickle to the source host for the specified TCP connection. A TCP tickle is a TCP ACK packet with an invalid sequence and acknowledge number and will when received by the source host result in it sending an immediate correct ACK back to the other end. </p>
<p> TCP tickles are useful to &quot;tickle&quot; clients after a IP failover has occured since this will make the client immediately recognize the TCP connection has been disrupted and that the client will need to reestablish. This greatly speeds up the time it takes for a client to detect and reestablish after an IP failover in the ctdb cluster.</p>
<h3>version</h3>
<p> Display the CTDB version.</p>
<h2>DEBUGGING COMMANDS</h2>
<p> These commands are primarily used for CTDB development and testing and should not be used for normal administration.</p>
<h3>OPTIONS</h3>
<p> &#8211;print-emptyrecords</p>
<dl>
<dt>
<dd> This enables printing of empty records when dumping databases with the catdb, cattbd and dumpdbbackup commands. Records with empty data segment are considered deleted by ctdb and cleaned by the vacuuming mechanism, so this switch can come in handy for debugging the vacuuming behaviour.</dl>
<p> &#8211;print-datasize</p>
<dl>
<dt>
<dd> This lets database dumps (catdb, cattdb, dumpdbbackup) print the size of the record data instead of dumping the data contents.</dl>
<p> &#8211;print-lmaster</p>
<dl>
<dt>
<dd> This lets catdb print the lmaster for each record.</dl>
<p> &#8211;print-hash</p>
<dl>
<dt>
<dd> This lets database dumps (catdb, cattdb, dumpdbbackup) print the hash for each record.</dl>
<p> &#8211;print-recordflags</p>
<dl>
<dt>
<dd> This lets catdb and dumpdbbackup print the record flags for each record. Note that cattdb always prints the flags.</dl>
<h3>process-exists <i>PID</i></h3>
<p> This command checks if a specific process exists on the CTDB host. This is mainly used by Samba to check if remote instances of samba are still running or not.</p>
<h3>getdbstatus <i>DB</i></h3>
<p> This command displays more details about a database. </p>
<p> <font SIZE="+1"> <code>Example</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> </font></p>
<pre>
# ctdb getdbstatus test.tdb.0
dbid: 0x122224da
name: test.tdb
path: /var/lib/ctdb/test.tdb.0
PERSISTENT: no
HEALTH: OK
# ctdb getdbstatus registry.tdb  # with a corrupted TDB
dbid: 0xf2a58948
name: registry.tdb
path: /var/lib/ctdb/persistent/registry.tdb.0
PERSISTENT: yes
HEALTH: NO-HEALTHY-NODES - ERROR - Backup of corrupted TDB in '/var/lib/ctdb/persistent/registry.tdb.0.corrupted.20091208091949.0Z'
        
</pre>
</dl>
</dl>
<h3>catdb <i>DB</i></h3>
<p> Print a dump of the clustered TDB database DB.</p>
<h3>cattdb <i>DB</i></h3>
<p> Print a dump of the contents of the local TDB database DB.</p>
<h3>dumpdbbackup <i>FILE</i></h3>
<p> Print a dump of the contents from database backup FILE, similar to <code>catdb</code>.</p>
<h3>wipedb <i>DB</i></h3>
<p> Remove all contents of database DB.</p>
<h3>recover</h3>
<p> This command will trigger the recovery daemon to do a cluster recovery.</p>
<h3>ipreallocate, sync</h3>
<p> This command will force the recovery master to perform a full ip reallocation process and redistribute all ip addresses. This is useful to &quot;reset&quot; the allocations back to its default state if they have been changed using the &quot;moveip&quot; command. While a &quot;recover&quot; will also perform this reallocation, a recovery is much more hevyweight since it will also rebuild all the databases.</p>
<h3>getmonmode</h3>
<p> This command returns the monutoring mode of a node. The monitoring mode is either ACTIVE or DISABLED. Normally a node will continuously monitor that all other nodes that are expected are in fact connected and that they respond to commands. </p>
<p> ACTIVE &#8211; This is the normal mode. The node is actively monitoring all other nodes, both that the transport is connected and also that the node responds to commands. If a node becomes unavailable, it will be marked as DISCONNECTED and a recovery is initiated to restore the cluster. </p>
<p> DISABLED &#8211; This node is not monitoring that other nodes are available. In this mode a node failure will not be detected and no recovery will be performed. This mode is useful when for debugging purposes one wants to attach GDB to a ctdb process but wants to prevent the rest of the cluster from marking this node as DISCONNECTED and do a recovery.</p>
<h3>setmonmode 0|1</h3>
<p> This command can be used to explicitly disable/enable monitoring mode on a node. The main purpose is if one wants to attach GDB to a running ctdb daemon but wants to prevent the other nodes from marking it as DISCONNECTED and issuing a recovery. To do this, set monitoring mode to 0 on all nodes before attaching with GDB. Remember to set monitoring mode back to 1 afterwards.</p>
<h3>attach <i>DBNAME</i> [persistent]</h3>
<p> Create a new CTDB database called DBNAME and attach to it on all nodes.</p>
<h3>detach <i>DB-LIST</i></h3>
<p> Detach specified non-persistent database(s) from the cluster. This command will disconnect specified database(s) on all nodes in the cluster. This command should only be used when none of the specified database(s) are in use. </p>
<p> All nodes should be active and tunable AllowClientDBAccess should be disabled on all nodes before detaching databases.</p>
<h3>dumpmemory</h3>
<p> This is a debugging command. This command will make the ctdb daemon to write a fill memory allocation map to standard output.</p>
<h3>rddumpmemory</h3>
<p> This is a debugging command. This command will dump the talloc memory allocation tree for the recovery daemon to standard output.</p>
<h3>thaw</h3>
<p> Thaw a previously frozen node.</p>
<h3>eventscript <i>ARGUMENTS</i></h3>
<p> This is a debugging command. This command can be used to manually invoke and run the eventscritps with arbitrary arguments.</p>
<h3>ban <i>BANTIME</i></h3>
<p> Administratively ban a node for BANTIME seconds. The node will be unbanned after BANTIME seconds have elapsed. </p>
<p> A banned node does not participate in the cluster. It does not host any records for the clustered TDB and does not host any public IP addresses. </p>
<p> Nodes are automatically banned if they misbehave. For example, a node may be banned if it causes too many cluster recoveries. </p>
<p> To administratively exclude a node from a cluster use the <code>stop</code> command.</p>
<h3>unban</h3>
<p> This command is used to unban a node that has either been administratively banned using the ban command or has been automatically banned.</p>
<h3>rebalancenode [<i>PNN-LIST</i>]</h3>
<p> This command marks the given nodes as rebalance targets in the LCP2 IP allocation algorithm. The <code>reloadips</code> command will do this as necessary so this command should not be needed.</p>
<h3>check_srvids <i>SRVID</i> &#8230;</h3>
<p> This command checks whether a set of srvid message ports are registered on the node or not. The command takes a list of values to check. </p>
<p> <font SIZE="+1"> <code>Example</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> </font></p>
<pre>
# ctdb check_srvids 1 2 3 14765
Server id 0:1 does not exist
Server id 0:2 does not exist
Server id 0:3 does not exist
Server id 0:14765 exists
        
</pre>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ctdbd/">ctdbd</a></code>(1), <code><a href="/docs/linux/man/1-onnode/">onnode</a></code>(1), <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7), <code><a href="/docs/linux/man/7-ctdb-statistics/">ctdb-statistics</a></code>(7), <code><a href="/docs/linux/man/7-ctdb-tunables/">ctdb-tunables</a></code>(7), m[blue]<code><a rel="nofollow" href="http://ctdb.samba.org/">http://ctdb.samba.org/</a></code>m[]</p>
<h2>AUTHOR</h2>
<p> This documentation was written by Ronnie Sahlberg, Amitay Isaacs, Martin Schwenke</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2007 Andrew Tridgell, Ronnie Sahlberg </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, see m[blue]<code><a rel="nofollow" href="http://www.gnu.org/licenses">http://www.gnu.org/licenses</a></code>m[]. </p>
<h2>Index</h2>
<dt><a href="#lbCA">INTERNAL COMMANDS</a></p>
<dd>
<dt><a href="#lbCM">DEBUGGING COMMANDS</a></p>
<dd>
<dt><a href="#lbDI">SEE ALSO</a></p>
<dd>
<dt><a href="#lbDJ">AUTHOR</a></p>
<dd>
<dt><a href="#lbDK">COPYRIGHT</a></p>
<dd></dl>
