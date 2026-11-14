---
title: "cmake3-properties(7)"
name: "cmake3-properties"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake3-properties/"
description: "cmake-properties – CMake Properties Reference"
---

<p>cmake-properties &#8211; CMake Properties Reference</p>
<h2>Properties Of Global Scope</h2>
<h3>Allow_Duplicate_Custom_Targets</h3>
<p>Allow duplicate custom targets to be created. </p>
<p> Normally CMake requires that all targets built in a project have globally unique logical names (see policy CMP0002). This is necessary to generate meaningful project file names in Xcode and VS IDE generators. It also allows the target names to be referenced unambiguously. </p>
<p> Makefile generators are capable of supporting duplicate custom target names. For projects that care only about Makefile generators and do not wish to support Xcode or VS IDE generators, one may set this property to true to allow duplicate custom targets. The property allows multiple add_custom_target command calls in different directories to specify the same target name. However, setting this property will cause non-Makefile generators to produce an error and refuse to generate the project.</p>
<h3>Autogen_Targets_Folder</h3>
<p>Name of <code>FOLDER</code> for <code>*_automoc</code> targets that are added automatically by CMake for targets for which <code>AUTOMOC</code> is enabled. </p>
<p> If not set, CMake uses the <code>FOLDER</code> property of the parent target as a default value for this property. See also the documentation for the <code>FOLDER</code> target property and the <code>AUTOMOC</code> target property.</p>
<h3>Automoc_Targets_Folder</h3>
<p>Name of <code>FOLDER</code> for <code>*_automoc</code> targets that are added automatically by CMake for targets for which <code>AUTOMOC</code> is enabled. </p>
<p> This property is obsolete. Use <code>AUTOGEN_TARGETS_FOLDER</code> instead. </p>
<p> If not set, CMake uses the <code>FOLDER</code> property of the parent target as a default value for this property. See also the documentation for the <code>FOLDER</code> target property and the <code>AUTOMOC</code> target property.</p>
<h3>Cmake_C_Known_Features</h3>
<p>List of C features known to this version of CMake. </p>
<p> The features listed in this global property may be known to be available to the C compiler. If the feature is available with the C compiler, it will be listed in the <code>CMAKE_C_COMPILE_FEATURES</code> variable. </p>
<p> The features listed here may be used with the <code>target_compile_features()</code> command. See the <code><a href="/docs/linux/man/7-cmake3-compile-features/">cmake3-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers. </p>
<p> The features known to this version of CMake are:</p>
<dl>
<dt><code>c_function_prototypes</code></p>
<dd>Function prototypes, as defined in <code>ISO/IEC 9899:1990</code>.</p>
<dt><code>c_restrict</code></p>
<dd><code>restrict</code> keyword, as defined in <code>ISO/IEC 9899:1999</code>.</p>
<dt><code>c_static_assert</code></p>
<dd>Static assert, as defined in <code>ISO/IEC 9899:2011</code>.</p>
<dt><code>c_variadic_macros</code></p>
<dd>Variadic macros, as defined in <code>ISO/IEC 9899:1999</code>.</dl>
<h3>Cmake_Cxx_Known_Features</h3>
<p>List of C++ features known to this version of CMake. </p>
<p> The features listed in this global property may be known to be available to the C++ compiler. If the feature is available with the C++ compiler, it will be listed in the <code>CMAKE_CXX_COMPILE_FEATURES</code> variable. </p>
<p> The features listed here may be used with the <code>target_compile_features()</code> command. See the <code><a href="/docs/linux/man/7-cmake3-compile-features/">cmake3-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers. </p>
<p> The features known to this version of CMake are:</p>
<dl>
<dt><code>cxx_aggregate_default_initializers</code></p>
<dd>Aggregate default initializers, as defined in <i>N3605</i>.</p>
<dt><code>cxx_alias_templates</code></p>
<dd>Template aliases, as defined in <i>N2258</i>.</p>
<dt><code>cxx_alignas</code></p>
<dd>Alignment control <code>alignas</code>, as defined in <i>N2341</i>.</p>
<dt><code>cxx_alignof</code></p>
<dd>Alignment control <code>alignof</code>, as defined in <i>N2341</i>.</p>
<dt><code>cxx_attributes</code></p>
<dd>Generic attributes, as defined in <i>N2761</i>.</p>
<dt><code>cxx_attribute_deprecated</code></p>
<dd><code>[[deprecated]]</code> attribute, as defined in <i>N3760</i>.</p>
<dt><code>cxx_auto_type</code></p>
<dd>Automatic type deduction, as defined in <i>N1984</i>.</p>
<dt><code>cxx_binary_literals</code></p>
<dd>Binary literals, as defined in <i>N3472</i>.</p>
<dt><code>cxx_constexpr</code></p>
<dd>Constant expressions, as defined in <i>N2235</i>.</p>
<dt><code>cxx_contextual_conversions</code></p>
<dd>Contextual conversions, as defined in <i>N3323</i>.</p>
<dt><code>cxx_decltype_incomplete_return_types</code></p>
<dd>Decltype on incomplete return types, as defined in <i>N3276</i>.</p>
<dt><code>cxx_decltype</code></p>
<dd>Decltype, as defined in <i>N2343</i>.</p>
<dt><code>cxx_decltype_auto</code></p>
<dd><code>decltype(auto)</code> semantics, as defined in <i>N3638</i>.</p>
<dt><code>cxx_default_function_template_args</code></p>
<dd>Default template arguments for function templates, as defined in <i>DR226</i></p>
<dt><code>cxx_defaulted_functions</code></p>
<dd>Defaulted functions, as defined in <i>N2346</i>.</p>
<dt><code>cxx_defaulted_move_initializers</code></p>
<dd>Defaulted move initializers, as defined in <i>N3053</i>.</p>
<dt><code>cxx_delegating_constructors</code></p>
<dd>Delegating constructors, as defined in <i>N1986</i>.</p>
<dt><code>cxx_deleted_functions</code></p>
<dd>Deleted functions, as defined in <i>N2346</i>.</p>
<dt><code>cxx_digit_separators</code></p>
<dd>Digit separators, as defined in <i>N3781</i>.</p>
<dt><code>cxx_enum_forward_declarations</code></p>
<dd>Enum forward declarations, as defined in <i>N2764</i>.</p>
<dt><code>cxx_explicit_conversions</code></p>
<dd>Explicit conversion operators, as defined in <i>N2437</i>.</p>
<dt><code>cxx_extended_friend_declarations</code></p>
<dd>Extended friend declarations, as defined in <i>N1791</i>.</p>
<dt><code>cxx_extern_templates</code></p>
<dd>Extern templates, as defined in <i>N1987</i>.</p>
<dt><code>cxx_final</code></p>
<dd>Override control <code>final</code> keyword, as defined in <i>N2928</i>, <i>N3206</i> and <i>N3272</i>.</p>
<dt><code>cxx_func_identifier</code></p>
<dd>Predefined <code>__func__</code> identifier, as defined in <i>N2340</i>.</p>
<dt><code>cxx_generalized_initializers</code></p>
<dd>Initializer lists, as defined in <i>N2672</i>.</p>
<dt><code>cxx_generic_lambdas</code></p>
<dd>Generic lambdas, as defined in <i>N3649</i>.</p>
<dt><code>cxx_inheriting_constructors</code></p>
<dd>Inheriting constructors, as defined in <i>N2540</i>.</p>
<dt><code>cxx_inline_namespaces</code></p>
<dd>Inline namespaces, as defined in <i>N2535</i>.</p>
<dt><code>cxx_lambdas</code></p>
<dd>Lambda functions, as defined in <i>N2927</i>.</p>
<dt><code>cxx_lambda_init_captures</code></p>
<dd>Initialized lambda captures, as defined in <i>N3648</i>.</p>
<dt><code>cxx_local_type_template_args</code></p>
<dd>Local and unnamed types as template arguments, as defined in <i>N2657</i>.</p>
<dt><code>cxx_long_long_type</code></p>
<dd><code>long long</code> type, as defined in <i>N1811</i>.</p>
<dt><code>cxx_noexcept</code></p>
<dd>Exception specifications, as defined in <i>N3050</i>.</p>
<dt><code>cxx_nonstatic_member_init</code></p>
<dd>Non-static data member initialization, as defined in <i>N2756</i>.</p>
<dt><code>cxx_nullptr</code></p>
<dd>Null pointer, as defined in <i>N2431</i>.</p>
<dt><code>cxx_override</code></p>
<dd>Override control <code>override</code> keyword, as defined in <i>N2928</i>, <i>N3206</i> and <i>N3272</i>.</p>
<dt><code>cxx_range_for</code></p>
<dd>Range-based for, as defined in <i>N2930</i>.</p>
<dt><code>cxx_raw_string_literals</code></p>
<dd>Raw string literals, as defined in <i>N2442</i>.</p>
<dt><code>cxx_reference_qualified_functions</code></p>
<dd>Reference qualified functions, as defined in <i>N2439</i>.</p>
<dt><code>cxx_relaxed_constexpr</code></p>
<dd>Relaxed constexpr, as defined in <i>N3652</i>.</p>
<dt><code>cxx_return_type_deduction</code></p>
<dd>Return type deduction on normal functions, as defined in <i>N3386</i>.</p>
<dt><code>cxx_right_angle_brackets</code></p>
<dd>Right angle bracket parsing, as defined in <i>N1757</i>.</p>
<dt><code>cxx_rvalue_references</code></p>
<dd>R-value references, as defined in <i>N2118</i>.</p>
<dt><code>cxx_sizeof_member</code></p>
<dd>Size of non-static data members, as defined in <i>N2253</i>.</p>
<dt><code>cxx_static_assert</code></p>
<dd>Static assert, as defined in <i>N1720</i>.</p>
<dt><code>cxx_strong_enums</code></p>
<dd>Strongly typed enums, as defined in <i>N2347</i>.</p>
<dt><code>cxx_thread_local</code></p>
<dd>Thread-local variables, as defined in <i>N2659</i>.</p>
<dt><code>cxx_trailing_return_types</code></p>
<dd>Automatic function return type, as defined in <i>N2541</i>.</p>
<dt><code>cxx_unicode_literals</code></p>
<dd>Unicode string literals, as defined in <i>N2442</i>.</p>
<dt><code>cxx_uniform_initialization</code></p>
<dd>Uniform initialization, as defined in <i>N2640</i>.</p>
<dt><code>cxx_unrestricted_unions</code></p>
<dd>Unrestricted unions, as defined in <i>N2544</i>.</p>
<dt><code>cxx_user_literals</code></p>
<dd>User-defined literals, as defined in <i>N2765</i>.</p>
<dt><code>cxx_variable_templates</code></p>
<dd>Variable templates, as defined in <i>N3651</i>.</p>
<dt><code>cxx_variadic_macros</code></p>
<dd>Variadic macros, as defined in <i>N1653</i>.</p>
<dt><code>cxx_variadic_templates</code></p>
<dd>Variadic templates, as defined in <i>N2242</i>.</p>
<dt><code>cxx_template_template_parameters</code></p>
<dd>Template template parameters, as defined in <code>ISO/IEC 14882:1998</code>.</dl>
<h3>Debug_Configurations</h3>
<p>Specify which configurations are for debugging. </p>
<p> The value must be a semi-colon separated list of configuration names. Currently this property is used only by the target_link_libraries command (see its documentation for details). Additional uses may be defined in the future. </p>
<p> This property must be set at the top level of the project and before the first target_link_libraries command invocation. If any entry in the list does not match a valid configuration for the project the behavior is undefined.</p>
<h3>Disabled_Features</h3>
<p>List of features which are disabled during the CMake run. </p>
<p> List of features which are disabled during the CMake run. By default it contains the names of all packages which were not found. This is determined using the &lt;NAME&gt;_FOUND variables. Packages which are searched QUIET are not listed. A project can add its own features to this list. This property is used by the macros in FeatureSummary.cmake.</p>
<h3>Enabled_Features</h3>
<p>List of features which are enabled during the CMake run. </p>
<p> List of features which are enabled during the CMake run. By default it contains the names of all packages which were found. This is determined using the &lt;NAME&gt;_FOUND variables. Packages which are searched QUIET are not listed. A project can add its own features to this list. This property is used by the macros in FeatureSummary.cmake.</p>
<h3>Enabled_Languages</h3>
<p>Read-only property that contains the list of currently enabled languages </p>
<p> Set to list of currently enabled languages.</p>
<h3>Find_Library_Use_Lib64_Paths</h3>
<p>Whether <code>find_library()</code> should automatically search lib64 directories. </p>
<p> FIND_LIBRARY_USE_LIB64_PATHS is a boolean specifying whether the <code>find_library()</code> command should automatically search the lib64 variant of directories called lib in the search path when building 64-bit binaries.</p>
<h3>Find_Library_Use_Openbsd_Versioning</h3>
<p>Whether <code>find_library()</code> should find OpenBSD-style shared libraries. </p>
<p> This property is a boolean specifying whether the <code>find_library()</code> command should find shared libraries with OpenBSD-style versioned extension: &quot;.so.&lt;major&gt;.&lt;minor&gt;&quot;. The property is set to true on OpenBSD and false on other platforms.</p>
<h3>Global_Depends_Debug_Mode</h3>
<p>Enable global target dependency graph debug mode. </p>
<p> CMake automatically analyzes the global inter-target dependency graph at the beginning of native build system generation. This property causes it to display details of its analysis to stderr.</p>
<h3>Global_Depends_No_Cycles</h3>
<p>Disallow global target dependency graph cycles. </p>
<p> CMake automatically analyzes the global inter-target dependency graph at the beginning of native build system generation. It reports an error if the dependency graph contains a cycle that does not consist of all STATIC library targets. This property tells CMake to disallow all cycles completely, even among static libraries.</p>
<h3>In_Try_Compile</h3>
<p>Read-only property that is true during a try-compile configuration. </p>
<p> True when building a project inside a <code>try_compile()</code> or <code>try_run()</code> command.</p>
<h3>Packages_Found</h3>
<p>List of packages which were found during the CMake run. </p>
<p> List of packages which were found during the CMake run. Whether a package has been found is determined using the &lt;NAME&gt;_FOUND variables.</p>
<h3>Packages_Not_Found</h3>
<p>List of packages which were not found during the CMake run. </p>
<p> List of packages which were not found during the CMake run. Whether a package has been found is determined using the &lt;NAME&gt;_FOUND variables.</p>
<h3>Job_Pools</h3>
<p>Ninja only: List of available pools. </p>
<p> A pool is a named integer property and defines the maximum number of concurrent jobs which can be started by a rule assigned to the pool. The <code>JOB_POOLS</code> property is a semicolon-separated list of pairs using the syntax NAME=integer (without a space after the equality sign). </p>
<p> For instance: </p>
<pre>set_property(GLOBAL PROPERTY JOB_POOLS two_jobs=2 ten_jobs=10)</pre>
<p>Defined pools could be used globally by setting <code>CMAKE_JOB_POOL_COMPILE</code> and <code>CMAKE_JOB_POOL_LINK</code> or per target by setting the target properties <code>JOB_POOL_COMPILE</code> and <code>JOB_POOL_LINK</code>. </p>
<p> Build targets provided by CMake that are meant for individual interactive use, such as <code>install</code>, are placed in the <code>console</code> pool automatically.</p>
<h3>Predefined_Targets_Folder</h3>
<p>Name of FOLDER for targets that are added automatically by CMake. </p>
<p> If not set, CMake uses &quot;CMakePredefinedTargets&quot; as a default value for this property. Targets such as INSTALL, PACKAGE and RUN_TESTS will be organized into this FOLDER. See also the documentation for the <code>FOLDER</code> target property.</p>
<h3>Eclipse_Extra_Natures</h3>
<p>List of natures to add to the generated Eclipse project file. </p>
<p> Eclipse projects specify language plugins by using natures. This property should be set to the unique identifier for a nature (which looks like a Java package name).</p>
<h3>Report_Undefined_Properties</h3>
<p>If set, report any undefined properties to this file. </p>
<p> If this property is set to a filename then when CMake runs it will report any properties or variables that were accessed but not defined into the filename specified in this property.</p>
<h3>Rule_Launch_Compile</h3>
<p>Specify a launcher for compile rules. </p>
<p> <i>Makefile Generators</i> and the <code>Ninja</code> generator prefix compiler commands with the given launcher command line. This is intended to allow launchers to intercept build problems with high granularity. Other generators ignore this property because their underlying build systems provide no hook to wrap individual commands with a launcher.</p>
<h3>Rule_Launch_Custom</h3>
<p>Specify a launcher for custom rules. </p>
<p> <i>Makefile Generators</i> and the <code>Ninja</code> generator prefix custom commands with the given launcher command line. This is intended to allow launchers to intercept build problems with high granularity. Other generators ignore this property because their underlying build systems provide no hook to wrap individual commands with a launcher.</p>
<h3>Rule_Launch_Link</h3>
<p>Specify a launcher for link rules. </p>
<p> <i>Makefile Generators</i> and the <code>Ninja</code> generator prefix link and archive commands with the given launcher command line. This is intended to allow launchers to intercept build problems with high granularity. Other generators ignore this property because their underlying build systems provide no hook to wrap individual commands with a launcher.</p>
<h3>Rule_Messages</h3>
<p>Specify whether to report a message for each make rule. </p>
<p> This property specifies whether Makefile generators should add a progress message describing what each build rule does. If the property is not set the default is ON. Set the property to OFF to disable granular messages and report only as each target completes. This is intended to allow scripted builds to avoid the build time cost of detailed reports. If a <code>CMAKE_RULE_MESSAGES</code> cache entry exists its value initializes the value of this property. Non-Makefile generators currently ignore this property.</p>
<h3>Target_Archives_May_Be_Shared_Libs</h3>
<p>Set if shared libraries may be named like archives. </p>
<p> On AIX shared libraries may be named &quot;lib&lt;name&gt;.a&quot;. This property is set to true on such platforms.</p>
<h3>Target_Messages</h3>
<p>Specify whether to report the completion of each target. </p>
<p> This property specifies whether <i>Makefile Generators</i> should add a progress message describing that each target has been completed. If the property is not set the default is <code>ON</code>. Set the property to <code>OFF</code> to disable target completion messages. </p>
<p> This option is intended to reduce build output when little or no work needs to be done to bring the build tree up to date. </p>
<p> If a <code>CMAKE_TARGET_MESSAGES</code> cache entry exists its value initializes the value of this property. </p>
<p> Non-Makefile generators currently ignore this property. </p>
<p> See the counterpart property <code>RULE_MESSAGES</code> to disable everything except for target completion messages.</p>
<h3>Target_Supports_Shared_Libs</h3>
<p>Does the target platform support shared libraries. </p>
<p> TARGET_SUPPORTS_SHARED_LIBS is a boolean specifying whether the target platform supports shared libraries. Basically all current general general purpose OS do so, the exception are usually embedded systems with no or special OSs.</p>
<h3>Use_Folders</h3>
<p>Use the <code>FOLDER</code> target property to organize targets into folders. </p>
<p> If not set, CMake treats this property as OFF by default. CMake generators that are capable of organizing into a hierarchy of folders use the values of the <code>FOLDER</code> target property to name those folders. See also the documentation for the FOLDER target property.</p>
<h2>Properties On Directories</h2>
<h3>Additional_Make_Clean_Files</h3>
<p>Additional files to clean during the make clean stage. </p>
<p> A list of files that will be cleaned as a part of the &quot;make clean&quot; stage.</p>
<h3>Cache_Variables</h3>
<p>List of cache variables available in the current directory. </p>
<p> This read-only property specifies the list of CMake cache variables currently defined. It is intended for debugging purposes.</p>
<h3>Clean_No_Custom</h3>
<p>Set to true to tell <i>Makefile Generators</i> not to remove the outputs of custom commands for this directory during the <code>make clean</code> operation. This is ignored on other generators because it is not possible to implement.</p>
<h3>Cmake_Configure_Depends</h3>
<p>Tell CMake about additional input files to the configuration process. If any named file is modified the build system will re-run CMake to re-configure the file and generate the build system again. </p>
<p> Specify files as a semicolon-separated list of paths. Relative paths are interpreted as relative to the current source directory.</p>
<h3>Compile_Definitions</h3>
<p>Preprocessor definitions for compiling a directory&#8217;s sources. </p>
<p> This property specifies the list of options given so far to the <code>add_definitions()</code> command. </p>
<p> The <code>COMPILE_DEFINITIONS</code> property may be set to a semicolon-separated list of preprocessor definitions using the syntax <code>VAR</code> or <code>VAR=value</code>. Function-style definitions are not supported. CMake will automatically escape the value correctly for the native build system (note that CMake language syntax may require escapes to specify some values). </p>
<p> This property will be initialized in each directory by its value in the directory&#8217;s parent. </p>
<p> CMake will automatically drop some definitions that are not supported by the native build tool. </p>
<p> Disclaimer: Most native build tools have poor support for escaping certain values. CMake has work-arounds for many cases but some values may just not be possible to pass correctly. If a value does not seem to be escaped correctly, do not attempt to work-around the problem by adding escape sequences to the value. Your work-around may break in a future version of CMake that has improved escape support. Instead consider defining the macro in a (configured) header file. Then report the limitation. Known limitations include: </p>
<pre># - broken almost everywhere
; - broken in VS IDE 7.0 and Borland Makefiles
, - broken in VS IDE
% - broken in some cases in NMake
&amp; | - broken in some cases on MinGW
^ &lt; &gt; \&quot; - broken in most Make tools on Windows</pre>
<p>CMake does not reject these values outright because they do work in some cases. Use with caution. </p>
<p> Contents of <code>COMPILE_DEFINITIONS</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties. </p>
<p> The corresponding <code>COMPILE_DEFINITIONS_&lt;CONFIG&gt;</code> property may be set to specify per-configuration definitions. Generator expressions should be preferred instead of setting the alternative property.</p>
<h3>Compile_Options</h3>
<p>List of options to pass to the compiler. </p>
<p> This property holds a <i>;-list</i> of options given so far to the <code>add_compile_options()</code> command. </p>
<p> This property is used to initialize the <code>COMPILE_OPTIONS</code> target property when a target is created, which is used by the generators to set the options for the compiler. </p>
<p> Contents of <code>COMPILE_OPTIONS</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.</p>
<h3>Definitions</h3>
<p>For CMake 2.4 compatibility only. Use <code>COMPILE_DEFINITIONS</code> instead. </p>
<p> This read-only property specifies the list of flags given so far to the <code>add_definitions()</code> command. It is intended for debugging purposes. Use the <code>COMPILE_DEFINITIONS</code> directory property instead. </p>
<p> This built-in read-only property does not exist if policy <code>CMP0059</code> is set to <code>NEW</code>.</p>
<h3>Exclude_From_All</h3>
<p>Exclude the directory from the all target of its parent. </p>
<p> A property on a directory that indicates if its targets are excluded from the default build target. If it is not, then with a Makefile for example typing make will cause the targets to be built. The same concept applies to the default build of other generators.</p>
<h3>Implicit_Depends_Include_Transform</h3>
<p>Specify #include line transforms for dependencies in a directory. </p>
<p> This property specifies rules to transform macro-like #include lines during implicit dependency scanning of C and C++ source files. The list of rules must be semicolon-separated with each entry of the form &quot;A_MACRO(%)=value-with-%&quot; (the % must be literal). During dependency scanning occurrences of A_MACRO(&#8230;) on #include lines will be replaced by the value given with the macro argument substituted for &#8216;%&#8217;. For example, the entry </p>
<pre>MYDIR(%)=&lt;mydir/%&gt;</pre>
<p>will convert lines of the form </p>
<pre>#include MYDIR(myheader.h)</pre>
<p>to </p>
<pre>#include &lt;mydir/myheader.h&gt;</pre>
<p>allowing the dependency to be followed. </p>
<p> This property applies to sources in all targets within a directory. The property value is initialized in each directory by its value in the directory&#8217;s parent.</p>
<h3>Include_Directories</h3>
<p>List of preprocessor include file search directories. </p>
<p> This property specifies the list of directories given so far to the <code>include_directories()</code> command. </p>
<p> This property is used to populate the <code>INCLUDE_DIRECTORIES</code> target property, which is used by the generators to set the include directories for the compiler. </p>
<p> In addition to accepting values from that command, values may be set directly on any directory using the <code>set_property()</code> command. A directory gets its initial value from its parent directory if it has one. The initial value of the <code>INCLUDE_DIRECTORIES</code> target property comes from the value of this property. Both directory and target property values are adjusted by calls to the <code>include_directories()</code> command. </p>
<p> The target property values are used by the generators to set the include paths for the compiler. </p>
<p> Contents of <code>INCLUDE_DIRECTORIES</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.</p>
<h3>Include_Regular_Expression</h3>
<p>Include file scanning regular expression. </p>
<p> This property specifies the regular expression used during dependency scanning to match include files that should be followed. See the <code>include_regular_expression()</code> command for a high-level interface to set this property.</p>
<h3>INTERPROCEDURAL_OPTIMIZATION_&lt;CONFIG&gt;</h3>
<p>Per-configuration interprocedural optimization for a directory. </p>
<p> This is a per-configuration version of INTERPROCEDURAL_OPTIMIZATION. If set, this property overrides the generic property for the named configuration.</p>
<h3>Interprocedural_Optimization</h3>
<p>Enable interprocedural optimization for targets in a directory. </p>
<p> If set to true, enables interprocedural optimizations if they are known to be supported by the compiler.</p>
<h3>Link_Directories</h3>
<p>List of linker search directories. </p>
<p> This read-only property specifies the list of directories given so far to the link_directories command. It is intended for debugging purposes.</p>
<h3>Listfile_Stack</h3>
<p>The current stack of listfiles being processed. </p>
<p> This property is mainly useful when trying to debug errors in your CMake scripts. It returns a list of what list files are currently being processed, in order. So if one listfile does an <code>include()</code> command then that is effectively pushing the included listfile onto the stack.</p>
<h3>Macros</h3>
<p>List of macro commands available in the current directory. </p>
<p> This read-only property specifies the list of CMake macros currently defined. It is intended for debugging purposes. See the macro command.</p>
<h3>Parent_Directory</h3>
<p>Source directory that added current subdirectory. </p>
<p> This read-only property specifies the source directory that added the current source directory as a subdirectory of the build. In the top-level directory the value is the empty-string.</p>
<h3>Rule_Launch_Compile</h3>
<p>Specify a launcher for compile rules. </p>
<p> See the global property of the same name for details. This overrides the global property for a directory.</p>
<h3>Rule_Launch_Custom</h3>
<p>Specify a launcher for custom rules. </p>
<p> See the global property of the same name for details. This overrides the global property for a directory.</p>
<h3>Rule_Launch_Link</h3>
<p>Specify a launcher for link rules. </p>
<p> See the global property of the same name for details. This overrides the global property for a directory.</p>
<h3>Test_Include_File</h3>
<p>A cmake file that will be included when ctest is run. </p>
<p> If you specify TEST_INCLUDE_FILE, that file will be included and processed when ctest is run on the directory.</p>
<h3>Variables</h3>
<p>List of variables defined in the current directory. </p>
<p> This read-only property specifies the list of CMake variables currently defined. It is intended for debugging purposes.</p>
<h3>VS_GLOBAL_SECTION_POST_&lt;section&gt;</h3>
<p>Specify a postSolution global section in Visual Studio. </p>
<p> Setting a property like this generates an entry of the following form in the solution file: </p>
<pre>GlobalSection(&lt;section&gt;) = postSolution
 &lt;contents based on property value&gt;
