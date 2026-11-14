---
title: "cmake3-modules(7)"
name: "cmake3-modules"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake3-modules/"
description: "cmake-modules – CMake Modules Reference"
---

<p>cmake-modules &#8211; CMake Modules Reference</p>
<h2>All Modules</h2>
<h3>AddFileDependencies</h3>
<p>ADD_FILE_DEPENDENCIES(source_file depend_files&#8230;) </p>
<p> Adds the given files as dependencies to source_file</p>
<h3>BundleUtilities</h3>
<p>Functions to help assemble a standalone bundle application. </p>
<p> A collection of CMake utility functions useful for dealing with .app bundles on the Mac and bundle-like directories on any OS. </p>
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
<p>Requires CMake 2.6 or greater because it uses function, break and PARENT_SCOPE. Also depends on GetPrerequisites.cmake. </p>
<pre>FIXUP_BUNDLE(&lt;app&gt; &lt;libs&gt; &lt;dirs&gt;)</pre>
<p>Fix up a bundle in-place and make it standalone, such that it can be drag-n-drop copied to another machine and run on that machine as long as all of the system libraries are compatible. </p>
<p> If you pass plugins to fixup_bundle as the libs parameter, you should install them or copy them into the bundle before calling fixup_bundle. The &quot;libs&quot; parameter is a list of libraries that must be fixed up, but that cannot be determined by otool output analysis. (i.e., plugins) </p>
<p> Gather all the keys for all the executables and libraries in a bundle, and then, for each key, copy each prerequisite into the bundle. Then fix each one up according to its own list of prerequisites. </p>
<p> Then clear all the keys and call verify_app on the final bundle to ensure that it is truly standalone. </p>
<p> As an optional parameter (IGNORE_ITEM) a list of file names can be passed, which are then ignored (e.g. IGNORE_ITEM &quot;vcredist_x86.exe;vcredist_x64.exe&quot;) </p>
<pre>COPY_AND_FIXUP_BUNDLE(&lt;src&gt; &lt;dst&gt; &lt;libs&gt; &lt;dirs&gt;)</pre>
<p>Makes a copy of the bundle &lt;src&gt; at location &lt;dst&gt; and then fixes up the new copied bundle in-place at &lt;dst&gt;&#8230; </p>
<pre>VERIFY_APP(&lt;app&gt;)</pre>
<p>Verifies that an application &lt;app&gt; appears valid based on running analysis tools on it. Calls &quot;message(FATAL_ERROR&quot; if the application is not verified. </p>
<p> As an optional parameter (IGNORE_ITEM) a list of file names can be passed, which are then ignored (e.g. IGNORE_ITEM &quot;vcredist_x86.exe;vcredist_x64.exe&quot;) </p>
<pre>GET_BUNDLE_MAIN_EXECUTABLE(&lt;bundle&gt; &lt;result_var&gt;)</pre>
<p>The result will be the full path name of the bundle&#8217;s main executable file or an &quot;error:&quot; prefixed string if it could not be determined. </p>
<pre>GET_DOTAPP_DIR(&lt;exe&gt; &lt;dotapp_dir_var&gt;)</pre>
<p>Returns the nearest parent dir whose name ends with &quot;.app&quot; given the full path to an executable. If there is no such parent dir, then simply return the dir containing the executable. </p>
<p> The returned directory may or may not exist. </p>
<pre>GET_BUNDLE_AND_EXECUTABLE(&lt;app&gt; &lt;bundle_var&gt; &lt;executable_var&gt; &lt;valid_var&gt;)</pre>
<p>Takes either a &quot;.app&quot; directory name or the name of an executable nested inside a &quot;.app&quot; directory and returns the path to the &quot;.app&quot; directory in &lt;bundle_var&gt; and the path to its main executable in &lt;executable_var&gt; </p>
<pre>GET_BUNDLE_ALL_EXECUTABLES(&lt;bundle&gt; &lt;exes_var&gt;)</pre>
<p>Scans the given bundle recursively for all executable files and accumulates them into a variable. </p>
<pre>GET_ITEM_KEY(&lt;item&gt; &lt;key_var&gt;)</pre>
<p>Given a file (item) name, generate a key that should be unique considering the set of libraries that need copying or fixing up to make a bundle standalone. This is essentially the file name including extension with &quot;.&quot; replaced by &quot;_&quot; </p>
<p> This key is used as a prefix for CMake variables so that we can associate a set of variables with a given item based on its key. </p>
<pre>CLEAR_BUNDLE_KEYS(&lt;keys_var&gt;)</pre>
<p>Loop over the list of keys, clearing all the variables associated with each key. After the loop, clear the list of keys itself. </p>
<p> Caller of get_bundle_keys should call clear_bundle_keys when done with list of keys. </p>
<pre>SET_BUNDLE_KEY_VALUES(&lt;keys_var&gt; &lt;context&gt; &lt;item&gt; &lt;exepath&gt; &lt;dirs&gt;
 &lt;copyflag&gt; [&lt;rpaths&gt;])</pre>
<p>Add a key to the list (if necessary) for the given item. If added, also set all the variables associated with that key. </p>
<pre>GET_BUNDLE_KEYS(&lt;app&gt; &lt;libs&gt; &lt;dirs&gt; &lt;keys_var&gt;)</pre>
<p>Loop over all the executable and library files within the bundle (and given as extra &lt;libs&gt;) and accumulate a list of keys representing them. Set values associated with each key such that we can loop over all of them and copy prerequisite libs into the bundle and then do appropriate install_name_tool fixups. </p>
<p> As an optional parameter (IGNORE_ITEM) a list of file names can be passed, which are then ignored (e.g. IGNORE_ITEM &quot;vcredist_x86.exe;vcredist_x64.exe&quot;) </p>
<pre>COPY_RESOLVED_ITEM_INTO_BUNDLE(&lt;resolved_item&gt; &lt;resolved_embedded_item&gt;)</pre>
<p>Copy a resolved item into the bundle if necessary. Copy is not necessary if the resolved_item is &quot;the same as&quot; the resolved_embedded_item. </p>
<pre>COPY_RESOLVED_FRAMEWORK_INTO_BUNDLE(&lt;resolved_item&gt; &lt;resolved_embedded_item&gt;)</pre>
<p>Copy a resolved framework into the bundle if necessary. Copy is not necessary if the resolved_item is &quot;the same as&quot; the resolved_embedded_item. </p>
<p> By default, BU_COPY_FULL_FRAMEWORK_CONTENTS is not set. If you want full frameworks embedded in your bundles, set BU_COPY_FULL_FRAMEWORK_CONTENTS to ON before calling fixup_bundle. By default, COPY_RESOLVED_FRAMEWORK_INTO_BUNDLE copies the framework dylib itself plus the framework Resources directory. </p>
<pre>FIXUP_BUNDLE_ITEM(&lt;resolved_embedded_item&gt; &lt;exepath&gt; &lt;dirs&gt;)</pre>
<p>Get the direct/non-system prerequisites of the resolved embedded item. For each prerequisite, change the way it is referenced to the value of the _EMBEDDED_ITEM keyed variable for that prerequisite. (Most likely changing to an &quot;@executable_path&quot; style reference.) </p>
<p> This function requires that the resolved_embedded_item be &quot;inside&quot; the bundle already. In other words, if you pass plugins to fixup_bundle as the libs parameter, you should install them or copy them into the bundle before calling fixup_bundle. The &quot;libs&quot; parameter is a list of libraries that must be fixed up, but that cannot be determined by otool output analysis. (i.e., plugins) </p>
<p> Also, change the id of the item being fixed up to its own _EMBEDDED_ITEM value. </p>
<p> Accumulate changes in a local variable and make <i>one</i> call to install_name_tool at the end of the function with all the changes at once. </p>
<p> If the BU_CHMOD_BUNDLE_ITEMS variable is set then bundle items will be marked writable before install_name_tool tries to change them. </p>
<pre>VERIFY_BUNDLE_PREREQUISITES(&lt;bundle&gt; &lt;result_var&gt; &lt;info_var&gt;)</pre>
<p>Verifies that the sum of all prerequisites of all files inside the bundle are contained within the bundle or are &quot;system&quot; libraries, presumed to exist everywhere. </p>
<p> As an optional parameter (IGNORE_ITEM) a list of file names can be passed, which are then ignored (e.g. IGNORE_ITEM &quot;vcredist_x86.exe;vcredist_x64.exe&quot;) </p>
<pre>VERIFY_BUNDLE_SYMLINKS(&lt;bundle&gt; &lt;result_var&gt; &lt;info_var&gt;)</pre>
<p>Verifies that any symlinks found in the bundle point to other files that are already also in the bundle&#8230; Anything that points to an external file causes this function to fail the verification.</p>
<h3>CheckCCompilerFlag</h3>
<p>Check whether the C compiler supports a given flag. </p>
<p> CHECK_C_COMPILER_FLAG(&lt;flag&gt; &lt;var&gt;) </p>
<pre>&lt;flag&gt; - the compiler flag
&lt;var&gt; - variable to store the result
 Will be created as an internal cache variable.</pre>
<p>This internally calls the check_c_source_compiles macro and sets CMAKE_REQUIRED_DEFINITIONS to &lt;flag&gt;. See help for CheckCSourceCompiles for a listing of variables that can otherwise modify the build. The result only tells that the compiler does not give an error message when it encounters the flag. If the flag has any effect or even a specific one is beyond the scope of this module.</p>
<h3>CheckCSourceCompiles</h3>
<p>Check if given C source compiles and links into an executable </p>
<p> CHECK_C_SOURCE_COMPILES(&lt;code&gt; &lt;var&gt; [FAIL_REGEX &lt;fail-regex&gt;]) </p>
<pre>&lt;code&gt; - source code to try to compile, must define 'main'
&lt;var&gt; - variable to store whether the source code compiled
 Will be created as an internal cache variable.
&lt;fail-regex&gt; - fail if test output matches this regex</pre>
<p>The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>CMAKE_REQUIRED_FLAGS = string of compile command line flags
CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
CMAKE_REQUIRED_INCLUDES = list of include directories
CMAKE_REQUIRED_LIBRARIES = list of libraries to link
CMAKE_REQUIRED_QUIET = execute quietly without messages</pre>
<h3>CheckCSourceRuns</h3>
<p>Check if the given C source code compiles and runs. </p>
<p> CHECK_C_SOURCE_RUNS(&lt;code&gt; &lt;var&gt;) </p>
<pre>&lt;code&gt; - source code to try to compile
&lt;var&gt; - variable to store the result
 (1 for success, empty for failure)
 Will be created as an internal cache variable.</pre>
<p>The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>CMAKE_REQUIRED_FLAGS = string of compile command line flags
CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
CMAKE_REQUIRED_INCLUDES = list of include directories
CMAKE_REQUIRED_LIBRARIES = list of libraries to link
CMAKE_REQUIRED_QUIET = execute quietly without messages</pre>
<h3>CheckCXXCompilerFlag</h3>
<p>Check whether the CXX compiler supports a given flag. </p>
<p> CHECK_CXX_COMPILER_FLAG(&lt;flag&gt; &lt;var&gt;) </p>
<pre>&lt;flag&gt; - the compiler flag
&lt;var&gt; - variable to store the result</pre>
<p>This internally calls the check_cxx_source_compiles macro and sets CMAKE_REQUIRED_DEFINITIONS to &lt;flag&gt;. See help for CheckCXXSourceCompiles for a listing of variables that can otherwise modify the build. The result only tells that the compiler does not give an error message when it encounters the flag. If the flag has any effect or even a specific one is beyond the scope of this module.</p>
<h3>CheckCXXSourceCompiles</h3>
<p>Check if given C++ source compiles and links into an executable </p>
<p> CHECK_CXX_SOURCE_COMPILES(&lt;code&gt; &lt;var&gt; [FAIL_REGEX &lt;fail-regex&gt;]) </p>
<pre>&lt;code&gt; - source code to try to compile, must define 'main'
&lt;var&gt; - variable to store whether the source code compiled
 Will be created as an internal cache variable.
&lt;fail-regex&gt; - fail if test output matches this regex</pre>
<p>The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>CMAKE_REQUIRED_FLAGS = string of compile command line flags
CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
CMAKE_REQUIRED_INCLUDES = list of include directories
CMAKE_REQUIRED_LIBRARIES = list of libraries to link
CMAKE_REQUIRED_QUIET = execute quietly without messages</pre>
<h3>CheckCXXSourceRuns</h3>
<p>Check if the given C++ source code compiles and runs. </p>
<p> CHECK_CXX_SOURCE_RUNS(&lt;code&gt; &lt;var&gt;) </p>
<pre>&lt;code&gt; - source code to try to compile
&lt;var&gt; - variable to store the result
 (1 for success, empty for failure)
 Will be created as an internal cache variable.</pre>
<p>The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>CMAKE_REQUIRED_FLAGS = string of compile command line flags
CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
CMAKE_REQUIRED_INCLUDES = list of include directories
CMAKE_REQUIRED_LIBRARIES = list of libraries to link
CMAKE_REQUIRED_QUIET = execute quietly without messages</pre>
<h3>CheckCXXSymbolExists</h3>
<p>Check if a symbol exists as a function, variable, or macro in C++ </p>
<p> CHECK_CXX_SYMBOL_EXISTS(&lt;symbol&gt; &lt;files&gt; &lt;variable&gt;) </p>
<p> Check that the &lt;symbol&gt; is available after including given header &lt;files&gt; and store the result in a &lt;variable&gt;. Specify the list of files in one argument as a semicolon-separated list. CHECK_CXX_SYMBOL_EXISTS() can be used to check in C++ files, as opposed to CHECK_SYMBOL_EXISTS(), which works only for C. </p>
<p> If the header files define the symbol as a macro it is considered available and assumed to work. If the header files declare the symbol as a function or variable then the symbol must also be available for linking. If the symbol is a type or enum value it will not be recognized (consider using CheckTypeSize or CheckCSourceCompiles). </p>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>CMAKE_REQUIRED_FLAGS = string of compile command line flags
CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
CMAKE_REQUIRED_INCLUDES = list of include directories
CMAKE_REQUIRED_LIBRARIES = list of libraries to link
CMAKE_REQUIRED_QUIET = execute quietly without messages</pre>
<h3>CheckFortranCompilerFlag</h3>
<p>Check whether the Fortran compiler supports a given flag. </p>
<p> CHECK_Fortran_COMPILER_FLAG(&lt;flag&gt; &lt;var&gt;) </p>
<pre>&lt;flag&gt; - the compiler flag
&lt;var&gt; - variable to store the result
 Will be created as an internal cache variable.</pre>
<p>This internally calls the check_fortran_source_compiles macro and sets CMAKE_REQUIRED_DEFINITIONS to &lt;flag&gt;. See help for CheckFortranSourceCompiles for a listing of variables that can otherwise modify the build. The result only tells that the compiler does not give an error message when it encounters the flag. If the flag has any effect or even a specific one is beyond the scope of this module.</p>
<h3>CheckFortranFunctionExists</h3>
<p>macro which checks if the Fortran function exists </p>
<p> CHECK_FORTRAN_FUNCTION_EXISTS(FUNCTION VARIABLE) </p>
<pre>FUNCTION - the name of the Fortran function
VARIABLE - variable to store the result
 Will be created as an internal cache variable.</pre>
<p>The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>CMAKE_REQUIRED_LIBRARIES = list of libraries to link</pre>
<h3>CheckFortranSourceCompiles</h3>
<p>Check if given Fortran source compiles and links into an executable: </p>
<pre>CHECK_Fortran_SOURCE_COMPILES(&lt;code&gt; &lt;var&gt; [FAIL_REGEX &lt;fail-regex&gt;])</pre>
<p>The arguments are:</p>
<dl>
<dt><code>&lt;code&gt;</code></p>
<dd>Source code to try to compile. It must define a PROGRAM entry point.</p>
<dt><code>&lt;var&gt;</code></p>
<dd>Variable to store whether the source code compiled. Will be created as an internal cache variable.</p>
<dt><code>&lt;fail-regex&gt;</code></p>
<dd>Fail if test output matches this regex. </p>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>CMAKE_REQUIRED_FLAGS = string of compile command line flags
CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
CMAKE_REQUIRED_INCLUDES = list of include directories
CMAKE_REQUIRED_LIBRARIES = list of libraries to link
CMAKE_REQUIRED_QUIET = execute quietly without messages</pre>
</dl>
<h3>CheckFunctionExists</h3>
<p>Check if a C function can be linked </p>
<p> CHECK_FUNCTION_EXISTS(&lt;function&gt; &lt;variable&gt;) </p>
<p> Check that the &lt;function&gt; is provided by libraries on the system and store the result in a &lt;variable&gt;. This does not verify that any system header file declares the function, only that it can be found at link time (consider using CheckSymbolExists). &lt;variable&gt; will be created as an internal cache variable. </p>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>CMAKE_REQUIRED_FLAGS = string of compile command line flags
CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
CMAKE_REQUIRED_INCLUDES = list of include directories
CMAKE_REQUIRED_LIBRARIES = list of libraries to link
CMAKE_REQUIRED_QUIET = execute quietly without messages</pre>
<h3>CheckIncludeFileCXX</h3>
<p>Provides a macro to check if a header file can be included in <code>CXX</code>.</p>
<dl>
<dt><code>CHECK_INCLUDE_FILE_CXX</code></p>
<dd>
<pre>CHECK_INCLUDE_FILE_CXX(&lt;include&gt; &lt;variable&gt; [&lt;flags&gt;])</pre>
<p>Check if the given <code>&lt;include&gt;</code> file may be included in a <code>CXX</code> source file and store the result in an internal cache entry named <code>&lt;variable&gt;</code>. The optional third argument may be used to add compilation flags to the check (or use <code>CMAKE_REQUIRED_FLAGS</code> below). </p>
<p> The following variables may be set before calling this macro to modify the way the check is run:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>string of compile command line flags</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>list of macros to define (-DFOO=bar)</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>list of include directories</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>execute quietly without messages </p>
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
<dd>string of compile command line flags</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>list of macros to define (-DFOO=bar)</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>list of include directories</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>execute quietly without messages </p>
<p> See the <code>CheckIncludeFiles</code> module to check for multiple headers at once. See the <code>CheckIncludeFileCXX</code> module to check for headers using the <code>CXX</code> language.</dl>
<h3>CheckIncludeFiles</h3>
<p>Provides a macro to check if a list of one or more header files can be included together in <code>C</code>.</p>
<dl>
<dt><code>CHECK_INCLUDE_FILES</code></p>
<dd>
<pre>CHECK_INCLUDE_FILES(&quot;&lt;includes&gt;&quot; &lt;variable&gt;)</pre>
<p>Check if the given <code>&lt;includes&gt;</code> list may be included together in a <code>C</code> source file and store the result in an internal cache entry named <code>&lt;variable&gt;</code>. Specify the <code>&lt;includes&gt;</code> argument as a <i>;-list</i> of header file names. </p>
<p> The following variables may be set before calling this macro to modify the way the check is run:</p>
<dt><code>CMAKE_REQUIRED_FLAGS</code></p>
<dd>string of compile command line flags</p>
<dt><code>CMAKE_REQUIRED_DEFINITIONS</code></p>
<dd>list of macros to define (-DFOO=bar)</p>
<dt><code>CMAKE_REQUIRED_INCLUDES</code></p>
<dd>list of include directories</p>
<dt><code>CMAKE_REQUIRED_QUIET</code></p>
<dd>execute quietly without messages </p>
<p> See modules <code>CheckIncludeFile</code> and <code>CheckIncludeFileCXX</code> to check for a single header file in <code>C</code> or <code>CXX</code> languages.</dl>
<h3>CheckLanguage</h3>
<p>Check if a language can be enabled </p>
<p> Usage: </p>
<pre>check_language(&lt;lang&gt;)</pre>
<p>where &lt;lang&gt; is a language that may be passed to enable_language() such as &quot;Fortran&quot;. If CMAKE_&lt;lang&gt;_COMPILER is already defined the check does nothing. Otherwise it tries enabling the language in a test project. The result is cached in CMAKE_&lt;lang&gt;_COMPILER as the compiler that was found, or NOTFOUND if the language cannot be enabled. </p>
<p> Example: </p>
<pre>check_language(Fortran)
if(CMAKE_Fortran_COMPILER)
 enable_language(Fortran)
else()
 message(STATUS &quot;No Fortran support&quot;)
endif()</pre>
<h3>CheckLibraryExists</h3>
<p>Check if the function exists. </p>
<p> CHECK_LIBRARY_EXISTS (LIBRARY FUNCTION LOCATION VARIABLE) </p>
<pre>LIBRARY - the name of the library you are looking for
FUNCTION - the name of the function
LOCATION - location where the library should be found
VARIABLE - variable to store the result
 Will be created as an internal cache variable.</pre>
<p>The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>CMAKE_REQUIRED_FLAGS = string of compile command line flags
CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
CMAKE_REQUIRED_LIBRARIES = list of libraries to link
CMAKE_REQUIRED_QUIET = execute quietly without messages</pre>
<h3>CheckPrototypeDefinition</h3>
<p>Check if the protoype we expect is correct. </p>
<p> check_prototype_definition(FUNCTION PROTOTYPE RETURN HEADER VARIABLE) </p>
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
<p>The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>CMAKE_REQUIRED_FLAGS = string of compile command line flags
CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
CMAKE_REQUIRED_INCLUDES = list of include directories
CMAKE_REQUIRED_LIBRARIES = list of libraries to link
CMAKE_REQUIRED_QUIET = execute quietly without messages</pre>
<h3>CheckStructHasMember</h3>
<p>Check if the given struct or class has the specified member variable </p>
<pre>CHECK_STRUCT_HAS_MEMBER(&lt;struct&gt; &lt;member&gt; &lt;header&gt; &lt;variable&gt;
 [LANGUAGE &lt;language&gt;])</pre>
<pre>&lt;struct&gt; - the name of the struct or class you are interested in
&lt;member&gt; - the member which existence you want to check
&lt;header&gt; - the header(s) where the prototype should be declared
&lt;variable&gt; - variable to store the result
&lt;language&gt; - the compiler to use (C or CXX)</pre>
<p>The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>CMAKE_REQUIRED_FLAGS = string of compile command line flags
CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
CMAKE_REQUIRED_INCLUDES = list of include directories
CMAKE_REQUIRED_LIBRARIES = list of libraries to link
CMAKE_REQUIRED_QUIET = execute quietly without messages</pre>
<p>Example: CHECK_STRUCT_HAS_MEMBER(&quot;struct timeval&quot; tv_sec sys/select.h HAVE_TIMEVAL_TV_SEC LANGUAGE C)</p>
<h3>CheckSymbolExists</h3>
<p>Check if a symbol exists as a function, variable, or macro </p>
<p> CHECK_SYMBOL_EXISTS(&lt;symbol&gt; &lt;files&gt; &lt;variable&gt;) </p>
<p> Check that the &lt;symbol&gt; is available after including given header &lt;files&gt; and store the result in a &lt;variable&gt;. Specify the list of files in one argument as a semicolon-separated list. &lt;variable&gt; will be created as an internal cache variable. </p>
<p> If the header files define the symbol as a macro it is considered available and assumed to work. If the header files declare the symbol as a function or variable then the symbol must also be available for linking. If the symbol is a type or enum value it will not be recognized (consider using CheckTypeSize or CheckCSourceCompiles). If the check needs to be done in C++, consider using CHECK_CXX_SYMBOL_EXISTS(), which does the same as CHECK_SYMBOL_EXISTS(), but in C++. </p>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>CMAKE_REQUIRED_FLAGS = string of compile command line flags
CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
CMAKE_REQUIRED_INCLUDES = list of include directories
CMAKE_REQUIRED_LIBRARIES = list of libraries to link
CMAKE_REQUIRED_QUIET = execute quietly without messages</pre>
<h3>CheckTypeSize</h3>
<p>Check sizeof a type </p>
<pre>CHECK_TYPE_SIZE(TYPE VARIABLE [BUILTIN_TYPES_ONLY]
 [LANGUAGE &lt;language&gt;])</pre>
<p>Check if the type exists and determine its size. On return, &quot;HAVE_${VARIABLE}&quot; holds the existence of the type, and &quot;${VARIABLE}&quot; holds one of the following: </p>
<pre>&lt;size&gt; = type has non-zero size &lt;size&gt;
&quot;0&quot; = type has arch-dependent size (see below)
&quot;&quot; = type does not exist</pre>
<p>Both <code>HAVE_${VARIABLE}</code> and <code>${VARIABLE}</code> will be created as internal cache variables. </p>
<p> Furthermore, the variable &quot;${VARIABLE}_CODE&quot; holds C preprocessor code to define the macro &quot;${VARIABLE}&quot; to the size of the type, or leave the macro undefined if the type does not exist. </p>
<p> The variable &quot;${VARIABLE}&quot; may be &quot;0&quot; when CMAKE_OSX_ARCHITECTURES has multiple architectures for building OS X universal binaries. This indicates that the type size varies across architectures. In this case &quot;${VARIABLE}_CODE&quot; contains C preprocessor tests mapping from each architecture macro to the corresponding type size. The list of architecture macros is stored in &quot;${VARIABLE}_KEYS&quot;, and the value for each key is stored in &quot;${VARIABLE}-${KEY}&quot;. </p>
<p> If the BUILTIN_TYPES_ONLY option is not given, the macro checks for headers &lt;sys/types.h&gt;, &lt;stdint.h&gt;, and &lt;stddef.h&gt;, and saves results in HAVE_SYS_TYPES_H, HAVE_STDINT_H, and HAVE_STDDEF_H. The type size check automatically includes the available headers, thus supporting checks of types defined in the headers. </p>
<p> If LANGUAGE is set, the specified compiler will be used to perform the check. Acceptable values are C and CXX </p>
<p> Despite the name of the macro you may use it to check the size of more complex expressions, too. To check e.g. for the size of a struct member you can do something like this: </p>
<pre>check_type_size(&quot;((struct something*)0)-&gt;member&quot; SIZEOF_MEMBER)</pre>
<p>The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>CMAKE_REQUIRED_FLAGS = string of compile command line flags
CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
CMAKE_REQUIRED_INCLUDES = list of include directories
CMAKE_REQUIRED_LIBRARIES = list of libraries to link
CMAKE_REQUIRED_QUIET = execute quietly without messages
CMAKE_EXTRA_INCLUDE_FILES = list of extra headers to include</pre>
<h3>CheckVariableExists</h3>
<p>Check if the variable exists. </p>
<pre>CHECK_VARIABLE_EXISTS(VAR VARIABLE)</pre>
<pre>VAR - the name of the variable
VARIABLE - variable to store the result
 Will be created as an internal cache variable.</pre>
<p>This macro is only for C variables. </p>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>CMAKE_REQUIRED_FLAGS = string of compile command line flags
CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
CMAKE_REQUIRED_LIBRARIES = list of libraries to link
CMAKE_REQUIRED_QUIET = execute quietly without messages</pre>
<h3>CMakeAddFortranSubdirectory</h3>
<p>Use MinGW gfortran from VS if a fortran compiler is not found. </p>
<p> The &#8216;add_fortran_subdirectory&#8217; function adds a subdirectory to a project that contains a fortran only sub-project. The module will check the current compiler and see if it can support fortran. If no fortran compiler is found and the compiler is MSVC, then this module will find the MinGW gfortran. It will then use an external project to build with the MinGW tools. It will also create imported targets for the libraries created. This will only work if the fortran code is built into a dll, so BUILD_SHARED_LIBS is turned on in the project. In addition the CMAKE_GNUtoMS option is set to on, so that the MS .lib files are created. Usage is as follows: </p>
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
<p>Relative paths in ARCHIVE_DIR and RUNTIME_DIR are interpreted with respect to the build directory corresponding to the source directory in which the function is invoked. </p>
<p> Limitations: </p>
<p> NO_EXTERNAL_INSTALL is required for forward compatibility with a future version that supports installation of the external project binaries during &quot;make install&quot;.</p>
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
<p> This macro presents an option to the user only if a set of other conditions are true. When the option is not presented a default value is used, but any value set by the user is preserved for when the option is presented again. Example invocation: </p>
<pre>CMAKE_DEPENDENT_OPTION(USE_FOO &quot;Use Foo&quot; ON
 &quot;USE_BAR;NOT USE_ZOT&quot; OFF)</pre>
<p>If USE_BAR is true and USE_ZOT is false, this provides an option called USE_FOO that defaults to ON. Otherwise, it sets USE_FOO to OFF. If the status of USE_BAR or USE_ZOT ever changes, any value for the USE_FOO option is saved so that when the option is re-enabled it retains its old value.</p>
<h3>CMakeDetermineVSServicePack</h3>
<p>Deprecated. Do not use. </p>
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
<p>Deprecated. Do not use. </p>
<p> This module was once needed to expand imported targets to the underlying libraries they reference on disk for use with the <code>try_compile()</code> and <code>try_run()</code> commands. These commands now support imported libraries in their <code>LINK_LIBRARIES</code> options (since CMake 2.8.11 for <code>try_compile()</code> and since CMake 3.2 for <code>try_run()</code>). </p>
<p> This module does not support the policy <code>CMP0022</code> <code>NEW</code> behavior or use of the <code>INTERFACE_LINK_LIBRARIES</code> property because <code>generator expressions</code> cannot be evaluated during configuration. </p>
<pre>CMAKE_EXPAND_IMPORTED_TARGETS(&lt;var&gt; LIBRARIES lib1 lib2...libN
 [CONFIGURATION &lt;config&gt;])</pre>
<p>CMAKE_EXPAND_IMPORTED_TARGETS() takes a list of libraries and replaces all imported targets contained in this list with their actual file paths of the referenced libraries on disk, including the libraries from their link interfaces. If a CONFIGURATION is given, it uses the respective configuration of the imported targets if it exists. If no CONFIGURATION is given, it uses the first configuration from ${CMAKE_CONFIGURATION_TYPES} if set, otherwise ${CMAKE_BUILD_TYPE}. </p>
<pre>cmake_expand_imported_targets(expandedLibs
 LIBRARIES ${CMAKE_REQUIRED_LIBRARIES}
 CONFIGURATION &quot;${CMAKE_TRY_COMPILE_CONFIGURATION}&quot; )</pre>
<h3>CMakeFindDependencyMacro</h3>
<pre>find_dependency(&lt;dep&gt; [&lt;version&gt; [EXACT]])</pre>
<p><code>find_dependency()</code> wraps a <code>find_package()</code> call for a package dependency. It is designed to be used in a &lt;package&gt;Config.cmake file, and it forwards the correct parameters for EXACT, QUIET and REQUIRED which were passed to the original <code>find_package()</code> call. It also sets an informative diagnostic message if the dependency could not be found.</p>
<h3>CMakeFindFrameworks</h3>
<p>helper module to find OSX frameworks</p>
<h3>CMakeFindPackageMode</h3>
<p>This file is executed by cmake when invoked with &#8211;find-package. It expects that the following variables are set using -D:</p>
<dl>
<dt><code>NAME</code></p>
<dd>name of the package</p>
<dt><code>COMPILER_ID</code></p>
<dd>the CMake compiler ID for which the result is, i.e. GNU/Intel/Clang/MSVC, etc.</p>
<dt><code>LANGUAGE</code></p>
<dd>language for which the result will be used, i.e. C/CXX/Fortan/ASM</p>
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
<h3>CMakeForceCompiler</h3>
<p>Deprecated. Do not use. </p>
<p> The macros provided by this module were once intended for use by cross-compiling toolchain files when CMake was not able to automatically detect the compiler identification. Since the introduction of this module, CMake&#8217;s compiler identification capabilities have improved and can now be taught to recognize any compiler. Furthermore, the suite of information CMake detects from a compiler is now too extensive to be provided by toolchain files using these macros. </p>
<p> One common use case for this module was to skip CMake&#8217;s checks for a working compiler when using a cross-compiler that cannot link binaries without special flags or custom linker scripts. This case is now supported by setting the <code>CMAKE_TRY_COMPILE_TARGET_TYPE</code> variable in the toolchain file instead. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<p> Macro CMAKE_FORCE_C_COMPILER has the following signature: </p>
<pre>CMAKE_FORCE_C_COMPILER(&lt;compiler&gt; &lt;compiler-id&gt;)</pre>
<p>It sets CMAKE_C_COMPILER to the given compiler and the cmake internal variable CMAKE_C_COMPILER_ID to the given compiler-id. It also bypasses the check for working compiler and basic compiler information tests. </p>
<p> Macro CMAKE_FORCE_CXX_COMPILER has the following signature: </p>
<pre>CMAKE_FORCE_CXX_COMPILER(&lt;compiler&gt; &lt;compiler-id&gt;)</pre>
<p>It sets CMAKE_CXX_COMPILER to the given compiler and the cmake internal variable CMAKE_CXX_COMPILER_ID to the given compiler-id. It also bypasses the check for working compiler and basic compiler information tests. </p>
<p> Macro CMAKE_FORCE_Fortran_COMPILER has the following signature: </p>
<pre>CMAKE_FORCE_Fortran_COMPILER(&lt;compiler&gt; &lt;compiler-id&gt;)</pre>
<p>It sets CMAKE_Fortran_COMPILER to the given compiler and the cmake internal variable CMAKE_Fortran_COMPILER_ID to the given compiler-id. It also bypasses the check for working compiler and basic compiler information tests. </p>
<p> So a simple toolchain file could look like this: </p>
<pre>include (CMakeForceCompiler)
set(CMAKE_SYSTEM_NAME Generic)
CMAKE_FORCE_C_COMPILER (chc12 MetrowerksHicross)
CMAKE_FORCE_CXX_COMPILER (chc12 MetrowerksHicross)</pre>
<h3>CMakeGraphVizOptions</h3>
<p>The builtin graphviz support of CMake.</p>
<h3>Variables specific to the graphviz support</h3>
<p>CMake can generate graphviz files, showing the dependencies between the targets in a project and also external libraries which are linked against. When CMake is run with the &#8211;graphviz=foo option, it will produce</p>
<dl>
<dt>&bull;</p>
<dd>a foo.dot file showing all dependencies in the project</p>
<dt>&bull;</p>
<dd>a foo.dot.&lt;target&gt; file for each target, file showing on which other targets the respective target depends</p>
<dt>&bull;</p>
<dd>a foo.dot.&lt;target&gt;.dependers file, showing which other targets depend on the respective target </p>
<p> This can result in huge graphs. Using the file CMakeGraphVizOptions.cmake the look and content of the generated graphs can be influenced. This file is searched first in ${CMAKE_BINARY_DIR} and then in ${CMAKE_SOURCE_DIR}. If found, it is read and the variables set in it are used to adjust options for the generated graphviz files.</p>
<dt><code>GRAPHVIZ_GRAPH_TYPE</code></p>
<dd>The graph type</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &quot;digraph&quot;</p>
<dt><code>GRAPHVIZ_GRAPH_NAME</code></p>
<dd>The graph name.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &quot;GG&quot;</p>
<dt><code>GRAPHVIZ_GRAPH_HEADER</code></p>
<dd>The header written at the top of the graphviz file.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &quot;node [n fontsize = &quot;12&quot;];&quot;</p>
<dt><code>GRAPHVIZ_NODE_PREFIX</code></p>
<dd>The prefix for each node in the graphviz file.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &quot;node&quot;</p>
<dt><code>GRAPHVIZ_EXECUTABLES</code></p>
<dd>Set this to FALSE to exclude executables from the generated graphs.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : TRUE</p>
<dt><code>GRAPHVIZ_STATIC_LIBS</code></p>
<dd>Set this to FALSE to exclude static libraries from the generated graphs.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : TRUE</p>
<dt><code>GRAPHVIZ_SHARED_LIBS</code></p>
<dd>Set this to FALSE to exclude shared libraries from the generated graphs.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : TRUE</p>
<dt><code>GRAPHVIZ_MODULE_LIBS</code></p>
<dd>Set this to FALSE to exclude module libraries from the generated graphs.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : TRUE</p>
<dt><code>GRAPHVIZ_EXTERNAL_LIBS</code></p>
<dd>Set this to FALSE to exclude external libraries from the generated graphs.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : TRUE</p>
<dt><code>GRAPHVIZ_IGNORE_TARGETS</code></p>
<dd>A list of regular expressions for ignoring targets.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : empty</p>
<dt><code>GRAPHVIZ_GENERATE_PER_TARGET</code></p>
<dd>Set this to FALSE to exclude per target graphs <code>foo.dot.&lt;target&gt;</code>.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : TRUE</p>
<dt><code>GRAPHVIZ_GENERATE_DEPENDERS</code></p>
<dd>Set this to FALSE to exclude depender graphs <code>foo.dot.&lt;target&gt;.dependers</code>.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : TRUE</dl>
<h3>CMakePackageConfigHelpers</h3>
<p>Helpers functions for creating config files that can be included by other projects to find and use a package. </p>
<p> Adds the <code>configure_package_config_file()</code> and <code>write_basic_package_version_file()</code> commands.</p>
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
<p><code>configure_package_config_file()</code> should be used instead of the plain <code>configure_file()</code> command when creating the <code>&lt;Name&gt;Config.cmake</code> or <code>&lt;Name&gt;-config.cmake</code> file for installing a project or library. It helps making the resulting package relocatable by avoiding hardcoded paths in the installed <code>Config.cmake</code> file. </p>
<p> In a <code>FooConfig.cmake</code> file there may be code like this to make the install destinations know to the using project: </p>
<pre>set(FOO_INCLUDE_DIR &quot;@CMAKE_INSTALL_FULL_INCLUDEDIR@&quot; )
set(FOO_DATA_DIR &quot;@CMAKE_INSTALL_PREFIX@/@RELATIVE_DATA_INSTALL_DIR@&quot; )
set(FOO_ICONS_DIR &quot;@CMAKE_INSTALL_PREFIX@/share/icons&quot; )
...logic to determine installedPrefix from the own location...
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
<p> If the <code>INSTALL_PREFIX</code> argument is passed, this is used as base path to calculate all the relative paths. The <code>&lt;path&gt;</code> argument must be an absolute path. If this argument is not passed, the <code>CMAKE_INSTALL_PREFIX</code> variable will be used instead. The default value is good when generating a FooConfig.cmake file to use your package from the install tree. When generating a FooConfig.cmake file to use your package from the build tree this option should be used. </p>
<p> By default <code>configure_package_config_file</code> also generates two helper macros, <code>set_and_check()</code> and <code>check_required_components()</code> into the <code>FooConfig.cmake</code> file. </p>
<p> <code>set_and_check()</code> should be used instead of the normal <code>set()</code> command for setting directories and file locations. Additionally to setting the variable it also checks that the referenced file or directory actually exists and fails with a <code>FATAL_ERROR</code> otherwise. This makes sure that the created <code>FooConfig.cmake</code> file does not contain wrong references. When using the <code>NO_SET_AND_CHECK_MACRO</code>, this macro is not generated into the <code>FooConfig.cmake</code> file. </p>
<p> <code>check_required_components(&lt;package_name&gt;)</code> should be called at the end of the <code>FooConfig.cmake</code> file if the package supports components. This macro checks whether all requested, non-optional components have been found, and if this is not the case, sets the <code>Foo_FOUND</code> variable to <code>FALSE</code>, so that the package is considered to be not found. It does that by testing the <code>Foo_&lt;Component&gt;_FOUND</code> variables for all requested required components. When using the <code>NO_CHECK_REQUIRED_COMPONENTS_MACRO</code> option, this macro is not generated into the <code>FooConfig.cmake</code> file. </p>
<p> For an example see below the documentation for <code>write_basic_package_version_file()</code>.</dl>
<h3>Generating a Package Version File</h3>
<dl>
<dt><code>write_basic_package_version_file</code></p>
<dd>Create a version file for a project: </p>
<pre>write_basic_package_version_file(&lt;filename&gt;
 [VERSION &lt;major.minor.patch&gt;]
 COMPATIBILITY &lt;AnyNewerVersion|SameMajorVersion|ExactVersion&gt; )</pre>
<p>Writes a file for use as <code>&lt;package&gt;ConfigVersion.cmake</code> file to <code>&lt;filename&gt;</code>. See the documentation of <code>find_package()</code> for details on this. </p>
<p> <code>&lt;filename&gt;</code> is the output filename, it should be in the build tree. <code>&lt;major.minor.patch&gt;</code> is the version number of the project to be installed. </p>
<p> If no <code>VERSION</code> is given, the <code>PROJECT_VERSION</code> variable is used. If this hasn&#8217;t been set, it errors out. </p>
<p> The <code>COMPATIBILITY</code> mode <code>AnyNewerVersion</code> means that the installed package version will be considered compatible if it is newer or exactly the same as the requested version. This mode should be used for packages which are fully backward compatible, also across major versions. If <code>SameMajorVersion</code> is used instead, then the behaviour differs from <code>AnyNewerVersion</code> in that the major version number must be the same as requested, e.g. version 2.0 will not be considered compatible if 1.0 is requested. This mode should be used for packages which guarantee backward compatibility within the same major version. If <code>ExactVersion</code> is used, then the package is only considered compatible if the requested version matches exactly its own version number (not considering the tweak version). For example, version 1.2.3 of a package is only considered compatible to requested version 1.2.3. This mode is for packages without compatibility guarantees. If your project has more elaborated version matching rules, you will need to write your own custom <code>ConfigVersion.cmake</code> file instead of using this macro. </p>
<p> Internally, this macro executes <code>configure_file()</code> to create the resulting version file. Depending on the <code>COMPATIBLITY</code>, either the file <code>BasicConfigVersion-SameMajorVersion.cmake.in</code> or <code>BasicConfigVersion-AnyNewerVersion.cmake.in</code> is used. Please note that these two files are internal to CMake and you should not call <code>configure_file()</code> on them yourself, but they can be used as starting point to create more sophisticted custom <code>ConfigVersion.cmake</code> files.</dl>
<h3>Example Generating Package Files</h3>
<p>Example using both <code>configure_package_config_file()</code> and <code>write_basic_package_version_file()</code>: </p>
<p> <code>CMakeLists.txt</code>: </p>
<pre>set(INCLUDE_INSTALL_DIR include/ ... CACHE )
set(LIB_INSTALL_DIR lib/ ... CACHE )
set(SYSCONFIG_INSTALL_DIR etc/foo/ ... CACHE )
...
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
<h3>CMakeParseArguments</h3>
<p>This module once implemented the <code>cmake_parse_arguments()</code> command that is now implemented natively by CMake. It is now an empty placeholder for compatibility with projects that include it to get the command from CMake 3.4 and lower.</p>
<h3>CMakePrintHelpers</h3>
<p>Convenience macros for printing properties and variables, useful e.g. for debugging. </p>
<pre>CMAKE_PRINT_PROPERTIES([TARGETS target1 .. targetN]
 [SOURCES source1 .. sourceN]
 [DIRECTORIES dir1 .. dirN]
 [TESTS test1 .. testN]
 [CACHE_ENTRIES entry1 .. entryN]
 PROPERTIES prop1 .. propN )</pre>
<p>This macro prints the values of the properties of the given targets, source files, directories, tests or cache entries. Exactly one of the scope keywords must be used. Example: </p>
<pre>cmake_print_properties(TARGETS foo bar PROPERTIES
 LOCATION INTERFACE_INCLUDE_DIRS)</pre>
<p>This will print the LOCATION and INTERFACE_INCLUDE_DIRS properties for both targets foo and bar. </p>
<p> CMAKE_PRINT_VARIABLES(var1 var2 .. varN) </p>
<p> This macro will print the name of each variable followed by its value. Example: </p>
<pre>cmake_print_variables(CMAKE_C_COMPILER CMAKE_MAJOR_VERSION DOES_NOT_EXIST)</pre>
<p>Gives: </p>
<pre>-- CMAKE_C_COMPILER=&quot;/usr/bin/gcc&quot; ; CMAKE_MAJOR_VERSION=&quot;2&quot; ; DOES_NOT_EXIST=&quot;&quot;</pre>
<h3>CMakePrintSystemInformation</h3>
<p>print system information </p>
<p> This file can be used for diagnostic purposes just include it in a project to see various internal CMake variables.</p>
<h3>CMakePushCheckState</h3>
<p>This module defines three macros: CMAKE_PUSH_CHECK_STATE() CMAKE_POP_CHECK_STATE() and CMAKE_RESET_CHECK_STATE() These macros can be used to save, restore and reset (i.e., clear contents) the state of the variables CMAKE_REQUIRED_FLAGS, CMAKE_REQUIRED_DEFINITIONS, CMAKE_REQUIRED_LIBRARIES, CMAKE_REQUIRED_INCLUDES and CMAKE_EXTRA_INCLUDE_FILES used by the various Check-files coming with CMake, like e.g. check_function_exists() etc. The variable contents are pushed on a stack, pushing multiple times is supported. This is useful e.g. when executing such tests in a Find-module, where they have to be set, but after the Find-module has been executed they should have the same value as they had before. </p>
<p> CMAKE_PUSH_CHECK_STATE() macro receives optional argument RESET. Whether it&#8217;s specified, CMAKE_PUSH_CHECK_STATE() will set all CMAKE_REQUIRED_* variables to empty values, same as CMAKE_RESET_CHECK_STATE() call will do. </p>
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
<h3>CPackBundle</h3>
<p>CPack Bundle generator (Mac OS X) specific options</p>
<h3>Variables specific to CPack Bundle generator</h3>
<p>Installers built on Mac OS X using the Bundle generator use the aforementioned DragNDrop (CPACK_DMG_xxx) variables, plus the following Bundle-specific parameters (CPACK_BUNDLE_xxx).</p>
<dl>
<dt><code>CPACK_BUNDLE_NAME</code></p>
<dd>The name of the generated bundle. This appears in the OSX finder as the bundle name. Required.</p>
<dt><code>CPACK_BUNDLE_PLIST</code></p>
<dd>Path to an OSX plist file that will be used for the generated bundle. This assumes that the caller has generated or specified their own Info.plist file. Required.</p>
<dt><code>CPACK_BUNDLE_ICON</code></p>
<dd>Path to an OSX icon file that will be used as the icon for the generated bundle. This is the icon that appears in the OSX finder for the bundle, and in the OSX dock when the bundle is opened. Required.</p>
<dt><code>CPACK_BUNDLE_STARTUP_COMMAND</code></p>
<dd>Path to a startup script. This is a path to an executable or script that will be run whenever an end-user double-clicks the generated bundle in the OSX Finder. Optional.</p>
<dt><code>CPACK_BUNDLE_APPLE_CERT_APP</code></p>
<dd>The name of your Apple supplied code signing certificate for the application. The name usually takes the form &quot;Developer ID Application: [Name]&quot; or &quot;3rd Party Mac Developer Application: [Name]&quot;. If this variable is not set the application will not be signed.</p>
<dt><code>CPACK_BUNDLE_APPLE_ENTITLEMENTS</code></p>
<dd>The name of the plist file that contains your apple entitlements for sandboxing your application. This file is required for submission to the Mac App Store.</p>
<dt><code>CPACK_BUNDLE_APPLE_CODESIGN_FILES</code></p>
<dd>A list of additional files that you wish to be signed. You do not need to list the main application folder, or the main executable. You should list any frameworks and plugins that are included in your app bundle.</p>
<dt><code>CPACK_BUNDLE_APPLE_CODESIGN_PARAMETER</code></p>
<dd>Additional parameter that will passed to codesign. Default value: &quot;&#8211;deep -f&quot;</p>
<dt><code>CPACK_COMMAND_CODESIGN</code></p>
<dd>Path to the <a href="/docs/linux/man/1-codesign/">codesign</a>(1) command used to sign applications with an Apple cert. This variable can be used to override the automatically detected command (or specify its location if the auto-detection fails to find it.)</dl>
<h3>CPackComponent</h3>
<p>Build binary and source package installers</p>
<h3>Variables concerning CPack Components</h3>
<p>The CPackComponent module is the module which handles the component part of CPack. See CPack module for general information about CPack. </p>
<p> For certain kinds of binary installers (including the graphical installers on Mac OS X and Windows), CPack generates installers that allow users to select individual application components to install. The contents of each of the components are identified by the COMPONENT argument of CMake&#8217;s INSTALL command. These components can be annotated with user-friendly names and descriptions, inter-component dependencies, etc., and grouped in various ways to customize the resulting installer. See the cpack_add_* commands, described below, for more information about component-specific installations. </p>
<p> Component-specific installation allows users to select specific sets of components to install during the install process. Installation components are identified by the COMPONENT argument of CMake&#8217;s INSTALL commands, and should be further described by the following CPack commands:</p>
<dl>
<dt><code>CPACK_COMPONENTS_ALL</code></p>
<dd>The list of component to install. </p>
<p> The default value of this variable is computed by CPack and contains all components defined by the project. The user may set it to only include the specified components.</p>
<dt><code>CPACK_&lt;GENNAME&gt;_COMPONENT_INSTALL</code></p>
<dd>Enable/Disable component install for CPack generator &lt;GENNAME&gt;. </p>
<p> Each CPack Generator (RPM, DEB, ARCHIVE, NSIS, DMG, etc&#8230;) has a legacy default behavior. e.g. RPM builds monolithic whereas NSIS builds component. One can change the default behavior by setting this variable to 0/1 or OFF/ON.</p>
<dt><code>CPACK_COMPONENTS_GROUPING</code></p>
<dd>Specify how components are grouped for multi-package component-aware CPack generators. </p>
<p> Some generators like RPM or ARCHIVE family (TGZ, ZIP, &#8230;) generates several packages files when asked for component packaging. They group the component differently depending on the value of this variable:</p>
<dt>&bull;</p>
<dd>ONE_PER_GROUP (default): creates one package file per component group</p>
<dt>&bull;</p>
<dd>ALL_COMPONENTS_IN_ONE : creates a single package with all (requested) component</p>
<dt>&bull;</p>
<dd>IGNORE : creates one package per component, i.e. IGNORE component group </p>
<p> One can specify different grouping for different CPack generator by using a CPACK_PROJECT_CONFIG_FILE.</p>
<dt><code>CPACK_COMPONENT_&lt;compName&gt;_DISPLAY_NAME</code></p>
<dd>The name to be displayed for a component.</p>
<dt><code>CPACK_COMPONENT_&lt;compName&gt;_DESCRIPTION</code></p>
<dd>The description of a component.</p>
<dt><code>CPACK_COMPONENT_&lt;compName&gt;_GROUP</code></p>
<dd>The group of a component.</p>
<dt><code>CPACK_COMPONENT_&lt;compName&gt;_DEPENDS</code></p>
<dd>The dependencies (list of components) on which this component depends.</p>
<dt><code>CPACK_COMPONENT_&lt;compName&gt;_REQUIRED</code></p>
<dd>True is this component is required.</p>
<dt><code>cpack_add_component</code></p>
<dd>Describes a CPack installation component named by the COMPONENT argument to a CMake INSTALL command. </p>
<pre>cpack_add_component(compname
 [DISPLAY_NAME name]
 [DESCRIPTION description]
 [HIDDEN | REQUIRED | DISABLED ]
 [GROUP group]
 [DEPENDS comp1 comp2 ... ]
 [INSTALL_TYPES type1 type2 ... ]
 [DOWNLOADED]
 [ARCHIVE_FILE filename])</pre>
<p>The cmake_add_component command describes an installation component, which the user can opt to install or remove as part of the graphical installation process. compname is the name of the component, as provided to the COMPONENT argument of one or more CMake INSTALL commands. </p>
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
<p> ARCHIVE_FILE provides a name for the archive file created by CPack to be used for downloaded components. If not supplied, CPack will create a file with some name based on CPACK_PACKAGE_FILE_NAME and the name of the component. See cpack_configure_downloads for more information.</p>
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
<p> BOLD_TITLE indicates that the group title should appear in bold, to call the user&#8217;s attention to the group.</p>
<dt><code>cpack_add_install_type</code></p>
<dd>Add a new installation type containing a set of predefined component selections to the graphical installer. </p>
<pre>cpack_add_install_type(typename
 [DISPLAY_NAME name])</pre>
<p>The cpack_add_install_type command identifies a set of preselected components that represents a common use case for an application. For example, a &quot;Developer&quot; install type might include an application along with its header and library files, while an &quot;End user&quot; install type might just include the application&#8217;s executable. Each component identifies itself with one or more install types via the INSTALL_TYPES argument to cpack_add_component. </p>
<p> DISPLAY_NAME is the displayed name of the install type, which will typically show up in a drop-down box within a graphical installer. This value can be any string.</p>
<dt><code>cpack_configure_downloads</code></p>
<dd>Configure CPack to download selected components on-the-fly as part of the installation process. </p>
<pre>cpack_configure_downloads(site
 [UPLOAD_DIRECTORY dirname]
 [ALL]
 [ADD_REMOVE|NO_ADD_REMOVE])</pre>
<p>The cpack_configure_downloads command configures installation-time downloads of selected components. For each downloadable component, CPack will create an archive containing the contents of that component, which should be uploaded to the given site. When the user selects that component for installation, the installer will download and extract the component in place. This feature is useful for creating small installers that only download the requested components, saving bandwidth. Additionally, the installers are small enough that they will be installed as part of the normal installation process, and the &quot;Change&quot; button in Windows Add/Remove Programs control panel will allow one to add or remove parts of the application after the original installation. On Windows, the downloaded-components functionality requires the ZipDLL plug-in for NSIS, available at: </p>
<pre><a rel="nofollow" href="http://nsis.sourceforge.net/ZipDLL_plug-in">http://nsis.sourceforge.net/ZipDLL_plug-in</a></pre>
<p>On Mac OS X, installers that download components on-the-fly can only be built and installed on system using Mac OS X 10.5 or later. </p>
<p> The site argument is a URL where the archives for downloadable components will reside, e.g., <i><a rel="nofollow" href="https://cmake.org/files/2.6.1/installer/">https://cmake.org/files/2.6.1/installer/</a></i> All of the archives produced by CPack should be uploaded to that location. </p>
<p> UPLOAD_DIRECTORY is the local directory where CPack will create the various archives for each of the components. The contents of this directory should be uploaded to a location accessible by the URL given in the site argument. If omitted, CPack will use the directory CPackUploads inside the CMake binary directory to store the generated archives. </p>
<p> The ALL flag indicates that all components be downloaded. Otherwise, only those components explicitly marked as DOWNLOADED or that have a specified ARCHIVE_FILE will be downloaded. Additionally, the ALL option implies ADD_REMOVE (unless NO_ADD_REMOVE is specified). </p>
<p> ADD_REMOVE indicates that CPack should install a copy of the installer that can be called from Windows&#8217; Add/Remove Programs dialog (via the &quot;Modify&quot; button) to change the set of installed components. NO_ADD_REMOVE turns off this behavior. This option is ignored on Mac OS X.</dl>
<h3>CPackCygwin</h3>
<p>Cygwin CPack generator (Cygwin).</p>
<h3>Variables specific to CPack Cygwin generator</h3>
<p>The following variable is specific to installers build on and/or for Cygwin:</p>
<dl>
<dt><code>CPACK_CYGWIN_PATCH_NUMBER</code></p>
<dd>The Cygwin patch number. FIXME: This documentation is incomplete.</p>
<dt><code>CPACK_CYGWIN_PATCH_FILE</code></p>
<dd>The Cygwin patch file. FIXME: This documentation is incomplete.</p>
<dt><code>CPACK_CYGWIN_BUILD_SCRIPT</code></p>
<dd>The Cygwin build script. FIXME: This documentation is incomplete.</dl>
<h3>CPackDeb</h3>
<p>The built in (binary) CPack Deb generator (Unix only)</p>
<h3>Variables specific to CPack Debian (DEB) generator</h3>
<p>CPackDeb may be used to create Deb package using <code>CPack</code>. CPackDeb is a <code>CPack</code> generator thus it uses the <code>CPACK_XXX</code> variables used by <code>CPack</code>. </p>
<p> CPackDeb generator should work on any Linux host but it will produce better deb package when Debian specific tools <code>dpkg-xxx</code> are usable on the build system. </p>
<p> CPackDeb has specific features which are controlled by the specifics <code>CPACK_DEBIAN_XXX</code> variables. </p>
<p> <code>CPACK_DEBIAN_&lt;COMPONENT&gt;_XXXX</code> variables may be used in order to have <code>component</code> specific values. Note however that <code>&lt;COMPONENT&gt;</code> refers to the <code>grouping name</code> written in upper case. It may be either a component name or a component GROUP name. </p>
<p> Here are some CPackDeb wiki resources that are here for historic reasons and are no longer maintained but may still prove useful:</p>
<dl>
<dt>&bull;</p>
<dd><i><a rel="nofollow" href="https://cmake.org/Wiki/CMake:CPackConfiguration">https://cmake.org/Wiki/CMake:CPackConfiguration</a></i></p>
<dt>&bull;</p>
<dd><i><a rel="nofollow" href="https://cmake.org/Wiki/CMake:CPackPackageGenerators#DEB_.28UNIX_only.29">https://cmake.org/Wiki/CMake:CPackPackageGenerators#DEB_.28UNIX_only.29</a></i> </p>
<p> List of CPackRPM specific variables:</p>
<dt><code>CPACK_DEB_PACKAGE_COMPONENT</code></p>
<dd>Enable component packaging for CPackRPM</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : OFF </p>
<p> If enabled (ON) multiple packages are generated. By default a single package containing files of all components is generated.</p>
<dt><code>CPACK_DEBIAN_PACKAGE_NAME</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_NAME</code></p>
<dd>Set Package control field (variable is automatically transformed to lower case).</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd><code>CPACK_PACKAGE_NAME</code> for non-component based installations</p>
<dt>&bull;</p>
<dd><code>CPACK_DEBIAN_PACKAGE_NAME</code> suffixed with -&lt;COMPONENT&gt; for component-based installations. </p>
<p> See <i><a rel="nofollow" href="https://www.debian.org/doc/debian-policy/ch-controlfields.html#s-f-Source">https://www.debian.org/doc/debian-policy/ch-controlfields.html#s-f-Source</a></i></p>
<dt><code>CPACK_DEBIAN_FILE_NAME</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_FILE_NAME</code></p>
<dd>Package file name.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : <code>&lt;CPACK_PACKAGE_FILE_NAME&gt;[-&lt;component&gt;].deb</code> </p>
<p> This may be set to <code>DEB-DEFAULT</code> to allow CPackDeb to generate package file name by itself in deb format: </p>
<pre>&lt;PackageName&gt;_&lt;VersionNumber&gt;-&lt;DebianRevisionNumber&gt;_&lt;DebianArchitecture&gt;.deb</pre>
<p>Alternatively provided package file name must end with <code>.deb</code> suffix. </p>
<p> <code>NOTE:</code> Preferred setting of this variable is <code>DEB-DEFAULT</code> but for backward compatibility with CPackDeb in CMake prior to version 3.6 this feature is disabled by default. </p>
<p> <code>NOTE:</code> By using non default filenames duplicate names may occur. Duplicate files get overwritten and it is up to the packager to set the variables in a manner that will prevent such errors.</p>
<dt><code>CPACK_DEBIAN_PACKAGE_VERSION</code></p>
<dd>The Debian package version</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : <code>CPACK_PACKAGE_VERSION</code></p>
<dt><code>CPACK_DEBIAN_PACKAGE_RELEASE</code></p>
<dd>The Debian package release &#8211; Debian revision number.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : 1 </p>
<p> This is the numbering of the DEB package itself, i.e. the version of the packaging and not the version of the content (see <code>CPACK_DEBIAN_PACKAGE_VERSION</code>). One may change the default value if the previous packaging was buggy and/or you want to put here a fancy Linux distro specific numbering.</p>
<dt><code>CPACK_DEBIAN_PACKAGE_ARCHITECTURE</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_ARCHITECTURE</code></p>
<dd>The Debian package architecture</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : Output of <code>dpkg &#8211;print-architecture</code> (or <code>i386</code> if <code>dpkg</code> is not found)</p>
<dt><code>CPACK_DEBIAN_PACKAGE_DEPENDS</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_DEPENDS</code></p>
<dd>Sets the Debian dependencies of this package.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd>An empty string for non-component based installations</p>
<dt>&bull;</p>
<dd><code>CPACK_DEBIAN_PACKAGE_DEPENDS</code> for component-based installations. </p>
<p> <code>NOTE:</code> If <code>CPACK_DEBIAN_PACKAGE_SHLIBDEPS</code> or more specifically <code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_SHLIBDEPS</code> is set for this component, the discovered dependencies will be appended to <code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_DEPENDS</code> instead of <code>CPACK_DEBIAN_PACKAGE_DEPENDS</code>. If <code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_DEPENDS</code> is an empty string, only the automatically discovered dependencies will be set for this component. </p>
<p> Example: </p>
<pre>set(CPACK_DEBIAN_PACKAGE_DEPENDS &quot;libc6 (&gt;= 2.3.1-6), libc6 (&lt; 2.4)&quot;)</pre>
<dt><code>CPACK_DEBIAN_ENABLE_COMPONENT_DEPENDS</code></p>
<dd>Sets inter component dependencies if listed with <code>CPACK_COMPONENT_&lt;compName&gt;_DEPENDS</code> variables.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211;</p>
<dt><code>CPACK_DEBIAN_PACKAGE_MAINTAINER</code></p>
<dd>The Debian package maintainer</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : <code>CPACK_PACKAGE_CONTACT</code></p>
<dt><code>CPACK_DEBIAN_PACKAGE_DESCRIPTION</code></p>
<dd>
<dt><code>CPACK_COMPONENT_&lt;COMPONENT&gt;_DESCRIPTION</code></p>
<dd>The Debian package description</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd><code>CPACK_DEBIAN_PACKAGE_DESCRIPTION</code> if set or</p>
<dt>&bull;</p>
<dd><code>CPACK_PACKAGE_DESCRIPTION_SUMMARY</code></p>
<dt><code>CPACK_DEBIAN_PACKAGE_SECTION</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_SECTION</code></p>
<dd>Set Section control field e.g. admin, devel, doc, &#8230;</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : &quot;devel&quot; </p>
<p> See <i><a rel="nofollow" href="https://www.debian.org/doc/debian-policy/ch-archive.html#s-subsections">https://www.debian.org/doc/debian-policy/ch-archive.html#s-subsections</a></i></p>
<dt><code>CPACK_DEBIAN_COMPRESSION_TYPE</code></p>
<dd>The compression used for creating the Debian package.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : &quot;gzip&quot; </p>
<p> Possible values are:</p>
<dt>&bull;</p>
<dd>lzma</p>
<dt>&bull;</p>
<dd>xz</p>
<dt>&bull;</p>
<dd>bzip2</p>
<dt>&bull;</p>
<dd>gzip</p>
<dt><code>CPACK_DEBIAN_PACKAGE_PRIORITY</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_PRIORITY</code></p>
<dd>Set Priority control field e.g. required, important, standard, optional, extra</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : &quot;optional&quot; </p>
<p> See <i><a rel="nofollow" href="https://www.debian.org/doc/debian-policy/ch-archive.html#s-priorities">https://www.debian.org/doc/debian-policy/ch-archive.html#s-priorities</a></i></p>
<dt><code>CPACK_DEBIAN_PACKAGE_HOMEPAGE</code></p>
<dd>The URL of the web site for this package, preferably (when applicable) the site from which the original source can be obtained and any additional upstream documentation or information may be found.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> <code>NOTE:</code> The content of this field is a simple URL without any surrounding characters such as &lt;&gt;.</p>
<dt><code>CPACK_DEBIAN_PACKAGE_SHLIBDEPS</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_SHLIBDEPS</code></p>
<dd>May be set to ON in order to use <code>dpkg-shlibdeps</code> to generate better package dependency list.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd><code>CPACK_DEBIAN_PACKAGE_SHLIBDEPS</code> if set or</p>
<dt>&bull;</p>
<dd>OFF </p>
<p> <code>NOTE:</code> You may need set <code>CMAKE_INSTALL_RPATH</code> to an appropriate value if you use this feature, because if you don&#8217;t <code>dpkg-shlibdeps</code> may fail to find your own shared libs. See <i><a rel="nofollow" href="https://cmake.org/Wiki/CMake_RPATH_handling">https://cmake.org/Wiki/CMake_RPATH_handling</a></i>.</p>
<dt><code>CPACK_DEBIAN_PACKAGE_DEBUG</code></p>
<dd>May be set when invoking cpack in order to trace debug information during CPackDeb run.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211;</p>
<dt><code>CPACK_DEBIAN_PACKAGE_PREDEPENDS</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_PREDEPENDS</code></p>
<dd>Sets the <i>Pre-Depends</i> field of the Debian package. Like <code>Depends</code>, except that it also forces <code>dpkg</code> to complete installation of the packages named before even starting the installation of the package which declares the pre-dependency.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd>An empty string for non-component based installations</p>
<dt>&bull;</p>
<dd><code>CPACK_DEBIAN_PACKAGE_PREDEPENDS</code> for component-based installations. </p>
<p> See <i><a rel="nofollow" href="http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps">http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps</a></i></p>
<dt><code>CPACK_DEBIAN_PACKAGE_ENHANCES</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_ENHANCES</code></p>
<dd>Sets the <i>Enhances</i> field of the Debian package. Similar to <code>Suggests</code> but works in the opposite direction: declares that a package can enhance the functionality of another package.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd>An empty string for non-component based installations</p>
<dt>&bull;</p>
<dd><code>CPACK_DEBIAN_PACKAGE_ENHANCES</code> for component-based installations. </p>
<p> See <i><a rel="nofollow" href="http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps">http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps</a></i></p>
<dt><code>CPACK_DEBIAN_PACKAGE_BREAKS</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_BREAKS</code></p>
<dd>Sets the <i>Breaks</i> field of the Debian package. When a binary package (P) declares that it breaks other packages (B), <code>dpkg</code> will not allow the package (P) which declares <i>Breaks</i> be <code>unpacked</code> unless the packages that will be broken (B) are deconfigured first. As long as the package (P) is configured, the previously deconfigured packages (B) cannot be reconfigured again.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd>An empty string for non-component based installations</p>
<dt>&bull;</p>
<dd><code>CPACK_DEBIAN_PACKAGE_BREAKS</code> for component-based installations. </p>
<p> See <i><a rel="nofollow" href="https://www.debian.org/doc/debian-policy/ch-relationships.html#s-breaks">https://www.debian.org/doc/debian-policy/ch-relationships.html#s-breaks</a></i></p>
<dt><code>CPACK_DEBIAN_PACKAGE_CONFLICTS</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_CONFLICTS</code></p>
<dd>Sets the <i>Conflicts</i> field of the Debian package. When one binary package declares a conflict with another using a <i>Conflicts</i> field, <code>dpkg</code> will not allow them to be unpacked on the system at the same time.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd>An empty string for non-component based installations</p>
<dt>&bull;</p>
<dd><code>CPACK_DEBIAN_PACKAGE_CONFLICTS</code> for component-based installations. </p>
<p> See <i><a rel="nofollow" href="https://www.debian.org/doc/debian-policy/ch-relationships.html#s-conflicts">https://www.debian.org/doc/debian-policy/ch-relationships.html#s-conflicts</a></i> </p>
<p> <code>NOTE:</code> This is a stronger restriction than <code>Breaks</code>, which prevents the broken package from being configured while the breaking package is in the &quot;Unpacked&quot; state but allows both packages to be unpacked at the same time.</p>
<dt><code>CPACK_DEBIAN_PACKAGE_PROVIDES</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_PROVIDES</code></p>
<dd>Sets the <i>Provides</i> field of the Debian package. A virtual package is one which appears in the <i>Provides</i> control field of another package.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd>An empty string for non-component based installations</p>
<dt>&bull;</p>
<dd><code>CPACK_DEBIAN_PACKAGE_PROVIDES</code> for component-based installations. </p>
<p> See <i><a rel="nofollow" href="https://www.debian.org/doc/debian-policy/ch-relationships.html#s-virtual">https://www.debian.org/doc/debian-policy/ch-relationships.html#s-virtual</a></i></p>
<dt><code>CPACK_DEBIAN_PACKAGE_REPLACES</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_REPLACES</code></p>
<dd>Sets the <i>Replaces</i> field of the Debian package. Packages can declare in their control file that they should overwrite files in certain other packages, or completely replace other packages.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd>An empty string for non-component based installations</p>
<dt>&bull;</p>
<dd><code>CPACK_DEBIAN_PACKAGE_REPLACES</code> for component-based installations. </p>
<p> See <i><a rel="nofollow" href="http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps">http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps</a></i></p>
<dt><code>CPACK_DEBIAN_PACKAGE_RECOMMENDS</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_RECOMMENDS</code></p>
<dd>Sets the <i>Recommends</i> field of the Debian package. Allows packages to declare a strong, but not absolute, dependency on other packages.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd>An empty string for non-component based installations</p>
<dt>&bull;</p>
<dd><code>CPACK_DEBIAN_PACKAGE_RECOMMENDS</code> for component-based installations. </p>
<p> See <i><a rel="nofollow" href="http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps">http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps</a></i></p>
<dt><code>CPACK_DEBIAN_PACKAGE_SUGGESTS</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_SUGGESTS</code></p>
<dd>Sets the <i>Suggests</i> field of the Debian package. Allows packages to declare a suggested package install grouping.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd>An empty string for non-component based installations</p>
<dt>&bull;</p>
<dd><code>CPACK_DEBIAN_PACKAGE_SUGGESTS</code> for component-based installations. </p>
<p> See <i><a rel="nofollow" href="http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps">http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps</a></i></p>
<dt><code>CPACK_DEBIAN_PACKAGE_GENERATE_SHLIBS</code></p>
<dd>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : OFF </p>
<p> Allows to generate shlibs control file automatically. Compatibility is defined by <code>CPACK_DEBIAN_PACKAGE_GENERATE_SHLIBS_POLICY</code> variable value. </p>
<p> <code>NOTE:</code> Libraries are only considered if they have both library name and version set. This can be done by setting SOVERSION property with <code>set_target_properties()</code> command.</p>
<dt><code>CPACK_DEBIAN_PACKAGE_GENERATE_SHLIBS_POLICY</code></p>
<dd>Compatibility policy for auto-generated shlibs control file.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &quot;=&quot; </p>
<p> Defines compatibility policy for auto-generated shlibs control file. Possible values: &quot;=&quot;, &quot;&gt;=&quot; </p>
<p> See <i><a rel="nofollow" href="https://www.debian.org/doc/debian-policy/ch-sharedlibs.html#s-sharedlibs-shlibdeps">https://www.debian.org/doc/debian-policy/ch-sharedlibs.html#s-sharedlibs-shlibdeps</a></i></p>
<dt><code>CPACK_DEBIAN_PACKAGE_CONTROL_EXTRA</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_CONTROL_EXTRA</code></p>
<dd>This variable allow advanced user to add custom script to the control.tar.gz. Typical usage is for conffiles, postinst, postrm, prerm.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> Usage: </p>
<pre>set(CPACK_DEBIAN_PACKAGE_CONTROL_EXTRA
 &quot;${CMAKE_CURRENT_SOURCE_DIR/prerm;${CMAKE_CURRENT_SOURCE_DIR}/postrm&quot;)</pre>
<p><code>NOTE:</code> The original permissions of the files will be used in the final package unless the variable <code>CPACK_DEBIAN_PACKAGE_CONTROL_STRICT_PERMISSION</code> is set. In particular, the scripts should have the proper executable flag prior to the generation of the package.</p>
<dt><code>CPACK_DEBIAN_PACKAGE_CONTROL_STRICT_PERMISSION</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_CONTROL_STRICT_PERMISSION</code></p>
<dd>This variable indicates if the Debian policy on control files should be strictly followed.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : FALSE </p>
<p> Usage: </p>
<pre>set(CPACK_DEBIAN_PACKAGE_CONTROL_STRICT_PERMISSION TRUE)</pre>
<p><code>NOTE:</code> This overrides the permissions on the original files, following the rules set by Debian policy <i><a rel="nofollow" href="https://www.debian.org/doc/debian-policy/ch-files.html#s-permissions-owners">https://www.debian.org/doc/debian-policy/ch-files.html#s-permissions-owners</a></i></p>
<dt><code>CPACK_DEBIAN_PACKAGE_SOURCE</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_SOURCE</code></p>
<dd>Sets the <code>Source</code> field of the binary Debian package. When the binary package name is not the same as the source package name (in particular when several components/binaries are generated from one source) the source from which the binary has been generated should be indicated with the field <code>Source</code>.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd>An empty string for non-component based installations</p>
<dt>&bull;</p>
<dd><code>CPACK_DEBIAN_PACKAGE_SOURCE</code> for component-based installations. </p>
<p> See <i><a rel="nofollow" href="https://www.debian.org/doc/debian-policy/ch-controlfields.html#s-f-Source">https://www.debian.org/doc/debian-policy/ch-controlfields.html#s-f-Source</a></i> </p>
<p> <code>NOTE:</code> This value is not interpreted. It is possible to pass an optional revision number of the referenced source package as well.</dl>
<h3>CPackDMG</h3>
<p>DragNDrop CPack generator (Mac OS X).</p>
<h3>Variables specific to CPack DragNDrop generator</h3>
<p>The following variables are specific to the DragNDrop installers built on Mac OS X:</p>
<dl>
<dt><code>CPACK_DMG_VOLUME_NAME</code></p>
<dd>The volume name of the generated disk image. Defaults to CPACK_PACKAGE_FILE_NAME.</p>
<dt><code>CPACK_DMG_FORMAT</code></p>
<dd>The disk image format. Common values are UDRO (UDIF read-only), UDZO (UDIF zlib-compressed) or UDBZ (UDIF bzip2-compressed). Refer to <a href="/docs/linux/man/1-hdiutil/">hdiutil</a>(1) for more information on other available formats. Defaults to UDZO.</p>
<dt><code>CPACK_DMG_DS_STORE</code></p>
<dd>Path to a custom DS_Store file. This .DS_Store file e.g. can be used to specify the Finder window position/geometry and layout (such as hidden toolbars, placement of the icons etc.). This file has to be generated by the Finder (either manually or through AppleScript) using a normal folder from which the .DS_Store file can then be extracted.</p>
<dt><code>CPACK_DMG_DS_STORE_SETUP_SCRIPT</code></p>
<dd>Path to a custom AppleScript file. This AppleScript is used to generate a .DS_Store file which specifies the Finder window position/geometry and layout (such as hidden toolbars, placement of the icons etc.). By specifying a custom AppleScript there is no need to use CPACK_DMG_DS_STORE, as the .DS_Store that is generated by the AppleScript will be packaged.</p>
<dt><code>CPACK_DMG_BACKGROUND_IMAGE</code></p>
<dd>Path to an image file to be used as the background. This file will be copied to .background/background.&lt;ext&gt;, where ext is the original image file extension. The background image is installed into the image before CPACK_DMG_DS_STORE_SETUP_SCRIPT is executed or CPACK_DMG_DS_STORE is installed. By default no background image is set.</p>
<dt><code>CPACK_DMG_DISABLE_APPLICATIONS_SYMLINK</code></p>
<dd>Default behaviour is to include a symlink to <code>/Applications</code> in the DMG. Set this option to <code>ON</code> to avoid adding the symlink.</p>
<dt><code>CPACK_DMG_SLA_DIR</code></p>
<dd>Directory where license and menu files for different languages are stored. Setting this causes CPack to look for a <code>&lt;language&gt;.menu.txt</code> and <code>&lt;language&gt;.license.txt</code> file for every language defined in <code>CPACK_DMG_SLA_LANGUAGES</code>. If both this variable and <code>CPACK_RESOURCE_FILE_LICENSE</code> are set, CPack will only look for the menu files and use the same license file for all languages.</p>
<dt><code>CPACK_DMG_SLA_LANGUAGES</code></p>
<dd>Languages for which a license agreement is provided when mounting the generated DMG. A menu file consists of 9 lines of text. The first line is is the name of the language itself, uppercase, in English (e.g. German). The other lines are translations of the following strings:</p>
<dt>&bull;</p>
<dd>Agree</p>
<dt>&bull;</p>
<dd>Disagree</p>
<dt>&bull;</p>
<dd>Print</p>
<dt>&bull;</p>
<dd>Save&#8230;</p>
<dt>&bull;</p>
<dd>You agree to the terms of the License Agreement when you click the &quot;Agree&quot; button.</p>
<dt>&bull;</p>
<dd>Software License Agreement</p>
<dt>&bull;</p>
<dd>This text cannot be saved. The disk may be full or locked, or the file may be locked.</p>
<dt>&bull;</p>
<dd>Unable to print. Make sure you have selected a printer. </p>
<p> For every language in this list, CPack will try to find files <code>&lt;language&gt;.menu.txt</code> and <code>&lt;language&gt;.license.txt</code> in the directory specified by the <code>CPACK_DMG_SLA_DIR</code> variable.</p>
<dt><code>CPACK_COMMAND_HDIUTIL</code></p>
<dd>Path to the <a href="/docs/linux/man/1-hdiutil/">hdiutil</a>(1) command used to operate on disk image files on Mac OS X. This variable can be used to override the automatically detected command (or specify its location if the auto-detection fails to find it.)</p>
<dt><code>CPACK_COMMAND_SETFILE</code></p>
<dd>Path to the <a href="/docs/linux/man/1-setfile/">SetFile</a>(1) command used to set extended attributes on files and directories on Mac OS X. This variable can be used to override the automatically detected command (or specify its location if the auto-detection fails to find it.)</p>
<dt><code>CPACK_COMMAND_REZ</code></p>
<dd>Path to the <a href="/docs/linux/man/1-rez/">Rez</a>(1) command used to compile resources on Mac OS X. This variable can be used to override the automatically detected command (or specify its location if the auto-detection fails to find it.)</dl>
<h3>CPackIFW</h3>
<p>This module looks for the location of the command line utilities supplied with the Qt Installer Framework (<i>QtIFW</i>). </p>
<p> The module also defines several commands to control the behavior of the CPack <code>IFW</code> generator.</p>
<h3>Overview</h3>
<p>CPack <code>IFW</code> generator helps you to create online and offline binary cross-platform installers with a graphical user interface. </p>
<p> CPack IFW generator prepares project installation and generates configuration and meta information for <i>QtIFW</i> tools. </p>
<p> The <i>QtIFW</i> provides a set of tools and utilities to create installers for the supported desktop Qt platforms: Linux, Microsoft Windows, and Mac OS X. </p>
<p> You should also install <i>QtIFW</i> to use CPack <code>IFW</code> generator. If you don&#8217;t use a default path for the installation, please set the used path in the variable <code>QTIFWDIR</code>.</p>
<h3>Variables</h3>
<p>You can use the following variables to change behavior of CPack <code>IFW</code> generator.</p>
<h3>Debug</h3>
<dl>
<dt><code>CPACK_IFW_VERBOSE</code></p>
<dd>Set to <code>ON</code> to enable addition debug output. By default is <code>OFF</code>.</dl>
<h3>Package</h3>
<dl>
<dt><code>CPACK_IFW_PACKAGE_TITLE</code></p>
<dd>Name of the installer as displayed on the title bar. By default used <code>CPACK_PACKAGE_DESCRIPTION_SUMMARY</code>.</p>
<dt><code>CPACK_IFW_PACKAGE_PUBLISHER</code></p>
<dd>Publisher of the software (as shown in the Windows Control Panel). By default used <code>CPACK_PACKAGE_VENDOR</code>.</p>
<dt><code>CPACK_IFW_PRODUCT_URL</code></p>
<dd>URL to a page that contains product information on your web site.</p>
<dt><code>CPACK_IFW_PACKAGE_ICON</code></p>
<dd>Filename for a custom installer icon. The actual file is &#8216;.icns&#8217; (Mac OS X), &#8216;.ico&#8217; (Windows). No functionality on Unix.</p>
<dt><code>CPACK_IFW_PACKAGE_WINDOW_ICON</code></p>
<dd>Filename for a custom window icon in PNG format for the Installer application.</p>
<dt><code>CPACK_IFW_PACKAGE_LOGO</code></p>
<dd>Filename for a logo is used as QWizard::LogoPixmap.</p>
<dt><code>CPACK_IFW_PACKAGE_START_MENU_DIRECTORY</code></p>
<dd>Name of the default program group for the product in the Windows Start menu. </p>
<p> By default used <code>CPACK_IFW_PACKAGE_NAME</code>.</p>
<dt><code>CPACK_IFW_TARGET_DIRECTORY</code></p>
<dd>Default target directory for installation. By default used &quot;@ApplicationsDir@/<code>CPACK_PACKAGE_INSTALL_DIRECTORY</code>&quot; </p>
<p> You can use predefined variables.</p>
<dt><code>CPACK_IFW_ADMIN_TARGET_DIRECTORY</code></p>
<dd>Default target directory for installation with administrator rights. </p>
<p> You can use predefined variables.</p>
<dt><code>CPACK_IFW_PACKAGE_GROUP</code></p>
<dd>The group, which will be used to configure the root package</p>
<dt><code>CPACK_IFW_PACKAGE_NAME</code></p>
<dd>The root package name, which will be used if configuration group is not specified</p>
<dt><code>CPACK_IFW_PACKAGE_MAINTENANCE_TOOL_NAME</code></p>
<dd>Filename of the generated maintenance tool. The platform-specific executable file extension is appended. </p>
<p> By default used <i>QtIFW</i> defaults (<code>maintenancetool</code>).</p>
<dt><code>CPACK_IFW_PACKAGE_MAINTENANCE_TOOL_INI_FILE</code></p>
<dd>Filename for the configuration of the generated maintenance tool. </p>
<p> By default used <i>QtIFW</i> defaults (<code>maintenancetool.ini</code>).</p>
<dt><code>CPACK_IFW_PACKAGE_ALLOW_NON_ASCII_CHARACTERS</code></p>
<dd>Set to <code>ON</code> if the installation path can contain non-ASCII characters. </p>
<p> Is <code>ON</code> for <i>QtIFW</i> less 2.0 tools.</p>
<dt><code>CPACK_IFW_PACKAGE_ALLOW_SPACE_IN_PATH</code></p>
<dd>Set to <code>OFF</code> if the installation path cannot contain space characters. </p>
<p> Is <code>ON</code> for <i>QtIFW</i> less 2.0 tools.</p>
<dt><code>CPACK_IFW_PACKAGE_CONTROL_SCRIPT</code></p>
<dd>Filename for a custom installer control script.</p>
<dt><code>CPACK_IFW_REPOSITORIES_ALL</code></p>
<dd>The list of remote repositories. </p>
<p> The default value of this variable is computed by CPack and contains all repositories added with command <code>cpack_ifw_add_repository()</code> or updated with command <code>cpack_ifw_update_repository()</code>.</p>
<dt><code>CPACK_IFW_DOWNLOAD_ALL</code></p>
<dd>If this is <code>ON</code> all components will be downloaded. By default is <code>OFF</code> or used value from <code>CPACK_DOWNLOAD_ALL</code> if set</dl>
<h3>Components</h3>
<dl>
<dt><code>CPACK_IFW_RESOLVE_DUPLICATE_NAMES</code></p>
<dd>Resolve duplicate names when installing components with groups.</p>
<dt><code>CPACK_IFW_PACKAGES_DIRECTORIES</code></p>
<dd>Additional prepared packages dirs that will be used to resolve dependent components.</dl>
<h3>Tools</h3>
<dl>
<dt><code>CPACK_IFW_FRAMEWORK_VERSION</code></p>
<dd>The version of used <i>QtIFW</i> tools.</p>
<dt><code>CPACK_IFW_BINARYCREATOR_EXECUTABLE</code></p>
<dd>The path to &quot;binarycreator&quot; command line client. </p>
<p> This variable is cached and can be configured user if need.</p>
<dt><code>CPACK_IFW_REPOGEN_EXECUTABLE</code></p>
<dd>The path to &quot;repogen&quot; command line client. </p>
<p> This variable is cached and can be configured user if need.</dl>
<h3>Commands</h3>
<p>The module defines the following commands: </p>
<p> <center> &#8212;-<br />
 </center> </p>
<dl>
<dt><code>cpack_ifw_configure_component</code></p>
<dd>Sets the arguments specific to the CPack IFW generator. </p>
<pre>cpack_ifw_configure_component(&lt;compname&gt; [COMMON] [ESSENTIAL]
 [NAME &lt;name&gt;]
 [VERSION &lt;version&gt;]
 [SCRIPT &lt;script&gt;]
 [PRIORITY &lt;priority&gt;]
 [DEPENDS &lt;com_id&gt; ...]
 [LICENSES &lt;display_name&gt; &lt;file_path&gt; ...])</pre>
<p>This command should be called after <code>cpack_add_component()</code> command. </p>
<p> <code>COMMON</code> if set, then the component will be packaged and installed as part of a group to which it belongs. </p>
<p> <code>ESSENTIAL</code> if set, then the package manager stays disabled until that component is updated. </p>
<p> <code>NAME</code> is used to create domain-like identification for this component. By default used origin component name. </p>
<p> <code>VERSION</code> is version of component. By default used <code>CPACK_PACKAGE_VERSION</code>. </p>
<p> <code>SCRIPT</code> is a relative or absolute path to operations script for this component. </p>
<p> <code>PRIORITY</code> is priority of the component in the tree. </p>
<p> <code>DEPENDS</code> list of dependency component identifiers in <i>QtIFW</i> style. </p>
<p> <code>LICENSES</code> pair of &lt;display_name&gt; and &lt;file_path&gt; of license text for this component. You can specify more then one license. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<dt><code>cpack_ifw_configure_component_group</code></p>
<dd>Sets the arguments specific to the CPack IFW generator. </p>
<pre>cpack_ifw_configure_component_group(&lt;groupname&gt;
 [NAME &lt;name&gt;]
 [VERSION &lt;version&gt;]
 [SCRIPT &lt;script&gt;]
 [PRIORITY &lt;priority&gt;]
 [LICENSES &lt;display_name&gt; &lt;file_path&gt; ...])</pre>
<p>This command should be called after <code>cpack_add_component_group()</code> command. </p>
<p> <code>NAME</code> is used to create domain-like identification for this component group. By default used origin component group name. </p>
<p> <code>VERSION</code> is version of component group. By default used <code>CPACK_PACKAGE_VERSION</code>. </p>
<p> <code>SCRIPT</code> is a relative or absolute path to operations script for this component group. </p>
<p> <code>PRIORITY</code> is priority of the component group in the tree. </p>
<p> <code>LICENSES</code> pair of &lt;display_name&gt; and &lt;file_path&gt; of license text for this component group. You can specify more then one license. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<dt><code>cpack_ifw_add_repository</code></p>
<dd>Add <i>QtIFW</i> specific remote repository to binary installer. </p>
<pre>cpack_ifw_add_repository(&lt;reponame&gt; [DISABLED]
 URL &lt;url&gt;
 [USERNAME &lt;username&gt;]
 [PASSWORD &lt;password&gt;]
 [DISPLAY_NAME &lt;display_name&gt;])</pre>
<p>This command will also add the &lt;reponame&gt; repository to a variable <code>CPACK_IFW_REPOSITORIES_ALL</code>. </p>
<p> <code>DISABLED</code> if set, then the repository will be disabled by default. </p>
<p> <code>URL</code> is points to a list of available components. </p>
<p> <code>USERNAME</code> is used as user on a protected repository. </p>
<p> <code>PASSWORD</code> is password to use on a protected repository. </p>
<p> <code>DISPLAY_NAME</code> is string to display instead of the URL. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<dt><code>cpack_ifw_update_repository</code></p>
<dd>Update <i>QtIFW</i> specific repository from remote repository. </p>
<pre>cpack_ifw_update_repository(&lt;reponame&gt;
 [[ADD|REMOVE] URL &lt;url&gt;]|
 [REPLACE OLD_URL &lt;old_url&gt; NEW_URL &lt;new_url&gt;]]
 [USERNAME &lt;username&gt;]
 [PASSWORD &lt;password&gt;]
 [DISPLAY_NAME &lt;display_name&gt;])</pre>
<p>This command will also add the &lt;reponame&gt; repository to a variable <code>CPACK_IFW_REPOSITORIES_ALL</code>. </p>
<p> <code>URL</code> is points to a list of available components. </p>
<p> <code>OLD_URL</code> is points to a list that will replaced. </p>
<p> <code>NEW_URL</code> is points to a list that will replace to. </p>
<p> <code>USERNAME</code> is used as user on a protected repository. </p>
<p> <code>PASSWORD</code> is password to use on a protected repository. </p>
<p> <code>DISPLAY_NAME</code> is string to display instead of the URL.</dl>
<h3>Example usage</h3>
<pre>set(CPACK_PACKAGE_NAME &quot;MyPackage&quot;)
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY &quot;MyPackage Installation Example&quot;)
set(CPACK_PACKAGE_VERSION &quot;1.0.0&quot;) # Version of installer
include(CPack)
include(CPackIFW)
cpack_add_component(myapp
 DISPLAY_NAME &quot;MyApp&quot;
 DESCRIPTION &quot;My Application&quot;)
cpack_ifw_configure_component(myapp
 VERSION &quot;1.2.3&quot; # Version of component
 SCRIPT &quot;operations.qs&quot;)
cpack_add_component(mybigplugin
 DISPLAY_NAME &quot;MyBigPlugin&quot;
 DESCRIPTION &quot;My Big Downloadable Plugin&quot;
 DOWNLOADED)
cpack_ifw_add_repository(myrepo
 URL &quot;<a rel="nofollow" href="http://example.com/ifw/repo/myapp">http://example.com/ifw/repo/myapp</a>&quot;
 DISPLAY_NAME &quot;My Application Repository&quot;)</pre>
<h3>Online installer</h3>
<p>By default CPack IFW generator makes offline installer. This means that all components will be packaged into a binary file. </p>
<p> To make a component downloaded, you must set the <code>DOWNLOADED</code> option in <code>cpack_add_component()</code>. </p>
<p> Then you would use the command <code>cpack_configure_downloads()</code>. If you set <code>ALL</code> option all components will be downloaded. </p>
<p> You also can use command <code>cpack_ifw_add_repository()</code> and variable <code>CPACK_IFW_DOWNLOAD_ALL</code> for more specific configuration. </p>
<p> CPack IFW generator creates &quot;repository&quot; dir in current binary dir. You would copy content of this dir to specified <code>site</code> (<code>url</code>).</p>
<h3>See Also</h3>
<p>Qt Installer Framework Manual:</p>
<dl>
<dt><code>Index page</code></p>
<dd><i><a rel="nofollow" href="http://doc.qt.io/qtinstallerframework/index.html">http://doc.qt.io/qtinstallerframework/index.html</a></i></p>
<dt><code>Component Scripting</code></p>
<dd><i><a rel="nofollow" href="http://doc.qt.io/qtinstallerframework/scripting.html">http://doc.qt.io/qtinstallerframework/scripting.html</a></i></p>
<dt><code>Predefined Variables</code></p>
<dd><i><a rel="nofollow" href="http://doc.qt.io/qtinstallerframework/scripting.html#predefined-variables">http://doc.qt.io/qtinstallerframework/scripting.html#predefined-variables</a></i></p>
<dt><code>Promoting Updates</code></p>
<dd><i><a rel="nofollow" href="http://doc.qt.io/qtinstallerframework/ifw-updates.html">http://doc.qt.io/qtinstallerframework/ifw-updates.html</a></i></p>
<dt><code>Download Qt Installer Framework for you platform from Qt site:</code></p>
<dd><i><a rel="nofollow" href="http://download.qt.io/official_releases/qt-installer-framework">http://download.qt.io/official_releases/qt-installer-framework</a></i></dl>
<h3>CPackNSIS</h3>
<p>CPack NSIS generator specific options</p>
<h3>Variables specific to CPack NSIS generator</h3>
<p>The following variables are specific to the graphical installers built on Windows using the Nullsoft Installation System.</p>
<dl>
<dt><code>CPACK_NSIS_INSTALL_ROOT</code></p>
<dd>The default installation directory presented to the end user by the NSIS installer is under this root dir. The full directory presented to the end user is: ${CPACK_NSIS_INSTALL_ROOT}/${CPACK_PACKAGE_INSTALL_DIRECTORY}</p>
<dt><code>CPACK_NSIS_MUI_ICON</code></p>
<dd>An icon filename. The name of a <code>*.ico</code> file used as the main icon for the generated install program.</p>
<dt><code>CPACK_NSIS_MUI_UNIICON</code></p>
<dd>An icon filename. The name of a <code>*.ico</code> file used as the main icon for the generated uninstall program.</p>
<dt><code>CPACK_NSIS_INSTALLER_MUI_ICON_CODE</code></p>
<dd>undocumented.</p>
<dt><code>CPACK_NSIS_MUI_WELCOMEFINISHPAGE_BITMAP</code></p>
<dd>The filename of a bitmap to use as the NSIS MUI_WELCOMEFINISHPAGE_BITMAP.</p>
<dt><code>CPACK_NSIS_MUI_UNWELCOMEFINISHPAGE_BITMAP</code></p>
<dd>The filename of a bitmap to use as the NSIS MUI_UNWELCOMEFINISHPAGE_BITMAP.</p>
<dt><code>CPACK_NSIS_EXTRA_PREINSTALL_COMMANDS</code></p>
<dd>Extra NSIS commands that will be added to the beginning of the install Section, before your install tree is available on the target system.</p>
<dt><code>CPACK_NSIS_EXTRA_INSTALL_COMMANDS</code></p>
<dd>Extra NSIS commands that will be added to the end of the install Section, after your install tree is available on the target system.</p>
<dt><code>CPACK_NSIS_EXTRA_UNINSTALL_COMMANDS</code></p>
<dd>Extra NSIS commands that will be added to the uninstall Section, before your install tree is removed from the target system.</p>
<dt><code>CPACK_NSIS_COMPRESSOR</code></p>
<dd>The arguments that will be passed to the NSIS SetCompressor command.</p>
<dt><code>CPACK_NSIS_ENABLE_UNINSTALL_BEFORE_INSTALL</code></p>
<dd>Ask about uninstalling previous versions first. If this is set to &quot;ON&quot;, then an installer will look for previous installed versions and if one is found, ask the user whether to uninstall it before proceeding with the install.</p>
<dt><code>CPACK_NSIS_MODIFY_PATH</code></p>
<dd>Modify PATH toggle. If this is set to &quot;ON&quot;, then an extra page will appear in the installer that will allow the user to choose whether the program directory should be added to the system PATH variable.</p>
<dt><code>CPACK_NSIS_DISPLAY_NAME</code></p>
<dd>The display name string that appears in the Windows Add/Remove Program control panel</p>
<dt><code>CPACK_NSIS_PACKAGE_NAME</code></p>
<dd>The title displayed at the top of the installer.</p>
<dt><code>CPACK_NSIS_INSTALLED_ICON_NAME</code></p>
<dd>A path to the executable that contains the installer icon.</p>
<dt><code>CPACK_NSIS_HELP_LINK</code></p>
<dd>URL to a web site providing assistance in installing your application.</p>
<dt><code>CPACK_NSIS_URL_INFO_ABOUT</code></p>
<dd>URL to a web site providing more information about your application.</p>
<dt><code>CPACK_NSIS_CONTACT</code></p>
<dd>Contact information for questions and comments about the installation process.</p>
<dt><code>CPACK_NSIS_CREATE_ICONS_EXTRA</code></p>
<dd>Additional NSIS commands for creating start menu shortcuts.</p>
<dt><code>CPACK_NSIS_DELETE_ICONS_EXTRA</code></p>
<dd>Additional NSIS commands to uninstall start menu shortcuts.</p>
<dt><code>CPACK_NSIS_EXECUTABLES_DIRECTORY</code></p>
<dd>Creating NSIS start menu links assumes that they are in &#8216;bin&#8217; unless this variable is set. For example, you would set this to &#8216;exec&#8217; if your executables are in an exec directory.</p>
<dt><code>CPACK_NSIS_MUI_FINISHPAGE_RUN</code></p>
<dd>Specify an executable to add an option to run on the finish page of the NSIS installer.</p>
<dt><code>CPACK_NSIS_MENU_LINKS</code></p>
<dd>Specify links in [application] menu. This should contain a list of pair &quot;link&quot; &quot;link name&quot;. The link may be an URL or a path relative to installation prefix. Like: </p>
<pre>set(CPACK_NSIS_MENU_LINKS
 &quot;doc/cmake- [at] CMake_VERSION_MAJOR@.@CMake_VERSION_MINOR@/cmake.html&quot;
 &quot;CMake Help&quot; &quot;<a rel="nofollow" href="https://cmake.org">https://cmake.org</a>&quot; &quot;CMake Web Site&quot;)</pre>
</dl>
<h3>CPackPackageMaker</h3>
<p>PackageMaker CPack generator (Mac OS X).</p>
<h3>Variables specific to CPack PackageMaker generator</h3>
<p>The following variable is specific to installers built on Mac OS X using PackageMaker:</p>
<dl>
<dt><code>CPACK_OSX_PACKAGE_VERSION</code></p>
<dd>The version of Mac OS X that the resulting PackageMaker archive should be compatible with. Different versions of Mac OS X support different features. For example, CPack can only build component-based installers for Mac OS X 10.4 or newer, and can only build installers that download component son-the-fly for Mac OS X 10.5 or newer. If left blank, this value will be set to the minimum version of Mac OS X that supports the requested features. Set this variable to some value (e.g., 10.4) only if you want to guarantee that your installer will work on that version of Mac OS X, and don&#8217;t mind missing extra features available in the installer shipping with later versions of Mac OS X.</dl>
<h3>CPackRPM</h3>
<p>The built in (binary) CPack RPM generator (Unix only)</p>
<h3>Variables specific to CPack RPM generator</h3>
<p>CPackRPM may be used to create RPM packages using <code>CPack</code>. CPackRPM is a <code>CPack</code> generator thus it uses the <code>CPACK_XXX</code> variables used by <code>CPack</code>. </p>
<p> CPackRPM has specific features which are controlled by the specifics <code>CPACK_RPM_XXX</code> variables. </p>
<p> <code>CPACK_RPM_&lt;COMPONENT&gt;_XXXX</code> variables may be used in order to have <code>component</code> specific values. Note however that <code>&lt;COMPONENT&gt;</code> refers to the <code>grouping name</code> written in upper case. It may be either a component name or a component GROUP name. Usually those variables correspond to RPM spec file entities. One may find information about spec files here <i><a rel="nofollow" href="http://www.rpm.org/wiki/Docs">http://www.rpm.org/wiki/Docs</a></i> </p>
<p> <code>NOTE:</code> <i>&lt;COMPONENT&gt;</i> part of variables is preferred to be in upper case (for e.g. if component is named <i>foo</i> then use <i>CPACK_RPM_FOO_XXXX</i> variable name format) as is with other <i>CPACK_&lt;COMPONENT&gt;_XXXX</i> variables. For the purposes of back compatibility (CMake/CPack version 3.5 and lower) support for same cased component (e.g. <i>fOo</i> would be used as <i>CPACK_RPM_fOo_XXXX</i>) is still supported for variables defined in older versions of CMake/CPack but is not guaranteed for variables that will be added in the future. For the sake of back compatibility same cased component variables also override upper cased versions where both are present. </p>
<p> Here are some CPackRPM wiki resources that are here for historic reasons and are no longer maintained but may still prove useful:</p>
<dl>
<dt>&bull;</p>
<dd><i><a rel="nofollow" href="https://cmake.org/Wiki/CMake:CPackConfiguration">https://cmake.org/Wiki/CMake:CPackConfiguration</a></i></p>
<dt>&bull;</p>
<dd><i><a rel="nofollow" href="https://cmake.org/Wiki/CMake:CPackPackageGenerators#RPM_.28Unix_Only.29">https://cmake.org/Wiki/CMake:CPackPackageGenerators#RPM_.28Unix_Only.29</a></i> </p>
<p> List of CPackRPM specific variables:</p>
<dt><code>CPACK_RPM_PACKAGE_COMPONENT</code></p>
<dd>Enable component packaging for CPackRPM</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : OFF </p>
<p> If enabled (ON) multiple packages are generated. By default a single package containing files of all components is generated.</p>
<dt><code>CPACK_RPM_PACKAGE_SUMMARY</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_SUMMARY</code></p>
<dd>The RPM package summary.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : <code>CPACK_PACKAGE_DESCRIPTION_SUMMARY</code></p>
<dt><code>CPACK_RPM_PACKAGE_NAME</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_NAME</code></p>
<dd>The RPM package name.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : <code>CPACK_PACKAGE_NAME</code></p>
<dt><code>CPACK_RPM_FILE_NAME</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_FILE_NAME</code></p>
<dd>Package file name.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>
<dt><code>Default</code></p>
<dd><code>&lt;CPACK_PACKAGE_FILE_NAME&gt;[-&lt;component&gt;].rpm</code> with spaces replaced by &#8216;-&#8216; </p>
<p> This may be set to <code>RPM-DEFAULT</code> to allow rpmbuild tool to generate package file name by itself. Alternatively provided package file name must end with <code>.rpm</code> suffix. </p>
<p> <code>NOTE:</code> By using user provided spec file, rpm macro extensions such as for generating debuginfo packages or by simply using multiple components more than one rpm file may be generated, either from a single spec file or from multiple spec files (each component execution produces it&#8217;s own spec file). In such cases duplicate file names may occur as a result of this variable setting or spec file content structure. Duplicate files get overwritten and it is up to the packager to set the variables in a manner that will prevent such errors.</p>
<dt><code>CPACK_RPM_PACKAGE_VERSION</code></p>
<dd>The RPM package version.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : <code>CPACK_PACKAGE_VERSION</code></p>
<dt><code>CPACK_RPM_PACKAGE_ARCHITECTURE</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_ARCHITECTURE</code></p>
<dd>The RPM package architecture.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : Native architecture output by <code>uname -m</code> </p>
<p> This may be set to <code>noarch</code> if you know you are building a noarch package.</p>
<dt><code>CPACK_RPM_PACKAGE_RELEASE</code></p>
<dd>The RPM package release.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : 1 </p>
<p> This is the numbering of the RPM package itself, i.e. the version of the packaging and not the version of the content (see <code>CPACK_RPM_PACKAGE_VERSION</code>). One may change the default value if the previous packaging was buggy and/or you want to put here a fancy Linux distro specific numbering. </p>
<p> <code>NOTE:</code> This is the string that goes into the RPM <code>Release:</code> field. Some distros (e.g. Fedora, CentOS) require <code>1%{?dist}</code> format and not just a number. <code>%{?dist}</code> part can be added by setting <code>CPACK_RPM_PACKAGE_RELEASE_DIST</code>.</p>
<dt><code>CPACK_RPM_PACKAGE_RELEASE_DIST</code></p>
<dd>The dist tag that is added RPM <code>Release:</code> field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : OFF </p>
<p> This is the reported <code>%{dist}</code> tag from the current distribution or empty <code>%{dist}</code> if RPM macro is not set. If this variable is set then RPM <code>Release:</code> field value is set to <code>${CPACK_RPM_PACKAGE_RELEASE}%{?dist}</code>.</p>
<dt><code>CPACK_RPM_PACKAGE_LICENSE</code></p>
<dd>The RPM package license policy.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : &quot;unknown&quot;</p>
<dt><code>CPACK_RPM_PACKAGE_GROUP</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_GROUP</code></p>
<dd>The RPM package group.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : &quot;unknown&quot;</p>
<dt><code>CPACK_RPM_PACKAGE_VENDOR</code></p>
<dd>The RPM package vendor.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : CPACK_PACKAGE_VENDOR if set or &quot;unknown&quot;</p>
<dt><code>CPACK_RPM_PACKAGE_URL</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_URL</code></p>
<dd>The projects URL.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211;</p>
<dt><code>CPACK_RPM_PACKAGE_DESCRIPTION</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_DESCRIPTION</code></p>
<dd>RPM package description.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : <code>CPACK_COMPONENT_&lt;compName&gt;_DESCRIPTION</code> (component based installers only) if set, <code>CPACK_PACKAGE_DESCRIPTION_FILE</code> if set or &quot;no package description available&quot;</p>
<dt><code>CPACK_RPM_COMPRESSION_TYPE</code></p>
<dd>RPM compression type.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to override RPM compression type to be used to build the RPM. For example some Linux distribution now default to lzma or xz compression whereas older cannot use such RPM. Using this one can enforce compression type to be used. </p>
<p> Possible values are:</p>
<dt>&bull;</p>
<dd>lzma</p>
<dt>&bull;</p>
<dd>xz</p>
<dt>&bull;</p>
<dd>bzip2</p>
<dt>&bull;</p>
<dd>gzip</p>
<dt><code>CPACK_RPM_PACKAGE_AUTOREQ</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_AUTOREQ</code></p>
<dd>RPM spec autoreq field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to enable (1, yes) or disable (0, no) automatic shared libraries dependency detection. Dependencies are added to requires list. </p>
<p> <code>NOTE:</code> By default automatic dependency detection is enabled by rpm generator.</p>
<dt><code>CPACK_RPM_PACKAGE_AUTOPROV</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_AUTOPROV</code></p>
<dd>RPM spec autoprov field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to enable (1, yes) or disable (0, no) automatic listing of shared libraries that are provided by the package. Shared libraries are added to provides list. </p>
<p> <code>NOTE:</code> By default automatic provides detection is enabled by rpm generator.</p>
<dt><code>CPACK_RPM_PACKAGE_AUTOREQPROV</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_AUTOREQPROV</code></p>
<dd>RPM spec autoreqprov field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> Variable enables/disables autoreq and autoprov at the same time. See <code>CPACK_RPM_PACKAGE_AUTOREQ</code> and <code>CPACK_RPM_PACKAGE_AUTOPROV</code> for more details. </p>
<p> <code>NOTE:</code> By default automatic detection feature is enabled by rpm.</p>
<dt><code>CPACK_RPM_PACKAGE_REQUIRES</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_REQUIRES</code></p>
<dd>RPM spec requires field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to set RPM dependencies (requires). Note that you must enclose the complete requires string between quotes, for example: </p>
<pre>set(CPACK_RPM_PACKAGE_REQUIRES &quot;python &gt;= 2.5.0, cmake &gt;= 2.8&quot;)</pre>
<p>The required package list of an RPM file could be printed with: </p>
<pre>rpm -qp --requires file.rpm</pre>
<dt><code>CPACK_RPM_PACKAGE_CONFLICTS</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_CONFLICTS</code></p>
<dd>RPM spec conflicts field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to set negative RPM dependencies (conflicts). Note that you must enclose the complete requires string between quotes, for example: </p>
<pre>set(CPACK_RPM_PACKAGE_CONFLICTS &quot;libxml2&quot;)</pre>
<p>The conflicting package list of an RPM file could be printed with: </p>
<pre>rpm -qp --conflicts file.rpm</pre>
<dt><code>CPACK_RPM_PACKAGE_REQUIRES_PRE</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_REQUIRES_PRE</code></p>
<dd>RPM spec requires(pre) field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to set RPM preinstall dependencies (requires(pre)). Note that you must enclose the complete requires string between quotes, for example: </p>
<pre>set(CPACK_RPM_PACKAGE_REQUIRES_PRE &quot;shadow-utils, initscripts&quot;)</pre>
<dt><code>CPACK_RPM_PACKAGE_REQUIRES_POST</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_REQUIRES_POST</code></p>
<dd>RPM spec requires(post) field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to set RPM postinstall dependencies (requires(post)). Note that you must enclose the complete requires string between quotes, for example: </p>
<pre>set(CPACK_RPM_PACKAGE_REQUIRES_POST &quot;shadow-utils, initscripts&quot;)</pre>
<dt><code>CPACK_RPM_PACKAGE_REQUIRES_POSTUN</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_REQUIRES_POSTUN</code></p>
<dd>RPM spec requires(postun) field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to set RPM postuninstall dependencies (requires(postun)). Note that you must enclose the complete requires string between quotes, for example: </p>
<pre>set(CPACK_RPM_PACKAGE_REQUIRES_POSTUN &quot;shadow-utils, initscripts&quot;)</pre>
<dt><code>CPACK_RPM_PACKAGE_REQUIRES_PREUN</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_REQUIRES_PREUN</code></p>
<dd>RPM spec requires(preun) field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to set RPM preuninstall dependencies (requires(preun)). Note that you must enclose the complete requires string between quotes, for example: </p>
<pre>set(CPACK_RPM_PACKAGE_REQUIRES_PREUN &quot;shadow-utils, initscripts&quot;)</pre>
<dt><code>CPACK_RPM_PACKAGE_SUGGESTS</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_SUGGESTS</code></p>
<dd>RPM spec suggest field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to set weak RPM dependencies (suggests). Note that you must enclose the complete requires string between quotes.</p>
<dt><code>CPACK_RPM_PACKAGE_PROVIDES</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_PROVIDES</code></p>
<dd>RPM spec provides field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to set RPM dependencies (provides). The provided package list of an RPM file could be printed with: </p>
<pre>rpm -qp --provides file.rpm</pre>
<dt><code>CPACK_RPM_PACKAGE_OBSOLETES</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_OBSOLETES</code></p>
<dd>RPM spec obsoletes field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to set RPM packages that are obsoleted by this one.</p>
<dt><code>CPACK_RPM_PACKAGE_RELOCATABLE</code></p>
<dd>build a relocatable RPM.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : CPACK_PACKAGE_RELOCATABLE </p>
<p> If this variable is set to TRUE or ON CPackRPM will try to build a relocatable RPM package. A relocatable RPM may be installed using: </p>
<pre>rpm --prefix or --relocate</pre>
<p>in order to install it at an alternate place see <a href="/docs/linux/man/8-rpm/">rpm</a>(8). Note that currently this may fail if <code>CPACK_SET_DESTDIR</code> is set to <code>ON</code>. If <code>CPACK_SET_DESTDIR</code> is set then you will get a warning message but if there is file installed with absolute path you&#8217;ll get unexpected behavior.</p>
<dt><code>CPACK_RPM_SPEC_INSTALL_POST</code></p>
<dd>Deprecated &#8211; use <code>CPACK_RPM_POST_INSTALL_SCRIPT_FILE</code> instead.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211;</p>
<dt>&bull;</p>
<dd>Deprecated: YES </p>
<p> This way of specifying post-install script is deprecated, use <code>CPACK_RPM_POST_INSTALL_SCRIPT_FILE</code>. May be used to set an RPM post-install command inside the spec file. For example setting it to <code>/bin/true</code> may be used to prevent rpmbuild to strip binaries.</p>
<dt><code>CPACK_RPM_SPEC_MORE_DEFINE</code></p>
<dd>RPM extended spec definitions lines.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to add any <code>%define</code> lines to the generated spec file.</p>
<dt><code>CPACK_RPM_PACKAGE_DEBUG</code></p>
<dd>Toggle CPackRPM debug output.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be set when invoking cpack in order to trace debug information during CPack RPM run. For example you may launch CPack like this: </p>
<pre>cpack -D CPACK_RPM_PACKAGE_DEBUG=1 -G RPM</pre>
<dt><code>CPACK_RPM_USER_BINARY_SPECFILE</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;componentName&gt;_USER_BINARY_SPECFILE</code></p>
<dd>A user provided spec file.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be set by the user in order to specify a USER binary spec file to be used by CPackRPM instead of generating the file. The specified file will be processed by configure_file( @ONLY).</p>
<dt><code>CPACK_RPM_GENERATE_USER_BINARY_SPECFILE_TEMPLATE</code></p>
<dd>Spec file template.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> If set CPack will generate a template for USER specified binary spec file and stop with an error. For example launch CPack like this: </p>
<pre>cpack -D CPACK_RPM_GENERATE_USER_BINARY_SPECFILE_TEMPLATE=1 -G RPM</pre>
<p>The user may then use this file in order to hand-craft is own binary spec file which may be used with <code>CPACK_RPM_USER_BINARY_SPECFILE</code>.</p>
<dt><code>CPACK_RPM_PRE_INSTALL_SCRIPT_FILE</code></p>
<dd>
<dt><code>CPACK_RPM_PRE_UNINSTALL_SCRIPT_FILE</code></p>
<dd>Path to file containing pre (un)install script.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to embed a pre (un)installation script in the spec file. The referred script file (or both) will be read and directly put after the <code>%pre</code> or <code>%preun</code> section If <code>CPACK_RPM_PACKAGE_COMPONENT</code> is set to ON the (un)install script for each component can be overridden with <code>CPACK_RPM_&lt;COMPONENT&gt;_PRE_INSTALL_SCRIPT_FILE</code> and <code>CPACK_RPM_&lt;COMPONENT&gt;_PRE_UNINSTALL_SCRIPT_FILE</code>. One may verify which scriptlet has been included with: </p>
<pre>rpm -qp --scripts package.rpm</pre>
<dt><code>CPACK_RPM_POST_INSTALL_SCRIPT_FILE</code></p>
<dd>
<dt><code>CPACK_RPM_POST_UNINSTALL_SCRIPT_FILE</code></p>
<dd>Path to file containing post (un)install script.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to embed a post (un)installation script in the spec file. The referred script file (or both) will be read and directly put after the <code>%post</code> or <code>%postun</code> section. If <code>CPACK_RPM_PACKAGE_COMPONENT</code> is set to ON the (un)install script for each component can be overridden with <code>CPACK_RPM_&lt;COMPONENT&gt;_POST_INSTALL_SCRIPT_FILE</code> and <code>CPACK_RPM_&lt;COMPONENT&gt;_POST_UNINSTALL_SCRIPT_FILE</code>. One may verify which scriptlet has been included with: </p>
<pre>rpm -qp --scripts package.rpm</pre>
<dt><code>CPACK_RPM_USER_FILELIST</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;COMPONENT&gt;_USER_FILELIST</code></p>
<dd>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to explicitly specify <code>%(&lt;directive&gt;)</code> file line in the spec file. Like <code>%config(noreplace)</code> or any other directive that be found in the <code>%files</code> section. Since CPackRPM is generating the list of files (and directories) the user specified files of the <code>CPACK_RPM_&lt;COMPONENT&gt;_USER_FILELIST</code> list will be removed from the generated list.</p>
<dt><code>CPACK_RPM_CHANGELOG_FILE</code></p>
<dd>RPM changelog file.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to embed a changelog in the spec file. The referred file will be read and directly put after the <code>%changelog</code> section.</p>
<dt><code>CPACK_RPM_EXCLUDE_FROM_AUTO_FILELIST</code></p>
<dd>list of path to be excluded.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : /etc /etc/init.d /usr /usr/share /usr/share/doc /usr/bin /usr/lib /usr/lib64 /usr/include </p>
<p> May be used to exclude path (directories or files) from the auto-generated list of paths discovered by CPack RPM. The defaut value contains a reasonable set of values if the variable is not defined by the user. If the variable is defined by the user then CPackRPM will NOT any of the default path. If you want to add some path to the default list then you can use <code>CPACK_RPM_EXCLUDE_FROM_AUTO_FILELIST_ADDITION</code> variable.</p>
<dt><code>CPACK_RPM_EXCLUDE_FROM_AUTO_FILELIST_ADDITION</code></p>
<dd>additional list of path to be excluded.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to add more exclude path (directories or files) from the initial default list of excluded paths. See <code>CPACK_RPM_EXCLUDE_FROM_AUTO_FILELIST</code>.</p>
<dt><code>CPACK_RPM_RELOCATION_PATHS</code></p>
<dd>Packages relocation paths list.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to specify more than one relocation path per relocatable RPM. Variable contains a list of relocation paths that if relative are prefixed by the value of <code>CPACK_RPM_&lt;COMPONENT&gt;_PACKAGE_PREFIX</code> or by the value of <code>CPACK_PACKAGING_INSTALL_PREFIX</code> if the component version is not provided. Variable is not component based as its content can be used to set a different path prefix for e.g. binary dir and documentation dir at the same time. Only prefixes that are required by a certain component are added to that component &#8211; component must contain at least one file/directory/symbolic link with <code>CPACK_RPM_RELOCATION_PATHS</code> prefix for a certain relocation path to be added. Package will not contain any relocation paths if there are no files/directories/symbolic links on any of the provided prefix locations. Packages that either do not contain any relocation paths or contain files/directories/symbolic links that are outside relocation paths print out an <code>AUTHOR_WARNING</code> that RPM will be partially relocatable.</p>
<dt><code>CPACK_RPM_&lt;COMPONENT&gt;_PACKAGE_PREFIX</code></p>
<dd>Per component relocation path install prefix.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : CPACK_PACKAGING_INSTALL_PREFIX </p>
<p> May be used to set per component <code>CPACK_PACKAGING_INSTALL_PREFIX</code> for relocatable RPM packages.</p>
<dt><code>CPACK_RPM_NO_INSTALL_PREFIX_RELOCATION</code></p>
<dd>
<dt><code>CPACK_RPM_NO_&lt;COMPONENT&gt;_INSTALL_PREFIX_RELOCATION</code></p>
<dd>Removal of default install prefix from relocation paths list.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>
<dt><code>Default</code></p>
<dd>CPACK_PACKAGING_INSTALL_PREFIX or CPACK_RPM_&lt;COMPONENT&gt;_PACKAGE_PREFIX are treated as one of relocation paths </p>
<p> May be used to remove CPACK_PACKAGING_INSTALL_PREFIX and CPACK_RPM_&lt;COMPONENT&gt;_PACKAGE_PREFIX from relocatable RPM prefix paths.</p>
<dt><code>CPACK_RPM_ADDITIONAL_MAN_DIRS</code></p>
<dd>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to set additional man dirs that could potentially be compressed by brp-compress RPM macro. Variable content must be a list of regular expressions that point to directories containing man files or to man files directly. Note that in order to compress man pages a path must also be present in brp-compress RPM script and that brp-compress script must be added to RPM configuration by the operating system. </p>
<p> Regular expressions that are added by default were taken from brp-compress RPM macro:</p>
<dt>&bull;</p>
<dd>/usr/man/man.*</p>
<dt>&bull;</p>
<dd>/usr/man/.*/man.*</p>
<dt>&bull;</p>
<dd>/usr/info.*</p>
<dt>&bull;</p>
<dd>/usr/share/man/man.*</p>
<dt>&bull;</p>
<dd>/usr/share/man/.*/man.*</p>
<dt>&bull;</p>
<dd>/usr/share/info.*</p>
<dt>&bull;</p>
<dd>/usr/kerberos/man.*</p>
<dt>&bull;</p>
<dd>/usr/X11R6/man/man.*</p>
<dt>&bull;</p>
<dd>/usr/lib/perl5/man/man.*</p>
<dt>&bull;</p>
<dd>/usr/share/doc/.*/man/man.*</p>
<dt>&bull;</p>
<dd>/usr/lib/.*/man/man.*</p>
<dt><code>CPACK_RPM_DEFAULT_USER</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;compName&gt;_DEFAULT_USER</code></p>
<dd>default user ownership of RPM content</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : root </p>
<p> Value should be user name and not UID. Note that &lt;compName&gt; must be in upper-case.</p>
<dt><code>CPACK_RPM_DEFAULT_GROUP</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;compName&gt;_DEFAULT_GROUP</code></p>
<dd>default group ownership of RPM content</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : root </p>
<p> Value should be group name and not GID. Note that &lt;compName&gt; must be in upper-case.</p>
<dt><code>CPACK_RPM_DEFAULT_FILE_PERMISSIONS</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;compName&gt;_DEFAULT_FILE_PERMISSIONS</code></p>
<dd>default permissions used for packaged files</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; (system default) </p>
<p> Accepted values are lists with <code>PERMISSIONS</code>. Valid permissions are:</p>
<dt>&bull;</p>
<dd>OWNER_READ</p>
<dt>&bull;</p>
<dd>OWNER_WRITE</p>
<dt>&bull;</p>
<dd>OWNER_EXECUTE</p>
<dt>&bull;</p>
<dd>GROUP_READ</p>
<dt>&bull;</p>
<dd>GROUP_WRITE</p>
<dt>&bull;</p>
<dd>GROUP_EXECUTE</p>
<dt>&bull;</p>
<dd>WORLD_READ</p>
<dt>&bull;</p>
<dd>WORLD_WRITE</p>
<dt>&bull;</p>
<dd>WORLD_EXECUTE </p>
<p> Note that &lt;compName&gt; must be in upper-case.</p>
<dt><code>CPACK_RPM_DEFAULT_DIR_PERMISSIONS</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;compName&gt;_DEFAULT_DIR_PERMISSIONS</code></p>
<dd>default permissions used for packaged directories</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; (system default) </p>
<p> Accepted values are lists with PERMISSIONS. Valid permissions are the same as for <code>CPACK_RPM_DEFAULT_FILE_PERMISSIONS</code>. Note that &lt;compName&gt; must be in upper-case.</dl>
<h3>Packaging of Symbolic Links</h3>
<p>CPackRPM supports packaging of symbolic links: </p>
<pre>execute_process(COMMAND ${CMAKE_COMMAND}
 -E create_symlink &lt;relative_path_location&gt; &lt;symlink_name&gt;)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/&lt;symlink_name&gt;
 DESTINATION &lt;symlink_location&gt; COMPONENT libraries)</pre>
<p>Symbolic links will be optimized (paths will be shortened if possible) before being added to the package or if multiple relocation paths are detected, a post install symlink relocation script will be generated. </p>
<p> Symbolic links may point to locations that are not packaged by the same package (either a different component or even not packaged at all) but those locations will be treated as if they were a part of the package while determining if symlink should be either created or present in a post install script &#8211; depending on relocation paths. </p>
<p> Symbolic links that point to locations outside packaging path produce a warning and are treated as non relocatable permanent symbolic links. </p>
<p> Currently there are a few limitations though:</p>
<dl>
<dt>&bull;</p>
<dd>For component based packaging component interdependency is not checked when processing symbolic links. Symbolic links pointing to content of a different component are treated the same way as if pointing to location that will not be packaged.</p>
<dt>&bull;</p>
<dd>Symbolic links pointing to a location through one or more intermediate symbolic links will not be handled differently &#8211; if the intermediate symbolic link(s) is also on a relocatable path, relocating it during package installation may cause initial symbolic link to point to an invalid location.</dl>
<h3>CPack</h3>
<p>Build binary and source package installers.</p>
<h3>Variables common to all CPack generators</h3>
<p>The CPack module generates binary and source installers in a variety of formats using the cpack program. Inclusion of the CPack module adds two new targets to the resulting makefiles, package and package_source, which build the binary and source installers, respectively. The generated binary installers contain everything installed via CMake&#8217;s INSTALL command (and the deprecated INSTALL_FILES, INSTALL_PROGRAMS, and INSTALL_TARGETS commands). </p>
<p> For certain kinds of binary installers (including the graphical installers on Mac OS X and Windows), CPack generates installers that allow users to select individual application components to install. See CPackComponent module for that. </p>
<p> The CPACK_GENERATOR variable has different meanings in different contexts. In your CMakeLists.txt file, CPACK_GENERATOR is a <i>list of generators</i>: when run with no other arguments, CPack will iterate over that list and produce one package for each generator. In a CPACK_PROJECT_CONFIG_FILE, though, CPACK_GENERATOR is a <i>string naming a single generator</i>. If you need per-cpack- generator logic to control <i>other</i> cpack settings, then you need a CPACK_PROJECT_CONFIG_FILE. </p>
<p> The CMake source tree itself contains a CPACK_PROJECT_CONFIG_FILE. See the top level file CMakeCPackOptions.cmake.in for an example. </p>
<p> If set, the CPACK_PROJECT_CONFIG_FILE is included automatically on a per-generator basis. It only need contain overrides. </p>
<p> Here&#8217;s how it works:</p>
<dl>
<dt>&bull;</p>
<dd>cpack runs</p>
<dt>&bull;</p>
<dd>it includes CPackConfig.cmake</p>
<dt>&bull;</p>
<dd>it iterates over the generators listed in that file&#8217;s CPACK_GENERATOR list variable (unless told to use just a specific one via -G on the command line&#8230;)</p>
<dt>&bull;</p>
<dd>foreach generator, it then</p>
<dt>&bull;</p>
<dd>sets CPACK_GENERATOR to the one currently being iterated</p>
<dt>&bull;</p>
<dd>includes the CPACK_PROJECT_CONFIG_FILE</p>
<dt>&bull;</p>
<dd>produces the package for that generator </p>
<p> This is the key: For each generator listed in CPACK_GENERATOR in CPackConfig.cmake, cpack will <i>reset</i> CPACK_GENERATOR internally to <i>the one currently being used</i> and then include the CPACK_PROJECT_CONFIG_FILE. </p>
<p> Before including this CPack module in your CMakeLists.txt file, there are a variety of variables that can be set to customize the resulting installers. The most commonly-used variables are:</p>
<dt><code>CPACK_PACKAGE_NAME</code></p>
<dd>The name of the package (or application). If not specified, defaults to the project name.</p>
<dt><code>CPACK_PACKAGE_VENDOR</code></p>
<dd>The name of the package vendor. (e.g., &quot;Kitware&quot;).</p>
<dt><code>CPACK_PACKAGE_DIRECTORY</code></p>
<dd>The directory in which CPack is doing its packaging. If it is not set then this will default (internally) to the build dir. This variable may be defined in CPack config file or from the cpack command line option &quot;-B&quot;. If set the command line option override the value found in the config file.</p>
<dt><code>CPACK_PACKAGE_VERSION_MAJOR</code></p>
<dd>Package major Version</p>
<dt><code>CPACK_PACKAGE_VERSION_MINOR</code></p>
<dd>Package minor Version</p>
<dt><code>CPACK_PACKAGE_VERSION_PATCH</code></p>
<dd>Package patch Version</p>
<dt><code>CPACK_PACKAGE_DESCRIPTION_FILE</code></p>
<dd>A text file used to describe the project. Used, for example, the introduction screen of a CPack-generated Windows installer to describe the project.</p>
<dt><code>CPACK_PACKAGE_DESCRIPTION_SUMMARY</code></p>
<dd>Short description of the project (only a few words).</p>
<dt><code>CPACK_PACKAGE_FILE_NAME</code></p>
<dd>The name of the package file to generate, not including the extension. For example, cmake-2.6.1-Linux-i686. The default value is: </p>
<pre>${CPACK_PACKAGE_NAME}-${CPACK_PACKAGE_VERSION}-${CPACK_SYSTEM_NAME}.</pre>
<dt><code>CPACK_PACKAGE_INSTALL_DIRECTORY</code></p>
<dd>Installation directory on the target system. This may be used by some CPack generators like NSIS to create an installation directory e.g., &quot;CMake 2.5&quot; below the installation prefix. All installed element will be put inside this directory.</p>
<dt><code>CPACK_PACKAGE_ICON</code></p>
<dd>A branding image that will be displayed inside the installer (used by GUI installers).</p>
<dt><code>CPACK_PROJECT_CONFIG_FILE</code></p>
<dd>CPack-time project CPack configuration file. This file included at cpack time, once per generator after CPack has set CPACK_GENERATOR to the actual generator being used. It allows per-generator setting of CPACK_* variables at cpack time.</p>
<dt><code>CPACK_RESOURCE_FILE_LICENSE</code></p>
<dd>License to be embedded in the installer. It will typically be displayed to the user by the produced installer (often with an explicit &quot;Accept&quot; button, for graphical installers) prior to installation. This license file is NOT added to installed file but is used by some CPack generators like NSIS. If you want to install a license file (may be the same as this one) along with your project you must add an appropriate CMake INSTALL command in your CMakeLists.txt.</p>
<dt><code>CPACK_RESOURCE_FILE_README</code></p>
<dd>ReadMe file to be embedded in the installer. It typically describes in some detail the purpose of the project during the installation. Not all CPack generators uses this file.</p>
<dt><code>CPACK_RESOURCE_FILE_WELCOME</code></p>
<dd>Welcome file to be embedded in the installer. It welcomes users to this installer. Typically used in the graphical installers on Windows and Mac OS X.</p>
<dt><code>CPACK_MONOLITHIC_INSTALL</code></p>
<dd>Disables the component-based installation mechanism. When set the component specification is ignored and all installed items are put in a single &quot;MONOLITHIC&quot; package. Some CPack generators do monolithic packaging by default and may be asked to do component packaging by setting CPACK_&lt;GENNAME&gt;_COMPONENT_INSTALL to 1/TRUE.</p>
<dt><code>CPACK_GENERATOR</code></p>
<dd>List of CPack generators to use. If not specified, CPack will create a set of options CPACK_BINARY_&lt;GENNAME&gt; (e.g., CPACK_BINARY_NSIS) allowing the user to enable/disable individual generators. This variable may be used on the command line as well as in: </p>
<pre>cpack -D CPACK_GENERATOR=&quot;ZIP;TGZ&quot; /path/to/build/tree</pre>
<dt><code>CPACK_OUTPUT_CONFIG_FILE</code></p>
<dd>The name of the CPack binary configuration file. This file is the CPack configuration generated by the CPack module for binary installers. Defaults to CPackConfig.cmake.</p>
<dt><code>CPACK_PACKAGE_EXECUTABLES</code></p>
<dd>Lists each of the executables and associated text label to be used to create Start Menu shortcuts. For example, setting this to the list ccmake;CMake will create a shortcut named &quot;CMake&quot; that will execute the installed executable ccmake. Not all CPack generators use it (at least NSIS, WIX and OSXX11 do).</p>
<dt><code>CPACK_STRIP_FILES</code></p>
<dd>List of files to be stripped. Starting with CMake 2.6.0 CPACK_STRIP_FILES will be a boolean variable which enables stripping of all files (a list of files evaluates to TRUE in CMake, so this change is compatible).</p>
<dt><code>CPACK_VERBATIM_VARIABLES</code></p>
<dd>If set to TRUE, values of variables prefixed with <i>CPACK</i> will be escaped before being written to the configuration files, so that the cpack program receives them exactly as they were specified. If not, characters like quotes and backslashes can cause parsing errors or alter the value received by the cpack program. Defaults to FALSE for backwards compatibility.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : FALSE </p>
<p> The following CPack variables are specific to source packages, and will not affect binary packages:</p>
<dt><code>CPACK_SOURCE_PACKAGE_FILE_NAME</code></p>
<dd>The name of the source package. For example cmake-2.6.1.</p>
<dt><code>CPACK_SOURCE_STRIP_FILES</code></p>
<dd>List of files in the source tree that will be stripped. Starting with CMake 2.6.0 CPACK_SOURCE_STRIP_FILES will be a boolean variable which enables stripping of all files (a list of files evaluates to TRUE in CMake, so this change is compatible).</p>
<dt><code>CPACK_SOURCE_GENERATOR</code></p>
<dd>List of generators used for the source packages. As with CPACK_GENERATOR, if this is not specified then CPack will create a set of options (e.g., CPACK_SOURCE_ZIP) allowing users to select which packages will be generated.</p>
<dt><code>CPACK_SOURCE_OUTPUT_CONFIG_FILE</code></p>
<dd>The name of the CPack source configuration file. This file is the CPack configuration generated by the CPack module for source installers. Defaults to CPackSourceConfig.cmake.</p>
<dt><code>CPACK_SOURCE_IGNORE_FILES</code></p>
<dd>Pattern of files in the source tree that won&#8217;t be packaged when building a source package. This is a list of regular expression patterns (that must be properly escaped), e.g., /CVS/;/\.svn/;\.swp$;\.#;/#;.*~;cscope.* </p>
<p> The following variables are for advanced uses of CPack:</p>
<dt><code>CPACK_CMAKE_GENERATOR</code></p>
<dd>What CMake generator should be used if the project is CMake project. Defaults to the value of CMAKE_GENERATOR few users will want to change this setting.</p>
<dt><code>CPACK_INSTALL_CMAKE_PROJECTS</code></p>
<dd>List of four values that specify what project to install. The four values are: Build directory, Project Name, Project Component, Directory. If omitted, CPack will build an installer that installs everything.</p>
<dt><code>CPACK_SYSTEM_NAME</code></p>
<dd>System name, defaults to the value of ${CMAKE_SYSTEM_NAME}.</p>
<dt><code>CPACK_PACKAGE_VERSION</code></p>
<dd>Package full version, used internally. By default, this is built from CPACK_PACKAGE_VERSION_MAJOR, CPACK_PACKAGE_VERSION_MINOR, and CPACK_PACKAGE_VERSION_PATCH.</p>
<dt><code>CPACK_TOPLEVEL_TAG</code></p>
<dd>Directory for the installed files.</p>
<dt><code>CPACK_INSTALL_COMMANDS</code></p>
<dd>Extra commands to install components.</p>
<dt><code>CPACK_INSTALLED_DIRECTORIES</code></p>
<dd>Extra directories to install.</p>
<dt><code>CPACK_PACKAGE_INSTALL_REGISTRY_KEY</code></p>
<dd>Registry key used when installing this project. This is only used by installer for Windows. The default value is based on the installation directory.</p>
<dt><code>CPACK_CREATE_DESKTOP_LINKS</code></p>
<dd>List of desktop links to create. Each desktop link requires a corresponding start menu shortcut as created by <code>CPACK_PACKAGE_EXECUTABLES</code>.</p>
<dt><code>CPACK_BINARY_&lt;GENNAME&gt;</code></p>
<dd>CPack generated options for binary generators. The CPack.cmake module generates (when CPACK_GENERATOR is not set) a set of CMake options (see CMake option command) which may then be used to select the CPack generator(s) to be used when launching the package target. </p>
<p> Provide options to choose generators we might check here if the required tools for the generates exist and set the defaults according to the results</dl>
<h3>CPackWIX</h3>
<p>CPack WiX generator specific options</p>
<h3>Variables specific to CPack WiX generator</h3>
<p>The following variables are specific to the installers built on Windows using WiX.</p>
<dl>
<dt><code>CPACK_WIX_UPGRADE_GUID</code></p>
<dd>Upgrade GUID (<code>Product/@UpgradeCode</code>) </p>
<p> Will be automatically generated unless explicitly provided. </p>
<p> It should be explicitly set to a constant generated globally unique identifier (GUID) to allow your installers to replace existing installations that use the same GUID. </p>
<p> You may for example explicitly set this variable in your CMakeLists.txt to the value that has been generated per default. You should not use GUIDs that you did not generate yourself or which may belong to other projects. </p>
<p> A GUID shall have the following fixed length syntax: </p>
<pre>XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX</pre>
<p>(each X represents an uppercase hexadecimal digit)</p>
<dt><code>CPACK_WIX_PRODUCT_GUID</code></p>
<dd>Product GUID (<code>Product/@Id</code>) </p>
<p> Will be automatically generated unless explicitly provided. </p>
<p> If explicitly provided this will set the Product Id of your installer. </p>
<p> The installer will abort if it detects a pre-existing installation that uses the same GUID. </p>
<p> The GUID shall use the syntax described for CPACK_WIX_UPGRADE_GUID.</p>
<dt><code>CPACK_WIX_LICENSE_RTF</code></p>
<dd>RTF License File </p>
<p> If CPACK_RESOURCE_FILE_LICENSE has an .rtf extension it is used as-is. </p>
<p> If CPACK_RESOURCE_FILE_LICENSE has an .txt extension it is implicitly converted to RTF by the WiX Generator. The expected encoding of the .txt file is UTF-8. </p>
<p> With CPACK_WIX_LICENSE_RTF you can override the license file used by the WiX Generator in case CPACK_RESOURCE_FILE_LICENSE is in an unsupported format or the .txt -&gt; .rtf conversion does not work as expected.</p>
<dt><code>CPACK_WIX_PRODUCT_ICON</code></p>
<dd>The Icon shown next to the program name in Add/Remove programs. </p>
<p> If set, this icon is used in place of the default icon.</p>
<dt><code>CPACK_WIX_UI_REF</code></p>
<dd>This variable allows you to override the Id of the <code>&lt;UIRef&gt;</code> element in the WiX template. </p>
<p> The default is <code>WixUI_InstallDir</code> in case no CPack components have been defined and <code>WixUI_FeatureTree</code> otherwise.</p>
<dt><code>CPACK_WIX_UI_BANNER</code></p>
<dd>The bitmap will appear at the top of all installer pages other than the welcome and completion dialogs. </p>
<p> If set, this image will replace the default banner image. </p>
<p> This image must be 493 by 58 pixels.</p>
<dt><code>CPACK_WIX_UI_DIALOG</code></p>
<dd>Background bitmap used on the welcome and completion dialogs. </p>
<p> If this variable is set, the installer will replace the default dialog image. </p>
<p> This image must be 493 by 312 pixels.</p>
<dt><code>CPACK_WIX_PROGRAM_MENU_FOLDER</code></p>
<dd>Start menu folder name for launcher. </p>
<p> If this variable is not set, it will be initialized with CPACK_PACKAGE_NAME</p>
<dt><code>CPACK_WIX_CULTURES</code></p>
<dd>Language(s) of the installer </p>
<p> Languages are compiled into the WixUI extension library. To use them, simply provide the name of the culture. If you specify more than one culture identifier in a comma or semicolon delimited list, the first one that is found will be used. You can find a list of supported languages at: <i><a rel="nofollow" href="http://wix.sourceforge.net/manual-wix3/WixUI_localization.htm">http://wix.sourceforge.net/manual-wix3/WixUI_localization.htm</a></i></p>
<dt><code>CPACK_WIX_TEMPLATE</code></p>
<dd>Template file for WiX generation </p>
<p> If this variable is set, the specified template will be used to generate the WiX wxs file. This should be used if further customization of the output is required. </p>
<p> If this variable is not set, the default MSI template included with CMake will be used.</p>
<dt><code>CPACK_WIX_PATCH_FILE</code></p>
<dd>Optional list of XML files with fragments to be inserted into generated WiX sources </p>
<p> This optional variable can be used to specify an XML file that the WiX generator will use to inject fragments into its generated source files. </p>
<p> Patch files understood by the CPack WiX generator roughly follow this RELAX NG compact schema: </p>
<pre>start = CPackWiXPatch
CPackWiXPatch = element CPackWiXPatch { CPackWiXFragment* }
CPackWiXFragment = element CPackWiXFragment
{
 attribute Id { string },
 fragmentContent*
}
fragmentContent = element * - CPackWiXFragment
{
 (attribute * { text } | text | fragmentContent)*
}</pre>
<p>Currently fragments can be injected into most Component, File and Directory elements. </p>
<p> The following additional special Ids can be used:</p>
<dt>&bull;</p>
<dd><code>#PRODUCT</code> for the <code>&lt;Product&gt;</code> element.</p>
<dt>&bull;</p>
<dd><code>#PRODUCTFEATURE</code> for the root <code>&lt;Feature&gt;</code> element. </p>
<p> The following example illustrates how this works. </p>
<p> Given that the WiX generator creates the following XML element: </p>
<pre>&lt;Component Id=&quot;CM_CP_applications.bin.my_libapp.exe&quot; Guid=&quot;*&quot;/&gt;</pre>
<p>The following XML patch file may be used to inject an Environment element into it: </p>
<pre>&lt;CPackWiXPatch&gt;
 &lt;CPackWiXFragment Id=&quot;CM_CP_applications.bin.my_libapp.exe&quot;&gt;
 &lt;Environment Id=&quot;MyEnvironment&quot; Action=&quot;set&quot;
 Name=&quot;MyVariableName&quot; Value=&quot;MyVariableValue&quot;/&gt;
 &lt;/CPackWiXFragment&gt;
&lt;/CPackWiXPatch&gt;</pre>
<dt><code>CPACK_WIX_EXTRA_SOURCES</code></p>
<dd>Extra WiX source files </p>
<p> This variable provides an optional list of extra WiX source files (.wxs) that should be compiled and linked. The full path to source files is required.</p>
<dt><code>CPACK_WIX_EXTRA_OBJECTS</code></p>
<dd>Extra WiX object files or libraries </p>
<p> This variable provides an optional list of extra WiX object (.wixobj) and/or WiX library (.wixlib) files. The full path to objects and libraries is required.</p>
<dt><code>CPACK_WIX_EXTENSIONS</code></p>
<dd>This variable provides a list of additional extensions for the WiX tools light and candle.</p>
<dt><code>CPACK_WIX_&lt;TOOL&gt;_EXTENSIONS</code></p>
<dd>This is the tool specific version of CPACK_WIX_EXTENSIONS. <code>&lt;TOOL&gt;</code> can be either LIGHT or CANDLE.</p>
<dt><code>CPACK_WIX_&lt;TOOL&gt;_EXTRA_FLAGS</code></p>
<dd>This list variable allows you to pass additional flags to the WiX tool <code>&lt;TOOL&gt;</code>. </p>
<p> Use it at your own risk. Future versions of CPack may generate flags which may be in conflict with your own flags. </p>
<p> <code>&lt;TOOL&gt;</code> can be either LIGHT or CANDLE.</p>
<dt><code>CPACK_WIX_CMAKE_PACKAGE_REGISTRY</code></p>
<dd>If this variable is set the generated installer will create an entry in the windows registry key <code>HKEY_LOCAL_MACHINE\Software\Kitware\CMake\Packages\&lt;package&gt;</code> The value for <code>&lt;package&gt;</code> is provided by this variable. </p>
<p> Assuming you also install a CMake configuration file this will allow other CMake projects to find your package with the <code>find_package()</code> command.</p>
<dt><code>CPACK_WIX_PROPERTY_&lt;PROPERTY&gt;</code></p>
<dd>This variable can be used to provide a value for the Windows Installer property <code>&lt;PROPERTY&gt;</code> </p>
<p> The following list contains some example properties that can be used to customize information under &quot;Programs and Features&quot; (also known as &quot;Add or Remove Programs&quot;)</p>
<dt>&bull;</p>
<dd>ARPCOMMENTS &#8211; Comments</p>
<dt>&bull;</p>
<dd>ARPHELPLINK &#8211; Help and support information URL</p>
<dt>&bull;</p>
<dd>ARPURLINFOABOUT &#8211; General information URL</p>
<dt>&bull;</p>
<dd>ARPURLUPDATEINFO &#8211; Update information URL</p>
<dt>&bull;</p>
<dd>ARPHELPTELEPHONE &#8211; Help and support telephone number</p>
<dt>&bull;</p>
<dd>ARPSIZE &#8211; Size (in kilobytes) of the application</dl>
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
<pre>set(CTEST_PROJECT_NAME &quot;MyProject&quot;)
set(CTEST_NIGHTLY_START_TIME &quot;01:00:00 UTC&quot;)
set(CTEST_DROP_METHOD &quot;http&quot;)
set(CTEST_DROP_SITE &quot;my.cdash.org&quot;)
set(CTEST_DROP_LOCATION &quot;/submit.php?project=MyProject&quot;)
set(CTEST_DROP_SITE_CDASH TRUE)</pre>
<p>(the CDash server can provide the file to a project administrator who configures <code>MyProject</code>). Settings in the config file are shared by both this <code>CTest</code> module and the <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> command-line <i>Dashboard Client</i> mode (<code>ctest -S</code>). </p>
<p> While building a project for submission to CDash, CTest scans the build output for errors and warnings and reports them with surrounding context from the build log. This generic approach works for all build tools, but does not give details about the command invocation that produced a given problem. One may get more detailed reports by setting the <code>CTEST_USE_LAUNCHERS</code> variable: </p>
<pre>set(CTEST_USE_LAUNCHERS 1)</pre>
<p>in the <code>CTestConfig.cmake</code> file.</p>
<h3>CTestCoverageCollectGCOV</h3>
<p>This module provides the <code>ctest_coverage_collect_gcov</code> function. </p>
<p> This function runs gcov on all .gcda files found in the binary tree and packages the resulting .gcov files into a tar file. This tarball also contains the following:</p>
<dl>
<dt>&bull;</p>
<dd><i>data.json</i> defines the source and build directories for use by CDash.</p>
<dt>&bull;</p>
<dd><i>Labels.json</i> indicates any <code>LABELS</code> that have been set on the source files.</p>
<dt>&bull;</p>
<dd>The <i>uncovered</i> directory holds any uncovered files found by <code>CTEST_EXTRA_COVERAGE_GLOB</code>. </p>
<p> After generating this tar file, it can be sent to CDash for display with the <code>ctest_submit(CDASH_UPLOAD)</code> command.</p>
<dt><code>cdash_coverage_collect_gcov</code></p>
<dd>
<pre>ctest_coverage_collect_gcov(TARBALL &lt;tarfile&gt;
 [SOURCE &lt;source_dir&gt;][BUILD &lt;build_dir&gt;]
 [GCOV_COMMAND &lt;gcov_command&gt;]
 [GCOV_OPTIONS &lt;options&gt;...]
 )</pre>
<p>Run gcov and package a tar file for CDash. The options are:</p>
<dt><code>TARBALL &lt;tarfile&gt;</code></p>
<dd>Specify the location of the <code>.tar</code> file to be created for later upload to CDash. Relative paths will be interpreted with respect to the top-level build directory.</p>
<dt><code>SOURCE &lt;source_dir&gt;</code></p>
<dd>Specify the top-level source directory for the build. Default is the value of <code>CTEST_SOURCE_DIRECTORY</code>.</p>
<dt><code>BUILD &lt;build_dir&gt;</code></p>
<dd>Specify the top-level build directory for the build. Default is the value of <code>CTEST_BINARY_DIRECTORY</code>.</p>
<dt><code>GCOV_COMMAND &lt;gcov_command&gt;</code></p>
<dd>Specify the full path to the <code>gcov</code> command on the machine. Default is the value of <code>CTEST_COVERAGE_COMMAND</code>.</p>
<dt><code>GCOV_OPTIONS &lt;options&gt;&#8230;</code></p>
<dd>Specify options to be passed to gcov. The <code>gcov</code> command is run as <code>gcov &lt;options&gt;&#8230; -o &lt;gcov-dir&gt; &lt;file&gt;.gcda</code>. If not specified, the default option is just <code>-b</code>.</p>
<dt><code>GLOB</code></p>
<dd>Recursively search for .gcda files in build_dir rather than determining search locations by reading TargetDirectories.txt.</p>
<dt><code>DELETE</code></p>
<dd>Delete coverage files after they&#8217;ve been packaged into the .tar.</p>
<dt><code>QUIET</code></p>
<dd>Suppress non-error messages that otherwise would have been printed out by this function.</dl>
<h3>CTestScriptMode</h3>
<p>This file is read by ctest in script mode (-S)</p>
<h3>CTestUseLaunchers</h3>
<p>Set the RULE_LAUNCH_* global properties when CTEST_USE_LAUNCHERS is on. </p>
<p> CTestUseLaunchers is automatically included when you include(CTest). However, it is split out into its own module file so projects can use the CTEST_USE_LAUNCHERS functionality independently. </p>
<p> To use launchers, set CTEST_USE_LAUNCHERS to ON in a ctest -S dashboard script, and then also set it in the cache of the configured project. Both cmake and ctest need to know the value of it for the launchers to work properly. CMake needs to know in order to generate proper build rules, and ctest, in order to produce the proper error and warning analysis. </p>
<p> For convenience, you may set the ENV variable CTEST_USE_LAUNCHERS_DEFAULT in your ctest -S script, too. Then, as long as your CMakeLists uses include(CTest) or include(CTestUseLaunchers), it will use the value of the ENV variable to initialize a CTEST_USE_LAUNCHERS cache variable. This cache variable initialization only occurs if CTEST_USE_LAUNCHERS is not already defined.</p>
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
<pre>WRITE_QT4_CONF(&lt;qt_conf_dir&gt; &lt;qt_conf_contents&gt;)</pre>
<p>Writes a qt.conf file with the &lt;qt_conf_contents&gt; into &lt;qt_conf_dir&gt;. </p>
<pre>RESOLVE_QT4_PATHS(&lt;paths_var&gt; [&lt;executable_path&gt;])</pre>
<p>Loop through &lt;paths_var&gt; list and if any don&#8217;t exist resolve them relative to the &lt;executable_path&gt; (if supplied) or the CMAKE_INSTALL_PREFIX. </p>
<pre>FIXUP_QT4_EXECUTABLE(&lt;executable&gt;
 [&lt;qtplugins&gt; &lt;libs&gt; &lt;dirs&gt; &lt;plugins_dir&gt; &lt;request_qt_conf&gt;])</pre>
<p>Copies Qt plugins, writes a Qt configuration file (if needed) and fixes up a Qt4 executable using BundleUtilities so it is standalone and can be drag-and-drop copied to another machine as long as all of the system libraries are compatible. </p>
<p> &lt;executable&gt; should point to the executable to be fixed-up. </p>
<p> &lt;qtplugins&gt; should contain a list of the names or paths of any Qt plugins to be installed. </p>
<p> &lt;libs&gt; will be passed to BundleUtilities and should be a list of any already installed plugins, libraries or executables to also be fixed-up. </p>
<p> &lt;dirs&gt; will be passed to BundleUtilities and should contain and directories to be searched to find library dependencies. </p>
<p> &lt;plugins_dir&gt; allows an custom plugins directory to be used. </p>
<p> &lt;request_qt_conf&gt; will force a qt.conf file to be written even if not needed. </p>
<pre>INSTALL_QT4_PLUGIN_PATH(plugin executable copy installed_plugin_path_var
 &lt;plugins_dir&gt; &lt;component&gt; &lt;configurations&gt;)</pre>
<p>Install (or copy) a resolved &lt;plugin&gt; to the default plugins directory (or &lt;plugins_dir&gt;) relative to &lt;executable&gt; and store the result in &lt;installed_plugin_path_var&gt;. </p>
<p> If &lt;copy&gt; is set to TRUE then the plugins will be copied rather than installed. This is to allow this module to be used at CMake time rather than install time. </p>
<p> If &lt;component&gt; is set then anything installed will use this COMPONENT. </p>
<pre>INSTALL_QT4_PLUGIN(plugin executable copy installed_plugin_path_var
 &lt;plugins_dir&gt; &lt;component&gt;)</pre>
<p>Install (or copy) an unresolved &lt;plugin&gt; to the default plugins directory (or &lt;plugins_dir&gt;) relative to &lt;executable&gt; and store the result in &lt;installed_plugin_path_var&gt;. See documentation of INSTALL_QT4_PLUGIN_PATH. </p>
<pre>INSTALL_QT4_EXECUTABLE(&lt;executable&gt;
 [&lt;qtplugins&gt; &lt;libs&gt; &lt;dirs&gt; &lt;plugins_dir&gt; &lt;request_qt_conf&gt; &lt;component&gt;])</pre>
<p>Installs Qt plugins, writes a Qt configuration file (if needed) and fixes up a Qt4 executable using BundleUtilities so it is standalone and can be drag-and-drop copied to another machine as long as all of the system libraries are compatible. The executable will be fixed-up at install time. &lt;component&gt; is the COMPONENT used for bundle fixup and plugin installation. See documentation of FIXUP_QT4_BUNDLE.</p>
<h3>Documentation</h3>
<p>DocumentationVTK.cmake </p>
<p> This file provides support for the VTK documentation framework. It relies on several tools (Doxygen, Perl, etc).</p>
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
 )</pre>
<p>It creates custom commands in the target as necessary to make data files available for each <code>DATA{}</code> reference previously evaluated by other functions provided by this module. Data files may be fetched from one of the URL templates specified in the <code>ExternalData_URL_TEMPLATES</code> variable, or may be found locally in one of the paths specified in the <code>ExternalData_OBJECT_STORES</code> variable.</dl>
<h3>Module Variables</h3>
<p>The following variables configure behavior. They should be set before calling any of the functions provided by this module.</p>
<dl>
<dt><code>ExternalData_BINARY_ROOT</code></p>
<dd>The <code>ExternalData_BINARY_ROOT</code> variable may be set to the directory to hold the real data files named by expanded <code>DATA{}</code> references. The default is <code>CMAKE_BINARY_DIR</code>. The directory layout will mirror that of content links under <code>ExternalData_SOURCE_ROOT</code>.</p>
<dt><code>ExternalData_CUSTOM_SCRIPT_&lt;key&gt;</code></p>
<dd>Specify a full path to a <code>.cmake</code> custom fetch script identified by <code>&lt;key&gt;</code> in entries of the <code>ExternalData_URL_TEMPLATES</code> list. See <i>Custom Fetch Scripts</i>.</p>
<dt><code>ExternalData_LINK_CONTENT</code></p>
<dd>The <code>ExternalData_LINK_CONTENT</code> variable may be set to the name of a supported hash algorithm to enable automatic conversion of real data files referenced by the <code>DATA{}</code> syntax into content links. For each such <code>&lt;file&gt;</code> a content link named <code>&lt;file&gt;&lt;ext&gt;</code> is created. The original file is renamed to the form <code>.ExternalData_&lt;algo&gt;_&lt;hash&gt;</code> to stage it for future transmission to one of the locations in the list of URL templates (by means outside the scope of this module). The data fetch rule created for the content link will use the staged object if it cannot be found using any URL template.</p>
<dt><code>ExternalData_NO_SYMLINKS</code></p>
<dd>The real data files named by expanded <code>DATA{}</code> references may be made available under <code>ExternalData_BINARY_ROOT</code> using symbolic links on some platforms. The <code>ExternalData_NO_SYMLINKS</code> variable may be set to disable use of symbolic links and enable use of copies instead.</p>
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
<dd>Specify a custom URL component to be substituted for URL template placeholders of the form <code>%(algo:&lt;key&gt;)</code>, where <code>&lt;key&gt;</code> is a valid C identifier, when fetching an object referenced via hash algorithm <code>&lt;algo&gt;</code>. If not defined, the default URL component is just <code>&lt;algo&gt;</code> for any <code>&lt;key&gt;</code>.</p>
<dt><code>ExternalData_URL_TEMPLATES</code></p>
<dd>The <code>ExternalData_URL_TEMPLATES</code> may be set to provide a list of of URL templates using the placeholders <code>%(algo)</code> and <code>%(hash)</code> in each template. Data fetch rules try each URL template in order by substituting the hash algorithm name for <code>%(algo)</code> and the hash value for <code>%(hash)</code>. Alternatively one may use <code>%(algo:&lt;key&gt;)</code> with <code>ExternalData_URL_ALGO_&lt;algo&gt;_&lt;key&gt;</code> variables to gain more flexibility in remote URLs.</dl>
<h3>Referencing Files</h3>
<h3>Referencing Single Files</h3>
<p>The <code>DATA{}</code> syntax is literal and the <code>&lt;name&gt;</code> is a full or relative path within the source tree. The source tree must contain either a real data file at <code>&lt;name&gt;</code> or a &quot;content link&quot; at <code>&lt;name&gt;&lt;ext&gt;</code> containing a hash of the real file using a hash algorithm corresponding to <code>&lt;ext&gt;</code>. For example, the argument <code>DATA{img.png}</code> may be satisfied by either a real <code>img.png</code> file in the current source directory or a <code>img.png.md5</code> file containing its MD5 sum.</p>
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
<p>The <code>DATA{}</code> syntax may reference a directory using a trailing slash and a list of associated files. The form <code>DATA{&lt;name&gt;/,&lt;opt1&gt;,&lt;opt2&gt;,&#8230;}</code> adds rules to fetch any files in the directory that match one of the associated file options. For example, the argument <code>DATA{MyDataDir/,REGEX:.*}</code> will pass the full path to a <code>MyDataDir</code> directory on the command line and ensure that the directory contains files corresponding to every file or content link in the <code>MyDataDir</code> source directory. In order to match associated files in subdirectories, specify a <code>RECURSE:</code> option, e.g. <code>DATA{MyDataDir/,RECURSE:,REGEX:.*}</code>.</p>
<h3>Hash Algorithms</h3>
<p>The following hash algorithms are supported: </p>
<pre>%(algo) &lt;ext&gt; Description
------- ----- -----------
MD5 .md5 Message-Digest Algorithm 5, RFC 1321
SHA1 .sha1 US Secure Hash Algorithm 1, RFC 3174
SHA224 .sha224 US Secure Hash Algorithms, RFC 4634
SHA256 .sha256 US Secure Hash Algorithms, RFC 4634
SHA384 .sha384 US Secure Hash Algorithms, RFC 4634
SHA512 .sha512 US Secure Hash Algorithms, RFC 4634</pre>
<p>Note that the hashes are used only for unique data identification and download verification.</p>
<h3>Custom Fetch Scripts</h3>
<p>When a data file must be fetched from one of the URL templates specified in the <code>ExternalData_URL_TEMPLATES</code> variable, it is normally downloaded using the <code>file(DOWNLOAD)</code> command. One may specify usage of a custom fetch script by using a URL template of the form <code>ExternalDataCustomScript://&lt;key&gt;/&lt;loc&gt;</code>. The <code>&lt;key&gt;</code> must be a C identifier, and the <code>&lt;loc&gt;</code> must contain the <code>%(algo)</code> and <code>%(hash)</code> placeholders. A variable corresponding to the key, <code>ExternalData_CUSTOM_SCRIPT_&lt;key&gt;</code>, must be set to the full path to a <code>.cmake</code> script file. The script will be included to perform the actual fetch, and provided with the following variables:</p>
<dl>
<dt><code>ExternalData_CUSTOM_LOCATION</code></p>
<dd>When a custom fetch script is loaded, this variable is set to the location part of the URL, which will contain the substituted hash algorithm name and content hash value.</p>
<dt><code>ExternalData_CUSTOM_FILE</code></p>
<dd>When a custom fetch script is loaded, this variable is set to the full path to a file in which the script must store the fetched content. The name of the file is unspecified and should not be interpreted in any way. </p>
<p> The custom fetch script is expected to store fetched content in the file or set a variable:</p>
<dt><code>ExternalData_CUSTOM_ERROR</code></p>
<dd>When a custom fetch script fails to fetch the requested content, it must set this variable to a short one-line message describing the reason for failure.</dl>
<h3>ExternalProject</h3>
<p>Create custom targets to build projects in external trees</p>
<dl>
<dt><code>ExternalProject_Add</code></p>
<dd>The <code>ExternalProject_Add</code> function creates a custom target to drive download, update/patch, configure, build, install and test steps of an external project: </p>
<pre>ExternalProject_Add(&lt;name&gt; [&lt;option&gt;...])</pre>
<p>General options are:</p>
<dt><code>DEPENDS &lt;projects&gt;&#8230;</code></p>
<dd>Targets on which the project depends</p>
<dt><code>PREFIX &lt;dir&gt;</code></p>
<dd>Root dir for entire project</p>
<dt><code>LIST_SEPARATOR &lt;sep&gt;</code></p>
<dd>Sep to be replaced by ; in cmd lines</p>
<dt><code>TMP_DIR &lt;dir&gt;</code></p>
<dd>Directory to store temporary files</p>
<dt><code>STAMP_DIR &lt;dir&gt;</code></p>
<dd>Directory to store step timestamps</p>
<dt><code>EXCLUDE_FROM_ALL 1</code></p>
<dd>The &quot;all&quot; target does not depend on this </p>
<p> Download step options are:</p>
<dt><code>DOWNLOAD_NAME &lt;fname&gt;</code></p>
<dd>File name to store (if not end of URL)</p>
<dt><code>DOWNLOAD_DIR &lt;dir&gt;</code></p>
<dd>Directory to store downloaded files</p>
<dt><code>DOWNLOAD_COMMAND &lt;cmd&gt;&#8230;</code></p>
<dd>Command to download source tree</p>
<dt><code>DOWNLOAD_NO_PROGRESS 1</code></p>
<dd>Disable download progress reports</p>
<dt><code>CVS_REPOSITORY &lt;cvsroot&gt;</code></p>
<dd>CVSROOT of CVS repository</p>
<dt><code>CVS_MODULE &lt;mod&gt;</code></p>
<dd>Module to checkout from CVS repo</p>
<dt><code>CVS_TAG &lt;tag&gt;</code></p>
<dd>Tag to checkout from CVS repo</p>
<dt><code>SVN_REPOSITORY &lt;url&gt;</code></p>
<dd>URL of Subversion repo</p>
<dt><code>SVN_REVISION -r&lt;rev&gt;</code></p>
<dd>Revision to checkout from Subversion repo</p>
<dt><code>SVN_USERNAME &lt;username&gt;</code></p>
<dd>Username for Subversion checkout and update</p>
<dt><code>SVN_PASSWORD &lt;password&gt;</code></p>
<dd>Password for Subversion checkout and update</p>
<dt><code>SVN_TRUST_CERT 1</code></p>
<dd>Trust the Subversion server site certificate</p>
<dt><code>GIT_REPOSITORY &lt;url&gt;</code></p>
<dd>URL of git repo</p>
<dt><code>GIT_TAG &lt;tag&gt;</code></p>
<dd>Git branch name, commit id or tag</p>
<dt><code>GIT_REMOTE_NAME &lt;name&gt;</code></p>
<dd>The optional name of the remote, default to <code>origin</code></p>
<dt><code>GIT_SUBMODULES &lt;module&gt;&#8230;</code></p>
<dd>Git submodules that shall be updated, all if empty</p>
<dt><code>GIT_SHALLOW 1</code></p>
<dd>Tell Git to clone with <code>&#8211;depth 1</code>. Use when <code>GIT_TAG</code> is not specified or when it names a branch in order to download only the tip of the branch without the rest of its history.</p>
<dt><code>HG_REPOSITORY &lt;url&gt;</code></p>
<dd>URL of mercurial repo</p>
<dt><code>HG_TAG &lt;tag&gt;</code></p>
<dd>Mercurial branch name, commit id or tag</p>
<dt><code>URL /&#8230;/src.tgz</code></p>
<dd>Full path or URL of source</p>
<dt><code>URL_HASH ALGO=value</code></p>
<dd>Hash of file at URL</p>
<dt><code>URL_MD5 md5</code></p>
<dd>Equivalent to URL_HASH MD5=md5</p>
<dt><code>TLS_VERIFY &lt;bool&gt;</code></p>
<dd>Should certificate for https be checked</p>
<dt><code>TLS_CAINFO &lt;file&gt;</code></p>
<dd>Path to a certificate authority file</p>
<dt><code>TIMEOUT &lt;seconds&gt;</code></p>
<dd>Time allowed for file download operations</p>
<dt><code>DOWNLOAD_NO_EXTRACT 1</code></p>
<dd>Just download the file and do not extract it; the full path to the downloaded file is available as <code>&lt;DOWNLOADED_FILE&gt;</code>. </p>
<p> Update/Patch step options are:</p>
<dt><code>UPDATE_COMMAND &lt;cmd&gt;&#8230;</code></p>
<dd>Source work-tree update command</p>
<dt><code>UPDATE_DISCONNECTED 1</code></p>
<dd>Never update automatically from the remote repository</p>
<dt><code>PATCH_COMMAND &lt;cmd&gt;&#8230;</code></p>
<dd>Command to patch downloaded source </p>
<p> Configure step options are:</p>
<dt><code>SOURCE_DIR &lt;dir&gt;</code></p>
<dd>Source dir to be used for build</p>
<dt><code>CONFIGURE_COMMAND &lt;cmd&gt;&#8230;</code></p>
<dd>Build tree configuration command</p>
<dt><code>CMAKE_COMMAND /&#8230;/cmake</code></p>
<dd>Specify alternative cmake executable</p>
<dt><code>CMAKE_GENERATOR &lt;gen&gt;</code></p>
<dd>Specify generator for native build</p>
<dt><code>CMAKE_GENERATOR_PLATFORM &lt;platform&gt;</code></p>
<dd>Generator-specific platform name</p>
<dt><code>CMAKE_GENERATOR_TOOLSET &lt;toolset&gt;</code></p>
<dd>Generator-specific toolset name</p>
<dt><code>CMAKE_ARGS &lt;arg&gt;&#8230;</code></p>
<dd>Arguments to CMake command line. These arguments are passed to CMake command line, and can contain arguments other than cache values, see also <code>CMake Options</code>. Arguments in the form <code>-Dvar:string=on</code> are always passed to the command line, and therefore cannot be changed by the user. Arguments may use <code>generator expressions</code>.</p>
<dt><code>CMAKE_CACHE_ARGS &lt;arg&gt;&#8230;</code></p>
<dd>Initial cache arguments, of the form <code>-Dvar:string=on</code>. These arguments are written in a pre-load a script that populates CMake cache, see also <code>cmake -C</code>. This allows one to overcome command line length limits. These arguments are <code>set()</code> using the <code>FORCE</code> argument, and therefore cannot be changed by the user. Arguments may use <code>generator expressions</code>.</p>
<dt><code>CMAKE_CACHE_DEFAULT_ARGS &lt;arg&gt;&#8230;</code></p>
<dd>Initial default cache arguments, of the form <code>-Dvar:string=on</code>. These arguments are written in a pre-load a script that populates CMake cache, see also <code>cmake -C</code>. This allows one to overcome command line length limits. These arguments can be used as default value that will be set if no previous value is found in the cache, and that the user can change later. Arguments may use <code>generator expressions</code>. </p>
<p> Build step options are:</p>
<dt><code>BINARY_DIR &lt;dir&gt;</code></p>
<dd>Specify build dir location</p>
<dt><code>BUILD_COMMAND &lt;cmd&gt;&#8230;</code></p>
<dd>Command to drive the native build</p>
<dt><code>BUILD_IN_SOURCE 1</code></p>
<dd>Use source dir for build dir</p>
<dt><code>BUILD_ALWAYS 1</code></p>
<dd>No stamp file, build step always runs</p>
<dt><code>BUILD_BYPRODUCTS &lt;file&gt;&#8230;</code></p>
<dd>Files that will be generated by the build command but may or may not have their modification time updated by subsequent builds. </p>
<p> Install step options are:</p>
<dt><code>INSTALL_DIR &lt;dir&gt;</code></p>
<dd>Installation prefix</p>
<dt><code>INSTALL_COMMAND &lt;cmd&gt;&#8230;</code></p>
<dd>Command to drive install after build </p>
<p> Test step options are:</p>
<dt><code>TEST_BEFORE_INSTALL 1</code></p>
<dd>Add test step executed before install step</p>
<dt><code>TEST_AFTER_INSTALL 1</code></p>
<dd>Add test step executed after install step</p>
<dt><code>TEST_EXCLUDE_FROM_MAIN 1</code></p>
<dd>Main target does not depend on the test step</p>
<dt><code>TEST_COMMAND &lt;cmd&gt;&#8230;</code></p>
<dd>Command to drive test </p>
<p> Output logging options are:</p>
<dt><code>LOG_DOWNLOAD 1</code></p>
<dd>Wrap download in script to log output</p>
<dt><code>LOG_UPDATE 1</code></p>
<dd>Wrap update in script to log output</p>
<dt><code>LOG_CONFIGURE 1</code></p>
<dd>Wrap configure in script to log output</p>
<dt><code>LOG_BUILD 1</code></p>
<dd>Wrap build in script to log output</p>
<dt><code>LOG_TEST 1</code></p>
<dd>Wrap test in script to log output</p>
<dt><code>LOG_INSTALL 1</code></p>
<dd>Wrap install in script to log output </p>
<p> Steps can be given direct access to the terminal if possible. With the <code>Ninja</code> generator, this places the steps in the <code>console</code> <code>pool</code>. Options are:</p>
<dt><code>USES_TERMINAL_DOWNLOAD 1</code></p>
<dd>Give download terminal access.</p>
<dt><code>USES_TERMINAL_UPDATE 1</code></p>
<dd>Give update terminal access.</p>
<dt><code>USES_TERMINAL_CONFIGURE 1</code></p>
<dd>Give configure terminal access.</p>
<dt><code>USES_TERMINAL_BUILD 1</code></p>
<dd>Give build terminal access.</p>
<dt><code>USES_TERMINAL_TEST 1</code></p>
<dd>Give test terminal access.</p>
<dt><code>USES_TERMINAL_INSTALL 1</code></p>
<dd>Give install terminal access. </p>
<p> Other options are:</p>
<dt><code>STEP_TARGETS &lt;step-target&gt;&#8230;</code></p>
<dd>Generate custom targets for these steps</p>
<dt><code>INDEPENDENT_STEP_TARGETS &lt;step-target&gt;&#8230;</code></p>
<dd>Generate custom targets for these steps that do not depend on other external projects even if a dependency is set </p>
<p> The <code>*_DIR</code> options specify directories for the project, with default directories computed as follows. If the <code>PREFIX</code> option is given to <code>ExternalProject_Add()</code> or the <code>EP_PREFIX</code> directory property is set, then an external project is built and installed under the specified prefix: </p>
<pre>TMP_DIR = &lt;prefix&gt;/tmp
STAMP_DIR = &lt;prefix&gt;/src/&lt;name&gt;-stamp
DOWNLOAD_DIR = &lt;prefix&gt;/src
SOURCE_DIR = &lt;prefix&gt;/src/&lt;name&gt;
BINARY_DIR = &lt;prefix&gt;/src/&lt;name&gt;-build
INSTALL_DIR = &lt;prefix&gt;</pre>
<p>Otherwise, if the <code>EP_BASE</code> directory property is set then components of an external project are stored under the specified base: </p>
<pre>TMP_DIR = &lt;base&gt;/tmp/&lt;name&gt;
STAMP_DIR = &lt;base&gt;/Stamp/&lt;name&gt;
DOWNLOAD_DIR = &lt;base&gt;/Download/&lt;name&gt;
SOURCE_DIR = &lt;base&gt;/Source/&lt;name&gt;
BINARY_DIR = &lt;base&gt;/Build/&lt;name&gt;
INSTALL_DIR = &lt;base&gt;/Install/&lt;name&gt;</pre>
<p>If no <code>PREFIX</code>, <code>EP_PREFIX</code>, or <code>EP_BASE</code> is specified then the default is to set <code>PREFIX</code> to <code>&lt;name&gt;-prefix</code>. Relative paths are interpreted with respect to the build directory corresponding to the source directory in which <code>ExternalProject_Add</code> is invoked. </p>
<p> If <code>SOURCE_DIR</code> is explicitly set to an existing directory the project will be built from it. Otherwise a download step must be specified using one of the <code>DOWNLOAD_COMMAND</code>, <code>CVS_*</code>, <code>SVN_*</code>, or <code>URL</code> options. The <code>URL</code> option may refer locally to a directory or source tarball, or refer to a remote tarball (e.g. <code><a rel="nofollow" href="http://.../src.tgz">http://&#8230;/src.tgz</a></code>). </p>
<p> If <code>UPDATE_DISCONNECTED</code> is set, the update step is not executed automatically when building the main target. The update step can still be added as a step target and called manually. This is useful if you want to allow one to build the project when you are disconnected from the network (you might still need the network for the download step). This is disabled by default. The directory property <code>EP_UPDATE_DISCONNECTED</code> can be used to change the default value for all the external projects in the current directory and its subdirectories.</p>
<dt><code>ExternalProject_Add_Step</code></p>
<dd>The <code>ExternalProject_Add_Step</code> function adds a custom step to an external project: </p>
<pre>ExternalProject_Add_Step(&lt;name&gt; &lt;step&gt; [&lt;option&gt;...])</pre>
<p>Options are:</p>
<dt><code>COMMAND &lt;cmd&gt;&#8230;</code></p>
<dd>Command line invoked by this step</p>
<dt><code>COMMENT &lt;text&gt;&#8230;</code></p>
<dd>Text printed when step executes</p>
<dt><code>DEPENDEES &lt;step&gt;&#8230;</code></p>
<dd>Steps on which this step depends</p>
<dt><code>DEPENDERS &lt;step&gt;&#8230;</code></p>
<dd>Steps that depend on this step</p>
<dt><code>DEPENDS &lt;file&gt;&#8230;</code></p>
<dd>Files on which this step depends</p>
<dt><code>BYPRODUCTS &lt;file&gt;&#8230;</code></p>
<dd>Files that will be generated by this step but may or may not have their modification time updated by subsequent builds.</p>
<dt><code>ALWAYS 1</code></p>
<dd>No stamp file, step always runs</p>
<dt><code>EXCLUDE_FROM_MAIN 1</code></p>
<dd>Main target does not depend on this step</p>
<dt><code>WORKING_DIRECTORY &lt;dir&gt;</code></p>
<dd>Working directory for command</p>
<dt><code>LOG 1</code></p>
<dd>Wrap step in script to log output</p>
<dt><code>USES_TERMINAL 1</code></p>
<dd>Give the step direct access to the terminal if possible. </p>
<p> The command line, comment, working directory, and byproducts of every standard and custom step are processed to replace tokens <code>&lt;SOURCE_DIR&gt;</code>, <code>&lt;BINARY_DIR&gt;</code>, <code>&lt;INSTALL_DIR&gt;</code>, and <code>&lt;TMP_DIR&gt;</code> with corresponding property values. </p>
<p> Any builtin step that specifies a <code>&lt;step&gt;_COMMAND cmd&#8230;</code> or custom step that specifies a <code>COMMAND cmd&#8230;</code> may specify additional command lines using the form <code>COMMAND cmd&#8230;</code>. At build time the commands will be executed in order and aborted if any one fails. For example: </p>
<pre>... BUILD_COMMAND make COMMAND echo done ...</pre>
<p>specifies to run <code>make</code> and then <code>echo done</code> during the build step. Whether the current working directory is preserved between commands is not defined. Behavior of shell operators like <code>&amp;&amp;</code> is not defined. </p>
<p> Arguments to <code>&lt;step&gt;_COMMAND</code> or <code>COMMAND</code> options may use <code>generator expressions</code>.</p>
<dt><code>ExternalProject_Get_Property</code></p>
<dd>The <code>ExternalProject_Get_Property</code> function retrieves external project target properties: </p>
<pre>ExternalProject_Get_Property(&lt;name&gt; [prop1 [prop2 [...]]])</pre>
<p>It stores property values in variables of the same name. Property names correspond to the keyword argument names of <code>ExternalProject_Add</code>.</p>
<dt><code>ExternalProject_Add_StepTargets</code></p>
<dd>The <code>ExternalProject_Add_StepTargets</code> function generates custom targets for the steps listed: </p>
<pre>ExternalProject_Add_StepTargets(&lt;name&gt; [NO_DEPENDS] [step1 [step2 [...]]])</pre>
<p>If <code>NO_DEPENDS</code> is set, the target will not depend on the dependencies of the complete project. This is usually safe to use for the download, update, and patch steps that do not require that all the dependencies are updated and built. Using <code>NO_DEPENDS</code> for other of the default steps might break parallel builds, so you should avoid, it. For custom steps, you should consider whether or not the custom commands requires that the dependencies are configured, built and installed. </p>
<p> If <code>STEP_TARGETS</code> or <code>INDEPENDENT_STEP_TARGETS</code> is set then <code>ExternalProject_Add_StepTargets</code> is automatically called at the end of matching calls to <code>ExternalProject_Add_Step</code>. Pass <code>STEP_TARGETS</code> or <code>INDEPENDENT_STEP_TARGETS</code> explicitly to individual <code>ExternalProject_Add</code> calls, or implicitly to all <code>ExternalProject_Add</code> calls by setting the directory properties <code>EP_STEP_TARGETS</code> and <code>EP_INDEPENDENT_STEP_TARGETS</code>. The <code>INDEPENDENT</code> version of the argument and of the property will call <code>ExternalProject_Add_StepTargets</code> with the <code>NO_DEPENDS</code> argument. </p>
<p> If <code>STEP_TARGETS</code> and <code>INDEPENDENT_STEP_TARGETS</code> are not set, clients may still manually call <code>ExternalProject_Add_StepTargets</code> after calling <code>ExternalProject_Add</code> or <code>ExternalProject_Add_Step</code>. </p>
<p> This functionality is provided to make it easy to drive the steps independently of each other by specifying targets on build command lines. For example, you may be submitting to a sub-project based dashboard, where you want to drive the configure portion of the build, then submit to the dashboard, followed by the build portion, followed by tests. If you invoke a custom target that depends on a step halfway through the step dependency chain, then all the previous steps will also run to ensure everything is up to date. </p>
<p> For example, to drive configure, build and test steps independently for each <code>ExternalProject_Add</code> call in your project, write the following line prior to any <code>ExternalProject_Add</code> calls in your <code>CMakeLists.txt</code> file: </p>
<pre>set_property(DIRECTORY PROPERTY EP_STEP_TARGETS configure build test)</pre>
<dt><code>ExternalProject_Add_StepDependencies</code></p>
<dd>The <code>ExternalProject_Add_StepDependencies</code> function add some dependencies for some external project step: </p>
<pre>ExternalProject_Add_StepDependencies(&lt;name&gt; &lt;step&gt; [target1 [target2 [...]]])</pre>
<p>This function takes care to set both target and file level dependencies, and will ensure that parallel builds will not break. It should be used instead of <code>add_dependencies()</code> when adding a dependency for some of the step targets generated by <code>ExternalProject</code>.</dl>
<h3>FeatureSummary</h3>
<p>Macros for generating a summary of enabled/disabled features </p>
<p> This module provides the macros feature_summary(), set_package_properties() and add_feature_info(). For compatibility it also still provides set_package_info(), set_feature_info(), print_enabled_features() and print_disabled_features(). </p>
<p> These macros can be used to generate a summary of enabled and disabled packages and/or feature for a build tree: </p>
<pre>-- The following OPTIONAL packages have been found:
LibXml2 (required version &gt;= 2.4), XML processing lib, &lt;<a rel="nofollow" href="http://xmlsoft.org">http://xmlsoft.org</a>&gt;
 * Enables HTML-import in MyWordProcessor
 * Enables odt-export in MyWordProcessor
PNG , A PNG image library. , &lt;<a rel="nofollow" href="http://www.libpng.org/pub/png/">http://www.libpng.org/pub/png/</a>&gt;
 * Enables saving screenshots
-- The following OPTIONAL packages have not been found:
Lua51 , The Lua scripting language. , &lt;<a rel="nofollow" href="http://www.lua.org">http://www.lua.org</a>&gt;
 * Enables macros in MyWordProcessor
Foo , Foo provides cool stuff.</pre>
<pre>FEATURE_SUMMARY( [FILENAME &lt;file&gt;]
 [APPEND]
 [VAR &lt;variable_name&gt;]
 [INCLUDE_QUIET_PACKAGES]
 [FATAL_ON_MISSING_REQUIRED_PACKAGES]
 [DESCRIPTION &quot;Found packages:&quot;]
 WHAT (ALL | PACKAGES_FOUND | PACKAGES_NOT_FOUND
 | ENABLED_FEATURES | DISABLED_FEATURES)
 )</pre>
<p>The FEATURE_SUMMARY() macro can be used to print information about enabled or disabled packages or features of a project. By default, only the names of the features/packages will be printed and their required version when one was specified. Use SET_PACKAGE_PROPERTIES() to add more useful information, like e.g. a download URL for the respective package or their purpose in the project. </p>
<p> The WHAT option is the only mandatory option. Here you specify what information will be printed:</p>
<dl>
<dt><code>ALL</code></p>
<dd>print everything</p>
<dt><code>ENABLED_FEATURES</code></p>
<dd>the list of all features which are enabled</p>
<dt><code>DISABLED_FEATURES</code></p>
<dd>the list of all features which are disabled</p>
<dt><code>PACKAGES_FOUND</code></p>
<dd>the list of all packages which have been found</p>
<dt><code>PACKAGES_NOT_FOUND</code></p>
<dd>the list of all packages which have not been found</p>
<dt><code>OPTIONAL_PACKAGES_FOUND</code></p>
<dd>only those packages which have been found which have the type OPTIONAL</p>
<dt><code>OPTIONAL_PACKAGES_NOT_FOUND</code></p>
<dd>only those packages which have not been found which have the type OPTIONAL</p>
<dt><code>RECOMMENDED_PACKAGES_FOUND</code></p>
<dd>only those packages which have been found which have the type RECOMMENDED</p>
<dt><code>RECOMMENDED_PACKAGES_NOT_FOUND</code></p>
<dd>only those packages which have not been found which have the type RECOMMENDED</p>
<dt><code>REQUIRED_PACKAGES_FOUND</code></p>
<dd>only those packages which have been found which have the type REQUIRED</p>
<dt><code>REQUIRED_PACKAGES_NOT_FOUND</code></p>
<dd>only those packages which have not been found which have the type REQUIRED</p>
<dt><code>RUNTIME_PACKAGES_FOUND</code></p>
<dd>only those packages which have been found which have the type RUNTIME</p>
<dt><code>RUNTIME_PACKAGES_NOT_FOUND</code></p>
<dd>only those packages which have not been found which have the type RUNTIME </p>
<p> With the exception of the <code>ALL</code> value, these values can be combined in order to customize the output. For example: </p>
<pre>feature_summary(WHAT ENABLED_FEATURES DISABLED_FEATURES)</pre>
<p>If a FILENAME is given, the information is printed into this file. If APPEND is used, it is appended to this file, otherwise the file is overwritten if it already existed. If the VAR option is used, the information is &quot;printed&quot; into the specified variable. If FILENAME is not used, the information is printed to the terminal. Using the DESCRIPTION option a description or headline can be set which will be printed above the actual content. If INCLUDE_QUIET_PACKAGES is given, packages which have been searched with find_package(&#8230; QUIET) will also be listed. By default they are skipped. If FATAL_ON_MISSING_REQUIRED_PACKAGES is given, CMake will abort if a package which is marked as REQUIRED has not been found. </p>
<p> Example 1, append everything to a file: </p>
<pre>feature_summary(WHAT ALL
 FILENAME ${CMAKE_BINARY_DIR}/all.log APPEND)</pre>
<p>Example 2, print the enabled features into the variable enabledFeaturesText, including QUIET packages: </p>
<pre>feature_summary(WHAT ENABLED_FEATURES
 INCLUDE_QUIET_PACKAGES
 DESCRIPTION &quot;Enabled Features:&quot;
 VAR enabledFeaturesText)
message(STATUS &quot;${enabledFeaturesText}&quot;)</pre>
<pre>SET_PACKAGE_PROPERTIES(&lt;name&gt; PROPERTIES
 [ URL &lt;url&gt; ]
 [ DESCRIPTION &lt;description&gt; ]
 [ TYPE (RUNTIME|OPTIONAL|RECOMMENDED|REQUIRED) ]
 [ PURPOSE &lt;purpose&gt; ]
 )</pre>
<p>Use this macro to set up information about the named package, which can then be displayed via FEATURE_SUMMARY(). This can be done either directly in the Find-module or in the project which uses the module after the find_package() call. The features for which information can be set are added automatically by the find_package() command. </p>
<p> URL: this should be the homepage of the package, or something similar. Ideally this is set already directly in the Find-module. </p>
<p> DESCRIPTION: A short description what that package is, at most one sentence. Ideally this is set already directly in the Find-module. </p>
<p> TYPE: What type of dependency has the using project on that package. Default is OPTIONAL. In this case it is a package which can be used by the project when available at buildtime, but it also work without. RECOMMENDED is similar to OPTIONAL, i.e. the project will build if the package is not present, but the functionality of the resulting binaries will be severly limited. If a REQUIRED package is not available at buildtime, the project may not even build. This can be combined with the FATAL_ON_MISSING_REQUIRED_PACKAGES argument for feature_summary(). Last, a RUNTIME package is a package which is actually not used at all during the build, but which is required for actually running the resulting binaries. So if such a package is missing, the project can still be built, but it may not work later on. If set_package_properties() is called multiple times for the same package with different TYPEs, the TYPE is only changed to higher TYPEs ( RUNTIME &lt; OPTIONAL &lt; RECOMMENDED &lt; REQUIRED ), lower TYPEs are ignored. The TYPE property is project-specific, so it cannot be set by the Find-module, but must be set in the project. </p>
<p> PURPOSE: This describes which features this package enables in the project, i.e. it tells the user what functionality he gets in the resulting binaries. If set_package_properties() is called multiple times for a package, all PURPOSE properties are appended to a list of purposes of the package in the project. As the TYPE property, also the PURPOSE property is project-specific, so it cannot be set by the Find-module, but must be set in the project. </p>
<p> Example for setting the info for a package: </p>
<pre>find_package(LibXml2)
set_package_properties(LibXml2 PROPERTIES
 DESCRIPTION &quot;A XML processing library.&quot;
 URL &quot;<a rel="nofollow" href="http://xmlsoft.org/">http://xmlsoft.org/</a>&quot;)</pre>
<pre>set_package_properties(LibXml2 PROPERTIES
 TYPE RECOMMENDED
 PURPOSE &quot;Enables HTML-import in MyWordProcessor&quot;)
...
set_package_properties(LibXml2 PROPERTIES
 TYPE OPTIONAL
 PURPOSE &quot;Enables odt-export in MyWordProcessor&quot;)</pre>
<pre>find_package(DBUS)
set_package_properties(DBUS PROPERTIES
 TYPE RUNTIME
 PURPOSE &quot;Necessary to disable the screensaver during a presentation&quot; )</pre>
<pre>ADD_FEATURE_INFO(&lt;name&gt; &lt;enabled&gt; &lt;description&gt;)</pre>
<p>Use this macro to add information about a feature with the given &lt;name&gt;. &lt;enabled&gt; contains whether this feature is enabled or not, &lt;description&gt; is a text describing the feature. The information can be displayed using feature_summary() for ENABLED_FEATURES and DISABLED_FEATURES respectively. </p>
<p> Example for setting the info for a feature: </p>
<pre>option(WITH_FOO &quot;Help for foo&quot; ON)
add_feature_info(Foo WITH_FOO &quot;The Foo feature provides very cool stuff.&quot;)</pre>
<p>The following macros are provided for compatibility with previous CMake versions: </p>
<pre>SET_PACKAGE_INFO(&lt;name&gt; &lt;description&gt; [&lt;url&gt; [&lt;purpose&gt;] ] )</pre>
<p>Use this macro to set up information about the named package, which can then be displayed via FEATURE_SUMMARY(). This can be done either directly in the Find-module or in the project which uses the module after the find_package() call. The features for which information can be set are added automatically by the find_package() command. </p>
<pre>PRINT_ENABLED_FEATURES()</pre>
<p>Does the same as FEATURE_SUMMARY(WHAT ENABLED_FEATURES DESCRIPTION &quot;Enabled features:&quot;) </p>
<pre>PRINT_DISABLED_FEATURES()</pre>
<p>Does the same as FEATURE_SUMMARY(WHAT DISABLED_FEATURES DESCRIPTION &quot;Disabled features:&quot;) </p>
<pre>SET_FEATURE_INFO(&lt;name&gt; &lt;description&gt; [&lt;url&gt;] )</pre>
<p>Does the same as SET_PACKAGE_INFO(&lt;name&gt; &lt;description&gt; &lt;url&gt; )</dl>
<h3>FindALSA</h3>
<p>Find alsa </p>
<p> Find the alsa libraries (asound) </p>
<pre>This module defines the following variables:
 ALSA_FOUND - True if ALSA_INCLUDE_DIR &amp; ALSA_LIBRARY are found
 ALSA_LIBRARIES - Set when ALSA_LIBRARY is found
 ALSA_INCLUDE_DIRS - Set when ALSA_INCLUDE_DIR is found</pre>
<pre>ALSA_INCLUDE_DIR - where to find asoundlib.h, etc.
ALSA_LIBRARY - the asound library
ALSA_VERSION_STRING - the version of alsa found (since CMake 2.8.8)</pre>
<h3>FindArmadillo</h3>
<p>Find Armadillo </p>
<p> Find the Armadillo C++ library </p>
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
<p> AVIFILE (<i><a rel="nofollow" href="http://avifile.sourceforge.net/)is">http://avifile.sourceforge.net/)is</a></i> a set of libraries for i386 machines to use various AVI codecs. Support is limited beyond Linux. Windows provides native AVI support, and so doesn&#8217;t need this library. This module defines </p>
<pre>AVIFILE_INCLUDE_DIR, where to find avifile.h , etc.
AVIFILE_LIBRARIES, the libraries to link against
AVIFILE_DEFINITIONS, definitions to use when compiling
AVIFILE_FOUND, If false, don't try to use AVIFILE</pre>
<h3>FindBISON</h3>
<p>Find <code>bison</code> executable and provide a macro to generate custom build rules. </p>
<p> The module defines the following variables:</p>
<dl>
<dt><code>BISON_EXECUTABLE</code></p>
<dd>path to the <code>bison</code> program</p>
<dt><code>BISON_VERSION</code></p>
<dd>version of <code>bison</code></p>
<dt><code>BISON_FOUND</code></p>
<dd>true if the program was found </p>
<p> The minimum required version of <code>bison</code> can be specified using the standard CMake syntax, e.g. <code>find_package(BISON 2.1.3)</code>. </p>
<p> If <code>bison</code> is found, the module defines the macro: </p>
<pre>BISON_TARGET(&lt;Name&gt; &lt;YaccInput&gt; &lt;CodeOutput&gt;
 [COMPILE_FLAGS &lt;flags&gt;]
 [DEFINES_FILE &lt;file&gt;]
 [VERBOSE &lt;file&gt;]
 )</pre>
<p>which will create a custom rule to generate a parser. <code>&lt;YaccInput&gt;</code> is the path to a yacc file. <code>&lt;CodeOutput&gt;</code> is the name of the source file generated by bison. A header file is also be generated, and contains the token list. </p>
<p> The options are:</p>
<dt><code>COMPILE_FLAGS &lt;flags&gt;</code></p>
<dd>Specify flags to be added to the <code>bison</code> command line.</p>
<dt><code>DEFINES_FILE &lt;file&gt;</code></p>
<dd>Specify a non-default header <code>&lt;file&gt;</code> to be generated by <code>bison</code>.</p>
<dt><code>VERBOSE &lt;file&gt;</code></p>
<dd>Tell <code>bison</code> to write verbose descriptions of the grammar and parser to the given <code>&lt;file&gt;</code>. </p>
<p> The macro defines the following variables:</p>
<dt><code>BISON_&lt;Name&gt;_DEFINED</code></p>
<dd>true is the macro ran successfully</p>
<dt><code>BISON_&lt;Name&gt;_INPUT</code></p>
<dd>The input source file, an alias for &lt;YaccInput&gt;</p>
<dt><code>BISON_&lt;Name&gt;_OUTPUT_SOURCE</code></p>
<dd>The source file generated by bison</p>
<dt><code>BISON_&lt;Name&gt;_OUTPUT_HEADER</code></p>
<dd>The header file generated by bison</p>
<dt><code>BISON_&lt;Name&gt;_OUTPUTS</code></p>
<dd>The sources files generated by bison</p>
<dt><code>BISON_&lt;Name&gt;_COMPILE_FLAGS</code></p>
<dd>Options used in the <code>bison</code> command line </p>
<p> Example usage: </p>
<pre>find_package(BISON)
BISON_TARGET(MyParser parser.y ${CMAKE_CURRENT_BINARY_DIR}/parser.cpp
 DEFINES_FILE ${CMAKE_CURRENT_BINARY_DIR}/parser.h)
add_executable(Foo main.cpp ${BISON_MyParser_OUTPUTS})</pre>
</dl>
<h3>FindBLAS</h3>
<p>Find BLAS library </p>
<p> This module finds an installed fortran library that implements the BLAS linear-algebra interface (see <i><a rel="nofollow" href="http://www.netlib.org/blas/">http://www.netlib.org/blas/</a></i>). The list of libraries searched for is taken from the autoconf macro file, acx_blas.m4 (distributed at <i><a rel="nofollow" href="http://ac-archive.sourceforge.net/ac-archive/acx_blas.html">http://ac-archive.sourceforge.net/ac-archive/acx_blas.html</a></i>). </p>
<p> This module sets the following variables: </p>
<pre>BLAS_FOUND - set to true if a library implementing the BLAS interface
 is found
BLAS_LINKER_FLAGS - uncached list of required linker flags (excluding -l
 and -L).
BLAS_LIBRARIES - uncached list of libraries (using full path name) to
 link against to use BLAS
BLAS95_LIBRARIES - uncached list of libraries (using full path name)
 to link against to use BLAS95 interface
BLAS95_FOUND - set to true if a library implementing the BLAS f95 interface
 is found
BLA_STATIC if set on this determines what kind of linkage we do (static)
BLA_VENDOR if set checks only the specified vendor, if not set checks
 all the possibilities
BLA_F95 if set on tries to find the f95 interfaces for BLAS/LAPACK</pre>
<p>######### ## List of vendors (BLA_VENDOR) valid in this module # Goto,OpenBLAS,ATLAS PhiPACK,CXML,DXML,SunPerf,SCSL,SGIMATH,IBMESSL, Intel10_32 (intel mkl v10 32 bit),Intel10_64lp (intel mkl v10 64 bit, lp thread model, lp64 model), # Intel10_64lp_seq (intel mkl v10 64 bit,sequential code, lp64 model), # Intel( older versions of mkl 32 and 64 bit), ACML,ACML_MP,ACML_GPU,Apple, NAS, Generic C/CXX should be enabled to use Intel mkl</p>
<h3>FindBacktrace</h3>
<p>Find provider for <a href="/docs/linux/man/3-backtrace/">backtrace</a>(3). </p>
<p> Checks if OS supports <a href="/docs/linux/man/3-backtrace/">backtrace</a>(3) via either libc or custom library. This module defines the following variables:</p>
<dl>
<dt><code>Backtrace_HEADER</code></p>
<dd>The header file needed for <a href="/docs/linux/man/3-backtrace/">backtrace</a>(3). Cached. Could be forcibly set by user.</p>
<dt><code>Backtrace_INCLUDE_DIRS</code></p>
<dd>The include directories needed to use <a href="/docs/linux/man/3-backtrace/">backtrace</a>(3) header.</p>
<dt><code>Backtrace_LIBRARIES</code></p>
<dd>The libraries (linker flags) needed to use <a href="/docs/linux/man/3-backtrace/">backtrace</a>(3), if any.</p>
<dt><code>Backtrace_FOUND</code></p>
<dd>Is set if and only if <a href="/docs/linux/man/3-backtrace/">backtrace</a>(3) support detected. </p>
<p> The following cache variables are also available to set or use:</p>
<dt><code>Backtrace_LIBRARY</code></p>
<dd>The external library providing backtrace, if any.</p>
<dt><code>Backtrace_INCLUDE_DIR</code></p>
<dd>The directory holding the <a href="/docs/linux/man/3-backtrace/">backtrace</a>(3) header. </p>
<p> Typical usage is to generate of header file using configure_file() with the contents like the following: </p>
<pre>#cmakedefine01 Backtrace_FOUND
#if Backtrace_FOUND
# include &lt;${Backtrace_HEADER}&gt;
#endif</pre>
<p>And then reference that generated header file in actual source.</dl>
<h3>FindBoost</h3>
<p>Find Boost include dirs and libraries </p>
<p> Use this module by invoking find_package with the form: </p>
<pre>find_package(Boost
 [version] [EXACT] # Minimum or EXACT version e.g. 1.36.0
 [REQUIRED] # Fail with error if Boost is not found
 [COMPONENTS &lt;libs&gt;...] # Boost libraries by their canonical name
 ) # e.g. &quot;date_time&quot; for &quot;libboost_date_time&quot;</pre>
<p>This module finds headers and requested component libraries OR a CMake package configuration file provided by a &quot;Boost CMake&quot; build. For the latter case skip to the &quot;Boost CMake&quot; section below. For the former case results are reported in variables: </p>
<pre>Boost_FOUND - True if headers and requested libraries were found
Boost_INCLUDE_DIRS - Boost include directories
Boost_LIBRARY_DIRS - Link directories for Boost libraries
Boost_LIBRARIES - Boost component libraries to be linked
Boost_&lt;C&gt;_FOUND - True if component &lt;C&gt; was found (&lt;C&gt; is upper-case)
Boost_&lt;C&gt;_LIBRARY - Libraries to link for component &lt;C&gt; (may include
 target_link_libraries debug/optimized keywords)
Boost_VERSION - BOOST_VERSION value from boost/version.hpp
Boost_LIB_VERSION - Version string appended to library filenames
Boost_MAJOR_VERSION - Boost major version number (X in X.y.z)
Boost_MINOR_VERSION - Boost minor version number (Y in x.Y.z)
Boost_SUBMINOR_VERSION - Boost subminor version number (Z in x.y.Z)
Boost_LIB_DIAGNOSTIC_DEFINITIONS (Windows)
 - Pass to add_definitions() to have diagnostic
 information about Boost's automatic linking
 displayed during compilation</pre>
<p>This module reads hints about search locations from variables: </p>
<pre>BOOST_ROOT - Preferred installation prefix
 (or BOOSTROOT)
BOOST_INCLUDEDIR - Preferred include directory e.g. &lt;prefix&gt;/include
BOOST_LIBRARYDIR - Preferred library directory e.g. &lt;prefix&gt;/lib
Boost_NO_SYSTEM_PATHS - Set to ON to disable searching in locations not
 specified by these hint variables. Default is OFF.
Boost_ADDITIONAL_VERSIONS
 - List of Boost versions not known to this module
 (Boost install locations may contain the version)</pre>
<p>and saves search results persistently in CMake cache entries: </p>
<pre>Boost_INCLUDE_DIR - Directory containing Boost headers
Boost_LIBRARY_DIR_RELEASE - Directory containing release Boost libraries
Boost_LIBRARY_DIR_DEBUG - Directory containing debug Boost libraries
Boost_&lt;C&gt;_LIBRARY_DEBUG - Component &lt;C&gt; library debug variant
Boost_&lt;C&gt;_LIBRARY_RELEASE - Component &lt;C&gt; library release variant</pre>
<p>The following <code>IMPORTED</code> targets are also defined: </p>
<pre>Boost::boost - Target for header-only dependencies
 (Boost include directory)
Boost::&lt;C&gt; - Target for specific component dependency
 (shared or static library); &lt;C&gt; is lower-
 case
Boost::diagnostic_definitions - interface target to enable diagnostic
 information about Boost's automatic linking
 during compilation (adds BOOST_LIB_DIAGNOSTIC)
Boost::disable_autolinking - interface target to disable automatic
 linking with MSVC (adds BOOST_ALL_NO_LIB)
Boost::dynamic_linking - interface target to enable dynamic linking
 linking with MSVC (adds BOOST_ALL_DYN_LINK)</pre>
<p>Implicit dependencies such as Boost::filesystem requiring Boost::system will be automatically detected and satisfied, even if system is not specified when using find_package and if Boost::system is not added to target_link_libraries. If using Boost::thread, then Thread::Thread will also be added automatically. </p>
<p> It is important to note that the imported targets behave differently than variables created by this module: multiple calls to find_package(Boost) in the same directory or sub-directories with different options (e.g. static or shared) will not override the values of the targets created by the first call. </p>
<p> Users may set these hints or results as cache entries. Projects should not read these entries directly but instead use the above result variables. Note that some hint names start in upper-case &quot;BOOST&quot;. One may specify these as environment variables if they are not specified as CMake variables or cache entries. </p>
<p> This module first searches for the Boost header files using the above hint variables (excluding BOOST_LIBRARYDIR) and saves the result in Boost_INCLUDE_DIR. Then it searches for requested component libraries using the above hints (excluding BOOST_INCLUDEDIR and Boost_ADDITIONAL_VERSIONS), &quot;lib&quot; directories near Boost_INCLUDE_DIR, and the library name configuration settings below. It saves the library directories in Boost_LIBRARY_DIR_DEBUG and Boost_LIBRARY_DIR_RELEASE and individual library locations in Boost_&lt;C&gt;_LIBRARY_DEBUG and Boost_&lt;C&gt;_LIBRARY_RELEASE. When one changes settings used by previous searches in the same build tree (excluding environment variables) this module discards previous search results affected by the changes and searches again. </p>
<p> Boost libraries come in many variants encoded in their file name. Users or projects may tell this module which variant to find by setting variables: </p>
<pre>Boost_USE_MULTITHREADED - Set to OFF to use the non-multithreaded
 libraries ('mt' tag). Default is ON.
Boost_USE_STATIC_LIBS - Set to ON to force the use of the static
 libraries. Default is OFF.
Boost_USE_STATIC_RUNTIME - Set to ON or OFF to specify whether to use
 libraries linked statically to the C++ runtime
 ('s' tag). Default is platform dependent.
Boost_USE_DEBUG_RUNTIME - Set to ON or OFF to specify whether to use
 libraries linked to the MS debug C++ runtime
 ('g' tag). Default is ON.
Boost_USE_DEBUG_PYTHON - Set to ON to use libraries compiled with a
 debug Python build ('y' tag). Default is OFF.
Boost_USE_STLPORT - Set to ON to use libraries compiled with
 STLPort ('p' tag). Default is OFF.
Boost_USE_STLPORT_DEPRECATED_NATIVE_IOSTREAMS
 - Set to ON to use libraries compiled with
 STLPort deprecated &quot;native iostreams&quot;
 ('n' tag). Default is OFF.
Boost_COMPILER - Set to the compiler-specific library suffix
 (e.g. &quot;-gcc43&quot;). Default is auto-computed
 for the C++ compiler in use.
Boost_THREADAPI - Suffix for &quot;thread&quot; component library name,
 such as &quot;pthread&quot; or &quot;win32&quot;. Names with
 and without this suffix will both be tried.
Boost_NAMESPACE - Alternate namespace used to build boost with
 e.g. if set to &quot;myboost&quot;, will search for
 myboost_thread instead of boost_thread.</pre>
<p>Other variables one may set to control this module are: </p>
<pre>Boost_DEBUG - Set to ON to enable debug output from FindBoost.
 Please enable this before filing any bug report.
Boost_DETAILED_FAILURE_MSG
 - Set to ON to add detailed information to the
 failure message even when the REQUIRED option
 is not given to the find_package call.
Boost_REALPATH - Set to ON to resolve symlinks for discovered
 libraries to assist with packaging. For example,
 the &quot;system&quot; component library may be resolved to
 &quot;/usr/lib/libboost_system.so.1.42.0&quot; instead of
 &quot;/usr/lib/libboost_system.so&quot;. This does not
 affect linking and should not be enabled unless
 the user needs this information.
Boost_LIBRARY_DIR - Default value for Boost_LIBRARY_DIR_RELEASE and
 Boost_LIBRARY_DIR_DEBUG.</pre>
<p>On Visual Studio and Borland compilers Boost headers request automatic linking to corresponding libraries. This requires matching libraries to be linked explicitly or available in the link library search path. In this case setting Boost_USE_STATIC_LIBS to OFF may not achieve dynamic linking. Boost automatic linking typically requests static libraries with a few exceptions (such as Boost.Python). Use: </p>
<pre>add_definitions(${Boost_LIB_DIAGNOSTIC_DEFINITIONS})</pre>
<p>to ask Boost to report information about automatic linking requests. </p>
<p> Example to find Boost headers only: </p>
<pre>find_package(Boost 1.36.0)
if(Boost_FOUND)
 include_directories(${Boost_INCLUDE_DIRS})
 add_executable(foo foo.cc)
endif()</pre>
<p>Example to find Boost libraries and use imported targets: </p>
<pre>find_package(Boost 1.56 REQUIRED COMPONENTS
 date_time filesystem iostreams)
add_executable(foo foo.cc)
target_link_libraries(foo Boost::date_time Boost::filesystem
 Boost::iostreams)</pre>
<p>Example to find Boost headers and some <i>static</i> libraries: </p>
<pre>set(Boost_USE_STATIC_LIBS ON) # only find static libs
set(Boost_USE_MULTITHREADED ON)
set(Boost_USE_STATIC_RUNTIME OFF)
find_package(Boost 1.36.0 COMPONENTS date_time filesystem system ...)
if(Boost_FOUND)
 include_directories(${Boost_INCLUDE_DIRS})
 add_executable(foo foo.cc)
 target_link_libraries(foo ${Boost_LIBRARIES})
endif()</pre>
<h3>Boost CMake</h3>
<p>If Boost was built using the boost-cmake project it provides a package configuration file for use with find_package&#8217;s Config mode. This module looks for the package configuration file called BoostConfig.cmake or boost-config.cmake and stores the result in cache entry &quot;Boost_DIR&quot;. If found, the package configuration file is loaded and this module returns with no further action. See documentation of the Boost CMake package configuration for details on what it provides. </p>
<p> Set Boost_NO_BOOST_CMAKE to ON to disable the search for boost-cmake.</p>
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
<p>Try to find BZip2 </p>
<p> Once done this will define </p>
<pre>BZIP2_FOUND - system has BZip2
BZIP2_INCLUDE_DIR - the BZip2 include directory
BZIP2_LIBRARIES - Link these to use BZip2
BZIP2_NEED_PREFIX - this is set if the functions are prefixed with BZ2_
BZIP2_VERSION_STRING - the version of BZip2 found (since CMake 2.8.8)</pre>
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
<h3>FindCUDA</h3>
<p>Tools for building CUDA C files: libraries and build dependencies. </p>
<p> This script locates the NVIDIA CUDA C tools. It should work on linux, windows, and mac and should be reasonably up to date with CUDA C releases. </p>
<p> This script makes use of the standard find_package arguments of &lt;VERSION&gt;, REQUIRED and QUIET. CUDA_FOUND will report if an acceptable version of CUDA was found. </p>
<p> The script will prompt the user to specify CUDA_TOOLKIT_ROOT_DIR if the prefix cannot be determined by the location of nvcc in the system path and REQUIRED is specified to find_package(). To use a different installed version of the toolkit set the environment variable CUDA_BIN_PATH before running cmake (e.g. CUDA_BIN_PATH=/usr/local/cuda1.0 instead of the default /usr/local/cuda) or set CUDA_TOOLKIT_ROOT_DIR after configuring. If you change the value of CUDA_TOOLKIT_ROOT_DIR, various components that depend on the path will be relocated. </p>
<p> It might be necessary to set CUDA_TOOLKIT_ROOT_DIR manually on certain platforms, or to use a cuda runtime not installed in the default location. In newer versions of the toolkit the cuda library is included with the graphics driver- be sure that the driver version matches what is needed by the cuda runtime version. </p>
<p> The following variables affect the behavior of the macros in the script (in alphebetical order). Note that any of these flags can be changed multiple times in the same directory before calling CUDA_ADD_EXECUTABLE, CUDA_ADD_LIBRARY, CUDA_COMPILE, CUDA_COMPILE_PTX, CUDA_COMPILE_FATBIN, CUDA_COMPILE_CUBIN or CUDA_WRAP_SRCS: </p>
<pre>CUDA_64_BIT_DEVICE_CODE (Default matches host bit size)
-- Set to ON to compile for 64 bit device code, OFF for 32 bit device code.
 Note that making this different from the host code when generating object
 or C files from CUDA code just won't work, because size_t gets defined by
 nvcc in the generated source. If you compile to PTX and then load the
 file yourself, you can mix bit sizes between device and host.
CUDA_ATTACH_VS_BUILD_RULE_TO_CUDA_FILE (Default ON)
-- Set to ON if you want the custom build rule to be attached to the source
 file in Visual Studio. Turn OFF if you add the same cuda file to multiple
 targets.
 This allows the user to build the target from the CUDA file; however, bad
 things can happen if the CUDA source file is added to multiple targets.
 When performing parallel builds it is possible for the custom build
 command to be run more than once and in parallel causing cryptic build
 errors. VS runs the rules for every source file in the target, and a
 source can have only one rule no matter how many projects it is added to.
 When the rule is run from multiple targets race conditions can occur on
 the generated file. Eventually everything will get built, but if the user
 is unaware of this behavior, there may be confusion. It would be nice if
 this script could detect the reuse of source files across multiple targets
 and turn the option off for the user, but no good solution could be found.
CUDA_BUILD_CUBIN (Default OFF)
-- Set to ON to enable and extra compilation pass with the -cubin option in
 Device mode. The output is parsed and register, shared memory usage is
 printed during build.
CUDA_BUILD_EMULATION (Default OFF for device mode)
-- Set to ON for Emulation mode. -D_DEVICEEMU is defined for CUDA C files
 when CUDA_BUILD_EMULATION is TRUE.
CUDA_GENERATED_OUTPUT_DIR (Default CMAKE_CURRENT_BINARY_DIR)
-- Set to the path you wish to have the generated files placed. If it is
 blank output files will be placed in CMAKE_CURRENT_BINARY_DIR.
 Intermediate files will always be placed in
 CMAKE_CURRENT_BINARY_DIR/CMakeFiles.
CUDA_HOST_COMPILATION_CPP (Default ON)
-- Set to OFF for C compilation of host code.
CUDA_HOST_COMPILER (Default CMAKE_C_COMPILER, $(VCInstallDir)/bin for VS)
-- Set the host compiler to be used by nvcc. Ignored if -ccbin or
 --compiler-bindir is already present in the CUDA_NVCC_FLAGS or
 CUDA_NVCC_FLAGS_&lt;CONFIG&gt; variables. For Visual Studio targets
 $(VCInstallDir)/bin is a special value that expands out to the path when
 the command is run from within VS.
CUDA_NVCC_FLAGS
CUDA_NVCC_FLAGS_&lt;CONFIG&gt;
-- Additional NVCC command line arguments. NOTE: multiple arguments must be
 semi-colon delimited (e.g. --compiler-options;-Wall)
CUDA_PROPAGATE_HOST_FLAGS (Default ON)
-- Set to ON to propagate CMAKE_{C,CXX}_FLAGS and their configuration
 dependent counterparts (e.g. CMAKE_C_FLAGS_DEBUG) automatically to the
 host compiler through nvcc's -Xcompiler flag. This helps make the
 generated host code match the rest of the system better. Sometimes
 certain flags give nvcc problems, and this will help you turn the flag
 propagation off. This does not affect the flags supplied directly to nvcc
 via CUDA_NVCC_FLAGS or through the OPTION flags specified through
 CUDA_ADD_LIBRARY, CUDA_ADD_EXECUTABLE, or CUDA_WRAP_SRCS. Flags used for
 shared library compilation are not affected by this flag.
CUDA_SEPARABLE_COMPILATION (Default OFF)
-- If set this will enable separable compilation for all CUDA runtime object
 files. If used outside of CUDA_ADD_EXECUTABLE and CUDA_ADD_LIBRARY
 (e.g. calling CUDA_WRAP_SRCS directly),
 CUDA_COMPUTE_SEPARABLE_COMPILATION_OBJECT_FILE_NAME and
 CUDA_LINK_SEPARABLE_COMPILATION_OBJECTS should be called.
CUDA_SOURCE_PROPERTY_FORMAT
-- If this source file property is set, it can override the format specified
 to CUDA_WRAP_SRCS (OBJ, PTX, CUBIN, or FATBIN). If an input source file
 is not a .cu file, setting this file will cause it to be treated as a .cu
 file. See documentation for set_source_files_properties on how to set
 this property.
CUDA_USE_STATIC_CUDA_RUNTIME (Default ON)
-- When enabled the static version of the CUDA runtime library will be used
 in CUDA_LIBRARIES. If the version of CUDA configured doesn't support
 this option, then it will be silently disabled.
CUDA_VERBOSE_BUILD (Default OFF)
-- Set to ON to see all the commands used when building the CUDA file. When
 using a Makefile generator the value defaults to VERBOSE (run make
 VERBOSE=1 to see output), although setting CUDA_VERBOSE_BUILD to ON will
 always print the output.</pre>
<p>The script creates the following macros (in alphebetical order): </p>
<pre>CUDA_ADD_CUFFT_TO_TARGET( cuda_target )
-- Adds the cufft library to the target (can be any target). Handles whether
 you are in emulation mode or not.
CUDA_ADD_CUBLAS_TO_TARGET( cuda_target )
-- Adds the cublas library to the target (can be any target). Handles
 whether you are in emulation mode or not.
CUDA_ADD_EXECUTABLE( cuda_target file0 file1 ...
 [WIN32] [MACOSX_BUNDLE] [EXCLUDE_FROM_ALL] [OPTIONS ...] )
-- Creates an executable &quot;cuda_target&quot; which is made up of the files
 specified. All of the non CUDA C files are compiled using the standard
 build rules specified by CMAKE and the cuda files are compiled to object
 files using nvcc and the host compiler. In addition CUDA_INCLUDE_DIRS is
 added automatically to include_directories(). Some standard CMake target
 calls can be used on the target after calling this macro
 (e.g. set_target_properties and target_link_libraries), but setting
 properties that adjust compilation flags will not affect code compiled by
 nvcc. Such flags should be modified before calling CUDA_ADD_EXECUTABLE,
 CUDA_ADD_LIBRARY or CUDA_WRAP_SRCS.
CUDA_ADD_LIBRARY( cuda_target file0 file1 ...
 [STATIC | SHARED | MODULE] [EXCLUDE_FROM_ALL] [OPTIONS ...] )
-- Same as CUDA_ADD_EXECUTABLE except that a library is created.
CUDA_BUILD_CLEAN_TARGET()
-- Creates a convience target that deletes all the dependency files
 generated. You should make clean after running this target to ensure the
 dependency files get regenerated.
CUDA_COMPILE( generated_files file0 file1 ... [STATIC | SHARED | MODULE]
 [OPTIONS ...] )
-- Returns a list of generated files from the input source files to be used
 with ADD_LIBRARY or ADD_EXECUTABLE.
CUDA_COMPILE_PTX( generated_files file0 file1 ... [OPTIONS ...] )
-- Returns a list of PTX files generated from the input source files.
CUDA_COMPILE_FATBIN( generated_files file0 file1 ... [OPTIONS ...] )
-- Returns a list of FATBIN files generated from the input source files.
CUDA_COMPILE_CUBIN( generated_files file0 file1 ... [OPTIONS ...] )
-- Returns a list of CUBIN files generated from the input source files.
CUDA_COMPUTE_SEPARABLE_COMPILATION_OBJECT_FILE_NAME( output_file_var
 cuda_target
 object_files )
-- Compute the name of the intermediate link file used for separable
 compilation. This file name is typically passed into
 CUDA_LINK_SEPARABLE_COMPILATION_OBJECTS. output_file_var is produced
 based on cuda_target the list of objects files that need separable
 compilation as specified by object_files. If the object_files list is
 empty, then output_file_var will be empty. This function is called
 automatically for CUDA_ADD_LIBRARY and CUDA_ADD_EXECUTABLE. Note that
 this is a function and not a macro.
CUDA_INCLUDE_DIRECTORIES( path0 path1 ... )
-- Sets the directories that should be passed to nvcc
 (e.g. nvcc -Ipath0 -Ipath1 ... ). These paths usually contain other .cu
 files.
CUDA_LINK_SEPARABLE_COMPILATION_OBJECTS( output_file_var cuda_target
 nvcc_flags object_files)
-- Generates the link object required by separable compilation from the given
 object files. This is called automatically for CUDA_ADD_EXECUTABLE and
 CUDA_ADD_LIBRARY, but can be called manually when using CUDA_WRAP_SRCS
 directly. When called from CUDA_ADD_LIBRARY or CUDA_ADD_EXECUTABLE the
 nvcc_flags passed in are the same as the flags passed in via the OPTIONS
 argument. The only nvcc flag added automatically is the bitness flag as
 specified by CUDA_64_BIT_DEVICE_CODE. Note that this is a function
 instead of a macro.
CUDA_WRAP_SRCS ( cuda_target format generated_files file0 file1 ...
 [STATIC | SHARED | MODULE] [OPTIONS ...] )
-- This is where all the magic happens. CUDA_ADD_EXECUTABLE,
 CUDA_ADD_LIBRARY, CUDA_COMPILE, and CUDA_COMPILE_PTX all call this
 function under the hood.
 Given the list of files (file0 file1 ... fileN) this macro generates
 custom commands that generate either PTX or linkable objects (use &quot;PTX&quot; or
 &quot;OBJ&quot; for the format argument to switch). Files that don't end with .cu
 or have the HEADER_FILE_ONLY property are ignored.
 The arguments passed in after OPTIONS are extra command line options to
 give to nvcc. You can also specify per configuration options by
 specifying the name of the configuration followed by the options. General
 options must precede configuration specific options. Not all
 configurations need to be specified, only the ones provided will be used.
 OPTIONS -DFLAG=2 &quot;-DFLAG_OTHER=space in flag&quot;
 DEBUG -g
 RELEASE --use_fast_math
 RELWITHDEBINFO --use_fast_math;-g
 MINSIZEREL --use_fast_math
 For certain configurations (namely VS generating object files with
 CUDA_ATTACH_VS_BUILD_RULE_TO_CUDA_FILE set to ON), no generated file will
 be produced for the given cuda file. This is because when you add the
 cuda file to Visual Studio it knows that this file produces an object file
 and will link in the resulting object file automatically.
 This script will also generate a separate cmake script that is used at
 build time to invoke nvcc. This is for several reasons.
 1. nvcc can return negative numbers as return values which confuses
 Visual Studio into thinking that the command succeeded. The script now
 checks the error codes and produces errors when there was a problem.
 2. nvcc has been known to not delete incomplete results when it
 encounters problems. This confuses build systems into thinking the
 target was generated when in fact an unusable file exists. The script
 now deletes the output files if there was an error.
 3. By putting all the options that affect the build into a file and then
 make the build rule dependent on the file, the output files will be
 regenerated when the options change.
 This script also looks at optional arguments STATIC, SHARED, or MODULE to
 determine when to target the object compilation for a shared library.
 BUILD_SHARED_LIBS is ignored in CUDA_WRAP_SRCS, but it is respected in
 CUDA_ADD_LIBRARY. On some systems special flags are added for building
 objects intended for shared libraries. A preprocessor macro,
 &lt;target_name&gt;_EXPORTS is defined when a shared library compilation is
 detected.
 Flags passed into add_definitions with -D or /D are passed along to nvcc.</pre>
<p>The script defines the following variables: </p>
<pre>CUDA_VERSION_MAJOR -- The major version of cuda as reported by nvcc.
CUDA_VERSION_MINOR -- The minor version.
CUDA_VERSION
CUDA_VERSION_STRING -- CUDA_VERSION_MAJOR.CUDA_VERSION_MINOR
CUDA_HAS_FP16 -- Whether a short float (float16,fp16) is supported.
CUDA_TOOLKIT_ROOT_DIR -- Path to the CUDA Toolkit (defined if not set).
CUDA_SDK_ROOT_DIR -- Path to the CUDA SDK. Use this to find files in the
 SDK. This script will not directly support finding
 specific libraries or headers, as that isn't
 supported by NVIDIA. If you want to change
 libraries when the path changes see the
 FindCUDA.cmake script for an example of how to clear
 these variables. There are also examples of how to
 use the CUDA_SDK_ROOT_DIR to locate headers or
 libraries, if you so choose (at your own risk).
CUDA_INCLUDE_DIRS -- Include directory for cuda headers. Added automatically
 for CUDA_ADD_EXECUTABLE and CUDA_ADD_LIBRARY.
CUDA_LIBRARIES -- Cuda RT library.
CUDA_CUFFT_LIBRARIES -- Device or emulation library for the Cuda FFT
 implementation (alternative to:
 CUDA_ADD_CUFFT_TO_TARGET macro)
CUDA_CUBLAS_LIBRARIES -- Device or emulation library for the Cuda BLAS
 implementation (alterative to:
 CUDA_ADD_CUBLAS_TO_TARGET macro).
CUDA_cudart_static_LIBRARY -- Statically linkable cuda runtime library.
 Only available for CUDA version 5.5+
CUDA_cupti_LIBRARY -- CUDA Profiling Tools Interface library.
 Only available for CUDA version 4.0+.
CUDA_curand_LIBRARY -- CUDA Random Number Generation library.
 Only available for CUDA version 3.2+.
CUDA_cusolver_LIBRARY -- CUDA Direct Solver library.
 Only available for CUDA version 7.0+.
CUDA_cusparse_LIBRARY -- CUDA Sparse Matrix library.
 Only available for CUDA version 3.2+.
CUDA_npp_LIBRARY -- NVIDIA Performance Primitives lib.
 Only available for CUDA version 4.0+.
CUDA_nppc_LIBRARY -- NVIDIA Performance Primitives lib (core).
 Only available for CUDA version 5.5+.
CUDA_nppi_LIBRARY -- NVIDIA Performance Primitives lib (image processing).
 Only available for CUDA version 5.5+.
CUDA_npps_LIBRARY -- NVIDIA Performance Primitives lib (signal processing).
 Only available for CUDA version 5.5+.
CUDA_nvcuvenc_LIBRARY -- CUDA Video Encoder library.
 Only available for CUDA version 3.2+.
 Windows only.
CUDA_nvcuvid_LIBRARY -- CUDA Video Decoder library.
 Only available for CUDA version 3.2+.
 Windows only.</pre>
<h3>FindCups</h3>
<p>Try to find the Cups printing system </p>
<p> Once done this will define </p>
<pre>CUPS_FOUND - system has Cups
CUPS_INCLUDE_DIR - the Cups include directory
CUPS_LIBRARIES - Libraries needed to use Cups
CUPS_VERSION_STRING - version of Cups found (since CMake 2.8.8)
Set CUPS_REQUIRE_IPP_DELETE_ATTRIBUTE to TRUE if you need a version which
features this function (i.e. at least 1.1.19)</pre>
<h3>FindCURL</h3>
<p>Find curl </p>
<p> Find the native CURL headers and libraries. </p>
<pre>CURL_INCLUDE_DIRS - where to find curl/curl.h, etc.
CURL_LIBRARIES - List of libraries when using curl.
CURL_FOUND - True if curl found.
CURL_VERSION_STRING - the version of curl found (since CMake 2.8.8)</pre>
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
<dt><code>CURSES_HAVE_CURSES_H</code></p>
<dd>True if curses.h is available.</p>
<dt><code>CURSES_HAVE_NCURSES_H</code></p>
<dd>True if ncurses.h is available.</p>
<dt><code>CURSES_HAVE_NCURSES_NCURSES_H</code></p>
<dd>True if <code>ncurses/ncurses.h</code> is available.</p>
<dt><code>CURSES_HAVE_NCURSES_CURSES_H</code></p>
<dd>True if <code>ncurses/curses.h</code> is available. </p>
<p> Set <code>CURSES_NEED_NCURSES</code> to <code>TRUE</code> before the <code>find_package(Curses)</code> call if NCurses functionality is required.</dl>
<h3>Backward Compatibility</h3>
<p>The following variable are provided for backward compatibility:</p>
<dl>
<dt><code>CURSES_INCLUDE_DIR</code></p>
<dd>Path to Curses include. Use <code>CURSES_INCLUDE_DIRS</code> instead.</p>
<dt><code>CURSES_LIBRARY</code></p>
<dd>Path to Curses library. Use <code>CURSES_LIBRARIES</code> instead.</dl>
<h3>FindCVS</h3>
<p>The module defines the following variables: </p>
<pre>CVS_EXECUTABLE - path to cvs command line client
CVS_FOUND - true if the command line client was found</pre>
<p>Example usage: </p>
<pre>find_package(CVS)
if(CVS_FOUND)
 message(&quot;CVS found: ${CVS_EXECUTABLE}&quot;)
endif()</pre>
<h3>FindCxxTest</h3>
<p>Find CxxTest </p>
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
 The full path to the Perl or Python executable on the system</pre>
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
<p>this module looks for Cygwin</p>
<h3>FindDart</h3>
<p>Find DART </p>
<p> This module looks for the dart testing software and sets DART_ROOT to point to where it found it.</p>
<h3>FindDCMTK</h3>
<p>Find DCMTK libraries and applications </p>
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
<p>This module locates the developer&#8217;s image library. <i><a rel="nofollow" href="http://openil.sourceforge.net/">http://openil.sourceforge.net/</a></i> </p>
<p> This module sets: </p>
<pre>IL_LIBRARIES - the name of the IL library. These include the full path to
 the core DevIL library. This one has to be linked into the
 application.
ILU_LIBRARIES - the name of the ILU library. Again, the full path. This
 library is for filters and effects, not actual loading. It
 doesn't have to be linked if the functionality it provides
 is not used.
ILUT_LIBRARIES - the name of the ILUT library. Full path. This part of the
 library interfaces with OpenGL. It is not strictly needed
 in applications.
IL_INCLUDE_DIR - where to find the il.h, ilu.h and ilut.h files.
IL_FOUND - this is set to TRUE if all the above variables were set.
 This will be set to false if ILU or ILUT are not found,
 even if they are not needed. In most systems, if one
 library is found all the others are as well. That's the
 way the DevIL developers release it.</pre>
<h3>FindDoxygen</h3>
<p>This module looks for Doxygen and the path to Graphviz&#8217;s dot </p>
<p> Doxygen is a documentation generation tool. Please see <i><a rel="nofollow" href="http://www.doxygen.org">http://www.doxygen.org</a></i> </p>
<p> This module accepts the following optional variables: </p>
<pre>DOXYGEN_SKIP_DOT = If true this module will skip trying to find Dot
 (an optional component often used by Doxygen)</pre>
<p>This modules defines the following variables: </p>
<pre>DOXYGEN_EXECUTABLE = The path to the doxygen command.
DOXYGEN_FOUND = Was Doxygen found or not?
DOXYGEN_VERSION = The version reported by doxygen --version</pre>
<pre>DOXYGEN_DOT_EXECUTABLE = The path to the dot program used by doxygen.
DOXYGEN_DOT_FOUND = Was Dot found or not?</pre>
<p>For compatibility with older versions of CMake, the now-deprecated variable <code>DOXYGEN_DOT_PATH</code> is set to the path to the directory containing <code>dot</code> as reported in <code>DOXYGEN_DOT_EXECUTABLE</code>. The path may have forward slashes even on Windows and is not suitable for direct substitution into a <code>Doxyfile.in</code> template. If you need this value, use <code>get_filename_component()</code> to compute it from <code>DOXYGEN_DOT_EXECUTABLE</code> directly, and perhaps the <code>file(TO_NATIVE_PATH)</code> command to prepare the path for a Doxygen configuration file.</p>
<h3>FindEXPAT</h3>
<p>Find expat </p>
<p> Find the native EXPAT headers and libraries. </p>
<pre>EXPAT_INCLUDE_DIRS - where to find expat.h, etc.
EXPAT_LIBRARIES - List of libraries when using expat.
EXPAT_FOUND - True if expat found.</pre>
<h3>FindFLEX</h3>
<p>Find flex executable and provides a macro to generate custom build rules </p>
<p> The module defines the following variables: </p>
<pre>FLEX_FOUND - true is flex executable is found
FLEX_EXECUTABLE - the path to the flex executable
FLEX_VERSION - the version of flex
FLEX_LIBRARIES - The flex libraries
FLEX_INCLUDE_DIRS - The path to the flex headers</pre>
<p>The minimum required version of flex can be specified using the standard syntax, e.g. find_package(FLEX 2.5.13) </p>
<p> If flex is found on the system, the module provides the macro: </p>
<pre>FLEX_TARGET(Name FlexInput FlexOutput
 [COMPILE_FLAGS &lt;string&gt;]
 [DEFINES_FILE &lt;string&gt;]
 )</pre>
<p>which creates a custom command to generate the &lt;FlexOutput&gt; file from the &lt;FlexInput&gt; file. If COMPILE_FLAGS option is specified, the next parameter is added to the flex command line. If flex is configured to output a header file, the DEFINES_FILE option may be used to specify its name. Name is an alias used to get details of this custom command. Indeed the macro defines the following variables: </p>
<pre>FLEX_${Name}_DEFINED - true is the macro ran successfully
FLEX_${Name}_OUTPUTS - the source file generated by the custom rule, an
alias for FlexOutput
FLEX_${Name}_INPUT - the flex source file, an alias for ${FlexInput}
FLEX_${Name}_OUTPUT_HEADER - the header flex output, if any.</pre>
<p>Flex scanners oftenly use tokens defined by Bison: the code generated by Flex depends of the header generated by Bison. This module also defines a macro: </p>
<pre>ADD_FLEX_BISON_DEPENDENCY(FlexTarget BisonTarget)</pre>
<p>which adds the required dependency between a scanner and a parser where &lt;FlexTarget&gt; and &lt;BisonTarget&gt; are the first parameters of respectively FLEX_TARGET and BISON_TARGET macros. </p>
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
====================================================================</pre>
<h3>FindFLTK2</h3>
<p>Find the native FLTK2 includes and library </p>
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
<h3>FindFLTK</h3>
<p>Find the native FLTK includes and library </p>
<p> By default FindFLTK.cmake will search for all of the FLTK components and add them to the FLTK_LIBRARIES variable. </p>
<pre>You can limit the components which get placed in FLTK_LIBRARIES by
defining one or more of the following three options:</pre>
<pre>FLTK_SKIP_OPENGL, set to true to disable searching for opengl and
 the FLTK GL library
FLTK_SKIP_FORMS, set to true to disable searching for fltk_forms
FLTK_SKIP_IMAGES, set to true to disable searching for fltk_images</pre>
<pre>FLTK_SKIP_FLUID, set to true if the fluid binary need not be present
 at build time</pre>
<p>The following variables will be defined: </p>
<pre>FLTK_FOUND, True if all components not skipped were found
FLTK_INCLUDE_DIR, where to find include files
FLTK_LIBRARIES, list of fltk libraries you should link against
FLTK_FLUID_EXECUTABLE, where to find the Fluid tool
FLTK_WRAP_UI, This enables the FLTK_WRAP_UI command</pre>
<p>The following cache variables are assigned but should not be used. See the FLTK_LIBRARIES variable instead. </p>
<pre>FLTK_BASE_LIBRARY = the full path to fltk.lib
FLTK_GL_LIBRARY = the full path to fltk_gl.lib
FLTK_FORMS_LIBRARY = the full path to fltk_forms.lib
FLTK_IMAGES_LIBRARY = the full path to fltk_images.lib</pre>
<h3>FindFreetype</h3>
<p>Locate FreeType library </p>
<p> This module defines </p>
<pre>FREETYPE_LIBRARIES, the library to link against
FREETYPE_FOUND, if false, do not try to link to FREETYPE
FREETYPE_INCLUDE_DIRS, where to find headers.
FREETYPE_VERSION_STRING, the version of freetype found (since CMake 2.8.8)
This is the concatenation of the paths:
FREETYPE_INCLUDE_DIR_ft2build
FREETYPE_INCLUDE_DIR_freetype2</pre>
<p>$FREETYPE_DIR is an environment variable that would correspond to the</p>
<h3>FindGCCXML</h3>
<p>Find the GCC-XML front-end executable. </p>
<p> This module will define the following variables: </p>
<pre>GCCXML - the GCC-XML front-end executable.</pre>
<h3>FindGDAL</h3>
<p>Locate gdal </p>
<p> This module accepts the following environment variables: </p>
<pre>GDAL_DIR or GDAL_ROOT - Specify the location of GDAL</pre>
<p>This module defines the following CMake variables: </p>
<pre>GDAL_FOUND - True if libgdal is found
GDAL_LIBRARY - A variable pointing to the GDAL library
GDAL_INCLUDE_DIR - Where to find the headers</pre>
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
If ALL is specified, the pot file is processed when building the all traget.
It creates a custom target &quot;potfile&quot;.</pre>
<p>GETTEXT_PROCESS_PO_FILES( &lt;lang&gt; [ALL] [INSTALL_DESTINATION &lt;dir&gt;] PO_FILES &lt;po1&gt; &lt;po2&gt; &#8230; ) </p>
<pre>Process the given po files to mo files for the given language.
If INSTALL_DESTINATION is given then automatically install rules will
be created, the language subdirectory will be taken into account
(by default use share/locale/).
If ALL is specified, the po files are processed when building the all traget.
It creates a custom target &quot;pofiles&quot;.</pre>
<p><code>NOTE:</code> If you wish to use the Gettext library (libintl), use <code>FindIntl</code>.</p>
<h3>FindGIF</h3>
<p>This module searches giflib and defines GIF_LIBRARIES &#8211; libraries to link to in order to use GIF GIF_FOUND, if false, do not try to link GIF_INCLUDE_DIR, where to find the headers GIF_VERSION, reports either version 4 or 3 (for everything before version 4) </p>
<p> The minimum required version of giflib can be specified using the standard syntax, e.g. find_package(GIF 4) </p>
<p> $GIF_DIR is an environment variable that would correspond to the</p>
<h3>FindGit</h3>
<p>The module defines the following variables:</p>
<dl>
<dt><code>GIT_EXECUTABLE</code></p>
<dd>Path to Git command-line client.</p>
<dt><code>Git_FOUND</code>, <code>GIT_FOUND</code></p>
<dd>True if the Git command-line client was found.</p>
<dt><code>GIT_VERSION_STRING</code></p>
<dd>The version of Git found. </p>
<p> Example usage: </p>
<pre>find_package(Git)
if(Git_FOUND)
 message(&quot;Git found: ${GIT_EXECUTABLE}&quot;)
endif()</pre>
</dl>
<h3>FindGLEW</h3>
<p>Find the OpenGL Extension Wrangler Library (GLEW)</p>
<h3>IMPORTED Targets</h3>
<p>This module defines the <code>IMPORTED</code> target <code>GLEW::GLEW</code>, if GLEW has been found.</p>
<h3>Result Variables</h3>
<p>This module defines the following variables: </p>
<pre>GLEW_INCLUDE_DIRS - include directories for GLEW
GLEW_LIBRARIES - libraries to link against GLEW
GLEW_FOUND - true if GLEW has been found and can be used</pre>
<h3>FindGLUT</h3>
<p>try to find glut library and include files.</p>
<h3>IMPORTED Targets</h3>
<p>This module defines the <code>IMPORTED</code> targets:</p>
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
<h3>FindGnuplot</h3>
<p>this module looks for gnuplot </p>
<p> Once done this will define </p>
<pre>GNUPLOT_FOUND - system has Gnuplot
GNUPLOT_EXECUTABLE - the Gnuplot executable
GNUPLOT_VERSION_STRING - the version of Gnuplot found (since CMake 2.8.8)</pre>
<p>GNUPLOT_VERSION_STRING will not work for old versions like 3.7.1.</p>
<h3>FindGnuTLS</h3>
<p>Try to find the GNU Transport Layer Security library (gnutls) </p>
<p> Once done this will define </p>
<pre>GNUTLS_FOUND - System has gnutls
GNUTLS_INCLUDE_DIR - The gnutls include directory
GNUTLS_LIBRARIES - The libraries needed to use gnutls
GNUTLS_DEFINITIONS - Compiler switches required for using gnutls</pre>
<h3>FindGSL</h3>
<p>Find the native GSL includes and libraries. </p>
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
<p> This script expects to find libraries at <code>$GSL_ROOT_DIR/lib</code> and the GSL headers at <code>$GSL_ROOT_DIR/include/gsl</code>. The library directory may optionally provide Release and Debug folders. For Unix-like systems, this script will use <code>$GSL_ROOT_DIR/bin/gsl-config</code> (if found) to aid in the discovery GSL.</p>
<h3>Cache Variables</h3>
<p>This module may set the following variables depending on platform and type of GSL installation discovered. These variables may optionally be set to help this module find the correct files: </p>
<pre>GSL_CBLAS_LIBRARY - Location of the GSL CBLAS library.
GSL_CBLAS_LIBRARY_DEBUG - Location of the debug GSL CBLAS library (if any).
GSL_CONFIG_EXECUTABLE - Location of the ``gsl-config`` script (if any).
GSL_LIBRARY - Location of the GSL library.
GSL_LIBRARY_DEBUG - Location of the debug GSL library (if any).</pre>
<h3>FindGTest</h3>
<p>Locate the Google C++ Testing Framework.</p>
<h3>Imported targets</h3>
<p>This module defines the following <code>IMPORTED</code> targets:</p>
<dl>
<dt><code>GTest::GTest</code></p>
<dd>The Google Test <code>gtest</code> library, if found; adds Thread::Thread automatically</p>
<dt><code>GTest::Main</code></p>
<dd>The Google Test <code>gtest_main</code> library, if found</dl>
<h3>Result variables</h3>
<p>This module will set the following variables in your project:</p>
<dl>
<dt><code>GTEST_FOUND</code></p>
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
<dd>If compiling with MSVC, this variable can be set to <code>MD</code> or <code>MT</code> (the default) to enable searching a GTest build tree</dl>
<h3>Example usage</h3>
<pre>enable_testing()
find_package(GTest REQUIRED)
add_executable(foo foo.cc)
target_link_libraries(foo GTest::GTest GTest::Main)
add_test(AllTestsInFoo foo)</pre>
<h3>Deeper integration with CTest</h3>
<p>If you would like each Google test to show up in CTest as a test you may use the following macro: </p>
<pre>GTEST_ADD_TESTS(executable extra_args files...)</pre>
<dl>
<dt><code>executable</code></p>
<dd>the path to the test executable</p>
<dt><code>extra_args</code></p>
<dd>a list of extra arguments to be passed to executable enclosed in quotes (or <code>&quot;&quot;</code> for none)</p>
<dt><code>files&#8230;</code></p>
<dd>a list of source files to search for tests and test fixtures. Or <code>AUTO</code> to find them from executable target </p>
<p> However, note that this macro will slow down your tests by running an executable for each test and test fixture. </p>
<p> Example usage: </p>
<pre>set(FooTestArgs --foo 1 --bar 2)
add_executable(FooTest FooUnitTest.cc)
GTEST_ADD_TESTS(FooTest &quot;${FooTestArgs}&quot; AUTO)</pre>
</dl>
<h3>FindGTK2</h3>
<p>FindGTK2.cmake </p>
<p> This module can find the GTK2 widget libraries and several of its other optional components like gtkmm, glade, and glademm. </p>
<p> NOTE: If you intend to use version checking, CMake 2.6.2 or later is </p>
<pre>required.</pre>
<p>Specify one or more of the following components as you call this find module. See example below. </p>
<pre>gtk
gtkmm
glade
glademm</pre>
<p>The following variables will be defined for your use </p>
<pre>GTK2_FOUND - Were all of your specified components found?
GTK2_INCLUDE_DIRS - All include directories
GTK2_LIBRARIES - All libraries
GTK2_TARGETS - All imported targets
GTK2_DEFINITIONS - Additional compiler flags</pre>
<pre>GTK2_VERSION - The version of GTK2 found (x.y.z)
GTK2_MAJOR_VERSION - The major version of GTK2
GTK2_MINOR_VERSION - The minor version of GTK2
GTK2_PATCH_VERSION - The patch version of GTK2</pre>
<p>Optional variables you can define prior to calling this module: </p>
<pre>GTK2_DEBUG - Enables verbose debugging of the module
GTK2_ADDITIONAL_SUFFIXES - Allows defining additional directories to
 search for include files</pre>
<p>================= Example Usage: </p>
<pre>Call find_package() once, here are some examples to pick from:</pre>
<pre>Require GTK 2.6 or later
 find_package(GTK2 2.6 REQUIRED gtk)</pre>
<pre>Require GTK 2.10 or later and Glade
 find_package(GTK2 2.10 REQUIRED gtk glade)</pre>
<pre>Search for GTK/GTKMM 2.8 or later
 find_package(GTK2 2.8 COMPONENTS gtk gtkmm)</pre>
<pre>if(GTK2_FOUND)
 include_directories(${GTK2_INCLUDE_DIRS})
 add_executable(mygui mygui.cc)
 target_link_libraries(mygui ${GTK2_LIBRARIES})
endif()</pre>
<h3>FindGTK</h3>
<p>try to find GTK (and glib) and GTKGLArea </p>
<pre>GTK_INCLUDE_DIR - Directories to include to use GTK
GTK_LIBRARIES - Files to link against to use GTK
GTK_FOUND - GTK was found
GTK_GL_FOUND - GTK's GL features were found</pre>
<h3>FindHDF5</h3>
<p>Find HDF5, a library for reading and writing self describing array data. </p>
<p> This module invokes the HDF5 wrapper compiler that should be installed alongside HDF5. Depending upon the HDF5 Configuration, the wrapper compiler is called either h5cc or h5pcc. If this succeeds, the module will then call the compiler with the -show argument to see what flags are used when compiling an HDF5 client application. </p>
<p> The module will optionally accept the COMPONENTS argument. If no COMPONENTS are specified, then the find module will default to finding only the HDF5 C library. If one or more COMPONENTS are specified, the module will attempt to find the language bindings for the specified components. The only valid components are C, CXX, Fortran, HL, and Fortran_HL. If the COMPONENTS argument is not given, the module will attempt to find only the C bindings. </p>
<p> On UNIX systems, this module will read the variable HDF5_USE_STATIC_LIBRARIES to determine whether or not to prefer a static link to a dynamic link for HDF5 and all of it&#8217;s dependencies. To use this feature, make sure that the HDF5_USE_STATIC_LIBRARIES variable is set before the call to find_package. </p>
<p> To provide the module with a hint about where to find your HDF5 installation, you can set the environment variable HDF5_ROOT. The Find module will then look in this path when searching for HDF5 executables, paths, and libraries. </p>
<p> Both the serial and parallel HDF5 wrappers are considered and the first directory to contain either one will be used. In the event that both appear in the same directory the serial version is preferentially selected. This behavior can be reversed by setting the variable HDF5_PREFER_PARALLEL to true. </p>
<p> In addition to finding the includes and libraries required to compile an HDF5 client application, this module also makes an effort to find tools that come with the HDF5 distribution that may be useful for regression testing. </p>
<p> This module will define the following variables: </p>
<pre>HDF5_FOUND - true if HDF5 was found on the system
HDF5_VERSION - HDF5 version in format Major.Minor.Release
HDF5_INCLUDE_DIRS - Location of the hdf5 includes
HDF5_INCLUDE_DIR - Location of the hdf5 includes (deprecated)
HDF5_DEFINITIONS - Required compiler definitions for HDF5
HDF5_LIBRARIES - Required libraries for all requested bindings
HDF5_HL_LIBRARIES - Required libraries for the HDF5 high level API for all
 bindings, if the HL component is enabled</pre>
<p>Available components are: C CXX Fortran and HL. For each enabled language binding, a corresponding HDF5_${LANG}_LIBRARIES variable will be defined. If the HL component is enabled, then an HDF5_${LANG}_HL_LIBRARIES will also be defined. With all components enabled, the following variables will be defined: </p>
<pre>HDF5_C_LIBRARIES - Required libraries for the HDF5 C bindings
HDF5_CXX_LIBRARIES - Required libraries for the HDF5 C++ bindings
HDF5_Fortran_LIBRARIES - Required libraries for the HDF5 Fortran bindings
HDF5_C_HL_LIBRARIES - Required libraries for the high level C bindings
HDF5_CXX_HL_LIBRARIES - Required libraries for the high level C++ bindings
HDF5_Fortran_HL_LIBRARIES - Required libraries for the high level Fortran
 bindings.
HDF5_IS_PARALLEL - Whether or not HDF5 was found with parallel IO support
HDF5_C_COMPILER_EXECUTABLE - the path to the HDF5 C wrapper compiler
HDF5_CXX_COMPILER_EXECUTABLE - the path to the HDF5 C++ wrapper compiler
HDF5_Fortran_COMPILER_EXECUTABLE - the path to the HDF5 Fortran wrapper compiler
HDF5_C_COMPILER_EXECUTABLE_NO_INTERROGATE - path to the primary C compiler
 which is also the HDF5 wrapper
HDF5_CXX_COMPILER_EXECUTABLE_NO_INTERROGATE - path to the primary C++
 compiler which is also
 the HDF5 wrapper
HDF5_Fortran_COMPILER_EXECUTABLE_NO_INTERROGATE - path to the primary
 Fortran compiler which
 is also the HDF5 wrapper
HDF5_DIFF_EXECUTABLE - the path to the HDF5 dataset comparison tool</pre>
<p>The following variable can be set to guide the search for HDF5 libraries and includes: </p>
<p> HDF5_ROOT</p>
<h3>FindHg</h3>
<p>Extract information from a mercurial working copy. </p>
<p> The module defines the following variables: </p>
<pre>HG_EXECUTABLE - path to mercurial command line client (hg)
HG_FOUND - true if the command line client was found
HG_VERSION_STRING - the version of mercurial found</pre>
<p>If the command line client executable is found the following macro is defined: </p>
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
<p>Try to find Hspell </p>
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
<p>Find the ZeroC Internet Communication Engine (ICE) programs, libraries and datafiles. </p>
<p> This module supports multiple components. Components can include any of: <code>Freeze</code>, <code>Glacier2</code>, <code>Ice</code>, <code>IceBox</code>, <code>IceDB</code>, <code>IceGrid</code>, <code>IcePatch</code>, <code>IceSSL</code>, <code>IceStorm</code>, <code>IceUtil</code>, <code>IceXML</code>, or <code>Slice</code>. </p>
<p> This module reports information about the Ice installation in several variables. General variables: </p>
<pre>Ice_VERSION - Ice release version
Ice_FOUND - true if the main programs and libraries were found
Ice_LIBRARIES - component libraries to be linked
Ice_INCLUDE_DIRS - the directories containing the Ice headers
Ice_SLICE_DIRS - the directories containing the Ice slice interface
 definitions</pre>
<p>Imported targets: </p>
<pre>Ice::&lt;C&gt;</pre>
<p>Where <code>&lt;C&gt;</code> is the name of an Ice component, for example <code>Ice::Glacier2</code>. </p>
<p> Ice slice programs are reported in: </p>
<pre>Ice_SLICE2CPP_EXECUTABLE - path to slice2cpp executable
Ice_SLICE2CS_EXECUTABLE - path to slice2cs executable
Ice_SLICE2FREEZEJ_EXECUTABLE - path to slice2freezej executable
Ice_SLICE2FREEZE_EXECUTABLE - path to slice2freeze executable
Ice_SLICE2HTML_EXECUTABLE - path to slice2html executable
Ice_SLICE2JAVA_EXECUTABLE - path to slice2java executable
Ice_SLICE2JS_EXECUTABLE - path to slice2js executable
Ice_SLICE2PHP_EXECUTABLE - path to slice2php executable
Ice_SLICE2PY_EXECUTABLE - path to slice2py executable
Ice_SLICE2RB_EXECUTABLE - path to slice2rb executable</pre>
<p>Ice programs are reported in: </p>
<pre>Ice_GLACIER2ROUTER_EXECUTABLE - path to glacier2router executable
Ice_ICEBOX_EXECUTABLE - path to icebox executable
Ice_ICEBOXADMIN_EXECUTABLE - path to iceboxadmin executable
Ice_ICEBOXD_EXECUTABLE - path to iceboxd executable
Ice_ICEBOXNET_EXECUTABLE - path to iceboxnet executable
Ice_ICEGRIDADMIN_EXECUTABLE - path to icegridadmin executable
Ice_ICEGRIDNODE_EXECUTABLE - path to icegridnode executable
Ice_ICEGRIDNODED_EXECUTABLE - path to icegridnoded executable
Ice_ICEGRIDREGISTRY_EXECUTABLE - path to icegridregistry executable
Ice_ICEGRIDREGISTRYD_EXECUTABLE - path to icegridregistryd executable
Ice_ICEPATCH2CALC_EXECUTABLE - path to icepatch2calc executable
Ice_ICEPATCH2CLIENT_EXECUTABLE - path to icepatch2client executable
Ice_ICEPATCH2SERVER_EXECUTABLE - path to icepatch2server executable
Ice_ICESERVICEINSTALL_EXECUTABLE - path to iceserviceinstall executable
Ice_ICESTORMADMIN_EXECUTABLE - path to icestormadmin executable
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
<p> The following cache variables may also be set: </p>
<pre>Ice_&lt;P&gt;_EXECUTABLE - the path to executable &lt;P&gt;
Ice_INCLUDE_DIR - the directory containing the Ice headers
Ice_SLICE_DIR - the directory containing the Ice slice interface
 definitions
Ice_&lt;C&gt;_LIBRARY - the library for component &lt;C&gt;</pre>
<p><code>NOTE:</code> In most cases none of the above variables will require setting, unless multiple Ice versions are available and a specific version is required. On Windows, the most recent version of Ice will be found through the registry. On Unix, the programs, headers and libraries will usually be in standard locations, but Ice_SLICE_DIRS might not be automatically detected (commonly known locations are searched). All the other variables are defaulted using Ice_HOME, if set. It&#8217;s possible to set Ice_HOME and selectively specify alternative locations for the other components; this might be required for e.g. newer versions of Visual Studio if the heuristics are not sufficient to identify the correct programs and libraries for the specific Visual Studio version. </p>
<p> Other variables one may set to control this module are: </p>
<pre>Ice_DEBUG - Set to ON to enable debug output from FindIce.</pre>
<h3>FindIcotool</h3>
<p>Find icotool </p>
<p> This module looks for icotool. This module defines the following values: </p>
<pre>ICOTOOL_EXECUTABLE: the full path to the icotool tool.
ICOTOOL_FOUND: True if icotool has been found.
ICOTOOL_VERSION_STRING: the version of icotool found.</pre>
<h3>FindImageMagick</h3>
<p>Find the ImageMagick binary suite. </p>
<p> This module will search for a set of ImageMagick tools specified as components in the FIND_PACKAGE call. Typical components include, but are not limited to (future versions of ImageMagick might have additional components not listed here): </p>
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
<p>If no component is specified in the FIND_PACKAGE call, then it only searches for the ImageMagick executable directory. This code defines the following variables: </p>
<pre>ImageMagick_FOUND - TRUE if all components are found.
ImageMagick_EXECUTABLE_DIR - Full path to executables directory.
ImageMagick_&lt;component&gt;_FOUND - TRUE if &lt;component&gt; is found.
ImageMagick_&lt;component&gt;_EXECUTABLE - Full path to &lt;component&gt; executable.
ImageMagick_VERSION_STRING - the version of ImageMagick found
 (since CMake 2.8.8)</pre>
<p>ImageMagick_VERSION_STRING will not work for old versions like 5.2.3. </p>
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
<p>Note that the standard FIND_PACKAGE features are supported (i.e., QUIET, REQUIRED, etc.).</p>
<h3>FindIntl</h3>
<p>Find the Gettext libintl headers and libraries. </p>
<p> This module reports information about the Gettext libintl installation in several variables. General variables: </p>
<pre>Intl_FOUND - true if the libintl headers and libraries were found
Intl_INCLUDE_DIRS - the directory containing the libintl headers
Intl_LIBRARIES - libintl libraries to be linked</pre>
<p>The following cache variables may also be set: </p>
<pre>Intl_INCLUDE_DIR - the directory containing the libintl headers
Intl_LIBRARY - the libintl library (if any)</pre>
<p><code>NOTE:</code> On some platforms, such as Linux with GNU libc, the gettext functions are present in the C standard library and libintl is not required. <code>Intl_LIBRARIES</code> will be empty in this case. </p>
<p> <code>NOTE:</code> If you wish to use the Gettext tools (<code>msgmerge</code>, <code>msgfmt</code>, etc.), use <code>FindGettext</code>.</p>
<h3>FindITK</h3>
<p>This module no longer exists. </p>
<p> This module existed in versions of CMake prior to 3.1, but became only a thin wrapper around <code>find_package(ITK NO_MODULE)</code> to provide compatibility for projects using long-outdated conventions. Now <code>find_package(ITK)</code> will search for <code>ITKConfig.cmake</code> directly.</p>
<h3>FindJasper</h3>
<p>Try to find the Jasper JPEG2000 library </p>
<p> Once done this will define </p>
<pre>JASPER_FOUND - system has Jasper
JASPER_INCLUDE_DIR - the Jasper include directory
JASPER_LIBRARIES - the libraries needed to use Jasper
JASPER_VERSION_STRING - the version of Jasper found (since CMake 2.8.8)</pre>
<h3>FindJava</h3>
<p>Find Java </p>
<p> This module finds if Java is installed and determines where the include files and libraries are. The caller may set variable JAVA_HOME to specify a Java installation prefix explicitly. </p>
<p> Specify one or more of the following components as you call this find module. See example below. </p>
<pre>Runtime = User just want to execute some Java byte-compiled
Development = Development tools (java, javac, javah and javadoc), includes Runtime component
IdlJ = idl compiler for Java
JarSigner = signer tool for jar</pre>
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
Java_VERSION = This is set to: $major.$minor.$patch(.$tweak)</pre>
<p>The minimum required version of Java can be specified using the standard CMake syntax, e.g. find_package(Java 1.5) </p>
<p> NOTE: ${Java_VERSION} and ${Java_VERSION_STRING} are not guaranteed to be identical. For example some java version may return: Java_VERSION_STRING = 1.5.0_17 and Java_VERSION = 1.5.0.17 </p>
<p> another example is the Java OEM, with: Java_VERSION_STRING = 1.6.0-oem and Java_VERSION = 1.6.0 </p>
<p> For these components the following variables are set: </p>
<pre>Java_FOUND - TRUE if all components are found.
Java_INCLUDE_DIRS - Full paths to all include dirs.
Java_LIBRARIES - Full paths to all libraries.
Java_&lt;component&gt;_FOUND - TRUE if &lt;component&gt; is found.</pre>
<p>Example Usages: </p>
<pre>find_package(Java)
find_package(Java COMPONENTS Runtime)
find_package(Java COMPONENTS Development)</pre>
<h3>FindJNI</h3>
<p>Find JNI java libraries. </p>
<p> This module finds if Java is installed and determines where the include files and libraries are. It also determines what the name of the library is. The caller may set variable JAVA_HOME to specify a Java installation prefix explicitly. </p>
<p> This module sets the following result variables: </p>
<pre>JNI_INCLUDE_DIRS = the include dirs to use
JNI_LIBRARIES = the libraries to use
JNI_FOUND = TRUE if JNI headers and libraries were found.
JAVA_AWT_LIBRARY = the path to the jawt library
JAVA_JVM_LIBRARY = the path to the jvm library
JAVA_INCLUDE_PATH = the include path to jni.h
JAVA_INCLUDE_PATH2 = the include path to jni_md.h
JAVA_AWT_INCLUDE_PATH = the include path to jawt.h</pre>
<h3>FindJPEG</h3>
<p>Find JPEG </p>
<p> Find the native JPEG includes and library This module defines </p>
<pre>JPEG_INCLUDE_DIR, where to find jpeglib.h, etc.
JPEG_LIBRARIES, the libraries needed to use JPEG.
JPEG_FOUND, If false, do not try to use JPEG.</pre>
<p>also defined, but not for general use are </p>
<pre>JPEG_LIBRARY, where to find the JPEG library.</pre>
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
<p> It also adds the following macros (from KDE3Macros.cmake) SRCS_VAR is always the variable which contains the list of source files for your application or library. </p>
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
<p>Please look in FindKDE4Internal.cmake and KDE4Macros.cmake for more information. They are installed with the KDE 4 libraries in $KDEDIRS/share/apps/cmake/modules/. </p>
<p> Author: Alexander Neundorf &lt;<i>neundorf [at] kde.org</i>&gt;</p>
<h3>FindLAPACK</h3>
<p>Find LAPACK library </p>
<p> This module finds an installed fortran library that implements the LAPACK linear-algebra interface (see <i><a rel="nofollow" href="http://www.netlib.org/lapack/">http://www.netlib.org/lapack/</a></i>). </p>
<p> The approach follows that taken for the autoconf macro file, acx_lapack.m4 (distributed at <i><a rel="nofollow" href="http://ac-archive.sourceforge.net/ac-archive/acx_lapack.html">http://ac-archive.sourceforge.net/ac-archive/acx_lapack.html</a></i>). </p>
<p> This module sets the following variables: </p>
<pre>LAPACK_FOUND - set to true if a library implementing the LAPACK interface
 is found
LAPACK_LINKER_FLAGS - uncached list of required linker flags (excluding -l
 and -L).
LAPACK_LIBRARIES - uncached list of libraries (using full path name) to
 link against to use LAPACK
LAPACK95_LIBRARIES - uncached list of libraries (using full path name) to
 link against to use LAPACK95
LAPACK95_FOUND - set to true if a library implementing the LAPACK f95
 interface is found
BLA_STATIC if set on this determines what kind of linkage we do (static)
BLA_VENDOR if set checks only the specified vendor, if not set checks
 all the possibilities
BLA_F95 if set on tries to find the f95 interfaces for BLAS/LAPACK</pre>
<p>## List of vendors (BLA_VENDOR) valid in this module # Intel(mkl), OpenBLAS, ACML,Apple, NAS, Generic</p>
<h3>FindLATEX</h3>
<p>Find Latex </p>
<p> This module finds an installed Latex and determines the location of the compiler. Additionally the module looks for Latex-related software like BibTeX. </p>
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
<p>Find libarchive library and headers </p>
<p> The module defines the following variables: </p>
<pre>LibArchive_FOUND - true if libarchive was found
LibArchive_INCLUDE_DIRS - include search path
LibArchive_LIBRARIES - libraries to link
LibArchive_VERSION - libarchive 3-component version number</pre>
<h3>FindLibLZMA</h3>
<p>Find LibLZMA </p>
<p> Find LibLZMA headers and library </p>
<pre>LIBLZMA_FOUND - True if liblzma is found.
LIBLZMA_INCLUDE_DIRS - Directory where liblzma headers are located.
LIBLZMA_LIBRARIES - Lzma libraries to link against.
LIBLZMA_HAS_AUTO_DECODER - True if lzma_auto_decoder() is found (required).
LIBLZMA_HAS_EASY_ENCODER - True if lzma_easy_encoder() is found (required).
LIBLZMA_HAS_LZMA_PRESET - True if lzma_lzma_preset() is found (required).
LIBLZMA_VERSION_MAJOR - The major version of lzma
LIBLZMA_VERSION_MINOR - The minor version of lzma
LIBLZMA_VERSION_PATCH - The patch version of lzma
LIBLZMA_VERSION_STRING - version number as a string (ex: &quot;5.0.3&quot;)</pre>
<h3>FindLibXml2</h3>
<p>Try to find the LibXml2 xml processing library </p>
<p> Once done this will define </p>
<pre>LIBXML2_FOUND - System has LibXml2
LIBXML2_INCLUDE_DIR - The LibXml2 include directory
LIBXML2_LIBRARIES - The libraries needed to use LibXml2
LIBXML2_DEFINITIONS - Compiler switches required for using LibXml2
LIBXML2_XMLLINT_EXECUTABLE - The XML checking tool xmllint coming with LibXml2
LIBXML2_VERSION_STRING - the version of LibXml2 found (since CMake 2.8.8)</pre>
<h3>FindLibXslt</h3>
<p>Try to find the LibXslt library </p>
<p> Once done this will define </p>
<pre>LIBXSLT_FOUND - system has LibXslt
LIBXSLT_INCLUDE_DIR - the LibXslt include directory
LIBXSLT_LIBRARIES - Link these to LibXslt
LIBXSLT_DEFINITIONS - Compiler switches required for using LibXslt
LIBXSLT_VERSION_STRING - version of LibXslt found (since CMake 2.8.8)</pre>
<p>Additionally, the following two variables are set (but not required for using xslt):</p>
<dl>
<dt><code>LIBXSLT_EXSLT_LIBRARIES</code></p>
<dd>Link to these if you need to link against the exslt library.</p>
<dt><code>LIBXSLT_XSLTPROC_EXECUTABLE</code></p>
<dd>Contains the full path to the xsltproc executable if found.</dl>
<h3>FindLTTngUST</h3>
<p>This module finds the <i>LTTng-UST</i> library.</p>
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
<h3>FindLua50</h3>
<p>Locate Lua library This module defines </p>
<pre>LUA50_FOUND, if false, do not try to link to Lua
LUA_LIBRARIES, both lua and lualib
LUA_INCLUDE_DIR, where to find lua.h and lualib.h (and probably lauxlib.h)</pre>
<p>Note that the expected include convention is </p>
<pre>#include &quot;lua.h&quot;</pre>
<p>and not </p>
<pre>#include &lt;lua/lua.h&gt;</pre>
<p>This is because, the lua location is not standardized and may exist in locations other than lua/</p>
<h3>FindLua51</h3>
<p>Locate Lua library This module defines </p>
<pre>LUA51_FOUND, if false, do not try to link to Lua
LUA_LIBRARIES
LUA_INCLUDE_DIR, where to find lua.h
LUA_VERSION_STRING, the version of Lua found (since CMake 2.8.8)</pre>
<p>Note that the expected include convention is </p>
<pre>#include &quot;lua.h&quot;</pre>
<p>and not </p>
<pre>#include &lt;lua/lua.h&gt;</pre>
<p>This is because, the lua location is not standardized and may exist in locations other than lua/</p>
<h3>FindLua</h3>
<p>Locate Lua library This module defines </p>
<pre>LUA_FOUND - if false, do not try to link to Lua
LUA_LIBRARIES - both lua and lualib
LUA_INCLUDE_DIR - where to find lua.h
LUA_VERSION_STRING - the version of Lua found
LUA_VERSION_MAJOR - the major version of Lua
LUA_VERSION_MINOR - the minor version of Lua
LUA_VERSION_PATCH - the patch version of Lua</pre>
<p>Note that the expected include convention is </p>
<pre>#include &quot;lua.h&quot;</pre>
<p>and not </p>
<pre>#include &lt;lua/lua.h&gt;</pre>
<p>This is because, the lua location is not standardized and may exist in locations other than lua/</p>
<h3>FindMatlab</h3>
<p>Finds Matlab installations and provides Matlab tools and libraries to cmake. </p>
<p> This package first intention is to find the libraries associated with Matlab in order to be able to build Matlab extensions (mex files). It can also be used:</p>
<dl>
<dt>&bull;</p>
<dd>run specific commands in Matlab</p>
<dt>&bull;</p>
<dd>declare Matlab unit test</p>
<dt>&bull;</p>
<dd>retrieve various information from Matlab (mex extensions, versions and release queries, &#8230;) </p>
<p> The module supports the following components:</p>
<dt>&bull;</p>
<dd><code>MX_LIBRARY</code> and <code>ENG_LIBRARY</code> respectively the MX and ENG libraries of Matlab</p>
<dt>&bull;</p>
<dd><code>MAIN_PROGRAM</code> the Matlab binary program. </p>
<p> <code>NOTE:</code> The version given to the <code>find_package()</code> directive is the Matlab <code>version</code>, which should not be confused with the Matlab <i>release</i> name (eg. <i>R2014</i>). The <code>matlab_get_version_from_release_name()</code> and <code>matlab_get_release_name_from_version()</code> allow a mapping from the release name to the version. </p>
<p> The variable <code>Matlab_ROOT_DIR</code> may be specified in order to give the path of the desired Matlab version. Otherwise, the behaviour is platform specific:</p>
<dt>&bull;</p>
<dd>Windows: The installed versions of Matlab are retrieved from the Windows registry</p>
<dt>&bull;</p>
<dd>OS X: The installed versions of Matlab are given by the MATLAB paths in <code>/Application</code>. If no such application is found, it falls back to the one that might be accessible from the PATH.</p>
<dt>&bull;</p>
<dd>Unix: The desired Matlab should be accessible from the PATH. </p>
<p> Additional information is provided when <code>MATLAB_FIND_DEBUG</code> is set. When a Matlab binary is found automatically and the <code>MATLAB_VERSION</code> is not given, the version is queried from Matlab directly. On Windows, it can make a window running Matlab appear. </p>
<p> The mapping of the release names and the version of Matlab is performed by defining pairs (name, version). The variable <code>MATLAB_ADDITIONAL_VERSIONS</code> may be provided before the call to the <code>find_package()</code> in order to handle additional versions. </p>
<p> A Matlab scripts can be added to the set of tests using the <code>matlab_add_unit_test()</code>. By default, the Matlab unit test framework will be used (&gt;= 2013a) to run this script, but regular <code>.m</code> files returning an exit code can be used as well (0 indicating a success).</dl>
<h3>Module Input Variables</h3>
<p>Users or projects may set the following variables to configure the module behaviour:</p>
<dl>
<dt><code>Matlab_ROOT_DIR</code></p>
<dd>the root of the Matlab installation.</p>
<dt><code>MATLAB_FIND_DEBUG</code></p>
<dd>outputs debug information</p>
<dt><code>MATLAB_ADDITIONAL_VERSIONS</code></p>
<dd>additional versions of Matlab for the automatic retrieval of the installed versions.</dl>
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
<dd>mx library of Matlab (arrays). Available only if the component <code>MX_LIBRARY</code> has been requested.</p>
<dt><code>Matlab_ENG_LIBRARY</code></p>
<dd>Matlab engine library. Available only if the component <code>ENG_LIBRARY</code> is requested.</p>
<dt><code>Matlab_LIBRARIES</code></p>
<dd>the whole set of libraries of Matlab</p>
<dt><code>Matlab_MEX_COMPILER</code></p>
<dd>the mex compiler of Matlab. Currently not used. Available only if the component <code>MEX_COMPILER</code> is asked</dl>
<h3>Cached variables</h3>
<dl>
<dt><code>Matlab_MEX_EXTENSION</code></p>
<dd>the extension of the mex files for the current platform (given by Matlab).</p>
<dt><code>Matlab_ROOT_DIR</code></p>
<dd>the location of the root of the Matlab installation found. If this value is changed by the user, the result variables are recomputed.</dl>
<h3>Provided macros</h3>
<dl>
<dt><code>matlab_get_version_from_release_name()</code></p>
<dd>returns the version from the release name</p>
<dt><code>matlab_get_release_name_from_version()</code></p>
<dd>returns the release name from the Matlab version</dl>
<h3>Provided functions</h3>
<dl>
<dt><code>matlab_add_mex()</code></p>
<dd>adds a target compiling a MEX file.</p>
<dt><code>matlab_add_unit_test()</code></p>
<dd>adds a Matlab unit test file as a test to the project.</p>
<dt><code>matlab_extract_all_installed_versions_from_registry()</code></p>
<dd>parses the registry for all Matlab versions. Available on Windows only. The part of the registry parsed is dependent on the host processor</p>
<dt><code>matlab_get_all_valid_matlab_roots_from_registry()</code></p>
<dd>returns all the possible Matlab paths, according to a previously given list. Only the existing/accessible paths are kept. This is mainly useful for the searching all possible Matlab installation.</p>
<dt><code>matlab_get_mex_suffix()</code></p>
<dd>returns the suffix to be used for the mex files (platform/architecture dependent)</p>
<dt><code>matlab_get_version_from_matlab_run()</code></p>
<dd>returns the version of Matlab, given the full directory of the Matlab program.</dl>
<h3>Known issues</h3>
<dl>
<dt><code>Symbol clash in a MEX target</code></p>
<dd>By default, every symbols inside a MEX file defined with the command <code>matlab_add_mex()</code> have hidden visibility, except for the entry point. This is the default behaviour of the MEX compiler, which lowers the risk of symbol collision between the libraries shipped with Matlab, and the libraries to which the MEX file is linking to. This is also the default on Windows platforms. </p>
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
<dd>If set, specifies additional versions of Matlab that may be looked for. The variable should be a list of strings, organised by pairs of release name and versions, such as follows: </p>
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
<dd>This function parses the registry and founds the Matlab versions that are installed. The found versions are returned in <i>matlab_versions</i>. Set <i>win64</i> to <i>TRUE</i> if the 64 bit version of Matlab should be looked for The returned list contains all versions under <code>HKLM\SOFTWARE\Mathworks\MATLAB</code> or an empty list in case an error occurred (or nothing found). </p>
<p> <code>NOTE:</code> Only the versions are provided. No check is made over the existence of the installation referenced in the registry,</p>
<dt><code>matlab_get_all_valid_matlab_roots_from_registry</code></p>
<dd>Populates the Matlab root with valid versions of Matlab. The returned matlab_roots is organized in pairs <code>(version_number,matlab_root_path)</code>. </p>
<pre>matlab_get_all_valid_matlab_roots_from_registry(
 matlab_versions
 matlab_roots)</pre>
<dt><code>matlab_versions</code></p>
<dd>the versions of each of the Matlab installations</p>
<dt><code>matlab_roots</code></p>
<dd>the location of each of the Matlab installations</p>
<dt><code>matlab_get_mex_suffix</code></p>
<dd>Returns the extension of the mex files (the suffixes). This function should not be called before the appropriate Matlab root has been found. </p>
<pre>matlab_get_mex_suffix(
 matlab_root
 mex_suffix)</pre>
<dt><code>matlab_root</code></p>
<dd>the root of the Matlab installation</p>
<dt><code>mex_suffix</code></p>
<dd>the variable name in which the suffix will be returned.</p>
<dt><code>matlab_get_version_from_matlab_run</code></p>
<dd>This function runs Matlab program specified on arguments and extracts its version. </p>
<pre>matlab_get_version_from_matlab_run(
 matlab_binary_path
 matlab_list_versions)</pre>
<dt><code>matlab_binary_path</code></p>
<dd>the location of the <i>matlab</i> binary executable</p>
<dt><code>matlab_list_versions</code></p>
<dd>the version extracted from Matlab</p>
<dt><code>matlab_add_unit_test</code></p>
<dd>Adds a Matlab unit test to the test set of cmake/ctest. This command requires the component <code>MAIN_PROGRAM</code>. The unit test uses the Matlab unittest framework (default, available starting Matlab 2013b+) except if the option <code>NO_UNITTEST_FRAMEWORK</code> is given. </p>
<p> The function expects one Matlab test script file to be given. In the case <code>NO_UNITTEST_FRAMEWORK</code> is given, the unittest script file should contain the script to be run, plus an exit command with the exit value. This exit value will be passed to the ctest framework (0 success, non 0 failure). Additional arguments accepted by <code>add_test()</code> can be passed through <code>TEST_ARGS</code> (eg. <code>CONFIGURATION &lt;config&gt; &#8230;</code>). </p>
<pre>matlab_add_unit_test(
 NAME &lt;name&gt;
 UNITTEST_FILE matlab_file_containing_unittest.m
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
<dt><code>UNITTEST_PRECOMMAND</code></p>
<dd>Matlab script command to be ran before the file containing the test (eg. GPU device initialisation based on CMake variables).</p>
<dt><code>TIMEOUT</code></p>
<dd>the test timeout in seconds. Defaults to 180 seconds as the Matlab unit test may hang.</p>
<dt><code>ADDITIONAL_PATH</code></p>
<dd>a list of paths to add to the Matlab path prior to running the unit test.</p>
<dt><code>MATLAB_ADDITIONAL_STARTUP_OPTIONS</code></p>
<dd>a list of additional option in order to run Matlab from the command line.</p>
<dt><code>TEST_ARGS</code></p>
<dd>Additional options provided to the add_test command. These options are added to the default options (eg. &quot;CONFIGURATIONS Release&quot;)</p>
<dt><code>NO_UNITTEST_FRAMEWORK</code></p>
<dd>when set, indicates that the test should not use the unittest framework of Matlab (available for versions &gt;= R2013a).</p>
<dt><code>matlab_add_mex</code></p>
<dd>Adds a Matlab MEX target. This commands compiles the given sources with the current tool-chain in order to produce a MEX file. The final name of the produced output may be specified, as well as additional link libraries, and a documentation entry for the MEX file. Remaining arguments of the call are passed to the <code>add_library()</code> command. </p>
<pre>matlab_add_mex(
 NAME &lt;name&gt;
 SRC src1 [src2 ...]
 [OUTPUT_NAME output_name]
 [DOCUMENTATION file.txt]
 [LINK_TO target1 target2 ...]
 [...]
)</pre>
<dt><code>NAME</code></p>
<dd>name of the target.</p>
<dt><code>SRC</code></p>
<dd>list of tje source files.</p>
<dt><code>LINK_TO</code></p>
<dd>a list of additional link dependencies. The target links to <code>libmex</code> by default. If <code>Matlab_MX_LIBRARY</code> is defined, it also links to <code>libmx</code>.</p>
<dt><code>OUTPUT_NAME</code></p>
<dd>if given, overrides the default name. The default name is the name of the target without any prefix and with <code>Matlab_MEX_EXTENSION</code> suffix.</p>
<dt><code>DOCUMENTATION</code></p>
<dd>if given, the file <code>file.txt</code> will be considered as being the documentation file for the MEX file. This file is copied into the same folder without any processing, with the same name as the final mex file, and with extension <i>.m</i>. In that case, typing <code>help &lt;name&gt;</code> in Matlab prints the documentation contained in this file. </p>
<p> The documentation file is not processed and should be in the following format: </p>
<pre>% This is the documentation
function ret = mex_target_output_name(input1)</pre>
</dl>
<h3>FindMFC</h3>
<p>Find MFC on Windows </p>
<p> Find the native MFC &#8211; i.e. decide if an application can link to the MFC libraries. </p>
<pre>MFC_FOUND - Was MFC support found</pre>
<p>You don&#8217;t need to include anything or link anything to use it.</p>
<h3>FindMotif</h3>
<p>Try to find Motif (or lesstif) </p>
<p> Once done this will define: </p>
<pre>MOTIF_FOUND - system has MOTIF
MOTIF_INCLUDE_DIR - include paths to use Motif
MOTIF_LIBRARIES - Link these to use Motif</pre>
<h3>FindMPEG2</h3>
<p>Find the native MPEG2 includes and library </p>
<p> This module defines </p>
<pre>MPEG2_INCLUDE_DIR, path to mpeg2dec/mpeg2.h, etc.
MPEG2_LIBRARIES, the libraries required to use MPEG2.
MPEG2_FOUND, If false, do not try to use MPEG2.</pre>
<p>also defined, but not for general use are </p>
<pre>MPEG2_mpeg2_LIBRARY, where to find the MPEG2 library.
MPEG2_vo_LIBRARY, where to find the vo library.</pre>
<h3>FindMPEG</h3>
<p>Find the native MPEG includes and library </p>
<p> This module defines </p>
<pre>MPEG_INCLUDE_DIR, where to find MPEG.h, etc.
MPEG_LIBRARIES, the libraries required to use MPEG.
MPEG_FOUND, If false, do not try to use MPEG.</pre>
<p>also defined, but not for general use are </p>
<pre>MPEG_mpeg2_LIBRARY, where to find the MPEG library.
MPEG_vo_LIBRARY, where to find the vo library.</pre>
<h3>FindMPI</h3>
<p>Find a Message Passing Interface (MPI) implementation </p>
<p> The Message Passing Interface (MPI) is a library used to write high-performance distributed-memory parallel applications, and is typically deployed on a cluster. MPI is a standard interface (defined by the MPI forum) for which many implementations are available. All of them have somewhat different include paths, libraries to link against, etc., and this module tries to smooth out those differences.</p>
<h3>Variables</h3>
<p>This module will set the following variables per language in your project, where &lt;lang&gt; is one of C, CXX, or Fortran: </p>
<pre>MPI_&lt;lang&gt;_FOUND TRUE if FindMPI found MPI flags for &lt;lang&gt;
MPI_&lt;lang&gt;_COMPILER MPI Compiler wrapper for &lt;lang&gt;
MPI_&lt;lang&gt;_COMPILE_FLAGS Compilation flags for MPI programs
MPI_&lt;lang&gt;_INCLUDE_PATH Include path(s) for MPI header
MPI_&lt;lang&gt;_LINK_FLAGS Linking flags for MPI programs
MPI_&lt;lang&gt;_LIBRARIES All libraries to link MPI programs against</pre>
<p>Additionally, FindMPI sets the following variables for running MPI programs from the command line: </p>
<pre>MPIEXEC Executable for running MPI programs
MPIEXEC_NUMPROC_FLAG Flag to pass to MPIEXEC before giving
 it the number of processors to run on
MPIEXEC_PREFLAGS Flags to pass to MPIEXEC directly
 before the executable to run.
MPIEXEC_POSTFLAGS Flags to pass to MPIEXEC after other flags</pre>
<h3>Usage</h3>
<p>To use this module, simply call FindMPI from a CMakeLists.txt file, or run <code>find_package(MPI)</code>, then run CMake. If you are happy with the auto-detected configuration for your language, then you&#8217;re done. If not, you have two options: </p>
<pre>1. Set MPI_&lt;lang&gt;_COMPILER to the MPI wrapper (mpicc, etc.) of your
 choice and reconfigure. FindMPI will attempt to determine all the
 necessary variables using THAT compiler's compile and link flags.
2. If this fails, or if your MPI implementation does not come with
 a compiler wrapper, then set both MPI_&lt;lang&gt;_LIBRARIES and
 MPI_&lt;lang&gt;_INCLUDE_PATH. You may also set any other variables
 listed above, but these two are required. This will circumvent
 autodetection entirely.</pre>
<p>When configuration is successful, <code>MPI_&lt;lang&gt;_COMPILER</code> will be set to the compiler wrapper for &lt;lang&gt;, if it was found. <code>MPI_&lt;lang&gt;_FOUND</code> and other variables above will be set if any MPI implementation was found for &lt;lang&gt;, regardless of whether a compiler was found. </p>
<p> When using <code>MPIEXEC</code> to execute MPI applications, you should typically use all of the <code>MPIEXEC</code> flags as follows: </p>
<pre>${MPIEXEC} ${MPIEXEC_NUMPROC_FLAG} PROCS
 ${MPIEXEC_PREFLAGS} EXECUTABLE ${MPIEXEC_POSTFLAGS} ARGS</pre>
<p>where <code>PROCS</code> is the number of processors on which to execute the program, <code>EXECUTABLE</code> is the MPI program, and <code>ARGS</code> are the arguments to pass to the MPI program.</p>
<h3>Backward Compatibility</h3>
<p>For backward compatibility with older versions of FindMPI, these variables are set, but deprecated: </p>
<pre>MPI_FOUND MPI_COMPILER MPI_LIBRARY
MPI_COMPILE_FLAGS MPI_INCLUDE_PATH MPI_EXTRA_LIBRARY
MPI_LINK_FLAGS MPI_LIBRARIES</pre>
<p>In new projects, please use the <code>MPI_&lt;lang&gt;_XXX</code> equivalents.</p>
<h3>FindOpenAL</h3>
<p>Locate OpenAL This module defines OPENAL_LIBRARY OPENAL_FOUND, if false, do not try to link to OpenAL OPENAL_INCLUDE_DIR, where to find the headers </p>
<p> $OPENALDIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing. This was influenced by the FindSDL.cmake module.</p>
<h3>FindOpenCL</h3>
<p>Try to find OpenCL </p>
<p> Once done this will define: </p>
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
<p>FindModule for OpenGL and GLU.</p>
<h3>Result Variables</h3>
<p>This module sets the following variables:</p>
<dl>
<dt><code>OPENGL_FOUND</code></p>
<dd>True, if the system has OpenGL.</p>
<dt><code>OPENGL_XMESA_FOUND</code></p>
<dd>True, if the system has XMESA.</p>
<dt><code>OPENGL_GLU_FOUND</code></p>
<dd>True, if the system has GLU.</p>
<dt><code>OPENGL_INCLUDE_DIR</code></p>
<dd>Path to the OpenGL include directory.</p>
<dt><code>OPENGL_LIBRARIES</code></p>
<dd>Paths to the OpenGL and GLU libraries. </p>
<p> If you want to use just GL you can use these values:</p>
<dt><code>OPENGL_gl_LIBRARY</code></p>
<dd>Path to the OpenGL library.</p>
<dt><code>OPENGL_glu_LIBRARY</code></p>
<dd>Path to the GLU library.</dl>
<h3>OSX Specific</h3>
<p>On OSX default to using the framework version of OpenGL. People will have to change the cache values of OPENGL_glu_LIBRARY and OPENGL_gl_LIBRARY to use OpenGL with X11 on OSX.</p>
<h3>FindOpenMP</h3>
<p>Finds OpenMP support </p>
<p> This module can be used to detect OpenMP support in a compiler. If the compiler supports OpenMP, the flags required to compile with OpenMP support are returned in variables for the different languages. The variables may be empty if the compiler does not need a special flag to support OpenMP. </p>
<p> The following variables are set: </p>
<pre>OpenMP_C_FLAGS - flags to add to the C compiler for OpenMP support
OpenMP_CXX_FLAGS - flags to add to the CXX compiler for OpenMP support
OpenMP_Fortran_FLAGS - flags to add to the Fortran compiler for OpenMP support
OPENMP_FOUND - true if openmp is detected</pre>
<p>Supported compilers can be found at <i><a rel="nofollow" href="http://openmp.org/wp/openmp-compilers/">http://openmp.org/wp/openmp-compilers/</a></i></p>
<h3>FindOpenSceneGraph</h3>
<p>Find OpenSceneGraph </p>
<p> This module searches for the OpenSceneGraph core &quot;osg&quot; library as well as OpenThreads, and whatever additional COMPONENTS (nodekits) that you specify. </p>
<pre>See <a rel="nofollow" href="http://www.openscenegraph.org">http://www.openscenegraph.org</a></pre>
<p>NOTE: To use this module effectively you must either require CMake &gt;= 2.6.3 with cmake_minimum_required(VERSION 2.6.3) or download and place FindOpenThreads.cmake, Findosg_functions.cmake, Findosg.cmake, and Find&lt;etc&gt;.cmake files into your CMAKE_MODULE_PATH. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<p> This module accepts the following variables (note mixed case) </p>
<pre>OpenSceneGraph_DEBUG - Enable debugging output</pre>
<pre>OpenSceneGraph_MARK_AS_ADVANCED - Mark cache variables as advanced
 automatically</pre>
<p>The following environment variables are also respected for finding the OSG and it&#8217;s various components. CMAKE_PREFIX_PATH can also be used for this (see find_library() CMake documentation).</p>
<dl>
<dt><code>&lt;MODULE&gt;_DIR</code></p>
<dd>(where MODULE is of the form &quot;OSGVOLUME&quot; and there is a FindosgVolume.cmake file)</p>
<dt><code>OSG_DIR</code></p>
<dd>
<dt><code>OSGDIR</code></p>
<dd>
<dt><code>OSG_ROOT</code></p>
<dd>[CMake 2.8.10]: The CMake variable OSG_DIR can now be used as well to influence detection, instead of needing to specify an environment variable. </p>
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
<p>Find the OpenSSL encryption library.</p>
<h3>Imported Targets</h3>
<p>This module defines the following <code>IMPORTED</code> targets:</p>
<dl>
<dt><code>OpenSSL::SSL</code></p>
<dd>The OpenSSL <code>ssl</code> library, if found.</p>
<dt><code>OpenSSL::Crypto</code></p>
<dd>The OpenSSL <code>crypto</code> library, if found.</dl>
<h3>Result Variables</h3>
<p>This module will set the following variables in your project:</p>
<dl>
<dt><code>OPENSSL_FOUND</code></p>
<dd>System has the OpenSSL library.</p>
<dt><code>OPENSSL_INCLUDE_DIR</code></p>
<dd>The OpenSSL include directory.</p>
<dt><code>OPENSSL_CRYPTO_LIBRARY</code></p>
<dd>The OpenSSL crypto library.</p>
<dt><code>OPENSSL_SSL_LIBRARY</code></p>
<dd>The OpenSSL SSL library.</p>
<dt><code>OPENSSL_LIBRARIES</code></p>
<dd>All OpenSSL libraries.</p>
<dt><code>OPENSSL_VERSION</code></p>
<dd>This is set to <code>$major.$minor.$revision$patch</code> (e.g. <code>0.9.8s</code>).</dl>
<h3>Hints</h3>
<p>Set <code>OPENSSL_ROOT_DIR</code> to the root directory of an OpenSSL installation. Set <code>OPENSSL_USE_STATIC_LIBS</code> to <code>TRUE</code> to look for static libraries. Set <code>OPENSSL_MSVC_STATIC_RT</code> set <code>TRUE</code> to choose the MT version of the lib.</p>
<h3>FindOpenThreads</h3>
<p>OpenThreads is a C++ based threading library. Its largest userbase seems to OpenSceneGraph so you might notice I accept OSGDIR as an environment path. I consider this part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. </p>
<p> Locate OpenThreads This module defines OPENTHREADS_LIBRARY OPENTHREADS_FOUND, if false, do not try to link to OpenThreads OPENTHREADS_INCLUDE_DIR, where to find the headers </p>
<p> $OPENTHREADS_DIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OPENTHREADS_DIR used in building osg. </p>
<p> [CMake 2.8.10]: The CMake variables OPENTHREADS_DIR or OSG_DIR can now be used as well to influence detection, instead of needing to specify an environment variable. </p>
<p> Created by Eric Wing.</p>
<h3>FindosgAnimation</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgAnimation This module defines </p>
<p> OSGANIMATION_FOUND &#8211; Was osgAnimation found? OSGANIMATION_INCLUDE_DIR &#8211; Where to find the headers OSGANIMATION_LIBRARIES &#8211; The libraries to link against for the OSG (use this) </p>
<p> OSGANIMATION_LIBRARY &#8211; The OSG library OSGANIMATION_LIBRARY_DEBUG &#8211; The OSG debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing.</p>
<h3>FindosgDB</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgDB This module defines </p>
<p> OSGDB_FOUND &#8211; Was osgDB found? OSGDB_INCLUDE_DIR &#8211; Where to find the headers OSGDB_LIBRARIES &#8211; The libraries to link against for the osgDB (use this) </p>
<p> OSGDB_LIBRARY &#8211; The osgDB library OSGDB_LIBRARY_DEBUG &#8211; The osgDB debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing.</p>
<h3>Findosg_functions</h3>
<p>This CMake file contains two macros to assist with searching for OSG libraries and nodekits. Please see FindOpenSceneGraph.cmake for full documentation.</p>
<h3>FindosgFX</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgFX This module defines </p>
<p> OSGFX_FOUND &#8211; Was osgFX found? OSGFX_INCLUDE_DIR &#8211; Where to find the headers OSGFX_LIBRARIES &#8211; The libraries to link against for the osgFX (use this) </p>
<p> OSGFX_LIBRARY &#8211; The osgFX library OSGFX_LIBRARY_DEBUG &#8211; The osgFX debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing.</p>
<h3>FindosgGA</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgGA This module defines </p>
<p> OSGGA_FOUND &#8211; Was osgGA found? OSGGA_INCLUDE_DIR &#8211; Where to find the headers OSGGA_LIBRARIES &#8211; The libraries to link against for the osgGA (use this) </p>
<p> OSGGA_LIBRARY &#8211; The osgGA library OSGGA_LIBRARY_DEBUG &#8211; The osgGA debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing.</p>
<h3>FindosgIntrospection</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgINTROSPECTION This module defines </p>
<p> OSGINTROSPECTION_FOUND &#8211; Was osgIntrospection found? OSGINTROSPECTION_INCLUDE_DIR &#8211; Where to find the headers OSGINTROSPECTION_LIBRARIES &#8211; The libraries to link for osgIntrospection (use this) </p>
<p> OSGINTROSPECTION_LIBRARY &#8211; The osgIntrospection library OSGINTROSPECTION_LIBRARY_DEBUG &#8211; The osgIntrospection debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing.</p>
<h3>FindosgManipulator</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgManipulator This module defines </p>
<p> OSGMANIPULATOR_FOUND &#8211; Was osgManipulator found? OSGMANIPULATOR_INCLUDE_DIR &#8211; Where to find the headers OSGMANIPULATOR_LIBRARIES &#8211; The libraries to link for osgManipulator (use this) </p>
<p> OSGMANIPULATOR_LIBRARY &#8211; The osgManipulator library OSGMANIPULATOR_LIBRARY_DEBUG &#8211; The osgManipulator debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing.</p>
<h3>FindosgParticle</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgParticle This module defines </p>
<p> OSGPARTICLE_FOUND &#8211; Was osgParticle found? OSGPARTICLE_INCLUDE_DIR &#8211; Where to find the headers OSGPARTICLE_LIBRARIES &#8211; The libraries to link for osgParticle (use this) </p>
<p> OSGPARTICLE_LIBRARY &#8211; The osgParticle library OSGPARTICLE_LIBRARY_DEBUG &#8211; The osgParticle debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing.</p>
<h3>FindosgPresentation</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgPresentation This module defines </p>
<p> OSGPRESENTATION_FOUND &#8211; Was osgPresentation found? OSGPRESENTATION_INCLUDE_DIR &#8211; Where to find the headers OSGPRESENTATION_LIBRARIES &#8211; The libraries to link for osgPresentation (use this) </p>
<p> OSGPRESENTATION_LIBRARY &#8211; The osgPresentation library OSGPRESENTATION_LIBRARY_DEBUG &#8211; The osgPresentation debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing. Modified to work with osgPresentation by Robert Osfield, January 2012.</p>
<h3>FindosgProducer</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgProducer This module defines </p>
<p> OSGPRODUCER_FOUND &#8211; Was osgProducer found? OSGPRODUCER_INCLUDE_DIR &#8211; Where to find the headers OSGPRODUCER_LIBRARIES &#8211; The libraries to link for osgProducer (use this) </p>
<p> OSGPRODUCER_LIBRARY &#8211; The osgProducer library OSGPRODUCER_LIBRARY_DEBUG &#8211; The osgProducer debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing.</p>
<h3>FindosgQt</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgQt This module defines </p>
<p> OSGQT_FOUND &#8211; Was osgQt found? OSGQT_INCLUDE_DIR &#8211; Where to find the headers OSGQT_LIBRARIES &#8211; The libraries to link for osgQt (use this) </p>
<p> OSGQT_LIBRARY &#8211; The osgQt library OSGQT_LIBRARY_DEBUG &#8211; The osgQt debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing. Modified to work with osgQt by Robert Osfield, January 2012.</p>
<h3>Findosg</h3>
<p>NOTE: It is highly recommended that you use the new FindOpenSceneGraph.cmake introduced in CMake 2.6.3 and not use this Find module directly. </p>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osg This module defines </p>
<p> OSG_FOUND &#8211; Was the Osg found? OSG_INCLUDE_DIR &#8211; Where to find the headers OSG_LIBRARIES &#8211; The libraries to link against for the OSG (use this) </p>
<p> OSG_LIBRARY &#8211; The OSG library OSG_LIBRARY_DEBUG &#8211; The OSG debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing.</p>
<h3>FindosgShadow</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgShadow This module defines </p>
<p> OSGSHADOW_FOUND &#8211; Was osgShadow found? OSGSHADOW_INCLUDE_DIR &#8211; Where to find the headers OSGSHADOW_LIBRARIES &#8211; The libraries to link for osgShadow (use this) </p>
<p> OSGSHADOW_LIBRARY &#8211; The osgShadow library OSGSHADOW_LIBRARY_DEBUG &#8211; The osgShadow debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing.</p>
<h3>FindosgSim</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgSim This module defines </p>
<p> OSGSIM_FOUND &#8211; Was osgSim found? OSGSIM_INCLUDE_DIR &#8211; Where to find the headers OSGSIM_LIBRARIES &#8211; The libraries to link for osgSim (use this) </p>
<p> OSGSIM_LIBRARY &#8211; The osgSim library OSGSIM_LIBRARY_DEBUG &#8211; The osgSim debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing.</p>
<h3>FindosgTerrain</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgTerrain This module defines </p>
<p> OSGTERRAIN_FOUND &#8211; Was osgTerrain found? OSGTERRAIN_INCLUDE_DIR &#8211; Where to find the headers OSGTERRAIN_LIBRARIES &#8211; The libraries to link for osgTerrain (use this) </p>
<p> OSGTERRAIN_LIBRARY &#8211; The osgTerrain library OSGTERRAIN_LIBRARY_DEBUG &#8211; The osgTerrain debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing.</p>
<h3>FindosgText</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgText This module defines </p>
<p> OSGTEXT_FOUND &#8211; Was osgText found? OSGTEXT_INCLUDE_DIR &#8211; Where to find the headers OSGTEXT_LIBRARIES &#8211; The libraries to link for osgText (use this) </p>
<p> OSGTEXT_LIBRARY &#8211; The osgText library OSGTEXT_LIBRARY_DEBUG &#8211; The osgText debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing.</p>
<h3>FindosgUtil</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgUtil This module defines </p>
<p> OSGUTIL_FOUND &#8211; Was osgUtil found? OSGUTIL_INCLUDE_DIR &#8211; Where to find the headers OSGUTIL_LIBRARIES &#8211; The libraries to link for osgUtil (use this) </p>
<p> OSGUTIL_LIBRARY &#8211; The osgUtil library OSGUTIL_LIBRARY_DEBUG &#8211; The osgUtil debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing.</p>
<h3>FindosgViewer</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgViewer This module defines </p>
<p> OSGVIEWER_FOUND &#8211; Was osgViewer found? OSGVIEWER_INCLUDE_DIR &#8211; Where to find the headers OSGVIEWER_LIBRARIES &#8211; The libraries to link for osgViewer (use this) </p>
<p> OSGVIEWER_LIBRARY &#8211; The osgViewer library OSGVIEWER_LIBRARY_DEBUG &#8211; The osgViewer debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing.</p>
<h3>FindosgVolume</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgVolume This module defines </p>
<p> OSGVOLUME_FOUND &#8211; Was osgVolume found? OSGVOLUME_INCLUDE_DIR &#8211; Where to find the headers OSGVOLUME_LIBRARIES &#8211; The libraries to link for osgVolume (use this) </p>
<p> OSGVOLUME_LIBRARY &#8211; The osgVolume library OSGVOLUME_LIBRARY_DEBUG &#8211; The osgVolume debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing.</p>
<h3>FindosgWidget</h3>
<p>This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgWidget This module defines </p>
<p> OSGWIDGET_FOUND &#8211; Was osgWidget found? OSGWIDGET_INCLUDE_DIR &#8211; Where to find the headers OSGWIDGET_LIBRARIES &#8211; The libraries to link for osgWidget (use this) </p>
<p> OSGWIDGET_LIBRARY &#8211; The osgWidget library OSGWIDGET_LIBRARY_DEBUG &#8211; The osgWidget debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the </p>
<p> FindosgWidget.cmake tweaked from Findosg* suite as created by Eric Wing.</p>
<h3>FindPackageHandleStandardArgs</h3>
<p>This module provides a function intended to be used in <i>Find Modules</i> implementing <code>find_package(&lt;PackageName&gt;)</code> calls. It handles the <code>REQUIRED</code>, <code>QUIET</code> and version-related arguments of <code>find_package</code>. It also sets the <code>&lt;PackageName&gt;_FOUND</code> variable. The package is considered found if all variables listed contain valid results, e.g. valid filepaths.</p>
<dl>
<dt><code>find_package_handle_standard_args</code></p>
<dd>There are two signatures: </p>
<pre>find_package_handle_standard_args(&lt;PackageName&gt;
 (DEFAULT_MSG|&lt;custom-failure-message&gt;)
 &lt;required-var&gt;...
 )
find_package_handle_standard_args(&lt;PackageName&gt;
 [FOUND_VAR &lt;result-var&gt;]
 [REQUIRED_VARS &lt;required-var&gt;...]
 [VERSION_VAR &lt;version-var&gt;]
 [HANDLE_COMPONENTS]
 [CONFIG_MODE]
 [FAIL_MESSAGE &lt;custom-failure-message&gt;]
 )</pre>
<p>The <code>&lt;PackageName&gt;_FOUND</code> variable will be set to <code>TRUE</code> if all the variables <code>&lt;required-var&gt;&#8230;</code> are valid and any optional constraints are satisfied, and <code>FALSE</code> otherwise. A success or failure message may be displayed based on the results and on whether the <code>REQUIRED</code> and/or <code>QUIET</code> option was given to the <code>find_package()</code> call. </p>
<p> The options are:</p>
<dt><code>(DEFAULT_MSG|&lt;custom-failure-message&gt;)</code></p>
<dd>In the simple signature this specifies the failure message. Use <code>DEFAULT_MSG</code> to ask for a default message to be computed (recommended). Not valid in the full signature.</p>
<dt><code>FOUND_VAR &lt;result-var&gt;</code></p>
<dd>Obsolete. Specifies either <code>&lt;PackageName&gt;_FOUND</code> or <code>&lt;PACKAGENAME&gt;_FOUND</code> as the result variable. This exists only for compatibility with older versions of CMake and is now ignored. Result variables of both names are always set for compatibility.</p>
<dt><code>REQUIRED_VARS &lt;required-var&gt;&#8230;</code></p>
<dd>Specify the variables which are required for this package. These may be named in the generated failure message asking the user to set the missing variable values. Therefore these should typically be cache entries such as <code>FOO_LIBRARY</code> and not output variables like <code>FOO_LIBRARIES</code>.</p>
<dt><code>VERSION_VAR &lt;version-var&gt;</code></p>
<dd>Specify the name of a variable that holds the version of the package that has been found. This version will be checked against the (potentially) specified required version given to the <code>find_package()</code> call, including its <code>EXACT</code> option. The default messages include information about the required version and the version which has been actually found, both if the version is ok or not.</p>
<dt><code>HANDLE_COMPONENTS</code></p>
<dd>Enable handling of package components. In this case, the command will report which components have been found and which are missing, and the <code>&lt;PackageName&gt;_FOUND</code> variable will be set to <code>FALSE</code> if any of the required components (i.e. not the ones listed after the <code>OPTIONAL_COMPONENTS</code> option of <code>find_package()</code>) are missing.</p>
<dt><code>CONFIG_MODE</code></p>
<dd>Specify that the calling find module is a wrapper around a call to <code>find_package(&lt;PackageName&gt; NO_MODULE)</code>. This implies a <code>VERSION_VAR</code> value of <code>&lt;PackageName&gt;_VERSION</code>. The command will automatically check whether the package configuration file was found.</p>
<dt><code>FAIL_MESSAGE &lt;custom-failure-message&gt;</code></p>
<dd>Specify a custom failure message instead of using the default generated message. Not recommended. </p>
<p> Example for the simple signature: </p>
<pre>find_package_handle_standard_args(LibXml2 DEFAULT_MSG
 LIBXML2_LIBRARY LIBXML2_INCLUDE_DIR)</pre>
<p>The <code>LibXml2</code> package is considered to be found if both <code>LIBXML2_LIBRARY</code> and <code>LIBXML2_INCLUDE_DIR</code> are valid. Then also <code>LibXml2_FOUND</code> is set to <code>TRUE</code>. If it is not found and <code>REQUIRED</code> was used, it fails with a <code>message(FATAL_ERROR)</code>, independent whether <code>QUIET</code> was used or not. If it is found, success will be reported, including the content of the first <code>&lt;required-var&gt;</code>. On repeated CMake runs, the same message will not be printed again. </p>
<p> Example for the full signature: </p>
<pre>find_package_handle_standard_args(LibArchive
 REQUIRED_VARS LibArchive_LIBRARY LibArchive_INCLUDE_DIR
 VERSION_VAR LibArchive_VERSION)</pre>
<p>In this case, the <code>LibArchive</code> package is considered to be found if both <code>LibArchive_LIBRARY</code> and <code>LibArchive_INCLUDE_DIR</code> are valid. Also the version of <code>LibArchive</code> will be checked by using the version contained in <code>LibArchive_VERSION</code>. Since no <code>FAIL_MESSAGE</code> is given, the default messages will be printed. </p>
<p> Another example for the full signature: </p>
<pre>find_package(Automoc4 QUIET NO_MODULE HINTS /opt/automoc4)
find_package_handle_standard_args(Automoc4 CONFIG_MODE)</pre>
<p>In this case, a <code>FindAutmoc4.cmake</code> module wraps a call to <code>find_package(Automoc4 NO_MODULE)</code> and adds an additional search directory for <code>automoc4</code>. Then the call to <code>find_package_handle_standard_args</code> produces a proper success/failure message.</dl>
<h3>FindPackageMessage</h3>
<p>FIND_PACKAGE_MESSAGE(&lt;name&gt; &quot;message for user&quot; &quot;find result details&quot;) </p>
<p> This macro is intended to be used in FindXXX.cmake modules files. It will print a message once for each unique find result. This is useful for telling the user where a package was found. The first argument specifies the name (XXX) of the package. The second argument specifies the message to display. The third argument lists details about the find result so that if they change the message will be displayed again. The macro also obeys the QUIET argument to the find_package command. </p>
<p> Example: </p>
<pre>if(X11_FOUND)
 FIND_PACKAGE_MESSAGE(X11 &quot;Found X11: ${X11_X11_LIB}&quot;
 &quot;[${X11_X11_LIB}][${X11_INCLUDE_DIR}]&quot;)
else()
 ...
endif()</pre>
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
<pre>PERL_SITESEARCH = path to the sitesearch install dir
PERL_SITELIB = path to the sitelib install directory
PERL_VENDORARCH = path to the vendor arch install directory
PERL_VENDORLIB = path to the vendor lib install directory
PERL_ARCHLIB = path to the arch lib install directory
PERL_PRIVLIB = path to the priv lib install directory
PERL_EXTRA_C_FLAGS = Compilation flags used to build perl</pre>
<h3>FindPerl</h3>
<p>Find perl </p>
<p> this module looks for Perl </p>
<pre>PERL_EXECUTABLE - the full path to perl
PERL_FOUND - If false, don't attempt to use perl.
PERL_VERSION_STRING - version of perl found (since CMake 2.8.8)</pre>
<h3>FindPHP4</h3>
<p>Find PHP4 </p>
<p> This module finds if PHP4 is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>PHP4_INCLUDE_PATH = path to where php.h can be found
PHP4_EXECUTABLE = full path to the php4 binary</pre>
<h3>FindPhysFS</h3>
<p>Locate PhysFS library This module defines PHYSFS_LIBRARY, the name of the library to link against PHYSFS_FOUND, if false, do not try to link to PHYSFS PHYSFS_INCLUDE_DIR, where to find physfs.h </p>
<p> $PHYSFSDIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing.</p>
<h3>FindPike</h3>
<p>Find Pike </p>
<p> This module finds if PIKE is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>PIKE_INCLUDE_PATH = path to where program.h is found
PIKE_EXECUTABLE = full path to the pike binary</pre>
<h3>FindPkgConfig</h3>
<p>A <i>pkg-config</i> module for CMake. </p>
<p> Finds the <code>pkg-config</code> executable and add the <code>pkg_check_modules()</code> and <code>pkg_search_module()</code> commands. </p>
<p> In order to find the <code>pkg-config</code> executable, it uses the <code>PKG_CONFIG_EXECUTABLE</code> variable or the <code>PKG_CONFIG</code> environment variable first.</p>
<dl>
<dt><code>pkg_get_variable</code></p>
<dd>Retrieves the value of a variable from a package: </p>
<pre>pkg_get_variable(&lt;RESULT&gt; &lt;MODULE&gt; &lt;VARIABLE&gt;)</pre>
<p>For example: </p>
<pre>pkg_get_variable(GI_GIRDIR gobject-introspection-1.0 girdir)</pre>
<dt><code>pkg_check_modules</code></p>
<dd>Checks for all the given modules. </p>
<pre>pkg_check_modules(&lt;PREFIX&gt; [REQUIRED] [QUIET]
 [NO_CMAKE_PATH] [NO_CMAKE_ENVIRONMENT_PATH]
 [IMPORTED_TARGET]
 &lt;MODULE&gt; [&lt;MODULE&gt;]*)</pre>
<p>When the <code>REQUIRED</code> argument was set, macros will fail with an error when module(s) could not be found. </p>
<p> When the <code>QUIET</code> argument is set, no status messages will be printed. </p>
<p> By default, if <code>CMAKE_MINIMUM_REQUIRED_VERSION</code> is 3.1 or later, or if <code>PKG_CONFIG_USE_CMAKE_PREFIX_PATH</code> is set, the <code>CMAKE_PREFIX_PATH</code>, <code>CMAKE_FRAMEWORK_PATH</code>, and <code>CMAKE_APPBUNDLE_PATH</code> cache and environment variables will be added to <code>pkg-config</code> search path. The <code>NO_CMAKE_PATH</code> and <code>NO_CMAKE_ENVIRONMENT_PATH</code> arguments disable this behavior for the cache variables and the environment variables, respectively. The <code>IMPORTED_TARGET</code> argument will create an imported target named PkgConfig::&lt;PREFIX&gt;&gt; that can be passed directly as an argument to <code>target_link_libraries()</code>. </p>
<p> It sets the following variables: </p>
<pre>PKG_CONFIG_FOUND ... if pkg-config executable was found
PKG_CONFIG_EXECUTABLE ... pathname of the pkg-config program
PKG_CONFIG_VERSION_STRING ... the version of the pkg-config program found
 (since CMake 2.8.8)</pre>
<p>For the following variables two sets of values exist; first one is the common one and has the given PREFIX. The second set contains flags which are given out when <code>pkg-config</code> was called with the <code>&#8211;static</code> option. </p>
<pre>&lt;XPREFIX&gt;_FOUND ... set to 1 if module(s) exist
&lt;XPREFIX&gt;_LIBRARIES ... only the libraries (w/o the '-l')
&lt;XPREFIX&gt;_LIBRARY_DIRS ... the paths of the libraries (w/o the '-L')
&lt;XPREFIX&gt;_LDFLAGS ... all required linker flags
&lt;XPREFIX&gt;_LDFLAGS_OTHER ... all other linker flags
&lt;XPREFIX&gt;_INCLUDE_DIRS ... the '-I' preprocessor flags (w/o the '-I')
&lt;XPREFIX&gt;_CFLAGS ... all required cflags
&lt;XPREFIX&gt;_CFLAGS_OTHER ... the other compiler flags</pre>
<pre>&lt;XPREFIX&gt; = &lt;PREFIX&gt; for common case
&lt;XPREFIX&gt; = &lt;PREFIX&gt;_STATIC for static linking</pre>
<p>There are some special variables whose prefix depends on the count of given modules. When there is only one module, &lt;PREFIX&gt; stays unchanged. When there are multiple modules, the prefix will be changed to &lt;PREFIX&gt;_&lt;MODNAME&gt;: </p>
<pre>&lt;XPREFIX&gt;_VERSION ... version of the module
&lt;XPREFIX&gt;_PREFIX ... prefix-directory of the module
&lt;XPREFIX&gt;_INCLUDEDIR ... include-dir of the module
&lt;XPREFIX&gt;_LIBDIR ... lib-dir of the module</pre>
<pre>&lt;XPREFIX&gt; = &lt;PREFIX&gt; when |MODULES| == 1, else
&lt;XPREFIX&gt; = &lt;PREFIX&gt;_&lt;MODNAME&gt;</pre>
<p>A &lt;MODULE&gt; parameter can have the following formats: </p>
<pre>{MODNAME} ... matches any version
{MODNAME}&gt;={VERSION} ... at least version &lt;VERSION&gt; is required
{MODNAME}={VERSION} ... exactly version &lt;VERSION&gt; is required
{MODNAME}&lt;={VERSION} ... modules must not be newer than &lt;VERSION&gt;</pre>
<p>Examples </p>
<pre>pkg_check_modules (GLIB2 glib-2.0)</pre>
<pre>pkg_check_modules (GLIB2 glib-2.0&gt;=2.10)</pre>
<p>Requires at least version 2.10 of glib2 and defines e.g. <code>GLIB2_VERSION=2.10.3</code> </p>
<pre>pkg_check_modules (FOO glib-2.0&gt;=2.10 gtk+-2.0)</pre>
<p>Requires both glib2 and gtk2, and defines e.g. <code>FOO_glib-2.0_VERSION=2.10.3</code> and <code>FOO_gtk+-2.0_VERSION=2.8.20</code> </p>
<pre>pkg_check_modules (XRENDER REQUIRED xrender)</pre>
<p>Defines for example: </p>
<pre>XRENDER_LIBRARIES=Xrender;X11``
XRENDER_STATIC_LIBRARIES=Xrender;X11;pthread;Xau;Xdmcp</pre>
<dt><code>pkg_search_module</code></p>
<dd>Same as <code>pkg_check_modules()</code>, but instead it checks for given modules and uses the first working one. </p>
<pre>pkg_search_module(&lt;PREFIX&gt; [REQUIRED] [QUIET]
 [NO_CMAKE_PATH] [NO_CMAKE_ENVIRONMENT_PATH]
 [IMPORTED_TARGET]
 &lt;MODULE&gt; [&lt;MODULE&gt;]*)</pre>
<p>Examples </p>
<pre>pkg_search_module (BAR libxml-2.0 libxml2 libxml&gt;=2)</pre>
<dt><code>PKG_CONFIG_EXECUTABLE</code></p>
<dd>Path to the pkg-config executable.</p>
<dt><code>PKG_CONFIG_USE_CMAKE_PREFIX_PATH</code></p>
<dd>Whether <code>pkg_check_modules()</code> and <code>pkg_search_module()</code> should add the paths in <code>CMAKE_PREFIX_PATH</code>, <code>CMAKE_FRAMEWORK_PATH</code>, and <code>CMAKE_APPBUNDLE_PATH</code> cache and environment variables to <code>pkg-config</code> search path. </p>
<p> If this variable is not set, this behavior is enabled by default if <code>CMAKE_MINIMUM_REQUIRED_VERSION</code> is 3.1 or later, disabled otherwise.</dl>
<h3>FindPNG</h3>
<p>Find libpng, the official reference library for the PNG image format.</p>
<h3>Imported targets</h3>
<p>This module defines the following <code>IMPORTED</code> target:</p>
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
<dd>You should add_definitons(${PNG_DEFINITIONS}) before compiling code that includes png library files.</p>
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
<p>Find the PostgreSQL installation. </p>
<p> This module defines </p>
<pre>PostgreSQL_LIBRARIES - the PostgreSQL libraries needed for linking
PostgreSQL_INCLUDE_DIRS - the directories of the PostgreSQL headers
PostgreSQL_LIBRARY_DIRS - the link directories for PostgreSQL libraries
PostgreSQL_VERSION_STRING - the version of PostgreSQL found (since CMake 2.8.8)</pre>
<h3>FindProducer</h3>
<p>Though Producer isn&#8217;t directly part of OpenSceneGraph, its primary user is OSG so I consider this part of the Findosg* suite used to find OpenSceneGraph components. You&#8217;ll notice that I accept OSGDIR as an environment path. </p>
<p> Each component is separate and you must opt in to each module. You must also opt into OpenGL (and OpenThreads?) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate Producer This module defines PRODUCER_LIBRARY PRODUCER_FOUND, if false, do not try to link to Producer PRODUCER_INCLUDE_DIR, where to find the headers </p>
<p> $PRODUCER_DIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing.</p>
<h3>FindProtobuf</h3>
<p>Locate and configure the Google Protocol Buffers library. </p>
<p> The following variables can be set and are optional:</p>
<dl>
<dt><code>Protobuf_SRC_ROOT_FOLDER</code></p>
<dd>When compiling with MSVC, if this cache variable is set the protobuf-default VS project build locations (vsprojects/Debug and vsprojects/Release or vsprojects/x64/Debug and vsprojects/x64/Release) will be searched for libraries and binaries.</p>
<dt><code>Protobuf_IMPORT_DIRS</code></p>
<dd>List of additional directories to be searched for imported .proto files.</p>
<dt><code>Protobuf_DEBUG</code></p>
<dd>Show debug messages. </p>
<p> Defines the following variables:</p>
<dt><code>Protobuf_FOUND</code></p>
<dd>Found the Google Protocol Buffers library (libprotobuf &amp; header files)</p>
<dt><code>Protobuf_VERSION</code></p>
<dd>Version of package found.</p>
<dt><code>Protobuf_INCLUDE_DIRS</code></p>
<dd>Include directories for Google Protocol Buffers</p>
<dt><code>Protobuf_LIBRARIES</code></p>
<dd>The protobuf libraries</p>
<dt><code>Protobuf_PROTOC_LIBRARIES</code></p>
<dd>The protoc libraries</p>
<dt><code>Protobuf_LITE_LIBRARIES</code></p>
<dd>The protobuf-lite libraries </p>
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
protobuf_generate_python(PROTO_PY foo.proto)
add_executable(bar bar.cc ${PROTO_SRCS} ${PROTO_HDRS})
target_link_libraries(bar ${Protobuf_LIBRARIES})</pre>
<p><code>NOTE:</code> The <code>protobuf_generate_cpp</code> and <code>protobuf_generate_python</code> functions and <code>add_executable()</code> or <code>add_library()</code> calls only work properly within the same directory.</p>
<dt><code>protobuf_generate_cpp</code></p>
<dd>Add custom commands to process <code>.proto</code> files to C++: </p>
<pre>protobuf_generate_cpp (&lt;SRCS&gt; &lt;HDRS&gt; [&lt;ARGN&gt;...])</pre>
<dt><code>SRCS</code></p>
<dd>Variable to define with autogenerated source files</p>
<dt><code>HDRS</code></p>
<dd>Variable to define with autogenerated header files</p>
<dt><code>ARGN</code></p>
<dd><code>.proto</code> files</p>
<dt><code>protobuf_generate_python</code></p>
<dd>Add custom commands to process <code>.proto</code> files to Python: </p>
<pre>protobuf_generate_python (&lt;PY&gt; [&lt;ARGN&gt;...])</pre>
<dt><code>PY</code></p>
<dd>Variable to define with autogenerated Python files</p>
<dt><code>ARGN</code></p>
<dd><code>.proto</code> filess</dl>
<h3>FindPythonInterp</h3>
<p>Find python interpreter </p>
<p> This module finds if Python interpreter is installed and determines where the executables are. This code sets the following variables: </p>
<pre>PYTHONINTERP_FOUND - Was the Python executable found
PYTHON_EXECUTABLE - path to the Python interpreter</pre>
<pre>PYTHON_VERSION_STRING - Python version found e.g. 2.5.2
PYTHON_VERSION_MAJOR - Python major version found e.g. 2
PYTHON_VERSION_MINOR - Python minor version found e.g. 5
PYTHON_VERSION_PATCH - Python patch version found e.g. 2</pre>
<p>The Python_ADDITIONAL_VERSIONS variable can be used to specify a list of version numbers that should be taken into account when searching for Python. You need to set this variable before calling find_package(PythonInterp). </p>
<p> If calling both <code>find_package(PythonInterp)</code> and <code>find_package(PythonLibs)</code>, call <code>find_package(PythonInterp)</code> first to get the currently active Python version by default with a consistent version of PYTHON_LIBRARIES.</p>
<h3>FindPythonLibs</h3>
<p>Find python libraries </p>
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
 generates commands to create .ts (vie lupdate) and .qm
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
<h3>FindQt</h3>
<p>Searches for all installed versions of Qt. </p>
<p> This should only be used if your project can work with multiple versions of Qt. If not, you should just directly use FindQt4 or FindQt3. If multiple versions of Qt are found on the machine, then The user must set the option DESIRED_QT_VERSION to the version they want to use. If only one version of qt is found on the machine, then the DESIRED_QT_VERSION is set to that version and the matching FindQt3 or FindQt4 module is included. Once the user sets DESIRED_QT_VERSION, then the FindQt3 or FindQt4 module is included. </p>
<p> This module can only detect and switch between Qt versions 3 and 4. It cannot handle Qt5 or any later versions. </p>
<pre>QT_REQUIRED if this is set to TRUE then if CMake can
 not find Qt4 or Qt3 an error is raised
 and a message is sent to the user.</pre>
<pre>DESIRED_QT_VERSION OPTION is created
QT4_INSTALLED is set to TRUE if qt4 is found.
QT3_INSTALLED is set to TRUE if qt3 is found.</pre>
<h3>FindQuickTime</h3>
<p>Locate QuickTime This module defines QUICKTIME_LIBRARY QUICKTIME_FOUND, if false, do not try to link to gdal QUICKTIME_INCLUDE_DIR, where to find the headers </p>
<p> $QUICKTIME_DIR is an environment variable that would correspond to the </p>
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
<p> This module finds if Ruby is installed and determines where the include files and libraries are. Ruby 1.8, 1.9, 2.0 and 2.1 are supported. </p>
<p> The minimum required version of Ruby can be specified using the standard syntax, e.g. find_package(Ruby 1.8) </p>
<p> It also determines what the name of the library is. This code sets the following variables:</p>
<dl>
<dt><code>RUBY_EXECUTABLE</code></p>
<dd>full path to the ruby binary</p>
<dt><code>RUBY_INCLUDE_DIRS</code></p>
<dd>include dirs to be used when using the ruby library</p>
<dt><code>RUBY_LIBRARY</code></p>
<dd>full path to the ruby library</p>
<dt><code>RUBY_VERSION</code></p>
<dd>the version of ruby which was found, e.g. &quot;1.8.7&quot;</p>
<dt><code>RUBY_FOUND</code></p>
<dd>set to true if ruby ws found successfully </p>
<p> Also:</p>
<dt><code>RUBY_INCLUDE_PATH</code></p>
<dd>same as RUBY_INCLUDE_DIRS, only provided for compatibility reasons, don&#8217;t use it</dl>
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
<p>$SDLDIR is an environment variable that would correspond to the </p>
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
<p>$SDLDIR is an environment variable that would correspond to the </p>
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
<p>$SDLDIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing. This was influenced by the FindSDL.cmake module, but with modifications to recognize OS X frameworks and additional Unix paths (FreeBSD, etc).</p>
<h3>FindSDL</h3>
<p>Locate SDL library </p>
<p> This module defines </p>
<pre>SDL_LIBRARY, the name of the library to link against
SDL_FOUND, if false, do not try to link to SDL
SDL_INCLUDE_DIR, where to find SDL.h
SDL_VERSION_STRING, human-readable string containing the version of SDL</pre>
<p>This module responds to the flag: </p>
<pre>SDL_BUILDING_LIBRARY
 If this is defined, then no SDL_main will be linked in because
 only applications need main().
 Otherwise, it is assumed you are building an application and this
 module will attempt to locate and set the proper link flags
 as part of the returned SDL_LIBRARY variable.</pre>
<p>Don&#8217;t forget to include SDLmain.h and SDLmain.m your project for the OS X framework based version. (Other versions link to -lSDLmain which this module will try to find on your behalf.) Also for OS X, this module will automatically add the -framework Cocoa on your behalf. </p>
<p> Additional Note: If you see an empty SDL_LIBRARY_TEMP in your configuration and no SDL_LIBRARY, it means CMake did not find your SDL library (SDL.dll, libsdl.so, SDL.framework, etc). Set SDL_LIBRARY_TEMP to point to your SDL library, and configure again. Similarly, if you see an empty SDLMAIN_LIBRARY, you should set this value as appropriate. These values are used to generate the final SDL_LIBRARY variable, but when these values are unset, SDL_LIBRARY does not get created. </p>
<p> $SDLDIR is an environment variable that would correspond to the </p>
<p> Modified by Eric Wing. Added code to assist with automated building by using environmental variables and providing a more controlled/consistent search behavior. Added new modifications to recognize OS X frameworks and additional Unix paths (FreeBSD, etc). Also corrected the header search path to follow &quot;proper&quot; SDL guidelines. Added a search for SDLmain which is needed by some platforms. Added a search for threads which is needed by some platforms. Added needed compile switches for MinGW. </p>
<p> On OSX, this will prefer the Framework version (if found) over others. People will have to manually change the cache values of SDL_LIBRARY to override this selection or set the CMake environment CMAKE_INCLUDE_PATH to modify the search paths. </p>
<p> Note that the header path has changed from SDL/SDL.h to just SDL.h This needed to change because &quot;proper&quot; SDL convention is #include &quot;SDL.h&quot;, not &lt;SDL/SDL.h&gt;. This is done for portability reasons because not all systems place things in SDL/ (see FreeBSD).</p>
<h3>FindSDL_sound</h3>
<p>Locates the SDL_sound library </p>
<p> This module depends on SDL being found and must be called AFTER FindSDL.cmake is called. </p>
<p> This module defines </p>
<pre>SDL_SOUND_INCLUDE_DIR, where to find SDL_sound.h
SDL_SOUND_FOUND, if false, do not try to link to SDL_sound
SDL_SOUND_LIBRARIES, this contains the list of libraries that you need
 to link against. This is a read-only variable and is marked INTERNAL.
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
<p>$SDLDIR is an environment variable that would correspond to the </p>
<p> Created by Eric Wing. This was influenced by the FindSDL.cmake module, but with modifications to recognize OS X frameworks and additional Unix paths (FreeBSD, etc).</p>
<h3>FindSelfPackers</h3>
<p>Find upx </p>
<p> This module looks for some executable packers (i.e. software that compress executables or shared libs into on-the-fly self-extracting executables or shared libs. Examples: </p>
<pre>UPX: <a rel="nofollow" href="http://wildsau.idv.uni-linz.ac.at/mfx/upx.html">http://wildsau.idv.uni-linz.ac.at/mfx/upx.html</a></pre>
<h3>FindSquish</h3>
<p>&#8212; Typical Use </p>
<p> This module can be used to find Squish. Currently Squish versions 3 and 4 are supported. </p>
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
<p>It provides the function squish_v4_add_test() for adding a squish test to cmake using Squish 4.x: </p>
<pre>squish_v4_add_test(cmakeTestName
 AUT targetName SUITE suiteName TEST squishTestName
 [SETTINGSGROUP group] [PRE_COMMAND command] [POST_COMMAND command] )</pre>
<p>The arguments have the following meaning:</p>
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
<dd>if specified, the given settings group will be used for executing the test. If not specified, the groupname will be &quot;CTest_&lt;username&gt;&quot;</p>
<dt><code>PRE_COMMAND command</code></p>
<dd>if specified, the given command will be executed before starting the squish test.</p>
<dt><code>POST_COMMAND command</code></p>
<dd>same as PRE_COMMAND, but after the squish test has been executed. </p>
<pre>enable_testing()
find_package(Squish 4.0)
if (SQUISH_FOUND)
 squish_v4_add_test(myTestName
 AUT myApp
 SUITE ${CMAKE_SOURCE_DIR}/tests/mySuite
 TEST someSquishTest
 SETTINGSGROUP myGroup
 )
endif ()</pre>
<p>For users of Squish version 3.x the macro squish_v3_add_test() is provided: </p>
<pre>squish_v3_add_test(testName applicationUnderTest testCase envVars testWrapper)
Use this macro to add a test using Squish 3.x.</pre>
<pre>enable_testing()
find_package(Squish)
if (SQUISH_FOUND)
 squish_v3_add_test(myTestName myApplication testCase envVars testWrapper)
endif ()</pre>
<p>macro SQUISH_ADD_TEST(testName applicationUnderTest testCase envVars testWrapper) </p>
<pre>This is deprecated. Use SQUISH_V3_ADD_TEST() if you are using Squish 3.x instead.</pre>
</dl>
<h3>FindSubversion</h3>
<p>Extract information from a subversion working copy </p>
<p> The module defines the following variables: </p>
<pre>Subversion_SVN_EXECUTABLE - path to svn command line client
Subversion_VERSION_SVN - version of svn command line client
Subversion_FOUND - true if the command line client was found
SUBVERSION_FOUND - same as Subversion_FOUND, set for compatibility reasons</pre>
<p>The minimum required version of Subversion can be specified using the standard syntax, e.g. find_package(Subversion 1.4) </p>
<p> If the command line client executable is found two macros are defined: </p>
<pre>Subversion_WC_INFO(&lt;dir&gt; &lt;var-prefix&gt;)
Subversion_WC_LOG(&lt;dir&gt; &lt;var-prefix&gt;)</pre>
<p>Subversion_WC_INFO extracts information of a subversion working copy at a given location. This macro defines the following variables: </p>
<pre>&lt;var-prefix&gt;_WC_URL - url of the repository (at &lt;dir&gt;)
&lt;var-prefix&gt;_WC_ROOT - root url of the repository
&lt;var-prefix&gt;_WC_REVISION - current revision
&lt;var-prefix&gt;_WC_LAST_CHANGED_AUTHOR - author of last commit
&lt;var-prefix&gt;_WC_LAST_CHANGED_DATE - date of last commit
&lt;var-prefix&gt;_WC_LAST_CHANGED_REV - revision of last commit
&lt;var-prefix&gt;_WC_INFO - output of command `svn info &lt;dir&gt;'</pre>
<p>Subversion_WC_LOG retrieves the log message of the base revision of a subversion working copy at a given location. This macro defines the variable: </p>
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
<p>Find SWIG </p>
<p> This module finds an installed SWIG. It sets the following variables: </p>
<pre>SWIG_FOUND - set to true if SWIG is found
SWIG_DIR - the directory where swig is installed
SWIG_EXECUTABLE - the path to the swig executable
SWIG_VERSION - the version number of the swig executable</pre>
<p>The minimum required version of SWIG can be specified using the standard syntax, e.g. find_package(SWIG 1.1) </p>
<p> All information is collected from the SWIG_EXECUTABLE so the version to be found can be changed from the command line by means of setting SWIG_EXECUTABLE</p>
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
<p>In an effort to remove some clutter and clear up some issues for people who are not necessarily Tcl/Tk gurus/developpers, some variables were moved or removed. Changes compared to CMake 2.4 are: </p>
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
<p>In cygwin, look for the cygwin version first. Don&#8217;t look for it later to avoid finding the cygwin version on a Win32 build.</p>
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
<p>In an effort to remove some clutter and clear up some issues for people who are not necessarily Tcl/Tk gurus/developpers, some variables were moved or removed. Changes compared to CMake 2.4 are: </p>
<pre>=&gt; these libs are not packaged by default with Tcl/Tk distributions.
 Even when Tcl/Tk is built from source, several flavors of debug libs
 are created and there is no real reason to pick a single one
 specifically (say, amongst tclstub84g, tclstub84gs, or tclstub84sgx).
 Let's leave that choice to the user by allowing him to assign
 TCL_STUB_LIBRARY to any Tcl library, debug or not.</pre>
<h3>FindThreads</h3>
<p>This module determines the thread library of the system. </p>
<p> The following variables are set </p>
<pre>CMAKE_THREAD_LIBS_INIT - the thread library
CMAKE_USE_SPROC_INIT - are we using sproc?
CMAKE_USE_WIN32_THREADS_INIT - using WIN32 threads?
CMAKE_USE_PTHREADS_INIT - are we using pthreads
CMAKE_HP_PTHREADS_INIT - are we using hp pthreads</pre>
<p>The following import target is created </p>
<pre>Threads::Threads</pre>
<p>For systems with multiple thread libraries, caller can set </p>
<pre>CMAKE_THREAD_PREFER_PTHREAD</pre>
<p>If the use of the -pthread compiler and linker flag is preferred then the caller can set </p>
<pre>THREADS_PREFER_PTHREAD_FLAG</pre>
<p>Please note that the compiler flag can only be used with the imported target. Use of both the imported target as well as this switch is highly recommended for new code.</p>
<h3>FindTIFF</h3>
<p>Find the TIFF library (libtiff).</p>
<h3>Imported targets</h3>
<p>This module defines the following <code>IMPORTED</code> targets:</p>
<dl>
<dt><code>TIFF::TIFF</code></p>
<dd>The TIFF library, if found.</dl>
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
<dt><code>TIFF_LIBRARY</code></p>
<dd>the path to the TIFF library</dl>
<h3>FindUnixCommands</h3>
<p>Find Unix commands, including the ones from Cygwin </p>
<p> This module looks for the Unix commands bash, cp, gzip, mv, rm, and tar and stores the result in the variables BASH, CP, GZIP, MV, RM, and TAR.</p>
<h3>FindVTK</h3>
<p>This module no longer exists. </p>
<p> This module existed in versions of CMake prior to 3.1, but became only a thin wrapper around <code>find_package(VTK NO_MODULE)</code> to provide compatibility for projects using long-outdated conventions. Now <code>find_package(VTK)</code> will search for <code>VTKConfig.cmake</code> directly.</p>
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
<p> find_package(wxWidgets COMPONENTS core base &#8230;) </p>
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
<p>Sample usage: </p>
<pre># Note that for MinGW users the order of libs is important!
find_package(wxWidgets COMPONENTS net gl core base)
if(wxWidgets_FOUND)
 include(${wxWidgets_USE_FILE})
 # and for each of your dependent executable/library targets:
 target_link_libraries(&lt;YourTarget&gt; ${wxWidgets_LIBRARIES})
endif()</pre>
<p>If wxWidgets is required (i.e., not an optional part): </p>
<pre>find_package(wxWidgets REQUIRED net gl core base)
include(${wxWidgets_USE_FILE})
# and for each of your dependent executable/library targets:
target_link_libraries(&lt;YourTarget&gt; ${wxWidgets_LIBRARIES})</pre>
<h3>FindwxWindows</h3>
<p>Find wxWindows (wxWidgets) installation </p>
<p> This module finds if wxWindows/wxWidgets is installed and determines where the include files and libraries are. It also determines what the name of the library is. Please note this file is DEPRECATED and replaced by FindwxWidgets.cmake. This code sets the following variables: </p>
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
<h3>FindXCTest</h3>
<p>Functions to help creating and executing XCTest bundles. </p>
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
<h3>FindXalanC</h3>
<p>Find the Apache Xalan-C++ XSL transform processor headers and libraries.</p>
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
<h3>FindXercesC</h3>
<p>Find the Apache Xerces-C++ validating XML parser headers and libraries.</p>
<h3>Imported targets</h3>
<p>This module defines the following <code>IMPORTED</code> targets:</p>
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
<dd>the Xerces library</dl>
<h3>FindX11</h3>
<p>Find X11 installation </p>
<p> Try to find X11 on UNIX systems. The following values are defined </p>
<pre>X11_FOUND - True if X11 is available
X11_INCLUDE_DIR - include directories to use X11
X11_LIBRARIES - link against these to use X11</pre>
<p>and also the following more fine grained variables: </p>
<pre>X11_ICE_INCLUDE_PATH, X11_ICE_LIB, X11_ICE_FOUND
X11_SM_INCLUDE_PATH, X11_SM_LIB, X11_SM_FOUND
X11_X11_INCLUDE_PATH, X11_X11_LIB
X11_Xaccessrules_INCLUDE_PATH, X11_Xaccess_FOUND
X11_Xaccessstr_INCLUDE_PATH, X11_Xaccess_FOUND
X11_Xau_INCLUDE_PATH, X11_Xau_LIB, X11_Xau_FOUND
X11_Xcomposite_INCLUDE_PATH, X11_Xcomposite_LIB, X11_Xcomposite_FOUND
X11_Xcursor_INCLUDE_PATH, X11_Xcursor_LIB, X11_Xcursor_FOUND
X11_Xdamage_INCLUDE_PATH, X11_Xdamage_LIB, X11_Xdamage_FOUND
X11_Xdmcp_INCLUDE_PATH, X11_Xdmcp_LIB, X11_Xdmcp_FOUND
X11_Xext_LIB, X11_Xext_FOUND
X11_dpms_INCLUDE_PATH, (in X11_Xext_LIB), X11_dpms_FOUND
X11_XShm_INCLUDE_PATH, (in X11_Xext_LIB), X11_XShm_FOUND
X11_Xshape_INCLUDE_PATH, (in X11_Xext_LIB), X11_Xshape_FOUND
X11_xf86misc_INCLUDE_PATH, X11_Xxf86misc_LIB, X11_xf86misc_FOUND
X11_xf86vmode_INCLUDE_PATH, X11_Xxf86vm_LIB X11_xf86vmode_FOUND
X11_Xfixes_INCLUDE_PATH, X11_Xfixes_LIB, X11_Xfixes_FOUND
X11_Xft_INCLUDE_PATH, X11_Xft_LIB, X11_Xft_FOUND
X11_Xi_INCLUDE_PATH, X11_Xi_LIB, X11_Xi_FOUND
X11_Xinerama_INCLUDE_PATH, X11_Xinerama_LIB, X11_Xinerama_FOUND
X11_Xinput_INCLUDE_PATH, X11_Xinput_LIB, X11_Xinput_FOUND
X11_Xkb_INCLUDE_PATH, X11_Xkb_FOUND
X11_Xkblib_INCLUDE_PATH, X11_Xkb_FOUND
X11_Xkbfile_INCLUDE_PATH, X11_Xkbfile_LIB, X11_Xkbfile_FOUND
X11_Xmu_INCLUDE_PATH, X11_Xmu_LIB, X11_Xmu_FOUND
X11_Xpm_INCLUDE_PATH, X11_Xpm_LIB, X11_Xpm_FOUND
X11_XTest_INCLUDE_PATH, X11_XTest_LIB, X11_XTest_FOUND
X11_Xrandr_INCLUDE_PATH, X11_Xrandr_LIB, X11_Xrandr_FOUND
X11_Xrender_INCLUDE_PATH, X11_Xrender_LIB, X11_Xrender_FOUND
X11_Xscreensaver_INCLUDE_PATH, X11_Xscreensaver_LIB, X11_Xscreensaver_FOUND
X11_Xt_INCLUDE_PATH, X11_Xt_LIB, X11_Xt_FOUND
X11_Xutil_INCLUDE_PATH, X11_Xutil_FOUND
X11_Xv_INCLUDE_PATH, X11_Xv_LIB, X11_Xv_FOUND
X11_XSync_INCLUDE_PATH, (in X11_Xext_LIB), X11_XSync_FOUND</pre>
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
<p>This module defines <code>IMPORTED</code> target <code>ZLIB::ZLIB</code>, if ZLIB has been found.</p>
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
<h3>Backward Compatibility</h3>
<p>The following variable are provided for backward compatibility </p>
<pre>ZLIB_MAJOR_VERSION - The major version of zlib
ZLIB_MINOR_VERSION - The minor version of zlib
ZLIB_PATCH_VERSION - The patch version of zlib</pre>
<h3>Hints</h3>
<p>A user may set <code>ZLIB_ROOT</code> to a zlib installation root to tell this module where to look.</p>
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
<p> This module provides the function GENERATE_EXPORT_HEADER(). </p>
<p> The <code>GENERATE_EXPORT_HEADER</code> function can be used to generate a file suitable for preprocessor inclusion which contains EXPORT macros to be used in library classes: </p>
<pre>GENERATE_EXPORT_HEADER( LIBRARY_TARGET
 [BASE_NAME &lt;base_name&gt;]
 [EXPORT_MACRO_NAME &lt;export_macro_name&gt;]
 [EXPORT_FILE_NAME &lt;export_file_name&gt;]
 [DEPRECATED_MACRO_NAME &lt;deprecated_macro_name&gt;]
 [NO_EXPORT_MACRO_NAME &lt;no_export_macro_name&gt;]
 [STATIC_DEFINE &lt;static_define&gt;]
 [NO_DEPRECATED_MACRO_NAME &lt;no_deprecated_macro_name&gt;]
 [DEFINE_NO_DEPRECATED]
 [PREFIX_NAME &lt;prefix_name&gt;]
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
<p>The CMake fragment will generate a file in the <code>${CMAKE_CURRENT_BINARY_DIR}</code> called <code>somelib_export.h</code> containing the macros <code>SOMELIB_EXPORT</code>, <code>SOMELIB_NO_EXPORT</code>, <code>SOMELIB_DEPRECATED</code>, <code>SOMELIB_DEPRECATED_EXPORT</code> and <code>SOMELIB_DEPRECATED_NO_EXPORT</code>. The resulting file should be installed with other headers in the library. </p>
<p> The <code>BASE_NAME</code> argument can be used to override the file name and the names used for the macros: </p>
<pre>add_library(somelib someclass.cpp)
generate_export_header(somelib
 BASE_NAME other_name
)</pre>
<p>Generates a file called <code>other_name_export.h</code> containing the macros <code>OTHER_NAME_EXPORT</code>, <code>OTHER_NAME_NO_EXPORT</code> and <code>OTHER_NAME_DEPRECATED</code> etc. </p>
<p> The <code>BASE_NAME</code> may be overridden by specifiying other options in the function. For example: </p>
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
<pre>ADD_COMPILER_EXPORT_FLAGS( [&lt;output_variable&gt;] )</pre>
<p>The <code>ADD_COMPILER_EXPORT_FLAGS</code> function adds <code>-fvisibility=hidden</code> to <code>CMAKE_CXX_FLAGS</code> if supported, and is a no-op on Windows which does not need extra compiler flags for exporting support. You may optionally pass a single argument to <code>ADD_COMPILER_EXPORT_FLAGS</code> that will be populated with the <code>CXX_FLAGS</code> required to enable visibility support for the compiler/architecture in use. </p>
<p> This function is deprecated. Set the target properties <code>CXX_VISIBILITY_PRESET</code> and <code>VISIBILITY_INLINES_HIDDEN</code> instead.</p>
<h3>GetPrerequisites</h3>
<p>Functions to analyze and list executable file prerequisites. </p>
<p> This module provides functions to list the .dll, .dylib or .so files that an executable or shared library file depends on. (Its prerequisites.) </p>
<p> It uses various tools to obtain the list of required shared library files: </p>
<pre>dumpbin (Windows)
objdump (MinGW on Windows)
ldd (Linux/Unix)
otool (Mac OSX)</pre>
<p>The following functions are provided by this module: </p>
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
<p>Requires CMake 2.6 or greater because it uses function, break, return and PARENT_SCOPE. </p>
<pre>GET_PREREQUISITES(&lt;target&gt; &lt;prerequisites_var&gt; &lt;exclude_system&gt; &lt;recurse&gt;
 &lt;exepath&gt; &lt;dirs&gt; [&lt;rpaths&gt;])</pre>
<p>Get the list of shared library files required by &lt;target&gt;. The list in the variable named &lt;prerequisites_var&gt; should be empty on first entry to this function. On exit, &lt;prerequisites_var&gt; will contain the list of required shared library files. </p>
<p> &lt;target&gt; is the full path to an executable file. &lt;prerequisites_var&gt; is the name of a CMake variable to contain the results. &lt;exclude_system&gt; must be 0 or 1 indicating whether to include or exclude &quot;system&quot; prerequisites. If &lt;recurse&gt; is set to 1 all prerequisites will be found recursively, if set to 0 only direct prerequisites are listed. &lt;exepath&gt; is the path to the top level executable used for @executable_path replacment on the Mac. &lt;dirs&gt; is a list of paths where libraries might be found: these paths are searched first when a target without any path info is given. Then standard system locations are also searched: PATH, Framework locations, /usr/lib&#8230; </p>
<pre>LIST_PREREQUISITES(&lt;target&gt; [&lt;recurse&gt; [&lt;exclude_system&gt; [&lt;verbose&gt;]]])</pre>
<p>Print a message listing the prerequisites of &lt;target&gt;. </p>
<p> &lt;target&gt; is the name of a shared library or executable target or the full path to a shared library or executable file. If &lt;recurse&gt; is set to 1 all prerequisites will be found recursively, if set to 0 only direct prerequisites are listed. &lt;exclude_system&gt; must be 0 or 1 indicating whether to include or exclude &quot;system&quot; prerequisites. With &lt;verbose&gt; set to 0 only the full path names of the prerequisites are printed, set to 1 extra informatin will be displayed. </p>
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
<p> <code>CMAKE_INSTALL_&lt;dir&gt;</code> Destination for files of a given type. This value may be passed to the <code>DESTINATION</code> options of <code>install()</code> commands for the corresponding file type. </p>
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
<p>The following values of <code>CMAKE_INSTALL_PREFIX</code> are special: </p>
<p> <code>/</code> For <code>&lt;dir&gt;</code> other than the <code>SYSCONFDIR</code> and <code>LOCALSTATEDIR</code>, the value of <code>CMAKE_INSTALL_&lt;dir&gt;</code> is prefixed with <code>usr/</code> if it is not user-specified as an absolute path. For example, the <code>INCLUDEDIR</code> value <code>include</code> becomes <code>usr/include</code>. This is required by the <i>GNU Coding Standards</i>, which state: When building the complete GNU system, the prefix will be empty and <code>/usr</code> will be a symbolic link to <code>/</code>. </p>
<p> <code>/usr</code> For <code>&lt;dir&gt;</code> equal to <code>SYSCONFDIR</code> or <code>LOCALSTATEDIR</code>, the <code>CMAKE_INSTALL_FULL_&lt;dir&gt;</code> is computed by prepending just <code>/</code> to the value of <code>CMAKE_INSTALL_&lt;dir&gt;</code> if it is not user-specified as an absolute path. For example, the <code>SYSCONFDIR</code> value <code>etc</code> becomes <code>/etc</code>. This is required by the <i>GNU Coding Standards</i>. </p>
<p> <code>/opt/&#8230;</code> For <code>&lt;dir&gt;</code> equal to <code>SYSCONFDIR</code> or <code>LOCALSTATEDIR</code>, the <code>CMAKE_INSTALL_FULL_&lt;dir&gt;</code> is computed by <i>appending</i> the prefix to the value of <code>CMAKE_INSTALL_&lt;dir&gt;</code> if it is not user-specified as an absolute path. For example, the <code>SYSCONFDIR</code> value <code>etc</code> becomes <code>/etc/opt/&#8230;</code>. This is defined by the <i>Filesystem Hierarchy Standard</i>.</p>
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
<dd>Set to TRUE to install the Windows Universal CRT libraries for app-local deployment (e.g. to Windows XP). This is meaningful only with MSVC from Visual Studio 2015 or higher.</p>
<dt><code>CMAKE_INSTALL_MFC_LIBRARIES</code></p>
<dd>Set to TRUE to install the MSVC MFC runtime libraries.</p>
<dt><code>CMAKE_INSTALL_OPENMP_LIBRARIES</code></p>
<dd>Set to TRUE to install the MSVC OpenMP runtime libraries</p>
<dt><code>CMAKE_INSTALL_SYSTEM_RUNTIME_DESTINATION</code></p>
<dd>Specify the <code>install(PROGRAMS)</code> command <code>DESTINATION</code> option. If not specified, the default is <code>bin</code> on Windows and <code>lib</code> elsewhere.</p>
<dt><code>CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS_NO_WARNINGS</code></p>
<dd>Set to TRUE to disable warnings about required library files that do not exist. (For example, Visual Studio Express editions may not provide the redistributable files.)</p>
<dt><code>CMAKE_INSTALL_SYSTEM_RUNTIME_COMPONENT</code></p>
<dd>Specify the <code>install(PROGRAMS)</code> command <code>COMPONENT</code> option. If not specified, no such option will be used.</dl>
<h3>MacroAddFileDependencies</h3>
<p>MACRO_ADD_FILE_DEPENDENCIES(&lt;_file&gt; depend_files&#8230;) </p>
<p> Using the macro MACRO_ADD_FILE_DEPENDENCIES() is discouraged. There are usually better ways to specify the correct dependencies. </p>
<p> MACRO_ADD_FILE_DEPENDENCIES(&lt;_file&gt; depend_files&#8230;) is just a convenience wrapper around the OBJECT_DEPENDS source file property. You can just use set_property(SOURCE &lt;file&gt; APPEND PROPERTY OBJECT_DEPENDS depend_files) instead.</p>
<h3>ProcessorCount</h3>
<p>ProcessorCount(var) </p>
<p> Determine the number of processors/cores and save value in ${var} </p>
<p> Sets the variable named ${var} to the number of physical cores available on the machine if the information can be determined. Otherwise it is set to 0. Currently this functionality is implemented for AIX, cygwin, FreeBSD, HPUX, IRIX, Linux, Mac OS X, QNX, Sun and Windows. </p>
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
<p>select_library_configurations( basename ) </p>
<p> This macro takes a library base name as an argument, and will choose good values for basename_LIBRARY, basename_LIBRARIES, basename_LIBRARY_DEBUG, and basename_LIBRARY_RELEASE depending on what has been found and set. If only basename_LIBRARY_RELEASE is defined, basename_LIBRARY will be set to the release value, and basename_LIBRARY_DEBUG will be set to basename_LIBRARY_DEBUG-NOTFOUND. If only basename_LIBRARY_DEBUG is defined, then basename_LIBRARY will take the debug value, and basename_LIBRARY_RELEASE will be set to basename_LIBRARY_RELEASE-NOTFOUND. </p>
<p> If the generator supports configuration types, then basename_LIBRARY and basename_LIBRARIES will be set with debug and optimized flags specifying the library to be used for the given configuration. If no build type has been set or the generator in use does not support configuration types, then basename_LIBRARY and basename_LIBRARIES will take only the release value, or the debug value if the release one is not set.</p>
<h3>SquishTestScript</h3>
<p>This script launches a GUI test using Squish. You should not call the script directly; instead, you should access it via the SQUISH_ADD_TEST macro that is defined in FindSquish.cmake. </p>
<p> This script starts the Squish server, launches the test on the client, and finally stops the squish server. If any of these steps fail (including if the tests do not pass) then a fatal error is raised.</p>
<h3>TestBigEndian</h3>
<p>Define macro to determine endian type </p>
<p> Check if the system is big endian or little endian </p>
<pre>TEST_BIG_ENDIAN(VARIABLE)
VARIABLE - variable to store the result to</pre>
<h3>TestCXXAcceptsFlag</h3>
<p>Deprecated. See <code>CheckCXXCompilerFlag</code>. </p>
<p> Check if the CXX compiler accepts a flag. </p>
<pre>CHECK_CXX_ACCEPTS_FLAG(&lt;flags&gt; &lt;variable&gt;)</pre>
<dl>
<dt><code>&lt;flags&gt;</code></p>
<dd>the flags to try</p>
<dt><code>&lt;variable&gt;</code></p>
<dd>variable to store the result</dl>
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
<h3>UseJavaClassFilelist</h3>
<p>This script create a list of compiled Java class files to be added to a jar file. This avoids including cmake files which get created in the binary directory.</p>
<h3>UseJava</h3>
<p>Use Module for Java </p>
<p> This file provides functions for Java. It is assumed that FindJava.cmake has already been loaded. See FindJava.cmake for information on how to load Java into your CMake project. </p>
<pre>add_jar(target_name
 [SOURCES] source1 [source2 ...] [resource1 ...]
 [INCLUDE_JARS jar1 [jar2 ...]]
 [ENTRY_POINT entry]
 [VERSION version]
 [OUTPUT_NAME name]
 [OUTPUT_DIR dir]
 )</pre>
<p>This command creates a &lt;target_name&gt;.jar. It compiles the given source files (source) and adds the given resource files (resource) to the jar file. Source files can be java files or listing files (prefixed by &#8216;@&#8217;). If only resource files are given then just a jar file is created. The list of include jars are added to the classpath when compiling the java sources and also to the dependencies of the target. INCLUDE_JARS also accepts other target names created by add_jar. For backwards compatibility, jar files listed as sources are ignored (as they have been since the first version of this module). </p>
<p> The default OUTPUT_DIR can also be changed by setting the variable CMAKE_JAVA_TARGET_OUTPUT_DIR. </p>
<p> Additional instructions: </p>
<pre>To add compile flags to the target you can set these flags with
the following variable:</pre>
<pre>set(CMAKE_JAVA_COMPILE_FLAGS -nowarn)</pre>
<pre>To add a path or a jar file to the class path you can do this
with the CMAKE_JAVA_INCLUDE_PATH variable.</pre>
<pre>set(CMAKE_JAVA_INCLUDE_PATH /usr/share/java/shibboleet.jar)</pre>
<pre>To use a different output name for the target you can set it with:</pre>
<pre>add_jar(foobar foobar.java OUTPUT_NAME shibboleet.jar)</pre>
<pre>To use a different output directory than CMAKE_CURRENT_BINARY_DIR
you can set it with:</pre>
<pre>add_jar(foobar foobar.java OUTPUT_DIR ${PROJECT_BINARY_DIR}/bin)</pre>
<pre>To define an entry point in your jar you can set it with the ENTRY_POINT
named argument:</pre>
<pre>add_jar(example ENTRY_POINT com/examples/MyProject/Main)</pre>
<pre>To define a custom manifest for the jar, you can set it with the manifest
named argument:</pre>
<pre>add_jar(example MANIFEST /path/to/manifest)</pre>
<pre>To add a VERSION to the target output name you can set it using
the VERSION named argument to add_jar. This will create a jar file with the
name shibboleet-1.0.0.jar and will create a symlink shibboleet.jar
pointing to the jar with the version information.</pre>
<pre>add_jar(shibboleet shibbotleet.java VERSION 1.2.0)</pre>
<pre>If the target is a JNI library, utilize the following commands to
create a JNI symbolic link:</pre>
<pre>set(CMAKE_JNI_TARGET TRUE)
add_jar(shibboleet shibbotleet.java VERSION 1.2.0)
install_jar(shibboleet ${LIB_INSTALL_DIR}/shibboleet)
install_jni_symlink(shibboleet ${JAVA_LIB_INSTALL_DIR})</pre>
<pre>If a single target needs to produce more than one jar from its
java source code, to prevent the accumulation of duplicate class
files in subsequent jars, set/reset CMAKE_JAR_CLASSES_PREFIX prior
to calling the add_jar() function:</pre>
<pre>set(CMAKE_JAR_CLASSES_PREFIX com/redhat/foo)
add_jar(foo foo.java)</pre>
<pre>set(CMAKE_JAR_CLASSES_PREFIX com/redhat/bar)
add_jar(bar bar.java)</pre>
<p>Target Properties: </p>
<pre>The add_jar() function sets some target properties. You can get these
properties with the
 get_property(TARGET &lt;target_name&gt; PROPERTY &lt;propery_name&gt;)
command.</pre>
<pre>INSTALL_FILES The files which should be installed. This is used by
 install_jar().
JNI_SYMLINK The JNI symlink which should be installed.
 This is used by install_jni_symlink().
JAR_FILE The location of the jar file so that you can include
 it.
CLASSDIR The directory where the class files can be found. For
 example to use them with javah.</pre>
<pre>find_jar(&lt;VAR&gt;
 name | NAMES name1 [name2 ...]
 [PATHS path1 [path2 ... ENV var]]
 [VERSIONS version1 [version2]]
 [DOC &quot;cache documentation string&quot;]
 )</pre>
<p>This command is used to find a full path to the named jar. A cache entry named by &lt;VAR&gt; is created to stor the result of this command. If the full path to a jar is found the result is stored in the variable and the search will not repeated unless the variable is cleared. If nothing is found, the result will be &lt;VAR&gt;-NOTFOUND, and the search will be attempted again next time find_jar is invoked with the same variable. The name of the full path to a file that is searched for is specified by the names listed after NAMES argument. Additional search locations can be specified after the PATHS argument. If you require special a version of a jar file you can specify it with the VERSIONS argument. The argument after DOC will be used for the documentation string in the cache. </p>
<pre>install_jar(target_name destination)
install_jar(target_name DESTINATION destination [COMPONENT component])</pre>
<p>This command installs the TARGET_NAME files to the given DESTINATION. It should be called in the same scope as add_jar() or it will fail. </p>
<pre>install_jni_symlink(target_name destination)
install_jni_symlink(target_name DESTINATION destination [COMPONENT component])</pre>
<p>This command installs the TARGET_NAME JNI symlinks to the given DESTINATION. It should be called in the same scope as add_jar() or it will fail. </p>
<pre>create_javadoc(&lt;VAR&gt;
 PACKAGES pkg1 [pkg2 ...]
 [SOURCEPATH &lt;sourcepath&gt;]
 [CLASSPATH &lt;classpath&gt;]
 [INSTALLPATH &lt;install path&gt;]
 [DOCTITLE &quot;the documentation title&quot;]
 [WINDOWTITLE &quot;the title of the document&quot;]
 [AUTHOR TRUE|FALSE]
 [USE TRUE|FALSE]
 [VERSION TRUE|FALSE]
 )</pre>
<p>Create java documentation based on files or packages. For more details please read the javadoc manpage. </p>
<p> There are two main signatures for create_javadoc. The first signature works with package names on a path with source files: </p>
<pre>Example:
create_javadoc(my_example_doc
 PACKAGES com.exmaple.foo com.example.bar
 SOURCEPATH &quot;${CMAKE_CURRENT_SOURCE_DIR}&quot;
 CLASSPATH ${CMAKE_JAVA_INCLUDE_PATH}
 WINDOWTITLE &quot;My example&quot;
 DOCTITLE &quot;&lt;h1&gt;My example&lt;/h1&gt;&quot;
 AUTHOR TRUE
 USE TRUE
 VERSION TRUE
)</pre>
<p>The second signature for create_javadoc works on a given list of files. </p>
<pre>create_javadoc(&lt;VAR&gt;
 FILES file1 [file2 ...]
 [CLASSPATH &lt;classpath&gt;]
 [INSTALLPATH &lt;install path&gt;]
 [DOCTITLE &quot;the documentation title&quot;]
 [WINDOWTITLE &quot;the title of the document&quot;]
 [AUTHOR TRUE|FALSE]
 [USE TRUE|FALSE]
 [VERSION TRUE|FALSE]
 )</pre>
<p>Example: </p>
<pre>create_javadoc(my_example_doc
 FILES ${example_SRCS}
 CLASSPATH ${CMAKE_JAVA_INCLUDE_PATH}
 WINDOWTITLE &quot;My example&quot;
 DOCTITLE &quot;&lt;h1&gt;My example&lt;/h1&gt;&quot;
 AUTHOR TRUE
 USE TRUE
 VERSION TRUE
)</pre>
<p>Both signatures share most of the options. These options are the same as what you can find in the javadoc manpage. Please look at the manpage for CLASSPATH, DOCTITLE, WINDOWTITLE, AUTHOR, USE and VERSION. </p>
<p> The documentation will be by default installed to </p>
<pre>${CMAKE_INSTALL_PREFIX}/share/javadoc/&lt;VAR&gt;</pre>
<p>if you don&#8217;t set the INSTALLPATH. </p>
<pre>create_javah(TARGET &lt;target&gt;
 GENERATED_FILES &lt;VAR&gt;
 CLASSES &lt;class&gt;...
 [CLASSPATH &lt;classpath&gt;...]
 [DEPENDS &lt;depend&gt;...]
 [OUTPUT_NAME &lt;path&gt;|OUTPUT_DIR &lt;path&gt;]
 )</pre>
<p>Create C header files from java classes. These files provide the connective glue that allow your Java and C code to interact. </p>
<p> There are two main signatures for create_javah. The first signature returns generated files through variable specified by GENERATED_FILES option: </p>
<pre>Example:
Create_javah(GENERATED_FILES files_headers
 CLASSES org.cmake.HelloWorld
 CLASSPATH hello.jar
)</pre>
<p>The second signature for create_javah creates a target which encapsulates header files generation. </p>
<pre>Example:
Create_javah(TARGET target_headers
 CLASSES org.cmake.HelloWorld
 CLASSPATH hello.jar
)</pre>
<p>Both signatures share same options.</p>
<dl>
<dt><code>CLASSES &lt;class&gt;&#8230;</code></p>
<dd>Specifies Java classes used to generate headers.</p>
<dt><code>CLASSPATH &lt;classpath&gt;&#8230;</code></p>
<dd>Specifies various paths to look up classes. Here .class files, jar files or targets created by command add_jar can be used.</p>
<dt><code>DEPENDS &lt;depend&gt;&#8230;</code></p>
<dd>Targets on which the javah target depends</p>
<dt><code>OUTPUT_NAME &lt;path&gt;</code></p>
<dd>Concatenates the resulting header files for all the classes listed by option CLASSES into &lt;path&gt;. Same behavior as option &#8216;-o&#8217; of javah tool.</p>
<dt><code>OUTPUT_DIR &lt;path&gt;</code></p>
<dd>Sets the directory where the header files will be generated. Same behavior as option &#8216;-d&#8217; of javah tool. If not specified, ${CMAKE_CURRENT_BINARY_DIR} is used as output directory.</dl>
<h3>UseJavaSymlinks</h3>
<p>Helper script for UseJava.cmake</p>
<h3>UsePkgConfig</h3>
<p>Obsolete pkg-config module for CMake, use FindPkgConfig instead. </p>
<p> This module defines the following macro: </p>
<p> PKGCONFIG(package includedir libdir linkflags cflags) </p>
<p> Calling PKGCONFIG will fill the desired information into the 4 given arguments, e.g. PKGCONFIG(libart-2.0 LIBART_INCLUDE_DIR LIBART_LINK_DIR LIBART_LINK_FLAGS LIBART_CFLAGS) if pkg-config was NOT found or the specified software package doesn&#8217;t exist, the variable will be empty when the function returns, otherwise they will contain the respective information</p>
<h3>UseSWIG</h3>
<p>Defines the following macros for use with SWIG: </p>
<pre>SWIG_ADD_MODULE(name language [ files ])
 - Define swig module with given name and specified language
SWIG_LINK_LIBRARIES(name [ libraries ])
 - Link libraries to swig module</pre>
<p>Source files properties on module files can be set before the invocation of the SWIG_ADD_MODULE macro to specify special behavior of SWIG. </p>
<p> The source file property CPLUSPLUS calls SWIG in c++ mode, e.g.: </p>
<pre>set_property(SOURCE mymod.i PROPERTY CPLUSPLUS ON)
swig_add_module(mymod python mymod.i)</pre>
<p>The source file property SWIG_FLAGS adds custom flags to the SWIG executable. </p>
<p> The source-file property SWIG_MODULE_NAME have to be provided to specify the actual import name of the module in the target language if it cannot be scanned automatically from source or different from the module file basename.: </p>
<pre>set_property(SOURCE mymod.i PROPERTY SWIG_MODULE_NAME mymod_realname)</pre>
<p>To get the name of the swig module target library, use: ${SWIG_MODULE_${name}_REAL_NAME}. </p>
<p> Also some variables can be set to specify special behavior of SWIG. </p>
<p> CMAKE_SWIG_FLAGS can be used to add special flags to all swig calls. </p>
<p> Another special variable is CMAKE_SWIG_OUTDIR, it allows one to specify where to write all the swig generated module (swig -outdir option) </p>
<p> The name-specific variable SWIG_MODULE_&lt;name&gt;_EXTRA_DEPS may be used to specify extra dependencies for the generated modules. </p>
<p> If the source file generated by swig need some special flag you can use: </p>
<pre>set_source_files_properties( ${swig_generated_file_fullname}
 PROPERTIES COMPILE_FLAGS &quot;-bla&quot;)</pre>
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
<h3>Use_wxWindows</h3>
<p>This convenience include finds if wxWindows is installed and set the appropriate libs, incdirs, flags etc. author Jan Woetzel &lt;jw -at- mip.informatik.uni-kiel.de&gt; (07/2003) </p>
<p> USAGE: </p>
<pre>just include Use_wxWindows.cmake
in your projects CMakeLists.txt</pre>
<p>include( ${CMAKE_MODULE_PATH}/Use_wxWindows.cmake) </p>
<pre>if you are sure you need GL then</pre>
<p>set(WXWINDOWS_USE_GL 1) </p>
<pre>*before* you include this file.</pre>
<h3>WriteBasicConfigVersionFile</h3>
<pre>WRITE_BASIC_CONFIG_VERSION_FILE( filename
 [VERSION major.minor.patch]
 COMPATIBILITY (AnyNewerVersion|SameMajorVersion)
 )</pre>
<p>Deprecated, see WRITE_BASIC_PACKAGE_VERSION_FILE(), it is identical.</p>
<h3>WriteCompilerDetectionHeader</h3>
<p>This module provides the function write_compiler_detection_header(). </p>
<p> The <code>WRITE_COMPILER_DETECTION_HEADER</code> function can be used to generate a file suitable for preprocessor inclusion which contains macros to be used in source code: </p>
<pre>write_compiler_detection_header(
 FILE &lt;file&gt;
 PREFIX &lt;prefix&gt;
 [OUTPUT_FILES_VAR &lt;output_files_var&gt; OUTPUT_DIR &lt;output_dir&gt;]
 COMPILERS &lt;compiler&gt; [...]
 FEATURES &lt;feature&gt; [...]
 [VERSION &lt;version&gt;]
 [PROLOG &lt;prolog&gt;]
 [EPILOG &lt;epilog&gt;]
)</pre>
<p>The <code>write_compiler_detection_header</code> function generates the file <code>&lt;file&gt;</code> with macros which all have the prefix <code>&lt;prefix&gt;</code>. </p>
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
<p><code>VERSION</code> may be used to specify the API version to be generated. Future versions of CMake may introduce alternative APIs. A given API is selected by any <code>&lt;version&gt;</code> value greater than or equal to the version of CMake that introduced the given API and less than the version of CMake that introduced its succeeding API. The value of the <code>CMAKE_MINIMUM_REQUIRED_VERSION</code> variable is used if no explicit version is specified. (As of CMake version 3.6.3 there is only one API version.) </p>
<p> <code>PROLOG</code> may be specified as text content to write at the start of the header. <code>EPILOG</code> may be specified as text content to write at the end of the header </p>
<p> At least one <code>&lt;compiler&gt;</code> and one <code>&lt;feature&gt;</code> must be listed. Compilers which are known to CMake, but not specified are detected and a preprocessor <code>#error</code> is generated for them. A preprocessor macro matching <code>&lt;PREFIX&gt;_COMPILER_IS_&lt;compiler&gt;</code> is generated for each compiler known to CMake to contain the value <code>0</code> or <code>1</code>. </p>
<p> Possible compiler identifiers are documented with the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable. Available features in this version of CMake are listed in the <code>CMAKE_C_KNOWN_FEATURES</code> and <code>CMAKE_CXX_KNOWN_FEATURES</code> global properties. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features.</p>
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
<p> The following features generate corresponding symbol defines: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Feature </td>
<td> Define </td>
<td> Symbol
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>c_restrict</code> </td>
<td> <code>&lt;PREFIX&gt;_RESTRICT</code> </td>
<td> <code>restrict</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_constexpr</code> </td>
<td> <code>&lt;PREFIX&gt;_CONSTEXPR</code> </td>
<td> <code>constexpr</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_deleted_functions</code> </td>
<td> <code>&lt;PREFIX&gt;_DELETED_FUNCTION</code> </td>
<td> <code>= delete</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_extern_templates</code> </td>
<td> <code>&lt;PREFIX&gt;_EXTERN_TEMPLATE</code> </td>
<td> <code>extern</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_final</code> </td>
<td> <code>&lt;PREFIX&gt;_FINAL</code> </td>
<td> <code>final</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_noexcept</code> </td>
<td> <code>&lt;PREFIX&gt;_NOEXCEPT</code> </td>
<td> <code>noexcept</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_noexcept</code> </td>
<td> <code>&lt;PREFIX&gt;_NOEXCEPT_EXPR(X)</code> </td>
<td> <code>noexcept(X)</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_override</code> </td>
<td> <code>&lt;PREFIX&gt;_OVERRIDE</code> </td>
<td> <code>override</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
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
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Feature </td>
<td> Define </td>
<td> Symbol
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_alignas</code> </td>
<td> <code>&lt;PREFIX&gt;_ALIGNAS</code> </td>
<td> <code>alignas</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_alignof</code> </td>
<td> <code>&lt;PREFIX&gt;_ALIGNOF</code> </td>
<td> <code>alignof</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_nullptr</code> </td>
<td> <code>&lt;PREFIX&gt;_NULLPTR</code> </td>
<td> <code>nullptr</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_static_assert</code> </td>
<td> <code>&lt;PREFIX&gt;_STATIC_ASSERT</code> </td>
<td> <code>static_assert</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_static_assert</code> </td>
<td> <code>&lt;PREFIX&gt;_STATIC_ASSERT_MSG</code> </td>
<td> <code>static_assert</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_attribute_deprecated</code> </td>
<td> <code>&lt;PREFIX&gt;_DEPRECATED</code> </td>
<td> <code>[[deprecated]]</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_attribute_deprecated</code> </td>
<td> <code>&lt;PREFIX&gt;_DEPRECATED_MSG</code> </td>
<td> <code>[[deprecated]]</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>cxx_thread_local</code> </td>
<td> <code>&lt;PREFIX&gt;_THREAD_LOCAL</code> </td>
<td> <code>thread_local</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
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
<h2>Copyright</h2>
<p>2000-2016 Kitware, Inc.</p>
