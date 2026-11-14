---
title: "votequorum(5)"
name: "votequorum"
section: "5"
letter: "v"
url: "/docs/linux/man/5-votequorum/"
description: "votequorum – Votequorum Configuration Overview"
---

<p>votequorum &#8211; Votequorum Configuration Overview</p>
<h2>Overview</h2>
<p>The votequorum service is part of the corosync project. This service can be optionally loaded into the nodes of a corosync cluster to avoid split-brain situations. It does this by having a number of votes assigned to each system in the cluster and ensuring that only when a majority of the votes are present, cluster operations are allowed to proceed. The service must be loaded into all nodes or none. If it is loaded into a subset of cluster nodes the results will be unpredictable. </p>
<p> The following corosync.conf extract will enable votequorum service within corosync: </p>
<pre>quorum {
 provider: corosync_votequorum
}</pre>
<p>votequorum reads its configuration from corosync.conf. Some values can be changed at runtime, others are only read at corosync startup. It is very important that those values are consistent across all the nodes participating in the cluster or votequorum behavior will be unpredictable. </p>
<p> votequorum requires an expected_votes value to function, this can be provided in two ways. The number of expected votes will be automatically calculated when the nodelist { } section is present in corosync.conf or expected_votes can be specified in the quorum { } section. Lack of both will disable votequorum. If both are present at the same time, the quorum.expected_votes value will override the one calculated from the nodelist. </p>
<p> Example (no nodelist) of an 8 node cluster (each node has 1 vote): </p>
<pre>quorum { 
 provider: corosync_votequorum
 expected_votes: 8
}</pre>
<p>Example (with nodelist) of a 3 node cluster (each node has 1 vote): </p>
<pre>quorum { 
 provider: corosync_votequorum
} 
nodelist {
 node {
 ring0_addr: 192.168.1.1
 }
 node {
 ring0_addr: 192.168.1.2
 }
 node {
 ring0_addr: 192.168.1.3
 }
}</pre>
<h2>Special Features</h2>
<p><code>two_node: 1</code> </p>
<p> Enables two node cluster operations (default: 0). </p>
<p> The &quot;two node cluster&quot; is a use case that requires special consideration. With a standard two node cluster, each node with a single vote, there are 2 votes in the cluster. Using the simple majority calculation (50% of the votes + 1) to calculate quorum, the quorum would be 2. This means that the both nodes would always have to be alive for the cluster to be quorate and operate. </p>
<p> Enabling two_node: 1, quorum is set artificially to 1. </p>
<p> Example configuration 1: </p>
<pre>quorum {
 provider: corosync_votequorum
 expected_votes: 2
 two_node: 1
}</pre>
<p>Example configuration 2: </p>
<pre>quorum {
 provider: corosync_votequorum
 two_node: 1
}
nodelist {
 node {
 ring0_addr: 192.168.1.1
 }
 node {
 ring0_addr: 192.168.1.2
 }
}</pre>
<p>NOTES: enabling two_node: 1 automatically enables wait_for_all. It is still possible to override wait_for_all by explicitly setting it to 0. If more than 2 nodes join the cluster, the two_node option is automatically disabled. </p>
<p> <code>wait_for_all: 1</code> </p>
<p> Enables Wait For All (WFA) feature (default: 0). </p>
<p> The general behaviour of votequorum is to switch a cluster from inquorate to quorate as soon as possible. For example, in an 8 node cluster, where every node has 1 vote, expected_votes is set to 8 and quorum is (50% + 1) 5. As soon as 5 (or more) nodes are visible to each other, the partition of 5 (or more) becomes quorate and can start operating. </p>
<p> When WFA is enabled, the cluster will be quorate for the first time only after all nodes have been visible at least once at the same time. </p>
<p> This feature has the advantage of avoiding some startup race conditions, with the cost that all nodes need to be up at the same time at least once before the cluster can operate. </p>
<p> A common startup race condition based on the above example is that as soon as 5 nodes become quorate, with the other 3 still offline, the remaining 3 nodes will be fenced. </p>
<p> It is very useful when combined with last_man_standing (see below). </p>
<p> Example configuration: </p>
<pre>quorum {
 provider: corosync_votequorum
 expected_votes: 8
 wait_for_all: 1
}</pre>
<p><code>last_man_standing: 1</code> / <code>last_man_standing_window: 10000</code> </p>
<p> Enables Last Man Standing (LMS) feature (default: 0). Tunable last_man_standing_window (default: 10 seconds, expressed in ms). </p>
<p> The general behaviour of votequorum is to set expected_votes and quorum at startup (unless modified by the user at runtime, see below) and use those values during the whole lifetime of the cluster. </p>
<p> Using for example an 8 node cluster where each node has 1 vote, expected_votes is set to 8 and quorum to 5. This condition allows a total failure of 3 nodes. If a 4th node fails, the cluster becomes inquorate and it will stop providing services. </p>
<p> Enabling LMS allows the cluster to dynamically recalculate expected_votes and quorum under specific circumstances. It is essential to enable WFA when using LMS in High Availability clusters. </p>
<p> Using the above 8 node cluster example, with LMS enabled the cluster can retain quorum and continue operating by losing, in a cascade fashion, up to 6 nodes with only 2 remaining active. </p>
<p> Example chain of events: </p>
<pre>1) cluster is fully operational with 8 nodes.
 (expected_votes: 8 quorum: 5)
