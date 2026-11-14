---
title: "pand(1)"
name: "pand"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pand/"
description: "pand – BlueZ Bluetooth PAN daemon"
---

<h2>NAME</h2>
<p> pand &#8211; BlueZ Bluetooth PAN daemon</p>
<h2>DESCRIPTION</h2>
<p> The pand PAN daemon allows your computer to connect to ethernet networks using Bluetooth.</p>
<h2>SYNPOSIS</h2>
<p> pand &lt;options&gt;</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;show</code> <code>&#8211;list</code> <code>-l</code></p>
<dd> Show active PAN connections</p>
<dt><code>&#8211;listen</code> <code>-s</code></p>
<dd> Listen for PAN connections</p>
<dt><code>&#8211;connect</code> <code>-c</code> &lt;bdaddr&gt;</p>
<dd> Create PAN connection</p>
<dt><code>&#8211;search</code> <code>-Q[duration]</code></p>
<dd> Search and connect</p>
<dt><code>&#8211;kill</code> <code>-k</code> &lt;bdaddr&gt;</p>
<dd> Kill PAN connection</p>
<dt><code>&#8211;killall</code> <code>-K</code></p>
<dd> Kill all PAN connections</p>
<dt><code>&#8211;role</code> <code>-r</code> &lt;role&gt;</p>
<dd> Local PAN role (PANU, NAP, GN)</p>
<dt><code>&#8211;service</code> <code>-d</code> &lt;role&gt;</p>
<dd> Remote PAN service (PANU, NAP, GN)</p>
<dt><code>&#8211;ethernet</code> <code>-e</code> &lt;name&gt;</p>
<dd> Network interface name</p>
<dt><code>&#8211;device</code> <code>-i</code> &lt;bdaddr&gt;</p>
<dd> Source bdaddr</p>
<dt><code>&#8211;nosdp</code> <code>-D</code></p>
<dd> Disable SDP</p>
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
<dt><code>&#8211;cache</code> <code>-C[valid]</code></p>
<dd> Cache addresses</p>
<dt><code>&#8211;pidfile</code> <code>-P &lt;pidfile&gt;</code></p>
<dd> Create PID file</p>
<dt><code>&#8211;devup</code> <code>-u &lt;script&gt;</code></p>
<dd> Script to run when interface comes up</p>
<dt><code>&#8211;devdown</code> <code>-o &lt;script&gt;</code></p>
<dd> Script to run when interface comes down</p>
<dt><code>&#8211;autozap</code> <code>-z</code></p>
<dd> Disconnect automatically on exit </p>
</dl>
<h2>SCRIPTS</h2>
<p> The devup/devdown script will be called with bluetooth device as first argument and bluetooth destination address as second argument. </p>
<h2>Index</h2>
