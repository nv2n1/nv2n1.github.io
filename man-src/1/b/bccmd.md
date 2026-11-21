---

title: "bccmd(1)"
name: "bccmd"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bccmd/"
description: "bccmd – Utility for the CSR BCCMD interface"
---

<p> <code>bccmd</code><br />
 <code>bccmd [-t &lt;transport&gt;] [-d &lt;device&gt;] &lt;command&gt; [&lt;args&gt;]</code><br />
 <code>bccmd [-h &#8211;help]</code> </p>
<p> <code>bccmd</code> issues BlueCore commands to <code>Cambridge Silicon Radio</code> devices. If run without the &lt;command&gt; argument, a short help page will be displayed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t&nbsp;&lt;transport&gt;</code></dt>
<dd> Specify the communication transport. Valid options are:</dd>
<dl>
<dl>
<dt><code>HCI</code></dt>
<dd> Local device with Host Controller Interface (default).</dd>
<dt><code>USB</code></dt>
<dd> Direct USB connection.</dd>
<dt><code>BCSP</code></dt>
<dd> Blue Core Serial Protocol.</dd>
<dt><code>H4</code></dt>
<dd> H4 serial protocol.</dd>
<dt><code>3WIRE</code></dt>
<dd> 3WIRE protocol (not implemented).</dd></dl>
</dl>
</dl>
<h2>
<dt><code>-d&nbsp;&lt;dev&gt;</code></dt>
<dd></h2>
<p> Specify a particular device to operate on. If not specified, default is the first available HCI device or /dev/ttyS0 for serial transports.</dd></dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>builddef</code></dt>
<dd> Get build definitions</dd>
<dt><code>keylen&nbsp;&lt;handle&gt;</code></dt>
<dd> Get current crypt key length</dd>
<dt><code>clock</code></dt>
<dd> Get local Bluetooth clock</dd>
<dt><code>rand</code></dt>
<dd> Get random number</dd>
<dt><code>chiprev</code></dt>
<dd> Get chip revision</dd>
<dt><code>buildname</code></dt>
<dd> Get the full build name</dd>
<dt><code>panicarg</code></dt>
<dd> Get panic code argument</dd>
<dt><code>faultarg</code></dt>
<dd> Get fault code argument</dd>
<dt><code>coldreset</code></dt>
<dd> Perform cold reset</dd>
<dt><code>warmreset</code></dt>
<dd> Perform warm reset</dd>
<dt><code>disabletx</code></dt>
<dd> Disable TX on the device</dd>
<dt><code>enabletx</code></dt>
<dd> Enable TX on the device</dd>
<dt><code>singlechan&nbsp;&lt;channel&gt;</code></dt>
<dd> Lock radio on specific channel</dd>
<dt><code>hoppingon</code></dt>
<dd> Revert to channel hopping</dd>
<dt><code>rttxdata1&nbsp;&lt;decimal freq MHz&gt;&nbsp;&lt;level&gt;</code></dt>
<dd> TXData1 radio test</dd>
<dt><code>radiotest&nbsp;&lt;decimal freq MHz&gt;&nbsp;&lt;level&gt;&nbsp;&lt;id&gt;</code></dt>
<dd> Run radio tests, tests 4, 6 and 7 are transmit tests</dd>
<dt><code>memtypes</code></dt>
<dd> Get memory types</dd>
<dt><code>psget&nbsp;[-r]&nbsp;[-s&nbsp;&lt;stores&gt;]&nbsp;&lt;key&gt;</code></dt>
<dd> Get value for PS key. -r sends a warm reset afterwards</dd>
<dt><code>psset&nbsp;[-r]&nbsp;[-s&nbsp;&lt;stores&gt;]&nbsp;&lt;key&gt;&nbsp;&lt;value&gt;</code></dt>
<dd> Set value for PS key. -r sends a warm reset afterwards</dd>
<dt><code>psclr&nbsp;[-r]&nbsp;[-s&nbsp;&lt;stores&gt;]&nbsp;&lt;key&gt;</code></dt>
<dd> Clear value for PS key. -r sends a warm reset afterwards</dd>
<dt><code>pslist&nbsp;[-r]&nbsp;[-s&nbsp;&lt;stores&gt;]</code></dt>
<dd> List all PS keys. -r sends a warm reset afterwards</dd>
<dt><code>psread&nbsp;[-r]&nbsp;[-s&nbsp;&lt;stores&gt;]</code></dt>
<dd> Read all PS keys. -r sends a warm reset afterwards</dd>
<dt><code>psload&nbsp;[-r]&nbsp;[-s&nbsp;&lt;stores&gt;]&nbsp;&lt;file&gt;</code></dt>
<dd> Load all PS keys from PSR file. -r sends a warm reset afterwards</dd>
<dt><code>pscheck&nbsp;[-r]&nbsp;[-s&nbsp;&lt;stores&gt;]&nbsp;&lt;file&gt;</code></dt>
<dd> Check syntax of PSR file. -r sends a warm reset afterwards</dd></dl>
<h2>KEYS</h2>
<p> bdaddr country devclass keymin keymax features commands version remver hciextn mapsco baudrate hostintf anafreq anaftrim usbvid usbpid dfupid bootmode</p>
<h2>AUTHORS</h2>
<p> Written by Marcel Holtmann &lt;marcel [at] holtmann.org&gt;, man page by Adam Laurie &lt;adam [at] algroup.co.uk&gt; </p>
