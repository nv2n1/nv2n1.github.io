---
title: "statist(1)"
name: "statist"
section: "1"
letter: "s"
url: "/docs/linux/man/1-statist/"
description: "statist – calculate Huffman distribution for freeze(1)"
---

<h2>NAME</h2>
<p> statist &#8211; calculate Huffman distribution for <i><a href="/docs/linux/man/1-freeze/">freeze</a></i>(1)</p>
<h2>SYNOPSIS</h2>
<p> <code>statist</code> [ <code>-gx&#8230;</code> ] </p>
<h2>DESCRIPTION</h2>
<p> The default table is tuned for both C texts and executable files (as in LHARC). If you will freeze any other files (natural language texts, databases, images, fonts, etc.) you can calculate the matching positions distribution using the <code>`statist&#8217;</code> program, which calculates and displays the mentioned distribution for the given file. It is useful for large (100K or more) files. </p>
<p> Though the built-in position table is polyvalent, the tuning can increase the compression rate up to one additional percent. (Observed mainly on text files.)</p>
<h2>USAGE</h2>
<p> <code>statist [-g&#8230;] &lt; sample_file</code> or <code>gensample | statist [-g&#8230;]</code><br />
 where <code>`gensample&#8217;</code> is a program generating some sample stream of bytes similar to files to be frozen. </p>
<p> The <code>-g</code> and <code>-x</code> switches have the same meaning as for <i><a href="/docs/linux/man/1-freeze/">freeze</a></i>(1) and may be repeated. </p>
<p> You can also see the intermediate values and watch their changes by pressing INTR key when you wish. </p>
<p> Note: If you use <code>gensample | statist</code> , remember that INTR influence BOTH processes !!<br />
 The results have the following format:<br />
 <i>n1 n2 n3 n4 n5 n6 n7 n8</i> (uncertainty = <i>x)</i><br />
 Average match length: <i>xx.yy</i><br />
 Percentile 99.9: <i>p999</i><br />
 Percentile 99.5: <i>p995</i><br />
 Percentile 99.0: <i>p990</i><br />
 Percentile 97.0: <i>p970</i><br />
 Percentile 95.0: <i>p950</i><br />
 Percentile 90.0: <i>p900</i><br />
 Percentile 80.0: <i>p800</i><br />
 Percentile 70.0: <i>p700</i><br />
 Percentile 50.0: <i>p500</i><br />
 Sigma: <i>xx.yy</i> </p>
<p> Here <i>n1 &#8211; n8</i> are values of the calculated position table elements, uncertainty is a number which denotes validity of given results (non-zero values of uncertainty indicate that the results may be unusable). Other values (average match length, percentiles and sigma) are FYI only. </p>
<p> You may create the <i>/etc/default/freeze</i> file (if you don&#8217;t like <i>/etc/default/</i> directory, choose another &#8211; in MS-DOS it is FREEZE.CNF in the directory of FREEZE.EXE), which has the following format: <i>name</i> = <i>n1 n2 n3 n4 n5 n6 n7 n8</i> <i>(name</i> must start in column 1). For example:<br />
 &#8212;&#8212;&#8212;- cut here &#8212;&#8212;&#8212;&#8211;<br />
 # This is freeze&#8217;s defaults file<br />
 russian=0 0 1 2 6 20 31 2 # The sample was mailx.lp (Russian)<br />
 english=0 0 1 2 7 16 36 0 # The sample was gcc.lp (English)<br />
 # End of file<br />
 &#8212;&#8212;&#8212;- cut here &#8212;&#8212;&#8212;&#8211; </p>
<p> If you find values, which are better THAN DEFAULT both for text (C programs) and binary (executable) files, please send them to me. </p>
<p> Important note: statist.c is NOT a part of freeze package, it is an aditional feature. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-freeze/">freeze</a>(1), <a href="/docs/linux/man/1-melt/">melt</a>(1), <a href="/docs/linux/man/1-fcat/">fcat</a>(1)</p>
<h2>DIAGNOSTICS</h2>
<p> Huffman tree has more than 8 levels, reducing&#8230; Self-explanatory, but sometimes reducing falls into infinite loop. <i>xxx</i>K Progress indicator is written after each 4K of a file processed.</p>
<h2>BUGS</h2>
<p> Sometimes use of the results with uncertainty = 1 (on a file) gives compression rate worse than default but use of the results with uncertainty = 13 (on other file) works quite good. </p>
<p> Found bugs descriptions, incompatibilities, etc. please send to leo [at] s514.ipmce.su. </p>
<h2>Index</h2>
