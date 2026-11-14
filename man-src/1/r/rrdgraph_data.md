---
title: "rrdgraph_data(1)"
name: "rrdgraph_data"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdgraph_data/"
description: "rrdgraph_data – preparing data for graphing in rrdtool graph"
---

<h2 class="name">NAME</h2>
<p> rrdgraph_data &#8211; preparing data for graphing in rrdtool graph </p>
<h2>SYNOPSIS</h2>
<p> <font SIZE="-1"><code>DEF:</code></font><i>&lt;vname&gt;</i>=<i>&lt;rrdfile&gt;</i>:<i>&lt;ds-name&gt;</i>:<i>&lt;</i><font SIZE="-1"><i>CF</i></font><i>&gt;</i>[:step=<i>&lt;step&gt;</i>][:start=<i>&lt;time&gt;</i>][:end=<i>&lt;time&gt;</i>][:reduce=<i>&lt;</i><font SIZE="-1">CF</font><i>&gt;</i>] </p>
<p> <font SIZE="-1"><code>VDEF</code></font>:<i>vname</i>=<i></i><font SIZE="-1"><i>RPN</i></font><i> expression</i> </p>
<p> <font SIZE="-1"><code>CDEF</code></font>:<i>vname</i>=<i></i><font SIZE="-1"><i>RPN</i></font><i> expression</i></p>
<h2>DESCRIPTION</h2>
<p> These three instructions extract data values out of the <font SIZE="-1"><code>RRD</code></font> files, optionally altering them (think, for example, of a bytes to bits conversion). If so desired, you can also define variables containing useful information such as maximum, minimum etcetera. Two of the instructions use a language called <font SIZE="-1"><code>RPN</code></font> which is described in its own manual page. </p>
<p> Variable names (<i>vname</i>) must be made up strings of the following characters <tt>&quot;A-Z, a-z, 0-9, -,_&quot;</tt> and a maximum length of 255 characters. </p>
<p> When picking variable names, make sure you do not choose a name that is already taken by an <font SIZE="-1">RPN</font> operator. A safe bet it to use lowercase or mixed case names for variables since operators will always be in uppercase.</p>
<h2>DEF</h2>
<p> <font SIZE="-1"><code>DEF:</code></font><i>&lt;vname&gt;</i>=<i>&lt;rrdfile&gt;</i>:<i>&lt;ds-name&gt;</i>:<i>&lt;</i><font SIZE="-1"><i>CF</i></font><i>&gt;</i>[:step=<i>&lt;step&gt;</i>][:start=<i>&lt;time&gt;</i>][:end=<i>&lt;time&gt;</i>][:reduce=<i>&lt;</i><font SIZE="-1">CF</font><i>&gt;</i>] </p>
<p> This command fetches data from an <font SIZE="-1"><code>RRD</code></font> file. The virtual name <i>vname</i> can then be used throughout the rest of the script. By default, an <font SIZE="-1"><code>RRA</code></font> which contains the correct consolidated data at an appropriate resolution will be chosen. The resolution can be overridden with the &#8211;step option. The resolution can again be overridden by specifying the <code>step size</code>. The time span of this data is the same as for the graph by default, you can override this by specifying <code>start and end</code>. Remember to escape colons in the time specification! </p>
<p> If the resolution of the data is higher than the resolution of the graph, the data will be further consolidated. This may result in a graph that spans slightly more time than requested. Ideally each point in the graph should correspond with one <font SIZE="-1"><code>CDP</code></font> from an <font SIZE="-1"><code>RRA</code></font>. For instance, if your <font SIZE="-1"><code>RRD</code></font> has an <font SIZE="-1"><code>RRA</code></font> with a resolution of 1800 seconds per <font SIZE="-1"><code>CDP</code></font>, you should create an image with width 400 and time span 400*1800 seconds (use appropriate start and end times, such as <tt>&quot;--start end-8days8hours&quot;</tt>). </p>
<p> If consolidation needs to be done, the <font SIZE="-1"><code>CF</code></font> of the <font SIZE="-1"><code>RRA</code></font> specified in the <font SIZE="-1"><code>DEF</code></font> itself will be used to reduce the data density. This behavior can be changed using <tt>&quot;:reduce=</tt>&lt;CF&gt;<tt>&quot;</tt>. This optional parameter specifies the <font SIZE="-1"><code>CF</code></font> to use during the data reduction phase. </p>
<p> Example: </p>
<pre>
        DEF:ds0=router.rrd:ds0:AVERAGE
        DEF:ds0weekly=router.rrd:ds0:AVERAGE:step=7200
        DEF:ds0weekly=router.rrd:ds0:AVERAGE:start=end-1h
        DEF:ds0weekly=router.rrd:ds0:AVERAGE:start=11\:00:end=start+1h
