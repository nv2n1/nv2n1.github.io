---
title: "pmstore(1)"
name: "pmstore"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmstore/"
description: "pmstore – modify performance metric values"
---

<h2>NAME</h2>
<p> <code>pmstore</code> &#8211; modify performance metric values</p>
<h2>SYNOPSIS</h2>
<p> <code>pmstore</code> [<code>-Lf</code>] [<code>-h</code> <i>host</i>] [<code>-i</code> <i>instances</i>] [<code>-K</code> <i>spec</i>] [<code>-n</code> <i>pmnsfile</i>] <i>metricname</i> <i>value</i></p>
<h2>DESCRIPTION</h2>
<p> Under certain circumstances, it is useful to be able to modify the values of performance metrics, for example to re-initialize counters or to assign new values to metrics that act as control variables. </p>
<p> <code>pmstore</code> changes the current values for the nominated instances of a single performance metric, as identified by <i>metricname</i> and the list of instance identifiers following the <code>-i</code> argument. <i>instances</i> must be a single argument, with elements of the list separated by commas and/or white space. By default all instances of <i>metricname</i> will be updated. </p>
<p> Normally <code>pmstore</code> operates on the default Performance Metrics Name Space (PMNS), however if the <code>-n</code> option is specified an alternative namespace is loaded from the file <i>pmnsfile.</i> </p>
<p> Unless directed to another host by the <code>-h</code> option, <code>pmstore</code> will interact with the Performance Metric Collector Daemon (PMCD) on the local host. </p>
<p> The <code>-L</code> option causes <code>pmstore</code> to use a local context to store to metrics from PMDAs on the local host without PMCD. Only some metrics are available in this mode. The <code>-h</code> and <code>-L</code> options are mutually exclusive. </p>
<p> The <code>-f</code> option forces the given value to be stored, even if there is no current value set. </p>
<p> The interpretation of <i>value</i> is dependent on the syntax used in its specification and the underlying data type of <i>metricname</i>, as follows.</p>
<dl>
<dt>1.</p>
<dd> If the metric has an <code>integer</code> type, then <i>value</i> should be an optional leading hyphen, followed either by decimal digits or &#8220;0x&#8221; and some hexadecimal digits. &#8220;0X&#8221; is also acceptable in lieu of &#8220;0x&#8221;. See <code><a href="/docs/linux/man/3-strtol/">strtol</a></code>(3) and the related routines.</p>
<dt>2.</p>
<dd> If the metric has a <code>floating point</code> type, then <i>value</i> should be either in the form of an integer described above, or a fixed point number, or a number in scientific notation. See <code><a href="/docs/linux/man/3-strtod/">strtod</a></code>(3).</p>
<dt>3.</p>
<dd> If the metric has a <code>string</code> type, then <i>value</i> is interpreted as a literal string of ASCII characters.</p>
<dt>4.</p>
<dd> If the metric has any other type (i.e. <code>PM_TYPE_EVENT</code> or <code>PM_TYPE_AGGREGATE</code>) then no encoding of <i>value</i> from the command line makes sense, and the values of these metrics cannot be modified with <code>pmstore</code>.</dl>
<p> The output reports the old value and the new value for each updated instance of the requested metric. </p>
<p> When using the <code>-L</code> option to fetch metrics from a local context, the <code>-K</code> option may be used to control the DSO PMDAs that should be made accessible. The <i>spec</i> argument conforms to the syntax described in <code><a href="/docs/linux/man/3-__pmspeclocalpmda/">__pmSpecLocalPMDA</a></code>(3). More than one <code>-K</code> option may be used.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_VAR_DIR/pmns/</code><i>*</i></p>
<dd> default PMNS specification files</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pminfo/">pminfo</a></code>(1), <code><a href="/docs/linux/man/1-pmval/">pmval</a></code>(1), <code><a href="/docs/linux/man/3-__pmspeclocalpmda/">__pmSpecLocalPMDA</a></code>(3), <code><a href="/docs/linux/man/3-strtod/">strtod</a></code>(3) and <code><a href="/docs/linux/man/3-strtol/">strtol</a></code>(3).</p>
<h2>DIAGNOSTICS</h2>
<p> Two messages indicate a mismatch between the internal data type for <i>metricname</i> and the <i>value</i> provided. </p>
<p> The value &quot;???&quot; is out of range for the data type (PM_TYPE_&#8230;) </p>
<p> The value &quot;???&quot; is incompatible with the data type (PM_TYPE_&#8230;) </p>
<h2>Index</h2>
