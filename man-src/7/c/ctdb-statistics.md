---
title: "ctdb-statistics(7)"
name: "ctdb-statistics"
section: "7"
letter: "c"
url: "/docs/linux/man/7-ctdb-statistics/"
description: "ctdb-statistics – CTDB statistics output"
---

<p>ctdb-statistics &#8211; CTDB statistics output</p>
<h2>Overall Statistics</h2>
<p>CTDB maintains information about various messages communicated and some of the important operations per node. See the <code><a href="/docs/linux/man/1-ctdb/">ctdb</a></code>(1) commands <code>statistics</code> and <code>statisticsreset</code> for displaying statistics.</p>
<h3>Example: ctdb statistics</h3>
<dl>
<dd>
<pre>CTDB version 1
Current time of statistics : Fri Sep 12 13:32:32 2014
Statistics collected since : (000 01:49:20) Fri Sep 12 11:43:12 2014
 num_clients 6
 frozen 0
 recovering 0
 num_recoveries 2
 client_packets_sent 281293
 client_packets_recv 296317
 node_packets_sent 452387
 node_packets_recv 182394
 keepalive_packets_sent 3927
 keepalive_packets_recv 3928
 node
 req_call 48605
 reply_call 1
 req_dmaster 23404
 reply_dmaster 24917
 reply_error 0
 req_message 958
 req_control 197513
 reply_control 153705
 client
 req_call 130866
 req_message 770
 req_control 168921
 timeouts
 call 0
 control 0
 traverse 0
 locks
 num_calls 220
 num_current 0
 num_pending 0
 num_failed 0
 total_calls 130866
 pending_calls 0
 childwrite_calls 1
 pending_childwrite_calls 0
 memory_used 334490
 max_hop_count 18
 total_ro_delegations 2
 total_ro_revokes 2
 hop_count_buckets: 42816 5464 26 1 0 0 0 0 0 0 0 0 0 0 0 0
 lock_buckets: 9 165 14 15 7 2 2 0 0 0 0 0 0 0 0 0
 locks_latency MIN/AVG/MAX 0.000685/0.160302/6.369342 sec out of 214
 reclock_ctdbd MIN/AVG/MAX 0.004940/0.004969/0.004998 sec out of 2
 reclock_recd MIN/AVG/MAX 0.000000/0.000000/0.000000 sec out of 0
 call_latency MIN/AVG/MAX 0.000006/0.000719/4.562991 sec out of 126626
 childwrite_latency MIN/AVG/MAX 0.014527/0.014527/0.014527 sec out of 1</pre>
