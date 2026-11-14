---
title: "cmake-generator-expressions(7)"
name: "cmake-generator-expressions"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake-generator-expressions/"
description: "cmake-generator-expressions – CMake Generator Expressions"
---

<p>cmake-generator-expressions &#8211; CMake Generator Expressions</p>
<h2>Introduction</h2>
<p>Generator expressions are evaluated during build system generation to produce information specific to each build configuration. </p>
<p> Generator expressions are allowed in the context of many target properties, such as <code>LINK_LIBRARIES</code>, <code>INCLUDE_DIRECTORIES</code>, <code>COMPILE_DEFINITIONS</code> and others. They may also be used when using commands to populate those properties, such as <code>target_link_libraries()</code>, <code>target_include_directories()</code>, <code>target_compile_definitions()</code> and others. </p>
<p> They enable conditional linking, conditional definitions used when compiling, conditional include directories, and more. The conditions may be based on the build configuration, target properties, platform information or any other queryable information. </p>
<p> Generator expressions have the form <code>$&lt;&#8230;&gt;</code>. To avoid confusion, this page deviates from most of the CMake documentation in that it omits angular brackets <code>&lt;&#8230;&gt;</code> around placeholders like <code>condition</code>, <code>string</code>, <code>target</code>, among others. </p>
<p> Generator expressions can be nested, as shown in most of the examples below.</p>
<h2>Boolean Generator Expressions</h2>
<p>Boolean expressions evaluate to either <code>0</code> or <code>1</code>. They are typically used to construct the condition in a <i>conditional generator expression</i>. </p>
<p> Available boolean expressions are:</p>
<h3>Logical Operators</h3>
<dl>
<dt><code>$&lt;BOOL:string&gt;</code></p>
<dd>Converts <code>string</code> to <code>0</code> or <code>1</code>. Evaluates to <code>0</code> if any of the following is true:</p>
<dt>&bull;</p>
<dd><code>string</code> is empty,</p>
<dt>&bull;</p>
<dd><code>string</code> is a case-insensitive equal of <code>0</code>, <code>FALSE</code>, <code>OFF</code>, <code>N</code>, <code>NO</code>, <code>IGNORE</code>, or <code>NOTFOUND</code>, or</p>
<dt>&bull;</p>
<dd><code>string</code> ends in the suffix <code>-NOTFOUND</code> (case-sensitive). </p>
<p> Otherwise evaluates to <code>1</code>.</p>
<dt><code>$&lt;AND:conditions&gt;</code></p>
<dd>where <code>conditions</code> is a comma-separated list of boolean expressions. Evaluates to <code>1</code> if all conditions are <code>1</code>. Otherwise evaluates to <code>0</code>.</p>
<dt><code>$&lt;OR:conditions&gt;</code></p>
<dd>where <code>conditions</code> is a comma-separated list of boolean expressions. Evaluates to <code>1</code> if at least one of the conditions is <code>1</code>. Otherwise evaluates to <code>0</code>.</p>
<dt><code>$&lt;NOT:condition&gt;</code></p>
<dd><code>0</code> if <code>condition</code> is <code>1</code>, else <code>1</code>.</dl>
<h3>String Comparisons</h3>
<dl>
<dt><code>$&lt;STREQUAL:string1,string2&gt;</code></p>
<dd><code>1</code> if <code>string1</code> and <code>string2</code> are equal, else <code>0</code>. The comparison is case-sensitive. For a case-insensitive comparison, combine with a <i>string transforming generator expression</i>, </p>
<pre>$&lt;STREQUAL:$&lt;UPPER_CASE:${foo}&gt;,&quot;BAR&quot;&gt; # &quot;1&quot; if ${foo} is any of &quot;BAR&quot;, &quot;Bar&quot;, &quot;bar&quot;, ...</pre>
<dt><code>$&lt;EQUAL:value1,value2&gt;</code></p>
<dd><code>1</code> if <code>value1</code> and <code>value2</code> are numerically equal, else <code>0</code>.</p>
<dt><code>$&lt;IN_LIST:string,list&gt;</code></p>
<dd>New in version 3.12. </p>
<p> <code>1</code> if <code>string</code> is member of the semicolon-separated <code>list</code>, else <code>0</code>. Uses case-sensitive comparisons.</p>
<dt><code>$&lt;VERSION_LESS:v1,v2&gt;</code></p>
<dd><code>1</code> if <code>v1</code> is a version less than <code>v2</code>, else <code>0</code>.</p>
<dt><code>$&lt;VERSION_GREATER:v1,v2&gt;</code></p>
<dd><code>1</code> if <code>v1</code> is a version greater than <code>v2</code>, else <code>0</code>.</p>
<dt><code>$&lt;VERSION_EQUAL:v1,v2&gt;</code></p>
<dd><code>1</code> if <code>v1</code> is the same version as <code>v2</code>, else <code>0</code>.</p>
<dt><code>$&lt;VERSION_LESS_EQUAL:v1,v2&gt;</code></p>
<dd>New in version 3.7. </p>
<p> <code>1</code> if <code>v1</code> is a version less than or equal to <code>v2</code>, else <code>0</code>.</p>
<dt><code>$&lt;VERSION_GREATER_EQUAL:v1,v2&gt;</code></p>
<dd>New in version 3.7. </p>
<p> <code>1</code> if <code>v1</code> is a version greater than or equal to <code>v2</code>, else <code>0</code>.</dl>
<h3>Variable Queries</h3>
<dl>
<dt><code>$&lt;TARGET_EXISTS:target&gt;</code></p>
<dd>New in version 3.12. </p>
<p> <code>1</code> if <code>target</code> exists, else <code>0</code>.</p>
<dt><code>$&lt;CONFIG:cfgs&gt;</code></p>
<dd><code>1</code> if config is any one of the entries in comma-separated list <code>cfgs</code>, else <code>0</code>. This is a case-insensitive comparison. The mapping in <code>MAP_IMPORTED_CONFIG_&lt;CONFIG&gt;</code> is also considered by this expression when it is evaluated on a property on an <code>IMPORTED</code> target.</p>
<dt><code>$&lt;PLATFORM_ID:platform_ids&gt;</code></p>
<dd>where <code>platform_ids</code> is a comma-separated list. <code>1</code> if the CMake&#8217;s platform id matches any one of the entries in <code>platform_ids</code>, otherwise <code>0</code>. See also the <code>CMAKE_SYSTEM_NAME</code> variable.</p>
<dt><code>$&lt;C_COMPILER_ID:compiler_ids&gt;</code></p>
<dd>where <code>compiler_ids</code> is a comma-separated list. <code>1</code> if the CMake&#8217;s compiler id of the C compiler matches any one of the entries in <code>compiler_ids</code>, otherwise <code>0</code>. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable.</p>
<dt><code>$&lt;CXX_COMPILER_ID:compiler_ids&gt;</code></p>
<dd>where <code>compiler_ids</code> is a comma-separated list. <code>1</code> if the CMake&#8217;s compiler id of the CXX compiler matches any one of the entries in <code>compiler_ids</code>, otherwise <code>0</code>. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable.</p>
<dt><code>$&lt;CUDA_COMPILER_ID:compiler_ids&gt;</code></p>
<dd>New in version 3.15. </p>
<p> where <code>compiler_ids</code> is a comma-separated list. <code>1</code> if the CMake&#8217;s compiler id of the CUDA compiler matches any one of the entries in <code>compiler_ids</code>, otherwise <code>0</code>. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable.</p>
<dt><code>$&lt;OBJC_COMPILER_ID:compiler_ids&gt;</code></p>
<dd>New in version 3.16. </p>
<p> where <code>compiler_ids</code> is a comma-separated list. <code>1</code> if the CMake&#8217;s compiler id of the Objective-C compiler matches any one of the entries in <code>compiler_ids</code>, otherwise <code>0</code>. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable.</p>
<dt><code>$&lt;OBJCXX_COMPILER_ID:compiler_ids&gt;</code></p>
<dd>New in version 3.16. </p>
<p> where <code>compiler_ids</code> is a comma-separated list. <code>1</code> if the CMake&#8217;s compiler id of the Objective-C++ compiler matches any one of the entries in <code>compiler_ids</code>, otherwise <code>0</code>. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable.</p>
<dt><code>$&lt;Fortran_COMPILER_ID:compiler_ids&gt;</code></p>
<dd>where <code>compiler_ids</code> is a comma-separated list. <code>1</code> if the CMake&#8217;s compiler id of the Fortran compiler matches any one of the entries in <code>compiler_ids</code>, otherwise <code>0</code>. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable.</p>
<dt><code>$&lt;HIP_COMPILER_ID:compiler_ids&gt;</code></p>
<dd>where <code>compiler_ids</code> is a comma-separated list. <code>1</code> if the CMake&#8217;s compiler id of the HIP compiler matches any one of the entries in <code>compiler_ids</code>, otherwise <code>0</code>. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable.</p>
<dt><code>$&lt;ISPC_COMPILER_ID:compiler_ids&gt;</code></p>
<dd>New in version 3.19. </p>
<p> where <code>compiler_ids</code> is a comma-separated list. <code>1</code> if the CMake&#8217;s compiler id of the ISPC compiler matches any one of the entries in <code>compiler_ids</code>, otherwise <code>0</code>. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable.</p>
<dt><code>$&lt;C_COMPILER_VERSION:version&gt;</code></p>
<dd><code>1</code> if the version of the C compiler matches <code>version</code>, otherwise <code>0</code>. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> variable.</p>
<dt><code>$&lt;CXX_COMPILER_VERSION:version&gt;</code></p>
<dd><code>1</code> if the version of the CXX compiler matches <code>version</code>, otherwise <code>0</code>. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> variable.</p>
<dt><code>$&lt;CUDA_COMPILER_VERSION:version&gt;</code></p>
<dd>New in version 3.15. </p>
<p> <code>1</code> if the version of the CXX compiler matches <code>version</code>, otherwise <code>0</code>. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> variable.</p>
<dt><code>$&lt;OBJC_COMPILER_VERSION:version&gt;</code></p>
<dd>New in version 3.16. </p>
<p> <code>1</code> if the version of the OBJC compiler matches <code>version</code>, otherwise <code>0</code>. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> variable.</p>
<dt><code>$&lt;OBJCXX_COMPILER_VERSION:version&gt;</code></p>
<dd>New in version 3.16. </p>
<p> <code>1</code> if the version of the OBJCXX compiler matches <code>version</code>, otherwise <code>0</code>. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> variable.</p>
<dt><code>$&lt;Fortran_COMPILER_VERSION:version&gt;</code></p>
<dd><code>1</code> if the version of the Fortran compiler matches <code>version</code>, otherwise <code>0</code>. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> variable.</p>
<dt><code>$&lt;HIP_COMPILER_VERSION:version&gt;</code></p>
<dd><code>1</code> if the version of the HIP compiler matches <code>version</code>, otherwise <code>0</code>. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> variable.</p>
<dt><code>$&lt;ISPC_COMPILER_VERSION:version&gt;</code></p>
<dd>New in version 3.19. </p>
<p> <code>1</code> if the version of the ISPC compiler matches <code>version</code>, otherwise <code>0</code>. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> variable.</p>
<dt><code>$&lt;TARGET_POLICY:policy&gt;</code></p>
<dd><code>1</code> if the <code>policy</code> was NEW when the &#8216;head&#8217; target was created, else <code>0</code>. If the <code>policy</code> was not set, the warning message for the policy will be emitted. This generator expression only works for a subset of policies.</p>
<dt><code>$&lt;COMPILE_FEATURES:features&gt;</code></p>
<dd>New in version 3.1. </p>
<p> where <code>features</code> is a comma-spearated list. Evaluates to <code>1</code> if all of the <code>features</code> are available for the &#8216;head&#8217; target, and <code>0</code> otherwise. If this expression is used while evaluating the link implementation of a target and if any dependency transitively increases the required <code>C_STANDARD</code> or <code>CXX_STANDARD</code> for the &#8216;head&#8217; target, an error is reported. See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.</p>
<dt><code>$&lt;COMPILE_LANG_AND_ID:language,compiler_ids&gt;</code></p>
<dd>New in version 3.15. </p>
<p> <code>1</code> when the language used for compilation unit matches <code>language</code> and the CMake&#8217;s compiler id of the language compiler matches any one of the entries in <code>compiler_ids</code>, otherwise <code>0</code>. This expression is a short form for the combination of <code>$&lt;COMPILE_LANGUAGE:language&gt;</code> and <code>$&lt;LANG_COMPILER_ID:compiler_ids&gt;</code>. This expression may be used to specify compile options, compile definitions, and include directories for source files of a particular language and compiler combination in a target. For example: </p>
<pre>add_executable(myapp main.cpp foo.c bar.cpp zot.cu)
target_compile_definitions(myapp
 PRIVATE $&lt;$&lt;COMPILE_LANG_AND_ID:CXX,AppleClang,Clang&gt;:COMPILING_CXX_WITH_CLANG&gt;
 $&lt;$&lt;COMPILE_LANG_AND_ID:CXX,Intel&gt;:COMPILING_CXX_WITH_INTEL&gt;
 $&lt;$&lt;COMPILE_LANG_AND_ID:C,Clang&gt;:COMPILING_C_WITH_CLANG&gt;
)</pre>
<p>This specifies the use of different compile definitions based on both the compiler id and compilation language. This example will have a <code>COMPILING_CXX_WITH_CLANG</code> compile definition when Clang is the CXX compiler, and <code>COMPILING_CXX_WITH_INTEL</code> when Intel is the CXX compiler. Likewise when the C compiler is Clang it will only see the <code>COMPILING_C_WITH_CLANG</code> definition. </p>
<p> Without the <code>COMPILE_LANG_AND_ID</code> generator expression the same logic would be expressed as: </p>
<pre>target_compile_definitions(myapp
 PRIVATE $&lt;$&lt;AND:$&lt;COMPILE_LANGUAGE:CXX&gt;,$&lt;CXX_COMPILER_ID:AppleClang,Clang&gt;&gt;:COMPILING_CXX_WITH_CLANG&gt;
 $&lt;$&lt;AND:$&lt;COMPILE_LANGUAGE:CXX&gt;,$&lt;CXX_COMPILER_ID:Intel&gt;&gt;:COMPILING_CXX_WITH_INTEL&gt;
 $&lt;$&lt;AND:$&lt;COMPILE_LANGUAGE:C&gt;,$&lt;C_COMPILER_ID:Clang&gt;&gt;:COMPILING_C_WITH_CLANG&gt;
)</pre>
<dt><code>$&lt;COMPILE_LANGUAGE:languages&gt;</code></p>
<dd>New in version 3.3. </p>
<p> <code>1</code> when the language used for compilation unit matches any of the entries in <code>languages</code>, otherwise <code>0</code>. This expression may be used to specify compile options, compile definitions, and include directories for source files of a particular language in a target. For example: </p>
<pre>add_executable(myapp main.cpp foo.c bar.cpp zot.cu)
target_compile_options(myapp
 PRIVATE $&lt;$&lt;COMPILE_LANGUAGE:CXX&gt;:-fno-exceptions&gt;
)
target_compile_definitions(myapp
 PRIVATE $&lt;$&lt;COMPILE_LANGUAGE:CXX&gt;:COMPILING_CXX&gt;
 $&lt;$&lt;COMPILE_LANGUAGE:CUDA&gt;:COMPILING_CUDA&gt;
)
target_include_directories(myapp
 PRIVATE $&lt;$&lt;COMPILE_LANGUAGE:CXX,CUDA&gt;:/opt/foo/headers&gt;
)</pre>
<p>This specifies the use of the <code>-fno-exceptions</code> compile option, <code>COMPILING_CXX</code> compile definition, and <code>cxx_headers</code> include directory for C++ only (compiler id checks elided). It also specifies a <code>COMPILING_CUDA</code> compile definition for CUDA. </p>
<p> Note that with Visual Studio Generators and <code>Xcode</code> there is no way to represent target-wide compile definitions or include directories separately for <code>C</code> and <code>CXX</code> languages. Also, with Visual Studio Generators there is no way to represent target-wide flags separately for <code>C</code> and <code>CXX</code> languages. Under these generators, expressions for both C and C++ sources will be evaluated using <code>CXX</code> if there are any C++ sources and otherwise using <code>C</code>. A workaround is to create separate libraries for each source file language instead: </p>
<pre>add_library(myapp_c foo.c)
add_library(myapp_cxx bar.cpp)
target_compile_options(myapp_cxx PUBLIC -fno-exceptions)
add_executable(myapp main.cpp)
target_link_libraries(myapp myapp_c myapp_cxx)</pre>
<dt><code>$&lt;LINK_LANG_AND_ID:language,compiler_ids&gt;</code></p>
<dd>New in version 3.18. </p>
<p> <code>1</code> when the language used for link step matches <code>language</code> and the CMake&#8217;s compiler id of the language linker matches any one of the entries in <code>compiler_ids</code>, otherwise <code>0</code>. This expression is a short form for the combination of <code>$&lt;LINK_LANGUAGE:language&gt;</code> and <code>$&lt;LANG_COMPILER_ID:compiler_ids&gt;</code>. This expression may be used to specify link libraries, link options, link directories and link dependencies of a particular language and linker combination in a target. For example: </p>
<pre>add_library(libC_Clang ...)
add_library(libCXX_Clang ...)
add_library(libC_Intel ...)
add_library(libCXX_Intel ...)
add_executable(myapp main.c)
if (CXX_CONFIG)
 target_sources(myapp PRIVATE file.cxx)
