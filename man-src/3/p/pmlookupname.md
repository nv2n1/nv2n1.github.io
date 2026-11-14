---
title: "pmlookupname(3)"
name: "pmlookupname"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmlookupname/"
description: "pmLookupName – translate performance metric names into PMIDs"
---

<p><code>pmLookupName</code> &#8211; translate performance metric names into PMIDs</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> </code></p>
<pre>int pmLookupName(int <i>numpmid</i>, char **<i>namelist</i>, pmID *<i>pmidlist</i>);</pre>
<p>cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>Given a list in <i>namelist</i> containing <i>numpmid</i> full pathnames for performance metrics from a Performance Metrics Name Space (PMNS), <code>pmLookupName</code> returns the list of associated Performance Metric Identifiers (PMIDs) via <i>pmidlist</i>. </p>
<p> The result from <code>pmLookupName</code> depends on the presence of any lookup failures, their severity and the number of metrics being looked up.</p>
<dl>
<dt>1.</p>
<dd>If there are no lookup failures, the return value will be <i>numpmid</i>.</p>
<dt>2.</p>
<dd>If a fatal error is encountered, the return value will be less than 0. For example <code>PM_ERR_TOOSMALL</code>, <code>PM_ERR_NOPMNS</code> or <code>PM_ERR_IPC</code>.</p>
<dt>3.</p>
<dd>If <i>numpmid</i> is greater than one and non-fatal error(s) are encountered, the return value is the number of metric names that have successfully been looked up (greater than or equal to zero and less than or equal to <i>numpmid</i>).</p>
<dt>4.</p>
<dd>If <i>numpmid</i> is one and a non-fatal error is encountered, the return value is the error code (less than zero).</dl>
<p> When errors are encountered, any metrics that cannot be looked up result in the corresponding element of <i>pmidlist </i> being set to <code>PM_ID_NULL</code>. </p>
<p> The slightly convoluted error protocol allows bulk lookups, then probing for more error details in the case of a specific failure, as shown in the <code>EXAMPLES</code> section below. </p>
<p> Note that the error protocol guarantees there is a 1:1 relationship between the elements of <i>namelist</i> and <i>pmidlist</i>, hence both lists contain exactly <i>numpmid</i> elements. For this reason, the caller is expected to have pre-allocated a suitably sized array for <i>pmidlist</i>.</p>
<h2>Example</h2>
<pre><code>#include &lt;pcp/pmapi.h&gt;

#define NUMPMID 5
char *names[] = {&quot;sample.bin&quot;,
                 &quot;sample&quot;,
                 &quot;sample.bog&quot;,
                 &quot;sample.secret.bar&quot;,
                 &quot;sample.secret.bar.bad&quot;};
pmID pmids[NUMPMID];

int main(int argc, char **argv)
{
    int sts;
    int numpmid = NUMPMID;

    pmNewContext(PM_CONTEXT_HOST, &quot;local:&quot;);

    sts = pmLookupName(numpmid, names, pmids);

    if (sts &lt; 0) {
        fprintf(stderr, &quot;pmLookupName failed: %s, pmErrStr(sts));
        exit(1);
    }
    if (sts != numpmid) {
        /*
         * some of the lookups failed ... report the reason(s)
         */
        int i;

        for (i = 0; i &lt; numpmid; i++) {
            if (pmids[i] != PM_ID_NULL)
                continue;
            /* this one failed */
            sts = pmLookupName(1, &amp;names[i], &amp;pmids[i]);
            fprintf(stderr, &quot;%s: lookup failed: %s, names[i], pmErrStr(sts));
        }
        exit(1);
    }

    /* all good ... */
    ...
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmgetchildren/">pmGetChildren</a></code>(3), <code><a href="/docs/linux/man/3-pmgetchildrenstatus/">pmGetChildrenStatus</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmloadnamespace/">pmLoadNameSpace</a></code>(3), <code><a href="/docs/linux/man/3-pmnameid/">pmNameID</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_TOOSMALL</code></p>
<dd><i>numpmid</i> must be at least 1</p>
<dt><code>PM_ERR_NOPMNS</code></p>
<dd>Failed to access a PMNS for operation. Note that if the application hasn&#8217;t a priori called <code><a href="/docs/linux/man/3-pmloadnamespace/">pmLoadNameSpace</a></code>(3) and wants to use the distributed PMNS, then a call to <code>pmLookupName</code> must be made after the creation of a context (see <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3)).</p>
<dt><code>PM_ERR_NAME</code></p>
<dd><i>namelist[0]</i> does not correspond to a valid metric name in the PMNS.</p>
<dt><code>PM_ERR_NONLEAF</code></p>
<dd><i>namelist[0]</i> refers to a node in the PMNS but it was not a leaf node.</p>
<dt><code>PM_ERR_*</code></p>
<dd>Other diagnostics are for protocol failures when accessing the distributed PMNS. </p>
</dl>
