---
title: "bccmd(8)"
name: "bccmd"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bccmd/"
description: "bccmd – Utility for the CSR BCCMD interface"
---

<p>bccmd &#8211; Utility for the CSR BCCMD interface</p>
<h2>Synopsis</h2>
<p><code>bccmd</code><br />
 <code>bccmd [-t &lt;transport&gt;] [-d &lt;device&gt;] &lt;command&gt; [&lt;args&gt;]</code><br />
 <code>bccmd [-h &#8211;help]</code></p>
<h2>Description</h2>
<p><code>bccmd</code> issues BlueCore commands to <code>Cambridge Silicon Radio</code> devices. If run without the &lt;command&gt; argument, a short help page will be displayed.</p>
<h2>Options</h2>
<dl>
<dt><code>-t&nbsp;<wbr>&lt;transport&gt;</code></p>
<dd>Specify the communication transport. Valid options are:</p>
<dl>
<dd>
<dl>
<dt><code>HCI</code></p>
<dd>Local device with Host Controller Interface (default).</p>
<dt><code>USB</code></p>
<dd>Direct USB connection.</p>
<dt><code>BCSP</code></p>
<dd>Blue Core Serial Protocol.</p>
<dt><code>H4</code></p>
<dd>H4 serial protocol.</p>
<dt><code>3WIRE</code></p>
<dd>3WIRE protocol (not implemented).</dl>
</dl>
</dl>
<h2>
<dt><code>-d&nbsp;<wbr>&lt;dev&gt;</code></p>
<dd></h2>
<p>Specify a particular device to operate on. If not specified, default is the first available HCI device or /dev/ttyS0 for serial transports.</dl>
<h2>Commands</h2>
<dl>
<dt><code>builddef</code></p>
<dd>Get build definitions</p>
<dt><code>keylen&nbsp;<wbr>&lt;handle&gt;</code></p>
<dd>Get current crypt key length</p>
<dt><code>clock</code></p>
<dd>Get local Bluetooth clock</p>
<dt><code>rand</code></p>
<dd>Get random number</p>
<dt><code>chiprev</code></p>
<dd>Get chip revision</p>
<dt><code>buildname</code></p>
<dd>Get the full build name</p>
<dt><code>panicarg</code></p>
<dd>Get panic code argument</p>
<dt><code>faultarg</code></p>
<dd>Get fault code argument</p>
<dt><code>coldreset</code></p>
<dd>Perform cold reset</p>
<dt><code>warmreset</code></p>
<dd>Perform warm reset</p>
<dt><code>disabletx</code></p>
<dd>Disable TX on the device</p>
<dt><code>enabletx</code></p>
<dd>Enable TX on the device</p>
<dt><code>singlechan&nbsp;<wbr>&lt;channel&gt;</code></p>
<dd>Lock radio on specific channel</p>
<dt><code>hoppingon</code></p>
<dd>Revert to channel hopping</p>
<dt><code>rttxdata1&nbsp;<wbr>&lt;decimal freq MHz&gt;&nbsp;<wbr>&lt;level&gt;</code></p>
<dd>TXData1 radio test</p>
<dt><code>radiotest&nbsp;<wbr>&lt;decimal freq MHz&gt;&nbsp;<wbr>&lt;level&gt;&nbsp;<wbr>&lt;id&gt;</code></p>
<dd>Run radio tests, tests 4, 6 and 7 are transmit tests</p>
<dt><code>memtypes</code></p>
<dd>Get memory types</p>
<dt><code>psget&nbsp;<wbr>[-r]&nbsp;<wbr>[-s&nbsp;<wbr>&lt;stores&gt;]&nbsp;<wbr>&lt;key&gt;</code></p>
<dd>Get value for PS key. -r sends a warm reset afterwards</p>
<dt><code>psset&nbsp;<wbr>[-r]&nbsp;<wbr>[-s&nbsp;<wbr>&lt;stores&gt;]&nbsp;<wbr>&lt;key&gt;&nbsp;<wbr>&lt;value&gt;</code></p>
<dd>Set value for PS key. -r sends a warm reset afterwards</p>
<dt><code>psclr&nbsp;<wbr>[-r]&nbsp;<wbr>[-s&nbsp;<wbr>&lt;stores&gt;]&nbsp;<wbr>&lt;key&gt;</code></p>
<dd>Clear value for PS key. -r sends a warm reset afterwards</p>
<dt><code>pslist&nbsp;<wbr>[-r]&nbsp;<wbr>[-s&nbsp;<wbr>&lt;stores&gt;]</code></p>
<dd>List all PS keys. -r sends a warm reset afterwards</p>
<dt><code>psread&nbsp;<wbr>[-r]&nbsp;<wbr>[-s&nbsp;<wbr>&lt;stores&gt;]</code></p>
<dd>Read all PS keys. -r sends a warm reset afterwards</p>
<dt><code>psload&nbsp;<wbr>[-r]&nbsp;<wbr>[-s&nbsp;<wbr>&lt;stores&gt;]&nbsp;<wbr>&lt;file&gt;</code></p>
<dd>Load all PS keys from PSR file. -r sends a warm reset afterwards</p>
<dt><code>pscheck&nbsp;<wbr>[-r]&nbsp;<wbr>[-s&nbsp;<wbr>&lt;stores&gt;]&nbsp;<wbr>&lt;file&gt;</code></p>
<dd>Check syntax of PSR file. -r sends a warm reset afterwards</dl>
<h2>Keys</h2>
<p>bdaddr country devclass keymin keymax features commands version remver hciextn mapsco baudrate hostintf anafreq anaftrim usbvid usbpid dfupid bootmode</p>
<h2>Authors</h2>
<p>Written by Marcel Holtmann &lt;marcel [at] holtmann.org&gt;, man page by Adam Laurie &lt;adam [at] algroup.co.uk&gt;</p>
