---
title: "pdl2(1)"
name: "pdl2"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdl2/"
---

<h2 class="name">NAME</h2>
 

 pdl2 - Simple shell (version 2) for PDL 

<h2>SYNOPSIS</h2>

 Use <font SIZE="-1">PDL</font> interactively: 

 <pre>
  %&gt; pdl2
  pdl&gt; $a = sequence(10)  # or any other perl or PDL command
  
  pdl&gt; print &quot;\$a = $a\n&quot;; 
  $a = [0 1 2 3 4 5 6 7 8 9]
</pre>

<h2>DESCRIPTION</h2>

 The <tt>&quot;pdl2&quot;</tt> program, also known as the Perldl2 shell, is a second generation version of the original <tt>&quot;perldl&quot;</tt> interactive <font SIZE="-1">PDL</font> shell. It attempts to be backward compatible in usage while providing improved features, better support for Perl syntax, and an more easily extended framework based on the Devel::REPL shell. 

 If you have Devel::REPL version 1.003011 or later, then <tt>&quot;pdl2&quot;</tt> will start with full functionality. If Devel::REPL is not installed or found then <tt>&quot;pdl2&quot;</tt> will print a warning and run the legacy <tt>&quot;perldl&quot;</tt> shell command instead. 

 By default, command lines beginning with the default prompt of either <tt>&quot;pdl2&quot;</tt> or <tt>&quot;perldl&quot;</tt> (one of 'pdl&gt; ', '<font SIZE="-1">PDL</font>&gt; ', or 'perldl&gt; ') will have the prefix string and surrounding whitespace stripped. This allows for easy cut-and-paste from sample <font SIZE="-1">PDL</font> shell sessions or other examples into another <font SIZE="-1">PDL</font> shell session.

<h2>FUNCTIONS</h2>

<h3>do_print</h3>

 Toggle print-by-default on and off (default value: off) 

 By default, <tt>&quot;pdl2&quot;</tt> does not print the results of operations since the results can be very large (e.g., a small 640x480 <font SIZE="-1">RGBA</font> image is still more than 1_000_000 elements). However, for experimenting and debugging more complex structures, it helps to see the results of <i>every</i> operation. The <tt>&quot;do_print&quot;</tt> routine allows you to toggle between the default ``quiet'' operation and a full Read, Evaluate, Loop style. 

 <pre>
  pdl&gt; $a = pdl(3,2)
  pdl&gt; do_print
  1
  pdl&gt; $a = pdl(3,2)
  $PDL1 = [3 2];
  pdl&gt; do_print
  pdl&gt; $a = pdl(3,2)
</pre>

<h2>VARIABLES</h2>

<dl>
<dt>$PDL::toolongtoprint
<dd> The maximal size pdls to print (defaults to 10000 elements). This is not just a <tt>&quot;perldl&quot;</tt> or <tt>&quot;pdl2&quot;</tt> variable but it is something that is usually needed in an interactive debugging session.</dl>

<h2>SEE ALSO</h2>

 perldl, Devel::REPL 

<h2>Index</h2>


