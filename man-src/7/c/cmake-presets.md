---
title: "cmake-presets(7)"
name: "cmake-presets"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake-presets/"
description: "cmake-presets – CMakePresets.json"
---

<p>cmake-presets &#8211; CMakePresets.json</p>
<h2>Introduction</h2>
<p>One problem that CMake users often face is sharing settings with other people for common ways to configure a project. This may be done to support CI builds, or for users who frequently use the same build. CMake supports two files, <code>CMakePresets.json</code> and <code>CMakeUserPresets.json</code>, that allow users to specify common configure options and share them with others. </p>
<p> <code>CMakePresets.json</code> and <code>CMakeUserPresets.json</code> live in the project&#8217;s root directory. They both have exactly the same format, and both are optional (though at least one must be present if <code>&#8211;preset</code> is specified.) <code>CMakePresets.json</code> is meant to save project-wide builds, while <code>CMakeUserPresets.json</code> is meant for developers to save their own local builds. <code>CMakePresets.json</code> may be checked into a version control system, and <code>CMakeUserPresets.json</code> should NOT be checked in. For example, if a project is using Git, <code>CMakePresets.json</code> may be tracked, and <code>CMakeUserPresets.json</code> should be added to the <code>.gitignore</code>.</p>
<h2>Format</h2>
<p>The files are a JSON document with an object as the root: </p>
<pre>{
 &quot;version&quot;: 3,
 &quot;cmakeMinimumRequired&quot;: {
 &quot;major&quot;: 3,
 &quot;minor&quot;: 21,
 &quot;patch&quot;: 0
 },
 &quot;configurePresets&quot;: [
 {
 &quot;name&quot;: &quot;default&quot;,
 &quot;displayName&quot;: &quot;Default Config&quot;,
 &quot;description&quot;: &quot;Default build using Ninja generator&quot;,
 &quot;generator&quot;: &quot;Ninja&quot;,
 &quot;binaryDir&quot;: &quot;${sourceDir}/build/default&quot;,
 &quot;cacheVariables&quot;: {
 &quot;FIRST_CACHE_VARIABLE&quot;: {
 &quot;type&quot;: &quot;BOOL&quot;,
 &quot;value&quot;: &quot;OFF&quot;
 },
 &quot;SECOND_CACHE_VARIABLE&quot;: &quot;ON&quot;
 },
 &quot;environment&quot;: {
 &quot;MY_ENVIRONMENT_VARIABLE&quot;: &quot;Test&quot;,
 &quot;PATH&quot;: &quot;$env{HOME}/ninja/bin:$penv{PATH}&quot;
 },
 &quot;vendor&quot;: {
 &quot;example.com/ExampleIDE/1.0&quot;: {
 &quot;autoFormat&quot;: true
 }
 }
 },
 {
 &quot;name&quot;: &quot;ninja-multi&quot;,
 &quot;inherits&quot;: &quot;default&quot;,
 &quot;displayName&quot;: &quot;Ninja Multi-Config&quot;,
 &quot;description&quot;: &quot;Default build using Ninja Multi-Config generator&quot;,
 &quot;generator&quot;: &quot;Ninja Multi-Config&quot;
 },
 {
 &quot;name&quot;: &quot;windows-only&quot;,
 &quot;inherits&quot;: &quot;default&quot;,
 &quot;displayName&quot;: &quot;Windows-only configuration&quot;,
 &quot;description&quot;: &quot;This build is only available on Windows&quot;,
 &quot;condition&quot;: {
 &quot;type&quot;: &quot;equals&quot;,
 &quot;lhs&quot;: &quot;${hostSystemName}&quot;,
 &quot;rhs&quot;: &quot;Windows&quot;
 }
 }
 ],
 &quot;buildPresets&quot;: [
 {
 &quot;name&quot;: &quot;default&quot;,
 &quot;configurePreset&quot;: &quot;default&quot;
 }
 ],
 &quot;testPresets&quot;: [
 {
 &quot;name&quot;: &quot;default&quot;,
 &quot;configurePreset&quot;: &quot;default&quot;,
 &quot;output&quot;: {&quot;outputOnFailure&quot;: true},
 &quot;execution&quot;: {&quot;noTestsAction&quot;: &quot;error&quot;, &quot;stopOnFailure&quot;: true}
 }
 ],
 &quot;vendor&quot;: {
 &quot;example.com/ExampleIDE/1.0&quot;: {
 &quot;autoFormat&quot;: false
 }
 }
}</pre>
<p>The root object recognizes the following fields: </p>
<p> <code>version</code> A required integer representing the version of the JSON schema. The supported versions are <code>1</code>, <code>2</code>, and <code>3</code>. </p>
<p> <code>cmakeMinimumRequired</code> An optional object representing the minimum version of CMake needed to build this project. This object consists of the following fields: </p>
<p> <code>major</code> An optional integer representing the major version. </p>
<p> <code>minor</code> An optional integer representing the minor version. </p>
<p> <code>patch</code> An optional integer representing the patch version. </p>
<p> <code>vendor</code> An optional map containing vendor-specific information. CMake does not interpret the contents of this field except to verify that it is a map if it does exist. However, the keys should be a vendor-specific domain name followed by a <code>/</code>-separated path. For example, the Example IDE 1.0 could use <code>example.com/ExampleIDE/1.0</code>. The value of each field can be anything desired by the vendor, though will typically be a map. </p>
<p> <code>configurePresets</code> An optional array of <i>Configure Preset</i> objects. This is allowed in preset files specifying version <code>1</code> or above. </p>
<p> <code>buildPresets</code> An optional array of <i>Build Preset</i> objects. This is allowed in preset files specifying version <code>2</code> or above. </p>
<p> <code>testPresets</code> An optional array of <i>Test Preset</i> objects. This is allowed in preset files specifying version <code>2</code> or above.</p>
<h3>Configure Preset</h3>
<p>Each entry of the <code>configurePresets</code> array is a JSON object that may contain the following fields: </p>
<p> <code>name</code> A required string representing the machine-friendly name of the preset. This identifier is used in the cmake &#8211;preset option. There must not be two configure presets in the union of <code>CMakePresets.json</code> and <code>CMakeUserPresets.json</code> in the same directory with the same name. However, a configure preset may have the same name as a build or test preset. </p>
<p> <code>hidden</code> An optional boolean specifying whether or not a preset should be hidden. If a preset is hidden, it cannot be used in the <code>&#8211;preset=</code> argument, will not show up in the <code>CMake GUI</code>, and does not have to have a valid <code>generator</code> or <code>binaryDir</code>, even from inheritance. <code>hidden</code> presets are intended to be used as a base for other presets to inherit via the <code>inherits</code> field. </p>
<p> <code>inherits</code> An optional array of strings representing the names of presets to inherit from. The preset will inherit all of the fields from the <code>inherits</code> presets by default (except <code>name</code>, <code>hidden</code>, <code>inherits</code>, <code>description</code>, and <code>displayName</code>), but can override them as desired. If multiple <code>inherits</code> presets provide conflicting values for the same field, the earlier preset in the <code>inherits</code> list will be preferred. Presets in <code>CMakePresets.json</code> may not inherit from presets in <code>CMakeUserPresets.json</code>. </p>
<p> This field can also be a string, which is equivalent to an array containing one string. </p>
<p> <code>condition</code> An optional <i>Condition</i> object. This is allowed in preset files specifying version <code>3</code> or above. </p>
<p> <code>vendor</code> An optional map containing vendor-specific information. CMake does not interpret the contents of this field except to verify that it is a map if it does exist. However, it should follow the same conventions as the root-level <code>vendor</code> field. If vendors use their own per-preset <code>vendor</code> field, they should implement inheritance in a sensible manner when appropriate. </p>
<p> <code>displayName</code> An optional string with a human-friendly name of the preset. </p>
<p> <code>description</code> An optional string with a human-friendly description of the preset. </p>
<p> <code>generator</code> An optional string representing the generator to use for the preset. If <code>generator</code> is not specified, it must be inherited from the <code>inherits</code> preset (unless this preset is <code>hidden</code>). In version <code>3</code> or above, this field may be omitted to fall back to regular generator discovery procedure. </p>
<p> Note that for Visual Studio generators, unlike in the command line <code>-G</code> argument, you cannot include the platform name in the generator name. Use the <code>architecture</code> field instead. </p>
<p> <code>architecture</code>, <code>toolset</code> Optional fields representing the platform and toolset, respectively, for generators that support them. Each may be either a string or an object with the following fields: </p>
<p> <code>value</code> An optional string representing the value. </p>
<p> <code>strategy</code> An optional string telling CMake how to handle the <code>architecture</code> or <code>toolset</code> field. Valid values are: </p>
<p> <code>&quot;set&quot;</code> Set the respective value. This will result in an error for generators that do not support the respective field. </p>
<p> <code>&quot;external&quot;</code> Do not set the value, even if the generator supports it. This is useful if, for example, a preset uses the Ninja generator, and an IDE knows how to set up the Visual C++ environment from the <code>architecture</code> and <code>toolset</code> fields. In that case, CMake will ignore the field, but the IDE can use them to set up the environment before invoking CMake. </p>
<p> <code>toolchainFile</code> An optional string representing the path to the toolchain file. This field supports <i>macro expansion</i>. If a relative path is specified, it is calculated relative to the build directory, and if not found, relative to the source directory. This field takes precedence over any <code>CMAKE_TOOLCHAIN_FILE</code> value. It is allowed in preset files specifying version <code>3</code> or above. </p>
<p> <code>binaryDir</code> An optional string representing the path to the output binary directory. This field supports <i>macro expansion</i>. If a relative path is specified, it is calculated relative to the source directory. If <code>binaryDir</code> is not specified, it must be inherited from the <code>inherits</code> preset (unless this preset is <code>hidden</code>). In version <code>3</code> or above, this field may be omitted. </p>
<p> <code>installDir</code> An optional string representing the path to the installation directory. This field supports <i>macro expansion</i>. If a relative path is specified, it is calculated relative to the source directory. This is allowed in preset files specifying version <code>3</code> or above. </p>
<p> <code>cmakeExecutable</code> An optional string representing the path to the CMake executable to use for this preset. This is reserved for use by IDEs, and is not used by CMake itself. IDEs that use this field should expand any macros in it. </p>
<p> <code>cacheVariables</code> An optional map of cache variables. The key is the variable name (which may not be an empty string), and the value is either <code>null</code>, a boolean (which is equivalent to a value of <code>&quot;TRUE&quot;</code> or <code>&quot;FALSE&quot;</code> and a type of <code>BOOL</code>), a string representing the value of the variable (which supports <i>macro expansion</i>), or an object with the following fields: </p>
<p> <code>type</code> An optional string representing the type of the variable. </p>
<p> <code>value</code> A required string or boolean representing the value of the variable. A boolean is equivalent to <code>&quot;TRUE&quot;</code> or <code>&quot;FALSE&quot;</code>. This field supports <i>macro expansion</i>. </p>
<p> Cache variables are inherited through the <code>inherits</code> field, and the preset&#8217;s variables will be the union of its own <code>cacheVariables</code> and the <code>cacheVariables</code> from all its parents. If multiple presets in this union define the same variable, the standard rules of <code>inherits</code> are applied. Setting a variable to <code>null</code> causes it to not be set, even if a value was inherited from another preset. </p>
<p> <code>environment</code> An optional map of environment variables. The key is the variable name (which may not be an empty string), and the value is either <code>null</code> or a string representing the value of the variable. Each variable is set regardless of whether or not a value was given to it by the process&#8217;s environment. This field supports <i>macro expansion</i>, and environment variables in this map may reference each other, and may be listed in any order, as long as such references do not cause a cycle (for example, if <code>ENV_1</code> is <code>$env{ENV_2}</code>, <code>ENV_2</code> may not be <code>$env{ENV_1}</code>.) </p>
<p> Environment variables are inherited through the <code>inherits</code> field, and the preset&#8217;s environment will be the union of its own <code>environment</code> and the <code>environment</code> from all its parents. If multiple presets in this union define the same variable, the standard rules of <code>inherits</code> are applied. Setting a variable to <code>null</code> causes it to not be set, even if a value was inherited from another preset. </p>
<p> <code>warnings</code> An optional object specifying the warnings to enable. The object may contain the following fields: </p>
<p> <code>dev</code> An optional boolean. Equivalent to passing <code>-Wdev</code> or <code>-Wno-dev</code> on the command line. This may not be set to <code>false</code> if <code>errors.dev</code> is set to <code>true</code>. </p>
<p> <code>deprecated</code> An optional boolean. Equivalent to passing <code>-Wdeprecated</code> or <code>-Wno-deprecated</code> on the command line. This may not be set to <code>false</code> if <code>errors.deprecated</code> is set to <code>true</code>. </p>
<p> <code>uninitialized</code> An optional boolean. Setting this to <code>true</code> is equivalent to passing <code>&#8211;warn-uninitialized</code> on the command line. </p>
<p> <code>unusedCli</code> An optional boolean. Setting this to <code>false</code> is equivalent to passing <code>&#8211;no-warn-unused-cli</code> on the command line. </p>
<p> <code>systemVars</code> An optional boolean. Setting this to <code>true</code> is equivalent to passing <code>&#8211;check-system-vars</code> on the command line. </p>
<p> <code>errors</code> An optional object specifying the errors to enable. The object may contain the following fields: </p>
<p> <code>dev</code> An optional boolean. Equivalent to passing <code>-Werror=dev</code> or <code>-Wno-error=dev</code> on the command line. This may not be set to <code>true</code> if <code>warnings.dev</code> is set to <code>false</code>. </p>
<p> <code>deprecated</code> An optional boolean. Equivalent to passing <code>-Werror=deprecated</code> or <code>-Wno-error=deprecated</code> on the command line. This may not be set to <code>true</code> if <code>warnings.deprecated</code> is set to <code>false</code>. </p>
<p> <code>debug</code> An optional object specifying debug options. The object may contain the following fields: </p>
<p> <code>output</code> An optional boolean. Setting this to <code>true</code> is equivalent to passing <code>&#8211;debug-output</code> on the command line. </p>
<p> <code>tryCompile</code> An optional boolean. Setting this to <code>true</code> is equivalent to passing <code>&#8211;debug-trycompile</code> on the command line. </p>
<p> <code>find</code> An optional boolean. Setting this to <code>true</code> is equivalent to passing <code>&#8211;debug-find</code> on the command line.</p>
<h3>Build Preset</h3>
<p>Each entry of the <code>buildPresets</code> array is a JSON object that may contain the following fields: </p>
<p> <code>name</code> A required string representing the machine-friendly name of the preset. This identifier is used in the cmake &#8211;build &#8211;preset option. There must not be two build presets in the union of <code>CMakePresets.json</code> and <code>CMakeUserPresets.json</code> in the same directory with the same name. However, a build preset may have the same name as a configure or test preset. </p>
<p> <code>hidden</code> An optional boolean specifying whether or not a preset should be hidden. If a preset is hidden, it cannot be used in the <code>&#8211;preset</code> argument and does not have to have a valid <code>configurePreset</code>, even from inheritance. <code>hidden</code> presets are intended to be used as a base for other presets to inherit via the <code>inherits</code> field. </p>
<p> <code>inherits</code> An optional array of strings representing the names of presets to inherit from. The preset will inherit all of the fields from the <code>inherits</code> presets by default (except <code>name</code>, <code>hidden</code>, <code>inherits</code>, <code>description</code>, and <code>displayName</code>), but can override them as desired. If multiple <code>inherits</code> presets provide conflicting values for the same field, the earlier preset in the <code>inherits</code> list will be preferred. Presets in <code>CMakePresets.json</code> may not inherit from presets in <code>CMakeUserPresets.json</code>. </p>
<p> This field can also be a string, which is equivalent to an array containing one string. </p>
<p> <code>condition</code> An optional <i>Condition</i> object. This is allowed in preset files specifying version <code>3</code> or above. </p>
<p> <code>vendor</code> An optional map containing vendor-specific information. CMake does not interpret the contents of this field except to verify that it is a map if it does exist. However, it should follow the same conventions as the root-level <code>vendor</code> field. If vendors use their own per-preset <code>vendor</code> field, they should implement inheritance in a sensible manner when appropriate. </p>
<p> <code>displayName</code> An optional string with a human-friendly name of the preset. </p>
<p> <code>description</code> An optional string with a human-friendly description of the preset. </p>
<p> <code>environment</code> An optional map of environment variables. The key is the variable name (which may not be an empty string), and the value is either <code>null</code> or a string representing the value of the variable. Each variable is set regardless of whether or not a value was given to it by the process&#8217;s environment. This field supports macro expansion, and environment variables in this map may reference each other, and may be listed in any order, as long as such references do not cause a cycle (for example, if <code>ENV_1</code> is <code>$env{ENV_2}</code>, <code>ENV_2</code> may not be <code>$env{ENV_1}</code>.) </p>
<p> Environment variables are inherited through the <code>inherits</code> field, and the preset&#8217;s environment will be the union of its own <code>environment</code> and the <code>environment</code> from all its parents. If multiple presets in this union define the same variable, the standard rules of <code>inherits</code> are applied. Setting a variable to <code>null</code> causes it to not be set, even if a value was inherited from another preset. </p>
<p> <code>NOTE:</code> For a CMake project using ExternalProject with a configuration preset having environment variables needed in the ExternalProject, use a build preset that inherits that configuration preset or the ExternalProject will not have the environment variables set in the configuration preset. Example: suppose the host defaults to one compiler (say Clang) and the user wishes to use another compiler (say GCC). Set configuration preset environment variables <code>CC</code> and <code>CXX</code> and use a build preset that inherits that configuration preset. Otherwise the ExternalProject may use a different (system default) compiler than the top-level CMake project. </p>
<p> <code>configurePreset</code> An optional string specifying the name of a configure preset to associate with this build preset. If <code>configurePreset</code> is not specified, it must be inherited from the inherits preset (unless this preset is hidden). The build directory is inferred from the configure preset, so the build will take place in the same <code>binaryDir</code> that the configuration did. </p>
<p> <code>inheritConfigureEnvironment</code> An optional boolean that defaults to true. If true, the environment variables from the associated configure preset are inherited after all inherited build preset environments, but before environment variables explicitly specified in this build preset. </p>
<p> <code>jobs</code> An optional integer. Equivalent to passing <code>&#8211;parallel</code> or <code>-j</code> on the command line. </p>
<p> <code>targets</code> An optional string or array of strings. Equivalent to passing <code>&#8211;target</code> or <code>-t</code> on the command line. Vendors may ignore the targets property or hide build presets that explicitly specify targets. This field supports macro expansion. </p>
<p> <code>configuration</code> An optional string. Equivalent to passing <code>&#8211;config</code> on the command line. </p>
<p> <code>cleanFirst</code> An optional bool. If true, equivalent to passing <code>&#8211;clean-first</code> on the command line. </p>
<p> <code>verbose</code> An optional bool. If true, equivalent to passing <code>&#8211;verbose</code> on the command line. </p>
<p> <code>nativeToolOptions</code> An optional array of strings. Equivalent to passing options after <code>&#8212;</code> on the command line. The array values support macro expansion.</p>
<h3>Test Preset</h3>
<p>Each entry of the <code>testPresets</code> array is a JSON object that may contain the following fields: </p>
<p> <code>name</code> A required string representing the machine-friendly name of the preset. This identifier is used in the ctest &#8211;preset option. There must not be two test presets in the union of <code>CMakePresets.json</code> and <code>CMakeUserPresets.json</code> in the same directory with the same name. However, a test preset may have the same name as a configure or build preset. </p>
<p> <code>hidden</code> An optional boolean specifying whether or not a preset should be hidden. If a preset is hidden, it cannot be used in the <code>&#8211;preset</code> argument and does not have to have a valid <code>configurePreset</code>, even from inheritance. <code>hidden</code> presets are intended to be used as a base for other presets to inherit via the <code>inherits</code> field. </p>
<p> <code>inherits</code> An optional array of strings representing the names of presets to inherit from. The preset will inherit all of the fields from the <code>inherits</code> presets by default (except <code>name</code>, <code>hidden</code>, <code>inherits</code>, <code>description</code>, and <code>displayName</code>), but can override them as desired. If multiple <code>inherits</code> presets provide conflicting values for the same field, the earlier preset in the <code>inherits</code> list will be preferred. Presets in <code>CMakePresets.json</code> may not inherit from presets in <code>CMakeUserPresets.json</code>. </p>
<p> This field can also be a string, which is equivalent to an array containing one string. </p>
<p> <code>condition</code> An optional <i>Condition</i> object. This is allowed in preset files specifying version <code>3</code> or above. </p>
<p> <code>vendor</code> An optional map containing vendor-specific information. CMake does not interpret the contents of this field except to verify that it is a map if it does exist. However, it should follow the same conventions as the root-level <code>vendor</code> field. If vendors use their own per-preset <code>vendor</code> field, they should implement inheritance in a sensible manner when appropriate. </p>
<p> <code>displayName</code> An optional string with a human-friendly name of the preset. </p>
<p> <code>description</code> An optional string with a human-friendly description of the preset. </p>
<p> <code>environment</code> An optional map of environment variables. The key is the variable name (which may not be an empty string), and the value is either <code>null</code> or a string representing the value of the variable. Each variable is set regardless of whether or not a value was given to it by the process&#8217;s environment. This field supports macro expansion, and environment variables in this map may reference each other, and may be listed in any order, as long as such references do not cause a cycle (for example, if <code>ENV_1</code> is <code>$env{ENV_2}</code>, <code>ENV_2</code> may not be <code>$env{ENV_1}</code>.) </p>
<p> Environment variables are inherited through the <code>inherits</code> field, and the preset&#8217;s environment will be the union of its own <code>environment</code> and the <code>environment</code> from all its parents. If multiple presets in this union define the same variable, the standard rules of <code>inherits</code> are applied. Setting a variable to <code>null</code> causes it to not be set, even if a value was inherited from another preset. </p>
<p> <code>configurePreset</code> An optional string specifying the name of a configure preset to associate with this test preset. If <code>configurePreset</code> is not specified, it must be inherited from the inherits preset (unless this preset is hidden). The build directory is inferred from the configure preset, so tests will run in the same <code>binaryDir</code> that the configuration did and build did. </p>
<p> <code>inheritConfigureEnvironment</code> An optional boolean that defaults to true. If true, the environment variables from the associated configure preset are inherited after all inherited test preset environments, but before environment variables explicitly specified in this test preset. </p>
<p> <code>configuration</code> An optional string. Equivalent to passing <code>&#8211;build-config</code> on the command line. </p>
<p> <code>overwriteConfigurationFile</code> An optional array of configuration options to overwrite options specified in the CTest configuration file. Equivalent to passing <code>&#8211;overwrite</code> for each value in the array. The array values support macro expansion. </p>
<p> <code>output</code> An optional object specifying output options. The object may contain the following fields. </p>
<p> <code>shortProgress</code> An optional bool. If true, equivalent to passing <code>&#8211;progress</code> on the command line. </p>
<p> <code>verbosity</code> An optional string specifying verbosity level. Must be one of the following: </p>
<p> <code>default</code> Equivalent to passing no verbosity flags on the command line. </p>
<p> <code>verbose</code> Equivalent to passing <code>&#8211;verbose</code> on the command line. </p>
<p> <code>extra</code> Equivalent to passing <code>&#8211;extra-verbose</code> on the command line. </p>
<p> <code>debug</code> An optional bool. If true, equivalent to passing <code>&#8211;debug</code> on the command line. </p>
<p> <code>outputOnFailure</code> An optional bool. If true, equivalent to passing <code>&#8211;output-on-failure</code> on the command line. </p>
<p> <code>quiet</code> An optional bool. If true, equivalent to passing <code>&#8211;quiet</code> on the command line. </p>
<p> <code>outputLogFile</code> An optional string specifying a path to a log file. Equivalent to passing <code>&#8211;output-log</code> on the command line. This field supports macro expansion. </p>
<p> <code>labelSummary</code> An optional bool. If false, equivalent to passing <code>&#8211;no-label-summary</code> on the command line. </p>
<p> <code>subprojectSummary</code> An optional bool. If false, equivalent to passing <code>&#8211;no-subproject-summary</code> on the command line. </p>
<p> <code>maxPassedTestOutputSize</code> An optional integer specifying the maximum output for passed tests in bytes. Equivalent to passing <code>&#8211;test-output-size-passed</code> on the command line. </p>
<p> <code>maxFailedTestOutputSize</code> An optional integer specifying the maximum output for failed tests in bytes. Equivalent to passing <code>&#8211;test-output-size-failed</code> on the command line. </p>
<p> <code>maxTestNameWidth</code> An optional integer specifying the maximum width of a test name to output. Equivalent to passing <code>&#8211;max-width</code> on the command line. </p>
<p> <code>filter</code> An optional object specifying how to filter the tests to run. The object may contain the following fields. </p>
<p> <code>include</code> An optional object specifying which tests to include. The object may contain the following fields. </p>
<p> <code>name</code> An optional string specifying a regex for test names. Equivalent to passing <code>&#8211;tests-regex</code> on the command line. This field supports macro expansion. CMake regex syntax is described under string(REGEX). </p>
<p> <code>label</code> An optional string specifying a regex for test labels. Equivalent to passing <code>&#8211;label-regex</code> on the command line. This field supports macro expansion. </p>
<p> <code>useUnion</code> An optional bool. Equivalent to passing <code>&#8211;union</code> on the command line. </p>
<p> <code>index</code> An optional object specifying tests to include by test index. The object may contain the following fields. Can also be an optional string specifying a file with the command line syntax for <code>&#8211;tests-information</code>. If specified as a string, this field supports macro expansion. </p>
<p> <code>start</code> An optional integer specifying a test index to start testing at. </p>
<p> <code>end</code> An optional integer specifying a test index to stop testing at. </p>
<p> <code>stride</code> An optional integer specifying the increment. </p>
<p> <code>specificTests</code> An optional array of integers specifying specific test indices to run. </p>
<p> <code>exclude</code> An optional object specifying which tests to exclude. The object may contain the following fields. </p>
<p> <code>name</code> An optional string specifying a regex for test names. Equivalent to passing <code>&#8211;exclude-regex</code> on the command line. This field supports macro expansion. </p>
<p> <code>label</code> An optional string specifying a regex for test labels. Equivalent to passing <code>&#8211;label-exclude</code> on the command line. This field supports macro expansion. </p>
<p> <code>fixtures</code> An optional object specifying which fixtures to exclude from adding tests. The object may contain the following fields. </p>
<p> <code>any</code> An optional string specifying a regex for text fixtures to exclude from adding any tests. Equivalent to <code>&#8211;fixture-exclude-any</code> on the command line. This field supports macro expansion. </p>
<p> <code>setup</code> An optional string specifying a regex for text fixtures to exclude from adding setup tests. Equivalent to <code>&#8211;fixture-exclude-setup</code> on the command line. This field supports macro expansion. </p>
<p> <code>cleanup</code> An optional string specifying a regex for text fixtures to exclude from adding cleanup tests. Equivalent to <code>&#8211;fixture-exclude-cleanup</code> on the command line. This field supports macro expansion. </p>
<p> <code>execution</code> An optional object specifying options for test execution. The object may contain the following fields. </p>
<p> <code>stopOnFailure</code> An optional bool. If true, equivalent to passing <code>&#8211;stop-on-failure</code> on the command line. </p>
<p> <code>enableFailover</code> An optional bool. If true, equivalent to passing <code>-F</code> on the command line. </p>
<p> <code>jobs</code> An optional integer. Equivalent to passing <code>&#8211;parallel</code> on the command line. </p>
<p> <code>resourceSpecFile</code> An optional string. Equivalent to passing <code>&#8211;resource-spec-file</code> on the command line. This field supports macro expansion. </p>
<p> <code>testLoad</code> An optional integer. Equivalent to passing <code>&#8211;test-load</code> on the command line. </p>
<p> <code>showOnly</code> An optional string. Equivalent to passing <code>&#8211;show-only</code> on the command line. The string must be one of the following values: </p>
<p> <code>human</code> </p>
<p> <code>json-v1</code> </p>
<p> <code>repeat</code> An optional object specifying how to repeat tests. Equivalent to passing <code>&#8211;repeat</code> on the command line. The object must have the following fields. </p>
<p> <code>mode</code> A required string. Must be one of the following values: </p>
<p> <code>until-fail</code> </p>
<p> <code>until-pass</code> </p>
<p> <code>after-timeout</code> </p>
<p> <code>count</code> A required integer. </p>
<p> <code>interactiveDebugging</code> An optional bool. If true, equivalent to passing <code>&#8211;interactive-debug-mode 1</code> on the command line. If false, equivalent to passing <code>&#8211;interactive-debug-mode 0</code> on the command line. </p>
<p> <code>scheduleRandom</code> An optional bool. If true, equivalent to passing <code>&#8211;schedule-random</code> on the command line. </p>
<p> <code>timeout</code> An optional integer. Equivalent to passing <code>&#8211;timeout</code> on the command line. </p>
<p> <code>noTestsAction</code> An optional string specifying the behavior if no tests are found. Must be one of the following values: </p>
<p> <code>default</code> Equivalent to not passing any value on the command line. </p>
<p> <code>error</code> Equivalent to passing <code>&#8211;no-tests=error</code> on the command line. </p>
<p> <code>ignore</code> Equivalent to passing <code>&#8211;no-tests=ignore</code> on the command line.</p>
<h3>Condition</h3>
<p>The <code>condition</code> field of a preset, allowed in preset files specifying version <code>3</code> or above, is used to determine whether or not the preset is enabled. For example, this can be used to disable a preset on platforms other than Windows. <code>condition</code> may be either a boolean, <code>null</code>, or an object. If it is a boolean, the boolean indicates whether the preset is enabled or disabled. If it is <code>null</code>, the preset is enabled, but the <code>null</code> condition is not inherited by any presets that may inherit from the preset. Sub-conditions (for example in a <code>not</code>, <code>anyOf</code>, or <code>allOf</code> condition) may not be <code>null</code>. If it is an object, it has the following fields: </p>
<p> <code>type</code> A required string with one of the following values: </p>
<p> <code>&quot;const&quot;</code> Indicates that the condition is constant. This is equivalent to using a boolean in place of the object. The condition object will have the following additional fields: </p>
<p> <code>value</code> A required boolean which provides a constant value for the condition&#8217;s evaluation. </p>
<p> <code>&quot;equals&quot;</code> </p>
<p> <code>&quot;notEquals&quot;</code> Indicates that the condition compares two strings to see if they are equal (or not equal). The condition object will have the following additional fields: </p>
<p> <code>lhs</code> First string to compare. This field supports macro expansion. </p>
<p> <code>rhs</code> Second string to compare. This field supports macro expansion. </p>
<p> <code>&quot;inList&quot;</code> </p>
<p> <code>&quot;notInList&quot;</code> Indicates that the condition searches for a string in a list of strings. The condition object will have the following additional fields: </p>
<p> <code>string</code> A required string to search for. This field supports macro expansion. </p>
<p> <code>list</code> A required list of strings to search. This field supports macro expansion, and uses short-circuit evaluation. </p>
<p> <code>&quot;matches&quot;</code> </p>
<p> <code>&quot;notMatches&quot;</code> Indicates that the condition searches for a regular expression in a string. The condition object will have the following additional fields: </p>
<p> <code>string</code> A required string to search. This field supports macro expansion. </p>
<p> <code>regex</code> A required regular expression to search for. This field supports macro expansion. </p>
<p> <code>&quot;anyOf&quot;</code> </p>
<p> <code>&quot;allOf&quot;</code> Indicates that the condition is an aggregation of zero or more nested conditions. The condition object will have the following additional fields: </p>
<p> <code>conditions</code> A required array of condition objects. These conditions use short-circuit evaluation. </p>
<p> <code>&quot;not&quot;</code> Indicates that the condition is an inversion of another condition. The condition object will have the following additional fields: </p>
<p> <code>condition</code> A required condition object.</p>
<h3>Macro Expansion</h3>
<p>As mentioned above, some fields support macro expansion. Macros are recognized in the form <code>$&lt;macro-namespace&gt;{&lt;macro-name&gt;}</code>. All macros are evaluated in the context of the preset being used, even if the macro is in a field that was inherited from another preset. For example, if the <code>Base</code> preset sets variable <code>PRESET_NAME</code> to <code>${presetName}</code>, and the <code>Derived</code> preset inherits from <code>Base</code>, <code>PRESET_NAME</code> will be set to <code>Derived</code>. </p>
<p> It is an error to not put a closing brace at the end of a macro name. For example, <code>${sourceDir</code> is invalid. A dollar sign (<code>$</code>) followed by anything other than a left curly brace (<code>{</code>) with a possible namespace is interpreted as a literal dollar sign. </p>
<p> Recognized macros include: </p>
<p> <code>${sourceDir}</code> Path to the project source directory. </p>
<p> <code>${sourceParentDir}</code> Path to the project source directory&#8217;s parent directory. </p>
<p> <code>${sourceDirName}</code> The last filename component of <code>${sourceDir}</code>. For example, if <code>${sourceDir}</code> is <code>/path/to/source</code>, this would be <code>source</code>. </p>
<p> <code>${presetName}</code> Name specified in the preset&#8217;s <code>name</code> field. </p>
<p> <code>${generator}</code> Generator specified in the preset&#8217;s <code>generator</code> field. For build and test presets, this will evaluate to the generator specified by <code>configurePreset</code>. </p>
<p> <code>${hostSystemName}</code> The name of the host operating system. Contains the same value as <code>CMAKE_HOST_SYSTEM_NAME</code>. This is allowed in preset files specifying version <code>3</code> or above. </p>
<p> <code>${dollar}</code> A literal dollar sign (<code>$</code>). </p>
<p> <code>$env{&lt;variable-name&gt;}</code> Environment variable with name <code>&lt;variable-name&gt;</code>. The variable name may not be an empty string. If the variable is defined in the <code>environment</code> field, that value is used instead of the value from the parent environment. If the environment variable is not defined, this evaluates as an empty string. </p>
<p> Note that while Windows environment variable names are case-insensitive, variable names within a preset are still case-sensitive. This may lead to unexpected results when using inconsistent casing. For best results, keep the casing of environment variable names consistent. </p>
<p> <code>$penv{&lt;variable-name&gt;}</code> Similar to <code>$env{&lt;variable-name&gt;}</code>, except that the value only comes from the parent environment, and never from the <code>environment</code> field. This allows you to prepend or append values to existing environment variables. For example, setting <code>PATH</code> to <code>/path/to/ninja/bin:$penv{PATH}</code> will prepend <code>/path/to/ninja/bin</code> to the <code>PATH</code> environment variable. This is needed because <code>$env{&lt;variable-name&gt;}</code> does not allow circular references. </p>
<p> <code>$vendor{&lt;macro-name&gt;}</code> An extension point for vendors to insert their own macros. CMake will not be able to use presets which have a <code>$vendor{&lt;macro-name&gt;}</code> macro, and effectively ignores such presets. However, it will still be able to use other presets from the same file. </p>
<p> CMake does not make any attempt to interpret <code>$vendor{&lt;macro-name&gt;}</code> macros. However, to avoid name collisions, IDE vendors should prefix <code>&lt;macro-name&gt;</code> with a very short (preferably &lt;= 4 characters) vendor identifier prefix, followed by a <code>.</code>, followed by the macro name. For example, the Example IDE could have <code>$vendor{xide.ideInstallDir}</code>.</p>
<h2>Schema</h2>
<p><code>This file</code> provides a machine-readable JSON schema for the <code>CMakePresets.json</code> format.</p>
<h2>Copyright</h2>
<p>2000-2022 Kitware, Inc. and Contributors</p>
