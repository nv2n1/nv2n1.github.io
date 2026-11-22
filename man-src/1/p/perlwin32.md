---

title: "perlwin32(1)"
name: "perlwin32"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlwin32/"
description: "perlwin32 – Perl under Windows"
---

<p> perlwin32 - Perl under Windows </p>
<h2>SYNOPSIS</h2>
<p> These are instructions for building Perl under Windows 2000 and later.  </p>
<h2>DESCRIPTION</h2>
<p> Before you start, you should glance through the README file found in the top-level directory to which the Perl distribution was extracted. Make sure you read and understand the terms under which this software is being distributed. </p>
<p> Also make sure you read ``BUGS AND CAVEATS&#8217;&#8216; below for the known limitations of this port. </p>
<p> The INSTALL file in the perl top-level has much information that is only relevant to people building Perl on Unix-like systems. In particular, you can safely ignore any information that talks about ``Configure&#8217;&#8216;. </p>
<p> You may also want to look at one other option for building a perl that will work on Windows: the README.cygwin file, which give a different set of rules to build a perl for Windows. This method will probably enable you to build a more Unix-compatible perl, but you will also need to download and use various other build-time and run-time support software described in that file. </p>
<p> This set of instructions is meant to describe a so-called ``native&#8217;&#8216; port of Perl to the Windows platform. This includes both 32-bit and 64-bit Windows operating systems. The resulting Perl requires no additional software to run (other than what came with your operating system). Currently, this port is capable of using one of the following compilers on the Intel x86 architecture: </p>
<pre><code>      Microsoft Visual C++ version 6.0 or later
      Intel C++ Compiler (experimental)
      Gcc by mingw.org gcc version 3.4.5 or later
                              with runtime &lt; 3.21
      Gcc by mingw-w64.org gcc version 4.4.3 or later
</code></pre>
<p> Note that the last two of these are actually competing projects both delivering complete gcc toolchain for MS Windows: </p>
<dl>
<dt>&lt;<a rel="nofollow" href="http://mingw.org">http://mingw.org</a>&gt;</dt>
<dd> <p> Delivers gcc toolchain targeting 32-bit Windows platform. </p>
 </dd>
