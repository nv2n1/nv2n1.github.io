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
<dt>&bull;</dt>
<dd>VOID cache_req_body(BYTES)</dd>
<dt>&bull;</dt>
<dd>VOID collect(HEADER)</dd>
<dt>&bull;</dt>
<dd>DURATION duration(STRING, DURATION)</dd>
<dt>&bull;</dt>
<dd>STRING fileread(PRIV_CALL, STRING)</dd>
<dt>&bull;</dt>
<dd>BOOL healthy(BACKEND)</dd>
<dt>&bull;</dt>
<dd>INT integer(STRING, INT)</dd>
<dt>&bull;</dt>
<dd>IP ip(STRING, IP)</dd>
<dt>&bull;</dt>
<dd>VOID log(STRING_LIST)</dd>
<dt>&bull;</dt>
<dd>INT port(IP)</dd>
<dt>&bull;</dt>
<dd>STRING querysort(STRING)</dd>
<dt>&bull;</dt>
<dd>REAL random(REAL, REAL)</dd>
<dt>&bull;</dt>
<dd>REAL real(STRING, REAL)</dd>
<dt>&bull;</dt>
<dd>TIME real2time(REAL)</dd>
<dt>&bull;</dt>
<dd>VOID rollback(HTTP)</dd>
<dt>&bull;</dt>
<dd>VOID set_ip_tos(INT)</dd>
<dt>&bull;</dt>
<dd>STRING strstr(STRING, STRING)</dd>
<dt>&bull;</dt>
<dd>VOID syslog(INT, STRING_LIST)</dd>
<dt>&bull;</dt>
<dd>TIME time(STRING, TIME)</dd>
<dt>&bull;</dt>
<dd>INT time2integer(TIME)</dd>
<dt>&bull;</dt>
<dd>REAL time2real(TIME)</dd>
<dt>&bull;</dt>
<dd>VOID timestamp(STRING)</dd>
<dt>&bull;</dt>
<dd>STRING tolower(STRING_LIST)</dd>
<dt>&bull;</dt>
<dd>STRING toupper(STRING_LIST)</dd></dl>
<h3>STRING toupper(STRING_LIST)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>STRING toupper(STRING_LIST s)</dd>
<dt><code>Description</code></dt>
<dd>Converts the string <i>s</i> to uppercase.</dd>
<dt><code>Example</code></dt>
<dd>set beresp.http.x-scream = std.toupper(&quot;yes!&quot;);</dd></dl>
<h3>STRING tolower(STRING_LIST)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>STRING tolower(STRING_LIST s)</dd>
<dt><code>Description</code></dt>
<dd>Converts the string <i>s</i> to lowercase.</dd>
<dt><code>Example</code></dt>
<dd>set beresp.http.x-nice = std.tolower(&quot;VerY&quot;);</dd></dl>
<h3>VOID set_ip_tos(INT)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>VOID set_ip_tos(INT tos)</dd>
<dt><code>Description</code></dt>
<dd>Sets the IP type-of-service (TOS) field for the current session to <i>tos</i>. Please note that the TOS field is not removed by the end of the request so probably want to set it on every request should you utilize it.</dd>
<dt><code>Example</code></dt>
<dd>
<pre>if (req.url ~ ^/slow/) {
std.set_ip_tos(0x0);
}</pre>
</dd></dl>
<h3>REAL random(REAL, REAL)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>REAL random(REAL lo, REAL hi)</dd>
<dt><code>Description</code></dt>
<dd>Returns a random real number between <i>lo</i> and <i>hi</i>.</dd>
<dt><code>Example</code></dt>
<dd>set beresp.http.x-random-number = std.random(1, 100);</dd></dl>
<h3>VOID log(STRING_LIST)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>VOID log(STRING_LIST s)</dd>
<dt><code>Description</code></dt>
<dd>Logs the string <i>s</i> to the shared memory log, using VSL tag <i>SLT_VCL_Log</i>.</dd>
<dt><code>Example</code></dt>
<dd>std.log(&quot;Something fishy is going on with the vhost &quot; + req.host);</dd></dl>
<h3>VOID syslog(INT, STRING_LIST)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>VOID syslog(INT priority, STRING_LIST s)</dd>
<dt><code>Description</code></dt>
<dd>Logs the string <i>s</i> to syslog marked with <i>priority</i>. See your system&#8217;s syslog.h file for the legal values of <i>priority</i>.</dd>
<dt><code>Example</code></dt>
<dd>std.syslog(8 + 1, &quot;Something is wrong&quot;);</dd></dl>
<h3>STRING fileread(PRIV_CALL, STRING)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>STRING fileread(PRIV_CALL, STRING)</dd>
<dt><code>Description</code></dt>
<dd>Reads a file and returns a string with the content. Please note that it is not recommended to send variables to this function the caching in the function doesn&#8217;t take this into account. Also, files are not re-read.</dd>
<dt><code>Example</code></dt>
<dd>set beresp.http.x-served-by = std.fileread(&quot;/etc/hostname&quot;);</dd></dl>
<h3>VOID collect(HEADER)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>VOID collect(HEADER hdr)</dd>
<dt><code>Description</code></dt>
<dd>Collapses the header <i>hdr</i>, joining them into one.</dd>
<dt><code>Example</code></dt>
<dd>std.collect(req.http.cookie); </dd>
<p> This will collapse several Cookie: headers into one, long cookie header.</dl>
<h3>DURATION duration(STRING, DURATION)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>DURATION duration(STRING s, DURATION fallback)</dd>
<dt><code>Description</code></dt>
<dd>Converts the string <i>s</i> to seconds. <i>s</i> must be quantified with ms (milliseconds), s (seconds), m (minutes), h (hours), d (days), w (weeks) or y (years) units. If conversion fails, <i>fallback</i> will be returned.</dd>
<dt><code>Example</code></dt>
<dd>set beresp.ttl = std.duration(&quot;1w&quot;, 3600s);</dd></dl>
<h3>INT integer(STRING, INT)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>INT integer(STRING s, INT fallback)</dd>
<dt><code>Description</code></dt>
<dd>Converts the string <i>s</i> to an integer. If conversion fails, <i>fallback</i> will be returned.</dd>
<dt><code>Example</code></dt>
<dd>
<pre>if (std.integer(beresp.http.x-foo, 0) &gt; 5) {
...
}</pre>
</dd></dl>
<h3>IP ip(STRING, IP)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>IP ip(STRING s, IP fallback)</dd>
<dt><code>Description</code></dt>
<dd>Converts the string <i>s</i> to the first IP number returned by the system library function <a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a>(3). If conversion fails, <i>fallback</i> will be returned.</dd>
<dt><code>Example</code></dt>
<dd>
<pre>if (std.ip(req.http.X-forwarded-for, &quot;0.0.0.0&quot;) ~ my_acl) {
...
}</pre>
</dd></dl>
<h3>REAL real(STRING, REAL)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>REAL real(STRING s, REAL fallback)</dd>
<dt><code>Description</code></dt>
<dd>Converts the string <i>s</i> to a real. If conversion fails, <i>fallback</i> will be returned.</dd>
<dt><code>Example</code></dt>
<dd>set req.http.x-real = std.real(req.http.x-foo, 0.0);</dd></dl>
<h3>TIME real2time(REAL)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>TIME real2time(REAL r)</dd>
<dt><code>Description</code></dt>
<dd>Converts the real <i>r</i> to a time.</dd>
<dt><code>Example</code></dt>
<dd>set req.http.x-time = std.real2time(1140618699.00);</dd></dl>
<h3>INT time2integer(TIME)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>INT time2integer(TIME t)</dd>
<dt><code>Description</code></dt>
<dd>Converts the time <i>t</i> to a integer.</dd>
<dt><code>Example</code></dt>
<dd>set req.http.x-int = std.time2integer(now);</dd></dl>
<h3>REAL time2real(TIME)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>REAL time2real(TIME t)</dd>
<dt><code>Description</code></dt>
<dd>Converts the time <i>t</i> to a real.</dd>
<dt><code>Example</code></dt>
<dd>set req.http.x-real = std.time2real(now);</dd></dl>
<h3>BOOL healthy(BACKEND)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>BOOL healthy(BACKEND be)</dd>
<dt><code>Description</code></dt>
<dd>Returns <i>true</i> if the backend <i>be</i> is healthy.</dd></dl>
<h3>INT port(IP)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>INT port(IP ip)</dd>
<dt><code>Description</code></dt>
<dd>Returns the port number of the IP address <i>ip</i>.</dd></dl>
<h3>VOID rollback(HTTP)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>VOID rollback(HTTP h)</dd>
<dt><code>Description</code></dt>
<dd>Restores the <i>h</i> HTTP headers to their original state.</dd>
<dt><code>Example</code></dt>
<dd>std.rollback(bereq);</dd></dl>
<h3>VOID timestamp(STRING)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>VOID timestamp(STRING s)</dd>
<dt><code>Description</code></dt>
<dd>Introduces a timestamp in the log with the current time, using the string <i>s</i> as the label. This is useful to time the execution of lengthy VCL procedures, and makes the timestamps inserted automatically by Varnish more accurate.</dd>
<dt><code>Example</code></dt>
<dd>std.timestamp(&quot;curl-request&quot;);</dd></dl>
<h3>STRING querysort(STRING)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>STRING querysort(STRING)</dd>
<dt><code>Description</code></dt>
<dd>Sorts the query string for cache normalization purposes.</dd>
<dt><code>Example</code></dt>
<dd>set req.url = std.querysort(req.url);</dd></dl>
<h3>VOID cache_req_body(BYTES)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>VOID cache_req_body(BYTES size)</dd>
<dt><code>Description</code></dt>
<dd>Cache the req.body if it is smaller than <i>size</i>. </dd>
<p> Caching the req.body makes it possible to retry pass operations (POST, PUT).</p>
<dt><code>Example</code></dt>
<dd>std.cache_req_body(1KB); </dd>
<p> This will cache the req.body if its size is smaller than 1KB.</dl>
<h3>STRING strstr(STRING, STRING)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>STRING strstr(STRING s1, STRING s2)</dd>
<dt><code>Description</code></dt>
<dd>Returns the first occurrence of the string <i>s2</i> in the string <i>s1</i>, or an empty string if not found. </dd>
<p> Note that the comparison is case sensitive.</p>
<dt><code>Example</code></dt>
<dd>
<pre>if (std.strstr(req.url, req.http.x-restrict)) {
...
}</pre>
</dd></dl>
<h3>TIME time(STRING, TIME)</h3>
<dl>
<dt><code>Prototype</code></dt>
<dd>TIME time(STRING s, TIME fallback)</dd>
<dt><code>Description</code></dt>
<dd>Converts the string <i>s</i> to a time. If conversion fails, <i>fallback</i> will be returned. </dd>
<p> Supported formats: </p>
<pre>&quot;Sun, 06 Nov 1994 08:49:37 GMT&quot;
&quot;Sunday, 06-Nov-94 08:49:37 GMT&quot;
&quot;Sun Nov 6 08:49:37 1994&quot;
&quot;1994-11-06T08:49:37&quot;
&quot;784111777.00&quot;
&quot;784111777&quot;</pre>
<dt><code>Example</code></dt>
<dd>
<pre>if (std.time(resp.http.last-modified, now) &lt; now - 1w) {
...
}</pre>
</dd></dl>
<h2>See Also</h2>
<dl>
<dt>&bull;</dt>
<dd><a href="/docs/linux/man/7-vcl/">vcl</a>(7)</dd>
<dt>&bull;</dt>
<dd><a href="/docs/linux/man/1-varnishd/">varnishd</a>(1)</dd></dl>
<h2>History</h2>
<p>The Varnish standard module was released along with Varnish Cache 3.0. This manual page was written by Per Buer with help from Martin Blix Grydeland.</p>
<h2>Copyright</h2>
<p>This document is licensed under the same licence as Varnish itself. See LICENCE for details.</p>
