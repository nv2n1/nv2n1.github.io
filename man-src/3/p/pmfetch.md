---
title: "pmfetch(3)"
name: "pmfetch"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmfetch/"
description: "pmFetch – get performance metric values"
---

<p><code>pmFetch</code> &#8211; get performance metric values</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> </code></p>
<pre>int pmFetch(int <i>numpmid</i>, pmID *<i>pmidlist</i>, pmResult **<i>result</i>);</pre>
<p>cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>Given a list of Performance Metric Identifiers (PMID)s, e.g. as constructed by <code><a href="/docs/linux/man/3-pmlookupname/">pmLookupName</a></code>(3), via <i>pmidlist</i> and <i>numpmid</i>, fetch the values for these performance metrics. </p>
<p> The call to <code>pmFetch</code> is executed in the context of a source of metrics, instance profile and collection time, previously established by calls to the appropriate context and profile functions, namely some of <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3), <code><a href="/docs/linux/man/3-pmdupcontext/">pmDupContext</a></code>(3), <code><a href="/docs/linux/man/3-pmusecontext/">pmUseContext</a></code>(3), <code><a href="/docs/linux/man/3-pmaddprofile/">pmAddProfile</a></code>(3), <code><a href="/docs/linux/man/3-pmdelprofile/">pmDelProfile</a></code>(3) and <code><a href="/docs/linux/man/3-pmsetmode/">pmSetMode</a></code>(3). </p>
<p> The principal result from <code>pmFetch</code> is returned in the argument <i>result</i> as a tree, using the following component data structures; </p>
<pre>typedef struct {
 unsigned int vtype : 8; /* value type (same as pmDesc.type) */
 unsigned int vlen : 24; /* bytes for vtype/vlen + vbuf */
 char vbuf[1]; /* one or more values */
} pmValueBlock;
typedef struct {
 int inst; /* instance identifier */
 union {
 pmValueBlock *pval; /* pointer to value-block */
 int lval; /* integer value insitu */
 } value;
} pmValue;
typedef struct {
 pmID pmid; /* metric identifier */
 int numval; /* number of values or error code */
 int valfmt; /* value style, insitu or ptr */
 pmValue vlist[1]; /* set of instances/values */
} pmValueSet;
/* Result returned by pmFetch() */
typedef struct {
 struct timeval timestamp; /* time stamped by collector */
 int numpmid; /* number of PMIDs */
 pmValueSet *vset[1]; /* set of value sets */
} pmResult;</pre>
<p>To accommodate metrics with multiple value instances, the <i>numval</i> field indicates how many values are returned for each requested PMID. The field <i>valfmt</i> in the <i>pmValueSet</i> structure indicates if the values for this metric are stored <i>insitu</i> in the <i>lval</i> field, i.e. a 32-bit integer quantity (either int, unsigned int, long or unsigned long) or if the values are held in associated <i>pmValueBlock</i> structures. The <i>pmValueBlock</i> structure is always used for floating point values (float or double) and also accommodates arbitrary sized binary data such as `string-valued&#8217; metrics and metrics with aggregated or complex data types. The maximum length of a <i>pmValueBlock</i> buffer is <code>PM_VAL_VLEN_MAX</code> bytes. If the <i>pmValueBlock</i> format is used, the <i>vtype</i> field indicates the data type of the value. This field has the same interpretation as the <i>type</i> field in the <code>pmDesc</code> structure, see <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3). </p>
<p> Note that the insitu value may be a signed or unsigned 32 bit integer, signed or unsigned 32 bit long value (on 32 bit platforms), In the special cases described below, it may also be a 32 bit floating point value. If the application needs to know the type of an insitu value, which is almost always the case, it is necessary to fetch the descriptor for the metric and interpret the <code>type</code> field, as described in detail in <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3). When the <i>pmResult</i> is received from a PCP1.x <code>pmcd</code>, insitu values may also be 32 bit floating point values (of type <code>PM_TYPE_FLOAT</code>). In all cases, it is good practice to use <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3) to fetch the descriptor for the metric and interpret the <code>type</code> field therein. Note also that the <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) will automatically translate from the PCP2.0 format to the PCP1.x format when a PCP1.x client requests 32 bit floating point values from a PCP2.0 <code>pmcd</code>, but the reverse translation does not occur (because the PCP2.0 <code>pmcd</code> cannot automatically distinguish between arbitrary 32 bit floating point values and 32 bit integers). </p>
<p> If one value (i.e. associated with a particular instance) for a requested metric is `unavailable&#8217; (at the requested time), then there is no associated <i>pmValue</i> structure in the <i>result</i>. If there are no available values for a metric, then <i>numval</i> will be zero and the associated <i>pmValue[]</i> instance will be empty ( <i>valfmt</i> is undefined in these circumstances, however <i>pmid</i> will be correctly set to the PMID of the metric with no values). </p>
<p> As an extension of this protocol, if the Performance Metrics Collection System (PMCS) is able to provide a reason why no values are available for a particular metric, this is encoded as a standard error code in the corresponding <i>numval</i>. Since the error codes are all negative, values for a requested metric are `unavailable&#8217; if <i>numval</i> is less than, or equal to, zero. A performance metric&#8217;s value may be `unavailable&#8217; for a number of reasons; the following list is illustrative but not exhaustive: of the software for the associated Performance Metric Domain</p>
<dl>
<dt>+</p>
<dd>Collection is not currently activated in the software for the associated Performance Metric Domain</p>
<dt>+</p>
<dd>The associated PMID is not known</p>
<dt>+</p>
<dd>The current system configuration does not include the associated hardware component and/or the associated software module, e.g. a disk is not installed, or off-line, or Oracle is not installed</p>
<dt>+</p>
<dd>The metric is one for which an instance profile is required, and none was provided (there are a small number of metrics in this category, typically ones with very large, and/or very dynamic instance domains, and/or expensive metric instantiation methods).</p>
<dt>+</p>
<dd>If the current context involves fetching metrics from an archive log, values may be unavailable in the region around a <i>&lt;mark&gt;</i> record (see <code><a href="/docs/linux/man/1-pmlogextract/">pmlogextract</a></code>(1)) that indicate a temporal discontinuity in the time-series of metric values.</dl>
<p> In general, we may not be able to differentiate between the various cases, and if differentiation is not possible, <i>numval</i> will simply be zero. </p>
<p> The argument definition and the result specifications have been constructed to ensure that for each PMID in the requested <i>pmidlist</i> there is exactly one <i>pmValueSet</i> in the <i>result</i>, and further the PMIDs appear in exactly the same sequence in both <i>pmidlist</i> and <i>result</i>. This makes the number and order of entries in <i>result</i> completely deterministic, and greatly simplifies the application programming logic after the call to <code>pmFetch</code>. </p>
<p> The <i>result</i> structure returned by <code>pmFetch</code> is dynamically allocated using a combination of <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) calls and specialized allocation strategies, and should be released when no longer required by calling <code><a href="/docs/linux/man/3-pmfreeresult/">pmFreeResult</a></code>(3) &#8211; under no circumstances should <code><a href="/docs/linux/man/3-free/">free</a></code>(3) be called directly to release this space. </p>
<p> As common error conditions are encoded in the <i>result</i> data structure, we&#8217;d expect only cataclysmic events to cause an error value to be returned. One example would be if the metrics source context was a remote host, and that host or the PMCS on that host became unreachable. Otherwise the value returned by the <code>pmFetch</code> function will be non-negative. </p>
<p> If the current context involves fetching metrics from a Performance Metrics Collector Daemon (PMCD), then the return value may be used to encode out-of-band changes in the state of the PMCD and the associated Performance Metrics Daemon Agents (PMDAs), as a bit-wise &#8220;or&#8221; of the following values: </p>
<dl>
<dt><code>PMCD_RESTART_AGENT</code></p>
<dd>An attempt has been made to restart at least one failed PMDA.</p>
<dt><code>PMCD_ADD_AGENT</code></p>
<dd>At least one PMDA has been started.</p>
<dt><code>PMCD_DROP_AGENT</code></p>
<dd>PMCD has noticed the termination of at least one PMDA.</dl>
<p> The default is to return zero to indicate no change in state, however the <i>pmResult</i> returned by <code>pmFetch</code> has the same interpretation independent of the return value being zero or greater than zero.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/3-pmaddprofile/">pmAddProfile</a></code>(3), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmdelprofile/">pmDelProfile</a></code>(3), <code><a href="/docs/linux/man/3-pmdupcontext/">pmDupContext</a></code>(3), <code><a href="/docs/linux/man/3-pmextractvalue/">pmExtractValue</a></code>(3), <code><a href="/docs/linux/man/3-pmfetcharchive/">pmFetchArchive</a></code>(3), <code><a href="/docs/linux/man/3-pmfreeresult/">pmFreeResult</a></code>(3), <code><a href="/docs/linux/man/3-pmgetindom/">pmGetInDom</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupname/">pmLookupName</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3), <code><a href="/docs/linux/man/3-pmsetmode/">pmSetMode</a></code>(3), <code><a href="/docs/linux/man/3-pmusecontext/">pmUseContext</a></code>(3) and <code><a href="/docs/linux/man/3-pmwhichcontext/">pmWhichContext</a></code>(3). </p>
<p> Note that <code>pmFetch</code> is the most primitive method of fetching metric values from the PMCS. See the <code><a href="/docs/linux/man/3-pmfetchgroup/">pmFetchGroup</a></code>(3) API for a higher level method that insulates the user from the intricacies of looking up metric names and metadata, setting up instance profiles, <i>pmResult</i> traversal, conversions, and scaling.</p>
<h2>Diagnostics</h2>
<p>As mentioned above, <code>pmFetch</code> returns error codes <i>insitu</i> in the argument <i>result</i>. If no result is returned, e.g. due to IPC failure using the current PMAPI context, or end of file on an archive log, then <code>pmFetch</code> will return a negative error code which may be examined using <code><a href="/docs/linux/man/3-pmerrstr/">pmErrStr</a></code>(3).</p>
<dl>
<dt><code>PM_ERR_EOL</code></p>
<dd>When fetching records from an archive log, <code>pmFetch</code> returns this error code to indicate the end of the log has been passed (or the start of the log has been passed, if the direction of traversal is backwards in time). If the &#8220;mode&#8221; for the current PMAPI context (see <code><a href="/docs/linux/man/3-pmsetmode/">pmSetMode</a></code>(3)) is <code>PM_MODE_INTERP</code> then the time origin is advanced, even when this error code is returned. In this way applications that position the time outside the range defined by the records in the archive, and then commence to <code>pmFetch</code> will eventually see valid results once the time origin moves inside the temporal span of the archive.</dl>
<h2>Environment</h2>
<p>Many of the performance metrics exported from PCP agents have the semantics of <i>counter</i> meaning they are expected to be monotonically increasing. Under some circumstances, one value of these metrics may be smaller than the previously fetched value. This can happen when a counter of finite precision overflows, or when the PCP agent has been reset or restarted, or when the PCP agent is exporting values from some underlying instrumentation that is subject to some asynchronous discontinuity. </p>
<p> The environment variable <code>PCP_COUNTER_WRAP</code> may be set to indicate that all such cases of a decreasing &#8220;counter&#8221; should be treated as a counter overflow, and hence the values are assumed to have wrapped once in the interval between consecutive samples. This &#8220;wrapping&#8221; behavior was the default in earlier PCP versions, but by default has been disabled in PCP version 1.3 and later.</p>
