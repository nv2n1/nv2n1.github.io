---
title: "hb_takeover(1)"
name: "hb_takeover"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hb_takeover/"
description: "hb_takeover – hb_takeover is a simple linux-ha shell script. It issues a command to takeover resources from the other node, if available."
---

<h2>NAME</h2>
<p> hb_takeover &#8211; hb_takeover is a simple linux-ha shell script. It issues a command to takeover resources from the other node, if available.</p>
<h2>SYNOPSIS</h2>
<p> <code>hb_takeover</code> [all|foreign|local|failback]</p>
<h2>DESCRIPTION</h2>
<p> The full path is usually /usr/lib/heartbeat/hb_takeover. Performing an hb_takeover on the current node is equivalent to performing an hb_standby on the other node. </p>
<h2>CAVEATS</h2>
<p> <code>hb_takeover</code> is only usable in R1-style configurations (i.e., those configured using the <i>haresources</i> file). </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-hb_standby/">hb_standby</a>(1), <a href="/docs/linux/man/8-heartbeat/">heartbeat</a>(8), <a href="/docs/linux/man/1-cl_status/">cl_status</a>(1) </p>
<h2>DOCUMENTATION</h2>
<p> More information may be found at <a rel="nofollow" href="http://linux-ha.org/hb_takeover">http://linux-ha.org/hb_takeover</a> </p>
<h2>AUTHORS</h2>
<p> linux-ha &#8212; Alan Robertson &lt;alanr [at] unix.sh&gt; <i>et al</i>. </p>
<p> man page &#8212; Guochun Shi &lt;gshi [at] ncsa.uiuc.edu&gt; </p>
<h2>Index</h2>
