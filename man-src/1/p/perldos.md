---
title: "perldos(1)"
name: "perldos"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perldos/"
description: "perldos – Perl under DOS, W31, W95."
---

<h2 class="name">NAME</h2>
<p> perldos &#8211; Perl under DOS, W31, W95. </p>
<h2>SYNOPSIS</h2>
<p> These are instructions for building Perl under <font SIZE="-1">DOS</font> (or w??), using <font SIZE="-1">DJGPP</font> v2.03 or later. Under w95 long filenames are supported.</p>
<h2>DESCRIPTION</h2>
<p> Before you start, you should glance through the <font SIZE="-1">README</font> file found in the top-level directory where the Perl distribution was extracted. Make sure you read and understand the terms under which this software is being distributed. </p>
<p> This port currently supports MakeMaker (the set of modules that is used to build extensions to perl). Therefore, you should be able to build and install most extensions found in the <font SIZE="-1">CPAN</font> sites. </p>
<p> Detailed instructions on how to build and install perl extension modules, including XS-type modules, is included. See &#8216;<font SIZE="-1">BUILDING AND INSTALLING MODULES</font>&#8216;.</p>
<h3>Prerequisites for Compiling Perl on <font SIZE="-1">DOS</font></h3>
<dl>
<dt><font SIZE="-1">DJGPP</font></p>
<dd> <font SIZE="-1">DJGPP</font> is a port of <font SIZE="-1">GNU C/C<font SIZE="-2">++</font></font> compiler and development tools to 32-bit, protected-mode environment on Intel 32-bit CPUs running MS-DOS and compatible operating systems, by <font SIZE="-1">DJ</font> Delorie &lt;dj [at] delorie.com&gt; and friends. </p>
<p> For more details (<font SIZE="-1">FAQ</font>), check out the home of <font SIZE="-1">DJGPP</font> at: </p>
<pre>
        <a rel="nofollow" href="http://www.delorie.com/djgpp/">http://www.delorie.com/djgpp/</a>
</pre>
<p> If you have questions about <font SIZE="-1">DJGPP,</font> try posting to the <font SIZE="-1">DJGPP</font> newsgroup: comp.os.msdos.djgpp, or use the email gateway djgpp [at] delorie.com. </p>
<p> You can find the full <font SIZE="-1">DJGPP</font> distribution on any of the mirrors listed here: </p>
<pre>
        <a rel="nofollow" href="http://www.delorie.com/djgpp/getting.html">http://www.delorie.com/djgpp/getting.html</a>
</pre>
<p> You need the following files to build perl (or add new modules): </p>
<pre>
        v2/djdev203.zip
        v2gnu/bnu2112b.zip
        v2gnu/gcc2953b.zip
        v2gnu/bsh204b.zip
        v2gnu/mak3791b.zip
        v2gnu/fil40b.zip
        v2gnu/sed3028b.zip
        v2gnu/txt20b.zip
        v2gnu/dif272b.zip
        v2gnu/grep24b.zip
        v2gnu/shl20jb.zip
        v2gnu/gwk306b.zip
        v2misc/csdpmi5b.zip
</pre>
<p> or possibly any newer version.</p>
<dt>Pthreads</p>
<dd> Thread support is not tested in this version of the djgpp perl.</dl>
<h3>Shortcomings of Perl under <font SIZE="-1">DOS</font></h3>
<p> Perl under <font SIZE="-1">DOS</font> lacks some features of perl under <font SIZE="-1">UNIX</font> because of deficiencies in the UNIX-emulation, most notably:</p>
<dl>
<dt>&bull;</p>
<dd> <code>fork()</code> and <code>pipe()</code></p>
<dt>&bull;</p>
<dd> some features of the <font SIZE="-1">UNIX</font> filesystem regarding link count and file dates</p>
<dt>&bull;</p>
<dd> in-place operation is a little bit broken with short filenames</p>
<dt>&bull;</p>
<dd> sockets</dl>
<h3>Building Perl on <font SIZE="-1">DOS</font></h3>
<dl>
<dt>&bull;</p>
<dd> Unpack the source package <i>perl5.8*.tar.gz</i> with djtarx. If you want to use long file names under w95 and also to get Perl to pass all its tests, don&#8217;t forget to use </p>
<pre>
        set LFN=y
        set FNCASE=y
</pre>
<p> before unpacking the archive.</p>
<dt>&bull;</p>
<dd> Create a &#8220;symlink&#8221; or copy your bash.exe to sh.exe in your <tt>&quot;($DJDIR)/bin&quot;</tt> directory. </p>
<pre>
        ln -s bash.exe sh.exe
</pre>
<p> [If you have the recommended version of bash for <font SIZE="-1">DJGPP,</font> this is already done for you.] </p>
<p> And make the <tt>&quot;SHELL&quot;</tt> environment variable point to this <i>sh.exe</i>: </p>
<pre>
        set SHELL=c:/djgpp/bin/sh.exe (use full path name!)
