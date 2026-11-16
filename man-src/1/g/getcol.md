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
<dt><code>filename</code></dt>
<dd> Name of a ASCII table file. At least one of these must be present for any values to be printed. If it is stdin or STDIN, an ASCII table is expected as standard input. If there is no input file, standard input is assumed.</dd>
<dt><code>@filename</code></dt>
<dd> Name of a file containing a list of ASCII table files. If this is present, any other file names on the command line will be ignored.</dd>
<dt><code>field range</code></dt>
<dd> Print value of these columns for the number of lines of the table specified by the -n argument after the skippiing the number of lines specified by the -s argument. A value of 0 causes the entire input line to be printed.</dd>
<dt><code>-a</code></dt>
<dd> Sum all numeric columns selected, printing the sum on the line following the result. Columns with no sum are filled with ___. (Added in version 2.6.9)</dd>
<dt><code>-b</code></dt>
<dd> Input is bar-separate table file</dd>
<dt><code>-c</code></dt>
<dd> Add count of number of lines in each column at end</dd>
<dt><code>-d &lt;number&gt;</code></dt>
<dd> Number of decimal places in f.p. output</dd>
<dt><code>-e</code></dt>
<dd> Compute medians of selected columns</dd>
<dt><code>-f</code></dt>
<dd> Print range of values in selected columns</dd>
<dt><code>-h</code></dt>
<dd> Print Starbase tab table header</dd>
<dt><code>-i</code></dt>
<dd> Input is tab-separate table file</dd>
<dt><code>-k</code></dt>
<dd> Print number of columns on first line</dd>
<dt><code>-l &lt;number&gt;</code></dt>
<dd> Number of lines to add to each line</dd>
<dt><code>-m</code></dt>
<dd> Compute the means of all numeric columns selected, printing the mean on the line following the result (or the line following the sum if -a is used). Columns with no mean are filled with ___. (Added in version 2.6.9)</dd>
<dt><code>-n num</code></dt>
<dd> Print selected columns for this many lines. If not specified, all lines will be read after the number of lines specified by -s have been skipped.</dd>
<dt><code>-o</code></dt>
<dd> OR conditions insted of ANDing them</dd>
<dt><code>-p</code></dt>
<dd> Print only sum, mmean, sigma, median, or range, not entries</dd>
<dt><code>-r @listfile</code></dt>
<dd> <code>-r line range</code> Print columns from the lines specified as either the first nonzero number on each line of the file listfile or the comma- and hyphen- delimitied range; i.e. 1-5,10-12 will print values from lines 1, 2, 3, 4, 5, 10, 11, and 12. (added in version 2.6.12)</dd>
<dt><code>-s num</code></dt>
<dd> Skip this many line before starting to print values. If not specified, no lines will be skipped.</dd>
<dt><code>-t</code></dt>
<dd> Starbase (tab-separated) table output</dd>
<dt><code>-v</code></dt>
<dd> Print more information about process.</dd>
</dl>
<h2>Web Page</h2>
<p> <a rel="nofollow" href="http://tdc-www.harvard.edu/software/wcstools/getcol.html">http://tdc-www.harvard.edu/software/wcstools/getcol.html</a> </p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
