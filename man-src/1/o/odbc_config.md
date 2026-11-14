---
title: "odbc_config(1)"
name: "odbc_config"
section: "1"
letter: "o"
url: "/docs/linux/man/1-odbc_config/"
description: "odbc_config – get compile options for compiling unixODBC client"
---

<h2 class="name">NAME</h2>
<p> odbc_config &#8211; get compile options for compiling unixODBC client</p>
<h2>SYNOPSIS</h2>
<p> [ <code>&#8211;prefix</code> ] [ <code>&#8211;exec-prefix</code> ] [ <code>&#8211;include-prefix</code> ] [ <code>&#8211;lib-prefix</code> ] [ <code>&#8211;bin-prefix</code> ] [ <code>&#8211;version</code> ] [ <code>&#8211;libs</code> ] [ <code>&#8211;static-libs</code> ] [ <code>&#8211;libtool-libs</code> ] [ <code>&#8211;cflags</code> ] [ <code>&#8211;odbcversion</code> ] [ <code>&#8211;odbcini</code> ] [ <code>&#8211;odbcinstini</code> ] [ <code>&#8211;header</code> ] [ <code>&#8211;ulen</code> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>odbc_config</code> provides built-in options, specified at build time of the unixODBC suite, which are useful for building unixODBC clients and similar programs. </p>
<h2>OPTIONS</h2>
<p> <code></p>
<dl>
<dt>&#8211;prefix</p>
<dd> </code> Prefix for architecture-independent file tree. </p>
<p> <code></p>
<dt>&#8211;exec-prefix</p>
<dd> </code> Prefix for architecture-dependent file tree. </p>
<p> <code></p>
<dt>&#8211;include-prefix</p>
<dd> </code> Directory with C header files for unixODBC. </p>
<p> <code></p>
<dt>&#8211;lib-prefix</p>
<dd> </code> Directory with object code (.so) libraries. </p>
<p> <code></p>
<dt>&#8211;bin-prefix</p>
<dd> </code> Location of user executables. </p>
<p> <code></p>
<dt>&#8211;version</p>
<dd> </code> unixODBC version. </p>
<p> <code></p>
<dt>&#8211;libs</p>
<dd> </code> Compiler flags for linking dynamic libraries. </p>
<p> <code></p>
<dt>&#8211;static-libs</p>
<dd> </code> Absolute file name of static unixODBC library. </p>
<p> <code></p>
<dt>&#8211;libtool-libs</p>
<dd> </code> Absolute file name of libtool unixODBC library. </p>
<p> <code></p>
<dt>&#8211;cflags</p>
<dd> </code> Compiler flags to find include files and critical compiler flags and defines used when compiling the libodbc library. </p>
<p> <code></p>
<dt>&#8211;odbcversion</p>
<dd> </code> Version of the ODBC specification used by the unixODBC. </p>
<p> <code></p>
<dt>&#8211;odbcini</p>
<dd> </code> Absolute file name of the system-wide DSN configuration file <i>odbc.ini</i>. </p>
<p> <code></p>
<dt>&#8211;odbcinstini</p>
<dd> </code> Absolute file name of the driver configuration file <i>odbcinst.ini</i>. </p>
<p> <code></p>
<dt>&#8211;header</p>
<dd> </code> Definitions of used C preprocessor constants. It is suitable to be piped into C header file. </p>
<p> <code></p>
<dt>&#8211;ulen</p>
<dd> </code> Compiler flag for defining <i>SIZEOF_SQLULEN</i>. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-odbcinst-ini/">odbcinst.ini</a></code>(5), <code><a href="/docs/linux/man/5-odbc-ini/">odbc.ini</a></code>(5) </p>
<h2>AUTHORS</h2>
<p> The authors of unixODBC are Peter Harvey and Nick Gorham For the full list of contributors see the <i>AUTHORS</i> file. </p>
<h2>COPYRIGHT</h2>
<p> unixODBC is licensed under the GNU Lesser General Public License. For details about the license, see the <i>COPYING</i> file. </p>
<h2>Index</h2>
