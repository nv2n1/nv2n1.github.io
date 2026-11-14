---
title: "rrdgraph_examples(1)"
name: "rrdgraph_examples"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdgraph_examples/"
description: "rrdgraph_examples – Examples for rrdtool graph"
---

<h2 class="name">NAME</h2>
<p> rrdgraph_examples &#8211; Examples for rrdtool graph </p>
<h2>SYNOPSIS</h2>
<p> <code>rrdtool graph /home/httpd/html/test.png &#8211;img-format </code><font SIZE="-1"><code>PNG</code></font> </p>
<p> followed by any of the examples below</p>
<h2>DESCRIPTION</h2>
<p> For your convenience some of the commands are explained here by using detailed examples. They are not always cut-and-paste ready because comments are intermixed with the examples.</p>
<h2>EXAMPLES</h2>
<h3>Data with multiple resolutions</h3>
<pre>
    --end now --start end-120000s --width 400
    DEF:ds0a=/home/rrdtool/data/router1.rrd:ds0:AVERAGE
    DEF:ds0b=/home/rrdtool/data/router1.rrd:ds0:AVERAGE:step=1800
    DEF:ds0c=/home/rrdtool/data/router1.rrd:ds0:AVERAGE:step=7200
    LINE1:ds0a#0000FF:&quot;default resolution\l&quot;
    LINE1:ds0b#00CCFF:&quot;resolution 1800 seconds per interval\l&quot;
    LINE1:ds0c#FF00FF:&quot;resolution 7200 seconds per interval\l&quot;
</pre>
<h3>Nicely formatted legend section</h3>
<pre>
    DEF:ds0=/home/rrdtool/data/router1.rrd:ds0:AVERAGE
    DEF:ds1=/home/rrdtool/data/router1.rrd:ds1:AVERAGE
    VDEF:ds0max=ds0,MAXIMUM
    VDEF:ds0avg=ds0,AVERAGE
    VDEF:ds0min=ds0,MINIMUM
    VDEF:ds0pct=ds0,95,PERCENT
    VDEF:ds1max=ds1,MAXIMUM
    VDEF:ds1avg=ds1,AVERAGE
    VDEF:ds1min=ds1,MINIMUM
    VDEF:ds1pct=ds1,95,PERCENT
</pre>
<p> Note: consolidation occurs here. </p>
<pre>
    CDEF:ds0bits=ds0,8,*
    CDEF:ds1bits=ds1,8,*
</pre>
<p> Note: 10 spaces to move text to the right </p>
<pre>
    COMMENT:&quot;          &quot;
</pre>
<p> Note: the column titles have to be as wide as the columns </p>
<pre>
    COMMENT:&quot;Maximum    &quot;
    COMMENT:&quot;Average    &quot;
    COMMENT:&quot;Minimum    &quot;
    COMMENT:&quot;95th percentile\l&quot;
    AREA:ds0bits#00C000:&quot;Inbound &quot;
    GPRINT:ds0max:&quot;%6.2lf %Sbps&quot;
    GPRINT:ds0avg:&quot;%6.2lf %Sbps&quot;
    GPRINT:ds0min:&quot;%6.2lf %Sbps&quot;
    GPRINT:ds0pct:&quot;%6.2lf %Sbps\l&quot;
    LINE1:ds1bits#0000FF:&quot;Outbound&quot;
    GPRINT:ds1max:&quot;%6.2lf %Sbps&quot;
    GPRINT:ds1avg:&quot;%6.2lf %Sbps&quot;
    GPRINT:ds1min:&quot;%6.2lf %Sbps&quot;
    GPRINT:ds1pct:&quot;%6.2lf %Sbps\l&quot;
</pre>
<h3>Offsetting a line on the y-axis</h3>
<p> Depending on your needs you can do this in two ways:</p>
<dl>
<dt>&bull;</p>
<dd> Offset the data, then graph this </p>
<pre>
    DEF:mydata=my.rrd:ds:AVERAGE
</pre>
<p> Note: this will also influence any other command that uses &#8220;data&#8221; </p>
<pre>
    CDEF:data=mydata,100,+
    LINE1:data#FF0000:&quot;Data with offset&quot;
</pre>
<dt>&bull;</p>
<dd> Graph the original data, with an offset </p>
<pre>
    DEF:mydata=my.rrd:ds:AVERAGE
</pre>
<p> Note: no color in the first line so it is not visible </p>
<pre>
    LINE1:100
</pre>
<p> Note: the second line gets stacked on top of the first one </p>
<pre>
    LINE1:data#FF0000:&quot;Data with offset&quot;:STACK
</pre>
</dl>
<h3>Drawing dashed lines</h3>
<p> Also works for <font SIZE="-1">HRULE</font> and <font SIZE="-1">VRULE</font></p>
<dl>
<dt>&bull;</p>
<dd> default style: &#8211; &#8211; &#8211; &#8211; &#8211;<br />
&nbsp;<wbr>LINE1:data#FF0000:&#8220;dashed line&#8221;:dashes</p>
<dt>&bull;</p>
<dd> more fancy style with offset: &#8211; &#8211; &#8212; &#8211; &#8212; &#8211;<br />
&nbsp;<wbr>LINE1:data#FF0000:&#8220;another dashed line&#8221;:dashes=15,5,5,10:dash-offset=10</dl>
<h3>Time ranges</h3>
<pre><code>
Last four weeks : --start end - 4w --end 00 : 00 January 2001 : --start 20010101 --end start + 31d January 2001 : --start 20010101 --end 20010201 Last hour : --start end - 1h Last 24 hours : &lt;nothing at all&gt; Yesterday : --end 00 : 00
</code></pre>
<h3>Viewing the current and previous week together</h3>
<pre>
    --end now --start end-1w
    DEF:thisweek=router.rrd:ds0:AVERAGE
    DEF:lastweek=router.rrd:ds0:AVERAGE:end=now-1w:start=end-1w
