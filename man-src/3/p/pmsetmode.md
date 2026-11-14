---
title: "pmsetmode(3)"
name: "pmsetmode"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmsetmode/"
description: "pmSetMode – set collection time parameters for the current PMAPI context"
---

<p><code>pmSetMode</code> &#8211; set collection time parameters for the current PMAPI context</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmSetMode(int </code><i>mode</i>, const struct timeval *<i>when</i>, int <i>delta</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p><code>pmSetMode</code> is used to define the collection time and/or mode for accessing performance metrics and meta-data in the current Performance Metrics Application Programming Interface (PMAPI) context. This mode affects the semantics of subsequent calls to the following PMAPI routines: <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3), <code><a href="/docs/linux/man/3-pmfetcharchive/">pmFetchArchive</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3), <code><a href="/docs/linux/man/3-pmgetindom/">pmGetInDom</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupindom/">pmLookupInDom</a></code>(3) and <code><a href="/docs/linux/man/3-pmnameindom/">pmNameInDom</a></code>(3). </p>
<p> If <i>mode</i> is <code>PM_MODE_LIVE</code> then all information is returned from the active pool of performance metrics as of the time that the PMAPI call is made, and the other two parameters to <code>pmSetMode</code> are ignored. <code>PM_MODE_LIVE</code> is the default mode when a new PMAPI context of type <code>PM_CONTEXT_HOST</code> is created. </p>
<p> If the <i>mode</i> is not <code>PM_MODE_LIVE</code>, then the <i>when</i> parameter defines a time origin, and all requests for meta-data (metric descriptions and instance identifiers from the instance domains) will be processed to reflect the state of the meta-data as of the time origin, i.e. we use the last state of this information at, or before, the time origin. </p>
<p> If the <i>mode</i> is <code>PM_MODE_INTERP</code> then, in the case of <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3), the underlying code will use an interpolation scheme to compute the values of the metrics from the values recorded for times in the proximity of the time origin. A <i>mode</i> of <code>PM_MODE_INTERP</code> may only be used with an archive context. </p>
<p> If the <i>mode</i> is <code>PM_MODE_FORW</code> then, in the case of <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3), the collection of recorded metric values will be scanned in a forwards direction in time, until values for at least one of the requested metrics is located after the time origin, and then all requested metrics stored in the set of archives at that time will be returned with the corresponding timestamp. A <i>mode</i> of <code>PM_MODE_FORW</code> may only be used with an archive context. </p>
<p> If the <i>mode</i> is <code>PM_MODE_BACK</code> then, the situation is the same as for <code>PM_MODE_FORW</code>, except a <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3) will be serviced by scanning the collection of recorded metrics in a backwards direction in time for metrics before the time origin. A <i>mode</i> of <code>PM_MODE_BACK</code> may only be used with an archive context. </p>
<p> If the <i>mode</i> is <code>PM_MODE_FORW</code> or <code>PM_MODE_BACK</code>, and no qualifying metrics can be found in the requested direction of searching before the end or start of the set of archive logs is found, then <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3) returns the special error indicator, <code>PM_ERR_EOL</code>. </p>
<p> For <i>mode</i>s other than <code>PM_MODE_LIVE</code>, after each successful <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3), the time origin is reset to the timestamp returned via the <i>pmResult</i> structure from <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3). </p>
<p> The <code>pmSetMode</code> parameter <i>delta</i> defines an additional number of time units that should be used to adjust the time origin (forwards or backwards), after the new time origin from the <i>pmResult</i> has been determined. This automatic adjustment of the time origin only occurs when the <i>mode</i> is <code>PM_MODE_INTERP</code>, and the adjustment is applied, even if the <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3) fails because the time origin is outside the range defined by the records in a set of archive logs, i.e. returns <code>PM_ERR_EOL</code>. </p>
<p> By default <i>delta</i> is interpreted as milliseconds (but see the LARGE DELTA VALUES section below). </p>
<p> Using these <i>mode</i> options, an application can implement replay, playback, fast forward, reverse, etc. for performance metric values held in the set of archive logs by alternating calls to <code>pmSetMode</code> and <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3). </p>
<p> As a special case, if <i>when</i> is <code>NULL</code> then the <i>mode</i> and <i>delta</i> arguments are used as described above, but the current time in the archive is not altered.</p>
<h2>Examples</h2>
<p>The following code fragment may be used to dump just those values recorded in an archive in correct temporal sequence, for a selected set of performance metrics; this uses the default collection time mechanisms. </p>
<pre><code>pmNewContext(PM_CONTEXT_ARCHIVE, &quot;myarchive&quot;);
while (pmFetch(npmid, pmidlist, &amp;result) != PM_ERR_EOL) {
    /*
     * process real metric values as of result-&gt;timestamp
     */
    ...pmFreeResult(result);
}</code></pre>
<p> Alternatively, to replay interpolated metrics from the log in reverse chronological order, at 10 second intervals (of recorded time), the following code fragment could be used. </p>
<pre><code>struct timeval mytime;

