---
title: "bltk_report(1)"
name: "bltk_report"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bltk_report/"
description: "bltk_report – automated report creation bltk_report_table – summary table creation from several results folders bltk_plot – graph drawing"
---

<h2>NAME</h2>
<p> bltk_report &#8211; automated report creation bltk_report_table &#8211; summary table creation from several results folders bltk_plot &#8211; graph drawing</p>
<h2>SYNOPSIS</h2>
<p> <code>bltk_report</code> [-hdofI013EiS] [-r ] [-s ] [-b ] [-c ] [-U ] [-B ] [-D ] [-C ] [-P ] [-K ] [-R ] [-2 ] [-4 ] directory&#8230; </p>
<p> <code>bltk_report_table</code> [-hdstfuEe13SR] [-2 ] [-4 ] [-F ] directory &#8230; </p>
<p> <code>bltk_plot</code> [-hDswy1vnr] [-d ] [-f ] [-x ] [-X ] [-Y ] [-t ] [-o ] [-2 ] [-p ] results_dir &#8230;</p>
<h2>DESCRIPTION</h2>
<p> The following tools are implemented for results analysis:</p>
<dl>
<dt><code>bltk_report</code></p>
<dd> automated report creation</p>
<dt><code>bltk_report_table</code></p>
<dd> summary table creation from several results folders</p>
<dt><code>bltk_plot</code></p>
<dd> graph drawing</dl>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> theis help</p>
<dt><code>-1</code></p>
<dd> first statistic item of score file is ignored</p>
<dt><code>-2 </code>item:num</p>
<dd> statistic from item &#8216;item&#8217;, &#8216;num&#8217; number of score file</p>
<dt><code>-f</code></p>
<dd> statistics file name</dl>
<h2>SPECIFIC OPTIONS</h2>
<p> <code>bltk_report</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-o</code></p>
<dd> print report to output</p>
<dt><code>-K </code>string</p>
<dd> comment string</p>
<dt><code>-R </code>filename</p>
<dd> argument will be used as report file name</p>
<dt><code>-3 </code></p>
<dd> first statistic item of stat.log file is ignored</p>
<dt><code>-4 </code>item:num</p>
<dd> statistic from item &#8216;item&#8217;, &#8216;num&#8217; number of stat.log file</p>
<dt><code>-E</code></p>
<dd> errors being ignored (allows to create report file anyway)</p>
<dt><code>-i</code></p>
<dd> idle mode</dl>
</dl>
<p> <code>bltk_report_table</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-d</code></p>
<dd> debugging mode</p>
<dt><code>-s</code></p>
<dd> sort result lines</p>
<dt><code>-t</code></p>
<dd> Excel-compatible file format</p>
<dt><code>-3</code></p>
<dd> first statistic item of stat.log file is ignored</p>
<dt><code>-4 </code>item:num</p>
<dd> statistic from item &#8216;item&#8217;, &#8216;num&#8217; number of stat.log file</p>
<dt><code>-u</code></p>
<dd> only columns which contain different values will be included into table</p>
<dt><code>-E</code></p>
<dd> errors being ignored (allows to create result table anyway)</p>
<dt><code>-e</code></p>
<dd> skip error results</p>
<dt><code>-F </code>filter</p>
<dd> only fields from filter file will be included into table (see doc/filter as an example)</p>
<dt><code>-S</code></p>
<dd> split mode &#8211; split multiple values to columns</p>
<dt><code>-R</code></p>
<dd> analyze all results dirs under passed directories</dl>
</dl>
<p> <code>bltk_plot</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-D</code></p>
<dd> debugging mode</p>
<dt><code>-d </code>results_dir</p>
<dd> results directory name. This option could be passed several times default is current directory.</p>
<dt><code>-s</code></p>
<dd> use stat.log file</p>
<dt><code>-w</code></p>
<dd> use work.log file</p>
<dt><code>-x </code>name</p>
<dd> argument is used to be an X parameter default is &#8216;time&#8217; field</p>
<dt><code>-y </code>name<code>&#8230;</code></p>
<dd> argument is used to be an Y parameter this option could be passed several times default is &#8216;cap&#8217; field</p>
<dt><code>-X </code>x1:x2</p>
<dd> x range from x1 to x2</p>
<dt><code>-Y </code>y1:y2</p>
<dd> y range from y1 to y2</p>
<dt><code>-t title</code></p>
<dd> graph title</p>
<dt><code>-o </code>options</p>
<dd> options passed to &#8216;plot&#8217; command</p>
<dt><code>-v</code></p>
<dd> print current variables</p>
<dt><code>-p </code>file</p>
<dd> save graph to specified file</p>
<dt><code>-n</code></p>
<dd> print available field&#8217;s names</p>
<dt><code>-R</code></p>
<dd> analyze all results dirs under passed directories</dl>
</dl>
<h2>EXAMPLE</h2>
<dl>
<dt>bltk_report_table &lt;results1&gt; &#8230; &lt;resultsn&gt; &gt;sum</p>
<dd> Common results table will be generated in &#8216;sum&#8217; file for &lt;results1&gt; &#8230; &lt;resultsn&gt; directories.</p>
<dt>bltk_report result</p>
<dd> &#8216;Report&#8217; file will be generated in results directory</p>
<dt>bltk_plot -y bat -x N &lt;results_dir1&gt; &#8230; &lt;results_dir&gt;</p>
<dd> Common graph will be generated for &lt;results_dir1&gt; &#8230; &lt;results_dirn&gt;</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-bltk/">bltk</a></code>(1), <code><a href="/docs/linux/man/5-bltk-conf/">bltk.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<pre><code>
Konstantin Karasyov&lt;konstantin.a.karasyov[at] intel.com&gt;
    Vladimir Lebedev&lt;vladimir.p.lebedev[at] intel.com&gt;
</code></pre>
<h2>Index</h2>
