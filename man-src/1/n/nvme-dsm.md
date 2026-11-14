---
title: "nvme-dsm(1)"
name: "nvme-dsm"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-dsm/"
---

<h2 class="name">NAME</h2>
 

 nvme-dsm - Send NVMe Data Set Management, return results 

<h2>SYNOPSIS</h2>

 

 <pre><code>
nvme dsm&lt;device&gt;[--namespace - id = &lt;nsid&gt; | -n&lt;nsid&gt;]
                [--ctx - attrs = &lt;attribute - list, &gt; | -a&lt;attribute - list, &gt;]
                [--blocks = &lt;nlb - list, &gt; | -b&lt;nlb - list, &gt;]
                [--slbs = &lt;slba - list, &gt; | -s&lt;slba - list, &gt;]
                [--ad | -d][--idw | -w][--idr | -r]
                [--cdw11 = &lt;cdw11&gt; | -c&lt;cdw11&gt;]
</code></pre>

<h2>DESCRIPTION</h2>

 

 For the NVMe device given, sends an Data Set Management command and provides the result and returned structure. 

 The &lt;device&gt; parameter is mandatory and may be either the NVMe character device (ex: /dev/nvme0), or a namespace block device (ex: /dev/nvme0n1). If the character device is given, the '--namespace-id' option is mandatory, otherwise it will use the ns-id of the namespace for the block device you opened. For block devices, the ns-id used can be overridden with the same option. 

 You must specify at least one of the values for range list. If the range lists provided do not list the same number of elements, the default values for the remaining in the range will be set to 0. 

 The command dword 11 may be provided at the command line. For convenience, the current defined attributes (discard, integral read/write) for a data-set management have flags. If cdw11 is specified, this will override any settings from the flags may have provided.

<h2>OPTIONS</h2>

 

 -n &lt;nsid&gt;, --namespace-id=&lt;nsid&gt;
<dl>
<dt>
<dd> Sends the command with the requested nsid. This is required for the character devices, or overrides the block nsid if given.</dl>
 

 -a &lt;attribute-list,&gt;, --ctx-attrs=&lt;attribute-list&gt;
<dl>
<dt>
<dd> Comma separated list of the context attributes in each range</dl>
 

 -b &lt;nlb-list,&gt;, --blocks=&lt;nlb-list,&gt;
<dl>
<dt>
<dd> Comma separated list of the number of blocks in each range</dl>
 

 -s &lt;slba-list,&gt;, --slbs=&lt;slba-list,&gt;
<dl>
<dt>
<dd> Comma separated list of the starting block in each range</dl>
 

 -d &lt;deallocate&gt;, --ad=&lt;deallocate&gt;
<dl>
<dt>
<dd> Attribute Deallocate.</dl>
 

 -w &lt;write&gt;, --idw=&lt;write&gt;
<dl>
<dt>
<dd> Attribute Integral Dataset for Write.</dl>
 

 -r &lt;read&gt;, --idr=&lt;read&gt;
<dl>
<dt>
<dd> Attribute Integral Dataset for Read.</dl>
 

 -c &lt;cdw11&gt;, --cdw11=&lt;cdw11&gt;
<dl>
<dt>
<dd> All the command command dword 11 attributes. Use exclusive from specifying individual attributes</dl>

<h2>EXAMPLES</h2>

 

 No examples yet

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


