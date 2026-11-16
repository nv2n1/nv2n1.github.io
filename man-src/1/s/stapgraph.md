---
title: "stapgraph(1)"
name: "stapgraph"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stapgraph/"
description: "stapgraph – systemtap grapher"
---

<h2>NAME</h2>
<p> stapgraph &#8211; systemtap grapher </p>
<h2>SYNOPSIS</h2>
<p> <code>stapgraph</code> [ <i>OPTIONS</i> ] <i>FILENAME</i> [ <i>ARGUMENTS</i> ]<br />
 <code>stapgraph</code> [ <i>OPTIONS</i> ] <code>&#8211;</code> [ <i>ARGUMENTS</i> ]<br />
 <code>stapgraph</code> [ <i>OPTIONS</i> ] <code>-e</code><i> SCRIPT</i> [ <i>ARGUMENTS</i> ] </p>
<h2>DESCRIPTION</h2>
<p> The <i>stapgraph</i> program is a simple frontend to <i>stap</i> that produces graphs from the output of <i>stap</i> scripts. </p>
<p> This manual corresponds to version 1.3. </p>
<h2>OPTIONS</h2>
<p> <i>stapgraph</i> accepts all options accepted by <i>stap.</i> They are passed through to the <i>stap</i> process running the script or probe points. </p>
<h2>USER INTERFACE</h2>
<p> The script that produces results can be started from a dialog within the program, in addition to being launched using the program&#8217;s command line arguments. This dialog allows arguments to be passed to <i>stap</i> and to the script. </p>
<p> When running, a mouse left click on a graph pauses the display of data, even though it is still collected by the program. Dragging the mouse scrolls the graph backwards and forwards in time; clicking the displayed pause button restarts the display of new data. </p>
<p> The scroll wheel can be used to zoom in and out on the graph. </p>
<h2>SCRIPT OUTPUT SYNTAX</h2>
<p> Scripts can output Comma Seperated Values (CSV) which will be interpreted by <i>stapgraph.</i> The first value is the X coordinate of the graph, usually a time value. <i>stapgraph</i> assumes that this value is constantly increasing. </p>
<p> A different syntax allows the script to specify many details of the graph&#8217;s appearance.</p>
<dl>
<dt><code>%DataSet:</code> DATA-SET-NAME <code> SCALE </code> COLOR <code> GRAPHSTYLE </code></dt>
<dd></dd></dl>
<p> The data set name identifies a data set that will be emitted by the script. &quot;SCALE&quot; is the overall vertical scale of the graph for this data set. &quot;COLOR&quot; is a red-green-blue hex color. &quot;GRAPHSTYLE&quot; is one of bar &#8211; a traditional bar graph dot &#8211; plotted points discreet &#8211; An event style timeline that records that an event happened at a certain time.</p>
<dl>
<dt><code>%Title:</code> TITLE</dt>
<dd> A title for the whole graph.</dd>
<dt><code>%XAxisTitle:</code> TITLE</dt>
<dd> The legend for the X axis</dd>
<dt><code>%YAxisTitle:</code> TITLE</dt>
<dd> The legend for the Y axis.</dd>
<dt><code>%YMax:</code> MAX VALUE</dt>
<dd> The maximum value displayed on the graph. </dd>
</dl>
<h2>GRAPH DATA</h2>
<p> <code> DATA SET </code> TIME <code> VALUE </code> Each data point that is to be plotted is tagged with the data set name, followed by the time and value of the point. </p>
<h2>SEE ALSO</h2>
<p> <i>stap</i>(3stap), <i>staprun</i>(3stap), </p>
<h2>BUGS</h2>
<p> Use the Bugzilla link off of the project web page or our mailing list. <code><a rel="nofollow" href="http://sources.redhat.com/systemtap/">http://sources.redhat.com/systemtap/</a></code>,<code>&lt;systemtap [at] sources.redhat.com&gt;</code>. </p>
<h2>Index</h2>
