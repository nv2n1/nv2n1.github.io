---
title: "rasplit(1)"
name: "rasplit"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rasplit/"
description: "rasplit – split argus(8) data."
---

<h2>NAME</h2>
<p> <code>rasplit</code> &#8211; split <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data.</p>
<h2>SYNOPSIS</h2>
<p> <code>rasplit</code> [[<code>-M</code> <i>splitmode</i>] [<i>splitmode options</i>]] [<code>raoptions</code>] [<code>&#8212;</code> <i>filter-expression</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Rasplit</code> reads <code>argus</code> data from an <i>argus-data</i> source, and splits the resulting output into consecutive sections of records based on size, count time, or flow event, writing the output into a set of output-files. By default, <code>rasplit</code> puts 10,000 records of input into each <code>argus</code> output file, or standard out. </p>
<p> The output files&#8217; name consists of a prefix, which is specified using the <i>-w</i> <i>ra option</i>, and a suffix, which is created for each resulting file. If no prefix is provided, then <code>rasplit</code> will use &#8216;x&#8217; as the default prefix. The suffix that is used is determined by the mode of operation. When <code>rasplit</code> is using the default count mode or the size mode, the suffix is a group of letters &#8216;aa&#8217;, &#8216;ab&#8217;, and so on, such that concatenating the output files in sorted order by file name produces the original input file. If <code>rasplit</code> will need to create more output files than are allowed by the default suffix strategy, more letters will be added, in order to accomodate the needed files. When the mode is <code>time</code> mode, the default output filename suffix is &#8216;%Y.%m.%d.%h.%m.%s&#8217;, which is used by strftime() to create an output filename that is time oriented. This default is overrided by adding a &#8216;%&#8217; extension to the name provided on the commandline using the <i>-w</i> option. </p>
<p> When standard out is specified, using <i>-w &#8211;</i>, <code>rasplit</code> will output a single <code>argus-stream</code> with START and STOP argus management records inserted appropriately to indicate where the output is split. See <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> for more information on output stream formats. </p>
<p> When <code>rasplit</code> is spliting on output record count (the default), the number of records is specified as an ordinal counter, the default is 10,000 records. When <code>rasplit</code> is spliting based on the maximum output file size, the size is specified as bytes. The scale of the bytes can be specified by appending &#8216;b&#8217;, &#8216;k&#8217; and &#8216;m&#8217; to the number provided. </p>
<p> When <code>rasplit</code> is spliting based on time, the time period is specified with the option, and can be any period based in seconds (s), minutes (m), hours (h), days (d), weeks (w), months (M) or years (y). <code>Rasplit</code> will create and modify records as required to split on prescribed time boundaries. If any record spans a time boundary, the record is split and the metrics are adjusted using a uniform distribution model to distribute the statistics between the two records. Care is taken to avoid records with zero packet and byte counts, that could result from roundoff error. </p>
<p> When <code>rasplit</code> is spliting based on flow event, the flow that acts as the event marker is specified using a standard <code>ra</code> filter expression, that is bounded by quotes (&quot;). Records that preceed the first flow event in the data stream are written to the specified output file, and then new files are generated with the flow event record being the first record of the new file. This method will allow you to use wire events as triggers for spliting data. </p>
<h2>RASPLIT SPECIFIC OPTIONS</h2>
<p> Rasplit, like all ra based clients, supports a number of <code>ra options</code> including remote data access, reading from multiple files and filtering of input argus records through a terminating filter expression. <code><a href="/docs/linux/man/1-rasplit/">rasplit</a>(1)</code> specific options are:</p>
<dl>
<dt><code>-a</code><i> suffix length</i></p>
<dd> default is 2 characters.</p>
<dt><code>-d</code></p>
<dd> Toggle running as a deamon.</p>
<dt><code>-M</code><i> splitmode</i></p>
<dd> Supported spliting modes are: </p>
<pre>
<code>    count &lt;num&gt;</code>
<code>     size &lt;size&gt;</code>
<code>     time &lt;period&gt;</code>
<code>     flow &quot;filter-expression&quot;</code>
</pre>
<dt><code>-w</code><i> filename</i></p>
<dd> <code>Rasplit</code> supports an extended <i>-w</i> option that allows for output record contents to be inserted into the output filename. Specified using &#8216;$&#8217; (dollar) notation, any printable field can be used. Care should be taken to honor any shell escape requirements when specifying on the command line. See <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> for the list of printable fields. </p>
<p> Another extended feature, when using <code>time</code> mode, <code>rasplit</code> will process the supplied filename using <code><a href="/docs/linux/man/3-strftime/">strftime</a>(3)</code>, so that time fields can be inserted into the resulting output filename. </p>
</dl>
<h2>INVOCATION</h2>
<p> This invocation reads <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from <code>inputfile</code> and splits the <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data stream based on output file size of no greater than 1 Megabyte. The resulting output files have a prefix of <i>argus.</i> and suffix that starts with &#8216;aa&#8217;. The single trailing &#8216;.&#8217; is significant. </p>
<pre>
 
   <code>rasplit</code> -r inputfile -M size 1m -w argus.
 
</pre>
<p> This invocation splits <code>inputfile</code> based on hard 10 minute time boundaries. The resulting output files are created with a prefix of <i>/archive/%Y/%m/%d/argus.</i> and the suffix is <i>%H.%M.%S</i>. The values will be supplied based on the time in the record being written out. </p>
<pre>
  
   <code>rasplit</code> -r * -M time 10m -w &quot;/archive/%Y/%m/%d/argus.%H.%M.%S&quot;
 
</pre>
<p> This invocation splits <code>inputfile</code> based on the argus source identifier. The resulting output files are created with a prefix of <i>/archive/Source Identifier/argus.</i> and the default suffix starting with &quot;aa&quot;. The source identifier will be supplied based on the contents of the record being exported. </p>
<pre>
  
   <code>rasplit</code> -r * -M time 10m -w &quot;/archive/$srcid/argus.&quot;
 
</pre>
<p> This invocation splits <code>inputfile</code> based on a flow event marker. The resulting output files are created with a prefix of &#8216;outfile.&#8217; and the default suffix starting with &quot;aa&quot;. Whenever a ping to a specific host is seen in the stream, a new output file is generated. </p>
<pre>
  
   <code>rasplit</code> -r * -M flow &quot;echo and host 1.2.3.4&quot; -w outfile.
 
</pre>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2016 QoSient. All rights reserved. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ra/">ra</a>(1),</code> <code><a href="/docs/linux/man/5-rarc/">rarc</a>(5),</code> <code><a href="/docs/linux/man/8-argus/">argus</a>(8),</code> </p>
<h2>AUTHORS</h2>
<pre>
Carter Bullard (carter [at] qosient.com).
</pre>
<h2>Index</h2>