<dt>&lt;<a rel="nofollow" href="http://mingw-w64.org">http://mingw-w64.org</a>&gt;</dt>
<dd> <p> Delivers gcc toolchain targeting both 64-bit Windows and 32-bit Windows platforms (despite the project name ``mingw-w64&#8217;&#8216; they are not only 64-bit oriented). They deliver the native gcc compilers and cross-compilers that are also supported by perl&#8217;s makefile. </p>
 </dd></dl>
<p> The Microsoft Visual C++ compilers are also now being given away free. They are available as ``Visual C++ Toolkit 2003&#8217;&#8216; or ``Visual C++ 2005-2019 Express [or Community, from 2017] Edition&#8217;&#8216; (and also as part of the ``.NET Framework SDK&#8217;&#8216;) and are the same compilers that ship with ``Visual C++ .NET 2003 Professional&#8217;&#8216; or ``Visual C++ 2005-2019 Professional&#8217;&#8216; respectively. </p>
<p> This port can also be built on IA64/AMD64 using: </p>
<pre><code>      Microsoft Platform SDK Nov 2001 (64-bit compiler and tools)
      MinGW64 compiler (gcc version 4.4.3 or later)
</code></pre>
<p> The Windows SDK can be downloaded from &lt;<a rel="nofollow" href="http://www.microsoft.com/">http://www.microsoft.com/</a>&gt;. The MinGW64 compiler is available at &lt;<a rel="nofollow" href="http://mingw-w64.org">http://mingw-w64.org</a>&gt;. The latter is actually a cross-compiler targeting Win64. There&#8217;s also a trimmed down compiler (no java, or gfortran) suitable for building perl available at: &lt;<a rel="nofollow" href="http://strawberryperl.com/package/kmx/64_gcctoolchain/">http://strawberryperl.com/package/kmx/64_gcctoolchain/</a>&gt; </p>
<p> NOTE: If you&#8217;re using a 32-bit compiler to build perl on a 64-bit Windows operating system, then you should set the WIN64 environment variable to ``undef&#8217;&#8216;. Also, the trimmed down compiler only passes tests when USE_ITHREADS *= define (as opposed to undef) and when the CFG *= Debug line is commented out. </p>
<p> This port fully supports MakeMaker (the set of modules that is used to build extensions to perl). Therefore, you should be able to build and install most extensions found in the CPAN sites. See ``Usage Hints for Perl on Windows&#8217;&#8216; below for general hints about this.  </p>
<h3>Setting Up Perl on Windows</h3>
<dl>
<dt>Make</dt>
<dd> <p> You need a ``make&#8217;&#8216; program to build the sources. If you are using Visual C++ or the Windows SDK tools, you can use nmake supplied with Visual C++ or Windows SDK. You may also use, for Visual C++ or Windows SDK, dmake or gmake instead of nmake. dmake is open source software, but is not included with Visual C++ or Windows SDK. Builds using gcc need dmake or gmake. nmake is not supported for gcc builds. Parallel building is only supported with dmake and gmake, not nmake. When using dmake it is recommended to use dmake 4.13 or newer for parallel building. Older dmakes, in parallel mode, have very high CPU usage and pound the disk/filing system with duplicate I/O calls in an aggressive polling loop. </p>
<p> A port of dmake for Windows is available from: </p>
<p> &lt;<a rel="nofollow" href="http://search.cpan.org/dist/dmake/">http://search.cpan.org/dist/dmake/</a>&gt; </p>
<p> Fetch and install dmake somewhere on your path. </p>
 </dd>
<dt>Command Shell</dt>
<dd> <p> Use the default ``cmd&#8217;&#8216; shell that comes with Windows. Some versions of the popular 4DOS/NT shell have incompatibilities that may cause you trouble. If the build fails under that shell, try building again with the cmd shell. </p>
<p> Make sure the path to the build directory does not contain spaces. The build usually works in this circumstance, but some tests will fail. </p>
 </dd>
<dt>Microsoft Visual C++</dt>
<dd> <p> The nmake that comes with Visual C++ will suffice for building. Visual C requires that certain things be set up in the console before Visual C will sucessfully run. To make a console box be able to run the C compiler, you will need to beforehand, run the <code>&quot;vcvars32.bat&quot;</code> file to compile for x86-32 and for x86-64 <code>&quot;vcvarsall.bat x64&quot;</code> or <code>&quot;vcvarsamd64.bat&quot;</code>. On a typical install of a Microsoft C compiler product, these batch files will already be in your <code>&quot;PATH&quot;</code> environment variable so you may just type them without an absolute path into your console. If you need to find the absolute path to the batch file, it is usually found somewhere like C:\Program Files\Microsoft Visual Studio\VC98\Bin. With some newer Micrsoft C products (released after ~2004), the installer will put a shortcut in the start menu to launch a new console window with the console already set up for your target architecture (x86-32 or x86-64 or IA64). With the newer compilers, you may also use the older batch files if you choose so. </p>
 </dd>
<dt>Microsoft Visual C++ 2008-2019 Express/Community Edition</dt>
<dd> <p> These free versions of Visual C++ 2008-2019 Professional contain the same compilers and linkers that ship with the full versions, and also contain everything necessary to build Perl, rather than requiring a separate download of the Windows SDK like previous versions did. </p>
<p> These packages can be downloaded by searching in the Download Center at &lt;<a rel="nofollow" href="http://www.microsoft.com/downloads/search.aspx?displaylang=en">http://www.microsoft.com/downloads/search.aspx?displaylang=en</a>&gt;. (Providing exact links to these packages has proven a pointless task because the links keep on changing so often.) </p>
<p> Install Visual C++ 2008-2019 Express/Community, then setup your environment using, e.g. </p>
<pre><code> C:\Program Files\Microsoft Visual Studio 12.0\Common7\Tools\vsvars32.bat
</code></pre>
<p> (assuming the default installation location was chosen). </p>
<p> Perl should now build using the win32/Makefile. You will need to edit that file to set CCTYPE to one of MSVC90-MSVC142 first. </p>
 </dd>
<dt>Microsoft Visual C++ 2005 Express Edition</dt>
<dd> <p> This free version of Visual C++ 2005 Professional contains the same compiler and linker that ship with the full version, but doesn&#8217;t contain everything necessary to build Perl. </p>
<p> You will also need to download the ``Windows SDK&#8217;&#8216; (the ``Core SDK&#8217;&#8216; and ``MDAC SDK&#8217;&#8216; components are required) for more header files and libraries. </p>
<p> These packages can both be downloaded by searching in the Download Center at &lt;<a rel="nofollow" href="http://www.microsoft.com/downloads/search.aspx?displaylang=en">http://www.microsoft.com/downloads/search.aspx?displaylang=en</a>&gt;. (Providing exact links to these packages has proven a pointless task because the links keep on changing so often.) </p>
<p> Try to obtain the latest version of the Windows SDK. Sometimes these packages contain a particular Windows OS version in their name, but actually work on other OS versions too. For example, the ``Windows Server 2003 R2 Platform SDK&#8217;&#8216; also runs on Windows XP SP2 and Windows 2000. </p>
<p> Install Visual C++ 2005 first, then the Platform SDK. Setup your environment as follows (assuming default installation locations were chosen): </p>
<pre><code> SET PlatformSDKDir=C:\Program Files\Microsoft Platform SDK
 SET PATH=%SystemRoot%\system32;%SystemRoot%;C:\Program Files\Microsoft Visual Studio 8\Common7\IDE;C:\Program Files\Microsoft Visual Studio 8\VC\BIN;C:\Program Files\Microsoft Visual Studio 8\Common7\Tools;C:\Program Files\Microsoft Visual Studio 8\SDK\v2.0\bin;C:\WINDOWS\Microsoft.NET\Framework\v2.0.50727;C:\Program Files\Microsoft Visual Studio 8\VC\VCPackages;%PlatformSDKDir%\Bin
 SET INCLUDE=C:\Program Files\Microsoft Visual Studio 8\VC\INCLUDE;%PlatformSDKDir%\include
 SET LIB=C:\Program Files\Microsoft Visual Studio 8\VC\LIB;C:\Program Files\Microsoft Visual Studio 8\SDK\v2.0\lib;%PlatformSDKDir%\lib
 SET LIBPATH=C:\WINDOWS\Microsoft.NET\Framework\v2.0.50727
</code></pre>
<p> (The PlatformSDKDir might need to be set differently depending on which version you are using. Earlier versions installed into ``C:\Program Files\Microsoft SDK&#8217;&#8216;, while the latest versions install into version-specific locations such as ``C:\Program Files\Microsoft Platform SDK for Windows Server 2003 R2&#8217;&#8216;.) </p>
<p> Perl should now build using the win32/Makefile. You will need to edit that file to set </p>
<pre><code> CCTYPE = MSVC80
</code></pre>
<p> and to set CCHOME, CCINCDIR and CCLIBDIR as per the environment setup above. </p>
 </dd>
<dt>Microsoft Visual C++ Toolkit 2003</dt>
<dd> <p> This free toolkit contains the same compiler and linker that ship with Visual C++ .NET 2003 Professional, but doesn&#8217;t contain everything necessary to build Perl. </p>
<p> You will also need to download the ``Platform SDK&#8217;&#8216; (the ``Core SDK&#8217;&#8216; and ``MDAC SDK&#8217;&#8216; components are required) for header files, libraries and rc.exe, and ``.NET Framework SDK&#8217;&#8216; for more libraries and nmake.exe. Note that the latter (which also includes the free compiler and linker) requires the ``.NET Framework Redistributable&#8217;&#8216; to be installed first. This can be downloaded and installed separately, but is included in the ``Visual C++ Toolkit 2003&#8217;&#8216; anyway. </p>
<p> These packages can all be downloaded by searching in the Download Center at &lt;<a rel="nofollow" href="http://www.microsoft.com/downloads/search.aspx?displaylang=en">http://www.microsoft.com/downloads/search.aspx?displaylang=en</a>&gt;. (Providing exact links to these packages has proven a pointless task because the links keep on changing so often.) </p>
<p> Try to obtain the latest version of the Windows SDK. Sometimes these packages contain a particular Windows OS version in their name, but actually work on other OS versions too. For example, the ``Windows Server 2003 R2 Platform SDK&#8217;&#8216; also runs on Windows XP SP2 and Windows 2000. </p>
<p> Install the Toolkit first, then the Platform SDK, then the .NET Framework SDK. Setup your environment as follows (assuming default installation locations were chosen): </p>
<pre><code> SET PlatformSDKDir=C:\Program Files\Microsoft Platform SDK
 SET PATH=%SystemRoot%\system32;%SystemRoot%;C:\Program Files\Microsoft Visual C++ Toolkit 2003\bin;%PlatformSDKDir%\Bin;C:\Program Files\Microsoft.NET\SDK\v1.1\Bin
 SET INCLUDE=C:\Program Files\Microsoft Visual C++ Toolkit 2003\include;%PlatformSDKDir%\include;C:\Program Files\Microsoft Visual Studio .NET 2003\Vc7\include
 SET LIB=C:\Program Files\Microsoft Visual C++ Toolkit 2003\lib;%PlatformSDKDir%\lib;C:\Program Files\Microsoft Visual Studio .NET 2003\Vc7\lib
</code></pre>
<p> (The PlatformSDKDir might need to be set differently depending on which version you are using. Earlier versions installed into ``C:\Program Files\Microsoft SDK&#8217;&#8216;, while the latest versions install into version-specific locations such as ``C:\Program Files\Microsoft Platform SDK for Windows Server 2003 R2&#8217;&#8216;.) </p>
<p> Several required files will still be missing: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> cvtres.exe is required by link.exe when using a .res file. It is actually installed by the .NET Framework SDK, but into a location such as the following: </p>
<pre><code> C:\WINDOWS\Microsoft.NET\Framework\v1.1.4322
</code></pre>
<p> Copy it from there to <code>%PlatformSDKDir</code>%\Bin </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> lib.exe is normally used to build libraries, but link.exe with the /lib option also works, so change win32/config.vc to use it instead: </p>
<p> Change the line reading: </p>
<pre><code>        ar='lib'
</code></pre>
<p> to: </p>
<pre><code>        ar='link /lib'
</code></pre>
<p> It may also be useful to create a batch file called lib.bat in C:\Program Files\Microsoft Visual C++ Toolkit 2003\bin containing: </p>
<pre><code>        @echo off
        link /lib %*
</code></pre>
<p> for the benefit of any naughty C extension modules that you might want to build later which explicitly reference ``lib&#8217;&#8216; rather than taking their value from <code>$Config</code>{ar}. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> setargv.obj is required to build perlglob.exe (and perl.exe if the USE_SETARGV option is enabled). The Platform SDK supplies this object file in source form in <code>%PlatformSDKDir</code>%\src\crt. Copy setargv.c, cruntime.h and internal.h from there to some temporary location and build setargv.obj using </p>
<pre><code>        cl.exe /c /I. /D_CRTBLD setargv.c
</code></pre>
<p> Then copy setargv.obj to <code>%PlatformSDKDir</code>%\lib </p>
<p> Alternatively, if you don&#8217;t need perlglob.exe and don&#8217;t need to enable the USE_SETARGV option then you can safely just remove all mention of $(GLOBEXE) from win32/Makefile and setargv.obj won&#8217;t be required anyway. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> Perl should now build using the win32/Makefile. You will need to edit that file to set </p>
<pre><code>        CCTYPE = MSVC70FREE
</code></pre>
<p> and to set CCHOME, CCINCDIR and CCLIBDIR as per the environment setup above. </p>
 </dd></dl>
<dt>Microsoft Platform SDK 64-bit Compiler</dt>
<dd> <p> The nmake that comes with the Platform SDK will suffice for building Perl. Make sure you are building within one of the ``Build Environment&#8217;&#8216; shells available after you install the Platform SDK from the Start Menu. </p>
 </dd>
<dt>GCC</dt>
<dd> <p> Perl can be compiled with gcc from MinGW (version 3.4.5 or later) or from MinGW64 (version 4.4.3 or later). It can be downloaded here: </p>
<p> &lt;<a rel="nofollow" href="http://www.mingw.org/">http://www.mingw.org/</a>&gt; &lt;<a rel="nofollow" href="http://www.mingw-w64.org/">http://www.mingw-w64.org/</a>&gt; </p>
<p> You also need dmake or gmake. See ``Make&#8217;&#8216; above on how to get it. </p>
<p> Note that the MinGW build currently requires a MinGW runtime version earlier than 3.21 (check __MINGW32_MAJOR_VERSION and __MINGW32_MINOR_VERSION). </p>
<p> Note also that the C++ mode build currently fails with MinGW 3.4.5 and 4.7.2 or later, and with MinGW64 64-bit 6.3.0 or later. </p>
 </dd>
<dt>Intel C++ Compiler</dt>
<dd> <p> Experimental support for using Intel C++ Compiler has been added. Edit win32/Makefile and pick the correct CCTYPE for the Visual C that Intel C was installed into. Also uncomment __ICC to enable Intel C on Visual C support. To set up the build environment, from the Start Menu run IA-32 Visual Studio 20__ mode or Intel 64 Visual Studio 20__ mode as appropriate. Then run nmake as usually in that prompt box. </p>
<p> Only Intel C++ Compiler v12.1 has been tested. Other versions probably will work. Using Intel C++ Compiler instead of Visual C has the benefit of C99 compatibility which is needed by some CPAN XS modules, while maintaining compatibility with Visual C object code and Visual C debugging infrastructure unlike GCC. </p>
 </dd></dl>
<h3>Building</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Make sure you are in the ``win32&#8217;&#8216; subdirectory under the perl toplevel. This directory contains a ``Makefile&#8217;&#8216; that will work with versions of nmake that come with Visual C++ or the Windows SDK, and a GNU make ``GNUmakefile&#8217;&#8216; or dmake ``makefile.mk&#8217;&#8216; that will work for all supported compilers. The defaults in the gmake and dmake makefile are setup to build using MinGW/gcc. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Edit the GNUmakefile, makefile.mk (or Makefile, if you&#8217;re using nmake) and change the values of INST_DRV and INST_TOP. You can also enable various build flags. These are explained in the makefiles. </p>
<p> Note that it is generally not a good idea to try to build a perl with INST_DRV and INST_TOP set to a path that already exists from a previous build. In particular, this may cause problems with the lib/ExtUtils/t/Embed.t test, which attempts to build a test program and may end up building against the installed perl&#8217;s lib/CORE directory rather than the one being tested. </p>
<p> You will have to make sure that CCTYPE is set correctly and that CCHOME points to wherever you installed your compiler. For GCC this should be the directory that contains the <i>bin</i>, <i>include</i> and <i>lib</i> directories. </p>
<p> If building with the cross-compiler provided by mingw-w64.org you&#8217;ll need to uncomment the line that sets GCCCROSS in the makefile.mk. Do this only if it&#8217;s the cross-compiler - ie only if the bin folder doesn&#8217;t contain a gcc.exe. (The cross-compiler does not provide a gcc.exe, g++.exe, ar.exe, etc. Instead, all of these executables are prefixed with &#8216;x86_64-w64-mingw32-&#8216;.) </p>
<p> The default value for CCHOME in the makefiles for Visual C++ may not be correct for some versions. Make sure the default exists and is valid. </p>
<p> You may also need to comment out the <code>&quot;DELAYLOAD = ...&quot;</code> line in the Makefile if you&#8217;re using VC++ 6.0 without the latest service pack and the linker reports an internal error. </p>
<p> If you want build some core extensions statically into perl&#8217;s dll, specify them in the STATIC_EXT macro. </p>
<p> NOTE: The USE_64_BIT_INT build option is not supported with the 32-bit Visual C++ 6.0 compiler. </p>
<p> Be sure to read the instructions near the top of the makefiles carefully. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Type ``dmake&#8217;&#8216; (``gmake&#8217;&#8216; for GNU make, or ``nmake&#8217;&#8216; if you are using that make). </p>
<p> This should build everything. Specifically, it will create perl.exe, perl530.dll at the perl toplevel, and various other extension dll&#8217;s under the lib\auto directory. If the build fails for any reason, make sure you have done the previous steps correctly. </p>
<p> To try dmake&#8217;s parallel mode, type ``dmake -P2&#8217;&#8216;, where 2, is the maximum number of parallel jobs you want to run. A number of things in the build process will run in parallel, but there are serialization points where you will see just 1 CPU maxed out. This is normal. </p>
<p> Similarly you can build in parallel with GNU make, type ``gmake -j2&#8217;&#8216; to build with two parallel jobs, or higher for more. </p>
<p> If you are advanced enough with building C code, here is a suggestion to speed up building perl, and the later <code>&quot;make test&quot;</code>. Try to keep your PATH environmental variable with the least number of folders possible (remember to keep your C compiler&#8217;s folders there). <code>&quot;C:\WINDOWS\system32&quot;</code> or <code>&quot;C:\WINNT\system32&quot;</code> depending on your OS version should be first folder in PATH, since ``cmd.exe&#8217;&#8216; is the most commonly launched program during the build and later testing. </p>
 </dd></dl>
<h3>Testing Perl on Windows</h3>
<p> Type ``dmake test&#8217;&#8216; (or ``gmake test&#8217;&#8216;, ``nmake test&#8217;&#8216;). This will run most of the tests from the testsuite (many tests will be skipped). </p>
<p> There should be no test failures. </p>
<p> If you build with Visual C++ 2013 then three tests currently may fail with Daylight Saving Time related problems: <i>t/io/fs.t</i>, <i>cpan/HTTP-Tiny/t/110_mirror.t</i> and <i>lib/File/Copy.t</i>. The failures are caused by bugs in the CRT in VC++ 2013 which are fixed in VC++2015 and later, as explained by Microsoft here: &lt;<a rel="nofollow" href="https://connect.microsoft.com/VisualStudio/feedback/details/811534/utime-sometimes-fails-to-set-the-correct-file-times-in-visual-c-2013">https://connect.microsoft.com/VisualStudio/feedback/details/811534/utime-sometimes-fails-to-set-the-correct-file-times-in-visual-c-2013</a>&gt;. In the meantime, if you need fixed <code>&quot;stat&quot;</code> and <code>&quot;utime&quot;</code> functions then have a look at the CPAN distribution Win32::UTCFileTime. </p>
<p> If you build with Visual C++ 2015 or later then <i>ext/XS-APItest/t/locale.t</i> may crash (after all its tests have passed). This is due to a regression in the Universal CRT introduced in the Windows 10 April 2018 Update, and will be fixed in the May 2019 Update, as explained here: &lt;<a rel="nofollow" href="https://developercommunity.visualstudio.com/content/problem/519486/setlocalelc-numeric-iso-latin-16-fails-then-succee.html">https://developercommunity.visualstudio.com/content/problem/519486/setlocalelc-numeric-iso-latin-16-fails-then-succee.html</a>&gt;. </p>
<p> If you build with certain versions (e.g. 4.8.1) of gcc from <a rel="nofollow" href="http://www.mingw.org">www.mingw.org</a> then <i>ext/POSIX/t/time.t</i> may fail test 17 due to a known bug in those gcc builds: see &lt;<a rel="nofollow" href="http://sourceforge.net/p/mingw/bugs/2152/">http://sourceforge.net/p/mingw/bugs/2152/</a>&gt;. </p>
<p> Some test failures may occur if you use a command shell other than the native ``cmd.exe&#8217;&#8216;, or if you are building from a path that contains spaces. So don&#8217;t do that. </p>
<p> If you are running the tests from a emacs shell window, you may see failures in op/stat.t. Run ``dmake test-notty&#8217;&#8216; in that case. </p>
<p> Furthermore, you should make sure that during <code>&quot;make test&quot;</code> you do not have any GNU tool packages in your path: some toolkits like Unixutils include some tools (<code>&quot;type&quot;</code> for instance) which override the Windows ones and makes tests fail. Remove them from your path while testing to avoid these errors. </p>
<p> To see the output of specific failing tests run the harness from the t directory: </p>
<pre><code>  # assuming you're starting from the win32 directory
  cd ..\win32
  .\perl harness &lt;list of tests&gt;
</code></pre>
<p> Please report any other failures as described under ``BUGS AND CAVEATS&#8217;&#8216;.  </p>
<h3>Installation of Perl on Windows</h3>
<p> Type ``dmake install&#8217;&#8216; (or ``gmake install&#8217;&#8216;, ``nmake install&#8217;&#8216;). This will put the newly built perl and the libraries under whatever <code>&quot;INST_TOP&quot;</code> points to in the Makefile. It will also install the pod documentation under <code>&quot;$INST_TOP\$INST_VER\lib\pod&quot;</code> and HTML versions of the same under <code>&quot;$INST_TOP\$INST_VER\lib\pod\html&quot;</code>. </p>
<p> To use the Perl you just installed you will need to add a new entry to your PATH environment variable: <code>&quot;$INST_TOP\bin&quot;</code>, e.g. </p>
<pre><code>    set PATH=c:\perl\bin;%PATH%
</code></pre>
<p> If you opted to uncomment <code>&quot;INST_VER&quot;</code> and <code>&quot;INST_ARCH&quot;</code> in the makefile then the installation structure is a little more complicated and you will need to add two new PATH components instead: <code>&quot;$INST_TOP\$INST_VER\bin&quot;</code> and <code>&quot;$INST_TOP\$INST_VER\bin\$ARCHNAME&quot;</code>, e.g. </p>
<pre><code>    set PATH=c:\perl\5.6.0\bin;c:\perl\5.6.0\bin\MSWin32-x86;%PATH%
</code></pre>
<h3>Usage Hints for Perl on Windows</h3>
<dl>
<dt>Environment Variables</dt>
<dd> <p> The installation paths that you set during the build get compiled into perl, so you don&#8217;t have to do anything additional to start using that perl (except add its location to your PATH variable). </p>
<p> If you put extensions in unusual places, you can set PERL5LIB to a list of paths separated by semicolons where you want perl to look for libraries. Look for descriptions of other environment variables you can set in perlrun. </p>
<p> You can also control the shell that perl uses to run <code>system()</code> and backtick commands via PERL5SHELL. See perlrun. </p>
<p> Perl does not depend on the registry, but it can look up certain default values if you choose to put them there unless disabled at build time with USE_NO_REGISTRY. On Perl process start Perl checks if <code>&quot;HKEY_CURRENT_USER\Software\Perl&quot;</code> and <code>&quot;HKEY_LOCAL_MACHINE\Software\Perl&quot;</code> exist. If the keys exists, they will be checked for remainder of the Perl process&#8217;s run life for certain entries. Entries in <code>&quot;HKEY_CURRENT_USER\Software\Perl&quot;</code> override entries in <code>&quot;HKEY_LOCAL_MACHINE\Software\Perl&quot;</code>. One or more of the following entries (of type REG_SZ or REG_EXPAND_SZ) may be set in the keys: </p>
<pre><code> lib-$] version-specific standard library path to add to @INC
 lib standard library path to add to @INC
 sitelib-$] version-specific site library path to add to @INC
 sitelib site library path to add to @INC
 vendorlib-$] version-specific vendor library path to add to @INC
 vendorlib vendor library path to add to @INC
 PERL* fallback for all %ENV lookups that begin with &quot;PERL&quot;
</code></pre>
<p> Note the <code>$]</code> in the above is not literal. Substitute whatever version of perl you want to honor that entry, e.g. <code>5.6.0</code>. Paths must be separated with semicolons, as usual on Windows. </p>
 </dd>
