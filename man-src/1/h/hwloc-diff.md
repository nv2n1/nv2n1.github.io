---
title: "hwloc-diff(1)"
name: "hwloc-diff"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hwloc-diff/"
description: "hwloc-diff – Compute differences between two XML topologies"
---

<h2>NAME</h2>
<p> hwloc-diff &#8211; Compute differences between two XML topologies</p>
<h2>SYNOPSIS</h2>
<p> <code>hwloc-diff</code> [<i>options</i>] <i>&lt;input1.xml&gt;</i> <i>&lt;input2.xml&gt;</i> </p>
<p> <code>hwloc-diff</code> [<i>options</i>] <i>&lt;input1.xml&gt;</i> <i>&lt;input2.xml&gt;</i> <i>&lt;output.xml&gt;</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;refname</code> &lt;name&gt;</p>
<dd> Use &lt;name&gt; as the identifier for the reference topology in the output XML difference. It is meant to tell which topology should be used when applying the resulting difference. hwloc-patch may use that name to automatically load the relevant reference topology XML. By default, &lt;input1.xml&gt; is used without its full path.</p>
<dt><code>&#8211;version</code></p>
<dd> Report version and exit.</dl>
<h2>DESCRIPTION</h2>
<p> hwloc-diff computes the difference between two XML topologies and stores the result into &lt;output.xml&gt; if any, or dumps it to stdout otherwise. </p>
<p> The output difference may later be applied to another topology with hwloc-patch. </p>
<p> hwloc-compress-dir may be used for computing the diffs between all XML files in a directory. </p>
<p> <code>NOTE:</code> It is highly recommended that you read the <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7) overview page before reading this man page. Most of the concepts described in <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7) directly apply to the hwloc-diff utility.</p>
<h2>EXAMPLES</h2>
<p> hwloc-diff&#8217;s operation is best described through several examples. </p>
<p> Compute the difference between two XML topologies and output it to stdout: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-diff fourmi023.xml fourmi024.xml<br />
&nbsp;<wbr>Found 11 differences, exporting to stdout<br />
&nbsp;<wbr>&lt;?xml version=&quot;1.0&quot;&nbsp;<wbr>encoding=&quot;UTF-8&quot;?&gt;<br />
&nbsp;<wbr>&#8230; </p>
<p> Output the difference to file diff.xml instead: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-diff fourmi023.xml fourmi024.xml diff.xml<br />
&nbsp;<wbr>Found 11 differences, exporting to diff.xml </p>
<p> When the difference is too complex to be represented: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-diff fourmi023.xml avakas-frontend1.xml<br />
&nbsp;<wbr>Found 1 differences, including 1 too complex ones.<br />
&nbsp;<wbr>Cannot export differences to stdout </p>
<p> Directly compute the difference between two topologies and apply it to another one: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-diff fourmi023.xml fourmi024.xml | hwloc-patch fourmi025.xml &#8211; </p>
<h2>RETURN VALUE</h2>
<p> Upon successful execution, hwloc-diff outputs the difference. The return value is 0. </p>
<p> If the difference is too complex to be represented, an error is returned and the output is not generated. </p>
<p> hwloc-diff also returns nonzero if any kind of error occurs, such as (but not limited to) failure to parse the command line.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7), <a href="/docs/linux/man/1-lstopo/">lstopo</a>(1), <a href="/docs/linux/man/1-hwloc-patch/">hwloc-patch</a>(1), <a href="/docs/linux/man/1-hwloc-compress-dir/">hwloc-compress-dir</a>(1) </p>
<h2>Index</h2>
