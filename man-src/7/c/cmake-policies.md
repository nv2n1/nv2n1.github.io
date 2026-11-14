---
title: "cmake-policies(7)"
name: "cmake-policies"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake-policies/"
description: "cmake-policies – CMake Policies Reference"
---

<p>cmake-policies &#8211; CMake Policies Reference</p>
<h2>Introduction</h2>
<p>Policies in CMake are used to preserve backward compatible behavior across multiple releases. When a new policy is introduced, newer CMake versions will begin to warn about the backward compatible behavior. It is possible to disable the warning by explicitly requesting the OLD, or backward compatible behavior using the <code>cmake_policy()</code> command. It is also possible to request <code>NEW</code>, or non-backward compatible behavior for a policy, also avoiding the warning. Each policy can also be set to either <code>NEW</code> or <code>OLD</code> behavior explicitly on the command line with the <code>CMAKE_POLICY_DEFAULT_CMP&lt;NNNN&gt;</code> variable. </p>
<p> A policy is a deprecation mechanism and not a reliable feature toggle. A policy should almost never be set to <code>OLD</code>, except to silence warnings in an otherwise frozen or stable codebase, or temporarily as part of a larger migration path. The <code>OLD</code> behavior of each policy is undesirable and will be replaced with an error condition in a future release. </p>
<p> The <code>cmake_minimum_required()</code> command does more than report an error if a too-old version of CMake is used to build a project. It also sets all policies introduced in that CMake version or earlier to <code>NEW</code> behavior. To manage policies without increasing the minimum required CMake version, the <code>if(POLICY)</code> command may be used: </p>
<pre>if(POLICY CMP0990)
 cmake_policy(SET CMP0990 NEW)
endif()</pre>
<p>This has the effect of using the <code>NEW</code> behavior with newer CMake releases which users may be using and not issuing a compatibility warning. </p>
<p> The setting of a policy is confined in some cases to not propagate to the parent scope. For example, if the files read by the <code>include()</code> command or the <code>find_package()</code> command contain a use of <code>cmake_policy()</code>, that policy setting will not affect the caller by default. Both commands accept an optional <code>NO_POLICY_SCOPE</code> keyword to control this behavior. </p>
<p> The <code>CMAKE_MINIMUM_REQUIRED_VERSION</code> variable may also be used to determine whether to report an error on use of deprecated macros or functions.</p>
<h2>Policies Introduced By Cmake 3.22</h2>
<h3>Cmp0128</h3>
<p>New in version 3.22. </p>
<p> When this policy is set to <code>NEW</code>:</p>
<dl>
<dt>&bull;</p>
<dd><code>&lt;LANG&gt;_EXTENSIONS</code> is initialized to <code>CMAKE_&lt;LANG&gt;_EXTENSIONS</code> if set, otherwise falling back to <code>CMAKE_&lt;LANG&gt;_EXTENSIONS_DEFAULT</code>.</p>
<dt>&bull;</p>
<dd>Extensions are correctly enabled/disabled if <code>&lt;LANG&gt;_STANDARD</code> is unset or satisfied by the default.</p>
<dt>&bull;</p>
<dd>Standard mode-affecting flags aren&#8217;t added unless necessary to achieve the specified mode. </p>
<p> The <code>OLD</code> behavior:</p>
<dt>&bull;</p>
<dd>Initializes <code>&lt;LANG&gt;_EXTENSIONS</code> to <code>CMAKE_&lt;LANG&gt;_EXTENSIONS</code> if set, otherwise falling back to <code>ON</code>.</p>
<dt>&bull;</p>
<dd>Always adds a flag if <code>&lt;LANG&gt;_STANDARD</code> is set and <code>&lt;LANG&gt;_STANDARD_REQUIRED</code> is <code>OFF</code>.</p>
<dt>&bull;</p>
<dd>If <code>&lt;LANG&gt;_STANDARD</code> is unset:</p>
<dt>&bull;</p>
<dd>Doesn&#8217;t disable extensions even if <code>&lt;LANG&gt;_EXTENSIONS</code> is <code>OFF</code>.</p>
<dt>&bull;</p>
<dd>Fails to enable extensions if <code>&lt;LANG&gt;_EXTENSIONS</code> is <code>ON</code> except for the <code>IAR</code> compiler. </p>
<p> Code may need to be updated for the <code>NEW</code> behavior in the following cases:</p>
<dt>&bull;</p>
<dd>If a standard mode flag previously overridden by CMake&#8217;s and not used during compiler detection now takes effect due to CMake no longer adding one as the default detected is appropriate. </p>
<p> Such code should be converted to either:</p>
<dt>&bull;</p>
<dd>Use <code>&lt;LANG&gt;_STANDARD</code> and <code>&lt;LANG&gt;_EXTENSIONS</code> instead of manually adding flags.</p>
<dt>&bull;</p>
<dd>Or ensure the manually-specified flags are used during compiler detection.</p>
<dt>&bull;</p>
<dd>If extensions were disabled without <code>&lt;LANG&gt;_STANDARD</code> being set CMake previously wouldn&#8217;t actually disable extensions. </p>
<p> Such code should be updated to not disable extensions if they are required.</p>
<dt>&bull;</p>
<dd>If extensions were enabled/disabled when <code>&lt;LANG&gt;_STANDARD</code> was satisfied by the compiler&#8217;s default CMake previously wouldn&#8217;t actually enable/disable extensions. </p>
<p> Such code should be updated to set the correct extensions mode. </p>
<p> If compiler flags affecting the standard mode are used during compiler detection (for example in <code>a toolchain file</code> using <code>CMAKE_&lt;LANG&gt;_FLAGS_INIT</code>) then they will affect the detected default <code>standard</code> and <code>extensions</code>. </p>
<p> Unlike many policies, CMake version 3.22.1 does <i>not</i> warn when the policy is not set and simply uses the <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. See documentation of the <code>CMAKE_POLICY_WARNING_CMP0128</code> variable to control the warning. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</dl>
<h3>Cmp0127</h3>
<p>New in version 3.22. </p>
<p> <code>cmake_dependent_option()</code> supports full Condition Syntax. </p>
<p> The <code>&lt;depends&gt;</code> parameter accepts a semicolon-separated list of conditions. CMake 3.21 and lower evaluates each <code>condition</code> as <code>if(${condition})</code>, which does not properly handle conditions with nested paren groups. CMake 3.22 and above instead prefer to evaluate each <code>condition</code> as <code>if(&lt;condition&gt;)</code>, where <code>&lt;condition&gt;</code> is re-parsed as if literally written in a call to <code>if()</code>. This allows expressions like: </p>
<pre>&quot;A AND (B OR C)&quot;</pre>
<p>but requires expressions like: </p>
<pre>&quot;FOO MATCHES (UPPER|lower)&quot;</pre>
<p>to be re-written as: </p>
<pre>&quot;FOO MATCHES \&quot;(UPPER|lower)\&quot;&quot;</pre>
<p>Policy <code>CMP0127</code> provides compatibility for projects that have not been updated to expect the new behavior. </p>
<p> This policy was introduced in CMake version 3.22. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 3.21</h2>
<h3>Cmp0126</h3>
<p>New in version 3.21. </p>
<p> When this policy is set to <code>NEW</code>, the <code>set(CACHE)</code> command does not remove any normal variable of the same name from the current scope. The <code>OLD</code> behavior removes any normal variable of the same name from the current scope in the following situations:</p>
<dl>
<dt>&bull;</p>
<dd>No cache variable of that name existed previously.</p>
<dt>&bull;</p>
<dd>A cache variable of that name existed previously, but it had no type. This can occur when the variable was set on the command line using a form like <code>cmake -DMYVAR=blah</code> instead of <code>cmake -DMYVAR:STRING=blah</code>. </p>
<p> Note that the <code>NEW</code> behavior has an important difference to the similar <code>NEW</code> behavior of policy <code>CMP0077</code>. The <code>set(CACHE)</code> command always sets the cache variable if it did not exist previously, regardless of the <code>CMP0126</code> policy setting. The <code>option()</code> command will <i>not</i> set the cache variable if a non-cache variable of the same name already exists and <code>CMP0077</code> is set to <code>NEW</code>. </p>
<p> Policy <code>CMP0126</code> was introduced in CMake version 3.21. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly within a project. Use the <code>CMAKE_POLICY_DEFAULT_CMP0126</code> variable to set the policy for a third-party project in a subdirectory without modifying it. Unlike many policies, CMake version 3.22.1 does <i>not</i> warn when the policy is not set and simply uses <code>OLD</code> behavior. See documentation of the <code>CMAKE_POLICY_WARNING_CMP0126</code> variable to control the warning. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</dl>
<h3>Cmp0125</h3>
<p>New in version 3.21. </p>
<p> The <code>find_file()</code>, <code>find_path()</code>, <code>find_library()</code> and <code>find_program()</code> commands cache their result in the variable specified by their first argument. Prior to CMake 3.21, if a cache variable of that name already existed before the call but the cache variable had no type, any non-cache variable of the same name would be discarded and the cache variable was always used (see also <code>CMP0126</code> for a different but similar behavior). This contradicts the convention that a non-cache variable should take precedence over a cache variable of the same name. Such a situation can arise if a user sets a cache variable on the command line without specifying a type, such as <code>cmake -DMYVAR=blah &#8230;</code> instead of <code>cmake -DMYVAR:FILEPATH=blah</code>. </p>
<p> Related to the above, if a cache variable of the specified name already exists and it <i>does</i> have a type, the various <code>find_&#8230;()</code> commands would return that value unchanged. In particular, if it contained a relative path, it would not be converted to an absolute path in this situation. </p>
<p> When policy <code>CMP0125</code> is set to <code>OLD</code> or is unset, the behavior is as described above. When it is set to <code>NEW</code>, the behavior is as follows:</p>
<dl>
<dt>&bull;</p>
<dd>If a non-cache variable of the specified name exists when the <code>find_&#8230;()</code> command is called, its value will be used regardless of whether a cache variable of the same name already exists or not. A cache variable will not be created in this case if no such cache variable existed before. If a cache variable of the specified name did already exist, the cache will be updated to match the non-cache variable.</p>
<dt>&bull;</p>
<dd>The various <code>find&#8230;()</code> commands will always provide an absolute path in the result variable, except where a relative path provided by a cache or non-cache variable cannot be resolved to an existing path. </p>
<p> This policy was introduced in CMake version 3.21. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. Unlike many policies, CMake version 3.22.1 does <i>not</i> warn when the policy is not set and simply uses <code>OLD</code> behavior. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</dl>
<h3>Cmp0124</h3>
<p>New in version 3.21. </p>
<p> When this policy is set to <code>NEW</code>, the scope of loop variables defined by the <code>foreach()</code> command is restricted to the loop only. They will be unset at the end of the loop. </p>
<p> The <code>OLD</code> behavior for this policy still clears the loop variables at the end of the loop, but does not unset them. This leaves them as defined, but empty. </p>
<p> This policy was introduced in CMake version 3.21. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. Unlike many policies, CMake version 3.22.1 does <i>not</i> warn when the policy is not set and simply uses <code>OLD</code> behavior. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0123</h3>
<p>New in version 3.21. </p>
<p> <code>ARMClang</code> cpu/arch compile and link flags must be set explicitly. </p>
<p> CMake 3.20 and lower automatically maps the <code>CMAKE_SYSTEM_PROCESSOR</code> variable and an undocumented <code>CMAKE_SYSTEM_ARCH</code> to compile and link options for <code>ARMClang</code>. For example, the <code>-mcpu=cortex-m33</code> flag is added when <code>CMAKE_SYSTEM_PROCESSOR</code> equals <code>cortex-m33</code>. CMake requires projects to set either variable or it raises a fatal error. However, the project may need to additionally specify CPU features using e.g. <code>-mcpu=cortex-m33+nodsp</code>, conflicting with the <code>-mcpu=cortex-m33</code> added by CMake. This results in either link errors or unusable binaries. </p>
<p> CMake 3.21 and above prefer instead to not add any cpu/arch compile and link flags automatically. Instead, projects must specify them explicitly. This policy provides compatibility for projects that have not been updated. </p>
<p> The <code>OLD</code> behavior of this policy requires projects that use <code>ARMClang</code> to set either <code>CMAKE_SYSTEM_PROCESSOR</code> or <code>CMAKE_SYSTEM_ARCH</code> and it automatically adds a compile option <code>-mcpu=</code> or <code>-march=</code> and a link option <code>&#8211;cpu=</code> based on those variables. The <code>NEW</code> behavior does not add compile or link options, and projects are responsible for setting correct options. </p>
<p> This policy was introduced in CMake version 3.21. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0122</h3>
<p>New in version 3.21. </p>
<p> <code>UseSWIG</code> use library name conventions for <code>CSharp</code> language. </p>
<p> Starting with CMake 3.21, <code>UseSWIG</code> generates now a library using default naming conventions. This policy provides compatibility with projects that expect the legacy behavior. </p>
<p> This policy was introduced in CMake version 3.21. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0121</h3>
<p>New in version 3.21. </p>
<p> The <code>list()</code> command now detects invalid indices. </p>
<p> Prior to CMake version 3.21, the <code>list()</code> command&#8217;s <code>GET</code>, <code>INSERT</code>, <code>SUBLIST</code>, and <code>REMOVE_AT</code> subcommands did not detect invalid index arguments. </p>
<p> The <code>OLD</code> behavior of this policy is for invalid indices to be treated as their integer value (if any) at the start of the string. For example, <code>2good4you</code> is a <code>2</code> and <code>not_an_integer</code> is a <code>0</code>. The <code>NEW</code> behavior is for invalid indices to trigger an error. </p>
<p> This policy was introduced in CMake version 3.21. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 3.20</h2>
<h3>Cmp0120</h3>
<p>New in version 3.20. </p>
<p> The <code>WriteCompilerDetectionHeader</code> module is removed. </p>
<p> CMake versions 3.1 through 3.19 provide this module to generate a C++ compatibility layer by re-using information from CMake&#8217;s table of preprocessor checks for <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code>. However:</p>
<dl>
<dt>&bull;</p>
<dd>Those granular features have been superseded by meta-features for Requiring Language Standards such as <code>cxx_std_11</code>. Therefore no new granular feature checks will be added and projects will need to use other means to conditionally use new C++ features.</p>
<dt>&bull;</p>
<dd>The module exposes some of CMake&#8217;s implementation details directly to C++ translation units.</p>
<dt>&bull;</p>
<dd>The module&#8217;s approach effectively provides a header file with CMake, thus tying the version of the header to the version of CMake. Many projects found that the <code>WriteCompilerDetectionHeader</code> was best used by manually generating its header locally with a recent version of CMake and then bundling it with the project source so that it could be used with older CMake versions. </p>
<p> For reasons including the above, CMake 3.20 and above prefer to not provide the <code>WriteCompilerDetectionHeader</code> module. This policy provides compatibility for projects that have not been ported away from it. Projects using the module should be updated to stop using it. Alternatives include:</p>
<dt>&bull;</p>
<dd>Bundle a copy of the generated header in the project&#8217;s source.</p>
<dt>&bull;</p>
<dd>Use a third-party alternative, such as the CC0-licensed <i>Hedley</i>.</p>
<dt>&bull;</p>
<dd>Drop support for compilers too old to provide the features natively. </p>
<p> The <code>OLD</code> behavior of this policy is for inclusion of the deprecated <code>WriteCompilerDetectionHeader</code> module to work. The <code>NEW</code> behavior is for inclusion of the module to fail as if it does not exist. </p>
<p> This policy was introduced in CMake version 3.20. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</dl>
<h3>Cmp0119</h3>
<p>New in version 3.20. </p>
<p> <code>LANGUAGE</code> source file property explicitly compiles as specified language. </p>
<p> The <code>LANGUAGE</code> source file property is documented to mean that the source file is written in the specified language. In CMake 3.19 and below, setting this property causes CMake to compile the source file using the compiler for the specified language. However, it only passes an explicit flag to tell the compiler to treat the source as the specified language for MSVC-like, XL, and Embarcadero compilers for the <code>CXX</code> language. CMake 3.20 and above prefer to also explicitly tell the compiler to use the specified language using a flag such as <code>-x c</code> on all compilers for which such flags are known. </p>
<p> This policy provides compatibility for projects that have not been updated to expect this behavior. For example, some projects were setting the <code>LANGUAGE</code> property to <code>C</code> on assembly-language <code>.S</code> source files in order to compile them using the C compiler. Such projects should be updated to use <code>enable_language(ASM)</code>, for which CMake will often choose the C compiler as the assembler on relevant platforms anyway. </p>
<p> The <code>OLD</code> behavior for this policy is to interpret the <code>LANGUAGE &lt;LANG&gt;</code> property using its undocumented meaning to &quot;use the <code>&lt;LANG&gt;</code> compiler&quot;. The <code>NEW</code> behavior for this policy is to interpret the <code>LANGUAGE &lt;LANG&gt;</code> property using its documented meaning to &quot;compile as a <code>&lt;LANG&gt;</code> source&quot;. </p>
<p> This policy was introduced in CMake version 3.20. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. Unlike many policies, CMake version 3.22.1 does <i>not</i> warn when this policy is not set and simply uses <code>OLD</code> behavior. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0118</h3>
<p>New in version 3.20. </p>
<p> The <code>GENERATED</code> source file property is now visible in all directories. </p>
<p> Whether or not a source file is generated is an all-or-nothing global property of the source. Consequently, the associated <code>GENERATED</code> property is now visible from any directory scope, not only from the scope for which it was set. </p>
<p> Additionally, the <code>GENERATED</code> property may now be set only to boolean values, and may not be turned off once turned on. </p>
<p> The <code>OLD</code> behavior of this policy is to only allow <code>GENERATED</code> to be visible from the directory scope for which it was set. The <code>NEW</code> behavior on the other hand allows it to be visible from any scope. </p>
<p> This policy was introduced in CMake version 3.20. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. Unlike many policies, CMake version 3.22.1 does <i>not</i> warn when this policy is not set and simply uses <code>OLD</code> behavior with regard to visibility of the <code>GENERATED</code> property. However, CMake does warn about setting the <code>GENERATED</code> property to a non-boolean value.</p>
<h3>Cmp0117</h3>
<p>New in version 3.20. </p>
<p> MSVC RTTI flag <code>/GR</code> is not added to <code>CMAKE_CXX_FLAGS</code> by default. </p>
<p> When using MSVC-like compilers in CMake 3.19 and below, the RTTI flag <code>/GR</code> is added to <code>CMAKE_CXX_FLAGS</code> by default. This behavior is left from support for MSVC versions from Visual Studio 2003 and below that did not enable RTTI by default. It is no longer necessary. Furthermore, it is problematic for projects that want to change to <code>/GR-</code> programmatically. In particular, it requires string editing of the <code>CMAKE_CXX_FLAGS</code> variable with knowledge of the CMake builtin default so it can be replaced. </p>
<p> CMake 3.20 and above prefer to leave out <code>/GR</code> from the value of <code>CMAKE_CXX_FLAGS</code> by default. </p>
<p> This policy provides compatibility with projects that have not been updated to expect the lack of the <code>/GR</code> flag. The policy setting takes effect as of the first <code>project()</code> or <code>enable_language()</code> command that initializes <code>CMAKE_CXX_FLAGS</code>. </p>
<p> <code>NOTE:</code> Once the policy has taken effect at the top of a project for a given language, that choice must be used throughout the tree for that language. In projects that have nested projects in subdirectories, be sure to convert everything together. </p>
<p> The <code>OLD</code> behavior for this policy is to place the MSVC <code>/GR</code> flag in the default <code>CMAKE_CXX_FLAGS</code> cache entry. The <code>NEW</code> behavior for this policy is to <i>not</i> place the MSVC <code>/GR</code> flag in the default cache entry. </p>
<p> This policy was introduced in CMake version 3.20. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. Unlike many policies, CMake version 3.22.1 does <i>not</i> warn when this policy is not set and simply uses <code>OLD</code> behavior. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0116</h3>
<p>New in version 3.20. </p>
<p> Ninja generators transform <code>DEPFILE</code> s from <code>add_custom_command()</code>. </p>
<p> In CMake 3.19 and below, files given to the <code>DEPFILE</code> argument of <code>add_custom_command()</code> were passed directly to Ninja&#8217;s <code>depfile</code> variable without any path resolution. This meant that if <code>add_custom_command()</code> was called from a subdirectory (created by <code>add_subdirectory()</code>), the <code>DEPFILE</code> argument would have to be either an absolute path or a path relative to <code>CMAKE_BINARY_DIR</code>, rather than <code>CMAKE_CURRENT_BINARY_DIR</code>. In addition, no transformation was done on the file listed in <code>DEPFILE</code>, which meant that the paths within the <code>DEPFILE</code> had the same restrictions. </p>
<p> Starting with CMake 3.20, the <code>DEPFILE</code> argument is relative to <code>CMAKE_CURRENT_BINARY_DIR</code> (unless it is absolute), and the paths in the <code>DEPFILE</code> are also relative to <code>CMAKE_CURRENT_BINARY_DIR</code>. CMake automatically transforms the paths in the <code>DEPFILE</code> (unless they are absolute) after the custom command is run. The file listed in <code>DEPFILE</code> is not modified in any way. Instead, CMake writes the transformation to its own internal file, and passes this internal file to Ninja&#8217;s <code>depfile</code> variable. This transformation happens regardless of whether or not <code>DEPFILE</code> is relative, and regardless of whether or not <code>add_custom_command()</code> is called from a subdirectory. </p>
<p> The <code>OLD</code> behavior for this policy is to pass the <code>DEPFILE</code> to Ninja unaltered. The <code>NEW</code> behavior for this policy is to transform the <code>DEPFILE</code> after running the custom command. The status of <code>CMP0116</code> is recorded at the time of the custom command&#8217;s creation, and you can have custom commands in the same directory with different values for <code>CMP0116</code> by setting the policy before each custom command. </p>
<p> This policy was introduced in CMake version 3.20. Unlike most policies, CMake version 3.22.1 does <i>not</i> warn by default when this policy is not set (unless <code>DEPFILE</code> is used in a subdirectory) and simply uses <code>OLD</code> behavior. See documentation of the <code>CMAKE_POLICY_WARNING_CMP0116</code> variable to control the warning.</p>
<h3>Cmp0115</h3>
<p>New in version 3.20. </p>
<p> Source file extensions must be explicit. </p>
<p> In CMake 3.19 and below, if a source file could not be found by the name specified, it would append a list of known extensions to the name to see if the file with the extension could be found. For example, this would allow the user to run: </p>
<pre>add_executable(exe main)</pre>
<p>and put <code>main.c</code> in the executable without specifying the extension. </p>
<p> Starting in CMake 3.20, CMake prefers all source files to have their extensions explicitly listed: </p>
<pre>add_executable(exe main.c)</pre>
<p>The <code>OLD</code> behavior for this policy is to implicitly append known extensions to source files if they can&#8217;t be found. The <code>NEW</code> behavior of this policy is to not append known extensions and require them to be explicit. </p>
<p> This policy was introduced in CMake version 3.20. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 3.19</h2>
<h3>Cmp0114</h3>
<p>New in version 3.19. </p>
<p> <code>ExternalProject</code> step targets fully adopt their steps. </p>
<p> The <code>ExternalProject_Add()</code> <code>STEP_TARGETS</code> option, and the <code>ExternalProject_Add_StepTargets()</code> function, can be used to create build targets for individual steps of an external project. </p>
<p> In CMake 3.18 and below, step targets have some limitations:</p>
<dl>
<dt>&bull;</p>
<dd>Step targets always depend on targets named by the <code>ExternalProject_Add()</code> <code>DEPENDS</code> option even though not all steps need them. In order to allow step targets to be created without those dependencies, the <code>ExternalProject_Add()</code> <code>INDEPENDENT_STEP_TARGETS</code> option or the <code>ExternalProject_Add_StepTargets()</code> <code>NO_DEPENDS</code> option may be used. However, adding such &quot;independent&quot; step targets makes sense only for specific steps such as <code>download</code>, <code>update</code>, and <code>patch</code> because they do not need any of the external project&#8217;s build dependencies. Furthermore, it does not make sense to create independent step targets for steps that depend on non-independent steps. Such rules are not enforced, and projects that do not follow them can generate build systems with confusing and generator-specific behavior.</p>
<dt>&bull;</p>
<dd>Step targets hold copies of the custom commands implementing their steps that are separate from the copies in the primary target created by <code>ExternalProject_Add()</code>, and the primary target does not depend on the step targets. In parallel builds that drive the primary target and step targets concurrently, multiple copies of the steps&#8217; commands may run concurrently and race each other. </p>
<p> Also, prior to policy <code>CMP0113</code>, the step targets generated by Makefile Generators also contain all the custom commands on which their step depends. This can lead to repeated execution of those steps even in serial builds. </p>
<p> In CMake 3.19 and above, the <code>ExternalProject</code> module prefers a revised design to address these problems:</p>
<dt>&bull;</p>
<dd>Each step is classified as &quot;independent&quot; if it does not depend on other targets named by the <code>ExternalProject_Add()</code> <code>DEPENDS</code>. The predefined steps are automatically classified by default:</p>
<dt>&bull;</p>
<dd>The <code>download</code>, <code>update</code>, and <code>patch</code> steps are independent.</p>
<dt>&bull;</p>
<dd>The <code>configure</code>, <code>build</code>, <code>test</code>, and <code>install</code> steps are not. </p>
<p> For custom steps, the <code>ExternalProject_Add_Step()</code> command provides an <code>INDEPENDENT</code> option to mark them as independent. It is an error to mark a step as independent if it depends on other steps that are not. Note that this use of the term &quot;independent&quot; refers only to independence from external targets and is orthogonal to a step&#8217;s dependencies on other steps.</p>
<dt>&bull;</p>
<dd>Step targets created by the <code>ExternalProject_Add()</code> <code>STEP_TARGETS</code> option or the <code>ExternalProject_Add_Step()</code> function are now independent if and only if their steps are marked as independent. The <code>ExternalProject_Add()</code> <code>INDEPENDENT_STEP_TARGETS</code> option and <code>ExternalProject_Add_StepTargets()</code> <code>NO_DEPENDS</code> option are no longer allowed.</p>
<dt>&bull;</p>
<dd>Step targets, when created, are fully responsible for holding the custom commands implementing their steps. The primary target created by <code>ExternalProject_Add()</code> depends on the step targets, and the step targets depend on each other. The target-level dependencies match the file-level dependencies used by the custom commands for each step. </p>
<p> When the <code>ExternalProject_Add()</code> <code>UPDATE_DISCONNECTED</code> or <code>TEST_EXCLUDE_FROM_MAIN</code> option is used, or the <code>ExternalProject_Add_Step()</code> <code>EXCLUDE_FROM_MAIN</code> option is used for a custom step, some step targets may be created automatically. These are needed to hold the steps commonly depended upon by the primary target and the disconnected step targets. </p>
<p> Policy <code>CMP0114</code> provides compatibility for projects that have not been updated to expect the new behavior. The <code>OLD</code> behavior for this policy is to use the above-documented behavior from 3.18 and below. The <code>NEW</code> behavior for this policy is to use the above-documented behavior preferred by 3.19 and above. </p>
<p> This policy was introduced in CMake version 3.19. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly.</dl>
<h3>Cmp0113</h3>
<p>New in version 3.19. </p>
<p> Makefile Generators do not repeat custom commands from target dependencies. </p>
<p> Consider a chain of custom commands split across two dependent targets: </p>
<pre>add_custom_command(OUTPUT output-not-created
 COMMAND ... DEPENDS ...)
