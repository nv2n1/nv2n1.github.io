---
title: "dbiprof(1)"
name: "dbiprof"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbiprof/"
---

<h2 class="name">NAME</h2>
 

 dbiprof - command-line client for DBI::ProfileData 

<h2>SYNOPSIS</h2>

 See a report of the ten queries with the longest total runtime in the profile dump file <i>prof1.out</i>: 

 <pre>
 dbiprof prof1.out
</pre> 

 See the top 10 most frequently run queries in the profile file <i>dbi.prof</i> (the default): 

 <pre>
  dbiprof --sort count
</pre> 

 See the same report with 15 entries: 

 <pre>
  dbiprof --sort count --number 15
</pre>

<h2>DESCRIPTION</h2>

 This tool is a command-line client for the DBI::ProfileData. It allows you to analyze the profile data file produced by DBI::ProfileDumper and produce various useful reports.

<h2>OPTIONS</h2>

 This program accepts the following options:
<dl>
<dt>--number N
<dd> Produce this many items in the report. Defaults to 10. If set to ``all'' then all results are shown.
<dt>--sort field
<dd> Sort results by the given field. Sorting by multiple fields isn't currently supported (patches welcome). The available sort fields are:
<dl>
<dt>
<dd>
<dl>
<dt>total
<dd> Sorts by total time run time across all runs. This is the default sort.
<dt>longest
<dd> Sorts by the longest single run.
<dt>count
<dd> Sorts by total number of runs.
<dt>first
<dd> Sorts by the time taken in the first run.
<dt>shortest
<dd> Sorts by the shortest single run.
<dt>key1
<dd> Sorts by the value of the first element in the Path, which should be numeric. You can also sort by <tt>&quot;key2&quot;</tt> and <tt>&quot;key3&quot;</tt>.</dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt>--reverse
<dd> Reverses the selected sort. For example, to see a report of the shortest overall time: 

 <pre>
  dbiprof --sort total --reverse
</pre>
<dt>--match keyN=value
<dd> Consider only items where the specified key matches the given value. Keys are numbered from 1. For example, let's say you used a DBI::Profile Path of: 

 <pre>
  [ DBIprofile_Statement, DBIprofile_Methodname ]
</pre> 

 And called dbiprof as in: 

 <pre>
  dbiprof --match key2=execute
</pre> 

 Your report would only show execute queries, leaving out prepares, fetches, etc. 

 If the value given starts and ends with slashes (<tt>&quot;/&quot;</tt>) then it will be treated as a regular expression. For example, to only include <font SIZE="-1">SELECT</font> queries where key1 is the statement: 

 <pre>
  dbiprof --match key1=/^SELECT/
</pre> 

 By default the match expression is matched case-insensitively, but this can be changed with the --case-sensitive option.
<dt>--exclude keyN=value
<dd> Remove items for where the specified key matches the given value. For example, to exclude all prepare entries where key2 is the method name: 

 <pre>
  dbiprof --exclude key2=prepare
</pre> 

 Like <tt>&quot;--match&quot;</tt>, If the value given starts and ends with slashes (<tt>&quot;/&quot;</tt>) then it will be treated as a regular expression. For example, to exclude <font SIZE="-1">UPDATE</font> queries where key1 is the statement: 

 <pre>
  dbiprof --match key1=/^UPDATE/
</pre> 

 By default the exclude expression is matched case-insensitively, but this can be changed with the --case-sensitive option.
<dt>--case-sensitive
<dd> Using this option causes --match and --exclude to work case-sensitively. Defaults to off.
<dt>--delete
<dd> Sets the <tt>&quot;DeleteFiles&quot;</tt> option to DBI::ProfileData which causes the files to be deleted after reading. See DBI::ProfileData for more details.
<dt>--dumpnodes
<dd> Print the list of nodes in the form of a perl data structure. Use the <tt>&quot;-sort&quot;</tt> option if you want the list sorted.
<dt>--version
<dd> Print the dbiprof version number and exit.</dl>

<h2>AUTHOR</h2>

 Sam Tregar &lt;sam [at] tregar.com&gt;

<h2>COPYRIGHT AND LICENSE</h2>

 Copyright (C) 2002 Sam Tregar 

 This program is free software; you can redistribute it and/or modify it under the same terms as Perl 5 itself.

<h2>SEE ALSO</h2>

 DBI::ProfileDumper, DBI::Profile, <font SIZE="-1">DBI</font>. 

<h2>Index</h2>


