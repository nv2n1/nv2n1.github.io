---
title: "debconf-updatepo(1)"
name: "debconf-updatepo"
section: "1"
letter: "d"
url: "/docs/linux/man/1-debconf-updatepo/"
description: "debconf-updatepo – update PO files about debconf templates"
---

<h2 class="name">NAME</h2>
<p> debconf-updatepo &#8211; update PO files about debconf templates </p>
<h2>SYNOPSIS</h2>
<p> <code>debconf-updatepo</code> [<code>-v</code>] [<code>-h</code>] [<code>&#8211;podir=</code><font SIZE="-1">DIR</font>] [<code>&#8211;skip-pot</code>] [<code>&#8211;skip-merge</code>] [<code>&#8211;msgid-bugs-address=</code><font SIZE="-1">EMAIL</font>]</p>
<h2>DESCRIPTION</h2>
<p> This program reads <i>po/POTFILES.in</i> to determine which master files need to be processed, then extracts new gettext strings into <i>po/templates.pot</i> and updates all <i>po/*.po</i> files. This script can be called either in the top-level directory, or in the <i>debian</i> or <i>debian/po</i> subdirectories. It is run by developer and/or translator to update <font SIZE="-1">PO</font> files when the English text is modified in <i>templates</i> files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display a usage summary and exit.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Process in verbose mode.</p>
<dt><code>&#8211;podir=</code><font SIZE="-1">DIR</font></p>
<dd> Set directory for <font SIZE="-1">PO</font> files. By default <font SIZE="-1">PO</font> files are searched in <i>debian/po</i>, <i>po</i> and <i>../po</i> directories in that order.</p>
<dt><code>&#8211;skip-pot</code></p>
<dd> Do not generate a new <i>po/templates.pot</i> file.</p>
<dt><code>&#8211;skip-merge</code></p>
<dd> Do not merge existing <font SIZE="-1">PO</font> files with <i>po/templates.pot</i>.</p>
<dt><code>&#8211;msgid-bugs-address=</code><font SIZE="-1">EMAIL</font></p>
<dd> Set the email address that will be specified in the <font SIZE="-1">POT</font>&#8216;s Report-Msgid-Bugs-To field. </p>
<p> By default, this field is set to &lt;package&gt;@package.debian.org. </p>
<p> It is intended for the maintainers of Debian based distributions, and should be used in the following cases:</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> The package is not present in Debian (and thus the &lt;package&gt;@packages.debian.org address does not exist).</p>
<dt>o</p>
<dd> The maintainer made significant changes in the debconf templates (or added templates to a Debian package without templates), and does not want to bother the Debian maintainer with bug reports that won&#8217;t be relevant for the Debian maintainer.</dl>
</dl>
<dl>
<dt>
<dd>
<p> The default address is preferred to avoid corrections in the Debian based distribution without a notification to the Debian maintainer.</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-debconf-gettextize/">debconf-gettextize</a></code>(1), <code><a href="/docs/linux/man/1-po2debconf/">po2debconf</a></code>(1), <code><a href="/docs/linux/man/1-podebconf-report-po/">podebconf-report-po</a></code>(1), <code><a href="/docs/linux/man/7-po-debconf/">po-debconf</a></code>(7).</p>
<h2>AUTHOR</h2>
<pre>
  Denis Barbier &lt;barbier [at] linuxfr.org&gt;
</pre>
<h2>Index</h2>
