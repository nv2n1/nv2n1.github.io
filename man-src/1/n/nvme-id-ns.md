---
title: "nvme-id-ns(1)"
name: "nvme-id-ns"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-id-ns/"
---

<h2 class="name">NAME</h2>
 

 nvme-id-ns - Send NVMe Identify Namespace, return result and structure 

<h2>SYNOPSIS</h2>

 

 <pre><code>
nvme id - ns&lt;device&gt;[-v | --vendor - specific][-b | --raw - binary]
                    [--namespace - id = &lt;nsid&gt; | -n&lt;nsid&gt;][-f | --force]
</code></pre>

<h2>DESCRIPTION</h2>

 

 For the NVMe device given, sends an identify namespace command and provides the result and returned structure. 

 The &lt;device&gt; parameter is mandatory and may be either the NVMe character device (ex: /dev/nvme0), or a namespace block device (ex: /dev/nvme0n1). If the character device is given, the '--namespace-id' option is mandatory, otherwise it will use the ns-id of the namespace for the block device you opened. For block devices, the ns-id used can be overridden with the same option. 

 On success, the structure may be returned in one of several ways depending on the option flags; the structure may be parsed by the program or the raw buffer may be printed to stdout.

<h2>OPTIONS</h2>

 

 -n &lt;nsid&gt;, --namespace-id=&lt;nsid&gt;
<dl>
<dt>
<dd> Retrieve the identify namespace structure for the given nsid. This is required for the character devices, or overrides the block nsid if given.</dl>
 

 -f, --force
<dl>
<dt>
<dd> Request controller return the indentify namespace structure even if the namespace is not attached to the controller. This is valid only for controllers at or newer than revision 1.2. Controllers at revision lower than this may interpret the command incorrectly.</dl>
 

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
# nvme id-ns /dev/nvme0n1
</pre></dl>
</dl>
 

<dl>
<dt>
<dd> &bull; If using the character device or overriding namespace id: 

<dl>
<dt>
<dd> <pre>
# nvme id-ns /dev/nvme0 -n 1
# nvme id-ns /dev/nvme0n1 -n 1
# nvme id-ns /dev/nvme0 --namespace-id=1
</pre></dl>
</dl>
 

<dl>
<dt>
<dd> &bull; In addition to showing the known fields, have the program to display the vendor unique field: 

<dl>
<dt>
<dd> <pre>
# nvme id-ns /dev/nvme0n1 --vendor-specific
# nvme id-ns /dev/nvme0n1 -v
</pre></dl>
 

 The above will dump the 'vs' buffer in hex since it doesn't know how to interpret it.</dl>
 

<dl>
<dt>
<dd> &bull; Have the program return the raw structure in binary: 

<dl>
<dt>
<dd> <pre>
# nvme id-ns /dev/nvme0n1 --raw-binary &gt; id_ns.raw
# nvme id-ns /dev/nvme0n1 -b &gt; id_ns.raw
</pre></dl>
 

 It is probably a bad idea to not redirect stdout when using this mode.</dl>
 

<dl>
<dt>
<dd> &bull; Alternatively you may want to send the data to another program that can parse the raw buffer. 

<dl>
<dt>
<dd> <pre>
# nvme id-ns /dev/nvme0n1 --raw-binary | nvme_parse_id_ns
</pre></dl>
 

 The parse program in the above example can be a program that shows the structure in a way you like. The following program is such an example that will parse it and can accept the output through a pipe, '|', as shown in the above example, or you can 'cat' a saved output buffer to it.</dl>
 

<dl>
<dt>
<dd> <pre><code>
/* File: nvme_parse_id_ns.c */
#include &lt;linux/nvme.h&gt;
#include &lt;stdio.h&gt;
#include &lt;unistd.h&gt;
int main(int argc, char **argv)
{
    unsigned char buf[sizeof(struct nvme_id_ns)];
    struct nvme_id_ns *ns = (struct nvme_id_ns *)buf;
    if (read(STDIN_FILENO, buf, sizeof(buf)))
        return 1;
    printf("nsze : %#llx\n", ns-&gt;nsze);
    printf("ncap : %#llx\n", ns-&gt;ncap);
    return 0;
}
</code></pre></dl>

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


