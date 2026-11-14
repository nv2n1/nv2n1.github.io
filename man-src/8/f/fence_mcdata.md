---
title: "fence_mcdata(8)"
name: "fence_mcdata"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_mcdata/"
description: "fence_mcdata – I/O Fencing agent for McData FC switches"
---

<p>fence_mcdata &#8211; I/O Fencing agent for McData FC switches</p>
<h2>Synopsis</h2>
<p><code>fence_mcdata</code> [<i>OPTION</i>]&#8230; </p>
<h2>Description</h2>
<p>fence_mcdata is an I/O Fencing agent which can be used with McData FC switches. It logs into a McData switch via telnet and disables a specified port. Disabling the port which a machine is connected to effectively fences that machine. Lengthy telnet connections to the switch should be avoided while a GFS cluster is running because the connection will block any necessary fencing actions. fence_mcdata accepts options on the command line as well as from stdin. fenced sends parameters through stdin when it execs the agent. fence_mcdata can be run by itself with command line options which is useful for testing. After a fence operation has taken place the fenced machine can no longer connect to the McData FC switch. When the fenced machine is ready to be brought back into the GFS cluster (after reboot) the port on the McData FC switch needs to be enabled. This can be done by running fence_mcdata and specifying the enable action. Vendor URL: <a rel="nofollow" href="http://www.brocade.com">http://www.brocade.com</a> </p>
<h2>Options</h2>
<dl>
<dt><code>-a</code> <i>IPaddress</i></p>
<dd>IP address of the switch.</p>
<dt><code>-h</code></p>
<dd>Print out a help message describing available options, then exit.</p>
<dt><code>-l</code> <i>login</i></p>
<dd>Username name for the switch.</p>
<dt><code>-n</code> <i>port</i></p>
<dd>The port number to disable on the switch.</p>
<dt><code>-o</code> <i>action</i></p>
<dd>The action required. disable (default) or enable.</p>
<dt><code>-p</code> <i>password</i></p>
<dd>Password for login.</p>
<dt><code>-S</code> <i>path</i></p>
<dd>Full path to an executable to generate the password for login.</p>
<dt><code>-q</code></p>
<dd>Quiet mode: print only error messages.</p>
<dt><code>-V</code></p>
<dd>Print out a version message, then exit. </p>
</dl>
<h2>Stdin Parameters</h2>
<dl>
<dt><i>agent = &lt; param &gt;</i></p>
<dd>This option is used by <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8) and is ignored by fence_mcdata.</p>
<dt><i>ipaddr = &lt; hostname | ip &gt;</i></p>
<dd>IP address or hostname of the switch.</p>
<dt><i>login = &lt; param &gt;</i></p>
<dd>Login name.</p>
<dt><i>option = &lt; param &gt;</i></p>
<dd>The action required. disable (default) or enable.</p>
<dt><i>passwd = &lt; param &gt;</i></p>
<dd>Password for login.</p>
<dt><i>passwd_script = &lt; param &gt;</i></p>
<dd>Full path to an executable to generate the password for login.</p>
<dt><i>port = &lt; param &gt;</i></p>
<dd>The port number to disable on the switch. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-fence/">fence</a>(8), <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8) </p>
