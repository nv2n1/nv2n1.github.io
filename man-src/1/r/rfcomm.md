---

title: "rfcomm(1)"
name: "rfcomm"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rfcomm/"
description: "rfcomm – RFCOMM configuration utility"
---

<p> rfcomm &#8211; RFCOMM configuration utility </p>
<h2>SYNOPSIS</h2>
<p> <code>rfcomm</code> [<i>OPTIONS</i>] &lt;<i>COMMAND</i>&gt; &lt;<i>dev</i>&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-rfcomm/">rfcomm</a>(1)</code> is used to set up, maintain, and inspect the RFCOMM configuration of the Bluetooth subsystem in the Linux kernel. If no <code>command</code> is given, or if the option <code>-a</code> is used, <code>rfcomm</code> prints information about the configured RFCOMM devices.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> Gives a list of possible commands.</dd>
<dt><code>-a</code></dt>
<dd> Prints information about all configured RFCOMM devices.</dd>
<dt><code>-r</code></dt>
<dd> Switch TTY into raw mode (doesn&#8217;t work with &quot;bind&quot;).</dd>
<dt><code>-i &lt;</code><i>hciX</i>&gt; | &lt;<i>bdaddr</i>&gt;</dt>
<dd> The command is applied to device <i>hciX</i>, which must be the name or the address of an installed Bluetooth device. If not specified, the command will be use the first available Bluetooth device.</dd>
<dt><code>-A</code></dt>
<dd> Enable authentication</dd>
<dt><code>-E</code></dt>
<dd> Enable encryption</dd>
<dt><code>-S</code></dt>
<dd> Secure connection</dd>
<dt><code>-C</code></dt>
<dd> Become the central of a piconet</dd>
<dt><code>-L</code><i>&nbsp;&lt;seconds&gt;</i></dt>
<dd> Set linger timeout</dd></dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>show &lt;</code><i>dev</i>&gt;</dt>
<dd> Display the information about the specified device.</dd>
<dt><code>connect &lt;</code><i>dev</i>&gt; [<i>bdaddr</i>] [<i>channel</i>]</dt>
<dd> Connect the RFCOMM device to the remote Bluetooth device on the specified channel. If no channel is specified, it will use the channel number <code>1</code>. This command can be terminated with the key sequence CTRL-C.</dd>
<dt><code>listen &lt;</code><i>dev</i>&gt; [<i>channel</i>] [<i>cmd</i>]</dt>
<dd> Listen on a specified RFCOMM channel for incoming connections. If no channel is specified, it will use the channel number <code>1</code>, but a channel must be specified before cmd. If cmd is given, it will be executed as soon as a client connects. When the child process terminates or the client disconnect, the command will terminate. Occurrences of {} in cmd will be replaced by the name of the device used by the connection. This command can be terminated with the key sequence CTRL-C.</dd>
<dt><code>watch &lt;</code><i>dev</i>&gt; [<i>channel</i>] [<i>cmd</i>]</dt>
<dd> Watch is identical to listen except that when the child process terminates or the client disconnect, the command will restart listening with the same parameters.</dd>
<dt><code>bind &lt;</code><i>dev</i>&gt; [<i>bdaddr</i>] [<i>channel</i>]</dt>
<dd> This binds the RFCOMM device to a remote Bluetooth device. The command does not establish a connection to the remote device, it only creates the binding. The connection will be established right after an application tries to open the RFCOMM device. If no channel number is specified, it uses the channel number <code>1</code>.</dd>
<dt><code>release &lt;</code><i>dev</i>&gt;</dt>
<dd> This command releases a defined RFCOMM binding. </dd>
<p> If <code>all</code> is specified for the RFCOMM device, then all bindings will be removed.</dl>
<h2>RESOURCES</h2>
<p> <i><a rel="nofollow" href="http://www.bluez.org">http://www.bluez.org</a></i></p>
<h2>REPORTING BUGS</h2>
<p> <i>linux-bluetooth [at] vger.kernel.org</i></p>
<h2>AUTHOR</h2>
<p> Marcel Holtmann &lt;marcel [at] holtmann.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Free use of this software is granted under ther terms of the GNU Lesser General Public Licenses (LGPL). </p>
