---
title: "dfutool(1)"
name: "dfutool"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dfutool/"
description: "dfutool – Device Firmware Upgrade utility"
---

<h2 class="name">NAME</h2>
<p> dfutool &#8211; Device Firmware Upgrade utility </p>
<h2>SYNOPSIS</h2>
<p> <code>dfutool</code> [ <i>options</i> ] &lt; <i>command</i> &gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>dfutool</code> is used to verify, archive and upgrade firmware files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Gives a list of possible commands.</p>
<dt><code>-d</code><i> &lt;device&gt;</i></p>
<dd> The command specifies the device to use.</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>verify</code><i> &lt;dfu-file&gt;</i></p>
<dd> Display information about the firmware file.</p>
<dt><code>modify</code><i> &lt;dfu-file&gt;</i></p>
<dd> Change DFU specific values in the firmware file.</p>
<dt><code>upgrade</code><i> &lt;dfu-file&gt;</i></p>
<dd> Upgrade the device with a new firmware.</p>
<dt><code>archive</code><i> &lt;dfu-file&gt;</i></p>
<dd> Archive the current firmware of the device.</dl>
<h2>AUTHOR</h2>
<p> Written by Marcel Holtmann &lt;marcel [at] holtmann.org&gt;. </p>
<h2>Index</h2>
