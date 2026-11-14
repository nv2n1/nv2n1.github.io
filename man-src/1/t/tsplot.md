---
title: "tsplot(1)"
name: "tsplot"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tsplot/"
description: "tsplot – Plot several tsung logs on the same charts, for comparison purpose."
---

<h2>NAME</h2>
<p> tsplot &#8211; Plot several tsung logs on the same charts, for comparison purpose.</p>
<h2>SYNOPSIS</h2>
<p> <code>tsplot</code> [ <code>-c configuration file</code> ] [ <code>-d images output directory</code> ] [ <code>-v verbose</code> ] [ <code>legend logfile</code> ]</p>
<h2>DESCRIPTION</h2>
<p> Tsung comes with a plotting tool using <code>gnuplot</code>, producing some graphs from the <i>tsung.log</i> file data. <code>tsplot</code> is able to plot data from several <i>tsung.log</i> files onto the same charts serie, for further comparison and analyze.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd>
<dt><code>&#8211;config</code></p>
<dd> specifies the configuration file to use. Default is <i>http.en.plots.conf</i>.</p>
<dt><code>-d</code></p>
<dd>
<dt><code>&#8211;outdir</code></p>
<dd> directory where <code>tsplot</code> saves the images it produces, defaults to <i>/tmp/tsung</i>.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> makes <code>tsplot</code> very verbose about what it does.</dl>
<h2>CONFIGURATION</h2>
<p> The configuration file of <code>tsplot</code> allows one to define the plots you want to obtain, from their label to the data they will show. The configuration file adopts a <i>.ini</i> file syntax, each section defining a chart. </p>
<p> <code>tsplot</code> comes with two sample configuration files, namely <i>http.plots.en.conf</i> and <i>pgsql.plots.en.conf</i>. They respectively define charts to be plotted for a <code>tsung</code> HTTP test and a <code>tsung</code> PGSQL test. </p>
<p> A <code>DEFAULT</code> section may be provided, any element configured here may then be overridden into a specific plot section. </p>
<p> Another configuration file is used by <code>tsplot</code>: the <i>tsung/stats.conf</i> one. It&#8217;s used to define by type the statistics to be read into <code>tsung</code> log files, and you shouldn&#8217;t need to edit it, short of adding support for new <code>tsung</code> statistics. </p>
<p> Common settings, to be found into <code>DEFAULT</code> section or any specific chart section.</p>
<dl>
<dt><code>encoding</code></p>
<dd> set here the encoding used thereafter in the file, for labels and titles.</p>
<dt><code>dpi</code></p>
<dd> dpi setting of produced charts images</p>
<dt><code>tn_dpi</code></p>
<dd> dpi setting of produced charts thumbnail images</p>
<dt><code>imgtype</code></p>
<dd> type of chart image to produce, as in <i>png</i> or <i>ps</i> </p>
<p> A complete list might be obtained on the <code>python-matplotlib</code> website, <a rel="nofollow" href="http://matplotlib.sourceforge.net/">http://matplotlib.sourceforge.net/</a></p>
<dt><code>xlabel</code></p>
<dd> default label for horizontal axe, often you want seconds or minutes, depending on xfactor. </p>
<p> Please note you can also set some defaults for ylabel, but this seems not to be a good idea in practise.</p>
<dt><code>xfactor</code></p>
<dd> tsung logs statistics in its logfile every 10 seconds. By default, charts will not scale this and have seconds as horizontal axis units. By setting an xfactor of 60, you have a minute precision on horizontal axis.</p>
<dt><code>yfactor</code></p>
<dd> same as xfactor, but for vertical axis. </p>
<p> Depending on the data you obtain with your tests, you may want to adapt the vertical scale of your plotting. For example, the <code>page.mean</code> statistic is logged in milliseconds by <code>tsung</code>. You may want to display seconds if this unit better fits your measures. Then simply set <code>yfactor = 1000</code>.</p>
<dt><code>styles</code></p>
<dd> set here any number of <code>matplotlib</code> styles you want to use, separated by spaces, as available here: <a rel="nofollow" href="http://matplotlib.sourceforge.net/matplotlib.pylab.html#-plot.">http://matplotlib.sourceforge.net/matplotlib.pylab.html#-plot.</a> </p>
<p> For exemple, set <code>styles = b- g+ r- cx</code> for plotting first dataset (see <code>stats</code> below) with a blue solid line, second with green plus symbols, third with a red line and last with cyan cross symbols. </p>
<p> This could fit a <code>stats = 200.count 400.count</code> stats setting when plotting two <code>tsung</code> logs.</dl>
<p> You then can define any number of plot, one by section, and give them an arbitrary name. The name must be unique, and will be used for naming output images. </p>
<p> Any option available in DEFAULT section is also available in any specific chart section, with the same meaning and effect. The specific setting will systematically override the DEFAULT one. </p>
<dl>
<dt><code>title</code></p>
<dd> Title of the chart, as printed into the resulting image.</p>
<dt><code>stats</code></p>
<dd> The statistics properties to use for this plotting, as named in the <i>tsung/stats</i> configuration file. Please see this bundled file for a list of what is available. </p>
<p> Tsung provide several types of statistics, as documented here: <a rel="nofollow" href="http://tsung.erlang-projects.org/user_manual.html#htoc53.">http://tsung.erlang-projects.org/user_manual.html#htoc53.</a> The two main types of statistics used are <code>sample</code> and <code>counter</code>. A third one is <code>gauge</code> but is only use for a single statistic (users). </p>
<p> sample provides count, mean, stdvar, max, min and gmean (global mean) properties, and counter provides only count and totalcount. gauge provide count and max. </p>
<p> The stats setting can accept several <code>stat.property</code> elements, separated by spaces. </p>
<p> Examples: <code>stats = users.count</code> to plot the number of simultaneously connected users, and <code>stats = 200.count 400.count</code> to plot given HTTP return codes count, both on the same chart. </p>
<p> Please notice <code>tsplot</code> is currently limited to use only one horizontal and only one vertical scales. <code>matplotlib</code> is able to define some more complex drawings, but <code>tsplot</code> is not yet able to benefit from this.</p>
<dt><code>legend</code></p>
<dd> Legend prefix, which will be followed by the legend given on command line. </p>
<p> Each plot on a chart has a legend entry, you configure here the meaning of the plot (say &#8216;concurrent users&#8217;) and <code>tsplot</code> will add it the name of the data serie being plotted (say &#8216;scenario x&#8217;). You&#8217;d obtain this legend: &#8216;concurrent users scenario x&#8217;.</p>
<dt><code>ylabel</code></p>
<dd> label for vertical axe</dl>
<h2>CONFIGURATION EXAMPLE</h2>
<p> Please see the given configuration examples which should be distributed in <i>/usr/share/doc/tsung/tsung-plotter/http.plots.en.conf</i> and <i>/usr/share/doc/tsung/tsung-plotter/pgsql.plots.en.conf</i>.</p>
<h2>BUGS</h2>
<p> Please reports bugs to the mailing list &lt;tsung-users [at] process-one.net&gt; or in the bug tracker &lt;URL:<a rel="nofollow" href="https://support.process-one.net/browse/TSUN">https://support.process-one.net/browse/TSUN</a>&gt;, see also &lt;URL:<a rel="nofollow" href="https://lists.process-one.net/mailman/listinfo/tsung-users">https://lists.process-one.net/mailman/listinfo/tsung-users</a>&gt; for archives.</p>
<h2>AUTHORS</h2>
<p> <code>tsplot</code> is written by Dimitri Fontaine &lt;dim [at] tapoueh.org&gt;. </p>
<h2>Index</h2>
