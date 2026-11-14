---
title: "sc-config(1)"
name: "sc-config"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sc-config/"
---

<h2 class="name">NAME</h2>
 

 sc-config - The sc-config program is used to obtain information about MPQC's compile time environment.

<h2>Synopsis</h2>

 

 

 

 <pre><code>
sc - config
{
    --prefix, --exec - prefix, --version, --so - version, --scdatadir, --buildid, --cppflags, --cflags, --cxxflags, --cc, --f77flags, --f77, f-- cxx, --libdir, --libs, --libtool, --ltlink, --ltlinklibopts, --ltlinkbinopts, --ltcomp, --ltinst
}
</code></pre> 

 

<h2>Description</h2>

 

 

 The sc-config program is used to obtain information about MPQC's compile time environment. It can be used to initialize variables in a makefile that will be used to compile programs that depend on MPQC. For example, the following makefile could be used to compile a program myprog, which depends on the MPQC libraries. 

 

 <pre><code>
SCCONFIG = / usr / local / mpqc / current / bin / sc - config
                                                           CXX : = $(shell $(SCCONFIG)-- cxx)
                                                                     CXXFLAGS : = $(shell $(SCCONFIG)-- cxxflags)
                                                                                    CPPFLAGS : = $(shell $(SCCONFIG)-- cppflags)
                                                                                                   LIBS : = $(shell $(SCCONFIG)-- libs)
</code></pre> 

 

 

 <pre>
myprog: myprog.o
        $(CXX) $(CXXFLAGS) -o $@ $^ $(LIBS)
</pre> 

 

<h2>Running sc-config</h2>

 

 

 sc-config takes the following command line options: 

<dl>
<dt>--prefix
<dd> Print the installation prefix.
<dt>--exec-prefix
<dd> Print the executable installation prefix.
<dt>--version
<dd> Print the version number.
<dt>--so-version
<dd> Print the shared object version.
<dt>--scdatadir
<dd> Print the data installation directory.
<dt>--buildid
<dd> Print the build identifier.
<dt>--cppflags
<dd> Print the C preprocessor flags.
<dt>--cflags
<dd> Print the C flags.
<dt>--cxxflags
<dd> Print the C++ flags.
<dt>--cc
<dd> Print the C flags.
<dt>--f77flags
<dd> Print the FORTRAN 77 flags.
<dt>--f77
<dd> Print the FORTRAN 77 compiler.
<dt>--cxx
<dd> Print the C++ compiler.
<dt>--libdir
<dd> Print the library directories.
<dt>--libs
<dd> Print the libraries.
<dt>--libtool
<dd> Print the libtool executable.
<dt>--ltlink
<dd> Print the libtool link command.
<dt>--ltlinklibopts
<dd> Print the libtool library link options.
<dt>--ltlinkbinopts
<dd> Print the libtool binary link options.
<dt>--ltcomp
<dd> Print the libtool compile command.
<dt>--ltinst
<dd> Print the libtool install command.</dl>
 

 

<h2>License</h2>

 

 

 sc-config is open-source software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

<h2>Warranty</h2>

 

 

 sc-config is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. 

<h2>Index</h2>


