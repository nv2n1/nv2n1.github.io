---
title: "fence_cpint(8)"
name: "fence_cpint"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_cpint/"
description: "fence_cpint – I/O Fencing agent for GFS on s390 and zSeries VM clusters"
---

<p>fence_cpint &#8211; I/O Fencing agent for GFS on s390 and zSeries VM clusters</p>
<h2>Synopsis</h2>
<p><code>fence_cpint</code> [<i>OPTION</i>]&#8230; </p>
<h2>Description</h2>
<p>fence_cpint is an I/O Fencing agent used on a virtual machine running GFS in a s390 or zSeries VM cluster. It uses the cpint package to send a CP LOGOFF command to the specified virtual machine. For fence_cpint to execute correctly, you must have the cpint module installed, and hcp in your PATH. <code>NOTE:</code> for fence_cpint to send a command to another virtual machine, the machine executing it must either be a privilege class C user or it must be the secondary user of the virtual machine to be fenced. This means that unless all of you GULM server nodes are privilege class C, fence_cpint can only be used with SLM. fence_cpint accepts options on the command line as well as from stdin. fence_node sends the options through stdin when it execs the agent. fence_cpint can be run by itself with command line options which is useful for testing. Vendor URL: <a rel="nofollow" href="http://www.ibm.com">http://www.ibm.com</a> </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Print out a help message describing available options, then exit.</p>
<dt><code>-u</code> <i>userid</i></p>
<dd>userid of the virtual machine to fence (required).</p>
<dt><code>-q</code></p>
<dd>quiet mode, no output.</p>
<dt><code>-V</code></p>
<dd>Print out a version message, then exit. </p>
</dl>
<h2>Stdin Parameters</h2>
<dl>
<dt><i>agent = &lt; param &gt;</i></p>
<dd>This option is used by <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8) and is ignored by fence_cpint.</p>
<dt><i>userid = &lt; parm &gt;</i></p>
<dd>userid of the virtual machine to fence (required). </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-fence/">fence</a>(8), <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8) </p>
