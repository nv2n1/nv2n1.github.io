---
title: "pmdafetch(3)"
name: "pmdafetch"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdafetch/"
description: "pmdaFetch, pmdaSetFetchCallBack – fill a pmResult structure with the requested metric values"
---

<p><code>pmdaFetch</code>, <code>pmdaSetFetchCallBack</code> &#8211; fill a pmResult structure with the requested metric values</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/pmda.h&gt; </p>
<p> int pmdaFetch(int </code><i>numpmid</i>, pmID *<i>pmidlist</i>, pmResult **<i>resp</i>, pmdaExt&nbsp;<wbr>*<i>pmda</i>); </p>
<p> void pmdaSetFetchCallBack(pmdaInterface *<i>dispatch</i>, pmdaFetchCallBack&nbsp;<wbr><i>callback</i>); </p>
<p> cc &#8230; -lpcp_pmda -lpcp</p>
<h2>Description</h2>
<p><code>pmdaFetch</code> is a generic callback used by a <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3) to process a fetch request from <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1). The request from <code>pmcd</code> is initiated by a client calling <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3). </p>
<p> This is the only generic callback in <i>libpcp_pmda</i> (see <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3)) that is incomplete, requiring a further <code>pmdaFetchCallBack</code> method of its own. The additional callback should be registered using <code>pmdaSetFetchCallBack</code> and the <code>pmdaFetchCallBack</code> method has the following prototype: </p>
<pre><FONT SIZE="-1">int func(pmdaMetric *mdesc, unsigned int inst, pmAtomValue *avp)
</FONT></pre>
<p><code>pmdaFetch</code> will allocate and resize the <i>resp</i> result structure, to store values for the <i>numpmid </i> metrics listed in <i>pmidlist</i>. </p>
<p> For each instance listed in the profile (see <code><a href="/docs/linux/man/3-pmdaprofile/">pmdaProfile</a></code>(3)) of each metric listed in <i>pmidlist</i>, the <code>pmdaFetchCallBack</code> method is called to fill the <code>pmAtomValue</code> structure identified by <i>avp</i> with a value for a specific metric-instance pair identified by the metric descriptor <i>mdesc</i> and the instance <i>inst</i>. This value is then copied into the <code>pmResult</code> structure. </p>
<p> The <code>pmdaFetchCallBack</code> method should return a value less than zero for an error, and the most likely cases would be <code>PM_ERR_PMID</code> if the metric identified by <i>mdesc</i> is not known to the method, or <code>PM_ERR_INST</code> if the method believes the instance <i>inst</i> is not known for the metric identified by <i>mdesc</i>. </p>
<p> The success error codes depend on the version of <code>PMDA_INTERFACE</code> the PMDA is using. </p>
<p> If the PMDA is using <code>PMDA_INTERFACE_2 </code> then on success the <code>pmdaFetchCallBack</code> method should return <code>0</code>. </p>
<p> If the PMDA is using <code>PMDA_INTERFACE_3 </code> or <code>PMDA_INTERFACE_4 </code> then on success the <code>pmdaFetchCallBack</code> method should return <code>1</code> if a value is returned via <i>avp</i>, else <code>0</code> if no values are currently available for the requested metric-instance pair although <i>mdesc</i> and <i>inst</i> both seem reasonable. </p>
<p> If the PMDA is using <code>PMDA_INTERFACE_5 </code> or later then on success the <code>pmdaFetchCallBack</code> method should return <code>PMDA_FETCH_STATIC</code> (<code>1</code>) if the value returned via <i>avp</i> can be ignored by <code>pmdaFetch</code> once it has been copied into the <code>pmResult</code> structure, else <code>PMDA_FETCH_DYNAMIC</code> (<code>2</code>) if the value returned via <i>avp</i> uses the either the <code>vp</code> or <code>cp</code> fields of the <code>pmAtomValue</code> and the associated value (buffer) was allocated using one of <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-calloc/">calloc</a></code>(3), <code><a href="/docs/linux/man/3-realloc/">realloc</a></code>(3), <code>strdup (3)</code> etc. and <code>pmdaFetch</code> should release the memory by calling <i><a href="/docs/linux/man/3-free/">free</a></i>(3) once a new buffer has been allocated and the value copied, else <code>PMDA_FETCH_NOVALUES</code> (<code>0</code>) if no values are currently available for the requested metric-instance pair although <i>mdesc</i> and <i>inst</i> both seem reasonable. </p>
<p> If the <code>pmdaFetchCallBack</code> method returns a value for an instance of a metric of type <code>PM_TYPE_STRING</code> or <code>PM_TYPE_AGGREGATE</code> some special care is needed &#8211; the method should either use a static buffer, set <i>avp-&gt;cp</i> or <i>avp-&gt;vp</i> to the address of the buffer and return <code>PMDA_FETCH_STATIC</code>, or use a dynamically allocated buffer, keep a static reference to the buffer&#8217;s address, return <code>PMDA_FETCH_STATIC</code> and <i>free (3)</i> or <i>realloc (3)</i> or reuse the buffer the next time the <code>pmdaFetchCallBack</code> method is called, else use a dynamically allocated buffer and return <code>PMDA_FETCH_DYNAMIC</code>.</p>
<h2>Example</h2>
<p>The following code fragments are for a hypothetical PMDA has with metrics (A, B, C and D) and an instance domain (X) with two instances (X1 and X2). The instance domain and metrics description tables (see <code><a href="/docs/linux/man/3-pmdainit/">pmdaInit</a></code>(3)) could be defined as: </p>
<pre><code>static pmdaInstid _X[] = {
    {0, &quot;X1&quot;}, {1, &quot;X2&quot;}};

