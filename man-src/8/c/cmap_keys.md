---
title: "cmap_keys(8)"
name: "cmap_keys"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cmap_keys/"
description: "cmap_keys – Overview of keys stored in the Configuration Map"
---

<p>cmap_keys &#8211; Overview of keys stored in the Configuration Map</p>
<h2>Overview</h2>
<p>There are 3 main types of keys stored in CMAP: </p>
<p> * Mapping of values stored in the config file. </p>
<p> * Runtime statistics. </p>
<p> * Other user created values. </p>
<p> In this man page, wild-cards have the usual meaning.</p>
<h2>Keys</h2>
<dl>
<dt>internal_configuration.*</p>
<dd>Internal configuration data. All keys in this prefix are read only. It&#8217;s only useful for getting a list of loaded services. </p>
<dt>logging.*</p>
<dd>Values read from the configuration file. It&#8217;s possible to change them at runtime. If subsystem specific configuration is needed, the key must be in the form logging.logger_subsys.SERVICE.key, where SERVICE is upper case name of the service and key is same as in the configuration file. All values are of string type. </p>
<dt>nodelist.*</p>
<dd>Values read from the configuration file. Each node element in the configuration file gets assigned it&#8217;s position starting from zero. So the first node from the config file has nodelist.node.0. prefix. To be a valid entry, each node must have <code>ring0_addr</code> key. To change the <code>nodeid</code> key, use a u32 data type. </p>
<p> Local node position is stored in <code>local_node_pos</code> key (RO), so it&#8217;s easy to find out nodeid/ring addresses of the local node directly from cmap. </p>
<dt>runtime.blackbox.*</p>
<dd>Trigger keys for storing fplay data. It&#8217;s recommended that you the corosync-blackbox command to change keys in this prefix. </p>
<dt>runtime.connections.*</p>
<dd>There is information about total number of active connections in given moment in the <code>active</code> key, number of closed connections during whole runtime of corosync in the <code>closed</code> key and information about each active IPC connection. All keys in this prefix are read-only. </p>
<dt>runtime.connections.ID.*</p>
<dd>Each IPC connection has a unique ID. This is in the form [[short_name:][PID:]internal_id. On some platforms, short_name and PID are not filled and only internal_id is used. </p>
<p> Typical keys in this prefix are: </p>
<p> <code>client_pid</code> containing PID of IPC connection (unavailable on some platforms). </p>
<p> <code>dispatched</code> number of dispatched messages. </p>
<p> <code>invalid_request</code> number of requests made by IPC which are invalid (calling non-existing call, &#8230;). </p>
<p> <code>name</code> contains short name of the IPC connection (unavailable on some platforms). </p>
<p> <code>overload</code> is number of requests which were not processed because of overload. </p>
<p> <code>queue_size</code> contains the number of messages in the queue waiting for send. </p>
<p> <code>recv_retries</code> is the total number of interrupted receives. </p>
<p> <code>requests</code> contains the number of requests made by IPC. </p>
<p> <code>responses</code> is the number of responses sent to the IPC client. </p>
<p> <code>send_retries</code> contains the total number of interrupted sends. </p>
<p> <code>service_id</code> contains the ID of service which the IPC is connected to. </p>
<dt>runtime.config.*</p>
<dd>Contains the values actually in use by the totem membership protocol. Values here are either taken from the Corosync configuration file, defaults or computed from entries in the config file. For information on individual keys please refer to the man page <code><a href="/docs/linux/man/5-corosync-conf/">corosync.conf</a></code>(5). </p>
<dt>runtime.services.*</p>
<dd>Prefix with statistics for service engines. Each service has it&#8217;s own <code>service_id</code> key in the prefix with the name runtime.services.SERVICE., where SERVICE is the lower case name of the service. Inside the service prefix is the number of messages received and sent by the corosync engine in the format runtime.services.SERVICE.EXEC_CALL.rx and runtime.services.SERVICE.EXEC_CALL.tx, where EXEC_CALL is the internal id of the service call (so for example 3 in cpg service is receive of multicast message from other nodes). </p>
<dt>runtime.totem.pg.mrp.srp.*</p>
<dd>Prefix containing statistics about totem. All keys here are read only. Typical key prefixes: </p>
<p> <code>commit_entered</code> Number of times the processor entered COMMIT state. </p>
<p> <code>commit_token_lost</code> Number of times the processor lost token in COMMIT state. </p>
<p> <code>consensus_timeouts</code> How many times the processor timed out forming a consensus about membership. </p>
<p> <code>continuous_gather</code> How many times the processor was not able to reach consensus. </p>
<p> <code>firewall_enabled_or_nic_failure</code> Set to 1 when processor was not able to reach consensus for long time. The usual reason is a badly configured firewall or connection failure. </p>
<p> <code>gather_entered</code> Number of times the processor entered GATHER state. </p>
<p> <code>gather_token_lost</code> Number of times the processor lost token in GATHER state. </p>
<p> <code>mcast_retx</code> Number of retransmitted messages. </p>
<p> <code>mcast_rx</code> Number of received multicast messages. </p>
<p> <code>mcast_tx</code> Number of transmitted multicast messages. </p>
<p> <code>memb_commit_token_rx</code> Number of received commit tokens. </p>
<p> <code>memb_commit_token_tx</code> Number of transmitted commit tokens. </p>
<p> <code>memb_join_rx</code> Number of received join messages. </p>
<p> <code>memb_join_tx</code> Number of transmitted join messages. </p>
<p> <code>memb_merge_detect_rx</code> Number of received member merge messages. </p>
<p> <code>memb_merge_detect_tx</code> Number of transmitted member merge messages. </p>
<p> <code>orf_token_rx</code> Number of received orf tokens. </p>
<p> <code>orf_token_tx</code> Number of transmitted orf tokens. </p>
<p> <code>recovery_entered</code> Number of times the processor entered recovery. </p>
<p> <code>recovery_token_lost</code> Number of times the token was lost in recovery state. </p>
<p> <code>rx_msg_dropped</code> Number of received messages which were dropped because they were not expected (as example multicast message in commit state). </p>
<p> <code>token_hold_cancel_rx</code> Number of received token hold cancel messages. </p>
<p> <code>token_hold_cancel_tx</code> Number of transmitted token hold cancel messages. </p>
<p> <code>mtt_rx_token</code> Mean transit time of token in milliseconds. In other words, time between two consecutive token receives. </p>
<p> <code>avg_token_workload</code> Average time in milliseconds of holding time of token on the current processor. </p>
<p> <code>avg_backlog_calc</code> Average number of not yet sent messages on the current processor. </p>
<dt>runtime.totem.pg.mrp.srp.members.*</p>
<dd>Prefix containing members of the totem single ring protocol. Each member keys has format runtime.totem.pg.mrp.srp.members.NODEID.KEY, where key is one of: </p>
<p> <code>ip</code> IP address of member. It&#8217;s stored in format r(RING_ID) ip(IP_ADDRESS). </p>
<p> <code>join_count</code> Number of times the processor joined membership with local cluster. When processor fails and rejoins again, this value is incremented. </p>
<p> <code>status</code> Status of the processor. Can be one of joined and left. </p>
<p> <code>config_version</code> Config version of the member node. </p>
<dt>resources.process.PID.*</p>
<dd>Prefix created by applications using SAM with CMAP integration. It contains the following keys: </p>
<p> <code>recovery</code> Recovery policy of the process. Can be one of quit or restart. </p>
<p> <code>poll_period</code> Value passed in sam_initialize as a time_interval. </p>
<p> <code>last_updated</code> Last time SAM received a heartbeat from the client. </p>
<p> <code>state</code> State of the client. Can be one of failed, stopped, running and waiting for quorum. </p>
<dt>uidgid.*</p>
<dd>Information about users/groups which are allowed to make IPC connections to corosync. Entries loaded from configuration file are stored with uidgid.config.* prefix and are pruned on configuration file reload. Dynamic entries has uidgid.* prefix and a configuration file reload doesn&#8217;t affect them. </p>
<dt>quorum.cancel_wait_for_all</p>
<dd>Tells votequorum to cancel waiting for all nodes at cluster startup. Can be used to unblock quorum if notes are known to be down. for pcs use only. </p>
<dt>config.reload_in_progress</p>
<dd>This value will be set to 1 (or created) when a corosync.conf reload is started, and set to 0 when the reload is completed. This allows interested subsystems to do atomic reconfiguration rather than changing each key. Note that individual add/change/delete notifications will still be sent during a reload. </p>
<dt>config.totemconfig_reload_in_progress</p>
<dd>This key is similar to <code>config.totemconfig_reload_in_progress</code> but changed after the totem config trigger is processed. It is useful (mainly) for situations when <code>nodelist.local_node_pos</code> must be correctly reinstated before anything else. </p>
</dl>
<h2>Dynamic Change User/Group Permission To Use Corosync Ipc</h2>
<p>Is the same as in the configuration file. eg: to add UID 500 use </p>
<p> # corosync-cmapctl -s uidgid.uid.500 u8 1 </p>
<p> GID is similar, so to add a GID use </p>
<p> # corosync-cmapctl -s uidgid.gid.500 u8 1 </p>
<p> For removal of permissions, simply delete the key </p>
<p> # corosync-cmapctl -d uidgid.gid.500</p>
<h2>Dynamic Add/Remove Of Udpu Node</h2>
<p>Eg. To add the node with address 10.34.38.108 and nodeid 3. This node is called NEW and it&#8217;s not running corosync yet. </p>
<p> * Find a node position in the node list which is not used yet. It&#8217;s recommended that you use highest_number + 1. Let&#8217;s say output of corosync-cmapctl looks like: </p>
<p> nodelist.local_node_pos (u32) = 1<br />
 nodelist.node.0.nodeid (u32) = 1<br />
 nodelist.node.0.ring0_addr (str) = 10.34.38.106<br />
 nodelist.node.1.nodeid (u32) = 2<br />
 nodelist.node.1.ring0_addr (str) = 10.34.38.107 </p>
<p> So next node position will be 2. </p>
<p> * Add all entries needed for the node on all running nodes, as: </p>
<p> # corosync-cmapctl -s nodelist.node.2.nodeid u32 3<br />
 # corosync-cmapctl -s nodelist.node.2.ring0_addr str 10.34.38.108 </p>
<p> Always add the ring0_addr key last. The Corosync engine on all nodes should reply with <i>notice [TOTEM ] adding new UDPU member {10.34.38.108}</i> message. </p>
<p> * Add node information to the configuration file on all nodes so that it will survive a restart of corosync. </p>
<p> * Copy and edit configuration file to the NEW node. </p>
<p> * Start corosync on the NEW node. </p>
<p> Removal of a UDPU node is a very similar, slightly reversed action, so </p>
<p> * Stop corosync on the OLD node. </p>
<p> * Remove the relevant entries from cmap on all nodes. </p>
<p> * Change the configuration file on all nodes.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-corosync_overview/">corosync_overview</a></code>(8), <code><a href="/docs/linux/man/5-corosync-conf/">corosync.conf</a></code>(5), <code><a href="/docs/linux/man/8-corosync-cmapctl/">corosync-cmapctl</a></code>(8) </p>
