---
title: "ptar(1)"
name: "ptar"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ptar/"
description: "ptar – a tar-like program written in perl"
---

<h2 class="name">NAME</h2>
<p> ptar &#8211; a tar-like program written in perl </p>
<h2>DESCRIPTION</h2>
<p> ptar is a small, tar look-alike program that uses the perl module Archive::Tar to extract, create and list tar archives.</p>
<h2>SYNOPSIS</h2>
<pre><code>
ptar - c[-v][-z][-C][-f ARCHIVE_FILE | -] FILE FILE... ptar - c[-v][-z][-C][-T index | -][-f ARCHIVE_FILE | -] ptar - x[-v][-z][-f ARCHIVE_FILE | -] ptar - t[-z][-f ARCHIVE_FILE | -] ptar - h
</code></pre>
<h2>OPTIONS</h2>
<pre>
    c   Create ARCHIVE_FILE or STDOUT (-) from FILE
    x   Extract from ARCHIVE_FILE or STDIN (-)
    t   List the contents of ARCHIVE_FILE or STDIN (-)
    f   Name of the ARCHIVE_FILE to use. Default is './default.tar'
    z   Read/Write zlib compressed ARCHIVE_FILE (not always available)
    v   Print filenames as they are added or extracted from ARCHIVE_FILE
    h   Prints this help message
    C   CPAN mode - drop 022 from permissions
    T   get names to create from file
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1), Archive::Tar. </p>
<h2>Index</h2>
