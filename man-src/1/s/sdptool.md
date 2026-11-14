---
title: "sdptool(1)"
name: "sdptool"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sdptool/"
description: "sdptool – control and interrogate SDP servers"
---

<h2 class="name">NAME</h2>
<p> sdptool &#8211; control and interrogate SDP servers </p>
<h2>SYNOPSIS</h2>
<p> <code>sdptool</code> [<i>OPTIONS</i>] [<i>COMMAND</i> [<i>PARAMETERS</i>]]</p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-sdptool/">sdptool</a>(1)</code> provides the interface for performing SDP queries on Bluetooth devices, and administering a local SDP database.</p>
<h2>COMMANDS</h2>
<p> The following commands are available. In all cases <code>bdaddr</code> specifies the device to search or browse. If <i>local</i> is used for <code>bdaddr</code>, then the local SDP database is searched. </p>
<p> Services are identified and manipulated with a 4-byte <code>record_handle</code> (NOT the service name). To find a service&#8217;s <code>record_handle</code>, look for the &quot;Service RecHandle&quot; line in the <code>search</code> or <code>browse</code> results</p>
<dl>
<dt><code>search [&#8211;bdaddr bdaddr] [&#8211;tree] [&#8211;raw] [&#8211;xml] service_name</code></p>
<dd> Search for services.. </p>
<p> Known service names are <code>DID</code>, <code>SP</code>, <code>DUN</code>, <code>LAN</code>, <code>FAX</code>, <code>OPUSH</code>, <code>FTP</code>, <code>HS</code>, <code>HF</code>, <code>HFAG</code>, <code>SAP</code>, <code>NAP</code>, <code>GN</code>, <code>PANU</code>, <code>HCRP</code>, <code>HID</code>, <code>CIP</code>, <code>A2SRC</code>, <code>A2SNK</code>, <code>AVRCT</code>, <code>AVRTG</code>, <code>UDIUE</code>, <code>UDITE</code> and <code>SYNCML</code>.</p>
<dt><code>browse [&#8211;tree] [&#8211;raw] [&#8211;xml] [bdaddr]</code></p>
<dd> Browse all available services on the device specified by a Bluetooth address as a parameter.</p>
<dt><code>records [&#8211;tree] [&#8211;raw] [&#8211;xml] bdaddr</code></p>
<dd> Retrieve all possible service records.</p>
<dt><code>add [ &#8211;handle=N &#8211;channel=N ]</code></p>
<dd> Add a service to the local SDP database. </p>
<p> You can specify a handle for this record using the <code>&#8211;handle</code> option. </p>
<p> You can specify a channel to add the service on using the <code>&#8211;channel</code> option. </p>
<p> NOTE: Local adapters configuration will not be updated and this command should be used only for SDP testing.</p>
<dt><code>del record_handle</code></p>
<dd> Remove a service from the local SDP database. </p>
<p> NOTE: Local adapters configuration will not be updated and this command should be used only for SDP testing.</p>
<dt><code>get [&#8211;tree] [&#8211;raw] [&#8211;xml] [&#8211;bdaddr bdaddr] record_handle</code></p>
<dd> Retrieve a service from the local SDP database.</p>
<dt><code>setattr record_handle attrib_id attrib_value</code></p>
<dd> Set or add an attribute to an SDP record.</p>
<dt><code>setseq record_handle attrib_id attrib_values</code></p>
<dd> Set or add an attribute sequence to an SDP record.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Displays help on using sdptool.</dl>
<h2>EXAMPLES</h2>
<pre>
$ sdptool browse 00:80:98:24:15:6D
$ sdptool browse local
$ sdptool add DUN
$ sdptool del 0x10000
</pre>
<h2>RESOURCES</h2>
<p> <i><a rel="nofollow" href="http://www.bluez.org">http://www.bluez.org</a></i></p>
<h2>REPORTING BUGS</h2>
<p> <i>linux-bluetooth [at] vger.kernel.org</i></p>
<h2>AUTHOR</h2>
<p> Maxim Krasnyansky &lt;maxk [at] qualcomm.com&gt;, Edd Dumbill &lt;ejad [at] debian.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Free use of this software is granted under ther terms of the GNU Lesser General Public Licenses (LGPL). </p>
<h2>Index</h2>