<dt>File Globbing</dt>
<dd> <p> By default, perl handles file globbing using the File::Glob extension, which provides portable globbing. </p>
<p> If you want perl to use globbing that emulates the quirks of DOS filename conventions, you might want to consider using File::DosGlob to override the internal <code>glob()</code> implementation. See File::DosGlob for details. </p>
 </dd>
<dt>Using perl from the command line</dt>
<dd> <p> If you are accustomed to using perl from various command-line shells found in UNIX environments, you will be less than pleased with what Windows offers by way of a command shell. </p>
<p> The crucial thing to understand about the Windows environment is that the command line you type in is processed twice before Perl sees it. First, your command shell (usually CMD.EXE) preprocesses the command line, to handle redirection, environment variable expansion, and location of the executable to run. Then, the perl executable splits the remaining command line into individual arguments, using the C runtime library upon which Perl was built. </p>
<p> It is particularly important to note that neither the shell nor the C runtime do any wildcard expansions of command-line arguments (so wildcards need not be quoted). Also, the quoting behaviours of the shell and the C runtime are rudimentary at best (and may, if you are using a non-standard shell, be inconsistent). The only (useful) quote character is the double quote (&quot;). It can be used to protect spaces and other special characters in arguments. </p>
<p> The Windows documentation describes the shell parsing rules here: &lt;<a rel="nofollow" href="http://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/cmd.mspx?mfr=true">http://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/cmd.mspx?mfr=true</a>&gt; and the C runtime parsing rules here: &lt;<a rel="nofollow" href="http://msdn.microsoft.com/en-us/library/17w5ykft%28v=VS.100%29.aspx">http://msdn.microsoft.com/en-us/library/17w5ykft%28v=VS.100%29.aspx</a>&gt;. </p>
<p> Here are some further observations based on experiments: The C runtime breaks arguments at spaces and passes them to programs in argc/argv. Double quotes can be used to prevent arguments with spaces in them from being split up. You can put a double quote in an argument by escaping it with a backslash and enclosing the whole argument within double quotes. The backslash and the pair of double quotes surrounding the argument will be stripped by the C runtime. </p>
<p> The file redirection characters ``&lt;&#8216;&#8216;, ``&gt;&#8216;&#8216;, and ``|&#8216;&#8216; can be quoted by double quotes (although there are suggestions that this may not always be true). Single quotes are not treated as quotes by the shell or the C runtime, they don&#8217;t get stripped by the shell (just to make this type of quoting completely useless). The caret ``^&#8216;&#8216; has also been observed to behave as a quoting character, but this appears to be a shell feature, and the caret is not stripped from the command line, so Perl still sees it (and the C runtime phase does not treat the caret as a quote character). </p>
<p> Here are some examples of usage of the ``cmd&#8217;&#8216; shell: </p>
<p> This prints two doublequotes: </p>
<pre><code>    perl -e &quot;print '\&quot;\&quot;' &quot;
</code></pre>
<p> This does the same: </p>
<pre><code>    perl -e &quot;print \&quot;\\\&quot;\\\&quot;\&quot; &quot;
</code></pre>
<p> This prints ``bar&#8217;&#8216; and writes ``foo&#8217;&#8216; to the file ``blurch&#8217;&#8216;: </p>
<pre><code>    perl -e &quot;print 'foo'; print STDERR 'bar'&quot; &gt; blurch
</code></pre>
<p> This prints ``foo&#8217;&#8216; (``bar&#8217;&#8216; disappears into nowhereland): </p>
<pre><code>    perl -e &quot;print 'foo'; print STDERR 'bar'&quot; 2&gt; nul
</code></pre>
<p> This prints ``bar&#8217;&#8216; and writes ``foo&#8217;&#8216; into the file ``blurch&#8217;&#8216;: </p>
<pre><code>    perl -e &quot;print 'foo'; print STDERR 'bar'&quot; 1&gt; blurch
</code></pre>
<p> This pipes ``foo&#8217;&#8216; to the ``less&#8217;&#8216; pager and prints ``bar&#8217;&#8216; on the console: </p>
<pre><code>    perl -e &quot;print 'foo'; print STDERR 'bar'&quot; | less
</code></pre>
<p> This pipes ``foo\nbar\n&#8217;&#8216; to the less pager: </p>
<pre><code>    perl -le &quot;print 'foo'; print STDERR 'bar'&quot; 2&gt;&amp;1 | less
</code></pre>
<p> This pipes ``foo&#8217;&#8216; to the pager and writes ``bar&#8217;&#8216; in the file ``blurch&#8217;&#8216;: </p>
<pre><code>    perl -e &quot;print 'foo'; print STDERR 'bar'&quot; 2&gt; blurch | less
</code></pre>
<p> Discovering the usefulness of the ``command.com&#8217;&#8216; shell on Windows 9x is left as an exercise to the reader :) </p>
<p> One particularly pernicious problem with the 4NT command shell for Windows is that it (nearly) always treats a % character as indicating that environment variable expansion is needed. Under this shell, it is therefore important to always double any % characters which you want Perl to see (for example, for hash variables), even when they are quoted. </p>
 </dd>