2) 3 nodes die, cluster is quorate with 5 nodes.
3) after last_man_standing_window timer expires,
 expected_votes and quorum are recalculated.
 (expected_votes: 5 quorum: 3)
4) at this point, 2 more nodes can die and
 cluster will still be quorate with 3.
5) once again, after last_man_standing_window
 timer expires expected_votes and quorum are
 recalculated.
 (expected_votes: 3 quorum: 2)
6) at this point, 1 more node can die and
 cluster will still be quorate with 2.
7) one more last_man_standing_window timer
 (expected_votes: 2 quorum: 2)</pre>
<p>NOTES: In order for the cluster to downgrade automatically from 2 nodes to a 1 node cluster, the auto_tie_breaker feature must also be enabled (see below). If auto_tie_breaker is not enabled, and one more failure occours, the remaining node will not be quorate. LMS does not work with asymmetric voting schemes, each node must vote 1. LMS is also incompatible with quorum devices, if last_man_standing is specified in corosync.conf then the quorum device will be disabled. </p>
<p> Example configuration 1: </p>
<pre>quorum {
 provider: corosync_votequorum
 expected_votes: 8
 last_man_standing: 1
}</pre>
<p>Example configuration 2 (increase timeout to 20 seconds): </p>
<pre>quorum {
 provider: corosync_votequorum
 expected_votes: 8
 last_man_standing: 1
 last_man_standing_window: 20000
}</pre>
<p><code>auto_tie_breaker: 1</code> </p>
<p> Enables Auto Tie Breaker (ATB) feature (default: 0). </p>
<p> The general behaviour of votequorum allows a simultaneous node failure up to 50% &#8211; 1 node, assuming each node has 1 vote. </p>
<p> When ATB is enabled, the cluster can suffer up to 50% of the nodes failing at the same time, in a deterministic fashion. By default the cluster partition, or the set of nodes that are still in contact with the node that has the lowest nodeid will remain quorate. The other nodes will be inquorate. This behaviour can be changed by also specifying </p>
<p> <code>auto_tie_breaker_node: lowest|highest|&lt;list of node IDs&gt;</code> </p>
<p> &#8216;lowest&#8217; is the default, &#8216;highest&#8217; is similar in that if the current set of nodes contains the highest nodeid then it will remain quorate. Alternatively it is possible to specify a particular node ID or list of node IDs that will be required to maintain quorum. If a (space-separated) list is given, the nodes are evaluated in order, so if the first node is present then it will be used to determine the quorate partition, if that node is not in either half (ie was not in the cluster before the split) then the second node ID will be checked for and so on. ATB is incompatible with quorum devices &#8211; if auto_tie_breaker is specified in corosync.conf then the quorum device will be disabled. </p>
<p> Example configuration 1: </p>
<pre>quorum {
 provider: corosync_votequorum
 expected_votes: 8
 auto_tie_breaker: 1
 auto_tie_breaker_node: lowest
}</pre>
<p>Example configuration 2: </p>
<pre>quorum {
 provider: corosync_votequorum
 expected_votes: 8
 auto_tie_breaker: 1
 auto_tie_breaker_node: 1 3 5
}</pre>
<p><code>allow_downscale: 1</code> </p>
<p> Enables allow downscale (AD) feature (default: 0). </p>
<p> THIS FEATURE IS INCOMPLETE AND CURRENTLY UNSUPPORTED. </p>
<p> The general behaviour of votequorum is to never decrease expected votes or quorum. </p>
<p> When AD is enabled, both expected votes and quorum are recalculated when a node leaves the cluster in a clean state (normal corosync shutdown process) down to configured expected_votes. </p>
<p> Example use case: </p>
<pre>1) N node cluster (where N is any value higher than 3)
2) expected_votes set to 3 in corosync.conf
3) only 3 nodes are running
4) admin requires to increase processing power and adds 10 nodes
5) internal expected_votes is automatically set to 13
6) minimum expected_votes is 3 (from configuration)
- up to this point this is standard votequorum behavior -
7) once the work is done, admin wants to remove nodes from the cluster
8) using an ordered shutdown the admin can reduce the cluster size
 automatically back to 3, but not below 3, where normal quorum
 operation will work as usual.</pre>
