---
title: "pmgetversion(3)"
name: "pmgetversion"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmgetversion/"
description: "pmGetVersion – fetch installed PCP version number"
---

<p><code>pmGetVersion</code> &#8211; fetch installed PCP version number</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmGetVersion(void); </p>
<p> cc &#8230; -lpcp </code></p>
<h2>Description</h2>
<p><code>pmGetVersion</code> returns a binary encoding of the locally installed PCP version number. </p>
<p> This may be used in conjunction with the related macros <code>PM_VERSION</code>(a,b,c) and <code>PM_VERSION_CURRENT</code> that generate PCP version numbers in the same format. Refer to the example below. </p>
<p> The encoding uses one byte for each of the parts of the version number of the installed PCP package, namely the major number, the minor number and the revision number. So PCP version 3.10.5 is encoded as 0x30a05. </p>
<p> The string format of the installed PCP package version number as also available from <code>pmGetConfig</code> with the argument <code>PCP_VERSION</code>. </p>
<p> <code>pmGetVersion</code> was introduced in PCP 3.10.5.</p>
<h2>Example</h2>
<p>The following C fragment demonstrates the use of both the compile-time macros and the run-time <code>pmGetVersion</code> function for an application that should not be built for PCP versions older than 3.10.5, but after that there are two alternative implementations with a newer (faster, sweeter, smaller) variant of the XYZ service that only becoming available in PCP 4.0.0. </p>
<pre><code>#include &lt;pcp/pmapi.h&gt;

#ifdef PM_VERSION_CURRENT
#if PM_VERSION_CURRENT &lt; PM_VERSION(3, 10, 5)
/* no pmGetVersion() before PCP 3.10.5 */
printf(&quot;PCP version 0x%x too old
&quot;, PM_VERSION_CURRENT);
#endif
version = pmGetVersion();
    if (version &gt;= PM_VERSION(4,0,0) {
    /* V2 of the XYZ service introduced in PCP 4.0.0 */
    printf(&quot;Using V2 of service XYZ
&quot;)...
    }
    else {
        printf(&quot;Using V1 of service XYZ
&quot;)
        ...
    }
#else
{
    char *ver = pmGetConfig(&quot;PCP_VERSION&quot;);
    /* only option is to extract version number from returned string */
    ...
}
#endif</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), and <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3).</p>
<h2>Diagnostics</h2>
<p>None.</p>
