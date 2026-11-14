---
title: "nvme-resv-report(1)"
name: "nvme-resv-report"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-resv-report/"
---

<h2 class="name">NAME</h2>
 

 nvme-resv-report - Send NVMe Reservation Report, parse the result 

<h2>SYNOPSIS</h2>

 

 <pre><code>
nvme resv - report&lt;device&gt;[--namespace - id = &lt;nsid&gt; | -n&lt;nsid&gt;]
                          [--numd = &lt;num - dwords&gt; | -d&lt;num - dwords&gt;]
                          [-b | --raw - binary]
</code></pre>

<h2>DESCRIPTION</h2>

 

 The Reservation Report command returns a Reservation Status data structure to host memory that describes the registration and reservation status of a namespace. 

 The size of the Reservation Status data structure is a function of the number of controllers in the NVM Subsystem that are associated with hosts that are registrants of the namespace (i.e., there is a Registered Controller data structure for each such controller).

<h2>OPTIONS</h2>

 

 -n &lt;nsid&gt;, --namespace-id=&lt;nsid&gt;
<dl>
<dt>
<dd> Retrieve the reservation report structure for the given nsid. This is required for the character devices, or overrides the block nsid if given.</dl>
 

 -d &lt;num-dwords&gt;, --numd=&lt;num-dwords&gt;
<dl>
<dt>
<dd> Specify the number of Dwords of the Reservation Status structure to transfer. Defaults to 4k.</dl>
 

 -b, --raw-binary
<dl>
<dt>
<dd> Print the raw buffer to stdout. Structure is not parsed by program.</dl>

<h2>EXAMPLES</h2>

 

 No examples yet.

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


