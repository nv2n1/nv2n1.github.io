---
title: "perlnetware(1)"
name: "perlnetware"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlnetware/"
---

<h2 class="name">NAME</h2>
 

 perlnetware - Perl for NetWare 

<h2>DESCRIPTION</h2>

 This file gives instructions for building Perl 5.7 and above, and also Perl modules for NetWare. Before you start, you may want to read the <font SIZE="-1">README</font> file found in the top level directory into which the Perl source code distribution was extracted. Make sure you read and understand the terms under which the software is being distributed.

<h2>BUILD</h2>

 This section describes the steps to be performed to build a Perl <font SIZE="-1">NLM</font> and other associated NLMs.

<h3>Tools &amp; <font SIZE="-1">SDK</font></h3>

 The build requires CodeWarrior compiler and linker. In addition, the ``NetWare <font SIZE="-1">SDK'', ``NLM &amp;</font> NetWare Libraries for C'' and ``NetWare Server Protocol Libraries for C'', all available at &lt;<a rel="nofollow" HREF="http://developer.novell.com/wiki/index.php/Category:Novell_Developer_Kit">http://developer.novell.com/wiki/index.php/Category:Novell_Developer_Kit</a>&gt;, are required. Microsoft Visual C<font SIZE="-2">++</font> version 4.2 or later is also required.

<h3>Setup</h3>

 The build process is dependent on the location of the NetWare <font SIZE="-1">SDK.</font> Once the Tools &amp; <font SIZE="-1">SDK</font> are installed, the build environment has to be setup. The following batch files setup the environment.
<dl>
<dt>SetNWBld.bat
<dd> The Execution of this file takes 2 parameters as input. The first being the NetWare <font SIZE="-1">SDK</font> path, second being the path for CodeWarrior Compiler &amp; tools. Execution of this file sets these paths and also sets the build type to Release by default.
<dt>Buildtype.bat
<dd> This is used to set the build type to debug or release. Change the build type only after executing SetNWBld.bat 

 Example:
<dl>
<dt>
<dd>
<dl>
<dt>1.
<dd> Typing ``buildtype d on'' at the command prompt causes the buildtype to be set to Debug type with D2 flag set.
<dt>2.
<dd> Typing ``buildtype d off'' or ``buildtype d'' at the command prompt causes the buildtype to be set to Debug type with D1 flag set.
<dt>3.
<dd> Typing ``buildtype r'' at the command prompt sets it to Release Build type.</dl>
</dl>

<dl>
<dt>
<dd></dl>
</dl>

<h3>Make</h3>

 The make process runs only under WinNT shell. The NetWare makefile is located under the NetWare folder. This makes use of miniperl.exe to run some of the Perl scripts. To create miniperl.exe, first set the required paths for Visual c++ compiler (specify vcvars32 location) at the command prompt. Then run nmake from win32 folder through WinNT command prompt. The build process can be stopped after miniperl.exe is created. Then run nmake from NetWare folder through WinNT command prompt. 

 Currently the following two build types are tested on NetWare:
<dl>
<dt>&bull;
<dd> <font SIZE="-1">USE_MULTI, USE_ITHREADS &amp; USE_IMP_SYS</font> defined
<dt>&bull;
<dd> <font SIZE="-1">USE_MULTI &amp; USE_IMP_SYS</font> defined and <font SIZE="-1">USE_ITHREADS</font> not defined</dl>

<h3>Interpreter</h3>

 Once miniperl.exe creation is over, run nmake from the NetWare folder. This will build the Perl interpreter for NetWare as <i>perl.nlm</i>. This is copied under the <i>Release</i> folder if you are doing a release build, else will be copied under <i>Debug</i> folder for debug builds.

<h3>Extensions</h3>

 The make process also creates the Perl extensions as <i>&lt;Extension</i>.nlm&gt;

