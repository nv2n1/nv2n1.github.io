---
title: "libtool(1)"
name: "libtool"
section: "1"
letter: "l"
url: "/docs/linux/man/1-libtool/"
description: "libtool – manual page for libtool 2.4.2"
---

<h2>NAME</h2>
<p> libtool &#8211; manual page for libtool 2.4.2</p>
<h2>SYNOPSIS</h2>
<p> <code>libtool</code> [<i>OPTION</i>]&#8230; [<i>MODE-ARG</i>]&#8230;<br />
 <code>libtool</code> [<i>OPTION</i>]&#8230; <i>&#8211;mode=compile COMPILE-COMMAND</i>&#8230; <i>SOURCEFILE</i><br />
 <code>libtool</code> [<i>OPTION</i>]&#8230; <i>&#8211;mode=link LINK-COMMAND</i>&#8230;<br />
 <code>libtool</code> [<i>OPTION</i>]&#8230; <i>&#8211;mode=execute COMMAND </i>[<i>ARGS</i>]&#8230;<br />
 <code>libtool</code> [<i>OPTION</i>]&#8230; <i>&#8211;mode=install INSTALL-COMMAND</i>&#8230;<br />
 <code>libtool</code> [<i>OPTION</i>]&#8230; <i>&#8211;mode=finish </i>[<i>LIBDIR</i>]&#8230;<br />
 <code>libtool</code> [<i>OPTION</i>]&#8230; <i>&#8211;mode=uninstall RM </i>[<i>RM-OPTION</i>]&#8230; <i>FILE</i>&#8230;<br />
 <code>libtool</code> [<i>OPTION</i>]&#8230; <i>&#8211;mode=clean RM </i>[<i>RM-OPTION</i>]&#8230; <i>FILE</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Provide generalized library-building support services.</p>
