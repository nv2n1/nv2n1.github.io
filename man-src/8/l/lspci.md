---
title: "lspci(8)"
name: "lspci"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lspci/"
description: "lspci – list all PCI devices"
---

<p>lspci &#8211; list all PCI devices</p>
<h2>Synopsis</h2>
<p><code>lspci</code> [<code>options</code>]</p>
<h2>Description</h2>
<p><code>lspci</code> is a utility for displaying information about PCI buses in the system and devices connected to them. By default, it shows a brief list of devices. Use the options described below to request either a more verbose output or output intended for parsing by other programs. If you are going to report bugs in PCI device drivers or in <i>lspci</i> itself, please include output of &quot;lspci -vvx&quot; or even better &quot;lspci -vvxxx&quot; (however, see below for possible caveats). Some parts of the output, especially in the highly verbose modes, are probably intelligible only to experienced PCI hackers. For exact definitions of the fields, please consult either the PCI specifications or the <code>header.h</code> and <code>/usr/include/linux/pci.h</code> include files. Access to some parts of the PCI configuration space is restricted to root on many operating systems, so the features of <i>lspci</i> available to normal users are limited. However, <i>lspci</i> tries its best to display as much as available and mark all other information with <i>&lt;access denied&gt;</i> text. </p>
<h2>Options</h2>
<h3>Basic display modes</h3>
<dl>
<dt><code>-m</code></p>
<dd>Dump PCI device data in a backward-compatible machine readable form. See below for details.</p>
<dt><code>-mm</code></p>
<dd>Dump PCI device data in a machine readable form for easy parsing by scripts. See below for details.</p>
<dt><code>-t</code></p>
<dd>Show a tree-like diagram containing all buses, bridges, devices and connections between them. </p>
</dl>
<h3>Display options</h3>
<dl>
<dt><code>-v</code></p>
<dd>Be verbose and display detailed information about all devices.</p>
<dt><code>-vv</code></p>
<dd>Be very verbose and display more details. This level includes everything deemed useful.</p>
<dt><code>-vvv</code></p>
<dd>Be even more verbose and display everything we are able to parse, even if it doesn&#8217;t look interesting at all (e.g., undefined memory regions).</p>
<dt><code>-k</code></p>
<dd>Show kernel drivers handling each device and also kernel modules capable of handling it. Turned on by default when <code>-v</code> is given in the normal mode of output. (Currently works only on Linux with kernel 2.6 or newer.)</p>
<dt><code>-x</code></p>
<dd>Show hexadecimal dump of the standard part of the configuration space (the first 64 bytes or 128 bytes for CardBus bridges).</p>
<dt><code>-xxx</code></p>
<dd>Show hexadecimal dump of the whole PCI configuration space. It is available only to root as several PCI devices <code>crash</code> when you try to read some parts of the config space (this behavior probably doesn&#8217;t violate the PCI standard, but it&#8217;s at least very stupid). However, such devices are rare, so you needn&#8217;t worry much.</p>
<dt><code>-xxxx</code></p>
<dd>Show hexadecimal dump of the extended (4096-byte) PCI configuration space available on PCI-X 2.0 and PCI Express buses.</p>
<dt><code>-b</code></p>
<dd>Bus-centric view. Show all IRQ numbers and addresses as seen by the cards on the PCI bus instead of as seen by the kernel.</p>
<dt><code>-D</code></p>
<dd>Always show PCI domain numbers. By default, lspci suppresses them on machines which have only domain 0.</p>
<dt><code>-P</code></p>
<dd>Identify PCI devices by path through each bridge, instead of by bus number.</p>
<dt><code>-PP</code></p>
<dd>Identify PCI devices by path through each bridge, showing the bus number as well as the device number. </p>
</dl>
<h3>Options to control resolving ID&#8217;s to names</h3>
<dl>
<dt><code>-n</code></p>
<dd>Show PCI vendor and device codes as numbers instead of looking them up in the PCI ID list.</p>
<dt><code>-nn</code></p>
<dd>Show PCI vendor and device codes as both numbers and names.</p>
<dt><code>-q</code></p>
<dd>Use DNS to query the central PCI ID database if a device is not found in the local <code>pci.ids</code> file. If the DNS query succeeds, the result is cached in <code>~/.pciids-cache</code> and it is recognized in subsequent runs even if <code>-q</code> is not given any more. Please use this switch inside automated scripts only with caution to avoid overloading the database servers.</p>
<dt><code>-qq</code></p>
<dd>Same as <code>-q</code>, but the local cache is reset.</p>
<dt><code>-Q</code></p>
<dd>Query the central database even for entries which are recognized locally. Use this if you suspect that the displayed entry is wrong. </p>
</dl>
<h3>Options for selection of devices</h3>
<dl>
<dt><code>-s [[[[&lt;domain&gt;]:]&lt;bus&gt;]:][&lt;device&gt;][.[&lt;func&gt;]]</code></p>
<dd>Show only devices in the specified domain (in case your machine has several host bridges, they can either share a common bus number space or each of them can address a PCI domain of its own; domains are numbered from 0 to ffff), bus (0 to ff), device (0 to 1f) and function (0 to 7). Each component of the device address can be omitted or set to &quot;*&quot;, both meaning &quot;any value&quot;. All numbers are hexadecimal. E.g., &quot;0:&quot; means all devices on bus 0, &quot;0&quot; means all functions of device 0 on any bus, &quot;0.3&quot; selects third function of device 0 on all buses and &quot;.4&quot; shows only the fourth function of each device.</p>
<dt><code>-d [&lt;vendor&gt;]:[&lt;device&gt;][:&lt;class&gt;]</code></p>
<dd>Show only devices with specified vendor, device and class ID. The ID&#8217;s are given in hexadecimal and may be omitted or given as &quot;*&quot;, both meaning &quot;any value&quot;. </p>
</dl>
<h3>Other options</h3>
<dl>
<dt><code>-i &lt;file&gt;</code></p>
<dd>Use <code>&lt;file&gt;</code> as the PCI ID list instead of /usr/share/misc/pci.ids.</p>
<dt><code>-p &lt;file&gt;</code></p>
<dd>Use <code>&lt;file&gt;</code> as the map of PCI ID&#8217;s handled by kernel modules. By default, lspci uses /lib/modules/<i>kernel_version</i>/modules.pcimap. Applies only to Linux systems with recent enough module tools.</p>
<dt><code>-M</code></p>
<dd>Invoke bus mapping mode which performs a thorough scan of all PCI devices, including those behind misconfigured bridges, etc. This option gives meaningful results only with a direct hardware access mode, which usually requires root privileges. Please note that the bus mapper only scans PCI domain 0.</p>
<dt><code>&#8211;version</code></p>
<dd>Shows <i>lspci</i> version. This option should be used stand-alone. </p>
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
<dt><code>-F &lt;file&gt;</code></p>
<dd>Instead of accessing real hardware, read the list of devices and values of their configuration registers from the given file produced by an earlier run of lspci -x. This is very useful for analysis of user-supplied bug reports, because you can display the hardware configuration in any way you want without disturbing the user with requests for more dumps.</p>
<dt><code>-G</code></p>
<dd>Increase debug level of the library. </p>
</dl>
<h2>Machine Readable Output</h2>
<p>If you intend to process the output of lspci automatically, please use one of the machine-readable output formats (<code>-m</code>, <code>-vm</code>, <code>-vmm</code>) described in this section. All other formats are likely to change between versions of lspci. </p>
<p> All numbers are always printed in hexadecimal. If you want to process numeric ID&#8217;s instead of names, please add the <code>-n</code> switch.</p>
<h3>Simple format (-m)</h3>
<p>In the simple format, each device is described on a single line, which is formatted as parameters suitable for passing to a shell script, i.e., values separated by whitespaces, quoted and escaped if necessary. Some of the arguments are positional: slot, class, vendor name, device name, subsystem vendor name and subsystem name (the last two are empty if the device has no subsystem); the remaining arguments are option-like: </p>
<dl>
<dt><code>-r</code><i>rev</i></p>
<dd>Revision number. </p>
<dt><code>-p</code><i>progif</i></p>
<dd>Programming interface. </p>
</dl>
<p> The relative order of positional arguments and options is undefined. New options can be added in future versions, but they will always have a single argument not separated from the option by any spaces, so they can be easily ignored if not recognized.</p>
<h3>Verbose format (-vmm)</h3>
<p>The verbose output is a sequence of records separated by blank lines. Each record describes a single device by a sequence of lines, each line containing a single `<i>tag</i>: <i>value</i>&#8216; pair. The <i>tag</i> and the <i>value</i> are separated by a single tab character. Neither the records nor the lines within a record are in any particular order. Tags are case-sensitive. </p>
<p> The following tags are defined: </p>
<dl>
<dt><code>Slot</code></p>
<dd>The name of the slot where the device resides ([<i>domain</i>:]<i>bus</i>:<i>device</i>.<i>function</i>). This tag is always the first in a record. </p>
<dt><code>Class</code></p>
<dd>Name of the class. </p>
<dt><code>Vendor</code></p>
<dd>Name of the vendor. </p>
<dt><code>Device</code></p>
<dd>Name of the device. </p>
<dt><code>SVendor</code></p>
<dd>Name of the subsystem vendor (optional). </p>
<dt><code>SDevice</code></p>
<dd>Name of the subsystem (optional). </p>
<dt><code>PhySlot</code></p>
<dd>The physical slot where the device resides (optional, Linux only). </p>
<dt><code>Rev</code></p>
<dd>Revision number (optional). </p>
<dt><code>ProgIf</code></p>
<dd>Programming interface (optional). </p>
<dt><code>Driver</code></p>
<dd>Kernel driver currently handling the device (optional, Linux only). </p>
<dt><code>Module</code></p>
<dd>Kernel module reporting that it is capable of handling the device (optional, Linux only). Multiple lines with this tag can occur. </p>
<dt><code>NUMANode</code></p>
<dd>NUMA node this device is connected to (optional, Linux only). </p>
<dt><code>IOMMUGroup</code></p>
<dd>IOMMU group that this device is part of (optional, Linux only). </p>
</dl>
<p> New tags can be added in future versions, so you should silently ignore any tags you don&#8217;t recognize.</p>
<h3>Backward-compatible verbose format (-vm)</h3>
<p>In this mode, lspci tries to be perfectly compatible with its old versions. It&#8217;s almost the same as the regular verbose format, but the <code>Device</code> tag is used for both the slot and the device name, so it occurs twice in a single record. Please avoid using this format in any new code.</p>
<h2>Files</h2>
<dl>
<dt><code>/usr/share/misc/pci.ids</code></p>
<dd>A list of all known PCI ID&#8217;s (vendors, devices, classes and subclasses). Maintained at <a rel="nofollow" href="https://pci-ids.ucw.cz/,">https://pci-ids.ucw.cz/,</a> use the <code>update-pciids</code> utility to download the most recent version.</p>
<dt><code>/usr/share/misc/pci.ids.gz</code></p>
<dd>If lspci is compiled with support for compression, this file is tried before pci.ids.</p>
<dt><code>~/.pciids-cache</code></p>
<dd>All ID&#8217;s found in the DNS query mode are cached in this file. </p>
</dl>
<h2>Bugs</h2>
<p>Sometimes, lspci is not able to decode the configuration registers completely. This usually happens when not enough documentation was available to the authors. In such cases, it at least prints the <code>&lt;?&gt;</code> mark to signal that there is potentially something more to say. If you know the details, patches will be of course welcome. Access to the extended configuration space is currently supported only by the <code>linux_sysfs</code> back-end. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-setpci/">setpci</a></code>(8), <code><a href="/docs/linux/man/5-pci-ids/">pci.ids</a></code>(5), <code><a href="/docs/linux/man/8-update-pciids/">update-pciids</a></code>(8), <code><a href="/docs/linux/man/7-pcilib/">pcilib</a></code>(7) </p>
<h2>Author</h2>
<p>The PCI Utilities are maintained by Martin Mares &lt;mj [at] ucw.cz&gt;.</p>
