---
title: "engrampa(1)"
name: "engrampa"
section: "1"
letter: "e"
url: "/docs/linux/man/1-engrampa/"
description: "Engrampa – Archive Manager for MATE"
---

<h2 class="name">NAME</h2>
<p> Engrampa &#8211; Archive Manager for MATE </p>
<h2>SYNOPSIS</h2>
<p> <code>engrampa [OPTIONS&#8230;] [FILES&#8230;]</code></p>
<h2>DESCRIPTION</h2>
<p> Engrampa is the official archive manager for the MATE Desktop Environment, it is a graphical front-end to archiving utilities such as tar and zip. It is a fork of File Roller.</p>
<dl>
<dt>Engrampa supports most common operations such as creating, modifying and extracting files from an archive. You can also view the contents of an archive and open files contained within the archive.</dt>
<dd>
</dd><dt>This manual page briefly documents the <code>engrampa</code> command.</dt>
<dd>
</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>filename(s)&#8230;</code></dt>
<dd> Specifies the archive file to open when <code>engrampa</code> starts. If this is not specified, <code>engrampa</code> will start with a blank window and you may open an archive from the menu or by using the shortcut CTRL+O.</dd>
<dt><code>-a, &#8211;add-to=ARCHIVE</code></dt>
<dd> Add files to the specified archive and quit the program</dd>
<dt><code>-d, &#8211;add FILE</code></dt>
<dd> Add files asking the name of the archive and quit the program</dd>
<dt><code>-e, &#8211;extract-to=FOLDER</code></dt>
<dd> Extract archives to the specified folder and quit the program</dd>
<dt><code>-f, &#8211;extract</code></dt>
<dd> Extract archives asking the destination folder and quit the program</dd>
<dt><code>-h, &#8211;extract-here</code></dt>
<dd> Extract archives using the archive name as destination folder and quit the program</dd>
<dt><code>&#8211;default-dir=FOLDER</code></dt>
<dd> Default folder to use for the &#8216;&#8211;add&#8217; and &#8216;&#8211;extract&#8217; commands</dd>
<dt><code>&#8211;force</code></dt>
<dd> Create destination folder without asking confirmation</dd>
<dt><code>&#8211;display=DISPLAY</code></dt>
<dd> X display to use.</dd>
<dt><code>-?, &#8211;help</code></dt>
<dd> Print standard command line options.</dd>
<dt><code>&#8211;help-all</code></dt>
<dd> Print all command line options.</dd></dl>
<p> This program also accepts the standard GTK options. </p>
<h2>EXAMPLES</h2>
<p> <code>engrampa -h matelivecd.iso</code></p>
<dl>
<dt>
</dt><dd> Extract matelivecd.iso to ./matelivecd in the current working directory.</dd></dl>
<p> <code>engrampa ./matelivecd/* -a matelivecd.tar.gz</code></p>
<dl>
<dt>
</dt><dd> Create a new gzip compressed tarball archive named matelivecd.tar.gz, containing all the files located in the ./matelivecd directory.</dd></dl>
<p> <code>engrampa matelivecd.tar.gz</code></p>
<dl>
<dt>
</dt><dd> Open matelivecd.tar.gz to view and manipulate its contents. </dd>
</dl>
<h2>BUGS</h2>
<h3>Should you encounter any bugs, they may be reported at:</h3>
<p> <a rel="nofollow" href="http://github.com/mate-desktop/engrampa/issues">http://github.com/mate-desktop/engrampa/issues</a></p>
<h2>AUTHORS</h2>
<h3><code>Engrampa</code> is written by Paolo Bacchilega &lt;paolo.bacch [at] tin.it&gt; and Perberos &lt;perberos [at] gmail.com&gt;.</h3>
<h3>This Man Page has been updated/re-written for the MATE Desktop Environment by:</h3>
<pre><code>
Stefano Karapetsas&lt;stefano[at] karapetsas.com&gt;(2014)
    Adam Erdman&lt;hekel[at] archlinux.info&gt;(2014)
</code></pre>
<h2>HISTORY</h2>
<p> This manual page was originally written for the Debian Project by Sven Arvidsson &lt;sa [at] whiz.se&gt;, for File Roller. (2007)</p>
<h2>SEE ALSO</h2>
<h3>Engrampa documentation can be found from the Help menu, or by pressing the F1 key.</h3>
<p> Further information may also be available at: <a rel="nofollow" href="http://wiki.mate-desktop.org/docs">http://wiki.mate-desktop.org/docs</a> </p>
<h2>Index</h2>
<dt><a href="#lbAL">HISTORY</a></dt>
<dd>
</dd><dt><a href="#lbAM">SEE ALSO</a></dt>
<dd>
</dd></dl>
