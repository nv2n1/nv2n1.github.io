---
title: "atomic-diff(1)"
name: "atomic-diff"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atomic-diff/"
description: "atomic-diff – show the differences between two images|containers RPMs"
---

<h2 class="name">NAME</h2>
<p> atomic-diff &#8211; show the differences between two images|containers RPMs </p>
<h2>SYNOPSIS</h2>
<p> <code>atomic diff</code> [<code>-h</code>|<code>&#8211;help</code>] [<code>&#8211;json</code>] [<code>&#8211;names-only</code>] [<code>-n</code>][<code>&#8211;no-files</code>] [<code>-r</code>][<code>&#8211;rpms</code>] [<code>-v</code>][<code>&#8211;verbose</code>] image|container image|container &#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>atomic diff</code> will compare the files found in two different images or containers and output to stdout or as JSON. By default, the comparison is done on the file level but there are switches for comparing RPMs and metadata as well. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement. </p>
<p> <code>&#8211;json</code><br />
&nbsp;<wbr>&nbsp;<wbr>Output in the form of JSON. </p>
<p> <code>-k</code> <code>&#8211;keywords</code><br />
&nbsp;<wbr>&nbsp;<wbr>Use the following keywords for comparison of files.&nbsp;<wbr>&nbsp;<wbr>You must select at least one but multiple can<br />
&nbsp;<wbr>&nbsp;<wbr>be used as well. Keywords that are used for this option are exclusive, which means that any only those<br />
&nbsp;<wbr>&nbsp;<wbr>keywords will be used. </p>
<p> Keywords currently defined are: <code>all</code>, <code>link</code>, <code>nlink</code>, <code>mode</code>, <code>type</code>, <code>time</code>, <code>uid</code>, <code>gid</code>, <code>size</code>, <code>sha256digest</code> </p>
<p> <code>-m</code> <code>&#8211;metadata</code><br />
&nbsp;<wbr>&nbsp;<wbr>Show the differences in the metadata for the two images or containers. </p>
<p> <code>-n</code> <code>&#8211;no-files</code><br />
&nbsp;<wbr>&nbsp;<wbr>Do not perform a file based diff between the two images or containers.&nbsp;<wbr>&nbsp;<wbr>Often used<br />
&nbsp;<wbr>&nbsp;<wbr>when performing an RPM-based diff to restrict output. </p>
<p> <code>&#8211;names-only</code><br />
&nbsp;<wbr>&nbsp;<wbr>When performing the diff, only compare package names and not their versions. </p>
<p> <code>-r</code> <code>&#8211;rpms</code><br />
&nbsp;<wbr>&nbsp;<wbr>Show the where the two docker objects have different RPMs. </p>
<p> <code>-v</code> <code>&#8211;verbose</code><br />
&nbsp;<wbr>&nbsp;<wbr>Be verbose in showing the differences in RPMs.&nbsp;<wbr>&nbsp;<wbr>The default will only show the differences in RPMs, whereas<br />
&nbsp;<wbr>&nbsp;<wbr>with&nbsp;<wbr><code>verbose</code>&nbsp;<wbr>it will show all the RPMS in each object. </p>
<h2>EXAMPLES</h2>
<p> Compare images the files in &#8216;foo1&#8217; and &#8216;foo2&#8217;. </p>
<dl>
<dt>
<dd>
<pre>
atomic diff foo1 foo2
</pre>
</dl>
<p> Compare the files in images &#8216;foo1&#8217; and &#8216;foo2&#8217; and output in JSON. </p>
<dl>
<dt>
<dd>
<pre>
atomic diff --json foo1 foo2
</pre>
</dl>
<p> Compare only the RPMs in images &#8216;foo1&#8217; and &#8216;foo2&#8217; </p>
<dl>
<dt>
<dd>
<pre>
atomic diff -r -n foo1 foo2
</pre>
</dl>
<p> Compare the files and RPMs (without versions) in images &#8216;foo1&#8217; and &#8216;foo2&#8217; and output as json </p>
<dl>
<dt>
<dd>
<pre>
atomic diff -r --json foo1 foo2
</pre>
</dl>
<p> Compare only the metadata between images &#8216;foo1&#8217; and &#8216;foo2&#8217; </p>
<dl>
<dt>
<dd>
<pre>
atomic diff -m foo1 foo2
</pre>
</dl>
<p> Compare files by &#8216;sha256digests&#8217; and &#8216;time&#8217; between images &#8216;foo1&#8217; and &#8216;foo2&#8217; </p>
<dl>
<dt>
<dd>
<pre>
atomic diff foo1 foo2 --keywords sha256digest time
</pre>
</dl>
<h2>HISTORY</h2>
<p> Updated by Brent Baude (bbaude at redhat dot com) Nov 2016 Updated by Brent Baude (bbaude at redhat dot com) May 2016 Initial revision by Brent Baude (bbaude at redhat dot com) November 2015 </p>
<h2>Index</h2>
