---
title: "rdma-ndd(8)"
name: "rdma-ndd"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rdma-ndd/"
description: "RDMA-NDD – RDMA device Node Description update daemon"
---

<p>RDMA-NDD &#8211; RDMA device Node Description update daemon</p>
<h2>Synopsis</h2>
<p>rdma-ndd &lt;options&gt;</p>
<h2>Description</h2>
<p>rdma-ndd is a system daemon which watches for rdma device changes and/or hostname changes and updates the Node Description of the rdma devices based on those changes.</p>
<h2>Details</h2>
<p>Full operation of this daemon requires kernels which support polling of the procfs hostname file as well as libudev. </p>
<p> If your system does not support either of these features, the daemon will set the Node Descriptions at start up and then sleep forever.</p>
<h3>Node Description configuration</h3>
<p>The daemon uses the environment variable RDMA_NDD_ND_FORMAT to set the node description. The following wild cards can be specified for more dynamic control. </p>
<p> %h &#8212; replace with the current hostname (not including domain) </p>
<p> %d &#8212; replace with the device name (for example mlx4_0, qib0, etc.) </p>
<p> If not specified the default is &quot;%h %d&quot;. </p>
<p> NOTE: At startup, and on new device detection, the Node Description is always written to ensure the SM and rdma-ndd are in sync. Subsequent events will only write the Node Description on a device if it has changed.</p>
<h3>Using systemd</h3>
<p>Setting the environment variable for the daemon is normally be done via a systemd drop in unit. For example the following could be added to a file named /etc/systemd/system/rdma-ndd.service.d/nd-format.conf to use only the hostname as your node description. </p>
<p> [Service] Environment=&quot;RDMA_NDD_ND_FORMAT=%%h&quot; </p>
<p> NOTE: Systemd requires an extra &#8216;%&#8217;.</p>
<h2>Options</h2>
<p><code>-f, &#8211;foreground</code> Run in the foreground instead of as a daemon </p>
<p> <code>-d, &#8211;debugging</code> Log additional debugging information to syslog</p>
<h2>Author</h2>
<dl>
<dt><code>Ira Weiny</code></p>
<dd>&lt; <i>ira.weiny [at] intel.com</i> &gt; </p>
</dl>
