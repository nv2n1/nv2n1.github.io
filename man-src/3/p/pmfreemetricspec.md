---
title: "pmfreemetricspec(3)"
name: "pmfreemetricspec"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmfreemetricspec/"
description: "pmParseMetricSpec, pmFreeMetricSpec – uniform metric specification parser"
---

<p><code>pmParseMetricSpec</code>, <code>pmFreeMetricSpec</code> &#8211; uniform metric specification parser</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmParseMetricSpec(const char *</code><i>string</i>, int <i>isarch</i>, char&nbsp;<wbr>*<i>source</i>, pmMetricSpec&nbsp;<wbr>**<i>rsltp</i>, char&nbsp;<wbr>**<i>errmsg</i>); </p>
<p> void pmFreeMetricSpec(pmMetricSpec *<i>rslt</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p><code>pmParseMetricSpec</code> accepts a <code>string</code> specifying the name of a PCP performance metric, and optionally the source (either a hostname or a PCP archive log filename) and instances for that metric. The syntax is described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). </p>
<p> If neither <code>host</code> nor <code>archive</code> component of the metric specification is provided, the <code>isarch</code> and <code>source</code> arguments are used to fill in the returned <code>pmMetricSpec</code> structure. </p>
<p> The <code>pmMetricSpec</code> structure that is returned via <code>rsltp</code> represents the parsed <code>string</code> and has the following declaration: </p>
<pre> typedef struct {
 int isarch; /* source type: 0 -&gt; live host, 1 -&gt; archive, 2 -&gt; local context */
 char *source; /* name of source host or archive */
 char *metric; /* name of metric */
 int ninst; /* number of instances, 0 -&gt; all */
 char *inst[1]; /* array of instance names */
 } pmMetricSpec;</pre>
<p><code>pmParseMetricSpec</code> returns 0 if the given <code>string</code> was successfully parsed. In this case all the storage allocated by <code>pmParseMetricSpec</code> can be released by a single call to <code><a href="/docs/linux/man/3-free/">free</a></code>(3) using the address returned from <code>pmMetricSpec</code> via <code>rsltp</code>. The convenience macro <code>pmFreeMetricSpec</code> is a thinly disguised wrapper for <code><a href="/docs/linux/man/3-free/">free</a></code>(3). </p>
<p> <code>pmParseMetricSpec</code> returns <code>PM_ERR_GENERIC</code> and a dynamically allocated error message string in <code>errmsg</code>, if the given <code>string</code> does not parse. Be sure to <code><a href="/docs/linux/man/3-free/">free</a></code>(3) the error message string in this situation. </p>
<p> In the case of an error, <code>rsltp</code> is undefined. In the case of success, <code>errmsg</code> is undefined. If <code>rsltp-&gt;ninst</code> is 0, then <code>rsltp-&gt;inst[0]</code> is undefined.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) and <code><a href="/docs/linux/man/3-pmlookupname/">pmLookupName</a></code>(3). </p>