<dt>Building Extensions</dt>
<dd> <p> The Comprehensive Perl Archive Network (CPAN) offers a wealth of extensions, some of which require a C compiler to build. Look in &lt;<a rel="nofollow" href="http://www.cpan.org/">http://www.cpan.org/</a>&gt; for more information on CPAN. </p>
<p> Note that not all of the extensions available from CPAN may work in the Windows environment; you should check the information at &lt;<a rel="nofollow" href="http://www.cpantesters.org/">http://www.cpantesters.org/</a>&gt; before investing too much effort into porting modules that don&#8217;t readily build. </p>
<p> Most extensions (whether they require a C compiler or not) can be built, tested and installed with the standard mantra: </p>
<pre><code>    perl Makefile.PL
    $MAKE
    $MAKE test
    $MAKE install
</code></pre>
<p> where <code>$MAKE</code> is whatever &#8216;make&#8217; program you have configured perl to use. Use ``perl -V:make&#8217;&#8216; to find out what this is. Some extensions may not provide a testsuite (so ``$MAKE test&#8217;&#8216; may not do anything or fail), but most serious ones do. </p>
<p> It is important that you use a supported &#8216;make&#8217; program, and ensure Config.pm knows about it. If you don&#8217;t have nmake, you can either get dmake from the location mentioned earlier or get an old version of nmake reportedly available from: </p>
<p> &lt;<a rel="nofollow" href="http://download.microsoft.com/download/vc15/Patch/1.52/W95/EN-US/nmake15.exe">http://download.microsoft.com/download/vc15/Patch/1.52/W95/EN-US/nmake15.exe</a>&gt; </p>
<p> Another option is to use the make written in Perl, available from CPAN. </p>
<p> &lt;<a rel="nofollow" href="http://www.cpan.org/modules/by-module/Make/">http://www.cpan.org/modules/by-module/Make/</a>&gt; </p>
<p> You may also use dmake or gmake. See ``Make&#8217;&#8216; above on how to get it. </p>
<p> Note that MakeMaker actually emits makefiles with different syntax depending on what &#8216;make&#8217; it thinks you are using. Therefore, it is important that one of the following values appears in Config.pm: </p>
<pre><code>    make='nmake' # MakeMaker emits nmake syntax
    make='dmake' # MakeMaker emits dmake syntax
    any other value # MakeMaker emits generic make syntax
                            (e.g GNU make, or Perl make)
