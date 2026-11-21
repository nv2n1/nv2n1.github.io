---
title: "cbtest(1)"
name: "cbtest"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cbtest/"
description: "cbtest – test cases for QDBM Cabin"
---

<h2 class="name">NAME</h2>
<p> cbtest &#8211; test cases for QDBM Cabin</p>
<h2>SYNOPSIS</h2>
<p> <code>cbtest sort</code> [-d] <i>rnum</i><br />
 <code>cbtest strstr</code> [-d] <i>rnum</i><br />
 <code>cbtest list</code> [-d] <i>rnum</i><br />
 <code>cbtest map</code> [-d] <i>rnum</i><br />
 <code>cbtest wicked</code> <i>rnum</i><br />
 <code>cbtest misc</code> </p>
<h2>DESCRIPTION</h2>
<p> The command `cbtest&#8217; is a utility for facility test and performance test. Measure the execution time of the command. This command is used in the following format. `rnum&#8217; specifies the number of records. </p>
<dl>
<dt><code>cbtest sort [-d] rnum</code></dt>
<dd> Perform test of sorting algorithms.</dd>
<dt><code>cbtest sort [-d] rnum</code></dt>
<dd> Perform test of string locating algorithms.</dd>
<dt><code>cbtest list [-d] rnum</code></dt>
<dd> Perform writing test of list.</dd>
<dt><code>cbtest map [-d] rnum</code></dt>
<dd> Perform writing test of map.</dd>
<dt><code>cbtest wicked rnum</code></dt>
<dd> Perform updating operations of list and map selected at random.</dd>
<dt><code>cbtest misc</code></dt>
<dd> Perform test of miscellaneous routines.</dd></dl>
<p> Options feature the following. </p>
<dl>
<dt>
</dt><dd> <code>-d</code> : read and show data of the result.</dd></dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code>qdbm</code>(3), <code>cabin</code>(3) </p>
<h2>AUTHOR</h2>
<p> QDBM was written by Mikio Hirabayashi &lt;mikio [at] fallabs.com&gt;. </p>
