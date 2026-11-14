---
title: "perlaix(1)"
name: "perlaix"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlaix/"
description: "perlaix – Perl version 5 on IBM AIX (UNIX) systems"
---

<h2 class="name">NAME</h2>
<p> perlaix &#8211; Perl version 5 on IBM AIX (UNIX) systems </p>
<h2>DESCRIPTION</h2>
<p> This document describes various features of <font SIZE="-1">IBM</font>&#8216;s <font SIZE="-1">UNIX</font> operating system <font SIZE="-1">AIX</font> that will affect how Perl version 5 (hereafter just Perl) is compiled and/or runs.</p>
<h3>Compiling Perl 5 on <font SIZE="-1">AIX</font></h3>
<p> For information on compilers on older versions of <font SIZE="-1">AIX,</font> see &#8220;Compiling Perl 5 on older <font SIZE="-1">AIX</font> versions up to 4.3.3&#8221;. </p>
<p> When compiling Perl, you must use an <font SIZE="-1">ANSI C</font> compiler. <font SIZE="-1">AIX</font> does not ship an <font SIZE="-1">ANSI</font> compliant C compiler with <font SIZE="-1">AIX</font> by default, but binary builds of gcc for <font SIZE="-1">AIX</font> are widely available. A version of gcc is also included in the <font SIZE="-1">AIX</font> Toolbox which is shipped with <font SIZE="-1">AIX.</font></p>
<h3>Supported Compilers</h3>
<p> Currently all versions of <font SIZE="-1">IBM</font>&#8216;s &#8220;xlc&#8221;, &#8220;xlc_r&#8221;, &#8220;cc&#8221;, &#8220;cc_r&#8221; or &#8220;vac&#8221; <font SIZE="-1">ANSI/C</font> compiler will work for building Perl if that compiler works on your system. </p>
<p> If you plan to link Perl to any module that requires thread-support, like DBD::Oracle, it is better to use the _r version of the compiler. This will not build a threaded Perl, but a thread-enabled Perl. See also &#8220;Threaded Perl&#8221; later on. </p>
<p> As of writing (2010-09) only the <i></i><font SIZE="-1"><i>IBM XL C</i></font><i> for </i><font SIZE="-1"><i>AIX</i></font><i></i> or <i></i><font SIZE="-1"><i>IBM XL C/C<font SIZE="-2">++</font></i></font><i> for </i><font SIZE="-1"><i>AIX</i></font><i></i> compiler is supported by <font SIZE="-1">IBM</font> on <font SIZE="-1">AIX 5L/6.1/7.1.</font> </p>
<p> The following compiler versions are currently supported by <font SIZE="-1">IBM:</font> </p>
<pre>
    IBM XL C and IBM XL C/C++ V8, V9, V10, V11
