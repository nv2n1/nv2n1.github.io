---
title: "vcl(7)"
name: "vcl"
section: "7"
letter: "v"
url: "/docs/linux/man/7-vcl/"
description: "VCL – Varnish Configuration Language"
---

<p>VCL &#8211; Varnish Configuration Language</p>
<h2>Description</h2>
<p>The VCL language is a small domain-specific language designed to be used to describe request handling and document caching policies for Varnish Cache. When a new configuration is loaded, the varnishd management process translates the VCL code to C and compiles it to a shared object which is then loaded into the server process. This document focuses on the syntax of the VCL language. For a full description of syntax and semantics, with ample examples, please see the online documentation at <i><a rel="nofollow" href="https://www.varnish-cache.org/docs/">https://www.varnish-cache.org/docs/</a></i> . Starting with Varnish 4.0, each VCL file must start by declaring its version with a special &quot;vcl 4.0;&quot; marker at the top of the file.</p>
<h3>Operators</h3>
<p>The following operators are available in VCL:</p>
<dl>
<dt><code>=</code></p>
<dd>Assignment operator.</p>
<dt><code>==</code></p>
<dd>Comparison.</p>
<dt><code>~</code></p>
<dd>Match. Can either be used with regular expressions or ACLs.</p>
<dt><code>!</code></p>
<dd>Negation.</p>
<dt><code>&amp;&amp;</code></p>
<dd>Logical and.</p>
<dt><code>||</code></p>
<dd>Logical or.</dl>
<h3>Conditionals</h3>
<p>VCL has <i>if</i> and <i>else</i> statements. Nested logic can be implemented with the <i>elseif</i> statement. (<i>elsif</i>/<i>elif</i>/<i>else if</i> is equivalent.) Note that are no loops or iterators of any kind in VCL.</p>
<h3>Strings, booleans, time, duration and integers</h3>
<p>These are the data types in Varnish. You can <i>set</i> or <i>unset</i> these. Example: </p>
<pre>set req.http.User-Agent = &quot;unknown&quot;;
unset req.http.Range;</pre>
<h3>Strings</h3>
<p>Basic strings are enclosed in double quotes (&quot; &#8230; &quot;), and may not contain newlines. Long strings are enclosed in {&quot; &#8230; &quot;}. They may contain any character including single double quotes (&quot;), newline and other control characters except for the NUL (0x00) character.</p>
<h3>Booleans</h3>
<p>Booleans can be either <i>true</i> or <i>false</i>.</p>
<h3>Time</h3>
<p>VCL has time. The function <i>now</i> returns a time. A duration can be added to a time to make another time. In string context they return a formatted string.</p>
<h3>Durations</h3>
<p>Durations are defined by a number and a designation. The number can be a real so 1.5w is allowed.</p>
<dl>
<dt><code>ms</code></p>
<dd>milliseconds</p>
<dt><code>s</code></p>
<dd>seconds</p>
<dt><code>m</code></p>
<dd>minutes</p>
<dt><code>h</code></p>
<dd>hours</p>
<dt><code>d</code></p>
<dd>days</p>
<dt><code>w</code></p>
<dd>weeks</p>
<dt><code>y</code></p>
<dd>years</dl>
<h3>Integers</h3>
<p>Certain fields are integers, used as expected. In string context they return a string.</p>
<h3>Real numbers</h3>
<p>VCL understands real numbers. As with integers, when used in a string context they will return a string.</p>
<h3>Regular Expressions</h3>
<p>Varnish uses Perl-compatible regular expressions (PCRE). For a complete description please see the <a href="/docs/linux/man/3-pcre/">pcre</a>(3) man page. To send flags to the PCRE engine, such as to do case insensitive matching, add the flag within parens following a question mark, like this: </p>
<pre># If host is NOT example dot com..
if (req.http.host !~ &quot;(?i)example.com$&quot;) {
 ...
}</pre>
<h3>Include statement</h3>
<p>To include a VCL file in another file use the include keyword: </p>
<pre>include &quot;foo.vcl&quot;;</pre>
<h3>Import statement</h3>
<p>The <i>import</i> statement is used to load Varnish Modules (VMODs.) Example: </p>
<pre>import std;
sub vcl_recv {
 std.log(&quot;foo&quot;);
}</pre>
<h3>Comments</h3>
<p>Single lines of VCL can be commented out using // or #. Multi-line blocks can be commented out with /* block /*. Example: </p>
<pre>sub vcl_recv {
 // Single line of out-commented VCL.
 # Another way of commenting out a single line.
 /*
 Multi-line block of commented-out VCL.
 */
}</pre>
<h3>Backend definition</h3>
<p>A backend declaration creates and initialises a named backend object. A declaration start with the keyword <i>backend</i> followed by the name of the backend. The actual declaration is in curly brackets, in a key/value fashion.: </p>
<pre><code>backend name {
    .attribute = &quot;value&quot;;
}</code></pre>
<p> The only mandatory attribute is <i>host</i>. The attributes will inherit their defaults from the global parameters. The following attributes are available:</p>
<dl>
<dt><code>host (mandatory)</code></p>
<dd>The host to be used. IP address or a hostname that resolves to a single IP address.</p>
<dt><code>port</code></p>
<dd>The port on the backend that Varnish should connect to.</p>
<dt><code>host_header</code></p>
<dd>A host header to add.</p>
<dt><code>connect_timeout</code></p>
<dd>Timeout for connections.</p>
<dt><code>first_byte_timeout</code></p>
<dd>Timeout for first byte.</p>
<dt><code>between_bytes_timeout</code></p>
<dd>Timeout between bytes.</p>
<dt><code>probe</code></p>
<dd>Attach a probe to the backend. See Probes.</p>
<dt><code>max_connections</code></p>
<dd>Maximum number of open connections towards this backend. If Varnish reaches the maximum Varnish it will start failing connections. Backends can be used with <i>directors</i>. Please see the <a href="/docs/linux/man/3-vmod_directors/">vmod_directors</a>(3) man page for more information.</dl>
<h3>Probes</h3>
<p>Probes will query the backend for status on a regular basis and mark the backend as down it they fail. A probe is defined as this:: probe name {<br />
    .attribute = &quot;value&quot;;<br />
} There are no mandatory options. These are the options you can set:</p>
<dl>
<dt><code>url</code></p>
<dd>The URL to query. Defaults to &quot;/&quot;.</p>
<dt><code>request</code></p>
<dd>Specify a full HTTP request using multiple strings. .request will have rn automatically inserted after every string. If specified,</p>
<dt><code>expected_response</code></p>
<dd>The expected HTTP response code. Defaults to 200.</p>
<dt><code>timeout</code></p>
<dd>The timeout for the probe. Default is 2s.</p>
<dt><code>interval</code></p>
<dd>How often the probe is run. Default is 5s.</p>
<dt><code>initial</code></p>
<dd>How many of the polls in .window are considered good when Varnish starts. Defaults to the value of threshold &#8211; 1. In this case, the backend starts as sick and requires one single poll to be considered healthy.</p>
<dt><code>window</code></p>
<dd>How many of the latest polls we examine to determine backend health. Defaults to 8.</p>
<dt><code>threshold</code></p>
<dd>How many of the polls in .window must have succeeded for us to consider the backend healthy. Defaults to 3.</dl>
<h3>Access Control List (ACL)</h3>
<p>An Access Control List (ACL) declaration creates and initialises a named access control list which can later be used to match client addresses: </p>
<pre>acl localnetwork {
 &quot;localhost&quot;; # myself
 &quot;192.0.2.0&quot;/24; # and everyone on the local network
 ! &quot;192.0.2.23&quot;; # except for the dial-in router
}</pre>
<p>If an ACL entry specifies a host name which Varnish is unable to resolve, it will match any address it is compared to. Consequently, if it is preceded by a negation mark, it will reject any address it is compared to, which may not be what you intended. If the entry is enclosed in parentheses, however, it will simply be ignored. To match an IP address against an ACL, simply use the match operator: if (client.ip ~localnetwork) {<br />
    return (pipe);<br />
}</p>
<p>VCL objects A VCL object can be made with the <i>new</i> keyword. Example: </p>
<pre>sub vcl_init {
 new b = directors.round_robin()
 b.add_backend(node1);
}</pre>
<h3>Subroutines</h3>
<p>A subroutine is used to group code for legibility or reusability: </p>
<pre><code>sub pipe_if_local
{
    if (client.ip ~localnetwork) {
        return (pipe);
    }
}</code></pre>
<p> Subroutines in VCL do not take arguments, nor do they return values. The built in subroutines all have names beginning with vcl_, which is reserved. To call a subroutine, use the call keyword followed by the subroutine&#8217;s name: </p>
<pre>sub vcl_recv {
 call pipe_if_local;
}</pre>
<h3>Return statements</h3>
<p>The ongoing vcl_* subroutine execution ends when a return(<i>action</i>) statement is made. The <i>action</i> specifies how execution should proceed. The context defines which actions are available.</p>
<h3>Multiple subroutines</h3>
<p>If multiple subroutines with the name of one of the built-in ones are defined, they are concatenated in the order in which they appear in the source. The built-in VCL distributed with Varnish will be implicitly concatenated when the VCL is compiled.</p>
<h3>Variables</h3>
<p>In VCL you have access to certain variable objects. These contain requests and responses currently being worked on. What variables are available depends on context.</p>
<h3>bereq</h3>
<p>bereq Type: HTTP Readable from: backend The entire backend request HTTP data structure bereq.backend Type: BACKEND Readable from: vcl_pipe, backend Writable from: vcl_pipe, backend bereq.between_bytes_timeout Type: DURATION Readable from: backend Writable from: backend The time in seconds to wait between each received byte from the backend. Not available in pipe mode. bereq.connect_timeout Type: DURATION Readable from: vcl_pipe, backend Writable from: vcl_pipe, backend The time in seconds to wait for a backend connection. bereq.first_byte_timeout Type: DURATION Readable from: backend Writable from: backend The time in seconds to wait for the first byte from the backend. Not available in pipe mode. bereq.http. Type: HEADER Readable from: vcl_pipe, backend Writable from: vcl_pipe, backend The corresponding HTTP header. bereq.method Type: STRING Readable from: vcl_pipe, backend Writable from: vcl_pipe, backend The request type (e.g. &quot;GET&quot;, &quot;HEAD&quot;). bereq.proto Type: STRING Readable from: vcl_pipe, backend Writable from: vcl_pipe, backend The HTTP protocol version used to talk to the server. bereq.retries Type: INT Readable from: backend A count of how many times this request has been retried. bereq.uncacheable Type: BOOL Readable from: backend Indicates whether this request is uncacheable due to a pass in the client side or a hit on an existing uncacheable object (aka hit-for-pass). bereq.url Type: STRING Readable from: vcl_pipe, backend Writable from: vcl_pipe, backend The requested URL. bereq.xid Type: STRING Readable from: backend Unique ID of this request.</p>
<h3>beresp</h3>
<p>beresp Type: HTTP Readable from: vcl_backend_response, vcl_backend_error The entire backend response HTTP data structure beresp.backend.ip Type: IP Readable from: vcl_backend_response, vcl_backend_error IP of the backend this response was fetched from. beresp.backend.name Type: STRING Readable from: vcl_backend_response, vcl_backend_error Name of the backend this response was fetched from. beresp.do_esi Type: BOOL Readable from: vcl_backend_response, vcl_backend_error Writable from: vcl_backend_response, vcl_backend_error Boolean. ESI-process the object after fetching it. Defaults to false. Set it to true to parse the object for ESI directives. Will only be honored if req.esi is true. beresp.do_gunzip Type: BOOL Readable from: vcl_backend_response, vcl_backend_error Writable from: vcl_backend_response, vcl_backend_error Boolean. Unzip the object before storing it in the cache. Defaults to false. beresp.do_gzip Type: BOOL Readable from: vcl_backend_response, vcl_backend_error Writable from: vcl_backend_response, vcl_backend_error Boolean. Gzip the object before storing it. Defaults to false. When http_gzip_support is on Varnish will request already compressed content from the backend and as such compression in Varnish is not needed. beresp.do_stream Type: BOOL Readable from: vcl_backend_response, vcl_backend_error Writable from: vcl_backend_response, vcl_backend_error Deliver the object to the client directly without fetching the whole object into varnish. If this request is pass&#8217;ed it will not be stored in memory. beresp.grace Type: DURATION Readable from: vcl_backend_response, vcl_backend_error Writable from: vcl_backend_response, vcl_backend_error Set to a period to enable grace. beresp.http. Type: HEADER Readable from: vcl_backend_response, vcl_backend_error Writable from: vcl_backend_response, vcl_backend_error The corresponding HTTP header. beresp.keep Type: DURATION Readable from: vcl_backend_response, vcl_backend_error Writable from: vcl_backend_response, vcl_backend_error Set to a period to enable conditional backend requests. The keep time is cache lifetime in addition to the ttl. Objects with ttl expired but with keep time left may be used to issue conditional (If-Modified-Since / If-None-Match) requests to the backend to refresh them. beresp.proto Type: STRING Readable from: vcl_backend_response, vcl_backend_error Writable from: vcl_backend_response, vcl_backend_error The HTTP protocol version used the backend replied with. beresp.reason Type: STRING Readable from: vcl_backend_response, vcl_backend_error Writable from: vcl_backend_response, vcl_backend_error The HTTP status message returned by the server. beresp.status Type: INT Readable from: vcl_backend_response, vcl_backend_error Writable from: vcl_backend_response, vcl_backend_error The HTTP status code returned by the server. beresp.storage_hint Type: STRING Readable from: vcl_backend_response, vcl_backend_error Writable from: vcl_backend_response, vcl_backend_error Hint to Varnish that you want to save this object to a particular storage backend. beresp.ttl Type: DURATION Readable from: vcl_backend_response, vcl_backend_error Writable from: vcl_backend_response, vcl_backend_error The object&#8217;s remaining time to live, in seconds. beresp.ttl is writable. beresp.uncacheable Type: BOOL Readable from: vcl_backend_response, vcl_backend_error Writable from: vcl_backend_response, vcl_backend_error Inherited from bereq.uncacheable, see there. Setting this variable makes the object uncacheable, which may get stored as a hit-for-pass object in the cache. Clearing the variable has no effect and will log the warning &quot;Ignoring attempt to reset beresp.uncacheable&quot;.</p>
<h3>client</h3>
<p>client.identity Type: STRING Readable from: client Writable from: client Identification of the client, used to load balance in the client director. client.ip Type: IP Readable from: client The client&#8217;s IP address.</p>
<h3>now</h3>
<p>now Type: TIME Readable from: vcl_all The current time, in seconds since the epoch. When used in string context it returns a formatted string.</p>
<h3>obj</h3>
<p>obj.grace Type: DURATION Readable from: vcl_hit The object&#8217;s remaining grace period in seconds. obj.hits Type: INT Readable from: vcl_hit, vcl_deliver The count of cache-hits on this object. A value of 0 indicates a cache miss. obj.http. Type: HEADER Readable from: vcl_hit The corresponding HTTP header. obj.keep Type: DURATION Readable from: vcl_hit The object&#8217;s remaining keep period in seconds. obj.proto Type: STRING Readable from: vcl_hit The HTTP protocol version used when the object was retrieved. obj.reason Type: STRING Readable from: vcl_hit The HTTP status message returned by the server. obj.status Type: INT Readable from: vcl_hit The HTTP status code returned by the server. obj.ttl Type: DURATION Readable from: vcl_hit The object&#8217;s remaining time to live, in seconds. obj.uncacheable Type: BOOL Readable from: vcl_deliver Whether the object is uncacheable (pass or hit-for-pass).</p>
<h3>req</h3>
<p>req Type: HTTP Readable from: client The entire request HTTP data structure req.backend_hint Type: BACKEND Readable from: client Writable from: client Set bereq.backend to this if we attempt to fetch. req.can_gzip Type: BOOL Readable from: client Does the client accept the gzip transfer encoding. req.esi Type: BOOL Readable from: client Writable from: client Boolean. Set to false to disable ESI processing regardless of any value in beresp.do_esi. Defaults to true. This variable is subject to change in future versions, you should avoid using it. req.esi_level Type: INT Readable from: client A count of how many levels of ESI requests we&#8217;re currently at. req.hash_always_miss Type: BOOL Readable from: vcl_recv Writable from: vcl_recv Force a cache miss for this request. If set to true Varnish will disregard any existing objects and always (re)fetch from the backend. req.hash_ignore_busy Type: BOOL Readable from: vcl_recv Writable from: vcl_recv Ignore any busy object during cache lookup. You would want to do this if you have two server looking up content from each other to avoid potential deadlocks. req.http. Type: HEADER Readable from: client Writable from: client The corresponding HTTP header. req.method Type: STRING Readable from: client Writable from: client The request type (e.g. &quot;GET&quot;, &quot;HEAD&quot;). req.proto Type: STRING Readable from: client Writable from: client The HTTP protocol version used by the client. req.restarts Type: INT Readable from: client A count of how many times this request has been restarted. req.ttl Type: DURATION Readable from: client Writable from: client req.url Type: STRING Readable from: client Writable from: client The requested URL. req.xid Type: STRING Readable from: client Unique ID of this request.</p>
<h3>resp</h3>
<p>resp Type: HTTP Readable from: vcl_deliver, vcl_synth The entire response HTTP data structure resp.http. Type: HEADER Readable from: vcl_deliver, vcl_synth Writable from: vcl_deliver, vcl_synth The corresponding HTTP header. resp.proto Type: STRING Readable from: vcl_deliver, vcl_synth Writable from: vcl_deliver, vcl_synth The HTTP protocol version to use for the response. resp.reason Type: STRING Readable from: vcl_deliver, vcl_synth Writable from: vcl_deliver, vcl_synth The HTTP status message that will be returned. resp.status Type: INT Readable from: vcl_deliver, vcl_synth Writable from: vcl_deliver, vcl_synth The HTTP status code that will be returned.</p>
<h3>server</h3>
<p>server.hostname Type: STRING Readable from: vcl_all The host name of the server. server.identity Type: STRING Readable from: vcl_all The identity of the server, as set by the -i parameter. If the -i parameter is not passed to varnishd, server.identity will be set to the name of the instance, as specified by the -n parameter. server.ip Type: IP Readable from: client The IP address of the socket on which the client connection was received.</p>
<h3>storage</h3>
<p>storage.&lt;name&gt;.free_space Type: BYTES Readable from: client, backend Free space available in the named stevedore. Only available for the malloc stevedore. storage.&lt;name&gt;.used_space Type: BYTES Readable from: client, backend Used space in the named stevedore. Only available for the malloc stevedore. storage.&lt;name&gt;.happy Type: BOOL Readable from: client, backend Health status for the named stevedore. Not available in any of the current stevedores.</p>
<h3>Functions</h3>
<p>The following built-in functions are available:</p>
<dl>
<dt><code>ban(expression)</code></p>
<dd>Invalidates all objects in cache that match the expression with the ban mechanism.</p>
<dt><code>call(subroutine)</code></p>
<dd>Run a VCL subroutine within the current scope.</p>
<dt><code>hash_data(input)</code></p>
<dd>Adds an input to the hash input. In the built-in VCL hash_data() is called on the host and URL of the <i>request</i>. Available in vcl_hash.</p>
<dt><code>new()</code></p>
<dd>Instanciate a new VCL object. Available in vcl_init.</p>
<dt><code>return()</code></p>
<dd>End execution of the current VCL subroutine, and continue to the next step in the request handling state machine.</p>
<dt><code>rollback()</code></p>
<dd>Restore <i>req</i> HTTP headers to their original state. This function is deprecated. Use std.rollback() instead.</p>
<dt><code>synthetic(STRING)</code></p>
<dd>Prepare a synthetic response body containing the STRING. Available in vcl_synth and vcl_backend_error.</p>
<dt><code>regsub(str, regex, sub)</code></p>
<dd>Returns a copy of str with the first occurrence of the regular expression regex replaced with sub. Within sub, 
