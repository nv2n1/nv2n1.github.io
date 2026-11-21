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
<dt><code>bltk_report</code></dt>
<dd> automated report creation</dd>
<dt><code>bltk_report_table</code></dt>
<dd> summary table creation from several results folders</dd>
<dt><code>bltk_plot</code></dt>
<dd> graph drawing</dd></dl>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> theis help</dd>
<dt><code>-1</code></dt>
<dd> first statistic item of score file is ignored</dd>
<dt><code>-2 </code>item:num</dt>
<dd> statistic from item &#8216;item&#8217;, &#8216;num&#8217; number of score file</dd>
<dt><code>-f</code></dt>
<dd> statistics file name</dd></dl>
<h2>SPECIFIC OPTIONS</h2>
<p> <code>bltk_report</code></p>
<dl>
<dl>
<dt><code>-o</code></dt>
<dd> print report to output</dd>
<dt><code>-K </code>string</dt>
<dd> comment string</dd>
<dt><code>-R </code>filename</dt>
<dd> argument will be used as report file name</dd>
<dt><code>-3 </code></dt>
<dd> first statistic item of stat.log file is ignored</dd>
<dt><code>-4 </code>item:num</dt>
<dd> statistic from item &#8216;item&#8217;, &#8216;num&#8217; number of stat.log file</dd>
<dt><code>-E</code></dt>
<dd> errors being ignored (allows to create report file anyway)</dd>
<dt><code>-i</code></dt>
<dd> idle mode</dd></dl>
</dl>
<p> <code>bltk_report_table</code></p>
<dl>
<dl>
<dt><code>-d</code></dt>
<dd> debugging mode</dd>
<dt><code>-s</code></dt>
<dd> sort result lines</dd>
<dt><code>-t</code></dt>
<dd> Excel-compatible file format</dd>
<dt><code>-3</code></dt>
<dd> first statistic item of stat.log file is ignored</dd>
<dt><code>-4 </code>item:num</dt>
<dd> statistic from item &#8216;item&#8217;, &#8216;num&#8217; number of stat.log file</dd>
<dt><code>-u</code></dt>
<dd> only columns which contain different values will be included into table</dd>
<dt><code>-E</code></dt>
<dd> errors being ignored (allows to create result table anyway)</dd>
<dt><code>-e</code></dt>
<dd> skip error results</dd>
<dt><code>-F </code>filter</dt>
<dd> only fields from filter file will be included into table (see doc/filter as an example)</dd>
<dt><code>-S</code></dt>
<dd> split mode &#8211; split multiple values to columns</dd>
<dt><code>-R</code></dt>
<dd> analyze all results dirs under passed directories</dd></dl>
</dl>
<p> <code>bltk_plot</code></p>
<dl>
<dl>
<dt><code>-D</code></dt>
<dd> debugging mode</dd>
<dt><code>-d </code>results_dir</dt>
<dd> results directory name. This option could be passed several times default is current directory.</dd>
<dt><code>-s</code></dt>
<dd> use stat.log file</dd>
<dt><code>-w</code></dt>
<dd> use work.log file</dd>
<dt><code>-x </code>name</dt>
<dd> argument is used to be an X parameter default is &#8216;time&#8217; field</dd>
<dt><code>-y </code>name<code>&#8230;</code></dt>
<dd> argument is used to be an Y parameter this option could be passed several times default is &#8216;cap&#8217; field</dd>
<dt><code>-X </code>x1:x2</dt>
<dd> x range from x1 to x2</dd>
<dt><code>-Y </code>y1:y2</dt>
<dd> y range from y1 to y2</dd>
<dt><code>-t title</code></dt>
<dd> graph title</dd>
<dt><code>-o </code>options</dt>
<dd> options passed to &#8216;plot&#8217; command</dd>
<dt><code>-v</code></dt>
<dd> print current variables</dd>
<dt><code>-p </code>file</dt>
<dd> save graph to specified file</dd>
<dt><code>-n</code></dt>
<dd> print available field&#8217;s names</dd>
<dt><code>-R</code></dt>
<dd> analyze all results dirs under passed directories</dd></dl>
</dl>
<h2>EXAMPLE</h2>
<dl>
<dt>bltk_report_table &lt;results1&gt; &#8230; &lt;resultsn&gt; &gt;sum</dt>
<dd> Common results table will be generated in &#8216;sum&#8217; file for &lt;results1&gt; &#8230; &lt;resultsn&gt; directories.</dd>
<dt>bltk_report result</dt>
<dd> &#8216;Report&#8217; file will be generated in results directory</dd>
<dt>bltk_plot -y bat -x N &lt;results_dir1&gt; &#8230; &lt;results_dir&gt;</dt>
<dd> Common graph will be generated for &lt;results_dir1&gt; &#8230; &lt;results_dirn&gt;</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-bltk/">bltk</a></code>(1), <code><a href="/docs/linux/man/5-bltk-conf/">bltk.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<pre><code>
Konstantin Karasyov&lt;konstantin.a.karasyov[at] intel.com&gt;
    Vladimir Lebedev&lt;vladimir.p.lebedev[at] intel.com&gt;
</code></pre>
