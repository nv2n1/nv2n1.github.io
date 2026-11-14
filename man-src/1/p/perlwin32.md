---
title: "perlwin32(1)"
name: "perlwin32"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlwin32/"
description: "perlwin32 – Perl under Windows"
---

<h2 class="name">NAME</h2>
<p> perlwin32 &#8211; Perl under Windows </p>
<h2>SYNOPSIS</h2>
<p> These are instructions for building Perl under Windows 2000 and later.</p>
<h2>DESCRIPTION</h2>
<p> Before you start, you should glance through the <font SIZE="-1">README</font> file found in the top-level directory to which the Perl distribution was extracted. Make sure you read and understand the terms under which this software is being distributed. </p>
<p> Also make sure you read &#8220;<font SIZE="-1">BUGS AND CAVEATS&#8221;</font> below for the known limitations of this port. </p>
<p> The <font SIZE="-1">INSTALL</font> file in the perl top-level has much information that is only relevant to people building Perl on Unix-like systems. In particular, you can safely ignore any information that talks about &#8220;Configure&#8221;. </p>
<p> You may also want to look at one other option for building a perl that will work on Windows: the <font SIZE="-1">README</font>.cygwin file, which give a different set of rules to build a perl for Windows. This method will probably enable you to build a more Unix-compatible perl, but you will also need to download and use various other build-time and run-time support software described in that file. </p>
<p> This set of instructions is meant to describe a so-called &#8220;native&#8221; port of Perl to the Windows platform. This includes both 32-bit and 64-bit Windows operating systems. The resulting Perl requires no additional software to run (other than what came with your operating system). Currently, this port is capable of using one of the following compilers on the Intel x86 architecture: </p>
<pre>
      Microsoft Visual C++    version 6.0 or later
      Intel C++ Compiler      (experimental)
      Gcc by mingw.org        gcc version 3.4.5 or later
                              with runtime &lt; 3.21
      Gcc by mingw-w64.org    gcc version 4.4.3 or later
