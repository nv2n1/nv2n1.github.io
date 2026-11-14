---
title: "xmlrpc(3)"
name: "xmlrpc"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlrpc/"
---

<h2>Module</h2>
<p>xmlrpc &#8211; XML-RPC library</p>
<h2>Description</h2>
<p>This is an HTTP 1.1 compliant XML-RPC Erlang library. It is designed to make it easy to write XML-RPC Erlang clients and/or servers. The library is compliant with the XML-RPC specification published by <i><a rel="nofollow" href="http://www.xmlrpc.org/">http://www.xmlrpc.org/</a></i>.</p>
<h2>Exports</h2>
<p><code>call(</code><i>Socket</i><code>, </code><i>URI</i><code>, </code><i>Payload</i><code>)</code><br />
 <code>call(</code><i>Host</i><code>, </code><i>Port</i><code>, </code><i>URI</i><code>, </code><i>Payload</i><code>)</code><br />
 <code>call(</code><i>Socket</i><code>, </code><i>URI</i><code>, </code><i>Payload</i><code>, </code><i>KeepAlive</i><code>, </code><i>Timeout</i><code>)</code><br />
 <code>call(</code><i>Host</i><code>, </code><i>Port</i><code>, </code><i>URI</i><code>, </code><i>Payload</i><code>, </code><i>KeepAlive</i><code>, </code><i>Timeout</i><code>) -&gt; </code><i>Result</i></p>
<dl>
<dd>
<dl>
<dt>Types</p>
<dd>Socket = socket()<br />
 URI = string()<br />
 Payload = {call, Method, [Value]}<br />
 Method = atom()<br />
 Value = integer() | float() | string() | Boolean | ISO8601Date | Base64 | Struct | Array<br />
 Boolean = true | false<br />
 ISO8601Date = {date, string()}<br />
 Base64 = {base64, string()}<br />
 Struct = {struct, [{Key, Value}]}<br />
 Key = atom()<br />
 Array = {array, [Value]}<br />
 Host = string() | ip()<br />
 Port = integer()<br />
 KeepAlive = true | false<br />
 Timeout = integer()<br />
 ResponsePayload = {response, [Value]} | {response, Fault}<br />
 Fault = {fault, FaultCode, FaultString}<br />
 FaultCode = integer()<br />
 FaultString = string()<br />
 Result = {ok, ResponsePayload} | {error, Reason} | {ok, Socket, ResponsePayload} | {error, Socket, Reason}<br />
 Reason = term()</dl>
<p> Calls an XML-RPC server listening on <i>Host</i>:<i>Port</i>. The <i>URI</i> and <i>Payload</i> is used in the HTTP POST request being sent to the server. The <i>Value</i> is converted to XML (see <code>DATA TYPES</code> below) and is used as request body. </p>
<p> If <i>KeepAlive</i> is <code>true</code> a <i>Socket</i> is returned. The socket can be used to send several calls on the same connection in accordance with HTTP 1.1. If no server response is received within <i>Timeout</i> milli-seconds <code>{error, timeout}</code> or <code>{error, </code><i>Socket</i><code>, timeout}</code> is returned. </p>
<p> <i>KeepAlive</i> and <i>Timeout</i> default to <code>false</code> and 60000 milli-seconds. </p>
<p> See <code>EXAMPLES</code> section below.</dl>
<p> <code>start_link(</code><i>Handler</i><code>)</code><br />
 <code>start_link(</code><i>Port</i><code>, </code><i>MaxSessions</i><code>, </code><i>Timeout</i><code>, </code><i>Handler</i><code>, </code><i>State</i><code>)</code><br />
 <code>start_link(</code><i>IP</i><code>, </code><i>Port</i><code>, </code><i>MaxSessions</i><code>, </code><i>Timeout</i><code>, </code><i>Handler</i><code>, </code><i>State</i><code>) -&gt; </code><i>Result</i></p>
<dl>
<dd>
<dl>
<dt>Types</p>
<dd>Handler = {Module, Function}<br />
 Module = Function = atom()<br />
 Port = MaxSessions = integer()<br />
 Timeout = integer()<br />
 State = term()<br />
 IP = ip()<br />
 Result = {ok, Pid} | {error, Reason}<br />
 Pid = pid()<br />
 Reason = term()</dl>
