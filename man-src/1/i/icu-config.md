---
title: "icu-config(1)"
name: "icu-config"
section: "1"
letter: "i"
url: "/docs/linux/man/1-icu-config/"
description: "icu-config – output ICU build options"
---

<h2 class="name">NAME</h2>
<p> <code>icu-config</code> &#8211; output ICU build options </p>
<h2>SYNOPSIS</h2>
<p> <code>icu-config</code> [ <code>&#8211;bindir</code> ] [ <code>&#8211;cc</code> ] [ <code>&#8211;cflags</code> ] [ <code>&#8211;cppflags</code> ] [ <code>&#8211;cppflags-searchpath</code> ] [ <code>&#8211;cxx</code> ] [ <code>&#8211;cxxflags</code> ] [ <code>&#8211;detect-prefix</code> ] [ <code>&#8211;exec-prefix</code> ] [ <code>&#8211;exists</code> ] [ <code>&#8211;help</code>, <code>-?</code>, <code>&#8211;usage</code> ] [ <code>&#8211;icudata</code> ] [ <code>&#8211;icudata-install-dir</code> ] [ <code>&#8211;icudata-mode</code> ] [ <code>&#8211;icudatadir</code> ] [ <code>&#8211;invoke</code> ] [ <code>&#8211;invoke=</code><i>prog</i> ] [ <code>&#8211;ldflags</code> ] [ <code>&#8211;ldflags-layout</code> ] [ <code>&#8211;ldflags-libsonly</code> ] [ <code>&#8211;ldflags-searchpath</code> ] [ <code>&#8211;ldflags-system</code> ] [ <code>&#8211;ldflags-icuio</code> ] [ <code>&#8211;mandir</code> ] [ <code>&#8211;prefix</code> ] [ <code>&#8211;prefix=</code><i>prefix</i> ] [ <code>&#8211;sbindir</code> ] [ <code>&#8211;shared-datadir</code> ] [ <code>&#8211;sysconfdir</code> ] [ <code>&#8211;unicode-version</code> ] [ <code>&#8211;version</code> ] [ <code>&#8211;incfile</code> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>icu-config</code> simplifies the task of building and linking against ICU as compared to manually configuring user makefiles or equivalent. Because <code>icu-config</code> is an executable script, it also solves the problem of locating the ICU libraries and headers, by allowing the system PATH to locate it.</p>
<h2>EXAMPLES</h2>
<p> <code>icu-config</code> can be used without a makefile. The command line below is sufficient for building a single-file c++ program against ICU. (For example, <code>icu/source/samples/props/props.cpp</code>) </p>
<dl>
<dt>
<dd> `icu-config &#8211;cxx &#8211;cxxflags &#8211;cppflags &#8211;ldflags` -o props props.cpp</dl>
<p> More commonly, <code>icu-config</code> will be called from within a makefile, and used to set up variables. The following example also builds the <i>props</i> example. </p>
<dl>
<dt>
<dd> CC=$(shell icu-config &#8211;cc) </p>
<p> CXX=$(shell icu-config &#8211;cxx) </p>
<p> CPPFLAGS=$(shell icu-config &#8211;cppflags) </p>
<p> CXXFLAGS=$(shell icu-config &#8211;cxxflags) </p>
<p> LDFLAGS =$(shell icu-config &#8211;ldflags) </p>
<p> all: props </p>
<p> props.o: props.cpp</dl>
<p> <a href="/docs/linux/man/1-make/">make</a>(1) will automatically use the above variables.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;bindir</code></p>
<dd> Prints the binary (executable) directory path. Normally equivalent to &#8216;bin&#8217;. ICU user-executable applications and scripts are found here.</p>
<dt><code>&#8211;cc</code></p>
<dd> Print the C compiler used. Equivalent to the $(CC) Makefile variable.</p>
<dt><code>&#8211;cflags</code></p>
<dd> Print the C compiler flags. Equivalent to the $(CFLAGS) Makefile variable. Does NOT include preprocessor directives such as include path or defined symbols. Examples include debugging (-g) and optimization flags</p>
<dt><code>&#8211;cppflags</code></p>
<dd> Print the C preprocessor flags. Equivalent to the $(CPPFLAGS) Makefile variable. Examples are -I include paths and -D define directives.</p>
<dt><code>&#8211;cppflags-searchpath</code></p>
<dd> Print the C preprocessor flags, as above but only -I search paths.</p>
<dt><code>&#8211;cxx</code></p>
<dd> Print the C++ compiler. Equivalent to the $(CXX) Makefile variable.</p>
<dt><code>&#8211;cxxflags</code></p>
<dd> Print the C++ compiler flags. Equivalent to the $(CXXFLAGS) Makefile variable.</p>
<dt><code>&#8211;detect-prefix</code></p>
<dd> If ICU has been moved from its installed location, prepending this flag to other <code>icu-config</code> calls will attempt to locate ICU relative to where the <code>icu-config</code> script has been located. Can be used as a last-chance effort if the ICU install has been damaged.</p>
<dt><code>&#8211;exec-prefix</code></p>
<dd> Print the prefix used for executable program directories (such as bin, sbin, etc). Normally the same as the prefix.</p>
<dt><code>&#8211;exists</code></p>
<dd> Script will return with a successful (0) status if ICU seems to be installed and located correctly, otherwise an error message and nonzero status will be displayed.</p>
<dt><code>&#8211;help</code>, <code>-?</code>,<code>&#8211;usage</code></p>
<dd> Print a help and usage message.</p>
<dt><code>&#8211;icudata</code></p>
<dd> Print the <i>shortname</i> of the ICU data file. This does not include any suffix such as .dat, .dll, .so, .lib, .a, etc nor does it include prefixes such as &#8216;lib&#8217;. It may be in the form <code>icudt21b</code></p>
<dt><code>&#8211;icudata-install-dir</code></p>
<dd> Print the directory where ICU packaged data should be installed. Can use as <a href="/docs/linux/man/1-pkgdata/">pkgdata</a>(1)&#8217;s &#8211;install option.</p>
<dt><code>&#8211;icudata-mode</code></p>
<dd> Print the default ICU pkgdata mode, such as dll or common. Can use as <a href="/docs/linux/man/1-pkgdata/">pkgdata</a>(1)&#8217;s &#8211;mode option.</p>
<dt><code>&#8211;icudatadir</code></p>
<dd> Print the path to packaged archive data. (should be where $ICU_DATA or equivalent default path points.) Will NOT point to the libdir.</p>
<dt><code>&#8211;invoke</code></p>
<dd> If ICU is not installed in a location where the operating system will locate its shared libraries, this option will print out commands so as to set the appropriate environment variables to load ICU&#8217;s shared libraries. For example, on many systems a variable named LD_LIBRARY_PATH or equivalent must be set.</p>
<dt><code>&#8211;invoke=</code><i>prog</i></p>
<dd> Same as the <code>&#8211;invoke</code> option, except includes options for invoking a program named <i>prog</i>. If <i>prog</i> is the name of an ICU tool, such as <a href="/docs/linux/man/1-genrb/">genrb</a>(1), then <code>icu-config</code> will also include the full path to that tool.</p>
<dt><code>&#8211;ldflags</code></p>
<dd> Print any flags which should be passed to the linker. These may include -L for library search paths, and -l for including ICU libraries. By default, this option will attempt to link in the &quot;common&quot; (libicuuc) and &quot;i18n&quot; (libicui18n) libraries, as well as the data library. If additional libraries are required, any of the following two flags may be added in conjunction with this one, for example &quot;&#8211;ldflags &#8211;ldflags-icuio&quot; if the icuio library is required in addition to the standard ICU libraries. Equivalent to the $(LDFLAGS) Makefile variable.</p>
<dt><code>&#8211;ldflags-layout</code></p>
<dd> Prints the link option for the ICU layout library.</p>
<dt><code>&#8211;ldflags-icuio</code></p>
<dd> Prints the link option to add the ICU I/O package</p>
<dt><code>&#8211;ldflags-libsonly</code></p>
<dd> Similar to <i>&#8211;ldflags</i> but only includes the -l options.</p>
<dt><code>&#8211;ldflags-searchpath</code></p>
<dd> Similar to <i>&#8211;ldflags</i> but only includes the -L search path options.</p>
<dt><code>&#8211;ldflags-system</code></p>
<dd> Similar to <i>&#8211;ldflags</i> but only includes system libraries (such as pthreads) <code>&#8211;mandir</code> Prints the location of the installed ICU man pages. Normally (man)</p>
<dt><code>&#8211;prefix</code></p>
<dd> Prints the prefix (base directory) under which the installed ICU resides.</p>
<dt><code>&#8211;prefix=</code><i>prefix</i></p>
<dd> Sets the ICU prefix to <i>prefix</i> for the remainder of this command line. Does test whether the new prefix is valid.</p>
<dt><code>&#8211;sbindir</code></p>
<dd> Prints the location of ICU system binaries, normally (sbin)</p>
<dt><code>&#8211;shared-datadir</code></p>
<dd> Prints the location of ICU shared data, normally (share)</p>
<dt><code>&#8211;sysconfdir</code></p>
<dd> Prints the location of ICU system configuration data, normally (etc)</p>
<dt><code>&#8211;unicode-version</code></p>
<dd> Prints the Version of the Unicode Standard which the current ICU uses.</p>
<dt><code>&#8211;version</code></p>
<dd> Prints the current version of ICU.</p>
<dt><code>&#8211;incfile</code></p>
<dd> Prints the &#8216;Makefile.inc&#8217; path, suitable for use with <a href="/docs/linux/man/1-pkgdata/">pkgdata</a>(1)&#8217;s -O option.</dl>
<h2>AUTHORS</h2>
<p> Steven Loomis</p>
<h2>VERSION</h2>
<p> 50.1.2</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2002-2004 IBM, Inc. and others. </p>
<h2>Index</h2>
