---

title: "mkoctfile(1)"
name: "mkoctfile"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkoctfile/"
description: "mkoctfile – Compile dynamic-load modules for GNU Octave"
---

<h2>NAME</h2>
<p> mkoctfile &#8211; Compile dynamic-load modules for GNU Octave</p>
<p> <code>mkoctfile</code> [<i>OPTION</i>]&#8230; file&#8230;</p>
<p> <code>mkoctfile</code> is used to compile C, C++, or Fortran source code in to a dynamically loadable <i>.oct</i> file for <code><a href="/docs/linux/man/1-octave/">octave</a></code>(1).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></dt>
<dd> Print help message.</dd>
<dt><code>-I</code><i>dir</i></dt>
<dd> Add include directory <i>dir</i> to compile commands.</dd>
<dt><code>-idirafter</code><i>dir</i></dt>
<dd> Add include directory to second include search path after &#8216;<code>-I</code>&#8216;.</dd>
<dt><code>-D</code><i>def</i></dt>
<dd> Add definition <i>def</i> to compiler command.</dd>
<dt><code>-l</code><i>lib</i></dt>
<dd> Add library <i>lib</i> to link command.</dd>
<dt><code>-L</code><i>dir</i></dt>
<dd> Add library directory <i>dir</i> to link command.</dd>
<dt><code>-R</code><i>dir</i></dt>
<dd> Pass <code>-R</code><i>dir</i> to link command.</dd>
<dt><code>-g</code></dt>
<dd> Enable debugging option for all compilers.</dd>
<dt><code>-pthread</code></dt>
<dd> Add <code>-pthread</code> to link command.</dd>
<dt><code>-W&#8230;</code></dt>
<dd> Pass flags to the compiler such as <code>-Wa,</code><i>OPTION</i>.</dd>
<dt><code>-Wl,&#8230;</code></dt>
<dd> Pass flags to the linker such as <code>-Wl,-rpath=&#8230;</code></dd>
<dt><code>-M</code>,<code> &#8211;depend</code></dt>
<dd> Generate dependency files (.d) for C and C++ source files.</dd>
<dt><code>-c</code></dt>
<dd> Compile but do not link.</dd>
<dt><code>&#8211;link-stand-alone</code></dt>
<dd> Link a stand-alone executable file.</dd>
<dt><code>-s</code>,<code> &#8211;strip</code></dt>
<dd> Strip the output file.</dd>
<dt><code>&#8211;mex</code></dt>
<dd> Create a MEX file. Set the default output extension to <code>.mex</code>.</dd>
<dt><code>-o </code><i>file</i>,<code> &#8211;output </code><i>file</i></dt>
<dd> Output file name. Default extension is <code>.oct</code> (or <code>.mex</code> if &#8211;mex is specified) unless linking a stand-alone executable.</dd>
<dt><code>-p </code><i>VAR</i>,<code> &#8211;print </code><i>VAR</i></dt>
<dd> Print configuration variable <i>VAR</i>. Recognized variables are:</dd>
<dl>
<dt>
</dt><dd>
<pre>
    ALL_CFLAGS                FFTW3F_LDFLAGS
    ALL_CXXFLAGS              FFTW3F_LIBS
    ALL_FFLAGS                FLIBS
    ALL_LDFLAGS               FPICFLAG
    AR                        INCFLAGS
    BLAS_LIBS                 LAPACK_LIBS
    CC                        LDFLAGS
    CFLAGS                    LD_CXX
    CPICFLAG                  LD_STATIC_FLAG
    CPPFLAGS                  LFLAGS
    CXX                       LIBOCTAVE
    CXXFLAGS                  LIBOCTINTERP
    CXXPICFLAG                LIBS
    DEPEND_EXTRA_SED_PATTERN  OCTAVE_LIBS
    DEPEND_FLAGS              OCTAVE_LINK_DEPS
    DL_LD                     OCT_LINK_DEPS
    DL_LDFLAGS                RANLIB
    EXEEXT                    RDYNAMIC_FLAG
    F77                       READLINE_LIBS
    F77_INTEGER_8_FLAG        SED
    FFLAGS                    XTRA_CFLAGS
    FFTW3_LDFLAGS             XTRA_CXXFLAGS
    FFTW3_LIBS
</pre>
</dd></dl>
<dt><code>-v</code>,<code> &#8211;verbose</code></dt>
<dd> Echo commands as they are executed.</dd>
<dt><code>file</code></dt>
<dd> Compile or link file. Recognized file types are</dd>
<dl>
<dt>
</dt><dd>
<pre>
   .c    C source
   .cc   C++ source
   .C    C++ source
   .cpp  C++ source
   .f    Fortran source (fixed form)
   .F    Fortran source (fixed form)
   .f90  Fortran source (free form)
   .F90  Fortran source (free form)
   .o    object file
   .a    library file
</pre>
</dd></dl>
</dl>
<h2>AUTHOR</h2>
<p> John W. Eaton &lt;jwe [at] octave.org&gt; </p>
<p> This manual page was contributed by Dirk Eddelbuettel &lt;edd [at] debian.org&gt; for the Debian GNU/Linux distribution but may be used by others.</p>
<h2>SEE ALSO</h2>
<p> octave (1). </p>
