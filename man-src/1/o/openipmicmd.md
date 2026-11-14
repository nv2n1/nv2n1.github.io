---
title: "openipmicmd(1)"
name: "openipmicmd"
section: "1"
letter: "o"
url: "/docs/linux/man/1-openipmicmd/"
description: "openipmicmd – An IPMI Command Interface"
---

<h2 class="name">NAME</h2>
<p> openipmicmd &#8211; An IPMI Command Interface</p>
<h2>SYNOPSIS</h2>
<p> <code>openipmicmd</code> [<code>-k</code> <i>entry-to-execute</i>] <code>&lt;connection parms&gt;</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>openipmicmd</code> program allows a user to execute direct IPMI commands. It can work with direct interface with the OpenIPMI driver or with IPMI LAN interfaces. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-k&nbsp;<wbr></code><i>entry-to-execute</i></p>
<dd> Execute a single command an exit. </p>
<dt><code>&lt;connection parms&gt;</code></p>
<dd> The parameters for the connection depend on the connection type. These are all described in openipmi_conparms (7) </p>
</dl>
<h2>COMMANDS</h2>
<p> Once up, you can execute commands in the user interface. Note that commands and responses are asynchronous, you issue a command and the interface returns immediately. When the response comes back, it will be dumped on your console. That&#8217;s a little strange looking, but IPMI is asynchronous underneath. Note that the <code>-k</code> option is synchronous, it will wait for the response or a timeout before returning. </p>
<dl>
<dt><code>0f</code> <i>lun</i> <i>netfn</i> <i>cmd</i> [<i>data1</i> [<i>data2</i> &#8230;]]</p>
<dd> Send a command to the BMC you are connected to. </p>
<dt><i>channel</i> [<code>ipmb</code>] <i>IPMB-addr</i> <i>lun</i> <i>netfn</i> [<code>seq</code>] <i>cmd</i> [<i>data1</i> [<i>data2</i> &#8230;]]</p>
<dd> Send a command to a device on the IPMB bus. The &quot;<code>ipmb</code>&quot; string is optional. The <code>seq</code> must be provided if the netfn is a response (an odd number). It must be the same sequence number that came in on the command in the &quot;Command Sequence = seq&quot; part of the command. </p>
<dt><i>channel</i> <code>00</code> <i>IPMB-addr</i> <i>lun</i> <i>netfn</i> <i>cmd</i> [<i>data1</i> [<i>data2</i> &#8230;]]</p>
<dd> Send a broadcast command to a device on the IPMB bus. </p>
<dt><i>channel</i> <code>lan</code> <i>handle</i> <i>remote-swid</i> <i>local-swid</i> <i>lun</i> <i>netfn</i> <i>cmd</i> [<i>data1</i> [<i>data</i> &#8230;]]</p>
<dd> Send a command to a device over a LAN channel. Note that this not the same as a LAN connection. This sends a message through a local BMC to a remote system that is hooked up with a LAN connection. </p>
<dt><code>test_lat</code> <i>count</i> <i>command</i></p>
<dd> Executes the given <i>commands</i> (one of the previous commands) <i>count</i> times and gives the average time per command to execute. Note that &quot;<i>count</i>&quot; is hexadecimal. </p>
<dt><code>help</code></p>
<dd> Display some help. </p>
<dt><code>regcmd</code> <i>netfn</i> <i>cmd</i></p>
<dd> Register to receive the given command. If the driver receives an external command, it will print it out. This only works with system interface connections, it will not work on LAN connections. </p>
<dt><code>unregcmd</code> <i>netfn</i> <i>cmd</i></p>
<dd> Remove a command registration. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ipmi_ui/">ipmi_ui</a></code>(1), <code><a href="/docs/linux/man/8-ipmilan/">ipmilan</a></code>(8), <code><a href="/docs/linux/man/7-openipmi_conparms/">openipmi_conparms</a></code>(7) </p>
<h2>KNOWN PROBLEMS</h2>
<p> The asynchronous nature of the program can be annoying. </p>
<h2>AUTHOR</h2>
<p> Corey Minyard &lt;cminyard [at] mvista.org&gt; </p>
<h2>Index</h2>
