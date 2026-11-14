---
title: "root(1)"
name: "root"
section: "1"
letter: "r"
url: "/docs/linux/man/1-root/"
description: "root – Interpretor of C++ for the ROOT framework"
---

<h2 class="name">NAME</h2>
<p> root &#8211; Interpretor of C++ for the ROOT framework </p>
<h2>SYNOPSIS</h2>
<p> <code>root</code> <i>[options] files &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>R</code>OOTs <code>O</code>bject-<code>O</code>riented <code>T</code>echnologies. </p>
<p> <code>root</code> is a interactive interpretor of C++ code. It uses the <code>ROOT</code> framework. For more information on <code>ROOT</code>, please refer to <i><a rel="nofollow" href="http://root.cern.ch">http://root.cern.ch</a></i>. </p>
<p> An extensive <i>Users Guide</i> is available from that site.</p>
<h2>OPTIONS</h2>
<p> <code>-?</code> Show summary of options.</p>
<dl>
<dt><code>-b</code></p>
<dd> Run in batch mode without graphics</p>
<dt><code>-e</code></p>
<dd> Execute the command passed between single quotes</p>
<dt><code>-n</code></p>
<dd> Do not execute logon and logoff macros as specified in <code>.rootrc</code></p>
<dt><code>-q</code></p>
<dd> Exit after processing command line macro files</p>
<dt><code>-l</code></p>
<dd> Do not show splash screen</dl>
<h2>SEE ALSO</h2>
<p> <font SIZE="-1"></font> <i><a href="/docs/linux/man/1-rootcling/">rootcling</a></i>(1), <i><a href="/docs/linux/man/1-cling/">cling</a></i>(1), <i><a href="/docs/linux/man/1-root-config/">root-config</a></i>(1), <i><a href="/docs/linux/man/1-rootd/">rootd</a></i>(1), <i><a href="/docs/linux/man/1-h2root/">h2root</a></i>(1), <i><a href="/docs/linux/man/1-g2root/">g2root</a></i>(1) </p>
<p> For extensive documentation on the <code>ROOT</code> system, see <i><a rel="nofollow" href="http://root.cern.ch">http://root.cern.ch</a></i> </p>
<p> A <code>Users Guide</code> is available online. </p>
<p> The classes of ROOT are all documented by the automatic documentation system, and is available online.</p>
<h2>FILES</h2>
<dl>
<dt>&lt;<i>etcdir</i>&gt;/<code>system.rootrc</code></p>
<dd> System-wide configuration file. &lt;<i>etcdir</i>&gt; either ROOTSYS, or something like <code>/etc/root</code></p>
<dt>&lt;<i>libdir</i>&gt;/*</p>
<dd> <code>ROOT</code> C++ class libraries. &lt;<i>libdir</i>&gt; is either ROOTSYS/lib or something like <code>/usr/lib/root</code>.</p>
<dt>&lt;<i>incdir</i>&gt;/*</p>
<dd> The header files for the <code>ROOT</code> C++ class libraries. &lt;<i>incdir</i>&gt; is either ROOTSYS/include or something like <code>/usr/include/root</code>.</p>
<dt><code>~/.rootrc</code>, <code>./.rootrc</code></p>
<dd> User configuration file</dl>
<h2>ORIGINAL AUTHORS</h2>
<p> The ROOT team (see web page above):</p>
<dl>
<dt>
<dd> <code>Rene Brun</code> and <code>Fons Rademakers</code></dl>
<h2>COPYRIGHT</h2>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version. </p>
<p> This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Christian Holm Christensen &lt;cholm [at] nbi.dk&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