<p>Example configuration: </p>
<pre>quorum {
 provider: corosync_votequorum
 expected_votes: 3
 allow_downscale: 1
}</pre>
<p>allow_downscale implicitly enabled EVT (see below). </p>
<p> <code>expected_votes_tracking: 1</code> </p>
<p> Enables Expected Votes Tracking (EVT) feature (default: 0). </p>
<p> Expected Votes Tracking stores the highest-seen value of expected votes on disk and uses that as the minimum value for expected votes in the absence of any higher authority (eg a current quorate cluster). This is useful for when a group of nodes becomes detached from the main cluster and after a restart could have enough votes to provide quorum, which can happen after using allow_downscale. </p>
<p> Note that even if the in-memory version of expected_votes is reduced, eg by removing nodes or using corosync-quorumtool, the stored value will still be the highest value seen &#8211; it never gets reduced. </p>
<p> The value is held in the file /var/lib/corosync/ev_tracking which can be deleted if you really do need to reduce the expected votes for any reason, like the node has been moved to a different cluster.</p>
<h2>Various Notes</h2>
<p>* WFA / LMS / ATB / AD can be used combined together. </p>
<p> * In order to change the default votes for a node there are two options: </p>
<pre>1) nodelist:
nodelist {
 node {
 ring0_addr: 192.168.1.1
 quorum_votes: 3
 }
 ....
}
2) quorum section (deprecated):
quorum {
 provider: corosync_votequorum
 expected_votes: 2
 votes: 2
}</pre>
<p>In the event that both nodelist and quorum { votes: } are defined, the value from the nodelist will be used. </p>
<p> * Only votes, quorum_votes, expected_votes and two_node can be changed at runtime. Everything else requires a cluster restart.</p>
<h2>Bugs</h2>
<p>No known bugs at the time of writing. The authors are from outerspace. Deal with it.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-corosync/">corosync</a></code>(8), <code><a href="/docs/linux/man/5-corosync-conf/">corosync.conf</a></code>(5), <code><a href="/docs/linux/man/8-corosync-quorumtool/">corosync-quorumtool</a></code>(8), <code><a href="/docs/linux/man/8-votequorum_overview/">votequorum_overview</a></code>(8) </p>
