---
title: "biosdecode(8)"
name: "biosdecode"
section: "8"
letter: "b"
url: "/docs/linux/man/8-biosdecode/"
description: "biosdecode – BIOS information decoder"
---

<p>biosdecode &#8211; <font SIZE="-1">BIOS</font> information decoder</p>
<h2>Synopsis</h2>
<p><code>biosdecode</code> [<code>OPTIONS</code>]</p>
<h2>Description</h2>
<p><code>biosdecode</code> parses the <font SIZE="-1">BIOS</font> memory and prints information about all structures (or entry points) it knows of. Currently known entry point types are:</p>
<dl>
<dt>&bull;</dt>
<dd><font SIZE="-1">SMBIOS</font> (System Management <font SIZE="-1">BIOS</font>)<br />
 Use <code>dmidecode</code> for a more detailed output.</dd>
<dt>&bull;</dt>
<dd><font SIZE="-1">DMI</font> (Desktop Management Interface, a legacy version of <font SIZE="-1">SMBIOS</font>)<br />
 Use <code>dmidecode</code> for a more detailed output.</dd>
<dt>&bull;</dt>
<dd><font SIZE="-1">SYSID</font></dd>
<dt>&bull;</dt>
<dd><font SIZE="-1">PNP</font> (Plug and Play)</dd>
<dt>&bull;</dt>
<dd><font SIZE="-1">ACPI</font> (Advanced Configuration and Power Interface)</dd>
<dt>&bull;</dt>
<dd><font SIZE="-1">BIOS32</font> (<font SIZE="-1">BIOS32</font> Service Directory)</dd>
<dt>&bull;</dt>
<dd><font SIZE="-1">PIR</font> (<font SIZE="-1">PCI</font> <font SIZE="-1">IRQ</font> Routing)</dd>
<dt>&bull;</dt>
<dd><font SIZE="-1">32OS</font> (<font SIZE="-1">BIOS32</font> Extension, Compaq-specific)<br />
 See <code>ownership</code> for a Compaq ownership tag retrieval tool.</dd>
<dt>&bull;</dt>
<dd><font SIZE="-1">SNY</font> (Sony-specific, not decoded)</dd>
<dt>&bull;</dt>
<dd><font SIZE="-1">VPD</font> (Vital Product Data, IBM-specific)<br />
 Use <code>vpddecode</code> for a more detailed output.</dd>
<dt>&bull;</dt>
<dd><font SIZE="-1">FJKEYINF</font> (Application Panel, Fujitsu-specific)  <code>biosdecode</code> started its life as a part of <code>dmidecode</code> but as more entry point types were added, it was moved to a different program.</dd>
<h2>Options</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;dev-mem FILE</code></dt>
<dd>Read memory from device <code>FILE</code> (default: <code>/dev/mem</code>)</dd>
<dt> <code>&#8211;pir full</code></dt>
<dd>Decode the details of the PCI IRQ routing table</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>Display usage information and exit</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd>Display the version and exit</dd></dl>
<h2>Files</h2>
<p><i>/dev/mem</i></p>
<h2>Bugs</h2>
<p>Most of the time, <code>biosdecode</code> prints too much information (you don&#8217;t really care about addresses) or not enough (because it doesn&#8217;t follow pointers and has no lookup tables).</p>
<h2>Authors</h2>
<p>Alan Cox, Jean Delvare</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dmidecode/">dmidecode</a></code>(8), <code><a href="/docs/linux/man/4-mem/">mem</a></code>(4), <code><a href="/docs/linux/man/8-ownership/">ownership</a></code>(8), <code><a href="/docs/linux/man/8-vpddecode/">vpddecode</a></code>(8) </p>
</dl>