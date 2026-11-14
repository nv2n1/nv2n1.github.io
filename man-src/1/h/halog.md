---
title: "halog(1)"
name: "halog"
section: "1"
letter: "h"
url: "/docs/linux/man/1-halog/"
description: "halog – HAProxy log statistics reporter"
---

<h2>NAME</h2>
<p> halog &#8211; HAProxy log statistics reporter</p>
<h2>SYNOPSIS</h2>
<p> <code>halog</code> [<i>-h|&#8211;help</i>]<br />
 <code>halog</code> [<i>options</i>] &lt;LOGFILE</p>
<h2>DESCRIPTION</h2>
<p> <code>halog</code> reads HAProxy log data from stdin and extracts and displays lines matching user-specified criteria.</p>
<h2>OPTIONS</h2>
<h3>Input filters (several filters may be combined)</h3>
<dl>
<dt><code>-H</code></p>
<dd> Only match lines containing HTTP logs (ignore TCP)</p>
<dt><code>-E</code></p>
<dd> Only match lines without any error (no 5xx status)</p>
<dt><code>-e</code></p>
<dd> Only match lines with errors (status 5xx or negative)</p>
<dt><code>-rt</code>|<code>-RT</code> &lt;time&gt;</p>
<dd> Only match response times larger|smaller than &lt;time&gt;</p>
<dt><code>-Q</code>|<code>-QS</code></p>
<dd> Only match queued requests (any queue|server queue)</p>
<dt><code>-tcn</code>|<code>-TCN</code> &lt;code&gt;</p>
<dd> Only match requests with/without termination code &lt;code&gt;</p>
<dt><code>-hs</code>|<code>-HS</code> &lt;[min][:][max]&gt;</p>
<dd> Only match requests with HTTP status codes within/not within min..max. Any of them may be omitted. Exact code is checked for if no &#8216;:&#8217; is specified.</dl>
<h3>Modifiers</h3>
<dl>
<dt><code>-v</code></p>
<dd> Invert the input filtering condition</p>
<dt><code>-q</code></p>
<dd> Don&#8217;t report errors/warnings</p>
<dt><code>-m</code> &lt;lines&gt;</p>
<dd> Limit output to the first &lt;lines&gt; lines</dl>
<h3>Output filters &#8211; only one may be used at a time</h3>
<dl>
<dt><code>-c</code></p>
<dd> Only report the number of lines that would have been printed</p>
<dt><code>-pct</code></p>
<dd> Output connect and response times percentiles</p>
<dt><code>-st</code></p>
<dd> Output number of requests per HTTP status code</p>
<dt><code>-cc</code></p>
<dd> Output number of requests per cookie code (2 chars)</p>
<dt><code>-tc</code></p>
<dd> Output number of requests per termination code (2 chars)</p>
<dt><code>-srv</code></p>
<dd> Output statistics per server (time, requests, errors)</p>
<dt><code>-u</code>*</p>
<dd> Output statistics per URL (time, requests, errors)<br />
 Additional characters indicate the output sorting key:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-u</code></p>
<dd> URL</p>
<dt><code>-uc</code></p>
<dd> Request count</p>
<dt><code>-ue</code></p>
<dd> Error count</p>
<dt><code>-ua</code></p>
<dd> Average response time</p>
<dt><code>-ut</code></p>
<dd> Average total time</p>
<dt><code>-uao</code>, <code>-uto</code></p>
<dd> Average times computed on valid (&#8216;OK&#8217;) requests</p>
<dt><code>-uba</code></p>
<dd> Average bytes returned</p>
<dt><code>-ubt</code></p>
<dd> Total bytes returned</dl>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-haproxy/">haproxy</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>halog</code> was written by Willy Tarreau &lt;w@1wt.eu&gt; and is part of <code><a href="/docs/linux/man/1-haproxy/">haproxy</a></code>(1). </p>
<p> This manual page was written by Apollon Oikonomopoulos &lt;apoikos [at] gmail.com&gt; for the Debian project (but may be used by others). </p>
<h2>Index</h2>