endif()
target_link_libraries(myapp
 PRIVATE $&lt;$&lt;LINK_LANG_AND_ID:CXX,Clang,AppleClang&gt;:libCXX_Clang&gt;
 $&lt;$&lt;LINK_LANG_AND_ID:C,Clang,AppleClang&gt;:libC_Clang&gt;
 $&lt;$&lt;LINK_LANG_AND_ID:CXX,Intel&gt;:libCXX_Intel&gt;
 $&lt;$&lt;LINK_LANG_AND_ID:C,Intel&gt;:libC_Intel&gt;)</pre>
<p>This specifies the use of different link libraries based on both the compiler id and link language. This example will have target <code>libCXX_Clang</code> as link dependency when <code>Clang</code> or <code>AppleClang</code> is the <code>CXX</code> linker, and <code>libCXX_Intel</code> when <code>Intel</code> is the <code>CXX</code> linker. Likewise when the <code>C</code> linker is <code>Clang</code> or <code>AppleClang</code>, target <code>libC_Clang</code> will be added as link dependency and <code>libC_Intel</code> when <code>Intel</code> is the <code>C</code> linker. </p>
<p> See <i>the note related to</i> <code>$&lt;LINK_LANGUAGE:language&gt;</code> for constraints about the usage of this generator expression.</p>
<dt><code>$&lt;LINK_LANGUAGE:languages&gt;</code></p>
<dd>New in version 3.18. </p>
<p> <code>1</code> when the language used for link step matches any of the entries in <code>languages</code>, otherwise <code>0</code>. This expression may be used to specify link libraries, link options, link directories and link dependencies of a particular language in a target. For example: </p>
<pre>add_library(api_C ...)
add_library(api_CXX ...)
add_library(api INTERFACE)
target_link_options(api INTERFACE $&lt;$&lt;LINK_LANGUAGE:C&gt;:-opt_c&gt;
 $&lt;$&lt;LINK_LANGUAGE:CXX&gt;:-opt_cxx&gt;)
