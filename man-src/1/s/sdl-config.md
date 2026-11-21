---

title: "sdl-config(1)"
name: "sdl-config"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sdl-config/"
description: "sdl-config – script to get information about the installed version of SDL"
---

<h2>NAME</h2>
<p> sdl-config &#8211; script to get information about the installed version of SDL</p>
<p> <code>sdl-config [~&#8211;prefix[=</code><i>DIR</i>]~] [~&#8211;exec-prefix[=<i>DIR</i>]~] [~&#8211;version~] [~&#8211;cflags~] [~&#8211;libs~] [~&#8211;static-libs~]</p>
<p> <code>sdl-config</code> is a tool that is used to configure and determine the compiler and linker flags that should be used to compile and link programs, and libraries, and plugins that use SDL. It is also used internally by the m4 macros that are included with SDL.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;cflags</code></dt>
<dd> Print the compiler flags that are necessary to compile a program or library that uses SDL.</dd>
<dt><code>&#8211;exec-prefix=</code><i>DIR</i></dt>
<dd> If specified, use <i>DIR</i> instead of the installation exec prefix that SDL was build with when computing the output for the &#8211;exec-prefix option. This option must be specified before any of the &#8211;cflags, and &#8211;libs options.</dd>
<dt><code>&#8211;libs</code></dt>
<dd> Print the linker flags that are necessary to link a program that uses SDL.</dd>
<dt><code>&#8211;prefix=</code><i>DIR</i></dt>
<dd> If specified, use DIR instead of the installation prefix that SDL was built with when computing the output for the &#8211;prefix, and &#8211;exec-prefix options. This option is also used for the exec prefix if &#8211;exec-prefix was not specified. This option must be specified before any of the &#8211;cflags, and &#8211;libs options.</dd>
<dt><code>&#8211;static-libs</code></dt>
<dd> Print the linker flags that are necessary to statically link a program that uses SDL.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Prints the currently installed version of SDL on standard output.</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>gcc -o main.o $(sdl-config &#8211;cflags) main.c</dt>
<dd> is how you might use <code>sdl-config</code> to compile a C source file for an executable program.</dd>
<dt>gcc -o my_app $(sdl-config &#8211;libs) main.o util.o</dt>
<dd> is how you might use <code>sdl-config</code> to link compiled objects into an executable program.</dd></dl>
<h2>AUTHOR</h2>
<p> The Simple DirectMedia Layer (SDL) library was written by Sam Lantinga. </p>
<p> This manual page was written by Branden Robinson, originally for Progeny Linux Systems, Inc., and the Debian Project. </p>
<p> This manual page was modified by Petr Pisar to match original SDL distribution. </p>