</code></pre>
<p> If the value doesn&#8217;t match the &#8216;make&#8217; program you want to use, edit Config.pm to fix it. </p>
<p> If a module implements XSUBs, you will need one of the supported C compilers. You must make sure you have set up the environment for the compiler for command-line compilation before running <code>&quot;perl Makefile.PL&quot;</code> or any invocation of make. </p>
<p> If a module does not build for some reason, look carefully for why it failed, and report problems to the module author. If it looks like the extension building support is at fault, report that with full details of how the build failed using the perlbug utility. </p>
 </dd>
<dt>Command-line Wildcard Expansion</dt>
<dd> <p> The default command shells on DOS descendant operating systems (such as they are) usually do not expand wildcard arguments supplied to programs. They consider it the application&#8217;s job to handle that. This is commonly achieved by linking the application (in our case, perl) with startup code that the C runtime libraries usually provide. However, doing that results in incompatible perl versions (since the behavior of the argv expansion code differs depending on the compiler, and it is even buggy on some compilers). Besides, it may be a source of frustration if you use such a perl binary with an alternate shell that *does* expand wildcards. </p>
<p> Instead, the following solution works rather well. The nice things about it are 1) you can start using it right away; 2) it is more powerful, because it will do the right thing with a pattern like */*/*.c; 3) you can decide whether you do/don&#8217;t want to use it; and 4) you can extend the method to add any customizations (or even entirely different kinds of wildcard expansion). </p>
<pre><code> C:\&gt; copy con c:\perl\lib\Wild.pm
 # Wild.pm - emulate shell @ARGV expansion on shells that don't
 use File::DosGlob;
 @ARGV = map {
              my @g = File::DosGlob::glob($_) if /[*?]/;
              @g ? @g : $_;
            } @ARGV;
 1;
 ^Z
 C:\&gt; set PERL5OPT=-MWild
 C:\&gt; perl -le &quot;for (@ARGV) { print }&quot; */*/perl*.c
 p4view/perl/perl.c
 p4view/perl/perlio.c
 p4view/perl/perly.c
 perl5.005/win32/perlglob.c
 perl5.005/win32/perllib.c
 perl5.005/win32/perlglob.c
 perl5.005/win32/perllib.c
 perl5.005/win32/perlglob.c
 perl5.005/win32/perllib.c
