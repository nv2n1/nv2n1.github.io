---
title: "nvme-compare(1)"
name: "nvme-compare"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-compare/"
---

<h2 class="name">NAME</h2>
 

 nvme-compare - Send an NVMe Compare command, provide results 

<h2>SYNOPSIS</h2>

 

 <pre><code>
nvme - compare&lt;device&gt;[--start - block = &lt;slba&gt; | -s&lt;slba&gt;]
                      [--block - count = &lt;nlb&gt; | -c&lt;nlb&gt;]
                      [--data - size = &lt;size&gt; | -z&lt;size&gt;]
                      [--ref - tag = &lt;reftag&gt; | -r&lt;reftag&gt;]
                      [--data = &lt;data - file&gt; | -d&lt;data - file&gt;]
                      [--prinfo = &lt;prinfo&gt; | -p&lt;prinfo&gt;]
                      [--app - tag - mask = &lt;appmask&gt; | -m&lt;appmask&gt;]
                      [--app - tag = &lt;apptag&gt; | -a&lt;apptag&gt;]
                      [--limited - retry | -l]
                      [--force - unit - access | -f]
</code></pre>

<h2>DESCRIPTION</h2>

 

 The Compare command reads the logical blocks specified by the command from the medium and compares the data read to a comparison data buffer transferred as part of the command. If the data read from the controller and the comparison data buffer are equivalent with no miscompares, then the command completes successfully. If there is any miscompare, the command completes with an error of Compare Failure. If metadata is provided, then a comparison is also performed for the metadata.

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


