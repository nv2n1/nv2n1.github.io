---
title: "ibnd_discover_fabric(3)"
name: "ibnd_discover_fabric"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibnd_discover_fabric/"
description: "ibnd_discover_fabric, ibnd_destroy_fabric, ibnd_debug ibnd_show_progress – initialize ibnetdiscover library."
---

<h2>NAME</h2>
<p> ibnd_discover_fabric, ibnd_destroy_fabric, ibnd_debug ibnd_show_progress &#8211; initialize ibnetdiscover library.</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/ibnetdisc.h&gt;
void ibnd_destroy_fabric(ibnd_fabric_t *fabric) void ibnd_debug(int i) void ibnd_show_progress(int i) int ibnd_set_max_smps_on_wire(int i)
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibnd_discover_fabric()</code> Discover the fabric connected to the port specified by ibmad_port, using a timeout specified. The &quot;from&quot; and &quot;hops&quot; parameters are optional and allow one to scan part of a fabric by specifying a node &quot;from&quot; and a number of hops away from that node to scan, &quot;hops&quot;. This gives the user a &quot;sub-fabric&quot; which is &quot;centered&quot; anywhere they chose. </p>
<p> ibmad_port must be opened with at least IB_SMI_CLASS and IB_SMI_DIRECT_CLASS classes for ibnd_discover_fabric to work. </p>
<p> <code>ibnd_destroy_fabric()</code> free all memory and resources associated with the fabric. </p>
<p> <code>ibnd_debug()</code> Set the debug level to be printed as library operations take place. </p>
<p> <code>ibnd_show_progress()</code> Indicate that the library should print debug output which shows it&#8217;s progress through the fabric. </p>
<p> <code>ibnd_set_max_smps_on_wire()</code> Set the number of SMP&#8217;s which will be issued on the wire simultaneously. </p>
<h2>RETURN VALUE</h2>
<p> <code>ibnd_discover_fabric()</code> return NULL on failure, otherwise a valid ibnd_fabric_t object. </p>
<p> <code>ibnd_destory_fabric(), ibnd_debug()</code> NONE </p>
<p> <code>ibnd_set_max_smps_on_wire()</code> The previous value is returned </p>
<h2>EXAMPLES</h2>
<p> <code>Discover the entire fabric connected to device mthca0, port 1.</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>int mgmt_classes[2] = {IB_SMI_CLASS, IB_SMI_DIRECT_CLASS};<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>struct ibmad_port *ibmad_port = mad_rpc_open_port(ca, ca_port, mgmt_classes, 2);<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ibnd_fabric_t *fabric = ibnd_discover_fabric(ibmad_port, 100, NULL, 0);<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ibnd_destroy_fabric(fabric);<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mad_rpc_close_port(ibmad_port);</p>
<p> <code>Discover only a single node and those nodes connected to it.</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>str2drpath(&amp;(port_id.drpath), from, 0, 0);<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ibnd_discover_fabric(ibmad_port, 100, &amp;port_id, 1);<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;</p>
<h2>SEE ALSO</h2>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>libibmad, mad_rpc_open_port</p>
<h2>AUTHORS</h2>
<dl>
<dt>Ira Weiny &lt;weiny2 [at] llnl.gov&gt;</p>
<dd>
</dl>
<h2>Index</h2>
