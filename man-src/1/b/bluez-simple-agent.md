---
title: "bluez-simple-agent(1)"
name: "bluez-simple-agent"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bluez-simple-agent/"
description: "bluez-simple-agent – A PIN management and agent program for pairing to Bluetooth device."
---

<h2>SYNOPSIS</h2>
<dl>
<dt> <code>bluez-simple-agent [&lt;hciX&gt;] [&lt;bdaddr&gt;] [remove]</code></dt></dl>
<h2>DESCRIPTION</h2>
<dd>bluez-simple-agent is pass agent program for bluetooth.</dd>
<h2>OPTIONS</h2>
<p> <code>&lt;hciX&gt;</code></p>
<dl>
<dt>
</dt><dd> The command is applied to device hciX , which must be the name of an installed Blue- tooth device. If not specified, the command will be sent to the first available Blue- tooth device.</dd></dl>
<p> <code>&lt;bdaddr&gt;</code></p>
<dl>
<dt>
</dt><dd> bdaddr of device doing pairing.</dd></dl>
<p> <code>remove</code></p>
<dl>
<dt>
</dt><dd> Remove intended bdaddr from database.</dd></dl>
<h2>AUTHOR</h2>
<p> <code>Nobuhiro Iwamatsu</code> &lt;iwamatsu [at] nigauri.org&gt;</p>
<dl>
<dt>
</dt><dd> Wrote this manpage for the Debian system.</dd></dl>
