---
title: "dc_test(1)"
name: "dc_test"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dc_test/"
description: "dc_test – Distributed session cache testing and benchmarking tool"
---

<h2>NAME</h2>
<p> dc_test &#8211; Distributed session cache testing and benchmarking tool</p>
<h2>SYNOPSIS</h2>
<p> <code>dc_test</code> -connect &lt;addr&gt; [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>dc_test</code> runs a configurable number of session caching operations against a given network address using the <i><a href="/docs/linux/man/8-distcache/">distcache</a></i>(8) protocol. This is typically to verify an installation, to help diagnose problems, and to measure latency and/or throughput. The given address could be for an instance of <code>dc_client</code> or directly to a running instance of <code>dc_server</code>. Note that whenever the service is running over TCP/IPv4, use of the <code>-persistent</code> flag is advised because many systems will fairly quickly exhaust the limit of available file-descriptors and stop allowing new sockets until the closed connections finish with the <font SIZE="-1">TIME_WAIT</font> state. </p>
<p> <code>dc_test</code> runs one cache operation at a time, so it provides an accurate measurement of latency in the distcache architecture being tested. However if one wants to test the potential throughput of the architecture when multiple cache operations occur in parallel (and distcache tools are asynchronous to scale well in such circumstances), it makes sense to launch multiple instances of <code>dc_test</code> in parallel. </p>
<p> <code>dc_test</code> attempts to verify correctness of any optimisation caching tricks in distcache tools by creating an array of &#8220;sessions&#8221; in advance and then sending sending <font SIZE="-1">ADD</font>, <font SIZE="-1">GET</font>, and <font SIZE="-1">REMOVE</font> requests on these sessions chosen completely at random. As such, many of these requests <code>should</code> fail, and <code>dc_test</code> will itself immediately halt with an error if any operation that should succeed fails or any operation that should fail succeeds.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-connect</code> address</p>
<dd> This flag specifies the address <code>dc_test</code> should connect and send cache operation requests to.</p>
<dt><code>-progress</code> num</p>
<dd> Normally <code>dc_test</code> will remain silent while testing is in progress and will only produce output when complete (whether it is because an error was detected or because the required number of operations have completd). With this flag, a line of output is produced each time another <code>num</code> operations have been completed. This can be useful for giving an intuitive idea of the latency in the architecture and to verify that neither <code>dc_test</code> nor the tools it connects to have deadlocked. </p>
<p> The default value for this flag is 0, which leaves <code>dc_test</code> silent until it has completed.</p>
<dt><code>-sessions</code> num</p>
<dd> This flag controls the number of sample sessions created by <code>dc_test</code> before testing begins. The default value is 10.</p>
<dt><code>-datamin</code> num</p>
<dd>
<dt><code>-datamax</code> num</p>
<dd> The sessions created by <code>dc_test</code> during initialisation have random session IDs between 10 and 63 bytes in length, and random session data of varying length also. The minimum length of the session data is set by the <code>-datamin</code> switch, and the maximum length is set by the <code>-datamax</code> switch. The default value for <code>-datamin</code> is 50, and the default for <code>-datamax</code> is 2100.</p>
<dt><code>-timeout</code> secs</p>
<dd>
<dt><code>-timevar</code> secs</p>
<dd> The sessions created by <code>dc_test</code> during initialisation have random timeouts associated with them, so as to better probe for potential expiry-ordering bugs in a cache server. Each session addition to a cache server must specify an expiry period after which the cache will be automatically removed if it hasn&#8217;t already been removed explicitly or implicitly because of the <font SIZE="-1">FIFO</font> behaviour of a full cache. The <code>-timeout</code> switch specifies the average timeout for creating sessions with, and the <code>-timevar</code> switch specifies the range above or below the average that session timeouts should be (randomly) chosen from. </p>
<p> The default value for <code>-timeout</code> is 60 seconds, and the default value for <code>-timevar</code> is 5 seconds. </p>
<p> If <code>dc_server</code> is not running as a daemon, then it can also be useful to watch it&#8217;s behaviour after testing has finished (or in the middle of subsequent testing) because it should automatically scroll out test sessions as their expiry period runs out. See also the <i></i><font SIZE="-1"><i>BUGS</i></font><i></i> section.</p>
<dt><code>-ops</code> num</p>
<dd> <code>dc_test</code> does not (yet) support running indefinitely (see the <i></i><font SIZE="-1"><i>BUGS</i></font><i></i> section for the primary reason), so it will run until any error has been observed or until it has successfully performed a configurable number of operations. The <code>-ops</code> switch can be used to set this number of operations. </p>
<p> If <code>-ops</code> is not supplied on the command-line, it&#8217;s default value will be calculated from the number of sessions created (which is itself controlled by <code>-sessions</code>). This default is 10*(sessions^2). As the default number of sessions is 10, the default number of operations is thus 1000.</p>
<dt><code>-persistent</code></p>
<dd> The default behaviour of <code>dc_test</code> is to open and close a connection to the target address (controlled by <code>-connect</code>) for every operation. This is the logical choice when connecting to an instance of <code>dc_client</code> as it is the mode of operation employed by most applications that integrate with distcache. However, it can be desirable to measure the behaviour of the architecture when all operations are taking place over a single established &#8220;persistent&#8221; connection. This is more certainly the case when connecting directly to an instance of <code>dc_server</code> over TCP/IPv4, as <code>dc_server</code> forks a child process for each connection and TCP/IPv4 does not react well to thousands of connections being opened and closed in a short space of time. </p>
<p> Using the <code>-persistent</code> switch, a single connection will be opened to the target address when <code>dc_test</code> initialises, and all cache operations will use this connection.</p>
<dt><code>-h</code>, <code>-help</code>, <code>-?</code></p>
<dd> Any of these flags will cause <code>dc_test</code> to display a brief usage summary to the console and exit cleanly. Any other flags are ignored.</dl>
<h2>BUGS</h2>
<p> <code>dc_test</code> will monitor each of the sessions it creates during intialisation to determine whether it thinks it should already be present in the destination session cache or not. Using this state, it determines whether it expects a corresponding <font SIZE="-1">ADD</font>, <font SIZE="-1">GET</font>, or <font SIZE="-1">DELETE</font> operation on the session to succeed or fail. <font SIZE="-1">GET</font> and <font SIZE="-1">DELETE</font> should fail if the session is not supposed to be in the cache (if it has never been added or was last seen in a <font SIZE="-1">DELETE</font> operation). Likewise, <font SIZE="-1">ADD</font> should fail if the session is supposed to be in the cache. None of this logic, however, pays any attention to the expiry period in each of these sessions and so if a long enough test is run (high value of <code>ops</code> or a slow architecture) and/or short session timeouts are used, it becomes possible for this state to become incorrect when the cache itself expires sessions that <code>dc_test</code> thinks should still be in the cache. This bug should be hard to trigger even with long tests or short timeouts, because a session needs to be added to the cache and then not <font SIZE="-1">DELETE</font>&#8216;d during a long enough period that the server gets a chance to expire it.</p>
<h2>SEE ALSO</h2>
<dl>
<dt><i><a href="/docs/linux/man/1-dc_client/">dc_client</a></i>(1)</p>
<dd> Distributed caching client proxy.</p>
<dt><i><a href="/docs/linux/man/1-dc_server/">dc_server</a></i>(1)</p>
<dd> Distributed cache server.</p>
<dt><i><a href="/docs/linux/man/1-dc_snoop/">dc_snoop</a></i>(1)</p>
<dd> Distcache protocol analyser and debugging tool.</p>
<dt><i><a href="/docs/linux/man/8-distcache/">distcache</a></i>(8)</p>
<dd> Overview of the distcache architecture.</p>
<dt><i><a rel="nofollow" href="http://www.distcache.org/">http://www.distcache.org/</a></i></p>
<dd> Distcache home page.</dl>
<h2>AUTHOR</h2>
<p> This toolkit was designed and implemented by Geoff Thorpe for Cryptographic Appliances Incorporated. Since the project was released into open source, it has a home page and a project environment where development, mailing lists, and releases are organised. For problems with the software or this man page please check for new releases at the project web-site below, mail the users mailing list described there, or contact the author at <i>geoff [at] geoffthorpe.net</i>. </p>
<p> Home Page: <i><a rel="nofollow" href="http://www.distcache.org">http://www.distcache.org</a></i> </p>
<h2>Index</h2>
