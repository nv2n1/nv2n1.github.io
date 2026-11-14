---
title: "qdisk(5)"
name: "qdisk"
section: "5"
letter: "q"
url: "/docs/linux/man/5-qdisk/"
description: "qdisk – a disk-based quorum daemon for CMAN / Linux-Cluster"
---

<p>qdisk &#8211; a disk-based quorum daemon for CMAN / Linux-Cluster</p>
<h2>1. Overview</h2>
<h2>1.1 Problem</h2>
<p>In some situations, it may be necessary or desirable to sustain a majority node failure of a cluster without introducing the need for asymmetric cluster configurations (e.g. client-server, or heavily-weighted voting nodes).</p>
<h2>1.2. Design Requirements</h2>
<p>* Ability to sustain 1..(n-1)/n simultaneous node failures, without the danger of a simple network partition causing a split brain. That is, we need to be able to ensure that the majority failure case is not merely the result of a network partition. </p>
<p> * Ability to use external reasons for deciding which partition is the the quorate partition in a partitioned cluster. For example, a user may have a service running on one node, and that node must always be the master in the event of a network partition. Or, a node might lose all network connectivity except the cluster communication path &#8211; in which case, a user may wish that node to be evicted from the cluster. </p>
<p> * Integration with CMAN. We must not require CMAN to run with us (or without us). Linux-Cluster does not require a quorum disk normally &#8211; introducing new requirements on the base of how Linux-Cluster operates is not allowed. </p>
<p> * Data integrity. In order to recover from a majority failure, fencing is required. The fencing subsystem is already provided by Linux-Cluster. </p>
<p> * Non-reliance on hardware or protocol specific methods (i.e. SCSI reservations). This ensures the quorum disk algorithm can be used on the widest range of hardware configurations possible. </p>
<p> * Little or no memory allocation after initialization. In critical paths during failover, we do not want to have to worry about being killed during a memory pressure situation because we request a page fault, and the Linux OOM killer responds&#8230;</p>
<h2>1.3. Hardware Considerations and Requirements</h2>
<h2>1.3.1. Concurrent, Synchronous, Read/Write Access</h2>
<p>This quorum daemon requires a shared block device with concurrent read/write access from all nodes in the cluster. The shared block device can be a multi-port SCSI RAID array, a Fiber-Channel RAID SAN, a RAIDed iSCSI target, or even GNBD. The quorum daemon uses O_DIRECT to write to the device.</p>
<h2>1.3.2. Bargain-basement JBODs need not apply</h2>
<p>There is a minimum performance requirement inherent when using disk-based cluster quorum algorithms, so design your cluster accordingly. Using a cheap JBOD with old SCSI2 disks on a multi-initiator bus will cause problems at the first load spike. Plan your loads accordingly; a node&#8217;s inability to write to the quorum disk in a timely manner will cause the cluster to evict the node. Using host-RAID or multi-initiator parallel SCSI configurations with the qdisk daemon is unlikely to work, and will probably cause administrators a lot of frustration. That having been said, because the timeouts are configurable, most hardware should work if the timeouts are set high enough.</p>
<h2>1.3.3. Fencing is Required</h2>
<p>In order to maintain data integrity under all failure scenarios, use of this quorum daemon requires adequate fencing, preferably power-based fencing. Watchdog timers and software-based solutions to reboot the node internally, while possibly sufficient, are not considered &#8216;fencing&#8217; for the purposes of using the quorum disk.</p>
<h2>1.4. Limitations</h2>
<p>* At this time, this daemon supports a maximum of 16 nodes. This is primarily a scalability issue: As we increase the node count, we increase the amount of synchronous I/O contention on the shared quorum disk. </p>
<p> * Cluster node IDs must be statically configured in cluster.conf and must be numbered from 1..16 (there can be gaps, of course). </p>
<p> * Cluster node votes must all be 1. </p>
<p> * CMAN must be running before the qdisk program can operate in full capacity. If CMAN is not running, qdisk will wait for it. </p>
<p> * CMAN&#8217;s eviction timeout should be at least 2x the quorum daemon&#8217;s to give the quorum daemon adequate time to converge on a master during a failure + load spike situation. See section 3.3.1 for specific details. </p>
<p> * For &#8216;all-but-one&#8217; failure operation, the total number of votes assigned to the quorum device should be equal to or greater than the total number of node-votes in the cluster. While it is possible to assign only one (or a few) votes to the quorum device, the effects of doing so have not been explored. </p>
<p> * For &#8216;tiebreaker&#8217; operation in a two-node cluster, unset CMAN&#8217;s two_node flag (or set it to 0), set CMAN&#8217;s expected votes to &#8216;3&#8217;, set each node&#8217;s vote to &#8216;1&#8217;, and leave qdisk&#8217;s vote count unset. This will allow the cluster to operate if either both nodes are online, or a single node &amp; the heuristics. </p>
<p> * Currently, the quorum disk daemon is difficult to use with CLVM if the quorum disk resides on a CLVM logical volume. CLVM requires a quorate cluster to correctly operate, which introduces a chicken-and-egg problem for starting the cluster: CLVM needs quorum, but the quorum daemon needs CLVM (if and only if the quorum device lies on CLVM-managed storage). One way to work around this is to *not* set the cluster&#8217;s expected votes to include the quorum daemon&#8217;s votes. Bring all nodes online, and start the quorum daemon *after* the whole cluster is running. This will allow the expected votes to increase naturally.</p>
<h2>2. Algorithms</h2>
<h2>2.1. Heartbeating &amp; Liveliness Determination</h2>
<p>Nodes update individual status blocks on the quorum disk at a user- defined rate. Each write of a status block alters the timestamp, which is what other nodes use to decide whether a node has hung or not. If, after a user-defined number of &#8216;misses&#8217; (that is, failure to update a timestamp), a node is declared offline. After a certain number of &#8216;hits&#8217; (changed timestamp + &quot;i am alive&quot; state), the node is declared online. </p>
<p> The status block contains additional information, such as a bitmask of the nodes that node believes are online. Some of this information is used by the master &#8211; while some is just for performance recording, and may be used at a later time. The most important pieces of information a node writes to its status block are: </p>
<p> &#8211; Timestamp<br />
 &#8211; Internal state (available / not available)<br />
 &#8211; Score<br />
 &#8211; Known max score (may be used in the future to detect invalid configurations)<br />
 &#8211; Vote/bid messages<br />
 &#8211; Other nodes it thinks are online</p>
