---
title: "pmlookupdesc(3)"
name: "pmlookupdesc"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmlookupdesc/"
description: "pmLookupDesc – obtain a description for a performance metric"
---

<p><code>pmLookupDesc</code> &#8211; obtain a description for a performance metric</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> </code></p>
<pre>int pmLookupDesc(pmID <i>pmid</i>, pmDesc *<i>desc</i>);</pre>
<p>cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>Given a Performance Metrics Identifier (PMID) as <i>pmid</i>, fill in the given <i>pmDesc</i> structure, pointed to by the parameter <i>desc</i>, from the current Performance Metrics Application Programming Interface (PMAPI) context. The <i>pmDesc</i> structure provides all of the information required to describe and manipulate a performance metric via the PMAPI, and has the following declaration. </p>
<pre><code>/* Performance Metric Descriptor */
typedef struct {
    pmID pmid;     /* unique identifier */
    int type;      /* base data type (see below) */
    pmInDom indom; /* instance domain */
    int sem;       /* semantics of value (see below) *
   pmUnits units;  /* dimension and units (see below) */
} pmDesc;

/* pmDesc.type -- data type of metric values */
#define PM_TYPE_NOSUPPORT -1       /* not impl. in this version */
#define PM_TYPE_32 0               /* 32-bit signed integer */
#define PM_TYPE_U32 1              /* 32-bit unsigned integer */
#define PM_TYPE_64 2               /* 64-bit signed integer */
#define PM_TYPE_U64 3              /* 64-bit unsigned integer */
#define PM_TYPE_FLOAT 4            /* 32-bit floating point */
#define PM_TYPE_DOUBLE 5           /* 64-bit floating point */
#define PM_TYPE_STRING 6           /* array of char */
#define PM_TYPE_AGGREGATE 7        /* arbitrary binary data */
#define PM_TYPE_AGGREGATE_STATIC 8 /* static pointer to aggregate */
#define PM_TYPE_EVENT 9            /* packed pmEventArray */
#define PM_TYPE_UNKNOWN 255        /* used in pmValueBlock, not pmDesc */

/* pmDesc.sem -- semantics/interpretation of metric values */
#define PM_SEM_COUNTER 1  /* cumulative ctr (monotonic incr) */
#define PM_SEM_INSTANT 3  /* instant. value continuous domain */
#define PM_SEM_DISCRETE 4 /* instant. value discrete domain */</code></pre>
<p> The <i>type</i> field in the <i>pmDesc</i> describes various encodings (or formats) for a metric&#8217;s value. If a value is counted in the underlying base instrumentation with less than 32 bits of integer precision, it is the responsibility of the Performance Metrics Domain Agent (PMDA) to promote the value to a 32-bit integer before it is exported into the Performance Metrics Collection Subsystem (PMCS); i.e. applications above the PMAPI never have to deal with 8-bit and 16-bit counters. If the value of a performance metric is of type <code>PM_TYPE_AGGREGATE</code>, <code>PM_TYPE_AGGREGATE_STATIC,</code> <code>PM_TYPE_EVENT</code> or <code>PM_TYPE_STRING</code>, the interpretation of the value is unknown to the PMCS. In these cases, the application using the value, and the PMDA providing the value must have some common understanding about how the value is structured and interpreted. Each value for a performance metric is assumed to be drawn from a set of values that can be described in terms of their dimensionality and scale by a compact encoding as follows. The dimensionality is defined by a power, or index, in each of 3 orthogonal dimensions, namely Space, Time and Count (or Events, which are dimensionless). For example I/O throughput might be represented as<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-1</i><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <i>Space.Time</i><br />
 while the running total of system calls is <i>Count</i>, memory allocation is <i>Space</i> and average service time is<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-1</i><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <i>Time.Count</i><br />
 In each dimension there are a number of common scale values that may be used to better encode ranges that might otherwise exhaust the precision of a 32-bit value. This information is encoded in the <i>pmUnits</i> structure which is embedded in the <i>pmDesc</i> structure. </p>
<pre><code>/*
 * Encoding for the units (dimensions Time and Space) and scale
 * for Performance Metric Values
 *
 * For example, a pmUnits struct of
 *      { 1, -1, 0, PM_SPACE_MBYTE, PM_TIME_SEC, 0 }
 * represents Mbytes/sec, while
 *      { 0, 1, -1, 0, PM_TIME_HOUR, 6 }
 * represents hours/million-events
 */
typedef struct {
    int dimSpace : 4;            /* space dimension */
    int dimTime : 4;             /* time dimension */
    int dimCount : 4;            /* event dimension */
    unsigned int scaleSpace : 4; /* one of PM_SPACE_* below */
    unsigned int scaleTime : 4;  /* one of PM_TIME_* below */
    int scaleCount : 4;          /* one of PM_COUNT_* below */
} pmUnits;                       /* dimensional units and scale of value */

/* pmUnits.scaleSpace */
#define PM_SPACE_BYTE 0  /* bytes */
#define PM_SPACE_KBYTE 1 /* Kilobytes (1024) */
#define PM_SPACE_MBYTE 2 /* Megabytes (1024^2) */
#define PM_SPACE_GBYTE 3 /* Gigabytes (1024^3) */
#define PM_SPACE_TBYTE 4 /* Terabytes (1024^4) */
/* pmUnits.scaleTime */
#define PM_TIME_NSEC 0 /* nanoseconds */
#define PM_TIME_USEC 1 /* microseconds */
#define PM_TIME_MSEC 2 /* milliseconds */
#define PM_TIME_SEC 3  /* seconds */
#define PM_TIME_MIN 4  /* minutes */
#define PM_TIME_HOUR 5 /* hours */
/*
 * pmUnits.scaleCount (e.g. count events, syscalls, interrupts,
 * etc.) these are simply powers of 10, and not enumerated here,
 * e.g. 6 for 10^6, or -3 for 10^-3
 */
#define PM_COUNT_ONE 0 /* 1 */</code></pre>
<p> Special routines (e.g. <code><a href="/docs/linux/man/3-pmextractvalue/">pmExtractValue</a></code>(3), <code><a href="/docs/linux/man/3-pmconvscale/">pmConvScale</a></code>(3)) are provided to manipulate values in conjunction with the <i>pmUnits</i> structure that defines the dimension and scale of the values for a particular performance metric. Below the PMAPI, the information required to complete the <i>pmDesc</i> structure, is fetched from the PMDAs, and in this way the format and scale of performance metrics may change dynamically, as the PMDAs and their underlying instrumentation evolve with time. In particular, when some metrics suddenly become 64-bits long, or change their units from Mbytes to Gbytes, well-written applications using the services provided by the PMAPI will continue to function correctly.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmatomstr/">pmAtomStr</a></code>(3), <code><a href="/docs/linux/man/3-pmconvscale/">pmConvScale</a></code>(3), <code><a href="/docs/linux/man/3-pmextractvalue/">pmExtractValue</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmtypestr/">pmTypeStr</a></code>(3), <code><a href="/docs/linux/man/3-pmunitsstr/">pmUnitsStr</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_PMID</code></p>
<dd>The requested PMID is not known to the PMCS</p>
<dt><code>PM_ERR_NOAGENT</code></p>
<dd>The PMDA responsible for providing the metric is currently not available </p>
</dl>