target_link_libraries(api INTERFACE $&lt;$&lt;LINK_LANGUAGE:C&gt;:api_C&gt;
 $&lt;$&lt;LINK_LANGUAGE:CXX&gt;:api_CXX&gt;)
add_executable(myapp1 main.c)
target_link_options(myapp1 PRIVATE api)
add_executable(myapp2 main.cpp)
target_link_options(myapp2 PRIVATE api)</pre>
<p>This specifies to use the <code>api</code> target for linking targets <code>myapp1</code> and <code>myapp2</code>. In practice, <code>myapp1</code> will link with target <code>api_C</code> and option <code>-opt_c</code> because it will use <code>C</code> as link language. And <code>myapp2</code> will link with <code>api_CXX</code> and option <code>-opt_cxx</code> because <code>CXX</code> will be the link language. </p>
<p> <code>NOTE:</code> To determine the link language of a target, it is required to collect, transitively, all the targets which will be linked to it. So, for link libraries properties, a double evaluation will be done. During the first evaluation, <code>$&lt;LINK_LANGUAGE:..&gt;</code> expressions will always return <code>0</code>. The link language computed after this first pass will be used to do the second pass. To avoid inconsistency, it is required that the second pass do not change the link language. Moreover, to avoid unexpected side-effects, it is required to specify complete entities as part of the <code>$&lt;LINK_LANGUAGE:..&gt;</code> expression. For example: </p>
<pre>add_library(lib STATIC file.cxx)
add_library(libother STATIC file.c)
# bad usage
add_executable(myapp1 main.c)
target_link_libraries(myapp1 PRIVATE lib$&lt;$&lt;LINK_LANGUAGE:C&gt;:other&gt;)
# correct usage
add_executable(myapp2 main.c)
target_link_libraries(myapp2 PRIVATE $&lt;$&lt;LINK_LANGUAGE:C&gt;:libother&gt;)</pre>
<p>In this example, for <code>myapp1</code>, the first pass will, unexpectedly, determine that the link language is <code>CXX</code> because the evaluation of the generator expression will be an empty string so <code>myapp1</code> will depends on target <code>lib</code> which is <code>C++</code>. On the contrary, for <code>myapp2</code>, the first evaluation will give <code>C</code> as link language, so the second pass will correctly add target <code>libother</code> as link dependency.</p>
<dt><code>$&lt;DEVICE_LINK:list&gt;</code></p>
<dd>New in version 3.18. </p>
<p> Returns the list if it is the device link step, an empty list otherwise. The device link step is controlled by <code>CUDA_SEPARABLE_COMPILATION</code> and <code>CUDA_RESOLVE_DEVICE_SYMBOLS</code> properties and policy <code>CMP0105</code>. This expression can only be used to specify link options.</p>
<dt><code>$&lt;HOST_LINK:list&gt;</code></p>
<dd>New in version 3.18. </p>
<p> Returns the list if it is the normal link step, an empty list otherwise. This expression is mainly useful when a device link step is also involved (see <code>$&lt;DEVICE_LINK:list&gt;</code> generator expression). This expression can only be used to specify link options.</dl>
<h2>String-Valued Generator Expressions</h2>
<p>These expressions expand to some string. For example, </p>
<pre>include_directories(/usr/include/$&lt;CXX_COMPILER_ID&gt;/)</pre>
<p>expands to <code>/usr/include/GNU/</code> or <code>/usr/include/Clang/</code> etc, depending on the compiler identifier. </p>
<p> String-valued expressions may also be combined with other expressions. Here an example for a string-valued expression within a boolean expressions within a conditional expression: </p>
<pre>$&lt;$&lt;VERSION_LESS:$&lt;CXX_COMPILER_VERSION&gt;,4.2.0&gt;:OLD_COMPILER&gt;</pre>
<p>expands to <code>OLD_COMPILER</code> if the <code>CMAKE_CXX_COMPILER_VERSION</code> is less than 4.2.0. </p>
<p> And here two nested string-valued expressions: </p>
<pre>-I$&lt;JOIN:$&lt;TARGET_PROPERTY:INCLUDE_DIRECTORIES&gt;, -I&gt;</pre>
<p>generates a string of the entries in the <code>INCLUDE_DIRECTORIES</code> target property with each entry preceded by <code>-I</code>. </p>
<p> Expanding on the previous example, if one first wants to check if the <code>INCLUDE_DIRECTORIES</code> property is non-empty, then it is advisable to introduce a helper variable to keep the code readable: </p>
<pre>set(prop &quot;$&lt;TARGET_PROPERTY:INCLUDE_DIRECTORIES&gt;&quot;) # helper variable
$&lt;$&lt;BOOL:${prop}&gt;:-I$&lt;JOIN:${prop}, -I&gt;&gt;</pre>
<p>The following string-valued generator expressions are available:</p>
<h3>Escaped Characters</h3>
<p>String literals to escape the special meaning a character would otherwise have:</p>
<dl>
<dt><code>$&lt;ANGLE-R&gt;</code></p>
<dd>A literal <code>&gt;</code>. Used for example to compare strings that contain a <code>&gt;</code>.</p>
<dt><code>$&lt;COMMA&gt;</code></p>
<dd>A literal <code>,</code>. Used for example to compare strings which contain a <code>,</code>.</p>
<dt><code>$&lt;SEMICOLON&gt;</code></p>
<dd>A literal <code>;</code>. Used to prevent list expansion on an argument with <code>;</code>.</dl>
<h3>Conditional Expressions</h3>
<p>Conditional generator expressions depend on a boolean condition that must be <code>0</code> or <code>1</code>.</p>
<dl>
<dt><code>$&lt;condition:true_string&gt;</code></p>
<dd>Evaluates to <code>true_string</code> if <code>condition</code> is <code>1</code>. Otherwise evaluates to the empty string.</p>
<dt><code>$&lt;IF:condition,true_string,false_string&gt;</code></p>
<dd>New in version 3.8. </p>
<p> Evaluates to <code>true_string</code> if <code>condition</code> is <code>1</code>. Otherwise evaluates to <code>false_string</code>. </p>
<p> Typically, the <code>condition</code> is a <i>boolean generator expression</i>. For instance, </p>
<pre>$&lt;$&lt;CONFIG:Debug&gt;:DEBUG_MODE&gt;</pre>
<p>expands to <code>DEBUG_MODE</code> when the <code>Debug</code> configuration is used, and otherwise expands to the empty string.</dl>
<h3>String Transformations</h3>
<dl>
<dt><code>$&lt;JOIN:list,string&gt;</code></p>
<dd>Joins the list with the content of <code>string</code>.</p>
<dt><code>$&lt;REMOVE_DUPLICATES:list&gt;</code></p>
<dd>New in version 3.15. </p>
<p> Removes duplicated items in the given <code>list</code>.</p>
<dt><code>$&lt;FILTER:list,INCLUDE|EXCLUDE,regex&gt;</code></p>
<dd>New in version 3.15. </p>
<p> Includes or removes items from <code>list</code> that match the regular expression <code>regex</code>.</p>
<dt><code>$&lt;LOWER_CASE:string&gt;</code></p>
<dd>Content of <code>string</code> converted to lower case.</p>
<dt><code>$&lt;UPPER_CASE:string&gt;</code></p>
<dd>Content of <code>string</code> converted to upper case.</p>
<dt><code>$&lt;GENEX_EVAL:expr&gt;</code></p>
<dd>New in version 3.12. </p>
<p> Content of <code>expr</code> evaluated as a generator expression in the current context. This enables consumption of generator expressions whose evaluation results itself in generator expressions.</p>
<dt><code>$&lt;TARGET_GENEX_EVAL:tgt,expr&gt;</code></p>
<dd>New in version 3.12. </p>
<p> Content of <code>expr</code> evaluated as a generator expression in the context of <code>tgt</code> target. This enables consumption of custom target properties that themselves contain generator expressions. </p>
<p> Having the capability to evaluate generator expressions is very useful when you want to manage custom properties supporting generator expressions. For example: </p>
<pre>add_library(foo ...)
set_property(TARGET foo PROPERTY
 CUSTOM_KEYS $&lt;$&lt;CONFIG:DEBUG&gt;:FOO_EXTRA_THINGS&gt;
)
add_custom_target(printFooKeys
 COMMAND ${CMAKE_COMMAND} -E echo $&lt;TARGET_PROPERTY:foo,CUSTOM_KEYS&gt;
)</pre>
<p>This naive implementation of the <code>printFooKeys</code> custom command is wrong because <code>CUSTOM_KEYS</code> target property is not evaluated and the content is passed as is (i.e. <code>$&lt;$&lt;CONFIG:DEBUG&gt;:FOO_EXTRA_THINGS&gt;</code>). </p>
<p> To have the expected result (i.e. <code>FOO_EXTRA_THINGS</code> if config is <code>Debug</code>), it is required to evaluate the output of <code>$&lt;TARGET_PROPERTY:foo,CUSTOM_KEYS&gt;</code>: </p>
<pre>add_custom_target(printFooKeys
 COMMAND ${CMAKE_COMMAND} -E
 echo $&lt;TARGET_GENEX_EVAL:foo,$&lt;TARGET_PROPERTY:foo,CUSTOM_KEYS&gt;&gt;
)</pre>
</dl>
<h3>Variable Queries</h3>
<dl>
<dt><code>$&lt;CONFIG&gt;</code></p>
<dd>Configuration name.</p>
<dt><code>$&lt;CONFIGURATION&gt;</code></p>
<dd>Configuration name. Deprecated since CMake 3.0. Use <code>CONFIG</code> instead.</p>
<dt><code>$&lt;PLATFORM_ID&gt;</code></p>
<dd>The current system&#8217;s CMake platform id. See also the <code>CMAKE_SYSTEM_NAME</code> variable.</p>
<dt><code>$&lt;C_COMPILER_ID&gt;</code></p>
<dd>The CMake&#8217;s compiler id of the C compiler used. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable.</p>
<dt><code>$&lt;CXX_COMPILER_ID&gt;</code></p>
<dd>The CMake&#8217;s compiler id of the CXX compiler used. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable.</p>
<dt><code>$&lt;CUDA_COMPILER_ID&gt;</code></p>
<dd>The CMake&#8217;s compiler id of the CUDA compiler used. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable.</p>
<dt><code>$&lt;OBJC_COMPILER_ID&gt;</code></p>
<dd>New in version 3.16. </p>
<p> The CMake&#8217;s compiler id of the OBJC compiler used. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable.</p>
<dt><code>$&lt;OBJCXX_COMPILER_ID&gt;</code></p>
<dd>New in version 3.16. </p>
<p> The CMake&#8217;s compiler id of the OBJCXX compiler used. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable.</p>
<dt><code>$&lt;Fortran_COMPILER_ID&gt;</code></p>
<dd>The CMake&#8217;s compiler id of the Fortran compiler used. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable.</p>
<dt><code>$&lt;HIP_COMPILER_ID&gt;</code></p>
<dd>The CMake&#8217;s compiler id of the HIP compiler used. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable.</p>
<dt><code>$&lt;ISPC_COMPILER_ID&gt;</code></p>
<dd>New in version 3.19. </p>
<p> The CMake&#8217;s compiler id of the ISPC compiler used. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable.</p>
<dt><code>$&lt;C_COMPILER_VERSION&gt;</code></p>
<dd>The version of the C compiler used. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> variable.</p>
<dt><code>$&lt;CXX_COMPILER_VERSION&gt;</code></p>
<dd>The version of the CXX compiler used. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> variable.</p>
<dt><code>$&lt;CUDA_COMPILER_VERSION&gt;</code></p>
<dd>The version of the CUDA compiler used. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> variable.</p>
<dt><code>$&lt;OBJC_COMPILER_VERSION&gt;</code></p>
<dd>New in version 3.16. </p>
<p> The version of the OBJC compiler used. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> variable.</p>
<dt><code>$&lt;OBJCXX_COMPILER_VERSION&gt;</code></p>
<dd>New in version 3.16. </p>
<p> The version of the OBJCXX compiler used. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> variable.</p>
<dt><code>$&lt;Fortran_COMPILER_VERSION&gt;</code></p>
<dd>The version of the Fortran compiler used. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> variable.</p>
<dt><code>$&lt;HIP_COMPILER_VERSION&gt;</code></p>
<dd>The version of the HIP compiler used. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> variable.</p>
<dt><code>$&lt;ISPC_COMPILER_VERSION&gt;</code></p>
<dd>New in version 3.19. </p>
<p> The version of the ISPC compiler used. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> variable.</p>
<dt><code>$&lt;COMPILE_LANGUAGE&gt;</code></p>
<dd>New in version 3.3. </p>
<p> The compile language of source files when evaluating compile options. See <i>the related boolean expression</i> <code>$&lt;COMPILE_LANGUAGE:language&gt;</code> for notes about the portability of this generator expression.</p>
<dt><code>$&lt;LINK_LANGUAGE&gt;</code></p>
<dd>New in version 3.18. </p>
<p> The link language of target when evaluating link options. See <i>the related boolean expression</i> <code>$&lt;LINK_LANGUAGE:language&gt;</code> for notes about the portability of this generator expression. </p>
<p> <code>NOTE:</code> This generator expression is not supported by the link libraries properties to avoid side-effects due to the double evaluation of these properties.</dl>
<h3>Target-Dependent Queries</h3>
<p>These queries refer to a target <code>tgt</code>. This can be any runtime artifact, namely:</p>
<dl>
<dt>&bull;</p>
<dd>an executable target created by <code>add_executable()</code></p>
<dt>&bull;</p>
<dd>a shared library target (<code>.so</code>, <code>.dll</code> but not their <code>.lib</code> import library) created by <code>add_library()</code></p>
<dt>&bull;</p>
<dd>a static library target created by <code>add_library()</code> </p>
<p> In the following, &quot;the <code>tgt</code> filename&quot; means the name of the <code>tgt</code> binary file. This has to be distinguished from &quot;the target name&quot;, which is just the string <code>tgt</code>.</p>
<dt><code>$&lt;TARGET_NAME_IF_EXISTS:tgt&gt;</code></p>
<dd>New in version 3.12. </p>
<p> The target name <code>tgt</code> if the target exists, an empty string otherwise. </p>
<p> Note that <code>tgt</code> is not added as a dependency of the target this expression is evaluated on.</p>
<dt><code>$&lt;TARGET_FILE:tgt&gt;</code></p>
<dd>Full path to the <code>tgt</code> binary file.</p>
<dt><code>$&lt;TARGET_FILE_BASE_NAME:tgt&gt;</code></p>
<dd>New in version 3.15. </p>
<p> Base name of <code>tgt</code>, i.e. <code>$&lt;TARGET_FILE_NAME:tgt&gt;</code> without prefix and suffix. For example, if the <code>tgt</code> filename is <code>libbase.so</code>, the base name is <code>base</code>. </p>
<p> See also the <code>OUTPUT_NAME</code>, <code>ARCHIVE_OUTPUT_NAME</code>, <code>LIBRARY_OUTPUT_NAME</code> and <code>RUNTIME_OUTPUT_NAME</code> target properties and their configuration specific variants <code>OUTPUT_NAME_&lt;CONFIG&gt;</code>, <code>ARCHIVE_OUTPUT_NAME_&lt;CONFIG&gt;</code>, <code>LIBRARY_OUTPUT_NAME_&lt;CONFIG&gt;</code> and <code>RUNTIME_OUTPUT_NAME_&lt;CONFIG&gt;</code>. </p>
<p> The <code>&lt;CONFIG&gt;_POSTFIX</code> and <code>DEBUG_POSTFIX</code> target properties can also be considered. </p>
<p> Note that <code>tgt</code> is not added as a dependency of the target this expression is evaluated on.</p>
<dt><code>$&lt;TARGET_FILE_PREFIX:tgt&gt;</code></p>
<dd>New in version 3.15. </p>
<p> Prefix of the <code>tgt</code> filename (such as <code>lib</code>). </p>
<p> See also the <code>PREFIX</code> target property. </p>
<p> Note that <code>tgt</code> is not added as a dependency of the target this expression is evaluated on.</p>
<dt><code>$&lt;TARGET_FILE_SUFFIX:tgt&gt;</code></p>
<dd>New in version 3.15. </p>
<p> Suffix of the <code>tgt</code> filename (extension such as <code>.so</code> or <code>.exe</code>). </p>
<p> See also the <code>SUFFIX</code> target property. </p>
<p> Note that <code>tgt</code> is not added as a dependency of the target this expression is evaluated on.</p>
<dt><code>$&lt;TARGET_FILE_NAME:tgt&gt;</code></p>
<dd>The <code>tgt</code> filename. </p>
<p> Note that <code>tgt</code> is not added as a dependency of the target this expression is evaluated on (see policy <code>CMP0112</code>).</p>
<dt><code>$&lt;TARGET_FILE_DIR:tgt&gt;</code></p>
<dd>Directory of the <code>tgt</code> binary file. </p>
<p> Note that <code>tgt</code> is not added as a dependency of the target this expression is evaluated on (see policy <code>CMP0112</code>).</p>
<dt><code>$&lt;TARGET_LINKER_FILE:tgt&gt;</code></p>
<dd>File used when linking to the <code>tgt</code> target. This will usually be the library that <code>tgt</code> represents (<code>.a</code>, <code>.lib</code>, <code>.so</code>), but for a shared library on DLL platforms, it would be the <code>.lib</code> import library associated with the DLL.</p>
<dt><code>$&lt;TARGET_LINKER_FILE_BASE_NAME:tgt&gt;</code></p>
<dd>New in version 3.15. </p>
<p> Base name of file used to link the target <code>tgt</code>, i.e. <code>$&lt;TARGET_LINKER_FILE_NAME:tgt&gt;</code> without prefix and suffix. For example, if target file name is <code>libbase.a</code>, the base name is <code>base</code>. </p>
<p> See also the <code>OUTPUT_NAME</code>, <code>ARCHIVE_OUTPUT_NAME</code>, and <code>LIBRARY_OUTPUT_NAME</code> target properties and their configuration specific variants <code>OUTPUT_NAME_&lt;CONFIG&gt;</code>, <code>ARCHIVE_OUTPUT_NAME_&lt;CONFIG&gt;</code> and <code>LIBRARY_OUTPUT_NAME_&lt;CONFIG&gt;</code>. </p>
<p> The <code>&lt;CONFIG&gt;_POSTFIX</code> and <code>DEBUG_POSTFIX</code> target properties can also be considered. </p>
<p> Note that <code>tgt</code> is not added as a dependency of the target this expression is evaluated on.</p>
<dt><code>$&lt;TARGET_LINKER_FILE_PREFIX:tgt&gt;</code></p>
<dd>New in version 3.15. </p>
<p> Prefix of file used to link target <code>tgt</code>. </p>
<p> See also the <code>PREFIX</code> and <code>IMPORT_PREFIX</code> target properties. </p>
<p> Note that <code>tgt</code> is not added as a dependency of the target this expression is evaluated on.</p>
<dt><code>$&lt;TARGET_LINKER_FILE_SUFFIX:tgt&gt;</code></p>
<dd>New in version 3.15. </p>
<p> Suffix of file used to link where <code>tgt</code> is the name of a target. </p>
<p> The suffix corresponds to the file extension (such as &quot;.so&quot; or &quot;.lib&quot;). </p>
<p> See also the <code>SUFFIX</code> and <code>IMPORT_SUFFIX</code> target properties. </p>
<p> Note that <code>tgt</code> is not added as a dependency of the target this expression is evaluated on.</p>
<dt><code>$&lt;TARGET_LINKER_FILE_NAME:tgt&gt;</code></p>
<dd>Name of file used to link target <code>tgt</code>. </p>
<p> Note that <code>tgt</code> is not added as a dependency of the target this expression is evaluated on (see policy <code>CMP0112</code>).</p>
<dt><code>$&lt;TARGET_LINKER_FILE_DIR:tgt&gt;</code></p>
<dd>Directory of file used to link target <code>tgt</code>. </p>
<p> Note that <code>tgt</code> is not added as a dependency of the target this expression is evaluated on (see policy <code>CMP0112</code>).</p>
<dt><code>$&lt;TARGET_SONAME_FILE:tgt&gt;</code></p>
<dd>File with soname (<code>.so.3</code>) where <code>tgt</code> is the name of a target.</p>
<dt><code>$&lt;TARGET_SONAME_FILE_NAME:tgt&gt;</code></p>
<dd>Name of file with soname (<code>.so.3</code>). </p>
<p> Note that <code>tgt</code> is not added as a dependency of the target this expression is evaluated on (see policy <code>CMP0112</code>).</p>
<dt><code>$&lt;TARGET_SONAME_FILE_DIR:tgt&gt;</code></p>
<dd>Directory of with soname (<code>.so.3</code>). </p>
<p> Note that <code>tgt</code> is not added as a dependency of the target this expression is evaluated on (see policy <code>CMP0112</code>).</p>
<dt><code>$&lt;TARGET_PDB_FILE:tgt&gt;</code></p>
<dd>New in version 3.1. </p>
<p> Full path to the linker generated program database file (.pdb) where <code>tgt</code> is the name of a target. </p>
<p> See also the <code>PDB_NAME</code> and <code>PDB_OUTPUT_DIRECTORY</code> target properties and their configuration specific variants <code>PDB_NAME_&lt;CONFIG&gt;</code> and <code>PDB_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code>.</p>
<dt><code>$&lt;TARGET_PDB_FILE_BASE_NAME:tgt&gt;</code></p>
<dd>New in version 3.15. </p>
<p> Base name of the linker generated program database file (.pdb) where <code>tgt</code> is the name of a target. </p>
<p> The base name corresponds to the target PDB file name (see <code>$&lt;TARGET_PDB_FILE_NAME:tgt&gt;</code>) without prefix and suffix. For example, if target file name is <code>base.pdb</code>, the base name is <code>base</code>. </p>
<p> See also the <code>PDB_NAME</code> target property and its configuration specific variant <code>PDB_NAME_&lt;CONFIG&gt;</code>. </p>
<p> The <code>&lt;CONFIG&gt;_POSTFIX</code> and <code>DEBUG_POSTFIX</code> target properties can also be considered. </p>
<p> Note that <code>tgt</code> is not added as a dependency of the target this expression is evaluated on.</p>
<dt><code>$&lt;TARGET_PDB_FILE_NAME:tgt&gt;</code></p>
<dd>New in version 3.1. </p>
<p> Name of the linker generated program database file (.pdb). </p>
<p> Note that <code>tgt</code> is not added as a dependency of the target this expression is evaluated on (see policy <code>CMP0112</code>).</p>
<dt><code>$&lt;TARGET_PDB_FILE_DIR:tgt&gt;</code></p>
<dd>New in version 3.1. </p>
<p> Directory of the linker generated program database file (.pdb). </p>
<p> Note that <code>tgt</code> is not added as a dependency of the target this expression is evaluated on (see policy <code>CMP0112</code>).</p>
<dt><code>$&lt;TARGET_BUNDLE_DIR:tgt&gt;</code></p>
<dd>New in version 3.9. </p>
<p> Full path to the bundle directory (<code>my.app</code>, <code>my.framework</code>, or <code>my.bundle</code>) where <code>tgt</code> is the name of a target. </p>
<p> Note that <code>tgt</code> is not added as a dependency of the target this expression is evaluated on (see policy <code>CMP0112</code>).</p>
<dt><code>$&lt;TARGET_BUNDLE_CONTENT_DIR:tgt&gt;</code></p>
<dd>New in version 3.9. </p>
<p> Full path to the bundle content directory where <code>tgt</code> is the name of a target. For the macOS SDK it leads to <code>my.app/Contents</code>, <code>my.framework</code>, or <code>my.bundle/Contents</code>. For all other SDKs (e.g. iOS) it leads to <code>my.app</code>, <code>my.framework</code>, or <code>my.bundle</code> due to the flat bundle structure. </p>
<p> Note that <code>tgt</code> is not added as a dependency of the target this expression is evaluated on (see policy <code>CMP0112</code>).</p>
<dt><code>$&lt;TARGET_PROPERTY:tgt,prop&gt;</code></p>
<dd>Value of the property <code>prop</code> on the target <code>tgt</code>. </p>
<p> Note that <code>tgt</code> is not added as a dependency of the target this expression is evaluated on.</p>
<dt><code>$&lt;TARGET_PROPERTY:prop&gt;</code></p>
<dd>Value of the property <code>prop</code> on the target for which the expression is being evaluated. Note that for generator expressions in Target Usage Requirements this is the consuming target rather than the target specifying the requirement.</p>
<dt><code>$&lt;TARGET_RUNTIME_DLLS:tgt&gt;</code></p>
<dd>New in version 3.21. </p>
<p> List of DLLs that the target depends on at runtime. This is determined by the locations of all the <code>SHARED</code> and <code>MODULE</code> targets in the target&#8217;s transitive dependencies. Using this generator expression on targets other than executables, <code>SHARED</code> libraries, and <code>MODULE</code> libraries is an error. On non-DLL platforms, it evaluates to an empty string. </p>
<p> This generator expression can be used to copy all of the DLLs that a target depends on into its output directory in a <code>POST_BUILD</code> custom command. For example: </p>
<pre>find_package(foo CONFIG REQUIRED) # package generated by install(EXPORT)
add_executable(exe main.c)
target_link_libraries(exe PRIVATE foo::foo foo::bar)
add_custom_command(TARGET exe POST_BUILD
 COMMAND ${CMAKE_COMMAND} -E copy $&lt;TARGET_RUNTIME_DLLS:exe&gt; $&lt;TARGET_FILE_DIR:exe&gt;
 COMMAND_EXPAND_LISTS
 )</pre>
