---
title: "g-ir-scanner(1)"
name: "g-ir-scanner"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g-ir-scanner/"
description: "g-ir-scanner – extracting C metadata from sources and headers"
---

<h2>NAME</h2>
<p> g-ir-scanner &#8211; extracting C metadata from sources and headers</p>
<h2>SYNOPSIS</h2>
<p> <code>g-ir-scanner</code> [OPTION&#8230;] FILES&#8230;</p>
<h2>DESCRIPTION</h2>
<p> g-ir-scanner is a tool which generates GIR XML files by parsing headers and introspecting GObject based libraries. It is usually invoked during the normal build step for a project and the information is saved to disk and later installed, so that language bindings and other applications can use it. Header files and source files are passed in as arguments on the command line. The suffix determines whether a file be treated as a source file (.c) or a header file (.h). Currently only C based libraries are supported by the scanner.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Show help options</p>
<dt><code>&#8211;quiet</code></p>
<dd> If passed, do not print details of normal operation.</p>
<dt><code>&#8211;warn-all</code></p>
<dd> Display warnings for public API which is not introspectable.</p>
<dt><code>&#8211;warn-error</code></p>
<dd> Make warnings be fatal errors.</p>
<dt><code>&#8211;format=FORMAT</code></p>
<dd> This parameters decides which the resulting format will be used. The default value is gir.</p>
<dt><code>&#8211;include=NAME</code></p>
<dd> Add the specified introspection dependency to the scanned namespace. NAME is of the form NAMESPACE-VERSION, like Gtk-3.0.</p>
<dt><code>&#8211;include-uninstalled=PATH</code></p>
<dd> Add the specified introspection dependency to the scanned namespace. This differs from &#8211;include in that it takes a file path, and does not process the pkg-config dependencies (since they may not be installed yet).</p>
<dt><code>&#8211;add-include-path=PATH</code></p>
<dd> Add a directory to the path which the scanner uses to find GIR files. Can be used multiple times to specify multiple directories</p>
<dt><code>-i, &#8211;library=LIBRARY</code></p>
<dd> Specifies a library that will be introspected. This means that the *_get_type() functions in it will be called for GObject data types. The name of the library should not contain the leading lib prefix nor the ending shared library suffix.</p>
<dt><code>-L, &#8211;library-path=PATH</code></p>
<dd> Include this directory when searching for a library. This option can be specified multiple times to include more than one directory to look for libraries in.</p>
<dt><code>-Idirectory</code></p>
<dd> Include this directory in the list of directories to be searched for header files. You need to pass to the scanner all the directories you&#8217;d normally pass to the compiler when using the specified source files.</p>
<dt><code>-n, &#8211;namespace=NAME</code></p>
<dd> The namespace name. This name should be capitalized, eg the first letter should be upper case. Examples: Gtk, Clutter, WebKit.</p>
<dt><code>&#8211;no-libtool</code></p>
<dd> Disable usage of libtool for compiling stub introspection binary. Use this if your build system does not require libtool.</p>
<dt><code>&#8211;libtool</code></p>
<dd> Full path to libtool executable. Typically used for Automake systems.</p>
<dt><code>&#8211;nsversion=VERSION</code></p>
<dd> The namespace version. For instance 1.0. This is usually the platform version, eg 2.0 for Gtk+, not 2.12.7.</p>
<dt><code>-p, &#8211;program=PROGRAM</code></p>
<dd> Specifies a binary that will be introspected. This means that the *_get_type() functions in it will be called for GObject data types. The binary must be modified to take a &#8211;introspect-dump= option, and to pass the argument to this function to g_irepository_dump.</p>
<dt><code>&#8211;program-arg=ARG</code></p>
<dd> Additional argument to pass to program for introspection.</p>
<dt><code>&#8211;identifier-prefix=PREFIX</code></p>
<dd> This option may be specified multiple times. Each one gives a prefix that will be stripped from all C identifiers. If none specified, the namespace will be used. Eg, an identifier prefix of <code>Foo</code> will export the identifier <code>typdef struct _FooBar FooBar;</code> as <code>Foo.Bar.</code></p>
<dt><code>&#8211;symbol-prefix=PREFIX</code></p>
<dd> This option may be specified multiple times. Each one gives a prefix that will be stripped from all C symbols. Eg, an symbol prefix of <code>foo</code> will export the symbol <code>foo_bar_do_something</code> as <code>Foo.Bar.do_something.</code></p>
<dt><code>&#8211;accept-unprefixed</code></p>
<dd> If specified, the scanner will accept identifiers and symbols which do not match the namespace prefix. Try to avoid using this if possible.</p>
<dt><code>&#8211;output=FILENAME</code></p>
<dd> Name of the file to output. Normally namespace + format extension. Eg, GLib-2.0.gir.</p>
<dt><code>&#8211;pkg=PACKAGE</code></p>
<dd> List of pkg-config packages to get compiler and linker flags from. This option can be specified multiple times to include flags from several pkg-config packages.</p>
<dt><code>&#8211;pkg-export=PACKAGE</code></p>
<dd> List of pkg-config packages that are provided by the generated gir. This option can be specified multiple times if the gir provides more packages. If not specified, the packages specified with &#8211;pkg= will be used.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Be verbose, include some debugging information.</p>
<dt></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dd> The g-ir-scanner uses the XDG_DATA_DIRS variable to check for dirs, the girs are located in XDG_DATA_DIRS/gir-1.0. It is normally set on a distribution so you shouldn&#8217;t need to set it yourself. </p>
<p> The variable GI_SCANNER_DISABLE_CACHE ensures that the scanner will not write cache data to $HOME.</p>
<h2>BUGS</h2>
<p> Report bugs at <a rel="nofollow" href="http://bugzilla.gnome.org/">http://bugzilla.gnome.org/</a> in the gobject-introspection product.</p>
<h2>HOMEPAGE and CONTACT</h2>
<p> <a rel="nofollow" href="http://live.gnome.org/GObjectIntrospection">http://live.gnome.org/GObjectIntrospection</a></p>
<h2>AUTHORS</h2>
<p> Johan Dahlin </p>
<h2>Index</h2>
