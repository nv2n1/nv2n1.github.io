---
title: "library-combo(7)"
name: "library-combo"
section: "7"
letter: "l"
url: "/docs/linux/man/7-library-combo/"
description: "library-combo – GNUstep Make support for cross-compilation."
---

<p>library-combo &#8211; GNUstep Make support for cross-compilation.</p>
<h2>Description</h2>
<p>This manual page is about cross-compilation and fat binaries. Fat binaries are packages that you can supply which contain more the one binary of your program (e.g. your application). So you can support multiple platforms with a single package. To support this your system has to be built in a non-flattened way. Meaning that during the installation of <i>gnustep-make</i> you should have selected <code>&#8211;disable-flattened</code> and the types of library combinations you want to support, through the <code>&#8211;with-library-combo</code> option. With library combinations we mean the Objective-C runtime, the Foundation library and the Application library. For more details about this see the LIBRARY-COMBO section. If you installed your <code>GNUstep</code> system in a non-flattened way all system dependend binaries are installed in subdirectories with <i>cpu/os/library-combo</i> information. That means for instance that the <i>gnustep-base</i> library will be installed in <i>Library/Libraries/ix86/linux/gnu-gnu-gnu/</i> when you are on an Intel x86 system, running linux with the <font SIZE="-1">GNU</font> runtime for Objective-C and you installed <code>GNUstep</code>. For each and every library-combo that you want to support you should create the environment through <i>gnustep-make</i>, because it installs a different <i>config.make</i> to support its own <code>CC</code>, <code>OPTFLAGS</code>, etc. flags.</p>
<h3>Library-Combo</h3>
<p>An important issue is to let to a package the ability to deal with various libraries and configurations available now:</p>
<dl>
<dt><code>Objective-C runtimes</code></p>
<dd>In the Objective-C world there are three major runtimes: the GNUstep runtime, the Apple runtime and the <font SIZE="-1">GNU</font> runtime. They are different in several respects and a program or library that works at the runtime level should be aware of them.</p>
<dt><code>Foundation libraries</code></p>
<dd>There are different Foundation libraries an application or tool can be written on top of: gnustep-base, libFoundation and Apple Cocoa system.</p>
<dt><code>Graphical interfaces</code></p>
<dd>Until now three libraries provide or try to provide OpenStep compliant systems: the AppKit from NeXT, gnustep-gui and Cocoa from Apple.</dl>
<p> If a program wants to work with all the possible combinations it will have to provide different binaries for each combination because it&#8217;s not possible to have a tool compiled for NeXT Foundation that runs with gnustep-base or vice-versa. To summarize, a program can be compiled for these combinations:</p>
<dl>
<dt><code>Objective-C runtime</code></p>
<dd>ng (for GNUstep Next Generation), gnu (for <font SIZE="-1">GNU</font> , or for GNUstep without latest language features), apple (for Apple), nx (for NeXT)</p>
<dt><code>Foundation library</code></p>
<dd>gnu (for gnustep-base), fd (for libFoundation), apple (for Apple Cocoa), nx (for NeXT Foundation)</p>
<dt><code>GUI library</code></p>
<dd>gnu (for gnustep-gui), apple (for Apple Cocoa), nx (for NeXT GUI)</dl>
<p> We&#8217;ll denote the fact that an application was compiled for a certain combination of the above values by using the abbreviations of the different subsystems and placing dashes between them. For example an application compiled for NeXT Foundation using NeXT AppKit will have the compile attribute nx-nx-nx. An application compiled for Apple Cocoa with the <font SIZE="-1">GNU</font> compiler for Objective-C gnu-apple-apple and another one compiled for <i>gnustep-base</i> using <i>gnustep-gui</i> under Unix will be denoted by gnu-gnu-gnu. Here is a list of some of the possible combinations:</p>
<dl>
<dd>Runtime<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Foundation<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>GUI</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>nx<tt>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>nx<tt>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>nx</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>nx<tt>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>fd<tt>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>gnu</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>gnu<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gnu<tt>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>gnu</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>ng<tt>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gnu<tt>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>gnu</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>gnu<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>fd<tt>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>gnu</p>
<dl>
<dd>&nbsp;<wbr>gnugc<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gnu<tt>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>gnu</p>
<dl>
<dd>&nbsp;<wbr>gnugc<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>fd<tt>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>gnu</p>
<dl>
<dd>&nbsp;<wbr>apple<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>apple<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>apple</p>
<dl>
<dd>&nbsp;<wbr>apple<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gnu<tt>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>gnu
</dl>
<p> Note that one can choose his/her own packages to build; it is not required to have all the packages installed on the system. Not having all of them installed limits only the ability to build and distribute binaries for those missing combinations.</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
<h3>Directory Structure</h3>
<p>For cross-compilation in a non-flattened directory structure is recommended, so that you can store on the same directory structure binaries for different machines. The standard <code>GNUstep</code> filesystem layout is normally used when a non-flattened directory structure is being used; this is obtained with the <code>&#8211;with-layout=</code><i>gnustep</i> option when configuring <i>gnustep-make</i>. The entire <code>GNUstep</code> installation is then created inside <i>/usr/GNUstep</i> (or another directory if you use the <code>&#8211;prefix=&#8230;</code> option when configuring <i>gnustep-make</i>). Directories that contain binaries (such as the <i>Libraries</i> directory) inside <i>/usr/GNUstep</i> are then set up to support fat binaries as follows:</p>
<dl>
<dd>Libraries/</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>ix86/</p>
<dl>
<dd>&nbsp;<wbr>linux-gnu/</p>
<dl>
<dd>gnu-gnu-gnu/</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>libgnustep-base.so</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>libgnustep-gui.so</p>
<dl>
<dd>gnu-fd-gnu/</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>libFoundation.so</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>libgnustep-gui.so<br />
 To allow the right libraries to be found, you need to source <i>GNUstep.sh</i> before using <code>GNUstep</code>, and you need to start up your application by using <code>openapp</code>, which will locate the right binary for your library combo.</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
