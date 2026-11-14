---
title: "bt-network(1)"
name: "bt-network"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bt-network/"
description: "bt-network – a bluetooth network manager"
---

<h2 class="name">NAME</h2>
<p> bt-network &#8211; a bluetooth network manager </p>
<h2>SYNOPSIS</h2>
<p> bt-network [<font SIZE="-1">OPTION&#8230;</font>] </p>
<p> Help Options:<br />
&nbsp;<wbr>&nbsp;<wbr>-h, &#8211;help </p>
<p> Application Options:<br />
&nbsp;<wbr>&nbsp;<wbr>-a, &#8211;adapter=&lt;name|mac&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>-c, &#8211;connect&nbsp;<wbr>&lt;name|mac&gt;&nbsp;<wbr>&lt;uuid&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>-s, &#8211;server&nbsp;<wbr>&lt;gn|panu|nap&gt;&nbsp;<wbr>&lt;brige&gt;</p>
<h2>DESCRIPTION</h2>
<p> This utility is used to manage network services (client/server). All servers will be automatically unregistered when the application terminates.</p>
<h2>OPTIONS</h2>
<p> <code>-h, &#8211;help</code><br />
&nbsp;<wbr>Show help </p>
<p> <code>-a, &#8211;adapter &lt;name|mac&gt;</code><br />
&nbsp;<wbr>Specify adapter to use by his Name or&nbsp;<wbr><font SIZE="-1">MAC</font>&nbsp;<wbr>address<br />
&nbsp;<wbr>(if this option does not defined &#8211; default adapter used) </p>
<p> <code>-c, &#8211;connect &lt;name|mac&gt; &lt;uuid&gt;</code><br />
&nbsp;<wbr>Connect to the network device and return the network interface<br />
&nbsp;<wbr>name, uuid can be either one of&nbsp;<wbr>&#8220;gn&#8221;,&nbsp;<wbr>&#8220;panu&#8221;&nbsp;<wbr>or&nbsp;<wbr>&#8220;nap&#8221; </p>
<p> <code>-s, &#8211;server &lt;gn|panu|nap&gt; &lt;brige&gt;</code><br />
&nbsp;<wbr>Register server for the provided&nbsp;<wbr><font SIZE="-1">UUID,</font>&nbsp;<wbr>every new connection to<br />
&nbsp;<wbr>this server will be added the bridge interface</p>
<h2>AUTHOR</h2>
<p> Alexander Orlenko &lt;zxteam [at] gmail.com&gt;.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-bt-adapter/">bt-adapter</a></i>(1) <i><a href="/docs/linux/man/1-bt-agent/">bt-agent</a></i>(1) <i><a href="/docs/linux/man/1-bt-device/">bt-device</a></i>(1) </p>
<h2>Index</h2>