<p><code>NOTE:</code> Imported Targets are supported only if they know the location of their <code>.dll</code> files. An imported <code>SHARED</code> or <code>MODULE</code> library must have <code>IMPORTED_LOCATION</code> set to its <code>.dll</code> file. See the add_library imported libraries section for details. Many Find Modules produce imported targets with the <code>UNKNOWN</code> type and therefore will be ignored.</p>
<dt><code>$&lt;INSTALL_PREFIX&gt;</code></p>
<dd>Content of the install prefix when the target is exported via <code>install(EXPORT)</code>, or when evaluated in the <code>INSTALL_NAME_DIR</code> property or the <code>INSTALL_NAME_DIR</code> argument of <code>install(RUNTIME_DEPENDENCY_SET)</code>, and empty otherwise.</dl>
<h3>Output-Related Expressions</h3>
<dl>
<dt><code>$&lt;TARGET_NAME:&#8230;&gt;</code></p>
<dd>Marks <code>&#8230;</code> as being the name of a target. This is required if exporting targets to multiple dependent export sets. The <code>&#8230;</code> must be a literal name of a target- it may not contain generator expressions.</p>
<dt><code>$&lt;LINK_ONLY:&#8230;&gt;</code></p>
<dd>New in version 3.1. </p>
<p> Content of <code>&#8230;</code> except when evaluated in a link interface while propagating Target Usage Requirements, in which case it is the empty string. Intended for use only in an <code>INTERFACE_LINK_LIBRARIES</code> target property, perhaps via the <code>target_link_libraries()</code> command, to specify private link dependencies without other usage requirements.</p>
<dt><code>$&lt;INSTALL_INTERFACE:&#8230;&gt;</code></p>
<dd>Content of <code>&#8230;</code> when the property is exported using <code>install(EXPORT)</code>, and empty otherwise.</p>
<dt><code>$&lt;BUILD_INTERFACE:&#8230;&gt;</code></p>
<dd>Content of <code>&#8230;</code> when the property is exported using <code>export()</code>, or when the target is used by another target in the same buildsystem. Expands to the empty string otherwise.</p>
<dt><code>$&lt;MAKE_C_IDENTIFIER:&#8230;&gt;</code></p>
<dd>Content of <code>&#8230;</code> converted to a C identifier. The conversion follows the same behavior as <code>string(MAKE_C_IDENTIFIER)</code>.</p>
<dt><code>$&lt;TARGET_OBJECTS:objLib&gt;</code></p>
<dd>New in version 3.1. </p>
<p> List of objects resulting from build of <code>objLib</code>.</p>
<dt><code>$&lt;SHELL_PATH:&#8230;&gt;</code></p>
<dd>New in version 3.4. </p>
<p> Content of <code>&#8230;</code> converted to shell path style. For example, slashes are converted to backslashes in Windows shells and drive letters are converted to posix paths in MSYS shells. The <code>&#8230;</code> must be an absolute path. </p>
<p> New in version 3.14: The <code>&#8230;</code> may be a semicolon-separated list of paths, in which case each path is converted individually and a result list is generated using the shell path separator (<code>:</code> on POSIX and <code>;</code> on Windows). Be sure to enclose the argument containing this genex in double quotes in CMake source code so that <code>;</code> does not split arguments. </p>
<dt><code>$&lt;OUTPUT_CONFIG:&#8230;&gt;</code></p>
<dd>New in version 3.20. </p>
<p> Only valid in <code>add_custom_command()</code> and <code>add_custom_target()</code> as the outer-most generator expression in an argument. With the <code>Ninja Multi-Config</code> generator, generator expressions in <code>&#8230;</code> are evaluated using the custom command&#8217;s &quot;output config&quot;. With other generators, the content of <code>&#8230;</code> is evaluated normally.</p>
<dt><code>$&lt;COMMAND_CONFIG:&#8230;&gt;</code></p>
<dd>New in version 3.20. </p>
<p> Only valid in <code>add_custom_command()</code> and <code>add_custom_target()</code> as the outer-most generator expression in an argument. With the <code>Ninja Multi-Config</code> generator, generator expressions in <code>&#8230;</code> are evaluated using the custom command&#8217;s &quot;command config&quot;. With other generators, the content of <code>&#8230;</code> is evaluated normally.</dl>
<h2>Debugging</h2>
<p>Since generator expressions are evaluated during generation of the buildsystem, and not during processing of <code>CMakeLists.txt</code> files, it is not possible to inspect their result with the <code>message()</code> command. </p>
<p> One possible way to generate debug messages is to add a custom target, </p>
<pre>add_custom_target(genexdebug COMMAND ${CMAKE_COMMAND} -E echo &quot;$&lt;...&gt;&quot;)</pre>
<p>The shell command <code>make genexdebug</code> (invoked after execution of <code>cmake</code>) would then print the result of <code>$&lt;&#8230;&gt;</code>. </p>
<p> Another way is to write debug messages to a file: </p>
<pre>file(GENERATE OUTPUT filename CONTENT &quot;$&lt;...&gt;&quot;)</pre>
<h2>Copyright</h2>
<p>2000-2022 Kitware, Inc. and Contributors</p>
