---
title: "nvme-create-ns(1)"
name: "nvme-create-ns"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-create-ns/"
---

<h2 class="name">NAME</h2>
 

 nvme-create-ns - Send NVMe Namespace management command to create namespace, returns results. 

<h2>SYNOPSIS</h2>

 

 <pre><code>
nvme create - ns&lt;device&gt;[--nsze = &lt;nsze&gt; | -s&lt;nsze&gt;]
                        [--ncap = &lt;ncap&gt; | -c&lt;ncap&gt;]
                        [--flbas = &lt;flbas&gt; | -f&lt;flbas&gt;]
                        [--dps = &lt;dps&gt; | -d&lt;dps&gt;]
                        [--nmic = &lt;nmic&gt; | -m&lt;nmic&gt;]
</code></pre>

<h2>DESCRIPTION</h2>

 

 For the NVMe device given, sends a namespace management command to create the namespace with the requested settings. On success, the namespace identifier assigned by the controller is returned. 

 The &lt;device&gt; parameter is mandatory and may be either the NVMe character device (ex: /dev/nvme0), or a namespace block device (ex: /dev/nvme0n1).

<h2>OPTIONS</h2>

 

 -s, --nsze
<dl>
<dt>
<dd> The namespace size.</dl>
 

 -c, --ncap
<dl>
<dt>
<dd> The namespace capacity.</dl>
 

 -f, --flbas
<dl>
<dt>
<dd> The namespace formatted logical block size setting.</dl>
 

 -d, --dps
<dl>
<dt>
<dd> The data protection settings.</dl>
 

 -m, --nmic
<dl>
<dt>
<dd> Namespace multipath and sharing capabilities.</dl>

<h2>EXAMPLES</h2>

 

 No examples provided yet.

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


