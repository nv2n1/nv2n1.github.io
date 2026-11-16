---
title: "nvme-get-feature(1)"
name: "nvme-get-feature"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-get-feature/"
---

<h2 class="name">NAME</h2>
 

 nvme-get-feature - Gets an NVMe feature, returns applicable results 

<h2>SYNOPSIS</h2>

 

 <pre><code>
nvme get - feature&lt;device&gt;[--namespace - id = &lt;nsid&gt; | -n&lt;nsid&gt;]
                          [--feature - id = &lt;fid&gt; | -f&lt;fid&gt;][--cdw11 = &lt;cdw11&gt;]
                          [--data - len = &lt;data - len&gt; | -l&lt;data - len&gt;]
                          [--sel = &lt;select&gt; | -s&lt;select&gt;]
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
</dt><dd> Retrieve the feature for the given nsid. This is optional and most features do not use this value.</dd></dl>
 

 -f &lt;fid&gt;, --feature-id=&lt;fid&gt;
<dl>
<dt>
</dt><dd> The feature id to send with the command. Value provided should be in hex.</dd></dl>
 

 -s &lt;select&gt;, --sel=&lt;select&gt;
<dl>
<dt>
</dt><dd> Select (SEL): This field specifies which value of the attributes to return in the provided data: <table BORDER> <tr VALIGN=top><td> Select </td><td> Description 
</td></tr> <tr VALIGN=top><td> 0 </td><td> Current 
</td></tr> <tr VALIGN=top><td> 1 </td><td> Default 
</td></tr> <tr VALIGN=top><td> 2 </td><td> Saved 
</td></tr> <tr VALIGN=top><td> 3 </td><td> Supported capabilities 
</td></tr> <tr VALIGN=top><td> 4-7 </td><td> Reserved 
</td></tr> </table> 
</dd></dl>
 

 -l &lt;data-len&gt;, --data-len=&lt;data-len&gt;
<dl>
<dt>
</dt><dd> The data length for the buffer returned for this feature. Most known features do not use this value. The exception is LBA Range Type</dd></dl>
 

 --cdw11=&lt;cdw11&gt;
<dl>
<dt>
</dt><dd> The value for command dword 11, if applicable. Only known feature using this is the interrupt vector configuration feature.</dd></dl>
 

 -b, --raw-binary
<dl>
<dt>
</dt><dd> Print the raw feature buffer to stdout if the feature returns a structure.</dd></dl>

<h2>EXAMPLES</h2>

 

<dl>
<dt>
</dt><dd> &bull; Retrieves the feature for Number of Queues, or feature id 7: 
</dd><dl>
<dt>
</dt><dd> <pre>
# nvme get-feature /dev/nvme0 -f 7
</pre></dd></dl>
</dl>
 

<dl>
<dt>
</dt><dd> &bull; The following retrieves the feature for the LBA Range Type, which implicitly requires a buffer and will be printed to the screen in human readable format: 
</dd><dl>
<dt>
</dt><dd> <pre>
# nvme get-feature /dev/nvme0 -f 3
</pre></dd></dl>
</dl>
 

<dl>
<dt>
</dt><dd> &bull; Retrieves the feature for the some vendor specific feature and specifically requesting a buffer be allocate for this feature, which will be displayed to the user in as a hex dump: 
</dd><dl>
<dt>
</dt><dd> <pre>
# nvme get-feature /dev/nvme0 -f 0xc0 -l 512
</pre></dd></dl>
</dl>
 

<dl>
<dt>
</dt><dd> &bull; The following retrieves the feature for the LBA Range Type, which implicitly requires a buffer and will be saved to a file in its raw format: 
</dd><dl>
<dt>
</dt><dd> <pre>
# nvme get-feature /dev/nvme0 -f 3 --raw-binary &gt; lba_range.raw
</pre></dd></dl>
 

 It is probably a bad idea to not redirect stdout when using this mode.</dl>

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


