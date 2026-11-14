---
title: "combine(1)"
name: "combine"
section: "1"
letter: "c"
url: "/docs/linux/man/1-combine/"
description: "combine – combine sets of lines from two files using boolean operations"
---

<h2 class="name">NAME</h2>
<p> combine &#8211; combine sets of lines from two files using boolean operations </p>
<h2>SYNOPSIS</h2>
<p> combine file1 and file2 </p>
<p> combine file1 not file2 </p>
<p> combine file1 or file2 </p>
<p> combine file1 xor file2 </p>
<p> _ file1 and file2 _ </p>
<p> _ file1 not file2 _ </p>
<p> _ file1 or file2 _ </p>
<p> _ file1 xor file2 _</p>
<h2>DESCRIPTION</h2>
<p> <code>combine</code> combines the lines in two files. Depending on the boolean operation specified, the contents will be combined in different ways:</p>
<dl>
<dt>and</p>
<dd> Outputs lines that are in file1 if they are also present in file2.</p>
<dt>not</p>
<dd> Outputs lines that are in file1 but not in file2.</p>
<dt>or</p>
<dd> Outputs lines that are in file1 or file2.</p>
<dt>xor</p>
<dd> Outputs lines that are in either file1 or file2, but not in both files.</dl>
<p> &#8220;-&#8221; can be specified for either file to read stdin for that file. </p>
<p> The input files need not be sorted, and the lines are output in the order they occur in file1 (followed by the order they occur in file2 for the two &#8220;or&#8221; operations). Bear in mind that this means that the operations are not commutative; &#8220;a and b&#8221; will not necessarily be the same as &#8220;b and a&#8221;. To obtain commutative behavior sort and uniq the result. </p>
<p> Note that this program can be installed as &#8220;_&#8221; to allow for the syntactic sugar shown in the latter half of the synopsis (similar to the test/[ command). It is not currently installed as &#8220;_&#8221; by default, but you can alias it to that if you like.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-join/">join</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright 2006 by Joey Hess &lt;id [at] joeyh.name&gt; </p>
<p> Licensed under the <font SIZE="-1">GNU GPL.</font> </p>
<h2>Index</h2>