<h2>2.2. Scoring &amp; Heuristics</h2>
<p>The administrator can configure up to 10 purely arbitrary heuristics, and must exercise caution in doing so. At least one administrator- defined heuristic is required for operation, but it is generally a good idea to have more than one heuristic. By default, only nodes scoring over 1/2 of the total maximum score will claim they are available via the quorum disk, and a node (master or otherwise) whose score drops too low will remove itself (usually, by rebooting). </p>
<p> The heuristics themselves can be any command executable by &#8216;sh -c&#8217;. For example, in early testing the following was used: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> &lt;<code>heuristic </code><i>program</i><code>=&quot;</code>[ -f /quorum ]<code>&quot; </code><i>score</i><code>=&quot;</code>10<code>&quot; </code><i>interval</i><code>=&quot;</code>2<code>&quot;/&gt;</code> </p>
<p> This is a literal sh-ism which tests for the existence of a file called &quot;/quorum&quot;. Without that file, the node would claim it was unavailable. This is an awful example, and should never, ever be used in production, but is provided as an example as to what one could do&#8230; </p>
<p> Typically, the heuristics should be snippets of shell code or commands which help determine a node&#8217;s usefulness to the cluster or clients. Ideally, you want to add traces for all of your network paths (e.g. check links, or ping routers), and methods to detect availability of shared storage.</p>
<h2>2.3. Master Election</h2>
<p>Only one master is present at any one time in the cluster, regardless of how many partitions exist within the cluster itself. The master is elected by a simple voting scheme in which the lowest node which believes it is capable of running (i.e. scores high enough) bids for master status. If the other nodes agree, it becomes the master. This algorithm is run whenever no master is present. </p>
<p> If another node comes online with a lower node ID while a node is still bidding for master status, it will rescind its bid and vote for the lower node ID. If a master dies or a bidding node dies, the voting algorithm is started over. The voting algorithm typically takes two passes to complete. </p>
<p> Master deaths take marginally longer to recover from than non-master deaths, because a new master must be elected before the old master can be evicted &amp; fenced.</p>
<h2>2.4. Master Duties</h2>
<p>The master node decides who is or is not in the master partition, as well as handles eviction of dead nodes (both via the quorum disk and via the linux-cluster fencing system by using the cman_kill_node() API).</p>
<h2>2.5. How it All Ties Together</h2>
<p>When a master is present, and if the master believes a node to be online, that node will advertise to CMAN that the quorum disk is available. The master will only grant a node membership if: </p>
<p> (a) CMAN believes the node to be online, and (b) that node has made enough consecutive, timely writes to the quorum disk, and (c) the node has a high enough score to consider itself online.</p>
<h2>3. Configuration</h2>
<h2>3.1. The &lt;quorumd&gt; tag</h2>
<p>This tag is a child of the top-level &lt;cluster&gt; tag. </p>
<p> <code>&lt;quorumd</code> <i>interval</i><code>=&quot;</code>1<code>&quot;</code> This is the frequency of read/write cycles, in seconds. </p>
<p> <i>tko</i><code>=&quot;</code>10<code>&quot;</code> This is the number of cycles a node must miss in order to be declared dead. The default for this number is dependent on the configured token timeout. </p>
<p> <i>tko_up</i><code>=&quot;</code>X<code>&quot;</code> This is the number of cycles a node must be seen in order to be declared online. Default is <code>floor(tko/3)</code>. </p>
<p> <i>upgrade_wait</i><code>=&quot;</code>2<code>&quot;</code> This is the number of cycles a node must wait before initiating a bid for master status after heuristic scoring becomes sufficient. The default is 2. This can not be set to 0, and should not exceed <code>tko</code>. </p>
<p> <i>master_wait</i><code>=&quot;</code>X<code>&quot;</code> This is the number of cycles a node must wait for votes before declaring itself master after making a bid. Default is <code>floor(tko/2)</code>. This can not be less than 2, must be greater than tko_up, and should not exceed <code>tko</code>. </p>
<p> <i>votes</i><code>=&quot;</code>3<code>&quot;</code> This is the number of votes the quorum daemon advertises to CMAN when it has a high enough score. The default is the number of nodes in the cluster minus 1. For example, in a 4 node cluster, the default is 3. This value may change during normal operation, for example when adding or removing a node from the cluster. </p>
<p> <i>log_level</i><code>=&quot;</code>4<code>&quot;</code> This controls the verbosity of the quorum daemon in the system logs. 0 = emergencies; 7 = debug. This option is deprecated. </p>
<p> <i>log_facility</i><code>=&quot;</code>daemon<code>&quot;</code> This controls the syslog facility used by the quorum daemon when logging. For a complete list of available facilities, see <code><a href="/docs/linux/man/5-syslog-conf/">syslog.conf</a>(5)</code>. The default value for this is &#8216;daemon&#8217;. This option is deprecated. </p>
<p> <i>status_file</i><code>=&quot;</code>/foo<code>&quot;</code> Write internal states out to this file periodically (&quot;-&quot; = use stdout). This is primarily used for debugging. The default value for this attribute is undefined. This option can be changed while qdiskd is running. </p>
<p> <i>min_score</i><code>=&quot;</code>3<code>&quot;</code> Absolute minimum score to be consider one&#8217;s self &quot;alive&quot;. If omitted, or set to 0, the default function &quot;floor((n+1)/2)&quot; is used, where <i>n</i> is the total of all of defined heuristics&#8217; <i>score</i> attribute. This must never exceed the sum of the heuristic scores, or else the quorum disk will never be available. </p>
<p> <i>reboot</i><code>=&quot;</code>1<code>&quot;</code> If set to 0 (off), qdiskd will *not* reboot after a negative transition as a result in a change in score (see section 2.2). The default for this value is 1 (on). This option can be changed while qdiskd is running. </p>
<p> <i>master_wins</i><code>=&quot;</code>0<code>&quot;</code> If set to 1 (on), only the qdiskd master will advertise its votes to CMAN. In a network partition, only the qdisk master will provide votes to CMAN. Consequently, that node will automatically &quot;win&quot; in a fence race. </p>
<p> This option requires careful tuning of the CMAN timeout, the qdiskd timeout, and CMAN&#8217;s quorum_dev_poll value. As a rule of thumb, CMAN&#8217;s quorum_dev_poll value should be equal to Totem&#8217;s token timeout and qdiskd&#8217;s timeout (interval*tko) should be less than half of Totem&#8217;s token timeout. See section 3.3.1 for more information. </p>
<p> This option only takes effect if there are no heuristics configured. Usage of this option in configurations with more than two cluster nodes is undefined and should not be done. </p>
<p> In a two-node cluster with no heuristics and no defined vote count (see above), this mode is turned by default. If enabled in this way at startup and a node is later added to the cluster configuration or the vote count is set to a value other than 1, this mode will be disabled. </p>
<p> <i>allow_kill</i><code>=&quot;</code>1<code>&quot;</code> If set to 0 (off), qdiskd will *not* instruct to kill nodes it thinks are dead (as a result of not writing to the quorum disk). The default for this value is 1 (on). This option can be changed while qdiskd is running. </p>
<p> <i>paranoid</i><code>=&quot;</code>0<code>&quot;</code> If set to 1 (on), qdiskd will watch internal timers and reboot the node if it takes more than (interval * tko) seconds to complete a quorum disk pass. The default for this value is 0 (off). This option can be changed while qdiskd is running. </p>
<p> <i>io_timeout</i><code>=&quot;</code>0<code>&quot;</code> If set to 1 (on), qdiskd will watch internal timers and reboot the node if qdisk is not able to write to disk after (interval * tko) seconds. The default for this value is 0 (off). If io_timeout is active max_error_cycles is overridden and set to off. </p>
<p> <i>scheduler</i><code>=&quot;</code>rr<code>&quot;</code> Valid values are &#8216;rr&#8217;, &#8216;fifo&#8217;, and &#8216;other&#8217;. Selects the scheduling queue in the Linux kernel for operation of the main &amp; score threads (does not affect the heuristics; they are always run in the &#8216;other&#8217; queue). Default is &#8216;rr&#8217;. See <a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a>(2) for more details. </p>
<p> <i>priority</i><code>=&quot;</code>1<code>&quot;</code> Valid values for &#8216;rr&#8217; and &#8216;fifo&#8217; are 1..100 inclusive. Valid values for &#8216;other&#8217; are -20..20 inclusive. Sets the priority of the main &amp; score threads. The default value is 1 (in the RR and FIFO queues, higher numbers denote higher priority; in OTHER, lower values denote higher priority). This option can be changed while qdiskd is running. </p>
<p> <i>stop_cman</i><code>=&quot;</code>0<code>&quot;</code> Ordinarily, cluster membership is left up to CMAN, not qdisk. If this parameter is set to 1 (on), qdiskd will tell CMAN to leave the cluster if it is unable to initialize the quorum disk during startup. This can be used to prevent cluster participation by a node which has been disconnected from the SAN. The default for this value is 0 (off). This option can be changed while qdiskd is running. </p>
<p> <i>use_uptime</i><code>=&quot;</code>1<code>&quot;</code> If this parameter is set to 1 (on), qdiskd will use values from /proc/uptime for internal timings. This is a bit less precise than <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a>(2)</code>, but the benefit is that changing the system clock will not affect qdiskd&#8217;s behavior &#8211; even if <code>paranoid</code> is enabled. If set to 0, qdiskd will use <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a>(2)</code>, which is more precise. The default for this value is 1 (on / use uptime). </p>
<p> <i>device</i><code>=&quot;</code>/dev/sda1<code>&quot;</code> This is the device the quorum daemon will use. This device must be the same on all nodes. </p>
<p> <i>label</i><code>=&quot;</code>mylabel<code>&quot;</code> This overrides the device field if present. If specified, the quorum daemon will read /proc/partitions and check for qdisk signatures on every block device found, comparing the label against the specified label. This is useful in configurations where the block device name differs on a per-node basis. </p>
<p> <i>cman_label</i><code>=&quot;</code>mylabel<code>&quot;</code> This overrides the label advertised to CMAN if present. If specified, the quorum daemon will register with this name instead of the actual device name. </p>
<p> <i>max_error_cycles</i><code>=&quot;</code>0<code>&quot;/&gt;</code> If we receive an I/O error during a cycle, we do not poll CMAN and tell it we are alive. If specified, this value will cause qdiskd to exit after the specified number of consecutive cycles during which I/O errors occur. The default is 0 (no maximum). This option can be changed while qdiskd is running. This option is ignored if io_timeout is set to 1. </p>
<p> <code>/&gt;</code></p>
<h2>3.3.1. Quorum Disk Timings</h2>
<p>Qdiskd should not be used in environments requiring failure detection times of less than approximately 10 seconds. </p>
<p> Qdiskd will attempt to automatically configure timings based on the totem timeout and the TKO. If configuring manually, Totem&#8217;s token timeout <code>must</code> be set to a value at least 1 interval greater than the the following function: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>interval&nbsp;<wbr>*&nbsp;<wbr>(tko&nbsp;<wbr>+&nbsp;<wbr>master_wait&nbsp;<wbr>+&nbsp;<wbr>upgrade_wait) </p>
<p> So, if you have an interval of 2, a tko of 7, master_wait of 2 and upgrade_wait of 2, the token timeout should be at least 24 seconds (24000 msec). </p>
<p> It is recommended to have at least 3 intervals to reduce the risk of quorum loss during heavy I/O load. As a rule of thumb, using a totem timeout more than 2x of qdiskd&#8217;s timeout will result in good behavior. </p>
<p> An improper timing configuration will cause CMAN to give up on qdiskd, causing a temporary loss of quorum during master transition.</p>
<h2>3.2. The &lt;heuristic&gt; tag</h2>
<p>This tag is a child of the &lt;quorumd&gt; tag. Heuristics may not be changed while qdiskd is running. </p>
<p> <code>&lt;heuristic</code> <i>program</i><code>=&quot;</code>/test.sh<code>&quot;</code> This is the program used to determine if this heuristic is alive. This can be anything which may be executed by <i>/bin/sh -c</i>. A return value of zero indicates success; anything else indicates failure. This is required. </p>
<p> <i>score</i><code>=&quot;</code>1<code>&quot;</code> This is the weight of this heuristic. Be careful when determining scores for heuristics. The default score for each heuristic is 1. </p>
<p> <i>interval</i><code>=&quot;</code>2<code>&quot;</code> This is the frequency (in seconds) at which we poll the heuristic. The default interval is determined by the qdiskd timeout. </p>
<p> <i>tko</i><code>=&quot;</code>1<code>&quot;</code> After this many failed attempts to run the heuristic, it is considered DOWN, and its score is removed. The default tko for each heuristic is determined by the qdiskd timeout. <code>/&gt;</code></p>
<h2>3.3. Examples</h2>
<h2>3.3.1. 3 cluster nodes &amp; 3 routers</h2>
<p>&lt;cman expected_votes=&quot;6&quot; &#8230;/&gt;<br />
 &lt;clusternodes&gt; &lt;clusternode name=&quot;node1&quot; votes=&quot;1&quot; &#8230; /&gt;<br />
 &lt;clusternode name=&quot;node2&quot; votes=&quot;1&quot; &#8230; /&gt;<br />
 &lt;clusternode name=&quot;node3&quot; votes=&quot;1&quot; &#8230; /&gt; &lt;/clusternodes&gt;<br />
 &lt;quorumd interval=&quot;1&quot; tko=&quot;10&quot; votes=&quot;3&quot; label=&quot;testing&quot;&gt; &lt;heuristic program=&quot;ping A -c1 -t1&quot; score=&quot;1&quot; interval=&quot;2&quot; tko=&quot;3&quot;/&gt;<br />
 &lt;heuristic program=&quot;ping B -c1 -t1&quot; score=&quot;1&quot; interval=&quot;2&quot; tko=&quot;3&quot;/&gt;<br />
 &lt;heuristic program=&quot;ping C -c1 -t1&quot; score=&quot;1&quot; interval=&quot;2&quot; tko=&quot;3&quot;/&gt;<br />
 &lt;/quorumd&gt;</p>
