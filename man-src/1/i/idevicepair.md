---
title: "idevicepair(1)"
name: "idevicepair"
section: "1"
letter: "i"
url: "/docs/linux/man/1-idevicepair/"
description: "idevicepair – Manage pairings with devices and this host."
---

<h2>NAME</h2>
<p> idevicepair &#8211; Manage pairings with devices and this host.</p>
<h2>SYNOPSIS</h2>
<p> <code>idevicepair</code> [OPTIONS] COMMAND </p>
<h2>DESCRIPTION</h2>
<p> Manage pairings with devices and this host. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-u, &#8211;udid UDID</code></p>
<dd> target specific device by its 40-digit device UDID.</p>
<dt><code>-d, &#8211;debug</code></p>
<dd> enable communication debugging.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> prints usage information. </p>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>hostid</code></p>
<dd> print the host id of this computer.</p>
<dt><code>pair</code></p>
<dd> pair device with this computer.</p>
<dt><code>validate</code></p>
<dd> validate if device is paired with this computer.</p>
<dt><code>unpair</code></p>
<dd> unpair device with this computer.</p>
<dt><code>list</code></p>
<dd> list devices paired with this computer. </p>
</dl>
<h2>AUTHORS</h2>
<p> Nikias Bassen </p>
<p> Man page written to conform with Debian by Julien Lavergne. </p>
<h2>Index</h2>
