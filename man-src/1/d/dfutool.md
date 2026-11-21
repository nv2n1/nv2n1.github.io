---
title: "dfutool(1)"
name: "dfutool"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dfutool/"
description: "dfutool – Device Firmware Upgrade utility"
---

<h2>SYNOPSIS</h2>
<p> <code>dfutool</code> [ <i>options</i> ] &lt; <i>command</i> &gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>dfutool</code> is used to verify, archive and upgrade firmware files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> Gives a list of possible commands.</dd>
<dt><code>-d</code><i> &lt;device&gt;</i></dt>
<dd> The command specifies the device to use.</dd></dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>verify</code><i> &lt;dfu-file&gt;</i></dt>
<dd> Display information about the firmware file.</dd>
<dt><code>modify</code><i> &lt;dfu-file&gt;</i></dt>
<dd> Change DFU specific values in the firmware file.</dd>
<dt><code>upgrade</code><i> &lt;dfu-file&gt;</i></dt>
<dd> Upgrade the device with a new firmware.</dd>
<dt><code>archive</code><i> &lt;dfu-file&gt;</i></dt>
<dd> Archive the current firmware of the device.</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Marcel Holtmann &lt;marcel [at] holtmann.org&gt;. </p>
