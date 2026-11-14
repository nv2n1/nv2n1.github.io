---
title: "getcol(1)"
name: "getcol"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getcol/"
description: "getcol – Extract specified columns from an ASCII table file"
---

<h2>Name</h2>
<p> getcol &#8211; Extract specified columns from an ASCII table file</p>
<h2>Synopsis</h2>
<p> getcol [-amv][-n num][-r lines][-s num] filename [column number range]</p>
<h2>Description</h2>
<p> Extract specified columns from an ASCII table file </p>
<h2>Options</h2>
<dl>
<dt><code>filename</code></p>
<dd> Name of a ASCII table file. At least one of these must be present for any values to be printed. If it is stdin or STDIN, an ASCII table is expected as standard input. If there is no input file, standard input is assumed.</p>
<dt><code>@filename</code></p>
<dd> Name of a file containing a list of ASCII table files. If this is present, any other file names on the command line will be ignored.</p>
<dt><code>field range</code></p>
<dd> Print value of these columns for the number of lines of the table specified by the -n argument after the skippiing the number of lines specified by the -s argument. A value of 0 causes the entire input line to be printed.</p>
<dt><code>-a</code></p>
<dd> Sum all numeric columns selected, printing the sum on the line following the result. Columns with no sum are filled with ___. (Added in version 2.6.9)</p>
<dt><code>-b</code></p>
<dd> Input is bar-separate table file</p>
<dt><code>-c</code></p>
<dd> Add count of number of lines in each column at end</p>
<dt><code>-d &lt;number&gt;</code></p>
<dd> Number of decimal places in f.p. output</p>
<dt><code>-e</code></p>
<dd> Compute medians of selected columns</p>
<dt><code>-f</code></p>
<dd> Print range of values in selected columns</p>
<dt><code>-h</code></p>
<dd> Print Starbase tab table header</p>
<dt><code>-i</code></p>
<dd> Input is tab-separate table file</p>
<dt><code>-k</code></p>
<dd> Print number of columns on first line</p>
<dt><code>-l &lt;number&gt;</code></p>
<dd> Number of lines to add to each line</p>
<dt><code>-m</code></p>
<dd> Compute the means of all numeric columns selected, printing the mean on the line following the result (or the line following the sum if -a is used). Columns with no mean are filled with ___. (Added in version 2.6.9)</p>
<dt><code>-n num</code></p>
<dd> Print selected columns for this many lines. If not specified, all lines will be read after the number of lines specified by -s have been skipped.</p>
<dt><code>-o</code></p>
<dd> OR conditions insted of ANDing them</p>
<dt><code>-p</code></p>
<dd> Print only sum, mmean, sigma, median, or range, not entries</p>
<dt><code>-r @listfile</code></p>
<dd> <code>-r line range</code> Print columns from the lines specified as either the first nonzero number on each line of the file listfile or the comma- and hyphen- delimitied range; i.e. 1-5,10-12 will print values from lines 1, 2, 3, 4, 5, 10, 11, and 12. (added in version 2.6.12)</p>
<dt><code>-s num</code></p>
<dd> Skip this many line before starting to print values. If not specified, no lines will be skipped.</p>
<dt><code>-t</code></p>
<dd> Starbase (tab-separated) table output</p>
<dt><code>-v</code></p>
<dd> Print more information about process.</p>
<dt>
<dd></dl>
<h2>Web Page</h2>
<p> <a rel="nofollow" href="http://tdc-www.harvard.edu/software/wcstools/getcol.html">http://tdc-www.harvard.edu/software/wcstools/getcol.html</a> </p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
