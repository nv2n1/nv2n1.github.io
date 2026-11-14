---
title: "hwloc-patch(1)"
name: "hwloc-patch"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hwloc-patch/"
description: "hwloc-patch – Apply a topology difference to an existing XML topology"
---

<h2>NAME</h2>
<p> hwloc-patch &#8211; Apply a topology difference to an existing XML topology</p>
<h2>SYNOPSIS</h2>
<p> <code>hwloc-patch</code> [<i>options</i>] <i>[&lt;topology.xml&gt; | refname]</i> <i>[&lt;diff.xml&gt; | -]</i> <i>&lt;output.xml&gt;</i> </p>
<p> <code>hwloc-patch</code> [<i>options</i>] <i>[&lt;topology.xml&gt; | refname]</i> <i>[&lt;diff.xml&gt; | -]</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-R &#8211;reverse</code></p>
<dd> Reverse the sense the difference file.</p>
<dt><code>&#8211;version</code></p>
<dd> Report version and exit.</dl>
<h2>DESCRIPTION</h2>
<p> hwloc-patch loads the difference between two topologies from a XML file (or from the standard input) and applies it to an existing topology, generating a new, modified one. </p>
<p> The XML difference may have been computed earlier with hwloc-diff or hwloc-compress-dir. </p>
<p> If &lt;output.xml&gt; is given, the new, modified topology is stored in that new file. Otherwise, &lt;topology.xml&gt; is modified in place. </p>
<p> If <code>refname</code> is given instead of &lt;topology.xml&gt;, the input topology filename is automatically guessed by reading the refname field of the XML diff file. By default hwloc-diff generates XML diffs with the right reference topology filename (without any path prefix). </p>
<p> If <code>&#8211;</code> is given instead of &lt;diff.xml&gt;, the topology difference is read from the standard input. </p>
<p> <code>NOTE:</code> It is highly recommended that you read the <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7) overview page before reading this man page. Most of the concepts described in <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7) directly apply to the hwloc-patch utility.</p>
<h2>EXAMPLES</h2>
<p> hwloc-patch&#8217;s operation is best described through several examples. </p>
<p> Apply a XML topology difference file to an existing topology: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-patch fourmi023.xml diff.xml fourmi023-new.xml </p>
<p> Apply a XML topology difference file whole refname field contains the right input topology: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-patch refname diff.xml fourmi023-new.xml </p>
<p> Apply a XML topology from the standard intput: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>cat diff.xml | hwloc-patch fourmi023.xml &#8211; fourmi023-new.xml </p>
<p> Directly compute the difference between two topologies and apply it to another one, in place: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>hwloc-diff fourmi023.xml fourmi024.xml | hwloc-patch fourmi025.xml &#8211; </p>
<h2>RETURN VALUE</h2>
<p> Upon successful execution, hwloc-patch outputs the modified topology. The return value is 0. </p>
<p> hwloc-patch also returns nonzero if any kind of error occurs, such as (but not limited to) failure to parse the command line.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7), <a href="/docs/linux/man/1-lstopo/">lstopo</a>(1), <a href="/docs/linux/man/1-hwloc-diff/">hwloc-diff</a>(1), <a href="/docs/linux/man/1-hwloc-compress-dir/">hwloc-compress-dir</a>(1) </p>
<h2>Index</h2>
