---
title: "bt-device(1)"
name: "bt-device"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bt-device/"
description: "bt-device – a bluetooth device manager"
---

<h2 class="name">NAME</h2>
<p> bt-device &#8211; a bluetooth device manager </p>
<h2>SYNOPSIS</h2>
<p> bt-device [<font SIZE="-1">OPTION&#8230;</font>] </p>
<p> Help Options:<br />
&nbsp;<wbr>&nbsp;<wbr>-h, &#8211;help </p>
<p> Application Options:<br />
&nbsp;<wbr>&nbsp;<wbr>-a, &#8211;adapter=&lt;name|mac&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>-l, &#8211;list<br />
&nbsp;<wbr>&nbsp;<wbr>-c, &#8211;connect=&lt;mac&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;disconnect=&lt;name|mac&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>-r, &#8211;remove=&lt;name|mac&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>-i, &#8211;info=&lt;name|mac&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;services&nbsp;<wbr>&lt;name|mac&gt;&nbsp;<wbr>[&lt;pattern&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;set&nbsp;<wbr>&lt;name|mac&gt;&nbsp;<wbr>&lt;property&gt;&nbsp;<wbr>&lt;value&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>-v, &#8211;verbose</p>
<h2>DESCRIPTION</h2>
<p> This utility is used to manage Bluetooth devices. You can list added devices, connect to a new device, disconnect device, remove added device, show info about device, discover remote device services or change device properties.</p>
<h2>OPTIONS</h2>
<p> <code>-h, &#8211;help</code><br />
&nbsp;<wbr>Show help </p>
<p> <code>-a, &#8211;adapter &lt;name|mac&gt;</code><br />
&nbsp;<wbr>Specify adapter to use by his Name or&nbsp;<wbr><font SIZE="-1">MAC</font>&nbsp;<wbr>address<br />
&nbsp;<wbr>(if this option does not defined &#8211; default adapter used) </p>
<p> <code>-l, &#8211;list</code><br />
&nbsp;<wbr>List added devices </p>
<p> <code>-c, &#8211;connect &lt;mac&gt;</code><br />
&nbsp;<wbr>Connect to the remote device by his&nbsp;<wbr><font SIZE="-1">MAC,</font>&nbsp;<wbr>retrieve all&nbsp;<wbr><font SIZE="-1">SDP<br />
</font>&nbsp;<wbr>records and then initiate the pairing </p>
<p> <code>-d, &#8211;disconnect &lt;name|mac&gt;</code><br />
&nbsp;<wbr>Disconnects a specific remote device by terminating the<br />
&nbsp;<wbr>low-level&nbsp;<wbr><font SIZE="-1">ACL</font>&nbsp;<wbr>connection. </p>
<p> <code>-r, &#8211;remove</code><br />
&nbsp;<wbr>Remove device&nbsp;<wbr>(and also the pairing information) </p>
<p> <code>-i, &#8211;info</code><br />
&nbsp;<wbr>Show information about device&nbsp;<wbr>(returns all properties) </p>
<p> <code>-s, &#8211;services &lt;name|mac&gt; [&lt;pattern&gt;]</code><br />
&nbsp;<wbr>Starts the service discovery to retrieve remote service records,<br />
&nbsp;<wbr>the&nbsp;<wbr>`pattern`&nbsp;<wbr>parameter can be used to specify specific UUIDs </p>
<p> <code>&#8211;set &lt;property&gt; &lt;value&gt;</code><br />
&nbsp;<wbr>Change device properties&nbsp;<wbr>(see&nbsp;<wbr><font SIZE="-1">DEVICE PROPERTIES</font>&nbsp;<wbr>section for list<br />
&nbsp;<wbr>of available properties) </p>
<p> <code>-v, &#8211;verbose</code><br />
&nbsp;<wbr>Verbosely display remote service records&nbsp;<wbr>(affect to service<br />
&nbsp;<wbr>discovery mode)</p>
<h2>DEVICE PROPERTIES</h2>
<p> string Address [ro]<br />
&nbsp;<wbr>&nbsp;<wbr>The Bluetooth device address&nbsp;<wbr>(<font SIZE="-1">MAC</font>)&nbsp;<wbr>of the remote device. </p>
<p> string Name [ro]<br />
&nbsp;<wbr>&nbsp;<wbr>The Bluetooth remote device name. </p>
<p> string Icon [ro]<br />
&nbsp;<wbr>&nbsp;<wbr>Proposed icon name according to the freedesktop.org<br />
&nbsp;<wbr>&nbsp;<wbr>icon naming specification. </p>
<p> uint32 Class [ro]<br />
&nbsp;<wbr>&nbsp;<wbr>The Bluetooth class of device of the remote device. </p>
<p> list UUIDs [ro]<br />
&nbsp;<wbr>&nbsp;<wbr>List of 128-bit UUIDs that represents the available<br />
&nbsp;<wbr>&nbsp;<wbr>remote services. </p>
<p> boolean Paired [ro]<br />
&nbsp;<wbr>&nbsp;<wbr>Indicates if the remote device is paired. </p>
<p> boolean Connected [ro]<br />
&nbsp;<wbr>&nbsp;<wbr>Indicates if the remote device is currently connected. </p>
<p> boolean Trusted [rw]<br />
&nbsp;<wbr>&nbsp;<wbr>Indicates if the remote is seen as trusted. </p>
<p> boolean Blocked [rw]<br />
&nbsp;<wbr>&nbsp;<wbr>If set to true any incoming connections from the<br />
&nbsp;<wbr>&nbsp;<wbr>device will be immediately rejected. </p>
<p> string Alias [rw]<br />
&nbsp;<wbr>&nbsp;<wbr>The name alias for the remote device. The alias can<br />
&nbsp;<wbr>&nbsp;<wbr>be used to have a different friendly name for the<br />
&nbsp;<wbr>&nbsp;<wbr>remote device. </p>
<pre>
        In case no alias is set, it will return the remote
        device name. Setting an empty string as alias will
        convert it back to the remote device name.
</pre>
<p> boolean LegacyPairing [ro]<br />
&nbsp;<wbr>&nbsp;<wbr>Set to true if the device only supports the pre-2.1<br />
&nbsp;<wbr>&nbsp;<wbr>pairing mechanism.</p>
<h2>AUTHOR</h2>
<p> Alexander Orlenko &lt;zxteam [at] gmail.com&gt;.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-bt-adapter/">bt-adapter</a></i>(1) <i><a href="/docs/linux/man/1-bt-agent/">bt-agent</a></i>(1) <i><a href="/docs/linux/man/1-bt-network/">bt-network</a></i>(1) </p>
<h2>Index</h2>
