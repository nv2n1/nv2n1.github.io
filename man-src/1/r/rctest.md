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
<dt><code>-r</code></dt>
<dd> listen and receive</dd>
<dt><code>-w</code></dt>
<dd> listen and send</dd>
<dt><code>-d</code></dt>
<dd> listen and dump incoming data</dd>
<dt><code>-s</code></dt>
<dd> connect and send</dd>
<dt><code>-u</code></dt>
<dd> connect and receive</dd>
<dt><code>-n</code></dt>
<dd> connect and be silent</dd>
<dt><code>-c</code></dt>
<dd> connect, disconnect, connect, &#8230;</dd>
<dt><code>-m</code></dt>
<dd> multiple connects</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code><i>&nbsp;bytes</i></dt>
<dd> send/receive bytes</dd>
<dt><code>-i</code><i>&nbsp;device</i></dt>
<dd> select the specified device</dd>
<dt><code>-P</code><i>&nbsp;channel</i></dt>
<dd> select the specified channel</dd>
<dt><code>-U</code><i>&nbsp;uuid</i></dt>
<dd> select the specified uuid</dd>
<dt><code>-L</code><i>&nbsp;seconds</i></dt>
<dd> enable SO_LINGER options for seconds</dd>
<dt><code>-W</code><i>&nbsp;seconds</i></dt>
<dd> enable deferred setup for seconds</dd>
<dt><code>-B</code><i>&nbsp;filename</i></dt>
<dd> use data packets from filename</dd>
<dt><code>-N</code><i>&nbsp;num</i></dt>
<dd> send num frames</dd>
<dt><code>-C</code><i>&nbsp;num</i></dt>
<dd> send num frames before delay (default: 1)</dd>
<dt><code>-D</code><i>&nbsp;milliseconds</i></dt>
<dd> delay milliseconds after sending num frames (default: 0)</dd>
<dt><code>-A</code></dt>
<dd> request authentication</dd>
<dt><code>-E</code></dt>
<dd> request encryption</dd>
<dt><code>-S</code></dt>
<dd> secure connection</dd>
<dt><code>-M</code></dt>
<dd> become central</dd>
<dt><code>-T</code></dt>
<dd> enable timestamps</dd></dl>
<h2>RESOURCES</h2>
<p> <i><a rel="nofollow" href="http://www.bluez.org">http://www.bluez.org</a></i></p>
<h2>REPORTING BUGS</h2>
<p> <i>linux-bluetooth [at] vger.kernel.org</i></p>
<h2>AUTHOR</h2>
<p> Maxim Krasnyansky &lt;maxk [at] qualcomm.com&gt;, Marcel Holtmann &lt;marcel [at] holtmann.org&gt;, Filippo Giunchedi &lt;filippo [at] debian.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Free use of this software is granted under ther terms of the GNU Lesser General Public Licenses (LGPL). </p>
