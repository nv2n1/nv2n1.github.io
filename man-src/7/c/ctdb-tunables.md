---
title: "ctdb-tunables(7)"
name: "ctdb-tunables"
section: "7"
letter: "c"
url: "/docs/linux/man/7-ctdb-tunables/"
description: "ctdb-tunables – CTDB tunable configuration variables"
---

<p>ctdb-tunables &#8211; CTDB tunable configuration variables</p>
<h2>Description</h2>
<p>CTDB&#8217;s behaviour can be configured by setting run-time tunable variables. This lists and describes all tunables. See the <code><a href="/docs/linux/man/1-ctdb/">ctdb</a></code>(1)<code>listvars</code>, <code>setvar</code> and <code>getvar</code> commands for more details.</p>
<h3>MaxRedirectCount</h3>
<p>Default: 3 </p>
<p> If we are not the DMASTER and need to fetch a record across the network we first send the request to the LMASTER after which the record is passed onto the current DMASTER. If the DMASTER changes before the request has reached that node, the request will be passed onto the &quot;next&quot; DMASTER. For very hot records that migrate rapidly across the cluster this can cause a request to &quot;chase&quot; the record for many hops before it catches up with the record. this is how many hops we allow trying to chase the DMASTER before we switch back to the LMASTER again to ask for new directions. </p>
<p> When chasing a record, this is how many hops we will chase the record for before going back to the LMASTER to ask for new guidance.</p>
<h3>SeqnumInterval</h3>
<p>Default: 1000 </p>
<p> Some databases have seqnum tracking enabled, so that samba will be able to detect asynchronously when there has been updates to the database. Everytime a database is updated its sequence number is increased. </p>
<p> This tunable is used to specify in &#8216;ms&#8217; how frequently ctdb will send out updates to remote nodes to inform them that the sequence number is increased.</p>
<h3>ControlTimeout</h3>
<p>Default: 60 </p>
<p> This is the default setting for timeout for when sending a control message to either the local or a remote ctdb daemon.</p>
<h3>TraverseTimeout</h3>
<p>Default: 20 </p>
<p> This setting controls how long we allow a traverse process to run. After this timeout triggers, the main ctdb daemon will abort the traverse if it has not yet finished.</p>
<h3>KeepaliveInterval</h3>
<p>Default: 5 </p>
<p> How often in seconds should the nodes send keepalives to eachother.</p>
<h3>KeepaliveLimit</h3>
<p>Default: 5 </p>
<p> After how many keepalive intervals without any traffic should a node wait until marking the peer as DISCONNECTED. </p>
<p> If a node has hung, it can thus take KeepaliveInterval*(KeepaliveLimit+1) seconds before we determine that the node is DISCONNECTED and that we require a recovery. This limitshould not be set too high since we want a hung node to be detectec, and expunged from the cluster well before common CIFS timeouts (45-90 seconds) kick in.</p>
<h3>RecoverTimeout</h3>
<p>Default: 20 </p>
<p> This is the default setting for timeouts for controls when sent from the recovery daemon. We allow longer control timeouts from the recovery daemon than from normal use since the recovery dameon often use controls that can take a lot longer than normal controls.</p>
<h3>RecoverInterval</h3>
<p>Default: 1 </p>
<p> How frequently in seconds should the recovery daemon perform the consistency checks that determine if we need to perform a recovery or not.</p>
<h3>ElectionTimeout</h3>
<p>Default: 3 </p>
<p> When electing a new recovery master, this is how many seconds we allow the election to take before we either deem the election finished or we fail the election and start a new one.</p>
<h3>TakeoverTimeout</h3>
<p>Default: 9 </p>
<p> This is how many seconds we allow controls to take for IP failover events.</p>
<h3>MonitorInterval</h3>
<p>Default: 15 </p>
<p> How often should ctdb run the event scripts to check for a nodes health.</p>
<h3>TickleUpdateInterval</h3>
<p>Default: 20 </p>
<p> How often will ctdb record and store the &quot;tickle&quot; information used to kickstart stalled tcp connections after a recovery.</p>
<h3>EventScriptTimeout</h3>
<p>Default: 30 </p>
<p> Maximum time in seconds to allow an event to run before timing out. This is the total time for all enabled scripts that are run for an event, not just a single event script. </p>
<p> Note that timeouts are ignored for some events (&quot;takeip&quot;, &quot;releaseip&quot;, &quot;startrecovery&quot;, &quot;recovered&quot;) and converted to success. The logic here is that the callers of these events implement their own additional timeout.</p>
<h3>MonitorTimeoutCount</h3>
<p>Default: 20 </p>
<p> How many monitor events in a row need to timeout before a node is flagged as UNHEALTHY. This setting is useful if scripts can not be written so that they do not hang for benign reasons.</p>
<h3>RecoveryGracePeriod</h3>
<p>Default: 120 </p>
<p> During recoveries, if a node has not caused recovery failures during the last grace period, any records of transgressions that the node has caused recovery failures will be forgiven. This resets the ban-counter back to zero for that node.</p>
<h3>RecoveryBanPeriod</h3>
<p>Default: 300 </p>
<p> If a node becomes banned causing repetitive recovery failures. The node will eventually become banned from the cluster. This controls how long the culprit node will be banned from the cluster before it is allowed to try to join the cluster again. Don&#8217;t set to small. A node gets banned for a reason and it is usually due to real problems with the node.</p>
<h3>DatabaseHashSize</h3>
<p>Default: 100001 </p>
<p> Size of the hash chains for the local store of the tdbs that ctdb manages.</p>
<h3>DatabaseMaxDead</h3>
<p>Default: 5 </p>
<p> How many dead records per hashchain in the TDB database do we allow before the freelist needs to be processed.</p>
<h3>RerecoveryTimeout</h3>
<p>Default: 10 </p>
<p> Once a recovery has completed, no additional recoveries are permitted until this timeout has expired.</p>
<h3>EnableBans</h3>
<p>Default: 1 </p>
<p> When set to 0, this disables BANNING completely in the cluster and thus nodes can not get banned, even it they break. Don&#8217;t set to 0 unless you know what you are doing. You should set this to the same value on all nodes to avoid unexpected behaviour.</p>
<h3>DeterministicIPs</h3>
<p>Default: 0 </p>
<p> When enabled, this tunable makes ctdb try to keep public IP addresses locked to specific nodes as far as possible. This makes it easier for debugging since you can know that as long as all nodes are healthy public IP X will always be hosted by node Y. </p>
<p> The cost of using deterministic IP address assignment is that it disables part of the logic where ctdb tries to reduce the number of public IP assignment changes in the cluster. This tunable may increase the number of IP failover/failbacks that are performed on the cluster by a small margin.</p>
<h3>LCP2PublicIPs</h3>
<p>Default: 1 </p>
<p> When enabled this switches ctdb to use the LCP2 ip allocation algorithm.</p>
<h3>ReclockPingPeriod</h3>
<p>Default: x </p>
<p> Obsolete</p>
<h3>NoIPFailback</h3>
<p>Default: 0 </p>
<p> When set to 1, ctdb will not perform failback of IP addresses when a node becomes healthy. Ctdb WILL perform failover of public IP addresses when a node becomes UNHEALTHY, but when the node becomes HEALTHY again, ctdb will not fail the addresses back. </p>
<p> Use with caution! Normally when a node becomes available to the cluster ctdb will try to reassign public IP addresses onto the new node as a way to distribute the workload evenly across the clusternode. Ctdb tries to make sure that all running nodes have approximately the same number of public addresses it hosts. </p>
<p> When you enable this tunable, CTDB will no longer attempt to rebalance the cluster by failing IP addresses back to the new nodes. An unbalanced cluster will therefore remain unbalanced until there is manual intervention from the administrator. When this parameter is set, you can manually fail public IP addresses over to the new node(s) using the &#8216;ctdb moveip&#8217; command.</p>
<h3>DisableIPFailover</h3>
<p>Default: 0 </p>
<p> When enabled, ctdb will not perform failover or failback. Even if a node fails while holding public IPs, ctdb will not recover the IPs or assign them to another node. </p>
<p> When you enable this tunable, CTDB will no longer attempt to recover the cluster by failing IP addresses over to other nodes. This leads to a service outage until the administrator has manually performed failover to replacement nodes using the &#8216;ctdb moveip&#8217; command.</p>
<h3>NoIPTakeover</h3>
<p>Default: 0 </p>
<p> When set to 1, ctdb will not allow IP addresses to be failed over onto this node. Any IP addresses that the node currently hosts will remain on the node but no new IP addresses can be failed over to the node.</p>
<h3>NoIPHostOnAllDisabled</h3>
<p>Default: 0 </p>
<p> If no nodes are healthy then by default ctdb will happily host public IPs on disabled (unhealthy or administratively disabled) nodes. This can cause problems, for example if the underlying cluster filesystem is not mounted. When set to 1 on a node and that node is disabled it, any IPs hosted by this node will be released and the node will not takeover any IPs until it is no longer disabled.</p>
<h3>DBRecordCountWarn</h3>
<p>Default: 100000 </p>
<p> When set to non-zero, ctdb will log a warning when we try to recover a database with more than this many records. This will produce a warning if a database grows uncontrollably with orphaned records.</p>
<h3>DBRecordSizeWarn</h3>
<p>Default: 10000000 </p>
<p> When set to non-zero, ctdb will log a warning when we try to recover a database where a single record is bigger than this. This will produce a warning if a database record grows uncontrollably with orphaned sub-records.</p>
<h3>DBSizeWarn</h3>
<p>Default: 1000000000 </p>
<p> When set to non-zero, ctdb will log a warning when we try to recover a database bigger than this. This will produce a warning if a database grows uncontrollably.</p>
<h3>VerboseMemoryNames</h3>
<p>Default: 0 </p>
<p> This feature consumes additional memory. when used the talloc library will create more verbose names for all talloc allocated objects.</p>
<h3>RecdPingTimeout</h3>
<p>Default: 60 </p>
<p> If the main dameon has not heard a &quot;ping&quot; from the recovery dameon for this many seconds, the main dameon will log a message that the recovery daemon is potentially hung.</p>
<h3>RecdFailCount</h3>
<p>Default: 10 </p>
<p> If the recovery daemon has failed to ping the main dameon for this many consecutive intervals, the main daemon will consider the recovery daemon as hung and will try to restart it to recover.</p>
<h3>LogLatencyMs</h3>
<p>Default: 0 </p>
<p> When set to non-zero, this will make the main daemon log any operation that took longer than this value, in &#8216;ms&#8217;, to complete. These include &quot;how long time a lockwait child process needed&quot;, &quot;how long time to write to a persistent database&quot; but also &quot;how long did it take to get a response to a CALL from a remote node&quot;.</p>
<h3>RecLockLatencyMs</h3>
<p>Default: 1000 </p>
<p> When using a reclock file for split brain prevention, if set to non-zero this tunable will make the recovery dameon log a message if the fcntl() call to lock/testlock the recovery file takes longer than this number of ms.</p>
<h3>RecoveryDropAllIPs</h3>
<p>Default: 120 </p>
<p> If we have been stuck in recovery, or stopped, or banned, mode for this many seconds we will force drop all held public addresses.</p>
<h3>VacuumInterval</h3>
<p>Default: 10 </p>
<p> Periodic interval in seconds when vacuuming is triggered for volatile databases.</p>
<h3>VacuumMaxRunTime</h3>
<p>Default: 120 </p>
<p> The maximum time in seconds for which the vacuuming process is allowed to run. If vacuuming process takes longer than this value, then the vacuuming process is terminated.</p>
<h3>RepackLimit</h3>
<p>Default: 10000 </p>
<p> During vacuuming, if the number of freelist records are more than <i>RepackLimit</i>, then databases are repacked to get rid of the freelist records to avoid fragmentation. </p>
<p> Databases are repacked only if both <i>RepackLimit</i> and <i>VacuumLimit</i> are exceeded.</p>
<h3>VacuumLimit</h3>
<p>Default: 5000 </p>
<p> During vacuuming, if the number of deleted records are more than <i>VacuumLimit</i>, then databases are repacked to avoid fragmentation. </p>
<p> Databases are repacked only if both <i>RepackLimit</i> and <i>VacuumLimit</i> are exceeded.</p>
<h3>VacuumFastPathCount</h3>
<p>Default: 60 </p>
<p> When a record is deleted, it is marked for deletion during vacuuming. Vacuuming process usually processes this list to purge the records from the database. If the number of records marked for deletion are more than VacuumFastPathCount, then vacuuming process will scan the complete database for empty records instead of using the list of records marked for deletion.</p>
<h3>DeferredAttachTO</h3>
<p>Default: 120 </p>
<p> When databases are frozen we do not allow clients to attach to the databases. Instead of returning an error immediately to the application the attach request from the client is deferred until the database becomes available again at which stage we respond to the client. </p>
<p> This timeout controls how long we will defer the request from the client before timing it out and returning an error to the client.</p>
<h3>HopcountMakeSticky</h3>
<p>Default: 50 </p>
<p> If the database is set to &#8216;STICKY&#8217; mode, using the &#8216;ctdb setdbsticky&#8217; command, any record that is seen as very hot and migrating so fast that hopcount surpasses 50 is set to become a STICKY record for StickyDuration seconds. This means that after each migration the record will be kept on the node and prevented from being migrated off the node. </p>
<p> This setting allows one to try to identify such records and stop them from migrating across the cluster so fast. This will improve performance for certain workloads, such as locking.tdb if many clients are opening/closing the same file concurrently.</p>
<h3>StickyDuration</h3>
<p>Default: 600 </p>
<p> Once a record has been found to be fetch-lock hot and has been flagged to become STICKY, this is for how long, in seconds, the record will be flagged as a STICKY record.</p>
<h3>StickyPindown</h3>
<p>Default: 200 </p>
<p> Once a STICKY record has been migrated onto a node, it will be pinned down on that node for this number of ms. Any request from other nodes to migrate the record off the node will be deferred until the pindown timer expires.</p>
<h3>StatHistoryInterval</h3>
<p>Default: 1 </p>
<p> Granularity of the statistics collected in the statistics history.</p>
<h3>AllowClientDBAttach</h3>
<p>Default: 1 </p>
<p> When set to 0, clients are not allowed to attach to any databases. This can be used to temporarily block any new processes from attaching to and accessing the databases.</p>
<h3>RecoverPDBBySeqNum</h3>
<p>Default: 1 </p>
<p> When set to zero, database recovery for persistent databases is record-by-record and recovery process simply collects the most recent version of every individual record. </p>
<p> When set to non-zero, persistent databases will instead be recovered as a whole db and not by individual records. The node that contains the highest value stored in the record &quot;__db_sequence_number__&quot; is selected and the copy of that nodes database is used as the recovered database. </p>
<p> By default, recovery of persistent databses is done using __db_sequence_number__ record.</p>
<h3>FetchCollapse</h3>
<p>Default: 1 </p>
<p> When many clients across many nodes try to access the same record at the same time this can lead to a fetch storm where the record becomes very active and bounces between nodes very fast. This leads to high CPU utilization of the ctdbd daemon, trying to bounce that record around very fast, and poor performance. </p>
<p> This parameter is used to activate a fetch-collapse. A fetch-collapse is when we track which records we have requests in flight so that we only keep one request in flight from a certain node, even if multiple smbd processes are attemtping to fetch the record at the same time. This can improve performance and reduce CPU utilization for certain workloads. </p>
<p> This timeout controls if we should collapse multiple fetch operations of the same record into a single request and defer all duplicates or not.</p>
<h3>Samba3AvoidDeadlocks</h3>
<p>Default: 0 </p>
<p> Enable code that prevents deadlocks with Samba (only for Samba 3.x). </p>
<p> This should be set to 1 when using Samba version 3.x to enable special code in CTDB to avoid deadlock with Samba version 3.x. This code is not required for Samba version 4.x and must not be enabled for Samba 4.x.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ctdb/">ctdb</a></code>(1), <code><a href="/docs/linux/man/1-ctdbd/">ctdbd</a></code>(1), <code><a href="/docs/linux/man/5-ctdbd-conf/">ctdbd.conf</a></code>(5), <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7), m[blue]<code><a rel="nofollow" href="http://ctdb.samba.org/">http://ctdb.samba.org/</a></code>m[]</p>
<h2>Author</h2>
<p>This documentation was written by Ronnie Sahlberg, Amitay Isaacs, Martin Schwenke</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2007 Andrew Tridgell, Ronnie Sahlberg </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, see m[blue]<code><a rel="nofollow" href="http://www.gnu.org/licenses">http://www.gnu.org/licenses</a></code>m[].</p>
