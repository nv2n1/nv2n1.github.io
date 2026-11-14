---
title: "checkbashisms(1)"
name: "checkbashisms"
section: "1"
letter: "c"
url: "/docs/linux/man/1-checkbashisms/"
description: "checkbashisms – check for bashisms in /bin/sh scripts"
---

<h2>NAME</h2>
<p> checkbashisms &#8211; check for bashisms in /bin/sh scripts</p>
<h2>SYNOPSIS</h2>
<p> <code>checkbashisms</code> <i>script</i> &#8230;<br />
 <code>checkbashisms &#8211;help</code>|<code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <code>checkbashisms</code>, based on one of the checks from the <code>lintian</code> system, performs basic checks on <i>/bin/sh</i> shell scripts for the possible presence of bashisms. It takes the names of the shell scripts on the command line, and outputs warnings if possible bashisms are detected. </p>
<p> Note that the definition of a bashism in this context roughly equates to &quot;a shell feature that is not required to be supported by POSIX&quot;; this means that some issues flagged may be permitted under optional sections of POSIX, such as XSI or User Portability. </p>
<p> In cases where POSIX and Debian Policy disagree, <code>checkbashisms</code> by default allows extensions permitted by Policy but may also provide options for stricter checking.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code>, <code>-h</code></p>
<dd> Show a summary of options.</p>
<dt><code>&#8211;newline</code>, <code>-n</code></p>
<dd> Check for &quot;<code>echo -n</code>&quot; usage (non POSIX but required by Debian Policy 10.4.)</p>
<dt><code>&#8211;posix</code>, <code>-p</code></p>
<dd> Check for issues which are non POSIX but required to be supported by Debian Policy 10.4 (implies <code>-n</code>).</p>
<dt><code>&#8211;force</code>, <code>-f</code></p>
<dd> Force each script to be checked, even if it would normally not be (for instance, it has a bash or non POSIX shell shebang or appears to be a shell wrapper).</p>
<dt><code>&#8211;extra</code>, <code>-x</code></p>
<dd> Highlight lines which, whilst they do not contain bashisms, may be useful in determining whether a particular issue is a false positive which may be ignored. For example, the use of &quot;<code>$BASH_ENV</code>&quot; may be preceded by checking whether &quot;<code>$BASH</code>&quot; is set.</p>
<dt><code>&#8211;version</code>, <code>-v</code></p>
<dd> Show version and copyright information.</dl>
<h2>EXIT VALUES</h2>
<p> The exit value will be 0 if no possible bashisms or other problems were detected. Otherwise it will be the sum of the following error values:</p>
<dl>
<dt>1</p>
<dd> A possible bashism was detected.</p>
<dt>2</p>
<dd> A file was skipped for some reason, for example, because it was unreadable or not found. The warning message will give details.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> <code>checkbashisms</code> was originally written as a shell script by Yann Dirson &lt;<i>dirson [at] debian.org</i>&gt; and rewritten in Perl with many more features by Julian Gilbey &lt;<i>jdg [at] debian.org</i>&gt;. </p>
<h2>Index</h2>
