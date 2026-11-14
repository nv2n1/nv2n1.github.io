---
title: "runc-resume(8)"
name: "runc-resume"
section: "8"
letter: "r"
url: "/docs/linux/man/8-runc-resume/"
description: "runc-resume – resume all processes that have been previously paused"
---

<p><code>runc-resume</code> &#8211; resume all processes that have been previously paused </p>
<h2>Synopsis</h2>
<p><code>runc resume</code> <i>container-id</i> </p>
<h2>Description</h2>
<p>The <code>resume</code> command resumes all processes in the instance of the container identified by <i>container-id</i>. Use <code>runc list</code> to identify instances of containers and their current status. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-runc-list/">runc-list</a></code>(8), <code><a href="/docs/linux/man/8-runc-pause/">runc-pause</a></code>(8), <code><a href="/docs/linux/man/8-runc/">runc</a></code>(8). </p>
