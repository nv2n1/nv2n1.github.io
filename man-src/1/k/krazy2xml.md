---
title: "krazy2xml(1)"
name: "krazy2xml"
section: "1"
letter: "k"
url: "/docs/linux/man/1-krazy2xml/"
description: "krazy2xml – KDE source code checking for the English Breakfast Network (EBN)"
---

<h2 class="name">NAME</h2>
<p> krazy2xml &#8211; KDE source code checking for the English Breakfast Network (EBN) </p>
<h2>SYNOPSIS</h2>
<p> krazy2xml [options]</p>
<h2>DESCRIPTION</h2>
<p> krazy2xml is a big wrapper around <i><a href="/docs/linux/man/1-krazy/">krazy</a></i>(1) for no obvious use other than generating Code Checking Quality reports on the English Breakfast Network.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print help message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information and exit.</p>
<dt><code>&#8211;dry-run</code></p>
<dd> With this option the checker programs aren&#8217;t run; instead, the command line for each check that would be run is printed.</p>
<dt><code>&#8211;nodb</code></p>
<dd> Set this option to turn-off all database operations.</p>
<dt><code>&#8211;dbgen</code>=[id]</p>
<dd> Use the specified value for the database generationId. </p>
<p> The value is intended to be computed by the database being used and then passed into this program, rather than this program computing the value itself. </p>
<p> Do <font SIZE="-1"><code>NOT</code></font> use this option unless you know what you&#8217;re doing.</p>
<dt><code>&#8211;component</code>=[comp]</p>
<dd> Only run for the specified <font SIZE="-1">KDE</font> component. By default, the kde-4.x component is assumed.</p>
<dt><code>&#8211;module</code>=[mod1,&lt;mod2&gt;,&#8230;&lt;modN&gt;]</p>
<dd> Only run for the specified <font SIZE="-1">KDE</font> module within the component. By default all modules within the component are processed.</p>
<dt><code>&#8211;title</code>=title</p>
<dd> A title string to print onto each report page. If this option is not provided, a title for each page is generated that contains the source component, module and subdir.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Process all modules within component extragear</p>
<dd>
<pre>
 % krazy2xml --component=extragear
</pre>
<dt>Process module kdelibs within component kde-4.0</p>
<dd>
<pre>
 % krazy2xml --component=kde-4.0 --module=kdelibs
</pre>
</dl>
<h2>ENVIRONMENT</h2>
<p> <font SIZE="-1">KRAZY_PLUGIN_PATH</font> &#8211; this is a colon-separated list of paths which is searched when locating plugins. By default, plugins are searched for in the path <i></i>$TOP<i>/lib/krazy2/krazy-plugins:krazy-plugins</i>. </p>
<p> <font SIZE="-1">KRAZY_EXTRA_PATH</font> &#8211; this is a colon-separated list of paths which is searched when locating &#8220;extra&#8221; plugins. By default, the &#8220;extras&#8221; are searched for in the path <i></i>$TOP<i>/lib/krazy2/krazy-extras:krazy-extras</i>. </p>
<p> <font SIZE="-1">KRAZY_SET_PATH</font> &#8211; this is a colon-separated list of paths which is searched when locating checker sets. By default, the sets are searched for in the path <i></i>$TOP<i>/lib/krazy2/krazy-sets:krazy-sets</i>. </p>
<p> where <tt>$TOP</tt> is the top-level installation directory (eg. <i>/usr/local</i>, <i>/usr/local/Krazy2</i>)</p>
<h2>EXIT STATUS</h2>
<p> In normal operation, krazy2xml exits with status 0. </p>
<p> If a command line option was incorrectly provided, krazy2xml exits with status=1. </p>
<p> If krazy2 was envoked with the <code>&#8211;help</code> or <code>&#8211;version</code> options it will exit with status=0.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2005-2010 by Allen Winter &lt;winter [at] kde.org&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA</font> 02110-1301, <font SIZE="-1">USA</font>.</p>
<h2>FILES</h2>
<p> <i><a href="/docs/linux/man/5-krazyrc/">krazyrc</a></i>(5) files are processed in descending hierarchical order with each sublevel setting appending in a logical way to the previous level settings. The following files are read:<br />
&nbsp;<wbr><i>component/.krazy</i><br />
&nbsp;<wbr><i>component/module/.krazy</i><br />
&nbsp;<wbr><i>component/module/subdir/.krazy</i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-krazyrc/">krazyrc</a></i>(5), <i><a href="/docs/linux/man/1-krazy2/">krazy2</a></i>(1), <i><a href="/docs/linux/man/1-krazy2all/">krazy2all</a></i>(1)</p>
<h2>AUTHORS</h2>
<p> Allen Winter, &lt;winter [at] kde.org&gt; </p>
<h2>Index</h2>
