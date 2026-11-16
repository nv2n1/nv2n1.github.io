---
title: "root-config(1)"
name: "root-config"
section: "1"
letter: "r"
url: "/docs/linux/man/1-root-config/"
description: "root-config – ROOT utility for your Makefiles"
---

<h2 class="name">NAME</h2>
<p> root-config &#8211; ROOT utility for your Makefiles </p>
<h2>SYNOPSIS</h2>
<p> <code>root-config</code> <i>[options]</i></p>
<h2>DESCRIPTION</h2>
<p> Put lines like</p>
<dl>
<dt>
</dt><dd>
<pre>
CFLAGS = $(shell root-config --cflags)
LIBS   = $(shell root-config --libs)
GLIBS  = $(shell root-config --glibs)
%Cint.cxx:Include.h LinkDef.h
        rootcint -f $@ -c $^ 
</pre>
</dd></dl>
<p> in you Makefile. </p>
<p> You may also find the <i><a href="/docs/linux/man/1-automake/">automake</a></i>(1), <i><a href="/docs/linux/man/1-autoconf/">autoconf</a></i>(1), and <i><a href="/docs/linux/man/1-libtool/">libtool</a></i>(1) macro file <i>/usr/share/aclocal/root.m4</i> useful. If that macro file isn&#8217;t installed where Iaclocal will find it, copy the contents to your local <i>acinclude.m4</i> file. In the directories you use <code>ROOT</code> libraries, have in your <i>Makefile.am</i> file:</p>
<dl>
<dt>
</dt><dd>
<pre><code>
lib_LTLIBRARIES = libFoo.la
                      pkginclude_HEADERS = Foo.h
                                               noinst_HEADERS = FooCint.h
                                                                    libFoo_la_SOURCES = Foo.cxx FooCint.cxx
                                                                                            libFoo_la_LDFLAGS = -version - info 1 : 0 - R @ROOTLIBDIR @libFoo_la_LDADD = -lCore - lCint @ROOTAUXLIBS @BUILT_SOURCES = FooCint.cxx FooCint.h
                                                                                                                                                                                                                          AM_CPPFLAGS = -I[at] ROOTINCDIR @AM_LDFLAGS = -L[at] ROOTLIBDIR @CLEANFILES = *Cint.cxx * Cint.h * ~core % Cint.cxx % Cint.h : Include.h LinkDef.h @ROOTCINT @-f $ * Cint.cxx - c $(INCLUDES) $(AM_CPPFLAGS) $ ^
