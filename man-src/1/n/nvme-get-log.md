---
title: "nvme-get-log(1)"
name: "nvme-get-log"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-get-log/"
---

<h2 class="name">NAME</h2>
 

 nvme-get-log - Retrieves a log page from an NVMe device 

<h2>SYNOPSIS</h2>

 

 <pre><code>
nvme get - log&lt;device&gt;[--log - id = &lt;log - id&gt; | -i&lt;log - id&gt;]
                      [--log - len = &lt;log - len&gt; | -l&lt;log - len&gt;]
                      [--namespace - id = &lt;nsid&gt; | -n&lt;nsid&gt;]
                      [--raw - binary | -b]
</code></pre>

<h2>DESCRIPTION</h2>

 

 Retrieves an arbitrary NVMe log page from an NVMe device and provides the retuned structure. 

 The &lt;device&gt; parameter is mandatory and may be either the NVMe character device (ex: /dev/nvme0), or a namespace block device (ex: /dev/nvme0n1). 

 On success, the returned log structure may be returned in one of several ways depending on the option flags; the structure may be displayed in hex by the program or the raw buffer may be printed to stdout for another program to parse.

<h2>OPTIONS</h2>

 

 -l &lt;log-len&gt;, --log-len=&lt;log-len&gt;
<dl>
<dt>
<dd> Allocates a buffer of &lt;log-len&gt; bytes size and requests this many bytes be returned in the constructed NVMe command. This param is mandatory.</dl>
 

 -i &lt;log-id&gt;, --log-id=&lt;log-id&gt;
<dl>
<dt>
<dd> Sets the commands requested log-id to &lt;log-id&gt;. Defaults to 0.</dl>
 

 -n &lt;nsid&gt;, --namespace-id=&lt;nsid&gt;
<dl>
<dt>
<dd> Sets the command's nsid value to the given nsid. Defaults to 0xffffffff if not given. This option may not affect anything depending on the log page, which may or may not be specific to a namespace.</dl>
 

 -b, --raw-binary
<dl>
<dt>
<dd> Print the raw log buffer to stdout.</dl>

<h2>EXAMPLES</h2>

 

<dl>
<dt>
<dd> &bull; Get 512 bytes from log page 2 

<dl>
<dt>
<dd> <pre>
# nvme get-log /dev/nvme0 --log-id=2 --log-len=512
</pre></dl>
 

 The above example will get log page 2 (SMART), and request 512 bytes. On success, the returned log will be dumped in hex and not interpreted by the program.</dl>
 

<dl>
<dt>
<dd> &bull; Have the program return the raw log page in binary: 

<dl>
<dt>
<dd> <pre>
# nvme get-log /dev/nvme0 -log-id=2 --log-len=512 --raw-binary &gt; log_page_2.raw
# nvme get-log /dev/nvme0 -i 2 -l 512 -b &gt; log_page_2.raw
</pre></dl>
 

 It is not a good idea to not redirect stdout when using this mode.</dl>

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


