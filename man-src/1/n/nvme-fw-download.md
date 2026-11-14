---
title: "nvme-fw-download(1)"
name: "nvme-fw-download"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-fw-download/"
---

<h2 class="name">NAME</h2>
 

 nvme-fw-download - Download all or a portion of an nvme firmware image. 

<h2>SYNOPSIS</h2>

 

 <pre><code>
nvme fw - download&lt;device&gt;[--fw = &lt;firmware - file&gt; | -f&lt;firmware - file&gt;]
                          [--xfer = &lt;transfer - size&gt; | -x&lt;transfer - size&gt;]
                          [--offset = &lt;offset&gt; | -o&lt;offset&gt;]
</code></pre>

<h2>DESCRIPTION</h2>

 

 The Firmware Image Download command is used to download all or a portion of the firmware image for a future update to the controller. The Firmware Image Download command may be submitted while other commands on the Admin Submission Queue or I/O Submission Queues are outstanding. The Firmware Image Download command copies the new firmware image (in whole or in part) to the controller. 

 The firmware image may be constructed of multiple pieces that are individually downloaded with separate Firmware Image Download commands. Each Firmware Image Download command includes a Dword Offset and Number of Dwords that specify a Dword range. The host software shall ensure that firmware pieces do not have Dword ranges that overlap. Firmware portions may be submitted out of order to the controller. 

 The new firmware image is not applied as part of the Firmware Image Download command. It is applied following a reset, where the image to apply and the firmware slot it should be committed to is specified with the Firmware Activate command.

<h2>OPTIONS</h2>

 

 -f &lt;firmware-file&gt;, --fw=&lt;firmeware-file&gt;
<dl>
<dt>
<dd> Required argument. This specifies the path to the device's firmware file on your system that will be read by the program and sent to the device.</dl>
 

 -x &lt;transfer-size&gt;, --xfer=&lt;transfer-size&gt;
<dl>
<dt>
<dd> This specifies the size to split each transfer. This is useful if the device has a max transfer size requirement for firmware. It defaults to 4k.</dl>
 

 -o &lt;offset&gt;, --offset=&lt;offset&gt;
<dl>
<dt>
<dd> This specifies the starting offset in dwords. This is really only useful if your firmware is split in multiple files; otherwise the offset starts at zero and automatically adjusts based on the <i>xfer</i> size given.</dl>

<h2>EXAMPLES</h2>

 

<dl>
<dt>
<dd> &bull; Transfer a firmware size 128KiB at a time: 

<dl>
<dt>
<dd> <pre>
# nvme fw-download /dev/nvme0 --fw=/path/to/nvme.fw --xfer=0x20000
</pre></dl>
</dl>

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


