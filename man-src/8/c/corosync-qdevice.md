---
title: "corosync-qdevice(8)"
name: "corosync-qdevice"
section: "8"
letter: "c"
url: "/docs/linux/man/8-corosync-qdevice/"
description: "corosync-qdevice – QDevice daemon"
---

<p>corosync-qdevice &#8211; QDevice daemon</p>
<h2>Synopsis</h2>
<p><code>corosync-qdevice [-dfh] [-S option=value[,option2=value2,&#8230;]]</code> </p>
<h2>Description</h2>
<p><code>corosync-qdevice</code> is a daemon running on each node of a cluster. It provides a configured number of votes to the quorum subsystem based on a third-party arbitrator&#8217;s decision. Its primary use is to allow a cluster to sustain more node failures than standard quorum rules allow. It is recommended for clusters with an even number of nodes and highly recommended for 2 node clusters.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code></p>
<dd>Forcefully turn on debug information without the need to change corosync.conf.</p>
<dt><code>-f</code></p>
<dd>Do not daemonize, run in the foreground.</p>
<dt><code>-h</code></p>
<dd>Show short help text</p>
<dt><code>-S</code></p>
<dd>Set advanced settings described in its own section below. This option shouldn&#8217;t be generally used because most of the options are not safe to change.</dl>
<h2>Configuration</h2>
<p><code>corosync-qdevice</code> reads its configuration from corosync.conf file. </p>
<p> The main configuration is within <code>quorum.device</code> sub-key. Each model also has its own configuration within a similarly named sub-key.</p>
<dl>
<dt><code>model</code></p>
<dd>Specifies the model to be used. This parameter is required. <code>corosync-qdevice</code> is modular and is able to support multiple different models. The model basically defines what type of arbitrator is used. Currently only <i>net</i> is supported.</p>
<dt><code>timeout</code></p>
<dd>Specifies how often should <code>corosync-qdevice</code> should call the votequorum_poll function. It is also used by the net model to adjust its hearbeat timeout. It is recommended that you don&#8217;t change this value. Default is 10000.</p>
<dt><code>sync_timeout</code></p>
<dd>Specifies how often <code>corosync-qdevice</code> should call the votequorum_poll function during a sync phase. It is recommended that you don&#8217;t change this value. Default is 30000.</p>
<dt><code>votes</code></p>
<dd>The number of votes provided to the cluster by qdevice. Default is (number_of_nodes &#8211; 1) or generally sum(votes_per_node) &#8211; 1.</dl>
<p> <code>quorum.device.net</code> holds the configuration for model &#8216;net&#8217;.</p>
<dl>
<dt><code>tls</code></p>
<dd>Can be one of <i>on, off or required</i> and specifies if tls should be used. <i>on</i> means a connection with TLS is attempted first, but if the server doesn&#8217;t advertise TLS support then non-TLS will be used. <i>off</i> is used then TLS is not required and it&#8217;s then not even tried. This mode is the only one which doesn&#8217;t need a properly initialized NSS database. <i>required</i> means TLS is required and if the server doesn&#8217;t support TLS, qdevice will exit with error message. Default is on.</p>
<dt><code>host</code></p>
<dd>Specifies the IP address or host name of the qnetd server to be used. This parameter is required.</p>
<dt><code>port</code></p>
<dd>Specifies TCP port of qnetd server. Default is 5403.</p>
<dt><code>algorithm</code></p>
<dd>Decision algorithm. Can be one of the <i>ffsplit</i> or <i>lms.</i> (actually there are also <i>test</i> and <i>2nodelms</i> , both of which are mainly for developers and shouldn&#8217;t be used for production clusters). For a description of what each algorithm means and how the algorithms differ see their individual sections. Default value is ffsplit.</p>
<dt><code>tie-breaker</code></p>
<dd>can be one of <i>lowest,</i> <i>highest</i> or valid_node_id (number) values. It&#8217;s used as a fallback if qdevice has to decide between two or more equal partitions. <i>lowest</i> means the partition with the lowest node id is chosen. <i>highest</i> means the partition with highest node id is chosen. And valid_node_id means that the partition containing the node with the given node id is chosen.</p>
<dt><code>connect_timeout</code></p>
<dd>Timeout when <code>corosync-qdevice</code> is trying to connect to <code>corosync-qnetd</code> host. Default is 0.8 * quorum.sync_timeout.</p>
<dt><code>force_ip_version</code></p>
<dd>can be one of <i>0|4|6</i> and forces the software to use the given IP version. <i>0</i> (default value) means IPv6 is prefered and IPv4 should be used as a fallback. </p>
</dl>
<p> Logging configuration is within the <code>logging</code> directive. <code>corosync-qdevice</code> parses and supports most of the options with exception of <code>to_logfile,</code> <code>logfile</code> and <code>logfile_priority.</code> The <code>logger_subsys</code> sub-directive can be also used if <code>subsys</code> is set to QDEVICE. </p>
<p> For <code>corosync-qdevice</code> to work correctly, the <code>nodelist</code> directive has to be used and properly configured. Also the net model requires that <code>totem.cluster_name</code> option is set.</p>
<h2>Model Net Tls Configuration</h2>
<p>For model net to work using TLS, it&#8217;s necessary to create the NSS database, import Qnetd CA certificate, and get/distribute a valid client certificate. </p>
<p> If pcs is used (recommended) the following steps are not needed because pcs does them automatically. </p>
<p> <code>corosync-qdevice-net-certutil</code> is the tool to perform required actions semi-automatically. Please consult the help output of it and its man page. For a first time configuration it may make sense to start with the <code>-Q</code> option. </p>
<p> If TLS is not required just edit corosync.conf file and set <code>quorum.device.net.tls</code> to <i>off.</i></p>
<h2>Model Net Algorithms</h2>
<p>Algorithms are used to change behavior of how <code>corosync-qnetd</code> provides votes to a given node/partition. Currently there are two algorithms supported.</p>
<dl>
<dt><code>ffsplit</code></p>
<dd>This one makes sense only for clusters with even number of nodes. It provides exactly one vote to the partition with the highest number of active nodes. If there are two exactly similar partitions, it provides its vote to the partition that has the most clients connected to the qnetd server. If this number is also equal, then the tie-breaker is used. It is able to transition its vote if the currently active partition becomes partitioned and a non-active partition still has at least 50% of the active nodes. Because of this, a vote is not provided if the qnetd connection is not active. </p>
<p> To use this algorithm it&#8217;s required to set the number of votes per node to 1 (default) and the qdevice number of votes has to be also 1. This is achieved by setting <code>quorum.device.votes</code> key in corosync.conf file to 1.</p>
<dt><code>lms</code></p>
<dd>Last-man-standing. If the node is the only one left in the cluster that can see the qnetd server then we return a vote. </p>
<p> If more than one node can see the qnetd server but some nodes can&#8217;t see each other then the cluster is divided up into &#8216;partitions&#8217; based on their ring_id and this algorithm returns a vote to the largest active partition or, if there is more than 1 equal partiton, the partition that contains the tie_breaker node (lowest, highest, etc). For LMS to work, the number of qdevice votes has to be set to default (so just delete <code>quorum.device.votes</code> key from corosync.conf). </p>
</dl>
<h2>Advanced Settings</h2>
<p>Set by using <code>-S</code> option. The default value is shown in parentheses) Options beginning with <code>net_</code> prefix are specific to model net.</p>
<dl>
<dt><code>lock_file</code></p>
<dd>Lock file location. (/var/run/corosync-qdevice/corosync-qdevice.pid)</p>
<dt><code>local_socket_file</code></p>
<dd>Internal IPC socket file location. (/var/run/corosync-qdevice/corosync-qdevice.sock)</p>
<dt><code>local_socket_backlog</code></p>
<dd>Parameter passed to listen syscall. (10)</p>
<dt><code>max_cs_try_again</code></p>
<dd>How many times to retry the call to a corosync function which has returned CS_ERR_TRY_AGAIN. (10)</p>
<dt><code>votequorum_device_name</code></p>
<dd>Name used for qdevice registration. (Qdevice)</p>
<dt><code>ipc_max_clients</code></p>
<dd>Maximum allowed simultaneous IPC clients. (10)</p>
<dt><code>ipc_max_receive_size</code></p>
<dd>Maximum size of a message received by IPC client. (4096)</p>
<dt><code>ipc_max_send_size</code></p>
<dd>Maximum size of a message allowed to be sent to an IPC client. (65536)</p>
<dt><code>master_wins</code></p>
<dd>Force enable/disable master wins. (default is model)</p>
<dt><code>net_nss_db_dir</code></p>
<dd>NSS database directory. (/etc/corosync/qdevice/net/nssdb)</p>
<dt><code>net_initial_msg_receive_size</code></p>
<dd>Initial (used during connection parameters negotiation) maximum size of the receive buffer for message (maximum allowed message size received from qnetd). (32768)</p>
<dt><code>net_initial_msg_send_size</code></p>
<dd>Initial (used during connection parameter negotiation) maximum size of one send buffer (message) to be sent to server. (32768)</p>
<dt><code>net_min_msg_send_size</code></p>
<dd>Minimum required size of one send buffer (message) to be sent to server. (32768)</p>
<dt><code>net_max_msg_receive_size</code></p>
<dd>Maximum allowed size of receive buffer for a message sent by server. (16777216)</p>
<dt><code>net_max_send_buffers</code></p>
<dd>Maximum number of send buffers. (10)</p>
<dt><code>net_nss_qnetd_cn</code></p>
<dd>Canonical name of qnetd server certificate. (Qnetd Server)</p>
<dt><code>net_nss_client_cert_nickname</code></p>
<dd>NSS nickname of qdevice client certificate. (Cluster Cert)</p>
<dt><code>net_heartbeat_interval_min</code></p>
<dd>Minimum heartbeat timeout accepted by client in ms. (1000)</p>
<dt><code>net_heartbeat_interval_max</code></p>
<dd>Maximum heartbeat timeout accepted by client in ms. (120000)</p>
<dt><code>net_min_connect_timeout</code></p>
<dd>Minimum connection timeout accepted by client in ms. (1000)</p>
<dt><code>net_max_connect_timeout</code></p>
<dd>Maximum connection timeout accepted by client in ms. (120000)</p>
<dt><code>net_test_algorithm_enabled</code></p>
<dd>Enable test algorithm. (if built with &#8211;enable-debug on, otherwise off)</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-corosync-qdevice-tool/">corosync-qdevice-tool</a></code>(8) <code><a href="/docs/linux/man/8-corosync-qdevice-net-certutil/">corosync-qdevice-net-certutil</a></code>(8) <code><a href="/docs/linux/man/8-corosync-qnetd/">corosync-qnetd</a></code>(8) <code><a href="/docs/linux/man/5-corosync-conf/">corosync.conf</a></code>(5)</p>
<h2>Author</h2>
<p>Jan Friesse</p>
