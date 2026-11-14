---
title: "devlink-monitor(8)"
name: "devlink-monitor"
section: "8"
letter: "d"
url: "/docs/linux/man/8-devlink-monitor/"
description: "devlink-monitor – state monitoring"
---

<p>devlink-monitor &#8211; state monitoring</p>
<h2>Synopsis</h2>
<p><code>devlink monitor</code> [ <code>all</code> | <i>OBJECT-LIST</i> ] </p>
<h2>Description</h2>
<p>The <code>devlink</code> utility can monitor the state of devlink devices and ports continuously. This option has a slightly different format. Namely, the <code>monitor</code> command is the first in the command line and then the object list. <i>OBJECT-LIST</i> is the list of object types that we want to monitor. It may contain <code>dev</code>, <code>port</code>, <code>health</code>, <code>trap</code>, <code>trap-group</code>, <code>trap-policer</code>. <code>devlink</code> opens Devlink Netlink socket, listens on it and dumps state changes. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-devlink/">devlink</a></code>(8), <code><a href="/docs/linux/man/8-devlink-dev/">devlink-dev</a></code>(8), <code><a href="/docs/linux/man/8-devlink-sb/">devlink-sb</a></code>(8), <code><a href="/docs/linux/man/8-devlink-port/">devlink-port</a></code>(8), <code><a href="/docs/linux/man/8-devlink-health/">devlink-health</a></code>(8), <code><a href="/docs/linux/man/8-devlink-trap/">devlink-trap</a></code>(8), </p>
<h2>Author</h2>
<p>Jiri Pirko &lt;jiri [at] mellanox.com&gt;</p>
