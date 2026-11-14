---
title: "gsql(1)"
name: "gsql"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gsql/"
description: "GSQL – an integrated database development environment for GNOME"
---

<h2>NAME</h2>
<p> GSQL &#8211; an integrated database development environment for <code>GNOME</code></p>
<h2>VERSION</h2>
<p> Current version is 0.2.1</p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>gsql </code><i>[options]</i></p>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>GSQL</code> is a gtk2-based modular development tool for various RDBMS, such as Oracle, MySQL, PostgreSQL and others </p>
<h2>OPTIONS</h2>
<p> The following options are provided by <code>GSQL</code> using the standard GNU command line syntax:</p>
<dl>
<dt><code>&#8211;enable-debug</code></p>
<dd> Print debugging messages to stdout. </p>
<dt><code>&#8211;enable-trace</code></p>
<dd> Print tracing messages to stdout. </p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print this help and exit. </p>
<dt><code>-v, &#8211;version</code></p>
<dd> Display the version information window. </p>
</dl>
<h2>ENGINES</h2>
<p> The <code>Engine</code> are <code>GSQL</code>&#8216;s shared library contains a set of functions to access specific database plus the GUI components performing access to the database objects. Engines can be enabled and configured from the <code>Preferences</code> window. See <a rel="nofollow" href="http://gsql.org/development/">http://gsql.org/development/</a> page for more information on developing engines. </p>
<h2>PLUGINS</h2>
<p> <code>GSQL</code> allows for dynamic loading of plugins to add extra functionality to <code>GSQL</code>. See <a rel="nofollow" href="http://gsql.org/development/">http://gsql.org/development/</a> page for more information on developing plugins. </p>
<h2>BUGS&#8217;n&#8217;PATCHES</h2>
<p> If you fix a bug in <code>GSQL</code> (or otherwise enhance it), please submit a patch (using <i>svn diff &gt; my.diff</i> against the latest SVN revision) at<br />
 <i><a rel="nofollow" href="http://code.google.com/p/gsql/issues/list">http://code.google.com/p/gsql/issues/list</a></i> </p>
<p> Before sending a bug report, please verify that you have the latest version of <code>GSQL</code>. Many bugs (major and minor) are fixed at each release, and if yours is out of date, the problem may already have been solved. </p>
<h2>SEE ALSO</h2>
<p> <i><a rel="nofollow" href="http://gsql.org/">http://gsql.org/</a></i><br />
 <i><a rel="nofollow" href="http://code.google.com/p/gsql/">http://code.google.com/p/gsql/</a></i> </p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <code>WITHOUT ANY WARRANTY</code>; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA </p>
<h2>AUTHORS</h2>
<p> <code>GSQL</code>&#8216;s active developers are: </p>
<p>&nbsp;<wbr>Taras Halturin&nbsp;<wbr>(lead developer)&nbsp;<wbr>&lt;<i>halturin [at] gmail.com</i>&gt; </p>
<p> This manpage was originally written by Taras Halturin. </p>
<h2>Index</h2>
