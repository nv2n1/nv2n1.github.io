---
title: "pmcreatefetchgroup(3)"
name: "pmcreatefetchgroup"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmcreatefetchgroup/"
description: "pmCreateFetchGroup, pmExtendFetchGroup_item, pmExtendFetchGroup_indom, pmExtendFetchGroup_event, pmExtendFetchGroup_timestamp, pmFetchGroup, pmGetFetchGroupContext, pmDestroyFetchGroup – simplified..."
---

<p><code>pmCreateFetchGroup</code>, <code>pmExtendFetchGroup_item</code>, <code>pmExtendFetchGroup_indom</code>, <code>pmExtendFetchGroup_event</code>, <code>pmExtendFetchGroup_timestamp</code>, <code>pmFetchGroup</code>, <code>pmGetFetchGroupContext</code>, <code>pmDestroyFetchGroup</code> &#8211; simplified performance metrics value fetch and conversion</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmCreateFetchGroup(pmFG *</code><i>ptr</i>, int <i>type</i>, const char *<i>name</i>); </p>
<p> int pmExtendFetchGroup_item(pmFG <i>pmfg</i>, const char *<i>metric</i>, const char *<i>instance</i>, const char *<i>scale</i>, pmAtomValue *<i>out_value</i>, int <i>out_type</i>, int <i>out_sts</i>); </p>
<p> int pmExtendFetchGroup_indom(pmFG <i>pmfg</i>, const char *<i>metric</i>, const char *<i>scale</i>, int <i>out_inst_codes</i>[], char *<i>out_inst_names</i>[], pmAtomValue <i>out_values</i>[], int <i>out_type</i>, int <i>out_stss</i>[], unsigned int <i>out_maxnum</i>, unsigned int *<i>out_num</i>, int *<i>out_sts</i>); </p>
<p> int pmExtendFetchGroup_event(pmFG <i>pmfg</i>, const char *<i>metric</i>, const char *<i>instance</i>, const char *<i>field</i>, const char *<i>scale</i>, struct timespec <i>out_times</i>[], pmAtomValue <i>out_values</i>[], int <i>out_type</i>, int <i>out_stss</i>[], unsigned int <i>out_maxnum</i>, unsigned int *<i>out_num</i>, int *<i>out_sts</i>); </p>
<p> int pmExtendFetchGroup_timestamp(pmFG <i>pmfg</i>, struct timeval *<i>out_value</i>); </p>
<p> int pmGetFetchGroupContext(pmFG <i>pmfg</i>); </p>
<p> int pmFetchGroup(pmFG <i>pmfg</i>); </p>
<p> int pmDestroyFetchGroup(pmFG <i>pmfg</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>The fetchgroup functions implement a registration-based mechanism to fetch groups of performance metrics, including automation for general unit, rate and type conversions as well as convenient instance and value encodings. They constitute a powerful and compact alternative to the classic Performance Metrics Application Programming Interface (<code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3)) sequence of separate lookup, check, fetch, iterate, extract and convert functions. The general idea consists of two stages. In the setup stage, the application identifies metrics of interest by name and with desired conversions, and register a unique <code>pmAtomValue</code> output location where the fetchgroup system is to later deposit the result. It is also possible to identify a metric with an instance domain, and register a unique <i>vector</i> of pmAtomValue objects for them. In the operation stage, one simple <code>pmFetchGroup</code> function fetches, decodes, converts, and stores all metrics to their destinations, where the application can <i>read</i> them directly. This function may be called repeatedly, and each time new <code>pmAtomValue</code> values will be stored in the same destinations. Rate conversions between consecutive samples may be requested. Each fetchgroup is associated with a private PMAPI context, so it can manipulate instance profiles and other such state without disrupting other contexts. This private PMAPI context belongs to the fetchgroup, is used for all of its internal operations, and will be destroyed. Multiple fetchgroups may be used concurrently, independently. An opaque type <code>pmFG</code> is used to identify a fetchgroup, which is passed to all related function calls.</p>
<h3>Creating a fetchgroup</h3>
<p><code> </p>
<pre><code>int pmCreateFetchGroup(pmFG *ptr, int type, const char *name);</code></pre>
<p> This function creates a new fetchgroup, associated with a new PMAPI context. The <i>type</i> and <i>name</i> parameters are relayed to <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3) for creation of the context. The fetchgroup identifier is returned upon success through the <i>ptr</i> pointer. This object is later used as a parameter to all other fetchgroup functions. The private PMAPI context may be accessed with <code>pmGetFetchGroupContext</code>, if required. The normal function return code is zero, and <i>ptr</i> is set. This function may fail in case of <code>pmNewContext</code> or memory allocation errors. Those are indicated with a negative return code and a cleared <i>ptr</i> value.</p>
<h3>Getting the private PMAPI context</h3>
<p><code> int pmGetFetchGroupContext(pmFG pmfg); This function returns the private PMAPI context used by the given fetchgroup. It may be safely used to adjust some configuration parameters of the context, such as via <code><a href="/docs/linux/man/3-pmsetmode/">pmSetMode</a></code>(3), before fetchgroup extension and fetching begins. However, <i>mutation</i> of this context by PMAPI functions after this time may disrupt fetchgroup functionality. For example, a <code>pmSetMode</code> call could invalidate one rate-conversion time-step. The normal function return code is the context number.</p>
<h3>Extending a fetchgroup with a metric instance of interest</h3>
<p><code> int pmExtendFetchGroup_item(pmFG pmfg, const char *metric, const char *instance, const char *scale, pmAtomValue *out_value, int out_type, int *out_sts); This function registers interest in a single metric and optional instance. The metric name is given in the mandatory <i>metric</i> parameter, which is checked immediately via <code><a href="/docs/linux/man/3-pmlookupname/">pmLookupName</a></code>(3) and other calls. If and only if the metric has an instance domain, the specific instance of interest may be named by the <i>instance</i> parameter, which is checked immediately via <code><a href="/docs/linux/man/3-pmnameindom/">pmNameInDom</a></code>(3); otherwise pass NULL. If the fetchgroup context is a set of archives, it is possible that the metric / instance pair is not yet defined at the current time origin. Therefore, this function may attempt to seek to the <i>end</i> of the current set of archives <i>temporarily</i> to retry the metric / instance lookup. The optional <i>scale</i> parameter specifies desired unit/scale/rate conversions for the metric value. It can take the following values:</p>
<dl>
<dt>NULL</p>
<dd>No unit/scale conversion. If metric has <code>PM_SEM_COUNTER</code> semantics, perform rate conversion.</p>
<dt>rate</p>
<dd>Perform rate conversion regardless of semantics, and no unit/scale conversion.</p>
<dt>instant</p>
<dd>Perform no rate conversion regardless of semantics, and no unit/scale conversion.</p>
<dt>EXPRESSION</p>
<dd>Perform unit/scale/rate conversion as specified by the EXPRESSION, which is parsed by <code><a href="/docs/linux/man/3-pmparseunitsstr/">pmParseUnitsStr</a></code>(3). This may be useful to assert a canonical scaling for the resulting metric value, independent of PCP version or configuration. Dimensionality must match the metric, except if rate conversion is requested, in which case the time dimension must be one smaller than the metric&#8217;s time dimension. Note that the type of rate conversion performed here matches the <code>rate(x)</code> function in derived metric expressions, in that it is calculated as the naive difference between previous and current values of a metric, divided by elapsed time. For example, if a counter wraps around, or a non-counter value decreases, a <i>negative</i> output rate may be computed.</dl>
<p> The optional but usual <i>out_value</i> parameter specifies the <code>pmAtomValue</code> where the converted result should later be stored. If the value is NULL, fetching and conversions will be attempted, and possible errors reported, but the result tossed away. The mandatory <i>out_type</i> parameter specifes the <code>PM_TYPE_*</code> requested for the output value. It need not match the metric&#8217;s native type, as the fetchgroup facility is capable of casting between all supported types (including to and from strings). Any errors subsequently encountered during fetching, unit/scale/rate conversion, or casting, will result in the assignment of a sentinel value to the output <code>pmAtomValue</code> (see the &#8220;UNUSUAL SITUATIONS&#8221; section below). In addition, if the optional <i>out_sts</i> parameter is specified, an appropriate PMAPI error code will be stored there. As a review, only the <i>pmfg</i>, <i>metric</i>, and <i>out_type</i> parameters are mandatory. Others may be NULL to indicate applicaton disinterest. The normal function return code is zero. This function may fail in case of various lookup, type- and conversion- checking errors. Those are indicated with a negative return code.</p>
<h3>Extending a fetchgroup with a metric instance domain of interest</h3>
<p><code> int pmExtendFetchGroup_indom(pmFG pmfg, const char *metric, const char *scale, int out_inst_codes[], char *out_inst_names[], pmAtomValue out_values[], int out_type, int out_stss[], unsigned int out_maxnum, unsigned int *out_num, int *out_sts); This function generalizes the <code>pmExtendFetchGroup_item</code> function by registering interest in a whole instance domain. Therefore, the function registers preallocated <i>vectors</i> for output variables (instead of a singleton). Instances will be stored in sorted order in elements of those vectors. The concepts are otherwise the same. The metric name is specified by the mandatory <i>metric</i> parameter. Note that it <i>may</i> refer to a metric without an instance domain, in which case the single output value will appear as one unnamed instance. The optional <i>scale</i> parameter specifies desired unit/scale/rate conversions for the metric value, same as above. The optional <i>out_inst_codes</i> parameter specifies a vector of integers, where the raw instance number of the fetched metrics should later be stored. The optional <i>out_inst_names</i> parameter specifies a vector of strings, where the instance names of the fetched metrics should later be stored. If an instance does not have a corresponding name, a NULL pointer is stored instead. The application must not modify or <code><a href="/docs/linux/man/3-free/">free</a></code>(3) strings in that vector. The optional <i>out_values</i> parameter specifies a vector of <code>pmAtomValue</code> objects where the converted result should later be stored. The mandatory <i>out_type</i> parameter specifies the <code>PM_TYPE_*</code> requested for the all output values, same as above. The optional <i>out_stss</i> parameter specifies a vector of integers where per-instance error codes should be stored. The mandatory <i>out_maxnum</i> parameter specifies the number of elements of the vectors above. In other words, it tells the fetchgroup the maximum number of instances which are expected. The optional <i>out_num</i> parameter specifies an integer where the actual number of instances should later be stored. It will range between 0 and <i>out_maxnum</i>. It is initialized to 0 by this function. Finally, the optional <i>out_sts</i> parameter specifies a single location where an integer status code for the overall fetch for this metric should be stored. Normally, this will be zero. Other than a severe fetch error, one may see a <code>PM_ERR_TOOBIG</code> here if the number of instances actually encountered was larger than <i>out_maxnum</i>. Any errors subsequently encountered during fetching, unit/scale/rate conversion, or casting, will result in the assignment of a sentinel value to the appropriate output <code>pmAtomValue</code> (see the &#8220;UNUSUAL SITUATIONS&#8221; section below). In addition, if the optional <i>out_stss</i> parameter was specified, a PMAPI error code will be stored in the appropriate position. As a review, only the <i>pmfg</i>, <i>metric</i>, <i>out_type</i>, and <i>out_maxnum</i> parameters are mandatory. Others may be NULL to indicate applicaton disinterest. The normal function return code is zero. This function may fail in case of various lookup, type- and conversion- checking errors. Those are indicated with a negative return code.</p>
<h3>Extending a fetchgroup with an event field</h3>
<p><code> int pmExtendFetchGroup_event(pmFG pmfg, const char *metric, const char *instance, const char *field, const char *scale, struct timespec out_times[], pmAtomValue out_values[], int out_type, int out_stss[], unsigned int out_maxnum, unsigned int *out_num, int *out_sts); This function registers interest in all instances of one field of all records of an event metric. Since event metrics may return multiple records per fetch, and each record may have multiple fields of a given field metric type, this function registers preallocated <i>vectors</i> for output variables, similarly to <code>pmExtendFetchGroup_indom</code>. They are filled in temporal/sequential order. The metric name is specified by the mandatory <i>metric</i> parameter. It must be of <code>PM_TYPE_EVENT</code>. If the metric has an instance domain, the <i>instance</i> parameter is mandatory to identify the instance of interest. The field to extract from event records is specified by the mandatory <i>field</i> parameter, which is a metric name of normal scalar type. As is typical for event field metrics, it should not have an instance domain. The optional <i>scale</i> parameter specifies desired unit/scale conversions on this metric value. Rate conversions are <code>not available</code>, because of ambiguity about which previous value to compute rates from. The optional <i>out_times</i> parameter specifies a vector of <code>timespec</code> structs, which will receive a copy of the timestamp of the event record where each particular field was found. The optional <i>out_values</i> parameter specifies a vector of <code>pmAtomValue</code> objects where the converted result should later be stored. The mandatory <i>out_type</i> parameter specifies the <code>PM_TYPE_*</code> requested for the output values. The optional <i>out_stss</i> parameter specifies a vector of integers where per-field error codes should be stored. The mandatory <i>out_maxnum</i> parameter specifies the number of elements of the vectors above. In other words, it tells the fetchgroup the maximum number of instances which are expected. The optional <i>out_num</i> parameter specifies an integer where the the actual number of instances should later be stored. It will range between zero and <i>out_maxnum</i>. It is initialized to zero by this function. Finally, the optional <i>out_sts</i> parameter specifies a single location where an integer status code for the overall fetch for this metric should be stored. Normally, this will be zero, even if no event field values were found (<i>out_num</i> would then be zero). Other than a severe fetch error, one may see a <code>PM_ERR_TOOBIG</code> here if the number of fields actually encountered was larger than <i>out_maxnum</i>. Any errors subsequently encountered during fetching, unit/scale conversion, or casting, will result in the assignment of a sentinel value to the appropriate output <code>pmAtomValue</code> (see the &#8220;UNUSUAL SITUATIONS&#8221; section below). In addition, if the optional <i>out_stss</i> parameter was specified, a PMAPI error code will be stored in the appropriate position. As a review, only the <i>pmfg</i>, <i>metric</i>, <i>field</i>, <i>out_type</i>, and <i>out_maxnum</i> parameters are mandatory. Others may be NULL to indicate applicaton disinterest. The normal function return code is zero. This function may fail in case of various lookup, type- and conversion- checking errors. Those are indicated with a negative return code.</p>
<h3>Extending a fetchgroup with the fetch timestamp</h3>
<p><code> int pmExtendFetchGroup_timestamp(pmFG pmfg, struct timeval *out_value); This function registers interest in the <code>pmResult</code> timestamp. If the <i>out_value</i> pointer is non-NULL, at every future <code>pmFetchGroup</code> call, the corresponding result timestamp will be copied there.</p>
<h3>Fetching all metrics in a fetchgroup</h3>
<p><code> int pmFetchGroup(pmFG pmfg); This function performs one <code>pmFetch</code> on its private PMAPI context, including all the metrics that were registered via prior <code>pmExtendFetchGroup_*</code> calls. It runs all the data extraction and conversion operations necessary to populate all the requested output variables. The normal function return code is zero or positive, as per the underlying <code>pmFetch</code> function. This function may fail in case of severe fetch errors, which are indicated with a negative return code. In the case of per-metric availability or conversion errors, or severe fetch errors, output variables are reset to sentinel values and individual error codes are set. <i>PM_ERR_AGAIN</i> signals rate-conversion failure due to lack of a previous value. However, temporarily absent metrics with discrete semantics are exempt from some sentinel/error processing: if a <code>pmFetchGroup</code> fails to collect a result for a discrete metric (pmResult pmValueSet.numval==0), then the last seen valid value (if any) is retained. This is intended to ease the processing of sets of archives with a mixture of once- and repeatedly-sampled metrics.</p>
<h3>Destroying a fetchgroup</h3>
<pre>int pmDestroyFetchGroup(pmFG <i>pmfg</i>);</pre>
<p>When the fetchgroup is no longer needed, it may be explicitly freed with this function. It releases any dynamically stored state, as well as the private PMAPI context. It clears frees any pointers such as indom instance names or strings that may have been stored in output variables.</p>
<h2>Example</h2>
<p>The following program demonstrates fetchgroup usage. Run it with different $PCP_DISK_UNITS environment variables to see different unit/rate conversion in effect. </p>
<pre><code>#include &lt;pcp/pmapi.h&gt;
#include &lt;stdio.h&gt;

#define pcpassert(sts)                          \
    while (sts &lt; 0) {                           \
        fprintf(stderr, &quot;%s
&quot;, pmErrStr(sts)); \
        exit(42);                               \
    }

int main()
{
    pmFG fg;
    pmAtomValue v, v2;
    enum { v3_maxnum = 100 };
    pmAtomValue v3_values[v3_maxnum];
    char *v3_names[v3_maxnum];
    int v3_stss[v3_maxnum];
    unsigned int v3_num;
    int sts, i;
    char *diskunits = getenv(&quot;PCP_DISK_UNITS&quot;);
    struct timeval t;

    sts = pmCreateFetchGroup(&amp;fg, PM_CONTEXT_HOST, &quot;local:&quot;);
    pcpassert(sts);
    sts = pmExtendFetchGroup_item(fg, &quot;kernel.all.load&quot;, &quot;1 minute&quot;,
                                  NULL, &amp;v, PM_TYPE_FLOAT, NULL);
    pcpassert(sts);
    sts = pmExtendFetchGroup_item(fg, &quot;kernel.all.idletime&quot;, NULL,
                                  &quot;hour&quot;, &amp;v2, PM_TYPE_DOUBLE, NULL);
    pcpassert(sts);
    sts = pmExtendFetchGroup_indom(fg, &quot;disk.dev.total&quot;, diskunits,
                                   NULL, v3_names,
                                   v3_values, PM_TYPE_STRING,
                                   v3_stss, v3_maxnum, &amp;v3_num, NULL);
    pcpassert(sts);
    sts = pmExtendFetchGroup_timestamp(fg, &amp;t);
    pcpassert(sts);

    for (i = 0; i &lt; 10; i++) {
        unsigned int j;
        char stamp[28];

        sts = pmFetchGroup(fg);
        pcpassert(sts);
        printf(&quot;%s&quot;, pmCtime(&amp;t.tv_sec, stamp));
        printf(&quot;1-minute load: %f; idletime: %f h
&quot;, v.f, v2.d);
        for (j = 0; j &lt; v3_num; j++) {
            if (v3_stss[j] == 0)
                printf(&quot;disk %s i/o operations (%s): %s
&quot;,
                       v3_names[j] ? v3_names[j] : &quot;?&quot;,
                       diskunits ? diskunits : &quot;-&quot;,
                       v3_values[j].cp);
        }
        sleep(1);
    }

    sts = pmDestroyFetchGroup(fg);
    pcpassert(sts);
    return 0;
}</code></pre>
<h2>Unusual Situations</h2>
<p>The fetchgroup API supports only the numeric, string and event metric types. Aggregates are rejected during <code>pmExtendFetchGroup_*</code>. </p>
<p> Any strings supplied by the fetchgroup API to the application are &quot;owned&quot; by the API. The application should consider them read-only, so it should not modify them nor <code>free</code> them. </p>
<p> Error codes are always negative integers, whether returned from fetchgroup functions as return value, or stored in <i>out_sts</i> type variables. Normal result codes are always zero. </p>
<p> Because of the unique ways in which extracted data is shared between the application and a fetchgroup, the functions in this API are <i>not protected</i> by the multi-threading mutexes conventional in other parts of PMAPI. Specifically, for any given <code>pmFG</code>, it is <i>not safe</i> to concurrently call two or more fetchgroup API functions, nor to traverse the registered output variables while calling one of the functions. Instead, the calling application must ensure that only one thread at a time uses these calls <i>and</i> the registered output variables. On the other hand, concurrency between different <code>pmFG</code> instances is unrestricted, because they share no global data. </p>
<p> Any pointers passed to a successful <code>pmFetchGroupExtent_*</code> call must stay valid throughout the lifetime of the fetchgroup, since future <code>pmFetchGroup</code> calls may write into them.</p>
<h2>Diagnostics</h2>
<p>The fetchgroup API offers several options for collecting diagnostics. Negative integer error codes may be returned from each function for serious conditions. </p>
<p> In addition, each output pmAtomValue may have a corresponding integer variable, where <code>pmFetchGroup</code> can store per-metric per-instance error codes. </p>
<p> As an alternative, per-metric per-instance error conditions are also signalled by setting the corresponding pmAtomValue to a sentinel value. If unambiguous and precise error detection is not required, this may be sufficient. The sentinel value is negative one for all integers (including unsigned integers &#8211; i.e. all bits are set), <code>NaN</code> for floating point types, a NULL pointer for strings, and 0.0s for the timestamp. The fetchgroup API guarantees that once an output pmAtomValue is registered (during a successful <code>pmExtendFetchGroup_*</code> call), it will be cleared to the sentinel value or to a valid converted metric value, from the time of registration until the <code>pmDestroyFetchGroup</code> call.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupname/">pmLookupName</a></code>(3), <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3), <code><a href="/docs/linux/man/3-pmparseunitsstr/">pmParseUnitsStr</a></code>(3), <code><a href="/docs/linux/man/3-pmusecontext/">pmUseContext</a></code>(3), <code><a href="/docs/linux/man/3-pmregisterderived/">pmRegisterDerived</a></code>(3) and <code><a href="/docs/linux/man/3-pmextractvalue/">pmExtractValue</a></code>(3). </p>
