---
title: "fence_baytech(8)"
name: "fence_baytech"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_baytech/"
description: "fence_baytech – I/O Fencing agent for Baytech RPC switches in combination with a Cyclades Terminal Server"
---

<p>fence_baytech &#8211; I/O Fencing agent for Baytech RPC switches in combination with a Cyclades Terminal Server</p>
<h2>Synopsis</h2>
<p><code>fence_baytech</code> [<i>OPTION</i>]&#8230; </p>
<h2>Description</h2>
<p>This fencing agent is written for the Baytech RPC27-20nc in combination with a Cyclades terminal server. The Cyclades TS exports the RPC&#8217;s serial port via a Telnet interface. Other interfaces, such as SSH, are possible. However, this script relies upon the assumption that Telnet is used. Future features to this agent would allow the agent to work with a multitude of different communication protocols such as Telnet, SSH or Kermit. The other assumption that is made is that Outlet names do not end in space. The name &quot;Foo&quot; and &quot;Foo &quot; are identical when the RPC prints them with the status command. fence_baytech accepts options on the command line as well as from stdin. fenced sends parameters through stdin when it execs the agent. fence_baytech can be run by itself with command line options which is useful for testing. Vendor URL: <a rel="nofollow" href="http://www.baytech.net">http://www.baytech.net</a> </p>
<h2>Options</h2>
<dl>
<dt><code>-a</code> <i>host</i></dt>
<dd>IP address or hostname to connect to.</dd>
<dt><code>-h</code></dt>
<dd>Print out a help message describing available options, then exit.</dd>
<dt><code>-l</code> <i>login</i></dt>
<dd>Username name for the switch.</dd>
<dt><code>-n</code> <i>port</i></dt>
<dd>The name of the outlet to act upon.</dd>
<dt><code>-o</code> <i>action</i></dt>
<dd>The action required. This can be on, off, status or reboot (default)</dd>
<dt><code>-p</code> <i>password</i></dt>
<dd>Password for login.</dd>
<dt><code>-S</code> <i>path</i></dt>
<dd>Full path to an executable to generate the password for login.</dd>
<dt><code>-q</code></dt>
<dd>Quiet mode: print only error messages.</dd>
<dt><code>-V</code></dt>
<dd>Print out a version message, then exit. </dd>
</dl>
<h2>Stdin Parameters</h2>
<dl>
<dt><i>agent = &lt; param &gt;</i></dt>
<dd>This option is used by <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8) and is ignored by fence_baytech.</dd>
<dt><i>host = &lt; hostname | ip &gt;</i></dt>
<dd>IP address or hostname to connect to.</dd>
<dt><i>login = &lt; param &gt;</i></dt>
<dd>Login name.</dd>
<dt><i>action = &lt; param &gt;</i></dt>
<dd>The action required. This can be on, off, status or reboot (default)</dd>
<dt><i>passwd = &lt; param &gt;</i></dt>
<dd>Password for login.</dd>
<dt><i>passwd_script = &lt; param &gt;</i></dt>
<dd>Full path to an executable to generate the password for login.</dd>
<dt><i>outlet = &lt; param &gt;</i></dt>
<dd>The name of the outlet to act upon. </dd>
</dl>
<h2>See Also</h2>
<p>fence(8), <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8) </p>
