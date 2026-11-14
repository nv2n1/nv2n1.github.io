---
title: "pmdainit(3)"
name: "pmdainit"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdainit/"
description: "pmdaInit, pmdaRehash, pmdaSetFlags – initialize a PMDA"
---

<p><code>pmdaInit</code>, <code>pmdaRehash</code>, <code>pmdaSetFlags</code> &#8211; initialize a PMDA</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/pmda.h&gt; </p>
<p> void pmdaInit(pmdaInterface *</code><i>dispatch</i>, pmdaIndom *<i>indoms</i>, int&nbsp;<wbr><i>nindoms</i>, pmdaMetric&nbsp;<wbr>*<i>metrics</i>, int&nbsp;<wbr><i>nmetrics</i>); </p>
<p> void pmdaRehash(pmdaExt *<i>pmda</i>, pmdaMetric&nbsp;<wbr>*<i>metrics</i>, int&nbsp;<wbr><i>nmetrics</i>); </p>
<p> void pmdaSetFlags(pmdaInterface *<i>dispatch</i>, int <i>flags</i>); </p>
<p> cc &#8230; -lpcp_pmda -lpcp</p>
<h2>Description</h2>
<p><code>pmdaInit</code> initializes a PMDA so that it is ready to receive PDUs from <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1). The function expects as arguments the instance domain table (<i>indoms</i>) and the metric description table (<i>metrics</i>) that are initialized by the PMDA. The arguments <i>nindoms</i> and <i>nmetrics</i> should be set to the number of instances and metrics in the tables, respectively. </p>
<p> Much of the <code>pmdaInterface</code> structure can be automatically initialized with <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3), <code><a href="/docs/linux/man/3-pmdagetopt/">pmdaGetOpt</a></code>(3) and <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3). <code>pmdaInit</code> completes the PMDA initialization phase with three operations. The first operation adds the domain and instance numbers to the instance and metric tables. Singular metrics (metrics without an instance domain) should have the instance domain <code>PM_INDOM_NULL</code> set in the <i>indom</i> field of the <code>pmDesc</code> structure (see <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3)). Metrics with an instance domain should set this field to be the serial number of the instance domain in the <i>indoms</i> table. </p>
<p> The instance domain table may be made empty by setting <i>indoms</i> to NULL and <i>nindoms</i> to 0. This allows the caller to provide custom Fetch and Instance callback functions. The metric table may be made empty by setting <i>metrics</i> to NULL and <i>nmetrics</i> to 0. This allows the caller to provide custom Fetch and Descriptor callback functions.</p>
<h2>Example</h2>
<p>For example, a PMDA has three metrics: A, B and C, and two instance domains X and Y, with two instances in each instance domain. The instance domain and metrics description tables could be defined as: </p>
<pre><code>static pmdaInstid _X[] = {
    {0, &quot;X1&quot;}, {1, &quot;X2&quot;}};

static pmdaInstid _Y[] = {
    {0, &quot;Y1&quot;}, {1, &quot;Y2&quot;}};

static pmdaIndom indomtab[] = {
#define X_INDOM 0
    {X_INDOM, 2, _X},
#define Y_INDOM 3
    {Y_INDOM, 2, _Y}};

static pmdaMetric metrictab[] = {
    /* A */
    {
        (void *)0,
        {PMDA_PMID(0, 0), PM_TYPE_U32, PM_INDOM_NULL, PM_SEM_INSTANT, {0, 0, 0, 0, 0, 0}},
    },
    /* B */
    {
        (void *)0,
        {PMDA_PMID(0, 1), PM_TYPE_U32, X_INDOM, PM_SEM_INSTANT, {0, 0, 0, 0, 0, 0}},
    },
    /* C */
    {
        (void *)0,
        {PMDA_PMID(0, 2), PM_TYPE_DOUBLE, Y_INDOM, PM_SEM_INSTANT, {0, 1, 0, 0, PM_TIME_SEC, 0}},
    }};</code></pre>
