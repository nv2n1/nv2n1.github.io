---
title: "apxs(1)"
name: "apxs"
section: "1"
letter: "a"
url: "/docs/linux/man/1-apxs/"
description: "apxs – APache eXtenSion tool"
---

<h2 class="name">NAME</h2>
<p> apxs &#8211; APache eXtenSion tool</p>
<h2>SYNOPSIS</h2>
<p>&nbsp;<wbr> </p>
<p> <code>apxs</code> &#8211;<code>g</code> [ &#8211;<code>S</code> <i>name</i>=<i>value</i> ] &#8211;<code>n</code> <i>modname</i><br />
&nbsp;<wbr> </p>
<p> <code>apxs</code> &#8211;<code>q</code> [ &#8211;<code>v</code> ] [ &#8211;<code>S</code> <i>name</i>=<i>value</i> ] <i>query</i> &#8230;<br />
&nbsp;<wbr> </p>
<p> <code>apxs</code> &#8211;<code>c</code> [ &#8211;<code>S</code> <i>name</i>=<i>value</i> ] [ &#8211;<code>o</code> <i>dsofile</i> ] [ &#8211;<code>I</code> <i>incdir</i> ] [ &#8211;<code>D</code> <i>name</i>=<i>value</i> ] [ &#8211;<code>L</code> <i>libdir</i> ] [ &#8211;<code>l</code> <i>libname</i> ] [ &#8211;<code>Wc,</code><i>compiler-flags</i> ] [ &#8211;<code>Wl,</code><i>linker-flags</i> ] <i>files</i> &#8230;<br />
&nbsp;<wbr> </p>
<p> <code>apxs</code> &#8211;<code>i</code> [ &#8211;<code>S</code> <i>name</i>=<i>value</i> ] [ &#8211;<code>n</code> <i>modname</i> ] [ &#8211;<code>a</code> ] [ &#8211;<code>A</code> ] <i>dso-file</i> &#8230;<br />
&nbsp;<wbr> </p>
<p> <code>apxs</code> &#8211;<code>e</code> [ &#8211;<code>S</code> <i>name</i>=<i>value</i> ] [ &#8211;<code>n</code> <i>modname</i> ] [ &#8211;<code>a</code> ] [ &#8211;<code>A</code> ] <i>dso-file</i> &#8230;<br />
&nbsp;<wbr> </p>
<h2>SUMMARY</h2>
<p>&nbsp;<wbr> </p>
<p> apxs is a tool for building and installing extension modules for the Apache HyperText Transfer Protocol (HTTP) server. This is achieved by building a dynamic shared object (DSO) from one or more source or object <i>files</i> which then can be loaded into the Apache server under runtime via the LoadModule directive from mod_so.<br />
&nbsp;<wbr> </p>
<p> So to use this extension mechanism your platform has to support the DSO feature and your Apache httpd binary has to be built with the mod_so module. The apxs tool automatically complains if this is not the case. You can check this yourself by manually running the command<br />
&nbsp;<wbr> </p>
<pre>
      $ httpd -l
    
