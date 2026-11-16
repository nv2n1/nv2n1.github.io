---
title: "xgfconfig(1)"
name: "xgfconfig"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xgfconfig/"
description: "xgfconfig – configuration program for Xgridfit"
---

<h2>NAME</h2>
<p> <code>xgfconfig</code> &#8211; configuration program for Xgridfit</p>
<h2>SYNOPSIS</h2>
<p> <code>xgfconfig [options]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>Xgfconfig</code> is a script that selects an XSLT processor and a RELAX NG validator for Xgridfit to invoke. If the program is run as root, the settings are global. If run as an ordinary user, settings are saved in ~/.xgridfit. Current settings are backed up in a file with extension .bak.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-c</dt>
<dd> Clear the current settings. If this is the only option, xgfconfig deletes the configuration file, restoring the default settings. If it is the first option on the command line, old settings are deleted before new ones are set.</dd>
<dt>-h</dt>
<dd> Display a help message and exit.</dd>
<dt>-j file</dt>
<dd> The full path to the jar file belonging to the XSLT processor selected with the -p option: use this if xgfconfig fails to find the right file by itself. The path must include the file name (e.g. ~/saxon/saxon9.jar). This option has no effect except when a Java-based XSLT processor is selected. To make xgfconfig try to find an appropriate jar file, pass the name of the processor (e.g. &quot;xalan-j&quot;).</dd>
<dt>-J file</dt>
<dd> The full path to a validator&#8217;s jar file. This works like the -j option.</dd>
<dt>-l</dt>
<dd> List processors and validators known to xgfconfig.</dd>
<dt>-p xsltproc | saxon-6 | saxon-9 | xalan-j | xalan-c | 4xslt</dt>
<dd> Select an XSLT processor for Xgridfit to use. For Java-based processors, this also tries to find the jar file.</dd>
<dt>-V xmllint | jing | msv | rnv | xmlstarlet</dt>
<dd> Select a validator for Xgridfit to use. Works like the -p option.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>utils/configure.xsl,</i></dt>
<dd> <i>utils/defaults.xml</i> </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fontforge/">fontforge</a></code>(1), <code><a href="/docs/linux/man/1-xgridfit/">xgridfit</a></code>(1), <code><a href="/docs/linux/man/1-ttx2xgf/">ttx2xgf</a></code>(1), <code><a href="/docs/linux/man/1-xgfupdate/">xgfupdate</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> <code>xgfconfig</code> was written by Peter Baker &lt;psb6m [at] virginia.edu&gt;. </p>
<p> This manual page was written by Peter Baker </p>
<h2>Index</h2>