</dl>
<h3>CTDB version</h3>
<p>Version of the ctdb protocol used by the node.</p>
<h3>Current time of statistics</h3>
<p>Time when the statistics are generated. </p>
<p> This is useful when collecting statistics output periodically for post-processing.</p>
<h3>Statistics collected since</h3>
<p>Time when ctdb was started or the last time statistics was reset. The output shows the duration and the timestamp.</p>
<h3>num_clients</h3>
<p>Number of processes currently connected to CTDB&#8217;s unix socket. This includes recovery daemon, ctdb tool and samba processes (smbd, winbindd).</p>
<h3>frozen</h3>
<p>1 if the the databases are currently frozen, 0 otherwise.</p>
<h3>recovering</h3>
<p>1 if recovery is active, 0 otherwise.</p>
<h3>num_recoveries</h3>
<p>Number of recoveries since the start of ctdb or since the last statistics reset.</p>
<h3>client_packets_sent</h3>
<p>Number of packets sent to client processes via unix domain socket.</p>
<h3>client_packets_recv</h3>
<p>Number of packets received from client processes via unix domain socket.</p>
<h3>node_packets_sent</h3>
<p>Number of packets sent to the other nodes in the cluster via TCP.</p>
<h3>node_packets_recv</h3>
<p>Number of packets received from the other nodes in the cluster via TCP.</p>
<h3>keepalive_packets_sent</h3>
<p>Number of keepalive messages sent to other nodes. </p>
<p> CTDB periodically sends keepalive messages to other nodes. See KeepaliveInterval tunable in <code><a href="/docs/linux/man/7-ctdb-tunables/">ctdb-tunables</a></code>(7) for more details.</p>
<h3>keepalive_packets_recv</h3>
<p>Number of keepalive messages received from other nodes.</p>
<h3>node</h3>
<p>This section lists various types of messages processed which originated from other nodes via TCP. </p>
<p> <font SIZE="+1"> <code>req_call</code></p>
<dl>
<dd>Number of REQ_CALL messages from the other nodes.</dl>
<p> </font><font SIZE="+2"> <code>reply_call</code></p>
<dl>
<dd>Number of REPLY_CALL messages from the other nodes.</dl>
<p> </font><font SIZE="+3"> <code>req_dmaster</code></p>
<dl>
<dd>Number of REQ_DMASTER messages from the other nodes.</dl>
<p> </font><font SIZE="+4"> <code>reply_dmaster</code></p>
<dl>
<dd>Number of REPLY_DMASTER messages from the other nodes.</dl>
<p> </font><font SIZE="+5"> <code>reply_error</code></p>
<dl>
<dd>Number of REPLY_ERROR messages from the other nodes.</dl>
<p> </font><font SIZE="+6"> <code>req_message</code></p>
<dl>
<dd>Number of REQ_MESSAGE messages from the other nodes.</dl>
<p> </font><font SIZE="+7"> <code>req_control</code></p>
<dl>
<dd>Number of REQ_CONTROL messages from the other nodes.</dl>
<p> </font><font SIZE="+8"> <code>reply_control</code></p>
<dl>
<dd>Number of REPLY_CONTROL messages from the other nodes.</dl>
<p> </font></p>
<h3>client</h3>
<p>This section lists various types of messages processed which originated from clients via unix domain socket. </p>
<p> <font SIZE="+1"> <code>req_call</code></p>
<dl>
<dd>Number of REQ_CALL messages from the clients.</dl>
<p> </font><font SIZE="+2"> <code>req_message</code></p>
<dl>
<dd>Number of REQ_MESSAGE messages from the clients.</dl>
<p> </font><font SIZE="+3"> <code>req_control</code></p>
<dl>
<dd>Number of REQ_CONTROL messages from the clients.</dl>
<p> </font></p>
<h3>timeouts</h3>
<p>This section lists timeouts occurred when sending various messages. </p>
<p> <font SIZE="+1"> <code>call</code></p>
<dl>
<dd>Number of timeouts for REQ_CALL messages.</dl>
<p> </font><font SIZE="+2"> <code>control</code></p>
<dl>
<dd>Number of timeouts for REQ_CONTROL messages.</dl>
<p> </font><font SIZE="+3"> <code>traverse</code></p>
<dl>
<dd>Number of timeouts for database traverse operations.</dl>
<p> </font></p>
<h3>locks</h3>
<p>This section lists locking statistics. </p>
<p> <font SIZE="+1"> <code>num_calls</code></p>
<dl>
<dd>Number of completed lock calls. This includes database locks and record locks.</dl>
<p> </font><font SIZE="+2"> <code>num_current</code></p>
<dl>
<dd>Number of scheduled lock calls. This includes database locks and record locks.</dl>
<p> </font><font SIZE="+3"> <code>num_pending</code></p>
<dl>
<dd>Number of queued lock calls. This includes database locks and record locks.</dl>
<p> </font><font SIZE="+4"> <code>num_failed</code></p>
<dl>
<dd>Number of failed lock calls. This includes database locks and record locks.</dl>
<p> </font></p>
<h3>total_calls</h3>
<p>Number of req_call messages processed from clients. This number should be same as client &#8211;&gt; req_call.</p>
<h3>pending_calls</h3>
<p>Number of req_call messages which are currenly being processed. This number indicates the number of record migrations in flight.</p>
<h3>childwrite_calls</h3>
<p>Number of record update calls. Record update calls are used to update a record under a transaction.</p>
<h3>pending_childwrite_calls</h3>
<p>Number of record update calls currently active.</p>
<h3>memory_used</h3>
<p>The amount of memory in bytes currently used by CTDB using talloc. This includes all the memory used for CTDB&#8217;s internal data structures. This does not include the memory mapped TDB databases.</p>
<h3>max_hop_count</h3>
<p>The maximum number of hops required for a record migration request to obtain the record. High numbers indicate record contention.</p>
<h3>total_ro_delegations</h3>
<p>Number of readonly delegations created.</p>
<h3>total_ro_revokes</h3>
<p>Number of readonly delegations that were revoked. The difference between total_ro_revokes and total_ro_delegations gives the number of currently active readonly delegations.</p>
<h3>hop_count_buckets</h3>
<p>Distribution of migration requests based on hop counts values. Buckets are 1, &lt; 4, &lt; 8, &lt; 16, &lt; 32, &lt; 64, &lt; 128, &lt; 256, &lt; 512, ≥ 512.</p>
<h3>lock_buckets</h3>
<p>Distribution of record lock requests based on time required to obtain locks. Buckets are &lt; 1ms, &lt; 10ms, &lt; 100ms, &lt; 1s, &lt; 2s, &lt; 4s, &lt; 8s, &lt; 16s, &lt; 32s, &lt; 64s, ≥ 64s.</p>
<h3>locks_latency</h3>
<p>The minimum, the average and the maximum time (in seconds) required to obtain record locks.</p>
<h3>reclock_ctdbd</h3>
<p>The minimum, the average and the maximum time (in seconds) required to check if recovery lock is still held by recovery daemon when recovery mode is changed. This check is done in ctdb daemon.</p>
<h3>reclock_recd</h3>
<p>The minimum, the average and the maximum time (in seconds) required to check if recovery lock is still held by recovery daemon during recovery. This check is done in recovery daemon.</p>
<h3>call_latency</h3>
<p>The minimum, the average and the maximum time (in seconds) required to process a REQ_CALL message from client. This includes the time required to migrate a record from remote node, if the record is not available on the local node.</p>
<h3>childwrite_latency</h3>
<p>Default: 0 </p>
<p> The minimum, the average and the maximum time (in seconds) required to update records under a transaction.</p>
<h2>Database Statistics</h2>
<p>CTDB maintains per database statistics about important operations. See the <code><a href="/docs/linux/man/1-ctdb/">ctdb</a></code>(1) command <code>dbstatistics</code> for displaying database statistics.</p>
<h3>Example: ctdb dbstatistics notify_index.tdb</h3>
<dl>
<dd>
<pre>DB Statistics: notify_index.tdb
 ro_delegations 0
 ro_revokes 0
 locks
 total 131
 failed 0
 current 0
 pending 0
 hop_count_buckets: 9890 5454 26 1 0 0 0 0 0 0 0 0 0 0 0 0
 lock_buckets: 4 117 10 0 0 0 0 0 0 0 0 0 0 0 0 0
 locks_latency MIN/AVG/MAX 0.000683/0.004198/0.014730 sec out of 131
 Num Hot Keys: 3
 Count:7 Key:2f636c75737465726673
 Count:18 Key:2f636c757374657266732f64617461
 Count:7 Key:2f636c757374657266732f646174612f636c69656e7473</pre>
