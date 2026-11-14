---
title: "ip-nexthop(8)"
name: "ip-nexthop"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-nexthop/"
description: "ip-nexthop – nexthop object management"
---

<p>ip-nexthop &#8211; nexthop object management</p>
<h2>Synopsis</h2>
<pre><code>ip

[ ip-OPTIONS ]

nexthop

{ COMMAND |

    help }
</code></pre>
<p> <code>ip nexthop</code> { <code>show</code> | <code>flush</code> } <i>SELECTOR</i><br />
 <code>ip nexthop</code> { <code>add</code> | <code>replace</code> } id <i>ID</i> <i>NH</i><br />
 <code>ip nexthop</code> { <code>get</code> | <code>del</code> } id <i>ID</i><br />
 <code>ip nexthop bucket list </code><i>BUCKET_SELECTOR</i><br />
 <code>ip nexthop bucket get </code>id <i>ID</i> index <i>INDEX</i> </p>
<pre><code>SELECTOR :=

[ id

ID ] [

dev

DEV ] [

vrf

NAME ] [

master

DEV ] [

groups ] [

fdb ]
BUCKET_SELECTOR :=

SELECTOR

| [ nhid

ID ]
NH := {

    blackhole | [

    via

    ADDRESS ] [

    dev

    DEV ] [

    onlink ] [

    encap

    ENCAP ] [

    fdb ] |

    group

    GROUP [

    fdb ] [

    type

    TYPE [ TYPE_ARGS ] ] }
ENCAP := [

ENCAP_MPLS ]
ENCAP_MPLS :=

mpls [

LABEL ] [

ttl

TTL ]
GROUP :=