</code></pre>
<p> Note there are two distinct steps there: 1) You&#8217;ll have to create Wild.pm and put it in your perl lib directory. 2) You&#8217;ll need to set the PERL5OPT environment variable. If you want argv expansion to be the default, just set PERL5OPT in your default startup environment. </p>
<p> If you are using the Visual C compiler, you can get the C runtime&#8217;s command line wildcard expansion built into perl binary. The resulting binary will always expand unquoted command lines, which may not be what you want if you use a shell that does that for you. The expansion done is also somewhat less powerful than the approach suggested above. </p>
 </dd>
<dt>Notes on 64-bit Windows</dt>
<dd> <p> Windows .NET Server supports the LLP64 data model on the Intel Itanium architecture. </p>
<p> The LLP64 data model is different from the LP64 data model that is the norm on 64-bit Unix platforms. In the former, <code>&quot;int&quot;</code> and <code>&quot;long&quot;</code> are both 32-bit data types, while pointers are 64 bits wide. In addition, there is a separate 64-bit wide integral type, <code>&quot;__int64&quot;</code>. In contrast, the LP64 data model that is pervasive on Unix platforms provides <code>&quot;int&quot;</code> as the 32-bit type, while both the <code>&quot;long&quot;</code> type and pointers are of 64-bit precision. Note that both models provide for 64-bits of addressability. </p>
<p> 64-bit Windows running on Itanium is capable of running 32-bit x86 binaries transparently. This means that you could use a 32-bit build of Perl on a 64-bit system. Given this, why would one want to build a 64-bit build of Perl? Here are some reasons why you would bother: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> A 64-bit native application will run much more efficiently on Itanium hardware. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> There is no 2GB limit on process size. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl automatically provides large file support when built under 64-bit Windows. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Embedding Perl inside a 64-bit application. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<h3>Running Perl Scripts</h3>
<p> Perl scripts on UNIX use the ``#!&#8216;&#8216; (a.k.a ``shebang&#8217;&#8216;) line to indicate to the OS that it should execute the file using perl. Windows has no comparable means to indicate arbitrary files are executables. </p>
<p> Instead, all available methods to execute plain text files on Windows rely on the file ``extension&#8217;&#8216;. There are three methods to use this to execute perl scripts: </p>
<dl>
<dt>1.</dt>
<dd> <p> There is a facility called ``file extension associations&#8217;&#8216;. This can be manipulated via the two commands ``assoc&#8217;&#8216; and ``ftype&#8217;&#8216; that come standard with Windows. Type ``ftype /?&#8216;&#8216; for a complete example of how to set this up for perl scripts (Say what? You thought Windows wasn&#8217;t perl-ready? :). </p>
 </dd>
