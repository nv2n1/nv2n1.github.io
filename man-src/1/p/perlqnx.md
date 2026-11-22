---

title: "perlqnx(1)"
name: "perlqnx"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlqnx/"
---

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

 Under QNX 6.2.0 there are still a few tests which fail. See below and hints/qnx.sh for more information.

<h3>Required Software for Compiling Perl on QNX4</h3>

 As with many unix ports, this one depends on a few ``standard'' unix utilities which are not necessarily standard for QNX4.
<dl>
<dt>/bin/sh
</dt><dd> This is used heavily by Configure and then by perl itself. QNX4's version is fine, but Configure will choke on the 16-bit version, so if you are running QNX 4.22, link /bin/sh to /bin32/ksh
</dd><dt>ar
</dt><dd> This is the standard unix library builder. We use wlib. With Watcom 10.6, when wlib is linked as ``ar'', it behaves like ar and all is fine. Under 9.5, a cover is required. One is included in ../qnx
</dd><dt>nm
</dt><dd> This is used (optionally) by configure to list the contents of libraries. I will generate a cover function on the fly in the UU directory.
</dd><dt>cpp
</dt><dd> Configure and perl need a way to invoke a C preprocessor. I have created a simple cover for cc which does the right thing. Without this, Configure will create its own wrapper which works, but it doesn't handle some of the command line arguments that perl will throw at it.
</dd><dt>make
</dt><dd> You really need GNU make to compile this. GNU make ships by default with QNX 4.23, but you can get it from quics for earlier versions.</dd></dl>

<h3>Outstanding Issues with Perl on QNX4</h3>

 There is no support for dynamically linked libraries in QNX4. 

 If you wish to compile with the Socket extension, you need to have the TCP/IP toolkit, and you need to make sure that -lsocket locates the correct copy of socket3r.lib. Beware that the Watcom compiler ships with a stub version of socket3r.lib which has very little functionality. Also beware the order in which wlink searches directories for libraries. You may have /usr/lib/socket3r.lib pointing to the correct library, but wlink may pick up /usr/watcom/10.6/usr/lib/socket3r.lib instead. Make sure they both point to the correct library, that is, /usr/tcptk/current/usr/lib/socket3r.lib. 

 The following tests may report errors under QNX4: 

 dist/Cwd/Cwd.t will complain if `pwd` and cwd don't give the same results. cwd calls `fullpath -t`, so if you cd `fullpath -t` before running the test, it will pass. 

 lib/File/Find/taint.t will complain if '.' is in your PATH. The PATH test is triggered because cwd calls `fullpath -t`. 

 ext/IO/lib/IO/t/io_sock.t: Subtests 14 and 22 are skipped due to the fact that the functionality to read back the non-blocking status of a socket is not implemented in QNX's TCP/IP. This has been reported to QNX and it may work with later versions of TCP/IP. 

 t/io/tell.t: Subtest 27 is failing. We are still investigating.

<h3>QNX auxiliary files</h3>

 The files in the ``qnx'' directory are:
<dl>
<dt>qnx/ar
</dt><dd> A script that emulates the standard unix archive (aka library) utility. Under Watcom 10.6, ar is linked to wlib and provides the expected interface. With Watcom 9.5, a cover function is required. This one is fairly crude but has proved adequate for compiling perl.
</dd><dt>qnx/cpp
</dt><dd> A script that provides C preprocessing functionality. Configure can generate a similar cover, but it doesn't handle all the command-line options that perl throws at it. This might be reasonably placed in /usr/local/bin.</dd></dl>

<h3>Outstanding issues with perl under QNX6</h3>

 The following tests are still failing for Perl 5.8.1 under QNX 6.2.0: 

 <pre>
  op/sprintf.........................FAILED at test 91
  lib/Benchmark......................FAILED at test 26
</pre> 

 This is due to a bug in the C library's printf routine. printf(``'%e''', 0. ) produces '0.000000e+0', but ANSI requires '0.000000e+00'. QNX has acknowledged the bug.

<h3>Cross-compilation</h3>

 Perl supports cross-compiling to QNX NTO through the Native Development Kit (NDK) for the Blackberry 10. This means that you can cross-compile for both ARM and x86 versions of the platform. 

 <i>Setting up a cross-compilation environment</i> 

 You can download the NDK from &lt;<a rel="nofollow" HREF="http://developer.blackberry.com/native/downloads/">http://developer.blackberry.com/native/downloads/</a>&gt;. 

 See &lt;<a rel="nofollow" HREF="http://developer.blackberry.com/native/documentation/cascades/getting_started/setting_up.html">http://developer.blackberry.com/native/documentation/cascades/getting_started/setting_up.html</a>&gt; for instructions to set up your device prior to attempting anything else. 

 Once you've installed the NDK and set up your device, all that's left to do is setting up the device and the cross-compilation environment. Blackberry provides a script, <tt>&quot;bbndk-env.sh&quot;</tt> (occasionally named something like <tt>&quot;bbndk-env_10_1_0_4828.sh&quot;</tt>) which can be used to do this. However, there's a bit of a snag that we have to work through: The script modifies PATH so that 'gcc' or 'ar' point to their cross-compilation equivalents, which screws over the build process. 

 So instead you'll want to do something like this: 

 <pre>
    $ orig_path=$PATH
    $ source $location_of_bbndk/bbndk-env*.sh
    $ export PATH=&quot;$orig_path:$PATH&quot;
</pre> 

 Besides putting the cross-compiler and the rest of the toolchain in your PATH, this will also provide the QNX_TARGET variable, which we will pass to Configure through -Dsysroot. 

 <i>Preparing the target system</i> 

 It's quite possible that the target system doesn't have a readily available /tmp, so it's generall safer to do something like this: 

 <pre>
 $ ssh $TARGETUSER@$TARGETHOST 'rm -rf perl; mkdir perl; mkdir perl/tmp'
 $ export TARGETDIR=`ssh $TARGETUSER@$TARGETHOST pwd`/perl
 $ export TARGETENV=&quot;export TMPDIR=$TARGETDIR/tmp; &quot;
</pre> 

 Later on, we'll pass this to Configure through -Dtargetenv 

 <i>Calling Configure</i> 

 If you are targetting an ARM device --- which currently includes the vast majority of phones and tablets --- you'll want to pass -Dcc=arm-unknown-nto-qnx8.0.0eabi-gcc to Configure. Alternatively, if you are targetting an x86 device, or using the simulator provided with the NDK, you should specify -Dcc=ntox86-gcc instead. 

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



<dt><a HREF="#lbAI">AUTHOR</a>
</dt><dd></dd></dl>
