---
title: "pmlogrewrite(1)"
name: "pmlogrewrite"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmlogrewrite/"
description: "pmlogrewrite – rewrite Performance Co-Pilot archives"
---

<h2>NAME</h2>
<p> <code>pmlogrewrite</code> &#8211; rewrite Performance Co-Pilot archives</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_BINADM_DIR/pmlogrewrite</code> [<code>-Cdiqsvw </code>] [<code>-c</code> <i>config</i>] <i>inlog</i> [<i>outlog</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmlogrewrite</code> reads a set of Performance Co-Pilot (PCP) archive logs identified by <i>inlog</i> and creates a PCP archive log in <i>outlog</i>. Under normal usage, the <code>-c</code> option will be used to nominate a configuration file or files that contains specifications (see the <code>REWRITING RULES SYNTAX</code> section below) that describe how the data and metadata from <i>inlog</i> should be transformed to produce <i>outlog</i>. </p>
<p> The typical uses for <code>pmlogrewrite</code> would be to accommodate the evolution of Performance Metric Domain Agents (PMDAs) where the names, metadata and semantics of metrics and their associated instance domains may change over time, e.g. promoting the type of a metric from a 32-bit to a 64-bit integer, or renaming a group of metrics. Refer to the <code>EXAMPLES</code> section for some additional use cases. </p>
<p> <code>pmlogrewrite</code> is most useful where PMDA changes, or errors in the production environment, result in archives that cannot be combined with <code><a href="/docs/linux/man/1-pmlogextract/">pmlogextract</a></code>(1). By pre-processing the archives with <code>pmlogrewrite</code> the resulting archives may be able to be merged with <code><a href="/docs/linux/man/1-pmlogextract/">pmlogextract</a></code>(1). </p>
<p> The input <i>inlog</i> must be a set of PCP archive logs created by <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), or possibly one of the tools that read and create PCP archives, e.g. <code><a href="/docs/linux/man/1-pmlogextract/">pmlogextract</a></code>(1) and <code><a href="/docs/linux/man/1-pmlogreduce/">pmlogreduce</a></code>(1). <i>inlog</i> is a comma-separated list of names, each of which may be the base name of an archive or the name of a directory containing one or more archives. </p>
<p> If no <code>-c</code> option is specified, then the default behavior simply creates <i>outlog</i> as a copy of <i>inlog</i>. This is a little more complicated than <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1), as each PCP archive is made up of several physical files. </p>
<p> While <code>pmlogrewrite</code> may be used to repair some data consistency issues in PCP archives, there is also a class of repair tasks that cannot be handled by <code>pmlogrewrite</code> and <code><a href="/docs/linux/man/1-pmloglabel/">pmloglabel</a></code>(1) may be a useful tool in these cases.</p>
<h2>COMMAND LINE OPTIONS</h2>
<p> The command line options for <code>pmlogrewrite</code> are as follows:</p>
<dl>
<dt><code>-C</code></p>
<dd> Parse the rewriting rules and quit. <i>outlog</i> is not created. When <code>-C</code> is specified, this also sets <code>-v</code> and <code>-w</code> so that all warnings and verbose messages are displayed as <i>config</i> is parsed.</p>
<dt><code>-c</code><i> config</i></p>
<dd> If <i>config</i> is a file or symbolic link, read and parse rewriting rules from there. If <i>config</i> is a directory, then all of the files or symbolic links in that directory (excluding those beginning with a period &#8220;.&#8221;) will be used to provide the rewriting rules. Multiple <code>-c</code> options are allowed.</p>
<dt><code>-d</code></p>
<dd> Desperate mode. Normally if a fatal error occurs, all trace of the partially written PCP archive <i>outlog</i> is removed. With the <code>-d</code> option, the partially created <i>outlog</i> archive log is not removed.</p>
<dt><code>-i</code></p>
<dd> Rather than creating <i>outlog</i>, <i>inlog</i> is rewritten in place when the <code>-i</code> option is used. A new archive is created using temporary file names and then renamed to <i>inlog</i> in such a way that if any errors (not warnings) are encountered, <i>inlog</i> remains unaltered.</p>
<dt><code>-q</code></p>
<dd> Quick mode, where if there are no rewriting actions to be performed (none of the global data, instance domains or metrics from <i>inlog</i> will be changed), then <code>pmlogrewrite</code> will exit (with status 0, so success) immediately after parsing the configuration file(s) and <i>outlog</i> is not created.</p>
<dt><code>-s</code></p>
<dd> When the &#8220;units&#8221; of a metric are changed, if the dimension in terms of space, time and count is unaltered, then the scaling factor is being changed, e.g. BYTE to KBYTE, or MSEC<font SIZE="-3">-1</font> to USEC<font SIZE="-3">-1</font>, or the composite MBYTE.SEC<font SIZE="-3">-1</font> to KBYTE.USEC<font SIZE="-3">-1</font>. The motivation may be (a) that the original metadata was wrong but the values in <i>inlog</i> are correct, or (b) the metadata is changing so the values need to change as well. The default <code>pmlogrewrite</code> behaviour matches case (a). If case (b) applies, then use the <code>-s</code> option and the values of all the metrics with a scale factor change in each result will be rescaled. For finer control over value rescaling refer to the RESCALE option for the UNITS clause of the metric rewriting rule described below.</p>
<dt><code>-v</code></p>
<dd> Increase verbosity of diagnostic output.</p>
<dt><code>-w</code></p>
<dd> Emit warnings. Normally <code>pmlogrewrite</code> remains silent for any warning that is not fatal and it is expected that for a particular archive, some (or indeed, all) of the rewriting specifications may not apply. For example, changes to a PMDA may be captured in a set of rewriting rules, but a single archive may not contain all of the modified metrics nor all of the modified instance domains and/or instances. Because these cases are expected, they do not prevent <code>pmlogrewrite</code> executing, and rules that do not apply to <i>inlog</i> are silently ignored by default. Similarly, some rewriting rules may involve no change because the metadata in <i>inlog</i> already matches the intent of the rewriting rule to correct data from a previous version of a PMDA. The <code>-w</code> flag forces warnings to be emitted for all of these cases.</dl>
<p> The argument <i>outlog</i> is required in all cases, except when <code>-i</code> is specified.</p>
<h2>REWRITING RULES SYNTAX</h2>
<p> A configuration file contains zero or more rewriting rules as defined below. </p>
<p> Keywords and special punctuation characters are shown below in bolditalic font and are case-insensitive, so METRIC, metric and Metric are all equivalent in rewriting rules. </p>
<p> The character &#8220;#&#8221; introduces a comment and the remainder of the line is ignored. Otherwise the input is relatively free format with optional white space (spaces, tabs or newlines) between lexical items in the rules. </p>
<p> A <code>global</code> rewriting rule has the form: </p>
<p> GLOBAL { <i>globalspec</i> &#8230; } </p>
<p> where <i>globalspec</i> is zero or more of the following clauses:</p>
<dl>
<dt>
<dd>
<p> HOSTNAME -&gt; <i>hostname</i></p>
<dl>
<dt>
<dd>
<p> Modifies the label records in the <i>outlog</i> PCP archive, so that the metrics will appear to have been collected from the host <i>hostname</i>.</dl>
<p> TIME -&gt; <i>delta</i></p>
<dl>
<dt>
<dd>
<p> Both metric values and the instance domain metadata in a PCP archive carry timestamps. This clause forces all the timestamps to be adjusted by <i>delta</i>, where <i>delta</i> is an optional sign &#8220;+&#8221; (the default) or &#8220;-&#8221;, an optional number of hours followed by a colon &#8220;:&#8221;, an optional number of minutes followed by a colon &#8220;:&#8221;, a number of seconds, an optional fraction of seconds following a period &#8220;.&#8221;. The simplest example would be &#8220;30&#8221; to increase the timestamps by 30 seconds. A more complex example would be &#8220;-23:59:59.999&#8221; to move the timestamps backwards by one millisecond less than one day.</dl>
<p> TZ -&gt; &quot;<i>timezone</i>&quot;</p>
<dl>
<dt>
<dd>
<p> Modifies the label records in the <i>outlog</i> PCP archive, so that the metrics will appear to have been collected from a host with a local timezone of <i>timezone</i>. <i>timezone</i> must be enclosed in quotes, and should conform to the valid timezone syntax rules for the local platform.</dl>
</dl>
<p> An <code>indom</code> rewriting rule modifies an instance domain and has the form: </p>
<p> INDOM <i>domain</i>.<i>serial</i> { <i>indomspec</i> &#8230; } </p>
<p> where <i>domain</i> and <i>serial</i> identify one or more existing instance domains from <i>inlog</i> &#8211; typically <i>domain</i> would be an integer in the range 1 to 510 and <i>serial</i> would be an integer in the range 0 to 4194304. </p>
<p> As a special case <i>serial</i> could be an asterisk &#8220;*&#8221; which means the rule applies to every instance domain with a domain number of <i>domain</i>. </p>
<p> If a designated instance domain is not in <i>inlog</i> the rule has no effect. </p>
<p> The <i>indomspec</i> is zero or more of the following clauses:</p>
<dl>
<dt>
<dd>
<p> INAME &quot;<i>oldname</i>&quot; -&gt; &quot;<i>newname</i>&quot;</p>
<dl>
<dt>
<dd>
<p> The instance identified by the external instance name <i>oldname</i> is renamed to <i>newname</i>. Both <i>oldname</i> and <i>newname</i> must be enclosed in quotes. </p>
<p> As a special case, the new name may be the keyword DELETE (with no quotes), and then the instance <i>oldname</i> will be expunged from <i>outlog</i> which removes it from the instance domain metadata and removes all values of this instance for all the associated metrics. </p>
<p> If the instance names contain any embedded spaces then special care needs to be taken in respect of the PCP instance naming rule that treats the leading non-space part of the instance name as the unique portion of the name for the purposes of matching and ensuring uniqueness within an instance domain, refer to <code><a href="/docs/linux/man/3-pmdainstance/">pmdaInstance</a></code>(3) for a discussion of this issue. </p>
<p> As an illustration, consider the hypothetical instance domain for a metric which contains 2 instances with the following names:</p>
<dl>
<dt>
<dd>
<pre>
red
eek urk
</pre>
</dl>
<p> Then some possible INAME clauses might be:</p>
<dl>
<dt><tt>&quot;eek&quot; -&gt; &quot;yellow like a flower&quot;</tt></p>
<dd> Acceptable, <i>oldname</i> &quot;eek&quot; matches the &quot;eek urk&quot; instance.</p>
<dt><tt>&quot;red&quot; -&gt; &quot;eek&quot;</tt></p>
<dd> Error, <i>newname</i> &quot;eek&quot; matches the existing &quot;eek urk&quot; instance.</p>
<dt><tt>&quot;eek urk&quot; -&gt; &quot;red of another hue&quot;</tt></p>
<dd> Error, <i>newname</i> &quot;red of another hue&quot; matches the existing &quot;red&quot; instance.</dl>
</dl>
<p> INDOM -&gt; <i>newdomain</i>.<i>newserial</i></p>
<dl>
<dt>
<dd>
<p> Modifies the metadata for the instance domain and every metric associated with the instance domain. As a special case, <i>newserial</i> could be an asterisk &#8220;*&#8221; which means use <i>serial</i> from the <code>indom</code> rewriting rule, although this is most useful when <i>serial</i> is also an asterisk. So for example:</p>
<dl>
<dt>
<dd> indom 29.* { indom -&gt; 109.* }</dl>
<p> will move all instance domains from domain 29 to domain 109.</dl>
<p> INDOM -&gt; DUPLICATE <i>newdomain</i>.<i>newserial</i></p>
<dl>
<dt>
<dd>
<p> A special case of the previous INDOM clause where the instance domain is a duplicate copy of the <i>domain</i>.<i>serial</i> instance domain from the <i>indom</i> rewriting rule, and then any mapping rules are applied to the copied <i>newdomain</i>.<i>newserial</i> instance domain. This is useful when a PMDA is split and the same instance domain needs to be replicated for domain <i>domain</i> and domain <i>newdomain</i>. So for example if the metrics <i>foo.one</i> and <i>foo.two</i> are both defined over instance domain 12.34, and <i>foo.two</i> is moved to another PMDA using domain 27, then the following rewriting rules could be used:</p>
<dl>
<dt>
<dd> indom 12.34 { indom -&gt; duplicate 27.34 }<br />
 metric foo.two { indom -&gt; 27.34 pmid -&gt; 27.*.* }</dl>
</dl>
<p> INST <i>oldid</i> -&gt; <i>newid</i></p>
<dl>
<dt>
<dd>
<p> The instance identified by the internal instance identifier <i>oldid</i> is renumbered to <i>newid</i>. Both <i>oldid</i> and <i>newid</i> are integers in the range 0 to 2<font SIZE="-3">31</font>-1. </p>
<p> As a special case, <i>newid</i> may be the keyword DELETE and then the instance <i>oldid</i> will be expunged from <i>outlog</i> which removes it from the instance domain metadata and removes all values of this instance for all the associated metrics.</dl>
</dl>
<p> A <code>metric</code> rewriting rule has the form: </p>
<p> METRIC <i>metricid</i> { <i>metricspec</i> &#8230; } </p>
<p> where <i>metricid</i> identifies one or more existing metrics from <i>inlog</i> using either a metric name, or the internal encoding for a metric&#8217;s PMID as <i>domain</i>.<i>cluster</i>.<i>item</i>. In the latter case, typically <i>domain</i> would be an integer in the range 1 to 510, <i>cluster</i> would be an integer in the range 0 to 4095, and <i>item</i> would be an integer in the range 0 to 1023. </p>
<p> As special cases <i>item</i> could be an asterisk &#8220;*&#8221; which means the rule applies to every metric with a domain number of <i>domain</i> and a cluster number of <i>cluster</i>, or <i>cluster</i> could be an asterisk which means the rule applies to every metric with a domain number of <i>domain</i> and an item number of <i>item</i>, or both <i>cluster</i> and <i>item</i> could be asterisks, and rule applies to every metric with a domain number of <i>domain</i>. </p>
<p> If a designated metric is not in <i>inlog</i> the rule has no effect. </p>
<p> The <i>metricspec</i> is zero or more of the following clauses:</p>
<dl>
<dt>
<dd>
<p> DELETE</p>
<dl>
<dt>
<dd>
<p> The metric is completely removed from <i>outlog</i>, both the metadata and all values in results are expunged.</dl>
<p> INDOM -&gt; <i>newdomain</i>.<i>newserial</i> [ <i>pick</i> ]</p>
<dl>
<dt>
<dd>
<p> Modifies the metadata to change the instance domain for this metric. The new instance domain must exist in <i>outlog</i>. </p>
<p> The optional <i>pick</i> clause may be used to select one input value, or compute an aggregate value from the instances in an input result, or assign an internal instance identifier to a single output value. If no <i>pick</i> clause is specified, the default behaviour is to copy all input values from each input result to an output result, however if the input instance domain is singular (indom <code>PM_INDOM_NULL</code>) then the one output value must be assigned an internal instance identifier, which is 0 by default, unless over-ridden by a INST or INAME clause as defined below. </p>
<p> The choices for <i>pick</i> are as follows:</p>
<dl>
<dt>OUTPUT FIRST</p>
<dd> choose the value of the first instance from each input result</p>
<dt>OUTPUT LAST</p>
<dd> choose the value of the last instance from each input result</p>
<dt>OUTPUT INST <i>instid</i></p>
<dd> choose the value of the instance with internal instance identifier <i>instid</i> from each result; the sequence of rewriting rules ensures the OUTPUT processing happens before instance identifier renumbering from any associated <code>indom</code> rule, so <i>instid</i> should be one of the internal instance identifiers that appears in <i>inlog</i></p>
<dt>OUTPUT INAME &quot;<i>name</i>&quot;</p>
<dd> choose the value of the instance with <i>name</i> for its external instance name from each result; the sequence of rewriting rules ensures the OUTPUT processing happens before instance renaming from any associated <code>indom</code> rule, so <i>name</i> should be one of the external instance names that appears in <i>inlog</i></p>
<dt>OUTPUT MIN</p>
<dd> choose the smallest value in each result (metric type must be numeric and output instance will be 0 for a non-singular instance domain)</p>
<dt>OUTPUT MAX</p>
<dd> choose the largest value in each result (metric type must be numeric and output instance will be 0 for a non-singular instance domain)</p>
<dt>OUTPUT SUM</p>
<dd> choose the sum of all values in each result (metric type must be numeric and output instance will be 0 for a non-singular instance domain)</p>
<dt>OUTPUT AVG</p>
<dd> choose the average of all values in each result (metric type must be numeric and output instance will be 0 for a non-singular instance domain)</dl>
<p> If the input instance domain is singular (indom <code>PM_INDOM_NULL</code>) then independent of any <i>pick</i> specifications, there is at most one value in each input result and so FIRST, LAST, MIN, MAX, SUM and AVG are all equivalent and the output instance identifier will be 0. </p>
<p> In general it is an error to specify a rewriting action for the same metadata or result values more than once, e.g. more than one INDOM clause for the same instance domain. The one exception is the possible interaction between the INDOM clauses in the <code>indom</code> and <code>metric</code> rules. For example the metric <i>sample.bin</i> is defined over the instance domain 29.2 in <i>inlog</i> and the following is acceptable (albeit redundant):</p>
<dl>
<dt>
<dd>
<pre><code>
indom 29. * {indom-&gt;109. * } metric sample.bin
{
    indom-&gt;109.2
}
</code></pre>
</dl>
<p> However the following is an error, because the instance domain for <i>sample.bin</i> has two conflicting definitions:</p>
<dl>
<dt>
<dd>
indom 29. * {indom-&gt;109. * } metric sample.bin<br />
{<br />
    indom-&gt;123.2<br />
}
</dl>
</dl>
<p> INDOM -&gt; NULL[ <i>pick</i> ]</p>
<dl>
<dt>
<dd>
<p> The metric (which must have been previously defined over an instance domain) is being modified to be a singular metric. This involves a metadata change and collapsing all results for this metric so that multiple values become one value. </p>
<p> The optional <i>pick</i> part of the clause defines how the one value for each result should be calculated and follows the same rules as described for the non-NULL INDOM case above. </p>
<p> In the absence of <i>pick</i>, the default is OUTPUT FIRST.</dl>
<p> NAME -&gt; <i>newname</i></p>
<dl>
<dt>
<dd>
<p> Renames the metric in the PCP archive&#8217;s metadata that supports the Performance Metrics Name Space (PMNS). <i>newname</i> should not match any existing name in the archive&#8217;s PMNS and must follow the syntactic rules for valid metric names as outlined in <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5).</dl>
<p> PMID -&gt; <i>newdomain</i>.<i>newcluster</i>.<i>newitem</i></p>
<dl>
<dt>
<dd>
<p> Modifies the metadata and results to renumber the metric&#8217;s PMID. As special cases, <i>newcluster</i> could be an asterisk &#8220;*&#8221; which means use <i>cluster</i> from the <code>metric</code> rewriting rule and/or <i>item</i> could be an asterisk which means use <i>item</i> from the <code>metric</code> rewriting rule. This is most useful when <i>cluster</i> and/or <i>item</i> is also an asterisk. So for example:</p>
<dl>
<dt>
<dd> metric 30.*.* { pmid -&gt; 123.*.* }</dl>
<p> will move all metrics from domain 30 to domain 123.</dl>
<p> SEM -&gt; <i>newsem</i></p>
<dl>
<dt>
<dd>
<p> Change the semantics of the metric. <i>newsem</i> should be the XXX part of the name of one of the <code>PM_SEM_XXX</code> macros defined in &lt;pcp/pmapi.h&gt; or <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3), e.g. COUNTER for <code>PM_TYPE_COUNTER</code>. </p>
<p> No data value rewriting is performed as a result of the SEM clause, so the usefulness is limited to cases where a version of the associated PMDA was exporting incorrect semantics for the metric. <code><a href="/docs/linux/man/1-pmlogreduce/">pmlogreduce</a></code>(1) may provide an alternative in cases where re-computation of result values is desired.</dl>
<p> TYPE -&gt; <i>newtype</i></p>
<dl>
<dt>
<dd>
<p> Change the type of the metric which alters the metadata and may change the encoding of values in results. <i>newtype</i> should be the XXX part of the name of one of the <code>PM_TYPE_XXX</code> macros defined in &lt;pcp/pmapi.h&gt; or <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3), e.g. FLOAT for <code>PM_TYPE_FLOAT</code>. </p>
<p> Type conversion is only supported for cases where the old and new metric type is numeric, so <code>PM_TYPE_STRING</code>, <code>PM_TYPE_AGGREGATE</code> and <code>PM_TYPE_EVENT</code> are not allowed. Even for the numeric cases, some conversions may produce run-time errors, e.g. integer overflow, or attempting to rewrite a negative value into an unsigned type.</dl>
<p> UNITS -&gt; <i>newunits</i> [ RESCALE ]</p>
<dl>
<dt>
<dd>
<p> <i>newunits</i> is six values separated by commas. The first 3 values describe the dimension of the metric along the dimensions of space, time and count; these are integer values, usually 0, 1 or -1. The remaining 3 values describe the scale of the metric&#8217;s values in the dimensions of space, time and count. Space scale values should be 0 (if the space dimension is 0), else the XXX part of the name of one of the <code>PM_SPACE_XXX</code> macros, e.g. KBYTE for <code>PM_TYPE_KBYTE</code>. Time scale values should be 0 (if the time dimension is 0), else the XXX part of the name of one of the <code>PM_TIME_XXX</code> macros, e.g. SEC for <code>PM_TIME_SEC</code>. Count scale values should be 0 (if the time dimension is 0), else ONE for <code>PM_COUNT_ONE</code>. </p>
<p> The <code>PM_SPACE_XXX</code>, <code>PM_TIME_XXX</code> and <code>PM_COUNT_XXX</code> macros are defined in &lt;pcp/pmapi.h&gt; or <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3). </p>
<p> When the scale is changed (but the dimension is unaltered) the optional keyword RESCALE may be used to chose value rescaling as per the <code>-s</code> command line option, but applied to just this metric.</dl>
<p> When changing the domain number for a metric or instance domain, the new domain number will usually match an existing PMDA&#8217;s domain number. If this is not the case, then the new domain number should not be randomly chosen; consult <code>$PCP_VAR_DIR/pmns/stdpmid</code> for domain numbers that are already assigned to PMDAs.</dl>
<h2>EXAMPLES</h2>
<p> To promote the values of the per-disk IOPS metrics to 64-bit to allow aggregation over a long time period for capacity planning, or because the PMDA has changed to export 64-bit counters and we want to convert old archives so they can be processed alongside new archives.</p>
<dl>
<dt>
<dd>
metric disk.dev.read{type-&gt;U64} metric disk.dev.write{type-&gt;U64} metric disk.dev.total<br />
{<br />
    type-&gt;U64<br />
}
</dl>
<p> The instances associated with the load average metric <code>kernel.all.load</code> could be renamed and renumbered by the rules below.</p>
<dl>
<dt>
<dd>
#for the Linux PMDA, the kernel.all.load metric is defined<br />
#over instance domain 60.2<br />
indom 60.2<br />
{<br />
    inst 1-&gt;60 iname &#8220;1 minute&#8221;-&gt;&#8221;60 second&#8221; inst 5-&gt;300 iname &#8220;5 minute&#8221;-&gt;&#8221;300 second&#8221; inst 15-&gt;900 iname &#8220;15 minute&#8221;-&gt;&#8221;900 second&#8221;<br />
}
</dl>
<p> If we decide to split the &#8220;proc&#8221; metrics out of the Linux PMDA, this will involve changing the domain number for the PMID of these metrics and the associated instance domains. The rules below would rewrite an old archive to match the changes after the PMDA split.</p>
<dl>
<dt>
<dd>
<pre><code>
#all Linux proc metrics are in 7 clusters
metric 60.8. * {pmid-&gt;123. *.*} metric 60.9. * {pmid-&gt;123. *.*} metric 60.13. * {pmid-&gt;123. *.*} metric 60.24. * {pmid-&gt;123. *.*} metric 60.31. * {pmid-&gt;123. *.*} metric 60.32. * {pmid-&gt;123. *.*} metric 60.51. * {pmid-&gt;123. *.*}
#only one instance domain for Linux proc metrics
    indom 60.9
{
    indom-&gt;123.0
}
</code></pre>
</dl>
<h2>FILES</h2>
<p> For each of the <i>inlog</i> and <i>outlog</i> archive logs, several physical files are used.</p>
<dl>
<dt><i>archive</i><code>.meta</p>
<dd> metadata (metric descriptions, instance domains, etc.) for the archive log</p>
<dt></code><i>archive</i><code>.0</p>
<dd> initial volume of metrics values (subsequent volumes have suffixes 1</code>, <code>2</code>, &#8230;).</p>
<dt><i>archive</i><code>.index</p>
<dd> temporal index to support rapid random access to the other files in the archive log.</dl>
<p> </code></p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/3-pmdainstance/">pmdaInstance</a></code>(3), <code><a href="/docs/linux/man/1-pmdumplog/">pmdumplog</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/1-pmlogextract/">pmlogextract</a></code>(1), <code><a href="/docs/linux/man/1-pmloglabel/">pmloglabel</a></code>(1), <code><a href="/docs/linux/man/1-pmlogreduce/">pmlogreduce</a></code>(1), <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3), <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>DIAGNOSTICS</h2>
<p> All error conditions detected by <code>pmlogrewrite</code> are reported on <i>stderr</i> with textual (if sometimes terse) explanation. </p>
<p> Should the input archive log be corrupted (this can happen if the <code>pmlogger</code> instance writing the log suddenly dies), then <code>pmlogrewrite</code> will detect and report the position of the corruption in the file, and any subsequent information from that archive log will not be processed. </p>
<p> If any error is detected, <code>pmlogrewrite</code> will exit with a non-zero status. </p>
<h2>Index</h2>
