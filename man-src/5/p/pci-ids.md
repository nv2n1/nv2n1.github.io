---
title: "pci-ids(5)"
name: "pci-ids"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pci-ids/"
description: "pci.ids – list of known identifiers related to PCI devices"
---

<p>pci.ids &#8211; list of known identifiers related to PCI devices</p>
<h2>Introduction</h2>
<p>Devices on the PCI bus are identified by a combination of a vendor ID (assigned by the PCI SIG) and device ID (assigned by the vendor). Both IDs are 16-bit integers and the device itself provides no translation to a human-readable string. </p>
<p> In addition to the vendor and device, devices also report several other identifiers: </p>
<dl>
<dt>&bull;</p>
<dd>Device class and subclass (two 8-bit numbers) </p>
<dt>&bull;</p>
<dd>Programming interface (8-bit number, meaning specific for the subclass) </p>
<dt>&bull;</p>
<dd>Subsystem, which identifies the assembly in which the device is contained. A typical example is an Ethernet add-in card: the device is the Ethernet controller chip, while the card plays the role of the subsystem. Subsystems have their vendor ID (from the same namespace as device vendors) and subsystem ID. Generally, the meaning of the subsystem ID depends on the device, but there are cases in which a single subsystem ID is used for many devices &#8211; e.g., laptop motherboards. </p>
<p> The PCI utilities use the <code>pci.ids</code> file to translate all these numeric IDs to strings. </p>
</dl>
<h2>Keeping The List Up-To-Date</h2>
<p>The <code>pci.ids</code> file is generated from the PCI ID database, which is maintained at If you find any IDs missing from the list, please contribute them to the database. </p>
<p> You can use the <code>update-pciids</code> command to download the current version of the list. </p>
<p> Alternatively, you can use <code>lspci -q</code> to query the database online.</p>
<h2>File Format</h2>
<p>The pci.ids file is a text file in plain ASCII, interpreted line by line. Lines starting with the hash sign are treated as comments are ignored. Comments regarding a specific entry are written immediately before the entry. </p>
<p> Vendor entries start with a 4-digit hexadecimal vendor ID, followed by one or more spaces, and the name of the vendor extending to the end of the line. </p>
<p> Device entries are placed below the vendor entry. Each device entry consists of a single TAB character, a 4-digit hexadecimal device ID, followed by one or more spaces, and the name of the device extending to the end of the line. </p>
<p> Subsystem entries are placed below the device entry. They start with two TAB characters, a 4-digit hexadecimal vendor ID (which must be defined elsewhere in the list), a single space, a 4-digit hexadecimal subsystem ID, one or more spaces, and the name of the subsystem extending to the end of the line. </p>
<p> Class entries consist of &quot;C&quot;, one space, 2-digit hexadecimal class ID, one or more spaces, and the name of the class. Subclasses are placed below the corresponding class, indented by a single TAB, followed by a 2-digit hexadecimal subclass ID, one or more spaces, and the name of the subclass. Programming interfaces are below the subclass, indented by two TABs, followed by a 2-digit hexadecimal prog-if ID, one or more spaces, and the name. </p>
<p> There can be device-independent subsystem IDs, although the web interface of the database does not support them yet. They start with a subsystem vendor line consisting of &quot;S&quot;, one space, and a 4-digit hexadecimal vendor ID (which must correspond to an already listed vendor). Subsystems follow on subsequent lines, each indented by one TAB, followed by a 4-digit hexadecimal subsystem ID, one or more spaces, and the name of the subsystem. </p>
<p> To ensure extensibility of the format, lines starting with an unrecognized letter followed by a single space are ignored and so are all following TAB-indented lines.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lspci/">lspci</a></code>(8), <code><a href="/docs/linux/man/8-update-pciids/">update-pciids</a></code>(8), <code><a href="/docs/linux/man/7-pcilib/">pcilib</a></code>(7) </p>
<h2>Author</h2>
<p>The PCI Utilities are maintained by Martin Mares &lt;mj [at] ucw.cz&gt;.</p>