static pmdaIndom indomtab[] = {
#define X_INDOM 0
    {0, 2, _X},
};

static pmdaMetric metrictab[] = {
    /* A */
    {
        (void *)0,
        {PMDA_PMID(0, 0), PM_TYPE_32, PM_INDOM_NULL, PM_SEM_INSTANT, {0, 0, 0, 0, 0, 0}},
    },
    /* B */
    {
        (void *)0,
        {PMDA_PMID(0, 1), PM_TYPE_DOUBLE, X_INDOM, PM_SEM_INSTANT, {0, 1, 0, 0, PM_TIME_SEC, 0}},
    },
    /* C */
    {
        (void *)0,
        {PMDA_PMID(0, 2), PM_TYPE_STRING, PM_INDOM_NULL, PM_SEM_INSTANT, {0, 0, 0, 0, 0, 0}},
    },
    /* D */
    {
        (void *)0,
        {PMDA_PMID(0, 3), PM_TYPE_STRING, PM_INDOM_NULL, PM_SEM_INSTANT, {0, 0, 0, 0, 0, 0}},
    },
};</code></pre>
<p> A <code>pmdaFetchCallBack</code> method to be called from <code>pmdaFetch</code> could be defined as: </p>
<pre><code>int myFetchCallBack(pmdaMetric *mdesc, unsigned int inst, pmAtomValue *avp)
{
    static char sbuf[20]; // reuse this buffer
    char *dbuf;           // malloc'd

    switch (pmid_item(mdesc-&gt;m_desc.pmid)) {
    case 0:
        /* assign some value for metric A */;
        avp-&gt;l = ... break;
    case 1:
        switch (inst) {
        case 0:
            /* assign a value for metric B, instance X1 */;
            avp-&gt;d = ... break;
        case 1:
            /* assign a value for metric B, instance X2 */;
            avp-&gt;d = ... break;
        default:
            return PM_ERR_INST;
        }
    case 2:
        /* place value for metric C in dbuf[] */
        memcpy(dbuf, ...);
        avp-&gt;cp = dbuf;
        break;
    case 3:
        avp-&gt;cp = (char *)malloc(somesize);
        /* place value in avp-&gt;cp */
        snprintf(avp-&gt;cp, somesize, ...);
        return PMDA_FETCH_DYNAMIC;

    default:
        return PM_ERR_PMID;
    }
    return PMDA_FETCH_STATIC;
}
</code></pre>
<h2>Diagnostics</h2>
<p>The following error messages indicate that there is discrepancy between the namespace, <code>pmdaMetric</code> and <code>pmdaIndom</code> tables passed to <code><a href="/docs/linux/man/3-pmdainit/">pmdaInit</a></code>(3), and the registered fetch callback:</p>
<dl>
<dt><code>pmdaFetch: Requested metric </code><i>metric</i><code> is not defined</code></p>
<dd>A requested metric <i>metric</i> is not listed in the <code>pmdaMetric</code> table. The namespace for this <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3) may contain additional metrics.</p>
<dt><code>pmdaFetch: PMID </code><i>pmid</i><code> not handled by fetch callback</code></p>
<dd>The <code>pmdaFetchCallBack</code> method has returned <code>PM_ERR_PMID</code>. This indicates that a metric may be listed in the <code>pmdaMetric</code> table, but is not supported by the callback method.</p>
<dt><code>pmdaFetch: Instance </code><i>inst</i><code> of PMID </code><i>pmid</i><code> not handled by fetch callback</code></p>
<dd>The <code>pmdaFetchCallBack</code> method has returned <code>PM_ERR_INST</code>. This indicates that an instance of metric is listed in the <code>pmdaIndom</code> table, but is not supported by the callback method.</p>
<dt><code>pmdaFetch: Fetch callback error:</code></p>
<dd>The <code>pmdaFetchCallBack</code> method returned a result other than <code>PMDA_FETCH_NOVALUES</code>, <code>PMDA_FETCH_STATIC</code>, <code>PMDA_FETCH_DYNAMIC</code>, <code>PM_ERR_PMID</code> or <code>PM_ERR_INST</code>.</p>
<dt><code>pmdaFetch: Descriptor type (</code><i>type</i><code>) for metric </code><i>pmid</i><code> is bad</code></p>
<dd>The data type <i>type</i> specified for the metric <i>pmid</i> in the <code>pmdaMetric</code> table is illegal.</dl>
<p> <code>pmdaFetch</code> will return <code>-errno</code> if an error occurred while allocating the <code>pmResult</code> structure or copying the value from the <code>pmAtomValue</code>.</p>
<h2>Caveat</h2>
<p>The PMDA must be using <code>PMDA_INTERFACE_2 </code> or later, as specified in the call to <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) or <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3), <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3), <code><a href="/docs/linux/man/3-pmdainit/">pmdaInit</a></code>(3) and <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3). </p>
