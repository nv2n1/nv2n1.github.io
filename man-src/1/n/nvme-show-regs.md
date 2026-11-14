---
title: "nvme-show-regs(1)"
name: "nvme-show-regs"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-show-regs/"
---

<h2 class="name">NAME</h2>
 

 nvme-show-regs - Reads and shows the defined NVMe controller registers. 

<h2>SYNOPSIS</h2>

 

 <pre>
<i>nvme show-regs</i> &lt;device&gt;
</pre>

<h2>DESCRIPTION</h2>

 

 For the NVMe device given, sends an identify namespace command and provides the result and returned structure. 

 The &lt;device&gt; parameter is mandatory and must be the nvme admin character device (ex: /dev/nvme0). The program uses knowledge of the sysfs layout to map the device to the pci resource stored there and mmaps the memory to get access to the registers.

<h2>EXAMPLES</h2>

 

<dl>
<dt>
<dd> &bull; Has the program map the nvme pci controller registers and prints them in a human readable format: 

<dl>
<dt>
<dd> <pre>
# nvme show-regs /dev/nvme0
</pre></dl>
</dl>

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


