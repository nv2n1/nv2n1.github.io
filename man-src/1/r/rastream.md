---
title: "rastream(1)"
name: "rastream"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rastream/"
description: "rastream – stream block processor for argus(8) data."
---

<h2>NAME</h2>
<p> <code>rastream</code> &#8211; stream block processor for <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data.</p>
<h2>SYNOPSIS</h2>
<p> <code>rastream</code> [[<code>-M</code> <i>splitmode</i>] [<i>splitmode options</i>]] [<code>-f</code> <i>file processing program</i> -B secs] [<code>raoptions</code>] [<code>&#8212;</code> <i>filter-expression</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Rastream</code> reads <code>argus</code> data from an <i>argus-data</i> source, and splits the resulting output into consecutive sections of records based on size, count time, or flow event, writing the output into a set of output-files. </p>
<p> <code>Rastream</code> provides the option to run a program against the output files, <code>seconds</code> after the file is understood to be finished. The program must be specified in a manner so that <code>rastream</code> can find it, either within the system $PATH, or provided as a full pathname. </p>
<p> By default, <code>rastream</code> splits the stream by output file record count, putting 10,000 records of input into each <code>argus</code> output file, or standard out, as needed. The behavior is similar to the unix split.1 command. </p>
<p> The output files&#8217; name consists of a prefix, which is specified using the <i>-w</i> <i>ra option</i>, and a suffix, which is created for each resulting file. If no prefix is provided, then <code>rastream</code> will use &#8216;x&#8217; as the default prefix. The suffix that is used is determined by the mode of operation. When <code>rastream</code> is using the default count mode or the size mode, the suffix is a group of letters &#8216;aa&#8217;, &#8216;ab&#8217;, and so on, such that concatenating the output files in sorted order by file name produces the original input file. If <code>rastream</code> will need to create more output files than are allowed by the default suffix strategy, more letters will be added, in order to accomodate the needed files. When the mode is <code>time</code> mode, the default output filename suffix is &#8216;%Y.%m.%d.%h.%m.%s&#8217;, which is used by strftime() to create an output filename that is time oriented. This default is overrided by adding a &#8216;%&#8217; extension to the name provided on the commandline using the <i>-w</i> option. </p>
<p> When standard out is specified, using <i>-w &#8211;</i>, <code>rastream</code> will output a single <code>argus-stream</code> with START and STOP argus management records inserted appropriately to indicate where the output is split. See <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> for more information on output stream formats. </p>
<p> When <code>rastream</code> is spliting on output record count (the default), the number of records is specified as an ordinal counter, the default is 10,000 records. When <code>rastream</code> is spliting based on the maximum output file size, the size is specified as bytes. The scale of the bytes can be specified by appending &#8216;b&#8217;, &#8216;k&#8217; and &#8216;m&#8217; to the number provided. </p>
<p> When <code>rastream</code> is spliting based on time, the time period is specified with the option, and can be any period based in seconds (s), minutes (m), hours (h), days (d), weeks (w), months (M) or years (y). <code>Rastream</code> will create and modify records as required to split on prescribed time boundaries. If any record spans a time boundary, the record is split and the metrics are adjusted using a uniform distribution model to distribute the statistics between the two records. Care is taken to avoid records with zero packet and byte counts, that could result from roundoff error. </p>
<p> When <code>rastream</code> is spliting based on flow event, the flow that acts as the event marker is specified using a standard <code>ra</code> filter expression, that is bounded by quotes (&quot;). Records that preceed the first flow event in the data stream are written to the specified output file, and then new files are generated with the flow event record being the first record of the new file. This method will allow you to use wire events as triggers for spliting data. </p>
<h2>RASTREAM SPECIFIC OPTIONS</h2>
<p> Rastream, like all ra based clients, supports a number of <code>ra options</code> including remote data access, reading from multiple files and filtering of input argus records through a terminating filter expression. <code><a href="/docs/linux/man/1-rastream/">rastream</a>(1)</code> specific options are:</p>
<dl>
<dt><code>-a</code><i> suffix length</i></p>
<dd> Starting append suffix length. The default is 2 characters.</p>
<dt><code>-B</code><i> duration</i></p>
<dd> Buffer hold time before processing. This value is usually in the 5-15 second range and provides time for rastream to sort records and schedule outputfile processing. The number is derived from the larges FAR status interval of all the argus data sources encountered. </p>
<dt><code>-f</code><i> program</i></p>
<dd> Post processing program. <code>rastream</code>, will execute this program just after closing the output file, passing the full path to the closed output file as a parameter, using this convention: </p>
<pre>
   program -r /full/path/to/closed/file
</pre>
<p> This allows you to post-process the output file in an automated fashion. </p>
<p> Generally, this program can do anything you like, such as aggregating and correcting flow records, labeling records for semantic enhancement, indexing the files, using programs like rasqltimeindex(), and compressing the files. Traditionally, the program has been a shell-script, perl program, or php script, so that it can be easily modified, on the fly, but it can be any executable that can handle the &quot;-r filename&quot; parameter convention. The program should provides its own accountability and error logging, so that you know that things are working as you expect. </p>
<p> <code>rastream</code> must have a path to the program, the program must be executable, and <code>rastream</code> must have permission to run the program for this strategy to be successful. </p>
<p> An example rastream.sh is provided in the ./support/Config directory. </p>
<dt><code>-M</code><i> splitmode</i></p>
<dd> Supported spliting modes are: </p>
<pre>
   <code>    count &lt;num&gt;</code>
   <code>     size &lt;size&gt;</code>
   <code>     time &lt;period&gt;</code>
   <code>     flow &quot;filter-expression&quot;</code>
</pre>
<dt><code>-w</code><i> filename</i></p>
<dd> <code>Rastream</code> supports an extended <i>-w</i> option that allows for output record contents to be inserted into the output filename. Specified using &#8216;$&#8217; (dollar) notation, any printable field can be used. Care should be taken to honor any shell escape requirements when specifying on the command line. See <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> for the list of printable fields. </p>
<p> Another extended feature, when using <code>time</code> mode, <code>rastream</code> will process the supplied filename using <code><a href="/docs/linux/man/3-strftime/">strftime</a>(3)</code>, so that time fields can be inserted into the resulting output filename. </p>
</dl>
<h2>INVOCATION</h2>
<p> This invocation reads <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from <code>inputfile</code> and splits the <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data stream based on output file size of no greater than 1 Megabyte. The resulting output files have a prefix of <i>argus.</i> and suffix that starts with &#8216;aa&#8217;. The single trailing &#8216;.&#8217; is significant. </p>
<pre>
 
   <code>rastream</code> -r inputfile -M size 1m -w argus.
 
</pre>
<p> This invocation splits <code>inputfile</code> based on hard 10 minute time boundaries. The resulting output files are created with a prefix of <i>/archive/%Y/%m/%d/argus.</i> and the suffix is <i>%H.%M.%S</i>. The values will be supplied based on the time in the record being written out. </p>
<pre>
  
   <code>rastream</code> -r * -M time 10m -w &quot;/archive/%Y/%m/%d/argus.%H.%M.%S&quot;
 
</pre>
<p> This invocation splits <code>inputfile</code> based on the argus source identifier. The resulting output files are created with a prefix of <i>/archive/Source Identifier/argus.</i> and the default suffix starting with &quot;aa&quot;. The source identifier will be supplied based on the contents of the record being exported. </p>
<pre>
  
   <code>rastream</code> -r * -M time 10m -w &quot;/archive/$srcid/argus.&quot;
 
</pre>
<p> This invocation splits <code>inputfile</code> based on a flow event marker. The resulting output files are created with a prefix of &#8216;outfile.&#8217; and the default suffix starting with &quot;aa&quot;. Whenever a ping to a specific host is seen in the stream, a new output file is generated. </p>
<pre>
  
   <code>rastream</code> -r * -M flow &quot;echo and host 1.2.3.4&quot; -w outfile.
 
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
