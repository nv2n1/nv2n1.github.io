---
title: "kpsetool(1)"
name: "kpsetool"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kpsetool/"
description: "kpsetool – script to make teTeX-style kpsetool, kpsexpand, and kpsepath available"
---

<h2>NAME</h2>
<p> kpsetool &#8211; script to make teTeX-style <code>kpsetool</code>, <code>kpsexpand</code>, and <code>kpsepath</code> available </p>
<h2>SYNOPSIS</h2>
<p> <code>kpsetool </code> [ <i>OPTIONS</i>&#8230; ] <i>COMMAND</i> </p>
<p> <code>kpsexpand</code> [ <i>OPTIONS</i>&#8230; ] <i>STRING</i> </p>
<p> <code>kpsepath</code> [ <i>OPTIONS</i>&#8230; ] <i>PATHTYPE</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>kpsetool</code> is a Bourne shell script that makes a teTeX-style <code>kpsetool</code>, <code>kpsexpand</code>, and <code>kpsepath</code> available. <code>kpsetool</code> uses <code>web2c</code>&#8216;s (new) <code>kpsexpand</code> binary, so the syntax for <code>kpsexpand</code> is incompatible with teTeX&#8217;s as of version 0.4. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-m</code> <i>mode</i></p>
<dd> set Metafont mode</p>
<dt><code>-n</code> <i>progname</i></p>
<dd> pretend to be <i>progname</i> to kpathsea</p>
<dt><code>-p</code></p>
<dd> act like <code><a href="/docs/linux/man/1-kpsepath/">kpsepath</a></code>(1)</p>
<dt><code>-v</code></p>
<dd> act like <code><a href="/docs/linux/man/1-kpsexpand/">kpsexpand</a></code>(1)</p>
<dt><code>-w</code></p>
<dd> act like <code><a href="/docs/linux/man/1-kpsewhich/">kpsewhich</a></code>(1)</dl>
<h2>USAGE</h2>
<p> <i>PATHTYPE</i> can be </p>
<dl>
<dt><code>base</code></p>
<dd> Metafont memory dump</p>
<dt><code>bib</code></p>
<dd> BibTeX bibliography source</p>
<dt><code>bst</code></p>
<dd> BibTeX style files</p>
<dt><code>cnf</code></p>
<dd> Kpathsea runtime configuration files</p>
<dt><code>dvips_config</code></p>
<dd> dvips config files</p>
<dt><code>dvips_header</code></p>
<dd> dvips header files</p>
<dt><code>fmt</code></p>
<dd> TeX memory dump</p>
<dt><code>gf</code></p>
<dd> generic font bitmap</p>
<dt><code>mem</code></p>
<dd> MetaPost memory dump</p>
<dt><code>mf</code></p>
<dd> Metafont source</p>
<dt><code>mfpool</code></p>
<dd> Metafont program strings</p>
<dt><code>mp</code></p>
<dd> MetaPost source</p>
<dt><code>mppool</code></p>
<dd> MetaPost program strings</p>
<dt><code>mpsupport</code></p>
<dd> MetaPost support files</p>
<dt><code>pict</code></p>
<dd> Other kinds of figures</p>
<dt><code>pk</code></p>
<dd> packed bitmap font</p>
<dt><code>tex</code></p>
<dd> TeX source</p>
<dt><code>texpool</code></p>
<dd> TeX program strings</p>
<dt><code>tfm</code></p>
<dd> TeX font metrics</p>
<dt><code>troff_font</code></p>
<dd> troff fonts</p>
<dt><code>vf</code></p>
<dd> virtual font</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kpsewhich/">kpsewhich</a></code>(1) </p>
<p> <i>Kpathsea: A library for path searching</i> (info or DVI file) </p>
<p> Web page: &lt;<a rel="nofollow" href="http://tug.org/teTeX/">http://tug.org/teTeX/</a>&gt; </p>
<h2>BUGS</h2>
<p> None known, but report any bugs found to &lt;tetex [at] dbs.uni-hannover.de&gt; (mailing list). </p>
<h2>AUTHOR</h2>
<p> <code>kpsetool</code> was written by Thomas Esser &lt;te [at] dbs.uni-hannover.de&gt; in March, 1997. <code>kpsetool</code> is in the public domain. </p>
<p> This manual page was written by C.M. Connelly &lt;c@eskimo.com&gt;, for the Debian GNU/Linux system. It may be used by other distributions without contacting the author. Any mistakes or omissions in the manual page are my fault; inquiries about or corrections to this manual page should be directed to me (and not to the primary author). </p>
<h2>Index</h2>
