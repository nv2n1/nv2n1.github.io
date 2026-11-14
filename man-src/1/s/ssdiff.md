---
title: "ssdiff(1)"
name: "ssdiff"
section: "1"
letter: "s"
url: "/docs/linux/man/1-ssdiff/"
description: "ssdiff – compare two spreadsheets"
---

<h2 class="name">NAME</h2>
<p> ssdiff &#8211; compare two spreadsheets</p>
<h2>SYNOPSIS</h2>
<p> <code>ssdiff </code> [<i>OPTIONS</i>] <i>OLDFILE</i> <i>NEWFILE</i> </p>
<h2>DESCRIPTION</h2>
<p> This manual page briefly documents the <code>ssdiff</code> command. </p>
<p> <code>ssdiff</code> is a command line utility to compare two spreadsheets and list their differences </p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with single letter options starting with a single dash (`-&#8216;) and longer options starting with two dashes (`&#8211;&#8216;). </p>
<h3>Output options</h3>
<dl>
<dt><code>-x, &#8211;xml</code></p>
<dd> Display differences in xml format </p>
</dl>
<h3>Help options</h3>
<dl>
<dt><code>-V, &#8211;version</code></p>
<dd> Display ssdiff&#8217;s version</p>
<dt><code>-?, &#8211;help</code></p>
<dd> Display the supported options </p>
</dl>
<h2>EXAMPLE</h2>
<p> To compare an old version of a file with a newer file, run: </p>
<p> <code>ssdiff</code> <i>old.gnumeric</i> <i>new.gnumeric</i> </p>
<p> The exit code will be 0 if no differences were found, 1 if differences were found, and 2 in case of trouble. </p>
<h2>LICENSE</h2>
<p> <code>ssdiff</code> is licensed under the terms of the General Public License (GPL), version 2 or 3. For information on this license look at the source code that came with the software or see the GNU project page &lt;URL: <a rel="nofollow" href="http://www.gnu.org">http://www.gnu.org</a> &gt;. </p>
<h2>COPYRIGHT</h2>
<p> The copyright on <code>ssdiff</code> and the <code>gnumeric</code> software and source code is held by the individual authors as is documented in the source code. </p>
<h2>AUTHOR</h2>
<p> <code>ssdiff</code>&#8216;s primary author is Morten Welinder &lt;terra [at] gnome.org&gt;; <code>ssdiff</code> builds on the <code>gnumeric</code> codebase. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gnumeric/">gnumeric</a></code>(1), <code><a href="/docs/linux/man/1-ssconvert/">ssconvert</a></code>(1), <code><a href="/docs/linux/man/1-ssindex/">ssindex</a></code>(1) <code><a href="/docs/linux/man/1-ssgrep/">ssgrep</a></code>(1) </p>
<p> The Gnumeric Homepage &lt;URL: <a rel="nofollow" href="http://www.gnome.org/projects/gnumeric/">http://www.gnome.org/projects/gnumeric/</a> &gt;. </p>
<p> The GNOME project page &lt;URL: <a rel="nofollow" href="http://www.gnome.org/">http://www.gnome.org/</a> &gt;. </p>
<h2>Index</h2>
