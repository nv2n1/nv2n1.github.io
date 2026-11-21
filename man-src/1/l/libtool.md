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
<dt><code>&#8211;config</code></dt>
<dd> show all configuration variables</dd>
<dt><code>&#8211;debug</code></dt>
<dd> enable verbose shell tracing</dd>
<dt><code>-n</code>, <code>&#8211;dry-run</code></dt>
<dd> display commands without modifying any files</dd>
<dt><code>&#8211;features</code></dt>
<dd> display basic configuration information and exit</dd>
<dt><code>&#8211;mode</code>=<i>MODE</i></dt>
<dd> use operation mode MODE</dd>
<dt><code>&#8211;preserve-dup-deps</code></dt>
<dd> don&#8217;t remove duplicate dependency libraries</dd>
<dt><code>&#8211;quiet</code>, <code>&#8211;silent</code></dt>
<dd> don&#8217;t print informational messages</dd>
<dt><code>&#8211;no-quiet</code>, <code>&#8211;no-silent</code></dt>
<dd> print informational messages (default)</dd>
<dt><code>&#8211;no-warn</code></dt>
<dd> don&#8217;t display warning messages</dd>
<dt><code>&#8211;tag</code>=<i>TAG</i></dt>
<dd> use configuration variables from tag TAG</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> print more informational messages than default</dd>
<dt><code>&#8211;no-verbose</code></dt>
<dd> don&#8217;t print the extra informational messages</dd>
<dt><code>&#8211;version</code></dt>
<dd> print version information</dd>
<dt><code>-h</code>, <code>&#8211;help</code>, <code>&#8211;help-all</code></dt>
<dd> print short, long, or detailed help message</dd></dl>
<p> MODE must be one of the following:</p>
<dl>
<dt>clean</dt>
<dd> remove files from the build directory</dd>
<dt>compile</dt>
<dd> compile a source file into a libtool object</dd>
<dt>execute</dt>
<dd> automatically set library path, then run a program</dd>
<dt>finish</dt>
<dd> complete the installation of libtool libraries</dd>
<dt>install</dt>
<dd> install libraries or executables</dd>
<dt>link</dt>
<dd> create a library or an executable</dd>
<dt>uninstall</dt>
<dd> remove libraries from an installed directory</dd></dl>
<p> MODE-ARGS vary depending on the MODE. When passed as first option, `&#8211;mode=MODE&#8217; may be abbreviated as `MODE&#8217; or a unique abbreviation of that. </p>
<p> GNU libtool home page: &lt;<a rel="nofollow" href="http://www.gnu.org/software/libtool/">http://www.gnu.org/software/libtool/</a>&gt;. General help using GNU software: &lt;<a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a>&gt;. </p>
<p> Description of compile mode: </p>
<p> Compile a source file into a libtool library object. </p>
<p> This mode accepts the following additional options:</p>
<dl>
<dt><code>-o</code> OUTPUT-FILE</dt>
<dd> set the output file name to OUTPUT-FILE</dd>
<dt><code>-no-suppress</code></dt>
<dd> do not suppress compiler output for multiple passes</dd>
<dt><code>-prefer-pic</code></dt>
<dd> try to build PIC objects only</dd>
<dt><code>-prefer-non-pic</code></dt>
<dd> try to build non-PIC objects only</dd>
<dt><code>-shared</code></dt>
<dd> do not build a `.o&#8217; file suitable for static linking</dd>
<dt><code>-static</code></dt>
<dd> only build a `.o&#8217; file suitable for static linking</dd>
<dt><code>-Wc</code>,FLAG</dt>
<dd> pass FLAG directly to the compiler</dd></dl>
<p> COMPILE-COMMAND is a command to be used in creating a `standard&#8217; object file from the given SOURCEFILE. </p>
<p> The output file name is determined by removing the directory component from SOURCEFILE, then substituting the C source code suffix `.c&#8217; with the library object suffix, `.lo&#8217;. </p>
<p> Description of link mode: </p>
<p> Link object files or libraries together to form another library, or to create an executable program. </p>
<p> LINK-COMMAND is a command using the C compiler that you would use to create a program from several object files. </p>
<p> The following components of LINK-COMMAND are treated specially:</p>
<dl>
<dt><code>-all-static</code></dt>
<dd> do not do any dynamic linking at all</dd>
<dt><code>-avoid-version</code></dt>
<dd> do not add a version suffix if possible</dd>
<dt><code>-bindir</code> BINDIR</dt>
<dd> specify path to binaries directory (for systems where libraries must be found in the PATH setting at runtime)</dd>
<dt><code>-dlopen</code> FILE</dt>
<dd> `-dlpreopen&#8217; FILE if it cannot be dlopened at runtime</dd>
<dt><code>-dlpreopen</code> FILE</dt>
<dd> link in FILE and add its symbols to lt_preloaded_symbols</dd>
<dt><code>-export-dynamic</code></dt>
<dd> allow symbols from OUTPUT-FILE to be resolved with <a href="/docs/linux/man/3-dlsym/">dlsym</a>(3)</dd>
<dt><code>-export-symbols</code> SYMFILE</dt>
<dd> try to export only the symbols listed in SYMFILE</dd>
<dt><code>-export-symbols-regex</code> REGEX</dt>
<dd> try to export only the symbols matching REGEX</dd>
<dt><code>-LLIBDIR</code></dt>
<dd> search LIBDIR for required installed libraries</dd>
<dt><code>-lNAME</code></dt>
<dd> OUTPUT-FILE requires the installed library libNAME</dd>
<dt><code>-module</code></dt>
<dd> build a library that can dlopened</dd>
<dt><code>-no-fast-install</code></dt>
<dd> disable the fast-install mode</dd>
<dt><code>-no-install</code></dt>
<dd> link a not-installable executable</dd>
<dt><code>-no-undefined</code></dt>
<dd> declare that a library does not refer to external symbols</dd>
<dt><code>-o</code> OUTPUT-FILE</dt>
<dd> create OUTPUT-FILE from the specified objects</dd>
<dt><code>-objectlist</code> FILE</dt>
<dd> Use a list of object files found in FILE to specify objects</dd>
<dt><code>-precious-files-regex</code> REGEX</dt>
<dd> don&#8217;t remove output files matching REGEX</dd>
<dt><code>-release</code> RELEASE</dt>
<dd> specify package release information</dd>
<dt><code>-rpath</code> LIBDIR</dt>
<dd> the created library will eventually be installed in LIBDIR</dd>
<dt><code>-R[</code> ]LIBDIR</dt>
<dd> add LIBDIR to the runtime path of programs and libraries</dd>
<dt><code>-shared</code></dt>
<dd> only do dynamic linking of libtool libraries</dd>
<dt><code>-shrext</code> SUFFIX</dt>
<dd> override the standard shared library file extension</dd>
<dt><code>-static</code></dt>
<dd> do not do any dynamic linking of uninstalled libtool libraries</dd>
<dt><code>-static-libtool-libs</code></dt>
<dd> do not do any dynamic linking of libtool libraries</dd>
<dt><code>-version-info</code> CURRENT[:REVISION[:AGE]]</dt>
<dd> specify library version info [each variable defaults to 0]</dd>
<dt><code>-weak</code> LIBNAME</dt>
<dd> declare that the target provides the LIBNAME interface</dd>
<dt> <code>-Wc</code>,FLAG</dt>
<dt><code>-Xcompiler</code> FLAG</dt>
<dd>
</dd><dd>pass linker-specific FLAG directly to the compiler</dd>
<dt> <code>-Wl</code>,FLAG</dt>
<dt><code>-Xlinker</code> FLAG</dt>
<dd>
</dd><dd>pass linker-specific FLAG directly to the linker</dd>
<dt><code>-XCClinker</code> FLAG</dt>
<dd> pass link-specific FLAG to the compiler driver (CC)</dd></dl>
<p> All other options (arguments beginning with `-&#8216;) are ignored. </p>
<p> Every other argument is treated as a filename. Files ending in `.la&#8217; are treated as uninstalled libtool libraries, other files are standard or library object files. </p>
<p> If the OUTPUT-FILE ends in `.la&#8217;, then a libtool library is created, only library objects (`.lo&#8217; files) may be specified, and `-rpath&#8217; is required, except when creating a convenience library. </p>
<p> If OUTPUT-FILE ends in `.a&#8217; or `.lib&#8217;, then a standard library is created using `ar&#8217; and `ranlib&#8217;, or on Windows using `lib&#8217;. </p>
<p> If OUTPUT-FILE ends in `.lo&#8217; or `.o&#8217;, then a reloadable object file is created, otherwise an executable program is created. </p>
<p> Description of execute mode: </p>
<p> Automatically set library path, then run a program. </p>
<p> This mode accepts the following additional options:</p>
<dl>
<dt><code>-dlopen</code> FILE</dt>
<dd> add the directory containing FILE to the library path</dd></dl>
<p> This mode sets the library path environment variable according to `-dlopen&#8217; flags. </p>
<p> If any of the ARGS are libtool executable wrappers, then they are translated into their corresponding uninstalled binary, and any of their required library directories are added to the library path. </p>
<p> Then, COMMAND is executed, with ARGS as arguments. </p>
<p> Description of install mode: </p>
<p> Install executables or libraries. </p>
<p> INSTALL-COMMAND is the installation command. The first component should be either the `install&#8217; or `cp&#8217; program. </p>
<p> The following components of INSTALL-COMMAND are treated specially:</p>
<dl>
<dt><code>-inst-prefix-dir</code> PREFIX-DIR</dt>
<dd> Use PREFIX-DIR as a staging area for installation</dd></dl>
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
<dt>host-triplet:</dt>
<dd> x86_64-apple-darwin11.2.0</dd>
<dt>shell:</dt>
<dd> /bin/sh</dd>
<dt>compiler:</dt>
<dd> gcc</dd>
<dt>compiler flags:</dt>
<dd> <code>-g</code> <code>-O2</code></dd>
<dt>linker:</dt>
<dd> /usr/llvm-gcc-4.2/libexec/gcc/i686-apple-darwin11/4.2.1/ld (gnu? no)</dd>
<dt>libtool:</dt>
<dd> (GNU libtool) 2.4.2</dd>
<dt>automake:</dt>
<dd> automake (GNU automake) 1.11.1</dd>
<dt>autoconf:</dt>
<dd> autoconf (GNU Autoconf) 2.68</dd></dl>
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
</dt><dd> <code>info libtool</code></dd></dl>
<p> should give you access to the complete manual. </p>
