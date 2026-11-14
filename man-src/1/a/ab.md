---
title: "ab(1)"
name: "ab"
section: "1"
letter: "a"
url: "/docs/linux/man/1-ab/"
description: "ab – Apache HTTP server benchmarking tool"
---

<h2 class="name">NAME</h2>
<p> ab &#8211; Apache HTTP server benchmarking tool</p>
<h2>SYNOPSIS</h2>
<p>&nbsp; </p>
<p> <code>ab</code> [ &#8211;<code>A</code> <i>auth-username</i>:<i>password</i> ] [ &#8211;<code>b</code> <i>windowsize</i> ] [ &#8211;<code>B</code> <i>local-address</i> ] [ &#8211;<code>c</code> <i>concurrency</i> ] [ &#8211;<code>C</code> <i>cookie-name</i>=<i>value</i> ] [ &#8211;<code>d</code> ] [ &#8211;<code>e</code> <i>csv-file</i> ] [ &#8211;<code>E</code> <i>client-certificate file</i> ] [ &#8211;<code>f</code> <i>protocol</i> ] [ &#8211;<code>g</code> <i>gnuplot-file</i> ] [ &#8211;<code>h</code> ] [ &#8211;<code>H</code> <i>custom-header</i> ] [ &#8211;<code>i</code> ] [ &#8211;<code>k</code> ] [ &#8211;<code>l</code> ] [ &#8211;<code>m</code> <i>HTTP-method</i> ] [ &#8211;<code>n</code> <i>requests</i> ] [ &#8211;<code>p</code> <i>POST-file</i> ] [ &#8211;<code>P</code> <i>proxy-auth-username</i>:<i>password</i> ] [ &#8211;<code>q</code> ] [ &#8211;<code>r</code> ] [ &#8211;<code>s</code> <i>timeout</i> ] [ &#8211;<code>S</code> ] [ &#8211;<code>t</code> <i>timelimit</i> ] [ &#8211;<code>T</code> <i>content-type</i> ] [ &#8211;<code>u</code> <i>PUT-file</i> ] [ &#8211;<code>v</code> <i>verbosity</i>] [ &#8211;<code>V</code> ] [ &#8211;<code>w</code> ] [ &#8211;<code>x</code> <i>&lt;table&gt;-attributes</i> ] [ &#8211;<code>X</code> <i>proxy</i>[:<i>port</i>] ] [ &#8211;<code>y</code> <i>&lt;tr&gt;-attributes</i> ] [ &#8211;<code>z</code> <i>&lt;td&gt;-attributes</i> ] [ &#8211;<code>Z</code> <i>ciphersuite</i> ] [http[s]://]<i>hostname</i>[:<i>port</i>]/<i>path</i><br />
&nbsp; </p>
<h2>SUMMARY</h2>
<p>&nbsp; </p>
<p> <code>ab</code> is a tool for benchmarking your Apache Hypertext Transfer Protocol (HTTP) server. It is designed to give you an impression of how your current Apache installation performs. This especially shows you how many requests per second your Apache installation is capable of serving.<br />
&nbsp; </p>
<h2>OPTIONS</h2>
<p>&nbsp;<br />
&nbsp;</p>
<dl>
<dt><code>-A </code><i>auth-username</i>:<i>password</i></p>
<dd> Supply BASIC Authentication credentials to the server. The username and password are separated by a single <code>:</code> and sent on the wire base64 encoded. The string is sent regardless of whether the server needs it (<i>i.e.</i>, has sent an 401 authentication needed).</p>
<dt><code>-b </code><i>windowsize</i></p>
<dd> Size of TCP send/receive buffer, in bytes.</p>
<dt><code>-B </code><i>local-address</i></p>
<dd> Address to bind to when making outgoing connections.</p>
<dt><code>-c </code><i>concurrency</i></p>
<dd> Number of multiple requests to perform at a time. Default is one request at a time.</p>
<dt><code>-C </code><i>cookie-name</i>=<i>value</i></p>
<dd> Add a <code>Cookie:</code> line to the request. The argument is typically in the form of a <i>name</i>=<i>value</i> pair. This field is repeatable.</p>
<dt><code>-d</code></p>
<dd> Do not display the &quot;percentage served within XX [ms] table&quot;. (legacy support).</p>
<dt><code>-e </code><i>csv-file</i></p>
<dd> Write a Comma separated value (CSV) file which contains for each percentage (from 1% to 100%) the time (in milliseconds) it took to serve that percentage of the requests. This is usually more useful than the &#8216;gnuplot&#8217; file; as the results are already &#8216;binned&#8217;.</p>
<dt><code>-E </code><i>client-certificate-file</i></p>
<dd> When connecting to an SSL website, use the provided client certificate in PEM format to authenticate with the server. The file is expected to contain the client certificate, followed by intermediate certificates, followed by the private key. Available in 2.4.36 and later.</p>
<dt><code>-f </code><i>protocol</i></p>
<dd> Specify SSL/TLS protocol (SSL2, SSL3, TLS1, TLS1.1, TLS1.2, or ALL). TLS1.1 and TLS1.2 support available in 2.4.4 and later.</p>
<dt><code>-g </code><i>gnuplot-file</i></p>
<dd> Write all measured values out as a &#8216;gnuplot&#8217; or TSV (Tab separate values) file. This file can easily be imported into packages like Gnuplot, IDL, Mathematica, Igor or even Excel. The labels are on the first line of the file.</p>
<dt><code>-h</code></p>
<dd> Display usage information.</p>
<dt><code>-H </code><i>custom-header</i></p>
<dd> Append extra headers to the request. The argument is typically in the form of a valid header line, containing a colon-separated field-value pair (<i>i.e.</i>, <code>&quot;Accept-Encoding: zip/zop;8bit&quot;</code>).</p>
<dt><code>-i</code></p>
<dd> Do <code>HEAD</code> requests instead of <code>GET</code>.</p>
<dt><code>-k</code></p>
<dd> Enable the HTTP KeepAlive feature, <i>i.e.</i>, perform multiple requests within one HTTP session. Default is no KeepAlive.</p>
<dt><code>-l</code></p>
<dd> Do not report errors if the length of the responses is not constant. This can be useful for dynamic pages. Available in 2.4.7 and later.</p>
<dt><code>-m </code><i>HTTP-method</i></p>
<dd> Custom HTTP method for the requests. Available in 2.4.10 and later.</p>
<dt><code>-n </code><i>requests</i></p>
<dd> Number of requests to perform for the benchmarking session. The default is to just perform a single request which usually leads to non-representative benchmarking results.</p>
<dt><code>-p </code><i>POST-file</i></p>
<dd> File containing data to POST. Remember to also set <code>-T</code>.</p>
<dt><code>-P </code><i>proxy-auth-username</i>:<i>password</i></p>
<dd> Supply BASIC Authentication credentials to a proxy en-route. The username and password are separated by a single <code>:</code> and sent on the wire base64 encoded. The string is sent regardless of whether the proxy needs it (<i>i.e.</i>, has sent an 407 proxy authentication needed).</p>
<dt><code>-q</code></p>
<dd> When processing more than 150 requests, <code>ab</code> outputs a progress count on <code>stderr</code> every 10% or 100 requests or so. The <code>-q</code> flag will suppress these messages.</p>
<dt><code>-r</code></p>
<dd> Don&#8217;t exit on socket receive errors.</p>
<dt><code>-s </code><i>timeout</i></p>
<dd> Maximum number of seconds to wait before the socket times out. Default is 30 seconds. Available in 2.4.4 and later.</p>
<dt><code>-S</code></p>
<dd> Do not display the median and standard deviation values, nor display the warning/error messages when the average and median are more than one or two times the standard deviation apart. And default to the min/avg/max values. (legacy support).</p>
<dt><code>-t </code><i>timelimit</i></p>
<dd> Maximum number of seconds to spend for benchmarking. This implies a <code>-n 50000</code> internally. Use this to benchmark the server within a fixed total amount of time. Per default there is no timelimit.</p>
<dt><code>-T </code><i>content-type</i></p>
<dd> Content-type header to use for POST/PUT data, eg. <code>application/x-www-form-urlencoded</code>. Default is <code>text/plain</code>.</p>
<dt><code>-u </code><i>PUT-file</i></p>
<dd> File containing data to PUT. Remember to also set <code>-T</code>.</p>
<dt><code>-v </code><i>verbosity</i></p>
<dd> Set verbosity level &#8211; <code>4</code> and above prints information on headers, <code>3</code> and above prints response codes (404, 200, etc.), <code>2</code> and above prints warnings and info.</p>
<dt><code>-V</code></p>
<dd> Display version number and exit.</p>
<dt><code>-w</code></p>
<dd> Print out results in HTML tables. Default table is two columns wide, with a white background.</p>
<dt><code>-x </code><i>&lt;table&gt;-attributes</i></p>
<dd> String to use as attributes for <code>&lt;table&gt;</code>. Attributes are inserted <code>&lt;table </code><i>here</i> &gt;.</p>
<dt><code>-X </code><i>proxy</i>[:<i>port</i>]</p>
<dd> Use a proxy server for the requests.</p>
<dt><code>-y </code><i>&lt;tr&gt;-attributes</i></p>
<dd> String to use as attributes for <code>&lt;tr&gt;</code>.</p>
<dt><code>-z </code><i>&lt;td&gt;-attributes</i></p>
<dd> String to use as attributes for <code>&lt;td&gt;</code>.</p>
<dt><code>-Z </code><i>ciphersuite</i></p>
<dd> Specify SSL/TLS cipher suite (See openssl ciphers)<br />
&nbsp;</dl>
<h2>OUTPUT</h2>
<p>&nbsp; </p>
<p> The following list describes the values returned by <code>ab</code>:<br />
&nbsp;<br />
&nbsp;</p>
<dl>
<dt>Server Software</p>
<dd> The value, if any, returned in the <i>server</i> HTTP header of the first successful response. This includes all characters in the header from beginning to the point a character with decimal value of 32 (most notably: a space or CR/LF) is detected.</p>
<dt>Server Hostname</p>
<dd> The DNS or IP address given on the command line</p>
<dt>Server Port</p>
<dd> The port to which ab is connecting. If no port is given on the command line, this will default to 80 for http and 443 for https.</p>
<dt>SSL/TLS Protocol</p>
<dd> The protocol parameters negotiated between the client and server. This will only be printed if SSL is used.</p>
<dt>Document Path</p>
<dd> The request URI parsed from the command line string.</p>
<dt>Document Length</p>
<dd> This is the size in bytes of the first successfully returned document. If the document length changes during testing, the response is considered an error.</p>
<dt>Concurrency Level</p>
<dd> The number of concurrent clients used during the test</p>
<dt>Time taken for tests</p>
<dd> This is the time taken from the moment the first socket connection is created to the moment the last response is received</p>
<dt>Complete requests</p>
<dd> The number of successful responses received</p>
<dt>Failed requests</p>
<dd> The number of requests that were considered a failure. If the number is greater than zero, another line will be printed showing the number of requests that failed due to connecting, reading, incorrect content length, or exceptions.</p>
<dt>Write errors</p>
<dd> The number of errors that failed during write (broken pipe).</p>
<dt>Non-2xx responses</p>
<dd> The number of responses that were not in the 200 series of response codes. If all responses were 200, this field is not printed.</p>
<dt>Keep-Alive requests</p>
<dd> The number of connections that resulted in Keep-Alive requests</p>
<dt>Total body sent</p>
<dd> If configured to send data as part of the test, this is the total number of bytes sent during the tests. This field is omitted if the test did not include a body to send.</p>
<dt>Total transferred</p>
<dd> The total number of bytes received from the server. This number is essentially the number of bytes sent over the wire.</p>
<dt>HTML transferred</p>
<dd> The total number of document bytes received from the server. This number excludes bytes received in HTTP headers</p>
<dt>Requests per second</p>
<dd> This is the number of requests per second. This value is the result of dividing the number of requests by the total time taken</p>
<dt>Time per request</p>
<dd> The average time spent per request. The first value is calculated with the formula <code>concurrency * timetaken * 1000 / done</code> while the second value is calculated with the formula <code>timetaken * 1000 / done</code></p>
<dt>Transfer rate</p>
<dd> The rate of transfer as calculated by the formula <code>totalread / 1024 / timetaken</code><br />
&nbsp;</dl>
<h2>BUGS</h2>
<p>&nbsp; </p>
<p> There are various statically declared buffers of fixed length. Combined with the lazy parsing of the command line arguments, the response headers from the server and other external inputs, this might bite you.<br />
&nbsp; </p>
<p> It does not implement HTTP/1.x fully; only accepts some &#8216;expected&#8217; forms of responses. The rather heavy use of <code><a href="/docs/linux/man/3-strstr/">strstr</a>(3)</code> shows up top in profile, which might indicate a performance problem; <i>i.e.</i>, you would measure the <code>ab</code> performance rather than the server&#8217;s.<br />
&nbsp; </p>
<h2>Index</h2>
