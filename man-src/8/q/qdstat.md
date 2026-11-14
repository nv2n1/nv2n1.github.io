---
title: "qdstat(8)"
name: "qdstat"
section: "8"
letter: "q"
url: "/docs/linux/man/8-qdstat/"
---

qdstat - dispatch router status

<h2>Synopsis</h2>

qdstat [options]

<h2>Description</h2>

<i>qdstat</i> shows status information about networks of Dispatch routers. It can display connections, network nodes and links, and router stats such as memory use.

<h2>Options</h2>

-h, --help : show this help message and exit 

 --version : Print version and exit. 

 -g, --general : Show General Router Stats 

 -c, --connections : Show Connections 

 -l, --links : Show Router Links 

 -n, --nodes : Show Router Nodes 

 -a, --address : Show Router Addresses 

 -m, --memory : Show Router Memory Stats 

 --autolinks : Show Auto Links 

 --linkroutes : Show Link Routes 

 -v, --verbose : Show maximum detail 

 --log : Show recent log entries 

 --limit=LIMIT : Limit number of log entries

<h3>Connection Options</h3>

-b URL, --bus=URL : URL of the messaging bus to connect to (default 

 -r ROUTER-ID, --router=ROUTER-ID : Router to be queried 

 -t SECS, --timeout=SECS : Maximum time to wait for connection in seconds (default 5) 

 --ssl-certificate=CERT : Client SSL certificate (PEM Format) 

 --ssl-key=KEY : Client SSL private key (PEM Format) 

 --ssl-trustfile=TRUSTED-CA-DB : Trusted Certificate Authority Database file (PEM Format) 

 --ssl-password=PASSWORD : Certificate password, will be prompted if not specifed.

<h2>Output Columns</h2>

<h3>qdstat -c</h3>

Id : Unique connection identifier 

 host : The hostname or internet address of the remotely connected AMQP container 

 container : The container-name of the remotely connected AMQP container 

 role : The configured role of the connection
<dl><dt>&bull;
<dd>normal - Normal connections from client to router
<dt>&bull;
<dd>inter-router - Connection between routers to form a network
<dt>&bull;
<dd>route-container - Connection to/from a Broker or other host to receive link-routes and waypoints 

 dir : The direction of connection establishment
<dt>&bull;
<dd>in - The connection was initiated by the remote container
<dt>&bull;
<dd>out - The connection was initiated by this router 

 security : A description of the security/encryption in effect for this connection 

 authentication : The method and user-id of the authenticated user for this connection</dl>

<h3>qdstat -l</h3>

type : Type of link
<dl><dt>&bull;
<dd>router-control - An inter-router link that is reserved for control messages exchanged between routers
<dt>&bull;
<dd>inter-router - An inter-router link that is used for normal message-routed deliveries
<dt>&bull;
<dd>endpoint - A normal link to an external endpoint container 

 dir : The direction of message flow on the link
<dt>&bull;
<dd>in - Deliveries flow inbound to the router
<dt>&bull;
<dd>out - Deliveries flow outbound from the router 

 conn id : Unique identifier of the connection over which this link is attached 

 id : Unique identifier of this link 

 peer : For link-routed links, the unique identifier of the peer link. In link routing, an inbound link is paired with an outbound link 

 class : Class of the address bound to the link 

 addr : The address bound to the link 

 phs : The phase of the address bound to the link 

 cap : The capacity, in deliveries, of the link 

 undel : The number of undelivered messages stored on the link's FIFO 

 unsettled : The number of unsettled deliveries being tracked by the link 

 deliveries : The total number of deliveries that have transited this link 

 admin : The administrative status of the link
<dt>&bull;
<dd>enabled - The link is enabled for normal operation
<dt>&bull;
<dd>disabled - The link is disabled and should be quiescing or stopped (not yet supported) 

 oper : The operational status of the link
<dt>&bull;
<dd>up - The link is operational
<dt>&bull;
<dd>down - The link is not attached
<dt>&bull;
<dd>quiescing - The link is in the process of quiescing (not yet supported)
<dt>&bull;
<dd>idle - The link has completed quiescing and is idle (not yet supported) 

 name : The link name (only shown if the -v option is provided)</dl>

<h3>qdstat -n</h3>

router-id : Identifier of the router 

 next-hop : If this router is not a neighbor, identifies the next-hop neighbor used to reach this router 

 link : Unique identifier of the link to the neighbor router 

 cost : The topology cost to this remote router (with -v option only) 

 neighbors : The list of neighbor routers (the router's link-state) (with -v option only) 

 valid-origins : The list of origin routers for which the best path to the listed router passes through this router (with -v option only)

<h3>qdstat -a</h3>

class : The class of the listed address
<dl><dt>&bull;
<dd>local - Address that is local to this router
<dt>&bull;
<dd>topo - Topological address used for router control messages
<dt>&bull;
<dd>router - A summary router address used to route messages to a remote router's local addresses
<dt>&bull;
<dd>mobile - A mobile address for an attached consumer or producer 

 addr : The address text 

 phs : For mobile addresses only, the phase of the address. Direct addresses have only a phase 0. Waypoint addresses have multiple phases, normally 0 and 1. 

 distrib : Distribution method used for this address
<dt>&bull;
<dd>multicast - A copy of each message is delivered once to each consumer for the address
<dt>&bull;
<dd>closest - Each message is delivered to only one consumer for the address. The closest (lowest cost) consumer will be chosen. If there are multiple lowest-cost consumers, deliveries will be spread across those consumers.
<dt>&bull;
<dd>balanced - Each message is delivered to only one consumer for the address. The consumer with the fewest outstanding (unsettled) deliveries will be chosen. The cost of the route to the consumer is a threshold for delivery (i.e. higher cost consumers will only receive deliveries if closer consumers are backed up).
<dt>&bull;
<dd>flood - Used only for router-control traffic. This is multicast without prevention of duplicate deliveries. 

 in-proc : The number of in-process consumers for this address 

 local : The number of local (on this router) consumers for this address 

 remote : The number of remote routers that have at least one consumer for this address 

 cntnr : The number of locally attached containers that are destinations for link-routes on this address 

 in : The number of deliveries for this address that entered the network on this router 

 out : The number of deliveries for this address that exited the network on this router 

 thru : The number of deliveries for this address that were forwarded to other routers 

 to-proc : The number of deliveries for this address that were delivered to an in-process consumer 

 from-proc : The number of deliveries for this address that were received from an in-process producer</dl>

<h3>qdstat --linkroutes</h3>

prefix : The prefix for matching addresses of routed links 

 dir : The direction (from the router's perspective) of matching links 

 distrib : The distribution method used for routed links
<dl><dt>&bull;
<dd>linkBalanced - the only supported distribution for routed links 

 status : Operational status of the link route
<dt>&bull;
<dd>active - Route is actively routing attaches (i.e. ready for use)
<dt>&bull;
<dd>inactive - Route is inactive because there is no local destination connected</dl>

<h3>qstat --autolinks</h3>

addr : The address of the auto link 

 dir : The direction of message flow for the auto link
<dl><dt>&bull;
<dd>in - Messages flow in from the route-container to the router network
<dt>&bull;
<dd>out - Messages flow out to the route-container from the router network 

 phs : Phase of the address for this auto link 

 link : Unique identifier of the link managed by this auto link 

 status : The operational status of this auto link
<dt>&bull;
<dd>inactive - There is no connected container for this auto link
<dt>&bull;
<dd>attaching - The link is attaching to the container
<dt>&bull;
<dd>failed - The link-attach failed
<dt>&bull;
<dd>active - The link is operational
<dt>&bull;
<dd>quiescing - The link is quiescing (not yet supported)
<dt>&bull;
<dd>idle - The link is idle (not yet supported) 

 lastErr : The description of the last attach failure that occurred on this auto link</dl>

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/8-qdrouterd/">qdrouterd</a>(8)</i>, <i><a HREF="/docs/linux/man/8-qdmanage/">qdmanage</a>(8)</i>, <i><a HREF="/docs/linux/man/5-qdrouterd-conf/">qdrouterd.conf</a>(5)</i> 

 <i><a rel="nofollow" HREF="http://qpid.apache.org/components/dispatch-router">http://qpid.apache.org/components/dispatch-router</a></i>

<h2>Copyright</h2>

2013, Apache Qpid &lt;<a rel="nofollow" HREF="http://qpid.apache.org/">http://qpid.apache.org/</a>&gt;