mytime.tv_sec = 0x7fffffff; /* or use pmGetArchiveEnd(&amp;mtime) */
pmSetMode(PM_MODE_BACK, &amp;mytime, 0);
pmFetchArchive(&amp;result);
mytime = result-&gt;timestamp;
pmFreeResult(result);
pmSetMode(PM_MODE_INTERP | PM_XTB_SET(PM_TIME_SEC), &amp;mytime, -10);

while (pmFetch(numpmid, pmidlist, &amp;result) != PM_ERR_EOL) {
    /*
     * process interpolated metric values as of
     * result-&gt;timestamp
     */
    ...pmFreeResult(result);
}</code></pre>
<h2>Large Delta Values</h2>
<p>Because <i>delta</i> is an <i>int</i> and treated as milliseconds by default there is a limit on the maximum absolute value of <i>delta</i> that can be specified with this default interpretation, namely about 24 days if a signed <i>int</i> has 31 bits of precision. To accommodate longer values of <i>delta</i> the high-order bits of the <i>mode</i> parameter is also used to optionally set the units of time for the <i>delta</i> parameter. To specify the units of time use the <code>PM_XTB_SET </code> macro with one of the values <code>PM_TIME_NSEC</code>, <code>PM_TIME_MSEC</code>, <code>PM_TIME_SEC</code>, etc. to set the <i>mode</i> as follows: </p>
<p> PM_MODE_INTERP | PM_XTB_SET(PM_TIME_XXXX) </p>
<p> The following code shows how this could be done if the desired <i>delta</i> is initially encoded in <i>interval</i> (a struct timeval). </p>
<pre>struct timeval interval;
int mode;
mode = ...
if (abs(interval.tv_sec / (3600*24)) &lt;= 24) {
 /* default encoding of milliseconds is fine */
 mode = PM_MODE_INTERP;
 delta = interval.tv_sec * 1000 + (interval.tv_usec + 500)/ 1000;
}
else {
 /* encode delta in units of seconds */
 mode = PM_MODE_INTERP | PM_XTB_SET(PM_TIME_SEC);
 delta = interval.tv_sec + (interval.tv_usec + 500000)/ 1000000;
}</pre>
<p>For millisecond encoding of <i>delta</i>, using <code>PM_XTB_SET(PM_TIME_MSEC)</code> is functionally equivalent to not using <code>PM_XTB_SET</code> at all.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3), <code><a href="/docs/linux/man/3-pmfetcharchive/">pmFetchArchive</a></code>(3), <code><a href="/docs/linux/man/3-pmgetindom/">pmGetInDom</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupindom/">pmLookupInDom</a></code>(3) and <code><a href="/docs/linux/man/3-pmnameindom/">pmNameInDom</a></code>(3).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_MODE</code></p>
<dd>The <i>mode</i> parameter is invalid </p>
</dl>
