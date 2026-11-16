---
title: "fence_rackswitch(8)"
name: "fence_rackswitch"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_rackswitch/"
description: "fence_rackswitch – I/O Fencing agent for RackSaver RackSwitch"
---

<p>fence_rackswitch &#8211; I/O Fencing agent for RackSaver RackSwitch</p>
<h2>Synopsis</h2>
<p><code>fence_rackswitch</code> [<i>OPTION</i>]&#8230; </p>
<h2>Description</h2>
<p>fence_rackswitch is an I/O Fencing agent which can be used with the RackSaver RackSwitch. It logs into the RackSwitch and boots a specified plug. Using the http interface to the RackSwitch should be avoided while a GFS cluster is running because the connection may interfere with the operation of this agent. fence_rackswitch accepts options on the command line as well as from stdin. fenced sends the options through stdin when it execs the agent. fence_rackswitch can be run by itself with command line options which is useful for testing. Vendor URL: <a rel="nofollow" href="http://www.bladenetwork.net">http://www.bladenetwork.net</a> </p>
<h2>Options</h2>
<dl>
<dt><code>-a</code> <i>IPaddress</i></dt>
<dd>IP address of the switch.</dd>
<dt><code>-h</code></dt>
<dd>Print out a help message describing available options, then exit.</dd>
<dt><code>-n</code> <i>plug</i></dt>
<dd>The plug number to power cycle.</dd>
<dt><code>-p</code> <i>password</i></dt>
<dd>Password for login.</dd>
<dt><code>-S</code> <i>path</i></dt>
<dd>Full path to an executable to generate the password for login.</dd>
<dt><code>-l</code> <i>username</i></dt>
<dd>Username for login.</dd>
<dt><code>-q</code></dt>
<dd>Quiet operation. Only print out error messages.</dd>
<dt><code>-V</code></dt>
<dd>Print out a version message, then exit. </dd>
</dl>
<h2>Stdin Parameters</h2>
<dl>
<dt><i>agent = &lt; param &gt;</i></dt>
<dd>This option is used by <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8) and is ignored by fence_rackswitch.</dd>
<dt><i>ipaddr = &lt; ip &gt;</i></dt>
<dd>IP address of the switch.</dd>
<dt><i>username = &lt; param &gt;</i></dt>
<dd>Username for login.</dd>
<dt><i>password = &lt; param &gt;</i></dt>
<dd>Password for login.</dd>
<dt><i>passwd_script = &lt; param &gt;</i></dt>
<dd>Full path to an executable to generate the password for login.</dd>
<dt><i>port = &lt; param &gt;</i></dt>
<dd>The port (outlet) number to act upon. </dd>
</dl>
<h2>See Also</h2>
<p>fence(8), <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8) </p>
