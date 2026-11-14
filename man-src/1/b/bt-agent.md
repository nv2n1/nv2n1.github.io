---
title: "bt-agent(1)"
name: "bt-agent"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bt-agent/"
description: "bt-adapter – a bluetooth agent"
---

<h2 class="name">NAME</h2>
<p> bt-adapter &#8211; a bluetooth agent </p>
<h2>SYNOPSIS</h2>
<p> bt-agent [<font SIZE="-1">OPTION&#8230;</font>] </p>
<p> Help Options:<br />
&nbsp;<wbr>&nbsp;<wbr>-h, &#8211;help </p>
<p> Application Options:<br />
&nbsp;<wbr>&nbsp;<wbr>-c, &#8211;capability=&lt;capability&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>-p, &#8211;pin<br />
&nbsp;<wbr>&nbsp;<wbr>-d, &#8211;daemon</p>
<h2>DESCRIPTION</h2>
<p> This interactive utility is used to manage incoming Bluetooth requests (eg. request of pincode, request of authorize a connection/service request, etc).</p>
<h2>OPTIONS</h2>
<p> <code>-h, &#8211;help</code><br />
&nbsp;<wbr>Show help </p>
<p> <code>-c, &#8211;capability &lt;capability&gt;</code><br />
&nbsp;<wbr>Specify the input and output capabilities of the agent.<br />
&nbsp;<wbr>`capability`&nbsp;<wbr>can be one of:<br />
&nbsp;<wbr>&nbsp;<wbr>DisplayOnly<br />
&nbsp;<wbr>&nbsp;<wbr>DisplayYesNo&nbsp;<wbr>(default)<br />
&nbsp;<wbr>&nbsp;<wbr>KeyboardOnly<br />
&nbsp;<wbr>&nbsp;<wbr>NoInputNoOutput<br />
&nbsp;<wbr>(if this option does not defined &#8211;&nbsp;<wbr>`DisplayYesNo&#8217;&nbsp;<wbr>will be used) </p>
<p> <code>-p, &#8211;pin &lt;file path&lt;gt</code>&gt;<br />
&nbsp;<wbr>Use a file that holds a list of authorization codes for each device by name or mac address.<br />
&nbsp;<wbr>The contents of the file should be in this format:<br />
&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">AA:BB:CC:DD:EE:FF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>123456&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr></font>&nbsp;<wbr>RemoteDeviceName&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(accept any pin code)<br />
&nbsp;<wbr>If a pin file is included, it will check the passkey of the pairing device against the key included in the file. It will automatically authorize the device if the key matches, otherwise it will request the user for manual authorization. </p>
<p> <code>-d, &#8211;daemon</code><br />
&nbsp;<wbr>Run the agent as a background process&nbsp;<wbr>(as a daemon).<br />
&nbsp;<wbr>The agent will rely on a pin file and request no manual user authorization. Any devices that attempt to pair without a valid passkey defined in the pin file will be automatically rejected.</p>
<h2>AUTHOR</h2>
<p> Alexander Orlenko &lt;zxteam [at] gmail.com&gt;.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-bt-adapter/">bt-adapter</a></i>(1) <i><a href="/docs/linux/man/1-bt-device/">bt-device</a></i>(1) <i><a href="/docs/linux/man/1-bt-network/">bt-network</a></i>(1) </p>
<h2>Index</h2>
