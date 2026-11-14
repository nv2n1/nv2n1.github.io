---
title: "i686-w64-mingw32-pkg-config(1)"
name: "i686-w64-mingw32-pkg-config"
section: "1"
letter: "i"
url: "/docs/linux/man/1-i686-w64-mingw32-pkg-config/"
description: "pkg-config – Return metainformation about installed libraries"
---

<h2>NAME</h2>
<p> pkg-config &#8211; Return metainformation about installed libraries</p>
<h2>SYNOPSIS</h2>
<p> <code>pkg-config</code> [&#8211;modversion] [&#8211;version] [&#8211;help] [&#8211;print-errors] [&#8211;silence-errors] [&#8211;errors-to-stdout] [&#8211;debug] [&#8211;cflags] [&#8211;libs] [&#8211;libs-only-L] [&#8211;libs-only-l] [&#8211;cflags-only-I] [&#8211;variable=VARIABLENAME] [&#8211;define-variable=VARIABLENAME=VARIABLEVALUE] [&#8211;print-variables] [&#8211;uninstalled] [&#8211;exists] [&#8211;atleast-version=VERSION] [&#8211;exact-version=VERSION] [&#8211;max-version=VERSION] [&#8211;list-all] [LIBRARIES&#8230;] [&#8211;print-provides] [&#8211;print-requires] [&#8211;print-requires-private] [LIBRARIES&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <i>pkg-config</i> program is used to retrieve information about installed libraries in the system. It is typically used to compile and link against one or more libraries. Here is a typical usage scenario in a Makefile: </p>
<pre>
program: program.c
        cc program.c $(pkg-config --cflags --libs gnomeui)
</pre>
<p> <i>pkg-config</i> retrieves information about packages from special metadata files. These files are named after the package, and has a <i>.pc</i> extension. On most systems, <i>pkg-config</i> looks in <i>/usr/lib/pkgconfig, /usr/share/pkgconfig, /usr/local/lib/pkgconfig</i> and <i>/usr/local/share/pkgconfig</i> for these files. It will additionally look in the colon-separated (on Windows, semicolon-separated) list of directories specified by the PKG_CONFIG_PATH environment variable. </p>
<p> The package name specified on the <i>pkg-config</i> command line is defined to be the name of the metadata file, minus the <i>.pc</i> extension. If a library can install multiple versions simultaneously, it must give each version its own name (for example, GTK 1.2 might have the package name &quot;gtk+&quot; while GTK 2.0 has &quot;gtk+-2.0&quot;). </p>
<p> In addition to specifying a package name on the command line, the full path to a given <i>.pc</i> file may be given instead. This allows a user to directly query a particular <i>.pc</i> file.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><i>&#8211;modversion</i></p>
<dd> Requests that the version information of the libraries specified on the command line be displayed. If <i>pkg-config</i> can find all the libraries on the command line, each library&#8217;s version string is printed to stdout, one version per line. In this case <i>pkg-config</i> exits successfully. If one or more libraries is unknown, <i>pkg-config</i> exits with a nonzero code, and the contents of stdout are undefined.</p>
<dt><i>&#8211;version</i></p>
<dd> Displays the version of <i>pkg-config</i> and terminates.</p>
<dt><i>&#8211;help</i></p>
<dd> Displays a help message and terminates.</p>
<dt><i>&#8211;print-errors</i></p>
<dd> If one or more of the modules on the command line, or their dependencies, are not found, or if an error occurs in parsing a <i>.pc</i> file, then this option will cause errors explaining the problem to be printed. With &quot;predicate&quot; options such as &quot;&#8211;exists&quot; <i>pkg-config</i> runs silently by default, because it&#8217;s usually used in scripts that want to control what&#8217;s output. This option can be used alone (to just print errors encountered locating modules on the command line) or with other options. The PKG_CONFIG_DEBUG_SPEW environment variable overrides this option.</p>
<dt><i>&#8211;silence-errors</i></p>
<dd> If one or more of the modules on the command line, or their dependencies, are not found, or if an error occurs in parsing a a <i>.pc</i> file, then this option will keep errors explaining the problem from being printed. With &quot;predicate&quot; options such as &quot;&#8211;exists&quot; <i>pkg-config</i> runs silently by default, because it&#8217;s usually used in scripts that want to control what&#8217;s output. So this option is only useful with options such as &quot;&#8211;cflags&quot; or &quot;&#8211;modversion&quot; that print errors by default. The PKG_CONFIG_DEBUG_SPEW environment variable overrides this option.</p>
<dt><i>&#8211;errors-to-stdout</i></p>
<dd> If printing errors, print them to stdout rather than the default stderr</p>
<dt><i>&#8211;debug</i></p>
<dd> Print debugging information. This is slightly different than the PKG_CONFIG_DEBUG_SPEW environment variable, which also enable &quot;&#8211;print-errors&quot;. </p>
</dl>
<p> The following options are used to compile and link programs:</p>
<dl>
<dt><i>&#8211;cflags</i></p>
<dd> This prints pre-processor and compile flags required to compile the packages on the command line, including flags for all their dependencies. Flags are &quot;compressed&quot; so that each identical flag appears only once. <i>pkg-config</i> exits with a nonzero code if it can&#8217;t find metadata for one or more of the packages on the command line.</p>
<dt><i>&#8211;cflags-only-I</i></p>
<dd> This prints the -I part of &quot;&#8211;cflags&quot;. That is, it defines the header search path but doesn&#8217;t specify anything else.</p>
<dt><i>&#8211;libs</i></p>
<dd> This option is identical to &quot;&#8211;cflags&quot;, only it prints the link flags. As with &quot;&#8211;cflags&quot;, duplicate flags are merged (maintaining proper ordering), and flags for dependencies are included in the output.</p>
<dt><i>&#8211;libs-only-L</i></p>
<dd> This prints the -L/-R part of &quot;&#8211;libs&quot;. That is, it defines the library search path but doesn&#8217;t specify which libraries to link with.</p>
<dt><i>&#8211;libs-only-l</i></p>
<dd> This prints the -l part of &quot;&#8211;libs&quot; for the libraries specified on the command line. Note that the union of &quot;&#8211;libs-only-l&quot; and &quot;&#8211;libs-only-L&quot; may be smaller than &quot;&#8211;libs&quot;, due to flags such as -rdynamic.</p>
<dt><i>&#8211;variable=VARIABLENAME</i></p>
<dd> This returns the value of a variable defined in a package&#8217;s <i>.pc</i> file. Most packages define the variable &quot;prefix&quot;, for example, so you can say: </p>
<pre>
  $ pkg-config --variable=prefix glib-2.0
  /usr/
</pre>
<dt><i>&#8211;define-variable=VARIABLENAME=VARIABLEVALUE</i></p>
<dd> This sets a global value for a variable, overriding the value in any <i>.pc</i> files. Most packages define the variable &quot;prefix&quot;, for example, so you can say: </p>
<pre><code>
$ pkg - config-- print - errors-- define - variable = prefix = / foo-- variable = prefix glib - 2.0 / foo
</code></pre>
<dt><i>&#8211;print-variables</i></p>
<dd> Returns a list of all variables defined in the package. </p>
<dt><i>&#8211;uninstalled</i></p>
<dd> Normally if you request the package &quot;foo&quot; and the package &quot;foo-uninstalled&quot; exists, <i>pkg-config</i> will prefer the &quot;-uninstalled&quot; variant. This allows compilation/linking against uninstalled packages. If you specify the &quot;&#8211;uninstalled&quot; option, <i>pkg-config</i> will return successfully if any &quot;-uninstalled&quot; packages are being used, and return failure (false) otherwise. (The PKG_CONFIG_DISABLE_UNINSTALLED environment variable keeps <i>pkg-config</i> from implicitly choosing &quot;-uninstalled&quot; packages, so if that variable is set, they will only have been used if you pass a name like &quot;foo-uninstalled&quot; on the command line explicitly.)</p>
<dt><i>&#8211;exists</i></p>
<dd>
<dt><i>&#8211;atleast-version=VERSION</i></p>
<dd>
<dt><i>&#8211;exact-version=VERSION</i></p>
<dd>
<dt><i>&#8211;max-version=VERSION</i></p>
<dd> These options test whether the package or list of packages on the command line are known to <i>pkg-config</i>, and optionally whether the version number of a package meets certain constraints. If all packages exist and meet the specified version constraints, <i>pkg-config</i> exits successfully. Otherwise it exits unsuccessfully. Only the first VERSION comparing option will be honored. Subsequent options of this type will be ignored. </p>
<p> Rather than using the version-test options, you can simply give a version constraint after each package name, for example: </p>
<pre>
  $ pkg-config --exists 'glib-2.0 &gt;= 1.3.4 libxml = 1.8.3'
</pre>
<p> Remember to use &#8211;print-errors if you want error messages. When no output options are supplied to <i>pkg-config</i>, &#8211;exists is implied.</p>
<dt><i>&#8211;msvc-syntax</i></p>
<dd> This option is available only on Windows. It causes <i>pkg-config</i> to output -l and -L flags in the form recognized by the Microsoft Visual C++ command-line compiler, <i>cl</i>. Specifically, instead of <i>-Lx:/some/path</i> it prints <i>/libpath:x/some/path</i>, and instead of <i>-lfoo</i> it prints <i>foo.lib</i>. Note that the &#8211;libs output consists of flags for the linker, and should be placed on the cl command line after a /link switch.</p>
<dt><i>&#8211;dont-define-prefix</i></p>
<dd> This option is available only on Windows. It prevents <i>pkg-config</i> from automatically trying to override the value of the variable &quot;prefix&quot; in each .pc file.</p>
<dt><i>&#8211;prefix-variable=PREFIX</i></p>
<dd> Also this option is available only on Windows. It sets the name of the variable that <i>pkg-config</i> automatically sets as described above.</p>
<dt><i>&#8211;static</i></p>
<dd> Output libraries suitable for static linking. That means including any private libraries in the output. This relies on proper tagging in the .pc files, else a too large number of libraries will ordinarily be output.</p>
<dt><i>&#8211;list-all</i></p>
<dd> List all modules found in the <i>pkg-config</i> path.</p>
<dt><i>&#8211;print-provides</i></p>
<dd> List all modules the given packages provides.</p>
<dt><i>&#8211;print-requires</i></p>
<dd> List all modules the given packages requires.</p>
<dt><i>&#8211;print-requires-private</i></p>
<dd> List all modules the given packages requires for static linking (see &#8211;static).</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><i>PKG_CONFIG_PATH</i></p>
<dd> A colon-separated (on Windows, semicolon-separated) list of directories to search for .pc files. The default directory will always be searched after searching the path; the default is <i>libdir/</i>pkgconfig:<i>datadir</i>/pkgconfig where <i>libdir</i> is the libdir for <i>pkg-config</i> and <i>datadir</i> is the datadir for <i>pkg-config</i> when it was installed.</p>
<dt><i>PKG_CONFIG_DEBUG_SPEW</i></p>
<dd> If set, causes <i>pkg-config</i> to print all kinds of debugging information and report all errors.</p>
<dt><i>PKG_CONFIG_TOP_BUILD_DIR</i></p>
<dd> A value to set for the magic variable <i>pc_top_builddir</i> which may appear in <i>.pc</i> files. If the environment variable is not set, the default value &#8216;$(top_builddir)&#8217; will be used. This variable should refer to the top builddir of the Makefile where the compile/link flags reported by <i>pkg-config</i> will be used. This only matters when compiling/linking against a package that hasn&#8217;t yet been installed.</p>
<dt><i>PKG_CONFIG_DISABLE_UNINSTALLED</i></p>
<dd> Normally if you request the package &quot;foo&quot; and the package &quot;foo-uninstalled&quot; exists, <i>pkg-config</i> will prefer the &quot;-uninstalled&quot; variant. This allows compilation/linking against uninstalled packages. If this environment variable is set, it disables said behavior.</p>
<dt><i>PKG_CONFIG_ALLOW_SYSTEM_CFLAGS</i></p>
<dd> Don&#8217;t strip -I/usr/include out of cflags.</p>
<dt><i>PKG_CONFIG_ALLOW_SYSTEM_LIBS</i></p>
<dd> Don&#8217;t strip -L/usr/lib or -L/lib out of libs.</p>
<dt><i>PKG_CONFIG_SYSROOT_DIR</i></p>
<dd> Modify -I and -L to use the directories located in target sysroot. this option is useful when cross-compiling packages that use pkg-config to determine CFLAGS and LDFLAGS. -I and -L are modified to point to the new system root. this means that a -I/usr/include/libfoo will become -I/var/target/usr/include/libfoo with a PKG_CONFIG_SYSROOT_DIR equal to /var/target (same rule apply to -L)</p>
<dt><i>PKG_CONFIG_LIBDIR</i></p>
<dd> Replaces the default <i>pkg-config</i> search directory, usually <i>/usr/lib/pkgconfig</i></dl>
<h2>QUERYING PKG-CONFIG&#8217;S DEFAULTS</h2>
<p> <i>pkg-config</i> can be used to query itself for the default search path, version number and other information, for instance using: </p>
<pre>
  $ pkg-config --variable pc_path pkg-config
</pre>
<p> or </p>
<pre>
  $ pkg-config --modversion pkg-config
</pre>
<h2>WINDOWS SPECIALITIES</h2>
<p> If a .pc file is found in a directory that matches the usual conventions (i.e., ends with \lib\pkgconfig or \share\pkgconfig), the prefix for that package is assumed to be the grandparent of the directory where the file was found, and the <i>prefix</i> variable is overridden for that file accordingly. </p>
<p> If the value of a variable in a .pc file begins with the original, non-overridden, value of the <i>prefix</i> variable, then the overridden value of <i>prefix</i> is used instead.</p>
<h2>AUTOCONF MACROS</h2>
<dl>
<dt><i>PKG_CHECK_MODULES(VARIABLE-PREFIX, MODULES [,ACTION-IF-FOUND [,ACTION-IF-NOT-FOUND]])</i></p>
<dd>
<p> The macro PKG_CHECK_MODULES can be used in <i>configure.ac</i> to check whether modules exist. A typical usage would be:<br />
PKG_CHECK_MODULES([MYSTUFF], [gtk + -2.0 &gt;= 1.3.5 libxml = 1.8.4])</p>
<p> This would result in MYSTUFF_LIBS and MYSTUFF_CFLAGS substitution variables, set to the libs and cflags for the given module list. If a module is missing or has the wrong version, by default configure will abort with a message. To replace the default action, specify an ACTION-IF-NOT-FOUND. PKG_CHECK_MODULES will not print any error messages if you specify your own ACTION-IF-NOT-FOUND. However, it will set the variable MYSTUFF_PKG_ERRORS, which you can use to display what went wrong. </p>
<p> Note that if there is a possibility the first call to PKG_CHECK_MODULES might not happen, you should be sure to include an explicit call to PKG_PROG_PKG_CONFIG in your configure.ac. </p>
<p> Also note that repeated usage of VARIABLE-PREFIX is not recommended. After the first successful usage, subsequent calls with the same VARIABLE-PREFIX will simply use the _LIBS and _CFLAGS variables set from the previous usage without calling <i>pkg-config</i> again.</p>
<dt><i>PKG_PROG_PKG_CONFIG([MIN-VERSION])</i></p>
<dd>
<p> Defines the PKG_CONFIG variable to the best pkg-config available, useful if you need pkg-config but don&#8217;t want to use PKG_CHECK_MODULES.</p>
<dt><i>PKG_CHECK_EXISTS(MODULES, [ACTION-IF-FOUND], [ACTION-IF-NOT-FOUND])</i></p>
<dd>
<p> Check to see whether a particular set of modules exists. Similar to PKG_CHECK_MODULES(), but does not set variables or print errors. </p>
<p> Similar to PKG_CHECK_MODULES, make sure that the first instance of this or PKG_CHECK_MODULES is called, or make sure to call PKG_CHECK_EXISTS manually.</p>
<dt><i>PKG_INSTALLDIR(DIRECTORY)</i></p>
<dd>
<p> Substitutes the variable pkgconfigdir as the location where a module should install pkg-config .pc files. By default the directory is $libdir/pkgconfig, but the default can be changed by passing DIRECTORY. The user can override through the &#8211;with-pkgconfigdir parameter.</p>
<dt><i>PKG_NOARCH_INSTALLDIR(DIRECTORY)</i></p>
<dd>
<p> Substitutes the variable noarch_pkgconfigdir as the location where a module should install arch-independent pkg-config .pc files. By default the directory is $datadir/pkgconfig, but the default can be changed by passing DIRECTORY. The user can override through the &#8211;with-noarch-pkgconfigdir parameter.</p>
<dt><i>PKG_CHECK_VAR(VARIABLE, MODULE, CONFIG-VARIABLE, [ACTION-IF-FOUND], [ACTION-IF-NOT-FOUND])</i></p>
<dd>
<p> Retrieves the value of the pkg-config variable CONFIG-VARIABLE from MODULE and stores it in VARIABLE. Note that repeated usage of VARIABLE is not recommended as the check will be skipped if the variable is already set. </p>
</dl>
<h2>METADATA FILE SYNTAX</h2>
<p> To add a library to the set of packages <i>pkg-config</i> knows about, simply install a <i>.pc</i> file. You should install this file to <i>libdir</i>/pkgconfig. </p>
<p> Here is an example file: </p>
<pre><code>
#This is a comment
prefix=/home/hp/unst   # this defines a variable
exec_prefix=${prefix}  # defining another variable in terms of the first
libdir=${exec_prefix}/lib
includedir=${prefix}/include
Name: GObject                            # human-readable name
Description: Object/type system for GLib # human-readable description
Version: 1.3.1
URL: http://www.gtk.org
Requires: glib-2.0 = 1.3.1
Conflicts: foobar &lt;= 4.5
Libs: -L${libdir} -lgobject-1.3
Libs.private: -lm
Cflags: -I${includedir}/glib-2.0 -I${libdir}/glib/include
</code></pre>
<p> You would normally generate the file using configure, so that the prefix, etc. are set to the proper values. The GNU Autoconf manual recommends generating files like .pc files at build time rather than configure time, so when you build the .pc file is a matter of taste and preference. </p>
<p> Files have two kinds of line: keyword lines start with a keyword plus a colon, and variable definitions start with an alphanumeric string plus an equals sign. Keywords are defined in advance and have special meaning to <i>pkg-config</i>; variables do not, you can have any variables that you wish (however, users may expect to retrieve the usual directory name variables). </p>
<p> Note that variable references are written &quot;${foo}&quot;; you can escape literal &quot;${&quot; as &quot;$${&quot;.</p>
<dl>
<dt><i>Name:</i></p>
<dd> This field should be a human-readable name for the package. Note that it is not the name passed as an argument to <i>pkg-config</i>.</p>
<dt><i>Description:</i></p>
<dd> This should be a brief description of the package</p>
<dt><i>URL:</i></p>
<dd> An URL where people can get more information about and download the package</p>
<dt><i>Version:</i></p>
<dd> This should be the most-specific-possible package version string.</p>
<dt><i>Requires:</i></p>
<dd> This is a comma-separated list of packages that are required by your package. Flags from dependent packages will be merged in to the flags reported for your package. Optionally, you can specify the version of the required package (using the operators =, &lt;, &gt;, &gt;=, &lt;=); specifying a version allows <i>pkg-config</i> to perform extra sanity checks. You may only mention the same package one time on the <i>Requires:</i> line. If the version of a package is unspecified, any version will be used with no checking.</p>
<dt><i>Requires.private:</i></p>
<dd> A list of packages required by this package. The difference from <i>Requires</i> is that the packages listed under <i>Requires.private</i> are not taken into account when a flag list is computed for dynamically linked executable (i.e., when &#8211;static was not specified). In the situation where each .pc file corresponds to a library, <i>Requires.private</i> shall be used exclusively to specify the dependencies between the libraries.</p>
<dt><i>Conflicts:</i></p>
<dd> This optional line allows <i>pkg-config</i> to perform additional sanity checks, primarily to detect broken user installations. The syntax is the same as <i>Requires:</i> except that you can list the same package more than once here, for example &quot;foobar = 1.2.3, foobar = 1.2.5, foobar &gt;= 1.3&quot;, if you have reason to do so. If a version isn&#8217;t specified, then your package conflicts with all versions of the mentioned package. If a user tries to use your package and a conflicting package at the same time, then <i>pkg-config</i> will complain.</p>
<dt><i>Libs:</i></p>
<dd> This line should give the link flags specific to your package. Don&#8217;t add any flags for required packages; <i>pkg-config</i> will add those automatically.</p>
<dt><i>Libs.private:</i></p>
<dd> This line should list any private libraries in use. Private libraries are libraries which are not exposed through your library, but are needed in the case of static linking. This differs from <i>Requires.private</i> in that it references libraries that do not have package files installed.</p>
<dt><i>Cflags:</i></p>
<dd> This line should list the compile flags specific to your package. Don&#8217;t add any flags for required packages; <i>pkg-config</i> will add those automatically.</dl>
<h2>AUTHOR</h2>
<p> <i>pkg-config</i> was written by James Henstridge, rewritten by Martijn van Beers, and rewritten again by Havoc Pennington. Tim Janik, Owen Taylor, and Raja Harinath submitted suggestions and some code. <i>gnome-config</i> was written by Miguel de Icaza, Raja Harinath and various hackers in the GNOME team. It was inspired by Owen Taylor&#8217;s <i>gtk-config</i> program.</p>
<h2>BUGS</h2>
<p> <i>pkg-config</i> does not handle mixing of parameters with and without = well. Stick with one. </p>
<p> Bugs can be reported at <a rel="nofollow" href="http://bugs.freedesktop.org/">http://bugs.freedesktop.org/</a> under the <i>pkg-config</i> component. </p>
<h2>Index</h2>
