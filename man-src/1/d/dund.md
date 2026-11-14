---
title: "dund(1)"
name: "dund"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dund/"
description: "dund – BlueZ Bluetooth dial-up networking daemon"
---

<h2>NAME</h2>
<p> dund &#8211; BlueZ Bluetooth dial-up networking daemon</p>
<h2>DESCRIPTION</h2>
<p> DUN daemon</p>
<h2>SYNOPSIS</h2>
<p> dund &lt;options&gt; [pppd options]</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;show</code> <code>&#8211;list</code> <code>-l</code></p>
<dd> Show active DUN connections</p>
<dt><code>&#8211;listen</code> <code>-s</code></p>
<dd> Listen for DUN connections</p>
<dt><code>&#8211;dialup</code> <code>-u</code></p>
<dd> Listen for dialup/telephone connections</p>
<dt><code>&#8211;connect</code> <code>-c</code> &lt;bdaddr&gt;</p>
<dd> Create DUN connection</p>
<dt><code>&#8211;mrouter</code> <code>-m</code> &lt;bdaddr&gt;</p>
<dd> Create mRouter connection</p>
<dt><code>&#8211;search</code> <code>-Q[duration]</code></p>
<dd> Search and connect</p>
<dt><code>&#8211;kill</code> <code>-k</code> &lt;bdaddr&gt;</p>
<dd> Kill DUN connection</p>
<dt><code>&#8211;killall</code> <code>-K</code></p>
<dd> Kill all DUN connections</p>
<dt><code>&#8211;channel</code> <code>-C</code> &lt;channel&gt;</p>
<dd> RFCOMM channel</p>
<dt><code>&#8211;device</code> <code>-i</code> &lt;bdaddr&gt;</p>
<dd> Source bdaddr</p>
<dt><code>&#8211;nosdp</code> <code>-D</code></p>
<dd> Disable SDP</p>
<dt><code>&#8211;auth</code> <code>-A</code></p>
<dd> Enable authentification</p>
<dt><code>&#8211;encrypt</code> <code>-E</code></p>
<dd> Enable encryption</p>
<dt><code>&#8211;secure</code> <code>-S</code></p>
<dd> Secure connection</p>
<dt><code>&#8211;master</code> <code>-M</code></p>
<dd> Become the master of a piconet</p>
<dt><code>&#8211;nodetach</code> <code>-n</code></p>
<dd> Do not become a daemon</p>
<dt><code>&#8211;persist</code> <code>-p[interval]</code></p>
<dd> Persist mode</p>
<dt><code>&#8211;pppd</code> <code>-d</code> &lt;pppd&gt;</p>
<dd> Location of the PPP daemon (pppd)</p>
<dt><code>&#8211;msdun</code> <code>-X</code> [timeo]</p>
<dd> Enable Microsoft dialup networking support</p>
<dt><code>&#8211;activesync</code> <code>-a</code></p>
<dd> Enable Microsoft ActiveSync networking</p>
<dt><code>&#8211;cache</code> <code>-C</code> [valid]</p>
<dd> Enable address cache </p>
</dl>
<h2>Index</h2>