<h2>INSTALL</h2>

 To install NetWare Perl onto a NetWare server, first map the Sys volume of a NetWare server to <i>i:</i>. This is because the makefile by default sets the drive letter to <i>i:</i>. Type <i>nmake nwinstall</i> from NetWare folder on a WinNT command prompt. This will copy the binaries and module files onto the NetWare server under <i>sys:\Perl</i> folder. The Perl interpreter, <i>perl.nlm</i>, is copied under <i>sys:\perl\system</i> folder. Copy this to <i>sys:\system</i> folder. 

 Example: At the command prompt Type ``nmake nwinstall''. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;This will install NetWare Perl on the NetWare Server. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Similarly, if you type&nbsp;``nmake install'', 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;this will cause the binaries to be installed on the local machine. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(Typically under the c:\perl folder)

<h2>BUILD NEW EXTENSIONS</h2>

 To build extensions other than standard extensions, NetWare Perl has to be installed on Windows along with Windows Perl. The Perl for Windows can be either downloaded from the <font SIZE="-1">CPAN</font> site and built using the sources, or the binaries can be directly downloaded from the ActiveState site. Installation can be done by invoking <i>nmake install</i> from the NetWare folder on a WinNT command prompt after building NetWare Perl by following steps given above. This will copy all the *.pm files and other required files. Documentation files are not copied. Thus one must first install Windows Perl, Then install NetWare Perl. 

 Once this is done, do the following to build any extension:
<dl>
<dt>&bull;
<dd> Change to the extension directory where its source files are present.
<dt>&bull;
<dd> Run the following command at the command prompt: 

 <pre>
    perl -II&lt;path to NetWare lib dir&gt; -II&lt;path to lib&gt; Makefile.pl
</pre> 

 Example: 

 <pre>
    perl -Ic:/perl/5.6.1/lib/NetWare-x86-multi-thread           \
                                -Ic:\perl\5.6.1\lib MakeFile.pl
</pre> 

 or 

 <pre>
    perl -Ic:/perl/5.8.0/lib/NetWare-x86-multi-thread           \
                                -Ic:\perl\5.8.0\lib MakeFile.pl
</pre>
<dt>&bull;
<dd> nmake
<dt>&bull;
<dd> nmake install 

 Install will copy the files into the Windows machine where NetWare Perl is installed and these files may have to be copied to the NetWare server manually. Alternatively, pass <i>INSTALLSITELIB=i:\perl\lib</i> as an input to makefile.pl above. Here <i>i:</i> is the mapped drive to the sys: volume of the server where Perl on NetWare is installed. Now typing <i>nmake install</i>, will copy the files onto the NetWare server. 

 Example: You can execute the following on the command prompt. 

 <pre>
  perl -Ic:/perl/5.6.1/lib/NetWare-x86-multi-thread             \
                                -Ic:\perl\5.6.1\lib MakeFile.pl
  INSTALLSITELIB=i:\perl\lib
</pre> 

 or 

 <pre>
  perl -Ic:/perl/5.8.0/lib/NetWare-x86-multi-thread             \
                                -Ic:\perl\5.8.0\lib MakeFile.pl
  INSTALLSITELIB=i:\perl\lib
</pre>
<dt>&bull;
<dd> Note: Some modules downloaded from <font SIZE="-1">CPAN</font> may require NetWare related <font SIZE="-1">API</font> in order to build on NetWare. Other modules may however build smoothly with or without minor changes depending on the type of module.</dl>

<h2>ACKNOWLEDGEMENTS</h2>

 The makefile for Win32 is used as a reference to create the makefile for NetWare. Also, the make process for NetWare port uses miniperl.exe to run scripts during the make and installation process.

<h2>AUTHORS</h2>

 Anantha Kesari H Y (hyanantha [at] novell.com) Aditya C (caditya [at] novell.com)

<h2>DATE</h2>

<dl>
<dt>&bull;
<dd> Created - 18 Jan 2001
<dt>&bull;
<dd> Modified - 25 June 2001
<dt>&bull;
<dd> Modified - 13 July 2001
<dt>&bull;
<dd> Modified - 28 May 2002 

</dl>

<h2>Index</h2>



<dt><a HREF="#lbAJ">INSTALL</a>
<dd>
<dt><a HREF="#lbAK">BUILD NEW EXTENSIONS</a>
<dd>
<dt><a HREF="#lbAL">ACKNOWLEDGEMENTS</a>
<dd>
<dt><a HREF="#lbAM">AUTHORS</a>
<dd>
<dt><a HREF="#lbAN">DATE</a>
<dd></dl>
