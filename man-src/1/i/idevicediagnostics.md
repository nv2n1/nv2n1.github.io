---
title: "idevicediagnostics(1)"
name: "idevicediagnostics"
section: "1"
letter: "i"
url: "/docs/linux/man/1-idevicediagnostics/"
description: "idevicediagnostics – Interact with the diagnostics interface of a device."
---

<h2>NAME</h2>
<p> idevicediagnostics &#8211; Interact with the diagnostics interface of a device.</p>
<h2>SYNOPSIS</h2>
<p> <code>idevicediagnostics</code> [OPTIONS] COMMAND </p>
<h2>DESCRIPTION</h2>
<p> Interact with the diagnostics interface of a device which allows to retrive all kinds of information including diagnostics data, mobilegestalt data, remote access to the IORegistry and certain commands like restart, shutdown and sleep. Only available for iOS 4 and later. Accessing IORegistry is only supported on iOS 5 and later. </p>
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
<dt><code>diagnostics [TYPE]</code></dt>
<dd> print diagnostics information from device optionally by TYPE. This includes &quot;All&quot;, &quot;WiFi&quot;, &quot;GasGauge&quot; or &quot;NAND&quot;. Default is &quot;All&quot;.</dd>
<dt><code>mobilegestalt KEY [&#8230;]</code></dt>
<dd> print values of mobilegestalt keys passed as arguments after the command and seperated by a space.</dd>
<dt><code>ioreg [PLANE]</code></dt>
<dd> print IORegistry of device, optionally by PLANE like &quot;IODeviceTree&quot;, &quot;IOPower&quot;<br />
&nbsp;<wbr>or&nbsp;<wbr>&quot;IOService&quot;. Only available on iOS 5 and later.</dd>
<dt><code>shutdown</code></dt>
<dd> shutdown device</dd>
<dt><code>restart</code></dt>
<dd> restart device</dd>
<dt><code>sleep</code></dt>
<dd> put device into sleep mode which also disconnects it from the host. </dd>
</dl>
<h2>AUTHORS</h2>
<p> Martin Szulecki </p>
<h2>Index</h2>
