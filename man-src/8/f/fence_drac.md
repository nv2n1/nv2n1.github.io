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
<dt><code>-a</code> <i>IPaddress</i></dt>
<dd>IP address or hostname of the switch.</dd>
<dt><code>-c</code> <i>cmd_prompt</i></dt>
<dd>Force fence_drac to use cmd_prompt as the command prompt</dd>
<dt><code>-d</code> <i>dracversion</i></dt>
<dd>Force fence_drac to treat the device as though it was for the specified drac version</dd>
<dt><code>-D</code> <i>dumpfile</i></dt>
<dd>Debug file of the telnet interaction</dd>
<dt><code>-h</code></dt>
<dd>Print out a help message describing available options, then exit.</dd>
<dt><code>-l</code> <i>login</i></dt>
<dd>Login name.</dd>
<dt><code>-m</code> <i>modulename</i></dt>
<dd>The module name of the blade when using DRAC/MC firmware.</dd>
<dt><code>-o</code> <i>action</i></dt>
<dd>The action required. reboot (default), off, on or status.</dd>
<dt><code>-p</code> <i>password</i></dt>
<dd>Password for login.</dd>
<dt><code>-S</code> <i>path</i></dt>
<dd>Full path to an executable to generate the password for login.</dd>
<dt><code>-f</code> <i>seconds</i></dt>
<dd>Wait X seconds before fencing is started</dd>
<dt><code>-V</code></dt>
<dd>Print out a version message, then exit. </dd>
</dl>
<h2>Stdin Parameters</h2>
<dl>
<dt><i>action = &lt; param &gt;</i></dt>
<dd>The action required. reboot (default), off, on or status.</dd>
<dt><i>agent = &lt; param &gt;</i></dt>
<dd>This option is used by <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8) and is ignored by fence_apc.</dd>
<dt><i>cmd_prompt = &lt; param &gt;</i></dt>
<dd>Force fence_drac to use cmd_prompt as the command prompt</dd>
<dt><i>drac_version = &lt; param &gt;</i></dt>
<dd>Force fence_drac to treat the device as though it was for the specified drac version.</dd>
<dt><i>debug = &lt; dumpfile &gt;</i></dt>
<dd>Debug file of the telnet interaction</dd>
<dt><i>ipaddr = &lt; hostname | ip &gt;</i></dt>
<dd>IP address or hostname of the switch.</dd>
<dt><i>login = &lt; param &gt;</i></dt>
<dd>Login name.</dd>
<dt><i>modulename = &lt; param &gt;</i></dt>
<dd>The module name of the blade when using DRAC/MC firmware.</dd>
<dt><i>passwd = &lt; param &gt;</i></dt>
<dd>Password for login.</dd>
<dt><i>passwd_script = &lt; param &gt;</i></dt>
<dd>Full path to an executable to generate the password for login.</dd>
<dt><i>delay = &lt; param &gt;</i></dt>
<dd>Wait X seconds before fencing is started</dd>
<dd></dd></dl>
<h2>See Also</h2>
<p>fence(8), <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8) </p>