<dl>
<dt><code>&#8211;config</code></p>
<dd> show all configuration variables</p>
<dt><code>&#8211;debug</code></p>
<dd> enable verbose shell tracing</p>
<dt><code>-n</code>, <code>&#8211;dry-run</code></p>
<dd> display commands without modifying any files</p>
<dt><code>&#8211;features</code></p>
<dd> display basic configuration information and exit</p>
<dt><code>&#8211;mode</code>=<i>MODE</i></p>
<dd> use operation mode MODE</p>
<dt><code>&#8211;preserve-dup-deps</code></p>
<dd> don&#8217;t remove duplicate dependency libraries</p>
<dt><code>&#8211;quiet</code>, <code>&#8211;silent</code></p>
<dd> don&#8217;t print informational messages</p>
<dt><code>&#8211;no-quiet</code>, <code>&#8211;no-silent</code></p>
<dd> print informational messages (default)</p>
<dt><code>&#8211;no-warn</code></p>
<dd> don&#8217;t display warning messages</p>
<dt><code>&#8211;tag</code>=<i>TAG</i></p>
<dd> use configuration variables from tag TAG</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> print more informational messages than default</p>
<dt><code>&#8211;no-verbose</code></p>
<dd> don&#8217;t print the extra informational messages</p>
<dt><code>&#8211;version</code></p>
<dd> print version information</p>
<dt><code>-h</code>, <code>&#8211;help</code>, <code>&#8211;help-all</code></p>
<dd> print short, long, or detailed help message</dl>
<p> MODE must be one of the following:</p>
<dl>
<dt>clean</p>
<dd> remove files from the build directory</p>
<dt>compile</p>
<dd> compile a source file into a libtool object</p>
<dt>execute</p>
<dd> automatically set library path, then run a program</p>
<dt>finish</p>
<dd> complete the installation of libtool libraries</p>
<dt>install</p>
<dd> install libraries or executables</p>
<dt>link</p>
<dd> create a library or an executable</p>
<dt>uninstall</p>
<dd> remove libraries from an installed directory</dl>
<p> MODE-ARGS vary depending on the MODE. When passed as first option, `&#8211;mode=MODE&#8217; may be abbreviated as `MODE&#8217; or a unique abbreviation of that. </p>
<p> GNU libtool home page: &lt;<a rel="nofollow" href="http://www.gnu.org/software/libtool/">http://www.gnu.org/software/libtool/</a>&gt;. General help using GNU software: &lt;<a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a>&gt;. </p>
<p> Description of compile mode: </p>
<p> Compile a source file into a libtool library object. </p>
<p> This mode accepts the following additional options:</p>
<dl>
<dt><code>-o</code> OUTPUT-FILE</p>
<dd> set the output file name to OUTPUT-FILE</p>
<dt><code>-no-suppress</code></p>
<dd> do not suppress compiler output for multiple passes</p>
<dt><code>-prefer-pic</code></p>
<dd> try to build PIC objects only</p>
<dt><code>-prefer-non-pic</code></p>
<dd> try to build non-PIC objects only</p>
<dt><code>-shared</code></p>
<dd> do not build a `.o&#8217; file suitable for static linking</p>
<dt><code>-static</code></p>
<dd> only build a `.o&#8217; file suitable for static linking</p>
<dt><code>-Wc</code>,FLAG</p>
<dd> pass FLAG directly to the compiler</dl>
<p> COMPILE-COMMAND is a command to be used in creating a `standard&#8217; object file from the given SOURCEFILE. </p>
<p> The output file name is determined by removing the directory component from SOURCEFILE, then substituting the C source code suffix `.c&#8217; with the library object suffix, `.lo&#8217;. </p>
<p> Description of link mode: </p>
<p> Link object files or libraries together to form another library, or to create an executable program. </p>
<p> LINK-COMMAND is a command using the C compiler that you would use to create a program from several object files. </p>
<p> The following components of LINK-COMMAND are treated specially:</p>
<dl>
<dt><code>-all-static</code></p>
<dd> do not do any dynamic linking at all</p>
<dt><code>-avoid-version</code></p>
<dd> do not add a version suffix if possible</p>
<dt><code>-bindir</code> BINDIR</p>
<dd> specify path to binaries directory (for systems where libraries must be found in the PATH setting at runtime)</p>
<dt><code>-dlopen</code> FILE</p>
<dd> `-dlpreopen&#8217; FILE if it cannot be dlopened at runtime</p>
<dt><code>-dlpreopen</code> FILE</p>
<dd> link in FILE and add its symbols to lt_preloaded_symbols</p>
<dt><code>-export-dynamic</code></p>
<dd> allow symbols from OUTPUT-FILE to be resolved with <a href="/docs/linux/man/3-dlsym/">dlsym</a>(3)</p>
<dt><code>-export-symbols</code> SYMFILE</p>
<dd> try to export only the symbols listed in SYMFILE</p>
<dt><code>-export-symbols-regex</code> REGEX</p>
<dd> try to export only the symbols matching REGEX</p>
<dt><code>-LLIBDIR</code></p>
<dd> search LIBDIR for required installed libraries</p>
<dt><code>-lNAME</code></p>
<dd> OUTPUT-FILE requires the installed library libNAME</p>
<dt><code>-module</code></p>
<dd> build a library that can dlopened</p>
<dt><code>-no-fast-install</code></p>
<dd> disable the fast-install mode</p>
<dt><code>-no-install</code></p>
<dd> link a not-installable executable</p>
<dt><code>-no-undefined</code></p>
<dd> declare that a library does not refer to external symbols</p>
<dt><code>-o</code> OUTPUT-FILE</p>
<dd> create OUTPUT-FILE from the specified objects</p>
<dt><code>-objectlist</code> FILE</p>
<dd> Use a list of object files found in FILE to specify objects</p>
<dt><code>-precious-files-regex</code> REGEX</p>
<dd> don&#8217;t remove output files matching REGEX</p>
<dt><code>-release</code> RELEASE</p>
<dd> specify package release information</p>
<dt><code>-rpath</code> LIBDIR</p>
<dd> the created library will eventually be installed in LIBDIR</p>
<dt><code>-R[</code> ]LIBDIR</p>
<dd> add LIBDIR to the runtime path of programs and libraries</p>
<dt><code>-shared</code></p>
<dd> only do dynamic linking of libtool libraries</p>
<dt><code>-shrext</code> SUFFIX</p>
<dd> override the standard shared library file extension</p>
<dt><code>-static</code></p>
<dd> do not do any dynamic linking of uninstalled libtool libraries</p>
<dt><code>-static-libtool-libs</code></p>
<dd> do not do any dynamic linking of libtool libraries</p>
<dt><code>-version-info</code> CURRENT[:REVISION[:AGE]]</p>
<dd> specify library version info [each variable defaults to 0]</p>
<dt><code>-weak</code> LIBNAME</p>
<dd> declare that the target provides the LIBNAME interface</p>
<dt> <code>-Wc</code>,FLAG</p>
<dt><code>-Xcompiler</code> FLAG</p>
<dd>
<dd>pass linker-specific FLAG directly to the compiler</p>
<dt> <code>-Wl</code>,FLAG</p>
<dt><code>-Xlinker</code> FLAG</p>
<dd>
<dd>pass linker-specific FLAG directly to the linker</p>
<dt><code>-XCClinker</code> FLAG</p>
<dd> pass link-specific FLAG to the compiler driver (CC)</dl>
<p> All other options (arguments beginning with `-&#8216;) are ignored. </p>
<p> Every other argument is treated as a filename. Files ending in `.la&#8217; are treated as uninstalled libtool libraries, other files are standard or library object files. </p>
<p> If the OUTPUT-FILE ends in `.la&#8217;, then a libtool library is created, only library objects (`.lo&#8217; files) may be specified, and `-rpath&#8217; is required, except when creating a convenience library. </p>
<p> If OUTPUT-FILE ends in `.a&#8217; or `.lib&#8217;, then a standard library is created using `ar&#8217; and `ranlib&#8217;, or on Windows using `lib&#8217;. </p>
<p> If OUTPUT-FILE ends in `.lo&#8217; or `.o&#8217;, then a reloadable object file is created, otherwise an executable program is created. </p>
<p> Description of execute mode: </p>
<p> Automatically set library path, then run a program. </p>
<p> This mode accepts the following additional options:</p>
<dl>
<dt><code>-dlopen</code> FILE</p>
<dd> add the directory containing FILE to the library path</dl>
<p> This mode sets the library path environment variable according to `-dlopen&#8217; flags. </p>
<p> If any of the ARGS are libtool executable wrappers, then they are translated into their corresponding uninstalled binary, and any of their required library directories are added to the library path. </p>
<p> Then, COMMAND is executed, with ARGS as arguments. </p>
<p> Description of install mode: </p>
<p> Install executables or libraries. </p>
<p> INSTALL-COMMAND is the installation command. The first component should be either the `install&#8217; or `cp&#8217; program. </p>
<p> The following components of INSTALL-COMMAND are treated specially:</p>
<dl>
<dt><code>-inst-prefix-dir</code> PREFIX-DIR</p>
<dd> Use PREFIX-DIR as a staging area for installation</dl>
<p> The rest of the components are interpreted as arguments to that command (only BSD-compatible install options are recognized). </p>
<p> Description of finish mode: </p>
<p> Complete the installation of libtool libraries. </p>
<p> Each LIBDIR is a directory that contains libtool libraries. </p>
<p> The commands that this mode executes may require superuser privileges. Use the `&#8211;dry-run&#8217; option if you just want to see what would be executed. </p>
<p> Description of uninstall mode: </p>
<p> Remove libraries from an installation directory. </p>
<p> RM is the name of the program to use to delete files associated with each FILE (typically `/bin/rm&#8217;). RM-OPTIONS are options (such as `-f&#8217;) to be passed to RM. </p>
<p> If FILE is a libtool library, all the files associated with it are deleted. Otherwise, only FILE itself is deleted using RM. </p>
<p> Description of clean mode: </p>
<p> Remove files from the build directory. </p>
<p> RM is the name of the program to use to delete files associated with each FILE (typically `/bin/rm&#8217;). RM-OPTIONS are options (such as `-f&#8217;) to be passed to RM. </p>
<p> If FILE is a libtool library, object or program, all the files associated with it are deleted. Otherwise, only FILE itself is deleted using RM. </p>
<p> When reporting a bug, please describe a test case to reproduce it and include the following information:</p>
<dl>
<dt>host-triplet:</p>
<dd> x86_64-apple-darwin11.2.0</p>
<dt>shell:</p>
<dd> /bin/sh</p>
<dt>compiler:</p>
<dd> gcc</p>
<dt>compiler flags:</p>
<dd> <code>-g</code> <code>-O2</code></p>
<dt>linker:</p>
<dd> /usr/llvm-gcc-4.2/libexec/gcc/i686-apple-darwin11/4.2.1/ld (gnu? no)</p>
<dt>libtool:</p>
<dd> (GNU libtool) 2.4.2</p>
<dt>automake:</p>
<dd> automake (GNU automake) 1.11.1</p>
<dt>autoconf:</p>
<dd> autoconf (GNU Autoconf) 2.68</dl>
<h2>AUTHOR</h2>
<p> Written by Gordon Matzigkeit &lt;gord [at] gnu.ai.mit.edu&gt;, 1996</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-libtool [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2011 Free Software Foundation, Inc.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>libtool</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>libtool</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info libtool</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
