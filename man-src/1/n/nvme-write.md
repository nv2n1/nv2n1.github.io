---
title: "nvme-write(1)"
name: "nvme-write"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-write/"
---

<h2 class="name">NAME</h2>
 

 nvme-write - Send an NVMe write command, provide results 

<h2>SYNOPSIS</h2>

 

 <pre><code>
nvme - write&lt;device&gt;[--start - block = &lt;slba&gt; | -s&lt;slba&gt;]
                    [--block - count = &lt;nlb&gt; | -c&lt;nlb&gt;]
                    [--data - size = &lt;size&gt; | -z&lt;size&gt;]
                    [--metadata - size = &lt;size&gt; | -y&lt;size&gt;]
                    [--ref - tag = &lt;reftag&gt; | -r&lt;reftag&gt;]
                    [--data = &lt;data - file&gt; | -d&lt;data - file&gt;]
                    [--metadata = &lt;metadata - file&gt; | -M&lt;metadata - file&gt;]
                    [--prinfo = &lt;prinfo&gt; | -p&lt;prinfo&gt;]
                    [--app - tag - mask = &lt;appmask&gt; | -m&lt;appmask&gt;]
                    [--app - tag = &lt;apptag&gt; | -a&lt;apptag&gt;]
                    [--limited - retry | -l]
                    [--latency | -t]
                    [--force - unit - access | -f]
</code></pre>

<h2>DESCRIPTION</h2>

 

 The Write command writes the logical blocks specified by the command to the medium from the data data buffer provided. Will use stdin by default if you don't provide a file.

<h2>OPTIONS</h2>

 

 --start-block=&lt;slba&gt;, -s &lt;slba&gt;
<dl>
<dt>
<dd> Start block.</dl>
 

 --latency, -t
<dl>
<dt>
<dd> Print out the latency the IOCTL took (in us).</dl>

<h2>EXAMPLES</h2>

 

 No examples yet.

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


