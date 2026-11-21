---

title: "sc-libtool(1)"
name: "sc-libtool"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sc-libtool/"
---

sc-libtool - The sc-libtool program is used to link and build MPQC executables and libraries.

<h2>Synopsis</h2>

 

 

 

 <pre><code>
sc - libtool[--config][--debug][{-n, --dry - run}][--features][--finish][--help][--mode = {clean, compile, finish, install, link, uninstall}][{--quiet, --silent}][--tag = TAG][--version] MODE - ARGS
</code></pre> 

 

<h2>Description</h2>

 

 

 The sc-libtool command provides generalized library-building support services. sc-libtool accepts the following options: 

<dl>
<dt>--config
</dt><dd> Show all configuration variables.
</dd><dt>--debug
</dt><dd> Enable verbose shell tracing.
</dd><dt>-n, --dry-run
</dt><dd> Display commands without modifying any files.
</dd><dt>--features
</dt><dd> Display basic configuration information and exit.
</dd><dt>--finish
</dt><dd> Same as --mode=finish.
</dd><dt>--help
</dt><dd> Display help message and exit
</dd><dt>--mode=<i>MODE</i>
</dt><dd> Use operation mode <i>MODE</i> (default=inferred from <i>MODE-ARGS</i>).
</dd><dt>--quiet
</dt><dd> Same as --silent.
</dd><dt>--silent
</dt><dd> Don't print informational messages.
</dd><dt>--tag=<i>TAG</i>
</dt><dd> Use configuration variables from tag <i>TAG</i>.
</dd><dt>--version
</dt><dd> Print version information.</dd></dl>
 

 

 <i>MODE</i> must be one of the following: 

<dl>
<dt>clean
</dt><dd> Remove files from the build directory.
</dd><dt>compile
</dt><dd> Compile a source file into a libtool object.
</dd><dt>execute
</dt><dd> Automatically set library path, then run a program.
</dd><dt>finish
</dt><dd> Complete the installation of libtool libraries.
</dd><dt>install
</dt><dd> Install libraries or executables.
</dd><dt>link
</dt><dd> Create a library or an executable.
</dd><dt>uninstall
</dt><dd> Remove libraries from an installed directory.</dd></dl>
 

 

<h2>License</h2>

 

 

 sc-libtool is open-source software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

<h2>Warranty</h2>

 

 

 sc-libtool is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
