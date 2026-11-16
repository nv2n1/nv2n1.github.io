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
<p>fence_egenera is an I/O Fencing agent which can be used with the Egenera BladeFrame. It logs into a control blade (cserver) via ssh and operates on a processing blade (pserver) identified by the pserver name and the logical process area network (LPAN) that it is in. fence_egenera requires that ssh keys have been setup so that the fence_egenera does not require a password to authenticate. Refer to ssh(8) for more information on setting up ssh keys. fence_egenera accepts options on the command line as well as from stdin. Fenced sends parameters through stdin when it execs the agent. fence_egenera can also be run by itself with command line options. Vendor URL: <a rel="nofollow" href="http://www.egenera.com">http://www.egenera.com</a> </p>
<h2>Options</h2>
<dl>
<dt><code>-c</code> <i>cserver</i></dt>
<dd>The cserver to ssh to. cserver can be in the form user [at] hostname to specify a different user to login as.</dd>
<dt><code>-h</code></dt>
<dd>Print out a help message describing available options, then exit.</dd>
<dt><code>-l</code> <i>lpan</i></dt>
<dd>the lpan to operate on</dd>
<dt><code>-o</code> <i>action</i></dt>
<dd>The action required. reboot (default), off, on or status.</dd>
<dt><code>-p</code> <i>pserver</i></dt>
<dd>the pserver to operate on</dd>
<dt><code>-f</code> <i>seconds</i></dt>
<dd>Wait X seconds before fencing is started</dd>
<dt><code>-q</code></dt>
<dd>quite mode. suppress output.</dd>
<dt><code>-V</code></dt>
<dd>Print out a version message, then exit. </dd>
</dl>
<h2>Stdin Parameters</h2>
<dl>
<dt><i>action = &lt; param &gt;</i></dt>
<dd>The action required. reboot (default), off, on or status.</dd>
<dt><i>agent = &lt; param &gt;</i></dt>
<dd>This option is used by <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8) and is ignored by fence_apc.</dd>
<dt><i>cserver = &lt; param &gt;</i></dt>
<dd>The cserver to ssh to. cserver can be in the form user [at] hostname to specify a different user to login as.</dd>
<dt><i>lpan = &lt; param &gt;</i></dt>
<dd>The lpan to operate on</dd>
<dt><i>pserver = &lt; param &gt;</i></dt>
<dd>The pserver to operate on</dd>
<dt><i>esh = &lt; param &gt;</i></dt>
<dd>The path to the esh command on the cserver (default is /opt/panmgr/bin/esh)</dd>
<dt><i>delay = &lt; param &gt;</i></dt>
<dd>Wait X seconds before fencing is started </dd>
</dl>
<h2>See Also</h2>
<p>fence(8), <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8), ssh(8) </p>