<h2>3.3.2. 2 cluster nodes &amp; 1 IP tiebreaker</h2>
<p>&lt;cman two_node=&quot;0&quot; expected_votes=&quot;3&quot; &#8230;/&gt;<br />
 &lt;clusternodes&gt; &lt;clusternode name=&quot;node1&quot; votes=&quot;1&quot; &#8230; /&gt;<br />
 &lt;clusternode name=&quot;node2&quot; votes=&quot;1&quot; &#8230; /&gt; &lt;/clusternodes&gt;<br />
 &lt;quorumd interval=&quot;1&quot; tko=&quot;10&quot; votes=&quot;1&quot; label=&quot;testing&quot;&gt; &lt;heuristic program=&quot;ping A -c1 -t1&quot; score=&quot;1&quot; interval=&quot;2&quot; tko=&quot;3&quot;/&gt;<br />
 &lt;/quorumd&gt;</p>
<h2>3.4. Heuristic score considerations</h2>
<p>* Heuristic timeouts should be set high enough to allow the previous run of a given heuristic to complete. </p>
<p> * Heuristic scripts returning anything except 0 as their return code are considered failed. </p>
<p> * The worst-case for improperly configured quorum heuristics is a race to fence where two partitions simultaneously try to kill each other.</p>
<h2>3.5. Creating a quorum disk partition</h2>
<p>The mkqdisk utility can create and list currently configured quorum disks visible to the local node; see <code><a href="/docs/linux/man/8-mkqdisk/">mkqdisk</a>(8)</code> for more details.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-mkqdisk/">mkqdisk</a>(8), <a href="/docs/linux/man/8-qdiskd/">qdiskd</a>(8), <a href="/docs/linux/man/5-cman/">cman</a>(5), <a href="/docs/linux/man/5-syslog-conf/">syslog.conf</a>(5), <a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a>(2) </p>
