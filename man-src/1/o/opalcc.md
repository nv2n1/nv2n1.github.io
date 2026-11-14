---
title: "opalcc(1)"
name: "opalcc"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opalcc/"
description: "opalcc — Open PAL C wrapper compiler"
---

<h2 class="name">NAME</h2>
<p> opalcc &#8212; Open PAL C wrapper compiler </p>
<h2>SYNTAX</h2>
<p> opalcc [-showme|-showme:compile|-showme:link] &#8230;</p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;showme</p>
<dd> This option comes in several different variants (see below). None of the variants invokes the underlying compiler; they all provide information on how the underlying compiler would have been invoked had <i>&#8211;showme</i> not been used. The basic <i>&#8211;showme</i> option outputs the command line that would be executed to compile the program. <code>NOTE:</code> If a non-filename argument is passed on the command line, the <i>-showme</i> option will <i>not</i> display any additional flags. For example, both &quot;opalcc &#8211;showme&quot; and &quot;opalcc &#8211;showme my_source.c&quot; will show all the wrapper-supplied flags. But &quot;opalcc &#8211;showme -v&quot; will only show the underlying compiler name and &quot;-v&quot;.</p>
<dt>&#8211;showme:compile</p>
<dd> Output the compiler flags that would have been supplied to the C compiler.</p>
<dt>&#8211;showme:link</p>
<dd> Output the linker flags that would have been supplied to the C compiler.</p>
<dt>&#8211;showme:command</p>
<dd> Outputs the underlying C compiler command (which may be one or more tokens).</p>
<dt>&#8211;showme:incdirs</p>
<dd> Outputs a space-delimited (but otherwise undecorated) list of directories that the wrapper compiler would have provided to the underlying C compiler to indicate where relevant header files are located.</p>
<dt>&#8211;showme:libdirs</p>
<dd> Outputs a space-delimited (but otherwise undecorated) list of directories that the wrapper compiler would have provided to the underlying linker to indicate where relevant libraries are located.</p>
<dt>&#8211;showme:libs</p>
<dd> Outputs a space-delimited (but otherwise undecorated) list of library names that the wrapper compiler would have used to link an application. For example: &quot;mpi open-rte open-pal util&quot;.</p>
<dt>&#8211;showme:version</p>
<dd> Outputs the version number of Open MPI.</p>
<dt>&#8211;showme:help</p>
<dd> Output a brief usage help message.</dl>
<p> See the man page for your underlying C compiler for other options that can be passed through opalcc.</p>
<h2>DESCRIPTION</h2>
<p> Conceptually, the role of these commands is quite simple: transparently add relevant compiler and linker flags to the user&#8217;s command line that are necessary to compile / link Open PAL programs, and then invoke the underlying compiler to actually perform the command. </p>
<p> As such, these commands are frequently referred to as &quot;wrapper&quot; compilers because they do not actually compile or link applications themselves; they only add in command line flags and invoke the back-end compiler.</p>
<h3>Background</h3>
<p> Open MPI is comprised of three software layers: OPAL (Open Portable Access Layer), ORTE (Open Run-Time Environment), and OMPI (Open MPI). There are wrapper compilers for each layer; each layer&#8217;s wrapper only links in the libraries relevant for that layer. Specifically, each layer provides the following wrapper compilers:</p>
<dl>
<dt>OPAL</p>
<dd> <i>opalcc</i> and <i>opalc++</i></p>
<dt>ORTE</p>
<dd> <i>ortecc</i> and <i>ortec++</i></p>
<dt>OMPI</p>
<dd> <i>mpicc</i>, <i>mpic++</i>, <i>mpicxx</i>, <i>mpiCC</i> (only on systems with case-senstive file systems), and <i>mpifort</i> (and its legacy/deprecated names <i>mpif77</i> and <i>mpif90</i>). Note that <i>mpic++</i>, <i>mpicxx</i>, and <i>mpiCC</i> all invoke the same underlying C++ compiler with the same options. All are provided as compatibility with other MPI implementations.</dl>
<h3>Fortran Notes</h3>
<p> The Fortran wrapper compiler for MPI (<i>mpifort</i>, and its legacy/deprecated names <i>mpif77</i> and <i>mpif90</i>) can compile and link MPI applications that use any/all of the MPI Fortran bindings: <i>mpif.h</i>, the <i>mpi</i> module, and the <i>mpi_f08</i> module (assuming Open MPI was installed with support for each of these Fortran bindings). Specifically: it is no longer necessary to use different wrapper compilers for applications that use <i>mpif.h</i> vs. applications that use the <i>mpi</i> module &#8212; just use <i>mpifort</i> for all Fortran MPI applications. </p>
<p> Note, however, that the Fortran compiler may require additional command-line options to enforce a specific Fortran dialect. For example, in some versions of the IBM XLF compiler, if xlf90 is the underlying Fortran compiler, <i>-qfixed</i> may be necessary to compile fixed-format Fortran source files. </p>
<p> Finally, note that <i>mpifort</i> will be inoperative and will return an error on use if Fortran support was not built into the MP Ilayer.</p>
<h3>Overview</h3>
<p> <i>opalcc</i> is a convenience wrappers for the underlying C compiler. Translation of an Open PAL program requires the linkage of the Open PAL-specific libraries which may not reside in one of the standard search directories of <a href="/docs/linux/man/1-ld/">ld</a>(1). It also often requires the inclusion of header files what may also not be found in a standard location. </p>
<p> <i>opalcc</i> passes its arguments to the underlying C compiler along with the -I, -L and -l options required by Open PAL programs. </p>
<p> The Open PAL Team <i>strongly</i> encourages using the wrapper compilers instead of attempting to link to the Open PAL libraries manually. This allows the specific implementation of Open PAL to change without forcing changes to linker directives in users&#8217; Makefiles. Indeed, the specific set of flags and libraries used by the wrapper compilers depends on how Open PAL was configured and built; the values can change between different installations of the same version of Open PAL. </p>
<p> Indeed, since the wrappers are simply thin shells on top of an underlying compiler, there are very, very few compelling reasons <i>not</i> to use <i>opalcc</i>. When it is not possible to use the wrappers directly, the <i>-showme:compile</i> and <i>-showme:link</i> options should be used to determine what flags the wrappers would have used. For example: </p>
<p> shell$ cc -c file1.c `mpicc -showme:compile` </p>
<p> shell$ cc -c file2.c `mpicc -showme:compile` </p>
<p> shell$ cc file1.o file2.o `mpicc -showme:link` -o my_mpi_program</p>
<h2>NOTES</h2>
<p> It is possible to make the wrapper compilers multi-lib aware. That is, the libraries and includes specified may differ based on the compiler flags specified (for example, with the GNU compilers on Linux, a different library path may be used if -m32 is seen versus -m64 being seen). This is not the default behavior in a standard build, but can be activated (for example, in a binary package providing both 32 and 64 bit support). More information can be found at: </p>
<p>&nbsp;<wbr>&nbsp;<a rel="nofollow" href="https://github.com/open-mpi/ompi/wiki/compilerwrapper3264">https://github.com/open-mpi/ompi/wiki/compilerwrapper3264</a></p>
<h2>FILES</h2>
<p> The string that the wrapper compilers insert into the command line before invoking the underlying compiler are stored in a text file created by Open PAL and installed to <i>$pkgdata/opalcc-wrapper-data.txt</i>, where <i>$pkgdata</i> is typically <i>$prefix/share/openmpi</i>, and <i>$prefix</i> is the top installation directory of Open PAL. </p>
<p> It is rarely necessary to edit this file, but it can be examined to gain insight into what flags the wrappers are placing on the command line.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> By default, the wrappers use the compilers that were selected when Open PAL was configured. These compilers were either found automatically by Open MPI&#8217;s &quot;configure&quot; script, or were selected by the user in the CC, CXX, F77, and/or FC environment variables before &quot;configure&quot; was invoked. Additionally, other arguments specific to the compiler may have been selected by configure. </p>
<p> These values can be selectively overridden by either editing the text files containing this configuration information (see the <code>FILES</code> section), or by setting selected environment variables of the form &quot;OPAL_value&quot;. </p>
<p> Valid value names are:</p>
<dl>
<dt>CPPFLAGS</p>
<dd> Flags added when invoking the preprocessor (C or C++)</p>
<dt>LDFLAGS</p>
<dd> Flags added when invoking the linker (C, C++, or Fortran)</p>
<dt>LIBS</p>
<dd> Libraries added when invoking the linker (C, C++, or Fortran)</p>
<dt>CC</p>
<dd> C compiler</p>
<dt>CFLAGS</p>
<dd> C compiler flags</p>
<dt>CXX</p>
<dd> C++ compiler</p>
<dt>CXXFLAGS</p>
<dd> C++ compiler flags</p>
<dt>FC</p>
<dd> Fortran compiler</p>
<dt>FCFLAGS</p>
<dd> Fortran compiler flags </p>
</dl>
<h2>Index</h2>
