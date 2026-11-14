---
title: "pkgdata(1)"
name: "pkgdata"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pkgdata/"
description: "pkgdata – package data for use by ICU"
---

<h2 class="name">NAME</h2>
<p> <code>pkgdata</code> &#8211; package data for use by ICU </p>
<h2>SYNOPSIS</h2>
<p> <code>pkgdata</code> [ <code>-h</code>, <code>-?</code>, <code>&#8211;help</code> ] [ <code>-v</code>, <code>&#8211;verbose</code> ] [ <code>-c</code>, <code>&#8211;copyright</code> | <code>-C</code>, <code>&#8211;comment</code><i> comment</i> ] [ <code>-m</code>, <code>&#8211;mode</code><i> mode</i> ] <code>-p</code>, <code>&#8211;name</code><i> name</i> <code>-O</code>, <code>&#8211;bldopt</code><i> options</i> [ <code>-e</code>, <code>&#8211;entrypoint</code><i> name</i> ] [ <code>-r</code>, <code>&#8211;revision</code><i> version</i> ] [ <code>-F</code>, <code>&#8211;rebuild</code> ] [ <code>-I</code>, <code>&#8211;install</code> ] [ <code>-s</code>, <code>&#8211;sourcedir</code><i> source</i> ] [ <code>-d</code>, <code>&#8211;destdir</code><i> destination</i> ] [ <code>-T</code>, <code>&#8211;tempdir</code><i> directory</i> ] [ <i>file</i> &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <code>pkgdata</code> takes a set of data files and packages them for use by ICU or applications that use ICU. The typical reason to package files using <code>pkgdata</code> is to make their distribution easier and their loading by ICU faster and less consuming of limited system resources such as file descriptors. Packaged data also allow applications to be distributed with fewer resource files, or even with none at all if they link against the packaged data directly. </p>
<p> <code>pkgdata</code> supports a few different methods of packaging data that serve different purposes. </p>
<p> The default packaging <i>mode</i> is <code>common</code>, or <code>archive</code>. In this mode, the different data files are bundled together as an architecture-dependent file that can later be memory mapped for use by ICU. Data packaged using this mode will be looked up under the ICU data directory. Such packaging is easy to use for applications resource bundles, for example, as long as the application can install the packaged file in the ICU data directory. </p>
<p> Another packaging mode is the <code>dll</code>, or <code>library</code>, mode, where the data files are compiled into a shared library. ICU used to be able to dynamically load these shared libraries, but as of ICU 2.0, such support has been removed. This mode is still useful for two main purposes: to build ICU itself, as the ICU data is packaged as a shared library by default; and to build resource bundles that are linked to the application that uses them. Such resource bundles can then be placed anywhere where the system&#8217;s dynamic linker will be looking for shared libraries, instead of being forced to live inside the ICU data directory. </p>
<p> The <code>static</code> packaging mode is similar to the shared library one except that it produces a static library. </p>
<p> Finally, <code>pkgdata</code> supports a <code>files</code> mode which simply copies the data files instead of packaging them as a single file or library. This mode is mainly intended to provide support for building ICU before it is packaged as separate small packages for distribution with operating systems such as Debian GNU/Linux for example. Please refer to the packaging documentation in the ICU source distribution for further information on the use of this mode. </p>
<p> <code>pkgdata</code> builds, packages, installs, or cleans the appropriate data based on the options given without the need to call GNU <code>make</code> anymore.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd> Print help about usage and exit.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display extra informative messages during execution.</p>
<dt><code>-c</code>, <code>&#8211;copyright</code></p>
<dd> Include a copyright notice in the binary data.</p>
<dt><code>-C</code>, <code>&#8211;comment</code><i> comment</i></p>
<dd> Includes the specified <i>comment</i> in the resulting data instead of the ICU copyright notice.</p>
<dt><code>-m</code>, <code>&#8211;mode</code><i> mode</i></p>
<dd> Set the packaging <i>mode</i> to be used by <code>pkgdata</code>. The different modes and their meaning are explained in the <code>DESCRIPTION</code> section above. The valid mode names are <code>common</code> (or <code>archive</code>), <code>dll</code> (or <code>library</code>), and <code>files</code>.</p>
<dt><code>-O</code>, <code>&#8211;bldopt</code><i> options</i></p>
<dd> Specify options for the builder. The builder is used internally by <code>pkgdata</code> to generate the correct packaged file. Such options include, but are not limited to, setting variables used by <code><a href="/docs/linux/man/1-make/">make</a></code>(1) during the build of the packaged file. Note: If <code>icu-config</code> is available, then this option is not needed.</p>
<dt><code>-p</code>, <code>&#8211;name</code><i> name</i></p>
<dd> Set the packaged file name to <i>name</i>. This name is also used as the default entry point name after having been turned into a valid C identifier.</p>
<dt><code>-e</code>, <code>&#8211;entrypoint</code><i> name</i></p>
<dd> Set the data entry point (used for linking against the data in a shared library form) to <i>name</i>. The default entry point name is the name set by the <code>-n</code>, <code>&#8211;name</code> option.</p>
<dt><code>-r</code>, <code>&#8211;revision</code><i> version</i></p>
<dd> Enable versioning of the shared library produced in <code>dll</code>, or <code>library</code>, mode. The version number has the format <i>major</i>.<i>minor</i>.<i>patchlevel</i> and all parts except for <i>major</i> are optional. If only <i>major</i> is supplied then the version is assumed to be <i>major</i>.0 for versioning purposes.</p>
<dt><code>-F</code>, <code>&#8211;rebuild</code></p>
<dd> Force the rebuilding of all data and their repackaging.</p>
<dt><code>-I</code>, <code>&#8211;install</code></p>
<dd> Install the packaged file (or all the files in the <code>files</code> mode). If the variable <code>DESTDIR</code> is set it will be used for installation.</p>
<dt><code>-s</code>, <code>&#8211;sourcedir</code><i> source</i></p>
<dd> Set the source directory to <i>source</i>. The default source directory is the current directory.</p>
<dt><code>-d</code>, <code>&#8211;destdir</code><i> destination</i></p>
<dd> Set the destination directory to <i>destination</i>. The default destination directory is the current directory.</p>
<dt><code>-T</code>, <code>&#8211;tempdir</code><i> directory</i></p>
<dd> Set the directory used to generate temporary files to <i>directory</i>. The default temporary directory is the same as the destination directory as set by the <code>-d</code>, <code>&#8211;destdir</code> option.</dl>
<h2>AUTHORS</h2>
<p> Steven Loomis<br />
 Yves Arrouye</p>
<h2>VERSION</h2>
<p> 70.1</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2000-2009 IBM, Inc. and others. </p>
<h2>Index</h2>