</dl>
<h3>DB Statistics</h3>
<p>Name of the database.</p>
<h3>ro_delegations</h3>
<p>Number of readonly delegations created in the database.</p>
<h3>ro_revokes</h3>
<p>Number of readonly delegations revoked. The difference in ro_delegations and ro_revokes indicates the currently active readonly delegations.</p>
<h3>locks</h3>
<p>This section lists locking statistics. </p>
<p> <font SIZE="+1"> <code>total</code></p>
<dl>
<dd>Number of completed lock calls. This includes database locks and record locks.</dl>
<p> </font><font SIZE="+2"> <code>failed</code></p>
<dl>
<dd>Number of failed lock calls. This includes database locks and record locks.</dl>
<p> </font><font SIZE="+3"> <code>current</code></p>
<dl>
<dd>Number of scheduled lock calls. This includes database locks and record locks.</dl>
<p> </font><font SIZE="+4"> <code>pending</code></p>
<dl>
<dd>Number of queued lock calls. This includes database locks and record locks.</dl>
<p> </font></p>
<h3>hop_count_buckets</h3>
<p>Distribution of migration requests based on hop counts values. Buckets are 1, &lt; 4, &lt; 8, &lt; 16, &lt; 32, &lt; 64, &lt; 128, &lt; 256, &lt; 512, ≥ 512.</p>
<h3>lock_buckets</h3>
<p>Distribution of record lock requests based on time required to obtain locks. Buckets are &lt; 1ms, &lt; 10ms, &lt; 100ms, &lt; 1s, &lt; 2s, &lt; 4s, &lt; 8s, &lt; 16s, &lt; 32s, &lt; 64s, ≥ 64s.</p>
<h3>locks_latency</h3>
<p>The minimum, the average and the maximum time (in seconds) required to obtain record locks.</p>
<h3>Num Hot Keys</h3>
<p>Number of contended records determined by hop count. CTDB keeps track of top 10 hot records and the output shows hex encoded keys for the hot records.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ctdb/">ctdb</a></code>(1), <code><a href="/docs/linux/man/1-ctdbd/">ctdbd</a></code>(1), <code><a href="/docs/linux/man/7-ctdb-tunables/">ctdb-tunables</a></code>(7), m[blue]<code><a rel="nofollow" href="http://ctdb.samba.org/">http://ctdb.samba.org/</a></code>m[]</p>
<h2>Author</h2>
<p>This documentation was written by Amitay Isaacs, Martin Schwenke</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2007 Andrew Tridgell, Ronnie Sahlberg </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, see m[blue]<code><a rel="nofollow" href="http://www.gnu.org/licenses">http://www.gnu.org/licenses</a></code>m[].</p>
