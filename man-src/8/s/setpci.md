---
title: "setpci(8)"
name: "setpci"
section: "8"
letter: "s"
url: "/docs/linux/man/8-setpci/"
description: "setpci – configure PCI devices"
---

<p>setpci &#8211; configure PCI devices</p>
<h2>Synopsis</h2>
<p><code>setpci</code> [<code>options</code>] <code>devices</code> <code>operations</code>&#8230; </p>
<h2>Description</h2>
<p><code>setpci</code> is a utility for querying and configuring PCI devices. All numbers are entered in hexadecimal notation. Root privileges are necessary for almost all operations, excluding reads of the standard header of the configuration space on some operating systems. Please see <code><a href="/docs/linux/man/8-lspci/">lspci</a>(8)</code> for details on access rights. </p>
<h2>Options</h2>
<h3>General options</h3>
<dl>
<dt><code>-v</code></p>
<dd>Tells <i>setpci</i> to be verbose and display detailed information about configuration space accesses.</p>
<dt><code>-f</code></p>
<dd>Tells <i>setpci</i> not to complain when there&#8217;s nothing to do (when no devices are selected). This option is intended for use in widely-distributed configuration scripts where it&#8217;s uncertain whether the device in question is present in the machine or not.</p>
<dt><code>-D</code></p>
<dd>`Demo mode&#8217; &#8212; don&#8217;t write anything to the configuration registers. It&#8217;s useful to try <code>setpci -vD</code> to verify that your complex sequence of <code>setpci</code> operations does what you think it should do.</p>
<dt><code>-r</code></p>
<dd>Avoids bus scan if each operation selects a specific device (uses the <code>-s</code> selector with specific domain, bus, slot, and function). This is faster, but if the device does not exist, it fails instead of matching an empty set of devices.</p>
<dt><code>&#8211;version</code></p>
<dd>Show <i>setpci</i> version. This option should be used stand-alone.</p>
<dt><code>&#8211;help</code></p>
<dd>Show detailed help on available options. This option should be used stand-alone.</p>
<dt><code>&#8211;dumpregs</code></p>
<dd>Show a list of all known PCI registers and capabilities. This option should be used stand-alone. </p>
</dl>
<h3>PCI access options</h3>
<p>The PCI utilities use the PCI library to talk to PCI devices (see <code><a href="/docs/linux/man/7-pcilib/">pcilib</a></code>(7) for details). You can use the following options to influence its behavior:</p>
<dl>
<dt><code>-A &lt;method&gt;</code></p>
<dd>The library supports a variety of methods to access the PCI hardware. By default, it uses the first access method available, but you can use this option to override this decision. See <code>-A help</code> for a list of available methods and their descriptions.</p>
<dt><code>-O &lt;param&gt;=&lt;value&gt;</code></p>
<dd>The behavior of the library is controlled by several named parameters. This option allows one to set the value of any of the parameters. Use <code>-O help</code> for a list of known parameters and their default values.</p>
<dt><code>-H1</code></p>
<dd>Use direct hardware access via Intel configuration mechanism 1. (This is a shorthand for <code>-A intel-conf1</code>.)</p>
<dt><code>-H2</code></p>
<dd>Use direct hardware access via Intel configuration mechanism 2. (This is a shorthand for <code>-A intel-conf2</code>.)</p>
<dt><code>-G</code></p>
<dd>Increase debug level of the library. </p>
</dl>
<h2>Device Selection</h2>
<p>Before each sequence of operations you need to select which devices you wish that operation to affect.</p>
<dl>
<dt><code>-s [[[[&lt;domain&gt;]:]&lt;bus&gt;]:][&lt;slot&gt;][.[&lt;func&gt;]]</code></p>
<dd>Consider only devices in the specified domain (in case your machine has several host bridges, they can either share a common bus number space or each of them can address a PCI domain of its own; domains are numbered from 0 to ffff), bus (0 to ff), slot (0 to 1f) and function (0 to 7). Each component of the device address can be omitted or set to &quot;*&quot;, both meaning &quot;any value&quot;. All numbers are hexadecimal. E.g., &quot;0:&quot; means all devices on bus 0, &quot;0&quot; means all functions of device 0 on any bus, &quot;0.3&quot; selects third function of device 0 on all buses and &quot;.4&quot; matches only the fourth function of each device.</p>
<dt><code>-d [&lt;vendor&gt;]:[&lt;device&gt;]</code></p>
<dd>Select devices with specified vendor and device ID. Both ID&#8217;s are given in hexadecimal and may be omitted or given as &quot;*&quot;, both meaning &quot;any value&quot;.</dl>
<p> When <code>-s</code> and <code>-d</code> are combined, only devices that match both criteria are selected. When multiple options of the same kind are specified, the rightmost one overrides the others.</p>
<h2>Operations</h2>
<p>There are two kinds of operations: reads and writes. To read a register, just specify its name. Writes have the form <i>name</i>=<i>value</i>,<i>value</i>&#8230; where each <i>value</i> is either a hexadecimal number or an expression of type <i>data</i>:<i>mask</i> where both <i>data</i> and <i>mask</i> are hexadecimal numbers. In the latter case, only the bits corresponding to binary ones in the <i>mask</i> are changed (technically, this is a read-modify-write operation). </p>
<p> There are several ways how to identity a register:</p>
<dl>
<dt>&bull;</p>
<dd>Tell its address in hexadecimal.</p>
<dt>&bull;</p>
<dd>Spell its name. Setpci knows the names of all registers in the standard configuration headers. Use `<code>setpci &#8211;dumpregs</code>&#8216; to get the complete list. See PCI bus specifications for the precise meaning of these registers or consult <code>header.h</code> or <code>/usr/include/pci/pci.h</code> for a brief sketch.</p>
<dt>&bull;</p>
<dd>If the register is a part of a PCI capability, you can specify the name of the capability to get the address of its first register. See the names starting with `CAP_&#8217; or `ECAP_&#8217; in the <code>&#8211;dumpregs</code> output.</p>
<dt>&bull;</p>
<dd>If the name of the capability is not known to <code>setpci</code>, you can refer to it by its number in the form CAP<code>id</code> or ECAP<code>id</code>, where <code>id</code> is the numeric identifier of the capability in hexadecimal.</p>
<dt>&bull;</p>
<dd>Each of the previous formats can be followed by <code>+offset</code> to add an offset (a hex number) to the address. This feature can be useful for addressing of registers living within a capability, or to modify parts of standard registers.</p>
<dt>&bull;</p>
<dd>To choose how many bytes (1, 2, or 4) should be transferred, you should append a width specifier <code>.B</code>, <code>.W</code>, or <code>.L</code>. The width can be omitted if you are referring to a register by its name and the width of the register is well known.</p>
<dt>&bull;</p>
<dd>Finally, if a capability exists multiple times you can choose which one to target using <code>@number</code>. Indexing starts at 0. </p>
</dl>
<p> All names of registers and width specifiers are case-insensitive.</p>
<h2>Examples</h2>
<dl>
<dt>COMMAND</p>
<dd>asks for the word-sized command register.</p>
<dt>4.w</p>
<dd>is a numeric address of the same register.</p>
<dt>COMMAND.l</p>
<dd>asks for a 32-bit word starting at the location of the command register, i.e., the command and status registers together.</p>
<dt>VENDOR_ID+1.b</p>
<dd>specifies the upper byte of the vendor ID register (remember, PCI is little-endian).</p>
<dt>CAP_PM+2.w</p>
<dd>corresponds to the second word of the power management capability.</p>
<dt>ECAP108.l</p>
<dd>asks for the first 32-bit word of the extended capability with ID 0x108. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lspci/">lspci</a></code>(8), <code><a href="/docs/linux/man/7-pcilib/">pcilib</a></code>(7) </p>
<h2>Author</h2>
<p>The PCI Utilities are maintained by Martin Mares &lt;mj [at] ucw.cz&gt;.</p>
