---
title: "imake(1)"
name: "imake"
section: "1"
letter: "i"
url: "/docs/linux/man/1-imake/"
description: "imake – C preprocessor interface to the make utility"
---

<h2>NAME</h2>
<p> imake &#8211; C preprocessor interface to the make utility</p>
<h2>SYNOPSIS</h2>
<p> <code>imake</code> [ <code>-D</code><i>define</i> ] [ <code>-I</code><i>dir</i> ] [ <code>-U</code><i>define</i> ] [ <code>-T</code><i>template</i> ] [ <code>-f</code> <i>filename</i> ] [ <code>-C</code> <i>filename</i> ] [ <code>-s</code> <i>filename</i> ] [ <code>-e</code> ] [ <code>-v</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Imake</i> is used to generate <i>Makefiles</i> from a template, a set of <i>cpp</i> macro functions, and a per-directory input file called an <i>Imakefile</i>. This allows machine dependencies (such as compiler options, alternate command names, and special <i>make</i> rules) to be kept separate from the descriptions of the various items to be built.</p>
<h2>OPTIONS</h2>
<p> The following command line options may be passed to <i>imake</i>:</p>
<dl>
<dt><code>-D</code><i>define</i></p>
<dd> This option is passed directly to <i>cpp</i>. It is typically used to set directory-specific variables. For example, the X Window System used this flag to set <i>TOPDIR</i> to the name of the directory containing the top of the core distribution and <i>CURDIR</i> to the name of the current directory, relative to the top.</p>
<dt><code>-I</code><i>directory</i></p>
<dd> This option is passed directly to <i>cpp</i>. It is typically used to indicate the directory in which the <i>imake</i> template and configuration files may be found.</p>
<dt><code>-U</code><i>define</i></p>
<dd> This option is passed directly to <i>cpp</i>. It is typically used to unset variables when debugging <i>imake</i> configuration files.</p>
<dt><code>-T</code><i>template</i></p>
<dd> This option specifies the name of the master template file (which is usually located in the directory specified with <i>-I</i>) used by <i>cpp</i>. The default is <i>Imake.tmpl</i>.</p>
<dt><code>-f </code><i>filename</i></p>
<dd> This option specifies the name of the per-directory input file. The default is <i>Imakefile</i>.</p>
<dt><code>-C </code><i>filename</i></p>
<dd> This option specifies the name of the .c file that is constructed in the current directory. The default is <i>Imakefile.c</i>.</p>
<dt><code>-s </code><i>filename</i></p>
<dd> This option specifies the name of the <i>make</i> description file to be generated but <i>make</i> should not be invoked. If the <i>filename</i> is a dash (-), the output is written to <i>stdout</i>. The default is to generate, but not execute, a <i>Makefile</i>.</p>
<dt><code>-e</code></p>
<dd> This option indicates the <i>imake</i> should execute the generated <i>Makefile</i>. The default is to leave this to the user.</p>
<dt><code>-v</code></p>
<dd> This option indicates that <i>imake</i> should print the <i>cpp</i> command line that it is using to generate the <i>Makefile</i>.</dl>
<h2>HOW IT WORKS</h2>
<p> <i>Imake</i> invokes <i>cpp</i> with any <i>-I</i> or <i>-D</i> flags passed on the command line and passes the name of a file containing the following 3 lines: </p>
<pre><code>
#define IMAKE_TEMPLATE "Imake.tmpl"
#define INCLUDE_IMAKEFILE &lt;Imakefile&gt;
#include IMAKE_TEMPLATE
</code></pre>
<p> where <i>Imake.tmpl</i> and <i>Imakefile</i> may be overridden by the <i>-T</i> and <i>-f</i> command options, respectively. </p>
<p> The IMAKE_TEMPLATE typically reads in a file containing machine-dependent parameters (specified as <i>cpp</i> symbols), a site-specific parameters file, a file defining variables, a file containing <i>cpp</i> macro functions for generating <i>make</i> rules, and finally the <i>Imakefile</i> (specified by INCLUDE_IMAKEFILE) in the current directory. The <i>Imakefile</i> uses the macro functions to indicate what targets should be built; <i>imake</i> takes care of generating the appropriate rules. </p>
<p> <i>Imake</i> configuration files contain two types of variables, imake variables and make variables. The imake variables are interpreted by cpp when <i>imake</i> is run. By convention they are mixed case. The make variables are written into the <i>Makefile</i> for later interpretation by <i>make.</i> By convention make variables are upper case. </p>
<p> The rules file (usually named <i>Imake.rules</i> in the configuration directory) contains a variety of <i>cpp</i> macro functions that are configured according to the current platform. <i>Imake</i> replaces any occurrences of the string &#8220;@@&#8221; with a newline to allow macros that generate more than one line of <i>make</i> rules. For example, the macro </p>
<pre><code>
#define program_target(program, objlist) @ @program : objlist @ @$(CC) - o $ @objlist $(LDFLAGS)
</code></pre>
<p> when called with <i>program_target(foo, foo1.o foo2.o)</i> will expand to </p>
<pre>
 foo:     foo1.o  foo2.o
          $(CC)  -o  $@  foo1.o  foo2.o  $(LDFLAGS)
</pre>
<p> <i>Imake</i> also replaces any occurrences of the word &#8220;XCOMM&#8221; with the character &#8220;#&#8221; to permit placing comments in the Makefile without causing &#8220;invalid directive&#8221; errors from the preprocessor. </p>
<p> Some complex <i>imake</i> macros require generated <i>make</i> variables local to each invocation of the macro, often because their value depends on parameters passed to the macro. Such variables can be created by using an <i>imake</i> variable of the form <code>XVARdef</code><i>n</i>, where <i>n</i> is a single digit. A unique <i>make</i> variable will be substituted. Later occurrences of the variable <code>XVARuse</code><i>n</i> will be replaced by the variable created by the corresponding <code>XVARdef</code><i>n</i>. </p>
<p> On systems whose <i>cpp</i> reduces multiple tabs and spaces to a single space, <i>imake</i> attempts to put back any necessary tabs (<i>make</i> is very picky about the difference between tabs and spaces). For this reason, colons (:) in command lines must be preceded by a backslash (\).</p>
<h2>USE WITH THE X WINDOW SYSTEM</h2>
<p> The X Window System used <i>imake</i> extensively up through the X11R6.9 release, for both full builds within the source tree and external software. X has since moved to GNU autoconf and automake for its build system in X11R7.0 and later releases, but still maintains imake for building existing external software programs that have not yet converted. </p>
<p> As mentioned above, two special variables, <i>TOPDIR</i> and <i>CURDIR,</i> are set to make referencing files using relative path names easier. For example, the following command is generated automatically to build the <i>Makefile</i> in the directory <i>lib/X/</i> (relative to the top of the sources): </p>
<pre>
          %  ../.././config/imake  -I../.././config  \
                -DTOPDIR=../../.   -DCURDIR=./lib/X
</pre>
<p> When building X programs outside the source tree, a special symbol <i>UseInstalled</i> is defined and <i>TOPDIR</i> and <i>CURDIR</i> are omitted. If the configuration files have been properly installed, the script <i><a href="/docs/linux/man/1-xmkmf/">xmkmf</a></i>(1) may be used.</p>
<h2>INPUT FILES</h2>
<p> Here is a summary of the files read by <i>imake</i> as used by X. The indentation shows what files include what other files. </p>
<pre>
    Imake.tmpl                generic variables
        site.def              site-specific, BeforeVendorCF defined
        *.cf                  machine-specific
            *Lib.rules        shared library rules
        site.def              site-specific, AfterVendorCF defined
        Imake.rules           rules
        Project.tmpl          X-specific variables
            *Lib.tmpl         shared library variables
        Imakefile
            Library.tmpl      library rules
            Server.tmpl       server rules
            Threads.tmpl      multi-threaded rules
</pre>
<p> Note that <i>site.def</i> gets included twice, once before the <i>*.cf</i> file and once after. Although most site customizations should be specified after the <i>*.cf</i> file, some, such as the choice of compiler, need to be specified before, because other variable settings may depend on them. </p>
<p> The first time <i>site.def</i> is included, the variable BeforeVendorCF is defined, and the second time, the variable AfterVendorCF is defined. All code in <i>site.def</i> should be inside an #ifdef for one of these symbols.</p>
<h2>FILES</h2>
<p> Imakefile.c<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>temporary input file for cpp</p>
<p> /tmp/Imf.XXXXXX<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>temporary Makefile for -s</p>
<p> /tmp/IIf.XXXXXX<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>temporary Imakefile if specified Imakefile uses # comments</p>
<p> /usr/bin/cpp<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>default C preprocessor</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-make/">make</a>(1), <a href="/docs/linux/man/1-xmkmf/">xmkmf</a>(1)<br />
 Paul DuBois, <i>imake-Related Software and Documentation,</i> <a rel="nofollow" href="http://www.snake.net/software/imake-stuff/">http://www.snake.net/software/imake-stuff/</a><br />
 Paul DuBois, <i>Software Portability with imake, Second Edition,</i> O&#8217;Reilly &amp; Associates, 1996.<br />
 S. I. Feldman, <i>Make &#8212; A Program for Maintaining Computer Programs</i></p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variables may be set, however their use is not recommended as they introduce dependencies that are not readily apparent when <i>imake</i> is run:</p>
<dl>
<dt><code>IMAKEINCLUDE</code></p>
<dd> If defined, this specifies a &#8220;-I&#8221; include argument to pass to the C preprocessor. E.g., &#8220;-I/usr/X11/config&#8221;.</p>
<dt><code>IMAKECPP</code></p>
<dd> If defined, this should be a valid path to a preprocessor program. E.g., &#8220;/usr/local/cpp&#8221;. By default, <i>imake</i> will use cc -E or /usr/bin/cpp, depending on the OS specific configuration.</p>
<dt><code>IMAKEMAKE</code></p>
<dd> If defined, this should be a valid path to a make program, such as &#8220;/usr/local/make&#8221;. By default, <i>imake</i> will use whatever <i>make</i> program is found using <i><a href="/docs/linux/man/3-execvp/">execvp</a>(3).</i> This variable is only used if the &#8220;-e&#8221; option is specified.</dl>
<h2>AUTHOR</h2>
<p> Todd Brunhoff, Tektronix and MIT Project Athena; Jim Fulton, MIT X Consortium </p>
<h2>Index</h2>