set_property(SOURCE output-not-created PROPERTY SYMBOLIC 1)
add_custom_command(OUTPUT output-created
 COMMAND ... DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/output-not-created)
add_custom_target(first DEPENDS output-not-created)
add_custom_target(second DEPENDS output-created)
add_dependencies(second first)</pre>
<p>In CMake 3.18 and lower, the Makefile generators put a copy of both custom commands in the Makefile for target <code>second</code> even though its dependency on target <code>first</code> ensures that the first custom command runs before the second. Running <code>make second</code> would cause the first custom command to run once in the <code>first</code> target and then again in the <code>second</code> target. </p>
<p> CMake 3.19 and above prefer to not duplicate custom commands in a target that are already generated in other targets on which the target depends (directly or indirectly). This policy provides compatibility for projects that have not been updated to expect the new behavior. In particular, projects that relied on the duplicate execution or that did not properly set the <code>SYMBOLIC</code> source file property may be affected. </p>
<p> The <code>OLD</code> behavior for this policy is to duplicate custom commands in dependent targets. The <code>NEW</code> behavior of this policy is to not duplicate custom commands in dependent targets. </p>
<p> This policy was introduced in CMake version 3.19. Unlike many policies, CMake version 3.22.1 does <i>not</i> warn when this policy is not set and simply uses <code>OLD</code> behavior. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0112</h3>
<p>New in version 3.19. </p>
<p> Target file component generator expressions do not add target dependencies. </p>
<p> The following target-based generator expressions that query for directory or file name components no longer add a dependency on the evaluated target.</p>
<dl>
<dt>&bull;</p>
<dd><code>TARGET_FILE_NAME</code></p>
<dt>&bull;</p>
<dd><code>TARGET_FILE_DIR</code></p>
<dt>&bull;</p>
<dd><code>TARGET_LINKER_FILE_BASE_NAME</code></p>
<dt>&bull;</p>
<dd><code>TARGET_LINKER_FILE_NAME</code></p>
<dt>&bull;</p>
<dd><code>TARGET_LINKER_FILE_DIR</code></p>
<dt>&bull;</p>
<dd><code>TARGET_SONAME_FILE_NAME</code></p>
<dt>&bull;</p>
<dd><code>TARGET_SONAME_FILE_DIR</code></p>
<dt>&bull;</p>
<dd><code>TARGET_PDB_FILE_NAME</code></p>
<dt>&bull;</p>
<dd><code>TARGET_PDB_FILE_DIR</code></p>
<dt>&bull;</p>
<dd><code>TARGET_BUNDLE_DIR</code></p>
<dt>&bull;</p>
<dd><code>TARGET_BUNDLE_CONTENT_DIR</code> </p>
<p> In CMake 3.18 and lower a dependency on the evaluated target of the above generator expressions would always be added. CMake 3.19 and above prefer to not add this dependency. This policy provides compatibility for projects that have not been updated to expect the new behavior. </p>
<p> The <code>OLD</code> behavior for this policy is to add a dependency on the evaluated target for the above generator expressions. The <code>NEW</code> behavior of this policy is to not add a dependency on the evaluated target for the above generator expressions. </p>
<p> This policy was introduced in CMake version 3.19. Unlike many policies, CMake version 3.22.1 does <i>not</i> warn by default when this policy is not set and simply uses <code>OLD</code> behavior. See documentation of the <code>CMAKE_POLICY_WARNING_CMP0112</code> variable to control the warning. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</dl>
<h3>Cmp0111</h3>
<p>New in version 3.19. </p>
<p> An imported target missing its location property fails during generation. </p>
<p> Imported Targets for library files and executables require that their location on disk is specified in a target property such as <code>IMPORTED_LOCATION</code>, <code>IMPORTED_IMPLIB</code>, or a per-configuration equivalent. If a needed location property is not set, CMake 3.18 and below generate the string <code>&lt;TARGET_NAME&gt;-NOTFOUND</code> in its place, which results in failures of the corresponding rules at build time. CMake 3.19 and above prefer instead to raise an error during generation. This policy provides compatibility for projects that have not been updated to expect the new behavior. </p>
<p> The <code>OLD</code> behavior of this policy is to generate the location of an imported unknown, static or shared library target as <code>&lt;TARGET_NAME&gt;-NOTFOUND</code> if not set. The <code>NEW</code> behavior is to raise an error. </p>
<p> This policy was introduced in CMake version 3.19. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0110</h3>
<p>New in version 3.19. </p>
<p> <code>add_test()</code> supports arbitrary characters in test names. </p>
<p> <code>add_test()</code> can now (officially) create tests with whitespace and other special characters in its name. Before CMake version 3.19 that was not allowed, however, it was possible to work around this limitation by explicitly putting escaped quotes around the test&#8217;s name in the <code>add_test</code> command. </p>
<p> Although never officially supported several projects in the wild found and implemented this workaround. However, the new change which officially allows the <code>add_test</code> command to support whitespace and other special characters in test names now breaks that workaround. In order for these projects to work smoothly with newer CMake versions, this policy was introduced. </p>
<p> The <code>OLD</code> behavior of this policy is to still prevent <code>add_test</code> from handling whitespace and special characters properly (if not using the mentioned workaround). The <code>NEW</code> behavior on the other hand allows names with whitespace and special characters for tests created by <code>add_test</code>. </p>
<p> This policy was introduced in CMake version 3.19. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly.</p>
<h3>Cmp0109</h3>
<p>New in version 3.19. </p>
<p> <code>find_program()</code> requires permission to execute but not to read. </p>
<p> In CMake 3.18 and below, the <code>find_program()</code> command on UNIX would find files that are readable without requiring execute permission, and would not find files that are executable without read permission. In CMake 3.19 and above, <code>find_program</code> now prefers to require execute permission but not read permission. This policy provides compatibility with projects that have not been updated to expect the new behavior. </p>
<p> The <code>OLD</code> behavior for this policy is for <code>find_program</code> to require read permission but not execute permission. The <code>NEW</code> behavior for this policy is for <code>find_program</code> to require execute permission but not read permission. </p>
<p> This policy was introduced in CMake version 3.19. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 3.18</h2>
<h3>Cmp0108</h3>
<p>New in version 3.18. </p>
<p> A target is not allowed to link to itself even through an <code>ALIAS</code> target. </p>
<p> In CMake 3.17 and below, a target can link to a target aliased to itself. </p>
<p> The <code>OLD</code> behavior for this policy is to allow a target to link to a target aliased to itself. </p>
<p> The <code>NEW</code> behavior of this policy is to prevent a target to link to itself through an <code>ALIAS</code> target. </p>
<p> This policy was introduced in CMake version 3.17. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. Unlike many policies, CMake version 3.22.1 does <i>not</i> warn when this policy is not set and simply uses <code>OLD</code> behavior. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0107</h3>
<p>New in version 3.18. </p>
<p> It is not allowed to create an <code>ALIAS</code> target with the same name as an another target. </p>
<p> In CMake 3.17 and below, an <code>ALIAS</code> target can overwrite silently an existing target with the same name. </p>
<p> The <code>OLD</code> behavior for this policy is to allow target overwrite. </p>
<p> The <code>NEW</code> behavior of this policy is to prevent target overwriting. </p>
<p> This policy was introduced in CMake version 3.17. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. Unlike many policies, CMake version 3.22.1 does <i>not</i> warn when this policy is not set and simply uses <code>OLD</code> behavior. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0106</h3>
<p>New in version 3.18. </p>
<p> The <code>Documentation</code> module is removed. </p>
<p> The <code>Documentation</code> was added as a support mechanism for the VTK project and was tuned for that project. Instead of CMake providing this module with (now old) VTK patterns for cache variables and required packages, the module is now deprecated by CMake itself. </p>
<p> The <code>OLD</code> behavior of this policy is for <code>Documentation</code> to add cache variables and find VTK documentation dependent packages. The <code>NEW</code> behavior is to act as an empty module. </p>
<p> This policy was introduced in CMake version 3.18. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0105</h3>
<p>New in version 3.18. </p>
<p> <code>LINK_OPTIONS</code> and <code>INTERFACE_LINK_OPTIONS</code> target properties are now used for the device link step. </p>
<p> In CMake 3.17 and below, link options are not used by the device link step. </p>
<p> The <code>OLD</code> behavior for this policy is to ignore the link options. </p>
<p> The <code>NEW</code> behavior of this policy is to use the link options during the device link step. </p>
<p> This policy was introduced in CMake version 3.17. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. Unlike many policies, CMake version 3.22.1 does <i>not</i> warn when this policy is not set and simply uses <code>OLD</code> behavior. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0104</h3>
<p>New in version 3.18. </p>
<p> Initialize <code>CMAKE_CUDA_ARCHITECTURES</code> when <code>CMAKE_CUDA_COMPILER_ID</code> is <code>NVIDIA</code>. Raise an error if <code>CUDA_ARCHITECTURES</code> is empty. </p>
<p> <code>CMAKE_CUDA_ARCHITECTURES</code> introduced in CMake 3.18 is used to initialize <code>CUDA_ARCHITECTURES</code>, which passes correct code generation flags to the CUDA compiler. </p>
<p> Previous to this users had to manually specify the code generation flags. This policy is for backwards compatibility with manually specifying code generation flags. </p>
<p> The <code>OLD</code> behavior for this policy is to not initialize <code>CMAKE_CUDA_ARCHITECTURES</code> when <code>CMAKE_CUDA_COMPILER_ID</code> is <code>NVIDIA</code>. Empty <code>CUDA_ARCHITECTURES</code> is allowed. </p>
<p> The <code>NEW</code> behavior of this policy is to initialize <code>CMAKE_CUDA_ARCHITECTURES</code> when <code>CMAKE_CUDA_COMPILER_ID</code> is <code>NVIDIA</code> and raise an error if <code>CUDA_ARCHITECTURES</code> is empty during generation. </p>
<p> If <code>CUDA_ARCHITECTURES</code> is set to a false value no architectures flags are passed to the compiler. This is intended to support packagers and the rare cases where full control over the passed flags is required. </p>
<p> This policy was introduced in CMake version 3.18. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Examples</h3>
<pre>set_target_properties(tgt PROPERTIES CUDA_ARCHITECTURES &quot;35;50;72&quot;)</pre>
<p>Generates code for real and virtual architectures <code>30</code>, <code>50</code> and <code>72</code>. </p>
<pre>set_property(TARGET tgt PROPERTY CUDA_ARCHITECTURES 70-real 72-virtual)</pre>
<p>Generates code for real architecture <code>70</code> and virtual architecture <code>72</code>. </p>
<pre>set_property(TARGET tgt PROPERTY CUDA_ARCHITECTURES OFF)</pre>
<p>CMake will not pass any architecture flags to the compiler.</p>
<h3>Cmp0103</h3>
<p>New in version 3.18. </p>
<p> Multiple calls to <code>export()</code> command with same <code>FILE</code> without <code>APPEND</code> is no longer allowed. </p>
<p> In CMake 3.17 and below, multiple calls to <code>export()</code> command with the same <code>FILE</code> without <code>APPEND</code> are accepted silently but only the last occurrence is taken into account during the generation.</p>
<dl>
<dt><code>The OLD</code> behavior for this policy is to ignore the multiple occurrences of</p>
<dd><code>export()</code> command except the last one. </p>
<p> The <code>NEW</code> behavior of this policy is to raise an error on second call to <code>export()</code> command with same <code>FILE</code> without <code>APPEND</code>. </p>
<p> This policy was introduced in CMake version 3.18. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</dl>
<h2>Policies Introduced By Cmake 3.17</h2>
<h3>Cmp0102</h3>
<p>New in version 3.17. </p>
<p> The <code>mark_as_advanced()</code> command no longer creates a cache entry if one does not already exist. </p>
<p> In CMake 3.16 and below, if a variable was not defined at all or just defined locally, the <code>mark_as_advanced()</code> command would create a new cache entry with an <code>UNINITIALIZED</code> type and no value. When a <code>find_path()</code> (or other similar <code>find_</code> command) would next run, it would find this undefined cache entry and set it up with an empty string value. This process would end up deleting the local variable in the process (due to the way the cache works), effectively clearing any stored <code>find_</code> results that were only available in the local scope. </p>
<p> The <code>OLD</code> behavior for this policy is to create the empty cache definition. The <code>NEW</code> behavior of this policy is to ignore variables which do not already exist in the cache. </p>
<p> This policy was introduced in CMake version 3.17. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. Unlike many policies, CMake version 3.22.1 does <i>not</i> warn when this policy is not set and simply uses <code>OLD</code> behavior. See documentation of the <code>CMAKE_POLICY_WARNING_CMP0102</code> variable to control the warning. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0101</h3>
<p>New in version 3.17. </p>
<p> <code>target_compile_options()</code> now honors <code>BEFORE</code> keyword in all scopes. </p>
<p> In CMake 3.16 and below the <code>target_compile_options()</code> ignores the <code>BEFORE</code> keyword in private scope. CMake 3.17 and later honors <code>BEFORE</code> keyword in all scopes. This policy provides compatibility for projects that have not been updated to expect the new behavior. </p>
<p> The <code>OLD</code> behavior for this policy is to not honor <code>BEFORE</code> keyword in private scope. The <code>NEW</code> behavior of this policy is to honor <code>BEFORE</code> keyword in all scopes. </p>
<p> This policy was introduced in CMake version 3.17. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. Unlike many policies, CMake version 3.22.1 does <i>not</i> warn when this policy is not set and simply uses <code>OLD</code> behavior. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0100</h3>
<p>New in version 3.17. </p>
<p> Let <code>AUTOMOC</code> and <code>AUTOUIC</code> process header files that end with a <code>.hh</code> extension. </p>
<p> Since version 3.17, CMake processes header files that end with a <code>.hh</code> extension in <code>AUTOMOC</code> and <code>AUTOUIC</code>. In earlier CMake versions, these header files were ignored by <code>AUTOMOC</code> and <code>AUTOUIC</code>. </p>
<p> This policy affects how header files that end with a <code>.hh</code> extension get treated in <code>AUTOMOC</code> and <code>AUTOUIC</code>. </p>
<p> The <code>OLD</code> behavior for this policy is to ignore <code>.hh</code> header files in <code>AUTOMOC</code> and <code>AUTOUIC</code>. </p>
<p> The <code>NEW</code> behavior for this policy is to process <code>.hh</code> header files in <code>AUTOMOC</code> and <code>AUTOUIC</code> just like other header files. </p>
<p> <code>NOTE:</code> To silence the <code>CMP0100</code> warning source files can be excluded from <code>AUTOMOC</code> and <code>AUTOUIC</code> processing by setting the source file properties <code>SKIP_AUTOMOC</code>, <code>SKIP_AUTOUIC</code> or <code>SKIP_AUTOGEN</code>. </p>
<pre># Source skip example:
set_property(SOURCE /path/to/file1.hh PROPERTY SKIP_AUTOMOC ON)
set_property(SOURCE /path/to/file2.hh PROPERTY SKIP_AUTOUIC ON)
set_property(SOURCE /path/to/file3.hh PROPERTY SKIP_AUTOGEN ON)</pre>
<p>This policy was introduced in CMake version 3.17.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0099</h3>
<p>New in version 3.17. </p>
<p> Target link properties <code>INTERFACE_LINK_OPTIONS</code>, <code>INTERFACE_LINK_DIRECTORIES</code> and <code>INTERFACE_LINK_DEPENDS</code> are now transitive over private dependencies of static libraries. </p>
<p> In CMake 3.16 and below the interface link properties attached to libraries are not propagated for private dependencies of static libraries. Only the libraries themselves are propagated to link the dependent binary. CMake 3.17 and later prefer to propagate all interface link properties. This policy provides compatibility for projects that have not been updated to expect the new behavior. </p>
<p> The <code>OLD</code> behavior for this policy is to not propagate interface link properties. The <code>NEW</code> behavior of this policy is to propagate interface link properties. </p>
<p> This policy was introduced in CMake version 3.17. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. Unlike many policies, CMake version 3.22.1 does <i>not</i> warn when this policy is not set and simply uses <code>OLD</code> behavior. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0098</h3>
<p>New in version 3.17. </p>
<p> <code>FindFLEX</code> runs <code>flex</code> in directory <code>CMAKE_CURRENT_BINARY_DIR</code> when executing. </p>
<p> The module provides a <code>FLEX_TARGET</code> macro which generates FLEX output. In CMake 3.16 and below the macro would generate a custom command that runs <code>flex</code> in the current source directory. CMake 3.17 and later prefer to run it in the build directory and use <code>CMAKE_CURRENT_BINARY_DIR</code> as the <code>WORKING_DIRECTORY</code> of its <code>add_custom_command()</code> invocation. This ensures that any implicitly generated file is written relative to the build tree rather than the source tree, unless the generated file is provided as absolute path. </p>
<p> This policy provides compatibility for projects that have not been updated to expect the new behavior. </p>
<p> The <code>OLD</code> behavior for this policy is for <code>FLEX_TARGET</code> to use the current source directory for the <code>WORKING_DIRECTORY</code> and where to generate implicit files. The <code>NEW</code> behavior of this policy is to use the current binary directory for the <code>WORKING_DIRECTORY</code> relative to which implicit files are generated unless provided as absolute path. </p>
<p> This policy was introduced in CMake version 3.17. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. Unlike many policies, CMake version 3.22.1 does <i>not</i> warn when this policy is not set and simply uses <code>OLD</code> behavior. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 3.16</h2>
<h3>Cmp0097</h3>
<p>New in version 3.16. </p>
<p> <code>ExternalProject_Add()</code> with <code>GIT_SUBMODULES &quot;&quot;</code> initializes no submodules. </p>
<p> The module provides a <code>GIT_SUBMODULES</code> option which controls what submodules to initialize and update. Starting with CMake 3.16, explicitly setting <code>GIT_SUBMODULES</code> to an empty string means no submodules will be initialized or updated. </p>
<p> This policy provides compatibility for projects that have not been updated to expect the new behavior. </p>
<p> The <code>OLD</code> behavior for this policy is for <code>GIT_SUBMODULES</code> when set to an empty string to initialize and update all git submodules. The <code>NEW</code> behavior for this policy is for <code>GIT_SUBMODULES</code> when set to an empty string to initialize and update no git submodules. </p>
<p> This policy was introduced in CMake version 3.16. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. Unlike most policies, CMake version 3.22.1 does <i>not</i> warn when this policy is not set and simply uses <code>OLD</code> behavior.</p>
<h3>Cmp0096</h3>
<p>New in version 3.16. </p>
<p> The <code>project()</code> command preserves leading zeros in version components. </p>
<p> When a <code>VERSION &lt;major&gt;[.&lt;minor&gt;[.&lt;patch&gt;[.&lt;tweak&gt;]]]]</code> argument is given to the <code>project()</code> command, it stores the version string in the <code>PROJECT_VERSION</code> variable and stores individual integer version components in <code>PROJECT_VERSION_{MAJOR,MINOR,PATCH,TWEAK}</code> variables (see policy <code>CMP0048</code>). CMake 3.15 and below dropped leading zeros from each component. CMake 3.16 and higher prefer to preserve leading zeros. This policy provides compatibility for projects that have not been updated to expect the new behavior. </p>
<p> The <code>OLD</code> behavior of this policy drops leading zeros in all components, e.g. such that version <code>1.07.06</code> becomes <code>1.7.6</code>. The <code>NEW</code> behavior of this policy preserves the leading zeros in all components, such that version <code>1.07.06</code> remains unchanged. </p>
<p> This policy was introduced in CMake version 3.16. Unlike many policies, CMake version 3.22.1 does <i>not</i> warn when this policy is not set and simply uses the <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0095</h3>
<p>New in version 3.16. </p>
<p> <code>RPATH</code> entries are properly escaped in the intermediary CMake install script. </p>
<p> In CMake 3.15 and earlier, <code>RPATH</code> entries set via <code>CMAKE_INSTALL_RPATH</code> or via <code>INSTALL_RPATH</code> have not been escaped before being inserted into the <code>cmake_install.cmake</code> script. Dynamic linkers on ELF-based systems (e.g. Linux and FreeBSD) allow certain keywords in <code>RPATH</code> entries, such as <code>${ORIGIN}</code> (More details are available in the <code>ld.so</code> man pages on those systems). The syntax of these keywords can match CMake&#8217;s variable syntax. In order to not be substituted (usually to an empty string) already by the intermediary <code>cmake_install.cmake</code> script, the user had to double-escape such <code>RPATH</code> keywords, e.g. <code>set(CMAKE_INSTALL_RPATH &quot;\\${ORIGIN}/../lib&quot;)</code>. Since the intermediary <code>cmake_install.cmake</code> script is an implementation detail of CMake, CMake 3.16 and later will make sure <code>RPATH</code> entries are inserted literally by escaping any coincidental CMake syntax. </p>
<p> The <code>OLD</code> behavior of this policy is to not escape <code>RPATH</code> entries in the intermediary <code>cmake_install.cmake</code> script. The <code>NEW</code> behavior is to properly escape coincidental CMake syntax in <code>RPATH</code> entries when generating the intermediary <code>cmake_install.cmake</code> script. </p>
<p> This policy was introduced in CMake version 3.16. CMake version 3.22.1 warns when the policy is not set and detected usage of CMake-like syntax and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 3.15</h2>
<h3>Cmp0094</h3>
<p>New in version 3.15. </p>
<p> Modules <code>FindPython3</code>, <code>FindPython2</code> and <code>FindPython</code> use <code>LOCATION</code> for lookup strategy. </p>
<p> Starting with CMake 3.15, Modules <code>FindPython3</code>, <code>FindPython2</code> and <code>FindPython</code> set value <code>LOCATION</code> for, respectively, variables <code>Python3_FIND_STRATEGY</code>, <code>Python2_FIND_STRATEGY</code> and <code>Python_FIND_STRATEGY</code>. This policy provides compatibility with projects that expect the legacy behavior. </p>
<p> The <code>OLD</code> behavior for this policy set value <code>VERSION</code> for variables <code>Python3_FIND_STRATEGY</code>, <code>Python2_FIND_STRATEGY</code> and <code>Python_FIND_STRATEGY</code>. </p>
<p> This policy was introduced in CMake version 3.15. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. Unlike many policies, CMake version 3.22.1 does <i>not</i> warn when this policy is not set and simply uses the <code>OLD</code> behavior. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0093</h3>
<p>New in version 3.15. </p>
<p> <code>FindBoost</code> reports <code>Boost_VERSION</code> in <code>x.y.z</code> format. </p>
<p> In CMake 3.14 and below the module would report the Boost version number as specified in the preprocessor definition <code>BOOST_VERSION</code> in the <code>boost/version.hpp</code> file. In CMake 3.15 and later it is preferred that the reported version number matches the <code>x.y.z</code> format reported by the CMake package shipped with Boost <code>1.70.0</code> and later. The macro value is still reported in the <code>Boost_VERSION_MACRO</code> variable. </p>
<p> The <code>OLD</code> behavior for this policy is for <code>FindBoost</code> to report <code>Boost_VERSION</code> as specified in the preprocessor definition <code>BOOST_VERSION</code> in <code>boost/version.hpp</code>. The <code>NEW</code> behavior for this policy is for <code>FindBoost</code> to report <code>Boost_VERSION</code> in <code>x.y.z</code> format. </p>
<p> This policy was introduced in CMake version 3.15. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. Unlike many policies, CMake version 3.22.1 does <i>not</i> warn when this policy is not set and simply uses the <code>OLD</code> behavior. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0092</h3>
<p>New in version 3.15. </p>
<p> MSVC warning flags are not in <code>CMAKE_&lt;LANG&gt;_FLAGS</code> by default. </p>
<p> When using MSVC-like compilers in CMake 3.14 and below, warning flags like <code>/W3</code> are added to <code>CMAKE_&lt;LANG&gt;_FLAGS</code> by default. This is problematic for projects that want to choose a different warning level programmatically. In particular, it requires string editing of the <code>CMAKE_&lt;LANG&gt;_FLAGS</code> variables with knowledge of the CMake builtin defaults so they can be replaced. </p>
<p> CMake 3.15 and above prefer to leave out warning flags from the value of <code>CMAKE_&lt;LANG&gt;_FLAGS</code> by default. </p>
<p> This policy provides compatibility with projects that have not been updated to expect the lack of warning flags. The policy setting takes effect as of the first <code>project()</code> or <code>enable_language()</code> command that initializes <code>CMAKE_&lt;LANG&gt;_FLAGS</code> for a given language <code>&lt;LANG&gt;</code>. </p>
<p> <code>NOTE:</code> Once the policy has taken effect at the top of a project for a given language, that choice must be used throughout the tree for that language. In projects that have nested projects in subdirectories, be sure to convert everything together. </p>
<p> The <code>OLD</code> behavior for this policy is to place MSVC warning flags in the default <code>CMAKE_&lt;LANG&gt;_FLAGS</code> cache entries. The <code>NEW</code> behavior for this policy is to <i>not</i> place MSVC warning flags in the default cache entries. </p>
<p> This policy was introduced in CMake version 3.15. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. Unlike many policies, CMake version 3.22.1 does <i>not</i> warn when this policy is not set and simply uses <code>OLD</code> behavior. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0091</h3>
<p>New in version 3.15. </p>
<p> MSVC runtime library flags are selected by an abstraction. </p>
<p> Compilers targeting the MSVC ABI have flags to select the MSVC runtime library. Runtime library selection typically varies with build configuration because there is a separate runtime library for Debug builds. </p>
<p> In CMake 3.14 and below, MSVC runtime library selection flags are added to the default <code>CMAKE_&lt;LANG&gt;_FLAGS_&lt;CONFIG&gt;</code> cache entries by CMake automatically. This allows users to edit their cache entries to adjust the flags. However, the presence of such default flags is problematic for projects that want to choose a different runtime library programmatically. In particular, it requires string editing of the <code>CMAKE_&lt;LANG&gt;_FLAGS_&lt;CONFIG&gt;</code> variables with knowledge of the CMake builtin defaults so they can be replaced. </p>
<p> CMake 3.15 and above prefer to leave the MSVC runtime library selection flags out of the default <code>CMAKE_&lt;LANG&gt;_FLAGS_&lt;CONFIG&gt;</code> values and instead offer a first-class abstraction. The <code>CMAKE_MSVC_RUNTIME_LIBRARY</code> variable and <code>MSVC_RUNTIME_LIBRARY</code> target property may be set to select the MSVC runtime library. If they are not set then CMake uses the default value <code>MultiThreaded$&lt;$&lt;CONFIG:Debug&gt;:Debug&gt;DLL</code> which is equivalent to the original flags. </p>
<p> This policy provides compatibility with projects that have not been updated to be aware of the abstraction. The policy setting takes effect as of the first <code>project()</code> or <code>enable_language()</code> command that enables a language whose compiler targets the MSVC ABI. </p>
<p> <code>NOTE:</code> Once the policy has taken effect at the top of a project, that choice must be used throughout the tree. In projects that have nested projects in subdirectories, be sure to convert everything together. </p>
<p> The <code>OLD</code> behavior for this policy is to place MSVC runtime library flags in the default <code>CMAKE_&lt;LANG&gt;_FLAGS_&lt;CONFIG&gt;</code> cache entries and ignore the <code>CMAKE_MSVC_RUNTIME_LIBRARY</code> abstraction. The <code>NEW</code> behavior for this policy is to <i>not</i> place MSVC runtime library flags in the default cache entries and use the abstraction instead. </p>
<p> This policy was introduced in CMake version 3.15. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. Unlike many policies, CMake version 3.22.1 does <i>not</i> warn when this policy is not set and simply uses <code>OLD</code> behavior. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0090</h3>
<p>New in version 3.15. </p>
<p> <code>export(PACKAGE)</code> does not populate package registry by default. </p>
<p> In CMake 3.14 and below the <code>export(PACKAGE)</code> command populated the user package registry by default and users needed to set the <code>CMAKE_EXPORT_NO_PACKAGE_REGISTRY</code> to disable it, e.g. in automated build and packaging environments. Since the user package registry is stored outside the build tree, this side effect should not be enabled by default. Therefore CMake 3.15 and above prefer that <code>export(PACKAGE)</code> does nothing unless an explicit <code>CMAKE_EXPORT_PACKAGE_REGISTRY</code> variable is set to enable it. This policy provides compatibility with projects that have not been updated. </p>
<p> The <code>OLD</code> behavior for this policy is for <code>export(PACKAGE)</code> command to populate the user package registry unless <code>CMAKE_EXPORT_NO_PACKAGE_REGISTRY</code> is enabled. The <code>NEW</code> behavior is for <code>export(PACKAGE)</code> command to do nothing unless the <code>CMAKE_EXPORT_PACKAGE_REGISTRY</code> is enabled. </p>
<p> This policy was introduced in CMake version 3.15. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. Unlike most policies, CMake version 3.22.1 does <i>not</i> warn when this policy is not set and simply uses <code>OLD</code> behavior. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0089</h3>
<p>New in version 3.15. </p>
<p> Compiler id for IBM Clang-based XL compilers is now <code>XLClang</code>. </p>
<p> CMake 3.15 and above recognize that IBM&#8217;s Clang-based XL compilers that define <code>__ibmxl__</code> are a new front-end distinct from <code>xlc</code> with a different command line and set of capabilities. CMake now prefers to present this to projects by setting the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable to <code>XLClang</code> instead of <code>XL</code>. However, existing projects may assume the compiler id for Clang-based XL is just <code>XL</code> as it was in CMake versions prior to 3.15. Therefore this policy determines for Clang-based XL compilers which compiler id to report in the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable after language <code>&lt;LANG&gt;</code> is enabled by the <code>project()</code> or <code>enable_language()</code> command. The policy must be set prior to the invocation of either command. </p>
<p> The <code>OLD</code> behavior for this policy is to use compiler id <code>XL</code>. The <code>NEW</code> behavior for this policy is to use compiler id <code>XLClang</code>. </p>
<p> This policy was introduced in CMake version 3.15. Use the <code>cmake_policy()</code> command to set this policy to <code>OLD</code> or <code>NEW</code> explicitly. Unlike most policies, CMake version 3.22.1 does <i>not</i> warn by default when this policy is not set and simply uses <code>OLD</code> behavior. See documentation of the <code>CMAKE_POLICY_WARNING_CMP0089</code> variable to control the warning. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 3.14</h2>
<h3>Cmp0088</h3>
<p>New in version 3.14. </p>
<p> <code>FindBISON</code> runs bison in <code>CMAKE_CURRENT_BINARY_DIR</code> when executing. </p>
<p> The module provides a <code>BISON_TARGET</code> macro which generates BISON output. In CMake 3.13 and below the macro would generate a custom command that runs <code>bison</code> in the source directory. CMake 3.14 and later prefer to run it in the build directory and use <code>CMAKE_CURRENT_BINARY_DIR</code> as the <code>WORKING_DIRECTORY</code> of its <code>add_custom_command()</code> invocation. This ensures that any implicitly generated file is written to the build tree rather than the source. </p>
<p> This policy provides compatibility for projects that have not been updated to expect the new behavior. </p>
<p> The <code>OLD</code> behavior for this policy is for <code>BISON_TARGET</code> to use the current source directory for the <code>WORKING_DIRECTORY</code> and where to generate implicit files. The <code>NEW</code> behavior of this policy is to use the current binary directory for the <code>WORKING_DIRECTORY</code> and where to generate implicit files. </p>
<p> This policy was introduced in CMake version 3.14. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. Unlike most policies, CMake version 3.22.1 does <i>not</i> warn when this policy is not set and simply uses <code>OLD</code> behavior. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0087</h3>
<p>New in version 3.14. </p>
<p> <code>install(CODE)</code> and <code>install(SCRIPT)</code> support generator expressions. </p>
<p> In CMake 3.13 and earlier, <code>install(CODE)</code> and <code>install(SCRIPT)</code> did not evaluate generator expressions. CMake 3.14 and later will evaluate generator expressions for <code>install(CODE)</code> and <code>install(SCRIPT)</code>. </p>
<p> The <code>OLD</code> behavior of this policy is for <code>install(CODE)</code> and <code>install(SCRIPT)</code> to not evaluate generator expressions. The <code>NEW</code> behavior is to evaluate generator expressions for <code>install(CODE)</code> and <code>install(SCRIPT)</code>. </p>
<p> Note that it is the value of this policy setting at the end of the directory scope that is important, not its setting at the time of the call to <code>install(CODE)</code> or <code>install(SCRIPT)</code>. This has implications for calling these commands from places that have their own policy scope but not their own directory scope (e.g. from files brought in via <code>include()</code> rather than <code>add_subdirectory()</code>). </p>
<p> This policy was introduced in CMake version 3.14. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0086</h3>
<p>New in version 3.14. </p>
<p> <code>UseSWIG</code> honors <code>SWIG_MODULE_NAME</code> via <code>-module</code> flag. </p>
<p> Starting with CMake 3.14, <code>UseSWIG</code> passes option <code>-module &lt;module_name&gt;</code> to <code>SWIG</code> compiler if the file property <code>SWIG_MODULE_NAME</code> is specified. This policy provides compatibility with projects that expect the legacy behavior. </p>
<p> The <code>OLD</code> behavior for this policy is to never pass <code>-module</code> option. The <code>NEW</code> behavior is to pass <code>-module</code> option to <code>SWIG</code> compiler if <code>SWIG_MODULE_NAME</code> is specified. </p>
<p> This policy was introduced in CMake version 3.14. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0085</h3>
<p>New in version 3.14. </p>
<p> <code>$&lt;IN_LIST:&#8230;&gt;</code> handles empty list items. </p>
<p> In CMake 3.13 and lower, the <code>$&lt;IN_LIST:&#8230;&gt;</code> generator expression always returned <code>0</code> if the first argument was empty, even if the list contained an empty item. This behavior is inconsistent with the <code>IN_LIST</code> behavior of <code>if()</code>, which this generator expression is meant to emulate. CMake 3.14 and later handles this case correctly. </p>
<p> The <code>OLD</code> behavior of this policy is for <code>$&lt;IN_LIST:&#8230;&gt;</code> to always return <code>0</code> if the first argument is empty. The <code>NEW</code> behavior is to return <code>1</code> if the first argument is empty and the list contains an empty item. </p>
<p> This policy was introduced in CMake version 3.14. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0084</h3>
<p>New in version 3.14. </p>
<p> The <code>FindQt</code> module does not exist for <code>find_package()</code>. </p>
<p> The existence of <code>FindQt</code> means that for Qt upstream to provide package config files that can be found by <code>find_package(Qt)</code>, the consuming project has to explicitly specify <code>find_package(Qt CONFIG)</code>. Removing this module gives Qt a path forward for exporting its own config files which can easily be found by consuming projects. </p>
<p> This policy pretends that CMake&#8217;s internal <code>FindQt</code> module does not exist for <code>find_package()</code>. If a project really wants to use Qt 3 or 4, it can call <code>find_package(Qt[34])</code>, <code>include(FindQt)</code>, or add <code>FindQt</code> to their <code>CMAKE_MODULE_PATH</code>. </p>
<p> The <code>OLD</code> behavior of this policy is for <code>FindQt</code> to exist for <code>find_package()</code>. The <code>NEW</code> behavior is to pretend that it doesn&#8217;t exist for <code>find_package()</code>. </p>
<p> This policy was introduced in CMake version 3.14. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0083</h3>
<p>New in version 3.14. </p>
<p> To control generation of Position Independent Executable (<code>PIE</code>) or not, some flags are required at link time. </p>
<p> CMake 3.13 and lower did not add these link flags when <code>POSITION_INDEPENDENT_CODE</code> is set. </p>
<p> The <code>OLD</code> behavior for this policy is to not manage <code>PIE</code> link flags. The <code>NEW</code> behavior is to add link flags if <code>POSITION_INDEPENDENT_CODE</code> is set:</p>
<dl>
<dt>&bull;</p>
<dd>Set to <code>TRUE</code>: flags to produce a position independent executable are passed to the linker step. For example <code>-pie</code> for <code>GCC</code>.</p>
<dt>&bull;</p>
<dd>Set to <code>FALSE</code>: flags not to produce a position independent executable are passed to the linker step. For example <code>-no-pie</code> for <code>GCC</code>.</p>
<dt>&bull;</p>
<dd>Not set: no flags are passed to the linker step. </p>
<p> Since a given linker may not support <code>PIE</code> flags in all environments in which it is used, it is the project&#8217;s responsibility to use the <code>CheckPIESupported</code> module to check for support to ensure that the <code>POSITION_INDEPENDENT_CODE</code> target property for executables will be honored at link time. </p>
<p> This policy was introduced in CMake version 3.14. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. Unlike most policies, CMake version 3.22.1 does not warn when this policy is not set and simply uses <code>OLD</code> behavior. </p>
<p> <code>NOTE:</code> Android platform has a special handling of <code>PIE</code> so it is not required to use the <code>CheckPIESupported</code> module to ensure flags are passed to the linker. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</dl>
<h3>Examples</h3>
<p>Behave like CMake 3.13 and do not apply any <code>PIE</code> flags at link stage. </p>
<pre>cmake_minimum_required(VERSION 3.13)
project(foo)
# ...
add_executable(foo ...)
set_property(TARGET foo PROPERTY POSITION_INDEPENDENT_CODE TRUE)</pre>
<p>Use the <code>CheckPIESupported</code> module to detect whether <code>PIE</code> is supported by the current linker and environment. Apply <code>PIE</code> flags only if the linker supports them. </p>
<pre>cmake_minimum_required(VERSION 3.14) # CMP0083 NEW
project(foo)
include(CheckPIESupported)
check_pie_supported()
# ...
add_executable(foo ...)
set_property(TARGET foo PROPERTY POSITION_INDEPENDENT_CODE TRUE)</pre>
<h3>Cmp0082</h3>
<p>New in version 3.14. </p>
<p> Install rules from <code>add_subdirectory()</code> calls are interleaved with those in caller. </p>
<p> CMake 3.13 and lower ran the install rules from <code>add_subdirectory()</code> after all other install rules, even if <code>add_subdirectory()</code> was called before the other install rules. CMake 3.14 and above prefer to interleave these <code>add_subdirectory()</code> install rules with the others so that they are run in the order they are declared. This policy provides compatibility for projects that have not been updated to expect the new behavior. </p>
<p> The <code>OLD</code> behavior for this policy is to run the install rules from <code>add_subdirectory()</code> after the other install rules. The <code>NEW</code> behavior for this policy is to run all install rules in the order they are declared. </p>
<p> This policy was introduced in CMake version 3.14. Unlike most policies, CMake version 3.22.1 does <i>not</i> warn by default when this policy is not set and simply uses <code>OLD</code> behavior. See documentation of the <code>CMAKE_POLICY_WARNING_CMP0082</code> variable to control the warning. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 3.13</h2>
<h3>Cmp0081</h3>
<p>New in version 3.13. </p>
<p> Relative paths not allowed in <code>LINK_DIRECTORIES</code> target property. </p>
<p> CMake 3.12 and lower allowed the <code>LINK_DIRECTORIES</code> directory property to contain relative paths. The base path for such relative entries is not well defined. CMake 3.13 and later will issue a <code>FATAL_ERROR</code> if the <code>LINK_DIRECTORIES</code> target property (which is initialized by the <code>LINK_DIRECTORIES</code> directory property) contains a relative path. </p>
<p> The <code>OLD</code> behavior for this policy is not to warn about relative paths in the <code>LINK_DIRECTORIES</code> target property. The <code>NEW</code> behavior for this policy is to issue a <code>FATAL_ERROR</code> if <code>LINK_DIRECTORIES</code> contains a relative path. </p>
<p> This policy was introduced in CMake version 3.13. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0080</h3>
<p>New in version 3.13. </p>
<p> <code>BundleUtilities</code> cannot be included at configure time. </p>
<p> The macros provided by <code>BundleUtilities</code> are intended to be invoked at install time rather than at configure time, because they depend on the listed targets already existing at the time they are invoked. If they are invoked at configure time, the targets haven&#8217;t been built yet, and the commands will fail. </p>
<p> This policy restricts the inclusion of <code>BundleUtilities</code> to <code>cmake -P</code> style scripts and install rules. Specifically, it looks for the presence of <code>CMAKE_GENERATOR</code> and throws a fatal error if it exists. </p>
<p> The <code>OLD</code> behavior of this policy is to allow <code>BundleUtilities</code> to be included at configure time. The <code>NEW</code> behavior of this policy is to disallow such inclusion. </p>
<p> This policy was introduced in CMake version 3.13. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0079</h3>
<p>New in version 3.13. </p>
<p> <code>target_link_libraries()</code> allows use with targets in other directories. </p>
<p> Prior to CMake 3.13 the <code>target_link_libraries()</code> command did not accept targets not created in the calling directory as its first argument for calls that update the <code>LINK_LIBRARIES</code> of the target itself. It did accidentally accept targets from other directories on calls that only update the <code>INTERFACE_LINK_LIBRARIES</code>, but would simply add entries to the property as if the call were made in the original directory. Thus link interface libraries specified this way were always looked up by generators in the scope of the original target rather than in the scope that called <code>target_link_libraries()</code>. </p>
<p> CMake 3.13 now allows the <code>target_link_libraries()</code> command to be called from any directory to add link dependencies and link interface libraries to targets created in other directories. The entries are added to <code>LINK_LIBRARIES</code> and <code>INTERFACE_LINK_LIBRARIES</code> using a special (internal) suffix to tell the generators to look up the names in the calling scope rather than the scope that created the target. </p>
<p> This policy provides compatibility with projects that already use <code>target_link_libraries()</code> with the <code>INTERFACE</code> keyword on a target in another directory to add <code>INTERFACE_LINK_LIBRARIES</code> entries to be looked up in the target&#8217;s directory. Such projects should be updated to be aware of the new scoping rules in that case. </p>
<p> The <code>OLD</code> behavior of this policy is to disallow <code>target_link_libraries()</code> calls naming targets from another directory except in the previously accidentally allowed case of using the <code>INTERFACE</code> keyword only. The <code>NEW</code> behavior of this policy is to allow all such calls but use the new scoping rules. </p>
<p> This policy was introduced in CMake version 3.13. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0078</h3>
<p>New in version 3.13. </p>
<p> <code>UseSWIG</code> generates standard target names. </p>
<p> Starting with CMake 3.13, <code>UseSWIG</code> generates now standard target names. This policy provides compatibility with projects that expect the legacy behavior. </p>
<p> The <code>OLD</code> behavior for this policy relies on <code>UseSWIG_TARGET_NAME_PREFERENCE</code> variable that can be used to specify an explicit preference. The value may be one of:</p>
<dl>
<dt>&bull;</p>
<dd><code>LEGACY</code>: legacy strategy is applied. Variable <code>SWIG_MODULE_&lt;name&gt;_REAL_NAME</code> must be used to get real target name. This is the default if not specified.</p>
<dt>&bull;</p>
<dd><code>STANDARD</code>: target name matches specified name. </p>
<p> This policy was introduced in CMake version 3.13. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</dl>
<h3>Cmp0077</h3>
<p>New in version 3.13. </p>
<p> <code>option()</code> honors normal variables. </p>
<p> The <code>option()</code> command is typically used to create a cache entry to allow users to set the option. However, there are cases in which a normal (non-cached) variable of the same name as the option may be defined by the project prior to calling the <code>option()</code> command. For example, a project that embeds another project as a subdirectory may want to hard-code options of the subproject to build the way it needs. </p>
<p> For historical reasons in CMake 3.12 and below the <code>option()</code> command <i>removes</i> a normal (non-cached) variable of the same name when:</p>
<dl>
<dt>&bull;</p>
<dd>a cache entry of the specified name does not exist at all, or</p>
<dt>&bull;</p>
<dd>a cache entry of the specified name exists but has not been given a type (e.g. via <code>-D&lt;name&gt;=ON</code> on the command line). </p>
<p> In both of these cases (typically on the first run in a new build tree), the <code>option()</code> command gives the cache entry type <code>BOOL</code> and removes any normal (non-cached) variable of the same name. In the remaining case that the cache entry of the specified name already exists and has a type (typically on later runs in a build tree), the <code>option()</code> command changes nothing and any normal variable of the same name remains set. </p>
<p> In CMake 3.13 and above the <code>option()</code> command prefers to do nothing when a normal variable of the given name already exists. It does not create or update a cache entry or remove the normal variable. The new behavior is consistent between the first and later runs in a build tree. This policy provides compatibility with projects that have not been updated to expect the new behavior. </p>
<p> When the <code>option()</code> command sees a normal variable of the given name:</p>
<dt>&bull;</p>
<dd>The <code>OLD</code> behavior for this policy is to proceed even when a normal variable of the same name exists. If the cache entry does not already exist and have a type then it is created and/or given a type and the normal variable is removed.</p>
<dt>&bull;</p>
<dd>The <code>NEW</code> behavior for this policy is to do nothing when a normal variable of the same name exists. The normal variable is not removed. The cache entry is not created or updated and is ignored if it exists. </p>
<p> See <code>CMP0126</code> for a similar policy for the <code>set(CACHE)</code> command, but note that there are some differences in <code>NEW</code> behavior between the two policies. </p>
<p> This policy was introduced in CMake version 3.13. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly within a project. Use the <code>CMAKE_POLICY_DEFAULT_CMP0077</code> variable to set the policy for a third-party project in a subdirectory without modifying it. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</dl>
<h3>Cmp0076</h3>
<p>New in version 3.13. </p>
<p> The <code>target_sources()</code> command converts relative paths to absolute. </p>
<p> In CMake 3.13 and above, the <code>target_sources()</code> command now converts relative source file paths to absolute paths in the following cases:</p>
<dl>
<dt>&bull;</p>
<dd>Source files are added to the target&#8217;s <code>INTERFACE_SOURCES</code> property.</p>
<dt>&bull;</p>
<dd>The target&#8217;s <code>SOURCE_DIR</code> property differs from <code>CMAKE_CURRENT_SOURCE_DIR</code>. </p>
<p> A path that begins with a generator expression is always left unmodified. </p>
<p> This policy provides compatibility with projects that have not been updated to expect this behavior. The <code>OLD</code> behavior for this policy is to leave all relative source file paths unmodified. The <code>NEW</code> behavior of this policy is to convert relative paths to absolute according to above rules. </p>
<p> This policy was introduced in CMake version 3.13. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</dl>
<h2>Policies Introduced By Cmake 3.12</h2>
<h3>Cmp0075</h3>
<p>New in version 3.12. </p>
<p> Include file check macros honor <code>CMAKE_REQUIRED_LIBRARIES</code>. </p>
<p> In CMake 3.12 and above, the</p>
<dl>
<dt>&bull;</p>
<dd><code>check_include_file</code> macro in the <code>CheckIncludeFile</code> module, the</p>
<dt>&bull;</p>
<dd><code>check_include_file_cxx</code> macro in the <code>CheckIncludeFileCXX</code> module, and the</p>
<dt>&bull;</p>
<dd><code>check_include_files</code> macro in the <code>CheckIncludeFiles</code> module </p>
<p> now prefer to link the check executable to the libraries listed in the <code>CMAKE_REQUIRED_LIBRARIES</code> variable. This policy provides compatibility with projects that have not been updated to expect this behavior. </p>
<p> The <code>OLD</code> behavior for this policy is to ignore <code>CMAKE_REQUIRED_LIBRARIES</code> in the include file check macros. The <code>NEW</code> behavior of this policy is to honor <code>CMAKE_REQUIRED_LIBRARIES</code> in the include file check macros. </p>
<p> This policy was introduced in CMake version 3.12. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</dl>
<h3>Cmp0074</h3>
<p>New in version 3.12. </p>
<p> <code>find_package()</code> uses <code>&lt;PackageName&gt;_ROOT</code> variables. </p>
<p> In CMake 3.12 and above the <code>find_package(&lt;PackageName&gt;)</code> command now searches prefixes specified by the <code>&lt;PackageName&gt;_ROOT</code> CMake variable and the <code>&lt;PackageName&gt;_ROOT</code> environment variable. Package roots are maintained as a stack so nested calls to all <code>find_*</code> commands inside find modules and config packages also search the roots as prefixes. This policy provides compatibility with projects that have not been updated to avoid using <code>&lt;PackageName&gt;_ROOT</code> variables for other purposes. </p>
<p> The <code>OLD</code> behavior for this policy is to ignore <code>&lt;PackageName&gt;_ROOT</code> variables. The <code>NEW</code> behavior for this policy is to use <code>&lt;PackageName&gt;_ROOT</code> variables. </p>
<p> This policy was introduced in CMake version 3.12. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0073</h3>
<p>New in version 3.12. </p>
<p> Do not produce legacy <code>_LIB_DEPENDS</code> cache entries. </p>
<p> Ancient CMake versions once used <code>&lt;tgt&gt;_LIB_DEPENDS</code> cache entries to propagate library link dependencies. This has long been done by other means, leaving the <code>export_library_dependencies()</code> command as the only user of these values. That command has long been disallowed by policy <code>CMP0033</code>, but the <code>&lt;tgt&gt;_LIB_DEPENDS</code> cache entries were left for compatibility with possible non-standard uses by projects. </p>
<p> CMake 3.12 and above now prefer to not produce these cache entries at all. This policy provides compatibility with projects that have not been updated to avoid using them. </p>
<p> The <code>OLD</code> behavior for this policy is to set <code>&lt;tgt&gt;_LIB_DEPENDS</code> cache entries. The <code>NEW</code> behavior for this policy is to not set them. </p>
<p> This policy was introduced in CMake version 3.12. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. Unlike most policies, CMake version 3.22.1 does <i>not</i> warn when this policy is not set and simply uses <code>OLD</code> behavior. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 3.11</h2>
<h3>Cmp0072</h3>
<p>New in version 3.11. </p>
<p> <code>FindOpenGL</code> prefers GLVND by default when available. </p>
<p> The <code>FindOpenGL</code> module provides an <code>OpenGL::GL</code> target and an <code>OPENGL_LIBRARIES</code> variable for projects to use for legacy GL interfaces. When both a legacy GL library (e.g. <code>libGL.so</code>) and GLVND libraries for OpenGL and GLX (e.g. <code>libOpenGL.so</code> and <code>libGLX.so</code>) are available, the module must choose between them. It documents an <code>OpenGL_GL_PREFERENCE</code> variable that can be used to specify an explicit preference. When no such preference is set, the module must choose a default preference. </p>
<p> CMake 3.11 and above prefer to choose GLVND libraries. This policy provides compatibility with projects that expect the legacy GL library to be used. </p>
<p> The <code>OLD</code> behavior for this policy is to set <code>OpenGL_GL_PREFERENCE</code> to <code>LEGACY</code>. The <code>NEW</code> behavior for this policy is to set <code>OpenGL_GL_PREFERENCE</code> to <code>GLVND</code>. </p>
<p> This policy was introduced in CMake version 3.11. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 3.10</h2>
<h3>Cmp0071</h3>
<p>New in version 3.10. </p>
<p> Let <code>AUTOMOC</code> and <code>AUTOUIC</code> process <code>GENERATED</code> files. </p>
<p> Since version 3.10, CMake processes <code>regular</code> and <code>GENERATED</code> source files in <code>AUTOMOC</code> and <code>AUTOUIC</code>. In earlier CMake versions, only <code>regular</code> source files were processed. <code>GENERATED</code> source files were ignored silently. </p>
<p> This policy affects how source files that are <code>GENERATED</code> get treated in <code>AUTOMOC</code> and <code>AUTOUIC</code>. </p>
<p> The <code>OLD</code> behavior for this policy is to ignore <code>GENERATED</code> source files in <code>AUTOMOC</code> and <code>AUTOUIC</code>. </p>
<p> The <code>NEW</code> behavior for this policy is to process <code>GENERATED</code> source files in <code>AUTOMOC</code> and <code>AUTOUIC</code> just like regular source files. </p>
<p> <code>NOTE:</code> To silence the <code>CMP0071</code> warning source files can be excluded from <code>AUTOMOC</code> and <code>AUTOUIC</code> processing by setting the source file properties <code>SKIP_AUTOMOC</code>, <code>SKIP_AUTOUIC</code> or <code>SKIP_AUTOGEN</code>. </p>
<p> Source skip example: </p>
<pre># ...
set_property(SOURCE /path/to/file1.h PROPERTY SKIP_AUTOMOC ON)
set_property(SOURCE /path/to/file2.h PROPERTY SKIP_AUTOUIC ON)
set_property(SOURCE /path/to/file3.h PROPERTY SKIP_AUTOGEN ON)
# ...</pre>
<p>This policy was introduced in CMake version 3.10. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0070</h3>
<p>New in version 3.10. </p>
<p> Define <code>file(GENERATE)</code> behavior for relative paths. </p>
<p> CMake 3.10 and newer define that relative paths given to <code>INPUT</code> and <code>OUTPUT</code> arguments of <code>file(GENERATE)</code> are interpreted relative to the current source and binary directories, respectively. CMake 3.9 and lower did not define any behavior for relative paths but did not diagnose them either and accidentally treated them relative to the process working directory. Policy <code>CMP0070</code> provides compatibility with projects that used the old undefined behavior. </p>
<p> This policy affects behavior of relative paths given to <code>file(GENERATE)</code>. The <code>OLD</code> behavior for this policy is to treat the paths relative to the working directory of CMake. The <code>NEW</code> behavior for this policy is to interpret relative paths with respect to the current source or binary directory of the caller. </p>
<p> This policy was introduced in CMake version 3.10. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 3.9</h2>
<h3>Cmp0069</h3>
<p>New in version 3.9. </p>
<p> <code>INTERPROCEDURAL_OPTIMIZATION</code> is enforced when enabled. </p>
<p> CMake 3.9 and newer prefer to add IPO flags whenever the <code>INTERPROCEDURAL_OPTIMIZATION</code> target property is enabled and produce an error if flags are not known to CMake for the current compiler. Since a given compiler may not support IPO flags in all environments in which it is used, it is now the project&#8217;s responsibility to use the <code>CheckIPOSupported</code> module to check for support before enabling the <code>INTERPROCEDURAL_OPTIMIZATION</code> target property. This approach allows a project to conditionally activate IPO when supported. It also allows an end user to set the <code>CMAKE_INTERPROCEDURAL_OPTIMIZATION</code> variable in an environment known to support IPO even if the project does not enable the property. </p>
<p> Since CMake 3.8 and lower only honored <code>INTERPROCEDURAL_OPTIMIZATION</code> for the Intel compiler on Linux, some projects may unconditionally enable the target property. Policy <code>CMP0069</code> provides compatibility with such projects. </p>
<p> This policy takes effect whenever the IPO property is enabled. The <code>OLD</code> behavior for this policy is to add IPO flags only for Intel compiler on Linux. The <code>NEW</code> behavior for this policy is to add IPO flags for the current compiler or produce an error if CMake does not know the flags. </p>
<p> This policy was introduced in CMake version 3.9. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Examples</h3>
<p>Behave like CMake 3.8 and do not apply any IPO flags except for Intel compiler on Linux: </p>
<pre>cmake_minimum_required(VERSION 3.8)
project(foo)
# ...
set_property(TARGET ... PROPERTY INTERPROCEDURAL_OPTIMIZATION TRUE)</pre>
<p>Use the <code>CheckIPOSupported</code> module to detect whether IPO is supported by the current compiler, environment, and CMake version. Produce a fatal error if support is not available: </p>
<pre>cmake_minimum_required(VERSION 3.9) # CMP0069 NEW
project(foo)
include(CheckIPOSupported)
check_ipo_supported()
# ...
set_property(TARGET ... PROPERTY INTERPROCEDURAL_OPTIMIZATION TRUE)</pre>
<p>Apply IPO flags only if compiler supports it: </p>
<pre>cmake_minimum_required(VERSION 3.9) # CMP0069 NEW
project(foo)
include(CheckIPOSupported)
# ...
check_ipo_supported(RESULT result)
if(result)
 set_property(TARGET ... PROPERTY INTERPROCEDURAL_OPTIMIZATION TRUE)