<p> Starts an XML-RPC server listening on <i>IP</i>:<i>Port</i>. If no <i>IP</i> address is given the server listens on <i>Port</i> for all available <i>IP</i> addresses. <i>MaxSessions</i> is used to restrict the number of concurrent connections. If <i>MaxSessions</i> is reached the server accepts no new connections for 5 seconds, i.e. blocking new connect attempts. </p>
<p> <i>Handler</i> is a callback, implemented by <i>Module</i>:<i>Function</i>/2, which is used to instantiate an XML-RPC server. The <i>Timeout</i> value is used if the handler is keepalive oriented. <i>State</i> is the initial state given to <i>Module</i>:<i>Function</i>/2. The resulting <i>Pid</i> can be used as input to <code>xmlrpc:stop/1</code>. </p>
<p> See <code>Module:Function/2</code> and <code>EXAMPLES</code> below.</dl>
<p> <code>stop(</code><i>Pid</i><code>) -&gt; </code><i>Result</i></p>
<dl>
<dd>
<dl>
<dt>Types</p>
<dd>Pid = pid()<br />
 Result = void()</dl>
<p> Stops a running XML-RPC server.</dl>
<p> <i>Module</i><code>:</code><i>Function</i><code>(</code><i>State</i><code>, </code><i>Payload</i><code>) -&gt; </code><i>Result</i></p>
<dl>
<dd>
<dl>
<dt>Types</p>
<dd>State = term()<br />
 Payload = &lt;See above&gt;<br />
 Result = {KeepAlive, ResponsePayload} | {KeepAlive, State, Timeout, ResponsePayload}<br />
 KeepAlive = true | false<br />
 ResponsePayload = &lt;See above&gt;<br />
 Timeout = integer()</dl>
<p> It is up to you to implement <i>Function</i> clauses in <i>Module</i> to instantiate an XML-RPC server. Every time an XML-RPC call arrives the <i>Value</i> in the <i>Payload</i> gets converted to Erlang format and is passed on to <i>Module</i>:<i>Function</i>/2. </p>
<p> A <i>Function</i> clause is supposed to return either a 2-tuple or a 4-tuple. <i>KeepAlive</i> <code>must</code> be <code>false</code> in a 2-tuple and <code>true</code> in a 4-tuple. <i>KeepAlive</i> decides if the connection to the client should be kept open or not, i.e. compare with the <i>KeepAlive</i> argument to <code>call/{3,4,5,6}</code> above. </p>
<p> <i>State</i> can be used as a state variable by the callback function and changes made to it is propagated to the next call to <i>Module</i>:<i>Function</i>/2. The state variable is only meaningful if both the client and the server is keepalive oriented. The <i>Timeout</i> specified in <code>start_link/{1,5,6}</code> can be updated in the returning 4-tuple. </p>
<p> If <i>KeepAlive</i> is <code>true</code> and no call arrives within <i>Timeout</i> milli-seconds the socket is closed. The socket may be closed by the client before the specified timeout. </p>
<p> See <code>EXAMPLES</code> below.</dl>
<h2>Data Types</h2>
<p>The conversion of <i>Value</i> in <i>Payload</i> and <i>ResponsePayload</i> (see above) is done as follows: </p>
<pre>XML-RPC data type Erlang data type
----------------- ----------------
&lt;int&gt; integer()
&lt;boolean&gt; true or false
&lt;string&gt; string()
&lt;double&gt; float()
&lt;dateTime.iso8601&gt; {date, string()}
&lt;struct&gt; {struct, [{Key, Value}]}
&lt;array&gt; {array, [Value]}
&lt;base64&gt; {base64, string()}</pre>
<p>Read more about the XML-RPC data types in the XML-RPC specification published by <i><a rel="nofollow" href="http://www.xmlrpc.org/">http://www.xmlrpc.org/</a></i>. </p>
<p> Here are some examples on how Erlang format is converted to XML:</p>
<dl>
<dt><code>42</code></p>
<dd>&lt;int&gt;42&lt;/int&gt;</p>
<dt><code>true</code></p>
<dd>&lt;boolean&gt;true&lt;/boolean&gt;</p>
<dt><code>&quot;Kilroy was here&quot;</code></p>
<dd>&lt;string&gt;Kilroy was here&lt;/string&gt;</p>
<dt><code>42.5</code></p>
<dd>&lt;double&gt;42.5&lt;/double&gt;</p>
<dt><code>{date, &quot;19980717T14:08:55&quot;} </code></p>
<dd>&lt;dateTime.iso8601&gt;19980717T14:08:55&lt;/dateTime.iso8601&gt;</p>
<dt><code>{struct, [{foo, 42}, {bar, 4711}]}</code></p>
<dd>
<pre>&lt;struct&gt;
 &lt;member&gt;
 &lt;name&gt;foo&lt;/name&gt;&lt;value&gt;&lt;int&gt;42&lt;/int&gt;&lt;/value&gt;
 &lt;/member&gt;
 &lt;member&gt;
 &lt;name&gt;bar&lt;/name&gt;&lt;value&gt;&lt;int&gt;4711&lt;/int&gt;&lt;/value&gt;
 &lt;/member&gt;
