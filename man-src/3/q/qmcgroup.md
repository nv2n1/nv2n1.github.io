---
title: "qmcgroup(3)"
name: "qmcgroup"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qmcgroup/"
description: "QmcGroup – container representing a single fetch group of metrics from multiple sources"
---

<p><code>QmcGroup</code> &#8211; container representing a single fetch group of metrics from multiple sources</p>
<h2>C++ Synopsis</h2>
<p><code> #include &lt;QmcGroup.h&gt; </p>
<p> CC &#8230; -lqmc -lpcp </code></p>
<h2>Description</h2>
<p>A <code>QmcGroup</code> object is a container for contexts and metrics that should be fetched at the same time. The class manages the <code><a href="/docs/linux/man/3-qmccontext/">QmcContext</a></code>(3) objects, timezones and bounds for every context created with <code>QmcGroup::use</code> and <code>QmcGroup::addMetric</code>.</p>
<h2>CONSTRUCTORS &amp; DESTRUCTOR</h2>
<dl COMPACT>
<dt><code>~QmcGroup();</code></p>
<dd>Destructor which destroys all metrics and contexts created by this group.</p>
<dt><code>QmcGroup(bool restrictArchives = false);</code></p>
<dd>Construct a new fetch group. <i>restrictArchives</i> will restrict the creating of multiple archive contexts created from the same host.</dl>
<h2>Contexts</h2>
<p>The default context of the group is defined as the first context created with <code>QmcGroup::use </code> before the first call to <code>QmcGroup::addMetric</code>. If no context is created before the first metric is added, the localhost is used as the default context. Therefore, if any metrics specifications contain archive sources, an archive source must have been created with <code>QmcGroup::use</code> to avoid an error for mixing context types.</p>
<dl COMPACT>
<dt><code>uint_t numContexts() const;</code></p>
<dd>The number of valid contexts created in this group.</p>
<dt><code>QmcContext const&amp; context(uint_t index) const</code></p>
<dd>Return a handle to a context.</p>
<dt><code>QmcContext&amp; context(uint_t index);</code></p>
<dd>Return a modifiable handle to a context.</p>
<dt><code>int mode() const;</code></p>
<dd>Return the type of context, either <code>PM_CONTEXT_LOCAL</code>, <code>PM_CONTEXT_HOST</code> or <code>PM_CONTEXT_ARCHIVE</code>.</p>
<dt><code>QmcContext* which() const;</code></p>
<dd>Return a handle to the current context of this group. This does not call <code><a href="/docs/linux/man/3-pmusecontext/">pmUseContext</a></code>(3) so it may not be the current <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) context.</p>
<dt><code>uint_t whichIndex() const</code></p>
<dd>The index to the current group context.</p>
<dt><code>int use(int type, char const* source);</code></p>
<dd>Use the context of <i>type</i> from <i>source</i>. If a context to this <i>source</i> already exists in this group, that context will become the current <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) context. Otherwise a new context will be created. The result is the <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) context handle for the <code>QmcGroup::context</code> or a <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) error code if the context failed.</p>
<dt><code>bool defaultDefined() const;</code></p>
<dd>Returns <code>true</code> if a default context has been determined.</p>
<dt><code>int useDefault();</code></p>
<dd>Use the default context. If a default context has not been created, the context to the local host will be attempted. A result less than zero indicates that the method failed with the <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) error encoded in the result.</p>
<dt><code>void createLocalContext();</code></p>
<dd>Create and use a context to the local host. A result less than zero indicates that the method failed with the <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) error encoded in the result.</dl>
<h2>Metrics</h2>
<p>These <code>addMetric</code> methods should be used to create new metrics as the <code>QmcMetric</code> constructors are private. These methods will always return a pointer to a <code>QmcMetric</code> object, however the <code>QmcMetric::status()</code> field should be checked to ensure the metric is valid.</p>
<dl COMPACT>
<dt><code>QmcMetric* addMetric(char const* str, double theScale = 0.0,</code></p>
<dd><code>bool active = false);</code> </p>
<p> Add the metric <i>str</i> to the group, with a scaling factor of <i>scale</i>. If <i>active</i> is set the metric will use only active instances (see <code><a href="/docs/linux/man/3-qmcmetric/">QmcMetric</a></code>(3)).</p>
<dt><code>QmcMetric* addMetric(pmMetricSpec* theMetric, double theScale</code></p>
<dd><code>= 0.0, bool active);</code> </p>
<p> Add the metric <i>theMetric</i> to the group, with a scaling factor of <i>scale</i>. If <i>active</i> is set the metric will use only active instances (see <code><a href="/docs/linux/man/3-qmcmetric/">QmcMetric</a></code>(3)).</p>
<dt><code>int fetch(bool update = true);</code></p>
<dd>Fetch all the metrics in all the contexts in this group. If <i>update</i> is equal to <code>true</code>, all counter metrics will be automatically converted to rates (see <code><a href="/docs/linux/man/3-qmcmetric/">QmcMetric</a></code>(3)).</p>
<dt><code>int setArchiveMode(int mode, const struct timeval *when,</code></p>
<dd><code>int interval);</code> </p>
<p> Set the mode and time to access all archive contexts in this group. See <code><a href="/docs/linux/man/3-pmsetmode/">pmSetmode</a></code>(3) for more details.</dl>
<h2>Timezones</h2>
<p>These methods assist in the management of multiple timezones and help to control the current timezone.</p>
<dl COMPACT>
<dt><code>enum TimeZoneFlag { localTZ, userTZ, groupTZ, unknownTZ };</code></p>
<dd>Enumeration used to describe the origin of the default timezone. <code>localTZ</code>, <code>userTZ</code> and <code>groupTZ</code> indicate that the timezone was set with <code>QmcGroup::useLocalTZ</code>, <code>QmcGroup::useTZ(QString const&amp;)</code> and <code>QmcGroup::useTZ()</code> respectively. <code>unknownTZ</code> indicates that a timezone has not been set. <code>userTZ</code> indicates that the timezone was</p>
<dt><code>int useTZ();</code></p>
<dd>Use the timezone of the current group context as the default.</p>
<dt><code>int useTZ(const QString &amp;tz);</code></p>
<dd>Add and use <i>tz</i> as the default timezone of this group.</p>
<dt><code>int useLocalTZ();</code></p>
<dd>Use the timezone of the localhost as the default for this group.</p>
<dt><code>void defaultTZ(QString &amp;label, QString &amp;tz);</code></p>
<dd>Return the <i>label</i> and <i>tz</i> string of the default timezone of this group.</p>
<dt><code>TimeZoneFlag defaultTZ() const</code></p>
<dd>Return the origin of the default timezone.</p>
<dt><code>int useDefaultTZ();</code></p>
<dd>Set the timezone to be the default timezone as defined in a previous call to <code>QmcGroup::useTZ</code> or <code>QmcGroup::useLocalTZ</code>.</p>
<dt><code>struct timeval const&amp; logStart() const;</code></p>
<dd>Return the earliest starting time of any archives in this group. Assumes that <code>QmcGroup::updateBounds</code> has been called.</p>
<dt><code>struct timeval const&amp; logEnd() const;</code></p>
<dd>Return the latest finish time of any archives in this group. Assumes that <code>QmcGroup::updateBounds</code> has been called.</p>
<dt><code>void updateBounds();</code></p>
<dd>Determine the earliest start and latest finish times of all archives in this group.</p>
<dt><code>int sendTimezones();</code></p>
<dd>Send the current timezones to <code>kmtime (3).</code></dl>
<h2>Debugging</h2>
<dl COMPACT>
<dt><code>void dump(ostream &amp;os);</code></p>
<dd>Dump state information about this group to <i>os</i>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-qmc/">QMC</a></code>(3), <code><a href="/docs/linux/man/3-qmccontext/">QmcContext</a></code>(3), <code><a href="/docs/linux/man/3-qmcmetric/">QmcMetric</a></code>(3), <code><a href="/docs/linux/man/3-pmflush/">pmflush</a></code>(3), <code><a href="/docs/linux/man/3-pmprintf/">pmprintf</a></code>(3) and <code><a href="/docs/linux/man/3-pmsetmode/">pmSetMode</a></code>(3).</p>
<h2>Diagnostics</h2>
<p>Error messages are generated using <code><a href="/docs/linux/man/3-pmprintf/">pmprintf</a></code>(3) but are not flushed. It is the responsibility of the user to call <code><a href="/docs/linux/man/3-pmflush/">pmflush</a></code>(3) to output any messages. </p>
<p> Additional diagnostics may be activated by adding <code>DBG_TRACE_PMC</code> to the global <i>pmDebug</i>.</p>
