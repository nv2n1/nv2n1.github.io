---
title: "shlock(1)"
name: "shlock"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shlock/"
description: "shlock – Create lock files for use in shell scripts"
---

<h2 class="name">NAME</h2>
<p> shlock &#8211; Create lock files for use in shell scripts </p>
<h2>SYNOPSIS</h2>
<p> <code>shlock</code> [<code>-b</code>|<code>-c</code>|<code>-u</code>] <code>-f</code> <i>name</i> <code>-p</code> <i>pid</i></p>
<h2>DESCRIPTION</h2>
<p> <code>shlock</code> tries to create a lock file named <i>name</i> and write the process <font SIZE="-1">ID</font> <i>pid</i> into it. If the file already exists, <code>shlock</code> will read the process <font SIZE="-1">ID</font> from the file and test to see whether the process is currently running. If the process exists, then the file will not be created. <i>shlock</i> exits with a zero status if it could create the lock file, or non-zero if the file refers to a currently active process. </p>
<p> A Perl wrapper around <code>shlock</code> can be used via the <tt>&quot;INN::Utils::Shlock&quot;</tt> module.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></p>
<dd> Process IDs are normally read and written in <font SIZE="-1">ASCII</font>. If the <code>-b</code> flag is used, then they will be written as a binary int.</p>
<dt><code>-c</code></p>
<dd> If the <code>-c</code> flag is used, then <code>shlock</code> will not create a lock file, but will instead use the file to see if the lock is held by another program. If the lock is valid, the program will exit with a non-zero status; if the lock is not valid (i.e. invoking <code>shlock</code> without the flag would have succeeded), then the program will exit with a zero status.</p>
<dt><code>-f</code> <i>name</i></p>
<dd> <i>name</i> is the name of the lock file <code>shlock</code> attempts to create. If the file already exists, it will read the process <font SIZE="-1">ID</font> from the file and exit with a non-zero status if this process is currently active.</p>
<dt><code>-p</code> <i>pid</i></p>
<dd> <i>pid</i> is the process <font SIZE="-1">ID</font> to write into the file <i>name</i>.</p>
<dt><code>-u</code></p>
<dd> For compatibility with other systems, the <code>-u</code> flag is accepted as a synonym for <code>-b</code> since binary locks are used by many <font SIZE="-1">UUCP</font> packages.</dl>
<h2>EXAMPLES</h2>
<p> The following example shows how <code>shlock</code> would be used within a shell script: </p>
<pre><code>
LOCK = &lt;pathrun in inn.conf&gt; / LOCK.send
                                   trap 'rm -f ${LOCK} ; exit 1' 1 2 3 15 if shlock -
       p $$ - f ${LOCK};
then
#Do appropriate work.
    else echo "Locked by `cat ${LOCK}`" fi
</code></pre>
<h2>HISTORY</h2>
<p> Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews after a description of <font SIZE="-1">HDB</font> <font SIZE="-1">UUCP</font> locking given by Peter Honeyman, and improved by Berend Reitsma to solve a race condition. Converted to <font SIZE="-1">POD</font> by Julien Elie. </p>
<p> <tt>$Id:</tt> shlock.pod 9304 2011-08-04 22:10:47Z iulius $</p>
<h2>SEE ALSO</h2>
<p> <i><a href="//www.systutorials.com/docs/linux/man/3pm-INN::Utils::Shlock/">INN::Utils::Shlock</a></i>(3pm). </p>
<h2>Index</h2>
