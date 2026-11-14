---
title: "vboxheadless(1)"
name: "vboxheadless"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vboxheadless/"
description: "VBoxHeadless – x86 virtualization solution"
---

<h2 class="name">NAME</h2>
<p> VBoxHeadless &#8211; x86 virtualization solution </p>
<h2>DESCRIPTION</h2>
<p> Oracle VM VirtualBox Headless Interface (C) 2008-2019 Oracle Corporation All rights reserved.</p>
<h3>Usage:</h3>
<dl>
<dt><code>-s</code>, <code>-startvm</code>, <code>&#8211;startvm</code> &lt;name|uuid&gt;</p>
<dd> Start given VM (required argument)</p>
<dt><code>-v</code>, <code>-vrde</code>, <code>&#8211;vrde</code> on|off|config</p>
<dd> Enable or disable the VRDE server or don&#8217;t change the setting (default)</p>
<dt><code>-e</code>, <code>-vrdeproperty</code>, <code>&#8211;vrdeproperty</code> &lt;name=[value]&gt; Set a VRDE property:</p>
<dd> &quot;TCP/Ports&quot; &#8211; comma-separated list of</p>
<dt>ports the VRDE server can bind to; dash</p>
<dd> between two port numbers specifies range</p>
<dt>&quot;TCP/Address&quot; &#8211; interface IP the VRDE</p>
<dd> server will bind to</p>
<dt><code>&#8211;settingspw</code> &lt;pw&gt;</p>
<dd> Specify the settings password</p>
<dt><code>&#8211;settingspwfile</code> &lt;file&gt;</p>
<dd> Specify a file containing the settings password</p>
<dt><code>-start-paused</code>, <code>&#8211;start-paused</code></p>
<dd> Start the VM in paused state</p>
<dt><code>-c</code>, <code>-record</code>, <code>&#8211;record</code></p>
<dd> Record the VM screen output to a file</p>
<dt><code>-w</code>, <code>&#8211;videowidth</code></p>
<dd> Video frame width when recording</p>
<dt><code>-h</code>, <code>&#8211;videoheight</code></p>
<dd> Video frame height when recording</p>
<dt><code>-r</code>, <code>&#8211;videobitrate</code></p>
<dd> Recording bit rate when recording</p>
<dt><code>-f</code>, <code>&#8211;filename</code></p>
<dd> File name when recording. The codec used will be chosen based on file extension </p>
</dl>
<h2>Index</h2>
