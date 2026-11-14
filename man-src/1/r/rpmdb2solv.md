---
title: "rpmdb2solv(1)"
name: "rpmdb2solv"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpmdb2solv/"
description: "rpmdb2solv – convert the rpm database into a solv file"
---

<h2 class="name">NAME</h2>
<p> rpmdb2solv &#8211; convert the rpm database into a solv file </p>
<h2>SYNOPSIS</h2>
<p> <code>rpmdb2solv</code> [<i>OPTIONS</i>] [<i>REFFILE.solv</i>]</p>
<h2>DESCRIPTION</h2>
<p> The rpmdb2solv tool reads rpm&#8217;s installed packages database and writes it in solv file format to standard output. You can make use of an old version of the database by specifying a <i>REFFILE.solv</i> file. </p>
<p> <code>-o</code> <i>OUTFILE</i></p>
<dl>
<dt>
<dd> Write the generated solv to <i>OUTFILE</i> instead of standard output.</dl>
<p> <code>-P</code></p>
<dl>
<dt>
<dd> Print percentages as packages are being read in. The output format is like rpm&#8217;s &#8211;percent option.</dl>
<p> <code>-r</code> <i>ROOTDIR</i></p>
<dl>
<dt>
<dd> Use <i>ROOTDIR</i> as root directory.</dl>
<p> <code>-k</code></p>
<dl>
<dt>
<dd> Read pubkeys from the rpm database instead of installed packages. Note that many distributions stopped storing pubkeys in the database but use a directory like <code>/var/lib/rpm/pubkeys</code> instead.</dl>
<p> <code>-A</code></p>
<dl>
<dt>
<dd> Also scan the <code>/usr/share/appdata</code> for installed appdata files and create pseudo packages for each file.</dl>
<p> <code>-p</code> <i>PRODDIR</i></p>
<dl>
<dt>
<dd> Also read SUSE product files from directory <i>PRODDIR</i>. The standard directory is <code>/etc/products.d</code>.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> Do not read any packages from the rpm database. This is useful together with <code>-p</code> to only convert SUSE products.</dl>
<p> <code>-X</code></p>
<dl>
<dt>
<dd> Autoexpand SUSE pattern and product provides into packages.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-rpms2solv/">rpms2solv</a>(1)</p>
<h2>AUTHOR</h2>
<p> Michael Schroeder &lt;mls [at] suse.de&gt; </p>
<h2>Index</h2>
