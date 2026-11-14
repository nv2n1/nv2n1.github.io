---
title: "gendiff(1)"
name: "gendiff"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gendiff/"
description: "gendiff – utility to aid in error-free diff file generation"
---

<h2 class="name">NAME</h2>
<p> gendiff &#8211; utility to aid in error-free diff file generation </p>
<h2>SYNOPSIS</h2>
<p> <code>gendiff</code> &lt;directory&gt; &lt;diff-extension&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>gendiff</code> is a rather simple script which aids in generating a diff file from a single directory. It takes a directory name and a &quot;diff-extension&quot; as its only arguments. The diff extension should be a unique sequence of characters added to the end of all original, unmodified files. The output of the program is a diff file which may be applied with the <code>patch</code> program to recreate the changes. </p>
<p> The usual sequence of events for creating a diff is to create two identical directories, make changes in one directory, and then use the <code>diff</code> utility to create a list of differences between the two. Using gendiff eliminates the need for the extra, original and unmodified directory copy. Instead, only the individual files that are modified need to be saved. </p>
<p> Before editing a file, copy the file, appending the extension you have chosen to the filename. I.e. if you were going to edit somefile.cpp and have chosen the extension &quot;fix&quot;, copy it to somefile.cpp.fix before editing it. Then edit the first copy (somefile.cpp). </p>
<p> After editing all the files you need to edit in this fashion, enter the directory one level above where your source code resides, and then type </p>
<pre>
    $ gendiff somedirectory .fix &gt; mydiff-fix.patch
</pre>
<p> You should redirect the output to a file (as illustrated) unless you want to see the results on stdout. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1), <code><a href="/docs/linux/man/1-patch/">patch</a></code>(1) </p>
<h2>AUTHOR</h2>
<pre>
Marc Ewing &lt;marc [at] redhat.com&gt;
</pre>
<h2>Index</h2>
