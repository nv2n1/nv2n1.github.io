---
title: "pmdagetcontext(3)"
name: "pmdagetcontext"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdagetcontext/"
description: "pmdaMain, pmdaGetContext, pmdaSetResultCallBack, pmdaSetCheckCallBack, pmdaSetDoneCallBack, pmdaSetEndContextCallBack – generic PDU processing for a PMDA"
---

<p><code>pmdaMain</code>, <code>pmdaGetContext</code>, <code>pmdaSetResultCallBack</code>, <code>pmdaSetCheckCallBack</code>, <code>pmdaSetDoneCallBack</code>, <code>pmdaSetEndContextCallBack</code> &#8211; generic PDU processing for a PMDA</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/pmda.h&gt; </p>
<p> cc &#8230; -lpcp_pmda -lpcp </p>
<p> void pmdaMain(pmdaInterface *</code><i>dispatch</i>); </p>
<p> void pmdaSetCheckCallBack(pmdaInterface *<i>dispatch</i>, pmdaCheckCallBack&nbsp;<wbr><i>callback</i>); </p>
<p> void pmdaSetDoneCallBack(pmdaInterface *<i>dispatch</i>, pmdaDoneCallBack&nbsp;<wbr><i>callback</i>); </p>
<p> void pmdaSetResultCallBack(pmdaInterface *<i>dispatch</i>, pmdaResultCallBack&nbsp;<wbr><i>callback</i>); </p>
<p> void pmdaSetEndContextCallBack(pmdaInterface *<i>dispatch</i>, pmdaEndContextCallBack&nbsp;<wbr><i>callback</i>); </p>
<p> int pmdaGetContext(void);</p>
<h2>Description</h2>
<p>For Performance Metric Domain Agents (<code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3)) using the binary PDU protocols to communicate with <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), the routine <code>pmdaMain</code> provides a generic implementation of the PDU-driven main loop. <i>dispatch</i> describes how to process each incoming PDU. It is a vector of function pointers, one per request PDU type, as used in the DSO interface for a PMDA, namely: </p>
<pre><code>/*
 * Interface Definitions for PMDA Methods
 */
