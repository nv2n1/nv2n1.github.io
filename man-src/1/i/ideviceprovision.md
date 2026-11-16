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
<dt><code>-u, &#8211;udid UDID</code></dt>
<dd> target specific device by its 40-digit device UDID.</dd>
<dt><code>-d, &#8211;debug</code></dt>
<dd> enable communication debugging.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> prints usage information. </dd>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>install FILE</code></dt>
<dd> Install the provisioning profile specified by FILE. A valid &quot;.mobileprovision&quot; file is expected.</dd>
<dt><code>list</code></dt>
<dd> Get a list of all provisioning profiles on the device.</dd>
<dt><code>copy PATH</code></dt>
<dd> Retrieves all provisioning profiles from the device and stores them into the existing directory specified by PATH. The files will be stored as &quot;UUID.mobileprovision&quot;.</dd>
<dt><code>remove UUID</code></dt>
<dd> Removes the provisioning profile identified by UUID. </dd>
</dl>
<h2>AUTHORS</h2>
<p> Nikias Bassen </p>
<h2>Index</h2>