EndGlobalSection</pre>
<p>The property must be set to a semicolon-separated list of key=value pairs. Each such pair will be transformed into an entry in the solution global section. Whitespace around key and value is ignored. List elements which do not contain an equal sign are skipped. </p>
<p> This property only works for Visual Studio 7 and above; it is ignored on other generators. The property only applies when set on a directory whose CMakeLists.txt contains a project() command. </p>
<p> Note that CMake generates postSolution sections ExtensibilityGlobals and ExtensibilityAddIns by default. If you set the corresponding property, it will override the default section. For example, setting VS_GLOBAL_SECTION_POST_ExtensibilityGlobals will override the default contents of the ExtensibilityGlobals section, while keeping ExtensibilityAddIns on its default.</p>
<h3>VS_GLOBAL_SECTION_PRE_&lt;section&gt;</h3>
<p>Specify a preSolution global section in Visual Studio. </p>
<p> Setting a property like this generates an entry of the following form in the solution file: </p>
<pre>GlobalSection(&lt;section&gt;) = preSolution
 &lt;contents based on property value&gt;
EndGlobalSection</pre>
<p>The property must be set to a semicolon-separated list of key=value pairs. Each such pair will be transformed into an entry in the solution global section. Whitespace around key and value is ignored. List elements which do not contain an equal sign are skipped. </p>
<p> This property only works for Visual Studio 7 and above; it is ignored on other generators. The property only applies when set on a directory whose CMakeLists.txt contains a project() command.</p>
<h3>Vs_Startup_Project</h3>
<p>Specify the default startup project in a Visual Studio solution. </p>
<p> The <i>Visual Studio Generators</i> create a <code>.sln</code> file for each directory whose <code>CMakeLists.txt</code> file calls the <code>project()</code> command. Set this property in the same directory as a <code>project()</code> command call (e.g. in the top-level <code>CMakeLists.txt</code> file) to specify the default startup project for the correpsonding solution file. </p>
<p> The property must be set to the name of an existing target. This will cause that project to be listed first in the generated solution file causing Visual Studio to make it the startup project if the solution has never been opened before. </p>
<p> If this property is not specified, then the <code>ALL_BUILD</code> project will be the default.</p>
<h2>Properties On Targets</h2>
<h3>Aliased_Target</h3>
<p>Name of target aliased by this target. </p>
<p> If this is an <i>Alias Target</i>, this property contains the name of the target aliased.</p>
<h3>Android_Ant_Additional_Options</h3>
<p>Set the additional options for Android Ant build system. This is a string value containing all command line options for the Ant build. This property is initialized by the value of the <code>CMAKE_ANDROID_ANT_ADDITIONAL_OPTIONS</code> variable if it is set when a target is created.</p>
<h3>Android_Api</h3>
<p>Set the Android Target API version (e.g. <code>15</code>). The version number must be a positive decimal integer. This property is initialized by the value of the <code>CMAKE_ANDROID_API</code> variable if it is set when a target is created.</p>
<h3>Android_Api_Min</h3>
<p>Set the Android MIN API version (e.g. <code>9</code>). The version number must be a positive decimal integer. This property is initialized by the value of the <code>CMAKE_ANDROID_API_MIN</code> variable if it is set when a target is created. Native code builds using this API version.</p>
<h3>Android_Arch</h3>
<p>Set the Android target architecture. </p>
<p> This is a string property that could be set to the one of the following values:</p>
<dl>
<dt>&bull;</p>
<dd><code>armv7-a</code>: &quot;ARMv7-A (armv7-a)&quot;</p>
<dt>&bull;</p>
<dd><code>armv7-a-hard</code>: &quot;ARMv7-A, hard-float ABI (armv7-a)&quot;</p>
<dt>&bull;</p>
<dd><code>arm64-v8a</code>: &quot;ARMv8-A, 64bit (arm64-v8a)&quot;</p>
<dt>&bull;</p>
<dd><code>x86</code>: &quot;x86 (x86)&quot;</p>
<dt>&bull;</p>
<dd><code>x86_64</code>: &quot;x86_64 (x86_64)&quot; </p>
<p> This property is initialized by the value of the <code>CMAKE_ANDROID_ARCH</code> variable if it is set when a target is created.</dl>
<h3>Android_Assets_Directories</h3>
<p>Set the Android assets directories to copy into the main assets folder before build. This a string property that contains the directory paths separated by semicolon. This property is initialized by the value of the <code>CMAKE_ANDROID_ASSETS_DIRECTORIES</code> variable if it is set when a target is created.</p>
<h3>Android_Gui</h3>
<p>Build an executable as an application package on Android. </p>
<p> When this property is set to true the executable when built for Android will be created as an application package. This property is initialized by the value of the <code>CMAKE_ANDROID_GUI</code> variable if it is set when a target is created. </p>
<p> Add the <code>AndroidManifest.xml</code> source file explicitly to the target <code>add_executable()</code> command invocation to specify the root directory of the application package source.</p>
<h3>Android_Jar_Dependencies</h3>
<p>Set the Android property that specifies JAR dependencies. This is a string value property. This property is initialized by the value of the <code>CMAKE_ANDROID_JAR_DEPENDENCIES</code> variable if it is set when a target is created.</p>
<h3>Android_Jar_Directories</h3>
<p>Set the Android property that specifies directories to search for the JAR libraries. </p>
<p> This a string property that contains the directory paths separated by semicolons. This property is initialized by the value of the <code>CMAKE_ANDROID_JAR_DIRECTORIES</code> variable if it is set when a target is created. </p>
<p> Contents of <code>ANDROID_JAR_DIRECTORIES</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions.</p>
<h3>Android_Java_Source_Dir</h3>
<p>Set the Android property that defines the Java source code root directories. This a string property that contains the directory paths separated by semicolon. This property is initialized by the value of the <code>CMAKE_ANDROID_JAVA_SOURCE_DIR</code> variable if it is set when a target is created.</p>
<h3>Android_Native_Lib_Dependencies</h3>
<p>Set the Android property that specifies the .so dependencies. This is a string property. </p>
<p> This property is initialized by the value of the <code>CMAKE_ANDROID_NATIVE_LIB_DEPENDENCIES</code> variable if it is set when a target is created. </p>
<p> Contents of <code>ANDROID_NATIVE_LIB_DEPENDENCIES</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions.</p>
<h3>Android_Native_Lib_Directories</h3>
<p>Set the Android property that specifies directories to search for the </p>
<p> This a string property that contains the directory paths separated by semicolons. </p>
<p> This property is initialized by the value of the <code>CMAKE_ANDROID_NATIVE_LIB_DIRECTORIES</code> variable if it is set when a target is created. </p>
<p> Contents of <code>ANDROID_NATIVE_LIB_DIRECTORIES</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions.</p>
<h3>Android_Process_Max</h3>
<p>Set the Android property that defines the maximum number of a parallel Android NDK compiler processes (e.g. <code>4</code>). This property is initialized by the value of the <code>CMAKE_ANDROID_PROCESS_MAX</code> variable if it is set when a target is created.</p>
<h3>Android_Proguard</h3>
<p>When this property is set to true that enables the ProGuard tool to shrink, optimize, and obfuscate the code by removing unused code and renaming classes, fields, and methods with semantically obscure names. This property is initialized by the value of the <code>CMAKE_ANDROID_PROGUARD</code> variable if it is set when a target is created.</p>
<h3>Android_Proguard_Config_Path</h3>
<p>Set the Android property that specifies the location of the ProGuard config file. Leave empty to use the default one. This a string property that contains the path to ProGuard config file. This property is initialized by the value of the <code>CMAKE_ANDROID_PROGUARD_CONFIG_PATH</code> variable if it is set when a target is created.</p>
<h3>Android_Secure_Props_Path</h3>
<p>Set the Android property that states the location of the secure properties file. This is a string property that contains the file path. This property is initialized by the value of the <code>CMAKE_ANDROID_SECURE_PROPS_PATH</code> variable if it is set when a target is created.</p>
<h3>Android_Skip_Ant_Step</h3>
<p>Set the Android property that defines whether or not to skip the Ant build step. This is a boolean property initialized by the value of the <code>CMAKE_ANDROID_SKIP_ANT_STEP</code> variable if it is set when a target is created.</p>
<h3>Android_Stl_Type</h3>
<p>Set the Android property that defines the type of STL support for the project. This is a string property that could set to the one of the following values: <code>none</code> e.g. &quot;No C++ Support&quot; <code>system</code> e.g. &quot;Minimal C++ without STL&quot; <code>gabi++_static</code> e.g. &quot;GAbi++ Static&quot; <code>gabi++_shared</code> e.g. &quot;GAbi++ Shared&quot; <code>gnustl_static</code> e.g. &quot;GNU libstdc++ Static&quot; <code>gnustl_shared</code> e.g. &quot;GNU libstdc++ Shared&quot; <code>stlport_static</code> e.g. &quot;STLport Static&quot; <code>stlport_shared</code> e.g. &quot;STLport Shared&quot; This property is initialized by the value of the variable:<i>CMAKE_ANDROID_STL_TYPE</i> variable if it is set when a target is created.</p>
<h3>ARCHIVE_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</h3>
<p>Per-configuration output directory for <i>ARCHIVE</i> target files. </p>
<p> This is a per-configuration version of the <code>ARCHIVE_OUTPUT_DIRECTORY</code> target property, but multi-configuration generators (VS, Xcode) do NOT append a per-configuration subdirectory to the specified directory. This property is initialized by the value of the <code>CMAKE_ARCHIVE_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> variable if it is set when a target is created. </p>
<p> Contents of <code>ARCHIVE_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> may use <code>generator expressions</code>.</p>
<h3>Archive_Output_Directory</h3>
<p>Output directory in which to build <i>ARCHIVE</i> target files. </p>
<p> This property specifies the directory into which archive target files should be built. The property value may use <code>generator expressions</code>. Multi-configuration generators (VS, Xcode) append a per-configuration subdirectory to the specified directory unless a generator expression is used. </p>
<p> This property is initialized by the value of the variable CMAKE_ARCHIVE_OUTPUT_DIRECTORY if it is set when a target is created. </p>
<p> See also the <code>ARCHIVE_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> target property.</p>
<h3>ARCHIVE_OUTPUT_NAME_&lt;CONFIG&gt;</h3>
<p>Per-configuration output name for <i>ARCHIVE</i> target files. </p>
<p> This is the configuration-specific version of the <code>ARCHIVE_OUTPUT_NAME</code> target property.</p>
<h3>Archive_Output_Name</h3>
<p>Output name for <i>ARCHIVE</i> target files. </p>
<p> This property specifies the base name for archive target files. It overrides <code>OUTPUT_NAME</code> and <code>OUTPUT_NAME_&lt;CONFIG&gt;</code> properties. </p>
<p> See also the <code>ARCHIVE_OUTPUT_NAME_&lt;CONFIG&gt;</code> target property.</p>
<h3>Autogen_Target_Depends</h3>
<p>Target dependencies of the corresponding <code>_automoc</code> target. </p>
<p> Targets which have their <code>AUTOMOC</code> target <code>ON</code> have a corresponding <code>_automoc</code> target which is used to autogenerate generate moc files. As this <code>_automoc</code> target is created at generate-time, it is not possible to define dependencies of it, such as to create inputs for the <code>moc</code> executable. </p>
<p> The <code>AUTOGEN_TARGET_DEPENDS</code> target property can be set instead to a list of dependencies for the <code>_automoc</code> target. The buildsystem will be generated to depend on its contents. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-qt/">cmake3-qt</a>(7)</code> manual for more information on using CMake with Qt.</p>
<h3>Automoc_Moc_Options</h3>
<p>Additional options for moc when using <code>AUTOMOC</code> </p>
<p> This property is only used if the <code>AUTOMOC</code> property is <code>ON</code> for this target. In this case, it holds additional command line options which will be used when <code>moc</code> is executed during the build, i.e. it is equivalent to the optional <code>OPTIONS</code> argument of the <code>qt4_wrap_cpp()</code> macro. </p>
<p> By default it is empty. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-qt/">cmake3-qt</a>(7)</code> manual for more information on using CMake with Qt.</p>
<h3>Automoc</h3>
<p>Should the target be processed with automoc (for Qt projects). </p>
<p> AUTOMOC is a boolean specifying whether CMake will handle the Qt <code>moc</code> preprocessor automatically, i.e. without having to use the <code>QT4_WRAP_CPP()</code> or QT5_WRAP_CPP() macro. Currently Qt4 and Qt5 are supported. </p>
<p> When this property is set <code>ON</code>, CMake will scan the source files at build time and invoke moc accordingly.</p>
<dl>
<dt>&bull;</p>
<dd>If an <code>#include</code> statement like <code>#include &quot;moc_foo.cpp&quot;</code> is found, the <code>Q_OBJECT</code> class declaration is expected in the header, and <code>moc</code> is run on the header file. A <code>moc_foo.cpp</code> file will be generated from the source&#8217;s header into the <code>CMAKE_CURRENT_BINARY_DIR</code> directory. This allows the compiler to find the included <code>moc_foo.cpp</code> file regardless of the location the original source. However, if multiple source files in different directories do this then their generated moc files would collide. In this case a diagnostic will be issued.</p>
<dt>&bull;</p>
<dd>If an <code>#include</code> statement like <code>#include &quot;foo.moc&quot;</code> is found, then a <code>Q_OBJECT</code> is expected in the current source file and <code>moc</code> is run on the file itself. Additionally, header files with the same base name (like <code>foo.h</code>) or <code>_p</code> appended to the base name (like <code>foo_p.h</code>) are parsed for <code>Q_OBJECT</code> macros, and if found, <code>moc</code> is also executed on those files. <code>AUTOMOC</code> checks multiple header alternative extensions, such as <code>hpp</code>, <code>hxx</code> etc when searching for headers. The resulting moc files, which are not included as shown above in any of the source files are included in a generated <code>&lt;targetname&gt;_automoc.cpp</code> file, which is compiled as part of the target. </p>
<p> This property is initialized by the value of the <code>CMAKE_AUTOMOC</code> variable if it is set when a target is created. </p>
<p> Additional command line options for moc can be set via the <code>AUTOMOC_MOC_OPTIONS</code> property. </p>
<p> By enabling the <code>CMAKE_AUTOMOC_RELAXED_MODE</code> variable the rules for searching the files which will be processed by moc can be relaxed. See the documentation for this variable for more details. </p>
<p> The global property <code>AUTOGEN_TARGETS_FOLDER</code> can be used to group the automoc targets together in an IDE, e.g. in MSVS. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-qt/">cmake3-qt</a>(7)</code> manual for more information on using CMake with Qt.</dl>
<h3>Autouic</h3>
<p>Should the target be processed with autouic (for Qt projects). </p>
<p> <code>AUTOUIC</code> is a boolean specifying whether CMake will handle the Qt <code>uic</code> code generator automatically, i.e. without having to use the <code>QT4_WRAP_UI()</code> or <code>QT5_WRAP_UI()</code> macro. Currently Qt4 and Qt5 are supported. </p>
<p> When this property is <code>ON</code>, CMake will scan the source files at build time and invoke <code>uic</code> accordingly. If an <code>#include</code> statement like <code>#include &quot;ui_foo.h&quot;</code> is found in <code>foo.cpp</code>, a <code>foo.ui</code> file is expected next to <code>foo.cpp</code>, and <code>uic</code> is run on the <code>foo.ui</code> file. This property is initialized by the value of the <code>CMAKE_AUTOUIC</code> variable if it is set when a target is created. </p>
<p> Additional command line options for <code>uic</code> can be set via the <code>AUTOUIC_OPTIONS</code> source file property on the <code>foo.ui</code> file. The global property <code>AUTOGEN_TARGETS_FOLDER</code> can be used to group the autouic targets together in an IDE, e.g. in MSVS. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-qt/">cmake3-qt</a>(7)</code> manual for more information on using CMake with Qt.</p>
<h3>Autouic_Options</h3>
<p>Additional options for uic when using <code>AUTOUIC</code> </p>
<p> This property holds additional command line options which will be used when <code>uic</code> is executed during the build via <code>AUTOUIC</code>, i.e. it is equivalent to the optional <code>OPTIONS</code> argument of the <code>qt4_wrap_ui()</code> macro. </p>
<p> By default it is empty. </p>
<p> This property is initialized by the value of the <code>CMAKE_AUTOUIC_OPTIONS</code> variable if it is set when a target is created. </p>
<p> The options set on the target may be overridden by <code>AUTOUIC_OPTIONS</code> set on the <code>.ui</code> source file. </p>
<p> This property may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-qt/">cmake3-qt</a>(7)</code> manual for more information on using CMake with Qt.</p>
<h3>Autorcc</h3>
<p>Should the target be processed with autorcc (for Qt projects). </p>
<p> <code>AUTORCC</code> is a boolean specifying whether CMake will handle the Qt <code>rcc</code> code generator automatically, i.e. without having to use the <code>QT4_ADD_RESOURCES()</code> or <code>QT5_ADD_RESOURCES()</code> macro. Currently Qt4 and Qt5 are supported. </p>
<p> When this property is <code>ON</code>, CMake will handle <code>.qrc</code> files added as target sources at build time and invoke <code>rcc</code> accordingly. This property is initialized by the value of the <code>CMAKE_AUTORCC</code> variable if it is set when a target is created. </p>
<p> Additional command line options for rcc can be set via the <code>AUTORCC_OPTIONS</code> source file property on the <code>.qrc</code> file. </p>
<p> The global property <code>AUTOGEN_TARGETS_FOLDER</code> can be used to group the autorcc targets together in an IDE, e.g. in MSVS. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-qt/">cmake3-qt</a>(7)</code> manual for more information on using CMake with Qt.</p>
<h3>Autorcc_Options</h3>
<p>Additional options for <code>rcc</code> when using <code>AUTORCC</code> </p>
<p> This property holds additional command line options which will be used when <code>rcc</code> is executed during the build via <code>AUTORCC</code>, i.e. it is equivalent to the optional <code>OPTIONS</code> argument of the <code>qt4_add_resources()</code> macro. </p>
<p> By default it is empty. </p>
<p> This property is initialized by the value of the <code>CMAKE_AUTORCC_OPTIONS</code> variable if it is set when a target is created. </p>
<p> The options set on the target may be overridden by <code>AUTORCC_OPTIONS</code> set on the <code>.qrc</code> source file. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-qt/">cmake3-qt</a>(7)</code> manual for more information on using CMake with Qt.</p>
<h3>Binary_Dir</h3>
<p>This read-only property reports the value of the <code>CMAKE_CURRENT_BINARY_DIR</code> variable in the directory in which the target was defined.</p>
<h3>Build_With_Install_Rpath</h3>
<p>Should build tree targets have install tree rpaths. </p>
<p> BUILD_WITH_INSTALL_RPATH is a boolean specifying whether to link the target in the build tree with the INSTALL_RPATH. This takes precedence over SKIP_BUILD_RPATH and avoids the need for relinking before installation. This property is initialized by the value of the variable CMAKE_BUILD_WITH_INSTALL_RPATH if it is set when a target is created.</p>
<h3>Bundle_Extension</h3>
<p>The file extension used to name a <code>BUNDLE</code> target on the OS X and iOS. </p>
<p> The default value is <code>bundle</code> &#8211; you can also use <code>plugin</code> or whatever file extension is required by the host app for your bundle.</p>
<h3>Bundle</h3>
<p>This target is a <code>CFBundle</code> on the OS X. </p>
<p> If a module library target has this property set to true it will be built as a <code>CFBundle</code> when built on the mac. It will have the directory structure required for a <code>CFBundle</code> and will be suitable to be used for creating Browser Plugins or other application resources.</p>
<h3>C_Extensions</h3>
<p>Boolean specifying whether compiler specific extensions are requested. </p>
<p> This property specifies whether compiler specific extensions should be used. For some compilers, this results in adding a flag such as <code>-std=gnu11</code> instead of <code>-std=c11</code> to the compile line. This property is <code>ON</code> by default. The basic C standard level is controlled by the <code>C_STANDARD</code> target property. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-compile-features/">cmake3-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers. </p>
<p> This property is initialized by the value of the <code>CMAKE_C_EXTENSIONS</code> variable if it is set when a target is created.</p>
<h3>C_Standard</h3>
<p>The C standard whose features are requested to build this target. </p>
<p> This property specifies the C standard whose features are requested to build this target. For some compilers, this results in adding a flag such as <code>-std=gnu11</code> to the compile line. For compilers that have no notion of a standard level, such as MSVC, this has no effect. </p>
<p> Supported values are <code>90</code>, <code>99</code> and <code>11</code>. </p>
<p> If the value requested does not result in a compile flag being added for the compiler in use, a previous standard flag will be added instead. This means that using: </p>
<pre>set_property(TARGET tgt PROPERTY C_STANDARD 11)</pre>
<p>with a compiler which does not support <code>-std=gnu11</code> or an equivalent flag will not result in an error or warning, but will instead add the <code>-std=gnu99</code> or <code>-std=gnu90</code> flag if supported. This &quot;decay&quot; behavior may be controlled with the <code>C_STANDARD_REQUIRED</code> target property. Additionally, the <code>C_EXTENSIONS</code> target property may be used to control whether compiler-specific extensions are enabled on a per-target basis. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-compile-features/">cmake3-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers. </p>
<p> This property is initialized by the value of the <code>CMAKE_C_STANDARD</code> variable if it is set when a target is created.</p>
<h3>C_Standard_Required</h3>
<p>Boolean describing whether the value of <code>C_STANDARD</code> is a requirement. </p>
<p> If this property is set to <code>ON</code>, then the value of the <code>C_STANDARD</code> target property is treated as a requirement. If this property is <code>OFF</code> or unset, the <code>C_STANDARD</code> target property is treated as optional and may &quot;decay&quot; to a previous standard if the requested is not available. For compilers that have no notion of a standard level, such as MSVC, this has no effect. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-compile-features/">cmake3-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers. </p>
<p> This property is initialized by the value of the <code>CMAKE_C_STANDARD_REQUIRED</code> variable if it is set when a target is created.</p>
<h3>Compatible_Interface_Bool</h3>
<p>Properties which must be compatible with their link interface </p>
<p> The <code>COMPATIBLE_INTERFACE_BOOL</code> property may contain a list of properties for this target which must be consistent when evaluated as a boolean with the <code>INTERFACE</code> variant of the property in all linked dependees. For example, if a property <code>FOO</code> appears in the list, then for each dependee, the <code>INTERFACE_FOO</code> property content in all of its dependencies must be consistent with each other, and with the <code>FOO</code> property in the depender. </p>
<p> Consistency in this sense has the meaning that if the property is set, then it must have the same boolean value as all others, and if the property is not set, then it is ignored. </p>
<p> Note that for each dependee, the set of properties specified in this property must not intersect with the set specified in any of the other <i>Compatible Interface Properties</i>.</p>
<h3>Compatible_Interface_Number_Max</h3>
<p>Properties whose maximum value from the link interface will be used. </p>
<p> The <code>COMPATIBLE_INTERFACE_NUMBER_MAX</code> property may contain a list of properties for this target whose maximum value may be read at generate time when evaluated in the <code>INTERFACE</code> variant of the property in all linked dependees. For example, if a property <code>FOO</code> appears in the list, then for each dependee, the <code>INTERFACE_FOO</code> property content in all of its dependencies will be compared with each other and with the <code>FOO</code> property in the depender. When reading the <code>FOO</code> property at generate time, the maximum value will be returned. If the property is not set, then it is ignored. </p>
<p> Note that for each dependee, the set of properties specified in this property must not intersect with the set specified in any of the other <i>Compatible Interface Properties</i>.</p>
<h3>Compatible_Interface_Number_Min</h3>
<p>Properties whose maximum value from the link interface will be used. </p>
<p> The <code>COMPATIBLE_INTERFACE_NUMBER_MIN</code> property may contain a list of properties for this target whose minimum value may be read at generate time when evaluated in the <code>INTERFACE</code> variant of the property of all linked dependees. For example, if a property <code>FOO</code> appears in the list, then for each dependee, the <code>INTERFACE_FOO</code> property content in all of its dependencies will be compared with each other and with the <code>FOO</code> property in the depender. When reading the <code>FOO</code> property at generate time, the minimum value will be returned. If the property is not set, then it is ignored. </p>
<p> Note that for each dependee, the set of properties specified in this property must not intersect with the set specified in any of the other <i>Compatible Interface Properties</i>.</p>
<h3>Compatible_Interface_String</h3>
<p>Properties which must be string-compatible with their link interface </p>
<p> The <code>COMPATIBLE_INTERFACE_STRING</code> property may contain a list of properties for this target which must be the same when evaluated as a string in the <code>INTERFACE</code> variant of the property all linked dependees. For example, if a property <code>FOO</code> appears in the list, then for each dependee, the <code>INTERFACE_FOO</code> property content in all of its dependencies must be equal with each other, and with the <code>FOO</code> property in the depender. If the property is not set, then it is ignored. </p>
<p> Note that for each dependee, the set of properties specified in this property must not intersect with the set specified in any of the other <i>Compatible Interface Properties</i>.</p>
<h3>Compile_Definitions</h3>
<p>Preprocessor definitions for compiling a target&#8217;s sources. </p>
<p> The <code>COMPILE_DEFINITIONS</code> property may be set to a semicolon-separated list of preprocessor definitions using the syntax <code>VAR</code> or <code>VAR=value</code>. Function-style definitions are not supported. CMake will automatically escape the value correctly for the native build system (note that CMake language syntax may require escapes to specify some values). </p>
<p> CMake will automatically drop some definitions that are not supported by the native build tool. </p>
<p> Disclaimer: Most native build tools have poor support for escaping certain values. CMake has work-arounds for many cases but some values may just not be possible to pass correctly. If a value does not seem to be escaped correctly, do not attempt to work-around the problem by adding escape sequences to the value. Your work-around may break in a future version of CMake that has improved escape support. Instead consider defining the macro in a (configured) header file. Then report the limitation. Known limitations include: </p>
<pre># - broken almost everywhere
; - broken in VS IDE 7.0 and Borland Makefiles
, - broken in VS IDE
% - broken in some cases in NMake
&amp; | - broken in some cases on MinGW
^ &lt; &gt; \&quot; - broken in most Make tools on Windows</pre>
<p>CMake does not reject these values outright because they do work in some cases. Use with caution. </p>
<p> Contents of <code>COMPILE_DEFINITIONS</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties. </p>
<p> The corresponding <code>COMPILE_DEFINITIONS_&lt;CONFIG&gt;</code> property may be set to specify per-configuration definitions. Generator expressions should be preferred instead of setting the alternative property.</p>
<h3>Compile_Features</h3>
<p>Compiler features enabled for this target. </p>
<p> The list of features in this property are a subset of the features listed in the <code>CMAKE_CXX_COMPILE_FEATURES</code> variable. </p>
<p> Contents of <code>COMPILE_FEATURES</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-compile-features/">cmake3-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.</p>
<h3>Compile_Flags</h3>
<p>Additional flags to use when compiling this target&#8217;s sources. </p>
<p> The <code>COMPILE_FLAGS</code> property sets additional compiler flags used to build sources within the target. Use <code>COMPILE_DEFINITIONS</code> to pass additional preprocessor definitions. </p>
<p> This property is deprecated. Use the <code>COMPILE_OPTIONS</code> property or the command:<i>target_compile_options</i> command instead.</p>
<h3>Compile_Options</h3>
<p>List of options to pass to the compiler. </p>
<p> This property holds a <i>;-list</i> of options specified so far for its target. Use the <code>target_compile_options()</code> command to append more options. </p>
<p> This property is initialized by the <code>COMPILE_OPTIONS</code> directory property when a target is created, and is used by the generators to set the options for the compiler. </p>
<p> Contents of <code>COMPILE_OPTIONS</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.</p>
<h3>Compile_Pdb_Name</h3>
<p>Output name for the MS debug symbol <code>.pdb</code> file generated by the compiler while building source files. </p>
<p> This property specifies the base name for the debug symbols file. If not set, the default is unspecified. </p>
<p> <code>NOTE:</code> The compiler-generated program database files are specified by the <code>/Fd</code> compiler flag and are not the same as linker-generated program database files specified by the <code>/pdb</code> linker flag. Use the <code>PDB_NAME</code> property to specify the latter.</p>
<h3>COMPILE_PDB_NAME_&lt;CONFIG&gt;</h3>
<p>Per-configuration output name for the MS debug symbol <code>.pdb</code> file generated by the compiler while building source files. </p>
<p> This is the configuration-specific version of <code>COMPILE_PDB_NAME</code>. </p>
<p> <code>NOTE:</code> The compiler-generated program database files are specified by the <code>/Fd</code> compiler flag and are not the same as linker-generated program database files specified by the <code>/pdb</code> linker flag. Use the <code>PDB_NAME_&lt;CONFIG&gt;</code> property to specify the latter.</p>
<h3>Compile_Pdb_Output_Directory</h3>
<p>Output directory for the MS debug symbol <code>.pdb</code> file generated by the compiler while building source files. </p>
<p> This property specifies the directory into which the MS debug symbols will be placed by the compiler. This property is initialized by the value of the <code>CMAKE_COMPILE_PDB_OUTPUT_DIRECTORY</code> variable if it is set when a target is created. </p>
<p> <code>NOTE:</code> The compiler-generated program database files are specified by the <code>/Fd</code> compiler flag and are not the same as linker-generated program database files specified by the <code>/pdb</code> linker flag. Use the <code>PDB_OUTPUT_DIRECTORY</code> property to specify the latter.</p>
<h3>COMPILE_PDB_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</h3>
<p>Per-configuration output directory for the MS debug symbol <code>.pdb</code> file generated by the compiler while building source files. </p>
<p> This is a per-configuration version of <code>COMPILE_PDB_OUTPUT_DIRECTORY</code>, but multi-configuration generators (VS, Xcode) do NOT append a per-configuration subdirectory to the specified directory. This property is initialized by the value of the <code>CMAKE_COMPILE_PDB_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> variable if it is set when a target is created. </p>
<p> <code>NOTE:</code> The compiler-generated program database files are specified by the <code>/Fd</code> compiler flag and are not the same as linker-generated program database files specified by the <code>/pdb</code> linker flag. Use the <code>PDB_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> property to specify the latter.</p>
<h3>&lt;CONFIG&gt;_OUTPUT_NAME</h3>
<p>Old per-configuration target file base name. Use <code>OUTPUT_NAME_&lt;CONFIG&gt;</code> instead. </p>
<p> This is a configuration-specific version of the <code>OUTPUT_NAME</code> target property.</p>
<h3>&lt;CONFIG&gt;_POSTFIX</h3>
<p>Postfix to append to the target file name for configuration &lt;CONFIG&gt;. </p>
<p> When building with configuration &lt;CONFIG&gt; the value of this property is appended to the target file name built on disk. For non-executable targets, this property is initialized by the value of the variable CMAKE_&lt;CONFIG&gt;_POSTFIX if it is set when a target is created. This property is ignored on the Mac for Frameworks and App Bundles.</p>
<h3>Crosscompiling_Emulator</h3>
<p>Use the given emulator to run executables created when crosscompiling. This command will be added as a prefix to <code>add_test()</code>, <code>add_custom_command()</code>, and <code>add_custom_target()</code> commands for built target system executables.</p>
<h3>Cxx_Extensions</h3>
<p>Boolean specifying whether compiler specific extensions are requested. </p>
<p> This property specifies whether compiler specific extensions should be used. For some compilers, this results in adding a flag such as <code>-std=gnu++11</code> instead of <code>-std=c++11</code> to the compile line. This property is <code>ON</code> by default. The basic C++ standard level is controlled by the <code>CXX_STANDARD</code> target property. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-compile-features/">cmake3-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers. </p>
<p> This property is initialized by the value of the <code>CMAKE_CXX_EXTENSIONS</code> variable if it is set when a target is created.</p>
<h3>Cxx_Standard</h3>
<p>The C++ standard whose features are requested to build this target. </p>
<p> This property specifies the C++ standard whose features are requested to build this target. For some compilers, this results in adding a flag such as <code>-std=gnu++11</code> to the compile line. For compilers that have no notion of a standard level, such as MSVC, this has no effect. </p>
<p> Supported values are <code>98</code>, <code>11</code> and <code>14</code>. </p>
<p> If the value requested does not result in a compile flag being added for the compiler in use, a previous standard flag will be added instead. This means that using: </p>
<pre>set_property(TARGET tgt PROPERTY CXX_STANDARD 11)</pre>
<p>with a compiler which does not support <code>-std=gnu++11</code> or an equivalent flag will not result in an error or warning, but will instead add the <code>-std=gnu++98</code> flag if supported. This &quot;decay&quot; behavior may be controlled with the <code>CXX_STANDARD_REQUIRED</code> target property. Additionally, the <code>CXX_EXTENSIONS</code> target property may be used to control whether compiler-specific extensions are enabled on a per-target basis. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-compile-features/">cmake3-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers. </p>
<p> This property is initialized by the value of the <code>CMAKE_CXX_STANDARD</code> variable if it is set when a target is created.</p>
<h3>Cxx_Standard_Required</h3>
<p>Boolean describing whether the value of <code>CXX_STANDARD</code> is a requirement. </p>
<p> If this property is set to <code>ON</code>, then the value of the <code>CXX_STANDARD</code> target property is treated as a requirement. If this property is <code>OFF</code> or unset, the <code>CXX_STANDARD</code> target property is treated as optional and may &quot;decay&quot; to a previous standard if the requested is not available. For compilers that have no notion of a standard level, such as MSVC, this has no effect. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-compile-features/">cmake3-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers. </p>
<p> This property is initialized by the value of the <code>CMAKE_CXX_STANDARD_REQUIRED</code> variable if it is set when a target is created.</p>
<h3>Debug_Postfix</h3>
<p>See target property &lt;CONFIG&gt;_POSTFIX. </p>
<p> This property is a special case of the more-general &lt;CONFIG&gt;_POSTFIX property for the DEBUG configuration.</p>
<h3>Define_Symbol</h3>
<p>Define a symbol when compiling this target&#8217;s sources. </p>
<p> DEFINE_SYMBOL sets the name of the preprocessor symbol defined when compiling sources in a shared library. If not set here then it is set to target_EXPORTS by default (with some substitutions if the target is not a valid C identifier). This is useful for headers to know whether they are being included from inside their library or outside to properly setup dllexport/dllimport decorations.</p>
<h3>Deployment_Remote_Directory</h3>
<p>Set the WinCE project <code>RemoteDirectory</code> in <code>DeploymentTool</code> and <code>RemoteExecutable</code> in <code>DebuggerTool</code> in <code>.vcproj</code> files generated by the <code>Visual Studio 9 2008</code> and <code>Visual Studio 8 2005</code> generators. This is useful when you want to debug on remote WinCE device. For example: </p>
<pre>set_property(TARGET ${TARGET} PROPERTY
 DEPLOYMENT_REMOTE_DIRECTORY &quot;\FlashStorage&quot;)</pre>
