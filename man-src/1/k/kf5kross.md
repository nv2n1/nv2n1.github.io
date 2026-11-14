---
title: "kf5kross(1)"
name: "kf5kross"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kf5kross/"
description: "kf5kross – KDE application to run kross scripts."
---

<h2 class="name">NAME</h2>
<p> kf5kross &#8211; KDE application to run kross scripts. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>kf5kross</code> [-h, &#8211;help] [-v, &#8211;version] [&#8211;author] [&#8211;license] [file &#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>kf5kross</code></p>
<dd>executes kross scripts written in KDE Javascript, Python, Ruby, Java and Falcon. </p>
<p> This command line tool is used for any non-GUI scripts, e.g. Calligra Sheets has some of these.</p>
<h2>OPTIONS</h2>
<p> <code>-h</code><code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about options.</dl>
<p> <code>-v</code><code>&#8211;version</code></p>
<dl>
<dt>
<dd> Show version information</dl>
<p> <code>&#8211;author</code></p>
<dl>
<dt>
<dd> Show author information.</dl>
<p> <code>&#8211;license</code></p>
<dl>
<dt>
<dd> Show license information.</dl>
<p> <code>file</code>&#8230;</p>
<dl>
<dt>
<dd> The files with the scripts to run.</dl>
<h2>USAGE</h2>
<p> <code>kf5kross</code><i>file</i> runs the script in <i>file</i> after loading the interpreter plugin for the script language (detected by filename suffix). </p>
<p> To interpret other languages than KDE Javascript, <i>kdebindings</i> must be installed.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-kf5options/">kf5options</a></i>(7), <i><a href="/docs/linux/man/7-qt5options/">qt5options</a></i>(7), <i><a href="/docs/linux/man/1-python/">python</a></i>(1), <i><a href="/docs/linux/man/1-ruby/">ruby</a></i>(1), <i><a href="/docs/linux/man/1-kjs5/">kjs5</a></i>(1), <i><a href="/docs/linux/man/1-java/">java</a></i>(1), <i><a href="/docs/linux/man/1-falcon/">falcon</a></i>(1) </p>
<p> Look at <i><a rel="nofollow" href="http://kross.dipe.org/solution.html">http://kross.dipe.org/solution.html</a></i> for more information and tutorials.</p>
<h2>BUGS</h2>
<p> Please use m[blue]<code>KDE&#8217;s bugtracker</code>m[]<font SIZE="-2">[1]</font> to report bugs.</p>
<h2>AUTHOR</h2>
<p> <code>Sebastian Sauer</code> &lt;mail [at] dipe.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> KDE&#8217;s bugtracker</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://bugs.kde.org">http://bugs.kde.org</a></dl>
</dl>
<h2>Index</h2>