</pre>
<p> Note that the last two of these are actually competing projects both delivering complete gcc toolchain for <font SIZE="-1">MS</font> Windows:</p>
<dl>
<dt>&lt;<a rel="nofollow" href="http://mingw.org">http://mingw.org</a>&gt;</p>
<dd> Delivers gcc toolchain targeting 32-bit Windows platform.</p>
<dt>&lt;<a rel="nofollow" href="http://mingw-w64.org">http://mingw-w64.org</a>&gt;</p>
<dd> Delivers gcc toolchain targeting both 64-bit Windows and 32-bit Windows platforms (despite the project name &#8220;mingw-w64&#8221; they are not only 64-bit oriented). They deliver the native gcc compilers and cross-compilers that are also supported by perl&#8217;s makefile.</dl>
<p> The Microsoft Visual C<font SIZE="-2">++</font> compilers are also now being given away free. They are available as &#8220;Visual C<font SIZE="-2">++</font> Toolkit 2003&#8221; or &#8220;Visual C<font SIZE="-2">++</font> 2005-2019 Express [or Community, from 2017] Edition&#8221; (and also as part of the &#8220;.NET Framework <font SIZE="-1">SDK&#8221;</font>) and are the same compilers that ship with &#8220;Visual C<font SIZE="-2">++</font> .NET 2003 Professional&#8221; or &#8220;Visual C<font SIZE="-2">++</font> 2005-2019 Professional&#8221; respectively. </p>
<p> This port can also be built on <font SIZE="-1">IA64/AMD64</font> using: </p>
<pre>
      Microsoft Platform SDK    Nov 2001 (64-bit compiler and tools)
      MinGW64 compiler (gcc version 4.4.3 or later)
</pre>
<p> The Windows <font SIZE="-1">SDK</font> can be downloaded from &lt;<a rel="nofollow" href="http://www.microsoft.com/">http://www.microsoft.com/</a>&gt;. The MinGW64 compiler is available at &lt;<a rel="nofollow" href="http://mingw-w64.org">http://mingw-w64.org</a>&gt;. The latter is actually a cross-compiler targeting Win64. There&#8217;s also a trimmed down compiler (no java, or gfortran) suitable for building perl available at: &lt;<a rel="nofollow" href="http://strawberryperl.com/package/kmx/64_gcctoolchain/">http://strawberryperl.com/package/kmx/64_gcctoolchain/</a>&gt; </p>
<p> <font SIZE="-1">NOTE:</font> If you&#8217;re using a 32-bit compiler to build perl on a 64-bit Windows operating system, then you should set the <font SIZE="-1">WIN64</font> environment variable to &#8220;undef&#8221;. Also, the trimmed down compiler only passes tests when <font SIZE="-1">USE_ITHREADS</font> *= define (as opposed to undef) and when the <font SIZE="-1">CFG</font> *= Debug line is commented out. </p>
<p> This port fully supports MakeMaker (the set of modules that is used to build extensions to perl). Therefore, you should be able to build and install most extensions found in the <font SIZE="-1">CPAN</font> sites. See &#8220;Usage Hints for Perl on Windows&#8221; below for general hints about this.</p>
<h3>Setting Up Perl on Windows</h3>
<dl>
<dt>Make</p>
<dd> You need a &#8220;make&#8221; program to build the sources. If you are using Visual C<font SIZE="-2">++</font> or the Windows <font SIZE="-1">SDK</font> tools, you can use nmake supplied with Visual C<font SIZE="-2">++</font> or Windows <font SIZE="-1">SDK.</font> You may also use, for Visual C<font SIZE="-2">++</font> or Windows <font SIZE="-1">SDK,</font> dmake or gmake instead of nmake. dmake is open source software, but is not included with Visual C<font SIZE="-2">++</font> or Windows <font SIZE="-1">SDK.</font> Builds using gcc need dmake or gmake. nmake is not supported for gcc builds. Parallel building is only supported with dmake and gmake, not nmake. When using dmake it is recommended to use dmake 4.13 or newer for parallel building. Older dmakes, in parallel mode, have very high <font SIZE="-1">CPU</font> usage and pound the disk/filing system with duplicate I/O calls in an aggressive polling loop. </p>
<p> A port of dmake for Windows is available from: </p>
<p> &lt;<a rel="nofollow" href="http://search.cpan.org/dist/dmake/">http://search.cpan.org/dist/dmake/</a>&gt; </p>
<p> Fetch and install dmake somewhere on your path.</p>
<dt>Command Shell</p>
<dd> Use the default &#8220;cmd&#8221; shell that comes with Windows. Some versions of the popular 4DOS/NT shell have incompatibilities that may cause you trouble. If the build fails under that shell, try building again with the cmd shell. </p>
<p> Make sure the path to the build directory does not contain spaces. The build usually works in this circumstance, but some tests will fail.</p>
<dt>Microsoft Visual C<font SIZE="-2">++</font></p>
<dd> The nmake that comes with Visual C<font SIZE="-2">++</font> will suffice for building. Visual C requires that certain things be set up in the console before Visual C will sucessfully run. To make a console box be able to run the C compiler, you will need to beforehand, run the <tt>&quot;vcvars32.bat&quot;</tt> file to compile for x86-32 and for x86-64 <tt>&quot;vcvarsall.bat x64&quot;</tt> or <tt>&quot;vcvarsamd64.bat&quot;</tt>. On a typical install of a Microsoft C compiler product, these batch files will already be in your <tt>&quot;PATH&quot;</tt> environment variable so you may just type them without an absolute path into your console. If you need to find the absolute path to the batch file, it is usually found somewhere like C:\Program Files\Microsoft Visual Studio\VC98\Bin. With some newer Micrsoft C products (released after ~2004), the installer will put a shortcut in the start menu to launch a new console window with the console already set up for your target architecture (x86-32 or x86-64 or <font SIZE="-1">IA64</font>). With the newer compilers, you may also use the older batch files if you choose so.</p>
<dt>Microsoft Visual C<font SIZE="-2">++</font> 2008-2019 Express/Community Edition</p>
<dd> These free versions of Visual C<font SIZE="-2">++</font> 2008-2019 Professional contain the same compilers and linkers that ship with the full versions, and also contain everything necessary to build Perl, rather than requiring a separate download of the Windows <font SIZE="-1">SDK</font> like previous versions did. </p>
<p> These packages can be downloaded by searching in the Download Center at &lt;<a rel="nofollow" href="http://www.microsoft.com/downloads/search.aspx?displaylang=en">http://www.microsoft.com/downloads/search.aspx?displaylang=en</a>&gt;. (Providing exact links to these packages has proven a pointless task because the links keep on changing so often.) </p>
<p> Install Visual C<font SIZE="-2">++</font> 2008-2019 Express/Community, then setup your environment using, e.g. </p>
<pre>
 C:\Program Files\Microsoft Visual Studio 12.0\Common7\Toolssvars32.bat
</pre>
<p> (assuming the default installation location was chosen). </p>
<p> Perl should now build using the win32/Makefile. You will need to edit that file to set <font SIZE="-1">CCTYPE</font> to one of <font SIZE="-1">MSVC90-MSVC142</font> first.</p>
<dt>Microsoft Visual C<font SIZE="-2">++</font> 2005 Express Edition</p>
<dd> This free version of Visual C<font SIZE="-2">++</font> 2005 Professional contains the same compiler and linker that ship with the full version, but doesn&#8217;t contain everything necessary to build Perl. </p>
<p> You will also need to download the &#8220;Windows <font SIZE="-1">SDK&#8221;</font> (the &#8220;Core <font SIZE="-1">SDK&#8221;</font> and &#8220;<font SIZE="-1">MDAC SDK&#8221;</font> components are required) for more header files and libraries. </p>
<p> These packages can both be downloaded by searching in the Download Center at &lt;<a rel="nofollow" href="http://www.microsoft.com/downloads/search.aspx?displaylang=en">http://www.microsoft.com/downloads/search.aspx?displaylang=en</a>&gt;. (Providing exact links to these packages has proven a pointless task because the links keep on changing so often.) </p>
<p> Try to obtain the latest version of the Windows <font SIZE="-1">SDK.</font> Sometimes these packages contain a particular Windows <font SIZE="-1">OS</font> version in their name, but actually work on other <font SIZE="-1">OS</font> versions too. For example, the &#8220;Windows Server 2003 R2 Platform <font SIZE="-1">SDK&#8221;</font> also runs on Windows <font SIZE="-1">XP SP2</font> and Windows 2000. </p>
<p> Install Visual C<font SIZE="-2">++</font> 2005 first, then the Platform <font SIZE="-1">SDK.</font> Setup your environment as follows (assuming default installation locations were chosen): </p>
<pre><code>
SET PlatformSDKDir = C :\Program Files\Microsoft Platform SDK
        SET PATH = % SystemRoot %\system32;
% SystemRoot % ;
C :\Program Files\Microsoft Visual Studio 8\Common7\IDE;
C :\Program Files\Microsoft Visual Studio 8\VC\BIN;
C :\Program Files\Microsoft Visual Studio 8\Common7\Tools;
C :\Program Files\Microsoft Visual Studio 8\SDK2 .0in;
C :\WINDOWS\Microsoft.NET\Framework2 .0.50727;
C :\Program Files\Microsoft Visual Studio 8\VC\VCPackages;
% PlatformSDKDir %\Bin
        SET INCLUDE = C :\Program Files\Microsoft Visual Studio 8\VC\INCLUDE;
% PlatformSDKDir %\include
        SET LIB = C :\Program Files\Microsoft Visual Studio 8\VC\LIB;
C :\Program Files\Microsoft Visual Studio 8\SDK2 .0\lib;
% PlatformSDKDir %\lib
        SET LIBPATH = C :\WINDOWS\Microsoft.NET\Framework2 .0.50727
</code></pre>
<p> (The PlatformSDKDir might need to be set differently depending on which version you are using. Earlier versions installed into &#8220;C:\Program Files\Microsoft <font SIZE="-1">SDK&#8221;,</font> while the latest versions install into version-specific locations such as &#8220;C:\Program Files\Microsoft Platform <font SIZE="-1">SDK</font> for Windows Server 2003 R2&#8221;.) </p>
<p> Perl should now build using the win32/Makefile. You will need to edit that file to set </p>
<pre>
 CCTYPE = MSVC80
</pre>
<p> and to set <font SIZE="-1">CCHOME, CCINCDIR</font> and <font SIZE="-1">CCLIBDIR</font> as per the environment setup above.</p>
<dt>Microsoft Visual C<font SIZE="-2">++</font> Toolkit 2003</p>
<dd> This free toolkit contains the same compiler and linker that ship with Visual C<font SIZE="-2">++</font> .NET 2003 Professional, but doesn&#8217;t contain everything necessary to build Perl. </p>
<p> You will also need to download the &#8220;Platform <font SIZE="-1">SDK&#8221;</font> (the &#8220;Core <font SIZE="-1">SDK&#8221;</font> and &#8220;<font SIZE="-1">MDAC SDK&#8221;</font> components are required) for header files, libraries and rc.exe, and &#8220;.NET Framework <font SIZE="-1">SDK&#8221;</font> for more libraries and nmake.exe. Note that the latter (which also includes the free compiler and linker) requires the &#8220;.NET Framework Redistributable&#8221; to be installed first. This can be downloaded and installed separately, but is included in the &#8220;Visual C<font SIZE="-2">++</font> Toolkit 2003&#8221; anyway. </p>
<p> These packages can all be downloaded by searching in the Download Center at &lt;<a rel="nofollow" href="http://www.microsoft.com/downloads/search.aspx?displaylang=en">http://www.microsoft.com/downloads/search.aspx?displaylang=en</a>&gt;. (Providing exact links to these packages has proven a pointless task because the links keep on changing so often.) </p>
<p> Try to obtain the latest version of the Windows <font SIZE="-1">SDK.</font> Sometimes these packages contain a particular Windows <font SIZE="-1">OS</font> version in their name, but actually work on other <font SIZE="-1">OS</font> versions too. For example, the &#8220;Windows Server 2003 R2 Platform <font SIZE="-1">SDK&#8221;</font> also runs on Windows <font SIZE="-1">XP SP2</font> and Windows 2000. </p>
<p> Install the Toolkit first, then the Platform <font SIZE="-1">SDK,</font> then the .NET Framework <font SIZE="-1">SDK.</font> Setup your environment as follows (assuming default installation locations were chosen): </p>
<p>SET PlatformSDKDir = C :\Program Files\Microsoft Platform SDK<br />
        SET PATH = % SystemRoot %\system32;<br />
% SystemRoot % ;<br />
C :\Program Files\Microsoft Visual C++ Toolkit 2003in;<br />
% PlatformSDKDir %\Bin;<br />
C :\Program Files\Microsoft.NET\SDK1 .1\Bin<br />
        SET INCLUDE = C :\Program Files\Microsoft Visual C++ Toolkit 2003\include;<br />
% PlatformSDKDir %\include;<br />
C :\Program Files\Microsoft Visual Studio.NET 2003\Vc7\include<br />
        SET LIB = C :\Program Files\Microsoft Visual C++ Toolkit 2003\lib;<br />
% PlatformSDKDir %\lib;<br />
C :\Program Files\Microsoft Visual Studio.NET 2003\Vc7\lib</p>
<p> (The PlatformSDKDir might need to be set differently depending on which version you are using. Earlier versions installed into &#8220;C:\Program Files\Microsoft <font SIZE="-1">SDK&#8221;,</font> while the latest versions install into version-specific locations such as &#8220;C:\Program Files\Microsoft Platform <font SIZE="-1">SDK</font> for Windows Server 2003 R2&#8221;.) </p>
<p> Several required files will still be missing:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> cvtres.exe is required by link.exe when using a .res file. It is actually installed by the .NET Framework <font SIZE="-1">SDK,</font> but into a location such as the following: </p>
<pre>
 C:\WINDOWS\Microsoft.NET\Framework1.1.4322
</pre>
<p> Copy it from there to <tt>%PlatformSDKDir</tt>%\Bin</p>
<dt>&bull;</p>
<dd> lib.exe is normally used to build libraries, but link.exe with the /lib option also works, so change win32/config.vc to use it instead: </p>
<p> Change the line reading: </p>
<pre>
        ar='lib'
</pre>
<p> to: </p>
<pre>
        ar='link /lib'
</pre>
<p> It may also be useful to create a batch file called lib.bat in C:\Program Files\Microsoft Visual C<font SIZE="-2">++</font> Toolkit 2003in containing: </p>
<pre>
        @echo off
        link /lib %*
</pre>
<p> for the benefit of any naughty C extension modules that you might want to build later which explicitly reference &#8220;lib&#8221; rather than taking their value from <tt>$Config</tt>{ar}.</p>
<dt>&bull;</p>
<dd> setargv.obj is required to build perlglob.exe (and perl.exe if the <font SIZE="-1">USE_SETARGV</font> option is enabled). The Platform <font SIZE="-1">SDK</font> supplies this object file in source form in <tt>%PlatformSDKDir</tt>%\src