&lt;/struct&gt;</pre>
<dt><code>{array, [42, 42.5}</code></p>
<dd>
<pre>&lt;array&gt;
 &lt;data&gt;
 &lt;value&gt;&lt;int&gt;42&lt;/i4&gt;&lt;/value&gt;
 &lt;value&gt;&lt;double&gt;42.5&lt;/double&gt;&lt;/value&gt;
 &lt;/data&gt;
&lt;/array&gt;</pre>
<dt><code>{date, &quot;19980717T14:08:55&quot;}</code></p>
<dd>&lt;dateTime.iso8601&gt;19980717T14:08:55&lt;/dateTime.iso8601&gt;</dl>
<h2>Examples</h2>
<p>You are strongly advised to inspect the example code in the <i>examples/</i> directory. The first example (<i>fib_server.erl</i>) calculates Fibonacci values and is a non-keepalive server. The second example (<i>echo_server.erl</i>) echoes back any incoming parameters and is a non-keepalive server. The third example (<i>date_server.erl</i>) calculates calendar values for given dates and is a keepalive server which uses the state variable to provide login state and different timeout settings. The fourth example (<i>validator.erl</i>) is a validation server which can be used to validate the library using the <i><a rel="nofollow" href="http://validator.xmlrpc.org/">http://validator.xmlrpc.org/</a></i> service. A snippet from the Fibonacci callback module in the <i>examples/</i> directory: </p>
<pre>handler(_State, {call, fib, [N]}) when integer(N) -&gt;
 {false, {response, [fib(N)]}};
handler(_State, Payload) -&gt;
 FaultString = lists:flatten(io_lib:format(&quot;Unknown call: ~p&quot;, [Payload])),
 {false, {response, {fault, -1, FaultString}}}.
fib(0) -&gt; 1;
<a href="//www.systutorials.com/docs/linux/man/1-fib/">fib</a>(1) -&gt; 1;
fib(N) -&gt; fib(N-1)+fib(N-2).</pre>
<p>and how it can be called: </p>
<pre>1&gt; xmlrpc:call({127, 0, 0, 1}, 4567, &quot;/&quot;, {call, fib, [0]}). 
{ok,{response,[1]}}
2&gt; xmlrpc:call({127, 0, 0, 1}, 4567, &quot;/&quot;, {call, fib, [4]}).
{ok,{response,[5]}}</pre>
<p>Again: You are strongly advised to inspect the example code in the <i>examples/</i> directory. </p>
<h2>Files</h2>
<dl>
<dt><i><a rel="nofollow" href="http://www.xmlrpc.org/">http://www.xmlrpc.org/</a></i></p>
<dd>Home for the XML-RPC specification.</p>
<dt><i>README</i></p>
<dd>Main README file for the library.</p>
<dt><i>examples/</i></p>
<dd>Example code</dl>
<h2>Author</h2>
<p>Joakim Grebeno &#8211; jocke [at] gleipnir.com</p>
