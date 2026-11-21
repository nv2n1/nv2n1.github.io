---

title: "idevicepair(1)"
name: "idevicepair"
section: "1"
letter: "i"
url: "/docs/linux/man/1-idevicepair/"
description: "idevicepair – Manage pairings with devices and this host."
---

<p> idevicepair &#8211; Manage pairings with devices and this host.</p>
<h2>SYNOPSIS</h2>
<p> <code>idevicepair</code> [OPTIONS] COMMAND </p>
<h2>DESCRIPTION</h2>
<p> Manage pairings with devices and this host. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-u, &#8211;udid UDID</code></dt>
<dd> target specific device by its 40-digit device UDID.</dd>
<dt><code>-d, &#8211;debug</code></dt>
<dd> enable communication debugging.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> prints usage information. </dd>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>hostid</code></dt>
<dd> print the host id of this computer.</dd>
<dt><code>pair</code></dt>
<dd> pair device with this computer.</dd>
<dt><code>validate</code></dt>
<dd> validate if device is paired with this computer.</dd>
<dt><code>unpair</code></dt>
<dd> unpair device with this computer.</dd>
<dt><code>list</code></dt>
<dd> list devices paired with this computer. </dd>
</dl>
<h2>AUTHORS</h2>
<p> Nikias Bassen </p>
<p> Man page written to conform with Debian by Julien Lavergne. </p>
