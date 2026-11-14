---
title: "cmakecompat(1)"
name: "cmakecompat"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cmakecompat/"
description: "cmakecompat – Reference of CMake compatibility commands."
---

<h2>NAME</h2>
<p> cmakecompat &#8211; Reference of CMake compatibility commands. </p>
<h2>COMPATIBILITY COMMANDS</h2>
<pre>
  CMake Compatibility Listfile Commands - Obsolete commands supported by CMake for compatibility.
</pre>
<p> This is the documentation for now obsolete listfile commands from previous CMake versions, which are still supported for compatibility reasons. You should instead use the newer, faster and shinier new commands. ;-) </p>
<dl>
<dt><code>build_name</code></p>
<dd> Deprecated. Use ${CMAKE_SYSTEM} and ${CMAKE_CXX_COMPILER} instead. </p>
<pre>
  build_name(variable)
</pre>
<p> Sets the specified variable to a string representing the platform and compiler settings. These values are now available through the CMAKE_SYSTEM and CMAKE_CXX_COMPILER variables. </p>
<dt><code>exec_program</code></p>
<dd> Deprecated. Use the execute_process() command instead. </p>
<p> Run an executable program during the processing of the CMakeList.txt file. </p>
<pre><code>
exec_program(Executable[directory in which to run]
                       [ARGS&lt;arguments to executable&gt;]
                       [OUTPUT_VARIABLE&lt;var&gt;]
                       [RETURN_VALUE&lt;var&gt;])
</code></pre>
<p> The executable is run in the optionally specified directory. The executable can include arguments if it is double quoted, but it is better to use the optional ARGS argument to specify arguments to the program. This is because cmake will then be able to escape spaces in the executable path. An optional argument OUTPUT_VARIABLE specifies a variable in which to store the output. To capture the return value of the execution, provide a RETURN_VALUE. If OUTPUT_VARIABLE is specified, then no output will go to the stdout/stderr of the console running cmake. </p>
<dt><code>export_library_dependencies</code></p>
<dd> Deprecated. Use INSTALL(EXPORT) or EXPORT command. </p>
<p> This command generates an old-style library dependencies file. Projects requiring CMake 2.6 or later should not use the command. Use instead the install(EXPORT) command to help export targets from an installation tree and the export() command to export targets from a build tree. </p>
<p> The old-style library dependencies file does not take into account per-configuration names of libraries or the LINK_INTERFACE_LIBRARIES target property. </p>
<pre>
  export_library_dependencies(&lt;file&gt; [APPEND])
</pre>
<p> Create a file named &lt;file&gt; that can be included into a CMake listfile with the INCLUDE command. The file will contain a number of SET commands that will set all the variables needed for library dependency information. This should be the last command in the top level CMakeLists.txt file of the project. If the APPEND option is specified, the SET commands will be appended to the given file instead of replacing it. </p>
<dt><code>install_files</code></p>
<dd> Deprecated. Use the install(FILES ) command instead. </p>
<p> This command has been superceded by the install command. It is provided for compatibility with older CMake code. The FILES form is directly replaced by the FILES form of the install command. The regexp form can be expressed more clearly using the GLOB form of the file command. </p>
<pre>
  install_files(&lt;dir&gt; extension file file ...)
</pre>
<p> Create rules to install the listed files with the given extension into the given directory. Only files existing in the current source tree or its corresponding location in the binary tree may be listed. If a file specified already has an extension, that extension will be removed first. This is useful for providing lists of source files such as foo.cxx when you want the corresponding foo.h to be installed. A typical extension is &#8216;.h&#8217;. </p>
<pre>
  install_files(&lt;dir&gt; regexp)
</pre>
<p> Any files in the current source directory that match the regular expression will be installed. </p>
<pre>
  install_files(&lt;dir&gt; FILES file file ...)