<dt>2.</dt>
<dd> <p> Since file associations don&#8217;t work everywhere, and there are reportedly bugs with file associations where it does work, the old method of wrapping the perl script to make it look like a regular batch file to the OS, may be used. The install process makes available the ``pl2bat.bat&#8217;&#8216; script which can be used to wrap perl scripts into batch files. For example: </p>
<pre><code>        pl2bat foo.pl
</code></pre>
<p> will create the file ``FOO.BAT&#8217;&#8216;. Note ``pl2bat&#8217;&#8216; strips any .pl suffix and adds a .bat suffix to the generated file. </p>
<p> If you use the 4DOS/NT or similar command shell, note that ``pl2bat&#8217;&#8216; uses the ``%*&#8216;&#8216; variable in the generated batch file to refer to all the command line arguments, so you may need to make sure that construct works in batch files. As of this writing, 4DOS/NT users will need a ``ParameterChar = *&#8216;&#8216; statement in their 4NT.INI file or will need to execute ``setdos /p*&#8216;&#8216; in the 4DOS/NT startup file to enable this to work. </p>
 </dd>
<dt>3.</dt>
<dd> <p> Using ``pl2bat&#8217;&#8216; has a few problems: the file name gets changed, so scripts that rely on <code>$0</code> to find what they must do may not run properly; running ``pl2bat&#8217;&#8216; replicates the contents of the original script, and so this process can be maintenance intensive if the originals get updated often. A different approach that avoids both problems is possible. </p>
<p> A script called ``runperl.bat&#8217;&#8216; is available that can be copied to any filename (along with the .bat suffix). For example, if you call it ``foo.bat&#8217;&#8216;, it will run the file ``foo&#8217;&#8216; when it is executed. Since you can run batch files on Windows platforms simply by typing the name (without the extension), this effectively runs the file ``foo&#8217;&#8216;, when you type either ``foo&#8217;&#8216; or ``foo.bat&#8217;&#8216;. With this method, ``foo.bat&#8217;&#8216; can even be in a different location than the file ``foo&#8217;&#8216;, as long as ``foo&#8217;&#8216; is available somewhere on the PATH. If your scripts are on a filesystem that allows symbolic links, you can even avoid copying ``runperl.bat&#8217;&#8216;. </p>
<p> Here&#8217;s a diversion: copy ``runperl.bat&#8217;&#8216; to ``runperl&#8217;&#8216;, and type ``runperl&#8217;&#8216;. Explain the observed behavior, or lack thereof. :) Hint: .gnidnats llits er&#8217;uoy fi ,``lrepnur&#8217;&#8216; eteled :tniH </p>
 </dd></dl>
