---

title: "vboxheadless(1)"
name: "vboxheadless"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vboxheadless/"
description: "VBoxHeadless – x86 virtualization solution"
---

<p> VBoxHeadless &#8211; x86 virtualization solution </p>
<h2>DESCRIPTION</h2>
<p> Oracle VM VirtualBox Headless Interface (C) 2008-2019 Oracle Corporation All rights reserved.</p>
<h3>Usage:</h3>
<dl>
<dt><code>-s</code>, <code>-startvm</code>, <code>&#8211;startvm</code> &lt;name|uuid&gt;</dt>
<dd> Start given VM (required argument)</dd>
<dt><code>-v</code>, <code>-vrde</code>, <code>&#8211;vrde</code> on|off|config</dt>
<dd> Enable or disable the VRDE server or don&#8217;t change the setting (default)</dd>
<dt><code>-e</code>, <code>-vrdeproperty</code>, <code>&#8211;vrdeproperty</code> &lt;name=[value]&gt; Set a VRDE property:</dt>
<dd> &quot;TCP/Ports&quot; &#8211; comma-separated list of</dd>
<dt>ports the VRDE server can bind to; dash</dt>
<dd> between two port numbers specifies range</dd>
<dt>&quot;TCP/Address&quot; &#8211; interface IP the VRDE</dt>
<dd> server will bind to</dd>
<dt><code>&#8211;settingspw</code> &lt;pw&gt;</dt>
<dd> Specify the settings password</dd>
<dt><code>&#8211;settingspwfile</code> &lt;file&gt;</dt>
<dd> Specify a file containing the settings password</dd>
<dt><code>-start-paused</code>, <code>&#8211;start-paused</code></dt>
<dd> Start the VM in paused state</dd>
<dt><code>-c</code>, <code>-record</code>, <code>&#8211;record</code></dt>
<dd> Record the VM screen output to a file</dd>
<dt><code>-w</code>, <code>&#8211;videowidth</code></dt>
<dd> Video frame width when recording</dd>
<dt><code>-h</code>, <code>&#8211;videoheight</code></dt>
<dd> Video frame height when recording</dd>
<dt><code>-r</code>, <code>&#8211;videobitrate</code></dt>
<dd> Recording bit rate when recording</dd>
<dt><code>-f</code>, <code>&#8211;filename</code></dt>
<dd> File name when recording. The codec used will be chosen based on file extension </dd>
</dl>
