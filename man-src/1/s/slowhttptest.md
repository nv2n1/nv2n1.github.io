---
title: "slowhttptest(1)"
name: "slowhttptest"
section: "1"
letter: "s"
url: "/docs/linux/man/1-slowhttptest/"
description: "slowhttptest – Denial Of Service attacks simulator"
---

<h2>NAME</h2>
<p> <code>slowhttptest</code> &#8211; Denial Of Service attacks simulator</p>
<h2>SYNOPSIS</h2>
<p> <code>slowhttptest</code> -words [-<code>H|B|R|X</code> ] [-<code>g</code> ] [-<code>a </code><i>range start</i> ] [-<code>b </code><i>range limit</i> ] [-<code>c </code><i>number of connections</i> ] [-<code>d </code><i>all traffic directed through HTTP proxy at host:port</i> ] [-<code>e </code><i>probe traffic directed through HTTP proxy at host:port</i> ] [-<code>i </code><i>interval in seconds</i> ] [-<code>k </code><i>request multiply factor</i> ] [-<code>l </code><i>test duration in seconds</i> ] [-<code>n </code><i>slow read interval in seconds</i> ] [-<code>o </code><i>output file path and/or name</i> ] [-<code>p </code><i>timeout for probe connection in seconds</i> ] [-<code>r </code><i>connection per second</i> ] [-<code>s </code><i>value of Content-Length header</i> ] [-<code>t </code><i>HTTP verb</i> ] [-<code>u </code><i>absolute URL</i> ] [-<code>v </code><i>output verbosity level</i> ] [-<code>w </code><i>advertised window size range start </i> ] [-<code>x </code><i>max length of follow up data</i> ] [-<code>y </code><i>advertised window size range end</i> ] [-<code>z </code><i>slow read from recieve buffer in bytes</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>slowhttptest</code> implements most common low-bandwidth Application Layer DoS attacks and produces CSV and HTML files with test statistics. </p>
<p> Currently supported attacks are: </p>
<ul>
<li> Slowloris
<li> Slow HTTP POST
<li> Apache Range Header
<li> Slow Read </ul>
<p> The options are as follows:</p>
<dl>
<dt><code>-g</code></p>
<dd> Forces <code>slowhttptest</code> to generate CSV and HTML files when test finishes with timestamp in filename.</p>
<dt><code>-H</code></p>
<dd> Starts <code>slowhttptest</code> in SlowLoris mode, sending unfinished HTTP requests.</p>
<dt><code>-B</code></p>
<dd> Starts <code>slowhttptest</code> in Slow POST mode, sending unfinished HTTP message bodies.</p>
<dt><code>-R</code></p>
<dd> Starts <code>slowhttptest</code> in Range Header mode, sending malicious Range Request header data.</p>
<dt><code>-X</code></p>
<dd> Starts <code>slowhttptest</code> in Slow Read mode, reading HTTP responses slowly.</p>
<dt><code>-a </code><i>start</i></p>
<dd> Sets the start value of range-specifier for Range Header attack.</p>
<dt><code>-b </code><i>bytes</i></p>
<dd> Sets the limit value of range-specifier for Range Header attack.</p>
<dt><code>-c </code><i>number of connections</i></p>
<dd> Specifies the target number of connections to establish during the test.</p>
<dt><code>-d </code><i>HTTP proxy host:port</i></p>
<dd> Specifies HTTP proxy server to connect to for all connections.</p>
<dt><code>-e </code><i>HTTP proxy host:port</i></p>
<dd> Specifies HTTP proxy server to connect to for probe connections.</p>
<dt><code>-i </code><i>seconds</i></p>
<dd> Specifies the interval between follow up data for slowrois and Slow POST tests.</p>
<dt><code>-k </code><i>pipeline factor</i></p>
<dd> Specifies number of times the resource would be requested per socket in Slow Read test.</p>
<dt><code>-l </code><i>seconds</i></p>
<dd> Specifies test duration in seconds.</p>
<dt><code>-n </code><i>seconds</i></p>
<dd> Specifies the interval between read operations for Slow Read test.</p>
<dt><code>-o </code><i>file name</i></p>
<dd> Specifies custom file name, effective with -g.</p>
<dt><code>-p </code><i>seconds</i></p>
<dd> Specifies the interval to wait for HTTP response onprobe connection, before marking the server as DoSed.</p>
<dt><code>-r </code><i>connections per second</i></p>
<dd> Specifies the connection rate.</p>
<dt><code>-s </code><i>bytes</i></p>
<dd> Specifies the value of Content-Length header for Slow POST test.</p>
<dt><code>-t </code><i>HTTP verb</i></p>
<dd> Specifies the verb to use in HTTP request.</p>
<dt><code>-u </code><i>URL</i></p>
<dd> Specifies the URL.</p>
<dt><code>-v </code><i>level</i></p>
<dd> Specifies the verbosity level of logging.</p>
<dt><code>-w </code><i>bytes</i></p>
<dd> Specifies the start of the range the TCP advertised window size would be picked from in Slow Read test.</p>
<dt><code>-x </code><i>bytes</i></p>
<dd> Specifies the maximum length of follow up data for slowloris and Slow POST tests.</p>
<dt><code>-y </code><i>bytes</i></p>
<dd> Specifies the end of the range the TCP advertised window size would be picked from in Slow Read test.</p>
<dt><code>-z </code><i>bytes</i></p>
<dd> Specifies the number of bytes to read from receive buffer with each read() operation.</dl>
</dl>
<h2>EXAMPLES</h2>
<p> Start a slowloris test of host.example.com with 1000 connections, statistics goes into my_header_stats, interval between follow up headers is 10 seconds and connection rate is 200 connections per second: </p>
<blockquote><p><tt>$ slowhttptest -c 1000 -H -g -o my_header_stats -i 10 -r 200 -t GET -u <a rel="nofollow" href="https://host.example.com/index.html">https://host.example.com/index.html</a> -x 24 -p 3</tt></p></blockquote>
<p> Start slow POST test of host.example.com with 3000 connections, statistics goes into my_body_stats, interval between follow up headers is 110 seconds, connection rate is 200 connections per second, Content-Length header value is 8192, maximum length of follow up data is random value limited by 10 bytes and probe connections waits 3 seconds for HTTP response before marking server as DoSed: </p>
<blockquote><p><tt>$ slowhttptest -c 3000 -B -g -o my_body_stats -i 110 -r 200 -s 8192 -t FAKEVERB -u <a rel="nofollow" href="http://host.example.com/loginform.html">http://host.example.com/loginform.html</a> -x 10 -p 3</tt></p></blockquote>
<p> Start Range Header test of host.example.com with 1000 connections, use HEAD verb, and generate HTTP header Range:0-, x-1, x-2, x-3, &#8230; x-y, where x is 10 and y is 3000, connection rate is 500: interval between follow up headers is 10 seconds and connection rate is 200 connections per second: </p>
<blockquote><p><tt>$ slowhttptest -R -u <a rel="nofollow" href="http://host.example.com/">http://host.example.com/</a> -t HEAD -c 1000 -a 10 -b 3000 -r 500</tt></p></blockquote>
<p> Start Slow Read test of host.example.com with 8000 connections, no statistics is generated, connection rate is 200 connections per second, TCP advertised window size is a random value between 512 and 1024, <code>slowhttptest</code> reads 32 bytes from each connections every 5 seconds, 3 requests are pipelined per each connections, probe connection waits 3 seconds for HTTP response before marking server as DoSed: </p>
<blockquote><p><tt>$ slowhttptest -c 8000 -X -r 200 -w 512 -y 1024 -n 5 -z 32 -k 3 -u <a rel="nofollow" href="https://host.example.com/resources/index.html">https://host.example.com/resources/index.html</a> -p 3</tt></p></blockquote>
<p> Start Slow Read test of host.example.com through HTTP proxy server at 10.10.0.1:8080 with 8000 connections, no statistics is generated, the rest test vaules are default. <code>slowhttptest</code> most likely would test HTTP proxy server itself, rather than target server, but it all depends on the HTTP proxy server implementation: </p>
<blockquote><p><tt>$ slowhttptest -d 10.10.0.1:8080 -c 8000 -X -u <a rel="nofollow" href="https://host.example.com/resources/index.html">https://host.example.com/resources/index.html</a></tt></p></blockquote>
<p> Start Slow Read test of host.example.com and direct probe traffic through HTTP proxy server at 10.10.0.1:8080 with 8000 connections, no statistics is generated, the rest test vaules are default. Specifying another connection channel for probe connections helps to make sure that <code>slowhttptest</code> shows valid statistics for availability of server under test: </p>
<blockquote><p><tt>$ slowhttptest -e 10.10.0.1:8080 -c 8000 -X -u <a rel="nofollow" href="https://host.example.com/resources/index.html">https://host.example.com/resources/index.html</a></tt></p></blockquote>
<h2>AUTHOR</h2>
<p> Sergey Shekyan Aq shekyan [at] gmail.com . </p>
<p> Project page Aq <a rel="nofollow" href="http://code.google.com/p/slowhttptest/">http://code.google.com/p/slowhttptest/</a> . </p>
<h2>Index</h2>
