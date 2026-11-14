---
title: "bjam148(1)"
name: "bjam148"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bjam148/"
description: "bjam – Command-line utility to build Boost-related C++ projects with Boost.Build"
---

<h2 class="name">NAME</h2>
<p> bjam &#8211; Command-line utility to build Boost-related C++ projects with Boost.Build </p>
<h2>SYNOPSIS</h2>
<p> <code>bjam</code> [-a] [-dx] [-fx] [-jx] [-lx] [-n] [-ox] [-px] [-q] [-sx=y] [-tx] [-v] [&#8211;x] </p>
<p> <i>bjam</i> accepts the following options: </p>
<p> <code>-a</code> </p>
<p>&nbsp;<wbr>Build all targets, even if they are current </p>
<p> <code>-dx</code> </p>
<p>&nbsp;<wbr>Set the debug level to x&nbsp;<wbr>(0-9) </p>
<p> <code>-fx</code> </p>
<p>&nbsp;<wbr>Read x instead of Jambase </p>
<p> <code>-jx</code> </p>
<p>&nbsp;<wbr>Run up to x shell commands concurrently </p>
<p> <code>-lx</code> </p>
<p>&nbsp;<wbr>Limit actions to x number of seconds after which they are stopped </p>
<p> <code>-n</code> </p>
<p>&nbsp;<wbr>Don&#8217;t actually execute the updating actions </p>
<p> <code>-ox</code> </p>
<p>&nbsp;<wbr>Write the updating actions to file x </p>
<p> <code>-px</code> </p>
<p>&nbsp;<wbr>x=0, pipes action stdout and stderr merged into action output </p>
<p> <code>-q</code> </p>
<p>&nbsp;<wbr>Quit quickly as soon as a target fails </p>
<p> <code>-sx=y</code> </p>
<p>&nbsp;<wbr>Set variable x=y, overriding environment </p>
<p> <code>-tx</code> </p>
<p>&nbsp;<wbr>Rebuild x, even if it is up-to-date </p>
<p> <code>-v</code> </p>
<p>&nbsp;<wbr>Print the version of jam and exit </p>
<p> <code>&#8211;x</code> </p>
<p>&nbsp;<wbr>Option is ignored</p>
<h2>DESCRIPTION</h2>
<p> This section provides the information necessary to create your own projects using <i>Boost.Build</i> The information provided here is relatively high-level, and Chapter 6, Reference as well as the on-line help system must be used to obtain low-level documentation (see &#8211;help) </p>
<p> <i>Boost.Build</i> actually consists of two parts &#8211; <i>Boost.Jam</i>, a build engine with its own interpreted language, and <i>Boost.Build</i> itself, implemented in <i>Boost.Jam&#8217;s</i> language. The chain of events when you type bjam on the command line is as follows:</p>
<dl>
<dt>&bull;</p>
<dd> <i>Boost.Jam</i> tries to find <i>Boost.Build</i> and loads the top-level module. The exact process is described in the section called “Initialization”</dl>
<dl>
<dt>&bull;</p>
<dd> The top-level module loads user-defined configuration files, <i>user-config.jam</i> and <i>site-config.jam</i>, which define available toolsets</dl>
<dl>
<dt>&bull;</p>
<dd> The <i>Jamfile</i> in the current directory is read That in turn might cause reading of further Jamfiles. As a result, a tree of projects is created, with targets inside projects</dl>
<dl>
<dt>&bull;</p>
<dd> Finally, using the build request specified on the command line, <i>Boost.Build</i> decides which targets should be built and how. That information is passed back to <i>Boost.Jam</i>, which takes care of actually running the scheduled build action commands</dl>
<p> So, to be able to successfully use <i>Boost.Build</i>, you need to know only four things:</p>
<dl>
<dt>&bull;</p>
<dd> How to configure <i>Boost.Build</i> (<a rel="nofollow" href="http://www.boost.org/boost-build2/doc/html/bbv2/overview/configuration.html)">http://www.boost.org/boost-build2/doc/html/bbv2/overview/configuration.html)</a></p>
<dt>&bull;</p>
<dd> How to declare targets in Jamfiles (<a rel="nofollow" href="http://www.boost.org/boost-build2/doc/html/bbv2/overview/targets.html)">http://www.boost.org/boost-build2/doc/html/bbv2/overview/targets.html)</a></p>
<dt>&bull;</p>
<dd> How the build process works (<a rel="nofollow" href="http://www.boost.org/boost-build2/doc/html/bbv2/overview/build_process.html)">http://www.boost.org/boost-build2/doc/html/bbv2/overview/build_process.html)</a></dl>
<p> Some Basics about the <i>Boost.Jam</i> language. See the section called “Boost.Jam Language” (<a rel="nofollow" href="http://www.boost.org/boost-build2/doc/html/bbv2/overview/jam_language.html)">http://www.boost.org/boost-build2/doc/html/bbv2/overview/jam_language.html)</a></p>
<h2>CONCEPTS</h2>
<p> <i>Boost.Build</i> has a few unique concepts that are introduced in this section. The best way to explain the concepts is by comparison with more classical build tools </p>
<p> When using any flavour of make, you directly specify targets and commands that are used to create them from other target. The below example creates a.o from a.c using a hardcoded compiler invocation command </p>
<p> a.o: a.c </p>
<p>&nbsp;<wbr>g++&nbsp;<wbr>-o a.o -g a.c </p>
<p> This is rather low-level description mechanism and it is hard to adjust commands, options, and sets of created targets depending on the used compiler and operating system. </p>
<p> To improve portability, most modern build system provide a set of higher-level functions that can be used in build description files. Consider this example: </p>
<p> add_program (&#8216;a&#8217;, &#8216;a.c&#8217;) </p>
<p> This is a function call that creates targets necessary to create executable file from source file a.c. Depending on configured properties, different commands line may be used. However, <i>add_program</i> is higher-level, but rather thin level All targets are created immediately when build description is parsed, which makes it impossible to perform multi-variant builds. Often, change in any build property requires complete reconfiguration of the build tree </p>
<p> In order to support true multivariant builds, Boost.Build introduces the concept of metatarget—object that is created when build description is parsed and can be later called with specific build properties to generate actual targets </p>
<p> Consider an example: </p>
<p> exe a : a.cpp ; </p>
<p> When this declaration is parsed, <i>Boost.Build</i> creates a metatarget, but does not yet decides what files must be created, or what commands must be used. After all build files are parsed, Boost.Build considers properties requested on the command line. Supposed you have invoked <i>Boost.Build</i> with: </p>
<p> <i>bjam</i> toolset=gcc toolset=msvc </p>
<p> In that case, the metatarget will be called twice, once with toolset=gcc and once with toolset=msvc. Both invocations will produce concrete targets, that will have different extensions and use different command lines. Another key concept is build property. Build property is a variable that affects the build process. It can be specified on the command line, and is passed when calling a metatarget </p>
<p> While all build tools have a similar mechanism, <i>Boost.Build</i> differs by requiring that all build properties are declared in advance, and providing a large set of properties with portable semantics </p>
<p> The final concept is property propagation. Boost.Build does not require that every metatarget is called with the same properties. Instead, the &#8216;top-level&#8217; metatargets are called with the properties specified on the command line Each metatarget can elect to augment or override some properties (in particular, using the requirements mechanism, see the section called “Requirements”: <a rel="nofollow" href="http://www.boost.org/boost-build2/doc/html/bbv2/overview/targets.html#bbv2.overview.targets.requirements)">http://www.boost.org/boost-build2/doc/html/bbv2/overview/targets.html#bbv2.overview.targets.requirements)</a> Then, the dependency metatargets are called with modified properties and produce concrete targets that are then used in build process Of course, dependency metatargets maybe in turn modify build properties and have dependencies of their own. </p>
<p> For more in-depth treatment of the requirements and concepts, you may refer to SYRCoSE 2009 Boost.Build article (<a rel="nofollow" href="http://syrcose.ispras.ru/2009/files/04_paper.pdf">http://syrcose.ispras.ru/2009/files/04_paper.pdf</a>).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-boost-libraries/">boost-libraries</a></code>(3)</p>
<h2>SUPPORT</h2>
<p> Please report any bugs to <a rel="nofollow" href="https://svn.boost.org/trac/boost/">https://svn.boost.org/trac/boost/</a></p>
<h2>COPYRIGHT</h2>
<p> Boost Software License &#8211; Version 1.0 &#8211; August 17th, 2003 </p>
<p> See the LICENSE_1_0.txt file for more information on that license, or directly on Internet: </p>
<p>&nbsp;<wbr><a rel="nofollow" href="http://www.boost.org/LICENSE_1_0.txt">http://www.boost.org/LICENSE_1_0.txt</a>&nbsp;<wbr> </p>
<h2>Index</h2>
