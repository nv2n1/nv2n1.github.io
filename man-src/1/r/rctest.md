---
title: "rctest(1)"
name: "rctest"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rctest/"
description: "rctest – RFCOMM testing"
---

<h2 class="name">NAME</h2>
<p> rctest &#8211; RFCOMM testing </p>
<h2>SYNOPSIS</h2>
<p> <code>rctest</code> &lt;<i>MODE</i>&gt; [<i>OPTIONS</i>] [<i>bdaddr</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-rctest/">rctest</a>(1)</code> is used to test RFCOMM communications on the BlueZ stack</p>
<h2>MODES</h2>
<dl>
<dt><code>-r</code></p>
<dd> listen and receive</p>
<dt><code>-w</code></p>
<dd> listen and send</p>
<dt><code>-d</code></p>
<dd> listen and dump incoming data</p>
<dt><code>-s</code></p>
<dd> connect and send</p>
<dt><code>-u</code></p>
<dd> connect and receive</p>
<dt><code>-n</code></p>
<dd> connect and be silent</p>
<dt><code>-c</code></p>
<dd> connect, disconnect, connect, &#8230;</p>
<dt><code>-m</code></p>
<dd> multiple connects</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code><i>&nbsp;bytes</i></p>
<dd> send/receive bytes</p>
<dt><code>-i</code><i>&nbsp;device</i></p>
<dd> select the specified device</p>
<dt><code>-P</code><i>&nbsp;channel</i></p>
<dd> select the specified channel</p>
<dt><code>-U</code><i>&nbsp;uuid</i></p>
<dd> select the specified uuid</p>
<dt><code>-L</code><i>&nbsp;seconds</i></p>
<dd> enable SO_LINGER options for seconds</p>
<dt><code>-W</code><i>&nbsp;seconds</i></p>
<dd> enable deferred setup for seconds</p>
<dt><code>-B</code><i>&nbsp;filename</i></p>
<dd> use data packets from filename</p>
<dt><code>-N</code><i>&nbsp;num</i></p>
<dd> send num frames</p>
<dt><code>-C</code><i>&nbsp;num</i></p>
<dd> send num frames before delay (default: 1)</p>
<dt><code>-D</code><i>&nbsp;milliseconds</i></p>
<dd> delay milliseconds after sending num frames (default: 0)</p>
<dt><code>-A</code></p>
<dd> request authentication</p>
<dt><code>-E</code></p>
<dd> request encryption</p>
<dt><code>-S</code></p>
<dd> secure connection</p>
<dt><code>-M</code></p>
<dd> become central</p>
<dt><code>-T</code></p>
<dd> enable timestamps</dl>
<h2>RESOURCES</h2>
<p> <i><a rel="nofollow" href="http://www.bluez.org">http://www.bluez.org</a></i></p>
<h2>REPORTING BUGS</h2>
<p> <i>linux-bluetooth [at] vger.kernel.org</i></p>
<h2>AUTHOR</h2>
<p> Maxim Krasnyansky &lt;maxk [at] qualcomm.com&gt;, Marcel Holtmann &lt;marcel [at] holtmann.org&gt;, Filippo Giunchedi &lt;filippo [at] debian.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Free use of this software is granted under ther terms of the GNU Lesser General Public Licenses (LGPL). </p>
<h2>Index</h2>
