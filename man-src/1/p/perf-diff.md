---
title: "perf-diff(1)"
name: "perf-diff"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-diff/"
description: "perf-diff – Read perf.data files and display the differential profile"
---

<h2 class="name">NAME</h2>
<p> perf-diff &#8211; Read perf.data files and display the differential profile </p>
<h2>SYNOPSIS</h2>
<pre><code>
perf diff[baseline file][data file1][[data file2]...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This command displays the performance difference amongst two or more perf.data files captured via perf record. </p>
<p> If no parameters are passed it will assume perf.data.old and perf.data. </p>
<p> The differential profile is displayed only for events matching both specified perf.data files.</p>
<h2>OPTIONS</h2>
<p> -D, &#8211;dump-raw-trace</p>
<dl>
<dt>
<dd> Dump raw trace in ASCII.</dl>
<p> -m, &#8211;modules</p>
<dl>
<dt>
<dd> Load module symbols. WARNING: use only with -k and LIVE kernel</dl>
<p> -d, &#8211;dsos=</p>
<dl>
<dt>
<dd> Only consider symbols in these dsos. CSV that understands m[blue]<code>file://filename</code>m[] entries. This option will affect the percentage of the Baseline/Delta column. See &#8211;percentage for more info.</dl>
<p> -C, &#8211;comms=</p>
<dl>
<dt>
<dd> Only consider symbols in these comms. CSV that understands m[blue]<code>file://filename</code>m[] entries. This option will affect the percentage of the Baseline/Delta column. See &#8211;percentage for more info.</dl>
<p> -S, &#8211;symbols=</p>
<dl>
<dt>
<dd> Only consider these symbols. CSV that understands m[blue]<code>file://filename</code>m[] entries. This option will affect the percentage of the Baseline/Delta column. See &#8211;percentage for more info.</dl>
<p> -s, &#8211;sort=</p>
<dl>
<dt>
<dd> Sort by key(s): pid, comm, dso, symbol, cpu, parent, srcline. Please see description of &#8211;sort in the perf-report man page.</dl>
<p> -t, &#8211;field-separator=</p>
<dl>
<dt>
<dd> Use a special separator character and don&#8217;t pad with spaces, replacing all occurrences of this separator in symbol names (and other output) with a <i>.</i> character, that thus it&#8217;s the only non valid separator.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Be verbose, for instance, show the raw counts in addition to the diff.</dl>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> Don&#8217;t complain, do it.</dl>
<p> &#8211;symfs=&lt;directory&gt;</p>
<dl>
<dt>
<dd> Look for files with symbols relative to this directory.</dl>
<p> -b, &#8211;baseline-only</p>
<dl>
<dt>
<dd> Show only items with match in baseline.</dl>
<p> -c, &#8211;compute</p>
<dl>
<dt>
<dd> Differential computation selection &#8211; delta,ratio,wdiff (default is delta). See COMPARISON METHODS section for more info.</dl>
<p> -p, &#8211;period</p>
<dl>
<dt>
<dd> Show period values for both compared hist entries.</dl>
<p> -F, &#8211;formula</p>
<dl>
<dt>
<dd> Show formula for given computation.</dl>
<p> -o, &#8211;order</p>
<dl>
<dt>
<dd> Specify compute sorting column number.</dl>
<p> &#8211;percentage</p>
<dl>
<dt>
<dd> Determine how to display the overhead percentage of filtered entries. Filters can be applied by &#8211;comms, &#8211;dsos and/or &#8211;symbols options. </p>
<dl>
<dt>
<dd>
<pre>
&quot;relative&quot; means it's relative to filtered entries only so that the
sum of shown entries will be always 100%.  &quot;absolute&quot; means it retains
the original value before and after the filter is applied.
</pre>
</dl>
</dl>
<h2>COMPARISON</h2>
<p> The comparison is governed by the baseline file. The baseline perf.data file is iterated for samples. All other perf.data files specified on the command line are searched for the baseline sample pair. If the pair is found, specified computation is made and result is displayed. </p>
<p> All samples from non-baseline perf.data files, that do not match any baseline entry, are displayed with empty space within baseline column and possible computation results (delta) in their related column. </p>
<p> Example files samples: &#8211; file A with samples f1, f2, f3, f4, f6 &#8211; file B with samples f2, f4, f5 &#8211; file C with samples f1, f2, f5 </p>
<p> Example output: x &#8211; computation takes place for pair b &#8211; baseline sample percentage </p>
<dl>
<dt>
<dd> &bull; perf diff A B C </p>
<dl>
<dt>
<dd>
baseline / A compute / B compute / C samples&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -b x f1 b x x f2 b f3 b x f4 b f6 x x f5
</dl>
</dl>
<dl>
<dt>
<dd> &bull; perf diff B A C </p>
<dl>
<dt>
<dd>
baseline / B compute / A compute / C samples&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -b x x f2 b x f4 b x f5 x x f1 x f3 x f6
</dl>
</dl>
<dl>
<dt>
<dd> &bull; perf diff C B A </p>
<dl>
<dt>
<dd>
<pre><code>
baseline / C compute / B compute / A samples-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -b x f1 b x x f2 b x f5 x f3 x x f4 x f6
</code></pre>
</dl>
</dl>
<h2>COMPARISON METHODS</h2>
<h3>delta</h3>
<p> If specified the <i>Delta</i> column is displayed with value <i>d</i> computed as: </p>
<dl>
<dt>
<dd>
<pre>
d = A-&gt;period_percent - B-&gt;period_percent
</pre>
</dl>
<p> with: &#8211; A/B being matching hist entry from data/baseline file specified (or perf.data/perf.data.old) respectively. </p>
<dl>
<dt>
<dd> &bull; period_percent being the % of the hist entry period value within single data file</dl>
<dl>
<dt>
<dd> &bull; with filtering by -C, -d and/or -S, period_percent might be changed relative to how entries are filtered. Use &#8211;percentage=absolute to prevent such fluctuation.</dl>
<h3>ratio</h3>
<p> If specified the <i>Ratio</i> column is displayed with value <i>r</i> computed as: </p>
<dl>
<dt>
<dd>
<pre>
r = A-&gt;period / B-&gt;period
</pre>
</dl>
<p> with: &#8211; A/B being matching hist entry from data/baseline file specified (or perf.data/perf.data.old) respectively. </p>
<dl>
<dt>
<dd> &bull; period being the hist entry period value</dl>
<h3>wdiff:WEIGHT-B,WEIGHT-A</h3>
<p> If specified the <i>Weighted diff</i> column is displayed with value <i>d</i> computed as: </p>
<dl>
<dt>
<dd>
<pre>
d = B-&gt;period * WEIGHT-A - A-&gt;period * WEIGHT-B
</pre>
</dl>
<dl>
<dt>
<dd> &bull; A/B being matching hist entry from data/baseline file specified (or perf.data/perf.data.old) respectively.</dl>
<dl>
<dt>
<dd> &bull; period being the hist entry period value</dl>
<dl>
<dt>
<dd> &bull; WEIGHT-A/WEIGHT-B being user supplied weights in the the <i>-c</i> option behind <i>:</i> separator like <i>-c wdiff:1,2</i>.</dl>
<dl>
<dt>
<dd> &bull; WEIGHT-A being the weight of the data file</dl>
<dl>
<dt>
<dd> &bull; WEIGHT-B being the weight of the baseline data file</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-record/">perf-record</a></code>(1), <code><a href="/docs/linux/man/1-perf-report/">perf-report</a></code>(1) </p>
<h2>Index</h2>
