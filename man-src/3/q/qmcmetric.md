---
title: "qmcmetric(3)"
name: "qmcmetric"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qmcmetric/"
description: "QmcMetric – container for a metric and all its values"
---

<p><code>QmcMetric</code> &#8211; container for a metric and all its values</p>
<h2>C++ Synopsis</h2>
<p><code> #include &lt;pcp/pmc/Metric.h&gt; </p>
<p> CC &#8230; -lpcp_pmc -lpcp </code></p>
<h2>Description</h2>
<p>A <code>QmcMetric</code> object is a container for a single metric and all its values. </p>
<p> The <code>QmcMetricValue</code> structure is used to hold the instance index, values and errors of each instance. In the case of a singular metric, a single <code>QmcMetricValue</code> object is used. </p>
<p> A <code>QmcMetric</code> object consists of a list of <code>QmcMetricValue</code> objects, indexes to the descriptors in the metric&#8217;s <code>QmcGroup</code> and <code>QmcContext</code> and flags to indicate if the instances are explicit or implicit, and if only active metrics are required after <code>QmcMetric::updateIndom</code> is called.</p>
<h2>Constructors</h2>
<p>Metrics should be constructed through the <code>QmcGroup::addMetric</code> methods as this will ensure that the references to the metric&#8217;s context, descriptor and instance domain are correctly initialized.</p>
<h2>Instances</h2>
<p>For metrics with an instance domain it is possible to add and remove any instance, and also update the instance list to reflect changes in a dynamic instance domain.</p>
<dl COMPACT>
<dt><code>bool updateIndom();</code></p>
<dd>Update the metric to include new instances. This method will first call <code>QmcContext::update</code> to update the instance domain. If the <i>active</i> flag is set in the <code>QmcGroup::addMetric</code> call, only instances will exported by the metric, otherwise the metric will export all instances listed in the domain. </p>
<p> The ordering of instances may change as a result of this call. Instances that already existed will keep their current and previous values and errors, even if they are in a different order.</p>
<dt><code>int addInst(QString const&amp; name);</code></p>
<dd>Add the instance <code>name</code> to the metric. If the instance does not exist in the instance domain, a <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) error will be returned. This method ignores the value of the <i>active</i> flag set in the <code>QmcMetric</code> constructor.</p>
<dt><code>void removeInst(uint_t index);</code></p>
<dd>Remove the instance at position <i>index </i> from the metric.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-qmc/">QMC</a></code>(3), <code><a href="/docs/linux/man/3-qmc_context/">QMC_Context</a></code>(3), <code><a href="/docs/linux/man/3-qmc_group/">QMC_Group</a></code>(3), <code><a href="/docs/linux/man/3-pmflush/">pmflush</a></code>(3) and <code><a href="/docs/linux/man/3-pmprintf/">pmprintf</a></code>(3).</p>
<h2>Diagnostics</h2>
<p>Error messages are generated using <code><a href="/docs/linux/man/3-pmprintf/">pmprintf</a></code>(3) but are not flushed. It is the responsibility of the user to call <code><a href="/docs/linux/man/3-pmflush/">pmflush</a></code>(3) to output any messages. </p>
<p> Additional diagnostics may be activated by adding <code>DBG_TRACE_PMC</code> to the global <i>pmDebug</i>.</p>
