---
title: "ab(8)"
name: "ab"
section: "8"
letter: "a"
url: "/docs/linux/man/8-ab/"
description: "ab – Apache HTTP server benchmarking tool"
---

<p>ab &#8211; Apache HTTP server benchmarking tool</p>
<h2>Synopsis</h2>
<p> <code>ab</code> [ &#8211;<code>A</code> <i>auth-username</i>:<i>password</i> ] [ &#8211;<code>b</code> <i>windowsize</i> ] [ &#8211;<code>c</code> <i>concurrency</i> ] [ &#8211;<code>C</code> <i>cookie-name</i>=<i>value</i> ] [ &#8211;<code>d</code> ] [ &#8211;<code>e</code> <i>csv-file</i> ] [ &#8211;<code>f</code> <i>protocol</i> ] [ &#8211;<code>g</code> <i>gnuplot-file</i> ] [ &#8211;<code>h</code> ] [ &#8211;<code>H</code> <i>custom-header</i> ] [ &#8211;<code>i</code> ] [ &#8211;<code>k</code> ] [ &#8211;<code>n</code> <i>requests</i> ] [ &#8211;<code>p</code> <i>POST-file</i> ] [ &#8211;<code>P</code> <i>proxy-auth-username</i>:<i>password</i> ] [ &#8211;<code>q</code> ] [ &#8211;<code>r</code> ] [ &#8211;<code>s</code> ] [ &#8211;<code>S</code> ] [ &#8211;<code>t</code> <i>timelimit</i> ] [ &#8211;<code>T</code> <i>content-type</i> ] [ &#8211;<code>u</code> <i>PUT-file</i> ] [ &#8211;<code>v</code> <i>verbosity</i>] [ &#8211;<code>V</code> ] [ &#8211;<code>w</code> ] [ &#8211;<code>x</code> <i>&lt;table&gt;-attributes</i> ] [ &#8211;<code>X</code> <i>proxy</i>[:<i>port</i>] ] [ &#8211;<code>y</code> <i>&lt;tr&gt;-attributes</i> ] [ &#8211;<code>z</code> <i>&lt;td&gt;-attributes</i> ] [ &#8211;<code>Z</code> <i>ciphersuite</i> ] [http[s]://]<i>hostname</i>[:<i>port</i>]/<i>path</i><br />
&nbsp;<wbr> </p>
<h2>Summary</h2>
<p>&nbsp;<wbr> </p>
<p> ab is a tool for benchmarking your Apache Hypertext Transfer Protocol (HTTP) server. It is designed to give you an impression of how your current Apache installation performs. This especially shows you how many requests per second your Apache installation is capable of serving.<br />
&nbsp;<wbr></p>
<h2>Options</h2>
<p>&nbsp;<wbr><br />
&nbsp;<wbr></p>
<dl>
<dt>-A <i>auth-username</i>:<i>password</i></p>
<dd>Supply BASIC Authentication credentials to the server. The username and password are separated by a single : and sent on the wire base64 encoded. The string is sent regardless of whether the server needs it (<i>i.e.</i>, has sent an 401 authentication needed).</p>
<dt>-b <i>windowsize</i></p>
<dd>Size of TCP send/receive buffer, in bytes.</p>
<dt>-c <i>concurrency</i></p>
<dd>Number of multiple requests to perform at a time. Default is one request at a time.</p>
<dt>-C <i>cookie-name</i>=<i>value</i></p>
<dd>Add a Cookie: line to the request. The argument is typically in the form of a <i>name</i>=<i>value</i> pair. This field is repeatable.</p>
<dt>-d</p>
<dd>Do not display the &quot;percentage served within XX [ms] table&quot;. (legacy support).</p>
<dt>-e <i>csv-file</i></p>
<dd>Write a Comma separated value (CSV) file which contains for each percentage (from 1% to 100%) the time (in milliseconds) it took to serve that percentage of the requests. This is usually more useful than the &#8216;gnuplot&#8217; file; as the results are already &#8216;binned&#8217;.</p>
<dt>-f <i>protocol</i></p>
<dd>Specify SSL/TLS protocol (SSL2, SSL3, TLS1, or ALL).</p>
<dt>-g <i>gnuplot-file</i></p>
<dd>Write all measured values out as a &#8216;gnuplot&#8217; or TSV (Tab separate values) file. This file can easily be imported into packages like Gnuplot, IDL, Mathematica, Igor or even Excel. The labels are on the first line of the file.</p>
<dt>-h</p>
<dd>Display usage information.</p>
<dt>-H <i>custom-header</i></p>
<dd>Append extra headers to the request. The argument is typically in the form of a valid header line, containing a colon-separated field-value pair (<i>i.e.</i>, &quot;Accept-Encoding: zip/zop;8bit&quot;).</p>
<dt>-i</p>
<dd>Do HEAD requests instead of GET.</p>
<dt>-k</p>
<dd>Enable the HTTP KeepAlive feature, <i>i.e.</i>, perform multiple requests within one HTTP session. Default is no KeepAlive.</p>
<dt>-n <i>requests</i></p>
<dd>Number of requests to perform for the benchmarking session. The default is to just perform a single request which usually leads to non-representative benchmarking results.</p>
<dt>-p <i>POST-file</i></p>
<dd>File containing data to POST. Remember to also set -T.</p>
<dt>-P <i>proxy-auth-username</i>:<i>password</i></p>
<dd>Supply BASIC Authentication credentials to a proxy en-route. The username and password are separated by a single : and sent on the wire base64 encoded. The string is sent regardless of whether the proxy needs it (<i>i.e.</i>, has sent an 407 proxy authentication needed).</p>
<dt>-q</p>
<dd>When processing more than 150 requests, ab outputs a progress count on stderr every 10% or 100 requests or so. The -q flag will suppress these messages.</p>
<dt>-r</p>
<dd>Don&#8217;t exit on socket receive errors.</p>
<dt>-s</p>
<dd>When compiled in (ab -h will show you) use the SSL protected https rather than the http protocol. This feature is experimental and <i>very</i> rudimentary. You probably do not want to use it.</p>
<dt>-S</p>
<dd>Do not display the median and standard deviation values, nor display the warning/error messages when the average and median are more than one or two times the standard deviation apart. And default to the min/avg/max values. (legacy support).</p>
<dt>-t <i>timelimit</i></p>
<dd>Maximum number of seconds to spend for benchmarking. This implies a -n 50000 internally. Use this to benchmark the server within a fixed total amount of time. Per default there is no timelimit.</p>
<dt>-T <i>content-type</i></p>
<dd>Content-type header to use for POST/PUT data, eg. application/x-www-form-urlencoded. Default: text/plain.</p>
<dt>-u <i>PUT-file</i></p>
<dd>File containing data to PUT. Remember to also set -T.</p>
<dt>-v <i>verbosity</i></p>
<dd>Set verbosity level &#8211; 4 and above prints information on headers, 3 and above prints response codes (404, 200, etc.), 2 and above prints warnings and info.</p>
<dt>-V</p>
<dd>Display version number and exit.</p>
<dt>-w</p>
<dd>Print out results in HTML tables. Default table is two columns wide, with a white background.</p>
<dt>-x <i>&lt;table&gt;-attributes</i></p>
<dd>String to use as attributes for &lt;table&gt;. Attributes are inserted &lt;table <i>here</i> &gt;.</p>
<dt>-X <i>proxy</i>[:<i>port</i>]</p>
<dd>Use a proxy server for the requests.</p>
<dt>-y <i>&lt;tr&gt;-attributes</i></p>
<dd>String to use as attributes for &lt;tr&gt;.</p>
<dt>-z <i>&lt;td&gt;-attributes</i></p>
<dd>String to use as attributes for &lt;td&gt;.</p>
<dt>-Z <i>ciphersuite</i></p>
<dd>Specify SSL/TLS cipher suite (See openssl ciphers).<br />
&nbsp;<wbr></dl>
<h2>Description Of Output</h2>
<p>&nbsp;<wbr> </p>
<p> The following list describes the values returned by ab:<br />
&nbsp;<wbr><br />
&nbsp;<wbr></p>
<dl>
<dt>Server Software</p>
<dd>The value, if any, returned in the <i>server</i> HTTP header of the first successful response. This includes all characters in the header from beginning to the point a character with decimal value of 32 (most notably: a space or CR/LF) is detected.</p>
<dt>Server Hostname</p>
<dd>The DNS or IP address given on the command line</p>
<dt>Server Port</p>
<dd>The port to which ab is connecting. If no port is given on the command line, this will default to 80 for http and 443 for https.</p>
<dt>SSL/TLS Protocol</p>
<dd>The protocol parameters negotiated between the client and server. This will only be printed if SSL is used.</p>
<dt>Document Path</p>
<dd>The request URI parsed from the command line string.</p>
<dt>Document Length</p>
<dd>This is size in bytes of the first succesfully returning document. If the document length changes during testing, the response is considered an error.</p>
<dt>Concurrency Level</p>
<dd>The number of concurrent clients used during the test</p>
<dt>Time taken for tests</p>
<dd>This is the time taken from the moment the first socket connection is created to the moment the last response is recieved</p>
<dt>Complete requests</p>
<dd>The number of successful responses recieved</p>
<dt>Failed requests</p>
<dd>The number of requests that were considered a failure. If the number is greater than zero, another line will be printed showing the numer of requests that failed due to connecting, reading, incorrect content length, or exceptions.</p>
<dt>Write errors</p>
<dd>The number of errors that failed during write (broken pipe).</p>
<dt>Non-2xx responses</p>
<dd>The number of responses that were not in the 200 series of response codes. If all responses were 200, this field is not printed.</p>
<dt>Keep-Alive requests</p>
<dd>The number of connections that resulted in Keep-Alive requests</p>
<dt>Total body sent</p>
<dd>If configured to send data as part of the test, this is the total number of bytes sent during the tests. This field is omitted if the test did not include a body to send.</p>
<dt>Total transferred</p>
<dd>The total number of bytes received from the server. This number is essentially the number of bytes sent over the wire.</p>
<dt>HTML transferred</p>
<dd>The total number of document bytes received from the server. This number excludes bytes received in HTTP headers</p>
<dt>Requests per second</p>
<dd>This is the number of requests per second. This value is the result of dividing the number of requests by the total time taken</p>
<dt>Time per request</p>
<dd>The average time spent per request. The first value is calculated with the formula concurrency * timetaken * 1000 / done while the second value is calculated with the formula timetaken * 1000 / done</p>
<dt>Transfer rate</p>
<dd>The rate of transfer as calculated by the formula totalread / 1024 / timetaken<br />
&nbsp;<wbr></dl>
<h2>Bugs</h2>
<p> There are various statically declared buffers of fixed length. Combined with the lazy parsing of the command line arguments, the response headers from the server and other external inputs, this might bite you.<br />
&nbsp;<wbr> It does not implement HTTP/1.x fully; only accepts some &#8216;expected&#8217; forms of responses. The rather heavy use of <a href="/docs/linux/man/3-strstr/">strstr</a>(3) shows up top in profile, which might indicate a performance problem; <i>i.e.</i>, you would measure the ab performance rather than the server&#8217;s.<br />
&nbsp;<wbr> </p>
