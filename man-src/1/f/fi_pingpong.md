---
title: "fi_pingpong(1)"
name: "fi_pingpong"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fi_pingpong/"
---

<h2 class="name">NAME</h2>
 

 

 fi_pingpong - Quick and simple pingpong test for libfabric 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
&amp;nbsp;
fi_pingpong &amp;nbsp;
[OPTIONS] &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
start server
    &amp;nbsp;
fi_pingpong &amp;nbsp;
[OPTIONS] &amp; nbsp;
&lt;server address&gt; &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
connect to server
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 fi_pingpong is a pingpong test for the core feature of the libfabric library: transmitting data between two processes. fi_pingpong also displays aggregated statistics after each test run, and can additionally verify data integrity upon receipt. 

 By default, the datagram (FI_EP_DGRAM) endpoint is used for the test, unless otherwise specified via -e.

<h2>HOW TO RUN TESTS</h2>

 

 Two copies of the program must be launched: first, one copy must be launched as the server. Second, another copy is launched with the address of the server. 

 As a client-server test, each have the following usage model:

<h3>Start the server</h3>

<dl>
<dt>
<dd> <pre>
server$&nbsp;fi_pingpong
</pre></dl>

<h3>Start the client</h3>

<dl>
<dt>
<dd> <pre>
client$&nbsp;fi_pingpong&nbsp;&lt;server address&gt;
</pre></dl>

<h2>OPTIONS</h2>

 

 The server and client must be able to communicate properly for the fi_pingpong utility to function. If any of the -e, -I, -S, or -p options are used, then they must be specified on the invocation for both the server and the client process. If the -d option is specified on the server, then the client will select the appropriate domain if no hint is provided on the client side. If the -d option is specified on the client, then it must also be specified on the server. If both the server and client specify the -d option and the given domains cannot communicate, then the application will fail.

<h3>Control Messaging</h3>

 

 -B &lt;src_port&gt; : The non-default source port number of the control socket. If this is not provided then the server will bind to port 47592 by default and the client will allow the port to be selected automatically. 

 -P &lt;dest_port&gt; : The non-default destination port number of the control socket. If this is not provided then the client will connect to 47592 by default. The server ignores this option.

<h3>Fabric Filtering</h3>

 

 -p &lt;provider_name&gt; : The name of the underlying fabric provider (e.g., sockets, psm, usnic, etc.). If a provider is not specified via the -p switch, the test will pick one from the list of available providers (as returned by <a HREF="/docs/linux/man/3-fi_getinfo/">fi_getinfo</a>(3)). 

 -e &lt;endpoint&gt; : The type of endpoint to be used for data messaging between the two processes. Supported values are dgram, rdm, and msg. For more information on endpoint types, see <a HREF="/docs/linux/man/3-fi_endpoint/">fi_endpoint</a>(3). 

 -d &lt;domain&gt; : The name of the specific domain to be used.

<h3>Test Options</h3>

 

 -I &lt;iter&gt; : The number of iterations of the test will run. 

 -S &lt;msg_size&gt; : The specific size of the message in bytes the test will use or 'all' to run all the default sizes. 

 -c : Activate data integrity checks at the receiver (note: this will degrade performance).

<h3>Utility</h3>

 

 -v : Activate output debugging (warning: highly verbose) 

 -h : Displays help output for the pingpong test.

<h2>USAGE EXAMPLES</h2>

<h3>A simple example</h3>

<h3>Server: fi_pingpong -p&nbsp;&lt;provider_name&gt;</h3>

 

 server$&nbsp;fi_pingpong -p sockets

<h3>Client: fi_pingpong -p&nbsp;&lt;provider_name&gt;&nbsp;&lt;server_addr&gt;</h3>

 

 client$&nbsp;fi_pingpong -p sockets 192.168.0.123

<h3>An example with various options</h3>

<h3>Server:</h3>

 

 server$&nbsp;fi_pingpong -p usnic -I 1000 -S 1024

<h3>Client:</h3>

 

 client$&nbsp;fi_pingpong -p usnic -I 1000 -S 1024 192.168.0.123 

 Specifically, this will run a pingpong test with:
<dl>
<dt>&bull;
<dd> usNIC provider
<dt>&bull;
<dd> 1000 iterations
<dt>&bull;
<dd> 1024 bytes message size
<dt>&bull;
<dd> server node as 192.168.0.123</dl>

<h3>A longer test</h3>

<h3>Server:</h3>

 

 server$&nbsp;fi_pingpong -p usnic -I 10000 -S all

<h3>Client:</h3>

 

 client$&nbsp;fi_pingpong -p usnic -I 10000 -S all 192.168.0.123

<h2>DEFAULTS</h2>

 

 There is no default provider; if a provider is not specified via the -p switch, the test will pick one from the list of available providers (as returned by <a HREF="/docs/linux/man/3-fi_getinfo/">fi_getinfo</a>(3)). 

 If no endpoint type is specified, 'dgram' is used. 

 The default tested sizes are: 64, 256, 1024, 4096, 65536, and 1048576. The test will only test sizes that are within the selected endpoints maximum message size boundary.

<h2>OUTPUT</h2>

 

 Each test generates data messages which are accounted for. Specifically, the displayed statistics at the end are :
<dl>
<dt>&bull;
<dd> bytes : number of bytes per message sent
<dt>&bull;
<dd> #sent : number of messages (ping) sent from the client to the server
<dt>&bull;
<dd> #ack : number of replies (pong) of the server received by the client
<dt>&bull;
<dd> total : amount of memory exchanged between the processes
<dt>&bull;
<dd> time : duration of this single test
<dt>&bull;
<dd> MB/sec : throughput computed from total and time
<dt>&bull;
<dd> usec/xfer : average time for transferring a message outbound (ping or pong) in microseconds
<dt>&bull;
<dd> Mxfers/sec : average amount of transfers of message outbound per second</dl>

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-fi_getinfo/">fi_getinfo</a>(3), <a HREF="/docs/linux/man/3-fi_endpoint/">fi_endpoint</a>(3) <a HREF="/docs/linux/man/7-fabric/">fabric</a>(7),

<h2>AUTHORS</h2>

 OpenFabrics. 

<h2>Index</h2>


