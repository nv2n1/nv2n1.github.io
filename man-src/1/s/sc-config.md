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
</dt><dd> Print the installation prefix.
</dd><dt>--exec-prefix
</dt><dd> Print the executable installation prefix.
</dd><dt>--version
</dt><dd> Print the version number.
</dd><dt>--so-version
</dt><dd> Print the shared object version.
</dd><dt>--scdatadir
</dt><dd> Print the data installation directory.
</dd><dt>--buildid
</dt><dd> Print the build identifier.
</dd><dt>--cppflags
</dt><dd> Print the C preprocessor flags.
</dd><dt>--cflags
</dt><dd> Print the C flags.
</dd><dt>--cxxflags
</dt><dd> Print the C++ flags.
</dd><dt>--cc
</dt><dd> Print the C flags.
</dd><dt>--f77flags
</dt><dd> Print the FORTRAN 77 flags.
</dd><dt>--f77
</dt><dd> Print the FORTRAN 77 compiler.
</dd><dt>--cxx
</dt><dd> Print the C++ compiler.
</dd><dt>--libdir
</dt><dd> Print the library directories.
</dd><dt>--libs
</dt><dd> Print the libraries.
</dd><dt>--libtool
</dt><dd> Print the libtool executable.
</dd><dt>--ltlink
</dt><dd> Print the libtool link command.
</dd><dt>--ltlinklibopts
</dt><dd> Print the libtool library link options.
</dd><dt>--ltlinkbinopts
</dt><dd> Print the libtool binary link options.
</dd><dt>--ltcomp
</dt><dd> Print the libtool compile command.
</dd><dt>--ltinst
</dt><dd> Print the libtool install command.</dd></dl>
 

 

<h2>License</h2>

 

 

 sc-config is open-source software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

<h2>Warranty</h2>

 

 

 sc-config is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. 

<h2>Index</h2>


