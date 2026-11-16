---
title: "fence_zvm(8)"
name: "fence_zvm"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_zvm/"
description: "fence_zvm – I/O Fencing agent for GFS on s390 and zSeries VM clusters"
---

<p>fence_zvm &#8211; I/O Fencing agent for GFS on s390 and zSeries VM clusters</p>
<h2>Synopsis</h2>
<p><code>fence_zvm</code> [<i>OPTION</i>]&#8230; </p>
<h2>Description</h2>
<p>fence_zvm is an I/O Fencing agent used on a GFS virtual machine in a s390 or zSeries VM cluster. It uses the s3270 program to log the specified virtual machine out of VM. For fence_zvm to execute correctly, you must have s3270 in your PATH. fence_zvm accepts options on the command line as well as from stdin. fence_node sends the options through stdin when it execs the agent. fence_zvm can be run by itself with command line options which is useful for testing. Vendor URL: <a rel="nofollow" href="http://www.ibm.com">http://www.ibm.com</a> </p>
<h2>Options</h2>
<dl>
<dt><code>-a</code> <i>IPaddress</i></dt>
<dd>IP address or hostname of the Physical machine (required).</dd>
<dt><code>-h</code></dt>
<dd>Print out a help message describing available options, then exit.</dd>
<dt><code>-u</code> <i>userid</i></dt>
<dd>userid of the virtual machine to fence (required).</dd>
<dt><code>-p</code> <i>password</i></dt>
<dd>password of the virtual machine to fence (required).</dd>
<dt><code>-S</code> <i>path</i></dt>
<dd>Full path to an executable to generate the password of the virtual machine to fence.</dd>
<dt><code>-q</code></dt>
<dd>quiet mode, no output.</dd>
<dt><code>-V</code></dt>
<dd>Print out a version message, then exit. </dd>
</dl>
<h2>Stdin Parameters</h2>
<dl>
<dt><i>agent = &lt; param &gt;</i></dt>
<dd>This option is used by <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8) and is ignored by fence_zvm.</dd>
<dt><i>ipaddr = &lt; hostname | ip &gt;</i></dt>
<dd>IP address or hostname of the Physical machine (required).</dd>
<dt><i>passwd = &lt; param &gt;</i></dt>
<dd>password of the virtual machine to fence (required).</dd>
<dt><i>passwd_script = &lt; param &gt;</i></dt>
<dd>Full path to an executable to generate the password of the virtual machine to fence.</dd>
<dt><i>userid = &lt; param &gt;</i></dt>
<dd>userid of the virtual machine to fence (required). </dd>
</dl>
<h2>See Also</h2>
<p>fence(8), <a href="/docs/linux/man/8-fenced/">fenced</a>(8), <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8) </p>
