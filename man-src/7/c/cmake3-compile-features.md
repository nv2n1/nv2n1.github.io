---
title: "cmake3-compile-features(7)"
name: "cmake3-compile-features"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake3-compile-features/"
description: "cmake-compile-features – CMake Compile Features Reference"
---

<p>cmake-compile-features &#8211; CMake Compile Features Reference</p>
<h2>Introduction</h2>
<p>Project source code may depend on, or be conditional on, the availability of certain features of the compiler. There are three use-cases which arise: <i>Compile Feature Requirements</i>, <i>Optional Compile Features</i> and <i>Conditional Compilation Options</i>. </p>
<p> While features are typically specified in programming language standards, CMake provides a primary user interface based on granular handling of the features, not the language standard that introduced the feature. </p>
<p> The <code>CMAKE_C_KNOWN_FEATURES</code> and <code>CMAKE_CXX_KNOWN_FEATURES</code> global properties contain all the features known to CMake, regardless of compiler support for the feature. The <code>CMAKE_C_COMPILE_FEATURES</code> and <code>CMAKE_CXX_COMPILE_FEATURES</code> variables contain all features CMake knows are known to the compiler, regardless of language standard or compile flags needed to use them. </p>
<p> Features known to CMake are named mostly following the same convention as the Clang feature test macros. The are some exceptions, such as CMake using <code>cxx_final</code> and <code>cxx_override</code> instead of the single <code>cxx_override_control</code> used by Clang.</p>
<h2>Compile Feature Requirements</h2>
<p>Compile feature requirements may be specified with the <code>target_compile_features()</code> command. For example, if a target must be compiled with compiler support for the <code>cxx_constexpr</code> feature: </p>
<pre>add_library(mylib requires_constexpr.cpp)
target_compile_features(mylib PRIVATE cxx_constexpr)</pre>
<p>In processing the requirement for the <code>cxx_constexpr</code> feature, <code><a href="/docs/linux/man/1-cmake3/">cmake3</a>(1)</code> will ensure that the in-use C++ compiler is capable of the feature, and will add any necessary flags such as <code>-std=gnu++11</code> to the compile lines of C++ files in the <code>mylib</code> target. A <code>FATAL_ERROR</code> is issued if the compiler is not capable of the feature. </p>
<p> The exact compile flags and language standard are deliberately not part of the user interface for this use-case. CMake will compute the appropriate compile flags to use by considering the features specified for each target. </p>
<p> Such compile flags are added even if the compiler supports the particular feature without the flag. For example, the GNU compiler supports variadic templates (with a warning) even if <code>-std=gnu++98</code> is used. CMake adds the <code>-std=gnu++11</code> flag if <code>cxx_variadic_templates</code> is specified as a requirement. </p>
<p> In the above example, <code>mylib</code> requires <code>cxx_constexpr</code> when it is built itself, but consumers of <code>mylib</code> are not required to use a compiler which supports <code>cxx_constexpr</code>. If the interface of <code>mylib</code> does require the <code>cxx_constexpr</code> feature (or any other known feature), that may be specified with the <code>PUBLIC</code> or <code>INTERFACE</code> signatures of <code>target_compile_features()</code>: </p>
<pre>add_library(mylib requires_constexpr.cpp)
# cxx_constexpr is a usage-requirement
target_compile_features(mylib PUBLIC cxx_constexpr)
# main.cpp will be compiled with -std=gnu++11 on GNU for cxx_constexpr.
add_executable(myexe main.cpp)
target_link_libraries(myexe mylib)</pre>
<p>Feature requirements are evaluated transitively by consuming the link implementation. See <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> for more on transitive behavior of build properties and usage requirements. </p>
<p> Because the <code>CXX_EXTENSIONS</code> target property is <code>ON</code> by default, CMake uses extended variants of language dialects by default, such as <code>-std=gnu++11</code> instead of <code>-std=c++11</code>. That target property may be set to <code>OFF</code> to use the non-extended variant of the dialect flag. Note that because most compilers enable extensions by default, this could expose cross-platform bugs in user code or in the headers of third-party dependencies.</p>
<h2>Optional Compile Features</h2>
<p>Compile features may be preferred if available, without creating a hard requirement. For example, a library may provides alternative implementations depending on whether the <code>cxx_variadic_templates</code> feature is available: </p>
<pre>#if Foo_COMPILER_CXX_VARIADIC_TEMPLATES
template&lt;int I, int... Is&gt;
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
};
#else
template&lt;int I1, int I2 = 0, int I3 = 0, int I4 = 0&gt;
struct Interface
{
 static int accumulate() { return I1 + I2 + I3 + I4; }
};
#endif</pre>
<p>Such an interface depends on using the correct preprocessor defines for the compiler features. CMake can generate a header file containing such defines using the <code>WriteCompilerDetectionHeader</code> module. The module contains the <code>write_compiler_detection_header</code> function which accepts parameters to control the content of the generated header file: </p>
<pre>write_compiler_detection_header(
 FILE &quot;${CMAKE_CURRENT_BINARY_DIR}/foo_compiler_detection.h&quot;
 PREFIX Foo
 COMPILERS GNU
 FEATURES
 cxx_variadic_templates
)</pre>
<p>Such a header file may be used internally in the source code of a project, and it may be installed and used in the interface of library code. </p>
<p> For each feature listed in <code>FEATURES</code>, a preprocessor definition is created in the header file, and defined to either <code>1</code> or <code>0</code>. </p>
<p> Additionally, some features call for additional defines, such as the <code>cxx_final</code> and <code>cxx_override</code> features. Rather than being used in <code>#ifdef</code> code, the <code>final</code> keyword is abstracted by a symbol which is defined to either <code>final</code>, a compiler-specific equivalent, or to empty. That way, C++ code can be written to unconditionally use the symbol, and compiler support determines what it is expanded to: </p>
<pre>struct Interface {
 virtual void Execute() = 0;
};
struct Concrete Foo_FINAL {
 void Execute() Foo_OVERRIDE;
};</pre>
<p>In this case, <code>Foo_FINAL</code> will expand to <code>final</code> if the compiler supports the keyword, or to empty otherwise. </p>
<p> In this use-case, the CMake code will wish to enable a particular language standard if available from the compiler. The <code>CXX_STANDARD</code> target property variable may be set to the desired language standard for a particular target, and the <code>CMAKE_CXX_STANDARD</code> may be set to influence all following targets: </p>
<pre>write_compiler_detection_header(
 FILE &quot;${CMAKE_CURRENT_BINARY_DIR}/foo_compiler_detection.h&quot;
 PREFIX Foo
 COMPILERS GNU
 FEATURES
 cxx_final cxx_override
)
# Includes foo_compiler_detection.h and uses the Foo_FINAL symbol
# which will expand to 'final' if the compiler supports the requested
# CXX_STANDARD.
add_library(foo foo.cpp)
set_property(TARGET foo PROPERTY CXX_STANDARD 11)
# Includes foo_compiler_detection.h and uses the Foo_FINAL symbol
# which will expand to 'final' if the compiler supports the feature,
# even though CXX_STANDARD is not set explicitly. The requirement of
# cxx_constexpr causes CMake to set CXX_STANDARD internally, which
# affects the compile flags.
add_library(foo_impl foo_impl.cpp)
target_compile_features(foo_impl PRIVATE cxx_constexpr)</pre>
<p>The <code>write_compiler_detection_header</code> function also creates compatibility code for other features which have standard equivalents. For example, the <code>cxx_static_assert</code> feature is emulated with a template and abstracted via the <code>&lt;PREFIX&gt;_STATIC_ASSERT</code> and <code>&lt;PREFIX&gt;_STATIC_ASSERT_MSG</code> function-macros.</p>
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
<p>It would be possible to write a abstraction <code>interface.h</code> header containing something like: </p>
<pre>#include &quot;foo_compiler_detection.h&quot;
#if Foo_COMPILER_CXX_VARIADIC_TEMPLATES
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
<p>CMake is currently aware of the <code>language standards</code> and <code>compile features</code> available from the following <code>compiler ids</code> as of the versions specified for each:</p>
<dl>
<dt>&bull;</p>
<dd><code>AppleClang</code>: Apple Clang for Xcode versions 4.4 though 6.2.</p>
<dt>&bull;</p>
<dd><code>Clang</code>: Clang compiler versions 2.9 through 3.4.</p>
<dt>&bull;</p>
<dd><code>GNU</code>: GNU compiler versions 4.4 through 5.0.</p>
<dt>&bull;</p>
<dd><code>MSVC</code>: Microsoft Visual Studio versions 2010 through 2015.</p>
<dt>&bull;</p>
<dd><code>SunPro</code>: Oracle SolarisStudio version 12.4.</p>
<dt>&bull;</p>
<dd><code>Intel</code>: Intel compiler versions 12.1 through 16.0 on UNIX platforms.</dl>
<h2>Copyright</h2>
<p>2000-2016 Kitware, Inc.</p>
