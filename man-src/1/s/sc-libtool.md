---
title: "sc-libtool(1)"
name: "sc-libtool"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sc-libtool/"
---

<h2 class="name">NAME</h2>
 

 sc-libtool - The sc-libtool program is used to link and build MPQC executables and libraries.

<h2>Synopsis</h2>

 

 

 

 <pre><code>
sc - libtool[--config][--debug][{-n, --dry - run}][--features][--finish][--help][--mode = {clean, compile, finish, install, link, uninstall}][{--quiet, --silent}][--tag = TAG][--version] MODE - ARGS
</code></pre> 

 

<h2>Description</h2>

 

 

 The sc-libtool command provides generalized library-building support services. sc-libtool accepts the following options: 

<dl>
<dt>--config
<dd> Show all configuration variables.
<dt>--debug
<dd> Enable verbose shell tracing.
<dt>-n, --dry-run
<dd> Display commands without modifying any files.
<dt>--features
<dd> Display basic configuration information and exit.
<dt>--finish
<dd> Same as --mode=finish.
<dt>--help
<dd> Display help message and exit
<dt>--mode=<i>MODE</i>
<dd> Use operation mode <i>MODE</i> (default=inferred from <i>MODE-ARGS</i>).
<dt>--quiet
<dd> Same as --silent.
<dt>--silent
<dd> Don't print informational messages.
<dt>--tag=<i>TAG</i>
<dd> Use configuration variables from tag <i>TAG</i>.
<dt>--version
<dd> Print version information.</dl>
 

 

 <i>MODE</i> must be one of the following: 

<dl>
<dt>clean
<dd> Remove files from the build directory.
<dt>compile
<dd> Compile a source file into a libtool object.
<dt>execute
<dd> Automatically set library path, then run a program.
<dt>finish
<dd> Complete the installation of libtool libraries.
<dt>install
<dd> Install libraries or executables.
<dt>link
<dd> Create a library or an executable.
<dt>uninstall
<dd> Remove libraries from an installed directory.</dl>
 

 

<h2>License</h2>

 

 

 sc-libtool is open-source software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

<h2>Warranty</h2>

 

 

 sc-libtool is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. 

<h2>Index</h2>


