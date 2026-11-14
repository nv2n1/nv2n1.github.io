---
title: "licensecheck(1)"
name: "licensecheck"
section: "1"
letter: "l"
url: "/docs/linux/man/1-licensecheck/"
description: "licensecheck – simple license checker for source files"
---

<h2 class="name">NAME</h2>
<p> licensecheck &#8211; simple license checker for source files </p>
<h2>SYNOPSIS</h2>
<p> <code>licensecheck</code> <code>&#8211;help</code>|<code>&#8211;version</code> </p>
<p> <code>licensecheck</code> [<code>&#8211;no-conf</code>] [<code>&#8211;verbose</code>] [<code>&#8211;copyright</code>] [<code>-l</code>|<code>&#8211;lines=</code><i>N</i>] [<code>-i</code>|<code>&#8211;ignore=</code><i>regex</i>] [<code>-c</code>|<code>&#8211;check=</code><i>regex</i>] [<code>-m</code>|<code>&#8211;machine</code>] [<code>-r</code>|<code>&#8211;recursive</code>] <i>list of files and directories to check</i></p>
<h2>DESCRIPTION</h2>
<p> <code>licensecheck</code> attempts to determine the license that applies to each file passed to it, by searching the start of the file for text belonging to various licenses. </p>
<p> If any of the arguments passed are directories, <code>licensecheck</code> will add the files contained within to the list of files to process.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;verbose</code>, <code>&#8211;no-verbose</code></p>
<dd> Specify whether to output the text being processed from each file before the corresponding license information. </p>
<p> Default is to be quiet.</p>
<dt><code>-l=</code><i>N</i>, <code>&#8211;lines=</code><i>N</i></p>
<dd> Specify the number of lines of each file&#8217;s header which should be parsed for license information. (Default is 60).</p>
<dt><code>-i=</code><i>regex</i>, <code>&#8211;ignore=</code><i>regex</i></p>
<dd> When processing the list of files and directories, the regular expression specified by this option will be used to indicate those which should not be considered (e.g. backup files, <font SIZE="-1">VCS</font> metadata).</p>
<dt><code>-r</code>, <code>&#8211;recursive</code></p>
<dd> Specify that the contents of directories should be added recursively.</p>
<dt><code>-c=</code><i>regex</i>, <code>&#8211;check=</code><i>regex</i></p>
<dd> Specify a pattern against which filenames will be matched in order to decide which files to check the license of. </p>
<p> The default includes common source files.</p>
<dt><code>&#8211;copyright</code></p>
<dd> Also display copyright text found within the file</p>
<dt><code>-m</code>, <code>&#8211;machine</code></p>
<dd> Display the information in a machine readable way, i.e. in the form &lt;file&gt;&lt;tab&gt;&lt;license&gt;[&lt;tab&gt;&lt;copyright&gt;] so that it can be easily sorted and/or filtered, e.g. with the <code>awk</code> and <code>sort</code> commands. Note that using the <code>&#8211;verbose</code> option will kill the readability.</p>
<dt><code>&#8211;no-conf</code>, <code>&#8211;noconf</code></p>
<dd> Do not read any configuration files. This can only be used as the first option given on the command-line.</dl>
<h2>CONFIGURATION VARIABLES</h2>
<p> The two configuration files <i>/etc/rpmdevtools/devscripts.conf</i> and <i>~/.devscripts</i> are sourced by a shell in that order to set configuration variables. Command line options can be used to override configuration file settings. Environment variable settings are ignored for this purpose. The currently recognised variables are:</p>
<dl>
<dt><font SIZE="-1"><code>LICENSECHECK_VERBOSE</code></font></p>
<dd> If this is set to <i>yes</i>, then it is the same as the <code>&#8211;verbose</code> command line parameter being used. The default is <i>no</i>.</p>
<dt><font SIZE="-1"><code>LICENSECHECK_PARSELINES</code></font></p>
<dd> If this is set to a positive number then the specified number of lines at the start of each file will be read whilst attempting to determine the license(s) in use. This is equivalent to the <code>&#8211;lines</code> command line option.</dl>
<h2>LICENSE</h2>
<p> This code is copyright by Adam D. Barratt &lt;<i>adam [at] adam-barratt.org.uk</i>&gt;, all rights reserved; based on a script of the same name from the <font SIZE="-1">KDE SDK,</font> which is copyright by &lt;<i>dfaure [at] kde.org</i>&gt;. This program comes with <font SIZE="-1">ABSOLUTELY NO WARRANTY.</font> You are free to redistribute this code under the terms of the <font SIZE="-1">GNU</font> General Public License, version 2 or later.</p>
<h2>AUTHOR</h2>
<p> Adam D. Barratt &lt;adam [at] adam-barratt.org.uk&gt; </p>
<h2>Index</h2>