endif()</pre>
<p>Apply IPO flags without any checks. This may lead to build errors if IPO is not supported by the compiler in the current environment. Produce an error if CMake does not know IPO flags for the current compiler: </p>
<pre>cmake_minimum_required(VERSION 3.9) # CMP0069 NEW
project(foo)
# ...
set_property(TARGET ... PROPERTY INTERPROCEDURAL_OPTIMIZATION TRUE)</pre>
<h3>Cmp0068</h3>
<p>New in version 3.9. </p>
<p> <code>RPATH</code> settings on macOS do not affect <code>install_name</code>. </p>
<p> CMake 3.9 and newer remove any effect the following settings may have on the <code>install_name</code> of a target on macOS:</p>
<dl>
<dt>&bull;</p>
<dd><code>BUILD_WITH_INSTALL_RPATH</code> target property</p>
<dt>&bull;</p>
<dd><code>SKIP_BUILD_RPATH</code> target property</p>
<dt>&bull;</p>
<dd><code>CMAKE_SKIP_RPATH</code> variable</p>
<dt>&bull;</p>
<dd><code>CMAKE_SKIP_INSTALL_RPATH</code> variable </p>
<p> Previously, setting <code>BUILD_WITH_INSTALL_RPATH</code> had the effect of setting both the <code>install_name</code> of a target to <code>INSTALL_NAME_DIR</code> and the <code>RPATH</code> to <code>INSTALL_RPATH</code>. In CMake 3.9, it only affects setting of <code>RPATH</code>. However, if one wants <code>INSTALL_NAME_DIR</code> to apply to the target in the build tree, one may set <code>BUILD_WITH_INSTALL_NAME_DIR</code>. </p>
<p> If <code>SKIP_BUILD_RPATH</code>, <code>CMAKE_SKIP_RPATH</code> or <code>CMAKE_SKIP_INSTALL_RPATH</code> were used to strip the directory portion of the <code>install_name</code> of a target, one may set <code>INSTALL_NAME_DIR=&quot;&quot;</code> instead. </p>
<p> The <code>OLD</code> behavior of this policy is to use the <code>RPATH</code> settings for <code>install_name</code> on macOS. The <code>NEW</code> behavior of this policy is to ignore the <code>RPATH</code> settings for <code>install_name</code> on macOS. </p>
<p> This policy was introduced in CMake version 3.9. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</dl>
<h2>Policies Introduced By Cmake 3.8</h2>
<h3>Cmp0067</h3>
<p>New in version 3.8. </p>
<p> Honor language standard in <code>try_compile()</code> source-file signature. </p>
<p> The <code>try_compile()</code> source file signature is intended to allow callers to check whether they will be able to compile a given source file with the current toolchain. In order to match compiler behavior, any language standard mode should match. However, CMake 3.7 and below did not do this. CMake 3.8 and above prefer to honor the language standard settings for <code>C</code>, <code>CXX</code> (C++), and <code>CUDA</code> using the values of the variables:</p>
<dl>
<dt>&bull;</p>
<dd><code>CMAKE_C_STANDARD</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_C_STANDARD_REQUIRED</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_C_EXTENSIONS</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_CXX_STANDARD</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_CXX_STANDARD_REQUIRED</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_CXX_EXTENSIONS</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_CUDA_STANDARD</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_CUDA_STANDARD_REQUIRED</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_CUDA_EXTENSIONS</code> </p>
<p> This policy provides compatibility for projects that do not expect the language standard settings to be used automatically. </p>
<p> The <code>OLD</code> behavior of this policy is to ignore language standard setting variables when generating the <code>try_compile</code> test project. The <code>NEW</code> behavior of this policy is to honor language standard setting variables. </p>
<p> This policy was introduced in CMake version 3.8. Unlike most policies, CMake version 3.22.1 does <i>not</i> warn by default when this policy is not set and simply uses <code>OLD</code> behavior. See documentation of the <code>CMAKE_POLICY_WARNING_CMP0067</code> variable to control the warning. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</dl>
<h2>Policies Introduced By Cmake 3.7</h2>
<h3>Cmp0066</h3>
<p>New in version 3.7. </p>
<p> Honor per-config flags in <code>try_compile()</code> source-file signature. </p>
<p> The source file signature of the <code>try_compile()</code> command uses the value of the <code>CMAKE_&lt;LANG&gt;_FLAGS</code> variable in the test project so that the test compilation works as it would in the main project. However, CMake 3.6 and below do not also honor config-specific compiler flags such as those in the <code>CMAKE_&lt;LANG&gt;_FLAGS_DEBUG</code> variable. CMake 3.7 and above prefer to honor config-specific compiler flags too. This policy provides compatibility for projects that do not expect config-specific compiler flags to be used. </p>
<p> The <code>OLD</code> behavior of this policy is to ignore config-specific flag variables like <code>CMAKE_&lt;LANG&gt;_FLAGS_DEBUG</code> and only use CMake&#8217;s built-in defaults for the current compiler and platform. </p>
<p> The <code>NEW</code> behavior of this policy is to honor config-specific flag variabldes like <code>CMAKE_&lt;LANG&gt;_FLAGS_DEBUG</code>. </p>
<p> This policy was introduced in CMake version 3.7. Unlike most policies, CMake version 3.22.1 does <i>not</i> warn by default when this policy is not set and simply uses <code>OLD</code> behavior. See documentation of the <code>CMAKE_POLICY_WARNING_CMP0066</code> variable to control the warning. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 3.4</h2>
<h3>Cmp0065</h3>
<p>New in version 3.4. </p>
<p> Do not add flags to export symbols from executables without the <code>ENABLE_EXPORTS</code> target property. </p>
<p> CMake 3.3 and below, for historical reasons, always linked executables on some platforms with flags like <code>-rdynamic</code> to export symbols from the executables for use by any plugins they may load via <code>dlopen</code>. CMake 3.4 and above prefer to do this only for executables that are explicitly marked with the <code>ENABLE_EXPORTS</code> target property. </p>
<p> The <code>OLD</code> behavior of this policy is to always use the additional link flags when linking executables regardless of the value of the <code>ENABLE_EXPORTS</code> target property. </p>
<p> The <code>NEW</code> behavior of this policy is to only use the additional link flags when linking executables if the <code>ENABLE_EXPORTS</code> target property is set to <code>True</code>. </p>
<p> This policy was introduced in CMake version 3.4. Unlike most policies, CMake version 3.22.1 does <i>not</i> warn by default when this policy is not set and simply uses <code>OLD</code> behavior. See documentation of the <code>CMAKE_POLICY_WARNING_CMP0065</code> variable to control the warning. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0064</h3>
<p>New in version 3.4. </p>
<p> Recognize <code>TEST</code> as a operator for the <code>if()</code> command. </p>
<p> The <code>TEST</code> operator was added to the <code>if()</code> command to determine if a given test name was created by the <code>add_test()</code> command. </p>
<p> The <code>OLD</code> behavior for this policy is to ignore the <code>TEST</code> operator. The <code>NEW</code> behavior is to interpret the <code>TEST</code> operator. </p>
<p> This policy was introduced in CMake version 3.4. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 3.3</h2>
<h3>Cmp0063</h3>
<p>New in version 3.3. </p>
<p> Honor visibility properties for all target types. </p>
<p> The <code>&lt;LANG&gt;_VISIBILITY_PRESET</code> and <code>VISIBILITY_INLINES_HIDDEN</code> target properties affect visibility of symbols during dynamic linking. When first introduced these properties affected compilation of sources only in shared libraries, module libraries, and executables with the <code>ENABLE_EXPORTS</code> property set. This was sufficient for the basic use cases of shared libraries and executables with plugins. However, some sources may be compiled as part of static libraries or object libraries and then linked into a shared library later. CMake 3.3 and above prefer to honor these properties for sources compiled in all target types. This policy preserves compatibility for projects expecting the properties to work only for some target types. </p>
<p> The <code>OLD</code> behavior for this policy is to ignore the visibility properties for static libraries, object libraries, and executables without exports. The <code>NEW</code> behavior for this policy is to honor the visibility properties for all target types. </p>
<p> This policy was introduced in CMake version 3.3. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0062</h3>
<p>New in version 3.3. </p>
<p> Disallow <code>install()</code> of <code>export()</code> result. </p>
<p> The <code>export()</code> command generates a file containing Imported Targets, which is suitable for use from the build directory. It is not suitable for installation because it contains absolute paths to buildsystem locations, and is particular to a single build configuration. </p>
<p> The <code>install(EXPORT)</code> generates and installs files which contain Imported Targets. These files are generated with relative paths (unless the user specifies absolute paths), and are designed for multi-configuration use. See Creating Packages for more. </p>
<p> CMake 3.3 no longer allows the use of the <code>install(FILES)</code> command with the result of the <code>export()</code> command. </p>
<p> The <code>OLD</code> behavior for this policy is to allow installing the result of an <code>export()</code> command. The <code>NEW</code> behavior for this policy is not to allow installing the result of an <code>export()</code> command. </p>
<p> This policy was introduced in CMake version 3.3. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0061</h3>
<p>New in version 3.3. </p>
<p> CTest does not by default tell <code>make</code> to ignore errors (<code>-i</code>). </p>
<p> The <code>ctest_build()</code> and <code>build_command()</code> commands no longer generate build commands for Makefile Generators with the <code>-i</code> option. Previously this was done to help build as much of tested projects as possible. However, this behavior is not consistent with other generators and also causes the return code of the <code>make</code> tool to be meaningless. </p>
<p> Of course users may still add this option manually by setting <code>CTEST_BUILD_COMMAND</code> or the <code>MAKECOMMAND</code> cache entry. See the CTest Build Step <code>MakeCommand</code> setting documentation for their effects. </p>
<p> The <code>OLD</code> behavior for this policy is to add <code>-i</code> to <code>make</code> calls in CTest. The <code>NEW</code> behavior for this policy is to not add <code>-i</code>. </p>
<p> This policy was introduced in CMake version 3.3. Unlike most policies, CMake version 3.22.1 does <i>not</i> warn when this policy is not set and simply uses <code>OLD</code> behavior. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0060</h3>
<p>New in version 3.3. </p>
<p> Link libraries by full path even in implicit directories. </p>
<p> Policy <code>CMP0003</code> was introduced with the intention of always linking library files by full path when a full path is given to the <code>target_link_libraries()</code> command. However, on some platforms (e.g. HP-UX) the compiler front-end adds alternative library search paths for the current architecture (e.g. <code>/usr/lib/&lt;arch&gt;</code> has alternatives to libraries in <code>/usr/lib</code> for the current architecture). On such platforms the <code>find_library()</code> may find a library such as <code>/usr/lib/libfoo.so</code> that does not belong to the current architecture. </p>
<p> Prior to policy <code>CMP0003</code> projects would still build in such cases because the incorrect library path would be converted to <code>-lfoo</code> on the link line and the linker would find the proper library in the arch-specific search path provided by the compiler front-end implicitly. At the time we chose to remain compatible with such projects by always converting library files found in implicit link directories to <code>-lfoo</code> flags to ask the linker to search for them. This approach allowed existing projects to continue to build while still linking to libraries outside implicit link directories via full path (such as those in the build tree). </p>
<p> CMake does allow projects to override this behavior by using an IMPORTED library target with its <code>IMPORTED_LOCATION</code> property set to the desired full path to a library file. In fact, many Find Modules are learning to provide Imported Targets instead of just the traditional <code>Foo_LIBRARIES</code> variable listing library files. However, this makes the link line generated for a library found by a Find Module depend on whether it is linked through an imported target or not, which is inconsistent. Furthermore, this behavior has been a source of confusion because the generated link line for a library file depends on its location. It is also problematic for projects trying to link statically because flags like <code>-Wl,-Bstatic -lfoo -Wl,-Bdynamic</code> may be used to help the linker select <code>libfoo.a</code> instead of <code>libfoo.so</code> but then leak dynamic linking to following libraries. (See the <code>LINK_SEARCH_END_STATIC</code> target property for a solution typically used for that problem.) </p>
<p> When the special case for libraries in implicit link directories was first introduced the list of implicit link directories was simply hard-coded (e.g. <code>/lib</code>, <code>/usr/lib</code>, and a few others). Since that time, CMake has learned to detect the implicit link directories used by the compiler front-end. If necessary, the <code>find_library()</code> command could be taught to use this information to help find libraries of the proper architecture. </p>
<p> For these reasons, CMake 3.3 and above prefer to drop the special case and link libraries by full path even when they are in implicit link directories. Policy <code>CMP0060</code> provides compatibility for existing projects. </p>
<p> The <code>OLD</code> behavior for this policy is to ask the linker to search for libraries whose full paths are known to be in implicit link directories. The <code>NEW</code> behavior for this policy is to link libraries by full path even if they are in implicit link directories. </p>
<p> This policy was introduced in CMake version 3.3. Unlike most policies, CMake version 3.22.1 does <i>not</i> warn by default when this policy is not set and simply uses <code>OLD</code> behavior. See documentation of the <code>CMAKE_POLICY_WARNING_CMP0060</code> variable to control the warning. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0059</h3>
<p>New in version 3.3. </p>
<p> Do not treat <code>DEFINITIONS</code> as a built-in directory property. </p>
<p> CMake 3.3 and above no longer make a list of definitions available through the <code>DEFINITIONS</code> directory property. The <code>COMPILE_DEFINITIONS</code> directory property may be used instead. </p>
<p> The <code>OLD</code> behavior for this policy is to provide the list of flags given so far to the <code>add_definitions()</code> command. The <code>NEW</code> behavior is to behave as a normal user-defined directory property. </p>
<p> This policy was introduced in CMake version 3.3. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0058</h3>
<p>New in version 3.3. </p>
<p> Ninja requires custom command byproducts to be explicit. </p>
<p> When an intermediate file generated during the build is consumed by an expensive operation or a large tree of dependents, one may reduce the work needed for an incremental rebuild by updating the file timestamp only when its content changes. With this approach the generation rule must have a separate output file that is always updated with a new timestamp that is newer than any dependencies of the rule so that the build tool re-runs the rule only when the input changes. We refer to the separate output file as a rule&#8217;s <i>witness</i> and the generated file as a rule&#8217;s <i>byproduct</i>. </p>
<p> Byproducts may not be listed as outputs because their timestamps are allowed to be older than the inputs. No build tools (like <code>make</code>) that existed when CMake was designed have a way to express byproducts. Therefore CMake versions prior to 3.2 had no way to specify them. Projects typically left byproducts undeclared in the rules that generate them. For example: </p>
<pre>add_custom_command(
 OUTPUT witness.txt
 COMMAND ${CMAKE_COMMAND} -E copy_if_different
 ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
 byproduct.txt # timestamp may not change
 COMMAND ${CMAKE_COMMAND} -E touch witness.txt
 DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
 )
