---
title: "perlqnx(1)"
name: "perlqnx"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlqnx/"
---

<h2 class="name">NAME</h2>
 

 perlqnx - Perl version 5 on QNX 

<h2>DESCRIPTION</h2>

 As of perl5.7.2 all tests pass under: 

 <pre>
  QNX 4.24G
  Watcom 10.6 with Beta/970211.wcc.update.tar.F
  socket3r.lib Nov21 1996.
</pre> 

 As of perl5.8.1 there is at least one test still failing. 

 Some tests may complain under known circumstances. 

 See below and hints/qnx.sh for more information. 

 Under <font SIZE="-1">QNX 6.2.0</font> there are still a few tests which fail. See below and hints/qnx.sh for more information.

<h3>Required Software for Compiling Perl on <font SIZE="-1">QNX4</font></h3>

 As with many unix ports, this one depends on a few ``standard'' unix utilities which are not necessarily standard for <font SIZE="-1">QNX4.</font>
<dl>
<dt>/bin/sh
<dd> This is used heavily by Configure and then by perl itself. <font SIZE="-1">QNX4</font>'s version is fine, but Configure will choke on the 16-bit version, so if you are running <font SIZE="-1">QNX 4.22,</font> link /bin/sh to /bin32/ksh
<dt>ar
<dd> This is the standard unix library builder. We use wlib. With Watcom 10.6, when wlib is linked as ``ar'', it behaves like ar and all is fine. Under 9.5, a cover is required. One is included in ../qnx
<dt>nm
<dd> This is used (optionally) by configure to list the contents of libraries. I will generate a cover function on the fly in the <font SIZE="-1">UU</font> directory.
<dt>cpp
<dd> Configure and perl need a way to invoke a C preprocessor. I have created a simple cover for cc which does the right thing. Without this, Configure will create its own wrapper which works, but it doesn't handle some of the command line arguments that perl will throw at it.
<dt>make
<dd> You really need <font SIZE="-1">GNU</font> make to compile this. <font SIZE="-1">GNU</font> make ships by default with <font SIZE="-1">QNX 4.23,</font> but you can get it from quics for earlier versions.</dl>

<h3>Outstanding Issues with Perl on <font SIZE="-1">QNX4</font></h3>

 There is no support for dynamically linked libraries in <font SIZE="-1">QNX4.</font> 

 If you wish to compile with the Socket extension, you need to have the <font SIZE="-1">TCP/IP</font> toolkit, and you need to make sure that -lsocket locates the correct copy of socket3r.lib. Beware that the Watcom compiler ships with a stub version of socket3r.lib which has very little functionality. Also beware the order in which wlink searches directories for libraries. You may have /usr/lib/socket3r.lib pointing to the correct library, but wlink may pick up /usr/watcom/10.6/usr/lib/socket3r.lib instead. Make sure they both point to the correct library, that is, /usr/tcptk/current/usr/lib/socket3r.lib. 

 The following tests may report errors under <font SIZE="-1">QNX4:</font> 

 dist/Cwd/Cwd.t will complain if `pwd` and cwd don't give the same results. cwd calls `fullpath -t`, so if you cd `fullpath -t` before running the test, it will pass. 

 lib/File/Find/taint.t will complain if '.' is in your <font SIZE="-1">PATH.</font> The <font SIZE="-1">PATH</font> test is triggered because cwd calls `fullpath -t`. 

 ext/IO/lib/IO/t/io_sock.t: Subtests 14 and 22 are skipped due to the fact that the functionality to read back the non-blocking status of a socket is not implemented in <font SIZE="-1">QNX</font>'s <font SIZE="-1">TCP/IP.</font> This has been reported to <font SIZE="-1">QNX</font> and it may work with later versions of <font SIZE="-1">TCP/IP.</font> 

 t/io/tell.t: Subtest 27 is failing. We are still investigating.

<h3><font SIZE="-1">QNX</font> auxiliary files</h3>

 The files in the ``qnx'' directory are:
<dl>
<dt>qnx/ar
<dd> A script that emulates the standard unix archive (aka library) utility. Under Watcom 10.6, ar is linked to wlib and provides the expected interface. With Watcom 9.5, a cover function is required. This one is fairly crude but has proved adequate for compiling perl.
<dt>qnx/cpp
<dd> A script that provides C preprocessing functionality. Configure can generate a similar cover, but it doesn't handle all the command-line options that perl throws at it. This might be reasonably placed in /usr/local/bin.</dl>

