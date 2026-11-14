---
title: "ideviceprovision(1)"
name: "ideviceprovision"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ideviceprovision/"
description: "ideviceprovision – Manage provisioning profiles on a device."
---

<h2>NAME</h2>
<p> ideviceprovision &#8211; Manage provisioning profiles on a device.</p>
<h2>SYNOPSIS</h2>
<p> <code>ideviceprovision</code> [OPTIONS] COMMAND </p>
<h2>DESCRIPTION</h2>
<p> Manage provisioning profiles on a device. </p>
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
<dt><code>install FILE</code></p>
<dd> Install the provisioning profile specified by FILE. A valid &quot;.mobileprovision&quot; file is expected.</p>
<dt><code>list</code></p>
<dd> Get a list of all provisioning profiles on the device.</p>
<dt><code>copy PATH</code></p>
<dd> Retrieves all provisioning profiles from the device and stores them into the existing directory specified by PATH. The files will be stored as &quot;UUID.mobileprovision&quot;.</p>
<dt><code>remove UUID</code></p>
<dd> Removes the provisioning profile identified by UUID. </p>
</dl>
<h2>AUTHORS</h2>
<p> Nikias Bassen </p>
<h2>Index</h2>
