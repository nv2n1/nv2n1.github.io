---
title: "cmake-compile-features(7)"
name: "cmake-compile-features"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake-compile-features/"
description: "cmake-compile-features – CMake Compile Features Reference"
---

<p>cmake-compile-features &#8211; CMake Compile Features Reference</p>
<h2>Introduction</h2>
<p>Project source code may depend on, or be conditional on, the availability of certain features of the compiler. There are three use-cases which arise: <i>Compile Feature Requirements</i>, <i>Optional Compile Features</i> and <i>Conditional Compilation Options</i>. </p>
<p> While features are typically specified in programming language standards, CMake provides a primary user interface based on granular handling of the features, not the language standard that introduced the feature. </p>
<p> The <code>CMAKE_C_KNOWN_FEATURES</code>, <code>CMAKE_CUDA_KNOWN_FEATURES</code>, and <code>CMAKE_CXX_KNOWN_FEATURES</code> global properties contain all the features known to CMake, regardless of compiler support for the feature. The <code>CMAKE_C_COMPILE_FEATURES</code>, <code>CMAKE_CUDA_COMPILE_FEATURES</code> , and <code>CMAKE_CXX_COMPILE_FEATURES</code> variables contain all features CMake knows are known to the compiler, regardless of language standard or compile flags needed to use them. </p>
<p> Features known to CMake are named mostly following the same convention as the Clang feature test macros. There are some exceptions, such as CMake using <code>cxx_final</code> and <code>cxx_override</code> instead of the single <code>cxx_override_control</code> used by Clang. </p>
<p> Note that there are no separate compile features properties or variables for the <code>OBJC</code> or <code>OBJCXX</code> languages. These are based off <code>C</code> or <code>C++</code> respectively, so the properties and variables for their corresponding base language should be used instead.</p>
<h2>Compile Feature Requirements</h2>
<p>Compile feature requirements may be specified with the <code>target_compile_features()</code> command. For example, if a target must be compiled with compiler support for the <code>cxx_constexpr</code> feature: </p>
<pre>add_library(mylib requires_constexpr.cpp)
target_compile_features(mylib PRIVATE cxx_constexpr)</pre>
<p>In processing the requirement for the <code>cxx_constexpr</code> feature, <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> will ensure that the in-use C++ compiler is capable of the feature, and will add any necessary flags such as <code>-std=gnu++11</code> to the compile lines of C++ files in the <code>mylib</code> target. A <code>FATAL_ERROR</code> is issued if the compiler is not capable of the feature. </p>
<p> The exact compile flags and language standard are deliberately not part of the user interface for this use-case. CMake will compute the appropriate compile flags to use by considering the features specified for each target. </p>
<p> Such compile flags are added even if the compiler supports the particular feature without the flag. For example, the GNU compiler supports variadic templates (with a warning) even if <code>-std=gnu++98</code> is used. CMake adds the <code>-std=gnu++11</code> flag if <code>cxx_variadic_templates</code> is specified as a requirement. </p>
<p> In the above example, <code>mylib</code> requires <code>cxx_constexpr</code> when it is built itself, but consumers of <code>mylib</code> are not required to use a compiler which supports <code>cxx_constexpr</code>. If the interface of <code>mylib</code> does require the <code>cxx_constexpr</code> feature (or any other known feature), that may be specified with the <code>PUBLIC</code> or <code>INTERFACE</code> signatures of <code>target_compile_features()</code>: </p>
<pre>add_library(mylib requires_constexpr.cpp)
# cxx_constexpr is a usage-requirement
target_compile_features(mylib PUBLIC cxx_constexpr)
# main.cpp will be compiled with -std=gnu++11 on GNU for cxx_constexpr.
add_executable(myexe main.cpp)
target_link_libraries(myexe mylib)</pre>
<p>Feature requirements are evaluated transitively by consuming the link implementation. See <code><a href="/docs/linux/man/7-cmake-buildsystem/">cmake-buildsystem</a>(7)</code> for more on transitive behavior of build properties and usage requirements.</p>
<h3>Requiring Language Standards</h3>
<p>In projects that use a large number of commonly available features from a particular language standard (e.g. C++ 11) one may specify a meta-feature (e.g. <code>cxx_std_11</code>) that requires use of a compiler mode that is at minimum aware of that standard, but could be greater. This is simpler than specifying all the features individually, but does not guarantee the existence of any particular feature. Diagnosis of use of unsupported features will be delayed until compile time. </p>
<p> For example, if C++ 11 features are used extensively in a project&#8217;s header files, then clients must use a compiler mode that is no less than C++ 11. This can be requested with the code: </p>
<pre>target_compile_features(mylib PUBLIC cxx_std_11)</pre>
<p>In this example, CMake will ensure the compiler is invoked in a mode of at-least C++ 11 (or C++ 14, C++ 17, &#8230;), adding flags such as <code>-std=gnu++11</code> if necessary. This applies to sources within <code>mylib</code> as well as any dependents (that may include headers from <code>mylib</code>).</p>
<h3>Availability of Compiler Extensions</h3>
<p>The <code>&lt;LANG&gt;_EXTENSIONS</code> target property defaults to the compiler&#8217;s default (see <code>CMAKE_&lt;LANG&gt;_EXTENSIONS_DEFAULT</code>). Note that because most compilers enable extensions by default, this may expose portability bugs in user code or in the headers of third-party dependencies. </p>
<p> <code>&lt;LANG&gt;_EXTENSIONS</code> used to default to <code>ON</code>. See <code>CMP0128</code>.</p>
<h2>Optional Compile Features</h2>
<p>Compile features may be preferred if available, without creating a hard requirement. This can be achieved by <i>not</i> specifying features with <code>target_compile_features()</code> and instead checking the compiler capabilities with preprocessor conditions in project code. </p>
<p> In this use-case, the project may wish to establish a particular language standard if available from the compiler, and use preprocessor conditions to detect the features actually available. A language standard may be established by <i>Requiring Language Standards</i> using <code>target_compile_features()</code> with meta-features like <code>cxx_std_11</code>, or by setting the <code>CXX_STANDARD</code> target property or <code>CMAKE_CXX_STANDARD</code> variable. </p>
<p> See also policy <code>CMP0120</code> and legacy documentation on Example Usage of the deprecated <code>WriteCompilerDetectionHeader</code> module.</p>
<h2>Conditional Compilation Options</h2>
<p>Libraries may provide entirely different header files depending on requested compiler features. </p>
<p> For example, a header at <code>with_variadics/interface.h</code> may contain: </p>
<pre>template&lt;int I, int... Is&gt;
struct Interface;
template&lt;int I&gt;
struct Interface&lt;I&gt;
{
 static int accumulate()
 {
 return I;
 }
};
template&lt;int I, int... Is&gt;
struct Interface
{
 static int accumulate()
 {
 return I + Interface&lt;Is...&gt;::accumulate();
 }
};</pre>
<p>while a header at <code>no_variadics/interface.h</code> may contain: </p>
<pre>template&lt;int I1, int I2 = 0, int I3 = 0, int I4 = 0&gt;
struct Interface
{
 static int accumulate() { return I1 + I2 + I3 + I4; }
};</pre>
<p>It may be possible to write an abstraction <code>interface.h</code> header containing something like: </p>
<pre>#ifdef HAVE_CXX_VARIADIC_TEMPLATES
#include &quot;with_variadics/interface.h&quot;
#else
#include &quot;no_variadics/interface.h&quot;
#endif</pre>
<p>However this could be unmaintainable if there are many files to abstract. What is needed is to use alternative include directories depending on the compiler capabilities. </p>
<p> CMake provides a <code>COMPILE_FEATURES</code> <code>generator expression</code> to implement such conditions. This may be used with the build-property commands such as <code>target_include_directories()</code> and <code>target_link_libraries()</code> to set the appropriate <code>buildsystem</code> properties: </p>
<pre>add_library(foo INTERFACE)
set(with_variadics ${CMAKE_CURRENT_SOURCE_DIR}/with_variadics)
set(no_variadics ${CMAKE_CURRENT_SOURCE_DIR}/no_variadics)
target_include_directories(foo
 INTERFACE
 &quot;$&lt;$&lt;COMPILE_FEATURES:cxx_variadic_templates&gt;:${with_variadics}&gt;&quot;
 &quot;$&lt;$&lt;NOT:$&lt;COMPILE_FEATURES:cxx_variadic_templates&gt;&gt;:${no_variadics}&gt;&quot;
 )</pre>
<p>Consuming code then simply links to the <code>foo</code> target as usual and uses the feature-appropriate include directory </p>
<pre>add_executable(consumer_with consumer_with.cpp)
target_link_libraries(consumer_with foo)
set_property(TARGET consumer_with CXX_STANDARD 11)
add_executable(consumer_no consumer_no.cpp)
target_link_libraries(consumer_no foo)</pre>
<h2>Supported Compilers</h2>
<p>CMake is currently aware of the <code>C++ standards</code> and <code>compile features</code> available from the following <code>compiler ids</code> as of the versions specified for each:</p>
<dl>
<dt>&bull;</p>
<dd><code>AppleClang</code>: Apple Clang for Xcode versions 4.4+.</p>
<dt>&bull;</p>
<dd><code>Clang</code>: Clang compiler versions 2.9+.</p>
<dt>&bull;</p>
<dd><code>GNU</code>: GNU compiler versions 4.4+.</p>
<dt>&bull;</p>
<dd><code>MSVC</code>: Microsoft Visual Studio versions 2010+.</p>
<dt>&bull;</p>
<dd><code>SunPro</code>: Oracle SolarisStudio versions 12.4+.</p>
<dt>&bull;</p>
<dd><code>Intel</code>: Intel compiler versions 12.1+. </p>
<p> CMake is currently aware of the <code>C standards</code> and <code>compile features</code> available from the following <code>compiler ids</code> as of the versions specified for each:</p>
<dt>&bull;</p>
<dd>all compilers and versions listed above for C++.</p>
<dt>&bull;</p>
<dd><code>GNU</code>: GNU compiler versions 3.4+ </p>
<p> CMake is currently aware of the <code>C++ standards</code> and their associated meta-features (e.g. <code>cxx_std_11</code>) available from the following <code>compiler ids</code> as of the versions specified for each:</p>
<dt>&bull;</p>
<dd><code>Cray</code>: Cray Compiler Environment version 8.1+.</p>
<dt>&bull;</p>
<dd><code>Fujitsu</code>: Fujitsu HPC compiler 4.0+.</p>
<dt>&bull;</p>
<dd><code>PGI</code>: PGI version 12.10+.</p>
<dt>&bull;</p>
<dd><code>NVHPC</code>: NVIDIA HPC compilers version 11.0+.</p>
<dt>&bull;</p>
<dd><code>TI</code>: Texas Instruments compiler.</p>
<dt>&bull;</p>
<dd><code>XL</code>: IBM XL version 10.1+. </p>
<p> CMake is currently aware of the <code>C standards</code> and their associated meta-features (e.g. <code>c_std_99</code>) available from the following <code>compiler ids</code> as of the versions specified for each:</p>
<dt>&bull;</p>
<dd>all compilers and versions listed above with only meta-features for C++. </p>
<p> CMake is currently aware of the <code>CUDA standards</code> and their associated meta-features (e.g. <code>cuda_std_11</code>) available from the following <code>compiler ids</code> as of the versions specified for each:</p>
<dt>&bull;</p>
<dd><code>Clang</code>: Clang compiler 5.0+.</p>
<dt>&bull;</p>
<dd><code>NVIDIA</code>: NVIDIA nvcc compiler 7.5+.</dl>
<h2>Copyright</h2>
<p>2000-2022 Kitware, Inc. and Contributors</p>
