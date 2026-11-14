---
title: "ptardiff(1)"
name: "ptardiff"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ptardiff/"
description: "ptardiff – program that diffs an extracted archive against an unextracted one"
---

<h2 class="name">NAME</h2>
<p> ptardiff &#8211; program that diffs an extracted archive against an unextracted one </p>
<h2>DESCRIPTION</h2>
<pre>
    ptardiff is a small program that diffs an extracted archive
    against an unextracted one, using the perl module Archive::Tar.
    This effectively lets you view changes made to an archives contents.
    Provide the progam with an ARCHIVE_FILE and it will look up all
    the files with in the archive, scan the current working directory
    for a file with the name and diff it against the contents of the
    archive.
</pre>
<h2>SYNOPSIS</h2>
<pre>
    ptardiff ARCHIVE_FILE
    ptardiff -h
    $ tar -xzf Acme-Buffy-1.3.tar.gz
    $ vi Acme-Buffy-1.3/README
    [...]
    $ ptardiff Acme-Buffy-1.3.tar.gz &gt; README.patch
</pre>
<h2>OPTIONS</h2>
<pre>
    h   Prints this help message
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1), Archive::Tar. </p>
<h2>Index</h2>
