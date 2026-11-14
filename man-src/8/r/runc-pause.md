---
title: "runc-pause(8)"
name: "runc-pause"
section: "8"
letter: "r"
url: "/docs/linux/man/8-runc-pause/"
description: "runc-pause – suspend all processes inside the container"
---

<p><code>runc-pause</code> &#8211; suspend all processes inside the container </p>
<h2>Synopsis</h2>
<p><code>runc pause</code> <i>container-id</i> </p>
<h2>Description</h2>
<p>The <code>pause</code> command suspends all processes in the instance of the container identified by <i>container-id</i>. Use <code>runc list</code> to identify instances of containers and their current status. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-runc-list/">runc-list</a></code>(8), <code><a href="/docs/linux/man/8-runc-resume/">runc-resume</a></code>(8), <code><a href="/docs/linux/man/8-runc/">runc</a></code>(8). </p>
