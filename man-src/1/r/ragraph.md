---
title: "ragraph(1)"
name: "ragraph"
section: "1"
letter: "r"
url: "/docs/linux/man/1-ragraph/"
description: "ragraph – graph argus(8) data."
---

<h2>NAME</h2>
<p> <code>ragraph</code> &#8211; graph <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data.</p>
<h2>SYNOPSIS</h2>
<p> <code>ragraph metric [object]</code> [<code>-M</code> <i>mode</i>] [<code>options</code>] [<code>raoptions</code>] [<code>&#8212;</code> <i>filter-expression</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Ragraph</code> reads <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from an <i>argus-file</i>, and graphs fields of interest from matching argus flow activity records. You must specify the metric(s), the flow object/identifier(s) and the time granularity required for the graph. Standard raoptions are available to filter input and specify the time range of interest, and graphing options are provided to specify x and y axis labels, titles, upper and lower range limits, and plot sizes. Support for logorithmic scaling, object stacking, and split graphing are provided to provide some flexibility in the graphs you can produce. </p>
<p> <code>Ragraph</code> supports graphing most metrics that are available in argus data, including, bytes, packet counts, average duration, loss, jitter, load, and rate. These metrics can be graphed in association with flow identifiers, such as source or destination address, network address, source identifier, protocol, port numbers, services, vlan id, mpls tag, ttl, and tos values. Currently, there are limits to the number of metrics and objects that can be graphed at one time, so assume that <code>ragraph</code> is a simple graphing tool. </p>
<p> By default <code>ragraph</code> writes its output to ragraph.png, in the current directory. Use the &#8216;-w&#8217; raoption to specify an alternate output filename. </p>
<p> <code>Ragraph</code> is implemented as a perl script front-end to the routine <code>rabins</code> and rrd-tool, which is used to generate PNG formatted graphs. As a result <code>ragraph</code> supports all the raoption and most of the options to the rrd-tool graphing functions. </p>
<h2>RA OPTIONS</h2>
<p> Ragraph, like all ra based clients, supports a number of <code>ra options</code> including filtering of input argus records through a terminating filter expression, and specifying an output filename using the -w option.<br />
&nbsp;<wbr> See <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> for a complete description of <code>ra options</code>. </p>
<h2>RRDTOOL GRAPH OPTIONS</h2>
<p> Ragraph, when using rrdtool as the graphing backend, will pass rrdgraph specific options to the appropriate rrdtool module. These are the specific rrdtool options that are supported.</p>
<h2>Appearance</h2>
<dl>
<dt><code>-fill</code></p>
<dd> Turn off area fill.</p>
<dt><code>-stack</code></p>
<dd> Turn off data stacking.</p>
<dt><code>-split</code></p>
<dd> Turn off axis splitting for src/dst(in/out) traffic.</p>
<dt><code>-invert</code></p>
<dd> Invert a split graph, so that src and dest data are flipped.</p>
<dt><code>-rigid</code></p>
<dd> Pass rrdtool rigid parameter to rrdgraph.</dl>
<h2>Labels</h2>
<dl>
<dt><code>-title string</code></p>
<dd> Specify a graph title.</p>
<dt><code>-vertical-label string</code></p>
<dd> Specify a vertically placed yaxis label.</dl>
<h2>Size</h2>
<dl>
<dt><code>-height pixels</code></p>
<dd> Specify height in pixels for the graph (275 pixels)</p>
<dt><code>-width pixels</code></p>
<dd> Specify width in pixels for the graph (800 pixels)</p>
<dt><code>-only-graph</code></p>
<dd> Generate only the graph with out any borders, title, labels, legend.</dl>
<h2>Limits</h2>
<dl>
<dt><code>-upper value</code></p>
<dd> Specify upper bounds for graphing data (automatic).</p>
<dt><code>-lower value</code></p>
<dd> Specify lower bounds for graphing data (automatic). When data is split, you need to specify the value as a negative number.</p>
<dt><code>-alt-autoscale</code></p>
<dd>
<dt><code>-alt-autoscale-max</code></p>
<dd> Use rrdtool alternate y-axis autoscale algorithm. See rrdgraph manpage for information.</p>
<dt><code>-no-gridfit</code></p>
<dd> Disable rrdtool grid scale modification strategies. See rrdgraph manpage for information.</dl>
<h2>Grid</h2>
<dl>
<dt><code>-x-grid GTM:GST:MTM:MST:LTM:LST:LPR:LFM | none</code></p>
<dd> Modify rrdtool x-axis label definition. See rrdgraph manpage for information.</p>
<dt><code>-y-grid &#8216;grid step:label factor&#8217; | none</code></p>
<dd> Modify rrdtool y-axis label definition. The use of &#8216; is important to parsing the option correctly. See rrdgraph manpage for information.</p>
<dt><code>-alt-y-grid</code></p>
<dd> Modify rrdtool default y-grid behavior. See rrdgraph manpage for information.</p>
<dt><code>-log</code></p>
<dd> Use logarithmic scale for y-axis.</p>
<dt><code>-units-exponent value</code></p>
<dd> Set the 10** exponent scaling of the y-axis. See rrdgraph manpage for information.</p>
<dt><code>-units-length value</code></p>
<dd> Set the width of the y-axis border. See rrdgraph manpage for information.</p>
<dt><code>-units=si</code></p>
<dd> Turn off expoenential notation for logarithmic graphs. See rrdgraph manpage for information.</dl>
<h2>Miscellaneous</h2>
<dl>
<dt><code>-imginfo printfstr</code></p>
<dd> Adds img information to the graph. See rrdgraph manpage for information.</p>
<dt><code>-zoom factor</code></p>
<dd> Zoom the graphics by the given factor. See rrdgraph manpage for information.</p>
<dt><code>-font FONTTAG:size:[font]</code></p>
<dd> Modify rrdgraph default font. See rrdgraph manpage for information.</p>
<dt><code>-font-render-mode {normal,light,mono}</code></p>
<dd> Modify rrdgraph font smoothing strength. See rrdgraph manpage for information.</p>
<dt><code>-font-smoothing-threshold size</code></p>
<dd> Modify rrdgraph font smoothing font size. See rrdgraph manpage for information.</p>
<dt><code>-slope-mode</code></p>
<dd> Modify rrdgraph slope-mode option. See rrdgraph manpage for information.</p>
<dt><code>-no-legend</code></p>
<dd> Supress generation of the legend.</p>
<dt><code>-watermark string</code></p>
<dd> Adds the given string as a watermark. See rrdgraph manpage for information.</p>
<dt><code>-norrdwmark</code></p>
<dd> Disables the default rrdtool watermark from appearing on the graph. </p>
</dl>
<h2>EXAMPLES</h2>
<p> To graph the total load for the data in an <i>argus-file</i> argus.data at 10 second intervals:</p>
<dl>
<dt>
<dd>
<pre>
<code>ragraph bytes -M 10s -r argus.data -title &quot;Total Load&quot;
</code></pre>
</dl>
<p> To graph the rate (pkt/sec) on a destination port basis for the data from a specific probe in an <i>argus-file</i> argus.data at 1 minute intervals:</p>
<dl>
<dt>
<dd>
<pre>
<code>ragraph bytes dport -M 1m -r argus.data - srcid 192.168.0.10
</code></pre>
</dl>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2016 QoSient. All rights reserved.</p>
<h2>AUTHORS</h2>
<pre>
Carter Bullard (carter [at] qosient.com).
</pre>
<h2>SEE ALSO</h2>
<p> <code>rrdtool</code><a rel="nofollow" href="http://oss.oetiker.sh/rrdtool">http://oss.oetiker.sh/rrdtool</a> <code><a href="/docs/linux/man/5-ragraph/">ragraph</a></code>(5), <code><a href="/docs/linux/man/1-ra/">ra</a></code>(1), <code><a href="/docs/linux/man/5-rarc/">rarc</a></code>(5), <code><a href="/docs/linux/man/8-argus/">argus</a></code>(8) </p>
<h2>Index</h2>
