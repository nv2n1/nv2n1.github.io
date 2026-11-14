---
title: "nvme-write-zeroes(1)"
name: "nvme-write-zeroes"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-write-zeroes/"
---

<h2 class="name">NAME</h2>
 

 nvme-write-zeroes - Send an NVMe write zeroes command, return results 

<h2>SYNOPSIS</h2>

 

 <pre><code>
nvme - write - zeroes&lt;device&gt;[--start - block = &lt;slba&gt; | -s&lt;slba&gt;][--block - count = &lt;nlb&gt; | -c&lt;nlb&gt;][--ref - tag = &lt;reftag&gt; | -r&lt;reftag&gt;][--prinfo = &lt;prinfo&gt; | -p&lt;prinfo&gt;][--app - tag - mask = &lt;appmask&gt; | -m&lt;appmask&gt;][--app - tag = &lt;apptag&gt; | -a&lt;apptag&gt;][--limited - retry | -l][--force - unit - access | -f][--namespace - id = &lt;nsid&gt; | -n&lt;nsid&gt;]
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


