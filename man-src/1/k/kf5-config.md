---
title: "kf5-config(1)"
name: "kf5-config"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kf5-config/"
description: "kf5-config – Prints Qt(TM) and Frameworks installation paths"
---

<h2>SYNOPSIS</h2>
<dl>
<dt> <code>kf5-config</code> [&#8211;expandvars] [&#8211;prefix] [&#8211;exec-prefix] [&#8211;libsuffix] [&#8211;localprefix] [&#8211;version] [&#8211;kde-version] [&#8211;types] [&#8211;path&nbsp;<wbr><i>type</i>] [&#8211;userpath&nbsp;<wbr><i>type</i>] [&#8211;install&nbsp;<wbr><i>type</i>] [&#8211;qt-prefix] [&#8211;qt-binaries] [&#8211;qt-libraries] [&#8211;qt-plugins]</dt></dl>
<h2>DESCRIPTION</h2>
<dd>kf5-config is a command line program used to retrieve information about Frameworks installation or user paths. </dd>
<p> Use this program to determine where the various aspects of the Frameworks installation reside on your system. </p>
<dl>
<dt>
</dt><dd>
 <font SIZE="+1"> <code>Note</code> </font> </dd>
<p> kf5-config is mostly a deprecated replacement for kde4-config, while the recommended tool to use instead is qtpaths (which is shipped with Qt(TM)). </p>
</dl>
<h2>OPTIONS</h2>
<p> <code>&#8211;expandvars</code></p>
<dl>
<dt>
</dt><dd> expand ${prefix} and ${exec_prefix} in output</dd></dl>
<p> <code>&#8211;prefix</code></p>
<dl>
<dt>
</dt><dd> Compiled in prefix for Frameworks libraries</dd></dl>
<p> <code>&#8211;exec-prefix</code></p>
<dl>
<dt>
</dt><dd> Compiled in exec_prefix for Frameworks libraries</dd></dl>
<p> <code>&#8211;libsuffix</code></p>
<dl>
<dt>
</dt><dd> Compiled in library path suffix</dd></dl>
<p> <code>&#8211;localprefix</code></p>
<dl>
<dt>
</dt><dd> Prefix in $<code>HOME</code> used to write files</dd></dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Version of Qt(TM) and compiled in version string for Frameworks libraries and kf5-config</dd></dl>
<p> <code>&#8211;kde-version</code></p>
<dl>
<dt>
</dt><dd> Compiled in version string for Frameworks libraries</dd></dl>
<p> <code>&#8211;types</code></p>
<dl>
<dt>
</dt><dd> Print a list of all available KDE resource types</dd></dl>
<p> <code>&#8211;path </code><i>type</i></p>
<dl>
<dt>
</dt><dd> Search path for the specified <i>type</i></dd></dl>
<p> <code>&#8211;userpath </code><i>type</i></p>
<dl>
<dt>
</dt><dd> User paths for the types: desktop|document</dd></dl>
<p> <code>&#8211;install </code><i>type</i></p>
<dl>
<dt>
</dt><dd> Prefix to install resource files to</dd></dl>
<p> <code>&#8211;qt-prefix</code></p>
<dl>
<dt>
</dt><dd> Installation prefix for Qt(TM)</dd></dl>
<p> <code>&#8211;qt-binaries</code></p>
<dl>
<dt>
</dt><dd> Location of installed Qt(TM) binaries</dd></dl>
<p> <code>&#8211;qt-libraries</code></p>
<dl>
<dt>
</dt><dd> Location of installed Qt(TM) libraries</dd></dl>
<p> <code>&#8211;qt-plugins</code></p>
<dl>
<dt>
</dt><dd> Location of installed Qt(TM) plugins</dd></dl>
<h2>EXAMPLES</h2>
<p> Print the top-level Frameworks installation directory: </p>
<p> %<code>kf5-config &#8211;prefix</code> </p>
<p> Print a list of all resource types: </p>
<p> %<code>kf5-config &#8211;types</code> </p>
<p> Print the installed wallpaper path: </p>
<p> %<code>kf5-config &#8211;path wallpaper</code></p>
<h2>SEE ALSO</h2>
<p> kf5options(7)</p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHOR</h2>
<p> <code>Stephan Kulow</code> &lt;coolo [at] kde.org&gt;</p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
