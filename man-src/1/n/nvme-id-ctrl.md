---
title: "nvme-id-ctrl(1)"
name: "nvme-id-ctrl"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-id-ctrl/"
---

<h2 class="name">NAME</h2>
 

 nvme-id-ctrl - Send NVMe Identify Controller, return result and structure 

<h2>SYNOPSIS</h2>

 

 <pre><code>
nvme id - ctrl&lt;device&gt;[-v | --vendor - specific][-b | --raw - binary]
</code></pre>

<h2>DESCRIPTION</h2>

 

 For the NVMe device given, sends an identify controller command and provides the result and returned structure. 

 The &lt;device&gt; parameter is mandatory and may be either the NVMe character device (ex: /dev/nvme0), or a namespace block device (ex: /dev/nvme0n1). 

 On success, the structure may be returned in one of several ways depending on the option flags; the structure may be parsed by the program or the raw buffer may be printed to stdout.

<h2>OPTIONS</h2>

 

 -b, --raw-binary
<dl>
<dt>
<dd> Print the raw buffer to stdout. Structure is not parsed by program. This overrides the vendor specific and human readable options.</dl>
 

 -v, --vendor-specific
<dl>
<dt>
<dd> In addition to parsing known fields, this option will dump the vendor specific region of the structure in hex with ascii interpretation.</dl>
 

 -H, --human-readable
<dl>
<dt>
<dd> This option will parse and format many of the bit fields into human-readable formats.</dl>

<h2>EXAMPLES</h2>

 

<dl>
<dt>
<dd> &bull; Has the program interpret the returned buffer and display the known fields in a human readable format: 

<dl>
<dt>
<dd> <pre>
# nvme id-ctrl /dev/nvme0
</pre></dl>
</dl>
 

<dl>
<dt>
<dd> &bull; In addition to showing the known fields, has the program to display the vendor unique field: 

<dl>
<dt>
<dd> <pre>
# nvme id-ctrl /dev/nvme0 --vendor-specific
# nvme id-ctrl /dev/nvme0 -v
</pre></dl>
 

 The above will dump the <i>vs</i> buffer in hex since it doesn't know how to interpret it.</dl>
 

<dl>
<dt>
<dd> &bull; Have the program return the raw structure in binary: 

<dl>
<dt>
<dd> <pre>
# nvme id-ctrl /dev/nvme0 --raw-binary &gt; id_ctrl.raw
# nvme id-ctrl /dev/nvme0 -b &gt; id_ctrl.raw
</pre></dl>
 

 It is probably a bad idea to not redirect stdout when using this mode.</dl>
 

<dl>
<dt>
<dd> &bull; Alternatively you may want to send the data to another program that can parse the raw buffer. 

<dl>
<dt>
<dd> <pre>
# nvme id-ctrl /dev/nvme0 --raw-binary | nvme_parse_id_ctrl
</pre></dl>
 

 The parse program in the above example can be a program that shows the structure in a way you like. The following program is such an example that will parse it and can accept the output through a pipe, '|', as shown in the above example, or you can 'cat' a saved output buffer to it.</dl>
 

<dl>
<dt>
<dd> <pre><code>
/* File: nvme_parse_id_ctrl.c */
#include &lt;linux/nvme.h&gt;
#include &lt;stdio.h&gt;
#include &lt;unistd.h&gt;
int main(int argc, char **argv)
{
    unsigned char buf[sizeof(struct nvme_id_ctrl)];
    struct nvme_id_ctrl *ctrl = (struct nvme_id_ctrl *)buf;
    if (read(STDIN_FILENO, buf, sizeof(buf)))
        return 1;
    printf("vid   : %#x\n", ctrl-&gt;vid);
    printf("ssvid : %#x\n", ctrl-&gt;ssvid);
    return 0;
}
</code></pre></dl>

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