</pre>
<p> The <font SIZE="-1">XL C</font> for <font SIZE="-1">AIX</font> is integrated in the <font SIZE="-1">XL C/C<font SIZE="-2">++</font></font> for <font SIZE="-1">AIX</font> compiler and therefore also supported. </p>
<p> If you choose <font SIZE="-1">XL C/C<font SIZE="-2">++</font> V9</font> you need <font SIZE="-1">APAR IZ35785</font> installed otherwise the integrated SDBM_File do not compile correctly due to an optimization bug. You can circumvent this problem by adding -qipa to the optimization flags (-Doptimize=&#8217;-O -qipa&#8217;). The <font SIZE="-1">PTF</font> for <font SIZE="-1">APAR IZ35785</font> which solves this problem is available from <font SIZE="-1">IBM</font> (April 2009 <font SIZE="-1">PTF</font> for <font SIZE="-1">XL C/C<font SIZE="-2">++</font></font> Enterprise Edition for <font SIZE="-1">AIX, V9.0</font>). </p>
<p> If you choose <font SIZE="-1">XL C/C<font SIZE="-2">++</font> V11</font> you need the April 2010 <font SIZE="-1">PTF</font> (or newer) installed otherwise you will not get a working Perl version. </p>
<p> Perl can be compiled with either <font SIZE="-1">IBM</font>&#8216;s <font SIZE="-1">ANSI C</font> compiler or with gcc. The former is recommended, as not only it can compile Perl with no difficulty, but also can take advantage of features listed later that require the use of <font SIZE="-1">IBM</font> compiler-specific command-line flags. </p>
<p> If you decide to use gcc, make sure your installation is recent and complete, and be sure to read the Perl <font SIZE="-1">INSTALL</font> file for more gcc-specific details. Please report any hoops you had to jump through to the development team.</p>
<h3>Incompatibility with <font SIZE="-1">AIX</font> Toolbox lib gdbm</h3>
<p> If the <font SIZE="-1">AIX</font> Toolbox version of lib gdbm &lt; 1.8.3-5 is installed on your system then Perl will not work. This library contains the header files /opt/freeware/include/gdbm/dbm.h|ndbm.h which conflict with the <font SIZE="-1">AIX</font> system versions. The lib gdbm will be automatically removed from the wanted libraries if the presence of one of these two header files is detected. If you want to build Perl with <font SIZE="-1">GDBM</font> support then please install at least gdbm-devel-1.8.3-5 (or higher).</p>
<h3>Perl 5 was successfully compiled and tested on:</h3>
<pre><code>
Perl | AIX Level | Compiler Level | w th | w / o th-- -- -- -+-- -- -- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -- -- -- -- -- -+-- -- --+-- -- -- -5.12.2 | 5.1 TL9 32 bit | XL C / C++ V7 | OK | OK 5.12.2 | 5.1 TL9 64 bit | XL C / C++ V7 | OK | OK 5.12.2 | 5.2 TL10 SP8 32 bit | XL C / C++ V8 | OK | OK 5.12.2 | 5.2 TL10 SP8 32 bit | gcc 3.2.2 | OK | OK 5.12.2 | 5.2 TL10 SP8 64 bit | XL C / C++ V8 | OK | OK 5.12.2 | 5.3 TL8 SP8 32 bit | XL C / C++ V9 + IZ35785 | OK | OK 5.12.2 | 5.3 TL8 SP8 32 bit | gcc 4.2.4 | OK | OK 5.12.2 | 5.3 TL8 SP8 64 bit | XL C / C++ V9 + IZ35785 | OK | OK 5.12.2 | 5.3 TL10 SP3 32 bit | XL C / C++ V11 + Apr 2010 | OK | OK 5.12.2 | 5.3 TL10 SP3 64 bit | XL C / C++ V11 + Apr 2010 | OK | OK 5.12.2 | 6.1 TL1 SP7 32 bit | XL C / C++ V10 | OK | OK 5.12.2 | 6.1 TL1 SP7 64 bit | XL C / C++ V10 | OK | OK 5.13 | 7.1 TL0 SP1 32 bit | XL C / C++ V11 + Jul 2010 | OK | OK 5.13 | 7.1 TL0 SP1 64 bit | XL C / C++ V11 + Jul 2010 | OK | OK w th = with thread support
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             w /
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         o th = without thread support
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             OK = tested
</code></pre>
<p> Successfully tested means that all &#8220;make test&#8221; runs finish with a result of 100% <font SIZE="-1">OK.</font> All tests were conducted with -Duseshrplib set. </p>
<p> All tests were conducted on the oldest supported <font SIZE="-1">AIX</font> technology level with the latest support package applied. If the tested <font SIZE="-1">AIX</font> version is out of support (<font SIZE="-1">AIX 4.3.3, 5.1, 5.2</font>) then the last available support level was used.</p>
<h3>Building Dynamic Extensions on <font SIZE="-1">AIX</font></h3>
<p> Starting from Perl 5.7.2 (and consequently 5.8.x / 5.10.x / 5.12.x) and <font SIZE="-1">AIX 4.3</font> or newer Perl uses the <font SIZE="-1">AIX</font> native dynamic loading interface in the so called runtime linking mode instead of the emulated interface that was used in Perl releases 5.6.1 and earlier or, for <font SIZE="-1">AIX</font> releases 4.2 and earlier. This change does break backward compatibility with compiled modules from earlier Perl releases. The change was made to make Perl more compliant with other applications like Apache/mod_perl which are using the <font SIZE="-1">AIX</font> native interface. This change also enables the use of C<font SIZE="-2">++</font> code with static constructors and destructors in Perl extensions, which was not possible using the emulated interface. </p>
<p> It is highly recommended to use the new interface.</p>
<h3>Using Large Files with Perl</h3>
<p> Should yield no problems.</p>
<h3>Threaded Perl</h3>
<p> Should yield no problems with <font SIZE="-1">AIX 5.1 / 5.2 / 5.3 / 6.1 / 7.1.</font> </p>
<p> <font SIZE="-1">IBM</font> uses the <font SIZE="-1">AIX</font> system Perl (V5.6.0 on <font SIZE="-1">AIX 5.1</font> and V5.8.2 on <font SIZE="-1">AIX 5.2 / 5.3</font> and 6.1; V5.8.8 on <font SIZE="-1">AIX 5.3 TL11</font> and <font SIZE="-1">AIX 6.1 TL4</font>; V5.10.1 on <font SIZE="-1">AIX 7.1</font>) for some <font SIZE="-1">AIX</font> system scripts. If you switch the links in /usr/bin from the <font SIZE="-1">AIX</font> system Perl (/usr/opt/perl5) to the newly build Perl then you get the same features as with the <font SIZE="-1">IBM AIX</font> system Perl if the threaded options are used. </p>
<p> The threaded Perl build works also on <font SIZE="-1">AIX 5.1</font> but the <font SIZE="-1">IBM</font> Perl build (Perl v5.6.0) is not threaded on <font SIZE="-1">AIX 5.1.</font> </p>
<p> Perl 5.12 an newer is not compatible with the <font SIZE="-1">IBM</font> fileset perl.libext.</p>
<h3>64-bit Perl</h3>
<p> If your <font SIZE="-1">AIX</font> system is installed with 64-bit support, you can expect 64-bit configurations to work. If you want to use 64-bit Perl on <font SIZE="-1">AIX 6.1</font> you need an <font SIZE="-1">APAR</font> for a libc.a bug which affects (n)dbm_XXX functions. The <font SIZE="-1">APAR</font> number for this problem is <font SIZE="-1">IZ39077.</font> </p>
<p> If you need more memory (larger data segment) for your Perl programs you can set: </p>
<pre>
    /etc/security/limits
    default:                    (or your user)
        data = -1               (default is 262144 * 512 byte)
</pre>
<p> With the default setting the size is limited to 128MB. The -1 removes this limit. If the &#8220;make test&#8221; fails please change your /etc/security/limits as stated above.</p>
<h3>Long doubles</h3>
<p> <font SIZE="-1">IBM</font> calls its implementation of long doubles 128-bit, but it is not the <font SIZE="-1">IEEE</font> 128-bit (&#8220;quadruple precision&#8221;) which would give 116 bit of mantissa (nor it is implemented in hardware), instead it&#8217;s a special software implementation called &#8220;double-double&#8221;, which gives 106 bits of mantissa. </p>
<p> There seem to be various problems in this long double implementation. If Configure detects this brokenness, it will disable the long double support. This can be overridden with explicit <tt>&quot;-Duselongdouble&quot;</tt> (or <tt>&quot;-Dusemorebits&quot;</tt>, which enables both long doubles and 64 bit integers). If you decide to enable long doubles, for most of the broken things Perl has implemented workarounds, but the handling of the special values infinity and NaN remains badly broken: for example infinity plus zero results in NaN.</p>
<h3>Recommended Options <font SIZE="-1">AIX 5.1/5.2/5.3/6.1</font> and 7.1 (threaded/32-bit)</h3>
<p> With the following options you get a threaded Perl version which passes all make tests in threaded 32-bit mode, which is the default configuration for the Perl builds that <font SIZE="-1">AIX</font> ships with. </p>
<pre>
    rm config.sh
    ./Configure \
    -d \
    -Dcc=cc_r \
    -Duseshrplib \
    -Dusethreads \
    -Dprefix=/usr/opt/perl5_32
</pre>
<p> The -Dprefix option will install Perl in a directory parallel to the <font SIZE="-1">IBM AIX</font> system Perl installation.</p>
<h3>Recommended Options <font SIZE="-1">AIX 5.1/5.2/5.3/6.1</font> and 7.1 (32-bit)</h3>
<p> With the following options you get a Perl version which passes all make tests in 32-bit mode. </p>
<pre>
    rm config.sh
    ./Configure \
    -d \
    -Dcc=cc_r \
    -Duseshrplib \
    -Dprefix=/usr/opt/perl5_32
</pre>
<p> The -Dprefix option will install Perl in a directory parallel to the <font SIZE="-1">IBM AIX</font> system Perl installation.</p>
<h3>Recommended Options <font SIZE="-1">AIX 5.1/5.2/5.3/6.1</font> and 7.1 (threaded/64-bit)</h3>
<p> With the following options you get a threaded Perl version which passes all make tests in 64-bit mode. </p>
<pre>
 export OBJECT_MODE=64 / setenv OBJECT_MODE 64 (depending on your shell)
 rm config.sh
 ./Configure \
 -d \
 -Dcc=cc_r \
 -Duseshrplib \
 -Dusethreads \
 -Duse64bitall \
 -Dprefix=/usr/opt/perl5_64
</pre>
<h3>Recommended Options <font SIZE="-1">AIX 5.1/5.2/5.3/6.1</font> and 7.1 (64-bit)</h3>
<p> With the following options you get a Perl version which passes all make tests in 64-bit mode. </p>
<pre>
 export OBJECT_MODE=64 / setenv OBJECT_MODE 64 (depending on your shell)
 rm config.sh
 ./Configure \
 -d \
 -Dcc=cc_r \
 -Duseshrplib \
 -Duse64bitall \
 -Dprefix=/usr/opt/perl5_64
</pre>
<p> The -Dprefix option will install Perl in a directory parallel to the <font SIZE="-1">IBM AIX</font> system Perl installation. </p>
<p> If you choose gcc to compile 64-bit Perl then you need to add the following option: </p>
<pre>
    -Dcc='gcc -maix64'
</pre>
<h3>Compiling Perl 5 on <font SIZE="-1">AIX 7.1.0</font></h3>
<p> A regression in <font SIZE="-1">AIX 7</font> causes a failure in make test in Time::Piece during daylight savings time. <font SIZE="-1">APAR IV16514</font> provides the fix for this. A quick test to see if it&#8217;s required, assuming it is currently daylight savings in Eastern Time, would be to run <tt>&quot; TZ=EST5 date +%Z &quot;</tt>. This will come back with <tt>&quot;EST&quot;</tt> normally, but nothing if you have the problem.</p>
<h3>Compiling Perl 5 on older <font SIZE="-1">AIX</font> versions up to 4.3.3</h3>
<p> Due to the fact that <font SIZE="-1">AIX 4.3.3</font> reached end-of-service in December 31, 2003 this information is provided as is. The Perl versions prior to Perl 5.8.9 could be compiled on <font SIZE="-1">AIX</font> up to 4.3.3 with the following settings (your mileage may vary): </p>
<p> When compiling Perl, you must use an <font SIZE="-1">ANSI C</font> compiler. <font SIZE="-1">AIX</font> does not ship an <font SIZE="-1">ANSI</font> compliant C-compiler with <font SIZE="-1">AIX</font> by default, but binary builds of gcc for <font SIZE="-1">AIX</font> are widely available. </p>
<p> At the moment of writing, <font SIZE="-1">AIX</font> supports two different native C compilers, for which you have to pay: <code>xlC</code> and <code>vac</code>. If you decide to use either of these two (which is quite a lot easier than using gcc), be sure to upgrade to the latest available patch level. Currently: </p>
<pre>
    xlC.C     3.1.4.10 or 3.6.6.0 or 4.0.2.2 or 5.0.2.9 or 6.0.0.3
    vac.C     4.4.0.3  or 5.0.2.6 or 6.0.0.1
</pre>
<p> note that xlC has the <font SIZE="-1">OS</font> version in the name as of version 4.0.2.0, so you will find xlC.C for <font SIZE="-1">AIX-5.0</font> as package </p>
<pre>
    xlC.aix50.rte   5.0.2.0 or 6.0.0.3
</pre>
<p> subversions are not the same &#8220;latest&#8221; on all <font SIZE="-1">OS</font> versions. For example, the latest xlC-5 on aix41 is 5.0.2.9, while on aix43, it is 5.0.2.7. </p>
<p> Perl can be compiled with either <font SIZE="-1">IBM</font>&#8216;s <font SIZE="-1">ANSI C</font> compiler or with gcc. The former is recommended, as not only can it compile Perl with no difficulty, but also can take advantage of features listed later that require the use of <font SIZE="-1">IBM</font> compiler-specific command-line flags. </p>
<p> The <font SIZE="-1">IBM</font>&#8216;s compiler patch levels 5.0.0.0 and 5.0.1.0 have compiler optimization bugs that affect compiling perl.c and regcomp.c, respectively. If Perl&#8217;s configuration detects those compiler patch levels, optimization is turned off for the said source code files. Upgrading to at least 5.0.2.0 is recommended. </p>
<p> If you decide to use gcc, make sure your installation is recent and complete, and be sure to read the Perl <font SIZE="-1">INSTALL</font> file for more gcc-specific details. Please report any hoops you had to jump through to the development team.</p>
<h3><font SIZE="-1">OS</font> level</h3>
<p> Before installing the patches to the <font SIZE="-1">IBM</font> C-compiler you need to know the level of patching for the Operating System. <font SIZE="-1">IBM</font>&#8216;s command &#8216;oslevel&#8217; will show the base, but is not always complete (in this example oslevel shows 4.3.NULL, whereas the system might run most of 4.3.THREE): </p>
<pre>
    # oslevel
    4.3.0.0
    # lslpp -l | grep 'bos.rte '
    bos.rte           4.3.3.75  COMMITTED  Base Operating System Runtime
    bos.rte            4.3.2.0  COMMITTED  Base Operating System Runtime
    #
</pre>
<p> The same might happen to <font SIZE="-1">AIX 5.1</font> or other <font SIZE="-1">OS</font> levels. As a side note, Perl cannot be built without bos.adt.syscalls and bos.adt.libm installed </p>
<pre>
    # lslpp -l | egrep &quot;syscalls|libm&quot;
    bos.adt.libm      5.1.0.25  COMMITTED  Base Application Development
    bos.adt.syscalls  5.1.0.36  COMMITTED  System Calls Application
    #
</pre>
<h3>Building Dynamic Extensions on <font SIZE="-1">AIX</font> &lt; 5L</h3>
<p> <font SIZE="-1">AIX</font> supports dynamically loadable objects as well as shared libraries. Shared libraries by convention end with the suffix .a, which is a bit misleading, as an archive can contain static as well as dynamic members. For Perl dynamically loaded objects we use the .so suffix also used on many other platforms. </p>
<p> Note that starting from Perl 5.7.2 (and consequently 5.8.0) and <font SIZE="-1">AIX 4.3</font> or newer Perl uses the <font SIZE="-1">AIX</font> native dynamic loading interface in the so called runtime linking mode instead of the emulated interface that was used in Perl releases 5.6.1 and earlier or, for <font SIZE="-1">AIX</font> releases 4.2 and earlier. This change does break backward compatibility with compiled modules from earlier Perl releases. The change was made to make Perl more compliant with other applications like Apache/mod_perl which are using the <font SIZE="-1">AIX</font> native interface. This change also enables the use of C<font SIZE="-2">++</font> code with static constructors and destructors in Perl extensions, which was not possible using the emulated interface.</p>
<h3>The <font SIZE="-1">IBM ANSI C</font> Compiler</h3>
<p> All defaults for Configure can be used. </p>
<p> If you&#8217;ve chosen to use vac 4, be sure to run 4.4.0.3. Older versions will turn up nasty later on. For vac 5 be sure to run at least 5.0.1.0, but vac 5.0.2.6 or up is highly recommended. Note that since <font SIZE="-1">IBM</font> has removed vac 5.0.2.1 through 5.0.2.5 from the software depot, these versions should be considered obsolete. </p>
<p> Here&#8217;s a brief lead of how to upgrade the compiler to the latest level. Of course this is subject to changes. You can only upgrade versions from ftp-available updates if the first three digit groups are the same (in where you can skip intermediate unlike the patches in the developer snapshots of Perl), or to one version up where the &#8220;base&#8221; is available. In other words, the <font SIZE="-1">AIX</font> compiler patches are cumulative. </p>
<pre>
 vac.C.4.4.0.1 =&gt; vac.C.4.4.0.3  is OK     (vac.C.4.4.0.2 not needed)
 xlC.C.3.1.3.3 =&gt; xlC.C.3.1.4.10 is NOT OK (xlC.C.3.1.4.0 is not
                                                              available)
 # ftp <a href="ftp://ftp.software.ibm.com">ftp.software.ibm.com</a>
 Connected to service.boulder.ibm.com.
 : welcome message ...
 Name (<a href="ftp://ftp.software.ibm.com">ftp.software.ibm.com</a>:merijn): anonymous
 331 Guest login ok, send your complete e-mail address as password.
 Password:
 ... accepted login stuff
 ftp&gt; cd /aix/fixes/v4/
 ftp&gt; dir other other.ll
 output to local-file: other.ll? y
 200 PORT command successful.
 150 Opening ASCII mode data connection for /bin/ls.
 226 Transfer complete.
 ftp&gt; dir xlc xlc.ll
 output to local-file: xlc.ll? y
 200 PORT command successful.
 150 Opening ASCII mode data connection for /bin/ls.
 226 Transfer complete.
 ftp&gt; bye
 ... goodbye messages
 # ls -l *.ll
 -rw-rw-rw-   1 merijn   system    1169432 Nov  2 17:29 other.ll
 -rw-rw-rw-   1 merijn   system      29170 Nov  2 17:29 xlc.ll
</pre>
<p> On <font SIZE="-1">AIX 4.2</font> using xlC, we continue: </p>
<p>#lslpp &#8211; l | fgrep &#8216;xlC.C &#8216;<br />
   xlC.C                     3.1.4.9  COMMITTED  C for AIX Compiler<br />
   xlC.C                     3.1.4.0  COMMITTED  C for AIX Compiler<br />
#grep &#8216;xlC.C.3.1.4.*.bff&#8217; xlc.ll<br />
 -rw-r&#8211;r&#8211;   1 45776101 1       6286336 Jul 22 1996  xlC.C.3.1.4.1.bff<br />
 -rw-rw-r&#8211;   1 45776101 1       6173696 Aug 24 1998  xlC.C.3.1.4.10.bff<br />
 -rw-r&#8211;r&#8211;   1 45776101 1       6319104 Aug 14 1996  xlC.C.3.1.4.2.bff<br />
 -rw-r&#8211;r&#8211;   1 45776101 1       6316032 Oct 21 1996  xlC.C.3.1.4.3.bff<br />
 -rw-r&#8211;r&#8211;   1 45776101 1       6315008 Dec 20 1996  xlC.C.3.1.4.4.bff<br />
 -rw-rw-r&#8211;   1 45776101 1       6178816 Mar 28 1997  xlC.C.3.1.4.5.bff<br />
 -rw-rw-r&#8211;   1 45776101 1       6188032 May 22 1997  xlC.C.3.1.4.6.bff<br />
 -rw-rw-r&#8211;   1 45776101 1       6191104 Sep  5 1997  xlC.C.3.1.4.7.bff<br />
 -rw-rw-r&#8211;   1 45776101 1       6185984 Jan 13 1998  xlC.C.3.1.4.8.bff<br />
 -rw-rw-r&#8211;   1 45776101 1       6169600 May 27 1998  xlC.C.3.1.4.9.bff<br />
#wget ftp: // ftp.software.ibm.com/aix/fixes/v4/xlc/xlC.C.3.1.4.10.bff<br />
#</p>
<p> On <font SIZE="-1">AIX 4.3</font> using vac, we continue: </p>
<p>#lslpp &#8211; l | grep &#8216;vac.C &#8216;<br />
  vac.C                      5.0.2.2  COMMITTED  C for AIX Compiler<br />
  vac.C                      5.0.2.0  COMMITTED  C for AIX Compiler<br />
#grep &#8216;vac.C.5.0.2.*.bff&#8217; other.ll<br />
 -rw-rw-r&#8211;   1 45776101 1       13592576 Apr 16 2001  vac.C.5.0.2.0.bff<br />
 -rw-rw-r&#8211;   1 45776101 1       14133248 Apr  9 2002  vac.C.5.0.2.3.bff<br />
 -rw-rw-r&#8211;   1 45776101 1       14173184 May 20 2002  vac.C.5.0.2.4.bff<br />
 -rw-rw-r&#8211;   1 45776101 1       14192640 Nov 22 2002  vac.C.5.0.2.6.bff<br />
#wget ftp: // ftp.software.ibm.com/aix/fixes/v4/other/vac.C.5.0.2.6.bff<br />
#</p>
<p> Likewise on all other <font SIZE="-1">OS</font> levels. Then execute the following command, and fill in its choices </p>
<p>#smit install_update<br />
  -&gt; Install and Update from LATEST Available Software<br />
  * INPUT device / directory for software [ vac.C.5.0.2.6.bff    ]<br />
  [ OK ]<br />
  [ OK ]</p>
<p> Follow the messages &#8230; and you&#8217;re done. </p>
<p> If you like a more web-like approach, a good start point can be &lt;<a rel="nofollow" href="http://www14.software.ibm.com/webapp/download/downloadaz.jsp">http://www14.software.ibm.com/webapp/download/downloadaz.jsp</a>&gt; and click &#8220;C for <font SIZE="-1">AIX&#8221;,</font> and follow the instructions.</p>
<h3>The usenm option</h3>
<p> If linking miniperl </p>
<pre>
 cc -o miniperl ... miniperlmain.o opmini.o perl.o ... -lm -lc ...
</pre>
<p> causes error like this </p>
<pre>
 ld: 0711-317 ERROR: Undefined symbol: .aintl
 ld: 0711-317 ERROR: Undefined symbol: .copysignl
 ld: 0711-317 ERROR: Undefined symbol: .syscall
 ld: 0711-317 ERROR: Undefined symbol: .eaccess
 ld: 0711-317 ERROR: Undefined symbol: .setresuid
 ld: 0711-317 ERROR: Undefined symbol: .setresgid
 ld: 0711-317 ERROR: Undefined symbol: .setproctitle
 ld: 0711-345 Use the -bloadmap or -bnoquiet option to obtain more
                                                            information.
</pre>
<p> you could retry with </p>
<pre>
 make realclean
 rm config.sh
 ./Configure -Dusenm ...
</pre>
<p> which makes Configure to use the <tt>&quot;nm&quot;</tt> tool when scanning for library symbols, which usually is not done in <font SIZE="-1">AIX.</font> </p>
<p> Related to this, you probably should not use the <tt>&quot;-r&quot;</tt> option of Configure in <font SIZE="-1">AIX,</font> because that affects of how the <tt>&quot;nm&quot;</tt> tool is used.</p>
<h3>Using <font SIZE="-1">GNU</font>&#8216;s gcc for building Perl</h3>
<p> Using gcc-3.x (tested with 3.0.4, 3.1, and 3.2) now works out of the box, as do recent gcc-2.9 builds available directly from <font SIZE="-1">IBM</font> as part of their Linux compatibility packages, available here: </p>
<pre>
  <a rel="nofollow" href="http://www.ibm.com/servers/aix/products/aixos/linux/">http://www.ibm.com/servers/aix/products/aixos/linux/</a>
</pre>
<h3>Using Large Files with Perl &lt; 5L</h3>
<p> Should yield no problems.</p>
<h3>Threaded Perl &lt; 5L</h3>
<p> Threads seem to work <font SIZE="-1">OK,</font> though at the moment not all tests pass when threads are used in combination with 64-bit configurations. </p>
<p> You may get a warning when doing a threaded build: </p>
<pre><code>
"pp_sys.c", line 4640.39 : 1506 - 280(W)Function argument assignment
                    between types "unsigned char*" and
                "const void*" is not allowed.
</code></pre>
<p> The exact line number may vary, but if the warning (W) comes from a line line this </p>
<pre>
  hent = PerlSock_gethostbyaddr(addr, (Netdb_hlen_t) addrlen, addrtype);
</pre>
<p> in the &#8220;pp_ghostent&#8221; function, you may ignore it safely. The warning is caused by the reentrant variant of <code>gethostbyaddr()</code> having a slightly different prototype than its non-reentrant variant, but the difference is not really significant here.</p>
<h3>64-bit Perl &lt; 5L</h3>
<p> If your <font SIZE="-1">AIX</font> is installed with 64-bit support, you can expect 64-bit configurations to work. In combination with threads some tests might still fail.</p>
<h3><font SIZE="-1">AIX 4.2</font> and extensions using C<font SIZE="-2">++</font> with statics</h3>
<p> In <font SIZE="-1">AIX 4.2</font> Perl extensions that use C<font SIZE="-2">++</font> functions that use statics may have problems in that the statics are not getting initialized. In newer <font SIZE="-1">AIX</font> releases this has been solved by linking Perl with the libC_r library, but unfortunately in <font SIZE="-1">AIX 4.2</font> the said library has an obscure bug where the various functions related to time (such as <code>time()</code> and <code>gettimeofday()</code>) return broken values, and therefore in <font SIZE="-1">AIX 4.2</font> Perl is not linked against the libC_r.</p>
<h2>AUTHORS</h2>
<p> Rainer Tammer &lt;tammer [at] tammer.net&gt; </p>
<h2>Index</h2>
<dt><a href="#lbBB">AUTHORS</a></p>
<dd></dl>
