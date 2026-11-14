---
title: "w1_reset_resume_command(9)"
name: "w1_reset_resume_command"
section: "9"
letter: "w"
url: "/docs/linux/man/9-w1_reset_resume_command/"
description: "w1_reset_resume_command – resume instead of another match ROM"
---

<p>w1_reset_resume_command &#8211; resume instead of another match ROM</p>
<h2>Synopsis</h2>
<pre><code>int w1_reset_resume_command(struct w1_master *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the master device</dl>
<h2>Description</h2>
<p>When the workflow with a slave amongst many requires several successive commands a reset between each, this function is similar to doing a reset then a match ROM for the last matched ROM. The advantage being that the matched ROM step is skipped in favor of the resume command. The slave must support the command of course. </p>
<p> If the bus has only one slave, traditionnaly the match ROM is skipped and a &#8220;SKIP ROM&#8221; is done for efficiency. On multi-slave busses, this doesn&#8217;t work of course, but the resume command is the next best thing. </p>
<p> The w1 master lock must be held.</p>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