</pre>
<p> Any files listed after the FILES keyword will be installed explicitly from the names given. Full paths are allowed in this form. </p>
<p> The directory &lt;dir&gt; is relative to the installation prefix, which is stored in the variable CMAKE_INSTALL_PREFIX. </p>
<dt><code>install_programs</code></p>
<dd> Deprecated. Use the install(PROGRAMS ) command instead. </p>
<p> This command has been superceded by the install command. It is provided for compatibility with older CMake code. The FILES form is directly replaced by the PROGRAMS form of the INSTALL command. The regexp form can be expressed more clearly using the GLOB form of the FILE command. </p>
<p>install_programs(&lt;dir&gt; file1 file2[file3&#8230;])<br />
    install_programs(&lt;dir&gt; FILES file1[file2&#8230;])</p>
<p> Create rules to install the listed programs into the given directory. Use the FILES argument to guarantee that the file list version of the command will be used even when there is only one argument. </p>
<pre>
  install_programs(&lt;dir&gt; regexp)
</pre>
<p> In the second form any program in the current source directory that matches the regular expression will be installed. </p>
<p> This command is intended to install programs that are not built by cmake, such as shell scripts. See the TARGETS form of the INSTALL command to create installation rules for targets built by cmake. </p>
<p> The directory &lt;dir&gt; is relative to the installation prefix, which is stored in the variable CMAKE_INSTALL_PREFIX. </p>
<dt><code>install_targets</code></p>
<dd> Deprecated. Use the install(TARGETS ) command instead. </p>
<p> This command has been superceded by the install command. It is provided for compatibility with older CMake code. </p>
<pre>
  install_targets(&lt;dir&gt; [RUNTIME_DIRECTORY dir] target target)
</pre>
<p> Create rules to install the listed targets into the given directory. The directory &lt;dir&gt; is relative to the installation prefix, which is stored in the variable CMAKE_INSTALL_PREFIX. If RUNTIME_DIRECTORY is specified, then on systems with special runtime files (Windows DLL), the files will be copied to that directory. </p>
<dt><code>link_libraries</code></p>
<dd> Deprecated. Use the target_link_libraries() command instead. </p>
<p> Link libraries to all targets added later. </p>
<pre>
  link_libraries(library1 &lt;debug | optimized&gt; library2 ...)
</pre>
<p> Specify a list of libraries to be linked into any following targets (typically added with the add_executable or add_library calls). This command is passed down to all subdirectories. The debug and optimized strings may be used to indicate that the next library listed is to be used only for that specific type of build. </p>
<dt><code>make_directory</code></p>
<dd> Deprecated. Use the file(MAKE_DIRECTORY ) command instead. </p>
<pre>
  make_directory(directory)
</pre>
<p> Creates the specified directory. Full paths should be given. Any parent directories that do not exist will also be created. Use with care. </p>
<dt><code>output_required_files</code></p>
<dd> Deprecated. Approximate C preprocessor dependency scanning. </p>
<p> This command exists only because ancient CMake versions provided it. CMake handles preprocessor dependency scanning automatically using a more advanced scanner. </p>
<pre>
  output_required_files(srcfile outputfile)
</pre>
<p> Outputs a list of all the source files that are required by the specified srcfile. This list is written into outputfile. This is similar to writing out the dependencies for srcfile except that it jumps from .h files into .cxx, .c and .cpp files if possible. </p>
<dt><code>remove</code></p>
<dd> Deprecated. Use the list(REMOVE_ITEM ) command instead. </p>
<pre>
  remove(VAR VALUE VALUE ...)
</pre>
<p> Removes VALUE from the variable VAR. This is typically used to remove entries from a vector (e.g. semicolon separated list). VALUE is expanded. </p>
<dt><code>subdir_depends</code></p>
<dd> Deprecated. Does nothing. </p>
<pre>
  subdir_depends(subdir dep1 dep2 ...)
</pre>
<p> Does not do anything. This command used to help projects order parallel builds correctly. This functionality is now automatic. </p>
<dt><code>subdirs</code></p>
<dd> Deprecated. Use the add_subdirectory() command instead. </p>
<p> Add a list of subdirectories to the build. </p>
<pre><code>
subdirs(dir1 dir2...[EXCLUDE_FROM_ALL exclude_dir1 exclude_dir2...]
                    [PREORDER])
</code></pre>
<p> Add a list of subdirectories to the build. The add_subdirectory command should be used instead of subdirs although subdirs will still work. This will cause any CMakeLists.txt files in the sub directories to be processed by CMake. Any directories after the PREORDER flag are traversed first by makefile builds, the PREORDER flag has no effect on IDE projects. Any directories after the EXCLUDE_FROM_ALL marker will not be included in the top level makefile or project file. This is useful for having CMake create makefiles or projects for a set of examples in a project. You would want CMake to generate makefiles or project files for all the examples at the same time, but you would not want them to show up in the top level project or be built each time make is run from the top. </p>
<dt><code>use_mangled_mesa</code></p>
<dd> Copy mesa headers for use in combination with system GL. </p>
<pre>
  use_mangled_mesa(PATH_TO_MESA OUTPUT_DIRECTORY)
</pre>
<p> The path to mesa includes, should contain gl_mangle.h. The mesa headers are copied to the specified output directory. This allows mangled mesa headers to override other GL headers by being added to the include directory path earlier. </p>
<dt><code>utility_source</code></p>
<dd> Specify the source tree of a third-party utility. </p>
<pre>
  utility_source(cache_entry executable_name
                 path_to_source [file1 file2 ...])
</pre>
<p> When a third-party utility&#8217;s source is included in the distribution, this command specifies its location and name. The cache entry will not be set unless the path_to_source and all listed files exist. It is assumed that the source tree of the utility will have been built before it is needed. </p>
<p> When cross compiling CMake will print a warning if a utility_source() command is executed, because in many cases it is used to build an executable which is executed later on. This doesn&#8217;t work when cross compiling, since the executable can run only on their target platform. So in this case the cache entry has to be adjusted manually so it points to an executable which is runnable on the build host. </p>
<dt><code>variable_requires</code></p>
<dd> Deprecated. Use the if() command instead. </p>
<p> Assert satisfaction of an option&#8217;s required variables. </p>
<pre>
  variable_requires(TEST_VARIABLE RESULT_VARIABLE
                    REQUIRED_VARIABLE1
                    REQUIRED_VARIABLE2 ...)
</pre>
<p> The first argument (TEST_VARIABLE) is the name of the variable to be tested, if that variable is false nothing else is done. If TEST_VARIABLE is true, then the next argument (RESULT_VARIABLE) is a variable that is set to true if all the required variables are set. The rest of the arguments are variables that must be true or not set to NOTFOUND to avoid an error. If any are not true, an error is reported. </p>
<dt><code>write_file</code></p>
<dd> Deprecated. Use the file(WRITE ) command instead. </p>
<pre>
  write_file(filename &quot;message to write&quot;... [APPEND])
</pre>
<p> The first argument is the file name, the rest of the arguments are messages to write. If the argument APPEND is specified, then the message will be appended. </p>
<p> NOTE 1: file(WRITE &#8230; and file(APPEND &#8230; do exactly the same as this one but add some more functionality. </p>
<p> NOTE 2: When using write_file the produced file cannot be used as an input to CMake (CONFIGURE_FILE, source file &#8230;) because it will lead to an infinite loop. Use configure_file if you want to generate input files to CMake. </p>
</dl>
<h2>COPYRIGHT</h2>
<p> Copyright 2000-2012 Kitware, Inc., Insight Software Consortium. All rights reserved. </p>
<p> Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: </p>
<p> Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. </p>
<p> Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. </p>
<p> Neither the names of Kitware, Inc., the Insight Software Consortium, nor the names of their contributors may be used to endorse or promote products derived from this software without specific prior written permission. </p>
<p> THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS &quot;AS IS&quot; AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. </p>
<h2>SEE ALSO</h2>
<p> The following resources are available to get help using CMake: </p>
<dl>
<dt><code>Home Page</code></p>
<dd> <a rel="nofollow" href="http://www.cmake.org">http://www.cmake.org</a> </p>
<p> The primary starting point for learning about CMake. </p>
<dt><code>Frequently Asked Questions</code></p>
<dd> <a rel="nofollow" href="http://www.cmake.org/Wiki/CMake_FAQ">http://www.cmake.org/Wiki/CMake_FAQ</a> </p>
<p> A Wiki is provided containing answers to frequently asked questions. </p>
<dt><code>Online Documentation</code></p>
<dd> <a rel="nofollow" href="http://www.cmake.org/HTML/Documentation.html">http://www.cmake.org/HTML/Documentation.html</a> </p>
<p> Links to available documentation may be found on this web page. </p>
<dt><code>Mailing List</code></p>
<dd> <a rel="nofollow" href="http://www.cmake.org/HTML/MailingLists.html">http://www.cmake.org/HTML/MailingLists.html</a> </p>
<p> For help and discussion about using cmake, a mailing list is provided at cmake [at] cmake.org. The list is member-post-only but one may sign up on the CMake web page. Please first read the full documentation at <a rel="nofollow" href="http://www.cmake.org">http://www.cmake.org</a> before posting questions to the list. </p>
</dl>
<h2>Index</h2>
