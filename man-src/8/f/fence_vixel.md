---
title: "fence_vixel(8)"
name: "fence_vixel"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_vixel/"
description: "fence_vixel – I/O Fencing agent for Vixel FC switches"
---

<p>fence_vixel &#8211; I/O Fencing agent for Vixel FC switches</p>
<h2>Synopsis</h2>
<p><code>fence_vixel</code> [<i>OPTION</i>]&#8230; </p>
<h2>Description</h2>
<p>fence_vixel is an I/O Fencing agent which can be used with Vixel FC switches. It logs into a Vixel switch via telnet and removes the specified port from the zone. Removing the zone access from the port disables the port from being able to access the storage. fence_vixel accepts options on the command line as well as from stdin. fenced sends parameters through stdin when it execs the agent. fence_vixel can be run by itself with command line options which is useful for testing. After a fence operation has taken place the fenced machine can no longer connect to the Vixel FC switch. When the fenced machine is ready to be brought back into the GFS cluster (after reboot) the port on the Vixel FC switch needs to be enabled. In order to do this, log into the Vixel FC switch. Then go to: config-&gt;zones-&gt;config &lt;port&gt; &lt;comma-separated-list-of-ports-in-the-zone&gt; Then apply Consult the Vixel manual for details Vendor URL: <a rel="nofollow" href="http://www.emulex.com">http://www.emulex.com</a> </p>
<h2>Options</h2>
<dl>
<dt><code>-a</code> <i>IPaddress</i></p>
<dd>IP address of the switch.</p>
<dt><code>-h</code></p>
<dd>Print out a help message describing available options, then exit.</p>
<dt><code>-n</code> <i>port</i></p>
<dd>The port number to remove zoning from on the switch.</p>
<dt><code>-p</code> <i>password</i></p>
<dd>Password for login.</p>
<dt><code>-S</code> <i>path</i></p>
<dd>Full path to an executable to generate the password for login.</p>
<dt><code>-V</code></p>
<dd>Print out a version message, then exit. </p>
</dl>
<h2>Stdin Parameters</h2>
<dl>
<dt><i>agent = &lt; param &gt;</i></p>
<dd>This option is used by <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8) and is ignored by fence_vixel.</p>
<dt><i>ipaddr = &lt; hostname | ip &gt;</i></p>
<dd>IP address or hostname of the switch.</p>
<dt><i>passwd = &lt; param &gt;</i></p>
<dd>Password for login.</p>
<dt><i>passwd_script = &lt; param &gt;</i></p>
<dd>Full path to an executable to generate the password for login.</p>
<dt><i>port = &lt; param &gt;</i></p>
<dd>The port number to remove zoning from on the switch. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-fence/">fence</a>(8), <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8) </p>