add_custom_target(Provider DEPENDS witness.txt)
add_custom_command(
 OUTPUT generated.c
 COMMAND expensive-task -i byproduct.txt -o generated.c
 DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/byproduct.txt
 )
add_library(Consumer generated.c)
add_dependencies(Consumer Provider)</pre>
<p>This works well for all generators except <code>Ninja</code>. The Ninja build tool sees a rule listing <code>byproduct.txt</code> as a dependency and no rule listing it as an output. Ninja then complains that there is no way to satisfy the dependency and stops building even though there are order-only dependencies that ensure <code>byproduct.txt</code> will exist before its consumers need it. See discussion of this problem in <i>Ninja Issue 760</i> for further details on why Ninja works this way. </p>
<p> Instead of leaving byproducts undeclared in the rules that generate them, Ninja expects byproducts to be listed along with other outputs. Such rules may be marked with a <code>restat</code> option that tells Ninja to check the timestamps of outputs after the rules run. This prevents byproducts whose timestamps do not change from causing their dependents to re-build unnecessarily. </p>
<p> Since the above approach does not tell CMake what custom command generates <code>byproduct.txt</code>, the Ninja generator does not have enough information to add the byproduct as an output of any rule. CMake 2.8.12 and above work around this problem and allow projects using the above approach to build by generating <code>phony</code> build rules to tell Ninja to tolerate such missing files. However, this workaround prevents Ninja from diagnosing a dependency that is really missing. It also works poorly in in-source builds where every custom command dependency, even on source files, needs to be treated this way because CMake does not have enough information to know which files are generated as byproducts of custom commands. </p>
<p> CMake 3.2 introduced the <code>BYPRODUCTS</code> option to the <code>add_custom_command()</code> and <code>add_custom_target()</code> commands. This option allows byproducts to be specified explicitly: </p>
<pre>add_custom_command(
 OUTPUT witness.txt
 BYPRODUCTS byproduct.txt # explicit byproduct specification
 COMMAND ${CMAKE_COMMAND} -E copy_if_different
 ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
 byproduct.txt # timestamp may not change
...</pre>
<p>The <code>BYPRODUCTS</code> option is used by the <code>Ninja</code> generator to list byproducts among the outputs of the custom commands that generate them, and is ignored by other generators. </p>
<p> CMake 3.3 and above prefer to require projects to specify custom command byproducts explicitly so that it can avoid using the <code>phony</code> rule workaround altogether. Policy <code>CMP0058</code> was introduced to provide compatibility with existing projects that still need the workaround. </p>
<p> This policy has no effect on generators other than <code>Ninja</code>. The <code>OLD</code> behavior for this policy is to generate Ninja <code>phony</code> rules for unknown dependencies in the build tree. The <code>NEW</code> behavior for this policy is to not generate these and instead require projects to specify custom command <code>BYPRODUCTS</code> explicitly. </p>
<p> This policy was introduced in CMake version 3.3. CMake version 3.22.1 warns when it sees unknown dependencies in out-of-source build trees if the policy is not set and then uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set the policy to <code>OLD</code> or <code>NEW</code> explicitly. The policy setting must be in scope at the end of the top-level <code>CMakeLists.txt</code> file of the project and has global effect. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0057</h3>
<p>New in version 3.3. </p>
<p> Support new <code>if()</code> IN_LIST operator. </p>
<p> CMake 3.3 adds support for the new IN_LIST operator. </p>
<p> The <code>OLD</code> behavior for this policy is to ignore the IN_LIST operator. The <code>NEW</code> behavior is to interpret the IN_LIST operator. </p>
<p> This policy was introduced in CMake version 3.3. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 3.2</h2>
<h3>Cmp0056</h3>
<p>New in version 3.2. </p>
<p> Honor link flags in <code>try_compile()</code> source-file signature. </p>
<p> The <code>try_compile()</code> command source-file signature generates a <code>CMakeLists.txt</code> file to build the source file into an executable. In order to compile the source the same way as it might be compiled by the calling project, the generated project sets the value of the <code>CMAKE_&lt;LANG&gt;_FLAGS</code> variable to that in the calling project. The value of the <code>CMAKE_EXE_LINKER_FLAGS</code> variable may be needed in some cases too, but CMake 3.1 and lower did not set it in the generated project. CMake 3.2 and above prefer to set it so that linker flags are honored as well as compiler flags. This policy provides compatibility with the pre-3.2 behavior. </p>
<p> The <code>OLD</code> behavior for this policy is to not set the value of the <code>CMAKE_EXE_LINKER_FLAGS</code> variable in the generated test project. The <code>NEW</code> behavior for this policy is to set the value of the <code>CMAKE_EXE_LINKER_FLAGS</code> variable in the test project to the same as it is in the calling project. </p>
<p> If the project code does not set the policy explicitly, users may set it on the command line by defining the <code>CMAKE_POLICY_DEFAULT_CMP0056</code> variable in the cache. </p>
<p> This policy was introduced in CMake version 3.2. Unlike most policies, CMake version 3.22.1 does <i>not</i> warn by default when this policy is not set and simply uses <code>OLD</code> behavior. See documentation of the <code>CMAKE_POLICY_WARNING_CMP0056</code> variable to control the warning. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0055</h3>
<p>New in version 3.2. </p>
<p> Strict checking for the <code>break()</code> command. </p>
<p> CMake 3.1 and lower allowed calls to the <code>break()</code> command outside of a loop context and also ignored any given arguments. This was undefined behavior. </p>
<p> The <code>OLD</code> behavior for this policy is to allow <code>break()</code> to be placed outside of loop contexts and ignores any arguments. The <code>NEW</code> behavior for this policy is to issue an error if a misplaced break or any arguments are found. </p>
<p> This policy was introduced in CMake version 3.2. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 3.1</h2>
<h3>Cmp0054</h3>
<p>New in version 3.1. </p>
<p> Only interpret <code>if()</code> arguments as variables or keywords when unquoted. </p>
<p> CMake 3.1 and above no longer implicitly dereference variables or interpret keywords in an <code>if()</code> command argument when it is a Quoted Argument or a Bracket Argument. </p>
<p> The <code>OLD</code> behavior for this policy is to dereference variables and interpret keywords even if they are quoted or bracketed. The <code>NEW</code> behavior is to not dereference variables or interpret keywords that have been quoted or bracketed. </p>
<p> Given the following partial example: </p>
<pre>set(A E)
set(E &quot;&quot;)
if(&quot;${A}&quot; STREQUAL &quot;&quot;)
 message(&quot;Result is TRUE before CMake 3.1 or when CMP0054 is OLD&quot;)
else()
 message(&quot;Result is FALSE in CMake 3.1 and above if CMP0054 is NEW&quot;)
endif()</pre>
<p>After explicit expansion of variables this gives: </p>
<pre>if(&quot;E&quot; STREQUAL &quot;&quot;)</pre>
<p>With the policy set to <code>OLD</code> implicit expansion reduces this semantically to: </p>
<pre>if(&quot;&quot; STREQUAL &quot;&quot;)</pre>
<p>With the policy set to <code>NEW</code> the quoted arguments will not be further dereferenced: </p>
<pre>if(&quot;E&quot; STREQUAL &quot;&quot;)</pre>
<p>This policy was introduced in CMake version 3.1. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0053</h3>
<p>New in version 3.1. </p>
<p> Simplify variable reference and escape sequence evaluation. </p>
<p> CMake 3.1 introduced a much faster implementation of evaluation of the Variable References and Escape Sequences documented in the <code><a href="/docs/linux/man/7-cmake-language/">cmake-language</a>(7)</code> manual. While the behavior is identical to the legacy implementation in most cases, some corner cases were cleaned up to simplify the behavior. Specifically:</p>
<dl>
<dt>&bull;</p>
<dd>Expansion of <code>@VAR@</code> reference syntax defined by the <code>configure_file()</code> and <code>string(CONFIGURE)</code> commands is no longer performed in other contexts.</p>
<dt>&bull;</p>
<dd>Literal <code>${VAR}</code> reference syntax may contain only alphanumeric characters (<code>A-Z</code>, <code>a-z</code>, <code>0-9</code>) and the characters <code>_</code>, <code>.</code>, <code>/</code>, <code>&#8211;</code>, and <code>+</code>. Note that <code>$</code> is technically allowed in the <code>NEW</code> behavior, but is invalid for <code>OLD</code> behavior. This is due to an oversight during the implementation of <i>CMP0053</i> and its use as a literal variable reference is discouraged for this reason. Variables with other characters in their name may still be referenced indirectly, e.g. </p>
<pre>set(varname &quot;otherwise &amp; disallowed $ characters&quot;)
message(&quot;${${varname}}&quot;)</pre>
<dt>&bull;</p>
<dd>The setting of policy <code>CMP0010</code> is not considered, so improper variable reference syntax is always an error.</p>
<dt>&bull;</p>
<dd>More characters are allowed to be escaped in variable names. Previously, only <code>()#&quot; \@^</code> were valid characters to escape. Now any non-alphanumeric, non-semicolon, non-NUL character may be escaped following the <code>escape_identity</code> production in the Escape Sequences section of the <code><a href="/docs/linux/man/7-cmake-language/">cmake-language</a>(7)</code> manual. </p>
<p> The <code>OLD</code> behavior for this policy is to honor the legacy behavior for variable references and escape sequences. The <code>NEW</code> behavior is to use the simpler variable expansion and escape sequence evaluation rules. </p>
<p> This policy was introduced in CMake version 3.1. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</dl>
<h3>Cmp0052</h3>
<p>New in version 3.1. </p>
<p> Reject source and build dirs in installed <code>INTERFACE_INCLUDE_DIRECTORIES</code>. </p>
<p> CMake 3.0 and lower allowed subdirectories of the source directory or build directory to be in the <code>INTERFACE_INCLUDE_DIRECTORIES</code> of installed and exported targets, if the directory was also a subdirectory of the installation prefix. This makes the installation depend on the existence of the source dir or binary dir, and the installation will be broken if either are removed after installation. </p>
<p> See Include Directories and Usage Requirements for more on specifying include directories for targets. </p>
<p> The <code>OLD</code> behavior for this policy is to export the content of the <code>INTERFACE_INCLUDE_DIRECTORIES</code> with the source or binary directory. The <code>NEW</code> behavior for this policy is to issue an error if such a directory is used. </p>
<p> This policy was introduced in CMake version 3.1. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0051</h3>
<p>New in version 3.1. </p>
<p> List <code>TARGET_OBJECTS</code> in SOURCES target property. </p>
<p> CMake 3.0 and lower did not include the <code>TARGET_OBJECTS</code> <code>generator expression</code> when returning the <code>SOURCES</code> target property. </p>
<p> Configure-time CMake code is not able to handle generator expressions. If using the <code>SOURCES</code> target property at configure time, it may be necessary to first remove generator expressions using the <code>string(GENEX_STRIP)</code> command. Generate-time CMake code such as <code>file(GENERATE)</code> can handle the content without stripping. </p>
<p> The <code>OLD</code> behavior for this policy is to omit <code>TARGET_OBJECTS</code> expressions from the <code>SOURCES</code> target property. The <code>NEW</code> behavior for this policy is to include <code>TARGET_OBJECTS</code> expressions in the output. </p>
<p> This policy was introduced in CMake version 3.1. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 3.0</h2>
<h3>Cmp0050</h3>
<p>Disallow add_custom_command SOURCE signatures. </p>
<p> CMake 2.8.12 and lower allowed a signature for <code>add_custom_command()</code> which specified an input to a command. This was undocumented behavior. Modern use of CMake associates custom commands with their output, rather than their input. </p>
<p> The <code>OLD</code> behavior for this policy is to allow the use of <code>add_custom_command()</code> SOURCE signatures. The <code>NEW</code> behavior for this policy is to issue an error if such a signature is used. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0049</h3>
<p>Do not expand variables in target source entries. </p>
<p> CMake 2.8.12 and lower performed an extra layer of variable expansion when evaluating source file names: </p>
<pre>set(a_source foo.c)
add_executable(foo \${a_source})</pre>
<p>This was undocumented behavior. </p>
<p> The <code>OLD</code> behavior for this policy is to expand such variables when processing the target sources. The <code>NEW</code> behavior for this policy is to issue an error if such variables need to be expanded. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0048</h3>
<p>The <code>project()</code> command manages <code>VERSION</code> variables. </p>
<p> CMake version 3.0 introduced the <code>VERSION</code> option of the <code>project()</code> command to specify a project version as well as the name. In order to keep <code>PROJECT_VERSION</code> and related variables consistent with variable <code>PROJECT_NAME</code> it is necessary to set the <code>VERSION</code> variables to the empty string when no <code>VERSION</code> is given to <code>project()</code>. However, this can change behavior for existing projects that set <code>VERSION</code> variables themselves since <code>project()</code> may now clear them. This policy controls the behavior for compatibility with such projects. </p>
<p> The <code>OLD</code> behavior for this policy is to leave <code>VERSION</code> variables untouched. The <code>NEW</code> behavior for this policy is to set <code>VERSION</code> as documented by the <code>project()</code> command. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0047</h3>
<p>Use <code>QCC</code> compiler id for the qcc drivers on QNX. </p>
<p> CMake 3.0 and above recognize that the QNX qcc compiler driver is different from the GNU compiler. CMake now prefers to present this to projects by setting the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable to <code>QCC</code> instead of <code>GNU</code>. However, existing projects may assume the compiler id for QNX qcc is just <code>GNU</code> as it was in CMake versions prior to 3.0. Therefore this policy determines for QNX qcc which compiler id to report in the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable after language <code>&lt;LANG&gt;</code> is enabled by the <code>project()</code> or <code>enable_language()</code> command. The policy must be set prior to the invocation of either command. </p>
<p> The <code>OLD</code> behavior for this policy is to use the <code>GNU</code> compiler id for the qcc and QCC compiler drivers. The <code>NEW</code> behavior for this policy is to use the <code>QCC</code> compiler id for those drivers. </p>
<p> This policy was introduced in CMake version 3.0. Use the <code>cmake_policy()</code> command to set this policy to <code>OLD</code> or <code>NEW</code> explicitly. Unlike most policies, CMake version 3.22.1 does <i>not</i> warn by default when this policy is not set and simply uses <code>OLD</code> behavior. See documentation of the <code>CMAKE_POLICY_WARNING_CMP0047</code> variable to control the warning. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0046</h3>
<p>Error on non-existent dependency in add_dependencies. </p>
<p> CMake 2.8.12 and lower silently ignored non-existent dependencies listed in the <code>add_dependencies()</code> command. </p>
<p> The <code>OLD</code> behavior for this policy is to silently ignore non-existent dependencies. The <code>NEW</code> behavior for this policy is to report an error if non-existent dependencies are listed in the <code>add_dependencies()</code> command. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0045</h3>
<p>Error on non-existent target in get_target_property. </p>
<p> In CMake 2.8.12 and lower, the <code>get_target_property()</code> command accepted a non-existent target argument without issuing any error or warning. The result variable is set to a <code>-NOTFOUND</code> value. </p>
<p> The <code>OLD</code> behavior for this policy is to issue no warning and set the result variable to a <code>-NOTFOUND</code> value. The <code>NEW</code> behavior for this policy is to issue a <code>FATAL_ERROR</code> if the command is called with a non-existent target. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0044</h3>
<p>Case sensitive <code>&lt;LANG&gt;_COMPILER_ID</code> generator expressions </p>
<p> CMake 2.8.12 introduced the <code>&lt;LANG&gt;_COMPILER_ID</code> <code>generator expressions</code> to allow comparison of the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> with a test value. The possible valid values are lowercase, but the comparison with the test value was performed case-insensitively. </p>
<p> The <code>OLD</code> behavior for this policy is to perform a case-insensitive comparison with the value in the <code>&lt;LANG&gt;_COMPILER_ID</code> expression. The <code>NEW</code> behavior for this policy is to perform a case-sensitive comparison with the value in the <code>&lt;LANG&gt;_COMPILER_ID</code> expression. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0043</h3>
<p>Ignore COMPILE_DEFINITIONS_&lt;Config&gt; properties </p>
<p> CMake 2.8.12 and lower allowed setting the <code>COMPILE_DEFINITIONS_&lt;CONFIG&gt;</code> target property and <code>COMPILE_DEFINITIONS_&lt;CONFIG&gt;</code> directory property to apply configuration-specific compile definitions. </p>
<p> Since CMake 2.8.10, the <code>COMPILE_DEFINITIONS</code> property has supported <code>generator expressions</code> for setting configuration-dependent content. The continued existence of the suffixed variables is redundant, and causes a maintenance burden. Population of the <code>COMPILE_DEFINITIONS_DEBUG</code> property may be replaced with a population of <code>COMPILE_DEFINITIONS</code> directly or via <code>target_compile_definitions()</code>: </p>
<pre># Old Interfaces:
set_property(TARGET tgt APPEND PROPERTY
 COMPILE_DEFINITIONS_DEBUG DEBUG_MODE
)
set_property(DIRECTORY APPEND PROPERTY
 COMPILE_DEFINITIONS_DEBUG DIR_DEBUG_MODE
)
# New Interfaces:
set_property(TARGET tgt APPEND PROPERTY
 COMPILE_DEFINITIONS $&lt;$&lt;CONFIG:Debug&gt;:DEBUG_MODE&gt;
)
target_compile_definitions(tgt PRIVATE $&lt;$&lt;CONFIG:Debug&gt;:DEBUG_MODE&gt;)
set_property(DIRECTORY APPEND PROPERTY
 COMPILE_DEFINITIONS $&lt;$&lt;CONFIG:Debug&gt;:DIR_DEBUG_MODE&gt;
)</pre>
<p>The <code>OLD</code> behavior for this policy is to consume the content of the suffixed <code>COMPILE_DEFINITIONS_&lt;CONFIG&gt;</code> target property when generating the compilation command. The <code>NEW</code> behavior for this policy is to ignore the content of the <code>COMPILE_DEFINITIONS_&lt;CONFIG&gt;</code> target property . </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0042</h3>
<p><code>MACOSX_RPATH</code> is enabled by default. </p>
<p> CMake 2.8.12 and newer has support for using <code>@rpath</code> in a target&#8217;s install name. This was enabled by setting the target property <code>MACOSX_RPATH</code>. The <code>@rpath</code> in an install name is a more flexible and powerful mechanism than <code>@executable_path</code> or <code>@loader_path</code> for locating shared libraries. </p>
<p> CMake 3.0 and later prefer this property to be ON by default. Projects wanting <code>@rpath</code> in a target&#8217;s install name may remove any setting of the <code>INSTALL_NAME_DIR</code> and <code>CMAKE_INSTALL_NAME_DIR</code> variables. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0041</h3>
<p>Error on relative include with generator expression. </p>
<p> Diagnostics in CMake 2.8.12 and lower silently ignored an entry in the <code>INTERFACE_INCLUDE_DIRECTORIES</code> of a target if it contained a generator expression at any position. </p>
<p> The path entries in that target property should not be relative. High-level API should ensure that by adding either a source directory or a install directory prefix, as appropriate. </p>
<p> As an additional diagnostic, the <code>INTERFACE_INCLUDE_DIRECTORIES</code> generated on an <code>IMPORTED</code> target for the install location should not contain paths in the source directory or the build directory. </p>
<p> The <code>OLD</code> behavior for this policy is to ignore relative path entries if they contain a generator expression. The <code>NEW</code> behavior for this policy is to report an error if a generator expression appears in another location and the path is relative. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0040</h3>
<p>The target in the <code>TARGET</code> signature of <code>add_custom_command()</code> must exist and must be defined in the current directory. </p>
<p> CMake 2.8.12 and lower silently ignored a custom command created with the <code>TARGET</code> signature of <code>add_custom_command()</code> if the target is unknown or was defined outside the current directory. </p>
<p> The <code>OLD</code> behavior for this policy is to ignore custom commands for unknown targets. The <code>NEW</code> behavior for this policy is to report an error if the target referenced in <code>add_custom_command()</code> is unknown or was defined outside the current directory. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0039</h3>
<p>Utility targets may not have link dependencies. </p>
<p> CMake 2.8.12 and lower allowed using utility targets in the left hand side position of the <code>target_link_libraries()</code> command. This is an indicator of a bug in user code. </p>
<p> The <code>OLD</code> behavior for this policy is to ignore attempts to set the link libraries of utility targets. The <code>NEW</code> behavior for this policy is to report an error if an attempt is made to set the link libraries of a utility target. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0038</h3>
<p>Targets may not link directly to themselves. </p>
<p> CMake 2.8.12 and lower allowed a build target to link to itself directly with a <code>target_link_libraries()</code> call. This is an indicator of a bug in user code. </p>
<p> The <code>OLD</code> behavior for this policy is to ignore targets which list themselves in their own link implementation. The <code>NEW</code> behavior for this policy is to report an error if a target attempts to link to itself. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0037</h3>
<p>Target names should not be reserved and should match a validity pattern. </p>
<p> CMake 2.8.12 and lower allowed creating targets using <code>add_library()</code>, <code>add_executable()</code> and <code>add_custom_target()</code> with unrestricted choice for the target name. Newer cmake features such as <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> and some diagnostics expect target names to match a restricted pattern. </p>
<p> Target names may contain upper and lower case letters, numbers, the underscore character (<code>_</code>), dot(<code>.</code>), plus(<code>+</code>) and minus(<code>&#8211;</code>). As a special case, <code>ALIAS</code> and <code>IMPORTED</code> targets may contain two consecutive colons. </p>
<p> Target names reserved by one or more CMake generators are not allowed. Among others these include <code>all</code>, <code>clean</code>, <code>help</code>, and <code>install</code>. </p>
<p> Target names associated with optional features, such as <code>test</code> and <code>package</code>, may also be reserved. CMake 3.10 and below always reserve them. CMake 3.11 and above reserve them only when the corresponding feature is enabled (e.g. by including the <code>CTest</code> or <code>CPack</code> modules). </p>
<p> The <code>OLD</code> behavior for this policy is to allow creating targets with reserved names or which do not match the validity pattern. The <code>NEW</code> behavior for this policy is to report an error if an add_* command is used with an invalid target name. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0036</h3>
<p>The <code>build_name()</code> command should not be called. </p>
<p> This command was added in May 2001 to compute a name for the current operating system and compiler combination. The command has long been documented as discouraged and replaced by the <code>CMAKE_SYSTEM</code> and <code>CMAKE_&lt;LANG&gt;_COMPILER</code> variables. </p>
<p> CMake &gt;= 3.0 prefer that this command never be called. The <code>OLD</code> behavior for this policy is to allow the command to be called. The <code>NEW</code> behavior for this policy is to issue a <code>FATAL_ERROR</code> when the command is called. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0035</h3>
<p>The <code>variable_requires()</code> command should not be called. </p>
<p> This command was introduced in November 2001 to perform some conditional logic. It has long been replaced by the <code>if()</code> command. </p>
<p> CMake &gt;= 3.0 prefer that this command never be called. The <code>OLD</code> behavior for this policy is to allow the command to be called. The <code>NEW</code> behavior for this policy is to issue a <code>FATAL_ERROR</code> when the command is called. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0034</h3>
<p>The <code>utility_source()</code> command should not be called. </p>
<p> This command was introduced in March 2001 to help build executables used to generate other files. This approach has long been replaced by <code>add_executable()</code> combined with <code>add_custom_command()</code>. </p>
<p> CMake &gt;= 3.0 prefer that this command never be called. The <code>OLD</code> behavior for this policy is to allow the command to be called. The <code>NEW</code> behavior for this policy is to issue a <code>FATAL_ERROR</code> when the command is called. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0033</h3>
<p>The <code>export_library_dependencies()</code> command should not be called. </p>
<p> This command was added in January 2003 to export <code>&lt;tgt&gt;_LIB_DEPENDS</code> internal CMake cache entries to a file for installation with a project. This was used at the time to allow transitive link dependencies to work for applications outside of the original build tree of a project. The functionality has been superseded by the <code>export()</code> and <code>install(EXPORT)</code> commands. </p>
<p> CMake &gt;= 3.0 prefer that this command never be called. The <code>OLD</code> behavior for this policy is to allow the command to be called. The <code>NEW</code> behavior for this policy is to issue a <code>FATAL_ERROR</code> when the command is called. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0032</h3>
<p>The <code>output_required_files()</code> command should not be called. </p>
<p> This command was added in June 2001 to expose the then-current CMake implicit dependency scanner. CMake&#8217;s real implicit dependency scanner has evolved since then but is not exposed through this command. The scanning capabilities of this command are very limited and this functionality is better achieved through dedicated outside tools. </p>
<p> CMake &gt;= 3.0 prefer that this command never be called. The <code>OLD</code> behavior for this policy is to allow the command to be called. The <code>NEW</code> behavior for this policy is to issue a <code>FATAL_ERROR</code> when the command is called. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0031</h3>
<p>The <code>load_command()</code> command should not be called. </p>
<p> This command was added in August 2002 to allow projects to add arbitrary commands implemented in C or C++. However, it does not work when the toolchain in use does not match the ABI of the CMake process. It has been mostly superseded by the <code>macro()</code> and <code>function()</code> commands. </p>
<p> CMake &gt;= 3.0 prefer that this command never be called. The <code>OLD</code> behavior for this policy is to allow the command to be called. The <code>NEW</code> behavior for this policy is to issue a <code>FATAL_ERROR</code> when the command is called. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0030</h3>
<p>The <code>use_mangled_mesa()</code> command should not be called. </p>
<p> This command was created in September 2001 to support VTK before modern CMake language and custom command capabilities. VTK has not used it in years. </p>
<p> CMake &gt;= 3.0 prefer that this command never be called. The <code>OLD</code> behavior for this policy is to allow the command to be called. The <code>NEW</code> behavior for this policy is to issue a <code>FATAL_ERROR</code> when the command is called. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0029</h3>
<p>The <code>subdir_depends()</code> command should not be called. </p>
<p> The implementation of this command has been empty since December 2001 but was kept in CMake for compatibility for a long time. </p>
<p> CMake &gt;= 3.0 prefer that this command never be called. The <code>OLD</code> behavior for this policy is to allow the command to be called. The <code>NEW</code> behavior for this policy is to issue a <code>FATAL_ERROR</code> when the command is called. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0028</h3>
<p>Double colon in target name means <code>ALIAS</code> or <code>IMPORTED</code> target. </p>
<p> CMake 2.8.12 and lower allowed the use of targets and files with double colons in <code>target_link_libraries()</code>, with some buildsystem generators. </p>
<p> The use of double-colons is a common pattern used to namespace <code>IMPORTED</code> targets and <code>ALIAS</code> targets. When computing the link dependencies of a target, the name of each dependency could either be a target, or a file on disk. Previously, if a target was not found with a matching name, the name was considered to refer to a file on disk. This can lead to confusing error messages if there is a typo in what should be a target name. </p>
<p> The <code>OLD</code> behavior for this policy is to search for targets, then files on disk, even if the search term contains double-colons. The <code>NEW</code> behavior for this policy is to issue a <code>FATAL_ERROR</code> if a link dependency contains double-colons but is not an <code>IMPORTED</code> target or an <code>ALIAS</code> target. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0027</h3>
<p>Conditionally linked imported targets with missing include directories. </p>
<p> CMake 2.8.11 introduced introduced the concept of <code>INTERFACE_INCLUDE_DIRECTORIES</code>, and a check at cmake time that the entries in the <code>INTERFACE_INCLUDE_DIRECTORIES</code> of an <code>IMPORTED</code> target actually exist. CMake 2.8.11 also introduced generator expression support in the <code>target_link_libraries()</code> command. However, if an imported target is linked as a result of a generator expression evaluation, the entries in the <code>INTERFACE_INCLUDE_DIRECTORIES</code> of that target were not checked for existence as they should be. </p>
<p> The <code>OLD</code> behavior of this policy is to report a warning if an entry in the <code>INTERFACE_INCLUDE_DIRECTORIES</code> of a generator-expression conditionally linked <code>IMPORTED</code> target does not exist. </p>
<p> The <code>NEW</code> behavior of this policy is to report an error if an entry in the <code>INTERFACE_INCLUDE_DIRECTORIES</code> of a generator-expression conditionally linked <code>IMPORTED</code> target does not exist. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0026</h3>
<p>Disallow use of the LOCATION property for build targets. </p>
<p> CMake 2.8.12 and lower allowed reading the <code>LOCATION</code> target property (and configuration-specific variants) to determine the eventual location of build targets. This relies on the assumption that all necessary information is available at configure-time to determine the final location and filename of the target. However, this property is not fully determined until later at generate-time. At generate time, the <code>$&lt;TARGET_FILE&gt;</code> generator expression can be used to determine the eventual <code>LOCATION</code> of a target output. </p>
<p> Code which reads the <code>LOCATION</code> target property can be ported to use the <code>$&lt;TARGET_FILE&gt;</code> generator expression together with the <code>file(GENERATE)</code> subcommand to generate a file containing the target location. </p>
<p> The <code>OLD</code> behavior for this policy is to allow reading the <code>LOCATION</code> properties from build-targets. The <code>NEW</code> behavior for this policy is to not to allow reading the <code>LOCATION</code> properties from build-targets. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0025</h3>
<p>Compiler id for Apple Clang is now <code>AppleClang</code>. </p>
<p> CMake 3.0 and above recognize that Apple Clang is a different compiler than upstream Clang and that they have different version numbers. CMake now prefers to present this to projects by setting the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable to <code>AppleClang</code> instead of <code>Clang</code>. However, existing projects may assume the compiler id for Apple Clang is just <code>Clang</code> as it was in CMake versions prior to 3.0. Therefore this policy determines for Apple Clang which compiler id to report in the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable after language <code>&lt;LANG&gt;</code> is enabled by the <code>project()</code> or <code>enable_language()</code> command. The policy must be set prior to the invocation of either command. </p>
<p> The <code>OLD</code> behavior for this policy is to use compiler id <code>Clang</code>. The <code>NEW</code> behavior for this policy is to use compiler id <code>AppleClang</code>. </p>
<p> This policy was introduced in CMake version 3.0. Use the <code>cmake_policy()</code> command to set this policy to <code>OLD</code> or <code>NEW</code> explicitly. Unlike most policies, CMake version 3.22.1 does <i>not</i> warn by default when this policy is not set and simply uses <code>OLD</code> behavior. See documentation of the <code>CMAKE_POLICY_WARNING_CMP0025</code> variable to control the warning. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0024</h3>
<p>Disallow include export result. </p>
<p> CMake 2.8.12 and lower allowed use of the <code>include()</code> command with the result of the <code>export()</code> command. This relies on the assumption that the <code>export()</code> command has an immediate effect at configure-time during a cmake run. Certain properties of targets are not fully determined until later at generate-time, such as the link language and complete list of link libraries. Future refactoring will change the effect of the <code>export()</code> command to be executed at generate-time. Use <code>ALIAS</code> targets instead in cases where the goal is to refer to targets by another name. </p>
<p> The <code>OLD</code> behavior for this policy is to allow including the result of an <code>export()</code> command. The <code>NEW</code> behavior for this policy is not to allow including the result of an <code>export()</code> command. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 2.8</h2>
<h3>Cmp0023</h3>
<p>Plain and keyword <code>target_link_libraries()</code> signatures cannot be mixed. </p>
<p> CMake 2.8.12 introduced the <code>target_link_libraries()</code> signature using the <code>PUBLIC</code>, <code>PRIVATE</code>, and <code>INTERFACE</code> keywords to generalize the <code>LINK_PUBLIC</code> and <code>LINK_PRIVATE</code> keywords introduced in CMake 2.8.7. Use of signatures with any of these keywords sets the link interface of a target explicitly, even if empty. This produces confusing behavior when used in combination with the historical behavior of the plain <code>target_link_libraries()</code> signature. For example, consider the code: </p>
<pre>target_link_libraries(mylib A)
target_link_libraries(mylib PRIVATE B)</pre>
<p>After the first line the link interface has not been set explicitly so CMake would use the link implementation, A, as the link interface. However, the second line sets the link interface to empty. In order to avoid this subtle behavior CMake now prefers to disallow mixing the plain and keyword signatures of <code>target_link_libraries()</code> for a single target. </p>
<p> The <code>OLD</code> behavior for this policy is to allow keyword and plain <code>target_link_libraries()</code> signatures to be mixed. The <code>NEW</code> behavior for this policy is to not to allow mixing of the keyword and plain signatures. </p>
<p> This policy was introduced in CMake version 2.8.12. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0022</h3>
<p><code>INTERFACE_LINK_LIBRARIES</code> defines the link interface. </p>
<p> CMake 2.8.11 constructed the &#8216;link interface&#8217; of a target from properties matching <code>(IMPORTED_)?LINK_INTERFACE_LIBRARIES(_&lt;CONFIG&gt;)?</code>. The modern way to specify config-sensitive content is to use generator expressions and the <code>IMPORTED_</code> prefix makes uniform processing of the link interface with generator expressions impossible. The <code>INTERFACE_LINK_LIBRARIES</code> target property was introduced as a replacement in CMake 2.8.12. This new property is named consistently with the <code>INTERFACE_COMPILE_DEFINITIONS</code>, <code>INTERFACE_INCLUDE_DIRECTORIES</code> and <code>INTERFACE_COMPILE_OPTIONS</code> properties. For in-build targets, CMake will use the INTERFACE_LINK_LIBRARIES property as the source of the link interface only if policy <code>CMP0022</code> is <code>NEW</code>. When exporting a target which has this policy set to <code>NEW</code>, only the <code>INTERFACE_LINK_LIBRARIES</code> property will be processed and generated for the <code>IMPORTED</code> target by default. A new option to the <code>install(EXPORT)</code> and export commands allows export of the old-style properties for compatibility with downstream users of CMake versions older than 2.8.12. The <code>target_link_libraries()</code> command will no longer populate the properties matching <code>LINK_INTERFACE_LIBRARIES(_&lt;CONFIG&gt;)?</code> if this policy is <code>NEW</code>. </p>
<p> Warning-free future-compatible code which works with CMake 2.8.7 onwards can be written by using the <code>LINK_PRIVATE</code> and <code>LINK_PUBLIC</code> keywords of <code>target_link_libraries()</code>. </p>
<p> The <code>OLD</code> behavior for this policy is to ignore the <code>INTERFACE_LINK_LIBRARIES</code> property for in-build targets. The <code>NEW</code> behavior for this policy is to use the <code>INTERFACE_LINK_LIBRARIES</code> property for in-build targets, and ignore the old properties matching <code>(IMPORTED_)?LINK_INTERFACE_LIBRARIES(_&lt;CONFIG&gt;)?</code>. </p>
<p> This policy was introduced in CMake version 2.8.12. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0021</h3>
<p>Fatal error on relative paths in <code>INCLUDE_DIRECTORIES</code> target property. </p>
<p> CMake 2.8.10.2 and lower allowed the <code>INCLUDE_DIRECTORIES</code> target property to contain relative paths. The base path for such relative entries is not well defined. CMake 2.8.12 issues a <code>FATAL_ERROR</code> if the <code>INCLUDE_DIRECTORIES</code> property contains a relative path. </p>
<p> The <code>OLD</code> behavior for this policy is not to warn about relative paths in the <code>INCLUDE_DIRECTORIES</code> target property. The <code>NEW</code> behavior for this policy is to issue a <code>FATAL_ERROR</code> if <code>INCLUDE_DIRECTORIES</code> contains a relative path. </p>
<p> This policy was introduced in CMake version 2.8.12. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0020</h3>
<p>Automatically link Qt executables to <code>qtmain</code> target on Windows. </p>
<p> CMake 2.8.10 and lower required users of Qt to always specify a link dependency to the <code>qtmain.lib</code> static library manually on Windows. CMake 2.8.11 gained the ability to evaluate generator expressions while determining the link dependencies from <code>IMPORTED</code> targets. This allows CMake itself to automatically link executables which link to Qt to the <code>qtmain.lib</code> library when using <code>IMPORTED</code> Qt targets. For applications already linking to <code>qtmain.lib</code>, this should have little impact. For applications which supply their own alternative WinMain implementation and for applications which use the QAxServer library, this automatic linking will need to be disabled as per the documentation. </p>
<p> The <code>OLD</code> behavior for this policy is not to link executables to <code>qtmain.lib</code> automatically when they link to the QtCore <code>IMPORTED</code> target. The <code>NEW</code> behavior for this policy is to link executables to <code>qtmain.lib</code> automatically when they link to QtCore <code>IMPORTED</code> target. </p>
<p> This policy was introduced in CMake version 2.8.11. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0019</h3>
<p>Do not re-expand variables in include and link information. </p>
<p> CMake 2.8.10 and lower re-evaluated values given to the include_directories, link_directories, and link_libraries commands to expand any leftover variable references at the end of the configuration step. This was for strict compatibility with VERY early CMake versions because all variable references are now normally evaluated during CMake language processing. CMake 2.8.11 and higher prefer to skip the extra evaluation. </p>
<p> The <code>OLD</code> behavior for this policy is to re-evaluate the values for strict compatibility. The <code>NEW</code> behavior for this policy is to leave the values untouched. </p>
<p> This policy was introduced in CMake version 2.8.11. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0018</h3>
<p>Ignore <code>CMAKE_SHARED_LIBRARY_&lt;Lang&gt;_FLAGS</code> variable. </p>
<p> CMake 2.8.8 and lower compiled sources in <code>SHARED</code> and <code>MODULE</code> libraries using the value of the undocumented <code>CMAKE_SHARED_LIBRARY_&lt;Lang&gt;_FLAGS</code> platform variable. The variable contained platform-specific flags needed to compile objects for shared libraries. Typically it included a flag such as <code>-fPIC</code> for position independent code but also included other flags needed on certain platforms. CMake 2.8.9 and higher prefer instead to use the <code>POSITION_INDEPENDENT_CODE</code> target property to determine what targets should be position independent, and new undocumented platform variables to select flags while ignoring <code>CMAKE_SHARED_LIBRARY_&lt;Lang&gt;_FLAGS</code> completely. </p>
<p> The default for either approach produces identical compilation flags, but if a project modifies <code>CMAKE_SHARED_LIBRARY_&lt;Lang&gt;_FLAGS</code> from its original value this policy determines which approach to use. </p>
<p> The <code>OLD</code> behavior for this policy is to ignore the <code>POSITION_INDEPENDENT_CODE</code> property for all targets and use the modified value of <code>CMAKE_SHARED_LIBRARY_&lt;Lang&gt;_FLAGS</code> for <code>SHARED</code> and <code>MODULE</code> libraries. </p>
<p> The <code>NEW</code> behavior for this policy is to ignore <code>CMAKE_SHARED_LIBRARY_&lt;Lang&gt;_FLAGS</code> whether it is modified or not and honor the <code>POSITION_INDEPENDENT_CODE</code> target property. </p>
<p> This policy was introduced in CMake version 2.8.9. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0017</h3>
<p>Prefer files from the CMake module directory when including from there. </p>
<p> Starting with CMake 2.8.4, if a cmake-module shipped with CMake (i.e. located in the CMake module directory) calls <code>include()</code> or <code>find_package()</code>, the files located in the CMake module directory are preferred over the files in <code>CMAKE_MODULE_PATH</code>. This makes sure that the modules belonging to CMake always get those files included which they expect, and against which they were developed and tested. In all other cases, the files found in <code>CMAKE_MODULE_PATH</code> still take precedence over the ones in the CMake module directory. The <code>OLD</code> behavior is to always prefer files from CMAKE_MODULE_PATH over files from the CMake modules directory. </p>
<p> This policy was introduced in CMake version 2.8.4. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0016</h3>
<p><code>target_link_libraries()</code> reports error if its only argument is not a target. </p>
<p> In CMake 2.8.2 and lower the <code>target_link_libraries()</code> command silently ignored if it was called with only one argument, and this argument wasn&#8217;t a valid target. In CMake 2.8.3 and above it reports an error in this case. </p>
<p> This policy was introduced in CMake version 2.8.3. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0015</h3>
<p><code>link_directories()</code> treats paths relative to the source dir. </p>
<p> In CMake 2.8.0 and lower the <code>link_directories()</code> command passed relative paths unchanged to the linker. In CMake 2.8.1 and above the <code>link_directories()</code> command prefers to interpret relative paths with respect to <code>CMAKE_CURRENT_SOURCE_DIR</code>, which is consistent with <code>include_directories()</code> and other commands. The <code>OLD</code> behavior for this policy is to use relative paths verbatim in the linker command. The <code>NEW</code> behavior for this policy is to convert relative paths to absolute paths by appending the relative path to <code>CMAKE_CURRENT_SOURCE_DIR</code>. </p>
<p> This policy was introduced in CMake version 2.8.1. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0014</h3>
<p>Input directories must have <code>CMakeLists.txt</code>. </p>
<p> CMake versions before 2.8 silently ignored missing <code>CMakeLists.txt</code> files in directories referenced by <code>add_subdirectory()</code> or <code>subdirs()</code>, treating them as if present but empty. In CMake 2.8.0 and above this <code>cmake_policy()</code> determines whether or not the case is an error. The <code>OLD</code> behavior for this policy is to silently ignore the problem. The <code>NEW</code> behavior for this policy is to report an error. </p>
<p> This policy was introduced in CMake version 2.8.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0013</h3>
<p>Duplicate binary directories are not allowed. </p>
<p> CMake 2.6.3 and below silently permitted add_subdirectory() calls to create the same binary directory multiple times. During build system generation files would be written and then overwritten in the build tree and could lead to strange behavior. CMake 2.6.4 and above explicitly detect duplicate binary directories. CMake 2.6.4 always considers this case an error. In CMake 2.8.0 and above this policy determines whether or not the case is an error. The <code>OLD</code> behavior for this policy is to allow duplicate binary directories. The NEW behavior for this policy is to disallow duplicate binary directories with an error. </p>
<p> This policy was introduced in CMake version 2.8.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0012</h3>
<p><code>if()</code> recognizes numbers and boolean constants. </p>
<p> In CMake versions 2.6.4 and lower the <code>if()</code> command implicitly dereferenced arguments corresponding to variables, even those named like numbers or boolean constants, except for <code>0</code> and <code>1</code>. Numbers and boolean constants such as <code>true</code>, <code>false</code>, <code>yes</code>, <code>no</code>, <code>on</code>, <code>off</code>, <code>y</code>, <code>n</code>, <code>notfound</code>, <code>ignore</code> (all case insensitive) were recognized in some cases but not all. For example, the code <code>if(TRUE)</code> might have evaluated as <code>false</code>. Numbers such as 2 were recognized only in boolean expressions like <code>if(NOT 2)</code> (leading to <code>false</code>) but not as a single-argument like <code><a href="/docs/linux/man/2-if/">if</a>(2)</code> (also leading to <code>false</code>). Later versions of CMake prefer to treat numbers and boolean constants literally, so they should not be used as variable names. </p>
<p> The <code>OLD</code> behavior for this policy is to implicitly dereference variables named like numbers and boolean constants. The <code>NEW</code> behavior for this policy is to recognize numbers and boolean constants without dereferencing variables with such names. </p>
<p> This policy was introduced in CMake version 2.8.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 2.6</h2>
<h3>Cmp0011</h3>
<p>Included scripts do automatic <code>cmake_policy()</code> PUSH and POP. </p>
<p> In CMake 2.6.2 and below, CMake Policy settings in scripts loaded by the <code>include()</code> and <code>find_package()</code> commands would affect the includer. Explicit invocations of <code>cmake_policy(PUSH)</code> and <code>cmake_policy(POP)</code> were required to isolate policy changes and protect the includer. While some scripts intend to affect the policies of their includer, most do not. In CMake 2.6.3 and above, <code>include()</code> and <code>find_package()</code> by default <code>PUSH</code> and <code>POP</code> an entry on the policy stack around an included script, but provide a <code>NO_POLICY_SCOPE</code> option to disable it. This policy determines whether or not to imply <code>NO_POLICY_SCOPE</code> for compatibility. The <code>OLD</code> behavior for this policy is to imply <code>NO_POLICY_SCOPE</code> for <code>include()</code> and <code>find_package()</code> commands. The <code>NEW</code> behavior for this policy is to allow the commands to do their default cmake_policy <code>PUSH</code> and <code>POP</code>. </p>
<p> This policy was introduced in CMake version 2.6.3. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0010</h3>
<p>Bad variable reference syntax is an error. </p>
<p> In CMake 2.6.2 and below, incorrect variable reference syntax such as a missing close-brace (<code>${FOO</code>) was reported but did not stop processing of CMake code. This policy determines whether a bad variable reference is an error. The <code>OLD</code> behavior for this policy is to warn about the error, leave the string untouched, and continue. The <code>NEW</code> behavior for this policy is to report an error. </p>
<p> If <code>CMP0053</code> is set to <code>NEW</code>, this policy has no effect and is treated as always being <code>NEW</code>. </p>
<p> This policy was introduced in CMake version 2.6.3. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0009</h3>
<p>FILE GLOB_RECURSE calls should not follow symlinks by default. </p>
<p> In CMake 2.6.1 and below, <code>file(GLOB_RECURSE)</code> calls would follow through symlinks, sometimes coming up with unexpectedly large result sets because of symlinks to top level directories that contain hundreds of thousands of files. </p>
<p> This policy determines whether or not to follow symlinks encountered during a <code>file(GLOB_RECURSE)</code> call. The <code>OLD</code> behavior for this policy is to follow the symlinks. The <code>NEW</code> behavior for this policy is not to follow the symlinks by default, but only if <code>FOLLOW_SYMLINKS</code> is given as an additional argument to the <code>FILE</code> command. </p>
<p> This policy was introduced in CMake version 2.6.2. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0008</h3>
<p>Libraries linked by full-path must have a valid library file name. </p>
<p> In CMake 2.4 and below it is possible to write code like </p>
<pre>target_link_libraries(myexe /full/path/to/somelib)</pre>
<p>where <code>somelib</code> is supposed to be a valid library file name such as <code>libsomelib.a</code> or <code>somelib.lib</code>. For Makefile generators this produces an error at build time because the dependency on the full path cannot be found. For Visual Studio Generators IDE and <code>Xcode</code> generators this used to work by accident because CMake would always split off the library directory and ask the linker to search for the library by name (<code>-lsomelib</code> or <code>somelib.lib</code>). Despite the failure with Makefiles, some projects have code like this and build only with Visual Studio and/or Xcode. This version of CMake prefers to pass the full path directly to the native build tool, which will fail in this case because it does not name a valid library file. </p>
<p> This policy determines what to do with full paths that do not appear to name a valid library file. The <code>OLD</code> behavior for this policy is to split the library name from the path and ask the linker to search for it. The <code>NEW</code> behavior for this policy is to trust the given path and pass it directly to the native build tool unchanged. </p>
<p> This policy was introduced in CMake version 2.6.1. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0007</h3>
<p>list command no longer ignores empty elements. </p>
<p> This policy determines whether the list command will ignore empty elements in the list. CMake 2.4 and below list commands ignored all empty elements in the list. For example, <code>a;b;;c</code> would have length 3 and not 4. The <code>OLD</code> behavior for this policy is to ignore empty list elements. The <code>NEW</code> behavior for this policy is to correctly count empty elements in a list. </p>
<p> This policy was introduced in CMake version 2.6.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0006</h3>
<p>Installing <code>MACOSX_BUNDLE</code> targets requires a <code>BUNDLE DESTINATION</code>. </p>
<p> This policy determines whether the <code>install(TARGETS)</code> command must be given a <code>BUNDLE DESTINATION</code> when asked to install a target with the <code>MACOSX_BUNDLE</code> property set. CMake 2.4 and below did not distinguish application bundles from normal executables when installing targets. CMake 2.6 provides a <code>BUNDLE</code> option to the <code>install(TARGETS)</code> command that specifies rules specific to application bundles on the Mac. Projects should use this option when installing a target with the <code>MACOSX_BUNDLE</code> property set. </p>
<p> The <code>OLD</code> behavior for this policy is to fall back to the <code>RUNTIME DESTINATION</code> if a <code>BUNDLE DESTINATION</code> is not given. The <code>NEW</code> behavior for this policy is to produce an error if a bundle target is installed without a <code>BUNDLE DESTINATION</code>. </p>
<p> This policy was introduced in CMake version 2.6.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0005</h3>
<p>Preprocessor definition values are now escaped automatically. </p>
<p> This policy determines whether or not CMake should generate escaped preprocessor definition values added via add_definitions. CMake versions 2.4 and below assumed that only trivial values would be given for macros in add_definitions calls. It did not attempt to escape non-trivial values such as string literals in generated build rules. CMake versions 2.6 and above support escaping of most values, but cannot assume the user has not added escapes already in an attempt to work around limitations in earlier versions. </p>
<p> The <code>OLD</code> behavior for this policy is to place definition values given to add_definitions directly in the generated build rules without attempting to escape anything. The <code>NEW</code> behavior for this policy is to generate correct escapes for all native build tools automatically. See documentation of the <code>COMPILE_DEFINITIONS</code> target property for limitations of the escaping implementation. </p>
<p> This policy was introduced in CMake version 2.6.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0004</h3>
<p>Libraries linked may not have leading or trailing whitespace. </p>
<p> CMake versions 2.4 and below silently removed leading and trailing whitespace from libraries linked with code like </p>
<pre>target_link_libraries(myexe &quot; A &quot;)</pre>
<p>This could lead to subtle errors in user projects. </p>
<p> The <code>OLD</code> behavior for this policy is to silently remove leading and trailing whitespace. The <code>NEW</code> behavior for this policy is to diagnose the existence of such whitespace as an error. The setting for this policy used when checking the library names is that in effect when the target is created by an <code>add_executable()</code> or <code>add_library()</code> command. </p>
<p> This policy was introduced in CMake version 2.6.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0003</h3>
<p>Libraries linked via full path no longer produce linker search paths. </p>
<p> This policy affects how libraries whose full paths are NOT known are found at link time, but was created due to a change in how CMake deals with libraries whose full paths are known. Consider the code </p>
<pre>target_link_libraries(myexe /path/to/libA.so)</pre>
<p>CMake 2.4 and below implemented linking to libraries whose full paths are known by splitting them on the link line into separate components consisting of the linker search path and the library name. The example code might have produced something like </p>
<pre>... -L/path/to -lA ...</pre>
<p>in order to link to library A. An analysis was performed to order multiple link directories such that the linker would find library A in the desired location, but there are cases in which this does not work. CMake versions 2.6 and above use the more reliable approach of passing the full path to libraries directly to the linker in most cases. The example code now produces something like </p>
<pre>... /path/to/libA.so ....</pre>
<p>Unfortunately this change can break code like </p>
<pre>target_link_libraries(myexe /path/to/libA.so B)</pre>
<p>where <code>B</code> is meant to find <code>/path/to/libB.so</code>. This code is wrong because the user is asking the linker to find library B but has not provided a linker search path (which may be added with the link_directories command). However, with the old linking implementation the code would work accidentally because the linker search path added for library A allowed library B to be found. </p>
<p> In order to support projects depending on linker search paths added by linking to libraries with known full paths, the <code>OLD</code> behavior for this policy will add the linker search paths even though they are not needed for their own libraries. When this policy is set to <code>OLD</code>, CMake will produce a link line such as </p>
<pre>... -L/path/to /path/to/libA.so -lB ...</pre>
<p>which will allow library B to be found as it was previously. When this policy is set to NEW, CMake will produce a link line such as </p>
<pre>... /path/to/libA.so -lB ...</pre>
<p>which more accurately matches what the project specified. </p>
<p> The setting for this policy used when generating the link line is that in effect when the target is created by an add_executable or add_library command. For the example described above, the code </p>
<pre>cmake_policy(SET CMP0003 OLD) # or cmake_policy(VERSION 2.4)
add_executable(myexe myexe.c)
target_link_libraries(myexe /path/to/libA.so B)</pre>
<p>will work and suppress the warning for this policy. It may also be updated to work with the corrected linking approach: </p>
<pre>cmake_policy(SET CMP0003 NEW) # or cmake_policy(VERSION 2.6)
link_directories(/path/to) # needed to find library B
add_executable(myexe myexe.c)
target_link_libraries(myexe /path/to/libA.so B)</pre>
<p>Even better, library B may be specified with a full path: </p>
<pre>add_executable(myexe myexe.c)
target_link_libraries(myexe /path/to/libA.so /path/to/libB.so)</pre>
<p>When all items on the link line have known paths CMake does not check this policy so it has no effect. </p>
<p> Note that the warning for this policy will be issued for at most one target. This avoids flooding users with messages for every target when setting the policy once will probably fix all targets. </p>
<p> This policy was introduced in CMake version 2.6.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0002</h3>
<p>Logical target names must be globally unique. </p>
<p> Targets names created with <code>add_executable()</code>, <code>add_library()</code>, or <code>add_custom_target()</code> are logical build target names. Logical target names must be globally unique because: </p>
<pre>- Unique names may be referenced unambiguously both in CMake
 code and on make tool command lines.
- Logical names are used by Xcode and VS IDE generators
 to produce meaningful project names for the targets.</pre>
<p>The logical name of executable and library targets does not have to correspond to the physical file names built. Consider using the <code>OUTPUT_NAME</code> target property to create two targets with the same physical name while keeping logical names distinct. Custom targets must simply have globally unique names (unless one uses the global property <code>ALLOW_DUPLICATE_CUSTOM_TARGETS</code> with a Makefiles generator). </p>
<p> This policy was introduced in CMake version 2.6.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0001</h3>
<p><code>CMAKE_BACKWARDS_COMPATIBILITY</code> should no longer be used. </p>
<p> The behavior is to check <code>CMAKE_BACKWARDS_COMPATIBILITY</code> and present it to the user. The <code>NEW</code> behavior is to ignore CMAKE_BACKWARDS_COMPATIBILITY completely. </p>
<p> In CMake 2.4 and below the variable <code>CMAKE_BACKWARDS_COMPATIBILITY</code> was used to request compatibility with earlier versions of CMake. In CMake 2.6 and above all compatibility issues are handled by policies and the <code>cmake_policy()</code> command. However, CMake must still check <code>CMAKE_BACKWARDS_COMPATIBILITY</code> for projects written for CMake 2.4 and below. </p>
<p> This policy was introduced in CMake version 2.6.0. CMake version 3.22.1 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0000</h3>
<p>A minimum required CMake version must be specified. </p>
<p> CMake requires that projects specify the version of CMake to which they have been written. This policy has been put in place so users trying to build the project may be told when they need to update their CMake. Specifying a version also helps the project build with CMake versions newer than that specified. Use the <code>cmake_minimum_required()</code> command at the top of your main <code>CMakeLists.txt</code> file: </p>
<pre>cmake_minimum_required(VERSION &lt;major&gt;.&lt;minor&gt;)</pre>
<p>where <code>&lt;major&gt;.&lt;minor&gt;</code> is the version of CMake you want to support (such as <code>3.14</code>). The command will ensure that at least the given version of CMake is running and help newer versions be compatible with the project. See documentation of <code>cmake_minimum_required()</code> for details. </p>
<p> Note that the command invocation must appear in the <code>CMakeLists.txt</code> file itself; a call in an included file is not sufficient. However, the <code>cmake_policy()</code> command may be called to set policy <code>CMP0000</code> to <code>OLD</code> or <code>NEW</code> behavior explicitly. The <code>OLD</code> behavior is to silently ignore the missing invocation. The <code>NEW</code> behavior is to issue an error instead of a warning. An included file may set <code>CMP0000</code> explicitly to affect how this policy is enforced for the main <code>CMakeLists.txt</code> file. </p>
<p> This policy was introduced in CMake version 2.6.0. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Copyright</h2>
<p>2000-2022 Kitware, Inc. and Contributors</p>
