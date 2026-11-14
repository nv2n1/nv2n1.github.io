---
title: "nvme-set-feature(1)"
name: "nvme-set-feature"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-set-feature/"
---

<h2 class="name">NAME</h2>
 

 nvme-set-feature - Sets an NVMe feature, returns applicable results 

<h2>SYNOPSIS</h2>

 

 <pre><code>
nvme set - feature&lt;device&gt;[--namespace - id = &lt;nsid&gt; | -n&lt;nsid&gt;]
                          [--feature - id = &lt;fid&gt; | -f&lt;fid&gt;][--value = &lt;value&gt;]
                          [--data - len = &lt;data - len&gt; | -l&lt;data - len&gt;]
                          [--data = &lt;data - file&gt; | -d&lt;data - file&gt;]
                          [--raw - binary | -b]
</code></pre>

<h2>DESCRIPTION</h2>

 

 Submits an NVMe Get Feature admin command and returns the applicable results. This may be the feature's value, or may also include a feature structure if the feature requires it (ex: LBA Range Type). 

 The &lt;device&gt; parameter is mandatory and may be either the NVMe character device (ex: /dev/nvme0), or a namespace block device (ex: /dev/nvme0n1). 

 On success, the returned feature's structure (if applicable) may be returned in one of several ways depending on the option flags; the structure may parsed by the program and printed in a readable format if it is a known structure, displayed in hex, or the raw buffer may be printed to stdout for another program to parse.

<h2>OPTIONS</h2>

 

 -n &lt;nsid&gt;, --namespace-id=&lt;nsid&gt;
<dl>
<dt>
<dd> Retrieve the feature for the given nsid. This is optional and most features do not use this value.</dl>
 

 -f &lt;fid&gt;, --feature-id=&lt;fid&gt;
<dl>
<dt>
<dd> The feature id to send with the command. Value provided should be in hex.</dl>
 

 -l &lt;data-len&gt;, --data-len=&lt;data-len&gt;
<dl>
<dt>
<dd> The data length for the buffer submitted for this feature. Most known features do not use this value. The exceptions are LBA Range Type and host identifier.</dl>
 

 -d &lt;data-file&gt;, --data=&lt;data-file&gt;
<dl>
<dt>
<dd> The data file for the buffer submitted for this feature. Most known features do not use this value. The exceptions is LBA Range Type and host identifier. This defaults to STDIN so files and echo can be piped.</dl>
 

 --value=&lt;value&gt;
<dl>
<dt>
<dd> The value for command dword 11, the value you want to set the feature to.</dl>

<h2>EXAMPLES</h2>

 

<dl>
<dt>
<dd> &bull; Retrieves the feature for Number of Queues, or feature id 7: 

<dl>
<dt>
<dd> <pre>
# nvme set-feature /dev/nvme0 -f 7
</pre></dl>
</dl>
 

<dl>
<dt>
<dd> &bull; The following retrieves the feature for the LBA Range Type, which implicitly requires a buffer and will be printed to the screen in human readable format: 

<dl>
<dt>
<dd> <pre>
# nvme set-feature /dev/nvme0 -f 3
</pre></dl>
</dl>
 

<dl>
<dt>
<dd> &bull; Retrieves the feature for the some vendor specific feature and specifically requesting a buffer be allocate for this feature, which will be displayed to the user in as a hex dump: 

<dl>
<dt>
<dd> <pre>
# nvme set-feature /dev/nvme0 -f 0xc0 -l 512
</pre></dl>
</dl>
 

<dl>
<dt>
<dd> &bull; Sets the host id to the ascii string. 

<dl>
<dt>
<dd> <pre>
# echo &quot;abcdefgh&quot; | nvme set-feature /dev/nvme0 -f 0x81 -l 8
</pre></dl>
</dl>
 

<dl>
<dt>
<dd> &bull; The following retrieves the feature for the LBA Range Type, which implicitly requires a buffer and will be saved to a file in its raw format: 

<dl>
<dt>
<dd> <pre>
# nvme set-feature /dev/nvme0 -f 3 --raw-binary &gt; lba_range.raw
</pre></dl>
 

 It is probably a bad idea to not redirect stdout when using this mode.</dl>

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