</pre>
<h2>VDEF</h2>
<p> <font SIZE="-1"><code>VDEF</code></font>:<i>vname</i>=<i></i><font SIZE="-1"><i>RPN</i></font><i> expression</i> </p>
<p> This command returns a value and/or a time according to the <font SIZE="-1"><code>RPN</code></font> statements used. The resulting <i>vname</i> will, depending on the functions used, have a value and a time component. When you use this <i>vname</i> in another <font SIZE="-1"><code>RPN</code></font> expression, you are effectively inserting its value just as if you had put a number at that place. The variable can also be used in the various graph and print elements. </p>
<p> Example: <tt>&quot;VDEF:avg=mydata,AVERAGE&quot;</tt> </p>
<p> Note that currently only aggregation functions work in <font SIZE="-1">VDEF</font> rpn expressions. Patches to change this are welcome.</p>
<h2>CDEF</h2>
<p> <font SIZE="-1"><code>CDEF</code></font>:<i>vname</i>=<i></i><font SIZE="-1"><i>RPN</i></font><i> expression</i> </p>
<p> This command creates a new set of data points (in memory only, not in the <font SIZE="-1"><code>RRD</code></font> file) out of one or more other data series. The <font SIZE="-1"><code>RPN</code></font> instructions are used to evaluate a mathematical function on each data point. The resulting <i>vname</i> can then be used further on in the script, just as if it were generated by a <font SIZE="-1"><code>DEF</code></font> instruction. </p>
<p> Example: <tt>&quot;CDEF:mydatabits=mydata,8,*&quot;</tt></p>
<h2>About CDEF versus VDEF</h2>
<p> At some point in processing, <code>RRDtool</code> has gathered an array of rates ready to display. </p>
<p> <font SIZE="-1"><code>CDEF</code></font> works on such an array. For example, <i>CDEF:new=ds0,8,*</i> would multiply each of the array members by eight (probably transforming bytes into bits). The result is an array containing the new values. </p>
<p> <font SIZE="-1"><code>VDEF</code></font> also works on such an array but in a different way. For example, <i>VDEF:max=ds0,MAXIMUM</i> would scan each of the array members and store the maximum value.</p>
<h3>When do you use <font SIZE="-1"><code>VDEF</code></font> versus <font SIZE="-1"><code>CDEF</code></font>?</h3>
<p> Use <font SIZE="-1"><code>CDEF</code></font> to transform your data prior to graphing. In the above example, we&#8217;d use a <font SIZE="-1"><code>CDEF</code></font> to transform bytes to bits before graphing the bits. </p>
<p> You use a <font SIZE="-1"><code>VDEF</code></font> if you want <i>max(1,5,3,2,4)</i> to return five which would be displayed in the graph&#8217;s legend (to answer, what was the maximum value during the graph period). </p>
<p> If you want to apply &#8216;complex&#8217; operations to the result of a <font SIZE="-1">VDEF</font> you have to use a <font SIZE="-1">CDEF</font> again since VDEFs only look like <font SIZE="-1">RPN</font> expressions, they aren&#8217;t really.</p>
<h2>SEE ALSO</h2>
<p> rrdgraph gives an overview of how <code>rrdtool graph</code> works. rrdgraph_data describes <font SIZE="-1"><code>DEF</code></font>,<font SIZE="-1"><code>CDEF</code></font> and <font SIZE="-1"><code>VDEF</code></font> in detail. rrdgraph_rpn describes the <font SIZE="-1"><code>RPN</code></font> language used in the <code>?DEF</code> statements. rrdgraph_graph page describes all of the graph and print functions. </p>
<p> Make sure to read rrdgraph_examples for tips&amp;tricks.</p>
<h2>AUTHOR</h2>
<p> Program by Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
<p> This manual page by Alex van den Bogaerdt &lt;alex [at] vandenbogaerdt.nl&gt; with corrections and/or additions by several people </p>
<h2>Index</h2>
<dt><a href="#lbAJ">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAK">AUTHOR</a></p>
<dd></dl>
