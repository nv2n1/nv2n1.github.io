---
title: "rapt-file(1)"
name: "rapt-file"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rapt-file/"
description: "rapt-file – APT package searching utility — search remotely"
---

<h2 class="name">NAME</h2>
<p> rapt-file &#8211; APT package searching utility &#8212; search remotely </p>
<h2>SYNOPSIS</h2>
<p> <code>rapt-file</code> [ <code>options</code> ] [ <code>action</code> ] [ <code>pattern</code> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>rapt-file</code> is a command line tool for searching files in packages for the APT package management system. It differs from apt-file in that it works with remote package indices, so it doesn&#8217;t need to download full Contents files.</p>
<dl>
<dt><code>find</code></dt>
<dd> Alias for <code>search</code>.</dd>
<dt><code>list</code></dt>
<dd> List the contents of a package matching the <code>pattern</code> pattern. This action is very close to the <code>dpkg -L</code> command except the package does not need to be installed or fetched.</dd>
<dt><code>search</code></dt>
<dd> Search in which package a file is included. A list of all packages containing the <code>pattern</code> pattern is returned. </dd>
<p> rapt-file will only search for filenames, not directory names. This is due to the format of the Contents files it searches.</p>
<dt><code>show</code></dt>
<dd> Alias for <code>list</code>.</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code> -a, &#8211;architecture architecture </code></dt>
<dd> Sets architecture to architecture. This option is useful if you search a package for a different architecture from the one installed on your system. It determines how the $ARCH variable in sources.list is expanded (but it does not influence the search in any other way).</dd>
<dt><code> -l, &#8211;package-only </code></dt>
<dd> Only display package name; do not display file names.</dd>
<dt><code> -v, &#8211;verbose </code></dt>
<dd> Run <code>rapt-file</code> in verbose mode.</dd>
<dt><code> -h, &#8211;help </code></dt>
<dd> Display a short help screen.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/apt/sources.list</i></dt>
<dd> Locations to fetch package contents from.</dd>
<dt><i>/etc/apt/sources.list.d/</i></dt>
<dd> Directory with additional sources.list snippets</dd></dl>
<h2>AUTHOR</h2>
<p> <code>rapt-file</code> was written by Enrico Zini &lt;enrico [at] debian.org&gt;. </p>
