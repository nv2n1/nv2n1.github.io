---
title: "tcpdump_to_db(1)"
name: "tcpdump_to_db"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcpdump_to_db/"
description: "tcpdump_to_db – convert tcpdump textual output to fsdb"
---

<h2 class="name">NAME</h2>
<p> tcpdump_to_db &#8211; convert tcpdump textual output to fsdb </p>
<h2>SYNOPSIS</h2>
<pre>
    tcpdump_to_db [-T] &lt; source.tcpdump &gt; target.fsdb
</pre>
<h2>DESCRIPTION</h2>
<p> Converts a tcpdump data stream to Fsdb format. </p>
<p> <code>Currently it handles only </code><font SIZE="-1"><code>TCP</code></font><code> and silently fails on other traffic!</code> Awaiting enhancement&#8230; you&#8217;re welcome to help.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t</code> or <code>&#8211;daytime</code></p>
<dd> Adjust times relative to the first timestamp. (Defaults on.)</dl>
<p> This module also supports the standard fsdb options:</p>
<dl>
<dt><code>-d</code></p>
<dd> Enable debugging output.</p>
<dt><code>-i</code> or <code>&#8211;input</code> InputSource</p>
<dd> Read from InputSource, typically a file name, or <tt>&quot;-&quot;</tt> for standard input, or (if in Perl) a IO::Handle, Fsdb::IO or Fsdb::BoundedQueue objects.</p>
<dt><code>-o</code> or <code>&#8211;output</code> OutputDestination</p>
<dd> Write to OutputDestination, typically a file name, or <tt>&quot;-&quot;</tt> for standard output, or (if in Perl) a IO::Handle, Fsdb::IO or Fsdb::BoundedQueue objects.</p>
<dt><code>&#8211;autorun</code> or <code>&#8211;noautorun</code></p>
<dd> By default, programs process automatically, but Fsdb::Filter objects in Perl do not run until you invoke the <i>run()</i> method. The <tt>&quot;--(no)autorun&quot;</tt> option controls that behavior within Perl.</p>
<dt><code>&#8211;help</code></p>
<dd> Show help.</p>
<dt><code>&#8211;man</code></p>
<dd> Show full manual.</dl>
<h2>SAMPLE USAGE</h2>
<h3>Input:</h3>
<pre><code>
14 : 11 : 12.556781 dash.isi.edu .1023 &gt; excalibur.usc.edu.ssh : S 2306448962 : 2306448962(0)win 32120 &lt; mss 1460, sackOK, timestamp 82802652 [| tcp] &gt; (DF)14 : 11 : 12.561734 excalibur.usc.edu.ssh &gt; dash.isi.edu .1023 : S 1968320001 : 1968320001(0)ack 2306448963 win 4096 14 : 11 : 12.561875 dash.isi.edu .1023 &gt; excalibur.usc.edu.ssh :.ack 1 win 32120(DF)14 : 11 : 18.746567 excalibur.usc.edu.ssh &gt; dash.isi.edu .1023 : P 316 : 328(12)ack 348 win 4096 14 : 11 : 18.755176 dash.isi.edu .1023 &gt; excalibur.usc.edu.ssh : P 348 : 488(140)ack 328 win 32696(DF)[tos 0x10] 14 : 11 : 18.847937 excalibur.usc.edu.ssh &gt; dash.isi.edu .1023 : P 328 : 468(140)ack 488 win 4096 14 : 11 : 18.860047 dash.isi.edu .1023 &gt; excalibur.usc.edu.ssh :.ack 468 win 32696(DF)[tos 0x10] 14 : 11 : 18.936255 dash.isi.edu .1023 &gt; excalibur.usc.edu.ssh : P 488 : 516(28)ack 468 win 32696(DF)[tos 0x10]
</code></pre>
<h3>Command:</h3>
<pre>
    tcpdump_to_db
</pre>
<h3>Output:</h3>
<pre>
    #fsdb time proto src dest flags start end len ack win
    51072.556781 tcp dash.isi.edu.1023 excalibur.usc.edu.ssh S 2306448962 2306448962 0 - 32120
    51072.561734 tcp excalibur.usc.edu.ssh dash.isi.edu.1023 S 1968320001 1968320001 0 2306448963 4096
    51072.561875 tcp dash.isi.edu.1023 excalibur.usc.edu.ssh . - - - 1 32120
    51078.746567 tcp excalibur.usc.edu.ssh dash.isi.edu.1023 P 316 328 12 348 4096
    51078.755176 tcp dash.isi.edu.1023 excalibur.usc.edu.ssh P 348 488 140 328 32696
    51078.847937 tcp excalibur.usc.edu.ssh dash.isi.edu.1023 P 328 468 140 488 4096
    51078.860047 tcp dash.isi.edu.1023 excalibur.usc.edu.ssh . - - - 468 32696
    51078.936255 tcp dash.isi.edu.1023 excalibur.usc.edu.ssh P 488 516 28 468 32696
    #  | tcpdump_to_db
</pre>
<h2>SEE ALSO</h2>
<p> Fsdb.</p>
<h2>AUTHOR and COPYRIGHT</h2>
<p> Copyright (C) 1991-2008 by John Heidemann &lt;johnh [at] isi.edu&gt; </p>
<p> This program is distributed under terms of the <font SIZE="-1">GNU</font> general public license, version 2. See the file <font SIZE="-1">COPYING</font> with the distribution for details. </p>
<h2>Index</h2>
