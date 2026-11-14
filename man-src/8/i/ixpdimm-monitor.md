---
title: "ixpdimm-monitor(8)"
name: "ixpdimm-monitor"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ixpdimm-monitor/"
description: "ixpdimm-monitor – Daemon to monitor Intel(R) DIMM management events. Used by ixpdimm-cli."
---

<p>ixpdimm-monitor &#8211; Daemon to monitor Intel(R) DIMM management events. Used by ixpdimm-cli. </p>
<h2>Synopsis</h2>
<p><code>ixpdimm-monitor</code> [<code>-d</code>] </p>
<h2>Description</h2>
<p>Daemon to monitor Intel(R) DIMM management events. These events can be viewed using ixpdimm-cli. </p>
<h2>Option</h2>
<dl>
<dt><code>-d</code></p>
<dd>Starts <code>ixpdimm-monitor</code> as a background daemon. </p>
</dl>
<h2>Exit Codes</h2>
<dl>
<dt><code>0</code></p>
<dd>The operation succeeded.</p>
<dt><code>1</code></p>
<dd>An error occurred. </p>
</dl>
<h2>Files</h2>
<p>/var/lib/ixpdimm_sw/apss.dat<br />
 /var/run/ixpdimm-monitor.pid</p>
<h2>See Also</h2>
<p>ixpdimm-cli (8) </p>
<h2>Author</h2>
<p>Created by Intel Corporation.</p>
