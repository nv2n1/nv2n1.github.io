---
title: "dbilogstrip(1)"
name: "dbilogstrip"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbilogstrip/"
---

<h2 class="name">NAME</h2>
 

 dbilogstrip - filter to normalize DBI trace logs for diff'ing 

<h2>SYNOPSIS</h2>

 Read <font SIZE="-1">DBI</font> trace file <tt>&quot;dbitrace.log&quot;</tt> and write out a stripped version to <tt>&quot;dbitrace_stripped.log&quot;</tt> 

 <pre>
  dbilogstrip dbitrace.log &gt; dbitrace_stripped.log
</pre> 

 Run <tt>&quot;yourscript.pl&quot;</tt> twice, each with different sets of arguments, with <font SIZE="-1">DBI_TRACE</font> enabled. Filter the output and trace through <tt>&quot;dbilogstrip&quot;</tt> into a separate file for each run. Then compare using diff. (This example assumes you're using a standard shell.) 

 <pre>
  DBI_TRACE=2 perl yourscript.pl ...args1... 2&gt;&amp;1 | dbilogstrip &gt; dbitrace1.log
  DBI_TRACE=2 perl yourscript.pl ...args2... 2&gt;&amp;1 | dbilogstrip &gt; dbitrace2.log
  diff -u dbitrace1.log dbitrace2.log
</pre>

<h2>DESCRIPTION</h2>

 Replaces any hex addresses, e.g, <tt>0x128f72ce</tt> with <tt>&quot;0xN&quot;</tt>. 

 Replaces any references to process id or thread id, like <tt>&quot;pid#6254&quot;</tt> with <tt>&quot;pidN&quot;</tt>. 

 So a <font SIZE="-1">DBI</font> trace line like this: 

 <pre>
  -&gt; STORE for DBD::DBM::st (DBI::st=HASH(0x19162a0)~0x191f9c8 'f_params' ARRAY(0x1922018)) thr#1800400
</pre> 

 will look like this: 

 <pre>
  -&gt; STORE for DBD::DBM::st (DBI::st=HASH(0xN)~0xN 'f_params' ARRAY(0xN)) thrN
</pre> 

<h2>Index</h2>


