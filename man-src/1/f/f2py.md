---

title: "f2py(1)"
name: "f2py"
section: "1"
letter: "f"
url: "/docs/linux/man/1-f2py/"
description: "f2py – Fortran to Python interface generator"
---

<p> f2py &#8211; Fortran to Python interface generator </p>
<h2>SYNOPSIS</h2>
<p> (1) To construct extension module sources: </p>
<p> <code>f2py</code> [&lt;options&gt;] &lt;fortran files&gt; [[[only:]||[skip:]] &lt;fortran functions&gt; ] [: &lt;fortran files&gt; &#8230;] </p>
<p> (2) To compile fortran files and build extension modules: </p>
<p> <code>f2py</code> -c [&lt;options&gt;, &lt;config_fc options&gt;, &lt;extra options&gt;] &lt;fortran files&gt; </p>
<p> (3) To generate signature files: </p>
<p> <code>f2py</code> -h &lt;filename.pyf&gt; &#8230;&lt; same options as in (1) &gt;</p>
<h2>DESCRIPTION</h2>
<p> This program generates a Python C/API file (&lt;modulename&gt;module.c) that contains wrappers for given Fortran or C functions so that they can be called from Python. With the -c option the corresponding extension modules are built.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h &lt;filename&gt;</code></dt>
<dd> Write signatures of the fortran routines to file &lt;filename&gt; and exit. You can then edit &lt;filename&gt; and use it instead of &lt;fortran files&gt;. If &lt;filename&gt;==stdout then the signatures are printed to stdout.</dd>
<dt><code>&lt;fortran functions&gt;</code></dt>
<dd> Names of fortran routines for which Python C/API functions will be generated. Default is all that are found in &lt;fortran files&gt;.</dd>
<dt><code>skip:</code></dt>
<dd> Ignore fortran functions that follow until `:&#8217;.</dd>
<dt><code>only:</code></dt>
<dd> Use only fortran functions that follow until `:&#8217;.</dd>
<dt><code>:</code></dt>
<dd> Get back to &lt;fortran files&gt; mode.</dd>
<dt><code>-m &lt;modulename&gt;</code></dt>
<dd> Name of the module; f2py generates a Python/C API file &lt;modulename&gt;module.c or extension module &lt;modulename&gt;. Default is &#8216;untitled&#8217;.</dd>
<dt><code>&#8211;[no-]lower</code></dt>
<dd> Do [not] lower the cases in &lt;fortran files&gt;. By default, &#8211;lower is assumed with -h key, and &#8211;no-lower without -h key.</dd>
<dt><code>&#8211;build-dir &lt;dirname&gt;</code></dt>
<dd> All f2py generated files are created in &lt;dirname&gt;. Default is tempfile.mkdtemp().</dd>
<dt><code>&#8211;overwrite-signature</code></dt>
<dd> Overwrite existing signature file.</dd>
<dt><code>&#8211;[no-]latex-doc</code></dt>
<dd> Create (or not) &lt;modulename&gt;module.tex. Default is &#8211;no-latex-doc.</dd>
<dt><code>&#8211;short-latex</code></dt>
<dd> Create &#8216;incomplete&#8217; LaTeX document (without commands \documentclass, 	ableofcontents, and egin{document}, nd{document}).</dd>
<dt><code>&#8211;[no-]rest-doc</code></dt>
<dd> Create (or not) &lt;modulename&gt;module.rst. Default is &#8211;no-rest-doc.</dd>
<dt><code>&#8211;debug-capi</code></dt>
<dd> Create C/API code that reports the state of the wrappers during runtime. Useful for debugging.</dd>
<dt><code>-include'&lt;includefile&gt;&#8217;</code></dt>
<dd> Add CPP #include statement to the C/API code. &lt;includefile&gt; should be in the format of either `&quot;filename.ext&quot;&#8217; or `&lt;filename.ext&gt;&#8217;. As a result &lt;includefile&gt; will be included just before wrapper functions part in the C/API code. The option is depreciated, use `usercode` statement in signature files instead.</dd>
<dt><code>&#8211;[no-]wrap-functions</code></dt>
<dd> Create Fortran subroutine wrappers to Fortran 77 functions. &#8211;wrap-functions is default because it ensures maximum portability/compiler independence.</dd>
<dt><code>&#8211;help-link [..]</code></dt>
<dd> List system resources found by system_info.py. [..] may contain a list of resources names. See also &#8211;link-&lt;resource&gt; switch below.</dd>
<dt><code>&#8211;quiet</code></dt>
<dd> Run quietly.</dd>
<dt><code>&#8211;verbose</code></dt>
<dd> Run with extra verbosity.</dd>
<dt><code>-v</code></dt>
<dd> Print f2py version ID and exit.</dd>
<dt><code>&#8211;include_paths path1:path2:&#8230;</code></dt>
<dd> Search include files (that f2py will scan) from the given directories.</dd></dl>
<h2>CONFIG_FC OPTIONS</h2>
<p> The following options are effective only when -c switch is used.</p>
<dl>
<dt><code>&#8211;help-compiler</code></dt>
<dd> List available Fortran compilers [DEPRECIATED].</dd>
<dt><code>&#8211;fcompiler=&lt;name&gt;</code></dt>
<dd> Specify Fortran compiler type by vendor.</dd>
<dt><code>&#8211;compiler=&lt;name&gt;</code></dt>
<dd> Specify C compiler type (as defined by distutils)</dd>
<dt><code>&#8211;fcompiler-exec=&lt;path&gt;</code></dt>
<dd> Specify the path to F77 compiler [DEPRECIATED].</dd>
<dt><code>&#8211;f90compiler-exec=&lt;path&gt;</code></dt>
<dd> Specify the path to F90 compiler [DEPRECIATED].</dd>
<dt><code>&#8211;help-fcompiler</code></dt>
<dd> List available Fortran compilers and exit.</dd>
<dt><code>&#8211;f77exec=&lt;path&gt;</code></dt>
<dd> Specify the path to F77 compiler.</dd>
<dt><code>&#8211;f90exec=&lt;path&gt;</code></dt>
<dd> Specify the path to F90 compiler.</dd>
<dt><code>&#8211;f77flags=&#8230;</code></dt>
<dd> Specify F77 compiler flags.</dd>
<dt><code>&#8211;f90flags=&#8230;</code></dt>
<dd> Specify F90 compiler flags.</dd>
<dt><code>&#8211;opt=&#8230;</code></dt>
<dd> Specify optimization flags.</dd>
<dt><code>&#8211;arch=&#8230;</code></dt>
<dd> Specify architecture specific optimization flags.</dd>
<dt><code>&#8211;noopt</code></dt>
<dd> Compile without optimization.</dd>
<dt><code>&#8211;noarch</code></dt>
<dd> Compile without arch-dependent optimization.</dd>
<dt><code>&#8211;debug</code></dt>
<dd> Compile with debugging information.</dd></dl>
<h2>EXTRA OPTIONS</h2>
<p> The following options are effective only when -c switch is used.</p>
<dl>
<dt><code>&#8211;link-&lt;resource&gt; </code></dt>
<dd> Link extension module with &lt;resource&gt; as defined by numpy_distutils/system_info.py. E.g. to link with optimized LAPACK libraries (vecLib on MacOSX, ATLAS elsewhere), use &#8211;link-lapack_opt. See also &#8211;help-link switch. </dd>
<dt><code>-L/path/to/lib/ -l&lt;libname&gt;</code></dt>
<dd>
</dd><dt><code>-D&lt;define&gt; -U&lt;name&gt; -I/path/to/include/ </code></dt>
<dd>
</dd><dt><code>&lt;filename&gt;.o &lt;filename&gt;.so &lt;filename&gt;.a</code></dt>
<dd>
</dd><dt><code>-DPREPEND_FORTRAN -DNO_APPEND_FORTRAN -DUPPERCASE_FORTRAN -DUNDERSCORE_G77</code></dt>
<dd> Macros that might be required with non-gcc Fortran compilers. </dd>
<dt><code>-DF2PY_REPORT_ATEXIT</code></dt>
<dd> To print out a performance report of F2PY interface when python exits. Available for Linux. </dd>
<dt><code>-DF2PY_REPORT_ON_ARRAY_COPY=&lt;int&gt;</code></dt>
<dd> To send a message to stderr whenever F2PY interface makes a copy of an array. Integer &lt;int&gt; sets the threshold for array sizes when a message should be shown. </dd>
</dl>
<h2>REQUIREMENTS</h2>
<p> Python 1.5.2 or higher (2.x is supported). </p>
<p> Numerical Python 13 or higher (20.x,21.x,22.x,23.x are supported). </p>
<p> Optional Numarray 0.9 or higher partially supported. </p>
<p> numpy_distutils from Scipy (can be downloaded from F2PY homepage)</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-python/">python</a>(1)</p>
<h2>BUGS</h2>
<p> For instructions on reporting bugs, see </p>
<p>&nbsp;<wbr>&nbsp;<a rel="nofollow" href="http://cens.ioc.ee/projects/f2py2e/FAQ.html">http://cens.ioc.ee/projects/f2py2e/FAQ.html</a></p>
<h2>AUTHOR</h2>
<p> Pearu Peterson &lt;pearu [at] cens.ioc.ee&gt;</p>
<h2>INTERNET RESOURCES</h2>
<p> Main website: <a rel="nofollow" href="http://cens.ioc.ee/projects/f2py2e/">http://cens.ioc.ee/projects/f2py2e/</a> </p>
<p> User&#8217;s Guide: <a rel="nofollow" href="http://cens.ioc.ee/projects/f2py2e/usersguide/">http://cens.ioc.ee/projects/f2py2e/usersguide/</a> </p>
<p> Mailing list: <a rel="nofollow" href="http://cens.ioc.ee/mailman/listinfo/f2py-users/">http://cens.ioc.ee/mailman/listinfo/f2py-users/</a> </p>
<p> Scipy website: <a rel="nofollow" href="http://www.numpy.org">http://www.numpy.org</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1999, 2000, 2001, 2002, 2003, 2004, 2005 Pearu Peterson</p>
<h2>LICENSE</h2>
<p> NumPy License</p>
<h2>VERSION</h2>
<p> 2.45.241 </p>
