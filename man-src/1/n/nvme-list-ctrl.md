---
title: "nvme-list-ctrl(1)"
name: "nvme-list-ctrl"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-list-ctrl/"
---

<h2 class="name">NAME</h2>
 

 nvme-list-ctrl - Send NVMe Identify List Controllers, return result and structure 

<h2>SYNOPSIS</h2>

 

 <pre><code>
nvme list - ctrl&lt;device&gt;[--cntid = &lt;cntid&gt; | -c&lt;cntid&gt;]
                        [--namespace - id = &lt;nsid&gt; | -n&lt;nsid&gt;] DESCRIPTION
</code></pre> 

 <pre>
For the NVMe device given, sends an identify command for controller list
and provides the result and returned structure. This uses either mode
12h or 13h depending on the requested namespace identifier.
The &lt;device&gt; parameter is mandatory and may be either the NVMe character
device (ex: /dev/nvme0), or a namespace block device (ex: /dev/nvme0n1).
The starting controller in the list always begins with 0 unless the
`'--cntid'` option is given to override.
On success, the controller array is printed for each index and controller
identifier.
OPTIONS
</pre> 

 -c &lt;cntid&gt;, --cntid=&lt;cntid&gt;
<dl>
<dt>
<dd> Retrieve the identify list structure starting with the given controller id.</dl>
 

 -n &lt;nsid&gt;, --namespace-id=&lt;nsid&gt;
<dl>
<dt>
<dd> If provided, will request the controllers attached to the specified namespace. If no namespace is given, or set to 0, the command requests the controller list for the entire subsystem, whether or not they are attached to namespace(s).</dl>

<h2>EXAMPLES</h2>

 

 No examples yet.

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


