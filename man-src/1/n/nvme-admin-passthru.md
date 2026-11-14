---
title: "nvme-admin-passthru(1)"
name: "nvme-admin-passthru"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-admin-passthru/"
---

<h2 class="name">NAME</h2>
 

 nvme-admin-passthru - Submit an arbitrary admin command, return results 

<h2>SYNOPSIS</h2>

 

 <pre><code>
nvme - admin - passthru&lt;device&gt;[--opcode = &lt;opcode&gt; | -o&lt;opcode&gt;][--flags = &lt;flags&gt; | -f&lt;flags&gt;][-rsvd = &lt;rsvd&gt; | -R&lt;rsvd&gt;][--namespace - id = &lt;nsid&gt;][--cdw2 = &lt;cdw2&gt;][--cdw3 = &lt;cdw3&gt;][--cdw10 = &lt;cdw10&gt;][--cdw11 = &lt;cdw11&gt;][--cdw12 = &lt;cdw12&gt;][--cdw13 = &lt;cdw13&gt;][--cdw14 = &lt;cdw14&gt;][--cdw15 = &lt;cdw15&gt;][--data - len = &lt;data - len&gt; | -l&lt;data - len&gt;][--metadata - len = &lt;len&gt; | -m&lt;len&gt;][--input - file = &lt;file&gt; | -f&lt;file&gt;][--read | -r][--write | -w][--timeout = &lt;to&gt; | -t&lt;to&gt;][--show - command | --dry - run | -s][--raw - binary | -b][--prefill = &lt;prefill&gt; | -p&lt;prefill&gt;]
</code></pre>

<h2>DESCRIPTION</h2>

 

 Submits an arbitrary NVMe admin command and returns the applicable results. This may be the simply the commands result and status, or may also include a buffer if the command returns one. This command does no interpretation of the opcodes or options. 

 The &lt;device&gt; parameter is mandatory and may be either the NVMe character device (ex: /dev/nvme0), or a namespace block device (ex: /dev/nvme0n1). 

 On success, the returned structure (if applicable) may be returned in one of several ways depending on the option flags; the structure may printed by the program as a hex dump, or may be returned as a raw buffer printed to stdout for another program to parse.

<h2>OPTIONS</h2>

 

 -o &lt;opcode&gt;, --opcode=&lt;opcode&gt;
<dl>
<dt>
<dd> The NVMe opcode to send to the device in the command</dl>
 

 -f &lt;flags&gt;, --flags=&lt;flags&gt;
<dl>
<dt>
<dd> The NVMe command flags to send to the device in the command</dl>
 

 -R &lt;rsvd&gt;, --rsvd=&lt;rsvd&gt;
<dl>
<dt>
<dd> The value for the reserved field in the command.</dl>
 

 -n &lt;nsid&gt;, --namespace-id=&lt;nsid&gt;
<dl>
<dt>
<dd> The value for the ns-id in the command.</dl>
 

 --cdw[2-3,10-15]=&lt;cdw&gt;
<dl>
<dt>
<dd> Specifies the command dword value for that specified entry in the command</dl>
 

 -r, --read, -w, --write
<dl>
<dt>
<dd> Used for the data-direction for the command and required for commands sending/receiving data. Don't use both read and write at the same time.</dl>
 

 -i &lt;file&gt;, --input-file=&lt;file&gt;
<dl>
<dt>
<dd> If the command is a data-out (write) command, use this file to fill the buffer sent to the device. If no file is given, assumed to use STDIN.</dl>
 

 -l &lt;data-len&gt;, --data-len=&lt;data-len&gt;
<dl>
<dt>
<dd> The data length for the buffer used for this command.</dl>
 

 -m &lt;data-len&gt;, --metadata-len=&lt;data-len&gt;
<dl>
<dt>
<dd> The metadata length for the buffer used for this command.</dl>
 

 -s, --show-cmd, --dry-run
<dl>
<dt>
<dd> Do not actually send the command; print out the command that would be sent.</dl>
 

 -b, --raw-binary
<dl>
<dt>
<dd> Print the raw returned buffer to stdout if the command returns a structure.</dl>
 

 -p, --prefill
<dl>
<dt>
<dd> Prefill the buffer with a predetermined byte value. Defaults to 0. This may be useful if the data you are writing is shorter than the required buffer, and you need to pad it with a known value. It may also be useful if you need to confirm if a device is overwriting a buffer for a data-in command.</dl>

<h2>EXAMPLES</h2>

 

<dl>
<dt>
<dd> &bull; The following will run the admin command with opcode=6 and cdw10=1, which corresponds to an identify controller command. This example requires the data-len param be 4096, which is the size of the returned structure. The -r option is used because it is a data-in command 

<dl>
<dt>
<dd> <pre>
# nvme admin-passthru /dev/nvme0 --opcode=06 --data-len=4096 --cdw10=1 -r
</pre></dl>
</dl>
 

<dl>
<dt>
<dd> &bull; Or if you want to save that structure to a file: 

<dl>
<dt>
<dd> <pre>
# nvme admin-passthru /dev/nvme0 --opcode=06 --data-len=4096 --cdw10=1 -r -b &gt; id_ns.raw
</pre></dl>
</dl>

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


