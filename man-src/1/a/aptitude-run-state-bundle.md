---
title: "aptitude-run-state-bundle(1)"
name: "aptitude-run-state-bundle"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aptitude-run-state-bundle/"
description: "aptitude-run-state-bundle – unpack an aptitude state bundle and invoke aptitude on it"
---

<h2 class="name">NAME</h2>
<p> aptitude-run-state-bundle &#8211; unpack an aptitude state bundle and invoke aptitude on it </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>aptitude-run-state-bundle</code> [&lt;<i>options</i>&gt;&#8230;] &lt;<i>input-file</i>&gt; [&lt;<i>program</i>&gt;&nbsp;<wbr>[&lt;<i>arguments</i>&gt;&#8230;]]</dl>
<h2>DESCRIPTION</h2>
<p> <code>aptitude-run-state-bundle</code></p>
<dd>unpacks the given aptitude state bundle created by <code><a href="/docs/linux/man/1-aptitude-create-state-bundle/">aptitude-create-state-bundle</a></code>(1) to a temporary directory, invokes &lt;<i>program</i>&gt; on it with the supplied &lt;<i>arguments</i>&gt;, and removes the temporary directory afterwards. If &lt;<i>program</i>&gt; is not supplied, it defaults to <code><a href="/docs/linux/man/8-aptitude/">aptitude</a></code>(8).</p>
<h2>OPTIONS</h2>
<p> The following options may occur on the command-line before the input file. Options following the input file are presumed to be arguments to <code>aptitude</code>. </p>
<p> <code>&#8211;append-args</code></p>
<dl>
<dt>
<dd> Place the options that give the location of the state bundle at the end of the command line when invoking &lt;<i>program</i>&gt;, rather than at the beginning (the default is to place options at the beginning).</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display a brief usage summary.</dl>
<p> <code>&#8211;prepend-args</code></p>
<dl>
<dt>
<dd> Place the options that give the location of the state bundle at the beginning of the command line when invoking &lt;<i>program</i>&gt;, overriding any previous <code>&#8211;append-args</code> (the default is to place options at the beginning).</dl>
<p> <code>&#8211;no-clean</code></p>
<dl>
<dt>
<dd> Do not remove the unpacked state directory after running <code>aptitude</code>. You might want to use this if, for instance, you are debugging a problem that appears when <code>aptitude</code>&#8216;s state file is modified. When <code>aptitude</code> finishes running, the name of the state directory will be printed so that you can access it in the future. </p>
<p> This option is enabled automatically by <code>&#8211;statedir</code>.</dl>
<p> <code>&#8211;really-clean</code></p>
<dl>
<dt>
<dd> Delete the state directory after running <code>aptitude</code>, even if <code>&#8211;no-clean</code> or <code>&#8211;statedir</code> was supplied.</dl>
<p> <code>&#8211;statedir</code></p>
<dl>
<dt>
<dd> Instead of treating the input file as a state bundle, treat it as an unpacked state bundle. For instance, you can use this to access the state directory that was created by a prior run with <code>&#8211;no-clean</code>.</dl>
<p> <code>&#8211;unpack</code></p>
<dl>
<dt>
<dd> Unpack the input file to a temporary directory, but don&#8217;t actually run <code>aptitude</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-aptitude-create-state-bundle/">aptitude-create-state-bundle</a></code>(1), <code><a href="/docs/linux/man/8-aptitude/">aptitude</a></code>(8), <code><a href="/docs/linux/man/8-apt/">apt</a></code>(8)</p>
<h2>AUTHOR</h2>
<p> <code>Daniel Burrows</code> &lt;dburrows [at] debian.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright 2007 Daniel Burrows. </p>
<p> This manual page is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This manual page is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA. </p>
<h2>Index</h2>
