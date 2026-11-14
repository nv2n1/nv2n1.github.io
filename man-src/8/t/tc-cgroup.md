---
title: "tc-cgroup(8)"
name: "tc-cgroup"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-cgroup/"
description: "cgroup – control group based traffic control filter"
---

<p>cgroup &#8211; control group based traffic control filter</p>
<h2>Synopsis</h2>
<p><code>tc</code> <code>filter</code> &#8230; <code>cgroup</code> [ <code>match</code> <i>EMATCH_TREE</i> ] [ <code>action</code> <i>ACTION_SPEC</i> ]</p>
<h2>Description</h2>
<p>This filter serves as a hint to <code>tc</code> that the assigned class ID of the net_cls control group the process the packet originates from belongs to should be used for classification. Obviously, it is useful for locally generated packets only.</p>
<h2>Options</h2>
<dl>
<dt><code>action</code><i> ACTION_SPEC</i></p>
<dd>Apply an action from the generic actions framework on matching packets.</p>
<dt><code>match</code><i> EMATCH_TREE</i></p>
<dd>Match packets using the extended match infrastructure. See <code><a href="/docs/linux/man/8-tc-ematch/">tc-ematch</a></code>(8) for a detailed description of the allowed syntax in <i>EMATCH_TREE</i>.</dl>
<h2>Examples</h2>
<p>In order to use this filter, a net_cls control group has to be created first and class as well as process ID(s) assigned to it. The following creates a net_cls cgroup named &quot;foobar&quot;:</p>
<dl>
<dd>modprobe cls_cgroup mkdir /sys/fs/cgroup/net_cls mount -t cgroup -onet_cls net_cls /sys/fs/cgroup/net_cls mkdir /sys/fs/cgroup/net_cls/foobar</dl>
<p> To assign a class ID to the created cgroup, a file named <i>net_cls.classid</i> has to be created which contains the class ID to be assigned as a hexadecimal, 64bit wide number. The upper 32bits are reserved for the major handle, the remaining hold the minor. So a class ID of e.g. <code>ff:be</code> has to be written like so: <code>0xff00be</code> (leading zeroes may be omitted). To continue the above example, the following assigns class ID 1:2 to foobar cgroup:</p>
<dl>
<dd>echo 0x10002 &gt; /sys/fs/cgroup/net_cls/foobar/net_cls.classid</dl>
<p> Finally some PIDs can be assigned to the given cgroup:</p>
<dl>
<dd>echo 1234 &gt; /sys/fs/cgroup/net_cls/foobar/tasks echo 5678 &gt; /sys/fs/cgroup/net_cls/foobar/tasks</dl>
<p> Now by simply attaching a <code>cgroup</code> filter to a <code>qdisc</code> makes packets from PIDs 1234 and 5678 be pushed into class 1:2. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-ematch/">tc-ematch</a></code>(8),<br />
 the file <i>Documentation/cgroups/net_cls.txt</i> of the Linux kernel tree </p>
