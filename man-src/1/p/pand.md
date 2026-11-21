---

title: "pand(1)"
name: "pand"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pand/"
description: "pand – BlueZ Bluetooth PAN daemon"
---

<p> pand &#8211; BlueZ Bluetooth PAN daemon</p>
<h2>DESCRIPTION</h2>
<p> The pand PAN daemon allows your computer to connect to ethernet networks using Bluetooth.</p>
<h2>SYNPOSIS</h2>
<p> pand &lt;options&gt;</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;show</code> <code>&#8211;list</code> <code>-l</code></dt>
<dd> Show active PAN connections</dd>
<dt><code>&#8211;listen</code> <code>-s</code></dt>
<dd> Listen for PAN connections</dd>
<dt><code>&#8211;connect</code> <code>-c</code> &lt;bdaddr&gt;</dt>
<dd> Create PAN connection</dd>
<dt><code>&#8211;search</code> <code>-Q[duration]</code></dt>
<dd> Search and connect</dd>
<dt><code>&#8211;kill</code> <code>-k</code> &lt;bdaddr&gt;</dt>
<dd> Kill PAN connection</dd>
<dt><code>&#8211;killall</code> <code>-K</code></dt>
<dd> Kill all PAN connections</dd>
<dt><code>&#8211;role</code> <code>-r</code> &lt;role&gt;</dt>
<dd> Local PAN role (PANU, NAP, GN)</dd>
<dt><code>&#8211;service</code> <code>-d</code> &lt;role&gt;</dt>
<dd> Remote PAN service (PANU, NAP, GN)</dd>
<dt><code>&#8211;ethernet</code> <code>-e</code> &lt;name&gt;</dt>
<dd> Network interface name</dd>
<dt><code>&#8211;device</code> <code>-i</code> &lt;bdaddr&gt;</dt>
<dd> Source bdaddr</dd>
<dt><code>&#8211;nosdp</code> <code>-D</code></dt>
<dd> Disable SDP</dd>
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
<dt><code>&#8211;cache</code> <code>-C[valid]</code></dt>
<dd> Cache addresses</dd>
<dt><code>&#8211;pidfile</code> <code>-P &lt;pidfile&gt;</code></dt>
<dd> Create PID file</dd>
<dt><code>&#8211;devup</code> <code>-u &lt;script&gt;</code></dt>
<dd> Script to run when interface comes up</dd>
<dt><code>&#8211;devdown</code> <code>-o &lt;script&gt;</code></dt>
<dd> Script to run when interface comes down</dd>
<dt><code>&#8211;autozap</code> <code>-z</code></dt>
<dd> Disconnect automatically on exit </dd>
</dl>
<h2>SCRIPTS</h2>
<p> The devup/devdown script will be called with bluetooth device as first argument and bluetooth destination address as second argument. </p>
