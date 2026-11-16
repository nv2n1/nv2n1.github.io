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
<dt><code>&#8211;show</code> <code>&#8211;list</code> <code>-l</code></dt>
<dd> Show active DUN connections</dd>
<dt><code>&#8211;listen</code> <code>-s</code></dt>
<dd> Listen for DUN connections</dd>
<dt><code>&#8211;dialup</code> <code>-u</code></dt>
<dd> Listen for dialup/telephone connections</dd>
<dt><code>&#8211;connect</code> <code>-c</code> &lt;bdaddr&gt;</dt>
<dd> Create DUN connection</dd>
<dt><code>&#8211;mrouter</code> <code>-m</code> &lt;bdaddr&gt;</dt>
<dd> Create mRouter connection</dd>
<dt><code>&#8211;search</code> <code>-Q[duration]</code></dt>
<dd> Search and connect</dd>
<dt><code>&#8211;kill</code> <code>-k</code> &lt;bdaddr&gt;</dt>
<dd> Kill DUN connection</dd>
<dt><code>&#8211;killall</code> <code>-K</code></dt>
<dd> Kill all DUN connections</dd>
<dt><code>&#8211;channel</code> <code>-C</code> &lt;channel&gt;</dt>
<dd> RFCOMM channel</dd>
<dt><code>&#8211;device</code> <code>-i</code> &lt;bdaddr&gt;</dt>
<dd> Source bdaddr</dd>
<dt><code>&#8211;nosdp</code> <code>-D</code></dt>
<dd> Disable SDP</dd>
<dt><code>&#8211;auth</code> <code>-A</code></dt>
<dd> Enable authentification</dd>
<dt><code>&#8211;encrypt</code> <code>-E</code></dt>
<dd> Enable encryption</dd>
<dt><code>&#8211;secure</code> <code>-S</code></dt>
<dd> Secure connection</dd>
<dt><code>&#8211;master</code> <code>-M</code></dt>
<dd> Become the master of a piconet</dd>
<dt><code>&#8211;nodetach</code> <code>-n</code></dt>
<dd> Do not become a daemon</dd>
<dt><code>&#8211;persist</code> <code>-p[interval]</code></dt>
<dd> Persist mode</dd>
<dt><code>&#8211;pppd</code> <code>-d</code> &lt;pppd&gt;</dt>
<dd> Location of the PPP daemon (pppd)</dd>
<dt><code>&#8211;msdun</code> <code>-X</code> [timeo]</dt>
<dd> Enable Microsoft dialup networking support</dd>
<dt><code>&#8211;activesync</code> <code>-a</code></dt>
<dd> Enable Microsoft ActiveSync networking</dd>
<dt><code>&#8211;cache</code> <code>-C</code> [valid]</dt>
<dd> Enable address cache </dd>
</dl>
<h2>Index</h2>
