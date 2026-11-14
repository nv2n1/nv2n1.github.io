---
title: "kbuildsycoca4(8)"
name: "kbuildsycoca4"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kbuildsycoca4/"
description: "kbuildsycoca4 – Rebuilds the system configuration cache."
---

<p>kbuildsycoca4 &#8211; Rebuilds the system configuration cache.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kbuildsycoca4</code> [[&#8211;nosignal] | [&#8211;noincremental] | [&#8211;checkstamps] | [&#8211;nocheckfiles] | [&#8211;global] | [&#8211;menutest] | [&#8211;track&nbsp;<wbr><i>menu-id</i>] | [&#8211;help] | [&#8211;help-qt] | [&#8211;help-kde] | [&#8211;help-all] | [&#8211;author] | [-v, &#8211;version] | [&#8211;license]]</dl>
<h2>Description</h2>
<p><code>kbuildsycoca4</code>, as part of the</p>
<dd>KDE command line tools ensures the proper operation of KDE by reading in all the .desktop, .xml, and .protocol files to construct a binary database. </p>
<p> KDE itself accesses this database during operation to provide configuration information a program needs to run. </p>
<p> This tool is part of ksycoca4, which stands for KDE System Configuration Cache</p>
<h2>Options</h2>
<p><code>&#8211;nosignal</code></p>
<dl>
<dd>Do not signal applications to update</dl>
<p> <code>&#8211;noincremental</code></p>
<dl>
<dd>Disable incremental update, re-read everything</dl>
<p> <code>&#8211;checkstamps</code></p>
<dl>
<dd>Check file timestamps</dl>
<p> <code>&#8211;nocheckfiles</code></p>
<dl>
<dd>Disable checking files (dangerous)</dl>
<p> <code>&#8211;global</code></p>
<dl>
<dd>Create global database</dl>
<p> <code>&#8211;menutest</code></p>
<dl>
<dd>Perform menu generation test run only</dl>
<p> <code>&#8211;track </code><i>menu-id</i></p>
<dl>
<dd>Track menu id for debug purposes</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dd>Show help about options</dl>
<p> <code>&#8211;help-qt</code></p>
<dl>
<dd>Show Qt specific options</dl>
<p> <code>&#8211;help-kde</code></p>
<dl>
<dd>Show KDE specific options</dl>
<p> <code>&#8211;help-all</code></p>
<dl>
<dd>Show all options</dl>
<p> <code>&#8211;author</code></p>
<dl>
<dd>Show author information</dl>
<p> <code>-v , &#8211;version</code></p>
<dl>
<dd>Show version information</dl>
<p> <code>&#8211;license</code></p>
<dl>
<dd>Show license information</dl>
<h2>Usage</h2>
<p>A standard way to run this program is by simply specifying the following command at the prompt <code>kbuildsycoca4</code></p>
<h2>Files</h2>
<p>/var/tmp/kde-$USER/ksycoca4</p>
<dl>
<dd>The default directory where the cache files are stored.</dl>
<h2>Environment Variables</h2>
<p>$<code>KDEDIRS</code></p>
<dl>
<dd>Specifies which directories are part of the KDE installations</dl>
<p> $<code>KDESYCOCA</code></p>
<dl>
<dd>Specifies the path to the sycoca database file</dl>
<h2>See Also</h2>
<p>kdeinit4</p>
<h2>Bugs</h2>
<p>There are probably tons of bugs. Use m[blue]<code>bugs.kde.org</code>m[]<font SIZE="-2">[1]</font> to report them.</p>
<h2>Author</h2>
<p><code>Darian Lanx</code> &lt;content [at] openprojects.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>bugs.kde.org</p>
<dl>
<dd><a rel="nofollow" href="http://bugs.kde.org">http://bugs.kde.org</a></dl>
