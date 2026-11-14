---
title: "hb_delnode(1)"
name: "hb_delnode"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hb_delnode/"
description: "hb_delnode – hb_delnode is a simple linux-ha shell script. It sends a message to the cluster to delete nodes."
---

<h2>NAME</h2>
<p> hb_delnode &#8211; hb_delnode is a simple linux-ha shell script. It sends a message to the cluster to delete nodes.</p>
<h2>SYNOPSIS</h2>
<p> <code>hb_delnode</code> <code>&lt;node1&gt;</code> <code>[node2]</code> <code>[node3]</code> <code>&#8230;</code></p>
<h2>DESCRIPTION</h2>
<p> The full path is usually /usr/lib/heartbeat/hb_delnode. To get a list of the options, issue the command, <code> &quot;/usr/lib/heartbeat/hb_delnode &#8211;help&quot; </code> </p>
<p> If there is any node in the arguments is not in the cluster, the command will fail and no node will be deleted. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-hb_addnode/">hb_addnode</a>(1), <a href="/docs/linux/man/8-heartbeat/">heartbeat</a>(8), <a href="/docs/linux/man/1-cl_status/">cl_status</a>(1) </p>
<h2>AUTHORS</h2>
<p> linux-ha &#8212; Alan Robertson &lt;alanr [at] unix.sh&gt; <i>et al</i>. </p>
<p> man page &#8212; Guochun Shi &lt;gshi [at] ncsa.uiuc.edu&gt; </p>
<h2>Index</h2>
