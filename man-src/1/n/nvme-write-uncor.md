---
title: "nvme-write-uncor(1)"
name: "nvme-write-uncor"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-write-uncor/"
---

<h2 class="name">NAME</h2>
 

 nvme-write-uncor - Send an NVMe write uncorrectable command, return results 

<h2>SYNOPSIS</h2>

 

 <pre><code>
nvme - write - zeroes&lt;device&gt;[--start - block = &lt;slba&gt; | -s&lt;slba&gt;][--block - count = &lt;nlb&gt; | -c&lt;nlb&gt;][--namespace - id = &lt;nsid&gt; | -n&lt;nsid&gt;]
</code></pre>

<h2>DESCRIPTION</h2>

 

 The Write Zeroes command is used to set a range of logical blocks to 0.

<h2>OPTIONS</h2>

 

 --start-block=&lt;slba&gt;, -s &lt;slba&gt;
<dl>
<dt>
<dd> Start block.</dl>

<h2>EXAMPLES</h2>

 

 No examples yet.

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


