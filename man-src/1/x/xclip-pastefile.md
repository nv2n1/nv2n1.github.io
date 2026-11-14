---
title: "xclip-pastefile(1)"
name: "xclip-pastefile"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xclip-pastefile/"
description: "xclip-copyfile, xclip-cutfile, xclip-pastefile – copy and move files via the X clipboard"
---

<h2 class="name">NAME</h2>
<p> xclip-copyfile, xclip-cutfile, xclip-pastefile &#8211; copy and move files via the X clipboard </p>
<h2>SYNOPSIS</h2>
<p> <code>xclip-copyfile</code> [-p] FILES&#8230; </p>
<p> <code>xclip-cutfile</code> [-p] FILES&#8230; </p>
<p> <code>xclip-pastefile</code></p>
<h2>DESCRIPTION</h2>
<p> <code>xclip-copyfile</code> copies files into the X clipboard, recursing into directories. </p>
<p> <code>xclip-cutfile</code> copies the files, but also deletes them afterwards.</p>
<dl>
<dt><code>-p</code></p>
<dd> preserve path formation </p>
</dl>
<p> <code>xclip-pastefile</code> pastes the files out of the clipboard</p>
<h2>EXAMPLES</h2>
<p> <code>Copying a file to a remote host</code> </p>
<pre><code>
[maggie.lkpg.cendio.se ~] $ echo "A file created on ${HOSTNAME}" &gt; file1
                                                                           [maggie.lkpg.cendio.se ~] $ xclip -
                                                                       copyfile file1
                                                                           [sofie.homeip.net ~ / doc] $ xclip -
                                                                       pastefile
                                                                           file1
                                                                               [sofie.homeip.net ~ / doc] $ cat file1
                                                                                   A file created on maggie.lkpg.cendio.se
                                                                                       Copying an entire tree structure
                                                                                           [sofie.homeip.net ~] $ xclip -
                                                                       copyfile doc
                                                                           [maggie.lkpg.cendio.se ~ / tmp] $ xclip -
                                                                       pastefile
                                                                               doc /
                                                                           doc / letter -
                                                                       mom - april.txt doc / file1 doc / letter - dad - march.txt Copying files with preserved path information[maggie.lkpg.cendio.se ~] $ xclip - copyfile - p / etc / sysconfig / grub tar : Removing leading `/' from member names [sofie.homeip.net ~ / tmp] $ xclip - pastefile etc / sysconfig / grub[sofie.homeip.net ~ / tmp] $ ls etc / sysconfig / grub etc / sysconfig / grub Moving files[sofie.homeip.net ~] $ ls letter - brother - may.txt letter - brother - may.txt[sofie.homeip.net ~] $ xclip - cutfile letter - brother - may.txt[sofie.homeip.net ~] $ ls letter - brother - may.txt ls : cannot access letter - brother - may.txt : No such file or
    directory
            [sofie.homeip.net ~] $ cd doc
                [sofie.homeip.net ~ / doc] $ xclip -
        pastefile
            letter -
        brother - may.txt
</code></pre>
<h2>AUTHORS</h2>
<p> This manual page was written by Maximilian Gass &lt;mxey [at] cloudconnected.org&gt; for the Debian project. It may be used for everything else, of course. </p>
<h2>Index</h2>
