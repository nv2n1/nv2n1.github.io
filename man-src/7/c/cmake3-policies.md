---
title: "cmake3-policies(7)"
name: "cmake3-policies"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake3-policies/"
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
<h2>Policies Introduced By Cmake 3.4</h2>
<h3>Cmp0065</h3>
<p>Do not add flags to export symbols from executables without the <code>ENABLE_EXPORTS</code> target property. </p>
<p> CMake 3.3 and below, for historical reasons, always linked executables on some platforms with flags like <code>-rdynamic</code> to export symbols from the executables for use by any plugins they may load via <code>dlopen</code>. CMake 3.4 and above prefer to do this only for executables that are explicitly marked with the <code>ENABLE_EXPORTS</code> target property. </p>
<p> The <code>OLD</code> behavior of this policy is to always use the additional link flags when linking executables regardless of the value of the <code>ENABLE_EXPORTS</code> target property. </p>
<p> The <code>NEW</code> behavior of this policy is to only use the additional link flags when linking executables if the <code>ENABLE_EXPORTS</code> target property is set to <code>True</code>. </p>
<p> This policy was introduced in CMake version 3.4. Unlike most policies, CMake version 3.6.3 does <i>not</i> warn by default when this policy is not set and simply uses OLD behavior. See documentation of the <code>CMAKE_POLICY_WARNING_CMP0065</code> variable to control the warning. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0064</h3>
<p>Recognize <code>TEST</code> as a operator for the <code>if()</code> command. </p>
<p> The <code>TEST</code> operator was added to the <code>if()</code> command to determine if a given test name was created by the <code>add_test()</code> command. </p>
<p> The <code>OLD</code> behavior for this policy is to ignore the <code>TEST</code> operator. The <code>NEW</code> behavior is to interpret the <code>TEST</code> operator. </p>
<p> This policy was introduced in CMake version 3.4. CMake version 3.6.3 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 3.3</h2>
<h3>Cmp0063</h3>
<p>Honor visibility properties for all target types. </p>
<p> The <code>&lt;LANG&gt;_VISIBILITY_PRESET</code> and <code>VISIBILITY_INLINES_HIDDEN</code> target properties affect visibility of symbols during dynamic linking. When first introduced these properties affected compilation of sources only in shared libraries, module libraries, and executables with the <code>ENABLE_EXPORTS</code> property set. This was sufficient for the basic use cases of shared libraries and executables with plugins. However, some sources may be compiled as part of static libraries or object libraries and then linked into a shared library later. CMake 3.3 and above prefer to honor these properties for sources compiled in all target types. This policy preserves compatibility for projects expecting the properties to work only for some target types. </p>
<p> The <code>OLD</code> behavior for this policy is to ignore the visibility properties for static libraries, object libraries, and executables without exports. The <code>NEW</code> behavior for this policy is to honor the visibility properties for all target types. </p>
<p> This policy was introduced in CMake version 3.3. CMake version 3.6.3 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0062</h3>
<p>Disallow install() of export() result. </p>
<p> The <code>export()</code> command generates a file containing <i>Imported Targets</i>, which is suitable for use from the build directory. It is not suitable for installation because it contains absolute paths to buildsystem locations, and is particular to a single build configuration. </p>
<p> The <code>install(EXPORT)</code> generates and installs files which contain <i>Imported Targets</i>. These files are generated with relative paths (unless the user specifies absolute paths), and are designed for multi-configuration use. See <i>Creating Packages</i> for more. </p>
<p> CMake 3.3 no longer allows the use of the <code>install(FILES)</code> command with the result of the <code>export()</code> command. </p>
<p> The <code>OLD</code> behavior for this policy is to allow installing the result of an <code>export()</code> command. The <code>NEW</code> behavior for this policy is not to allow installing the result of an <code>export()</code> command. </p>
<p> This policy was introduced in CMake version 3.3. CMake version 3.6.3 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0061</h3>
<p>CTest does not by default tell <code>make</code> to ignore errors (<code>-i</code>). </p>
<p> The <code>ctest_build()</code> and <code>build_command()</code> commands no longer generate build commands for <i>Makefile Generators</i> with the <code>-i</code> option. Previously this was done to help build as much of tested projects as possible. However, this behavior is not consistent with other generators and also causes the return code of the <code>make</code> tool to be meaningless. </p>
<p> Of course users may still add this option manually by setting <code>CTEST_BUILD_COMMAND</code> or the <code>MAKECOMMAND</code> cache entry. See the <i>CTest Build Step</i> <code>MakeCommand</code> setting documentation for their effects. </p>
<p> The <code>OLD</code> behavior for this policy is to add <code>-i</code> to <code>make</code> calls in CTest. The <code>NEW</code> behavior for this policy is to not add <code>-i</code>. </p>
<p> This policy was introduced in CMake version 3.3. Unlike most policies, CMake version 3.6.3 does <i>not</i> warn when this policy is not set and simply uses OLD behavior. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0060</h3>
<p>Link libraries by full path even in implicit directories. </p>
<p> Policy <code>CMP0003</code> was introduced with the intention of always linking library files by full path when a full path is given to the <code>target_link_libraries()</code> command. However, on some platforms (e.g. HP-UX) the compiler front-end adds alternative library search paths for the current architecture (e.g. <code>/usr/lib/&lt;arch&gt;</code> has alternatives to libraries in <code>/usr/lib</code> for the current architecture). On such platforms the <code>find_library()</code> may find a library such as <code>/usr/lib/libfoo.so</code> that does not belong to the current architecture. </p>
<p> Prior to policy <code>CMP0003</code> projects would still build in such cases because the incorrect library path would be converted to <code>-lfoo</code> on the link line and the linker would find the proper library in the arch-specific search path provided by the compiler front-end implicitly. At the time we chose to remain compatible with such projects by always converting library files found in implicit link directories to <code>-lfoo</code> flags to ask the linker to search for them. This approach allowed existing projects to continue to build while still linking to libraries outside implicit link directories via full path (such as those in the build tree). </p>
<p> CMake does allow projects to override this behavior by using an <i>IMPORTED library target</i> with its <code>IMPORTED_LOCATION</code> property set to the desired full path to a library file. In fact, many <i>Find Modules</i> are learning to provide <i>Imported Targets</i> instead of just the traditional <code>Foo_LIBRARIES</code> variable listing library files. However, this makes the link line generated for a library found by a Find Module depend on whether it is linked through an imported target or not, which is inconsistent. Furthermore, this behavior has been a source of confusion because the generated link line for a library file depends on its location. It is also problematic for projects trying to link statically because flags like <code>-Wl,-Bstatic -lfoo -Wl,-Bdynamic</code> may be used to help the linker select <code>libfoo.a</code> instead of <code>libfoo.so</code> but then leak dynamic linking to following libraries. (See the <code>LINK_SEARCH_END_STATIC</code> target property for a solution typically used for that problem.) </p>
<p> When the special case for libraries in implicit link directories was first introduced the list of implicit link directories was simply hard-coded (e.g. <code>/lib</code>, <code>/usr/lib</code>, and a few others). Since that time, CMake has learned to detect the implicit link directories used by the compiler front-end. If necessary, the <code>find_library()</code> command could be taught to use this information to help find libraries of the proper architecture. </p>
<p> For these reasons, CMake 3.3 and above prefer to drop the special case and link libraries by full path even when they are in implicit link directories. Policy <code>CMP0060</code> provides compatibility for existing projects. </p>
<p> The OLD behavior for this policy is to ask the linker to search for libraries whose full paths are known to be in implicit link directories. The NEW behavior for this policy is to link libraries by full path even if they are in implicit link directories. </p>
<p> This policy was introduced in CMake version 3.3. Unlike most policies, CMake version 3.6.3 does <i>not</i> warn by default when this policy is not set and simply uses OLD behavior. See documentation of the <code>CMAKE_POLICY_WARNING_CMP0060</code> variable to control the warning. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0059</h3>
<p>Do not treat <code>DEFINITIONS</code> as a built-in directory property. </p>
<p> CMake 3.3 and above no longer make a list of definitions available through the <code>DEFINITIONS</code> directory property. The <code>COMPILE_DEFINITIONS</code> directory property may be used instead. </p>
<p> The <code>OLD</code> behavior for this policy is to provide the list of flags given so far to the <code>add_definitions()</code> command. The <code>NEW</code> behavior is to behave as a normal user-defined directory property. </p>
<p> This policy was introduced in CMake version 3.3. CMake version 3.6.3 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0058</h3>
<p>Ninja requires custom command byproducts to be explicit. </p>
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
<p> This policy was introduced in CMake version 3.3. CMake version 3.6.3 warns when it sees unknown dependencies in out-of-source build trees if the policy is not set and then uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set the policy to <code>OLD</code> or <code>NEW</code> explicitly. The policy setting must be in scope at the end of the top-level <code>CMakeLists.txt</code> file of the project and has global effect. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0057</h3>
<p>Support new <code>if()</code> IN_LIST operator. </p>
<p> CMake 3.3 adds support for the new IN_LIST operator. </p>
<p> The <code>OLD</code> behavior for this policy is to ignore the IN_LIST operator. The <code>NEW</code> behavior is to interpret the IN_LIST operator. </p>
<p> This policy was introduced in CMake version 3.3. CMake version 3.6.3 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 3.2</h2>
<h3>Cmp0056</h3>
<p>Honor link flags in <code>try_compile()</code> source-file signature. </p>
<p> The <code>try_compile()</code> command source-file signature generates a <code>CMakeLists.txt</code> file to build the source file into an executable. In order to compile the source the same way as it might be compiled by the calling project, the generated project sets the value of the <code>CMAKE_&lt;LANG&gt;_FLAGS</code> variable to that in the calling project. The value of the <code>CMAKE_EXE_LINKER_FLAGS</code> variable may be needed in some cases too, but CMake 3.1 and lower did not set it in the generated project. CMake 3.2 and above prefer to set it so that linker flags are honored as well as compiler flags. This policy provides compatibility with the pre-3.2 behavior. </p>
<p> The OLD behavior for this policy is to not set the value of the <code>CMAKE_EXE_LINKER_FLAGS</code> variable in the generated test project. The NEW behavior for this policy is to set the value of the <code>CMAKE_EXE_LINKER_FLAGS</code> variable in the test project to the same as it is in the calling project. </p>
<p> If the project code does not set the policy explicitly, users may set it on the command line by defining the <code>CMAKE_POLICY_DEFAULT_CMP0056</code> variable in the cache. </p>
<p> This policy was introduced in CMake version 3.2. Unlike most policies, CMake version 3.6.3 does <i>not</i> warn by default when this policy is not set and simply uses OLD behavior. See documentation of the <code>CMAKE_POLICY_WARNING_CMP0056</code> variable to control the warning. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0055</h3>
<p>Strict checking for the <code>break()</code> command. </p>
<p> CMake 3.1 and lower allowed calls to the <code>break()</code> command outside of a loop context and also ignored any given arguments. This was undefined behavior. </p>
<p> The OLD behavior for this policy is to allow <code>break()</code> to be placed outside of loop contexts and ignores any arguments. The NEW behavior for this policy is to issue an error if a misplaced break or any arguments are found. </p>
<p> This policy was introduced in CMake version 3.2. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 3.1</h2>
<h3>Cmp0054</h3>
<p>Only interpret <code>if()</code> arguments as variables or keywords when unquoted. </p>
<p> CMake 3.1 and above no longer implicitly dereference variables or interpret keywords in an <code>if()</code> command argument when it is a <i>Quoted Argument</i> or a <i>Bracket Argument</i>. </p>
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
<p>This policy was introduced in CMake version 3.1. CMake version 3.6.3 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0053</h3>
<p>Simplify variable reference and escape sequence evaluation. </p>
<p> CMake 3.1 introduced a much faster implementation of evaluation of the <i>Variable References</i> and <i>Escape Sequences</i> documented in the <code><a href="/docs/linux/man/7-cmake3-language/">cmake3-language</a>(7)</code> manual. While the behavior is identical to the legacy implementation in most cases, some corner cases were cleaned up to simplify the behavior. Specifically:</p>
<dl>
<dt>&bull;</p>
<dd>Expansion of <code>@VAR@</code> reference syntax defined by the <code>configure_file()</code> and <code>string(CONFIGURE)</code> commands is no longer performed in other contexts.</p>
<dt>&bull;</p>
<dd>Literal <code>${VAR}</code> reference syntax may contain only alphanumeric characters (<code>A-Z</code>, <code>a-z</code>, <code>0-9</code>) and the characters <code>_</code>, <code>.</code>, <code>/</code>, <code>&#8211;</code>, and <code>+</code>. Variables with other characters in their name may still be referenced indirectly, e.g. </p>
<pre>set(varname &quot;otherwise &amp; disallowed $ characters&quot;)
message(&quot;${${varname}}&quot;)</pre>
<dt>&bull;</p>
<dd>The setting of policy <code>CMP0010</code> is not considered, so improper variable reference syntax is always an error.</p>
<dt>&bull;</p>
<dd>More characters are allowed to be escaped in variable names. Previously, only <code>()#&quot; \@^</code> were valid characters to escape. Now any non-alphanumeric, non-semicolon, non-NUL character may be escaped following the <code>escape_identity</code> production in the <i>Escape Sequences</i> section of the <code><a href="/docs/linux/man/7-cmake3-language/">cmake3-language</a>(7)</code> manual. </p>
<p> The <code>OLD</code> behavior for this policy is to honor the legacy behavior for variable references and escape sequences. The <code>NEW</code> behavior is to use the simpler variable expansion and escape sequence evaluation rules. </p>
<p> This policy was introduced in CMake version 3.1. CMake version 3.6.3 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</dl>
<h3>Cmp0052</h3>
<p>Reject source and build dirs in installed INTERFACE_INCLUDE_DIRECTORIES. </p>
<p> CMake 3.0 and lower allowed subdirectories of the source directory or build directory to be in the <code>INTERFACE_INCLUDE_DIRECTORIES</code> of installed and exported targets, if the directory was also a subdirectory of the installation prefix. This makes the installation depend on the existence of the source dir or binary dir, and the installation will be broken if either are removed after installation. </p>
<p> See <i>Include Directories and Usage Requirements</i> for more on specifying include directories for targets. </p>
<p> The OLD behavior for this policy is to export the content of the <code>INTERFACE_INCLUDE_DIRECTORIES</code> with the source or binary directory. The NEW behavior for this policy is to issue an error if such a directory is used. </p>
<p> This policy was introduced in CMake version 3.1. CMake version 3.6.3 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0051</h3>
<p>List TARGET_OBJECTS in SOURCES target property. </p>
<p> CMake 3.0 and lower did not include the <code>TARGET_OBJECTS</code> <code>generator expression</code> when returning the <code>SOURCES</code> target property. </p>
<p> Configure-time CMake code is not able to handle generator expressions. If using the <code>SOURCES</code> target property at configure time, it may be necessary to first remove generator expressions using the <code>string(GENEX_STRIP)</code> command. Generate-time CMake code such as <code>file(GENERATE)</code> can handle the content without stripping. </p>
<p> The <code>OLD</code> behavior for this policy is to omit <code>TARGET_OBJECTS</code> expressions from the <code>SOURCES</code> target property. The <code>NEW</code> behavior for this policy is to include <code>TARGET_OBJECTS</code> expressions in the output. </p>
<p> This policy was introduced in CMake version 3.1. CMake version 3.6.3 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 3.0</h2>
<h3>Cmp0050</h3>
<p>Disallow add_custom_command SOURCE signatures. </p>
<p> CMake 2.8.12 and lower allowed a signature for <code>add_custom_command()</code> which specified an input to a command. This was undocumented behavior. Modern use of CMake associates custom commands with their output, rather than their input. </p>
<p> The OLD behavior for this policy is to allow the use of <code>add_custom_command()</code> SOURCE signatures. The NEW behavior for this policy is to issue an error if such a signature is used. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0049</h3>
<p>Do not expand variables in target source entries. </p>
<p> CMake 2.8.12 and lower performed and extra layer of variable expansion when evaluating source file names: </p>
<pre>set(a_source foo.c)
add_executable(foo \${a_source})</pre>
<p>This was undocumented behavior. </p>
<p> The OLD behavior for this policy is to expand such variables when processing the target sources. The NEW behavior for this policy is to issue an error if such variables need to be expanded. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0048</h3>
<p>The <code>project()</code> command manages VERSION variables. </p>
<p> CMake version 3.0 introduced the <code>VERSION</code> option of the <code>project()</code> command to specify a project version as well as the name. In order to keep <code>PROJECT_VERSION</code> and related variables consistent with variable <code>PROJECT_NAME</code> it is necessary to set the VERSION variables to the empty string when no <code>VERSION</code> is given to <code>project()</code>. However, this can change behavior for existing projects that set VERSION variables themselves since <code>project()</code> may now clear them. This policy controls the behavior for compatibility with such projects. </p>
<p> The OLD behavior for this policy is to leave VERSION variables untouched. The NEW behavior for this policy is to set VERSION as documented by the <code>project()</code> command. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0047</h3>
<p>Use <code>QCC</code> compiler id for the qcc drivers on QNX. </p>
<p> CMake 3.0 and above recognize that the QNX qcc compiler driver is different from the GNU compiler. CMake now prefers to present this to projects by setting the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable to <code>QCC</code> instead of <code>GNU</code>. However, existing projects may assume the compiler id for QNX qcc is just <code>GNU</code> as it was in CMake versions prior to 3.0. Therefore this policy determines for QNX qcc which compiler id to report in the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable after language <code>&lt;LANG&gt;</code> is enabled by the <code>project()</code> or <code>enable_language()</code> command. The policy must be set prior to the invocation of either command. </p>
<p> The OLD behavior for this policy is to use the <code>GNU</code> compiler id for the qcc and QCC compiler drivers. The NEW behavior for this policy is to use the <code>QCC</code> compiler id for those drivers. </p>
<p> This policy was introduced in CMake version 3.0. Use the <code>cmake_policy()</code> command to set this policy to OLD or NEW explicitly. Unlike most policies, CMake version 3.6.3 does <i>not</i> warn by default when this policy is not set and simply uses OLD behavior. See documentation of the <code>CMAKE_POLICY_WARNING_CMP0047</code> variable to control the warning. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0046</h3>
<p>Error on non-existent dependency in add_dependencies. </p>
<p> CMake 2.8.12 and lower silently ignored non-existent dependencies listed in the <code>add_dependencies()</code> command. </p>
<p> The OLD behavior for this policy is to silently ignore non-existent dependencies. The NEW behavior for this policy is to report an error if non-existent dependencies are listed in the <code>add_dependencies()</code> command. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0045</h3>
<p>Error on non-existent target in get_target_property. </p>
<p> In CMake 2.8.12 and lower, the <code>get_target_property()</code> command accepted a non-existent target argument without issuing any error or warning. The result variable is set to a <code>-NOTFOUND</code> value. </p>
<p> The OLD behavior for this policy is to issue no warning and set the result variable to a <code>-NOTFOUND</code> value. The NEW behavior for this policy is to issue a <code>FATAL_ERROR</code> if the command is called with a non-existent target. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0044</h3>
<p>Case sensitive <code>&lt;LANG&gt;_COMPILER_ID</code> generator expressions </p>
<p> CMake 2.8.12 introduced the <code>&lt;LANG&gt;_COMPILER_ID</code> <code>generator expressions</code> to allow comparison of the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> with a test value. The possible valid values are lowercase, but the comparison with the test value was performed case-insensitively. </p>
<p> The OLD behavior for this policy is to perform a case-insensitive comparison with the value in the <code>&lt;LANG&gt;_COMPILER_ID</code> expression. The NEW behavior for this policy is to perform a case-sensitive comparison with the value in the <code>&lt;LANG&gt;_COMPILER_ID</code> expression. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
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
<p>The OLD behavior for this policy is to consume the content of the suffixed <code>COMPILE_DEFINITIONS_&lt;CONFIG&gt;</code> target property when generating the compilation command. The NEW behavior for this policy is to ignore the content of the <code>COMPILE_DEFINITIONS_&lt;CONFIG&gt;</code> target property . </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0042</h3>
<p><code>MACOSX_RPATH</code> is enabled by default. </p>
<p> CMake 2.8.12 and newer has support for using <code>@rpath</code> in a target&#8217;s install name. This was enabled by setting the target property <code>MACOSX_RPATH</code>. The <code>@rpath</code> in an install name is a more flexible and powerful mechanism than <code>@executable_path</code> or <code>@loader_path</code> for locating shared libraries. </p>
<p> CMake 3.0 and later prefer this property to be ON by default. Projects wanting <code>@rpath</code> in a target&#8217;s install name may remove any setting of the <code>INSTALL_NAME_DIR</code> and <code>CMAKE_INSTALL_NAME_DIR</code> variables. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0041</h3>
<p>Error on relative include with generator expression. </p>
<p> Diagnostics in CMake 2.8.12 and lower silently ignored an entry in the <code>INTERFACE_INCLUDE_DIRECTORIES</code> of a target if it contained a generator expression at any position. </p>
<p> The path entries in that target property should not be relative. High-level API should ensure that by adding either a source directory or a install directory prefix, as appropriate. </p>
<p> As an additional diagnostic, the <code>INTERFACE_INCLUDE_DIRECTORIES</code> generated on an <code>IMPORTED</code> target for the install location should not contain paths in the source directory or the build directory. </p>
<p> The OLD behavior for this policy is to ignore relative path entries if they contain a generator expression. The NEW behavior for this policy is to report an error if a generator expression appears in another location and the path is relative. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0040</h3>
<p>The target in the <code>TARGET</code> signature of <code>add_custom_command()</code> must exist and must be defined in current directory. </p>
<p> CMake 2.8.12 and lower silently ignored a custom command created with the <code>TARGET</code> signature of <code>add_custom_command()</code> if the target is unknown or was defined outside the current directory. </p>
<p> The <code>OLD</code> behavior for this policy is to ignore custom commands for unknown targets. The <code>NEW</code> behavior for this policy is to report an error if the target referenced in <code>add_custom_command()</code> is unknown or was defined outside the current directory. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses <code>OLD</code> behavior. Use the <code>cmake_policy()</code> command to set it to <code>OLD</code> or <code>NEW</code> explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0039</h3>
<p>Utility targets may not have link dependencies. </p>
<p> CMake 2.8.12 and lower allowed using utility targets in the left hand side position of the <code>target_link_libraries()</code> command. This is an indicator of a bug in user code. </p>
<p> The OLD behavior for this policy is to ignore attempts to set the link libraries of utility targets. The NEW behavior for this policy is to report an error if an attempt is made to set the link libraries of a utility target. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0038</h3>
<p>Targets may not link directly to themselves. </p>
<p> CMake 2.8.12 and lower allowed a build target to link to itself directly with a <code>target_link_libraries()</code> call. This is an indicator of a bug in user code. </p>
<p> The OLD behavior for this policy is to ignore targets which list themselves in their own link implementation. The NEW behavior for this policy is to report an error if a target attempts to link to itself. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0037</h3>
<p>Target names should not be reserved and should match a validity pattern. </p>
<p> CMake 2.8.12 and lower allowed creating targets using <code>add_library()</code>, <code>add_executable()</code> and <code>add_custom_target()</code> with unrestricted choice for the target name. Newer cmake features such as <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> and some diagnostics expect target names to match a restricted pattern. </p>
<p> Target names may contain upper and lower case letters, numbers, the underscore character (_), dot(.), plus(+) and minus(-). As a special case, ALIAS targets and IMPORTED targets may contain two consequtive colons. </p>
<p> Target names reserved by one or more CMake generators are not allowed. Among others these include &quot;all&quot;, &quot;help&quot; and &quot;test&quot;. </p>
<p> The OLD behavior for this policy is to allow creating targets with reserved names or which do not match the validity pattern. The NEW behavior for this policy is to report an error if an add_* command is used with an invalid target name. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0036</h3>
<p>The <code>build_name()</code> command should not be called. </p>
<p> This command was added in May 2001 to compute a name for the current operating system and compiler combination. The command has long been documented as discouraged and replaced by the <code>CMAKE_SYSTEM</code> and <code>CMAKE_&lt;LANG&gt;_COMPILER</code> variables. </p>
<p> CMake &gt;= 3.0 prefer that this command never be called. The OLD behavior for this policy is to allow the command to be called. The NEW behavior for this policy is to issue a FATAL_ERROR when the command is called. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0035</h3>
<p>The <code>variable_requires()</code> command should not be called. </p>
<p> This command was introduced in November 2001 to perform some conditional logic. It has long been replaced by the <code>if()</code> command. </p>
<p> CMake &gt;= 3.0 prefer that this command never be called. The OLD behavior for this policy is to allow the command to be called. The NEW behavior for this policy is to issue a FATAL_ERROR when the command is called. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0034</h3>
<p>The <code>utility_source()</code> command should not be called. </p>
<p> This command was introduced in March 2001 to help build executables used to generate other files. This approach has long been replaced by <code>add_executable()</code> combined with <code>add_custom_command()</code>. </p>
<p> CMake &gt;= 3.0 prefer that this command never be called. The OLD behavior for this policy is to allow the command to be called. The NEW behavior for this policy is to issue a FATAL_ERROR when the command is called. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0033</h3>
<p>The <code>export_library_dependencies()</code> command should not be called. </p>
<p> This command was added in January 2003 to export <code>&lt;tgt&gt;_LIB_DEPENDS</code> internal CMake cache entries to a file for installation with a project. This was used at the time to allow transitive link dependencies to work for applications outside of the original build tree of a project. The functionality has been superseded by the <code>export()</code> and <code>install(EXPORT)</code> commands. </p>
<p> CMake &gt;= 3.0 prefer that this command never be called. The OLD behavior for this policy is to allow the command to be called. The NEW behavior for this policy is to issue a FATAL_ERROR when the command is called. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0032</h3>
<p>The <code>output_required_files()</code> command should not be called. </p>
<p> This command was added in June 2001 to expose the then-current CMake implicit dependency scanner. CMake&#8217;s real implicit dependency scanner has evolved since then but is not exposed through this command. The scanning capabilities of this command are very limited and this functionality is better achieved through dedicated outside tools. </p>
<p> CMake &gt;= 3.0 prefer that this command never be called. The OLD behavior for this policy is to allow the command to be called. The NEW behavior for this policy is to issue a FATAL_ERROR when the command is called. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0031</h3>
<p>The <code>load_command()</code> command should not be called. </p>
<p> This command was added in August 2002 to allow projects to add arbitrary commands implemented in C or C++. However, it does not work when the toolchain in use does not match the ABI of the CMake process. It has been mostly superseded by the <code>macro()</code> and <code>function()</code> commands. </p>
<p> CMake &gt;= 3.0 prefer that this command never be called. The OLD behavior for this policy is to allow the command to be called. The NEW behavior for this policy is to issue a FATAL_ERROR when the command is called. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0030</h3>
<p>The <code>use_mangled_mesa()</code> command should not be called. </p>
<p> This command was created in September 2001 to support VTK before modern CMake language and custom command capabilities. VTK has not used it in years. </p>
<p> CMake &gt;= 3.0 prefer that this command never be called. The OLD behavior for this policy is to allow the command to be called. The NEW behavior for this policy is to issue a FATAL_ERROR when the command is called. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0029</h3>
<p>The <code>subdir_depends()</code> command should not be called. </p>
<p> The implementation of this command has been empty since December 2001 but was kept in CMake for compatibility for a long time. </p>
<p> CMake &gt;= 3.0 prefer that this command never be called. The OLD behavior for this policy is to allow the command to be called. The NEW behavior for this policy is to issue a FATAL_ERROR when the command is called. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0028</h3>
<p>Double colon in target name means ALIAS or IMPORTED target. </p>
<p> CMake 2.8.12 and lower allowed the use of targets and files with double colons in target_link_libraries, with some buildsystem generators. </p>
<p> The use of double-colons is a common pattern used to namespace IMPORTED targets and ALIAS targets. When computing the link dependencies of a target, the name of each dependency could either be a target, or a file on disk. Previously, if a target was not found with a matching name, the name was considered to refer to a file on disk. This can lead to confusing error messages if there is a typo in what should be a target name. </p>
<p> The OLD behavior for this policy is to search for targets, then files on disk, even if the search term contains double-colons. The NEW behavior for this policy is to issue a FATAL_ERROR if a link dependency contains double-colons but is not an IMPORTED target or an ALIAS target. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0027</h3>
<p>Conditionally linked imported targets with missing include directories. </p>
<p> CMake 2.8.11 introduced introduced the concept of INTERFACE_INCLUDE_DIRECTORIES, and a check at cmake time that the entries in the INTERFACE_INCLUDE_DIRECTORIES of an IMPORTED target actually exist. CMake 2.8.11 also introduced generator expression support in the target_link_libraries command. However, if an imported target is linked as a result of a generator expression evaluation, the entries in the INTERFACE_INCLUDE_DIRECTORIES of that target were not checked for existence as they should be. </p>
<p> The OLD behavior of this policy is to report a warning if an entry in the INTERFACE_INCLUDE_DIRECTORIES of a generator-expression conditionally linked IMPORTED target does not exist. </p>
<p> The NEW behavior of this policy is to report an error if an entry in the INTERFACE_INCLUDE_DIRECTORIES of a generator-expression conditionally linked IMPORTED target does not exist. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0026</h3>
<p>Disallow use of the LOCATION property for build targets. </p>
<p> CMake 2.8.12 and lower allowed reading the LOCATION target property (and configuration-specific variants) to determine the eventual location of build targets. This relies on the assumption that all necessary information is available at configure-time to determine the final location and filename of the target. However, this property is not fully determined until later at generate-time. At generate time, the $&lt;TARGET_FILE&gt; generator expression can be used to determine the eventual LOCATION of a target output. </p>
<p> Code which reads the LOCATION target property can be ported to use the $&lt;TARGET_FILE&gt; generator expression together with the file(GENERATE) subcommand to generate a file containing the target location. </p>
<p> The OLD behavior for this policy is to allow reading the LOCATION properties from build-targets. The NEW behavior for this policy is to not to allow reading the LOCATION properties from build-targets. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0025</h3>
<p>Compiler id for Apple Clang is now <code>AppleClang</code>. </p>
<p> CMake 3.0 and above recognize that Apple Clang is a different compiler than upstream Clang and that they have different version numbers. CMake now prefers to present this to projects by setting the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable to <code>AppleClang</code> instead of <code>Clang</code>. However, existing projects may assume the compiler id for Apple Clang is just <code>Clang</code> as it was in CMake versions prior to 3.0. Therefore this policy determines for Apple Clang which compiler id to report in the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable after language <code>&lt;LANG&gt;</code> is enabled by the <code>project()</code> or <code>enable_language()</code> command. The policy must be set prior to the invocation of either command. </p>
<p> The OLD behavior for this policy is to use compiler id <code>Clang</code>. The NEW behavior for this policy is to use compiler id <code>AppleClang</code>. </p>
<p> This policy was introduced in CMake version 3.0. Use the <code>cmake_policy()</code> command to set this policy to OLD or NEW explicitly. Unlike most policies, CMake version 3.6.3 does <i>not</i> warn by default when this policy is not set and simply uses OLD behavior. See documentation of the <code>CMAKE_POLICY_WARNING_CMP0025</code> variable to control the warning. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0024</h3>
<p>Disallow include export result. </p>
<p> CMake 2.8.12 and lower allowed use of the include() command with the result of the export() command. This relies on the assumption that the export() command has an immediate effect at configure-time during a cmake run. Certain properties of targets are not fully determined until later at generate-time, such as the link language and complete list of link libraries. Future refactoring will change the effect of the export() command to be executed at generate-time. Use ALIAS targets instead in cases where the goal is to refer to targets by another name. </p>
<p> The OLD behavior for this policy is to allow including the result of an export() command. The NEW behavior for this policy is not to allow including the result of an export() command. </p>
<p> This policy was introduced in CMake version 3.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 2.8</h2>
<h3>Cmp0023</h3>
<p>Plain and keyword target_link_libraries signatures cannot be mixed. </p>
<p> CMake 2.8.12 introduced the target_link_libraries signature using the PUBLIC, PRIVATE, and INTERFACE keywords to generalize the LINK_PUBLIC and LINK_PRIVATE keywords introduced in CMake 2.8.7. Use of signatures with any of these keywords sets the link interface of a target explicitly, even if empty. This produces confusing behavior when used in combination with the historical behavior of the plain target_link_libraries signature. For example, consider the code: </p>
<pre>target_link_libraries(mylib A)
target_link_libraries(mylib PRIVATE B)</pre>
<p>After the first line the link interface has not been set explicitly so CMake would use the link implementation, A, as the link interface. However, the second line sets the link interface to empty. In order to avoid this subtle behavior CMake now prefers to disallow mixing the plain and keyword signatures of target_link_libraries for a single target. </p>
<p> The OLD behavior for this policy is to allow keyword and plain target_link_libraries signatures to be mixed. The NEW behavior for this policy is to not to allow mixing of the keyword and plain signatures. </p>
<p> This policy was introduced in CMake version 2.8.12. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0022</h3>
<p>INTERFACE_LINK_LIBRARIES defines the link interface. </p>
<p> CMake 2.8.11 constructed the &#8216;link interface&#8217; of a target from properties matching <code>(IMPORTED_)?LINK_INTERFACE_LIBRARIES(_&lt;CONFIG&gt;)?</code>. The modern way to specify config-sensitive content is to use generator expressions and the <code>IMPORTED_</code> prefix makes uniform processing of the link interface with generator expressions impossible. The INTERFACE_LINK_LIBRARIES target property was introduced as a replacement in CMake 2.8.12. This new property is named consistently with the INTERFACE_COMPILE_DEFINITIONS, INTERFACE_INCLUDE_DIRECTORIES and INTERFACE_COMPILE_OPTIONS properties. For in-build targets, CMake will use the INTERFACE_LINK_LIBRARIES property as the source of the link interface only if policy CMP0022 is NEW. When exporting a target which has this policy set to NEW, only the INTERFACE_LINK_LIBRARIES property will be processed and generated for the IMPORTED target by default. A new option to the install(EXPORT) and export commands allows export of the old-style properties for compatibility with downstream users of CMake versions older than 2.8.12. The target_link_libraries command will no longer populate the properties matching LINK_INTERFACE_LIBRARIES(_&lt;CONFIG&gt;)? if this policy is NEW. </p>
<p> Warning-free future-compatible code which works with CMake 2.8.7 onwards can be written by using the <code>LINK_PRIVATE</code> and <code>LINK_PUBLIC</code> keywords of <code>target_link_libraries()</code>. </p>
<p> The OLD behavior for this policy is to ignore the INTERFACE_LINK_LIBRARIES property for in-build targets. The NEW behavior for this policy is to use the INTERFACE_LINK_LIBRARIES property for in-build targets, and ignore the old properties matching <code>(IMPORTED_)?LINK_INTERFACE_LIBRARIES(_&lt;CONFIG&gt;)?</code>. </p>
<p> This policy was introduced in CMake version 2.8.12. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0021</h3>
<p>Fatal error on relative paths in INCLUDE_DIRECTORIES target property. </p>
<p> CMake 2.8.10.2 and lower allowed the INCLUDE_DIRECTORIES target property to contain relative paths. The base path for such relative entries is not well defined. CMake 2.8.12 issues a FATAL_ERROR if the INCLUDE_DIRECTORIES property contains a relative path. </p>
<p> The OLD behavior for this policy is not to warn about relative paths in the INCLUDE_DIRECTORIES target property. The NEW behavior for this policy is to issue a FATAL_ERROR if INCLUDE_DIRECTORIES contains a relative path. </p>
<p> This policy was introduced in CMake version 2.8.12. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0020</h3>
<p>Automatically link Qt executables to qtmain target on Windows. </p>
<p> CMake 2.8.10 and lower required users of Qt to always specify a link dependency to the qtmain.lib static library manually on Windows. CMake 2.8.11 gained the ability to evaluate generator expressions while determining the link dependencies from IMPORTED targets. This allows CMake itself to automatically link executables which link to Qt to the qtmain.lib library when using IMPORTED Qt targets. For applications already linking to qtmain.lib, this should have little impact. For applications which supply their own alternative WinMain implementation and for applications which use the QAxServer library, this automatic linking will need to be disabled as per the documentation. </p>
<p> The OLD behavior for this policy is not to link executables to qtmain.lib automatically when they link to the QtCore IMPORTED target. The NEW behavior for this policy is to link executables to qtmain.lib automatically when they link to QtCore IMPORTED target. </p>
<p> This policy was introduced in CMake version 2.8.11. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0019</h3>
<p>Do not re-expand variables in include and link information. </p>
<p> CMake 2.8.10 and lower re-evaluated values given to the include_directories, link_directories, and link_libraries commands to expand any leftover variable references at the end of the configuration step. This was for strict compatibility with VERY early CMake versions because all variable references are now normally evaluated during CMake language processing. CMake 2.8.11 and higher prefer to skip the extra evaluation. </p>
<p> The OLD behavior for this policy is to re-evaluate the values for strict compatibility. The NEW behavior for this policy is to leave the values untouched. </p>
<p> This policy was introduced in CMake version 2.8.11. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0018</h3>
<p>Ignore CMAKE_SHARED_LIBRARY_&lt;Lang&gt;_FLAGS variable. </p>
<p> CMake 2.8.8 and lower compiled sources in SHARED and MODULE libraries using the value of the undocumented CMAKE_SHARED_LIBRARY_&lt;Lang&gt;_FLAGS platform variable. The variable contained platform-specific flags needed to compile objects for shared libraries. Typically it included a flag such as -fPIC for position independent code but also included other flags needed on certain platforms. CMake 2.8.9 and higher prefer instead to use the POSITION_INDEPENDENT_CODE target property to determine what targets should be position independent, and new undocumented platform variables to select flags while ignoring CMAKE_SHARED_LIBRARY_&lt;Lang&gt;_FLAGS completely. </p>
<p> The default for either approach produces identical compilation flags, but if a project modifies CMAKE_SHARED_LIBRARY_&lt;Lang&gt;_FLAGS from its original value this policy determines which approach to use. </p>
<p> The OLD behavior for this policy is to ignore the POSITION_INDEPENDENT_CODE property for all targets and use the modified value of CMAKE_SHARED_LIBRARY_&lt;Lang&gt;_FLAGS for SHARED and MODULE libraries. </p>
<p> The NEW behavior for this policy is to ignore CMAKE_SHARED_LIBRARY_&lt;Lang&gt;_FLAGS whether it is modified or not and honor the POSITION_INDEPENDENT_CODE target property. </p>
<p> This policy was introduced in CMake version 2.8.9. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0017</h3>
<p>Prefer files from the CMake module directory when including from there. </p>
<p> Starting with CMake 2.8.4, if a cmake-module shipped with CMake (i.e. located in the CMake module directory) calls include() or find_package(), the files located in the CMake module directory are preferred over the files in CMAKE_MODULE_PATH. This makes sure that the modules belonging to CMake always get those files included which they expect, and against which they were developed and tested. In all other cases, the files found in CMAKE_MODULE_PATH still take precedence over the ones in the CMake module directory. The OLD behavior is to always prefer files from CMAKE_MODULE_PATH over files from the CMake modules directory. </p>
<p> This policy was introduced in CMake version 2.8.4. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0016</h3>
<p>target_link_libraries() reports error if its only argument is not a target. </p>
<p> In CMake 2.8.2 and lower the target_link_libraries() command silently ignored if it was called with only one argument, and this argument wasn&#8217;t a valid target. In CMake 2.8.3 and above it reports an error in this case. </p>
<p> This policy was introduced in CMake version 2.8.3. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0015</h3>
<p>link_directories() treats paths relative to the source dir. </p>
<p> In CMake 2.8.0 and lower the link_directories() command passed relative paths unchanged to the linker. In CMake 2.8.1 and above the link_directories() command prefers to interpret relative paths with respect to CMAKE_CURRENT_SOURCE_DIR, which is consistent with include_directories() and other commands. The OLD behavior for this policy is to use relative paths verbatim in the linker command. The NEW behavior for this policy is to convert relative paths to absolute paths by appending the relative path to CMAKE_CURRENT_SOURCE_DIR. </p>
<p> This policy was introduced in CMake version 2.8.1. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0014</h3>
<p>Input directories must have CMakeLists.txt. </p>
<p> CMake versions before 2.8 silently ignored missing CMakeLists.txt files in directories referenced by add_subdirectory() or subdirs(), treating them as if present but empty. In CMake 2.8.0 and above this policy determines whether or not the case is an error. The OLD behavior for this policy is to silently ignore the problem. The NEW behavior for this policy is to report an error. </p>
<p> This policy was introduced in CMake version 2.8.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0013</h3>
<p>Duplicate binary directories are not allowed. </p>
<p> CMake 2.6.3 and below silently permitted add_subdirectory() calls to create the same binary directory multiple times. During build system generation files would be written and then overwritten in the build tree and could lead to strange behavior. CMake 2.6.4 and above explicitly detect duplicate binary directories. CMake 2.6.4 always considers this case an error. In CMake 2.8.0 and above this policy determines whether or not the case is an error. The OLD behavior for this policy is to allow duplicate binary directories. The NEW behavior for this policy is to disallow duplicate binary directories with an error. </p>
<p> This policy was introduced in CMake version 2.8.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0012</h3>
<p>if() recognizes numbers and boolean constants. </p>
<p> In CMake versions 2.6.4 and lower the if() command implicitly dereferenced arguments corresponding to variables, even those named like numbers or boolean constants, except for 0 and 1. Numbers and boolean constants such as true, false, yes, no, on, off, y, n, notfound, ignore (all case insensitive) were recognized in some cases but not all. For example, the code &quot;if(TRUE)&quot; might have evaluated as false. Numbers such as 2 were recognized only in boolean expressions like &quot;if(NOT 2)&quot; (leading to false) but not as a single-argument like &quot;<a href="/docs/linux/man/2-if/">if</a>(2)&quot; (also leading to false). Later versions of CMake prefer to treat numbers and boolean constants literally, so they should not be used as variable names. </p>
<p> The OLD behavior for this policy is to implicitly dereference variables named like numbers and boolean constants. The NEW behavior for this policy is to recognize numbers and boolean constants without dereferencing variables with such names. </p>
<p> This policy was introduced in CMake version 2.8.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Policies Introduced By Cmake 2.6</h2>
<h3>Cmp0011</h3>
<p>Included scripts do automatic cmake_policy PUSH and POP. </p>
<p> In CMake 2.6.2 and below, CMake Policy settings in scripts loaded by the include() and find_package() commands would affect the includer. Explicit invocations of cmake_policy(PUSH) and cmake_policy(POP) were required to isolate policy changes and protect the includer. While some scripts intend to affect the policies of their includer, most do not. In CMake 2.6.3 and above, include() and find_package() by default PUSH and POP an entry on the policy stack around an included script, but provide a NO_POLICY_SCOPE option to disable it. This policy determines whether or not to imply NO_POLICY_SCOPE for compatibility. The OLD behavior for this policy is to imply NO_POLICY_SCOPE for include() and find_package() commands. The NEW behavior for this policy is to allow the commands to do their default cmake_policy PUSH and POP. </p>
<p> This policy was introduced in CMake version 2.6.3. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0010</h3>
<p>Bad variable reference syntax is an error. </p>
<p> In CMake 2.6.2 and below, incorrect variable reference syntax such as a missing close-brace (&quot;${FOO&quot;) was reported but did not stop processing of CMake code. This policy determines whether a bad variable reference is an error. The OLD behavior for this policy is to warn about the error, leave the string untouched, and continue. The NEW behavior for this policy is to report an error. </p>
<p> If <code>CMP0053</code> is set to <code>NEW</code>, this policy has no effect and is treated as always being <code>NEW</code>. </p>
<p> This policy was introduced in CMake version 2.6.3. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0009</h3>
<p>FILE GLOB_RECURSE calls should not follow symlinks by default. </p>
<p> In CMake 2.6.1 and below, FILE GLOB_RECURSE calls would follow through symlinks, sometimes coming up with unexpectedly large result sets because of symlinks to top level directories that contain hundreds of thousands of files. </p>
<p> This policy determines whether or not to follow symlinks encountered during a FILE GLOB_RECURSE call. The OLD behavior for this policy is to follow the symlinks. The NEW behavior for this policy is not to follow the symlinks by default, but only if FOLLOW_SYMLINKS is given as an additional argument to the FILE command. </p>
<p> This policy was introduced in CMake version 2.6.2. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0008</h3>
<p>Libraries linked by full-path must have a valid library file name. </p>
<p> In CMake 2.4 and below it is possible to write code like </p>
<pre>target_link_libraries(myexe /full/path/to/somelib)</pre>
<p>where &quot;somelib&quot; is supposed to be a valid library file name such as &quot;libsomelib.a&quot; or &quot;somelib.lib&quot;. For Makefile generators this produces an error at build time because the dependency on the full path cannot be found. For VS IDE and Xcode generators this used to work by accident because CMake would always split off the library directory and ask the linker to search for the library by name (-lsomelib or somelib.lib). Despite the failure with Makefiles, some projects have code like this and build only with VS and/or Xcode. This version of CMake prefers to pass the full path directly to the native build tool, which will fail in this case because it does not name a valid library file. </p>
<p> This policy determines what to do with full paths that do not appear to name a valid library file. The OLD behavior for this policy is to split the library name from the path and ask the linker to search for it. The NEW behavior for this policy is to trust the given path and pass it directly to the native build tool unchanged. </p>
<p> This policy was introduced in CMake version 2.6.1. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0007</h3>
<p>list command no longer ignores empty elements. </p>
<p> This policy determines whether the list command will ignore empty elements in the list. CMake 2.4 and below list commands ignored all empty elements in the list. For example, a;b;;c would have length 3 and not 4. The OLD behavior for this policy is to ignore empty list elements. The NEW behavior for this policy is to correctly count empty elements in a list. </p>
<p> This policy was introduced in CMake version 2.6.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0006</h3>
<p>Installing MACOSX_BUNDLE targets requires a BUNDLE DESTINATION. </p>
<p> This policy determines whether the install(TARGETS) command must be given a BUNDLE DESTINATION when asked to install a target with the MACOSX_BUNDLE property set. CMake 2.4 and below did not distinguish application bundles from normal executables when installing targets. CMake 2.6 provides a BUNDLE option to the install(TARGETS) command that specifies rules specific to application bundles on the Mac. Projects should use this option when installing a target with the MACOSX_BUNDLE property set. </p>
<p> The OLD behavior for this policy is to fall back to the RUNTIME DESTINATION if a BUNDLE DESTINATION is not given. The NEW behavior for this policy is to produce an error if a bundle target is installed without a BUNDLE DESTINATION. </p>
<p> This policy was introduced in CMake version 2.6.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0005</h3>
<p>Preprocessor definition values are now escaped automatically. </p>
<p> This policy determines whether or not CMake should generate escaped preprocessor definition values added via add_definitions. CMake versions 2.4 and below assumed that only trivial values would be given for macros in add_definitions calls. It did not attempt to escape non-trivial values such as string literals in generated build rules. CMake versions 2.6 and above support escaping of most values, but cannot assume the user has not added escapes already in an attempt to work around limitations in earlier versions. </p>
<p> The OLD behavior for this policy is to place definition values given to add_definitions directly in the generated build rules without attempting to escape anything. The NEW behavior for this policy is to generate correct escapes for all native build tools automatically. See documentation of the COMPILE_DEFINITIONS target property for limitations of the escaping implementation. </p>
<p> This policy was introduced in CMake version 2.6.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0004</h3>
<p>Libraries linked may not have leading or trailing whitespace. </p>
<p> CMake versions 2.4 and below silently removed leading and trailing whitespace from libraries linked with code like </p>
<pre>target_link_libraries(myexe &quot; A &quot;)</pre>
<p>This could lead to subtle errors in user projects. </p>
<p> The OLD behavior for this policy is to silently remove leading and trailing whitespace. The NEW behavior for this policy is to diagnose the existence of such whitespace as an error. The setting for this policy used when checking the library names is that in effect when the target is created by an add_executable or add_library command. </p>
<p> This policy was introduced in CMake version 2.6.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
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
<p>where &quot;B&quot; is meant to find &quot;/path/to/libB.so&quot;. This code is wrong because the user is asking the linker to find library B but has not provided a linker search path (which may be added with the link_directories command). However, with the old linking implementation the code would work accidentally because the linker search path added for library A allowed library B to be found. </p>
<p> In order to support projects depending on linker search paths added by linking to libraries with known full paths, the OLD behavior for this policy will add the linker search paths even though they are not needed for their own libraries. When this policy is set to OLD, CMake will produce a link line such as </p>
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
<p> This policy was introduced in CMake version 2.6.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0002</h3>
<p>Logical target names must be globally unique. </p>
<p> Targets names created with add_executable, add_library, or add_custom_target are logical build target names. Logical target names must be globally unique because: </p>
<pre>- Unique names may be referenced unambiguously both in CMake
 code and on make tool command lines.
- Logical names are used by Xcode and VS IDE generators
 to produce meaningful project names for the targets.</pre>
<p>The logical name of executable and library targets does not have to correspond to the physical file names built. Consider using the OUTPUT_NAME target property to create two targets with the same physical name while keeping logical names distinct. Custom targets must simply have globally unique names (unless one uses the global property ALLOW_DUPLICATE_CUSTOM_TARGETS with a Makefiles generator). </p>
<p> This policy was introduced in CMake version 2.6.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0001</h3>
<p>CMAKE_BACKWARDS_COMPATIBILITY should no longer be used. </p>
<p> The OLD behavior is to check CMAKE_BACKWARDS_COMPATIBILITY and present it to the user. The NEW behavior is to ignore CMAKE_BACKWARDS_COMPATIBILITY completely. </p>
<p> In CMake 2.4 and below the variable CMAKE_BACKWARDS_COMPATIBILITY was used to request compatibility with earlier versions of CMake. In CMake 2.6 and above all compatibility issues are handled by policies and the cmake_policy command. However, CMake must still check CMAKE_BACKWARDS_COMPATIBILITY for projects written for CMake 2.4 and below. </p>
<p> This policy was introduced in CMake version 2.6.0. CMake version 3.6.3 warns when the policy is not set and uses OLD behavior. Use the cmake_policy command to set it to OLD or NEW explicitly. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Cmp0000</h3>
<p>A minimum required CMake version must be specified. </p>
<p> CMake requires that projects specify the version of CMake to which they have been written. This policy has been put in place so users trying to build the project may be told when they need to update their CMake. Specifying a version also helps the project build with CMake versions newer than that specified. Use the cmake_minimum_required command at the top of your main CMakeLists.txt file: </p>
<pre>cmake_minimum_required(VERSION &lt;major&gt;.&lt;minor&gt;)</pre>
<p>where &quot;&lt;major&gt;.&lt;minor&gt;&quot; is the version of CMake you want to support (such as &quot;2.6&quot;). The command will ensure that at least the given version of CMake is running and help newer versions be compatible with the project. See documentation of cmake_minimum_required for details. </p>
<p> Note that the command invocation must appear in the CMakeLists.txt file itself; a call in an included file is not sufficient. However, the cmake_policy command may be called to set policy CMP0000 to OLD or NEW behavior explicitly. The OLD behavior is to silently ignore the missing invocation. The NEW behavior is to issue an error instead of a warning. An included file may set CMP0000 explicitly to affect how this policy is enforced for the main CMakeLists.txt file. </p>
<p> This policy was introduced in CMake version 2.6.0. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h2>Copyright</h2>
<p>2000-2016 Kitware, Inc.</p>
