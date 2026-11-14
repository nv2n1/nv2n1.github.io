---
title: "pg_config(1)"
name: "pg_config"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pg_config/"
description: "pg_config – retrieve information about the installed version of PostgreSQL"
---

<h2 class="name">NAME</h2>
<p> pg_config &#8211; retrieve information about the installed version of PostgreSQL </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pg_config</code> [<i>option</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>The pg_config utility prints configuration parameters of the currently installed version of PostgreSQL. It is intended, for example, to be used by software packages that want to interface to PostgreSQL to facilitate finding the required header files and libraries.</p>
<h2>OPTIONS</h2>
<p> To use pg_config, supply one or more of the following options: </p>
<p> <code>&#8211;bindir</code></p>
<dl>
<dt>
<dd> Print the location of user executables. Use this, for example, to find the <code>psql</code> program. This is normally also the location where the pg_config program resides.</dl>
<p> <code>&#8211;docdir</code></p>
<dl>
<dt>
<dd> Print the location of documentation files.</dl>
<p> <code>&#8211;htmldir</code></p>
<dl>
<dt>
<dd> Print the location of HTML documentation files.</dl>
<p> <code>&#8211;includedir</code></p>
<dl>
<dt>
<dd> Print the location of C header files of the client interfaces.</dl>
<p> <code>&#8211;pkgincludedir</code></p>
<dl>
<dt>
<dd> Print the location of other C header files.</dl>
<p> <code>&#8211;includedir-server</code></p>
<dl>
<dt>
<dd> Print the location of C header files for server programming.</dl>
<p> <code>&#8211;libdir</code></p>
<dl>
<dt>
<dd> Print the location of object code libraries.</dl>
<p> <code>&#8211;pkglibdir</code></p>
<dl>
<dt>
<dd> Print the location of dynamically loadable modules, or where the server would search for them. (Other architecture-dependent data files might also be installed in this directory.)</dl>
<p> <code>&#8211;localedir</code></p>
<dl>
<dt>
<dd> Print the location of locale support files. (This will be an empty string if locale support was not configured when PostgreSQL was built.)</dl>
<p> <code>&#8211;mandir</code></p>
<dl>
<dt>
<dd> Print the location of manual pages.</dl>
<p> <code>&#8211;sharedir</code></p>
<dl>
<dt>
<dd> Print the location of architecture-independent support files.</dl>
<p> <code>&#8211;sysconfdir</code></p>
<dl>
<dt>
<dd> Print the location of system-wide configuration files.</dl>
<p> <code>&#8211;pgxs</code></p>
<dl>
<dt>
<dd> Print the location of extension makefiles.</dl>
<p> <code>&#8211;configure</code></p>
<dl>
<dt>
<dd> Print the options that were given to the configure script when PostgreSQL was configured for building. This can be used to reproduce the identical configuration, or to find out with what options a binary package was built. (Note however that binary packages often contain vendor-specific custom patches.) See also the examples below.</dl>
<p> <code>&#8211;cc</code></p>
<dl>
<dt>
<dd> Print the value of the <i>CC</i> variable that was used for building PostgreSQL. This shows the C compiler used.</dl>
<p> <code>&#8211;cppflags</code></p>
<dl>
<dt>
<dd> Print the value of the <i>CPPFLAGS</i> variable that was used for building PostgreSQL. This shows C compiler switches needed at preprocessing time (typically, -I switches).</dl>
<p> <code>&#8211;cflags</code></p>
<dl>
<dt>
<dd> Print the value of the <i>CFLAGS</i> variable that was used for building PostgreSQL. This shows C compiler switches.</dl>
<p> <code>&#8211;cflags_sl</code></p>
<dl>
<dt>
<dd> Print the value of the <i>CFLAGS_SL</i> variable that was used for building PostgreSQL. This shows extra C compiler switches used for building shared libraries.</dl>
<p> <code>&#8211;ldflags</code></p>
<dl>
<dt>
<dd> Print the value of the <i>LDFLAGS</i> variable that was used for building PostgreSQL. This shows linker switches.</dl>
<p> <code>&#8211;ldflags_ex</code></p>
<dl>
<dt>
<dd> Print the value of the <i>LDFLAGS_EX</i> variable that was used for building PostgreSQL. This shows linker switches used for building executables only.</dl>
<p> <code>&#8211;ldflags_sl</code></p>
<dl>
<dt>
<dd> Print the value of the <i>LDFLAGS_SL</i> variable that was used for building PostgreSQL. This shows linker switches used for building shared libraries only.</dl>
<p> <code>&#8211;libs</code></p>
<dl>
<dt>
<dd> Print the value of the <i>LIBS</i> variable that was used for building PostgreSQL. This normally contains -l switches for external libraries linked into PostgreSQL.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the version of PostgreSQL.</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about pg_config command line arguments, and exit.</dl>
<p> If more than one option is given, the information is printed in that order, one item per line. If no options are given, all available information is printed, with labels.</p>
<h2>NOTES</h2>
<p> The option <code>&#8211;includedir-server</code> was added in PostgreSQL 7.2. In prior releases, the server include files were installed in the same location as the client headers, which could be queried with the option <code>&#8211;includedir</code>. To make your package handle both cases, try the newer option first and test the exit status to see whether it succeeded. </p>
<p> The options <code>&#8211;docdir</code>, <code>&#8211;pkgincludedir</code>, <code>&#8211;localedir</code>, <code>&#8211;mandir</code>, <code>&#8211;sharedir</code>, <code>&#8211;sysconfdir</code>, <code>&#8211;cc</code>, <code>&#8211;cppflags</code>, <code>&#8211;cflags</code>, <code>&#8211;cflags_sl</code>, <code>&#8211;ldflags</code>, <code>&#8211;ldflags_sl</code>, and <code>&#8211;libs</code> were added in PostgreSQL 8.1. The option <code>&#8211;htmldir</code> was added in PostgreSQL 8.4. The option <code>&#8211;ldflags_ex</code> was added in PostgreSQL 9.0. </p>
<p> In releases prior to PostgreSQL 7.1, before <code>pg_config</code> came to be, a method for finding the equivalent configuration information did not exist.</p>
<h2>EXAMPLE</h2>
<p> To reproduce the build configuration of the current PostgreSQL installation, run the following command: </p>
<dl>
<dt>
<dd>
<pre>
eval ./configure `pg_config --configure`
</pre>
</dl>
<p> The output of pg_config &#8211;configure contains shell quotation marks so arguments with spaces are represented correctly. Therefore, using eval is required for proper results. </p>
<h2>Index</h2>
