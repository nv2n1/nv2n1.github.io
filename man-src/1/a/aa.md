---
title: "aa(1)"
name: "aa"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aa/"
description: "aa, autoarchive – simple backup utility"
---

<h2>NAME</h2>
<p> aa, autoarchive &#8211; simple backup utility</p>
<h2>SYNOPSIS</h2>
<p> <code>aa/autoarchive</code> &nbsp;<wbr>[<i>options</i>] <i>AA_SPEC</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Simple backup utility. </p>
<p> <code>AutoArchive</code> is a simple python script for making backups more easily. It uses <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1) for creating archives. The idea of the program is that every information needed for making a backup is in one file &#8211; the <code>archive spec file</code> (<i>AA_SPEC</i>). Path to this file is passed as a parameter to &#8216;aa&#8217; command which reads informations from it and creates desired backup. </p>
<p> Command &#8216;autoarchive&#8217; is alias for &#8216;aa&#8217;; commands are equivalent.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show program&#8217;s version number and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Turns on verbose output.</p>
<dt><code>-a</code> ARCHIVER, <code>&#8211;archiver</code>=<i>ARCHIVER</i></p>
<dd> Specify archiver type. Supported types are: (&#8216;tar&#8217;, &#8216;targz&#8217;, &#8216;tarbz2&#8217;, &#8216;tarlzma&#8217;, &#8216;tarxz&#8217;) (default: tarbz2).</p>
<dt><code>-i</code>, <code>&#8211;incremental</code></p>
<dd> Perform incremental backup.</p>
<dt><code>-l</code> LEVEL, <code>&#8211;level</code>=<i>LEVEL</i></p>
<dd> Specify backup level which should be created. Informations about higher levels will be erased. If not present, creates next level in a row.</p>
<dt><code>-c</code> NUM, <code>&#8211;compression-level</code>=<i>NUM</i></p>
<dd> Compression level. If not specified, default behaviour of underlying compression program will be used.</dl>
<p> AA_SPEC is an archive spec file. It specifies what should be archived and the archive name. Its standard file name extension is &quot;.aa&quot;. For syntax please see README file. It is possible to specify multiple &quot;.aa&quot; files.</p>
<h2>EXAMPLES</h2>
<p> Let&#8217;s say that we want make a backup of configuration files of all users except user <i>foo</i>. Assume that our system has unix-like style of home directories (directory /home contains directories of all users; configuration files begins with dot). Name of this backup will be &#8216;users-config&#8217;. </p>
<p> First, create file users-config.aa (it doesn&#8217;t need to have same name as backup). </p>
<p>&nbsp;<wbr>&#8212;&#8211; content of file users-config.aa &#8212;&#8211; </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>AutoArchive file for users configuration files </p>
<p>&nbsp;<wbr>[General] </p>
<p>&nbsp;<wbr>name: users-config </p>
<p>&nbsp;<wbr>path:&nbsp;<wbr>/home </p>
<p>&nbsp;<wbr>include_files:&nbsp;<wbr>*/.* </p>
<p>&nbsp;<wbr>exclude_files: foo </p>
<p>&nbsp;<wbr>&#8212;&#8212;&#8212;- end of users-config.aa &#8212;&#8212;&#8212;- </p>
<p> Then to create the backup just type </p>
<p>&nbsp;<wbr>&nbsp;<wbr>aa users-config.aa </p>
<p> and in current directory will be created archive users-config.tar.bz2.</p>
<h2>FILES</h2>
<p> <i>~/.config/aa/snapshots/*.snar</i></p>
<dl>
<dt>
<dd> Files stores informations about incremental backup. They are created by <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1) archiver.</dl>
<h2>BUGS</h2>
<p> When creating incremental backup, files and directories specified in &#8216;include_files&#8217; are always added to archive, even if they did not changed. This is bug/feature of <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> Robert Cernansky &lt;openhs [at] users.sourceforge.net&gt; </p>
<p> Homepage: <a rel="nofollow" href="http://autoarchive.sourceforge.net/">http://autoarchive.sourceforge.net/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003 &#8211; 2010 Robert Cernansky<br />
 Copyright &#169; 2003 &#8211; 2010 HOME software </p>
<p> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License version 3 as published by the Free Software Foundation. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program. If not, see &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a>&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1), <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1), <code><a href="/docs/linux/man/1-lzma/">lzma</a></code>(1), <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1) </p>
<h2>Index</h2>
