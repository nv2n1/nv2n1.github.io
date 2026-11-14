---
title: "httxt2dbm(1)"
name: "httxt2dbm"
section: "1"
letter: "h"
url: "/docs/linux/man/1-httxt2dbm/"
description: "httxt2dbm – Generate dbm files for use with RewriteMap"
---

<h2 class="name">NAME</h2>
<p> httxt2dbm &#8211; Generate dbm files for use with RewriteMap</p>
<h2>SYNOPSIS</h2>
<p>&nbsp; </p>
<p> <code>httxt2dbm</code> [ &#8211;<code>v</code> ] [ &#8211;<code>f</code> <i>DBM_TYPE</i> ] &#8211;<code>i</code> <i>SOURCE_TXT</i> &#8211;<code>o</code> <i>OUTPUT_DBM</i><br />
&nbsp; </p>
<h2>SUMMARY</h2>
<p>&nbsp; </p>
<p> <code>httxt2dbm</code> is used to generate dbm files from text input, for use in RewriteMap with the <code>dbm</code> map type.<br />
&nbsp; </p>
<p> If the output file already exists, it will not be truncated. New keys will be added and existing keys will be updated.<br />
&nbsp; </p>
<h2>OPTIONS</h2>
<p>&nbsp;<br />
&nbsp;</p>
<dl>
<dt><code>-v</code></p>
<dd> More verbose output</p>
<dt><code>-f </code><i>DBM_TYPE</i></p>
<dd> Specify the DBM type to be used for the output. If not specified, will use the APR Default. Available types are: <code>GDBM</code> for GDBM files, <code>SDBM</code> for SDBM files, <code>DB</code> for berkeley DB files, <code>NDBM</code> for NDBM files, <code>default</code> for the default DBM type.</p>
<dt><code>-i </code><i>SOURCE_TXT</i></p>
<dd> Input file from which the dbm is to be created. The file should be formatted with one record per line, of the form: <code>key value</code>. See the documentation for RewriteMap for further details of this file&#8217;s format and meaning.</p>
<dt><code>-o </code><i>OUTPUT_DBM</i></p>
<dd> Name of the output dbm files.<br />
&nbsp;</dl>
<h2>EXAMPLES</h2>
<p>&nbsp; </p>
<pre>
      httxt2dbm -i rewritemap.txt -o rewritemap.dbm
      httxt2dbm -f SDBM -i rewritemap.txt -o rewritemap.dbm 
</pre>
<p>&nbsp; </p>
<h2>Index</h2>
