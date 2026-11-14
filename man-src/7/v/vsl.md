---
title: "vsl(7)"
name: "vsl"
section: "7"
letter: "v"
url: "/docs/linux/man/7-vsl/"
description: "VSL – Shared Memory Logging"
---

<p>VSL &#8211; Shared Memory Logging</p>
<h2>Overview</h2>
<p>This document describes the format and content of all the Varnish shared memory logging tags. These tags are used by the <a href="/docs/linux/man/1-varnishlog/">varnishlog</a>(1), <a href="/docs/linux/man/1-varnishtop/">varnishtop</a>(1), etc. logging tools supplied with Varnish.</p>
<h3>VSL tags</h3>
<dl>
<dt><code>Backend &#8211; Backend selected</code></p>
<dd>Logged when a connection is selected for handling a backend request. </p>
<p> The format is: </p>
<pre>%d %s %s
| | |
| | +- Backend display name
| +---- VCL name
+------- Connection file descriptor</pre>
<dt><code>BackendClose &#8211; Backend connection closed</code></p>
<dd>Logged when a backend connection is closed. </p>
<p> The format is: </p>
<pre>%d %s [ %s ]
| | |
| | +- Optional reason
| +------ Backend display name
+--------- Connection file descriptor</pre>
<dt><code>BackendOpen &#8211; Backend connection opened</code></p>
<dd>Logged when a new backend connection is opened. </p>
<p> The format is: </p>
<pre>%d %s %s %s
| | | |
| | | +- Remote port
| | +---- Remote address
| +------- Backend display name
+---------- Connection file descriptor</pre>
<dt><code>BackendReuse &#8211; Backend connection put up for reuse</code></p>
<dd>Logged when a backend connection is put up for reuse by a later connection. </p>
<p> The format is: </p>
<pre>%d %s
| |
| +- Backend display name
+---- Connection file descriptor</pre>
<dt><code>Backend_health &#8211; Backend health check</code></p>
<dd>The result of a backend health probe. </p>
<p> The format is: </p>
<pre>%s %s %s %u %u %u %f %f %s
| | | | | | | | |
| | | | | | | | +- Probe HTTP response
| | | | | | | +---- Average response time
| | | | | | +------- Response time
| | | | | +---------- Probe window size
| | | | +------------- Probe threshold level
| | | +---------------- Number of good probes in window
| | +------------------- Probe window bits
| +---------------------- Status message
+------------------------- Backend name</pre>
<dt><code>Begin &#8211; Marks the start of a VXID</code></p>
<dd>The first record of a VXID transaction. </p>
<p> The format is: </p>
<pre>%s %d %s
| | |
| | +- Reason
| +---- Parent vxid
+------- Type (&quot;sess&quot;, &quot;req&quot; or &quot;bereq&quot;)</pre>
<dt><code>BereqAcct &#8211; Backend request accounting</code></p>
<dd>Contains byte counters from backend request processing. </p>
<p> The format is: </p>
<pre>%d %d %d %d %d %d
| | | | | |
| | | | | +- Total bytes received
| | | | +---- Body bytes received
| | | +------- Header bytes received
| | +---------- Total bytes transmitted
| +------------- Body bytes transmitted
+---------------- Header bytes transmitted</pre>
<dt><code>BereqHeader &#8211; Backend request header</code></p>
<dd>HTTP header contents. </p>
<p> The format is: </p>
<pre>%s: %s
| |
| +- Header value
+----- Header name</pre>
<dt><code>BereqMethod &#8211; Backend request method</code></p>
<dd>The HTTP request method used.</p>
<dt><code>BereqProtocol &#8211; Backend request protocol</code></p>
<dd>The HTTP protocol version information.</p>
<dt><code>BereqURL &#8211; Backend request URL</code></p>
<dd>The HTTP request URL.</p>
<dt><code>BerespHeader &#8211; Backend response header</code></p>
<dd>HTTP header contents. </p>
<p> The format is: </p>
<pre>%s: %s
| |
| +- Header value
+----- Header name</pre>
<dt><code>BerespProtocol &#8211; Backend response protocol</code></p>
<dd>The HTTP protocol version information.</p>
<dt><code>BerespReason &#8211; Backend response response</code></p>
<dd>The HTTP response string received.</p>
<dt><code>BerespStatus &#8211; Backend response status</code></p>
<dd>The HTTP status code received.</p>
<dt><code>BogoHeader &#8211; Bogus HTTP received</code></p>
<dd>Contains the first 20 characters of received HTTP headers we could not make sense of. Applies to both req.http and beresp.http.</p>
<dt><code>CLI &#8211; CLI communication</code></p>
<dd>CLI communication between varnishd master and child process.</p>
<dt><code>Debug &#8211; Debug messages</code></p>
<dd>Debug messages can normally be ignored, but are sometimes helpful during trouble-shooting. Most debug messages must be explicitly enabled with parameters.</p>
<dt><code>ESI_BodyBytes &#8211; ESI body fragment byte counter</code></p>
<dd>Contains the body byte count for this ESI body fragment. This number does not include any transfer encoding overhead. </p>
<p> The format is: </p>
<pre>%d
|
+- Body bytes</pre>
<dt><code>ESI_xmlerror &#8211; ESI parser error or warning message</code></p>
<dd>An error or warning was generated during parsing of an ESI object. The log record describes the problem encountered.</p>
<dt><code>End &#8211; Marks the end of a VXID</code></p>
<dd>The last record of a VXID transaction.</p>
<dt><code>Error &#8211; Error messages</code></p>
<dd>Error messages are stuff you probably want to know.</p>
<dt><code>ExpBan &#8211; Object evicted due to ban</code></p>
<dd>Logs the VXID when an object is banned.</p>
<dt><code>ExpKill &#8211; Object expiry event</code></p>
<dd>Logs events related to object expiry. The events are:</p>
<dt><code>EXP_Rearm</code></p>
<dd>Logged when the expiry time of an object changes.</p>
<dt><code>EXP_Inbox</code></p>
<dd>Logged when the expiry thread picks an object from the inbox for processing.</p>
<dt><code>EXP_Kill</code></p>
<dd>Logged when the expiry thread kills an object from the inbox.</p>
<dt><code>EXP_When</code></p>
<dd>Logged when the expiry thread moves an object on the binheap.</p>
<dt><code>EXP_Expired</code></p>
<dd>Logged when the expiry thread expires an object.</p>
<dt><code>LRU_Cand</code></p>
<dd>Logged when an object is evaluated for LRU force expiry.</p>
<dt><code>LRU</code></p>
<dd>Logged when an object is force expired due to LRU.</p>
<dt><code>LRU_Fail</code></p>
<dd>Logged when no suitable candidate object is found for LRU force expiry. </p>
<p> The format is: </p>
<pre>EXP_Rearm p=%p E=%f e=%f f=0x%x
EXP_Inbox p=%p e=%f f=0x%x
EXP_Kill p=%p e=%f f=0x%x
EXP_When p=%p e=%f f=0x%x
EXP_Expired x=%u t=%f
LRU_Cand p=%p f=0x%x r=%d
LRU x=%u
LRU_Fail
Legend:
p=%p Objcore pointer
t=%f Remaining TTL (s)
e=%f Expiry time (unix epoch)
E=%f Old expiry time (unix epoch)
f=0x%x Objcore flags
r=%d Objcore refcount
x=%u Object VXID</pre>
<dt><code>FetchError &#8211; Error while fetching object</code></p>
<dd>Logs the error message of a failed fetch operation.</p>
<dt><code>Fetch_Body &#8211; Body fetched from backend</code></p>
<dd>Ready to fetch body from backend. </p>
<p> The format is: </p>
<pre>%d (%s) %s
| | |
| | +---- 'stream' or '-'
| +--------- Text description of body fetch mode
+------------- Body fetch mode</pre>
<dt><code>Gzip &#8211; G(un)zip performed on object</code></p>
<dd>A Gzip record is emitted for each instance of gzip or gunzip work performed. Worst case, an ESI transaction stored in gzip&#8217;ed objects but delivered gunziped, will run into many of these. </p>
<p> The format is: </p>
<pre>%c %c %c %d %d %d %d %d
| | | | | | | |
| | | | | | | +- Bit length of compressed data
| | | | | | +---- Bit location of 'last' bit
| | | | | +------- Bit location of first deflate block
| | | | +---------- Bytes output
| | | +------------- Bytes input
| | +---------------- 'E': ESI, '-': Plain object
| +------------------- 'F': Fetch, 'D': Deliver
+---------------------- 'G': Gzip, 'U': Gunzip, 'u': Gunzip-test</pre>
<p>Examples: </p>
<pre>U F E 182 159 80 80 1392
G F E 159 173 80 1304 1314</pre>
<dt><code>Hash &#8211; Value added to hash</code></p>
<dd>This value was added to the object lookup hash. </p>
<p> NB: This log record is masked by default.</p>
<dt><code>Hit &#8211; Hit object in cache</code></p>
<dd>Object looked up in cache. Shows the VXID of the object.</p>
<dt><code>HitPass &#8211; Hit for pass object in cache.</code></p>
<dd>Hit-for-pass object looked up in cache. Shows the VXID of the hit-for-pass object.</p>
<dt><code>HttpGarbage &#8211; Unparseable HTTP request</code></p>
<dd>Logs the content of unparseable HTTP requests.</p>
<dt><code>Length &#8211; Size of object body</code></p>
<dd>Logs the size of a fetch object body.</p>
<dt><code>Link &#8211; Links to a child VXID</code></p>
<dd>Links this VXID to any child VXID it initiates. </p>
<p> The format is: </p>
<pre>%s %d %s
| | |
| | +- Reason
| +---- Child vxid
+------- Child type (&quot;req&quot; or &quot;bereq&quot;)</pre>
<dt><code>LostHeader &#8211; Failed attempt to set HTTP header</code></p>
<dd>Logs the header name of a failed HTTP header operation due to resource exhaustion or configured limits.</p>
<dt><code>ObjHeader &#8211; Object header</code></p>
<dd>HTTP header contents. </p>
<p> The format is: </p>
<pre>%s: %s
| |
| +- Header value
+----- Header name</pre>
<dt><code>ObjProtocol &#8211; Object protocol</code></p>
<dd>The HTTP protocol version information.</p>
<dt><code>ObjReason &#8211; Object response</code></p>
<dd>The HTTP response string received.</p>
<dt><code>ObjStatus &#8211; Object status</code></p>
<dd>The HTTP status code received.</p>
<dt><code>PipeAcct &#8211; Pipe byte counts</code></p>
<dd>Contains byte counters for pipe sessions. </p>
<p> The format is: </p>
<pre>%d %d %d %d
| | | |
| | | +------- Piped bytes to client
| | +---------- Piped bytes from client
| +------------- Backend request headers
+---------------- Client request headers</pre>
<dt><code>ReqAcct &#8211; Request handling byte counts</code></p>
<dd>Contains byte counts for the request handling. This record is not logged for ESI sub-requests, but the sub-requests&#8217; response body count is added to the main request. </p>
<p> The format is: </p>
<pre>%d %d %d %d %d %d
| | | | | |
| | | | | +- Total bytes transmitted
| | | | +---- Body bytes transmitted
| | | +------- Header bytes transmitted
| | +---------- Total bytes received
| +------------- Body bytes received
+---------------- Header bytes received</pre>
<dt><code>ReqHeader &#8211; Client request header</code></p>
<dd>HTTP header contents. </p>
<p> The format is: </p>
<pre>%s: %s
| |
| +- Header value
+----- Header name</pre>
<dt><code>ReqMethod &#8211; Client request method</code></p>
<dd>The HTTP request method used.</p>
<dt><code>ReqProtocol &#8211; Client request protocol</code></p>
<dd>The HTTP protocol version information.</p>
<dt><code>ReqStart &#8211; Client request start</code></p>
<dd>Start of request processing. Logs the client IP address and port number. </p>
<p> The format is: </p>
<pre>%s %s
| |
| +- Port number
+---- IP address</pre>
<dt><code>ReqURL &#8211; Client request URL</code></p>
<dd>The HTTP request URL.</p>
<dt><code>RespHeader &#8211; Client response header</code></p>
<dd>HTTP header contents. </p>
<p> The format is: </p>
<pre>%s: %s
| |
| +- Header value
+----- Header name</pre>
<dt><code>RespProtocol &#8211; Client response protocol</code></p>
<dd>The HTTP protocol version information.</p>
<dt><code>RespReason &#8211; Client response response</code></p>
<dd>The HTTP response string received.</p>
<dt><code>RespStatus &#8211; Client response status</code></p>
<dd>The HTTP status code received.</p>
<dt><code>SessClose &#8211; Client connection closed</code></p>
<dd>SessionClose is the last record for any client connection. </p>
<p> The format is: </p>
<pre>%s %f
| |
| +- How long the session was open
+---- Why the connection closed</pre>
<dt><code>SessOpen &#8211; Client connection opened</code></p>
<dd>The first record for a client connection, with the socket-endpoints of the connection. </p>
<p> The format is: </p>
<pre>%s %d %s %s %s %d
| | | | | |
| | | | | +- File descriptor number
| | | | +---- Local TCP port ('-' if !$log_local_addr)
| | | +------- Local IPv4/6 address ('-' if !$log_local_addr)
| | +---------- Listen socket
| +------------- Client TCP socket
+---------------- Client IPv4/6 address</pre>
<dt><code>Storage &#8211; Where object is stored</code></p>
<dd>Type and name of the storage backend the object is stored in. </p>
<p> The format is: </p>
<pre>%s %s
| |
| +- Name of storage backend
+---- Type (&quot;malloc&quot;, &quot;file&quot;, &quot;persistent&quot; etc.)</pre>
<dt><code>TTL &#8211; TTL set on object</code></p>
<dd>A TTL record is emitted whenever the ttl, grace or keep values for an object is set. </p>
<p> The format is: </p>
<pre>%s %d %d %d %d [ %d %d %u %u ]
| | | | | | | | |
| | | | | | | | +- Max-Age from Cache-Control header
| | | | | | | +---- Expires header
| | | | | | +------- Date header
| | | | | +---------- Age (incl Age: header value)
| | | | +--------------- Reference time for TTL
| | | +------------------ Keep
| | +--------------------- Grace
| +------------------------ TTL
+--------------------------- &quot;RFC&quot; or &quot;VCL&quot;</pre>
<p>The last four fields are only present in &quot;RFC&quot; headers. </p>
<p> Examples: </p>
<pre>RFC 60 -1 -1 1312966109 1312966109 1312966109 0 60
VCL 120 10 0 1312966111</pre>
<dt><code>Timestamp &#8211; Timing information</code></p>
<dd>Contains timing information for the Varnish worker threads. </p>
<p> Time stamps are issued by Varnish on certain events, and show the absolute time of the event, the time spent since the start of the work unit, and the time spent since the last timestamp was logged. See <a href="/docs/linux/man/7-vsl/">vsl</a>(7) for information about the individual timestamps. </p>
<p> The format is: </p>
<pre>%s: %f %f %f
| | | |
| | | +- Time since last timestamp
| | +---- Time since start of work unit
| +------- Absolute time of event
+----------- Event label</pre>
<dt><code>VCL_Error &#8211; VCL execution error message</code></p>
<dd>Logs error messages generated during VCL execution.</p>
<dt><code>VCL_Log &#8211; Log statement from VCL</code></p>
<dd>User generated log messages insert from VCL through std.log()</p>
<dt><code>VCL_acl &#8211; VSL ACL check results</code></p>
<dd>Logs VCL ACL evaluation results.</p>
<dt><code>VCL_call &#8211; VCL method called</code></p>
<dd>Logs the VCL method name when a VCL method is called.</p>
<dt><code>VCL_return &#8211; VCL method return value</code></p>
<dd>Logs the VCL method terminating statement.</p>
<dt><code>VCL_trace &#8211; VCL trace data</code></p>
<dd>Logs VCL execution trace data. </p>
<p> The format is: </p>
<pre>%u %u.%u
| | |
| | +- VCL program line position
| +---- VCL program line number
+------- VCL trace point index</pre>
<p>NB: This log record is masked by default.</p>
<dt><code>VSL &#8211; VSL API warnings and error message</code></p>
<dd>Warnings and error messages genererated by the VSL API while reading the shared memory log.</p>
<dt><code>WorkThread &#8211; Logs thread start/stop events</code></p>
<dd>Logs worker thread creation and termination events. </p>
<p> The format is: </p>
<pre>%p %s
| |
| +- [start|end]
+---- Worker struct pointer</pre>
<p>NB: This log record is masked by default.</dl>
<h2>Timestamps</h2>
<p>Timestamps are inserted in the log on completing certain events during the worker thread&#8217;s task handling. The timestamps has a label showing which event was completed. The reported fields show the absolute time of the event, the time spent since the start of the task and the time spent since the last timestamp was logged. </p>
<p> The timestamps logged automatically by Varnish are inserted after completing events that are expected to have delays (e.g. network IO or spending time on a waitinglist). Timestamps can also be inserted from VCL using the std.timestamp() method. If one is doing time consuming tasks in the VCL configuration, it&#8217;s a good idea to log a timestamp after completing that task. This keeps the timing information in subsequent timestamps from including the time spent on the VCL event.</p>
<h3>Request handling timestamps</h3>
<dl>
<dt><code>Start</code></p>
<dd>The start of request processing (first byte received or restart).</p>
<dt><code>Req</code></p>
<dd>Complete client request received.</p>
<dt><code>ReqBody</code></p>
<dd>Client request body processed (discarded, cached or passed to the backend).</p>
<dt><code>Waitinglist</code></p>
<dd>Came off waitinglist.</p>
<dt><code>Fetch</code></p>
<dd>Fetch processing finished (completely fetched or ready for streaming).</p>
<dt><code>Process</code></p>
<dd>Processing finished, ready to deliver the client response.</p>
<dt><code>Resp</code></p>
<dd>Delivery of response to the client finished.</p>
<dt><code>Restart</code></p>
<dd>Client request is being restarted.</dl>
<h3>Pipe handling timestamps</h3>
<dl>
<dt><code>Pipe</code></p>
<dd>Opened a pipe to the backend and forwarded the request.</p>
<dt><code>PipeSess</code></p>
<dd>The pipe session has finished.</dl>
<h3>Backend fetch timestamps</h3>
<dl>
<dt><code>Start</code></p>
<dd>Start of the backend fetch processing.</p>
<dt><code>Bereq</code></p>
<dd>Backend request sent.</p>
<dt><code>Beresp</code></p>
<dd>Backend response headers received.</p>
<dt><code>BerespBody</code></p>
<dd>Backend response body received.</p>
<dt><code>Retry</code></p>
<dd>Backend request is being retried.</p>
<dt><code>Error</code></p>
<dd>Backend request failed to vcl_backend_error.</dl>
<h2>History</h2>
<p>This document was initially written by Poul-Henning Kamp, and later updated by Martin Blix Grydeland.</p>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-varnishlog/">varnishlog</a>(1)</p>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-varnishhist/">varnishhist</a>(1)</p>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-varnishncsa/">varnishncsa</a>(1)</p>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-varnishtop/">varnishtop</a>(1) </p>
