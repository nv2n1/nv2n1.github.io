---
title: "fence_egenera(8)"
name: "fence_egenera"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_egenera/"
description: "fence_egenera – I/O Fencing agent for the Egenera BladeFrame"
---

<p>fence_egenera &#8211; I/O Fencing agent for the Egenera BladeFrame</p>
<h2>Synopsis</h2>
<p><code>fence_egenera</code> [<i>OPTION</i>]&#8230; </p>
<h2>Description</h2>
<p>fence_egenera is an I/O Fencing agent which can be used with the Egenera BladeFrame. It logs into a control blade (cserver) via ssh and operates on a processing blade (pserver) identified by the pserver name and the logical process area network (LPAN) that it is in. fence_egenera requires that ssh keys have been setup so that the fence_egenera does not require a password to authenticate. Refer to <a href="/docs/linux/man/8-ssh/">ssh</a>(8) for more information on setting up ssh keys. fence_egenera accepts options on the command line as well as from stdin. Fenced sends parameters through stdin when it execs the agent. fence_egenera can also be run by itself with command line options. Vendor URL: <a rel="nofollow" href="http://www.egenera.com">http://www.egenera.com</a> </p>
<h2>Options</h2>
<dl>
<dt><code>-c</code> <i>cserver</i></p>
<dd>The cserver to ssh to. cserver can be in the form user [at] hostname to specify a different user to login as.</p>
<dt><code>-h</code></p>
<dd>Print out a help message describing available options, then exit.</p>
<dt><code>-l</code> <i>lpan</i></p>
<dd>the lpan to operate on</p>
<dt><code>-o</code> <i>action</i></p>
<dd>The action required. reboot (default), off, on or status.</p>
<dt><code>-p</code> <i>pserver</i></p>
<dd>the pserver to operate on</p>
<dt><code>-f</code> <i>seconds</i></p>
<dd>Wait X seconds before fencing is started</p>
<dt><code>-q</code></p>
<dd>quite mode. suppress output.</p>
<dt><code>-V</code></p>
<dd>Print out a version message, then exit. </p>
</dl>
<h2>Stdin Parameters</h2>
<dl>
<dt><i>action = &lt; param &gt;</i></p>
<dd>The action required. reboot (default), off, on or status.</p>
<dt><i>agent = &lt; param &gt;</i></p>
<dd>This option is used by <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8) and is ignored by fence_apc.</p>
<dt><i>cserver = &lt; param &gt;</i></p>
<dd>The cserver to ssh to. cserver can be in the form user [at] hostname to specify a different user to login as.</p>
<dt><i>lpan = &lt; param &gt;</i></p>
<dd>The lpan to operate on</p>
<dt><i>pserver = &lt; param &gt;</i></p>
<dd>The pserver to operate on</p>
<dt><i>esh = &lt; param &gt;</i></p>
<dd>The path to the esh command on the cserver (default is /opt/panmgr/bin/esh)</p>
<dt><i>delay = &lt; param &gt;</i></p>
<dd>Wait X seconds before fencing is started </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-fence/">fence</a>(8), <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8), <a href="/docs/linux/man/8-ssh/">ssh</a>(8) </p>
