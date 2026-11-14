---
title: "mmv_stats_init(3)"
name: "mmv_stats_init"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mmv_stats_init/"
description: "mmv_stats_init – create and initialize Memory Mapped Value file"
---

<p><code>mmv_stats_init</code> &#8211; create and initialize Memory Mapped Value file</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/mmv_stats.h&gt; </p>
<p> void *mmv_stats_init(const char *</code><i>name</i>, int <i>cluster</i>, mmv_stats_flags_t&nbsp;<wbr><i>flags</i>, const mmv_metric_t&nbsp;<wbr>*<i>stats</i>, int&nbsp;<wbr><i>nstats</i>, mmv_indom_t&nbsp;<wbr>*<i>indoms</i>, int&nbsp;<wbr><i>nindoms</i>); </p>
<p> cc &#8230; -lpcp_mmv -lpcp</p>
<h2>Description</h2>
<p><code>mmv_stats_init</code> creates and initializes the content of the <i><a href="/docs/linux/man/5-mmv/">MMV</a></i>(5) file, returning a handle that is used in subsequent MMV API calls. </p>
<p> <code>mmv_stats_stop</code> performs an orderly shutdown of the mapping handle returned by an earlier initialization call. </p>
<p> The file is created in the $PCP_TMP_DIR/mmv directory, <i>name</i> argument is expected to be a basename of the file, not the full path. The metadata content of the file does not change after the file has been created. </p>
<p> The old file is removed unconditionally unless there was an error. </p>
<p> <i>cluster</i> is the preferred MMV PMDA cluster ID to be used for the metrics originating from this call to <code>mmv_stats_init</code>. The <i>flags</i> provide additional control over the behaviour of the MMV PMDA &#8211; e.g. use of MMV_FLAG_PROCESS will ensure values are only exported when the instrumented application is running &#8211; this is verified on each request for new values. </p>
<p> <i>stats</i> is the array of <code>mmv_metric_t</code> elements of length <i>nstats</i>. Each element of the array describes one PCP metric. </p>
<pre> typedef struct {
 char name[MMV_NAMEMAX]; /* Name of the metric */
 __uint32_t item; /* Item component of PMID */
 mmv_metric_type_t type; /* Type of the metric */
 mmv_metric_sem_t semantics; /* Semantics of the metric */
 pmUnits dimension; /* Dimensions (TIME,SPACE,etc) */
 __uint32_t indom; /* Instance domain identifier */
 char *shorttext; /* Optional, one-line help */
 char *helptext; /* Optional, full help text */
 } mmv_metric_t;</pre>
<p>If <code>indom</code> is not zero and not PM_INDOM_NULL, then the metric has multiple values and there must be a corresponding <i>indom</i> entry in the <i>indom</i> list (uniquely identified by <code>serial</code> number). </p>
<p> The <i>stats</i> array cannot contain any elements which have no name &#8211; this is considered an error and no metrics will be exported in this case. </p>
<p> <i>indoms</i> is the array of <code>mmv_indom_t</code> elements of length <i>nindoms</i>. Each element of the array describes one PCP instance domain. </p>
<pre> typedef struct {
 __int32_t internal;
 char external[MMV_NAMEMAX];
 } mmv_instances_t;
 typedef struct {
 __uint32_t serial; /* Unique serial number */
 __uint32_t count; /* Number of instances */
 mmv_instances_t *instances; /* Internal/external IDs */
 char *shorttext; /* Short help text */
 char *helptext; /* Long help text */
 } mmv_indom_t;</pre>
<h2>Returns</h2>
<p>The function returns the address of the memory mapped region on success or NULL on failure.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mmv_inc_value/">mmv_inc_value</a></code>(3), <code><a href="/docs/linux/man/3-mmv_lookup_value_desc/">mmv_lookup_value_desc</a></code>(3) and <code><a href="/docs/linux/man/5-mmv/">mmv</a></code>(5).</p>