</code></pre>
</dd></dl>
<p> where you should substitute <code>Foo</code> with whatever, and list the appropriate source files in the <code>_SOURCES</code> variable. In you configure.in file, put:</p>
<dl>
<dt>
</dt><dd>
<pre>
AC_PROG_CC
AC_PROG_CXX
ROOT_PATH
AM_PROG_LIBTOOL
</pre>
</dd></dl>
<p> along with any other macros you may need. </p>
<p> Note that the <code>ROOT_PATH</code> macro takes three optional arguments: the minimal <code>ROOT</code> version to use, action if <code>ROOT</code> is found, and action if <code>ROOT</code> isn&#8217;t found. Some examples are</p>
<dl>
<dt>
</dt><dd>
<pre>
ROOT_PATH(3.03/05, , AC_MSG_ERROR(Your ROOT version is too old))
ROOT_PATH(, AC_DEFUN(HAVE_ROOT))
</pre>
</dd></dl>
<p> For example, if you want to compile some part of your source tree conditionally on wether <code>ROOT</code> is present or not, you can put in your <i>configure.in</i> file</p>
<dl>
<dt>
</dt><dd>
<pre>
ROOT_PATH(,
[
  AC_DEFUN(HAVE_ROOT)
  have_root=yes  
])
AM_CONDITIONAL(GOT_ROOT, test &quot;x$have_root&quot; = &quot;xyes&quot;)
</pre>
</dd></dl>
<p> And then in some <i>Makefile.am</i></p>
<dl>
<dt>
</dt><dd>
<pre>
EXTRA_SOURCES           = root_depenent_source.cc
if GOT_ROOT
LIBFOOXTRA              = root_depenent_source.cc
else
LIBFOOXTRA              =
endif
lib_LTLIBRARIES         = libFoo.la
libFoo_la_SOURCES       = Foo.cc  $(LIBFOOXTRA)
</pre>
</dd></dl>
<p> The full list of substitution variables are:</p>
<dl>
<dt><code>ROOTCONF</code></dt>
<dd> full path to <i>root-config</i></dd>
<dt><code>ROOTEXEC</code></dt>
<dd> full path to <i>root</i></dd>
<dt><code>ROOTCINT</code></dt>
<dd> full path to <i>rootcint</i></dd>
<dt><code>ROOTLIBDIR</code></dt>
<dd> Where the <code>ROOT</code> libraries are</dd>
<dt><code>ROOTINCDIR</code></dt>
<dd> Where the <code>ROOT</code> headers are</dd>
<dt><code>ROOTCFLAGS</code></dt>
<dd> Extra compiler flags</dd>
<dt><code>ROOTLIBS</code></dt>
<dd> <code>ROOT</code> basic libraries</dd>
<dt><code>ROOTGLIBS</code></dt>
<dd> <code>ROOT</code> basic + GUI libraries</dd>
<dt><code>ROOTAUXLIBS</code></dt>
<dd> Auxilary libraries and linker flags for <code>ROOT</code></dd>
<dt><code>ROOTAUXCFLAGS</code></dt>
<dd> Auxilary compiler flags</dd>
<dt><code>ROOTRPATH</code></dt>
<dd> Same as <code>ROOTLIBDIR</code></dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Gives a short list of options available, and exit</dd>
<dt><code>&#8211;version </code></dt>
<dd> Report the version number of installed <code>ROOT</code>, and exit.</dd>
<dt><code>&#8211;prefix</code><i>=&lt;prefix&gt;</i></dt>
<dd> If no arguments is given, reports where <code>ROOT</code> is installed. With an argument of =<i>&lt;prefix&gt;</i>, set the base of the subsequent options to <i>&lt;prefix&gt;</i>. If <code>\&#8211;exec-prefix</code> is passedwith an argument, that argument overrides the argument given to <code>\&#8211;prefix</code> for the library path.</dd>
<dt><code>&#8211;exec-prefix</code><i>=&lt;prefix&gt;</i></dt>
<dd> If no argument is given, report where the libraries are installed. If an argument is given, use that as the installation base directory for the libraries. This option does not affect the include path.</dd>
<dt><code>&#8211;libdir</code></dt>
<dd> Print the directory where the ROOT libraries are installed.</dd>
<dt><code>&#8211;incdir</code></dt>
<dd> Print the directory where the ROOT headers are installed.</dd>
<dt><code>&#8211;libs</code></dt>
<dd> Output a line suitable for linking a program agains the <code>ROOT</code> libraries. No graphics libraries are output.</dd>
<dt><code>&#8211;glibs</code></dt>
<dd> As above, but also output for the graphics libraries.</dd>
<dt><code>&#8211;cflags</code></dt>
<dd> Output a line suitable for compiling a source file againd the <code>ROOT</code> header (class declararion) files.</dd>
<dt><code>&#8211;new </code></dt>
<dd> Put the <code>libNew.so</code> library in the library lists. This option <i>must</i> be given before options <code>&#8211;libs</code> and <code>&#8211;glibs</code>.</dd>
<dt><code>&#8211;nonew </code></dt>
<dd> Compatiblity option. Does nothing.</dd>
<dt><code>&#8211;auxlibs</code></dt>
<dd> Print auxiliary libraries and/or system linker flags.</dd>
<dt><code>&#8211;noauxlibs</code></dt>
<dd> Do not print auxiliary libraries and/or system linker flags in the output of <code>&#8211;libs</code> and <code>&#8211;glibs</code>. <code>&#8211;auxcflags</code> Print auxiliary compiler flags.</dd>
<dt><code>&#8211;noauxcflags</code></dt>
<dd> Do not print auxiliary compiler flags in the output of <code>&#8211;cflags</code>.</dd>
<dt><code>&#8211;noldflags</code></dt>
<dd> Do not print library path link option in output of <code>&#8211;libs</code> and <code>&#8211;glibs</code>.</dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-root/">root</a></i>(1), <i>root-cint</i>(1) </p>
<p> See also the <code>ROOT</code> webpages: <i><a rel="nofollow" href="http://root.cern.ch">http://root.cern.ch</a></i></p>
<h2>ORIGINAL AUTHORS</h2>
<p> The ROOT team (see web page above):</p>
<dl>
<dt>
</dt><dd> <code>Rene Brun</code> and <code>Fons Rademakers</code></dd></dl>
<h2>COPYRIGHT</h2>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version. </p>
<p> This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Christian Holm Christensen &lt;cholm [at] nbi.dk&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