<h3>Miscellaneous Things</h3>
<p> A full set of HTML documentation is installed, so you should be able to use it if you have a web browser installed on your system. </p>
<p> <code>&quot;perldoc&quot;</code> is also a useful tool for browsing information contained in the documentation, especially in conjunction with a pager like <code>&quot;less&quot;</code> (recent versions of which have Windows support). You may have to set the PAGER environment variable to use a specific pager. ``perldoc -f foo&#8217;&#8216; will print information about the perl operator ``foo&#8217;&#8216;. </p>
<p> One common mistake when using this port with a GUI library like <code>&quot;Tk&quot;</code> is assuming that Perl&#8217;s normal behavior of opening a command-line window will go away. This isn&#8217;t the case. If you want to start a copy of <code>&quot;perl&quot;</code> without opening a command-line window, use the <code>&quot;wperl&quot;</code> executable built during the installation process. Usage is exactly the same as normal <code>&quot;perl&quot;</code> on Windows, except that options like <code>&quot;-h&quot;</code> don&#8217;t work (since they need a command-line window to print to). </p>
<p> If you find bugs in perl, you can run <code>&quot;perlbug&quot;</code> to create a bug report (you may have to send it manually if <code>&quot;perlbug&quot;</code> cannot find a mailer on your system).  </p>
<h2>BUGS AND CAVEATS</h2>
<p> Norton AntiVirus interferes with the build process, particularly if set to ``AutoProtect, All Files, when Opened&#8217;&#8216;. Unlike large applications the perl build process opens and modifies a lot of files. Having the the AntiVirus scan each and every one slows build the process significantly. Worse, with PERLIO=stdio the build process fails with peculiar messages as the virus checker interacts badly with miniperl.exe writing configure files (it seems to either catch file part written and treat it as suspicious, or virus checker may have it ``locked&#8217;&#8216; in a way which inhibits miniperl updating it). The build does complete with </p>
<pre><code>   set PERLIO=perlio
</code></pre>
<p> but that may be just luck. Other AntiVirus software may have similar issues. </p>
<p> A git GUI shell extension for Windows such as TortoiseGit will cause the build and later <code>&quot;make test&quot;</code> to run much slower since every file is checked for its git status as soon as it is created and/or modified. TortoiseGit doesn&#8217;t cause any test failures or build problems unlike the antivirus software described above, but it does cause similar slowness. It is suggested to use Task Manager to look for background processes which use high CPU amounts during the building process. </p>
<p> Some of the built-in functions do not act exactly as documented in perlfunc, and a few are not implemented at all. To avoid surprises, particularly if you have had prior exposure to Perl in other operating environments or if you intend to write code that will be portable to other environments, see perlport for a reasonably definitive list of these differences. </p>
<p> Not all extensions available from CPAN may build or work properly in the Windows environment. See ``Building Extensions&#8217;&#8216;. </p>
<p> Most <code>&quot;socket()&quot;</code> related calls are supported, but they may not behave as on Unix platforms. See perlport for the full list. </p>
<p> Signal handling may not behave as on Unix platforms (where it doesn&#8217;t exactly ``behave&#8217;&#8216;, either :). For instance, calling <code>&quot;die()&quot;</code> or <code>&quot;exit()&quot;</code> from signal handlers will cause an exception, since most implementations of <code>&quot;signal()&quot;</code> on Windows are severely crippled. Thus, signals may work only for simple things like setting a flag variable in the handler. Using signals under this port should currently be considered unsupported. </p>
<p> Please send detailed descriptions of any problems and solutions that you may find to &lt;<i>perlbug [at] perl.org</i>&gt;, along with the output produced by <code>&quot;perl -V&quot;</code>.  </p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> The use of a camel with the topic of Perl is a trademark of O&#8217;Reilly and Associates, Inc. Used with permission.  </p>
<h2>AUTHORS</h2>
<dl>
<dt>Gary Ng &lt;71564.1743 [at] CompuServe.COM&gt;</dt>
<dd>  </dd>
<dt>Gurusamy Sarathy &lt;gsar [at] activestate.com&gt;</dt>
<dd>  </dd>
<dt>Nick Ing-Simmons &lt;nick [at] ing-simmons.net&gt;</dt>
<dd>  </dd>
<dt>Jan Dubois &lt;jand [at] activestate.com&gt;</dt>
<dd>  </dd>
<dt>Steve Hay &lt;steve.m.hay [at] googlemail.com&gt;</dt>
<dd>  </dd></dl>
<p> This document is maintained by Jan Dubois.  </p>
<h2>SEE ALSO</h2>
<p> perl  </p>
<h2>HISTORY</h2>
<p> This port was originally contributed by Gary Ng around 5.003_24, and borrowed from the Hip Communications port that was available at the time. Various people have made numerous and sundry hacks since then. </p>
<p> GCC/mingw32 support was added in 5.005 (Nick Ing-Simmons). </p>
<p> Support for PERL_OBJECT was added in 5.005 (ActiveState Tool Corp). </p>
<p> Support for <code>fork()</code> emulation was added in 5.6 (ActiveState Tool Corp). </p>
<p> Win9x support was added in 5.6 (Benjamin Stuhl). </p>
<p> Support for 64-bit Windows added in 5.8 (ActiveState Corp). </p>
<p> Last updated: 30 April 2019 </p>
