---
title: "bccmd(1)"
name: "bccmd"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bccmd/"
description: "bccmd – Utility for the CSR BCCMD interface"
---

<h2 class="name">NAME</h2>
<p> bccmd &#8211; Utility for the CSR BCCMD interface </p>
<h2>SYNOPSIS</h2>
<p> <code>bccmd</code><br />
 <code>bccmd [-t &lt;transport&gt;] [-d &lt;device&gt;] &lt;command&gt; [&lt;args&gt;]</code><br />
 <code>bccmd [-h &#8211;help]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>bccmd</code> issues BlueCore commands to <code>Cambridge Silicon Radio</code> devices. If run without the &lt;command&gt; argument, a short help page will be displayed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t&nbsp;&lt;transport&gt;</code></p>
<dd> Specify the communication transport. Valid options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>HCI</code></p>
<dd> Local device with Host Controller Interface (default).</p>
<dt><code>USB</code></p>
<dd> Direct USB connection.</p>
<dt><code>BCSP</code></p>
<dd> Blue Core Serial Protocol.</p>
<dt><code>H4</code></p>
<dd> H4 serial protocol.</p>
<dt><code>3WIRE</code></p>
<dd> 3WIRE protocol (not implemented).</dl>
</dl>
</dl>
<h2>
<dt><code>-d&nbsp;&lt;dev&gt;</code></p>
<dd></h2>
<p> Specify a particular device to operate on. If not specified, default is the first available HCI device or /dev/ttyS0 for serial transports.</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>builddef</code></p>
<dd> Get build definitions</p>
<dt><code>keylen&nbsp;&lt;handle&gt;</code></p>
<dd> Get current crypt key length</p>
<dt><code>clock</code></p>
<dd> Get local Bluetooth clock</p>
<dt><code>rand</code></p>
<dd> Get random number</p>
<dt><code>chiprev</code></p>
<dd> Get chip revision</p>
<dt><code>buildname</code></p>
<dd> Get the full build name</p>
<dt><code>panicarg</code></p>
<dd> Get panic code argument</p>
<dt><code>faultarg</code></p>
<dd> Get fault code argument</p>
<dt><code>coldreset</code></p>
<dd> Perform cold reset</p>
<dt><code>warmreset</code></p>
<dd> Perform warm reset</p>
<dt><code>disabletx</code></p>
<dd> Disable TX on the device</p>
<dt><code>enabletx</code></p>
<dd> Enable TX on the device</p>
<dt><code>singlechan&nbsp;&lt;channel&gt;</code></p>
<dd> Lock radio on specific channel</p>
<dt><code>hoppingon</code></p>
<dd> Revert to channel hopping</p>
<dt><code>rttxdata1&nbsp;&lt;decimal freq MHz&gt;&nbsp;&lt;level&gt;</code></p>
<dd> TXData1 radio test</p>
<dt><code>radiotest&nbsp;&lt;decimal freq MHz&gt;&nbsp;&lt;level&gt;&nbsp;&lt;id&gt;</code></p>
<dd> Run radio tests, tests 4, 6 and 7 are transmit tests</p>
<dt><code>memtypes</code></p>
<dd> Get memory types</p>
<dt><code>psget&nbsp;[-r]&nbsp;[-s&nbsp;&lt;stores&gt;]&nbsp;&lt;key&gt;</code></p>
<dd> Get value for PS key. -r sends a warm reset afterwards</p>
<dt><code>psset&nbsp;[-r]&nbsp;[-s&nbsp;&lt;stores&gt;]&nbsp;&lt;key&gt;&nbsp;&lt;value&gt;</code></p>
<dd> Set value for PS key. -r sends a warm reset afterwards</p>
<dt><code>psclr&nbsp;[-r]&nbsp;[-s&nbsp;&lt;stores&gt;]&nbsp;&lt;key&gt;</code></p>
<dd> Clear value for PS key. -r sends a warm reset afterwards</p>
<dt><code>pslist&nbsp;[-r]&nbsp;[-s&nbsp;&lt;stores&gt;]</code></p>
<dd> List all PS keys. -r sends a warm reset afterwards</p>
<dt><code>psread&nbsp;[-r]&nbsp;[-s&nbsp;&lt;stores&gt;]</code></p>
<dd> Read all PS keys. -r sends a warm reset afterwards</p>
<dt><code>psload&nbsp;[-r]&nbsp;[-s&nbsp;&lt;stores&gt;]&nbsp;&lt;file&gt;</code></p>
<dd> Load all PS keys from PSR file. -r sends a warm reset afterwards</p>
<dt><code>pscheck&nbsp;[-r]&nbsp;[-s&nbsp;&lt;stores&gt;]&nbsp;&lt;file&gt;</code></p>
<dd> Check syntax of PSR file. -r sends a warm reset afterwards</dl>
<h2>KEYS</h2>
<p> bdaddr country devclass keymin keymax features commands version remver hciextn mapsco baudrate hostintf anafreq anaftrim usbvid usbpid dfupid bootmode</p>
<h2>AUTHORS</h2>
<p> Written by Marcel Holtmann &lt;marcel [at] holtmann.org&gt;, man page by Adam Laurie &lt;adam [at] algroup.co.uk&gt; </p>
<h2>Index</h2>
