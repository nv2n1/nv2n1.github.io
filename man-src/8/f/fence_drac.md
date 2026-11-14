---
title: "fence_drac(8)"
name: "fence_drac"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_drac/"
description: "fence_drac – fencing agent for Dell Remote Access Card"
---

<p>fence_drac &#8211; fencing agent for Dell Remote Access Card</p>
<h2>Synopsis</h2>
<p><code>fence_drac</code> [<i>OPTION</i>]&#8230; </p>
<h2>Description</h2>
<p>fence_drac is an I/O Fencing agent which can be used with the Dell Remote Access Card (DRAC). This card provides remote access to controlling power to a server. It logs into the DRAC through the telnet interface of the card. By default, the telnet interface is not enabled. To enable the interface, you will need to use the racadm command in the racser-devel rpm available from Dell. To enable telnet on the DRAC: [root]# racadm config -g cfgSerial -o cfgSerialTelnetEnable 1 [root]# racadm racreset fence_drac accepts options on the command line as well as from stdin. Fenced sends parameters through stdin when it execs the agent. fence_drac can be run by itself with command line options. This is useful for testing and for turning outlets on or off from scripts. Vendor URL: <a rel="nofollow" href="http://www.dell.com">http://www.dell.com</a> </p>
<h2>Options</h2>
<dl>
<dt><code>-a</code> <i>IPaddress</i></p>
<dd>IP address or hostname of the switch.</p>
<dt><code>-c</code> <i>cmd_prompt</i></p>
<dd>Force fence_drac to use cmd_prompt as the command prompt</p>
<dt><code>-d</code> <i>dracversion</i></p>
<dd>Force fence_drac to treat the device as though it was for the specified drac version</p>
<dt><code>-D</code> <i>dumpfile</i></p>
<dd>Debug file of the telnet interaction</p>
<dt><code>-h</code></p>
<dd>Print out a help message describing available options, then exit.</p>
<dt><code>-l</code> <i>login</i></p>
<dd>Login name.</p>
<dt><code>-m</code> <i>modulename</i></p>
<dd>The module name of the blade when using DRAC/MC firmware.</p>
<dt><code>-o</code> <i>action</i></p>
<dd>The action required. reboot (default), off, on or status.</p>
<dt><code>-p</code> <i>password</i></p>
<dd>Password for login.</p>
<dt><code>-S</code> <i>path</i></p>
<dd>Full path to an executable to generate the password for login.</p>
<dt><code>-f</code> <i>seconds</i></p>
<dd>Wait X seconds before fencing is started</p>
<dt><code>-V</code></p>
<dd>Print out a version message, then exit. </p>
</dl>
<h2>Stdin Parameters</h2>
<dl>
<dt><i>action = &lt; param &gt;</i></p>
<dd>The action required. reboot (default), off, on or status.</p>
<dt><i>agent = &lt; param &gt;</i></p>
<dd>This option is used by <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8) and is ignored by fence_apc.</p>
<dt><i>cmd_prompt = &lt; param &gt;</i></p>
<dd>Force fence_drac to use cmd_prompt as the command prompt</p>
<dt><i>drac_version = &lt; param &gt;</i></p>
<dd>Force fence_drac to treat the device as though it was for the specified drac version.</p>
<dt><i>debug = &lt; dumpfile &gt;</i></p>
<dd>Debug file of the telnet interaction</p>
<dt><i>ipaddr = &lt; hostname | ip &gt;</i></p>
<dd>IP address or hostname of the switch.</p>
<dt><i>login = &lt; param &gt;</i></p>
<dd>Login name.</p>
<dt><i>modulename = &lt; param &gt;</i></p>
<dd>The module name of the blade when using DRAC/MC firmware.</p>
<dt><i>passwd = &lt; param &gt;</i></p>
<dd>Password for login.</p>
<dt><i>passwd_script = &lt; param &gt;</i></p>
<dd>Full path to an executable to generate the password for login.</p>
<dt><i>delay = &lt; param &gt;</i></p>
<dd>Wait X seconds before fencing is started</p>
<dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-fence/">fence</a>(8), <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8) </p>