</pre>
<p> Shift the data forward by one week (604800 seconds) </p>
<pre>
    SHIFT:lastweek:604800
    [ more of the usual VDEF and CDEF stuff if you like ]
    AREA:lastweek#0000FF:Last\ week
    LINE1:thisweek#FF0000:This\ week
</pre>
<h3>Aberrant Behaviour Detection</h3>
<p> If the specialized function <code>RRAs</code> exist for aberrant behavior detection, they can be used to generate the graph of a time series with confidence bands and failures. </p>
<pre>
   rrdtool graph example.png \
          DEF:obs=monitor.rrd:ifOutOctets:AVERAGE \
          DEF:pred=monitor.rrd:ifOutOctets:HWPREDICT \
          DEF:dev=monitor.rrd:ifOutOctets:DEVPREDICT \
          DEF:fail=monitor.rrd:ifOutOctets:FAILURES \
          TICK:fail#ffffa0:1.0:&quot;Failures\: Average bits out&quot; \
          CDEF:scaledobs=obs,8,* \
          CDEF:upper=pred,dev,2,*,+ \
          CDEF:lower=pred,dev,2,*,- \
          CDEF:scaledupper=upper,8,* \
          CDEF:scaledlower=lower,8,* \
          LINE2:scaledobs#0000ff:&quot;Average bits out&quot; \
          LINE1:scaledupper#ff0000:&quot;Upper Confidence Bound: Average bits out&quot; \
          LINE1:scaledlower#ff0000:&quot;Lower Confidence Bound: Average bits out&quot;
</pre>
<p> This example generates a graph of the data series in blue (<font SIZE="-1">LINE2</font> with the scaledobs virtual data source), confidence bounds in red (scaledupper and scaledlower virtual data sources), and potential failures (i.e. potential aberrant aberrant behavior) marked by vertical yellow lines (the fail data source). </p>
<p> The raw data comes from an <font SIZE="-1">AVERAGE</font> <font SIZE="-1"><code>RRA</code></font>, the finest resolution of the observed time series (one consolidated data point per primary data point). The predicted (or smoothed) values are stored in the <font SIZE="-1">HWPREDICT</font> <font SIZE="-1"><code>RRA</code></font>. The predicted deviations (think standard deviation) values are stored in the <font SIZE="-1">DEVPREDICT</font> <font SIZE="-1"><code>RRA</code></font>. Finally, the <font SIZE="-1">FAILURES</font> <font SIZE="-1"><code>RRA</code></font> contains indicators, with 1 denoting a potential failure. </p>
<p> All of the data is rescaled to bits (instead of Octets) by multiplying by 8. The confidence bounds are computed by an offset of 2 deviations both above and below the predicted values (the CDEFs upper and lower). Vertical lines indicated potential failures are graphed via the <font SIZE="-1">TICK</font> graph element, which converts non-zero values in an <font SIZE="-1"><code>RRA</code></font> into tick marks. Here an axis-fraction argument of 1.0 means the tick marks span the entire y-axis, and hence become vertical lines on the graph. </p>
<p> The choice of 2 deviations (a scaling factor) matches the default used internally by the <font SIZE="-1">FAILURES</font> <font SIZE="-1"><code>RRA</code></font>. If the internal value is changed (see rrdtune), this graphing command should be changed to be consistent. </p>
<p> <i>A note on data reduction:</i> </p>
<p> The <code>rrdtool</code> <i>graph</i> command is designed to plot data at a specified temporal resolution, regardless of the actually resolution of the data in the <font SIZE="-1">RRD</font> file. This can present a problem for the specialized consolidation functions which maintain a one-to-one mapping between primary data points and consolidated data points. If a graph insists on viewing the contents of these <code>RRAs</code> on a coarser temporal scale, the <i>graph</i> command tries to do something intelligent, but the confidence bands and failures no longer have the same meaning and may be misleading.</p>
<h2>SEE ALSO</h2>
<p> rrdgraph gives an overview of how <code>rrdtool graph</code> works. rrdgraph_data describes <font SIZE="-1"><code>DEF</code></font>,<font SIZE="-1"><code>CDEF</code></font> and <font SIZE="-1"><code>VDEF</code></font> in detail. rrdgraph_rpn describes the <font SIZE="-1"><code>RPN</code></font> language used in the <code>xDEF</code> statements. rrdgraph_graph page describes all the graph and print functions.</p>
<h2>AUTHOR</h2>
<p> Program by Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
<p> This manual page by Alex van den Bogaerdt &lt;alex [at] vandenbogaerdt.nl&gt; with corrections and/or additions by several people </p>
<h2>Index</h2>
