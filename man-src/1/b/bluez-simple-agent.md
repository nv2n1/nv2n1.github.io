---
title: "bluez-simple-agent(1)"
name: "bluez-simple-agent"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bluez-simple-agent/"
description: "bluez-simple-agent – A PIN management and agent program for pairing to Bluetooth device."
---

<h2 class="name">NAME</h2>
<p> bluez-simple-agent &#8211; A PIN management and agent program for pairing to Bluetooth device. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>bluez-simple-agent [&lt;hciX&gt;] [&lt;bdaddr&gt;] [remove]</code></dl>
<h2>DESCRIPTION</h2>
<dd>bluez-simple-agent is pass agent program for bluetooth.</p>
<h2>OPTIONS</h2>
<p> <code>&lt;hciX&gt;</code></p>
<dl>
<dt>
<dd> The command is applied to device hciX , which must be the name of an installed Blue- tooth device. If not specified, the command will be sent to the first available Blue- tooth device.</dl>
<p> <code>&lt;bdaddr&gt;</code></p>
<dl>
<dt>
<dd> bdaddr of device doing pairing.</dl>
<p> <code>remove</code></p>
<dl>
<dt>
<dd> Remove intended bdaddr from database.</dl>
<h2>AUTHOR</h2>
<p> <code>Nobuhiro Iwamatsu</code> &lt;iwamatsu [at] nigauri.org&gt;</p>
<dl>
<dt>
<dd> Wrote this manpage for the Debian system.</dl>
<h2>Index</h2>
