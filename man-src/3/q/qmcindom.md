---
title: "qmcindom(3)"
name: "qmcindom"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qmcindom/"
description: "QmcIndom – container for a instance domain description"
---

<p><code>QmcIndom</code> &#8211; container for a instance domain description</p>
<h2>C++ Synopsis</h2>
<p><code> #include &lt;QmcIndom.h&gt; </p>
<p> CC &#8230; -lqmc -lpcp </code></p>
<h2>Description</h2>
<p>A <code>QmcIndom</code> object represents a <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) instance domain. This includes a description of all the instances in the instance domain. </p>
<p> A <code>QmcInstance</code> is a structure used to describe each instance in the instance domain. This includes: </p>
<p> &#8211; internal identifier. If this is less than zero, the instance is treated as a NULL entry in the instance table. </p>
<p> &#8211; external name </p>
<p> &#8211; reference count, ie. the number of <code>QmcMetric</code> objects referring to this instance. </p>
<p> &#8211; the likely position of the instance in the <code>pmResult</code> from a <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3). This is also used to indicate the position of the next NULL instance in the instance table, if this entry is also NULL. </p>
<p> &#8211; a flag indicating if the instance was in the last <code><a href="/docs/linux/man/3-pmgetindom/">pmGetInDom</a></code>(3). </p>
<p> The <code>QmcIndom</code> object has a list of <code>QmcInstance</code> structures, and various flags and counters to support dynamic instance domains where instances may come and go with each fetch and efficient profile generation.</p>
<h2>Constructors</h2>
<dl COMPACT>
<dt><code>QmcIndom::QmcIndom(int type, QmcDesc &amp;desc);</code></p>
<dd>Calls <code><a href="/docs/linux/man/3-pmgetindom/">pmGetInDom</a></code>(3) and <code><a href="/docs/linux/man/3-pmgetindomarchive/">pmGetInDomArchive</a></code>(3) for host and archive contexts to obtain the entire instance list for the instance domain of <i>type</i> and identified in <i>desc</i>.</dl>
<h2>Dynamic Indoms</h2>
<p>The support of dynamic instance domains for live contexts is complex since many metrics may be referencing any of the instances in the domain. Therefore the instance list may be sparse as the position of instances in the list must be maintained. </p>
<p> When the instance domain is updated, instances may be removed from the list if they are not in the new instance list (as returned by <code><a href="/docs/linux/man/3-pmgetindom/">pmGetInDom</a></code>(3)) and is not referenced by any metrics. Each instance in the new list is then compared with the old list to determine which instances are still active, and any new instances need to be added. An instance is considered the same if both the internal and external identifiers are the same. New instances are first inserted into positions of deleted instances before being appended to the list. </p>
<p> This algorithm is expensive (potentially O(N^2)).</p>
<dl COMPACT>
<dt><code>bool changed() const;</code></p>
<dd>Returns <code>true</code> if the instance domain may have changed in the last fetch.</p>
<dt><code>void newFetch();</code></p>
<dd>Reset the flags that may have indicated that the instance domain had changed. This is called by <code>QmcContext::fetch</code>.</p>
<dt><code>void hasChanged();</code></p>
<dd>Set the flags to indicate that the instance domain may have changed. This is called by <code>QmcMetric::extractValues</code>.</p>
<dt><code>int update();</code></p>
<dd>Update the instance domain as described above. On subsequent calls, before the next fetch, this method will remove any instances that are no longer referenced without updating the instance list with a <code><a href="/docs/linux/man/3-pmgetindom/">pmGetInDom</a></code>(3) call.</p>
<dt><code>uint_t numInsts() const;</code></p>
<dd>Returns the number of instances that are not NULL.</p>
<dt><code>uint_t numActiveInsts() const;</code></p>
<dd>Returns the number of instances that are active according to the last <code>QmcIndom::update</code> call.</p>
<dt><code>uint_t listLen() const;</code></p>
<dd>Returns the length of the instance list, including NULL instances.</dl>
<h2>Profiles</h2>
<p>The algorithm for determining the most compact profile uses the number of instances (<code>_instances.length()</code>), the number of referenced instances (<code>_count</code>), the number of active instances (<code>_numActive</code>) and the number of referenced active instances (<code>_numActiveRef</code>). </p>
<pre>if (all active instances are referenced
 or there are no active instances)
 request all instances implicitly
else if (the number of referenced instances
 is less than the number of active
 instances that are not referenced)
 delete all instances from profile
 add all referenced instances
else
 add all instances to profile
 delete all instances that are not referenced </pre>
<dl COMPACT>
<dt><code>bool diffProfile() const;</code></p>
<dd>Returns <code>true</code> if the profile has potentially changed since the last call to <code>QmcIndom::genProfile</code>.</p>
<dt><code>int genProfile();</code></p>
<dd>Generates a new profile for the instance domain. a <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) error code is returned if the profile failed.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-qmc/">QMC</a></code>(3), <code><a href="/docs/linux/man/3-qmccontext/">QmcContext</a></code>(3), <code><a href="/docs/linux/man/3-qmcdesc/">QmcDesc</a></code>(3), <code><a href="/docs/linux/man/3-qmcmetric/">QmcMetric</a></code>(3), <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3), <code><a href="/docs/linux/man/3-pmflush/">pmflush</a></code>(3), <code><a href="/docs/linux/man/3-pmgetindom/">pmGetInDom</a></code>(3), <code><a href="/docs/linux/man/3-pmgetindomarchive/">pmGetInDomArchive</a></code>(3) and <code><a href="/docs/linux/man/3-pmprintf/">pmprintf</a></code>(3).</p>
<h2>Diagnostics</h2>
<p>Error messages are generated using <code><a href="/docs/linux/man/3-pmprintf/">pmprintf</a></code>(3) but are not flushed. It is the responsibility of the user to call <code><a href="/docs/linux/man/3-pmflush/">pmflush</a></code>(3) to output any messages. </p>
<p> Additional diagnostics may be activated by adding <code>DBG_TRACE_PMC</code> and <code>DBG_TRACE_INDOM</code> to the global <i>pmDebug</i>.</p>
<h2>Bugs</h2>
<p>User&#8217;s have no control over the algorithm used to generate the profile. In the case of <i>proc</i> metrics, an implicit profile could be generated if all process instances are required, even though this will result in no values being returned in the fetch.</p>