<p> The metric description table defines metric A with no instance domain, metric B with instance domain X and metric C with instance domain Y. Metric C has units of seconds, while the other metrics have no units (simple counters). <code>pmdaInit</code> will take these structures and assign the <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3) domain number to the <i>it_indom</i> field of each instance domain. This identifier also replaces the <i>indom</i> field of all metrics which have that instance domain, so that they are correctly associated. The second stage opens the help text file, if one was specified with the <code>-h</code> command line option (see <code><a href="/docs/linux/man/3-pmdagetopt/">pmdaGetOpt</a></code>(3)) or as a <i>helptext</i> argument to <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) or <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3). The final stage involves preparing the metric table lookup strategy.</p>
<h2>Metric Lookup</h2>
<p>When fetch and descriptor requests are made of the PMDA, each requested PMID must be mapped to a metric table entry. There are currently three strategies for performing this mapping &#8211; direct, linear and hashed. Each has its own set of tradeoffs and an appropriate strategy should be selected for each PMDA. </p>
<p> If all of the metric PMID item numbers correspond to the position in the <i>metrics</i> table, then direct mapping is used. This is the most efficient of the lookup functions as it involves a direct array index (no additional memory is required nor any additional processing overhead). If the PMID numbering requirement is met by the PMDA, it is ideal. This strategy can be explicitly requested by calling <code>pmdaSetFlags</code>(<i>pmda</i>, <i>PMDA_FLAG_EXT_DIRECT</i>) before calling <code>pmdaInit</code>. In this case, if the direct mapping is not possible (e.g. due to an oversight on the part of the PMDA developer), a warning is logged and the linear strategy is used instead. </p>
<p> The second strategy (linear search) is the default, when a direct mapping cannot be established. This provides greater flexibility in the PMID numbering scheme, as the PMDA item numbers do not have to be unique (hence, the PMID cluster numbers can be used more freely, which is often extremely convenient for the PMDA developer). However, lookup involves a linear walk from the start of the metric table until a matching PMID is found, for each requested PMID in a request. </p>
<p> The third strategy (hash lookup) can be requested by calling <code>pmdaSetFlags</code>(<i>pmda</i>, <i>PMDA_FLAG_EXT_HASHED</i>) before calling <code>pmdaInit</code>. This strategy is most useful for PMDAs with large numbers of metrics (many hundreds, or thousands). Such PMDAs will almost always use the cluster numbering scheme, so the direct lookup scheme becomes inappropriate. They may also be prepared to sacrifice a small amount of additional memory for a hash table, mapping PMID to metric table offsets, to speed up lookups in their vast metric tables. </p>
<p> This final strategy can also be used by PMDAs serving up dynamically numbered metrics. For this case, the <code>pmdaRehash</code> function should be used to replace the metric table when new metrics become available, or existing metrics are removed. The PMID hash mapping will be recomputed at the same time that the new metric table is installed.</p>
<h2>Diagnostics</h2>
<p><code>pmdaInit</code> will set <i>dispatch-&gt;status</i> to a value less than zero if there is an error that would prevent the <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3) from successfully running. <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) will terminate the connection to the <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3) if this occurs. </p>
<p> <code>pmdaInit</code> may issue any of these messages:</p>
<dl>
<dt><code>PMDA interface version </code><i>interface</i><code> not supported</code></p>
<dd>The <i>interface</i> version is not supported by <code>pmdaInit</code>.</p>
<dt><code>Using pmdaFetch() but fetch call back not set</code></p>
<dd>The fetch callback, <code><a href="/docs/linux/man/3-pmdafetch/">pmdaFetch</a></code>(3), requires an additional callback to be provided using <code><a href="/docs/linux/man/3-pmdasetfetchcallback/">pmdaSetFetchCallBack</a></code>(3).</p>
<dt><code>Illegal instance domain </code><i>inst</i><code> for metric </code><i>pmid</i></p>
<dd>The instance domain <i>inst</i> that was specified for metric <i>pmid</i> is not within the range of the instance domain table.</p>
<dt><code>No help text path specified</code></p>
<dd>The help text callback, <code><a href="/docs/linux/man/3-pmdatext/">pmdaText</a></code>(3), requires a help text file for the metrics to have been opened, however no path to the help text was specified as a command line option, or as an argument to <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) or <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3). This message is only a warning.</p>
<dt><code>Direct mapping for metrics disabled @ </code><i>num</i></p>
<dd>The unit numbers of the metrics did not correspond to the index in the metric description table. The direct mapping failed for metric number <i>num</i> in the <i>metrics</i> table. This is less efficient but is not fatal and the message is only a warning.</p>
<dt><code>Hashed mapping for metrics disabled @ </code><i>num</i></p>
<dd>A memory allocation failure occurred while building the hash table to index the metric description table. This is a non-fatal warning message &#8211; a fallback to linear searching will be automatically performed should this situation arise.</dl>
<h2>Caveat</h2>
<p>The PMDA must be using <code>PMDA_INTERFACE_2 </code> or later, as specified in the call to <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) or <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-newhelp/">newhelp</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3), <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3), <code><a href="/docs/linux/man/3-pmdafetch/">pmdaFetch</a></code>(3), <code><a href="/docs/linux/man/3-pmdagetopt/">pmdaGetOpt</a></code>(3), <code><a href="/docs/linux/man/3-pmdatext/">pmdaText</a></code>(3) and <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3). </p>
