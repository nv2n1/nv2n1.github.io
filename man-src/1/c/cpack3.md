---
title: "cpack3(1)"
name: "cpack3"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpack3/"
description: "cpack – CPack Command-Line Reference"
---

<h2>NAME</h2>
<p> cpack &#8211; CPack Command-Line Reference</p>
<h2>SYNOPSIS</h2>
<pre>
cpack3 -G &lt;generator&gt; [&lt;options&gt;]
</pre>
<h2>DESCRIPTION</h2>
<p> The &quot;cpack&quot; executable is the CMake packaging program. CMake-generated build trees created for projects that use the INSTALL_* commands have packaging support. This program will generate the package. </p>
<p> CMake is a cross-platform build system generator. Projects specify their build process with platform-independent CMake listfiles included in each directory of a source tree with the name CMakeLists.txt. Users build a project by using CMake to generate a build system for a native tool on their platform.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-G &lt;generator&gt;</code></p>
<dd> Use the specified generator to generate package. </p>
<p> CPack may support multiple native packaging systems on certain platforms. A generator is responsible for generating input files for particular system and invoking that systems. Possible generator names are specified in the Generators section.</p>
<dt><code>-C &lt;Configuration&gt;</code></p>
<dd> Specify the project configuration </p>
<p> This option specifies the configuration that the project was build with, for example &#8216;Debug&#8217;, &#8216;Release&#8217;.</p>
<dt><code>-D &lt;var&gt;=&lt;value&gt;</code></p>
<dd> Set a CPack variable. </p>
<p> Set a variable that can be used by the generator.</p>
<dt><code>&#8211;config &lt;config file&gt;</code></p>
<dd> Specify the config file. </p>
<p> Specify the config file to use to create the package. By default CPackConfig.cmake in the current directory will be used.</p>
<dt><code>&#8211;verbose,-V</code></p>
<dd> enable verbose output </p>
<p> Run cpack with verbose output.</p>
<dt><code>&#8211;debug</code></p>
<dd> enable debug output (for CPack developers) </p>
<p> Run cpack with debug output (for CPack developers).</p>
<dt><code>-P &lt;package name&gt;</code></p>
<dd> override/define CPACK_PACKAGE_NAME </p>
<p> If the package name is not specified on cpack command line thenCPack.cmake defines it as CMAKE_PROJECT_NAME</p>
<dt><code>-R &lt;package version&gt;</code></p>
<dd> override/define CPACK_PACKAGE_VERSION </p>
<p> If version is not specified on cpack command line thenCPack.cmake defines it from CPACK_PACKAGE_VERSION_[MAJOR|MINOR|PATCH]look into CPack.cmake for detail</p>
<dt><code>-B &lt;package directory&gt;</code></p>
<dd> override/define CPACK_PACKAGE_DIRECTORY </p>
<p> The directory where CPack will be doing its packaging work.The resulting package will be found there. Inside this directoryCPack creates &#8216;_CPack_Packages&#8217; sub-directory which is theCPack temporary directory.</p>
<dt><code>&#8211;vendor &lt;vendor name&gt;</code></p>
<dd> override/define CPACK_PACKAGE_VENDOR </p>
<p> If vendor is not specified on cpack command line (or inside CMakeLists.txt) thenCPack.cmake defines it with a default value</p>
<dt><code>&#8211;help,-help,-usage,-h,-H,/?</code></p>
<dd> Print usage information and exit. </p>
<p> Usage describes the basic command line interface and its options.</p>
<dt><code>&#8211;version,-version,/V [&lt;f&gt;]</code></p>
<dd> Show program name/version banner and exit. </p>
<p> If a file is specified, the version is written into it. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-full [&lt;f&gt;]</code></p>
<dd> Print all help manuals and exit. </p>
<p> All manuals are printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-manual &lt;man&gt; [&lt;f&gt;]</code></p>
<dd> Print one help manual and exit. </p>
<p> The specified manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-manual-list [&lt;f&gt;]</code></p>
<dd> List help manuals available and exit. </p>
<p> The list contains all manuals for which help may be obtained by using the <code>&#8211;help-manual</code> option followed by a manual name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-command &lt;cmd&gt; [&lt;f&gt;]</code></p>
<dd> Print help for one command and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-commands/">cmake-commands</a>(7)</code> manual entry for <code>&lt;cmd&gt;</code> is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-command-list [&lt;f&gt;]</code></p>
<dd> List commands with help available and exit. </p>
<p> The list contains all commands for which help may be obtained by using the <code>&#8211;help-command</code> option followed by a command name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-commands [&lt;f&gt;]</code></p>
<dd> Print cmake-commands manual and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-commands/">cmake-commands</a>(7)</code> manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-module &lt;mod&gt; [&lt;f&gt;]</code></p>
<dd> Print help for one module and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-modules/">cmake-modules</a>(7)</code> manual entry for <code>&lt;mod&gt;</code> is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-module-list [&lt;f&gt;]</code></p>
<dd> List modules with help available and exit. </p>
<p> The list contains all modules for which help may be obtained by using the <code>&#8211;help-module</code> option followed by a module name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-modules [&lt;f&gt;]</code></p>
<dd> Print cmake-modules manual and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-modules/">cmake-modules</a>(7)</code> manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-policy &lt;cmp&gt; [&lt;f&gt;]</code></p>
<dd> Print help for one policy and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-policies/">cmake-policies</a>(7)</code> manual entry for <code>&lt;cmp&gt;</code> is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-policy-list [&lt;f&gt;]</code></p>
<dd> List policies with help available and exit. </p>
<p> The list contains all policies for which help may be obtained by using the <code>&#8211;help-policy</code> option followed by a policy name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-policies [&lt;f&gt;]</code></p>
<dd> Print cmake-policies manual and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-policies/">cmake-policies</a>(7)</code> manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-property &lt;prop&gt; [&lt;f&gt;]</code></p>
<dd> Print help for one property and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-properties/">cmake-properties</a>(7)</code> manual entries for <code>&lt;prop&gt;</code> are printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-property-list [&lt;f&gt;]</code></p>
<dd> List properties with help available and exit. </p>
<p> The list contains all properties for which help may be obtained by using the <code>&#8211;help-property</code> option followed by a property name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-properties [&lt;f&gt;]</code></p>
<dd> Print cmake-properties manual and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-properties/">cmake-properties</a>(7)</code> manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-variable &lt;var&gt; [&lt;f&gt;]</code></p>
<dd> Print help for one variable and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-variables/">cmake-variables</a>(7)</code> manual entry for <code>&lt;var&gt;</code> is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-variable-list [&lt;f&gt;]</code></p>
<dd> List variables with help available and exit. </p>
<p> The list contains all variables for which help may be obtained by using the <code>&#8211;help-variable</code> option followed by a variable name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-variables [&lt;f&gt;]</code></p>
<dd> Print cmake-variables manual and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-variables/">cmake-variables</a>(7)</code> manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</dl>
<h2>SEE ALSO</h2>
<p> The following resources are available to get help using CMake:</p>
<dl>
<dt><code>Home Page</code></p>
<dd> <i><a rel="nofollow" href="https://cmake.org">https://cmake.org</a></i> </p>
<p> The primary starting point for learning about CMake.</p>
<dt><code>Frequently Asked Questions</code></p>
<dd> <i><a rel="nofollow" href="https://cmake.org/Wiki/CMake_FAQ">https://cmake.org/Wiki/CMake_FAQ</a></i> </p>
<p> A Wiki is provided containing answers to frequently asked questions.</p>
<dt><code>Online Documentation</code></p>
<dd> <i><a rel="nofollow" href="https://cmake.org/documentation">https://cmake.org/documentation</a></i> </p>
<p> Links to available documentation may be found on this web page.</p>
<dt><code>Mailing List</code></p>
<dd> <i><a rel="nofollow" href="https://cmake.org/mailing-lists">https://cmake.org/mailing-lists</a></i> </p>
<p> For help and discussion about using cmake, a mailing list is provided at <i>cmake [at] cmake.org</i>. The list is member-post-only but one may sign up on the CMake web page. Please first read the full documentation at <i><a rel="nofollow" href="https://cmake.org">https://cmake.org</a></i> before posting questions to the list.</dl>
<h2>COPYRIGHT</h2>
<p> 2000-2016 Kitware, Inc. </p>
<h2>Index</h2>