<h3>Outstanding issues with perl under <font SIZE="-1">QNX6</font></h3>

 The following tests are still failing for Perl 5.8.1 under <font SIZE="-1">QNX 6.2.0:</font> 

 <pre>
  op/sprintf.........................FAILED at test 91
  lib/Benchmark......................FAILED at test 26
</pre> 

 This is due to a bug in the C library's printf routine. printf(``'%e''', 0. ) produces '0.000000e+0', but <font SIZE="-1">ANSI</font> requires '0.000000e+00'. <font SIZE="-1">QNX</font> has acknowledged the bug.

<h3>Cross-compilation</h3>

 Perl supports cross-compiling to <font SIZE="-1">QNX NTO</font> through the Native Development Kit (<font SIZE="-1">NDK</font>) for the Blackberry 10. This means that you can cross-compile for both <font SIZE="-1">ARM</font> and x86 versions of the platform. 

 <i>Setting up a cross-compilation environment</i> 

 You can download the <font SIZE="-1">NDK</font> from &lt;<a rel="nofollow" HREF="http://developer.blackberry.com/native/downloads/">http://developer.blackberry.com/native/downloads/</a>&gt;. 

 See &lt;<a rel="nofollow" HREF="http://developer.blackberry.com/native/documentation/cascades/getting_started/setting_up.html">http://developer.blackberry.com/native/documentation/cascades/getting_started/setting_up.html</a>&gt; for instructions to set up your device prior to attempting anything else. 

 Once you've installed the <font SIZE="-1">NDK</font> and set up your device, all that's left to do is setting up the device and the cross-compilation environment. Blackberry provides a script, <tt>&quot;bbndk-env.sh&quot;</tt> (occasionally named something like <tt>&quot;bbndk-env_10_1_0_4828.sh&quot;</tt>) which can be used to do this. However, there's a bit of a snag that we have to work through: The script modifies <font SIZE="-1">PATH</font> so that 'gcc' or 'ar' point to their cross-compilation equivalents, which screws over the build process. 

 So instead you'll want to do something like this: 

 <pre>
    $ orig_path=$PATH
    $ source $location_of_bbndk/bbndk-env*.sh
    $ export PATH=&quot;$orig_path:$PATH&quot;
</pre> 

 Besides putting the cross-compiler and the rest of the toolchain in your <font SIZE="-1">PATH,</font> this will also provide the <font SIZE="-1">QNX_TARGET</font> variable, which we will pass to Configure through -Dsysroot. 

 <i>Preparing the target system</i> 

 It's quite possible that the target system doesn't have a readily available /tmp, so it's generall safer to do something like this: 

 <pre>
 $ ssh $TARGETUSER@$TARGETHOST 'rm -rf perl; mkdir perl; mkdir perl/tmp'
 $ export TARGETDIR=`ssh $TARGETUSER@$TARGETHOST pwd`/perl
 $ export TARGETENV=&quot;export TMPDIR=$TARGETDIR/tmp; &quot;
</pre> 

 Later on, we'll pass this to Configure through -Dtargetenv 

 <i>Calling Configure</i> 

 If you are targetting an <font SIZE="-1">ARM</font> device --- which currently includes the vast majority of phones and tablets --- you'll want to pass -Dcc=arm-unknown-nto-qnx8.0.0eabi-gcc to Configure. Alternatively, if you are targetting an x86 device, or using the simulator provided with the <font SIZE="-1">NDK,</font> you should specify -Dcc=ntox86-gcc instead. 

 A sample Configure invocation looks something like this: 

 <pre>
    ./Configure -des -Dusecrosscompile \
        -Dsysroot=$QNX_TARGET          \
        -Dtargetdir=$TARGETDIR         \
        -Dtargetenv=&quot;$TARGETENV&quot;       \
        -Dcc=ntox86-gcc                \
        -Dtarghost=... # Usual cross-compilation options
</pre>

<h2>AUTHOR</h2>

 Norton T. Allen (allen [at] huarp.harvard.edu) 

<h2>Index</h2>



<dt><a HREF="#lbAI">AUTHOR</a>
<dd></dl>
