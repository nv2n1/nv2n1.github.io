---

title: "dtest(1)"
name: "dtest"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dtest/"
description: "dtest – simple uDAPL send/receive and RDMA test"
---

<p> <code>dtest</code> [-P provider] [-b buf size] [-B burst count][-v] [-c] [-p] [-d]<code> [-s]</code> </p>
<p> <code>dtest</code> [-P provider] [-b buf size] [-B burst count][-v] [-c] [-p] [-d]<code> [-h HOSTNAME]</code> </p>
<p> dtest is a simple test used to exercise and verify the uDAPL interfaces. At least two instantiations of the test must be run. One acts as the server and the other the client. The server side of the test, once invoked listens for connection requests, until timing out or killed. Upon receipt of a cd connection request, the connection is established, the server and client sides exchange information necessary to perform RDMA writes and reads. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-P</code>=<i>PROVIDER</i></dt>
<dd> use <i>PROVIDER</i> to specify uDAPL interface using /etc/dat.conf (default OpenIB-cma)</dd>
<dt><code>-b</code>=<i>BUFFER_SIZE</i></dt>
<dd> use buffer size <i>BUFFER_SIZE</i> for RDMA(default 64)</dd>
<dt><code>-B</code>=<i>BURST_COUNT</i></dt>
<dd> use busrt count <i>BURST_COUNT</i> for interations (default 10)</dd>
<dt><code>-v</code>, verbose output(default off)</dt>
<dd>
</dd><dt><code>-c</code>, use consumer notification events (default off)</dt>
<dd>
</dd><dt><code>-p</code>, use polling (default wait for event)</dt>
<dd>
</dd><dt><code>-d</code>, delay in seconds before close (default off)</dt>
<dd>
</dd><dt><code>-s</code>, run as server (default &#8211; run as server)</dt>
<dd>
</dd><dt><code>-h</code>=<i>HOSTNAME</i></dt>
<dd> use <i>HOSTNAME</i> to specify server hostname or IP address (default &#8211; none) </dd>
</dl>
<h2>EXAMPLES</h2>
<p> dtest -P OpenIB-cma -v -s </p>
<pre>
     Starts a server process with debug verbosity using provider OpenIB-cma.
</pre>
<p> dtest -P OpenIB-cma -h server1-ib0 </p>
<pre>
     Starts a client process, using OpenIB-cma provider to connect to hostname server1-ib0.
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dapltest/">dapltest</a>(1)</code> </p>
<h2>AUTHORS</h2>
<dl>
<dt>Arlin Davis</dt>
<dd> &lt;<i>ardavis [at] ichips.intel.com</i>&gt; </dd>
</dl>
<h2>BUGS</h2>
