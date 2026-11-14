---
title: "ctdbd-conf(5)"
name: "ctdbd-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-ctdbd-conf/"
description: "ctdbd.conf – CTDB daemon configuration file"
---

<p>ctdbd.conf &#8211; CTDB daemon configuration file</p>
<h2>Description</h2>
<p>This file contains CTDB configuration variables that are affect the operation of CTDB. The default location of this file is /etc/ctdb/ctdbd.conf. </p>
<p> This file is a shell script (see <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1)) but is usually limited to simple variable assignments and shell-style comments. </p>
<p> CTDB configuration variables are grouped into several categories below. </p>
<p> Variables defined in this document can also be set in a distribution-specific configuration file such as /etc/sysconfig/ctdb (Red Hat) or /etc/default/ctdb (Debian). However, these files should be reserved for variables used by the initscript. A historical alternative is /etc/ctdb/sysconfig/ctdb &#8211; this is deprecated.</p>
<h2>Initscript Configuration</h2>
<p>Some options must be available to the initscript so they need to be set in the distribution-specific initscript configuration, such as /etc/sysconfig/ctdb or /etc/default/ctdb. </p>
<p> CTDB_PIDFILE=<i>FILENAME</i></p>
<dl>
<dd>FILENAME is the name of the file used to contain the process ID (PID) of the main CTDB daemon when it is running. This is passed from the initscript to <code><a href="/docs/linux/man/1-ctdbd_wrapper/">ctdbd_wrapper</a></code>(1). </p>
<p> Default is /var/run/ctdb/ctdbd.pid. Corresponds to <code>&#8211;pidfile</code>.</dl>
<h2>Global Configuration</h2>
<p>These options may be used in the initscripts, daemon and scripts. </p>
<p> CTDB_BASE=<i>DIRECTORY</i></p>
<dl>
<dd>DIRECTORY containing CTDB scripts and configuration files.</dl>
<h2>Daemon Configuration</h2>
<p>Variables in this section are processed by <code><a href="/docs/linux/man/1-ctdbd_wrapper/">ctdbd_wrapper</a></code>(1) and are converted into command-line arguments to <code><a href="/docs/linux/man/1-ctdbd/">ctdbd</a></code>(1). Correspondence with <code><a href="/docs/linux/man/1-ctdbd/">ctdbd</a></code>(1) options is shown for each variable. The the documentation for the relevant options for more details. </p>
<p> Many of these variables are also used by event scripts. </p>
<p> CTDB_CAPABILITY_LMASTER=yes|no</p>
<dl>
<dd>Defaults to yes. Corresponds to <code>&#8211;no-lmaster</code>.</dl>
<p> CTDB_CAPABILITY_RECMASTER=yes|no</p>
<dl>
<dd>Defaults to yes. Corresponds to <code>&#8211;no-recmaster</code>.</dl>
<p> CTDB_DBDIR=<i>DIRECTORY</i></p>
<dl>
<dd>Defaults to /var/lib/ctdb. </p>
<p> Apart from a DIRECTORY, this can take a special value of the form <code>tmpfs</code>[:<i>OPTIONS</i>]. OPTIONS is a comma-separated list of any permissible options to the tmpfs filesystem. The only pre-specified default is <code>mode=700</code>, which can overriden by specifying <code>mode</code> in OPTIONS. It probably makes sense to specify a maximum <code>size</code>. </p>
<p> Corresponds to <code>&#8211;dbdir</code>.</dl>
<p> CTDB_DBDIR_PERSISTENT=<i>DIRECTORY</i></p>
<dl>
<dd>Defaults to /var/lib/ctdb/persistent. </p>
<p> Corresponds to <code>&#8211;dbdir-persistent</code>.</dl>
<p> CTDB_DBDIR_STATE=<i>DIRECTORY</i></p>
<dl>
<dd>Defaults to /var/lib/ctdb/state. </p>
<p> Corresponds to <code>&#8211;dbdir-state</code>.</dl>
<p> CTDB_DEBUGLEVEL=<i>DEBUGLEVEL</i></p>
<dl>
<dd>Default is NOTICE (2). Corresponds to <code>-d</code> or <code>&#8211;debug</code>.</dl>
<p> CTDB_EVENT_SCRIPT_DIR=<i>DIRECTORY</i></p>
<dl>
<dd>Default is <i>CTDB_BASE</i>/events.d, so usually /etc/ctdb/events.d. Corresponds to <code>&#8211;event-script-dir</code>.</dl>
<p> CTDB_LOGGING=<i>STRING</i></p>
<dl>
<dd>STRING specifies where ctdbd will write its log. The default is file:/var/log/log.ctdb. Corresponds to <code>&#8211;logging</code>. </p>
<p> Valid values are: </p>
<p> file:<i>FILENAME</i></p>
<dl>
<dd>FILENAME where ctdbd will write its log. This is usually /var/log/log.ctdb.</dl>
<p> syslog[:<i>METHOD</i>]</p>
<dl>
<dd>CTDB will log to syslog. By default this will use the <a href="/docs/linux/man/3-syslog/">syslog</a>(3) API. </p>
<p> If METHOD is specified then it specifies an extension that causes logging to be done in a non-blocking fashion. This can be useful under heavy loads that might cause the syslog daemon to dequeue messages too slowly, which would otherwise cause CTDB to block when logging. METHOD must be one of: </p>
<p> nonblocking</p>
<dl>
<dd>CTDB will log to syslog via /dev/log in non-blocking mode.</dl>
<p> udp</p>
<dl>
<dd>CTDB will log to syslog via UDP to localhost:514. The syslog daemon must be configured to listen on (at least) localhost:514. Most implementations will log the messages against hostname &quot;localhost&quot; &#8211; this is a limit of the implementation for compatibility with more syslog daemon implementations.</dl>
<p> udp-rfc5424</p>
<dl>
<dd>As with &quot;udp&quot; but messages are sent in RFC5424 format. This method will log the correct hostname but is not as widely implemented in syslog daemons.</dl>
</dl>
</dl>
<p> CTDB_LVS_PUBLIC_IP=<i>IPADDR</i></p>
<dl>
<dd>No default. Corresponds to &quot;<code>&#8211;lvs</code><code>&#8211;single-public-ip IPADDR&quot;</code>.</dl>
<p> CTDB_NODES=<i>FILENAME</i></p>
<dl>
<dd>Default is <i>CTDB_BASE</i>/nodes, so usually /etc/ctdb/nodes. Corresponds to <code>&#8211;nlist</code>.</dl>
<p> CTDB_NOTIFY_SCRIPT=<i>FILENAME</i></p>
<dl>
<dd>No default, usually /etc/ctdb/notify.sh. Corresponds to <code>&#8211;notification-script</code>.</dl>
<p> CTDB_MAX_PERSISTENT_CHECK_ERRORS=<i>NUM</i></p>
<dl>
<dd>Default 0. Corresponds to <code>&#8211;max-persistent-check-errors</code>.</dl>
<p> CTDB_NODE_ADDRESS=<i>IPADDR</i></p>
<dl>
<dd>IPADDR is the private IP address that ctdbd will bind to. Corresponds to <code>&#8211;listen</code>. </p>
<p> By default ctdbd will select the first address from the nodes list that in can bind to. See also CTDB_NODES. </p>
<p> This option is only required when automatic address detection can not be used. This can be the case when running multiple ctdbd daemons/nodes on the same physical host (usually for testing), using InfiniBand for the private network or on Linux when sysctl net.ipv4.ip_nonlocal_bind=1.</dl>
<p> CTDB_PUBLIC_ADDRESSES=<i>FILENAME</i></p>
<dl>
<dd>No default, usually /etc/ctdb/public_addresses. Corresponds to <code>&#8211;public-addresses</code>.</dl>
<p> CTDB_PUBLIC_INTERFACE=<i>INTERFACE</i></p>
<dl>
<dd>No default. Corresponds to <code>&#8211;public-interface</code>.</dl>
<p> CTDB_RECOVERY_LOCK=<i>FILENAME</i></p>
<dl>
<dd>Defaults to /some/place/on/shared/storage, which should be change to a useful value. Corresponds to <code>&#8211;reclock</code>. </p>
<p> For information about the recovery lock please see the RECOVERY LOCK section in <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7).</dl>
<p> CTDB_SCRIPT_LOG_LEVEL=<i>DEBUGLEVEL</i></p>
<dl>
<dd>Defaults to ERR (0). Corresponds to <code>&#8211;script-log-level</code>.</dl>
<p> CTDB_SOCKET=<i>FILENAME</i></p>
<dl>
<dd>Defaults to /var/run/ctdb/ctdbd.socket. Corresponds to <code>&#8211;socket</code>. </p>
<p> If you change this then you probably want to set this in root&#8217;s environment (perhaps in a file in /etc/profile.d) so that you can use the <code><a href="/docs/linux/man/1-ctdb/">ctdb</a></code>(1) command in a straightforward manner.</dl>
<p> CTDB_START_AS_DISABLED=yes|no</p>
<dl>
<dd>Default is no. Corresponds to <code>&#8211;start-as-disabled</code>.</dl>
<p> CTDB_START_AS_STOPPED=yes|no</p>
<dl>
<dd>Default is no. Corresponds to <code>&#8211;start-as-stopped</code>.</dl>
<p> CTDB_TRANSPORT=tcp|infiniband</p>
<dl>
<dd>Defaults to tcp. Corresponds to <code>&#8211;transport</code>.</dl>
<p> While the following variables do not translate into daemon options they are used by <code><a href="/docs/linux/man/1-ctdbd_wrapper/">ctdbd_wrapper</a></code>(1) when starting and stopping <code><a href="/docs/linux/man/1-ctdbd/">ctdbd</a></code>(1). </p>
<p> CTDB_SHUTDOWN_TIMEOUT=<i>NUM</i></p>
<dl>
<dd>NUM is the number of seconds to wait for <code><a href="/docs/linux/man/1-ctdbd/">ctdbd</a></code>(1) to shut down gracefully before giving up and killing it. </p>
<p> Defaults is 30.</dl>
<p> CTDB_STARTUP_TIMEOUT=<i>NUM</i></p>
<dl>
<dd>NUM is the number of seconds to wait for <code><a href="/docs/linux/man/1-ctdbd/">ctdbd</a></code>(1) complete early initialisation up to a point where it is unlikely to abort. If <code>ctdbd</code> doesn&#8217;t complete the &quot;setup&quot; event before this timeout then it is killed. </p>
<p> Defaults is 10.</dl>
<h2>Network Configuration</h2>
<h3>Nat Gateway</h3>
<p>NAT gateway is used to configure fallback routing for nodes when they do not host any public IP addresses. For example, it allows unhealthy nodes to reliably communicate with external infrastructure. One node in a NAT gateway group will be designated as the NAT gateway master node and other (slave) nodes will be configured with fallback routes via the NAT gateway master node. For more information, see the NAT GATEWAY section in <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7). </p>
<p> CTDB_NATGW_DEFAULT_GATEWAY=<i>IPADDR</i></p>
<dl>
<dd>IPADDR is an alternate network gateway to use on the NAT gateway master node. If set, a fallback default route is added via this network gateway. </p>
<p> No default. Setting this variable is optional &#8211; if not set that no route is created on the NAT gateway master node.</dl>
<p> CTDB_NATGW_NODES=<i>FILENAME</i></p>
<dl>
<dd>FILENAME contains the list of nodes that belong to the same NAT gateway group. </p>
<p> File format: </p>
<dl>
<dd>
<pre><i>IPADDR</i> [slave-only]</pre>
</dl>
<p> IPADDR is the private IP address of each node in the NAT gateway group. </p>
<p> If &quot;slave-only&quot; is specified then the corresponding node can not be the NAT gateway master node. In this case <i>CTDB_NATGW_PUBLIC_IFACE</i> and <i>CTDB_NATGW_PUBLIC_IP</i> are optional and unused. </p>
<p> No default, usually /etc/ctdb/natgw_nodes when enabled.</dl>
<p> CTDB_NATGW_PRIVATE_NETWORK=<i>IPADDR/MASK</i></p>
<dl>
<dd>IPADDR/MASK is the private sub-network that is internally routed via the NAT gateway master node. This is usually the private network that is used for node addresses. </p>
<p> No default.</dl>
<p> CTDB_NATGW_PUBLIC_IFACE=<i>IFACE</i></p>
<dl>
<dd>IFACE is the network interface on which the CTDB_NATGW_PUBLIC_IP will be configured. </p>
<p> No default.</dl>
<p> CTDB_NATGW_PUBLIC_IP=<i>IPADDR/MASK</i></p>
<dl>
<dd>IPADDR/MASK indicates the IP address that is used for outgoing traffic (originating from CTDB_NATGW_PRIVATE_NETWORK) on the NAT gateway master node. This <i>must not</i> be a configured public IP address. </p>
<p> No default.</dl>
<p> CTDB_NATGW_STATIC_ROUTES=<i>IPADDR/MASK[@GATEWAY]</i> &#8230;</p>
<dl>
<dd>Each IPADDR/MASK identifies a network or host to which NATGW should create a fallback route, instead of creating a single default route. This can be used when there is already a default route, via an interface that can not reach required infrastructure, that overrides the NAT gateway default route. </p>
<p> If GATEWAY is specified then the corresponding route on the NATGW master node will be via GATEWAY. Such routes are created even if <i>CTDB_NATGW_DEFAULT_GATEWAY</i> is not specified. If GATEWAY is not specified for some networks then routes are only created on the NATGW master node for those networks if <i>CTDB_NATGW_DEFAULT_GATEWAY</i> is specified. </p>
<p> This should be used with care to avoid causing traffic to unnecessarily double-hop through the NAT gateway master, even when a node is hosting public IP addresses. Each specified network or host should probably have a corresponding automatically created link route or static route to avoid this. </p>
<p> No default.</dl>
<p> <font SIZE="+1"> <code>Example</code></p>
<dl>
<dd>
<dl>
<dd></font></p>
<pre>CTDB_NATGW_NODES=/etc/ctdb/natgw_nodes
CTDB_NATGW_PRIVATE_NETWORK=192.168.1.0/24
CTDB_NATGW_DEFAULT_GATEWAY=10.0.0.1
CTDB_NATGW_PUBLIC_IP=10.0.0.227/24
CTDB_NATGW_PUBLIC_IFACE=eth0</pre>
</dl>
<p> A variation that ensures that infrastructure (ADS, DNS, &#8230;) directly attached to the public network (10.0.0.0/24) is always reachable would look like this: </p>
<dl>
<dd>
<pre>CTDB_NATGW_NODES=/etc/ctdb/natgw_nodes
CTDB_NATGW_PRIVATE_NETWORK=192.168.1.0/24
CTDB_NATGW_PUBLIC_IP=10.0.0.227/24
CTDB_NATGW_PUBLIC_IFACE=eth0
CTDB_NATGW_STATIC_ROUTES=10.0.0.0/24</pre>
</dl>
<p> Note that <i>CTDB_NATGW_DEFAULT_GATEWAY</i> is not specified.</dl>
<h3>Policy Routing</h3>
<p>A node running CTDB may be a component of a complex network topology. In particular, public addresses may be spread across several different networks (or VLANs) and it may not be possible to route packets from these public addresses via the system&#8217;s default route. Therefore, CTDB has support for policy routing via the 13.per_ip_routing eventscript. This allows routing to be specified for packets sourced from each public address. The routes are added and removed as CTDB moves public addresses between nodes. </p>
<p> For more information, see the POLICY ROUTING section in <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7). </p>
<p> CTDB_PER_IP_ROUTING_CONF=<i>FILENAME</i></p>
<dl>
<dd>FILENAME contains elements for constructing the desired routes for each source address. </p>
<p> The special FILENAME value <code>__auto_link_local__</code> indicates that no configuration file is provided and that CTDB should generate reasonable link-local routes for each public IP address. </p>
<p> File format: </p>
<dl>
<dd>
<pre><i>IPADDR</i> <i>DEST-IPADDR/MASK</i> [<i>GATEWAY-IPADDR</i>]</pre>
</dl>
<p> No default, usually /etc/ctdb/policy_routing when enabled.</dl>
<p> CTDB_PER_IP_ROUTING_RULE_PREF=<i>NUM</i></p>
<dl>
<dd>NUM sets the priority (or preference) for the routing rules that are added by CTDB. </p>
<p> This should be (strictly) greater than 0 and (strictly) less than 32766. A priority of 100 is recommended, unless this conflicts with a priority already in use on the system. See <code><a href="/docs/linux/man/8-ip/">ip</a></code>(8), for more details.</dl>
<p> CTDB_PER_IP_ROUTING_TABLE_ID_LOW=<i>LOW-NUM</i>, CTDB_PER_IP_ROUTING_TABLE_ID_HIGH=<i>HIGH-NUM</i></p>
<dl>
<dd>CTDB determines a unique routing table number to use for the routing related to each public address. LOW-NUM and HIGH-NUM indicate the minimum and maximum routing table numbers that are used. </p>
<p> <code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) uses some reserved routing table numbers below 255. Therefore, CTDB_PER_IP_ROUTING_TABLE_ID_LOW should be (strictly) greater than 255. </p>
<p> CTDB uses the standard file /etc/iproute2/rt_tables to maintain a mapping between the routing table numbers and labels. The label for a public address <i>ADDR</i> will look like ctdb.<i>addr</i>. This means that the associated rules and routes are easy to read (and manipulate). </p>
<p> No default, usually 1000 and 9000.</dl>
<p> <font SIZE="+1"> <code>Example</code></p>
<dl>
<dd>
<dl>
<dd></font></p>
<pre>CTDB_PER_IP_ROUTING_CONF=/etc/ctdb/policy_routing
CTDB_PER_IP_ROUTING_RULE_PREF=100
CTDB_PER_IP_ROUTING_TABLE_ID_LOW=1000
CTDB_PER_IP_ROUTING_TABLE_ID_HIGH=9000</pre>
</dl>
</dl>
<h3>Miscellaneous Network Configuration</h3>
<p>CTDB_PARTIALLY_ONLINE_INTERFACES=yes|no</p>
<dl>
<dd>Whether one or more offline interfaces should cause a monitor event to fail if there are other interfaces that are up. If this is &quot;yes&quot; and a node has some interfaces that are down then <code>ctdb status</code> will display the node as &quot;PARTIALLYONLINE&quot;. </p>
<p> Note that CTDB_PARTIALLY_ONLINE_INTERFACES=yes is incompatible with NAT gateway, since NAT gateway relies on the interface configured by CTDB_NATGW_PUBLIC_IFACE to be up. </p>
<p> Default is &quot;no&quot;.</dl>
<h2>Service Configuration</h2>
<p>CTDB can be configured to manage and/or monitor various NAS (and other) services via its eventscripts. </p>
<p> In the simplest case CTDB will manage a service. This means the service will be started and stopped along with CTDB, CTDB will monitor the service and CTDB will do any required reconfiguration of the service when public IP addresses are failed over.</p>
<h3>Samba</h3>
<p><font SIZE="+1"> <code>Eventscripts</code></p>
<dl>
<dd>
<dl>
<dd>49.winbind</dl>
<dl>
<dd>50.samba</dl>
</dl>
<p> CTDB_MANAGES_SAMBA=yes|no</p>
<dl>
<dd>Should CTDB manage Samba? </p>
<p> Default is no.</dl>
<p> CTDB_MANAGES_WINBIND=yes|no</p>
<dl>
<dd>Should CTDB manage Winbind? </p>
<p> Default is no.</dl>
<p> CTDB_SAMBA_CHECK_PORTS=<i>PORT-LIST</i></p>
<dl>
<dd>When monitoring Samba, check TCP ports in space-separated PORT-LIST. </p>
<p> Default is to monitor ports that Samba is configured to listen on.</dl>
<p> CTDB_SAMBA_SKIP_SHARE_CHECK=yes|no</p>
<dl>
<dd>As part of monitoring, should CTDB skip the check for the existence of each directory configured as share in Samba. This may be desirable if there is a large number of shares. </p>
<p> Default is no.</dl>
<p> CTDB_SERVICE_NMB=<i>SERVICE</i></p>
<dl>
<dd>Distribution specific SERVICE for managing nmbd. </p>
<p> Default is distribution-dependant.</dl>
<p> CTDB_SERVICE_SMB=<i>SERVICE</i></p>
<dl>
<dd>Distribution specific SERVICE for managing smbd. </p>
<p> Default is distribution-dependant.</dl>
<p> CTDB_SERVICE_WINBIND=<i>SERVICE</i></p>
<dl>
<dd>Distribution specific SERVICE for managing winbindd. </p>
<p> Default is &quot;winbind&quot;.</dl>
<p> </font></p>
<h3>Nfs</h3>
<p>This includes parameters for the kernel NFS server. Alternative NFS subsystems (such as m[blue]<code>NFS-Ganesha</code>m[]<font SIZE="-2">[1]</font>) can be integrated using <i>CTDB_NFS_CALLOUT</i>. </p>
<p> <font SIZE="+1"> <code>Eventscript</code></p>
<dl>
<dd>
<dl>
<dd>60.nfs</dl>
</dl>
<p> CTDB_CLUSTER_FILESYSTEM_TYPE=gpfs</p>
<dl>
<dd>The type of cluster filesystem to use with NFS-ganesha. Currently only &quot;gpfs&quot; is supported. </p>
<p> Default is &quot;gpfs&quot;.</dl>
<p> CTDB_MANAGES_NFS=yes|no</p>
<dl>
<dd>Should CTDB manage NFS? </p>
<p> Default is no.</dl>
<p> CTDB_NFS_CALLOUT=<i>COMMAND</i></p>
<dl>
<dd>COMMAND specifies the path to a callout to handle interactions with the configured NFS system, including startup, shutdown, monitoring. </p>
<p> Default is the included <code>nfs-linux-kernel-callout</code>.</dl>
<p> CTDB_NFS_SKIP_SHARE_CHECK=yes|no</p>
<dl>
<dd>As part of monitoring, should CTDB skip the check for the existence of each directory exported via NFS. This may be desirable if there is a large number of exports. </p>
<p> Default is no.</dl>
<p> CTDB_RPCINFO_LOCALHOST=<i>IPADDR</i>|<i>HOSTNAME</i></p>
<dl>
<dd>IPADDR or HOSTNAME indicates the address that <code>rpcinfo</code> should connect to when doing <code>rpcinfo</code> check on IPv4 RPC service during monitoring. Optimally this would be &quot;localhost&quot;. However, this can add some performance overheads. </p>
<p> Default is &quot;127.0.0.1&quot;.</dl>
<p> CTDB_RPCINFO_LOCALHOST6=<i>IPADDR</i>|<i>HOSTNAME</i></p>
<dl>
<dd>IPADDR or HOSTNAME indicates the address that <code>rpcinfo</code> should connect to when doing <code>rpcinfo</code> check on IPv6 RPC service during monitoring. Optimally this would be &quot;localhost6&quot; (or similar). However, this can add some performance overheads. </p>
<p> Default is &quot;::1&quot;.</dl>
<p> </font></p>
<h3>Apache Httpd</h3>
<p>CTDB can manage the Apache web server. </p>
<p> <font SIZE="+1"> <code>Eventscript</code></p>
<dl>
<dd>
<dl>
<dd>41.httpd</dl>
</dl>
<p> CTDB_MANAGES_HTTPD=yes|no</p>
<dl>
<dd>Should CTDB manage the Apache web server? </p>
<p> Default is no.</dl>
<p> </font></p>
<h3>Clamav</h3>
<p>CTDB has support to manage the popular anti-virus daemon ClamAV. </p>
<p> <font SIZE="+1"> <code>Eventscript</code></p>
<dl>
<dd>
<dl>
<dd>31.clamd</dl>
<p> This eventscript is not enabled by default. Use <code>ctdb enablescript</code> to enable it.</dl>
<p> CTDB_MANAGES_CLAMD=yes|no</p>
<dl>
<dd>Should CTDB manage ClamAV? </p>
<p> Default is no.</dl>
<p> CTDB_CLAMD_SOCKET=<i>FILENAME</i></p>
<dl>
<dd>FILENAME is the socket to monitor ClamAV. </p>
<p> No default.</dl>
<p> </font></p>
<h3>Iscsi</h3>
<p>CTDB has support for managing the Linux iSCSI tgtd service. </p>
<p> <font SIZE="+1"> <code>Eventscript</code></p>
<dl>
<dd>
<dl>
<dd>70.iscsi</dl>
</dl>
<p> CTDB_MANAGES_ISCSI=yes|no</p>
<dl>
<dd>Should CTDB manage iSCSI tgtd? </p>
<p> Default is no.</dl>
<p> CTDB_START_ISCSI_SCRIPTS=<i>DIRECTORY</i></p>
<dl>
<dd>DIRECTORY on shared storage containing scripts to start tgtd for each public IP address. </p>
<p> No default.</dl>
<p> </font></p>
<h3>Multipathd</h3>
<p>CTDB can monitor multipath devices to ensure that active paths are available. </p>
<p> <font SIZE="+1"> <code>Eventscript</code></p>
<dl>
<dd>
<dl>
<dd>20.multipathd</dl>
<p> This eventscript is not enabled by default. Use <code>ctdb enablescript</code> to enable it.</dl>
<p> CTDB_MONITOR_MPDEVICES=<i>MP-DEVICE-LIST</i></p>
<dl>
<dd>MP-DEVICE-LIST is a list of multipath devices for CTDB to monitor? </p>
<p> No default.</dl>
<p> </font></p>
<h3>Vsftpd</h3>
<p>CTDB can manage the vsftpd FTP server. </p>
<p> <font SIZE="+1"> <code>Eventscript</code></p>
<dl>
<dd>
<dl>
<dd>40.vsftpd</dl>
</dl>
<p> CTDB_MANAGES_VSFTPD=yes|no</p>
<dl>
<dd>Should CTDB manage the vsftpd FTP server? </p>
<p> Default is no.</dl>
<p> </font></p>
<h3>System Resource Monitoring Configuration</h3>
<p>CTDB can experience seemingly random (performance and other) issues if system resources become too constrained. Options in this section can be enabled to allow certain system resources to be checked. They allows warnings to be logged and nodes to be marked unhealthy when system resource usage reaches the configured thresholds. </p>
<p> Some checks are enabled by default. It is recommended that these checks remain enabled or are augmented by extra checks. There is no supported way of completely disabling the checks. </p>
<p> <font SIZE="+1"> <code>Eventscripts</code></p>
<dl>
<dd>
<dl>
<dd>05.system</dl>
<p> Filesystem and memory usage monitoring is in 05.system.</dl>
<p> CTDB_MONITOR_FILESYSTEM_USAGE=<i>FS-LIMIT-LIST</i></p>
<dl>
<dd>FS-LIMIT-LIST is a space-separated list of <i>FILESYSTEM</i>:<i>WARN_LIMIT</i>[:<i>UNHEALTHY_LIMIT</i>] triples indicating that warnings should be logged if the space used on FILESYSTEM reaches WARN_LIMIT%. If usage reaches UNHEALTHY_LIMIT then the node should be flagged unhealthy. Either WARN_LIMIT or UNHEALTHY_LIMIT may be left blank, meaning that check will be omitted. </p>
<p> Default is to warn for each filesystem containing a database directory (<code>CTDB_DBDIR</code>, <code>CTDB_DBDIR_PERSISTENT</code>, <code>CTDB_DBDIR_STATE</code>) with a threshold of 90%.</dl>
<p> CTDB_MONITOR_MEMORY_USAGE=<i>MEM-LIMITS</i></p>
<dl>
<dd>MEM-LIMITS takes the form <i>WARN_LIMIT</i>[:<i>UNHEALTHY_LIMIT</i>] indicating that warnings should be logged if memory usage reaches WARN_LIMIT%. If usage reaches UNHEALTHY_LIMIT then the node should be flagged unhealthy. Either WARN_LIMIT or UNHEALTHY_LIMIT may be left blank, meaning that check will be omitted. </p>
<p> Default is 80, so warnings will be logged when memory usage reaches 80%.</dl>
<p> CTDB_MONITOR_SWAP_USAGE=<i>SWAP-LIMITS</i></p>
<dl>
<dd>SWAP-LIMITS takes the form <i>WARN_LIMIT</i>[:<i>UNHEALTHY_LIMIT</i>] indicating that warnings should be logged if swap usage reaches WARN_LIMIT%. If usage reaches UNHEALTHY_LIMIT then the node should be flagged unhealthy. Either WARN_LIMIT or UNHEALTHY_LIMIT may be left blank, meaning that check will be omitted. </p>
<p> Default is 25, so warnings will be logged when swap usage reaches 25%.</dl>
<p> </font></p>
<h3>Miscellaneous Service-Related Configuration</h3>
<p>CTDB_MANAGED_SERVICES=<i>SERVICE-LIST</i></p>
<dl>
<dd>SERVICE-LIST is a space-separated list of SERVICEs that CTDB should manage. This can be used as an alternative to the <i>CTDB_MANAGES_</i><i>SERVICE</i> variables. </p>
<p> No default.</dl>
<p> CTDB_SERVICE_AUTOSTARTSTOP=yes|no</p>
<dl>
<dd>When CTDB should start and stop services if they become managed or unmanaged. </p>
<p> Default is no.</dl>
<h2>Tunables Configuration</h2>
<p>CTDB tunables (see <code><a href="/docs/linux/man/7-ctdbd-tunables/">ctdbd-tunables</a></code>(7)) can be set from the configuration file. They are set as follows: </p>
<dl>
<dd>
<pre>CTDB_SET_<i>TUNABLE</i>=<i>VALUE</i></pre>
</dl>
<p> For example: </p>
<dl>
<dd>
<pre>CTDB_SET_MonitorInterval=20</pre>
</dl>
<h2>Debug And Test</h2>
<p>Variable in this section are for debugging and testing CTDB. They should not generally be needed. </p>
<p> CTDB_DEBUG_HUNG_SCRIPT=<i>FILENAME</i></p>
<dl>
<dd>FILENAME is a script to run to log debug information when an event script times out. </p>
<p> Default is <i>CTDB_BASE</i>/debug-hung-script.sh.</dl>
<p> CTDB_DEBUG_HUNG_SCRIPT_LOGFILE=<i>FILENAME</i></p>
<dl>
<dd>FILENAME specifies where log messages should go when debugging hung eventscripts. This is a testing option. See also CTDB_DEBUG_HUNG_SCRIPT. </p>
<p> No default. Messages go to stdout/stderr and are logged to the same place as other CTDB log messages.</dl>
<p> CTDB_DEBUG_HUNG_SCRIPT_STACKPAT=<i>REGEXP</i></p>
<dl>
<dd>REGEXP specifies interesting processes for which stack traces should be logged when debugging hung eventscripts and those processes are matched in pstree output. REGEXP is an extended regexp so choices are separated by pipes (&#8216;|&#8217;). However, REGEXP should not contain parentheses. See also CTDB_DEBUG_HUNG_SCRIPT. </p>
<p> Default is &quot;exportfs|rpcinfo&quot;.</dl>
<p> CTDB_DEBUG_LOCKS=<i>FILENAME</i></p>
<dl>
<dd>FILENAME is a script to run to log debug information when an CTDB fails to freeze databases during recovery. </p>
<p> No default, usually <i>CTDB_BASE</i>/debug_locks.sh.</dl>
<p> CTDB_SYS_ETCDIR=<i>DIRECTORY</i></p>
<dl>
<dd>DIRECTORY containing system configuration files. This is used to provide alternate configuration when testing and should not need to be changed from the default. </p>
<p> Default is /etc.</dl>
<p> CTDB_INIT_STYLE=debian|redhat|suse</p>
<dl>
<dd>This is the init style used by the Linux distribution (or other operating system) being used. This is usually determined dynamically by checking the system. This variable is used by the initscript to determine which init system primitives to use. It is also used by some eventscripts to choose the name of initscripts for certain services, since these can vary between distributions. </p>
<p> No fixed default. </p>
<p> If this option needs to be changed from the calculated default for the initscript to function properly, then it must be set in the distribution-specific initscript configuration, such as /etc/sysconfig/ctdb</dl>
<p> CTDB_MAX_CORRUPT_DB_BACKUPS=<i>NUM</i></p>
<dl>
<dd>NUM is the maximum number of volatile TDB database backups to be kept (for each database) when a corrupt database is found during startup. Volatile TDBs are zeroed during startup so backups are needed to debug any corruption that occurs before a restart. </p>
<p> Default is 10.</dl>
<p> CTDB_MAX_OPEN_FILES=<i>NUM</i></p>
<dl>
<dd>NUM is the maximum number of open files. </p>
<p> There is no default.</dl>
<p> CTDB_RC_LOCAL=<i>FILENAME</i></p>
<dl>
<dd>FILENAME is a script fragment to be sourced by the functions that is sourced by scripts. On example use would be to override function definitions in unit tests. As a sanity check, this file must be executable for it to be used. </p>
<p> No default.</dl>
<p> CTDB_RUN_TIMEOUT_MONITOR=yes|no</p>
<dl>
<dd>Whether CTDB should simulate timing out monitor events. This uses the 99.timeout eventscript. </p>
<p> Default is no.</dl>
<p> CTDB_SCRIPT_DEBUGLEVEL=<i>NUM</i></p>
<dl>
<dd>NUM is the level debugging messages printed by CTDB scripts. Setting this to a higher number (e.g. 4) will cause some scripts to log more messages. </p>
<p> Default is 2.</dl>
<p> CTDB_SUPPRESS_COREFILE=yes|no</p>
<dl>
<dd>Whether CTDB core files should be suppressed. </p>
<p> Default is no.</dl>
<p> CTDB_VALGRIND=yes|no|<i>COMMAND</i></p>
<dl>
<dd>If &quot;yes&quot;, this causes <code><a href="/docs/linux/man/1-ctdbd/">ctdbd</a></code>(1) to be run under <code><a href="/docs/linux/man/1-valgrind/">valgrind</a></code>(1) with logs going to /var/log/ctdb_valgrind. If neither &quot;yes&quot; nor &quot;no&quot; then the value is assumed to be a COMMAND (e.g. a <code>valgrind</code> variation, a <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1) command) that is used in place of the default <code>valgrind</code> command. In either case, the <code>&#8211;valgrind</code> option is passed to <code>ctdbd</code>. </p>
<p> Default is no.</dl>
<p> CTDB_VARDIR=<i>DIRECTORY</i></p>
<dl>
<dd>DIRECTORY containing CTDB files that are modified at runtime. </p>
<p> Defaults to /var/lib/ctdb.</dl>
<h2>Files</h2>
<dl>
<dd>/etc/ctdb/ctdbd.conf</dl>
<dl>
<dd>/etc/sysconfig/ctdb</dl>
<dl>
<dd>/etc/default/ctdb</dl>
<dl>
<dd>/etc/ctdb/sysconfig/ctdb</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ctdbd/">ctdbd</a></code>(1), <code><a href="/docs/linux/man/1-ctdbd_wrapper/">ctdbd_wrapper</a></code>(1), <code><a href="/docs/linux/man/1-onnode/">onnode</a></code>(1), <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7), <code><a href="/docs/linux/man/7-ctdb-tunables/">ctdb-tunables</a></code>(7), m[blue]<code><a rel="nofollow" href="http://ctdb.samba.org/">http://ctdb.samba.org/</a></code>m[]</p>
<h2>Author</h2>
<p>This documentation was written by Amitay Isaacs, Martin Schwenke</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2007 Andrew Tridgell, Ronnie Sahlberg </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, see m[blue]<code><a rel="nofollow" href="http://www.gnu.org/licenses">http://www.gnu.org/licenses</a></code>m[].</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>NFS-Ganesha</p>
<dl>
<dd><a rel="nofollow" href="https://github.com/nfs-ganesha/nfs-ganesha/wiki">https://github.com/nfs-ganesha/nfs-ganesha/wiki</a></dl>
