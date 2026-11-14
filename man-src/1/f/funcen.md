---
title: "funcen(1)"
name: "funcen"
section: "1"
letter: "f"
url: "/docs/linux/man/1-funcen/"
description: "funcen – find centroid (for binary tables)"
---

<h2>NAME</h2>
<p> <code>funcen &#8211; find centroid (for binary tables)</code></p>
<h2>SYNOPSIS</h2>
<p> funcen [-i] [-n iter] [-t tol] [-v lev] &lt;iname&gt; &lt;region&gt;</p>
<h2>OPTIONS</h2>
<pre>
  -i            # use image filtering (default: event filtering)
  -n iter       # max number of iterations (default: 0)
  -t tol        # pixel tolerance distance (default: 1.0)
  -v [0,1,2,3]  # output verbosity level (default: 0)
</pre>
<h2>DESCRIPTION</h2>
<p> <code>funcen</code> iteratively calculates the centroid position within one or more regions of a Funtools table (<font SIZE="-1">FITS</font> binary table or raw event file). Starting with an input table, an initial region specification, and an iteration count, the program calculates the average x and y position within the region and then uses this new position as the region center for the next iteration. Iteration terminates when the maximum number of iterations is reached or when the input tolerance distance is met for that region. A count of events in the final region is then output, along with the pixel position value (and, where available, <font SIZE="-1">WCS</font> position). </p>
<p> The first argument to the program specifies the Funtools table file to process. Since the file must be read repeatedly, a value of &#8220;stdin&#8221; is not permitted when the number of iterations is non-zero. Use Funtools Bracket Notation to specify <font SIZE="-1">FITS</font> extensions and filters. </p>
<p> The second required argument is the initial region descriptor. Multiple regions are permitted. However, compound regions (accelerators, variable argument regions and regions connected via boolean algebra) are not permitted. Points and polygons also are illegal. These restrictions might be lifted in a future version, if warranted. </p>
<p> The <code>-n</code> (iteration number) switch specifies the maximum number of iterations to perform. The default is 0, which means that the program will simply count and display the number of events in the initial region(s). Note that when iterations is 0, the data can be input via stdin. </p>
<p> The <code>-t</code> (tolerance) switch specifies a floating point tolerance value. If the distance between the current centroid position value and the last position values is less than this value, iteration terminates. The default value is 1 pixel. </p>
<p> The <code>-v</code> (verbosity) switch specifies the verbosity level of the output. The default is 0, which results in a single line of output for each input region consisting of the following values: </p>
<pre>
  counts x y [ra dec coordsys]
</pre>
<p> The last 3 <font SIZE="-1">WCS</font> values are output if <font SIZE="-1">WCS</font> information is available in the data file header. Thus, for example: </p>
<pre>
  [sh] funcen -n 0 snr.ev &quot;cir 505 508 5&quot;
  915 505.00 508.00 345.284038 58.870920 j2000
</pre>
<pre>
  [sh] funcen -n 3 snr.ev &quot;cir 505 508 5&quot;
  1120 504.43 509.65 345.286480 58.874587 j2000
</pre>
<p> The first example simply counts the number of events in the initial region. The second example iterates the centroid calculation three times to determine a final &#8220;best&#8221; position. </p>
<p> Higher levels of verbosity obviously imply more verbose output. At level 1, the output essentially contains the same information as level 0, but with keyword formatting: </p>
<pre>
  [sh] funcen -v 1 -n 3 snr.ev &quot;cir 505 508 5&quot;
  event_file:     snr.ev
  initial_region: cir 505 508 5
  tolerance:      1.0000
  iterations:     1
</pre>
<pre>
  events:         1120
  x,y(physical):  504.43 509.65
  ra,dec(j2000):  345.286480 58.874587
  final_region1:  cir 504.43 509.65 5
</pre>
<p> Level 2 outputs results from intermediate calculations as well. </p>
<p> Ordinarily, region filtering is performed using analytic (event) filtering, i.e. that same style of filtering as is performed by <code>fundisp</code> and <code>funtable</code>. Use the <code>-i</code> switch to specify image filtering, i.e. the same style filtering as is performed by <code>funcnts</code>. Thus, you can perform a quick calculation of counts in regions, using either the analytic or image filtering method, by specifying the<br />
&nbsp;<wbr><code>-n 0</code>&nbsp;<wbr>and optional&nbsp;<wbr><code>-i</code>&nbsp;<wbr>switches. These two method often give different results because of how boundary events are processed: </p>
<pre>
  [sh] funcen  snr.ev &quot;cir 505 508 5&quot;
  915 505.00 508.00 345.284038 58.870920 j2000
</pre>
<pre>
  [sh] funcen -i snr.ev &quot;cir 505 508 5&quot;
  798 505.00 508.00 345.284038 58.870920 j2000
</pre>
<p> See Region Boundaries for more information about how boundaries are calculated using these two methods.</p>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
