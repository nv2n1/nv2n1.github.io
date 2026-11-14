---
title: "amttool(1)"
name: "amttool"
section: "1"
letter: "a"
url: "/docs/linux/man/1-amttool/"
description: "amttool – remotely control Intel AMT managed machines."
---

<h2>NAME</h2>
<p> amttool &#8211; remotely control Intel AMT managed machines.</p>
<h2>SYNOPSIS</h2>
<p> <code>amttool host [ command ] [ arg(s) ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>amttool</code> is a perl script which speaks SOAP to Intel AMT managed machines. It can query informations about the machine in question and also send some commands for basic remote control. </p>
<p> <code>host</code> is the hostname or IP address of the machine amttool should control. <code>command</code> is an optional command. </p>
<p> You must set fill AMT_PASSWORD environment variable with the AMT password. </p>
<p> For more inforamtions on Intel AMT check <a href="/docs/linux/man/7-amt-howto/">amt-howto</a>(7).</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>info</code></p>
<dd> gather information (default).</p>
<dt><code>reset [ special ]</code></p>
<dd> reset machine, with optional special command (see section below).</p>
<dt><code>powerup [ special ]</code></p>
<dd> turn on machine.</p>
<dt><code>powerdown</code></p>
<dd> turn off machine.</p>
<dt><code>powercycle [ special ]</code></p>
<dd> powercycle machine.</p>
<dt><code>netinfo</code></p>
<dd> print network configuration (requires AMT 2.5+).</p>
<dt><code>netconf if link [ ip mask gw [ dns1 [ dns2 ]]]</code></p>
<dd> configure network interface (requires AMT 2.5+). <code>if</code> is the interface handle, <code>link</code> the link policy. If in doubt just feed in what the netinfo command prints. <code>ip</code> is the IPv4 address, <code>mask</code> the netmask, <code>gw</code> the default gateway, <code>dns1</code> and <code>dns2</code> are the DNS Servers. If no IP configuration is specified the tool tries to configure the machine in shared mac address mode with dhcp, otherwise in separate mac address mode with static IP address. Default for dns1 is the gateway address, for dns2 it is 0.0.0.0.</dl>
<h2>SPECIAL COMMANDS</h2>
<p> Special commands can optionally be specified for reset, powerup and powercycle. They change the default boot behavior of the machine.</p>
<dl>
<dt><code>bios</code></p>
<dd> Asks for the BIOS boot messages being redirected to serial-over-lan.</p>
<dt><code>pxe</code></p>
<dd> Network boot via PXE.</p>
<dt><code>hd</code></p>
<dd> Boot from local disk.</p>
<dt><code>hdsafe</code></p>
<dd> Boot from local disk (safe mode).</p>
<dt><code>cd</code></p>
<dd> Boot from CD/DVD.</p>
<dt><code>diag</code></p>
<dd> Boot in diagnostics mode.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>AMT_PASSWORD</code></p>
<dd> AMT password.</p>
<dt><code>AMT_DEBUG</code></p>
<dd> Enable debug output.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-amtterm/">amtterm</a>(1), <a href="/docs/linux/man/1-gamt/">gamt</a>(1), <a href="/docs/linux/man/7-amt-howto/">amt-howto</a>(7)</p>
<h2>AUTHOR</h2>
<p> (c) 2007 Gerd Hoffmann &lt;kraxel [at] redhat.com&gt; </p>
<h2>Index</h2>