id[,weight[/...]
TYPE := {

    mpath | resilient }
TYPE_ARGS := [

RESILIENT_ARGS ]
RESILIENT_ARGS :=

[ buckets

BUCKETS ] [

idle_timer

IDLE ] [

unbalanced_timer

UNBALANCED ]
</code></pre>
<h2>Description</h2>
<p><code>ip nexthop</code> is used to manipulate entries in the kernel&#8217;s nexthop tables.</p>
<dl>
<dt>ip nexthop add id ID</p>
<dd>add new nexthop entry</p>
<dt>ip nexthop replace id ID</p>
<dd>change the configuration of a nexthop or add new one</p>
<dl>
<dd>
<dl>
<dt><code>via</code><i> [ FAMILY ] ADDRESS</i></p>
<dd>the address of the nexthop router, in the address family FAMILY. Address family must match address family of nexthop instance.</p>
<dt><code>dev</code><i> NAME</i></p>
<dd>is the output device.</p>
<dt><code>onlink</code></p>
<dd>pretend that the nexthop is directly attached to this link, even if it does not match any interface prefix.</p>
<dt><code>encap</code><i> ENCAPTYPE ENCAPHDR</i></p>
<dd>attach tunnel encapsulation attributes to this route. <i>ENCAPTYPE</i> is a string specifying the supported encapsulation type. Namely: <code>mpls</code> &#8211; encapsulation type MPLS <i>ENCAPHDR</i> is a set of encapsulation attributes specific to the <i>ENCAPTYPE.</i> <code>mpls</code> <i>MPLSLABEL</i> &#8211; mpls label stack with labels separated by <i>/</i> <code>ttl</code> <i>TTL</i> &#8211; TTL to use for MPLS header or 0 to inherit from IP header</p>
<dt><code>group</code><i> GROUP [ </i><code>type</code><i> TYPE [ TYPE_ARGS ] ]</i></p>
<dd>create a nexthop group. Group specification is id with an optional weight (id,weight) and a &#8216;/&#8217; as a separator between entries. <i>TYPE</i> is a string specifying the nexthop group type. Namely: <code>mpath</code> &#8211; Multipath nexthop group backed by the hash-threshold algorithm. The default when the type is unspecified. <code>resilient</code> &#8211; Resilient nexthop group. Group is resilient to addition and deletion of nexthops. <i>TYPE_ARGS</i> is a set of attributes specific to the <i>TYPE.</i> <code>resilient</code> <code>buckets</code> <i>BUCKETS</i> &#8211; Number of nexthop buckets. Cannot be changed for an existing group <code>idle_timer</code> <i>IDLE</i> &#8211; Time in seconds in which a nexthop bucket does not see traffic and is therefore considered idle. Default is 120 seconds <code>unbalanced_timer</code> <i>UNBALANCED</i> &#8211; Time in seconds in which a nexthop group is unbalanced and is therefore considered unbalanced. The kernel will try to rebalance unbalanced groups, which might result in some flows being reset. A value of 0 means that no rebalancing will take place. Default is 0 seconds</p>
<dt><code>blackhole</code></p>
<dd>create a blackhole nexthop</p>
<dt><code>fdb</code></p>
<dd>nexthop and nexthop groups for use with layer-2 fdb entries. A fdb nexthop group can only have fdb nexthops. Example: Used to represent a vxlan remote vtep ip. layer-2 vxlan fdb entry pointing to an ecmp nexthop group containing multiple remote vtep ips.</dl>
</dl>
<dt>ip nexthop delete id ID</p>
<dd>delete nexthop with given id.</p>
<dt>ip nexthop show</p>
<dd>show the contents of the nexthop table or the nexthops selected by some criteria.</p>
<dl>
<dd>
<dl>
<dt><code>dev</code><i> DEV </i></p>
<dd>show the nexthops using the given device.</p>
<dt><code>vrf</code><i> NAME </i></p>
<dd>show the nexthops using devices associated with the vrf name</p>
<dt><code>master</code><i> DEV </i></p>
<dd>show the nexthops using devices enslaved to given master device</p>
<dt><code>groups</code></p>
<dd>show only nexthop groups</p>
<dt><code>fdb</code></p>
<dd>show only fdb nexthops and nexthop groups</dl>
</dl>
<dt>ip nexthop flush</p>
<dd>flushes nexthops selected by some criteria. Criteria options are the same as show.</p>
<dt>ip nexthop get id ID</p>
<dd>get a single nexthop by id</p>
<dt>ip nexthop bucket show</p>
<dd>show the contents of the nexthop bucket table or the nexthop buckets selected by some criteria.</p>
<dl>
<dd>
<dl>
<dt><code>id</code><i> ID </i></p>
<dd>show the nexthop buckets that belong to a nexthop group with a given id</p>
<dt><code>nhid</code><i> ID </i></p>
<dd>show the nexthop buckets that hold a nexthop with a given id</p>
<dt><code>dev</code><i> DEV </i></p>
<dd>show the nexthop buckets using the given device</p>
<dt><code>vrf</code><i> NAME </i></p>
<dd>show the nexthop buckets using devices associated with the vrf name</p>
<dt><code>master</code><i> DEV </i></p>
<dd>show the nexthop buckets using devices enslaved to given master device</dl>
</dl>
<dt>ip nexthop bucket get id ID index INDEX</p>
<dd>get a single nexthop bucket by nexthop group id and bucket index </p>
<h2>Examples</h2>
<p>ip nexthop ls</p>
<dl>
<dd>Show all nexthop entries in the kernel.</dl>
<p> ip nexthop add id 1 via 192.168.1.1 dev eth0</p>
<dl>
<dd>Adds an IPv4 nexthop with id 1 using the gateway 192.168.1.1 out device eth0.</dl>
<p> ip nexthop add id 2 encap mpls 200/300 via 10.1.1.1 dev eth0</p>
<dl>
<dd>Adds an IPv4 nexthop with mpls encapsulation attributes attached to it.</dl>
<p> ip nexthop add id 3 group 1/2</p>
<dl>
<dd>Adds a nexthop with id 3. The nexthop is a group using nexthops with ids 1 and 2 at equal weight.</dl>
<p> ip nexthop add id 4 group 1,5/2,11</p>
<dl>
<dd>Adds a nexthop with id 4. The nexthop is a group using nexthops with ids 1 and 2 with nexthop 1 at weight 5 and nexthop 2 at weight 11.</dl>
<p> ip nexthop add id 5 via 192.168.1.2 fdb</p>
<dl>
<dd>Adds a fdb nexthop with id 5.</dl>
<p> ip nexthop add id 7 group 5/6 fdb</p>
<dl>
<dd>Adds a fdb nexthop group with id 7. A fdb nexthop group can only have fdb nexthops.</dl>
<p> ip nexthop add id 10 group 1/2 type resilient buckets 32</p>
<dl>
<dd>Add a resilient nexthop group with id 10 and 32 nexthop buckets.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) </p>
<h2>Author</h2>
<p>Original Manpage by David Ahern &lt;dsahern [at] kernel.org&gt;</p>