typedef struct {
    int domain; /* set/return performance metrics domain id here */
    struct {
        unsigned int pmda_interface : 8; /* PMDA DSO interface version */
        unsigned int pmapi_version : 8;  /* PMAPI version */
        unsigned int flags : 16;         /* optional feature flags */
    } comm;                              /* set/return communication and version info */
    int status;                          /* return initialization status here */

    union {
        struct { /* PMDA_INTERFACE_2 or _3 */
            pmdaExt *ext;
            int (*profile)(__pmProfile *, pmdaExt *);
            int (*fetch)(int, pmID *, pmResult **, pmdaExt *);
            int (*desc)(pmID, pmDesc *, pmdaExt *);
            int (*instance)(pmInDom, int, char *, __pmInResult **, pmdaExt *);
            int (*text)(int, int, char **, pmdaExt *);
            int (*store)(pmResult *, pmdaExt *);
        } two, three;

        struct { /* PMDA_INTERFACE_4 or _5 */
            pmdaExt *ext;
            int (*profile)(__pmProfile *, pmdaExt *);
            int (*fetch)(int, pmID *, pmResult **, pmdaExt *);
            int (*desc)(pmID, pmDesc *, pmdaExt *);
            int (*instance)(pmInDom, int, char *, __pmInResult **, pmdaExt *);
            int (*text)(int, int, char **, pmdaExt *);
            int (*store)(pmResult *, pmdaExt *);
            int (*pmid)(char *, pmID *, pmdaExt *);
            int (*name)(pmID, char ***, pmdaExt *);
            int (*children)(char *, int, char ***, int **, pmdaExt *);
        } four, five;

        struct { /* PMDA_INTERFACE_6 */
            pmdaExt *ext;
            int (*profile)(__pmProfile *, pmdaExt *);
            int (*fetch)(int, pmID *, pmResult **, pmdaExt *);
            int (*desc)(pmID, pmDesc *, pmdaExt *);
            int (*instance)(pmInDom, int, char *, __pmInResult **, pmdaExt *);
            int (*text)(int, int, char **, pmdaExt *);
            int (*store)(pmResult *, pmdaExt *);
            int (*pmid)(char *, pmID *, pmdaExt *);
            int (*name)(pmID, char ***, pmdaExt *);
            int (*children)(char *, int, char ***, int **, pmdaExt *);
            int (*attribute)(int, int, const char *, int, pmdaExt *);
        } six;
    } version;

} pmdaInterface;</code></pre>
<p> This structure has been extended to incorporate the multiple interface versions that have evolved over time. For <code>pmdaMain,</code> <i>dispatch-&gt;domain</i> and <i>dispatch-&gt;status</i> are ignored. The <i>comm.pmda_interface</i> field is used to determine the interface used by the PMDA. Setting this field to <code>PMDA_INTERFACE_2</code> or <code>PMDA_INTERFACE_3</code> will force <code>pmdaMain</code> to use the callbacks in the <i>version.two</i> or <i>version.three</i> structure. A setting of <code>PMDA_INTERFACE_4</code> or <code>PMDA_INTERFACE_5</code> will force <code>pmdaMain</code> to use the callbacks in the <i>version.four</i> or <i>version.five</i> structure, and similarly a <code>PMDA_INTERFACE_6</code> setting forces <code>pmdaMain</code> to use the callbacks in the <i>version.six</i> structure. Any other value will result in an error and termination of <code>pmdaMain</code>. Note that the use of <code>dispatch</code> as the interface between the <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and the methods of the PMDA allows each PMDA to be implemented as though it were a DSO, with <code>pmdaMain</code> providing a convenient wrapper that may be used to convert from the DSO interface to the binary PDU (daemon PMDA) interface. <code>pmdaMain</code> executes as a continuous loop, returning only when an end of file is encountered on the PDU input file descriptor.</p>
<h2>Callbacks</h2>
<p>In addition to the individual PDU processing callbacks &#8211; <code><a href="/docs/linux/man/3-pmdaprofile/">pmdaProfile</a></code>(3), <code><a href="/docs/linux/man/3-pmdafetch/">pmdaFetch</a></code>(3), <code><a href="/docs/linux/man/3-pmdadesc/">pmdaDesc</a></code>(3), <code><a href="/docs/linux/man/3-pmdainstance/">pmdaInstance</a></code>(3), <code><a href="/docs/linux/man/3-pmdatext/">pmdaText</a></code>(3), <code><a href="/docs/linux/man/3-pmdastore/">pmdaStore</a></code>(3), <code><a href="/docs/linux/man/3-pmdapmid/">pmdaPMID</a></code>(3), <code><a href="/docs/linux/man/3-pmdaname/">pmdaName</a></code>(3), <code><a href="/docs/linux/man/3-pmdachildren/">pmdaChildren</a></code>(3), and <code><a href="/docs/linux/man/3-pmdaattribute/">pmdaAttribute</a></code>(3) there are other callbacks that can affect or inform all PDU processing within a PMDA, namely <i>check</i>, <i>done</i> and <i>end</i>. These callbacks should be set with <code>pmdaSetCheckCallBack</code>, <code>pmdaSetDoneCallBack</code> and <code>pmdaSetEndContextCallBack</code>. </p>
<p> If not null, <i>check </i> is called after each PDU is received (but before it was processed), and <i>done</i> is called after each PDU is sent. If <i>check</i> returns a value less than zero (typically PM_ERR_AGAIN), the PDU processing is skipped and in most cases the function value is returned as an error PDU to <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) &#8211; this may be used for PMDAs that require some sort of deferred connection or reconnect protocols for the underlying sources of performance metrics, e.g. a DBMS. The error indication from <i>check</i> is not passed back to <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) in the cases where no acknowledgment is expected, e.g. for a PDU_PROFILE. </p>
<p> The <i>end</i> callback allows a PMDA to keep track of state for individual clients that are requesting it to perform actions (PDU processing). Using <code>pmdaGetContext</code> a PMDA can determine, at any point, an integer identifier that uniquely identifies the client tools at the remote end of PMCD (for local context modes, this identifier is always zero). This becomes very important for handling event metrics, where each event must be propagated once only to each interested client. It also underlies the mechanism whereby connection information is passed to the PMDA, such as the the credentials (user and group identifiers) for the client tool. </p>
<p> One final callback mechanism is provided for handling the <code>pmResult</code> built for a PDU_RESULT in response to a PDU_FETCH request. By default, <code>pmdaMain</code> will free the <code>pmResult</code> once the result has been sent to the <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1). For some PMDAs this is inappropriate, e.g. the <code>pmResult</code> is statically allocated, or contains a hybrid of pinned PDU buffer information and dynamically allocated information. <code>pmdaSetResultCallback</code> may be used to define an alternative <code>callback</code> from <code>pmdaMain</code>.</p>
<h2>Diagnostics</h2>
<p>These messages may be appended to the PMDA&#8217;s log file:</p>
<dl>
<dt><code>PMDA interface version </code><i>interface</i><code> not supported</code></p>
<dd>The <i>interface</i> version is not supported by <code>pmdaMain</code>.</p>
<dt><code>Unrecognized pdu type</code></p>
<dd>The PMDA received a PDU from <code>pmcd</code> that it does not recognize. This may indicate that the <code>pmcd</code> process is using a more advanced interface than <code>pmdaMain</code>.</dl>
<p> If the <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) debug control variable (<code>pmdebug</code>) has the DBG_TRACE_LIBPMDA flag set then each PDU that is received is reported in the PMDA&#8217;s log file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/3-pmdaprofile/">pmdaProfile</a></code>(3), <code><a href="/docs/linux/man/3-pmdafetch/">pmdaFetch</a></code>(3), <code><a href="/docs/linux/man/3-pmdadesc/">pmdaDesc</a></code>(3), <code><a href="/docs/linux/man/3-pmdainstance/">pmdaInstance</a></code>(3), <code><a href="/docs/linux/man/3-pmdatext/">pmdaText</a></code>(3), <code><a href="/docs/linux/man/3-pmdastore/">pmdaStore</a></code>(3), <code><a href="/docs/linux/man/3-pmdapmid/">pmdaPMID</a></code>(3), <code><a href="/docs/linux/man/3-pmdaname/">pmdaName</a></code>(3), <code><a href="/docs/linux/man/3-pmdachildren/">pmdaChildren</a></code>(3), and <code><a href="/docs/linux/man/3-pmdaattribute/">pmdaAttribute</a></code>(3). </p>
