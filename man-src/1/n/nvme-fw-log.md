---
title: "nvme-fw-log(1)"
name: "nvme-fw-log"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-fw-log/"
---

<h2 class="name">NAME</h2>
 

 nvme-fw-log - Send NVMe Firmware log page request, returns result and log 

<h2>SYNOPSIS</h2>

 

 <pre>
<i>nvme fw-log</i> &lt;device&gt; [--raw-binary | -b]
</pre>

<h2>DESCRIPTION</h2>

 

 Retrieves the NVMe Firmware log page from an NVMe device and provides the retuned structure. 

 The &lt;device&gt; parameter is mandatory and may be either the NVMe character device (ex: /dev/nvme0), or a namespace block device (ex: /dev/nvme0n1). 

 On success, the returned f/w log structure may be returned in one of several ways depending on the option flags; the structure may parsed by the program and printed in a readable format or the raw buffer may be printed to stdout for another program to parse.

<h2>OPTIONS</h2>

 

 -b, --raw-binary
<dl>
<dt>
<dd> Print the raw fw log buffer to stdout.</dl>

<h2>EXAMPLES</h2>

 

<dl>
<dt>
<dd> &bull; Print the firmware log page in a human readable format: 

<dl>
<dt>
<dd> <pre>
# nvme fw-log /dev/nvme0
</pre></dl>
</dl>
 

<dl>
<dt>
<dd> &bull; Print the log firmware to a file: 

<dl>
<dt>
<dd> <pre>
# nvme fw-log /dev/nvme0 --raw-binary &gt; fw_log.raw
</pre></dl>
 

 It is probably a bad idea to not redirect stdout when using this mode.</dl>

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