<p>produces: </p>
<pre>&lt;DeploymentTool RemoteDirectory=&quot;\FlashStorage&quot; ... /&gt;
&lt;DebuggerTool RemoteExecutable=&quot;\FlashStorage	arget_file&quot; ... /&gt;</pre>
<h3>EchoString</h3>
<p>A message to be displayed when the target is built. </p>
<p> A message to display on some generators (such as makefiles) when the target is built.</p>
<h3>Enable_Exports</h3>
<p>Specify whether an executable exports symbols for loadable modules. </p>
<p> Normally an executable does not export any symbols because it is the final program. It is possible for an executable to export symbols to be used by loadable modules. When this property is set to true CMake will allow other targets to &quot;link&quot; to the executable with the <code>TARGET_LINK_LIBRARIES()</code> command. On all platforms a target-level dependency on the executable is created for targets that link to it. For DLL platforms an import library will be created for the exported symbols and then used for linking. All Windows-based systems including Cygwin are DLL platforms. For non-DLL platforms that require all symbols to be resolved at link time, such as OS X, the module will &quot;link&quot; to the executable using a flag like <code>-bundle_loader</code>. For other non-DLL platforms the link rule is simply ignored since the dynamic loader will automatically bind symbols when the module is loaded. </p>
<p> This property is initialized by the value of the variable <code>CMAKE_ENABLE_EXPORTS</code> if it is set when a target is created.</p>
<h3>Exclude_From_All</h3>
<p>Exclude the target from the all target. </p>
<p> A property on a target that indicates if the target is excluded from the default build target. If it is not, then with a Makefile for example typing make will cause this target to be built. The same concept applies to the default build of other generators. Installing a target with EXCLUDE_FROM_ALL set to true has undefined behavior.</p>
<h3>EXCLUDE_FROM_DEFAULT_BUILD_&lt;CONFIG&gt;</h3>
<p>Per-configuration version of target exclusion from &quot;Build Solution&quot;. </p>
<p> This is the configuration-specific version of EXCLUDE_FROM_DEFAULT_BUILD. If the generic EXCLUDE_FROM_DEFAULT_BUILD is also set on a target, EXCLUDE_FROM_DEFAULT_BUILD_&lt;CONFIG&gt; takes precedence in configurations for which it has a value.</p>
<h3>Exclude_From_Default_Build</h3>
<p>Exclude target from &quot;Build Solution&quot;. </p>
<p> This property is only used by Visual Studio generators 7 and above. When set to TRUE, the target will not be built when you press &quot;Build Solution&quot;.</p>
<h3>Export_Name</h3>
<p>Exported name for target files. </p>
<p> This sets the name for the IMPORTED target generated when it this target is is exported. If not set, the logical target name is used by default.</p>
<h3>Folder</h3>
<p>Set the folder name. Use to organize targets in an IDE. </p>
<p> Targets with no FOLDER property will appear as top level entities in IDEs like Visual Studio. Targets with the same FOLDER property value will appear next to each other in a folder of that name. To nest folders, use FOLDER values such as &#8216;GUI/Dialogs&#8217; with &#8216;/&#8217; characters separating folder levels.</p>
<h3>Fortran_FORMAT</h3>
<p>Set to FIXED or FREE to indicate the Fortran source layout. </p>
<p> This property tells CMake whether the Fortran source files in a target use fixed-format or free-format. CMake will pass the corresponding format flag to the compiler. Use the source-specific Fortran_FORMAT property to change the format of a specific source file. If the variable CMAKE_Fortran_FORMAT is set when a target is created its value is used to initialize this property.</p>
<h3>Fortran_MODULE_DIRECTORY</h3>
<p>Specify output directory for Fortran modules provided by the target. </p>
<p> If the target contains Fortran source files that provide modules and the compiler supports a module output directory this specifies the directory in which the modules will be placed. When this property is not set the modules will be placed in the build directory corresponding to the target&#8217;s source directory. If the variable CMAKE_Fortran_MODULE_DIRECTORY is set when a target is created its value is used to initialize this property. </p>
<p> Note that some compilers will automatically search the module output directory for modules USEd during compilation but others will not. If your sources USE modules their location must be specified by INCLUDE_DIRECTORIES regardless of this property.</p>
<h3>Framework</h3>
<p>Build <code>SHARED</code> library as Framework Bundle on the OS X and iOS. </p>
<p> If a <code>SHARED</code> library target has this property set to <code>TRUE</code> it will be built as a framework when built on the OS X and iOS. It will have the directory structure required for a framework and will be suitable to be used with the <code>-framework</code> option </p>
<p> To customize <code>Info.plist</code> file in the framework, use <code>MACOSX_FRAMEWORK_INFO_PLIST</code> target property. </p>
<p> For OS X see also the <code>FRAMEWORK_VERSION</code> target property. </p>
<p> Example of creation <code>dynamicFramework</code>: </p>
<pre>add_library(dynamicFramework SHARED
 dynamicFramework.c
 dynamicFramework.h
)
set_target_properties(dynamicFramework PROPERTIES
 FRAMEWORK TRUE
 FRAMEWORK_VERSION C
 MACOSX_FRAMEWORK_IDENTIFIER com.cmake.dynamicFramework
 MACOSX_FRAMEWORK_INFO_PLIST Info.plist
 # &quot;current version&quot; in semantic format in Mach-O binary file
 VERSION 16.4.0
 # &quot;compatibility version&quot; in semantic format in Mach-O binary file
 SOVERSION 1.0.0
 PUBLIC_HEADER dynamicFramework.h
 XCODE_ATTRIBUTE_CODE_SIGN_IDENTITY &quot;iPhone Developer&quot;
)</pre>
<h3>Framework_Version</h3>
<p>Version of a framework created using the <code>FRAMEWORK</code> target property (e.g. <code>A</code>). </p>
<p> This property only affects OS X, as iOS doesn&#8217;t have versioned directory structure.</p>
<h3>Generator_File_Name</h3>
<p>Generator&#8217;s file for this target. </p>
<p> An internal property used by some generators to record the name of the project or dsp file associated with this target. Note that at configure time, this property is only set for targets created by include_external_msproject().</p>
<h3>GNUtoMS</h3>
<p>Convert GNU import library (.dll.a) to MS format (.lib). </p>
<p> When linking a shared library or executable that exports symbols using GNU tools on Windows (MinGW/MSYS) with Visual Studio installed convert the import library (.dll.a) from GNU to MS format (.lib). Both import libraries will be installed by install(TARGETS) and exported by install(EXPORT) and export() to be linked by applications with either GNU- or MS-compatible tools. </p>
<p> If the variable CMAKE_GNUtoMS is set when a target is created its value is used to initialize this property. The variable must be set prior to the first command that enables a language such as project() or enable_language(). CMake provides the variable as an option to the user automatically when configuring on Windows with GNU tools.</p>
<h3>Has_Cxx</h3>
<p>Link the target using the C++ linker tool (obsolete). </p>
<p> This is equivalent to setting the LINKER_LANGUAGE property to CXX. See that property&#8217;s documentation for details.</p>
<h3>Implicit_Depends_Include_Transform</h3>
<p>Specify #include line transforms for dependencies in a target. </p>
<p> This property specifies rules to transform macro-like #include lines during implicit dependency scanning of C and C++ source files. The list of rules must be semicolon-separated with each entry of the form &quot;A_MACRO(%)=value-with-%&quot; (the % must be literal). During dependency scanning occurrences of A_MACRO(&#8230;) on #include lines will be replaced by the value given with the macro argument substituted for &#8216;%&#8217;. For example, the entry </p>
<pre>MYDIR(%)=&lt;mydir/%&gt;</pre>
<p>will convert lines of the form </p>
<pre>#include MYDIR(myheader.h)</pre>
<p>to </p>
<pre>#include &lt;mydir/myheader.h&gt;</pre>
<p>allowing the dependency to be followed. </p>
<p> This property applies to sources in the target on which it is set.</p>
<h3>Imported_Configurations</h3>
<p>Configurations provided for an IMPORTED target. </p>
<p> Set this to the list of configuration names available for an IMPORTED target. The names correspond to configurations defined in the project from which the target is imported. If the importing project uses a different set of configurations the names may be mapped using the MAP_IMPORTED_CONFIG_&lt;CONFIG&gt; property. Ignored for non-imported targets.</p>
<h3>IMPORTED_IMPLIB_&lt;CONFIG&gt;</h3>
<p>&lt;CONFIG&gt;-specific version of IMPORTED_IMPLIB property. </p>
<p> Configuration names correspond to those provided by the project from which the target is imported.</p>
<h3>Imported_Implib</h3>
<p>Full path to the import library for an IMPORTED target. </p>
<p> Set this to the location of the &quot;.lib&quot; part of a windows DLL. Ignored for non-imported targets.</p>
<h3>IMPORTED_LINK_DEPENDENT_LIBRARIES_&lt;CONFIG&gt;</h3>
<p>&lt;CONFIG&gt;-specific version of IMPORTED_LINK_DEPENDENT_LIBRARIES. </p>
<p> Configuration names correspond to those provided by the project from which the target is imported. If set, this property completely overrides the generic property for the named configuration.</p>
<h3>Imported_Link_Dependent_Libraries</h3>
<p>Dependent shared libraries of an imported shared library. </p>
<p> Shared libraries may be linked to other shared libraries as part of their implementation. On some platforms the linker searches for the dependent libraries of shared libraries they are including in the link. Set this property to the list of dependent shared libraries of an imported library. The list should be disjoint from the list of interface libraries in the INTERFACE_LINK_LIBRARIES property. On platforms requiring dependent shared libraries to be found at link time CMake uses this list to add appropriate files or paths to the link command line. Ignored for non-imported targets.</p>
<h3>IMPORTED_LINK_INTERFACE_LANGUAGES_&lt;CONFIG&gt;</h3>
<p>&lt;CONFIG&gt;-specific version of IMPORTED_LINK_INTERFACE_LANGUAGES. </p>
<p> Configuration names correspond to those provided by the project from which the target is imported. If set, this property completely overrides the generic property for the named configuration.</p>
<h3>Imported_Link_Interface_Languages</h3>
<p>Languages compiled into an IMPORTED static library. </p>
<p> Set this to the list of languages of source files compiled to produce a STATIC IMPORTED library (such as &quot;C&quot; or &quot;CXX&quot;). CMake accounts for these languages when computing how to link a target to the imported library. For example, when a C executable links to an imported C++ static library CMake chooses the C++ linker to satisfy language runtime dependencies of the static library. </p>
<p> This property is ignored for targets that are not STATIC libraries. This property is ignored for non-imported targets.</p>
<h3>IMPORTED_LINK_INTERFACE_LIBRARIES_&lt;CONFIG&gt;</h3>
<p>&lt;CONFIG&gt;-specific version of IMPORTED_LINK_INTERFACE_LIBRARIES. </p>
<p> Configuration names correspond to those provided by the project from which the target is imported. If set, this property completely overrides the generic property for the named configuration. </p>
<p> This property is ignored if the target also has a non-empty INTERFACE_LINK_LIBRARIES property. </p>
<p> This property is deprecated. Use INTERFACE_LINK_LIBRARIES instead.</p>
<h3>Imported_Link_Interface_Libraries</h3>
<p>Transitive link interface of an IMPORTED target. </p>
<p> Set this to the list of libraries whose interface is included when an IMPORTED library target is linked to another target. The libraries will be included on the link line for the target. Unlike the LINK_INTERFACE_LIBRARIES property, this property applies to all imported target types, including STATIC libraries. This property is ignored for non-imported targets. </p>
<p> This property is ignored if the target also has a non-empty INTERFACE_LINK_LIBRARIES property. </p>
<p> This property is deprecated. Use INTERFACE_LINK_LIBRARIES instead.</p>
<h3>IMPORTED_LINK_INTERFACE_MULTIPLICITY_&lt;CONFIG&gt;</h3>
<p>&lt;CONFIG&gt;-specific version of IMPORTED_LINK_INTERFACE_MULTIPLICITY. </p>
<p> If set, this property completely overrides the generic property for the named configuration.</p>
<h3>Imported_Link_Interface_Multiplicity</h3>
<p>Repetition count for cycles of IMPORTED static libraries. </p>
<p> This is LINK_INTERFACE_MULTIPLICITY for IMPORTED targets.</p>
<h3>IMPORTED_LOCATION_&lt;CONFIG&gt;</h3>
<p>&lt;CONFIG&gt;-specific version of IMPORTED_LOCATION property. </p>
<p> Configuration names correspond to those provided by the project from which the target is imported.</p>
<h3>Imported_Location</h3>
<p>Full path to the main file on disk for an IMPORTED target. </p>
<p> Set this to the location of an IMPORTED target file on disk. For executables this is the location of the executable file. For bundles on OS X this is the location of the executable file inside Contents/MacOS under the application bundle folder. For static libraries and modules this is the location of the library or module. For shared libraries on non-DLL platforms this is the location of the shared library. For frameworks on OS X this is the location of the library file symlink just inside the framework folder. For DLLs this is the location of the &quot;.dll&quot; part of the library. For UNKNOWN libraries this is the location of the file to be linked. Ignored for non-imported targets. </p>
<p> Projects may skip IMPORTED_LOCATION if the configuration-specific property IMPORTED_LOCATION_&lt;CONFIG&gt; is set. To get the location of an imported target read one of the LOCATION or LOCATION_&lt;CONFIG&gt; properties.</p>
<h3>IMPORTED_NO_SONAME_&lt;CONFIG&gt;</h3>
<p>&lt;CONFIG&gt;-specific version of IMPORTED_NO_SONAME property. </p>
<p> Configuration names correspond to those provided by the project from which the target is imported.</p>
<h3>Imported_No_Soname</h3>
<p>Specifies that an IMPORTED shared library target has no &quot;soname&quot;. </p>
<p> Set this property to true for an imported shared library file that has no &quot;soname&quot; field. CMake may adjust generated link commands for some platforms to prevent the linker from using the path to the library in place of its missing soname. Ignored for non-imported targets.</p>
<h3>Imported</h3>
<p>Read-only indication of whether a target is IMPORTED. </p>
<p> The boolean value of this property is <code>True</code> for targets created with the IMPORTED option to <code>add_executable()</code> or <code>add_library()</code>. It is <code>False</code> for targets built within the project.</p>
<h3>IMPORTED_SONAME_&lt;CONFIG&gt;</h3>
<p>&lt;CONFIG&gt;-specific version of IMPORTED_SONAME property. </p>
<p> Configuration names correspond to those provided by the project from which the target is imported.</p>
<h3>Imported_Soname</h3>
<p>The &quot;soname&quot; of an IMPORTED target of shared library type. </p>
<p> Set this to the &quot;soname&quot; embedded in an imported shared library. This is meaningful only on platforms supporting the feature. Ignored for non-imported targets.</p>
<h3>Import_Prefix</h3>
<p>What comes before the import library name. </p>
<p> Similar to the target property PREFIX, but used for import libraries (typically corresponding to a DLL) instead of regular libraries. A target property that can be set to override the prefix (such as &quot;lib&quot;) on an import library name.</p>
<h3>Import_Suffix</h3>
<p>What comes after the import library name. </p>
<p> Similar to the target property SUFFIX, but used for import libraries (typically corresponding to a DLL) instead of regular libraries. A target property that can be set to override the suffix (such as &quot;.lib&quot;) on an import library name.</p>
<h3>Include_Directories</h3>
<p>List of preprocessor include file search directories. </p>
<p> This property specifies the list of directories given so far to the <code>target_include_directories()</code> command. In addition to accepting values from that command, values may be set directly on any target using the <code>set_property()</code> command. A target gets its initial value for this property from the value of the <code>INCLUDE_DIRECTORIES</code> directory property. Both directory and target property values are adjusted by calls to the <code>include_directories()</code> command. </p>
<p> The value of this property is used by the generators to set the include paths for the compiler. </p>
<p> Relative paths should not be added to this property directly. Use one of the commands above instead to handle relative paths. </p>
<p> Contents of <code>INCLUDE_DIRECTORIES</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.</p>
<h3>Install_Name_Dir</h3>
<p>Mac OSX directory name for installed targets. </p>
<p> INSTALL_NAME_DIR is a string specifying the directory portion of the &quot;install_name&quot; field of shared libraries on Mac OSX to use in the installed targets.</p>
<h3>Install_Rpath</h3>
<p>The rpath to use for installed targets. </p>
<p> A semicolon-separated list specifying the rpath to use in installed targets (for platforms that support it). This property is initialized by the value of the variable CMAKE_INSTALL_RPATH if it is set when a target is created.</p>
<h3>Install_Rpath_Use_Link_Path</h3>
<p>Add paths to linker search and installed rpath. </p>
<p> INSTALL_RPATH_USE_LINK_PATH is a boolean that if set to true will append directories in the linker search path and outside the project to the INSTALL_RPATH. This property is initialized by the value of the variable CMAKE_INSTALL_RPATH_USE_LINK_PATH if it is set when a target is created.</p>
<h3>Interface_Autouic_Options</h3>
<p>List of interface options to pass to uic. </p>
<p> Targets may populate this property to publish the options required to use when invoking <code>uic</code>. Consuming targets can add entries to their own <code>AUTOUIC_OPTIONS</code> property such as <code>$&lt;TARGET_PROPERTY:foo,INTERFACE_AUTOUIC_OPTIONS&gt;</code> to use the uic options specified in the interface of <code>foo</code>. This is done automatically by the <code>target_link_libraries()</code> command. </p>
<p> This property supports generator expressions. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions.</p>
<h3>Interface_Compile_Definitions</h3>
<p>List of public compile definitions requirements for a library. </p>
<p> Targets may populate this property to publish the compile definitions required to compile against the headers for the target. The <code>target_compile_definitions()</code> command populates this property with values given to the <code>PUBLIC</code> and <code>INTERFACE</code> keywords. Projects may also get and set the property directly. </p>
<p> When target dependencies are specified using <code>target_link_libraries()</code>, CMake will read this property from all target dependencies to determine the build properties of the consumer. </p>
<p> Contents of <code>INTERFACE_COMPILE_DEFINITIONS</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake-buildsystem/">cmake-buildsystem</a>(7)</code> -manual for more on defining buildsystem properties.</p>
<h3>Interface_Compile_Features</h3>
<p>List of public compile features requirements for a library. </p>
<p> Targets may populate this property to publish the compile features required to compile against the headers for the target. The <code>target_compile_features()</code> command populates this property with values given to the <code>PUBLIC</code> and <code>INTERFACE</code> keywords. Projects may also get and set the property directly. </p>
<p> When target dependencies are specified using <code>target_link_libraries()</code>, CMake will read this property from all target dependencies to determine the build properties of the consumer. </p>
<p> Contents of <code>INTERFACE_COMPILE_FEATURES</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake-buildsystem/">cmake-buildsystem</a>(7)</code> -manual for more on defining buildsystem properties. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-compile-features/">cmake3-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.</p>
<h3>Interface_Compile_Options</h3>
<p>List of public compile options requirements for a library. </p>
<p> Targets may populate this property to publish the compile options required to compile against the headers for the target. The <code>target_compile_options()</code> command populates this property with values given to the <code>PUBLIC</code> and <code>INTERFACE</code> keywords. Projects may also get and set the property directly. </p>
<p> When target dependencies are specified using <code>target_link_libraries()</code>, CMake will read this property from all target dependencies to determine the build properties of the consumer. </p>
<p> Contents of <code>INTERFACE_COMPILE_OPTIONS</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake-buildsystem/">cmake-buildsystem</a>(7)</code> -manual for more on defining buildsystem properties.</p>
<h3>Interface_Include_Directories</h3>
<p>List of public include directories requirements for a library. </p>
<p> Targets may populate this property to publish the include directories required to compile against the headers for the target. The <code>target_include_directories()</code> command populates this property with values given to the <code>PUBLIC</code> and <code>INTERFACE</code> keywords. Projects may also get and set the property directly. </p>
<p> When target dependencies are specified using <code>target_link_libraries()</code>, CMake will read this property from all target dependencies to determine the build properties of the consumer. </p>
<p> Contents of <code>INTERFACE_INCLUDE_DIRECTORIES</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake-buildsystem/">cmake-buildsystem</a>(7)</code> -manual for more on defining buildsystem properties. </p>
<p> Include directories usage requirements commonly differ between the build-tree and the install-tree. The <code>BUILD_INTERFACE</code> and <code>INSTALL_INTERFACE</code> generator expressions can be used to describe separate usage requirements based on the usage location. Relative paths are allowed within the <code>INSTALL_INTERFACE</code> expression and are interpreted relative to the installation prefix. For example: </p>
<pre>target_include_directories(mylib INTERFACE
 $&lt;BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include/mylib&gt;
 $&lt;INSTALL_INTERFACE:include/mylib&gt; # &lt;prefix&gt;/include/mylib
)</pre>
<h3>Creating Relocatable Packages</h3>
<p>Note that it is not advisable to populate the <code>INSTALL_INTERFACE</code> of the <code>INTERFACE_INCLUDE_DIRECTORIES</code> of a target with absolute paths to the include directories of dependencies. That would hard-code into installed packages the include directory paths for dependencies <code>as found on the machine the package was made on</code>. </p>
<p> The <code>INSTALL_INTERFACE</code> of the <code>INTERFACE_INCLUDE_DIRECTORIES</code> is only suitable for specifying the required include directories for headers provided with the target itself, not those provided by the transitive dependencies listed in its <code>INTERFACE_LINK_LIBRARIES</code> target property. Those dependencies should themselves be targets that specify their own header locations in <code>INTERFACE_INCLUDE_DIRECTORIES</code>. </p>
<p> See the <i>Creating Relocatable Packages</i> section of the <code><a href="/docs/linux/man/7-cmake-packages/">cmake-packages</a>(7)</code> manual for discussion of additional care that must be taken when specifying usage requirements while creating packages for redistribution.</p>
<h3>Interface_Link_Libraries</h3>
<p>List public interface libraries for a library. </p>
<p> This property contains the list of transitive link dependencies. When the target is linked into another target using the <code>target_link_libraries()</code> command, the libraries listed (and recursively their link interface libraries) will be provided to the other target also. This property is overridden by the <code>LINK_INTERFACE_LIBRARIES</code> or <code>LINK_INTERFACE_LIBRARIES_&lt;CONFIG&gt;</code> property if policy <code>CMP0022</code> is <code>OLD</code> or unset. </p>
<p> Contents of <code>INTERFACE_LINK_LIBRARIES</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.</p>
<h3>Creating Relocatable Packages</h3>
<p>Note that it is not advisable to populate the <code>INTERFACE_LINK_LIBRARIES</code> of a target with absolute paths to dependencies. That would hard-code into installed packages the library file paths for dependencies <code>as found on the machine the package was made on</code>. </p>
<p> See the <i>Creating Relocatable Packages</i> section of the <code><a href="/docs/linux/man/7-cmake-packages/">cmake-packages</a>(7)</code> manual for discussion of additional care that must be taken when specifying usage requirements while creating packages for redistribution.</p>
<h3>Interface_Position_Independent_Code</h3>
<p>Whether consumers need to create a position-independent target </p>
<p> The <code>INTERFACE_POSITION_INDEPENDENT_CODE</code> property informs consumers of this target whether they must set their <code>POSITION_INDEPENDENT_CODE</code> property to <code>ON</code>. If this property is set to <code>ON</code>, then the <code>POSITION_INDEPENDENT_CODE</code> property on all consumers will be set to <code>ON</code>. Similarly, if this property is set to <code>OFF</code>, then the <code>POSITION_INDEPENDENT_CODE</code> property on all consumers will be set to <code>OFF</code>. If this property is undefined, then consumers will determine their <code>POSITION_INDEPENDENT_CODE</code> property by other means. Consumers must ensure that the targets that they link to have a consistent requirement for their <code>INTERFACE_POSITION_INDEPENDENT_CODE</code> property.</p>
<h3>Interface_Sources</h3>
<p>List of interface sources to compile into consuming targets. </p>
<p> Targets may populate this property to publish the sources for consuming targets to compile. The <code>target_sources()</code> command populates this property with values given to the <code>PUBLIC</code> and <code>INTERFACE</code> keywords. Projects may also get and set the property directly. </p>
<p> When target dependencies are specified using <code>target_link_libraries()</code>, CMake will read this property from all target dependencies to determine the sources of the consumer. </p>
<p> Contents of <code>INTERFACE_SOURCES</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.</p>
<h3>Interface_System_Include_Directories</h3>
<p>List of public system include directories for a library. </p>
<p> Targets may populate this property to publish the include directories which contain system headers, and therefore should not result in compiler warnings. The <code>target_include_directories(SYSTEM)</code> command signature populates this property with values given to the <code>PUBLIC</code> and <code>INTERFACE</code> keywords. </p>
<p> Projects may also get and set the property directly, but must be aware that adding directories to this property does not make those directories used during compilation. Adding directories to this property marks directories as <code>SYSTEM</code> which otherwise would be used in a non-<code>SYSTEM</code> manner. This can appear similar to &#8216;duplication&#8217;, so prefer the high-level <code>target_include_directories(SYSTEM)</code> command and avoid setting the property by low-level means. </p>
<p> When target dependencies are specified using <code>target_link_libraries()</code>, CMake will read this property from all target dependencies to mark the same include directories as containing system headers. </p>
<p> Contents of <code>INTERFACE_SYSTEM_INCLUDE_DIRECTORIES</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.</p>
<h3>INTERPROCEDURAL_OPTIMIZATION_&lt;CONFIG&gt;</h3>
<p>Per-configuration interprocedural optimization for a target. </p>
<p> This is a per-configuration version of INTERPROCEDURAL_OPTIMIZATION. If set, this property overrides the generic property for the named configuration.</p>
<h3>Interprocedural_Optimization</h3>
<p>Enable interprocedural optimization for a target. </p>
<p> If set to true, enables interprocedural optimizations if they are known to be supported by the compiler.</p>
<h3>Ios_Install_Combined</h3>
<p>Build a combined (device and simulator) target when installing. </p>
<p> When this property is set to set to false (which is the default) then it will either be built with the device SDK or the simulator SDK depending on the SDK set. But if this property is set to true then the target will at install time also be built for the corresponding SDK and combined into one library. </p>
<p> This feature requires at least Xcode version 6.</p>
<h3>Job_Pool_Compile</h3>
<p>Ninja only: Pool used for compiling. </p>
<p> The number of parallel compile processes could be limited by defining pools with the global <code>JOB_POOLS</code> property and then specifying here the pool name. </p>
<p> For instance: </p>
<pre>set_property(TARGET myexe PROPERTY JOB_POOL_COMPILE ten_jobs)</pre>
<p>This property is initialized by the value of <code>CMAKE_JOB_POOL_COMPILE</code>.</p>
<h3>Job_Pool_Link</h3>
<p>Ninja only: Pool used for linking. </p>
<p> The number of parallel link processes could be limited by defining pools with the global <code>JOB_POOLS</code> property and then specifying here the pool name. </p>
<p> For instance: </p>
<pre>set_property(TARGET myexe PROPERTY JOB_POOL_LINK two_jobs)</pre>
<p>This property is initialized by the value of <code>CMAKE_JOB_POOL_LINK</code>.</p>
<h3>Labels</h3>
<p>Specify a list of text labels associated with a target. </p>
<p> Target label semantics are currently unspecified.</p>
<h3>&lt;LANG&gt;_CLANG_TIDY</h3>
<p>This property is implemented only when <code>&lt;LANG&gt;</code> is <code>C</code> or <code>CXX</code>. </p>
<p> Specify a <i>;-list</i> containing a command line for the <code>clang-tidy</code> tool. The <i>Makefile Generators</i> and the <code>Ninja</code> generator will run this tool along with the compiler and report a warning if the tool reports any problems. </p>
<p> This property is initialized by the value of the <code>CMAKE_&lt;LANG&gt;_CLANG_TIDY</code> variable if it is set when a target is created.</p>
<h3>&lt;LANG&gt;_COMPILER_LAUNCHER</h3>
<p>This property is implemented only when <code>&lt;LANG&gt;</code> is <code>C</code> or <code>CXX</code>. </p>
<p> Specify a <i>;-list</i> containing a command line for a compiler launching tool. The <i>Makefile Generators</i> and the <code>Ninja</code> generator will run this tool and pass the compiler and its arguments to the tool. Some example tools are distcc and ccache. </p>
<p> This property is initialized by the value of the <code>CMAKE_&lt;LANG&gt;_COMPILER_LAUNCHER</code> variable if it is set when a target is created.</p>
<h3>&lt;LANG&gt;_INCLUDE_WHAT_YOU_USE</h3>
<p>This property is implemented only when <code>&lt;LANG&gt;</code> is <code>C</code> or <code>CXX</code>. </p>
<p> Specify a <i>;-list</i> containing a command line for the <code>include-what-you-use</code> tool. The <i>Makefile Generators</i> and the <code>Ninja</code> generator will run this tool along with the compiler and report a warning if the tool reports any problems. </p>
<p> This property is initialized by the value of the <code>CMAKE_&lt;LANG&gt;_INCLUDE_WHAT_YOU_USE</code> variable if it is set when a target is created.</p>
<h3>&lt;LANG&gt;_VISIBILITY_PRESET</h3>
<p>Value for symbol visibility compile flags </p>
<p> The <code>&lt;LANG&gt;_VISIBILITY_PRESET</code> property determines the value passed in a visibility related compile option, such as <code>-fvisibility=</code> for <code>&lt;LANG&gt;</code>. This property affects compilation in sources of all types of targets (subject to policy <code>CMP0063</code>). </p>
<p> This property is initialized by the value of the <code>CMAKE_&lt;LANG&gt;_VISIBILITY_PRESET</code> variable if it is set when a target is created.</p>
<h3>LIBRARY_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</h3>
<p>Per-configuration output directory for <i>LIBRARY</i> target files. </p>
<p> This is a per-configuration version of the <code>LIBRARY_OUTPUT_DIRECTORY</code> target property, but multi-configuration generators (VS, Xcode) do NOT append a per-configuration subdirectory to the specified directory. This property is initialized by the value of the <code>CMAKE_LIBRARY_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> variable if it is set when a target is created. </p>
<p> Contents of <code>LIBRARY_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> may use <code>generator expressions</code>.</p>
<h3>Library_Output_Directory</h3>
<p>Output directory in which to build <i>LIBRARY</i> target files. </p>
<p> This property specifies the directory into which library target files should be built. The property value may use <code>generator expressions</code>. Multi-configuration generators (VS, Xcode) append a per-configuration subdirectory to the specified directory unless a generator expression is used. </p>
<p> This property is initialized by the value of the variable CMAKE_LIBRARY_OUTPUT_DIRECTORY if it is set when a target is created. </p>
<p> See also the <code>LIBRARY_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> target property.</p>
<h3>LIBRARY_OUTPUT_NAME_&lt;CONFIG&gt;</h3>
<p>Per-configuration output name for <i>LIBRARY</i> target files. </p>
<p> This is the configuration-specific version of the <code>LIBRARY_OUTPUT_NAME</code> target property.</p>
<h3>Library_Output_Name</h3>
<p>Output name for <i>LIBRARY</i> target files. </p>
<p> This property specifies the base name for library target files. It overrides <code>OUTPUT_NAME</code> and <code>OUTPUT_NAME_&lt;CONFIG&gt;</code> properties. </p>
<p> See also the <code>LIBRARY_OUTPUT_NAME_&lt;CONFIG&gt;</code> target property.</p>
<h3>Link_Depends_No_Shared</h3>
<p>Do not depend on linked shared library files. </p>
<p> Set this property to true to tell CMake generators not to add file-level dependencies on the shared library files linked by this target. Modification to the shared libraries will not be sufficient to re-link this target. Logical target-level dependencies will not be affected so the linked shared libraries will still be brought up to date before this target is built. </p>
<p> This property is initialized by the value of the variable CMAKE_LINK_DEPENDS_NO_SHARED if it is set when a target is created.</p>
<h3>Link_Depends</h3>
<p>Additional files on which a target binary depends for linking. </p>
<p> Specifies a semicolon-separated list of full-paths to files on which the link rule for this target depends. The target binary will be linked if any of the named files is newer than it. </p>
<p> This property is ignored by non-Makefile generators. It is intended to specify dependencies on &quot;linker scripts&quot; for custom Makefile link rules.</p>
<h3>Linker_Language</h3>
<p>Specifies language whose compiler will invoke the linker. </p>
<p> For executables, shared libraries, and modules, this sets the language whose compiler is used to link the target (such as &quot;C&quot; or &quot;CXX&quot;). A typical value for an executable is the language of the source file providing the program entry point (main). If not set, the language with the highest linker preference value is the default. See documentation of CMAKE_&lt;LANG&gt;_LINKER_PREFERENCE variables. </p>
<p> If this property is not set by the user, it will be calculated at generate-time by CMake.</p>
<h3>LINK_FLAGS_&lt;CONFIG&gt;</h3>
<p>Per-configuration linker flags for a target. </p>
<p> This is the configuration-specific version of LINK_FLAGS.</p>
<h3>Link_Flags</h3>
<p>Additional flags to use when linking this target. </p>
<p> The LINK_FLAGS property can be used to add extra flags to the link step of a target. LINK_FLAGS_&lt;CONFIG&gt; will add to the configuration &lt;CONFIG&gt;, for example, DEBUG, RELEASE, MINSIZEREL, RELWITHDEBINFO.</p>
<h3>LINK_INTERFACE_LIBRARIES_&lt;CONFIG&gt;</h3>
<p>Per-configuration list of public interface libraries for a target. </p>
<p> This is the configuration-specific version of <code>LINK_INTERFACE_LIBRARIES</code>. If set, this property completely overrides the generic property for the named configuration. </p>
<p> This property is overridden by the <code>INTERFACE_LINK_LIBRARIES</code> property if policy <code>CMP0022</code> is <code>NEW</code>. </p>
<p> This property is deprecated. Use <code>INTERFACE_LINK_LIBRARIES</code> instead.</p>
<h3>Creating Relocatable Packages</h3>
<p>Note that it is not advisable to populate the <code>LINK_INTERFACE_LIBRARIES_&lt;CONFIG&gt;</code> of a target with absolute paths to dependencies. That would hard-code into installed packages the library file paths for dependencies <code>as found on the machine the package was made on</code>. </p>
<p> See the <i>Creating Relocatable Packages</i> section of the <code><a href="/docs/linux/man/7-cmake-packages/">cmake-packages</a>(7)</code> manual for discussion of additional care that must be taken when specifying usage requirements while creating packages for redistribution.</p>
<h3>Link_Interface_Libraries</h3>
<p>List public interface libraries for a shared library or executable. </p>
<p> By default linking to a shared library target transitively links to targets with which the library itself was linked. For an executable with exports (see the <code>ENABLE_EXPORTS</code> target property) no default transitive link dependencies are used. This property replaces the default transitive link dependencies with an explicit list. When the target is linked into another target using the <code>target_link_libraries()</code> command, the libraries listed (and recursively their link interface libraries) will be provided to the other target also. If the list is empty then no transitive link dependencies will be incorporated when this target is linked into another target even if the default set is non-empty. This property is initialized by the value of the <code>CMAKE_LINK_INTERFACE_LIBRARIES</code> variable if it is set when a target is created. This property is ignored for <code>STATIC</code> libraries. </p>
<p> This property is overridden by the <code>INTERFACE_LINK_LIBRARIES</code> property if policy <code>CMP0022</code> is <code>NEW</code>. </p>
<p> This property is deprecated. Use <code>INTERFACE_LINK_LIBRARIES</code> instead.</p>
<h3>Creating Relocatable Packages</h3>
<p>Note that it is not advisable to populate the <code>LINK_INTERFACE_LIBRARIES</code> of a target with absolute paths to dependencies. That would hard-code into installed packages the library file paths for dependencies <code>as found on the machine the package was made on</code>. </p>
<p> See the <i>Creating Relocatable Packages</i> section of the <code><a href="/docs/linux/man/7-cmake-packages/">cmake-packages</a>(7)</code> manual for discussion of additional care that must be taken when specifying usage requirements while creating packages for redistribution.</p>
<h3>LINK_INTERFACE_MULTIPLICITY_&lt;CONFIG&gt;</h3>
<p>Per-configuration repetition count for cycles of STATIC libraries. </p>
<p> This is the configuration-specific version of LINK_INTERFACE_MULTIPLICITY. If set, this property completely overrides the generic property for the named configuration.</p>
<h3>Link_Interface_Multiplicity</h3>
<p>Repetition count for STATIC libraries with cyclic dependencies. </p>
<p> When linking to a STATIC library target with cyclic dependencies the linker may need to scan more than once through the archives in the strongly connected component of the dependency graph. CMake by default constructs the link line so that the linker will scan through the component at least twice. This property specifies the minimum number of scans if it is larger than the default. CMake uses the largest value specified by any target in a component.</p>
<h3>Link_Libraries</h3>
<p>List of direct link dependencies. </p>
<p> This property specifies the list of libraries or targets which will be used for linking. In addition to accepting values from the <code>target_link_libraries()</code> command, values may be set directly on any target using the <code>set_property()</code> command. </p>
<p> The value of this property is used by the generators to set the link libraries for the compiler. </p>
<p> Contents of <code>LINK_LIBRARIES</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.</p>
<h3>Link_Search_End_Static</h3>
<p>End a link line such that static system libraries are used. </p>
<p> Some linkers support switches such as -Bstatic and -Bdynamic to determine whether to use static or shared libraries for -lXXX options. CMake uses these options to set the link type for libraries whose full paths are not known or (in some cases) are in implicit link directories for the platform. By default CMake adds an option at the end of the library list (if necessary) to set the linker search type back to its starting type. This property switches the final linker search type to -Bstatic regardless of how it started. </p>
<p> This property is initialized by the value of the variable CMAKE_LINK_SEARCH_END_STATIC if it is set when a target is created. </p>
<p> See also LINK_SEARCH_START_STATIC.</p>
<h3>Link_Search_Start_Static</h3>
<p>Assume the linker looks for static libraries by default. </p>
<p> Some linkers support switches such as -Bstatic and -Bdynamic to determine whether to use static or shared libraries for -lXXX options. CMake uses these options to set the link type for libraries whose full paths are not known or (in some cases) are in implicit link directories for the platform. By default the linker search type is assumed to be -Bdynamic at the beginning of the library list. This property switches the assumption to -Bstatic. It is intended for use when linking an executable statically (e.g. with the GNU -static option). </p>
<p> This property is initialized by the value of the variable CMAKE_LINK_SEARCH_START_STATIC if it is set when a target is created. </p>
<p> See also LINK_SEARCH_END_STATIC.</p>
<h3>LOCATION_&lt;CONFIG&gt;</h3>
<p>Read-only property providing a target location on disk. </p>
<p> A read-only property that indicates where a target&#8217;s main file is located on disk for the configuration &lt;CONFIG&gt;. The property is defined only for library and executable targets. An imported target may provide a set of configurations different from that of the importing project. By default CMake looks for an exact-match but otherwise uses an arbitrary available configuration. Use the MAP_IMPORTED_CONFIG_&lt;CONFIG&gt; property to map imported configurations explicitly. </p>
<p> Do not set properties that affect the location of a target after reading this property. These include properties whose names match &quot;(RUNTIME|LIBRARY|ARCHIVE)_OUTPUT_(NAME|DIRECTORY)(_&lt;CONFIG&gt;)?&quot;, <code>(IMPLIB_)?(PREFIX|SUFFIX)</code>, or &quot;LINKER_LANGUAGE&quot;. Failure to follow this rule is not diagnosed and leaves the location of the target undefined.</p>
<h3>Location</h3>
<p>Read-only location of a target on disk. </p>
<p> For an imported target, this read-only property returns the value of the LOCATION_&lt;CONFIG&gt; property for an unspecified configuration &lt;CONFIG&gt; provided by the target. </p>
<p> For a non-imported target, this property is provided for compatibility with CMake 2.4 and below. It was meant to get the location of an executable target&#8217;s output file for use in add_custom_command. The path may contain a build-system-specific portion that is replaced at build time with the configuration getting built (such as &quot;$(ConfigurationName)&quot; in VS). In CMake 2.6 and above add_custom_command automatically recognizes a target name in its COMMAND and DEPENDS options and computes the target location. In CMake 2.8.4 and above add_custom_command recognizes generator expressions to refer to target locations anywhere in the command. Therefore this property is not needed for creating custom commands. </p>
<p> Do not set properties that affect the location of a target after reading this property. These include properties whose names match &quot;(RUNTIME|LIBRARY|ARCHIVE)_OUTPUT_(NAME|DIRECTORY)(_&lt;CONFIG&gt;)?&quot;, <code>(IMPLIB_)?(PREFIX|SUFFIX)</code>, or &quot;LINKER_LANGUAGE&quot;. Failure to follow this rule is not diagnosed and leaves the location of the target undefined.</p>
<h3>Macosx_Bundle_Info_Plist</h3>
<p>Specify a custom <code>Info.plist</code> template for a OS X and iOS Application Bundle. </p>
<p> An executable target with <code>MACOSX_BUNDLE</code> enabled will be built as an application bundle on OS X. By default its <code>Info.plist</code> file is created by configuring a template called <code>MacOSXBundleInfo.plist.in</code> located in the <code>CMAKE_MODULE_PATH</code>. This property specifies an alternative template file name which may be a full path. </p>
<p> The following target properties may be set to specify content to be configured into the file:</p>
<dl>
<dt><code>MACOSX_BUNDLE_BUNDLE_NAME</code></p>
<dd>Sets <code>CFBundleName</code>.</p>
<dt><code>MACOSX_BUNDLE_BUNDLE_VERSION</code></p>
<dd>Sets <code>CFBundleVersion</code>.</p>
<dt><code>MACOSX_BUNDLE_COPYRIGHT</code></p>
<dd>Sets <code>NSHumanReadableCopyright</code>.</p>
<dt><code>MACOSX_BUNDLE_GUI_IDENTIFIER</code></p>
<dd>Sets <code>CFBundleIdentifier</code>.</p>
<dt><code>MACOSX_BUNDLE_ICON_FILE</code></p>
<dd>Sets <code>CFBundleIconFile</code>.</p>
<dt><code>MACOSX_BUNDLE_INFO_STRING</code></p>
<dd>Sets <code>CFBundleGetInfoString</code>.</p>
<dt><code>MACOSX_BUNDLE_LONG_VERSION_STRING</code></p>
<dd>Sets <code>CFBundleLongVersionString</code>.</p>
<dt><code>MACOSX_BUNDLE_SHORT_VERSION_STRING</code></p>
<dd>Sets <code>CFBundleShortVersionString</code>. </p>
<p> CMake variables of the same name may be set to affect all targets in a directory that do not have each specific property set. If a custom <code>Info.plist</code> is specified by this property it may of course hard-code all the settings instead of using the target properties.</dl>
<h3>Macosx_Bundle</h3>
<p>Build an executable as an Application Bundle on OS X or iOS. </p>
<p> When this property is set to <code>TRUE</code> the executable when built on OS X or iOS will be created as an application bundle. This makes it a GUI executable that can be launched from the Finder. See the <code>MACOSX_FRAMEWORK_INFO_PLIST</code> target property for information about creation of the <code>Info.plist</code> file for the application bundle. This property is initialized by the value of the variable <code>CMAKE_MACOSX_BUNDLE</code> if it is set when a target is created.</p>
<h3>Macosx_Framework_Info_Plist</h3>
<p>Specify a custom <code>Info.plist</code> template for a OS X and iOS Framework. </p>
<p> A library target with <code>FRAMEWORK</code> enabled will be built as a framework on OS X. By default its <code>Info.plist</code> file is created by configuring a template called <code>MacOSXFrameworkInfo.plist.in</code> located in the <code>CMAKE_MODULE_PATH</code>. This property specifies an alternative template file name which may be a full path. </p>
<p> The following target properties may be set to specify content to be configured into the file:</p>
<dl>
<dt><code>MACOSX_FRAMEWORK_BUNDLE_VERSION</code></p>
<dd>Sets <code>CFBundleVersion</code>.</p>
<dt><code>MACOSX_FRAMEWORK_ICON_FILE</code></p>
<dd>Sets <code>CFBundleIconFile</code>.</p>
<dt><code>MACOSX_FRAMEWORK_IDENTIFIER</code></p>
<dd>Sets <code>CFBundleIdentifier</code>.</p>
<dt><code>MACOSX_FRAMEWORK_SHORT_VERSION_STRING</code></p>
<dd>Sets <code>CFBundleShortVersionString</code>. </p>
<p> CMake variables of the same name may be set to affect all targets in a directory that do not have each specific property set. If a custom <code>Info.plist</code> is specified by this property it may of course hard-code all the settings instead of using the target properties.</dl>
<h3>Macosx_Rpath</h3>
<p>Whether this target on OS X or iOS is located at runtime using rpaths. </p>
<p> When this property is set to <code>TRUE</code>, the directory portion of the <code>install_name</code> field of this shared library will be <code>@rpath</code> unless overridden by <code>INSTALL_NAME_DIR</code>. This indicates the shared library is to be found at runtime using runtime paths (rpaths). </p>
<p> This property is initialized by the value of the variable <code>CMAKE_MACOSX_RPATH</code> if it is set when a target is created. </p>
<p> Runtime paths will also be embedded in binaries using this target and can be controlled by the <code>INSTALL_RPATH</code> target property on the target linking to this target. </p>
<p> Policy <code>CMP0042</code> was introduced to change the default value of <code>MACOSX_RPATH</code> to <code>TRUE</code>. This is because use of <code>@rpath</code> is a more flexible and powerful alternative to <code>@executable_path</code> and <code>@loader_path</code>.</p>
<h3>MAP_IMPORTED_CONFIG_&lt;CONFIG&gt;</h3>
<p>Map from project configuration to IMPORTED target&#8217;s configuration. </p>
<p> Set this to the list of configurations of an imported target that may be used for the current project&#8217;s &lt;CONFIG&gt; configuration. Targets imported from another project may not provide the same set of configuration names available in the current project. Setting this property tells CMake what imported configurations are suitable for use when building the &lt;CONFIG&gt; configuration. The first configuration in the list found to be provided by the imported target is selected. If this property is set and no matching configurations are available, then the imported target is considered to be not found. This property is ignored for non-imported targets. </p>
<p> This property is initialized by the value of the variable CMAKE_MAP_IMPORTED_CONFIG_&lt;CONFIG&gt; if it is set when a target is created.</p>
<h3>Name</h3>
<p>Logical name for the target. </p>
<p> Read-only logical name for the target as used by CMake.</p>
<h3>No_Soname</h3>
<p>Whether to set &quot;soname&quot; when linking a shared library. </p>
<p> Enable this boolean property if a generated shared library should not have &quot;soname&quot; set. Default is to set &quot;soname&quot; on all shared libraries as long as the platform supports it. Generally, use this property only for leaf private libraries or plugins. If you use it on normal shared libraries which other targets link against, on some platforms a linker will insert a full path to the library (as specified at link time) into the dynamic section of the dependent binary. Therefore, once installed, dynamic loader may eventually fail to locate the library for the binary.</p>
<h3>No_System_From_Imported</h3>
<p>Do not treat includes from IMPORTED target interfaces as SYSTEM. </p>
<p> The contents of the INTERFACE_INCLUDE_DIRECTORIES of IMPORTED targets are treated as SYSTEM includes by default. If this property is enabled, the contents of the INTERFACE_INCLUDE_DIRECTORIES of IMPORTED targets are not treated as system includes. This property is initialized by the value of the variable CMAKE_NO_SYSTEM_FROM_IMPORTED if it is set when a target is created.</p>
<h3>OSX_ARCHITECTURES_&lt;CONFIG&gt;</h3>
<p>Per-configuration OS X and iOS binary architectures for a target. </p>
<p> This property is the configuration-specific version of <code>OSX_ARCHITECTURES</code>.</p>
<h3>Osx_Architectures</h3>
<p>Target specific architectures for OS X. </p>
<p> The <code>OSX_ARCHITECTURES</code> property sets the target binary architecture for targets on OS X (<code>-arch</code>). This property is initialized by the value of the variable <code>CMAKE_OSX_ARCHITECTURES</code> if it is set when a target is created. Use <code>OSX_ARCHITECTURES_&lt;CONFIG&gt;</code> to set the binary architectures on a per-configuration basis, where <code>&lt;CONFIG&gt;</code> is an upper-case name (e.g. <code>OSX_ARCHITECTURES_DEBUG</code>).</p>
<h3>OUTPUT_NAME_&lt;CONFIG&gt;</h3>
<p>Per-configuration target file base name. </p>
<p> This is the configuration-specific version of the <code>OUTPUT_NAME</code> target property.</p>
<h3>Output_Name</h3>
<p>Output name for target files. </p>
<p> This sets the base name for output files created for an executable or library target. If not set, the logical target name is used by default. </p>
<p> Contents of <code>OUTPUT_NAME</code> and the variants listed below may use <code>generator expressions</code>. </p>
<p> See also the variants:</p>
<dl>
<dt>&bull;</p>
<dd><code>OUTPUT_NAME_&lt;CONFIG&gt;</code></p>
<dt>&bull;</p>
<dd><code>ARCHIVE_OUTPUT_NAME_&lt;CONFIG&gt;</code></p>
<dt>&bull;</p>
<dd><code>ARCHIVE_OUTPUT_NAME</code></p>
<dt>&bull;</p>
<dd><code>LIBRARY_OUTPUT_NAME_&lt;CONFIG&gt;</code></p>
<dt>&bull;</p>
<dd><code>LIBRARY_OUTPUT_NAME</code></p>
<dt>&bull;</p>
<dd><code>RUNTIME_OUTPUT_NAME_&lt;CONFIG&gt;</code></p>
<dt>&bull;</p>
<dd><code>RUNTIME_OUTPUT_NAME</code></dl>
<h3>PDB_NAME_&lt;CONFIG&gt;</h3>
<p>Per-configuration output name for the MS debug symbol <code>.pdb</code> file generated by the linker for an executable or shared library target. </p>
<p> This is the configuration-specific version of <code>PDB_NAME</code>. </p>
<p> <code>NOTE:</code> This property does not apply to STATIC library targets because no linker is invoked to produce them so they have no linker-generated <code>.pdb</code> file containing debug symbols. </p>
<p> The linker-generated program database files are specified by the <code>/pdb</code> linker flag and are not the same as compiler-generated program database files specified by the <code>/Fd</code> compiler flag. Use the <code>COMPILE_PDB_NAME_&lt;CONFIG&gt;</code> property to specify the latter.</p>
<h3>Pdb_Name</h3>
<p>Output name for the MS debug symbol <code>.pdb</code> file generated by the linker for an executable or shared library target. </p>
<p> This property specifies the base name for the debug symbols file. If not set, the <code>OUTPUT_NAME</code> target property value or logical target name is used by default. </p>
<p> <code>NOTE:</code> This property does not apply to STATIC library targets because no linker is invoked to produce them so they have no linker-generated <code>.pdb</code> file containing debug symbols. </p>
<p> The linker-generated program database files are specified by the <code>/pdb</code> linker flag and are not the same as compiler-generated program database files specified by the <code>/Fd</code> compiler flag. Use the <code>COMPILE_PDB_NAME</code> property to specify the latter.</p>
<h3>PDB_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</h3>
<p>Per-configuration output directory for the MS debug symbol <code>.pdb</code> file generated by the linker for an executable or shared library target. </p>
<p> This is a per-configuration version of <code>PDB_OUTPUT_DIRECTORY</code>, but multi-configuration generators (VS, Xcode) do NOT append a per-configuration subdirectory to the specified directory. This property is initialized by the value of the <code>CMAKE_PDB_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> variable if it is set when a target is created. </p>
<p> <code>NOTE:</code> This property does not apply to STATIC library targets because no linker is invoked to produce them so they have no linker-generated <code>.pdb</code> file containing debug symbols. </p>
<p> The linker-generated program database files are specified by the <code>/pdb</code> linker flag and are not the same as compiler-generated program database files specified by the <code>/Fd</code> compiler flag. Use the <code>COMPILE_PDB_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> property to specify the latter.</p>
<h3>Pdb_Output_Directory</h3>
<p>Output directory for the MS debug symbols <code>.pdb</code> file generated by the linker for an executable or shared library target. </p>
<p> This property specifies the directory into which the MS debug symbols will be placed by the linker. This property is initialized by the value of the <code>CMAKE_PDB_OUTPUT_DIRECTORY</code> variable if it is set when a target is created. </p>
<p> <code>NOTE:</code> This property does not apply to STATIC library targets because no linker is invoked to produce them so they have no linker-generated <code>.pdb</code> file containing debug symbols. </p>
<p> The linker-generated program database files are specified by the <code>/pdb</code> linker flag and are not the same as compiler-generated program database files specified by the <code>/Fd</code> compiler flag. Use the <code>COMPILE_PDB_OUTPUT_DIRECTORY</code> property to specify the latter.</p>
<h3>Position_Independent_Code</h3>
<p>Whether to create a position-independent target </p>
<p> The <code>POSITION_INDEPENDENT_CODE</code> property determines whether position independent executables or shared libraries will be created. This property is <code>True</code> by default for <code>SHARED</code> and <code>MODULE</code> library targets and <code>False</code> otherwise. This property is initialized by the value of the <code>CMAKE_POSITION_INDEPENDENT_CODE</code> variable if it is set when a target is created.</p>
<h3>Prefix</h3>
<p>What comes before the library name. </p>
<p> A target property that can be set to override the prefix (such as &quot;lib&quot;) on a library name.</p>
<h3>Private_Header</h3>
<p>Specify private header files in a <code>FRAMEWORK</code> shared library target. </p>
<p> Shared library targets marked with the <code>FRAMEWORK</code> property generate frameworks on OS X, iOS and normal shared libraries on other platforms. This property may be set to a list of header files to be placed in the PrivateHeaders directory inside the framework folder. On non-Apple platforms these headers may be installed using the <code>PRIVATE_HEADER</code> option to the <code>install(TARGETS)</code> command.</p>
<h3>Project_Label</h3>
<p>Change the name of a target in an IDE. </p>
<p> Can be used to change the name of the target in an IDE like Visual Studio.</p>
<h3>Public_Header</h3>
<p>Specify public header files in a <code>FRAMEWORK</code> shared library target. </p>
<p> Shared library targets marked with the <code>FRAMEWORK</code> property generate frameworks on OS X, iOS and normal shared libraries on other platforms. This property may be set to a list of header files to be placed in the <code>Headers</code> directory inside the framework folder. On non-Apple platforms these headers may be installed using the <code>PUBLIC_HEADER</code> option to the <code>install(TARGETS)</code> command.</p>
<h3>Resource</h3>
<p>Specify resource files in a <code>FRAMEWORK</code> or <code>BUNDLE</code>. </p>
<p> Target marked with the <code>FRAMEWORK</code> or <code>BUNDLE</code> property generate framework or application bundle (both OS X and iOS is supported) or normal shared libraries on other platforms. This property may be set to a list of files to be placed in the corresponding directory (eg. <code>Resources</code> directory for OS X) inside the bundle. On non-Apple platforms these files may be installed using the <code>RESOURCE</code> option to the <code>install(TARGETS)</code> command. </p>
<p> Following example of Application Bundle: </p>
<pre>add_executable(ExecutableTarget
 addDemo.c
 resourcefile.txt
 appresourcedir/appres.txt
)
target_link_libraries(ExecutableTarget heymath mul)
set(RESOURCE_FILES
 resourcefile.txt
 appresourcedir/appres.txt
)
set_target_properties(ExecutableTarget PROPERTIES
 MACOSX_BUNDLE TRUE
 MACOSX_FRAMEWORK_IDENTIFIER org.cmake.ExecutableTarget
 RESOURCE &quot;${RESOURCE_FILES}&quot;
)</pre>
<p>will produce flat structure for iOS systems: </p>
<pre>ExecutableTarget.app
 appres.txt
 ExecutableTarget
 Info.plist
 resourcefile.txt</pre>