</pre>
<p> You can do this in <i>djgpp.env</i> too. Add this line <font SIZE="-1">BEFORE</font> any section definition: </p>
<pre>
        +SHELL=%DJDIR%/bin/sh.exe
</pre>
<dt>&bull;</p>
<dd> If you have <i>split.exe</i> and <i>gsplit.exe</i> in your path, then rename <i>split.exe</i> to <i>djsplit.exe</i>, and <i>gsplit.exe</i> to <i>split.exe</i>. Copy or link <i>gecho.exe</i> to <i>echo.exe</i> if you don&#8217;t have <i>echo.exe</i>. Copy or link <i>gawk.exe</i> to <i>awk.exe</i> if you don&#8217;t have <i>awk.exe</i>. </p>
<p> [If you have the recommended versions of djdev, shell utilities and gawk, all these are already done for you, and you will not need to do anything.]</p>
<dt>&bull;</p>
<dd> Chdir to the djgpp subdirectory of perl toplevel and type the following commands: </p>
<pre>
        set FNCASE=y
        configure.bat
</pre>
<p> This will do some preprocessing then run the Configure script for you. The Configure script is interactive, but in most cases you just need to press <font SIZE="-1">ENTER.</font> The &#8220;set&#8221; command ensures that <font SIZE="-1">DJGPP</font> preserves the letter case of file names when reading directories. If you already issued this set command when unpacking the archive, and you are in the same <font SIZE="-1">DOS</font> session as when you unpacked the archive, you don&#8217;t have to issue the set command again. This command is necessary *before* you start to (re)configure or (re)build perl in order to ensure both that perl builds correctly and that building XS-type modules can succeed. See the <font SIZE="-1">DJGPP</font> info entry for &#8220;_preserve_fncase&#8221; for more information: </p>
<pre>
        info libc alphabetical _preserve_fncase