<h3>Building For A Library-Combo</h3>
<p>The makefile package will allow the user to choose between different library combinations. To specify a combination you want to compile for just type:</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>make library_combo=library-combo For instance if you want to choose to compile using the GNUstep&#8217;s Foundation implementation and use the GNUstep GUI library on a GNU/Linux machine you can do like this:</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>make library_combo=gnu-gnu-gnu If your project requires running configure before compiling there are two issues you have to keep in mind. &#8216;configure&#8217; is used to determine the existence of particular header files and/or of some specific functionality in the system header files. This thing is usually done by creating a config.h file which contains a couple of defines like HAVE_&#8230; which say if the checked functionality is present or not. Another usage of configure is to determine some specific libraries to link against to and/or some specific tools. A typical <code>GNUstep</code> program is not required to check for additional libraries because this step is done by the time the makefile package is installed. If the project still needs to check for additional libraries and/or tools, the recommended way is to output a <i>config.mak</i> file which is included by the main <i>GNUmakefile</i>, instead of using <i>Makefile.in</i> files which are modified by <i>configure</i>. The reason for not doing this is to avoid having the makefiles contain target dependencies like above, this way keeping only one makefile instead of several for each target machine. The makefile package is written for <font SIZE="-1">GNU</font> make because it provides some very powerful features that save time both in writing the package but also at runtime, when you compile a project.</dl>
</dl>
<h3>Building For An Architecture</h3>
<p>In order to build a project for multiple architectures you&#8217;ll need the development environment for the target machine installed on your machine. This includes a cross-compiler together with all the additional tools like the assembler and linker, the target header files and all the libraries you need. The <code>GNUstep</code> makefile package should be able to compile and link an application for another machine just by typing</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>make target=target-triplet where target-triplet is the canonical system name as reported by <i>config.guess</i>.</dl>
<h3>Using A Library-Combo</h3>
<p>When you use library-combos, you must always source <i>GNUstep.sh</i>. That allows you to switch library paths on the fly. If you want to switch to a different library-combo in your shell, and if you are using <code>bash</code>, it&#8217;s common to first source <i>GNUstep-reset.sh</i> to reset all shell variables, then to source <code>GNUstep.sh</code> again. Let&#8217;s assume we use gnu-gnu-gnu as our current <code>LIBRARY_COMBO</code> and we want to switch to gnugc-gnu-gnu, then we would use:</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>.&nbsp;<wbr>/usr/GNUstep/System/Library/Makefiles/GNUstep-reset.sh</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>export LIBRARY_COMBO=gnugc-gnu-gnu</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>.&nbsp;<wbr>/usr/GNUstep/System/Library/Makefiles/GNUstep.sh </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-debugapp/">debugapp</a>(1), <a href="/docs/linux/man/7-gnustep/">GNUstep</a>(7), <a href="/docs/linux/man/1-gnustep-config/">gnustep-config</a>(1), <a href="/docs/linux/man/1-openapp/">openapp</a>(1) </p>
<h2>History</h2>
<p>Work on gnustep-make started in 1997 by Scott Christley &lt;scottc [at] net-community.com&gt;. </p>
<p> Version 2.0.0 of gnustep-make introduced many changes with previous releases, which was mainly the work of Nicola Pero &lt;nicola.pero [at] meta-innovation.com&gt;</p>
<h2>Authors</h2>
<p>This man-page was written by Dennis Leeuw &lt;dleeuw [at] made-it.com&gt; based on the DESIGN document from the gnustep-make source tree.</p>
<h2>Credits</h2>
<p>The DESIGN document was written by Ovidiu Predescu. </p>
<p> This work could only be as is due to the notes and corrects from Nicola Pero &lt;nicola.pero [at] meta-innovation.com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2007 Free Software Foundation, Inc. </p>
<p> Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
