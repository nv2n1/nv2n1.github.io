---
title: "cmake-modules(7)"
name: "cmake-modules"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake-modules/"
description: "cmake-modules – CMake Modules Reference"
---

<p>cmake-modules &#8211; CMake Modules Reference </p>
<p> The modules listed here are part of the CMake distribution. Projects may provide further modules; their location(s) can be specified in the <code>CMAKE_MODULE_PATH</code> variable.</p>
<h2>Utility Modules</h2>
<p>These modules are loaded using the <code>include()</code> command.</p>
<h3>AndroidTestUtilities</h3>
<p>New in version 3.7. </p>
<p> Create a test that automatically loads specified data onto an Android device.</p>
<h3>Introduction</h3>
<p>Use this module to push data needed for testing an Android device behavior onto a connected Android device. The module will accept files and libraries as well as separate destinations for each. It will create a test that loads the files into a device object store and link to them from the specified destination. The files are only uploaded if they are not already in the object store. </p>
<p> For example: </p>
<pre>include(AndroidTestUtilities)
android_add_test_data(
 example_setup_test
 FILES &lt;files&gt;...
 LIBS &lt;libs&gt;...
 DEVICE_TEST_DIR &quot;/data/local/tests/example&quot;
 DEVICE_OBJECT_STORE &quot;/sdcard/.ExternalData/SHA&quot;
 )</pre>
<p>At build time a test named &quot;example_setup_test&quot; will be created. Run this test on the command line with <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> to load the data onto the Android device.</p>
<h3>Module Functions</h3>
<dl>
<dt><code>android_add_test_data</code></p>
<dd>
<pre>android_add_test_data(&lt;test-name&gt;
 [FILES &lt;files&gt;...] [FILES_DEST &lt;device-dir&gt;]
 [LIBS &lt;libs&gt;...] [LIBS_DEST &lt;device-dir&gt;]
 [DEVICE_OBJECT_STORE &lt;device-dir&gt;]
 [DEVICE_TEST_DIR &lt;device-dir&gt;]
 [NO_LINK_REGEX &lt;strings&gt;...]
 )</pre>
<p>The <code>android_add_test_data</code> function is used to copy files and libraries needed to run project-specific tests. On the host operating system, this is done at build time. For on-device testing, the files are loaded onto the device by the manufactured test at run time. </p>
<p> This function accepts the following named parameters:</p>
<dt><code>FILES &lt;files&gt;&#8230;</code></p>
<dd>zero or more files needed for testing</p>
<dt><code>LIBS &lt;libs&gt;&#8230;</code></p>
<dd>zero or more libraries needed for testing</p>
<dt><code>FILES_DEST &lt;device-dir&gt;</code></p>
<dd>absolute path where the data files are expected to be</p>
<dt><code>LIBS_DEST &lt;device-dir&gt;</code></p>
<dd>absolute path where the libraries are expected to be</p>
<dt><code>DEVICE_OBJECT_STORE &lt;device-dir&gt;</code></p>
<dd>absolute path to the location where the data is stored on-device</p>
<dt><code>DEVICE_TEST_DIR &lt;device-dir&gt;</code></p>
<dd>absolute path to the root directory of the on-device test location</p>
<dt><code>NO_LINK_REGEX &lt;strings&gt;&#8230;</code></p>
<dd>list of regex strings matching the names of files that should be copied from the object store to the testing directory</dl>
<h3>BundleUtilities</h3>
<p>Functions to help assemble a standalone bundle application. </p>
<p> A collection of CMake utility functions useful for dealing with <code>.app</code> bundles on the Mac and bundle-like directories on any OS. </p>
<p> The following functions are provided by this module: </p>
<pre>fixup_bundle
copy_and_fixup_bundle
verify_app
get_bundle_main_executable
get_dotapp_dir
get_bundle_and_executable
get_bundle_all_executables
get_item_key
get_item_rpaths
clear_bundle_keys
set_bundle_key_values
get_bundle_keys
copy_resolved_item_into_bundle
copy_resolved_framework_into_bundle
fixup_bundle_item
verify_bundle_prerequisites
verify_bundle_symlinks</pre>
<p>Requires CMake 2.6 or greater because it uses function, break and <code>PARENT_SCOPE</code>. Also depends on <code>GetPrerequisites.cmake</code>. </p>
<p> DO NOT USE THESE FUNCTIONS AT CONFIGURE TIME (from <code>CMakeLists.txt</code>)! Instead, invoke them from an <code>install(CODE)</code> or <code>install(SCRIPT)</code> rule. </p>
<pre>fixup_bundle(&lt;app&gt; &lt;libs&gt; &lt;dirs&gt;)</pre>
<p>Fix up <code>&lt;app&gt;</code> bundle in-place and make it standalone, such that it can be drag-n-drop copied to another machine and run on that machine as long as all of the system libraries are compatible. </p>
<p> If you pass plugins to <code>fixup_bundle</code> as the libs parameter, you should install them or copy them into the bundle before calling <code>fixup_bundle</code>. The <code>&lt;libs&gt;</code> parameter is a list of libraries that must be fixed up, but that cannot be determined by <code>otool</code> output analysis (i.e. <code>plugins</code>). </p>
<p> Gather all the keys for all the executables and libraries in a bundle, and then, for each key, copy each prerequisite into the bundle. Then fix each one up according to its own list of prerequisites. </p>
<p> Then clear all the keys and call <code>verify_app</code> on the final bundle to ensure that it is truly standalone. </p>
<p> New in version 3.6: As an optional parameter (<code>IGNORE_ITEM</code>) a list of file names can be passed, which are then ignored (e.g. <code>IGNORE_ITEM &quot;vcredist_x86.exe;vcredist_x64.exe&quot;</code>). </p>
<pre>copy_and_fixup_bundle(&lt;src&gt; &lt;dst&gt; &lt;libs&gt; &lt;dirs&gt;)</pre>
<p>Makes a copy of the bundle <code>&lt;src&gt;</code> at location <code>&lt;dst&gt;</code> and then fixes up the new copied bundle in-place at <code>&lt;dst&gt;</code>. </p>
<pre>verify_app(&lt;app&gt;)</pre>
<p>Verifies that an application <code>&lt;app&gt;</code> appears valid based on running analysis tools on it. Calls <code>message(FATAL_ERROR)</code> if the application is not verified. </p>
<p> New in version 3.6: As an optional parameter (<code>IGNORE_ITEM</code>) a list of file names can be passed, which are then ignored (e.g. <code>IGNORE_ITEM &quot;vcredist_x86.exe;vcredist_x64.exe&quot;</code>) </p>
<pre>get_bundle_main_executable(&lt;bundle&gt; &lt;result_var&gt;)</pre>
<p>The result will be the full path name of the bundle&#8217;s main executable file or an <code>error:</code> prefixed string if it could not be determined. </p>
<pre>get_dotapp_dir(&lt;exe&gt; &lt;dotapp_dir_var&gt;)</pre>
<p>Returns the nearest parent dir whose name ends with <code>.app</code> given the full path to an executable. If there is no such parent dir, then simply return the dir containing the executable. </p>
<p> The returned directory may or may not exist. </p>
<pre>get_bundle_and_executable(&lt;app&gt; &lt;bundle_var&gt; &lt;executable_var&gt; &lt;valid_var&gt;)</pre>
<p>Takes either a <code>.app</code> directory name or the name of an executable nested inside a <code>.app</code> directory and returns the path to the <code>.app</code> directory in <code>&lt;bundle_var&gt;</code> and the path to its main executable in <code>&lt;executable_var&gt;</code>. </p>
<pre>get_bundle_all_executables(&lt;bundle&gt; &lt;exes_var&gt;)</pre>
<p>Scans <code>&lt;bundle&gt;</code> bundle recursively for all <code>&lt;exes_var&gt;</code> executable files and accumulates them into a variable. </p>
<pre>get_item_key(&lt;item&gt; &lt;key_var&gt;)</pre>
<p>Given <code>&lt;item&gt;</code> file name, generate <code>&lt;key_var&gt;</code> key that should be unique considering the set of libraries that need copying or fixing up to make a bundle standalone. This is essentially the file name including extension with <code>.</code> replaced by <code>_</code> </p>
<p> This key is used as a prefix for CMake variables so that we can associate a set of variables with a given item based on its key. </p>
<pre>clear_bundle_keys(&lt;keys_var&gt;)</pre>
<p>Loop over the <code>&lt;keys_var&gt;</code> list of keys, clearing all the variables associated with each key. After the loop, clear the list of keys itself. </p>
<p> Caller of <code>get_bundle_keys</code> should call <code>clear_bundle_keys</code> when done with list of keys. </p>
<pre>set_bundle_key_values(&lt;keys_var&gt; &lt;context&gt; &lt;item&gt; &lt;exepath&gt; &lt;dirs&gt;
 &lt;copyflag&gt; [&lt;rpaths&gt;])</pre>
<p>Add <code>&lt;keys_var&gt;</code> key to the list (if necessary) for the given item. If added, also set all the variables associated with that key. </p>
<pre>get_bundle_keys(&lt;app&gt; &lt;libs&gt; &lt;dirs&gt; &lt;keys_var&gt;)</pre>
<p>Loop over all the executable and library files within <code>&lt;app&gt;</code> bundle (and given as extra <code>&lt;libs&gt;</code>) and accumulate a list of keys representing them. Set values associated with each key such that we can loop over all of them and copy prerequisite libs into the bundle and then do appropriate <code>install_name_tool</code> fixups. </p>
<p> New in version 3.6: As an optional parameter (<code>IGNORE_ITEM</code>) a list of file names can be passed, which are then ignored (e.g. <code>IGNORE_ITEM &quot;vcredist_x86.exe;vcredist_x64.exe&quot;</code>) </p>
<pre>copy_resolved_item_into_bundle(&lt;resolved_item&gt; &lt;resolved_embedded_item&gt;)</pre>
<p>Copy a resolved item into the bundle if necessary. Copy is not necessary, if the <code>&lt;resolved_item&gt;</code> is &quot;the same as&quot; the <code>&lt;resolved_embedded_item&gt;</code>. </p>
<pre>copy_resolved_framework_into_bundle(&lt;resolved_item&gt; &lt;resolved_embedded_item&gt;)</pre>
<p>Copy a resolved framework into the bundle if necessary. Copy is not necessary, if the <code>&lt;resolved_item&gt;</code> is &quot;the same as&quot; the <code>&lt;resolved_embedded_item&gt;</code>. </p>
<p> By default, <code>BU_COPY_FULL_FRAMEWORK_CONTENTS</code> is not set. If you want full frameworks embedded in your bundles, set <code>BU_COPY_FULL_FRAMEWORK_CONTENTS</code> to <code>ON</code> before calling fixup_bundle. By default, <code>COPY_RESOLVED_FRAMEWORK_INTO_BUNDLE</code> copies the framework dylib itself plus the framework <code>Resources</code> directory. </p>
<pre>fixup_bundle_item(&lt;resolved_embedded_item&gt; &lt;exepath&gt; &lt;dirs&gt;)</pre>
<p>Get the direct/non-system prerequisites of the <code>&lt;resolved_embedded_item&gt;</code>. For each prerequisite, change the way it is referenced to the value of the <code>_EMBEDDED_ITEM</code> keyed variable for that prerequisite. (Most likely changing to an <code>@executable_path</code> style reference.) </p>
<p> This function requires that the <code>&lt;resolved_embedded_item&gt;</code> be <code>inside</code> the bundle already. In other words, if you pass plugins to <code>fixup_bundle</code> as the libs parameter, you should install them or copy them into the bundle before calling <code>fixup_bundle</code>. The <code>libs</code> parameter is a list of libraries that must be fixed up, but that cannot be determined by otool output analysis. (i.e., <code>plugins</code>) </p>
<p> Also, change the id of the item being fixed up to its own <code>_EMBEDDED_ITEM</code> value. </p>
<p> Accumulate changes in a local variable and make <i>one</i> call to <code>install_name_tool</code> at the end of the function with all the changes at once. </p>
<p> If the <code>BU_CHMOD_BUNDLE_ITEMS</code> variable is set then bundle items will be marked writable before <code>install_name_tool</code> tries to change them. </p>
<pre>verify_bundle_prerequisites(&lt;bundle&gt; &lt;result_var&gt; &lt;info_var&gt;)</pre>
<p>Verifies that the sum of all prerequisites of all files inside the bundle are contained within the bundle or are <code>system</code> libraries, presumed to exist everywhere. </p>
<p> New in version 3.6: As an optional parameter (<code>IGNORE_ITEM</code>) a list of file names can be passed, which are then ignored (e.g. <code>IGNORE_ITEM &quot;vcredist_x86.exe;vcredist_x64.exe&quot;</code>) </p>
<pre>verify_bundle_symlinks(&lt;bundle&gt; &lt;result_var&gt; &lt;info_var&gt;)</pre>
<p>Verifies that any symlinks found in the <code>&lt;bundle&gt;</code> bundle point to other files that are already also in the bundle&#8230; Anything that points to an external file causes this function to fail the verification.</p>
<h3>CheckCCompilerFlag</h3>
<p>Check whether the C compiler supports a given flag.</p>
<dl>
<dt><code>check_c_compiler_flag</code></p>
<dd>
<pre>check_c_compiler_flag(&lt;flag&gt; &lt;var&gt;)</pre>
<p>Check that the <code>&lt;flag&gt;</code> is accepted by the compiler without a diagnostic. Stores the result in an internal cache entry named <code>&lt;var&gt;</code>. </p>
<p> This command temporarily sets the <code>CMAKE_REQUIRED_DEFINITIONS</code> variable and calls the <code>check_c_source_compiles</code> macro from the <code>CheckCSourceCompiles</code> module. See documentation of that module for a listing of variables that can otherwise modify the build. </p>
<p> A positive result from this check indicates only that the compiler did not issue a diagnostic message when given the flag. Whether the flag has any effect or even a specific one is beyond the scope of this module. </p>
<p> <code>NOTE:</code> Since the <code>try_compile()</code> command forwards flags from variables like <code>CMAKE_C_FLAGS</code>, unknown flags in such variables may cause a false negative for this check.</dl>
<h3>CheckCompilerFlag</h3>
<p>New in version 3.19. </p>
<p> Check whether the compiler supports a given flag.</p>
<dl>
<dt><code>check_compiler_flag</code></p>
<dd>
<pre>check_compiler_flag(&lt;lang&gt; &lt;flag&gt; &lt;var&gt;)</pre>
<p>Check that the <code>&lt;flag&gt;</code> is accepted by the compiler without a diagnostic. Stores the result in an internal cache entry named <code>&lt;var&gt;</code>. </p>
<p> This command temporarily sets the <code>CMAKE_REQUIRED_DEFINITIONS</code> variable and calls the <code>check_source_compiles(&lt;LANG&gt;)</code> function from the <code>CheckSourceCompiles</code> module. See documentation of that module for a listing of variables that can otherwise modify the build. </p>
<p> A positive result from this check indicates only that the compiler did not issue a diagnostic message when given the flag. Whether the flag has any effect or even a specific one is beyond the scope of this module. </p>
<p> <code>NOTE:</code> Since the <code>try_compile()</code> command forwards flags from variables like <code>CMAKE_&lt;LANG&gt;_FLAGS</code>, unknown flags in such variables may cause a false negative for this check.</dl>
<h3>CheckCSourceCompiles</h3>
<p>Check if given C source compiles and links into an executable.</p>
<dl>
<dt><code>check_c_source_compiles</code></p>
<dd>
<pre>check_c_source_compiles(&lt;code&gt; &lt;resultVar&gt;
 [FAIL_REGEX &lt;regex1&gt; [&lt;regex2&gt;...]])</pre>
<p>Check that the source supplied in <code>&lt;code&gt;</code> can be compiled as a C source file and linked as an executable (so it must contain at least a <code>main()</code> function). The result will be stored in the internal cache variable specified by <code>&lt;resultVar&gt;</code>, with a boolean true value for success and boolean false for failure. If <code>FAIL_REGEX</code> is provided, then failure is determined by checking if anything in the output matches any of the specified regular expressions. </p>
<p> The underlying check is performed by the <code>try_compile()</code> command. The compile and link commands can be influenced by setting any of the following variables prior to calling <code>check_c_source_compiles()</code>:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>Additional flags to pass to the compiler. Note that the contents of <code>CMAKE_C_FLAGS</code> and its associated configuration-specific variable are automatically added to the compiler command before the contents of <code>CMAKE_REQUIRED_FLAGS</code>.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>A ;-list of compiler definitions of the form <code>-DFOO</code> or <code>-DFOO=bar</code>. A definition for the name specified by <code>&lt;resultVar&gt;</code> will also be added automatically.</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>A ;-list of header search paths to pass to the compiler. These will be the only header search paths used by <code>try_compile()</code>, i.e. the contents of the <code>INCLUDE_DIRECTORIES</code> directory property will be ignored.</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>New in version 3.14. </p>
<p> A ;-list of options to add to the link command (see <code>try_compile()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>A ;-list of libraries to add to the link command. These can be the name of system libraries or they can be Imported Targets (see <code>try_compile()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>New in version 3.1. </p>
<p> If this variable evaluates to a boolean true value, all status messages associated with the check will be suppressed. </p>
<p> The check is only performed once, with the result cached in the variable named by <code>&lt;resultVar&gt;</code>. Every subsequent CMake run will re-use this cached value rather than performing the check again, even if the <code>&lt;code&gt;</code> changes. In order to force the check to be re-evaluated, the variable named by <code>&lt;resultVar&gt;</code> must be manually removed from the cache.</dl>
<h3>CheckCSourceRuns</h3>
<p>Check if given C source compiles and links into an executable and can subsequently be run.</p>
<dl>
<dt><code>check_c_source_runs</code></p>
<dd>
<pre>check_c_source_runs(&lt;code&gt; &lt;resultVar&gt;)</pre>
<p>Check that the source supplied in <code>&lt;code&gt;</code> can be compiled as a C source file, linked as an executable and then run. The <code>&lt;code&gt;</code> must contain at least a <code>main()</code> function. If the <code>&lt;code&gt;</code> could be built and run successfully, the internal cache variable specified by <code>&lt;resultVar&gt;</code> will be set to 1, otherwise it will be set to an value that evaluates to boolean false (e.g. an empty string or an error message). </p>
<p> The underlying check is performed by the <code>try_run()</code> command. The compile and link commands can be influenced by setting any of the following variables prior to calling <code>check_c_source_runs()</code>:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>Additional flags to pass to the compiler. Note that the contents of <code>CMAKE_C_FLAGS</code> and its associated configuration-specific variable are automatically added to the compiler command before the contents of <code>CMAKE_REQUIRED_FLAGS</code>.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>A ;-list of compiler definitions of the form <code>-DFOO</code> or <code>-DFOO=bar</code>. A definition for the name specified by <code>&lt;resultVar&gt;</code> will also be added automatically.</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>A ;-list of header search paths to pass to the compiler. These will be the only header search paths used by <code>try_run()</code>, i.e. the contents of the <code>INCLUDE_DIRECTORIES</code> directory property will be ignored.</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>New in version 3.14. </p>
<p> A ;-list of options to add to the link command (see <code>try_run()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>A ;-list of libraries to add to the link command. These can be the name of system libraries or they can be Imported Targets (see <code>try_run()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>New in version 3.1. </p>
<p> If this variable evaluates to a boolean true value, all status messages associated with the check will be suppressed. </p>
<p> The check is only performed once, with the result cached in the variable named by <code>&lt;resultVar&gt;</code>. Every subsequent CMake run will re-use this cached value rather than performing the check again, even if the <code>&lt;code&gt;</code> changes. In order to force the check to be re-evaluated, the variable named by <code>&lt;resultVar&gt;</code> must be manually removed from the cache.</dl>
<h3>CheckCXXCompilerFlag</h3>
<p>Check whether the CXX compiler supports a given flag.</p>
<dl>
<dt><code>check_cxx_compiler_flag</code></p>
<dd>
<pre>check_cxx_compiler_flag(&lt;flag&gt; &lt;var&gt;)</pre>
<p>Check that the <code>&lt;flag&gt;</code> is accepted by the compiler without a diagnostic. Stores the result in an internal cache entry named <code>&lt;var&gt;</code>. </p>
<p> This command temporarily sets the <code>CMAKE_REQUIRED_DEFINITIONS</code> variable and calls the <code>check_cxx_source_compiles</code> macro from the <code>CheckCXXSourceCompiles</code> module. See documentation of that module for a listing of variables that can otherwise modify the build. </p>
<p> A positive result from this check indicates only that the compiler did not issue a diagnostic message when given the flag. Whether the flag has any effect or even a specific one is beyond the scope of this module. </p>
<p> <code>NOTE:</code> Since the <code>try_compile()</code> command forwards flags from variables like <code>CMAKE_CXX_FLAGS</code>, unknown flags in such variables may cause a false negative for this check.</dl>
<h3>CheckCXXSourceCompiles</h3>
<p>Check if given C++ source compiles and links into an executable.</p>
<dl>
<dt><code>check_cxx_source_compiles</code></p>
<dd>
<pre>check_cxx_source_compiles(&lt;code&gt; &lt;resultVar&gt;
 [FAIL_REGEX &lt;regex1&gt; [&lt;regex2&gt;...]])</pre>
<p>Check that the source supplied in <code>&lt;code&gt;</code> can be compiled as a C++ source file and linked as an executable (so it must contain at least a <code>main()</code> function). The result will be stored in the internal cache variable specified by <code>&lt;resultVar&gt;</code>, with a boolean true value for success and boolean false for failure. If <code>FAIL_REGEX</code> is provided, then failure is determined by checking if anything in the output matches any of the specified regular expressions. </p>
<p> The underlying check is performed by the <code>try_compile()</code> command. The compile and link commands can be influenced by setting any of the following variables prior to calling <code>check_cxx_source_compiles()</code>:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>Additional flags to pass to the compiler. Note that the contents of <code>CMAKE_CXX_FLAGS</code> and its associated configuration-specific variable are automatically added to the compiler command before the contents of <code>CMAKE_REQUIRED_FLAGS</code>.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>A ;-list of compiler definitions of the form <code>-DFOO</code> or <code>-DFOO=bar</code>. A definition for the name specified by <code>&lt;resultVar&gt;</code> will also be added automatically.</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>A ;-list of header search paths to pass to the compiler. These will be the only header search paths used by <code>try_compile()</code>, i.e. the contents of the <code>INCLUDE_DIRECTORIES</code> directory property will be ignored.</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>New in version 3.14. </p>
<p> A ;-list of options to add to the link command (see <code>try_compile()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>A ;-list of libraries to add to the link command. These can be the name of system libraries or they can be Imported Targets (see <code>try_compile()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>New in version 3.1. </p>
<p> If this variable evaluates to a boolean true value, all status messages associated with the check will be suppressed. </p>
<p> The check is only performed once, with the result cached in the variable named by <code>&lt;resultVar&gt;</code>. Every subsequent CMake run will re-use this cached value rather than performing the check again, even if the <code>&lt;code&gt;</code> changes. In order to force the check to be re-evaluated, the variable named by <code>&lt;resultVar&gt;</code> must be manually removed from the cache.</dl>
<h3>CheckCXXSourceRuns</h3>
<p>Check if given C++ source compiles and links into an executable and can subsequently be run.</p>
<dl>
<dt><code>check_cxx_source_runs</code></p>
<dd>
<pre>check_cxx_source_runs(&lt;code&gt; &lt;resultVar&gt;)</pre>
<p>Check that the source supplied in <code>&lt;code&gt;</code> can be compiled as a C++ source file, linked as an executable and then run. The <code>&lt;code&gt;</code> must contain at least a <code>main()</code> function. If the <code>&lt;code&gt;</code> could be built and run successfully, the internal cache variable specified by <code>&lt;resultVar&gt;</code> will be set to 1, otherwise it will be set to an value that evaluates to boolean false (e.g. an empty string or an error message). </p>
<p> The underlying check is performed by the <code>try_run()</code> command. The compile and link commands can be influenced by setting any of the following variables prior to calling <code>check_cxx_source_runs()</code>:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>Additional flags to pass to the compiler. Note that the contents of <code>CMAKE_CXX_FLAGS</code> and its associated configuration-specific variable are automatically added to the compiler command before the contents of <code>CMAKE_REQUIRED_FLAGS</code>.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>A ;-list of compiler definitions of the form <code>-DFOO</code> or <code>-DFOO=bar</code>. A definition for the name specified by <code>&lt;resultVar&gt;</code> will also be added automatically.</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>A ;-list of header search paths to pass to the compiler. These will be the only header search paths used by <code>try_run()</code>, i.e. the contents of the <code>INCLUDE_DIRECTORIES</code> directory property will be ignored.</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>New in version 3.14. </p>
<p> A ;-list of options to add to the link command (see <code>try_run()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>A ;-list of libraries to add to the link command. These can be the name of system libraries or they can be Imported Targets (see <code>try_run()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>New in version 3.1. </p>
<p> If this variable evaluates to a boolean true value, all status messages associated with the check will be suppressed. </p>
<p> The check is only performed once, with the result cached in the variable named by <code>&lt;resultVar&gt;</code>. Every subsequent CMake run will re-use this cached value rather than performing the check again, even if the <code>&lt;code&gt;</code> changes. In order to force the check to be re-evaluated, the variable named by <code>&lt;resultVar&gt;</code> must be manually removed from the cache.</dl>
<h3>CheckCXXSymbolExists</h3>
<p>Check if a symbol exists as a function, variable, or macro in <code>C++</code>.</p>
<dl>
<dt><code>check_cxx_symbol_exists</code></p>
<dd>
<pre>check_cxx_symbol_exists(&lt;symbol&gt; &lt;files&gt; &lt;variable&gt;)</pre>
<p>Check that the <code>&lt;symbol&gt;</code> is available after including given header <code>&lt;files&gt;</code> and store the result in a <code>&lt;variable&gt;</code>. Specify the list of files in one argument as a semicolon-separated list. <code>check_cxx_symbol_exists()</code> can be used to check for symbols as seen by the C++ compiler, as opposed to <code>check_symbol_exists()</code>, which always uses the <code>C</code> compiler. </p>
<p> If the header files define the symbol as a macro it is considered available and assumed to work. If the header files declare the symbol as a function or variable then the symbol must also be available for linking. If the symbol is a type, enum value, or C++ template it will not be recognized: consider using the <code>CheckTypeSize</code> or <code>CheckSourceCompiles</code> module instead. </p>
<p> <code>NOTE:</code> This command is unreliable when <code>&lt;symbol&gt;</code> is (potentially) an overloaded function. Since there is no reliable way to predict whether a given function in the system environment may be defined as an overloaded function or may be an overloaded function on other systems or will become so in the future, it is generally advised to use the <code>CheckCXXSourceCompiles</code> module for checking any function symbol (unless somehow you surely know the checked function is not overloaded on other systems or will not be so in the future). </p>
<p> The following variables may be set before calling this macro to modify the way the check is run:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>string of compile command line flags.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>a ;-list of macros to define (-DFOO=bar).</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>a ;-list of header search paths to pass to the compiler.</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>New in version 3.14: a ;-list of options to add to the link command. </p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>a ;-list of libraries to add to the link command. See policy <code>CMP0075</code>.</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>New in version 3.1: execute quietly without messages. </p>
<p> For example: </p>
<pre>include(CheckCXXSymbolExists)
# Check for macro SEEK_SET
check_cxx_symbol_exists(SEEK_SET &quot;cstdio&quot; HAVE_SEEK_SET)
# Check for function std::fopen
check_cxx_symbol_exists(std::fopen &quot;cstdio&quot; HAVE_STD_FOPEN)</pre>
</dl>
<h3>CheckFortranCompilerFlag</h3>
<p>New in version 3.3. </p>
<p> Check whether the Fortran compiler supports a given flag.</p>
<dl>
<dt><code>check_fortran_compiler_flag</code></p>
<dd>
<pre>check_fortran_compiler_flag(&lt;flag&gt; &lt;var&gt;)</pre>
<p>Check that the <code>&lt;flag&gt;</code> is accepted by the compiler without a diagnostic. Stores the result in an internal cache entry named <code>&lt;var&gt;</code>. </p>
<p> This command temporarily sets the <code>CMAKE_REQUIRED_DEFINITIONS</code> variable and calls the <code>check_fortran_source_compiles</code> macro from the <code>CheckFortranSourceCompiles</code> module. See documentation of that module for a listing of variables that can otherwise modify the build. </p>
<p> A positive result from this check indicates only that the compiler did not issue a diagnostic message when given the flag. Whether the flag has any effect or even a specific one is beyond the scope of this module. </p>
<p> <code>NOTE:</code> Since the <code>try_compile()</code> command forwards flags from variables like <code>CMAKE_Fortran_FLAGS</code>, unknown flags in such variables may cause a false negative for this check.</dl>
<h3>CheckFortranFunctionExists</h3>
<p>Check if a Fortran function exists.</p>
<dl>
<dt><code>CHECK_FORTRAN_FUNCTION_EXISTS</code></p>
<dd>
<pre>CHECK_FORTRAN_FUNCTION_EXISTS(&lt;function&gt; &lt;result&gt;)</pre>
<p>where</p>
<dt><code>&lt;function&gt;</code></p>
<dd>the name of the Fortran function</p>
<dt><code>&lt;result&gt;</code></p>
<dd>variable to store the result; will be created as an internal cache variable. </p>
<p> <code>NOTE:</code> This command does not detect functions in Fortran modules. In general it is recommended to use <code>CheckSourceCompiles</code> instead to determine if a Fortran function or subroutine is available. </p>
<p> The following variables may be set before calling this macro to modify the way the check is run:</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>New in version 3.14: A ;-list of options to add to the link command (see <code>try_compile()</code> for further details). </p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>A ;-list of libraries to add to the link command. These can be the name of system libraries or they can be Imported Targets (see <code>try_compile()</code> for further details).</dl>
<h3>CheckFortranSourceCompiles</h3>
<p>New in version 3.1. </p>
<p> Check if given Fortran source compiles and links into an executable.</p>
<dl>
<dt><code>check_fortran_source_compiles</code></p>
<dd>
<pre>check_fortran_source_compiles(&lt;code&gt; &lt;resultVar&gt;
 [FAIL_REGEX &lt;regex&gt;...]
 [SRC_EXT &lt;extension&gt;]
)</pre>
<p>Checks that the source supplied in <code>&lt;code&gt;</code> can be compiled as a Fortran source file and linked as an executable. The <code>&lt;code&gt;</code> must be a Fortran program containing at least an <code>end</code> statement&#8211;for example: </p>
<pre>check_fortran_source_compiles(&quot;character :: b; error stop b; end&quot; F2018ESTOPOK SRC_EXT F90)</pre>
<p>This command can help avoid costly build processes when a compiler lacks support for a necessary feature, or a particular vendor library is not compatible with the Fortran compiler version being used. This generate-time check may advise the user of such before the main build process. See also the <code>check_fortran_source_runs()</code> command to actually run the compiled code. </p>
<p> The result will be stored in the internal cache variable <code>&lt;resultVar&gt;</code>, with a boolean true value for success and boolean false for failure. </p>
<p> If <code>FAIL_REGEX</code> is provided, then failure is determined by checking if anything in the output matches any of the specified regular expressions. </p>
<p> By default, the test source file will be given a <code>.F</code> file extension. The <code>SRC_EXT</code> option can be used to override this with <code>.&lt;extension&gt;</code> instead&#8211; <code>.F90</code> is a typical choice. </p>
<p> The underlying check is performed by the <code>try_compile()</code> command. The compile and link commands can be influenced by setting any of the following variables prior to calling <code>check_fortran_source_compiles()</code>:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>Additional flags to pass to the compiler. Note that the contents of <code>CMAKE_Fortran_FLAGS</code> and its associated configuration-specific variable are automatically added to the compiler command before the contents of <code>CMAKE_REQUIRED_FLAGS</code>.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>A ;-list of compiler definitions of the form <code>-DFOO</code> or <code>-DFOO=bar</code>. A definition for the name specified by <code>&lt;resultVar&gt;</code> will also be added automatically.</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>A ;-list of header search paths to pass to the compiler. These will be the only header search paths used by <code>try_compile()</code>, i.e. the contents of the <code>INCLUDE_DIRECTORIES</code> directory property will be ignored.</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>New in version 3.14. </p>
<p> A ;-list of options to add to the link command (see <code>try_compile()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>A ;-list of libraries to add to the link command. These can be the name of system libraries or they can be Imported Targets (see <code>try_compile()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>If this variable evaluates to a boolean true value, all status messages associated with the check will be suppressed. </p>
<p> The check is only performed once, with the result cached in the variable named by <code>&lt;resultVar&gt;</code>. Every subsequent CMake run will re-use this cached value rather than performing the check again, even if the <code>&lt;code&gt;</code> changes. In order to force the check to be re-evaluated, the variable named by <code>&lt;resultVar&gt;</code> must be manually removed from the cache.</dl>
<h3>CheckFortranSourceRuns</h3>
<p>New in version 3.14. </p>
<p> Check if given Fortran source compiles and links into an executable and can subsequently be run.</p>
<dl>
<dt><code>check_fortran_source_runs</code></p>
<dd>
<pre>check_fortran_source_runs(&lt;code&gt; &lt;resultVar&gt;
 [SRC_EXT &lt;extension&gt;])</pre>
<p>Check that the source supplied in <code>&lt;code&gt;</code> can be compiled as a Fortran source file, linked as an executable and then run. The <code>&lt;code&gt;</code> must be a Fortran program containing at least an <code>end</code> statement&#8211;for example: </p>
<pre>check_fortran_source_runs(&quot;real :: x[*]; call co_sum(x); end&quot; F2018coarrayOK)</pre>
<p>This command can help avoid costly build processes when a compiler lacks support for a necessary feature, or a particular vendor library is not compatible with the Fortran compiler version being used. Some of these failures only occur at runtime instead of linktime, and a trivial runtime example can catch the issue before the main build process. </p>
<p> If the <code>&lt;code&gt;</code> could be built and run successfully, the internal cache variable specified by <code>&lt;resultVar&gt;</code> will be set to 1, otherwise it will be set to an value that evaluates to boolean false (e.g. an empty string or an error message). </p>
<p> By default, the test source file will be given a <code>.F90</code> file extension. The <code>SRC_EXT</code> option can be used to override this with <code>.&lt;extension&gt;</code> instead. </p>
<p> The underlying check is performed by the <code>try_run()</code> command. The compile and link commands can be influenced by setting any of the following variables prior to calling <code>check_fortran_source_runs()</code>:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>Additional flags to pass to the compiler. Note that the contents of <code>CMAKE_Fortran_FLAGS</code> and its associated configuration-specific variable are automatically added to the compiler command before the contents of <code>CMAKE_REQUIRED_FLAGS</code>.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>A ;-list of compiler definitions of the form <code>-DFOO</code> or <code>-DFOO=bar</code>. A definition for the name specified by <code>&lt;resultVar&gt;</code> will also be added automatically.</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>A ;-list of header search paths to pass to the compiler. These will be the only header search paths used by <code>try_run()</code>, i.e. the contents of the <code>INCLUDE_DIRECTORIES</code> directory property will be ignored.</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>A ;-list of options to add to the link command (see <code>try_run()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>A ;-list of libraries to add to the link command. These can be the name of system libraries or they can be Imported Targets (see <code>try_run()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>If this variable evaluates to a boolean true value, all status messages associated with the check will be suppressed. </p>
<p> The check is only performed once, with the result cached in the variable named by <code>&lt;resultVar&gt;</code>. Every subsequent CMake run will re-use this cached value rather than performing the check again, even if the <code>&lt;code&gt;</code> changes. In order to force the check to be re-evaluated, the variable named by <code>&lt;resultVar&gt;</code> must be manually removed from the cache.</dl>
<h3>CheckFunctionExists</h3>
<p>Check if a C function can be linked</p>
<dl>
<dt><code>check_function_exists</code></p>
<dd>
<pre>check_function_exists(&lt;function&gt; &lt;variable&gt;)</pre>
<p>Checks that the <code>&lt;function&gt;</code> is provided by libraries on the system and store the result in a <code>&lt;variable&gt;</code>, which will be created as an internal cache variable. </p>
<p> The following variables may be set before calling this macro to modify the way the check is run:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>string of compile command line flags.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>a ;-list of macros to define (-DFOO=bar).</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>a ;-list of header search paths to pass to the compiler.</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>New in version 3.14: a ;-list of options to add to the link command. </p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>a ;-list of libraries to add to the link command. See policy <code>CMP0075</code>.</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>New in version 3.1: execute quietly without messages. </p>
<p> <code>NOTE:</code> Prefer using <code>CheckSymbolExists</code> instead of this module, for the following reasons:</p>
<dt>&bull;</p>
<dd><code>check_function_exists()</code> can&#8217;t detect functions that are inlined in headers or specified as a macro.</p>
<dt>&bull;</p>
<dd><code>check_function_exists()</code> can&#8217;t detect anything in the 32-bit versions of the Win32 API, because of a mismatch in calling conventions.</p>
<dt>&bull;</p>
<dd><code>check_function_exists()</code> only verifies linking, it does not verify that the function is declared in system headers.</dl>
<h3>CheckIncludeFileCXX</h3>
<p>Provides a macro to check if a header file can be included in <code>CXX</code>.</p>
<dl>
<dt><code>CHECK_INCLUDE_FILE_CXX</code></p>
<dd>
<pre>CHECK_INCLUDE_FILE_CXX(&lt;include&gt; &lt;variable&gt; [&lt;flags&gt;])</pre>
<p>Check if the given <code>&lt;include&gt;</code> file may be included in a <code>CXX</code> source file and store the result in an internal cache entry named <code>&lt;variable&gt;</code>. The optional third argument may be used to add compilation flags to the check (or use <code>CMAKE_REQUIRED_FLAGS</code> below). </p>
<p> The following variables may be set before calling this macro to modify the way the check is run:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>string of compile command line flags.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>a ;-list of macros to define (-DFOO=bar).</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>a ;-list of header search paths to pass to the compiler.</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>New in version 3.14: a ;-list of options to add to the link command. </p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>a ;-list of libraries to add to the link command. See policy <code>CMP0075</code>.</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>New in version 3.1: execute quietly without messages. </p>
<p> See modules <code>CheckIncludeFile</code> and <code>CheckIncludeFiles</code> to check for one or more <code>C</code> headers.</dl>
<h3>CheckIncludeFile</h3>
<p>Provides a macro to check if a header file can be included in <code>C</code>.</p>
<dl>
<dt><code>CHECK_INCLUDE_FILE</code></p>
<dd>
<pre>CHECK_INCLUDE_FILE(&lt;include&gt; &lt;variable&gt; [&lt;flags&gt;])</pre>
<p>Check if the given <code>&lt;include&gt;</code> file may be included in a <code>C</code> source file and store the result in an internal cache entry named <code>&lt;variable&gt;</code>. The optional third argument may be used to add compilation flags to the check (or use <code>CMAKE_REQUIRED_FLAGS</code> below). </p>
<p> The following variables may be set before calling this macro to modify the way the check is run:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>string of compile command line flags.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>a ;-list of macros to define (-DFOO=bar).</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>a ;-list of header search paths to pass to the compiler.</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>New in version 3.14: a ;-list of options to add to the link command. </p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>a ;-list of libraries to add to the link command. See policy <code>CMP0075</code>.</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>New in version 3.1: execute quietly without messages. </p>
<p> See the <code>CheckIncludeFiles</code> module to check for multiple headers at once. See the <code>CheckIncludeFileCXX</code> module to check for headers using the <code>CXX</code> language.</dl>
<h3>CheckIncludeFiles</h3>
<p>Provides a macro to check if a list of one or more header files can be included together.</p>
<dl>
<dt><code>CHECK_INCLUDE_FILES</code></p>
<dd>
<pre>CHECK_INCLUDE_FILES(&quot;&lt;includes&gt;&quot; &lt;variable&gt; [LANGUAGE &lt;language&gt;])</pre>
<p>Check if the given <code>&lt;includes&gt;</code> list may be included together in a source file and store the result in an internal cache entry named <code>&lt;variable&gt;</code>. Specify the <code>&lt;includes&gt;</code> argument as a ;-list of header file names. </p>
<p> If <code>LANGUAGE</code> is set, the specified compiler will be used to perform the check. Acceptable values are <code>C</code> and <code>CXX</code>. If not set, the C compiler will be used if enabled. If the C compiler is not enabled, the C++ compiler will be used if enabled. </p>
<p> The following variables may be set before calling this macro to modify the way the check is run:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>string of compile command line flags.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>a ;-list of macros to define (-DFOO=bar).</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>a ;-list of header search paths to pass to the compiler.</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>New in version 3.14: a ;-list of options to add to the link command. </p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>a ;-list of libraries to add to the link command. See policy <code>CMP0075</code>.</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>New in version 3.1: execute quietly without messages. </p>
<p> See modules <code>CheckIncludeFile</code> and <code>CheckIncludeFileCXX</code> to check for a single header file in <code>C</code> or <code>CXX</code> languages.</dl>
<h3>CheckIPOSupported</h3>
<p>New in version 3.9. </p>
<p> Check whether the compiler supports an interprocedural optimization (IPO/LTO). Use this before enabling the <code>INTERPROCEDURAL_OPTIMIZATION</code> target property.</p>
<dl>
<dt><code>check_ipo_supported</code></p>
<dd>
<pre>check_ipo_supported([RESULT &lt;result&gt;] [OUTPUT &lt;output&gt;]
 [LANGUAGES &lt;lang&gt;...])</pre>
<p>Options are:</p>
<dt><code>RESULT &lt;result&gt;</code></p>
<dd>Set <code>&lt;result&gt;</code> variable to <code>YES</code> if IPO is supported by the compiler and <code>NO</code> otherwise. If this option is not given then the command will issue a fatal error if IPO is not supported.</p>
<dt><code>OUTPUT &lt;output&gt;</code></p>
<dd>Set <code>&lt;output&gt;</code> variable with details about any error.</p>
<dt><code>LANGUAGES &lt;lang&gt;&#8230;</code></p>
<dd>Specify languages whose compilers to check. Languages <code>C</code>, <code>CXX</code>, and <code>Fortran</code> are supported. </p>
<p> It makes no sense to use this module when <code>CMP0069</code> is set to <code>OLD</code> so module will return error in this case. See policy <code>CMP0069</code> for details. </p>
<p> New in version 3.13: Add support for Visual Studio generators. </p>
</dl>
<h3>Examples</h3>
<pre>check_ipo_supported() # fatal error if IPO is not supported
set_property(TARGET foo PROPERTY INTERPROCEDURAL_OPTIMIZATION TRUE)</pre>
<pre># Optional IPO. Do not use IPO if it's not supported by compiler.
check_ipo_supported(RESULT result OUTPUT output)
if(result)
 set_property(TARGET foo PROPERTY INTERPROCEDURAL_OPTIMIZATION TRUE)
else()
 message(WARNING &quot;IPO is not supported: ${output}&quot;)
endif()</pre>
<h3>CheckLanguage</h3>
<p>Check if a language can be enabled </p>
<p> Usage: </p>
<pre>check_language(&lt;lang&gt;)</pre>
<p>where <code>&lt;lang&gt;</code> is a language that may be passed to <code>enable_language()</code> such as <code>Fortran</code>. If <code>CMAKE_&lt;LANG&gt;_COMPILER</code> is already defined the check does nothing. Otherwise it tries enabling the language in a test project. The result is cached in <code>CMAKE_&lt;LANG&gt;_COMPILER</code> as the compiler that was found, or <code>NOTFOUND</code> if the language cannot be enabled. For CUDA which can have an explicit host compiler, the cache <code>CMAKE_CUDA_HOST_COMPILER</code> variable will be set if it was required for compilation (and cleared if it was not). </p>
<p> Example: </p>
<pre>check_language(Fortran)
if(CMAKE_Fortran_COMPILER)
 enable_language(Fortran)
else()
 message(STATUS &quot;No Fortran support&quot;)
endif()</pre>
<h3>CheckLibraryExists</h3>
<p>Check if the function exists.</p>
<dl>
<dt><code>CHECK_LIBRARY_EXISTS</code></p>
<dd>
<pre>CHECK_LIBRARY_EXISTS(LIBRARY FUNCTION LOCATION VARIABLE)</pre>
<pre>LIBRARY - the name of the library you are looking for
FUNCTION - the name of the function
LOCATION - location where the library should be found
VARIABLE - variable to store the result
 Will be created as an internal cache variable.</pre>
<p>The following variables may be set before calling this macro to modify the way the check is run:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>string of compile command line flags.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>list of macros to define (-DFOO=bar).</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>New in version 3.14: list of options to pass to link command. </p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>list of libraries to link.</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>New in version 3.1: execute quietly without messages. </p>
</dl>
<h3>CheckLinkerFlag</h3>
<p>New in version 3.18. </p>
<p> Check whether the compiler supports a given link flag.</p>
<dl>
<dt><code>check_linker_flag</code></p>
<dd>
<pre>check_linker_flag(&lt;lang&gt; &lt;flag&gt; &lt;var&gt;)</pre>
<p>Check that the link <code>&lt;flag&gt;</code> is accepted by the <code>&lt;lang&gt;</code> compiler without a diagnostic. Stores the result in an internal cache entry named <code>&lt;var&gt;</code>. </p>
<p> This command temporarily sets the <code>CMAKE_REQUIRED_LINK_OPTIONS</code> variable and calls the <code>check_source_compiles()</code> command from the <code>CheckSourceCompiles</code> module. See that module&#8217;s documentation for a listing of variables that can otherwise modify the build. </p>
<p> The underlying implementation relies on the <code>LINK_OPTIONS</code> property to check the specified flag. The <code>LINKER:</code> prefix, as described in the <code>target_link_options()</code> command, can be used as well. </p>
<p> A positive result from this check indicates only that the compiler did not issue a diagnostic message when given the link flag. Whether the flag has any effect or even a specific one is beyond the scope of this module. </p>
<p> <code>NOTE:</code> Since the <code>try_compile()</code> command forwards flags from variables like <code>CMAKE_&lt;LANG&gt;_FLAGS</code>, unknown flags in such variables may cause a false negative for this check.</dl>
<h3>CheckOBJCCompilerFlag</h3>
<p>New in version 3.16. </p>
<p> Check whether the Objective-C compiler supports a given flag.</p>
<dl>
<dt><code>check_objc_compiler_flag</code></p>
<dd>
<pre>check_objc_compiler_flag(&lt;flag&gt; &lt;var&gt;)</pre>
<p>Check that the <code>&lt;flag&gt;</code> is accepted by the compiler without a diagnostic. Stores the result in an internal cache entry named <code>&lt;var&gt;</code>. </p>
<p> This command temporarily sets the <code>CMAKE_REQUIRED_DEFINITIONS</code> variable and calls the <code>check_objc_source_compiles</code> macro from the <code>CheckOBJCSourceCompiles</code> module. See documentation of that module for a listing of variables that can otherwise modify the build. </p>
<p> A positive result from this check indicates only that the compiler did not issue a diagnostic message when given the flag. Whether the flag has any effect or even a specific one is beyond the scope of this module. </p>
<p> <code>NOTE:</code> Since the <code>try_compile()</code> command forwards flags from variables like <code>CMAKE_OBJC_FLAGS</code>, unknown flags in such variables may cause a false negative for this check.</dl>
<h3>CheckOBJCSourceCompiles</h3>
<p>New in version 3.16. </p>
<p> Check if given Objective-C source compiles and links into an executable.</p>
<dl>
<dt><code>check_objc_source_compiles</code></p>
<dd>
<pre>check_objc_source_compiles(&lt;code&gt; &lt;resultVar&gt;
 [FAIL_REGEX &lt;regex1&gt; [&lt;regex2&gt;...]])</pre>
<p>Check that the source supplied in <code>&lt;code&gt;</code> can be compiled as a Objectie-C source file and linked as an executable (so it must contain at least a <code>main()</code> function). The result will be stored in the internal cache variable specified by <code>&lt;resultVar&gt;</code>, with a boolean true value for success and boolean false for failure. If <code>FAIL_REGEX</code> is provided, then failure is determined by checking if anything in the output matches any of the specified regular expressions. </p>
<p> The underlying check is performed by the <code>try_compile()</code> command. The compile and link commands can be influenced by setting any of the following variables prior to calling <code>check_objc_source_compiles()</code>:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>Additional flags to pass to the compiler. Note that the contents of <code>CMAKE_OBJC_FLAGS</code> and its associated configuration-specific variable are automatically added to the compiler command before the contents of <code>CMAKE_REQUIRED_FLAGS</code>.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>A ;-list of compiler definitions of the form <code>-DFOO</code> or <code>-DFOO=bar</code>. A definition for the name specified by <code>&lt;resultVar&gt;</code> will also be added automatically.</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>A ;-list of header search paths to pass to the compiler. These will be the only header search paths used by <code>try_compile()</code>, i.e. the contents of the <code>INCLUDE_DIRECTORIES</code> directory property will be ignored.</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>A ;-list of options to add to the link command (see <code>try_compile()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>A ;-list of libraries to add to the link command. These can be the name of system libraries or they can be Imported Targets (see <code>try_compile()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>If this variable evaluates to a boolean true value, all status messages associated with the check will be suppressed. </p>
<p> The check is only performed once, with the result cached in the variable named by <code>&lt;resultVar&gt;</code>. Every subsequent CMake run will re-use this cached value rather than performing the check again, even if the <code>&lt;code&gt;</code> changes. In order to force the check to be re-evaluated, the variable named by <code>&lt;resultVar&gt;</code> must be manually removed from the cache.</dl>
<h3>CheckOBJCSourceRuns</h3>
<p>New in version 3.16. </p>
<p> Check if given Objective-C source compiles and links into an executable and can subsequently be run.</p>
<dl>
<dt><code>check_objc_source_runs</code></p>
<dd>
<pre>check_objc_source_runs(&lt;code&gt; &lt;resultVar&gt;)</pre>
<p>Check that the source supplied in <code>&lt;code&gt;</code> can be compiled as a Objective-C source file, linked as an executable and then run. The <code>&lt;code&gt;</code> must contain at least a <code>main()</code> function. If the <code>&lt;code&gt;</code> could be built and run successfully, the internal cache variable specified by <code>&lt;resultVar&gt;</code> will be set to 1, otherwise it will be set to an value that evaluates to boolean false (e.g. an empty string or an error message). </p>
<p> The underlying check is performed by the <code>try_run()</code> command. The compile and link commands can be influenced by setting any of the following variables prior to calling <code>check_objc_source_runs()</code>:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>Additional flags to pass to the compiler. Note that the contents of <code>CMAKE_OBJC_FLAGS</code> and its associated configuration-specific variable are automatically added to the compiler command before the contents of <code>CMAKE_REQUIRED_FLAGS</code>.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>A ;-list of compiler definitions of the form <code>-DFOO</code> or <code>-DFOO=bar</code>. A definition for the name specified by <code>&lt;resultVar&gt;</code> will also be added automatically.</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>A ;-list of header search paths to pass to the compiler. These will be the only header search paths used by <code>try_run()</code>, i.e. the contents of the <code>INCLUDE_DIRECTORIES</code> directory property will be ignored.</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>A ;-list of options to add to the link command (see <code>try_run()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>A ;-list of libraries to add to the link command. These can be the name of system libraries or they can be Imported Targets (see <code>try_run()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>If this variable evaluates to a boolean true value, all status messages associated with the check will be suppressed. </p>
<p> The check is only performed once, with the result cached in the variable named by <code>&lt;resultVar&gt;</code>. Every subsequent CMake run will re-use this cached value rather than performing the check again, even if the <code>&lt;code&gt;</code> changes. In order to force the check to be re-evaluated, the variable named by <code>&lt;resultVar&gt;</code> must be manually removed from the cache.</dl>
<h3>CheckOBJCXXCompilerFlag</h3>
<p>New in version 3.16. </p>
<p> Check whether the Objective-C++ compiler supports a given flag.</p>
<dl>
<dt><code>check_objcxx_compiler_flag</code></p>
<dd>
<pre>check_objcxx_compiler_flag(&lt;flag&gt; &lt;var&gt;)</pre>
<p>Check that the <code>&lt;flag&gt;</code> is accepted by the compiler without a diagnostic. Stores the result in an internal cache entry named <code>&lt;var&gt;</code>. </p>
<p> This command temporarily sets the <code>CMAKE_REQUIRED_DEFINITIONS</code> variable and calls the <code>check_objcxx_source_compiles</code> macro from the <code>CheckOBJCXXSourceCompiles</code> module. See documentation of that module for a listing of variables that can otherwise modify the build. </p>
<p> A positive result from this check indicates only that the compiler did not issue a diagnostic message when given the flag. Whether the flag has any effect or even a specific one is beyond the scope of this module. </p>
<p> <code>NOTE:</code> Since the <code>try_compile()</code> command forwards flags from variables like <code>CMAKE_OBJCXX_FLAGS</code>, unknown flags in such variables may cause a false negative for this check.</dl>
<h3>CheckOBJCXXSourceCompiles</h3>
<p>New in version 3.16. </p>
<p> Check if given Objective-C++ source compiles and links into an executable.</p>
<dl>
<dt><code>check_objcxx_source_compiles</code></p>
<dd>
<pre>check_objcxx_source_compiles(&lt;code&gt; &lt;resultVar&gt;
 [FAIL_REGEX &lt;regex1&gt; [&lt;regex2&gt;...]])</pre>
<p>Check that the source supplied in <code>&lt;code&gt;</code> can be compiled as a Objective-C++ source file and linked as an executable (so it must contain at least a <code>main()</code> function). The result will be stored in the internal cache variable specified by <code>&lt;resultVar&gt;</code>, with a boolean true value for success and boolean false for failure. If <code>FAIL_REGEX</code> is provided, then failure is determined by checking if anything in the output matches any of the specified regular expressions. </p>
<p> The underlying check is performed by the <code>try_compile()</code> command. The compile and link commands can be influenced by setting any of the following variables prior to calling <code>check_objcxx_source_compiles()</code>:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>Additional flags to pass to the compiler. Note that the contents of <code>CMAKE_OBJCXX_FLAGS</code> and its associated configuration-specific variable are automatically added to the compiler command before the contents of <code>CMAKE_REQUIRED_FLAGS</code>.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>A ;-list of compiler definitions of the form <code>-DFOO</code> or <code>-DFOO=bar</code>. A definition for the name specified by <code>&lt;resultVar&gt;</code> will also be added automatically.</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>A ;-list of header search paths to pass to the compiler. These will be the only header search paths used by <code>try_compile()</code>, i.e. the contents of the <code>INCLUDE_DIRECTORIES</code> directory property will be ignored.</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>A ;-list of options to add to the link command (see <code>try_compile()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>A ;-list of libraries to add to the link command. These can be the name of system libraries or they can be Imported Targets (see <code>try_compile()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>If this variable evaluates to a boolean true value, all status messages associated with the check will be suppressed. </p>
<p> The check is only performed once, with the result cached in the variable named by <code>&lt;resultVar&gt;</code>. Every subsequent CMake run will re-use this cached value rather than performing the check again, even if the <code>&lt;code&gt;</code> changes. In order to force the check to be re-evaluated, the variable named by <code>&lt;resultVar&gt;</code> must be manually removed from the cache.</dl>
<h3>CheckOBJCXXSourceRuns</h3>
<p>New in version 3.16. </p>
<p> Check if given Objective-C++ source compiles and links into an executable and can subsequently be run.</p>
<dl>
<dt><code>check_objcxx_source_runs</code></p>
<dd>
<pre>check_objcxx_source_runs(&lt;code&gt; &lt;resultVar&gt;)</pre>
<p>Check that the source supplied in <code>&lt;code&gt;</code> can be compiled as a Objective-C++ source file, linked as an executable and then run. The <code>&lt;code&gt;</code> must contain at least a <code>main()</code> function. If the <code>&lt;code&gt;</code> could be built and run successfully, the internal cache variable specified by <code>&lt;resultVar&gt;</code> will be set to 1, otherwise it will be set to an value that evaluates to boolean false (e.g. an empty string or an error message). </p>
<p> The underlying check is performed by the <code>try_run()</code> command. The compile and link commands can be influenced by setting any of the following variables prior to calling <code>check_objcxx_source_runs()</code>:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>Additional flags to pass to the compiler. Note that the contents of <code>CMAKE_OBJCXX_FLAGS</code> and its associated configuration-specific variable are automatically added to the compiler command before the contents of <code>CMAKE_REQUIRED_FLAGS</code>.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>A ;-list of compiler definitions of the form <code>-DFOO</code> or <code>-DFOO=bar</code>. A definition for the name specified by <code>&lt;resultVar&gt;</code> will also be added automatically.</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>A ;-list of header search paths to pass to the compiler. These will be the only header search paths used by <code>try_run()</code>, i.e. the contents of the <code>INCLUDE_DIRECTORIES</code> directory property will be ignored.</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>A ;-list of options to add to the link command (see <code>try_run()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>A ;-list of libraries to add to the link command. These can be the name of system libraries or they can be Imported Targets (see <code>try_run()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>If this variable evaluates to a boolean true value, all status messages associated with the check will be suppressed. </p>
<p> The check is only performed once, with the result cached in the variable named by <code>&lt;resultVar&gt;</code>. Every subsequent CMake run will re-use this cached value rather than performing the check again, even if the <code>&lt;code&gt;</code> changes. In order to force the check to be re-evaluated, the variable named by <code>&lt;resultVar&gt;</code> must be manually removed from the cache.</dl>
<h3>CheckPIESupported</h3>
<p>New in version 3.14. </p>
<p> Check whether the linker supports Position Independent Code (PIE) or No Position Independent Code (NO_PIE) for executables. Use this to ensure that the <code>POSITION_INDEPENDENT_CODE</code> target property for executables will be honored at link time.</p>
<dl>
<dt><code>check_pie_supported</code></p>
<dd>
<pre>check_pie_supported([OUTPUT_VARIABLE &lt;output&gt;]
 [LANGUAGES &lt;lang&gt;...])</pre>
<p>Options are:</p>
<dt><code>OUTPUT_VARIABLE &lt;output&gt;</code></p>
<dd>Set <code>&lt;output&gt;</code> variable with details about any error.</p>
<dt><code>LANGUAGES &lt;lang&gt;&#8230;</code></p>
<dd>Check the linkers used for each of the specified languages. Supported languages are <code>C</code>, <code>CXX</code>, and <code>Fortran</code>. </p>
<p> It makes no sense to use this module when <code>CMP0083</code> is set to <code>OLD</code>, so the command will return an error in this case. See policy <code>CMP0083</code> for details.</dl>
<h3>Variables</h3>
<p>For each language checked, two boolean cache variables are defined.</p>
<dl>
<dt><code>CMAKE_&lt;lang&gt;_LINK_PIE_SUPPORTED</code></p>
<dd>Set to <code>YES</code> if <code>PIE</code> is supported by the linker and <code>NO</code> otherwise.</p>
<dt><code>CMAKE_&lt;lang&gt;_LINK_NO_PIE_SUPPORTED</code></p>
<dd>Set to <code>YES</code> if <code>NO_PIE</code> is supported by the linker and <code>NO</code> otherwise.</dl>
<h3>Examples</h3>
<pre>check_pie_supported()
set_property(TARGET foo PROPERTY POSITION_INDEPENDENT_CODE TRUE)</pre>
<pre># Retrieve any error message.
check_pie_supported(OUTPUT_VARIABLE output LANGUAGES C)
set_property(TARGET foo PROPERTY POSITION_INDEPENDENT_CODE TRUE)
if(NOT CMAKE_C_LINK_PIE_SUPPORTED)
 message(WARNING &quot;PIE is not supported at link time: ${output}.
&quot;
 &quot;PIE link options will not be passed to linker.&quot;)
endif()</pre>
<h3>CheckPrototypeDefinition</h3>
<p>Check if the prototype we expect is correct.</p>
<dl>
<dt><code>check_prototype_definition</code></p>
<dd>
<pre>check_prototype_definition(FUNCTION PROTOTYPE RETURN HEADER VARIABLE)</pre>
<pre>FUNCTION - The name of the function (used to check if prototype exists)
PROTOTYPE- The prototype to check.
RETURN - The return value of the function.
HEADER - The header files required.
VARIABLE - The variable to store the result.
 Will be created as an internal cache variable.</pre>
<p>Example: </p>
<pre>check_prototype_definition(getpwent_r
 &quot;struct passwd *getpwent_r(struct passwd *src, char *buf, int buflen)&quot;
 &quot;NULL&quot;
 &quot;unistd.h;pwd.h&quot;
 SOLARIS_GETPWENT_R)</pre>
<p>The following variables may be set before calling this function to modify the way the check is run:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>string of compile command line flags.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>list of macros to define (-DFOO=bar).</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>list of include directories.</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>New in version 3.14: list of options to pass to link command. </p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>list of libraries to link.</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>New in version 3.1: execute quietly without messages. </p>
</dl>
<h3>CheckSourceCompiles</h3>
<p>New in version 3.19. </p>
<p> Check if given source compiles and links into an executable.</p>
<dl>
<dt><code>check_source_compiles</code></p>
<dd>
<pre>check_source_compiles(&lt;lang&gt; &lt;code&gt; &lt;resultVar&gt;
 [FAIL_REGEX &lt;regex1&gt; [&lt;regex2&gt;...]]
 [SRC_EXT &lt;extension&gt;])</pre>
<p>Check that the source supplied in <code>&lt;code&gt;</code> can be compiled as a source file for the requested language and linked as an executable (so it must contain at least a <code>main()</code> function). The result will be stored in the internal cache variable specified by <code>&lt;resultVar&gt;</code>, with a boolean true value for success and boolean false for failure. If <code>FAIL_REGEX</code> is provided, then failure is determined by checking if anything in the output matches any of the specified regular expressions. </p>
<p> By default, the test source file will be given a file extension that matches the requested language. The <code>SRC_EXT</code> option can be used to override this with <code>.&lt;extension&gt;</code> instead. </p>
<p> The underlying check is performed by the <code>try_compile()</code> command. The compile and link commands can be influenced by setting any of the following variables prior to calling <code>check_source_compiles()</code>:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>Additional flags to pass to the compiler. Note that the contents of <code>CMAKE_&lt;LANG&gt;_FLAGS</code> and its associated configuration-specific variable are automatically added to the compiler command before the contents of <code>CMAKE_REQUIRED_FLAGS</code>.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>A ;-list of compiler definitions of the form <code>-DFOO</code> or <code>-DFOO=bar</code>. A definition for the name specified by <code>&lt;resultVar&gt;</code> will also be added automatically.</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>A ;-list of header search paths to pass to the compiler. These will be the only header search paths used by <code>try_compile()</code>, i.e. the contents of the <code>INCLUDE_DIRECTORIES</code> directory property will be ignored.</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>A ;-list of options to add to the link command (see <code>try_compile()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>A ;-list of libraries to add to the link command. These can be the name of system libraries or they can be Imported Targets (see <code>try_compile()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>If this variable evaluates to a boolean true value, all status messages associated with the check will be suppressed. </p>
<p> The check is only performed once, with the result cached in the variable named by <code>&lt;resultVar&gt;</code>. Every subsequent CMake run will re-use this cached value rather than performing the check again, even if the <code>&lt;code&gt;</code> changes. In order to force the check to be re-evaluated, the variable named by <code>&lt;resultVar&gt;</code> must be manually removed from the cache.</dl>
<h3>CheckSourceRuns</h3>
<p>New in version 3.19. </p>
<p> Check if given source compiles and links into an executable and can subsequently be run.</p>
<dl>
<dt><code>check_source_runs</code></p>
<dd>
<pre>check_source_runs(&lt;lang&gt; &lt;code&gt; &lt;resultVar&gt;
 [SRC_EXT &lt;extension&gt;])</pre>
<p>Check that the source supplied in <code>&lt;code&gt;</code> can be compiled as a source file for the requested language, linked as an executable and then run. The <code>&lt;code&gt;</code> must contain at least a <code>main()</code> function. If the <code>&lt;code&gt;</code> could be built and run successfully, the internal cache variable specified by <code>&lt;resultVar&gt;</code> will be set to 1, otherwise it will be set to an value that evaluates to boolean false (e.g. an empty string or an error message). </p>
<p> By default, the test source file will be given a file extension that matches the requested language. The <code>SRC_EXT</code> option can be used to override this with <code>.&lt;extension&gt;</code> instead. </p>
<p> The underlying check is performed by the <code>try_run()</code> command. The compile and link commands can be influenced by setting any of the following variables prior to calling <code>check_objc_source_runs()</code>:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>Additional flags to pass to the compiler. Note that the contents of <code>CMAKE_OBJC_FLAGS</code> and its associated configuration-specific variable are automatically added to the compiler command before the contents of <code>CMAKE_REQUIRED_FLAGS</code>.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>A ;-list of compiler definitions of the form <code>-DFOO</code> or <code>-DFOO=bar</code>. A definition for the name specified by <code>&lt;resultVar&gt;</code> will also be added automatically.</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>A ;-list of header search paths to pass to the compiler. These will be the only header search paths used by <code>try_run()</code>, i.e. the contents of the <code>INCLUDE_DIRECTORIES</code> directory property will be ignored.</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>A ;-list of options to add to the link command (see <code>try_run()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>A ;-list of libraries to add to the link command. These can be the name of system libraries or they can be Imported Targets (see <code>try_run()</code> for further details).</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>If this variable evaluates to a boolean true value, all status messages associated with the check will be suppressed. </p>
<p> The check is only performed once, with the result cached in the variable named by <code>&lt;resultVar&gt;</code>. Every subsequent CMake run will re-use this cached value rather than performing the check again, even if the <code>&lt;code&gt;</code> changes. In order to force the check to be re-evaluated, the variable named by <code>&lt;resultVar&gt;</code> must be manually removed from the cache.</dl>
<h3>CheckStructHasMember</h3>
<p>Check if the given struct or class has the specified member variable</p>
<dl>
<dt><code>CHECK_STRUCT_HAS_MEMBER</code></p>
<dd>
<pre>CHECK_STRUCT_HAS_MEMBER(&lt;struct&gt; &lt;member&gt; &lt;header&gt; &lt;variable&gt;
 [LANGUAGE &lt;language&gt;])</pre>
<pre>&lt;struct&gt; - the name of the struct or class you are interested in
&lt;member&gt; - the member which existence you want to check
&lt;header&gt; - the header(s) where the prototype should be declared
&lt;variable&gt; - variable to store the result
&lt;language&gt; - the compiler to use (C or CXX)</pre>
<p>The following variables may be set before calling this macro to modify the way the check is run:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>string of compile command line flags.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>list of macros to define (-DFOO=bar).</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>list of include directories.</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>New in version 3.14: list of options to pass to link command. </p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>list of libraries to link.</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>New in version 3.1: execute quietly without messages. </p>
<p> Example: </p>
<pre>CHECK_STRUCT_HAS_MEMBER(&quot;struct timeval&quot; tv_sec sys/select.h
 HAVE_TIMEVAL_TV_SEC LANGUAGE C)</pre>
</dl>
<h3>CheckSymbolExists</h3>
<p>Provides a macro to check if a symbol exists as a function, variable, or macro in <code>C</code>.</p>
<dl>
<dt><code>check_symbol_exists</code></p>
<dd>
<pre>check_symbol_exists(&lt;symbol&gt; &lt;files&gt; &lt;variable&gt;)</pre>
<p>Check that the <code>&lt;symbol&gt;</code> is available after including given header <code>&lt;files&gt;</code> and store the result in a <code>&lt;variable&gt;</code>. Specify the list of files in one argument as a semicolon-separated list. <code>&lt;variable&gt;</code> will be created as an internal cache variable. </p>
<p> If the header files define the symbol as a macro it is considered available and assumed to work. If the header files declare the symbol as a function or variable then the symbol must also be available for linking (so intrinsics may not be detected). If the symbol is a type, enum value, or intrinsic it will not be recognized (consider using <code>CheckTypeSize</code> or <code>CheckSourceCompiles</code>). If the check needs to be done in C++, consider using <code>CheckCXXSymbolExists</code> instead. </p>
<p> The following variables may be set before calling this macro to modify the way the check is run:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>string of compile command line flags.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>a ;-list of macros to define (-DFOO=bar).</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>a ;-list of header search paths to pass to the compiler.</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>New in version 3.14: a ;-list of options to add to the link command. </p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>a ;-list of libraries to add to the link command. See policy <code>CMP0075</code>.</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>New in version 3.1: execute quietly without messages. </p>
<p> For example: </p>
<pre>include(CheckSymbolExists)
# Check for macro SEEK_SET
check_symbol_exists(SEEK_SET &quot;stdio.h&quot; HAVE_SEEK_SET)
# Check for function fopen
check_symbol_exists(fopen &quot;stdio.h&quot; HAVE_FOPEN)</pre>
</dl>
<h3>CheckTypeSize</h3>
<p>Check sizeof a type</p>
<dl>
<dt><code>CHECK_TYPE_SIZE</code></p>
<dd>
<pre>CHECK_TYPE_SIZE(TYPE VARIABLE [BUILTIN_TYPES_ONLY]
 [LANGUAGE &lt;language&gt;])</pre>
<p>Check if the type exists and determine its size. On return, <code>HAVE_${VARIABLE}</code> holds the existence of the type, and <code>${VARIABLE}</code> holds one of the following: </p>
<pre>&lt;size&gt; = type has non-zero size &lt;size&gt;
&quot;0&quot; = type has arch-dependent size (see below)
&quot;&quot; = type does not exist</pre>
<p>Both <code>HAVE_${VARIABLE}</code> and <code>${VARIABLE}</code> will be created as internal cache variables. </p>
<p> Furthermore, the variable <code>${VARIABLE}_CODE</code> holds C preprocessor code to define the macro <code>${VARIABLE}</code> to the size of the type, or leave the macro undefined if the type does not exist. </p>
<p> The variable <code>${VARIABLE}</code> may be <code>0</code> when <code>CMAKE_OSX_ARCHITECTURES</code> has multiple architectures for building OS X universal binaries. This indicates that the type size varies across architectures. In this case <code>${VARIABLE}_CODE</code> contains C preprocessor tests mapping from each architecture macro to the corresponding type size. The list of architecture macros is stored in <code>${VARIABLE}_KEYS</code>, and the value for each key is stored in <code>${VARIABLE}-${KEY}</code>. </p>
<p> If the <code>BUILTIN_TYPES_ONLY</code> option is not given, the macro checks for headers <code>&lt;sys/types.h&gt;</code>, <code>&lt;stdint.h&gt;</code>, and <code>&lt;stddef.h&gt;</code>, and saves results in <code>HAVE_SYS_TYPES_H</code>, <code>HAVE_STDINT_H</code>, and <code>HAVE_STDDEF_H</code>. The type size check automatically includes the available headers, thus supporting checks of types defined in the headers. </p>
<p> If <code>LANGUAGE</code> is set, the specified compiler will be used to perform the check. Acceptable values are <code>C</code> and <code>CXX</code>. </p>
<p> Despite the name of the macro you may use it to check the size of more complex expressions, too. To check e.g. for the size of a struct member you can do something like this: </p>
<pre>check_type_size(&quot;((struct something*)0)-&gt;member&quot; SIZEOF_MEMBER)</pre>
<p>The following variables may be set before calling this macro to modify the way the check is run:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>string of compile command line flags.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>list of macros to define (-DFOO=bar).</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>list of include directories.</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>New in version 3.14: list of options to pass to link command. </p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>list of libraries to link.</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>New in version 3.1: execute quietly without messages. </p>
<dt><code>CMAKE_EXTRA_INCLUDE_FILES</code></p>
<dd>list of extra headers to include.</dl>
<h3>CheckVariableExists</h3>
<p>Check if the variable exists.</p>
<dl>
<dt><code>CHECK_VARIABLE_EXISTS</code></p>
<dd>
<pre>CHECK_VARIABLE_EXISTS(VAR VARIABLE)</pre>
<pre>VAR - the name of the variable
VARIABLE - variable to store the result
 Will be created as an internal cache variable.</pre>
<p>This macro is only for <code>C</code> variables. </p>
<p> The following variables may be set before calling this macro to modify the way the check is run:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>string of compile command line flags.</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>list of macros to define (-DFOO=bar).</p>
<dt><code>CMAKE_REQUIRED_LINK_OPTIONS</code></p>
<dd>New in version 3.14: list of options to pass to link command. </p>
<dt><code>CMAKE_REQUIRED_LIBRARIES</code></p>
<dd>list of libraries to link.</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>New in version 3.1: execute quietly without messages. </p>
</dl>
<h3>CMakeAddFortranSubdirectory</h3>
<p>Add a fortran-only subdirectory, find a fortran compiler, and build. </p>
<p> The <code>cmake_add_fortran_subdirectory</code> function adds a subdirectory to a project that contains a fortran-only subproject. The module will check the current compiler and see if it can support fortran. If no fortran compiler is found and the compiler is MSVC, then this module will find the MinGW gfortran. It will then use an external project to build with the MinGW tools. It will also create imported targets for the libraries created. This will only work if the fortran code is built into a dll, so <code>BUILD_SHARED_LIBS</code> is turned on in the project. In addition the <code>CMAKE_GNUtoMS</code> option is set to on, so that Microsoft <code>.lib</code> files are created. Usage is as follows: </p>
<pre>cmake_add_fortran_subdirectory(
 &lt;subdir&gt; # name of subdirectory
 PROJECT &lt;project_name&gt; # project name in subdir top CMakeLists.txt
 ARCHIVE_DIR &lt;dir&gt; # dir where project places .lib files
 RUNTIME_DIR &lt;dir&gt; # dir where project places .dll files
 LIBRARIES &lt;lib&gt;... # names of library targets to import
 LINK_LIBRARIES # link interface libraries for LIBRARIES
 [LINK_LIBS &lt;lib&gt; &lt;dep&gt;...]...
 CMAKE_COMMAND_LINE ... # extra command line flags to pass to cmake
 NO_EXTERNAL_INSTALL # skip installation of external project
 )</pre>
<p>Relative paths in <code>ARCHIVE_DIR</code> and <code>RUNTIME_DIR</code> are interpreted with respect to the build directory corresponding to the source directory in which the function is invoked. </p>
<p> Limitations: </p>
<p> <code>NO_EXTERNAL_INSTALL</code> is required for forward compatibility with a future version that supports installation of the external project binaries during <code>make install</code>.</p>
<h3>CMakeBackwardCompatibilityCXX</h3>
<p>define a bunch of backwards compatibility variables </p>
<pre>CMAKE_ANSI_CXXFLAGS - flag for ansi c++
CMAKE_HAS_ANSI_STRING_STREAM - has &lt;strstream&gt;
include(TestForANSIStreamHeaders)
include(CheckIncludeFileCXX)
include(TestForSTDNamespace)
include(TestForANSIForScope)</pre>
<h3>CMakeDependentOption</h3>
<p>Macro to provide an option dependent on other options. </p>
<p> This macro presents an option to the user only if a set of other conditions are true.</p>
<dl>
<dt><code>cmake_dependent_option</code></p>
<dd>
<pre>cmake_dependent_option(&lt;option&gt; &quot;&lt;help_text&gt;&quot; &lt;value&gt; &lt;depends&gt; &lt;force&gt;)</pre>
<p>Makes <code>&lt;option&gt;</code> available to the user if <code>&lt;depends&gt;</code> is true. When <code>&lt;option&gt;</code> is available, the given <code>&lt;help_text&gt;</code> and initial <code>&lt;value&gt;</code> are used. If the <code>&lt;depends&gt;</code> condition is not true, <code>&lt;option&gt;</code> will not be presented and will always have the value given by <code>&lt;force&gt;</code>. Any value set by the user is preserved for when the option is presented again. In case <code>&lt;depends&gt;</code> is a semicolon-separated list, all elements must be true in order to initialize <code>&lt;option&gt;</code> with <code>&lt;value&gt;</code>. </p>
<p> Example invocation: </p>
<pre>cmake_dependent_option(USE_FOO &quot;Use Foo&quot; ON &quot;USE_BAR;NOT USE_ZOT&quot; OFF)</pre>
<p>If <code>USE_BAR</code> is true and <code>USE_ZOT</code> is false, this provides an option called <code>USE_FOO</code> that defaults to ON. Otherwise, it sets <code>USE_FOO</code> to OFF and hides the option from the user. If the status of <code>USE_BAR</code> or <code>USE_ZOT</code> ever changes, any value for the <code>USE_FOO</code> option is saved so that when the option is re-enabled it retains its old value. </p>
<p> New in version 3.22: Full Condition Syntax is now supported. See policy <code>CMP0127</code>. </p>
</dl>
<h3>CMakeFindDependencyMacro</h3>
<dl>
<dt><code>find_dependency</code></p>
<dd>The <code>find_dependency()</code> macro wraps a <code>find_package()</code> call for a package dependency: </p>
<pre>find_dependency(&lt;dep&gt; [...])</pre>
<p>It is designed to be used in a Package Configuration File (<code>&lt;PackageName&gt;Config.cmake</code>). <code>find_dependency</code> forwards the correct parameters for <code>QUIET</code> and <code>REQUIRED</code> which were passed to the original <code>find_package()</code> call. Any additional arguments specified are forwarded to <code>find_package()</code>. </p>
<p> If the dependency could not be found it sets an informative diagnostic message and calls <code>return()</code> to end processing of the calling package configuration file and return to the <code>find_package()</code> command that loaded it. </p>
<p> <code>NOTE:</code> The call to <code>return()</code> makes this macro unsuitable to call from Find Modules.</dl>
<h3>CMakeFindFrameworks</h3>
<p>helper module to find OSX frameworks </p>
<p> This module reads hints about search locations from variables: </p>
<pre>CMAKE_FIND_FRAMEWORK_EXTRA_LOCATIONS - Extra directories</pre>
<h3>CMakeFindPackageMode</h3>
<p>This file is executed by cmake when invoked with &#8211;find-package. It expects that the following variables are set using -D:</p>
<dl>
<dt><code>NAME</code></p>
<dd>name of the package</p>
<dt><code>COMPILER_ID</code></p>
<dd>the CMake compiler ID for which the result is, i.e. GNU/Intel/Clang/MSVC, etc.</p>
<dt><code>LANGUAGE</code></p>
<dd>language for which the result will be used, i.e. C/CXX/Fortran/ASM</p>
<dt><code>MODE</code></p>
<dd>
<dt><code>EXIST</code></p>
<dd>only check for existence of the given package</p>
<dt><code>COMPILE</code></p>
<dd>print the flags needed for compiling an object file which uses the given package</p>
<dt><code>LINK</code></p>
<dd>print the flags needed for linking when using the given package</p>
<dt><code>QUIET</code></p>
<dd>if TRUE, don&#8217;t print anything</dl>
<h3>CMakeGraphVizOptions</h3>
<p>The builtin Graphviz support of CMake.</p>
<h3>Generating Graphviz files</h3>
<p>CMake can generate <i>Graphviz</i> files showing the dependencies between the targets in a project, as well as external libraries which are linked against. </p>
<p> When running CMake with the <code>&#8211;graphviz=foo.dot</code> option, it produces:</p>
<dl>
<dt>&bull;</p>
<dd>a <code>foo.dot</code> file, showing all dependencies in the project</p>
<dt>&bull;</p>
<dd>a <code>foo.dot.&lt;target&gt;</code> file for each target, showing on which other targets it depends</p>
<dt>&bull;</p>
<dd>a <code>foo.dot.&lt;target&gt;.dependers</code> file for each target, showing which other targets depend on it </p>
<p> Those .dot files can be converted to images using the <i>dot</i> command from the Graphviz package: </p>
<pre>dot -Tpng -o foo.png foo.dot</pre>
<p>New in version 3.10: The different dependency types <code>PUBLIC</code>, <code>INTERFACE</code> and <code>PRIVATE</code> are represented as solid, dashed and dotted edges. </p>
</dl>
<h3>Variables specific to the Graphviz support</h3>
<p>The resulting graphs can be huge. The look and content of the generated graphs can be controlled using the file <code>CMakeGraphVizOptions.cmake</code>. This file is first searched in <code>CMAKE_BINARY_DIR</code>, and then in <code>CMAKE_SOURCE_DIR</code>. If found, the variables set in it are used to adjust options for the generated Graphviz files.</p>
<dl>
<dt><code>GRAPHVIZ_GRAPH_NAME</code></p>
<dd>The graph name.</p>
<dt>&bull;</p>
<dd>Mandatory: NO</p>
<dt>&bull;</p>
<dd>Default: value of <code>CMAKE_PROJECT_NAME</code></p>
<dt><code>GRAPHVIZ_GRAPH_HEADER</code></p>
<dd>The header written at the top of the Graphviz files.</p>
<dt>&bull;</p>
<dd>Mandatory: NO</p>
<dt>&bull;</p>
<dd>Default: &quot;node [ fontsize = &quot;12&quot; ];&quot;</p>
<dt><code>GRAPHVIZ_NODE_PREFIX</code></p>
<dd>The prefix for each node in the Graphviz files.</p>
<dt>&bull;</p>
<dd>Mandatory: NO</p>
<dt>&bull;</p>
<dd>Default: &quot;node&quot;</p>
<dt><code>GRAPHVIZ_EXECUTABLES</code></p>
<dd>Set to FALSE to exclude executables from the generated graphs.</p>
<dt>&bull;</p>
<dd>Mandatory: NO</p>
<dt>&bull;</p>
<dd>Default: TRUE</p>
<dt><code>GRAPHVIZ_STATIC_LIBS</code></p>
<dd>Set to FALSE to exclude static libraries from the generated graphs.</p>
<dt>&bull;</p>
<dd>Mandatory: NO</p>
<dt>&bull;</p>
<dd>Default: TRUE</p>
<dt><code>GRAPHVIZ_SHARED_LIBS</code></p>
<dd>Set to FALSE to exclude shared libraries from the generated graphs.</p>
<dt>&bull;</p>
<dd>Mandatory: NO</p>
<dt>&bull;</p>
<dd>Default: TRUE</p>
<dt><code>GRAPHVIZ_MODULE_LIBS</code></p>
<dd>Set to FALSE to exclude module libraries from the generated graphs.</p>
<dt>&bull;</p>
<dd>Mandatory: NO</p>
<dt>&bull;</p>
<dd>Default: TRUE</p>
<dt><code>GRAPHVIZ_INTERFACE_LIBS</code></p>
<dd>Set to FALSE to exclude interface libraries from the generated graphs.</p>
<dt>&bull;</p>
<dd>Mandatory: NO</p>
<dt>&bull;</p>
<dd>Default: TRUE</p>
<dt><code>GRAPHVIZ_OBJECT_LIBS</code></p>
<dd>Set to FALSE to exclude object libraries from the generated graphs.</p>
<dt>&bull;</p>
<dd>Mandatory: NO</p>
<dt>&bull;</p>
<dd>Default: TRUE</p>
<dt><code>GRAPHVIZ_UNKNOWN_LIBS</code></p>
<dd>Set to FALSE to exclude unknown libraries from the generated graphs.</p>
<dt>&bull;</p>
<dd>Mandatory: NO</p>
<dt>&bull;</p>
<dd>Default: TRUE</p>
<dt><code>GRAPHVIZ_EXTERNAL_LIBS</code></p>
<dd>Set to FALSE to exclude external libraries from the generated graphs.</p>
<dt>&bull;</p>
<dd>Mandatory: NO</p>
<dt>&bull;</p>
<dd>Default: TRUE</p>
<dt><code>GRAPHVIZ_CUSTOM_TARGETS</code></p>
<dd>Set to TRUE to include custom targets in the generated graphs.</p>
<dt>&bull;</p>
<dd>Mandatory: NO</p>
<dt>&bull;</p>
<dd>Default: FALSE</p>
<dt><code>GRAPHVIZ_IGNORE_TARGETS</code></p>
<dd>A list of regular expressions for names of targets to exclude from the generated graphs.</p>
<dt>&bull;</p>
<dd>Mandatory: NO</p>
<dt>&bull;</p>
<dd>Default: empty</p>
<dt><code>GRAPHVIZ_GENERATE_PER_TARGET</code></p>
<dd>Set to FALSE to not generate per-target graphs <code>foo.dot.&lt;target&gt;</code>.</p>
<dt>&bull;</p>
<dd>Mandatory: NO</p>
<dt>&bull;</p>
<dd>Default: TRUE</p>
<dt><code>GRAPHVIZ_GENERATE_DEPENDERS</code></p>
<dd>Set to FALSE to not generate depender graphs <code>foo.dot.&lt;target&gt;.dependers</code>.</p>
<dt>&bull;</p>
<dd>Mandatory: NO</p>
<dt>&bull;</p>
<dd>Default: TRUE</dl>
<h3>CMakePackageConfigHelpers</h3>
<p>Helpers functions for creating config files that can be included by other projects to find and use a package. </p>
<p> Adds the <i>configure_package_config_file()</i> and <i>write_basic_package_version_file()</i> commands.</p>
<h3>Generating a Package Configuration File</h3>
<dl>
<dt><code>configure_package_config_file</code></p>
<dd>Create a config file for a project: </p>
<pre>configure_package_config_file(&lt;input&gt; &lt;output&gt;
 INSTALL_DESTINATION &lt;path&gt;
 [PATH_VARS &lt;var1&gt; &lt;var2&gt; ... &lt;varN&gt;]
 [NO_SET_AND_CHECK_MACRO]
 [NO_CHECK_REQUIRED_COMPONENTS_MACRO]
 [INSTALL_PREFIX &lt;path&gt;]
 )</pre>
<p><code>configure_package_config_file()</code> should be used instead of the plain <code>configure_file()</code> command when creating the <code>&lt;PackageName&gt;Config.cmake</code> or <code>&lt;PackageName&gt;-config.cmake</code> file for installing a project or library. It helps making the resulting package relocatable by avoiding hardcoded paths in the installed <code>Config.cmake</code> file. </p>
<p> In a <code>FooConfig.cmake</code> file there may be code like this to make the install destinations know to the using project: </p>
<pre>set(FOO_INCLUDE_DIR &quot;@CMAKE_INSTALL_FULL_INCLUDEDIR@&quot; )
set(FOO_DATA_DIR &quot;@CMAKE_INSTALL_PREFIX@/@RELATIVE_DATA_INSTALL_DIR@&quot; )
set(FOO_ICONS_DIR &quot;@CMAKE_INSTALL_PREFIX@/share/icons&quot; )
#...logic to determine installedPrefix from the own location...
set(FOO_CONFIG_DIR &quot;${installedPrefix}/@CONFIG_INSTALL_DIR@&quot; )</pre>
<p>All 4 options shown above are not sufficient, since the first 3 hardcode the absolute directory locations, and the 4th case works only if the logic to determine the <code>installedPrefix</code> is correct, and if <code>CONFIG_INSTALL_DIR</code> contains a relative path, which in general cannot be guaranteed. This has the effect that the resulting <code>FooConfig.cmake</code> file would work poorly under Windows and OSX, where users are used to choose the install location of a binary package at install time, independent from how <code>CMAKE_INSTALL_PREFIX</code> was set at build/cmake time. </p>
<p> Using <code>configure_package_config_file</code> helps. If used correctly, it makes the resulting <code>FooConfig.cmake</code> file relocatable. Usage:</p>
<dt>1.</p>
<dd>write a <code>FooConfig.cmake.in</code> file as you are used to</p>
<dt>2.</p>
<dd>insert a line containing only the string <code>@PACKAGE_INIT@</code></p>
<dt>3.</p>
<dd>instead of <code>set(FOO_DIR &quot;@SOME_INSTALL_DIR@&quot;)</code>, use <code>set(FOO_DIR &quot;@PACKAGE_SOME_INSTALL_DIR@&quot;)</code> (this must be after the <code>@PACKAGE_INIT@</code> line)</p>
<dt>4.</p>
<dd>instead of using the normal <code>configure_file()</code>, use <code>configure_package_config_file()</code> </p>
<p> The <code>&lt;input&gt;</code> and <code>&lt;output&gt;</code> arguments are the input and output file, the same way as in <code>configure_file()</code>. </p>
<p> The <code>&lt;path&gt;</code> given to <code>INSTALL_DESTINATION</code> must be the destination where the <code>FooConfig.cmake</code> file will be installed to. This path can either be absolute, or relative to the <code>INSTALL_PREFIX</code> path. </p>
<p> The variables <code>&lt;var1&gt;</code> to <code>&lt;varN&gt;</code> given as <code>PATH_VARS</code> are the variables which contain install destinations. For each of them the macro will create a helper variable <code>PACKAGE_&lt;var&#8230;&gt;</code>. These helper variables must be used in the <code>FooConfig.cmake.in</code> file for setting the installed location. They are calculated by <code>configure_package_config_file</code> so that they are always relative to the installed location of the package. This works both for relative and also for absolute locations. For absolute locations it works only if the absolute location is a subdirectory of <code>INSTALL_PREFIX</code>. </p>
<p> New in version 3.1: If the <code>INSTALL_PREFIX</code> argument is passed, this is used as base path to calculate all the relative paths. The <code>&lt;path&gt;</code> argument must be an absolute path. If this argument is not passed, the <code>CMAKE_INSTALL_PREFIX</code> variable will be used instead. The default value is good when generating a FooConfig.cmake file to use your package from the install tree. When generating a FooConfig.cmake file to use your package from the build tree this option should be used. </p>
<p> By default <code>configure_package_config_file</code> also generates two helper macros, <code>set_and_check()</code> and <code>check_required_components()</code> into the <code>FooConfig.cmake</code> file. </p>
<p> <code>set_and_check()</code> should be used instead of the normal <code>set()</code> command for setting directories and file locations. Additionally to setting the variable it also checks that the referenced file or directory actually exists and fails with a <code>FATAL_ERROR</code> otherwise. This makes sure that the created <code>FooConfig.cmake</code> file does not contain wrong references. When using the <code>NO_SET_AND_CHECK_MACRO</code>, this macro is not generated into the <code>FooConfig.cmake</code> file. </p>
<p> <code>check_required_components(&lt;PackageName&gt;)</code> should be called at the end of the <code>FooConfig.cmake</code> file. This macro checks whether all requested, non-optional components have been found, and if this is not the case, sets the <code>Foo_FOUND</code> variable to <code>FALSE</code>, so that the package is considered to be not found. It does that by testing the <code>Foo_&lt;Component&gt;_FOUND</code> variables for all requested required components. This macro should be called even if the package doesn&#8217;t provide any components to make sure users are not specifying components erroneously. When using the <code>NO_CHECK_REQUIRED_COMPONENTS_MACRO</code> option, this macro is not generated into the <code>FooConfig.cmake</code> file. </p>
<p> For an example see below the documentation for <i>write_basic_package_version_file()</i>.</dl>
<h3>Generating a Package Version File</h3>
<dl>
<dt><code>write_basic_package_version_file</code></p>
<dd>Create a version file for a project: </p>
<pre>write_basic_package_version_file(&lt;filename&gt;
 [VERSION &lt;major.minor.patch&gt;]
 COMPATIBILITY &lt;AnyNewerVersion|SameMajorVersion|SameMinorVersion|ExactVersion&gt;
 [ARCH_INDEPENDENT] )</pre>
<p>Writes a file for use as <code>&lt;PackageName&gt;ConfigVersion.cmake</code> file to <code>&lt;filename&gt;</code>. See the documentation of <code>find_package()</code> for details on this. </p>
<p> <code>&lt;filename&gt;</code> is the output filename, it should be in the build tree. <code>&lt;major.minor.patch&gt;</code> is the version number of the project to be installed. </p>
<p> If no <code>VERSION</code> is given, the <code>PROJECT_VERSION</code> variable is used. If this hasn&#8217;t been set, it errors out. </p>
<p> The <code>COMPATIBILITY</code> mode <code>AnyNewerVersion</code> means that the installed package version will be considered compatible if it is newer or exactly the same as the requested version. This mode should be used for packages which are fully backward compatible, also across major versions. If <code>SameMajorVersion</code> is used instead, then the behavior differs from <code>AnyNewerVersion</code> in that the major version number must be the same as requested, e.g. version 2.0 will not be considered compatible if 1.0 is requested. This mode should be used for packages which guarantee backward compatibility within the same major version. If <code>SameMinorVersion</code> is used, the behavior is the same as <code>SameMajorVersion</code>, but both major and minor version must be the same as requested, e.g version 0.2 will not be compatible if 0.1 is requested. If <code>ExactVersion</code> is used, then the package is only considered compatible if the requested version matches exactly its own version number (not considering the tweak version). For example, version 1.2.3 of a package is only considered compatible to requested version 1.2.3. This mode is for packages without compatibility guarantees. If your project has more elaborated version matching rules, you will need to write your own custom <code>ConfigVersion.cmake</code> file instead of using this macro. </p>
<p> New in version 3.11: The <code>SameMinorVersion</code> compatibility mode. </p>
<p> New in version 3.14: If <code>ARCH_INDEPENDENT</code> is given, the installed package version will be considered compatible even if it was built for a different architecture than the requested architecture. Otherwise, an architecture check will be performed, and the package will be considered compatible only if the architecture matches exactly. For example, if the package is built for a 32-bit architecture, the package is only considered compatible if it is used on a 32-bit architecture, unless <code>ARCH_INDEPENDENT</code> is given, in which case the package is considered compatible on any architecture. </p>
<p> <code>NOTE:</code> <code>ARCH_INDEPENDENT</code> is intended for header-only libraries or similar packages with no binaries. </p>
<p> New in version 3.19: <code>COMPATIBILITY_MODE</code> <code>AnyNewerVersion</code>, <code>SameMajorVersion</code> and <code>SameMinorVersion</code> handle the version range if any is specified (see <code>find_package()</code> command for the details). <code>ExactVersion</code> mode is incompatible with version ranges and will display an author warning if one is specified. </p>
<p> Internally, this macro executes <code>configure_file()</code> to create the resulting version file. Depending on the <code>COMPATIBILITY</code>, the corresponding <code>BasicConfigVersion-&lt;COMPATIBILITY&gt;.cmake.in</code> file is used. Please note that these files are internal to CMake and you should not call <code>configure_file()</code> on them yourself, but they can be used as starting point to create more sophisticted custom <code>ConfigVersion.cmake</code> files.</dl>
<h3>Example Generating Package Files</h3>
<p>Example using both <i>configure_package_config_file()</i> and <code>write_basic_package_version_file()</code>: </p>
<p> <code>CMakeLists.txt</code>: </p>
<pre>set(INCLUDE_INSTALL_DIR include/ ... CACHE )
set(LIB_INSTALL_DIR lib/ ... CACHE )
set(SYSCONFIG_INSTALL_DIR etc/foo/ ... CACHE )
#...
include(CMakePackageConfigHelpers)
configure_package_config_file(FooConfig.cmake.in
 ${CMAKE_CURRENT_BINARY_DIR}/FooConfig.cmake
 INSTALL_DESTINATION ${LIB_INSTALL_DIR}/Foo/cmake
 PATH_VARS INCLUDE_INSTALL_DIR SYSCONFIG_INSTALL_DIR)
write_basic_package_version_file(
 ${CMAKE_CURRENT_BINARY_DIR}/FooConfigVersion.cmake
 VERSION 1.2.3
 COMPATIBILITY SameMajorVersion )
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/FooConfig.cmake
 ${CMAKE_CURRENT_BINARY_DIR}/FooConfigVersion.cmake
 DESTINATION ${LIB_INSTALL_DIR}/Foo/cmake )</pre>
<p><code>FooConfig.cmake.in</code>: </p>
<pre>set(FOO_VERSION x.y.z)
...
@PACKAGE_INIT@
...
set_and_check(FOO_INCLUDE_DIR &quot;@PACKAGE_INCLUDE_INSTALL_DIR@&quot;)
set_and_check(FOO_SYSCONFIG_DIR &quot;@PACKAGE_SYSCONFIG_INSTALL_DIR@&quot;)
check_required_components(Foo)</pre>
<h3>CMakePrintHelpers</h3>
<p>Convenience functions for printing properties and variables, useful e.g. for debugging. </p>
<pre>cmake_print_properties([TARGETS target1 .. targetN]
 [SOURCES source1 .. sourceN]
 [DIRECTORIES dir1 .. dirN]
 [TESTS test1 .. testN]
 [CACHE_ENTRIES entry1 .. entryN]
 PROPERTIES prop1 .. propN )</pre>
<p>This function prints the values of the properties of the given targets, source files, directories, tests or cache entries. Exactly one of the scope keywords must be used. Example: </p>
<pre>cmake_print_properties(TARGETS foo bar PROPERTIES
 LOCATION INTERFACE_INCLUDE_DIRECTORIES)</pre>
<p>This will print the LOCATION and INTERFACE_INCLUDE_DIRECTORIES properties for both targets foo and bar. </p>
<pre>cmake_print_variables(var1 var2 .. varN)</pre>
<p>This function will print the name of each variable followed by its value. Example: </p>
<pre>cmake_print_variables(CMAKE_C_COMPILER CMAKE_MAJOR_VERSION DOES_NOT_EXIST)</pre>
<p>Gives: </p>
<pre>-- CMAKE_C_COMPILER=&quot;/usr/bin/gcc&quot; ; CMAKE_MAJOR_VERSION=&quot;2&quot; ; DOES_NOT_EXIST=&quot;&quot;</pre>
<h3>CMakePrintSystemInformation</h3>
<p>Print system information. </p>
<p> This module serves diagnostic purposes. Just include it in a project to see various internal CMake variables.</p>
<h3>CMakePushCheckState</h3>
<p>This module defines three macros: <code>CMAKE_PUSH_CHECK_STATE()</code> <code>CMAKE_POP_CHECK_STATE()</code> and <code>CMAKE_RESET_CHECK_STATE()</code> These macros can be used to save, restore and reset (i.e., clear contents) the state of the variables <code>CMAKE_REQUIRED_FLAGS</code>, <code>CMAKE_REQUIRED_DEFINITIONS</code>, <code>CMAKE_REQUIRED_LINK_OPTIONS</code>, <code>CMAKE_REQUIRED_LIBRARIES</code>, <code>CMAKE_REQUIRED_INCLUDES</code> and <code>CMAKE_EXTRA_INCLUDE_FILES</code> used by the various Check-files coming with CMake, like e.g. <code>check_function_exists()</code> etc. The variable contents are pushed on a stack, pushing multiple times is supported. This is useful e.g. when executing such tests in a Find-module, where they have to be set, but after the Find-module has been executed they should have the same value as they had before. </p>
<p> <code>CMAKE_PUSH_CHECK_STATE()</code> macro receives optional argument <code>RESET</code>. Whether it&#8217;s specified, <code>CMAKE_PUSH_CHECK_STATE()</code> will set all <code>CMAKE_REQUIRED_*</code> variables to empty values, same as <code>CMAKE_RESET_CHECK_STATE()</code> call will do. </p>
<p> Usage: </p>
<pre>cmake_push_check_state(RESET)
set(CMAKE_REQUIRED_DEFINITIONS -DSOME_MORE_DEF)
check_function_exists(...)
cmake_reset_check_state()
set(CMAKE_REQUIRED_DEFINITIONS -DANOTHER_DEF)
check_function_exists(...)
cmake_pop_check_state()</pre>
<h3>CMakeVerifyManifest</h3>
<p>CMakeVerifyManifest.cmake </p>
<p> This script is used to verify that embedded manifests and side by side manifests for a project match. To run this script, cd to a directory and run the script with cmake -P. On the command line you can pass in versions that are OK even if not found in the .manifest files. For example, cmake -Dallow_versions=8.0.50608.0 -PCmakeVerifyManifest.cmake could be used to allow an embedded manifest of 8.0.50608.0 to be used in a project even if that version was not found in the .manifest file.</p>
<h3>CPack</h3>
<p>Configure generators for binary installers and source packages.</p>
<h3>Introduction</h3>
<p>The CPack module generates the configuration files <code>CPackConfig.cmake</code> and <code>CPackSourceConfig.cmake</code>. They are intended for use in a subsequent run of the <code>cpack</code> program where they steer the generation of installers or/and source packages. </p>
<p> Depending on the CMake generator, the CPack module may also add two new build targets, <code>package</code> and <code>package_source</code>. See the <i>packaging targets</i> section below for details. </p>
<p> The generated binary installers will contain all files that have been installed via CMake&#8217;s <code>install()</code> command (and the deprecated commands <code>install_files()</code>, <code>install_programs()</code>, and <code>install_targets()</code>). Note that the <code>DESTINATION</code> option of the <code>install()</code> command must be a relative path; otherwise installed files are ignored by CPack. </p>
<p> Certain kinds of binary installers can be configured such that users can select individual application components to install. See the <code>CPackComponent</code> module for further details. </p>
<p> Source packages (configured through <code>CPackSourceConfig.cmake</code> and generated by the <code>CPack Archive Generator</code>) will contain all source files in the project directory except those specified in <i>CPACK_SOURCE_IGNORE_FILES</i>.</p>
<h3>CPack Generators</h3>
<p>The <i>CPACK_GENERATOR</i> variable has different meanings in different contexts. In a <code>CMakeLists.txt</code> file, <i>CPACK_GENERATOR</i> is a <i>list of generators</i>: and when <code>cpack</code> is run with no other arguments, it will iterate over that list and produce one package for each generator. In a <i>CPACK_PROJECT_CONFIG_FILE</i>, <i>CPACK_GENERATOR</i> is a <i>string naming a single generator</i>. If you need per-cpack-generator logic to control <i>other</i> cpack settings, then you need a <i>CPACK_PROJECT_CONFIG_FILE</i>. If set, the <i>CPACK_PROJECT_CONFIG_FILE</i> is included automatically on a per-generator basis. It only need contain overrides. </p>
<p> Here&#8217;s how it works:</p>
<dl>
<dt>&bull;</p>
<dd><code>cpack</code> runs</p>
<dt>&bull;</p>
<dd>it includes <code>CPackConfig.cmake</code></p>
<dt>&bull;</p>
<dd>it iterates over the generators given by the <code>-G</code> command line option, or if no such option was specified, over the list of generators given by the <i>CPACK_GENERATOR</i> variable set in the <code>CPackConfig.cmake</code> input file.</p>
<dt>&bull;</p>
<dd>foreach generator, it then</p>
<dt>&bull;</p>
<dd>sets <i>CPACK_GENERATOR</i> to the one currently being iterated</p>
<dt>&bull;</p>
<dd>includes the <i>CPACK_PROJECT_CONFIG_FILE</i></p>
<dt>&bull;</p>
<dd>produces the package for that generator </p>
<p> This is the key: For each generator listed in <i>CPACK_GENERATOR</i> in <code>CPackConfig.cmake</code>, cpack will <i>reset</i> <i>CPACK_GENERATOR</i> internally to <i>the one currently being used</i> and then include the <i>CPACK_PROJECT_CONFIG_FILE</i>. </p>
<p> For a list of available generators, see <code><a href="/docs/linux/man/7-cpack-generators/">cpack-generators</a>(7)</code>.</dl>
<h3>Targets package and package_source</h3>
<p>If CMake is run with the Makefile, Ninja, or Xcode generator, then <code>include(CPack)</code> generates a target <code>package</code>. This makes it possible to build a binary installer from CMake, Make, or Ninja: Instead of <code>cpack</code>, one may call <code>cmake &#8211;build . &#8211;target package</code> or <code>make package</code> or <code>ninja package</code>. The VS generator creates an uppercase target <code>PACKAGE</code>. </p>
<p> If CMake is run with the Makefile or Ninja generator, then <code>include(CPack)</code> also generates a target <code>package_source</code>. To build a source package, instead of <code>cpack -G TGZ &#8211;config CPackSourceConfig.cmake</code> one may call <code>cmake &#8211;build . &#8211;target package_source</code>, <code>make package_source</code>, or <code>ninja package_source</code>.</p>
<h3>Variables common to all CPack Generators</h3>
<p>Before including this CPack module in your <code>CMakeLists.txt</code> file, there are a variety of variables that can be set to customize the resulting installers. The most commonly-used variables are:</p>
<dl>
<dt><code>CPACK_PACKAGE_NAME</code></p>
<dd>The name of the package (or application). If not specified, it defaults to the project name.</p>
<dt><code>CPACK_PACKAGE_VENDOR</code></p>
<dd>The name of the package vendor. (e.g., &quot;Kitware&quot;). The default is &quot;Humanity&quot;.</p>
<dt><code>CPACK_PACKAGE_DIRECTORY</code></p>
<dd>The directory in which CPack is doing its packaging. If it is not set then this will default (internally) to the build dir. This variable may be defined in a CPack config file or from the <code>cpack</code> command line option <code>-B</code>. If set, the command line option overrides the value found in the config file.</p>
<dt><code>CPACK_PACKAGE_VERSION_MAJOR</code></p>
<dd>Package major version. This variable will always be set, but its default value depends on whether or not version details were given to the <code>project()</code> command in the top level CMakeLists.txt file. If version details were given, the default value will be <code>CMAKE_PROJECT_VERSION_MAJOR</code>. If no version details were given, a default version of 0.1.1 will be assumed, leading to <code>CPACK_PACKAGE_VERSION_MAJOR</code> having a default value of 0.</p>
<dt><code>CPACK_PACKAGE_VERSION_MINOR</code></p>
<dd>Package minor version. The default value is determined based on whether or not version details were given to the <code>project()</code> command in the top level CMakeLists.txt file. If version details were given, the default value will be <code>CMAKE_PROJECT_VERSION_MINOR</code>, but if no minor version component was specified then <code>CPACK_PACKAGE_VERSION_MINOR</code> will be left unset. If no project version was given at all, a default version of 0.1.1 will be assumed, leading to <code>CPACK_PACKAGE_VERSION_MINOR</code> having a default value of 1.</p>
<dt><code>CPACK_PACKAGE_VERSION_PATCH</code></p>
<dd>Package patch version. The default value is determined based on whether or not version details were given to the <code>project()</code> command in the top level CMakeLists.txt file. If version details were given, the default value will be <code>CMAKE_PROJECT_VERSION_PATCH</code>, but if no patch version component was specified then <code>CPACK_PACKAGE_VERSION_PATCH</code> will be left unset. If no project version was given at all, a default version of 0.1.1 will be assumed, leading to <code>CPACK_PACKAGE_VERSION_PATCH</code> having a default value of 1.</p>
<dt><code>CPACK_PACKAGE_DESCRIPTION</code></p>
<dd>A description of the project, used in places such as the introduction screen of CPack-generated Windows installers. If not set, the value of this variable is populated from the file named by <i>CPACK_PACKAGE_DESCRIPTION_FILE</i>.</p>
<dt><code>CPACK_PACKAGE_DESCRIPTION_FILE</code></p>
<dd>A text file used to describe the project when <i>CPACK_PACKAGE_DESCRIPTION</i> is not explicitly set. The default value for <code>CPACK_PACKAGE_DESCRIPTION_FILE</code> points to a built-in template file <code>Templates/CPack.GenericDescription.txt</code>.</p>
<dt><code>CPACK_PACKAGE_DESCRIPTION_SUMMARY</code></p>
<dd>Short description of the project (only a few words). If the <code>CMAKE_PROJECT_DESCRIPTION</code> variable is set, it is used as the default value, otherwise the default will be a string generated by CMake based on <code>CMAKE_PROJECT_NAME</code>.</p>
<dt><code>CPACK_PACKAGE_HOMEPAGE_URL</code></p>
<dd>Project homepage URL. The default value is taken from the <code>CMAKE_PROJECT_HOMEPAGE_URL</code> variable, which is set by the top level <code>project()</code> command, or else the default will be empty if no URL was provided to <code>project()</code>.</p>
<dt><code>CPACK_PACKAGE_FILE_NAME</code></p>
<dd>The name of the package file to generate, not including the extension. For example, <code>cmake-2.6.1-Linux-i686</code>. The default value is: </p>
<pre>${CPACK_PACKAGE_NAME}-${CPACK_PACKAGE_VERSION}-${CPACK_SYSTEM_NAME}</pre>
<dt><code>CPACK_PACKAGE_INSTALL_DIRECTORY</code></p>
<dd>Installation directory on the target system. This may be used by some CPack generators like NSIS to create an installation directory e.g., &quot;CMake 2.5&quot; below the installation prefix. All installed elements will be put inside this directory.</p>
<dt><code>CPACK_PACKAGE_ICON</code></p>
<dd>A branding image that will be displayed inside the installer (used by GUI installers).</p>
<dt><code>CPACK_PACKAGE_CHECKSUM</code></p>
<dd>New in version 3.7. </p>
<p> An algorithm that will be used to generate an additional file with the checksum of the package. The output file name will be: </p>
<pre>${CPACK_PACKAGE_FILE_NAME}.${CPACK_PACKAGE_CHECKSUM}</pre>
<p>Supported algorithms are those listed by the string(&lt;HASH&gt;) command.</p>
<dt><code>CPACK_PROJECT_CONFIG_FILE</code></p>
<dd>CPack-time project CPack configuration file. This file is included at cpack time, once per generator after CPack has set <i>CPACK_GENERATOR</i> to the actual generator being used. It allows per-generator setting of <code>CPACK_*</code> variables at cpack time.</p>
<dt><code>CPACK_RESOURCE_FILE_LICENSE</code></p>
<dd>License to be embedded in the installer. It will typically be displayed to the user by the produced installer (often with an explicit &quot;Accept&quot; button, for graphical installers) prior to installation. This license file is NOT added to the installed files but is used by some CPack generators like NSIS. If you want to install a license file (may be the same as this one) along with your project, you must add an appropriate CMake <code>install()</code> command in your <code>CMakeLists.txt</code>.</p>
<dt><code>CPACK_RESOURCE_FILE_README</code></p>
<dd>ReadMe file to be embedded in the installer. It typically describes in some detail the purpose of the project during the installation. Not all CPack generators use this file.</p>
<dt><code>CPACK_RESOURCE_FILE_WELCOME</code></p>
<dd>Welcome file to be embedded in the installer. It welcomes users to this installer. Typically used in the graphical installers on Windows and Mac OS X.</p>
<dt><code>CPACK_MONOLITHIC_INSTALL</code></p>
<dd>Disables the component-based installation mechanism. When set, the component specification is ignored and all installed items are put in a single &quot;MONOLITHIC&quot; package. Some CPack generators do monolithic packaging by default and may be asked to do component packaging by setting <code>CPACK_&lt;GENNAME&gt;_COMPONENT_INSTALL</code> to <code>TRUE</code>.</p>
<dt><code>CPACK_GENERATOR</code></p>
<dd>List of CPack generators to use. If not specified, CPack will create a set of options following the naming pattern <i>CPACK_BINARY_&lt;GENNAME&gt;</i> (e.g. <code>CPACK_BINARY_NSIS</code>) allowing the user to enable/disable individual generators. If the <code>-G</code> option is given on the <code>cpack</code> command line, it will override this variable and any <code>CPACK_BINARY_&lt;GENNAME&gt;</code> options.</p>
<dt><code>CPACK_OUTPUT_CONFIG_FILE</code></p>
<dd>The name of the CPack binary configuration file. This file is the CPack configuration generated by the CPack module for binary installers. Defaults to <code>CPackConfig.cmake</code>.</p>
<dt><code>CPACK_PACKAGE_EXECUTABLES</code></p>
<dd>Lists each of the executables and associated text label to be used to create Start Menu shortcuts. For example, setting this to the list <code>ccmake;CMake</code> will create a shortcut named &quot;CMake&quot; that will execute the installed executable <code>ccmake</code>. Not all CPack generators use it (at least NSIS, WIX and OSXX11 do).</p>
<dt><code>CPACK_STRIP_FILES</code></p>
<dd>List of files to be stripped. Starting with CMake 2.6.0, <code>CPACK_STRIP_FILES</code> will be a boolean variable which enables stripping of all files (a list of files evaluates to <code>TRUE</code> in CMake, so this change is compatible).</p>
<dt><code>CPACK_VERBATIM_VARIABLES</code></p>
<dd>New in version 3.4. </p>
<p> If set to <code>TRUE</code>, values of variables prefixed with <code>CPACK_</code> will be escaped before being written to the configuration files, so that the cpack program receives them exactly as they were specified. If not, characters like quotes and backslashes can cause parsing errors or alter the value received by the cpack program. Defaults to <code>FALSE</code> for backwards compatibility.</p>
<dt><code>CPACK_THREADS</code></p>
<dd>New in version 3.20. </p>
<p> Number of threads to use when performing parallelized operations, such as compressing the installer package. </p>
<p> Some compression methods used by CPack generators such as Debian or Archive may take advantage of multiple CPU cores to speed up compression. <code>CPACK_THREADS</code> can be set to specify how many threads will be used for compression. </p>
<p> A positive integer can be used to specify an exact desired thread count. </p>
<p> When given a negative integer CPack will use the absolute value as the upper limit but may choose a lower value based on the available hardware concurrency. </p>
<p> Given 0 CPack will try to use all available CPU cores. </p>
<p> By default <code>CPACK_THREADS</code> is set to <code>1</code>. </p>
<p> Currently only <code>xz</code> compression <i>may</i> take advantage of multiple cores. Other compression methods ignore this value and use only one thread. </p>
<p> New in version 3.21: Official CMake binaries available on <code>cmake.org</code> now ship with a <code>liblzma</code> that supports parallel compression. Older versions did not. </p>
</dl>
<h3>Variables for Source Package Generators</h3>
<p>The following CPack variables are specific to source packages, and will not affect binary packages:</p>
<dl>
<dt><code>CPACK_SOURCE_PACKAGE_FILE_NAME</code></p>
<dd>The name of the source package. For example <code>cmake-2.6.1</code>.</p>
<dt><code>CPACK_SOURCE_STRIP_FILES</code></p>
<dd>List of files in the source tree that will be stripped. Starting with CMake 2.6.0, <code>CPACK_SOURCE_STRIP_FILES</code> will be a boolean variable which enables stripping of all files (a list of files evaluates to <code>TRUE</code> in CMake, so this change is compatible).</p>
<dt><code>CPACK_SOURCE_GENERATOR</code></p>
<dd>List of generators used for the source packages. As with <i>CPACK_GENERATOR</i>, if this is not specified then CPack will create a set of options (e.g. <code>CPACK_SOURCE_ZIP</code>) allowing users to select which packages will be generated.</p>
<dt><code>CPACK_SOURCE_OUTPUT_CONFIG_FILE</code></p>
<dd>The name of the CPack source configuration file. This file is the CPack configuration generated by the CPack module for source installers. Defaults to <code>CPackSourceConfig.cmake</code>.</p>
<dt><code>CPACK_SOURCE_IGNORE_FILES</code></p>
<dd>Pattern of files in the source tree that won&#8217;t be packaged when building a source package. This is a list of regular expression patterns (that must be properly escaped), e.g., <code>/CVS/;/\.svn/;\.swp$;\.#;/#;.*~;cscope.*</code></dl>
<h3>Variables for Advanced Use</h3>
<p>The following variables are for advanced uses of CPack:</p>
<dl>
<dt><code>CPACK_CMAKE_GENERATOR</code></p>
<dd>What CMake generator should be used if the project is a CMake project. Defaults to the value of <code>CMAKE_GENERATOR</code>. Few users will want to change this setting.</p>
<dt><code>CPACK_INSTALL_CMAKE_PROJECTS</code></p>
<dd>List of four values that specify what project to install. The four values are: Build directory, Project Name, Project Component, Directory. If omitted, CPack will build an installer that installs everything.</p>
<dt><code>CPACK_SYSTEM_NAME</code></p>
<dd>System name, defaults to the value of <code>CMAKE_SYSTEM_NAME</code>, except on Windows where it will be <code>win32</code> or <code>win64</code>.</p>
<dt><code>CPACK_PACKAGE_VERSION</code></p>
<dd>Package full version, used internally. By default, this is built from <i>CPACK_PACKAGE_VERSION_MAJOR</i>, <i>CPACK_PACKAGE_VERSION_MINOR</i>, and <i>CPACK_PACKAGE_VERSION_PATCH</i>.</p>
<dt><code>CPACK_TOPLEVEL_TAG</code></p>
<dd>Directory for the installed files.</p>
<dt><code>CPACK_INSTALL_COMMANDS</code></p>
<dd>Extra commands to install components. The environment variable <code>CMAKE_INSTALL_PREFIX</code> is set to the temporary install directory during execution.</p>
<dt><code>CPACK_INSTALL_SCRIPTS</code></p>
<dd>New in version 3.16. </p>
<p> Extra CMake scripts executed by CPack during its local staging installation. They are executed before installing the files to be packaged. The scripts are not called by a standalone install (e.g.: <code>make install</code>). For every script, the following variables will be set: <code>CMAKE_CURRENT_SOURCE_DIR</code>, <code>CMAKE_CURRENT_BINARY_DIR</code> and <code>CMAKE_INSTALL_PREFIX</code> (which is set to the staging install directory). The singular form <code>CMAKE_INSTALL_SCRIPT</code> is supported as an alternative variable for historical reasons, but its value is ignored if <code>CMAKE_INSTALL_SCRIPTS</code> is set and a warning will be issued. </p>
<p> See also <i>CPACK_PRE_BUILD_SCRIPTS</i> and <i>CPACK_POST_BUILD_SCRIPTS</i> which can be used to specify scripts to be executed later in the packaging process.</p>
<dt><code>CPACK_PRE_BUILD_SCRIPTS</code></p>
<dd>New in version 3.19. </p>
<p> List of CMake scripts to execute after CPack has installed the files to be packaged into a staging directory and before producing the package(s) from those files. See also <i>CPACK_INSTALL_SCRIPTS</i> and <i>CPACK_POST_BUILD_SCRIPTS</i>.</p>
<dt><code>CPACK_POST_BUILD_SCRIPTS</code></p>
<dd>New in version 3.19. </p>
<p> List of CMake scripts to execute after CPack has produced the resultant packages and before copying them back to the build directory. See also <i>CPACK_INSTALL_SCRIPTS</i>, <i>CPACK_PRE_BUILD_SCRIPTS</i> and <i>CPACK_PACKAGE_FILES</i>.</p>
<dt><code>CPACK_PACKAGE_FILES</code></p>
<dd>New in version 3.19. </p>
<p> List of package files created in the staging directory, with each file provided as a full absolute path. This variable is populated by CPack just before invoking the post-build scripts listed in <i>CPACK_POST_BUILD_SCRIPTS</i>. It is the preferred way for the post-build scripts to know the set of package files to operate on. Projects should not try to set this variable themselves.</p>
<dt><code>CPACK_INSTALLED_DIRECTORIES</code></p>
<dd>Extra directories to install.</p>
<dt><code>CPACK_PACKAGE_INSTALL_REGISTRY_KEY</code></p>
<dd>Registry key used when installing this project. This is only used by installers for Windows. The default value is based on the installation directory.</p>
<dt><code>CPACK_CREATE_DESKTOP_LINKS</code></p>
<dd>List of desktop links to create. Each desktop link requires a corresponding start menu shortcut as created by <i>CPACK_PACKAGE_EXECUTABLES</i>.</p>
<dt><code>CPACK_BINARY_&lt;GENNAME&gt;</code></p>
<dd>CPack generated options for binary generators. The <code>CPack.cmake</code> module generates (when <i>CPACK_GENERATOR</i> is not set) a set of CMake options (see CMake <code>option()</code> command) which may then be used to select the CPack generator(s) to be used when building the <code>package</code> target or when running <code>cpack</code> without the <code>-G</code> option.</dl>
<h3>CPackComponent</h3>
<p>Configure components for binary installers and source packages.</p>
<h3>Introduction</h3>
<p>This module is automatically included by <code>CPack</code>. </p>
<p> Certain binary installers (especially the graphical installers) generated by CPack allow users to select individual application <i>components</i> to install. This module allows developers to configure the packaging of such components. </p>
<p> Contents is assigned to components by the <code>COMPONENT</code> argument of CMake&#8217;s <code>install()</code> command. Components can be annotated with user-friendly names and descriptions, inter-component dependencies, etc., and grouped in various ways to customize the resulting installer, using the commands described below. </p>
<p> To specify different groupings for different CPack generators use a CPACK_PROJECT_CONFIG_FILE.</p>
<h3>Variables</h3>
<p>The following variables influence the component-specific packaging:</p>
<dl>
<dt><code>CPACK_COMPONENTS_ALL</code></p>
<dd>The list of component to install. </p>
<p> The default value of this variable is computed by CPack and contains all components defined by the project. The user may set it to only include the specified components. </p>
<p> Instead of specifying all the desired components, it is possible to obtain a list of all defined components and then remove the unwanted ones from the list. The <code>get_cmake_property()</code> command can be used to obtain the <code>COMPONENTS</code> property, then the <code>list(REMOVE_ITEM)</code> command can be used to remove the unwanted ones. For example, to use all defined components except <code>foo</code> and <code>bar</code>: </p>
<pre>get_cmake_property(CPACK_COMPONENTS_ALL COMPONENTS)
list(REMOVE_ITEM CPACK_COMPONENTS_ALL &quot;foo&quot; &quot;bar&quot;)</pre>
<dt><code>CPACK_&lt;GENNAME&gt;_COMPONENT_INSTALL</code></p>
<dd>Enable/Disable component install for CPack generator &lt;GENNAME&gt;. </p>
<p> Each CPack Generator (RPM, DEB, ARCHIVE, NSIS, DMG, etc&#8230;) has a legacy default behavior. e.g. RPM builds monolithic whereas NSIS builds component. One can change the default behavior by setting this variable to 0/1 or OFF/ON.</p>
<dt><code>CPACK_COMPONENTS_GROUPING</code></p>
<dd>Specify how components are grouped for multi-package component-aware CPack generators. </p>
<p> Some generators like RPM or ARCHIVE (TGZ, ZIP, &#8230;) may generate several packages files when there are components, depending on the value of this variable:</p>
<dt>&bull;</p>
<dd>ONE_PER_GROUP (default): create one package per component group</p>
<dt>&bull;</p>
<dd>IGNORE : create one package per component (ignore the groups)</p>
<dt>&bull;</p>
<dd>ALL_COMPONENTS_IN_ONE : create a single package with all requested components</p>
<dt><code>CPACK_COMPONENT_&lt;compName&gt;_DISPLAY_NAME</code></p>
<dd>The name to be displayed for a component.</p>
<dt><code>CPACK_COMPONENT_&lt;compName&gt;_DESCRIPTION</code></p>
<dd>The description of a component.</p>
<dt><code>CPACK_COMPONENT_&lt;compName&gt;_GROUP</code></p>
<dd>The group of a component.</p>
<dt><code>CPACK_COMPONENT_&lt;compName&gt;_DEPENDS</code></p>
<dd>The dependencies (list of components) on which this component depends.</p>
<dt><code>CPACK_COMPONENT_&lt;compName&gt;_HIDDEN</code></p>
<dd>True if this component is hidden from the user.</p>
<dt><code>CPACK_COMPONENT_&lt;compName&gt;_REQUIRED</code></p>
<dd>True if this component is required.</p>
<dt><code>CPACK_COMPONENT_&lt;compName&gt;_DISABLED</code></p>
<dd>True if this component is not selected to be installed by default.</dl>
<h3>Commands</h3>
<h3>Add component</h3>
<dl>
<dt><code>cpack_add_component</code></p>
<dd>Describe an installation component. </p>
<pre>cpack_add_component(compname
 [DISPLAY_NAME name]
 [DESCRIPTION description]
 [HIDDEN | REQUIRED | DISABLED ]
 [GROUP group]
 [DEPENDS comp1 comp2 ... ]
 [INSTALL_TYPES type1 type2 ... ]
 [DOWNLOADED]
 [ARCHIVE_FILE filename]
 [PLIST filename])</pre>
<p><code>compname</code> is the name of an installation component, as defined by the <code>COMPONENT</code> argument of one or more CMake <code>install()</code> commands. With the <code>cpack_add_component</code> command one can set a name, a description, and other attributes of an installation component. One can also assign a component to a component group. </p>
<p> DISPLAY_NAME is the displayed name of the component, used in graphical installers to display the component name. This value can be any string. </p>
<p> DESCRIPTION is an extended description of the component, used in graphical installers to give the user additional information about the component. Descriptions can span multiple lines using <code>
</code> as the line separator. Typically, these descriptions should be no more than a few lines long. </p>
<p> HIDDEN indicates that this component will be hidden in the graphical installer, so that the user cannot directly change whether it is installed or not. </p>
<p> REQUIRED indicates that this component is required, and therefore will always be installed. It will be visible in the graphical installer, but it cannot be unselected. (Typically, required components are shown greyed out). </p>
<p> DISABLED indicates that this component should be disabled (unselected) by default. The user is free to select this component for installation, unless it is also HIDDEN. </p>
<p> DEPENDS lists the components on which this component depends. If this component is selected, then each of the components listed must also be selected. The dependency information is encoded within the installer itself, so that users cannot install inconsistent sets of components. </p>
<p> GROUP names the component group of which this component is a part. If not provided, the component will be a standalone component, not part of any component group. Component groups are described with the cpack_add_component_group command, detailed below. </p>
<p> INSTALL_TYPES lists the installation types of which this component is a part. When one of these installations types is selected, this component will automatically be selected. Installation types are described with the cpack_add_install_type command, detailed below. </p>
<p> DOWNLOADED indicates that this component should be downloaded on-the-fly by the installer, rather than packaged in with the installer itself. For more information, see the cpack_configure_downloads command. </p>
<p> ARCHIVE_FILE provides a name for the archive file created by CPack to be used for downloaded components. If not supplied, CPack will create a file with some name based on CPACK_PACKAGE_FILE_NAME and the name of the component. See cpack_configure_downloads for more information. </p>
<p> PLIST gives a filename that is passed to pkgbuild with the <code>&#8211;component-plist</code> argument when using the productbuild generator.</dl>
<h3>Add component group</h3>
<dl>
<dt><code>cpack_add_component_group</code></p>
<dd>Describes a group of related CPack installation components. </p>
<pre>cpack_add_component_group(groupname
 [DISPLAY_NAME name]
 [DESCRIPTION description]
 [PARENT_GROUP parent]
 [EXPANDED]
 [BOLD_TITLE])</pre>
<p>The cpack_add_component_group describes a group of installation components, which will be placed together within the listing of options. Typically, component groups allow the user to select/deselect all of the components within a single group via a single group-level option. Use component groups to reduce the complexity of installers with many options. groupname is an arbitrary name used to identify the group in the GROUP argument of the cpack_add_component command, which is used to place a component in a group. The name of the group must not conflict with the name of any component. </p>
<p> DISPLAY_NAME is the displayed name of the component group, used in graphical installers to display the component group name. This value can be any string. </p>
<p> DESCRIPTION is an extended description of the component group, used in graphical installers to give the user additional information about the components within that group. Descriptions can span multiple lines using <code>
</code> as the line separator. Typically, these descriptions should be no more than a few lines long. </p>
<p> PARENT_GROUP, if supplied, names the parent group of this group. Parent groups are used to establish a hierarchy of groups, providing an arbitrary hierarchy of groups. </p>
<p> EXPANDED indicates that, by default, the group should show up as &quot;expanded&quot;, so that the user immediately sees all of the components within the group. Otherwise, the group will initially show up as a single entry. </p>
<p> BOLD_TITLE indicates that the group title should appear in bold, to call the user&#8217;s attention to the group.</dl>
<h3>Add installation type</h3>
<dl>
<dt><code>cpack_add_install_type</code></p>
<dd>Add a new installation type containing a set of predefined component selections to the graphical installer. </p>
<pre>cpack_add_install_type(typename
 [DISPLAY_NAME name])</pre>
<p>The cpack_add_install_type command identifies a set of preselected components that represents a common use case for an application. For example, a &quot;Developer&quot; install type might include an application along with its header and library files, while an &quot;End user&quot; install type might just include the application&#8217;s executable. Each component identifies itself with one or more install types via the INSTALL_TYPES argument to cpack_add_component. </p>
<p> DISPLAY_NAME is the displayed name of the install type, which will typically show up in a drop-down box within a graphical installer. This value can be any string.</dl>
<h3>Configure downloads</h3>
<dl>
<dt><code>cpack_configure_downloads</code></p>
<dd>Configure CPack to download selected components on-the-fly as part of the installation process. </p>
<pre>cpack_configure_downloads(site
 [UPLOAD_DIRECTORY dirname]
 [ALL]
 [ADD_REMOVE|NO_ADD_REMOVE])</pre>
<p>The cpack_configure_downloads command configures installation-time downloads of selected components. For each downloadable component, CPack will create an archive containing the contents of that component, which should be uploaded to the given site. When the user selects that component for installation, the installer will download and extract the component in place. This feature is useful for creating small installers that only download the requested components, saving bandwidth. Additionally, the installers are small enough that they will be installed as part of the normal installation process, and the &quot;Change&quot; button in Windows Add/Remove Programs control panel will allow one to add or remove parts of the application after the original installation. On Windows, the downloaded-components functionality requires the ZipDLL plug-in for NSIS, available at: </p>
<pre><a rel="nofollow" href="http://nsis.sourceforge.net/ZipDLL_plug-in">http://nsis.sourceforge.net/ZipDLL_plug-in</a></pre>
<p>On macOS, installers that download components on-the-fly can only be built and installed on system using macOS 10.5 or later. </p>
<p> The site argument is a URL where the archives for downloadable components will reside, e.g., <i><a rel="nofollow" href="https://cmake.org/files/2.6.1/installer/">https://cmake.org/files/2.6.1/installer/</a></i> All of the archives produced by CPack should be uploaded to that location. </p>
<p> UPLOAD_DIRECTORY is the local directory where CPack will create the various archives for each of the components. The contents of this directory should be uploaded to a location accessible by the URL given in the site argument. If omitted, CPack will use the directory CPackUploads inside the CMake binary directory to store the generated archives. </p>
<p> The ALL flag indicates that all components be downloaded. Otherwise, only those components explicitly marked as DOWNLOADED or that have a specified ARCHIVE_FILE will be downloaded. Additionally, the ALL option implies ADD_REMOVE (unless NO_ADD_REMOVE is specified). </p>
<p> ADD_REMOVE indicates that CPack should install a copy of the installer that can be called from Windows&#8217; Add/Remove Programs dialog (via the &quot;Modify&quot; button) to change the set of installed components. NO_ADD_REMOVE turns off this behavior. This option is ignored on Mac OS X.</dl>
<h3>CPackIFW</h3>
<p>New in version 3.1. </p>
<p> This module looks for the location of the command-line utilities supplied with the <i>Qt Installer Framework</i> (QtIFW). </p>
<p> The module also defines several commands to control the behavior of the <code>CPack IFW Generator</code>.</p>
<h3>Commands</h3>
<p>The module defines the following commands:</p>
<dl>
<dt><code>cpack_ifw_configure_component</code></p>
<dd>Sets the arguments specific to the CPack IFW generator. </p>
<pre>cpack_ifw_configure_component(&lt;compname&gt; [COMMON] [ESSENTIAL] [VIRTUAL]
 [FORCED_INSTALLATION] [REQUIRES_ADMIN_RIGHTS]
 [NAME &lt;name&gt;]
 [DISPLAY_NAME &lt;display_name&gt;] # Note: Internationalization supported
 [DESCRIPTION &lt;description&gt;] # Note: Internationalization supported
 [UPDATE_TEXT &lt;update_text&gt;]
 [VERSION &lt;version&gt;]
 [RELEASE_DATE &lt;release_date&gt;]
 [SCRIPT &lt;script&gt;]
 [PRIORITY|SORTING_PRIORITY &lt;sorting_priority&gt;] # Note: PRIORITY is deprecated
 [DEPENDS|DEPENDENCIES &lt;com_id&gt; ...]
 [AUTO_DEPEND_ON &lt;comp_id&gt; ...]
 [LICENSES &lt;display_name&gt; &lt;file_path&gt; ...]
 [DEFAULT &lt;value&gt;]
 [USER_INTERFACES &lt;file_path&gt; &lt;file_path&gt; ...]
 [TRANSLATIONS &lt;file_path&gt; &lt;file_path&gt; ...]
 [REPLACES &lt;comp_id&gt; ...]
 [CHECKABLE &lt;value&gt;])</pre>
<p>This command should be called after <code>cpack_add_component()</code> command.</p>
<dt><code>COMMON</code></p>
<dd>if set, then the component will be packaged and installed as part of a group to which it belongs.</p>
<dt><code>ESSENTIAL</code></p>
<dd>New in version 3.6. </p>
<p> if set, then the package manager stays disabled until that component is updated.</p>
<dt><code>VIRTUAL</code></p>
<dd>New in version 3.8. </p>
<p> if set, then the component will be hidden from the installer. It is a equivalent of the <code>HIDDEN</code> option from the <code>cpack_add_component()</code> command.</p>
<dt><code>FORCED_INSTALLATION</code></p>
<dd>New in version 3.8. </p>
<p> if set, then the component must always be installed. It is a equivalent of the <code>REQUIRED</code> option from the <code>cpack_add_component()</code> command.</p>
<dt><code>REQUIRES_ADMIN_RIGHTS</code></p>
<dd>New in version 3.8. </p>
<p> set it if the component needs to be installed with elevated permissions.</p>
<dt><code>NAME</code></p>
<dd>is used to create domain-like identification for this component. By default used origin component name.</p>
<dt><code>DISPLAY_NAME</code></p>
<dd>New in version 3.8. </p>
<p> set to rewrite original name configured by <code>cpack_add_component()</code> command.</p>
<dt><code>DESCRIPTION</code></p>
<dd>New in version 3.8. </p>
<p> set to rewrite original description configured by <code>cpack_add_component()</code> command.</p>
<dt><code>UPDATE_TEXT</code></p>
<dd>New in version 3.8. </p>
<p> will be added to the component description if this is an update to the component.</p>
<dt><code>VERSION</code></p>
<dd>is version of component. By default used <code>CPACK_PACKAGE_VERSION</code>.</p>
<dt><code>RELEASE_DATE</code></p>
<dd>New in version 3.8. </p>
<p> keep empty to auto generate.</p>
<dt><code>SCRIPT</code></p>
<dd>is a relative or absolute path to operations script for this component.</p>
<dt><code>SORTING_PRIORITY</code></p>
<dd>New in version 3.8. </p>
<p> is priority of the component in the tree.</p>
<dt><code>PRIORITY</code></p>
<dd>Deprecated since version 3.8: Old name for <code>SORTING_PRIORITY</code>. </p>
<dt><code>DEPENDS</code>, <code>DEPENDENCIES</code></p>
<dd>New in version 3.8. </p>
<p> list of dependency component or component group identifiers in QtIFW style. </p>
<p> New in version 3.21. </p>
<p> Component or group names listed as dependencies may contain hyphens. This requires QtIFW 3.1 or later.</p>
<dt><code>AUTO_DEPEND_ON</code></p>
<dd>New in version 3.8. </p>
<p> list of identifiers of component or component group in QtIFW style that this component has an automatic dependency on.</p>
<dt><code>LICENSES</code></p>
<dd>pair of &lt;display_name&gt; and &lt;file_path&gt; of license text for this component. You can specify more then one license.</p>
<dt><code>DEFAULT</code></p>
<dd>New in version 3.8. </p>
<p> Possible values are: TRUE, FALSE, and SCRIPT. Set to FALSE to disable the component in the installer or to SCRIPT to resolved during runtime (don&#8217;t forget add the file of the script as a value of the <code>SCRIPT</code> option).</p>
<dt><code>USER_INTERFACES</code></p>
<dd>New in version 3.7. </p>
<p> is a list of &lt;file_path&gt; (&#8216;.ui&#8217; files) representing pages to load.</p>
<dt><code>TRANSLATIONS</code></p>
<dd>New in version 3.8. </p>
<p> is a list of &lt;file_path&gt; (&#8216;.qm&#8217; files) representing translations to load.</p>
<dt><code>REPLACES</code></p>
<dd>New in version 3.10. </p>
<p> list of identifiers of component or component group to replace.</p>
<dt><code>CHECKABLE</code></p>
<dd>New in version 3.10. </p>
<p> Possible values are: TRUE, FALSE. Set to FALSE if you want to hide the checkbox for an item. This is useful when only a few subcomponents should be selected instead of all.</p>
<dt><code>cpack_ifw_configure_component_group</code></p>
<dd>Sets the arguments specific to the CPack IFW generator. </p>
<pre>cpack_ifw_configure_component_group(&lt;groupname&gt; [VIRTUAL]
 [FORCED_INSTALLATION] [REQUIRES_ADMIN_RIGHTS]
 [NAME &lt;name&gt;]
 [DISPLAY_NAME &lt;display_name&gt;] # Note: Internationalization supported
 [DESCRIPTION &lt;description&gt;] # Note: Internationalization supported
 [UPDATE_TEXT &lt;update_text&gt;]
 [VERSION &lt;version&gt;]
 [RELEASE_DATE &lt;release_date&gt;]
 [SCRIPT &lt;script&gt;]
 [PRIORITY|SORTING_PRIORITY &lt;sorting_priority&gt;] # Note: PRIORITY is deprecated
 [DEPENDS|DEPENDENCIES &lt;com_id&gt; ...]
 [AUTO_DEPEND_ON &lt;comp_id&gt; ...]
 [LICENSES &lt;display_name&gt; &lt;file_path&gt; ...]
 [DEFAULT &lt;value&gt;]
 [USER_INTERFACES &lt;file_path&gt; &lt;file_path&gt; ...]
 [TRANSLATIONS &lt;file_path&gt; &lt;file_path&gt; ...]
 [REPLACES &lt;comp_id&gt; ...]
 [CHECKABLE &lt;value&gt;])</pre>
<p>This command should be called after <code>cpack_add_component_group()</code> command.</p>
<dt><code>VIRTUAL</code></p>
<dd>New in version 3.8. </p>
<p> if set, then the group will be hidden from the installer. Note that setting this on a root component does not work.</p>
<dt><code>FORCED_INSTALLATION</code></p>
<dd>New in version 3.8. </p>
<p> if set, then the group must always be installed.</p>
<dt><code>REQUIRES_ADMIN_RIGHTS</code></p>
<dd>New in version 3.8. </p>
<p> set it if the component group needs to be installed with elevated permissions.</p>
<dt><code>NAME</code></p>
<dd>is used to create domain-like identification for this component group. By default used origin component group name.</p>
<dt><code>DISPLAY_NAME</code></p>
<dd>New in version 3.8. </p>
<p> set to rewrite original name configured by <code>cpack_add_component_group()</code> command.</p>
<dt><code>DESCRIPTION</code></p>
<dd>New in version 3.8. </p>
<p> set to rewrite original description configured by <code>cpack_add_component_group()</code> command.</p>
<dt><code>UPDATE_TEXT</code></p>
<dd>New in version 3.8. </p>
<p> will be added to the component group description if this is an update to the component group.</p>
<dt><code>VERSION</code></p>
<dd>is version of component group. By default used <code>CPACK_PACKAGE_VERSION</code>.</p>
<dt><code>RELEASE_DATE</code></p>
<dd>New in version 3.8. </p>
<p> keep empty to auto generate.</p>
<dt><code>SCRIPT</code></p>
<dd>is a relative or absolute path to operations script for this component group.</p>
<dt><code>SORTING_PRIORITY</code></p>
<dd>is priority of the component group in the tree.</p>
<dt><code>PRIORITY</code></p>
<dd>Deprecated since version 3.8: Old name for <code>SORTING_PRIORITY</code>. </p>
<dt><code>DEPENDS</code>, <code>DEPENDENCIES</code></p>
<dd>New in version 3.8. </p>
<p> list of dependency component or component group identifiers in QtIFW style. </p>
<p> New in version 3.21. </p>
<p> Component or group names listed as dependencies may contain hyphens. This requires QtIFW 3.1 or later.</p>
<dt><code>AUTO_DEPEND_ON</code></p>
<dd>New in version 3.8. </p>
<p> list of identifiers of component or component group in QtIFW style that this component group has an automatic dependency on.</p>
<dt><code>LICENSES</code></p>
<dd>pair of &lt;display_name&gt; and &lt;file_path&gt; of license text for this component group. You can specify more then one license.</p>
<dt><code>DEFAULT</code></p>
<dd>New in version 3.8. </p>
<p> Possible values are: TRUE, FALSE, and SCRIPT. Set to TRUE to preselect the group in the installer (this takes effect only on groups that have no visible child components) or to SCRIPT to resolved during runtime (don&#8217;t forget add the file of the script as a value of the <code>SCRIPT</code> option).</p>
<dt><code>USER_INTERFACES</code></p>
<dd>New in version 3.7. </p>
<p> is a list of &lt;file_path&gt; (&#8216;.ui&#8217; files) representing pages to load.</p>
<dt><code>TRANSLATIONS</code></p>
<dd>New in version 3.8. </p>
<p> is a list of &lt;file_path&gt; (&#8216;.qm&#8217; files) representing translations to load.</p>
<dt><code>REPLACES</code></p>
<dd>New in version 3.10. </p>
<p> list of identifiers of component or component group to replace.</p>
<dt><code>CHECKABLE</code></p>
<dd>New in version 3.10. </p>
<p> Possible values are: TRUE, FALSE. Set to FALSE if you want to hide the checkbox for an item. This is useful when only a few subcomponents should be selected instead of all.</p>
<dt><code>cpack_ifw_add_repository</code></p>
<dd>Add QtIFW specific remote repository to binary installer. </p>
<pre>cpack_ifw_add_repository(&lt;reponame&gt; [DISABLED]
 URL &lt;url&gt;
 [USERNAME &lt;username&gt;]
 [PASSWORD &lt;password&gt;]
 [DISPLAY_NAME &lt;display_name&gt;])</pre>
<p>This command will also add the &lt;reponame&gt; repository to a variable <code>CPACK_IFW_REPOSITORIES_ALL</code>.</p>
<dt><code>DISABLED</code></p>
<dd>if set, then the repository will be disabled by default.</p>
<dt><code>URL</code></p>
<dd>is points to a list of available components.</p>
<dt><code>USERNAME</code></p>
<dd>is used as user on a protected repository.</p>
<dt><code>PASSWORD</code></p>
<dd>is password to use on a protected repository.</p>
<dt><code>DISPLAY_NAME</code></p>
<dd>is string to display instead of the URL.</p>
<dt><code>cpack_ifw_update_repository</code></p>
<dd>New in version 3.6. </p>
<p> Update QtIFW specific repository from remote repository. </p>
<pre>cpack_ifw_update_repository(&lt;reponame&gt;
 [[ADD|REMOVE] URL &lt;url&gt;]|
 [REPLACE OLD_URL &lt;old_url&gt; NEW_URL &lt;new_url&gt;]]
 [USERNAME &lt;username&gt;]
 [PASSWORD &lt;password&gt;]
 [DISPLAY_NAME &lt;display_name&gt;])</pre>
<p>This command will also add the &lt;reponame&gt; repository to a variable <code>CPACK_IFW_REPOSITORIES_ALL</code>.</p>
<dt><code>URL</code></p>
<dd>is points to a list of available components.</p>
<dt><code>OLD_URL</code></p>
<dd>is points to a list that will replaced.</p>
<dt><code>NEW_URL</code></p>
<dd>is points to a list that will replace to.</p>
<dt><code>USERNAME</code></p>
<dd>is used as user on a protected repository.</p>
<dt><code>PASSWORD</code></p>
<dd>is password to use on a protected repository.</p>
<dt><code>DISPLAY_NAME</code></p>
<dd>is string to display instead of the URL.</p>
<dt><code>cpack_ifw_add_package_resources</code></p>
<dd>New in version 3.7. </p>
<p> Add additional resources in the installer binary. </p>
<pre>cpack_ifw_add_package_resources(&lt;file_path&gt; &lt;file_path&gt; ...)</pre>
<p>This command will also add the specified files to a variable <code>CPACK_IFW_PACKAGE_RESOURCES</code>.</dl>
<h3>CPackIFWConfigureFile</h3>
<p>New in version 3.8. </p>
<p> The module defines <code>configure_file()</code> similar command to configure file templates prepared in QtIFW/SDK/Creator style.</p>
<h3>Commands</h3>
<p>The module defines the following commands:</p>
<dl>
<dt><code>cpack_ifw_configure_file</code></p>
<dd>Copy a file to another location and modify its contents. </p>
<pre>cpack_ifw_configure_file(&lt;input&gt; &lt;output&gt;)</pre>
<p>Copies an <code>&lt;input&gt;</code> file to an <code>&lt;output&gt;</code> file and substitutes variable values referenced as <code>%{VAR}</code> or <code>%VAR%</code> in the input file content. Each variable reference will be replaced with the current value of the variable, or the empty string if the variable is not defined.</dl>
<h3>CSharpUtilities</h3>
<p>New in version 3.8. </p>
<p> Functions to make configuration of CSharp/.NET targets easier. </p>
<p> A collection of CMake utility functions useful for dealing with CSharp targets for Visual Studio generators from version 2010 and later. </p>
<p> The following functions are provided by this module: </p>
<p> <code>Main functions</code></p>
<dl>
<dt>&bull;</p>
<dd><i>csharp_set_windows_forms_properties()</i></p>
<dt>&bull;</p>
<dd><i>csharp_set_designer_cs_properties()</i></p>
<dt>&bull;</p>
<dd><i>csharp_set_xaml_cs_properties()</i> </p>
<p> <code>Helper functions</code></p>
<dt>&bull;</p>
<dd><i>csharp_get_filename_keys()</i></p>
<dt>&bull;</p>
<dd><i>csharp_get_filename_key_base()</i></p>
<dt>&bull;</p>
<dd><i>csharp_get_dependentupon_name()</i></dl>
<h3>Main functions provided by the module</h3>
<dl>
<dt><code>csharp_set_windows_forms_properties</code></p>
<dd>Sets source file properties for use of Windows Forms. Use this, if your CSharp target uses Windows Forms: </p>
<pre>csharp_set_windows_forms_properties([&lt;file1&gt; [&lt;file2&gt; [...]]])</pre>
<dt><code>&lt;fileN&gt;</code></p>
<dd>List of all source files which are relevant for setting the <code>VS_CSHARP_&lt;tagname&gt;</code> properties (including <code>.cs</code>, <code>.resx</code> and <code>.Designer.cs</code> extensions). </p>
<p> In the list of all given files for all files ending with <code>.Designer.cs</code> and <code>.resx</code> is searched. For every <i>designer</i> or <i>resource</i> file a file with the same base name but only <code>.cs</code> as extension is searched. If this is found, the <code>VS_CSHARP_&lt;tagname&gt;</code> properties are set as follows:</p>
<dt>for the <code>.cs</code> file:</p>
<dd>
<dt>&bull;</p>
<dd>VS_CSHARP_SubType &quot;Form&quot;</p>
<dt>for the <code>.Designer.cs</code> file (if it exists):</p>
<dd>
<dt>&bull;</p>
<dd>VS_CSHARP_DependentUpon &lt;cs-filename&gt;</p>
<dt>&bull;</p>
<dd>VS_CSHARP_DesignTime &quot;&quot; (delete tag if previously defined)</p>
<dt>&bull;</p>
<dd>VS_CSHARP_AutoGen &quot;&quot;(delete tag if previously defined)</p>
<dt>for the <code>.resx</code> file (if it exists):</p>
<dd>
<dt>&bull;</p>
<dd>VS_RESOURCE_GENERATOR &quot;&quot; (delete tag if previously defined)</p>
<dt>&bull;</p>
<dd>VS_CSHARP_DependentUpon &lt;cs-filename&gt;</p>
<dt>&bull;</p>
<dd>VS_CSHARP_SubType &quot;Designer&quot;</p>
<dt><code>csharp_set_designer_cs_properties</code></p>
<dd>Sets source file properties of <code>.Designer.cs</code> files depending on sibling filenames. Use this, if your CSharp target does <code>not</code> use Windows Forms (for Windows Forms use <i>csharp_set_designer_cs_properties()</i> instead): </p>
<pre>csharp_set_designer_cs_properties([&lt;file1&gt; [&lt;file2&gt; [...]]])</pre>
<dt><code>&lt;fileN&gt;</code></p>
<dd>List of all source files which are relevant for setting the <code>VS_CSHARP_&lt;tagname&gt;</code> properties (including <code>.cs</code>, <code>.resx</code>, <code>.settings</code> and <code>.Designer.cs</code> extensions). </p>
<p> In the list of all given files for all files ending with <code>.Designer.cs</code> is searched. For every <i>designer</i> file all files with the same base name but different extensions are searched. If a match is found, the source file properties of the <i>designer</i> file are set depending on the extension of the matched file:</p>
<dt>if match is <code>.resx</code> file:</p>
<dd>
<dt>&bull;</p>
<dd>VS_CSHARP_AutoGen &quot;True&quot;</p>
<dt>&bull;</p>
<dd>VS_CSHARP_DesignTime &quot;True&quot;</p>
<dt>&bull;</p>
<dd>VS_CSHARP_DependentUpon &lt;resx-filename&gt;</p>
<dt>if match is <code>.cs</code> file:</p>
<dd>
<dt>&bull;</p>
<dd>VS_CSHARP_DependentUpon &lt;cs-filename&gt;</p>
<dt>if match is <code>.settings</code> file:</p>
<dd>
<dt>&bull;</p>
<dd>VS_CSHARP_AutoGen &quot;True&quot;</p>
<dt>&bull;</p>
<dd>VS_CSHARP_DesignTimeSharedInput &quot;True&quot;</p>
<dt>&bull;</p>
<dd>VS_CSHARP_DependentUpon &lt;settings-filename&gt; </p>
<p> <code>NOTE:</code> Because the source file properties of the <code>.Designer.cs</code> file are set according to the found matches and every match sets the <code>VS_CSHARP_DependentUpon</code> property, there should only be one match for each <code>Designer.cs</code> file.</p>
<dt><code>csharp_set_xaml_cs_properties</code></p>
<dd>Sets source file properties for use of Windows Presentation Foundation (WPF) and XAML. Use this, if your CSharp target uses WPF/XAML: </p>
<pre>csharp_set_xaml_cs_properties([&lt;file1&gt; [&lt;file2&gt; [...]]])</pre>
<dt><code>&lt;fileN&gt;</code></p>
<dd>List of all source files which are relevant for setting the <code>VS_CSHARP_&lt;tagname&gt;</code> properties (including <code>.cs</code>, <code>.xaml</code>, and <code>.xaml.cs</code> extensions). </p>
<p> In the list of all given files for all files ending with <code>.xaml.cs</code> is searched. For every <i>xaml-cs</i> file, a file with the same base name but extension <code>.xaml</code> is searched. If a match is found, the source file properties of the <code>.xaml.cs</code> file are set:</p>
<dt>&bull;</p>
<dd>VS_CSHARP_DependentUpon &lt;xaml-filename&gt;</dl>
<h3>Helper functions which are used by the above ones</h3>
<dl>
<dt><code>csharp_get_filename_keys</code></p>
<dd>Helper function which computes a list of key values to identify source files independently of relative/absolute paths given in cmake and eliminates case sensitivity: </p>
<pre>csharp_get_filename_keys(OUT [&lt;file1&gt; [&lt;file2&gt; [...]]])</pre>
<dt><code>OUT</code></p>
<dd>Name of the variable in which the list of keys is stored</p>
<dt><code>&lt;fileN&gt;</code></p>
<dd>filename(s) as given to to CSharp target using <code>add_library()</code> or <code>add_executable()</code> </p>
<p> In some way the function applies a canonicalization to the source names. This is necessary to find file matches if the files have been added to the target with different directory prefixes: </p>
<pre>add_library(lib
 myfile.cs
 ${CMAKE_CURRENT_SOURCE_DIR}/myfile.Designer.cs)
set_source_files_properties(myfile.Designer.cs PROPERTIES
 VS_CSHARP_DependentUpon myfile.cs)
# this will fail, because in cmake
# - ${CMAKE_CURRENT_SOURCE_DIR}/myfile.Designer.cs
# - myfile.Designer.cs
# are not the same source file. The source file property is not set.</pre>
<dt><code>csharp_get_filename_key_base</code></p>
<dd>Returns the full filepath and name <code>without</code> extension of a key. KEY is expected to be a key from csharp_get_filename_keys. In BASE the value of KEY without the file extension is returned: </p>
<pre>csharp_get_filename_key_base(BASE KEY)</pre>
<dt><code>BASE</code></p>
<dd>Name of the variable with the computed &quot;base&quot; of <code>KEY</code>.</p>
<dt><code>KEY</code></p>
<dd>The key of which the base will be computed. Expected to be a upper case full filename.</p>
<dt><code>csharp_get_dependentupon_name</code></p>
<dd>Computes a string which can be used as value for the source file property <code>VS_CSHARP_&lt;tagname&gt;</code> with <i>target</i> being <code>DependentUpon</code>: </p>
<pre>csharp_get_dependentupon_name(NAME FILE)</pre>
<dt><code>NAME</code></p>
<dd>Name of the variable with the result value</p>
<dt><code>FILE</code></p>
<dd>Filename to convert to <code>&lt;DependentUpon&gt;</code> value </p>
<p> Actually this is only the filename without any path given at the moment.</dl>
<h3>CTest</h3>
<p>Configure a project for testing with CTest/CDash </p>
<p> Include this module in the top CMakeLists.txt file of a project to enable testing with CTest and dashboard submissions to CDash: </p>
<pre>project(MyProject)
...
include(CTest)</pre>
<p>The module automatically creates a <code>BUILD_TESTING</code> option that selects whether to enable testing support (<code>ON</code> by default). After including the module, use code like: </p>
<pre>if(BUILD_TESTING)
 # ... CMake code to create tests ...
endif()</pre>
<p>to creating tests when testing is enabled. </p>
<p> To enable submissions to a CDash server, create a <code>CTestConfig.cmake</code> file at the top of the project with content such as: </p>
<pre>set(CTEST_NIGHTLY_START_TIME &quot;01:00:00 UTC&quot;)
set(CTEST_SUBMIT_URL &quot;<a rel="nofollow" href="http://my.cdash.org/submit.php?project=MyProject">http://my.cdash.org/submit.php?project=MyProject</a>&quot;)</pre>
<p>(the CDash server can provide the file to a project administrator who configures <code>MyProject</code>). Settings in the config file are shared by both this <code>CTest</code> module and the <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> command-line Dashboard Client mode (<code>ctest -S</code>). </p>
<p> While building a project for submission to CDash, CTest scans the build output for errors and warnings and reports them with surrounding context from the build log. This generic approach works for all build tools, but does not give details about the command invocation that produced a given problem. One may get more detailed reports by setting the <code>CTEST_USE_LAUNCHERS</code> variable: </p>
<pre>set(CTEST_USE_LAUNCHERS 1)</pre>
<p>in the <code>CTestConfig.cmake</code> file.</p>
<h3>CTestCoverageCollectGCOV</h3>
<p>New in version 3.2. </p>
<p> This module provides the <code>ctest_coverage_collect_gcov</code> function. </p>
<p> This function runs gcov on all .gcda files found in the binary tree and packages the resulting .gcov files into a tar file. This tarball also contains the following:</p>
<dl>
<dt>&bull;</p>
<dd><i>data.json</i> defines the source and build directories for use by CDash.</p>
<dt>&bull;</p>
<dd><i>Labels.json</i> indicates any <code>LABELS</code> that have been set on the source files.</p>
<dt>&bull;</p>
<dd>The <i>uncovered</i> directory holds any uncovered files found by <code>CTEST_EXTRA_COVERAGE_GLOB</code>. </p>
<p> After generating this tar file, it can be sent to CDash for display with the <code>ctest_submit(CDASH_UPLOAD)</code> command.</p>
<dt><code>ctest_coverage_collect_gcov</code></p>
<dd>
<pre>ctest_coverage_collect_gcov(TARBALL &lt;tarfile&gt;
 [SOURCE &lt;source_dir&gt;][BUILD &lt;build_dir&gt;]
 [GCOV_COMMAND &lt;gcov_command&gt;]
 [GCOV_OPTIONS &lt;options&gt;...]
 )</pre>
<p>Run gcov and package a tar file for CDash. The options are:</p>
<dt><code>TARBALL &lt;tarfile&gt;</code></p>
<dd>Specify the location of the <code>.tar</code> file to be created for later upload to CDash. Relative paths will be interpreted with respect to the top-level build directory.</p>
<dt><code>TARBALL_COMPRESSION &lt;option&gt;</code></p>
<dd>New in version 3.18. </p>
<p> Specify a compression algorithm for the <code>TARBALL</code> data file. Using this option reduces the size of the data file before it is submitted to CDash. <code>&lt;option&gt;</code> must be one of <code>GZIP</code>, <code>BZIP2</code>, <code>XZ</code>, <code>ZSTD</code>, <code>FROM_EXT</code>, or an expression that CMake evaluates as <code>FALSE</code>. The default value is <code>BZIP2</code>. </p>
<p> If <code>FROM_EXT</code> is specified, the resulting file will be compressed based on the file extension of the <code>&lt;tarfile&gt;</code> (i.e. <code>.tar.gz</code> will use <code>GZIP</code> compression). File extensions that will produce compressed output include <code>.tar.gz</code>, <code>.tgz</code>, <code>.tar.bzip2</code>, <code>.tbz</code>, <code>.tar.xz</code>, and <code>.txz</code>.</p>
<dt><code>SOURCE &lt;source_dir&gt;</code></p>
<dd>Specify the top-level source directory for the build. Default is the value of <code>CTEST_SOURCE_DIRECTORY</code>.</p>
<dt><code>BUILD &lt;build_dir&gt;</code></p>
<dd>Specify the top-level build directory for the build. Default is the value of <code>CTEST_BINARY_DIRECTORY</code>.</p>
<dt><code>GCOV_COMMAND &lt;gcov_command&gt;</code></p>
<dd>Specify the full path to the <code>gcov</code> command on the machine. Default is the value of <code>CTEST_COVERAGE_COMMAND</code>.</p>
<dt><code>GCOV_OPTIONS &lt;options&gt;&#8230;</code></p>
<dd>Specify options to be passed to gcov. The <code>gcov</code> command is run as <code>gcov &lt;options&gt;&#8230; -o &lt;gcov-dir&gt; &lt;file&gt;.gcda</code>. If not specified, the default option is just <code>-b -x</code>.</p>
<dt><code>GLOB</code></p>
<dd>New in version 3.6. </p>
<p> Recursively search for .gcda files in build_dir rather than determining search locations by reading TargetDirectories.txt.</p>
<dt><code>DELETE</code></p>
<dd>New in version 3.6. </p>
<p> Delete coverage files after they&#8217;ve been packaged into the .tar.</p>
<dt><code>QUIET</code></p>
<dd>Suppress non-error messages that otherwise would have been printed out by this function. </p>
<p> New in version 3.3: Added support for the <code>CTEST_CUSTOM_COVERAGE_EXCLUDE</code> variable. </p>
</dl>
<h3>CTestScriptMode</h3>
<p>This file is read by ctest in script mode (-S)</p>
<h3>CTestUseLaunchers</h3>
<p>Set the RULE_LAUNCH_* global properties when CTEST_USE_LAUNCHERS is on. </p>
<p> CTestUseLaunchers is automatically included when you include(CTest). However, it is split out into its own module file so projects can use the CTEST_USE_LAUNCHERS functionality independently. </p>
<p> To use launchers, set CTEST_USE_LAUNCHERS to ON in a ctest -S dashboard script, and then also set it in the cache of the configured project. Both cmake and ctest need to know the value of it for the launchers to work properly. CMake needs to know in order to generate proper build rules, and ctest, in order to produce the proper error and warning analysis. </p>
<p> For convenience, you may set the ENV variable CTEST_USE_LAUNCHERS_DEFAULT in your ctest -S script, too. Then, as long as your CMakeLists uses include(CTest) or include(CTestUseLaunchers), it will use the value of the ENV variable to initialize a CTEST_USE_LAUNCHERS cache variable. This cache variable initialization only occurs if CTEST_USE_LAUNCHERS is not already defined. </p>
<p> New in version 3.8: If CTEST_USE_LAUNCHERS is on in a ctest -S script the ctest_configure command will add -DCTEST_USE_LAUNCHERS:BOOL=TRUE to the cmake command used to configure the project.</p>
<h3>Dart</h3>
<p>Configure a project for testing with CTest or old Dart Tcl Client </p>
<p> This file is the backwards-compatibility version of the CTest module. It supports using the old Dart 1 Tcl client for driving dashboard submissions as well as testing with CTest. This module should be included in the CMakeLists.txt file at the top of a project. Typical usage: </p>
<pre>include(Dart)
if(BUILD_TESTING)
 # ... testing related CMake code ...
endif()</pre>
<p>The BUILD_TESTING option is created by the Dart module to determine whether testing support should be enabled. The default is ON.</p>
<h3>DeployQt4</h3>
<p>Functions to help assemble a standalone Qt4 executable. </p>
<p> A collection of CMake utility functions useful for deploying Qt4 executables. </p>
<p> The following functions are provided by this module: </p>
<pre>write_qt4_conf
resolve_qt4_paths
fixup_qt4_executable
install_qt4_plugin_path
install_qt4_plugin
install_qt4_executable</pre>
<p>Requires CMake 2.6 or greater because it uses function and PARENT_SCOPE. Also depends on BundleUtilities.cmake. </p>
<pre>write_qt4_conf(&lt;qt_conf_dir&gt; &lt;qt_conf_contents&gt;)</pre>
<p>Writes a qt.conf file with the &lt;qt_conf_contents&gt; into &lt;qt_conf_dir&gt;. </p>
<pre>resolve_qt4_paths(&lt;paths_var&gt; [&lt;executable_path&gt;])</pre>
<p>Loop through &lt;paths_var&gt; list and if any don&#8217;t exist resolve them relative to the &lt;executable_path&gt; (if supplied) or the CMAKE_INSTALL_PREFIX. </p>
<pre>fixup_qt4_executable(&lt;executable&gt;
 [&lt;qtplugins&gt; &lt;libs&gt; &lt;dirs&gt; &lt;plugins_dir&gt; &lt;request_qt_conf&gt;])</pre>
<p>Copies Qt plugins, writes a Qt configuration file (if needed) and fixes up a Qt4 executable using BundleUtilities so it is standalone and can be drag-and-drop copied to another machine as long as all of the system libraries are compatible. </p>
<p> &lt;executable&gt; should point to the executable to be fixed-up. </p>
<p> &lt;qtplugins&gt; should contain a list of the names or paths of any Qt plugins to be installed. </p>
<p> &lt;libs&gt; will be passed to BundleUtilities and should be a list of any already installed plugins, libraries or executables to also be fixed-up. </p>
<p> &lt;dirs&gt; will be passed to BundleUtilities and should contain and directories to be searched to find library dependencies. </p>
<p> &lt;plugins_dir&gt; allows an custom plugins directory to be used. </p>
<p> &lt;request_qt_conf&gt; will force a qt.conf file to be written even if not needed. </p>
<pre>install_qt4_plugin_path(plugin executable copy installed_plugin_path_var
 &lt;plugins_dir&gt; &lt;component&gt; &lt;configurations&gt;)</pre>
<p>Install (or copy) a resolved &lt;plugin&gt; to the default plugins directory (or &lt;plugins_dir&gt;) relative to &lt;executable&gt; and store the result in &lt;installed_plugin_path_var&gt;. </p>
<p> If &lt;copy&gt; is set to TRUE then the plugins will be copied rather than installed. This is to allow this module to be used at CMake time rather than install time. </p>
<p> If &lt;component&gt; is set then anything installed will use this COMPONENT. </p>
<pre>install_qt4_plugin(plugin executable copy installed_plugin_path_var
 &lt;plugins_dir&gt; &lt;component&gt;)</pre>
<p>Install (or copy) an unresolved &lt;plugin&gt; to the default plugins directory (or &lt;plugins_dir&gt;) relative to &lt;executable&gt; and store the result in &lt;installed_plugin_path_var&gt;. See documentation of INSTALL_QT4_PLUGIN_PATH. </p>
<pre>install_qt4_executable(&lt;executable&gt;
 [&lt;qtplugins&gt; &lt;libs&gt; &lt;dirs&gt; &lt;plugins_dir&gt; &lt;request_qt_conf&gt; &lt;component&gt;])</pre>
<p>Installs Qt plugins, writes a Qt configuration file (if needed) and fixes up a Qt4 executable using BundleUtilities so it is standalone and can be drag-and-drop copied to another machine as long as all of the system libraries are compatible. The executable will be fixed-up at install time. &lt;component&gt; is the COMPONENT used for bundle fixup and plugin installation. See documentation of FIXUP_QT4_BUNDLE.</p>
<h3>ExternalData</h3>
<p>Manage data files stored outside source tree</p>
<h3>Introduction</h3>
<p>Use this module to unambiguously reference data files stored outside the source tree and fetch them at build time from arbitrary local and remote content-addressed locations. Functions provided by this module recognize arguments with the syntax <code>DATA{&lt;name&gt;}</code> as references to external data, replace them with full paths to local copies of those data, and create build rules to fetch and update the local copies. </p>
<p> For example: </p>
<pre>include(ExternalData)
set(ExternalData_URL_TEMPLATES &quot;file:///local/%(algo)/%(hash)&quot;
 &quot;file:////host/share/%(algo)/%(hash)&quot;
 &quot;<a rel="nofollow" href="http://data.org/%(algo)/%(hash)">http://data.org/%(algo)/%(hash)</a>&quot;)
ExternalData_Add_Test(MyData
 NAME MyTest
 COMMAND MyExe DATA{MyInput.png}
 )
ExternalData_Add_Target(MyData)</pre>
<p>When test <code>MyTest</code> runs the <code>DATA{MyInput.png}</code> argument will be replaced by the full path to a real instance of the data file <code>MyInput.png</code> on disk. If the source tree contains a content link such as <code>MyInput.png.md5</code> then the <code>MyData</code> target creates a real <code>MyInput.png</code> in the build tree.</p>
<h3>Module Functions</h3>
<dl>
<dt><code>ExternalData_Expand_Arguments</code></p>
<dd>The <code>ExternalData_Expand_Arguments</code> function evaluates <code>DATA{}</code> references in its arguments and constructs a new list of arguments: </p>
<pre>ExternalData_Expand_Arguments(
 &lt;target&gt; # Name of data management target
 &lt;outVar&gt; # Output variable
 [args...] # Input arguments, DATA{} allowed
 )</pre>
<p>It replaces each <code>DATA{}</code> reference in an argument with the full path of a real data file on disk that will exist after the <code>&lt;target&gt;</code> builds.</p>
<dt><code>ExternalData_Add_Test</code></p>
<dd>The <code>ExternalData_Add_Test</code> function wraps around the CMake <code>add_test()</code> command but supports <code>DATA{}</code> references in its arguments: </p>
<pre>ExternalData_Add_Test(
 &lt;target&gt; # Name of data management target
 ... # Arguments of add_test(), DATA{} allowed
 )</pre>
<p>It passes its arguments through <code>ExternalData_Expand_Arguments</code> and then invokes the <code>add_test()</code> command using the results.</p>
<dt><code>ExternalData_Add_Target</code></p>
<dd>The <code>ExternalData_Add_Target</code> function creates a custom target to manage local instances of data files stored externally: </p>
<pre>ExternalData_Add_Target(
 &lt;target&gt; # Name of data management target
 [SHOW_PROGRESS &lt;ON|OFF&gt;] # Show progress during the download
 )</pre>
<p>It creates custom commands in the target as necessary to make data files available for each <code>DATA{}</code> reference previously evaluated by other functions provided by this module. Data files may be fetched from one of the URL templates specified in the <code>ExternalData_URL_TEMPLATES</code> variable, or may be found locally in one of the paths specified in the <code>ExternalData_OBJECT_STORES</code> variable. </p>
<p> New in version 3.20: The <code>SHOW_PROGRESS</code> argument may be passed to suppress progress information during the download of objects. If not provided, it defaults to <code>OFF</code> for <code>Ninja</code> and <code>Ninja Multi-Config</code> generators and <code>ON</code> otherwise. </p>
<p> Typically only one target is needed to manage all external data within a project. Call this function once at the end of configuration after all data references have been processed.</dl>
<h3>Module Variables</h3>
<p>The following variables configure behavior. They should be set before calling any of the functions provided by this module.</p>
<dl>
<dt><code>ExternalData_BINARY_ROOT</code></p>
<dd>The <code>ExternalData_BINARY_ROOT</code> variable may be set to the directory to hold the real data files named by expanded <code>DATA{}</code> references. The default is <code>CMAKE_BINARY_DIR</code>. The directory layout will mirror that of content links under <code>ExternalData_SOURCE_ROOT</code>.</p>
<dt><code>ExternalData_CUSTOM_SCRIPT_&lt;key&gt;</code></p>
<dd>New in version 3.2. </p>
<p> Specify a full path to a <code>.cmake</code> custom fetch script identified by <code>&lt;key&gt;</code> in entries of the <code>ExternalData_URL_TEMPLATES</code> list. See <i>Custom Fetch Scripts</i>.</p>
<dt><code>ExternalData_LINK_CONTENT</code></p>
<dd>The <code>ExternalData_LINK_CONTENT</code> variable may be set to the name of a supported hash algorithm to enable automatic conversion of real data files referenced by the <code>DATA{}</code> syntax into content links. For each such <code>&lt;file&gt;</code> a content link named <code>&lt;file&gt;&lt;ext&gt;</code> is created. The original file is renamed to the form <code>.ExternalData_&lt;algo&gt;_&lt;hash&gt;</code> to stage it for future transmission to one of the locations in the list of URL templates (by means outside the scope of this module). The data fetch rule created for the content link will use the staged object if it cannot be found using any URL template.</p>
<dt><code>ExternalData_NO_SYMLINKS</code></p>
<dd>New in version 3.3. </p>
<p> The real data files named by expanded <code>DATA{}</code> references may be made available under <code>ExternalData_BINARY_ROOT</code> using symbolic links on some platforms. The <code>ExternalData_NO_SYMLINKS</code> variable may be set to disable use of symbolic links and enable use of copies instead.</p>
<dt><code>ExternalData_OBJECT_STORES</code></p>
<dd>The <code>ExternalData_OBJECT_STORES</code> variable may be set to a list of local directories that store objects using the layout <code>&lt;dir&gt;/%(algo)/%(hash)</code>. These directories will be searched first for a needed object. If the object is not available in any store then it will be fetched remotely using the URL templates and added to the first local store listed. If no stores are specified the default is a location inside the build tree.</p>
<dt><code>ExternalData_SERIES_PARSE</code></p>
<dd>
<dt><code>ExternalData_SERIES_PARSE_PREFIX</code></p>
<dd>
<dt><code>ExternalData_SERIES_PARSE_NUMBER</code></p>
<dd>
<dt><code>ExternalData_SERIES_PARSE_SUFFIX</code></p>
<dd>
<dt><code>ExternalData_SERIES_MATCH</code></p>
<dd>See <i>Referencing File Series</i>.</p>
<dt><code>ExternalData_SOURCE_ROOT</code></p>
<dd>The <code>ExternalData_SOURCE_ROOT</code> variable may be set to the highest source directory containing any path named by a <code>DATA{}</code> reference. The default is <code>CMAKE_SOURCE_DIR</code>. <code>ExternalData_SOURCE_ROOT</code> and <code>CMAKE_SOURCE_DIR</code> must refer to directories within a single source distribution (e.g. they come together in one tarball).</p>
<dt><code>ExternalData_TIMEOUT_ABSOLUTE</code></p>
<dd>The <code>ExternalData_TIMEOUT_ABSOLUTE</code> variable sets the download absolute timeout, in seconds, with a default of <code>300</code> seconds. Set to <code>0</code> to disable enforcement.</p>
<dt><code>ExternalData_TIMEOUT_INACTIVITY</code></p>
<dd>The <code>ExternalData_TIMEOUT_INACTIVITY</code> variable sets the download inactivity timeout, in seconds, with a default of <code>60</code> seconds. Set to <code>0</code> to disable enforcement.</p>
<dt><code>ExternalData_URL_ALGO_&lt;algo&gt;_&lt;key&gt;</code></p>
<dd>New in version 3.3. </p>
<p> Specify a custom URL component to be substituted for URL template placeholders of the form <code>%(algo:&lt;key&gt;)</code>, where <code>&lt;key&gt;</code> is a valid C identifier, when fetching an object referenced via hash algorithm <code>&lt;algo&gt;</code>. If not defined, the default URL component is just <code>&lt;algo&gt;</code> for any <code>&lt;key&gt;</code>.</p>
<dt><code>ExternalData_URL_TEMPLATES</code></p>
<dd>The <code>ExternalData_URL_TEMPLATES</code> may be set to provide a list of URL templates using the placeholders <code>%(algo)</code> and <code>%(hash)</code> in each template. Data fetch rules try each URL template in order by substituting the hash algorithm name for <code>%(algo)</code> and the hash value for <code>%(hash)</code>. Alternatively one may use <code>%(algo:&lt;key&gt;)</code> with <code>ExternalData_URL_ALGO_&lt;algo&gt;_&lt;key&gt;</code> variables to gain more flexibility in remote URLs.</dl>
<h3>Referencing Files</h3>
<h3>Referencing Single Files</h3>
<p>The <code>DATA{}</code> syntax is literal and the <code>&lt;name&gt;</code> is a full or relative path within the source tree. The source tree must contain either a real data file at <code>&lt;name&gt;</code> or a &quot;content link&quot; at <code>&lt;name&gt;&lt;ext&gt;</code> containing a hash of the real file using a hash algorithm corresponding to <code>&lt;ext&gt;</code>. For example, the argument <code>DATA{img.png}</code> may be satisfied by either a real <code>img.png</code> file in the current source directory or a <code>img.png.md5</code> file containing its MD5 sum. </p>
<p> New in version 3.8: Multiple content links of the same name with different hash algorithms are supported (e.g. <code>img.png.sha256</code> and <code>img.png.sha1</code>) so long as they all correspond to the same real file. This allows objects to be fetched from sources indexed by different hash algorithms.</p>
<h3>Referencing File Series</h3>
<p>The <code>DATA{}</code> syntax can be told to fetch a file series using the form <code>DATA{&lt;name&gt;,:}</code>, where the <code>:</code> is literal. If the source tree contains a group of files or content links named like a series then a reference to one member adds rules to fetch all of them. Although all members of a series are fetched, only the file originally named by the <code>DATA{}</code> argument is substituted for it. The default configuration recognizes file series names ending with <code>#.ext</code>, <code>_#.ext</code>, <code>.#.ext</code>, or <code>-#.ext</code> where <code>#</code> is a sequence of decimal digits and <code>.ext</code> is any single extension. Configure it with a regex that parses <code>&lt;number&gt;</code> and <code>&lt;suffix&gt;</code> parts from the end of <code>&lt;name&gt;</code>: </p>
<pre>ExternalData_SERIES_PARSE = regex of the form (&lt;number&gt;)(&lt;suffix&gt;)$</pre>
<p>For more complicated cases set: </p>
<pre>ExternalData_SERIES_PARSE = regex with at least two () groups
ExternalData_SERIES_PARSE_PREFIX = &lt;prefix&gt; regex group number, if any
ExternalData_SERIES_PARSE_NUMBER = &lt;number&gt; regex group number
ExternalData_SERIES_PARSE_SUFFIX = &lt;suffix&gt; regex group number</pre>
<p>Configure series number matching with a regex that matches the <code>&lt;number&gt;</code> part of series members named <code>&lt;prefix&gt;&lt;number&gt;&lt;suffix&gt;</code>: </p>
<pre>ExternalData_SERIES_MATCH = regex matching &lt;number&gt; in all series members</pre>
<p>Note that the <code>&lt;suffix&gt;</code> of a series does not include a hash-algorithm extension.</p>
<h3>Referencing Associated Files</h3>
<p>The <code>DATA{}</code> syntax can alternatively match files associated with the named file and contained in the same directory. Associated files may be specified by options using the syntax <code>DATA{&lt;name&gt;,&lt;opt1&gt;,&lt;opt2&gt;,&#8230;}</code>. Each option may specify one file by name or specify a regular expression to match file names using the syntax <code>REGEX:&lt;regex&gt;</code>. For example, the arguments: </p>
<pre>DATA{MyData/MyInput.mhd,MyInput.img} # File pair
DATA{MyData/MyFrames00.png,REGEX:MyFrames[0-9]+\.png} # Series</pre>
<p>will pass <code>MyInput.mha</code> and <code>MyFrames00.png</code> on the command line but ensure that the associated files are present next to them.</p>
<h3>Referencing Directories</h3>
<p>The <code>DATA{}</code> syntax may reference a directory using a trailing slash and a list of associated files. The form <code>DATA{&lt;name&gt;/,&lt;opt1&gt;,&lt;opt2&gt;,&#8230;}</code> adds rules to fetch any files in the directory that match one of the associated file options. For example, the argument <code>DATA{MyDataDir/,REGEX:.*}</code> will pass the full path to a <code>MyDataDir</code> directory on the command line and ensure that the directory contains files corresponding to every file or content link in the <code>MyDataDir</code> source directory. </p>
<p> New in version 3.3: In order to match associated files in subdirectories, specify a <code>RECURSE:</code> option, e.g. <code>DATA{MyDataDir/,RECURSE:,REGEX:.*}</code>.</p>
<h3>Hash Algorithms</h3>
<p>The following hash algorithms are supported: </p>
<pre>%(algo) &lt;ext&gt; Description
------- ----- -----------
MD5 .md5 Message-Digest Algorithm 5, RFC 1321
SHA1 .sha1 US Secure Hash Algorithm 1, RFC 3174
SHA224 .sha224 US Secure Hash Algorithms, RFC 4634
SHA256 .sha256 US Secure Hash Algorithms, RFC 4634
SHA384 .sha384 US Secure Hash Algorithms, RFC 4634
SHA512 .sha512 US Secure Hash Algorithms, RFC 4634
SHA3_224 .sha3-224 Keccak SHA-3
SHA3_256 .sha3-256 Keccak SHA-3
SHA3_384 .sha3-384 Keccak SHA-3
SHA3_512 .sha3-512 Keccak SHA-3</pre>
<p>New in version 3.8: Added the <code>SHA3_*</code> hash algorithms. </p>
<p> Note that the hashes are used only for unique data identification and download verification.</p>
<h3>Custom Fetch Scripts</h3>
<p>New in version 3.2. </p>
<p> When a data file must be fetched from one of the URL templates specified in the <code>ExternalData_URL_TEMPLATES</code> variable, it is normally downloaded using the <code>file(DOWNLOAD)</code> command. One may specify usage of a custom fetch script by using a URL template of the form <code>ExternalDataCustomScript://&lt;key&gt;/&lt;loc&gt;</code>. The <code>&lt;key&gt;</code> must be a C identifier, and the <code>&lt;loc&gt;</code> must contain the <code>%(algo)</code> and <code>%(hash)</code> placeholders. A variable corresponding to the key, <code>ExternalData_CUSTOM_SCRIPT_&lt;key&gt;</code>, must be set to the full path to a <code>.cmake</code> script file. The script will be included to perform the actual fetch, and provided with the following variables:</p>
<dl>
<dt><code>ExternalData_CUSTOM_LOCATION</code></p>
<dd>When a custom fetch script is loaded, this variable is set to the location part of the URL, which will contain the substituted hash algorithm name and content hash value.</p>
<dt><code>ExternalData_CUSTOM_FILE</code></p>
<dd>When a custom fetch script is loaded, this variable is set to the full path to a file in which the script must store the fetched content. The name of the file is unspecified and should not be interpreted in any way. </p>
<p> The custom fetch script is expected to store fetched content in the file or set a variable:</p>
<dt><code>ExternalData_CUSTOM_ERROR</code></p>
<dd>When a custom fetch script fails to fetch the requested content, it must set this variable to a short one-line message describing the reason for failure.</dl>
<h3>ExternalProject</h3>
<h3>Commands</h3>
<h3>External Project Definition</h3>
<dl>
<dt><code>ExternalProject_Add</code></p>
<dd>The <code>ExternalProject_Add()</code> function creates a custom target to drive download, update/patch, configure, build, install and test steps of an external project: </p>
<pre>ExternalProject_Add(&lt;name&gt; [&lt;option&gt;...])</pre>
<p>The individual steps within the process can be driven independently if required (e.g. for CDash submission) and extra custom steps can be defined, along with the ability to control the step dependencies. The directory structure used for the management of the external project can also be customized. The function supports a large number of options which can be used to tailor the external project behavior.</p>
<dt><code>Directory Options:</code></p>
<dd>Most of the time, the default directory layout is sufficient. It is largely an implementation detail that the main project usually doesn&#8217;t need to change. In some circumstances, however, control over the directory layout can be useful or necessary. The directory options are potentially more useful from the point of view that the main build can use the <i>ExternalProject_Get_Property()</i> command to retrieve their values, thereby allowing the main project to refer to build artifacts of the external project.</p>
<dt><code>PREFIX &lt;dir&gt;</code></p>
<dd>Root directory for the external project. Unless otherwise noted below, all other directories associated with the external project will be created under here.</p>
<dt><code>TMP_DIR &lt;dir&gt;</code></p>
<dd>Directory in which to store temporary files.</p>
<dt><code>STAMP_DIR &lt;dir&gt;</code></p>
<dd>Directory in which to store the timestamps of each step. Log files from individual steps are also created in here unless overridden by LOG_DIR (see <i>Logging Options</i> below).</p>
<dt><code>LOG_DIR &lt;dir&gt;</code></p>
<dd>New in version 3.14. </p>
<p> Directory in which to store the logs of each step.</p>
<dt><code>DOWNLOAD_DIR &lt;dir&gt;</code></p>
<dd>Directory in which to store downloaded files before unpacking them. This directory is only used by the URL download method, all other download methods use <code>SOURCE_DIR</code> directly instead.</p>
<dt><code>SOURCE_DIR &lt;dir&gt;</code></p>
<dd>Source directory into which downloaded contents will be unpacked, or for non-URL download methods, the directory in which the repository should be checked out, cloned, etc. If no download method is specified, this must point to an existing directory where the external project has already been unpacked or cloned/checked out. </p>
<p> <code>NOTE:</code> If a download method is specified, any existing contents of the source directory may be deleted. Only the URL download method checks whether this directory is either missing or empty before initiating the download, stopping with an error if it is not empty. All other download methods silently discard any previous contents of the source directory.</p>
<dt><code>BINARY_DIR &lt;dir&gt;</code></p>
<dd>Specify the build directory location. This option is ignored if <code>BUILD_IN_SOURCE</code> is enabled.</p>
<dt><code>INSTALL_DIR &lt;dir&gt;</code></p>
<dd>Installation prefix to be placed in the <code>&lt;INSTALL_DIR&gt;</code> placeholder. This does not actually configure the external project to install to the given prefix. That must be done by passing appropriate arguments to the external project configuration step, e.g. using <code>&lt;INSTALL_DIR&gt;</code>. </p>
<p> If any of the above <code>&#8230;_DIR</code> options are not specified, their defaults are computed as follows. If the <code>PREFIX</code> option is given or the <code>EP_PREFIX</code> directory property is set, then an external project is built and installed under the specified prefix: </p>
<pre>TMP_DIR = &lt;prefix&gt;/tmp
STAMP_DIR = &lt;prefix&gt;/src/&lt;name&gt;-stamp
DOWNLOAD_DIR = &lt;prefix&gt;/src
SOURCE_DIR = &lt;prefix&gt;/src/&lt;name&gt;
BINARY_DIR = &lt;prefix&gt;/src/&lt;name&gt;-build
INSTALL_DIR = &lt;prefix&gt;
LOG_DIR = &lt;STAMP_DIR&gt;</pre>
<p>Otherwise, if the <code>EP_BASE</code> directory property is set then components of an external project are stored under the specified base: </p>
<pre>TMP_DIR = &lt;base&gt;/tmp/&lt;name&gt;
STAMP_DIR = &lt;base&gt;/Stamp/&lt;name&gt;
DOWNLOAD_DIR = &lt;base&gt;/Download/&lt;name&gt;
SOURCE_DIR = &lt;base&gt;/Source/&lt;name&gt;
BINARY_DIR = &lt;base&gt;/Build/&lt;name&gt;
INSTALL_DIR = &lt;base&gt;/Install/&lt;name&gt;
LOG_DIR = &lt;STAMP_DIR&gt;</pre>
<p>If no <code>PREFIX</code>, <code>EP_PREFIX</code>, or <code>EP_BASE</code> is specified, then the default is to set <code>PREFIX</code> to <code>&lt;name&gt;-prefix</code>. Relative paths are interpreted with respect to <code>CMAKE_CURRENT_BINARY_DIR</code> at the point where <code>ExternalProject_Add()</code> is called.</p>
<dt><code>Download Step Options:</code></p>
<dd>A download method can be omitted if the <code>SOURCE_DIR</code> option is used to point to an existing non-empty directory. Otherwise, one of the download methods below must be specified (multiple download methods should not be given) or a custom <code>DOWNLOAD_COMMAND</code> provided.</p>
<dt><code>DOWNLOAD_COMMAND &lt;cmd&gt;&#8230;</code></p>
<dd>Overrides the command used for the download step (<code>generator expressions</code> are supported). If this option is specified, all other download options will be ignored. Providing an empty string for <code>&lt;cmd&gt;</code> effectively disables the download step.</p>
<dt><i>URL Download</i></p>
<dd>
<dt><code>URL &lt;url1&gt; [&lt;url2&gt;&#8230;]</code></p>
<dd>List of paths and/or URL(s) of the external project&#8217;s source. When more than one URL is given, they are tried in turn until one succeeds. A URL may be an ordinary path in the local file system (in which case it must be the only URL provided) or any downloadable URL supported by the <code>file(DOWNLOAD)</code> command. A local filesystem path may refer to either an existing directory or to an archive file, whereas a URL is expected to point to a file which can be treated as an archive. When an archive is used, it will be unpacked automatically unless the <code>DOWNLOAD_NO_EXTRACT</code> option is set to prevent it. The archive type is determined by inspecting the actual content rather than using logic based on the file extension. </p>
<p> Changed in version 3.7: Multiple URLs are allowed. </p>
<dt><code>URL_HASH &lt;algo&gt;=&lt;hashValue&gt;</code></p>
<dd>Hash of the archive file to be downloaded. The argument should be of the form <code>&lt;algo&gt;=&lt;hashValue&gt;</code> where <code>algo</code> can be any of the hashing algorithms supported by the <code>file()</code> command. Specifying this option is strongly recommended for URL downloads, as it ensures the integrity of the downloaded content. It is also used as a check for a previously downloaded file, allowing connection to the remote location to be avoided altogether if the local directory already has a file from an earlier download that matches the specified hash.</p>
<dt><code>URL_MD5 &lt;md5&gt;</code></p>
<dd>Equivalent to <code>URL_HASH MD5=&lt;md5&gt;</code>.</p>
<dt><code>DOWNLOAD_NAME &lt;fname&gt;</code></p>
<dd>File name to use for the downloaded file. If not given, the end of the URL is used to determine the file name. This option is rarely needed, the default name is generally suitable and is not normally used outside of code internal to the <code>ExternalProject</code> module.</p>
<dt><code>DOWNLOAD_NO_EXTRACT &lt;bool&gt;</code></p>
<dd>New in version 3.6. </p>
<p> Allows the extraction part of the download step to be disabled by passing a boolean true value for this option. If this option is not given, the downloaded contents will be unpacked automatically if required. If extraction has been disabled, the full path to the downloaded file is available as <code>&lt;DOWNLOADED_FILE&gt;</code> in subsequent steps or as the property <code>DOWNLOADED_FILE</code> with the <i>ExternalProject_Get_Property()</i> command.</p>
<dt><code>DOWNLOAD_NO_PROGRESS &lt;bool&gt;</code></p>
<dd>Can be used to disable logging the download progress. If this option is not given, download progress messages will be logged.</p>
<dt><code>TIMEOUT &lt;seconds&gt;</code></p>
<dd>Maximum time allowed for file download operations.</p>
<dt><code>INACTIVITY_TIMEOUT &lt;seconds&gt;</code></p>
<dd>New in version 3.19. </p>
<p> Terminate the operation after a period of inactivity.</p>
<dt><code>HTTP_USERNAME &lt;username&gt;</code></p>
<dd>New in version 3.7. </p>
<p> Username for the download operation if authentication is required.</p>
<dt><code>HTTP_PASSWORD &lt;password&gt;</code></p>
<dd>New in version 3.7. </p>
<p> Password for the download operation if authentication is required.</p>
<dt><code>HTTP_HEADER &lt;header1&gt; [&lt;header2&gt;&#8230;]</code></p>
<dd>New in version 3.7. </p>
<p> Provides an arbitrary list of HTTP headers for the download operation. This can be useful for accessing content in systems like AWS, etc.</p>
<dt><code>TLS_VERIFY &lt;bool&gt;</code></p>
<dd>Specifies whether certificate verification should be performed for https URLs. If this option is not provided, the default behavior is determined by the <code>CMAKE_TLS_VERIFY</code> variable (see <code>file(DOWNLOAD)</code>). If that is also not set, certificate verification will not be performed. In situations where <code>URL_HASH</code> cannot be provided, this option can be an alternative verification measure. </p>
<p> Changed in version 3.6: This option also applies to <code>git clone</code> invocations. </p>
<dt><code>TLS_CAINFO &lt;file&gt;</code></p>
<dd>Specify a custom certificate authority file to use if <code>TLS_VERIFY</code> is enabled. If this option is not specified, the value of the <code>CMAKE_TLS_CAINFO</code> variable will be used instead (see <code>file(DOWNLOAD)</code>)</p>
<dt><code>NETRC &lt;level&gt;</code></p>
<dd>New in version 3.11. </p>
<p> Specify whether the <code>.netrc</code> file is to be used for operation. If this option is not specified, the value of the <code>CMAKE_NETRC</code> variable will be used instead (see <code>file(DOWNLOAD)</code>) Valid levels are:</p>
<dt><code>IGNORED</code></p>
<dd>The <code>.netrc</code> file is ignored. This is the default.</p>
<dt><code>OPTIONAL</code></p>
<dd>The <code>.netrc</code> file is optional, and information in the URL is preferred. The file will be scanned to find which ever information is not specified in the URL.</p>
<dt><code>REQUIRED</code></p>
<dd>The <code>.netrc</code> file is required, and information in the URL is ignored.</p>
<dt><code>NETRC_FILE &lt;file&gt;</code></p>
<dd>New in version 3.11. </p>
<p> Specify an alternative <code>.netrc</code> file to the one in your home directory if the <code>NETRC</code> level is <code>OPTIONAL</code> or <code>REQUIRED</code>. If this option is not specified, the value of the <code>CMAKE_NETRC_FILE</code> variable will be used instead (see <code>file(DOWNLOAD)</code>) </p>
<p> New in version 3.1: Added support for <i>tbz2</i>, <i>.tar.xz</i>, <i>.txz</i>, and <i>.7z</i> extensions. </p>
<dt><i>Git</i></p>
<dd>NOTE: A git version of 1.6.5 or later is required if this download method is used.</p>
<dt><code>GIT_REPOSITORY &lt;url&gt;</code></p>
<dd>URL of the git repository. Any URL understood by the <code>git</code> command may be used.</p>
<dt><code>GIT_TAG &lt;tag&gt;</code></p>
<dd>Git branch name, tag or commit hash. Note that branch names and tags should generally be specified as remote names (i.e. <code>origin/myBranch</code> rather than simply <code>myBranch</code>). This ensures that if the remote end has its tag moved or branch rebased or history rewritten, the local clone will still be updated correctly. In general, however, specifying a commit hash should be preferred for a number of reasons:</p>
<dt>&bull;</p>
<dd>If the local clone already has the commit corresponding to the hash, no <code>git fetch</code> needs to be performed to check for changes each time CMake is re-run. This can result in a significant speed up if many external projects are being used.</p>
<dt>&bull;</p>
<dd>Using a specific git hash ensures that the main project&#8217;s own history is fully traceable to a specific point in the external project&#8217;s evolution. If a branch or tag name is used instead, then checking out a specific commit of the main project doesn&#8217;t necessarily pin the whole build to a specific point in the life of the external project. The lack of such deterministic behavior makes the main project lose traceability and repeatability. </p>
<p> If <code>GIT_SHALLOW</code> is enabled then <code>GIT_TAG</code> works only with branch names and tags. A commit hash is not allowed.</p>
<dt><code>GIT_REMOTE_NAME &lt;name&gt;</code></p>
<dd>The optional name of the remote. If this option is not specified, it defaults to <code>origin</code>.</p>
<dt><code>GIT_SUBMODULES &lt;module&gt;&#8230;</code></p>
<dd>Specific git submodules that should also be updated. If this option is not provided, all git submodules will be updated. </p>
<p> Changed in version 3.16: When <code>CMP0097</code> is set to <code>NEW</code>, if this value is set to an empty string then no submodules are initialized or updated. </p>
<dt><code>GIT_SUBMODULES_RECURSE &lt;bool&gt;</code></p>
<dd>New in version 3.17. </p>
<p> Specify whether git submodules (if any) should update recursively by passing the <code>&#8211;recursive</code> flag to <code>git submodule update</code>. If not specified, the default is on.</p>
<dt><code>GIT_SHALLOW &lt;bool&gt;</code></p>
<dd>New in version 3.6. </p>
<p> When this option is enabled, the <code>git clone</code> operation will be given the <code>&#8211;depth 1</code> option. This performs a shallow clone, which avoids downloading the whole history and instead retrieves just the commit denoted by the <code>GIT_TAG</code> option.</p>
<dt><code>GIT_PROGRESS &lt;bool&gt;</code></p>
<dd>New in version 3.8. </p>
<p> When enabled, this option instructs the <code>git clone</code> operation to report its progress by passing it the <code>&#8211;progress</code> option. Without this option, the clone step for large projects may appear to make the build stall, since nothing will be logged until the clone operation finishes. While this option can be used to provide progress to prevent the appearance of the build having stalled, it may also make the build overly noisy if lots of external projects are used.</p>
<dt><code>GIT_CONFIG &lt;option1&gt; [&lt;option2&gt;&#8230;]</code></p>
<dd>New in version 3.8. </p>
<p> Specify a list of config options to pass to <code>git clone</code>. Each option listed will be transformed into its own <code>&#8211;config &lt;option&gt;</code> on the <code>git clone</code> command line, with each option required to be in the form <code>key=value</code>.</p>
<dt><code>GIT_REMOTE_UPDATE_STRATEGY &lt;strategy&gt;</code></p>
<dd>New in version 3.18. </p>
<p> When <code>GIT_TAG</code> refers to a remote branch, this option can be used to specify how the update step behaves. The <code>&lt;strategy&gt;</code> must be one of the following:</p>
<dt><code>CHECKOUT</code></p>
<dd>Ignore the local branch and always checkout the branch specified by <code>GIT_TAG</code>.</p>
<dt><code>REBASE</code></p>
<dd>Try to rebase the current branch to the one specified by <code>GIT_TAG</code>. If there are local uncommitted changes, they will be stashed first and popped again after rebasing. If rebasing or popping stashed changes fail, abort the rebase and halt with an error. When <code>GIT_REMOTE_UPDATE_STRATEGY</code> is not present, this is the default strategy unless the default has been overridden with <code>CMAKE_EP_GIT_REMOTE_UPDATE_STRATEGY</code> (see below).</p>
<dt><code>REBASE_CHECKOUT</code></p>
<dd>Same as <code>REBASE</code> except if the rebase fails, an annotated tag will be created at the original <code>HEAD</code> position from before the rebase and then checkout <code>GIT_TAG</code> just like the <code>CHECKOUT</code> strategy. The message stored on the annotated tag will give information about what was attempted and the tag name will include a timestamp so that each failed run will add a new tag. This strategy ensures no changes will be lost, but updates should always succeed if <code>GIT_TAG</code> refers to a valid ref unless there are uncommitted changes that cannot be popped successfully. </p>
<p> The variable <code>CMAKE_EP_GIT_REMOTE_UPDATE_STRATEGY</code> can be set to override the default strategy. This variable should not be set by a project, it is intended for the user to set. It is primarily intended for use in continuous integration scripts to ensure that when history is rewritten on a remote branch, the build doesn&#8217;t end up with unintended changes or failed builds resulting from conflicts during rebase operations.</p>
<dt><i>Subversion</i></p>
<dd>
<dt><code>SVN_REPOSITORY &lt;url&gt;</code></p>
<dd>URL of the Subversion repository.</p>
<dt><code>SVN_REVISION -r&lt;rev&gt;</code></p>
<dd>Revision to checkout from the Subversion repository.</p>
<dt><code>SVN_USERNAME &lt;username&gt;</code></p>
<dd>Username for the Subversion checkout and update.</p>
<dt><code>SVN_PASSWORD &lt;password&gt;</code></p>
<dd>Password for the Subversion checkout and update.</p>
<dt><code>SVN_TRUST_CERT &lt;bool&gt;</code></p>
<dd>Specifies whether to trust the Subversion server site certificate. If enabled, the <code>&#8211;trust-server-cert</code> option is passed to the <code>svn</code> checkout and update commands.</p>
<dt><i>Mercurial</i></p>
<dd>
<dt><code>HG_REPOSITORY &lt;url&gt;</code></p>
<dd>URL of the mercurial repository.</p>
<dt><code>HG_TAG &lt;tag&gt;</code></p>
<dd>Mercurial branch name, tag or commit id.</p>
<dt><i>CVS</i></p>
<dd>
<dt><code>CVS_REPOSITORY &lt;cvsroot&gt;</code></p>
<dd>CVSROOT of the CVS repository.</p>
<dt><code>CVS_MODULE &lt;mod&gt;</code></p>
<dd>Module to checkout from the CVS repository.</p>
<dt><code>CVS_TAG &lt;tag&gt;</code></p>
<dd>Tag to checkout from the CVS repository.</p>
<dt><code>Update/Patch Step Options:</code></p>
<dd>Whenever CMake is re-run, by default the external project&#8217;s sources will be updated if the download method supports updates (e.g. a git repository would be checked if the <code>GIT_TAG</code> does not refer to a specific commit).</p>
<dt><code>UPDATE_COMMAND &lt;cmd&gt;&#8230;</code></p>
<dd>Overrides the download method&#8217;s update step with a custom command. The command may use <code>generator expressions</code>.</p>
<dt><code>UPDATE_DISCONNECTED &lt;bool&gt;</code></p>
<dd>New in version 3.2. </p>
<p> When enabled, this option causes the update step to be skipped. It does not, however, prevent the download step. The update step can still be added as a step target (see <i>ExternalProject_Add_StepTargets()</i>) and called manually. This is useful if you want to allow developers to build the project when disconnected from the network (the network may still be needed for the download step though). </p>
<p> When this option is present, it is generally advisable to make the value a cache variable under the developer&#8217;s control rather than hard-coding it. If this option is not present, the default value is taken from the <code>EP_UPDATE_DISCONNECTED</code> directory property. If that is also not defined, updates are performed as normal. The <code>EP_UPDATE_DISCONNECTED</code> directory property is intended as a convenience for controlling the <code>UPDATE_DISCONNECTED</code> behavior for an entire section of a project&#8217;s directory hierarchy and may be a more convenient method of giving developers control over whether or not to perform updates (assuming the project also provides a cache variable or some other convenient method for setting the directory property). </p>
<p> This may cause a step target to be created automatically for the <code>download</code> step. See policy <code>CMP0114</code>.</p>
<dt><code>PATCH_COMMAND &lt;cmd&gt;&#8230;</code></p>
<dd>Specifies a custom command to patch the sources after an update. By default, no patch command is defined. Note that it can be quite difficult to define an appropriate patch command that performs robustly, especially for download methods such as git where changing the <code>GIT_TAG</code> will not discard changes from a previous patch, but the patch command will be called again after updating to the new tag.</p>
<dt><code>Configure Step Options:</code></p>
<dd>The configure step is run after the download and update steps. By default, the external project is assumed to be a CMake project, but this can be overridden if required.</p>
<dt><code>CONFIGURE_COMMAND &lt;cmd&gt;&#8230;</code></p>
<dd>The default configure command runs CMake with a few options based on the main project. The options added are typically only those needed to use the same generator as the main project, but the <code>CMAKE_GENERATOR</code> option can be given to override this. The project is responsible for adding any toolchain details, flags or other settings it wants to re-use from the main project or otherwise specify (see <code>CMAKE_ARGS</code>, <code>CMAKE_CACHE_ARGS</code> and <code>CMAKE_CACHE_DEFAULT_ARGS</code> below). </p>
<p> For non-CMake external projects, the <code>CONFIGURE_COMMAND</code> option must be used to override the default configure command (<code>generator expressions</code> are supported). For projects that require no configure step, specify this option with an empty string as the command to execute.</p>
<dt><code>CMAKE_COMMAND /&#8230;/cmake</code></p>
<dd>Specify an alternative cmake executable for the configure step (use an absolute path). This is generally not recommended, since it is usually desirable to use the same CMake version throughout the whole build. This option is ignored if a custom configure command has been specified with <code>CONFIGURE_COMMAND</code>.</p>
<dt><code>CMAKE_GENERATOR &lt;gen&gt;</code></p>
<dd>Override the CMake generator used for the configure step. Without this option, the same generator as the main build will be used. This option is ignored if a custom configure command has been specified with the <code>CONFIGURE_COMMAND</code> option.</p>
<dt><code>CMAKE_GENERATOR_PLATFORM &lt;platform&gt;</code></p>
<dd>New in version 3.1. </p>
<p> Pass a generator-specific platform name to the CMake command (see <code>CMAKE_GENERATOR_PLATFORM</code>). It is an error to provide this option without the <code>CMAKE_GENERATOR</code> option.</p>
<dt><code>CMAKE_GENERATOR_TOOLSET &lt;toolset&gt;</code></p>
<dd>Pass a generator-specific toolset name to the CMake command (see <code>CMAKE_GENERATOR_TOOLSET</code>). It is an error to provide this option without the <code>CMAKE_GENERATOR</code> option.</p>
<dt><code>CMAKE_GENERATOR_INSTANCE &lt;instance&gt;</code></p>
<dd>New in version 3.11. </p>
<p> Pass a generator-specific instance selection to the CMake command (see <code>CMAKE_GENERATOR_INSTANCE</code>). It is an error to provide this option without the <code>CMAKE_GENERATOR</code> option.</p>
<dt><code>CMAKE_ARGS &lt;arg&gt;&#8230;</code></p>
<dd>The specified arguments are passed to the <code>cmake</code> command line. They can be any argument the <code>cmake</code> command understands, not just cache values defined by <code>-D&#8230;</code> arguments (see also <code>CMake Options</code>). </p>
<p> New in version 3.3: Arguments may use <code>generator expressions</code>. </p>
<dt><code>CMAKE_CACHE_ARGS &lt;arg&gt;&#8230;</code></p>
<dd>This is an alternate way of specifying cache variables where command line length issues may become a problem. The arguments are expected to be in the form <code>-Dvar:STRING=value</code>, which are then transformed into CMake <code>set()</code> commands with the <code>FORCE</code> option used. These <code>set()</code> commands are written to a pre-load script which is then applied using the <code>cmake -C</code> command line option. </p>
<p> New in version 3.3: Arguments may use <code>generator expressions</code>. </p>
<dt><code>CMAKE_CACHE_DEFAULT_ARGS &lt;arg&gt;&#8230;</code></p>
<dd>New in version 3.2. </p>
<p> This is the same as the <code>CMAKE_CACHE_ARGS</code> option except the <code>set()</code> commands do not include the <code>FORCE</code> keyword. This means the values act as initial defaults only and will not override any variables already set from a previous run. Use this option with care, as it can lead to different behavior depending on whether the build starts from a fresh build directory or re-uses previous build contents. </p>
<p> New in version 3.15: If the CMake generator is the <code>Green Hills MULTI</code> and not overridden then the original project&#8217;s settings for the GHS toolset and target system customization cache variables are propagated into the external project. </p>
<dt><code>SOURCE_SUBDIR &lt;dir&gt;</code></p>
<dd>New in version 3.7. </p>
<p> When no <code>CONFIGURE_COMMAND</code> option is specified, the configure step assumes the external project has a <code>CMakeLists.txt</code> file at the top of its source tree (i.e. in <code>SOURCE_DIR</code>). The <code>SOURCE_SUBDIR</code> option can be used to point to an alternative directory within the source tree to use as the top of the CMake source tree instead. This must be a relative path and it will be interpreted as being relative to <code>SOURCE_DIR</code>. </p>
<p> New in version 3.14: When <code>BUILD_IN_SOURCE</code> option is enabled, the <code>BUILD_COMMAND</code> is used to point to an alternative directory within the source tree. </p>
<dt><code>CONFIGURE_HANDLED_BY_BUILD &lt;bool&gt;</code></p>
<dd>New in version 3.20. </p>
<p> Enabling this option relaxes the dependencies of the configure step on other external projects to order-only. This means the configure step will be executed after its external project dependencies are built but it will not be marked dirty when one of its external project dependencies is rebuilt. This option can be enabled when the build step is smart enough to figure out if the configure step needs to be rerun. CMake and Meson are examples of build systems whose build step is smart enough to know if the configure step needs to be rerun.</p>
<dt><code>Build Step Options:</code></p>
<dd>If the configure step assumed the external project uses CMake as its build system, the build step will also. Otherwise, the build step will assume a Makefile-based build and simply run <code>make</code> with no arguments as the default build step. This can be overridden with custom build commands if required. </p>
<p> If both the main project and the external project use make as their build tool, the build step of the external project is invoked as a recursive make using <code>$(MAKE)</code>. This will communicate some build tool settings from the main project to the external project. If either the main project or external project is not using make, no build tool settings will be passed to the external project other than those established by the configure step (i.e. running <code>ninja -v</code> in the main project will not pass <code>-v</code> to the external project&#8217;s build step, even if it also uses <code>ninja</code> as its build tool).</p>
<dt><code>BUILD_COMMAND &lt;cmd&gt;&#8230;</code></p>
<dd>Overrides the default build command (<code>generator expressions</code> are supported). If this option is not given, the default build command will be chosen to integrate with the main build in the most appropriate way (e.g. using recursive <code>make</code> for Makefile generators or <code>cmake &#8211;build</code> if the project uses a CMake build). This option can be specified with an empty string as the command to make the build step do nothing.</p>
<dt><code>BUILD_IN_SOURCE &lt;bool&gt;</code></p>
<dd>When this option is enabled, the build will be done directly within the external project&#8217;s source tree. This should generally be avoided, the use of a separate build directory is usually preferred, but it can be useful when the external project assumes an in-source build. The <code>BINARY_DIR</code> option should not be specified if building in-source.</p>
<dt><code>BUILD_ALWAYS &lt;bool&gt;</code></p>
<dd>Enabling this option forces the build step to always be run. This can be the easiest way to robustly ensure that the external project&#8217;s own build dependencies are evaluated rather than relying on the default success timestamp-based method. This option is not normally needed unless developers are expected to modify something the external project&#8217;s build depends on in a way that is not detectable via the step target dependencies (e.g. <code>SOURCE_DIR</code> is used without a download method and developers might modify the sources in <code>SOURCE_DIR</code>).</p>
<dt><code>BUILD_BYPRODUCTS &lt;file&gt;&#8230;</code></p>
<dd>New in version 3.2. </p>
<p> Specifies files that will be generated by the build command but which might or might not have their modification time updated by subsequent builds. These ultimately get passed through as <code>BYPRODUCTS</code> to the build step&#8217;s own underlying call to <code>add_custom_command()</code>.</p>
<dt><code>Install Step Options:</code></p>
<dd>If the configure step assumed the external project uses CMake as its build system, the install step will also. Otherwise, the install step will assume a Makefile-based build and simply run <code>make install</code> as the default build step. This can be overridden with custom install commands if required.</p>
<dt><code>INSTALL_COMMAND &lt;cmd&gt;&#8230;</code></p>
<dd>The external project&#8217;s own install step is invoked as part of the main project&#8217;s <i>build</i>. It is done after the external project&#8217;s build step and may be before or after the external project&#8217;s test step (see the <code>TEST_BEFORE_INSTALL</code> option below). The external project&#8217;s install rules are not part of the main project&#8217;s install rules, so if anything from the external project should be installed as part of the main build, these need to be specified in the main build as additional <code>install()</code> commands. The default install step builds the <code>install</code> target of the external project, but this can be overridden with a custom command using this option (<code>generator expressions</code> are supported). Passing an empty string as the <code>&lt;cmd&gt;</code> makes the install step do nothing. </p>
<p> <code>NOTE:</code> If the <code>CMAKE_INSTALL_MODE</code> environment variable is set when the main project is built, it will only have an effect if the following conditions are met:</p>
<dt>&bull;</p>
<dd>The main project&#8217;s configure step assumed the external project uses CMake as its build system.</p>
<dt>&bull;</p>
<dd>The external project&#8217;s install command actually runs. Note that due to the way <code>ExternalProject</code> may use timestamps internally, if nothing the install step depends on needs to be re-executed, the install command might also not need to run. </p>
<p> Note also that <code>ExternalProject</code> does not check whether the <code>CMAKE_INSTALL_MODE</code> environment variable changes from one run to another.</p>
<dt><code>Test Step Options:</code></p>
<dd>The test step is only defined if at least one of the following <code>TEST_&#8230;</code> options are provided.</p>
<dt><code>TEST_COMMAND &lt;cmd&gt;&#8230;</code></p>
<dd>Overrides the default test command (<code>generator expressions</code> are supported). If this option is not given, the default behavior of the test step is to build the external project&#8217;s own <code>test</code> target. This option can be specified with <code>&lt;cmd&gt;</code> as an empty string, which allows the test step to still be defined, but it will do nothing. Do not specify any of the other <code>TEST_&#8230;</code> options if providing an empty string as the test command, but prefer to omit all <code>TEST_&#8230;</code> options altogether if the test step target is not needed.</p>
<dt><code>TEST_BEFORE_INSTALL &lt;bool&gt;</code></p>
<dd>When this option is enabled, the test step will be executed before the install step. The default behavior is for the test step to run after the install step.</p>
<dt><code>TEST_AFTER_INSTALL &lt;bool&gt;</code></p>
<dd>This option is mainly useful as a way to indicate that the test step is desired but all default behavior is sufficient. Specifying this option with a boolean true value ensures the test step is defined and that it comes after the install step. If both <code>TEST_BEFORE_INSTALL</code> and <code>TEST_AFTER_INSTALL</code> are enabled, the latter is silently ignored.</p>
<dt><code>TEST_EXCLUDE_FROM_MAIN &lt;bool&gt;</code></p>
<dd>New in version 3.2. </p>
<p> If enabled, the main build&#8217;s default ALL target will not depend on the test step. This can be a useful way of ensuring the test step is defined but only gets invoked when manually requested. This may cause a step target to be created automatically for either the <code>install</code> or <code>build</code> step. See policy <code>CMP0114</code>.</p>
<dt><code>Output Logging Options:</code></p>
<dd>Each of the following <code>LOG_&#8230;</code> options can be used to wrap the relevant step in a script to capture its output to files. The log files will be created in <code>LOG_DIR</code> if supplied or otherwise the <code>STAMP_DIR</code> directory with step-specific file names.</p>
<dt><code>LOG_DOWNLOAD &lt;bool&gt;</code></p>
<dd>When enabled, the output of the download step is logged to files.</p>
<dt><code>LOG_UPDATE &lt;bool&gt;</code></p>
<dd>When enabled, the output of the update step is logged to files.</p>
<dt><code>LOG_PATCH &lt;bool&gt;</code></p>
<dd>New in version 3.14. </p>
<p> When enabled, the output of the patch step is logged to files.</p>
<dt><code>LOG_CONFIGURE &lt;bool&gt;</code></p>
<dd>When enabled, the output of the configure step is logged to files.</p>
<dt><code>LOG_BUILD &lt;bool&gt;</code></p>
<dd>When enabled, the output of the build step is logged to files.</p>
<dt><code>LOG_INSTALL &lt;bool&gt;</code></p>
<dd>When enabled, the output of the install step is logged to files.</p>
<dt><code>LOG_TEST &lt;bool&gt;</code></p>
<dd>When enabled, the output of the test step is logged to files.</p>
<dt><code>LOG_MERGED_STDOUTERR &lt;bool&gt;</code></p>
<dd>New in version 3.14. </p>
<p> When enabled, stdout and stderr will be merged for any step whose output is being logged to files.</p>
<dt><code>LOG_OUTPUT_ON_FAILURE &lt;bool&gt;</code></p>
<dd>New in version 3.14. </p>
<p> This option only has an effect if at least one of the other <code>LOG_&lt;step&gt;</code> options is enabled. If an error occurs for a step which has logging to file enabled, that step&#8217;s output will be printed to the console if <code>LOG_OUTPUT_ON_FAILURE</code> is set to true. For cases where a large amount of output is recorded, just the end of that output may be printed to the console.</p>
<dt><code>Terminal Access Options:</code></p>
<dd>New in version 3.4. </p>
<p> Steps can be given direct access to the terminal in some cases. Giving a step access to the terminal may allow it to receive terminal input if required, such as for authentication details not provided by other options. With the <code>Ninja</code> generator, these options place the steps in the <code>console</code> <code>job pool</code>. Each step can be given access to the terminal individually via the following options:</p>
<dt><code>USES_TERMINAL_DOWNLOAD &lt;bool&gt;</code></p>
<dd>Give the download step access to the terminal.</p>
<dt><code>USES_TERMINAL_UPDATE &lt;bool&gt;</code></p>
<dd>Give the update step access to the terminal.</p>
<dt><code>USES_TERMINAL_CONFIGURE &lt;bool&gt;</code></p>
<dd>Give the configure step access to the terminal.</p>
<dt><code>USES_TERMINAL_BUILD &lt;bool&gt;</code></p>
<dd>Give the build step access to the terminal.</p>
<dt><code>USES_TERMINAL_INSTALL &lt;bool&gt;</code></p>
<dd>Give the install step access to the terminal.</p>
<dt><code>USES_TERMINAL_TEST &lt;bool&gt;</code></p>
<dd>Give the test step access to the terminal.</p>
<dt><code>Target Options:</code></p>
<dd>
<dt><code>DEPENDS &lt;targets&gt;&#8230;</code></p>
<dd>Specify other targets on which the external project depends. The other targets will be brought up to date before any of the external project&#8217;s steps are executed. Because the external project uses additional custom targets internally for each step, the <code>DEPENDS</code> option is the most convenient way to ensure all of those steps depend on the other targets. Simply doing <code>add_dependencies(&lt;name&gt; &lt;targets&gt;)</code> will not make any of the steps dependent on <code>&lt;targets&gt;</code>.</p>
<dt><code>EXCLUDE_FROM_ALL &lt;bool&gt;</code></p>
<dd>When enabled, this option excludes the external project from the default ALL target of the main build.</p>
<dt><code>STEP_TARGETS &lt;step-target&gt;&#8230;</code></p>
<dd>Generate custom targets for the specified steps. This is required if the steps need to be triggered manually or if they need to be used as dependencies of other targets. If this option is not specified, the default value is taken from the <code>EP_STEP_TARGETS</code> directory property. See <i>ExternalProject_Add_StepTargets()</i> below for further discussion of the effects of this option.</p>
<dt><code>INDEPENDENT_STEP_TARGETS &lt;step-target&gt;&#8230;</code></p>
<dd>Deprecated since version 3.19: This is allowed only if policy <code>CMP0114</code> is not set to <code>NEW</code>. </p>
<p> Generates custom targets for the specified steps and prevent these targets from having the usual dependencies applied to them. If this option is not specified, the default value is taken from the <code>EP_INDEPENDENT_STEP_TARGETS</code> directory property. This option is mostly useful for allowing individual steps to be driven independently, such as for a CDash setup where each step should be initiated and reported individually rather than as one whole build. See <i>ExternalProject_Add_StepTargets()</i> below for further discussion of the effects of this option.</p>
<dt><code>Miscellaneous Options:</code></p>
<dd>
<dt><code>LIST_SEPARATOR &lt;sep&gt;</code></p>
<dd>For any of the various <code>&#8230;_COMMAND</code> options, replace <code>;</code> with <code>&lt;sep&gt;</code> in the specified command lines. This can be useful where list variables may be given in commands where they should end up as space-separated arguments (<code>&lt;sep&gt;</code> would be a single space character string in this case).</p>
<dt><code>COMMAND &lt;cmd&gt;&#8230;</code></p>
<dd>Any of the other <code>&#8230;_COMMAND</code> options can have additional commands appended to them by following them with as many <code>COMMAND &#8230;</code> options as needed (<code>generator expressions</code> are supported). For example: </p>
<pre>ExternalProject_Add(example
 ... # Download options, etc.
 BUILD_COMMAND ${CMAKE_COMMAND} -E echo &quot;Starting $&lt;CONFIG&gt; build&quot;
 COMMAND ${CMAKE_COMMAND} --build &lt;BINARY_DIR&gt; --config $&lt;CONFIG&gt;
 COMMAND ${CMAKE_COMMAND} -E echo &quot;$&lt;CONFIG&gt; build complete&quot;
)</pre>
<p>It should also be noted that each build step is created via a call to <i>ExternalProject_Add_Step()</i>. See that command&#8217;s documentation for the automatic substitutions that are supported for some options.</dl>
<h3>Obtaining Project Properties</h3>
<dl>
<dt><code>ExternalProject_Get_Property</code></p>
<dd>The <code>ExternalProject_Get_Property()</code> function retrieves external project target properties: </p>
<pre>ExternalProject_Get_Property(&lt;name&gt; &lt;prop1&gt; [&lt;prop2&gt;...])</pre>
<p>The function stores property values in variables of the same name. Property names correspond to the keyword argument names of <code>ExternalProject_Add()</code>. For example, the source directory might be retrieved like so: </p>
<pre>ExternalProject_Get_property(myExtProj SOURCE_DIR)
message(&quot;Source dir of myExtProj = ${SOURCE_DIR}&quot;)</pre>
</dl>
<h3>Explicit Step Management</h3>
<p>The <code>ExternalProject_Add()</code> function on its own is often sufficient for incorporating an external project into the main build. Certain scenarios require additional work to implement desired behavior, such as adding in a custom step or making steps available as manually triggerable targets. The <code>ExternalProject_Add_Step()</code>, <code>ExternalProject_Add_StepTargets()</code> and <code>ExternalProject_Add_StepDependencies</code> functions provide the lower level control needed to implement such step-level capabilities.</p>
<dl>
<dt><code>ExternalProject_Add_Step</code></p>
<dd>The <code>ExternalProject_Add_Step()</code> function specifies an additional custom step for an external project defined by an earlier call to <i>ExternalProject_Add()</i>: </p>
<pre>ExternalProject_Add_Step(&lt;name&gt; &lt;step&gt; [&lt;option&gt;...])</pre>
<p><code>&lt;name&gt;</code> is the same as the name passed to the original call to <i>ExternalProject_Add()</i>. The specified <code>&lt;step&gt;</code> must not be one of the pre-defined steps (<code>mkdir</code>, <code>download</code>, <code>update</code>, <code>patch</code>, <code>configure</code>, <code>build</code>, <code>install</code> or <code>test</code>). The supported options are:</p>
<dt><code>COMMAND &lt;cmd&gt;&#8230;</code></p>
<dd>The command line to be executed by this custom step (<code>generator expressions</code> are supported). This option can be repeated multiple times to specify multiple commands to be executed in order.</p>
<dt><code>COMMENT &lt;text&gt;&#8230;</code></p>
<dd>Text to be printed when the custom step executes.</p>
<dt><code>DEPENDEES &lt;step&gt;&#8230;</code></p>
<dd>Other steps (custom or pre-defined) on which this step depends.</p>
<dt><code>DEPENDERS &lt;step&gt;&#8230;</code></p>
<dd>Other steps (custom or pre-defined) that depend on this new custom step.</p>
<dt><code>DEPENDS &lt;file&gt;&#8230;</code></p>
<dd>Files on which this custom step depends.</p>
<dt><code>INDEPENDENT &lt;bool&gt;</code></p>
<dd>New in version 3.19. </p>
<p> Specifies whether this step is independent of the external dependencies specified by the <i>ExternalProject_Add()</i>&#8216;s <code>DEPENDS</code> option. The default is <code>FALSE</code>. Steps marked as independent may depend only on other steps marked independent. See policy <code>CMP0114</code>. </p>
<p> Note that this use of the term &quot;independent&quot; refers only to independence from external targets specified by the <code>DEPENDS</code> option and is orthogonal to a step&#8217;s dependencies on other steps. </p>
<p> If a step target is created for an independent step by the <i>ExternalProject_Add()</i> <code>STEP_TARGETS</code> option or by the <i>ExternalProject_Add_StepTargets()</i> function, it will not depend on the external targets, but may depend on targets for other steps.</p>
<dt><code>BYPRODUCTS &lt;file&gt;&#8230;</code></p>
<dd>New in version 3.2. </p>
<p> Files that will be generated by this custom step but which might or might not have their modification time updated by subsequent builds. This list of files will ultimately be passed through as the <code>BYPRODUCTS</code> option to the <code>add_custom_command()</code> used to implement the custom step internally.</p>
<dt><code>ALWAYS &lt;bool&gt;</code></p>
<dd>When enabled, this option specifies that the custom step should always be run (i.e. that it is always considered out of date).</p>
<dt><code>EXCLUDE_FROM_MAIN &lt;bool&gt;</code></p>
<dd>When enabled, this option specifies that the external project&#8217;s main target does not depend on the custom step. This may cause step targets to be created automatically for the steps on which this step depends. See policy <code>CMP0114</code>.</p>
<dt><code>WORKING_DIRECTORY &lt;dir&gt;</code></p>
<dd>Specifies the working directory to set before running the custom step&#8217;s command. If this option is not specified, the directory will be the value of the <code>CMAKE_CURRENT_BINARY_DIR</code> at the point where <code>ExternalProject_Add_Step()</code> was called.</p>
<dt><code>LOG &lt;bool&gt;</code></p>
<dd>If set, this causes the output from the custom step to be captured to files in the external project&#8217;s <code>LOG_DIR</code> if supplied or <code>STAMP_DIR</code>.</p>
<dt><code>USES_TERMINAL &lt;bool&gt;</code></p>
<dd>If enabled, this gives the custom step direct access to the terminal if possible. </p>
<p> The command line, comment, working directory and byproducts of every standard and custom step are processed to replace the tokens <code>&lt;SOURCE_DIR&gt;</code>, <code>&lt;SOURCE_SUBDIR&gt;</code>, <code>&lt;BINARY_DIR&gt;</code>, <code>&lt;INSTALL_DIR&gt;</code> <code>&lt;TMP_DIR&gt;</code>, <code>&lt;DOWNLOAD_DIR&gt;</code> and <code>&lt;DOWNLOADED_FILE&gt;</code> with their corresponding property values defined in the original call to <i>ExternalProject_Add()</i>. </p>
<p> New in version 3.3: Token replacement is extended to byproducts. </p>
<p> New in version 3.11: The <code>&lt;DOWNLOAD_DIR&gt;</code> substitution token. </p>
<dt><code>ExternalProject_Add_StepTargets</code></p>
<dd>The <code>ExternalProject_Add_StepTargets()</code> function generates targets for the steps listed. The name of each created target will be of the form <code>&lt;name&gt;-&lt;step&gt;</code>: </p>
<pre>ExternalProject_Add_StepTargets(&lt;name&gt; &lt;step1&gt; [&lt;step2&gt;...])</pre>
<p>Creating a target for a step allows it to be used as a dependency of another target or to be triggered manually. Having targets for specific steps also allows them to be driven independently of each other by specifying targets on build command lines. For example, you may be submitting to a sub-project based dashboard where you want to drive the configure portion of the build, then submit to the dashboard, followed by the build portion, followed by tests. If you invoke a custom target that depends on a step halfway through the step dependency chain, then all the previous steps will also run to ensure everything is up to date. </p>
<p> Internally, <i>ExternalProject_Add()</i> calls <i>ExternalProject_Add_Step()</i> to create each step. If any <code>STEP_TARGETS</code> were specified, then <code>ExternalProject_Add_StepTargets()</code> will also be called after <i>ExternalProject_Add_Step()</i>. Even if a step is not mentioned in the <code>STEP_TARGETS</code> option, <code>ExternalProject_Add_StepTargets()</code> can still be called later to manually define a target for the step. </p>
<p> The <code>STEP_TARGETS</code> option for <i>ExternalProject_Add()</i> is generally the easiest way to ensure targets are created for specific steps of interest. For custom steps, <code>ExternalProject_Add_StepTargets()</code> must be called explicitly if a target should also be created for that custom step. An alternative to these two options is to populate the <code>EP_STEP_TARGETS</code> directory property. It acts as a default for the step target options and can save having to repeatedly specify the same set of step targets when multiple external projects are being defined. </p>
<p> New in version 3.19: If <code>CMP0114</code> is set to <code>NEW</code>, step targets are fully responsible for holding the custom commands implementing their steps. The primary target created by <code>ExternalProject_Add</code> depends on the step targets, and the step targets depend on each other. The target-level dependencies match the file-level dependencies used by the custom commands for each step. The targets for steps created with <i>ExternalProject_Add_Step()</i>&#8216;s <code>INDEPENDENT</code> option do not depend on the external targets specified by <i>ExternalProject_Add()</i>&#8216;s <code>DEPENDS</code> option. The predefined steps <code>mkdir</code>, <code>download</code>, <code>update</code>, and <code>patch</code> are independent. </p>
<p> If <code>CMP0114</code> is not <code>NEW</code>, the following deprecated behavior is available:</p>
<dt>&bull;</p>
<dd>A deprecated <code>NO_DEPENDS</code> option may be specified immediately after the <code>&lt;name&gt;</code> and before the first step. If the <code>NO_DEPENDS</code> option is specified, the step target will not depend on the dependencies of the external project (i.e. on any dependencies of the <code>&lt;name&gt;</code> custom target created by <i>ExternalProject_Add()</i>). This is usually safe for the <code>download</code>, <code>update</code> and <code>patch</code> steps, since they do not typically require that the dependencies are updated and built. Using <code>NO_DEPENDS</code> for any of the other pre-defined steps, however, may break parallel builds. Only use <code>NO_DEPENDS</code> where it is certain that the named steps genuinely do not have dependencies. For custom steps, consider whether or not the custom commands require the dependencies to be configured, built and installed.</p>
<dt>&bull;</p>
<dd>The <code>INDEPENDENT_STEP_TARGETS</code> option for <i>ExternalProject_Add()</i>, or the <code>EP_INDEPENDENT_STEP_TARGETS</code> directory property, tells the function to call <code>ExternalProject_Add_StepTargets()</code> internally using the <code>NO_DEPENDS</code> option for the specified steps.</p>
<dt><code>ExternalProject_Add_StepDependencies</code></p>
<dd>New in version 3.2. </p>
<p> The <code>ExternalProject_Add_StepDependencies()</code> function can be used to add dependencies to a step. The dependencies added must be targets CMake already knows about (these can be ordinary executable or library targets, custom targets or even step targets of another external project): </p>
<pre>ExternalProject_Add_StepDependencies(&lt;name&gt; &lt;step&gt; &lt;target1&gt; [&lt;target2&gt;...])</pre>
<p>This function takes care to set both target and file level dependencies and will ensure that parallel builds will not break. It should be used instead of <code>add_dependencies()</code> whenever adding a dependency for some of the step targets generated by the <code>ExternalProject</code> module.</dl>
<h3>Examples</h3>
<p>The following example shows how to download and build a hypothetical project called <i>FooBar</i> from github: </p>
<pre>include(ExternalProject)
ExternalProject_Add(foobar
 GIT_REPOSITORY git [at] github.com:FooCo/FooBar.git
 GIT_TAG origin/release/1.2.3
)</pre>
<p>For the sake of the example, also define a second hypothetical external project called <i>SecretSauce</i>, which is downloaded from a web server. Two URLs are given to take advantage of a faster internal network if available, with a fallback to a slower external server. The project is a typical <code>Makefile</code> project with no configure step, so some of the default commands are overridden. The build is only required to build the <i>sauce</i> target: </p>
<pre>find_program(MAKE_EXE NAMES gmake nmake make)
ExternalProject_Add(secretsauce
 URL <a rel="nofollow" href="http://intranet.somecompany.com/artifacts/sauce-2.7.tgz">http://intranet.somecompany.com/artifacts/sauce-2.7.tgz</a>
 <a rel="nofollow" href="https://www.somecompany.com/downloads/sauce-2.7.zip">https://www.somecompany.com/downloads/sauce-2.7.zip</a>
 URL_HASH MD5=d41d8cd98f00b204e9800998ecf8427e
 CONFIGURE_COMMAND &quot;&quot;
 BUILD_COMMAND ${MAKE_EXE} sauce
)</pre>
<p>Suppose the build step of <code>secretsauce</code> requires that <code>foobar</code> must already be built. This could be enforced like so: </p>
<pre>ExternalProject_Add_StepDependencies(secretsauce build foobar)</pre>
<p>Another alternative would be to create a custom target for <code>foobar</code>&#8216;s build step and make <code>secretsauce</code> depend on that rather than the whole <code>foobar</code> project. This would mean <code>foobar</code> only needs to be built, it doesn&#8217;t need to run its install or test steps before <code>secretsauce</code> can be built. The dependency can also be defined along with the <code>secretsauce</code> project: </p>
<pre>ExternalProject_Add_StepTargets(foobar build)
ExternalProject_Add(secretsauce
 URL <a rel="nofollow" href="http://intranet.somecompany.com/artifacts/sauce-2.7.tgz">http://intranet.somecompany.com/artifacts/sauce-2.7.tgz</a>
 <a rel="nofollow" href="https://www.somecompany.com/downloads/sauce-2.7.zip">https://www.somecompany.com/downloads/sauce-2.7.zip</a>
 URL_HASH MD5=d41d8cd98f00b204e9800998ecf8427e
 CONFIGURE_COMMAND &quot;&quot;
 BUILD_COMMAND ${MAKE_EXE} sauce
 DEPENDS foobar-build
)</pre>
<p>Instead of calling <i>ExternalProject_Add_StepTargets()</i>, the target could be defined along with the <code>foobar</code> project itself: </p>
<pre>ExternalProject_Add(foobar
 GIT_REPOSITORY git [at] github.com:FooCo/FooBar.git
 GIT_TAG origin/release/1.2.3
 STEP_TARGETS build
)</pre>
<p>If many external projects should have the same set of step targets, setting a directory property may be more convenient. The <code>build</code> step target could be created automatically by setting the <code>EP_STEP_TARGETS</code> directory property before creating the external projects with <i>ExternalProject_Add()</i>: </p>
<pre>set_property(DIRECTORY PROPERTY EP_STEP_TARGETS build)</pre>
<p>Lastly, suppose that <code>secretsauce</code> provides a script called <code>makedoc</code> which can be used to generate its own documentation. Further suppose that the script expects the output directory to be provided as the only parameter and that it should be run from the <code>secretsauce</code> source directory. A custom step and a custom target to trigger the script can be defined like so: </p>
<pre>ExternalProject_Add_Step(secretsauce docs
 COMMAND &lt;SOURCE_DIR&gt;/makedoc &lt;BINARY_DIR&gt;
 WORKING_DIRECTORY &lt;SOURCE_DIR&gt;
 COMMENT &quot;Building secretsauce docs&quot;
 ALWAYS TRUE
 EXCLUDE_FROM_MAIN TRUE
)
ExternalProject_Add_StepTargets(secretsauce docs)</pre>
<p>The custom step could then be triggered from the main build like so: </p>
<pre>cmake --build . --target secretsauce-docs</pre>
<h3>FeatureSummary</h3>
<p>Functions for generating a summary of enabled/disabled features. </p>
<p> These functions can be used to generate a summary of enabled and disabled packages and/or feature for a build tree such as: </p>
<pre>-- The following OPTIONAL packages have been found:
LibXml2 (required version &gt;= 2.4), XML processing lib, &lt;<a rel="nofollow" href="http://xmlsoft.org">http://xmlsoft.org</a>&gt;
 * Enables HTML-import in MyWordProcessor
 * Enables odt-export in MyWordProcessor
PNG, A PNG image library., &lt;<a rel="nofollow" href="http://www.libpng.org/pub/png/">http://www.libpng.org/pub/png/</a>&gt;
 * Enables saving screenshots
-- The following OPTIONAL packages have not been found:
Lua51, The Lua scripting language., &lt;<a rel="nofollow" href="http://www.lua.org">http://www.lua.org</a>&gt;
 * Enables macros in MyWordProcessor
Foo, Foo provides cool stuff.</pre>
<h3>Global Properties</h3>
<dl>
<dt><code>FeatureSummary_PKG_TYPES</code></p>
<dd>The global property <i>FeatureSummary_PKG_TYPES</i> defines the type of packages used by <i>FeatureSummary</i>. </p>
<p> The order in this list is important, the first package type in the list is the least important, the last is the most important. the of a package can only be changed to higher types. </p>
<p> The default package types are , <code>RUNTIME</code>, <code>OPTIONAL</code>, <code>RECOMMENDED</code> and <code>REQUIRED</code>, and their importance is <code>RUNTIME &lt; OPTIONAL &lt; RECOMMENDED &lt; REQUIRED</code>.</p>
<dt><code>FeatureSummary_REQUIRED_PKG_TYPES</code></p>
<dd>The global property <i>FeatureSummary_REQUIRED_PKG_TYPES</i> defines which package types are required. </p>
<p> If one or more package in this categories has not been found, CMake will abort when calling <i>feature_summary()</i> with the &#8216;FATAL_ON_MISSING_REQUIRED_PACKAGES&#8217; option enabled. </p>
<p> The default value for this global property is <code>REQUIRED</code>.</p>
<dt><code>FeatureSummary_DEFAULT_PKG_TYPE</code></p>
<dd>The global property <i>FeatureSummary_DEFAULT_PKG_TYPE</i> defines which package type is the default one. When calling <i>feature_summary()</i>, if the user did not set the package type explicitly, the package will be assigned to this category. </p>
<p> This value must be one of the types defined in the <i>FeatureSummary_PKG_TYPES</i> global property unless the package type is set for all the packages. </p>
<p> The default value for this global property is <code>OPTIONAL</code>.</p>
<dt><code>FeatureSummary_&lt;TYPE&gt;_DESCRIPTION</code></p>
<dd>New in version 3.9. </p>
<p> The global property <i>FeatureSummary_&lt;TYPE&gt;_DESCRIPTION</i> can be defined for each type to replace the type name with the specified string whenever the package type is used in an output string. </p>
<p> If not set, the string &quot;<code>&lt;TYPE&gt;</code> packages&quot; is used.</dl>
<h3>Functions</h3>
<dl>
<dt><code>feature_summary</code></p>
<dd>
<pre>feature_summary( [FILENAME &lt;file&gt;]
 [APPEND]
 [VAR &lt;variable_name&gt;]
 [INCLUDE_QUIET_PACKAGES]
 [FATAL_ON_MISSING_REQUIRED_PACKAGES]
 [DESCRIPTION &quot;&lt;description&gt;&quot; | DEFAULT_DESCRIPTION]
 [QUIET_ON_EMPTY]
 WHAT (ALL
 | PACKAGES_FOUND | PACKAGES_NOT_FOUND
 | &lt;TYPE&gt;_PACKAGES_FOUND | &lt;TYPE&gt;_PACKAGES_NOT_FOUND
 | ENABLED_FEATURES | DISABLED_FEATURES)
 )</pre>
<p>The <code>feature_summary()</code> macro can be used to print information about enabled or disabled packages or features of a project. By default, only the names of the features/packages will be printed and their required version when one was specified. Use <code>set_package_properties()</code> to add more useful information, like e.g. a download URL for the respective package or their purpose in the project. </p>
<p> The <code>WHAT</code> option is the only mandatory option. Here you specify what information will be printed:</p>
<dt><code>ALL</code></p>
<dd>print everything</p>
<dt><code>ENABLED_FEATURES</code></p>
<dd>the list of all features which are enabled</p>
<dt><code>DISABLED_FEATURES</code></p>
<dd>the list of all features which are disabled</p>
<dt><code>PACKAGES_FOUND</code></p>
<dd>the list of all packages which have been found</p>
<dt><code>PACKAGES_NOT_FOUND</code></p>
<dd>the list of all packages which have not been found </p>
<p> For each package type <code>&lt;TYPE&gt;</code> defined by the <i>FeatureSummary_PKG_TYPES</i> global property, the following information can also be used:</p>
<dt><code>&lt;TYPE&gt;_PACKAGES_FOUND</code></p>
<dd>only those packages which have been found which have the type &lt;TYPE&gt;</p>
<dt><code>&lt;TYPE&gt;_PACKAGES_NOT_FOUND</code></p>
<dd>only those packages which have not been found which have the type &lt;TYPE&gt; </p>
<p> Changed in version 3.1: With the exception of the <code>ALL</code> value, these values can be combined in order to customize the output. For example: </p>
<pre>feature_summary(WHAT ENABLED_FEATURES DISABLED_FEATURES)</pre>
<p>If a <code>FILENAME</code> is given, the information is printed into this file. If <code>APPEND</code> is used, it is appended to this file, otherwise the file is overwritten if it already existed. If the VAR option is used, the information is &quot;printed&quot; into the specified variable. If <code>FILENAME</code> is not used, the information is printed to the terminal. Using the <code>DESCRIPTION</code> option a description or headline can be set which will be printed above the actual content. If only one type of package was requested, no title is printed, unless it is explicitly set using either <code>DESCRIPTION</code> to use a custom string, or <code>DEFAULT_DESCRIPTION</code> to use a default title for the requested type. If <code>INCLUDE_QUIET_PACKAGES</code> is given, packages which have been searched with <code>find_package(&#8230; QUIET)</code> will also be listed. By default they are skipped. If <code>FATAL_ON_MISSING_REQUIRED_PACKAGES</code> is given, CMake will abort if a package which is marked as one of the package types listed in the <i>FeatureSummary_REQUIRED_PKG_TYPES</i> global property has not been found. The default value for the <i>FeatureSummary_REQUIRED_PKG_TYPES</i> global property is <code>REQUIRED</code>. </p>
<p> New in version 3.9: The <code>DEFAULT_DESCRIPTION</code> option. </p>
<p> The <i>FeatureSummary_DEFAULT_PKG_TYPE</i> global property can be modified to change the default package type assigned when not explicitly assigned by the user. </p>
<p> New in version 3.8: If the <code>QUIET_ON_EMPTY</code> option is used, if only one type of package was requested, and no packages belonging to that category were found, then no output (including the <code>DESCRIPTION</code>) is printed or added to the <code>VAR</code> variable. </p>
<p> Example 1, append everything to a file: </p>
<pre>include(FeatureSummary)
feature_summary(WHAT ALL
 FILENAME ${CMAKE_BINARY_DIR}/all.log APPEND)</pre>
<p>Example 2, print the enabled features into the variable enabledFeaturesText, including QUIET packages: </p>
<pre>include(FeatureSummary)
feature_summary(WHAT ENABLED_FEATURES
 INCLUDE_QUIET_PACKAGES
 DESCRIPTION &quot;Enabled Features:&quot;
 VAR enabledFeaturesText)
message(STATUS &quot;${enabledFeaturesText}&quot;)</pre>
<p>Example 3, change default package types and print only the categories that are not empty: </p>
<pre>include(FeatureSummary)
set_property(GLOBAL APPEND PROPERTY FeatureSummary_PKG_TYPES BUILD)
find_package(FOO)
set_package_properties(FOO PROPERTIES TYPE BUILD)
feature_summary(WHAT BUILD_PACKAGES_FOUND
 Description &quot;Build tools found:&quot;
 QUIET_ON_EMPTY)
feature_summary(WHAT BUILD_PACKAGES_NOT_FOUND
 Description &quot;Build tools not found:&quot;
 QUIET_ON_EMPTY)</pre>
<dt><code>set_package_properties</code></p>
<dd>
<pre>set_package_properties(&lt;name&gt; PROPERTIES
 [ URL &lt;url&gt; ]
 [ DESCRIPTION &lt;description&gt; ]
 [ TYPE (RUNTIME|OPTIONAL|RECOMMENDED|REQUIRED) ]
 [ PURPOSE &lt;purpose&gt; ]
 )</pre>
<p>Use this macro to set up information about the named package, which can then be displayed via FEATURE_SUMMARY(). This can be done either directly in the Find-module or in the project which uses the module after the find_package() call. The features for which information can be set are added automatically by the find_package() command.</p>
<dt><code>URL &lt;url&gt;</code></p>
<dd>This should be the homepage of the package, or something similar. Ideally this is set already directly in the Find-module.</p>
<dt><code>DESCRIPTION &lt;description&gt;</code></p>
<dd>A short description what that package is, at most one sentence. Ideally this is set already directly in the Find-module.</p>
<dt><code>TYPE &lt;type&gt;</code></p>
<dd>What type of dependency has the using project on that package. Default is <code>OPTIONAL</code>. In this case it is a package which can be used by the project when available at buildtime, but it also work without. <code>RECOMMENDED</code> is similar to <code>OPTIONAL</code>, i.e. the project will build if the package is not present, but the functionality of the resulting binaries will be severely limited. If a <code>REQUIRED</code> package is not available at buildtime, the project may not even build. This can be combined with the <code>FATAL_ON_MISSING_REQUIRED_PACKAGES</code> argument for <code>feature_summary()</code>. Last, a <code>RUNTIME</code> package is a package which is actually not used at all during the build, but which is required for actually running the resulting binaries. So if such a package is missing, the project can still be built, but it may not work later on. If <code>set_package_properties()</code> is called multiple times for the same package with different TYPEs, the <code>TYPE</code> is only changed to higher TYPEs (<code>RUNTIME &lt; OPTIONAL &lt; RECOMMENDED &lt; REQUIRED</code>), lower TYPEs are ignored. The <code>TYPE</code> property is project-specific, so it cannot be set by the Find-module, but must be set in the project. Type accepted can be changed by setting the <i>FeatureSummary_PKG_TYPES</i> global property.</p>
<dt><code>PURPOSE &lt;purpose&gt;</code></p>
<dd>This describes which features this package enables in the project, i.e. it tells the user what functionality he gets in the resulting binaries. If set_package_properties() is called multiple times for a package, all PURPOSE properties are appended to a list of purposes of the package in the project. As the TYPE property, also the PURPOSE property is project-specific, so it cannot be set by the Find-module, but must be set in the project. </p>
<p> Example for setting the info for a package: </p>
<pre>find_package(LibXml2)
set_package_properties(LibXml2 PROPERTIES
 DESCRIPTION &quot;A XML processing library.&quot;
 URL &quot;<a rel="nofollow" href="http://xmlsoft.org/">http://xmlsoft.org/</a>&quot;)
# or
set_package_properties(LibXml2 PROPERTIES
 TYPE RECOMMENDED
 PURPOSE &quot;Enables HTML-import in MyWordProcessor&quot;)
# or
set_package_properties(LibXml2 PROPERTIES
 TYPE OPTIONAL
 PURPOSE &quot;Enables odt-export in MyWordProcessor&quot;)
find_package(DBUS)
set_package_properties(DBUS PROPERTIES
 TYPE RUNTIME
 PURPOSE &quot;Necessary to disable the screensaver during a presentation&quot;)</pre>
<dt><code>add_feature_info</code></p>
<dd>
<pre>add_feature_info(&lt;name&gt; &lt;enabled&gt; &lt;description&gt;)</pre>
<p>Use this macro to add information about a feature with the given <code>&lt;name&gt;</code>. <code>&lt;enabled&gt;</code> contains whether this feature is enabled or not. It can be a variable or a list of conditions. <code>&lt;description&gt;</code> is a text describing the feature. The information can be displayed using <code>feature_summary()</code> for <code>ENABLED_FEATURES</code> and <code>DISABLED_FEATURES</code> respectively. </p>
<p> Changed in version 3.8: <code>&lt;enabled&gt;</code> can be a list of conditions. </p>
<p> Example for setting the info for a feature: </p>
<pre>option(WITH_FOO &quot;Help for foo&quot; ON)
add_feature_info(Foo WITH_FOO &quot;The Foo feature provides very cool stuff.&quot;)</pre>
</dl>
<h3>Legacy Macros</h3>
<p>The following macros are provided for compatibility with previous CMake versions:</p>
<dl>
<dt><code>set_package_info</code></p>
<dd>
<pre>set_package_info(&lt;name&gt; &lt;description&gt; [ &lt;url&gt; [&lt;purpose&gt;] ])</pre>
<p>Use this macro to set up information about the named package, which can then be displayed via <code>feature_summary()</code>. This can be done either directly in the Find-module or in the project which uses the module after the <code>find_package()</code> call. The features for which information can be set are added automatically by the <code>find_package()</code> command.</p>
<dt><code>set_feature_info</code></p>
<dd>
<pre>set_feature_info(&lt;name&gt; &lt;description&gt; [&lt;url&gt;])</pre>
<p>Does the same as: </p>
<pre>set_package_info(&lt;name&gt; &lt;description&gt; &lt;url&gt;)</pre>
<dt><code>print_enabled_features</code></p>
<dd>
<pre>print_enabled_features()</pre>
<p>Does the same as </p>
<pre>feature_summary(WHAT ENABLED_FEATURES DESCRIPTION &quot;Enabled features:&quot;)</pre>
<dt><code>print_disabled_features</code></p>
<dd>
<pre>print_disabled_features()</pre>
<p>Does the same as </p>
<pre>feature_summary(WHAT DISABLED_FEATURES DESCRIPTION &quot;Disabled features:&quot;)</pre>
</dl>
<h3>FetchContent</h3>
<p>New in version 3.11.</p>
<h3>Overview</h3>
<p>This module enables populating content at configure time via any method supported by the <code>ExternalProject</code> module. Whereas <code>ExternalProject_Add()</code> downloads at build time, the <code>FetchContent</code> module makes content available immediately, allowing the configure step to use the content in commands like <code>add_subdirectory()</code>, <code>include()</code> or <code>file()</code> operations. </p>
<p> Content population details should be defined separately from the command that performs the actual population. This separation ensures that all the dependency details are defined before anything might try to use them to populate content. This is particularly important in more complex project hierarchies where dependencies may be shared between multiple projects. </p>
<p> The following shows a typical example of declaring content details for some dependencies and then ensuring they are populated with a separate call: </p>
<pre>FetchContent_Declare(
 googletest
 GIT_REPOSITORY <a rel="nofollow" href="https://github.com/google/googletest.git">https://github.com/google/googletest.git</a>
 GIT_TAG 703bd9caab50b139428cea1aaff9974ebee5742e # release-1.10.0
)
FetchContent_Declare(
 myCompanyIcons
 URL <a rel="nofollow" href="https://intranet.mycompany.com/assets/iconset_1.12.tar.gz">https://intranet.mycompany.com/assets/iconset_1.12.tar.gz</a>
 URL_HASH MD5=5588a7b18261c20068beabfb4f530b87
)
FetchContent_MakeAvailable(googletest secret_sauce)</pre>
<p>The <i>FetchContent_MakeAvailable()</i> command ensures the named dependencies have been populated, either by an earlier call or by populating them itself. When performing the population, it will also add them to the main build, if possible, so that the main build can use the populated projects&#8217; targets, etc. See the command&#8217;s documentation for how these steps are performed. </p>
<p> When using a hierarchical project arrangement, projects at higher levels in the hierarchy are able to override the declared details of content specified anywhere lower in the project hierarchy. The first details to be declared for a given dependency take precedence, regardless of where in the project hierarchy that occurs. Similarly, the first call that tries to populate a dependency &quot;wins&quot;, with subsequent populations reusing the result of the first instead of repeating the population again. See the <i>Examples</i> which demonstrate this scenario. </p>
<p> In some cases, the main project may need to have more precise control over the population, or it may be required to explicitly define the population steps in a way that cannot be captured by the declared details alone. For such situations, the lower level <i>FetchContent_GetProperties()</i> and <i>FetchContent_Populate()</i> commands can be used. These lack the richer features provided by <i>FetchContent_MakeAvailable()</i> though, so their direct use should be considered a last resort. The typical pattern of such custom steps looks like this: </p>
<pre># NOTE: Where possible, prefer to use FetchContent_MakeAvailable()
# instead of custom logic like this
# Check if population has already been performed
FetchContent_GetProperties(depname)
if(NOT depname_POPULATED)
 # Fetch the content using previously declared details
 FetchContent_Populate(depname)
 # Set custom variables, policies, etc.
 # ...
 # Bring the populated content into the build
 add_subdirectory(${depname_SOURCE_DIR} ${depname_BINARY_DIR})
endif()</pre>
<p>The <code>FetchContent</code> module also supports defining and populating content in a single call, with no check for whether the content has been populated elsewhere already. This should not be done in projects, but may be appropriate for populating content in CMake&#8217;s script mode. See <i>FetchContent_Populate()</i> for details.</p>
<h3>Commands</h3>
<dl>
<dt><code>FetchContent_Declare</code></p>
<dd>
<pre>FetchContent_Declare(&lt;name&gt; &lt;contentOptions&gt;...)</pre>
<p>The <code>FetchContent_Declare()</code> function records the options that describe how to populate the specified content. If such details have already been recorded earlier in this project (regardless of where in the project hierarchy), this and all later calls for the same content <code>&lt;name&gt;</code> are ignored. This &quot;first to record, wins&quot; approach is what allows hierarchical projects to have parent projects override content details of child projects. </p>
<p> The content <code>&lt;name&gt;</code> can be any string without spaces, but good practice would be to use only letters, numbers and underscores. The name will be treated case-insensitively and it should be obvious for the content it represents, often being the name of the child project or the value given to its top level <code>project()</code> command (if it is a CMake project). For well-known public projects, the name should generally be the official name of the project. Choosing an unusual name makes it unlikely that other projects needing that same content will use the same name, leading to the content being populated multiple times. </p>
<p> The <code>&lt;contentOptions&gt;</code> can be any of the download, update or patch options that the <code>ExternalProject_Add()</code> command understands. The configure, build, install and test steps are explicitly disabled and therefore options related to them will be ignored. The <code>SOURCE_SUBDIR</code> option is an exception, see <i>FetchContent_MakeAvailable()</i> for details on how that affects behavior. </p>
<p> In most cases, <code>&lt;contentOptions&gt;</code> will just be a couple of options defining the download method and method-specific details like a commit tag or archive hash. For example: </p>
<pre>FetchContent_Declare(
 googletest
 GIT_REPOSITORY <a rel="nofollow" href="https://github.com/google/googletest.git">https://github.com/google/googletest.git</a>
 GIT_TAG 703bd9caab50b139428cea1aaff9974ebee5742e # release-1.10.0
)
FetchContent_Declare(
 myCompanyIcons
 URL <a rel="nofollow" href="https://intranet.mycompany.com/assets/iconset_1.12.tar.gz">https://intranet.mycompany.com/assets/iconset_1.12.tar.gz</a>
 URL_HASH MD5=5588a7b18261c20068beabfb4f530b87
)
FetchContent_Declare(
 myCompanyCertificates
 SVN_REPOSITORY svn+<a href="ssh://svn.mycompany.com/srv/svn/trunk/certs">ssh://svn.mycompany.com/srv/svn/trunk/certs</a>
 SVN_REVISION -r12345
)</pre>
<p>Where contents are being fetched from a remote location and you do not control that server, it is advisable to use a hash for <code>GIT_TAG</code> rather than a branch or tag name. A commit hash is more secure and helps to confirm that the downloaded contents are what you expected. </p>
<p> Changed in version 3.14: Commands for the download, update or patch steps can access the terminal. This may be needed for things like password prompts or real-time display of command progress. </p>
<p> New in version 3.22: The <code>CMAKE_TLS_VERIFY</code>, <code>CMAKE_TLS_CAINFO</code>, <code>CMAKE_NETRC</code> and <code>CMAKE_NETRC_FILE</code> variables now provide the defaults for their corresponding content options, just like they do for <code>ExternalProject_Add()</code>. Previously, these variables were ignored by the <code>FetchContent</code> module. </p>
<dt><code>FetchContent_MakeAvailable</code></p>
<dd>New in version 3.14. </p>
<pre>FetchContent_MakeAvailable(&lt;name1&gt; [&lt;name2&gt;...])</pre>
<p>This command ensures that each of the named dependencies are populated and potentially added to the build by the time it returns. It iterates over the list, and for each dependency, the following logic is applied:</p>
<dt>&bull;</p>
<dd>If the dependency has already been populated earlier in this run, set the <code>&lt;lowercaseName&gt;_POPULATED</code>, <code>&lt;lowercaseName&gt;_SOURCE_DIR</code> and <code>&lt;lowercaseName&gt;_BINARY_DIR</code> variables in the same way as a call to <i>FetchContent_GetProperties()</i>, then skip the remaining steps below and move on to the next dependency in the list.</p>
<dt>&bull;</p>
<dd>Call <i>FetchContent_Populate()</i> to populate the dependency using the details recorded by an earlier call to <i>FetchContent_Declare()</i>. Halt with a fatal error if no such details have been recorded. <i>FETCHCONTENT_SOURCE_DIR_&lt;uppercaseName&gt;</i> can be used to override the declared details and use content provided at the specified location instead.</p>
<dt>&bull;</p>
<dd>If the top directory of the populated content contains a <code>CMakeLists.txt</code> file, call <code>add_subdirectory()</code> to add it to the main build. It is not an error for there to be no <code>CMakeLists.txt</code> file, which allows the command to be used for dependencies that make downloaded content available at a known location, but which do not need or support being added directly to the build. </p>
<p> New in version 3.18: The <code>SOURCE_SUBDIR</code> option can be given in the declared details to look somewhere below the top directory instead (i.e. the same way that <code>SOURCE_SUBDIR</code> is used by the <code>ExternalProject_Add()</code> command). The path provided with <code>SOURCE_SUBDIR</code> must be relative and will be treated as relative to the top directory. It can also point to a directory that does not contain a <code>CMakeLists.txt</code> file or even to a directory that doesn&#8217;t exist. This can be used to avoid adding a project that contains a <code>CMakeLists.txt</code> file in its top directory. </p>
<p> Projects should aim to declare the details of all dependencies they might use before they call <code>FetchContent_MakeAvailable()</code> for any of them. This ensures that if any of the dependencies are also sub-dependencies of one or more of the others, the main project still controls the details that will be used (because it will declare them first before the dependencies get a chance to). In the following code samples, assume that the <code>uses_other</code> dependency also uses <code>FetchContent</code> to add the <code>other</code> dependency internally: </p>
<pre># WRONG: Should declare all details first
FetchContent_Declare(uses_other ...)
FetchContent_MakeAvailable(uses_other)
FetchContent_Declare(other ...) # Will be ignored, uses_other beat us to it
FetchContent_MakeAvailable(other) # Would use details declared by uses_other</pre>
<pre># CORRECT: All details declared first, so they will take priority
FetchContent_Declare(uses_other ...)
FetchContent_Declare(other ...)
FetchContent_MakeAvailable(uses_other other)</pre>
<dt><code>FetchContent_Populate</code></p>
<dd><code>NOTE:</code> Where possible, prefer to use <i>FetchContent_MakeAvailable()</i> instead of implementing population manually with this command. </p>
<pre>FetchContent_Populate(&lt;name&gt;)</pre>
<p>In most cases, the only argument given to <code>FetchContent_Populate()</code> is the <code>&lt;name&gt;</code>. When used this way, the command assumes the content details have been recorded by an earlier call to <i>FetchContent_Declare()</i>. The details are stored in a global property, so they are unaffected by things like variable or directory scope. Therefore, it doesn&#8217;t matter where in the project the details were previously declared, as long as they have been declared before the call to <code>FetchContent_Populate()</code>. Those saved details are then used to construct a call to <code>ExternalProject_Add()</code> in a private sub-build to perform the content population immediately. The implementation of <code>ExternalProject_Add()</code> ensures that if the content has already been populated in a previous CMake run, that content will be reused rather than repopulating them again. For the common case where population involves downloading content, the cost of the download is only paid once. </p>
<p> An internal global property records when a particular content population request has been processed. If <code>FetchContent_Populate()</code> is called more than once for the same content name within a configure run, the second call will halt with an error. Projects can and should check whether content population has already been processed with the <i>FetchContent_GetProperties()</i> command before calling <code>FetchContent_Populate()</code>. </p>
<p> <code>FetchContent_Populate()</code> will set three variables in the scope of the caller:</p>
<dt><code>&lt;lowercaseName&gt;_POPULATED</code></p>
<dd>This will always be set to <code>TRUE</code> by the call.</p>
<dt><code>&lt;lowercaseName&gt;_SOURCE_DIR</code></p>
<dd>The location where the populated content can be found upon return.</p>
<dt><code>&lt;lowercaseName&gt;_BINARY_DIR</code></p>
<dd>A directory intended for use as a corresponding build directory. </p>
<p> The main use case for the <code>&lt;lowercaseName&gt;_SOURCE_DIR</code> and <code>&lt;lowercaseName&gt;_BINARY_DIR</code> variables is to call <code>add_subdirectory()</code> immediately after population: </p>
<pre>FetchContent_Populate(FooBar)
add_subdirectory(${foobar_SOURCE_DIR} ${foobar_BINARY_DIR})</pre>
<p>The values of the three variables can also be retrieved from anywhere in the project hierarchy using the <i>FetchContent_GetProperties()</i> command. </p>
<p> The <code>FetchContent_Populate()</code> command also supports a syntax allowing the content details to be specified directly rather than using any saved details. This is more low-level and use of this form is generally to be avoided in favor of using saved content details as outlined above. Nevertheless, in certain situations it can be useful to invoke the content population as an isolated operation (typically as part of implementing some other higher level feature or when using CMake in script mode): </p>
<pre>FetchContent_Populate(
 &lt;name&gt;
 [QUIET]
 [SUBBUILD_DIR &lt;subBuildDir&gt;]
 [SOURCE_DIR &lt;srcDir&gt;]
 [BINARY_DIR &lt;binDir&gt;]
 ...
)</pre>
<p>This form has a number of key differences to that where only <code>&lt;name&gt;</code> is provided:</p>
<dt>&bull;</p>
<dd>All required population details are assumed to have been provided directly in the call to <code>FetchContent_Populate()</code>. Any saved details for <code>&lt;name&gt;</code> are ignored.</p>
<dt>&bull;</p>
<dd>No check is made for whether content for <code>&lt;name&gt;</code> has already been populated.</p>
<dt>&bull;</p>
<dd>No global property is set to record that the population has occurred.</p>
<dt>&bull;</p>
<dd>No global properties record the source or binary directories used for the populated content.</p>
<dt>&bull;</p>
<dd>The <code>FETCHCONTENT_FULLY_DISCONNECTED</code> and <code>FETCHCONTENT_UPDATES_DISCONNECTED</code> cache variables are ignored. </p>
<p> The <code>&lt;lowercaseName&gt;_SOURCE_DIR</code> and <code>&lt;lowercaseName&gt;_BINARY_DIR</code> variables are still returned to the caller, but since these locations are not stored as global properties when this form is used, they are only available to the calling scope and below rather than the entire project hierarchy. No <code>&lt;lowercaseName&gt;_POPULATED</code> variable is set in the caller&#8217;s scope with this form. </p>
<p> The supported options for <code>FetchContent_Populate()</code> are the same as those for <i>FetchContent_Declare()</i>. Those few options shown just above are either specific to <code>FetchContent_Populate()</code> or their behavior is slightly modified from how <code>ExternalProject_Add()</code> treats them:</p>
<dt><code>QUIET</code></p>
<dd>The <code>QUIET</code> option can be given to hide the output associated with populating the specified content. If the population fails, the output will be shown regardless of whether this option was given or not so that the cause of the failure can be diagnosed. The global <code>FETCHCONTENT_QUIET</code> cache variable has no effect on <code>FetchContent_Populate()</code> calls where the content details are provided directly.</p>
<dt><code>SUBBUILD_DIR</code></p>
<dd>The <code>SUBBUILD_DIR</code> argument can be provided to change the location of the sub-build created to perform the population. The default value is <code>${CMAKE_CURRENT_BINARY_DIR}/&lt;lowercaseName&gt;-subbuild</code> and it would be unusual to need to override this default. If a relative path is specified, it will be interpreted as relative to <code>CMAKE_CURRENT_BINARY_DIR</code>. This option should not be confused with the <code>SOURCE_SUBDIR</code> option which only affects the <i>FetchContent_MakeAvailable()</i> command.</p>
<dt><code>SOURCE_DIR</code>, <code>BINARY_DIR</code></p>
<dd>The <code>SOURCE_DIR</code> and <code>BINARY_DIR</code> arguments are supported by <code>ExternalProject_Add()</code>, but different default values are used by <code>FetchContent_Populate()</code>. <code>SOURCE_DIR</code> defaults to <code>${CMAKE_CURRENT_BINARY_DIR}/&lt;lowercaseName&gt;-src</code> and <code>BINARY_DIR</code> defaults to <code>${CMAKE_CURRENT_BINARY_DIR}/&lt;lowercaseName&gt;-build</code>. If a relative path is specified, it will be interpreted as relative to <code>CMAKE_CURRENT_BINARY_DIR</code>. </p>
<p> In addition to the above explicit options, any other unrecognized options are passed through unmodified to <code>ExternalProject_Add()</code> to perform the download, patch and update steps. The following options are explicitly prohibited (they are disabled by the <code>FetchContent_Populate()</code> command):</p>
<dt>&bull;</p>
<dd><code>CONFIGURE_COMMAND</code></p>
<dt>&bull;</p>
<dd><code>BUILD_COMMAND</code></p>
<dt>&bull;</p>
<dd><code>INSTALL_COMMAND</code></p>
<dt>&bull;</p>
<dd><code>TEST_COMMAND</code> </p>
<p> If using <code>FetchContent_Populate()</code> within CMake&#8217;s script mode, be aware that the implementation sets up a sub-build which therefore requires a CMake generator and build tool to be available. If these cannot be found by default, then the <code>CMAKE_GENERATOR</code> and/or <code>CMAKE_MAKE_PROGRAM</code> variables will need to be set appropriately on the command line invoking the script. </p>
<p> New in version 3.18: Added support for the <code>DOWNLOAD_NO_EXTRACT</code> option. </p>
<dt><code>FetchContent_GetProperties</code></p>
<dd>When using saved content details, a call to <i>FetchContent_MakeAvailable()</i> or <i>FetchContent_Populate()</i> records information in global properties which can be queried at any time. This information includes the source and binary directories associated with the content and also whether or not the content population has been processed during the current configure run. </p>
<pre>FetchContent_GetProperties(
 &lt;name&gt;
 [SOURCE_DIR &lt;srcDirVar&gt;]
 [BINARY_DIR &lt;binDirVar&gt;]
 [POPULATED &lt;doneVar&gt;]
)</pre>
<p>The <code>SOURCE_DIR</code>, <code>BINARY_DIR</code> and <code>POPULATED</code> options can be used to specify which properties should be retrieved. Each option accepts a value which is the name of the variable in which to store that property. Most of the time though, only <code>&lt;name&gt;</code> is given, in which case the call will then set the same variables as a call to <i>FetchContent_MakeAvailable(name)</i> or <i>FetchContent_Populate(name)</i>. </p>
<p> This command is rarely needed when using <i>FetchContent_MakeAvailable()</i>. It is more commonly used as part of implementing the following pattern with <i>FetchContent_Populate()</i>, which ensures that the relevant variables will always be defined regardless of whether or not the population has been performed elsewhere in the project already: </p>
<pre># Check if population has already been performed
FetchContent_GetProperties(depname)
if(NOT depname_POPULATED)
 # Fetch the content using previously declared details
 FetchContent_Populate(depname)
 # Set custom variables, policies, etc.
 # ...
 # Bring the populated content into the build
 add_subdirectory(${depname_SOURCE_DIR} ${depname_BINARY_DIR})
endif()</pre>
</dl>
<h3>Variables</h3>
<p>A number of cache variables can influence the behavior where details from a <i>FetchContent_Declare()</i> call are used to populate content. The variables are all intended for the developer to customize behavior and should not normally be set by the project.</p>
<dl>
<dt><code>FETCHCONTENT_BASE_DIR</code></p>
<dd>In most cases, the saved details do not specify any options relating to the directories to use for the internal sub-build, final source and build areas. It is generally best to leave these decisions up to the <code>FetchContent</code> module to handle on the project&#8217;s behalf. The <code>FETCHCONTENT_BASE_DIR</code> cache variable controls the point under which all content population directories are collected, but in most cases, developers would not need to change this. The default location is <code>${CMAKE_BINARY_DIR}/_deps</code>, but if developers change this value, they should aim to keep the path short and just below the top level of the build tree to avoid running into path length problems on Windows.</p>
<dt><code>FETCHCONTENT_QUIET</code></p>
<dd>The logging output during population can be quite verbose, making the configure stage quite noisy. This cache option (<code>ON</code> by default) hides all population output unless an error is encountered. If experiencing problems with hung downloads, temporarily switching this option off may help diagnose which content population is causing the issue.</p>
<dt><code>FETCHCONTENT_FULLY_DISCONNECTED</code></p>
<dd>When this option is enabled, no attempt is made to download or update any content. It is assumed that all content has already been populated in a previous run or the source directories have been pointed at existing contents the developer has provided manually (using options described further below). When the developer knows that no changes have been made to any content details, turning this option <code>ON</code> can significantly speed up the configure stage. It is <code>OFF</code> by default.</p>
<dt><code>FETCHCONTENT_UPDATES_DISCONNECTED</code></p>
<dd>This is a less severe download/update control compared to <i>FETCHCONTENT_FULLY_DISCONNECTED</i>. Instead of bypassing all download and update logic, <code>FETCHCONTENT_UPDATES_DISCONNECTED</code> only disables the update stage. Therefore, if content has not been downloaded previously, it will still be downloaded when this option is enabled. This can speed up the configure stage, but not as much as <i>FETCHCONTENT_FULLY_DISCONNECTED</i>. It is <code>OFF</code> by default. </p>
<p> In addition to the above cache variables, the following cache variables are also defined for each content name:</p>
<dt><code>FETCHCONTENT_SOURCE_DIR_&lt;uppercaseName&gt;</code></p>
<dd>If this is set, no download or update steps are performed for the specified content and the <code>&lt;lowercaseName&gt;_SOURCE_DIR</code> variable returned to the caller is pointed at this location. This gives developers a way to have a separate checkout of the content that they can modify freely without interference from the build. The build simply uses that existing source, but it still defines <code>&lt;lowercaseName&gt;_BINARY_DIR</code> to point inside its own build area. Developers are strongly encouraged to use this mechanism rather than editing the sources populated in the default location, as changes to sources in the default location can be lost when content population details are changed by the project.</p>
<dt><code>FETCHCONTENT_UPDATES_DISCONNECTED_&lt;uppercaseName&gt;</code></p>
<dd>This is the per-content equivalent of <i>FETCHCONTENT_UPDATES_DISCONNECTED</i>. If the global option or this option is <code>ON</code>, then updates will be disabled for the named content. Disabling updates for individual content can be useful for content whose details rarely change, while still leaving other frequently changing content with updates enabled.</dl>
<h3>Examples</h3>
<p>This first fairly straightforward example ensures that some popular testing frameworks are available to the main build: </p>
<pre>include(FetchContent)
FetchContent_Declare(
 googletest
 GIT_REPOSITORY <a rel="nofollow" href="https://github.com/google/googletest.git">https://github.com/google/googletest.git</a>
 GIT_TAG 703bd9caab50b139428cea1aaff9974ebee5742e # release-1.10.0
)
FetchContent_Declare(
 Catch2
 GIT_REPOSITORY <a rel="nofollow" href="https://github.com/catchorg/Catch2.git">https://github.com/catchorg/Catch2.git</a>
 GIT_TAG de6fe184a9ac1a06895cdd1c9b437f0a0bdf14ad # v2.13.4
)
# After the following call, the CMake targets defined by googletest and
# Catch2 will be available to the rest of the build
FetchContent_MakeAvailable(googletest Catch2)</pre>
<p>If the sub-project&#8217;s <code>CMakeLists.txt</code> file is not at the top level of its source tree, the <code>SOURCE_SUBDIR</code> option can be used to tell <code>FetchContent</code> where to find it. The following example shows how to use that option and it also sets a variable which is meaningful to the subproject before pulling it into the main build: </p>
<pre>include(FetchContent)
FetchContent_Declare(
 protobuf
 GIT_REPOSITORY <a rel="nofollow" href="https://github.com/protocolbuffers/protobuf.git">https://github.com/protocolbuffers/protobuf.git</a>
 GIT_TAG ae50d9b9902526efd6c7a1907d09739f959c6297 # v3.15.0
 SOURCE_SUBDIR cmake
)
set(protobuf_BUILD_TESTS OFF)
FetchContent_MakeAvailable(protobuf)</pre>
<p>In more complex project hierarchies, the dependency relationships can be more complicated. Consider a hierarchy where <code>projA</code> is the top level project and it depends directly on projects <code>projB</code> and <code>projC</code>. Both <code>projB</code> and <code>projC</code> can be built standalone and they also both depend on another project <code>projD</code>. <code>projB</code> additionally depends on <code>projE</code>. This example assumes that all five projects are available on a company git server. The <code>CMakeLists.txt</code> of each project might have sections like the following: </p>
<p> <i>projA</i>: </p>
<pre>include(FetchContent)
FetchContent_Declare(
 projB
 GIT_REPOSITORY git [at] mycompany.com:git/projB.git
 GIT_TAG 4a89dc7e24ff212a7b5167bef7ab079d
)
FetchContent_Declare(
 projC
 GIT_REPOSITORY git [at] mycompany.com:git/projC.git
 GIT_TAG 4ad4016bd1d8d5412d135cf8ceea1bb9
)
FetchContent_Declare(
 projD
 GIT_REPOSITORY git [at] mycompany.com:git/projD.git
 GIT_TAG origin/integrationBranch
)
FetchContent_Declare(
 projE
 GIT_REPOSITORY git [at] mycompany.com:git/projE.git
 GIT_TAG v2.3-rc1
)
# Order is important, see notes in the discussion further below
FetchContent_MakeAvailable(projD projB projC)</pre>
<p><i>projB</i>: </p>
<pre>include(FetchContent)
FetchContent_Declare(
 projD
 GIT_REPOSITORY git [at] mycompany.com:git/projD.git
 GIT_TAG 20b415f9034bbd2a2e8216e9a5c9e632
)
FetchContent_Declare(
 projE
 GIT_REPOSITORY git [at] mycompany.com:git/projE.git
 GIT_TAG 68e20f674a48be38d60e129f600faf7d
)
FetchContent_MakeAvailable(projD projE)</pre>
<p><i>projC</i>: </p>
<pre>include(FetchContent)
FetchContent_Declare(
 projD
 GIT_REPOSITORY git [at] mycompany.com:git/projD.git
 GIT_TAG 7d9a17ad2c962aa13e2fbb8043fb6b8a
)
# This particular version of projD requires workarounds
FetchContent_GetProperties(projD)
if(NOT projd_POPULATED)
 FetchContent_Populate(projD)
 # Copy an additional/replacement file into the populated source
 file(COPY someFile.c DESTINATION ${projd_SOURCE_DIR}/src)
 add_subdirectory(${projd_SOURCE_DIR} ${projd_BINARY_DIR})
endif()</pre>
<p>A few key points should be noted in the above:</p>
<dl>
<dt>&bull;</p>
<dd><code>projB</code> and <code>projC</code> define different content details for <code>projD</code>, but <code>projA</code> also defines a set of content details for <code>projD</code>. Because <code>projA</code> will define them first, the details from <code>projB</code> and <code>projC</code> will not be used. The override details defined by <code>projA</code> are not required to match either of those from <code>projB</code> or <code>projC</code>, but it is up to the higher level project to ensure that the details it does define still make sense for the child projects.</p>
<dt>&bull;</p>
<dd>In the <code>projA</code> call to <i>FetchContent_MakeAvailable()</i>, <code>projD</code> is listed ahead of <code>projB</code> and <code>projC</code> to ensure that <code>projA</code> is in control of how <code>projD</code> is populated.</p>
<dt>&bull;</p>
<dd>While <code>projA</code> defines content details for <code>projE</code>, it does not need to explicitly call <code>FetchContent_MakeAvailable(projE)</code> or <code>FetchContent_Populate(projD)</code> itself. Instead, it leaves that to the child <code>projB</code>. For higher level projects, it is often enough to just define the override content details and leave the actual population to the child projects. This saves repeating the same thing at each level of the project hierarchy unnecessarily. </p>
<p> Projects don&#8217;t always need to add the populated content to the build. Sometimes the project just wants to make the downloaded content available at a predictable location. The next example ensures that a set of standard company toolchain files (and potentially even the toolchain binaries themselves) is available early enough to be used for that same build. </p>
<pre>cmake_minimum_required(VERSION 3.14)
include(FetchContent)
FetchContent_Declare(
 mycom_toolchains
 URL <a rel="nofollow" href="https://intranet.mycompany.com//toolchains_1.3.2.tar.gz">https://intranet.mycompany.com//toolchains_1.3.2.tar.gz</a>
)
FetchContent_MakeAvailable(mycom_toolchains)
project(CrossCompileExample)</pre>
<p>The project could be configured to use one of the downloaded toolchains like so: </p>
<pre>cmake -DCMAKE_TOOLCHAIN_FILE=_deps/mycom_toolchains-src/toolchain_arm.cmake /path/to/src</pre>
<p>When CMake processes the <code>CMakeLists.txt</code> file, it will download and unpack the tarball into <code>_deps/mycompany_toolchains-src</code> relative to the build directory. The <code>CMAKE_TOOLCHAIN_FILE</code> variable is not used until the <code>project()</code> command is reached, at which point CMake looks for the named toolchain file relative to the build directory. Because the tarball has already been downloaded and unpacked by then, the toolchain file will be in place, even the very first time that <code>cmake</code> is run in the build directory. </p>
<p> Lastly, the following example demonstrates how one might download and unpack a firmware tarball using CMake&#8217;s <code>script mode</code>. The call to <i>FetchContent_Populate()</i> specifies all the content details and the unpacked firmware will be placed in a <code>firmware</code> directory below the current working directory. </p>
<p> <i>getFirmware.cmake</i>: </p>
<pre># NOTE: Intended to be run in script mode with cmake -P
include(FetchContent)
FetchContent_Populate(
 firmware
 URL <a rel="nofollow" href="https://mycompany.com/assets/firmware-1.23-arm.tar.gz">https://mycompany.com/assets/firmware-1.23-arm.tar.gz</a>
 URL_HASH MD5=68247684da89b608d466253762b0ff11
 SOURCE_DIR firmware
)</pre>
</dl>
<h3>FindPackageHandleStandardArgs</h3>
<p>This module provides functions intended to be used in Find Modules implementing <code>find_package(&lt;PackageName&gt;)</code> calls.</p>
<dl>
<dt><code>find_package_handle_standard_args</code></p>
<dd>This command handles the <code>REQUIRED</code>, <code>QUIET</code> and version-related arguments of <code>find_package()</code>. It also sets the <code>&lt;PackageName&gt;_FOUND</code> variable. The package is considered found if all variables listed contain valid results, e.g. valid filepaths. </p>
<p> There are two signatures: </p>
<pre>find_package_handle_standard_args(&lt;PackageName&gt;
 (DEFAULT_MSG|&lt;custom-failure-message&gt;)
 &lt;required-var&gt;...
 )
find_package_handle_standard_args(&lt;PackageName&gt;
 [FOUND_VAR &lt;result-var&gt;]
 [REQUIRED_VARS &lt;required-var&gt;...]
 [VERSION_VAR &lt;version-var&gt;]
 [HANDLE_VERSION_RANGE]
 [HANDLE_COMPONENTS]
 [CONFIG_MODE]
 [NAME_MISMATCHED]
 [REASON_FAILURE_MESSAGE &lt;reason-failure-message&gt;]
 [FAIL_MESSAGE &lt;custom-failure-message&gt;]
 )</pre>
<p>The <code>&lt;PackageName&gt;_FOUND</code> variable will be set to <code>TRUE</code> if all the variables <code>&lt;required-var&gt;&#8230;</code> are valid and any optional constraints are satisfied, and <code>FALSE</code> otherwise. A success or failure message may be displayed based on the results and on whether the <code>REQUIRED</code> and/or <code>QUIET</code> option was given to the <code>find_package()</code> call. </p>
<p> The options are:</p>
<dt><code>(DEFAULT_MSG|&lt;custom-failure-message&gt;)</code></p>
<dd>In the simple signature this specifies the failure message. Use <code>DEFAULT_MSG</code> to ask for a default message to be computed (recommended). Not valid in the full signature.</p>
<dt><code>FOUND_VAR &lt;result-var&gt;</code></p>
<dd>Deprecated since version 3.3. </p>
<p> Specifies either <code>&lt;PackageName&gt;_FOUND</code> or <code>&lt;PACKAGENAME&gt;_FOUND</code> as the result variable. This exists only for compatibility with older versions of CMake and is now ignored. Result variables of both names are always set for compatibility.</p>
<dt><code>REQUIRED_VARS &lt;required-var&gt;&#8230;</code></p>
<dd>Specify the variables which are required for this package. These may be named in the generated failure message asking the user to set the missing variable values. Therefore these should typically be cache entries such as <code>FOO_LIBRARY</code> and not output variables like <code>FOO_LIBRARIES</code>. </p>
<p> Changed in version 3.18: If <code>HANDLE_COMPONENTS</code> is specified, this option can be omitted. </p>
<dt><code>VERSION_VAR &lt;version-var&gt;</code></p>
<dd>Specify the name of a variable that holds the version of the package that has been found. This version will be checked against the (potentially) specified required version given to the <code>find_package()</code> call, including its <code>EXACT</code> option. The default messages include information about the required version and the version which has been actually found, both if the version is ok or not.</p>
<dt><code>HANDLE_VERSION_RANGE</code></p>
<dd>New in version 3.19. </p>
<p> Enable handling of a version range, if one is specified. Without this option, a developer warning will be displayed if a version range is specified.</p>
<dt><code>HANDLE_COMPONENTS</code></p>
<dd>Enable handling of package components. In this case, the command will report which components have been found and which are missing, and the <code>&lt;PackageName&gt;_FOUND</code> variable will be set to <code>FALSE</code> if any of the required components (i.e. not the ones listed after the <code>OPTIONAL_COMPONENTS</code> option of <code>find_package()</code>) are missing.</p>
<dt><code>CONFIG_MODE</code></p>
<dd>Specify that the calling find module is a wrapper around a call to <code>find_package(&lt;PackageName&gt; NO_MODULE)</code>. This implies a <code>VERSION_VAR</code> value of <code>&lt;PackageName&gt;_VERSION</code>. The command will automatically check whether the package configuration file was found.</p>
<dt><code>REASON_FAILURE_MESSAGE &lt;reason-failure-message&gt;</code></p>
<dd>New in version 3.16. </p>
<p> Specify a custom message of the reason for the failure which will be appended to the default generated message.</p>
<dt><code>FAIL_MESSAGE &lt;custom-failure-message&gt;</code></p>
<dd>Specify a custom failure message instead of using the default generated message. Not recommended.</p>
<dt><code>NAME_MISMATCHED</code></p>
<dd>New in version 3.17. </p>
<p> Indicate that the <code>&lt;PackageName&gt;</code> does not match <code>${CMAKE_FIND_PACKAGE_NAME}</code>. This is usually a mistake and raises a warning, but it may be intentional for usage of the command for components of a larger package. </p>
<p> Example for the simple signature: </p>
<pre>find_package_handle_standard_args(LibXml2 DEFAULT_MSG
 LIBXML2_LIBRARY LIBXML2_INCLUDE_DIR)</pre>
<p>The <code>LibXml2</code> package is considered to be found if both <code>LIBXML2_LIBRARY</code> and <code>LIBXML2_INCLUDE_DIR</code> are valid. Then also <code>LibXml2_FOUND</code> is set to <code>TRUE</code>. If it is not found and <code>REQUIRED</code> was used, it fails with a <code>message(FATAL_ERROR)</code>, independent whether <code>QUIET</code> was used or not. If it is found, success will be reported, including the content of the first <code>&lt;required-var&gt;</code>. On repeated CMake runs, the same message will not be printed again. </p>
<p> <code>NOTE:</code> If <code>&lt;PackageName&gt;</code> does not match <code>CMAKE_FIND_PACKAGE_NAME</code> for the calling module, a warning that there is a mismatch is given. The <code>FPHSA_NAME_MISMATCHED</code> variable may be set to bypass the warning if using the old signature and the <code>NAME_MISMATCHED</code> argument using the new signature. To avoid forcing the caller to require newer versions of CMake for usage, the variable&#8217;s value will be used if defined when the <code>NAME_MISMATCHED</code> argument is not passed for the new signature (but using both is an error).. </p>
<p> Example for the full signature: </p>
<pre>find_package_handle_standard_args(LibArchive
 REQUIRED_VARS LibArchive_LIBRARY LibArchive_INCLUDE_DIR
 VERSION_VAR LibArchive_VERSION)</pre>
<p>In this case, the <code>LibArchive</code> package is considered to be found if both <code>LibArchive_LIBRARY</code> and <code>LibArchive_INCLUDE_DIR</code> are valid. Also the version of <code>LibArchive</code> will be checked by using the version contained in <code>LibArchive_VERSION</code>. Since no <code>FAIL_MESSAGE</code> is given, the default messages will be printed. </p>
<p> Another example for the full signature: </p>
<pre>find_package(Automoc4 QUIET NO_MODULE HINTS /opt/automoc4)
find_package_handle_standard_args(Automoc4 CONFIG_MODE)</pre>
<p>In this case, a <code>FindAutmoc4.cmake</code> module wraps a call to <code>find_package(Automoc4 NO_MODULE)</code> and adds an additional search directory for <code>automoc4</code>. Then the call to <code>find_package_handle_standard_args</code> produces a proper success/failure message.</p>
<dt><code>find_package_check_version</code></p>
<dd>New in version 3.19. </p>
<p> Helper function which can be used to check if a <code>&lt;version&gt;</code> is valid against version-related arguments of <code>find_package()</code>. </p>
<pre>find_package_check_version(&lt;version&gt; &lt;result-var&gt;
 [HANDLE_VERSION_RANGE]
 [RESULT_MESSAGE_VARIABLE &lt;message-var&gt;]
 )</pre>
<p>The <code>&lt;result-var&gt;</code> will hold a boolean value giving the result of the check. </p>
<p> The options are:</p>
<dt><code>HANDLE_VERSION_RANGE</code></p>
<dd>Enable handling of a version range, if one is specified. Without this option, a developer warning will be displayed if a version range is specified.</p>
<dt><code>RESULT_MESSAGE_VARIABLE &lt;message-var&gt;</code></p>
<dd>Specify a variable to get back a message describing the result of the check. </p>
<p> Example for the usage: </p>
<pre>find_package_check_version(1.2.3 result HANDLE_VERSION_RANGE
 RESULT_MESSAGE_VARIABLE reason)
if (result)
 message (STATUS &quot;${reason}&quot;)
else()
 message (FATAL_ERROR &quot;${reason}&quot;)
endif()</pre>
</dl>
<h3>FindPackageMessage</h3>
<pre>find_package_message(&lt;name&gt; &quot;message for user&quot; &quot;find result details&quot;)</pre>
<p>This function is intended to be used in FindXXX.cmake modules files. It will print a message once for each unique find result. This is useful for telling the user where a package was found. The first argument specifies the name (XXX) of the package. The second argument specifies the message to display. The third argument lists details about the find result so that if they change the message will be displayed again. The macro also obeys the QUIET argument to the find_package command. </p>
<p> Example: </p>
<pre>if(X11_FOUND)
 find_package_message(X11 &quot;Found X11: ${X11_X11_LIB}&quot;
 &quot;[${X11_X11_LIB}][${X11_INCLUDE_DIR}]&quot;)
else()
 ...
endif()</pre>
<h3>FortranCInterface</h3>
<p>Fortran/C Interface Detection </p>
<p> This module automatically detects the API by which C and Fortran languages interact.</p>
<h3>Module Variables</h3>
<p>Variables that indicate if the mangling is found:</p>
<dl>
<dt><code>FortranCInterface_GLOBAL_FOUND</code></p>
<dd>Global subroutines and functions.</p>
<dt><code>FortranCInterface_MODULE_FOUND</code></p>
<dd>Module subroutines and functions (declared by &quot;MODULE PROCEDURE&quot;). </p>
<p> This module also provides the following variables to specify the detected mangling, though a typical use case does not need to reference them and can use the <i>Module Functions</i> below.</p>
<dt><code>FortranCInterface_GLOBAL_PREFIX</code></p>
<dd>Prefix for a global symbol without an underscore.</p>
<dt><code>FortranCInterface_GLOBAL_SUFFIX</code></p>
<dd>Suffix for a global symbol without an underscore.</p>
<dt><code>FortranCInterface_GLOBAL_CASE</code></p>
<dd>The case for a global symbol without an underscore, either <code>UPPER</code> or <code>LOWER</code>.</p>
<dt><code>FortranCInterface_GLOBAL__PREFIX</code></p>
<dd>Prefix for a global symbol with an underscore.</p>
<dt><code>FortranCInterface_GLOBAL__SUFFIX</code></p>
<dd>Suffix for a global symbol with an underscore.</p>
<dt><code>FortranCInterface_GLOBAL__CASE</code></p>
<dd>The case for a global symbol with an underscore, either <code>UPPER</code> or <code>LOWER</code>.</p>
<dt><code>FortranCInterface_MODULE_PREFIX</code></p>
<dd>Prefix for a module symbol without an underscore.</p>
<dt><code>FortranCInterface_MODULE_MIDDLE</code></p>
<dd>Middle of a module symbol without an underscore that appears between the name of the module and the name of the symbol.</p>
<dt><code>FortranCInterface_MODULE_SUFFIX</code></p>
<dd>Suffix for a module symbol without an underscore.</p>
<dt><code>FortranCInterface_MODULE_CASE</code></p>
<dd>The case for a module symbol without an underscore, either <code>UPPER</code> or <code>LOWER</code>.</p>
<dt><code>FortranCInterface_MODULE__PREFIX</code></p>
<dd>Prefix for a module symbol with an underscore.</p>
<dt><code>FortranCInterface_MODULE__MIDDLE</code></p>
<dd>Middle of a module symbol with an underscore that appears between the name of the module and the name of the symbol.</p>
<dt><code>FortranCInterface_MODULE__SUFFIX</code></p>
<dd>Suffix for a module symbol with an underscore.</p>
<dt><code>FortranCInterface_MODULE__CASE</code></p>
<dd>The case for a module symbol with an underscore, either <code>UPPER</code> or <code>LOWER</code>.</dl>
<h3>Module Functions</h3>
<dl>
<dt><code>FortranCInterface_HEADER</code></p>
<dd>The <code>FortranCInterface_HEADER</code> function is provided to generate a C header file containing macros to mangle symbol names: </p>
<pre>FortranCInterface_HEADER(&lt;file&gt;
 [MACRO_NAMESPACE &lt;macro-ns&gt;]
 [SYMBOL_NAMESPACE &lt;ns&gt;]
 [SYMBOLS [&lt;module&gt;:]&lt;function&gt; ...])</pre>
<p>It generates in <code>&lt;file&gt;</code> definitions of the following macros: </p>
<pre>#define FortranCInterface_GLOBAL (name,NAME) ...
#define FortranCInterface_GLOBAL_(name,NAME) ...
#define FortranCInterface_MODULE (mod,name, MOD,NAME) ...
#define FortranCInterface_MODULE_(mod,name, MOD,NAME) ...</pre>
<p>These macros mangle four categories of Fortran symbols, respectively:</p>
<dt>&bull;</p>
<dd>Global symbols without &#8216;_&#8217;: <code>call mysub()</code></p>
<dt>&bull;</p>
<dd>Global symbols with &#8216;_&#8217; : <code>call my_sub()</code></p>
<dt>&bull;</p>
<dd>Module symbols without &#8216;_&#8217;: <code>use mymod; call mysub()</code></p>
<dt>&bull;</p>
<dd>Module symbols with &#8216;_&#8217; : <code>use mymod; call my_sub()</code> </p>
<p> If mangling for a category is not known, its macro is left undefined. All macros require raw names in both lower case and upper case. </p>
<p> The options are:</p>
<dt><code>MACRO_NAMESPACE</code></p>
<dd>Replace the default <code>FortranCInterface_</code> prefix with a given namespace <code>&lt;macro-ns&gt;</code>.</p>
<dt><code>SYMBOLS</code></p>
<dd>List symbols to mangle automatically with C preprocessor definitions: </p>
<pre>&lt;function&gt; ==&gt; #define &lt;ns&gt;&lt;function&gt; ...
&lt;module&gt;:&lt;function&gt; ==&gt; #define &lt;ns&gt;&lt;module&gt;_&lt;function&gt; ...</pre>
<p>If the mangling for some symbol is not known then no preprocessor definition is created, and a warning is displayed.</p>
<dt><code>SYMBOL_NAMESPACE</code></p>
<dd>Prefix all preprocessor definitions generated by the <code>SYMBOLS</code> option with a given namespace <code>&lt;ns&gt;</code>.</p>
<dt><code>FortranCInterface_VERIFY</code></p>
<dd>The <code>FortranCInterface_VERIFY</code> function is provided to verify that the Fortran and C/C++ compilers work together: </p>
<pre>FortranCInterface_VERIFY([CXX] [QUIET])</pre>
<p>It tests whether a simple test executable using Fortran and C (and C++ when the CXX option is given) compiles and links successfully. The result is stored in the cache entry <code>FortranCInterface_VERIFIED_C</code> (or <code>FortranCInterface_VERIFIED_CXX</code> if <code>CXX</code> is given) as a boolean. If the check fails and <code>QUIET</code> is not given the function terminates with a fatal error message describing the problem. The purpose of this check is to stop a build early for incompatible compiler combinations. The test is built in the <code>Release</code> configuration.</dl>
<h3>Example Usage</h3>
<pre>include(FortranCInterface)
FortranCInterface_HEADER(FC.h MACRO_NAMESPACE &quot;FC_&quot;)</pre>
<p>This creates a &quot;FC.h&quot; header that defines mangling macros <code>FC_GLOBAL()</code>, <code>FC_GLOBAL_()</code>, <code>FC_MODULE()</code>, and <code>FC_MODULE_()</code>. </p>
<pre>include(FortranCInterface)
FortranCInterface_HEADER(FCMangle.h
 MACRO_NAMESPACE &quot;FC_&quot;
 SYMBOL_NAMESPACE &quot;FC_&quot;
 SYMBOLS mysub mymod:my_sub)</pre>
<p>This creates a &quot;FCMangle.h&quot; header that defines the same <code>FC_*()</code> mangling macros as the previous example plus preprocessor symbols <code>FC_mysub</code> and <code>FC_mymod_my_sub</code>.</p>
<h3>Additional Manglings</h3>
<p>FortranCInterface is aware of possible <code>GLOBAL</code> and <code>MODULE</code> manglings for many Fortran compilers, but it also provides an interface to specify new possible manglings. Set the variables: </p>
<pre>FortranCInterface_GLOBAL_SYMBOLS
FortranCInterface_MODULE_SYMBOLS</pre>
<p>before including FortranCInterface to specify manglings of the symbols <code>MySub</code>, <code>My_Sub</code>, <code>MyModule:MySub</code>, and <code>My_Module:My_Sub</code>. For example, the code: </p>
<pre>set(FortranCInterface_GLOBAL_SYMBOLS mysub_ my_sub__ MYSUB_)
 # ^^^^^ ^^^^^^ ^^^^^
set(FortranCInterface_MODULE_SYMBOLS
 __mymodule_MOD_mysub __my_module_MOD_my_sub)
 # ^^^^^^^^ ^^^^^ ^^^^^^^^^ ^^^^^^
include(FortranCInterface)</pre>
<p>tells FortranCInterface to try given <code>GLOBAL</code> and <code>MODULE</code> manglings. (The carets point at raw symbol names for clarity in this example but are not needed.)</p>
<h3>GenerateExportHeader</h3>
<p>Function for generation of export macros for libraries </p>
<p> This module provides the function <code>GENERATE_EXPORT_HEADER()</code>. </p>
<p> New in version 3.12: Added support for C projects. Previous versions supported C++ project only. </p>
<p> The <code>GENERATE_EXPORT_HEADER</code> function can be used to generate a file suitable for preprocessor inclusion which contains EXPORT macros to be used in library classes: </p>
<pre>GENERATE_EXPORT_HEADER( LIBRARY_TARGET
 [BASE_NAME &lt;base_name&gt;]
 [EXPORT_MACRO_NAME &lt;export_macro_name&gt;]
 [EXPORT_FILE_NAME &lt;export_file_name&gt;]
 [DEPRECATED_MACRO_NAME &lt;deprecated_macro_name&gt;]
 [NO_EXPORT_MACRO_NAME &lt;no_export_macro_name&gt;]
 [INCLUDE_GUARD_NAME &lt;include_guard_name&gt;]
 [STATIC_DEFINE &lt;static_define&gt;]
 [NO_DEPRECATED_MACRO_NAME &lt;no_deprecated_macro_name&gt;]
 [DEFINE_NO_DEPRECATED]
 [PREFIX_NAME &lt;prefix_name&gt;]
 [CUSTOM_CONTENT_FROM_VARIABLE &lt;variable&gt;]
)</pre>
<p>The target properties <code>CXX_VISIBILITY_PRESET</code> and <code>VISIBILITY_INLINES_HIDDEN</code> can be used to add the appropriate compile flags for targets. See the documentation of those target properties, and the convenience variables <code>CMAKE_CXX_VISIBILITY_PRESET</code> and <code>CMAKE_VISIBILITY_INLINES_HIDDEN</code>. </p>
<p> By default <code>GENERATE_EXPORT_HEADER()</code> generates macro names in a file name determined by the name of the library. This means that in the simplest case, users of <code>GenerateExportHeader</code> will be equivalent to: </p>
<pre>set(CMAKE_CXX_VISIBILITY_PRESET hidden)
set(CMAKE_VISIBILITY_INLINES_HIDDEN 1)
add_library(somelib someclass.cpp)
generate_export_header(somelib)
install(TARGETS somelib DESTINATION ${LIBRARY_INSTALL_DIR})
install(FILES
 someclass.h
 ${PROJECT_BINARY_DIR}/somelib_export.h DESTINATION ${INCLUDE_INSTALL_DIR}
)</pre>
<p>And in the ABI header files: </p>
<pre>#include &quot;somelib_export.h&quot;
class SOMELIB_EXPORT SomeClass {
 ...
};</pre>
<p>The CMake fragment will generate a file in the <code>${CMAKE_CURRENT_BINARY_DIR}</code> called <code>somelib_export.h</code> containing the macros <code>SOMELIB_EXPORT</code>, <code>SOMELIB_NO_EXPORT</code>, <code>SOMELIB_DEPRECATED</code>, <code>SOMELIB_DEPRECATED_EXPORT</code> and <code>SOMELIB_DEPRECATED_NO_EXPORT</code>. They will be followed by content taken from the variable specified by the <code>CUSTOM_CONTENT_FROM_VARIABLE</code> option, if any. The resulting file should be installed with other headers in the library. </p>
<p> The <code>BASE_NAME</code> argument can be used to override the file name and the names used for the macros: </p>
<pre>add_library(somelib someclass.cpp)
generate_export_header(somelib
 BASE_NAME other_name
)</pre>
<p>Generates a file called <code>other_name_export.h</code> containing the macros <code>OTHER_NAME_EXPORT</code>, <code>OTHER_NAME_NO_EXPORT</code> and <code>OTHER_NAME_DEPRECATED</code> etc. </p>
<p> The <code>BASE_NAME</code> may be overridden by specifying other options in the function. For example: </p>
<pre>add_library(somelib someclass.cpp)
generate_export_header(somelib
 EXPORT_MACRO_NAME OTHER_NAME_EXPORT
)</pre>
<p>creates the macro <code>OTHER_NAME_EXPORT</code> instead of <code>SOMELIB_EXPORT</code>, but other macros and the generated file name is as default: </p>
<pre>add_library(somelib someclass.cpp)
generate_export_header(somelib
 DEPRECATED_MACRO_NAME KDE_DEPRECATED
)</pre>
<p>creates the macro <code>KDE_DEPRECATED</code> instead of <code>SOMELIB_DEPRECATED</code>. </p>
<p> If <code>LIBRARY_TARGET</code> is a static library, macros are defined without values. </p>
<p> If the same sources are used to create both a shared and a static library, the uppercased symbol <code>${BASE_NAME}_STATIC_DEFINE</code> should be used when building the static library: </p>
<pre>add_library(shared_variant SHARED ${lib_SRCS})
add_library(static_variant ${lib_SRCS})
generate_export_header(shared_variant BASE_NAME libshared_and_static)
set_target_properties(static_variant PROPERTIES
 COMPILE_FLAGS -DLIBSHARED_AND_STATIC_STATIC_DEFINE)</pre>
<p>This will cause the export macros to expand to nothing when building the static library. </p>
<p> If <code>DEFINE_NO_DEPRECATED</code> is specified, then a macro <code>${BASE_NAME}_NO_DEPRECATED</code> will be defined This macro can be used to remove deprecated code from preprocessor output: </p>
<pre>option(EXCLUDE_DEPRECATED &quot;Exclude deprecated parts of the library&quot; FALSE)
if (EXCLUDE_DEPRECATED)
 set(NO_BUILD_DEPRECATED DEFINE_NO_DEPRECATED)
endif()
generate_export_header(somelib ${NO_BUILD_DEPRECATED})</pre>
<p>And then in somelib: </p>
<pre>class SOMELIB_EXPORT SomeClass
{
public:
#ifndef SOMELIB_NO_DEPRECATED
 SOMELIB_DEPRECATED void oldMethod();
#endif
};</pre>
<pre>#ifndef SOMELIB_NO_DEPRECATED
void SomeClass::oldMethod() { }
#endif</pre>
<p>If <code>PREFIX_NAME</code> is specified, the argument will be used as a prefix to all generated macros. </p>
<p> For example: </p>
<pre>generate_export_header(somelib PREFIX_NAME VTK_)</pre>
<p>Generates the macros <code>VTK_SOMELIB_EXPORT</code> etc. </p>
<p> New in version 3.1: Library target can be an <code>OBJECT</code> library. </p>
<p> New in version 3.7: Added the <code>CUSTOM_CONTENT_FROM_VARIABLE</code> option. </p>
<p> New in version 3.11: Added the <code>INCLUDE_GUARD_NAME</code> option. </p>
<pre>ADD_COMPILER_EXPORT_FLAGS( [&lt;output_variable&gt;] )</pre>
<p>Deprecated since version 3.0: Set the target properties <code>CXX_VISIBILITY_PRESET</code> and <code>VISIBILITY_INLINES_HIDDEN</code> instead. </p>
<p> The <code>ADD_COMPILER_EXPORT_FLAGS</code> function adds <code>-fvisibility=hidden</code> to <code>CMAKE_CXX_FLAGS</code> if supported, and is a no-op on Windows which does not need extra compiler flags for exporting support. You may optionally pass a single argument to <code>ADD_COMPILER_EXPORT_FLAGS</code> that will be populated with the <code>CXX_FLAGS</code> required to enable visibility support for the compiler/architecture in use.</p>
<h3>GetPrerequisites</h3>
<p>Deprecated since version 3.16: Use <code>file(GET_RUNTIME_DEPENDENCIES)</code> instead. </p>
<p> Functions to analyze and list executable file prerequisites. </p>
<p> This module provides functions to list the .dll, .dylib or .so files that an executable or shared library file depends on. (Its prerequisites.) </p>
<p> It uses various tools to obtain the list of required shared library files: </p>
<pre>dumpbin (Windows)
objdump (MinGW on Windows)
ldd (Linux/Unix)
otool (Mac OSX)</pre>
<p>Changed in version 3.16: The tool specified by <code>CMAKE_OBJDUMP</code> will be used, if set. </p>
<p> The following functions are provided by this module: </p>
<pre>get_prerequisites
list_prerequisites
list_prerequisites_by_glob
gp_append_unique
is_file_executable
gp_item_default_embedded_path
 (projects can override with gp_item_default_embedded_path_override)
gp_resolve_item
 (projects can override with gp_resolve_item_override)
gp_resolved_file_type
 (projects can override with gp_resolved_file_type_override)
gp_file_type</pre>
<pre>GET_PREREQUISITES(&lt;target&gt; &lt;prerequisites_var&gt; &lt;exclude_system&gt; &lt;recurse&gt;
 &lt;exepath&gt; &lt;dirs&gt; [&lt;rpaths&gt;])</pre>
<p>Get the list of shared library files required by &lt;target&gt;. The list in the variable named &lt;prerequisites_var&gt; should be empty on first entry to this function. On exit, &lt;prerequisites_var&gt; will contain the list of required shared library files. </p>
<p> &lt;target&gt; is the full path to an executable file. &lt;prerequisites_var&gt; is the name of a CMake variable to contain the results. &lt;exclude_system&gt; must be 0 or 1 indicating whether to include or exclude &quot;system&quot; prerequisites. If &lt;recurse&gt; is set to 1 all prerequisites will be found recursively, if set to 0 only direct prerequisites are listed. &lt;exepath&gt; is the path to the top level executable used for @executable_path replacement on the Mac. &lt;dirs&gt; is a list of paths where libraries might be found: these paths are searched first when a target without any path info is given. Then standard system locations are also searched: PATH, Framework locations, /usr/lib&#8230; </p>
<p> New in version 3.14: The variable GET_PREREQUISITES_VERBOSE can be set to true to enable verbose output. </p>
<pre>LIST_PREREQUISITES(&lt;target&gt; [&lt;recurse&gt; [&lt;exclude_system&gt; [&lt;verbose&gt;]]])</pre>
<p>Print a message listing the prerequisites of &lt;target&gt;. </p>
<p> &lt;target&gt; is the name of a shared library or executable target or the full path to a shared library or executable file. If &lt;recurse&gt; is set to 1 all prerequisites will be found recursively, if set to 0 only direct prerequisites are listed. &lt;exclude_system&gt; must be 0 or 1 indicating whether to include or exclude &quot;system&quot; prerequisites. With &lt;verbose&gt; set to 0 only the full path names of the prerequisites are printed, set to 1 extra information will be displayed. </p>
<pre>LIST_PREREQUISITES_BY_GLOB(&lt;glob_arg&gt; &lt;glob_exp&gt;)</pre>
<p>Print the prerequisites of shared library and executable files matching a globbing pattern. &lt;glob_arg&gt; is GLOB or GLOB_RECURSE and &lt;glob_exp&gt; is a globbing expression used with &quot;file(GLOB&quot; or &quot;file(GLOB_RECURSE&quot; to retrieve a list of matching files. If a matching file is executable, its prerequisites are listed. </p>
<p> Any additional (optional) arguments provided are passed along as the optional arguments to the list_prerequisites calls. </p>
<pre>GP_APPEND_UNIQUE(&lt;list_var&gt; &lt;value&gt;)</pre>
<p>Append &lt;value&gt; to the list variable &lt;list_var&gt; only if the value is not already in the list. </p>
<pre>IS_FILE_EXECUTABLE(&lt;file&gt; &lt;result_var&gt;)</pre>
<p>Return 1 in &lt;result_var&gt; if &lt;file&gt; is a binary executable, 0 otherwise. </p>
<pre>GP_ITEM_DEFAULT_EMBEDDED_PATH(&lt;item&gt; &lt;default_embedded_path_var&gt;)</pre>
<p>Return the path that others should refer to the item by when the item is embedded inside a bundle. </p>
<p> Override on a per-project basis by providing a project-specific gp_item_default_embedded_path_override function. </p>
<pre>GP_RESOLVE_ITEM(&lt;context&gt; &lt;item&gt; &lt;exepath&gt; &lt;dirs&gt; &lt;resolved_item_var&gt;
 [&lt;rpaths&gt;])</pre>
<p>Resolve an item into an existing full path file. </p>
<p> Override on a per-project basis by providing a project-specific gp_resolve_item_override function. </p>
<pre>GP_RESOLVED_FILE_TYPE(&lt;original_file&gt; &lt;file&gt; &lt;exepath&gt; &lt;dirs&gt; &lt;type_var&gt;
 [&lt;rpaths&gt;])</pre>
<p>Return the type of &lt;file&gt; with respect to &lt;original_file&gt;. String describing type of prerequisite is returned in variable named &lt;type_var&gt;. </p>
<p> Use &lt;exepath&gt; and &lt;dirs&gt; if necessary to resolve non-absolute &lt;file&gt; values &#8212; but only for non-embedded items. </p>
<p> Possible types are: </p>
<pre>system
local
embedded
other</pre>
<p>Override on a per-project basis by providing a project-specific gp_resolved_file_type_override function. </p>
<pre>GP_FILE_TYPE(&lt;original_file&gt; &lt;file&gt; &lt;type_var&gt;)</pre>
<p>Return the type of &lt;file&gt; with respect to &lt;original_file&gt;. String describing type of prerequisite is returned in variable named &lt;type_var&gt;. </p>
<p> Possible types are: </p>
<pre>system
local
embedded
other</pre>
<h3>GNUInstallDirs</h3>
<p>Define GNU standard installation directories </p>
<p> Provides install directory variables as defined by the <i>GNU Coding Standards</i>.</p>
<h3>Result Variables</h3>
<p>Inclusion of this module defines the following variables: </p>
<p> <code>CMAKE_INSTALL_&lt;dir&gt;</code> Destination for files of a given type. This value may be passed to the <code>DESTINATION</code> options of <code>install()</code> commands for the corresponding file type. It should typically be a path relative to the installation prefix so that it can be converted to an absolute path in a relocatable way (see <code>CMAKE_INSTALL_FULL_&lt;dir&gt;</code>). However, an absolute path is also allowed. </p>
<p> <code>CMAKE_INSTALL_FULL_&lt;dir&gt;</code> The absolute path generated from the corresponding <code>CMAKE_INSTALL_&lt;dir&gt;</code> value. If the value is not already an absolute path, an absolute path is constructed typically by prepending the value of the <code>CMAKE_INSTALL_PREFIX</code> variable. However, there are some <i>special cases</i> as documented below. </p>
<p> where <code>&lt;dir&gt;</code> is one of:</p>
<dl>
<dt><code>BINDIR</code></p>
<dd>user executables (<code>bin</code>)</p>
<dt><code>SBINDIR</code></p>
<dd>system admin executables (<code>sbin</code>)</p>
<dt><code>LIBEXECDIR</code></p>
<dd>program executables (<code>libexec</code>)</p>
<dt><code>SYSCONFDIR</code></p>
<dd>read-only single-machine data (<code>etc</code>)</p>
<dt><code>SHAREDSTATEDIR</code></p>
<dd>modifiable architecture-independent data (<code>com</code>)</p>
<dt><code>LOCALSTATEDIR</code></p>
<dd>modifiable single-machine data (<code>var</code>)</p>
<dt><code>RUNSTATEDIR</code></p>
<dd>New in version 3.9: run-time variable data (<code>LOCALSTATEDIR/run</code>) </p>
<dt><code>LIBDIR</code></p>
<dd>object code libraries (<code>lib</code> or <code>lib64</code> or <code>lib/&lt;multiarch-tuple&gt;</code> on Debian)</p>
<dt><code>INCLUDEDIR</code></p>
<dd>C header files (<code>include</code>)</p>
<dt><code>OLDINCLUDEDIR</code></p>
<dd>C header files for non-gcc (<code>/usr/include</code>)</p>
<dt><code>DATAROOTDIR</code></p>
<dd>read-only architecture-independent data root (<code>share</code>)</p>
<dt><code>DATADIR</code></p>
<dd>read-only architecture-independent data (<code>DATAROOTDIR</code>)</p>
<dt><code>INFODIR</code></p>
<dd>info documentation (<code>DATAROOTDIR/info</code>)</p>
<dt><code>LOCALEDIR</code></p>
<dd>locale-dependent data (<code>DATAROOTDIR/locale</code>)</p>
<dt><code>MANDIR</code></p>
<dd>man documentation (<code>DATAROOTDIR/man</code>)</p>
<dt><code>DOCDIR</code></p>
<dd>documentation root (<code>DATAROOTDIR/doc/PROJECT_NAME</code>) </p>
<p> If the includer does not define a value the above-shown default will be used and the value will appear in the cache for editing by the user.</dl>
<h3>Special Cases</h3>
<p>New in version 3.4. </p>
<p> The following values of <code>CMAKE_INSTALL_PREFIX</code> are special: </p>
<p> <code>/</code> For <code>&lt;dir&gt;</code> other than the <code>SYSCONFDIR</code>, <code>LOCALSTATEDIR</code> and <code>RUNSTATEDIR</code>, the value of <code>CMAKE_INSTALL_&lt;dir&gt;</code> is prefixed with <code>usr/</code> if it is not user-specified as an absolute path. For example, the <code>INCLUDEDIR</code> value <code>include</code> becomes <code>usr/include</code>. This is required by the <i>GNU Coding Standards</i>, which state: When building the complete GNU system, the prefix will be empty and <code>/usr</code> will be a symbolic link to <code>/</code>. </p>
<p> <code>/usr</code> For <code>&lt;dir&gt;</code> equal to <code>SYSCONFDIR</code>, <code>LOCALSTATEDIR</code> or <code>RUNSTATEDIR</code>, the <code>CMAKE_INSTALL_FULL_&lt;dir&gt;</code> is computed by prepending just <code>/</code> to the value of <code>CMAKE_INSTALL_&lt;dir&gt;</code> if it is not user-specified as an absolute path. For example, the <code>SYSCONFDIR</code> value <code>etc</code> becomes <code>/etc</code>. This is required by the <i>GNU Coding Standards</i>. </p>
<p> <code>/opt/&#8230;</code> For <code>&lt;dir&gt;</code> equal to <code>SYSCONFDIR</code>, <code>LOCALSTATEDIR</code> or <code>RUNSTATEDIR</code>, the <code>CMAKE_INSTALL_FULL_&lt;dir&gt;</code> is computed by <i>appending</i> the prefix to the value of <code>CMAKE_INSTALL_&lt;dir&gt;</code> if it is not user-specified as an absolute path. For example, the <code>SYSCONFDIR</code> value <code>etc</code> becomes <code>/etc/opt/&#8230;</code>. This is defined by the <i>Filesystem Hierarchy Standard</i>.</p>
<h3>Macros</h3>
<dl>
<dt><code>GNUInstallDirs_get_absolute_install_dir</code></p>
<dd>
<pre>GNUInstallDirs_get_absolute_install_dir(absvar var dirname)</pre>
<p>New in version 3.7. </p>
<p> Set the given variable <code>absvar</code> to the absolute path contained within the variable <code>var</code>. This is to allow the computation of an absolute path, accounting for all the special cases documented above. While this macro is used to compute the various <code>CMAKE_INSTALL_FULL_&lt;dir&gt;</code> variables, it is exposed publicly to allow users who create additional path variables to also compute absolute paths where necessary, using the same logic. <code>dirname</code> is the directory name to get, e.g. <code>BINDIR</code>. </p>
<p> Changed in version 3.20: Added the <code>&lt;dirname&gt;</code> parameter. Previous versions of CMake passed this value through the variable <code>${dir}</code>. </p>
</dl>
<h3>GoogleTest</h3>
<p>New in version 3.9. </p>
<p> This module defines functions to help use the Google Test infrastructure. Two mechanisms for adding tests are provided. <i>gtest_add_tests()</i> has been around for some time, originally via <code>find_package(GTest)</code>. <i>gtest_discover_tests()</i> was introduced in CMake 3.10. </p>
<p> The (older) <i>gtest_add_tests()</i> scans source files to identify tests. This is usually effective, with some caveats, including in cross-compiling environments, and makes setting additional properties on tests more convenient. However, its handling of parameterized tests is less comprehensive, and it requires re-running CMake to detect changes to the list of tests. </p>
<p> The (newer) <i>gtest_discover_tests()</i> discovers tests by asking the compiled test executable to enumerate its tests. This is more robust and provides better handling of parameterized tests, and does not require CMake to be re-run when tests change. However, it may not work in a cross-compiling environment, and setting test properties is less convenient. </p>
<p> More details can be found in the documentation of the respective functions. </p>
<p> Both commands are intended to replace use of <code>add_test()</code> to register tests, and will create a separate CTest test for each Google Test test case. Note that this is in some cases less efficient, as common set-up and tear-down logic cannot be shared by multiple test cases executing in the same instance. However, it provides more fine-grained pass/fail information to CTest, which is usually considered as more beneficial. By default, the CTest test name is the same as the Google Test name (i.e. <code>suite.testcase</code>); see also <code>TEST_PREFIX</code> and <code>TEST_SUFFIX</code>.</p>
<dl>
<dt><code>gtest_add_tests</code></p>
<dd>Automatically add tests with CTest by scanning source code for Google Test macros: </p>
<pre>gtest_add_tests(TARGET target
 [SOURCES src1...]
 [EXTRA_ARGS arg1...]
 [WORKING_DIRECTORY dir]
 [TEST_PREFIX prefix]
 [TEST_SUFFIX suffix]
 [SKIP_DEPENDENCY]
 [TEST_LIST outVar]
)</pre>
<p><code>gtest_add_tests</code> attempts to identify tests by scanning source files. Although this is generally effective, it uses only a basic regular expression match, which can be defeated by atypical test declarations, and is unable to fully &quot;split&quot; parameterized tests. Additionally, it requires that CMake be re-run to discover any newly added, removed or renamed tests (by default, this means that CMake is re-run when any test source file is changed, but see <code>SKIP_DEPENDENCY</code>). However, it has the advantage of declaring tests at CMake time, which somewhat simplifies setting additional properties on tests, and always works in a cross-compiling environment. </p>
<p> The options are:</p>
<dt><code>TARGET target</code></p>
<dd>Specifies the Google Test executable, which must be a known CMake executable target. CMake will substitute the location of the built executable when running the test.</p>
<dt><code>SOURCES src1&#8230;</code></p>
<dd>When provided, only the listed files will be scanned for test cases. If this option is not given, the <code>SOURCES</code> property of the specified <code>target</code> will be used to obtain the list of sources.</p>
<dt><code>EXTRA_ARGS arg1&#8230;</code></p>
<dd>Any extra arguments to pass on the command line to each test case.</p>
<dt><code>WORKING_DIRECTORY dir</code></p>
<dd>Specifies the directory in which to run the discovered test cases. If this option is not provided, the current binary directory is used.</p>
<dt><code>TEST_PREFIX prefix</code></p>
<dd>Specifies a <code>prefix</code> to be prepended to the name of each discovered test case. This can be useful when the same source files are being used in multiple calls to <code>gtest_add_test()</code> but with different <code>EXTRA_ARGS</code>.</p>
<dt><code>TEST_SUFFIX suffix</code></p>
<dd>Similar to <code>TEST_PREFIX</code> except the <code>suffix</code> is appended to the name of every discovered test case. Both <code>TEST_PREFIX</code> and <code>TEST_SUFFIX</code> may be specified.</p>
<dt><code>SKIP_DEPENDENCY</code></p>
<dd>Normally, the function creates a dependency which will cause CMake to be re-run if any of the sources being scanned are changed. This is to ensure that the list of discovered tests is updated. If this behavior is not desired (as may be the case while actually writing the test cases), this option can be used to prevent the dependency from being added.</p>
<dt><code>TEST_LIST outVar</code></p>
<dd>The variable named by <code>outVar</code> will be populated in the calling scope with the list of discovered test cases. This allows the caller to do things like manipulate test properties of the discovered tests. </p>
<p> Usage example: </p>
<pre>include(GoogleTest)
add_executable(FooTest FooUnitTest.cxx)
gtest_add_tests(TARGET FooTest
 TEST_SUFFIX .noArgs
 TEST_LIST noArgsTests
)
gtest_add_tests(TARGET FooTest
 EXTRA_ARGS --someArg someValue
 TEST_SUFFIX .withArgs
 TEST_LIST withArgsTests
)
set_tests_properties(${noArgsTests} PROPERTIES TIMEOUT 10)
set_tests_properties(${withArgsTests} PROPERTIES TIMEOUT 20)</pre>
<p>For backward compatibility, the following form is also supported: </p>
<pre>gtest_add_tests(exe args files...)</pre>
<dt><code>exe</code></p>
<dd>The path to the test executable or the name of a CMake target.</p>
<dt><code>args</code></p>
<dd>A ;-list of extra arguments to be passed to executable. The entire list must be passed as a single argument. Enclose it in quotes, or pass <code>&quot;&quot;</code> for no arguments.</p>
<dt><code>files&#8230;</code></p>
<dd>A list of source files to search for tests and test fixtures. Alternatively, use <code>AUTO</code> to specify that <code>exe</code> is the name of a CMake executable target whose sources should be scanned. </p>
<pre>include(GoogleTest)
set(FooTestArgs --foo 1 --bar 2)
add_executable(FooTest FooUnitTest.cxx)
gtest_add_tests(FooTest &quot;${FooTestArgs}&quot; AUTO)</pre>
<dt><code>gtest_discover_tests</code></p>
<dd>Automatically add tests with CTest by querying the compiled test executable for available tests: </p>
<pre>gtest_discover_tests(target
 [EXTRA_ARGS arg1...]
 [WORKING_DIRECTORY dir]
 [TEST_PREFIX prefix]
 [TEST_SUFFIX suffix]
 [TEST_FILTER expr]
 [NO_PRETTY_TYPES] [NO_PRETTY_VALUES]
 [PROPERTIES name1 value1...]
 [TEST_LIST var]
 [DISCOVERY_TIMEOUT seconds]
 [XML_OUTPUT_DIR dir]
 [DISCOVERY_MODE &lt;POST_BUILD|PRE_TEST&gt;]
)</pre>
<p>New in version 3.10. </p>
<p> <code>gtest_discover_tests()</code> sets up a post-build command on the test executable that generates the list of tests by parsing the output from running the test with the <code>&#8211;gtest_list_tests</code> argument. Compared to the source parsing approach of <i>gtest_add_tests()</i>, this ensures that the full list of tests, including instantiations of parameterized tests, is obtained. Since test discovery occurs at build time, it is not necessary to re-run CMake when the list of tests changes. However, it requires that <code>CROSSCOMPILING_EMULATOR</code> is properly set in order to function in a cross-compiling environment. </p>
<p> Additionally, setting properties on tests is somewhat less convenient, since the tests are not available at CMake time. Additional test properties may be assigned to the set of tests as a whole using the <code>PROPERTIES</code> option. If more fine-grained test control is needed, custom content may be provided through an external CTest script using the <code>TEST_INCLUDE_FILES</code> directory property. The set of discovered tests is made accessible to such a script via the <code>&lt;target&gt;_TESTS</code> variable. </p>
<p> The options are:</p>
<dt><code>target</code></p>
<dd>Specifies the Google Test executable, which must be a known CMake executable target. CMake will substitute the location of the built executable when running the test.</p>
<dt><code>EXTRA_ARGS arg1&#8230;</code></p>
<dd>Any extra arguments to pass on the command line to each test case.</p>
<dt><code>WORKING_DIRECTORY dir</code></p>
<dd>Specifies the directory in which to run the discovered test cases. If this option is not provided, the current binary directory is used.</p>
<dt><code>TEST_PREFIX prefix</code></p>
<dd>Specifies a <code>prefix</code> to be prepended to the name of each discovered test case. This can be useful when the same test executable is being used in multiple calls to <code>gtest_discover_tests()</code> but with different <code>EXTRA_ARGS</code>.</p>
<dt><code>TEST_SUFFIX suffix</code></p>
<dd>Similar to <code>TEST_PREFIX</code> except the <code>suffix</code> is appended to the name of every discovered test case. Both <code>TEST_PREFIX</code> and <code>TEST_SUFFIX</code> may be specified.</p>
<dt><code>TEST_FILTER expr</code></p>
<dd>New in version 3.22. </p>
<p> Filter expression to pass as a <code>&#8211;gtest_filter</code> argument during test discovery. Note that the expression is a wildcard-based format that matches against the original test names as used by gtest. For type or value-parameterized tests, these names may be different to the potentially pretty-printed test names that <code>ctest</code> uses.</p>
<dt><code>NO_PRETTY_TYPES</code></p>
<dd>By default, the type index of type-parameterized tests is replaced by the actual type name in the CTest test name. If this behavior is undesirable (e.g. because the type names are unwieldy), this option will suppress this behavior.</p>
<dt><code>NO_PRETTY_VALUES</code></p>
<dd>By default, the value index of value-parameterized tests is replaced by the actual value in the CTest test name. If this behavior is undesirable (e.g. because the value strings are unwieldy), this option will suppress this behavior.</p>
<dt><code>PROPERTIES name1 value1&#8230;</code></p>
<dd>Specifies additional properties to be set on all tests discovered by this invocation of <code>gtest_discover_tests()</code>.</p>
<dt><code>TEST_LIST var</code></p>
<dd>Make the list of tests available in the variable <code>var</code>, rather than the default <code>&lt;target&gt;_TESTS</code>. This can be useful when the same test executable is being used in multiple calls to <code>gtest_discover_tests()</code>. Note that this variable is only available in CTest.</p>
<dt><code>DISCOVERY_TIMEOUT num</code></p>
<dd>New in version 3.10.3. </p>
<p> Specifies how long (in seconds) CMake will wait for the test to enumerate available tests. If the test takes longer than this, discovery (and your build) will fail. Most test executables will enumerate their tests very quickly, but under some exceptional circumstances, a test may require a longer timeout. The default is 5. See also the <code>TIMEOUT</code> option of <code>execute_process()</code>. </p>
<p> <code>NOTE:</code> In CMake versions 3.10.1 and 3.10.2, this option was called <code>TIMEOUT</code>. This clashed with the <code>TIMEOUT</code> test property, which is one of the common properties that would be set with the <code>PROPERTIES</code> keyword, usually leading to legal but unintended behavior. The keyword was changed to <code>DISCOVERY_TIMEOUT</code> in CMake 3.10.3 to address this problem. The ambiguous behavior of the <code>TIMEOUT</code> keyword in 3.10.1 and 3.10.2 has not been preserved.</p>
<dt><code>XML_OUTPUT_DIR dir</code></p>
<dd>New in version 3.18. </p>
<p> If specified, the parameter is passed along with <code>&#8211;gtest_output=xml:</code> to test executable. The actual file name is the same as the test target, including prefix and suffix. This should be used instead of <code>EXTRA_ARGS &#8211;gtest_output=xml</code> to avoid race conditions writing the XML result output when using parallel test execution.</p>
<dt><code>DISCOVERY_MODE</code></p>
<dd>New in version 3.18. </p>
<p> Provides greater control over when <code>gtest_discover_tests()</code> performs test discovery. By default, <code>POST_BUILD</code> sets up a post-build command to perform test discovery at build time. In certain scenarios, like cross-compiling, this <code>POST_BUILD</code> behavior is not desirable. By contrast, <code>PRE_TEST</code> delays test discovery until just prior to test execution. This way test discovery occurs in the target environment where the test has a better chance at finding appropriate runtime dependencies. </p>
<p> <code>DISCOVERY_MODE</code> defaults to the value of the <code>CMAKE_GTEST_DISCOVER_TESTS_DISCOVERY_MODE</code> variable if it is not passed when calling <code>gtest_discover_tests()</code>. This provides a mechanism for globally selecting a preferred test discovery behavior without having to modify each call site.</dl>
<h3>InstallRequiredSystemLibraries</h3>
<p>Include this module to search for compiler-provided system runtime libraries and add install rules for them. Some optional variables may be set prior to including the module to adjust behavior:</p>
<dl>
<dt><code>CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS</code></p>
<dd>Specify additional runtime libraries that may not be detected. After inclusion any detected libraries will be appended to this.</p>
<dt><code>CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS_SKIP</code></p>
<dd>Set to TRUE to skip calling the <code>install(PROGRAMS)</code> command to allow the includer to specify its own install rule, using the value of <code>CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS</code> to get the list of libraries.</p>
<dt><code>CMAKE_INSTALL_DEBUG_LIBRARIES</code></p>
<dd>Set to TRUE to install the debug runtime libraries when available with MSVC tools.</p>
<dt><code>CMAKE_INSTALL_DEBUG_LIBRARIES_ONLY</code></p>
<dd>Set to TRUE to install only the debug runtime libraries with MSVC tools even if the release runtime libraries are also available.</p>
<dt><code>CMAKE_INSTALL_UCRT_LIBRARIES</code></p>
<dd>New in version 3.6. </p>
<p> Set to TRUE to install the Windows Universal CRT libraries for app-local deployment (e.g. to Windows XP). This is meaningful only with MSVC from Visual Studio 2015 or higher. </p>
<p> New in version 3.9: One may set a <code>CMAKE_WINDOWS_KITS_10_DIR</code> <i>environment variable</i> to an absolute path to tell CMake to look for Windows 10 SDKs in a custom location. The specified directory is expected to contain <code>Redist/ucrt/DLLs/*</code> directories. </p>
<dt><code>CMAKE_INSTALL_MFC_LIBRARIES</code></p>
<dd>Set to TRUE to install the MSVC MFC runtime libraries.</p>
<dt><code>CMAKE_INSTALL_OPENMP_LIBRARIES</code></p>
<dd>Set to TRUE to install the MSVC OpenMP runtime libraries</p>
<dt><code>CMAKE_INSTALL_SYSTEM_RUNTIME_DESTINATION</code></p>
<dd>Specify the <code>install(PROGRAMS)</code> command <code>DESTINATION</code> option. If not specified, the default is <code>bin</code> on Windows and <code>lib</code> elsewhere.</p>
<dt><code>CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS_NO_WARNINGS</code></p>
<dd>Set to TRUE to disable warnings about required library files that do not exist. (For example, Visual Studio Express editions may not provide the redistributable files.)</p>
<dt><code>CMAKE_INSTALL_SYSTEM_RUNTIME_COMPONENT</code></p>
<dd>New in version 3.3. </p>
<p> Specify the <code>install(PROGRAMS)</code> command <code>COMPONENT</code> option. If not specified, no such option will be used. </p>
<p> New in version 3.10: Support for installing Intel compiler runtimes. </p>
</dl>
<h3>ProcessorCount</h3>
<p>ProcessorCount(var) </p>
<p> Determine the number of processors/cores and save value in ${var} </p>
<p> Sets the variable named ${var} to the number of physical cores available on the machine if the information can be determined. Otherwise it is set to 0. Currently this functionality is implemented for AIX, cygwin, FreeBSD, HPUX, Linux, macOS, QNX, Sun and Windows. </p>
<p> Changed in version 3.15: On Linux, returns the container CPU count instead of the host CPU count. </p>
<p> This function is guaranteed to return a positive integer (&gt;=1) if it succeeds. It returns 0 if there&#8217;s a problem determining the processor count. </p>
<p> Example use, in a ctest -S dashboard script: </p>
<pre>include(ProcessorCount)
ProcessorCount(N)
if(NOT N EQUAL 0)
 set(CTEST_BUILD_FLAGS -j${N})
 set(ctest_test_args ${ctest_test_args} PARALLEL_LEVEL ${N})
endif()</pre>
<p>This function is intended to offer an approximation of the value of the number of compute cores available on the current machine, such that you may use that value for parallel building and parallel testing. It is meant to help utilize as much of the machine as seems reasonable. Of course, knowledge of what else might be running on the machine simultaneously should be used when deciding whether to request a machine&#8217;s full capacity all for yourself.</p>
<h3>SelectLibraryConfigurations</h3>
<pre>select_library_configurations(basename)</pre>
<p>This macro takes a library base name as an argument, and will choose good values for the variables </p>
<pre>basename_LIBRARY
basename_LIBRARIES
basename_LIBRARY_DEBUG
basename_LIBRARY_RELEASE</pre>
<p>depending on what has been found and set. </p>
<p> If only <code>basename_LIBRARY_RELEASE</code> is defined, <code>basename_LIBRARY</code> will be set to the release value, and <code>basename_LIBRARY_DEBUG</code> will be set to <code>basename_LIBRARY_DEBUG-NOTFOUND</code>. If only <code>basename_LIBRARY_DEBUG</code> is defined, then <code>basename_LIBRARY</code> will take the debug value, and <code>basename_LIBRARY_RELEASE</code> will be set to <code>basename_LIBRARY_RELEASE-NOTFOUND</code>. </p>
<p> If the generator supports configuration types, then <code>basename_LIBRARY</code> and <code>basename_LIBRARIES</code> will be set with debug and optimized flags specifying the library to be used for the given configuration. If no build type has been set or the generator in use does not support configuration types, then <code>basename_LIBRARY</code> and <code>basename_LIBRARIES</code> will take only the release value, or the debug value if the release one is not set.</p>
<h3>SquishTestScript</h3>
<p>This script launches a GUI test using Squish. You should not call the script directly; instead, you should access it via the SQUISH_ADD_TEST macro that is defined in FindSquish.cmake. </p>
<p> This script starts the Squish server, launches the test on the client, and finally stops the squish server. If any of these steps fail (including if the tests do not pass) then a fatal error is raised.</p>
<h3>TestBigEndian</h3>
<p>Deprecated since version 3.20: Supserseded by the <code>CMAKE_&lt;LANG&gt;_BYTE_ORDER</code> variable. </p>
<p> Check if the target architecture is big endian or little endian.</p>
<dl>
<dt><code>test_big_endian</code></p>
<dd>
<pre>test_big_endian(&lt;var&gt;)</pre>
<p>Stores in variable <code>&lt;var&gt;</code> either 1 or 0 indicating whether the target architecture is big or little endian.</dl>
<h3>TestForANSIForScope</h3>
<p>Check for ANSI for scope support </p>
<p> Check if the compiler restricts the scope of variables declared in a for-init-statement to the loop body. </p>
<pre>CMAKE_NO_ANSI_FOR_SCOPE - holds result</pre>
<h3>TestForANSIStreamHeaders</h3>
<p>Test for compiler support of ANSI stream headers iostream, etc. </p>
<p> check if the compiler supports the standard ANSI iostream header (without the .h) </p>
<pre>CMAKE_NO_ANSI_STREAM_HEADERS - defined by the results</pre>
<h3>TestForSSTREAM</h3>
<p>Test for compiler support of ANSI sstream header </p>
<p> check if the compiler supports the standard ANSI sstream header </p>
<pre>CMAKE_NO_ANSI_STRING_STREAM - defined by the results</pre>
<h3>TestForSTDNamespace</h3>
<p>Test for std:: namespace support </p>
<p> check if the compiler supports std:: on stl classes </p>
<pre>CMAKE_NO_STD_NAMESPACE - defined by the results</pre>
<h3>UseEcos</h3>
<p>This module defines variables and macros required to build eCos application. </p>
<p> This file contains the following macros: ECOS_ADD_INCLUDE_DIRECTORIES() &#8211; add the eCos include dirs ECOS_ADD_EXECUTABLE(name source1 &#8230; sourceN ) &#8211; create an eCos executable ECOS_ADJUST_DIRECTORY(VAR source1 &#8230; sourceN ) &#8211; adjusts the path of the source files and puts the result into VAR </p>
<p> Macros for selecting the toolchain: ECOS_USE_ARM_ELF_TOOLS() &#8211; enable the ARM ELF toolchain for the directory where it is called ECOS_USE_I386_ELF_TOOLS() &#8211; enable the i386 ELF toolchain for the directory where it is called ECOS_USE_PPC_EABI_TOOLS() &#8211; enable the PowerPC toolchain for the directory where it is called </p>
<p> It contains the following variables: ECOS_DEFINITIONS ECOSCONFIG_EXECUTABLE ECOS_CONFIG_FILE &#8211; defaults to ecos.ecc, if your eCos configuration file has a different name, adjust this variable for internal use only: </p>
<pre>ECOS_ADD_TARGET_LIB</pre>
<h3>UseJava</h3>
<p>This file provides support for <code>Java</code>. It is assumed that <code>FindJava</code> has already been loaded. See <code>FindJava</code> for information on how to load Java into your <code>CMake</code> project.</p>
<h3>Synopsis</h3>
<pre><i>Creating and Installing JARS</i>
 <i>add_jar</i> (&lt;target_name&gt; [SOURCES] &lt;source1&gt; [&lt;source2&gt;...] ...)
 <i>install_jar</i> (&lt;target_name&gt; DESTINATION &lt;destination&gt; [COMPONENT &lt;component&gt;])
 <i>install_jni_symlink</i> (&lt;target_name&gt; DESTINATION &lt;destination&gt; [COMPONENT &lt;component&gt;])
<i>Header Generation</i>
 <i>create_javah</i> ((TARGET &lt;target&gt; | GENERATED_FILES &lt;VAR&gt;) CLASSES &lt;class&gt;... ...)
<i>Exporting JAR Targets</i>
 <i>install_jar_exports</i> (TARGETS &lt;jars&gt;... FILE &lt;filename&gt; DESTINATION &lt;destination&gt; ...)
 <i>export_jars</i> (TARGETS &lt;jars&gt;... [NAMESPACE &lt;namespace&gt;] FILE &lt;filename&gt;)
<i>Finding JARs</i>
 <i>find_jar</i> (&lt;VAR&gt; NAMES &lt;name1&gt; [&lt;name2&gt;...] [PATHS &lt;path1&gt; [&lt;path2&gt;... ENV &lt;var&gt;]] ...)
<i>Creating Java Documentation</i>
 <i>create_javadoc</i> (&lt;VAR&gt; (PACKAGES &lt;pkg1&gt; [&lt;pkg2&gt;...] | FILES &lt;file1&gt; [&lt;file2&gt;...]) ...)</pre>
<h3>Creating And Installing JARs</h3>
<dl>
<dt><code>add_jar</code></p>
<dd>Creates a jar file containing java objects and, optionally, resources: </p>
<pre>add_jar(&lt;target_name&gt;
 [SOURCES] &lt;source1&gt; [&lt;source2&gt;...] [&lt;resource1&gt;...]
 [RESOURCES NAMESPACE &lt;ns1&gt; &lt;resource1&gt;... [NAMESPACE &lt;nsX&gt; &lt;resourceX&gt;...]... ]
 [INCLUDE_JARS &lt;jar1&gt; [&lt;jar2&gt;...]]
 [ENTRY_POINT &lt;entry&gt;]
 [VERSION &lt;version&gt;]
 [MANIFEST &lt;manifest&gt;]
 [OUTPUT_NAME &lt;name&gt;]
 [OUTPUT_DIR &lt;dir&gt;]
 [GENERATE_NATIVE_HEADERS &lt;target&gt;
 [DESTINATION (&lt;dir&gt;|INSTALL &lt;dir&gt; [BUILD &lt;dir&gt;])]]
 )</pre>
<p>This command creates a <code>&lt;target_name&gt;.jar</code>. It compiles the given <code>&lt;source&gt;</code> files and adds the given <code>&lt;resource&gt;</code> files to the jar file. Source files can be java files or listing files (prefixed by <code>@</code>). If only resource files are given then just a jar file is created.</p>
<dt><code>SOURCES</code></p>
<dd>Compiles the specified source files and adds the result in the jar file. </p>
<p> New in version 3.4: Support for response files, prefixed by <code>@</code>. </p>
<dt><code>RESOURCES</code></p>
<dd>New in version 3.21. </p>
<p> Adds the named <code>&lt;resource&gt;</code> files to the jar by stripping the source file path and placing the file beneath <code>&lt;ns&gt;</code> within the jar. </p>
<p> For example: </p>
<pre>RESOURCES NAMESPACE &quot;/com/my/namespace&quot; &quot;a/path/to/resource.txt&quot;</pre>
<p>results in a resource accessible via <code>/com/my/namespace/resource.txt</code> within the jar. </p>
<p> Resources may be added without adjusting the namespace by adding them to the list of <code>SOURCES</code> (original behavior), in this case, resource paths must be relative to <code>CMAKE_CURRENT_SOURCE_DIR</code>. Adding resources without using the <code>RESOURCES</code> parameter in out of source builds will almost certainly result in confusion. </p>
<p> <code>NOTE:</code> Adding resources via the <code>SOURCES</code> parameter relies upon a hard-coded list of file extensions which are tested to determine whether they compile (e.g. File.java). <code>SOURCES</code> files which match the extensions are compiled. Files which do not match are treated as resources. To include uncompiled resources matching those file extensions use the <code>RESOURCES</code> parameter.</p>
<dt><code>INCLUDE_JARS</code></p>
<dd>The list of jars are added to the classpath when compiling the java sources and also to the dependencies of the target. <code>INCLUDE_JARS</code> also accepts other target names created by <code>add_jar()</code>. For backwards compatibility, jar files listed as sources are ignored (as they have been since the first version of this module).</p>
<dt><code>ENTRY_POINT</code></p>
<dd>Defines an entry point in the jar file.</p>
<dt><code>VERSION</code></p>
<dd>Adds a version to the target output name. </p>
<p> The following example will create a jar file with the name <code>shibboleet-1.2.0.jar</code> and will create a symlink <code>shibboleet.jar</code> pointing to the jar with the version information. </p>
<pre>add_jar(shibboleet shibbotleet.java VERSION 1.2.0)</pre>
<dt><code>MANIFEST</code></p>
<dd>Defines a custom manifest for the jar.</p>
<dt><code>OUTPUT_NAME</code></p>
<dd>Specify a different output name for the target.</p>
<dt><code>OUTPUT_DIR</code></p>
<dd>Sets the directory where the jar file will be generated. If not specified, <code>CMAKE_CURRENT_BINARY_DIR</code> is used as the output directory.</p>
<dt><code>GENERATE_NATIVE_HEADERS</code></p>
<dd>New in version 3.11. </p>
<p> Generates native header files for methods declared as native. These files provide the connective glue that allow your Java and C code to interact. An INTERFACE target will be created for an easy usage of generated files. Sub-option <code>DESTINATION</code> can be used to specify the output directory for generated header files. </p>
<p> This option requires, at least, version 1.8 of the JDK. </p>
<p> For an optimum usage of this option, it is recommended to include module JNI before any call to <code>add_jar()</code>. The produced target for native headers can then be used to compile C/C++ sources with the <code>target_link_libraries()</code> command. </p>
<pre>find_package(JNI)
add_jar(foo foo.java GENERATE_NATIVE_HEADERS foo-native)
add_library(bar bar.cpp)
target_link_libraries(bar PRIVATE foo-native)</pre>
<p>New in version 3.20: <code>DESTINATION</code> sub-option now supports the possibility to specify different output directories for <code>BUILD</code> and <code>INSTALL</code> steps. If <code>BUILD</code> directory is not specified, a default directory will be used. </p>
<p> To export the interface target generated by <code>GENERATE_NATIVE_HEADERS</code> option, sub-option <code>INSTALL</code> of <code>DESTINATION</code> is required: </p>
<pre>add_jar(foo foo.java GENERATE_NATIVE_HEADERS foo-native
 DESTINATION INSTALL include)
install(TARGETS foo-native EXPORT native)
install(DIRECTORY &quot;$&lt;TARGET_PROPERTY:foo-native,NATIVE_HEADERS_DIRECTORY&gt;/&quot;
 DESTINATION include)
install(EXPORT native DESTINATION /to/export NAMESPACE foo)</pre>
<p>Some variables can be set to customize the behavior of <code>add_jar()</code> as well as the java compiler:</p>
<dt><code>CMAKE_JAVA_COMPILE_FLAGS</code></p>
<dd>Specify additional flags to java compiler.</p>
<dt><code>CMAKE_JAVA_INCLUDE_PATH</code></p>
<dd>Specify additional paths to the class path.</p>
<dt><code>CMAKE_JNI_TARGET</code></p>
<dd>If the target is a JNI library, sets this boolean variable to <code>TRUE</code> to enable creation of a JNI symbolic link (see also <i>install_jni_symlink()</i>).</p>
<dt><code>CMAKE_JAR_CLASSES_PREFIX</code></p>
<dd>If multiple jars should be produced from the same java source filetree, to prevent the accumulation of duplicate class files in subsequent jars, set/reset <code>CMAKE_JAR_CLASSES_PREFIX</code> prior to calling the <code>add_jar()</code>: </p>
<pre>set(CMAKE_JAR_CLASSES_PREFIX com/redhat/foo)
add_jar(foo foo.java)
set(CMAKE_JAR_CLASSES_PREFIX com/redhat/bar)
add_jar(bar bar.java)</pre>
<p>The <code>add_jar()</code> function sets the following target properties on <code>&lt;target_name&gt;</code>:</p>
<dt><code>INSTALL_FILES</code></p>
<dd>The files which should be installed. This is used by <i>install_jar()</i>.</p>
<dt><code>JNI_SYMLINK</code></p>
<dd>The JNI symlink which should be installed. This is used by <i>install_jni_symlink()</i>.</p>
<dt><code>JAR_FILE</code></p>
<dd>The location of the jar file so that you can include it.</p>
<dt><code>CLASSDIR</code></p>
<dd>The directory where the class files can be found. For example to use them with <code>javah</code>.</p>
<dt><code>NATIVE_HEADERS_DIRECTORY</code></p>
<dd>New in version 3.20. </p>
<p> The directory where native headers are generated. Defined when option <code>GENERATE_NATIVE_HEADERS</code> is specified.</p>
<dt><code>install_jar</code></p>
<dd>This command installs the jar file to the given destination: </p>
<pre>install_jar(&lt;target_name&gt; &lt;destination&gt;)
install_jar(&lt;target_name&gt; DESTINATION &lt;destination&gt; [COMPONENT &lt;component&gt;])</pre>
<p>This command installs the <code>&lt;target_name&gt;</code> file to the given <code>&lt;destination&gt;</code>. It should be called in the same scope as <i>add_jar()</i> or it will fail. </p>
<p> New in version 3.4: The second signature with <code>DESTINATION</code> and <code>COMPONENT</code> options. </p>
<dt><code>DESTINATION</code></p>
<dd>Specify the directory on disk to which a file will be installed.</p>
<dt><code>COMPONENT</code></p>
<dd>Specify an installation component name with which the install rule is associated, such as &quot;runtime&quot; or &quot;development&quot;. </p>
<p> The <code>install_jar()</code> command sets the following target properties on <code>&lt;target_name&gt;</code>:</p>
<dt><code>INSTALL_DESTINATION</code></p>
<dd>Holds the <code>&lt;destination&gt;</code> as described above, and is used by <i>install_jar_exports()</i>.</p>
<dt><code>install_jni_symlink</code></p>
<dd>Installs JNI symlinks for target generated by <i>add_jar()</i>: </p>
<pre>install_jni_symlink(&lt;target_name&gt; &lt;destination&gt;)
install_jni_symlink(&lt;target_name&gt; DESTINATION &lt;destination&gt; [COMPONENT &lt;component&gt;])</pre>
<p>This command installs the <code>&lt;target_name&gt;</code> JNI symlinks to the given <code>&lt;destination&gt;</code>. It should be called in the same scope as <i>add_jar()</i> or it will fail. </p>
<p> New in version 3.4: The second signature with <code>DESTINATION</code> and <code>COMPONENT</code> options. </p>
<dt><code>DESTINATION</code></p>
<dd>Specify the directory on disk to which a file will be installed.</p>
<dt><code>COMPONENT</code></p>
<dd>Specify an installation component name with which the install rule is associated, such as &quot;runtime&quot; or &quot;development&quot;. </p>
<p> Utilize the following commands to create a JNI symbolic link: </p>
<pre>set(CMAKE_JNI_TARGET TRUE)
add_jar(shibboleet shibbotleet.java VERSION 1.2.0)
install_jar(shibboleet ${LIB_INSTALL_DIR}/shibboleet)
install_jni_symlink(shibboleet ${JAVA_LIB_INSTALL_DIR})</pre>
</dl>
<h3>Header Generation</h3>
<dl>
<dt><code>create_javah</code></p>
<dd>New in version 3.4. </p>
<p> Generates C header files for java classes: </p>
<pre>create_javah(TARGET &lt;target&gt; | GENERATED_FILES &lt;VAR&gt;
 CLASSES &lt;class&gt;...
 [CLASSPATH &lt;classpath&gt;...]
 [DEPENDS &lt;depend&gt;...]
 [OUTPUT_NAME &lt;path&gt;|OUTPUT_DIR &lt;path&gt;]
 )</pre>
<p>Deprecated since version 3.11: This command will no longer be supported starting with version 10 of the JDK due to the <i>suppression of javah tool</i>. The <i>add_jar(GENERATE_NATIVE_HEADERS)</i> command should be used instead. </p>
<p> Create C header files from java classes. These files provide the connective glue that allow your Java and C code to interact. </p>
<p> There are two main signatures for <code>create_javah()</code>. The first signature returns generated files through variable specified by the <code>GENERATED_FILES</code> option. For example: </p>
<pre>create_javah(GENERATED_FILES files_headers
 CLASSES org.cmake.HelloWorld
 CLASSPATH hello.jar
)</pre>
<p>The second signature for <code>create_javah()</code> creates a target which encapsulates header files generation. E.g. </p>
<pre>create_javah(TARGET target_headers
 CLASSES org.cmake.HelloWorld
 CLASSPATH hello.jar
)</pre>
<p>Both signatures share same options.</p>
<dt><code>CLASSES</code></p>
<dd>Specifies Java classes used to generate headers.</p>
<dt><code>CLASSPATH</code></p>
<dd>Specifies various paths to look up classes. Here <code>.class</code> files, jar files or targets created by command add_jar can be used.</p>
<dt><code>DEPENDS</code></p>
<dd>Targets on which the javah target depends.</p>
<dt><code>OUTPUT_NAME</code></p>
<dd>Concatenates the resulting header files for all the classes listed by option <code>CLASSES</code> into <code>&lt;path&gt;</code>. Same behavior as option <code>-o</code> of <code>javah</code> tool.</p>
<dt><code>OUTPUT_DIR</code></p>
<dd>Sets the directory where the header files will be generated. Same behavior as option <code>-d</code> of <code>javah</code> tool. If not specified, <code>CMAKE_CURRENT_BINARY_DIR</code> is used as the output directory.</dl>
<h3>Exporting JAR Targets</h3>
<dl>
<dt><code>install_jar_exports</code></p>
<dd>New in version 3.7. </p>
<p> Installs a target export file: </p>
<pre>install_jar_exports(TARGETS &lt;jars&gt;...
 [NAMESPACE &lt;namespace&gt;]
 FILE &lt;filename&gt;
 DESTINATION &lt;destination&gt; [COMPONENT &lt;component&gt;])</pre>
<p>This command installs a target export file <code>&lt;filename&gt;</code> for the named jar targets to the given <code>&lt;destination&gt;</code> directory. Its function is similar to that of <code>install(EXPORT)</code>.</p>
<dt><code>TARGETS</code></p>
<dd>List of targets created by <i>add_jar()</i> command.</p>
<dt><code>NAMESPACE</code></p>
<dd>New in version 3.9. </p>
<p> The <code>&lt;namespace&gt;</code> value will be prepend to the target names as they are written to the import file.</p>
<dt><code>FILE</code></p>
<dd>Specify name of the export file.</p>
<dt><code>DESTINATION</code></p>
<dd>Specify the directory on disk to which a file will be installed.</p>
<dt><code>COMPONENT</code></p>
<dd>Specify an installation component name with which the install rule is associated, such as &quot;runtime&quot; or &quot;development&quot;.</p>
<dt><code>export_jars</code></p>
<dd>New in version 3.7. </p>
<p> Writes a target export file: </p>
<pre>export_jars(TARGETS &lt;jars&gt;...
 [NAMESPACE &lt;namespace&gt;]
 FILE &lt;filename&gt;)</pre>
<p>This command writes a target export file <code>&lt;filename&gt;</code> for the named <code>&lt;jars&gt;</code> targets. Its function is similar to that of <code>export()</code>.</p>
<dt><code>TARGETS</code></p>
<dd>List of targets created by <i>add_jar()</i> command.</p>
<dt><code>NAMESPACE</code></p>
<dd>New in version 3.9. </p>
<p> The <code>&lt;namespace&gt;</code> value will be prepend to the target names as they are written to the import file.</p>
<dt><code>FILE</code></p>
<dd>Specify name of the export file.</dl>
<h3>Finding JARs</h3>
<dl>
<dt><code>find_jar</code></p>
<dd>Finds the specified jar file: </p>
<pre>find_jar(&lt;VAR&gt;
 &lt;name&gt; | NAMES &lt;name1&gt; [&lt;name2&gt;...]
 [PATHS &lt;path1&gt; [&lt;path2&gt;... ENV &lt;var&gt;]]
 [VERSIONS &lt;version1&gt; [&lt;version2&gt;]]
 [DOC &quot;cache documentation string&quot;]
 )</pre>
<p>This command is used to find a full path to the named jar. A cache entry named by <code>&lt;VAR&gt;</code> is created to store the result of this command. If the full path to a jar is found the result is stored in the variable and the search will not repeated unless the variable is cleared. If nothing is found, the result will be <code>&lt;VAR&gt;-NOTFOUND</code>, and the search will be attempted again next time <code>find_jar()</code> is invoked with the same variable.</p>
<dt><code>NAMES</code></p>
<dd>Specify one or more possible names for the jar file.</p>
<dt><code>PATHS</code></p>
<dd>Specify directories to search in addition to the default locations. The <code>ENV</code> var sub-option reads paths from a system environment variable.</p>
<dt><code>VERSIONS</code></p>
<dd>Specify jar versions.</p>
<dt><code>DOC</code></p>
<dd>Specify the documentation string for the <code>&lt;VAR&gt;</code> cache entry.</dl>
<h3>Creating Java Documentation</h3>
<dl>
<dt><code>create_javadoc</code></p>
<dd>Creates java documentation based on files and packages: </p>
<pre>create_javadoc(&lt;VAR&gt;
 (PACKAGES &lt;pkg1&gt; [&lt;pkg2&gt;...] | FILES &lt;file1&gt; [&lt;file2&gt;...])
 [SOURCEPATH &lt;sourcepath&gt;]
 [CLASSPATH &lt;classpath&gt;]
 [INSTALLPATH &lt;install path&gt;]
 [DOCTITLE &lt;the documentation title&gt;]
 [WINDOWTITLE &lt;the title of the document&gt;]
 [AUTHOR (TRUE|FALSE)]
 [USE (TRUE|FALSE)]
 [VERSION (TRUE|FALSE)]
 )</pre>
<p>The <code>create_javadoc()</code> command can be used to create java documentation. There are two main signatures for <code>create_javadoc()</code>. </p>
<p> The first signature works with package names on a path with source files: </p>
<pre>create_javadoc(my_example_doc
 PACKAGES com.example.foo com.example.bar
 SOURCEPATH &quot;${CMAKE_CURRENT_SOURCE_DIR}&quot;
 CLASSPATH ${CMAKE_JAVA_INCLUDE_PATH}
 WINDOWTITLE &quot;My example&quot;
 DOCTITLE &quot;&lt;h1&gt;My example&lt;/h1&gt;&quot;
 AUTHOR TRUE
 USE TRUE
 VERSION TRUE
 )</pre>
<p>The second signature for <code>create_javadoc()</code> works on a given list of files: </p>
<pre>create_javadoc(my_example_doc
 FILES java/A.java java/B.java
 CLASSPATH ${CMAKE_JAVA_INCLUDE_PATH}
 WINDOWTITLE &quot;My example&quot;
 DOCTITLE &quot;&lt;h1&gt;My example&lt;/h1&gt;&quot;
 AUTHOR TRUE
 USE TRUE
 VERSION TRUE
 )</pre>
<p>Both signatures share most of the options. For more details please read the javadoc manpage.</p>
<dt><code>PACKAGES</code></p>
<dd>Specify java packages.</p>
<dt><code>FILES</code></p>
<dd>Specify java source files. If relative paths are specified, they are relative to <code>CMAKE_CURRENT_SOURCE_DIR</code>.</p>
<dt><code>SOURCEPATH</code></p>
<dd>Specify the directory where to look for packages. By default, <code>CMAKE_CURRENT_SOURCE_DIR</code> directory is used.</p>
<dt><code>CLASSPATH</code></p>
<dd>Specify where to find user class files. Same behavior as option <code>-classpath</code> of <code>javadoc</code> tool.</p>
<dt><code>INSTALLPATH</code></p>
<dd>Specify where to install the java documentation. If you specified, the documentation will be installed to <code>${CMAKE_INSTALL_PREFIX}/share/javadoc/&lt;VAR&gt;</code>.</p>
<dt><code>DOCTITLE</code></p>
<dd>Specify the title to place near the top of the overview summary file. Same behavior as option <code>-doctitle</code> of <code>javadoc</code> tool.</p>
<dt><code>WINDOWTITLE</code></p>
<dd>Specify the title to be placed in the HTML <code>&lt;title&gt;</code> tag. Same behavior as option <code>-windowtitle</code> of <code>javadoc</code> tool.</p>
<dt><code>AUTHOR</code></p>
<dd>When value <code>TRUE</code> is specified, includes the <code>@author</code> text in the generated docs. Same behavior as option <code>-author</code> of <code>javadoc</code> tool.</p>
<dt><code>USE</code></p>
<dd>When value <code>TRUE</code> is specified, creates class and package usage pages. Includes one Use page for each documented class and package. Same behavior as option <code>-use</code> of <code>javadoc</code> tool.</p>
<dt><code>VERSION</code></p>
<dd>When value <code>TRUE</code> is specified, includes the version text in the generated docs. Same behavior as option <code>-version</code> of <code>javadoc</code> tool.</dl>
<h3>UseSWIG</h3>
<p>This file provides support for <code>SWIG</code>. It is assumed that <code>FindSWIG</code> module has already been loaded. </p>
<p> Defines the following command for use with <code>SWIG</code>:</p>
<dl>
<dt><code>swig_add_library</code></p>
<dd>New in version 3.8. </p>
<p> Define swig module with given name and specified language: </p>
<pre>swig_add_library(&lt;name&gt;
 [TYPE &lt;SHARED|MODULE|STATIC|USE_BUILD_SHARED_LIBS&gt;]
 LANGUAGE &lt;language&gt;
 [NO_PROXY]
 [OUTPUT_DIR &lt;directory&gt;]
 [OUTFILE_DIR &lt;directory&gt;]
 SOURCES &lt;file&gt;...
 )</pre>
<p>Targets created with the <code>swig_add_library</code> command have the same capabilities as targets created with the <code>add_library()</code> command, so those targets can be used with any command expecting a target (e.g. <code>target_link_libraries()</code>). </p>
<p> Changed in version 3.13: This command creates a target with the specified <code>&lt;name&gt;</code> when policy <code>CMP0078</code> is set to <code>NEW</code>. Otherwise, the legacy behavior will choose a different target name and store it in the <code>SWIG_MODULE_&lt;name&gt;_REAL_NAME</code> variable. </p>
<p> Changed in version 3.15: Alternate library name (set with the <code>OUTPUT_NAME</code> property, for example) will be passed on to <code>Python</code> and <code>CSharp</code> wrapper libraries. </p>
<p> Changed in version 3.21: Generated library use standard naming conventions for <code>CSharp</code> language when policy <code>CMP0122</code> is set to <code>NEW</code>. Otherwise, the legacy behavior is applied. </p>
<p> <code>NOTE:</code> For multi-config generators, this module does not support configuration-specific files generated by <code>SWIG</code>. All build configurations must result in the same generated source file. </p>
<p> <code>NOTE:</code> For Makefile Generators, if, for some sources, the <code>USE_SWIG_DEPENDENCIES</code> property is <code>FALSE</code>, <code>swig_add_library</code> does not track file dependencies, so depending on the <code>&lt;name&gt;_swig_compilation</code> custom target is required for targets which require the <code>swig</code>-generated files to exist. Other generators may depend on the source files that would be generated by SWIG.</p>
<dt><code>TYPE</code></p>
<dd><code>SHARED</code>, <code>MODULE</code> and <code>STATIC</code> have the same semantic as for the <code>add_library()</code> command. If <code>USE_BUILD_SHARED_LIBS</code> is specified, the library type will be <code>STATIC</code> or <code>SHARED</code> based on whether the current value of the <code>BUILD_SHARED_LIBS</code> variable is <code>ON</code>. If no type is specified, <code>MODULE</code> will be used.</p>
<dt><code>LANGUAGE</code></p>
<dd>Specify the target language. </p>
<p> New in version 3.1: Go and Lua language support. </p>
<p> New in version 3.2: R language support. </p>
<p> New in version 3.18: Fortran language support. </p>
<dt><code>NO_PROXY</code></p>
<dd>New in version 3.12. </p>
<p> Prevent the generation of the wrapper layer (swig <code>-noproxy</code> option).</p>
<dt><code>OUTPUT_DIR</code></p>
<dd>New in version 3.12. </p>
<p> Specify where to write the language specific files (swig <code>-outdir</code> option). If not given, the <code>CMAKE_SWIG_OUTDIR</code> variable will be used. If neither is specified, the default depends on the value of the <code>UseSWIG_MODULE_VERSION</code> variable as follows:</p>
<dt>&bull;</p>
<dd>If <code>UseSWIG_MODULE_VERSION</code> is 1 or is undefined, output is written to the <code>CMAKE_CURRENT_BINARY_DIR</code> directory.</p>
<dt>&bull;</p>
<dd>If <code>UseSWIG_MODULE_VERSION</code> is 2, a dedicated directory will be used. The path of this directory can be retrieved from the <code>SWIG_SUPPORT_FILES_DIRECTORY</code> target property.</p>
<dt><code>OUTFILE_DIR</code></p>
<dd>New in version 3.12. </p>
<p> Specify an output directory name where the generated source file will be placed (swig <code>-o</code> option). If not specified, the <code>SWIG_OUTFILE_DIR</code> variable will be used. If neither is specified, <code>OUTPUT_DIR</code> or <code>CMAKE_SWIG_OUTDIR</code> is used instead.</p>
<dt><code>SOURCES</code></p>
<dd>List of sources for the library. Files with extension <code>.i</code> will be identified as sources for the <code>SWIG</code> tool. Other files will be handled in the standard way. </p>
<p> New in version 3.14: This behavior can be overridden by specifying the variable <code>SWIG_SOURCE_FILE_EXTENSIONS</code>. </p>
<p> <code>NOTE:</code> If <code>UseSWIG_MODULE_VERSION</code> is set to 2, it is <code>strongly</code> recommended to use a dedicated directory unique to the target when either the <code>OUTPUT_DIR</code> option or the <code>CMAKE_SWIG_OUTDIR</code> variable are specified. The output directory contents are erased as part of the target build, so to prevent interference between targets or losing other important files, each target should have its own dedicated output directory.</p>
<dt><code>swig_link_libraries</code></p>
<dd>Link libraries to swig module: </p>
<pre>swig_link_libraries(&lt;name&gt; &lt;item&gt;...)</pre>
<p>This command has same capabilities as <code>target_link_libraries()</code> command. </p>
<p> <code>NOTE:</code> If variable <code>UseSWIG_TARGET_NAME_PREFERENCE</code> is set to <code>STANDARD</code>, this command is deprecated and <code>target_link_libraries()</code> command must be used instead. </p>
<p> Source file properties on module files <code>must</code> be set before the invocation of the <code>swig_add_library</code> command to specify special behavior of SWIG and ensure generated files will receive the required settings.</p>
<dt><code>CPLUSPLUS</code></p>
<dd>Call SWIG in c++ mode. For example: </p>
<pre>set_property(SOURCE mymod.i PROPERTY CPLUSPLUS ON)
swig_add_library(mymod LANGUAGE python SOURCES mymod.i)</pre>
<dt><code>SWIG_FLAGS</code></p>
<dd>Deprecated since version 3.12: Replaced with the fine-grained properties that follow. </p>
<p> Pass custom flags to the SWIG executable.</p>
<dt><code>INCLUDE_DIRECTORIES</code>, <code>COMPILE_DEFINITIONS</code> and <code>COMPILE_OPTIONS</code></p>
<dd>New in version 3.12. </p>
<p> Add custom flags to SWIG compiler and have same semantic as properties <code>INCLUDE_DIRECTORIES</code>, <code>COMPILE_DEFINITIONS</code> and <code>COMPILE_OPTIONS</code>.</p>
<dt><code>USE_TARGET_INCLUDE_DIRECTORIES</code></p>
<dd>New in version 3.13. </p>
<p> If set to <code>TRUE</code>, contents of target property <code>INCLUDE_DIRECTORIES</code> will be forwarded to <code>SWIG</code> compiler. If set to <code>FALSE</code> target property <code>INCLUDE_DIRECTORIES</code> will be ignored. If not set, target property <code>SWIG_USE_TARGET_INCLUDE_DIRECTORIES</code> will be considered.</p>
<dt><code>GENERATED_INCLUDE_DIRECTORIES</code>, <code>GENERATED_COMPILE_DEFINITIONS</code> and <code>GENERATED_COMPILE_OPTIONS</code></p>
<dd>New in version 3.12. </p>
<p> Add custom flags to the C/C++ generated source. They will fill, respectively, properties <code>INCLUDE_DIRECTORIES</code>, <code>COMPILE_DEFINITIONS</code> and <code>COMPILE_OPTIONS</code> of generated C/C++ file.</p>
<dt><code>DEPENDS</code></p>
<dd>New in version 3.12. </p>
<p> Specify additional dependencies to the source file.</p>
<dt><code>USE_SWIG_DEPENDENCIES</code></p>
<dd>New in version 3.20. </p>
<p> If set to <code>TRUE</code>, implicit dependencies are generated by the <code>swig</code> tool itself. This property is only meaningful for Makefile, Ninja, <code>Xcode</code>, and Visual Studio (<code>Visual Studio 11 2012</code> and above) generators. Default value is <code>FALSE</code>. </p>
<p> New in version 3.21: Added the support of <code>Xcode</code> generator. </p>
<p> New in version 3.22: Added the support of Visual Studio Generators. </p>
<dt><code>SWIG_MODULE_NAME</code></p>
<dd>Specify the actual import name of the module in the target language. This is required if it cannot be scanned automatically from source or different from the module file basename. For example: </p>
<pre>set_property(SOURCE mymod.i PROPERTY SWIG_MODULE_NAME mymod_realname)</pre>
<p>Changed in version 3.14: If policy <code>CMP0086</code> is set to <code>NEW</code>, <code>-module &lt;module_name&gt;</code> is passed to <code>SWIG</code> compiler. </p>
<dt><code>OUTPUT_DIR</code></p>
<dd>New in version 3.19. </p>
<p> Specify where to write the language specific files (swig <code>-outdir</code> option) for the considered source file. If not specified, the other ways to define the output directory applies (see <code>OUTPUT_DIR</code> option of <code>swig_add_library()</code> command).</p>
<dt><code>OUTFILE_DIR</code></p>
<dd>New in version 3.19. </p>
<p> Specify an output directory where the generated source file will be placed (swig <code>-o</code> option) for the considered source file. If not specified, <code>OUTPUT_DIR</code> source property will be used. If neither are specified, the other ways to define output file directory applies (see <code>OUTFILE_DIR</code> option of <code>swig_add_library()</code> command). </p>
<p> Target library properties can be set to apply same configuration to all SWIG input files.</p>
<dt><code>SWIG_INCLUDE_DIRECTORIES</code>, <code>SWIG_COMPILE_DEFINITIONS</code> and <code>SWIG_COMPILE_OPTIONS</code></p>
<dd>New in version 3.12. </p>
<p> These properties will be applied to all SWIG input files and have same semantic as target properties <code>INCLUDE_DIRECTORIES</code>, <code>COMPILE_DEFINITIONS</code> and <code>COMPILE_OPTIONS</code>. </p>
<pre>set (UseSWIG_TARGET_NAME_PREFERENCE STANDARD)
swig_add_library(mymod LANGUAGE python SOURCES mymod.i)
set_property(TARGET mymod PROPERTY SWIG_COMPILE_DEFINITIONS MY_DEF1 MY_DEF2)
set_property(TARGET mymod PROPERTY SWIG_COMPILE_OPTIONS -bla -blb)</pre>
<dt><code>SWIG_USE_TARGET_INCLUDE_DIRECTORIES</code></p>
<dd>New in version 3.13. </p>
<p> If set to <code>TRUE</code>, contents of target property <code>INCLUDE_DIRECTORIES</code> will be forwarded to <code>SWIG</code> compiler. If set to <code>FALSE</code> or not defined, target property <code>INCLUDE_DIRECTORIES</code> will be ignored. This behavior can be overridden by specifying source property <code>USE_TARGET_INCLUDE_DIRECTORIES</code>.</p>
<dt><code>SWIG_GENERATED_INCLUDE_DIRECTORIES</code>, <code>SWIG_GENERATED_COMPILE_DEFINITIONS</code> and <code>SWIG_GENERATED_COMPILE_OPTIONS</code></p>
<dd>New in version 3.12. </p>
<p> These properties will populate, respectively, properties <code>INCLUDE_DIRECTORIES</code>, <code>COMPILE_DEFINITIONS</code> and <code>COMPILE_FLAGS</code> of all generated C/C++ files.</p>
<dt><code>SWIG_DEPENDS</code></p>
<dd>New in version 3.12. </p>
<p> Add dependencies to all SWIG input files. </p>
<p> The following target properties are output properties and can be used to get information about support files generated by <code>SWIG</code> interface compilation.</p>
<dt><code>SWIG_SUPPORT_FILES</code></p>
<dd>New in version 3.12. </p>
<p> This output property list of wrapper files generated during SWIG compilation. </p>
<pre>set (UseSWIG_TARGET_NAME_PREFERENCE STANDARD)
swig_add_library(mymod LANGUAGE python SOURCES mymod.i)
get_property(support_files TARGET mymod PROPERTY SWIG_SUPPORT_FILES)</pre>
<p><code>NOTE:</code> Only most principal support files are listed. In case some advanced features of <code>SWIG</code> are used (for example <code>%template</code>), associated support files may not be listed. Prefer to use the <code>SWIG_SUPPORT_FILES_DIRECTORY</code> property to handle support files.</p>
<dt><code>SWIG_SUPPORT_FILES_DIRECTORY</code></p>
<dd>New in version 3.12. </p>
<p> This output property specifies the directory where support files will be generated. </p>
<p> <code>NOTE:</code> When source property <code>OUTPUT_DIR</code> is defined, multiple directories can be specified as part of <code>SWIG_SUPPORT_FILES_DIRECTORY</code>. </p>
<p> Some variables can be set to customize the behavior of <code>swig_add_library</code> as well as <code>SWIG</code>:</p>
<dt><code>UseSWIG_MODULE_VERSION</code></p>
<dd>New in version 3.12. </p>
<p> Specify different behaviors for <code>UseSWIG</code> module.</p>
<dt>&bull;</p>
<dd>Set to 1 or undefined: Legacy behavior is applied.</p>
<dt>&bull;</p>
<dd>Set to 2: A new strategy is applied regarding support files: the output directory of support files is erased before <code>SWIG</code> interface compilation.</p>
<dt><code>CMAKE_SWIG_FLAGS</code></p>
<dd>Add flags to all swig calls.</p>
<dt><code>CMAKE_SWIG_OUTDIR</code></p>
<dd>Specify where to write the language specific files (swig <code>-outdir</code> option).</p>
<dt><code>SWIG_OUTFILE_DIR</code></p>
<dd>New in version 3.8. </p>
<p> Specify an output directory name where the generated source file will be placed. If not specified, <code>CMAKE_SWIG_OUTDIR</code> is used.</p>
<dt><code>SWIG_MODULE_&lt;name&gt;_EXTRA_DEPS</code></p>
<dd>Specify extra dependencies for the generated module for <code>&lt;name&gt;</code>.</p>
<dt><code>SWIG_SOURCE_FILE_EXTENSIONS</code></p>
<dd>New in version 3.14. </p>
<p> Specify a list of source file extensions to override the default behavior of considering only <code>.i</code> files as sources for the <code>SWIG</code> tool. For example: </p>
<pre>set(SWIG_SOURCE_FILE_EXTENSIONS &quot;.i&quot; &quot;.swg&quot;)</pre>
<dt><code>SWIG_USE_SWIG_DEPENDENCIES</code></p>
<dd>New in version 3.20. </p>
<p> If set to <code>TRUE</code>, implicit dependencies are generated by the <code>swig</code> tool itself. This variable is only meaningful for Makefile, Ninja, <code>Xcode</code>, and Visual Studio (<code>Visual Studio 11 2012</code> and above) generators. Default value is <code>FALSE</code>. </p>
<p> Source file property <code>USE_SWIG_DEPENDENCIES</code>, if not defined, will be initialized with the value of this variable. </p>
<p> New in version 3.21: Added the support of <code>Xcode</code> generator. </p>
<p> New in version 3.22: Added the support of Visual Studio Generators. </p>
</dl>
<h3>UsewxWidgets</h3>
<p>Convenience include for using wxWidgets library. </p>
<p> Determines if wxWidgets was FOUND and sets the appropriate libs, incdirs, flags, etc. INCLUDE_DIRECTORIES and LINK_DIRECTORIES are called. </p>
<p> USAGE </p>
<pre># Note that for MinGW users the order of libs is important!
find_package(wxWidgets REQUIRED net gl core base)
include(${wxWidgets_USE_FILE})
# and for each of your dependent executable/library targets:
target_link_libraries(&lt;YourTarget&gt; ${wxWidgets_LIBRARIES})</pre>
<p>DEPRECATED </p>
<pre>LINK_LIBRARIES is not called in favor of adding dependencies per target.</pre>
<p>AUTHOR </p>
<pre>Jan Woetzel &lt;jw -at- mip.informatik.uni-kiel.de&gt;</pre>
<h2>Find Modules</h2>
<p>These modules search for third-party software. They are normally called through the <code>find_package()</code> command.</p>
<h3>FindALSA</h3>
<p>Find Advanced Linux Sound Architecture (ALSA) </p>
<p> Find the alsa libraries (<code>asound</code>)</p>
<h3>IMPORTED Targets</h3>
<p>New in version 3.12. </p>
<p> This module defines <code>IMPORTED</code> target <code>ALSA::ALSA</code>, if ALSA has been found.</p>
<h3>Result Variables</h3>
<p>This module defines the following variables:</p>
<dl>
<dt><code>ALSA_FOUND</code></p>
<dd>True if ALSA_INCLUDE_DIR &amp; ALSA_LIBRARY are found</p>
<dt><code>ALSA_LIBRARIES</code></p>
<dd>List of libraries when using ALSA.</p>
<dt><code>ALSA_INCLUDE_DIRS</code></p>
<dd>Where to find the ALSA headers.</dl>
<h3>Cache variables</h3>
<p>The following cache variables may also be set:</p>
<dl>
<dt><code>ALSA_INCLUDE_DIR</code></p>
<dd>the ALSA include directory</p>
<dt><code>ALSA_LIBRARY</code></p>
<dd>the absolute path of the asound library</dl>
<h3>FindArmadillo</h3>
<p>Find the Armadillo C++ library. Armadillo is a library for linear algebra &amp; scientific computing. </p>
<p> New in version 3.18: Support for linking wrapped libraries directly (<code>ARMA_DONT_USE_WRAPPER</code>). </p>
<p> Using Armadillo: </p>
<pre>find_package(Armadillo REQUIRED)
include_directories(${ARMADILLO_INCLUDE_DIRS})
add_executable(foo foo.cc)
target_link_libraries(foo ${ARMADILLO_LIBRARIES})</pre>
<p>This module sets the following variables: </p>
<pre>ARMADILLO_FOUND - set to true if the library is found
ARMADILLO_INCLUDE_DIRS - list of required include directories
ARMADILLO_LIBRARIES - list of libraries to be linked
ARMADILLO_VERSION_MAJOR - major version number
ARMADILLO_VERSION_MINOR - minor version number
ARMADILLO_VERSION_PATCH - patch version number
ARMADILLO_VERSION_STRING - version number as a string (ex: &quot;1.0.4&quot;)
ARMADILLO_VERSION_NAME - name of the version (ex: &quot;Antipodean Antileech&quot;)</pre>
<h3>FindASPELL</h3>
<p>Try to find ASPELL </p>
<p> Once done this will define </p>
<pre>ASPELL_FOUND - system has ASPELL
ASPELL_EXECUTABLE - the ASPELL executable
ASPELL_INCLUDE_DIR - the ASPELL include directory
ASPELL_LIBRARIES - The libraries needed to use ASPELL
ASPELL_DEFINITIONS - Compiler switches required for using ASPELL</pre>
<h3>FindAVIFile</h3>
<p>Locate AVIFILE library and include paths </p>
<p> AVIFILE (<i><a rel="nofollow" href="http://avifile.sourceforge.net/">http://avifile.sourceforge.net/</a></i>) is a set of libraries for i386 machines to use various AVI codecs. Support is limited beyond Linux. Windows provides native AVI support, and so doesn&#8217;t need this library. This module defines </p>
<pre>AVIFILE_INCLUDE_DIR, where to find avifile.h , etc.
AVIFILE_LIBRARIES, the libraries to link against
AVIFILE_DEFINITIONS, definitions to use when compiling
AVIFILE_FOUND, If false, don't try to use AVIFILE</pre>
<h3>FindBacktrace</h3>
<p>Find provider for <i><a href="/docs/linux/man/3-backtrace/">backtrace</a>(3)</i>. </p>
<p> Checks if OS supports <code><a href="/docs/linux/man/3-backtrace/">backtrace</a>(3)</code> via either <code>libc</code> or custom library. This module defines the following variables:</p>
<dl>
<dt><code>Backtrace_HEADER</code></p>
<dd>The header file needed for <code><a href="/docs/linux/man/3-backtrace/">backtrace</a>(3)</code>. Cached. Could be forcibly set by user.</p>
<dt><code>Backtrace_INCLUDE_DIRS</code></p>
<dd>The include directories needed to use <code><a href="/docs/linux/man/3-backtrace/">backtrace</a>(3)</code> header.</p>
<dt><code>Backtrace_LIBRARIES</code></p>
<dd>The libraries (linker flags) needed to use <code><a href="/docs/linux/man/3-backtrace/">backtrace</a>(3)</code>, if any.</p>
<dt><code>Backtrace_FOUND</code></p>
<dd>Is set if and only if <code><a href="/docs/linux/man/3-backtrace/">backtrace</a>(3)</code> support detected. </p>
<p> The following cache variables are also available to set or use:</p>
<dt><code>Backtrace_LIBRARY</code></p>
<dd>The external library providing backtrace, if any.</p>
<dt><code>Backtrace_INCLUDE_DIR</code></p>
<dd>The directory holding the <code><a href="/docs/linux/man/3-backtrace/">backtrace</a>(3)</code> header. </p>
<p> Typical usage is to generate of header file using <code>configure_file()</code> with the contents like the following: </p>
<pre>#cmakedefine01 Backtrace_FOUND
#if Backtrace_FOUND
# include &lt;${Backtrace_HEADER}&gt;
#endif</pre>
<p>And then reference that generated header file in actual source.</dl>
<h3>FindBISON</h3>
<p>Find <code>bison</code> executable and provide a macro to generate custom build rules. </p>
<p> The module defines the following variables:</p>
<dl>
<dt><code>BISON_EXECUTABLE</code></p>
<dd>path to the <code>bison</code> program</p>
<dt><code>BISON_VERSION</code></p>
<dd>version of <code>bison</code></p>
<dt><code>BISON_FOUND</code></p>
<dd>&quot;True&quot; if the program was found </p>
<p> The minimum required version of <code>bison</code> can be specified using the standard CMake syntax, e.g. <code>find_package(BISON 2.1.3)</code>. </p>
<p> If <code>bison</code> is found, the module defines the macro: </p>
<pre>BISON_TARGET(&lt;Name&gt; &lt;YaccInput&gt; &lt;CodeOutput&gt;
 [COMPILE_FLAGS &lt;flags&gt;]
 [DEFINES_FILE &lt;file&gt;]
 [VERBOSE [&lt;file&gt;]]
 [REPORT_FILE &lt;file&gt;]
 )</pre>
<p>which will create a custom rule to generate a parser. <code>&lt;YaccInput&gt;</code> is the path to a yacc file. <code>&lt;CodeOutput&gt;</code> is the name of the source file generated by bison. A header file is also be generated, and contains the token list. </p>
<p> Changed in version 3.14: When <code>CMP0088</code> is set to <code>NEW</code>, <code>bison</code> runs in the <code>CMAKE_CURRENT_BINARY_DIR</code> directory. </p>
<p> The options are:</p>
<dt><code>COMPILE_FLAGS &lt;flags&gt;</code></p>
<dd>Specify flags to be added to the <code>bison</code> command line.</p>
<dt><code>DEFINES_FILE &lt;file&gt;</code></p>
<dd>New in version 3.4. </p>
<p> Specify a non-default header <code>&lt;file&gt;</code> to be generated by <code>bison</code>.</p>
<dt><code>VERBOSE [&lt;file&gt;]</code></p>
<dd>Tell <code>bison</code> to write a report file of the grammar and parser. </p>
<p> Deprecated since version 3.7: If <code>&lt;file&gt;</code> is given, it specifies path the report file is copied to. <code>[&lt;file&gt;]</code> is left for backward compatibility of this module. Use <code>VERBOSE REPORT_FILE &lt;file&gt;</code>. </p>
<dt><code>REPORT_FILE &lt;file&gt;</code></p>
<dd>New in version 3.7. </p>
<p> Specify a non-default report <code>&lt;file&gt;</code>, if generated. </p>
<p> The macro defines the following variables:</p>
<dt><code>BISON_&lt;Name&gt;_DEFINED</code></p>
<dd><code>True</code> is the macro ran successfully</p>
<dt><code>BISON_&lt;Name&gt;_INPUT</code></p>
<dd>The input source file, an alias for &lt;YaccInput&gt;</p>
<dt><code>BISON_&lt;Name&gt;_OUTPUT_SOURCE</code></p>
<dd>The source file generated by bison</p>
<dt><code>BISON_&lt;Name&gt;_OUTPUT_HEADER</code></p>
<dd>The header file generated by bison</p>
<dt><code>BISON_&lt;Name&gt;_OUTPUTS</code></p>
<dd>All files generated by bison including the source, the header and the report</p>
<dt><code>BISON_&lt;Name&gt;_COMPILE_FLAGS</code></p>
<dd>Options used in the <code>bison</code> command line </p>
<p> Example usage: </p>
<pre>find_package(BISON)
BISON_TARGET(MyParser parser.y ${CMAKE_CURRENT_BINARY_DIR}/parser.cpp
 DEFINES_FILE ${CMAKE_CURRENT_BINARY_DIR}/parser.h)
add_executable(Foo main.cpp ${BISON_MyParser_OUTPUTS})</pre>
</dl>
<h3>FindBLAS</h3>
<p>Find Basic Linear Algebra Subprograms (BLAS) library </p>
<p> This module finds an installed Fortran library that implements the <i>BLAS linear-algebra interface</i>. </p>
<p> At least one of the <code>C</code>, <code>CXX</code>, or <code>Fortran</code> languages must be enabled.</p>
<h3>Input Variables</h3>
<p>The following variables may be set to influence this module&#8217;s behavior:</p>
<dl>
<dt><code>BLA_STATIC</code></p>
<dd>if <code>ON</code> use static linkage</p>
<dt><code>BLA_VENDOR</code></p>
<dd>Set to one of the <i>BLAS/LAPACK Vendors</i> to search for BLAS only from the specified vendor. If not set, all vendors are considered.</p>
<dt><code>BLA_F95</code></p>
<dd>if <code>ON</code> tries to find the BLAS95 interfaces</p>
<dt><code>BLA_PREFER_PKGCONFIG</code></p>
<dd>New in version 3.11. </p>
<p> if set <code>pkg-config</code> will be used to search for a BLAS library first and if one is found that is preferred</p>
<dt><code>BLA_SIZEOF_INTEGER</code></p>
<dd>New in version 3.22. </p>
<p> Specify the BLAS/LAPACK library integer size:</p>
<dt><code>4</code></p>
<dd>Search for a BLAS/LAPACK with 32-bit integer interfaces.</p>
<dt><code>8</code></p>
<dd>Search for a BLAS/LAPACK with 64-bit integer interfaces.</p>
<dt><code>ANY</code></p>
<dd>Search for any BLAS/LAPACK. Most likely, a BLAS/LAPACK with 32-bit integer interfaces will be found.</dl>
<h3>Imported targets</h3>
<p>This module defines the following <code>IMPORTED</code> targets:</p>
<dl>
<dt><code>BLAS::BLAS</code></p>
<dd>New in version 3.18. </p>
<p> The libraries to use for BLAS, if found.</dl>
<h3>Result Variables</h3>
<p>This module defines the following variables:</p>
<dl>
<dt><code>BLAS_FOUND</code></p>
<dd>library implementing the BLAS interface is found</p>
<dt><code>BLAS_LINKER_FLAGS</code></p>
<dd>uncached list of required linker flags (excluding <code>-l</code> and <code>-L</code>).</p>
<dt><code>BLAS_LIBRARIES</code></p>
<dd>uncached list of libraries (using full path name) to link against to use BLAS (may be empty if compiler implicitly links BLAS)</p>
<dt><code>BLAS95_LIBRARIES</code></p>
<dd>uncached list of libraries (using full path name) to link against to use BLAS95 interface</p>
<dt><code>BLAS95_FOUND</code></p>
<dd>library implementing the BLAS95 interface is found</dl>
<h3>BLAS/LAPACK Vendors</h3>
<dl>
<dt><code>Generic</code></p>
<dd>Generic reference implementation</p>
<dt><code>ACML</code>, <code>ACML_MP</code>, <code>ACML_GPU</code></p>
<dd>AMD Core Math Library</p>
<dt><code>Apple</code>, <code>NAS</code></p>
<dd>Apple BLAS (Accelerate), and Apple NAS (vecLib)</p>
<dt><code>Arm</code>, <code>Arm_mp</code>, <code>Arm_ilp64</code>, <code>Arm_ilp64_mp</code></p>
<dd>New in version 3.18. </p>
<p> Arm Performance Libraries</p>
<dt><code>ATLAS</code></p>
<dd>Automatically Tuned Linear Algebra Software</p>
<dt><code>CXML</code>, <code>DXML</code></p>
<dd>Compaq/Digital Extended Math Library</p>
<dt><code>EML</code>, <code>EML_mt</code></p>
<dd>New in version 3.20. </p>
<p> Elbrus Math Library</p>
<dt><code>FLAME</code></p>
<dd>New in version 3.11. </p>
<p> BLIS Framework</p>
<dt><code>FlexiBLAS</code></p>
<dd>New in version 3.19. </p>
<dt><code>Fujitsu_SSL2</code>, <code>Fujitsu_SSL2BLAMP</code>, <code>Fujitsu_SSL2SVE</code>, <code>Fujitsu_SSL2BLAMPSVE</code></p>
<dd>New in version 3.20. </p>
<p> Fujitsu SSL2 serial and parallel blas/lapack with SVE instructions</p>
<dt><code>Goto</code></p>
<dd>GotoBLAS </p>
<p> <code>IBMESSL</code>, <code>IBMESSL_SMP</code> IBM Engineering and Scientific Subroutine Library</p>
<dt><code>Intel</code></p>
<dd>Intel MKL 32 bit and 64 bit obsolete versions</p>
<dt><code>Intel10_32</code></p>
<dd>Intel MKL v10 32 bit, threaded code</p>
<dt><code>Intel10_64lp</code></p>
<dd>Intel MKL v10+ 64 bit, threaded code, lp64 model</p>
<dt><code>Intel10_64lp_seq</code></p>
<dd>Intel MKL v10+ 64 bit, sequential code, lp64 model</p>
<dt><code>Intel10_64ilp</code></p>
<dd>New in version 3.13. </p>
<p> Intel MKL v10+ 64 bit, threaded code, ilp64 model</p>
<dt><code>Intel10_64ilp_seq</code></p>
<dd>New in version 3.13. </p>
<p> Intel MKL v10+ 64 bit, sequential code, ilp64 model</p>
<dt><code>Intel10_64_dyn</code></p>
<dd>New in version 3.17. </p>
<p> Intel MKL v10+ 64 bit, single dynamic library</p>
<dt><code>NVHPC</code></p>
<dd>New in version 3.21. </p>
<p> NVIDIA HPC SDK</p>
<dt><code>OpenBLAS</code></p>
<dd>New in version 3.6. </p>
<dt><code>PhiPACK</code></p>
<dd>Portable High Performance ANSI C (PHiPAC)</p>
<dt><code>SCSL</code>, <code>SCSL_mp</code></p>
<dd>Scientific Computing Software Library</p>
<dt><code>SGIMATH</code></p>
<dd>SGI Scientific Mathematical Library</p>
<dt><code>SunPerf</code></p>
<dd>Sun Performance Library</dl>
<h3>Intel MKL</h3>
<p>To use the Intel MKL implementation of BLAS, a project must enable at least one of the <code>C</code> or <code>CXX</code> languages. Set <code>BLA_VENDOR</code> to an Intel MKL variant either on the command-line as <code>-DBLA_VENDOR=Intel10_64lp</code> or in project code: </p>
<pre>set(BLA_VENDOR Intel10_64lp)
find_package(BLAS)</pre>
<p>In order to build a project using Intel MKL, and end user must first establish an Intel MKL environment:</p>
<dl>
<dt><code>Intel oneAPI</code></p>
<dd>Source the full Intel environment script: </p>
<pre>. /opt/intel/oneapi/setvars.sh</pre>
<p>Or, source the MKL component environment script: </p>
<pre>. /opt/intel/oneapi/mkl/latest/env/vars.sh</pre>
<dt><code>Intel Classic</code></p>
<dd>Source the full Intel environment script: </p>
<pre>. /opt/intel/bin/compilervars.sh intel64</pre>
<p>Or, source the MKL component environment script: </p>
<pre>. /opt/intel/mkl/bin/mklvars.sh intel64</pre>
<p>The above environment scripts set the <code>MKLROOT</code> environment variable to the top of the MKL installation. They also add the location of the runtime libraries to the dynamic library loader environment variable for your platform (e.g. <code>LD_LIBRARY_PATH</code>). This is necessary for programs linked against MKL to run. </p>
<p> <code>NOTE:</code> As of Intel oneAPI 2021.2, loading only the MKL component does not make all of its dependencies available. In particular, the <code>iomp5</code> library must be available separately, or provided by also loading the compiler component environment: </p>
<pre>. /opt/intel/oneapi/compiler/latest/env/vars.sh</pre>
</dl>
<h3>FindBoost</h3>
<p>Find Boost include dirs and libraries </p>
<p> Use this module by invoking <code>find_package()</code> with the form: </p>
<pre>find_package(Boost
 [version] [EXACT] # Minimum or EXACT version e.g. 1.67.0
 [REQUIRED] # Fail with error if Boost is not found
 [COMPONENTS &lt;libs&gt;...] # Boost libraries by their canonical name
 # e.g. &quot;date_time&quot; for &quot;libboost_date_time&quot;
 [OPTIONAL_COMPONENTS &lt;libs&gt;...]
 # Optional Boost libraries by their canonical name)
 ) # e.g. &quot;date_time&quot; for &quot;libboost_date_time&quot;</pre>
<p>This module finds headers and requested component libraries OR a CMake package configuration file provided by a &quot;Boost CMake&quot; build. For the latter case skip to the <i>Boost CMake</i> section below. </p>
<p> New in version 3.7: <code>bzip2</code> and <code>zlib</code> components (Windows only). </p>
<p> New in version 3.11: The <code>OPTIONAL_COMPONENTS</code> option. </p>
<p> New in version 3.13: <code>stacktrace_*</code> components. </p>
<p> New in version 3.19: <code>bzip2</code> and <code>zlib</code> components on all platforms.</p>
<h3>Result Variables</h3>
<p>This module defines the following variables:</p>
<dl>
<dt><code>Boost_FOUND</code></p>
<dd>True if headers and requested libraries were found.</p>
<dt><code>Boost_INCLUDE_DIRS</code></p>
<dd>Boost include directories.</p>
<dt><code>Boost_LIBRARY_DIRS</code></p>
<dd>Link directories for Boost libraries.</p>
<dt><code>Boost_LIBRARIES</code></p>
<dd>Boost component libraries to be linked.</p>
<dt><code>Boost_&lt;COMPONENT&gt;_FOUND</code></p>
<dd>True if component <code>&lt;COMPONENT&gt;</code> was found (<code>&lt;COMPONENT&gt;</code> name is upper-case).</p>
<dt><code>Boost_&lt;COMPONENT&gt;_LIBRARY</code></p>
<dd>Libraries to link for component <code>&lt;COMPONENT&gt;</code> (may include <code>target_link_libraries()</code> debug/optimized keywords).</p>
<dt><code>Boost_VERSION_MACRO</code></p>
<dd><code>BOOST_VERSION</code> value from <code>boost/version.hpp</code>.</p>
<dt><code>Boost_VERSION_STRING</code></p>
<dd>Boost version number in <code>X.Y.Z</code> format.</p>
<dt><code>Boost_VERSION</code></p>
<dd>Boost version number in <code>X.Y.Z</code> format (same as <code>Boost_VERSION_STRING</code>). </p>
<p> Changed in version 3.15: In previous CMake versions, this variable used the raw version string from the Boost header (same as <code>Boost_VERSION_MACRO</code>). See policy <code>CMP0093</code>. </p>
<dt><code>Boost_LIB_VERSION</code></p>
<dd>Version string appended to library filenames.</p>
<dt><code>Boost_VERSION_MAJOR</code>, <code>Boost_MAJOR_VERSION</code></p>
<dd>Boost major version number (<code>X</code> in <code>X.Y.Z</code>).</p>
<dt><code>Boost_VERSION_MINOR</code>, <code>Boost_MINOR_VERSION</code></p>
<dd>Boost minor version number (<code>Y</code> in <code>X.Y.Z</code>).</p>
<dt><code>Boost_VERSION_PATCH</code>, <code>Boost_SUBMINOR_VERSION</code></p>
<dd>Boost subminor version number (<code>Z</code> in <code>X.Y.Z</code>).</p>
<dt><code>Boost_VERSION_COUNT</code></p>
<dd>Amount of version components (3).</p>
<dt><code>Boost_LIB_DIAGNOSTIC_DEFINITIONS</code> (Windows-specific)</p>
<dd>Pass to <code>add_definitions()</code> to have diagnostic information about Boost&#8217;s automatic linking displayed during compilation </p>
<p> New in version 3.15: The <code>Boost_VERSION_&lt;PART&gt;</code> variables. </p>
</dl>
<h3>Cache variables</h3>
<p>Search results are saved persistently in CMake cache entries:</p>
<dl>
<dt><code>Boost_INCLUDE_DIR</code></p>
<dd>Directory containing Boost headers.</p>
<dt><code>Boost_LIBRARY_DIR_RELEASE</code></p>
<dd>Directory containing release Boost libraries.</p>
<dt><code>Boost_LIBRARY_DIR_DEBUG</code></p>
<dd>Directory containing debug Boost libraries.</p>
<dt><code>Boost_&lt;COMPONENT&gt;_LIBRARY_DEBUG</code></p>
<dd>Component <code>&lt;COMPONENT&gt;</code> library debug variant.</p>
<dt><code>Boost_&lt;COMPONENT&gt;_LIBRARY_RELEASE</code></p>
<dd>Component <code>&lt;COMPONENT&gt;</code> library release variant. </p>
<p> New in version 3.3: Per-configuration variables <code>Boost_LIBRARY_DIR_RELEASE</code> and <code>Boost_LIBRARY_DIR_DEBUG</code>. </p>
</dl>
<h3>Hints</h3>
<p>This module reads hints about search locations from variables:</p>
<dl>
<dt><code>BOOST_ROOT</code>, <code>BOOSTROOT</code></p>
<dd>Preferred installation prefix.</p>
<dt><code>BOOST_INCLUDEDIR</code></p>
<dd>Preferred include directory e.g. <code>&lt;prefix&gt;/include</code>.</p>
<dt><code>BOOST_LIBRARYDIR</code></p>
<dd>Preferred library directory e.g. <code>&lt;prefix&gt;/lib</code>.</p>
<dt><code>Boost_NO_SYSTEM_PATHS</code></p>
<dd>Set to <code>ON</code> to disable searching in locations not specified by these hint variables. Default is <code>OFF</code>.</p>
<dt><code>Boost_ADDITIONAL_VERSIONS</code></p>
<dd>List of Boost versions not known to this module. (Boost install locations may contain the version). </p>
<p> Users may set these hints or results as <code>CACHE</code> entries. Projects should not read these entries directly but instead use the above result variables. Note that some hint names start in upper-case <code>BOOST</code>. One may specify these as environment variables if they are not specified as CMake variables or cache entries. </p>
<p> This module first searches for the Boost header files using the above hint variables (excluding <code>BOOST_LIBRARYDIR</code>) and saves the result in <code>Boost_INCLUDE_DIR</code>. Then it searches for requested component libraries using the above hints (excluding <code>BOOST_INCLUDEDIR</code> and <code>Boost_ADDITIONAL_VERSIONS</code>), &quot;lib&quot; directories near <code>Boost_INCLUDE_DIR</code>, and the library name configuration settings below. It saves the library directories in <code>Boost_LIBRARY_DIR_DEBUG</code> and <code>Boost_LIBRARY_DIR_RELEASE</code> and individual library locations in <code>Boost_&lt;COMPONENT&gt;_LIBRARY_DEBUG</code> and <code>Boost_&lt;COMPONENT&gt;_LIBRARY_RELEASE</code>. When one changes settings used by previous searches in the same build tree (excluding environment variables) this module discards previous search results affected by the changes and searches again.</dl>
<h3>Imported Targets</h3>
<p>New in version 3.5. </p>
<p> This module defines the following <code>IMPORTED</code> targets:</p>
<dl>
<dt><code>Boost::boost</code></p>
<dd>Target for header-only dependencies. (Boost include directory).</p>
<dt><code>Boost::headers</code></p>
<dd>New in version 3.15: Alias for <code>Boost::boost</code>. </p>
<dt><code>Boost::&lt;component&gt;</code></p>
<dd>Target for specific component dependency (shared or static library); <code>&lt;component&gt;</code> name is lower-case.</p>
<dt><code>Boost::diagnostic_definitions</code></p>
<dd>Interface target to enable diagnostic information about Boost&#8217;s automatic linking during compilation (adds <code>-DBOOST_LIB_DIAGNOSTIC</code>).</p>
<dt><code>Boost::disable_autolinking</code></p>
<dd>Interface target to disable automatic linking with MSVC (adds <code>-DBOOST_ALL_NO_LIB</code>).</p>
<dt><code>Boost::dynamic_linking</code></p>
<dd>Interface target to enable dynamic linking with MSVC (adds <code>-DBOOST_ALL_DYN_LINK</code>). </p>
<p> Implicit dependencies such as <code>Boost::filesystem</code> requiring <code>Boost::system</code> will be automatically detected and satisfied, even if system is not specified when using <code>find_package()</code> and if <code>Boost::system</code> is not added to <code>target_link_libraries()</code>. If using <code>Boost::thread</code>, then <code>Threads::Threads</code> will also be added automatically. </p>
<p> It is important to note that the imported targets behave differently than variables created by this module: multiple calls to <code>find_package(Boost)</code> in the same directory or sub-directories with different options (e.g. static or shared) will not override the values of the targets created by the first call.</dl>
<h3>Other Variables</h3>
<p>Boost libraries come in many variants encoded in their file name. Users or projects may tell this module which variant to find by setting variables:</p>
<dl>
<dt><code>Boost_USE_DEBUG_LIBS</code></p>
<dd>New in version 3.10. </p>
<p> Set to <code>ON</code> or <code>OFF</code> to specify whether to search and use the debug libraries. Default is <code>ON</code>.</p>
<dt><code>Boost_USE_RELEASE_LIBS</code></p>
<dd>New in version 3.10. </p>
<p> Set to <code>ON</code> or <code>OFF</code> to specify whether to search and use the release libraries. Default is <code>ON</code>.</p>
<dt><code>Boost_USE_MULTITHREADED</code></p>
<dd>Set to OFF to use the non-multithreaded libraries (&quot;mt&quot; tag). Default is <code>ON</code>.</p>
<dt><code>Boost_USE_STATIC_LIBS</code></p>
<dd>Set to ON to force the use of the static libraries. Default is <code>OFF</code>.</p>
<dt><code>Boost_USE_STATIC_RUNTIME</code></p>
<dd>Set to <code>ON</code> or <code>OFF</code> to specify whether to use libraries linked statically to the C++ runtime (&quot;s&quot; tag). Default is platform dependent.</p>
<dt><code>Boost_USE_DEBUG_RUNTIME</code></p>
<dd>Set to <code>ON</code> or <code>OFF</code> to specify whether to use libraries linked to the MS debug C++ runtime (&quot;g&quot; tag). Default is <code>ON</code>.</p>
<dt><code>Boost_USE_DEBUG_PYTHON</code></p>
<dd>Set to <code>ON</code> to use libraries compiled with a debug Python build (&quot;y&quot; tag). Default is <code>OFF</code>.</p>
<dt><code>Boost_USE_STLPORT</code></p>
<dd>Set to <code>ON</code> to use libraries compiled with STLPort (&quot;p&quot; tag). Default is <code>OFF</code>.</p>
<dt><code>Boost_USE_STLPORT_DEPRECATED_NATIVE_IOSTREAMS</code></p>
<dd>Set to ON to use libraries compiled with STLPort deprecated &quot;native iostreams&quot; (&quot;n&quot; tag). Default is <code>OFF</code>.</p>
<dt><code>Boost_COMPILER</code></p>
<dd>Set to the compiler-specific library suffix (e.g. <code>-gcc43</code>). Default is auto-computed for the C++ compiler in use. </p>
<p> Changed in version 3.9: A list may be used if multiple compatible suffixes should be tested for, in decreasing order of preference. </p>
<dt><code>Boost_LIB_PREFIX</code></p>
<dd>New in version 3.18. </p>
<p> Set to the platform-specific library name prefix (e.g. <code>lib</code>) used by Boost static libs. This is needed only on platforms where CMake does not know the prefix by default.</p>
<dt><code>Boost_ARCHITECTURE</code></p>
<dd>New in version 3.13. </p>
<p> Set to the architecture-specific library suffix (e.g. <code>-x64</code>). Default is auto-computed for the C++ compiler in use.</p>
<dt><code>Boost_THREADAPI</code></p>
<dd>Suffix for <code>thread</code> component library name, such as <code>pthread</code> or <code>win32</code>. Names with and without this suffix will both be tried.</p>
<dt><code>Boost_NAMESPACE</code></p>
<dd>Alternate namespace used to build boost with e.g. if set to <code>myboost</code>, will search for <code>myboost_thread</code> instead of <code>boost_thread</code>. </p>
<p> Other variables one may set to control this module are:</p>
<dt><code>Boost_DEBUG</code></p>
<dd>Set to <code>ON</code> to enable debug output from <code>FindBoost</code>. Please enable this before filing any bug report.</p>
<dt><code>Boost_REALPATH</code></p>
<dd>Set to <code>ON</code> to resolve symlinks for discovered libraries to assist with packaging. For example, the &quot;system&quot; component library may be resolved to <code>/usr/lib/libboost_system.so.1.67.0</code> instead of <code>/usr/lib/libboost_system.so</code>. This does not affect linking and should not be enabled unless the user needs this information.</p>
<dt><code>Boost_LIBRARY_DIR</code></p>
<dd>Default value for <code>Boost_LIBRARY_DIR_RELEASE</code> and <code>Boost_LIBRARY_DIR_DEBUG</code>.</p>
<dt><code>Boost_NO_WARN_NEW_VERSIONS</code></p>
<dd>New in version 3.20. </p>
<p> Set to <code>ON</code> to suppress the warning about unknown dependencies for new Boost versions. </p>
<p> On Visual Studio and Borland compilers Boost headers request automatic linking to corresponding libraries. This requires matching libraries to be linked explicitly or available in the link library search path. In this case setting <code>Boost_USE_STATIC_LIBS</code> to <code>OFF</code> may not achieve dynamic linking. Boost automatic linking typically requests static libraries with a few exceptions (such as <code>Boost.Python</code>). Use: </p>
<pre>add_definitions(${Boost_LIB_DIAGNOSTIC_DEFINITIONS})</pre>
<p>to ask Boost to report information about automatic linking requests.</dl>
<h3>Examples</h3>
<p>Find Boost headers only: </p>
<pre>find_package(Boost 1.36.0)
if(Boost_FOUND)
 include_directories(${Boost_INCLUDE_DIRS})
 add_executable(foo foo.cc)
endif()</pre>
<p>Find Boost libraries and use imported targets: </p>
<pre>find_package(Boost 1.56 REQUIRED COMPONENTS
 date_time filesystem iostreams)
add_executable(foo foo.cc)
target_link_libraries(foo Boost::date_time Boost::filesystem
 Boost::iostreams)</pre>
<p>Find Boost Python 3.6 libraries and use imported targets: </p>
<pre>find_package(Boost 1.67 REQUIRED COMPONENTS
 python36 numpy36)
add_executable(foo foo.cc)
target_link_libraries(foo Boost::python36 Boost::numpy36)</pre>
<p>Find Boost headers and some <i>static</i> (release only) libraries: </p>
<pre>set(Boost_USE_STATIC_LIBS ON) # only find static libs
set(Boost_USE_DEBUG_LIBS OFF) # ignore debug libs and
set(Boost_USE_RELEASE_LIBS ON) # only find release libs
set(Boost_USE_MULTITHREADED ON)
set(Boost_USE_STATIC_RUNTIME OFF)
find_package(Boost 1.66.0 COMPONENTS date_time filesystem system ...)
if(Boost_FOUND)
 include_directories(${Boost_INCLUDE_DIRS})
 add_executable(foo foo.cc)
 target_link_libraries(foo ${Boost_LIBRARIES})
endif()</pre>
<h3>Boost CMake</h3>
<p>If Boost was built using the boost-cmake project or from Boost 1.70.0 on it provides a package configuration file for use with find_package&#8217;s config mode. This module looks for the package configuration file called <code>BoostConfig.cmake</code> or <code>boost-config.cmake</code> and stores the result in <code>CACHE</code> entry <code>Boost_DIR</code>. If found, the package configuration file is loaded and this module returns with no further action. See documentation of the Boost CMake package configuration for details on what it provides. </p>
<p> Set <code>Boost_NO_BOOST_CMAKE</code> to <code>ON</code>, to disable the search for boost-cmake.</p>
<h3>FindBullet</h3>
<p>Try to find the Bullet physics engine </p>
<pre>This module defines the following variables</pre>
<pre>BULLET_FOUND - Was bullet found
BULLET_INCLUDE_DIRS - the Bullet include directories
BULLET_LIBRARIES - Link to this, by default it includes
 all bullet components (Dynamics,
 Collision, LinearMath, &amp; SoftBody)</pre>
<pre>This module accepts the following variables</pre>
<pre>BULLET_ROOT - Can be set to bullet install path or Windows build path</pre>
<h3>FindBZip2</h3>
<p>Try to find BZip2</p>
<h3>IMPORTED Targets</h3>
<p>New in version 3.12. </p>
<p> This module defines <code>IMPORTED</code> target <code>BZip2::BZip2</code>, if BZip2 has been found.</p>
<h3>Result Variables</h3>
<p>This module defines the following variables:</p>
<dl>
<dt><code>BZIP2_FOUND</code></p>
<dd>system has BZip2</p>
<dt><code>BZIP2_INCLUDE_DIRS</code></p>
<dd>New in version 3.12: the BZip2 include directories </p>
<dt><code>BZIP2_LIBRARIES</code></p>
<dd>Link these to use BZip2</p>
<dt><code>BZIP2_NEED_PREFIX</code></p>
<dd>this is set if the functions are prefixed with <code>BZ2_</code></p>
<dt><code>BZIP2_VERSION_STRING</code></p>
<dd>the version of BZip2 found</dl>
<h3>Cache variables</h3>
<p>The following cache variables may also be set:</p>
<dl>
<dt><code>BZIP2_INCLUDE_DIR</code></p>
<dd>the BZip2 include directory</dl>
<h3>FindCABLE</h3>
<p>Find CABLE </p>
<p> This module finds if CABLE is installed and determines where the include files and libraries are. This code sets the following variables: </p>
<pre>CABLE the path to the cable executable
CABLE_TCL_LIBRARY the path to the Tcl wrapper library
CABLE_INCLUDE_DIR the path to the include directory</pre>
<p>To build Tcl wrappers, you should add shared library and link it to ${CABLE_TCL_LIBRARY}. You should also add ${CABLE_INCLUDE_DIR} as an include directory.</p>
<h3>FindCoin3D</h3>
<p>Find Coin3D (Open Inventor) </p>
<p> Coin3D is an implementation of the Open Inventor API. It provides data structures and algorithms for 3D visualization. </p>
<p> This module defines the following variables </p>
<pre>COIN3D_FOUND - system has Coin3D - Open Inventor
COIN3D_INCLUDE_DIRS - where the Inventor include directory can be found
COIN3D_LIBRARIES - Link to this to use Coin3D</pre>
<h3>FindCUDAToolkit</h3>
<p>New in version 3.17. </p>
<p> This script locates the NVIDIA CUDA toolkit and the associated libraries, but does not require the <code>CUDA</code> language be enabled for a given project. This module does not search for the NVIDIA CUDA Samples. </p>
<p> New in version 3.19: QNX support.</p>
<h3>Search Behavior</h3>
<p>The CUDA Toolkit search behavior uses the following order:</p>
<dl>
<dt>1.</p>
<dd>If the <code>CUDA</code> language has been enabled we will use the directory containing the compiler as the first search location for <code>nvcc</code>.</p>
<dt>2.</p>
<dd>If the <code>CUDAToolkit_ROOT</code> cmake configuration variable (e.g., <code>-DCUDAToolkit_ROOT=/some/path</code>) <i>or</i> environment variable is defined, it will be searched. If both an environment variable <code>and</code> a configuration variable are specified, the <i>configuration</i> variable takes precedence. </p>
<p> The directory specified here must be such that the executable <code>nvcc</code> or the appropriate <code>version.txt</code> file can be found underneath the specified directory.</p>
<dt>3.</p>
<dd>If the CUDA_PATH environment variable is defined, it will be searched for <code>nvcc</code>.</p>
<dt>4.</p>
<dd>The user&#8217;s path is searched for <code>nvcc</code> using <code>find_program()</code>. If this is found, no subsequent search attempts are performed. Users are responsible for ensuring that the first <code>nvcc</code> to show up in the path is the desired path in the event that multiple CUDA Toolkits are installed.</p>
<dt>5.</p>
<dd>On Unix systems, if the symbolic link <code>/usr/local/cuda</code> exists, this is used. No subsequent search attempts are performed. No default symbolic link location exists for the Windows platform.</p>
<dt>6.</p>
<dd>The platform specific default install locations are searched. If exactly one candidate is found, this is used. The default CUDA Toolkit install locations searched are: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Platform </td>
<td> Search Pattern
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> macOS </td>
<td> <code>/Developer/NVIDIA/CUDA-X.Y</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Other Unix </td>
<td> <code>/usr/local/cuda-X.Y</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Windows </td>
<td> <code>C:\Program Files\NVIDIA GPU Computing Toolkit\CUDAX.Y</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Where <code>X.Y</code> would be a specific version of the CUDA Toolkit, such as <code>/usr/local/cuda-9.0</code> or <code>C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA9.0</code> </p>
<p> <code>NOTE:</code> When multiple CUDA Toolkits are installed in the default location of a system (e.g., both <code>/usr/local/cuda-9.0</code> and <code>/usr/local/cuda-10.0</code> exist but the <code>/usr/local/cuda</code> symbolic link does <code>not</code> exist), this package is marked as <code>not</code> found. </p>
<p> There are too many factors involved in making an automatic decision in the presence of multiple CUDA Toolkits being installed. In this situation, users are encouraged to either (1) set <code>CUDAToolkit_ROOT</code> or (2) ensure that the correct <code>nvcc</code> executable shows up in <code>$PATH</code> for <code>find_program()</code> to find.</dl>
<h3>Arguments</h3>
<dl>
<dt><code>[&lt;version&gt;]</code></p>
<dd>The <code>[&lt;version&gt;]</code> argument requests a version with which the package found should be compatible. See find_package version format for more details.</dl>
<h3>Options</h3>
<dl>
<dt><code>REQUIRED</code></p>
<dd>If specified, configuration will error if a suitable CUDA Toolkit is not found.</p>
<dt><code>QUIET</code></p>
<dd>If specified, the search for a suitable CUDA Toolkit will not produce any messages.</p>
<dt><code>EXACT</code></p>
<dd>If specified, the CUDA Toolkit is considered found only if the exact <code>VERSION</code> specified is recovered.</dl>
<h3>Imported targets</h3>
<p>An imported target named <code>CUDA::toolkit</code> is provided. </p>
<p> This module defines <code>IMPORTED</code> targets for each of the following libraries that are part of the CUDAToolkit:</p>
<dl>
<dt>&bull;</p>
<dd><i>CUDA Runtime Library</i></p>
<dt>&bull;</p>
<dd><i>CUDA Driver Library</i></p>
<dt>&bull;</p>
<dd><i>cuBLAS</i></p>
<dt>&bull;</p>
<dd><i>cuFFT</i></p>
<dt>&bull;</p>
<dd><i>cuRAND</i></p>
<dt>&bull;</p>
<dd><i>cuSOLVER</i></p>
<dt>&bull;</p>
<dd><i>cuSPARSE</i></p>
<dt>&bull;</p>
<dd><i>cuPTI</i></p>
<dt>&bull;</p>
<dd><i>NPP</i></p>
<dt>&bull;</p>
<dd><i>nvBLAS</i></p>
<dt>&bull;</p>
<dd><i>nvGRAPH</i></p>
<dt>&bull;</p>
<dd><i>nvJPEG</i></p>
<dt>&bull;</p>
<dd><i>nvidia-ML</i></p>
<dt>&bull;</p>
<dd><i>nvRTC</i></p>
<dt>&bull;</p>
<dd><i>nvToolsExt</i></p>
<dt>&bull;</p>
<dd><i>OpenCL</i></p>
<dt>&bull;</p>
<dd><i>cuLIBOS</i></dl>
<h3>CUDA Runtime Library</h3>
<p>The CUDA Runtime library (cudart) are what most applications will typically need to link against to make any calls such as <i>cudaMalloc</i>, and <i>cudaFree</i>. </p>
<p> Targets Created:</p>
<dl>
<dt>&bull;</p>
<dd><code>CUDA::cudart</code></p>
<dt>&bull;</p>
<dd><code>CUDA::cudart_static</code></dl>
<h3>CUDA Driver Library</h3>
<p>The CUDA Driver library (cuda) are used by applications that use calls such as <i>cuMemAlloc</i>, and <i>cuMemFree</i>. This is generally used by advanced </p>
<p> Targets Created:</p>
<dl>
<dt>&bull;</p>
<dd><code>CUDA::cuda_driver</code></p>
<dt>&bull;</p>
<dd><code>CUDA::cuda_driver</code></dl>
<h3>cuBLAS</h3>
<p>The <i>cuBLAS</i> library. </p>
<p> Targets Created:</p>
<dl>
<dt>&bull;</p>
<dd><code>CUDA::cublas</code></p>
<dt>&bull;</p>
<dd><code>CUDA::cublas_static</code></p>
<dt>&bull;</p>
<dd><code>CUDA::cublasLt</code> starting in CUDA 10.1</p>
<dt>&bull;</p>
<dd><code>CUDA::cublasLt_static</code> starting in CUDA 10.1</dl>
<h3>cuFFT</h3>
<p>The <i>cuFFT</i> library. </p>
<p> Targets Created:</p>
<dl>
<dt>&bull;</p>
<dd><code>CUDA::cufft</code></p>
<dt>&bull;</p>
<dd><code>CUDA::cufftw</code></p>
<dt>&bull;</p>
<dd><code>CUDA::cufft_static</code></p>
<dt>&bull;</p>
<dd><code>CUDA::cufftw_static</code></dl>
<h3>cuRAND</h3>
<p>The <i>cuRAND</i> library. </p>
<p> Targets Created:</p>
<dl>
<dt>&bull;</p>
<dd><code>CUDA::curand</code></p>
<dt>&bull;</p>
<dd><code>CUDA::curand_static</code></dl>
<h3>cuSOLVER</h3>
<p>The <i>cuSOLVER</i> library. </p>
<p> Targets Created:</p>
<dl>
<dt>&bull;</p>
<dd><code>CUDA::cusolver</code></p>
<dt>&bull;</p>
<dd><code>CUDA::cusolver_static</code></dl>
<h3>cuSPARSE</h3>
<p>The <i>cuSPARSE</i> library. </p>
<p> Targets Created:</p>
<dl>
<dt>&bull;</p>
<dd><code>CUDA::cusparse</code></p>
<dt>&bull;</p>
<dd><code>CUDA::cusparse_static</code></dl>
<h3>cupti</h3>
<p>The <i>NVIDIA CUDA Profiling Tools Interface</i>. </p>
<p> Targets Created:</p>
<dl>
<dt>&bull;</p>
<dd><code>CUDA::cupti</code></p>
<dt>&bull;</p>
<dd><code>CUDA::cupti_static</code></dl>
<h3>Npp</h3>
<p>The <i>NPP</i> libraries. </p>
<p> Targets Created:</p>
<dl>
<dt>&bull;</p>
<dd><i>nppc</i>:</p>
<dt>&bull;</p>
<dd><code>CUDA::nppc</code></p>
<dt>&bull;</p>
<dd><code>CUDA::nppc_static</code></p>
<dt>&bull;</p>
<dd><i>nppial</i>: Arithmetic and logical operation functions in <i>nppi_arithmetic_and_logical_operations.h</i></p>
<dt>&bull;</p>
<dd><code>CUDA::nppial</code></p>
<dt>&bull;</p>
<dd><code>CUDA::nppial_static</code></p>
<dt>&bull;</p>
<dd><i>nppicc</i>: Color conversion and sampling functions in <i>nppi_color_conversion.h</i></p>
<dt>&bull;</p>
<dd><code>CUDA::nppicc</code></p>
<dt>&bull;</p>
<dd><code>CUDA::nppicc_static</code></p>
<dt>&bull;</p>
<dd><i>nppicom</i>: JPEG compression and decompression functions in <i>nppi_compression_functions.h</i> Removed starting in CUDA 11.0, use <i>nvJPEG</i> instead.</p>
<dt>&bull;</p>
<dd><code>CUDA::nppicom</code></p>
<dt>&bull;</p>
<dd><code>CUDA::nppicom_static</code></p>
<dt>&bull;</p>
<dd><i>nppidei</i>: Data exchange and initialization functions in <i>nppi_data_exchange_and_initialization.h</i></p>
<dt>&bull;</p>
<dd><code>CUDA::nppidei</code></p>
<dt>&bull;</p>
<dd><code>CUDA::nppidei_static</code></p>
<dt>&bull;</p>
<dd><i>nppif</i>: Filtering and computer vision functions in <i>nppi_filter_functions.h</i></p>
<dt>&bull;</p>
<dd><code>CUDA::nppif</code></p>
<dt>&bull;</p>
<dd><code>CUDA::nppif_static</code></p>
<dt>&bull;</p>
<dd><i>nppig</i>: Geometry transformation functions found in <i>nppi_geometry_transforms.h</i></p>
<dt>&bull;</p>
<dd><code>CUDA::nppig</code></p>
<dt>&bull;</p>
<dd><code>CUDA::nppig_static</code></p>
<dt>&bull;</p>
<dd><i>nppim</i>: Morphological operation functions found in <i>nppi_morphological_operations.h</i></p>
<dt>&bull;</p>
<dd><code>CUDA::nppim</code></p>
<dt>&bull;</p>
<dd><code>CUDA::nppim_static</code></p>
<dt>&bull;</p>
<dd><i>nppist</i>: Statistics and linear transform in <i>nppi_statistics_functions.h</i> and <i>nppi_linear_transforms.h</i></p>
<dt>&bull;</p>
<dd><code>CUDA::nppist</code></p>
<dt>&bull;</p>
<dd><code>CUDA::nppist_static</code></p>
<dt>&bull;</p>
<dd><i>nppisu</i>: Memory support functions in <i>nppi_support_functions.h</i></p>
<dt>&bull;</p>
<dd><code>CUDA::nppisu</code></p>
<dt>&bull;</p>
<dd><code>CUDA::nppisu_static</code></p>
<dt>&bull;</p>
<dd><i>nppitc</i>: Threshold and compare operation functions in <i>nppi_threshold_and_compare_operations.h</i></p>
<dt>&bull;</p>
<dd><code>CUDA::nppitc</code></p>
<dt>&bull;</p>
<dd><code>CUDA::nppitc_static</code></p>
<dt>&bull;</p>
<dd><i>npps</i>:</p>
<dt>&bull;</p>
<dd><code>CUDA::npps</code></p>
<dt>&bull;</p>
<dd><code>CUDA::npps_static</code></dl>
<h3>nvBLAS</h3>
<p>The <i>nvBLAS</i> libraries. This is a shared library only. </p>
<p> Targets Created:</p>
<dl>
<dt>&bull;</p>
<dd><code>CUDA::nvblas</code></dl>
<h3>nvGRAPH</h3>
<p>The <i>nvGRAPH</i> library. Removed starting in CUDA 11.0 </p>
<p> Targets Created:</p>
<dl>
<dt>&bull;</p>
<dd><code>CUDA::nvgraph</code></p>
<dt>&bull;</p>
<dd><code>CUDA::nvgraph_static</code></dl>
<h3>nvJPEG</h3>
<p>The <i>nvJPEG</i> library. Introduced in CUDA 10. </p>
<p> Targets Created:</p>
<dl>
<dt>&bull;</p>
<dd><code>CUDA::nvjpeg</code></p>
<dt>&bull;</p>
<dd><code>CUDA::nvjpeg_static</code></dl>
<h3>nvRTC</h3>
<p>The <i>nvRTC</i> (Runtime Compilation) library. This is a shared library only. </p>
<p> Targets Created:</p>
<dl>
<dt>&bull;</p>
<dd><code>CUDA::nvrtc</code></dl>
<h3>nvidia-ML</h3>
<p>The <i>NVIDIA Management Library</i>. This is a shared library only. </p>
<p> Targets Created:</p>
<dl>
<dt>&bull;</p>
<dd><code>CUDA::nvml</code></dl>
<h3>nvToolsExt</h3>
<p>The <i>NVIDIA Tools Extension</i>. This is a shared library only. </p>
<p> Targets Created:</p>
<dl>
<dt>&bull;</p>
<dd><code>CUDA::nvToolsExt</code></dl>
<h3>OpenCL</h3>
<p>The <i>NVIDIA OpenCL Library</i>. This is a shared library only. </p>
<p> Targets Created:</p>
<dl>
<dt>&bull;</p>
<dd><code>CUDA::OpenCL</code></dl>
<h3>cuLIBOS</h3>
<p>The cuLIBOS library is a backend thread abstraction layer library which is static only. The <code>CUDA::cublas_static</code>, <code>CUDA::cusparse_static</code>, <code>CUDA::cufft_static</code>, <code>CUDA::curand_static</code>, and (when implemented) NPP libraries all automatically have this dependency linked. </p>
<p> Target Created:</p>
<dl>
<dt>&bull;</p>
<dd><code>CUDA::culibos</code> </p>
<p> <code>Note</code>: direct usage of this target by consumers should not be necessary.</dl>
<h3>Result variables</h3>
<dl>
<dt><code>CUDAToolkit_FOUND</code></p>
<dd>A boolean specifying whether or not the CUDA Toolkit was found.</p>
<dt><code>CUDAToolkit_VERSION</code></p>
<dd>The exact version of the CUDA Toolkit found (as reported by <code>nvcc &#8211;version</code> or <code>version.txt</code>).</p>
<dt><code>CUDAToolkit_VERSION_MAJOR</code></p>
<dd>The major version of the CUDA Toolkit.</p>
<dt><code>CUDAToolkit_VERSION_MINOR</code></p>
<dd>The minor version of the CUDA Toolkit.</p>
<dt><code>CUDAToolkit_VERSION_PATCH</code></p>
<dd>The patch version of the CUDA Toolkit.</p>
<dt><code>CUDAToolkit_BIN_DIR</code></p>
<dd>The path to the CUDA Toolkit library directory that contains the CUDA executable <code>nvcc</code>.</p>
<dt><code>CUDAToolkit_INCLUDE_DIRS</code></p>
<dd>The path to the CUDA Toolkit <code>include</code> folder containing the header files required to compile a project linking against CUDA.</p>
<dt><code>CUDAToolkit_LIBRARY_DIR</code></p>
<dd>The path to the CUDA Toolkit library directory that contains the CUDA Runtime library <code>cudart</code>.</p>
<dt><code>CUDAToolkit_LIBRARY_ROOT</code></p>
<dd>New in version 3.18. </p>
<p> The path to the CUDA Toolkit directory containing the nvvm directory and version.txt.</p>
<dt><code>CUDAToolkit_TARGET_DIR</code></p>
<dd>The path to the CUDA Toolkit directory including the target architecture when cross-compiling. When not cross-compiling this will be equivalent to the parent directory of <code>CUDAToolkit_BIN_DIR</code>.</p>
<dt><code>CUDAToolkit_NVCC_EXECUTABLE</code></p>
<dd>The path to the NVIDIA CUDA compiler <code>nvcc</code>. Note that this path may <code>not</code> be the same as <code>CMAKE_CUDA_COMPILER</code>. <code>nvcc</code> must be found to determine the CUDA Toolkit version as well as determining other features of the Toolkit. This variable is set for the convenience of modules that depend on this one.</dl>
<h3>FindCups</h3>
<p>Find the Common UNIX Printing System (CUPS). </p>
<p> Set <code>CUPS_REQUIRE_IPP_DELETE_ATTRIBUTE</code> to <code>TRUE</code> if you need a version which features this function (i.e. at least <code>1.1.19</code>)</p>
<h3>Imported targets</h3>
<p>New in version 3.15. </p>
<p> This module defines <code>IMPORTED</code> target <code>Cups::Cups</code>, if Cups has been found.</p>
<h3>Result variables</h3>
<p>This module will set the following variables in your project:</p>
<dl>
<dt><code>CUPS_FOUND</code></p>
<dd>true if CUPS headers and libraries were found</p>
<dt><code>CUPS_INCLUDE_DIRS</code></p>
<dd>the directory containing the Cups headers</p>
<dt><code>CUPS_LIBRARIES</code></p>
<dd>the libraries to link against to use CUPS.</p>
<dt><code>CUPS_VERSION_STRING</code></p>
<dd>the version of CUPS found (since CMake 2.8.8)</dl>
<h3>Cache variables</h3>
<p>The following cache variables may also be set:</p>
<dl>
<dt><code>CUPS_INCLUDE_DIR</code></p>
<dd>the directory containing the Cups headers</dl>
<h3>FindCURL</h3>
<p>Find the native CURL headers and libraries. </p>
<p> New in version 3.14: This module accept optional COMPONENTS to check supported features and protocols: </p>
<pre>PROTOCOLS: ICT FILE FTP FTPS GOPHER HTTP HTTPS IMAP IMAPS LDAP LDAPS POP3
 POP3S RTMP RTSP SCP SFTP SMB SMBS SMTP SMTPS TELNET TFTP
FEATURES: SSL IPv6 UnixSockets libz AsynchDNS IDN GSS-API PSL SPNEGO
 Kerberos NTLM NTLM_WB TLS-SRP HTTP2 HTTPS-proxy</pre>
<h3>IMPORTED Targets</h3>
<p>New in version 3.12. </p>
<p> This module defines <code>IMPORTED</code> target <code>CURL::libcurl</code>, if curl has been found.</p>
<h3>Result Variables</h3>
<p>This module defines the following variables:</p>
<dl>
<dt><code>CURL_FOUND</code></p>
<dd>&quot;True&quot; if <code>curl</code> found.</p>
<dt><code>CURL_INCLUDE_DIRS</code></p>
<dd>where to find <code>curl</code>/<code>curl.h</code>, etc.</p>
<dt><code>CURL_LIBRARIES</code></p>
<dd>List of libraries when using <code>curl</code>.</p>
<dt><code>CURL_VERSION_STRING</code></p>
<dd>The version of <code>curl</code> found. </p>
<p> New in version 3.13: Debug and Release variants are found separately. </p>
</dl>
<h3>CURL CMake</h3>
<p>New in version 3.17. </p>
<p> If CURL was built using the CMake buildsystem then it provides its own <code>CURLConfig.cmake</code> file for use with the <code>find_package()</code> command&#8217;s config mode. This module looks for this file and, if found, returns its results with no further action. </p>
<p> Set <code>CURL_NO_CURL_CMAKE</code> to <code>ON</code> to disable this search.</p>
<h3>FindCurses</h3>
<p>Find the curses or ncurses include file and library.</p>
<h3>Result Variables</h3>
<p>This module defines the following variables:</p>
<dl>
<dt><code>CURSES_FOUND</code></p>
<dd>True if Curses is found.</p>
<dt><code>CURSES_INCLUDE_DIRS</code></p>
<dd>The include directories needed to use Curses.</p>
<dt><code>CURSES_LIBRARIES</code></p>
<dd>The libraries needed to use Curses.</p>
<dt><code>CURSES_CFLAGS</code></p>
<dd>New in version 3.16. </p>
<p> Parameters which ought be given to C/C++ compilers when using Curses.</p>
<dt><code>CURSES_HAVE_CURSES_H</code></p>
<dd>True if curses.h is available.</p>
<dt><code>CURSES_HAVE_NCURSES_H</code></p>
<dd>True if ncurses.h is available.</p>
<dt><code>CURSES_HAVE_NCURSES_NCURSES_H</code></p>
<dd>True if <code>ncurses/ncurses.h</code> is available.</p>
<dt><code>CURSES_HAVE_NCURSES_CURSES_H</code></p>
<dd>True if <code>ncurses/curses.h</code> is available. </p>
<p> Set <code>CURSES_NEED_NCURSES</code> to <code>TRUE</code> before the <code>find_package(Curses)</code> call if NCurses functionality is required. </p>
<p> New in version 3.10: Set <code>CURSES_NEED_WIDE</code> to <code>TRUE</code> before the <code>find_package(Curses)</code> call if unicode functionality is required. </p>
</dl>
<h3>Backward Compatibility</h3>
<p>The following variable are provided for backward compatibility:</p>
<dl>
<dt><code>CURSES_INCLUDE_DIR</code></p>
<dd>Path to Curses include. Use <code>CURSES_INCLUDE_DIRS</code> instead.</p>
<dt><code>CURSES_LIBRARY</code></p>
<dd>Path to Curses library. Use <code>CURSES_LIBRARIES</code> instead.</dl>
<h3>FindCVS</h3>
<p>Find the Concurrent Versions System (CVS). </p>
<p> The module defines the following variables: </p>
<pre>CVS_EXECUTABLE - path to cvs command line client
CVS_FOUND - true if the command line client was found</pre>
<p>Example usage: </p>
<pre>find_package(CVS)
if(CVS_FOUND)
 message(&quot;CVS found: ${CVS_EXECUTABLE}&quot;)
endif()</pre>
<h3>FindCxxTest</h3>
<p>Find CxxTest unit testing framework. </p>
<p> Find the CxxTest suite and declare a helper macro for creating unit tests and integrating them with CTest. For more details on CxxTest see <i><a rel="nofollow" href="http://cxxtest.tigris.org">http://cxxtest.tigris.org</a></i> </p>
<p> INPUT Variables </p>
<pre>CXXTEST_USE_PYTHON [deprecated since 1.3]
 Only used in the case both Python &amp; Perl
 are detected on the system to control
 which CxxTest code generator is used.
 Valid only for CxxTest version 3.</pre>
<pre>NOTE: In older versions of this Find Module,
this variable controlled if the Python test
generator was used instead of the Perl one,
regardless of which scripting language the
user had installed.</pre>
<pre>CXXTEST_TESTGEN_ARGS (since CMake 2.8.3)
 Specify a list of options to pass to the CxxTest code
 generator. If not defined, --error-printer is
 passed.</pre>
<p>OUTPUT Variables </p>
<pre>CXXTEST_FOUND
 True if the CxxTest framework was found
CXXTEST_INCLUDE_DIRS
 Where to find the CxxTest include directory
CXXTEST_PERL_TESTGEN_EXECUTABLE
 The perl-based test generator
CXXTEST_PYTHON_TESTGEN_EXECUTABLE
 The python-based test generator
CXXTEST_TESTGEN_EXECUTABLE (since CMake 2.8.3)
 The test generator that is actually used (chosen using user preferences
 and interpreters found in the system)
CXXTEST_TESTGEN_INTERPRETER (since CMake 2.8.3)
 The full path to the Perl or Python executable on the system, on
 platforms where the script cannot be executed using its shebang line.</pre>
<p>MACROS for optional use by CMake users: </p>
<pre>CXXTEST_ADD_TEST(&lt;test_name&gt; &lt;gen_source_file&gt; &lt;input_files_to_testgen...&gt;)
 Creates a CxxTest runner and adds it to the CTest testing suite
 Parameters:
 test_name The name of the test
 gen_source_file The generated source filename to be
 generated by CxxTest
 input_files_to_testgen The list of header files containing the
 CxxTest::TestSuite's to be included in
 this runner</pre>
<pre>#==============
Example Usage:</pre>
<pre>find_package(CxxTest)
if(CXXTEST_FOUND)
 include_directories(${CXXTEST_INCLUDE_DIR})
 enable_testing()</pre>
<pre> CXXTEST_ADD_TEST(unittest_foo foo_test.cc
 ${CMAKE_CURRENT_SOURCE_DIR}/foo_test.h)
 target_link_libraries(unittest_foo foo) # as needed
endif()</pre>
<pre>This will (if CxxTest is found):
1. Invoke the testgen executable to autogenerate foo_test.cc in the
 binary tree from &quot;foo_test.h&quot; in the current source directory.
2. Create an executable and test called unittest_foo.</pre>
<pre>#=============
Example foo_test.h:</pre>
<pre>#include &lt;cxxtest/TestSuite.h&gt;</pre>
<pre>class MyTestSuite : public CxxTest::TestSuite
{
public:
 void testAddition( void )
 {
 TS_ASSERT( 1 + 1 &gt; 1 );
 TS_ASSERT_EQUALS( 1 + 1, 2 );
 }
};</pre>
<h3>FindCygwin</h3>
<p>Find Cygwin, a POSIX-compatible environment that runs natively on Microsoft Windows</p>
<h3>FindDart</h3>
<p>Find DART </p>
<p> This module looks for the dart testing software and sets DART_ROOT to point to where it found it.</p>
<h3>FindDCMTK</h3>
<p>Find DICOM ToolKit (DCMTK) libraries and applications </p>
<p> The module defines the following variables: </p>
<pre>DCMTK_INCLUDE_DIRS - Directories to include to use DCMTK
DCMTK_LIBRARIES - Files to link against to use DCMTK
DCMTK_FOUND - If false, don't try to use DCMTK
DCMTK_DIR - (optional) Source directory for DCMTK</pre>
<h3>Compatibility</h3>
<p>This module is able to find a version of DCMTK that does or does not export a <i>DCMTKConfig.cmake</i> file. It applies a two step process:</p>
<dl>
<dt>&bull;</p>
<dd>Step 1: Attempt to find DCMTK version providing a <i>DCMTKConfig.cmake</i> file.</p>
<dt>&bull;</p>
<dd>Step 2: If step 1 failed, rely on <i>FindDCMTK.cmake</i> to set <i>DCMTK_*</i> variables details below. </p>
<p> <i>Recent DCMTK</i> provides a <i>DCMTKConfig.cmake</i> <code>package configuration file</code>. To exclusively use the package configuration file (recommended when possible), pass the <i>NO_MODULE</i> option to <code>find_package()</code>. For example, <i>find_package(DCMTK NO_MODULE)</i>. This requires official DCMTK snapshot <i>3.6.1_20140617</i> or newer. </p>
<p> Until all clients update to the more recent DCMTK, build systems will need to support different versions of DCMTK. </p>
<p> On any given system, the following combinations of DCMTK versions could be considered: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> </td>
<td> SYSTEM DCMTK </td>
<td> LOCAL DCMTK </td>
<td> Supported ?
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Case A </td>
<td> NA </td>
<td> [ ] DCMTKConfig </td>
<td> YES
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Case B </td>
<td> NA </td>
<td> [X] DCMTKConfig </td>
<td> YES
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Case C </td>
<td> [ ] DCMTKConfig </td>
<td> NA </td>
<td> YES
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Case D </td>
<td> [X] DCMTKConfig </td>
<td> NA </td>
<td> YES
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Case E </td>
<td> [ ] DCMTKConfig </td>
<td> [ ] DCMTKConfig </td>
<td> YES (*)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Case F </td>
<td> [X] DCMTKConfig </td>
<td> [ ] DCMTKConfig </td>
<td> NO
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Case G </td>
<td> [ ] DCMTKConfig </td>
<td> [X] DCMTKConfig </td>
<td> YES
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Case H </td>
<td> [X] DCMTKConfig </td>
<td> [X] DCMTKConfig </td>
<td> YES
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
</table>
<p></center> (*) See Troubleshooting section. </p>
<p> Legend: NA &#8230;&#8230;&#8230;&#8230;&#8230;: Means that no System or Local DCMTK is available </p>
<p> [ ] DCMTKConfig ..: Means that the version of DCMTK does NOT export a DCMTKConfig.cmake file. </p>
<p> [X] DCMTKConfig ..: Means that the version of DCMTK exports a DCMTKConfig.cmake file.</dl>
<h3>Troubleshooting</h3>
<p>What to do if my project finds a different version of DCMTK? </p>
<p> Remove DCMTK entry from the CMake cache per <code>find_package()</code> documentation.</p>
<h3>FindDevIL</h3>
<p>This module locates the developer&#8217;s image library. <i><a rel="nofollow" href="http://openil.sourceforge.net/">http://openil.sourceforge.net/</a></i></p>
<h3>IMPORTED Targets</h3>
<p>New in version 3.21. </p>
<p> This module defines the <code>IMPORTED</code> targets:</p>
<dl>
<dt><code>DevIL::IL</code></p>
<dd>Defined if the system has DevIL.</p>
<dt><code>DevIL::ILU</code></p>
<dd>Defined if the system has DevIL Utilities.</p>
<dt><code>DevIL::ILUT</code></p>
<dd>Defined if the system has DevIL Utility Toolkit.</dl>
<h3>Result Variables</h3>
<p>This module sets:</p>
<dl>
<dt><code>IL_LIBRARIES</code></p>
<dd>The name of the IL library. These include the full path to the core DevIL library. This one has to be linked into the application.</p>
<dt><code>ILU_LIBRARIES</code></p>
<dd>The name of the ILU library. Again, the full path. This library is for filters and effects, not actual loading. It doesn&#8217;t have to be linked if the functionality it provides is not used.</p>
<dt><code>ILUT_LIBRARIES</code></p>
<dd>The name of the ILUT library. Full path. This part of the library interfaces with OpenGL. It is not strictly needed in applications.</p>
<dt><code>IL_INCLUDE_DIR</code></p>
<dd>where to find the il.h, ilu.h and ilut.h files.</p>
<dt><code>DevIL_FOUND</code></p>
<dd>This is set to TRUE if all the above variables were set. This will be set to false if ILU or ILUT are not found, even if they are not needed. In most systems, if one library is found all the others are as well. That&#8217;s the way the DevIL developers release it.</p>
<dt><code>DevIL_ILUT_FOUND</code></p>
<dd>New in version 3.21. </p>
<p> This is set to TRUE if the ILUT library is found.</dl>
<h3>FindDoxygen</h3>
<p>Doxygen is a documentation generation tool (see <i><a rel="nofollow" href="http://www.doxygen.org">http://www.doxygen.org</a></i>). This module looks for Doxygen and some optional tools it supports:</p>
<dl>
<dt><code>dot</code></p>
<dd><i>Graphviz</i> <code>dot</code> utility used to render various graphs.</p>
<dt><code>mscgen</code></p>
<dd><i>Message Chart Generator</i> utility used by Doxygen&#8217;s <code>\msc</code> and <code>\mscfile</code> commands.</p>
<dt><code>dia</code></p>
<dd><i>Dia</i> the diagram editor used by Doxygen&#8217;s <code>\diafile</code> command. </p>
<p> New in version 3.9: These tools are available as components in the <code>find_package()</code> command. For example: </p>
<pre># Require dot, treat the other components as optional
find_package(Doxygen
 REQUIRED dot
 OPTIONAL_COMPONENTS mscgen dia)</pre>
<p>The following variables are defined by this module:</p>
<dt><code>DOXYGEN_FOUND</code></p>
<dd>True if the <code>doxygen</code> executable was found.</p>
<dt><code>DOXYGEN_VERSION</code></p>
<dd>The version reported by <code>doxygen &#8211;version</code>. </p>
<p> New in version 3.9: The module defines <code>IMPORTED</code> targets for Doxygen and each component found. These can be used as part of custom commands, etc. and should be preferred over old-style (and now deprecated) variables like <code>DOXYGEN_EXECUTABLE</code>. The following import targets are defined if their corresponding executable could be found (the component import targets will only be defined if that component was requested): </p>
<pre>Doxygen::doxygen
Doxygen::dot
Doxygen::mscgen
Doxygen::dia</pre>
</dl>
<h3>Functions</h3>
<dl>
<dt><code>doxygen_add_docs</code></p>
<dd>New in version 3.9. </p>
<p> This function is intended as a convenience for adding a target for generating documentation with Doxygen. It aims to provide sensible defaults so that projects can generally just provide the input files and directories and that will be sufficient to give sensible results. The function supports the ability to customize the Doxygen configuration used to build the documentation. </p>
<pre>doxygen_add_docs(targetName
 [filesOrDirs...]
 [ALL]
 [USE_STAMP_FILE]
 [WORKING_DIRECTORY dir]
 [COMMENT comment])</pre>
<p>The function constructs a <code>Doxyfile</code> and defines a custom target that runs Doxygen on that generated file. The listed files and directories are used as the <code>INPUT</code> of the generated <code>Doxyfile</code> and they can contain wildcards. Any files that are listed explicitly will also be added as <code>SOURCES</code> of the custom target so they will show up in an IDE project&#8217;s source list. </p>
<p> So that relative input paths work as expected, by default the working directory of the Doxygen command will be the current source directory (i.e. <code>CMAKE_CURRENT_SOURCE_DIR</code>). This can be overridden with the <code>WORKING_DIRECTORY</code> option to change the directory used as the relative base point. Note also that Doxygen&#8217;s default behavior is to strip the working directory from relative paths in the generated documentation (see the <code>STRIP_FROM_PATH</code> <i>Doxygen config option</i> for details). </p>
<p> If provided, the optional <code>comment</code> will be passed as the <code>COMMENT</code> for the <code>add_custom_target()</code> command used to create the custom target internally. </p>
<p> New in version 3.12: If <code>ALL</code> is set, the target will be added to the default build target. </p>
<p> New in version 3.16: If <code>USE_STAMP_FILE</code> is set, the custom command defined by this function will create a stamp file with the name <code>&lt;targetName&gt;.stamp</code> in the current binary directory whenever doxygen is re-run. With this option present, all items in <code>&lt;filesOrDirs&gt;</code> must be files (i.e. no directories, symlinks or wildcards) and each of the files must exist at the time <code>doxygen_add_docs()</code> is called. An error will be raised if any of the items listed is missing or is not a file when <code>USE_STAMP_FILE</code> is given. A dependency will be created on each of the files so that doxygen will only be re-run if one of the files is updated. Without the <code>USE_STAMP_FILE</code> option, doxygen will always be re-run if the <code>&lt;targetName&gt;</code> target is built regardless of whether anything listed in <code>&lt;filesOrDirs&gt;</code> has changed. </p>
<p> The contents of the generated <code>Doxyfile</code> can be customized by setting CMake variables before calling <code>doxygen_add_docs()</code>. Any variable with a name of the form <code>DOXYGEN_&lt;tag&gt;</code> will have its value substituted for the corresponding <code>&lt;tag&gt;</code> configuration option in the <code>Doxyfile</code>. See the <i>Doxygen documentation</i> for the full list of supported configuration options. </p>
<p> Some of Doxygen&#8217;s defaults are overridden to provide more appropriate behavior for a CMake project. Each of the following will be explicitly set unless the variable already has a value before <code>doxygen_add_docs()</code> is called (with some exceptions noted):</p>
<dt><code>DOXYGEN_HAVE_DOT</code></p>
<dd>Set to <code>YES</code> if the <code>dot</code> component was requested and it was found, <code>NO</code> otherwise. Any existing value of <code>DOXYGEN_HAVE_DOT</code> is ignored.</p>
<dt><code>DOXYGEN_DOT_MULTI_TARGETS</code></p>
<dd>Set to <code>YES</code> by this module (note that this requires a <code>dot</code> version newer than 1.8.10). This option is only meaningful if <code>DOXYGEN_HAVE_DOT</code> is also set to <code>YES</code>.</p>
<dt><code>DOXYGEN_GENERATE_LATEX</code></p>
<dd>Set to <code>NO</code> by this module.</p>
<dt><code>DOXYGEN_WARN_FORMAT</code></p>
<dd>For Visual Studio based generators, this is set to the form recognized by the Visual Studio IDE: <code>$file($line) : $text</code>. For all other generators, Doxygen&#8217;s default value is not overridden.</p>
<dt><code>DOXYGEN_PROJECT_NAME</code></p>
<dd>Populated with the name of the current project (i.e. <code>PROJECT_NAME</code>).</p>
<dt><code>DOXYGEN_PROJECT_NUMBER</code></p>
<dd>Populated with the version of the current project (i.e. <code>PROJECT_VERSION</code>).</p>
<dt><code>DOXYGEN_PROJECT_BRIEF</code></p>
<dd>Populated with the description of the current project (i.e. <code>PROJECT_DESCRIPTION</code>).</p>
<dt><code>DOXYGEN_INPUT</code></p>
<dd>Projects should not set this variable. It will be populated with the set of files and directories passed to <code>doxygen_add_docs()</code>, thereby providing consistent behavior with the other built-in commands like <code>add_executable()</code>, <code>add_library()</code> and <code>add_custom_target()</code>. If a variable named <code>DOXYGEN_INPUT</code> is set by the project, it will be ignored and a warning will be issued.</p>
<dt><code>DOXYGEN_RECURSIVE</code></p>
<dd>Set to <code>YES</code> by this module.</p>
<dt><code>DOXYGEN_EXCLUDE_PATTERNS</code></p>
<dd>If the set of inputs includes directories, this variable will specify patterns used to exclude files from them. The following patterns are added by <code>doxygen_add_docs()</code> to ensure CMake-specific files and directories are not included in the input. If the project sets <code>DOXYGEN_EXCLUDE_PATTERNS</code>, those contents are merged with these additional patterns rather than replacing them: </p>
<pre>*/.git/*
*/.svn/*
*/.hg/*
*/CMakeFiles/*
*/_CPack_Packages/*
DartConfiguration.tcl
CMakeLists.txt
CMakeCache.txt</pre>
<dt><code>DOXYGEN_OUTPUT_DIRECTORY</code></p>
<dd>Set to <code>CMAKE_CURRENT_BINARY_DIR</code> by this module. Note that if the project provides its own value for this and it is a relative path, it will be converted to an absolute path relative to the current binary directory. This is necessary because doxygen will normally be run from a directory within the source tree so that relative source paths work as expected. If this directory does not exist, it will be recursively created prior to executing the doxygen commands. </p>
<p> To change any of these defaults or override any other Doxygen config option, set relevant variables before calling <code>doxygen_add_docs()</code>. For example: </p>
<pre>set(DOXYGEN_GENERATE_HTML NO)
set(DOXYGEN_GENERATE_MAN YES)
doxygen_add_docs(
 doxygen
 ${PROJECT_SOURCE_DIR}
 COMMENT &quot;Generate man pages&quot;
)</pre>
<p>A number of Doxygen config options accept lists of values, but Doxygen requires them to be separated by whitespace. CMake variables hold lists as a string with items separated by semi-colons, so a conversion needs to be performed. The <code>doxygen_add_docs()</code> command specifically checks the following Doxygen config options and will convert their associated CMake variable&#8217;s contents into the required form if set. CMake variables are named <code>DOXYGEN_&lt;name&gt;</code> for the Doxygen settings specified here. </p>
<pre>ABBREVIATE_BRIEF
ALIASES
CITE_BIB_FILES
DIAFILE_DIRS
DOTFILE_DIRS
DOT_FONTPATH
ENABLED_SECTIONS
EXAMPLE_PATH
EXAMPLE_PATTERNS
EXCLUDE
EXCLUDE_PATTERNS
EXCLUDE_SYMBOLS
EXPAND_AS_DEFINED
EXTENSION_MAPPING
EXTRA_PACKAGES
EXTRA_SEARCH_MAPPINGS
FILE_PATTERNS
FILTER_PATTERNS
FILTER_SOURCE_PATTERNS
HTML_EXTRA_FILES
HTML_EXTRA_STYLESHEET
IGNORE_PREFIX
IMAGE_PATH
INCLUDE_FILE_PATTERNS
INCLUDE_PATH
INPUT
LATEX_EXTRA_FILES
LATEX_EXTRA_STYLESHEET
MATHJAX_EXTENSIONS
MSCFILE_DIRS
PLANTUML_INCLUDE_PATH
PREDEFINED
QHP_CUST_FILTER_ATTRS
QHP_SECT_FILTER_ATTRS
STRIP_FROM_INC_PATH
STRIP_FROM_PATH
TAGFILES
TCL_SUBST</pre>
<p>The following single value Doxygen options will be quoted automatically if they contain at least one space: </p>
<pre>CHM_FILE
DIA_PATH
DOCBOOK_OUTPUT
DOCSET_FEEDNAME
DOCSET_PUBLISHER_NAME
DOT_FONTNAME
DOT_PATH
EXTERNAL_SEARCH_ID
FILE_VERSION_FILTER
GENERATE_TAGFILE
HHC_LOCATION
HTML_FOOTER
HTML_HEADER
HTML_OUTPUT
HTML_STYLESHEET
INPUT_FILTER
LATEX_FOOTER
LATEX_HEADER
LATEX_OUTPUT
LAYOUT_FILE
MAN_OUTPUT
MAN_SUBDIR
MATHJAX_CODEFILE
MSCGEN_PATH
OUTPUT_DIRECTORY
PERL_PATH
PLANTUML_JAR_PATH
PROJECT_BRIEF
PROJECT_LOGO
PROJECT_NAME
QCH_FILE
QHG_LOCATION
QHP_CUST_FILTER_NAME
QHP_VIRTUAL_FOLDER
RTF_EXTENSIONS_FILE
RTF_OUTPUT
RTF_STYLESHEET_FILE
SEARCHDATA_FILE
USE_MDFILE_AS_MAINPAGE
WARN_FORMAT
WARN_LOGFILE
XML_OUTPUT</pre>
<p>New in version 3.11: There are situations where it may be undesirable for a particular config option to be automatically quoted by <code>doxygen_add_docs()</code>, such as <code>ALIASES</code> which may need to include its own embedded quoting. The <code>DOXYGEN_VERBATIM_VARS</code> variable can be used to specify a list of Doxygen variables (including the leading <code>DOXYGEN_</code> prefix) which should not be quoted. The project is then responsible for ensuring that those variables&#8217; values make sense when placed directly in the Doxygen input file. In the case of list variables, list items are still separated by spaces, it is only the automatic quoting that is skipped. For example, the following allows <code>doxygen_add_docs()</code> to apply quoting to <code>DOXYGEN_PROJECT_BRIEF</code>, but not each item in the <code>DOXYGEN_ALIASES</code> list (bracket syntax can also be used to make working with embedded quotes easier): </p>
<pre>set(DOXYGEN_PROJECT_BRIEF &quot;String with spaces&quot;)
set(DOXYGEN_ALIASES
 [[somealias=&quot;@some_command param&quot;]]
 &quot;anotherAlias=@foobar&quot;
)
set(DOXYGEN_VERBATIM_VARS DOXYGEN_ALIASES)</pre>
<p>The resultant <code>Doxyfile</code> will contain the following lines: </p>
<pre>PROJECT_BRIEF = &quot;String with spaces&quot;
ALIASES = somealias=&quot;@some_command param&quot; anotherAlias=@foobar</pre>
</dl>
<h3>Deprecated Result Variables</h3>
<p>Deprecated since version 3.9. </p>
<p> For compatibility with previous versions of CMake, the following variables are also defined but they are deprecated and should no longer be used:</p>
<dl>
<dt><code>DOXYGEN_EXECUTABLE</code></p>
<dd>The path to the <code>doxygen</code> command. If projects need to refer to the <code>doxygen</code> executable directly, they should use the <code>Doxygen::doxygen</code> import target instead.</p>
<dt><code>DOXYGEN_DOT_FOUND</code></p>
<dd>True if the <code>dot</code> executable was found.</p>
<dt><code>DOXYGEN_DOT_EXECUTABLE</code></p>
<dd>The path to the <code>dot</code> command. If projects need to refer to the <code>dot</code> executable directly, they should use the <code>Doxygen::dot</code> import target instead.</p>
<dt><code>DOXYGEN_DOT_PATH</code></p>
<dd>The path to the directory containing the <code>dot</code> executable as reported in <code>DOXYGEN_DOT_EXECUTABLE</code>. The path may have forward slashes even on Windows and is not suitable for direct substitution into a <code>Doxyfile.in</code> template. If you need this value, get the <code>IMPORTED_LOCATION</code> property of the <code>Doxygen::dot</code> target and use <code>get_filename_component()</code> to extract the directory part of that path. You may also want to consider using <code>file(TO_NATIVE_PATH)</code> to prepare the path for a Doxygen configuration file.</dl>
<h3>Deprecated Hint Variables</h3>
<p>Deprecated since version 3.9. </p>
<dl>
<dt><code>DOXYGEN_SKIP_DOT</code></p>
<dd>This variable has no effect for the component form of <code>find_package</code>. In backward compatibility mode (i.e. without components list) it prevents the finder module from searching for Graphviz&#8217;s <code>dot</code> utility.</dl>
<h3>FindEnvModules</h3>
<p>New in version 3.15. </p>
<p> Locate an environment module implementation and make commands available to CMake scripts to use them. This is compatible with both Lua-based Lmod and TCL-based EnvironmentModules. </p>
<p> This module is intended for the use case of setting up the compiler and library environment within a CTest Script (<code>ctest -S</code>). It can also be used in a CMake Script (<code>cmake -P</code>). </p>
<p> <code>NOTE:</code> The loaded environment will not survive past the end of the calling process. Do not use this module in project code (<code>CMakeLists.txt</code> files) to load a compiler environment; it will not be available during the build. Instead load the environment manually before running CMake or using the generated build system.</p>
<h3>Example Usage</h3>
<pre>set(CTEST_BUILD_NAME &quot;CrayLinux-CrayPE-Cray-dynamic&quot;)
set(CTEST_BUILD_CONFIGURATION Release)
set(CTEST_BUILD_FLAGS &quot;-k -j8&quot;)
set(CTEST_CMAKE_GENERATOR &quot;Unix Makefiles&quot;)
...
find_package(EnvModules REQUIRED)
env_module(purge)
env_module(load modules)
env_module(load craype)
env_module(load PrgEnv-cray)
env_module(load craype-knl)
env_module(load cray-mpich)
env_module(load cray-libsci)
set(ENV{CRAYPE_LINK_TYPE} dynamic)
...</pre>
<h3>Result Variables</h3>
<p>This module will set the following variables in your project:</p>
<dl>
<dt><code>EnvModules_FOUND</code></p>
<dd>True if a compatible environment modules framework was found.</dl>
<h3>Cache Variables</h3>
<p>The following cache variable will be set:</p>
<dl>
<dt><code>EnvModules_COMMAND</code></p>
<dd>The low level module command to use. Currently supported implementations are the Lua based Lmod and TCL based EnvironmentModules.</dl>
<h3>Environment Variables</h3>
<dl>
<dt><code>ENV{MODULESHOME}</code></p>
<dd>Usually set by the module environment implementation, used as a hint to locate the module command to execute.</dl>
<h3>Provided Functions</h3>
<p>This defines the following CMake functions for interacting with environment modules:</p>
<dl>
<dt><code>env_module</code></p>
<dd>Execute an aribitrary module command: </p>
<pre>env_module(cmd arg1 ... argN)
env_module(
 COMMAND cmd arg1 ... argN
 [OUTPUT_VARIABLE &lt;out-var&gt;]
 [RESULT_VARIABLE &lt;ret-var&gt;]
)</pre>
<p>The options are:</p>
<dt><code>cmd arg1 &#8230; argN</code></p>
<dd>The module sub-command and arguments to execute as if they were passed directly to the module command in your shell environment.</p>
<dt><code>OUTPUT_VARIABLE &lt;out-var&gt;</code></p>
<dd>The standard output from executing the module command.</p>
<dt><code>RESULT_VARIABLE &lt;ret-var&gt;</code></p>
<dd>The return code from executing the module command.</p>
<dt><code>env_module_swap</code></p>
<dd>Swap one module for another: </p>
<pre>env_module_swap(out_mod in_mod
 [OUTPUT_VARIABLE &lt;out-var&gt;]
 [RESULT_VARIABLE &lt;ret-var&gt;]
)</pre>
<p>This is functionally equivalent to the <code>module swap out_mod in_mod</code> shell command. The options are:</p>
<dt><code>OUTPUT_VARIABLE &lt;out-var&gt;</code></p>
<dd>The standard output from executing the module command.</p>
<dt><code>RESULT_VARIABLE &lt;ret-var&gt;</code></p>
<dd>The return code from executing the module command.</p>
<dt><code>env_module_list</code></p>
<dd>Retrieve the list of currently loaded modules: </p>
<pre>env_module_list(&lt;out-var&gt;)</pre>
<p>This is functionally equivalent to the <code>module list</code> shell command. The result is stored in <code>&lt;out-var&gt;</code> as a properly formatted CMake semicolon-separated list variable.</p>
<dt><code>env_module_avail</code></p>
<dd>Retrieve the list of available modules: </p>
<pre>env_module_avail([&lt;mod-prefix&gt;] &lt;out-var&gt;)</pre>
<p>This is functionally equivalent to the <code>module avail &lt;mod-prefix&gt;</code> shell command. The result is stored in <code>&lt;out-var&gt;</code> as a properly formatted CMake semicolon-separated list variable.</dl>
<h3>FindEXPAT</h3>
<p>Find the native Expat headers and library. Expat is a stream-oriented XML parser library written in C.</p>
<h3>Imported Targets</h3>
<p>New in version 3.10. </p>
<p> This module defines the following <code>IMPORTED</code> targets:</p>
<dl>
<dt><code>EXPAT::EXPAT</code></p>
<dd>The Expat <code>expat</code> library, if found.</dl>
<h3>Result Variables</h3>
<p>This module will set the following variables in your project:</p>
<dl>
<dt><code>EXPAT_INCLUDE_DIRS</code></p>
<dd>where to find expat.h, etc.</p>
<dt><code>EXPAT_LIBRARIES</code></p>
<dd>the libraries to link against to use Expat.</p>
<dt><code>EXPAT_FOUND</code></p>
<dd>true if the Expat headers and libraries were found.</dl>
<h3>FindFLEX</h3>
<p>Find Fast Lexical Analyzer (Flex) executable and provides a macro to generate custom build rules </p>
<p> The module defines the following variables: </p>
<pre>FLEX_FOUND - True is flex executable is found
FLEX_EXECUTABLE - the path to the flex executable
FLEX_VERSION - the version of flex
FLEX_LIBRARIES - The flex libraries
FLEX_INCLUDE_DIRS - The path to the flex headers</pre>
<p>The minimum required version of flex can be specified using the standard syntax, e.g. <code>find_package(FLEX 2.5.13)</code> </p>
<p> If flex is found on the system, the module provides the macro: </p>
<pre>FLEX_TARGET(Name FlexInput FlexOutput
 [COMPILE_FLAGS &lt;string&gt;]
 [DEFINES_FILE &lt;string&gt;]
 )</pre>
<p>which creates a custom command to generate the <code>FlexOutput</code> file from the <code>FlexInput</code> file. Name is an alias used to get details of this custom command. If <code>COMPILE_FLAGS</code> option is specified, the next parameter is added to the flex command line. </p>
<p> New in version 3.5: If flex is configured to output a header file, the <code>DEFINES_FILE</code> option may be used to specify its name. </p>
<p> Changed in version 3.17: When <code>CMP0098</code> is set to <code>NEW</code>, <code>flex</code> runs in the <code>CMAKE_CURRENT_BINARY_DIR</code> directory. </p>
<p> The macro defines the following variables: </p>
<pre>FLEX_${Name}_DEFINED - true is the macro ran successfully
FLEX_${Name}_OUTPUTS - the source file generated by the custom rule, an
alias for FlexOutput
FLEX_${Name}_INPUT - the flex source file, an alias for ${FlexInput}
FLEX_${Name}_OUTPUT_HEADER - the header flex output, if any.</pre>
<p>Flex scanners often use tokens defined by Bison: the code generated by Flex depends of the header generated by Bison. This module also defines a macro: </p>
<pre>ADD_FLEX_BISON_DEPENDENCY(FlexTarget BisonTarget)</pre>
<p>which adds the required dependency between a scanner and a parser where <code>FlexTarget</code> and <code>BisonTarget</code> are the first parameters of respectively <code>FLEX_TARGET</code> and <code>BISON_TARGET</code> macros. </p>
<pre>====================================================================
Example:</pre>
<pre>find_package(BISON)
find_package(FLEX)</pre>
<pre>BISON_TARGET(MyParser parser.y ${CMAKE_CURRENT_BINARY_DIR}/parser.cpp)
FLEX_TARGET(MyScanner lexer.l ${CMAKE_CURRENT_BINARY_DIR}/lexer.cpp)
ADD_FLEX_BISON_DEPENDENCY(MyScanner MyParser)</pre>
<pre> include_directories(${CMAKE_CURRENT_BINARY_DIR})
 add_executable(Foo
 Foo.cc
 ${BISON_MyParser_OUTPUTS}
 ${FLEX_MyScanner_OUTPUTS}
 )
 target_link_libraries(Foo ${FLEX_LIBRARIES})
====================================================================</pre>
<h3>FindFLTK</h3>
<p>Find the Fast Light Toolkit (FLTK) library</p>
<h3>Input Variables</h3>
<p>By default this module will search for all of the FLTK components and add them to the <code>FLTK_LIBRARIES</code> variable. You can limit the components which get placed in <code>FLTK_LIBRARIES</code> by defining one or more of the following three options:</p>
<dl>
<dt><code>FLTK_SKIP_OPENGL</code></p>
<dd>Set to true to disable searching for the FLTK GL library</p>
<dt><code>FLTK_SKIP_FORMS</code></p>
<dd>Set to true to disable searching for the FLTK Forms library</p>
<dt><code>FLTK_SKIP_IMAGES</code></p>
<dd>Set to true to disable searching for the FLTK Images library </p>
<p> FLTK is composed also by a binary tool. You can set the following option:</p>
<dt><code>FLTK_SKIP_FLUID</code></p>
<dd>Set to true to not look for the FLUID binary</dl>
<h3>Result Variables</h3>
<p>The following variables will be defined:</p>
<dl>
<dt><code>FLTK_FOUND</code></p>
<dd>True if all components not skipped were found</p>
<dt><code>FLTK_INCLUDE_DIR</code></p>
<dd>Path to the include directory for FLTK header files</p>
<dt><code>FLTK_LIBRARIES</code></p>
<dd>List of the FLTK libraries found</p>
<dt><code>FLTK_FLUID_EXECUTABLE</code></p>
<dd>Path to the FLUID binary tool</p>
<dt><code>FLTK_WRAP_UI</code></p>
<dd>True if FLUID is found, used to enable the FLTK_WRAP_UI command</dl>
<h3>Cache Variables</h3>
<p>The following cache variables are also available to set or use:</p>
<dl>
<dt><code>FLTK_BASE_LIBRARY_RELEASE</code></p>
<dd>The FLTK base library (optimized)</p>
<dt><code>FLTK_BASE_LIBRARY_DEBUG</code></p>
<dd>The FLTK base library (debug)</p>
<dt><code>FLTK_GL_LIBRARY_RELEASE</code></p>
<dd>The FLTK GL library (optimized)</p>
<dt><code>FLTK_GL_LIBRARY_DEBUG</code></p>
<dd>The FLTK GL library (debug)</p>
<dt><code>FLTK_FORMS_LIBRARY_RELEASE</code></p>
<dd>The FLTK Forms library (optimized)</p>
<dt><code>FLTK_FORMS_LIBRARY_DEBUG</code></p>
<dd>The FLTK Forms library (debug)</p>
<dt><code>FLTK_IMAGES_LIBRARY_RELEASE</code></p>
<dd>The FLTK Images protobuf library (optimized)</p>
<dt><code>FLTK_IMAGES_LIBRARY_DEBUG</code></p>
<dd>The FLTK Images library (debug) </p>
<p> New in version 3.11: Debug and Release variants are found separately and use per-configuration variables. </p>
</dl>
<h3>FindFLTK2</h3>
<p>Find the native FLTK 2.0 includes and library </p>
<p> The following settings are defined </p>
<pre>FLTK2_FLUID_EXECUTABLE, where to find the Fluid tool
FLTK2_WRAP_UI, This enables the FLTK2_WRAP_UI command
FLTK2_INCLUDE_DIR, where to find include files
FLTK2_LIBRARIES, list of fltk2 libraries
FLTK2_FOUND, Don't use FLTK2 if false.</pre>
<p>The following settings should not be used in general. </p>
<pre>FLTK2_BASE_LIBRARY = the full path to fltk2.lib
FLTK2_GL_LIBRARY = the full path to fltk2_gl.lib
FLTK2_IMAGES_LIBRARY = the full path to fltk2_images.lib</pre>
<h3>FindFontconfig</h3>
<p>New in version 3.14. </p>
<p> Find Fontconfig headers and library.</p>
<h3>Imported Targets</h3>
<dl>
<dt><code>Fontconfig::Fontconfig</code></p>
<dd>The Fontconfig library, if found.</dl>
<h3>Result Variables</h3>
<p>This will define the following variables in your project:</p>
<dl>
<dt><code>Fontconfig_FOUND</code></p>
<dd>true if (the requested version of) Fontconfig is available.</p>
<dt><code>Fontconfig_VERSION</code></p>
<dd>the version of Fontconfig.</p>
<dt><code>Fontconfig_LIBRARIES</code></p>
<dd>the libraries to link against to use Fontconfig.</p>
<dt><code>Fontconfig_INCLUDE_DIRS</code></p>
<dd>where to find the Fontconfig headers.</p>
<dt><code>Fontconfig_COMPILE_OPTIONS</code></p>
<dd>this should be passed to target_compile_options(), if the target is not used for linking</dl>
<h3>FindFreetype</h3>
<p>Find the FreeType font renderer includes and library.</p>
<h3>Imported Targets</h3>
<p>New in version 3.10. </p>
<p> This module defines the following <code>IMPORTED</code> target:</p>
<dl>
<dt><code>Freetype::Freetype</code></p>
<dd>The Freetype <code>freetype</code> library, if found</dl>
<h3>Result Variables</h3>
<p>This module will set the following variables in your project:</p>
<dl>
<dt><code>FREETYPE_FOUND</code></p>
<dd>true if the Freetype headers and libraries were found</p>
<dt><code>FREETYPE_INCLUDE_DIRS</code></p>
<dd>directories containing the Freetype headers. This is the concatenation of the variables:</p>
<dt><code>FREETYPE_INCLUDE_DIR_ft2build</code></p>
<dd>directory holding the main Freetype API configuration header</p>
<dt><code>FREETYPE_INCLUDE_DIR_freetype2</code></p>
<dd>directory holding Freetype public headers</p>
<dt><code>FREETYPE_LIBRARIES</code></p>
<dd>the library to link against</p>
<dt><code>FREETYPE_VERSION_STRING</code></p>
<dd>the version of freetype found </p>
<p> New in version 3.7: Debug and Release variants are found separately. </p>
</dl>
<h3>Hints</h3>
<p>The user may set the environment variable <code>FREETYPE_DIR</code> to the root directory of a Freetype installation.</p>
<h3>FindGCCXML</h3>
<p>Find the GCC-XML front-end executable. </p>
<p> This module will define the following variables: </p>
<pre>GCCXML - the GCC-XML front-end executable.</pre>
<h3>FindGDAL</h3>
<p>Find Geospatial Data Abstraction Library (GDAL).</p>
<h3>IMPORTED Targets</h3>
<p>New in version 3.14. </p>
<p> This module defines <code>IMPORTED</code> target <code>GDAL::GDAL</code> if GDAL has been found.</p>
<h3>Result Variables</h3>
<p>This module will set the following variables in your project:</p>
<dl>
<dt><code>GDAL_FOUND</code></p>
<dd>True if GDAL is found.</p>
<dt><code>GDAL_INCLUDE_DIRS</code></p>
<dd>Include directories for GDAL headers.</p>
<dt><code>GDAL_LIBRARIES</code></p>
<dd>Libraries to link to GDAL.</p>
<dt><code>GDAL_VERSION</code></p>
<dd>New in version 3.14: The version of GDAL found. </p>
</dl>
<h3>Cache variables</h3>
<p>The following cache variables may also be set:</p>
<dl>
<dt><code>GDAL_LIBRARY</code></p>
<dd>The libgdal library file.</p>
<dt><code>GDAL_INCLUDE_DIR</code></p>
<dd>The directory containing <code>gdal.h</code>.</dl>
<h3>Hints</h3>
<p>Set <code>GDAL_DIR</code> or <code>GDAL_ROOT</code> in the environment to specify the GDAL installation prefix. </p>
<p> The following variables may be set to modify the search strategy:</p>
<dl>
<dt><code>FindGDAL_SKIP_GDAL_CONFIG</code></p>
<dd>If set, <code>gdal-config</code> will not be used. This can be useful if there are GDAL libraries built with autotools (which provide the tool) and CMake (which do not) in the same environment.</p>
<dt><code>GDAL_ADDITIONAL_LIBRARY_VERSIONS</code></p>
<dd>Extra versions of library names to search for.</dl>
<h3>FindGettext</h3>
<p>Find GNU gettext tools </p>
<p> This module looks for the GNU gettext tools. This module defines the following values: </p>
<pre>GETTEXT_MSGMERGE_EXECUTABLE: the full path to the msgmerge tool.
GETTEXT_MSGFMT_EXECUTABLE: the full path to the msgfmt tool.
GETTEXT_FOUND: True if gettext has been found.
GETTEXT_VERSION_STRING: the version of gettext found (since CMake 2.8.8)</pre>
<p>Additionally it provides the following macros: </p>
<p> GETTEXT_CREATE_TRANSLATIONS ( outputFile [ALL] file1 &#8230; fileN ) </p>
<pre>This will create a target &quot;translations&quot; which will convert the
given input po files into the binary output mo file. If the
ALL option is used, the translations will also be created when
building the default target.</pre>
<p>GETTEXT_PROCESS_POT_FILE( &lt;potfile&gt; [ALL] [INSTALL_DESTINATION &lt;destdir&gt;] LANGUAGES &lt;lang1&gt; &lt;lang2&gt; &#8230; ) </p>
<pre>Process the given pot file to mo files.
If INSTALL_DESTINATION is given then automatically install rules will
be created, the language subdirectory will be taken into account
(by default use share/locale/).
If ALL is specified, the pot file is processed when building the all target.
It creates a custom target &quot;potfile&quot;.</pre>
<p>GETTEXT_PROCESS_PO_FILES( &lt;lang&gt; [ALL] [INSTALL_DESTINATION &lt;dir&gt;] PO_FILES &lt;po1&gt; &lt;po2&gt; &#8230; ) </p>
<pre>Process the given po files to mo files for the given language.
If INSTALL_DESTINATION is given then automatically install rules will
be created, the language subdirectory will be taken into account
(by default use share/locale/).
If ALL is specified, the po files are processed when building the all target.
It creates a custom target &quot;pofiles&quot;.</pre>
<p>New in version 3.2: If you wish to use the Gettext library (libintl), use <code>FindIntl</code>.</p>
<h3>FindGIF</h3>
<p>This finds the Graphics Interchange Format (GIF) library (<code>giflib</code>)</p>
<h3>Imported targets</h3>
<p>This module defines the following <code>IMPORTED</code> target:</p>
<dl>
<dt><code>GIF::GIF</code></p>
<dd>The <code>giflib</code> library, if found.</dl>
<h3>Result variables</h3>
<p>This module will set the following variables in your project:</p>
<dl>
<dt><code>GIF_FOUND</code></p>
<dd>If false, do not try to use GIF.</p>
<dt><code>GIF_INCLUDE_DIRS</code></p>
<dd>where to find gif_lib.h, etc.</p>
<dt><code>GIF_LIBRARIES</code></p>
<dd>the libraries needed to use GIF.</p>
<dt><code>GIF_VERSION</code></p>
<dd>3, 4 or a full version string (eg 5.1.4) for versions &gt;= 4.1.6.</dl>
<h3>Cache variables</h3>
<p>The following cache variables may also be set:</p>
<dl>
<dt><code>GIF_INCLUDE_DIR</code></p>
<dd>where to find the GIF headers.</p>
<dt><code>GIF_LIBRARY</code></p>
<dd>where to find the GIF library.</dl>
<h3>Hints</h3>
<p><code>GIF_DIR</code> is an environment variable that would correspond to the <code>./configure &#8211;prefix=$GIF_DIR</code>.</p>
<h3>FindGit</h3>
<p>The module defines the following variables:</p>
<dl>
<dt><code>GIT_EXECUTABLE</code></p>
<dd>Path to Git command-line client.</p>
<dt><code>Git_FOUND</code>, <code>GIT_FOUND</code></p>
<dd>True if the Git command-line client was found.</p>
<dt><code>GIT_VERSION_STRING</code></p>
<dd>The version of Git found. </p>
<p> New in version 3.14: The module defines the following <code>IMPORTED</code> targets (when <code>CMAKE_ROLE</code> is <code>PROJECT</code>): </p>
<dt><code>Git::Git</code></p>
<dd>Executable of the Git command-line client. </p>
<p> Example usage: </p>
<pre>find_package(Git)
if(Git_FOUND)
 message(&quot;Git found: ${GIT_EXECUTABLE}&quot;)
endif()</pre>
</dl>
<h3>FindGLEW</h3>
<p>Find the OpenGL Extension Wrangler Library (GLEW)</p>
<h3>Input Variables</h3>
<p>The following variables may be set to influence this module&#8217;s behavior:</p>
<dl>
<dt><code>GLEW_USE_STATIC_LIBS</code></p>
<dd>to find and create <code>IMPORTED</code> target for static linkage.</p>
<dt><code>GLEW_VERBOSE</code></p>
<dd>to output a detailed log of this module.</dl>
<h3>Imported Targets</h3>
<p>New in version 3.1. </p>
<p> This module defines the following Imported Targets:</p>
<dl>
<dt><code>GLEW::glew</code></p>
<dd>The GLEW shared library.</p>
<dt><code>GLEW::glew_s</code></p>
<dd>The GLEW static library, if <code>GLEW_USE_STATIC_LIBS</code> is set to <code>TRUE</code>.</p>
<dt><code>GLEW::GLEW</code></p>
<dd>Duplicates either <code>GLEW::glew</code> or <code>GLEW::glew_s</code> based on availability.</dl>
<h3>Result Variables</h3>
<p>This module defines the following variables:</p>
<dl>
<dt><code>GLEW_INCLUDE_DIRS</code></p>
<dd>include directories for GLEW</p>
<dt><code>GLEW_LIBRARIES</code></p>
<dd>libraries to link against GLEW</p>
<dt><code>GLEW_SHARED_LIBRARIES</code></p>
<dd>libraries to link against shared GLEW</p>
<dt><code>GLEW_STATIC_LIBRARIES</code></p>
<dd>libraries to link against static GLEW</p>
<dt><code>GLEW_FOUND</code></p>
<dd>true if GLEW has been found and can be used</p>
<dt><code>GLEW_VERSION</code></p>
<dd>GLEW version</p>
<dt><code>GLEW_VERSION_MAJOR</code></p>
<dd>GLEW major version</p>
<dt><code>GLEW_VERSION_MINOR</code></p>
<dd>GLEW minor version</p>
<dt><code>GLEW_VERSION_MICRO</code></p>
<dd>GLEW micro version </p>
<p> New in version 3.7: Debug and Release variants are found separately. </p>
</dl>
<h3>FindGLUT</h3>
<p>Find OpenGL Utility Toolkit (GLUT) library and include files.</p>
<h3>IMPORTED Targets</h3>
<p>New in version 3.1. </p>
<p> This module defines the <code>IMPORTED</code> targets:</p>
<dl>
<dt><code>GLUT::GLUT</code></p>
<dd>Defined if the system has GLUT.</dl>
<h3>Result Variables</h3>
<p>This module sets the following variables: </p>
<pre>GLUT_INCLUDE_DIR, where to find GL/glut.h, etc.
GLUT_LIBRARIES, the libraries to link against
GLUT_FOUND, If false, do not try to use GLUT.</pre>
<p>Also defined, but not for general use are: </p>
<pre>GLUT_glut_LIBRARY = the full path to the glut library.
GLUT_Xmu_LIBRARY = the full path to the Xmu library.
GLUT_Xi_LIBRARY = the full path to the Xi Library.</pre>
<p>New in version 3.13: Debug and Release variants are found separately.</p>
<h3>FindGnuplot</h3>
<p>this module looks for gnuplot </p>
<p> Once done this will define </p>
<pre>GNUPLOT_FOUND - system has Gnuplot
GNUPLOT_EXECUTABLE - the Gnuplot executable
GNUPLOT_VERSION_STRING - the version of Gnuplot found (since CMake 2.8.8)</pre>
<p>GNUPLOT_VERSION_STRING will not work for old versions like 3.7.1.</p>
<h3>FindGnuTLS</h3>
<p>Find the GNU Transport Layer Security library (gnutls)</p>
<h3>IMPORTED Targets</h3>
<p>New in version 3.16. </p>
<p> This module defines <code>IMPORTED</code> target <code>GnuTLS::GnuTLS</code>, if gnutls has been found.</p>
<h3>Result Variables</h3>
<dl>
<dt><code>GNUTLS_FOUND</code></p>
<dd>System has gnutls</p>
<dt><code>GNUTLS_INCLUDE_DIR</code></p>
<dd>The gnutls include directory</p>
<dt><code>GNUTLS_LIBRARIES</code></p>
<dd>The libraries needed to use gnutls</p>
<dt><code>GNUTLS_DEFINITIONS</code></p>
<dd>Compiler switches required for using gnutls</p>
<dt><code>GNUTLS_VERSION</code></p>
<dd>version of gnutls.</dl>
<h3>FindGSL</h3>
<p>New in version 3.2. </p>
<p> Find the native GNU Scientific Library (GSL) includes and libraries. </p>
<p> The GNU Scientific Library (GSL) is a numerical library for C and C++ programmers. It is free software under the GNU General Public License.</p>
<h3>Imported Targets</h3>
<p>If GSL is found, this module defines the following <code>IMPORTED</code> targets: </p>
<pre>GSL::gsl - The main GSL library.
GSL::gslcblas - The CBLAS support library used by GSL.</pre>
<h3>Result Variables</h3>
<p>This module will set the following variables in your project: </p>
<pre>GSL_FOUND - True if GSL found on the local system
GSL_INCLUDE_DIRS - Location of GSL header files.
GSL_LIBRARIES - The GSL libraries.
GSL_VERSION - The version of the discovered GSL install.</pre>
<h3>Hints</h3>
<p>Set <code>GSL_ROOT_DIR</code> to a directory that contains a GSL installation. </p>
<p> This script expects to find libraries at <code>$GSL_ROOT_DIR/lib</code> and the GSL headers at <code>$GSL_ROOT_DIR/include/gsl</code>. The library directory may optionally provide Release and Debug folders. If available, the libraries named <code>gsld</code>, <code>gslblasd</code> or <code>cblasd</code> are recognized as debug libraries. For Unix-like systems, this script will use <code>$GSL_ROOT_DIR/bin/gsl-config</code> (if found) to aid in the discovery of GSL.</p>
<h3>Cache Variables</h3>
<p>This module may set the following variables depending on platform and type of GSL installation discovered. These variables may optionally be set to help this module find the correct files: </p>
<pre>GSL_CBLAS_LIBRARY - Location of the GSL CBLAS library.
GSL_CBLAS_LIBRARY_DEBUG - Location of the debug GSL CBLAS library (if any).
GSL_CONFIG_EXECUTABLE - Location of the ``gsl-config`` script (if any).
GSL_LIBRARY - Location of the GSL library.
GSL_LIBRARY_DEBUG - Location of the debug GSL library (if any).</pre>
<h3>FindGTest</h3>
<p>Locate the Google C++ Testing Framework. </p>
<p> New in version 3.20: Upstream <code>GTestConfig.cmake</code> is used if possible.</p>
<h3>Imported targets</h3>
<p>New in version 3.20: This module defines the following <code>IMPORTED</code> targets: </p>
<dl>
<dt><code>GTest::gtest</code></p>
<dd>The Google Test <code>gtest</code> library, if found; adds Thread::Thread automatically</p>
<dt><code>GTest::gtest_main</code></p>
<dd>The Google Test <code>gtest_main</code> library, if found </p>
<p> New in version 3.23. </p>
<dt><code>GTest::gmock</code></p>
<dd>The Google Mock <code>gmock</code> library, if found; adds Thread::Thread automatically</p>
<dt><code>GTest::gmock_main</code></p>
<dd>The Google Mock <code>gmock_main</code> library, if found </p>
<p> Deprecated since version 3.20: For backwards compatibility, this module defines additionally the following deprecated <code>IMPORTED</code> targets (available since 3.5): </p>
<dt><code>GTest::GTest</code></p>
<dd>The Google Test <code>gtest</code> library, if found; adds Thread::Thread automatically</p>
<dt><code>GTest::Main</code></p>
<dd>The Google Test <code>gtest_main</code> library, if found</dl>
<h3>Result variables</h3>
<p>This module will set the following variables in your project:</p>
<dl>
<dt><code>GTest_FOUND</code></p>
<dd>Found the Google Testing framework</p>
<dt><code>GTEST_INCLUDE_DIRS</code></p>
<dd>the directory containing the Google Test headers </p>
<p> The library variables below are set as normal variables. These contain debug/optimized keywords when a debugging library is found.</p>
<dt><code>GTEST_LIBRARIES</code></p>
<dd>The Google Test <code>gtest</code> library; note it also requires linking with an appropriate thread library</p>
<dt><code>GTEST_MAIN_LIBRARIES</code></p>
<dd>The Google Test <code>gtest_main</code> library</p>
<dt><code>GTEST_BOTH_LIBRARIES</code></p>
<dd>Both <code>gtest</code> and <code>gtest_main</code></dl>
<h3>Cache variables</h3>
<p>The following cache variables may also be set:</p>
<dl>
<dt><code>GTEST_ROOT</code></p>
<dd>The root directory of the Google Test installation (may also be set as an environment variable)</p>
<dt><code>GTEST_MSVC_SEARCH</code></p>
<dd>If compiling with MSVC, this variable can be set to <code>MT</code> or <code>MD</code> (the default) to enable searching a GTest build tree</dl>
<h3>Example usage</h3>
<pre>enable_testing()
find_package(GTest REQUIRED)
add_executable(foo foo.cc)
target_link_libraries(foo GTest::gtest GTest::gtest_main)
add_test(AllTestsInFoo foo)</pre>
<h3>Deeper integration with CTest</h3>
<p>See <code>GoogleTest</code> for information on the <code>gtest_add_tests()</code> and <code>gtest_discover_tests()</code> commands. </p>
<p> Changed in version 3.9: Previous CMake versions defined <code>gtest_add_tests()</code> macro in this module.</p>
<h3>FindGTK</h3>
<p>Find GTK, glib and GTKGLArea </p>
<pre>GTK_INCLUDE_DIR - Directories to include to use GTK
GTK_LIBRARIES - Files to link against to use GTK
GTK_FOUND - GTK was found
GTK_GL_FOUND - GTK's GL features were found</pre>
<h3>FindGTK2</h3>
<p>Find the GTK2 widget libraries and several of its other optional components like <code>gtkmm</code>, <code>glade</code>, and <code>glademm</code>. </p>
<p> Specify one or more of the following components as you call this find module. See example below.</p>
<dl>
<dt>&bull;</p>
<dd><code>gtk</code></p>
<dt>&bull;</p>
<dd><code>gtkmm</code></p>
<dt>&bull;</p>
<dd><code>glade</code></p>
<dt>&bull;</p>
<dd><code>glademm</code></dl>
<h3>Imported Targets</h3>
<p>This module defines the following <code>IMPORTED</code> targets (subject to component selection): </p>
<p> <code>GTK2::atk</code>, <code>GTK2::atkmm</code>, <code>GTK2::cairo</code>, <code>GTK2::cairomm</code>, <code>GTK2::gdk_pixbuf</code>, <code>GTK2::gdk</code>, <code>GTK2::gdkmm</code>, <code>GTK2::gio</code>, <code>GTK2::giomm</code>, <code>GTK2::glade</code>, <code>GTK2::glademm</code>, <code>GTK2::glib</code>, <code>GTK2::glibmm</code>, <code>GTK2::gmodule</code>, <code>GTK2::gobject</code>, <code>GTK2::gthread</code>, <code>GTK2::gtk</code>, <code>GTK2::gtkmm</code>, <code>GTK2::harfbuzz</code>, <code>GTK2::pango</code>, <code>GTK2::pangocairo</code>, <code>GTK2::pangoft2</code>, <code>GTK2::pangomm</code>, <code>GTK2::pangoxft</code>, <code>GTK2::sigc</code>. </p>
<p> New in version 3.16.7: Added the <code>GTK2::harfbuzz</code> target.</p>
<h3>Result Variables</h3>
<p>The following variables will be defined for your use</p>
<dl>
<dt><code>GTK2_FOUND</code></p>
<dd>Were all of your specified components found?</p>
<dt><code>GTK2_INCLUDE_DIRS</code></p>
<dd>All include directories</p>
<dt><code>GTK2_LIBRARIES</code></p>
<dd>All libraries</p>
<dt><code>GTK2_TARGETS</code></p>
<dd>New in version 3.5: All imported targets </p>
<dt><code>GTK2_DEFINITIONS</code></p>
<dd>Additional compiler flags</p>
<dt><code>GTK2_VERSION</code></p>
<dd>The version of GTK2 found (x.y.z)</p>
<dt><code>GTK2_MAJOR_VERSION</code></p>
<dd>The major version of GTK2</p>
<dt><code>GTK2_MINOR_VERSION</code></p>
<dd>The minor version of GTK2</p>
<dt><code>GTK2_PATCH_VERSION</code></p>
<dd>The patch version of GTK2 </p>
<p> New in version 3.5: When <code>GTK2_USE_IMPORTED_TARGETS</code> is set to <code>TRUE</code>, <code>GTK2_LIBRARIES</code> will list imported targets instead of library paths. </p>
</dl>
<h3>Input Variables</h3>
<p>Optional variables you can define prior to calling this module:</p>
<dl>
<dt><code>GTK2_DEBUG</code></p>
<dd>Enables verbose debugging of the module</p>
<dt><code>GTK2_ADDITIONAL_SUFFIXES</code></p>
<dd>Allows defining additional directories to search for include files</dl>
<h3>Example Usage</h3>
<p>Call <code>find_package()</code> once. Here are some examples to pick from: </p>
<p> Require GTK 2.6 or later: </p>
<pre>find_package(GTK2 2.6 REQUIRED gtk)</pre>
<p>Require GTK 2.10 or later and Glade: </p>
<pre>find_package(GTK2 2.10 REQUIRED gtk glade)</pre>
<p>Search for GTK/GTKMM 2.8 or later: </p>
<pre>find_package(GTK2 2.8 COMPONENTS gtk gtkmm)</pre>
<p>Use the results: </p>
<pre>if(GTK2_FOUND)
 include_directories(${GTK2_INCLUDE_DIRS})
 add_executable(mygui mygui.cc)
 target_link_libraries(mygui ${GTK2_LIBRARIES})
endif()</pre>
<h3>FindHDF5</h3>
<p>Find Hierarchical Data Format (HDF5), a library for reading and writing self describing array data. </p>
<p> This module invokes the <code>HDF5</code> wrapper compiler that should be installed alongside <code>HDF5</code>. Depending upon the <code>HDF5</code> Configuration, the wrapper compiler is called either <code>h5cc</code> or <code>h5pcc</code>. If this succeeds, the module will then call the compiler with the show argument to see what flags are used when compiling an <code>HDF5</code> client application. </p>
<p> The module will optionally accept the <code>COMPONENTS</code> argument. If no <code>COMPONENTS</code> are specified, then the find module will default to finding only the <code>HDF5</code> C library. If one or more <code>COMPONENTS</code> are specified, the module will attempt to find the language bindings for the specified components. The valid components are <code>C</code>, <code>CXX</code>, <code>Fortran</code>, <code>HL</code>. <code>HL</code> refers to the &quot;high-level&quot; HDF5 functions for C and Fortran. If the <code>COMPONENTS</code> argument is not given, the module will attempt to find only the C bindings. For example, to use Fortran HDF5 and HDF5-HL functions, do: <code>find_package(HDF5 COMPONENTS Fortran HL)</code>. </p>
<p> This module will read the variable <code>HDF5_USE_STATIC_LIBRARIES</code> to determine whether or not to prefer a static link to a dynamic link for <code>HDF5</code> and all of it&#8217;s dependencies. To use this feature, make sure that the <code>HDF5_USE_STATIC_LIBRARIES</code> variable is set before the call to find_package. </p>
<p> New in version 3.10: Support for <code>HDF5_USE_STATIC_LIBRARIES</code> on Windows. </p>
<p> Both the serial and parallel <code>HDF5</code> wrappers are considered and the first directory to contain either one will be used. In the event that both appear in the same directory the serial version is preferentially selected. This behavior can be reversed by setting the variable <code>HDF5_PREFER_PARALLEL</code> to <code>TRUE</code>. </p>
<p> In addition to finding the includes and libraries required to compile an <code>HDF5</code> client application, this module also makes an effort to find tools that come with the <code>HDF5</code> distribution that may be useful for regression testing.</p>
<h3>Result Variables</h3>
<p>This module will set the following variables in your project:</p>
<dl>
<dt><code>HDF5_FOUND</code></p>
<dd>HDF5 was found on the system</p>
<dt><code>HDF5_VERSION</code></p>
<dd>New in version 3.3: HDF5 library version </p>
<dt><code>HDF5_INCLUDE_DIRS</code></p>
<dd>Location of the HDF5 header files</p>
<dt><code>HDF5_DEFINITIONS</code></p>
<dd>Required compiler definitions for HDF5</p>
<dt><code>HDF5_LIBRARIES</code></p>
<dd>Required libraries for all requested bindings</p>
<dt><code>HDF5_HL_LIBRARIES</code></p>
<dd>Required libraries for the HDF5 high level API for all bindings, if the <code>HL</code> component is enabled </p>
<p> Available components are: <code>C</code> <code>CXX</code> <code>Fortran</code> and <code>HL</code>. For each enabled language binding, a corresponding <code>HDF5_${LANG}_LIBRARIES</code> variable, and potentially <code>HDF5_${LANG}_DEFINITIONS</code>, will be defined. If the <code>HL</code> component is enabled, then an <code>HDF5_${LANG}_HL_LIBRARIES</code> will also be defined. With all components enabled, the following variables will be defined:</p>
<dt><code>HDF5_C_DEFINITIONS</code></p>
<dd>Required compiler definitions for HDF5 C bindings</p>
<dt><code>HDF5_CXX_DEFINITIONS</code></p>
<dd>Required compiler definitions for HDF5 C++ bindings</p>
<dt><code>HDF5_Fortran_DEFINITIONS</code></p>
<dd>Required compiler definitions for HDF5 Fortran bindings</p>
<dt><code>HDF5_C_INCLUDE_DIRS</code></p>
<dd>Required include directories for HDF5 C bindings</p>
<dt><code>HDF5_CXX_INCLUDE_DIRS</code></p>
<dd>Required include directories for HDF5 C++ bindings</p>
<dt><code>HDF5_Fortran_INCLUDE_DIRS</code></p>
<dd>Required include directories for HDF5 Fortran bindings</p>
<dt><code>HDF5_C_LIBRARIES</code></p>
<dd>Required libraries for the HDF5 C bindings</p>
<dt><code>HDF5_CXX_LIBRARIES</code></p>
<dd>Required libraries for the HDF5 C++ bindings</p>
<dt><code>HDF5_Fortran_LIBRARIES</code></p>
<dd>Required libraries for the HDF5 Fortran bindings</p>
<dt><code>HDF5_C_HL_LIBRARIES</code></p>
<dd>Required libraries for the high level C bindings</p>
<dt><code>HDF5_CXX_HL_LIBRARIES</code></p>
<dd>Required libraries for the high level C++ bindings</p>
<dt><code>HDF5_Fortran_HL_LIBRARIES</code></p>
<dd>Required libraries for the high level Fortran bindings.</p>
<dt><code>HDF5_IS_PARALLEL</code></p>
<dd>HDF5 library has parallel IO support</p>
<dt><code>HDF5_C_COMPILER_EXECUTABLE</code></p>
<dd>path to the HDF5 C wrapper compiler</p>
<dt><code>HDF5_CXX_COMPILER_EXECUTABLE</code></p>
<dd>path to the HDF5 C++ wrapper compiler</p>
<dt><code>HDF5_Fortran_COMPILER_EXECUTABLE</code></p>
<dd>path to the HDF5 Fortran wrapper compiler</p>
<dt><code>HDF5_C_COMPILER_EXECUTABLE_NO_INTERROGATE</code></p>
<dd>path to the primary C compiler which is also the HDF5 wrapper</p>
<dt><code>HDF5_CXX_COMPILER_EXECUTABLE_NO_INTERROGATE</code></p>
<dd>path to the primary C++ compiler which is also the HDF5 wrapper</p>
<dt><code>HDF5_Fortran_COMPILER_EXECUTABLE_NO_INTERROGATE</code></p>
<dd>path to the primary Fortran compiler which is also the HDF5 wrapper</p>
<dt><code>HDF5_DIFF_EXECUTABLE</code></p>
<dd>path to the HDF5 dataset comparison tool </p>
<p> With all components enabled, the following targets will be defined:</p>
<dt><code>HDF5::HDF5</code></p>
<dd>All detected <code>HDF5_LIBRARIES</code>.</p>
<dt><code>hdf5::hdf5</code></p>
<dd>C library.</p>
<dt><code>hdf5::hdf5_cpp</code></p>
<dd>C++ library.</p>
<dt><code>hdf5::hdf5_fortran</code></p>
<dd>Fortran library.</p>
<dt><code>hdf5::hdf5_hl</code></p>
<dd>High-level C library.</p>
<dt><code>hdf5::hdf5_hl_cpp</code></p>
<dd>High-level C++ library.</p>
<dt><code>hdf5::hdf5_hl_fortran</code></p>
<dd>High-level Fortran library.</p>
<dt><code>hdf5::h5diff</code></p>
<dd><code>h5diff</code> executable.</dl>
<h3>Hints</h3>
<p>The following variables can be set to guide the search for HDF5 libraries and includes:</p>
<dl>
<dt><code>HDF5_PREFER_PARALLEL</code></p>
<dd>New in version 3.4. </p>
<p> set <code>true</code> to prefer parallel HDF5 (by default, serial is preferred)</p>
<dt><code>HDF5_FIND_DEBUG</code></p>
<dd>New in version 3.9. </p>
<p> Set <code>true</code> to get extra debugging output.</p>
<dt><code>HDF5_NO_FIND_PACKAGE_CONFIG_FILE</code></p>
<dd>New in version 3.8. </p>
<p> Set <code>true</code> to skip trying to find <code>hdf5-config.cmake</code>.</dl>
<h3>FindHg</h3>
<p>Extract information from a mercurial working copy. </p>
<p> The module defines the following variables: </p>
<pre>HG_EXECUTABLE - path to mercurial command line client (hg)
HG_FOUND - true if the command line client was found
HG_VERSION_STRING - the version of mercurial found</pre>
<p>New in version 3.1: If the command line client executable is found the following macro is defined: </p>
<pre>HG_WC_INFO(&lt;dir&gt; &lt;var-prefix&gt;)</pre>
<p>Hg_WC_INFO extracts information of a mercurial working copy at a given location. This macro defines the following variables: </p>
<pre>&lt;var-prefix&gt;_WC_CHANGESET - current changeset
&lt;var-prefix&gt;_WC_REVISION - current revision</pre>
<p>Example usage: </p>
<pre>find_package(Hg)
if(HG_FOUND)
 message(&quot;hg found: ${HG_EXECUTABLE}&quot;)
 HG_WC_INFO(${PROJECT_SOURCE_DIR} Project)
 message(&quot;Current revision is ${Project_WC_REVISION}&quot;)
 message(&quot;Current changeset is ${Project_WC_CHANGESET}&quot;)
endif()</pre>
<h3>FindHSPELL</h3>
<p>Try to find Hebrew spell-checker (Hspell) and morphology engine. </p>
<p> Once done this will define </p>
<pre>HSPELL_FOUND - system has Hspell
HSPELL_INCLUDE_DIR - the Hspell include directory
HSPELL_LIBRARIES - The libraries needed to use Hspell
HSPELL_DEFINITIONS - Compiler switches required for using Hspell</pre>
<pre>HSPELL_VERSION_STRING - The version of Hspell found (x.y)
HSPELL_MAJOR_VERSION - the major version of Hspell
HSPELL_MINOR_VERSION - The minor version of Hspell</pre>
<h3>FindHTMLHelp</h3>
<p>This module looks for Microsoft HTML Help Compiler </p>
<p> It defines: </p>
<pre>HTML_HELP_COMPILER : full path to the Compiler (hhc.exe)
HTML_HELP_INCLUDE_PATH : include path to the API (htmlhelp.h)
HTML_HELP_LIBRARY : full path to the library (htmlhelp.lib)</pre>
<h3>FindIce</h3>
<p>New in version 3.1. </p>
<p> Find the ZeroC Internet Communication Engine (ICE) programs, libraries and datafiles. </p>
<p> This module supports multiple components. Components can include any of: <code>Freeze</code>, <code>Glacier2</code>, <code>Ice</code>, <code>IceBox</code>, <code>IceDB</code>, <code>IceDiscovery</code>, <code>IceGrid</code>, <code>IceLocatorDiscovery</code>, <code>IcePatch</code>, <code>IceSSL</code>, <code>IceStorm</code>, <code>IceUtil</code>, <code>IceXML</code>, or <code>Slice</code>. </p>
<p> Ice 3.7 and later also include C++11-specific components: <code>Glacier2++11</code>, <code>Ice++11</code>, <code>IceBox++11</code>, <code>IceDiscovery++11</code> <code>IceGrid</code>, <code>IceLocatorDiscovery++11</code>, <code>IceSSL++11</code>, <code>IceStorm++11</code> </p>
<p> Note that the set of supported components is Ice version-specific. </p>
<p> New in version 3.4: Imported targets for components and most <code>EXECUTABLE</code> variables. </p>
<p> New in version 3.7: Debug and Release variants are found separately. </p>
<p> New in version 3.10: Ice 3.7 support, including new components, programs and the Nuget package. </p>
<p> This module reports information about the Ice installation in several variables. General variables: </p>
<pre>Ice_VERSION - Ice release version
Ice_FOUND - true if the main programs and libraries were found
Ice_LIBRARIES - component libraries to be linked
Ice_INCLUDE_DIRS - the directories containing the Ice headers
Ice_SLICE_DIRS - the directories containing the Ice slice interface
 definitions</pre>
<p>Imported targets: </p>
<pre>Ice::&lt;C&gt;</pre>
<p>Where <code>&lt;C&gt;</code> is the name of an Ice component, for example <code>Ice::Glacier2</code> or <code>Ice++11</code>. </p>
<p> Ice slice programs are reported in: </p>
<pre>Ice_SLICE2CONFLUENCE_EXECUTABLE - path to slice2confluence executable
Ice_SLICE2CPP_EXECUTABLE - path to slice2cpp executable
Ice_SLICE2CS_EXECUTABLE - path to slice2cs executable
Ice_SLICE2FREEZEJ_EXECUTABLE - path to slice2freezej executable
Ice_SLICE2FREEZE_EXECUTABLE - path to slice2freeze executable
Ice_SLICE2HTML_EXECUTABLE - path to slice2html executable
Ice_SLICE2JAVA_EXECUTABLE - path to slice2java executable
Ice_SLICE2JS_EXECUTABLE - path to slice2js executable
Ice_SLICE2MATLAB_EXECUTABLE - path to slice2matlab executable
Ice_SLICE2OBJC_EXECUTABLE - path to slice2objc executable
Ice_SLICE2PHP_EXECUTABLE - path to slice2php executable
Ice_SLICE2PY_EXECUTABLE - path to slice2py executable
Ice_SLICE2RB_EXECUTABLE - path to slice2rb executable</pre>
<p>New in version 3.14: Variables for <code>slice2confluence</code> and <code>slice2matlab</code>. </p>
<p> Ice programs are reported in: </p>
<pre>Ice_GLACIER2ROUTER_EXECUTABLE - path to glacier2router executable
Ice_ICEBOX_EXECUTABLE - path to icebox executable
Ice_ICEBOXXX11_EXECUTABLE - path to icebox++11 executable
Ice_ICEBOXADMIN_EXECUTABLE - path to iceboxadmin executable
Ice_ICEBOXD_EXECUTABLE - path to iceboxd executable
Ice_ICEBOXNET_EXECUTABLE - path to iceboxnet executable
Ice_ICEBRIDGE_EXECUTABLE - path to icebridge executable
Ice_ICEGRIDADMIN_EXECUTABLE - path to icegridadmin executable
Ice_ICEGRIDDB_EXECUTABLE - path to icegriddb executable
Ice_ICEGRIDNODE_EXECUTABLE - path to icegridnode executable
Ice_ICEGRIDNODED_EXECUTABLE - path to icegridnoded executable
Ice_ICEGRIDREGISTRY_EXECUTABLE - path to icegridregistry executable
Ice_ICEGRIDREGISTRYD_EXECUTABLE - path to icegridregistryd executable
Ice_ICEPATCH2CALC_EXECUTABLE - path to icepatch2calc executable
Ice_ICEPATCH2CLIENT_EXECUTABLE - path to icepatch2client executable
Ice_ICEPATCH2SERVER_EXECUTABLE - path to icepatch2server executable
Ice_ICESERVICEINSTALL_EXECUTABLE - path to iceserviceinstall executable
Ice_ICESTORMADMIN_EXECUTABLE - path to icestormadmin executable
Ice_ICESTORMDB_EXECUTABLE - path to icestormdb executable
Ice_ICESTORMMIGRATE_EXECUTABLE - path to icestormmigrate executable</pre>
<p>Ice db programs (Windows only; standard system versions on all other platforms) are reported in: </p>
<pre>Ice_DB_ARCHIVE_EXECUTABLE - path to db_archive executable
Ice_DB_CHECKPOINT_EXECUTABLE - path to db_checkpoint executable
Ice_DB_DEADLOCK_EXECUTABLE - path to db_deadlock executable
Ice_DB_DUMP_EXECUTABLE - path to db_dump executable
Ice_DB_HOTBACKUP_EXECUTABLE - path to db_hotbackup executable
Ice_DB_LOAD_EXECUTABLE - path to db_load executable
Ice_DB_LOG_VERIFY_EXECUTABLE - path to db_log_verify executable
Ice_DB_PRINTLOG_EXECUTABLE - path to db_printlog executable
Ice_DB_RECOVER_EXECUTABLE - path to db_recover executable
Ice_DB_STAT_EXECUTABLE - path to db_stat executable
Ice_DB_TUNER_EXECUTABLE - path to db_tuner executable
Ice_DB_UPGRADE_EXECUTABLE - path to db_upgrade executable
Ice_DB_VERIFY_EXECUTABLE - path to db_verify executable
Ice_DUMPDB_EXECUTABLE - path to dumpdb executable
Ice_TRANSFORMDB_EXECUTABLE - path to transformdb executable</pre>
<p>Ice component libraries are reported in: </p>
<pre>Ice_&lt;C&gt;_FOUND - ON if component was found
Ice_&lt;C&gt;_LIBRARIES - libraries for component</pre>
<p>Note that <code>&lt;C&gt;</code> is the uppercased name of the component. </p>
<p> This module reads hints about search results from: </p>
<pre>Ice_HOME - the root of the Ice installation</pre>
<p>The environment variable <code>ICE_HOME</code> may also be used; the Ice_HOME variable takes precedence. </p>
<p> <code>NOTE:</code> On Windows, Ice 3.7.0 and later provide libraries via the NuGet package manager. Appropriate NuGet packages will be searched for using <code>CMAKE_PREFIX_PATH</code>, or alternatively <code>Ice_HOME</code> may be set to the location of a specific NuGet package to restrict the search. </p>
<p> The following cache variables may also be set: </p>
<pre>Ice_&lt;P&gt;_EXECUTABLE - the path to executable &lt;P&gt;
Ice_INCLUDE_DIR - the directory containing the Ice headers
Ice_SLICE_DIR - the directory containing the Ice slice interface
 definitions
Ice_&lt;C&gt;_LIBRARY - the library for component &lt;C&gt;</pre>
<p><code>NOTE:</code> In most cases none of the above variables will require setting, unless multiple Ice versions are available and a specific version is required. On Windows, the most recent version of Ice will be found through the registry. On Unix, the programs, headers and libraries will usually be in standard locations, but Ice_SLICE_DIRS might not be automatically detected (commonly known locations are searched). All the other variables are defaulted using Ice_HOME, if set. It&#8217;s possible to set Ice_HOME and selectively specify alternative locations for the other components; this might be required for e.g. newer versions of Visual Studio if the heuristics are not sufficient to identify the correct programs and libraries for the specific Visual Studio version. </p>
<p> Other variables one may set to control this module are: </p>
<pre>Ice_DEBUG - Set to ON to enable debug output from FindIce.</pre>
<h3>FindIconv</h3>
<p>New in version 3.11. </p>
<p> This module finds the <code>iconv()</code> POSIX.1 functions on the system. These functions might be provided in the regular C library or externally in the form of an additional library. </p>
<p> The following variables are provided to indicate iconv support:</p>
<dl>
<dt><code>Iconv_FOUND</code></p>
<dd>Variable indicating if the iconv support was found.</p>
<dt><code>Iconv_INCLUDE_DIRS</code></p>
<dd>The directories containing the iconv headers.</p>
<dt><code>Iconv_LIBRARIES</code></p>
<dd>The iconv libraries to be linked.</p>
<dt><code>Iconv_VERSION</code></p>
<dd>New in version 3.21. </p>
<p> The version of iconv found (x.y)</p>
<dt><code>Iconv_VERSION_MAJOR</code></p>
<dd>New in version 3.21. </p>
<p> The major version of iconv</p>
<dt><code>Iconv_VERSION_MINOR</code></p>
<dd>New in version 3.21. </p>
<p> The minor version of iconv</p>
<dt><code>Iconv_IS_BUILT_IN</code></p>
<dd>A variable indicating whether iconv support is stemming from the C library or not. Even if the C library provides <i>iconv()</i>, the presence of an external <i>libiconv</i> implementation might lead to this being false. </p>
<p> Additionally, the following <code>IMPORTED</code> target is being provided:</p>
<dt><code>Iconv::Iconv</code></p>
<dd>Imported target for using iconv. </p>
<p> The following cache variables may also be set:</p>
<dt><code>Iconv_INCLUDE_DIR</code></p>
<dd>The directory containing the iconv headers.</p>
<dt><code>Iconv_LIBRARY</code></p>
<dd>The iconv library (if not implicitly given in the C library). </p>
<p> <code>NOTE:</code> On POSIX platforms, iconv might be part of the C library and the cache variables <code>Iconv_INCLUDE_DIR</code> and <code>Iconv_LIBRARY</code> might be empty. </p>
<p> <code>NOTE:</code> Some libiconv implementations don&#8217;t embed the version number in their header files. In this case the variables <code>Iconv_VERSION*</code> will be empty.</dl>
<h3>FindIcotool</h3>
<p>Find icotool </p>
<p> This module looks for icotool. Convert and create Win32 icon and cursor files. This module defines the following values: </p>
<pre>ICOTOOL_EXECUTABLE: the full path to the icotool tool.
ICOTOOL_FOUND: True if icotool has been found.
ICOTOOL_VERSION_STRING: the version of icotool found.</pre>
<h3>FindICU</h3>
<p>New in version 3.7. </p>
<p> Find the International Components for Unicode (ICU) libraries and programs. </p>
<p> This module supports multiple components. Components can include any of: <code>data</code>, <code>i18n</code>, <code>io</code>, <code>le</code>, <code>lx</code>, <code>test</code>, <code>tu</code> and <code>uc</code>. </p>
<p> Note that on Windows <code>data</code> is named <code>dt</code> and <code>i18n</code> is named <code>in</code>; any of the names may be used, and the appropriate platform-specific library name will be automatically selected. </p>
<p> New in version 3.11: Added support for static libraries on Windows. </p>
<p> This module reports information about the ICU installation in several variables. General variables: </p>
<pre>ICU_VERSION - ICU release version
ICU_FOUND - true if the main programs and libraries were found
ICU_LIBRARIES - component libraries to be linked
ICU_INCLUDE_DIRS - the directories containing the ICU headers</pre>
<p>Imported targets: </p>
<pre>ICU::&lt;C&gt;</pre>
<p>Where <code>&lt;C&gt;</code> is the name of an ICU component, for example <code>ICU::i18n</code>; <code>&lt;C&gt;</code> is lower-case. </p>
<p> ICU programs are reported in: </p>
<pre>ICU_GENCNVAL_EXECUTABLE - path to gencnval executable
ICU_ICUINFO_EXECUTABLE - path to icuinfo executable
ICU_GENBRK_EXECUTABLE - path to genbrk executable
ICU_ICU-CONFIG_EXECUTABLE - path to icu-config executable
ICU_GENRB_EXECUTABLE - path to genrb executable
ICU_GENDICT_EXECUTABLE - path to gendict executable
ICU_DERB_EXECUTABLE - path to derb executable
ICU_PKGDATA_EXECUTABLE - path to pkgdata executable
ICU_UCONV_EXECUTABLE - path to uconv executable
ICU_GENCFU_EXECUTABLE - path to gencfu executable
ICU_MAKECONV_EXECUTABLE - path to makeconv executable
ICU_GENNORM2_EXECUTABLE - path to gennorm2 executable
ICU_GENCCODE_EXECUTABLE - path to genccode executable
ICU_GENSPREP_EXECUTABLE - path to gensprep executable
ICU_ICUPKG_EXECUTABLE - path to icupkg executable
ICU_GENCMN_EXECUTABLE - path to gencmn executable</pre>
<p>ICU component libraries are reported in: </p>
<pre>ICU_&lt;C&gt;_FOUND - ON if component was found; ``&lt;C&gt;`` is upper-case.
ICU_&lt;C&gt;_LIBRARIES - libraries for component; ``&lt;C&gt;`` is upper-case.</pre>
<p>ICU datafiles are reported in: </p>
<pre>ICU_MAKEFILE_INC - Makefile.inc
ICU_PKGDATA_INC - pkgdata.inc</pre>
<p>This module reads hints about search results from: </p>
<pre>ICU_ROOT - the root of the ICU installation</pre>
<p>The environment variable <code>ICU_ROOT</code> may also be used; the ICU_ROOT variable takes precedence. </p>
<p> The following cache variables may also be set: </p>
<pre>ICU_&lt;P&gt;_EXECUTABLE - the path to executable &lt;P&gt;; ``&lt;P&gt;`` is upper-case.
ICU_INCLUDE_DIR - the directory containing the ICU headers
ICU_&lt;C&gt;_LIBRARY - the library for component &lt;C&gt;; ``&lt;C&gt;`` is upper-case.</pre>
<p><code>NOTE:</code> In most cases none of the above variables will require setting, unless multiple ICU versions are available and a specific version is required. </p>
<p> Other variables one may set to control this module are: </p>
<pre>ICU_DEBUG - Set to ON to enable debug output from FindICU.</pre>
<h3>FindImageMagick</h3>
<p>Find ImageMagick binary suite. </p>
<p> New in version 3.9: Added support for ImageMagick 7. </p>
<p> This module will search for a set of ImageMagick tools specified as components in the <code>find_package()</code> call. Typical components include, but are not limited to (future versions of ImageMagick might have additional components not listed here): </p>
<pre>animate
compare
composite
conjure
convert
display
identify
import
mogrify
montage
stream</pre>
<p>If no component is specified in the <code>find_package()</code> call, then it only searches for the ImageMagick executable directory. This code defines the following variables: </p>
<pre>ImageMagick_FOUND - TRUE if all components are found.
ImageMagick_EXECUTABLE_DIR - Full path to executables directory.
ImageMagick_&lt;component&gt;_FOUND - TRUE if &lt;component&gt; is found.
ImageMagick_&lt;component&gt;_EXECUTABLE - Full path to &lt;component&gt; executable.
ImageMagick_VERSION_STRING - the version of ImageMagick found
 (since CMake 2.8.8)</pre>
<p><code>ImageMagick_VERSION_STRING</code> will not work for old versions like 5.2.3. </p>
<p> There are also components for the following ImageMagick APIs: </p>
<pre>Magick++
MagickWand
MagickCore</pre>
<p>For these components the following variables are set: </p>
<pre>ImageMagick_FOUND - TRUE if all components are found.
ImageMagick_INCLUDE_DIRS - Full paths to all include dirs.
ImageMagick_LIBRARIES - Full paths to all libraries.
ImageMagick_&lt;component&gt;_FOUND - TRUE if &lt;component&gt; is found.
ImageMagick_&lt;component&gt;_INCLUDE_DIRS - Full path to &lt;component&gt; include dirs.
ImageMagick_&lt;component&gt;_LIBRARIES - Full path to &lt;component&gt; libraries.</pre>
<p>Example Usages: </p>
<pre>find_package(ImageMagick)
find_package(ImageMagick COMPONENTS convert)
find_package(ImageMagick COMPONENTS convert mogrify display)
find_package(ImageMagick COMPONENTS Magick++)
find_package(ImageMagick COMPONENTS Magick++ convert)</pre>
<p>Note that the standard <code>find_package()</code> features are supported (i.e., <code>QUIET</code>, <code>REQUIRED</code>, etc.).</p>
<h3>FindIntl</h3>
<p>New in version 3.2. </p>
<p> Find the Gettext libintl headers and libraries. </p>
<p> This module reports information about the Gettext libintl installation in several variables.</p>
<dl>
<dt><code>Intl_FOUND</code></p>
<dd>True if libintl is found.</p>
<dt><code>Intl_INCLUDE_DIRS</code></p>
<dd>The directory containing the libintl headers.</p>
<dt><code>Intl_LIBRARIES</code></p>
<dd>The intl libraries to be linked.</p>
<dt><code>Intl_VERSION</code></p>
<dd>New in version 3.21. </p>
<p> The version of intl found (x.y.z)</p>
<dt><code>Intl_VERSION_MAJOR</code></p>
<dd>New in version 3.21. </p>
<p> The major version of intl</p>
<dt><code>Intl_VERSION_MINOR</code></p>
<dd>New in version 3.21. </p>
<p> The minor version of intl</p>
<dt><code>Intl_VERSION_PATCH</code></p>
<dd>New in version 3.21. </p>
<p> The patch version of intl </p>
<p> New in version 3.20: This module defines <code>IMPORTED</code> target <code>Intl::Intl</code>. </p>
<p> The following cache variables may also be set:</p>
<dt><code>Intl_INCLUDE_DIR</code></p>
<dd>The directory containing the libintl headers</p>
<dt><code>Intl_LIBRARY</code></p>
<dd>The libintl library (if any)</p>
<dt><code>Intl_IS_BUILT_IN</code></p>
<dd>New in version 3.20. </p>
<p> whether <code>intl</code> is a part of the C library. </p>
<p> <code>NOTE:</code> On some platforms, such as Linux with GNU libc, the gettext functions are present in the C standard library and libintl is not required. <code>Intl_LIBRARIES</code> will be empty in this case. </p>
<p> <code>NOTE:</code> Some libintl implementations don&#8217;t embed the version number in their header files. In this case the variables <code>Intl_VERSION*</code> will be empty. </p>
<p> <code>NOTE:</code> If you wish to use the Gettext tools (<code>msgmerge</code>, <code>msgfmt</code>, etc.), use <code>FindGettext</code>.</dl>
<h3>FindITK</h3>
<p>This module no longer exists. </p>
<p> This module existed in versions of CMake prior to 3.1, but became only a thin wrapper around <code>find_package(ITK NO_MODULE)</code> to provide compatibility for projects using long-outdated conventions. Now <code>find_package(ITK)</code> will search for <code>ITKConfig.cmake</code> directly.</p>
<h3>FindJasper</h3>
<p>Find the Jasper JPEG2000 library.</p>
<h3>IMPORTED Targets</h3>
<dl>
<dt><code>Jasper::Jasper</code></p>
<dd>The jasper library, if found.</dl>
<h3>Result Variables</h3>
<p>This module defines the following variables:</p>
<dl>
<dt><code>JASPER_FOUND</code></p>
<dd>system has Jasper</p>
<dt><code>JASPER_INCLUDE_DIRS</code></p>
<dd>New in version 3.22. </p>
<p> the Jasper include directory</p>
<dt><code>JASPER_LIBRARIES</code></p>
<dd>the libraries needed to use Jasper</p>
<dt><code>JASPER_VERSION_STRING</code></p>
<dd>the version of Jasper found</dl>
<h3>Cache variables</h3>
<p>The following cache variables may also be set:</p>
<dl>
<dt><code>JASPER_INCLUDE_DIR</code></p>
<dd>where to find jasper/jasper.h, etc.</p>
<dt><code>JASPER_LIBRARY_RELEASE</code></p>
<dd>where to find the Jasper library (optimized).</p>
<dt><code>JASPER_LIBARRY_DEBUG</code></p>
<dd>where to find the Jasper library (debug).</dl>
<h3>FindJava</h3>
<p>Find Java </p>
<p> This module finds if Java is installed and determines where the include files and libraries are. The caller may set variable <code>JAVA_HOME</code> to specify a Java installation prefix explicitly. </p>
<p> See also the <code>FindJNI</code> module to find Java Native Interface (JNI). </p>
<p> New in version 3.10: Added support for Java 9+ version parsing. </p>
<p> Specify one or more of the following components as you call this find module. See example below. </p>
<pre>Runtime = Java Runtime Environment used to execute Java byte-compiled applications
Development = Development tools (java, javac, javah, jar and javadoc), includes Runtime component
IdlJ = Interface Description Language (IDL) to Java compiler
JarSigner = Signer and verifier tool for Java Archive (JAR) files</pre>
<p>This module sets the following result variables: </p>
<pre>Java_JAVA_EXECUTABLE = the full path to the Java runtime
Java_JAVAC_EXECUTABLE = the full path to the Java compiler
Java_JAVAH_EXECUTABLE = the full path to the Java header generator
Java_JAVADOC_EXECUTABLE = the full path to the Java documentation generator
Java_IDLJ_EXECUTABLE = the full path to the Java idl compiler
Java_JAR_EXECUTABLE = the full path to the Java archiver
Java_JARSIGNER_EXECUTABLE = the full path to the Java jar signer
Java_VERSION_STRING = Version of java found, eg. 1.6.0_12
Java_VERSION_MAJOR = The major version of the package found.
Java_VERSION_MINOR = The minor version of the package found.
Java_VERSION_PATCH = The patch version of the package found.
Java_VERSION_TWEAK = The tweak version of the package found (after '_')
Java_VERSION = This is set to: $major[.$minor[.$patch[.$tweak]]]</pre>
<p>New in version 3.4: Added the <code>Java_IDLJ_EXECUTABLE</code> and <code>Java_JARSIGNER_EXECUTABLE</code> variables. </p>
<p> The minimum required version of Java can be specified using the <code>find_package()</code> syntax, e.g. </p>
<pre>find_package(Java 1.8)</pre>
<p>NOTE: <code>${Java_VERSION}</code> and <code>${Java_VERSION_STRING}</code> are not guaranteed to be identical. For example some java version may return: <code>Java_VERSION_STRING = 1.8.0_17</code> and <code>Java_VERSION = 1.8.0.17</code> </p>
<p> another example is the Java OEM, with: <code>Java_VERSION_STRING = 1.8.0-oem</code> and <code>Java_VERSION = 1.8.0</code> </p>
<p> For these components the following variables are set: </p>
<pre>Java_FOUND - TRUE if all components are found.
Java_&lt;component&gt;_FOUND - TRUE if &lt;component&gt; is found.</pre>
<p>Example Usages: </p>
<pre>find_package(Java)
find_package(Java 1.8 REQUIRED)
find_package(Java COMPONENTS Runtime)
find_package(Java COMPONENTS Development)</pre>
<h3>FindJNI</h3>
<p>Find Java Native Interface (JNI) libraries. </p>
<p> JNI enables Java code running in a Java Virtual Machine (JVM) to call and be called by native applications and libraries written in other languages such as C, C++. </p>
<p> This module finds if Java is installed and determines where the include files and libraries are. It also determines what the name of the library is. The caller may set variable <code>JAVA_HOME</code> to specify a Java installation prefix explicitly.</p>
<h3>Result Variables</h3>
<p>This module sets the following result variables:</p>
<dl>
<dt><code>JNI_INCLUDE_DIRS</code></p>
<dd>the include dirs to use</p>
<dt><code>JNI_LIBRARIES</code></p>
<dd>the libraries to use (JAWT and JVM)</p>
<dt><code>JNI_FOUND</code></p>
<dd>TRUE if JNI headers and libraries were found.</dl>
<h3>Cache Variables</h3>
<p>The following cache variables are also available to set or use:</p>
<dl>
<dt><code>JAVA_AWT_LIBRARY</code></p>
<dd>the path to the Java AWT Native Interface (JAWT) library</p>
<dt><code>JAVA_JVM_LIBRARY</code></p>
<dd>the path to the Java Virtual Machine (JVM) library</p>
<dt><code>JAVA_INCLUDE_PATH</code></p>
<dd>the include path to jni.h</p>
<dt><code>JAVA_INCLUDE_PATH2</code></p>
<dd>the include path to jni_md.h and jniport.h</p>
<dt><code>JAVA_AWT_INCLUDE_PATH</code></p>
<dd>the include path to jawt.h</dl>
<h3>FindJPEG</h3>
<p>Find the Joint Photographic Experts Group (JPEG) library (<code>libjpeg</code>)</p>
<h3>Imported targets</h3>
<p>New in version 3.12. </p>
<p> This module defines the following <code>IMPORTED</code> targets:</p>
<dl>
<dt><code>JPEG::JPEG</code></p>
<dd>The JPEG library, if found.</dl>
<h3>Result variables</h3>
<p>This module will set the following variables in your project:</p>
<dl>
<dt><code>JPEG_FOUND</code></p>
<dd>If false, do not try to use JPEG.</p>
<dt><code>JPEG_INCLUDE_DIRS</code></p>
<dd>where to find jpeglib.h, etc.</p>
<dt><code>JPEG_LIBRARIES</code></p>
<dd>the libraries needed to use JPEG.</p>
<dt><code>JPEG_VERSION</code></p>
<dd>New in version 3.12: the version of the JPEG library found </p>
</dl>
<h3>Cache variables</h3>
<p>The following cache variables may also be set:</p>
<dl>
<dt><code>JPEG_INCLUDE_DIRS</code></p>
<dd>where to find jpeglib.h, etc.</p>
<dt><code>JPEG_LIBRARY_RELEASE</code></p>
<dd>where to find the JPEG library (optimized).</p>
<dt><code>JPEG_LIBRARY_DEBUG</code></p>
<dd>where to find the JPEG library (debug). </p>
<p> New in version 3.12: Debug and Release variand are found separately. </p>
</dl>
<h3>Obsolete variables</h3>
<dl>
<dt><code>JPEG_INCLUDE_DIR</code></p>
<dd>where to find jpeglib.h, etc. (same as JPEG_INCLUDE_DIRS)</p>
<dt><code>JPEG_LIBRARY</code></p>
<dd>where to find the JPEG library.</dl>
<h3>FindKDE3</h3>
<p>Find the KDE3 include and library dirs, KDE preprocessors and define a some macros </p>
<p> This module defines the following variables:</p>
<dl>
<dt><code>KDE3_DEFINITIONS</code></p>
<dd>compiler definitions required for compiling KDE software</p>
<dt><code>KDE3_INCLUDE_DIR</code></p>
<dd>the KDE include directory</p>
<dt><code>KDE3_INCLUDE_DIRS</code></p>
<dd>the KDE and the Qt include directory, for use with include_directories()</p>
<dt><code>KDE3_LIB_DIR</code></p>
<dd>the directory where the KDE libraries are installed, for use with link_directories()</p>
<dt><code>QT_AND_KDECORE_LIBS</code></p>
<dd>this contains both the Qt and the kdecore library</p>
<dt><code>KDE3_DCOPIDL_EXECUTABLE</code></p>
<dd>the dcopidl executable</p>
<dt><code>KDE3_DCOPIDL2CPP_EXECUTABLE</code></p>
<dd>the dcopidl2cpp executable</p>
<dt><code>KDE3_KCFGC_EXECUTABLE</code></p>
<dd>the kconfig_compiler executable</p>
<dt><code>KDE3_FOUND</code></p>
<dd>set to TRUE if all of the above has been found </p>
<p> The following user adjustable options are provided:</p>
<dt><code>KDE3_BUILD_TESTS</code></p>
<dd>enable this to build KDE testcases </p>
<p> It also adds the following macros (from <code>KDE3Macros.cmake</code>) <code>SRCS_VAR</code> is always the variable which contains the list of source files for your application or library. </p>
<p> KDE3_AUTOMOC(file1 &#8230; fileN) </p>
<pre>Call this if you want to have automatic moc file handling.
This means if you include &quot;foo.moc&quot; in the source file foo.cpp
a moc file for the header foo.h will be created automatically.
You can set the property SKIP_AUTOMAKE using set_source_files_properties()
to exclude some files in the list from being processed.</pre>
<p>KDE3_ADD_MOC_FILES(SRCS_VAR file1 &#8230; fileN ) </p>
<pre>If you don't use the KDE3_AUTOMOC() macro, for the files
listed here moc files will be created (named &quot;foo.moc.cpp&quot;)</pre>
<p>KDE3_ADD_DCOP_SKELS(SRCS_VAR header1.h &#8230; headerN.h ) </p>
<pre>Use this to generate DCOP skeletions from the listed headers.</pre>
<p>KDE3_ADD_DCOP_STUBS(SRCS_VAR header1.h &#8230; headerN.h ) </p>
<pre>Use this to generate DCOP stubs from the listed headers.</pre>
<p>KDE3_ADD_UI_FILES(SRCS_VAR file1.ui &#8230; fileN.ui ) </p>
<pre>Use this to add the Qt designer ui files to your application/library.</pre>
<p>KDE3_ADD_KCFG_FILES(SRCS_VAR file1.kcfgc &#8230; fileN.kcfgc ) </p>
<pre>Use this to add KDE kconfig compiler files to your application/library.</pre>
<p>KDE3_INSTALL_LIBTOOL_FILE(target) </p>
<pre>This will create and install a simple libtool file for the given target.</pre>
<p>KDE3_ADD_EXECUTABLE(name file1 &#8230; fileN ) </p>
<pre>Currently identical to add_executable(), may provide some advanced
features in the future.</pre>
<p>KDE3_ADD_KPART(name [WITH_PREFIX] file1 &#8230; fileN ) </p>
<pre>Create a KDE plugin (KPart, kioslave, etc.) from the given source files.
If WITH_PREFIX is given, the resulting plugin will have the prefix &quot;lib&quot;,
otherwise it won't.
It creates and installs an appropriate libtool la-file.</pre>
<p>KDE3_ADD_KDEINIT_EXECUTABLE(name file1 &#8230; fileN ) </p>
<pre>Create a KDE application in the form of a module loadable via kdeinit.
A library named kdeinit_&lt;name&gt; will be created and a small executable
which links to it.</pre>
<p>The option KDE3_ENABLE_FINAL to enable all-in-one compilation is no longer supported. </p>
<p> Author: Alexander Neundorf &lt;<i>neundorf [at] kde.org</i>&gt;</dl>
<h3>FindKDE4</h3>
<p>Find KDE4 and provide all necessary variables and macros to compile software for it. It looks for KDE 4 in the following directories in the given order: </p>
<pre>CMAKE_INSTALL_PREFIX
KDEDIRS
/opt/kde4</pre>
<p>Please look in <code>FindKDE4Internal.cmake</code> and <code>KDE4Macros.cmake</code> for more information. They are installed with the KDE 4 libraries in $KDEDIRS/share/apps/cmake/modules/. </p>
<p> Author: Alexander Neundorf &lt;<i>neundorf [at] kde.org</i>&gt;</p>
<h3>FindLAPACK</h3>
<p>Find Linear Algebra PACKage (LAPACK) library </p>
<p> This module finds an installed Fortran library that implements the <i>LAPACK linear-algebra interface</i>. </p>
<p> At least one of the <code>C</code>, <code>CXX</code>, or <code>Fortran</code> languages must be enabled.</p>
<h3>Input Variables</h3>
<p>The following variables may be set to influence this module&#8217;s behavior:</p>
<dl>
<dt><code>BLA_STATIC</code></p>
<dd>if <code>ON</code> use static linkage</p>
<dt><code>BLA_VENDOR</code></p>
<dd>Set to one of the BLAS/LAPACK Vendors to search for BLAS only from the specified vendor. If not set, all vendors are considered.</p>
<dt><code>BLA_F95</code></p>
<dd>if <code>ON</code> tries to find the BLAS95/LAPACK95 interfaces</p>
<dt><code>BLA_PREFER_PKGCONFIG</code></p>
<dd>New in version 3.20. </p>
<p> if set <code>pkg-config</code> will be used to search for a LAPACK library first and if one is found that is preferred</p>
<dt><code>BLA_SIZEOF_INTEGER</code></p>
<dd>New in version 3.22. </p>
<p> Specify the BLAS/LAPACK library integer size:</p>
<dt><code>4</code></p>
<dd>Search for a BLAS/LAPACK with 32-bit integer interfaces.</p>
<dt><code>8</code></p>
<dd>Search for a BLAS/LAPACK with 64-bit integer interfaces.</p>
<dt><code>ANY</code></p>
<dd>Search for any BLAS/LAPACK. Most likely, a BLAS/LAPACK with 32-bit integer interfaces will be found.</dl>
<h3>Imported targets</h3>
<p>This module defines the following <code>IMPORTED</code> targets:</p>
<dl>
<dt><code>LAPACK::LAPACK</code></p>
<dd>New in version 3.18. </p>
<p> The libraries to use for LAPACK, if found.</dl>
<h3>Result Variables</h3>
<p>This module defines the following variables:</p>
<dl>
<dt><code>LAPACK_FOUND</code></p>
<dd>library implementing the LAPACK interface is found</p>
<dt><code>LAPACK_LINKER_FLAGS</code></p>
<dd>uncached list of required linker flags (excluding <code>-l</code> and <code>-L</code>).</p>
<dt><code>LAPACK_LIBRARIES</code></p>
<dd>uncached list of libraries (using full path name) to link against to use LAPACK</p>
<dt><code>LAPACK95_LIBRARIES</code></p>
<dd>uncached list of libraries (using full path name) to link against to use LAPACK95</p>
<dt><code>LAPACK95_FOUND</code></p>
<dd>library implementing the LAPACK95 interface is found</dl>
<h3>Intel MKL</h3>
<p>To use the Intel MKL implementation of LAPACK, a project must enable at least one of the <code>C</code> or <code>CXX</code> languages. Set <code>BLA_VENDOR</code> to an Intel MKL variant either on the command-line as <code>-DBLA_VENDOR=Intel10_64lp</code> or in project code: </p>
<pre>set(BLA_VENDOR Intel10_64lp)
find_package(LAPACK)</pre>
<p>In order to build a project using Intel MKL, and end user must first establish an Intel MKL environment. See the <code>FindBLAS</code> module section on Intel MKL for details.</p>
<h3>FindLATEX</h3>
<p>Find LaTeX </p>
<p> This module finds an installed LaTeX and determines the location of the compiler. Additionally the module looks for Latex-related software like BibTeX. </p>
<p> New in version 3.2: Component processing; support for htlatex, pdftops, Biber, xindy, XeLaTeX, LuaLaTeX. </p>
<p> This module sets the following result variables: </p>
<pre>LATEX_FOUND: whether found Latex and requested components
LATEX_&lt;component&gt;_FOUND: whether found &lt;component&gt;
LATEX_COMPILER: path to the LaTeX compiler
PDFLATEX_COMPILER: path to the PdfLaTeX compiler
XELATEX_COMPILER: path to the XeLaTeX compiler
LUALATEX_COMPILER: path to the LuaLaTeX compiler
BIBTEX_COMPILER: path to the BibTeX compiler
BIBER_COMPILER: path to the Biber compiler
MAKEINDEX_COMPILER: path to the MakeIndex compiler
XINDY_COMPILER: path to the xindy compiler
DVIPS_CONVERTER: path to the DVIPS converter
DVIPDF_CONVERTER: path to the DVIPDF converter
PS2PDF_CONVERTER: path to the PS2PDF converter
PDFTOPS_CONVERTER: path to the pdftops converter
LATEX2HTML_CONVERTER: path to the LaTeX2Html converter
HTLATEX_COMPILER: path to the htlatex compiler</pre>
<p>Possible components are: </p>
<pre>PDFLATEX
XELATEX
LUALATEX
BIBTEX
BIBER
MAKEINDEX
XINDY
DVIPS
DVIPDF
PS2PDF
PDFTOPS
LATEX2HTML
HTLATEX</pre>
<p>Example Usages: </p>
<pre>find_package(LATEX)
find_package(LATEX COMPONENTS PDFLATEX)
find_package(LATEX COMPONENTS BIBTEX PS2PDF)</pre>
<h3>FindLibArchive</h3>
<p>Find libarchive library and headers. Libarchive is multi-format archive and compression library. </p>
<p> The module defines the following variables: </p>
<pre>LibArchive_FOUND - true if libarchive was found
LibArchive_INCLUDE_DIRS - include search path
LibArchive_LIBRARIES - libraries to link
LibArchive_VERSION - libarchive 3-component version number</pre>
<p>The module defines the following <code>IMPORTED</code> targets: </p>
<pre>LibArchive::LibArchive - target for linking against libarchive</pre>
<p>New in version 3.6: Support for new libarchive 3.2 version string format.</p>
<h3>FindLibinput</h3>
<p>New in version 3.14. </p>
<p> Find libinput headers and library.</p>
<h3>Imported Targets</h3>
<dl>
<dt><code>Libinput::Libinput</code></p>
<dd>The libinput library, if found.</dl>
<h3>Result Variables</h3>
<p>This will define the following variables in your project:</p>
<dl>
<dt><code>Libinput_FOUND</code></p>
<dd>true if (the requested version of) libinput is available.</p>
<dt><code>Libinput_VERSION</code></p>
<dd>the version of libinput.</p>
<dt><code>Libinput_LIBRARIES</code></p>
<dd>the libraries to link against to use libinput.</p>
<dt><code>Libinput_INCLUDE_DIRS</code></p>
<dd>where to find the libinput headers.</p>
<dt><code>Libinput_COMPILE_OPTIONS</code></p>
<dd>this should be passed to target_compile_options(), if the target is not used for linking</dl>
<h3>FindLibLZMA</h3>
<p>Find LZMA compression algorithm headers and library.</p>
<h3>Imported Targets</h3>
<p>New in version 3.14. </p>
<p> This module defines <code>IMPORTED</code> target <code>LibLZMA::LibLZMA</code>, if liblzma has been found.</p>
<h3>Result variables</h3>
<p>This module will set the following variables in your project:</p>
<dl>
<dt><code>LIBLZMA_FOUND</code></p>
<dd>True if liblzma headers and library were found.</p>
<dt><code>LIBLZMA_INCLUDE_DIRS</code></p>
<dd>Directory where liblzma headers are located.</p>
<dt><code>LIBLZMA_LIBRARIES</code></p>
<dd>Lzma libraries to link against.</p>
<dt><code>LIBLZMA_HAS_AUTO_DECODER</code></p>
<dd>True if lzma_auto_decoder() is found (required).</p>
<dt><code>LIBLZMA_HAS_EASY_ENCODER</code></p>
<dd>True if lzma_easy_encoder() is found (required).</p>
<dt><code>LIBLZMA_HAS_LZMA_PRESET</code></p>
<dd>True if lzma_lzma_preset() is found (required).</p>
<dt><code>LIBLZMA_VERSION_MAJOR</code></p>
<dd>The major version of lzma</p>
<dt><code>LIBLZMA_VERSION_MINOR</code></p>
<dd>The minor version of lzma</p>
<dt><code>LIBLZMA_VERSION_PATCH</code></p>
<dd>The patch version of lzma</p>
<dt><code>LIBLZMA_VERSION_STRING</code></p>
<dd>version number as a string (ex: &quot;5.0.3&quot;)</dl>
<h3>FindLibXml2</h3>
<p>Find the XML processing library (libxml2).</p>
<h3>IMPORTED Targets</h3>
<p>New in version 3.12. </p>
<p> The following <code>IMPORTED</code> targets may be defined:</p>
<dl>
<dt><code>LibXml2::LibXml2</code></p>
<dd>libxml2 library.</p>
<dt><code>LibXml2::xmllint</code></p>
<dd>New in version 3.17. </p>
<p> xmllint command-line executable.</dl>
<h3>Result variables</h3>
<p>This module will set the following variables in your project:</p>
<dl>
<dt><code>LibXml2_FOUND</code></p>
<dd>true if libxml2 headers and libraries were found</p>
<dt><code>LIBXML2_INCLUDE_DIR</code></p>
<dd>the directory containing LibXml2 headers</p>
<dt><code>LIBXML2_INCLUDE_DIRS</code></p>
<dd>list of the include directories needed to use LibXml2</p>
<dt><code>LIBXML2_LIBRARIES</code></p>
<dd>LibXml2 libraries to be linked</p>
<dt><code>LIBXML2_DEFINITIONS</code></p>
<dd>the compiler switches required for using LibXml2</p>
<dt><code>LIBXML2_XMLLINT_EXECUTABLE</code></p>
<dd>path to the XML checking tool xmllint coming with LibXml2</p>
<dt><code>LIBXML2_VERSION_STRING</code></p>
<dd>the version of LibXml2 found (since CMake 2.8.8)</dl>
<h3>Cache variables</h3>
<p>The following cache variables may also be set:</p>
<dl>
<dt><code>LIBXML2_INCLUDE_DIR</code></p>
<dd>the directory containing LibXml2 headers</p>
<dt><code>LIBXML2_LIBRARY</code></p>
<dd>path to the LibXml2 library</dl>
<h3>FindLibXslt</h3>
<p>Find the XSL Transformations, Extensible Stylesheet Language Transformations (XSLT) library (LibXslt)</p>
<h3>IMPORTED Targets</h3>
<p>New in version 3.18. </p>
<p> The following <code>IMPORTED</code> targets may be defined:</p>
<dl>
<dt><code>LibXslt::LibXslt</code></p>
<dd>If the libxslt library has been found</p>
<dt><code>LibXslt::LibExslt</code></p>
<dd>If the libexslt library has been found</p>
<dt><code>LibXslt::xsltproc</code></p>
<dd>If the xsltproc command-line executable has been found</dl>
<h3>Result variables</h3>
<p>This module will set the following variables in your project: LIBXSLT_FOUND &#8211; system has LibXslt LIBXSLT_INCLUDE_DIR &#8211; the LibXslt include directory LIBXSLT_LIBRARIES &#8211; Link these to LibXslt LIBXSLT_DEFINITIONS &#8211; Compiler switches required for using LibXslt LIBXSLT_VERSION_STRING &#8211; version of LibXslt found (since CMake 2.8.8) </p>
<p> Additionally, the following two variables are set (but not required for using xslt):</p>
<dl>
<dt><code>LIBXSLT_EXSLT_INCLUDE_DIR</code></p>
<dd>New in version 3.18: The include directory for exslt. </p>
<dt><code>LIBXSLT_EXSLT_LIBRARIES</code></p>
<dd>Link to these if you need to link against the exslt library.</p>
<dt><code>LIBXSLT_XSLTPROC_EXECUTABLE</code></p>
<dd>Contains the full path to the xsltproc executable if found.</dl>
<h3>FindLTTngUST</h3>
<p>New in version 3.6. </p>
<p> Find <i>Linux Trace Toolkit Next Generation (LTTng-UST)</i> library.</p>
<h3>Imported target</h3>
<p>This module defines the following <code>IMPORTED</code> target:</p>
<dl>
<dt><code>LTTng::UST</code></p>
<dd>The LTTng-UST library, if found</dl>
<h3>Result variables</h3>
<p>This module sets the following</p>
<dl>
<dt><code>LTTNGUST_FOUND</code></p>
<dd><code>TRUE</code> if system has LTTng-UST</p>
<dt><code>LTTNGUST_INCLUDE_DIRS</code></p>
<dd>The LTTng-UST include directories</p>
<dt><code>LTTNGUST_LIBRARIES</code></p>
<dd>The libraries needed to use LTTng-UST</p>
<dt><code>LTTNGUST_VERSION_STRING</code></p>
<dd>The LTTng-UST version</p>
<dt><code>LTTNGUST_HAS_TRACEF</code></p>
<dd><code>TRUE</code> if the <code>tracef()</code> API is available in the system&#8217;s LTTng-UST</p>
<dt><code>LTTNGUST_HAS_TRACELOG</code></p>
<dd><code>TRUE</code> if the <code>tracelog()</code> API is available in the system&#8217;s LTTng-UST</dl>
<h3>FindLua</h3>
<p>Locate Lua library. </p>
<p> New in version 3.18: Support for Lua 5.4. </p>
<p> This module defines: </p>
<pre>::</pre>
<p>LUA_FOUND &#8211; if false, do not try to link to Lua LUA_LIBRARIES &#8211; both lua and lualib LUA_INCLUDE_DIR &#8211; where to find lua.h LUA_VERSION_STRING &#8211; the version of Lua found LUA_VERSION_MAJOR &#8211; the major version of Lua LUA_VERSION_MINOR &#8211; the minor version of Lua LUA_VERSION_PATCH &#8211; the patch version of Lua </p>
<p> Note that the expected include convention is </p>
<pre>#include &quot;lua.h&quot;</pre>
<p>and not </p>
<pre>#include &lt;lua/lua.h&gt;</pre>
<p>This is because, the lua location is not standardized and may exist in locations other than lua/</p>
<h3>FindLua50</h3>
<p>Locate Lua library. This module defines: </p>
<pre>::</pre>
<p>LUA50_FOUND, if false, do not try to link to Lua LUA_LIBRARIES, both lua and lualib LUA_INCLUDE_DIR, where to find lua.h and lualib.h (and probably lauxlib.h) </p>
<p> Note that the expected include convention is </p>
<pre>#include &quot;lua.h&quot;</pre>
<p>and not </p>
<pre>#include &lt;lua/lua.h&gt;</pre>
<p>This is because, the lua location is not standardized and may exist in locations other than lua/</p>
<h3>FindLua51</h3>
<p>Locate Lua library. This module defines: </p>
<pre>::</pre>
<p>LUA51_FOUND, if false, do not try to link to Lua LUA_LIBRARIES LUA_INCLUDE_DIR, where to find lua.h LUA_VERSION_STRING, the version of Lua found (since CMake 2.8.8) </p>
<p> Note that the expected include convention is </p>
<pre>#include &quot;lua.h&quot;</pre>
<p>and not </p>
<pre>#include &lt;lua/lua.h&gt;</pre>
<p>This is because, the lua location is not standardized and may exist in locations other than lua/</p>
<h3>FindMatlab</h3>
<p>Finds Matlab or Matlab Compiler Runtime (MCR) and provides Matlab tools, libraries and compilers to CMake. </p>
<p> This package primary purpose is to find the libraries associated with Matlab or the MCR in order to be able to build Matlab extensions (mex files). It can also be used:</p>
<dl>
<dt>&bull;</p>
<dd>to run specific commands in Matlab in case Matlab is available</p>
<dt>&bull;</p>
<dd>for declaring Matlab unit test</p>
<dt>&bull;</p>
<dd>to retrieve various information from Matlab (mex extensions, versions and release queries, &#8230;) </p>
<p> New in version 3.12: Added Matlab Compiler Runtime (MCR) support. </p>
<p> The module supports the following components:</p>
<dt>&bull;</p>
<dd><code>ENG_LIBRARY</code> and <code>MAT_LIBRARY</code>: respectively the <code>ENG</code> and <code>MAT</code> libraries of Matlab</p>
<dt>&bull;</p>
<dd><code>MAIN_PROGRAM</code> the Matlab binary program. Note that this component is not available on the MCR version, and will yield an error if the MCR is found instead of the regular Matlab installation.</p>
<dt>&bull;</p>
<dd><code>MEX_COMPILER</code> the MEX compiler.</p>
<dt>&bull;</p>
<dd><code>MCC_COMPILER</code> the MCC compiler, included with the Matlab Compiler add-on.</p>
<dt>&bull;</p>
<dd><code>SIMULINK</code> the Simulink environment. </p>
<p> New in version 3.7: Added the <code>MAT_LIBRARY</code> component. </p>
<p> New in version 3.13: Added the <code>ENGINE_LIBRARY</code>, <code>DATAARRAY_LIBRARY</code> and <code>MCC_COMPILER</code> components. </p>
<p> Changed in version 3.14: Removed the <code>MX_LIBRARY</code>, <code>ENGINE_LIBRARY</code> and <code>DATAARRAY_LIBRARY</code> components. These libraries are found unconditionally. </p>
<p> <code>NOTE:</code> The version given to the <code>find_package()</code> directive is the Matlab <code>version</code>, which should not be confused with the Matlab <i>release</i> name (eg. <i>R2014</i>). The <i>matlab_get_version_from_release_name()</i> and <i>matlab_get_release_name_from_version()</i> provide a mapping between the release name and the version. </p>
<p> The variable <i>Matlab_ROOT_DIR</i> may be specified in order to give the path of the desired Matlab version. Otherwise, the behavior is platform specific:</p>
<dt>&bull;</p>
<dd>Windows: The installed versions of Matlab/MCR are retrieved from the Windows registry</p>
<dt>&bull;</p>
<dd>OS X: The installed versions of Matlab/MCR are given by the MATLAB default installation paths in <code>/Application</code>. If no such application is found, it falls back to the one that might be accessible from the <code>PATH</code>.</p>
<dt>&bull;</p>
<dd>Unix: The desired Matlab should be accessible from the <code>PATH</code>. This does not work for MCR installation and <i>Matlab_ROOT_DIR</i> should be specified on this platform. </p>
<p> Additional information is provided when <i>MATLAB_FIND_DEBUG</i> is set. When a Matlab/MCR installation is found automatically and the <code>MATLAB_VERSION</code> is not given, the version is queried from Matlab directly (on Windows this may pop up a Matlab window) or from the MCR installation. </p>
<p> The mapping of the release names and the version of Matlab is performed by defining pairs (name, version). The variable <i>MATLAB_ADDITIONAL_VERSIONS</i> may be provided before the call to the <code>find_package()</code> in order to handle additional versions. </p>
<p> A Matlab scripts can be added to the set of tests using the <i>matlab_add_unit_test()</i>. By default, the Matlab unit test framework will be used (&gt;= 2013a) to run this script, but regular <code>.m</code> files returning an exit code can be used as well (0 indicating a success).</dl>
<h3>Module Input Variables</h3>
<p>Users or projects may set the following variables to configure the module behavior:</p>
<dl>
<dt><i>Matlab_ROOT_DIR</i></p>
<dd>the root of the Matlab installation.</p>
<dt><i>MATLAB_FIND_DEBUG</i></p>
<dd>outputs debug information</p>
<dt><i>MATLAB_ADDITIONAL_VERSIONS</i></p>
<dd>additional versions of Matlab for the automatic retrieval of the installed versions.</dl>
<h3>Imported targets</h3>
<p>New in version 3.22. </p>
<p> This module defines the following <code>IMPORTED</code> targets:</p>
<dl>
<dt><code>Matlab::mex</code></p>
<dd>The <code>mex</code> library, always available.</p>
<dt><code>Matlab::mx</code></p>
<dd>The mx library of Matlab (arrays), always available.</p>
<dt><code>Matlab::eng</code></p>
<dd>Matlab engine library. Available only if the <code>ENG_LIBRARY</code> component is requested.</p>
<dt><code>Matlab::mat</code></p>
<dd>Matlab matrix library. Available only if the <code>MAT_LIBRARY</code> component is requested.</p>
<dt><code>Matlab::MatlabEngine</code></p>
<dd>Matlab C++ engine library, always available for R2018a and newer.</p>
<dt><code>Matlab::MatlabDataArray</code></p>
<dd>Matlab C++ data array library, always available for R2018a and newer.</dl>
<h3>Variables defined by the module</h3>
<h3>Result variables</h3>
<dl>
<dt><code>Matlab_FOUND</code></p>
<dd><code>TRUE</code> if the Matlab installation is found, <code>FALSE</code> otherwise. All variable below are defined if Matlab is found.</p>
<dt><code>Matlab_ROOT_DIR</code></p>
<dd>the final root of the Matlab installation determined by the FindMatlab module.</p>
<dt><code>Matlab_MAIN_PROGRAM</code></p>
<dd>the Matlab binary program. Available only if the component <code>MAIN_PROGRAM</code> is given in the <code>find_package()</code> directive.</p>
<dt><code>Matlab_INCLUDE_DIRS</code></p>
<dd>the path of the Matlab libraries headers</p>
<dt><code>Matlab_MEX_LIBRARY</code></p>
<dd>library for mex, always available.</p>
<dt><code>Matlab_MX_LIBRARY</code></p>
<dd>mx library of Matlab (arrays), always available.</p>
<dt><code>Matlab_ENG_LIBRARY</code></p>
<dd>Matlab engine library. Available only if the component <code>ENG_LIBRARY</code> is requested.</p>
<dt><code>Matlab_MAT_LIBRARY</code></p>
<dd>Matlab matrix library. Available only if the component <code>MAT_LIBRARY</code> is requested.</p>
<dt><code>Matlab_ENGINE_LIBRARY</code></p>
<dd>New in version 3.13. </p>
<p> Matlab C++ engine library, always available for R2018a and newer.</p>
<dt><code>Matlab_DATAARRAY_LIBRARY</code></p>
<dd>New in version 3.13. </p>
<p> Matlab C++ data array library, always available for R2018a and newer.</p>
<dt><code>Matlab_LIBRARIES</code></p>
<dd>the whole set of libraries of Matlab</p>
<dt><code>Matlab_MEX_COMPILER</code></p>
<dd>the mex compiler of Matlab. Currently not used. Available only if the component <code>MEX_COMPILER</code> is requested.</p>
<dt><code>Matlab_MCC_COMPILER</code></p>
<dd>New in version 3.13. </p>
<p> the mcc compiler of Matlab. Included with the Matlab Compiler add-on. Available only if the component <code>MCC_COMPILER</code> is requested.</dl>
<h3>Cached variables</h3>
<dl>
<dt><code>Matlab_MEX_EXTENSION</code></p>
<dd>the extension of the mex files for the current platform (given by Matlab).</p>
<dt><code>Matlab_ROOT_DIR</code></p>
<dd>the location of the root of the Matlab installation found. If this value is changed by the user, the result variables are recomputed.</dl>
<h3>Provided macros</h3>
<dl>
<dt><i>matlab_get_version_from_release_name()</i></p>
<dd>returns the version from the release name</p>
<dt><i>matlab_get_release_name_from_version()</i></p>
<dd>returns the release name from the Matlab version</dl>
<h3>Provided functions</h3>
<dl>
<dt><i>matlab_add_mex()</i></p>
<dd>adds a target compiling a MEX file.</p>
<dt><i>matlab_add_unit_test()</i></p>
<dd>adds a Matlab unit test file as a test to the project.</p>
<dt><i>matlab_extract_all_installed_versions_from_registry()</i></p>
<dd>parses the registry for all Matlab versions. Available on Windows only. The part of the registry parsed is dependent on the host processor</p>
<dt><i>matlab_get_all_valid_matlab_roots_from_registry()</i></p>
<dd>returns all the possible Matlab or MCR paths, according to a previously given list. Only the existing/accessible paths are kept. This is mainly useful for the searching all possible Matlab installation.</p>
<dt><i>matlab_get_mex_suffix()</i></p>
<dd>returns the suffix to be used for the mex files (platform/architecture dependent)</p>
<dt><i>matlab_get_version_from_matlab_run()</i></p>
<dd>returns the version of Matlab/MCR, given the full directory of the Matlab/MCR installation path.</dl>
<h3>Known issues</h3>
<dl>
<dt><code>Symbol clash in a MEX target</code></p>
<dd>By default, every symbols inside a MEX file defined with the command <i>matlab_add_mex()</i> have hidden visibility, except for the entry point. This is the default behavior of the MEX compiler, which lowers the risk of symbol collision between the libraries shipped with Matlab, and the libraries to which the MEX file is linking to. This is also the default on Windows platforms. </p>
<p> However, this is not sufficient in certain case, where for instance your MEX file is linking against libraries that are already loaded by Matlab, even if those libraries have different SONAMES. A possible solution is to hide the symbols of the libraries to which the MEX target is linking to. This can be achieved in GNU GCC compilers with the linker option <code>-Wl,&#8211;exclude-libs,ALL</code>.</p>
<dt><code>Tests using GPU resources</code></p>
<dd>in case your MEX file is using the GPU and in order to be able to run unit tests on this MEX file, the GPU resources should be properly released by Matlab. A possible solution is to make Matlab aware of the use of the GPU resources in the session, which can be performed by a command such as <code>D = gpuDevice()</code> at the beginning of the test script (or via a fixture).</dl>
<h3>Reference</h3>
<dl>
<dt><code>Matlab_ROOT_DIR</code></p>
<dd>The root folder of the Matlab installation. If set before the call to <code>find_package()</code>, the module will look for the components in that path. If not set, then an automatic search of Matlab will be performed. If set, it should point to a valid version of Matlab.</p>
<dt><code>MATLAB_FIND_DEBUG</code></p>
<dd>If set, the lookup of Matlab and the intermediate configuration steps are outputted to the console.</p>
<dt><code>MATLAB_ADDITIONAL_VERSIONS</code></p>
<dd>If set, specifies additional versions of Matlab that may be looked for. The variable should be a list of strings, organized by pairs of release name and versions, such as follows: </p>
<pre>set(MATLAB_ADDITIONAL_VERSIONS
 &quot;release_name1=corresponding_version1&quot;
 &quot;release_name2=corresponding_version2&quot;
 ...
 )</pre>
<p>Example: </p>
<pre>set(MATLAB_ADDITIONAL_VERSIONS
 &quot;R2013b=8.2&quot;
 &quot;R2013a=8.1&quot;
 &quot;R2012b=8.0&quot;)</pre>
<p>The order of entries in this list matters when several versions of Matlab are installed. The priority is set according to the ordering in this list.</p>
<dt><code>matlab_get_version_from_release_name</code></p>
<dd>Returns the version of Matlab (17.58) from a release name (R2017k)</p>
<dt><code>matlab_get_release_name_from_version</code></p>
<dd>Returns the release name (R2017k) from the version of Matlab (17.58)</p>
<dt><code>matlab_extract_all_installed_versions_from_registry</code></p>
<dd>This function parses the registry and founds the Matlab versions that are installed. The found versions are returned in <i>matlab_versions</i>. Set <i>win64</i> to <i>TRUE</i> if the 64 bit version of Matlab should be looked for The returned list contains all versions under <code>HKLM\SOFTWARE\Mathworks\MATLAB</code> and <code>HKLM\SOFTWARE\Mathworks\MATLAB Runtime</code> or an empty list in case an error occurred (or nothing found). </p>
<p> <code>NOTE:</code> Only the versions are provided. No check is made over the existence of the installation referenced in the registry,</p>
<dt><code>matlab_get_all_valid_matlab_roots_from_registry</code></p>
<dd>Populates the Matlab root with valid versions of Matlab or Matlab Runtime (MCR). The returned matlab_roots is organized in triplets <code>(type,version_number,matlab_root_path)</code>, where <code>type</code> indicates either <code>MATLAB</code> or <code>MCR</code>. </p>
<pre>matlab_get_all_valid_matlab_roots_from_registry(
 matlab_versions
 matlab_roots)</pre>
<dt><code>matlab_versions</code></p>
<dd>the versions of each of the Matlab or MCR installations</p>
<dt><code>matlab_roots</code></p>
<dd>the location of each of the Matlab or MCR installations</p>
<dt><code>matlab_get_mex_suffix</code></p>
<dd>Returns the extension of the mex files (the suffixes). This function should not be called before the appropriate Matlab root has been found. </p>
<pre>matlab_get_mex_suffix(
 matlab_root
 mex_suffix)</pre>
<dt><code>matlab_root</code></p>
<dd>the root of the Matlab/MCR installation</p>
<dt><code>mex_suffix</code></p>
<dd>the variable name in which the suffix will be returned.</p>
<dt><code>matlab_get_version_from_matlab_run</code></p>
<dd>This function runs Matlab program specified on arguments and extracts its version. If the path provided for the Matlab installation points to an MCR installation, the version is extracted from the installed files. </p>
<pre>matlab_get_version_from_matlab_run(
 matlab_binary_path
 matlab_list_versions)</pre>
<dt><code>matlab_binary_path</code></p>
<dd>the location of the <i>matlab</i> binary executable</p>
<dt><code>matlab_list_versions</code></p>
<dd>the version extracted from Matlab</p>
<dt><code>matlab_add_unit_test</code></p>
<dd>Adds a Matlab unit test to the test set of cmake/ctest. This command requires the component <code>MAIN_PROGRAM</code> and hence is not available for an MCR installation. </p>
<p> The unit test uses the Matlab unittest framework (default, available starting Matlab 2013b+) except if the option <code>NO_UNITTEST_FRAMEWORK</code> is given. </p>
<p> The function expects one Matlab test script file to be given. In the case <code>NO_UNITTEST_FRAMEWORK</code> is given, the unittest script file should contain the script to be run, plus an exit command with the exit value. This exit value will be passed to the ctest framework (0 success, non 0 failure). Additional arguments accepted by <code>add_test()</code> can be passed through <code>TEST_ARGS</code> (eg. <code>CONFIGURATION &lt;config&gt; &#8230;</code>). </p>
<pre>matlab_add_unit_test(
 NAME &lt;name&gt;
 UNITTEST_FILE matlab_file_containing_unittest.m
 [CUSTOM_TEST_COMMAND matlab_command_to_run_as_test]
 [UNITTEST_PRECOMMAND matlab_command_to_run]
 [TIMEOUT timeout]
 [ADDITIONAL_PATH path1 [path2 ...]]
 [MATLAB_ADDITIONAL_STARTUP_OPTIONS option1 [option2 ...]]
 [TEST_ARGS arg1 [arg2 ...]]
 [NO_UNITTEST_FRAMEWORK]
 )</pre>
<p>The function arguments are:</p>
<dt><code>NAME</code></p>
<dd>name of the unittest in ctest.</p>
<dt><code>UNITTEST_FILE</code></p>
<dd>the matlab unittest file. Its path will be automatically added to the Matlab path.</p>
<dt><code>CUSTOM_TEST_COMMAND</code></p>
<dd>Matlab script command to run as the test. If this is not set, then the following is run: <code>runtests(&#8216;matlab_file_name&#8217;), exit(max([ans(1,:).Failed]))</code> where <code>matlab_file_name</code> is the <code>UNITTEST_FILE</code> without the extension.</p>
<dt><code>UNITTEST_PRECOMMAND</code></p>
<dd>Matlab script command to be ran before the file containing the test (eg. GPU device initialization based on CMake variables).</p>
<dt><code>TIMEOUT</code></p>
<dd>the test timeout in seconds. Defaults to 180 seconds as the Matlab unit test may hang.</p>
<dt><code>ADDITIONAL_PATH</code></p>
<dd>a list of paths to add to the Matlab path prior to running the unit test.</p>
<dt><code>MATLAB_ADDITIONAL_STARTUP_OPTIONS</code></p>
<dd>a list of additional option in order to run Matlab from the command line. <code>-nosplash -nodesktop -nodisplay</code> are always added.</p>
<dt><code>TEST_ARGS</code></p>
<dd>Additional options provided to the add_test command. These options are added to the default options (eg. &quot;CONFIGURATIONS Release&quot;)</p>
<dt><code>NO_UNITTEST_FRAMEWORK</code></p>
<dd>when set, indicates that the test should not use the unittest framework of Matlab (available for versions &gt;= R2013a).</p>
<dt><code>WORKING_DIRECTORY</code></p>
<dd>This will be the working directory for the test. If specified it will also be the output directory used for the log file of the test run. If not specified the temporary directory <code>${CMAKE_BINARY_DIR}/Matlab</code> will be used as the working directory and the log location.</p>
<dt><code>matlab_add_mex</code></p>
<dd>Adds a Matlab MEX target. This commands compiles the given sources with the current tool-chain in order to produce a MEX file. The final name of the produced output may be specified, as well as additional link libraries, and a documentation entry for the MEX file. Remaining arguments of the call are passed to the <code>add_library()</code> or <code>add_executable()</code> command. </p>
<pre>matlab_add_mex(
 NAME &lt;name&gt;
 [EXECUTABLE | MODULE | SHARED]
 SRC src1 [src2 ...]
 [OUTPUT_NAME output_name]
 [DOCUMENTATION file.txt]
 [LINK_TO target1 target2 ...]
 [R2017b | R2018a]
 [EXCLUDE_FROM_ALL]
 [...]
)</pre>
<dt><code>NAME</code></p>
<dd>name of the target.</p>
<dt><code>SRC</code></p>
<dd>list of source files.</p>
<dt><code>LINK_TO</code></p>
<dd>a list of additional link dependencies. The target links to <code>libmex</code> and <code>libmx</code> by default.</p>
<dt><code>OUTPUT_NAME</code></p>
<dd>if given, overrides the default name. The default name is the name of the target without any prefix and with <code>Matlab_MEX_EXTENSION</code> suffix.</p>
<dt><code>DOCUMENTATION</code></p>
<dd>if given, the file <code>file.txt</code> will be considered as being the documentation file for the MEX file. This file is copied into the same folder without any processing, with the same name as the final mex file, and with extension <i>.m</i>. In that case, typing <code>help &lt;name&gt;</code> in Matlab prints the documentation contained in this file.</p>
<dt><code>R2017b</code> or <code>R2018a</code></p>
<dd>New in version 3.14. </p>
<p> May be given to specify the version of the C API to use: <code>R2017b</code> specifies the traditional (separate complex) C API, and corresponds to the <code>-R2017b</code> flag for the <i>mex</i> command. <code>R2018a</code> specifies the new interleaved complex C API, and corresponds to the <code>-R2018a</code> flag for the <i>mex</i> command. Ignored if MATLAB version prior to R2018a. Defaults to <code>R2017b</code>.</p>
<dt><code>MODULE</code> or <code>SHARED</code></p>
<dd>New in version 3.7. </p>
<p> May be given to specify the type of library to be created.</p>
<dt><code>EXECUTABLE</code></p>
<dd>New in version 3.7. </p>
<p> May be given to create an executable instead of a library. If no type is given explicitly, the type is <code>SHARED</code>.</p>
<dt><code>EXCLUDE_FROM_ALL</code></p>
<dd>This option has the same meaning as for <code>EXCLUDE_FROM_ALL</code> and is forwarded to <code>add_library()</code> or <code>add_executable()</code> commands. </p>
<p> The documentation file is not processed and should be in the following format: </p>
<pre>% This is the documentation
function ret = mex_target_output_name(input1)</pre>
</dl>
<h3>FindMFC</h3>
<p>Find Microsoft Foundation Class Library (MFC) on Windows </p>
<p> Find the native MFC &#8211; i.e. decide if an application can link to the MFC libraries. </p>
<pre>MFC_FOUND - Was MFC support found</pre>
<p>You don&#8217;t need to include anything or link anything to use it.</p>
<h3>FindMotif</h3>
<p>Try to find Motif (or lesstif) </p>
<p> Once done this will define: </p>
<pre>MOTIF_FOUND - system has MOTIF
MOTIF_INCLUDE_DIR - include paths to use Motif
MOTIF_LIBRARIES - Link these to use Motif</pre>
<h3>FindMPEG</h3>
<p>Find the native MPEG includes and library </p>
<p> This module defines </p>
<pre>MPEG_INCLUDE_DIR, where to find MPEG.h, etc.
MPEG_LIBRARIES, the libraries required to use MPEG.
MPEG_FOUND, If false, do not try to use MPEG.</pre>
<p>also defined, but not for general use are </p>
<pre>MPEG_mpeg2_LIBRARY, where to find the MPEG library.
MPEG_vo_LIBRARY, where to find the vo library.</pre>
<h3>FindMPEG2</h3>
<p>Find the native MPEG2 includes and library </p>
<p> This module defines </p>
<pre>MPEG2_INCLUDE_DIR, path to mpeg2dec/mpeg2.h, etc.
MPEG2_LIBRARIES, the libraries required to use MPEG2.
MPEG2_FOUND, If false, do not try to use MPEG2.</pre>
<p>also defined, but not for general use are </p>
<pre>MPEG2_mpeg2_LIBRARY, where to find the MPEG2 library.
MPEG2_vo_LIBRARY, where to find the vo library.</pre>
<h3>FindMPI</h3>
<p>Find a Message Passing Interface (MPI) implementation. </p>
<p> The Message Passing Interface (MPI) is a library used to write high-performance distributed-memory parallel applications, and is typically deployed on a cluster. MPI is a standard interface (defined by the MPI forum) for which many implementations are available. </p>
<p> New in version 3.10: Major overhaul of the module: many new variables, per-language components, support for a wider variety of runtimes.</p>
<h3>Variables for using MPI</h3>
<p>The module exposes the components <code>C</code>, <code>CXX</code>, <code>MPICXX</code> and <code>Fortran</code>. Each of these controls the various MPI languages to search for. The difference between <code>CXX</code> and <code>MPICXX</code> is that <code>CXX</code> refers to the MPI C API being usable from C++, whereas <code>MPICXX</code> refers to the MPI-2 C++ API that was removed again in MPI-3. </p>
<p> Depending on the enabled components the following variables will be set:</p>
<dl>
<dt><code>MPI_FOUND</code></p>
<dd>Variable indicating that MPI settings for all requested languages have been found. If no components are specified, this is true if MPI settings for all enabled languages were detected. Note that the <code>MPICXX</code> component does not affect this variable.</p>
<dt><code>MPI_VERSION</code></p>
<dd>Minimal version of MPI detected among the requested languages, or all enabled languages if no components were specified. </p>
<p> This module will set the following variables per language in your project, where <code>&lt;lang&gt;</code> is one of C, CXX, or Fortran:</p>
<dt><code>MPI_&lt;lang&gt;_FOUND</code></p>
<dd>Variable indicating the MPI settings for <code>&lt;lang&gt;</code> were found and that simple MPI test programs compile with the provided settings.</p>
<dt><code>MPI_&lt;lang&gt;_COMPILER</code></p>
<dd>MPI compiler for <code>&lt;lang&gt;</code> if such a program exists.</p>
<dt><code>MPI_&lt;lang&gt;_COMPILE_OPTIONS</code></p>
<dd>Compilation options for MPI programs in <code>&lt;lang&gt;</code>, given as a ;-list.</p>
<dt><code>MPI_&lt;lang&gt;_COMPILE_DEFINITIONS</code></p>
<dd>Compilation definitions for MPI programs in <code>&lt;lang&gt;</code>, given as a ;-list.</p>
<dt><code>MPI_&lt;lang&gt;_INCLUDE_DIRS</code></p>
<dd>Include path(s) for MPI header.</p>
<dt><code>MPI_&lt;lang&gt;_LINK_FLAGS</code></p>
<dd>Linker flags for MPI programs.</p>
<dt><code>MPI_&lt;lang&gt;_LIBRARIES</code></p>
<dd>All libraries to link MPI programs against. </p>
<p> New in version 3.9: Additionally, the following <code>IMPORTED</code> targets are defined: </p>
<dt><code>MPI::MPI_&lt;lang&gt;</code></p>
<dd>Target for using MPI from <code>&lt;lang&gt;</code>. </p>
<p> The following variables indicating which bindings are present will be defined:</p>
<dt><code>MPI_MPICXX_FOUND</code></p>
<dd>Variable indicating whether the MPI-2 C++ bindings are present (introduced in MPI-2, removed with MPI-3).</p>
<dt><code>MPI_Fortran_HAVE_F77_HEADER</code></p>
<dd>True if the Fortran 77 header <code>mpif.h</code> is available.</p>
<dt><code>MPI_Fortran_HAVE_F90_MODULE</code></p>
<dd>True if the Fortran 90 module <code>mpi</code> can be used for accessing MPI (MPI-2 and higher only).</p>
<dt><code>MPI_Fortran_HAVE_F08_MODULE</code></p>
<dd>True if the Fortran 2008 <code>mpi_f08</code> is available to MPI programs (MPI-3 and higher only). </p>
<p> If possible, the MPI version will be determined by this module. The facilities to detect the MPI version were introduced with MPI-1.2, and therefore cannot be found for older MPI versions.</p>
<dt><code>MPI_&lt;lang&gt;_VERSION_MAJOR</code></p>
<dd>Major version of MPI implemented for <code>&lt;lang&gt;</code> by the MPI distribution.</p>
<dt><code>MPI_&lt;lang&gt;_VERSION_MINOR</code></p>
<dd>Minor version of MPI implemented for <code>&lt;lang&gt;</code> by the MPI distribution.</p>
<dt><code>MPI_&lt;lang&gt;_VERSION</code></p>
<dd>MPI version implemented for <code>&lt;lang&gt;</code> by the MPI distribution. </p>
<p> Note that there&#8217;s no variable for the C bindings being accessible through <code>mpi.h</code>, since the MPI standards always have required this binding to work in both C and C++ code. </p>
<p> For running MPI programs, the module sets the following variables</p>
<dt><code>MPIEXEC_EXECUTABLE</code></p>
<dd>Executable for running MPI programs, if such exists.</p>
<dt><code>MPIEXEC_NUMPROC_FLAG</code></p>
<dd>Flag to pass to <code>mpiexec</code> before giving it the number of processors to run on.</p>
<dt><code>MPIEXEC_MAX_NUMPROCS</code></p>
<dd>Number of MPI processors to utilize. Defaults to the number of processors detected on the host system.</p>
<dt><code>MPIEXEC_PREFLAGS</code></p>
<dd>Flags to pass to <code>mpiexec</code> directly before the executable to run.</p>
<dt><code>MPIEXEC_POSTFLAGS</code></p>
<dd>Flags to pass to <code>mpiexec</code> after other flags.</dl>
<h3>Variables for locating MPI</h3>
<p>This module performs a four step search for an MPI implementation:</p>
<dl>
<dt>1.</p>
<dd>Search for <code>MPIEXEC_EXECUTABLE</code> and, if found, use its base directory.</p>
<dt>2.</p>
<dd>Check if the compiler has MPI support built-in. This is the case if the user passed a compiler wrapper as <code>CMAKE_&lt;LANG&gt;_COMPILER</code> or if they use Cray system compiler wrappers.</p>
<dt>3.</p>
<dd>Attempt to find an MPI compiler wrapper and determine the compiler information from it.</p>
<dt>4.</p>
<dd>Try to find an MPI implementation that does not ship such a wrapper by guessing settings. Currently, only Microsoft MPI and MPICH2 on Windows are supported. </p>
<p> For controlling the <code>MPIEXEC_EXECUTABLE</code> step, the following variables may be set:</p>
<dt><code>MPIEXEC_EXECUTABLE</code></p>
<dd>Manually specify the location of <code>mpiexec</code>.</p>
<dt><code>MPI_HOME</code></p>
<dd>Specify the base directory of the MPI installation.</p>
<dt><code>ENV{MPI_HOME}</code></p>
<dd>Environment variable to specify the base directory of the MPI installation.</p>
<dt><code>ENV{I_MPI_ROOT}</code></p>
<dd>Environment variable to specify the base directory of the MPI installation. </p>
<p> For controlling the compiler wrapper step, the following variables may be set:</p>
<dt><code>MPI_&lt;lang&gt;_COMPILER</code></p>
<dd>Search for the specified compiler wrapper and use it.</p>
<dt><code>MPI_&lt;lang&gt;_COMPILER_FLAGS</code></p>
<dd>Flags to pass to the MPI compiler wrapper during interrogation. Some compiler wrappers support linking debug or tracing libraries if a specific flag is passed and this variable may be used to obtain them.</p>
<dt><code>MPI_COMPILER_FLAGS</code></p>
<dd>Used to initialize <code>MPI_&lt;lang&gt;_COMPILER_FLAGS</code> if no language specific flag has been given. Empty by default.</p>
<dt><code>MPI_EXECUTABLE_SUFFIX</code></p>
<dd>A suffix which is appended to all names that are being looked for. For instance you may set this to <code>.mpich</code> or <code>.openmpi</code> to prefer the one or the other on Debian and its derivatives. </p>
<p> In order to control the guessing step, the following variable may be set:</p>
<dt><code>MPI_GUESS_LIBRARY_NAME</code></p>
<dd>Valid values are <code>MSMPI</code> and <code>MPICH2</code>. If set, only the given library will be searched for. By default, <code>MSMPI</code> will be preferred over <code>MPICH2</code> if both are available. This also sets <code>MPI_SKIP_COMPILER_WRAPPER</code> to <code>true</code>, which may be overridden. </p>
<p> Each of the search steps may be skipped with the following control variables:</p>
<dt><code>MPI_ASSUME_NO_BUILTIN_MPI</code></p>
<dd>If true, the module assumes that the compiler itself does not provide an MPI implementation and skips to step 2.</p>
<dt><code>MPI_SKIP_COMPILER_WRAPPER</code></p>
<dd>If true, no compiler wrapper will be searched for.</p>
<dt><code>MPI_SKIP_GUESSING</code></p>
<dd>If true, the guessing step will be skipped. </p>
<p> Additionally, the following control variable is available to change search behavior:</p>
<dt><code>MPI_CXX_SKIP_MPICXX</code></p>
<dd>Add some definitions that will disable the MPI-2 C++ bindings. Currently supported are MPICH, Open MPI, Platform MPI and derivatives thereof, for example MVAPICH or Intel MPI. </p>
<p> If the find procedure fails for a variable <code>MPI_&lt;lang&gt;_WORKS</code>, then the settings detected by or passed to the module did not work and even a simple MPI test program failed to compile. </p>
<p> If all of these parameters were not sufficient to find the right MPI implementation, a user may disable the entire autodetection process by specifying both a list of libraries in <code>MPI_&lt;lang&gt;_LIBRARIES</code> and a list of include directories in <code>MPI_&lt;lang&gt;_ADDITIONAL_INCLUDE_DIRS</code>. Any other variable may be set in addition to these two. The module will then validate the MPI settings and store the settings in the cache.</dl>
<h3>Cache variables for MPI</h3>
<p>The variable <code>MPI_&lt;lang&gt;_INCLUDE_DIRS</code> will be assembled from the following variables. For C and CXX:</p>
<dl>
<dt><code>MPI_&lt;lang&gt;_HEADER_DIR</code></p>
<dd>Location of the <code>mpi.h</code> header on disk. </p>
<p> For Fortran:</p>
<dt><code>MPI_Fortran_F77_HEADER_DIR</code></p>
<dd>Location of the Fortran 77 header <code>mpif.h</code>, if it exists.</p>
<dt><code>MPI_Fortran_MODULE_DIR</code></p>
<dd>Location of the <code>mpi</code> or <code>mpi_f08</code> modules, if available. </p>
<p> For all languages the following variables are additionally considered:</p>
<dt><code>MPI_&lt;lang&gt;_ADDITIONAL_INCLUDE_DIRS</code></p>
<dd>A ;-list of paths needed in addition to the normal include directories.</p>
<dt><code>MPI_&lt;include_name&gt;_INCLUDE_DIR</code></p>
<dd>Path variables for include folders referred to by <code>&lt;include_name&gt;</code>.</p>
<dt><code>MPI_&lt;lang&gt;_ADDITIONAL_INCLUDE_VARS</code></p>
<dd>A ;-list of <code>&lt;include_name&gt;</code> that will be added to the include locations of <code>&lt;lang&gt;</code>. </p>
<p> The variable <code>MPI_&lt;lang&gt;_LIBRARIES</code> will be assembled from the following variables:</p>
<dt><code>MPI_&lt;lib_name&gt;_LIBRARY</code></p>
<dd>The location of a library called <code>&lt;lib_name&gt;</code> for use with MPI.</p>
<dt><code>MPI_&lt;lang&gt;_LIB_NAMES</code></p>
<dd>A ;-list of <code>&lt;lib_name&gt;</code> that will be added to the include locations of <code>&lt;lang&gt;</code>.</dl>
<h3>Usage of mpiexec</h3>
<p>When using <code>MPIEXEC_EXECUTABLE</code> to execute MPI applications, you should typically use all of the <code>MPIEXEC_EXECUTABLE</code> flags as follows: </p>
<pre>${MPIEXEC_EXECUTABLE} ${MPIEXEC_NUMPROC_FLAG} ${MPIEXEC_MAX_NUMPROCS}
 ${MPIEXEC_PREFLAGS} EXECUTABLE ${MPIEXEC_POSTFLAGS} ARGS</pre>
<p>where <code>EXECUTABLE</code> is the MPI program, and <code>ARGS</code> are the arguments to pass to the MPI program.</p>
<h3>Advanced variables for using MPI</h3>
<p>The module can perform some advanced feature detections upon explicit request. </p>
<p> <code>Important notice:</code> The following checks cannot be performed without <i>executing</i> an MPI test program. Consider the special considerations for the behavior of <code>try_run()</code> during cross compilation. Moreover, running an MPI program can cause additional issues, like a firewall notification on some systems. You should only enable these detections if you absolutely need the information. </p>
<p> If the following variables are set to true, the respective search will be performed:</p>
<dl>
<dt><code>MPI_DETERMINE_Fortran_CAPABILITIES</code></p>
<dd>Determine for all available Fortran bindings what the values of <code>MPI_SUBARRAYS_SUPPORTED</code> and <code>MPI_ASYNC_PROTECTS_NONBLOCKING</code> are and make their values available as <code>MPI_Fortran_&lt;binding&gt;_SUBARRAYS</code> and <code>MPI_Fortran_&lt;binding&gt;_ASYNCPROT</code>, where <code>&lt;binding&gt;</code> is one of <code>F77_HEADER</code>, <code>F90_MODULE</code> and <code>F08_MODULE</code>.</p>
<dt><code>MPI_DETERMINE_LIBRARY_VERSION</code></p>
<dd>For each language, find the output of <code>MPI_Get_library_version</code> and make it available as <code>MPI_&lt;lang&gt;_LIBRARY_VERSION_STRING</code>. This information is usually tied to the runtime component of an MPI implementation and might differ depending on <code>&lt;lang&gt;</code>. Note that the return value is entirely implementation defined. This information might be used to identify the MPI vendor and for example pick the correct one of multiple third party binaries that matches the MPI vendor.</dl>
<h3>Backward Compatibility</h3>
<p>Deprecated since version 3.10. </p>
<p> For backward compatibility with older versions of FindMPI, these variables are set: </p>
<pre>MPI_COMPILER MPI_LIBRARY MPI_EXTRA_LIBRARY
MPI_COMPILE_FLAGS MPI_INCLUDE_PATH MPI_LINK_FLAGS
MPI_LIBRARIES</pre>
<p>In new projects, please use the <code>MPI_&lt;lang&gt;_XXX</code> equivalents. Additionally, the following variables are deprecated:</p>
<dl>
<dt><code>MPI_&lt;lang&gt;_COMPILE_FLAGS</code></p>
<dd>Use <code>MPI_&lt;lang&gt;_COMPILE_OPTIONS</code> and <code>MPI_&lt;lang&gt;_COMPILE_DEFINITIONS</code> instead.</p>
<dt><code>MPI_&lt;lang&gt;_INCLUDE_PATH</code></p>
<dd>For consumption use <code>MPI_&lt;lang&gt;_INCLUDE_DIRS</code> and for specifying folders use <code>MPI_&lt;lang&gt;_ADDITIONAL_INCLUDE_DIRS</code> instead.</p>
<dt><code>MPIEXEC</code></p>
<dd>Use <code>MPIEXEC_EXECUTABLE</code> instead.</dl>
<h3>FindMsys</h3>
<p>New in version 3.21. </p>
<p> Find MSYS, a POSIX-compatible environment that runs natively on Microsoft Windows</p>
<h3>FindODBC</h3>
<p>New in version 3.12. </p>
<p> Find an Open Database Connectivity (ODBC) include directory and library. </p>
<p> On Windows, when building with Visual Studio, this module assumes the ODBC library is provided by the available Windows SDK. </p>
<p> On Unix, this module allows to search for ODBC library provided by unixODBC or iODBC implementations of ODBC API. This module reads hint about location of the config program:</p>
<dl>
<dt><code>ODBC_CONFIG</code></p>
<dd>Location of odbc_config or iodbc-config program </p>
<p> Otherwise, this module tries to find the config program, first from unixODBC, then from iODBC. If no config program found, this module searches for ODBC header and library in list of known locations.</dl>
<h3>Imported targets</h3>
<p>This module defines the following <code>IMPORTED</code> targets:</p>
<dl>
<dt><code>ODBC::ODBC</code></p>
<dd>Imported target for using the ODBC library, if found.</dl>
<h3>Result variables</h3>
<dl>
<dt><code>ODBC_FOUND</code></p>
<dd>Set to true if ODBC library found, otherwise false or undefined.</p>
<dt><code>ODBC_INCLUDE_DIRS</code></p>
<dd>Paths to include directories listed in one variable for use by ODBC client. May be empty on Windows, where the include directory corresponding to the expected Windows SDK is already available in the compilation environment.</p>
<dt><code>ODBC_LIBRARIES</code></p>
<dd>Paths to libraries to linked against to use ODBC. May just a library name on Windows, where the library directory corresponding to the expected Windows SDK is already available in the compilation environment.</p>
<dt><code>ODBC_CONFIG</code></p>
<dd>Path to unixODBC or iODBC config program, if found or specified.</dl>
<h3>Cache variables</h3>
<p>For users who wish to edit and control the module behavior, this module reads hints about search locations from the following variables:</p>
<dl>
<dt><code>ODBC_INCLUDE_DIR</code></p>
<dd>Path to ODBC include directory with <code>sql.h</code> header.</p>
<dt><code>ODBC_LIBRARY</code></p>
<dd>Path to ODBC library to be linked. </p>
<p> These variables should not be used directly by project code.</dl>
<h3>Limitations</h3>
<p>On Windows, this module does not search for iODBC. On Unix, there is no way to prefer unixODBC over iODBC, or vice versa, other than providing the config program location using the <code>ODBC_CONFIG</code>. This module does not allow to search for a specific ODBC driver.</p>
<h3>FindOpenACC</h3>
<p>New in version 3.10. </p>
<p> Detect OpenACC support by the compiler. </p>
<p> This module can be used to detect OpenACC support in a compiler. If the compiler supports OpenACC, the flags required to compile with OpenACC support are returned in variables for the different languages. Currently, only NVHPC, PGI, GNU and Cray compilers are supported.</p>
<h3>Imported Targets</h3>
<p>New in version 3.16. </p>
<p> The module provides <code>IMPORTED</code> targets:</p>
<dl>
<dt><code>OpenACC::OpenACC_&lt;lang&gt;</code></p>
<dd>Target for using OpenACC from <code>&lt;lang&gt;</code>.</dl>
<h3>Variables</h3>
<p>This module will set the following variables per language in your project, where <code>&lt;lang&gt;</code> is one of C, CXX, or Fortran:</p>
<dl>
<dt><code>OpenACC_&lt;lang&gt;_FOUND</code></p>
<dd>Variable indicating if OpenACC support for <code>&lt;lang&gt;</code> was detected.</p>
<dt><code>OpenACC_&lt;lang&gt;_FLAGS</code></p>
<dd>OpenACC compiler flags for <code>&lt;lang&gt;</code>, separated by spaces.</p>
<dt><code>OpenACC_&lt;lang&gt;_OPTIONS</code></p>
<dd>New in version 3.16. </p>
<p> OpenACC compiler flags for <code>&lt;lang&gt;</code>, as a list. Suitable for usage with target_compile_options or target_link_options. </p>
<p> The module will also try to provide the OpenACC version variables:</p>
<dt><code>OpenACC_&lt;lang&gt;_SPEC_DATE</code></p>
<dd>Date of the OpenACC specification implemented by the <code>&lt;lang&gt;</code> compiler.</p>
<dt><code>OpenACC_&lt;lang&gt;_VERSION_MAJOR</code></p>
<dd>Major version of OpenACC implemented by the <code>&lt;lang&gt;</code> compiler.</p>
<dt><code>OpenACC_&lt;lang&gt;_VERSION_MINOR</code></p>
<dd>Minor version of OpenACC implemented by the <code>&lt;lang&gt;</code> compiler.</p>
<dt><code>OpenACC_&lt;lang&gt;_VERSION</code></p>
<dd>OpenACC version implemented by the <code>&lt;lang&gt;</code> compiler. </p>
<p> The specification date is formatted as given in the OpenACC standard: <code>yyyymm</code> where <code>yyyy</code> and <code>mm</code> represents the year and month of the OpenACC specification implemented by the <code>&lt;lang&gt;</code> compiler.</dl>
<h3>Input Variables</h3>
<p><code>OpenACC_ACCEL_TARGET=&lt;target&gt;</code> If set, will the correct target accelerator flag set to the &lt;target&gt; will be returned with OpenACC_&lt;lang&gt;_FLAGS.</p>
<h3>FindOpenAL</h3>
<p>Finds Open Audio Library (OpenAL). </p>
<p> Projects using this module should use <code>#include &quot;al.h&quot;</code> to include the OpenAL header file, <code>not</code> <code>#include &lt;AL/al.h&gt;</code>. The reason for this is that the latter is not entirely portable. Windows/Creative Labs does not by default put their headers in <code>AL/</code> and macOS uses the convention <code>&lt;OpenAL/al.h&gt;</code>.</p>
<h3>Hints</h3>
<p>Environment variable <code>$OPENALDIR</code> can be used to set the prefix of OpenAL installation to be found. </p>
<p> By default on macOS, system framework is search first. In other words, OpenAL is searched in the following order:</p>
<dl>
<dt>1.</p>
<dd>System framework: <code>/System/Library/Frameworks</code>, whose priority can be changed via setting the <code>CMAKE_FIND_FRAMEWORK</code> variable.</p>
<dt>2.</p>
<dd>Environment variable <code>$OPENALDIR</code>.</p>
<dt>3.</p>
<dd>System paths.</p>
<dt>4.</p>
<dd>User-compiled framework: <code>~/Library/Frameworks</code>.</p>
<dt>5.</p>
<dd>Manually compiled framework: <code>/Library/Frameworks</code>.</p>
<dt>6.</p>
<dd>Add-on package: <code>/opt</code>.</dl>
<h3>Result Variables</h3>
<p>This module defines the following variables:</p>
<dl>
<dt><code>OPENAL_FOUND</code></p>
<dd>If false, do not try to link to OpenAL</p>
<dt><code>OPENAL_INCLUDE_DIR</code></p>
<dd>OpenAL include directory</p>
<dt><code>OPENAL_LIBRARY</code></p>
<dd>Path to the OpenAL library</p>
<dt><code>OPENAL_VERSION_STRING</code></p>
<dd>Human-readable string containing the version of OpenAL</dl>
<h3>FindOpenCL</h3>
<p>New in version 3.1. </p>
<p> Finds Open Computing Language (OpenCL) </p>
<p> New in version 3.10: Detection of OpenCL 2.1 and 2.2.</p>
<h3>IMPORTED Targets</h3>
<p>New in version 3.7. </p>
<p> This module defines <code>IMPORTED</code> target <code>OpenCL::OpenCL</code>, if OpenCL has been found.</p>
<h3>Result Variables</h3>
<p>This module defines the following variables: </p>
<pre>OpenCL_FOUND - True if OpenCL was found
OpenCL_INCLUDE_DIRS - include directories for OpenCL
OpenCL_LIBRARIES - link against this library to use OpenCL
OpenCL_VERSION_STRING - Highest supported OpenCL version (eg. 1.2)
OpenCL_VERSION_MAJOR - The major version of the OpenCL implementation
OpenCL_VERSION_MINOR - The minor version of the OpenCL implementation</pre>
<p>The module will also define two cache variables: </p>
<pre>OpenCL_INCLUDE_DIR - the OpenCL include directory
OpenCL_LIBRARY - the path to the OpenCL library</pre>
<h3>FindOpenGL</h3>
<p>FindModule for OpenGL and OpenGL Utility Library (GLU). </p>
<p> Changed in version 3.2: X11 is no longer added as a dependency on Unix/Linux systems. </p>
<p> New in version 3.10: GLVND support on Linux. See the <i>Linux-specific</i> section below.</p>
<h3>Optional COMPONENTS</h3>
<p>New in version 3.10. </p>
<p> This module respects several optional COMPONENTS: <code>EGL</code>, <code>GLX</code>, and <code>OpenGL</code>. There are corresponding import targets for each of these flags.</p>
<h3>IMPORTED Targets</h3>
<p>New in version 3.8. </p>
<p> This module defines the <code>IMPORTED</code> targets:</p>
<dl>
<dt><code>OpenGL::GL</code></p>
<dd>Defined to the platform-specific OpenGL libraries if the system has OpenGL.</p>
<dt><code>OpenGL::GLU</code></p>
<dd>Defined if the system has OpenGL Utility Library (GLU). </p>
<p> New in version 3.10: Additionally, the following GLVND-specific library targets are defined: </p>
<dt><code>OpenGL::OpenGL</code></p>
<dd>Defined to libOpenGL if the system is GLVND-based.</p>
<dt><code>OpenGL::GLX</code></p>
<dd>Defined if the system has OpenGL Extension to the X Window System (GLX).</p>
<dt><code>OpenGL::EGL</code></p>
<dd>Defined if the system has EGL.</dl>
<h3>Result Variables</h3>
<p>This module sets the following variables:</p>
<dl>
<dt><code>OPENGL_FOUND</code></p>
<dd>True, if the system has OpenGL and all components are found.</p>
<dt><code>OPENGL_XMESA_FOUND</code></p>
<dd>True, if the system has XMESA.</p>
<dt><code>OPENGL_GLU_FOUND</code></p>
<dd>True, if the system has GLU.</p>
<dt><code>OpenGL_OpenGL_FOUND</code></p>
<dd>True, if the system has an OpenGL library.</p>
<dt><code>OpenGL_GLX_FOUND</code></p>
<dd>True, if the system has GLX.</p>
<dt><code>OpenGL_EGL_FOUND</code></p>
<dd>True, if the system has EGL.</p>
<dt><code>OPENGL_INCLUDE_DIR</code></p>
<dd>Path to the OpenGL include directory.</p>
<dt><code>OPENGL_EGL_INCLUDE_DIRS</code></p>
<dd>Path to the EGL include directory.</p>
<dt><code>OPENGL_LIBRARIES</code></p>
<dd>Paths to the OpenGL library, windowing system libraries, and GLU libraries. On Linux, this assumes GLX and is never correct for EGL-based targets. Clients are encouraged to use the <code>OpenGL::*</code> import targets instead. </p>
<p> New in version 3.10: Variables for GLVND-specific libraries <code>OpenGL</code>, <code>EGL</code> and <code>GLX</code>. </p>
</dl>
<h3>Cache variables</h3>
<p>The following cache variables may also be set:</p>
<dl>
<dt><code>OPENGL_egl_LIBRARY</code></p>
<dd>Path to the EGL library.</p>
<dt><code>OPENGL_glu_LIBRARY</code></p>
<dd>Path to the GLU library.</p>
<dt><code>OPENGL_glx_LIBRARY</code></p>
<dd>Path to the GLVND &#8216;GLX&#8217; library.</p>
<dt><code>OPENGL_opengl_LIBRARY</code></p>
<dd>Path to the GLVND &#8216;OpenGL&#8217; library</p>
<dt><code>OPENGL_gl_LIBRARY</code></p>
<dd>Path to the OpenGL library. New code should prefer the <code>OpenGL::*</code> import targets. </p>
<p> New in version 3.10: Variables for GLVND-specific libraries <code>OpenGL</code>, <code>EGL</code> and <code>GLX</code>. </p>
</dl>
<h3>Linux-specific</h3>
<p>Some Linux systems utilize GLVND as a new ABI for OpenGL. GLVND separates context libraries from OpenGL itself; OpenGL lives in &quot;libOpenGL&quot;, and contexts are defined in &quot;libGLX&quot; or &quot;libEGL&quot;. GLVND is currently the only way to get OpenGL 3+ functionality via EGL in a manner portable across vendors. Projects may use GLVND explicitly with target <code>OpenGL::OpenGL</code> and either <code>OpenGL::GLX</code> or <code>OpenGL::EGL</code>. </p>
<p> Projects may use the <code>OpenGL::GL</code> target (or <code>OPENGL_LIBRARIES</code> variable) to use legacy GL interfaces. These will use the legacy GL library located by <code>OPENGL_gl_LIBRARY</code>, if available. If <code>OPENGL_gl_LIBRARY</code> is empty or not found and GLVND is available, the <code>OpenGL::GL</code> target will use GLVND <code>OpenGL::OpenGL</code> and <code>OpenGL::GLX</code> (and the <code>OPENGL_LIBRARIES</code> variable will use the corresponding libraries). Thus, for non-EGL-based Linux targets, the <code>OpenGL::GL</code> target is most portable. </p>
<p> A <code>OpenGL_GL_PREFERENCE</code> variable may be set to specify the preferred way to provide legacy GL interfaces in case multiple choices are available. The value may be one of:</p>
<dl>
<dt><code>GLVND</code></p>
<dd>If the GLVND OpenGL and GLX libraries are available, prefer them. This forces <code>OPENGL_gl_LIBRARY</code> to be empty. </p>
<p> Changed in version 3.11: This is the default, unless policy <code>CMP0072</code> is set to <code>OLD</code> and no components are requeted (since components correspond to GLVND libraries). </p>
<dt><code>LEGACY</code></p>
<dd>Prefer to use the legacy libGL library, if available. </p>
<p> For EGL targets the client must rely on GLVND support on the user&#8217;s system. Linking should use the <code>OpenGL::OpenGL OpenGL::EGL</code> targets. Using GLES* libraries is theoretically possible in place of <code>OpenGL::OpenGL</code>, but this module does not currently support that; contributions welcome. </p>
<p> <code>OPENGL_egl_LIBRARY</code> and <code>OPENGL_EGL_INCLUDE_DIRS</code> are defined in the case of GLVND. For non-GLVND Linux and other systems these are left undefined.</dl>
<h3>macOS-Specific</h3>
<p>On OSX FindOpenGL defaults to using the framework version of OpenGL. People will have to change the cache values of OPENGL_glu_LIBRARY and OPENGL_gl_LIBRARY to use OpenGL with X11 on OSX.</p>
<h3>FindOpenMP</h3>
<p>Finds Open Multi-Processing (OpenMP) support. </p>
<p> This module can be used to detect OpenMP support in a compiler. If the compiler supports OpenMP, the flags required to compile with OpenMP support are returned in variables for the different languages. The variables may be empty if the compiler does not need a special flag to support OpenMP. </p>
<p> New in version 3.5: Clang support.</p>
<h3>Variables</h3>
<p>New in version 3.10: The module exposes the components <code>C</code>, <code>CXX</code>, and <code>Fortran</code>. Each of these controls the various languages to search OpenMP support for. </p>
<p> Depending on the enabled components the following variables will be set:</p>
<dl>
<dt><code>OpenMP_FOUND</code></p>
<dd>Variable indicating that OpenMP flags for all requested languages have been found. If no components are specified, this is true if OpenMP settings for all enabled languages were detected.</p>
<dt><code>OpenMP_VERSION</code></p>
<dd>Minimal version of the OpenMP standard detected among the requested languages, or all enabled languages if no components were specified. </p>
<p> This module will set the following variables per language in your project, where <code>&lt;lang&gt;</code> is one of C, CXX, or Fortran:</p>
<dt><code>OpenMP_&lt;lang&gt;_FOUND</code></p>
<dd>Variable indicating if OpenMP support for <code>&lt;lang&gt;</code> was detected.</p>
<dt><code>OpenMP_&lt;lang&gt;_FLAGS</code></p>
<dd>OpenMP compiler flags for <code>&lt;lang&gt;</code>, separated by spaces.</p>
<dt><code>OpenMP_&lt;lang&gt;_INCLUDE_DIRS</code></p>
<dd>Directories that must be added to the header search path for <code>&lt;lang&gt;</code> when using OpenMP. </p>
<p> For linking with OpenMP code written in <code>&lt;lang&gt;</code>, the following variables are provided:</p>
<dt><code>OpenMP_&lt;lang&gt;_LIB_NAMES</code></p>
<dd>;-list of libraries for OpenMP programs for <code>&lt;lang&gt;</code>.</p>
<dt><code>OpenMP_&lt;libname&gt;_LIBRARY</code></p>
<dd>Location of the individual libraries needed for OpenMP support in <code>&lt;lang&gt;</code>.</p>
<dt><code>OpenMP_&lt;lang&gt;_LIBRARIES</code></p>
<dd>A list of libraries needed to link with OpenMP code written in <code>&lt;lang&gt;</code>. </p>
<p> Additionally, the module provides <code>IMPORTED</code> targets:</p>
<dt><code>OpenMP::OpenMP_&lt;lang&gt;</code></p>
<dd>Target for using OpenMP from <code>&lt;lang&gt;</code>. </p>
<p> Specifically for Fortran, the module sets the following variables:</p>
<dt><code>OpenMP_Fortran_HAVE_OMPLIB_HEADER</code></p>
<dd>Boolean indicating if OpenMP is accessible through <code>omp_lib.h</code>.</p>
<dt><code>OpenMP_Fortran_HAVE_OMPLIB_MODULE</code></p>
<dd>Boolean indicating if OpenMP is accessible through the <code>omp_lib</code> Fortran module. </p>
<p> The module will also try to provide the OpenMP version variables:</p>
<dt><code>OpenMP_&lt;lang&gt;_SPEC_DATE</code></p>
<dd>New in version 3.7. </p>
<p> Date of the OpenMP specification implemented by the <code>&lt;lang&gt;</code> compiler.</p>
<dt><code>OpenMP_&lt;lang&gt;_VERSION_MAJOR</code></p>
<dd>Major version of OpenMP implemented by the <code>&lt;lang&gt;</code> compiler.</p>
<dt><code>OpenMP_&lt;lang&gt;_VERSION_MINOR</code></p>
<dd>Minor version of OpenMP implemented by the <code>&lt;lang&gt;</code> compiler.</p>
<dt><code>OpenMP_&lt;lang&gt;_VERSION</code></p>
<dd>OpenMP version implemented by the <code>&lt;lang&gt;</code> compiler. </p>
<p> The specification date is formatted as given in the OpenMP standard: <code>yyyymm</code> where <code>yyyy</code> and <code>mm</code> represents the year and month of the OpenMP specification implemented by the <code>&lt;lang&gt;</code> compiler. </p>
<p> For some compilers, it may be necessary to add a header search path to find the relevant OpenMP headers. This location may be language-specific. Where this is needed, the module may attempt to find the location, but it can be provided directly by setting the <code>OpenMP_&lt;lang&gt;_INCLUDE_DIR</code> cache variable. Note that this variable is an _input_ control to the module. Project code should use the <code>OpenMP_&lt;lang&gt;_INCLUDE_DIRS</code> _output_ variable if it needs to know what include directories are needed.</dl>
<h3>FindOpenSceneGraph</h3>
<p>Find OpenSceneGraph (3D graphics application programming interface) </p>
<p> This module searches for the OpenSceneGraph core &quot;osg&quot; library as well as <code>FindOpenThreads</code>, and whatever additional <code>COMPONENTS</code> (nodekits) that you specify. </p>
<pre>See <a rel="nofollow" href="http://www.openscenegraph.org">http://www.openscenegraph.org</a></pre>
<p>NOTE: To use this module effectively you must either require <code>CMake &gt;= 2.6.3</code> with <code>cmake_minimum_required(VERSION 2.6.3)</code> or download and place <code>FindOpenThreads</code>, <code>Findosg</code> functions, <code>Findosg</code> and <code>Find&lt;etc&gt;.cmake</code> files into your <code>CMAKE_MODULE_PATH</code>. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<p> This module accepts the following variables (note mixed case) </p>
<pre>OpenSceneGraph_DEBUG - Enable debugging output</pre>
<pre>OpenSceneGraph_MARK_AS_ADVANCED - Mark cache variables as advanced
 automatically</pre>
<p>The following environment variables are also respected for finding the OSG and it&#8217;s various components. <code>CMAKE_PREFIX_PATH</code> can also be used for this (see <code>find_library()</code> CMake documentation).</p>
<dl>
<dt><code>&lt;MODULE&gt;_DIR</code></p>
<dd>(where <code>MODULE</code> is of the form &quot;OSGVOLUME&quot; and there is a <code>FindosgVolume</code>.cmake` file)</p>
<dt><code>OSG_DIR</code></p>
<dd>
<dt><code>OSGDIR</code></p>
<dd>
<dt><code>OSG_ROOT</code></p>
<dd>[CMake 2.8.10]: The CMake variable <code>OSG_DIR</code> can now be used as well to influence detection, instead of needing to specify an environment variable. </p>
<p> This module defines the following output variables: </p>
<pre>OPENSCENEGRAPH_FOUND - Was the OSG and all of the specified components found?</pre>
<pre>OPENSCENEGRAPH_VERSION - The version of the OSG which was found</pre>
<pre>OPENSCENEGRAPH_INCLUDE_DIRS - Where to find the headers</pre>
<pre>OPENSCENEGRAPH_LIBRARIES - The OSG libraries</pre>
<p>================================== Example Usage: </p>
<pre>find_package(OpenSceneGraph 2.0.0 REQUIRED osgDB osgUtil)
 # libOpenThreads &amp; libosg automatically searched
include_directories(${OPENSCENEGRAPH_INCLUDE_DIRS})</pre>
<pre>add_executable(foo foo.cc)
target_link_libraries(foo ${OPENSCENEGRAPH_LIBRARIES})</pre>
</dl>
<h3>FindOpenSSL</h3>
<p>Find the OpenSSL encryption library. </p>
<p> This module finds an installed OpenSSL library and determines its version. </p>
<p> New in version 3.19: When a version is requested, it can be specified as a simple value or as a range. For a detailed description of version range usage and capabilities, refer to the <code>find_package()</code> command. </p>
<p> New in version 3.18: Support for OpenSSL 3.0.</p>
<h3>Optional COMPONENTS</h3>
<p>New in version 3.12. </p>
<p> This module supports two optional COMPONENTS: <code>Crypto</code> and <code>SSL</code>. Both components have associated imported targets, as described below.</p>
<h3>Imported Targets</h3>
<p>New in version 3.4. </p>
<p> This module defines the following <code>IMPORTED</code> targets:</p>
<dl>
<dt><code>OpenSSL::SSL</code></p>
<dd>The OpenSSL <code>ssl</code> library, if found.</p>
<dt><code>OpenSSL::Crypto</code></p>
<dd>The OpenSSL <code>crypto</code> library, if found.</p>
<dt><code>OpenSSL::applink</code></p>
<dd>New in version 3.18. </p>
<p> The OpenSSL <code>applink</code> components that might be need to be compiled into projects under MSVC. This target is available only if found OpenSSL version is not less than 0.9.8. By linking this target the above OpenSSL targets can be linked even if the project has different MSVC runtime configurations with the above OpenSSL targets. This target has no effect on platforms other than MSVC. </p>
<p> NOTE: Due to how <code>INTERFACE_SOURCES</code> are consumed by the consuming target, unless you certainly know what you are doing, it is always preferred to link <code>OpenSSL::applink</code> target as <code>PRIVATE</code> and to make sure that this target is linked at most once for the whole dependency graph of any library or executable: </p>
<pre>target_link_libraries(myTarget PRIVATE OpenSSL::applink)</pre>
<p>Otherwise you would probably encounter unexpected random problems when building and linking, as both the ISO C and the ISO C++ standard claims almost nothing about what a link process should be.</dl>
<h3>Result Variables</h3>
<p>This module will set the following variables in your project:</p>
<dl>
<dt><code>OPENSSL_FOUND</code></p>
<dd>System has the OpenSSL library. If no components are requested it only requires the crypto library.</p>
<dt><code>OPENSSL_INCLUDE_DIR</code></p>
<dd>The OpenSSL include directory.</p>
<dt><code>OPENSSL_CRYPTO_LIBRARY</code></p>
<dd>The OpenSSL crypto library.</p>
<dt><code>OPENSSL_CRYPTO_LIBRARIES</code></p>
<dd>The OpenSSL crypto library and its dependencies.</p>
<dt><code>OPENSSL_SSL_LIBRARY</code></p>
<dd>The OpenSSL SSL library.</p>
<dt><code>OPENSSL_SSL_LIBRARIES</code></p>
<dd>The OpenSSL SSL library and its dependencies.</p>
<dt><code>OPENSSL_LIBRARIES</code></p>
<dd>All OpenSSL libraries and their dependencies.</p>
<dt><code>OPENSSL_VERSION</code></p>
<dd>This is set to <code>$major.$minor.$revision$patch</code> (e.g. <code>0.9.8s</code>).</p>
<dt><code>OPENSSL_APPLINK_SOURCE</code></p>
<dd>The sources in the target <code>OpenSSL::applink</code> that is mentioned above. This variable shall always be undefined if found openssl version is less than 0.9.8 or if platform is not MSVC.</dl>
<h3>Hints</h3>
<p>Set <code>OPENSSL_ROOT_DIR</code> to the root directory of an OpenSSL installation. </p>
<p> New in version 3.4: Set <code>OPENSSL_USE_STATIC_LIBS</code> to <code>TRUE</code> to look for static libraries. </p>
<p> New in version 3.5: Set <code>OPENSSL_MSVC_STATIC_RT</code> set <code>TRUE</code> to choose the MT version of the lib.</p>
<h3>FindOpenThreads</h3>
<p>OpenThreads is a C++ based threading library. Its largest userbase seems to OpenSceneGraph so you might notice I accept OSGDIR as an environment path. I consider this part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. </p>
<p> Locate OpenThreads This module defines OPENTHREADS_LIBRARY OPENTHREADS_FOUND, if false, do not try to link to OpenThreads OPENTHREADS_INCLUDE_DIR, where to find the headers </p>
<p> $OPENTHREADS_DIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OPENTHREADS_DIR used in building osg. </p>
<p> [CMake 2.8.10]: The CMake variables OPENTHREADS_DIR or OSG_DIR can now be used as well to influence detection, instead of needing to specify an environment variable. </p>
<p> Created by Eric Wing.</p>
<h3>Findosg</h3>
<p>NOTE: It is highly recommended that you use the new FindOpenSceneGraph.cmake introduced in CMake 2.6.3 and not use this Find module directly. </p>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osg This module defines </p>
<p> OSG_FOUND &#8211; Was the Osg found? OSG_INCLUDE_DIR &#8211; Where to find the headers OSG_LIBRARIES &#8211; The libraries to link against for the OSG (use this) </p>
<p> OSG_LIBRARY &#8211; The OSG library OSG_LIBRARY_DEBUG &#8211; The OSG debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing.</p>
<h3>Findosg_functions</h3>
<p>This CMake file contains two macros to assist with searching for OSG libraries and nodekits. Please see FindOpenSceneGraph.cmake for full documentation.</p>
<h3>FindosgAnimation</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgAnimation This module defines </p>
<p> OSGANIMATION_FOUND &#8211; Was osgAnimation found? OSGANIMATION_INCLUDE_DIR &#8211; Where to find the headers OSGANIMATION_LIBRARIES &#8211; The libraries to link against for the OSG (use this) </p>
<p> OSGANIMATION_LIBRARY &#8211; The OSG library OSGANIMATION_LIBRARY_DEBUG &#8211; The OSG debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing.</p>
<h3>FindosgDB</h3>
<p>This is part of the <code>Findosg*</code> suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default <code>FindOpenGL</code> module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the <code>FindOpenSceneGraph</code> instead of the <code>Findosg*.cmake</code> modules. </p>
<p> Locate osgDB This module defines:</p>
<dl>
<dt><code>OSGDB_FOUND</code></p>
<dd>Was osgDB found?</p>
<dt><code>OSGDB_INCLUDE_DIR</code></p>
<dd>Where to find the headers</p>
<dt><code>OSGDB_LIBRARIES</code></p>
<dd>The libraries to link against for the osgDB</p>
<dt><code>OSGDB_LIBRARY</code></p>
<dd>The osgDB library</p>
<dt><code>OSGDB_LIBRARY_DEBUG</code></p>
<dd>The osgDB debug library </p>
<p> <code>$OSGDIR</code> is an environment variable that would correspond to: </p>
<pre>./configure --prefix=$OSGDIR used in building osg.</pre>
</dl>
<h3>FindosgFX</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgFX This module defines </p>
<p> OSGFX_FOUND &#8211; Was osgFX found? OSGFX_INCLUDE_DIR &#8211; Where to find the headers OSGFX_LIBRARIES &#8211; The libraries to link against for the osgFX (use this) </p>
<p> OSGFX_LIBRARY &#8211; The osgFX library OSGFX_LIBRARY_DEBUG &#8211; The osgFX debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing.</p>
<h3>FindosgGA</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgGA This module defines </p>
<p> OSGGA_FOUND &#8211; Was osgGA found? OSGGA_INCLUDE_DIR &#8211; Where to find the headers OSGGA_LIBRARIES &#8211; The libraries to link against for the osgGA (use this) </p>
<p> OSGGA_LIBRARY &#8211; The osgGA library OSGGA_LIBRARY_DEBUG &#8211; The osgGA debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing.</p>
<h3>FindosgIntrospection</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgINTROSPECTION This module defines </p>
<p> OSGINTROSPECTION_FOUND &#8211; Was osgIntrospection found? OSGINTROSPECTION_INCLUDE_DIR &#8211; Where to find the headers OSGINTROSPECTION_LIBRARIES &#8211; The libraries to link for osgIntrospection (use this) </p>
<p> OSGINTROSPECTION_LIBRARY &#8211; The osgIntrospection library OSGINTROSPECTION_LIBRARY_DEBUG &#8211; The osgIntrospection debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing.</p>
<h3>FindosgManipulator</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgManipulator This module defines </p>
<p> OSGMANIPULATOR_FOUND &#8211; Was osgManipulator found? OSGMANIPULATOR_INCLUDE_DIR &#8211; Where to find the headers OSGMANIPULATOR_LIBRARIES &#8211; The libraries to link for osgManipulator (use this) </p>
<p> OSGMANIPULATOR_LIBRARY &#8211; The osgManipulator library OSGMANIPULATOR_LIBRARY_DEBUG &#8211; The osgManipulator debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing.</p>
<h3>FindosgParticle</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgParticle This module defines </p>
<p> OSGPARTICLE_FOUND &#8211; Was osgParticle found? OSGPARTICLE_INCLUDE_DIR &#8211; Where to find the headers OSGPARTICLE_LIBRARIES &#8211; The libraries to link for osgParticle (use this) </p>
<p> OSGPARTICLE_LIBRARY &#8211; The osgParticle library OSGPARTICLE_LIBRARY_DEBUG &#8211; The osgParticle debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing.</p>
<h3>FindosgPresentation</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgPresentation This module defines </p>
<p> OSGPRESENTATION_FOUND &#8211; Was osgPresentation found? OSGPRESENTATION_INCLUDE_DIR &#8211; Where to find the headers OSGPRESENTATION_LIBRARIES &#8211; The libraries to link for osgPresentation (use this) </p>
<p> OSGPRESENTATION_LIBRARY &#8211; The osgPresentation library OSGPRESENTATION_LIBRARY_DEBUG &#8211; The osgPresentation debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. Modified to work with osgPresentation by Robert Osfield, January 2012.</p>
<h3>FindosgProducer</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgProducer This module defines </p>
<p> OSGPRODUCER_FOUND &#8211; Was osgProducer found? OSGPRODUCER_INCLUDE_DIR &#8211; Where to find the headers OSGPRODUCER_LIBRARIES &#8211; The libraries to link for osgProducer (use this) </p>
<p> OSGPRODUCER_LIBRARY &#8211; The osgProducer library OSGPRODUCER_LIBRARY_DEBUG &#8211; The osgProducer debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing.</p>
<h3>FindosgQt</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgQt This module defines </p>
<p> OSGQT_FOUND &#8211; Was osgQt found? OSGQT_INCLUDE_DIR &#8211; Where to find the headers OSGQT_LIBRARIES &#8211; The libraries to link for osgQt (use this) </p>
<p> OSGQT_LIBRARY &#8211; The osgQt library OSGQT_LIBRARY_DEBUG &#8211; The osgQt debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. Modified to work with osgQt by Robert Osfield, January 2012.</p>
<h3>FindosgShadow</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgShadow This module defines </p>
<p> OSGSHADOW_FOUND &#8211; Was osgShadow found? OSGSHADOW_INCLUDE_DIR &#8211; Where to find the headers OSGSHADOW_LIBRARIES &#8211; The libraries to link for osgShadow (use this) </p>
<p> OSGSHADOW_LIBRARY &#8211; The osgShadow library OSGSHADOW_LIBRARY_DEBUG &#8211; The osgShadow debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing.</p>
<h3>FindosgSim</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgSim This module defines </p>
<p> OSGSIM_FOUND &#8211; Was osgSim found? OSGSIM_INCLUDE_DIR &#8211; Where to find the headers OSGSIM_LIBRARIES &#8211; The libraries to link for osgSim (use this) </p>
<p> OSGSIM_LIBRARY &#8211; The osgSim library OSGSIM_LIBRARY_DEBUG &#8211; The osgSim debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing.</p>
<h3>FindosgTerrain</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgTerrain This module defines </p>
<p> OSGTERRAIN_FOUND &#8211; Was osgTerrain found? OSGTERRAIN_INCLUDE_DIR &#8211; Where to find the headers OSGTERRAIN_LIBRARIES &#8211; The libraries to link for osgTerrain (use this) </p>
<p> OSGTERRAIN_LIBRARY &#8211; The osgTerrain library OSGTERRAIN_LIBRARY_DEBUG &#8211; The osgTerrain debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing.</p>
<h3>FindosgText</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgText This module defines </p>
<p> OSGTEXT_FOUND &#8211; Was osgText found? OSGTEXT_INCLUDE_DIR &#8211; Where to find the headers OSGTEXT_LIBRARIES &#8211; The libraries to link for osgText (use this) </p>
<p> OSGTEXT_LIBRARY &#8211; The osgText library OSGTEXT_LIBRARY_DEBUG &#8211; The osgText debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing.</p>
<h3>FindosgUtil</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgUtil This module defines </p>
<p> OSGUTIL_FOUND &#8211; Was osgUtil found? OSGUTIL_INCLUDE_DIR &#8211; Where to find the headers OSGUTIL_LIBRARIES &#8211; The libraries to link for osgUtil (use this) </p>
<p> OSGUTIL_LIBRARY &#8211; The osgUtil library OSGUTIL_LIBRARY_DEBUG &#8211; The osgUtil debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing.</p>
<h3>FindosgViewer</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgViewer This module defines </p>
<p> OSGVIEWER_FOUND &#8211; Was osgViewer found? OSGVIEWER_INCLUDE_DIR &#8211; Where to find the headers OSGVIEWER_LIBRARIES &#8211; The libraries to link for osgViewer (use this) </p>
<p> OSGVIEWER_LIBRARY &#8211; The osgViewer library OSGVIEWER_LIBRARY_DEBUG &#8211; The osgViewer debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing.</p>
<h3>FindosgVolume</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgVolume This module defines </p>
<p> OSGVOLUME_FOUND &#8211; Was osgVolume found? OSGVOLUME_INCLUDE_DIR &#8211; Where to find the headers OSGVOLUME_LIBRARIES &#8211; The libraries to link for osgVolume (use this) </p>
<p> OSGVOLUME_LIBRARY &#8211; The osgVolume library OSGVOLUME_LIBRARY_DEBUG &#8211; The osgVolume debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing.</p>
<h3>FindosgWidget</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgWidget This module defines </p>
<p> OSGWIDGET_FOUND &#8211; Was osgWidget found? OSGWIDGET_INCLUDE_DIR &#8211; Where to find the headers OSGWIDGET_LIBRARIES &#8211; The libraries to link for osgWidget (use this) </p>
<p> OSGWIDGET_LIBRARY &#8211; The osgWidget library OSGWIDGET_LIBRARY_DEBUG &#8211; The osgWidget debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> FindosgWidget.cmake tweaked from Findosg* suite as created by Eric Wing.</p>
<h3>FindPatch</h3>
<p>New in version 3.10. </p>
<p> The module defines the following variables:</p>
<dl>
<dt><code>Patch_EXECUTABLE</code></p>
<dd>Path to patch command-line executable.</p>
<dt><code>Patch_FOUND</code></p>
<dd>True if the patch command-line executable was found. </p>
<p> The following <code>IMPORTED</code> targets are also defined:</p>
<dt><code>Patch::patch</code></p>
<dd>The command-line executable. </p>
<p> Example usage: </p>
<pre>find_package(Patch)
if(Patch_FOUND)
 message(&quot;Patch found: ${Patch_EXECUTABLE}&quot;)
endif()</pre>
</dl>
<h3>FindPerl</h3>
<p>Find perl </p>
<p> this module looks for Perl </p>
<pre>PERL_EXECUTABLE - the full path to perl
PERL_FOUND - If false, don't attempt to use perl.
PERL_VERSION_STRING - version of perl found (since CMake 2.8.8)</pre>
<h3>FindPerlLibs</h3>
<p>Find Perl libraries </p>
<p> This module finds if PERL is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>PERLLIBS_FOUND = True if perl.h &amp; libperl were found
PERL_INCLUDE_PATH = path to where perl.h is found
PERL_LIBRARY = path to libperl
PERL_EXECUTABLE = full path to the perl binary</pre>
<p>The minimum required version of Perl can be specified using the standard syntax, e.g. find_package(PerlLibs 6.0) </p>
<pre>The following variables are also available if needed
(introduced after CMake 2.6.4)</pre>
<pre>PERL_SITESEARCH = path to the sitesearch install dir (-V:installsitesearch)
PERL_SITEARCH = path to the sitelib install directory (-V:installsitearch)
PERL_SITELIB = path to the sitelib install directory (-V:installsitelib)
PERL_VENDORARCH = path to the vendor arch install directory (-V:installvendorarch)
PERL_VENDORLIB = path to the vendor lib install directory (-V:installvendorlib)
PERL_ARCHLIB = path to the core arch lib install directory (-V:archlib)
PERL_PRIVLIB = path to the core priv lib install directory (-V:privlib)
PERL_UPDATE_ARCHLIB = path to the update arch lib install directory (-V:installarchlib)
PERL_UPDATE_PRIVLIB = path to the update priv lib install directory (-V:installprivlib)
PERL_EXTRA_C_FLAGS = Compilation flags used to build perl</pre>
<h3>FindPHP4</h3>
<p>Find PHP4 </p>
<p> This module finds if PHP4 is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>PHP4_INCLUDE_PATH = path to where php.h can be found
PHP4_EXECUTABLE = full path to the php4 binary</pre>
<h3>FindPhysFS</h3>
<p>Locate PhysFS library This module defines PHYSFS_LIBRARY, the name of the library to link against PHYSFS_FOUND, if false, do not try to link to PHYSFS PHYSFS_INCLUDE_DIR, where to find physfs.h </p>
<p> $PHYSFSDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$PHYSFSDIR used in building PHYSFS. </p>
<p> Created by Eric Wing.</p>
<h3>FindPike</h3>
<p>Find Pike </p>
<p> This module finds if PIKE is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>PIKE_INCLUDE_PATH = path to where program.h is found
PIKE_EXECUTABLE = full path to the pike binary</pre>
<h3>FindPkgConfig</h3>
<p>A <code>pkg-config</code> module for CMake. </p>
<p> Finds the <code>pkg-config</code> executable and adds the <i>pkg_get_variable()</i>, <i>pkg_check_modules()</i> and <i>pkg_search_module()</i> commands. The following variables will also be set:</p>
<dl>
<dt><code>PKG_CONFIG_FOUND</code></p>
<dd>True if a pkg-config executable was found.</p>
<dt><code>PKG_CONFIG_VERSION_STRING</code></p>
<dd>New in version 2.8.8. </p>
<p> The version of pkg-config that was found.</p>
<dt><code>PKG_CONFIG_EXECUTABLE</code></p>
<dd>The pathname of the pkg-config program.</p>
<dt><code>PKG_CONFIG_ARGN</code></p>
<dd>New in version 3.22. </p>
<p> A list of arguments to pass to pkg-config. </p>
<p> Both <code>PKG_CONFIG_EXECUTABLE</code> and <code>PKG_CONFIG_ARGN</code> are initialized by the module, but may be overridden by the user. See <i>Variables Affecting Behavior</i> for how these variables are initialized.</p>
<dt><code>pkg_check_modules</code></p>
<dd>Checks for all the given modules, setting a variety of result variables in the calling scope. </p>
<pre>pkg_check_modules(&lt;prefix&gt;
 [REQUIRED] [QUIET]
 [NO_CMAKE_PATH]
 [NO_CMAKE_ENVIRONMENT_PATH]
 [IMPORTED_TARGET [GLOBAL]]
 &lt;moduleSpec&gt; [&lt;moduleSpec&gt;...])</pre>
<p>When the <code>REQUIRED</code> argument is given, the command will fail with an error if module(s) could not be found. </p>
<p> When the <code>QUIET</code> argument is given, no status messages will be printed. </p>
<p> New in version 3.1: The <code>CMAKE_PREFIX_PATH</code>, <code>CMAKE_FRAMEWORK_PATH</code>, and <code>CMAKE_APPBUNDLE_PATH</code> cache and environment variables will be added to the <code>pkg-config</code> search path. The <code>NO_CMAKE_PATH</code> and <code>NO_CMAKE_ENVIRONMENT_PATH</code> arguments disable this behavior for the cache variables and environment variables respectively. The <i>PKG_CONFIG_USE_CMAKE_PREFIX_PATH</i> variable set to <code>FALSE</code> disables this behavior globally. </p>
<p> New in version 3.6: The <code>IMPORTED_TARGET</code> argument will create an imported target named <code>PkgConfig::&lt;prefix&gt;</code> that can be passed directly as an argument to <code>target_link_libraries()</code>. </p>
<p> New in version 3.13: The <code>GLOBAL</code> argument will make the imported target available in global scope. </p>
<p> New in version 3.15: Non-library linker options reported by <code>pkg-config</code> are stored in the <code>INTERFACE_LINK_OPTIONS</code> target property. </p>
<p> Changed in version 3.18: Include directories specified with <code>-isystem</code> are stored in the <code>INTERFACE_INCLUDE_DIRECTORIES</code> target property. Previous versions of CMake left them in the <code>INTERFACE_COMPILE_OPTIONS</code> property. </p>
<p> Each <code>&lt;moduleSpec&gt;</code> can be either a bare module name or it can be a module name with a version constraint (operators <code>=</code>, <code>&lt;</code>, <code>&gt;</code>, <code>&lt;=</code> and <code>&gt;=</code> are supported). The following are examples for a module named <code>foo</code> with various constraints:</p>
<dt>&bull;</p>
<dd><code>foo</code> matches any version.</p>
<dt>&bull;</p>
<dd><code>foo&lt;2</code> only matches versions before 2.</p>
<dt>&bull;</p>
<dd><code>foo&gt;=3.1</code> matches any version from 3.1 or later.</p>
<dt>&bull;</p>
<dd><code>foo=1.2.3</code> requires that foo must be exactly version 1.2.3. </p>
<p> The following variables may be set upon return. Two sets of values exist: One for the common case (<code>&lt;XXX&gt; = &lt;prefix&gt;</code>) and another for the information <code>pkg-config</code> provides when called with the <code>&#8211;static</code> option (<code>&lt;XXX&gt; = &lt;prefix&gt;_STATIC</code>).</p>
<dt><code>&lt;XXX&gt;_FOUND</code></p>
<dd>set to 1 if module(s) exist</p>
<dt><code>&lt;XXX&gt;_LIBRARIES</code></p>
<dd>only the libraries (without the &#8216;-l&#8217;)</p>
<dt><code>&lt;XXX&gt;_LINK_LIBRARIES</code></p>
<dd>the libraries and their absolute paths</p>
<dt><code>&lt;XXX&gt;_LIBRARY_DIRS</code></p>
<dd>the paths of the libraries (without the &#8216;-L&#8217;)</p>
<dt><code>&lt;XXX&gt;_LDFLAGS</code></p>
<dd>all required linker flags</p>
<dt><code>&lt;XXX&gt;_LDFLAGS_OTHER</code></p>
<dd>all other linker flags</p>
<dt><code>&lt;XXX&gt;_INCLUDE_DIRS</code></p>
<dd>the &#8216;-I&#8217; preprocessor flags (without the &#8216;-I&#8217;)</p>
<dt><code>&lt;XXX&gt;_CFLAGS</code></p>
<dd>all required cflags</p>
<dt><code>&lt;XXX&gt;_CFLAGS_OTHER</code></p>
<dd>the other compiler flags </p>
<p> All but <code>&lt;XXX&gt;_FOUND</code> may be a ;-list if the associated variable returned from <code>pkg-config</code> has multiple values. </p>
<p> Changed in version 3.18: Include directories specified with <code>-isystem</code> are stored in the <code>&lt;XXX&gt;_INCLUDE_DIRS</code> variable. Previous versions of CMake left them in <code>&lt;XXX&gt;_CFLAGS_OTHER</code>. </p>
<p> There are some special variables whose prefix depends on the number of <code>&lt;moduleSpec&gt;</code> given. When there is only one <code>&lt;moduleSpec&gt;</code>, <code>&lt;YYY&gt;</code> will simply be <code>&lt;prefix&gt;</code>, but if two or more <code>&lt;moduleSpec&gt;</code> items are given, <code>&lt;YYY&gt;</code> will be <code>&lt;prefix&gt;_&lt;moduleName&gt;</code>.</p>
<dt><code>&lt;YYY&gt;_VERSION</code></p>
<dd>version of the module</p>
<dt><code>&lt;YYY&gt;_PREFIX</code></p>
<dd>prefix directory of the module</p>
<dt><code>&lt;YYY&gt;_INCLUDEDIR</code></p>
<dd>include directory of the module</p>
<dt><code>&lt;YYY&gt;_LIBDIR</code></p>
<dd>lib directory of the module </p>
<p> Changed in version 3.8: For any given <code>&lt;prefix&gt;</code>, <code>pkg_check_modules()</code> can be called multiple times with different parameters. Previous versions of CMake cached and returned the first successful result. </p>
<p> Changed in version 3.16: If a full path to the found library can&#8217;t be determined, but it&#8217;s still visible to the linker, pass it through as <code>-l&lt;name&gt;</code>. Previous versions of CMake failed in this case. </p>
<p> Examples: </p>
<pre>pkg_check_modules (GLIB2 glib-2.0)</pre>
<p>Looks for any version of glib2. If found, the output variable <code>GLIB2_VERSION</code> will hold the actual version found. </p>
<pre>pkg_check_modules (GLIB2 glib-2.0&gt;=2.10)</pre>
<p>Looks for at least version 2.10 of glib2. If found, the output variable <code>GLIB2_VERSION</code> will hold the actual version found. </p>
<pre>pkg_check_modules (FOO glib-2.0&gt;=2.10 gtk+-2.0)</pre>
<p>Looks for both glib2-2.0 (at least version 2.10) and any version of gtk2+-2.0. Only if both are found will <code>FOO</code> be considered found. The <code>FOO_glib-2.0_VERSION</code> and <code>FOO_gtk+-2.0_VERSION</code> variables will be set to their respective found module versions. </p>
<pre>pkg_check_modules (XRENDER REQUIRED xrender)</pre>
<p>Requires any version of <code>xrender</code>. Example output variables set by a successful call: </p>
<pre>XRENDER_LIBRARIES=Xrender;X11
XRENDER_STATIC_LIBRARIES=Xrender;X11;pthread;Xau;Xdmcp</pre>
<dt><code>pkg_search_module</code></p>
<dd>The behavior of this command is the same as <i>pkg_check_modules()</i>, except that rather than checking for all the specified modules, it searches for just the first successful match. </p>
<pre>pkg_search_module(&lt;prefix&gt;
 [REQUIRED] [QUIET]
 [NO_CMAKE_PATH]
 [NO_CMAKE_ENVIRONMENT_PATH]
 [IMPORTED_TARGET [GLOBAL]]
 &lt;moduleSpec&gt; [&lt;moduleSpec&gt;...])</pre>
<p>New in version 3.16: If a module is found, the <code>&lt;prefix&gt;_MODULE_NAME</code> variable will contain the name of the matching module. This variable can be used if you need to run <i>pkg_get_variable()</i>. </p>
<p> Example: </p>
<pre>pkg_search_module (BAR libxml-2.0 libxml2 libxml&gt;=2)</pre>
<dt><code>pkg_get_variable</code></p>
<dd>New in version 3.4. </p>
<p> Retrieves the value of a pkg-config variable <code>varName</code> and stores it in the result variable <code>resultVar</code> in the calling scope. </p>
<pre>pkg_get_variable(&lt;resultVar&gt; &lt;moduleName&gt; &lt;varName&gt;)</pre>
<p>If <code>pkg-config</code> returns multiple values for the specified variable, <code>resultVar</code> will contain a ;-list. </p>
<p> For example: </p>
<pre>pkg_get_variable(GI_GIRDIR gobject-introspection-1.0 girdir)</pre>
</dl>
<h3>Variables Affecting Behavior</h3>
<dl>
<dt><code>PKG_CONFIG_EXECUTABLE</code></p>
<dd>This cache variable can be set to the path of the pkg-config executable. <code>find_program()</code> is called internally by the module with this variable. </p>
<p> New in version 3.1: The <code>PKG_CONFIG</code> environment variable can be used as a hint if <code>PKG_CONFIG_EXECUTABLE</code> has not yet been set. </p>
<p> Changed in version 3.22: If the <code>PKG_CONFIG</code> environment variable is set, only the first argument is taken from it when using it as a hint. </p>
<dt><code>PKG_CONFIG_ARGN</code></p>
<dd>New in version 3.22. </p>
<p> This cache variable can be set to a list of arguments to additionally pass to pkg-config if needed. If not provided, it will be initialized from the <code>PKG_CONFIG</code> environment variable, if set. The first argument in that environment variable is assumed to be the pkg-config program, while all remaining arguments after that are used to initialize <code>PKG_CONFIG_ARGN</code>. If no such environment variable is defined, <code>PKG_CONFIG_ARGN</code> is initialized to an empty string. The module does not update the variable once it has been set in the cache.</p>
<dt><code>PKG_CONFIG_USE_CMAKE_PREFIX_PATH</code></p>
<dd>New in version 3.1. </p>
<p> Specifies whether <i>pkg_check_modules()</i> and <i>pkg_search_module()</i> should add the paths in the <code>CMAKE_PREFIX_PATH</code>, <code>CMAKE_FRAMEWORK_PATH</code> and <code>CMAKE_APPBUNDLE_PATH</code> cache and environment variables to the <code>pkg-config</code> search path. </p>
<p> If this variable is not set, this behavior is enabled by default if <code>CMAKE_MINIMUM_REQUIRED_VERSION</code> is 3.1 or later, disabled otherwise.</dl>
<h3>FindPNG</h3>
<p>Find libpng, the official reference library for the PNG image format.</p>
<h3>Imported targets</h3>
<p>New in version 3.5. </p>
<p> This module defines the following <code>IMPORTED</code> target:</p>
<dl>
<dt><code>PNG::PNG</code></p>
<dd>The libpng library, if found.</dl>
<h3>Result variables</h3>
<p>This module will set the following variables in your project:</p>
<dl>
<dt><code>PNG_INCLUDE_DIRS</code></p>
<dd>where to find png.h, etc.</p>
<dt><code>PNG_LIBRARIES</code></p>
<dd>the libraries to link against to use PNG.</p>
<dt><code>PNG_DEFINITIONS</code></p>
<dd>You should add_definitions(${PNG_DEFINITIONS}) before compiling code that includes png library files.</p>
<dt><code>PNG_FOUND</code></p>
<dd>If false, do not try to use PNG.</p>
<dt><code>PNG_VERSION_STRING</code></p>
<dd>the version of the PNG library found (since CMake 2.8.8)</dl>
<h3>Obsolete variables</h3>
<p>The following variables may also be set, for backwards compatibility:</p>
<dl>
<dt><code>PNG_LIBRARY</code></p>
<dd>where to find the PNG library.</p>
<dt><code>PNG_INCLUDE_DIR</code></p>
<dd>where to find the PNG headers (same as PNG_INCLUDE_DIRS) </p>
<p> Since PNG depends on the ZLib compression library, none of the above will be defined unless ZLib can be found.</dl>
<h3>FindPostgreSQL</h3>
<p>Find the PostgreSQL installation.</p>
<h3>IMPORTED Targets</h3>
<p>New in version 3.14. </p>
<p> This module defines <code>IMPORTED</code> target <code>PostgreSQL::PostgreSQL</code> if PostgreSQL has been found.</p>
<h3>Result Variables</h3>
<p>This module will set the following variables in your project:</p>
<dl>
<dt><code>PostgreSQL_FOUND</code></p>
<dd>True if PostgreSQL is found.</p>
<dt><code>PostgreSQL_LIBRARIES</code></p>
<dd>the PostgreSQL libraries needed for linking</p>
<dt><code>PostgreSQL_INCLUDE_DIRS</code></p>
<dd>the directories of the PostgreSQL headers</p>
<dt><code>PostgreSQL_LIBRARY_DIRS</code></p>
<dd>the link directories for PostgreSQL libraries</p>
<dt><code>PostgreSQL_VERSION_STRING</code></p>
<dd>the version of PostgreSQL found</p>
<dt><code>PostgreSQL_TYPE_INCLUDE_DIR</code></p>
<dd>the directories of the PostgreSQL server headers</dl>
<h3>Components</h3>
<p>This module contains additional <code>Server</code> component, that forcibly checks for the presence of server headers. Note that <code>PostgreSQL_TYPE_INCLUDE_DIR</code> is set regardless of the presence of the <code>Server</code> component in find_package call.</p>
<h3>FindProducer</h3>
<p>Though Producer isn&#8217;t directly part of OpenSceneGraph, its primary user is OSG so I consider this part of the Findosg* suite used to find OpenSceneGraph components. You&#8217;ll notice that I accept OSGDIR as an environment path. </p>
<p> Each component is separate and you must opt in to each module. You must also opt into OpenGL (and OpenThreads?) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate Producer This module defines PRODUCER_LIBRARY PRODUCER_FOUND, if false, do not try to link to Producer PRODUCER_INCLUDE_DIR, where to find the headers </p>
<p> $PRODUCER_DIR is an environment variable that would correspond to the ./configure &#8211;prefix=$PRODUCER_DIR used in building osg. </p>
<p> Created by Eric Wing.</p>
<h3>FindProtobuf</h3>
<p>Locate and configure the Google Protocol Buffers library. </p>
<p> New in version 3.6: Support for <code>find_package()</code> version checks. </p>
<p> Changed in version 3.6: All input and output variables use the <code>Protobuf_</code> prefix. Variables with <code>PROTOBUF_</code> prefix are still supported for compatibility. </p>
<p> The following variables can be set and are optional:</p>
<dl>
<dt><code>Protobuf_SRC_ROOT_FOLDER</code></p>
<dd>When compiling with MSVC, if this cache variable is set the protobuf-default VS project build locations (vsprojects/Debug and vsprojects/Release or vsprojects/x64/Debug and vsprojects/x64/Release) will be searched for libraries and binaries.</p>
<dt><code>Protobuf_IMPORT_DIRS</code></p>
<dd>List of additional directories to be searched for imported .proto files.</p>
<dt><code>Protobuf_DEBUG</code></p>
<dd>New in version 3.6. </p>
<p> Show debug messages.</p>
<dt><code>Protobuf_USE_STATIC_LIBS</code></p>
<dd>New in version 3.9. </p>
<p> Set to ON to force the use of the static libraries. Default is OFF. </p>
<p> Defines the following variables:</p>
<dt><code>Protobuf_FOUND</code></p>
<dd>Found the Google Protocol Buffers library (libprotobuf &amp; header files)</p>
<dt><code>Protobuf_VERSION</code></p>
<dd>New in version 3.6. </p>
<p> Version of package found.</p>
<dt><code>Protobuf_INCLUDE_DIRS</code></p>
<dd>Include directories for Google Protocol Buffers</p>
<dt><code>Protobuf_LIBRARIES</code></p>
<dd>The protobuf libraries</p>
<dt><code>Protobuf_PROTOC_LIBRARIES</code></p>
<dd>The protoc libraries</p>
<dt><code>Protobuf_LITE_LIBRARIES</code></p>
<dd>The protobuf-lite libraries </p>
<p> New in version 3.9: The following <code>IMPORTED</code> targets are also defined: </p>
<dt><code>protobuf::libprotobuf</code></p>
<dd>The protobuf library.</p>
<dt><code>protobuf::libprotobuf-lite</code></p>
<dd>The protobuf lite library.</p>
<dt><code>protobuf::libprotoc</code></p>
<dd>The protoc library.</p>
<dt><code>protobuf::protoc</code></p>
<dd>New in version 3.10: The protoc compiler. </p>
<p> The following cache variables are also available to set or use:</p>
<dt><code>Protobuf_LIBRARY</code></p>
<dd>The protobuf library</p>
<dt><code>Protobuf_PROTOC_LIBRARY</code></p>
<dd>The protoc library</p>
<dt><code>Protobuf_INCLUDE_DIR</code></p>
<dd>The include directory for protocol buffers</p>
<dt><code>Protobuf_PROTOC_EXECUTABLE</code></p>
<dd>The protoc compiler</p>
<dt><code>Protobuf_LIBRARY_DEBUG</code></p>
<dd>The protobuf library (debug)</p>
<dt><code>Protobuf_PROTOC_LIBRARY_DEBUG</code></p>
<dd>The protoc library (debug)</p>
<dt><code>Protobuf_LITE_LIBRARY</code></p>
<dd>The protobuf lite library</p>
<dt><code>Protobuf_LITE_LIBRARY_DEBUG</code></p>
<dd>The protobuf lite library (debug) </p>
<p> Example: </p>
<pre>find_package(Protobuf REQUIRED)
include_directories(${Protobuf_INCLUDE_DIRS})
include_directories(${CMAKE_CURRENT_BINARY_DIR})
protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS foo.proto)
protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS EXPORT_MACRO DLL_EXPORT foo.proto)
protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS DESCRIPTORS PROTO_DESCS foo.proto)
protobuf_generate_python(PROTO_PY foo.proto)
add_executable(bar bar.cc ${PROTO_SRCS} ${PROTO_HDRS})
target_link_libraries(bar ${Protobuf_LIBRARIES})</pre>
<p><code>NOTE:</code> The <code>protobuf_generate_cpp</code> and <code>protobuf_generate_python</code> functions and <code>add_executable()</code> or <code>add_library()</code> calls only work properly within the same directory.</p>
<dt><code>protobuf_generate_cpp</code></p>
<dd>Add custom commands to process <code>.proto</code> files to C++: </p>
<pre>protobuf_generate_cpp (&lt;SRCS&gt; &lt;HDRS&gt;
 [DESCRIPTORS &lt;DESC&gt;] [EXPORT_MACRO &lt;MACRO&gt;] [&lt;ARGN&gt;...])</pre>
<dt><code>SRCS</code></p>
<dd>Variable to define with autogenerated source files</p>
<dt><code>HDRS</code></p>
<dd>Variable to define with autogenerated header files</p>
<dt><code>DESCRIPTORS</code></p>
<dd>New in version 3.10: Variable to define with autogenerated descriptor files, if requested. </p>
<dt><code>EXPORT_MACRO</code></p>
<dd>is a macro which should expand to <code>__declspec(dllexport)</code> or <code>__declspec(dllimport)</code> depending on what is being compiled.</p>
<dt><code>ARGN</code></p>
<dd><code>.proto</code> files</p>
<dt><code>protobuf_generate_python</code></p>
<dd>New in version 3.4. </p>
<p> Add custom commands to process <code>.proto</code> files to Python: </p>
<pre>protobuf_generate_python (&lt;PY&gt; [&lt;ARGN&gt;...])</pre>
<dt><code>PY</code></p>
<dd>Variable to define with autogenerated Python files</p>
<dt><code>ARGN</code></p>
<dd><code>.proto</code> files</dl>
<h3>FindPython</h3>
<p>New in version 3.12. </p>
<p> Find Python interpreter, compiler and development environment (include directories and libraries). </p>
<p> New in version 3.19: When a version is requested, it can be specified as a simple value or as a range. For a detailed description of version range usage and capabilities, refer to the <code>find_package()</code> command. </p>
<p> The following components are supported:</p>
<dl>
<dt>&bull;</p>
<dd><code>Interpreter</code>: search for Python interpreter.</p>
<dt>&bull;</p>
<dd><code>Compiler</code>: search for Python compiler. Only offered by IronPython.</p>
<dt>&bull;</p>
<dd><code>Development</code>: search for development artifacts (include directories and libraries). </p>
<p> New in version 3.18: This component includes two sub-components which can be specified independently:</p>
<dt>&bull;</p>
<dd><code>Development.Module</code>: search for artifacts for Python module developments.</p>
<dt>&bull;</p>
<dd><code>Development.Embed</code>: search for artifacts for Python embedding developments. </p>
<dt>&bull;</p>
<dd><code>NumPy</code>: search for NumPy include directories. </p>
<p> New in version 3.14: Added the <code>NumPy</code> component. </p>
<p> If no <code>COMPONENTS</code> are specified, <code>Interpreter</code> is assumed. </p>
<p> If component <code>Development</code> is specified, it implies sub-components <code>Development.Module</code> and <code>Development.Embed</code>. </p>
<p> To ensure consistent versions between components <code>Interpreter</code>, <code>Compiler</code>, <code>Development</code> (or one of its sub-components) and <code>NumPy</code>, specify all components at the same time: </p>
<pre>find_package (Python COMPONENTS Interpreter Development)</pre>
<p>This module looks preferably for version 3 of Python. If not found, version 2 is searched. To manage concurrent versions 3 and 2 of Python, use <code>FindPython3</code> and <code>FindPython2</code> modules rather than this one. </p>
<p> <code>NOTE:</code> If components <code>Interpreter</code> and <code>Development</code> (or one of its sub-components) are both specified, this module search only for interpreter with same platform architecture as the one defined by <code>CMake</code> configuration. This constraint does not apply if only <code>Interpreter</code> component is specified.</dl>
<h3>Imported Targets</h3>
<p>This module defines the following Imported Targets: </p>
<p> Changed in version 3.14: Imported Targets are only created when <code>CMAKE_ROLE</code> is <code>PROJECT</code>. </p>
<dl>
<dt><code>Python::Interpreter</code></p>
<dd>Python interpreter. Target defined if component <code>Interpreter</code> is found.</p>
<dt><code>Python::Compiler</code></p>
<dd>Python compiler. Target defined if component <code>Compiler</code> is found.</p>
<dt><code>Python::Module</code></p>
<dd>New in version 3.15. </p>
<p> Python library for Python module. Target defined if component <code>Development.Module</code> is found.</p>
<dt><code>Python::Python</code></p>
<dd>Python library for Python embedding. Target defined if component <code>Development.Embed</code> is found.</p>
<dt><code>Python::NumPy</code></p>
<dd>New in version 3.14. </p>
<p> NumPy Python library. Target defined if component <code>NumPy</code> is found.</dl>
<h3>Result Variables</h3>
<p>This module will set the following variables in your project (see Standard Variable Names):</p>
<dl>
<dt><code>Python_FOUND</code></p>
<dd>System has the Python requested components.</p>
<dt><code>Python_Interpreter_FOUND</code></p>
<dd>System has the Python interpreter.</p>
<dt><code>Python_EXECUTABLE</code></p>
<dd>Path to the Python interpreter.</p>
<dt><code>Python_INTERPRETER_ID</code></p>
<dd>
<dt><code>A short string unique to the interpreter. Possible values include:</code></p>
<dd>
<dt>&bull;</p>
<dd>Python</p>
<dt>&bull;</p>
<dd>ActivePython</p>
<dt>&bull;</p>
<dd>Anaconda</p>
<dt>&bull;</p>
<dd>Canopy</p>
<dt>&bull;</p>
<dd>IronPython</p>
<dt>&bull;</p>
<dd>PyPy</p>
<dt><code>Python_STDLIB</code></p>
<dd>Standard platform independent installation directory. </p>
<p> Information returned by <code>distutils.sysconfig.get_python_lib(plat_specific=False,standard_lib=True)</code> or else <code>sysconfig.get_path(&#8216;stdlib&#8217;)</code>.</p>
<dt><code>Python_STDARCH</code></p>
<dd>Standard platform dependent installation directory. </p>
<p> Information returned by <code>distutils.sysconfig.get_python_lib(plat_specific=True,standard_lib=True)</code> or else <code>sysconfig.get_path(&#8216;platstdlib&#8217;)</code>.</p>
<dt><code>Python_SITELIB</code></p>
<dd>Third-party platform independent installation directory. </p>
<p> Information returned by <code>distutils.sysconfig.get_python_lib(plat_specific=False,standard_lib=False)</code> or else <code>sysconfig.get_path(&#8216;purelib&#8217;)</code>.</p>
<dt><code>Python_SITEARCH</code></p>
<dd>Third-party platform dependent installation directory. </p>
<p> Information returned by <code>distutils.sysconfig.get_python_lib(plat_specific=True,standard_lib=False)</code> or else <code>sysconfig.get_path(&#8216;platlib&#8217;)</code>.</p>
<dt><code>Python_SOABI</code></p>
<dd>New in version 3.17. </p>
<p> Extension suffix for modules. </p>
<p> Information returned by <code>distutils.sysconfig.get_config_var(&#8216;SOABI&#8217;)</code> or computed from <code>distutils.sysconfig.get_config_var(&#8216;EXT_SUFFIX&#8217;)</code> or <code>python-config &#8211;extension-suffix</code>. If package <code>distutils.sysconfig</code> is not available, <code>sysconfig.get_config_var(&#8216;SOABI&#8217;)</code> or <code>sysconfig.get_config_var(&#8216;EXT_SUFFIX&#8217;)</code> are used.</p>
<dt><code>Python_Compiler_FOUND</code></p>
<dd>System has the Python compiler.</p>
<dt><code>Python_COMPILER</code></p>
<dd>Path to the Python compiler. Only offered by IronPython.</p>
<dt><code>Python_COMPILER_ID</code></p>
<dd>
<dt><code>A short string unique to the compiler. Possible values include:</code></p>
<dd>
<dt>&bull;</p>
<dd>IronPython</p>
<dt><code>Python_DOTNET_LAUNCHER</code></p>
<dd>New in version 3.18. </p>
<p> The <code>.Net</code> interpreter. Only used by <code>IronPython</code> implementation.</p>
<dt><code>Python_Development_FOUND</code></p>
<dd>System has the Python development artifacts.</p>
<dt><code>Python_Development.Module_FOUND</code></p>
<dd>New in version 3.18. </p>
<p> System has the Python development artifacts for Python module.</p>
<dt><code>Python_Development.Embed_FOUND</code></p>
<dd>New in version 3.18. </p>
<p> System has the Python development artifacts for Python embedding. </p>
<p> <code>Python_INCLUDE_DIRS</code> The Python include directories.</p>
<dt><code>Python_LINK_OPTIONS</code></p>
<dd>New in version 3.19. </p>
<p> The Python link options. Some configurations require specific link options for a correct build and execution.</p>
<dt><code>Python_LIBRARIES</code></p>
<dd>The Python libraries.</p>
<dt><code>Python_LIBRARY_DIRS</code></p>
<dd>The Python library directories.</p>
<dt><code>Python_RUNTIME_LIBRARY_DIRS</code></p>
<dd>The Python runtime library directories.</p>
<dt><code>Python_VERSION</code></p>
<dd>Python version.</p>
<dt><code>Python_VERSION_MAJOR</code></p>
<dd>Python major version.</p>
<dt><code>Python_VERSION_MINOR</code></p>
<dd>Python minor version.</p>
<dt><code>Python_VERSION_PATCH</code></p>
<dd>Python patch version.</p>
<dt><code>Python_PyPy_VERSION</code></p>
<dd>New in version 3.18. </p>
<p> Python PyPy version.</p>
<dt><code>Python_NumPy_FOUND</code></p>
<dd>New in version 3.14. </p>
<p> System has the NumPy.</p>
<dt><code>Python_NumPy_INCLUDE_DIRS</code></p>
<dd>New in version 3.14. </p>
<p> The NumPy include directories.</p>
<dt><code>Python_NumPy_VERSION</code></p>
<dd>New in version 3.14. </p>
<p> The NumPy version.</dl>
<h3>Hints</h3>
<dl>
<dt><code>Python_ROOT_DIR</code></p>
<dd>Define the root directory of a Python installation.</p>
<dt><code>Python_USE_STATIC_LIBS</code></p>
<dd>
<dt>&bull;</p>
<dd>If not defined, search for shared libraries and static libraries in that order.</p>
<dt>&bull;</p>
<dd>If set to TRUE, search <code>only</code> for static libraries.</p>
<dt>&bull;</p>
<dd>If set to FALSE, search <code>only</code> for shared libraries. </p>
<p> <code>NOTE:</code> This hint will be ignored on <code>Windows</code> because static libraries are not available on this platform.</p>
<dt><code>Python_FIND_ABI</code></p>
<dd>New in version 3.16. </p>
<p> This variable defines which ABIs, as defined in <i>PEP 3149</i>, should be searched. </p>
<p> <code>NOTE:</code> This hint will be honored only when searched for <code>Python</code> version 3. </p>
<p> <code>NOTE:</code> If <code>Python_FIND_ABI</code> is not defined, any ABI will be searched. </p>
<p> The <code>Python_FIND_ABI</code> variable is a 3-tuple specifying, in that order, <code>pydebug</code> (<code>d</code>), <code>pymalloc</code> (<code>m</code>) and <code>unicode</code> (<code>u</code>) flags. Each element can be set to one of the following:</p>
<dt>&bull;</p>
<dd><code>ON</code>: Corresponding flag is selected.</p>
<dt>&bull;</p>
<dd><code>OFF</code>: Corresponding flag is not selected.</p>
<dt>&bull;</p>
<dd><code>ANY</code>: The two possibilities (<code>ON</code> and <code>OFF</code>) will be searched. </p>
<p> From this 3-tuple, various ABIs will be searched starting from the most specialized to the most general. Moreover, <code>debug</code> versions will be searched <code>after</code> <code>non-debug</code> ones. </p>
<p> For example, if we have: </p>
<pre>set (Python_FIND_ABI &quot;ON&quot; &quot;ANY&quot; &quot;ANY&quot;)</pre>
<p>The following flags combinations will be appended, in that order, to the artifact names: <code>dmu</code>, <code>dm</code>, <code>du</code>, and <code>d</code>. </p>
<p> And to search any possible ABIs: </p>
<pre>set (Python_FIND_ABI &quot;ANY&quot; &quot;ANY&quot; &quot;ANY&quot;)</pre>
<p>The following combinations, in that order, will be used: <code>mu</code>, <code>m</code>, <code>u</code>, <code>&lt;empty&gt;</code>, <code>dmu</code>, <code>dm</code>, <code>du</code> and <code>d</code>. </p>
<p> <code>NOTE:</code> This hint is useful only on <code>POSIX</code> systems. So, on <code>Windows</code> systems, when <code>Python_FIND_ABI</code> is defined, <code>Python</code> distributions from <i>python.org</i> will be found only if value for each flag is <code>OFF</code> or <code>ANY</code>.</p>
<dt><code>Python_FIND_STRATEGY</code></p>
<dd>New in version 3.15. </p>
<p> This variable defines how lookup will be done. The <code>Python_FIND_STRATEGY</code> variable can be set to one of the following:</p>
<dt>&bull;</p>
<dd><code>VERSION</code>: Try to find the most recent version in all specified locations. This is the default if policy <code>CMP0094</code> is undefined or set to <code>OLD</code>.</p>
<dt>&bull;</p>
<dd><code>LOCATION</code>: Stops lookup as soon as a version satisfying version constraints is founded. This is the default if policy <code>CMP0094</code> is set to <code>NEW</code>.</p>
<dt><code>Python_FIND_REGISTRY</code></p>
<dd>New in version 3.13. </p>
<p> On Windows the <code>Python_FIND_REGISTRY</code> variable determine the order of preference between registry and environment variables. the <code>Python_FIND_REGISTRY</code> variable can be set to one of the following:</p>
<dt>&bull;</p>
<dd><code>FIRST</code>: Try to use registry before environment variables. This is the default.</p>
<dt>&bull;</p>
<dd><code>LAST</code>: Try to use registry after environment variables.</p>
<dt>&bull;</p>
<dd><code>NEVER</code>: Never try to use registry.</p>
<dt><code>Python_FIND_FRAMEWORK</code></p>
<dd>New in version 3.15. </p>
<p> On macOS the <code>Python_FIND_FRAMEWORK</code> variable determine the order of preference between Apple-style and unix-style package components. This variable can take same values as <code>CMAKE_FIND_FRAMEWORK</code> variable. </p>
<p> <code>NOTE:</code> Value <code>ONLY</code> is not supported so <code>FIRST</code> will be used instead. </p>
<p> If <code>Python_FIND_FRAMEWORK</code> is not defined, <code>CMAKE_FIND_FRAMEWORK</code> variable will be used, if any.</p>
<dt><code>Python_FIND_VIRTUALENV</code></p>
<dd>New in version 3.15. </p>
<p> This variable defines the handling of virtual environments managed by <code>virtualenv</code> or <code>conda</code>. It is meaningful only when a virtual environment is active (i.e. the <code>activate</code> script has been evaluated). In this case, it takes precedence over <code>Python_FIND_REGISTRY</code> and <code>CMAKE_FIND_FRAMEWORK</code> variables. The <code>Python_FIND_VIRTUALENV</code> variable can be set to one of the following:</p>
<dt>&bull;</p>
<dd><code>FIRST</code>: The virtual environment is used before any other standard paths to look-up for the interpreter. This is the default.</p>
<dt>&bull;</p>
<dd><code>ONLY</code>: Only the virtual environment is used to look-up for the interpreter.</p>
<dt>&bull;</p>
<dd><code>STANDARD</code>: The virtual environment is not used to look-up for the interpreter but environment variable <code>PATH</code> is always considered. In this case, variable <code>Python_FIND_REGISTRY</code> (Windows) or <code>CMAKE_FIND_FRAMEWORK</code> (macOS) can be set with value <code>LAST</code> or <code>NEVER</code> to select preferably the interpreter from the virtual environment. </p>
<p> New in version 3.17: Added support for <code>conda</code> environments. </p>
<p> <code>NOTE:</code> If the component <code>Development</code> is requested, it is <code>strongly</code> recommended to also include the component <code>Interpreter</code> to get expected result.</p>
<dt><code>Python_FIND_IMPLEMENTATIONS</code></p>
<dd>New in version 3.18. </p>
<p> This variable defines, in an ordered list, the different implementations which will be searched. The <code>Python_FIND_IMPLEMENTATIONS</code> variable can hold the following values:</p>
<dt>&bull;</p>
<dd><code>CPython</code>: this is the standard implementation. Various products, like <code>Anaconda</code> or <code>ActivePython</code>, rely on this implementation.</p>
<dt>&bull;</p>
<dd><code>IronPython</code>: This implementation use the <code>CSharp</code> language for <code>.NET Framework</code> on top of the <i>Dynamic Language Runtime</i> (<code>DLR</code>). See <i>IronPython</i>.</p>
<dt>&bull;</p>
<dd><code>PyPy</code>: This implementation use <code>RPython</code> language and <code>RPython translation toolchain</code> to produce the python interpreter. See <i>PyPy</i>. </p>
<p> The default value is:</p>
<dt>&bull;</p>
<dd>Windows platform: <code>CPython</code>, <code>IronPython</code></p>
<dt>&bull;</p>
<dd>Other platforms: <code>CPython</code> </p>
<p> <code>NOTE:</code> This hint has the lowest priority of all hints, so even if, for example, you specify <code>IronPython</code> first and <code>CPython</code> in second, a python product based on <code>CPython</code> can be selected because, for example with <code>Python_FIND_STRATEGY=LOCATION</code>, each location will be search first for <code>IronPython</code> and second for <code>CPython</code>. </p>
<p> <code>NOTE:</code> When <code>IronPython</code> is specified, on platforms other than <code>Windows</code>, the <code>.Net</code> interpreter (i.e. <code>mono</code> command) is expected to be available through the <code>PATH</code> variable.</p>
<dt><code>Python_FIND_UNVERSIONED_NAMES</code></p>
<dd>New in version 3.20. </p>
<p> This variable defines how the generic names will be searched. Currently, it only applies to the generic names of the interpreter, namely, <code>python3</code> or <code>python2</code> and <code>python</code>. The <code>Python_FIND_UNVERSIONED_NAMES</code> variable can be set to one of the following values:</p>
<dt>&bull;</p>
<dd><code>FIRST</code>: The generic names are searched before the more specialized ones (such as <code>python2.5</code> for example).</p>
<dt>&bull;</p>
<dd><code>LAST</code>: The generic names are searched after the more specialized ones. This is the default.</p>
<dt>&bull;</p>
<dd><code>NEVER</code>: The generic name are not searched at all.</dl>
<h3>Artifacts Specification</h3>
<p>New in version 3.16. </p>
<p> To solve special cases, it is possible to specify directly the artifacts by setting the following variables:</p>
<dl>
<dt><code>Python_EXECUTABLE</code></p>
<dd>The path to the interpreter.</p>
<dt><code>Python_COMPILER</code></p>
<dd>The path to the compiler.</p>
<dt><code>Python_DOTNET_LAUNCHER</code></p>
<dd>New in version 3.18. </p>
<p> The <code>.Net</code> interpreter. Only used by <code>IronPython</code> implementation.</p>
<dt><code>Python_LIBRARY</code></p>
<dd>The path to the library. It will be used to compute the variables <code>Python_LIBRARIES</code>, <code>Python_LIBRARY_DIRS</code> and <code>Python_RUNTIME_LIBRARY_DIRS</code>.</p>
<dt><code>Python_INCLUDE_DIR</code></p>
<dd>The path to the directory of the <code>Python</code> headers. It will be used to compute the variable <code>Python_INCLUDE_DIRS</code>.</p>
<dt><code>Python_NumPy_INCLUDE_DIR</code></p>
<dd>The path to the directory of the <code>NumPy</code> headers. It will be used to compute the variable <code>Python_NumPy_INCLUDE_DIRS</code>. </p>
<p> <code>NOTE:</code> All paths must be absolute. Any artifact specified with a relative path will be ignored. </p>
<p> <code>NOTE:</code> When an artifact is specified, all <code>HINTS</code> will be ignored and no search will be performed for this artifact. </p>
<p> If more than one artifact is specified, it is the user&#8217;s responsibility to ensure the consistency of the various artifacts. </p>
<p> By default, this module supports multiple calls in different directories of a project with different version/component requirements while providing correct and consistent results for each call. To support this behavior, <code>CMake</code> cache is not used in the traditional way which can be problematic for interactive specification. So, to enable also interactive specification, module behavior can be controlled with the following variable:</p>
<dt><code>Python_ARTIFACTS_INTERACTIVE</code></p>
<dd>New in version 3.18. </p>
<p> Selects the behavior of the module. This is a boolean variable:</p>
<dt>&bull;</p>
<dd>If set to <code>TRUE</code>: Create CMake cache entries for the above artifact specification variables so that users can edit them interactively. This disables support for multiple version/component requirements.</p>
<dt>&bull;</p>
<dd>If set to <code>FALSE</code> or undefined: Enable multiple version/component requirements.</dl>
<h3>Commands</h3>
<p>This module defines the command <code>Python_add_library</code> (when <code>CMAKE_ROLE</code> is <code>PROJECT</code>), which has the same semantics as <code>add_library()</code> and adds a dependency to target <code>Python::Python</code> or, when library type is <code>MODULE</code>, to target <code>Python::Module</code> and takes care of Python module naming rules: </p>
<pre>Python_add_library (&lt;name&gt; [STATIC | SHARED | MODULE [WITH_SOABI]]
 &lt;source1&gt; [&lt;source2&gt; ...])</pre>
<p>If the library type is not specified, <code>MODULE</code> is assumed. </p>
<p> New in version 3.17: For <code>MODULE</code> library type, if option <code>WITH_SOABI</code> is specified, the module suffix will include the <code>Python_SOABI</code> value, if any.</p>
<h3>FindPython2</h3>
<p>New in version 3.12. </p>
<p> Find Python 2 interpreter, compiler and development environment (include directories and libraries). </p>
<p> New in version 3.19: When a version is requested, it can be specified as a simple value or as a range. For a detailed description of version range usage and capabilities, refer to the <code>find_package()</code> command. </p>
<p> The following components are supported:</p>
<dl>
<dt>&bull;</p>
<dd><code>Interpreter</code>: search for Python 2 interpreter</p>
<dt>&bull;</p>
<dd><code>Compiler</code>: search for Python 2 compiler. Only offered by IronPython.</p>
<dt>&bull;</p>
<dd><code>Development</code>: search for development artifacts (include directories and libraries). </p>
<p> New in version 3.18: This component includes two sub-components which can be specified independently:</p>
<dt>&bull;</p>
<dd><code>Development.Module</code>: search for artifacts for Python 2 module developments.</p>
<dt>&bull;</p>
<dd><code>Development.Embed</code>: search for artifacts for Python 2 embedding developments. </p>
<dt>&bull;</p>
<dd><code>NumPy</code>: search for NumPy include directories. </p>
<p> New in version 3.14: Added the <code>NumPy</code> component. </p>
<p> If no <code>COMPONENTS</code> are specified, <code>Interpreter</code> is assumed. </p>
<p> If component <code>Development</code> is specified, it implies sub-components <code>Development.Module</code> and <code>Development.Embed</code>. </p>
<p> To ensure consistent versions between components <code>Interpreter</code>, <code>Compiler</code>, <code>Development</code> (or one of its sub-components) and <code>NumPy</code>, specify all components at the same time: </p>
<pre>find_package (Python2 COMPONENTS Interpreter Development)</pre>
<p>This module looks only for version 2 of Python. This module can be used concurrently with <code>FindPython3</code> module to use both Python versions. </p>
<p> The <code>FindPython</code> module can be used if Python version does not matter for you. </p>
<p> <code>NOTE:</code> If components <code>Interpreter</code> and <code>Development</code> (or one of its sub-components) are both specified, this module search only for interpreter with same platform architecture as the one defined by <code>CMake</code> configuration. This constraint does not apply if only <code>Interpreter</code> component is specified.</dl>
<h3>Imported Targets</h3>
<p>This module defines the following Imported Targets: </p>
<p> Changed in version 3.14: Imported Targets are only created when <code>CMAKE_ROLE</code> is <code>PROJECT</code>. </p>
<dl>
<dt><code>Python2::Interpreter</code></p>
<dd>Python 2 interpreter. Target defined if component <code>Interpreter</code> is found.</p>
<dt><code>Python2::Compiler</code></p>
<dd>Python 2 compiler. Target defined if component <code>Compiler</code> is found.</p>
<dt><code>Python2::Module</code></p>
<dd>New in version 3.15. </p>
<p> Python 2 library for Python module. Target defined if component <code>Development.Module</code> is found.</p>
<dt><code>Python2::Python</code></p>
<dd>Python 2 library for Python embedding. Target defined if component <code>Development.Embed</code> is found.</p>
<dt><code>Python2::NumPy</code></p>
<dd>New in version 3.14. </p>
<p> NumPy library for Python 2. Target defined if component <code>NumPy</code> is found.</dl>
<h3>Result Variables</h3>
<p>This module will set the following variables in your project (see Standard Variable Names):</p>
<dl>
<dt><code>Python2_FOUND</code></p>
<dd>System has the Python 2 requested components.</p>
<dt><code>Python2_Interpreter_FOUND</code></p>
<dd>System has the Python 2 interpreter.</p>
<dt><code>Python2_EXECUTABLE</code></p>
<dd>Path to the Python 2 interpreter.</p>
<dt><code>Python2_INTERPRETER_ID</code></p>
<dd>
<dt><code>A short string unique to the interpreter. Possible values include:</code></p>
<dd>
<dt>&bull;</p>
<dd>Python</p>
<dt>&bull;</p>
<dd>ActivePython</p>
<dt>&bull;</p>
<dd>Anaconda</p>
<dt>&bull;</p>
<dd>Canopy</p>
<dt>&bull;</p>
<dd>IronPython</p>
<dt>&bull;</p>
<dd>PyPy</p>
<dt><code>Python2_STDLIB</code></p>
<dd>Standard platform independent installation directory. </p>
<p> Information returned by <code>distutils.sysconfig.get_python_lib(plat_specific=False,standard_lib=True)</code> or else <code>sysconfig.get_path(&#8216;stdlib&#8217;)</code>.</p>
<dt><code>Python2_STDARCH</code></p>
<dd>Standard platform dependent installation directory. </p>
<p> Information returned by <code>distutils.sysconfig.get_python_lib(plat_specific=True,standard_lib=True)</code> or else <code>sysconfig.get_path(&#8216;platstdlib&#8217;)</code>.</p>
<dt><code>Python2_SITELIB</code></p>
<dd>Third-party platform independent installation directory. </p>
<p> Information returned by <code>distutils.sysconfig.get_python_lib(plat_specific=False,standard_lib=False)</code> or else <code>sysconfig.get_path(&#8216;purelib&#8217;)</code>.</p>
<dt><code>Python2_SITEARCH</code></p>
<dd>Third-party platform dependent installation directory. </p>
<p> Information returned by <code>distutils.sysconfig.get_python_lib(plat_specific=True,standard_lib=False)</code> or else <code>sysconfig.get_path(&#8216;platlib&#8217;)</code>.</p>
<dt><code>Python2_Compiler_FOUND</code></p>
<dd>System has the Python 2 compiler.</p>
<dt><code>Python2_COMPILER</code></p>
<dd>Path to the Python 2 compiler. Only offered by IronPython.</p>
<dt><code>Python2_COMPILER_ID</code></p>
<dd>
<dt><code>A short string unique to the compiler. Possible values include:</code></p>
<dd>
<dt>&bull;</p>
<dd>IronPython</p>
<dt><code>Python2_DOTNET_LAUNCHER</code></p>
<dd>New in version 3.18. </p>
<p> The <code>.Net</code> interpreter. Only used by <code>IronPython</code> implementation.</p>
<dt><code>Python2_Development_FOUND</code></p>
<dd>System has the Python 2 development artifacts.</p>
<dt><code>Python2_Development.Module_FOUND</code></p>
<dd>New in version 3.18. </p>
<p> System has the Python 2 development artifacts for Python module.</p>
<dt><code>Python2_Development.Embed_FOUND</code></p>
<dd>New in version 3.18. </p>
<p> System has the Python 2 development artifacts for Python embedding.</p>
<dt><code>Python2_INCLUDE_DIRS</code></p>
<dd>The Python 2 include directories.</p>
<dt><code>Python2_LINK_OPTIONS</code></p>
<dd>New in version 3.19. </p>
<p> The Python 2 link options. Some configurations require specific link options for a correct build and execution.</p>
<dt><code>Python2_LIBRARIES</code></p>
<dd>The Python 2 libraries.</p>
<dt><code>Python2_LIBRARY_DIRS</code></p>
<dd>The Python 2 library directories.</p>
<dt><code>Python2_RUNTIME_LIBRARY_DIRS</code></p>
<dd>The Python 2 runtime library directories.</p>
<dt><code>Python2_VERSION</code></p>
<dd>Python 2 version.</p>
<dt><code>Python2_VERSION_MAJOR</code></p>
<dd>Python 2 major version.</p>
<dt><code>Python2_VERSION_MINOR</code></p>
<dd>Python 2 minor version.</p>
<dt><code>Python2_VERSION_PATCH</code></p>
<dd>Python 2 patch version.</p>
<dt><code>Python2_PyPy_VERSION</code></p>
<dd>New in version 3.18. </p>
<p> Python 2 PyPy version.</p>
<dt><code>Python2_NumPy_FOUND</code></p>
<dd>New in version 3.14. </p>
<p> System has the NumPy.</p>
<dt><code>Python2_NumPy_INCLUDE_DIRS</code></p>
<dd>New in version 3.14. </p>
<p> The NumPy include directories.</p>
<dt><code>Python2_NumPy_VERSION</code></p>
<dd>New in version 3.14. </p>
<p> The NumPy version.</dl>
<h3>Hints</h3>
<dl>
<dt><code>Python2_ROOT_DIR</code></p>
<dd>Define the root directory of a Python 2 installation.</p>
<dt><code>Python2_USE_STATIC_LIBS</code></p>
<dd>
<dt>&bull;</p>
<dd>If not defined, search for shared libraries and static libraries in that order.</p>
<dt>&bull;</p>
<dd>If set to TRUE, search <code>only</code> for static libraries.</p>
<dt>&bull;</p>
<dd>If set to FALSE, search <code>only</code> for shared libraries. </p>
<p> <code>NOTE:</code> This hint will be ignored on <code>Windows</code> because static libraries are not available on this platform.</p>
<dt><code>Python2_FIND_STRATEGY</code></p>
<dd>New in version 3.15. </p>
<p> This variable defines how lookup will be done. The <code>Python2_FIND_STRATEGY</code> variable can be set to one of the following:</p>
<dt>&bull;</p>
<dd><code>VERSION</code>: Try to find the most recent version in all specified locations. This is the default if policy <code>CMP0094</code> is undefined or set to <code>OLD</code>.</p>
<dt>&bull;</p>
<dd><code>LOCATION</code>: Stops lookup as soon as a version satisfying version constraints is founded. This is the default if policy <code>CMP0094</code> is set to <code>NEW</code>.</p>
<dt><code>Python2_FIND_REGISTRY</code></p>
<dd>New in version 3.13. </p>
<p> On Windows the <code>Python2_FIND_REGISTRY</code> variable determine the order of preference between registry and environment variables. the <code>Python2_FIND_REGISTRY</code> variable can be set to one of the following:</p>
<dt>&bull;</p>
<dd><code>FIRST</code>: Try to use registry before environment variables. This is the default.</p>
<dt>&bull;</p>
<dd><code>LAST</code>: Try to use registry after environment variables.</p>
<dt>&bull;</p>
<dd><code>NEVER</code>: Never try to use registry.</p>
<dt><code>Python2_FIND_FRAMEWORK</code></p>
<dd>New in version 3.15. </p>
<p> On macOS the <code>Python2_FIND_FRAMEWORK</code> variable determine the order of preference between Apple-style and unix-style package components. This variable can take same values as <code>CMAKE_FIND_FRAMEWORK</code> variable. </p>
<p> <code>NOTE:</code> Value <code>ONLY</code> is not supported so <code>FIRST</code> will be used instead. </p>
<p> If <code>Python2_FIND_FRAMEWORK</code> is not defined, <code>CMAKE_FIND_FRAMEWORK</code> variable will be used, if any.</p>
<dt><code>Python2_FIND_VIRTUALENV</code></p>
<dd>New in version 3.15. </p>
<p> This variable defines the handling of virtual environments managed by <code>virtualenv</code> or <code>conda</code>. It is meaningful only when a virtual environment is active (i.e. the <code>activate</code> script has been evaluated). In this case, it takes precedence over <code>Python2_FIND_REGISTRY</code> and <code>CMAKE_FIND_FRAMEWORK</code> variables. The <code>Python2_FIND_VIRTUALENV</code> variable can be set to one of the following:</p>
<dt>&bull;</p>
<dd><code>FIRST</code>: The virtual environment is used before any other standard paths to look-up for the interpreter. This is the default.</p>
<dt>&bull;</p>
<dd><code>ONLY</code>: Only the virtual environment is used to look-up for the interpreter.</p>
<dt>&bull;</p>
<dd><code>STANDARD</code>: The virtual environment is not used to look-up for the interpreter but environment variable <code>PATH</code> is always considered. In this case, variable <code>Python2_FIND_REGISTRY</code> (Windows) or <code>CMAKE_FIND_FRAMEWORK</code> (macOS) can be set with value <code>LAST</code> or <code>NEVER</code> to select preferably the interpreter from the virtual environment. </p>
<p> New in version 3.17: Added support for <code>conda</code> environments. </p>
<p> <code>NOTE:</code> If the component <code>Development</code> is requested, it is <code>strongly</code> recommended to also include the component <code>Interpreter</code> to get expected result.</p>
<dt><code>Python2_FIND_IMPLEMENTATIONS</code></p>
<dd>New in version 3.18. </p>
<p> This variable defines, in an ordered list, the different implementations which will be searched. The <code>Python2_FIND_IMPLEMENTATIONS</code> variable can hold the following values:</p>
<dt>&bull;</p>
<dd><code>CPython</code>: this is the standard implementation. Various products, like <code>Anaconda</code> or <code>ActivePython</code>, rely on this implementation.</p>
<dt>&bull;</p>
<dd><code>IronPython</code>: This implementation use the <code>CSharp</code> language for <code>.NET Framework</code> on top of the <i>Dynamic Language Runtime</i> (<code>DLR</code>). See <i>IronPython</i>.</p>
<dt>&bull;</p>
<dd><code>PyPy</code>: This implementation use <code>RPython</code> language and <code>RPython translation toolchain</code> to produce the python interpreter. See <i>PyPy</i>. </p>
<p> The default value is:</p>
<dt>&bull;</p>
<dd>Windows platform: <code>CPython</code>, <code>IronPython</code></p>
<dt>&bull;</p>
<dd>Other platforms: <code>CPython</code> </p>
<p> <code>NOTE:</code> This hint has the lowest priority of all hints, so even if, for example, you specify <code>IronPython</code> first and <code>CPython</code> in second, a python product based on <code>CPython</code> can be selected because, for example with <code>Python2_FIND_STRATEGY=LOCATION</code>, each location will be search first for <code>IronPython</code> and second for <code>CPython</code>. </p>
<p> <code>NOTE:</code> When <code>IronPython</code> is specified, on platforms other than <code>Windows</code>, the <code>.Net</code> interpreter (i.e. <code>mono</code> command) is expected to be available through the <code>PATH</code> variable.</p>
<dt><code>Python2_FIND_UNVERSIONED_NAMES</code></p>
<dd>New in version 3.20. </p>
<p> This variable defines how the generic names will be searched. Currently, it only applies to the generic names of the interpreter, namely, <code>python2</code> and <code>python</code>. The <code>Python2_FIND_UNVERSIONED_NAMES</code> variable can be set to one of the following values:</p>
<dt>&bull;</p>
<dd><code>FIRST</code>: The generic names are searched before the more specialized ones (such as <code>python2.5</code> for example).</p>
<dt>&bull;</p>
<dd><code>LAST</code>: The generic names are searched after the more specialized ones. This is the default.</p>
<dt>&bull;</p>
<dd><code>NEVER</code>: The generic name are not searched at all.</dl>
<h3>Artifacts Specification</h3>
<p>New in version 3.16. </p>
<p> To solve special cases, it is possible to specify directly the artifacts by setting the following variables:</p>
<dl>
<dt><code>Python2_EXECUTABLE</code></p>
<dd>The path to the interpreter.</p>
<dt><code>Python2_COMPILER</code></p>
<dd>The path to the compiler.</p>
<dt><code>Python2_DOTNET_LAUNCHER</code></p>
<dd>New in version 3.18. </p>
<p> The <code>.Net</code> interpreter. Only used by <code>IronPython</code> implementation.</p>
<dt><code>Python2_LIBRARY</code></p>
<dd>The path to the library. It will be used to compute the variables <code>Python2_LIBRARIES</code>, <code>Python2_LIBRARY_DIRS</code> and <code>Python2_RUNTIME_LIBRARY_DIRS</code>.</p>
<dt><code>Python2_INCLUDE_DIR</code></p>
<dd>The path to the directory of the <code>Python</code> headers. It will be used to compute the variable <code>Python2_INCLUDE_DIRS</code>.</p>
<dt><code>Python2_NumPy_INCLUDE_DIR</code></p>
<dd>The path to the directory of the <code>NumPy</code> headers. It will be used to compute the variable <code>Python2_NumPy_INCLUDE_DIRS</code>. </p>
<p> <code>NOTE:</code> All paths must be absolute. Any artifact specified with a relative path will be ignored. </p>
<p> <code>NOTE:</code> When an artifact is specified, all <code>HINTS</code> will be ignored and no search will be performed for this artifact. </p>
<p> If more than one artifact is specified, it is the user&#8217;s responsibility to ensure the consistency of the various artifacts. </p>
<p> By default, this module supports multiple calls in different directories of a project with different version/component requirements while providing correct and consistent results for each call. To support this behavior, <code>CMake</code> cache is not used in the traditional way which can be problematic for interactive specification. So, to enable also interactive specification, module behavior can be controlled with the following variable:</p>
<dt><code>Python2_ARTIFACTS_INTERACTIVE</code></p>
<dd>New in version 3.18. </p>
<p> Selects the behavior of the module. This is a boolean variable:</p>
<dt>&bull;</p>
<dd>If set to <code>TRUE</code>: Create CMake cache entries for the above artifact specification variables so that users can edit them interactively. This disables support for multiple version/component requirements.</p>
<dt>&bull;</p>
<dd>If set to <code>FALSE</code> or undefined: Enable multiple version/component requirements.</dl>
<h3>Commands</h3>
<p>This module defines the command <code>Python2_add_library</code> (when <code>CMAKE_ROLE</code> is <code>PROJECT</code>), which has the same semantics as <code>add_library()</code> and adds a dependency to target <code>Python2::Python</code> or, when library type is <code>MODULE</code>, to target <code>Python2::Module</code> and takes care of Python module naming rules: </p>
<pre>Python2_add_library (&lt;name&gt; [STATIC | SHARED | MODULE]
 &lt;source1&gt; [&lt;source2&gt; ...])</pre>
<p>If library type is not specified, <code>MODULE</code> is assumed.</p>
<h3>FindPython3</h3>
<p>New in version 3.12. </p>
<p> Find Python 3 interpreter, compiler and development environment (include directories and libraries). </p>
<p> New in version 3.19: When a version is requested, it can be specified as a simple value or as a range. For a detailed description of version range usage and capabilities, refer to the <code>find_package()</code> command. </p>
<p> The following components are supported:</p>
<dl>
<dt>&bull;</p>
<dd><code>Interpreter</code>: search for Python 3 interpreter</p>
<dt>&bull;</p>
<dd><code>Compiler</code>: search for Python 3 compiler. Only offered by IronPython.</p>
<dt>&bull;</p>
<dd><code>Development</code>: search for development artifacts (include directories and libraries). </p>
<p> New in version 3.18: This component includes two sub-components which can be specified independently:</p>
<dt>&bull;</p>
<dd><code>Development.Module</code>: search for artifacts for Python 3 module developments.</p>
<dt>&bull;</p>
<dd><code>Development.Embed</code>: search for artifacts for Python 3 embedding developments. </p>
<dt>&bull;</p>
<dd><code>NumPy</code>: search for NumPy include directories. </p>
<p> New in version 3.14: Added the <code>NumPy</code> component. </p>
<p> If no <code>COMPONENTS</code> are specified, <code>Interpreter</code> is assumed. </p>
<p> If component <code>Development</code> is specified, it implies sub-components <code>Development.Module</code> and <code>Development.Embed</code>. </p>
<p> To ensure consistent versions between components <code>Interpreter</code>, <code>Compiler</code>, <code>Development</code> (or one of its sub-components) and <code>NumPy</code>, specify all components at the same time: </p>
<pre>find_package (Python3 COMPONENTS Interpreter Development)</pre>
<p>This module looks only for version 3 of Python. This module can be used concurrently with <code>FindPython2</code> module to use both Python versions. </p>
<p> The <code>FindPython</code> module can be used if Python version does not matter for you. </p>
<p> <code>NOTE:</code> If components <code>Interpreter</code> and <code>Development</code> (or one of its sub-components) are both specified, this module search only for interpreter with same platform architecture as the one defined by <code>CMake</code> configuration. This constraint does not apply if only <code>Interpreter</code> component is specified.</dl>
<h3>Imported Targets</h3>
<p>This module defines the following Imported Targets: </p>
<p> Changed in version 3.14: Imported Targets are only created when <code>CMAKE_ROLE</code> is <code>PROJECT</code>. </p>
<dl>
<dt><code>Python3::Interpreter</code></p>
<dd>Python 3 interpreter. Target defined if component <code>Interpreter</code> is found.</p>
<dt><code>Python3::Compiler</code></p>
<dd>Python 3 compiler. Target defined if component <code>Compiler</code> is found.</p>
<dt><code>Python3::Module</code></p>
<dd>New in version 3.15. </p>
<p> Python 3 library for Python module. Target defined if component <code>Development.Module</code> is found.</p>
<dt><code>Python3::Python</code></p>
<dd>Python 3 library for Python embedding. Target defined if component <code>Development.Embed</code> is found.</p>
<dt><code>Python3::NumPy</code></p>
<dd>New in version 3.14. </p>
<p> NumPy library for Python 3. Target defined if component <code>NumPy</code> is found.</dl>
<h3>Result Variables</h3>
<p>This module will set the following variables in your project (see Standard Variable Names):</p>
<dl>
<dt><code>Python3_FOUND</code></p>
<dd>System has the Python 3 requested components.</p>
<dt><code>Python3_Interpreter_FOUND</code></p>
<dd>System has the Python 3 interpreter.</p>
<dt><code>Python3_EXECUTABLE</code></p>
<dd>Path to the Python 3 interpreter.</p>
<dt><code>Python3_INTERPRETER_ID</code></p>
<dd>
<dt><code>A short string unique to the interpreter. Possible values include:</code></p>
<dd>
<dt>&bull;</p>
<dd>Python</p>
<dt>&bull;</p>
<dd>ActivePython</p>
<dt>&bull;</p>
<dd>Anaconda</p>
<dt>&bull;</p>
<dd>Canopy</p>
<dt>&bull;</p>
<dd>IronPython</p>
<dt>&bull;</p>
<dd>PyPy</p>
<dt><code>Python3_STDLIB</code></p>
<dd>Standard platform independent installation directory. </p>
<p> Information returned by <code>distutils.sysconfig.get_python_lib(plat_specific=False,standard_lib=True)</code> or else <code>sysconfig.get_path(&#8216;stdlib&#8217;)</code>.</p>
<dt><code>Python3_STDARCH</code></p>
<dd>Standard platform dependent installation directory. </p>
<p> Information returned by <code>distutils.sysconfig.get_python_lib(plat_specific=True,standard_lib=True)</code> or else <code>sysconfig.get_path(&#8216;platstdlib&#8217;)</code>.</p>
<dt><code>Python3_SITELIB</code></p>
<dd>Third-party platform independent installation directory. </p>
<p> Information returned by <code>distutils.sysconfig.get_python_lib(plat_specific=False,standard_lib=False)</code> or else <code>sysconfig.get_path(&#8216;purelib&#8217;)</code>.</p>
<dt><code>Python3_SITEARCH</code></p>
<dd>Third-party platform dependent installation directory. </p>
<p> Information returned by <code>distutils.sysconfig.get_python_lib(plat_specific=True,standard_lib=False)</code> or else <code>sysconfig.get_path(&#8216;platlib&#8217;)</code>.</p>
<dt><code>Python3_SOABI</code></p>
<dd>New in version 3.17. </p>
<p> Extension suffix for modules. </p>
<p> Information returned by <code>distutils.sysconfig.get_config_var(&#8216;SOABI&#8217;)</code> or computed from <code>distutils.sysconfig.get_config_var(&#8216;EXT_SUFFIX&#8217;)</code> or <code>python3-config &#8211;extension-suffix</code>. If package <code>distutils.sysconfig</code> is not available, <code>sysconfig.get_config_var(&#8216;SOABI&#8217;)</code> or <code>sysconfig.get_config_var(&#8216;EXT_SUFFIX&#8217;)</code> are used.</p>
<dt><code>Python3_Compiler_FOUND</code></p>
<dd>System has the Python 3 compiler.</p>
<dt><code>Python3_COMPILER</code></p>
<dd>Path to the Python 3 compiler. Only offered by IronPython.</p>
<dt><code>Python3_COMPILER_ID</code></p>
<dd>
<dt><code>A short string unique to the compiler. Possible values include:</code></p>
<dd>
<dt>&bull;</p>
<dd>IronPython</p>
<dt><code>Python3_DOTNET_LAUNCHER</code></p>
<dd>New in version 3.18. </p>
<p> The <code>.Net</code> interpreter. Only used by <code>IronPython</code> implementation. </p>
<p> <code>Python3_Development_FOUND</code> System has the Python 3 development artifacts.</p>
<dt><code>Python3_Development.Module_FOUND</code></p>
<dd>New in version 3.18. </p>
<p> System has the Python 3 development artifacts for Python module.</p>
<dt><code>Python3_Development.Embed_FOUND</code></p>
<dd>New in version 3.18. </p>
<p> System has the Python 3 development artifacts for Python embedding. </p>
<p> <code>Python3_INCLUDE_DIRS</code> The Python 3 include directories.</p>
<dt><code>Python3_LINK_OPTIONS</code></p>
<dd>New in version 3.19. </p>
<p> The Python 3 link options. Some configurations require specific link options for a correct build and execution.</p>
<dt><code>Python3_LIBRARIES</code></p>
<dd>The Python 3 libraries.</p>
<dt><code>Python3_LIBRARY_DIRS</code></p>
<dd>The Python 3 library directories.</p>
<dt><code>Python3_RUNTIME_LIBRARY_DIRS</code></p>
<dd>The Python 3 runtime library directories.</p>
<dt><code>Python3_VERSION</code></p>
<dd>Python 3 version.</p>
<dt><code>Python3_VERSION_MAJOR</code></p>
<dd>Python 3 major version.</p>
<dt><code>Python3_VERSION_MINOR</code></p>
<dd>Python 3 minor version.</p>
<dt><code>Python3_VERSION_PATCH</code></p>
<dd>Python 3 patch version.</p>
<dt><code>Python3_PyPy_VERSION</code></p>
<dd>New in version 3.18. </p>
<p> Python 3 PyPy version.</p>
<dt><code>Python3_NumPy_FOUND</code></p>
<dd>New in version 3.14. </p>
<p> System has the NumPy.</p>
<dt><code>Python3_NumPy_INCLUDE_DIRS</code></p>
<dd>New in version 3.14. </p>
<p> The NumPy include directories.</p>
<dt><code>Python3_NumPy_VERSION</code></p>
<dd>New in version 3.14. </p>
<p> The NumPy version.</dl>
<h3>Hints</h3>
<dl>
<dt><code>Python3_ROOT_DIR</code></p>
<dd>Define the root directory of a Python 3 installation.</p>
<dt><code>Python3_USE_STATIC_LIBS</code></p>
<dd>
<dt>&bull;</p>
<dd>If not defined, search for shared libraries and static libraries in that order.</p>
<dt>&bull;</p>
<dd>If set to TRUE, search <code>only</code> for static libraries.</p>
<dt>&bull;</p>
<dd>If set to FALSE, search <code>only</code> for shared libraries. </p>
<p> <code>NOTE:</code> This hint will be ignored on <code>Windows</code> because static libraries are not available on this platform.</p>
<dt><code>Python3_FIND_ABI</code></p>
<dd>New in version 3.16. </p>
<p> This variable defines which ABIs, as defined in <i>PEP 3149</i>, should be searched. </p>
<p> <code>NOTE:</code> If <code>Python3_FIND_ABI</code> is not defined, any ABI will be searched. </p>
<p> The <code>Python3_FIND_ABI</code> variable is a 3-tuple specifying, in that order, <code>pydebug</code> (<code>d</code>), <code>pymalloc</code> (<code>m</code>) and <code>unicode</code> (<code>u</code>) flags. Each element can be set to one of the following:</p>
<dt>&bull;</p>
<dd><code>ON</code>: Corresponding flag is selected.</p>
<dt>&bull;</p>
<dd><code>OFF</code>: Corresponding flag is not selected.</p>
<dt>&bull;</p>
<dd><code>ANY</code>: The two possibilities (<code>ON</code> and <code>OFF</code>) will be searched. </p>
<p> From this 3-tuple, various ABIs will be searched starting from the most specialized to the most general. Moreover, <code>debug</code> versions will be searched <code>after</code> <code>non-debug</code> ones. </p>
<p> For example, if we have: </p>
<pre>set (Python3_FIND_ABI &quot;ON&quot; &quot;ANY&quot; &quot;ANY&quot;)</pre>
<p>The following flags combinations will be appended, in that order, to the artifact names: <code>dmu</code>, <code>dm</code>, <code>du</code>, and <code>d</code>. </p>
<p> And to search any possible ABIs: </p>
<pre>set (Python3_FIND_ABI &quot;ANY&quot; &quot;ANY&quot; &quot;ANY&quot;)</pre>
<p>The following combinations, in that order, will be used: <code>mu</code>, <code>m</code>, <code>u</code>, <code>&lt;empty&gt;</code>, <code>dmu</code>, <code>dm</code>, <code>du</code> and <code>d</code>. </p>
<p> <code>NOTE:</code> This hint is useful only on <code>POSIX</code> systems. So, on <code>Windows</code> systems, when <code>Python3_FIND_ABI</code> is defined, <code>Python</code> distributions from <i>python.org</i> will be found only if value for each flag is <code>OFF</code> or <code>ANY</code>.</p>
<dt><code>Python3_FIND_STRATEGY</code></p>
<dd>New in version 3.15. </p>
<p> This variable defines how lookup will be done. The <code>Python3_FIND_STRATEGY</code> variable can be set to one of the following:</p>
<dt>&bull;</p>
<dd><code>VERSION</code>: Try to find the most recent version in all specified locations. This is the default if policy <code>CMP0094</code> is undefined or set to <code>OLD</code>.</p>
<dt>&bull;</p>
<dd><code>LOCATION</code>: Stops lookup as soon as a version satisfying version constraints is founded. This is the default if policy <code>CMP0094</code> is set to <code>NEW</code>.</p>
<dt><code>Python3_FIND_REGISTRY</code></p>
<dd>New in version 3.13. </p>
<p> On Windows the <code>Python3_FIND_REGISTRY</code> variable determine the order of preference between registry and environment variables. The <code>Python3_FIND_REGISTRY</code> variable can be set to one of the following:</p>
<dt>&bull;</p>
<dd><code>FIRST</code>: Try to use registry before environment variables. This is the default.</p>
<dt>&bull;</p>
<dd><code>LAST</code>: Try to use registry after environment variables.</p>
<dt>&bull;</p>
<dd><code>NEVER</code>: Never try to use registry.</p>
<dt><code>Python3_FIND_FRAMEWORK</code></p>
<dd>New in version 3.15. </p>
<p> On macOS the <code>Python3_FIND_FRAMEWORK</code> variable determine the order of preference between Apple-style and unix-style package components. This variable can take same values as <code>CMAKE_FIND_FRAMEWORK</code> variable. </p>
<p> <code>NOTE:</code> Value <code>ONLY</code> is not supported so <code>FIRST</code> will be used instead. </p>
<p> If <code>Python3_FIND_FRAMEWORK</code> is not defined, <code>CMAKE_FIND_FRAMEWORK</code> variable will be used, if any.</p>
<dt><code>Python3_FIND_VIRTUALENV</code></p>
<dd>New in version 3.15. </p>
<p> This variable defines the handling of virtual environments managed by <code>virtualenv</code> or <code>conda</code>. It is meaningful only when a virtual environment is active (i.e. the <code>activate</code> script has been evaluated). In this case, it takes precedence over <code>Python3_FIND_REGISTRY</code> and <code>CMAKE_FIND_FRAMEWORK</code> variables. The <code>Python3_FIND_VIRTUALENV</code> variable can be set to one of the following:</p>
<dt>&bull;</p>
<dd><code>FIRST</code>: The virtual environment is used before any other standard paths to look-up for the interpreter. This is the default.</p>
<dt>&bull;</p>
<dd><code>ONLY</code>: Only the virtual environment is used to look-up for the interpreter.</p>
<dt>&bull;</p>
<dd><code>STANDARD</code>: The virtual environment is not used to look-up for the interpreter but environment variable <code>PATH</code> is always considered. In this case, variable <code>Python3_FIND_REGISTRY</code> (Windows) or <code>CMAKE_FIND_FRAMEWORK</code> (macOS) can be set with value <code>LAST</code> or <code>NEVER</code> to select preferably the interpreter from the virtual environment. </p>
<p> New in version 3.17: Added support for <code>conda</code> environments. </p>
<p> <code>NOTE:</code> If the component <code>Development</code> is requested, it is <code>strongly</code> recommended to also include the component <code>Interpreter</code> to get expected result.</p>
<dt><code>Python3_FIND_IMPLEMENTATIONS</code></p>
<dd>New in version 3.18. </p>
<p> This variable defines, in an ordered list, the different implementations which will be searched. The <code>Python3_FIND_IMPLEMENTATIONS</code> variable can hold the following values:</p>
<dt>&bull;</p>
<dd><code>CPython</code>: this is the standard implementation. Various products, like <code>Anaconda</code> or <code>ActivePython</code>, rely on this implementation.</p>
<dt>&bull;</p>
<dd><code>IronPython</code>: This implementation use the <code>CSharp</code> language for <code>.NET Framework</code> on top of the <i>Dynamic Language Runtime</i> (<code>DLR</code>). See <i>IronPython</i>.</p>
<dt>&bull;</p>
<dd><code>PyPy</code>: This implementation use <code>RPython</code> language and <code>RPython translation toolchain</code> to produce the python interpreter. See <i>PyPy</i>. </p>
<p> The default value is:</p>
<dt>&bull;</p>
<dd>Windows platform: <code>CPython</code>, <code>IronPython</code></p>
<dt>&bull;</p>
<dd>Other platforms: <code>CPython</code> </p>
<p> <code>NOTE:</code> This hint has the lowest priority of all hints, so even if, for example, you specify <code>IronPython</code> first and <code>CPython</code> in second, a python product based on <code>CPython</code> can be selected because, for example with <code>Python3_FIND_STRATEGY=LOCATION</code>, each location will be search first for <code>IronPython</code> and second for <code>CPython</code>. </p>
<p> <code>NOTE:</code> When <code>IronPython</code> is specified, on platforms other than <code>Windows</code>, the <code>.Net</code> interpreter (i.e. <code>mono</code> command) is expected to be available through the <code>PATH</code> variable.</p>
<dt><code>Python3_FIND_UNVERSIONED_NAMES</code></p>
<dd>New in version 3.20. </p>
<p> This variable defines how the generic names will be searched. Currently, it only applies to the generic names of the interpreter, namely, <code>python3</code> and <code>python</code>. The <code>Python3_FIND_UNVERSIONED_NAMES</code> variable can be set to one of the following values:</p>
<dt>&bull;</p>
<dd><code>FIRST</code>: The generic names are searched before the more specialized ones (such as <code>python3.5</code> for example).</p>
<dt>&bull;</p>
<dd><code>LAST</code>: The generic names are searched after the more specialized ones. This is the default.</p>
<dt>&bull;</p>
<dd><code>NEVER</code>: The generic name are not searched at all.</dl>
<h3>Artifacts Specification</h3>
<p>New in version 3.16. </p>
<p> To solve special cases, it is possible to specify directly the artifacts by setting the following variables:</p>
<dl>
<dt><code>Python3_EXECUTABLE</code></p>
<dd>The path to the interpreter.</p>
<dt><code>Python3_COMPILER</code></p>
<dd>The path to the compiler.</p>
<dt><code>Python3_DOTNET_LAUNCHER</code></p>
<dd>New in version 3.18. </p>
<p> The <code>.Net</code> interpreter. Only used by <code>IronPython</code> implementation.</p>
<dt><code>Python3_LIBRARY</code></p>
<dd>The path to the library. It will be used to compute the variables <code>Python3_LIBRARIES</code>, <code>Python3_LIBRARY_DIRS</code> and <code>Python3_RUNTIME_LIBRARY_DIRS</code>.</p>
<dt><code>Python3_INCLUDE_DIR</code></p>
<dd>The path to the directory of the <code>Python</code> headers. It will be used to compute the variable <code>Python3_INCLUDE_DIRS</code>.</p>
<dt><code>Python3_NumPy_INCLUDE_DIR</code></p>
<dd>The path to the directory of the <code>NumPy</code> headers. It will be used to compute the variable <code>Python3_NumPy_INCLUDE_DIRS</code>. </p>
<p> <code>NOTE:</code> All paths must be absolute. Any artifact specified with a relative path will be ignored. </p>
<p> <code>NOTE:</code> When an artifact is specified, all <code>HINTS</code> will be ignored and no search will be performed for this artifact. </p>
<p> If more than one artifact is specified, it is the user&#8217;s responsibility to ensure the consistency of the various artifacts. </p>
<p> By default, this module supports multiple calls in different directories of a project with different version/component requirements while providing correct and consistent results for each call. To support this behavior, <code>CMake</code> cache is not used in the traditional way which can be problematic for interactive specification. So, to enable also interactive specification, module behavior can be controlled with the following variable:</p>
<dt><code>Python3_ARTIFACTS_INTERACTIVE</code></p>
<dd>New in version 3.18. </p>
<p> Selects the behavior of the module. This is a boolean variable:</p>
<dt>&bull;</p>
<dd>If set to <code>TRUE</code>: Create CMake cache entries for the above artifact specification variables so that users can edit them interactively. This disables support for multiple version/component requirements.</p>
<dt>&bull;</p>
<dd>If set to <code>FALSE</code> or undefined: Enable multiple version/component requirements.</dl>
<h3>Commands</h3>
<p>This module defines the command <code>Python3_add_library</code> (when <code>CMAKE_ROLE</code> is <code>PROJECT</code>), which has the same semantics as <code>add_library()</code> and adds a dependency to target <code>Python3::Python</code> or, when library type is <code>MODULE</code>, to target <code>Python3::Module</code> and takes care of Python module naming rules: </p>
<pre>Python3_add_library (&lt;name&gt; [STATIC | SHARED | MODULE [WITH_SOABI]]
 &lt;source1&gt; [&lt;source2&gt; ...])</pre>
<p>If the library type is not specified, <code>MODULE</code> is assumed. </p>
<p> New in version 3.17: For <code>MODULE</code> library type, if option <code>WITH_SOABI</code> is specified, the module suffix will include the <code>Python3_SOABI</code> value, if any.</p>
<h3>FindQt3</h3>
<p>Locate Qt include paths and libraries </p>
<p> This module defines: </p>
<pre>QT_INCLUDE_DIR - where to find qt.h, etc.
QT_LIBRARIES - the libraries to link against to use Qt.
QT_DEFINITIONS - definitions to use when
 compiling code that uses Qt.
QT_FOUND - If false, don't try to use Qt.
QT_VERSION_STRING - the version of Qt found</pre>
<p>If you need the multithreaded version of Qt, set QT_MT_REQUIRED to TRUE </p>
<p> Also defined, but not for general use are: </p>
<pre>QT_MOC_EXECUTABLE, where to find the moc tool.
QT_UIC_EXECUTABLE, where to find the uic tool.
QT_QT_LIBRARY, where to find the Qt library.
QT_QTMAIN_LIBRARY, where to find the qtmain
 library. This is only required by Qt3 on Windows.</pre>
<h3>FindQt4</h3>
<h3>Finding and Using Qt4</h3>
<p>This module can be used to find Qt4. The most important issue is that the Qt4 qmake is available via the system path. This qmake is then used to detect basically everything else. This module defines a number of <code>IMPORTED</code> targets, macros and variables. </p>
<p> Typical usage could be something like: </p>
<pre>set(CMAKE_AUTOMOC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
find_package(Qt4 4.4.3 REQUIRED QtGui QtXml)
add_executable(myexe main.cpp)
target_link_libraries(myexe Qt4::QtGui Qt4::QtXml)</pre>
<p><code>NOTE:</code> When using <code>IMPORTED</code> targets, the qtmain.lib static library is automatically linked on Windows for <code>WIN32</code> executables. To disable that globally, set the <code>QT4_NO_LINK_QTMAIN</code> variable before finding Qt4. To disable that for a particular executable, set the <code>QT4_NO_LINK_QTMAIN</code> target property to <code>TRUE</code> on the executable.</p>
<h3>Qt Build Tools</h3>
<p>Qt relies on some bundled tools for code generation, such as <code>moc</code> for meta-object code generation,&#8220;uic&#8220; for widget layout and population, and <code>rcc</code> for virtual filesystem content generation. These tools may be automatically invoked by <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> if the appropriate conditions are met. See <code><a href="/docs/linux/man/7-cmake-qt/">cmake-qt</a>(7)</code> for more.</p>
<h3>Qt Macros</h3>
<p>In some cases it can be necessary or useful to invoke the Qt build tools in a more-manual way. Several macros are available to add targets for such uses. </p>
<pre>macro QT4_WRAP_CPP(outfiles inputfile ... [TARGET tgt] OPTIONS ...)
 create moc code from a list of files containing Qt class with
 the Q_OBJECT declaration. Per-directory preprocessor definitions
 are also added. If the &lt;tgt&gt; is specified, the
 INTERFACE_INCLUDE_DIRECTORIES and INTERFACE_COMPILE_DEFINITIONS from
 the &lt;tgt&gt; are passed to moc. Options may be given to moc, such as
 those found when executing &quot;moc -help&quot;.</pre>
<pre>macro QT4_WRAP_UI(outfiles inputfile ... OPTIONS ...)
 create code from a list of Qt designer ui files.
 Options may be given to uic, such as those found
 when executing &quot;uic -help&quot;</pre>
<pre>macro QT4_ADD_RESOURCES(outfiles inputfile ... OPTIONS ...)
 create code from a list of Qt resource files.
 Options may be given to rcc, such as those found
 when executing &quot;rcc -help&quot;</pre>
<pre>macro QT4_GENERATE_MOC(inputfile outputfile [TARGET tgt])
 creates a rule to run moc on infile and create outfile.
 Use this if for some reason QT4_WRAP_CPP() isn't appropriate, e.g.
 because you need a custom filename for the moc file or something
 similar. If the &lt;tgt&gt; is specified, the
 INTERFACE_INCLUDE_DIRECTORIES and INTERFACE_COMPILE_DEFINITIONS from
 the &lt;tgt&gt; are passed to moc.</pre>
<pre>macro QT4_ADD_DBUS_INTERFACE(outfiles interface basename)
 Create the interface header and implementation files with the
 given basename from the given interface xml file and add it to
 the list of sources.
 You can pass additional parameters to the qdbusxml2cpp call by setting
 properties on the input file:
 INCLUDE the given file will be included in the generate interface header
 CLASSNAME the generated class is named accordingly
 NO_NAMESPACE the generated class is not wrapped in a namespace</pre>
<pre>macro QT4_ADD_DBUS_INTERFACES(outfiles inputfile ... )
 Create the interface header and implementation files
 for all listed interface xml files.
 The basename will be automatically determined from the name
 of the xml file.
 The source file properties described for
 QT4_ADD_DBUS_INTERFACE also apply here.</pre>
<pre>macro QT4_ADD_DBUS_ADAPTOR(outfiles xmlfile parentheader parentclassname
 [basename] [classname])
 create a dbus adaptor (header and implementation file) from the xml file
 describing the interface, and add it to the list of sources. The adaptor
 forwards the calls to a parent class, defined in parentheader and named
 parentclassname. The name of the generated files will be
 &lt;basename&gt;adaptor.{cpp,h} where basename defaults to the basename of the
 xml file.
 If &lt;classname&gt; is provided, then it will be used as the classname of the
 adaptor itself.</pre>
<pre>macro QT4_GENERATE_DBUS_INTERFACE( header [interfacename] OPTIONS ...)
 generate the xml interface file from the given header.
 If the optional argument interfacename is omitted, the name of the
 interface file is constructed from the basename of the header with
 the suffix .xml appended.
 Options may be given to qdbuscpp2xml, such as those found when
 executing &quot;qdbuscpp2xml --help&quot;</pre>
<pre>macro QT4_CREATE_TRANSLATION( qm_files directories ... sources ...
 ts_files ... OPTIONS ...)
 out: qm_files
 in: directories sources ts_files
 options: flags to pass to lupdate, such as -extensions to specify
 extensions for a directory scan.
 generates commands to create .ts (via lupdate) and .qm
 (via lrelease) - files from directories and/or sources. The ts files are
 created and/or updated in the source tree (unless given with full paths).
 The qm files are generated in the build tree.
 Updating the translations can be done by adding the qm_files
 to the source list of your library/executable, so they are
 always updated, or by adding a custom target to control when
 they get updated/generated.</pre>
<pre>macro QT4_ADD_TRANSLATION( qm_files ts_files ... )
 out: qm_files
 in: ts_files
 generates commands to create .qm from .ts - files. The generated
 filenames can be found in qm_files. The ts_files
 must exist and are not updated in any way.</pre>
<pre>macro QT4_AUTOMOC(sourcefile1 sourcefile2 ... [TARGET tgt])
 The qt4_automoc macro is obsolete. Use the CMAKE_AUTOMOC feature instead.
 This macro is still experimental.
 It can be used to have moc automatically handled.
 So if you have the files foo.h and foo.cpp, and in foo.h a
 a class uses the Q_OBJECT macro, moc has to run on it. If you don't
 want to use QT4_WRAP_CPP() (which is reliable and mature), you can insert
 #include &quot;foo.moc&quot;
 in foo.cpp and then give foo.cpp as argument to QT4_AUTOMOC(). This will
 scan all listed files at cmake-time for such included moc files and if it
 finds them cause a rule to be generated to run moc at build time on the
 accompanying header file foo.h.
 If a source file has the SKIP_AUTOMOC property set it will be ignored by
 this macro.
 If the &lt;tgt&gt; is specified, the INTERFACE_INCLUDE_DIRECTORIES and
 INTERFACE_COMPILE_DEFINITIONS from the &lt;tgt&gt; are passed to moc.</pre>
<pre>function QT4_USE_MODULES( target [link_type] modules...)
 This function is obsolete. Use target_link_libraries with IMPORTED targets
 instead.
 Make &lt;target&gt; use the &lt;modules&gt; from Qt. Using a Qt module means
 to link to the library, add the relevant include directories for the
 module, and add the relevant compiler defines for using the module.
 Modules are roughly equivalent to components of Qt4, so usage would be
 something like:
 qt4_use_modules(myexe Core Gui Declarative)
 to use QtCore, QtGui and QtDeclarative. The optional &lt;link_type&gt; argument
 can be specified as either LINK_PUBLIC or LINK_PRIVATE to specify the
 same argument to the target_link_libraries call.</pre>
<h3>IMPORTED Targets</h3>
<p>A particular Qt library may be used by using the corresponding <code>IMPORTED</code> target with the <code>target_link_libraries()</code> command: </p>
<pre>target_link_libraries(myexe Qt4::QtGui Qt4::QtXml)</pre>
<p>Using a target in this way causes <a href="/docs/linux/man/1--cmake/">:cmake</a>(1)` to use the appropriate include directories and compile definitions for the target when compiling <code>myexe</code>. </p>
<p> Targets are aware of their dependencies, so for example it is not necessary to list <code>Qt4::QtCore</code> if another Qt library is listed, and it is not necessary to list <code>Qt4::QtGui</code> if <code>Qt4::QtDeclarative</code> is listed. Targets may be tested for existence in the usual way with the <code>if(TARGET)</code> command. </p>
<p> The Qt toolkit may contain both debug and release libraries. <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> will choose the appropriate version based on the build configuration.</p>
<dl>
<dt><code>Qt4::QtCore</code></p>
<dd>The QtCore target</p>
<dt><code>Qt4::QtGui</code></p>
<dd>The QtGui target</p>
<dt><code>Qt4::Qt3Support</code></p>
<dd>The Qt3Support target</p>
<dt><code>Qt4::QtAssistant</code></p>
<dd>The QtAssistant target</p>
<dt><code>Qt4::QtAssistantClient</code></p>
<dd>The QtAssistantClient target</p>
<dt><code>Qt4::QAxContainer</code></p>
<dd>The QAxContainer target (Windows only)</p>
<dt><code>Qt4::QAxServer</code></p>
<dd>The QAxServer target (Windows only)</p>
<dt><code>Qt4::QtDBus</code></p>
<dd>The QtDBus target</p>
<dt><code>Qt4::QtDeclarative</code></p>
<dd>The QtDeclarative target</p>
<dt><code>Qt4::QtDesigner</code></p>
<dd>The QtDesigner target</p>
<dt><code>Qt4::QtDesignerComponents</code></p>
<dd>The QtDesignerComponents target</p>
<dt><code>Qt4::QtHelp</code></p>
<dd>The QtHelp target</p>
<dt><code>Qt4::QtMotif</code></p>
<dd>The QtMotif target</p>
<dt><code>Qt4::QtMultimedia</code></p>
<dd>The QtMultimedia target</p>
<dt><code>Qt4::QtNetwork</code></p>
<dd>The QtNetwork target</p>
<dt><code>Qt4::QtNsPLugin</code></p>
<dd>The QtNsPLugin target</p>
<dt><code>Qt4::QtOpenGL</code></p>
<dd>The QtOpenGL target</p>
<dt><code>Qt4::QtScript</code></p>
<dd>The QtScript target</p>
<dt><code>Qt4::QtScriptTools</code></p>
<dd>The QtScriptTools target</p>
<dt><code>Qt4::QtSql</code></p>
<dd>The QtSql target</p>
<dt><code>Qt4::QtSvg</code></p>
<dd>The QtSvg target</p>
<dt><code>Qt4::QtTest</code></p>
<dd>The QtTest target</p>
<dt><code>Qt4::QtUiTools</code></p>
<dd>The QtUiTools target</p>
<dt><code>Qt4::QtWebKit</code></p>
<dd>The QtWebKit target</p>
<dt><code>Qt4::QtXml</code></p>
<dd>The QtXml target</p>
<dt><code>Qt4::QtXmlPatterns</code></p>
<dd>The QtXmlPatterns target</p>
<dt><code>Qt4::phonon</code></p>
<dd>The phonon target</dl>
<h3>Result Variables</h3>
<p>Below is a detailed list of variables that FindQt4.cmake sets.</p>
<dl>
<dt><code>Qt4_FOUND</code></p>
<dd>If false, don&#8217;t try to use Qt 4.</p>
<dt><code>QT_FOUND</code></p>
<dd>If false, don&#8217;t try to use Qt. This variable is for compatibility only.</p>
<dt><code>QT4_FOUND</code></p>
<dd>If false, don&#8217;t try to use Qt 4. This variable is for compatibility only.</p>
<dt><code>QT_VERSION_MAJOR</code></p>
<dd>The major version of Qt found.</p>
<dt><code>QT_VERSION_MINOR</code></p>
<dd>The minor version of Qt found.</p>
<dt><code>QT_VERSION_PATCH</code></p>
<dd>The patch version of Qt found.</dl>
<h3>FindQuickTime</h3>
<p>Locate QuickTime This module defines QUICKTIME_LIBRARY QUICKTIME_FOUND, if false, do not try to link to gdal QUICKTIME_INCLUDE_DIR, where to find the headers </p>
<p> $QUICKTIME_DIR is an environment variable that would correspond to the ./configure &#8211;prefix=$QUICKTIME_DIR </p>
<p> Created by Eric Wing.</p>
<h3>FindRTI</h3>
<p>Try to find M&amp;S HLA RTI libraries </p>
<p> This module finds if any HLA RTI is installed and locates the standard RTI include files and libraries. </p>
<p> RTI is a simulation infrastructure standardized by IEEE and SISO. It has a well defined C++ API that assures that simulation applications are independent on a particular RTI implementation. </p>
<pre><a rel="nofollow" href="http://en.wikipedia.org/wiki/Run-Time_Infrastructure_(simulation)">http://en.wikipedia.org/wiki/Run-Time_Infrastructure_(simulation)</a></pre>
<p>This code sets the following variables: </p>
<pre>RTI_INCLUDE_DIR = the directory where RTI includes file are found
RTI_LIBRARIES = The libraries to link against to use RTI
RTI_DEFINITIONS = -DRTI_USES_STD_FSTREAM
RTI_FOUND = Set to FALSE if any HLA RTI was not found</pre>
<p>Report problems to &lt;<i>certi-devel [at] nongnu.org</i>&gt;</p>
<h3>FindRuby</h3>
<p>Find Ruby </p>
<p> This module finds if Ruby is installed and determines where the include files and libraries are. Ruby 1.8 through 2.7 are supported. </p>
<p> The minimum required version of Ruby can be specified using the standard syntax, e.g. </p>
<pre>find_package(Ruby 2.5.1 EXACT REQUIRED)
# OR
find_package(Ruby 2.4)</pre>
<p>It also determines what the name of the library is. </p>
<p> Virtual environments such as RVM are handled as well, by passing the argument <code>Ruby_FIND_VIRTUALENV</code></p>
<h3>Result Variables</h3>
<p>This module will set the following variables in your project:</p>
<dl>
<dt><code>Ruby_FOUND</code></p>
<dd>set to true if ruby was found successfully</p>
<dt><code>Ruby_EXECUTABLE</code></p>
<dd>full path to the ruby binary</p>
<dt><code>Ruby_INCLUDE_DIRS</code></p>
<dd>include dirs to be used when using the ruby library</p>
<dt><code>Ruby_LIBRARIES</code></p>
<dd>New in version 3.18: libraries needed to use ruby from C. </p>
<dt><code>Ruby_VERSION</code></p>
<dd>the version of ruby which was found, e.g. &quot;1.8.7&quot;</p>
<dt><code>Ruby_VERSION_MAJOR</code></p>
<dd>Ruby major version.</p>
<dt><code>Ruby_VERSION_MINOR</code></p>
<dd>Ruby minor version.</p>
<dt><code>Ruby_VERSION_PATCH</code></p>
<dd>Ruby patch version. </p>
<p> Changed in version 3.18: Previous versions of CMake used the <code>RUBY_</code> prefix for all variables. The following variables are provided for compatibility reasons, don&#8217;t use them in new code: </p>
<dt><code>RUBY_EXECUTABLE</code></p>
<dd>same as Ruby_EXECUTABLE.</p>
<dt><code>RUBY_INCLUDE_DIRS</code></p>
<dd>same as Ruby_INCLUDE_DIRS.</p>
<dt><code>RUBY_INCLUDE_PATH</code></p>
<dd>same as Ruby_INCLUDE_DIRS.</p>
<dt><code>RUBY_LIBRARY</code></p>
<dd>same as Ruby_LIBRARY.</p>
<dt><code>RUBY_VERSION</code></p>
<dd>same as Ruby_VERSION.</p>
<dt><code>RUBY_FOUND</code></p>
<dd>same as Ruby_FOUND.</dl>
<h3>Hints</h3>
<p>New in version 3.18. </p>
<dl>
<dt><code>Ruby_ROOT_DIR</code></p>
<dd>Define the root directory of a Ruby installation.</p>
<dt><code>Ruby_FIND_VIRTUALENV</code></p>
<dd>This variable defines the handling of virtual environments managed by <code>rvm</code>. It is meaningful only when a virtual environment is active (i.e. the <code>rvm</code> script has been evaluated or at least the <code>MY_RUBY_HOME</code> environment variable is set). The <code>Ruby_FIND_VIRTUALENV</code> variable can be set to empty or one of the following:</p>
<dt>&bull;</p>
<dd><code>FIRST</code>: The virtual environment is used before any other standard paths to look-up for the interpreter. This is the default.</p>
<dt>&bull;</p>
<dd><code>ONLY</code>: Only the virtual environment is used to look-up for the interpreter.</p>
<dt>&bull;</p>
<dd><code>STANDARD</code>: The virtual environment is not used to look-up for the interpreter (assuming it isn&#8217;t still in the PATH&#8230;)</dl>
<h3>FindSDL</h3>
<p>Locate the SDL library</p>
<h3>Imported targets</h3>
<p>New in version 3.19. </p>
<p> This module defines the following <code>IMPORTED</code> target:</p>
<dl>
<dt><code>SDL::SDL</code></p>
<dd>The SDL library, if found</dl>
<h3>Result variables</h3>
<p>This module will set the following variables in your project:</p>
<dl>
<dt><code>SDL_INCLUDE_DIRS</code></p>
<dd>where to find SDL.h</p>
<dt><code>SDL_LIBRARIES</code></p>
<dd>the name of the library to link against</p>
<dt><code>SDL_FOUND</code></p>
<dd>if false, do not try to link to SDL</p>
<dt><code>SDL_VERSION</code></p>
<dd>the human-readable string containing the version of SDL if found</p>
<dt><code>SDL_VERSION_MAJOR</code></p>
<dd>SDL major version</p>
<dt><code>SDL_VERSION_MINOR</code></p>
<dd>SDL minor version</p>
<dt><code>SDL_VERSION_PATCH</code></p>
<dd>SDL patch version </p>
<p> New in version 3.19: Added the <code>SDL_INCLUDE_DIRS</code>, <code>SDL_LIBRARIES</code> and <code>SDL_VERSION[_&lt;PART&gt;]</code> variables. </p>
</dl>
<h3>Cache variables</h3>
<p>These variables may optionally be set to help this module find the correct files:</p>
<dl>
<dt><code>SDL_INCLUDE_DIR</code></p>
<dd>where to find SDL.h</p>
<dt><code>SDL_LIBRARY</code></p>
<dd>the name of the library to link against</dl>
<h3>Variables for locating SDL</h3>
<p>This module responds to the flag:</p>
<dl>
<dt><code>SDL_BUILDING_LIBRARY</code></p>
<dd>If this is defined, then no SDL_main will be linked in because only applications need main(). Otherwise, it is assumed you are building an application and this module will attempt to locate and set the proper link flags as part of the returned SDL_LIBRARY variable.</dl>
<h3>Obsolete variables</h3>
<p>Deprecated since version 3.19. </p>
<p> These variables are obsolete and provided for backwards compatibility:</p>
<dl>
<dt><code>SDL_VERSION_STRING</code></p>
<dd>the human-readable string containing the version of SDL if found. Identical to SDL_VERSION </p>
<p> Don&#8217;t forget to include SDLmain.h and SDLmain.m your project for the OS X framework based version. (Other versions link to -lSDLmain which this module will try to find on your behalf.) Also for OS X, this module will automatically add the -framework Cocoa on your behalf. </p>
<p> Additional Note: If you see an empty SDL_LIBRARY_TEMP in your configuration and no SDL_LIBRARY, it means CMake did not find your SDL library (SDL.dll, libsdl.so, SDL.framework, etc). Set SDL_LIBRARY_TEMP to point to your SDL library, and configure again. Similarly, if you see an empty SDLMAIN_LIBRARY, you should set this value as appropriate. These values are used to generate the final SDL_LIBRARY variable, but when these values are unset, SDL_LIBRARY does not get created. </p>
<p> $SDLDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$SDLDIR used in building SDL. l.e.galup 9-20-02 </p>
<p> On OSX, this will prefer the Framework version (if found) over others. People will have to manually change the cache values of SDL_LIBRARY to override this selection or set the CMake environment CMAKE_INCLUDE_PATH to modify the search paths. </p>
<p> Note that the header path has changed from SDL/SDL.h to just SDL.h This needed to change because &quot;proper&quot; SDL convention is #include &quot;SDL.h&quot;, not &lt;SDL/SDL.h&gt;. This is done for portability reasons because not all systems place things in SDL/ (see FreeBSD).</dl>
<h3>FindSDL_image</h3>
<p>Locate SDL_image library </p>
<p> This module defines: </p>
<pre>SDL_IMAGE_LIBRARIES, the name of the library to link against
SDL_IMAGE_INCLUDE_DIRS, where to find the headers
SDL_IMAGE_FOUND, if false, do not try to link against
SDL_IMAGE_VERSION_STRING - human-readable string containing the
 version of SDL_image</pre>
<p>For backward compatibility the following variables are also set: </p>
<pre>SDLIMAGE_LIBRARY (same value as SDL_IMAGE_LIBRARIES)
SDLIMAGE_INCLUDE_DIR (same value as SDL_IMAGE_INCLUDE_DIRS)
SDLIMAGE_FOUND (same value as SDL_IMAGE_FOUND)</pre>
<p>$SDLDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$SDLDIR used in building SDL. </p>
<p> Created by Eric Wing. This was influenced by the FindSDL.cmake module, but with modifications to recognize OS X frameworks and additional Unix paths (FreeBSD, etc).</p>
<h3>FindSDL_mixer</h3>
<p>Locate SDL_mixer library </p>
<p> This module defines: </p>
<pre>SDL_MIXER_LIBRARIES, the name of the library to link against
SDL_MIXER_INCLUDE_DIRS, where to find the headers
SDL_MIXER_FOUND, if false, do not try to link against
SDL_MIXER_VERSION_STRING - human-readable string containing the
 version of SDL_mixer</pre>
<p>For backward compatibility the following variables are also set: </p>
<pre>SDLMIXER_LIBRARY (same value as SDL_MIXER_LIBRARIES)
SDLMIXER_INCLUDE_DIR (same value as SDL_MIXER_INCLUDE_DIRS)
SDLMIXER_FOUND (same value as SDL_MIXER_FOUND)</pre>
<p>$SDLDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$SDLDIR used in building SDL. </p>
<p> Created by Eric Wing. This was influenced by the FindSDL.cmake module, but with modifications to recognize OS X frameworks and additional Unix paths (FreeBSD, etc).</p>
<h3>FindSDL_net</h3>
<p>Locate SDL_net library </p>
<p> This module defines: </p>
<pre>SDL_NET_LIBRARIES, the name of the library to link against
SDL_NET_INCLUDE_DIRS, where to find the headers
SDL_NET_FOUND, if false, do not try to link against
SDL_NET_VERSION_STRING - human-readable string containing the version of SDL_net</pre>
<p>For backward compatibility the following variables are also set: </p>
<pre>SDLNET_LIBRARY (same value as SDL_NET_LIBRARIES)
SDLNET_INCLUDE_DIR (same value as SDL_NET_INCLUDE_DIRS)
SDLNET_FOUND (same value as SDL_NET_FOUND)</pre>
<p>$SDLDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$SDLDIR used in building SDL. </p>
<p> Created by Eric Wing. This was influenced by the FindSDL.cmake module, but with modifications to recognize OS X frameworks and additional Unix paths (FreeBSD, etc).</p>
<h3>FindSDL_sound</h3>
<p>Locates the SDL_sound library </p>
<p> This module depends on SDL being found and must be called AFTER FindSDL.cmake is called. </p>
<p> This module defines </p>
<pre>SDL_SOUND_INCLUDE_DIR, where to find SDL_sound.h
SDL_SOUND_FOUND, if false, do not try to link to SDL_sound
SDL_SOUND_LIBRARIES, this contains the list of libraries that you need
 to link against.
SDL_SOUND_EXTRAS, this is an optional variable for you to add your own
 flags to SDL_SOUND_LIBRARIES. This is prepended to SDL_SOUND_LIBRARIES.
 This is available mostly for cases this module failed to anticipate for
 and you must add additional flags. This is marked as ADVANCED.
SDL_SOUND_VERSION_STRING, human-readable string containing the
 version of SDL_sound</pre>
<p>This module also defines (but you shouldn&#8217;t need to use directly) </p>
<pre>SDL_SOUND_LIBRARY, the name of just the SDL_sound library you would link
against. Use SDL_SOUND_LIBRARIES for you link instructions and not this one.</pre>
<p>And might define the following as needed </p>
<pre>MIKMOD_LIBRARY
MODPLUG_LIBRARY
OGG_LIBRARY
VORBIS_LIBRARY
SMPEG_LIBRARY
FLAC_LIBRARY
SPEEX_LIBRARY</pre>
<p>Typically, you should not use these variables directly, and you should use SDL_SOUND_LIBRARIES which contains SDL_SOUND_LIBRARY and the other audio libraries (if needed) to successfully compile on your system. </p>
<p> Created by Eric Wing. This module is a bit more complicated than the other FindSDL* family modules. The reason is that SDL_sound can be compiled in a large variety of different ways which are independent of platform. SDL_sound may dynamically link against other 3rd party libraries to get additional codec support, such as Ogg Vorbis, SMPEG, ModPlug, MikMod, FLAC, Speex, and potentially others. Under some circumstances which I don&#8217;t fully understand, there seems to be a requirement that dependent libraries of libraries you use must also be explicitly linked against in order to successfully compile. SDL_sound does not currently have any system in place to know how it was compiled. So this CMake module does the hard work in trying to discover which 3rd party libraries are required for building (if any). This module uses a brute force approach to create a test program that uses SDL_sound, and then tries to build it. If the build fails, it parses the error output for known symbol names to figure out which libraries are needed. </p>
<p> Responds to the $SDLDIR and $SDLSOUNDDIR environmental variable that would correspond to the ./configure &#8211;prefix=$SDLDIR used in building SDL. </p>
<p> On OSX, this will prefer the Framework version (if found) over others. People will have to manually change the cache values of SDL_LIBRARY to override this selectionor set the CMake environment CMAKE_INCLUDE_PATH to modify the search paths.</p>
<h3>FindSDL_ttf</h3>
<p>Locate SDL_ttf library </p>
<p> This module defines: </p>
<pre>SDL_TTF_LIBRARIES, the name of the library to link against
SDL_TTF_INCLUDE_DIRS, where to find the headers
SDL_TTF_FOUND, if false, do not try to link against
SDL_TTF_VERSION_STRING - human-readable string containing the version of SDL_ttf</pre>
<p>For backward compatibility the following variables are also set: </p>
<pre>SDLTTF_LIBRARY (same value as SDL_TTF_LIBRARIES)
SDLTTF_INCLUDE_DIR (same value as SDL_TTF_INCLUDE_DIRS)
SDLTTF_FOUND (same value as SDL_TTF_FOUND)</pre>
<p>$SDLDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$SDLDIR used in building SDL. </p>
<p> Created by Eric Wing. This was influenced by the FindSDL.cmake module, but with modifications to recognize OS X frameworks and additional Unix paths (FreeBSD, etc).</p>
<h3>FindSelfPackers</h3>
<p>Find upx </p>
<p> This module looks for some executable packers (i.e. software that compress executables or shared libs into on-the-fly self-extracting executables or shared libs. Examples: </p>
<pre>UPX: <a rel="nofollow" href="http://wildsau.idv.uni-linz.ac.at/mfx/upx.html">http://wildsau.idv.uni-linz.ac.at/mfx/upx.html</a></pre>
<h3>FindSquish</h3>
<p>&#8212; Typical Use </p>
<p> This module can be used to find Squish. </p>
<pre>SQUISH_FOUND If false, don't try to use Squish
SQUISH_VERSION The full version of Squish found
SQUISH_VERSION_MAJOR The major version of Squish found
SQUISH_VERSION_MINOR The minor version of Squish found
SQUISH_VERSION_PATCH The patch version of Squish found</pre>
<pre>SQUISH_INSTALL_DIR The Squish installation directory
 (containing bin, lib, etc)
SQUISH_SERVER_EXECUTABLE The squishserver executable
SQUISH_CLIENT_EXECUTABLE The squishrunner executable</pre>
<pre>SQUISH_INSTALL_DIR_FOUND Was the install directory found?
SQUISH_SERVER_EXECUTABLE_FOUND Was the server executable found?
SQUISH_CLIENT_EXECUTABLE_FOUND Was the client executable found?</pre>
<p>It provides the function squish_add_test() for adding a squish test to cmake using Squish &gt;= 4.x: </p>
<pre>squish_add_test(cmakeTestName
 AUT targetName SUITE suiteName TEST squishTestName
 [SETTINGSGROUP group] [PRE_COMMAND command] [POST_COMMAND command] )</pre>
<p>Changed in version 3.18: In previous CMake versions, this function was named <code>squish_v4_add_test</code>. </p>
<p> The arguments have the following meaning:</p>
<dl>
<dt><code>cmakeTestName</code></p>
<dd>this will be used as the first argument for add_test()</p>
<dt><code>AUT targetName</code></p>
<dd>the name of the cmake target which will be used as AUT, i.e. the executable which will be tested.</p>
<dt><code>SUITE suiteName</code></p>
<dd>this is either the full path to the squish suite, or just the last directory of the suite, i.e. the suite name. In this case the CMakeLists.txt which calls squish_add_test() must be located in the parent directory of the suite directory.</p>
<dt><code>TEST squishTestName</code></p>
<dd>the name of the squish test, i.e. the name of the subdirectory of the test inside the suite directory.</p>
<dt><code>SETTINGSGROUP group</code></p>
<dd>deprecated, this argument will be ignored.</p>
<dt><code>PRE_COMMAND command</code></p>
<dd>if specified, the given command will be executed before starting the squish test.</p>
<dt><code>POST_COMMAND command</code></p>
<dd>same as PRE_COMMAND, but after the squish test has been executed. </p>
<pre>enable_testing()
find_package(Squish 6.5)
if (SQUISH_FOUND)
 squish_add_test(myTestName
 AUT myApp
 SUITE ${CMAKE_SOURCE_DIR}/tests/mySuite
 TEST someSquishTest
 )
endif ()</pre>
<p>For users of Squish version 3.x the macro squish_v3_add_test() is provided: </p>
<pre>squish_v3_add_test(testName applicationUnderTest testCase envVars testWrapper)
Use this macro to add a test using Squish 3.x.</pre>
<pre>enable_testing()
find_package(Squish 3.0)
if (SQUISH_FOUND)
 squish_v3_add_test(myTestName myApplication testCase envVars testWrapper)
endif ()</pre>
</dl>
<h3>FindSQLite3</h3>
<p>New in version 3.14. </p>
<p> Find the SQLite libraries, v3</p>
<h3>IMPORTED targets</h3>
<p>This module defines the following <code>IMPORTED</code> target: </p>
<p> <code>SQLite::SQLite3</code></p>
<h3>Result variables</h3>
<p>This module will set the following variables if found:</p>
<dl>
<dt><code>SQLite3_INCLUDE_DIRS</code></p>
<dd>where to find sqlite3.h, etc.</p>
<dt><code>SQLite3_LIBRARIES</code></p>
<dd>the libraries to link against to use SQLite3.</p>
<dt><code>SQLite3_VERSION</code></p>
<dd>version of the SQLite3 library found</p>
<dt><code>SQLite3_FOUND</code></p>
<dd>TRUE if found</dl>
<h3>FindSubversion</h3>
<p>Extract information from a subversion working copy </p>
<p> The module defines the following variables: </p>
<pre>Subversion_SVN_EXECUTABLE - path to svn command line client
Subversion_VERSION_SVN - version of svn command line client
Subversion_FOUND - true if the command line client was found
SUBVERSION_FOUND - same as Subversion_FOUND, set for compatibility reasons</pre>
<p>The minimum required version of Subversion can be specified using the standard syntax, e.g. <code>find_package(Subversion 1.4)</code>. </p>
<p> If the command line client executable is found two macros are defined: </p>
<pre>Subversion_WC_INFO(&lt;dir&gt; &lt;var-prefix&gt; [IGNORE_SVN_FAILURE])
Subversion_WC_LOG(&lt;dir&gt; &lt;var-prefix&gt;)</pre>
<p><code>Subversion_WC_INFO</code> extracts information of a subversion working copy at a given location. This macro defines the following variables if running Subversion&#8217;s <code>info</code> command on <code>&lt;dir&gt;</code> succeeds; otherwise a <code>SEND_ERROR</code> message is generated. </p>
<p> New in version 3.13: The error can be ignored by providing the <code>IGNORE_SVN_FAILURE</code> option, which causes these variables to remain undefined. </p>
<pre>&lt;var-prefix&gt;_WC_URL - url of the repository (at &lt;dir&gt;)
&lt;var-prefix&gt;_WC_ROOT - root url of the repository
&lt;var-prefix&gt;_WC_REVISION - current revision
&lt;var-prefix&gt;_WC_LAST_CHANGED_AUTHOR - author of last commit
&lt;var-prefix&gt;_WC_LAST_CHANGED_DATE - date of last commit
&lt;var-prefix&gt;_WC_LAST_CHANGED_REV - revision of last commit
&lt;var-prefix&gt;_WC_INFO - output of command `svn info &lt;dir&gt;'</pre>
<p><code>Subversion_WC_LOG</code> retrieves the log message of the base revision of a subversion working copy at a given location. This macro defines the variable: </p>
<pre>&lt;var-prefix&gt;_LAST_CHANGED_LOG - last log of base revision</pre>
<p>Example usage: </p>
<pre>find_package(Subversion)
if(SUBVERSION_FOUND)
 Subversion_WC_INFO(${PROJECT_SOURCE_DIR} Project)
 message(&quot;Current revision is ${Project_WC_REVISION}&quot;)
 Subversion_WC_LOG(${PROJECT_SOURCE_DIR} Project)
 message(&quot;Last changed log is ${Project_LAST_CHANGED_LOG}&quot;)
endif()</pre>
<h3>FindSWIG</h3>
<p>Find the Simplified Wrapper and Interface Generator (<i>SWIG</i>) executable. </p>
<p> This module finds an installed SWIG and determines its version. </p>
<p> New in version 3.18: If a <code>COMPONENTS</code> or <code>OPTIONAL_COMPONENTS</code> argument is given to the <code>find_package()</code> command, it will also determine supported target languages. </p>
<p> New in version 3.19: When a version is requested, it can be specified as a simple value or as a range. For a detailed description of version range usage and capabilities, refer to the <code>find_package()</code> command. </p>
<p> The module defines the following variables:</p>
<dl>
<dt><code>SWIG_FOUND</code></p>
<dd>Whether SWIG and any required components were found on the system.</p>
<dt><code>SWIG_EXECUTABLE</code></p>
<dd>Path to the SWIG executable.</p>
<dt><code>SWIG_DIR</code></p>
<dd>Path to the installed SWIG <code>Lib</code> directory (result of <code>swig -swiglib</code>).</p>
<dt><code>SWIG_VERSION</code></p>
<dd>SWIG executable version (result of <code>swig -version</code>).</p>
<dt><code>SWIG_&lt;lang&gt;_FOUND</code></p>
<dd>If <code>COMPONENTS</code> or <code>OPTIONAL_COMPONENTS</code> are requested, each available target language <code>&lt;lang&gt;</code> (lowercase) will be set to TRUE. </p>
<p> Any <code>COMPONENTS</code> given to <code>find_package</code> should be the names of supported target languages as provided to the LANGUAGE argument of <code>swig_add_library</code>, such as <code>python</code> or <code>perl5</code>. Language names <i>must</i> be lowercase. </p>
<p> All information is collected from the <code>SWIG_EXECUTABLE</code>, so the version to be found can be changed from the command line by means of setting <code>SWIG_EXECUTABLE</code>. </p>
<p> Example usage requiring SWIG 4.0 or higher and Python language support, with optional Fortran support: </p>
<pre>find_package(SWIG 4.0 COMPONENTS python OPTIONAL_COMPONENTS fortran)
if(SWIG_FOUND)
 message(&quot;SWIG found: ${SWIG_EXECUTABLE}&quot;)
 if(NOT SWIG_fortran_FOUND)
 message(WARNING &quot;SWIG Fortran bindings cannot be generated&quot;)
 endif()
endif()</pre>
</dl>
<h3>FindTCL</h3>
<p>TK_INTERNAL_PATH was removed. </p>
<p> This module finds if Tcl is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>TCL_FOUND = Tcl was found
TK_FOUND = Tk was found
TCLTK_FOUND = Tcl and Tk were found
TCL_LIBRARY = path to Tcl library (tcl tcl80)
TCL_INCLUDE_PATH = path to where tcl.h can be found
TCL_TCLSH = path to tclsh binary (tcl tcl80)
TK_LIBRARY = path to Tk library (tk tk80 etc)
TK_INCLUDE_PATH = path to where tk.h can be found
TK_WISH = full path to the wish executable</pre>
<p>In an effort to remove some clutter and clear up some issues for people who are not necessarily Tcl/Tk gurus/developers, some variables were moved or removed. Changes compared to CMake 2.4 are: </p>
<pre>=&gt; they were only useful for people writing Tcl/Tk extensions.
=&gt; these libs are not packaged by default with Tcl/Tk distributions.
 Even when Tcl/Tk is built from source, several flavors of debug libs
 are created and there is no real reason to pick a single one
 specifically (say, amongst tcl84g, tcl84gs, or tcl84sgx).
 Let's leave that choice to the user by allowing him to assign
 TCL_LIBRARY to any Tcl library, debug or not.
=&gt; this ended up being only a Win32 variable, and there is a lot of
 confusion regarding the location of this file in an installed Tcl/Tk
 tree anyway (see 8.5 for example). If you need the internal path at
 this point it is safer you ask directly where the *source* tree is
 and dig from there.</pre>
<h3>FindTclsh</h3>
<p>Find tclsh </p>
<p> This module finds if TCL is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>TCLSH_FOUND = TRUE if tclsh has been found
TCL_TCLSH = the path to the tclsh executable</pre>
<h3>FindTclStub</h3>
<p>TCL_STUB_LIBRARY_DEBUG and TK_STUB_LIBRARY_DEBUG were removed. </p>
<p> This module finds Tcl stub libraries. It first finds Tcl include files and libraries by calling FindTCL.cmake. How to Use the Tcl Stubs Library: </p>
<pre><a rel="nofollow" href="http://tcl.activestate.com/doc/howto/stubs.html">http://tcl.activestate.com/doc/howto/stubs.html</a></pre>
<p>Using Stub Libraries: </p>
<pre><a rel="nofollow" href="http://safari.oreilly.com/0130385603/ch48lev1sec3">http://safari.oreilly.com/0130385603/ch48lev1sec3</a></pre>
<p>This code sets the following variables: </p>
<pre>TCL_STUB_LIBRARY = path to Tcl stub library
TK_STUB_LIBRARY = path to Tk stub library
TTK_STUB_LIBRARY = path to ttk stub library</pre>
<p>In an effort to remove some clutter and clear up some issues for people who are not necessarily Tcl/Tk gurus/developers, some variables were moved or removed. Changes compared to CMake 2.4 are: </p>
<pre>=&gt; these libs are not packaged by default with Tcl/Tk distributions.
 Even when Tcl/Tk is built from source, several flavors of debug libs
 are created and there is no real reason to pick a single one
 specifically (say, amongst tclstub84g, tclstub84gs, or tclstub84sgx).
 Let's leave that choice to the user by allowing him to assign
 TCL_STUB_LIBRARY to any Tcl library, debug or not.</pre>
<h3>FindThreads</h3>
<p>This module determines the thread library of the system.</p>
<h3>Imported Targets</h3>
<p>New in version 3.1. </p>
<p> This module defines the following <code>IMPORTED</code> target:</p>
<dl>
<dt><code>Threads::Threads</code></p>
<dd>The thread library, if found.</dl>
<h3>Result Variables</h3>
<p>The following variables are set:</p>
<dl>
<dt><code>Threads_FOUND</code></p>
<dd>If a supported thread library was found.</p>
<dt><code>CMAKE_THREAD_LIBS_INIT</code></p>
<dd>The thread library to use. This may be empty if the thread functions are provided by the system libraries and no special flags are needed to use them.</p>
<dt><code>CMAKE_USE_WIN32_THREADS_INIT</code></p>
<dd>If the found thread library is the win32 one.</p>
<dt><code>CMAKE_USE_PTHREADS_INIT</code></p>
<dd>If the found thread library is pthread compatible.</p>
<dt><code>CMAKE_HP_PTHREADS_INIT</code></p>
<dd>If the found thread library is the HP thread library.</dl>
<h3>Variables Affecting Behavior</h3>
<dl>
<dt><code>THREADS_PREFER_PTHREAD_FLAG</code></p>
<dd>New in version 3.1. </p>
<p> If the use of the -pthread compiler and linker flag is preferred then the caller can set this variable to TRUE. The compiler flag can only be used with the imported target. Use of both the imported target as well as this switch is highly recommended for new code. </p>
<p> This variable has no effect if the system libraries provide the thread functions, i.e. when <code>CMAKE_THREAD_LIBS_INIT</code> will be empty.</dl>
<h3>FindTIFF</h3>
<p>Find the TIFF library (<code>libtiff</code>, <i><a rel="nofollow" href="https://libtiff.gitlab.io/libtiff/">https://libtiff.gitlab.io/libtiff/</a></i>).</p>
<h3>Optional COMPONENTS</h3>
<p>This module supports the optional component <i>CXX</i>, for use with the COMPONENTS argument of the <code>find_package()</code> command. This component has an associated imported target, as described below.</p>
<h3>Imported targets</h3>
<p>New in version 3.5. </p>
<p> This module defines the following <code>IMPORTED</code> targets:</p>
<dl>
<dt><code>TIFF::TIFF</code></p>
<dd>The TIFF library, if found.</p>
<dt><code>TIFF::CXX</code></p>
<dd>New in version 3.19. </p>
<p> The C++ wrapper libtiffxx, if requested by the <i>COMPONENTS CXX</i> option, if the compiler is not MSVC (which includes the C++ wrapper in libtiff), and if found.</dl>
<h3>Result variables</h3>
<p>This module will set the following variables in your project:</p>
<dl>
<dt><code>TIFF_FOUND</code></p>
<dd>true if the TIFF headers and libraries were found</p>
<dt><code>TIFF_INCLUDE_DIR</code></p>
<dd>the directory containing the TIFF headers</p>
<dt><code>TIFF_INCLUDE_DIRS</code></p>
<dd>the directory containing the TIFF headers</p>
<dt><code>TIFF_LIBRARIES</code></p>
<dd>TIFF libraries to be linked</dl>
<h3>Cache variables</h3>
<p>The following cache variables may also be set:</p>
<dl>
<dt><code>TIFF_INCLUDE_DIR</code></p>
<dd>the directory containing the TIFF headers</p>
<dt><code>TIFF_LIBRARY_RELEASE</code></p>
<dd>the path to the TIFF library for release configurations</p>
<dt><code>TIFF_LIBRARY_DEBUG</code></p>
<dd>the path to the TIFF library for debug configurations</p>
<dt><code>TIFFXX_LIBRARY_RELEASE</code></p>
<dd>the path to the TIFFXX library for release configurations</p>
<dt><code>TIFFXX_LIBRARY_DEBUG</code></p>
<dd>the path to the TIFFXX library for debug configurations </p>
<p> New in version 3.4: Debug and Release variants are found separately. </p>
</dl>
<h3>FindUnixCommands</h3>
<p>Find Unix commands, including the ones from Cygwin </p>
<p> This module looks for the Unix commands <code>bash</code>, <code>cp</code>, <code>gzip</code>, <code>mv</code>, <code>rm</code>, and <code>tar</code> and stores the result in the variables <code>BASH</code>, <code>CP</code>, <code>GZIP</code>, <code>MV</code>, <code>RM</code>, and <code>TAR</code>.</p>
<h3>FindVTK</h3>
<p>This module no longer exists. </p>
<p> This module existed in versions of CMake prior to 3.1, but became only a thin wrapper around <code>find_package(VTK NO_MODULE)</code> to provide compatibility for projects using long-outdated conventions. Now <code>find_package(VTK)</code> will search for <code>VTKConfig.cmake</code> directly.</p>
<h3>FindVulkan</h3>
<p>New in version 3.7. </p>
<p> Find Vulkan, which is a low-overhead, cross-platform 3D graphics and computing API.</p>
<h3>IMPORTED Targets</h3>
<p>This module defines <code>IMPORTED</code> targets if Vulkan has been found:</p>
<dl>
<dt><code>Vulkan::Vulkan</code></p>
<dd>The main Vulkan library.</p>
<dt><code>Vulkan::glslc</code></p>
<dd>New in version 3.19. </p>
<p> The GLSLC SPIR-V compiler, if it has been found.</p>
<dt><code>Vulkan::Headers</code></p>
<dd>New in version 3.21. </p>
<p> Provides just Vulkan headers include paths, if found. No library is included in this target. This can be useful for applications that load Vulkan library dynamically.</p>
<dt><code>Vulkan::glslangValidator</code></p>
<dd>New in version 3.21. </p>
<p> The glslangValidator tool, if found. It is used to compile GLSL and HLSL shaders into SPIR-V.</dl>
<h3>Result Variables</h3>
<p>This module defines the following variables: </p>
<pre>Vulkan_FOUND - &quot;True&quot; if Vulkan was found
Vulkan_INCLUDE_DIRS - include directories for Vulkan
Vulkan_LIBRARIES - link against this library to use Vulkan</pre>
<p>The module will also define three cache variables: </p>
<pre>Vulkan_INCLUDE_DIR - the Vulkan include directory
Vulkan_LIBRARY - the path to the Vulkan library
Vulkan_GLSLC_EXECUTABLE - the path to the GLSL SPIR-V compiler
Vulkan_GLSLANG_VALIDATOR_EXECUTABLE - the path to the glslangValidator tool</pre>
<h3>Hints</h3>
<p>New in version 3.18. </p>
<p> The <code>VULKAN_SDK</code> environment variable optionally specifies the location of the Vulkan SDK root directory for the given architecture. It is typically set by sourcing the toplevel <code>setup-env.sh</code> script of the Vulkan SDK directory into the shell environment.</p>
<h3>FindWget</h3>
<p>Find wget </p>
<p> This module looks for wget. This module defines the following values: </p>
<pre>WGET_EXECUTABLE: the full path to the wget tool.
WGET_FOUND: True if wget has been found.</pre>
<h3>FindWish</h3>
<p>Find wish installation </p>
<p> This module finds if TCL is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>TK_WISH = the path to the wish executable</pre>
<p>if UNIX is defined, then it will look for the cygwin version first</p>
<h3>FindwxWidgets</h3>
<p>Find a wxWidgets (a.k.a., wxWindows) installation. </p>
<p> This module finds if wxWidgets is installed and selects a default configuration to use. wxWidgets is a modular library. To specify the modules that you will use, you need to name them as components to the package: </p>
<p> find_package(wxWidgets COMPONENTS core base &#8230; OPTIONAL_COMPONENTS net &#8230;) </p>
<p> New in version 3.4: Support for <code>find_package()</code> version argument; <code>webview</code> component. </p>
<p> New in version 3.14: <code>OPTIONAL_COMPONENTS</code> support. </p>
<p> There are two search branches: a windows style and a unix style. For windows, the following variables are searched for and set to defaults in case of multiple choices. Change them if the defaults are not desired (i.e., these are the only variables you should change to select a configuration): </p>
<pre>wxWidgets_ROOT_DIR - Base wxWidgets directory
 (e.g., C:/wxWidgets-2.6.3).
wxWidgets_LIB_DIR - Path to wxWidgets libraries
 (e.g., C:/wxWidgets-2.6.3/lib/vc_lib).
wxWidgets_CONFIGURATION - Configuration to use
 (e.g., msw, mswd, mswu, mswunivud, etc.)
wxWidgets_EXCLUDE_COMMON_LIBRARIES
 - Set to TRUE to exclude linking of
 commonly required libs (e.g., png tiff
 jpeg zlib regex expat).</pre>
<p>For unix style it uses the wx-config utility. You can select between debug/release, unicode/ansi, universal/non-universal, and static/shared in the QtDialog or ccmake interfaces by turning ON/OFF the following variables: </p>
<pre>wxWidgets_USE_DEBUG
wxWidgets_USE_UNICODE
wxWidgets_USE_UNIVERSAL
wxWidgets_USE_STATIC</pre>
<p>There is also a wxWidgets_CONFIG_OPTIONS variable for all other options that need to be passed to the wx-config utility. For example, to use the base toolkit found in the /usr/local path, set the variable (before calling the FIND_PACKAGE command) as such: </p>
<pre>set(wxWidgets_CONFIG_OPTIONS --toolkit=base --prefix=/usr)</pre>
<p>The following are set after the configuration is done for both windows and unix style: </p>
<pre>wxWidgets_FOUND - Set to TRUE if wxWidgets was found.
wxWidgets_INCLUDE_DIRS - Include directories for WIN32
 i.e., where to find &quot;wx/wx.h&quot; and
 &quot;wx/setup.h&quot;; possibly empty for unices.
wxWidgets_LIBRARIES - Path to the wxWidgets libraries.
wxWidgets_LIBRARY_DIRS - compile time link dirs, useful for
 rpath on UNIX. Typically an empty string
 in WIN32 environment.
wxWidgets_DEFINITIONS - Contains defines required to compile/link
 against WX, e.g. WXUSINGDLL
wxWidgets_DEFINITIONS_DEBUG- Contains defines required to compile/link
 against WX debug builds, e.g. __WXDEBUG__
wxWidgets_CXX_FLAGS - Include dirs and compiler flags for
 unices, empty on WIN32. Essentially
 &quot;`wx-config --cxxflags`&quot;.
wxWidgets_USE_FILE - Convenience include file.</pre>
<p>New in version 3.11: The following environment variables can be used as hints: <code>WX_CONFIG</code>, <code>WXRC_CMD</code>. </p>
<p> Sample usage: </p>
<pre># Note that for MinGW users the order of libs is important!
find_package(wxWidgets COMPONENTS gl core base OPTIONAL_COMPONENTS net)
if(wxWidgets_FOUND)
 include(${wxWidgets_USE_FILE})
 # and for each of your dependent executable/library targets:
 target_link_libraries(&lt;YourTarget&gt; ${wxWidgets_LIBRARIES})
endif()</pre>
<p>If wxWidgets is required (i.e., not an optional part): </p>
<pre>find_package(wxWidgets REQUIRED gl core base OPTIONAL_COMPONENTS net)
include(${wxWidgets_USE_FILE})
# and for each of your dependent executable/library targets:
target_link_libraries(&lt;YourTarget&gt; ${wxWidgets_LIBRARIES})</pre>
<h3>FindX11</h3>
<p>Find X11 installation </p>
<p> Try to find X11 on UNIX systems. The following values are defined </p>
<pre>X11_FOUND - True if X11 is available
X11_INCLUDE_DIR - include directories to use X11
X11_LIBRARIES - link against these to use X11</pre>
<p>and also the following more fine grained variables and targets: </p>
<p> New in version 3.14: Imported targets. </p>
<pre>X11_ICE_INCLUDE_PATH, X11_ICE_LIB, X11_ICE_FOUND, X11::ICE
X11_SM_INCLUDE_PATH, X11_SM_LIB, X11_SM_FOUND, X11::SM
X11_X11_INCLUDE_PATH, X11_X11_LIB, X11::X11
X11_Xaccessrules_INCLUDE_PATH,
X11_Xaccessstr_INCLUDE_PATH, X11_Xaccess_FOUND
X11_Xau_INCLUDE_PATH, X11_Xau_LIB, X11_Xau_FOUND, X11::Xau
X11_xcb_INCLUDE_PATH, X11_xcb_LIB, X11_xcb_FOUND, X11::xcb
X11_X11_xcb_INCLUDE_PATH, X11_X11_xcb_LIB, X11_X11_xcb_FOUND, X11::X11_xcb
X11_xcb_icccm_INCLUDE_PATH, X11_xcb_icccm_LIB, X11_xcb_icccm_FOUND, X11::xcb_icccm
X11_xcb_util_INCLUDE_PATH, X11_xcb_util_LIB, X11_xcb_util_FOUND, X11::xcb_util
X11_xcb_xfixes_INCLUDE_PATH, X11_xcb_xfixes_LIB, X11_xcb_xfixes_FOUND, X11::xcb_xfixes
X11_xcb_xkb_INCLUDE_PATH, X11_xcb_xkb_LIB, X11_xcb_xkb_FOUND, X11::xcb_xkb
X11_Xcomposite_INCLUDE_PATH, X11_Xcomposite_LIB, X11_Xcomposite_FOUND, X11::Xcomposite
X11_Xcursor_INCLUDE_PATH, X11_Xcursor_LIB, X11_Xcursor_FOUND, X11::Xcursor
X11_Xdamage_INCLUDE_PATH, X11_Xdamage_LIB, X11_Xdamage_FOUND, X11::Xdamage
X11_Xdmcp_INCLUDE_PATH, X11_Xdmcp_LIB, X11_Xdmcp_FOUND, X11::Xdmcp
X11_Xext_INCLUDE_PATH, X11_Xext_LIB, X11_Xext_FOUND, X11::Xext
X11_Xxf86misc_INCLUDE_PATH, X11_Xxf86misc_LIB, X11_Xxf86misc_FOUND, X11::Xxf86misc
X11_Xxf86vm_INCLUDE_PATH, X11_Xxf86vm_LIB X11_Xxf86vm_FOUND, X11::Xxf86vm
X11_Xfixes_INCLUDE_PATH, X11_Xfixes_LIB, X11_Xfixes_FOUND, X11::Xfixes
X11_Xft_INCLUDE_PATH, X11_Xft_LIB, X11_Xft_FOUND, X11::Xft
X11_Xi_INCLUDE_PATH, X11_Xi_LIB, X11_Xi_FOUND, X11::Xi
X11_Xinerama_INCLUDE_PATH, X11_Xinerama_LIB, X11_Xinerama_FOUND, X11::Xinerama
X11_Xkb_INCLUDE_PATH,
X11_Xkblib_INCLUDE_PATH, X11_Xkb_FOUND, X11::Xkb
X11_xkbcommon_INCLUDE_PATH, X11_xkbcommon_LIB, X11_xkbcommon_FOUND, X11::xkbcommon
X11_xkbcommon_X11_INCLUDE_PATH,X11_xkbcommon_X11_LIB,X11_xkbcommon_X11_FOUND,X11::xkbcommon_X11
X11_xkbfile_INCLUDE_PATH, X11_xkbfile_LIB, X11_xkbfile_FOUND, X11::xkbfile
X11_Xmu_INCLUDE_PATH, X11_Xmu_LIB, X11_Xmu_FOUND, X11::Xmu
X11_Xpm_INCLUDE_PATH, X11_Xpm_LIB, X11_Xpm_FOUND, X11::Xpm
X11_Xtst_INCLUDE_PATH, X11_Xtst_LIB, X11_Xtst_FOUND, X11::Xtst
X11_Xrandr_INCLUDE_PATH, X11_Xrandr_LIB, X11_Xrandr_FOUND, X11::Xrandr
X11_Xrender_INCLUDE_PATH, X11_Xrender_LIB, X11_Xrender_FOUND, X11::Xrender
X11_XRes_INCLUDE_PATH, X11_XRes_LIB, X11_XRes_FOUND, X11::XRes
X11_Xss_INCLUDE_PATH, X11_Xss_LIB, X11_Xss_FOUND, X11::Xss
X11_Xt_INCLUDE_PATH, X11_Xt_LIB, X11_Xt_FOUND, X11::Xt
X11_Xutil_INCLUDE_PATH, X11_Xutil_FOUND, X11::Xutil
X11_Xv_INCLUDE_PATH, X11_Xv_LIB, X11_Xv_FOUND, X11::Xv
X11_dpms_INCLUDE_PATH, (in X11_Xext_LIB), X11_dpms_FOUND
X11_XShm_INCLUDE_PATH, (in X11_Xext_LIB), X11_XShm_FOUND
X11_Xshape_INCLUDE_PATH, (in X11_Xext_LIB), X11_Xshape_FOUND
X11_XSync_INCLUDE_PATH, (in X11_Xext_LIB), X11_XSync_FOUND
X11_Xaw_INCLUDE_PATH, X11_Xaw_LIB X11_Xaw_FOUND X11::Xaw</pre>
<p>New in version 3.14: Renamed <code>Xxf86misc</code>, <code>X11_Xxf86misc</code>, <code>X11_Xxf86vm</code>, <code>X11_xkbfile</code>, <code>X11_Xtst</code>, and <code>X11_Xss</code> libraries to match their file names. Deprecated the <code>X11_Xinput</code> library. Old names are still available for compatibility. </p>
<p> New in version 3.14: Added the <code>X11_Xext_INCLUDE_PATH</code> variable. </p>
<p> New in version 3.18: Added the <code>xcb</code>, <code>X11-xcb</code>, <code>xcb-icccm</code>, <code>xcb-xkb</code>, <code>xkbcommon</code>, and <code>xkbcommon-X11</code> libraries. </p>
<p> New in version 3.19: Added the <code>Xaw</code>, <code>xcb_util</code>, and <code>xcb_xfixes</code> libraries.</p>
<h3>FindXalanC</h3>
<p>New in version 3.5. </p>
<p> Find the Apache Xalan-C++ XSL transform processor headers and libraries.</p>
<h3>Imported targets</h3>
<p>This module defines the following <code>IMPORTED</code> targets:</p>
<dl>
<dt><code>XalanC::XalanC</code></p>
<dd>The Xalan-C++ <code>xalan-c</code> library, if found.</dl>
<h3>Result variables</h3>
<p>This module will set the following variables in your project:</p>
<dl>
<dt><code>XalanC_FOUND</code></p>
<dd>true if the Xalan headers and libraries were found</p>
<dt><code>XalanC_VERSION</code></p>
<dd>Xalan release version</p>
<dt><code>XalanC_INCLUDE_DIRS</code></p>
<dd>the directory containing the Xalan headers; note <code>XercesC_INCLUDE_DIRS</code> is also required</p>
<dt><code>XalanC_LIBRARIES</code></p>
<dd>Xalan libraries to be linked; note <code>XercesC_LIBRARIES</code> is also required</dl>
<h3>Cache variables</h3>
<p>The following cache variables may also be set:</p>
<dl>
<dt><code>XalanC_INCLUDE_DIR</code></p>
<dd>the directory containing the Xalan headers</p>
<dt><code>XalanC_LIBRARY</code></p>
<dd>the Xalan library</dl>
<h3>FindXCTest</h3>
<p>New in version 3.3. </p>
<p> Functions to help creating and executing XCTest bundles. </p>
<p> An XCTest bundle is a CFBundle with a special product-type and bundle extension. The Mac Developer Library provides more information in the <i>Testing with Xcode</i> document.</p>
<h3>Module Functions</h3>
<dl>
<dt><code>xctest_add_bundle</code></p>
<dd>The <code>xctest_add_bundle</code> function creates a XCTest bundle named &lt;target&gt; which will test the target &lt;testee&gt;. Supported target types for testee are Frameworks and App Bundles: </p>
<pre>xctest_add_bundle(
 &lt;target&gt; # Name of the XCTest bundle
 &lt;testee&gt; # Target name of the testee
 )</pre>
<dt><code>xctest_add_test</code></p>
<dd>The <code>xctest_add_test</code> function adds an XCTest bundle to the project to be run by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>. The test will be named &lt;name&gt; and tests &lt;bundle&gt;: </p>
<pre>xctest_add_test(
 &lt;name&gt; # Test name
 &lt;bundle&gt; # Target name of XCTest bundle
 )</pre>
</dl>
<h3>Module Variables</h3>
<p>The following variables are set by including this module:</p>
<dl>
<dt><code>XCTest_FOUND</code></p>
<dd>True if the XCTest Framework and executable were found.</p>
<dt><code>XCTest_EXECUTABLE</code></p>
<dd>The path to the xctest command line tool used to execute XCTest bundles.</p>
<dt><code>XCTest_INCLUDE_DIRS</code></p>
<dd>The directory containing the XCTest Framework headers.</p>
<dt><code>XCTest_LIBRARIES</code></p>
<dd>The location of the XCTest Framework.</dl>
<h3>FindXercesC</h3>
<p>New in version 3.1. </p>
<p> Find the Apache Xerces-C++ validating XML parser headers and libraries.</p>
<h3>Imported targets</h3>
<p>New in version 3.5. </p>
<p> This module defines the following <code>IMPORTED</code> targets:</p>
<dl>
<dt><code>XercesC::XercesC</code></p>
<dd>The Xerces-C++ <code>xerces-c</code> library, if found.</dl>
<h3>Result variables</h3>
<p>This module will set the following variables in your project:</p>
<dl>
<dt><code>XercesC_FOUND</code></p>
<dd>true if the Xerces headers and libraries were found</p>
<dt><code>XercesC_VERSION</code></p>
<dd>Xerces release version</p>
<dt><code>XercesC_INCLUDE_DIRS</code></p>
<dd>the directory containing the Xerces headers</p>
<dt><code>XercesC_LIBRARIES</code></p>
<dd>Xerces libraries to be linked</dl>
<h3>Cache variables</h3>
<p>The following cache variables may also be set:</p>
<dl>
<dt><code>XercesC_INCLUDE_DIR</code></p>
<dd>the directory containing the Xerces headers</p>
<dt><code>XercesC_LIBRARY</code></p>
<dd>the Xerces library </p>
<p> New in version 3.4: Debug and Release variants are found separately. </p>
</dl>
<h3>FindXMLRPC</h3>
<p>Find xmlrpc </p>
<p> Find the native XMLRPC headers and libraries. </p>
<pre>XMLRPC_INCLUDE_DIRS - where to find xmlrpc.h, etc.
XMLRPC_LIBRARIES - List of libraries when using xmlrpc.
XMLRPC_FOUND - True if xmlrpc found.</pre>
<p>XMLRPC modules may be specified as components for this find module. Modules may be listed by running &quot;xmlrpc-c-config&quot;. Modules include: </p>
<pre>c++ C++ wrapper code
libwww-client libwww-based client
cgi-server CGI-based server
abyss-server ABYSS-based server</pre>
<p>Typical usage: </p>
<pre>find_package(XMLRPC REQUIRED libwww-client)</pre>
<h3>FindZLIB</h3>
<p>Find the native ZLIB includes and library.</p>
<h3>IMPORTED Targets</h3>
<p>New in version 3.1. </p>
<p> This module defines <code>IMPORTED</code> target <code>ZLIB::ZLIB</code>, if ZLIB has been found.</p>
<h3>Result Variables</h3>
<p>This module defines the following variables: </p>
<pre>ZLIB_INCLUDE_DIRS - where to find zlib.h, etc.
ZLIB_LIBRARIES - List of libraries when using zlib.
ZLIB_FOUND - True if zlib found.</pre>
<pre>ZLIB_VERSION_STRING - The version of zlib found (x.y.z)
ZLIB_VERSION_MAJOR - The major version of zlib
ZLIB_VERSION_MINOR - The minor version of zlib
ZLIB_VERSION_PATCH - The patch version of zlib
ZLIB_VERSION_TWEAK - The tweak version of zlib</pre>
<p>New in version 3.4: Debug and Release variants are found separately.</p>
<h3>Backward Compatibility</h3>
<p>The following variable are provided for backward compatibility </p>
<pre>ZLIB_MAJOR_VERSION - The major version of zlib
ZLIB_MINOR_VERSION - The minor version of zlib
ZLIB_PATCH_VERSION - The patch version of zlib</pre>
<h3>Hints</h3>
<p>A user may set <code>ZLIB_ROOT</code> to a zlib installation root to tell this module where to look.</p>
<h2>Deprecated Modules</h2>
<h3>Deprecated Utility Modules</h3>
<h3>AddFileDependencies</h3>
<p>Deprecated since version 3.20. </p>
<p> Add dependencies to a source file. </p>
<pre>add_file_dependencies(&lt;source&gt; &lt;files&gt;...)</pre>
<p>Adds the given <code>&lt;files&gt;</code> to the dependencies of file <code>&lt;source&gt;</code>. </p>
<p> Do not use this command in new code. It is just a wrapper around: </p>
<pre>set_property(SOURCE &lt;source&gt; APPEND PROPERTY OBJECT_DEPENDS &lt;files&gt;...)</pre>
<p>Instead use the <code>set_property()</code> command to append to the <code>OBJECT_DEPENDS</code> source file property directly.</p>
<h3>CMakeDetermineVSServicePack</h3>
<p>Deprecated since version 3.0: Do not use. </p>
<p> The functionality of this module has been superseded by the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> variable that contains the compiler version number. </p>
<p> Determine the Visual Studio service pack of the &#8216;cl&#8217; in use. </p>
<p> Usage: </p>
<pre>if(MSVC)
 include(CMakeDetermineVSServicePack)
 DetermineVSServicePack( my_service_pack )
 if( my_service_pack )
 message(STATUS &quot;Detected: ${my_service_pack}&quot;)
 endif()
endif()</pre>
<p>Function DetermineVSServicePack sets the given variable to one of the following values or an empty string if unknown: </p>
<pre>vc80, vc80sp1
vc90, vc90sp1
vc100, vc100sp1
vc110, vc110sp1, vc110sp2, vc110sp3, vc110sp4</pre>
<h3>CMakeExpandImportedTargets</h3>
<p>Deprecated since version 3.4: Do not use. </p>
<p> This module was once needed to expand imported targets to the underlying libraries they reference on disk for use with the <code>try_compile()</code> and <code>try_run()</code> commands. These commands now support imported libraries in their <code>LINK_LIBRARIES</code> options (since CMake 2.8.11 for <code>try_compile()</code> and since CMake 3.2 for <code>try_run()</code>). </p>
<p> This module does not support the policy <code>CMP0022</code> <code>NEW</code> behavior or use of the <code>INTERFACE_LINK_LIBRARIES</code> property because <code>generator expressions</code> cannot be evaluated during configuration. </p>
<pre>CMAKE_EXPAND_IMPORTED_TARGETS(&lt;var&gt; LIBRARIES lib1 lib2...libN
 [CONFIGURATION &lt;config&gt;])</pre>
<p>CMAKE_EXPAND_IMPORTED_TARGETS() takes a list of libraries and replaces all imported targets contained in this list with their actual file paths of the referenced libraries on disk, including the libraries from their link interfaces. If a CONFIGURATION is given, it uses the respective configuration of the imported targets if it exists. If no CONFIGURATION is given, it uses the first configuration from ${CMAKE_CONFIGURATION_TYPES} if set, otherwise ${CMAKE_BUILD_TYPE}. </p>
<pre>cmake_expand_imported_targets(expandedLibs
 LIBRARIES ${CMAKE_REQUIRED_LIBRARIES}
 CONFIGURATION &quot;${CMAKE_TRY_COMPILE_CONFIGURATION}&quot; )</pre>
<h3>CMakeForceCompiler</h3>
<p>Deprecated since version 3.6: Do not use. </p>
<p> The macros provided by this module were once intended for use by cross-compiling toolchain files when CMake was not able to automatically detect the compiler identification. Since the introduction of this module, CMake&#8217;s compiler identification capabilities have improved and can now be taught to recognize any compiler. Furthermore, the suite of information CMake detects from a compiler is now too extensive to be provided by toolchain files using these macros. </p>
<p> One common use case for this module was to skip CMake&#8217;s checks for a working compiler when using a cross-compiler that cannot link binaries without special flags or custom linker scripts. This case is now supported by setting the <code>CMAKE_TRY_COMPILE_TARGET_TYPE</code> variable in the toolchain file instead. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<p> Macro <code>CMAKE_FORCE_C_COMPILER</code> has the following signature: </p>
<pre>CMAKE_FORCE_C_COMPILER(&lt;compiler&gt; &lt;compiler-id&gt;)</pre>
<p>It sets <code>CMAKE_C_COMPILER</code> to the given compiler and the cmake internal variable <code>CMAKE_C_COMPILER_ID</code> to the given compiler-id. It also bypasses the check for working compiler and basic compiler information tests. </p>
<p> Macro <code>CMAKE_FORCE_CXX_COMPILER</code> has the following signature: </p>
<pre>CMAKE_FORCE_CXX_COMPILER(&lt;compiler&gt; &lt;compiler-id&gt;)</pre>
<p>It sets <code>CMAKE_CXX_COMPILER</code> to the given compiler and the cmake internal variable <code>CMAKE_CXX_COMPILER_ID</code> to the given compiler-id. It also bypasses the check for working compiler and basic compiler information tests. </p>
<p> Macro <code>CMAKE_FORCE_Fortran_COMPILER</code> has the following signature: </p>
<pre>CMAKE_FORCE_Fortran_COMPILER(&lt;compiler&gt; &lt;compiler-id&gt;)</pre>
<p>It sets <code>CMAKE_Fortran_COMPILER</code> to the given compiler and the cmake internal variable <code>CMAKE_Fortran_COMPILER_ID</code> to the given compiler-id. It also bypasses the check for working compiler and basic compiler information tests. </p>
<p> So a simple toolchain file could look like this: </p>
<pre>include (CMakeForceCompiler)
set(CMAKE_SYSTEM_NAME Generic)
CMAKE_FORCE_C_COMPILER (chc12 MetrowerksHicross)
CMAKE_FORCE_CXX_COMPILER (chc12 MetrowerksHicross)</pre>
<h3>CMakeParseArguments</h3>
<p>This module once implemented the <code>cmake_parse_arguments()</code> command that is now implemented natively by CMake. It is now an empty placeholder for compatibility with projects that include it to get the command from CMake 3.4 and lower.</p>
<h3>Documentation</h3>
<p>Deprecated since version 3.18: This module does nothing, unless policy <code>CMP0106</code> is set to <code>OLD</code>. </p>
<p> This module provides support for the VTK documentation framework. It relies on several tools (Doxygen, Perl, etc).</p>
<h3>MacroAddFileDependencies</h3>
<p>Deprecated since version 3.14. </p>
<pre>MACRO_ADD_FILE_DEPENDENCIES(&lt;source&gt; &lt;files&gt;...)</pre>
<p>Do not use this command in new code. It is just a wrapper around: </p>
<pre>set_property(SOURCE &lt;source&gt; APPEND PROPERTY OBJECT_DEPENDS &lt;files&gt;...)</pre>
<p>Instead use the <code>set_property()</code> command to append to the <code>OBJECT_DEPENDS</code> source file property directly.</p>
<h3>TestCXXAcceptsFlag</h3>
<p>Deprecated since version 3.0: See <code>CheckCXXCompilerFlag</code>. </p>
<p> Check if the CXX compiler accepts a flag. </p>
<pre>CHECK_CXX_ACCEPTS_FLAG(&lt;flags&gt; &lt;variable&gt;)</pre>
<dl>
<dt><code>&lt;flags&gt;</code></p>
<dd>the flags to try</p>
<dt><code>&lt;variable&gt;</code></p>
<dd>variable to store the result</dl>
<h3>UseJavaClassFilelist</h3>
<p>Changed in version 3.20: This module was previously documented by mistake and was never meant for direct inclusion by project code. See the <code>UseJava</code> module.</p>
<h3>UseJavaSymlinks</h3>
<p>Changed in version 3.20: This module was previously documented by mistake and was never meant for direct inclusion by project code. See the <code>UseJava</code> module.</p>
<h3>UsePkgConfig</h3>
<p>Obsolete pkg-config module for CMake, use FindPkgConfig instead. </p>
<p> This module defines the following macro: </p>
<p> PKGCONFIG(package includedir libdir linkflags cflags) </p>
<p> Calling PKGCONFIG will fill the desired information into the 4 given arguments, e.g. PKGCONFIG(libart-2.0 LIBART_INCLUDE_DIR LIBART_LINK_DIR LIBART_LINK_FLAGS LIBART_CFLAGS) if pkg-config was NOT found or the specified software package doesn&#8217;t exist, the variable will be empty when the function returns, otherwise they will contain the respective information</p>
<h3>Use_wxWindows</h3>
<p>Deprecated since version 2.8.10: Use <code>find_package(wxWidgets)</code> and <code>include(${wxWidgets_USE_FILE})</code> instead. </p>
<p> This convenience include finds if wxWindows is installed and set the appropriate libs, incdirs, flags etc. author Jan Woetzel &lt;jw -at- mip.informatik.uni-kiel.de&gt; (07/2003) </p>
<p> USAGE: </p>
<pre>just include Use_wxWindows.cmake
in your projects CMakeLists.txt</pre>
<p>include( ${CMAKE_MODULE_PATH}/Use_wxWindows.cmake) </p>
<pre>if you are sure you need GL then</pre>
<p>set(WXWINDOWS_USE_GL 1) </p>
<pre>*before* you include this file.</pre>
<h3>WriteBasicConfigVersionFile</h3>
<p>Deprecated since version 3.0: Use the identical command <code>write_basic_package_version_file()</code> from module <code>CMakePackageConfigHelpers</code>. </p>
<pre>WRITE_BASIC_CONFIG_VERSION_FILE( filename
 [VERSION major.minor.patch]
 COMPATIBILITY (AnyNewerVersion|SameMajorVersion|SameMinorVersion|ExactVersion)
 [ARCH_INDEPENDENT]
 )</pre>
<h3>WriteCompilerDetectionHeader</h3>
<p>Deprecated since version 3.20: This module is available only if policy <code>CMP0120</code> is not set to <code>NEW</code>. Do not use it in new code. </p>
<p> New in version 3.1. </p>
<p> This module provides the function <code>write_compiler_detection_header()</code>. </p>
<p> This function can be used to generate a file suitable for preprocessor inclusion which contains macros to be used in source code: </p>
<pre>write_compiler_detection_header(
 FILE &lt;file&gt;
 PREFIX &lt;prefix&gt;
 [OUTPUT_FILES_VAR &lt;output_files_var&gt; OUTPUT_DIR &lt;output_dir&gt;]
 COMPILERS &lt;compiler&gt; [...]
 FEATURES &lt;feature&gt; [...]
 [BARE_FEATURES &lt;feature&gt; [...]]
 [VERSION &lt;version&gt;]
 [PROLOG &lt;prolog&gt;]
 [EPILOG &lt;epilog&gt;]
 [ALLOW_UNKNOWN_COMPILERS]
 [ALLOW_UNKNOWN_COMPILER_VERSIONS]
)</pre>
<p>This generates the file <code>&lt;file&gt;</code> with macros which all have the prefix <code>&lt;prefix&gt;</code>. </p>
<p> By default, all content is written directly to the <code>&lt;file&gt;</code>. The <code>OUTPUT_FILES_VAR</code> may be specified to cause the compiler-specific content to be written to separate files. The separate files are then available in the <code>&lt;output_files_var&gt;</code> and may be consumed by the caller for installation for example. The <code>OUTPUT_DIR</code> specifies a relative path from the main <code>&lt;file&gt;</code> to the compiler-specific files. For example: </p>
<pre>write_compiler_detection_header(
 FILE climbingstats_compiler_detection.h
 PREFIX ClimbingStats
 OUTPUT_FILES_VAR support_files
 OUTPUT_DIR compilers
 COMPILERS GNU Clang MSVC Intel
 FEATURES cxx_variadic_templates
)
install(FILES
 ${CMAKE_CURRENT_BINARY_DIR}/climbingstats_compiler_detection.h
 DESTINATION include
)
install(FILES
 ${support_files}
 DESTINATION include/compilers
)</pre>
<p><code>VERSION</code> may be used to specify the API version to be generated. Future versions of CMake may introduce alternative APIs. A given API is selected by any <code>&lt;version&gt;</code> value greater than or equal to the version of CMake that introduced the given API and less than the version of CMake that introduced its succeeding API. The value of the <code>CMAKE_MINIMUM_REQUIRED_VERSION</code> variable is used if no explicit version is specified. (As of CMake version 3.22.1 there is only one API version.) </p>
<p> <code>PROLOG</code> may be specified as text content to write at the start of the header. <code>EPILOG</code> may be specified as text content to write at the end of the header </p>
<p> At least one <code>&lt;compiler&gt;</code> and one <code>&lt;feature&gt;</code> must be listed. Compilers which are known to CMake, but not specified are detected and a preprocessor <code>#error</code> is generated for them. A preprocessor macro matching <code>&lt;PREFIX&gt;_COMPILER_IS_&lt;compiler&gt;</code> is generated for each compiler known to CMake to contain the value <code>0</code> or <code>1</code>. </p>
<p> Possible compiler identifiers are documented with the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable. Available features in this version of CMake are listed in the <code>CMAKE_C_KNOWN_FEATURES</code> and <code>CMAKE_CXX_KNOWN_FEATURES</code> global properties. See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features. </p>
<p> New in version 3.2: Added <code>MSVC</code> and <code>AppleClang</code> compiler support. </p>
<p> New in version 3.6: Added <code>Intel</code> compiler support. </p>
<p> Changed in version 3.8: The <code>{c,cxx}_std_*</code> meta-features are ignored if requested. </p>
<p> New in version 3.8: <code>ALLOW_UNKNOWN_COMPILERS</code> and <code>ALLOW_UNKNOWN_COMPILER_VERSIONS</code> cause the module to generate conditions that treat unknown compilers as simply lacking all features. Without these options the default behavior is to generate a <code>#error</code> for unknown compilers and versions. </p>
<p> New in version 3.12: <code>BARE_FEATURES</code> will define the compatibility macros with the name used in newer versions of the language standard, so the code can use the new feature name unconditionally.</p>
<h3>Feature Test Macros</h3>
<p>For each compiler, a preprocessor macro is generated matching <code>&lt;PREFIX&gt;_COMPILER_IS_&lt;compiler&gt;</code> which has the content either <code>0</code> or <code>1</code>, depending on the compiler in use. Preprocessor macros for compiler version components are generated matching <code>&lt;PREFIX&gt;_COMPILER_VERSION_MAJOR</code> <code>&lt;PREFIX&gt;_COMPILER_VERSION_MINOR</code> and <code>&lt;PREFIX&gt;_COMPILER_VERSION_PATCH</code> containing decimal values for the corresponding compiler version components, if defined. </p>
<p> A preprocessor test is generated based on the compiler version denoting whether each feature is enabled. A preprocessor macro matching <code>&lt;PREFIX&gt;_COMPILER_&lt;FEATURE&gt;</code>, where <code>&lt;FEATURE&gt;</code> is the upper-case <code>&lt;feature&gt;</code> name, is generated to contain the value <code>0</code> or <code>1</code> depending on whether the compiler in use supports the feature: </p>
<pre>write_compiler_detection_header(
 FILE climbingstats_compiler_detection.h
 PREFIX ClimbingStats
 COMPILERS GNU Clang AppleClang MSVC Intel
 FEATURES cxx_variadic_templates
)</pre>
<pre>#if ClimbingStats_COMPILER_CXX_VARIADIC_TEMPLATES
template&lt;typename... T&gt;
void someInterface(T t...) { /* ... */ }
#else
// Compatibility versions
template&lt;typename T1&gt;
void someInterface(T1 t1) { /* ... */ }
template&lt;typename T1, typename T2&gt;
void someInterface(T1 t1, T2 t2) { /* ... */ }
template&lt;typename T1, typename T2, typename T3&gt;
void someInterface(T1 t1, T2 t2, T3 t3) { /* ... */ }
#endif</pre>
<h3>Symbol Macros</h3>
<p>Some additional symbol-defines are created for particular features for use as symbols which may be conditionally defined empty: </p>
<pre>class MyClass ClimbingStats_FINAL
{
 ClimbingStats_CONSTEXPR int someInterface() { return 42; }
};</pre>
<p>The <code>ClimbingStats_FINAL</code> macro will expand to <code>final</code> if the compiler (and its flags) support the <code>cxx_final</code> feature, and the <code>ClimbingStats_CONSTEXPR</code> macro will expand to <code>constexpr</code> if <code>cxx_constexpr</code> is supported. </p>
<p> If <code>BARE_FEATURES cxx_final</code> was given as argument the <code>final</code> keyword will be defined for old compilers, too. </p>
<p> The following features generate corresponding symbol defines and if they are available as <code>BARE_FEATURES</code>: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Feature </td>
<td> Define </td>
<td> Symbol </td>
<td> bare
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>c_restrict</code> </td>
<td> <code>&lt;PREFIX&gt;_RESTRICT</code> </td>
<td> <code>restrict</code> </td>
<td> yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_constexpr</code> </td>
<td> <code>&lt;PREFIX&gt;_CONSTEXPR</code> </td>
<td> <code>constexpr</code> </td>
<td> yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_deleted_functions</code> </td>
<td> <code>&lt;PREFIX&gt;_DELETED_FUNCTION</code> </td>
<td> <code>= delete</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_extern_templates</code> </td>
<td> <code>&lt;PREFIX&gt;_EXTERN_TEMPLATE</code> </td>
<td> <code>extern</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_final</code> </td>
<td> <code>&lt;PREFIX&gt;_FINAL</code> </td>
<td> <code>final</code> </td>
<td> yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_noexcept</code> </td>
<td> <code>&lt;PREFIX&gt;_NOEXCEPT</code> </td>
<td> <code>noexcept</code> </td>
<td> yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_noexcept</code> </td>
<td> <code>&lt;PREFIX&gt;_NOEXCEPT_EXPR(X)</code> </td>
<td> <code>noexcept(X)</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_override</code> </td>
<td> <code>&lt;PREFIX&gt;_OVERRIDE</code> </td>
<td> <code>override</code> </td>
<td> yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
</table>
<p></center></p>
<h3>Compatibility Implementation Macros</h3>
<p>Some features are suitable for wrapping in a macro with a backward compatibility implementation if the compiler does not support the feature. </p>
<p> When the <code>cxx_static_assert</code> feature is not provided by the compiler, a compatibility implementation is available via the <code>&lt;PREFIX&gt;_STATIC_ASSERT(COND)</code> and <code>&lt;PREFIX&gt;_STATIC_ASSERT_MSG(COND, MSG)</code> function-like macros. The macros expand to <code>static_assert</code> where that compiler feature is available, and to a compatibility implementation otherwise. In the first form, the condition is stringified in the message field of <code>static_assert</code>. In the second form, the message <code>MSG</code> is passed to the message field of <code>static_assert</code>, or ignored if using the backward compatibility implementation. </p>
<p> The <code>cxx_attribute_deprecated</code> feature provides a macro definition <code>&lt;PREFIX&gt;_DEPRECATED</code>, which expands to either the standard <code>[[deprecated]]</code> attribute or a compiler-specific decorator such as <code>__attribute__((__deprecated__))</code> used by GNU compilers. </p>
<p> The <code>cxx_alignas</code> feature provides a macro definition <code>&lt;PREFIX&gt;_ALIGNAS</code> which expands to either the standard <code>alignas</code> decorator or a compiler-specific decorator such as <code>__attribute__ ((__aligned__))</code> used by GNU compilers. </p>
<p> The <code>cxx_alignof</code> feature provides a macro definition <code>&lt;PREFIX&gt;_ALIGNOF</code> which expands to either the standard <code>alignof</code> decorator or a compiler-specific decorator such as <code>__alignof__</code> used by GNU compilers. <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Feature </td>
<td> Define </td>
<td> Symbol </td>
<td> bare
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_alignas</code> </td>
<td> <code>&lt;PREFIX&gt;_ALIGNAS</code> </td>
<td> <code>alignas</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_alignof</code> </td>
<td> <code>&lt;PREFIX&gt;_ALIGNOF</code> </td>
<td> <code>alignof</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_nullptr</code> </td>
<td> <code>&lt;PREFIX&gt;_NULLPTR</code> </td>
<td> <code>nullptr</code> </td>
<td> yes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_static_assert</code> </td>
<td> <code>&lt;PREFIX&gt;_STATIC_ASSERT</code> </td>
<td> <code>static_assert</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_static_assert</code> </td>
<td> <code>&lt;PREFIX&gt;_STATIC_ASSERT_MSG</code> </td>
<td> <code>static_assert</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_attribute_deprecated</code> </td>
<td> <code>&lt;PREFIX&gt;_DEPRECATED</code> </td>
<td> <code>[[deprecated]]</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_attribute_deprecated</code> </td>
<td> <code>&lt;PREFIX&gt;_DEPRECATED_MSG</code> </td>
<td> <code>[[deprecated]]</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_thread_local</code> </td>
<td> <code>&lt;PREFIX&gt;_THREAD_LOCAL</code> </td>
<td> <code>thread_local</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> A use-case which arises with such deprecation macros is the deprecation of an entire library. In that case, all public API in the library may be decorated with the <code>&lt;PREFIX&gt;_DEPRECATED</code> macro. This results in very noisy build output when building the library itself, so the macro may be may be defined to empty in that case when building the deprecated library: </p>
<pre>add_library(compat_support ${srcs})
target_compile_definitions(compat_support
 PRIVATE
 CompatSupport_DEPRECATED=
)</pre>
<h3>Example Usage</h3>
<p><code>NOTE:</code> This section was migrated from the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual since it relies on the <code>WriteCompilerDetectionHeader</code> module which is removed by policy <code>CMP0120</code>. </p>
<p> Compile features may be preferred if available, without creating a hard requirement. For example, a library may provide alternative implementations depending on whether the <code>cxx_variadic_templates</code> feature is available: </p>
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
<p>Such an interface depends on using the correct preprocessor defines for the compiler features. CMake can generate a header file containing such defines using the <i>WriteCompilerDetectionHeader</i> module. The module contains the <code>write_compiler_detection_header</code> function which accepts parameters to control the content of the generated header file: </p>
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
<p> In this use-case, the project code may wish to enable a particular language standard if available from the compiler. The <code>CXX_STANDARD</code> target property may be set to the desired language standard for a particular target, and the <code>CMAKE_CXX_STANDARD</code> variable may be set to influence all following targets: </p>
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
<h3>Deprecated Find Modules</h3>
<h3>FindCUDA</h3>
<p><code>WARNING:</code> <i>Deprecated since version 3.10.</i> </p>
<p> It is no longer necessary to use this module or call <code>find_package(CUDA)</code> for compiling CUDA code. Instead, list <code>CUDA</code> among the languages named in the top-level call to the <code>project()</code> command, or call the <code>enable_language()</code> command with <code>CUDA</code>. Then one can add CUDA (<code>.cu</code>) sources directly to targets similar to other languages. </p>
<p> New in version 3.17: To find and use the CUDA toolkit libraries manually, use the <code>FindCUDAToolkit</code> module instead. It works regardless of the <code>CUDA</code> language being enabled.</p>
<h3>Documentation of Deprecated Usage</h3>
<p>Tools for building CUDA C files: libraries and build dependencies. </p>
<p> This script locates the NVIDIA CUDA C tools. It should work on Linux, Windows, and macOS and should be reasonably up to date with CUDA C releases. </p>
<p> New in version 3.19: QNX support. </p>
<p> This script makes use of the standard <code>find_package()</code> arguments of <code>&lt;VERSION&gt;</code>, <code>REQUIRED</code> and <code>QUIET</code>. <code>CUDA_FOUND</code> will report if an acceptable version of CUDA was found. </p>
<p> The script will prompt the user to specify <code>CUDA_TOOLKIT_ROOT_DIR</code> if the prefix cannot be determined by the location of nvcc in the system path and <code>REQUIRED</code> is specified to <code>find_package()</code>. To use a different installed version of the toolkit set the environment variable <code>CUDA_BIN_PATH</code> before running cmake (e.g. <code>CUDA_BIN_PATH=/usr/local/cuda1.0</code> instead of the default <code>/usr/local/cuda</code>) or set <code>CUDA_TOOLKIT_ROOT_DIR</code> after configuring. If you change the value of <code>CUDA_TOOLKIT_ROOT_DIR</code>, various components that depend on the path will be relocated. </p>
<p> It might be necessary to set <code>CUDA_TOOLKIT_ROOT_DIR</code> manually on certain platforms, or to use a CUDA runtime not installed in the default location. In newer versions of the toolkit the CUDA library is included with the graphics driver &#8212; be sure that the driver version matches what is needed by the CUDA runtime version.</p>
<h3>Input Variables</h3>
<p>The following variables affect the behavior of the macros in the script (in alphabetical order). Note that any of these flags can be changed multiple times in the same directory before calling <code>cuda_add_executable()</code>, <code>cuda_add_library()</code>, <code>cuda_compile()</code>, <code>cuda_compile_ptx()</code>, <code>cuda_compile_fatbin()</code>, <code>cuda_compile_cubin()</code> or <code>cuda_wrap_srcs()</code>:</p>
<dl>
<dt><code>CUDA_64_BIT_DEVICE_CODE</code> (Default: host bit size)</p>
<dd>Set to <code>ON</code> to compile for 64 bit device code, OFF for 32 bit device code. Note that making this different from the host code when generating object or C files from CUDA code just won&#8217;t work, because size_t gets defined by nvcc in the generated source. If you compile to PTX and then load the file yourself, you can mix bit sizes between device and host.</p>
<dt><code>CUDA_ATTACH_VS_BUILD_RULE_TO_CUDA_FILE</code> (Default: <code>ON</code>)</p>
<dd>Set to <code>ON</code> if you want the custom build rule to be attached to the source file in Visual Studio. Turn OFF if you add the same cuda file to multiple targets. </p>
<p> This allows the user to build the target from the CUDA file; however, bad things can happen if the CUDA source file is added to multiple targets. When performing parallel builds it is possible for the custom build command to be run more than once and in parallel causing cryptic build errors. VS runs the rules for every source file in the target, and a source can have only one rule no matter how many projects it is added to. When the rule is run from multiple targets race conditions can occur on the generated file. Eventually everything will get built, but if the user is unaware of this behavior, there may be confusion. It would be nice if this script could detect the reuse of source files across multiple targets and turn the option off for the user, but no good solution could be found.</p>
<dt><code>CUDA_BUILD_CUBIN</code> (Default: <code>OFF</code>)</p>
<dd>Set to <code>ON</code> to enable and extra compilation pass with the <code>-cubin</code> option in Device mode. The output is parsed and register, shared memory usage is printed during build.</p>
<dt><code>CUDA_BUILD_EMULATION</code> (Default: <code>OFF</code> for device mode)</p>
<dd>Set to <code>ON</code> for Emulation mode. <code>-D_DEVICEEMU</code> is defined for CUDA C files when <code>CUDA_BUILD_EMULATION</code> is <code>TRUE</code>.</p>
<dt><code>CUDA_LINK_LIBRARIES_KEYWORD</code> (Default: )</p>
<dd>New in version 3.9. </p>
<p> The <code>&lt;PRIVATE|PUBLIC|INTERFACE&gt;</code> keyword to use for internal <code>target_link_libraries()</code> calls. The default is to use no keyword which uses the old &quot;plain&quot; form of <code>target_link_libraries()</code>. Note that is matters because whatever is used inside the <code>FindCUDA</code> module must also be used outside &#8211; the two forms of <code>target_link_libraries()</code> cannot be mixed.</p>
<dt><code>CUDA_GENERATED_OUTPUT_DIR</code> (Default: <code>CMAKE_CURRENT_BINARY_DIR</code>)</p>
<dd>Set to the path you wish to have the generated files placed. If it is blank output files will be placed in <code>CMAKE_CURRENT_BINARY_DIR</code>. Intermediate files will always be placed in <code>CMAKE_CURRENT_BINARY_DIR/CMakeFiles</code>.</p>
<dt><code>CUDA_HOST_COMPILATION_CPP</code> (Default: <code>ON</code>)</p>
<dd>Set to <code>OFF</code> for C compilation of host code.</p>
<dt><code>CUDA_HOST_COMPILER</code> (Default: <code>CMAKE_C_COMPILER</code>)</p>
<dd>Set the host compiler to be used by nvcc. Ignored if <code>-ccbin</code> or <code>&#8211;compiler-bindir</code> is already present in the <code>CUDA_NVCC_FLAGS</code> or <code>CUDA_NVCC_FLAGS_&lt;CONFIG&gt;</code> variables. For Visual Studio targets, the host compiler is constructed with one or more visual studio macros such as <code>$(VCInstallDir)</code>, that expands out to the path when the command is run from within VS. </p>
<p> New in version 3.13: If the <code>CUDAHOSTCXX</code> environment variable is set it will be used as the default. </p>
<dt><code>CUDA_NVCC_FLAGS</code>, <code>CUDA_NVCC_FLAGS_&lt;CONFIG&gt;</code></p>
<dd>Additional NVCC command line arguments. NOTE: multiple arguments must be semi-colon delimited (e.g. <code>&#8211;compiler-options;-Wall</code>) </p>
<p> New in version 3.6: Contents of these variables may use <code>generator expressions</code>. </p>
<dt><code>CUDA_PROPAGATE_HOST_FLAGS</code> (Default: <code>ON</code>)</p>
<dd>Set to <code>ON</code> to propagate <code>CMAKE_{C,CXX}_FLAGS</code> and their configuration dependent counterparts (e.g. <code>CMAKE_C_FLAGS_DEBUG</code>) automatically to the host compiler through nvcc&#8217;s <code>-Xcompiler</code> flag. This helps make the generated host code match the rest of the system better. Sometimes certain flags give nvcc problems, and this will help you turn the flag propagation off. This does not affect the flags supplied directly to nvcc via <code>CUDA_NVCC_FLAGS</code> or through the <code>OPTION</code> flags specified through <code>cuda_add_library()</code>, <code>cuda_add_executable()</code>, or <code>cuda_wrap_srcs()</code>. Flags used for shared library compilation are not affected by this flag.</p>
<dt><code>CUDA_SEPARABLE_COMPILATION</code> (Default: <code>OFF</code>)</p>
<dd>If set this will enable separable compilation for all CUDA runtime object files. If used outside of <code>cuda_add_executable()</code> and <code>cuda_add_library()</code> (e.g. calling <code>cuda_wrap_srcs()</code> directly), <code>cuda_compute_separable_compilation_object_file_name()</code> and <code>cuda_link_separable_compilation_objects()</code> should be called.</p>
<dt><code>CUDA_SOURCE_PROPERTY_FORMAT</code></p>
<dd>New in version 3.3. </p>
<p> If this source file property is set, it can override the format specified to <code>cuda_wrap_srcs()</code> (<code>OBJ</code>, <code>PTX</code>, <code>CUBIN</code>, or <code>FATBIN</code>). If an input source file is not a <code>.cu</code> file, setting this file will cause it to be treated as a <code>.cu</code> file. See documentation for set_source_files_properties on how to set this property.</p>
<dt><code>CUDA_USE_STATIC_CUDA_RUNTIME</code> (Default: <code>ON</code>)</p>
<dd>New in version 3.3. </p>
<p> When enabled the static version of the CUDA runtime library will be used in <code>CUDA_LIBRARIES</code>. If the version of CUDA configured doesn&#8217;t support this option, then it will be silently disabled.</p>
<dt><code>CUDA_VERBOSE_BUILD</code> (Default: <code>OFF</code>)</p>
<dd>Set to <code>ON</code> to see all the commands used when building the CUDA file. When using a Makefile generator the value defaults to <code>VERBOSE</code> (run <code>make VERBOSE=1</code> to see output), although setting <code>CUDA_VERBOSE_BUILD</code> to <code>ON</code> will always print the output.</dl>
<h3>Commands</h3>
<p>The script creates the following functions and macros (in alphabetical order): </p>
<pre>cuda_add_cufft_to_target(&lt;cuda_target&gt;)</pre>
<p>Adds the cufft library to the target (can be any target). Handles whether you are in emulation mode or not. </p>
<pre>cuda_add_cublas_to_target(&lt;cuda_target&gt;)</pre>
<p>Adds the cublas library to the target (can be any target). Handles whether you are in emulation mode or not. </p>
<pre>cuda_add_executable(&lt;cuda_target&gt; &lt;file&gt;...
 [WIN32] [MACOSX_BUNDLE] [EXCLUDE_FROM_ALL] [OPTIONS ...])</pre>
<p>Creates an executable <code>&lt;cuda_target&gt;</code> which is made up of the files specified. All of the non CUDA C files are compiled using the standard build rules specified by CMake and the CUDA files are compiled to object files using nvcc and the host compiler. In addition <code>CUDA_INCLUDE_DIRS</code> is added automatically to <code>include_directories()</code>. Some standard CMake target calls can be used on the target after calling this macro (e.g. <code>set_target_properties()</code> and <code>target_link_libraries()</code>), but setting properties that adjust compilation flags will not affect code compiled by nvcc. Such flags should be modified before calling <code>cuda_add_executable()</code>, <code>cuda_add_library()</code> or <code>cuda_wrap_srcs()</code>. </p>
<pre>cuda_add_library(&lt;cuda_target&gt; &lt;file&gt;...
 [STATIC | SHARED | MODULE] [EXCLUDE_FROM_ALL] [OPTIONS ...])</pre>
<p>Same as <code>cuda_add_executable()</code> except that a library is created. </p>
<pre>cuda_build_clean_target()</pre>
<p>Creates a convenience target that deletes all the dependency files generated. You should make clean after running this target to ensure the dependency files get regenerated. </p>
<pre>cuda_compile(&lt;generated_files&gt; &lt;file&gt;... [STATIC | SHARED | MODULE]
 [OPTIONS ...])</pre>
<p>Returns a list of generated files from the input source files to be used with <code>add_library()</code> or <code>add_executable()</code>. </p>
<pre>cuda_compile_ptx(&lt;generated_files&gt; &lt;file&gt;... [OPTIONS ...])</pre>
<p>Returns a list of <code>PTX</code> files generated from the input source files. </p>
<pre>cuda_compile_fatbin(&lt;generated_files&gt; &lt;file&gt;... [OPTIONS ...])</pre>
<p>New in version 3.1. </p>
<p> Returns a list of <code>FATBIN</code> files generated from the input source files. </p>
<pre>cuda_compile_cubin(&lt;generated_files&gt; &lt;file&gt;... [OPTIONS ...])</pre>
<p>New in version 3.1. </p>
<p> Returns a list of <code>CUBIN</code> files generated from the input source files. </p>
<pre>cuda_compute_separable_compilation_object_file_name(&lt;output_file_var&gt;
 &lt;cuda_target&gt;
 &lt;object_files&gt;)</pre>
<p>Compute the name of the intermediate link file used for separable compilation. This file name is typically passed into <code>CUDA_LINK_SEPARABLE_COMPILATION_OBJECTS</code>. output_file_var is produced based on cuda_target the list of objects files that need separable compilation as specified by <code>&lt;object_files&gt;</code>. If the <code>&lt;object_files&gt;</code> list is empty, then <code>&lt;output_file_var&gt;</code> will be empty. This function is called automatically for <code>cuda_add_library()</code> and <code>cuda_add_executable()</code>. Note that this is a function and not a macro. </p>
<pre>cuda_include_directories(path0 path1 ...)</pre>
<p>Sets the directories that should be passed to nvcc (e.g. <code>nvcc -Ipath0 -Ipath1 &#8230;</code>). These paths usually contain other <code>.cu</code> files. </p>
<pre>cuda_link_separable_compilation_objects(&lt;output_file_var&gt; &lt;cuda_target&gt;
 &lt;nvcc_flags&gt; &lt;object_files&gt;)</pre>
<p>Generates the link object required by separable compilation from the given object files. This is called automatically for <code>cuda_add_executable()</code> and <code>cuda_add_library()</code>, but can be called manually when using <code>cuda_wrap_srcs()</code> directly. When called from <code>cuda_add_library()</code> or <code>cuda_add_executable()</code> the <code>&lt;nvcc_flags&gt;</code> passed in are the same as the flags passed in via the <code>OPTIONS</code> argument. The only nvcc flag added automatically is the bitness flag as specified by <code>CUDA_64_BIT_DEVICE_CODE</code>. Note that this is a function instead of a macro. </p>
<pre>cuda_select_nvcc_arch_flags(&lt;out_variable&gt; [&lt;target_CUDA_architecture&gt; ...])</pre>
<p>Selects GPU arch flags for nvcc based on <code>target_CUDA_architecture</code>. </p>
<p> Values for <code>target_CUDA_architecture</code>:</p>
<dl>
<dt>&bull;</p>
<dd><code>Auto</code>: detects local machine GPU compute arch at runtime.</p>
<dt>&bull;</p>
<dd><code>Common</code> and <code>All</code>: cover common and entire subsets of architectures.</p>
<dt>&bull;</p>
<dd><code>&lt;name&gt;</code>: one of <code>Fermi</code>, <code>Kepler</code>, <code>Maxwell</code>, <code>Kepler+Tegra</code>, <code>Kepler+Tesla</code>, <code>Maxwell+Tegra</code>, <code>Pascal</code>.</p>
<dt>&bull;</p>
<dd><code>&lt;ver&gt;</code>, <code>&lt;ver&gt;(&lt;ver&gt;)</code>, <code>&lt;ver&gt;+PTX</code>, where <code>&lt;ver&gt;</code> is one of <code>2.0</code>, <code>2.1</code>, <code>3.0</code>, <code>3.2</code>, <code>3.5</code>, <code>3.7</code>, <code>5.0</code>, <code>5.2</code>, <code>5.3</code>, <code>6.0</code>, <code>6.2</code>. </p>
<p> Returns list of flags to be added to <code>CUDA_NVCC_FLAGS</code> in <code>&lt;out_variable&gt;</code>. Additionally, sets <code>&lt;out_variable&gt;_readable</code> to the resulting numeric list. </p>
<p> Example: </p>
<pre>cuda_select_nvcc_arch_flags(ARCH_FLAGS 3.0 3.5+PTX 5.2(5.0) Maxwell)
list(APPEND CUDA_NVCC_FLAGS ${ARCH_FLAGS})</pre>
<p>More info on CUDA architectures: <i><a rel="nofollow" href="https://en.wikipedia.org/wiki/CUDA">https://en.wikipedia.org/wiki/CUDA</a></i>. Note that this is a function instead of a macro. </p>
<pre>cuda_wrap_srcs(&lt;cuda_target&gt; &lt;format&gt; &lt;generated_files&gt; &lt;file&gt;...
 [STATIC | SHARED | MODULE] [OPTIONS ...])</pre>
<p>This is where all the magic happens. <code>cuda_add_executable()</code>, <code>cuda_add_library()</code>, <code>cuda_compile()</code>, and <code>cuda_compile_ptx()</code> all call this function under the hood. </p>
<p> Given the list of files <code>&lt;file&gt;&#8230;</code> this macro generates custom commands that generate either PTX or linkable objects (use <code>PTX</code> or <code>OBJ</code> for the <code>&lt;format&gt;</code> argument to switch). Files that don&#8217;t end with <code>.cu</code> or have the <code>HEADER_FILE_ONLY</code> property are ignored. </p>
<p> The arguments passed in after <code>OPTIONS</code> are extra command line options to give to nvcc. You can also specify per configuration options by specifying the name of the configuration followed by the options. General options must precede configuration specific options. Not all configurations need to be specified, only the ones provided will be used. For example: </p>
<pre>cuda_add_executable(...
 OPTIONS -DFLAG=2 &quot;-DFLAG_OTHER=space in flag&quot;
 DEBUG -g
 RELEASE --use_fast_math
 RELWITHDEBINFO --use_fast_math;-g
 MINSIZEREL --use_fast_math)</pre>
<p>For certain configurations (namely VS generating object files with <code>CUDA_ATTACH_VS_BUILD_RULE_TO_CUDA_FILE</code> set to <code>ON</code>), no generated file will be produced for the given cuda file. This is because when you add the cuda file to Visual Studio it knows that this file produces an object file and will link in the resulting object file automatically. </p>
<p> This script will also generate a separate cmake script that is used at build time to invoke nvcc. This is for several reasons:</p>
<dt>&bull;</p>
<dd>nvcc can return negative numbers as return values which confuses Visual Studio into thinking that the command succeeded. The script now checks the error codes and produces errors when there was a problem.</p>
<dt>&bull;</p>
<dd>nvcc has been known to not delete incomplete results when it encounters problems. This confuses build systems into thinking the target was generated when in fact an unusable file exists. The script now deletes the output files if there was an error.</p>
<dt>&bull;</p>
<dd>By putting all the options that affect the build into a file and then make the build rule dependent on the file, the output files will be regenerated when the options change. </p>
<p> This script also looks at optional arguments <code>STATIC</code>, <code>SHARED</code>, or <code>MODULE</code> to determine when to target the object compilation for a shared library. <code>BUILD_SHARED_LIBS</code> is ignored in <code>cuda_wrap_srcs()</code>, but it is respected in <code>cuda_add_library()</code>. On some systems special flags are added for building objects intended for shared libraries. A preprocessor macro, <code>&lt;target_name&gt;_EXPORTS</code> is defined when a shared library compilation is detected. </p>
<p> Flags passed into add_definitions with <code>-D</code> or <code>/D</code> are passed along to nvcc.</dl>
<h3>Result Variables</h3>
<p>The script defines the following variables:</p>
<dl>
<dt><code>CUDA_VERSION_MAJOR</code></p>
<dd>The major version of cuda as reported by nvcc.</p>
<dt><code>CUDA_VERSION_MINOR</code></p>
<dd>The minor version.</p>
<dt><code>CUDA_VERSION</code>, <code>CUDA_VERSION_STRING</code></p>
<dd>Full version in the <code>X.Y</code> format.</p>
<dt><code>CUDA_HAS_FP16</code></p>
<dd>New in version 3.6: Whether a short float (<code>float16</code>, <code>fp16</code>) is supported. </p>
<dt><code>CUDA_TOOLKIT_ROOT_DIR</code></p>
<dd>Path to the CUDA Toolkit (defined if not set).</p>
<dt><code>CUDA_SDK_ROOT_DIR</code></p>
<dd>Path to the CUDA SDK. Use this to find files in the SDK. This script will not directly support finding specific libraries or headers, as that isn&#8217;t supported by NVIDIA. If you want to change libraries when the path changes see the <code>FindCUDA.cmake</code> script for an example of how to clear these variables. There are also examples of how to use the <code>CUDA_SDK_ROOT_DIR</code> to locate headers or libraries, if you so choose (at your own risk).</p>
<dt><code>CUDA_INCLUDE_DIRS</code></p>
<dd>Include directory for cuda headers. Added automatically for <code>cuda_add_executable()</code> and <code>cuda_add_library()</code>.</p>
<dt><code>CUDA_LIBRARIES</code></p>
<dd>Cuda RT library.</p>
<dt><code>CUDA_CUFFT_LIBRARIES</code></p>
<dd>Device or emulation library for the Cuda FFT implementation (alternative to <code>cuda_add_cufft_to_target()</code> macro)</p>
<dt><code>CUDA_CUBLAS_LIBRARIES</code></p>
<dd>Device or emulation library for the Cuda BLAS implementation (alternative to <code>cuda_add_cublas_to_target()</code> macro).</p>
<dt><code>CUDA_cudart_static_LIBRARY</code></p>
<dd>Statically linkable cuda runtime library. Only available for CUDA version 5.5+.</p>
<dt><code>CUDA_cudadevrt_LIBRARY</code></p>
<dd>New in version 3.7: Device runtime library. Required for separable compilation. </p>
<dt><code>CUDA_cupti_LIBRARY</code></p>
<dd>CUDA Profiling Tools Interface library. Only available for CUDA version 4.0+.</p>
<dt><code>CUDA_curand_LIBRARY</code></p>
<dd>CUDA Random Number Generation library. Only available for CUDA version 3.2+.</p>
<dt><code>CUDA_cusolver_LIBRARY</code></p>
<dd>New in version 3.2: CUDA Direct Solver library. Only available for CUDA version 7.0+. </p>
<dt><code>CUDA_cusparse_LIBRARY</code></p>
<dd>CUDA Sparse Matrix library. Only available for CUDA version 3.2+.</p>
<dt><code>CUDA_npp_LIBRARY</code></p>
<dd>NVIDIA Performance Primitives lib. Only available for CUDA version 4.0+.</p>
<dt><code>CUDA_nppc_LIBRARY</code></p>
<dd>NVIDIA Performance Primitives lib (core). Only available for CUDA version 5.5+.</p>
<dt><code>CUDA_nppi_LIBRARY</code></p>
<dd>NVIDIA Performance Primitives lib (image processing). Only available for CUDA version 5.5 &#8211; 8.0.</p>
<dt><code>CUDA_nppial_LIBRARY</code></p>
<dd>NVIDIA Performance Primitives lib (image processing). Only available for CUDA version 9.0.</p>
<dt><code>CUDA_nppicc_LIBRARY</code></p>
<dd>NVIDIA Performance Primitives lib (image processing). Only available for CUDA version 9.0.</p>
<dt><code>CUDA_nppicom_LIBRARY</code></p>
<dd>NVIDIA Performance Primitives lib (image processing). Only available for CUDA version 9.0 &#8211; 10.2. Replaced by nvjpeg.</p>
<dt><code>CUDA_nppidei_LIBRARY</code></p>
<dd>NVIDIA Performance Primitives lib (image processing). Only available for CUDA version 9.0.</p>
<dt><code>CUDA_nppif_LIBRARY</code></p>
<dd>NVIDIA Performance Primitives lib (image processing). Only available for CUDA version 9.0.</p>
<dt><code>CUDA_nppig_LIBRARY</code></p>
<dd>NVIDIA Performance Primitives lib (image processing). Only available for CUDA version 9.0.</p>
<dt><code>CUDA_nppim_LIBRARY</code></p>
<dd>NVIDIA Performance Primitives lib (image processing). Only available for CUDA version 9.0.</p>
<dt><code>CUDA_nppist_LIBRARY</code></p>
<dd>NVIDIA Performance Primitives lib (image processing). Only available for CUDA version 9.0.</p>
<dt><code>CUDA_nppisu_LIBRARY</code></p>
<dd>NVIDIA Performance Primitives lib (image processing). Only available for CUDA version 9.0.</p>
<dt><code>CUDA_nppitc_LIBRARY</code></p>
<dd>NVIDIA Performance Primitives lib (image processing). Only available for CUDA version 9.0.</p>
<dt><code>CUDA_npps_LIBRARY</code></p>
<dd>NVIDIA Performance Primitives lib (signal processing). Only available for CUDA version 5.5+.</p>
<dt><code>CUDA_nvcuvenc_LIBRARY</code></p>
<dd>CUDA Video Encoder library. Only available for CUDA version 3.2+. Windows only.</p>
<dt><code>CUDA_nvcuvid_LIBRARY</code></p>
<dd>CUDA Video Decoder library. Only available for CUDA version 3.2+. Windows only.</p>
<dt><code>CUDA_nvToolsExt_LIBRARY</code></p>
<dd>New in version 3.16: NVIDA CUDA Tools Extension library. Available for CUDA version 5+. </p>
<dt><code>CUDA_OpenCL_LIBRARY</code></p>
<dd>New in version 3.16: NVIDA CUDA OpenCL library. Available for CUDA version 5+. </p>
</dl>
<h3>FindPythonInterp</h3>
<p>Deprecated since version 3.12: Use <code>FindPython3</code>, <code>FindPython2</code> or <code>FindPython</code> instead. </p>
<p> Find python interpreter </p>
<p> This module finds if Python interpreter is installed and determines where the executables are. This code sets the following variables: </p>
<pre>PYTHONINTERP_FOUND - Was the Python executable found
PYTHON_EXECUTABLE - path to the Python interpreter</pre>
<pre>PYTHON_VERSION_STRING - Python version found e.g. 2.5.2
PYTHON_VERSION_MAJOR - Python major version found e.g. 2
PYTHON_VERSION_MINOR - Python minor version found e.g. 5
PYTHON_VERSION_PATCH - Python patch version found e.g. 2</pre>
<p>The Python_ADDITIONAL_VERSIONS variable can be used to specify a list of version numbers that should be taken into account when searching for Python. You need to set this variable before calling find_package(PythonInterp). </p>
<p> If calling both <code>find_package(PythonInterp)</code> and <code>find_package(PythonLibs)</code>, call <code>find_package(PythonInterp)</code> first to get the currently active Python version by default with a consistent version of PYTHON_LIBRARIES. </p>
<p> <code>NOTE:</code> A call to <code>find_package(PythonInterp ${V})</code> for python version <code>V</code> may find a <code>python</code> executable with no version suffix. In this case no attempt is made to avoid python executables from other versions. Use <code>FindPython3</code>, <code>FindPython2</code> or <code>FindPython</code> instead.</p>
<h3>FindPythonLibs</h3>
<p>Deprecated since version 3.12: Use <code>FindPython3</code>, <code>FindPython2</code> or <code>FindPython</code> instead. </p>
<p> Find python libraries </p>
<p> This module finds if Python is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>PYTHONLIBS_FOUND - have the Python libs been found
PYTHON_LIBRARIES - path to the python library
PYTHON_INCLUDE_PATH - path to where Python.h is found (deprecated)
PYTHON_INCLUDE_DIRS - path to where Python.h is found
PYTHON_DEBUG_LIBRARIES - path to the debug library (deprecated)
PYTHONLIBS_VERSION_STRING - version of the Python libs found (since CMake 2.8.8)</pre>
<p>The Python_ADDITIONAL_VERSIONS variable can be used to specify a list of version numbers that should be taken into account when searching for Python. You need to set this variable before calling find_package(PythonLibs). </p>
<p> If you&#8217;d like to specify the installation of Python to use, you should modify the following cache variables: </p>
<pre>PYTHON_LIBRARY - path to the python library
PYTHON_INCLUDE_DIR - path to where Python.h is found</pre>
<p>If calling both <code>find_package(PythonInterp)</code> and <code>find_package(PythonLibs)</code>, call <code>find_package(PythonInterp)</code> first to get the currently active Python version by default with a consistent version of PYTHON_LIBRARIES.</p>
<h3>FindQt</h3>
<p>Deprecated since version 3.14: This module is available only if policy <code>CMP0084</code> is not set to <code>NEW</code>. </p>
<p> Searches for all installed versions of Qt3 or Qt4. </p>
<p> This module cannot handle Qt5 or any later versions. For those, see <code><a href="/docs/linux/man/7-cmake-qt/">cmake-qt</a>(7)</code>. </p>
<p> This module should only be used if your project can work with multiple versions of Qt. If not, you should just directly use FindQt4 or FindQt3. If multiple versions of Qt are found on the machine, then The user must set the option DESIRED_QT_VERSION to the version they want to use. If only one version of qt is found on the machine, then the DESIRED_QT_VERSION is set to that version and the matching FindQt3 or FindQt4 module is included. Once the user sets DESIRED_QT_VERSION, then the FindQt3 or FindQt4 module is included. </p>
<pre>QT_REQUIRED if this is set to TRUE then if CMake can
 not find Qt4 or Qt3 an error is raised
 and a message is sent to the user.</pre>
<pre>DESIRED_QT_VERSION OPTION is created
QT4_INSTALLED is set to TRUE if qt4 is found.
QT3_INSTALLED is set to TRUE if qt3 is found.</pre>
<h3>FindwxWindows</h3>
<p>Deprecated since version 3.0: Replaced by <code>FindwxWidgets</code>. </p>
<p> Find wxWindows (wxWidgets) installation </p>
<p> This module finds if wxWindows/wxWidgets is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>WXWINDOWS_FOUND = system has WxWindows
WXWINDOWS_LIBRARIES = path to the wxWindows libraries
 on Unix/Linux with additional
 linker flags from
 &quot;wx-config --libs&quot;
CMAKE_WXWINDOWS_CXX_FLAGS = Compiler flags for wxWindows,
 essentially &quot;`wx-config --cxxflags`&quot;
 on Linux
WXWINDOWS_INCLUDE_DIR = where to find &quot;wx/wx.h&quot; and &quot;wx/setup.h&quot;
WXWINDOWS_LINK_DIRECTORIES = link directories, useful for rpath on
 Unix
WXWINDOWS_DEFINITIONS = extra defines</pre>
<p>OPTIONS If you need OpenGL support please </p>
<pre>set(WXWINDOWS_USE_GL 1)</pre>
<p>in your CMakeLists.txt <i>before</i> you include this file. </p>
<pre>HAVE_ISYSTEM - true required to replace -I by -isystem on g++</pre>
<p>For convenience include Use_wxWindows.cmake in your project&#8217;s CMakeLists.txt using include(${CMAKE_CURRENT_LIST_DIR}/Use_wxWindows.cmake). </p>
<p> USAGE </p>
<pre>set(WXWINDOWS_USE_GL 1)
find_package(wxWindows)</pre>
<p>NOTES wxWidgets 2.6.x is supported for monolithic builds e.g. compiled in wx/build/msw dir as: </p>
<pre>nmake -f makefile.vc BUILD=debug SHARED=0 USE_OPENGL=1 MONOLITHIC=1</pre>
<p>DEPRECATED </p>
<pre>CMAKE_WX_CAN_COMPILE
WXWINDOWS_LIBRARY
CMAKE_WX_CXX_FLAGS
WXWINDOWS_INCLUDE_PATH</pre>
<p>AUTHOR Jan Woetzel &lt;<i><a rel="nofollow" href="http://www.mip.informatik.uni-kiel.de/~jw">http://www.mip.informatik.uni-kiel.de/~jw</a></i>&gt; (07/2003-01/2006)</p>
<h3>Legacy CPack Modules</h3>
<p>These modules used to be mistakenly exposed to the user, and have been moved out of user visibility. They are for CPack internal use, and should never be used directly.</p>
<h3>CPackArchive</h3>
<p>New in version 3.9. </p>
<p> The documentation for the CPack Archive generator has moved here: <code>CPack Archive Generator</code></p>
<h3>CPackBundle</h3>
<p>The documentation for the CPack Bundle generator has moved here: <code>CPack Bundle Generator</code></p>
<h3>CPackCygwin</h3>
<p>The documentation for the CPack Cygwin generator has moved here: <code>CPack Cygwin Generator</code></p>
<h3>CPackDeb</h3>
<p>The documentation for the CPack DEB generator has moved here: <code>CPack DEB Generator</code></p>
<h3>CPackDMG</h3>
<p>The documentation for the CPack DragNDrop generator has moved here: <code>CPack DragNDrop Generator</code></p>
<h3>CPackFreeBSD</h3>
<p>New in version 3.10. </p>
<p> The documentation for the CPack FreeBSD generator has moved here: <code>CPack FreeBSD Generator</code></p>
<h3>CPackNSIS</h3>
<p>The documentation for the CPack NSIS generator has moved here: <code>CPack NSIS Generator</code></p>
<h3>CPackNuGet</h3>
<p>New in version 3.12. </p>
<p> The documentation for the CPack NuGet generator has moved here: <code>CPack NuGet Generator</code></p>
<h3>CPackPackageMaker</h3>
<p>The documentation for the CPack PackageMaker generator has moved here: <code>CPack PackageMaker Generator</code></p>
<h3>CPackProductBuild</h3>
<p>New in version 3.7. </p>
<p> The documentation for the CPack productbuild generator has moved here: <code>CPack productbuild Generator</code></p>
<h3>CPackRPM</h3>
<p>The documentation for the CPack RPM generator has moved here: <code>CPack RPM Generator</code></p>
<h3>CPackWIX</h3>
<p>The documentation for the CPack WIX generator has moved here: <code>CPack WIX Generator</code></p>
<h2>Copyright</h2>
<p>2000-2022 Kitware, Inc. and Contributors</p>
