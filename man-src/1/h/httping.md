---
title: "httping(1)"
name: "httping"
section: "1"
letter: "h"
url: "/docs/linux/man/1-httping/"
description: "httping – measure the latency and throughput of a webserver"
---

<h2>NAME</h2>
<p> httping &#8211; measure the latency and throughput of a webserver</p>
<h2>SYNOPSIS</h2>
<p> <code>httping [</code><i>options</i><code>]</code> </p>
<p> options: <code>[-g url] [-h hostname] [-p portnumber] [-x proxyhost:port] [-c count] [-i interval] [-t timeout] [-s] [-G] [-b] [-L xferlimit] [-X] [-l] [-z] [-f] [-m] [-o rc,&#8230;] [-e string]</code> <code>[-I useragent string] [-R referer string] [-r] [-n warn,crit] [-N mode] [-q] [-V]</code></p>
<h2>DESCRIPTION</h2>
<p> The program <code>httping</code> lets you measure the latency of a webserver. Since version 1.0.6 also the throughput can be measured. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-5</code></p>
<dd> The proxy server selected is a SOCKS5 server.</p>
<dt><code>-6</code></p>
<dd> Enable IPv6 mode. Default is IPv4.</p>
<dt><code>-a</code></p>
<dd> Audible ping</p>
<dt><code>-b</code></p>
<dd> Use this switch together with &#8216;-G&#8217;. When this option is used, the transferspeed (in KB/s) is shown.</p>
<dt><code>-B</code></p>
<dd> Use this switch together with &#8216;-G&#8217;. Ask the HTTP server to compress the returned data: this will reduce the influence of the bandwidth of your connection while increasing the influence of the processorpower of the HTTP server.</p>
<dt><code>-c count</code></p>
<dd> How many probes to send before exiting.</p>
<dt><code>-D</code></p>
<dd> Do not draw graphs in ncurses mode (-K).</p>
<dt><code>-e str</code></p>
<dd> When the status-code differs from the ones selected with &#8216;-o&#8217;, the given string is displayed.</p>
<dt><code>-E</code></p>
<dd> Retrieve proxy settings from environment variables (&#8216;http_proxy&#8217; and &#8216;https_proxy&#8217;).</p>
<dt><code>-F</code></p>
<dd> Attempt TCP Fast Open while trying to connect to a server (for Linux, version 3.7 onwards of the kernel)</p>
<dt><code>-f</code></p>
<dd> Flood ping: do not sit idle between each ping but ping as fast as the computer and network allow you to.</p>
<dt><code>-G</code></p>
<dd> Do a GET request instead of a HEAD request: this means that also the complete page/file must be transferred. Note that in this case you&#8217;re no longer measuring the latency!</p>
<dt><code>-g url</code></p>
<dd> This selects the url to probe. E.g.: <a rel="nofollow" href="http://localhost/">http://localhost/</a></p>
<dt><code>-h hostname</code></p>
<dd> Instead of &#8216;-g&#8217; one can also set a hostname to probe with -h: -h localhost</p>
<dt><code>-I str</code></p>
<dd> UserAgent-string to send to the webserver (instead of &#8216;HTTPing &lt;version&gt;&#8217;).</p>
<dt><code>-i interval</code></p>
<dd> How many seconds to sleep between every probe sent.</p>
<dt><code>-K</code></p>
<dd> Enable ncurses user interface.</p>
<dt><code>-L x</code></p>
<dd> Use this switch together with &#8216;-G&#8217;. Limit the amount of data transferred to &#8216;x&#8217;. Note that this only affects the content of the page/file and not the headerdata.</p>
<dt><code>-l</code></p>
<dd> Connect using SSL: for this to work you need to give a &#8216;https&#8217;-url or a 443 portnumber.</p>
<dt><code>-m</code></p>
<dd> Show machine readable output (also check &#8216;-o&#8217; and &#8216;-e&#8217;).</p>
<dt><code>-N x</code></p>
<dd> Switches HTTPing to Nagios-plugin mode 2: return 0 when everything is fine, &#8216;x&#8217; when anything fails. E.g.: 1 =&gt; Nagios warning state, 2 =&gt; Nagios critical state.</p>
<dt><code>-n warn,crit</code></p>
<dd> Switches HTTPing to Nagios-plugin mode 1: return exitcode &#8216;1&#8217; when the average response time is bigger then &#8216;warn&#8217;, return exitcode &#8216;2&#8217; when the the average response time is bigger then &#8216;crit&#8217;. In all other cases return exitcode &#8216;0&#8217;.</p>
<dt><code>-o x,x,&#8230;</code></p>
<dd> This selects the HTTP status-codes which are regarded as an OK-state (only with &#8216;-m&#8217;).</p>
<dt><code>-p portnumber</code></p>
<dd> -p can be used together with -h. -p selects the portnumber to probe.</p>
<dt><code>-q</code></p>
<dd> Be quiet, only return an exit-code.</p>
<dt><code>-R str</code></p>
<dd> Referer-string to send to the webserver.</p>
<dt><code>-Q</code></p>
<dd> Use a persistent connection, i.e. reuse the same TCP connection for multiple HTTP requests. Usually possible when &#8216;Connection: Keep-Alive&#8217; is sent by server. Adds a &#8216;C&#8217; to the output if httping had to reconnect.</p>
<dt><code>-r</code></p>
<dd> Only resolve the hostname once: this takes the resolving out of the loop so that the latency of the DNS is not measured. Also useful when you want to measure only 1 webserver while the DNS returns a different ip-address for each resolve (&#8217;roundrobin&#8217;).</p>
<dt><code>-S</code></p>
<dd> Split measured latency in time to connect and time to exchange a request with the HTTP server.</p>
<dt><code>-s</code></p>
<dd> When a successfull transaction was done, show the HTTP statuscode (200, 404, etc.).</p>
<dt><code>-T x</code></p>
<dd> Read the password for website authentication from file &#8216;x&#8217; (instead of entering it on the command line).</p>
<dt><code>-t timeout</code></p>
<dd> How long to wait for answer from the other side.</p>
<dt><code>-U</code></p>
<dd> Enable authentication against website. Set username with -U, set password with -P (or -T to read the password from a file).</p>
<dt><code>-v</code></p>
<dd> Increase verbosity mode. To show standard deviation and dates in output.</p>
<dt><code>-W</code></p>
<dd> Do not abort program if resolving fails.</p>
<dt><code>-X</code></p>
<dd> Use this switch together with &#8216;-G&#8217;. For each &quot;ping&quot; show the amount of data transferred (excluding the headers).</p>
<dt><code>-x proxyhost[:port]</code></p>
<dd> Probe using a proxyserver. Note that you&#8217;re also measuring the latency of the proxyserver!</p>
<dt><code>-Y</code></p>
<dd> Enable colors</p>
<dt><code>-z</code></p>
<dd> When connecting using SSL, display the fingerprint of the X509 certificate(s) of the peer.</p>
<dt><code>&#8211;abbreviate</code></p>
<dd> Abbreviate values bigger than thousand, million, billion, etc.</p>
<dt><code>&#8211;adaptive-interval or &#8211;ai</code></p>
<dd> (Try to) ping on the same interval. E.g. if interval is set to 1.0 seconds and ping a ping t[n] occurs at 500s with duration 250ms, then the next ping (t[n+1]) will happen at 501 seconds and not at 501.25 seconds. Of course when the ping duration is &gt; bigger than the interval, a ping will be &quot;skipped&quot; (not literally: the sequence number will continue) and t[n+1] will then be e.g. 502s instead of the expected 501s. This is useful for example in the ncurses output mode where an fft is calculated over the ping times.</p>
<dt><code>&#8211;aggregates x[,y[,z[,etc.]]]</code></p>
<dd> Show aggregates every x[/y[/z[/etc]]] seconds.</p>
<dt><code>&#8211;divert-connect x</code></p>
<dd> Ignore the hostname in the URL and connect to &#8216;x&#8217; instead. The given URL will be requested at &#8216;x&#8217;.</p>
<dt><code>&#8211;draw-phase</code></p>
<dd> Not only draw the magnitude of the fourier transform, draw the phase as well.</p>
<dt><code>&#8211;graph-limit x</code></p>
<dd> If values measured are bigger than x, then they&#8217;re limitted to x.</p>
<dt><code>&#8211;header x</code></p>
<dd> Add an additional request-header &#8216;x&#8217;.</p>
<dt><code>&#8211;keep-cookies</code></p>
<dd> When the server sends a cookie, it will be returned in the next request.</p>
<dt><code>&#8211;max-mtu x</code></p>
<dd> Maximum MTU to use. Cannot be larger than network interface MTU.</p>
<dt><code>&#8211;no-host-header</code></p>
<dd> Do not put a &quot;Host:&quot;-header in the request header.</p>
<dt><code>&#8211;no-tcp-nodelay</code></p>
<dd> Do not disable &quot;tcp delay&quot; (Naggle).</p>
<dt><code>&#8211;priority x</code></p>
<dd> Set priority of packets.</p>
<dt><code>&#8211;tos x</code></p>
<dd> Set type of service.</p>
<dt><code>&#8211;proxy-user x</code></p>
<dd> Use username &#8216;x&#8217; to authenticate against proxy (http/socks5) server (optional).</p>
<dt><code>&#8211;proxy-password x</code></p>
<dd> Use password &#8216;x&#8217; to authenticate against proxy (http/socks5) server (optional).</p>
<dt><code>&#8211;proxy-password-file x</code></p>
<dd> Read password from file &#8216;x&#8217; to authenticate against proxy (http/socks5) server (optional).</p>
<dt><code>&#8211;recv-buffer x</code></p>
<dd> Set the size of the receive buffer (in bytes).</p>
<dt><code>&#8211;slow-log x</code></p>
<dd> When the duration is x or more, show ping line in the slow log window (the middle window).</p>
<dt><code>&#8211;threshold-red x</code></p>
<dd> If the measured threshold is higher than x (and -Y is given), then the shown value is colored red. If you also use &#8211;threshold-yellow, then this value must be bigger.</p>
<dt><code>&#8211;threshold-yellow x</code></p>
<dd> If the measured threshold is higher than x (and -Y is given), then the shown value is colored yellow.</p>
<dt><code>&#8211;threshold-show x</code></p>
<dd> If the measured threshold is higher than x, then the result is shown (default is show always). The value x is in ms.</p>
<dt><code>&#8211;timestamp or &#8211;ts</code></p>
<dd> Put a timestamp before the result-lines. Use -v to also show a date.</p>
<dt><code>&#8211;tx-buffer x</code></p>
<dd> Set the size of the transmit buffer (in bytes).</p>
<dt><code>-V</code></p>
<dd> Show the version and exit. </p>
</dl>
<h2>OUTPUT</h2>
<p> In split mode (-S) something like &quot;time=0.08+24.09+23.17+15.64+0.02=62.98 ms&quot; is shown. The first value is the time it took to resolve the hostname (or &#8216;n/a&#8217; if it did not resolve in this iteration, e.g. in &quot;resolve once&quot; (-r) mode), then the time it took to connect (or -1 for example in persistent connection (-Q, HTTP v1.1), after that the time it took to put the request on the wire, then the time it took for the HTTP server to process the request and send it back and lastly the time it took to close the connection. </p>
<h2>GRAPH</h2>
<p> The graph in the ncurses uses colors to encode a meaning. Green: value is less than 1 block. Red: the value did not fit in the graph. Blue: the value was limitted by &#8211;graph-limit. Cyan: no measurement for that point in time. </p>
<h2>KEYS</h2>
<p> Press &lt;CTRL&gt; + &lt;c&gt; to exit the program. It will display a summary of what was measured. In the ncurses gui, press &lt;CTRL&gt; + &lt;l&gt; to forcibly redraw the screen. Press &#8216;H&#8217; to halt the graphs (and again to continue). Press &#8216;q&#8217; to stop the program (&lt;CTRL&gt; + &lt;c&gt; will work too). </p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>httping -g <a rel="nofollow" href="http://localhost/">http://localhost/</a></code></p>
<dd> Ping the webserver on host &#8216;localhost&#8217;.</p>
<dt><code>httping -h localhost -p 1000</code></p>
<dd> Ping the webserver on host &#8216;localhost&#8217; and portnumber 1000.</p>
<dt><code>httping -l -g <a rel="nofollow" href="https://localhost/">https://localhost/</a></code></p>
<dd> Ping the webserver on host &#8216;localhost&#8217; using an SSL connection.</p>
<dt><code>httping -g <a rel="nofollow" href="http://localhost/">http://localhost/</a> -U username -P password</code></p>
<dd> Ping the webserver on host &#8216;localhost&#8217; using the Basic HTTP Authentication.</dl>
<h2>BUGS</h2>
<p> None. This program is totally bug-free. </p>
<h2>SEE ALSO</h2>
<p> <code><a rel="nofollow" href="http://www.vanheusden.com/httping/">http://www.vanheusden.com/httping/</a></code> </p>
<h2>NOTES</h2>
<p> This page describes <code>httping</code> as found in the httping-2.3 package; other versions may differ slightly. Please mail corrections and additions to mail [at] vanheusden.com. Report bugs in the program to mail [at] vanheusden.com. Please consider sending bitcoins to 1N5Sn4jny4xVwTwSYLnf7WnFQEGoVRmTQF </p>
<h2>Index</h2>