<p>For OS X systems it will produce following directory structure: </p>
<pre>ExecutableTarget.app/
 Contents
 Info.plist
 MacOS
 ExecutableTarget
 Resources
 appres.txt
 resourcefile.txt</pre>
<p>For Linux, such cmake script produce following files: </p>
<pre>ExecutableTarget
Resources
 appres.txt
 resourcefile.txt</pre>
<h3>Rule_Launch_Compile</h3>
<p>Specify a launcher for compile rules. </p>
<p> See the global property of the same name for details. This overrides the global and directory property for a target.</p>
<h3>Rule_Launch_Custom</h3>
<p>Specify a launcher for custom rules. </p>
<p> See the global property of the same name for details. This overrides the global and directory property for a target.</p>
<h3>Rule_Launch_Link</h3>
<p>Specify a launcher for link rules. </p>
<p> See the global property of the same name for details. This overrides the global and directory property for a target.</p>
<h3>RUNTIME_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</h3>
<p>Per-configuration output directory for <i>RUNTIME</i> target files. </p>
<p> This is a per-configuration version of the <code>RUNTIME_OUTPUT_DIRECTORY</code> target property, but multi-configuration generators (VS, Xcode) do NOT append a per-configuration subdirectory to the specified directory. This property is initialized by the value of the <code>CMAKE_RUNTIME_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> variable if it is set when a target is created. </p>
<p> Contents of <code>RUNTIME_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> may use <code>generator expressions</code>.</p>
<h3>Runtime_Output_Directory</h3>
<p>Output directory in which to build <i>RUNTIME</i> target files. </p>
<p> This property specifies the directory into which runtime target files should be built. The property value may use <code>generator expressions</code>. Multi-configuration generators (VS, Xcode) append a per-configuration subdirectory to the specified directory unless a generator expression is used. </p>
<p> This property is initialized by the value of the variable CMAKE_RUNTIME_OUTPUT_DIRECTORY if it is set when a target is created. </p>
<p> See also the <code>RUNTIME_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> target property.</p>
<h3>RUNTIME_OUTPUT_NAME_&lt;CONFIG&gt;</h3>
<p>Per-configuration output name for <i>RUNTIME</i> target files. </p>
<p> This is the configuration-specific version of the <code>RUNTIME_OUTPUT_NAME</code> target property.</p>
<h3>Runtime_Output_Name</h3>
<p>Output name for <i>RUNTIME</i> target files. </p>
<p> This property specifies the base name for runtime target files. It overrides <code>OUTPUT_NAME</code> and <code>OUTPUT_NAME_&lt;CONFIG&gt;</code> properties. </p>
<p> See also the <code>RUNTIME_OUTPUT_NAME_&lt;CONFIG&gt;</code> target property.</p>
<h3>Skip_Build_Rpath</h3>
<p>Should rpaths be used for the build tree. </p>
<p> SKIP_BUILD_RPATH is a boolean specifying whether to skip automatic generation of an rpath allowing the target to run from the build tree. This property is initialized by the value of the variable CMAKE_SKIP_BUILD_RPATH if it is set when a target is created.</p>
<h3>Source_Dir</h3>
<p>This read-only property reports the value of the <code>CMAKE_CURRENT_SOURCE_DIR</code> variable in the directory in which the target was defined.</p>
<h3>Sources</h3>
<p>Source names specified for a target. </p>
<p> List of sources specified for a target.</p>
<h3>Soversion</h3>
<p>What version number is this target. </p>
<p> For shared libraries <code>VERSION</code> and <code>SOVERSION</code> can be used to specify the build version and API version respectively. When building or installing appropriate symlinks are created if the platform supports symlinks and the linker supports so-names. If only one of both is specified the missing is assumed to have the same version number. <code>SOVERSION</code> is ignored if <code>NO_SONAME</code> property is set.</p>
<h3>Windows Versions</h3>
<p>For shared libraries and executables on Windows the <code>VERSION</code> attribute is parsed to extract a <code>&lt;major&gt;.&lt;minor&gt;</code> version number. These numbers are used as the image version of the binary.</p>
<h3>Mach-O Versions</h3>
<p>For shared libraries and executables on Mach-O systems (e.g. OS X, iOS), the <code>SOVERSION</code> property corresponds to <i>compatibility version</i> and <code>VERSION</code> to <i>current version</i>. See the <code>FRAMEWORK</code> target property for an example. Versions of Mach-O binaries may be checked with the <code>otool -L &lt;binary&gt;</code> command.</p>
<h3>STATIC_LIBRARY_FLAGS_&lt;CONFIG&gt;</h3>
<p>Per-configuration flags for creating a static library. </p>
<p> This is the configuration-specific version of STATIC_LIBRARY_FLAGS.</p>
<h3>Static_Library_Flags</h3>
<p>Extra flags to use when linking static libraries. </p>
<p> Extra flags to use when linking a static library.</p>
<h3>Suffix</h3>
<p>What comes after the target name. </p>
<p> A target property that can be set to override the suffix (such as &quot;.so&quot; or &quot;.exe&quot;) on the name of a library, module or executable.</p>
<h3>Type</h3>
<p>The type of the target. </p>
<p> This read-only property can be used to test the type of the given target. It will be one of STATIC_LIBRARY, MODULE_LIBRARY, SHARED_LIBRARY, INTERFACE_LIBRARY, EXECUTABLE or one of the internal target types.</p>
<h3>Version</h3>
<p>What version number is this target. </p>
<p> For shared libraries <code>VERSION</code> and <code>SOVERSION</code> can be used to specify the build version and API version respectively. When building or installing appropriate symlinks are created if the platform supports symlinks and the linker supports so-names. If only one of both is specified the missing is assumed to have the same version number. For executables <code>VERSION</code> can be used to specify the build version. When building or installing appropriate symlinks are created if the platform supports symlinks.</p>
<h3>Windows Versions</h3>
<p>For shared libraries and executables on Windows the <code>VERSION</code> attribute is parsed to extract a <code>&lt;major&gt;.&lt;minor&gt;</code> version number. These numbers are used as the image version of the binary.</p>
<h3>Mach-O Versions</h3>
<p>For shared libraries and executables on Mach-O systems (e.g. OS X, iOS), the <code>SOVERSION</code> property correspond to <i>compatibility version</i> and <code>VERSION</code> to <i>current version</i>. See the <code>FRAMEWORK</code> target property for an example. Versions of Mach-O binaries may be checked with the <code>otool -L &lt;binary&gt;</code> command.</p>
<h3>Visibility_Inlines_Hidden</h3>
<p>Whether to add a compile flag to hide symbols of inline functions </p>
<p> The <code>VISIBILITY_INLINES_HIDDEN</code> property determines whether a flag for hiding symbols for inline functions, such as <code>-fvisibility-inlines-hidden</code>, should be used when invoking the compiler. This property affects compilation in sources of all types of targets (subject to policy <code>CMP0063</code>). </p>
<p> This property is initialized by the value of the <code>CMAKE_VISIBILITY_INLINES_HIDDEN</code> variable if it is set when a target is created.</p>
<h3>Vs_Configuration_Type</h3>
<p>Visual Studio project configuration type. </p>
<p> Sets the <code>ConfigurationType</code> attribute for a generated Visual Studio project. If this property is set, it overrides the default setting that is based on the target type (e.g. <code>StaticLibrary</code>, <code>Application</code>, &#8230;). </p>
<p> Supported on <i>Visual Studio Generators</i> for VS 2010 and higher.</p>
<h3>Vs_Desktop_Extensions_Version</h3>
<p>Visual Studio Windows 10 Desktop Extensions Version </p>
<p> Specifies the version of the Desktop Extensions that should be included in the target. For example <code>10.0.10240.0</code>. If the value is not specified, the Desktop Extensions will not be included. To use the same version of the extensions as the Windows 10 SDK that is being used, you can use the <code>CMAKE_VS_WINDOWS_TARGET_PLATFORM_VERSION</code> variable.</p>
<h3>Vs_Dotnet_References</h3>
<p>Visual Studio managed project .NET references </p>
<p> Adds one or more semicolon-delimited .NET references to a generated Visual Studio project. For example, &quot;System;System.Windows.Forms&quot;.</p>
<h3>Vs_Dotnet_Target_Framework_Version</h3>
<p>Specify the .NET target framework version. </p>
<p> Used to specify the .NET target framework version for C++/CLI. For example, &quot;v4.5&quot;.</p>
<h3>Vs_Global_Keyword</h3>
<p>Visual Studio project keyword for VS 10 (2010) and newer. </p>
<p> Sets the &quot;keyword&quot; attribute for a generated Visual Studio project. Defaults to &quot;Win32Proj&quot;. You may wish to override this value with &quot;ManagedCProj&quot;, for example, in a Visual Studio managed C++ unit test project. </p>
<p> Use the <code>VS_KEYWORD</code> target property to set the keyword for Visual Studio 9 (2008) and older.</p>
<h3>Vs_Global_Project_Types</h3>
<p>Visual Studio project type(s). </p>
<p> Can be set to one or more UUIDs recognized by Visual Studio to indicate the type of project. This value is copied verbatim into the generated project file. Example for a managed C++ unit testing project: </p>
<pre>{3AC096D0-A1C2-E12C-1390-A8335801FDAB};{8BC9CEB8-8B4A-11D0-8D11-00A0C91BC942}</pre>
<p>UUIDs are semicolon-delimited.</p>
<h3>Vs_Global_Rootnamespace</h3>
<p>Visual Studio project root namespace. </p>
<p> Sets the &quot;RootNamespace&quot; attribute for a generated Visual Studio project. The attribute will be generated only if this is set.</p>
<h3>VS_GLOBAL_&lt;variable&gt;</h3>
<p>Visual Studio project-specific global variable. </p>
<p> Tell the Visual Studio generator to set the global variable &#8216;&lt;variable&gt;&#8217; to a given value in the generated Visual Studio project. Ignored on other generators. Qt integration works better if VS_GLOBAL_QtVersion is set to the version FindQt4.cmake found. For example, &quot;4.7.3&quot;</p>
<h3>Vs_Iot_Extensions_Version</h3>
<p>Visual Studio Windows 10 IoT Extensions Version </p>
<p> Specifies the version of the IoT Extensions that should be included in the target. For example <code>10.0.10240.0</code>. If the value is not specified, the IoT Extensions will not be included. To use the same version of the extensions as the Windows 10 SDK that is being used, you can use the <code>CMAKE_VS_WINDOWS_TARGET_PLATFORM_VERSION</code> variable.</p>
<h3>Vs_Iot_Startup_Task</h3>
<p>Visual Studio Windows 10 IoT Continuous Background Task </p>
<p> Specifies that the target should be compiled as a Continuous Background Task library.</p>
<h3>Vs_Keyword</h3>
<p>Visual Studio project keyword for VS 9 (2008) and older. </p>
<p> Can be set to change the visual studio keyword, for example Qt integration works better if this is set to Qt4VSv1.0. </p>
<p> Use the <code>VS_GLOBAL_KEYWORD</code> target property to set the keyword for Visual Studio 10 (2010) and newer.</p>
<h3>Vs_Mobile_Extensions_Version</h3>
<p>Visual Studio Windows 10 Mobile Extensions Version </p>
<p> Specifies the version of the Mobile Extensions that should be included in the target. For example <code>10.0.10240.0</code>. If the value is not specified, the Mobile Extensions will not be included. To use the same version of the extensions as the Windows 10 SDK that is being used, you can use the <code>CMAKE_VS_WINDOWS_TARGET_PLATFORM_VERSION</code> variable.</p>
<h3>Vs_Scc_Auxpath</h3>
<p>Visual Studio Source Code Control Aux Path. </p>
<p> Can be set to change the visual studio source code control auxpath property.</p>
<h3>Vs_Scc_Localpath</h3>
<p>Visual Studio Source Code Control Local Path. </p>
<p> Can be set to change the visual studio source code control local path property.</p>
<h3>Vs_Scc_Projectname</h3>
<p>Visual Studio Source Code Control Project. </p>
<p> Can be set to change the visual studio source code control project name property.</p>
<h3>Vs_Scc_Provider</h3>
<p>Visual Studio Source Code Control Provider. </p>
<p> Can be set to change the visual studio source code control provider property.</p>
<h3>Vs_Windows_Target_Platform_Min_Version</h3>
<p>Visual Studio Windows Target Platform Minimum Version </p>
<p> For Windows 10. Specifies the minimum version of the OS that is being targeted. For example <code>10.0.10240.0</code>. If the value is not specified, the value of <code>CMAKE_VS_WINDOWS_TARGET_PLATFORM_VERSION</code> will be used on WindowsStore projects otherwise the target platform minimum version will not be specified for the project.</p>
<h3>Vs_Winrt_Component</h3>
<p>Mark a target as a Windows Runtime component for the Visual Studio generator. Compile the target with <code>C++/CX</code> language extensions for Windows Runtime. For <code>SHARED</code> and <code>MODULE</code> libraries, this also defines the <code>_WINRT_DLL</code> preprocessor macro. </p>
<p> <code>NOTE:</code> Currently this is implemented only by Visual Studio generators. Support may be added to other generators in the future.</p>
<h3>Vs_Winrt_Extensions</h3>
<p>Deprecated. Use <code>VS_WINRT_COMPONENT</code> instead. This property was an experimental partial implementation of that one.</p>
<h3>Vs_Winrt_References</h3>
<p>Visual Studio project Windows Runtime Metadata references </p>
<p> Adds one or more semicolon-delimited WinRT references to a generated Visual Studio project. For example, &quot;Windows;Windows.UI.Core&quot;.</p>
<h3>Win32_Executable</h3>
<p>Build an executable with a WinMain entry point on windows. </p>
<p> When this property is set to true the executable when linked on Windows will be created with a WinMain() entry point instead of just main(). This makes it a GUI executable instead of a console application. See the CMAKE_MFC_FLAG variable documentation to configure use of MFC for WinMain executables. This property is initialized by the value of the variable CMAKE_WIN32_EXECUTABLE if it is set when a target is created.</p>
<h3>Windows_Export_All_Symbols</h3>
<p>This property is implemented only for MS-compatible tools on Windows. </p>
<p> Enable this boolean property to automatically create a module definition (<code>.def</code>) file with all global symbols found in the input <code>.obj</code> files for a <code>SHARED</code> library on Windows. The module definition file will be passed to the linker causing all symbols to be exported from the <code>.dll</code>. For global <i>data</i> symbols, <code>__declspec(dllimport)</code> must still be used when compiling against the code in the <code>.dll</code>. All other function symbols will be automatically exported and imported by callers. This simplifies porting projects to Windows by reducing the need for explicit <code>dllexport</code> markup, even in <code>C++</code> classes. </p>
<p> This property is initialized by the value of the <code>CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS</code> variable if it is set when a target is created.</p>
<h3>XCODE_ATTRIBUTE_&lt;an-attribute&gt;</h3>
<p>Set Xcode target attributes directly. </p>
<p> Tell the Xcode generator to set &#8216;&lt;an-attribute&gt;&#8217; to a given value in the generated Xcode project. Ignored on other generators. </p>
<p> See the <code>CMAKE_XCODE_ATTRIBUTE_&lt;an-attribute&gt;</code> variable to set attributes on all targets in a directory tree. </p>
<p> Contents of <code>XCODE_ATTRIBUTE_&lt;an-attribute&gt;</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.</p>
<h3>Xctest</h3>
<p>This target is a XCTest CFBundle on the Mac. </p>
<p> This property will usually get set via the <code>xctest_add_bundle()</code> macro in <code>FindXCTest</code> module. </p>
<p> If a module library target has this property set to true it will be built as a CFBundle when built on the Mac. It will have the directory structure required for a CFBundle. </p>
<p> This property depends on <code>BUNDLE</code> to be effective.</p>
<h2>Properties On Tests</h2>
<h3>Attached_Files_On_Fail</h3>
<p>Attach a list of files to a dashboard submission if the test fails. </p>
<p> Same as <code>ATTACHED_FILES</code>, but these files will only be included if the test does not pass.</p>
<h3>Attached_Files</h3>
<p>Attach a list of files to a dashboard submission. </p>
<p> Set this property to a list of files that will be encoded and submitted to the dashboard as an addition to the test result.</p>
<h3>Cost</h3>
<p>Set this to a floating point value. Tests in a test set will be run in descending order of cost. </p>
<p> This property describes the cost of a test. You can explicitly set this value; tests with higher COST values will run first.</p>
<h3>Depends</h3>
<p>Specifies that this test should only be run after the specified list of tests. </p>
<p> Set this to a list of tests that must finish before this test is run.</p>
<h3>Environment</h3>
<p>Specify environment variables that should be defined for running a test. </p>
<p> If set to a list of environment variables and values of the form MYVAR=value those environment variables will be defined while running the test. The environment is restored to its previous state after the test is done.</p>
<h3>Fail_Regular_Expression</h3>
<p>If the output matches this regular expression the test will fail. </p>
<p> If set, if the output matches one of specified regular expressions, the test will fail. Example: </p>
<pre>set_tests_properties(mytest PROPERTIES
 FAIL_REGULAR_EXPRESSION &quot;[^a-z]Error;ERROR;Failed&quot;
)</pre>
<p><code>FAIL_REGULAR_EXPRESSION</code> expects a list of regular expressions.</p>
<h3>Labels</h3>
<p>Specify a list of text labels associated with a test. </p>
<p> The list is reported in dashboard submissions.</p>
<h3>Measurement</h3>
<p>Specify a CDASH measurement and value to be reported for a test. </p>
<p> If set to a name then that name will be reported to CDASH as a named measurement with a value of 1. You may also specify a value by setting MEASUREMENT to &quot;measurement=value&quot;.</p>
<h3>Pass_Regular_Expression</h3>
<p>The output must match this regular expression for the test to pass. </p>
<p> If set, the test output will be checked against the specified regular expressions and at least one of the regular expressions has to match, otherwise the test will fail. Example: </p>
<pre>set_tests_properties(mytest PROPERTIES
 PASS_REGULAR_EXPRESSION &quot;TestPassed;All ok&quot;
)</pre>
<p><code>PASS_REGULAR_EXPRESSION</code> expects a list of regular expressions.</p>
<h3>Processors</h3>
<p>How many process slots this test requires </p>
<p> Denotes the number of processors that this test will require. This is typically used for MPI tests, and should be used in conjunction with the ctest_test PARALLEL_LEVEL option.</p>
<h3>Required_Files</h3>
<p>List of files required to run the test. </p>
<p> If set to a list of files, the test will not be run unless all of the files exist.</p>
<h3>Resource_Lock</h3>
<p>Specify a list of resources that are locked by this test. </p>
<p> If multiple tests specify the same resource lock, they are guaranteed not to run concurrently.</p>
<h3>Run_Serial</h3>
<p>Do not run this test in parallel with any other test. </p>
<p> Use this option in conjunction with the ctest_test PARALLEL_LEVEL option to specify that this test should not be run in parallel with any other tests.</p>
<h3>Skip_Return_Code</h3>
<p>Return code to mark a test as skipped. </p>
<p> Sometimes only a test itself can determine if all requirements for the test are met. If such a situation should not be considered a hard failure a return code of the process can be specified that will mark the test as &quot;Not Run&quot; if it is encountered.</p>
<h3>Timeout</h3>
<p>How many seconds to allow for this test. </p>
<p> This property if set will limit a test to not take more than the specified number of seconds to run. If it exceeds that the test process will be killed and ctest will move to the next test. This setting takes precedence over <code>CTEST_TEST_TIMEOUT</code>.</p>
<h3>Timeout_After_Match</h3>
<p>Change a test&#8217;s timeout duration after a matching line is encountered in its output.</p>
<h3>Usage</h3>
<pre>add_test(mytest ...)
set_property(TEST mytest PROPERTY TIMEOUT_AFTER_MATCH &quot;${seconds}&quot; &quot;${regex}&quot;)</pre>
<h3>Description</h3>
<p>Allow a test <code>seconds</code> to complete after <code>regex</code> is encountered in its output. </p>
<p> When the test outputs a line that matches <code>regex</code> its start time is reset to the current time and its timeout duration is changed to <code>seconds</code>. Prior to this, the timeout duration is determined by the <code>TIMEOUT</code> property or the <code>CTEST_TEST_TIMEOUT</code> variable if either of these are set. </p>
<p> <code>TIMEOUT_AFTER_MATCH</code> is useful for avoiding spurious timeouts when your test must wait for some system resource to become available before it can execute. Set <code>TIMEOUT</code> to a longer duration that accounts for resource acquisition and use <code>TIMEOUT_AFTER_MATCH</code> to control how long the actual test is allowed to run. </p>
<p> If the required resource can be controlled by CTest you should use <code>RESOURCE_LOCK</code> instead of <code>TIMEOUT_AFTER_MATCH</code>. This property should be used when only the test itself can determine when its required resources are available.</p>
<h3>Will_Fail</h3>
<p>If set to true, this will invert the pass/fail flag of the test. </p>
<p> This property can be used for tests that are expected to fail and return a non zero return code.</p>
<h3>Working_Directory</h3>
<p>The directory from which the test executable will be called. </p>
<p> If this is not set it is called from the directory the test executable is located in.</p>
<h2>Properties On Source Files</h2>
<h3>Abstract</h3>
<p>Is this source file an abstract class. </p>
<p> A property on a source file that indicates if the source file represents a class that is abstract. This only makes sense for languages that have a notion of an abstract class and it is only used by some tools that wrap classes into other languages.</p>
<h3>Autouic_Options</h3>
<p>Additional options for <code>uic</code> when using <code>AUTOUIC</code> </p>
<p> This property holds additional command line options which will be used when <code>uic</code> is executed during the build via <code>AUTOUIC</code>, i.e. it is equivalent to the optional <code>OPTIONS</code> argument of the <code>qt4_wrap_ui()</code> macro. </p>
<p> By default it is empty. </p>
<p> The options set on the <code>.ui</code> source file may override <code>AUTOUIC_OPTIONS</code> set on the target.</p>
<h3>Autorcc_Options</h3>
<p>Additional options for <code>rcc</code> when using <code>AUTORCC</code> </p>
<p> This property holds additional command line options which will be used when <code>rcc</code> is executed during the build via <code>AUTORCC</code>, i.e. it is equivalent to the optional <code>OPTIONS</code> argument of the <code>qt4_add_resources()</code> macro. </p>
<p> By default it is empty. </p>
<p> The options set on the <code>.qrc</code> source file may override <code>AUTORCC_OPTIONS</code> set on the target.</p>
<h3>Compile_Definitions</h3>
<p>Preprocessor definitions for compiling a source file. </p>
<p> The COMPILE_DEFINITIONS property may be set to a semicolon-separated list of preprocessor definitions using the syntax VAR or VAR=value. Function-style definitions are not supported. CMake will automatically escape the value correctly for the native build system (note that CMake language syntax may require escapes to specify some values). This property may be set on a per-configuration basis using the name COMPILE_DEFINITIONS_&lt;CONFIG&gt; where &lt;CONFIG&gt; is an upper-case name (ex. &quot;COMPILE_DEFINITIONS_DEBUG&quot;). </p>
<p> CMake will automatically drop some definitions that are not supported by the native build tool. Xcode does not support per-configuration definitions on source files. </p>
<p> Disclaimer: Most native build tools have poor support for escaping certain values. CMake has work-arounds for many cases but some values may just not be possible to pass correctly. If a value does not seem to be escaped correctly, do not attempt to work-around the problem by adding escape sequences to the value. Your work-around may break in a future version of CMake that has improved escape support. Instead consider defining the macro in a (configured) header file. Then report the limitation. Known limitations include: </p>
<pre># - broken almost everywhere
; - broken in VS IDE 7.0 and Borland Makefiles
, - broken in VS IDE
% - broken in some cases in NMake
&amp; | - broken in some cases on MinGW
^ &lt; &gt; \&quot; - broken in most Make tools on Windows</pre>
<p>CMake does not reject these values outright because they do work in some cases. Use with caution.</p>
<h3>Compile_Flags</h3>
<p>Additional flags to be added when compiling this source file. </p>
<p> These flags will be added to the list of compile flags when this source file builds. Use <code>COMPILE_DEFINITIONS</code> to pass additional preprocessor definitions.</p>
<h3>External_Object</h3>
<p>If set to true then this is an object file. </p>
<p> If this property is set to true then the source file is really an object file and should not be compiled. It will still be linked into the target though.</p>
<h3>Fortran_FORMAT</h3>
<p>Set to FIXED or FREE to indicate the Fortran source layout. </p>
<p> This property tells CMake whether a given Fortran source file uses fixed-format or free-format. CMake will pass the corresponding format flag to the compiler. Consider using the target-wide Fortran_FORMAT property if all source files in a target share the same format.</p>
<h3>Generated</h3>
<p>Is this source file generated as part of the build process. </p>
<p> If a source file is generated by the build process CMake will handle it differently in terms of dependency checking etc. Otherwise having a non-existent source file could create problems.</p>
<h3>Header_File_Only</h3>
<p>Is this source file only a header file. </p>
<p> A property on a source file that indicates if the source file is a header file with no associated implementation. This is set automatically based on the file extension and is used by CMake to determine if certain dependency information should be computed.</p>
<h3>Keep_Extension</h3>
<p>Make the output file have the same extension as the source file. </p>
<p> If this property is set then the file extension of the output file will be the same as that of the source file. Normally the output file extension is computed based on the language of the source file, for example .cxx will go to a .o extension.</p>
<h3>Labels</h3>
<p>Specify a list of text labels associated with a source file. </p>
<p> This property has meaning only when the source file is listed in a target whose LABELS property is also set. No other semantics are currently specified.</p>
<h3>Language</h3>
<p>What programming language is the file. </p>
<p> A property that can be set to indicate what programming language the source file is. If it is not set the language is determined based on the file extension. Typical values are CXX C etc. Setting this property for a file means this file will be compiled. Do not set this for headers or files that should not be compiled.</p>
<h3>Location</h3>
<p>The full path to a source file. </p>
<p> A read only property on a SOURCE FILE that contains the full path to the source file.</p>
<h3>Macosx_Package_Location</h3>
<p>Place a source file inside a Application Bundle (<code>MACOSX_BUNDLE</code>), Core Foundation Bundle (<code>BUNDLE</code>), or Framework Bundle (<code>FRAMEWORK</code>). It is applicable for OS X and iOS. </p>
<p> Executable targets with the <code>MACOSX_BUNDLE</code> property set are built as OS X or iOS application bundles on Apple platforms. Shared library targets with the <code>FRAMEWORK</code> property set are built as OS X or iOS frameworks on Apple platforms. Module library targets with the <code>BUNDLE</code> property set are built as OS X <code>CFBundle</code> bundles on Apple platforms. Source files listed in the target with this property set will be copied to a directory inside the bundle or framework content folder specified by the property value. For OS X Application Bundles the content folder is <code>&lt;name&gt;.app/Contents</code>. For OS X Frameworks the content folder is <code>&lt;name&gt;.framework/Versions/&lt;version&gt;</code>. For OS X CFBundles the content folder is <code>&lt;name&gt;.bundle/Contents</code> (unless the extension is changed). See the <code>PUBLIC_HEADER</code>, <code>PRIVATE_HEADER</code>, and <code>RESOURCE</code> target properties for specifying files meant for <code>Headers</code>, <code>PrivateHeaders</code>, or <code>Resources</code> directories.</p>
<h3>Object_Depends</h3>
<p>Additional files on which a compiled object file depends. </p>
<p> Specifies a <i>;-list</i> of full-paths to files on which any object files compiled from this source file depend. On <i>Makefile Generators</i> and the <code>Ninja</code> generator an object file will be recompiled if any of the named files is newer than it. <i>Visual Studio Generators</i> and the <code>Xcode</code> generator cannot implement such compilation dependencies. </p>
<p> This property need not be used to specify the dependency of a source file on a generated header file that it includes. Although the property was originally introduced for this purpose, it is no longer necessary. If the generated header file is created by a custom command in the same target as the source file, the automatic dependency scanning process will recognize the dependency. If the generated header file is created by another target, an inter-target dependency should be created with the <code>add_dependencies()</code> command (if one does not already exist due to linking relationships).</p>
<h3>Object_Outputs</h3>
<p>Additional outputs for a Makefile rule. </p>
<p> Additional outputs created by compilation of this source file. If any of these outputs is missing the object will be recompiled. This is supported only on Makefile generators and will be ignored on other generators.</p>
<h3>Symbolic</h3>
<p>Is this just a name for a rule. </p>
<p> If SYMBOLIC (boolean) is set to true the build system will be informed that the source file is not actually created on disk but instead used as a symbolic name for a build rule.</p>
<h3>Vs_Deployment_Content</h3>
<p>Mark a source file as content for deployment with a Windows Phone or Windows Store application when built with a Visual Studio generator. The value must evaluate to either <code>1</code> or <code>0</code> and may use <code>generator expressions</code> to make the choice based on the build configuration. The <code>.vcxproj</code> file entry for the source file will be marked either <code>DeploymentContent</code> or <code>ExcludedFromBuild</code> for values <code>1</code> and <code>0</code>, respectively.</p>
<h3>Vs_Deployment_Location</h3>
<p>Specifies the deployment location for a content source file with a Windows Phone or Windows Store application when built with a Visual Studio generator. This property is only applicable when using <code>VS_DEPLOYMENT_CONTENT</code>. The value represent the path relative to the app package and applies to all configurations.</p>
<h3>Vs_Shader_Entrypoint</h3>
<p>Specifies the name of the entry point for the shader of a <code>.hlsl</code> source file.</p>
<h3>Vs_Shader_Flags</h3>
<p>Set additional VS shader flags of a <code>.hlsl</code> source file.</p>
<h3>Vs_Shader_Model</h3>
<p>Specifies the shader model of a <code>.hlsl</code> source file. Some shader types can only be used with recent shader models</p>
<h3>Vs_Shader_Type</h3>
<p>Set the VS shader type of a <code>.hlsl</code> source file.</p>
<h3>Vs_Xaml_Type</h3>
<p>Mark a XAML source file as a different type than the default <code>Page</code>. The most common usage would be to set the default App.xaml file as ApplicationDefinition.</p>
<h3>Wrap_Exclude</h3>
<p>Exclude this source file from any code wrapping techniques. </p>
<p> Some packages can wrap source files into alternate languages to provide additional functionality. For example, C++ code can be wrapped into Java or Python etc using SWIG etc. If WRAP_EXCLUDE is set to true (1 etc) that indicates that this source file should not be wrapped.</p>
<h3>Xcode_Explicit_File_Type</h3>
<p>Set the Xcode <code>explicitFileType</code> attribute on its reference to a source file. CMake computes a default based on file extension but can be told explicitly with this property. </p>
<p> See also <code>XCODE_LAST_KNOWN_FILE_TYPE</code>.</p>
<h3>Xcode_Last_Known_File_Type</h3>
<p>Set the Xcode <code>lastKnownFileType</code> attribute on its reference to a source file. CMake computes a default based on file extension but can be told explicitly with this property. </p>
<p> See also <code>XCODE_EXPLICIT_FILE_TYPE</code>, which is preferred over this property if set.</p>
<h2>Properties On Cache Entries</h2>
<h3>Advanced</h3>
<p>True if entry should be hidden by default in GUIs. </p>
<p> This is a boolean value indicating whether the entry is considered interesting only for advanced configuration. The mark_as_advanced() command modifies this property.</p>
<h3>Helpstring</h3>
<p>Help associated with entry in GUIs. </p>
<p> This string summarizes the purpose of an entry to help users set it through a CMake GUI.</p>
<h3>Modified</h3>
<p>Internal management property. Do not set or get. </p>
<p> This is an internal cache entry property managed by CMake to track interactive user modification of entries. Ignore it.</p>
<h3>Strings</h3>
<p>Enumerate possible STRING entry values for GUI selection. </p>
<p> For cache entries with type STRING, this enumerates a set of values. CMake GUIs may use this to provide a selection widget instead of a generic string entry field. This is for convenience only. CMake does not enforce that the value matches one of those listed.</p>
<h3>Type</h3>
<p>Widget type for entry in GUIs. </p>
<p> Cache entry values are always strings, but CMake GUIs present widgets to help users set values. The GUIs use this property as a hint to determine the widget type. Valid TYPE values are: </p>
<pre>BOOL = Boolean ON/OFF value.
PATH = Path to a directory.
FILEPATH = Path to a file.
STRING = Generic string value.
INTERNAL = Do not present in GUI at all.
STATIC = Value managed by CMake, do not change.
UNINITIALIZED = Type not yet specified.</pre>
<p>Generally the TYPE of a cache entry should be set by the command which creates it (set, option, find_library, etc.).</p>
<h3>Value</h3>
<p>Value of a cache entry. </p>
<p> This property maps to the actual value of a cache entry. Setting this property always sets the value without checking, so use with care.</p>
<h2>Properties On Installed Files</h2>
<h3>Cpack_Desktop_Shortcuts</h3>
<p>Species a list of shortcut names that should be created on the Desktop for this file. </p>
<p> The property is currently only supported by the WIX generator.</p>
<h3>Cpack_Never_Overwrite</h3>
<p>Request that this file not be overwritten on install or reinstall. </p>
<p> The property is currently only supported by the WIX generator.</p>
<h3>Cpack_Permanent</h3>
<p>Request that this file not be removed on uninstall. </p>
<p> The property is currently only supported by the WIX generator.</p>
<h3>Cpack_Start_Menu_Shortcuts</h3>
<p>Species a list of shortcut names that should be created in the Start Menu for this file. </p>
<p> The property is currently only supported by the WIX generator.</p>
<h3>Cpack_Startup_Shortcuts</h3>
<p>Species a list of shortcut names that should be created in the Startup folder for this file. </p>
<p> The property is currently only supported by the WIX generator.</p>
<h3>Cpack_Wix_Acl</h3>
<p>Specifies access permissions for files or directories installed by a WiX installer. </p>
<p> The property can contain multiple list entries, each of which has to match the following format. </p>
<pre>&lt;user&gt;[@&lt;domain&gt;]=&lt;permission&gt;[,&lt;permission&gt;]</pre>
<p><code>&lt;user&gt;</code> and <code>&lt;domain&gt;</code> specify the windows user and domain for which the <code>&lt;Permission&gt;</code> element should be generated. </p>
<p> <code>&lt;permission&gt;</code> is any of the YesNoType attributes listed here: </p>
<pre><a rel="nofollow" href="http://wixtoolset.org/documentation/manual/v3/xsd/wix/permission.html">http://wixtoolset.org/documentation/manual/v3/xsd/wix/permission.html</a></pre>
<h2>Deprecated Properties On Directories</h2>
<h3>COMPILE_DEFINITIONS_&lt;CONFIG&gt;</h3>
<p>Ignored. See CMake Policy <code>CMP0043</code>. </p>
<p> Per-configuration preprocessor definitions in a directory. </p>
<p> This is the configuration-specific version of <code>COMPILE_DEFINITIONS</code> where <code>&lt;CONFIG&gt;</code> is an upper-case name (ex. <code>COMPILE_DEFINITIONS_DEBUG</code>). </p>
<p> This property will be initialized in each directory by its value in the directory&#8217;s parent. </p>
<p> Contents of <code>COMPILE_DEFINITIONS_&lt;CONFIG&gt;</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties. </p>
<p> Generator expressions should be preferred instead of setting this property.</p>
<h2>Deprecated Properties On Targets</h2>
<h3>COMPILE_DEFINITIONS_&lt;CONFIG&gt;</h3>
<p>Ignored. See CMake Policy <code>CMP0043</code>. </p>
<p> Per-configuration preprocessor definitions on a target. </p>
<p> This is the configuration-specific version of <code>COMPILE_DEFINITIONS</code> where <code>&lt;CONFIG&gt;</code> is an upper-case name (ex. <code>COMPILE_DEFINITIONS_DEBUG</code>). </p>
<p> Contents of <code>COMPILE_DEFINITIONS_&lt;CONFIG&gt;</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties. </p>
<p> Generator expressions should be preferred instead of setting this property.</p>
<h3>Post_Install_Script</h3>
<p>Deprecated install support. </p>
<p> The PRE_INSTALL_SCRIPT and POST_INSTALL_SCRIPT properties are the old way to specify CMake scripts to run before and after installing a target. They are used only when the old INSTALL_TARGETS command is used to install the target. Use the INSTALL command instead.</p>
<h3>Pre_Install_Script</h3>
<p>Deprecated install support. </p>
<p> The PRE_INSTALL_SCRIPT and POST_INSTALL_SCRIPT properties are the old way to specify CMake scripts to run before and after installing a target. They are used only when the old INSTALL_TARGETS command is used to install the target. Use the INSTALL command instead.</p>
<h2>Deprecated Properties On Source Files</h2>
<h3>COMPILE_DEFINITIONS_&lt;CONFIG&gt;</h3>
<p>Ignored. See CMake Policy <code>CMP0043</code>. </p>
<p> Per-configuration preprocessor definitions on a source file. </p>
<p> This is the configuration-specific version of COMPILE_DEFINITIONS. Note that Xcode does not support per-configuration source file flags so this property will be ignored by the Xcode generator.</p>
<h2>Copyright</h2>
<p>2000-2016 Kitware, Inc.</p>
