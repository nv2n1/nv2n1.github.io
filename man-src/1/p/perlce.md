---
title: "perlce(1)"
name: "perlce"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlce/"
description: "perlce – Perl for WinCE"
---

<h2 class="name">NAME</h2>
<p> perlce &#8211; Perl for WinCE </p>
<h2>Building Perl for WinCE</h2>
<h3><font SIZE="-1">WARNING</font></h3>
<p> <code>Much of this document has become very out of date and needs updating, rewriting or deleting. The build process was overhauled during the 5.19 development track and the current instructions as of that time are given in &#8220;</code><font SIZE="-1"><code>CURRENT BUILD INSTRUCTIONS&#8221;</code></font><code>; the previous build instructions, which are largely superseded but may still contain some useful information, are left in &#8220;</code><font SIZE="-1"><code>OLD BUILD INSTRUCTIONS&#8221;</code></font><code> but really need removing after anything of use has been extracted from them.</code></p>
<h3><font SIZE="-1">DESCRIPTION</font></h3>
<p> This file gives the instructions for building Perl5.8 and above for WinCE. Please read and understand the terms under which this software is distributed.</p>
<h3>General explanations on cross-compiling WinCE</h3>
<dl>
<dt>&bull;</p>
<dd> <i>miniperl</i> is built. This is a single executable (without <font SIZE="-1">DLL</font>), intended to run on Win32, and it will facilitate remaining build process; all binaries built after it are foreign and should not run locally. </p>
<p> <i>miniperl</i> is built using <i>./win32/Makefile</i>; this is part of normal build process invoked as dependency from wince/Makefile.ce</p>
<dt>&bull;</p>
<dd> After <i>miniperl</i> is built, <i>configpm</i> is invoked to create right <i>Config.pm</i> in right place and its corresponding Cross.pm. </p>
<p> Unlike Win32 build, miniperl will not have <i>Config.pm</i> of host within reach; it rather will use <i>Config.pm</i> from within cross-compilation directories. </p>
<p> File <i>Cross.pm</i> is dead simple: for given cross-architecture places in <tt>@INC</tt> a path where perl modules are, and right <i>Config.pm</i> in that place. </p>
<p> That said, <tt>&quot;miniperl -Ilib -MConfig -we 1&quot;</tt> should report an error, because it can not find <i>Config.pm</i>. If it does not give an error &#8212; wrong <i>Config.pm</i> is substituted, and resulting binaries will be a mess. </p>
<p> <tt>&quot;miniperl -MCross -MConfig -we 1&quot;</tt> should run okay, and it will provide right <i>Config.pm</i> for further compilations.</p>
<dt>&bull;</p>
<dd> During extensions build phase, a script <i>./win32/buildext.pl</i> is invoked, which in turn steps in <i>./ext</i> subdirectories and performs a build of each extension in turn. </p>
<p> All invokes of <i>Makefile.PL</i> are provided with <tt>&quot;-MCross&quot;</tt> so to enable cross- compile.</dl>
<h3><font SIZE="-1">CURRENT BUILD INSTRUCTIONS</font></h3>
<p> (These instructions assume the host is 32-bit Windows. If you&#8217;re on 64-bit Windows then change &#8220;C:\Program Files&#8221; to &#8220;C:\Program Files (x86)&#8221; throughout.) </p>
<p> 1. Install <font SIZE="-1">EVC4</font> from </p>
<pre>
 <a rel="nofollow" href="http://download.microsoft.com/download/c/3/f/c3f8b58b-9753-4c2e-8b96-2dfe3476a2f7/eVC4.exe">http://download.microsoft.com/download/c/3/f/c3f8b58b-9753-4c2e-8b96-2dfe3476a2f7/eVC4.exe</a>
</pre>
<p> Use the key mentioned at </p>
<pre>
 <a rel="nofollow" href="http://download.cnet.com/Microsoft-eMbedded-Visual-C/3000-2212_4-10108490.html?tag=bc">http://download.cnet.com/Microsoft-eMbedded-Visual-C/3000-2212_4-10108490.html?tag=bc</a>
</pre>
<p> The installer is ancient and has a few bugs on the paths it uses. You will have to fix them later. Basically, some things go into &#8220;C:/Program Files/Windows <font SIZE="-1">CE</font> Tools&#8221;, others go into &#8220;C:/Windows <font SIZE="-1">CE</font> Tools&#8221; regardless of the path you gave to the installer (the default will be &#8220;C:/Windows <font SIZE="-1">CE</font> Tools&#8221;). Reboots will be required for the installer to proceed. Also .c and .h associations with Visual Studio might get overridden when installing <font SIZE="-1">EVC4.</font> You have been warned. </p>
<p> 2. Download celib from GitHub (using &#8220;Download <font SIZE="-1">ZIP&#8221;</font>) at </p>
<pre>
    <a rel="nofollow" href="https://github.com/bulk88/celib">https://github.com/bulk88/celib</a>
</pre>
<p> Extract it to a spaceless path but not into the perl build source. I call this directory &#8220;celib-palm-3.0&#8221; but in the GitHub snapshot it will be called &#8220;celib-master&#8221;. Make a copy of the &#8220;wince-arm-pocket-wce300-release&#8221; folder and rename the copy to &#8220;wince-arm-pocket-wce400&#8221;. This is a hack so we can build a <font SIZE="-1">CE 4.0</font> binary by linking in <font SIZE="-1">CE 3.0 ARM</font> asm; the linker doesn&#8217;t care. Windows Mobile/WinCE are backwards compatible with machine code like Desktop Windows. </p>
<p> 3. Download console-1.3-src.tar.gz from </p>
<pre>
 <a rel="nofollow" href="http://sourceforge.net/projects/perlce/files/PerlCE%20support%20files/console/">http://sourceforge.net/projects/perlce/files/PerlCE%20support%20files/console/</a>
</pre>
<p> Extract it to a spaceless path but not into the perl build source. Don&#8217;t extract it into the same directory as celib. Make a copy of the &#8220;wince-arm-pocket-wce300&#8221; folder and rename the copy to &#8220;wince-arm-pocket-wce400&#8221;. This is a hack so we can build a <font SIZE="-1">CE 4.0</font> binary by linking in <font SIZE="-1">CE 3.0 ARM</font> asm; the linker doesn&#8217;t care. Windows Mobile/WinCE are backwards compatible with machine code like Desktop Windows. </p>
<p> 4. Open a command prompt, run your regular batch file to set the environment for desktop Visual C building, goto the perl source directory, cd into win32/, fill out Makefile, and do a &#8220;nmake all&#8221; to build a Desktop Perl. </p>
<p> 5. Open win32/Makefile.ce in a text editor and do something similar to the following patch. </p>
<pre>
    -CELIBDLLDIR  = h:\src\wince
