---
title: "logtail(8)"
name: "logtail"
section: "8"
letter: "l"
url: "/docs/linux/man/8-logtail/"
description: "logtail – print log file lines that have not been read"
---

<p>logtail &#8211; print log file lines that have not been read</p>
<h2>Synopsis</h2>
<p><code>logtail</code> [-t] <code>-f</code><i>logfile</i> [-o<i>offsetfile</i>]</p>
<h2>Description</h2>
<p><code>logtail</code> reads a specified file (usually a log file) and writes to the standard output that part of it which has not been read by previous runs of <code>logtail</code>. It prints the appropriate number of bytes from the end of <i>logfile</i>, assuming that all changes that are made to it are to add new characters to it. </p>
<p> <i>logfile</i> must be a plain file. A symlink is not allowed. </p>
<p> <code>logtail</code> stores the information about how much of it has already been read in a separate file called <i>offsetfile</i>. <i>offsetfile</i> can be omitted. If omitted, the file named <i>logfile.offset</i> in the same directory which contains <i>logfile</i> is used by default. </p>
<p> If <i>offsetfile</i> is not empty, the inode of <i>logfile</i> is checked. If the inode is changed, <code>logtail</code> simply prints the entire file. If the inode is not changed but <i>logfile</i> is shorter than it was at the last run of <code>logtail</code>, it writes a warning message to the standard output.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></p>
<dd><i>logfile</i> to be read after offset</p>
<dt><code>-o</code></p>
<dd><i>offsetfile</i> stores offset of previous run</p>
<dt><code>-t</code></p>
<dd>test mode &#8211; do not change offset in <i>offsetfile</i></dl>
<h2>Return Values</h2>
<dl>
<dt>0</p>
<dd>successful</p>
<dt>65</p>
<dd>cannot get the size of <i>logfile</i></p>
<dt>66</p>
<dd><i>logfile</i> does not exist, is not a plain file, or is not readable</p>
<dt>73</p>
<dd>cannot write <i>offsetfile</i></dl>
<h2>Author</h2>
<p>The original <code>logtail</code> was written in C by Craig H. Rowland &lt;crowland [at] psionic.com&gt;. This version of <code>logtail</code> is a Perl reimplementation by Paul Slootman &lt;paul [at] debian.org&gt;. Enhanced by the Debian Logcheck Team &lt;logcheck-devel [at] lists.alioth.debian.org&gt;. </p>
<p> This manual was written by Oohara Yuuma &lt;oohara [at] libra.interq.or.jp&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-logcheck/">logcheck</a></code>(8) </p>
