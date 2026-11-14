---
title: "bt-adapter(1)"
name: "bt-adapter"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bt-adapter/"
description: "bt-adapter – a bluetooth adapter manager"
---

<h2 class="name">NAME</h2>
<p> bt-adapter &#8211; a bluetooth adapter manager </p>
<h2>SYNOPSIS</h2>
<p> bt-adapter [<font SIZE="-1">OPTION&#8230;</font>] </p>
<p> Help Options:<br />
&nbsp;<wbr>&nbsp;<wbr>-h, &#8211;help </p>
<p> Application Options:<br />
&nbsp;<wbr>&nbsp;<wbr>-l, &#8211;list<br />
&nbsp;<wbr>&nbsp;<wbr>-a, &#8211;adapter=&lt;name|mac&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>-i, &#8211;info<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;discover<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;set&nbsp;<wbr>&lt;property&gt;&nbsp;<wbr>&lt;value&gt;</p>
<h2>DESCRIPTION</h2>
<p> This utility is used to manage Bluetooth adapters. You can list all available adapters, show information about adapter, change adapter properties or discover remote devices.</p>
<h2>OPTIONS</h2>
<p> <code>-h, &#8211;help</code><br />
&nbsp;<wbr>Show help </p>
<p> <code>-l, &#8211;list</code><br />
&nbsp;<wbr>List all available adapters </p>
<p> <code>-a, &#8211;adapter &lt;name|mac&gt;</code><br />
&nbsp;<wbr>Specify adapter to use by his Name or&nbsp;<wbr><font SIZE="-1">MAC</font>&nbsp;<wbr>address<br />
&nbsp;<wbr>(if this option does not defined &#8211; default adapter used) </p>
<p> <code>-i, &#8211;info</code><br />
&nbsp;<wbr>Show information about adapter&nbsp;<wbr>(returns all properties) </p>
<p> <code>-d, &#8211;discover</code><br />
&nbsp;<wbr>Discover remote devices&nbsp;<wbr>(with remote device name resolving) </p>
<p> <code>&#8211;set &lt;property&gt; &lt;value&gt;</code><br />
&nbsp;<wbr>Change adapter properties&nbsp;<wbr>(see&nbsp;<wbr><font SIZE="-1">ADAPTER PROPERTIES</font>&nbsp;<wbr>section for list<br />
&nbsp;<wbr>of available properties)</p>
<h2>ADAPTER PROPERTIES</h2>
<p> string Address [ro]<br />
&nbsp;<wbr>&nbsp;<wbr>The Bluetooth adapter address&nbsp;<wbr>(<font SIZE="-1">MAC</font>). </p>
<p> string Alias [rw]<br />
&nbsp;<wbr>&nbsp;<wbr>The Bluetooth adapter friendly name. </p>
<p> uint32 Class [ro]<br />
&nbsp;<wbr>&nbsp;<wbr>The Bluetooth class of device. </p>
<p> boolean Powered [rw]<br />
&nbsp;<wbr>&nbsp;<wbr>Switch an adapter on or off. This will also set the<br />
&nbsp;<wbr>&nbsp;<wbr>appropiate connectable state. </p>
<p> boolean Discoverable [rw]<br />
&nbsp;<wbr>&nbsp;<wbr>Switch an adapter to discoverable or non-discoverable<br />
&nbsp;<wbr>&nbsp;<wbr>to either make it visible or hide it. </p>
<pre>
        If the DiscoverableTimeout is set to a non-zero
        value then the system will set this value back to
        false after the timer expired.
        In case the adapter is switched off, setting this
        value will fail.
</pre>
<p> boolean Pairable [rw]<br />
&nbsp;<wbr>&nbsp;<wbr>Switch an adapter to pairable or non-pairable. </p>
<pre>
        Note that this property only affects incoming pairing
        requests.
</pre>
<p> uint32 PaireableTimeout [rw]<br />
&nbsp;<wbr>&nbsp;<wbr>The pairable timeout in seconds. A value of zero<br />
&nbsp;<wbr>&nbsp;<wbr>means that the timeout is disabled and it will stay in<br />
&nbsp;<wbr>&nbsp;<wbr>pareable mode forever. </p>
<p> uint32 DiscoverableTimeout [rw]<br />
&nbsp;<wbr>&nbsp;<wbr>The discoverable timeout in seconds. A value of zero<br />
&nbsp;<wbr>&nbsp;<wbr>means that the timeout is disabled and it will stay in<br />
&nbsp;<wbr>&nbsp;<wbr>discoverable/limited mode forever. </p>
<pre>
        The default value for the discoverable timeout should
        be 180 seconds (3 minutes).
</pre>
<p> boolean Discovering [ro]<br />
&nbsp;<wbr>&nbsp;<wbr>Indicates that a device discovery procedure is active. </p>
<p> list UUIDs [ro]<br />
&nbsp;<wbr>&nbsp;<wbr>List of 128-bit UUIDs that represents the available local<br />
&nbsp;<wbr>&nbsp;<wbr>services.</p>
<h2>AUTHOR</h2>
<p> Alexander Orlenko &lt;zxteam [at] gmail.com&gt;.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-bt-agent/">bt-agent</a></i>(1) <i><a href="/docs/linux/man/1-bt-device/">bt-device</a></i>(1) <i><a href="/docs/linux/man/1-bt-network/">bt-network</a></i>(1) </p>
<h2>Index</h2>
