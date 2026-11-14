---
title: "vmod_std(3)"
name: "vmod_std"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vmod_std/"
description: "vmod_std – Varnish Standard Module"
---

<p>vmod_std &#8211; Varnish Standard Module</p>
<h2>Synopsis</h2>
<p>import std [from &quot;path&quot;] ;</p>
<h2>Description</h2>
<p>Vmod_std contains basic functions which are part and parcel of Varnish, but which for reasons of architecture fit better in a VMOD. </p>
<p> One particular class of functions in vmod_std is the conversions functions which all have the form: </p>
<pre>TYPE type(STRING, TYPE)</pre>
<p>These functions attempt to convert STRING to the TYPE, and if that fails, they return the second argument, which must have the given TYPE.</p>
<h2>Contents</h2>
<dl>
<dt>&bull;</p>
<dd>VOID cache_req_body(BYTES)</p>
<dt>&bull;</p>
<dd>VOID collect(HEADER)</p>
<dt>&bull;</p>
<dd>DURATION duration(STRING, DURATION)</p>
<dt>&bull;</p>
<dd>STRING fileread(PRIV_CALL, STRING)</p>
<dt>&bull;</p>
<dd>BOOL healthy(BACKEND)</p>
<dt>&bull;</p>
<dd>INT integer(STRING, INT)</p>
<dt>&bull;</p>
<dd>IP ip(STRING, IP)</p>
<dt>&bull;</p>
<dd>VOID log(STRING_LIST)</p>
<dt>&bull;</p>
<dd>INT port(IP)</p>
<dt>&bull;</p>
<dd>STRING querysort(STRING)</p>
<dt>&bull;</p>
<dd>REAL random(REAL, REAL)</p>
<dt>&bull;</p>
<dd>REAL real(STRING, REAL)</p>
<dt>&bull;</p>
<dd>TIME real2time(REAL)</p>
<dt>&bull;</p>
<dd>VOID rollback(HTTP)</p>
<dt>&bull;</p>
<dd>VOID set_ip_tos(INT)</p>
<dt>&bull;</p>
<dd>STRING strstr(STRING, STRING)</p>
<dt>&bull;</p>
<dd>VOID syslog(INT, STRING_LIST)</p>
<dt>&bull;</p>
<dd>TIME time(STRING, TIME)</p>
<dt>&bull;</p>
<dd>INT time2integer(TIME)</p>
<dt>&bull;</p>
<dd>REAL time2real(TIME)</p>
<dt>&bull;</p>
<dd>VOID timestamp(STRING)</p>
<dt>&bull;</p>
<dd>STRING tolower(STRING_LIST)</p>
<dt>&bull;</p>
<dd>STRING toupper(STRING_LIST)</dl>
<h3>STRING toupper(STRING_LIST)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>STRING toupper(STRING_LIST s)</p>
<dt><code>Description</code></p>
<dd>Converts the string <i>s</i> to uppercase.</p>
<dt><code>Example</code></p>
<dd>set beresp.http.x-scream = std.toupper(&quot;yes!&quot;);</dl>
<h3>STRING tolower(STRING_LIST)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>STRING tolower(STRING_LIST s)</p>
<dt><code>Description</code></p>
<dd>Converts the string <i>s</i> to lowercase.</p>
<dt><code>Example</code></p>
<dd>set beresp.http.x-nice = std.tolower(&quot;VerY&quot;);</dl>
<h3>VOID set_ip_tos(INT)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>VOID set_ip_tos(INT tos)</p>
<dt><code>Description</code></p>
<dd>Sets the IP type-of-service (TOS) field for the current session to <i>tos</i>. Please note that the TOS field is not removed by the end of the request so probably want to set it on every request should you utilize it.</p>
<dt><code>Example</code></p>
<dd>
<pre>if (req.url ~ ^/slow/) {
std.set_ip_tos(0x0);
}</pre>
</dl>
<h3>REAL random(REAL, REAL)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>REAL random(REAL lo, REAL hi)</p>
<dt><code>Description</code></p>
<dd>Returns a random real number between <i>lo</i> and <i>hi</i>.</p>
<dt><code>Example</code></p>
<dd>set beresp.http.x-random-number = std.random(1, 100);</dl>
<h3>VOID log(STRING_LIST)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>VOID log(STRING_LIST s)</p>
<dt><code>Description</code></p>
<dd>Logs the string <i>s</i> to the shared memory log, using VSL tag <i>SLT_VCL_Log</i>.</p>
<dt><code>Example</code></p>
<dd>std.log(&quot;Something fishy is going on with the vhost &quot; + req.host);</dl>
<h3>VOID syslog(INT, STRING_LIST)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>VOID syslog(INT priority, STRING_LIST s)</p>
<dt><code>Description</code></p>
<dd>Logs the string <i>s</i> to syslog marked with <i>priority</i>. See your system&#8217;s syslog.h file for the legal values of <i>priority</i>.</p>
<dt><code>Example</code></p>
<dd>std.syslog(8 + 1, &quot;Something is wrong&quot;);</dl>
<h3>STRING fileread(PRIV_CALL, STRING)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>STRING fileread(PRIV_CALL, STRING)</p>
<dt><code>Description</code></p>
<dd>Reads a file and returns a string with the content. Please note that it is not recommended to send variables to this function the caching in the function doesn&#8217;t take this into account. Also, files are not re-read.</p>
<dt><code>Example</code></p>
<dd>set beresp.http.x-served-by = std.fileread(&quot;/etc/hostname&quot;);</dl>
<h3>VOID collect(HEADER)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>VOID collect(HEADER hdr)</p>
<dt><code>Description</code></p>
<dd>Collapses the header <i>hdr</i>, joining them into one.</p>
<dt><code>Example</code></p>
<dd>std.collect(req.http.cookie); </p>
<p> This will collapse several Cookie: headers into one, long cookie header.</dl>
<h3>DURATION duration(STRING, DURATION)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>DURATION duration(STRING s, DURATION fallback)</p>
<dt><code>Description</code></p>
<dd>Converts the string <i>s</i> to seconds. <i>s</i> must be quantified with ms (milliseconds), s (seconds), m (minutes), h (hours), d (days), w (weeks) or y (years) units. If conversion fails, <i>fallback</i> will be returned.</p>
<dt><code>Example</code></p>
<dd>set beresp.ttl = std.duration(&quot;1w&quot;, 3600s);</dl>
<h3>INT integer(STRING, INT)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>INT integer(STRING s, INT fallback)</p>
<dt><code>Description</code></p>
<dd>Converts the string <i>s</i> to an integer. If conversion fails, <i>fallback</i> will be returned.</p>
<dt><code>Example</code></p>
<dd>
<pre>if (std.integer(beresp.http.x-foo, 0) &gt; 5) {
...
}</pre>
</dl>
<h3>IP ip(STRING, IP)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>IP ip(STRING s, IP fallback)</p>
<dt><code>Description</code></p>
<dd>Converts the string <i>s</i> to the first IP number returned by the system library function <a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a>(3). If conversion fails, <i>fallback</i> will be returned.</p>
<dt><code>Example</code></p>
<dd>
<pre>if (std.ip(req.http.X-forwarded-for, &quot;0.0.0.0&quot;) ~ my_acl) {
...
}</pre>
</dl>
<h3>REAL real(STRING, REAL)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>REAL real(STRING s, REAL fallback)</p>
<dt><code>Description</code></p>
<dd>Converts the string <i>s</i> to a real. If conversion fails, <i>fallback</i> will be returned.</p>
<dt><code>Example</code></p>
<dd>set req.http.x-real = std.real(req.http.x-foo, 0.0);</dl>
<h3>TIME real2time(REAL)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>TIME real2time(REAL r)</p>
<dt><code>Description</code></p>
<dd>Converts the real <i>r</i> to a time.</p>
<dt><code>Example</code></p>
<dd>set req.http.x-time = std.real2time(1140618699.00);</dl>
<h3>INT time2integer(TIME)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>INT time2integer(TIME t)</p>
<dt><code>Description</code></p>
<dd>Converts the time <i>t</i> to a integer.</p>
<dt><code>Example</code></p>
<dd>set req.http.x-int = std.time2integer(now);</dl>
<h3>REAL time2real(TIME)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>REAL time2real(TIME t)</p>
<dt><code>Description</code></p>
<dd>Converts the time <i>t</i> to a real.</p>
<dt><code>Example</code></p>
<dd>set req.http.x-real = std.time2real(now);</dl>
<h3>BOOL healthy(BACKEND)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>BOOL healthy(BACKEND be)</p>
<dt><code>Description</code></p>
<dd>Returns <i>true</i> if the backend <i>be</i> is healthy.</dl>
<h3>INT port(IP)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>INT port(IP ip)</p>
<dt><code>Description</code></p>
<dd>Returns the port number of the IP address <i>ip</i>.</dl>
<h3>VOID rollback(HTTP)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>VOID rollback(HTTP h)</p>
<dt><code>Description</code></p>
<dd>Restores the <i>h</i> HTTP headers to their original state.</p>
<dt><code>Example</code></p>
<dd>std.rollback(bereq);</dl>
<h3>VOID timestamp(STRING)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>VOID timestamp(STRING s)</p>
<dt><code>Description</code></p>
<dd>Introduces a timestamp in the log with the current time, using the string <i>s</i> as the label. This is useful to time the execution of lengthy VCL procedures, and makes the timestamps inserted automatically by Varnish more accurate.</p>
<dt><code>Example</code></p>
<dd>std.timestamp(&quot;curl-request&quot;);</dl>
<h3>STRING querysort(STRING)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>STRING querysort(STRING)</p>
<dt><code>Description</code></p>
<dd>Sorts the query string for cache normalization purposes.</p>
<dt><code>Example</code></p>
<dd>set req.url = std.querysort(req.url);</dl>
<h3>VOID cache_req_body(BYTES)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>VOID cache_req_body(BYTES size)</p>
<dt><code>Description</code></p>
<dd>Cache the req.body if it is smaller than <i>size</i>. </p>
<p> Caching the req.body makes it possible to retry pass operations (POST, PUT).</p>
<dt><code>Example</code></p>
<dd><a href="//www.systutorials.com/docs/linux/man/1KB-std.cache_req_body/">std.cache_req_body</a>(1KB); </p>
<p> This will cache the req.body if its size is smaller than 1KB.</dl>
<h3>STRING strstr(STRING, STRING)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>STRING strstr(STRING s1, STRING s2)</p>
<dt><code>Description</code></p>
<dd>Returns the first occurrence of the string <i>s2</i> in the string <i>s1</i>, or an empty string if not found. </p>
<p> Note that the comparison is case sensitive.</p>
<dt><code>Example</code></p>
<dd>
<pre>if (std.strstr(req.url, req.http.x-restrict)) {
...
}</pre>
</dl>
<h3>TIME time(STRING, TIME)</h3>
<dl>
<dt><code>Prototype</code></p>
<dd>TIME time(STRING s, TIME fallback)</p>
<dt><code>Description</code></p>
<dd>Converts the string <i>s</i> to a time. If conversion fails, <i>fallback</i> will be returned. </p>
<p> Supported formats: </p>
<pre>&quot;Sun, 06 Nov 1994 08:49:37 GMT&quot;
&quot;Sunday, 06-Nov-94 08:49:37 GMT&quot;
&quot;Sun Nov 6 08:49:37 1994&quot;
&quot;1994-11-06T08:49:37&quot;
&quot;784111777.00&quot;
&quot;784111777&quot;</pre>
<dt><code>Example</code></p>
<dd>
<pre>if (std.time(resp.http.last-modified, now) &lt; now - 1w) {
...
}</pre>
</dl>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/7-vcl/">vcl</a>(7)</p>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-varnishd/">varnishd</a>(1)</dl>
<h2>History</h2>
<p>The Varnish standard module was released along with Varnish Cache 3.0. This manual page was written by Per Buer with help from Martin Blix Grydeland.</p>
<h2>Copyright</h2>
<p>This document is licensed under the same licence as Varnish itself. See LICENCE for details.</p>
