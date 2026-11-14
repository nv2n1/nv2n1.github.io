---
title: "resperf(1)"
name: "resperf"
section: "1"
letter: "r"
url: "/docs/linux/man/1-resperf/"
description: "resperf – test the resolution performance of a caching DNS server"
---

<h2>NAME</h2>
<p> resperf &#8211; test the resolution performance of a caching DNS server</p>
<h2>SYNOPSIS</h2>
<p> <code>resperf-report</code>&nbsp;<wbr>[<code>-a&nbsp;<wbr></code><i>local_addr</i>] [<code>-d&nbsp;<wbr></code><i>datafile</i>] [<code>-s&nbsp;<wbr></code><i>server_addr</i>] [<code>-p&nbsp;<wbr></code><i>port</i>] [<code>-x&nbsp;<wbr></code><i>local_port</i>] [<code>-t&nbsp;<wbr></code><i>timeout</i>] [<code>-b&nbsp;<wbr></code><i>bufsize</i>] [<code>-f&nbsp;<wbr></code><i>family</i>] [<code>-e</code>] [<code>-D</code>] [<code>-y&nbsp;<wbr></code><i>[alg:]name:secret</i>] [<code>-h</code>] [<code>-i&nbsp;<wbr></code><i>interval</i>] [<code>-m&nbsp;<wbr></code><i>max_qps</i>] [<code>-r&nbsp;<wbr></code><i>rampup_time</i>] [<code>-c&nbsp;<wbr></code><i>constant_traffic_time</i>] [<code>-L&nbsp;<wbr></code><i>max_loss</i>] [<code>-C&nbsp;<wbr></code><i>clients</i>] [<code>-q&nbsp;<wbr></code><i>max_outstanding</i>] </p>
<p> <code>resperf</code>&nbsp;<wbr>[<code>-a&nbsp;<wbr></code><i>local_addr</i>] [<code>-d&nbsp;<wbr></code><i>datafile</i>] [<code>-s&nbsp;<wbr></code><i>server_addr</i>] [<code>-p&nbsp;<wbr></code><i>port</i>] [<code>-x&nbsp;<wbr></code><i>local_port</i>] [<code>-t&nbsp;<wbr></code><i>timeout</i>] [<code>-b&nbsp;<wbr></code><i>bufsize</i>] [<code>-f&nbsp;<wbr></code><i>family</i>] [<code>-e</code>] [<code>-D</code>] [<code>-y&nbsp;<wbr></code><i>[alg:]name:secret</i>] [<code>-h</code>] [<code>-i&nbsp;<wbr></code><i>interval</i>] [<code>-m&nbsp;<wbr></code><i>max_qps</i>] [<code>-P&nbsp;<wbr></code><i>plot_data_file</i>] [<code>-r&nbsp;<wbr></code><i>rampup_time</i>] [<code>-c&nbsp;<wbr></code><i>constant_traffic_time</i>] [<code>-L&nbsp;<wbr></code><i>max_loss</i>] [<code>-C&nbsp;<wbr></code><i>clients</i>] [<code>-q&nbsp;<wbr></code><i>max_outstanding</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>resperf</code> is a companion tool to <code>dnsperf</code>. <code>dnsperf</code> was primarily designed for benchmarking authoritative servers, and it does not work well with caching servers that are talking to the live Internet. One reason for this is that dnsperf uses a &quot;self-pacing&quot; approach, which is based on the assumption that you can keep the server 100% busy simply by sending it a small burst of back-to-back queries to fill up network buffers, and then send a new query whenever you get a response back. This approach works well for authoritative servers that process queries in order and one at a time; it also works pretty well for a caching server in a closed laboratory environment talking to a simulated Internet that&#8217;s all on the same LAN. Unfortunately, it does not work well with a caching server talking to the actual Internet, which may need to work on thousands of queries in parallel to achieve its maximum throughput. There have been numerous attempts to use dnsperf (or its predecessor, queryperf) for benchmarking live caching servers, usually with poor results. Therefore, a separate tool designed specifically for caching servers is needed.</p>
<h3>How resperf works</h3>
<p> Unlike the &quot;self-pacing&quot; approach of dnsperf, resperf works by sending DNS queries at a controlled, steadily increasing rate. By default, resperf will send traffic for 60 seconds, linearly increasing the amount of traffic from zero to 100,000 queries per second. </p>
<p> During the test, resperf listens for responses from the server and keeps track of response rates, failure rates, and latencies. It will also continue listening for responses for an additional 40 seconds after it has stopped sending traffic, so that there is time for the server to respond to the last queries sent. This time period was chosen to be longer than the overall query timeout of both Nominum Vantio and current versions of BIND. </p>
<p> If the test is successful, the query rate will at some point exceed the capacity of the server and queries will be dropped, causing the response rate to stop growing or even decrease as the query rate increases. </p>
<p> The result of the test is a set of measurements of the query rate, response rate, failure response rate, and average query latency as functions of time.</p>
<h3>What you will need</h3>
<p> Benchmarking a live caching server is serious business. A fast caching server like Nominum Vantio running on a XEON server, resolving a mix of cacheable and non-cacheable queries typical of ISP customer traffic, is capable of resolving over 100,000 queries per second. In the process, it will send more than 40,000 queries per second to authoritative servers on the Internet, and receive responses to most of them. Assuming an average request size of 50 bytes and a response size of 150 bytes, this amounts to some 16 Mbps of outgoing and 48 Mbps of incoming traffic. If your Internet connection can&#8217;t handle the bandwidth, you will end up measuring the speed of the connection, not the server, and may saturate the connection causing a degradation in service for other users. </p>
<p> Make sure there is no stateful firewall between the server and the Internet, because most of them can&#8217;t handle the amount of UDP traffic the test will generate and will end up dropping packets, skewing the test results. Some will even lock up or crash. </p>
<p> You should run resperf on a machine separate from the server under test, on the same LAN. Preferably, this should be a Gigabit Ethernet network. The machine running resperf should be at least as fast as the machine being tested; otherwise, it may end up being the bottleneck. </p>
<p> There should be no other applications running on the machine running resperf. Performance testing at the traffic levels involved is essentially a hard real-time application &#8211; consider the fact that at a query rate of 100,000 queries per second, if resperf gets delayed by just 1/100 of a second, 1000 incoming UDP packets will arrive in the meantime. This is more than most operating systems will buffer, which means packets will be dropped. </p>
<p> Because the granularity of the timers provided by operating systems is typically too coarse to accurately schedule packet transmissions at sub-millisecond intervals, resperf will busy-wait between packet transmissions, constantly polling for responses in the meantime. Therefore, it is normal for resperf to consume 100% CPU during the whole test run, even during periods where query rates are relatively low. </p>
<p> You will also need a set of test queries in the <code>dnsperf</code> file format. See the <code>dnsperf</code> man page for instructions on how to construct this query file. To make the test as realistic as possible, the queries should be derived from recorded production client DNS traffic, without removing duplicate queries or other filtering. With the default settings, resperf will use up to 3 million queries in each test run. </p>
<p> If the caching server to be tested has a configurable limit on the number of simultaneous resolutions, like the <code>max-recursive-clients</code> statement in Nominum Vantio or the <code>recursive-clients</code> option in BIND 9, you will probably have to increase it. As a starting point, we recommend a value of 10000 for Nominum Vantio and 100000 for BIND 9. Should the limit be reached, it will show up in the plots as an increase in the number of failure responses. </p>
<p> The server being tested should be restarted at the beginning of each test to make sure it is starting with an empty cache. If the cache already contains data from a previous test run that used the same set of queries, almost all queries will be answered from the cache, yielding inflated performance numbers. </p>
<p> To use the <code>resperf-report</code> script, you need to have <code>gnuplot</code> installed. Make sure your installed version of <code>gnuplot</code> supports the png terminal driver. If your <code>gnuplot</code> doesn&#8217;t support png but does support gif, you can change the line saying terminal=png in the <code>resperf-report</code> script to terminal=gif.</p>
<h3>Running the test</h3>
<p> Resperf is typically invoked via the <code>resperf-report</code> script, which will run <code>resperf</code> with its output redirected to a file and then automatically generate an illustrated report in HTML format. Command line arguments given to resperf-report will be passed on unchanged to resperf. </p>
<p> When running resperf-report, you will need to specify at least the server IP address and the query data file. A typical invocation will look like</p>
<dl>
<dt>
<dd>
<pre>
resperf-report -s 10.0.0.2 -d queryfile
</pre>
</dl>
<p> With default settings, the test run will take at most 100 seconds (60 seconds of ramping up traffic and then 40 seconds of waiting for responses), but in practice, the 60-second traffic phase will usually be cut short. To be precise, resperf can transition from the traffic-sending phase to the waiting-for-responses phase in three different ways:</p>
<dl>
<dt>&bull;</p>
<dd> Running for the full allotted time and successfully reaching the maximum query rate (by default, 60 seconds and 100,000 qps, respectively). Since this is a very high query rate, this will rarely happen (with today&#8217;s hardware); one of the other two conditions listed below will usually occur first.</p>
<dt>&bull;</p>
<dd> Exceeding 65,536 outstanding queries. This often happens as a result of (successfully) exceeding the capacity of the server being tested, causing the excess queries to be dropped. The limit of 65,536 queries comes from the number of possible values for the ID field in the DNS packet. Resperf needs to allocate a unique ID for each outstanding query, and is therefore unable to send further queries if the set of possible IDs is exhausted.</p>
<dt>&bull;</p>
<dd> When resperf finds itself unable to send queries fast enough. Resperf will notice if it is falling behind in its scheduled query transmissions, and if this backlog reaches 1000 queries, it will print a message like &quot;Fell behind by 1000 queries&quot; (or whatever the actual number is at the time) and stop sending traffic.</dl>
<p> Regardless of which of the above conditions caused the traffic-sending phase of the test to end, you should examine the resulting plots to make sure the server&#8217;s response rate is flattening out toward the end of the test. If it is not, then you are not loading the server enough. If you are getting the &quot;Fell behind&quot; message, make sure that the machine running resperf is fast enough and has no other applications running. </p>
<p> You should also monitor the CPU usage of the server under test. It should reach close to 100% CPU at the point of maximum traffic; if it does not, you most likely have a bottleneck in some other part of your test setup, for example, your external Internet connection. </p>
<p> The report generated by <code>resperf-report</code> will be stored with a unique file name based on the current date and time, e.g., <i>20060812-1550.html</i>. The PNG images of the plots and other auxiliary files will be stored in separate files beginning with the same date-time string. To view the report, simply open the <i>.html</i> file in a web browser. </p>
<p> If you need to copy the report to a separate machine for viewing, make sure to copy the .png files along with the .html file (or simply copy all the files, e.g., using scp 20060812-1550.* host:directory/).</p>
<h3>Interpreting the report</h3>
<p> The <i>.html</i> file produced by <code>resperf-report</code> consists of two sections. The first section, &quot;Resperf output&quot;, contains output from the <code>resperf</code> program such as progress messages, a summary of the command line arguments, and summary statistics. The second section, &quot;Plots&quot;, contains two plots generated by <code>gnuplot</code>: &quot;Query/response/failure rate&quot; and &quot;Latency&quot;. </p>
<p> The &quot;Query/response/failure rate&quot; plot contains three graphs. The &quot;Queries sent per second&quot; graph shows the amount of traffic being sent to the server; this should be very close to a straight diagonal line, reflecting the linear ramp-up of traffic. </p>
<p> The &quot;Total responses received per second&quot; graph shows how many of the queries received a response from the server. All responses are counted, whether successful (NOERROR or NXDOMAIN) or not (e.g., SERVFAIL). </p>
<p> The &quot;Failure responses received per second&quot; graph shows how many of the queries received a failure response. A response is considered to be a failure if its RCODE is neither NOERROR nor NXDOMAIN. </p>
<p> By visually inspecting the graphs, you can get an idea of how the server behaves under increasing load. The &quot;Total responses received per second&quot; graph will initially closely follow the &quot;Queries sent per second&quot; graph (often rendering it invisible in the plot as the two graphs are plotted on top of one another), but when the load exceeds the server&#8217;s capacity, the &quot;Total responses received per second&quot; graph may diverge from the &quot;Queries sent per second&quot; graph and flatten out, indicating that some of the queries are being dropped. </p>
<p> The &quot;Failure responses received per second&quot; graph will normally show a roughly linear ramp close to the bottom of the plot with some random fluctuation, since typical query traffic will contain some small percentage of failing queries randomly interspersed with the successful ones. As the total traffic increases, the number of failures will increase proportionally. </p>
<p> If the &quot;Failure responses received per second&quot; graph turns sharply upwards, this can be another indication that the load has exceeded the server&#8217;s capacity. This will happen if the server reacts to overload by sending SERVFAIL responses rather than by dropping queries. Since Nominum Vantio and BIND 9 will both respond with SERVFAIL when they exceed their <code>max-recursive-clients</code> or <code>recursive-clients</code> limit, respectively, a sudden increase in the number of failures could mean that the limit needs to be increased. </p>
<p> The &quot;Latency&quot; plot contains a single graph marked &quot;Average latency&quot;. This shows how the latency varies during the course of the test. Typically, the latency graph will exhibit a downwards trend because the cache hit rate improves as ever more responses are cached during the test, and the latency for a cache hit is much smaller than for a cache miss. The latency graph is provided as an aid in determining the point where the server gets overloaded, which can be seen as a sharp upwards turn in the graph. The latency graph is not intended for making absolute latency measurements or comparisons between servers; the latencies shown in the graph are not representative of production latencies due to the initially empty cache and the deliberate overloading of the server towards the end of the test. </p>
<p> Note that all measurements are displayed on the plot at the horizontal position corresponding to the point in time when the query was sent, not when the response (if any) was received. This makes it it easy to compare the query and response rates; for example, if no queries are dropped, the query and response graphs will be identical. As another example, if the plot shows 10% failure responses at t=5 seconds, this means that 10% of the queries sent at t=5 seconds eventually failed, not that 10% of the responses received at t=5 seconds were failures.</p>
<h3>Determining the server&#8217;s maximum throughput</h3>
<p> Often, the goal of running <code>resperf</code> is to determine the server&#8217;s maximum throughput, in other words, the number of queries per second it is capable of handling. This is not always an easy task, because as a server is driven into overload, the service it provides may deteriorate gradually, and this deterioration can manifest itself either as queries being dropped, as an increase in the number of SERVFAIL responses, or an increase in latency. The maximum throughput may be defined as the highest level of traffic at which the server still provides an acceptable level of service, but that means you first need to decide what an acceptable level of service means in terms of packet drop percentage, SERVFAIL percentage, and latency. </p>
<p> The summary statistics in the &quot;Resperf output&quot; section of the report contains a &quot;Maximum throughput&quot; value which by default is determined from the maximum rate at which the server was able to return responses, without regard to the number of queries being dropped or failing at that point. This method of throughput measurement has the advantage of simplicity, but it may or may not be appropriate for your needs; the reported value should always be validated by a visual inspection of the graphs to ensure that service has not already deteriorated unacceptably before the maximum response rate is reached. It may also be helpful to look at the &quot;Lost at that point&quot; value in the summary statistics; this indicates the percentage of the queries that was being dropped at the point in the test when the maximum throughput was reached. </p>
<p> Alternatively, you can make resperf report the throughput at the point in the test where the percentage of queries dropped exceeds a given limit (or the maximum as above if the limit is never exceeded). This can be a more realistic indication of how much the server can be loaded while still providing an acceptable level of service. This is done using the <code>-L</code> command line option; for example, specifying <code>-L 10</code> makes resperf report the highest throughput reached before the server starts dropping more than 10% of the queries. </p>
<p> There is no corresponding way of automatically constraining results based on the number of failed queries, because unlike dropped queries, resolution failures will occur even when the the server is not overloaded, and the number of such failures is heavily dependent on the query data and network conditions. Therefore, the plots should be manually inspected to ensure that there is not an abnormal number of failures.</p>
<h2>GENERATING CONSTANT TRAFFIC</h2>
<p> In addition to ramping up traffic linearly, <code>resperf</code> also has the capability to send a constant stream of traffic. This can be useful when using <code>resperf</code> for tasks other than performance measurement; for example, it can be used to &quot;soak test&quot; a server by subjecting it to a sustained load for an extended period of time. </p>
<p> To generate a constant traffic load, use the <code>-c</code> command line option, together with the <code>-m</code> option which specifies the desired constant query rate. For example, to send 10000 queries per second for an hour, use <code>-m 10000 -c 3600</code>. This will include the usual 30-second gradual ramp-up of traffic at the beginning, which may be useful to avoid initially overwhelming a server that is starting with an empty cache. To start the onslaught of traffic instantly, use <code>-m 10000 -c 3600 -r 0</code>. </p>
<p> To be precise, <code>resperf</code> will do a linear ramp-up of traffic from 0 to <code>-m</code> queries per second over a period of <code>-r</code> seconds, followed by a plateau of steady traffic at <code>-m</code> queries per second lasting for <code>-c</code> seconds, followed by waiting for responses for an extra 40 seconds. Either the ramp-up or the plateau can be suppressed by supplying a duration of zero seconds with <code>-r 0</code> and <code>-c 0</code>, respectively. The latter is the default. </p>
<p> Sending traffic at high rates for hours on end will of course require very large amounts of input data. Also, a long-running test will generate a large amount of plot data, which is kept in memory for the duration of the test. To reduce the memory usage and the size of the plot file, consider increasing the interval between measurements from the default of 0.5 seconds using the <code>-i</code> option in long-running tests. </p>
<p> When using <code>resperf</code> for long-running tests, it is important that the traffic rate specified using the <code>-m</code> is one that both <code>resperf</code> itself and the server under test can sustain. Otherwise, the test is likely to be cut short as a result of either running out of query IDs (because of large numbers of dropped queries) or of resperf falling behind its transmission schedule.</p>
<h2>OPTIONS</h2>
<p> Because the <code>resperf-report</code> script passes its command line options directly to the <code>resperf</code> programs, they both accept the same set of options, with one exception: <code>resperf-report</code> automatically adds an appropriate <code>-P</code> to the <code>resperf</code> command line, and therefore does not itself take a <code>-P</code> option. </p>
<p> <code>-d </code><i>datafile</i> </p>
<dl>
<dt>
<dd> Specifies the input data file. If not specified, <code>resperf</code> will read from standard input.</dl>
<p> <code>-s </code><i>server_addr</i> </p>
<dl>
<dt>
<dd> Specifies the name or address of the server to which requests will be sent. The default is the loopback address, 127.0.0.1.</dl>
<p> <code>-p </code><i>port</i> </p>
<dl>
<dt>
<dd> Sets the port on which the DNS packets are sent. If not specified, the standard DNS port (53) is used.</dl>
<p> <code>-a </code><i>local_addr</i> </p>
<dl>
<dt>
<dd> Specifies the local address from which to send requests. The default is the wildcard address.</dl>
<p> <code>-x </code><i>local_port</i> </p>
<dl>
<dt>
<dd> Specifies the local port from which to send requests. The default is the wildcard port (0). </p>
<p> If acting as multiple clients and the wildcard port is used, each client will use a different random port. If a port is specified, the clients will use a range of ports starting with the specified one.</dl>
<p> <code>-t </code><i>timeout</i> </p>
<dl>
<dt>
<dd> Specifies the request timeout value, in seconds. <code>resperf</code> will no longer wait for a response to a particular request after this many seconds have elapsed. The default is 45 seconds. </p>
<p> <code>resperf</code> times out unanswered requests in order to reclaim query IDs so that the query ID space will not be exhausted in a long-running test, such as when &quot;soak testing&quot; a server for an day with <code>-m 10000 -c 86400</code>. The timeouts and the ability to tune them are of little use in the more typical use case of a performance test lasting only a minute or two. </p>
<p> The default timeout of 45 seconds was chosen to be longer than the query timeout of current caching servers. Note that this is longer than the corresponding default in <code>dnsperf</code>, because caching servers can take many orders of magnitude longer to answer a query than authoritative servers do. </p>
<p> If a short timeout is used, there is a possibility that <code>resperf</code> will receive a response after the corresponding request has timed out; in this case, a message like Warning: Received a response with an unexpected id: 141 will be printed.</dl>
<p> <code>-b </code><i>bufsize</i> </p>
<dl>
<dt>
<dd> Sets the size of the socket&#8217;s send and receive buffers, in kilobytes. If not specified, the operating system&#8217;s default is used.</dl>
<p> <code>-f </code><i>family</i> </p>
<dl>
<dt>
<dd> Specifies the address family used for sending DNS packets. The possible values are &quot;inet&quot;, &quot;inet6&quot;, or &quot;any&quot;. If &quot;any&quot; (the default value) is specified, <code>resperf</code> will use whichever address family is appropriate for the server it is sending packets to.</dl>
<p> <code>-e</code> </p>
<dl>
<dt>
<dd> Enables EDNS0 [RFC2671], by adding an OPT record to all packets sent.</dl>
<p> <code>-D</code> </p>
<dl>
<dt>
<dd> Sets the DO (DNSSEC OK) bit [RFC3225] in all packets sent. This also enables EDNS0, which is required for DNSSEC.</dl>
<p> <code>-y </code><i>[alg:]name:secret</i> </p>
<dl>
<dt>
<dd> Add a TSIG record [RFC2845] to all packets sent, using the specified TSIG key algorithm, name and secret, where the algorithm defaults to hmac-md5 and the secret is expressed as a base-64 encoded string.</dl>
<p> <code>-h</code> </p>
<dl>
<dt>
<dd> Print a usage statement and exit.</dl>
<p> <code>-i </code><i>interval</i> </p>
<dl>
<dt>
<dd> Specifies the time interval between data points in the plot file. The default is 0.5 seconds.</dl>
<p> <code>-m </code><i>max_qps</i> </p>
<dl>
<dt>
<dd> Specifies the target maximum query rate (in queries per second). This should be higher than the expected maximum throughput of the server being tested. Traffic will be ramped up at a linearly increasing rate until this value is reached, or until one of the other conditions described in the section &quot;Running the test&quot; occurs. The default is 100000 queries per second.</dl>
<p> <code>-P </code><i>plot_data_file</i> </p>
<dl>
<dt>
<dd> Specifies the name of the plot data file. The default is <i>resperf.gnuplot</i>.</dl>
<p> <code>-r </code><i>rampup_time</i> </p>
<dl>
<dt>
<dd> Specifies the length of time over which traffic will be ramped up. The default is 60 seconds.</dl>
<p> <code>-c </code><i>constant_traffic_time</i> </p>
<dl>
<dt>
<dd> Specifies the length of time for which traffic will be sent at a constant rate following the initial ramp-up. The default is 0 seconds, meaning no sending of traffic at a constant rate will be done.</dl>
<p> <code>-L </code><i>max_loss</i> </p>
<dl>
<dt>
<dd> Specifies the maximum acceptable query loss percentage for purposes of determining the maximum throughput value. The default is 100%, meaning that <code>resperf</code> will measure the maximum throughput without regard to query loss.</dl>
<p> <code>-C </code><i>clients</i> </p>
<dl>
<dt>
<dd> Act as multiple clients. Requests are sent from multiple sockets. The default is to act as 1 client.</dl>
<p> <code>-q </code><i>max_outstanding</i> </p>
<dl>
<dt>
<dd> Sets the maximum number of outstanding requests. <code>resperf</code> will stop ramping up traffic when this many queries are outstanding. The default is 64k, and the limit is 64k per client.</dl>
<h2>THE PLOT DATA FILE</h2>
<p> The plot data file is written by the <code>resperf</code> program and contains the data to be plotted using <code>gnuplot</code>. When running <code>resperf</code> via the <code>resperf-report</code> script, there is no need for the user to deal with this file directly, but its format and contents are documented here for completeness and in case you wish to run <code>resperf</code> directly and use its output for purposes other than viewing it with <code>gnuplot</code>. </p>
<p> The first line of the file is a comment identifying the fields. It may be recognized as a comment by its leading hash sign (#). </p>
<p> Subsequent lines contain the actual plot data. For purposes of generating the plot data file, the test run is divided into time intervals of 0.5 seconds (or some other length of time specified with the <code>-i</code> command line option). Each line corresponds to one such interval, and contains the following values as floating-point numbers: </p>
<p> <code>Time</code> </p>
<dl>
<dt>
<dd> The midpoint of this time interval, in seconds since the beginning of the run</dl>
<p> <code>Target queries per second</code> </p>
<dl>
<dt>
<dd> The number of queries per second scheduled to be sent in this time interval</dl>
<p> <code>Actual queries per second</code> </p>
<dl>
<dt>
<dd> The number of queries per second actually sent in this time interval</dl>
<p> <code>Responses per second</code> </p>
<dl>
<dt>
<dd> The number of responses received corresponding to queries sent in this time interval, divided by the length of the interval</dl>
<p> <code>Failures per second</code> </p>
<dl>
<dt>
<dd> The number of responses received corresponding to queries sent in this time interval and having an RCODE other than NOERROR or NXDOMAIN, divided by the length of the interval</dl>
<p> <code>Average latency</code> </p>
<dl>
<dt>
<dd> The average time between sending the query and receiving a response, for queries sent in this time interval</dl>
<h2>AUTHOR</h2>
<p> Nominum, Inc.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dnsperf/">dnsperf</a></code>(1) </p>
<h2>Index</h2>
