---
title: "biosdevname(1)"
name: "biosdevname"
section: "1"
letter: "b"
url: "/docs/linux/man/1-biosdevname/"
description: "biosdevname – give BIOS-given name of a device"
---

<h2 class="name">NAME</h2>
<p> biosdevname &#8211; give BIOS-given name of a device </p>
<h2>SYNOPSIS</h2>
<p> <code>biosdevname</code> [options]&nbsp;<wbr>[args]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> biosdevname takes a kernel device name as an argument, and returns the BIOS-given name it &quot;should&quot; be.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i, &#8211;interface</code></p>
<dd> Treat [args] as ethernet devs</p>
<dt><code>-d, &#8211;debug</code></p>
<dd> Enable debugging</p>
<dt><code>-p, &#8211;policy </code><i>[physical|all_ethN]</i></p>
<dd>
<dt><code>-P, &#8211;prefix </code><i>[string]</i></p>
<dd> string use for embedded NICs in the physical policy (default=em)</p>
<dt><code>-x, &#8211;nopirq</code></p>
<dd> Do not use $PIR table for mapping PCI device to slot. Some BIOS have incorrect values.</p>
<dt><code>-s, &#8211;smbios </code><i>[x.y]</i></p>
<dd> Require minimum SMBIOS version x.y</dl>
<h2>POLICIES</h2>
<p> The <code>physical</code> policy is the current default. However, when invoking biosdevname in udev rules, one should always specify the policy you want, as the default has changed over time.<br />
 The <code>physical</code> policy uses the following scheme:</p>
<dl>
<dt>em&lt;port&gt;[_&lt;virtual instance&gt;]</p>
<dd> for embedded NICs</p>
<dt>p&lt;slot&gt;p&lt;port&gt;[_&lt;virtual instance&gt;]</p>
<dd> for cards in PCI slots </p>
<dt>The</p>
<dd> <code>all_ethN</code> policy makes a best guess at what the device order should be, with embedded devices first, PCI cards in ascending slot order, and ports in ascending PCI bus/device/function order breadth-first. However, this policy <i>does not work</i> if your PCI devices are hot-plugged or hot-pluggable, including the virtual functions on an SR-IOV device. In a hot-plug scenario, each separate udev instance will be invoked in parallel, while the device tree is still being populated with new devices. Each udev instance will see a different PCI tree, and thus cannot provide consistent enumeration. Use of this policy should be limited to only scenarios where all PCI devices are present at boot (cold-plug). </p>
</dl>
<h2>EXIT CODES</h2>
<p> Returns 0 on success, with BIOS-suggested name printed to stdout.<br />
 Returns 1 on provided device name lookup failure.<br />
 Returns 2 if system BIOS does not provide naming information. biosdevname requires system BIOS to provide naming information, either via SMBIOS or sysfs files.<br />
 Returns 3 if not run as root but requires root privileges.<br />
 Returns 4 if running in a virtual machine. </p>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://linux.dell.com/wiki/index.php/Oss/libnetdevname">http://linux.dell.com/wiki/index.php/Oss/libnetdevname</a><br />
 <a rel="nofollow" href="http://linux.dell.com/files/biosdevname/">http://linux.dell.com/files/biosdevname/</a><br />
 <a href="git://linux.dell.com/biosdevname.git">git://linux.dell.com/biosdevname.git</a> </p>
<h2>RELATED PROGRAMS</h2>
<p> The <code>dmidecode</code> package contains two tools useful for debugging BIOS features that biosdevname uses, specifically <code>dmidecode</code> to read the SMBIOS Type 9 and Type 41 tables, and <code>biosdecode</code> to read the PCI IRQ Routing Table. Please include the output of each of these programs in any bug reports.</p>
<h2>AUTHOR</h2>
<p> biosdevname was written by Matt Domsch &lt;Matt_Domsch [at] dell.com&gt; </p>
<p> This manual page was written by Rudy Gevaert &lt;Rudy.Gevaert [at] UGent.be&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