</pre>
<p>&nbsp;<wbr> </p>
<p> The module mod_so should be part of the displayed list. If these requirements are fulfilled you can easily extend your Apache server&#8217;s functionality by installing your own modules with the DSO mechanism by the help of this apxs tool:<br />
&nbsp;<wbr> </p>
<pre><code>
      $ apxs -i -a -c mod_foo.c
      gcc -fpic -DSHARED_MODULE -I/path/to/apache/include -c mod_foo.c
      ld -Bshareable -o mod_foo.so mod_foo.o
      cp mod_foo.so /path/to/apache/modules/mod_foo.so
      chmod 755 /path/to/apache/modules/mod_foo.so
      [activating module `foo' in /path/to/apache/etc/httpd.conf]
      $ apachectl restart
      /path/to/apache/sbin/apachectl restart: httpd not running, trying to start
      [Tue Mar 31 11:27:55 1998] [debug] mod_so.c(303): loaded module foo_module
      /path/to/apache/sbin/apachectl restart: httpd started
      $ _
</code></pre>
<p>&nbsp;<wbr> </p>
<p> The arguments <i>files</i> can be any C source file (.c), a object file (.o) or even a library archive (.a). The apxs tool automatically recognizes these extensions and automatically used the C source files for compilation while just using the object and archive files for the linking phase. But when using such pre-compiled objects make sure they are compiled for position independent code (PIC) to be able to use them for a dynamically loaded shared object. For instance with GCC you always just have to use -fpic. For other C compilers consult its manual page or at watch for the flags apxs uses to compile the object files.<br />
&nbsp;<wbr> </p>
<p> For more details about DSO support in Apache read the documentation of mod_so or perhaps even read the src/modules/standard/mod_so.c source file.<br />
&nbsp;<wbr> </p>
<h2>OPTIONS</h2>
<p>&nbsp;<wbr></p>
<h3>Common Options</h3>
<p>&nbsp;<wbr><br />
&nbsp;<wbr></p>
<dl>
<dt>-n <i>modname</i></p>
<dd> This explicitly sets the module name for the -i (install) and -g (template generation) option. Use this to explicitly specify the module name. For option -g this is required, for option -i the apxs tool tries to determine the name from the source or (as a fallback) at least by guessing it from the filename.<br />
&nbsp;<wbr>&nbsp;<wbr></dl>
<h3>Query Options</h3>
<p>&nbsp;<wbr><br />
&nbsp;<wbr></p>
<dl>
<dt>-q</p>
<dd> Performs a query for variables and environment settings used to build httpd. When invoked without <i>query</i> parameters, it prints all known variables and their values. The optional -v parameter formats the list output. .PP Use this to manually determine settings used to build the httpd that will load your module. For instance use INC=-I`apxs -q INCLUDEDIR` .PP inside your own Makefiles if you need manual access to Apache&#8217;s C header files.<br />
&nbsp;<wbr>&nbsp;<wbr></dl>
<h3>Configuration Options</h3>
<p>&nbsp;<wbr><br />
&nbsp;<wbr></p>
<dl>
<dt>-S <i>name</i>=<i>value</i></p>
<dd> This option changes the apxs settings described above.<br />
&nbsp;<wbr>&nbsp;<wbr></dl>
<h3>Template Generation Options</h3>
<p>&nbsp;<wbr><br />
&nbsp;<wbr></p>
<dl>
<dt>-g</p>
<dd> This generates a subdirectory <i>name</i> (see option -n) and there two files: A sample module source file named mod_<i>name</i>.c which can be used as a template for creating your own modules or as a quick start for playing with the apxs mechanism. And a corresponding Makefile for even easier build and installing of this module.<br />
&nbsp;<wbr>&nbsp;<wbr></dl>
<h3>DSO Compilation Options</h3>
<p>&nbsp;<wbr><br />
&nbsp;<wbr></p>
<dl>
<dt>-c</p>
<dd> This indicates the compilation operation. It first compiles the C source files (.c) of <i>files</i> into corresponding object files (.o) and then builds a dynamically shared object in <i>dsofile</i> by linking these object files plus the remaining object files (.o and .a) of <i>files</i>. If no -o option is specified the output file is guessed from the first filename in <i>files</i> and thus usually defaults to mod_<i>name</i>.so.</p>
<dt>-o <i>dsofile</i></p>
<dd> Explicitly specifies the filename of the created dynamically shared object. If not specified and the name cannot be guessed from the <i>files</i> list, the fallback name mod_unknown.so is used.</p>
<dt>-D <i>name</i>=<i>value</i></p>
<dd> This option is directly passed through to the compilation command(s). Use this to add your own defines to the build process.</p>
<dt>-I <i>incdir</i></p>
<dd> This option is directly passed through to the compilation command(s). Use this to add your own include directories to search to the build process.</p>
<dt>-L <i>libdir</i></p>
<dd> This option is directly passed through to the linker command. Use this to add your own library directories to search to the build process.</p>
<dt>-l <i>libname</i></p>
<dd> This option is directly passed through to the linker command. Use this to add your own libraries to search to the build process.</p>
<dt>-Wc,<i>compiler-flags</i></p>
<dd> This option passes <i>compiler-flags</i> as additional flags to the libtool &#8211;mode=compile command. Use this to add local compiler-specific options.</p>
<dt>-Wl,<i>linker-flags</i></p>
<dd> This option passes <i>linker-flags</i> as additional flags to the libtool &#8211;mode=link command. Use this to add local linker-specific options.</p>
<dt>-p</p>
<dd> This option causes apxs to link against the apr/apr-util libraries. This is useful when compiling helper programs that use the apr/apr-util libraries.<br />
&nbsp;<wbr>&nbsp;<wbr></dl>
<h3>DSO Installation and Configuration Options</h3>
<p>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr></p>
<dl>
<dt>-i</p>
<dd> This indicates the installation operation and installs one or more dynamically shared objects into the server&#8217;s <i>modules</i> directory.</p>
<dt>-a</p>
<dd> This activates the module by automatically adding a corresponding LoadModule line to Apache&#8217;s httpd.conf configuration file, or by enabling it if it already exists.</p>
<dt>-A</p>
<dd> Same as option -a but the created LoadModule directive is prefixed with a hash sign (#), <i>i.e.</i>, the module is just prepared for later activation but initially disabled.</p>
<dt>-e</p>
<dd> This indicates the editing operation, which can be used with the -a and -A options similarly to the -i operation to edit Apache&#8217;s httpd.conf configuration file without attempting to install the module.<br />
&nbsp;<wbr>&nbsp;<wbr></dl>
<h2>EXAMPLES</h2>
<p>&nbsp;<wbr> </p>
<p> Assume you have an Apache module named mod_foo.c available which should extend Apache&#8217;s server functionality. To accomplish this you first have to compile the C source into a shared object suitable for loading into the Apache server under runtime via the following command:<br />
&nbsp;<wbr> </p>
<pre>
      $ apxs -c mod_foo.c
      /path/to/libtool --mode=compile gcc ... -c mod_foo.c
      /path/to/libtool --mode=link gcc ... -o mod_foo.la mod_foo.slo
      $ _
    
</pre>
<p>&nbsp;<wbr> </p>
<p> Then you have to update the Apache configuration by making sure a LoadModule directive is present to load this shared object. To simplify this step apxs provides an automatic way to install the shared object in its &quot;modules&quot; directory and updating the httpd.conf file accordingly. This can be achieved by running:<br />
&nbsp;<wbr> </p>
<pre>
      $ apxs -i -a mod_foo.la
      /path/to/instdso.sh mod_foo.la /path/to/apache/modules
      /path/to/libtool --mode=install cp mod_foo.la /path/to/apache/modules
      ...
      chmod 755 /path/to/apache/modules/mod_foo.so
      [activating module `foo' in /path/to/apache/conf/httpd.conf]
      $ _
    
</pre>
<p>&nbsp;<wbr> </p>
<p> This way a line named<br />
&nbsp;<wbr> </p>
<pre>
      LoadModule foo_module modules/mod_foo.so
    
</pre>
<p>&nbsp;<wbr> </p>
<p> is added to the configuration file if still not present. If you want to have this disabled per default use the -A option, <i>i.e.</i><br />
&nbsp;<wbr> </p>
<pre>
      $ apxs -i -A mod_foo.c
    
</pre>
<p>&nbsp;<wbr> </p>
<p> For a quick test of the apxs mechanism you can create a sample Apache module template plus a corresponding Makefile via:<br />
&nbsp;<wbr><br />
$ apxs &#8211; g &#8211; n foo Creating[DIR] foo Creating[FILE] foo / Makefile Creating[FILE] foo / modules.mk Creating[FILE] foo / mod_foo.c Creating[FILE] foo /.deps $ _</p>
<p>&nbsp;<wbr> </p>
<p> Then you can immediately compile this sample module into a shared object and load it into the Apache server:<br />
&nbsp;<wbr> </p>
<pre><code>
      $ cd foo
      $ make all reload
      apxs -c mod_foo.c
      /path/to/libtool --mode=compile gcc ... -c mod_foo.c
      /path/to/libtool --mode=link gcc ... -o mod_foo.la mod_foo.slo
      apxs -i -a -n "foo" mod_foo.la
      /path/to/instdso.sh mod_foo.la /path/to/apache/modules
      /path/to/libtool --mode=install cp mod_foo.la /path/to/apache/modules
      ...
      chmod 755 /path/to/apache/modules/mod_foo.so
      [activating module `foo' in /path/to/apache/conf/httpd.conf]
      apachectl restart
      /path/to/apache/sbin/apachectl restart: httpd not running, trying to start
      [Tue Mar 31 11:27:55 1998] [debug] mod_so.c(303): loaded module foo_module
      /path/to/apache/sbin/apachectl restart: httpd started
      $ _
</code></pre>
<p>&nbsp;<wbr> </p>
<h2>Index</h2>
