---
title: "hciemu(1)"
name: "hciemu"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hciemu/"
description: "hciemu – HCI emulator"
---

<h2>SYNOPSIS</h2>
<p> <code>hciemu</code> [<i>options</i>] <i>local_address</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>hciemu</code> is used to emulate an HCI via <code>hci_vhci</code> kernel module </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d&nbsp;<wbr></code><i>device</i></dt>
<dd> use specified <i>device</i></dd>
<dt><code>-b&nbsp;<wbr></code><i>bdaddr</i></dt>
<dd> emulate <i>bdaddr</i></dd>
<dt><code>-s&nbsp;<wbr></code><i>file</i></dt>
<dd> create snoop file <i>file</i></dd>
<dt><code>-n</code></dt>
<dd> do not detach </dd>
</dl>
<h2>AUTHORS</h2>
<p> Written by Marcel Holtmann &lt;marcel [at] holtmann.org&gt; and Maxim Krasnyansky &lt;maxk [at] qualcomm.com&gt;, man page by Filippo Giunchedi &lt;filippo [at] debian.org&gt; </p>
