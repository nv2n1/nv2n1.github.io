---
title: "atmtcp(8)"
name: "atmtcp"
section: "8"
letter: "a"
url: "/docs/linux/man/8-atmtcp/"
description: "atmtcp – set up ATM over TCP connections"
---

<p>atmtcp &#8211; set up ATM over TCP connections</p>
<h2>Synopsis</h2>
<p><code>atmtcp</code> [<code>-d</code>] [<code>-v</code>] <i>command</i> <code>&#8230;</code><br />
 <code>atmtcp</code> <code>-V</code></p>
<h2>Description</h2>
<p>The main purpose of <code>atmtcp</code> is to establish TCP connections and to configure them as virtual ATM devices. Such pairs of &quot;ATM over TCP&quot; devices are connected as if they were real ATM adapters linked by a cable or fiber, i.e. SDUs sent on a given VPI/VCI are received at the other end on the same VPI/VCI. </p>
<p> Virtual interfaces and ATM over TCP connections are called <i>links</i>. Other link types supported by <code>atmtcp</code> are real interfaces, files for recording and playback of ATM traffic, and printing a hex dump of the PDU content on standard output. Any pair of such links can be connected with <code>atmtcp</code>. If additional links are attached to such a connection, they send to all other links, except to the first link and the respective sender, and they receive from all other links. </p>
<p> <code>atmtcp</code> can operate with two types of virtual interfaces: ephemeral or persistent. By default, <code>atmtcp</code> interfaces are ephemeral. When the <code>atmtcp</code> process that created an interface terminates, the virtual ATM device is removed as soon all VCs are closed. However, if the interface was previously created as a persistent interface, only the communication stops, but the interface and all VCs on it remain intact. Attempts to send data on an <code>atmtcp</code> interface in this state fail silently, i.e. the interface behaves just like a real ATM interface without a wire. A new <code>atmtcp</code> process can then attach to the interface and resume operation. Persistent interfaces need to be removed explicitly. </p>
<p> If <code>atmtcp</code> has any readable links after processing the command line, it enters a loop to perform the data forwarding. If no readable links have been specified, <code>atmtcp</code> terminates after processing the command line. If any setup operation fails, <code>atmtcp</code> terminates at this point and does not attempt to cancel previous operations (e.g. creation of permanent interfaces).</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code></p>
<dd>print detailed progress information on standard error.</p>
<dt><code>-v</code></p>
<dd>print some progress information on standard error.</p>
<dt><code>-V</code></p>
<dd>print version number of <code>atmtcp</code> on standard output and exit.</dl>
<h2>Commands</h2>
<dl>
<dt><code>create</code>&nbsp;<wbr>[<i>itf</i>]</p>
<dd>create a persistent interface. If no interface number is specified, <code>atmtcp</code> uses the default value 0.</p>
<dt><code>remove</code>&nbsp;<wbr>[<i>itf</i>]</p>
<dd>remove a persistent interface. If the interface is still in use, it is marked as ephemeral and will be removed as soon as all VCs are closed. If no interface number is specified, <code>atmtcp</code> uses the default value 0.</p>
<dt><code>virtual</code>&nbsp;<wbr>[<i>itf</i>]</p>
<dd>link to the corresponding virtual (ATM over TCP) interface. If no interface number is specified, the kernel assigns the first available number.</p>
<dt><code>real</code>&nbsp;<wbr>[<i>itf</i>]</p>
<dd>link to the corresponding ATM interface. If no interface number is specified, <code>atmtcp</code> uses the default value 0. If a link requests that a VC be opened, <code>atmtcp</code> will attempt to open a VC with the specified QoS parameters on that interface. If the operation succeeds, data can be sent or received on that VC. If the operation fails, an error code is returned to the requester. Note that only data arriving on open VCs can be received and that a <i>real</i> ATM interface never initiates a connection. <code>atmtcp</code> can share ATM interfaces with other applications.</p>
<dt><code>connect</code>&nbsp;<wbr><i>host</i>&nbsp;<wbr>[<i>port</i>]</p>
<dd>connect to an instance of <code>atmtcp</code> running on the specified host. If the port argument is omitted, <code>atmtcp</code> uses the default port 2812.</p>
<dt><code>switch</code>&nbsp;<wbr><i>host</i>&nbsp;<wbr><i>line</i>&nbsp;<wbr>[<i>port</i>]</p>
<dd>like <code>connect</code>, but connects to an ATM over TCP &quot;switch&quot; and selects the specified virtual line.</p>
<dt><code>listen</code>&nbsp;<wbr>[<i>port</i>]</p>
<dd>listen for an incoming ATM over TCP connection. If the port argument is omitted, <code>atmtcp</code> uses the default port 2812. <code>atmtcp</code> waits until the connection is established. Only one connection is accepted per <code>listen</code> command.</p>
<dt><code>listen-bg</code>&nbsp;<wbr>[<i>port</i>]</p>
<dd>like <code>listen</code>, but run in background after beginning to listen.</p>
<dt><code>read</code>&nbsp;<wbr><i>file</i>&nbsp;<wbr>[<i>stream</i>]</p>
<dd>play back all streams from the specified file. If a stream number is specified, only that stream is played back.</p>
<dt><code>write</code>&nbsp;<wbr><i>file</i></p>
<dd>record the traffic of all links in the specified file. The PDUs from each link are stored in a stream with the same number as the link.</p>
<dt><code>print</code></p>
<dd>print a hex dump of the content of all received PDUs on standard output.</p>
<dt><code>bg</code></p>
<dd>continue to run in background (i.e. in a forked child process).</p>
<dt><code>wait</code>&nbsp;<wbr>[<i>seconds</i>]</p>
<dd>wait for the specified number of seconds. If no time is specified, <code>atmtcp</code> waits for a newline on standard input.</dl>
<h2>Restrictions</h2>
<p>Due to recent protocol changes, <code>atmtcp</code> is currently not compatible with the ATM over TCP &quot;switch&quot;. </p>
<p> Only AAL SDUs are exchanged, no segmentation or reassembly is performed. That implies that using different AALs (e.g. AAL5 and AAL0) on either side will reveal limitations of this emulation. </p>
<p> The <code>atmtcp</code> process needs to run during the the whole lifetime of the connection.</p>
<h2>Examples</h2>
<p>Create a pair of virtual ATM over TCP interfaces on the local host and connect them: </p>
<pre> # session A
 atmtcp virtual listen
 # session B
 atmtcp virtual connect localhost</pre>
<p>Create virtual interface 1, connect it to real ATM interface 0, then start <code>atmsigd</code> on the virtual interface, and log all the traffic in a file: </p>
<pre> atmtcp virtual 1 real 0 write /tmp/log
 atmsigd 1.0.5</pre>
<p>Take the previously created file and examine the traffic sent from <code>atmsigd</code> using <code>saaldump</code>: </p>
<pre> # session A
 atmtcp virtual 1 read /tmp/log 0 wait
 # session B
 saaldump 1.0.5
 # press [Enter] in session A</pre>
<h2>Author</h2>
<p>Werner Almesberger, EPFL ICA &lt;Werner.Almesberger [at] epfl.ch&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-atmdiag/">atmdiag</a>(8) </p>