</pre>
<p> If the script says that your package is incomplete, and asks whether to continue, just answer with Y (this can only happen if you don&#8217;t use long filenames or forget to issue &#8220;set FNCASE=y&#8221; first). </p>
<p> When Configure asks about the extensions, I suggest <font SIZE="-1">IO</font> and Fcntl, and if you want database handling then SDBM_File or GDBM_File (you need to install gdbm for this one). If you want to use the <font SIZE="-1">POSIX</font> extension (this is the default), make sure that the stack size of your <i>cc1.exe</i> is at least 512kbyte (you can check this with: <tt>&quot;stubedit cc1.exe&quot;</tt>). </p>
<p> You can use the Configure script in non-interactive mode too. When I built my <i>perl.exe</i>, I used something like this: </p>
<pre>
        configure.bat -des
</pre>
<p> You can find more info about Configure&#8217;s command line switches in the <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file. </p>
<p> When the script ends, and you want to change some values in the generated <i>config.sh</i> file, then run </p>
<pre>
        sh Configure -S
</pre>
<p> after you made your modifications. </p>
<p> <font SIZE="-1">IMPORTANT:</font> if you use this <tt>&quot;-S&quot;</tt> switch, be sure to delete the <font SIZE="-1">CONFIG</font> environment variable before running the script: </p>
<pre>
        set CONFIG=
</pre>
<dt>&bull;</p>
<dd> Now you can compile Perl. Type: </p>
<pre>
        make
</pre>
</dl>
<h3>Testing Perl on <font SIZE="-1">DOS</font></h3>
<p> Type: </p>
<pre>
        make test
</pre>
<p> If you&#8217;re lucky you should see &#8220;All tests successful&#8221;. But there can be a few failed subtests (less than 5 hopefully) depending on some external conditions (e.g. some subtests fail under linux/dosemu or plain dos with short filenames only).</p>
<h3>Installation of Perl on <font SIZE="-1">DOS</font></h3>
<p> Type: </p>
<pre>
        make install
</pre>
<p> This will copy the newly compiled perl and libraries into your <font SIZE="-1">DJGPP</font> directory structure. Perl.exe and the utilities go into <tt>&quot;($DJDIR)/bin&quot;</tt>, and the library goes under <tt>&quot;($DJDIR)/lib/perl5&quot;</tt>. The pod documentation goes under <tt>&quot;($DJDIR)/lib/perl5/pod&quot;</tt>.</p>
<h2>BUILDING AND INSTALLING MODULES ON DOS</h2>
<h3>Building Prerequisites for Perl on <font SIZE="-1">DOS</font></h3>
<p> For building and installing non-XS modules, all you need is a working perl under <font SIZE="-1">DJGPP.</font> Non-XS modules do not require re-linking the perl binary, and so are simpler to build and install. </p>
<p> XS-type modules do require re-linking the perl binary, because part of an <font SIZE="-1">XS</font> module is written in &#8220;C&#8221;, and has to be linked together with the perl binary to be executed. This is required because perl under <font SIZE="-1">DJGPP</font> is built with the &#8220;static link&#8221; option, due to the lack of &#8220;dynamic linking&#8221; in the <font SIZE="-1">DJGPP</font> environment. </p>
<p> Because <font SIZE="-1">XS</font> modules require re-linking of the perl binary, you need both the perl binary distribution and the perl source distribution to build an <font SIZE="-1">XS</font> extension module. In addition, you will have to have built your perl binary from the source distribution so that all of the components of the perl binary are available for the required link step.</p>
<h3>Unpacking <font SIZE="-1">CPAN</font> Modules on <font SIZE="-1">DOS</font></h3>
<p> First, download the module package from <font SIZE="-1">CPAN</font> (e.g., the &#8220;Comma Separated Value&#8221; text package, Text-CSV-0.01.tar.gz). Then expand the contents of the package into some location on your disk. Most <font SIZE="-1">CPAN</font> modules are built with an internal directory structure, so it is usually safe to expand it in the root of your <font SIZE="-1">DJGPP</font> installation. Some people prefer to locate source trees under /usr/src (i.e., <tt>&quot;($DJDIR)/usr/src&quot;</tt>), but you may put it wherever seems most logical to you, *EXCEPT* under the same directory as your perl source code. There are special rules that apply to modules which live in the perl source tree that do not apply to most of the modules in <font SIZE="-1">CPAN.</font> </p>
<p> Unlike other <font SIZE="-1">DJGPP</font> packages, which are normal &#8220;zip&#8221; files, most <font SIZE="-1">CPAN</font> module packages are &#8220;gzipped tarballs&#8221;. Recent versions of WinZip will safely unpack and expand them, *UNLESS* they have zero-length files. It is a known WinZip bug (as of v7.0) that it will not extract zero-length files. </p>
<p> From the command line, you can use the djtar utility provided with <font SIZE="-1">DJGPP</font> to unpack and expand these files. For example: </p>
<pre>
        C:\djgpp&gt;djtarx -v Text-CSV-0.01.tar.gz
</pre>
<p> This will create the new directory <tt>&quot;($DJDIR)/Text-CSV-0.01&quot;</tt>, filling it with the source for this module.</p>
<h3>Building Non-XS Modules on <font SIZE="-1">DOS</font></h3>
<p> To build a non-XS module, you can use the standard module-building instructions distributed with perl modules. </p>
<pre>
    perl Makefile.PL
    make
    make test
    make install
</pre>
<p> This is sufficient because non-XS modules install only &#8220;.pm&#8221; files and (sometimes) pod and/or man documentation. No re-linking of the perl binary is needed to build, install or use non-XS modules.</p>
<h3>Building <font SIZE="-1">XS</font> Modules on <font SIZE="-1">DOS</font></h3>
<p> To build an <font SIZE="-1">XS</font> module, you must use the standard module-building instructions distributed with perl modules *PLUS* three extra instructions specific to the <font SIZE="-1">DJGPP</font> &#8220;static link&#8221; build environment. </p>
<pre>
    set FNCASE=y
    perl Makefile.PL
    make
    make perl
    make test
    make -f Makefile.aperl inst_perl MAP_TARGET=perl.exe
    make install
</pre>
<p> The first extra instruction sets <font SIZE="-1">DJGPP</font>&#8216;s <font SIZE="-1">FNCASE</font> environment variable so that the new perl binary which you must build for an XS-type module will build correctly. The second extra instruction re-builds the perl binary in your module directory before you run &#8220;make test&#8221;, so that you are testing with the new module code you built with &#8220;make&#8221;. The third extra instruction installs the perl binary from your module directory into the standard <font SIZE="-1">DJGPP</font> binary directory, <tt>&quot;($DJDIR)/bin&quot;</tt>, replacing your previous perl binary. </p>
<p> Note that the <font SIZE="-1">MAP_TARGET</font> value *must* have the &#8220;.exe&#8221; extension or you will not create a &#8220;perl.exe&#8221; to replace the one in <tt>&quot;($DJDIR)/bin&quot;</tt>. </p>
<p> When you are done, the XS-module install process will have added information to your &#8220;perllocal&#8221; information telling that the perl binary has been replaced, and what module was installed. You can view this information at any time by using the command: </p>
<pre>
        perl -S perldoc perllocal
</pre>
<h2>AUTHOR</h2>
<p> Laszlo Molnar, <i>laszlo.molnar [at] eth.ericsson.se</i> [Installing/building perl] </p>
<p> Peter J. Farley <font SIZE="-1">III</font> <i>pjfarley [at] banet.net</i> [Building/installing modules]</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1). </p>
<h2>Index</h2>
<dt><a href="#lbAJ">BUILDING AND INSTALLING MODULES ON DOS</a></p>
<dd>
<dt><a href="#lbAO">AUTHOR</a></p>
<dd>
<dt><a href="#lbAP">SEE ALSO</a></p>
<dd></dl>
