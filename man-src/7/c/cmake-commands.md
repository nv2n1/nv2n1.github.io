---
title: "cmake-commands(7)"
name: "cmake-commands"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake-commands/"
description: "cmake-commands – CMake Language Command Reference"
---
<p>cmake-commands &#8211; CMake Language Command Reference </p>
<h2>SCRIPTING COMMANDS</h2>
<p>These commands are always available.  </p>
<h3>break</h3>
<p>Break from an enclosing foreach or while loop. </p>
<pre><code>break()
</code></pre>
<p>Breaks from an enclosing <code>foreach()</code> or <code>while()</code> loop. </p>
<p>See also the <code>continue()</code> command.  </p>
<h3>cmake_host_system_information</h3>
<p>Query host system specific information. </p>
<pre><code>cmake_host_system_information(RESULT &lt;variable&gt; QUERY &lt;key&gt; ...)
</code></pre>
<p>Queries system information of the host system on which cmake runs. One or more <code>&lt;key&gt;</code> can be provided to select the information to be queried. The list of queried values is stored in <code>&lt;variable&gt;</code>. </p>
<p> <code>&lt;key&gt;</code> can be one of the following values: </p>
<dl>
<dt><code>NUMBER_OF_LOGICAL_CORES</code></dt>
<dd> <p> Number of logical cores </p>
 </dd>
<dt><code>NUMBER_OF_PHYSICAL_CORES</code></dt>
<dd> <p> Number of physical cores </p>
 </dd>
<dt><code>HOSTNAME</code></dt>
<dd> <p> Hostname </p>
 </dd>
<dt><code>FQDN</code></dt>
<dd> <p> Fully qualified domain name </p>
 </dd>
<dt><code>TOTAL_VIRTUAL_MEMORY</code></dt>
<dd> <p> Total virtual memory in MiB [1] </p>
 </dd>
<dt><code>AVAILABLE_VIRTUAL_MEMORY</code></dt>
<dd> <p> Available virtual memory in MiB [1] </p>
 </dd>
<dt><code>TOTAL_PHYSICAL_MEMORY</code></dt>
<dd> <p> Total physical memory in MiB [1] </p>
 </dd>
<dt><code>AVAILABLE_PHYSICAL_MEMORY</code></dt>
<dd> <p> Available physical memory in MiB [1] </p>
 </dd>
<dt><code>IS_64BIT</code></dt>
<dd> <p> New in version 3.10. </p>
<p>One if processor is 64Bit </p>
 </dd>
<dt><code>HAS_FPU</code></dt>
<dd> <p> New in version 3.10. </p>
<p>One if processor has floating point unit </p>
 </dd>
<dt><code>HAS_MMX</code></dt>
<dd> <p> New in version 3.10. </p>
<p>One if processor supports MMX instructions </p>
 </dd>
<dt><code>HAS_MMX_PLUS</code></dt>
<dd> <p> New in version 3.10. </p>
<p>One if processor supports Ext. MMX instructions </p>
 </dd>
<dt><code>HAS_SSE</code></dt>
<dd> <p> New in version 3.10. </p>
<p>One if processor supports SSE instructions </p>
 </dd>
<dt><code>HAS_SSE2</code></dt>
<dd> <p> New in version 3.10. </p>
<p>One if processor supports SSE2 instructions </p>
 </dd>
<dt><code>HAS_SSE_FP</code></dt>
<dd> <p> New in version 3.10. </p>
<p>One if processor supports SSE FP instructions </p>
 </dd>
<dt><code>HAS_SSE_MMX</code></dt>
<dd> <p> New in version 3.10. </p>
<p>One if processor supports SSE MMX instructions </p>
 </dd>
<dt><code>HAS_AMD_3DNOW</code></dt>
<dd> <p> New in version 3.10. </p>
<p>One if processor supports 3DNow instructions </p>
 </dd>
<dt><code>HAS_AMD_3DNOW_PLUS</code></dt>
<dd> <p> New in version 3.10. </p>
<p>One if processor supports 3DNow+ instructions </p>
 </dd>
<dt><code>HAS_IA64</code></dt>
<dd> <p> New in version 3.10. </p>
<p>One if IA64 processor emulating x86 </p>
 </dd>
<dt><code>HAS_SERIAL_NUMBER</code></dt>
<dd> <p> New in version 3.10. </p>
<p>One if processor has serial number </p>
 </dd>
<dt><code>PROCESSOR_SERIAL_NUMBER</code></dt>
<dd> <p> New in version 3.10. </p>
<p>Processor serial number </p>
 </dd>
<dt><code>PROCESSOR_NAME</code></dt>
<dd> <p> New in version 3.10. </p>
<p>Human readable processor name </p>
 </dd>
<dt><code>PROCESSOR_DESCRIPTION</code></dt>
<dd> <p> New in version 3.10. </p>
<p>Human readable full processor description </p>
 </dd>
<dt><code>OS_NAME</code></dt>
<dd> <p> New in version 3.10. </p>
<p>See <code>CMAKE_HOST_SYSTEM_NAME</code> </p>
 </dd>
<dt><code>OS_RELEASE</code></dt>
<dd> <p> New in version 3.10. </p>
<p>The OS sub-type e.g. on Windows <code>Professional</code> </p>
 </dd>
<dt><code>OS_VERSION</code></dt>
<dd> <p> New in version 3.10. </p>
<p>The OS build ID </p>
 </dd>
<dt><code>OS_PLATFORM</code></dt>
<dd> <p> New in version 3.10. </p>
<p>See <code>CMAKE_HOST_SYSTEM_PROCESSOR</code> </p>
 </dd>
<dt><code>DISTRIB_INFO</code></dt>
<dd> <p> New in version 3.22. </p>
<p>Read <code>/etc/os-release</code> file and define the given <code>&lt;variable&gt;</code> into a list of read variables </p>
 </dd>
<dt><code>DISTRIB_&lt;name&gt;</code></dt>
<dd> <p> New in version 3.22. </p>
<p>Get the <code>&lt;name&gt;</code> variable (see <i>man 5 os-release</i>) if it exists in the <code>/etc/os-release</code> file </p>
<p>Example: </p>
<pre><code>cmake_host_system_information(RESULT PRETTY_NAME QUERY DISTRIB_PRETTY_NAME)
message(STATUS &quot;${PRETTY_NAME}&quot;)
cmake_host_system_information(RESULT DISTRO QUERY DISTRIB_INFO)
foreach(VAR IN LISTS DISTRO)
  message(STATUS &quot;${VAR}=`${${VAR}}`&quot;)
endforeach()
</code></pre>
<p>Output: </p>
<pre><code>-- Ubuntu 20.04.2 LTS
-- DISTRO_BUG_REPORT_URL=`https://bugs.launchpad.net/ubuntu/`-- DISTRO_HOME_URL=`https://www.ubuntu.com/`-- DISTRO_ID=`ubuntu`
-- DISTRO_ID_LIKE=`debian`
-- DISTRO_NAME=`Ubuntu`
-- DISTRO_PRETTY_NAME=`Ubuntu 20.04.2 LTS`
-- DISTRO_PRIVACY_POLICY_URL=`https://www.ubuntu.com/legal/terms-and-policies/privacy-policy`-- DISTRO_SUPPORT_URL=`https://help.ubuntu.com/`-- DISTRO_UBUNTU_CODENAME=`focal`
-- DISTRO_VERSION=`20.04.2 LTS (Focal Fossa)`
-- DISTRO_VERSION_CODENAME=`focal`
-- DISTRO_VERSION_ID=`20.04`
</code></pre>
<p>If <code>/etc/os-release</code> file is not found, the command tries to gather OS identification via fallback scripts. The fallback script can use <i>various distribution-specific files</i> to collect OS identification data and map it into <i>man 5 os-release</i> variables. </p>
 </dd></dl>
<h3>Fallback Interface Variables</h3>
<dl>
<dt><code>CMAKE_GET_OS_RELEASE_FALLBACK_SCRIPTS</code></dt>
<dd> <p> In addition to the scripts shipped with CMake, a user may append full paths to his script(s) to the this list. The script filename has the following format: <code>NNN-&lt;name&gt;.cmake</code>, where <code>NNN</code> is three digits used to apply collected scripts in a specific order. </p>
 </dd>
<dt><code>CMAKE_GET_OS_RELEASE_FALLBACK_RESULT_&lt;varname&gt;</code></dt>
<dd> <p> Variables collected by the user provided fallback script ought to be assigned to CMake variables using this naming convention. Example, the <code>ID</code> variable from the manual becomes <code>CMAKE_GET_OS_RELEASE_FALLBACK_RESULT_ID</code>. </p>
 </dd>
<dt><code>CMAKE_GET_OS_RELEASE_FALLBACK_RESULT</code></dt>
<dd> <p> The fallback script ought to store names of all assigned <code>CMAKE_GET_OS_RELEASE_FALLBACK_RESULT_&lt;varname&gt;</code> variables in this list. </p>
<p>Example: </p>
<pre><code># Try to detect some old distribution
# See also
# -http://linuxmafia.com/faq/Admin/release-files.html#
if(NOT EXISTS &quot;${CMAKE_SYSROOT}/etc/foobar-release&quot;)
  return()
endif()
# Get the first string only
file(
    STRINGS &quot;${CMAKE_SYSROOT}/etc/foobar-release&quot; CMAKE_GET_OS_RELEASE_FALLBACK_CONTENT
    LIMIT_COUNT 1
  )
#
# Example:
#
# Foobar distribution release 1.2.3 (server)
#
if(CMAKE_GET_OS_RELEASE_FALLBACK_CONTENT MATCHES &quot;Foobar distribution release ([0-9\.]+) .*&quot;)
  set(CMAKE_GET_OS_RELEASE_FALLBACK_RESULT_NAME Foobar)
  set(CMAKE_GET_OS_RELEASE_FALLBACK_RESULT_PRETTY_NAME &quot;${CMAKE_GET_OS_RELEASE_FALLBACK_CONTENT}&quot;)
  set(CMAKE_GET_OS_RELEASE_FALLBACK_RESULT_ID foobar)
  set(CMAKE_GET_OS_RELEASE_FALLBACK_RESULT_VERSION ${CMAKE_MATCH_1})
  set(CMAKE_GET_OS_RELEASE_FALLBACK_RESULT_VERSION_ID ${CMAKE_MATCH_1})
  list(
      APPEND CMAKE_GET_OS_RELEASE_FALLBACK_RESULT
      CMAKE_GET_OS_RELEASE_FALLBACK_RESULT_NAME
      CMAKE_GET_OS_RELEASE_FALLBACK_RESULT_PRETTY_NAME
      CMAKE_GET_OS_RELEASE_FALLBACK_RESULT_ID
      CMAKE_GET_OS_RELEASE_FALLBACK_RESULT_VERSION
      CMAKE_GET_OS_RELEASE_FALLBACK_RESULT_VERSION_ID
    )
endif()
unset(CMAKE_GET_OS_RELEASE_FALLBACK_CONTENT)
</code></pre>
 </dd></dl>
<h2>FOOTNOTES</h2>
<dl>
<dt>[1]</dt>
<dd> <p> One MiB (mebibyte) is equal to 1024x1024 bytes. </p>
 </dd></dl>
<h3>cmake_language</h3>
<p>New in version 3.18. </p>
<p>Call meta-operations on CMake commands.  </p>
<h3>Synopsis</h3>
<pre><code>cmake_language( CALL  &lt;command&gt; [&lt;arg&gt;...])
cmake_language( EVAL  CODE &lt;code&gt;...)
cmake_language( DEFER  &lt;options&gt;... CALL &lt;command&gt; [&lt;arg&gt;...])
</code></pre>
<h3>Introduction</h3>
<p>This command will call meta-operations on built-in CMake commands or those created via the <code>macro()</code> or <code>function()</code> commands. </p>
<p> <code>cmake_language</code> does not introduce a new variable or policy scope.  </p>
<h3>Calling Commands</h3>
<pre><code>cmake_language(CALL &lt;command&gt; [&lt;arg&gt;...])
</code></pre>
<p>Calls the named <code>&lt;command&gt;</code> with the given arguments (if any). For example, the code: </p>
<pre><code>set(message_command &quot;message&quot;)
cmake_language(CALL ${message_command} STATUS &quot;Hello World!&quot;)
</code></pre>
<p>is equivalent to </p>
<pre><code>message(STATUS &quot;Hello World!&quot;)
</code></pre>
<p> <code>NOTE:</code> To ensure consistency of the code, the following commands are not allowed: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>if</code> / <code>elseif</code> / <code>else</code> / <code>endif</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>while</code> / <code>endwhile</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>foreach</code> / <code>endforeach</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>function</code> / <code>endfunction</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>macro</code> / <code>endmacro</code> </p>
 </dd></dl>
<h3>Evaluating Code</h3>
<pre><code>cmake_language(EVAL CODE &lt;code&gt;...)
</code></pre>
<p>Evaluates the <code>&lt;code&gt;...</code> as CMake code. </p>
<p>For example, the code: </p>
<pre><code>set(A TRUE)
set(B TRUE)
set(C TRUE)
set(condition &quot;(A AND B) OR C&quot;)
cmake_language(EVAL CODE &quot;
  if (${condition})
    message(STATUS TRUE)
  else()
    message(STATUS FALSE)
  endif()&quot;
)
</code></pre>
<p>is equivalent to </p>
<pre><code>set(A TRUE)
set(B TRUE)
set(C TRUE)
set(condition &quot;(A AND B) OR C&quot;)
file(WRITE ${CMAKE_CURRENT_BINARY_DIR}/eval.cmake &quot;
  if (${condition})
    message(STATUS TRUE)
  else()
    message(STATUS FALSE)
  endif()&quot;
)
include(${CMAKE_CURRENT_BINARY_DIR}/eval.cmake)
</code></pre>
<h3>Deferring Calls</h3>
<p>New in version 3.19. </p>
<pre><code>cmake_language(DEFER &lt;options&gt;... CALL &lt;command&gt; [&lt;arg&gt;...])
</code></pre>
<p>Schedules a call to the named <code>&lt;command&gt;</code> with the given arguments (if any) to occur at a later time. By default, deferred calls are executed as if written at the end of the current directory&#8217;s <code>CMakeLists.txt</code> file, except that they run even after a <code>return()</code> call. Variable references in arguments are evaluated at the time the deferred call is executed. </p>
<p>The options are: </p>
<dl>
<dt><code>DIRECTORY &lt;dir&gt;</code></dt>
<dd> <p> Schedule the call for the end of the given directory instead of the current directory. The <code>&lt;dir&gt;</code> may reference either a source directory or its corresponding binary directory. Relative paths are treated as relative to the current source directory. </p>
<p>The given directory must be known to CMake, being either the top-level directory or one added by <code>add_subdirectory()</code>. Furthermore, the given directory must not yet be finished processing. This means it can be the current directory or one of its ancestors. </p>
 </dd>
<dt><code>ID &lt;id&gt;</code></dt>
<dd> <p> Specify an identification for the deferred call. The <code>&lt;id&gt;</code> may not be empty and may not begin with a capital letter <code>A-Z</code>. The <code>&lt;id&gt;</code> may begin with an underscore (<code>_</code>) only if it was generated automatically by an earlier call that used <code>ID_VAR</code> to get the id. </p>
 </dd>
<dt><code>ID_VAR &lt;var&gt;</code></dt>
<dd> <p> Specify a variable in which to store the identification for the deferred call. If <code>ID &lt;id&gt;</code> is not given, a new identification will be generated and the generated id will start with an underscore (<code>_</code>). </p>
<p>The currently scheduled list of deferred calls may be retrieved: </p>
<pre><code>cmake_language(DEFER [DIRECTORY &lt;dir&gt;] GET_CALL_IDS &lt;var&gt;)
</code></pre>
<p>This will store in <code>&lt;var&gt;</code> a semicolon-separated list of deferred call ids. The ids are for the directory scope in which the calls have been deferred to (i.e. where they will be executed), which can be different to the scope in which they were created. The <code>DIRECTORY</code> option can be used to specify the scope for which to retrieve the call ids. If that option is not given, the call ids for the current directory scope will be returned. </p>
<p>Details of a specific call may be retrieved from its id: </p>
<pre><code>cmake_language(DEFER [DIRECTORY &lt;dir&gt;] GET_CALL &lt;id&gt; &lt;var&gt;)
</code></pre>
<p>This will store in <code>&lt;var&gt;</code> a semicolon-separated list in which the first element is the name of the command to be called, and the remaining elements are its unevaluated arguments (any contained <code>;</code> characters are included literally and cannot be distinguished from multiple arguments). If multiple calls are scheduled with the same id, this retrieves the first one. If no call is scheduled with the given id in the specified <code>DIRECTORY</code> scope (or the current directory scope if no <code>DIRECTORY</code> option is given), this stores an empty string in the variable. </p>
<p>Deferred calls may be canceled by their id: </p>
<pre><code>cmake_language(DEFER [DIRECTORY &lt;dir&gt;] CANCEL_CALL &lt;id&gt;...)
</code></pre>
<p>This cancels all deferred calls matching any of the given ids in the specified <code>DIRECTORY</code> scope (or the current directory scope if no <code>DIRECTORY</code> option is given). Unknown ids are silently ignored. </p>
 </dd></dl>
<h3>Deferred Call Examples</h3>
<p>For example, the code: </p>
<pre><code>cmake_language(DEFER CALL message &quot;${deferred_message}&quot;)
cmake_language(DEFER ID_VAR id CALL message &quot;Canceled Message&quot;)
cmake_language(DEFER CANCEL_CALL ${id})
message(&quot;Immediate Message&quot;)
set(deferred_message &quot;Deferred Message&quot;)
</code></pre>
<p>prints: </p>
<pre><code>Immediate Message
Deferred Message
</code></pre>
<p>The <code>Cancelled Message</code> is never printed because its command is canceled. The <code>deferred_message</code> variable reference is not evaluated until the call site, so it can be set after the deferred call is scheduled. </p>
<p>In order to evaluate variable references immediately when scheduling a deferred call, wrap it using <code>cmake_language(EVAL)</code>. However, note that arguments will be re-evaluated in the deferred call, though that can be avoided by using bracket arguments. For example: </p>
<pre><code>set(deferred_message &quot;Deferred Message 1&quot;)
set(re_evaluated [[${deferred_message}]])
cmake_language(EVAL CODE &quot;
  cmake_language(DEFER CALL message [[${deferred_message}]])
  cmake_language(DEFER CALL message \&quot;${re_evaluated}\&quot;)
&quot;)
message(&quot;Immediate Message&quot;)
set(deferred_message &quot;Deferred Message 2&quot;)
</code></pre>
<p>also prints: </p>
<pre><code>Immediate Message
Deferred Message 1
Deferred Message 2
</code></pre>
<h3>cmake_minimum_required</h3>
<p>Require a minimum version of cmake. </p>
<pre><code>cmake_minimum_required(VERSION &lt;min&gt;[...&lt;policy_max&gt;] [FATAL_ERROR])
</code></pre>
<p>New in version 3.12: The optional <code>&lt;policy_max&gt;</code> version. </p>
<p>Sets the minimum required version of cmake for a project. Also updates the policy settings as explained below. </p>
<p> <code>&lt;min&gt;</code> and the optional <code>&lt;policy_max&gt;</code> are each CMake versions of the form <code>major.minor[.patch[.tweak]]</code>, and the <code>...</code> is literal. </p>
<p>If the running version of CMake is lower than the <code>&lt;min&gt;</code> required version it will stop processing the project and report an error. The optional <code>&lt;policy_max&gt;</code> version, if specified, must be at least the <code>&lt;min&gt;</code> version and affects policy settings as described in <i>Policy Settings</i>. If the running version of CMake is older than 3.12, the extra <code>...</code> dots will be seen as version component separators, resulting in the <code>...&lt;max&gt;</code> part being ignored and preserving the pre-3.12 behavior of basing policies on <code>&lt;min&gt;</code>. </p>
<p>This command will set the value of the <code>CMAKE_MINIMUM_REQUIRED_VERSION</code> variable to <code>&lt;min&gt;</code>. </p>
<p>The <code>FATAL_ERROR</code> option is accepted but ignored by CMake 2.6 and higher. It should be specified so CMake versions 2.4 and lower fail with an error instead of just a warning. </p>
<p> <code>NOTE:</code> Call the <code>cmake_minimum_required()</code> command at the beginning of the top-level <code>CMakeLists.txt</code> file even before calling the <code>project()</code> command. It is important to establish version and policy settings before invoking other commands whose behavior they may affect. See also policy <code>CMP0000</code>. </p>
<p>Calling <code>cmake_minimum_required()</code> inside a <code>function()</code> limits some effects to the function scope when invoked. For example, the <code>CMAKE_MINIMUM_REQUIRED_VERSION</code> variable won&#8217;t be set in the calling scope. Functions do not introduce their own policy scope though, so policy settings of the caller <i>will</i> be affected (see below). Due to this mix of things that do and do not affect the calling scope, calling <code>cmake_minimum_required()</code> inside a function is generally discouraged.  </p>
<h3>Policy Settings</h3>
<p>The <code>cmake_minimum_required(VERSION)</code> command implicitly invokes the <code>cmake_policy(VERSION)</code> command to specify that the current project code is written for the given range of CMake versions. All policies known to the running version of CMake and introduced in the <code>&lt;min&gt;</code> (or <code>&lt;max&gt;</code>, if specified) version or earlier will be set to use <code>NEW</code> behavior. All policies introduced in later versions will be unset. This effectively requests behavior preferred as of a given CMake version and tells newer CMake versions to warn about their new policies. </p>
<p>When a <code>&lt;min&gt;</code> version higher than 2.4 is specified the command implicitly invokes </p>
<pre><code>cmake_policy(VERSION &lt;min&gt;[...&lt;max&gt;])
</code></pre>
<p>which sets CMake policies based on the range of versions specified. When a <code>&lt;min&gt;</code> version 2.4 or lower is given the command implicitly invokes </p>
<pre><code>cmake_policy(VERSION 2.4[...&lt;max&gt;])
</code></pre>
<p>which enables compatibility features for CMake 2.4 and lower.  </p>
<h3>cmake_parse_arguments</h3>
<p>Parse function or macro arguments. </p>
<pre><code>cmake_parse_arguments(&lt;prefix&gt; &lt;options&gt; &lt;one_value_keywords&gt;
                      &lt;multi_value_keywords&gt; &lt;args&gt;...)
cmake_parse_arguments(PARSE_ARGV &lt;N&gt; &lt;prefix&gt; &lt;options&gt;
                      &lt;one_value_keywords&gt; &lt;multi_value_keywords&gt;)
</code></pre>
<p>New in version 3.5: This command is implemented natively. Previously, it has been defined in the module <code>CMakeParseArguments</code>. </p>
<p>This command is for use in macros or functions. It processes the arguments given to that macro or function, and defines a set of variables which hold the values of the respective options. </p>
<p>The first signature reads processes arguments passed in the <code>&lt;args&gt;...</code>. This may be used in either a <code>macro()</code> or a <code>function()</code>. </p>
<p>New in version 3.7: The <code>PARSE_ARGV</code> signature is only for use in a <code>function()</code> body. In this case the arguments that are parsed come from the <code>ARGV#</code> variables of the calling function. The parsing starts with the <code>&lt;N&gt;</code>-th argument, where <code>&lt;N&gt;</code> is an unsigned integer. This allows for the values to have special characters like <code>;</code> in them. </p>
<p>The <code>&lt;options&gt;</code> argument contains all options for the respective macro, i.e. keywords which can be used when calling the macro without any value following, like e.g. the <code>OPTIONAL</code> keyword of the <code>install()</code> command. </p>
<p>The <code>&lt;one_value_keywords&gt;</code> argument contains all keywords for this macro which are followed by one value, like e.g. <code>DESTINATION</code> keyword of the <code>install()</code> command. </p>
<p>The <code>&lt;multi_value_keywords&gt;</code> argument contains all keywords for this macro which can be followed by more than one value, like e.g. the <code>TARGETS</code> or <code>FILES</code> keywords of the <code>install()</code> command. </p>
<p>Changed in version 3.5: All keywords shall be unique. I.e. every keyword shall only be specified once in either <code>&lt;options&gt;</code>, <code>&lt;one_value_keywords&gt;</code> or <code>&lt;multi_value_keywords&gt;</code>. A warning will be emitted if uniqueness is violated. </p>
<p>When done, <code>cmake_parse_arguments</code> will consider for each of the keywords listed in <code>&lt;options&gt;</code>, <code>&lt;one_value_keywords&gt;</code> and <code>&lt;multi_value_keywords&gt;</code> a variable composed of the given <code>&lt;prefix&gt;</code> followed by <code>&quot;_&quot;</code> and the name of the respective keyword. These variables will then hold the respective value from the argument list or be undefined if the associated option could not be found. For the <code>&lt;options&gt;</code> keywords, these will always be defined, to <code>TRUE</code> or <code>FALSE</code>, whether the option is in the argument list or not. </p>
<p>All remaining arguments are collected in a variable <code>&lt;prefix&gt;_UNPARSED_ARGUMENTS</code> that will be undefined if all arguments were recognized. This can be checked afterwards to see whether your macro was called with unrecognized parameters. </p>
<p>New in version 3.15: <code>&lt;one_value_keywords&gt;</code> and <code>&lt;multi_value_keywords&gt;</code> that were given no values at all are collected in a variable <code>&lt;prefix&gt;_KEYWORDS_MISSING_VALUES</code> that will be undefined if all keywords received values. This can be checked to see if there were keywords without any values given. </p>
<p>Consider the following example macro, <code>my_install()</code>, which takes similar arguments to the real <code>install()</code> command: </p>
<pre><code>macro(my_install)
    set(options OPTIONAL FAST)
    set(oneValueArgs DESTINATION RENAME)
    set(multiValueArgs TARGETS CONFIGURATIONS)
    cmake_parse_arguments(MY_INSTALL &quot;${options}&quot; &quot;${oneValueArgs}&quot;
                          &quot;${multiValueArgs}&quot; ${ARGN} )
    # ...
</code></pre>
<p>Assume <code>my_install()</code> has been called like this: </p>
<pre><code>my_install(TARGETS foo bar DESTINATION bin OPTIONAL blub CONFIGURATIONS)
</code></pre>
<p>After the <code>cmake_parse_arguments</code> call the macro will have set or undefined the following variables: </p>
<pre><code>MY_INSTALL_OPTIONAL = TRUE
MY_INSTALL_FAST = FALSE # was not used in call to my_install
MY_INSTALL_DESTINATION = &quot;bin&quot;
MY_INSTALL_RENAME &lt;UNDEFINED&gt; # was not used
MY_INSTALL_TARGETS = &quot;foo;bar&quot;
MY_INSTALL_CONFIGURATIONS &lt;UNDEFINED&gt; # was not used
MY_INSTALL_UNPARSED_ARGUMENTS = &quot;blub&quot; # nothing expected after &quot;OPTIONAL&quot;
MY_INSTALL_KEYWORDS_MISSING_VALUES = &quot;CONFIGURATIONS&quot;
         # No value for &quot;CONFIGURATIONS&quot; given
</code></pre>
<p>You can then continue and process these variables. </p>
<p>Keywords terminate lists of values, e.g. if directly after a <code>one_value_keyword</code> another recognized keyword follows, this is interpreted as the beginning of the new option. E.g. <code>my_install(TARGETS foo DESTINATION OPTIONAL)</code> would result in <code>MY_INSTALL_DESTINATION</code> set to <code>&quot;OPTIONAL&quot;</code>, but as <code>OPTIONAL</code> is a keyword itself <code>MY_INSTALL_DESTINATION</code> will be empty (but added to <code>MY_INSTALL_KEYWORDS_MISSING_VALUES</code>) and <code>MY_INSTALL_OPTIONAL</code> will therefore be set to <code>TRUE</code>.  </p>
<h3>cmake_path</h3>
<p>New in version 3.20. </p>
<p>This command is for the manipulation of paths. Only syntactic aspects of paths are handled, there is no interaction of any kind with any underlying file system. The path may represent a non-existing path or even one that is not allowed to exist on the current file system or platform. For operations that do interact with the filesystem, see the <code>file()</code> command. </p>
<p> <code>NOTE:</code> The <code>cmake_path</code> command handles paths in the format of the build system (i.e. the host platform), not the target system. When cross-compiling, if the path contains elements that are not representable on the host platform (e.g. a drive letter when the host is not Windows), the results will be unpredictable.  </p>
<h3>Synopsis</h3>
<pre><code>
 Conventions 
 Path Structure And Terminology 
 Normalization 
 Decomposition   cmake_path( GET  &lt;path-var&gt; ROOT_NAME  &lt;out-var&gt;)
  cmake_path( GET  &lt;path-var&gt; ROOT_DIRECTORY  &lt;out-var&gt;)
  cmake_path( GET  &lt;path-var&gt; ROOT_PATH  &lt;out-var&gt;)
  cmake_path( GET  &lt;path-var&gt; FILENAME  &lt;out-var&gt;)
  cmake_path( GET  &lt;path-var&gt; EXTENSION  [LAST_ONLY] &lt;out-var&gt;)
  cmake_path( GET  &lt;path-var&gt; STEM  [LAST_ONLY] &lt;out-var&gt;)
  cmake_path( GET  &lt;path-var&gt; RELATIVE_PART  &lt;out-var&gt;)
  cmake_path( GET  &lt;path-var&gt; PARENT_PATH  &lt;out-var&gt;)
 Query   cmake_path( HAS_ROOT_NAME  &lt;path-var&gt; &lt;out-var&gt;)
  cmake_path( HAS_ROOT_DIRECTORY  &lt;path-var&gt; &lt;out-var&gt;)
  cmake_path( HAS_ROOT_PATH  &lt;path-var&gt; &lt;out-var&gt;)
  cmake_path( HAS_FILENAME  &lt;path-var&gt; &lt;out-var&gt;)
  cmake_path( HAS_EXTENSION  &lt;path-var&gt; &lt;out-var&gt;)
  cmake_path( HAS_STEM  &lt;path-var&gt; &lt;out-var&gt;)
  cmake_path( HAS_RELATIVE_PART  &lt;path-var&gt; &lt;out-var&gt;)
  cmake_path( HAS_PARENT_PATH  &lt;path-var&gt; &lt;out-var&gt;)
  cmake_path( IS_ABSOLUTE  &lt;path-var&gt; &lt;out-var&gt;)
  cmake_path( IS_RELATIVE  &lt;path-var&gt; &lt;out-var&gt;)
  cmake_path( IS_PREFIX  &lt;path-var&gt; &lt;input&gt; [NORMALIZE] &lt;out-var&gt;)
  cmake_path( COMPARE  &lt;input1&gt; &lt;OP&gt; &lt;input2&gt; &lt;out-var&gt;)
 Modification   cmake_path( SET  &lt;path-var&gt; [NORMALIZE] &lt;input&gt;)
  cmake_path( APPEND  &lt;path-var&gt; [&lt;input&gt;...] [OUTPUT_VARIABLE &lt;out-var&gt;])
  cmake_path( APPEND_STRING  &lt;path-var&gt; [&lt;input&gt;...] [OUTPUT_VARIABLE &lt;out-var&gt;])
  cmake_path( REMOVE_FILENAME  &lt;path-var&gt; [OUTPUT_VARIABLE &lt;out-var&gt;])
  cmake_path( REPLACE_FILENAME  &lt;path-var&gt; &lt;input&gt; [OUTPUT_VARIABLE &lt;out-var&gt;])
  cmake_path( REMOVE_EXTENSION  &lt;path-var&gt; [LAST_ONLY] [OUTPUT_VARIABLE &lt;out-var&gt;])
  cmake_path( REPLACE_EXTENSION  &lt;path-var&gt; [LAST_ONLY] &lt;input&gt; [OUTPUT_VARIABLE &lt;out-var&gt;])
 Generation   cmake_path( NORMAL_PATH  &lt;path-var&gt; [OUTPUT_VARIABLE &lt;out-var&gt;])
  cmake_path( RELATIVE_PATH  &lt;path-var&gt; [BASE_DIRECTORY &lt;input&gt;] [OUTPUT_VARIABLE &lt;out-var&gt;])
  cmake_path( ABSOLUTE_PATH  &lt;path-var&gt; [BASE_DIRECTORY &lt;input&gt;] [NORMALIZE] [OUTPUT_VARIABLE &lt;out-var&gt;])
 Native Conversion   cmake_path( NATIVE_PATH  &lt;path-var&gt; [NORMALIZE] &lt;out-var&gt;)
  cmake_path( CONVERT  &lt;input&gt; TO_CMAKE_PATH_LIST  &lt;out-var&gt; [NORMALIZE])
  cmake_path( CONVERT  &lt;input&gt; TO_NATIVE_PATH_LIST  &lt;out-var&gt; [NORMALIZE])
 Hashing   cmake_path( HASH  &lt;path-var&gt; &lt;out-var&gt;)
</code></pre>
<h3>Conventions</h3>
<p>The following conventions are used in this command&#8217;s documentation: </p>
<dl>
<dt><code>&lt;path-var&gt;</code></dt>
<dd> <p> Always the name of a variable. For commands that expect a <code>&lt;path-var&gt;</code> as input, the variable must exist and it is expected to hold a single path. </p>
 </dd>
<dt><code>&lt;input&gt;</code></dt>
<dd> <p> A string literal which may contain a path, path fragment, or multiple paths with a special separator depending on the command. See the description of each command to see how this is interpreted. </p>
 </dd>
<dt><code>&lt;input&gt;...</code></dt>
<dd> <p> Zero or more string literal arguments. </p>
 </dd>
<dt><code>&lt;out-var&gt;</code></dt>
<dd> <p> The name of a variable into which the result of a command will be written. </p>
 </dd></dl>
<h3>Path Structure And Terminology</h3>
<p>A path has the following structure (all components are optional, with some constraints): </p>
<pre><code>root-name root-directory-separator (item-name directory-separator)* filename
</code></pre>
<dl>
<dt><code>root-name</code></dt>
<dd> <p> Identifies the root on a filesystem with multiple roots (such as <code>&quot;C:&quot;</code> or <code>&quot;//myserver&quot;</code>). It is optional. </p>
 </dd>
<dt><code>root-directory-separator</code></dt>
<dd> <p> A directory separator that, if present, indicates that this path is absolute. If it is missing and the first element other than the <code>root-name</code> is an <code>item-name</code>, then the path is relative. </p>
 </dd>
<dt><code>item-name</code></dt>
<dd> <p> A sequence of characters that aren&#8217;t directory separators. This name may identify a file, a hard link, a symbolic link, or a directory. Two special cases are recognized: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The item name consisting of a single dot character <code>.</code> is a directory name that refers to the current directory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The item name consisting of two dot characters <code>..</code> is a directory name that refers to the parent directory. </p>
<p>The <code>(...)*</code> pattern shown above is to indicate that there can be zero or more item names, with multiple items separated by a <code>directory-separator</code>. The <code>()*</code> characters are not part of the path. </p>
 </dd>
<dt><code>directory-separator</code></dt>
<dd> <p> The only recognized directory separator is a forward slash character <code>/</code>. If this character is repeated, it is treated as a single directory separator. In other words, <code>/usr///////lib</code> is the same as <code>/usr/lib</code>. </p>
 </dd>
<dt><code>filename</code></dt>
<dd> <p> A path has a <code>filename</code> if it does not end with a <code>directory-separator</code>. The <code>filename</code> is effectively the last <code>item-name</code> of the path, so it can also be a hard link, symbolic link or a directory. </p>
<p>A <code>filename</code> can have an <i>extension</i>. By default, the extension is defined as the sub-string beginning at the left-most period (including the period) and until the end of the <code>filename</code>. In commands that accept a <code>LAST_ONLY</code> keyword, <code>LAST_ONLY</code> changes the interpretation to the sub-string beginning at the right-most period. </p>
<p>The following exceptions apply to the above interpretation: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If the first character in the <code>filename</code> is a period, that period is ignored (i.e. a <code>filename</code> like <code>&quot;.profile&quot;</code> is treated as having no extension). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If the <code>filename</code> is either <code>.</code> or <code>..</code>, it has no extension. </p>
<p>The <i>stem</i> is the part of the <code>filename</code> before the extension. </p>
<p>Some commands refer to a <code>root-path</code>. This is the concatenation of <code>root-name</code> and <code>root-directory-separator</code>, either or both of which can be empty. A <code>relative-part</code> refers to the full path with any <code>root-path</code> removed. </p>
 </dd></dl>
<h3>Creating A Path Variable</h3>
<p>While a path can be created with care using an ordinary <code>set()</code> command, it is recommended to use <i>cmake_path(SET)</i> instead, as it automatically converts the path to the required form where required. The cmake_path(APPEND) subcommand may be another suitable alternative where a path needs to be constructed by joining fragments. The following example compares the three methods for constructing the same path: </p>
<pre><code>set(path1 &quot;${CMAKE_CURRENT_SOURCE_DIR}/data&quot;)
cmake_path(SET path2 &quot;${CMAKE_CURRENT_SOURCE_DIR}/data&quot;)
cmake_path(APPEND path3 &quot;${CMAKE_CURRENT_SOURCE_DIR}&quot; &quot;data&quot;)
</code></pre>
<p> <i>Modification</i> and <i>Generation</i> sub-commands can either store the result in-place, or in a separate variable named after an <code>OUTPUT_VARIABLE</code> keyword. All other sub-commands store the result in a mandatory <code>&lt;out-var&gt;</code> variable.  </p>
<h3>Normalization</h3>
<p>Some sub-commands support <i>normalizing</i> a path. The algorithm used to normalize a path is as follows: </p>
<dl>
<dt>1.</dt>
<dd> <p> If the path is empty, stop (the normalized form of an empty path is also an empty path). </p>
 </dd>
<dt>2.</dt>
<dd> <p> Replace each <code>directory-separator</code>, which may consist of multiple separators, with a single <code>/</code> (<code>/a///b --&gt; /a/b</code>). </p>
 </dd>
<dt>3.</dt>
<dd> <p> Remove each solitary period (<code>.</code>) and any immediately following <code>directory-separator</code> (<code>/a/./b/. --&gt; /a/b</code>). </p>
 </dd>
<dt>4.</dt>
<dd> <p> Remove each <code>item-name</code> (other than <code>..</code>) that is immediately followed by a <code>directory-separator</code> and a <code>..</code>, along with any immediately following <code>directory-separator</code> (<code>/a/b/../c --&gt; a/c</code>). </p>
 </dd>
<dt>5.</dt>
<dd> <p> If there is a <code>root-directory</code>, remove any <code>..</code> and any <code>directory-separators</code> immediately following them. The parent of the root directory is treated as still the root directory (<code>/../a --&gt; /a</code>). </p>
 </dd>
<dt>6.</dt>
<dd> <p> If the last <code>item-name</code> is <code>..</code>, remove any trailing <code>directory-separator</code> (<code>../ --&gt; ..</code>). </p>
 </dd>
<dt>7.</dt>
<dd> <p> If the path is empty by this stage, add a <code>dot</code> (normal form of <code>./</code> is <code>.</code>). </p>
 </dd></dl>
<h3>Decomposition</h3>
<p>The following forms of the <code>GET</code> subcommand each retrieve a different component or group of components from a path. See <i>Path Structure And Terminology</i> for the meaning of each path component. </p>
<pre><code>cmake_path(GET &lt;path-var&gt; ROOT_NAME &lt;out-var&gt;)
cmake_path(GET &lt;path-var&gt; ROOT_DIRECTORY &lt;out-var&gt;)
cmake_path(GET &lt;path-var&gt; ROOT_PATH &lt;out-var&gt;)
cmake_path(GET &lt;path-var&gt; FILENAME &lt;out-var&gt;)
cmake_path(GET &lt;path-var&gt; EXTENSION [LAST_ONLY] &lt;out-var&gt;)
cmake_path(GET &lt;path-var&gt; STEM [LAST_ONLY] &lt;out-var&gt;)
cmake_path(GET &lt;path-var&gt; RELATIVE_PART &lt;out-var&gt;)
cmake_path(GET &lt;path-var&gt; PARENT_PATH &lt;out-var&gt;)
</code></pre>
<p>If a requested component is not present in the path, an empty string will be stored in <code>&lt;out-var&gt;</code>. For example, only Windows systems have the concept of a <code>root-name</code>, so when the host machine is non-Windows, the <code>ROOT_NAME</code> subcommand will always return an empty string. </p>
<p>For <code>PARENT_PATH</code>, if the <i>HAS_RELATIVE_PART</i> subcommand returns false, the result is a copy of <code>&lt;path-var&gt;</code>. Note that this implies that a root directory is considered to have a parent, with that parent being itself. Where <i>HAS_RELATIVE_PART</i> returns true, the result will essentially be <code>&lt;path-var&gt;</code> with one less element.  </p>
<h3>Root examples</h3>
<pre><code>set(path &quot;c:/a&quot;)
cmake_path(GET path ROOT_NAME rootName)
cmake_path(GET path ROOT_DIRECTORY rootDir)
cmake_path(GET path ROOT_PATH rootPath)
message(&quot;Root name is \&quot;${rootName}\&quot;&quot;)
message(&quot;Root directory is \&quot;${rootDir}\&quot;&quot;)
message(&quot;Root path is \&quot;${rootPath}\&quot;&quot;)
</code></pre>
<pre><code>Root name is &quot;c:&quot;
Root directory is &quot;/&quot;
Root path is &quot;c:/&quot;
</code></pre>
<h3>Filename examples</h3>
<pre><code>set(path &quot;/a/b&quot;)
cmake_path(GET path FILENAME filename)
message(&quot;First filename is \&quot;${filename}\&quot;&quot;)
# Trailing slash means filename is empty
set(path &quot;/a/b/&quot;)
cmake_path(GET path FILENAME filename)
message(&quot;Second filename is \&quot;${filename}\&quot;&quot;)
</code></pre>
<pre><code>First filename is &quot;b&quot;
Second filename is &quot;&quot;
</code></pre>
<h3>Extension and stem examples</h3>
<pre><code>set(path &quot;name.ext1.ext2&quot;)
cmake_path(GET path EXTENSION fullExt)
cmake_path(GET path STEM fullStem)
message(&quot;Full extension is \&quot;${fullExt}\&quot;&quot;)
message(&quot;Full stem is \&quot;${fullStem}\&quot;&quot;)
# Effect of LAST_ONLY
cmake_path(GET path EXTENSION LAST_ONLY lastExt)
cmake_path(GET path STEM LAST_ONLY lastStem)
message(&quot;Last extension is \&quot;${lastExt}\&quot;&quot;)
message(&quot;Last stem is \&quot;${lastStem}\&quot;&quot;)
# Special cases
set(dotPath &quot;/a/.&quot;)
set(dotDotPath &quot;/a/..&quot;)
set(someMorePath &quot;/a/.some.more&quot;)
cmake_path(GET dotPath EXTENSION dotExt)
cmake_path(GET dotPath STEM dotStem)
cmake_path(GET dotDotPath EXTENSION dotDotExt)
cmake_path(GET dotDotPath STEM dotDotStem)
cmake_path(GET dotMorePath EXTENSION someMoreExt)
cmake_path(GET dotMorePath STEM someMoreStem)
message(&quot;Dot extension is \&quot;${dotExt}\&quot;&quot;)
message(&quot;Dot stem is \&quot;${dotStem}\&quot;&quot;)
message(&quot;Dot-dot extension is \&quot;${dotDotExt}\&quot;&quot;)
message(&quot;Dot-dot stem is \&quot;${dotDotStem}\&quot;&quot;)
message(&quot;.some.more extension is \&quot;${someMoreExt}\&quot;&quot;)
message(&quot;.some.more stem is \&quot;${someMoreStem}\&quot;&quot;)
</code></pre>
<pre><code>Full extension is &quot;.ext1.ext2&quot;
Full stem is &quot;name&quot;
Last extension is &quot;.ext2&quot;
Last stem is &quot;name.ext1&quot;
Dot extension is &quot;&quot;
Dot stem is &quot;.&quot;
Dot-dot extension is &quot;&quot;
Dot-dot stem is &quot;..&quot;
.some.more extension is &quot;.more&quot;
.some.more stem is &quot;.some&quot;
</code></pre>
<h3>Relative part examples</h3>
<pre><code>set(path &quot;c:/a/b&quot;)
cmake_path(GET path RELATIVE_PART result)
message(&quot;Relative part is \&quot;${result}\&quot;&quot;)
set(path &quot;c/d&quot;)
cmake_path(GET path RELATIVE_PART result)
message(&quot;Relative part is \&quot;${result}\&quot;&quot;)
set(path &quot;/&quot;)
cmake_path(GET path RELATIVE_PART result)
message(&quot;Relative part is \&quot;${result}\&quot;&quot;)
</code></pre>
<pre><code>Relative part is &quot;a/b&quot;
Relative part is &quot;c/d&quot;
Relative part is &quot;&quot;
</code></pre>
<h3>Path traversal examples</h3>
<pre><code>set(path &quot;c:/a/b&quot;)
cmake_path(GET path PARENT_PATH result)
message(&quot;Parent path is \&quot;${result}\&quot;&quot;)
set(path &quot;c:/&quot;)
cmake_path(GET path PARENT_PATH result)
message(&quot;Parent path is \&quot;${result}\&quot;&quot;)
</code></pre>
<pre><code>Parent path is &quot;c:/a&quot;
Parent path is &quot;c:/&quot;
</code></pre>
<h3>Query</h3>
<p>Each of the <code>GET</code> subcommands has a corresponding <code>HAS_...</code> subcommand which can be used to discover whether a particular path component is present. See <i>Path Structure And Terminology</i> for the meaning of each path component. </p>
<pre><code>cmake_path(HAS_ROOT_NAME &lt;path-var&gt; &lt;out-var&gt;)
cmake_path(HAS_ROOT_DIRECTORY &lt;path-var&gt; &lt;out-var&gt;)
cmake_path(HAS_ROOT_PATH &lt;path-var&gt; &lt;out-var&gt;)
cmake_path(HAS_FILENAME &lt;path-var&gt; &lt;out-var&gt;)
cmake_path(HAS_EXTENSION &lt;path-var&gt; &lt;out-var&gt;)
cmake_path(HAS_STEM &lt;path-var&gt; &lt;out-var&gt;)
cmake_path(HAS_RELATIVE_PART &lt;path-var&gt; &lt;out-var&gt;)
cmake_path(HAS_PARENT_PATH &lt;path-var&gt; &lt;out-var&gt;)
</code></pre>
<p>Each of the above follows the predictable pattern of setting <code>&lt;out-var&gt;</code> to true if the path has the associated component, or false otherwise. Note the following special cases: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> For <code>HAS_ROOT_PATH</code>, a true result will only be returned if at least one of <code>root-name</code> or <code>root-directory</code> is non-empty. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> For <code>HAS_PARENT_PATH</code>, the root directory is also considered to have a parent, which will be itself. The result is true except if the path consists of just a <i>filename</i>. </p>
<pre><code>cmake_path(IS_ABSOLUTE &lt;path-var&gt; &lt;out-var&gt;)
</code></pre>
<p>Sets <code>&lt;out-var&gt;</code> to true if <code>&lt;path-var&gt;</code> is absolute. An absolute path is a path that unambiguously identifies the location of a file without reference to an additional starting location. On Windows, this means the path must have both a <code>root-name</code> and a <code>root-directory-separator</code> to be considered absolute. On other platforms, just a <code>root-directory-separator</code> is sufficient. Note that this means on Windows, <code>IS_ABSOLUTE</code> can be false while <code>HAS_ROOT_DIRECTORY</code> can be true. </p>
<pre><code>cmake_path(IS_RELATIVE &lt;path-var&gt; &lt;out-var&gt;)
</code></pre>
<p>This will store the opposite of <code>IS_ABSOLUTE</code> in <code>&lt;out-var&gt;</code>. </p>
<pre><code>cmake_path(IS_PREFIX &lt;path-var&gt; &lt;input&gt; [NORMALIZE] &lt;out-var&gt;)
</code></pre>
<p>Checks if <code>&lt;path-var&gt;</code> is the prefix of <code>&lt;input&gt;</code>. </p>
<p>When the <code>NORMALIZE</code> option is specified, <code>&lt;path-var&gt;</code> and <code>&lt;input&gt;</code> are <i>normalized</i> before the check. </p>
<pre><code>set(path &quot;/a/b/c&quot;)
cmake_path(IS_PREFIX path &quot;/a/b/c/d&quot; result) # result = true
cmake_path(IS_PREFIX path &quot;/a/b&quot; result) # result = false
cmake_path(IS_PREFIX path &quot;/x/y/z&quot; result) # result = false
set(path &quot;/a/b&quot;)
cmake_path(IS_PREFIX path &quot;/a/c/../b&quot; NORMALIZE result) # result = true
</code></pre>
<pre><code>cmake_path(COMPARE &lt;input1&gt; EQUAL &lt;input2&gt; &lt;out-var&gt;)
cmake_path(COMPARE &lt;input1&gt; NOT_EQUAL &lt;input2&gt; &lt;out-var&gt;)
</code></pre>
<p>Compares the lexical representations of two paths provided as string literals. No normalization is performed on either path. Equality is determined according to the following pseudo-code logic: </p>
<pre><code>if(NOT &lt;input1&gt;.root_name() STREQUAL &lt;input2&gt;.root_name())
  return FALSE
if(&lt;input1&gt;.has_root_directory() XOR &lt;input2&gt;.has_root_directory())
  return FALSE
Return FALSE if a relative portion of &lt;input1&gt; is not lexicographically
equal to the relative portion of &lt;input2&gt;. This comparison is performed path
component-wise. If all of the components compare equal, then return TRUE.
</code></pre>
<p> <code>NOTE:</code> Unlike most other <code>cmake_path()</code> subcommands, the <code>COMPARE</code> subcommand takes literal strings as input, not the names of variables. </p>
 </dd></dl>
<h3>Modification</h3>
<pre><code>cmake_path(SET &lt;path-var&gt; [NORMALIZE] &lt;input&gt;)
</code></pre>
<p>Assign the <code>&lt;input&gt;</code> path to <code>&lt;path-var&gt;</code>. If <code>&lt;input&gt;</code> is a native path, it is converted into a cmake-style path with forward-slashes (<code>/</code>). On Windows, the long filename marker is taken into account. </p>
<p>When the <code>NORMALIZE</code> option is specified, the path is <i>normalized</i> before the conversion. </p>
<p>For example: </p>
<pre><code>set(native_path &quot;c:\\a\\b/..\\c&quot;)
cmake_path(SET path &quot;${native_path}&quot;)
message(&quot;CMake path is \&quot;${path}\&quot;&quot;)
cmake_path(SET path NORMALIZE &quot;${native_path}&quot;)
message(&quot;Normalized CMake path is \&quot;${path}\&quot;&quot;)
</code></pre>
<p>Output: </p>
<pre><code>CMake path is &quot;c:/a/b/../c&quot;
Normalized CMake path is &quot;c:/a/c&quot;
</code></pre>
<pre><code>cmake_path(APPEND &lt;path-var&gt; [&lt;input&gt;...] [OUTPUT_VARIABLE &lt;out-var&gt;])
</code></pre>
<p>Append all the <code>&lt;input&gt;</code> arguments to the <code>&lt;path-var&gt;</code> using <code>/</code> as the <code>directory-separator</code>. Depending on the <code>&lt;input&gt;</code>, the previous contents of <code>&lt;path-var&gt;</code> may be discarded. For each <code>&lt;input&gt;</code> argument, the following algorithm (pseudo-code) applies: </p>
<pre><code># &lt;path&gt; is the contents of &lt;path-var&gt;
if(&lt;input&gt;.is_absolute() OR
   (&lt;input&gt;.has_root_name() AND
    NOT &lt;input&gt;.root_name() STREQUAL &lt;path&gt;.root_name()))
  replace &lt;path&gt; with &lt;input&gt;
  return()
endif()
if(&lt;input&gt;.has_root_directory())
  remove any root-directory and the entire relative path from &lt;path&gt;
elseif(&lt;path&gt;.has_filename() OR
       (NOT &lt;path-var&gt;.has_root_directory() OR &lt;path&gt;.is_absolute()))
  append directory-separator to &lt;path&gt;
endif()
append &lt;input&gt; omitting any root-name to &lt;path&gt;
</code></pre>
<pre><code>cmake_path(APPEND_STRING &lt;path-var&gt; [&lt;input&gt;...] [OUTPUT_VARIABLE &lt;out-var&gt;])
</code></pre>
<p>Append all the <code>&lt;input&gt;</code> arguments to the <code>&lt;path-var&gt;</code> without adding any <code>directory-separator</code>. </p>
<pre><code>cmake_path(REMOVE_FILENAME &lt;path-var&gt; [OUTPUT_VARIABLE &lt;out-var&gt;])
</code></pre>
<p>Removes the <i>filename</i> component (as returned by <i>GET ... FILENAME</i>) from <code>&lt;path-var&gt;</code>. After removal, any trailing <code>directory-separator</code> is left alone, if present. </p>
<p>If <code>OUTPUT_VARIABLE</code> is not given, then after this function returns, <i>HAS_FILENAME</i> returns false for <code>&lt;path-var&gt;</code>. </p>
<p>For example: </p>
<pre><code>set(path &quot;/a/b&quot;)
cmake_path(REMOVE_FILENAME path)
message(&quot;First path is \&quot;${path}\&quot;&quot;)
# filename is now already empty, the following removes nothing
cmake_path(REMOVE_FILENAME path)
message(&quot;Second path is \&quot;${result}\&quot;&quot;)
</code></pre>
<p>Output: </p>
<pre><code>First path is &quot;/a/&quot;
Second path is &quot;/a/&quot;
</code></pre>
<pre><code>cmake_path(REPLACE_FILENAME &lt;path-var&gt; &lt;input&gt; [OUTPUT_VARIABLE &lt;out-var&gt;])
</code></pre>
<p>Replaces the <i>filename</i> component from <code>&lt;path-var&gt;</code> with <code>&lt;input&gt;</code>. If <code>&lt;path-var&gt;</code> has no filename component (i.e. <i>HAS_FILENAME</i> returns false), the path is unchanged. The operation is equivalent to the following: </p>
<pre><code>cmake_path(HAS_FILENAME path has_filename)
if(has_filename)
  cmake_path(REMOVE_FILENAME path)
  cmake_path(APPEND path input);
endif()
</code></pre>
<pre><code>cmake_path(REMOVE_EXTENSION &lt;path-var&gt; [LAST_ONLY]
                                       [OUTPUT_VARIABLE &lt;out-var&gt;])
</code></pre>
<p>Removes the <i>extension</i>, if any, from <code>&lt;path-var&gt;</code>. </p>
<pre><code>cmake_path(REPLACE_EXTENSION &lt;path-var&gt; [LAST_ONLY] &lt;input&gt;
                             [OUTPUT_VARIABLE &lt;out-var&gt;])
</code></pre>
<p>Replaces the <i>extension</i> with <code>&lt;input&gt;</code>. Its effect is equivalent to the following: </p>
<pre><code>cmake_path(REMOVE_EXTENSION path)
if(NOT &quot;input&quot; MATCHES &quot;^\\.&quot;)
  cmake_path(APPEND_STRING path &quot;.&quot;)
endif()
cmake_path(APPEND_STRING path &quot;input&quot;)
</code></pre>
<h3>Generation</h3>
<pre><code>cmake_path(NORMAL_PATH &lt;path-var&gt; [OUTPUT_VARIABLE &lt;out-var&gt;])
</code></pre>
<p>Normalize <code>&lt;path-var&gt;</code> according the steps described in <i>Normalization</i>. </p>
<pre><code>cmake_path(RELATIVE_PATH &lt;path-var&gt; [BASE_DIRECTORY &lt;input&gt;]
                                    [OUTPUT_VARIABLE &lt;out-var&gt;])
</code></pre>
<p>Modifies <code>&lt;path-var&gt;</code> to make it relative to the <code>BASE_DIRECTORY</code> argument. If <code>BASE_DIRECTORY</code> is not specified, the default base directory will be <code>CMAKE_CURRENT_SOURCE_DIR</code>. </p>
<p>For reference, the algorithm used to compute the relative path is the same as that used by C++ <i>std::filesystem::path::lexically_relative</i>. </p>
<pre><code>cmake_path(ABSOLUTE_PATH &lt;path-var&gt; [BASE_DIRECTORY &lt;input&gt;] [NORMALIZE]
                                    [OUTPUT_VARIABLE &lt;out-var&gt;])
</code></pre>
<p>If <code>&lt;path-var&gt;</code> is a relative path (<i>IS_RELATIVE</i> is true), it is evaluated relative to the given base directory specified by <code>BASE_DIRECTORY</code> option. If <code>BASE_DIRECTORY</code> is not specified, the default base directory will be <code>CMAKE_CURRENT_SOURCE_DIR</code>. </p>
<p>When the <code>NORMALIZE</code> option is specified, the path is <i>normalized</i> after the path computation. </p>
<p>Because <code>cmake_path()</code> does not access the filesystem, symbolic links are not resolved and any leading tilde is not expanded. To compute a real path with symbolic links resolved and leading tildes expanded, use the <code>file(REAL_PATH)</code> command instead.  </p>
<h3>Native Conversion</h3>
<p>For commands in this section, <i>native</i> refers to the host platform, not the target platform when cross-compiling. </p>
<pre><code>cmake_path(NATIVE_PATH &lt;path-var&gt; [NORMALIZE] &lt;out-var&gt;)
</code></pre>
<p>Converts a cmake-style <code>&lt;path-var&gt;</code> into a native path with platform-specific slashes (<code>\</code> on Windows hosts and <code>/</code> elsewhere). </p>
<p>When the <code>NORMALIZE</code> option is specified, the path is <i>normalized</i> before the conversion. </p>
<pre><code>cmake_path(CONVERT &lt;input&gt; TO_CMAKE_PATH_LIST &lt;out-var&gt; [NORMALIZE])
</code></pre>
<p>Converts a native <code>&lt;input&gt;</code> path into a cmake-style path with forward slashes (<code>/</code>). On Windows hosts, the long filename marker is taken into account. The input can be a single path or a system search path like <code>$ENV{PATH}</code>. A search path will be converted to a cmake-style list separated by <code>;</code> characters (on non-Windows platforms, this essentially means <code>:</code> separators are replaced with <code>;</code>). The result of the conversion is stored in the <code>&lt;out-var&gt;</code> variable. </p>
<p>When the <code>NORMALIZE</code> option is specified, the path is <i>normalized</i> before the conversion. </p>
<p> <code>NOTE:</code> Unlike most other <code>cmake_path()</code> subcommands, the <code>CONVERT</code> subcommand takes a literal string as input, not the name of a variable. </p>
<pre><code>cmake_path(CONVERT &lt;input&gt; TO_NATIVE_PATH_LIST &lt;out-var&gt; [NORMALIZE])
</code></pre>
<p>Converts a cmake-style <code>&lt;input&gt;</code> path into a native path with platform-specific slashes (<code>\</code> on Windows hosts and <code>/</code> elsewhere). The input can be a single path or a cmake-style list. A list will be converted into a native search path (<code>;</code>-separated on Windows, <code>:</code>-separated on other platforms). The result of the conversion is stored in the <code>&lt;out-var&gt;</code> variable. </p>
<p>When the <code>NORMALIZE</code> option is specified, the path is <i>normalized</i> before the conversion. </p>
<p> <code>NOTE:</code> Unlike most other <code>cmake_path()</code> subcommands, the <code>CONVERT</code> subcommand takes a literal string as input, not the name of a variable. </p>
<p>For example: </p>
<pre><code>set(paths &quot;/a/b/c&quot; &quot;/x/y/z&quot;)
cmake_path(CONVERT &quot;${paths}&quot; TO_NATIVE_PATH_LIST native_paths)
message(&quot;Native path list is \&quot;${native_paths}\&quot;&quot;)
</code></pre>
<p>Output on Windows: </p>
<pre><code>Native path list is &quot;\a\b\c;\x\y\z&quot;
</code></pre>
<p>Output on all other platforms: </p>
<pre><code>Native path list is &quot;/a/b/c:/x/y/z&quot;
</code></pre>
<h3>Hashing</h3>
<pre><code>cmake_path(HASH &lt;path-var&gt; &lt;out-var&gt;)
</code></pre>
<p>Compute a hash value of <code>&lt;path-var&gt;</code> such that for two paths <code>p1</code> and <code>p2</code> that compare equal (COMPARE ... EQUAL), the hash value of <code>p1</code> is equal to the hash value of <code>p2</code>. The path is always <i>normalized</i> before the hash is computed.  </p>
<h3>cmake_policy</h3>
<p>Manage CMake Policy settings. See the <code><a href="/docs/linux/man/7-cmake-policies/">cmake-policies</a>(7)</code> manual for defined policies. </p>
<p>As CMake evolves it is sometimes necessary to change existing behavior in order to fix bugs or improve implementations of existing features. The CMake Policy mechanism is designed to help keep existing projects building as new versions of CMake introduce changes in behavior. Each new policy (behavioral change) is given an identifier of the form <code>CMP&lt;NNNN&gt;</code> where <code>&lt;NNNN&gt;</code> is an integer index. Documentation associated with each policy describes the <code>OLD</code> and <code>NEW</code> behavior and the reason the policy was introduced. Projects may set each policy to select the desired behavior. When CMake needs to know which behavior to use it checks for a setting specified by the project. If no setting is available the <code>OLD</code> behavior is assumed and a warning is produced requesting that the policy be set.  </p>
<h3>Setting Policies by CMake Version</h3>
<p>The <code>cmake_policy</code> command is used to set policies to <code>OLD</code> or <code>NEW</code> behavior. While setting policies individually is supported, we encourage projects to set policies based on CMake versions: </p>
<pre><code>cmake_policy(VERSION &lt;min&gt;[...&lt;max&gt;])
</code></pre>
<p>New in version 3.12: The optional <code>&lt;max&gt;</code> version. </p>
<p> <code>&lt;min&gt;</code> and the optional <code>&lt;max&gt;</code> are each CMake versions of the form <code>major.minor[.patch[.tweak]]</code>, and the <code>...</code> is literal. The <code>&lt;min&gt;</code> version must be at least <code>2.4</code> and at most the running version of CMake. The <code>&lt;max&gt;</code> version, if specified, must be at least the <code>&lt;min&gt;</code> version but may exceed the running version of CMake. If the running version of CMake is older than 3.12, the extra <code>...</code> dots will be seen as version component separators, resulting in the <code>...&lt;max&gt;</code> part being ignored and preserving the pre-3.12 behavior of basing policies on <code>&lt;min&gt;</code>. </p>
<p>This specifies that the current CMake code is written for the given range of CMake versions. All policies known to the running version of CMake and introduced in the <code>&lt;min&gt;</code> (or <code>&lt;max&gt;</code>, if specified) version or earlier will be set to use <code>NEW</code> behavior. All policies introduced in later versions will be unset (unless the <code>CMAKE_POLICY_DEFAULT_CMP&lt;NNNN&gt;</code> variable sets a default). This effectively requests behavior preferred as of a given CMake version and tells newer CMake versions to warn about their new policies. </p>
<p>Note that the <code>cmake_minimum_required(VERSION)</code> command implicitly calls <code>cmake_policy(VERSION)</code> too.  </p>
<h3>Setting Policies Explicitly</h3>
<pre><code>cmake_policy(SET CMP&lt;NNNN&gt; NEW)
cmake_policy(SET CMP&lt;NNNN&gt; OLD)
</code></pre>
<p>Tell CMake to use the <code>OLD</code> or <code>NEW</code> behavior for a given policy. Projects depending on the old behavior of a given policy may silence a policy warning by setting the policy state to <code>OLD</code>. Alternatively one may fix the project to work with the new behavior and set the policy state to <code>NEW</code>. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.  </p>
<h3>Checking Policy Settings</h3>
<pre><code>cmake_policy(GET CMP&lt;NNNN&gt; &lt;variable&gt;)
</code></pre>
<p>Check whether a given policy is set to <code>OLD</code> or <code>NEW</code> behavior. The output <code>&lt;variable&gt;</code> value will be <code>OLD</code> or <code>NEW</code> if the policy is set, and empty otherwise.  </p>
<h3>CMake Policy Stack</h3>
<p>CMake keeps policy settings on a stack, so changes made by the <code>cmake_policy</code> command affect only the top of the stack. A new entry on the policy stack is managed automatically for each subdirectory to protect its parents and siblings. CMake also manages a new entry for scripts loaded by <code>include()</code> and <code>find_package()</code> commands except when invoked with the <code>NO_POLICY_SCOPE</code> option (see also policy <code>CMP0011</code>). The <code>cmake_policy</code> command provides an interface to manage custom entries on the policy stack: </p>
<pre><code>cmake_policy(PUSH)
cmake_policy(POP)
</code></pre>
<p>Each <code>PUSH</code> must have a matching <code>POP</code> to erase any changes. This is useful to make temporary changes to policy settings. Calls to the <code>cmake_minimum_required(VERSION)</code>, <code>cmake_policy(VERSION)</code>, or <code>cmake_policy(SET)</code> commands influence only the current top of the policy stack. </p>
<p>Commands created by the <code>function()</code> and <code>macro()</code> commands record policy settings when they are created and use the pre-record policies when they are invoked. If the function or macro implementation sets policies, the changes automatically propagate up through callers until they reach the closest nested policy stack entry.  </p>
<h3>configure_file</h3>
<p>Copy a file to another location and modify its contents. </p>
<pre><code>configure_file(&lt;input&gt; &lt;output&gt;
               [NO_SOURCE_PERMISSIONS | USE_SOURCE_PERMISSIONS |
                FILE_PERMISSIONS &lt;permissions&gt;...]
               [COPYONLY] [ESCAPE_QUOTES] [@ONLY]
               [NEWLINE_STYLE [UNIX|DOS|WIN32|LF|CRLF] ])
</code></pre>
<p>Copies an <code>&lt;input&gt;</code> file to an <code>&lt;output&gt;</code> file and substitutes variable values referenced as <code>@VAR@</code> or <code>${VAR}</code> in the input file content. Each variable reference will be replaced with the current value of the variable, or the empty string if the variable is not defined. Furthermore, input lines of the form </p>
<pre><code>#cmakedefine VAR ...
</code></pre>
<p>will be replaced with either </p>
<pre><code>#define VAR ...
</code></pre>
<p>or </p>
<pre><code>/* #undef VAR */
</code></pre>
<p>depending on whether <code>VAR</code> is set in CMake to any value not considered a false constant by the <code>if()</code> command. The &quot;...&quot; content on the line after the variable name, if any, is processed as above. </p>
<p>Unlike lines of the form <code>#cmakedefine VAR ...</code>, in lines of the form <code>#cmakedefine01 VAR</code>, <code>VAR</code> itself will expand to <code>VAR 0</code> or <code>VAR 1</code> rather than being assigned the value <code>...</code>. Therefore, input lines of the form </p>
<pre><code>#cmakedefine01 VAR
</code></pre>
<p>will be replaced with either </p>
<pre><code>#define VAR 0
</code></pre>
<p>or </p>
<pre><code>#define VAR 1
</code></pre>
<p>Input lines of the form <code>#cmakedefine01 VAR ...</code> will expand as <code>#cmakedefine01 VAR ... 0</code> or <code>#cmakedefine01 VAR ... 0</code>, which may lead to undefined behavior. </p>
<p>New in version 3.10: The result lines (with the exception of the <code>#undef</code> comments) can be indented using spaces and/or tabs between the <code>#</code> character and the <code>cmakedefine</code> or <code>cmakedefine01</code> words. This whitespace indentation will be preserved in the output lines: </p>
<pre><code># cmakedefine VAR
# cmakedefine01 VAR
</code></pre>
<p>will be replaced, if <code>VAR</code> is defined, with </p>
<pre><code># define VAR
# define VAR 1
</code></pre>
<p>If the input file is modified the build system will re-run CMake to re-configure the file and generate the build system again. The generated file is modified and its timestamp updated on subsequent cmake runs only if its content is changed. </p>
<p>The arguments are: </p>
<dl>
<dt><code>&lt;input&gt;</code></dt>
<dd> <p> Path to the input file. A relative path is treated with respect to the value of <code>CMAKE_CURRENT_SOURCE_DIR</code>. The input path must be a file, not a directory. </p>
 </dd>
<dt><code>&lt;output&gt;</code></dt>
<dd> <p> Path to the output file or directory. A relative path is treated with respect to the value of <code>CMAKE_CURRENT_BINARY_DIR</code>. If the path names an existing directory the output file is placed in that directory with the same file name as the input file. If the path contains non-existent directories, they are created. </p>
 </dd>
<dt><code>NO_SOURCE_PERMISSIONS</code></dt>
<dd> <p> New in version 3.19. </p>
<p>Do not transfer the permissions of the input file to the output file. The copied file permissions default to the standard 644 value (-rw-r--r--). </p>
 </dd>
<dt><code>USE_SOURCE_PERMISSIONS</code></dt>
<dd> <p> New in version 3.20. </p>
<p>Transfer the permissions of the input file to the output file. This is already the default behavior if none of the three permissions-related keywords are given (<code>NO_SOURCE_PERMISSIONS</code>, <code>USE_SOURCE_PERMISSIONS</code> or <code>FILE_PERMISSIONS</code>). The <code>USE_SOURCE_PERMISSIONS</code> keyword mostly serves as a way of making the intended behavior clearer at the call site. </p>
 </dd>
<dt><code>FILE_PERMISSIONS &lt;permissions&gt;...</code></dt>
<dd> <p> New in version 3.20. </p>
<p>Ignore the input file&#8217;s permissions and use the specified <code>&lt;permissions&gt;</code> for the output file instead. </p>
 </dd>
<dt><code>COPYONLY</code></dt>
<dd> <p> Copy the file without replacing any variable references or other content. This option may not be used with <code>NEWLINE_STYLE</code>. </p>
 </dd>
<dt><code>ESCAPE_QUOTES</code></dt>
<dd> <p> Escape any substituted quotes with backslashes (C-style). </p>
 </dd>
<dt><code>@ONLY</code></dt>
<dd> <p> Restrict variable replacement to references of the form <code>@VAR@</code>. This is useful for configuring scripts that use <code>${VAR}</code> syntax. </p>
 </dd>
<dt><code>NEWLINE_STYLE &lt;style&gt;</code></dt>
<dd> <p> Specify the newline style for the output file. Specify <code>UNIX</code> or <code>LF</code> for <code>\n</code> newlines, or specify <code>DOS</code>, <code>WIN32</code>, or <code>CRLF</code> for <code>\r\n</code> newlines. This option may not be used with <code>COPYONLY</code>. </p>
 </dd></dl>
<h3>Example</h3>
<p>Consider a source tree containing a <code>foo.h.in</code> file: </p>
<pre><code>#cmakedefine FOO_ENABLE
#cmakedefine FOO_STRING &quot;@FOO_STRING@&quot;
</code></pre>
<p>An adjacent <code>CMakeLists.txt</code> may use <code>configure_file</code> to configure the header: </p>
<pre><code>option(FOO_ENABLE &quot;Enable Foo&quot; ON)
if(FOO_ENABLE)
  set(FOO_STRING &quot;foo&quot;)
endif()
configure_file(foo.h.in foo.h @ONLY)
</code></pre>
<p>This creates a <code>foo.h</code> in the build directory corresponding to this source directory. If the <code>FOO_ENABLE</code> option is on, the configured file will contain: </p>
<pre><code>#define FOO_ENABLE
#define FOO_STRING &quot;foo&quot;
</code></pre>
<p>Otherwise it will contain: </p>
<pre><code>/* #undef FOO_ENABLE */
/* #undef FOO_STRING */
</code></pre>
<p>One may then use the <code>include_directories()</code> command to specify the output directory as an include directory: </p>
<pre><code>include_directories(${CMAKE_CURRENT_BINARY_DIR})
</code></pre>
<p>so that sources may include the header as <code>#include &lt;foo.h&gt;</code>.  </p>
<h3>continue</h3>
<p>New in version 3.2. </p>
<p>Continue to the top of enclosing foreach or while loop. </p>
<pre><code>continue()
</code></pre>
<p>The <code>continue</code> command allows a cmake script to abort the rest of a block in a <code>foreach()</code> or <code>while()</code> loop, and start at the top of the next iteration. </p>
<p>See also the <code>break()</code> command.  </p>
<h3>else</h3>
<p>Starts the else portion of an if block. </p>
<pre><code>else([&lt;condition&gt;])
</code></pre>
<p>See the <code>if()</code> command.  </p>
<h3>elseif</h3>
<p>Starts an elseif portion of an if block. </p>
<pre><code>elseif(&lt;condition&gt;)
</code></pre>
<p>See the <code>if()</code> command, especially for the syntax and logic of the <code>&lt;condition&gt;</code>.  </p>
<h3>endforeach</h3>
<p>Ends a list of commands in a foreach block. </p>
<pre><code>endforeach([&lt;loop_var&gt;])
</code></pre>
<p>See the <code>foreach()</code> command. </p>
<p>The optional <code>&lt;loop_var&gt;</code> argument is supported for backward compatibility only. If used it must be a verbatim repeat of the <code>&lt;loop_var&gt;</code> argument of the opening <code>foreach</code> clause.  </p>
<h3>endfunction</h3>
<p>Ends a list of commands in a function block. </p>
<pre><code>endfunction([&lt;name&gt;])
</code></pre>
<p>See the <code>function()</code> command. </p>
<p>The optional <code>&lt;name&gt;</code> argument is supported for backward compatibility only. If used it must be a verbatim repeat of the <code>&lt;name&gt;</code> argument of the opening <code>function</code> command.  </p>
<h3>endif</h3>
<p>Ends a list of commands in an if block. </p>
<pre><code>endif([&lt;condition&gt;])
</code></pre>
<p>See the <code>if()</code> command. </p>
<p>The optional <code>&lt;condition&gt;</code> argument is supported for backward compatibility only. If used it must be a verbatim repeat of the argument of the opening <code>if</code> clause.  </p>
<h3>endmacro</h3>
<p>Ends a list of commands in a macro block. </p>
<pre><code>endmacro([&lt;name&gt;])
</code></pre>
<p>See the <code>macro()</code> command. </p>
<p>The optional <code>&lt;name&gt;</code> argument is supported for backward compatibility only. If used it must be a verbatim repeat of the <code>&lt;name&gt;</code> argument of the opening <code>macro</code> command.  </p>
<h3>endwhile</h3>
<p>Ends a list of commands in a while block. </p>
<pre><code>endwhile([&lt;condition&gt;])
</code></pre>
<p>See the <code>while()</code> command. </p>
<p>The optional <code>&lt;condition&gt;</code> argument is supported for backward compatibility only. If used it must be a verbatim repeat of the argument of the opening <code>while</code> clause.  </p>
<h3>execute_process</h3>
<p>Execute one or more child processes. </p>
<pre><code>execute_process(COMMAND &lt;cmd1&gt; [&lt;arguments&gt;]
                [COMMAND &lt;cmd2&gt; [&lt;arguments&gt;]]...
                [WORKING_DIRECTORY &lt;directory&gt;]
                [TIMEOUT &lt;seconds&gt;]
                [RESULT_VARIABLE &lt;variable&gt;]
                [RESULTS_VARIABLE &lt;variable&gt;]
                [OUTPUT_VARIABLE &lt;variable&gt;]
                [ERROR_VARIABLE &lt;variable&gt;]
                [INPUT_FILE &lt;file&gt;]
                [OUTPUT_FILE &lt;file&gt;]
                [ERROR_FILE &lt;file&gt;]
                [OUTPUT_QUIET]
                [ERROR_QUIET]
                [COMMAND_ECHO &lt;where&gt;]
                [OUTPUT_STRIP_TRAILING_WHITESPACE]
                [ERROR_STRIP_TRAILING_WHITESPACE]
                [ENCODING &lt;name&gt;]
                [ECHO_OUTPUT_VARIABLE]
                [ECHO_ERROR_VARIABLE]
                [COMMAND_ERROR_IS_FATAL &lt;ANY|LAST&gt;])
</code></pre>
<p>Runs the given sequence of one or more commands. </p>
<p>Commands are executed concurrently as a pipeline, with the standard output of each process piped to the standard input of the next. A single standard error pipe is used for all processes. </p>
<p>Options: </p>
<dl>
<dt><code>COMMAND</code></dt>
<dd> <p> A child process command line. </p>
<p>CMake executes the child process using operating system APIs directly. All arguments are passed VERBATIM to the child process. No intermediate shell is used, so shell operators such as <code>&gt;</code> are treated as normal arguments. (Use the <code>INPUT_*</code>, <code>OUTPUT_*</code>, and <code>ERROR_*</code> options to redirect stdin, stdout, and stderr.) </p>
<p>If a sequential execution of multiple commands is required, use multiple <i>execute_process()</i> calls with a single <code>COMMAND</code> argument. </p>
 </dd>
<dt><code>WORKING_DIRECTORY</code></dt>
<dd> <p> The named directory will be set as the current working directory of the child processes. </p>
 </dd>
<dt><code>TIMEOUT</code></dt>
<dd> <p> After the specified number of seconds (fractions allowed), all unfinished child processes will be terminated, and the <code>RESULT_VARIABLE</code> will be set to a string mentioning the &quot;timeout&quot;. </p>
 </dd>
<dt><code>RESULT_VARIABLE</code></dt>
<dd> <p> The variable will be set to contain the result of last child process. This will be an integer return code from the last child or a string describing an error condition. </p>
 </dd>
<dt><code>RESULTS_VARIABLE &lt;variable&gt;</code></dt>
<dd> <p> New in version 3.10. </p>
<p>The variable will be set to contain the result of all processes as a semicolon-separated list, in order of the given <code>COMMAND</code> arguments. Each entry will be an integer return code from the corresponding child or a string describing an error condition. </p>
 </dd>
<dt><code>OUTPUT_VARIABLE</code>, <code>ERROR_VARIABLE</code></dt>
<dd> <p> The variable named will be set with the contents of the standard output and standard error pipes, respectively. If the same variable is named for both pipes their output will be merged in the order produced. </p>
 </dd>
<dt><code>INPUT_FILE, OUTPUT_FILE</code>, <code>ERROR_FILE</code></dt>
<dd> <p> The file named will be attached to the standard input of the first process, standard output of the last process, or standard error of all processes, respectively. </p>
<p>New in version 3.3: If the same file is named for both output and error then it will be used for both. </p>
 </dd>
<dt><code>OUTPUT_QUIET</code>, <code>ERROR_QUIET</code></dt>
<dd> <p> The standard output or standard error results will be quietly ignored. </p>
 </dd>
<dt><code>COMMAND_ECHO &lt;where&gt;</code></dt>
<dd> <p> New in version 3.15. </p>
<p>The command being run will be echo&#8217;ed to <code>&lt;where&gt;</code> with <code>&lt;where&gt;</code> being set to one of <code>STDERR</code>, <code>STDOUT</code> or <code>NONE</code>. See the <code>CMAKE_EXECUTE_PROCESS_COMMAND_ECHO</code> variable for a way to control the default behavior when this option is not present. </p>
 </dd>
<dt><code>ENCODING &lt;name&gt;</code></dt>
<dd> <p> New in version 3.8. </p>
<p>On Windows, the encoding that is used to decode output from the process. Ignored on other platforms. Valid encoding names are: </p>
 </dd>
<dt><code>NONE</code></dt>
<dd> <p> Perform no decoding. This assumes that the process output is encoded in the same way as CMake&#8217;s internal encoding (UTF-8). This is the default. </p>
 </dd>
<dt><code>AUTO</code></dt>
<dd> <p> Use the current active console&#8217;s codepage or if that isn&#8217;t available then use ANSI. </p>
 </dd>
<dt><code>ANSI</code></dt>
<dd> <p> Use the ANSI codepage. </p>
 </dd>
<dt><code>OEM</code></dt>
<dd> <p> Use the original equipment manufacturer (OEM) code page. </p>
 </dd>
<dt><code>UTF8</code> or <code>UTF-8</code></dt>
<dd> <p> Use the UTF-8 codepage. </p>
<p>New in version 3.11: Accept <code>UTF-8</code> spelling for consistency with the <i>UTF-8 RFC</i> naming convention. </p>
 </dd>
<dt><code>ECHO_OUTPUT_VARIABLE</code>, <code>ECHO_ERROR_VARIABLE</code></dt>
<dd> <p> New in version 3.18. </p>
<p>The standard output or standard error will not be exclusively redirected to the configured variables. </p>
<p>The output will be duplicated, it will be sent into the configured variables and also on standard output or standard error. </p>
<p>This is analogous to the <code>tee</code> Unix command. </p>
 </dd>
<dt><code>COMMAND_ERROR_IS_FATAL &lt;ANY|LAST&gt;</code></dt>
<dd> <p> New in version 3.19. </p>
<p>The option following <code>COMMAND_ERROR_IS_FATAL</code> determines the behavior when an error is encountered: <code>ANY</code> If any of the commands in the list of commands fail, the <code>execute_process()</code> command halts with an error. </p>
<p> <code>LAST</code> If the last command in the list of commands fails, the <code>execute_process()</code> command halts with an error. Commands earlier in the list will not cause a fatal error. </p>
<p>If more than one <code>OUTPUT_*</code> or <code>ERROR_*</code> option is given for the same pipe the precedence is not specified. If no <code>OUTPUT_*</code> or <code>ERROR_*</code> options are given the output will be shared with the corresponding pipes of the CMake process itself. </p>
<p>The <i>execute_process()</i> command is a newer more powerful version of <code>exec_program()</code>, but the old command has been kept for compatibility. Both commands run while CMake is processing the project prior to build system generation. Use <code>add_custom_target()</code> and <code>add_custom_command()</code> to create custom commands that run at build time. </p>
 </dd></dl>
<h3>file</h3>
<p>File manipulation command. </p>
<p>This command is dedicated to file and path manipulation requiring access to the filesystem. </p>
<p>For other path manipulation, handling only syntactic aspects, have a look at <code>cmake_path()</code> command. </p>
<p> <code>NOTE:</code> The sub-commands <i>RELATIVE_PATH</i>, <i>TO_CMAKE_PATH</i> and <i>TO_NATIVE_PATH</i> has been superseded, respectively, by sub-commands RELATIVE_PATH, CONVERT ... TO_CMAKE_PATH_LIST and CONVERT ... TO_NATIVE_PATH_LIST of <code>cmake_path()</code> command.  </p>
<h3>Synopsis</h3>
<pre><code>
 Reading   file( READ  &lt;filename&gt; &lt;out-var&gt; [...])
  file( STRINGS  &lt;filename&gt; &lt;out-var&gt; [...])
  file( &lt;HASH&gt;  &lt;filename&gt; &lt;out-var&gt;)
  file( TIMESTAMP  &lt;filename&gt; &lt;out-var&gt; [...])
  file( GET_RUNTIME_DEPENDENCIES  [...])
 Writing   file({ WRITE  | APPEND } &lt;filename&gt; &lt;content&gt;...)
  file({ TOUCH  | TOUCH_NOCREATE } [&lt;file&gt;...])
  file( GENERATE  OUTPUT &lt;output-file&gt; [...])
  file( CONFIGURE  OUTPUT &lt;output-file&gt; CONTENT &lt;content&gt; [...])
 Filesystem   file({ GLOB  | GLOB_RECURSE } &lt;out-var&gt; [...] [&lt;globbing-expr&gt;...])
  file( MAKE_DIRECTORY  [&lt;dir&gt;...])
  file({ REMOVE  | REMOVE_RECURSE  } [&lt;files&gt;...])
  file( RENAME  &lt;oldname&gt; &lt;newname&gt; [...])
  file( COPY_FILE  &lt;oldname&gt; &lt;newname&gt; [...])
  file({ COPY  | INSTALL } &lt;file&gt;... DESTINATION &lt;dir&gt; [...])
  file( SIZE  &lt;filename&gt; &lt;out-var&gt;)
  file( READ_SYMLINK  &lt;linkname&gt; &lt;out-var&gt;)
  file( CREATE_LINK  &lt;original&gt; &lt;linkname&gt; [...])
  file( CHMOD  &lt;files&gt;... &lt;directories&gt;... PERMISSIONS &lt;permissions&gt;... [...])
  file( CHMOD_RECURSE  &lt;files&gt;... &lt;directories&gt;... PERMISSIONS &lt;permissions&gt;... [...])
 Path Conversion   file( REAL_PATH  &lt;path&gt; &lt;out-var&gt; [BASE_DIRECTORY &lt;dir&gt;] [EXPAND_TILDE])
  file( RELATIVE_PATH  &lt;out-var&gt; &lt;directory&gt; &lt;file&gt;)
  file({ TO_CMAKE_PATH  | TO_NATIVE_PATH } &lt;path&gt; &lt;out-var&gt;)
 Transfer   file( DOWNLOAD  &lt;url&gt; [&lt;file&gt;] [...])
  file( UPLOAD  &lt;file&gt; &lt;url&gt; [...])
 Locking   file( LOCK  &lt;path&gt; [...])
 Archiving   file( ARCHIVE_CREATE  OUTPUT &lt;archive&gt; PATHS &lt;paths&gt;... [...])
  file( ARCHIVE_EXTRACT  INPUT &lt;archive&gt; [...])
</code></pre>
<h3>Reading</h3>
<pre><code>file(READ &lt;filename&gt; &lt;variable&gt;
     [OFFSET &lt;offset&gt;] [LIMIT &lt;max-in&gt;] [HEX])
</code></pre>
<p>Read content from a file called <code>&lt;filename&gt;</code> and store it in a <code>&lt;variable&gt;</code>. Optionally start from the given <code>&lt;offset&gt;</code> and read at most <code>&lt;max-in&gt;</code> bytes. The <code>HEX</code> option causes data to be converted to a hexadecimal representation (useful for binary data). If the <code>HEX</code> option is specified, letters in the output (<code>a</code> through <code>f</code>) are in lowercase. </p>
<pre><code>file(STRINGS &lt;filename&gt; &lt;variable&gt; [&lt;options&gt;...])
</code></pre>
<p>Parse a list of ASCII strings from <code>&lt;filename&gt;</code> and store it in <code>&lt;variable&gt;</code>. Binary data in the file are ignored. Carriage return (<code>\r</code>, CR) characters are ignored. The options are: </p>
<dl>
<dt><code>LENGTH_MAXIMUM &lt;max-len&gt;</code></dt>
<dd> <p> Consider only strings of at most a given length. </p>
 </dd>
<dt><code>LENGTH_MINIMUM &lt;min-len&gt;</code></dt>
<dd> <p> Consider only strings of at least a given length. </p>
 </dd>
<dt><code>LIMIT_COUNT &lt;max-num&gt;</code></dt>
<dd> <p> Limit the number of distinct strings to be extracted. </p>
 </dd>
<dt><code>LIMIT_INPUT &lt;max-in&gt;</code></dt>
<dd> <p> Limit the number of input bytes to read from the file. </p>
 </dd>
<dt><code>LIMIT_OUTPUT &lt;max-out&gt;</code></dt>
<dd> <p> Limit the number of total bytes to store in the <code>&lt;variable&gt;</code>. </p>
 </dd>
<dt><code>NEWLINE_CONSUME</code></dt>
<dd> <p> Treat newline characters (<code>\n</code>, LF) as part of string content instead of terminating at them. </p>
 </dd>
<dt><code>NO_HEX_CONVERSION</code></dt>
<dd> <p> Intel Hex and Motorola S-record files are automatically converted to binary while reading unless this option is given. </p>
 </dd>
<dt><code>REGEX &lt;regex&gt;</code></dt>
<dd> <p> Consider only strings that match the given regular expression, as described under string(REGEX). </p>
 </dd>
<dt><code>ENCODING &lt;encoding-type&gt;</code></dt>
<dd> <p> New in version 3.1. </p>
<p>Consider strings of a given encoding. Currently supported encodings are: <code>UTF-8</code>, <code>UTF-16LE</code>, <code>UTF-16BE</code>, <code>UTF-32LE</code>, <code>UTF-32BE</code>. If the <code>ENCODING</code> option is not provided and the file has a Byte Order Mark, the <code>ENCODING</code> option will be defaulted to respect the Byte Order Mark. </p>
<p>New in version 3.2: Added the <code>UTF-16LE</code>, <code>UTF-16BE</code>, <code>UTF-32LE</code>, <code>UTF-32BE</code> encodings. </p>
<p>For example, the code </p>
<pre><code>file(STRINGS myfile.txt myfile)
</code></pre>
<p>stores a list in the variable <code>myfile</code> in which each item is a line from the input file. </p>
<pre><code>file(&lt;HASH&gt; &lt;filename&gt; &lt;variable&gt;)
</code></pre>
<p>Compute a cryptographic hash of the content of <code>&lt;filename&gt;</code> and store it in a <code>&lt;variable&gt;</code>. The supported <code>&lt;HASH&gt;</code> algorithm names are those listed by the string(&lt;HASH&gt;) command. </p>
<pre><code>file(TIMESTAMP &lt;filename&gt; &lt;variable&gt; [&lt;format&gt;] [UTC])
</code></pre>
<p>Compute a string representation of the modification time of <code>&lt;filename&gt;</code> and store it in <code>&lt;variable&gt;</code>. Should the command be unable to obtain a timestamp variable will be set to the empty string (&quot;&quot;). </p>
<p>See the <code>string(TIMESTAMP)</code> command for documentation of the <code>&lt;format&gt;</code> and <code>UTC</code> options. </p>
<pre><code>file(GET_RUNTIME_DEPENDENCIES
  [RESOLVED_DEPENDENCIES_VAR &lt;deps_var&gt;]
  [UNRESOLVED_DEPENDENCIES_VAR &lt;unresolved_deps_var&gt;]
  [CONFLICTING_DEPENDENCIES_PREFIX &lt;conflicting_deps_prefix&gt;]
  [EXECUTABLES [&lt;executable_files&gt;...]]
  [LIBRARIES [&lt;library_files&gt;...]]
  [MODULES [&lt;module_files&gt;...]]
  [DIRECTORIES [&lt;directories&gt;...]]
  [BUNDLE_EXECUTABLE &lt;bundle_executable_file&gt;]
  [PRE_INCLUDE_REGEXES [&lt;regexes&gt;...]]
  [PRE_EXCLUDE_REGEXES [&lt;regexes&gt;...]]
  [POST_INCLUDE_REGEXES [&lt;regexes&gt;...]]
  [POST_EXCLUDE_REGEXES [&lt;regexes&gt;...]]
  [POST_INCLUDE_FILES [&lt;files&gt;...]]
  [POST_EXCLUDE_FILES [&lt;files&gt;...]]
  )
</code></pre>
<p>New in version 3.16. </p>
<p>Recursively get the list of libraries depended on by the given files. </p>
<p>Please note that this sub-command is not intended to be used in project mode. It is intended for use at install time, either from code generated by the <code>install(RUNTIME_DEPENDENCY_SET)</code> command, or from code provided by the project via <code>install(CODE)</code> or <code>install(SCRIPT)</code>. For example: </p>
<pre><code>install(CODE [[
  file(GET_RUNTIME_DEPENDENCIES
    # ...
    )
  ]])
</code></pre>
<p>The arguments are as follows: </p>
 </dd>
<dt><code>RESOLVED_DEPENDENCIES_VAR &lt;deps_var&gt;</code></dt>
<dd> <p> Name of the variable in which to store the list of resolved dependencies. </p>
 </dd>
<dt><code>UNRESOLVED_DEPENDENCIES_VAR &lt;unresolved_deps_var&gt;</code></dt>
<dd> <p> Name of the variable in which to store the list of unresolved dependencies. If this variable is not specified, and there are any unresolved dependencies, an error is issued. </p>
 </dd>
<dt><code>CONFLICTING_DEPENDENCIES_PREFIX &lt;conflicting_deps_prefix&gt;</code></dt>
<dd> <p> Variable prefix in which to store conflicting dependency information. Dependencies are conflicting if two files with the same name are found in two different directories. The list of filenames that conflict are stored in <code>&lt;conflicting_deps_prefix&gt;_FILENAMES</code>. For each filename, the list of paths that were found for that filename are stored in <code>&lt;conflicting_deps_prefix&gt;_&lt;filename&gt;</code>. </p>
 </dd>
<dt><code>EXECUTABLES &lt;executable_files&gt;</code></dt>
<dd> <p> List of executable files to read for dependencies. These are executables that are typically created with <code>add_executable()</code>, but they do not have to be created by CMake. On Apple platforms, the paths to these files determine the value of <code>@executable_path</code> when recursively resolving the libraries. Specifying any kind of library (<code>STATIC</code>, <code>MODULE</code>, or <code>SHARED</code>) here will result in undefined behavior. </p>
 </dd>
<dt><code>LIBRARIES &lt;library_files&gt;</code></dt>
<dd> <p> List of library files to read for dependencies. These are libraries that are typically created with <code>add_library(SHARED)</code>, but they do not have to be created by CMake. Specifying <code>STATIC</code> libraries, <code>MODULE</code> libraries, or executables here will result in undefined behavior. </p>
 </dd>
<dt><code>MODULES &lt;module_files&gt;</code></dt>
<dd> <p> List of loadable module files to read for dependencies. These are modules that are typically created with <code>add_library(MODULE)</code>, but they do not have to be created by CMake. They are typically used by calling <code>dlopen()</code> at runtime rather than linked at link time with <code>ld -l</code>. Specifying <code>STATIC</code> libraries, <code>SHARED</code> libraries, or executables here will result in undefined behavior. </p>
 </dd>
<dt><code>DIRECTORIES &lt;directories&gt;</code></dt>
<dd> <p> List of additional directories to search for dependencies. On Linux platforms, these directories are searched if the dependency is not found in any of the other usual paths. If it is found in such a directory, a warning is issued, because it means that the file is incomplete (it does not list all of the directories that contain its dependencies). On Windows platforms, these directories are searched if the dependency is not found in any of the other search paths, but no warning is issued, because searching other paths is a normal part of Windows dependency resolution. On Apple platforms, this argument has no effect. </p>
 </dd>
<dt><code>BUNDLE_EXECUTABLE &lt;bundle_executable_file&gt;</code></dt>
<dd> <p> Executable to treat as the &quot;bundle executable&quot; when resolving libraries. On Apple platforms, this argument determines the value of <code>@executable_path</code> when recursively resolving libraries for <code>LIBRARIES</code> and <code>MODULES</code> files. It has no effect on <code>EXECUTABLES</code> files. On other platforms, it has no effect. This is typically (but not always) one of the executables in the <code>EXECUTABLES</code> argument which designates the &quot;main&quot; executable of the package. </p>
<p>The following arguments specify filters for including or excluding libraries to be resolved. See below for a full description of how they work. </p>
 </dd>
<dt><code>PRE_INCLUDE_REGEXES &lt;regexes&gt;</code></dt>
<dd> <p> List of pre-include regexes through which to filter the names of not-yet-resolved dependencies. </p>
 </dd>
<dt><code>PRE_EXCLUDE_REGEXES &lt;regexes&gt;</code></dt>
<dd> <p> List of pre-exclude regexes through which to filter the names of not-yet-resolved dependencies. </p>
 </dd>
<dt><code>POST_INCLUDE_REGEXES &lt;regexes&gt;</code></dt>
<dd> <p> List of post-include regexes through which to filter the names of resolved dependencies. </p>
 </dd>
<dt><code>POST_EXCLUDE_REGEXES &lt;regexes&gt;</code></dt>
<dd> <p> List of post-exclude regexes through which to filter the names of resolved dependencies. </p>
 </dd>
<dt><code>POST_INCLUDE_FILES &lt;files&gt;</code></dt>
<dd> <p> New in version 3.21. </p>
<p>List of post-include filenames through which to filter the names of resolved dependencies. Symlinks are resolved when attempting to match these filenames. </p>
 </dd>
<dt><code>POST_EXCLUDE_FILES &lt;files&gt;</code></dt>
<dd> <p> New in version 3.21. </p>
<p>List of post-exclude filenames through which to filter the names of resolved dependencies. Symlinks are resolved when attempting to match these filenames. </p>
<p>These arguments can be used to exclude unwanted system libraries when resolving the dependencies, or to include libraries from a specific directory. The filtering works as follows: </p>
 </dd>
<dt>1.</dt>
<dd> <p> If the not-yet-resolved dependency matches any of the <code>PRE_INCLUDE_REGEXES</code>, steps 2 and 3 are skipped, and the dependency resolution proceeds to step 4. </p>
 </dd>
<dt>2.</dt>
<dd> <p> If the not-yet-resolved dependency matches any of the <code>PRE_EXCLUDE_REGEXES</code>, dependency resolution stops for that dependency. </p>
 </dd>
<dt>3.</dt>
<dd> <p> Otherwise, dependency resolution proceeds. </p>
 </dd>
<dt>4.</dt>
<dd> <p> <code>file(GET_RUNTIME_DEPENDENCIES)</code> searches for the dependency according to the linking rules of the platform (see below). </p>
 </dd>
<dt>5.</dt>
<dd> <p> If the dependency is found, and its full path matches one of the <code>POST_INCLUDE_REGEXES</code> or <code>POST_INCLUDE_FILES</code>, the full path is added to the resolved dependencies, and <code>file(GET_RUNTIME_DEPENDENCIES)</code> recursively resolves that library&#8217;s own dependencies. Otherwise, resolution proceeds to step 6. </p>
 </dd>
<dt>6.</dt>
<dd> <p> If the dependency is found, but its full path matches one of the <code>POST_EXCLUDE_REGEXES</code> or <code>POST_EXCLUDE_FILES</code>, it is not added to the resolved dependencies, and dependency resolution stops for that dependency. </p>
 </dd>
<dt>7.</dt>
<dd> <p> If the dependency is found, and its full path does not match either <code>POST_INCLUDE_REGEXES</code>, <code>POST_INCLUDE_FILES</code>, <code>POST_EXCLUDE_REGEXES</code>, or <code>POST_EXCLUDE_FILES</code>, the full path is added to the resolved dependencies, and <code>file(GET_RUNTIME_DEPENDENCIES)</code> recursively resolves that library&#8217;s own dependencies. </p>
<p>Different platforms have different rules for how dependencies are resolved. These specifics are described here. </p>
<p>On Linux platforms, library resolution works as follows: </p>
 </dd>
<dt>1.</dt>
<dd> <p> If the depending file does not have any <code>RUNPATH</code> entries, and the library exists in one of the depending file&#8217;s <code>RPATH</code> entries, or its parents&#8217;, in that order, the dependency is resolved to that file. </p>
 </dd>
<dt>2.</dt>
<dd> <p> Otherwise, if the depending file has any <code>RUNPATH</code> entries, and the library exists in one of those entries, the dependency is resolved to that file. </p>
 </dd>
<dt>3.</dt>
<dd> <p> Otherwise, if the library exists in one of the directories listed by <code>ldconfig</code>, the dependency is resolved to that file. </p>
 </dd>
<dt>4.</dt>
<dd> <p> Otherwise, if the library exists in one of the <code>DIRECTORIES</code> entries, the dependency is resolved to that file. In this case, a warning is issued, because finding a file in one of the <code>DIRECTORIES</code> means that the depending file is not complete (it does not list all the directories from which it pulls dependencies). </p>
 </dd>
<dt>5.</dt>
<dd> <p> Otherwise, the dependency is unresolved. </p>
<p>On Windows platforms, library resolution works as follows: </p>
 </dd>
<dt>1.</dt>
<dd> <p> The dependent DLL name is converted to lowercase. Windows DLL names are case-insensitive, and some linkers mangle the case of the DLL dependency names. However, this makes it more difficult for <code>PRE_INCLUDE_REGEXES</code>, <code>PRE_EXCLUDE_REGEXES</code>, <code>POST_INCLUDE_REGEXES</code>, and <code>POST_EXCLUDE_REGEXES</code> to properly filter DLL names - every regex would have to check for both uppercase and lowercase letters. For example: </p>
<pre><code>file(GET_RUNTIME_DEPENDENCIES
  # ...
  PRE_INCLUDE_REGEXES &quot;^[Mm][Yy][Ll][Ii][Bb][Rr][Aa][Rr][Yy]\\.[Dd][Ll][Ll]$&quot;
  )
</code></pre>
<p>Converting the DLL name to lowercase allows the regexes to only match lowercase names, thus simplifying the regex. For example: </p>
<pre><code>file(GET_RUNTIME_DEPENDENCIES
  # ...
  PRE_INCLUDE_REGEXES &quot;^mylibrary\\.dll$&quot;
  )
</code></pre>
<p>This regex will match <code>mylibrary.dll</code> regardless of how it is cased, either on disk or in the depending file. (For example, it will match <code>mylibrary.dll</code>, <code>MyLibrary.dll</code>, and <code>MYLIBRARY.DLL</code>.) </p>
<p>Please note that the directory portion of any resolved DLLs retains its casing and is not converted to lowercase. Only the filename portion is converted. </p>
 </dd>
<dt>2.</dt>
<dd> <p> (<code>Not yet implemented</code>) If the depending file is a Windows Store app, and the dependency is listed as a dependency in the application&#8217;s package manifest, the dependency is resolved to that file. </p>
 </dd>
<dt>3.</dt>
<dd> <p> Otherwise, if the library exists in the same directory as the depending file, the dependency is resolved to that file. </p>
 </dd>
<dt>4.</dt>
<dd> <p> Otherwise, if the library exists in either the operating system&#8217;s <code>system32</code> directory or the <code>Windows</code> directory, in that order, the dependency is resolved to that file. </p>
 </dd>
<dt>5.</dt>
<dd> <p> Otherwise, if the library exists in one of the directories specified by <code>DIRECTORIES</code>, in the order they are listed, the dependency is resolved to that file. In this case, a warning is not issued, because searching other directories is a normal part of Windows library resolution. </p>
 </dd>
<dt>6.</dt>
<dd> <p> Otherwise, the dependency is unresolved. </p>
<p>On Apple platforms, library resolution works as follows: </p>
 </dd>
<dt>1.</dt>
<dd> <p> If the dependency starts with <code>@executable_path/</code>, and an <code>EXECUTABLES</code> argument is in the process of being resolved, and replacing <code>@executable_path/</code> with the directory of the executable yields an existing file, the dependency is resolved to that file. </p>
 </dd>
<dt>2.</dt>
<dd> <p> Otherwise, if the dependency starts with <code>@executable_path/</code>, and there is a <code>BUNDLE_EXECUTABLE</code> argument, and replacing <code>@executable_path/</code> with the directory of the bundle executable yields an existing file, the dependency is resolved to that file. </p>
 </dd>
<dt>3.</dt>
<dd> <p> Otherwise, if the dependency starts with <code>@loader_path/</code>, and replacing <code>@loader_path/</code> with the directory of the depending file yields an existing file, the dependency is resolved to that file. </p>
 </dd>
<dt>4.</dt>
<dd> <p> Otherwise, if the dependency starts with <code>@rpath/</code>, and replacing <code>@rpath/</code> with one of the <code>RPATH</code> entries of the depending file yields an existing file, the dependency is resolved to that file. Note that <code>RPATH</code> entries that start with <code>@executable_path/</code> or <code>@loader_path/</code> also have these items replaced with the appropriate path. </p>
 </dd>
<dt>5.</dt>
<dd> <p> Otherwise, if the dependency is an absolute file that exists, the dependency is resolved to that file. </p>
 </dd>
<dt>6.</dt>
<dd> <p> Otherwise, the dependency is unresolved. </p>
<p>This function accepts several variables that determine which tool is used for dependency resolution: </p>
 </dd>
<dt><code>CMAKE_GET_RUNTIME_DEPENDENCIES_PLATFORM</code></dt>
<dd> <p> Determines which operating system and executable format the files are built for. This could be one of several values: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>linux+elf</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>windows+pe</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>macos+macho</code> </p>
<p>If this variable is not specified, it is determined automatically by system introspection. </p>
 </dd>
<dt><code>CMAKE_GET_RUNTIME_DEPENDENCIES_TOOL</code></dt>
<dd> <p> Determines the tool to use for dependency resolution. It could be one of several values, depending on the value of <i>CMAKE_GET_RUNTIME_DEPENDENCIES_PLATFORM</i>: <center> </p>
<table>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>CMAKE_GET_RUNTIME_DEPENDENCIES_PLATFORM</code> </td>
<td> <code>CMAKE_GET_RUNTIME_DEPENDENCIES_TOOL</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>linux+elf</code> </td>
<td> <code>objdump</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>windows+pe</code> </td>
<td> <code>dumpbin</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>windows+pe</code> </td>
<td> <code>objdump</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>macos+macho</code> </td>
<td> <code>otool</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
</table>
<p> </center> </p>
<p>If this variable is not specified, it is determined automatically by system introspection. </p>
 </dd>
<dt><code>CMAKE_GET_RUNTIME_DEPENDENCIES_COMMAND</code></dt>
<dd> <p> Determines the path to the tool to use for dependency resolution. This is the actual path to <code>objdump</code>, <code>dumpbin</code>, or <code>otool</code>. </p>
<p>If this variable is not specified, it is determined by the value of <code>CMAKE_OBJDUMP</code> if set, else by system introspection. </p>
<p>New in version 3.18: Use <code>CMAKE_OBJDUMP</code> if set. </p>
 </dd></dl>
<h3>Writing</h3>
<pre><code>file(WRITE &lt;filename&gt; &lt;content&gt;...)
file(APPEND &lt;filename&gt; &lt;content&gt;...)
</code></pre>
<p>Write <code>&lt;content&gt;</code> into a file called <code>&lt;filename&gt;</code>. If the file does not exist, it will be created. If the file already exists, <code>WRITE</code> mode will overwrite it and <code>APPEND</code> mode will append to the end. Any directories in the path specified by <code>&lt;filename&gt;</code> that do not exist will be created. </p>
<p>If the file is a build input, use the <code>configure_file()</code> command to update the file only when its content changes. </p>
<pre><code>file(TOUCH [&lt;files&gt;...])
file(TOUCH_NOCREATE [&lt;files&gt;...])
</code></pre>
<p>New in version 3.12. </p>
<p>Create a file with no content if it does not yet exist. If the file already exists, its access and/or modification will be updated to the time when the function call is executed. </p>
<p>Use TOUCH_NOCREATE to touch a file if it exists but not create it. If a file does not exist it will be silently ignored. </p>
<p>With TOUCH and TOUCH_NOCREATE the contents of an existing file will not be modified. </p>
<pre><code>file(GENERATE OUTPUT output-file
     &lt;INPUT input-file|CONTENT content&gt;
     [CONDITION expression] [TARGET target]
     [NO_SOURCE_PERMISSIONS | USE_SOURCE_PERMISSIONS |
      FILE_PERMISSIONS &lt;permissions&gt;...]
     [NEWLINE_STYLE [UNIX|DOS|WIN32|LF|CRLF] ])
</code></pre>
<p>Generate an output file for each build configuration supported by the current <code>CMake Generator</code>. Evaluate <code>generator expressions</code> from the input content to produce the output content. The options are: </p>
<dl>
<dt><code>CONDITION &lt;condition&gt;</code></dt>
<dd> <p> Generate the output file for a particular configuration only if the condition is true. The condition must be either <code>0</code> or <code>1</code> after evaluating generator expressions. </p>
 </dd>
<dt><code>CONTENT &lt;content&gt;</code></dt>
<dd> <p> Use the content given explicitly as input. </p>
 </dd>
<dt><code>INPUT &lt;input-file&gt;</code></dt>
<dd> <p> Use the content from a given file as input. </p>
<p>Changed in version 3.10: A relative path is treated with respect to the value of <code>CMAKE_CURRENT_SOURCE_DIR</code>. See policy <code>CMP0070</code>. </p>
 </dd>
<dt><code>OUTPUT &lt;output-file&gt;</code></dt>
<dd> <p> Specify the output file name to generate. Use generator expressions such as <code>$&lt;CONFIG&gt;</code> to specify a configuration-specific output file name. Multiple configurations may generate the same output file only if the generated content is identical. Otherwise, the <code>&lt;output-file&gt;</code> must evaluate to an unique name for each configuration. </p>
<p>Changed in version 3.10: A relative path (after evaluating generator expressions) is treated with respect to the value of <code>CMAKE_CURRENT_BINARY_DIR</code>. See policy <code>CMP0070</code>. </p>
 </dd>
<dt><code>TARGET &lt;target&gt;</code></dt>
<dd> <p> New in version 3.19. </p>
<p>Specify which target to use when evaluating generator expressions that require a target for evaluation (e.g. <code>$&lt;COMPILE_FEATURES:...&gt;</code>, <code>$&lt;TARGET_PROPERTY:prop&gt;</code>). </p>
 </dd>
<dt><code>NO_SOURCE_PERMISSIONS</code></dt>
<dd> <p> New in version 3.20. </p>
<p>The generated file permissions default to the standard 644 value (-rw-r--r--). </p>
 </dd>
<dt><code>USE_SOURCE_PERMISSIONS</code></dt>
<dd> <p> New in version 3.20. </p>
<p>Transfer the file permissions of the <code>INPUT</code> file to the generated file. This is already the default behavior if none of the three permissions-related keywords are given (<code>NO_SOURCE_PERMISSIONS</code>, <code>USE_SOURCE_PERMISSIONS</code> or <code>FILE_PERMISSIONS</code>). The <code>USE_SOURCE_PERMISSIONS</code> keyword mostly serves as a way of making the intended behavior clearer at the call site. It is an error to specify this option without <code>INPUT</code>. </p>
 </dd>
<dt><code>FILE_PERMISSIONS &lt;permissions&gt;...</code></dt>
<dd> <p> New in version 3.20. </p>
<p>Use the specified permissions for the generated file. </p>
 </dd>
<dt><code>NEWLINE_STYLE &lt;style&gt;</code></dt>
<dd> <p> New in version 3.20. </p>
<p>Specify the newline style for the generated file. Specify <code>UNIX</code> or <code>LF</code> for <code>\n</code> newlines, or specify <code>DOS</code>, <code>WIN32</code>, or <code>CRLF</code> for <code>\r\n</code> newlines. </p>
<p>Exactly one <code>CONTENT</code> or <code>INPUT</code> option must be given. A specific <code>OUTPUT</code> file may be named by at most one invocation of <code>file(GENERATE)</code>. Generated files are modified and their timestamp updated on subsequent cmake runs only if their content is changed. </p>
<p>Note also that <code>file(GENERATE)</code> does not create the output file until the generation phase. The output file will not yet have been written when the <code>file(GENERATE)</code> command returns, it is written only after processing all of a project&#8217;s <code>CMakeLists.txt</code> files. </p>
<pre><code>file(CONFIGURE OUTPUT output-file
     CONTENT content
     [ESCAPE_QUOTES] [@ONLY]
     [NEWLINE_STYLE [UNIX|DOS|WIN32|LF|CRLF] ])
</code></pre>
<p>New in version 3.18. </p>
<p>Generate an output file using the input given by <code>CONTENT</code> and substitute variable values referenced as <code>@VAR@</code> or <code>${VAR}</code> contained therein. The substitution rules behave the same as the <code>configure_file()</code> command. In order to match <code>configure_file()</code>&#8216;s behavior, generator expressions are not supported for both <code>OUTPUT</code> and <code>CONTENT</code>. </p>
<p>The arguments are: </p>
 </dd>
<dt><code>OUTPUT &lt;output-file&gt;</code></dt>
<dd> <p> Specify the output file name to generate. A relative path is treated with respect to the value of <code>CMAKE_CURRENT_BINARY_DIR</code>. <code>&lt;output-file&gt;</code> does not support generator expressions. </p>
 </dd>
<dt><code>CONTENT &lt;content&gt;</code></dt>
<dd> <p> Use the content given explicitly as input. <code>&lt;content&gt;</code> does not support generator expressions. </p>
 </dd>
<dt><code>ESCAPE_QUOTES</code></dt>
<dd> <p> Escape any substituted quotes with backslashes (C-style). </p>
 </dd>
<dt><code>@ONLY</code></dt>
<dd> <p> Restrict variable replacement to references of the form <code>@VAR@</code>. This is useful for configuring scripts that use <code>${VAR}</code> syntax. </p>
 </dd>
<dt><code>NEWLINE_STYLE &lt;style&gt;</code></dt>
<dd> <p> Specify the newline style for the output file. Specify <code>UNIX</code> or <code>LF</code> for <code>\n</code> newlines, or specify <code>DOS</code>, <code>WIN32</code>, or <code>CRLF</code> for <code>\r\n</code> newlines. </p>
 </dd></dl>
<h3>Filesystem</h3>
<pre><code>file(GLOB &lt;variable&gt;
     [LIST_DIRECTORIES true|false] [RELATIVE &lt;path&gt;] [CONFIGURE_DEPENDS]
     [&lt;globbing-expressions&gt;...])
file(GLOB_RECURSE &lt;variable&gt; [FOLLOW_SYMLINKS]
     [LIST_DIRECTORIES true|false] [RELATIVE &lt;path&gt;] [CONFIGURE_DEPENDS]
     [&lt;globbing-expressions&gt;...])
</code></pre>
<p>Generate a list of files that match the <code>&lt;globbing-expressions&gt;</code> and store it into the <code>&lt;variable&gt;</code>. Globbing expressions are similar to regular expressions, but much simpler. If <code>RELATIVE</code> flag is specified, the results will be returned as relative paths to the given path. </p>
<p>Changed in version 3.6: The results will be ordered lexicographically. </p>
<p>On Windows and macOS, globbing is case-insensitive even if the underlying filesystem is case-sensitive (both filenames and globbing expressions are converted to lowercase before matching). On other platforms, globbing is case-sensitive. </p>
<p>New in version 3.3: By default <code>GLOB</code> lists directories - directories are omitted in result if <code>LIST_DIRECTORIES</code> is set to false. </p>
<p>New in version 3.12: If the <code>CONFIGURE_DEPENDS</code> flag is specified, CMake will add logic to the main build system check target to rerun the flagged <code>GLOB</code> commands at build time. If any of the outputs change, CMake will regenerate the build system. </p>
<p> <code>NOTE:</code> We do not recommend using GLOB to collect a list of source files from your source tree. If no CMakeLists.txt file changes when a source is added or removed then the generated build system cannot know when to ask CMake to regenerate. The <code>CONFIGURE_DEPENDS</code> flag may not work reliably on all generators, or if a new generator is added in the future that cannot support it, projects using it will be stuck. Even if <code>CONFIGURE_DEPENDS</code> works reliably, there is still a cost to perform the check on every rebuild. </p>
<p>Examples of globbing expressions include: </p>
<pre><code>*.cxx - match all files with extension cxx
*.vt? - match all files with extension vta,...,vtz
f[3-5].txt - match files f3.txt, f4.txt, f5.txt
</code></pre>
<p>The <code>GLOB_RECURSE</code> mode will traverse all the subdirectories of the matched directory and match the files. Subdirectories that are symlinks are only traversed if <code>FOLLOW_SYMLINKS</code> is given or policy <code>CMP0009</code> is not set to <code>NEW</code>. </p>
<p>New in version 3.3: By default <code>GLOB_RECURSE</code> omits directories from result list - setting <code>LIST_DIRECTORIES</code> to true adds directories to result list. If <code>FOLLOW_SYMLINKS</code> is given or policy <code>CMP0009</code> is not set to <code>NEW</code> then <code>LIST_DIRECTORIES</code> treats symlinks as directories. </p>
<p>Examples of recursive globbing include: </p>
<pre><code>/dir/*.py - match all python files in /dir and subdirectories
</code></pre>
<pre><code>file(MAKE_DIRECTORY [&lt;directories&gt;...])
</code></pre>
<p>Create the given directories and their parents as needed. </p>
<pre><code>file(REMOVE [&lt;files&gt;...])
file(REMOVE_RECURSE [&lt;files&gt;...])
</code></pre>
<p>Remove the given files. The <code>REMOVE_RECURSE</code> mode will remove the given files and directories, also non-empty directories. No error is emitted if a given file does not exist. Relative input paths are evaluated with respect to the current source directory. </p>
<p>Changed in version 3.15: Empty input paths are ignored with a warning. Previous versions of CMake interpreted empty strings as a relative path with respect to the current directory and removed its contents. </p>
<pre><code>file(RENAME &lt;oldname&gt; &lt;newname&gt;
     [RESULT &lt;result&gt;]
     [NO_REPLACE])
</code></pre>
<p>Move a file or directory within a filesystem from <code>&lt;oldname&gt;</code> to <code>&lt;newname&gt;</code>, replacing the destination atomically. </p>
<p>The options are: </p>
<dl>
<dt><code>RESULT &lt;result&gt;</code></dt>
<dd> <p> New in version 3.21. </p>
<p>Set <code>&lt;result&gt;</code> variable to <code>0</code> on success or an error message otherwise. If <code>RESULT</code> is not specified and the operation fails, an error is emitted. </p>
 </dd>
<dt><code>NO_REPLACE</code></dt>
<dd> <p> New in version 3.21. </p>
<p>If the <code>&lt;newname&gt;</code> path already exists, do not replace it. If <code>RESULT &lt;result&gt;</code> is used, the result variable will be set to <code>NO_REPLACE</code>. Otherwise, an error is emitted. </p>
<pre><code>file(COPY_FILE &lt;oldname&gt; &lt;newname&gt;
     [RESULT &lt;result&gt;]
     [ONLY_IF_DIFFERENT])
</code></pre>
<p>New in version 3.21. </p>
<p>Copy a file from <code>&lt;oldname&gt;</code> to <code>&lt;newname&gt;</code>. Directories are not supported. Symlinks are ignored and <code>&lt;oldfile&gt;</code>&#8216;s content is read and written to <code>&lt;newname&gt;</code> as a new file. </p>
<p>The options are: </p>
 </dd>
<dt><code>RESULT &lt;result&gt;</code></dt>
<dd> <p> Set <code>&lt;result&gt;</code> variable to <code>0</code> on success or an error message otherwise. If <code>RESULT</code> is not specified and the operation fails, an error is emitted. </p>
 </dd>
<dt><code>ONLY_IF_DIFFERENT</code></dt>
<dd> <p> If the <code>&lt;newname&gt;</code> path already exists, do not replace it if the file&#8217;s contents are already the same as <code>&lt;oldname&gt;</code> (this avoids updating <code>&lt;newname&gt;</code>&#8216;s timestamp). </p>
<p>This sub-command has some similarities to <code>configure_file()</code> with the <code>COPYONLY</code> option. An important difference is that <code>configure_file()</code> creates a dependency on the source file, so CMake will be re-run if it changes. The <code>file(COPY_FILE)</code> sub-command does not create such a dependency. </p>
<p>See also the <code>file(COPY)</code> sub-command just below which provides further file-copying capabilities. </p>
<pre><code>file(&lt;COPY|INSTALL&gt; &lt;files&gt;... DESTINATION &lt;dir&gt;
     [NO_SOURCE_PERMISSIONS | USE_SOURCE_PERMISSIONS]
     [FILE_PERMISSIONS &lt;permissions&gt;...]
     [DIRECTORY_PERMISSIONS &lt;permissions&gt;...]
     [FOLLOW_SYMLINK_CHAIN]
     [FILES_MATCHING]
     [[PATTERN &lt;pattern&gt; | REGEX &lt;regex&gt;]
      [EXCLUDE] [PERMISSIONS &lt;permissions&gt;...]] [...])
</code></pre>
<p> <code>NOTE:</code> For a simple file copying operation, the <code>file(COPY_FILE)</code> sub-command just above may be easier to use. </p>
<p>The <code>COPY</code> signature copies files, directories, and symlinks to a destination folder. Relative input paths are evaluated with respect to the current source directory, and a relative destination is evaluated with respect to the current build directory. Copying preserves input file timestamps, and optimizes out a file if it exists at the destination with the same timestamp. Copying preserves input permissions unless explicit permissions or <code>NO_SOURCE_PERMISSIONS</code> are given (default is <code>USE_SOURCE_PERMISSIONS</code>). </p>
<p>New in version 3.15: If <code>FOLLOW_SYMLINK_CHAIN</code> is specified, <code>COPY</code> will recursively resolve the symlinks at the paths given until a real file is found, and install a corresponding symlink in the destination for each symlink encountered. For each symlink that is installed, the resolution is stripped of the directory, leaving only the filename, meaning that the new symlink points to a file in the same directory as the symlink. This feature is useful on some Unix systems, where libraries are installed as a chain of symlinks with version numbers, with less specific versions pointing to more specific versions. <code>FOLLOW_SYMLINK_CHAIN</code> will install all of these symlinks and the library itself into the destination directory. For example, if you have the following directory structure: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>/opt/foo/lib/libfoo.so.1.2.3</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>/opt/foo/lib/libfoo.so.1.2 -&gt; libfoo.so.1.2.3</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>/opt/foo/lib/libfoo.so.1 -&gt; libfoo.so.1.2</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>/opt/foo/lib/libfoo.so -&gt; libfoo.so.1</code> </p>
<p>and you do: </p>
<pre><code>file(COPY /opt/foo/lib/libfoo.so DESTINATION lib FOLLOW_SYMLINK_CHAIN)
</code></pre>
<p>This will install all of the symlinks and <code>libfoo.so.1.2.3</code> itself into <code>lib</code>. </p>
<p>See the <code>install(DIRECTORY)</code> command for documentation of permissions, <code>FILES_MATCHING</code>, <code>PATTERN</code>, <code>REGEX</code>, and <code>EXCLUDE</code> options. Copying directories preserves the structure of their content even if options are used to select a subset of files. </p>
<p>The <code>INSTALL</code> signature differs slightly from <code>COPY</code>: it prints status messages, and <code>NO_SOURCE_PERMISSIONS</code> is default. </p>
<p>Installation scripts generated by the <code>install()</code> command use this signature (with some undocumented options for internal use). </p>
<p>Changed in version 3.22: The environment variable <code>CMAKE_INSTALL_MODE</code> can override the default copying behavior of <i>file(INSTALL)</i>. </p>
<pre><code>file(SIZE &lt;filename&gt; &lt;variable&gt;)
</code></pre>
<p>New in version 3.14. </p>
<p>Determine the file size of the <code>&lt;filename&gt;</code> and put the result in <code>&lt;variable&gt;</code> variable. Requires that <code>&lt;filename&gt;</code> is a valid path pointing to a file and is readable. </p>
<pre><code>file(READ_SYMLINK &lt;linkname&gt; &lt;variable&gt;)
</code></pre>
<p>New in version 3.14. </p>
<p>This subcommand queries the symlink <code>&lt;linkname&gt;</code> and stores the path it points to in the result <code>&lt;variable&gt;</code>. If <code>&lt;linkname&gt;</code> does not exist or is not a symlink, CMake issues a fatal error. </p>
<p>Note that this command returns the raw symlink path and does not resolve a relative path. The following is an example of how to ensure that an absolute path is obtained: </p>
<pre><code>set(linkname &quot;/path/to/foo.sym&quot;)
file(READ_SYMLINK &quot;${linkname}&quot; result)
if(NOT IS_ABSOLUTE &quot;${result}&quot;)
  get_filename_component(dir &quot;${linkname}&quot; DIRECTORY)
  set(result &quot;${dir}/${result}&quot;)
endif()
</code></pre>
<pre><code>file(CREATE_LINK &lt;original&gt; &lt;linkname&gt;
     [RESULT &lt;result&gt;] [COPY_ON_ERROR] [SYMBOLIC])
</code></pre>
<p>New in version 3.14. </p>
<p>Create a link <code>&lt;linkname&gt;</code> that points to <code>&lt;original&gt;</code>. It will be a hard link by default, but providing the <code>SYMBOLIC</code> option results in a symbolic link instead. Hard links require that <code>original</code> exists and is a file, not a directory. If <code>&lt;linkname&gt;</code> already exists, it will be overwritten. </p>
<p>The <code>&lt;result&gt;</code> variable, if specified, receives the status of the operation. It is set to <code>0</code> upon success or an error message otherwise. If <code>RESULT</code> is not specified and the operation fails, a fatal error is emitted. </p>
<p>Specifying <code>COPY_ON_ERROR</code> enables copying the file as a fallback if creating the link fails. It can be useful for handling situations such as <code>&lt;original&gt;</code> and <code>&lt;linkname&gt;</code> being on different drives or mount points, which would make them unable to support a hard link. </p>
<pre><code>file(CHMOD &lt;files&gt;... &lt;directories&gt;...
    [PERMISSIONS &lt;permissions&gt;...]
    [FILE_PERMISSIONS &lt;permissions&gt;...]
    [DIRECTORY_PERMISSIONS &lt;permissions&gt;...])
</code></pre>
<p>New in version 3.19. </p>
<p>Set the permissions for the <code>&lt;files&gt;...</code> and <code>&lt;directories&gt;...</code> specified. Valid permissions are <code>OWNER_READ</code>, <code>OWNER_WRITE</code>, <code>OWNER_EXECUTE</code>, <code>GROUP_READ</code>, <code>GROUP_WRITE</code>, <code>GROUP_EXECUTE</code>, <code>WORLD_READ</code>, <code>WORLD_WRITE</code>, <code>WORLD_EXECUTE</code>, <code>SETUID</code>, <code>SETGID</code>. </p>
<p>Valid combination of keywords are: </p>
 </dd>
<dt><code>PERMISSIONS</code></dt>
<dd> <p> All items are changed. </p>
 </dd>
<dt><code>FILE_PERMISSIONS</code></dt>
<dd> <p> Only files are changed. </p>
 </dd>
<dt><code>DIRECTORY_PERMISSIONS</code></dt>
<dd> <p> Only directories are changed. </p>
 </dd>
<dt><code>PERMISSIONS</code> and <code>FILE_PERMISSIONS</code></dt>
<dd> <p> <code>FILE_PERMISSIONS</code> overrides <code>PERMISSIONS</code> for files. </p>
 </dd>
<dt><code>PERMISSIONS</code> and <code>DIRECTORY_PERMISSIONS</code></dt>
<dd> <p> <code>DIRECTORY_PERMISSIONS</code> overrides <code>PERMISSIONS</code> for directories. </p>
 </dd>
<dt><code>FILE_PERMISSIONS</code> and <code>DIRECTORY_PERMISSIONS</code></dt>
<dd> <p> Use <code>FILE_PERMISSIONS</code> for files and <code>DIRECTORY_PERMISSIONS</code> for directories. </p>
<pre><code>file(CHMOD_RECURSE &lt;files&gt;... &lt;directories&gt;...
     [PERMISSIONS &lt;permissions&gt;...]
     [FILE_PERMISSIONS &lt;permissions&gt;...]
     [DIRECTORY_PERMISSIONS &lt;permissions&gt;...])
</code></pre>
<p>New in version 3.19. </p>
<p>Same as <i>CHMOD</i>, but change the permissions of files and directories present in the <code>&lt;directories&gt;...</code> recursively. </p>
 </dd></dl>
<h3>Path Conversion</h3>
<pre><code>file(REAL_PATH &lt;path&gt; &lt;out-var&gt; [BASE_DIRECTORY &lt;dir&gt;] [EXPAND_TILDE])
</code></pre>
<p>New in version 3.19. </p>
<p>Compute the absolute path to an existing file or directory with symlinks resolved. </p>
<dl>
<dt><code>BASE_DIRECTORY &lt;dir&gt;</code></dt>
<dd> <p> If the provided <code>&lt;path&gt;</code> is a relative path, it is evaluated relative to the given base directory <code>&lt;dir&gt;</code>. If no base directory is provided, the default base directory will be <code>CMAKE_CURRENT_SOURCE_DIR</code>. </p>
 </dd>
<dt><code>EXPAND_TILDE</code></dt>
<dd> <p> New in version 3.21. </p>
<p>If the <code>&lt;path&gt;</code> is <code>~</code> or starts with <code>~/</code>, the <code>~</code> is replaced by the user&#8217;s home directory. The path to the home directory is obtained from environment variables. On Windows, the <code>USERPROFILE</code> environment variable is used, falling back to the <code>HOME</code> environment variable if <code>USERPROFILE</code> is not defined. On all other platforms, only <code>HOME</code> is used. </p>
<pre><code>file(RELATIVE_PATH &lt;variable&gt; &lt;directory&gt; &lt;file&gt;)
</code></pre>
<p>Compute the relative path from a <code>&lt;directory&gt;</code> to a <code>&lt;file&gt;</code> and store it in the <code>&lt;variable&gt;</code>. </p>
<pre><code>file(TO_CMAKE_PATH &quot;&lt;path&gt;&quot; &lt;variable&gt;)
file(TO_NATIVE_PATH &quot;&lt;path&gt;&quot; &lt;variable&gt;)
</code></pre>
<p>The <code>TO_CMAKE_PATH</code> mode converts a native <code>&lt;path&gt;</code> into a cmake-style path with forward-slashes (<code>/</code>). The input can be a single path or a system search path like <code>$ENV{PATH}</code>. A search path will be converted to a cmake-style list separated by <code>;</code> characters. </p>
<p>The <code>TO_NATIVE_PATH</code> mode converts a cmake-style <code>&lt;path&gt;</code> into a native path with platform-specific slashes (<code>\</code> on Windows hosts and <code>/</code> elsewhere). </p>
<p>Always use double quotes around the <code>&lt;path&gt;</code> to be sure it is treated as a single argument to this command. </p>
 </dd></dl>
<h3>Transfer</h3>
<pre><code>file(DOWNLOAD &lt;url&gt; [&lt;file&gt;] [&lt;options&gt;...])
file(UPLOAD &lt;file&gt; &lt;url&gt; [&lt;options&gt;...])
</code></pre>
<p>The <code>DOWNLOAD</code> subcommand downloads the given <code>&lt;url&gt;</code> to a local <code>&lt;file&gt;</code>. The <code>UPLOAD</code> mode uploads a local <code>&lt;file&gt;</code> to a given <code>&lt;url&gt;</code>. </p>
<p>New in version 3.19: If <code>&lt;file&gt;</code> is not specified for <code>file(DOWNLOAD)</code>, the file is not saved. This can be useful if you want to know if a file can be downloaded (for example, to check that it exists) without actually saving it anywhere. </p>
<p>Options to both <code>DOWNLOAD</code> and <code>UPLOAD</code> are: </p>
<dl>
<dt><code>INACTIVITY_TIMEOUT &lt;seconds&gt;</code></dt>
<dd> <p> Terminate the operation after a period of inactivity. </p>
 </dd>
<dt><code>LOG &lt;variable&gt;</code></dt>
<dd> <p> Store a human-readable log of the operation in a variable. </p>
 </dd>
<dt><code>SHOW_PROGRESS</code></dt>
<dd> <p> Print progress information as status messages until the operation is complete. </p>
 </dd>
<dt><code>STATUS &lt;variable&gt;</code></dt>
<dd> <p> Store the resulting status of the operation in a variable. The status is a <code>;</code> separated list of length 2. The first element is the numeric return value for the operation, and the second element is a string value for the error. A <code>0</code> numeric error means no error in the operation. </p>
 </dd>
<dt><code>TIMEOUT &lt;seconds&gt;</code></dt>
<dd> <p> Terminate the operation after a given total time has elapsed. </p>
 </dd>
<dt><code>USERPWD &lt;username&gt;:&lt;password&gt;</code></dt>
<dd> <p> New in version 3.7. </p>
<p>Set username and password for operation. </p>
 </dd>
<dt><code>HTTPHEADER &lt;HTTP-header&gt;</code></dt>
<dd> <p> New in version 3.7. </p>
<p>HTTP header for operation. Suboption can be repeated several times. </p>
 </dd>
<dt><code>NETRC &lt;level&gt;</code></dt>
<dd> <p> New in version 3.11. </p>
<p>Specify whether the .netrc file is to be used for operation. If this option is not specified, the value of the <code>CMAKE_NETRC</code> variable will be used instead. Valid levels are: </p>
 </dd>
<dt><code>IGNORED</code></dt>
<dd> <p> The .netrc file is ignored. This is the default. </p>
 </dd>
<dt><code>OPTIONAL</code></dt>
<dd> <p> The .netrc file is optional, and information in the URL is preferred. The file will be scanned to find which ever information is not specified in the URL. </p>
 </dd>
<dt><code>REQUIRED</code></dt>
<dd> <p> The .netrc file is required, and information in the URL is ignored. </p>
 </dd>
<dt><code>NETRC_FILE &lt;file&gt;</code></dt>
<dd> <p> New in version 3.11. </p>
<p>Specify an alternative .netrc file to the one in your home directory, if the <code>NETRC</code> level is <code>OPTIONAL</code> or <code>REQUIRED</code>. If this option is not specified, the value of the <code>CMAKE_NETRC_FILE</code> variable will be used instead. </p>
 </dd>
<dt><code>TLS_VERIFY &lt;ON|OFF&gt;</code></dt>
<dd> <p> Specify whether to verify the server certificate for <code>https://</code> URLs. The default is to <i>not</i> verify. If this option is not specified, the value of the <code>CMAKE_TLS_VERIFY</code> variable will be used instead. </p>
<p>New in version 3.18: Added support to <code>file(UPLOAD)</code>. </p>
 </dd>
<dt><code>TLS_CAINFO &lt;file&gt;</code></dt>
<dd> <p> Specify a custom Certificate Authority file for <code>https://</code> URLs. If this option is not specified, the value of the <code>CMAKE_TLS_CAINFO</code> variable will be used instead. </p>
<p>New in version 3.18: Added support to <code>file(UPLOAD)</code>. </p>
<p>For <code>https://</code> URLs CMake must be built with OpenSSL support. <code>TLS/SSL</code> certificates are not checked by default. Set <code>TLS_VERIFY</code> to <code>ON</code> to check certificates. </p>
<p>Additional options to <code>DOWNLOAD</code> are: </p>
<p> <code>EXPECTED_HASH ALGO=&lt;value&gt;</code> Verify that the downloaded content hash matches the expected value, where <code>ALGO</code> is one of the algorithms supported by <code>file(&lt;HASH&gt;)</code>. If it does not match, the operation fails with an error. It is an error to specify this if <code>DOWNLOAD</code> is not given a <code>&lt;file&gt;</code>. </p>
 </dd>
<dt><code>EXPECTED_MD5 &lt;value&gt;</code></dt>
<dd> <p> Historical short-hand for <code>EXPECTED_HASH MD5=&lt;value&gt;</code>. It is an error to specify this if <code>DOWNLOAD</code> is not given a <code>&lt;file&gt;</code>. </p>
 </dd></dl>
<h3>Locking</h3>
<pre><code>file(LOCK &lt;path&gt; [DIRECTORY] [RELEASE]
     [GUARD &lt;FUNCTION|FILE|PROCESS&gt;]
     [RESULT_VARIABLE &lt;variable&gt;]
     [TIMEOUT &lt;seconds&gt;])
</code></pre>
<p>New in version 3.2. </p>
<p>Lock a file specified by <code>&lt;path&gt;</code> if no <code>DIRECTORY</code> option present and file <code>&lt;path&gt;/cmake.lock</code> otherwise. File will be locked for scope defined by <code>GUARD</code> option (default value is <code>PROCESS</code>). <code>RELEASE</code> option can be used to unlock file explicitly. If option <code>TIMEOUT</code> is not specified CMake will wait until lock succeed or until fatal error occurs. If <code>TIMEOUT</code> is set to <code>0</code> lock will be tried once and result will be reported immediately. If <code>TIMEOUT</code> is not <code>0</code> CMake will try to lock file for the period specified by <code>&lt;seconds&gt;</code> value. Any errors will be interpreted as fatal if there is no <code>RESULT_VARIABLE</code> option. Otherwise result will be stored in <code>&lt;variable&gt;</code> and will be <code>0</code> on success or error message on failure. </p>
<p>Note that lock is advisory &#8211; there is no guarantee that other processes will respect this lock, i.e. lock synchronize two or more CMake instances sharing some modifiable resources. Similar logic applied to <code>DIRECTORY</code> option - locking parent directory doesn&#8217;t prevent other <code>LOCK</code> commands to lock any child directory or file. </p>
<p>Trying to lock file twice is not allowed. Any intermediate directories and file itself will be created if they not exist. <code>GUARD</code> and <code>TIMEOUT</code> options ignored on <code>RELEASE</code> operation.  </p>
<h3>Archiving</h3>
<pre><code>file(ARCHIVE_CREATE OUTPUT &lt;archive&gt;
  PATHS &lt;paths&gt;...
  [FORMAT &lt;format&gt;]
  [COMPRESSION &lt;compression&gt; [COMPRESSION_LEVEL &lt;compression-level&gt;]]
  [MTIME &lt;mtime&gt;]
  [VERBOSE])
</code></pre>
<p>New in version 3.18. </p>
<p>Creates the specified <code>&lt;archive&gt;</code> file with the files and directories listed in <code>&lt;paths&gt;</code>. Note that <code>&lt;paths&gt;</code> must list actual files or directories, wildcards are not supported. </p>
<p>Use the <code>FORMAT</code> option to specify the archive format. Supported values for <code>&lt;format&gt;</code> are <code>7zip</code>, <code>gnutar</code>, <code>pax</code>, <code>paxr</code>, <code>raw</code> and <code>zip</code>. If <code>FORMAT</code> is not given, the default format is <code>paxr</code>. </p>
<p>Some archive formats allow the type of compression to be specified. The <code>7zip</code> and <code>zip</code> archive formats already imply a specific type of compression. The other formats use no compression by default, but can be directed to do so with the <code>COMPRESSION</code> option. Valid values for <code>&lt;compression&gt;</code> are <code>None</code>, <code>BZip2</code>, <code>GZip</code>, <code>XZ</code>, and <code>Zstd</code>. </p>
<p>New in version 3.19: The compression level can be specified with the <code>COMPRESSION_LEVEL</code> option. The <code>&lt;compression-level&gt;</code> should be between 0-9, with the default being 0. The <code>COMPRESSION</code> option must be present when <code>COMPRESSION_LEVEL</code> is given. </p>
<p> <code>NOTE:</code> With <code>FORMAT</code> set to <code>raw</code> only one file will be compressed with the compression type specified by <code>COMPRESSION</code>. </p>
<p>The <code>VERBOSE</code> option enables verbose output for the archive operation. </p>
<p>To specify the modification time recorded in tarball entries, use the <code>MTIME</code> option. </p>
<pre><code>file(ARCHIVE_EXTRACT INPUT &lt;archive&gt;
  [DESTINATION &lt;dir&gt;]
  [PATTERNS &lt;patterns&gt;...]
  [LIST_ONLY]
  [VERBOSE])
</code></pre>
<p>New in version 3.18. </p>
<p>Extracts or lists the content of the specified <code>&lt;archive&gt;</code>. </p>
<p>The directory where the content of the archive will be extracted to can be specified using the <code>DESTINATION</code> option. If the directory does not exist, it will be created. If <code>DESTINATION</code> is not given, the current binary directory will be used. </p>
<p>If required, you may select which files and directories to list or extract from the archive using the specified <code>&lt;patterns&gt;</code>. Wildcards are supported. If the <code>PATTERNS</code> option is not given, the entire archive will be listed or extracted. </p>
<p> <code>LIST_ONLY</code> will list the files in the archive rather than extract them. </p>
<p>With <code>VERBOSE</code>, the command will produce verbose output.  </p>
<h3>find_file</h3>
<p>A short-hand signature is: </p>
<pre><code>find_file (&lt;VAR&gt; name1 [path1 path2 ...])
</code></pre>
<p>The general signature is: </p>
<pre><code>find_file (
          &lt;VAR&gt;
          name | NAMES name1 [name2 ...]
          [HINTS [path | ENV var]... ]
          [PATHS [path | ENV var]... ]
          [PATH_SUFFIXES suffix1 [suffix2 ...]]
          [DOC &quot;cache documentation string&quot;]
          [NO_CACHE]
          [REQUIRED]
          [NO_DEFAULT_PATH]
          [NO_PACKAGE_ROOT_PATH]
          [NO_CMAKE_PATH]
          [NO_CMAKE_ENVIRONMENT_PATH]
          [NO_SYSTEM_ENVIRONMENT_PATH]
          [NO_CMAKE_SYSTEM_PATH]
          [CMAKE_FIND_ROOT_PATH_BOTH |
           ONLY_CMAKE_FIND_ROOT_PATH |
           NO_CMAKE_FIND_ROOT_PATH]
         )
</code></pre>
<p>This command is used to find a full path to named file. A cache entry, or a normal variable if <code>NO_CACHE</code> is specified, named by <code>&lt;VAR&gt;</code> is created to store the result of this command. If the full path to a file is found the result is stored in the variable and the search will not be repeated unless the variable is cleared. If nothing is found, the result will be <code>&lt;VAR&gt;-NOTFOUND</code>. </p>
<p>Options include: </p>
<dl>
<dt><code>NAMES</code></dt>
<dd> <p> Specify one or more possible names for the full path to a file. </p>
<p>When using this to specify names with and without a version suffix, we recommend specifying the unversioned name first so that locally-built packages can be found before those provided by distributions. </p>
 </dd>
<dt><code>HINTS</code>, <code>PATHS</code></dt>
<dd> <p> Specify directories to search in addition to the default locations. The <code>ENV var</code> sub-option reads paths from a system environment variable. </p>
 </dd>
<dt><code>PATH_SUFFIXES</code></dt>
<dd> <p> Specify additional subdirectories to check below each directory location otherwise considered. </p>
 </dd>
<dt><code>DOC</code></dt>
<dd> <p> Specify the documentation string for the <code>&lt;VAR&gt;</code> cache entry. </p>
 </dd>
<dt><code>NO_CACHE</code></dt>
<dd> <p> New in version 3.21. </p>
<p>The result of the search will be stored in a normal variable rather than a cache entry. </p>
<p> <code>NOTE:</code> If the variable is already set before the call (as a normal or cache variable) then the search will not occur. </p>
<p> <code>WARNING:</code> This option should be used with caution because it can greatly increase the cost of repeated configure steps. </p>
 </dd>
<dt><code>REQUIRED</code></dt>
<dd> <p> New in version 3.18. </p>
<p>Stop processing with an error message if nothing is found, otherwise the search will be attempted again the next time find_file is invoked with the same variable. </p>
<p>If <code>NO_DEFAULT_PATH</code> is specified, then no additional paths are added to the search. If <code>NO_DEFAULT_PATH</code> is not specified, the search process is as follows: </p>
 </dd>
<dt>1.</dt>
<dd> <p> New in version 3.12: If called from within a find module or any other script loaded by a call to <code>find_package(&lt;PackageName&gt;)</code>, search prefixes unique to the current package being found. Specifically, look in the <code>&lt;PackageName&gt;_ROOT</code> CMake variable and the <code>&lt;PackageName&gt;_ROOT</code> environment variable. The package root variables are maintained as a stack, so if called from nested find modules or config packages, root paths from the parent&#8217;s find module or config package will be searched after paths from the current module or package. In other words, the search order would be <code>&lt;CurrentPackage&gt;_ROOT</code>, <code>ENV{&lt;CurrentPackage&gt;_ROOT}</code>, <code>&lt;ParentPackage&gt;_ROOT</code>, <code>ENV{&lt;ParentPackage&gt;_ROOT}</code>, etc. This can be skipped if <code>NO_PACKAGE_ROOT_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_PACKAGE_ROOT_PATH</code> to <code>FALSE</code>. See policy <code>CMP0074</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&lt;prefix&gt;/include/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/include</code> for each <code>&lt;prefix&gt;</code> in the <code>&lt;PackageName&gt;_ROOT</code> CMake variable and the <code>&lt;PackageName&gt;_ROOT</code> environment variable if called from within a find module loaded by <code>find_package(&lt;PackageName&gt;)</code> </p>
 </dd>
<dt>2.</dt>
<dd> <p> Search paths specified in cmake-specific cache variables. These are intended to be used on the command line with a <code>-DVAR=value</code>. The values are interpreted as semicolon-separated lists. This can be skipped if <code>NO_CMAKE_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_CMAKE_PATH</code> to <code>FALSE</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&lt;prefix&gt;/include/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/include</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_PREFIX_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_INCLUDE_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_FRAMEWORK_PATH</code> </p>
 </dd>
<dt>3.</dt>
<dd> <p> Search paths specified in cmake-specific environment variables. These are intended to be set in the user&#8217;s shell configuration, and therefore use the host&#8217;s native path separator (<code>;</code> on Windows and <code>:</code> on UNIX). This can be skipped if <code>NO_CMAKE_ENVIRONMENT_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_CMAKE_ENVIRONMENT_PATH</code> to <code>FALSE</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&lt;prefix&gt;/include/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/include</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_PREFIX_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_INCLUDE_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_FRAMEWORK_PATH</code> </p>
 </dd>
<dt>4.</dt>
<dd> <p> Search the paths specified by the <code>HINTS</code> option. These should be paths computed by system introspection, such as a hint provided by the location of another item already found. Hard-coded guesses should be specified with the <code>PATHS</code> option. </p>
 </dd>
<dt>5.</dt>
<dd> <p> Search the standard system environment variables. This can be skipped if <code>NO_SYSTEM_ENVIRONMENT_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_SYSTEM_ENVIRONMENT_PATH</code> to <code>FALSE</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The directories in <code>INCLUDE</code> and <code>PATH</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On Windows hosts: <code>&lt;prefix&gt;/include/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/include</code> for each <code>&lt;prefix&gt;/[s]bin</code> in <code>PATH</code>, and <code>&lt;entry&gt;/include</code> for other entries in <code>PATH</code>. </p>
 </dd>
<dt>6.</dt>
<dd> <p> Search cmake variables defined in the Platform files for the current system. This can be skipped if <code>NO_CMAKE_SYSTEM_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_CMAKE_SYSTEM_PATH</code> to <code>FALSE</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&lt;prefix&gt;/include/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/include</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_SYSTEM_PREFIX_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_SYSTEM_INCLUDE_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_SYSTEM_FRAMEWORK_PATH</code> </p>
<p>The platform paths that these variables contain are locations that typically include installed software. An example being <code>/usr/local</code> for UNIX based platforms. </p>
 </dd>
<dt>7.</dt>
<dd> <p> Search the paths specified by the PATHS option or in the short-hand version of the command. These are typically hard-coded guesses. </p>
<p>New in version 3.16: Added <code>CMAKE_FIND_USE_&lt;CATEGORY&gt;_PATH</code> variables to globally disable various search locations. </p>
<p>On macOS the <code>CMAKE_FIND_FRAMEWORK</code> and <code>CMAKE_FIND_APPBUNDLE</code> variables determine the order of preference between Apple-style and unix-style package components. </p>
<p>The CMake variable <code>CMAKE_FIND_ROOT_PATH</code> specifies one or more directories to be prepended to all other search directories. This effectively &quot;re-roots&quot; the entire search under given locations. Paths which are descendants of the <code>CMAKE_STAGING_PREFIX</code> are excluded from this re-rooting, because that variable is always a path on the host system. By default the <code>CMAKE_FIND_ROOT_PATH</code> is empty. </p>
<p>The <code>CMAKE_SYSROOT</code> variable can also be used to specify exactly one directory to use as a prefix. Setting <code>CMAKE_SYSROOT</code> also has other effects. See the documentation for that variable for more. </p>
<p>These variables are especially useful when cross-compiling to point to the root directory of the target environment and CMake will search there too. By default at first the directories listed in <code>CMAKE_FIND_ROOT_PATH</code> are searched, then the <code>CMAKE_SYSROOT</code> directory is searched, and then the non-rooted directories will be searched. The default behavior can be adjusted by setting <code>CMAKE_FIND_ROOT_PATH_MODE_INCLUDE</code>. This behavior can be manually overridden on a per-call basis using options: </p>
 </dd>
<dt><code>CMAKE_FIND_ROOT_PATH_BOTH</code></dt>
<dd> <p> Search in the order described above. </p>
 </dd>
<dt><code>NO_CMAKE_FIND_ROOT_PATH</code></dt>
<dd> <p> Do not use the <code>CMAKE_FIND_ROOT_PATH</code> variable. </p>
 </dd>
<dt><code>ONLY_CMAKE_FIND_ROOT_PATH</code></dt>
<dd> <p> Search only the re-rooted directories and directories below <code>CMAKE_STAGING_PREFIX</code>. </p>
<p>The default search order is designed to be most-specific to least-specific for common use cases. Projects may override the order by simply calling the command multiple times and using the <code>NO_*</code> options: </p>
<pre><code>find_file (&lt;VAR&gt; NAMES name PATHS paths... NO_DEFAULT_PATH)
find_file (&lt;VAR&gt; NAMES name)
</code></pre>
<p>Once one of the calls succeeds the result variable will be set and stored in the cache so that no call will search again. </p>
 </dd></dl>
<h3>find_library</h3>
<p>A short-hand signature is: </p>
<pre><code>find_library (&lt;VAR&gt; name1 [path1 path2 ...])
</code></pre>
<p>The general signature is: </p>
<pre><code>find_library (
          &lt;VAR&gt;
          name | NAMES name1 [name2 ...] [NAMES_PER_DIR]
          [HINTS [path | ENV var]... ]
          [PATHS [path | ENV var]... ]
          [PATH_SUFFIXES suffix1 [suffix2 ...]]
          [DOC &quot;cache documentation string&quot;]
          [NO_CACHE]
          [REQUIRED]
          [NO_DEFAULT_PATH]
          [NO_PACKAGE_ROOT_PATH]
          [NO_CMAKE_PATH]
          [NO_CMAKE_ENVIRONMENT_PATH]
          [NO_SYSTEM_ENVIRONMENT_PATH]
          [NO_CMAKE_SYSTEM_PATH]
          [CMAKE_FIND_ROOT_PATH_BOTH |
           ONLY_CMAKE_FIND_ROOT_PATH |
           NO_CMAKE_FIND_ROOT_PATH]
         )
</code></pre>
<p>This command is used to find a library. A cache entry, or a normal variable if <code>NO_CACHE</code> is specified, named by <code>&lt;VAR&gt;</code> is created to store the result of this command. If the library is found the result is stored in the variable and the search will not be repeated unless the variable is cleared. If nothing is found, the result will be <code>&lt;VAR&gt;-NOTFOUND</code>. </p>
<p>Options include: </p>
<dl>
<dt><code>NAMES</code></dt>
<dd> <p> Specify one or more possible names for the library. </p>
<p>When using this to specify names with and without a version suffix, we recommend specifying the unversioned name first so that locally-built packages can be found before those provided by distributions. </p>
 </dd>
<dt><code>HINTS</code>, <code>PATHS</code></dt>
<dd> <p> Specify directories to search in addition to the default locations. The <code>ENV var</code> sub-option reads paths from a system environment variable. </p>
 </dd>
<dt><code>PATH_SUFFIXES</code></dt>
<dd> <p> Specify additional subdirectories to check below each directory location otherwise considered. </p>
 </dd>
<dt><code>DOC</code></dt>
<dd> <p> Specify the documentation string for the <code>&lt;VAR&gt;</code> cache entry. </p>
 </dd>
<dt><code>NO_CACHE</code></dt>
<dd> <p> New in version 3.21. </p>
<p>The result of the search will be stored in a normal variable rather than a cache entry. </p>
<p> <code>NOTE:</code> If the variable is already set before the call (as a normal or cache variable) then the search will not occur. </p>
<p> <code>WARNING:</code> This option should be used with caution because it can greatly increase the cost of repeated configure steps. </p>
 </dd>
<dt><code>REQUIRED</code></dt>
<dd> <p> New in version 3.18. </p>
<p>Stop processing with an error message if nothing is found, otherwise the search will be attempted again the next time find_library is invoked with the same variable. </p>
<p>If <code>NO_DEFAULT_PATH</code> is specified, then no additional paths are added to the search. If <code>NO_DEFAULT_PATH</code> is not specified, the search process is as follows: </p>
 </dd>
<dt>1.</dt>
<dd> <p> New in version 3.12: If called from within a find module or any other script loaded by a call to <code>find_package(&lt;PackageName&gt;)</code>, search prefixes unique to the current package being found. Specifically, look in the <code>&lt;PackageName&gt;_ROOT</code> CMake variable and the <code>&lt;PackageName&gt;_ROOT</code> environment variable. The package root variables are maintained as a stack, so if called from nested find modules or config packages, root paths from the parent&#8217;s find module or config package will be searched after paths from the current module or package. In other words, the search order would be <code>&lt;CurrentPackage&gt;_ROOT</code>, <code>ENV{&lt;CurrentPackage&gt;_ROOT}</code>, <code>&lt;ParentPackage&gt;_ROOT</code>, <code>ENV{&lt;ParentPackage&gt;_ROOT}</code>, etc. This can be skipped if <code>NO_PACKAGE_ROOT_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_PACKAGE_ROOT_PATH</code> to <code>FALSE</code>. See policy <code>CMP0074</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&lt;prefix&gt;/lib/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/lib</code> for each <code>&lt;prefix&gt;</code> in the <code>&lt;PackageName&gt;_ROOT</code> CMake variable and the <code>&lt;PackageName&gt;_ROOT</code> environment variable if called from within a find module loaded by <code>find_package(&lt;PackageName&gt;)</code> </p>
 </dd>
<dt>2.</dt>
<dd> <p> Search paths specified in cmake-specific cache variables. These are intended to be used on the command line with a <code>-DVAR=value</code>. The values are interpreted as semicolon-separated lists. This can be skipped if <code>NO_CMAKE_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_CMAKE_PATH</code> to <code>FALSE</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&lt;prefix&gt;/lib/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/lib</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_PREFIX_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_LIBRARY_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_FRAMEWORK_PATH</code> </p>
 </dd>
<dt>3.</dt>
<dd> <p> Search paths specified in cmake-specific environment variables. These are intended to be set in the user&#8217;s shell configuration, and therefore use the host&#8217;s native path separator (<code>;</code> on Windows and <code>:</code> on UNIX). This can be skipped if <code>NO_CMAKE_ENVIRONMENT_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_CMAKE_ENVIRONMENT_PATH</code> to <code>FALSE</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&lt;prefix&gt;/lib/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/lib</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_PREFIX_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_LIBRARY_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_FRAMEWORK_PATH</code> </p>
 </dd>
<dt>4.</dt>
<dd> <p> Search the paths specified by the <code>HINTS</code> option. These should be paths computed by system introspection, such as a hint provided by the location of another item already found. Hard-coded guesses should be specified with the <code>PATHS</code> option. </p>
 </dd>
<dt>5.</dt>
<dd> <p> Search the standard system environment variables. This can be skipped if <code>NO_SYSTEM_ENVIRONMENT_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_SYSTEM_ENVIRONMENT_PATH</code> to <code>FALSE</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The directories in <code>LIB</code> and <code>PATH</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On Windows hosts: <code>&lt;prefix&gt;/lib/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/lib</code> for each <code>&lt;prefix&gt;/[s]bin</code> in <code>PATH</code>, and <code>&lt;entry&gt;/lib</code> for other entries in <code>PATH</code>. </p>
 </dd>
<dt>6.</dt>
<dd> <p> Search cmake variables defined in the Platform files for the current system. This can be skipped if <code>NO_CMAKE_SYSTEM_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_CMAKE_SYSTEM_PATH</code> to <code>FALSE</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&lt;prefix&gt;/lib/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/lib</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_SYSTEM_PREFIX_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_SYSTEM_LIBRARY_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_SYSTEM_FRAMEWORK_PATH</code> </p>
<p>The platform paths that these variables contain are locations that typically include installed software. An example being <code>/usr/local</code> for UNIX based platforms. </p>
 </dd>
<dt>7.</dt>
<dd> <p> Search the paths specified by the PATHS option or in the short-hand version of the command. These are typically hard-coded guesses. </p>
<p>New in version 3.16: Added <code>CMAKE_FIND_USE_&lt;CATEGORY&gt;_PATH</code> variables to globally disable various search locations. </p>
<p>On macOS the <code>CMAKE_FIND_FRAMEWORK</code> and <code>CMAKE_FIND_APPBUNDLE</code> variables determine the order of preference between Apple-style and unix-style package components. </p>
<p>The CMake variable <code>CMAKE_FIND_ROOT_PATH</code> specifies one or more directories to be prepended to all other search directories. This effectively &quot;re-roots&quot; the entire search under given locations. Paths which are descendants of the <code>CMAKE_STAGING_PREFIX</code> are excluded from this re-rooting, because that variable is always a path on the host system. By default the <code>CMAKE_FIND_ROOT_PATH</code> is empty. </p>
<p>The <code>CMAKE_SYSROOT</code> variable can also be used to specify exactly one directory to use as a prefix. Setting <code>CMAKE_SYSROOT</code> also has other effects. See the documentation for that variable for more. </p>
<p>These variables are especially useful when cross-compiling to point to the root directory of the target environment and CMake will search there too. By default at first the directories listed in <code>CMAKE_FIND_ROOT_PATH</code> are searched, then the <code>CMAKE_SYSROOT</code> directory is searched, and then the non-rooted directories will be searched. The default behavior can be adjusted by setting <code>CMAKE_FIND_ROOT_PATH_MODE_LIBRARY</code>. This behavior can be manually overridden on a per-call basis using options: </p>
 </dd>
<dt><code>CMAKE_FIND_ROOT_PATH_BOTH</code></dt>
<dd> <p> Search in the order described above. </p>
 </dd>
<dt><code>NO_CMAKE_FIND_ROOT_PATH</code></dt>
<dd> <p> Do not use the <code>CMAKE_FIND_ROOT_PATH</code> variable. </p>
 </dd>
<dt><code>ONLY_CMAKE_FIND_ROOT_PATH</code></dt>
<dd> <p> Search only the re-rooted directories and directories below <code>CMAKE_STAGING_PREFIX</code>. </p>
<p>The default search order is designed to be most-specific to least-specific for common use cases. Projects may override the order by simply calling the command multiple times and using the <code>NO_*</code> options: </p>
<pre><code>find_library (&lt;VAR&gt; NAMES name PATHS paths... NO_DEFAULT_PATH)
find_library (&lt;VAR&gt; NAMES name)
</code></pre>
<p>Once one of the calls succeeds the result variable will be set and stored in the cache so that no call will search again. </p>
<p>When more than one value is given to the <code>NAMES</code> option this command by default will consider one name at a time and search every directory for it. The <code>NAMES_PER_DIR</code> option tells this command to consider one directory at a time and search for all names in it. </p>
<p>Each library name given to the <code>NAMES</code> option is first considered as a library file name and then considered with platform-specific prefixes (e.g. <code>lib</code>) and suffixes (e.g. <code>.so</code>). Therefore one may specify library file names such as <code>libfoo.a</code> directly. This can be used to locate static libraries on UNIX-like systems. </p>
<p>If the library found is a framework, then <code>&lt;VAR&gt;</code> will be set to the full path to the framework <code>&lt;fullPath&gt;/A.framework</code>. When a full path to a framework is used as a library, CMake will use a <code>-framework A</code>, and a <code>-F&lt;fullPath&gt;</code> to link the framework to the target. </p>
<p>If the <code>CMAKE_FIND_LIBRARY_CUSTOM_LIB_SUFFIX</code> variable is set all search paths will be tested as normal, with the suffix appended, and with all matches of <code>lib/</code> replaced with <code>lib${CMAKE_FIND_LIBRARY_CUSTOM_LIB_SUFFIX}/</code>. This variable overrides the <code>FIND_LIBRARY_USE_LIB32_PATHS</code>, <code>FIND_LIBRARY_USE_LIBX32_PATHS</code>, and <code>FIND_LIBRARY_USE_LIB64_PATHS</code> global properties. </p>
<p>If the <code>FIND_LIBRARY_USE_LIB32_PATHS</code> global property is set all search paths will be tested as normal, with <code>32/</code> appended, and with all matches of <code>lib/</code> replaced with <code>lib32/</code>. This property is automatically set for the platforms that are known to need it if at least one of the languages supported by the <code>project()</code> command is enabled. </p>
<p>If the <code>FIND_LIBRARY_USE_LIBX32_PATHS</code> global property is set all search paths will be tested as normal, with <code>x32/</code> appended, and with all matches of <code>lib/</code> replaced with <code>libx32/</code>. This property is automatically set for the platforms that are known to need it if at least one of the languages supported by the <code>project()</code> command is enabled. </p>
<p>If the <code>FIND_LIBRARY_USE_LIB64_PATHS</code> global property is set all search paths will be tested as normal, with <code>64/</code> appended, and with all matches of <code>lib/</code> replaced with <code>lib64/</code>. This property is automatically set for the platforms that are known to need it if at least one of the languages supported by the <code>project()</code> command is enabled. </p>
 </dd></dl>
<h3>find_package</h3>
<p>Find a package (usually provided by something external to the project), and load its package-specific details.  </p>
<h3>Search Modes</h3>
<p>The command has two very distinct ways of conducting the search: </p>
<dl>
<dt><code>Module mode</code></dt>
<dd> <p> In this mode, CMake searches for a file called <code>Find&lt;PackageName&gt;.cmake</code>, looking first in the locations listed in the <code>CMAKE_MODULE_PATH</code>, then among the Find Modules provided by the CMake installation. If the file is found, it is read and processed by CMake. It is responsible for finding the package, checking the version, and producing any needed messages. Some Find modules provide limited or no support for versioning; check the Find module&#8217;s documentation. </p>
<p>The <code>Find&lt;PackageName&gt;.cmake</code> file is not typically provided by the package itself. Rather, it is normally provided by something external to the package, such as the operating system, CMake itself, or even the project from which the <code>find_package()</code> command was called. Being externally provided, Find Modules tend to be heuristic in nature and are susceptible to becoming out-of-date. They typically search for certain libraries, files and other package artifacts. </p>
<p>Module mode is only supported by the <i>basic command signature</i>. </p>
 </dd>
<dt><code>Config mode</code></dt>
<dd> <p> In this mode, CMake searches for a file called <code>&lt;lowercasePackageName&gt;-config.cmake</code> or <code>&lt;PackageName&gt;Config.cmake</code>. It will also look for <code>&lt;lowercasePackageName&gt;-config-version.cmake</code> or <code>&lt;PackageName&gt;ConfigVersion.cmake</code> if version details were specified (see <i>Config Mode Version Selection</i> for an explanation of how these separate version files are used). </p>
<p>In config mode, the command can be given a list of names to search for as package names. The locations where CMake searches for the config and version files is considerably more complicated than for Module mode (see <i>Config Mode Search Procedure</i>). </p>
<p>The config and version files are typically installed as part of the package, so they tend to be more reliable than Find modules. They usually contain direct knowledge of the package contents, so no searching or heuristics are needed within the config or version files themselves. </p>
<p>Config mode is supported by both the <i>basic</i> and <i>full</i> command signatures. </p>
<p>The command arguments determine which of the above modes is used. When the <i>basic signature</i> is used, the command searches in Module mode first. If the package is not found, the search falls back to Config mode. A user may set the <code>CMAKE_FIND_PACKAGE_PREFER_CONFIG</code> variable to true to reverse the priority and direct CMake to search using Config mode first before falling back to Module mode. The basic signature can also be forced to use only Module mode with a <code>MODULE</code> keyword. If the <i>full signature</i> is used, the command only searches in Config mode. </p>
<p>Where possible, user code should generally look for packages using the <i>basic signature</i>, since that allows the package to be found with either mode. Project maintainers wishing to provide a config package should understand the bigger picture, as explained in <i>Full Signature</i> and all subsequent sections on this page. </p>
 </dd></dl>
<h3>Basic Signature</h3>
<pre><code>find_package(&lt;PackageName&gt; [version] [EXACT] [QUIET] [MODULE]
             [REQUIRED] [[COMPONENTS] [components...]]
             [OPTIONAL_COMPONENTS components...]
             [NO_POLICY_SCOPE])
</code></pre>
<p>The basic signature is supported by both Module and Config modes. The <code>MODULE</code> keyword implies that only Module mode can be used to find the package, with no fallback to Config mode. </p>
<p>Regardless of the mode used, a <code>&lt;PackageName&gt;_FOUND</code> variable will be set to indicate whether the package was found. When the package is found, package-specific information may be provided through other variables and Imported Targets documented by the package itself. The <code>QUIET</code> option disables informational messages, including those indicating that the package cannot be found if it is not <code>REQUIRED</code>. The <code>REQUIRED</code> option stops processing with an error message if the package cannot be found. </p>
<p>A package-specific list of required components may be listed after the <code>COMPONENTS</code> keyword. If any of these components are not able to be satisfied, the package overall is considered to be not found. If the <code>REQUIRED</code> option is also present, this is treated as a fatal error, otherwise execution still continues. As a form of shorthand, if the <code>REQUIRED</code> option is present, the <code>COMPONENTS</code> keyword can be omitted and the required components can be listed directly after <code>REQUIRED</code>. </p>
<p>Additional optional components may be listed after <code>OPTIONAL_COMPONENTS</code>. If these cannot be satisfied, the package overall can still be considered found, as long as all required components are satisfied. </p>
<p>The set of available components and their meaning are defined by the target package. Formally, it is up to the target package how to interpret the component information given to it, but it should follow the expectations stated above. For calls where no components are specified, there is no single expected behavior and target packages should clearly define what occurs in such cases. Common arrangements include assuming it should find all components, no components or some well-defined subset of the available components. </p>
<p>The <code>[version]</code> argument requests a version with which the package found should be compatible. There are two possible forms in which it may be specified: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> A single version with the format <code>major[.minor[.patch[.tweak]]]</code>, where each component is a numeric value. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A version range with the format <code>versionMin...[&lt;]versionMax</code> where <code>versionMin</code> and <code>versionMax</code> have the same format and constraints on components being integers as the single version. By default, both end points are included. By specifying <code>&lt;</code>, the upper end point will be excluded. Version ranges are only supported with CMake 3.19 or later. </p>
<p>The <code>EXACT</code> option requests that the version be matched exactly. This option is incompatible with the specification of a version range. </p>
<p>If no <code>[version]</code> and/or component list is given to a recursive invocation inside a find-module, the corresponding arguments are forwarded automatically from the outer call (including the <code>EXACT</code> flag for <code>[version]</code>). Version support is currently provided only on a package-by-package basis (see the <i>Version Selection</i> section below). When a version range is specified but the package is only designed to expect a single version, the package will ignore the upper end point of the range and only take the single version at the lower end of the range into account. </p>
<p>See the <code>cmake_policy()</code> command documentation for discussion of the <code>NO_POLICY_SCOPE</code> option. </p>
 </dd></dl>
<h3>Full Signature</h3>
<pre><code>find_package(&lt;PackageName&gt; [version] [EXACT] [QUIET]
             [REQUIRED] [[COMPONENTS] [components...]]
             [OPTIONAL_COMPONENTS components...]
             [CONFIG|NO_MODULE]
             [NO_POLICY_SCOPE]
             [NAMES name1 [name2 ...]]
             [CONFIGS config1 [config2 ...]]
             [HINTS path1 [path2 ... ]]
             [PATHS path1 [path2 ... ]]
             [PATH_SUFFIXES suffix1 [suffix2 ...]]
             [NO_DEFAULT_PATH]
             [NO_PACKAGE_ROOT_PATH]
             [NO_CMAKE_PATH]
             [NO_CMAKE_ENVIRONMENT_PATH]
             [NO_SYSTEM_ENVIRONMENT_PATH]
             [NO_CMAKE_PACKAGE_REGISTRY]
             [NO_CMAKE_BUILDS_PATH] # Deprecated; does nothing.
             [NO_CMAKE_SYSTEM_PATH]
             [NO_CMAKE_SYSTEM_PACKAGE_REGISTRY]
             [CMAKE_FIND_ROOT_PATH_BOTH |
              ONLY_CMAKE_FIND_ROOT_PATH |
              NO_CMAKE_FIND_ROOT_PATH])
</code></pre>
<p>The <code>CONFIG</code> option, the synonymous <code>NO_MODULE</code> option, or the use of options not specified in the <i>basic signature</i> all enforce pure Config mode. In pure Config mode, the command skips Module mode search and proceeds at once with Config mode search. </p>
<p>Config mode search attempts to locate a configuration file provided by the package to be found. A cache entry called <code>&lt;PackageName&gt;_DIR</code> is created to hold the directory containing the file. By default the command searches for a package with the name <code>&lt;PackageName&gt;</code>. If the <code>NAMES</code> option is given the names following it are used instead of <code>&lt;PackageName&gt;</code>. The command searches for a file called <code>&lt;PackageName&gt;Config.cmake</code> or <code>&lt;lowercasePackageName&gt;-config.cmake</code> for each name specified. A replacement set of possible configuration file names may be given using the <code>CONFIGS</code> option. The <i>Config Mode Search Procedure</i> is specified below. Once found, any <i>version constraint</i> is checked, and if satisfied, the configuration file is read and processed by CMake. Since the file is provided by the package it already knows the location of package contents. The full path to the configuration file is stored in the cmake variable <code>&lt;PackageName&gt;_CONFIG</code>. </p>
<p>All configuration files which have been considered by CMake while searching for the package with an appropriate version are stored in the <code>&lt;PackageName&gt;_CONSIDERED_CONFIGS</code> variable, and the associated versions in the <code>&lt;PackageName&gt;_CONSIDERED_VERSIONS</code> variable. </p>
<p>If the package configuration file cannot be found CMake will generate an error describing the problem unless the <code>QUIET</code> argument is specified. If <code>REQUIRED</code> is specified and the package is not found a fatal error is generated and the configure step stops executing. If <code>&lt;PackageName&gt;_DIR</code> has been set to a directory not containing a configuration file CMake will ignore it and search from scratch. </p>
<p>Package maintainers providing CMake package configuration files are encouraged to name and install them such that the <i>Config Mode Search Procedure</i> outlined below will find them without requiring use of additional options.  </p>
<h3>Config Mode Search Procedure</h3>
<p> <code>NOTE:</code> When Config mode is used, this search procedure is applied regardless of whether the <i>full</i> or <i>basic</i> signature was given. </p>
<p>CMake constructs a set of possible installation prefixes for the package. Under each prefix several directories are searched for a configuration file. The tables below show the directories searched. Each entry is meant for installation trees following Windows (<code>W</code>), UNIX (<code>U</code>), or Apple (<code>A</code>) conventions: </p>
<pre><code>&lt;prefix&gt;/ (W)
&lt;prefix&gt;/(cmake|CMake)/ (W)
&lt;prefix&gt;/&lt;name&gt;*/ (W)
&lt;prefix&gt;/&lt;name&gt;*/(cmake|CMake)/ (W)
&lt;prefix&gt;/(lib/&lt;arch&gt;|lib*|share)/cmake/&lt;name&gt;*/ (U)
&lt;prefix&gt;/(lib/&lt;arch&gt;|lib*|share)/&lt;name&gt;*/ (U)
&lt;prefix&gt;/(lib/&lt;arch&gt;|lib*|share)/&lt;name&gt;*/(cmake|CMake)/ (U)
&lt;prefix&gt;/&lt;name&gt;*/(lib/&lt;arch&gt;|lib*|share)/cmake/&lt;name&gt;*/ (W/U)
&lt;prefix&gt;/&lt;name&gt;*/(lib/&lt;arch&gt;|lib*|share)/&lt;name&gt;*/ (W/U)
&lt;prefix&gt;/&lt;name&gt;*/(lib/&lt;arch&gt;|lib*|share)/&lt;name&gt;*/(cmake|CMake)/ (W/U)
</code></pre>
<p>On systems supporting macOS <code>FRAMEWORK</code> and <code>BUNDLE</code>, the following directories are searched for Frameworks or Application Bundles containing a configuration file: </p>
<pre><code>&lt;prefix&gt;/&lt;name&gt;.framework/Resources/ (A)
&lt;prefix&gt;/&lt;name&gt;.framework/Resources/CMake/ (A)
&lt;prefix&gt;/&lt;name&gt;.framework/Versions/*/Resources/ (A)
&lt;prefix&gt;/&lt;name&gt;.framework/Versions/*/Resources/CMake/ (A)
&lt;prefix&gt;/&lt;name&gt;.app/Contents/Resources/ (A)
&lt;prefix&gt;/&lt;name&gt;.app/Contents/Resources/CMake/ (A)
</code></pre>
<p>In all cases the <code>&lt;name&gt;</code> is treated as case-insensitive and corresponds to any of the names specified (<code>&lt;PackageName&gt;</code> or names given by <code>NAMES</code>). </p>
<p>Paths with <code>lib/&lt;arch&gt;</code> are enabled if the <code>CMAKE_LIBRARY_ARCHITECTURE</code> variable is set. <code>lib*</code> includes one or more of the values <code>lib64</code>, <code>lib32</code>, <code>libx32</code> or <code>lib</code> (searched in that order). </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Paths with <code>lib64</code> are searched on 64 bit platforms if the <code>FIND_LIBRARY_USE_LIB64_PATHS</code> property is set to <code>TRUE</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Paths with <code>lib32</code> are searched on 32 bit platforms if the <code>FIND_LIBRARY_USE_LIB32_PATHS</code> property is set to <code>TRUE</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Paths with <code>libx32</code> are searched on platforms using the x32 ABI if the <code>FIND_LIBRARY_USE_LIBX32_PATHS</code> property is set to <code>TRUE</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>lib</code> path is always searched. </p>
<p>If <code>PATH_SUFFIXES</code> is specified, the suffixes are appended to each (<code>W</code>) or (<code>U</code>) directory entry one-by-one. </p>
<p>This set of directories is intended to work in cooperation with projects that provide configuration files in their installation trees. Directories above marked with (<code>W</code>) are intended for installations on Windows where the prefix may point at the top of an application&#8217;s installation directory. Those marked with (<code>U</code>) are intended for installations on UNIX platforms where the prefix is shared by multiple packages. This is merely a convention, so all (<code>W</code>) and (<code>U</code>) directories are still searched on all platforms. Directories marked with (<code>A</code>) are intended for installations on Apple platforms. The <code>CMAKE_FIND_FRAMEWORK</code> and <code>CMAKE_FIND_APPBUNDLE</code> variables determine the order of preference. </p>
<p>The set of installation prefixes is constructed using the following steps. If <code>NO_DEFAULT_PATH</code> is specified all <code>NO_*</code> options are enabled. </p>
 </dd>
<dt>1.</dt>
<dd> <p> New in version 3.12: Search paths specified in the <code>&lt;PackageName&gt;_ROOT</code> CMake variable and the <code>&lt;PackageName&gt;_ROOT</code> environment variable, where <code>&lt;PackageName&gt;</code> is the package to be found. The package root variables are maintained as a stack so if called from within a find module, root paths from the parent&#8217;s find module will also be searched after paths for the current package. This can be skipped if <code>NO_PACKAGE_ROOT_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_PACKAGE_ROOT_PATH</code> to <code>FALSE</code>. See policy <code>CMP0074</code>. </p>
 </dd>
<dt>2.</dt>
<dd> <p> Search paths specified in cmake-specific cache variables. These are intended to be used on the command line with a <code>-DVAR=value</code>. The values are interpreted as semicolon-separated lists. This can be skipped if <code>NO_CMAKE_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_CMAKE_PATH</code> to <code>FALSE</code>: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_PREFIX_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_FRAMEWORK_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_APPBUNDLE_PATH</code> </p>
 </dd>
<dt>3.</dt>
<dd> <p> Search paths specified in cmake-specific environment variables. These are intended to be set in the user&#8217;s shell configuration, and therefore use the host&#8217;s native path separator (<code>;</code> on Windows and <code>:</code> on UNIX). This can be skipped if <code>NO_CMAKE_ENVIRONMENT_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_CMAKE_ENVIRONMENT_PATH</code> to <code>FALSE</code>: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&lt;PackageName&gt;_DIR</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_PREFIX_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_FRAMEWORK_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_APPBUNDLE_PATH</code> </p>
 </dd>
<dt>4.</dt>
<dd> <p> Search paths specified by the <code>HINTS</code> option. These should be paths computed by system introspection, such as a hint provided by the location of another item already found. Hard-coded guesses should be specified with the <code>PATHS</code> option. </p>
 </dd>
<dt>5.</dt>
<dd> <p> Search the standard system environment variables. This can be skipped if <code>NO_SYSTEM_ENVIRONMENT_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_SYSTEM_ENVIRONMENT_PATH</code> to <code>FALSE</code>. Path entries ending in <code>/bin</code> or <code>/sbin</code> are automatically converted to their parent directories: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>PATH</code> </p>
 </dd>
<dt>6.</dt>
<dd> <p> Search paths stored in the CMake User Package Registry. This can be skipped if <code>NO_CMAKE_PACKAGE_REGISTRY</code> is passed or by setting the variable <code>CMAKE_FIND_USE_PACKAGE_REGISTRY</code> to <code>FALSE</code> or the deprecated variable <code>CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY</code> to <code>TRUE</code>. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-packages/">cmake-packages</a>(7)</code> manual for details on the user package registry. </p>
 </dd>
<dt>7.</dt>
<dd> <p> Search cmake variables defined in the Platform files for the current system. This can be skipped if <code>NO_CMAKE_SYSTEM_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_CMAKE_SYSTEM_PATH</code> to <code>FALSE</code>: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_SYSTEM_PREFIX_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_SYSTEM_FRAMEWORK_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_SYSTEM_APPBUNDLE_PATH</code> </p>
<p>The platform paths that these variables contain are locations that typically include installed software. An example being <code>/usr/local</code> for UNIX based platforms. </p>
 </dd>
<dt>8.</dt>
<dd> <p> Search paths stored in the CMake System Package Registry. This can be skipped if <code>NO_CMAKE_SYSTEM_PACKAGE_REGISTRY</code> is passed or by setting the <code>CMAKE_FIND_USE_SYSTEM_PACKAGE_REGISTRY</code> variable to <code>FALSE</code> or the deprecated variable <code>CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY</code> to <code>TRUE</code>. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-packages/">cmake-packages</a>(7)</code> manual for details on the system package registry. </p>
 </dd>
<dt>9.</dt>
<dd> <p> Search paths specified by the <code>PATHS</code> option. These are typically hard-coded guesses. </p>
<p>New in version 3.16: Added the <code>CMAKE_FIND_USE_&lt;CATEGORY&gt;</code> variables to globally disable various search locations. </p>
<p>The CMake variable <code>CMAKE_FIND_ROOT_PATH</code> specifies one or more directories to be prepended to all other search directories. This effectively &quot;re-roots&quot; the entire search under given locations. Paths which are descendants of the <code>CMAKE_STAGING_PREFIX</code> are excluded from this re-rooting, because that variable is always a path on the host system. By default the <code>CMAKE_FIND_ROOT_PATH</code> is empty. </p>
<p>The <code>CMAKE_SYSROOT</code> variable can also be used to specify exactly one directory to use as a prefix. Setting <code>CMAKE_SYSROOT</code> also has other effects. See the documentation for that variable for more. </p>
<p>These variables are especially useful when cross-compiling to point to the root directory of the target environment and CMake will search there too. By default at first the directories listed in <code>CMAKE_FIND_ROOT_PATH</code> are searched, then the <code>CMAKE_SYSROOT</code> directory is searched, and then the non-rooted directories will be searched. The default behavior can be adjusted by setting <code>CMAKE_FIND_ROOT_PATH_MODE_PACKAGE</code>. This behavior can be manually overridden on a per-call basis using options: </p>
 </dd>
<dt><code>CMAKE_FIND_ROOT_PATH_BOTH</code></dt>
<dd> <p> Search in the order described above. </p>
 </dd>
<dt><code>NO_CMAKE_FIND_ROOT_PATH</code></dt>
<dd> <p> Do not use the <code>CMAKE_FIND_ROOT_PATH</code> variable. </p>
 </dd>
<dt><code>ONLY_CMAKE_FIND_ROOT_PATH</code></dt>
<dd> <p> Search only the re-rooted directories and directories below <code>CMAKE_STAGING_PREFIX</code>. </p>
<p>The default search order is designed to be most-specific to least-specific for common use cases. Projects may override the order by simply calling the command multiple times and using the <code>NO_*</code> options: </p>
<pre><code>find_package (&lt;PackageName&gt; PATHS paths... NO_DEFAULT_PATH)
find_package (&lt;PackageName&gt;)
</code></pre>
<p>Once one of the calls succeeds the result variable will be set and stored in the cache so that no call will search again. </p>
<p>By default the value stored in the result variable will be the path at which the file is found. The <code>CMAKE_FIND_PACKAGE_RESOLVE_SYMLINKS</code> variable may be set to <code>TRUE</code> before calling <code>find_package</code> in order to resolve symbolic links and store the real path to the file. </p>
<p>Every non-REQUIRED <code>find_package</code> call can be disabled or made REQUIRED: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Setting the <code>CMAKE_DISABLE_FIND_PACKAGE_&lt;PackageName&gt;</code> variable to <code>TRUE</code> disables the package. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Setting the <code>CMAKE_REQUIRE_FIND_PACKAGE_&lt;PackageName&gt;</code> variable to <code>TRUE</code> makes the package REQUIRED. </p>
<p>Setting both variables to <code>TRUE</code> simultaneously is an error. </p>
 </dd></dl>
<h3>Config Mode Version Selection</h3>
<p> <code>NOTE:</code> When Config mode is used, this version selection process is applied regardless of whether the <i>full</i> or <i>basic</i> signature was given. </p>
<p>When the <code>[version]</code> argument is given, Config mode will only find a version of the package that claims compatibility with the requested version (see <i>format specification</i>). If the <code>EXACT</code> option is given, only a version of the package claiming an exact match of the requested version may be found. CMake does not establish any convention for the meaning of version numbers. Package version numbers are checked by &quot;version&quot; files provided by the packages themselves. For a candidate package configuration file <code>&lt;config-file&gt;.cmake</code> the corresponding version file is located next to it and named either <code>&lt;config-file&gt;-version.cmake</code> or <code>&lt;config-file&gt;Version.cmake</code>. If no such version file is available then the configuration file is assumed to not be compatible with any requested version. A basic version file containing generic version matching code can be created using the <code>CMakePackageConfigHelpers</code> module. When a version file is found it is loaded to check the requested version number. The version file is loaded in a nested scope in which the following variables have been defined: </p>
<dl>
<dt><code>PACKAGE_FIND_NAME</code></dt>
<dd> <p> The <code>&lt;PackageName&gt;</code> </p>
 </dd>
<dt><code>PACKAGE_FIND_VERSION</code></dt>
<dd> <p> Full requested version string </p>
 </dd>
<dt><code>PACKAGE_FIND_VERSION_MAJOR</code></dt>
<dd> <p> Major version if requested, else 0 </p>
 </dd>
<dt><code>PACKAGE_FIND_VERSION_MINOR</code></dt>
<dd> <p> Minor version if requested, else 0 </p>
 </dd>
<dt><code>PACKAGE_FIND_VERSION_PATCH</code></dt>
<dd> <p> Patch version if requested, else 0 </p>
 </dd>
<dt><code>PACKAGE_FIND_VERSION_TWEAK</code></dt>
<dd> <p> Tweak version if requested, else 0 </p>
 </dd>
<dt><code>PACKAGE_FIND_VERSION_COUNT</code></dt>
<dd> <p> Number of version components, 0 to 4 </p>
<p>When a version range is specified, the above version variables will hold values based on the lower end of the version range. This is to preserve compatibility with packages that have not been implemented to expect version ranges. In addition, the version range will be described by the following variables: </p>
 </dd>
<dt><code>PACKAGE_FIND_VERSION_RANGE</code></dt>
<dd> <p> Full requested version range string </p>
 </dd>
<dt><code>PACKAGE_FIND_VERSION_RANGE_MIN</code></dt>
<dd> <p> This specifies whether the lower end point of the version range should be included or excluded. Currently, the only supported value for this variable is <code>INCLUDE</code>. </p>
 </dd>
<dt><code>PACKAGE_FIND_VERSION_RANGE_MAX</code></dt>
<dd> <p> This specifies whether the upper end point of the version range should be included or excluded. The supported values for this variable are <code>INCLUDE</code> and <code>EXCLUDE</code>. </p>
 </dd>
<dt><code>PACKAGE_FIND_VERSION_MIN</code></dt>
<dd> <p> Full requested version string of the lower end point of the range </p>
 </dd>
<dt><code>PACKAGE_FIND_VERSION_MIN_MAJOR</code></dt>
<dd> <p> Major version of the lower end point if requested, else 0 </p>
 </dd>
<dt><code>PACKAGE_FIND_VERSION_MIN_MINOR</code></dt>
<dd> <p> Minor version of the lower end point if requested, else 0 </p>
 </dd>
<dt><code>PACKAGE_FIND_VERSION_MIN_PATCH</code></dt>
<dd> <p> Patch version of the lower end point if requested, else 0 </p>
 </dd>
<dt><code>PACKAGE_FIND_VERSION_MIN_TWEAK</code></dt>
<dd> <p> Tweak version of the lower end point if requested, else 0 </p>
 </dd>
<dt><code>PACKAGE_FIND_VERSION_MIN_COUNT</code></dt>
<dd> <p> Number of version components of the lower end point, 0 to 4 </p>
 </dd>
<dt><code>PACKAGE_FIND_VERSION_MAX</code></dt>
<dd> <p> Full requested version string of the upper end point of the range </p>
 </dd>
<dt><code>PACKAGE_FIND_VERSION_MAX_MAJOR</code></dt>
<dd> <p> Major version of the upper end point if requested, else 0 </p>
 </dd>
<dt><code>PACKAGE_FIND_VERSION_MAX_MINOR</code></dt>
<dd> <p> Minor version of the upper end point if requested, else 0 </p>
 </dd>
<dt><code>PACKAGE_FIND_VERSION_MAX_PATCH</code></dt>
<dd> <p> Patch version of the upper end point if requested, else 0 </p>
 </dd>
<dt><code>PACKAGE_FIND_VERSION_MAX_TWEAK</code></dt>
<dd> <p> Tweak version of the upper end point if requested, else 0 </p>
 </dd>
<dt><code>PACKAGE_FIND_VERSION_MAX_COUNT</code></dt>
<dd> <p> Number of version components of the upper end point, 0 to 4 </p>
<p>Regardless of whether a single version or a version range is specified, the variable <code>PACKAGE_FIND_VERSION_COMPLETE</code> will be defined and will hold the full requested version string as specified. </p>
<p>The version file checks whether it satisfies the requested version and sets these variables: </p>
 </dd>
<dt><code>PACKAGE_VERSION</code></dt>
<dd> <p> Full provided version string </p>
 </dd>
<dt><code>PACKAGE_VERSION_EXACT</code></dt>
<dd> <p> True if version is exact match </p>
 </dd>
<dt><code>PACKAGE_VERSION_COMPATIBLE</code></dt>
<dd> <p> True if version is compatible </p>
 </dd>
<dt><code>PACKAGE_VERSION_UNSUITABLE</code></dt>
<dd> <p> True if unsuitable as any version </p>
<p>These variables are checked by the <code>find_package</code> command to determine whether the configuration file provides an acceptable version. They are not available after the <code>find_package</code> call returns. If the version is acceptable the following variables are set: </p>
 </dd>
<dt><code>&lt;PackageName&gt;_VERSION</code></dt>
<dd> <p> Full provided version string </p>
 </dd>
<dt><code>&lt;PackageName&gt;_VERSION_MAJOR</code></dt>
<dd> <p> Major version if provided, else 0 </p>
 </dd>
<dt><code>&lt;PackageName&gt;_VERSION_MINOR</code></dt>
<dd> <p> Minor version if provided, else 0 </p>
 </dd>
<dt><code>&lt;PackageName&gt;_VERSION_PATCH</code></dt>
<dd> <p> Patch version if provided, else 0 </p>
 </dd>
<dt><code>&lt;PackageName&gt;_VERSION_TWEAK</code></dt>
<dd> <p> Tweak version if provided, else 0 </p>
 </dd>
<dt><code>&lt;PackageName&gt;_VERSION_COUNT</code></dt>
<dd> <p> Number of version components, 0 to 4 </p>
<p>and the corresponding package configuration file is loaded. When multiple package configuration files are available whose version files claim compatibility with the version requested it is unspecified which one is chosen: unless the variable <code>CMAKE_FIND_PACKAGE_SORT_ORDER</code> is set no attempt is made to choose a highest or closest version number. </p>
<p>To control the order in which <code>find_package</code> checks for compatibility use the two variables <code>CMAKE_FIND_PACKAGE_SORT_ORDER</code> and <code>CMAKE_FIND_PACKAGE_SORT_DIRECTION</code>. For instance in order to select the highest version one can set </p>
<pre><code>SET(CMAKE_FIND_PACKAGE_SORT_ORDER NATURAL)
SET(CMAKE_FIND_PACKAGE_SORT_DIRECTION DEC)
</code></pre>
<p>before calling <code>find_package</code>. </p>
 </dd></dl>
<h3>Package File Interface Variables</h3>
<p>When loading a find module or package configuration file <code>find_package</code> defines variables to provide information about the call arguments (and restores their original state before returning): </p>
<dl>
<dt><code>CMAKE_FIND_PACKAGE_NAME</code></dt>
<dd> <p> The <code>&lt;PackageName&gt;</code> which is searched for </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_REQUIRED</code></dt>
<dd> <p> True if <code>REQUIRED</code> option was given </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_QUIETLY</code></dt>
<dd> <p> True if <code>QUIET</code> option was given </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_VERSION</code></dt>
<dd> <p> Full requested version string </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_VERSION_MAJOR</code></dt>
<dd> <p> Major version if requested, else 0 </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_VERSION_MINOR</code></dt>
<dd> <p> Minor version if requested, else 0 </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_VERSION_PATCH</code></dt>
<dd> <p> Patch version if requested, else 0 </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_VERSION_TWEAK</code></dt>
<dd> <p> Tweak version if requested, else 0 </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_VERSION_COUNT</code></dt>
<dd> <p> Number of version components, 0 to 4 </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_VERSION_EXACT</code></dt>
<dd> <p> True if <code>EXACT</code> option was given </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_COMPONENTS</code></dt>
<dd> <p> List of specified components (required and optional) </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_REQUIRED_&lt;c&gt;</code></dt>
<dd> <p> True if component <code>&lt;c&gt;</code> is required, false if component <code>&lt;c&gt;</code> is optional </p>
<p>When a version range is specified, the above version variables will hold values based on the lower end of the version range. This is to preserve compatibility with packages that have not been implemented to expect version ranges. In addition, the version range will be described by the following variables: </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_VERSION_RANGE</code></dt>
<dd> <p> Full requested version range string </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_VERSION_RANGE_MIN</code></dt>
<dd> <p> This specifies whether the lower end point of the version range is included or excluded. Currently, <code>INCLUDE</code> is the only supported value. </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_VERSION_RANGE_MAX</code></dt>
<dd> <p> This specifies whether the upper end point of the version range is included or excluded. The possible values for this variable are <code>INCLUDE</code> or <code>EXCLUDE</code>. </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_VERSION_MIN</code></dt>
<dd> <p> Full requested version string of the lower end point of the range </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_VERSION_MIN_MAJOR</code></dt>
<dd> <p> Major version of the lower end point if requested, else 0 </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_VERSION_MIN_MINOR</code></dt>
<dd> <p> Minor version of the lower end point if requested, else 0 </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_VERSION_MIN_PATCH</code></dt>
<dd> <p> Patch version of the lower end point if requested, else 0 </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_VERSION_MIN_TWEAK</code></dt>
<dd> <p> Tweak version of the lower end point if requested, else 0 </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_VERSION_MIN_COUNT</code></dt>
<dd> <p> Number of version components of the lower end point, 0 to 4 </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_VERSION_MAX</code></dt>
<dd> <p> Full requested version string of the upper end point of the range </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_VERSION_MAX_MAJOR</code></dt>
<dd> <p> Major version of the upper end point if requested, else 0 </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_VERSION_MAX_MINOR</code></dt>
<dd> <p> Minor version of the upper end point if requested, else 0 </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_VERSION_MAX_PATCH</code></dt>
<dd> <p> Patch version of the upper end point if requested, else 0 </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_VERSION_MAX_TWEAK</code></dt>
<dd> <p> Tweak version of the upper end point if requested, else 0 </p>
 </dd>
<dt><code>&lt;PackageName&gt;_FIND_VERSION_MAX_COUNT</code></dt>
<dd> <p> Number of version components of the upper end point, 0 to 4 </p>
<p>Regardless of whether a single version or a version range is specified, the variable <code>&lt;PackageName&gt;_FIND_VERSION_COMPLETE</code> will be defined and will hold the full requested version string as specified. </p>
<p>In Module mode the loaded find module is responsible to honor the request detailed by these variables; see the find module for details. In Config mode <code>find_package</code> handles <code>REQUIRED</code>, <code>QUIET</code>, and <code>[version]</code> options automatically but leaves it to the package configuration file to handle components in a way that makes sense for the package. The package configuration file may set <code>&lt;PackageName&gt;_FOUND</code> to false to tell <code>find_package</code> that component requirements are not satisfied. </p>
 </dd></dl>
<h3>find_path</h3>
<p>A short-hand signature is: </p>
<pre><code>find_path (&lt;VAR&gt; name1 [path1 path2 ...])
</code></pre>
<p>The general signature is: </p>
<pre><code>find_path (
          &lt;VAR&gt;
          name | NAMES name1 [name2 ...]
          [HINTS [path | ENV var]... ]
          [PATHS [path | ENV var]... ]
          [PATH_SUFFIXES suffix1 [suffix2 ...]]
          [DOC &quot;cache documentation string&quot;]
          [NO_CACHE]
          [REQUIRED]
          [NO_DEFAULT_PATH]
          [NO_PACKAGE_ROOT_PATH]
          [NO_CMAKE_PATH]
          [NO_CMAKE_ENVIRONMENT_PATH]
          [NO_SYSTEM_ENVIRONMENT_PATH]
          [NO_CMAKE_SYSTEM_PATH]
          [CMAKE_FIND_ROOT_PATH_BOTH |
           ONLY_CMAKE_FIND_ROOT_PATH |
           NO_CMAKE_FIND_ROOT_PATH]
         )
</code></pre>
<p>This command is used to find a directory containing the named file. A cache entry, or a normal variable if <code>NO_CACHE</code> is specified, named by <code>&lt;VAR&gt;</code> is created to store the result of this command. If the file in a directory is found the result is stored in the variable and the search will not be repeated unless the variable is cleared. If nothing is found, the result will be <code>&lt;VAR&gt;-NOTFOUND</code>. </p>
<p>Options include: </p>
<dl>
<dt><code>NAMES</code></dt>
<dd> <p> Specify one or more possible names for the file in a directory. </p>
<p>When using this to specify names with and without a version suffix, we recommend specifying the unversioned name first so that locally-built packages can be found before those provided by distributions. </p>
 </dd>
<dt><code>HINTS</code>, <code>PATHS</code></dt>
<dd> <p> Specify directories to search in addition to the default locations. The <code>ENV var</code> sub-option reads paths from a system environment variable. </p>
 </dd>
<dt><code>PATH_SUFFIXES</code></dt>
<dd> <p> Specify additional subdirectories to check below each directory location otherwise considered. </p>
 </dd>
<dt><code>DOC</code></dt>
<dd> <p> Specify the documentation string for the <code>&lt;VAR&gt;</code> cache entry. </p>
 </dd>
<dt><code>NO_CACHE</code></dt>
<dd> <p> New in version 3.21. </p>
<p>The result of the search will be stored in a normal variable rather than a cache entry. </p>
<p> <code>NOTE:</code> If the variable is already set before the call (as a normal or cache variable) then the search will not occur. </p>
<p> <code>WARNING:</code> This option should be used with caution because it can greatly increase the cost of repeated configure steps. </p>
 </dd>
<dt><code>REQUIRED</code></dt>
<dd> <p> New in version 3.18. </p>
<p>Stop processing with an error message if nothing is found, otherwise the search will be attempted again the next time find_path is invoked with the same variable. </p>
<p>If <code>NO_DEFAULT_PATH</code> is specified, then no additional paths are added to the search. If <code>NO_DEFAULT_PATH</code> is not specified, the search process is as follows: </p>
 </dd>
<dt>1.</dt>
<dd> <p> New in version 3.12: If called from within a find module or any other script loaded by a call to <code>find_package(&lt;PackageName&gt;)</code>, search prefixes unique to the current package being found. Specifically, look in the <code>&lt;PackageName&gt;_ROOT</code> CMake variable and the <code>&lt;PackageName&gt;_ROOT</code> environment variable. The package root variables are maintained as a stack, so if called from nested find modules or config packages, root paths from the parent&#8217;s find module or config package will be searched after paths from the current module or package. In other words, the search order would be <code>&lt;CurrentPackage&gt;_ROOT</code>, <code>ENV{&lt;CurrentPackage&gt;_ROOT}</code>, <code>&lt;ParentPackage&gt;_ROOT</code>, <code>ENV{&lt;ParentPackage&gt;_ROOT}</code>, etc. This can be skipped if <code>NO_PACKAGE_ROOT_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_PACKAGE_ROOT_PATH</code> to <code>FALSE</code>. See policy <code>CMP0074</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&lt;prefix&gt;/include/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/include</code> for each <code>&lt;prefix&gt;</code> in the <code>&lt;PackageName&gt;_ROOT</code> CMake variable and the <code>&lt;PackageName&gt;_ROOT</code> environment variable if called from within a find module loaded by <code>find_package(&lt;PackageName&gt;)</code> </p>
 </dd>
<dt>2.</dt>
<dd> <p> Search paths specified in cmake-specific cache variables. These are intended to be used on the command line with a <code>-DVAR=value</code>. The values are interpreted as semicolon-separated lists. This can be skipped if <code>NO_CMAKE_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_CMAKE_PATH</code> to <code>FALSE</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&lt;prefix&gt;/include/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/include</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_PREFIX_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_INCLUDE_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_FRAMEWORK_PATH</code> </p>
 </dd>
<dt>3.</dt>
<dd> <p> Search paths specified in cmake-specific environment variables. These are intended to be set in the user&#8217;s shell configuration, and therefore use the host&#8217;s native path separator (<code>;</code> on Windows and <code>:</code> on UNIX). This can be skipped if <code>NO_CMAKE_ENVIRONMENT_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_CMAKE_ENVIRONMENT_PATH</code> to <code>FALSE</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&lt;prefix&gt;/include/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/include</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_PREFIX_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_INCLUDE_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_FRAMEWORK_PATH</code> </p>
 </dd>
<dt>4.</dt>
<dd> <p> Search the paths specified by the <code>HINTS</code> option. These should be paths computed by system introspection, such as a hint provided by the location of another item already found. Hard-coded guesses should be specified with the <code>PATHS</code> option. </p>
 </dd>
<dt>5.</dt>
<dd> <p> Search the standard system environment variables. This can be skipped if <code>NO_SYSTEM_ENVIRONMENT_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_SYSTEM_ENVIRONMENT_PATH</code> to <code>FALSE</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The directories in <code>INCLUDE</code> and <code>PATH</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On Windows hosts: <code>&lt;prefix&gt;/include/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/include</code> for each <code>&lt;prefix&gt;/[s]bin</code> in <code>PATH</code>, and <code>&lt;entry&gt;/include</code> for other entries in <code>PATH</code>. </p>
 </dd>
<dt>6.</dt>
<dd> <p> Search cmake variables defined in the Platform files for the current system. This can be skipped if <code>NO_CMAKE_SYSTEM_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_CMAKE_SYSTEM_PATH</code> to <code>FALSE</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&lt;prefix&gt;/include/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/include</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_SYSTEM_PREFIX_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_SYSTEM_INCLUDE_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_SYSTEM_FRAMEWORK_PATH</code> </p>
<p>The platform paths that these variables contain are locations that typically include installed software. An example being <code>/usr/local</code> for UNIX based platforms. </p>
 </dd>
<dt>7.</dt>
<dd> <p> Search the paths specified by the PATHS option or in the short-hand version of the command. These are typically hard-coded guesses. </p>
<p>New in version 3.16: Added <code>CMAKE_FIND_USE_&lt;CATEGORY&gt;_PATH</code> variables to globally disable various search locations. </p>
<p>On macOS the <code>CMAKE_FIND_FRAMEWORK</code> and <code>CMAKE_FIND_APPBUNDLE</code> variables determine the order of preference between Apple-style and unix-style package components. </p>
<p>The CMake variable <code>CMAKE_FIND_ROOT_PATH</code> specifies one or more directories to be prepended to all other search directories. This effectively &quot;re-roots&quot; the entire search under given locations. Paths which are descendants of the <code>CMAKE_STAGING_PREFIX</code> are excluded from this re-rooting, because that variable is always a path on the host system. By default the <code>CMAKE_FIND_ROOT_PATH</code> is empty. </p>
<p>The <code>CMAKE_SYSROOT</code> variable can also be used to specify exactly one directory to use as a prefix. Setting <code>CMAKE_SYSROOT</code> also has other effects. See the documentation for that variable for more. </p>
<p>These variables are especially useful when cross-compiling to point to the root directory of the target environment and CMake will search there too. By default at first the directories listed in <code>CMAKE_FIND_ROOT_PATH</code> are searched, then the <code>CMAKE_SYSROOT</code> directory is searched, and then the non-rooted directories will be searched. The default behavior can be adjusted by setting <code>CMAKE_FIND_ROOT_PATH_MODE_INCLUDE</code>. This behavior can be manually overridden on a per-call basis using options: </p>
 </dd>
<dt><code>CMAKE_FIND_ROOT_PATH_BOTH</code></dt>
<dd> <p> Search in the order described above. </p>
 </dd>
<dt><code>NO_CMAKE_FIND_ROOT_PATH</code></dt>
<dd> <p> Do not use the <code>CMAKE_FIND_ROOT_PATH</code> variable. </p>
 </dd>
<dt><code>ONLY_CMAKE_FIND_ROOT_PATH</code></dt>
<dd> <p> Search only the re-rooted directories and directories below <code>CMAKE_STAGING_PREFIX</code>. </p>
<p>The default search order is designed to be most-specific to least-specific for common use cases. Projects may override the order by simply calling the command multiple times and using the <code>NO_*</code> options: </p>
<pre><code>find_path (&lt;VAR&gt; NAMES name PATHS paths... NO_DEFAULT_PATH)
find_path (&lt;VAR&gt; NAMES name)
</code></pre>
<p>Once one of the calls succeeds the result variable will be set and stored in the cache so that no call will search again. </p>
<p>When searching for frameworks, if the file is specified as <code>A/b.h</code>, then the framework search will look for <code>A.framework/Headers/b.h</code>. If that is found the path will be set to the path to the framework. CMake will convert this to the correct <code>-F</code> option to include the file. </p>
 </dd></dl>
<h3>find_program</h3>
<p>A short-hand signature is: </p>
<pre><code>find_program (&lt;VAR&gt; name1 [path1 path2 ...])
</code></pre>
<p>The general signature is: </p>
<pre><code>find_program (
          &lt;VAR&gt;
          name | NAMES name1 [name2 ...] [NAMES_PER_DIR]
          [HINTS [path | ENV var]... ]
          [PATHS [path | ENV var]... ]
          [PATH_SUFFIXES suffix1 [suffix2 ...]]
          [DOC &quot;cache documentation string&quot;]
          [NO_CACHE]
          [REQUIRED]
          [NO_DEFAULT_PATH]
          [NO_PACKAGE_ROOT_PATH]
          [NO_CMAKE_PATH]
          [NO_CMAKE_ENVIRONMENT_PATH]
          [NO_SYSTEM_ENVIRONMENT_PATH]
          [NO_CMAKE_SYSTEM_PATH]
          [CMAKE_FIND_ROOT_PATH_BOTH |
           ONLY_CMAKE_FIND_ROOT_PATH |
           NO_CMAKE_FIND_ROOT_PATH]
         )
</code></pre>
<p>This command is used to find a program. A cache entry, or a normal variable if <code>NO_CACHE</code> is specified, named by <code>&lt;VAR&gt;</code> is created to store the result of this command. If the program is found the result is stored in the variable and the search will not be repeated unless the variable is cleared. If nothing is found, the result will be <code>&lt;VAR&gt;-NOTFOUND</code>. </p>
<p>Options include: </p>
<dl>
<dt><code>NAMES</code></dt>
<dd> <p> Specify one or more possible names for the program. </p>
<p>When using this to specify names with and without a version suffix, we recommend specifying the unversioned name first so that locally-built packages can be found before those provided by distributions. </p>
 </dd>
<dt><code>HINTS</code>, <code>PATHS</code></dt>
<dd> <p> Specify directories to search in addition to the default locations. The <code>ENV var</code> sub-option reads paths from a system environment variable. </p>
 </dd>
<dt><code>PATH_SUFFIXES</code></dt>
<dd> <p> Specify additional subdirectories to check below each directory location otherwise considered. </p>
 </dd>
<dt><code>DOC</code></dt>
<dd> <p> Specify the documentation string for the <code>&lt;VAR&gt;</code> cache entry. </p>
 </dd>
<dt><code>NO_CACHE</code></dt>
<dd> <p> New in version 3.21. </p>
<p>The result of the search will be stored in a normal variable rather than a cache entry. </p>
<p> <code>NOTE:</code> If the variable is already set before the call (as a normal or cache variable) then the search will not occur. </p>
<p> <code>WARNING:</code> This option should be used with caution because it can greatly increase the cost of repeated configure steps. </p>
 </dd>
<dt><code>REQUIRED</code></dt>
<dd> <p> New in version 3.18. </p>
<p>Stop processing with an error message if nothing is found, otherwise the search will be attempted again the next time find_program is invoked with the same variable. </p>
<p>If <code>NO_DEFAULT_PATH</code> is specified, then no additional paths are added to the search. If <code>NO_DEFAULT_PATH</code> is not specified, the search process is as follows: </p>
 </dd>
<dt>1.</dt>
<dd> <p> New in version 3.12: If called from within a find module or any other script loaded by a call to <code>find_package(&lt;PackageName&gt;)</code>, search prefixes unique to the current package being found. Specifically, look in the <code>&lt;PackageName&gt;_ROOT</code> CMake variable and the <code>&lt;PackageName&gt;_ROOT</code> environment variable. The package root variables are maintained as a stack, so if called from nested find modules or config packages, root paths from the parent&#8217;s find module or config package will be searched after paths from the current module or package. In other words, the search order would be <code>&lt;CurrentPackage&gt;_ROOT</code>, <code>ENV{&lt;CurrentPackage&gt;_ROOT}</code>, <code>&lt;ParentPackage&gt;_ROOT</code>, <code>ENV{&lt;ParentPackage&gt;_ROOT}</code>, etc. This can be skipped if <code>NO_PACKAGE_ROOT_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_PACKAGE_ROOT_PATH</code> to <code>FALSE</code>. See policy <code>CMP0074</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&lt;prefix&gt;/[s]bin</code> for each <code>&lt;prefix&gt;</code> in the <code>&lt;PackageName&gt;_ROOT</code> CMake variable and the <code>&lt;PackageName&gt;_ROOT</code> environment variable if called from within a find module loaded by <code>find_package(&lt;PackageName&gt;)</code> </p>
 </dd>
<dt>2.</dt>
<dd> <p> Search paths specified in cmake-specific cache variables. These are intended to be used on the command line with a <code>-DVAR=value</code>. The values are interpreted as semicolon-separated lists. This can be skipped if <code>NO_CMAKE_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_CMAKE_PATH</code> to <code>FALSE</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&lt;prefix&gt;/[s]bin</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_PREFIX_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_PROGRAM_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_APPBUNDLE_PATH</code> </p>
 </dd>
<dt>3.</dt>
<dd> <p> Search paths specified in cmake-specific environment variables. These are intended to be set in the user&#8217;s shell configuration, and therefore use the host&#8217;s native path separator (<code>;</code> on Windows and <code>:</code> on UNIX). This can be skipped if <code>NO_CMAKE_ENVIRONMENT_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_CMAKE_ENVIRONMENT_PATH</code> to <code>FALSE</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&lt;prefix&gt;/[s]bin</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_PREFIX_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_PROGRAM_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_APPBUNDLE_PATH</code> </p>
 </dd>
<dt>4.</dt>
<dd> <p> Search the paths specified by the <code>HINTS</code> option. These should be paths computed by system introspection, such as a hint provided by the location of another item already found. Hard-coded guesses should be specified with the <code>PATHS</code> option. </p>
 </dd>
<dt>5.</dt>
<dd> <p> Search the standard system environment variables. This can be skipped if <code>NO_SYSTEM_ENVIRONMENT_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_SYSTEM_ENVIRONMENT_PATH</code> to <code>FALSE</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The directories in <code>PATH</code> itself. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On Windows hosts no extra search paths are included </p>
 </dd>
<dt>6.</dt>
<dd> <p> Search cmake variables defined in the Platform files for the current system. This can be skipped if <code>NO_CMAKE_SYSTEM_PATH</code> is passed or by setting the <code>CMAKE_FIND_USE_CMAKE_SYSTEM_PATH</code> to <code>FALSE</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&lt;prefix&gt;/[s]bin</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_SYSTEM_PREFIX_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_SYSTEM_PROGRAM_PATH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_SYSTEM_APPBUNDLE_PATH</code> </p>
<p>The platform paths that these variables contain are locations that typically include installed software. An example being <code>/usr/local</code> for UNIX based platforms. </p>
 </dd>
<dt>7.</dt>
<dd> <p> Search the paths specified by the PATHS option or in the short-hand version of the command. These are typically hard-coded guesses. </p>
<p>New in version 3.16: Added <code>CMAKE_FIND_USE_&lt;CATEGORY&gt;_PATH</code> variables to globally disable various search locations. </p>
<p>On macOS the <code>CMAKE_FIND_FRAMEWORK</code> and <code>CMAKE_FIND_APPBUNDLE</code> variables determine the order of preference between Apple-style and unix-style package components. </p>
<p>The CMake variable <code>CMAKE_FIND_ROOT_PATH</code> specifies one or more directories to be prepended to all other search directories. This effectively &quot;re-roots&quot; the entire search under given locations. Paths which are descendants of the <code>CMAKE_STAGING_PREFIX</code> are excluded from this re-rooting, because that variable is always a path on the host system. By default the <code>CMAKE_FIND_ROOT_PATH</code> is empty. </p>
<p>The <code>CMAKE_SYSROOT</code> variable can also be used to specify exactly one directory to use as a prefix. Setting <code>CMAKE_SYSROOT</code> also has other effects. See the documentation for that variable for more. </p>
<p>These variables are especially useful when cross-compiling to point to the root directory of the target environment and CMake will search there too. By default at first the directories listed in <code>CMAKE_FIND_ROOT_PATH</code> are searched, then the <code>CMAKE_SYSROOT</code> directory is searched, and then the non-rooted directories will be searched. The default behavior can be adjusted by setting <code>CMAKE_FIND_ROOT_PATH_MODE_PROGRAM</code>. This behavior can be manually overridden on a per-call basis using options: </p>
 </dd>
<dt><code>CMAKE_FIND_ROOT_PATH_BOTH</code></dt>
<dd> <p> Search in the order described above. </p>
 </dd>
<dt><code>NO_CMAKE_FIND_ROOT_PATH</code></dt>
<dd> <p> Do not use the <code>CMAKE_FIND_ROOT_PATH</code> variable. </p>
 </dd>
<dt><code>ONLY_CMAKE_FIND_ROOT_PATH</code></dt>
<dd> <p> Search only the re-rooted directories and directories below <code>CMAKE_STAGING_PREFIX</code>. </p>
<p>The default search order is designed to be most-specific to least-specific for common use cases. Projects may override the order by simply calling the command multiple times and using the <code>NO_*</code> options: </p>
<pre><code>find_program (&lt;VAR&gt; NAMES name PATHS paths... NO_DEFAULT_PATH)
find_program (&lt;VAR&gt; NAMES name)
</code></pre>
<p>Once one of the calls succeeds the result variable will be set and stored in the cache so that no call will search again. </p>
<p>When more than one value is given to the <code>NAMES</code> option this command by default will consider one name at a time and search every directory for it. The <code>NAMES_PER_DIR</code> option tells this command to consider one directory at a time and search for all names in it. </p>
 </dd></dl>
<h3>foreach</h3>
<p>Evaluate a group of commands for each value in a list. </p>
<pre><code>foreach(&lt;loop_var&gt; &lt;items&gt;)
  &lt;commands&gt;
endforeach()
</code></pre>
<p>where <code>&lt;items&gt;</code> is a list of items that are separated by semicolon or whitespace. All commands between <code>foreach</code> and the matching <code>endforeach</code> are recorded without being invoked. Once the <code>endforeach</code> is evaluated, the recorded list of commands is invoked once for each item in <code>&lt;items&gt;</code>. At the beginning of each iteration the variable <code>&lt;loop_var&gt;</code> will be set to the value of the current item. </p>
<p>The scope of <code>&lt;loop_var&gt;</code> is restricted to the loop scope. See policy <code>CMP0124</code> for details. </p>
<p>The commands <code>break()</code> and <code>continue()</code> provide means to escape from the normal control flow. </p>
<p>Per legacy, the <code>endforeach()</code> command admits an optional <code>&lt;loop_var&gt;</code> argument. If used, it must be a verbatim repeat of the argument of the opening <code>foreach</code> command. </p>
<pre><code>foreach(&lt;loop_var&gt; RANGE &lt;stop&gt;)
</code></pre>
<p>In this variant, <code>foreach</code> iterates over the numbers 0, 1, ... up to (and including) the nonnegative integer <code>&lt;stop&gt;</code>. </p>
<pre><code>foreach(&lt;loop_var&gt; RANGE &lt;start&gt; &lt;stop&gt; [&lt;step&gt;])
</code></pre>
<p>In this variant, <code>foreach</code> iterates over the numbers from <code>&lt;start&gt;</code> up to at most <code>&lt;stop&gt;</code> in steps of <code>&lt;step&gt;</code>. If <code>&lt;step&gt;</code> is not specified, then the step size is 1. The three arguments <code>&lt;start&gt;</code> <code>&lt;stop&gt;</code> <code>&lt;step&gt;</code> must all be nonnegative integers, and <code>&lt;stop&gt;</code> must not be smaller than <code>&lt;start&gt;</code>; otherwise you enter the danger zone of undocumented behavior that may change in future releases. </p>
<pre><code>foreach(&lt;loop_var&gt; IN [LISTS [&lt;lists&gt;]] [ITEMS [&lt;items&gt;]])
</code></pre>
<p>In this variant, <code>&lt;lists&gt;</code> is a whitespace or semicolon separated list of list-valued variables. The <code>foreach</code> command iterates over each item in each given list. The <code>&lt;items&gt;</code> following the <code>ITEMS</code> keyword are processed as in the first variant of the <code>foreach</code> command. The forms <code>LISTS A</code> and <code>ITEMS ${A}</code> are equivalent. </p>
<p>The following example shows how the <code>LISTS</code> option is processed: </p>
<pre><code>set(A 0;1)
set(B 2 3)
set(C &quot;4 5&quot;)
set(D 6;7 8)
set(E &quot;&quot;)
foreach(X IN LISTS A B C D E)
    message(STATUS &quot;X=${X}&quot;)
endforeach()
</code></pre>
<p>yields </p>
<pre><code>-- X=0
-- X=1
-- X=2
-- X=3
-- X=4 5
-- X=6
-- X=7
-- X=8
</code></pre>
<pre><code>foreach(&lt;loop_var&gt;... IN ZIP_LISTS &lt;lists&gt;)
</code></pre>
<p>New in version 3.17. </p>
<p>In this variant, <code>&lt;lists&gt;</code> is a whitespace or semicolon separated list of list-valued variables. The <code>foreach</code> command iterates over each list simultaneously setting the iteration variables as follows: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> if the only <code>loop_var</code> given, then it sets a series of <code>loop_var_N</code> variables to the current item from the corresponding list; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> if multiple variable names passed, their count should match the lists variables count; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> if any of the lists are shorter, the corresponding iteration variable is not defined for the current iteration. </p>
<pre><code>list(APPEND English one two three four)
list(APPEND Bahasa satu dua tiga)
foreach(num IN ZIP_LISTS English Bahasa)
    message(STATUS &quot;num_0=${num_0}, num_1=${num_1}&quot;)
endforeach()
foreach(en ba IN ZIP_LISTS English Bahasa)
    message(STATUS &quot;en=${en}, ba=${ba}&quot;)
endforeach()
</code></pre>
<p>yields </p>
<pre><code>-- num_0=one, num_1=satu
-- num_0=two, num_1=dua
-- num_0=three, num_1=tiga
-- num_0=four, num_1=
-- en=one, ba=satu
-- en=two, ba=dua
-- en=three, ba=tiga
-- en=four, ba=
</code></pre>
 </dd></dl>
<h3>function</h3>
<p>Start recording a function for later invocation as a command. </p>
<pre><code>function(&lt;name&gt; [&lt;arg1&gt; ...])
  &lt;commands&gt;
endfunction()
</code></pre>
<p>Defines a function named <code>&lt;name&gt;</code> that takes arguments named <code>&lt;arg1&gt;</code>, ... The <code>&lt;commands&gt;</code> in the function definition are recorded; they are not executed until the function is invoked. </p>
<p>Per legacy, the <code>endfunction()</code> command admits an optional <code>&lt;name&gt;</code> argument. If used, it must be a verbatim repeat of the argument of the opening <code>function</code> command. </p>
<p>A function opens a new scope: see <code>set(var PARENT_SCOPE)</code> for details. </p>
<p>See the <code>cmake_policy()</code> command documentation for the behavior of policies inside functions. </p>
<p>See the <code>macro()</code> command documentation for differences between CMake functions and macros.  </p>
<h3>Invocation</h3>
<p>The function invocation is case-insensitive. A function defined as </p>
<pre><code>function(foo)
  &lt;commands&gt;
endfunction()
</code></pre>
<p>can be invoked through any of </p>
<pre><code>foo()
Foo()
FOO()
cmake_language(CALL foo)
</code></pre>
<p>and so on. However, it is strongly recommended to stay with the case chosen in the function definition. Typically functions use all-lowercase names. </p>
<p>New in version 3.18: The <code>cmake_language(CALL ...)</code> command can also be used to invoke the function. </p>
<h3>Arguments</h3>
<p>When the function is invoked, the recorded <code>&lt;commands&gt;</code> are first modified by replacing formal parameters (<code>${arg1}</code>, ...) with the arguments passed, and then invoked as normal commands. </p>
<p>In addition to referencing the formal parameters you can reference the <code>ARGC</code> variable which will be set to the number of arguments passed into the function as well as <code>ARGV0</code>, <code>ARGV1</code>, <code>ARGV2</code>, ... which will have the actual values of the arguments passed in. This facilitates creating functions with optional arguments. </p>
<p>Furthermore, <code>ARGV</code> holds the list of all arguments given to the function and <code>ARGN</code> holds the list of arguments past the last expected argument. Referencing to <code>ARGV#</code> arguments beyond <code>ARGC</code> have undefined behavior. Checking that <code>ARGC</code> is greater than <code>#</code> is the only way to ensure that <code>ARGV#</code> was passed to the function as an extra argument.  </p>
<h3>get_cmake_property</h3>
<p>Get a global property of the CMake instance. </p>
<pre><code>get_cmake_property(&lt;var&gt; &lt;property&gt;)
</code></pre>
<p>Gets a global property from the CMake instance. The value of the <code>&lt;property&gt;</code> is stored in the variable <code>&lt;var&gt;</code>. If the property is not found, <code>&lt;var&gt;</code> will be set to <code>NOTFOUND</code>. See the <code><a href="/docs/linux/man/7-cmake-properties/">cmake-properties</a>(7)</code> manual for available properties. </p>
<p>See also the <code>get_property()</code> command <code>GLOBAL</code> option. </p>
<p>In addition to global properties, this command (for historical reasons) also supports the <code>VARIABLES</code> and <code>MACROS</code> directory properties. It also supports a special <code>COMPONENTS</code> global property that lists the components given to the <code>install()</code> command.  </p>
<h3>get_directory_property</h3>
<p>Get a property of <code>DIRECTORY</code> scope. </p>
<pre><code>get_directory_property(&lt;variable&gt; [DIRECTORY &lt;dir&gt;] &lt;prop-name&gt;)
</code></pre>
<p>Stores a property of directory scope in the named <code>&lt;variable&gt;</code>. </p>
<p>The <code>DIRECTORY</code> argument specifies another directory from which to retrieve the property value instead of the current directory. Relative paths are treated as relative to the current source directory. CMake must already know about the directory, either by having added it through a call to <code>add_subdirectory()</code> or being the top level directory. </p>
<p>New in version 3.19: <code>&lt;dir&gt;</code> may reference a binary directory. </p>
<p>If the property is not defined for the nominated directory scope, an empty string is returned. In the case of <code>INHERITED</code> properties, if the property is not found for the nominated directory scope, the search will chain to a parent scope as described for the <code>define_property()</code> command. </p>
<pre><code>get_directory_property(&lt;variable&gt; [DIRECTORY &lt;dir&gt;]
                       DEFINITION &lt;var-name&gt;)
</code></pre>
<p>Get a variable definition from a directory. This form is useful to get a variable definition from another directory. </p>
<p>See also the more general <code>get_property()</code> command.  </p>
<h3>get_filename_component</h3>
<p>Get a specific component of a full filename. </p>
<p>Changed in version 3.20: This command been superseded by <code>cmake_path()</code> command, except <code>REALPATH</code> now offered by file(REAL_PATH) command and <code>PROGRAM</code> now available in <code>separate_arguments(PROGRAM)</code> command. </p>
<pre><code>get_filename_component(&lt;var&gt; &lt;FileName&gt; &lt;mode&gt; [CACHE])
</code></pre>
<p>Sets <code>&lt;var&gt;</code> to a component of <code>&lt;FileName&gt;</code>, where <code>&lt;mode&gt;</code> is one of: </p>
<pre><code>DIRECTORY = Directory without file name
NAME = File name without directory
EXT = File name longest extension (.b.c from d/a.b.c)
NAME_WE = File name with neither the directory nor the longest extension
LAST_EXT = File name last extension (.c from d/a.b.c)
NAME_WLE = File name with neither the directory nor the last extension
PATH = Legacy alias for DIRECTORY (use for CMake &lt;= 2.8.11)
</code></pre>
<p>New in version 3.14: Added the <code>LAST_EXT</code> and <code>NAME_WLE</code> modes. </p>
<p>Paths are returned with forward slashes and have no trailing slashes. If the optional <code>CACHE</code> argument is specified, the result variable is added to the cache. </p>
<pre><code>get_filename_component(&lt;var&gt; &lt;FileName&gt; &lt;mode&gt; [BASE_DIR &lt;dir&gt;] [CACHE])
</code></pre>
<p>New in version 3.4. </p>
<p>Sets <code>&lt;var&gt;</code> to the absolute path of <code>&lt;FileName&gt;</code>, where <code>&lt;mode&gt;</code> is one of: </p>
<pre><code>ABSOLUTE = Full path to file
REALPATH = Full path to existing file with symlinks resolved
</code></pre>
<p>If the provided <code>&lt;FileName&gt;</code> is a relative path, it is evaluated relative to the given base directory <code>&lt;dir&gt;</code>. If no base directory is provided, the default base directory will be <code>CMAKE_CURRENT_SOURCE_DIR</code>. </p>
<p>Paths are returned with forward slashes and have no trailing slashes. If the optional <code>CACHE</code> argument is specified, the result variable is added to the cache. </p>
<pre><code>get_filename_component(&lt;var&gt; &lt;FileName&gt; PROGRAM [PROGRAM_ARGS &lt;arg_var&gt;] [CACHE])
</code></pre>
<p>The program in <code>&lt;FileName&gt;</code> will be found in the system search path or left as a full path. If <code>PROGRAM_ARGS</code> is present with <code>PROGRAM</code>, then any command-line arguments present in the <code>&lt;FileName&gt;</code> string are split from the program name and stored in <code>&lt;arg_var&gt;</code>. This is used to separate a program name from its arguments in a command line string.  </p>
<h3>get_property</h3>
<p>Get a property. </p>
<pre><code>get_property(&lt;variable&gt;
             &lt;GLOBAL |
              DIRECTORY [&lt;dir&gt;] |
              TARGET &lt;target&gt; |
              SOURCE &lt;source&gt;
                        [DIRECTORY &lt;dir&gt; | TARGET_DIRECTORY &lt;target&gt;] |
              INSTALL &lt;file&gt; |
              TEST &lt;test&gt; |
              CACHE &lt;entry&gt; |
              VARIABLE &gt;
             PROPERTY &lt;name&gt;
             [SET | DEFINED | BRIEF_DOCS | FULL_DOCS])
</code></pre>
<p>Gets one property from one object in a scope. </p>
<p>The first argument specifies the variable in which to store the result. The second argument determines the scope from which to get the property. It must be one of the following: </p>
<dl>
<dt><code>GLOBAL</code></dt>
<dd> <p> Scope is unique and does not accept a name. </p>
 </dd>
<dt><code>DIRECTORY</code></dt>
<dd> <p> Scope defaults to the current directory but another directory (already processed by CMake) may be named by the full or relative path <code>&lt;dir&gt;</code>. Relative paths are treated as relative to the current source directory. See also the <code>get_directory_property()</code> command. </p>
<p>New in version 3.19: <code>&lt;dir&gt;</code> may reference a binary directory. </p>
 </dd>
<dt><code>TARGET</code></dt>
<dd> <p> Scope must name one existing target. See also the <code>get_target_property()</code> command. </p>
 </dd>
<dt><code>SOURCE</code></dt>
<dd> <p> Scope must name one source file. By default, the source file&#8217;s property will be read from the current source directory&#8217;s scope. </p>
<p>New in version 3.18: Directory scope can be overridden with one of the following sub-options: </p>
 </dd>
<dt><code>DIRECTORY &lt;dir&gt;</code></dt>
<dd> <p> The source file property will be read from the <code>&lt;dir&gt;</code> directory&#8217;s scope. CMake must already know about the directory, either by having added it through a call to <code>add_subdirectory()</code> or <code>&lt;dir&gt;</code> being the top level directory. Relative paths are treated as relative to the current source directory. </p>
<p>New in version 3.19: <code>&lt;dir&gt;</code> may reference a binary directory. </p>
 </dd>
<dt><code>TARGET_DIRECTORY &lt;target&gt;</code></dt>
<dd> <p> The source file property will be read from the directory scope in which <code>&lt;target&gt;</code> was created (<code>&lt;target&gt;</code> must therefore already exist). </p>
<p>See also the <code>get_source_file_property()</code> command. </p>
 </dd>
<dt><code>INSTALL</code></dt>
<dd> <p> New in version 3.1. </p>
<p>Scope must name one installed file path. </p>
 </dd>
<dt><code>TEST</code></dt>
<dd> <p> Scope must name one existing test. See also the <code>get_test_property()</code> command. </p>
 </dd>
<dt><code>CACHE</code></dt>
<dd> <p> Scope must name one cache entry. </p>
 </dd>
<dt><code>VARIABLE</code></dt>
<dd> <p> Scope is unique and does not accept a name. </p>
<p>The required <code>PROPERTY</code> option is immediately followed by the name of the property to get. If the property is not set an empty value is returned, although some properties support inheriting from a parent scope if defined to behave that way (see <code>define_property()</code>). </p>
<p>If the <code>SET</code> option is given the variable is set to a boolean value indicating whether the property has been set. If the <code>DEFINED</code> option is given the variable is set to a boolean value indicating whether the property has been defined such as with the <code>define_property()</code> command. </p>
<p>If <code>BRIEF_DOCS</code> or <code>FULL_DOCS</code> is given then the variable is set to a string containing documentation for the requested property. If documentation is requested for a property that has not been defined <code>NOTFOUND</code> is returned. </p>
<p> <code>NOTE:</code> The <code>GENERATED</code> source file property may be globally visible. See its documentation for details. </p>
 </dd></dl>
<h3>if</h3>
<p>Conditionally execute a group of commands.  </p>
<h3>Synopsis</h3>
<pre><code>if(&lt;condition&gt;)
  &lt;commands&gt;
elseif(&lt;condition&gt;) # optional block, can be repeated
  &lt;commands&gt;
else() # optional block
  &lt;commands&gt;
endif()
</code></pre>
<p>Evaluates the <code>condition</code> argument of the <code>if</code> clause according to the <i>Condition syntax</i> described below. If the result is true, then the <code>commands</code> in the <code>if</code> block are executed. Otherwise, optional <code>elseif</code> blocks are processed in the same way. Finally, if no <code>condition</code> is true, <code>commands</code> in the optional <code>else</code> block are executed. </p>
<p>Per legacy, the <code>else()</code> and <code>endif()</code> commands admit an optional <code>&lt;condition&gt;</code> argument. If used, it must be a verbatim repeat of the argument of the opening <code>if</code> command.  </p>
<h3>Condition Syntax</h3>
<p>The following syntax applies to the <code>condition</code> argument of the <code>if</code>, <code>elseif</code> and <code>while()</code> clauses. </p>
<p>Compound conditions are evaluated in the following order of precedence: Innermost parentheses are evaluated first. Next come unary tests such as <i>EXISTS</i>, <i>COMMAND</i>, and <i>DEFINED</i>. Then binary tests such as <i>EQUAL</i>, <i>LESS</i>, <i>LESS_EQUAL</i>, <i>GREATER</i>, <i>GREATER_EQUAL</i>, <i>STREQUAL</i>, <i>STRLESS</i>, <i>STRLESS_EQUAL</i>, <i>STRGREATER</i>, <i>STRGREATER_EQUAL</i>, <i>VERSION_EQUAL</i>, <i>VERSION_LESS</i>, <i>VERSION_LESS_EQUAL</i>, <i>VERSION_GREATER</i>, <i>VERSION_GREATER_EQUAL</i>, and <i>MATCHES</i>. Then the boolean operators in the order <i>NOT</i>, <i>AND</i>, and finally <i>OR</i>.  </p>
<h3>Basic Expressions</h3>
<dl>
<dt><code>if(&lt;constant&gt;)</code></dt>
<dd> <p> True if the constant is <code>1</code>, <code>ON</code>, <code>YES</code>, <code>TRUE</code>, <code>Y</code>, or a non-zero number. False if the constant is <code>0</code>, <code>OFF</code>, <code>NO</code>, <code>FALSE</code>, <code>N</code>, <code>IGNORE</code>, <code>NOTFOUND</code>, the empty string, or ends in the suffix <code>-NOTFOUND</code>. Named boolean constants are case-insensitive. If the argument is not one of these specific constants, it is treated as a variable or string (see <i>Variable Expansion</i> further below) and one of the following two forms applies. </p>
 </dd>
<dt><code>if(&lt;variable&gt;)</code></dt>
<dd> <p> True if given a variable that is defined to a value that is not a false constant. False otherwise, including if the variable is undefined. Note that macro arguments are not variables. Environment variables also cannot be tested this way, e.g. <code>if(ENV{some_var})</code> will always evaluate to false. </p>
 </dd>
<dt><code>if(&lt;string&gt;)</code></dt>
<dd> <p> A quoted string always evaluates to false unless: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The string&#8217;s value is one of the true constants, or </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Policy <code>CMP0054</code> is not set to <code>NEW</code> and the string&#8217;s value happens to be a variable name that is affected by <code>CMP0054</code>&#8216;s behavior. </p>
 </dd></dl>
<h3>Logic Operators</h3>
<dl>
<dt><code>if(NOT &lt;condition&gt;)</code></dt>
<dd> <p> True if the condition is not true. </p>
 </dd>
<dt><code>if(&lt;cond1&gt; AND &lt;cond2&gt;)</code></dt>
<dd> <p> True if both conditions would be considered true individually. </p>
 </dd>
<dt><code>if(&lt;cond1&gt; OR &lt;cond2&gt;)</code></dt>
<dd> <p> True if either condition would be considered true individually. </p>
 </dd>
<dt><code>if((condition) AND (condition OR (condition)))</code></dt>
<dd> <p> The conditions inside the parenthesis are evaluated first and then the remaining condition is evaluated as in the other examples. Where there are nested parenthesis the innermost are evaluated as part of evaluating the condition that contains them. </p>
 </dd></dl>
<h3>Existence Checks</h3>
<dl>
<dt><code>if(COMMAND command-name)</code></dt>
<dd> <p> True if the given name is a command, macro or function that can be invoked. </p>
 </dd>
<dt><code>if(POLICY policy-id)</code></dt>
<dd> <p> True if the given name is an existing policy (of the form <code>CMP&lt;NNNN&gt;</code>). </p>
 </dd>
<dt><code>if(TARGET target-name)</code></dt>
<dd> <p> True if the given name is an existing logical target name created by a call to the <code>add_executable()</code>, <code>add_library()</code>, or <code>add_custom_target()</code> command that has already been invoked (in any directory). </p>
 </dd>
<dt><code>if(TEST test-name)</code></dt>
<dd> <p> New in version 3.3: True if the given name is an existing test name created by the <code>add_test()</code> command. </p>
 </dd>
<dt><code>if(DEFINED &lt;name&gt;|CACHE{&lt;name&gt;}|ENV{&lt;name&gt;})</code></dt>
<dd> <p> True if a variable, cache variable or environment variable with given <code>&lt;name&gt;</code> is defined. The value of the variable does not matter. Note that macro arguments are not variables. </p>
<p>New in version 3.14: Added support for <code>CACHE{&lt;name&gt;}</code> variables. </p>
 </dd>
<dt><code>if(&lt;variable|string&gt; IN_LIST &lt;variable&gt;)</code></dt>
<dd> <p> New in version 3.3: True if the given element is contained in the named list variable. </p>
 </dd></dl>
<h3>File Operations</h3>
<dl>
<dt><code>if(EXISTS path-to-file-or-directory)</code></dt>
<dd> <p> True if the named file or directory exists. Behavior is well-defined only for explicit full paths (a leading <code>~/</code> is not expanded as a home directory and is considered a relative path). Resolves symbolic links, i.e. if the named file or directory is a symbolic link, returns true if the target of the symbolic link exists. </p>
 </dd>
<dt><code>if(file1 IS_NEWER_THAN file2)</code></dt>
<dd> <p> True if <code>file1</code> is newer than <code>file2</code> or if one of the two files doesn&#8217;t exist. Behavior is well-defined only for full paths. If the file time stamps are exactly the same, an <code>IS_NEWER_THAN</code> comparison returns true, so that any dependent build operations will occur in the event of a tie. This includes the case of passing the same file name for both file1 and file2. </p>
 </dd>
<dt><code>if(IS_DIRECTORY path-to-directory)</code></dt>
<dd> <p> True if the given name is a directory. Behavior is well-defined only for full paths. </p>
 </dd>
<dt><code>if(IS_SYMLINK file-name)</code></dt>
<dd> <p> True if the given name is a symbolic link. Behavior is well-defined only for full paths. </p>
 </dd>
<dt><code>if(IS_ABSOLUTE path)</code></dt>
<dd> <p> True if the given path is an absolute path. Note the following special cases: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An empty <code>path</code> evaluates to false. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On Windows hosts, any <code>path</code> that begins with a drive letter and colon (e.g. <code>C:</code>), a forward slash or a backslash will evaluate to true. This means a path like <code>C:no\base\dir</code> will evaluate to true, even though the non-drive part of the path is relative. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On non-Windows hosts, any <code>path</code> that begins with a tilde (<code>~</code>) evaluates to true. </p>
 </dd></dl>
<h3>Comparisons</h3>
<dl>
<dt><code>if(&lt;variable|string&gt; MATCHES regex)</code></dt>
<dd> <p> True if the given string or variable&#8217;s value matches the given regular expression. See Regex Specification for regex format. </p>
<p>New in version 3.9: <code>()</code> groups are captured in <code>CMAKE_MATCH_&lt;n&gt;</code> variables. </p>
 </dd>
<dt><code>if(&lt;variable|string&gt; LESS &lt;variable|string&gt;)</code></dt>
<dd> <p> True if the given string or variable&#8217;s value is a valid number and less than that on the right. </p>
 </dd>
<dt><code>if(&lt;variable|string&gt; GREATER &lt;variable|string&gt;)</code></dt>
<dd> <p> True if the given string or variable&#8217;s value is a valid number and greater than that on the right. </p>
 </dd>
<dt><code>if(&lt;variable|string&gt; EQUAL &lt;variable|string&gt;)</code></dt>
<dd> <p> True if the given string or variable&#8217;s value is a valid number and equal to that on the right. </p>
 </dd>
<dt><code>if(&lt;variable|string&gt; LESS_EQUAL &lt;variable|string&gt;)</code></dt>
<dd> <p> New in version 3.7: True if the given string or variable&#8217;s value is a valid number and less than or equal to that on the right. </p>
 </dd>
<dt><code>if(&lt;variable|string&gt; GREATER_EQUAL &lt;variable|string&gt;)</code></dt>
<dd> <p> New in version 3.7: True if the given string or variable&#8217;s value is a valid number and greater than or equal to that on the right. </p>
 </dd>
<dt><code>if(&lt;variable|string&gt; STRLESS &lt;variable|string&gt;)</code></dt>
<dd> <p> True if the given string or variable&#8217;s value is lexicographically less than the string or variable on the right. </p>
 </dd>
<dt><code>if(&lt;variable|string&gt; STRGREATER &lt;variable|string&gt;)</code></dt>
<dd> <p> True if the given string or variable&#8217;s value is lexicographically greater than the string or variable on the right. </p>
 </dd>
<dt><code>if(&lt;variable|string&gt; STREQUAL &lt;variable|string&gt;)</code></dt>
<dd> <p> True if the given string or variable&#8217;s value is lexicographically equal to the string or variable on the right. </p>
 </dd>
<dt><code>if(&lt;variable|string&gt; STRLESS_EQUAL &lt;variable|string&gt;)</code></dt>
<dd> <p> New in version 3.7: True if the given string or variable&#8217;s value is lexicographically less than or equal to the string or variable on the right. </p>
 </dd>
<dt><code>if(&lt;variable|string&gt; STRGREATER_EQUAL &lt;variable|string&gt;)</code></dt>
<dd> <p> New in version 3.7: True if the given string or variable&#8217;s value is lexicographically greater than or equal to the string or variable on the right. </p>
 </dd></dl>
<h3>Version Comparisons</h3>
<dl>
<dt><code>if(&lt;variable|string&gt; VERSION_LESS &lt;variable|string&gt;)</code></dt>
<dd> <p> Component-wise integer version number comparison (version format is <code>major[.minor[.patch[.tweak]]]</code>, omitted components are treated as zero). Any non-integer version component or non-integer trailing part of a version component effectively truncates the string at that point. </p>
 </dd>
<dt><code>if(&lt;variable|string&gt; VERSION_GREATER &lt;variable|string&gt;)</code></dt>
<dd> <p> Component-wise integer version number comparison (version format is <code>major[.minor[.patch[.tweak]]]</code>, omitted components are treated as zero). Any non-integer version component or non-integer trailing part of a version component effectively truncates the string at that point. </p>
 </dd>
<dt><code>if(&lt;variable|string&gt; VERSION_EQUAL &lt;variable|string&gt;)</code></dt>
<dd> <p> Component-wise integer version number comparison (version format is <code>major[.minor[.patch[.tweak]]]</code>, omitted components are treated as zero). Any non-integer version component or non-integer trailing part of a version component effectively truncates the string at that point. </p>
 </dd>
<dt><code>if(&lt;variable|string&gt; VERSION_LESS_EQUAL &lt;variable|string&gt;)</code></dt>
<dd> <p> New in version 3.7: Component-wise integer version number comparison (version format is <code>major[.minor[.patch[.tweak]]]</code>, omitted components are treated as zero). Any non-integer version component or non-integer trailing part of a version component effectively truncates the string at that point. </p>
 </dd>
<dt><code>if(&lt;variable|string&gt; VERSION_GREATER_EQUAL &lt;variable|string&gt;)</code></dt>
<dd> <p> New in version 3.7: Component-wise integer version number comparison (version format is <code>major[.minor[.patch[.tweak]]]</code>, omitted components are treated as zero). Any non-integer version component or non-integer trailing part of a version component effectively truncates the string at that point. </p>
 </dd></dl>
<h3>Variable Expansion</h3>
<p>The if command was written very early in CMake&#8217;s history, predating the <code>${}</code> variable evaluation syntax, and for convenience evaluates variables named by its arguments as shown in the above signatures. Note that normal variable evaluation with <code>${}</code> applies before the if command even receives the arguments. Therefore code like </p>
<pre><code>set(var1 OFF)
set(var2 &quot;var1&quot;)
if(${var2})
</code></pre>
<p>appears to the if command as </p>
<pre><code>if(var1)
</code></pre>
<p>and is evaluated according to the <code>if(&lt;variable&gt;)</code> case documented above. The result is <code>OFF</code> which is false. However, if we remove the <code>${}</code> from the example then the command sees </p>
<pre><code>if(var2)
</code></pre>
<p>which is true because <code>var2</code> is defined to <code>var1</code> which is not a false constant. </p>
<p>Automatic evaluation applies in the other cases whenever the above-documented condition syntax accepts <code>&lt;variable|string&gt;</code>: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The left hand argument to <code>MATCHES</code> is first checked to see if it is a defined variable, if so the variable&#8217;s value is used, otherwise the original value is used. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If the left hand argument to <code>MATCHES</code> is missing it returns false without error </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Both left and right hand arguments to <code>LESS</code>, <code>GREATER</code>, <code>EQUAL</code>, <code>LESS_EQUAL</code>, and <code>GREATER_EQUAL</code>, are independently tested to see if they are defined variables, if so their defined values are used otherwise the original value is used. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Both left and right hand arguments to <code>STRLESS</code>, <code>STRGREATER</code>, <code>STREQUAL</code>, <code>STRLESS_EQUAL</code>, and <code>STRGREATER_EQUAL</code> are independently tested to see if they are defined variables, if so their defined values are used otherwise the original value is used. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Both left and right hand arguments to <code>VERSION_LESS</code>, <code>VERSION_GREATER</code>, <code>VERSION_EQUAL</code>, <code>VERSION_LESS_EQUAL</code>, and <code>VERSION_GREATER_EQUAL</code> are independently tested to see if they are defined variables, if so their defined values are used otherwise the original value is used. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The right hand argument to <code>NOT</code> is tested to see if it is a boolean constant, if so the value is used, otherwise it is assumed to be a variable and it is dereferenced. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The left and right hand arguments to <code>AND</code> and <code>OR</code> are independently tested to see if they are boolean constants, if so they are used as such, otherwise they are assumed to be variables and are dereferenced. </p>
<p>Changed in version 3.1: To prevent ambiguity, potential variable or keyword names can be specified in a Quoted Argument or a Bracket Argument. A quoted or bracketed variable or keyword will be interpreted as a string and not dereferenced or interpreted. See policy <code>CMP0054</code>. </p>
<p>There is no automatic evaluation for environment or cache Variable References. Their values must be referenced as <code>$ENV{&lt;name&gt;}</code> or <code>$CACHE{&lt;name&gt;}</code> wherever the above-documented condition syntax accepts <code>&lt;variable|string&gt;</code>. </p>
 </dd></dl>
<h3>include</h3>
<p>Load and run CMake code from a file or module. </p>
<pre><code>include(&lt;file|module&gt; [OPTIONAL] [RESULT_VARIABLE &lt;var&gt;]
                      [NO_POLICY_SCOPE])
</code></pre>
<p>Loads and runs CMake code from the file given. Variable reads and writes access the scope of the caller (dynamic scoping). If <code>OPTIONAL</code> is present, then no error is raised if the file does not exist. If <code>RESULT_VARIABLE</code> is given the variable <code>&lt;var&gt;</code> will be set to the full filename which has been included or <code>NOTFOUND</code> if it failed. </p>
<p>If a module is specified instead of a file, the file with name <code>&lt;modulename&gt;.cmake</code> is searched first in <code>CMAKE_MODULE_PATH</code>, then in the CMake module directory. There is one exception to this: if the file which calls <code>include()</code> is located itself in the CMake builtin module directory, then first the CMake builtin module directory is searched and <code>CMAKE_MODULE_PATH</code> afterwards. See also policy <code>CMP0017</code>. </p>
<p>See the <code>cmake_policy()</code> command documentation for discussion of the <code>NO_POLICY_SCOPE</code> option.  </p>
<h3>include_guard</h3>
<p>New in version 3.10. </p>
<p>Provides an include guard for the file currently being processed by CMake. </p>
<pre><code>include_guard([DIRECTORY|GLOBAL])
</code></pre>
<p>Sets up an include guard for the current CMake file (see the <code>CMAKE_CURRENT_LIST_FILE</code> variable documentation). </p>
<p>CMake will end its processing of the current file at the location of the <i>include_guard()</i> command if the current file has already been processed for the applicable scope (see below). This provides functionality similar to the include guards commonly used in source headers or to the <code>#pragma once</code> directive. If the current file has been processed previously for the applicable scope, the effect is as though <code>return()</code> had been called. Do not call this command from inside a function being defined within the current file. </p>
<p>An optional argument specifying the scope of the guard may be provided. Possible values for the option are: </p>
<dl>
<dt><code>DIRECTORY</code></dt>
<dd> <p> The include guard applies within the current directory and below. The file will only be included once within this directory scope, but may be included again by other files outside of this directory (i.e. a parent directory or another directory not pulled in by <code>add_subdirectory()</code> or <code>include()</code> from the current file or its children). </p>
 </dd>
<dt><code>GLOBAL</code></dt>
<dd> <p> The include guard applies globally to the whole build. The current file will only be included once regardless of the scope. </p>
<p>If no arguments given, <code>include_guard</code> has the same scope as a variable, meaning that the include guard effect is isolated by the most recent function scope or current directory if no inner function scopes exist. In this case the command behavior is the same as: </p>
<pre><code>if(__CURRENT_FILE_VAR__)
  return()
endif()
set(__CURRENT_FILE_VAR__ TRUE)
</code></pre>
 </dd></dl>
<h3>list</h3>
<p>List operations.  </p>
<h3>Synopsis</h3>
<pre><code>
 Reading   list( LENGTH  &lt;list&gt; &lt;out-var&gt;)
  list( GET  &lt;list&gt; &lt;element index&gt; [&lt;index&gt; ...] &lt;out-var&gt;)
  list( JOIN  &lt;list&gt; &lt;glue&gt; &lt;out-var&gt;)
  list( SUBLIST  &lt;list&gt; &lt;begin&gt; &lt;length&gt; &lt;out-var&gt;)
 Search   list( FIND  &lt;list&gt; &lt;value&gt; &lt;out-var&gt;)
 Modification   list( APPEND  &lt;list&gt; [&lt;element&gt;...])
  list( FILTER  &lt;list&gt; {INCLUDE | EXCLUDE} REGEX &lt;regex&gt;)
  list( INSERT  &lt;list&gt; &lt;index&gt; [&lt;element&gt;...])
  list( POP_BACK  &lt;list&gt; [&lt;out-var&gt;...])
  list( POP_FRONT  &lt;list&gt; [&lt;out-var&gt;...])
  list( PREPEND  &lt;list&gt; [&lt;element&gt;...])
  list( REMOVE_ITEM  &lt;list&gt; &lt;value&gt;...)
  list( REMOVE_AT  &lt;list&gt; &lt;index&gt;...)
  list( REMOVE_DUPLICATES  &lt;list&gt;)
  list( TRANSFORM  &lt;list&gt; &lt;ACTION&gt; [...])
 Ordering   list( REVERSE  &lt;list&gt;)
  list( SORT  &lt;list&gt; [...])
</code></pre>
<h3>Introduction</h3>
<p>The list subcommands <code>APPEND</code>, <code>INSERT</code>, <code>FILTER</code>, <code>PREPEND</code>, <code>POP_BACK</code>, <code>POP_FRONT</code>, <code>REMOVE_AT</code>, <code>REMOVE_ITEM</code>, <code>REMOVE_DUPLICATES</code>, <code>REVERSE</code> and <code>SORT</code> may create new values for the list within the current CMake variable scope. Similar to the <code>set()</code> command, the LIST command creates new variable values in the current scope, even if the list itself is actually defined in a parent scope. To propagate the results of these operations upwards, use <code>set()</code> with <code>PARENT_SCOPE</code>, <code>set()</code> with <code>CACHE INTERNAL</code>, or some other means of value propagation. </p>
<p> <code>NOTE:</code> A list in cmake is a <code>;</code> separated group of strings. To create a list the set command can be used. For example, <code>set(var a b c d e)</code> creates a list with <code>a;b;c;d;e</code>, and <code>set(var &quot;a b c d e&quot;)</code> creates a string or a list with one item in it. (Note macro arguments are not variables, and therefore cannot be used in LIST commands.) </p>
<p> <code>NOTE:</code> When specifying index values, if <code>&lt;element index&gt;</code> is 0 or greater, it is indexed from the beginning of the list, with 0 representing the first list element. If <code>&lt;element index&gt;</code> is -1 or lesser, it is indexed from the end of the list, with -1 representing the last list element. Be careful when counting with negative indices: they do not start from 0. -0 is equivalent to 0, the first list element.  </p>
<h3>Reading</h3>
<pre><code>list(LENGTH &lt;list&gt; &lt;output variable&gt;)
</code></pre>
<p>Returns the list&#8217;s length. </p>
<pre><code>list(GET &lt;list&gt; &lt;element index&gt; [&lt;element index&gt; ...] &lt;output variable&gt;)
</code></pre>
<p>Returns the list of elements specified by indices from the list. </p>
<pre><code>list(JOIN &lt;list&gt; &lt;glue&gt; &lt;output variable&gt;)
</code></pre>
<p>New in version 3.12. </p>
<p>Returns a string joining all list&#8217;s elements using the glue string. To join multiple strings, which are not part of a list, use <code>JOIN</code> operator from <code>string()</code> command. </p>
<pre><code>list(SUBLIST &lt;list&gt; &lt;begin&gt; &lt;length&gt; &lt;output variable&gt;)
</code></pre>
<p>New in version 3.12. </p>
<p>Returns a sublist of the given list. If <code>&lt;length&gt;</code> is 0, an empty list will be returned. If <code>&lt;length&gt;</code> is -1 or the list is smaller than <code>&lt;begin&gt;+&lt;length&gt;</code> then the remaining elements of the list starting at <code>&lt;begin&gt;</code> will be returned.  </p>
<h3>Search</h3>
<pre><code>list(FIND &lt;list&gt; &lt;value&gt; &lt;output variable&gt;)
</code></pre>
<p>Returns the index of the element specified in the list or -1 if it wasn&#8217;t found.  </p>
<h3>Modification</h3>
<pre><code>list(APPEND &lt;list&gt; [&lt;element&gt; ...])
</code></pre>
<p>Appends elements to the list. </p>
<pre><code>list(FILTER &lt;list&gt; &lt;INCLUDE|EXCLUDE&gt; REGEX &lt;regular_expression&gt;)
</code></pre>
<p>New in version 3.6. </p>
<p>Includes or removes items from the list that match the mode&#8217;s pattern. In <code>REGEX</code> mode, items will be matched against the given regular expression. </p>
<p>For more information on regular expressions look under string(REGEX). </p>
<pre><code>list(INSERT &lt;list&gt; &lt;element_index&gt; &lt;element&gt; [&lt;element&gt; ...])
</code></pre>
<p>Inserts elements to the list to the specified location. </p>
<pre><code>list(POP_BACK &lt;list&gt; [&lt;out-var&gt;...])
</code></pre>
<p>New in version 3.15. </p>
<p>If no variable name is given, removes exactly one element. Otherwise, with <i>N</i> variable names provided, assign the last <i>N</i> elements&#8217; values to the given variables and then remove the last <i>N</i> values from <code>&lt;list&gt;</code>. </p>
<pre><code>list(POP_FRONT &lt;list&gt; [&lt;out-var&gt;...])
</code></pre>
<p>New in version 3.15. </p>
<p>If no variable name is given, removes exactly one element. Otherwise, with <i>N</i> variable names provided, assign the first <i>N</i> elements&#8217; values to the given variables and then remove the first <i>N</i> values from <code>&lt;list&gt;</code>. </p>
<pre><code>list(PREPEND &lt;list&gt; [&lt;element&gt; ...])
</code></pre>
<p>New in version 3.15. </p>
<p>Insert elements to the 0th position in the list. </p>
<pre><code>list(REMOVE_ITEM &lt;list&gt; &lt;value&gt; [&lt;value&gt; ...])
</code></pre>
<p>Removes all instances of the given items from the list. </p>
<pre><code>list(REMOVE_AT &lt;list&gt; &lt;index&gt; [&lt;index&gt; ...])
</code></pre>
<p>Removes items at given indices from the list. </p>
<pre><code>list(REMOVE_DUPLICATES &lt;list&gt;)
</code></pre>
<p>Removes duplicated items in the list. The relative order of items is preserved, but if duplicates are encountered, only the first instance is preserved. </p>
<pre><code>list(TRANSFORM &lt;list&gt; &lt;ACTION&gt; [&lt;SELECTOR&gt;]
                      [OUTPUT_VARIABLE &lt;output variable&gt;])
</code></pre>
<p>New in version 3.12. </p>
<p>Transforms the list by applying an action to all or, by specifying a <code>&lt;SELECTOR&gt;</code>, to the selected elements of the list, storing the result in-place or in the specified output variable. </p>
<p> <code>NOTE:</code> The <code>TRANSFORM</code> sub-command does not change the number of elements in the list. If a <code>&lt;SELECTOR&gt;</code> is specified, only some elements will be changed, the other ones will remain the same as before the transformation. </p>
<p> <code>&lt;ACTION&gt;</code> specifies the action to apply to the elements of the list. The actions have exactly the same semantics as sub-commands of the <code>string()</code> command. <code>&lt;ACTION&gt;</code> must be one of the following: </p>
<p> <code>APPEND</code>, <code>PREPEND</code>: Append, prepend specified value to each element of the list. </p>
<pre><code>list(TRANSFORM &lt;list&gt; &lt;APPEND|PREPEND&gt; &lt;value&gt; ...)
</code></pre>
<p> <code>TOUPPER</code>, <code>TOLOWER</code>: Convert each element of the list to upper, lower characters. </p>
<pre><code>list(TRANSFORM &lt;list&gt; &lt;TOLOWER|TOUPPER&gt; ...)
</code></pre>
<p> <code>STRIP</code>: Remove leading and trailing spaces from each element of the list. </p>
<pre><code>list(TRANSFORM &lt;list&gt; STRIP ...)
</code></pre>
<p> <code>GENEX_STRIP</code>: Strip any <code>generator expressions</code> from each element of the list. </p>
<pre><code>list(TRANSFORM &lt;list&gt; GENEX_STRIP ...)
</code></pre>
<p> <code>REPLACE</code>: Match the regular expression as many times as possible and substitute the replacement expression for the match for each element of the list (Same semantic as <code>REGEX REPLACE</code> from <code>string()</code> command). </p>
<pre><code>list(TRANSFORM &lt;list&gt; REPLACE &lt;regular_expression&gt;
                              &lt;replace_expression&gt; ...)
</code></pre>
<p> <code>&lt;SELECTOR&gt;</code> determines which elements of the list will be transformed. Only one type of selector can be specified at a time. When given, <code>&lt;SELECTOR&gt;</code> must be one of the following: </p>
<p> <code>AT</code>: Specify a list of indexes. </p>
<pre><code>list(TRANSFORM &lt;list&gt; &lt;ACTION&gt; AT &lt;index&gt; [&lt;index&gt; ...] ...)
</code></pre>
<p> <code>FOR</code>: Specify a range with, optionally, an increment used to iterate over the range. </p>
<pre><code>list(TRANSFORM &lt;list&gt; &lt;ACTION&gt; FOR &lt;start&gt; &lt;stop&gt; [&lt;step&gt;] ...)
</code></pre>
<p> <code>REGEX</code>: Specify a regular expression. Only elements matching the regular expression will be transformed. </p>
<pre><code>list(TRANSFORM &lt;list&gt; &lt;ACTION&gt; REGEX &lt;regular_expression&gt; ...)
</code></pre>
<h3>Ordering</h3>
<pre><code>list(REVERSE &lt;list&gt;)
</code></pre>
<p>Reverses the contents of the list in-place. </p>
<pre><code>list(SORT &lt;list&gt; [COMPARE &lt;compare&gt;] [CASE &lt;case&gt;] [ORDER &lt;order&gt;])
</code></pre>
<p>Sorts the list in-place alphabetically. </p>
<p>New in version 3.13: Added the <code>COMPARE</code>, <code>CASE</code>, and <code>ORDER</code> options. </p>
<p>New in version 3.18: Added the <code>COMPARE NATURAL</code> option. </p>
<p>Use the <code>COMPARE</code> keyword to select the comparison method for sorting. The <code>&lt;compare&gt;</code> option should be one of: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>STRING</code>: Sorts a list of strings alphabetically. This is the default behavior if the <code>COMPARE</code> option is not given. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>FILE_BASENAME</code>: Sorts a list of pathnames of files by their basenames. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>NATURAL</code>: Sorts a list of strings using natural order (see <code><a href="/docs/linux/man/3-strverscmp/">strverscmp</a>(3)</code> manual), i.e. such that contiguous digits are compared as whole numbers. For example: the following list <i>10.0 1.1 2.1 8.0 2.0 3.1</i> will be sorted as <i>1.1 2.0 2.1 3.1 8.0 10.0</i> if the <code>NATURAL</code> comparison is selected where it will be sorted as <i>1.1 10.0 2.0 2.1 3.1 8.0</i> with the <code>STRING</code> comparison. </p>
<p>Use the <code>CASE</code> keyword to select a case sensitive or case insensitive sort mode. The <code>&lt;case&gt;</code> option should be one of: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>SENSITIVE</code>: List items are sorted in a case-sensitive manner. This is the default behavior if the <code>CASE</code> option is not given. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>INSENSITIVE</code>: List items are sorted case insensitively. The order of items which differ only by upper/lowercase is not specified. </p>
<p>To control the sort order, the <code>ORDER</code> keyword can be given. The <code>&lt;order&gt;</code> option should be one of: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>ASCENDING</code>: Sorts the list in ascending order. This is the default behavior when the <code>ORDER</code> option is not given. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>DESCENDING</code>: Sorts the list in descending order. </p>
 </dd></dl>
<h3>macro</h3>
<p>Start recording a macro for later invocation as a command </p>
<pre><code>macro(&lt;name&gt; [&lt;arg1&gt; ...])
  &lt;commands&gt;
endmacro()
</code></pre>
<p>Defines a macro named <code>&lt;name&gt;</code> that takes arguments named <code>&lt;arg1&gt;</code>, ... Commands listed after macro, but before the matching <code>endmacro()</code>, are not executed until the macro is invoked. </p>
<p>Per legacy, the <code>endmacro()</code> command admits an optional <code>&lt;name&gt;</code> argument. If used, it must be a verbatim repeat of the argument of the opening <code>macro</code> command. </p>
<p>See the <code>cmake_policy()</code> command documentation for the behavior of policies inside macros. </p>
<p>See the <i>Macro vs Function</i> section below for differences between CMake macros and <code>functions</code>.  </p>
<h3>Invocation</h3>
<p>The macro invocation is case-insensitive. A macro defined as </p>
<pre><code>macro(foo)
  &lt;commands&gt;
endmacro()
</code></pre>
<p>can be invoked through any of </p>
<pre><code>foo()
Foo()
FOO()
cmake_language(CALL foo)
</code></pre>
<p>and so on. However, it is strongly recommended to stay with the case chosen in the macro definition. Typically macros use all-lowercase names. </p>
<p>New in version 3.18: The <code>cmake_language(CALL ...)</code> command can also be used to invoke the macro. </p>
<h3>Arguments</h3>
<p>When a macro is invoked, the commands recorded in the macro are first modified by replacing formal parameters (<code>${arg1}</code>, ...) with the arguments passed, and then invoked as normal commands. </p>
<p>In addition to referencing the formal parameters you can reference the values <code>${ARGC}</code> which will be set to the number of arguments passed into the function as well as <code>${ARGV0}</code>, <code>${ARGV1}</code>, <code>${ARGV2}</code>, ... which will have the actual values of the arguments passed in. This facilitates creating macros with optional arguments. </p>
<p>Furthermore, <code>${ARGV}</code> holds the list of all arguments given to the macro and <code>${ARGN}</code> holds the list of arguments past the last expected argument. Referencing to <code>${ARGV#}</code> arguments beyond <code>${ARGC}</code> have undefined behavior. Checking that <code>${ARGC}</code> is greater than <code>#</code> is the only way to ensure that <code>${ARGV#}</code> was passed to the function as an extra argument.  </p>
<h3>Macro vs Function</h3>
<p>The <code>macro</code> command is very similar to the <code>function()</code> command. Nonetheless, there are a few important differences. </p>
<p>In a function, <code>ARGN</code>, <code>ARGC</code>, <code>ARGV</code> and <code>ARGV0</code>, <code>ARGV1</code>, ... are true variables in the usual CMake sense. In a macro, they are not, they are string replacements much like the C preprocessor would do with a macro. This has a number of consequences, as explained in the <i>Argument Caveats</i> section below. </p>
<p>Another difference between macros and functions is the control flow. A function is executed by transferring control from the calling statement to the function body. A macro is executed as if the macro body were pasted in place of the calling statement. This has the consequence that a <code>return()</code> in a macro body does not just terminate execution of the macro; rather, control is returned from the scope of the macro call. To avoid confusion, it is recommended to avoid <code>return()</code> in macros altogether. </p>
<p>Unlike a function, the <code>CMAKE_CURRENT_FUNCTION</code>, <code>CMAKE_CURRENT_FUNCTION_LIST_DIR</code>, <code>CMAKE_CURRENT_FUNCTION_LIST_FILE</code>, <code>CMAKE_CURRENT_FUNCTION_LIST_LINE</code> variables are not set for a macro.  </p>
<h3>Argument Caveats</h3>
<p>Since <code>ARGN</code>, <code>ARGC</code>, <code>ARGV</code>, <code>ARGV0</code> etc. are not variables, you will NOT be able to use commands like </p>
<pre><code>if(ARGV1) # ARGV1 is not a variable
if(DEFINED ARGV2) # ARGV2 is not a variable
if(ARGC GREATER 2) # ARGC is not a variable
foreach(loop_var IN LISTS ARGN) # ARGN is not a variable
</code></pre>
<p>In the first case, you can use <code>if(${ARGV1})</code>. In the second and third case, the proper way to check if an optional variable was passed to the macro is to use <code>if(${ARGC} GREATER 2)</code>. In the last case, you can use <code>foreach(loop_var ${ARGN})</code> but this will skip empty arguments. If you need to include them, you can use </p>
<pre><code>set(list_var &quot;${ARGN}&quot;)
foreach(loop_var IN LISTS list_var)
</code></pre>
<p>Note that if you have a variable with the same name in the scope from which the macro is called, using unreferenced names will use the existing variable instead of the arguments. For example: </p>
<pre><code>macro(bar)
  foreach(arg IN LISTS ARGN)
    &lt;commands&gt;
  endforeach()
endmacro()
function(foo)
  bar(x y z)
endfunction()
foo(a b c)
</code></pre>
<p>Will loop over <code>a;b;c</code> and not over <code>x;y;z</code> as one might have expected. If you want true CMake variables and/or better CMake scope control you should look at the function command.  </p>
<h3>mark_as_advanced</h3>
<p>Mark cmake cached variables as advanced. </p>
<pre><code>mark_as_advanced([CLEAR|FORCE] &lt;var1&gt; ...)
</code></pre>
<p>Sets the advanced/non-advanced state of the named cached variables. </p>
<p>An advanced variable will not be displayed in any of the cmake GUIs unless the <code>show advanced</code> option is on. In script mode, the advanced/non-advanced state has no effect. </p>
<p>If the keyword <code>CLEAR</code> is given then advanced variables are changed back to unadvanced. If the keyword <code>FORCE</code> is given then the variables are made advanced. If neither <code>FORCE</code> nor <code>CLEAR</code> is specified, new values will be marked as advanced, but if a variable already has an advanced/non-advanced state, it will not be changed. </p>
<p>Changed in version 3.17: Variables passed to this command which are not already in the cache are ignored. See policy <code>CMP0102</code>. </p>
<h3>math</h3>
<p>Evaluate a mathematical expression. </p>
<pre><code>math(EXPR &lt;variable&gt; &quot;&lt;expression&gt;&quot; [OUTPUT_FORMAT &lt;format&gt;])
</code></pre>
<p>Evaluates a mathematical <code>&lt;expression&gt;</code> and sets <code>&lt;variable&gt;</code> to the resulting value. The result of the expression must be representable as a 64-bit signed integer. </p>
<p>The mathematical expression must be given as a string (i.e. enclosed in double quotation marks). An example is <code>&quot;5 * (10 + 13)&quot;</code>. Supported operators are <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>, <code>%</code>, <code>|</code>, <code>&amp;</code>, <code>^</code>, <code>~</code>, <code>&lt;&lt;</code>, <code>&gt;&gt;</code>, and <code>(...)</code>; they have the same meaning as in C code. </p>
<p>New in version 3.13: Hexadecimal numbers are recognized when prefixed with <code>0x</code>, as in C code. </p>
<p>New in version 3.13: The result is formatted according to the option <code>OUTPUT_FORMAT</code>, where <code>&lt;format&gt;</code> is one of </p>
<dl>
<dt><code>HEXADECIMAL</code></dt>
<dd> <p> Hexadecimal notation as in C code, i. e. starting with &quot;0x&quot;. </p>
 </dd>
<dt><code>DECIMAL</code></dt>
<dd> <p> Decimal notation. Which is also used if no <code>OUTPUT_FORMAT</code> option is specified. </p>
<p>For example </p>
<pre><code>math(EXPR value &quot;100 * 0xA&quot; OUTPUT_FORMAT DECIMAL) # value is set to &quot;1000&quot;
math(EXPR value &quot;100 * 0xA&quot; OUTPUT_FORMAT HEXADECIMAL) # value is set to &quot;0x3e8&quot;
</code></pre>
 </dd></dl>
<h3>message</h3>
<p>Log a message.  </p>
<h3>Synopsis</h3>
<pre><code>
 General messages   message([&lt;mode&gt;] &quot;message text&quot; ...)
 Reporting checks   message(&lt;checkState&gt; &quot;message text&quot; ...)
</code></pre>
<h3>General messages</h3>
<pre><code>message([&lt;mode&gt;] &quot;message text&quot; ...)
</code></pre>
<p>Record the specified message text in the log. If more than one message string is given, they are concatenated into a single message with no separator between the strings. </p>
<p>The optional <code>&lt;mode&gt;</code> keyword determines the type of message, which influences the way the message is handled: </p>
<dl>
<dt><code>FATAL_ERROR</code></dt>
<dd> <p> CMake Error, stop processing and generation. </p>
 </dd>
<dt><code>SEND_ERROR</code></dt>
<dd> <p> CMake Error, continue processing, but skip generation. </p>
 </dd>
<dt><code>WARNING</code></dt>
<dd> <p> CMake Warning, continue processing. </p>
 </dd>
<dt><code>AUTHOR_WARNING</code></dt>
<dd> <p> CMake Warning (dev), continue processing. </p>
 </dd>
<dt><code>DEPRECATION</code></dt>
<dd> <p> CMake Deprecation Error or Warning if variable <code>CMAKE_ERROR_DEPRECATED</code> or <code>CMAKE_WARN_DEPRECATED</code> is enabled, respectively, else no message. </p>
 </dd>
<dt><code>(none) or NOTICE</code></dt>
<dd> <p> Important message printed to stderr to attract user&#8217;s attention. </p>
 </dd>
<dt><code>STATUS</code></dt>
<dd> <p> The main interesting messages that project users might be interested in. Ideally these should be concise, no more than a single line, but still informative. </p>
 </dd>
<dt><code>VERBOSE</code></dt>
<dd> <p> Detailed informational messages intended for project users. These messages should provide additional details that won&#8217;t be of interest in most cases, but which may be useful to those building the project when they want deeper insight into what&#8217;s happening. </p>
 </dd>
<dt><code>DEBUG</code></dt>
<dd> <p> Detailed informational messages intended for developers working on the project itself as opposed to users who just want to build it. These messages will not typically be of interest to other users building the project and will often be closely related to internal implementation details. </p>
 </dd>
<dt><code>TRACE</code></dt>
<dd> <p> Fine-grained messages with very low-level implementation details. Messages using this log level would normally only be temporary and would expect to be removed before releasing the project, packaging up the files, etc. </p>
<p>New in version 3.15: Added the <code>NOTICE</code>, <code>VERBOSE</code>, <code>DEBUG</code>, and <code>TRACE</code> levels. </p>
<p>The CMake command-line tool displays <code>STATUS</code> to <code>TRACE</code> messages on stdout with the message preceded by two hyphens and a space. All other message types are sent to stderr and are not prefixed with hyphens. The <code>CMake GUI</code> displays all messages in its log area. The <code>curses interface</code> shows <code>STATUS</code> to <code>TRACE</code> messages one at a time on a status line and other messages in an interactive pop-up box. The <code>--log-level</code> command-line option to each of these tools can be used to control which messages will be shown. </p>
<p>New in version 3.17: To make a log level persist between CMake runs, the <code>CMAKE_MESSAGE_LOG_LEVEL</code> variable can be set instead. Note that the command line option takes precedence over the cache variable. </p>
<p>New in version 3.16: Messages of log levels <code>NOTICE</code> and below will have each line preceded by the content of the <code>CMAKE_MESSAGE_INDENT</code> variable (converted to a single string by concatenating its list items). For <code>STATUS</code> to <code>TRACE</code> messages, this indenting content will be inserted after the hyphens. </p>
<p>New in version 3.17: Messages of log levels <code>NOTICE</code> and below can also have each line preceded with context of the form <code>[some.context.example]</code>. The content between the square brackets is obtained by converting the <code>CMAKE_MESSAGE_CONTEXT</code> list variable to a dot-separated string. The message context will always appear before any indenting content but after any automatically added leading hyphens. By default, message context is not shown, it has to be explicitly enabled by giving the <code>cmake</code> <code>--log-context</code> command-line option or by setting the <code>CMAKE_MESSAGE_CONTEXT_SHOW</code> variable to true. See the <code>CMAKE_MESSAGE_CONTEXT</code> documentation for usage examples. </p>
<p>CMake Warning and Error message text displays using a simple markup language. Non-indented text is formatted in line-wrapped paragraphs delimited by newlines. Indented text is considered pre-formatted. </p>
 </dd></dl>
<h3>Reporting checks</h3>
<p>New in version 3.17. </p>
<p>A common pattern in CMake output is a message indicating the start of some sort of check, followed by another message reporting the result of that check. For example: </p>
<pre><code>message(STATUS &quot;Looking for someheader.h&quot;)
#... do the checks, set checkSuccess with the result
if(checkSuccess)
  message(STATUS &quot;Looking for someheader.h - found&quot;)
else()
  message(STATUS &quot;Looking for someheader.h - not found&quot;)
endif()
</code></pre>
<p>This can be more robustly and conveniently expressed using the <code>CHECK_...</code> keyword form of the <code>message()</code> command: </p>
<pre><code>message(&lt;checkState&gt; &quot;message&quot; ...)
</code></pre>
<p>where <code>&lt;checkState&gt;</code> must be one of the following: </p>
<dl>
<dt><code>CHECK_START</code></dt>
<dd> <p> Record a concise message about the check about to be performed. </p>
 </dd>
<dt><code>CHECK_PASS</code></dt>
<dd> <p> Record a successful result for a check. </p>
 </dd>
<dt><code>CHECK_FAIL</code></dt>
<dd> <p> Record an unsuccessful result for a check. </p>
<p>When recording a check result, the command repeats the message from the most recently started check for which no result has yet been reported, then some separator characters and then the message text provided after the <code>CHECK_PASS</code> or <code>CHECK_FAIL</code> keyword. Check messages are always reported at <code>STATUS</code> log level. </p>
<p>Checks may be nested and every <code>CHECK_START</code> should have exactly one matching <code>CHECK_PASS</code> or <code>CHECK_FAIL</code>. The <code>CMAKE_MESSAGE_INDENT</code> variable can also be used to add indenting to nested checks if desired. For example: </p>
<pre><code>message(CHECK_START &quot;Finding my things&quot;)
list(APPEND CMAKE_MESSAGE_INDENT &quot; &quot;)
unset(missingComponents)
message(CHECK_START &quot;Finding partA&quot;)
# ... do check, assume we find A
message(CHECK_PASS &quot;found&quot;)
message(CHECK_START &quot;Finding partB&quot;)
# ... do check, assume we don't find B
list(APPEND missingComponents B)
message(CHECK_FAIL &quot;not found&quot;)
list(POP_BACK CMAKE_MESSAGE_INDENT)
if(missingComponents)
  message(CHECK_FAIL &quot;missing components: ${missingComponents}&quot;)
else()
  message(CHECK_PASS &quot;all components found&quot;)
endif()
</code></pre>
<p>Output from the above would appear something like the following: </p>
<pre><code>-- Finding my things
-- Finding partA
-- Finding partA - found
-- Finding partB
-- Finding partB - not found
-- Finding my things - missing components: B
</code></pre>
 </dd></dl>
<h3>option</h3>
<p>Provide an option that the user can optionally select. </p>
<pre><code>option(&lt;variable&gt; &quot;&lt;help_text&gt;&quot; [value])
</code></pre>
<p>Provides an option for the user to select as <code>ON</code> or <code>OFF</code>. If no initial <code>&lt;value&gt;</code> is provided, <code>OFF</code> is used. If <code>&lt;variable&gt;</code> is already set as a normal or cache variable, then the command does nothing (see policy <code>CMP0077</code>). </p>
<p>If you have options that depend on the values of other options, see the module help for <code>CMakeDependentOption</code>.  </p>
<h3>return</h3>
<p>Return from a file, directory or function. </p>
<pre><code>return()
</code></pre>
<p>Returns from a file, directory or function. When this command is encountered in an included file (via <code>include()</code> or <code>find_package()</code>), it causes processing of the current file to stop and control is returned to the including file. If it is encountered in a file which is not included by another file, e.g. a <code>CMakeLists.txt</code>, deferred calls scheduled by <code>cmake_language(DEFER)</code> are invoked and control is returned to the parent directory if there is one. If return is called in a function, control is returned to the caller of the function. </p>
<p>Note that a <code>macro</code>, unlike a <code>function</code>, is expanded in place and therefore cannot handle <code>return()</code>.  </p>
<h3>separate_arguments</h3>
<p>Parse command-line arguments into a semicolon-separated list. </p>
<pre><code>separate_arguments(&lt;variable&gt; &lt;mode&gt; [PROGRAM [SEPARATE_ARGS]] &lt;args&gt;)
</code></pre>
<p>Parses a space-separated string <code>&lt;args&gt;</code> into a list of items, and stores this list in semicolon-separated standard form in <code>&lt;variable&gt;</code>. </p>
<p>This function is intended for parsing command-line arguments. The entire command line must be passed as one string in the argument <code>&lt;args&gt;</code>. </p>
<p>The exact parsing rules depend on the operating system. They are specified by the <code>&lt;mode&gt;</code> argument which must be one of the following keywords: </p>
<dl>
<dt><code>UNIX_COMMAND</code></dt>
<dd> <p> Arguments are separated by unquoted whitespace. Both single-quote and double-quote pairs are respected. A backslash escapes the next literal character (<code>\&quot;</code> is <code>&quot;</code>); there are no special escapes (<code>\n</code> is just <code>n</code>). </p>
 </dd>
<dt><code>WINDOWS_COMMAND</code></dt>
<dd> <p> A Windows command-line is parsed using the same syntax the runtime library uses to construct argv at startup. It separates arguments by whitespace that is not double-quoted. Backslashes are literal unless they precede double-quotes. See the MSDN article <i>Parsing C Command-Line Arguments</i> for details. </p>
 </dd>
<dt><code>NATIVE_COMMAND</code></dt>
<dd> <p> New in version 3.9. </p>
<p>Proceeds as in <code>WINDOWS_COMMAND</code> mode if the host system is Windows. Otherwise proceeds as in <code>UNIX_COMMAND</code> mode. </p>
 </dd>
<dt><code>PROGRAM</code></dt>
<dd> <p> New in version 3.19. </p>
<p>The first item in <code>&lt;args&gt;</code> is assumed to be an executable and will be searched in the system search path or left as a full path. If not found, <code>&lt;variable&gt;</code> will be empty. Otherwise, <code>&lt;variable&gt;</code> is a list of 2 elements: </p>
 </dd>
<dt>0.</dt>
<dd> <p> Absolute path of the program </p>
 </dd>
<dt>1.</dt>
<dd> <p> Any command-line arguments present in <code>&lt;args&gt;</code> as a string </p>
<p>For example: </p>
<pre><code>separate_arguments (out UNIX_COMMAND PROGRAM &quot;cc -c main.c&quot;)
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> First element of the list: <code>/path/to/cc</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Second element of the list: <code>&quot; -c main.c&quot;</code> </p>
 </dd>
<dt><code>SEPARATE_ARGS</code></dt>
<dd> <p> When this sub-option of <code>PROGRAM</code> option is specified, command-line arguments will be split as well and stored in <code>&lt;variable&gt;</code>. </p>
<p>For example: </p>
<pre><code>separate_arguments (out UNIX_COMMAND PROGRAM SEPARATE_ARGS &quot;cc -c main.c&quot;)
</code></pre>
<p>The contents of <code>out</code> will be: <code>/path/to/cc;-c;main.c</code> </p>
<pre><code>separate_arguments(&lt;var&gt;)
</code></pre>
<p>Convert the value of <code>&lt;var&gt;</code> to a semi-colon separated list. All spaces are replaced with &#8216;;&#8216;. This helps with generating command lines. </p>
 </dd></dl>
<h3>set</h3>
<p>Set a normal, cache, or environment variable to a given value. See the <a href="/docs/linux/man/7-cmake-language/">cmake-language</a>(7) variables documentation for the scopes and interaction of normal variables and cache entries. </p>
<p>Signatures of this command that specify a <code>&lt;value&gt;...</code> placeholder expect zero or more arguments. Multiple arguments will be joined as a semicolon-separated list to form the actual variable value to be set. Zero arguments will cause normal variables to be unset. See the <code>unset()</code> command to unset variables explicitly.  </p>
<h3>Set Normal Variable</h3>
<pre><code>set(&lt;variable&gt; &lt;value&gt;... [PARENT_SCOPE])
</code></pre>
<p>Sets the given <code>&lt;variable&gt;</code> in the current function or directory scope. </p>
<p>If the <code>PARENT_SCOPE</code> option is given the variable will be set in the scope above the current scope. Each new directory or function creates a new scope. This command will set the value of a variable into the parent directory or calling function (whichever is applicable to the case at hand). The previous state of the variable&#8217;s value stays the same in the current scope (e.g., if it was undefined before, it is still undefined and if it had a value, it is still that value).  </p>
<h3>Set Cache Entry</h3>
<pre><code>set(&lt;variable&gt; &lt;value&gt;... CACHE &lt;type&gt; &lt;docstring&gt; [FORCE])
</code></pre>
<p>Sets the given cache <code>&lt;variable&gt;</code> (cache entry). Since cache entries are meant to provide user-settable values this does not overwrite existing cache entries by default. Use the <code>FORCE</code> option to overwrite existing entries. </p>
<p>The <code>&lt;type&gt;</code> must be specified as one of: </p>
<dl>
<dt><code>BOOL</code></dt>
<dd> <p> Boolean <code>ON/OFF</code> value. <code><a href="/docs/linux/man/1-cmake-gui/">cmake-gui</a>(1)</code> offers a checkbox. </p>
 </dd>
<dt><code>FILEPATH</code></dt>
<dd> <p> Path to a file on disk. <code><a href="/docs/linux/man/1-cmake-gui/">cmake-gui</a>(1)</code> offers a file dialog. </p>
 </dd>
<dt><code>PATH</code></dt>
<dd> <p> Path to a directory on disk. <code><a href="/docs/linux/man/1-cmake-gui/">cmake-gui</a>(1)</code> offers a file dialog. </p>
 </dd>
<dt><code>STRING</code></dt>
<dd> <p> A line of text. <code><a href="/docs/linux/man/1-cmake-gui/">cmake-gui</a>(1)</code> offers a text field or a drop-down selection if the <code>STRINGS</code> cache entry property is set. </p>
 </dd>
<dt><code>INTERNAL</code></dt>
<dd> <p> A line of text. <code><a href="/docs/linux/man/1-cmake-gui/">cmake-gui</a>(1)</code> does not show internal entries. They may be used to store variables persistently across runs. Use of this type implies <code>FORCE</code>. </p>
<p>The <code>&lt;docstring&gt;</code> must be specified as a line of text providing a quick summary of the option for presentation to <code><a href="/docs/linux/man/1-cmake-gui/">cmake-gui</a>(1)</code> users. </p>
<p>If the cache entry does not exist prior to the call or the <code>FORCE</code> option is given then the cache entry will be set to the given value. </p>
<p> <code>NOTE:</code> The content of the cache variable will not be directly accessible if a normal variable of the same name already exists (see rules of variable evaluation). If policy <code>CMP0126</code> is set to <code>OLD</code>, any normal variable binding in the current scope will be removed. </p>
<p>It is possible for the cache entry to exist prior to the call but have no type set if it was created on the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> command line by a user through the <code>-D&lt;var&gt;=&lt;value&gt;</code> option without specifying a type. In this case the <code>set</code> command will add the type. Furthermore, if the <code>&lt;type&gt;</code> is <code>PATH</code> or <code>FILEPATH</code> and the <code>&lt;value&gt;</code> provided on the command line is a relative path, then the <code>set</code> command will treat the path as relative to the current working directory and convert it to an absolute path. </p>
 </dd></dl>
<h3>Set Environment Variable</h3>
<pre><code>set(ENV{&lt;variable&gt;} [&lt;value&gt;])
</code></pre>
<p>Sets an <code>Environment Variable</code> to the given value. Subsequent calls of <code>$ENV{&lt;variable&gt;}</code> will return this new value. </p>
<p>This command affects only the current CMake process, not the process from which CMake was called, nor the system environment at large, nor the environment of subsequent build or test processes. </p>
<p>If no argument is given after <code>ENV{&lt;variable&gt;}</code> or if <code>&lt;value&gt;</code> is an empty string, then this command will clear any existing value of the environment variable. </p>
<p>Arguments after <code>&lt;value&gt;</code> are ignored. If extra arguments are found, then an author warning is issued.  </p>
<h3>set_directory_properties</h3>
<p>Set properties of the current directory and subdirectories. </p>
<pre><code>set_directory_properties(PROPERTIES prop1 value1 [prop2 value2] ...)
</code></pre>
<p>Sets properties of the current directory and its subdirectories in key-value pairs. </p>
<p>See also the <code>set_property(DIRECTORY)</code> command. </p>
<p>See Directory Properties for the list of properties known to CMake and their individual documentation for the behavior of each property.  </p>
<h3>set_property</h3>
<p>Set a named property in a given scope. </p>
<pre><code>set_property(&lt;GLOBAL |
              DIRECTORY [&lt;dir&gt;] |
              TARGET [&lt;target1&gt; ...] |
              SOURCE [&lt;src1&gt; ...]
                        [DIRECTORY &lt;dirs&gt; ...]
                        [TARGET_DIRECTORY &lt;targets&gt; ...] |
              INSTALL [&lt;file1&gt; ...] |
              TEST [&lt;test1&gt; ...] |
              CACHE [&lt;entry1&gt; ...] &gt;
             [APPEND] [APPEND_STRING]
             PROPERTY &lt;name&gt; [&lt;value1&gt; ...])
</code></pre>
<p>Sets one property on zero or more objects of a scope. </p>
<p>The first argument determines the scope in which the property is set. It must be one of the following: </p>
<dl>
<dt><code>GLOBAL</code></dt>
<dd> <p> Scope is unique and does not accept a name. </p>
 </dd>
<dt><code>DIRECTORY</code></dt>
<dd> <p> Scope defaults to the current directory but other directories (already processed by CMake) may be named by full or relative path. Relative paths are treated as relative to the current source directory. See also the <code>set_directory_properties()</code> command. </p>
<p>New in version 3.19: <code>&lt;dir&gt;</code> may reference a binary directory. </p>
 </dd>
<dt><code>TARGET</code></dt>
<dd> <p> Scope may name zero or more existing targets. See also the <code>set_target_properties()</code> command. </p>
 </dd>
<dt><code>SOURCE</code></dt>
<dd> <p> Scope may name zero or more source files. By default, source file properties are only visible to targets added in the same directory (<code>CMakeLists.txt</code>). </p>
<p>New in version 3.18: Visibility can be set in other directory scopes using one or both of the following sub-options: </p>
 </dd>
<dt><code>DIRECTORY &lt;dirs&gt;...</code></dt>
<dd> <p> The source file property will be set in each of the <code>&lt;dirs&gt;</code> directories&#8217; scopes. CMake must already know about each of these directories, either by having added them through a call to <code>add_subdirectory()</code> or it being the top level source directory. Relative paths are treated as relative to the current source directory. </p>
<p>New in version 3.19: <code>&lt;dirs&gt;</code> may reference a binary directory. </p>
 </dd>
<dt><code>TARGET_DIRECTORY &lt;targets&gt;...</code></dt>
<dd> <p> The source file property will be set in each of the directory scopes where any of the specified <code>&lt;targets&gt;</code> were created (the <code>&lt;targets&gt;</code> must therefore already exist). </p>
<p>See also the <code>set_source_files_properties()</code> command. </p>
 </dd>
<dt><code>INSTALL</code></dt>
<dd> <p> New in version 3.1. </p>
<p>Scope may name zero or more installed file paths. These are made available to CPack to influence deployment. </p>
<p>Both the property key and value may use generator expressions. Specific properties may apply to installed files and/or directories. </p>
<p>Path components have to be separated by forward slashes, must be normalized and are case sensitive. </p>
<p>To reference the installation prefix itself with a relative path use <code>.</code>. </p>
<p>Currently installed file properties are only defined for the WIX generator where the given paths are relative to the installation prefix. </p>
 </dd>
<dt><code>TEST</code></dt>
<dd> <p> Scope may name zero or more existing tests. See also the <code>set_tests_properties()</code> command. </p>
 </dd>
<dt><code>CACHE</code></dt>
<dd> <p> Scope must name zero or more cache existing entries. </p>
<p>The required <code>PROPERTY</code> option is immediately followed by the name of the property to set. Remaining arguments are used to compose the property value in the form of a semicolon-separated list. </p>
<p>If the <code>APPEND</code> option is given the list is appended to any existing property value (except that empty values are ignored and not appended). If the <code>APPEND_STRING</code> option is given the string is appended to any existing property value as string, i.e. it results in a longer string and not a list of strings. When using <code>APPEND</code> or <code>APPEND_STRING</code> with a property defined to support <code>INHERITED</code> behavior (see <code>define_property()</code>), no inheriting occurs when finding the initial value to append to. If the property is not already directly set in the nominated scope, the command will behave as though <code>APPEND</code> or <code>APPEND_STRING</code> had not been given. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-properties/">cmake-properties</a>(7)</code> manual for a list of properties in each scope. </p>
<p> <code>NOTE:</code> The <code>GENERATED</code> source file property may be globally visible. See its documentation for details. </p>
 </dd></dl>
<h3>site_name</h3>
<p>Set the given variable to the name of the computer. </p>
<pre><code>site_name(variable)
</code></pre>
<p>On UNIX-like platforms, if the variable <code>HOSTNAME</code> is set, its value will be executed as a command expected to print out the host name, much like the <code>hostname</code> command-line tool.  </p>
<h3>string</h3>
<p>String operations.  </p>
<h3>Synopsis</h3>
<pre><code>
 Search and Replace   string( FIND  &lt;string&gt; &lt;substring&gt; &lt;out-var&gt; [...])
  string( REPLACE  &lt;match-string&gt; &lt;replace-string&gt; &lt;out-var&gt; &lt;input&gt;...)
  string( REGEX MATCH  &lt;match-regex&gt; &lt;out-var&gt; &lt;input&gt;...)
  string( REGEX MATCHALL  &lt;match-regex&gt; &lt;out-var&gt; &lt;input&gt;...)
  string( REGEX REPLACE  &lt;match-regex&gt; &lt;replace-expr&gt; &lt;out-var&gt; &lt;input&gt;...)
 Manipulation   string( APPEND  &lt;string-var&gt; [&lt;input&gt;...])
  string( PREPEND  &lt;string-var&gt; [&lt;input&gt;...])
  string( CONCAT  &lt;out-var&gt; [&lt;input&gt;...])
  string( JOIN  &lt;glue&gt; &lt;out-var&gt; [&lt;input&gt;...])
  string( TOLOWER  &lt;string&gt; &lt;out-var&gt;)
  string( TOUPPER  &lt;string&gt; &lt;out-var&gt;)
  string( LENGTH  &lt;string&gt; &lt;out-var&gt;)
  string( SUBSTRING  &lt;string&gt; &lt;begin&gt; &lt;length&gt; &lt;out-var&gt;)
  string( STRIP  &lt;string&gt; &lt;out-var&gt;)
  string( GENEX_STRIP  &lt;string&gt; &lt;out-var&gt;)
  string( REPEAT  &lt;string&gt; &lt;count&gt; &lt;out-var&gt;)
 Comparison   string( COMPARE  &lt;op&gt; &lt;string1&gt; &lt;string2&gt; &lt;out-var&gt;)
 Hashing   string( &lt;HASH&gt;  &lt;out-var&gt; &lt;input&gt;)
 Generation   string( ASCII  &lt;number&gt;... &lt;out-var&gt;)
  string( HEX  &lt;string&gt; &lt;out-var&gt;)
  string( CONFIGURE  &lt;string&gt; &lt;out-var&gt; [...])
  string( MAKE_C_IDENTIFIER  &lt;string&gt; &lt;out-var&gt;)
  string( RANDOM  [&lt;option&gt;...] &lt;out-var&gt;)
  string( TIMESTAMP  &lt;out-var&gt; [&lt;format string&gt;] [UTC])
  string( UUID  &lt;out-var&gt; ...)
 JSON   string(JSON &lt;out-var&gt; [ERROR_VARIABLE &lt;error-var&gt;]
         { GET  | TYPE  | LENGTH  | REMOVE }
         &lt;json-string&gt; &lt;member|index&gt; [&lt;member|index&gt; ...])
  string(JSON &lt;out-var&gt; [ERROR_VARIABLE &lt;error-var&gt;] MEMBER  &lt;json-string&gt;
         [&lt;member|index&gt; ...] &lt;index&gt;)
  string(JSON &lt;out-var&gt; [ERROR_VARIABLE &lt;error-var&gt;] SET  &lt;json-string&gt;
         &lt;member|index&gt; [&lt;member|index&gt; ...] &lt;value&gt;)
  string(JSON &lt;out-var&gt; [ERROR_VARIABLE &lt;error-var&gt;] EQUAL  &lt;json-string1&gt; &lt;json-string2&gt;)
</code></pre>
<h3>Search and Replace</h3>
<h3>Search and Replace With Plain Strings</h3>
<pre><code>string(FIND &lt;string&gt; &lt;substring&gt; &lt;output_variable&gt; [REVERSE])
</code></pre>
<p>Return the position where the given <code>&lt;substring&gt;</code> was found in the supplied <code>&lt;string&gt;</code>. If the <code>REVERSE</code> flag was used, the command will search for the position of the last occurrence of the specified <code>&lt;substring&gt;</code>. If the <code>&lt;substring&gt;</code> is not found, a position of -1 is returned. </p>
<p>The <code>string(FIND)</code> subcommand treats all strings as ASCII-only characters. The index stored in <code>&lt;output_variable&gt;</code> will also be counted in bytes, so strings containing multi-byte characters may lead to unexpected results. </p>
<pre><code>string(REPLACE &lt;match_string&gt;
       &lt;replace_string&gt; &lt;output_variable&gt;
       &lt;input&gt; [&lt;input&gt;...])
</code></pre>
<p>Replace all occurrences of <code>&lt;match_string&gt;</code> in the <code>&lt;input&gt;</code> with <code>&lt;replace_string&gt;</code> and store the result in the <code>&lt;output_variable&gt;</code>.  </p>
<h3>Search and Replace With Regular Expressions</h3>
<pre><code>string(REGEX MATCH &lt;regular_expression&gt;
       &lt;output_variable&gt; &lt;input&gt; [&lt;input&gt;...])
</code></pre>
<p>Match the <code>&lt;regular_expression&gt;</code> once and store the match in the <code>&lt;output_variable&gt;</code>. All <code>&lt;input&gt;</code> arguments are concatenated before matching. Regular expressions are specified in the subsection just below. </p>
<pre><code>string(REGEX MATCHALL &lt;regular_expression&gt;
       &lt;output_variable&gt; &lt;input&gt; [&lt;input&gt;...])
</code></pre>
<p>Match the <code>&lt;regular_expression&gt;</code> as many times as possible and store the matches in the <code>&lt;output_variable&gt;</code> as a list. All <code>&lt;input&gt;</code> arguments are concatenated before matching. </p>
<pre><code>string(REGEX REPLACE &lt;regular_expression&gt;
       &lt;replacement_expression&gt; &lt;output_variable&gt;
       &lt;input&gt; [&lt;input&gt;...])
</code></pre>
<p>Match the <code>&lt;regular_expression&gt;</code> as many times as possible and substitute the <code>&lt;replacement_expression&gt;</code> for the match in the output. All <code>&lt;input&gt;</code> arguments are concatenated before matching. </p>
<p>The <code>&lt;replacement_expression&gt;</code> may refer to parenthesis-delimited subexpressions of the match using <code>\1</code>, <code>\2</code>, ..., <code>\9</code>. Note that two backslashes (<code>\\1</code>) are required in CMake code to get a backslash through argument parsing.  </p>
<h3>Regex Specification</h3>
<p>The following characters have special meaning in regular expressions: </p>
<dl>
<dt><code>^</code></dt>
<dd> <p> Matches at beginning of input </p>
 </dd>
<dt><code>$</code></dt>
<dd> <p> Matches at end of input </p>
 </dd>
<dt><code>.</code></dt>
<dd> <p> Matches any single character </p>
 </dd>
<dt><code>\&lt;char&gt;</code></dt>
<dd> <p> Matches the single character specified by <code>&lt;char&gt;</code>. Use this to match special regex characters, e.g. <code>\.</code> for a literal <code>.</code> or <code>\\</code> for a literal backslash <code>\</code>. Escaping a non-special character is unnecessary but allowed, e.g. <code>\a</code> matches <code>a</code>. </p>
 </dd>
<dt><code>[ ]</code></dt>
<dd> <p> Matches any character(s) inside the brackets </p>
 </dd>
<dt><code>[^ ]</code></dt>
<dd> <p> Matches any character(s) not inside the brackets </p>
 </dd>
<dt><code>-</code></dt>
<dd> <p> Inside brackets, specifies an inclusive range between characters on either side e.g. <code>[a-f]</code> is <code>[abcdef]</code> To match a literal <code>-</code> using brackets, make it the first or the last character e.g. <code>[+*/-]</code> matches basic mathematical operators. </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> Matches preceding pattern zero or more times </p>
 </dd>
<dt><code>+</code></dt>
<dd> <p> Matches preceding pattern one or more times </p>
 </dd>
<dt><code>?</code></dt>
<dd> <p> Matches preceding pattern zero or once only </p>
 </dd>
<dt><code>|</code></dt>
<dd> <p> Matches a pattern on either side of the <code>|</code> </p>
 </dd>
<dt><code>()</code></dt>
<dd> <p> Saves a matched subexpression, which can be referenced in the <code>REGEX REPLACE</code> operation. </p>
<p>New in version 3.9: All regular expression-related commands, including e.g. <code>if(MATCHES)</code>, save subgroup matches in the variables <code>CMAKE_MATCH_&lt;n&gt;</code> for <code>&lt;n&gt;</code> 0..9. </p>
<p> <code>*</code>, <code>+</code> and <code>?</code> have higher precedence than concatenation. <code>|</code> has lower precedence than concatenation. This means that the regular expression <code>^ab+d$</code> matches <code>abbd</code> but not <code>ababd</code>, and the regular expression <code>^(ab|cd)$</code> matches <code>ab</code> but not <code>abd</code>. </p>
<p>CMake language Escape Sequences such as <code>\t</code>, <code>\r</code>, <code>\n</code>, and <code>\\</code> may be used to construct literal tabs, carriage returns, newlines, and backslashes (respectively) to pass in a regex. For example: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The quoted argument <code>&quot;[ \t\r\n]&quot;</code> specifies a regex that matches any single whitespace character. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The quoted argument <code>&quot;[/\\]&quot;</code> specifies a regex that matches a single forward slash <code>/</code> or backslash <code>\</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The quoted argument <code>&quot;[A-Za-z0-9_]&quot;</code> specifies a regex that matches any single &quot;word&quot; character in the C locale. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The quoted argument <code>&quot;\\(\\a\\+b\\)&quot;</code> specifies a regex that matches the exact string <code>(a+b)</code>. Each <code>\\</code> is parsed in a quoted argument as just <code>\</code>, so the regex itself is actually <code>\(\a\+\b\)</code>. This can alternatively be specified in a bracket argument without having to escape the backslashes, e.g. <code>[[\(\a\+\b\)]]</code>. </p>
 </dd></dl>
<h3>Manipulation</h3>
<pre><code>string(APPEND &lt;string_variable&gt; [&lt;input&gt;...])
</code></pre>
<p>New in version 3.4. </p>
<p>Append all the <code>&lt;input&gt;</code> arguments to the string. </p>
<pre><code>string(PREPEND &lt;string_variable&gt; [&lt;input&gt;...])
</code></pre>
<p>New in version 3.10. </p>
<p>Prepend all the <code>&lt;input&gt;</code> arguments to the string. </p>
<pre><code>string(CONCAT &lt;output_variable&gt; [&lt;input&gt;...])
</code></pre>
<p>Concatenate all the <code>&lt;input&gt;</code> arguments together and store the result in the named <code>&lt;output_variable&gt;</code>. </p>
<pre><code>string(JOIN &lt;glue&gt; &lt;output_variable&gt; [&lt;input&gt;...])
</code></pre>
<p>New in version 3.12. </p>
<p>Join all the <code>&lt;input&gt;</code> arguments together using the <code>&lt;glue&gt;</code> string and store the result in the named <code>&lt;output_variable&gt;</code>. </p>
<p>To join a list&#8217;s elements, prefer to use the <code>JOIN</code> operator from the <code>list()</code> command. This allows for the elements to have special characters like <code>;</code> in them. </p>
<pre><code>string(TOLOWER &lt;string&gt; &lt;output_variable&gt;)
</code></pre>
<p>Convert <code>&lt;string&gt;</code> to lower characters. </p>
<pre><code>string(TOUPPER &lt;string&gt; &lt;output_variable&gt;)
</code></pre>
<p>Convert <code>&lt;string&gt;</code> to upper characters. </p>
<pre><code>string(LENGTH &lt;string&gt; &lt;output_variable&gt;)
</code></pre>
<p>Store in an <code>&lt;output_variable&gt;</code> a given string&#8217;s length in bytes. Note that this means if <code>&lt;string&gt;</code> contains multi-byte characters, the result stored in <code>&lt;output_variable&gt;</code> will <i>not</i> be the number of characters. </p>
<pre><code>string(SUBSTRING &lt;string&gt; &lt;begin&gt; &lt;length&gt; &lt;output_variable&gt;)
</code></pre>
<p>Store in an <code>&lt;output_variable&gt;</code> a substring of a given <code>&lt;string&gt;</code>. If <code>&lt;length&gt;</code> is <code>-1</code> the remainder of the string starting at <code>&lt;begin&gt;</code> will be returned. </p>
<p>Changed in version 3.2: If <code>&lt;string&gt;</code> is shorter than <code>&lt;length&gt;</code> then the end of the string is used instead. Previous versions of CMake reported an error in this case. </p>
<p>Both <code>&lt;begin&gt;</code> and <code>&lt;length&gt;</code> are counted in bytes, so care must be exercised if <code>&lt;string&gt;</code> could contain multi-byte characters. </p>
<pre><code>string(STRIP &lt;string&gt; &lt;output_variable&gt;)
</code></pre>
<p>Store in an <code>&lt;output_variable&gt;</code> a substring of a given <code>&lt;string&gt;</code> with leading and trailing spaces removed. </p>
<pre><code>string(GENEX_STRIP &lt;string&gt; &lt;output_variable&gt;)
</code></pre>
<p>New in version 3.1. </p>
<p>Strip any <code>generator expressions</code> from the input <code>&lt;string&gt;</code> and store the result in the <code>&lt;output_variable&gt;</code>. </p>
<pre><code>string(REPEAT &lt;string&gt; &lt;count&gt; &lt;output_variable&gt;)
</code></pre>
<p>New in version 3.15. </p>
<p>Produce the output string as the input <code>&lt;string&gt;</code> repeated <code>&lt;count&gt;</code> times.  </p>
<h3>Comparison</h3>
<pre><code>string(COMPARE LESS &lt;string1&gt; &lt;string2&gt; &lt;output_variable&gt;)
string(COMPARE GREATER &lt;string1&gt; &lt;string2&gt; &lt;output_variable&gt;)
string(COMPARE EQUAL &lt;string1&gt; &lt;string2&gt; &lt;output_variable&gt;)
string(COMPARE NOTEQUAL &lt;string1&gt; &lt;string2&gt; &lt;output_variable&gt;)
string(COMPARE LESS_EQUAL &lt;string1&gt; &lt;string2&gt; &lt;output_variable&gt;)
string(COMPARE GREATER_EQUAL &lt;string1&gt; &lt;string2&gt; &lt;output_variable&gt;)
</code></pre>
<p>Compare the strings and store true or false in the <code>&lt;output_variable&gt;</code>. </p>
<p>New in version 3.7: Added the <code>LESS_EQUAL</code> and <code>GREATER_EQUAL</code> options. </p>
<h3>Hashing</h3>
<pre><code>string(&lt;HASH&gt; &lt;output_variable&gt; &lt;input&gt;)
</code></pre>
<p>Compute a cryptographic hash of the <code>&lt;input&gt;</code> string. The supported <code>&lt;HASH&gt;</code> algorithm names are: </p>
<dl>
<dt><code>MD5</code></dt>
<dd> <p> Message-Digest Algorithm 5, RFC 1321. </p>
 </dd>
<dt><code>SHA1</code></dt>
<dd> <p> US Secure Hash Algorithm 1, RFC 3174. </p>
 </dd>
<dt><code>SHA224</code></dt>
<dd> <p> US Secure Hash Algorithms, RFC 4634. </p>
 </dd>
<dt><code>SHA256</code></dt>
<dd> <p> US Secure Hash Algorithms, RFC 4634. </p>
 </dd>
<dt><code>SHA384</code></dt>
<dd> <p> US Secure Hash Algorithms, RFC 4634. </p>
 </dd>
<dt><code>SHA512</code></dt>
<dd> <p> US Secure Hash Algorithms, RFC 4634. </p>
 </dd>
<dt><code>SHA3_224</code></dt>
<dd> <p> Keccak SHA-3. </p>
 </dd>
<dt><code>SHA3_256</code></dt>
<dd> <p> Keccak SHA-3. </p>
 </dd>
<dt><code>SHA3_384</code></dt>
<dd> <p> Keccak SHA-3. </p>
 </dd>
<dt><code>SHA3_512</code></dt>
<dd> <p> Keccak SHA-3. </p>
<p>New in version 3.8: Added the <code>SHA3_*</code> hash algorithms. </p>
 </dd></dl>
<h3>Generation</h3>
<pre><code>string(ASCII &lt;number&gt; [&lt;number&gt; ...] &lt;output_variable&gt;)
</code></pre>
<p>Convert all numbers into corresponding ASCII characters. </p>
<pre><code>string(HEX &lt;string&gt; &lt;output_variable&gt;)
</code></pre>
<p>New in version 3.18. </p>
<p>Convert each byte in the input <code>&lt;string&gt;</code> to its hexadecimal representation and store the concatenated hex digits in the <code>&lt;output_variable&gt;</code>. Letters in the output (<code>a</code> through <code>f</code>) are in lowercase. </p>
<pre><code>string(CONFIGURE &lt;string&gt; &lt;output_variable&gt;
       [@ONLY] [ESCAPE_QUOTES])
</code></pre>
<p>Transform a <code>&lt;string&gt;</code> like <code>configure_file()</code> transforms a file. </p>
<pre><code>string(MAKE_C_IDENTIFIER &lt;string&gt; &lt;output_variable&gt;)
</code></pre>
<p>Convert each non-alphanumeric character in the input <code>&lt;string&gt;</code> to an underscore and store the result in the <code>&lt;output_variable&gt;</code>. If the first character of the <code>&lt;string&gt;</code> is a digit, an underscore will also be prepended to the result. </p>
<pre><code>string(RANDOM [LENGTH &lt;length&gt;] [ALPHABET &lt;alphabet&gt;]
       [RANDOM_SEED &lt;seed&gt;] &lt;output_variable&gt;)
</code></pre>
<p>Return a random string of given <code>&lt;length&gt;</code> consisting of characters from the given <code>&lt;alphabet&gt;</code>. Default length is 5 characters and default alphabet is all numbers and upper and lower case letters. If an integer <code>RANDOM_SEED</code> is given, its value will be used to seed the random number generator. </p>
<pre><code>string(TIMESTAMP &lt;output_variable&gt; [&lt;format_string&gt;] [UTC])
</code></pre>
<p>Write a string representation of the current date and/or time to the <code>&lt;output_variable&gt;</code>. </p>
<p>If the command is unable to obtain a timestamp, the <code>&lt;output_variable&gt;</code> will be set to the empty string <code>&quot;&quot;</code>. </p>
<p>The optional <code>UTC</code> flag requests the current date/time representation to be in Coordinated Universal Time (UTC) rather than local time. </p>
<p>The optional <code>&lt;format_string&gt;</code> may contain the following format specifiers: </p>
<dl>
<dt><code>%%</code></dt>
<dd> <p> New in version 3.8. </p>
<p>A literal percent sign (%). </p>
 </dd>
<dt><code>%d</code></dt>
<dd> <p> The day of the current month (01-31). </p>
 </dd>
<dt><code>%H</code></dt>
<dd> <p> The hour on a 24-hour clock (00-23). </p>
 </dd>
<dt><code>%I</code></dt>
<dd> <p> The hour on a 12-hour clock (01-12). </p>
 </dd>
<dt><code>%j</code></dt>
<dd> <p> The day of the current year (001-366). </p>
 </dd>
<dt><code>%m</code></dt>
<dd> <p> The month of the current year (01-12). </p>
 </dd>
<dt><code>%b</code></dt>
<dd> <p> New in version 3.7. </p>
<p>Abbreviated month name (e.g. Oct). </p>
 </dd>
<dt><code>%B</code></dt>
<dd> <p> New in version 3.10. </p>
<p>Full month name (e.g. October). </p>
 </dd>
<dt><code>%M</code></dt>
<dd> <p> The minute of the current hour (00-59). </p>
 </dd>
<dt><code>%s</code></dt>
<dd> <p> New in version 3.6. </p>
<p>Seconds since midnight (UTC) 1-Jan-1970 (UNIX time). </p>
 </dd>
<dt><code>%S</code></dt>
<dd> <p> The second of the current minute. 60 represents a leap second. (00-60) </p>
 </dd>
<dt><code>%U</code></dt>
<dd> <p> The week number of the current year (00-53). </p>
 </dd>
<dt><code>%V</code></dt>
<dd> <p> New in version 3.22. </p>
<p>The ISO 8601 week number of the current year (01-53). </p>
 </dd>
<dt><code>%w</code></dt>
<dd> <p> The day of the current week. 0 is Sunday. (0-6) </p>
 </dd>
<dt><code>%a</code></dt>
<dd> <p> New in version 3.7. </p>
<p>Abbreviated weekday name (e.g. Fri). </p>
 </dd>
<dt><code>%A</code></dt>
<dd> <p> New in version 3.10. </p>
<p>Full weekday name (e.g. Friday). </p>
 </dd>
<dt><code>%y</code></dt>
<dd> <p> The last two digits of the current year (00-99). </p>
 </dd>
<dt><code>%Y</code></dt>
<dd> <p> The current year. </p>
<p>Unknown format specifiers will be ignored and copied to the output as-is. </p>
<p>If no explicit <code>&lt;format_string&gt;</code> is given, it will default to: </p>
<pre><code>%Y-%m-%dT%H:%M:%S for local time.
%Y-%m-%dT%H:%M:%SZ for UTC.
</code></pre>
<p>New in version 3.8: If the <code>SOURCE_DATE_EPOCH</code> environment variable is set, its value will be used instead of the current time. See <i><a rel="nofollow" href="https://reproducible-builds.org/specs/source-date-epoch/">https://reproducible-builds.org/specs/source-date-epoch/</a></i> for details. </p>
<pre><code>string(UUID &lt;output_variable&gt; NAMESPACE &lt;namespace&gt; NAME &lt;name&gt;
       TYPE &lt;MD5|SHA1&gt; [UPPER])
</code></pre>
<p>New in version 3.1. </p>
<p>Create a universally unique identifier (aka GUID) as per RFC4122 based on the hash of the combined values of <code>&lt;namespace&gt;</code> (which itself has to be a valid UUID) and <code>&lt;name&gt;</code>. The hash algorithm can be either <code>MD5</code> (Version 3 UUID) or <code>SHA1</code> (Version 5 UUID). A UUID has the format <code>xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx</code> where each <code>x</code> represents a lower case hexadecimal character. Where required, an uppercase representation can be requested with the optional <code>UPPER</code> flag. </p>
 </dd></dl>
<h3>JSON</h3>
<p>New in version 3.19. </p>
<p>Functionality for querying a JSON string. </p>
<p> <code>NOTE:</code> In each of the following JSON-related subcommands, if the optional <code>ERROR_VARIABLE</code> argument is given, errors will be reported in <code>&lt;error-variable&gt;</code> and the <code>&lt;out-var&gt;</code> will be set to <code>&lt;member|index&gt;-[&lt;member|index&gt;...]-NOTFOUND</code> with the path elements up to the point where the error occurred, or just <code>NOTFOUND</code> if there is no relevant path. If an error occurs but the <code>ERROR_VARIABLE</code> option is not present, a fatal error message is generated. If no error occurs, the <code>&lt;error-variable&gt;</code> will be set to <code>NOTFOUND</code>. </p>
<pre><code>string(JSON &lt;out-var&gt; [ERROR_VARIABLE &lt;error-variable&gt;]
       GET &lt;json-string&gt; &lt;member|index&gt; [&lt;member|index&gt; ...])
</code></pre>
<p>Get an element from <code>&lt;json-string&gt;</code> at the location given by the list of <code>&lt;member|index&gt;</code> arguments. Array and object elements will be returned as a JSON string. Boolean elements will be returned as <code>ON</code> or <code>OFF</code>. Null elements will be returned as an empty string. Number and string types will be returned as strings. </p>
<pre><code>string(JSON &lt;out-var&gt; [ERROR_VARIABLE &lt;error-variable&gt;]
       TYPE &lt;json-string&gt; &lt;member|index&gt; [&lt;member|index&gt; ...])
</code></pre>
<p>Get the type of an element in <code>&lt;json-string&gt;</code> at the location given by the list of <code>&lt;member|index&gt;</code> arguments. The <code>&lt;out-var&gt;</code> will be set to one of <code>NULL</code>, <code>NUMBER</code>, <code>STRING</code>, <code>BOOLEAN</code>, <code>ARRAY</code>, or <code>OBJECT</code>. </p>
<pre><code>string(JSON &lt;out-var&gt; [ERROR_VARIABLE &lt;error-var&gt;]
       MEMBER &lt;json-string&gt;
       [&lt;member|index&gt; ...] &lt;index&gt;)
</code></pre>
<p>Get the name of the <code>&lt;index&gt;</code>-th member in <code>&lt;json-string&gt;</code> at the location given by the list of <code>&lt;member|index&gt;</code> arguments. Requires an element of object type. </p>
<pre><code>string(JSON &lt;out-var&gt; [ERROR_VARIABLE &lt;error-variable&gt;]
       LENGTH &lt;json-string&gt; &lt;member|index&gt; [&lt;member|index&gt; ...])
</code></pre>
<p>Get the length of an element in <code>&lt;json-string&gt;</code> at the location given by the list of <code>&lt;member|index&gt;</code> arguments. Requires an element of array or object type. </p>
<pre><code>string(JSON &lt;out-var&gt; [ERROR_VARIABLE &lt;error-variable&gt;]
       REMOVE &lt;json-string&gt; &lt;member|index&gt; [&lt;member|index&gt; ...])
</code></pre>
<p>Remove an element from <code>&lt;json-string&gt;</code> at the location given by the list of <code>&lt;member|index&gt;</code> arguments. The JSON string without the removed element will be stored in <code>&lt;out-var&gt;</code>. </p>
<pre><code>string(JSON &lt;out-var&gt; [ERROR_VARIABLE &lt;error-variable&gt;]
       SET &lt;json-string&gt; &lt;member|index&gt; [&lt;member|index&gt; ...] &lt;value&gt;)
</code></pre>
<p>Set an element in <code>&lt;json-string&gt;</code> at the location given by the list of <code>&lt;member|index&gt;</code> arguments to <code>&lt;value&gt;</code>. The contents of <code>&lt;value&gt;</code> should be valid JSON. </p>
<pre><code>string(JSON &lt;out-var&gt; [ERROR_VARIABLE &lt;error-var&gt;]
       EQUAL &lt;json-string1&gt; &lt;json-string2&gt;)
</code></pre>
<p>Compare the two JSON objects given by <code>&lt;json-string1&gt;</code> and <code>&lt;json-string2&gt;</code> for equality. The contents of <code>&lt;json-string1&gt;</code> and <code>&lt;json-string2&gt;</code> should be valid JSON. The <code>&lt;out-var&gt;</code> will be set to a true value if the JSON objects are considered equal, or a false value otherwise.  </p>
<h3>unset</h3>
<p>Unset a variable, cache variable, or environment variable.  </p>
<h3>Unset Normal Variable or Cache Entry</h3>
<pre><code>unset(&lt;variable&gt; [CACHE | PARENT_SCOPE])
</code></pre>
<p>Removes a normal variable from the current scope, causing it to become undefined. If <code>CACHE</code> is present, then a cache variable is removed instead of a normal variable. Note that when evaluating Variable References of the form <code>${VAR}</code>, CMake first searches for a normal variable with that name. If no such normal variable exists, CMake will then search for a cache entry with that name. Because of this unsetting a normal variable can expose a cache variable that was previously hidden. To force a variable reference of the form <code>${VAR}</code> to return an empty string, use <code>set(&lt;variable&gt; &quot;&quot;)</code>, which clears the normal variable but leaves it defined. </p>
<p>If <code>PARENT_SCOPE</code> is present then the variable is removed from the scope above the current scope. See the same option in the <code>set()</code> command for further details.  </p>
<h3>Unset Environment Variable</h3>
<pre><code>unset(ENV{&lt;variable&gt;})
</code></pre>
<p>Removes <code>&lt;variable&gt;</code> from the currently available <code>Environment Variables</code>. Subsequent calls of <code>$ENV{&lt;variable&gt;}</code> will return the empty string. </p>
<p>This command affects only the current CMake process, not the process from which CMake was called, nor the system environment at large, nor the environment of subsequent build or test processes.  </p>
<h3>variable_watch</h3>
<p>Watch the CMake variable for change. </p>
<pre><code>variable_watch(&lt;variable&gt; [&lt;command&gt;])
</code></pre>
<p>If the specified <code>&lt;variable&gt;</code> changes and no <code>&lt;command&gt;</code> is given, a message will be printed to inform about the change. </p>
<p>If <code>&lt;command&gt;</code> is given, this command will be executed instead. The command will receive the following arguments: <code>COMMAND(&lt;variable&gt; &lt;access&gt; &lt;value&gt; &lt;current_list_file&gt; &lt;stack&gt;)</code> </p>
<dl>
<dt><code>&lt;variable&gt;</code></dt>
<dd> <p> Name of the variable being accessed. </p>
 </dd>
<dt><code>&lt;access&gt;</code></dt>
<dd> <p> One of <code>READ_ACCESS</code>, <code>UNKNOWN_READ_ACCESS</code>, <code>MODIFIED_ACCESS</code>, <code>UNKNOWN_MODIFIED_ACCESS</code>, or <code>REMOVED_ACCESS</code>. The <code>UNKNOWN_</code> values are only used when the variable has never been set. Once set, they are never used again during the same CMake run, even if the variable is later unset. </p>
 </dd>
<dt><code>&lt;value&gt;</code></dt>
<dd> <p> The value of the variable. On a modification, this is the new (modified) value of the variable. On removal, the value is empty. </p>
 </dd>
<dt><code>&lt;current_list_file&gt;</code></dt>
<dd> <p> Full path to the file doing the access. </p>
 </dd>
<dt><code>&lt;stack&gt;</code></dt>
<dd> <p> List of absolute paths of all files currently on the stack of file inclusion, with the bottom-most file first and the currently processed file (that is, <code>current_list_file</code>) last. </p>
<p>Note that for some accesses such as <code>list(APPEND)</code>, the watcher is executed twice, first with a read access and then with a write one. Also note that an <code>if(DEFINED)</code> query on the variable does not register as an access and the watcher is not executed. </p>
<p>Only non-cache variables can be watched using this command. Access to cache variables is never watched. However, the existence of a cache variable <code>var</code> causes accesses to the non-cache variable <code>var</code> to not use the <code>UNKNOWN_</code> prefix, even if a non-cache variable <code>var</code> has never existed. </p>
 </dd></dl>
<h3>while</h3>
<p>Evaluate a group of commands while a condition is true </p>
<pre><code>while(&lt;condition&gt;)
  &lt;commands&gt;
endwhile()
</code></pre>
<p>All commands between while and the matching <code>endwhile()</code> are recorded without being invoked. Once the <code>endwhile()</code> is evaluated, the recorded list of commands is invoked as long as the <code>&lt;condition&gt;</code> is true. </p>
<p>The <code>&lt;condition&gt;</code> has the same syntax and is evaluated using the same logic as described at length for the <code>if()</code> command. </p>
<p>The commands <code>break()</code> and <code>continue()</code> provide means to escape from the normal control flow. </p>
<p>Per legacy, the <code>endwhile()</code> command admits an optional <code>&lt;condition&gt;</code> argument. If used, it must be a verbatim repeat of the argument of the opening <code>while</code> command.  </p>
<h2>PROJECT COMMANDS</h2>
<p>These commands are available only in CMake projects.  </p>
<h3>add_compile_definitions</h3>
<p>New in version 3.12. </p>
<p>Add preprocessor definitions to the compilation of source files. </p>
<pre><code>add_compile_definitions(&lt;definition&gt; ...)
</code></pre>
<p>Adds preprocessor definitions to the compiler command line. </p>
<p>The preprocessor definitions are added to the <code>COMPILE_DEFINITIONS</code> directory property for the current <code>CMakeLists</code> file. They are also added to the <code>COMPILE_DEFINITIONS</code> target property for each target in the current <code>CMakeLists</code> file. </p>
<p>Definitions are specified using the syntax <code>VAR</code> or <code>VAR=value</code>. Function-style definitions are not supported. CMake will automatically escape the value correctly for the native build system (note that CMake language syntax may require escapes to specify some values). </p>
<p>Arguments to <code>add_compile_definitions</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;...&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake-buildsystem/">cmake-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.  </p>
<h3>add_compile_options</h3>
<p>Add options to the compilation of source files. </p>
<pre><code>add_compile_options(&lt;option&gt; ...)
</code></pre>
<p>Adds options to the <code>COMPILE_OPTIONS</code> directory property. These options are used when compiling targets from the current directory and below.  </p>
<h3>Arguments</h3>
<p>Arguments to <code>add_compile_options</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;...&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake-buildsystem/">cmake-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.  </p>
<h3>Option De-duplication</h3>
<p>The final set of options used for a target is constructed by accumulating options from the current target and the usage requirements of its dependencies. The set of options is de-duplicated to avoid repetition. </p>
<p>New in version 3.12: While beneficial for individual options, the de-duplication step can break up option groups. For example, <code>-option A -option B</code> becomes <code>-option A B</code>. One may specify a group of options using shell-like quoting along with a <code>SHELL:</code> prefix. The <code>SHELL:</code> prefix is dropped, and the rest of the option string is parsed using the <code>separate_arguments()</code> <code>UNIX_COMMAND</code> mode. For example, <code>&quot;SHELL:-option A&quot; &quot;SHELL:-option B&quot;</code> becomes <code>-option A -option B</code>. </p>
<h3>Example</h3>
<p>Since different compilers support different options, a typical use of this command is in a compiler-specific conditional clause: </p>
<pre><code>if (MSVC)
    # warning level 4 and all warnings as errors
    add_compile_options(/W4 /WX)
else()
    # lots of warnings and all warnings as errors
    add_compile_options(-Wall -Wextra -pedantic -Werror)
endif()
</code></pre>
<h3>See Also</h3>
<p>This command can be used to add any options. However, for adding preprocessor definitions and include directories it is recommended to use the more specific commands <code>add_compile_definitions()</code> and <code>include_directories()</code>. </p>
<p>The command <code>target_compile_options()</code> adds target-specific options. </p>
<p>The source file property <code>COMPILE_OPTIONS</code> adds options to one source file.  </p>
<h3>add_custom_command</h3>
<p>Add a custom build rule to the generated build system. </p>
<p>There are two main signatures for <code>add_custom_command</code>.  </p>
<h3>Generating Files</h3>
<p>The first signature is for adding a custom command to produce an output: </p>
<pre><code>add_custom_command(OUTPUT output1 [output2 ...]
                   COMMAND command1 [ARGS] [args1...]
                   [COMMAND command2 [ARGS] [args2...] ...]
                   [MAIN_DEPENDENCY depend]
                   [DEPENDS [depends...]]
                   [BYPRODUCTS [files...]]
                   [IMPLICIT_DEPENDS &lt;lang1&gt; depend1
                                    [&lt;lang2&gt; depend2] ...]
                   [WORKING_DIRECTORY dir]
                   [COMMENT comment]
                   [DEPFILE depfile]
                   [JOB_POOL job_pool]
                   [VERBATIM] [APPEND] [USES_TERMINAL]
                   [COMMAND_EXPAND_LISTS])
</code></pre>
<p>This defines a command to generate specified <code>OUTPUT</code> file(s). A target created in the same directory (<code>CMakeLists.txt</code> file) that specifies any output of the custom command as a source file is given a rule to generate the file using the command at build time. Do not list the output in more than one independent target that may build in parallel or the two instances of the rule may conflict (instead use the <code>add_custom_target()</code> command to drive the command and make the other targets depend on that one). In makefile terms this creates a new target in the following form: </p>
<pre><code>OUTPUT: MAIN_DEPENDENCY DEPENDS
        COMMAND
</code></pre>
<p>The options are: </p>
<dl>
<dt><code>APPEND</code></dt>
<dd> <p> Append the <code>COMMAND</code> and <code>DEPENDS</code> option values to the custom command for the first output specified. There must have already been a previous call to this command with the same output. </p>
<p>If the previous call specified the output via a generator expression, the output specified by the current call must match in at least one configuration after evaluating generator expressions. In this case, the appended commands and dependencies apply to all configurations. </p>
<p>The <code>COMMENT</code>, <code>MAIN_DEPENDENCY</code>, and <code>WORKING_DIRECTORY</code> options are currently ignored when APPEND is given, but may be used in the future. </p>
 </dd>
<dt><code>BYPRODUCTS</code></dt>
<dd> <p> New in version 3.2. </p>
<p>Specify the files the command is expected to produce but whose modification time may or may not be newer than the dependencies. If a byproduct name is a relative path it will be interpreted relative to the build tree directory corresponding to the current source directory. Each byproduct file will be marked with the <code>GENERATED</code> source file property automatically. </p>
<p>Explicit specification of byproducts is supported by the <code>Ninja</code> generator to tell the <code>ninja</code> build tool how to regenerate byproducts when they are missing. It is also useful when other build rules (e.g. custom commands) depend on the byproducts. Ninja requires a build rule for any generated file on which another rule depends even if there are order-only dependencies to ensure the byproducts will be available before their dependents build. </p>
<p>The Makefile Generators will remove <code>BYPRODUCTS</code> and other <code>GENERATED</code> files during <code>make clean</code>. </p>
<p>New in version 3.20: Arguments to <code>BYPRODUCTS</code> may use a restricted set of <code>generator expressions</code>. Target-dependent expressions are not permitted. </p>
 </dd>
<dt><code>COMMAND</code></dt>
<dd> <p> Specify the command-line(s) to execute at build time. If more than one <code>COMMAND</code> is specified they will be executed in order, but <i>not</i> necessarily composed into a stateful shell or batch script. (To run a full script, use the <code>configure_file()</code> command or the <code>file(GENERATE)</code> command to create it, and then specify a <code>COMMAND</code> to launch it.) The optional <code>ARGS</code> argument is for backward compatibility and will be ignored. </p>
<p>If <code>COMMAND</code> specifies an executable target name (created by the <code>add_executable()</code> command), it will automatically be replaced by the location of the executable created at build time if either of the following is true: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The target is not being cross-compiled (i.e. the <code>CMAKE_CROSSCOMPILING</code> variable is not set to true). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> New in version 3.6: The target is being cross-compiled and an emulator is provided (i.e. its <code>CROSSCOMPILING_EMULATOR</code> target property is set). In this case, the contents of <code>CROSSCOMPILING_EMULATOR</code> will be prepended to the command before the location of the target executable. </p>
<p>If neither of the above conditions are met, it is assumed that the command name is a program to be found on the <code>PATH</code> at build time. </p>
<p>Arguments to <code>COMMAND</code> may use <code>generator expressions</code>. Use the <code>TARGET_FILE</code> generator expression to refer to the location of a target later in the command line (i.e. as a command argument rather than as the command to execute). </p>
<p>Whenever one of the following target based generator expressions are used as a command to execute or is mentioned in a command argument, a target-level dependency will be added automatically so that the mentioned target will be built before any target using this custom command (see policy <code>CMP0112</code>). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>TARGET_FILE</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>TARGET_LINKER_FILE</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>TARGET_SONAME_FILE</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>TARGET_PDB_FILE</code> </p>
<p>This target-level dependency does NOT add a file-level dependency that would cause the custom command to re-run whenever the executable is recompiled. List target names with the <code>DEPENDS</code> option to add such file-level dependencies. </p>
 </dd>
<dt><code>COMMENT</code></dt>
<dd> <p> Display the given message before the commands are executed at build time. </p>
 </dd>
<dt><code>DEPENDS</code></dt>
<dd> <p> Specify files on which the command depends. Each argument is converted to a dependency as follows: </p>
 </dd>
<dt>1.</dt>
<dd> <p> If the argument is the name of a target (created by the <code>add_custom_target()</code>, <code>add_executable()</code>, or <code>add_library()</code> command) a target-level dependency is created to make sure the target is built before any target using this custom command. Additionally, if the target is an executable or library, a file-level dependency is created to cause the custom command to re-run whenever the target is recompiled. </p>
 </dd>
<dt>2.</dt>
<dd> <p> If the argument is an absolute path, a file-level dependency is created on that path. </p>
 </dd>
<dt>3.</dt>
<dd> <p> If the argument is the name of a source file that has been added to a target or on which a source file property has been set, a file-level dependency is created on that source file. </p>
 </dd>
<dt>4.</dt>
<dd> <p> If the argument is a relative path and it exists in the current source directory, a file-level dependency is created on that file in the current source directory. </p>
 </dd>
<dt>5.</dt>
<dd> <p> Otherwise, a file-level dependency is created on that path relative to the current binary directory. </p>
<p>If any dependency is an <code>OUTPUT</code> of another custom command in the same directory (<code>CMakeLists.txt</code> file), CMake automatically brings the other custom command into the target in which this command is built. </p>
<p>New in version 3.16: A target-level dependency is added if any dependency is listed as <code>BYPRODUCTS</code> of a target or any of its build events in the same directory to ensure the byproducts will be available. </p>
<p>If <code>DEPENDS</code> is not specified, the command will run whenever the <code>OUTPUT</code> is missing; if the command does not actually create the <code>OUTPUT</code>, the rule will always run. </p>
<p>New in version 3.1: Arguments to <code>DEPENDS</code> may use <code>generator expressions</code>. </p>
 </dd>
<dt><code>COMMAND_EXPAND_LISTS</code></dt>
<dd> <p> New in version 3.8. </p>
<p>Lists in <code>COMMAND</code> arguments will be expanded, including those created with <code>generator expressions</code>, allowing <code>COMMAND</code> arguments such as <code>${CC} &quot;-I$&lt;JOIN:$&lt;TARGET_PROPERTY:foo,INCLUDE_DIRECTORIES&gt;,;-I&gt;&quot; foo.cc</code> to be properly expanded. </p>
 </dd>
<dt><code>IMPLICIT_DEPENDS</code></dt>
<dd> <p> Request scanning of implicit dependencies of an input file. The language given specifies the programming language whose corresponding dependency scanner should be used. Currently only <code>C</code> and <code>CXX</code> language scanners are supported. The language has to be specified for every file in the <code>IMPLICIT_DEPENDS</code> list. Dependencies discovered from the scanning are added to those of the custom command at build time. Note that the <code>IMPLICIT_DEPENDS</code> option is currently supported only for Makefile generators and will be ignored by other generators. </p>
<p> <code>NOTE:</code> This option cannot be specified at the same time as <code>DEPFILE</code> option. </p>
 </dd>
<dt><code>JOB_POOL</code></dt>
<dd> <p> New in version 3.15. </p>
<p>Specify a <code>pool</code> for the <code>Ninja</code> generator. Incompatible with <code>USES_TERMINAL</code>, which implies the <code>console</code> pool. Using a pool that is not defined by <code>JOB_POOLS</code> causes an error by ninja at build time. </p>
 </dd>
<dt><code>MAIN_DEPENDENCY</code></dt>
<dd> <p> Specify the primary input source file to the command. This is treated just like any value given to the <code>DEPENDS</code> option but also suggests to Visual Studio generators where to hang the custom command. Each source file may have at most one command specifying it as its main dependency. A compile command (i.e. for a library or an executable) counts as an implicit main dependency which gets silently overwritten by a custom command specification. </p>
 </dd>
<dt><code>OUTPUT</code></dt>
<dd> <p> Specify the output files the command is expected to produce. If an output name is a relative path it will be interpreted relative to the build tree directory corresponding to the current source directory. Each output file will be marked with the <code>GENERATED</code> source file property automatically. If the output of the custom command is not actually created as a file on disk it should be marked with the <code>SYMBOLIC</code> source file property. </p>
<p>New in version 3.20: Arguments to <code>OUTPUT</code> may use a restricted set of <code>generator expressions</code>. Target-dependent expressions are not permitted. </p>
 </dd>
<dt><code>USES_TERMINAL</code></dt>
<dd> <p> New in version 3.2. </p>
<p>The command will be given direct access to the terminal if possible. With the <code>Ninja</code> generator, this places the command in the <code>console</code> <code>pool</code>. </p>
 </dd>
<dt><code>VERBATIM</code></dt>
<dd> <p> All arguments to the commands will be escaped properly for the build tool so that the invoked command receives each argument unchanged. Note that one level of escapes is still used by the CMake language processor before add_custom_command even sees the arguments. Use of <code>VERBATIM</code> is recommended as it enables correct behavior. When <code>VERBATIM</code> is not given the behavior is platform specific because there is no protection of tool-specific special characters. </p>
 </dd>
<dt><code>WORKING_DIRECTORY</code></dt>
<dd> <p> Execute the command with the given current working directory. If it is a relative path it will be interpreted relative to the build tree directory corresponding to the current source directory. </p>
<p>New in version 3.13: Arguments to <code>WORKING_DIRECTORY</code> may use <code>generator expressions</code>. </p>
 </dd>
<dt><code>DEPFILE</code></dt>
<dd> <p> New in version 3.7. </p>
<p>Specify a <code>.d</code> depfile which holds dependencies for the custom command. It is usually emitted by the custom command itself. This keyword may only be used if the generator supports it, as detailed below. </p>
<p>New in version 3.7: The <code>Ninja</code> generator supports <code>DEPFILE</code> since the keyword was first added. </p>
<p>New in version 3.17: Added the <code>Ninja Multi-Config</code> generator, which included support for the <code>DEPFILE</code> keyword. </p>
<p>New in version 3.20: Added support for Makefile Generators. </p>
<p> <code>NOTE:</code> <code>DEPFILE</code> cannot be specified at the same time as the <code>IMPLICIT_DEPENDS</code> option for Makefile Generators. </p>
<p>New in version 3.21: Added support for Visual Studio Generators with VS 2012 and above, and for the <code>Xcode</code> generator. Support for <code>generator expressions</code> was also added. </p>
<p>Using <code>DEPFILE</code> with generators other than those listed above is an error. </p>
<p>If the <code>DEPFILE</code> argument is relative, it should be relative to <code>CMAKE_CURRENT_BINARY_DIR</code>, and any relative paths inside the <code>DEPFILE</code> should also be relative to <code>CMAKE_CURRENT_BINARY_DIR</code>. See policy <code>CMP0116</code>, which is always <code>NEW</code> for Makefile Generators, Visual Studio Generators, and the <code>Xcode</code> generator. </p>
 </dd></dl>
<h3>Examples: Generating Files</h3>
<p>Custom commands may be used to generate source files. For example, the code: </p>
<pre><code>add_custom_command(
  OUTPUT out.c
  COMMAND someTool -i ${CMAKE_CURRENT_SOURCE_DIR}/in.txt
                   -o out.c
  DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/in.txt
  VERBATIM)
add_library(myLib out.c)
</code></pre>
<p>adds a custom command to run <code>someTool</code> to generate <code>out.c</code> and then compile the generated source as part of a library. The generation rule will re-run whenever <code>in.txt</code> changes. </p>
<p>New in version 3.20: One may use generator expressions to specify per-configuration outputs. For example, the code: </p>
<pre><code>add_custom_command(
  OUTPUT &quot;out-$&lt;CONFIG&gt;.c&quot;
  COMMAND someTool -i ${CMAKE_CURRENT_SOURCE_DIR}/in.txt
                   -o &quot;out-$&lt;CONFIG&gt;.c&quot;
                   -c &quot;$&lt;CONFIG&gt;&quot;
  DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/in.txt
  VERBATIM)
add_library(myLib &quot;out-$&lt;CONFIG&gt;.c&quot;)
</code></pre>
<p>adds a custom command to run <code>someTool</code> to generate <code>out-&lt;config&gt;.c</code>, where <code>&lt;config&gt;</code> is the build configuration, and then compile the generated source as part of a library. </p>
<h3>Build Events</h3>
<p>The second signature adds a custom command to a target such as a library or executable. This is useful for performing an operation before or after building the target. The command becomes part of the target and will only execute when the target itself is built. If the target is already built, the command will not execute. </p>
<pre><code>add_custom_command(TARGET &lt;target&gt;
                   PRE_BUILD | PRE_LINK | POST_BUILD
                   COMMAND command1 [ARGS] [args1...]
                   [COMMAND command2 [ARGS] [args2...] ...]
                   [BYPRODUCTS [files...]]
                   [WORKING_DIRECTORY dir]
                   [COMMENT comment]
                   [VERBATIM] [USES_TERMINAL]
                   [COMMAND_EXPAND_LISTS])
</code></pre>
<p>This defines a new command that will be associated with building the specified <code>&lt;target&gt;</code>. The <code>&lt;target&gt;</code> must be defined in the current directory; targets defined in other directories may not be specified. </p>
<p>When the command will happen is determined by which of the following is specified: </p>
<dl>
<dt><code>PRE_BUILD</code></dt>
<dd> <p> On Visual Studio Generators, run before any other rules are executed within the target. On other generators, run just before <code>PRE_LINK</code> commands. </p>
 </dd>
<dt><code>PRE_LINK</code></dt>
<dd> <p> Run after sources have been compiled but before linking the binary or running the librarian or archiver tool of a static library. This is not defined for targets created by the <code>add_custom_target()</code> command. </p>
 </dd>
<dt><code>POST_BUILD</code></dt>
<dd> <p> Run after all other rules within the target have been executed. </p>
<p> <code>NOTE:</code> Because generator expressions can be used in custom commands, it is possible to define <code>COMMAND</code> lines or whole custom commands which evaluate to empty strings for certain configurations. For <code>Visual Studio 2010 (and newer)</code> generators these command lines or custom commands will be omitted for the specific configuration and no &quot;empty-string-command&quot; will be added. </p>
<p>This allows to add individual build events for every configuration. </p>
<p>New in version 3.21: Support for target-dependent generator expressions. </p>
 </dd></dl>
<h3>Examples: Build Events</h3>
<p>A <code>POST_BUILD</code> event may be used to post-process a binary after linking. For example, the code: </p>
<pre><code>add_executable(myExe myExe.c)
add_custom_command(
  TARGET myExe POST_BUILD
  COMMAND someHasher -i &quot;$&lt;TARGET_FILE:myExe&gt;&quot;
                     -o &quot;$&lt;TARGET_FILE:myExe&gt;.hash&quot;
  VERBATIM)
</code></pre>
<p>will run <code>someHasher</code> to produce a <code>.hash</code> file next to the executable after linking. </p>
<p>New in version 3.20: One may use generator expressions to specify per-configuration byproducts. For example, the code: </p>
<pre><code>add_library(myPlugin MODULE myPlugin.c)
add_custom_command(
  TARGET myPlugin POST_BUILD
  COMMAND someHasher -i &quot;$&lt;TARGET_FILE:myPlugin&gt;&quot;
                     --as-code &quot;myPlugin-hash-$&lt;CONFIG&gt;.c&quot;
  BYPRODUCTS &quot;myPlugin-hash-$&lt;CONFIG&gt;.c&quot;
  VERBATIM)
add_executable(myExe myExe.c &quot;myPlugin-hash-$&lt;CONFIG&gt;.c&quot;)
</code></pre>
<p>will run <code>someHasher</code> after linking <code>myPlugin</code>, e.g. to produce a <code>.c</code> file containing code to check the hash of <code>myPlugin</code> that the <code>myExe</code> executable can use to verify it before loading. </p>
<h3>Ninja Multi-Config</h3>
<p>New in version 3.20: <code>add_custom_command</code> supports the <code>Ninja Multi-Config</code> generator&#8217;s cross-config capabilities. See the generator documentation for more information. </p>
<h3>add_custom_target</h3>
<p>Add a target with no output so it will always be built. </p>
<pre><code>add_custom_target(Name [ALL] [command1 [args1...]]
                  [COMMAND command2 [args2...] ...]
                  [DEPENDS depend depend depend ... ]
                  [BYPRODUCTS [files...]]
                  [WORKING_DIRECTORY dir]
                  [COMMENT comment]
                  [JOB_POOL job_pool]
                  [VERBATIM] [USES_TERMINAL]
                  [COMMAND_EXPAND_LISTS]
                  [SOURCES src1 [src2...]])
</code></pre>
<p>Adds a target with the given name that executes the given commands. The target has no output file and is <i>always considered out of date</i> even if the commands try to create a file with the name of the target. Use the <code>add_custom_command()</code> command to generate a file with dependencies. By default nothing depends on the custom target. Use the <code>add_dependencies()</code> command to add dependencies to or from other targets. </p>
<p>The options are: </p>
<dl>
<dt><code>ALL</code></dt>
<dd> <p> Indicate that this target should be added to the default build target so that it will be run every time (the command cannot be called <code>ALL</code>). </p>
 </dd>
<dt><code>BYPRODUCTS</code></dt>
<dd> <p> New in version 3.2. </p>
<p>Specify the files the command is expected to produce but whose modification time may or may not be updated on subsequent builds. If a byproduct name is a relative path it will be interpreted relative to the build tree directory corresponding to the current source directory. Each byproduct file will be marked with the <code>GENERATED</code> source file property automatically. </p>
<p>Explicit specification of byproducts is supported by the <code>Ninja</code> generator to tell the <code>ninja</code> build tool how to regenerate byproducts when they are missing. It is also useful when other build rules (e.g. custom commands) depend on the byproducts. Ninja requires a build rule for any generated file on which another rule depends even if there are order-only dependencies to ensure the byproducts will be available before their dependents build. </p>
<p>The Makefile Generators will remove <code>BYPRODUCTS</code> and other <code>GENERATED</code> files during <code>make clean</code>. </p>
<p>New in version 3.20: Arguments to <code>BYPRODUCTS</code> may use a restricted set of <code>generator expressions</code>. Target-dependent expressions are not permitted. </p>
 </dd>
<dt><code>COMMAND</code></dt>
<dd> <p> Specify the command-line(s) to execute at build time. If more than one <code>COMMAND</code> is specified they will be executed in order, but <i>not</i> necessarily composed into a stateful shell or batch script. (To run a full script, use the <code>configure_file()</code> command or the <code>file(GENERATE)</code> command to create it, and then specify a <code>COMMAND</code> to launch it.) </p>
<p>If <code>COMMAND</code> specifies an executable target name (created by the <code>add_executable()</code> command), it will automatically be replaced by the location of the executable created at build time if either of the following is true: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The target is not being cross-compiled (i.e. the <code>CMAKE_CROSSCOMPILING</code> variable is not set to true). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> New in version 3.6: The target is being cross-compiled and an emulator is provided (i.e. its <code>CROSSCOMPILING_EMULATOR</code> target property is set). In this case, the contents of <code>CROSSCOMPILING_EMULATOR</code> will be prepended to the command before the location of the target executable. </p>
<p>If neither of the above conditions are met, it is assumed that the command name is a program to be found on the <code>PATH</code> at build time. </p>
<p>Arguments to <code>COMMAND</code> may use <code>generator expressions</code>. Use the <code>TARGET_FILE</code> generator expression to refer to the location of a target later in the command line (i.e. as a command argument rather than as the command to execute). </p>
<p>Whenever one of the following target based generator expressions are used as a command to execute or is mentioned in a command argument, a target-level dependency will be added automatically so that the mentioned target will be built before this custom target (see policy <code>CMP0112</code>). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>TARGET_FILE</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>TARGET_LINKER_FILE</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>TARGET_SONAME_FILE</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>TARGET_PDB_FILE</code> </p>
<p>The command and arguments are optional and if not specified an empty target will be created. </p>
 </dd>
<dt><code>COMMENT</code></dt>
<dd> <p> Display the given message before the commands are executed at build time. </p>
 </dd>
<dt><code>DEPENDS</code></dt>
<dd> <p> Reference files and outputs of custom commands created with <code>add_custom_command()</code> command calls in the same directory (<code>CMakeLists.txt</code> file). They will be brought up to date when the target is built. </p>
<p>Changed in version 3.16: A target-level dependency is added if any dependency is a byproduct of a target or any of its build events in the same directory to ensure the byproducts will be available before this target is built. </p>
<p>Use the <code>add_dependencies()</code> command to add dependencies on other targets. </p>
 </dd>
<dt><code>COMMAND_EXPAND_LISTS</code></dt>
<dd> <p> New in version 3.8. </p>
<p>Lists in <code>COMMAND</code> arguments will be expanded, including those created with <code>generator expressions</code>, allowing <code>COMMAND</code> arguments such as <code>${CC} &quot;-I$&lt;JOIN:$&lt;TARGET_PROPERTY:foo,INCLUDE_DIRECTORIES&gt;,;-I&gt;&quot; foo.cc</code> to be properly expanded. </p>
 </dd>
<dt><code>JOB_POOL</code></dt>
<dd> <p> New in version 3.15. </p>
<p>Specify a <code>pool</code> for the <code>Ninja</code> generator. Incompatible with <code>USES_TERMINAL</code>, which implies the <code>console</code> pool. Using a pool that is not defined by <code>JOB_POOLS</code> causes an error by ninja at build time. </p>
 </dd>
<dt><code>SOURCES</code></dt>
<dd> <p> Specify additional source files to be included in the custom target. Specified source files will be added to IDE project files for convenience in editing even if they have no build rules. </p>
 </dd>
<dt><code>VERBATIM</code></dt>
<dd> <p> All arguments to the commands will be escaped properly for the build tool so that the invoked command receives each argument unchanged. Note that one level of escapes is still used by the CMake language processor before <code>add_custom_target</code> even sees the arguments. Use of <code>VERBATIM</code> is recommended as it enables correct behavior. When <code>VERBATIM</code> is not given the behavior is platform specific because there is no protection of tool-specific special characters. </p>
 </dd>
<dt><code>USES_TERMINAL</code></dt>
<dd> <p> New in version 3.2. </p>
<p>The command will be given direct access to the terminal if possible. With the <code>Ninja</code> generator, this places the command in the <code>console</code> <code>pool</code>. </p>
 </dd>
<dt><code>WORKING_DIRECTORY</code></dt>
<dd> <p> Execute the command with the given current working directory. If it is a relative path it will be interpreted relative to the build tree directory corresponding to the current source directory. </p>
<p>New in version 3.13: Arguments to <code>WORKING_DIRECTORY</code> may use <code>generator expressions</code>. </p>
 </dd></dl>
<h3>Ninja Multi-Config</h3>
<p>New in version 3.20: <code>add_custom_target</code> supports the <code>Ninja Multi-Config</code> generator&#8217;s cross-config capabilities. See the generator documentation for more information. </p>
<h3>add_definitions</h3>
<p>Add -D define flags to the compilation of source files. </p>
<pre><code>add_definitions(-DFOO -DBAR ...)
</code></pre>
<p>Adds definitions to the compiler command line for targets in the current directory, whether added before or after this command is invoked, and for the ones in sub-directories added after. This command can be used to add any flags, but it is intended to add preprocessor definitions. </p>
<p> <code>NOTE:</code> This command has been superseded by alternatives: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Use <code>add_compile_definitions()</code> to add preprocessor definitions. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use <code>include_directories()</code> to add include directories. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use <code>add_compile_options()</code> to add other options. </p>
<p>Flags beginning in <code>-D</code> or <code>/D</code> that look like preprocessor definitions are automatically added to the <code>COMPILE_DEFINITIONS</code> directory property for the current directory. Definitions with non-trivial values may be left in the set of flags instead of being converted for reasons of backwards compatibility. See documentation of the <code>directory</code>, <code>target</code>, <code>source file</code> <code>COMPILE_DEFINITIONS</code> properties for details on adding preprocessor definitions to specific scopes and configurations. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-buildsystem/">cmake-buildsystem</a>(7)</code> manual for more on defining buildsystem properties. </p>
 </dd></dl>
<h3>add_dependencies</h3>
<p>Add a dependency between top-level targets. </p>
<pre><code>add_dependencies(&lt;target&gt; [&lt;target-dependency&gt;]...)
</code></pre>
<p>Makes a top-level <code>&lt;target&gt;</code> depend on other top-level targets to ensure that they build before <code>&lt;target&gt;</code> does. A top-level target is one created by one of the <code>add_executable()</code>, <code>add_library()</code>, or <code>add_custom_target()</code> commands (but not targets generated by CMake like <code>install</code>). </p>
<p>Dependencies added to an imported target or an interface library are followed transitively in its place since the target itself does not build. </p>
<p>New in version 3.3: Allow adding dependencies to interface libraries. </p>
<p>See the <code>DEPENDS</code> option of <code>add_custom_target()</code> and <code>add_custom_command()</code> commands for adding file-level dependencies in custom rules. See the <code>OBJECT_DEPENDS</code> source file property to add file-level dependencies to object files.  </p>
<h3>add_executable</h3>
<p>Add an executable to the project using the specified source files.  </p>
<h3>Normal Executables</h3>
<pre><code>add_executable(&lt;name&gt; [WIN32] [MACOSX_BUNDLE]
               [EXCLUDE_FROM_ALL]
               [source1] [source2 ...])
</code></pre>
<p>Adds an executable target called <code>&lt;name&gt;</code> to be built from the source files listed in the command invocation. The <code>&lt;name&gt;</code> corresponds to the logical target name and must be globally unique within a project. The actual file name of the executable built is constructed based on conventions of the native platform (such as <code>&lt;name&gt;.exe</code> or just <code>&lt;name&gt;</code>). </p>
<p>New in version 3.1: Source arguments to <code>add_executable</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;...&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. </p>
<p>New in version 3.11: The source files can be omitted if they are added later using <code>target_sources()</code>. </p>
<p>By default the executable file will be created in the build tree directory corresponding to the source tree directory in which the command was invoked. See documentation of the <code>RUNTIME_OUTPUT_DIRECTORY</code> target property to change this location. See documentation of the <code>OUTPUT_NAME</code> target property to change the <code>&lt;name&gt;</code> part of the final file name. </p>
<p>If <code>WIN32</code> is given the property <code>WIN32_EXECUTABLE</code> will be set on the target created. See documentation of that target property for details. </p>
<p>If <code>MACOSX_BUNDLE</code> is given the corresponding property will be set on the created target. See documentation of the <code>MACOSX_BUNDLE</code> target property for details. </p>
<p>If <code>EXCLUDE_FROM_ALL</code> is given the corresponding property will be set on the created target. See documentation of the <code>EXCLUDE_FROM_ALL</code> target property for details. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-buildsystem/">cmake-buildsystem</a>(7)</code> manual for more on defining buildsystem properties. </p>
<p>See also <code>HEADER_FILE_ONLY</code> on what to do if some sources are pre-processed, and you want to have the original sources reachable from within IDE.  </p>
<h3>Imported Executables</h3>
<pre><code>add_executable(&lt;name&gt; IMPORTED [GLOBAL])
</code></pre>
<p>An IMPORTED executable target references an executable file located outside the project. No rules are generated to build it, and the <code>IMPORTED</code> target property is <code>True</code>. The target name has scope in the directory in which it is created and below, but the <code>GLOBAL</code> option extends visibility. It may be referenced like any target built within the project. <code>IMPORTED</code> executables are useful for convenient reference from commands like <code>add_custom_command()</code>. Details about the imported executable are specified by setting properties whose names begin in <code>IMPORTED_</code>. The most important such property is <code>IMPORTED_LOCATION</code> (and its per-configuration version <code>IMPORTED_LOCATION_&lt;CONFIG&gt;</code>) which specifies the location of the main executable file on disk. See documentation of the <code>IMPORTED_*</code> properties for more information.  </p>
<h3>Alias Executables</h3>
<pre><code>add_executable(&lt;name&gt; ALIAS &lt;target&gt;)
</code></pre>
<p>Creates an Alias Target, such that <code>&lt;name&gt;</code> can be used to refer to <code>&lt;target&gt;</code> in subsequent commands. The <code>&lt;name&gt;</code> does not appear in the generated buildsystem as a make target. The <code>&lt;target&gt;</code> may not be an <code>ALIAS</code>. </p>
<p>New in version 3.11: An <code>ALIAS</code> can target a <code>GLOBAL</code> Imported Target </p>
<p>New in version 3.18: An <code>ALIAS</code> can target a non-<code>GLOBAL</code> Imported Target. Such alias is scoped to the directory in which it is created and subdirectories. The <code>ALIAS_GLOBAL</code> target property can be used to check if the alias is global or not. </p>
<p> <code>ALIAS</code> targets can be used as targets to read properties from, executables for custom commands and custom targets. They can also be tested for existence with the regular <code>if(TARGET)</code> subcommand. The <code>&lt;name&gt;</code> may not be used to modify properties of <code>&lt;target&gt;</code>, that is, it may not be used as the operand of <code>set_property()</code>, <code>set_target_properties()</code>, <code>target_link_libraries()</code> etc. An <code>ALIAS</code> target may not be installed or exported.  </p>
<h3>add_library</h3>
<p>Add a library to the project using the specified source files.  </p>
<h3>Normal Libraries</h3>
<pre><code>add_library(&lt;name&gt; [STATIC | SHARED | MODULE]
            [EXCLUDE_FROM_ALL]
            [&lt;source&gt;...])
</code></pre>
<p>Adds a library target called <code>&lt;name&gt;</code> to be built from the source files listed in the command invocation. The <code>&lt;name&gt;</code> corresponds to the logical target name and must be globally unique within a project. The actual file name of the library built is constructed based on conventions of the native platform (such as <code>lib&lt;name&gt;.a</code> or <code>&lt;name&gt;.lib</code>). </p>
<p>New in version 3.1: Source arguments to <code>add_library</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;...&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. </p>
<p>New in version 3.11: The source files can be omitted if they are added later using <code>target_sources()</code>. </p>
<p> <code>STATIC</code>, <code>SHARED</code>, or <code>MODULE</code> may be given to specify the type of library to be created. <code>STATIC</code> libraries are archives of object files for use when linking other targets. <code>SHARED</code> libraries are linked dynamically and loaded at runtime. <code>MODULE</code> libraries are plugins that are not linked into other targets but may be loaded dynamically at runtime using dlopen-like functionality. If no type is given explicitly the type is <code>STATIC</code> or <code>SHARED</code> based on whether the current value of the variable <code>BUILD_SHARED_LIBS</code> is <code>ON</code>. For <code>SHARED</code> and <code>MODULE</code> libraries the <code>POSITION_INDEPENDENT_CODE</code> target property is set to <code>ON</code> automatically. A <code>SHARED</code> library may be marked with the <code>FRAMEWORK</code> target property to create an macOS Framework. </p>
<p>New in version 3.8: A <code>STATIC</code> library may be marked with the <code>FRAMEWORK</code> target property to create a static Framework. </p>
<p>If a library does not export any symbols, it must not be declared as a <code>SHARED</code> library. For example, a Windows resource DLL or a managed C++/CLI DLL that exports no unmanaged symbols would need to be a <code>MODULE</code> library. This is because CMake expects a <code>SHARED</code> library to always have an associated import library on Windows. </p>
<p>By default the library file will be created in the build tree directory corresponding to the source tree directory in which the command was invoked. See documentation of the <code>ARCHIVE_OUTPUT_DIRECTORY</code>, <code>LIBRARY_OUTPUT_DIRECTORY</code>, and <code>RUNTIME_OUTPUT_DIRECTORY</code> target properties to change this location. See documentation of the <code>OUTPUT_NAME</code> target property to change the <code>&lt;name&gt;</code> part of the final file name. </p>
<p>If <code>EXCLUDE_FROM_ALL</code> is given the corresponding property will be set on the created target. See documentation of the <code>EXCLUDE_FROM_ALL</code> target property for details. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-buildsystem/">cmake-buildsystem</a>(7)</code> manual for more on defining buildsystem properties. </p>
<p>See also <code>HEADER_FILE_ONLY</code> on what to do if some sources are pre-processed, and you want to have the original sources reachable from within IDE.  </p>
<h3>Object Libraries</h3>
<pre><code>add_library(&lt;name&gt; OBJECT [&lt;source&gt;...])
</code></pre>
<p>Creates an Object Library. An object library compiles source files but does not archive or link their object files into a library. Instead other targets created by <i>add_library()</i> or <code>add_executable()</code> may reference the objects using an expression of the form <code>$&lt;TARGET_OBJECTS:objlib&gt;</code> as a source, where <code>objlib</code> is the object library name. For example: </p>
<pre><code>add_library(... $&lt;TARGET_OBJECTS:objlib&gt; ...)
add_executable(... $&lt;TARGET_OBJECTS:objlib&gt; ...)
</code></pre>
<p>will include objlib&#8217;s object files in a library and an executable along with those compiled from their own sources. Object libraries may contain only sources that compile, header files, and other files that would not affect linking of a normal library (e.g. <code>.txt</code>). They may contain custom commands generating such sources, but not <code>PRE_BUILD</code>, <code>PRE_LINK</code>, or <code>POST_BUILD</code> commands. Some native build systems (such as Xcode) may not like targets that have only object files, so consider adding at least one real source file to any target that references <code>$&lt;TARGET_OBJECTS:objlib&gt;</code>. </p>
<p>New in version 3.12: Object libraries can be linked to with <code>target_link_libraries()</code>. </p>
<h3>Interface Libraries</h3>
<pre><code>add_library(&lt;name&gt; INTERFACE)
</code></pre>
<p>Creates an Interface Library. An <code>INTERFACE</code> library target does not compile sources and does not produce a library artifact on disk. However, it may have properties set on it and it may be installed and exported. Typically, <code>INTERFACE_*</code> properties are populated on an interface target using the commands: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>set_property()</code>, </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>target_link_libraries(INTERFACE)</code>, </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>target_link_options(INTERFACE)</code>, </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>target_include_directories(INTERFACE)</code>, </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>target_compile_options(INTERFACE)</code>, </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>target_compile_definitions(INTERFACE)</code>, and </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>target_sources(INTERFACE)</code>, </p>
<p>and then it is used as an argument to <code>target_link_libraries()</code> like any other target. </p>
<p>An interface library created with the above signature has no source files itself and is not included as a target in the generated buildsystem. </p>
<p>New in version 3.15: An interface library can have <code>PUBLIC_HEADER</code> and <code>PRIVATE_HEADER</code> properties. The headers specified by those properties can be installed using the <code>install(TARGETS)</code> command. </p>
<p>New in version 3.19: An interface library target may be created with source files: </p>
<pre><code>add_library(&lt;name&gt; INTERFACE [&lt;source&gt;...] [EXCLUDE_FROM_ALL])
</code></pre>
<p>Source files may be listed directly in the <code>add_library</code> call or added later by calls to <code>target_sources()</code> with the <code>PRIVATE</code> or <code>PUBLIC</code> keywords. </p>
<p>If an interface library has source files (i.e. the <code>SOURCES</code> target property is set), it will appear in the generated buildsystem as a build target much like a target defined by the <code>add_custom_target()</code> command. It does not compile any sources, but does contain build rules for custom commands created by the <code>add_custom_command()</code> command. </p>
<p> <code>NOTE:</code> In most command signatures where the <code>INTERFACE</code> keyword appears, the items listed after it only become part of that target&#8217;s usage requirements and are not part of the target&#8217;s own settings. However, in this signature of <code>add_library</code>, the <code>INTERFACE</code> keyword refers to the library type only. Sources listed after it in the <code>add_library</code> call are <code>PRIVATE</code> to the interface library and do not appear in its <code>INTERFACE_SOURCES</code> target property. </p>
 </dd></dl>
<h3>Imported Libraries</h3>
<pre><code>add_library(&lt;name&gt; &lt;type&gt; IMPORTED [GLOBAL])
</code></pre>
<p>Creates an IMPORTED library target called <code>&lt;name&gt;</code>. No rules are generated to build it, and the <code>IMPORTED</code> target property is <code>True</code>. The target name has scope in the directory in which it is created and below, but the <code>GLOBAL</code> option extends visibility. It may be referenced like any target built within the project. <code>IMPORTED</code> libraries are useful for convenient reference from commands like <code>target_link_libraries()</code>. Details about the imported library are specified by setting properties whose names begin in <code>IMPORTED_</code> and <code>INTERFACE_</code>. </p>
<p>The <code>&lt;type&gt;</code> must be one of: </p>
<dl>
<dt><code>STATIC</code>, <code>SHARED</code>, <code>MODULE</code>, <code>UNKNOWN</code></dt>
<dd> <p> References a library file located outside the project. The <code>IMPORTED_LOCATION</code> target property (or its per-configuration variant <code>IMPORTED_LOCATION_&lt;CONFIG&gt;</code>) specifies the location of the main library file on disk: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> For a <code>SHARED</code> library on most non-Windows platforms, the main library file is the <code>.so</code> or <code>.dylib</code> file used by both linkers and dynamic loaders. If the referenced library file has a <code>SONAME</code> (or on macOS, has a <code>LC_ID_DYLIB</code> starting in <code>@rpath/</code>), the value of that field should be set in the <code>IMPORTED_SONAME</code> target property. If the referenced library file does not have a <code>SONAME</code>, but the platform supports it, then the <code>IMPORTED_NO_SONAME</code> target property should be set. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> For a <code>SHARED</code> library on Windows, the <code>IMPORTED_IMPLIB</code> target property (or its per-configuration variant <code>IMPORTED_IMPLIB_&lt;CONFIG&gt;</code>) specifies the location of the DLL import library file (<code>.lib</code> or <code>.dll.a</code>) on disk, and the <code>IMPORTED_LOCATION</code> is the location of the <code>.dll</code> runtime library (and is optional, but needed by the <code>TARGET_RUNTIME_DLLS</code> generator expression). </p>
<p>Additional usage requirements may be specified in <code>INTERFACE_*</code> properties. </p>
<p>An <code>UNKNOWN</code> library type is typically only used in the implementation of Find Modules. It allows the path to an imported library (often found using the <code>find_library()</code> command) to be used without having to know what type of library it is. This is especially useful on Windows where a static library and a DLL&#8217;s import library both have the same file extension. </p>
 </dd>
<dt><code>OBJECT</code></dt>
<dd> <p> References a set of object files located outside the project. The <code>IMPORTED_OBJECTS</code> target property (or its per-configuration variant <code>IMPORTED_OBJECTS_&lt;CONFIG&gt;</code>) specifies the locations of object files on disk. Additional usage requirements may be specified in <code>INTERFACE_*</code> properties. </p>
 </dd>
<dt><code>INTERFACE</code></dt>
<dd> <p> Does not reference any library or object files on disk, but may specify usage requirements in <code>INTERFACE_*</code> properties. </p>
<p>See documentation of the <code>IMPORTED_*</code> and <code>INTERFACE_*</code> properties for more information. </p>
 </dd></dl>
<h3>Alias Libraries</h3>
<pre><code>add_library(&lt;name&gt; ALIAS &lt;target&gt;)
</code></pre>
<p>Creates an Alias Target, such that <code>&lt;name&gt;</code> can be used to refer to <code>&lt;target&gt;</code> in subsequent commands. The <code>&lt;name&gt;</code> does not appear in the generated buildsystem as a make target. The <code>&lt;target&gt;</code> may not be an <code>ALIAS</code>. </p>
<p>New in version 3.11: An <code>ALIAS</code> can target a <code>GLOBAL</code> Imported Target </p>
<p>New in version 3.18: An <code>ALIAS</code> can target a non-<code>GLOBAL</code> Imported Target. Such alias is scoped to the directory in which it is created and below. The <code>ALIAS_GLOBAL</code> target property can be used to check if the alias is global or not. </p>
<p> <code>ALIAS</code> targets can be used as linkable targets and as targets to read properties from. They can also be tested for existence with the regular <code>if(TARGET)</code> subcommand. The <code>&lt;name&gt;</code> may not be used to modify properties of <code>&lt;target&gt;</code>, that is, it may not be used as the operand of <code>set_property()</code>, <code>set_target_properties()</code>, <code>target_link_libraries()</code> etc. An <code>ALIAS</code> target may not be installed or exported.  </p>
<h3>add_link_options</h3>
<p>New in version 3.13. </p>
<p>Add options to the link step for executable, shared library or module library targets in the current directory and below that are added after this command is invoked. </p>
<pre><code>add_link_options(&lt;option&gt; ...)
</code></pre>
<p>This command can be used to add any link options, but alternative commands exist to add libraries (<code>target_link_libraries()</code> or <code>link_libraries()</code>). See documentation of the <code>directory</code> and <code>target</code> <code>LINK_OPTIONS</code> properties. </p>
<p> <code>NOTE:</code> This command cannot be used to add options for static library targets, since they do not use a linker. To add archiver or MSVC librarian flags, see the <code>STATIC_LIBRARY_OPTIONS</code> target property. </p>
<p>Arguments to <code>add_link_options</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;...&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake-buildsystem/">cmake-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.  </p>
<h3>Host And Device Specific Link Options</h3>
<p>New in version 3.18: When a device link step is involved, which is controlled by <code>CUDA_SEPARABLE_COMPILATION</code> and <code>CUDA_RESOLVE_DEVICE_SYMBOLS</code> properties and policy <code>CMP0105</code>, the raw options will be delivered to the host and device link steps (wrapped in <code>-Xcompiler</code> or equivalent for device link). Options wrapped with <code>$&lt;DEVICE_LINK:...&gt;</code> <code>generator expression</code> will be used only for the device link step. Options wrapped with <code>$&lt;HOST_LINK:...&gt;</code> <code>generator expression</code> will be used only for the host link step. </p>
<h3>Option De-duplication</h3>
<p>The final set of options used for a target is constructed by accumulating options from the current target and the usage requirements of its dependencies. The set of options is de-duplicated to avoid repetition. </p>
<p>New in version 3.12: While beneficial for individual options, the de-duplication step can break up option groups. For example, <code>-option A -option B</code> becomes <code>-option A B</code>. One may specify a group of options using shell-like quoting along with a <code>SHELL:</code> prefix. The <code>SHELL:</code> prefix is dropped, and the rest of the option string is parsed using the <code>separate_arguments()</code> <code>UNIX_COMMAND</code> mode. For example, <code>&quot;SHELL:-option A&quot; &quot;SHELL:-option B&quot;</code> becomes <code>-option A -option B</code>. </p>
<h3>Handling Compiler Driver Differences</h3>
<p>To pass options to the linker tool, each compiler driver has its own syntax. The <code>LINKER:</code> prefix and <code>,</code> separator can be used to specify, in a portable way, options to pass to the linker tool. <code>LINKER:</code> is replaced by the appropriate driver option and <code>,</code> by the appropriate driver separator. The driver prefix and driver separator are given by the values of the <code>CMAKE_&lt;LANG&gt;_LINKER_WRAPPER_FLAG</code> and <code>CMAKE_&lt;LANG&gt;_LINKER_WRAPPER_FLAG_SEP</code> variables. </p>
<p>For example, <code>&quot;LINKER:-z,defs&quot;</code> becomes <code>-Xlinker -z -Xlinker defs</code> for <code>Clang</code> and <code>-Wl,-z,defs</code> for <code>GNU GCC</code>. </p>
<p>The <code>LINKER:</code> prefix can be specified as part of a <code>SHELL:</code> prefix expression. </p>
<p>The <code>LINKER:</code> prefix supports, as an alternative syntax, specification of arguments using the <code>SHELL:</code> prefix and space as separator. The previous example then becomes <code>&quot;LINKER:SHELL:-z defs&quot;</code>. </p>
<p> <code>NOTE:</code> Specifying the <code>SHELL:</code> prefix anywhere other than at the beginning of the <code>LINKER:</code> prefix is not supported.  </p>
<h3>add_subdirectory</h3>
<p>Add a subdirectory to the build. </p>
<pre><code>add_subdirectory(source_dir [binary_dir] [EXCLUDE_FROM_ALL])
</code></pre>
<p>Adds a subdirectory to the build. The source_dir specifies the directory in which the source CMakeLists.txt and code files are located. If it is a relative path it will be evaluated with respect to the current directory (the typical usage), but it may also be an absolute path. The <code>binary_dir</code> specifies the directory in which to place the output files. If it is a relative path it will be evaluated with respect to the current output directory, but it may also be an absolute path. If <code>binary_dir</code> is not specified, the value of <code>source_dir</code>, before expanding any relative path, will be used (the typical usage). The CMakeLists.txt file in the specified source directory will be processed immediately by CMake before processing in the current input file continues beyond this command. </p>
<p>If the <code>EXCLUDE_FROM_ALL</code> argument is provided then targets in the subdirectory will not be included in the <code>ALL</code> target of the parent directory by default, and will be excluded from IDE project files. Users must explicitly build targets in the subdirectory. This is meant for use when the subdirectory contains a separate part of the project that is useful but not necessary, such as a set of examples. Typically the subdirectory should contain its own <code>project()</code> command invocation so that a full build system will be generated in the subdirectory (such as a VS IDE solution file). Note that inter-target dependencies supersede this exclusion. If a target built by the parent project depends on a target in the subdirectory, the dependee target will be included in the parent project build system to satisfy the dependency.  </p>
<h3>add_test</h3>
<p>Add a test to the project to be run by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>. </p>
<pre><code>add_test(NAME &lt;name&gt; COMMAND &lt;command&gt; [&lt;arg&gt;...]
         [CONFIGURATIONS &lt;config&gt;...]
         [WORKING_DIRECTORY &lt;dir&gt;]
         [COMMAND_EXPAND_LISTS])
</code></pre>
<p>Adds a test called <code>&lt;name&gt;</code>. The test name may contain arbitrary characters, expressed as a Quoted Argument or Bracket Argument if necessary. See policy <code>CMP0110</code>. The options are: </p>
<dl>
<dt><code>COMMAND</code></dt>
<dd> <p> Specify the test command-line. If <code>&lt;command&gt;</code> specifies an executable target (created by <code>add_executable()</code>) it will automatically be replaced by the location of the executable created at build time. </p>
 </dd>
<dt><code>CONFIGURATIONS</code></dt>
<dd> <p> Restrict execution of the test only to the named configurations. </p>
 </dd>
<dt><code>WORKING_DIRECTORY</code></dt>
<dd> <p> Set the <code>WORKING_DIRECTORY</code> test property to specify the working directory in which to execute the test. If not specified the test will be run with the current working directory set to the build directory corresponding to the current source directory. </p>
 </dd>
<dt><code>COMMAND_EXPAND_LISTS</code></dt>
<dd> <p> New in version 3.16. </p>
<p>Lists in <code>COMMAND</code> arguments will be expanded, including those created with <code>generator expressions</code>. </p>
<p>The given test command is expected to exit with code <code>0</code> to pass and non-zero to fail, or vice-versa if the <code>WILL_FAIL</code> test property is set. Any output written to stdout or stderr will be captured by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> but does not affect the pass/fail status unless the <code>PASS_REGULAR_EXPRESSION</code>, <code>FAIL_REGULAR_EXPRESSION</code> or <code>SKIP_REGULAR_EXPRESSION</code> test property is used. </p>
<p>New in version 3.16: Added <code>SKIP_REGULAR_EXPRESSION</code> property. </p>
<p>The <code>COMMAND</code> and <code>WORKING_DIRECTORY</code> options may use &quot;generator expressions&quot; with the syntax <code>$&lt;...&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. </p>
<p>Example usage: </p>
<pre><code>add_test(NAME mytest
         COMMAND testDriver --config $&lt;CONFIG&gt;
                            --exe $&lt;TARGET_FILE:myexe&gt;)
</code></pre>
<p>This creates a test <code>mytest</code> whose command runs a <code>testDriver</code> tool passing the configuration name and the full path to the executable file produced by target <code>myexe</code>. </p>
<p> <code>NOTE:</code> CMake will generate tests only if the <code>enable_testing()</code> command has been invoked. The <code>CTest</code> module invokes the command automatically unless the <code>BUILD_TESTING</code> option is turned <code>OFF</code>. </p>
<p> <center> ----<br/>
 </center> </p>
<pre><code>add_test(&lt;name&gt; &lt;command&gt; [&lt;arg&gt;...])
</code></pre>
<p>Add a test called <code>&lt;name&gt;</code> with the given command-line. Unlike the above <code>NAME</code> signature no transformation is performed on the command-line to support target names or generator expressions. </p>
 </dd></dl>
<h3>aux_source_directory</h3>
<p>Find all source files in a directory. </p>
<pre><code>aux_source_directory(&lt;dir&gt; &lt;variable&gt;)
</code></pre>
<p>Collects the names of all the source files in the specified directory and stores the list in the <code>&lt;variable&gt;</code> provided. This command is intended to be used by projects that use explicit template instantiation. Template instantiation files can be stored in a <code>Templates</code> subdirectory and collected automatically using this command to avoid manually listing all instantiations. </p>
<p>It is tempting to use this command to avoid writing the list of source files for a library or executable target. While this seems to work, there is no way for CMake to generate a build system that knows when a new source file has been added. Normally the generated build system knows when it needs to rerun CMake because the <code>CMakeLists.txt</code> file is modified to add a new source. When the source is just added to the directory without modifying this file, one would have to manually rerun CMake to generate a build system incorporating the new file.  </p>
<h3>build_command</h3>
<p>Get a command line to build the current project. This is mainly intended for internal use by the <code>CTest</code> module. </p>
<pre><code>build_command(&lt;variable&gt;
              [CONFIGURATION &lt;config&gt;]
              [PARALLEL_LEVEL &lt;parallel&gt;]
              [TARGET &lt;target&gt;]
              [PROJECT_NAME &lt;projname&gt;] # legacy, causes warning
             )
</code></pre>
<p>Sets the given <code>&lt;variable&gt;</code> to a command-line string of the form: </p>
<pre><code>&lt;cmake&gt; --build . [--config &lt;config&gt;] [--parallel &lt;parallel&gt;] [--target &lt;target&gt;...] [-- -i]
</code></pre>
<p>where <code>&lt;cmake&gt;</code> is the location of the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> command-line tool, and <code>&lt;config&gt;</code>, <code>&lt;parallel&gt;</code> and <code>&lt;target&gt;</code> are the values provided to the <code>CONFIGURATION</code>, <code>PARALLEL_LEVEL</code> and <code>TARGET</code> options, if any. The trailing <code>-- -i</code> option is added for Makefile Generators if policy <code>CMP0061</code> is not set to <code>NEW</code>. </p>
<p>When invoked, this <code>cmake --build</code> command line will launch the underlying build system tool. </p>
<p>New in version 3.21: The <code>PARALLEL_LEVEL</code> argument can be used to set the <code>--parallel</code> flag. </p>
<pre><code>build_command(&lt;cachevariable&gt; &lt;makecommand&gt;)
</code></pre>
<p>This second signature is deprecated, but still available for backwards compatibility. Use the first signature instead. </p>
<p>It sets the given <code>&lt;cachevariable&gt;</code> to a command-line string as above but without the <code>--target</code> option. The <code>&lt;makecommand&gt;</code> is ignored but should be the full path to devenv, nmake, make or one of the end user build tools for legacy invocations. </p>
<p> <code>NOTE:</code> In CMake versions prior to 3.0 this command returned a command line that directly invokes the native build tool for the current generator. Their implementation of the <code>PROJECT_NAME</code> option had no useful effects, so CMake now warns on use of the option.  </p>
<h3>create_test_sourcelist</h3>
<p>Create a test driver and source list for building test programs. </p>
<pre><code>create_test_sourcelist(sourceListName driverName
                       test1 test2 test3
                       EXTRA_INCLUDE include.h
                       FUNCTION function)
</code></pre>
<p>A test driver is a program that links together many small tests into a single executable. This is useful when building static executables with large libraries to shrink the total required size. The list of source files needed to build the test driver will be in <code>sourceListName</code>. <code>driverName</code> is the name of the test driver program. The rest of the arguments consist of a list of test source files, can be semicolon separated. Each test source file should have a function in it that is the same name as the file with no extension (foo.cxx should have int foo(int, char*[]);) <code>driverName</code> will be able to call each of the tests by name on the command line. If <code>EXTRA_INCLUDE</code> is specified, then the next argument is included into the generated file. If <code>FUNCTION</code> is specified, then the next argument is taken as a function name that is passed a pointer to ac and av. This can be used to add extra command line processing to each test. The <code>CMAKE_TESTDRIVER_BEFORE_TESTMAIN</code> cmake variable can be set to have code that will be placed directly before calling the test main function. <code>CMAKE_TESTDRIVER_AFTER_TESTMAIN</code> can be set to have code that will be placed directly after the call to the test main function.  </p>
<h3>define_property</h3>
<p>Define and document custom properties. </p>
<pre><code>define_property(&lt;GLOBAL | DIRECTORY | TARGET | SOURCE |
                 TEST | VARIABLE | CACHED_VARIABLE&gt;
                 PROPERTY &lt;name&gt; [INHERITED]
                 BRIEF_DOCS &lt;brief-doc&gt; [docs...]
                 FULL_DOCS &lt;full-doc&gt; [docs...])
</code></pre>
<p>Defines one property in a scope for use with the <code>set_property()</code> and <code>get_property()</code> commands. This is primarily useful to associate documentation with property names that may be retrieved with the <code>get_property()</code> command. The first argument determines the kind of scope in which the property should be used. It must be one of the following: </p>
<pre><code>GLOBAL = associated with the global namespace
DIRECTORY = associated with one directory
TARGET = associated with one target
SOURCE = associated with one source file
TEST = associated with a test named with add_test
VARIABLE = documents a CMake language variable
CACHED_VARIABLE = documents a CMake cache variable
</code></pre>
<p>Note that unlike <code>set_property()</code> and <code>get_property()</code> no actual scope needs to be given; only the kind of scope is important. </p>
<p>The required <code>PROPERTY</code> option is immediately followed by the name of the property being defined. </p>
<p>If the <code>INHERITED</code> option is given, then the <code>get_property()</code> command will chain up to the next higher scope when the requested property is not set in the scope given to the command. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>DIRECTORY</code> scope chains to its parent directory&#8217;s scope, continuing the walk up parent directories until a directory has the property set or there are no more parents. If still not found at the top level directory, it chains to the <code>GLOBAL</code> scope. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>TARGET</code>, <code>SOURCE</code> and <code>TEST</code> properties chain to <code>DIRECTORY</code> scope, including further chaining up the directories, etc. as needed. </p>
<p>Note that this scope chaining behavior only applies to calls to <code>get_property()</code>, <code>get_directory_property()</code>, <code>get_target_property()</code>, <code>get_source_file_property()</code> and <code>get_test_property()</code>. There is no inheriting behavior when <i>setting</i> properties, so using <code>APPEND</code> or <code>APPEND_STRING</code> with the <code>set_property()</code> command will not consider inherited values when working out the contents to append to. </p>
<p>The <code>BRIEF_DOCS</code> and <code>FULL_DOCS</code> options are followed by strings to be associated with the property as its brief and full documentation. Corresponding options to the <code>get_property()</code> command will retrieve the documentation. </p>
 </dd></dl>
<h3>enable_language</h3>
<p>Enable a language (CXX/C/OBJC/OBJCXX/Fortran/etc) </p>
<pre><code>enable_language(&lt;lang&gt; [OPTIONAL] )
</code></pre>
<p>Enables support for the named language in CMake. This is the same as the <code>project()</code> command but does not create any of the extra variables that are created by the project command. Example languages are <code>CXX</code>, <code>C</code>, <code>CUDA</code>, <code>OBJC</code>, <code>OBJCXX</code>, <code>Fortran</code>, <code>HIP</code>, <code>ISPC</code>, and <code>ASM</code>. </p>
<p>New in version 3.8: Added <code>CUDA</code> support. </p>
<p>New in version 3.16: Added <code>OBJC</code> and <code>OBJCXX</code> support. </p>
<p>New in version 3.18: Added <code>ISPC</code> support. </p>
<p>New in version 3.21: Added <code>HIP</code> support. </p>
<p>If enabling <code>ASM</code>, enable it last so that CMake can check whether compilers for other languages like <code>C</code> work for assembly too. </p>
<p>This command must be called in file scope, not in a function call. Furthermore, it must be called in the highest directory common to all targets using the named language directly for compiling sources or indirectly through link dependencies. It is simplest to enable all needed languages in the top-level directory of a project. </p>
<p>The <code>OPTIONAL</code> keyword is a placeholder for future implementation and does not currently work. Instead you can use the <code>CheckLanguage</code> module to verify support before enabling.  </p>
<h3>enable_testing</h3>
<p>Enable testing for current directory and below. </p>
<pre><code>enable_testing()
</code></pre>
<p>Enables testing for this directory and below. </p>
<p>This command should be in the source directory root because ctest expects to find a test file in the build directory root. </p>
<p>This command is automatically invoked when the <code>CTest</code> module is included, except if the <code>BUILD_TESTING</code> option is turned off. </p>
<p>See also the <code>add_test()</code> command.  </p>
<h3>export</h3>
<p>Export targets from the build tree for use by outside projects. </p>
<pre><code>export(EXPORT &lt;export-name&gt; [NAMESPACE &lt;namespace&gt;] [FILE &lt;filename&gt;])
</code></pre>
<p>Creates a file <code>&lt;filename&gt;</code> that may be included by outside projects to import targets from the current project&#8217;s build tree. This is useful during cross-compiling to build utility executables that can run on the host platform in one project and then import them into another project being compiled for the target platform. If the <code>NAMESPACE</code> option is given the <code>&lt;namespace&gt;</code> string will be prepended to all target names written to the file. </p>
<p>Target installations are associated with the export <code>&lt;export-name&gt;</code> using the <code>EXPORT</code> option of the <code>install(TARGETS)</code> command. </p>
<p>The file created by this command is specific to the build tree and should never be installed. See the <code>install(EXPORT)</code> command to export targets from an installation tree. </p>
<p>The properties set on the generated IMPORTED targets will have the same values as the final values of the input TARGETS. </p>
<pre><code>export(TARGETS [target1 [target2 [...]]] [NAMESPACE &lt;namespace&gt;]
       [APPEND] FILE &lt;filename&gt; [EXPORT_LINK_INTERFACE_LIBRARIES])
</code></pre>
<p>This signature is similar to the <code>EXPORT</code> signature, but targets are listed explicitly rather than specified as an export-name. If the APPEND option is given the generated code will be appended to the file instead of overwriting it. The EXPORT_LINK_INTERFACE_LIBRARIES keyword, if present, causes the contents of the properties matching <code>(IMPORTED_)?LINK_INTERFACE_LIBRARIES(_&lt;CONFIG&gt;)?</code> to be exported, when policy CMP0022 is NEW. If a library target is included in the export but a target to which it links is not included the behavior is unspecified. </p>
<p> <code>NOTE:</code> Object Libraries under <code>Xcode</code> have special handling if multiple architectures are listed in <code>CMAKE_OSX_ARCHITECTURES</code>. In this case they will be exported as Interface Libraries with no object files available to clients. This is sufficient to satisfy transitive usage requirements of other targets that link to the object libraries in their implementation. </p>
<pre><code>export(PACKAGE &lt;PackageName&gt;)
</code></pre>
<p>Store the current build directory in the CMake user package registry for package <code>&lt;PackageName&gt;</code>. The <code>find_package()</code> command may consider the directory while searching for package <code>&lt;PackageName&gt;</code>. This helps dependent projects find and use a package from the current project&#8217;s build tree without help from the user. Note that the entry in the package registry that this command creates works only in conjunction with a package configuration file (<code>&lt;PackageName&gt;Config.cmake</code>) that works with the build tree. In some cases, for example for packaging and for system wide installations, it is not desirable to write the user package registry. </p>
<p>Changed in version 3.1: If the <code>CMAKE_EXPORT_NO_PACKAGE_REGISTRY</code> variable is enabled, the <code>export(PACKAGE)</code> command will do nothing. </p>
<p>Changed in version 3.15: By default the <code>export(PACKAGE)</code> command does nothing (see policy <code>CMP0090</code>) because populating the user package registry has effects outside the source and build trees. Set the <code>CMAKE_EXPORT_PACKAGE_REGISTRY</code> variable to add build directories to the CMake user package registry. </p>
<pre><code>export(TARGETS [target1 [target2 [...]]] [ANDROID_MK &lt;filename&gt;])
</code></pre>
<p>New in version 3.7. </p>
<p>This signature exports cmake built targets to the android ndk build system by creating an Android.mk file that references the prebuilt targets. The Android NDK supports the use of prebuilt libraries, both static and shared. This allows cmake to build the libraries of a project and make them available to an ndk build system complete with transitive dependencies, include flags and defines required to use the libraries. The signature takes a list of targets and puts them in the Android.mk file specified by the <code>&lt;filename&gt;</code> given. This signature can only be used if policy CMP0022 is NEW for all targets given. A error will be issued if that policy is set to OLD for one of the targets.  </p>
<h3>fltk_wrap_ui</h3>
<p>Create FLTK user interfaces Wrappers. </p>
<pre><code>fltk_wrap_ui(resultingLibraryName source1
             source2 ... sourceN )
</code></pre>
<p>Produce .h and .cxx files for all the .fl and .fld files listed. The resulting .h and .cxx files will be added to a variable named <code>resultingLibraryName_FLTK_UI_SRCS</code> which should be added to your library.  </p>
<h3>get_source_file_property</h3>
<p>Get a property for a source file. </p>
<pre><code>get_source_file_property(&lt;variable&gt; &lt;file&gt;
                         [DIRECTORY &lt;dir&gt; | TARGET_DIRECTORY &lt;target&gt;]
                         &lt;property&gt;)
</code></pre>
<p>Gets a property from a source file. The value of the property is stored in the specified <code>&lt;variable&gt;</code>. If the source property is not found, the behavior depends on whether it has been defined to be an <code>INHERITED</code> property or not (see <code>define_property()</code>). Non-inherited properties will set <code>variable</code> to <code>NOTFOUND</code>, whereas inherited properties will search the relevant parent scope as described for the <code>define_property()</code> command and if still unable to find the property, <code>variable</code> will be set to an empty string. </p>
<p>By default, the source file&#8217;s property will be read from the current source directory&#8217;s scope. </p>
<p>New in version 3.18: Directory scope can be overridden with one of the following sub-options: </p>
<dl>
<dt><code>DIRECTORY &lt;dir&gt;</code></dt>
<dd> <p> The source file property will be read from the <code>&lt;dir&gt;</code> directory&#8217;s scope. CMake must already know about that source directory, either by having added it through a call to <code>add_subdirectory()</code> or <code>&lt;dir&gt;</code> being the top level source directory. Relative paths are treated as relative to the current source directory. </p>
 </dd>
<dt><code>TARGET_DIRECTORY &lt;target&gt;</code></dt>
<dd> <p> The source file property will be read from the directory scope in which <code>&lt;target&gt;</code> was created (<code>&lt;target&gt;</code> must therefore already exist). </p>
<p>Use <code>set_source_files_properties()</code> to set property values. Source file properties usually control how the file is built. One property that is always there is <code>LOCATION</code>. </p>
<p>See also the more general <code>get_property()</code> command. </p>
<p> <code>NOTE:</code> The <code>GENERATED</code> source file property may be globally visible. See its documentation for details. </p>
 </dd></dl>
<h3>get_target_property</h3>
<p>Get a property from a target. </p>
<pre><code>get_target_property(&lt;VAR&gt; target property)
</code></pre>
<p>Get a property from a target. The value of the property is stored in the variable <code>&lt;VAR&gt;</code>. If the target property is not found, the behavior depends on whether it has been defined to be an <code>INHERITED</code> property or not (see <code>define_property()</code>). Non-inherited properties will set <code>&lt;VAR&gt;</code> to <code>&lt;VAR&gt;-NOTFOUND</code>, whereas inherited properties will search the relevant parent scope as described for the <code>define_property()</code> command and if still unable to find the property, <code>&lt;VAR&gt;</code> will be set to an empty string. </p>
<p>Use <code>set_target_properties()</code> to set target property values. Properties are usually used to control how a target is built, but some query the target instead. This command can get properties for any target so far created. The targets do not need to be in the current <code>CMakeLists.txt</code> file. </p>
<p>See also the more general <code>get_property()</code> command. </p>
<p>See Target Properties for the list of properties known to CMake.  </p>
<h3>get_test_property</h3>
<p>Get a property of the test. </p>
<pre><code>get_test_property(test property VAR)
</code></pre>
<p>Get a property from the test. The value of the property is stored in the variable <code>VAR</code>. If the test property is not found, the behavior depends on whether it has been defined to be an <code>INHERITED</code> property or not (see <code>define_property()</code>). Non-inherited properties will set <code>VAR</code> to &quot;NOTFOUND&quot;, whereas inherited properties will search the relevant parent scope as described for the <code>define_property()</code> command and if still unable to find the property, <code>VAR</code> will be set to an empty string. </p>
<p>For a list of standard properties you can type <code>cmake --help-property-list</code>. </p>
<p>See also the more general <code>get_property()</code> command.  </p>
<h3>include_directories</h3>
<p>Add include directories to the build. </p>
<pre><code>include_directories([AFTER|BEFORE] [SYSTEM] dir1 [dir2 ...])
</code></pre>
<p>Add the given directories to those the compiler uses to search for include files. Relative paths are interpreted as relative to the current source directory. </p>
<p>The include directories are added to the <code>INCLUDE_DIRECTORIES</code> directory property for the current <code>CMakeLists</code> file. They are also added to the <code>INCLUDE_DIRECTORIES</code> target property for each target in the current <code>CMakeLists</code> file. The target property values are the ones used by the generators. </p>
<p>By default the directories specified are appended onto the current list of directories. This default behavior can be changed by setting <code>CMAKE_INCLUDE_DIRECTORIES_BEFORE</code> to <code>ON</code>. By using <code>AFTER</code> or <code>BEFORE</code> explicitly, you can select between appending and prepending, independent of the default. </p>
<p>If the <code>SYSTEM</code> option is given, the compiler will be told the directories are meant as system include directories on some platforms. Signalling this setting might achieve effects such as the compiler skipping warnings, or these fixed-install system files not being considered in dependency calculations - see compiler docs. </p>
<p>Arguments to <code>include_directories</code> may use &quot;generator expressions&quot; with the syntax &quot;$&lt;...&gt;&quot;. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake-buildsystem/">cmake-buildsystem</a>(7)</code> manual for more on defining buildsystem properties. </p>
<p> <code>NOTE:</code> Prefer the <code>target_include_directories()</code> command to add include directories to individual targets and optionally propagate/export them to dependents.  </p>
<h3>include_external_msproject</h3>
<p>Include an external Microsoft project file in a workspace. </p>
<pre><code>include_external_msproject(projectname location
                           [TYPE projectTypeGUID]
                           [GUID projectGUID]
                           [PLATFORM platformName]
                           dep1 dep2 ...)
</code></pre>
<p>Includes an external Microsoft project in the generated workspace file. Currently does nothing on UNIX. This will create a target named <code>[projectname]</code>. This can be used in the <code>add_dependencies()</code> command to make things depend on the external project. </p>
<p> <code>TYPE</code>, <code>GUID</code> and <code>PLATFORM</code> are optional parameters that allow one to specify the type of project, id (<code>GUID</code>) of the project and the name of the target platform. This is useful for projects requiring values other than the default (e.g. WIX projects). </p>
<p>New in version 3.9: If the imported project has different configuration names than the current project, set the <code>MAP_IMPORTED_CONFIG_&lt;CONFIG&gt;</code> target property to specify the mapping. </p>
<h3>include_regular_expression</h3>
<p>Set the regular expression used for dependency checking. </p>
<pre><code>include_regular_expression(regex_match [regex_complain])
</code></pre>
<p>Sets the regular expressions used in dependency checking. Only files matching <code>regex_match</code> will be traced as dependencies. Only files matching <code>regex_complain</code> will generate warnings if they cannot be found (standard header paths are not searched). The defaults are: </p>
<pre><code>regex_match = &quot;^.*$&quot; (match everything)
regex_complain = &quot;^$&quot; (match empty string only)
</code></pre>
<h3>install</h3>
<p>Specify rules to run at install time.  </p>
<h3>Synopsis</h3>
<pre><code>install( TARGETS  &lt;target&gt;... [...])
install( IMPORTED_RUNTIME_ARTIFACTS  &lt;target&gt;... [...])
install({ FILES  | PROGRAMS } &lt;file&gt;... [...])
install( DIRECTORY  &lt;dir&gt;... [...])
install( SCRIPT  &lt;file&gt; [...])
install( CODE  &lt;code&gt; [...])
install( EXPORT  &lt;export-name&gt; [...])
install( RUNTIME_DEPENDENCY_SET  &lt;set-name&gt; [...])
</code></pre>
<h3>Introduction</h3>
<p>This command generates installation rules for a project. Install rules specified by calls to the <code>install()</code> command within a source directory are executed in order during installation. </p>
<p>Changed in version 3.14: Install rules in subdirectories added by calls to the <code>add_subdirectory()</code> command are interleaved with those in the parent directory to run in the order declared (see policy <code>CMP0082</code>). </p>
<p>Changed in version 3.22: The environment variable <code>CMAKE_INSTALL_MODE</code> can override the default copying behavior of <i>install()</i>. </p>
<p>There are multiple signatures for this command. Some of them define installation options for files and targets. Options common to multiple signatures are covered here but they are valid only for signatures that specify them. The common options are: </p>
<dl>
<dt><code>DESTINATION</code></dt>
<dd> <p> Specify the directory on disk to which a file will be installed. Arguments can be relative or absolute paths. </p>
<p>If a relative path is given it is interpreted relative to the value of the <code>CMAKE_INSTALL_PREFIX</code> variable. The prefix can be relocated at install time using the <code>DESTDIR</code> mechanism explained in the <code>CMAKE_INSTALL_PREFIX</code> variable documentation. </p>
<p>If an absolute path (with a leading slash or drive letter) is given it is used verbatim. </p>
<p>As absolute paths are not supported by <code>cpack</code> installer generators, it is preferable to use relative paths throughout. In particular, there is no need to make paths absolute by prepending <code>CMAKE_INSTALL_PREFIX</code>; this prefix is used by default if the DESTINATION is a relative path. </p>
 </dd>
<dt><code>PERMISSIONS</code></dt>
<dd> <p> Specify permissions for installed files. Valid permissions are <code>OWNER_READ</code>, <code>OWNER_WRITE</code>, <code>OWNER_EXECUTE</code>, <code>GROUP_READ</code>, <code>GROUP_WRITE</code>, <code>GROUP_EXECUTE</code>, <code>WORLD_READ</code>, <code>WORLD_WRITE</code>, <code>WORLD_EXECUTE</code>, <code>SETUID</code>, and <code>SETGID</code>. Permissions that do not make sense on certain platforms are ignored on those platforms. </p>
 </dd>
<dt><code>CONFIGURATIONS</code></dt>
<dd> <p> Specify a list of build configurations for which the install rule applies (Debug, Release, etc.). Note that the values specified for this option only apply to options listed AFTER the <code>CONFIGURATIONS</code> option. For example, to set separate install paths for the Debug and Release configurations, do the following: </p>
<pre><code>install(TARGETS target
        CONFIGURATIONS Debug
        RUNTIME DESTINATION Debug/bin)
install(TARGETS target
        CONFIGURATIONS Release
        RUNTIME DESTINATION Release/bin)
</code></pre>
<p>Note that <code>CONFIGURATIONS</code> appears BEFORE <code>RUNTIME DESTINATION</code>. </p>
 </dd>
<dt><code>COMPONENT</code></dt>
<dd> <p> Specify an installation component name with which the install rule is associated, such as &quot;runtime&quot; or &quot;development&quot;. During component-specific installation only install rules associated with the given component name will be executed. During a full installation all components are installed unless marked with <code>EXCLUDE_FROM_ALL</code>. If <code>COMPONENT</code> is not provided a default component &quot;Unspecified&quot; is created. The default component name may be controlled with the <code>CMAKE_INSTALL_DEFAULT_COMPONENT_NAME</code> variable. </p>
 </dd>
<dt><code>EXCLUDE_FROM_ALL</code></dt>
<dd> <p> New in version 3.6. </p>
<p>Specify that the file is excluded from a full installation and only installed as part of a component-specific installation </p>
 </dd>
<dt><code>RENAME</code></dt>
<dd> <p> Specify a name for an installed file that may be different from the original file. Renaming is allowed only when a single file is installed by the command. </p>
 </dd>
<dt><code>OPTIONAL</code></dt>
<dd> <p> Specify that it is not an error if the file to be installed does not exist. </p>
<p>New in version 3.1: Command signatures that install files may print messages during installation. Use the <code>CMAKE_INSTALL_MESSAGE</code> variable to control which messages are printed. </p>
<p>New in version 3.11: Many of the <code>install()</code> variants implicitly create the directories containing the installed files. If <code>CMAKE_INSTALL_DEFAULT_DIRECTORY_PERMISSIONS</code> is set, these directories will be created with the permissions specified. Otherwise, they will be created according to the uname rules on Unix-like platforms. Windows platforms are unaffected. </p>
 </dd></dl>
<h3>Installing Targets</h3>
<pre><code>install(TARGETS targets... [EXPORT &lt;export-name&gt;]
        [RUNTIME_DEPENDENCIES args...|RUNTIME_DEPENDENCY_SET &lt;set-name&gt;]
        [[ARCHIVE|LIBRARY|RUNTIME|OBJECTS|FRAMEWORK|BUNDLE|
          PRIVATE_HEADER|PUBLIC_HEADER|RESOURCE]
         [DESTINATION &lt;dir&gt;]
         [PERMISSIONS permissions...]
         [CONFIGURATIONS [Debug|Release|...]]
         [COMPONENT &lt;component&gt;]
         [NAMELINK_COMPONENT &lt;component&gt;]
         [OPTIONAL] [EXCLUDE_FROM_ALL]
         [NAMELINK_ONLY|NAMELINK_SKIP]
        ] [...]
        [INCLUDES DESTINATION [&lt;dir&gt; ...]]
        )
</code></pre>
<p>The <code>TARGETS</code> form specifies rules for installing targets from a project. There are several kinds of target Output Artifacts that may be installed: </p>
<dl>
<dt><code>ARCHIVE</code></dt>
<dd> <p> Target artifacts of this kind include: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>Static libraries</i> (except on macOS when marked as <code>FRAMEWORK</code>, see below); </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>DLL import libraries</i> (on all Windows-based systems including Cygwin; they have extension <code>.lib</code>, in contrast to the <code>.dll</code> libraries that go to <code>RUNTIME</code>); </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On AIX, the <i>linker import file</i> created for executables with <code>ENABLE_EXPORTS</code> enabled. </p>
 </dd>
<dt><code>LIBRARY</code></dt>
<dd> <p> Target artifacts of this kind include: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>Shared libraries</i>, except </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> DLLs (these go to <code>RUNTIME</code>, see below), </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> on macOS when marked as <code>FRAMEWORK</code> (see below). </p>
 </dd>
<dt><code>RUNTIME</code></dt>
<dd> <p> Target artifacts of this kind include: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>Executables</i> (except on macOS when marked as <code>MACOSX_BUNDLE</code>, see <code>BUNDLE</code> below); </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> DLLs (on all Windows-based systems including Cygwin; note that the accompanying import libraries are of kind <code>ARCHIVE</code>). </p>
 </dd>
<dt><code>OBJECTS</code></dt>
<dd> <p> New in version 3.9. </p>
<p>Object files associated with <i>object libraries</i>. </p>
 </dd>
<dt><code>FRAMEWORK</code></dt>
<dd> <p> Both static and shared libraries marked with the <code>FRAMEWORK</code> property are treated as <code>FRAMEWORK</code> targets on macOS. </p>
 </dd>
<dt><code>BUNDLE</code></dt>
<dd> <p> Executables marked with the <code>MACOSX_BUNDLE</code> property are treated as <code>BUNDLE</code> targets on macOS. </p>
 </dd>
<dt><code>PUBLIC_HEADER</code></dt>
<dd> <p> Any <code>PUBLIC_HEADER</code> files associated with a library are installed in the destination specified by the <code>PUBLIC_HEADER</code> argument on non-Apple platforms. Rules defined by this argument are ignored for <code>FRAMEWORK</code> libraries on Apple platforms because the associated files are installed into the appropriate locations inside the framework folder. See <code>PUBLIC_HEADER</code> for details. </p>
 </dd>
<dt><code>PRIVATE_HEADER</code></dt>
<dd> <p> Similar to <code>PUBLIC_HEADER</code>, but for <code>PRIVATE_HEADER</code> files. See <code>PRIVATE_HEADER</code> for details. </p>
 </dd>
<dt><code>RESOURCE</code></dt>
<dd> <p> Similar to <code>PUBLIC_HEADER</code> and <code>PRIVATE_HEADER</code>, but for <code>RESOURCE</code> files. See <code>RESOURCE</code> for details. </p>
<p>For each of these arguments given, the arguments following them only apply to the target or file type specified in the argument. If none is given, the installation properties apply to all target types. If only one is given then only targets of that type will be installed (which can be used to install just a DLL or just an import library.) </p>
<p>For regular executables, static libraries and shared libraries, the <code>DESTINATION</code> argument is not required. For these target types, when <code>DESTINATION</code> is omitted, a default destination will be taken from the appropriate variable from <code>GNUInstallDirs</code>, or set to a built-in default value if that variable is not defined. The same is true for the public and private headers associated with the installed targets through the <code>PUBLIC_HEADER</code> and <code>PRIVATE_HEADER</code> target properties. A destination must always be provided for module libraries, Apple bundles and frameworks. A destination can be omitted for interface and object libraries, but they are handled differently (see the discussion of this topic toward the end of this section). </p>
<p>The following table shows the target types with their associated variables and built-in defaults that apply when no destination is given: <center> </p>
<table>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> Target Type </td>
<td> GNUInstallDirs Variable </td>
<td> Built-In Default 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>RUNTIME</code> </td>
<td> <code>${CMAKE_INSTALL_BINDIR}</code> </td>
<td> <code>bin</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>LIBRARY</code> </td>
<td> <code>${CMAKE_INSTALL_LIBDIR}</code> </td>
<td> <code>lib</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>ARCHIVE</code> </td>
<td> <code>${CMAKE_INSTALL_LIBDIR}</code> </td>
<td> <code>lib</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>PRIVATE_HEADER</code> </td>
<td> <code>${CMAKE_INSTALL_INCLUDEDIR}</code> </td>
<td> <code>include</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>PUBLIC_HEADER</code> </td>
<td> <code>${CMAKE_INSTALL_INCLUDEDIR}</code> </td>
<td> <code>include</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
</table>
<p> </center> </p>
<p>Projects wishing to follow the common practice of installing headers into a project-specific subdirectory will need to provide a destination rather than rely on the above. </p>
<p>To make packages compliant with distribution filesystem layout policies, if projects must specify a <code>DESTINATION</code>, it is recommended that they use a path that begins with the appropriate <code>GNUInstallDirs</code> variable. This allows package maintainers to control the install destination by setting the appropriate cache variables. The following example shows a static library being installed to the default destination provided by <code>GNUInstallDirs</code>, but with its headers installed to a project-specific subdirectory that follows the above recommendation: </p>
<pre><code>add_library(mylib STATIC ...)
set_target_properties(mylib PROPERTIES PUBLIC_HEADER mylib.h)
include(GNUInstallDirs)
install(TARGETS mylib
        PUBLIC_HEADER
          DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/myproj
)
</code></pre>
<p>In addition to the common options listed above, each target can accept the following additional arguments: </p>
 </dd>
<dt><code>NAMELINK_COMPONENT</code></dt>
<dd> <p> New in version 3.12. </p>
<p>On some platforms a versioned shared library has a symbolic link such as: </p>
<pre><code>lib&lt;name&gt;.so -&gt; lib&lt;name&gt;.so.1
</code></pre>
<p>where <code>lib&lt;name&gt;.so.1</code> is the soname of the library and <code>lib&lt;name&gt;.so</code> is a &quot;namelink&quot; allowing linkers to find the library when given <code>-l&lt;name&gt;</code>. The <code>NAMELINK_COMPONENT</code> option is similar to the <code>COMPONENT</code> option, but it changes the installation component of a shared library namelink if one is generated. If not specified, this defaults to the value of <code>COMPONENT</code>. It is an error to use this parameter outside of a <code>LIBRARY</code> block. </p>
<p>Consider the following example: </p>
<pre><code>install(TARGETS mylib
        LIBRARY
          COMPONENT Libraries
          NAMELINK_COMPONENT Development
        PUBLIC_HEADER
          COMPONENT Development
       )
</code></pre>
<p>In this scenario, if you choose to install only the <code>Development</code> component, both the headers and namelink will be installed without the library. (If you don&#8217;t also install the <code>Libraries</code> component, the namelink will be a dangling symlink, and projects that link to the library will have build errors.) If you install only the <code>Libraries</code> component, only the library will be installed, without the headers and namelink. </p>
<p>This option is typically used for package managers that have separate runtime and development packages. For example, on Debian systems, the library is expected to be in the runtime package, and the headers and namelink are expected to be in the development package. </p>
<p>See the <code>VERSION</code> and <code>SOVERSION</code> target properties for details on creating versioned shared libraries. </p>
 </dd>
<dt><code>NAMELINK_ONLY</code></dt>
<dd> <p> This option causes the installation of only the namelink when a library target is installed. On platforms where versioned shared libraries do not have namelinks or when a library is not versioned, the <code>NAMELINK_ONLY</code> option installs nothing. It is an error to use this parameter outside of a <code>LIBRARY</code> block. </p>
<p>When <code>NAMELINK_ONLY</code> is given, either <code>NAMELINK_COMPONENT</code> or <code>COMPONENT</code> may be used to specify the installation component of the namelink, but <code>COMPONENT</code> should generally be preferred. </p>
 </dd>
<dt><code>NAMELINK_SKIP</code></dt>
<dd> <p> Similar to <code>NAMELINK_ONLY</code>, but it has the opposite effect: it causes the installation of library files other than the namelink when a library target is installed. When neither <code>NAMELINK_ONLY</code> or <code>NAMELINK_SKIP</code> are given, both portions are installed. On platforms where versioned shared libraries do not have symlinks or when a library is not versioned, <code>NAMELINK_SKIP</code> installs the library. It is an error to use this parameter outside of a <code>LIBRARY</code> block. </p>
<p>If <code>NAMELINK_SKIP</code> is specified, <code>NAMELINK_COMPONENT</code> has no effect. It is not recommended to use <code>NAMELINK_SKIP</code> in conjunction with <code>NAMELINK_COMPONENT</code>. </p>
<p>The <i>install(TARGETS)</i> command can also accept the following options at the top level: </p>
 </dd>
<dt><code>EXPORT</code></dt>
<dd> <p> This option associates the installed target files with an export called <code>&lt;export-name&gt;</code>. It must appear before any target options. To actually install the export file itself, call <i>install(EXPORT)</i>, documented below. See documentation of the <code>EXPORT_NAME</code> target property to change the name of the exported target. </p>
 </dd>
<dt><code>INCLUDES DESTINATION</code></dt>
<dd> <p> This option specifies a list of directories which will be added to the <code>INTERFACE_INCLUDE_DIRECTORIES</code> target property of the <code>&lt;targets&gt;</code> when exported by the <i>install(EXPORT)</i> command. If a relative path is specified, it is treated as relative to the <code>$&lt;INSTALL_PREFIX&gt;</code>. </p>
 </dd>
<dt><code>RUNTIME_DEPENDENCY_SET</code></dt>
<dd> <p> New in version 3.21. </p>
<p>This option causes all runtime dependencies of installed executable, shared library, and module targets to be added to the specified runtime dependency set. This set can then be installed with an <i>install(RUNTIME_DEPENDENCY_SET)</i> command. </p>
<p>This keyword and the <code>RUNTIME_DEPENDENCIES</code> keyword are mutually exclusive. </p>
 </dd>
<dt><code>RUNTIME_DEPENDENCIES</code></dt>
<dd> <p> New in version 3.21. </p>
<p>This option causes all runtime dependencies of installed executable, shared library, and module targets to be installed along with the targets themselves. The <code>RUNTIME</code>, <code>LIBRARY</code>, <code>FRAMEWORK</code>, and generic arguments are used to determine the properties (<code>DESTINATION</code>, <code>COMPONENT</code>, etc.) of the installation of these dependencies. </p>
<p> <code>RUNTIME_DEPENDENCIES</code> is semantically equivalent to the following pair of calls: </p>
<pre><code>install(TARGETS ... RUNTIME_DEPENDENCY_SET &lt;set-name&gt;)
install(RUNTIME_DEPENDENCY_SET &lt;set-name&gt; args...)
</code></pre>
<p>where <code>&lt;set-name&gt;</code> will be a randomly generated set name. The <code>args...</code> may include any of the following keywords supported by the <i>install(RUNTIME_DEPENDENCY_SET)</i> command: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>DIRECTORIES</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>PRE_INCLUDE_REGEXES</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>PRE_EXCLUDE_REGEXES</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>POST_INCLUDE_REGEXES</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>POST_EXCLUDE_REGEXES</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>POST_INCLUDE_FILES</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>POST_EXCLUDE_FILES</code> </p>
<p>The <code>RUNTIME_DEPENDENCIES</code> and <code>RUNTIME_DEPENDENCY_SET</code> keywords are mutually exclusive. </p>
<p>One or more groups of properties may be specified in a single call to the <code>TARGETS</code> form of this command. A target may be installed more than once to different locations. Consider hypothetical targets <code>myExe</code>, <code>mySharedLib</code>, and <code>myStaticLib</code>. The code: </p>
<pre><code>install(TARGETS myExe mySharedLib myStaticLib
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib/static)
install(TARGETS mySharedLib DESTINATION /some/full/path)
</code></pre>
<p>will install <code>myExe</code> to <code>&lt;prefix&gt;/bin</code> and <code>myStaticLib</code> to <code>&lt;prefix&gt;/lib/static</code>. On non-DLL platforms <code>mySharedLib</code> will be installed to <code>&lt;prefix&gt;/lib</code> and <code>/some/full/path</code>. On DLL platforms the <code>mySharedLib</code> DLL will be installed to <code>&lt;prefix&gt;/bin</code> and <code>/some/full/path</code> and its import library will be installed to <code>&lt;prefix&gt;/lib/static</code> and <code>/some/full/path</code>. </p>
<p>Interface Libraries may be listed among the targets to install. They install no artifacts but will be included in an associated <code>EXPORT</code>. If Object Libraries are listed but given no destination for their object files, they will be exported as Interface Libraries. This is sufficient to satisfy transitive usage requirements of other targets that link to the object libraries in their implementation. </p>
<p>Installing a target with the <code>EXCLUDE_FROM_ALL</code> target property set to <code>TRUE</code> has undefined behavior. </p>
<p>New in version 3.3: An install destination given as a <code>DESTINATION</code> argument may use &quot;generator expressions&quot; with the syntax <code>$&lt;...&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. </p>
<p>New in version 3.13: <i>install(TARGETS)</i> can install targets that were created in other directories. When using such cross-directory install rules, running <code>make install</code> (or similar) from a subdirectory will not guarantee that targets from other directories are up-to-date. You can use <code>target_link_libraries()</code> or <code>add_dependencies()</code> to ensure that such out-of-directory targets are built before the subdirectory-specific install rules are run. </p>
 </dd></dl>
<h3>Installing Imported Runtime Artifacts</h3>
<p>New in version 3.21. </p>
<pre><code>install(IMPORTED_RUNTIME_ARTIFACTS targets...
        [RUNTIME_DEPENDENCY_SET &lt;set-name&gt;]
        [[LIBRARY|RUNTIME|FRAMEWORK|BUNDLE]
         [DESTINATION &lt;dir&gt;]
         [PERMISSIONS permissions...]
         [CONFIGURATIONS [Debug|Release|...]]
         [COMPONENT &lt;component&gt;]
         [OPTIONAL] [EXCLUDE_FROM_ALL]
        ] [...]
        )
</code></pre>
<p>The <code>IMPORTED_RUNTIME_ARTIFACTS</code> form specifies rules for installing the runtime artifacts of imported targets. Projects may do this if they want to bundle outside executables or modules inside their installation. The <code>LIBRARY</code>, <code>RUNTIME</code>, <code>FRAMEWORK</code>, and <code>BUNDLE</code> arguments have the same semantics that they do in the <i>TARGETS</i> mode. Only the runtime artifacts of imported targets are installed (except in the case of <code>FRAMEWORK</code> libraries, <code>MACOSX_BUNDLE</code> executables, and <code>BUNDLE</code> CFBundles.) For example, headers and import libraries associated with DLLs are not installed. In the case of <code>FRAMEWORK</code> libraries, <code>MACOSX_BUNDLE</code> executables, and <code>BUNDLE</code> CFBundles, the entire directory is installed. </p>
<p>The <code>RUNTIME_DEPENDENCY_SET</code> option causes the runtime artifacts of the imported executable, shared library, and module library <code>targets</code> to be added to the <code>&lt;set-name&gt;</code> runtime dependency set. This set can then be installed with an <i>install(RUNTIME_DEPENDENCY_SET)</i> command.  </p>
<h3>Installing Files</h3>
<pre><code>install(&lt;FILES|PROGRAMS&gt; files...
        TYPE &lt;type&gt; | DESTINATION &lt;dir&gt;
        [PERMISSIONS permissions...]
        [CONFIGURATIONS [Debug|Release|...]]
        [COMPONENT &lt;component&gt;]
        [RENAME &lt;name&gt;] [OPTIONAL] [EXCLUDE_FROM_ALL])
</code></pre>
<p>The <code>FILES</code> form specifies rules for installing files for a project. File names given as relative paths are interpreted with respect to the current source directory. Files installed by this form are by default given permissions <code>OWNER_WRITE</code>, <code>OWNER_READ</code>, <code>GROUP_READ</code>, and <code>WORLD_READ</code> if no <code>PERMISSIONS</code> argument is given. </p>
<p>The <code>PROGRAMS</code> form is identical to the <code>FILES</code> form except that the default permissions for the installed file also include <code>OWNER_EXECUTE</code>, <code>GROUP_EXECUTE</code>, and <code>WORLD_EXECUTE</code>. This form is intended to install programs that are not targets, such as shell scripts. Use the <code>TARGETS</code> form to install targets built within the project. </p>
<p>The list of <code>files...</code> given to <code>FILES</code> or <code>PROGRAMS</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;...&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. However, if any item begins in a generator expression it must evaluate to a full path. </p>
<p>Either a <code>TYPE</code> or a <code>DESTINATION</code> must be provided, but not both. A <code>TYPE</code> argument specifies the generic file type of the files being installed. A destination will then be set automatically by taking the corresponding variable from <code>GNUInstallDirs</code>, or by using a built-in default if that variable is not defined. See the table below for the supported file types and their corresponding variables and built-in defaults. Projects can provide a <code>DESTINATION</code> argument instead of a file type if they wish to explicitly define the install destination. <center> </p>
<table>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>TYPE</code> Argument </td>
<td> GNUInstallDirs Variable </td>
<td> Built-In Default 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>BIN</code> </td>
<td> <code>${CMAKE_INSTALL_BINDIR}</code> </td>
<td> <code>bin</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>SBIN</code> </td>
<td> <code>${CMAKE_INSTALL_SBINDIR}</code> </td>
<td> <code>sbin</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>LIB</code> </td>
<td> <code>${CMAKE_INSTALL_LIBDIR}</code> </td>
<td> <code>lib</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>INCLUDE</code> </td>
<td> <code>${CMAKE_INSTALL_INCLUDEDIR}</code> </td>
<td> <code>include</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>SYSCONF</code> </td>
<td> <code>${CMAKE_INSTALL_SYSCONFDIR}</code> </td>
<td> <code>etc</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>SHAREDSTATE</code> </td>
<td> <code>${CMAKE_INSTALL_SHARESTATEDIR}</code> </td>
<td> <code>com</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>LOCALSTATE</code> </td>
<td> <code>${CMAKE_INSTALL_LOCALSTATEDIR}</code> </td>
<td> <code>var</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>RUNSTATE</code> </td>
<td> <code>${CMAKE_INSTALL_RUNSTATEDIR}</code> </td>
<td> <code>&lt;LOCALSTATE dir&gt;/run</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>DATA</code> </td>
<td> <code>${CMAKE_INSTALL_DATADIR}</code> </td>
<td> <code>&lt;DATAROOT dir&gt;</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>INFO</code> </td>
<td> <code>${CMAKE_INSTALL_INFODIR}</code> </td>
<td> <code>&lt;DATAROOT dir&gt;/info</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>LOCALE</code> </td>
<td> <code>${CMAKE_INSTALL_LOCALEDIR}</code> </td>
<td> <code>&lt;DATAROOT dir&gt;/locale</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>MAN</code> </td>
<td> <code>${CMAKE_INSTALL_MANDIR}</code> </td>
<td> <code>&lt;DATAROOT dir&gt;/man</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>DOC</code> </td>
<td> <code>${CMAKE_INSTALL_DOCDIR}</code> </td>
<td> <code>&lt;DATAROOT dir&gt;/doc</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
</table>
<p> </center> </p>
<p>Projects wishing to follow the common practice of installing headers into a project-specific subdirectory will need to provide a destination rather than rely on the above. </p>
<p>Note that some of the types&#8217; built-in defaults use the <code>DATAROOT</code> directory as a prefix. The <code>DATAROOT</code> prefix is calculated similarly to the types, with <code>CMAKE_INSTALL_DATAROOTDIR</code> as the variable and <code>share</code> as the built-in default. You cannot use <code>DATAROOT</code> as a <code>TYPE</code> parameter; please use <code>DATA</code> instead. </p>
<p>To make packages compliant with distribution filesystem layout policies, if projects must specify a <code>DESTINATION</code>, it is recommended that they use a path that begins with the appropriate <code>GNUInstallDirs</code> variable. This allows package maintainers to control the install destination by setting the appropriate cache variables. The following example shows how to follow this advice while installing headers to a project-specific subdirectory: </p>
<pre><code>include(GNUInstallDirs)
install(FILES mylib.h
        DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/myproj
)
</code></pre>
<p>New in version 3.4: An install destination given as a <code>DESTINATION</code> argument may use &quot;generator expressions&quot; with the syntax <code>$&lt;...&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. </p>
<p>New in version 3.20: An install rename given as a <code>RENAME</code> argument may use &quot;generator expressions&quot; with the syntax <code>$&lt;...&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. </p>
<h3>Installing Directories</h3>
<pre><code>install(DIRECTORY dirs...
        TYPE &lt;type&gt; | DESTINATION &lt;dir&gt;
        [FILE_PERMISSIONS permissions...]
        [DIRECTORY_PERMISSIONS permissions...]
        [USE_SOURCE_PERMISSIONS] [OPTIONAL] [MESSAGE_NEVER]
        [CONFIGURATIONS [Debug|Release|...]]
        [COMPONENT &lt;component&gt;] [EXCLUDE_FROM_ALL]
        [FILES_MATCHING]
        [[PATTERN &lt;pattern&gt; | REGEX &lt;regex&gt;]
         [EXCLUDE] [PERMISSIONS permissions...]] [...])
</code></pre>
<p>The <code>DIRECTORY</code> form installs contents of one or more directories to a given destination. The directory structure is copied verbatim to the destination. The last component of each directory name is appended to the destination directory but a trailing slash may be used to avoid this because it leaves the last component empty. Directory names given as relative paths are interpreted with respect to the current source directory. If no input directory names are given the destination directory will be created but nothing will be installed into it. The <code>FILE_PERMISSIONS</code> and <code>DIRECTORY_PERMISSIONS</code> options specify permissions given to files and directories in the destination. If <code>USE_SOURCE_PERMISSIONS</code> is specified and <code>FILE_PERMISSIONS</code> is not, file permissions will be copied from the source directory structure. If no permissions are specified files will be given the default permissions specified in the <code>FILES</code> form of the command, and the directories will be given the default permissions specified in the <code>PROGRAMS</code> form of the command. </p>
<p>New in version 3.1: The <code>MESSAGE_NEVER</code> option disables file installation status output. </p>
<p>Installation of directories may be controlled with fine granularity using the <code>PATTERN</code> or <code>REGEX</code> options. These &quot;match&quot; options specify a globbing pattern or regular expression to match directories or files encountered within input directories. They may be used to apply certain options (see below) to a subset of the files and directories encountered. The full path to each input file or directory (with forward slashes) is matched against the expression. A <code>PATTERN</code> will match only complete file names: the portion of the full path matching the pattern must occur at the end of the file name and be preceded by a slash. A <code>REGEX</code> will match any portion of the full path but it may use <code>/</code> and <code>$</code> to simulate the <code>PATTERN</code> behavior. By default all files and directories are installed whether or not they are matched. The <code>FILES_MATCHING</code> option may be given before the first match option to disable installation of files (but not directories) not matched by any expression. For example, the code </p>
<pre><code>install(DIRECTORY src/ DESTINATION include/myproj
        FILES_MATCHING PATTERN &quot;*.h&quot;)
</code></pre>
<p>will extract and install header files from a source tree. </p>
<p>Some options may follow a <code>PATTERN</code> or <code>REGEX</code> expression as described under string(REGEX) and are applied only to files or directories matching them. The <code>EXCLUDE</code> option will skip the matched file or directory. The <code>PERMISSIONS</code> option overrides the permissions setting for the matched file or directory. For example the code </p>
<pre><code>install(DIRECTORY icons scripts/ DESTINATION share/myproj
        PATTERN &quot;CVS&quot; EXCLUDE
        PATTERN &quot;scripts/*&quot;
        PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ
                    GROUP_EXECUTE GROUP_READ)
</code></pre>
<p>will install the <code>icons</code> directory to <code>share/myproj/icons</code> and the <code>scripts</code> directory to <code>share/myproj</code>. The icons will get default file permissions, the scripts will be given specific permissions, and any <code>CVS</code> directories will be excluded. </p>
<p>Either a <code>TYPE</code> or a <code>DESTINATION</code> must be provided, but not both. A <code>TYPE</code> argument specifies the generic file type of the files within the listed directories being installed. A destination will then be set automatically by taking the corresponding variable from <code>GNUInstallDirs</code>, or by using a built-in default if that variable is not defined. See the table below for the supported file types and their corresponding variables and built-in defaults. Projects can provide a <code>DESTINATION</code> argument instead of a file type if they wish to explicitly define the install destination. <center> </p>
<table>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>TYPE</code> Argument </td>
<td> GNUInstallDirs Variable </td>
<td> Built-In Default 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>BIN</code> </td>
<td> <code>${CMAKE_INSTALL_BINDIR}</code> </td>
<td> <code>bin</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>SBIN</code> </td>
<td> <code>${CMAKE_INSTALL_SBINDIR}</code> </td>
<td> <code>sbin</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>LIB</code> </td>
<td> <code>${CMAKE_INSTALL_LIBDIR}</code> </td>
<td> <code>lib</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>INCLUDE</code> </td>
<td> <code>${CMAKE_INSTALL_INCLUDEDIR}</code> </td>
<td> <code>include</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>SYSCONF</code> </td>
<td> <code>${CMAKE_INSTALL_SYSCONFDIR}</code> </td>
<td> <code>etc</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>SHAREDSTATE</code> </td>
<td> <code>${CMAKE_INSTALL_SHARESTATEDIR}</code> </td>
<td> <code>com</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>LOCALSTATE</code> </td>
<td> <code>${CMAKE_INSTALL_LOCALSTATEDIR}</code> </td>
<td> <code>var</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>RUNSTATE</code> </td>
<td> <code>${CMAKE_INSTALL_RUNSTATEDIR}</code> </td>
<td> <code>&lt;LOCALSTATE dir&gt;/run</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>DATA</code> </td>
<td> <code>${CMAKE_INSTALL_DATADIR}</code> </td>
<td> <code>&lt;DATAROOT dir&gt;</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>INFO</code> </td>
<td> <code>${CMAKE_INSTALL_INFODIR}</code> </td>
<td> <code>&lt;DATAROOT dir&gt;/info</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>LOCALE</code> </td>
<td> <code>${CMAKE_INSTALL_LOCALEDIR}</code> </td>
<td> <code>&lt;DATAROOT dir&gt;/locale</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>MAN</code> </td>
<td> <code>${CMAKE_INSTALL_MANDIR}</code> </td>
<td> <code>&lt;DATAROOT dir&gt;/man</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td> <code>DOC</code> </td>
<td> <code>${CMAKE_INSTALL_DOCDIR}</code> </td>
<td> <code>&lt;DATAROOT dir&gt;/doc</code> 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
</tr>
</table>
<p> </center> </p>
<p>Note that some of the types&#8217; built-in defaults use the <code>DATAROOT</code> directory as a prefix. The <code>DATAROOT</code> prefix is calculated similarly to the types, with <code>CMAKE_INSTALL_DATAROOTDIR</code> as the variable and <code>share</code> as the built-in default. You cannot use <code>DATAROOT</code> as a <code>TYPE</code> parameter; please use <code>DATA</code> instead. </p>
<p>To make packages compliant with distribution filesystem layout policies, if projects must specify a <code>DESTINATION</code>, it is recommended that they use a path that begins with the appropriate <code>GNUInstallDirs</code> variable. This allows package maintainers to control the install destination by setting the appropriate cache variables. </p>
<p>New in version 3.4: An install destination given as a <code>DESTINATION</code> argument may use &quot;generator expressions&quot; with the syntax <code>$&lt;...&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. </p>
<p>New in version 3.5: The list of <code>dirs...</code> given to <code>DIRECTORY</code> may use &quot;generator expressions&quot; too. </p>
<h3>Custom Installation Logic</h3>
<pre><code>install([[SCRIPT &lt;file&gt;] [CODE &lt;code&gt;]]
        [ALL_COMPONENTS | COMPONENT &lt;component&gt;]
        [EXCLUDE_FROM_ALL] [...])
</code></pre>
<p>The <code>SCRIPT</code> form will invoke the given CMake script files during installation. If the script file name is a relative path it will be interpreted with respect to the current source directory. The <code>CODE</code> form will invoke the given CMake code during installation. Code is specified as a single argument inside a double-quoted string. For example, the code </p>
<pre><code>install(CODE &quot;MESSAGE(\&quot;Sample install message.\&quot;)&quot;)
</code></pre>
<p>will print a message during installation. </p>
<p>New in version 3.21: When the <code>ALL_COMPONENTS</code> option is given, the custom installation script code will be executed for every component of a component-specific installation. This option is mutually exclusive with the <code>COMPONENT</code> option. </p>
<p>New in version 3.14: <code>&lt;file&gt;</code> or <code>&lt;code&gt;</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;...&gt;</code> (in the case of <code>&lt;file&gt;</code>, this refers to their use in the file name, not the file&#8217;s contents). See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. </p>
<h3>Installing Exports</h3>
<pre><code>install(EXPORT &lt;export-name&gt; DESTINATION &lt;dir&gt;
        [NAMESPACE &lt;namespace&gt;] [[FILE &lt;name&gt;.cmake]|
        [PERMISSIONS permissions...]
        [CONFIGURATIONS [Debug|Release|...]]
        [EXPORT_LINK_INTERFACE_LIBRARIES]
        [COMPONENT &lt;component&gt;]
        [EXCLUDE_FROM_ALL])
install(EXPORT_ANDROID_MK &lt;export-name&gt; DESTINATION &lt;dir&gt; [...])
</code></pre>
<p>The <code>EXPORT</code> form generates and installs a CMake file containing code to import targets from the installation tree into another project. Target installations are associated with the export <code>&lt;export-name&gt;</code> using the <code>EXPORT</code> option of the <i>install(TARGETS)</i> signature documented above. The <code>NAMESPACE</code> option will prepend <code>&lt;namespace&gt;</code> to the target names as they are written to the import file. By default the generated file will be called <code>&lt;export-name&gt;.cmake</code> but the <code>FILE</code> option may be used to specify a different name. The value given to the <code>FILE</code> option must be a file name with the <code>.cmake</code> extension. If a <code>CONFIGURATIONS</code> option is given then the file will only be installed when one of the named configurations is installed. Additionally, the generated import file will reference only the matching target configurations. The <code>EXPORT_LINK_INTERFACE_LIBRARIES</code> keyword, if present, causes the contents of the properties matching <code>(IMPORTED_)?LINK_INTERFACE_LIBRARIES(_&lt;CONFIG&gt;)?</code> to be exported, when policy <code>CMP0022</code> is <code>NEW</code>. </p>
<p> <code>NOTE:</code> The installed <code>&lt;export-name&gt;.cmake</code> file may come with additional per-configuration <code>&lt;export-name&gt;-*.cmake</code> files to be loaded by globbing. Do not use an export name that is the same as the package name in combination with installing a <code>&lt;package-name&gt;-config.cmake</code> file or the latter may be incorrectly matched by the glob and loaded. </p>
<p>When a <code>COMPONENT</code> option is given, the listed <code>&lt;component&gt;</code> implicitly depends on all components mentioned in the export set. The exported <code>&lt;name&gt;.cmake</code> file will require each of the exported components to be present in order for dependent projects to build properly. For example, a project may define components <code>Runtime</code> and <code>Development</code>, with shared libraries going into the <code>Runtime</code> component and static libraries and headers going into the <code>Development</code> component. The export set would also typically be part of the <code>Development</code> component, but it would export targets from both the <code>Runtime</code> and <code>Development</code> components. Therefore, the <code>Runtime</code> component would need to be installed if the <code>Development</code> component was installed, but not vice versa. If the <code>Development</code> component was installed without the <code>Runtime</code> component, dependent projects that try to link against it would have build errors. Package managers, such as APT and RPM, typically handle this by listing the <code>Runtime</code> component as a dependency of the <code>Development</code> component in the package metadata, ensuring that the library is always installed if the headers and CMake export file are present. </p>
<p>New in version 3.7: In addition to cmake language files, the <code>EXPORT_ANDROID_MK</code> mode maybe used to specify an export to the android ndk build system. This mode accepts the same options as the normal export mode. The Android NDK supports the use of prebuilt libraries, both static and shared. This allows cmake to build the libraries of a project and make them available to an ndk build system complete with transitive dependencies, include flags and defines required to use the libraries. </p>
<p>The <code>EXPORT</code> form is useful to help outside projects use targets built and installed by the current project. For example, the code </p>
<pre><code>install(TARGETS myexe EXPORT myproj DESTINATION bin)
install(EXPORT myproj NAMESPACE mp_ DESTINATION lib/myproj)
install(EXPORT_ANDROID_MK myproj DESTINATION share/ndk-modules)
</code></pre>
<p>will install the executable <code>myexe</code> to <code>&lt;prefix&gt;/bin</code> and code to import it in the file <code>&lt;prefix&gt;/lib/myproj/myproj.cmake</code> and <code>&lt;prefix&gt;/share/ndk-modules/Android.mk</code>. An outside project may load this file with the include command and reference the <code>myexe</code> executable from the installation tree using the imported target name <code>mp_myexe</code> as if the target were built in its own tree. </p>
<p> <code>NOTE:</code> This command supersedes the <code>install_targets()</code> command and the <code>PRE_INSTALL_SCRIPT</code> and <code>POST_INSTALL_SCRIPT</code> target properties. It also replaces the <code>FILES</code> forms of the <code>install_files()</code> and <code>install_programs()</code> commands. The processing order of these install rules relative to those generated by <code>install_targets()</code>, <code>install_files()</code>, and <code>install_programs()</code> commands is not defined.  </p>
<h3>Installing Runtime Dependencies</h3>
<p>New in version 3.21. </p>
<pre><code>install(RUNTIME_DEPENDENCY_SET &lt;set-name&gt;
        [[LIBRARY|RUNTIME|FRAMEWORK]
         [DESTINATION &lt;dir&gt;]
         [PERMISSIONS permissions...]
         [CONFIGURATIONS [Debug|Release|...]]
         [COMPONENT &lt;component&gt;]
         [NAMELINK_COMPONENT &lt;component&gt;]
         [OPTIONAL] [EXCLUDE_FROM_ALL]
        ] [...]
        [PRE_INCLUDE_REGEXES regexes...]
        [PRE_EXCLUDE_REGEXES regexes...]
        [POST_INCLUDE_REGEXES regexes...]
        [POST_EXCLUDE_REGEXES regexes...]
        [POST_INCLUDE_FILES files...]
        [POST_EXCLUDE_FILES files...]
        [DIRECTORIES directories...]
        )
</code></pre>
<p>Installs a runtime dependency set previously created by one or more <i>install(TARGETS)</i> or <i>install(IMPORTED_RUNTIME_ARTIFACTS)</i> commands. The dependencies of targets belonging to a runtime dependency set are installed in the <code>RUNTIME</code> destination and component on DLL platforms, and in the <code>LIBRARY</code> destination and component on non-DLL platforms. macOS frameworks are installed in the <code>FRAMEWORK</code> destination and component. Targets built within the build tree will never be installed as runtime dependencies, nor will their own dependencies, unless the targets themselves are installed with <i>install(TARGETS)</i>. </p>
<p>The generated install script calls <code>file(GET_RUNTIME_DEPENDENCIES)</code> on the build-tree files to calculate the runtime dependencies. The build-tree executable files are passed as the <code>EXECUTABLES</code> argument, the build-tree shared libraries as the <code>LIBRARIES</code> argument, and the build-tree modules as the <code>MODULES</code> argument. On macOS, if one of the executables is a <code>MACOSX_BUNDLE</code>, that executable is passed as the <code>BUNDLE_EXECUTABLE</code> argument. At most one such bundle executable may be in the runtime dependency set on macOS. The <code>MACOSX_BUNDLE</code> property has no effect on other platforms. Note that <code>file(GET_RUNTIME_DEPENDENCIES)</code> only supports collecting the runtime dependencies for Windows, Linux and macOS platforms, so <code>install(RUNTIME_DEPENDENCY_SET)</code> has the same limitation. </p>
<p>The following sub-arguments are forwarded through as the corresponding arguments to <code>file(GET_RUNTIME_DEPENDENCIES)</code> (for those that provide a non-empty list of directories, regular expressions or files). They all support <code>generator expressions</code>. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>DIRECTORIES &lt;directories&gt;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>PRE_INCLUDE_REGEXES &lt;regexes&gt;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>PRE_EXCLUDE_REGEXES &lt;regexes&gt;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>POST_INCLUDE_REGEXES &lt;regexes&gt;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>POST_EXCLUDE_REGEXES &lt;regexes&gt;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>POST_INCLUDE_FILES &lt;files&gt;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>POST_EXCLUDE_FILES &lt;files&gt;</code> </p>
 </dd></dl>
<h3>Generated Installation Script</h3>
<p> <code>NOTE:</code> Use of this feature is not recommended. Please consider using the <code>--install</code> argument of <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> instead. </p>
<p>The <code>install()</code> command generates a file, <code>cmake_install.cmake</code>, inside the build directory, which is used internally by the generated install target and by CPack. You can also invoke this script manually with <code>cmake -P</code>. This script accepts several variables: </p>
<dl>
<dt><code>COMPONENT</code></dt>
<dd> <p> Set this variable to install only a single CPack component as opposed to all of them. For example, if you only want to install the <code>Development</code> component, run <code>cmake -DCOMPONENT=Development -P cmake_install.cmake</code>. </p>
 </dd>
<dt><code>BUILD_TYPE</code></dt>
<dd> <p> Set this variable to change the build type if you are using a multi-config generator. For example, to install with the <code>Debug</code> configuration, run <code>cmake -DBUILD_TYPE=Debug -P cmake_install.cmake</code>. </p>
 </dd>
<dt><code>DESTDIR</code></dt>
<dd> <p> This is an environment variable rather than a CMake variable. It allows you to change the installation prefix on UNIX systems. See <code>DESTDIR</code> for details. </p>
 </dd></dl>
<h3>link_directories</h3>
<p>Add directories in which the linker will look for libraries. </p>
<pre><code>link_directories([AFTER|BEFORE] directory1 [directory2 ...])
</code></pre>
<p>Adds the paths in which the linker should search for libraries. Relative paths given to this command are interpreted as relative to the current source directory, see <code>CMP0015</code>. </p>
<p>The command will apply only to targets created after it is called. </p>
<p>New in version 3.13: The directories are added to the <code>LINK_DIRECTORIES</code> directory property for the current <code>CMakeLists.txt</code> file, converting relative paths to absolute as needed. See the <code><a href="/docs/linux/man/7-cmake-buildsystem/">cmake-buildsystem</a>(7)</code> manual for more on defining buildsystem properties. </p>
<p>New in version 3.13: By default the directories specified are appended onto the current list of directories. This default behavior can be changed by setting <code>CMAKE_LINK_DIRECTORIES_BEFORE</code> to <code>ON</code>. By using <code>AFTER</code> or <code>BEFORE</code> explicitly, you can select between appending and prepending, independent of the default. </p>
<p>New in version 3.13: Arguments to <code>link_directories</code> may use &quot;generator expressions&quot; with the syntax &quot;$&lt;...&gt;&quot;. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. </p>
<p> <code>NOTE:</code> This command is rarely necessary and should be avoided where there are other choices. Prefer to pass full absolute paths to libraries where possible, since this ensures the correct library will always be linked. The <code>find_library()</code> command provides the full path, which can generally be used directly in calls to <code>target_link_libraries()</code>. Situations where a library search path may be needed include: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Project generators like Xcode where the user can switch target architecture at build time, but a full path to a library cannot be used because it only provides one architecture (i.e. it is not a universal binary). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Libraries may themselves have other private library dependencies that expect to be found via <code>RPATH</code> mechanisms, but some linkers are not able to fully decode those paths (e.g. due to the presence of things like <code>$ORIGIN</code>). </p>
<p>If a library search path must be provided, prefer to localize the effect where possible by using the <code>target_link_directories()</code> command rather than <code>link_directories()</code>. The target-specific command can also control how the search directories propagate to other dependent targets. </p>
 </dd></dl>
<h3>link_libraries</h3>
<p>Link libraries to all targets added later. </p>
<pre><code>link_libraries([item1 [item2 [...]]]
               [[debug|optimized|general] &lt;item&gt;] ...)
</code></pre>
<p>Specify libraries or flags to use when linking any targets created later in the current directory or below by commands such as <code>add_executable()</code> or <code>add_library()</code>. See the <code>target_link_libraries()</code> command for meaning of arguments. </p>
<p> <code>NOTE:</code> The <code>target_link_libraries()</code> command should be preferred whenever possible. Library dependencies are chained automatically, so directory-wide specification of link libraries is rarely needed.  </p>
<h3>load_cache</h3>
<p>Load in the values from another project&#8217;s CMake cache. </p>
<pre><code>load_cache(pathToBuildDirectory READ_WITH_PREFIX prefix entry1...)
</code></pre>
<p>Reads the cache and store the requested entries in variables with their name prefixed with the given prefix. This only reads the values, and does not create entries in the local project&#8217;s cache. </p>
<pre><code>load_cache(pathToBuildDirectory [EXCLUDE entry1...]
           [INCLUDE_INTERNALS entry1...])
</code></pre>
<p>Loads in the values from another cache and store them in the local project&#8217;s cache as internal entries. This is useful for a project that depends on another project built in a different tree. <code>EXCLUDE</code> option can be used to provide a list of entries to be excluded. <code>INCLUDE_INTERNALS</code> can be used to provide a list of internal entries to be included. Normally, no internal entries are brought in. Use of this form of the command is strongly discouraged, but it is provided for backward compatibility.  </p>
<h3>project</h3>
<p>Set the name of the project.  </p>
<h3>Synopsis</h3>
<pre><code>project(&lt;PROJECT-NAME&gt; [&lt;language-name&gt;...])
project(&lt;PROJECT-NAME&gt;
        [VERSION &lt;major&gt;[.&lt;minor&gt;[.&lt;patch&gt;[.&lt;tweak&gt;]]]]
        [DESCRIPTION &lt;project-description-string&gt;]
        [HOMEPAGE_URL &lt;url-string&gt;]
        [LANGUAGES &lt;language-name&gt;...])
</code></pre>
<p>Sets the name of the project, and stores it in the variable <code>PROJECT_NAME</code>. When called from the top-level <code>CMakeLists.txt</code> also stores the project name in the variable <code>CMAKE_PROJECT_NAME</code>. </p>
<p>Also sets the variables: </p>
<dl>
<dt><code>PROJECT_SOURCE_DIR</code>, <code>&lt;PROJECT-NAME&gt;_SOURCE_DIR</code></dt>
<dd> <p> Absolute path to the source directory for the project. </p>
 </dd>
<dt><code>PROJECT_BINARY_DIR</code>, <code>&lt;PROJECT-NAME&gt;_BINARY_DIR</code></dt>
<dd> <p> Absolute path to the binary directory for the project. </p>
 </dd>
<dt><code>PROJECT_IS_TOP_LEVEL</code>, <code>&lt;PROJECT-NAME&gt;_IS_TOP_LEVEL</code></dt>
<dd> <p> New in version 3.21. </p>
<p>Boolean value indicating whether the project is top-level. </p>
<p>Further variables are set by the optional arguments described in the following. If any of these arguments is not used, then the corresponding variables are set to the empty string. </p>
 </dd></dl>
<h3>Options</h3>
<p>The options are: </p>
<dl>
<dt><code>VERSION &lt;version&gt;</code></dt>
<dd> <p> Optional; may not be used unless policy <code>CMP0048</code> is set to <code>NEW</code>. </p>
<p>Takes a <code>&lt;version&gt;</code> argument composed of non-negative integer components, i.e. <code>&lt;major&gt;[.&lt;minor&gt;[.&lt;patch&gt;[.&lt;tweak&gt;]]]</code>, and sets the variables </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>PROJECT_VERSION</code>, <code>&lt;PROJECT-NAME&gt;_VERSION</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>PROJECT_VERSION_MAJOR</code>, <code>&lt;PROJECT-NAME&gt;_VERSION_MAJOR</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>PROJECT_VERSION_MINOR</code>, <code>&lt;PROJECT-NAME&gt;_VERSION_MINOR</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>PROJECT_VERSION_PATCH</code>, <code>&lt;PROJECT-NAME&gt;_VERSION_PATCH</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>PROJECT_VERSION_TWEAK</code>, <code>&lt;PROJECT-NAME&gt;_VERSION_TWEAK</code>. </p>
<p>New in version 3.12: When the <code>project()</code> command is called from the top-level <code>CMakeLists.txt</code>, then the version is also stored in the variable <code>CMAKE_PROJECT_VERSION</code>. </p>
 </dd>
<dt><code>DESCRIPTION &lt;project-description-string&gt;</code></dt>
<dd> <p> New in version 3.9. </p>
<p>Optional. Sets the variables </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>PROJECT_DESCRIPTION</code>, <code>&lt;PROJECT-NAME&gt;_DESCRIPTION</code> </p>
<p>to <code>&lt;project-description-string&gt;</code>. It is recommended that this description is a relatively short string, usually no more than a few words. </p>
<p>When the <code>project()</code> command is called from the top-level <code>CMakeLists.txt</code>, then the description is also stored in the variable <code>CMAKE_PROJECT_DESCRIPTION</code>. </p>
<p>New in version 3.12: Added the <code>&lt;PROJECT-NAME&gt;_DESCRIPTION</code> variable. </p>
 </dd>
<dt><code>HOMEPAGE_URL &lt;url-string&gt;</code></dt>
<dd> <p> New in version 3.12. </p>
<p>Optional. Sets the variables </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>PROJECT_HOMEPAGE_URL</code>, <code>&lt;PROJECT-NAME&gt;_HOMEPAGE_URL</code> </p>
<p>to <code>&lt;url-string&gt;</code>, which should be the canonical home URL for the project. </p>
<p>When the <code>project()</code> command is called from the top-level <code>CMakeLists.txt</code>, then the URL also is stored in the variable <code>CMAKE_PROJECT_HOMEPAGE_URL</code>. </p>
 </dd>
<dt><code>LANGUAGES &lt;language-name&gt;...</code></dt>
<dd> <p> Optional. Can also be specified without <code>LANGUAGES</code> keyword per the first, short signature. </p>
<p>Selects which programming languages are needed to build the project. Supported languages include <code>C</code>, <code>CXX</code> (i.e. C++), <code>CUDA</code>, <code>OBJC</code> (i.e. Objective-C), <code>OBJCXX</code>, <code>Fortran</code>, <code>HIP</code>, <code>ISPC</code>, and <code>ASM</code>. By default <code>C</code> and <code>CXX</code> are enabled if no language options are given. Specify language <code>NONE</code>, or use the <code>LANGUAGES</code> keyword and list no languages, to skip enabling any languages. </p>
<p>New in version 3.8: Added <code>CUDA</code> support. </p>
<p>New in version 3.16: Added <code>OBJC</code> and <code>OBJCXX</code> support. </p>
<p>New in version 3.18: Added <code>ISPC</code> support. </p>
<p>If enabling <code>ASM</code>, list it last so that CMake can check whether compilers for other languages like <code>C</code> work for assembly too. </p>
<p>The variables set through the <code>VERSION</code>, <code>DESCRIPTION</code> and <code>HOMEPAGE_URL</code> options are intended for use as default values in package metadata and documentation. </p>
 </dd></dl>
<h3>Code Injection</h3>
<p>If the <code>CMAKE_PROJECT_INCLUDE_BEFORE</code> or <code>CMAKE_PROJECT_&lt;PROJECT-NAME&gt;_INCLUDE_BEFORE</code> variables are set, the files they point to will be included as the first step of the <code>project()</code> command. If both are set, then <code>CMAKE_PROJECT_INCLUDE_BEFORE</code> will be included before <code>CMAKE_PROJECT_&lt;PROJECT-NAME&gt;_INCLUDE_BEFORE</code>. </p>
<p>If the <code>CMAKE_PROJECT_INCLUDE</code> or <code>CMAKE_PROJECT_&lt;PROJECT-NAME&gt;_INCLUDE</code> variables are set, the files they point to will be included as the last step of the <code>project()</code> command. If both are set, then <code>CMAKE_PROJECT_INCLUDE</code> will be included before <code>CMAKE_PROJECT_&lt;PROJECT-NAME&gt;_INCLUDE</code>. </p>
<p>New in version 3.15: Added the <code>CMAKE_PROJECT_INCLUDE</code> and <code>CMAKE_PROJECT_INCLUDE_BEFORE</code> variables. </p>
<p>New in version 3.17: Added the <code>CMAKE_PROJECT_&lt;PROJECT-NAME&gt;_INCLUDE_BEFORE</code> variable. </p>
<h3>Usage</h3>
<p>The top-level <code>CMakeLists.txt</code> file for a project must contain a literal, direct call to the <code>project()</code> command; loading one through the <code>include()</code> command is not sufficient. If no such call exists, CMake will issue a warning and pretend there is a <code>project(Project)</code> at the top to enable the default languages (<code>C</code> and <code>CXX</code>). </p>
<p> <code>NOTE:</code> Call the <code>project()</code> command near the top of the top-level <code>CMakeLists.txt</code>, but <i>after</i> calling <code>cmake_minimum_required()</code>. It is important to establish version and policy settings before invoking other commands whose behavior they may affect. See also policy <code>CMP0000</code>.  </p>
<h3>remove_definitions</h3>
<p>Remove -D define flags added by <code>add_definitions()</code>. </p>
<pre><code>remove_definitions(-DFOO -DBAR ...)
</code></pre>
<p>Removes flags (added by <code>add_definitions()</code>) from the compiler command line for sources in the current directory and below.  </p>
<h3>set_source_files_properties</h3>
<p>Source files can have properties that affect how they are built. </p>
<pre><code>set_source_files_properties(&lt;files&gt; ...
                            [DIRECTORY &lt;dirs&gt; ...]
                            [TARGET_DIRECTORY &lt;targets&gt; ...]
                            PROPERTIES &lt;prop1&gt; &lt;value1&gt;
                            [&lt;prop2&gt; &lt;value2&gt;] ...)
</code></pre>
<p>Sets properties associated with source files using a key/value paired list. </p>
<p>New in version 3.18: By default, source file properties are only visible to targets added in the same directory (<code>CMakeLists.txt</code>). Visibility can be set in other directory scopes using one or both of the following options: </p>
<dl>
<dt><code>DIRECTORY &lt;dirs&gt;...</code></dt>
<dd> <p> The source file properties will be set in each of the <code>&lt;dirs&gt;</code> directories&#8217; scopes. CMake must already know about each of these source directories, either by having added them through a call to <code>add_subdirectory()</code> or it being the top level source directory. Relative paths are treated as relative to the current source directory. </p>
 </dd>
<dt><code>TARGET_DIRECTORY &lt;targets&gt;...</code></dt>
<dd> <p> The source file properties will be set in each of the directory scopes where any of the specified <code>&lt;targets&gt;</code> were created (the <code>&lt;targets&gt;</code> must therefore already exist). </p>
<p>Use <code>get_source_file_property()</code> to get property values. See also the <code>set_property(SOURCE)</code> command. </p>
<p>See Source File Properties for the list of properties known to CMake. </p>
<p> <code>NOTE:</code> The <code>GENERATED</code> source file property may be globally visible. See its documentation for details. </p>
 </dd></dl>
<h3>set_target_properties</h3>
<p>Targets can have properties that affect how they are built. </p>
<pre><code>set_target_properties(target1 target2 ...
                      PROPERTIES prop1 value1
                      prop2 value2 ...)
</code></pre>
<p>Sets properties on targets. The syntax for the command is to list all the targets you want to change, and then provide the values you want to set next. You can use any prop value pair you want and extract it later with the <code>get_property()</code> or <code>get_target_property()</code> command. </p>
<p>See also the <code>set_property(TARGET)</code> command. </p>
<p>See Target Properties for the list of properties known to CMake.  </p>
<h3>set_tests_properties</h3>
<p>Set a property of the tests. </p>
<pre><code>set_tests_properties(test1 [test2...] PROPERTIES prop1 value1 prop2 value2)
</code></pre>
<p>Sets a property for the tests. If the test is not found, CMake will report an error. <code>Generator expressions</code> will be expanded the same as supported by the test&#8217;s <code>add_test()</code> call. </p>
<p>See also the <code>set_property(TEST)</code> command. </p>
<p>See Test Properties for the list of properties known to CMake.  </p>
<h3>source_group</h3>
<p>Define a grouping for source files in IDE project generation. There are two different signatures to create source groups. </p>
<pre><code>source_group(&lt;name&gt; [FILES &lt;src&gt;...] [REGULAR_EXPRESSION &lt;regex&gt;])
source_group(TREE &lt;root&gt; [PREFIX &lt;prefix&gt;] [FILES &lt;src&gt;...])
</code></pre>
<p>Defines a group into which sources will be placed in project files. This is intended to set up file tabs in Visual Studio. The group is scoped in the directory where the command is called, and applies to sources in targets created in that directory. </p>
<p>The options are: </p>
<dl>
<dt><code>TREE</code></dt>
<dd> <p> New in version 3.8. </p>
<p>CMake will automatically detect, from <code>&lt;src&gt;</code> files paths, source groups it needs to create, to keep structure of source groups analogically to the actual files and directories structure in the project. Paths of <code>&lt;src&gt;</code> files will be cut to be relative to <code>&lt;root&gt;</code>. The command fails if the paths within <code>src</code> do not start with <code>root</code>. </p>
 </dd>
<dt><code>PREFIX</code></dt>
<dd> <p> New in version 3.8. </p>
<p>Source group and files located directly in <code>&lt;root&gt;</code> path, will be placed in <code>&lt;prefix&gt;</code> source groups. </p>
 </dd>
<dt><code>FILES</code></dt>
<dd> <p> Any source file specified explicitly will be placed in group <code>&lt;name&gt;</code>. Relative paths are interpreted with respect to the current source directory. </p>
 </dd>
<dt><code>REGULAR_EXPRESSION</code></dt>
<dd> <p> Any source file whose name matches the regular expression will be placed in group <code>&lt;name&gt;</code>. </p>
<p>If a source file matches multiple groups, the <i>last</i> group that explicitly lists the file with <code>FILES</code> will be favored, if any. If no group explicitly lists the file, the <i>last</i> group whose regular expression matches the file will be favored. </p>
<p>The <code>&lt;name&gt;</code> of the group and <code>&lt;prefix&gt;</code> argument may contain forward slashes or backslashes to specify subgroups. Backslashes need to be escaped appropriately: </p>
<pre><code>source_group(base/subdir ...)
source_group(outer\\inner ...)
source_group(TREE &lt;root&gt; PREFIX sources\\inc ...)
</code></pre>
<p>New in version 3.18: Allow using forward slashes (<code>/</code>) to specify subgroups. </p>
<p>For backwards compatibility, the short-hand signature </p>
<pre><code>source_group(&lt;name&gt; &lt;regex&gt;)
</code></pre>
<p>is equivalent to </p>
<pre><code>source_group(&lt;name&gt; REGULAR_EXPRESSION &lt;regex&gt;)
</code></pre>
 </dd></dl>
<h3>target_compile_definitions</h3>
<p>Add compile definitions to a target. </p>
<pre><code>target_compile_definitions(&lt;target&gt;
  &lt;INTERFACE|PUBLIC|PRIVATE&gt; [items1...]
  [&lt;INTERFACE|PUBLIC|PRIVATE&gt; [items2...] ...])
</code></pre>
<p>Specifies compile definitions to use when compiling a given <code>&lt;target&gt;</code>. The named <code>&lt;target&gt;</code> must have been created by a command such as <code>add_executable()</code> or <code>add_library()</code> and must not be an ALIAS target. </p>
<p>The <code>INTERFACE</code>, <code>PUBLIC</code> and <code>PRIVATE</code> keywords are required to specify the scope of the following arguments. <code>PRIVATE</code> and <code>PUBLIC</code> items will populate the <code>COMPILE_DEFINITIONS</code> property of <code>&lt;target&gt;</code>. <code>PUBLIC</code> and <code>INTERFACE</code> items will populate the <code>INTERFACE_COMPILE_DEFINITIONS</code> property of <code>&lt;target&gt;</code>. The following arguments specify compile definitions. Repeated calls for the same <code>&lt;target&gt;</code> append items in the order called. </p>
<p>New in version 3.11: Allow setting <code>INTERFACE</code> items on IMPORTED targets. </p>
<p>Arguments to <code>target_compile_definitions</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;...&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake-buildsystem/">cmake-buildsystem</a>(7)</code> manual for more on defining buildsystem properties. </p>
<p>Any leading <code>-D</code> on an item will be removed. Empty items are ignored. For example, the following are all equivalent: </p>
<pre><code>target_compile_definitions(foo PUBLIC FOO)
target_compile_definitions(foo PUBLIC -DFOO) # -D removed
target_compile_definitions(foo PUBLIC &quot;&quot; FOO) # &quot;&quot; ignored
target_compile_definitions(foo PUBLIC -D FOO) # -D becomes &quot;&quot;, then ignored
</code></pre>
<p>Definitions may optionally have values: </p>
<pre><code>target_compile_definitions(foo PUBLIC FOO=1)
</code></pre>
<p>Note that many compilers treat <code>-DFOO</code> as equivalent to <code>-DFOO=1</code>, but other tools may not recognize this in all circumstances (e.g. IntelliSense).  </p>
<h3>target_compile_features</h3>
<p>New in version 3.1. </p>
<p>Add expected compiler features to a target. </p>
<pre><code>target_compile_features(&lt;target&gt; &lt;PRIVATE|PUBLIC|INTERFACE&gt; &lt;feature&gt; [...])
</code></pre>
<p>Specifies compiler features required when compiling a given target. If the feature is not listed in the <code>CMAKE_C_COMPILE_FEATURES</code>, <code>CMAKE_CUDA_COMPILE_FEATURES</code>, or <code>CMAKE_CXX_COMPILE_FEATURES</code> variables, then an error will be reported by CMake. If the use of the feature requires an additional compiler flag, such as <code>-std=gnu++11</code>, the flag will be added automatically. </p>
<p>The <code>INTERFACE</code>, <code>PUBLIC</code> and <code>PRIVATE</code> keywords are required to specify the scope of the features. <code>PRIVATE</code> and <code>PUBLIC</code> items will populate the <code>COMPILE_FEATURES</code> property of <code>&lt;target&gt;</code>. <code>PUBLIC</code> and <code>INTERFACE</code> items will populate the <code>INTERFACE_COMPILE_FEATURES</code> property of <code>&lt;target&gt;</code>. Repeated calls for the same <code>&lt;target&gt;</code> append items. </p>
<p>New in version 3.11: Allow setting <code>INTERFACE</code> items on IMPORTED targets. </p>
<p>The named <code>&lt;target&gt;</code> must have been created by a command such as <code>add_executable()</code> or <code>add_library()</code> and must not be an ALIAS target. </p>
<p>Arguments to <code>target_compile_features</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;...&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.  </p>
<h3>target_compile_options</h3>
<p>Add compile options to a target. </p>
<pre><code>target_compile_options(&lt;target&gt; [BEFORE]
  &lt;INTERFACE|PUBLIC|PRIVATE&gt; [items1...]
  [&lt;INTERFACE|PUBLIC|PRIVATE&gt; [items2...] ...])
</code></pre>
<p>Adds options to the <code>COMPILE_OPTIONS</code> or <code>INTERFACE_COMPILE_OPTIONS</code> target properties. These options are used when compiling the given <code>&lt;target&gt;</code>, which must have been created by a command such as <code>add_executable()</code> or <code>add_library()</code> and must not be an ALIAS target.  </p>
<h3>Arguments</h3>
<p>If <code>BEFORE</code> is specified, the content will be prepended to the property instead of being appended. </p>
<p>The <code>INTERFACE</code>, <code>PUBLIC</code> and <code>PRIVATE</code> keywords are required to specify the scope of the following arguments. <code>PRIVATE</code> and <code>PUBLIC</code> items will populate the <code>COMPILE_OPTIONS</code> property of <code>&lt;target&gt;</code>. <code>PUBLIC</code> and <code>INTERFACE</code> items will populate the <code>INTERFACE_COMPILE_OPTIONS</code> property of <code>&lt;target&gt;</code>. The following arguments specify compile options. Repeated calls for the same <code>&lt;target&gt;</code> append items in the order called. </p>
<p>New in version 3.11: Allow setting <code>INTERFACE</code> items on IMPORTED targets. </p>
<p>Arguments to <code>target_compile_options</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;...&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake-buildsystem/">cmake-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.  </p>
<h3>Option De-duplication</h3>
<p>The final set of options used for a target is constructed by accumulating options from the current target and the usage requirements of its dependencies. The set of options is de-duplicated to avoid repetition. </p>
<p>New in version 3.12: While beneficial for individual options, the de-duplication step can break up option groups. For example, <code>-option A -option B</code> becomes <code>-option A B</code>. One may specify a group of options using shell-like quoting along with a <code>SHELL:</code> prefix. The <code>SHELL:</code> prefix is dropped, and the rest of the option string is parsed using the <code>separate_arguments()</code> <code>UNIX_COMMAND</code> mode. For example, <code>&quot;SHELL:-option A&quot; &quot;SHELL:-option B&quot;</code> becomes <code>-option A -option B</code>. </p>
<h3>See Also</h3>
<p>This command can be used to add any options. However, for adding preprocessor definitions and include directories it is recommended to use the more specific commands <code>target_compile_definitions()</code> and <code>target_include_directories()</code>. </p>
<p>For directory-wide settings, there is the command <code>add_compile_options()</code>. </p>
<p>For file-specific settings, there is the source file property <code>COMPILE_OPTIONS</code>.  </p>
<h3>target_include_directories</h3>
<p>Add include directories to a target. </p>
<pre><code>target_include_directories(&lt;target&gt; [SYSTEM] [AFTER|BEFORE]
  &lt;INTERFACE|PUBLIC|PRIVATE&gt; [items1...]
  [&lt;INTERFACE|PUBLIC|PRIVATE&gt; [items2...] ...])
</code></pre>
<p>Specifies include directories to use when compiling a given target. The named <code>&lt;target&gt;</code> must have been created by a command such as <code>add_executable()</code> or <code>add_library()</code> and must not be an ALIAS target. </p>
<p>By using <code>AFTER</code> or <code>BEFORE</code> explicitly, you can select between appending and prepending, independent of the default. </p>
<p>The <code>INTERFACE</code>, <code>PUBLIC</code> and <code>PRIVATE</code> keywords are required to specify the scope of the following arguments. <code>PRIVATE</code> and <code>PUBLIC</code> items will populate the <code>INCLUDE_DIRECTORIES</code> property of <code>&lt;target&gt;</code>. <code>PUBLIC</code> and <code>INTERFACE</code> items will populate the <code>INTERFACE_INCLUDE_DIRECTORIES</code> property of <code>&lt;target&gt;</code>. The following arguments specify include directories. </p>
<p>New in version 3.11: Allow setting <code>INTERFACE</code> items on IMPORTED targets. </p>
<p>Specified include directories may be absolute paths or relative paths. Repeated calls for the same &lt;target&gt; append items in the order called. If <code>SYSTEM</code> is specified, the compiler will be told the directories are meant as system include directories on some platforms (signalling this setting might achieve effects such as the compiler skipping warnings, or these fixed-install system files not being considered in dependency calculations - see compiler docs). If <code>SYSTEM</code> is used together with <code>PUBLIC</code> or <code>INTERFACE</code>, the <code>INTERFACE_SYSTEM_INCLUDE_DIRECTORIES</code> target property will be populated with the specified directories. </p>
<p>Arguments to <code>target_include_directories</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;...&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake-buildsystem/">cmake-buildsystem</a>(7)</code> manual for more on defining buildsystem properties. </p>
<p>Include directories usage requirements commonly differ between the build-tree and the install-tree. The <code>BUILD_INTERFACE</code> and <code>INSTALL_INTERFACE</code> generator expressions can be used to describe separate usage requirements based on the usage location. Relative paths are allowed within the <code>INSTALL_INTERFACE</code> expression and are interpreted relative to the installation prefix. For example: </p>
<pre><code>target_include_directories(mylib PUBLIC
  $&lt;BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include/mylib&gt;
  $&lt;INSTALL_INTERFACE:include/mylib&gt; # &lt;prefix&gt;/include/mylib
)
</code></pre>
<h3>Creating Relocatable Packages</h3>
<p>Note that it is not advisable to populate the <code>INSTALL_INTERFACE</code> of the <code>INTERFACE_INCLUDE_DIRECTORIES</code> of a target with absolute paths to the include directories of dependencies. That would hard-code into installed packages the include directory paths for dependencies <code>as found on the machine the package was made on</code>. </p>
<p>The <code>INSTALL_INTERFACE</code> of the <code>INTERFACE_INCLUDE_DIRECTORIES</code> is only suitable for specifying the required include directories for headers provided with the target itself, not those provided by the transitive dependencies listed in its <code>INTERFACE_LINK_LIBRARIES</code> target property. Those dependencies should themselves be targets that specify their own header locations in <code>INTERFACE_INCLUDE_DIRECTORIES</code>. </p>
<p>See the Creating Relocatable Packages section of the <code><a href="/docs/linux/man/7-cmake-packages/">cmake-packages</a>(7)</code> manual for discussion of additional care that must be taken when specifying usage requirements while creating packages for redistribution.  </p>
<h3>target_link_directories</h3>
<p>New in version 3.13. </p>
<p>Add link directories to a target. </p>
<pre><code>target_link_directories(&lt;target&gt; [BEFORE]
  &lt;INTERFACE|PUBLIC|PRIVATE&gt; [items1...]
  [&lt;INTERFACE|PUBLIC|PRIVATE&gt; [items2...] ...])
</code></pre>
<p>Specifies the paths in which the linker should search for libraries when linking a given target. Each item can be an absolute or relative path, with the latter being interpreted as relative to the current source directory. These items will be added to the link command. </p>
<p>The named <code>&lt;target&gt;</code> must have been created by a command such as <code>add_executable()</code> or <code>add_library()</code> and must not be an ALIAS target. </p>
<p>The <code>INTERFACE</code>, <code>PUBLIC</code> and <code>PRIVATE</code> keywords are required to specify the scope of the items that follow them. <code>PRIVATE</code> and <code>PUBLIC</code> items will populate the <code>LINK_DIRECTORIES</code> property of <code>&lt;target&gt;</code>. <code>PUBLIC</code> and <code>INTERFACE</code> items will populate the <code>INTERFACE_LINK_DIRECTORIES</code> property of <code>&lt;target&gt;</code> (IMPORTED targets only support <code>INTERFACE</code> items). Each item specifies a link directory and will be converted to an absolute path if necessary before adding it to the relevant property. Repeated calls for the same <code>&lt;target&gt;</code> append items in the order called. </p>
<p>If <code>BEFORE</code> is specified, the content will be prepended to the relevant property instead of being appended. </p>
<p>Arguments to <code>target_link_directories</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;...&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake-buildsystem/">cmake-buildsystem</a>(7)</code> manual for more on defining buildsystem properties. </p>
<p> <code>NOTE:</code> This command is rarely necessary and should be avoided where there are other choices. Prefer to pass full absolute paths to libraries where possible, since this ensures the correct library will always be linked. The <code>find_library()</code> command provides the full path, which can generally be used directly in calls to <code>target_link_libraries()</code>. Situations where a library search path may be needed include: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Project generators like Xcode where the user can switch target architecture at build time, but a full path to a library cannot be used because it only provides one architecture (i.e. it is not a universal binary). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Libraries may themselves have other private library dependencies that expect to be found via <code>RPATH</code> mechanisms, but some linkers are not able to fully decode those paths (e.g. due to the presence of things like <code>$ORIGIN</code>). </p>
 </dd></dl>
<h3>target_link_libraries</h3>
<p>Specify libraries or flags to use when linking a given target and/or its dependents. Usage requirements from linked library targets will be propagated. Usage requirements of a target&#8217;s dependencies affect compilation of its own sources.  </p>
<h3>Overview</h3>
<p>This command has several signatures as detailed in subsections below. All of them have the general form </p>
<pre><code>target_link_libraries(&lt;target&gt; ... &lt;item&gt;... ...)
</code></pre>
<p>The named <code>&lt;target&gt;</code> must have been created by a command such as <code>add_executable()</code> or <code>add_library()</code> and must not be an ALIAS target. If policy <code>CMP0079</code> is not set to <code>NEW</code> then the target must have been created in the current directory. Repeated calls for the same <code>&lt;target&gt;</code> append items in the order called. </p>
<p>New in version 3.13: The <code>&lt;target&gt;</code> doesn&#8217;t have to be defined in the same directory as the <code>target_link_libraries</code> call. </p>
<p>Each <code>&lt;item&gt;</code> may be: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>A library target name</code>: The generated link line will have the full path to the linkable library file associated with the target. The buildsystem will have a dependency to re-link <code>&lt;target&gt;</code> if the library file changes. </p>
<p>The named target must be created by <code>add_library()</code> within the project or as an IMPORTED library. If it is created within the project an ordering dependency will automatically be added in the build system to make sure the named library target is up-to-date before the <code>&lt;target&gt;</code> links. </p>
<p>If an imported library has the <code>IMPORTED_NO_SONAME</code> target property set, CMake may ask the linker to search for the library instead of using the full path (e.g. <code>/usr/lib/libfoo.so</code> becomes <code>-lfoo</code>). </p>
<p>The full path to the target&#8217;s artifact will be quoted/escaped for the shell automatically. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>A full path to a library file</code>: The generated link line will normally preserve the full path to the file. The buildsystem will have a dependency to re-link <code>&lt;target&gt;</code> if the library file changes. </p>
<p>There are some cases where CMake may ask the linker to search for the library (e.g. <code>/usr/lib/libfoo.so</code> becomes <code>-lfoo</code>), such as when a shared library is detected to have no <code>SONAME</code> field. See policy <code>CMP0060</code> for discussion of another case. </p>
<p>If the library file is in a macOS framework, the <code>Headers</code> directory of the framework will also be processed as a usage requirement. This has the same effect as passing the framework directory as an include directory. </p>
<p>New in version 3.8: On Visual Studio Generators for VS 2010 and above, library files ending in <code>.targets</code> will be treated as MSBuild targets files and imported into generated project files. This is not supported by other generators. </p>
<p>The full path to the library file will be quoted/escaped for the shell automatically. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>A plain library name</code>: The generated link line will ask the linker to search for the library (e.g. <code>foo</code> becomes <code>-lfoo</code> or <code>foo.lib</code>). </p>
<p>The library name/flag is treated as a command-line string fragment and will be used with no extra quoting or escaping. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>A link flag</code>: Item names starting with <code>-</code>, but not <code>-l</code> or <code>-framework</code>, are treated as linker flags. Note that such flags will be treated like any other library link item for purposes of transitive dependencies, so they are generally safe to specify only as private link items that will not propagate to dependents. </p>
<p>Link flags specified here are inserted into the link command in the same place as the link libraries. This might not be correct, depending on the linker. Use the <code>LINK_OPTIONS</code> target property or <code>target_link_options()</code> command to add link flags explicitly. The flags will then be placed at the toolchain-defined flag position in the link command. </p>
<p>New in version 3.13: <code>LINK_OPTIONS</code> target property and <code>target_link_options()</code> command. For earlier versions of CMake, use <code>LINK_FLAGS</code> property instead. </p>
<p>The link flag is treated as a command-line string fragment and will be used with no extra quoting or escaping. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>A generator expression</code>: A <code>$&lt;...&gt;</code> <code>generator expression</code> may evaluate to any of the above items or to a semicolon-separated list of them. If the <code>...</code> contains any <code>;</code> characters, e.g. after evaluation of a <code>${list}</code> variable, be sure to use an explicitly quoted argument <code>&quot;$&lt;...&gt;&quot;</code> so that this command receives it as a single <code>&lt;item&gt;</code>. </p>
<p>Additionally, a generator expression may be used as a fragment of any of the above items, e.g. <code>foo$&lt;1:_d&gt;</code>. </p>
<p>Note that generator expressions will not be used in OLD handling of policy <code>CMP0003</code> or policy <code>CMP0004</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A <code>debug</code>, <code>optimized</code>, or <code>general</code> keyword immediately followed by another <code>&lt;item&gt;</code>. The item following such a keyword will be used only for the corresponding build configuration. The <code>debug</code> keyword corresponds to the <code>Debug</code> configuration (or to configurations named in the <code>DEBUG_CONFIGURATIONS</code> global property if it is set). The <code>optimized</code> keyword corresponds to all other configurations. The <code>general</code> keyword corresponds to all configurations, and is purely optional. Higher granularity may be achieved for per-configuration rules by creating and linking to IMPORTED library targets. These keywords are interpreted immediately by this command and therefore have no special meaning when produced by a generator expression. </p>
<p>Items containing <code>::</code>, such as <code>Foo::Bar</code>, are assumed to be IMPORTED or ALIAS library target names and will cause an error if no such target exists. See policy <code>CMP0028</code>. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-buildsystem/">cmake-buildsystem</a>(7)</code> manual for more on defining buildsystem properties. </p>
 </dd></dl>
<h3>Libraries for a Target and/or its Dependents</h3>
<pre><code>target_link_libraries(&lt;target&gt;
                      &lt;PRIVATE|PUBLIC|INTERFACE&gt; &lt;item&gt;...
                     [&lt;PRIVATE|PUBLIC|INTERFACE&gt; &lt;item&gt;...]...)
</code></pre>
<p>The <code>PUBLIC</code>, <code>PRIVATE</code> and <code>INTERFACE</code> keywords can be used to specify both the link dependencies and the link interface in one command. Libraries and targets following <code>PUBLIC</code> are linked to, and are made part of the link interface. Libraries and targets following <code>PRIVATE</code> are linked to, but are not made part of the link interface. Libraries following <code>INTERFACE</code> are appended to the link interface and are not used for linking <code>&lt;target&gt;</code>.  </p>
<h3>Libraries for both a Target and its Dependents</h3>
<pre><code>target_link_libraries(&lt;target&gt; &lt;item&gt;...)
</code></pre>
<p>Library dependencies are transitive by default with this signature. When this target is linked into another target then the libraries linked to this target will appear on the link line for the other target too. This transitive &quot;link interface&quot; is stored in the <code>INTERFACE_LINK_LIBRARIES</code> target property and may be overridden by setting the property directly. When <code>CMP0022</code> is not set to <code>NEW</code>, transitive linking is built in but may be overridden by the <code>LINK_INTERFACE_LIBRARIES</code> property. Calls to other signatures of this command may set the property making any libraries linked exclusively by this signature private.  </p>
<h3>Libraries for a Target and/or its Dependents (Legacy)</h3>
<pre><code>target_link_libraries(&lt;target&gt;
                      &lt;LINK_PRIVATE|LINK_PUBLIC&gt; &lt;lib&gt;...
                     [&lt;LINK_PRIVATE|LINK_PUBLIC&gt; &lt;lib&gt;...]...)
</code></pre>
<p>The <code>LINK_PUBLIC</code> and <code>LINK_PRIVATE</code> modes can be used to specify both the link dependencies and the link interface in one command. </p>
<p>This signature is for compatibility only. Prefer the <code>PUBLIC</code> or <code>PRIVATE</code> keywords instead. </p>
<p>Libraries and targets following <code>LINK_PUBLIC</code> are linked to, and are made part of the <code>INTERFACE_LINK_LIBRARIES</code>. If policy <code>CMP0022</code> is not <code>NEW</code>, they are also made part of the <code>LINK_INTERFACE_LIBRARIES</code>. Libraries and targets following <code>LINK_PRIVATE</code> are linked to, but are not made part of the <code>INTERFACE_LINK_LIBRARIES</code> (or <code>LINK_INTERFACE_LIBRARIES</code>).  </p>
<h3>Libraries for Dependents Only (Legacy)</h3>
<pre><code>target_link_libraries(&lt;target&gt; LINK_INTERFACE_LIBRARIES &lt;item&gt;...)
</code></pre>
<p>The <code>LINK_INTERFACE_LIBRARIES</code> mode appends the libraries to the <code>INTERFACE_LINK_LIBRARIES</code> target property instead of using them for linking. If policy <code>CMP0022</code> is not <code>NEW</code>, then this mode also appends libraries to the <code>LINK_INTERFACE_LIBRARIES</code> and its per-configuration equivalent. </p>
<p>This signature is for compatibility only. Prefer the <code>INTERFACE</code> mode instead. </p>
<p>Libraries specified as <code>debug</code> are wrapped in a generator expression to correspond to debug builds. If policy <code>CMP0022</code> is not <code>NEW</code>, the libraries are also appended to the <code>LINK_INTERFACE_LIBRARIES_DEBUG</code> property (or to the properties corresponding to configurations listed in the <code>DEBUG_CONFIGURATIONS</code> global property if it is set). Libraries specified as <code>optimized</code> are appended to the <code>INTERFACE_LINK_LIBRARIES</code> property. If policy <code>CMP0022</code> is not <code>NEW</code>, they are also appended to the <code>LINK_INTERFACE_LIBRARIES</code> property. Libraries specified as <code>general</code> (or without any keyword) are treated as if specified for both <code>debug</code> and <code>optimized</code>.  </p>
<h3>Linking Object Libraries</h3>
<p>New in version 3.12. </p>
<p>Object Libraries may be used as the <code>&lt;target&gt;</code> (first) argument of <code>target_link_libraries</code> to specify dependencies of their sources on other libraries. For example, the code </p>
<pre><code>add_library(A SHARED a.c)
target_compile_definitions(A PUBLIC A)
add_library(obj OBJECT obj.c)
target_compile_definitions(obj PUBLIC OBJ)
target_link_libraries(obj PUBLIC A)
</code></pre>
<p>compiles <code>obj.c</code> with <code>-DA -DOBJ</code> and establishes usage requirements for <code>obj</code> that propagate to its dependents. </p>
<p>Normal libraries and executables may link to Object Libraries to get their objects and usage requirements. Continuing the above example, the code </p>
<pre><code>add_library(B SHARED b.c)
target_link_libraries(B PUBLIC obj)
</code></pre>
<p>compiles <code>b.c</code> with <code>-DA -DOBJ</code>, creates shared library <code>B</code> with object files from <code>b.c</code> and <code>obj.c</code>, and links <code>B</code> to <code>A</code>. Furthermore, the code </p>
<pre><code>add_executable(main main.c)
target_link_libraries(main B)
</code></pre>
<p>compiles <code>main.c</code> with <code>-DA -DOBJ</code> and links executable <code>main</code> to <code>B</code> and <code>A</code>. The object library&#8217;s usage requirements are propagated transitively through <code>B</code>, but its object files are not. </p>
<p>Object Libraries may &quot;link&quot; to other object libraries to get usage requirements, but since they do not have a link step nothing is done with their object files. Continuing from the above example, the code: </p>
<pre><code>add_library(obj2 OBJECT obj2.c)
target_link_libraries(obj2 PUBLIC obj)
add_executable(main2 main2.c)
target_link_libraries(main2 obj2)
</code></pre>
<p>compiles <code>obj2.c</code> with <code>-DA -DOBJ</code>, creates executable <code>main2</code> with object files from <code>main2.c</code> and <code>obj2.c</code>, and links <code>main2</code> to <code>A</code>. </p>
<p>In other words, when Object Libraries appear in a target&#8217;s <code>INTERFACE_LINK_LIBRARIES</code> property they will be treated as Interface Libraries, but when they appear in a target&#8217;s <code>LINK_LIBRARIES</code> property their object files will be included in the link too.  </p>
<h3>Linking Object Libraries via $&lt;TARGET_OBJECTS&gt;</h3>
<p>New in version 3.21. </p>
<p>The object files associated with an object library may be referenced by the <code>$&lt;TARGET_OBJECTS&gt;</code> generator expression. Such object files are placed on the link line <i>before</i> all libraries, regardless of their relative order. Additionally, an ordering dependency will be added to the build system to make sure the object library is up-to-date before the dependent target links. For example, the code </p>
<pre><code>add_library(obj3 OBJECT obj3.c)
target_compile_definitions(obj3 PUBLIC OBJ3)
add_executable(main3 main3.c)
target_link_libraries(main3 PRIVATE a3 $&lt;TARGET_OBJECTS:obj3&gt; b3)
</code></pre>
<p>links executable <code>main3</code> with object files from <code>main3.c</code> and <code>obj3.c</code> followed by the <code>a3</code> and <code>b3</code> libraries. <code>main3.c</code> is <i>not</i> compiled with usage requirements from <code>obj3</code>, such as <code>-DOBJ3</code>. </p>
<p>This approach can be used to achieve transitive inclusion of object files in link lines as usage requirements. Continuing the above example, the code </p>
<pre><code>add_library(iface_obj3 INTERFACE)
target_link_libraries(iface_obj3 INTERFACE obj3 $&lt;TARGET_OBJECTS:obj3&gt;)
</code></pre>
<p>creates an interface library <code>iface_obj3</code> that forwards the <code>obj3</code> usage requirements and adds the <code>obj3</code> object files to dependents&#8217; link lines. The code </p>
<pre><code>add_executable(use_obj3 use_obj3.c)
target_link_libraries(use_obj3 PRIVATE iface_obj3)
</code></pre>
<p>compiles <code>use_obj3.c</code> with <code>-DOBJ3</code> and links executable <code>use_obj3</code> with object files from <code>use_obj3.c</code> and <code>obj3.c</code>. </p>
<p>This also works transitively through a static library. Since a static library does not link, it does not consume the object files from object libraries referenced this way. Instead, the object files become transitive link dependencies of the static library. Continuing the above example, the code </p>
<pre><code>add_library(static3 STATIC static3.c)
target_link_libraries(static3 PRIVATE iface_obj3)
add_executable(use_static3 use_static3.c)
target_link_libraries(use_static3 PRIVATE static3)
</code></pre>
<p>compiles <code>static3.c</code> with <code>-DOBJ3</code> and creates <code>libstatic3.a</code> using only its own object file. <code>use_static3.c</code> is compiled <i>without</i> <code>-DOBJ3</code> because the usage requirement is not transitive through the private dependency of <code>static3</code>. However, the link dependencies of <code>static3</code> are propagated, including the <code>iface_obj3</code> reference to <code>$&lt;TARGET_OBJECTS:obj3&gt;</code>. The <code>use_static3</code> executable is created with object files from <code>use_static3.c</code> and <code>obj3.c</code>, and linked to library <code>libstatic3.a</code>. </p>
<p>When using this approach, it is the project&#8217;s responsibility to avoid linking multiple dependent binaries to <code>iface_obj3</code>, because they will all get the <code>obj3</code> object files on their link lines. </p>
<p> <code>NOTE:</code> Referencing <code>$&lt;TARGET_OBJECTS&gt;</code> in <code>target_link_libraries</code> calls worked in versions of CMake prior to 3.21 for some cases, but was not fully supported: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> It did not place the object files before libraries on link lines. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> It did not add an ordering dependency on the object library. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> It did not work in Xcode with multiple architectures. </p>
 </dd></dl>
<h3>Cyclic Dependencies of Static Libraries</h3>
<p>The library dependency graph is normally acyclic (a DAG), but in the case of mutually-dependent <code>STATIC</code> libraries CMake allows the graph to contain cycles (strongly connected components). When another target links to one of the libraries, CMake repeats the entire connected component. For example, the code </p>
<pre><code>add_library(A STATIC a.c)
add_library(B STATIC b.c)
target_link_libraries(A B)
target_link_libraries(B A)
add_executable(main main.c)
target_link_libraries(main A)
</code></pre>
<p>links <code>main</code> to <code>A B A B</code>. While one repetition is usually sufficient, pathological object file and symbol arrangements can require more. One may handle such cases by using the <code>LINK_INTERFACE_MULTIPLICITY</code> target property or by manually repeating the component in the last <code>target_link_libraries</code> call. However, if two archives are really so interdependent they should probably be combined into a single archive, perhaps by using Object Libraries.  </p>
<h3>Creating Relocatable Packages</h3>
<p>Note that it is not advisable to populate the <code>INTERFACE_LINK_LIBRARIES</code> of a target with absolute paths to dependencies. That would hard-code into installed packages the library file paths for dependencies <code>as found on the machine the package was made on</code>. </p>
<p>See the Creating Relocatable Packages section of the <code><a href="/docs/linux/man/7-cmake-packages/">cmake-packages</a>(7)</code> manual for discussion of additional care that must be taken when specifying usage requirements while creating packages for redistribution.  </p>
<h3>target_link_options</h3>
<p>New in version 3.13. </p>
<p>Add options to the link step for an executable, shared library or module library target. </p>
<pre><code>target_link_options(&lt;target&gt; [BEFORE]
  &lt;INTERFACE|PUBLIC|PRIVATE&gt; [items1...]
  [&lt;INTERFACE|PUBLIC|PRIVATE&gt; [items2...] ...])
</code></pre>
<p>The named <code>&lt;target&gt;</code> must have been created by a command such as <code>add_executable()</code> or <code>add_library()</code> and must not be an ALIAS target. </p>
<p>This command can be used to add any link options, but alternative commands exist to add libraries (<code>target_link_libraries()</code> or <code>link_libraries()</code>). See documentation of the <code>directory</code> and <code>target</code> <code>LINK_OPTIONS</code> properties. </p>
<p> <code>NOTE:</code> This command cannot be used to add options for static library targets, since they do not use a linker. To add archiver or MSVC librarian flags, see the <code>STATIC_LIBRARY_OPTIONS</code> target property. </p>
<p>If <code>BEFORE</code> is specified, the content will be prepended to the property instead of being appended. </p>
<p>The <code>INTERFACE</code>, <code>PUBLIC</code> and <code>PRIVATE</code> keywords are required to specify the scope of the following arguments. <code>PRIVATE</code> and <code>PUBLIC</code> items will populate the <code>LINK_OPTIONS</code> property of <code>&lt;target&gt;</code>. <code>PUBLIC</code> and <code>INTERFACE</code> items will populate the <code>INTERFACE_LINK_OPTIONS</code> property of <code>&lt;target&gt;</code>. The following arguments specify link options. Repeated calls for the same <code>&lt;target&gt;</code> append items in the order called. </p>
<p> <code>NOTE:</code> IMPORTED targets only support <code>INTERFACE</code> items. </p>
<p>Arguments to <code>target_link_options</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;...&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake-buildsystem/">cmake-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.  </p>
<h3>Host And Device Specific Link Options</h3>
<p>New in version 3.18: When a device link step is involved, which is controlled by <code>CUDA_SEPARABLE_COMPILATION</code> and <code>CUDA_RESOLVE_DEVICE_SYMBOLS</code> properties and policy <code>CMP0105</code>, the raw options will be delivered to the host and device link steps (wrapped in <code>-Xcompiler</code> or equivalent for device link). Options wrapped with <code>$&lt;DEVICE_LINK:...&gt;</code> <code>generator expression</code> will be used only for the device link step. Options wrapped with <code>$&lt;HOST_LINK:...&gt;</code> <code>generator expression</code> will be used only for the host link step. </p>
<h3>Option De-duplication</h3>
<p>The final set of options used for a target is constructed by accumulating options from the current target and the usage requirements of its dependencies. The set of options is de-duplicated to avoid repetition. </p>
<p>New in version 3.12: While beneficial for individual options, the de-duplication step can break up option groups. For example, <code>-option A -option B</code> becomes <code>-option A B</code>. One may specify a group of options using shell-like quoting along with a <code>SHELL:</code> prefix. The <code>SHELL:</code> prefix is dropped, and the rest of the option string is parsed using the <code>separate_arguments()</code> <code>UNIX_COMMAND</code> mode. For example, <code>&quot;SHELL:-option A&quot; &quot;SHELL:-option B&quot;</code> becomes <code>-option A -option B</code>. </p>
<h3>Handling Compiler Driver Differences</h3>
<p>To pass options to the linker tool, each compiler driver has its own syntax. The <code>LINKER:</code> prefix and <code>,</code> separator can be used to specify, in a portable way, options to pass to the linker tool. <code>LINKER:</code> is replaced by the appropriate driver option and <code>,</code> by the appropriate driver separator. The driver prefix and driver separator are given by the values of the <code>CMAKE_&lt;LANG&gt;_LINKER_WRAPPER_FLAG</code> and <code>CMAKE_&lt;LANG&gt;_LINKER_WRAPPER_FLAG_SEP</code> variables. </p>
<p>For example, <code>&quot;LINKER:-z,defs&quot;</code> becomes <code>-Xlinker -z -Xlinker defs</code> for <code>Clang</code> and <code>-Wl,-z,defs</code> for <code>GNU GCC</code>. </p>
<p>The <code>LINKER:</code> prefix can be specified as part of a <code>SHELL:</code> prefix expression. </p>
<p>The <code>LINKER:</code> prefix supports, as an alternative syntax, specification of arguments using the <code>SHELL:</code> prefix and space as separator. The previous example then becomes <code>&quot;LINKER:SHELL:-z defs&quot;</code>. </p>
<p> <code>NOTE:</code> Specifying the <code>SHELL:</code> prefix anywhere other than at the beginning of the <code>LINKER:</code> prefix is not supported.  </p>
<h3>target_precompile_headers</h3>
<p>New in version 3.16. </p>
<p>Add a list of header files to precompile. </p>
<p>Precompiling header files can speed up compilation by creating a partially processed version of some header files, and then using that version during compilations rather than repeatedly parsing the original headers.  </p>
<h3>Main Form</h3>
<pre><code>target_precompile_headers(&lt;target&gt;
  &lt;INTERFACE|PUBLIC|PRIVATE&gt; [header1...]
  [&lt;INTERFACE|PUBLIC|PRIVATE&gt; [header2...] ...])
</code></pre>
<p>The command adds header files to the <code>PRECOMPILE_HEADERS</code> and/or <code>INTERFACE_PRECOMPILE_HEADERS</code> target properties of <code>&lt;target&gt;</code>. The named <code>&lt;target&gt;</code> must have been created by a command such as <code>add_executable()</code> or <code>add_library()</code> and must not be an ALIAS target. </p>
<p>The <code>INTERFACE</code>, <code>PUBLIC</code> and <code>PRIVATE</code> keywords are required to specify the scope of the following arguments. <code>PRIVATE</code> and <code>PUBLIC</code> items will populate the <code>PRECOMPILE_HEADERS</code> property of <code>&lt;target&gt;</code>. <code>PUBLIC</code> and <code>INTERFACE</code> items will populate the <code>INTERFACE_PRECOMPILE_HEADERS</code> property of <code>&lt;target&gt;</code> (IMPORTED targets only support <code>INTERFACE</code> items). Repeated calls for the same <code>&lt;target&gt;</code> will append items in the order called. </p>
<p>Projects should generally avoid using <code>PUBLIC</code> or <code>INTERFACE</code> for targets that will be exported, or they should at least use the <code>$&lt;BUILD_INTERFACE:...&gt;</code> generator expression to prevent precompile headers from appearing in an installed exported target. Consumers of a target should typically be in control of what precompile headers they use, not have precompile headers forced on them by the targets being consumed (since precompile headers are not typically usage requirements). A notable exception to this is where an interface library is created to define a commonly used set of precompile headers in one place and then other targets link to that interface library privately. In this case, the interface library exists specifically to propagate the precompile headers to its consumers and the consumer is effectively still in control, since it decides whether to link to the interface library or not. </p>
<p>The list of header files is used to generate a header file named <code>cmake_pch.h|xx</code> which is used to generate the precompiled header file (<code>.pch</code>, <code>.gch</code>, <code>.pchi</code>) artifact. The <code>cmake_pch.h|xx</code> header file will be force included (<code>-include</code> for GCC, <code>/FI</code> for MSVC) to all source files, so sources do not need to have <code>#include &quot;pch.h&quot;</code>. </p>
<p>Header file names specified with angle brackets (e.g. <code>&lt;unordered_map&gt;</code>) or explicit double quotes (escaped for the <code><a href="/docs/linux/man/7-cmake-language/">cmake-language</a>(7)</code>, e.g. <code>[[&quot;other_header.h&quot;]]</code>) will be treated as is, and include directories must be available for the compiler to find them. Other header file names (e.g. <code>project_header.h</code>) are interpreted as being relative to the current source directory (e.g. <code>CMAKE_CURRENT_SOURCE_DIR</code>) and will be included by absolute path. For example: </p>
<pre><code>target_precompile_headers(myTarget
  PUBLIC
    project_header.h
  PRIVATE
    [[&quot;other_header.h&quot;]]
    &lt;unordered_map&gt;
)
</code></pre>
<p>Arguments to <code>target_precompile_headers()</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;...&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. The <code>$&lt;COMPILE_LANGUAGE:...&gt;</code> generator expression is particularly useful for specifying a language-specific header to precompile for only one language (e.g. <code>CXX</code> and not <code>C</code>). In this case, header file names that are not explicitly in double quotes or angle brackets must be specified by absolute path. Also, when specifying angle brackets inside a generator expression, be sure to encode the closing <code>&gt;</code> as <code>$&lt;ANGLE-R&gt;</code>. For example: </p>
<pre><code>target_precompile_headers(mylib PRIVATE
  &quot;$&lt;$&lt;COMPILE_LANGUAGE:CXX&gt;:${CMAKE_CURRENT_SOURCE_DIR}/cxx_only.h&gt;&quot;
  &quot;$&lt;$&lt;COMPILE_LANGUAGE:C&gt;:&lt;stddef.h$&lt;ANGLE-R&gt;&gt;&quot;
  &quot;$&lt;$&lt;COMPILE_LANGUAGE:CXX&gt;:&lt;cstddef$&lt;ANGLE-R&gt;&gt;&quot;
)
</code></pre>
<h3>Reusing Precompile Headers</h3>
<p>The command also supports a second signature which can be used to specify that one target re-uses a precompiled header file artifact from another target instead of generating its own: </p>
<pre><code>target_precompile_headers(&lt;target&gt; REUSE_FROM &lt;other_target&gt;)
</code></pre>
<p>This form sets the <code>PRECOMPILE_HEADERS_REUSE_FROM</code> property to <code>&lt;other_target&gt;</code> and adds a dependency such that <code>&lt;target&gt;</code> will depend on <code>&lt;other_target&gt;</code>. CMake will halt with an error if the <code>PRECOMPILE_HEADERS</code> property of <code>&lt;target&gt;</code> is already set when the <code>REUSE_FROM</code> form is used. </p>
<p> <code>NOTE:</code> The <code>REUSE_FROM</code> form requires the same set of compiler options, compiler flags and compiler definitions for both <code>&lt;target&gt;</code> and <code>&lt;other_target&gt;</code>. Some compilers (e.g. GCC) may issue a warning if the precompiled header file cannot be used (<code>-Winvalid-pch</code>).  </p>
<h3>See Also</h3>
<p>To disable precompile headers for specific targets, see the <code>DISABLE_PRECOMPILE_HEADERS</code> target property. </p>
<p>To prevent precompile headers from being used when compiling a specific source file, see the <code>SKIP_PRECOMPILE_HEADERS</code> source file property.  </p>
<h3>target_sources</h3>
<p>New in version 3.1. </p>
<p>Add sources to a target. </p>
<pre><code>target_sources(&lt;target&gt;
  &lt;INTERFACE|PUBLIC|PRIVATE&gt; [items1...]
  [&lt;INTERFACE|PUBLIC|PRIVATE&gt; [items2...] ...])
</code></pre>
<p>Specifies sources to use when building a target and/or its dependents. The named <code>&lt;target&gt;</code> must have been created by a command such as <code>add_executable()</code> or <code>add_library()</code> or <code>add_custom_target()</code> and must not be an ALIAS target. </p>
<p>Changed in version 3.13: Relative source file paths are interpreted as being relative to the current source directory (i.e. <code>CMAKE_CURRENT_SOURCE_DIR</code>). See policy <code>CMP0076</code>. </p>
<p>New in version 3.20: <code>&lt;target&gt;</code> can be a custom target. </p>
<p>The <code>INTERFACE</code>, <code>PUBLIC</code> and <code>PRIVATE</code> keywords are required to specify the scope of the items following them. <code>PRIVATE</code> and <code>PUBLIC</code> items will populate the <code>SOURCES</code> property of <code>&lt;target&gt;</code>, which are used when building the target itself. <code>PUBLIC</code> and <code>INTERFACE</code> items will populate the <code>INTERFACE_SOURCES</code> property of <code>&lt;target&gt;</code>, which are used when building dependents. The following arguments specify sources. Repeated calls for the same <code>&lt;target&gt;</code> append items in the order called. The targets created by <code>add_custom_target()</code> can only have <code>PRIVATE</code> scope. </p>
<p>New in version 3.3: Allow exporting targets with <code>INTERFACE_SOURCES</code>. </p>
<p>New in version 3.11: Allow setting <code>INTERFACE</code> items on IMPORTED targets. </p>
<p>Arguments to <code>target_sources</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;...&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake-buildsystem/">cmake-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.  </p>
<h3>try_compile</h3>
<p>Try building some code.  </p>
<h3>Try Compiling Whole Projects</h3>
<pre><code>try_compile(&lt;resultVar&gt; &lt;bindir&gt; &lt;srcdir&gt;
            &lt;projectName&gt; [&lt;targetName&gt;] [CMAKE_FLAGS &lt;flags&gt;...]
            [OUTPUT_VARIABLE &lt;var&gt;])
</code></pre>
<p>Try building a project. The success or failure of the <code>try_compile</code>, i.e. <code>TRUE</code> or <code>FALSE</code> respectively, is returned in <code>&lt;resultVar&gt;</code>. </p>
<p>New in version 3.14: The name of the <code>&lt;resultVar&gt;</code> is defined by the user. Previously, it had a fixed name <code>RESULT_VAR</code>. </p>
<p>In this form, <code>&lt;srcdir&gt;</code> should contain a complete CMake project with a <code>CMakeLists.txt</code> file and all sources. The <code>&lt;bindir&gt;</code> and <code>&lt;srcdir&gt;</code> will not be deleted after this command is run. Specify <code>&lt;targetName&gt;</code> to build a specific target instead of the <code>all</code> or <code>ALL_BUILD</code> target. See below for the meaning of other options.  </p>
<h3>Try Compiling Source Files</h3>
<pre><code>try_compile(&lt;resultVar&gt; &lt;bindir&gt; &lt;srcfile|SOURCES srcfile...&gt;
            [CMAKE_FLAGS &lt;flags&gt;...]
            [COMPILE_DEFINITIONS &lt;defs&gt;...]
            [LINK_OPTIONS &lt;options&gt;...]
            [LINK_LIBRARIES &lt;libs&gt;...]
            [OUTPUT_VARIABLE &lt;var&gt;]
            [COPY_FILE &lt;fileName&gt; [COPY_FILE_ERROR &lt;var&gt;]]
            [&lt;LANG&gt;_STANDARD &lt;std&gt;]
            [&lt;LANG&gt;_STANDARD_REQUIRED &lt;bool&gt;]
            [&lt;LANG&gt;_EXTENSIONS &lt;bool&gt;]
            )
</code></pre>
<p>Try building an executable or static library from one or more source files (which one is determined by the <code>CMAKE_TRY_COMPILE_TARGET_TYPE</code> variable). The success or failure of the <code>try_compile</code>, i.e. <code>TRUE</code> or <code>FALSE</code> respectively, is returned in <code>&lt;resultVar&gt;</code>. </p>
<p>New in version 3.14: The name of the <code>&lt;resultVar&gt;</code> is defined by the user. Previously, it had a fixed name <code>RESULT_VAR</code>. </p>
<p>In this form, one or more source files must be provided. If <code>CMAKE_TRY_COMPILE_TARGET_TYPE</code> is unset or is set to <code>EXECUTABLE</code>, the sources must include a definition for <code>main</code> and CMake will create a <code>CMakeLists.txt</code> file to build the source(s) as an executable. If <code>CMAKE_TRY_COMPILE_TARGET_TYPE</code> is set to <code>STATIC_LIBRARY</code>, a static library will be built instead and no definition for <code>main</code> is required. For an executable, the generated <code>CMakeLists.txt</code> file would contain something like the following: </p>
<pre><code>add_definitions(&lt;expanded COMPILE_DEFINITIONS from caller&gt;)
include_directories(${INCLUDE_DIRECTORIES})
link_directories(${LINK_DIRECTORIES})
add_executable(cmTryCompileExec &lt;srcfile&gt;...)
target_link_options(cmTryCompileExec PRIVATE &lt;LINK_OPTIONS from caller&gt;)
target_link_libraries(cmTryCompileExec ${LINK_LIBRARIES})
</code></pre>
<p>The options are: </p>
<dl>
<dt><code>CMAKE_FLAGS &lt;flags&gt;...</code></dt>
<dd> <p> Specify flags of the form <code>-DVAR:TYPE=VALUE</code> to be passed to the <code>cmake</code> command-line used to drive the test build. The above example shows how values for variables <code>INCLUDE_DIRECTORIES</code>, <code>LINK_DIRECTORIES</code>, and <code>LINK_LIBRARIES</code> are used. </p>
 </dd>
<dt><code>COMPILE_DEFINITIONS &lt;defs&gt;...</code></dt>
<dd> <p> Specify <code>-Ddefinition</code> arguments to pass to <code>add_definitions()</code> in the generated test project. </p>
 </dd>
<dt><code>COPY_FILE &lt;fileName&gt;</code></dt>
<dd> <p> Copy the built executable or static library to the given <code>&lt;fileName&gt;</code>. </p>
 </dd>
<dt><code>COPY_FILE_ERROR &lt;var&gt;</code></dt>
<dd> <p> Use after <code>COPY_FILE</code> to capture into variable <code>&lt;var&gt;</code> any error message encountered while trying to copy the file. </p>
 </dd>
<dt><code>LINK_LIBRARIES &lt;libs&gt;...</code></dt>
<dd> <p> Specify libraries to be linked in the generated project. The list of libraries may refer to system libraries and to Imported Targets from the calling project. </p>
<p>If this option is specified, any <code>-DLINK_LIBRARIES=...</code> value given to the <code>CMAKE_FLAGS</code> option will be ignored. </p>
 </dd>
<dt><code>LINK_OPTIONS &lt;options&gt;...</code></dt>
<dd> <p> New in version 3.14. </p>
<p>Specify link step options to pass to <code>target_link_options()</code> or to set the <code>STATIC_LIBRARY_OPTIONS</code> target property in the generated project, depending on the <code>CMAKE_TRY_COMPILE_TARGET_TYPE</code> variable. </p>
 </dd>
<dt><code>OUTPUT_VARIABLE &lt;var&gt;</code></dt>
<dd> <p> Store the output from the build process in the given variable. </p>
 </dd>
<dt><code>&lt;LANG&gt;_STANDARD &lt;std&gt;</code></dt>
<dd> <p> New in version 3.8. </p>
<p>Specify the <code>C_STANDARD</code>, <code>CXX_STANDARD</code>, <code>OBJC_STANDARD</code>, <code>OBJCXX_STANDARD</code>, or <code>CUDA_STANDARD</code> target property of the generated project. </p>
 </dd>
<dt><code>&lt;LANG&gt;_STANDARD_REQUIRED &lt;bool&gt;</code></dt>
<dd> <p> New in version 3.8. </p>
<p>Specify the <code>C_STANDARD_REQUIRED</code>, <code>CXX_STANDARD_REQUIRED</code>, <code>OBJC_STANDARD_REQUIRED</code>, <code>OBJCXX_STANDARD_REQUIRED</code>,or <code>CUDA_STANDARD_REQUIRED</code> target property of the generated project. </p>
 </dd>
<dt><code>&lt;LANG&gt;_EXTENSIONS &lt;bool&gt;</code></dt>
<dd> <p> New in version 3.8. </p>
<p>Specify the <code>C_EXTENSIONS</code>, <code>CXX_EXTENSIONS</code>, <code>OBJC_EXTENSIONS</code>, <code>OBJCXX_EXTENSIONS</code>, or <code>CUDA_EXTENSIONS</code> target property of the generated project. </p>
<p>In this version all files in <code>&lt;bindir&gt;/CMakeFiles/CMakeTmp</code> will be cleaned automatically. For debugging, <code>--debug-trycompile</code> can be passed to <code>cmake</code> to avoid this clean. However, multiple sequential <code>try_compile</code> operations reuse this single output directory. If you use <code>--debug-trycompile</code>, you can only debug one <code>try_compile</code> call at a time. The recommended procedure is to protect all <code>try_compile</code> calls in your project by <code>if(NOT DEFINED &lt;resultVar&gt;)</code> logic, configure with cmake all the way through once, then delete the cache entry associated with the try_compile call of interest, and then re-run cmake again with <code>--debug-trycompile</code>. </p>
 </dd></dl>
<h3>Other Behavior Settings</h3>
<p>New in version 3.4: If set, the following variables are passed in to the generated try_compile CMakeLists.txt to initialize compile target properties with default values: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_CUDA_RUNTIME_LIBRARY</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_ENABLE_EXPORTS</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_LINK_SEARCH_START_STATIC</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_LINK_SEARCH_END_STATIC</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_MSVC_RUNTIME_LIBRARY</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_POSITION_INDEPENDENT_CODE</code> </p>
<p>If <code>CMP0056</code> is set to <code>NEW</code>, then <code>CMAKE_EXE_LINKER_FLAGS</code> is passed in as well. </p>
<p>Changed in version 3.14: If <code>CMP0083</code> is set to <code>NEW</code>, then in order to obtain correct behavior at link time, the <code>check_pie_supported()</code> command from the <code>CheckPIESupported</code> module must be called before using the <i>try_compile()</i> command. </p>
<p>The current settings of <code>CMP0065</code> and <code>CMP0083</code> are propagated through to the generated test project. </p>
<p>Set the <code>CMAKE_TRY_COMPILE_CONFIGURATION</code> variable to choose a build configuration. </p>
<p>New in version 3.6: Set the <code>CMAKE_TRY_COMPILE_TARGET_TYPE</code> variable to specify the type of target used for the source file signature. </p>
<p>New in version 3.6: Set the <code>CMAKE_TRY_COMPILE_PLATFORM_VARIABLES</code> variable to specify variables that must be propagated into the test project. This variable is meant for use only in toolchain files and is only honored by the <code>try_compile()</code> command for the source files form, not when given a whole project. </p>
<p>Changed in version 3.8: If <code>CMP0067</code> is set to <code>NEW</code>, or any of the <code>&lt;LANG&gt;_STANDARD</code>, <code>&lt;LANG&gt;_STANDARD_REQUIRED</code>, or <code>&lt;LANG&gt;_EXTENSIONS</code> options are used, then the language standard variables are honored: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_C_STANDARD</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_C_STANDARD_REQUIRED</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_C_EXTENSIONS</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_CXX_STANDARD</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_CXX_STANDARD_REQUIRED</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_CXX_EXTENSIONS</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_OBJC_STANDARD</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_OBJC_STANDARD_REQUIRED</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_OBJC_EXTENSIONS</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_OBJCXX_STANDARD</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_OBJCXX_STANDARD_REQUIRED</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_OBJCXX_EXTENSIONS</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_CUDA_STANDARD</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_CUDA_STANDARD_REQUIRED</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_CUDA_EXTENSIONS</code> </p>
<p>Their values are used to set the corresponding target properties in the generated project (unless overridden by an explicit option). </p>
<p>Changed in version 3.14: For the <code>Green Hills MULTI</code> generator the GHS toolset and target system customization cache variables are also propagated into the test project. </p>
 </dd></dl>
<h3>try_run</h3>
<p>Try compiling and then running some code.  </p>
<h3>Try Compiling and Running Source Files</h3>
<pre><code>try_run(&lt;runResultVar&gt; &lt;compileResultVar&gt;
        &lt;bindir&gt; &lt;srcfile&gt; [CMAKE_FLAGS &lt;flags&gt;...]
        [COMPILE_DEFINITIONS &lt;defs&gt;...]
        [LINK_OPTIONS &lt;options&gt;...]
        [LINK_LIBRARIES &lt;libs&gt;...]
        [COMPILE_OUTPUT_VARIABLE &lt;var&gt;]
        [RUN_OUTPUT_VARIABLE &lt;var&gt;]
        [OUTPUT_VARIABLE &lt;var&gt;]
        [WORKING_DIRECTORY &lt;var&gt;]
        [ARGS &lt;args&gt;...])
</code></pre>
<p>Try compiling a <code>&lt;srcfile&gt;</code>. Returns <code>TRUE</code> or <code>FALSE</code> for success or failure in <code>&lt;compileResultVar&gt;</code>. If the compile succeeded, runs the executable and returns its exit code in <code>&lt;runResultVar&gt;</code>. If the executable was built, but failed to run, then <code>&lt;runResultVar&gt;</code> will be set to <code>FAILED_TO_RUN</code>. See the <code>try_compile()</code> command for information on how the test project is constructed to build the source file. </p>
<p>New in version 3.14: The names of the result variables <code>&lt;runResultVar&gt;</code> and <code>&lt;compileResultVar&gt;</code> are defined by the user. Previously, they had fixed names <code>RUN_RESULT_VAR</code> and <code>COMPILE_RESULT_VAR</code>. </p>
<p>The options are: </p>
<dl>
<dt><code>CMAKE_FLAGS &lt;flags&gt;...</code></dt>
<dd> <p> Specify flags of the form <code>-DVAR:TYPE=VALUE</code> to be passed to the <code>cmake</code> command-line used to drive the test build. The example in <code>try_compile()</code> shows how values for variables <code>INCLUDE_DIRECTORIES</code>, <code>LINK_DIRECTORIES</code>, and <code>LINK_LIBRARIES</code> are used. </p>
 </dd>
<dt><code>COMPILE_DEFINITIONS &lt;defs&gt;...</code></dt>
<dd> <p> Specify <code>-Ddefinition</code> arguments to pass to <code>add_definitions()</code> in the generated test project. </p>
 </dd>
<dt><code>COMPILE_OUTPUT_VARIABLE &lt;var&gt;</code></dt>
<dd> <p> Report the compile step build output in a given variable. </p>
 </dd>
<dt><code>LINK_LIBRARIES &lt;libs&gt;...</code></dt>
<dd> <p> New in version 3.2. </p>
<p>Specify libraries to be linked in the generated project. The list of libraries may refer to system libraries and to Imported Targets from the calling project. </p>
<p>If this option is specified, any <code>-DLINK_LIBRARIES=...</code> value given to the <code>CMAKE_FLAGS</code> option will be ignored. </p>
 </dd>
<dt><code>LINK_OPTIONS &lt;options&gt;...</code></dt>
<dd> <p> New in version 3.14. </p>
<p>Specify link step options to pass to <code>target_link_options()</code> in the generated project. </p>
 </dd>
<dt><code>OUTPUT_VARIABLE &lt;var&gt;</code></dt>
<dd> <p> Report the compile build output and the output from running the executable in the given variable. This option exists for legacy reasons. Prefer <code>COMPILE_OUTPUT_VARIABLE</code> and <code>RUN_OUTPUT_VARIABLE</code> instead. </p>
 </dd>
<dt><code>RUN_OUTPUT_VARIABLE &lt;var&gt;</code></dt>
<dd> <p> Report the output from running the executable in a given variable. </p>
 </dd>
<dt><code>WORKING_DIRECTORY &lt;var&gt;</code></dt>
<dd> <p> New in version 3.20. </p>
<p>Run the executable in the given directory. If no <code>WORKING_DIRECTORY</code> is specified, the executable will run in <code>&lt;bindir&gt;</code>. </p>
 </dd></dl>
<h3>Other Behavior Settings</h3>
<p>Set the <code>CMAKE_TRY_COMPILE_CONFIGURATION</code> variable to choose a build configuration.  </p>
<h3>Behavior when Cross Compiling</h3>
<p>New in version 3.3: Use <code>CMAKE_CROSSCOMPILING_EMULATOR</code> when running cross-compiled binaries. </p>
<p>When cross compiling, the executable compiled in the first step usually cannot be run on the build host. The <code>try_run</code> command checks the <code>CMAKE_CROSSCOMPILING</code> variable to detect whether CMake is in cross-compiling mode. If that is the case, it will still try to compile the executable, but it will not try to run the executable unless the <code>CMAKE_CROSSCOMPILING_EMULATOR</code> variable is set. Instead it will create cache variables which must be filled by the user or by presetting them in some CMake script file to the values the executable would have produced if it had been run on its actual target platform. These cache entries are: </p>
<dl>
<dt><code>&lt;runResultVar&gt;</code></dt>
<dd> <p> Exit code if the executable were to be run on the target platform. </p>
 </dd>
<dt><code>&lt;runResultVar&gt;__TRYRUN_OUTPUT</code></dt>
<dd> <p> Output from stdout and stderr if the executable were to be run on the target platform. This is created only if the <code>RUN_OUTPUT_VARIABLE</code> or <code>OUTPUT_VARIABLE</code> option was used. </p>
<p>In order to make cross compiling your project easier, use <code>try_run</code> only if really required. If you use <code>try_run</code>, use the <code>RUN_OUTPUT_VARIABLE</code> or <code>OUTPUT_VARIABLE</code> options only if really required. Using them will require that when cross-compiling, the cache variables will have to be set manually to the output of the executable. You can also &quot;guard&quot; the calls to <code>try_run</code> with an <code>if()</code> block checking the <code>CMAKE_CROSSCOMPILING</code> variable and provide an easy-to-preset alternative for this case. </p>
 </dd></dl>
<h2>CTEST COMMANDS</h2>
<p>These commands are available only in CTest scripts.  </p>
<h3>ctest_build</h3>
<p>Perform the CTest Build Step as a Dashboard Client. </p>
<pre><code>ctest_build([BUILD &lt;build-dir&gt;] [APPEND]
            [CONFIGURATION &lt;config&gt;]
            [PARALLEL_LEVEL &lt;parallel&gt;]
            [FLAGS &lt;flags&gt;]
            [PROJECT_NAME &lt;project-name&gt;]
            [TARGET &lt;target-name&gt;]
            [NUMBER_ERRORS &lt;num-err-var&gt;]
            [NUMBER_WARNINGS &lt;num-warn-var&gt;]
            [RETURN_VALUE &lt;result-var&gt;]
            [CAPTURE_CMAKE_ERROR &lt;result-var&gt;]
            )
</code></pre>
<p>Build the project and store results in <code>Build.xml</code> for submission with the <code>ctest_submit()</code> command. </p>
<p>The <code>CTEST_BUILD_COMMAND</code> variable may be set to explicitly specify the build command line. Otherwise the build command line is computed automatically based on the options given. </p>
<p>The options are: </p>
<dl>
<dt><code>BUILD &lt;build-dir&gt;</code></dt>
<dd> <p> Specify the top-level build directory. If not given, the <code>CTEST_BINARY_DIRECTORY</code> variable is used. </p>
 </dd>
<dt><code>APPEND</code></dt>
<dd> <p> Mark <code>Build.xml</code> for append to results previously submitted to a dashboard server since the last <code>ctest_start()</code> call. Append semantics are defined by the dashboard server in use. This does <i>not</i> cause results to be appended to a <code>.xml</code> file produced by a previous call to this command. </p>
 </dd>
<dt><code>CONFIGURATION &lt;config&gt;</code></dt>
<dd> <p> Specify the build configuration (e.g. <code>Debug</code>). If not specified the <code>CTEST_BUILD_CONFIGURATION</code> variable will be checked. Otherwise the <code>-C &lt;cfg&gt;</code> option given to the <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> command will be used, if any. </p>
 </dd>
<dt><code>PARALLEL_LEVEL &lt;parallel&gt;</code></dt>
<dd> <p> New in version 3.21. </p>
<p>Specify the parallel level of the underlying build system. If not specified, the <code>CMAKE_BUILD_PARALLEL_LEVEL</code> environment variable will be checked. </p>
 </dd>
<dt><code>FLAGS &lt;flags&gt;</code></dt>
<dd> <p> Pass additional arguments to the underlying build command. If not specified the <code>CTEST_BUILD_FLAGS</code> variable will be checked. This can, e.g., be used to trigger a parallel build using the <code>-j</code> option of make. See the <code>ProcessorCount</code> module for an example. </p>
 </dd>
<dt><code>PROJECT_NAME &lt;project-name&gt;</code></dt>
<dd> <p> Ignored since CMake 3.0. </p>
<p>Changed in version 3.14: This value is no longer required. </p>
 </dd>
<dt><code>TARGET &lt;target-name&gt;</code></dt>
<dd> <p> Specify the name of a target to build. If not specified the <code>CTEST_BUILD_TARGET</code> variable will be checked. Otherwise the default target will be built. This is the &quot;all&quot; target (called <code>ALL_BUILD</code> in Visual Studio Generators). </p>
 </dd>
<dt><code>NUMBER_ERRORS &lt;num-err-var&gt;</code></dt>
<dd> <p> Store the number of build errors detected in the given variable. </p>
 </dd>
<dt><code>NUMBER_WARNINGS &lt;num-warn-var&gt;</code></dt>
<dd> <p> Store the number of build warnings detected in the given variable. </p>
 </dd>
<dt><code>RETURN_VALUE &lt;result-var&gt;</code></dt>
<dd> <p> Store the return value of the native build tool in the given variable. </p>
 </dd>
<dt><code>CAPTURE_CMAKE_ERROR &lt;result-var&gt;</code></dt>
<dd> <p> New in version 3.7. </p>
<p>Store in the <code>&lt;result-var&gt;</code> variable -1 if there are any errors running the command and prevent ctest from returning non-zero if an error occurs. </p>
 </dd>
<dt><code>QUIET</code></dt>
<dd> <p> New in version 3.3. </p>
<p>Suppress any CTest-specific non-error output that would have been printed to the console otherwise. The summary of warnings / errors, as well as the output from the native build tool is unaffected by this option. </p>
 </dd></dl>
<h3>ctest_configure</h3>
<p>Perform the CTest Configure Step as a Dashboard Client. </p>
<pre><code>ctest_configure([BUILD &lt;build-dir&gt;] [SOURCE &lt;source-dir&gt;] [APPEND]
                [OPTIONS &lt;options&gt;] [RETURN_VALUE &lt;result-var&gt;] [QUIET]
                [CAPTURE_CMAKE_ERROR &lt;result-var&gt;])
</code></pre>
<p>Configure the project build tree and record results in <code>Configure.xml</code> for submission with the <code>ctest_submit()</code> command. </p>
<p>The options are: </p>
<dl>
<dt><code>BUILD &lt;build-dir&gt;</code></dt>
<dd> <p> Specify the top-level build directory. If not given, the <code>CTEST_BINARY_DIRECTORY</code> variable is used. </p>
 </dd>
<dt><code>SOURCE &lt;source-dir&gt;</code></dt>
<dd> <p> Specify the source directory. If not given, the <code>CTEST_SOURCE_DIRECTORY</code> variable is used. </p>
 </dd>
<dt><code>APPEND</code></dt>
<dd> <p> Mark <code>Configure.xml</code> for append to results previously submitted to a dashboard server since the last <code>ctest_start()</code> call. Append semantics are defined by the dashboard server in use. This does <i>not</i> cause results to be appended to a <code>.xml</code> file produced by a previous call to this command. </p>
 </dd>
<dt><code>OPTIONS &lt;options&gt;</code></dt>
<dd> <p> Specify command-line arguments to pass to the configuration tool. </p>
 </dd>
<dt><code>RETURN_VALUE &lt;result-var&gt;</code></dt>
<dd> <p> Store in the <code>&lt;result-var&gt;</code> variable the return value of the native configuration tool. </p>
 </dd>
<dt><code>CAPTURE_CMAKE_ERROR &lt;result-var&gt;</code></dt>
<dd> <p> New in version 3.7. </p>
<p>Store in the <code>&lt;result-var&gt;</code> variable -1 if there are any errors running the command and prevent ctest from returning non-zero if an error occurs. </p>
 </dd>
<dt><code>QUIET</code></dt>
<dd> <p> New in version 3.3. </p>
<p>Suppress any CTest-specific non-error messages that would have otherwise been printed to the console. Output from the underlying configure command is not affected. </p>
 </dd></dl>
<h3>ctest_coverage</h3>
<p>Perform the CTest Coverage Step as a Dashboard Client. </p>
<pre><code>ctest_coverage([BUILD &lt;build-dir&gt;] [APPEND]
               [LABELS &lt;label&gt;...]
               [RETURN_VALUE &lt;result-var&gt;]
               [CAPTURE_CMAKE_ERROR &lt;result-var&gt;]
               [QUIET]
               )
</code></pre>
<p>Collect coverage tool results and stores them in <code>Coverage.xml</code> for submission with the <code>ctest_submit()</code> command. </p>
<p>The options are: </p>
<dl>
<dt><code>BUILD &lt;build-dir&gt;</code></dt>
<dd> <p> Specify the top-level build directory. If not given, the <code>CTEST_BINARY_DIRECTORY</code> variable is used. </p>
 </dd>
<dt><code>APPEND</code></dt>
<dd> <p> Mark <code>Coverage.xml</code> for append to results previously submitted to a dashboard server since the last <code>ctest_start()</code> call. Append semantics are defined by the dashboard server in use. This does <i>not</i> cause results to be appended to a <code>.xml</code> file produced by a previous call to this command. </p>
 </dd>
<dt><code>LABELS</code></dt>
<dd> <p> Filter the coverage report to include only source files labeled with at least one of the labels specified. </p>
 </dd>
<dt><code>RETURN_VALUE &lt;result-var&gt;</code></dt>
<dd> <p> Store in the <code>&lt;result-var&gt;</code> variable <code>0</code> if coverage tools ran without error and non-zero otherwise. </p>
 </dd>
<dt><code>CAPTURE_CMAKE_ERROR &lt;result-var&gt;</code></dt>
<dd> <p> New in version 3.7. </p>
<p>Store in the <code>&lt;result-var&gt;</code> variable -1 if there are any errors running the command and prevent ctest from returning non-zero if an error occurs. </p>
 </dd>
<dt><code>QUIET</code></dt>
<dd> <p> New in version 3.3. </p>
<p>Suppress any CTest-specific non-error output that would have been printed to the console otherwise. The summary indicating how many lines of code were covered is unaffected by this option. </p>
 </dd></dl>
<h3>ctest_empty_binary_directory</h3>
<p>empties the binary directory </p>
<pre><code>ctest_empty_binary_directory( directory )
</code></pre>
<p>Removes a binary directory. This command will perform some checks prior to deleting the directory in an attempt to avoid malicious or accidental directory deletion.  </p>
<h3>ctest_memcheck</h3>
<p>Perform the CTest MemCheck Step as a Dashboard Client. </p>
<pre><code>ctest_memcheck([BUILD &lt;build-dir&gt;] [APPEND]
               [START &lt;start-number&gt;]
               [END &lt;end-number&gt;]
               [STRIDE &lt;stride-number&gt;]
               [EXCLUDE &lt;exclude-regex&gt;]
               [INCLUDE &lt;include-regex&gt;]
               [EXCLUDE_LABEL &lt;label-exclude-regex&gt;]
               [INCLUDE_LABEL &lt;label-include-regex&gt;]
               [EXCLUDE_FIXTURE &lt;regex&gt;]
               [EXCLUDE_FIXTURE_SETUP &lt;regex&gt;]
               [EXCLUDE_FIXTURE_CLEANUP &lt;regex&gt;]
               [PARALLEL_LEVEL &lt;level&gt;]
               [RESOURCE_SPEC_FILE &lt;file&gt;]
               [TEST_LOAD &lt;threshold&gt;]
               [SCHEDULE_RANDOM &lt;ON|OFF&gt;]
               [STOP_ON_FAILURE]
               [STOP_TIME &lt;time-of-day&gt;]
               [RETURN_VALUE &lt;result-var&gt;]
               [CAPTURE_CMAKE_ERROR &lt;result-var&gt;]
               [REPEAT &lt;mode&gt;:&lt;n&gt;]
               [OUTPUT_JUNIT &lt;file&gt;]
               [DEFECT_COUNT &lt;defect-count-var&gt;]
               [QUIET]
               )
</code></pre>
<p>Run tests with a dynamic analysis tool and store results in <code>MemCheck.xml</code> for submission with the <code>ctest_submit()</code> command. </p>
<p>Most options are the same as those for the <code>ctest_test()</code> command. </p>
<p>The options unique to this command are: </p>
<dl>
<dt><code>DEFECT_COUNT &lt;defect-count-var&gt;</code></dt>
<dd> <p> New in version 3.8. </p>
<p>Store in the <code>&lt;defect-count-var&gt;</code> the number of defects found. </p>
 </dd></dl>
<h3>ctest_read_custom_files</h3>
<p>read CTestCustom files. </p>
<pre><code>ctest_read_custom_files( directory ... )
</code></pre>
<p>Read all the CTestCustom.ctest or CTestCustom.cmake files from the given directory. </p>
<p>By default, invoking <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> without a script will read custom files from the binary directory.  </p>
<h3>ctest_run_script</h3>
<p>runs a ctest -S script </p>
<pre><code>ctest_run_script([NEW_PROCESS] script_file_name script_file_name1
            script_file_name2 ... [RETURN_VALUE var])
</code></pre>
<p>Runs a script or scripts much like if it was run from ctest -S. If no argument is provided then the current script is run using the current settings of the variables. If <code>NEW_PROCESS</code> is specified then each script will be run in a separate process.If <code>RETURN_VALUE</code> is specified the return value of the last script run will be put into <code>var</code>.  </p>
<h3>ctest_sleep</h3>
<p>sleeps for some amount of time </p>
<pre><code>ctest_sleep(&lt;seconds&gt;)
</code></pre>
<p>Sleep for given number of seconds. </p>
<pre><code>ctest_sleep(&lt;time1&gt; &lt;duration&gt; &lt;time2&gt;)
</code></pre>
<p>Sleep for t=(time1 + duration &#8211; time2) seconds if t &gt; 0.  </p>
<h3>ctest_start</h3>
<p>Starts the testing for a given model </p>
<pre><code>ctest_start(&lt;model&gt; [&lt;source&gt; [&lt;binary&gt;]] [GROUP &lt;group&gt;] [QUIET])
ctest_start([&lt;model&gt; [&lt;source&gt; [&lt;binary&gt;]]] [GROUP &lt;group&gt;] APPEND [QUIET])
</code></pre>
<p>Starts the testing for a given model. The command should be called after the binary directory is initialized. </p>
<p>The parameters are as follows: </p>
<dl>
<dt><code>&lt;model&gt;</code></dt>
<dd> <p> Set the dashboard model. Must be one of <code>Experimental</code>, <code>Continuous</code>, or <code>Nightly</code>. This parameter is required unless <code>APPEND</code> is specified. </p>
 </dd>
<dt><code>&lt;source&gt;</code></dt>
<dd> <p> Set the source directory. If not specified, the value of <code>CTEST_SOURCE_DIRECTORY</code> is used instead. </p>
 </dd>
<dt><code>&lt;binary&gt;</code></dt>
<dd> <p> Set the binary directory. If not specified, the value of <code>CTEST_BINARY_DIRECTORY</code> is used instead. </p>
 </dd>
<dt><code>GROUP &lt;group&gt;</code></dt>
<dd> <p> If <code>GROUP</code> is used, the submissions will go to the specified group on the CDash server. If no <code>GROUP</code> is specified, the name of the model is used by default. </p>
<p>Changed in version 3.16: This replaces the deprecated option <code>TRACK</code>. Despite the name change its behavior is unchanged. </p>
 </dd>
<dt><code>APPEND</code></dt>
<dd> <p> If <code>APPEND</code> is used, the existing <code>TAG</code> is used rather than creating a new one based on the current time stamp. If you use <code>APPEND</code>, you can omit the <code>&lt;model&gt;</code> and <code>GROUP &lt;group&gt;</code> parameters, because they will be read from the generated <code>TAG</code> file. For example: </p>
<pre><code>ctest_start(Experimental GROUP GroupExperimental)
</code></pre>
<p>Later, in another <code>ctest -S</code> script: </p>
<pre><code>ctest_start(APPEND)
</code></pre>
<p>When the second script runs <code>ctest_start(APPEND)</code>, it will read the <code>Experimental</code> model and <code>GroupExperimental</code> group from the <code>TAG</code> file generated by the first <code>ctest_start()</code> command. Please note that if you call <code>ctest_start(APPEND)</code> and specify a different model or group than in the first <code>ctest_start()</code> command, a warning will be issued, and the new model and group will be used. </p>
 </dd>
<dt><code>QUIET</code></dt>
<dd> <p> New in version 3.3. </p>
<p>If <code>QUIET</code> is used, CTest will suppress any non-error messages that it otherwise would have printed to the console. </p>
<p>The parameters for <code>ctest_start()</code> can be issued in any order, with the exception that <code>&lt;model&gt;</code>, <code>&lt;source&gt;</code>, and <code>&lt;binary&gt;</code> have to appear in that order with respect to each other. The following are all valid and equivalent: </p>
<pre><code>ctest_start(Experimental path/to/source path/to/binary GROUP SomeGroup QUIET APPEND)
ctest_start(GROUP SomeGroup Experimental QUIET path/to/source APPEND path/to/binary)
ctest_start(APPEND QUIET Experimental path/to/source GROUP SomeGroup path/to/binary)
</code></pre>
<p>However, for the sake of readability, it is recommended that you order your parameters in the order listed at the top of this page. </p>
<p>If the <code>CTEST_CHECKOUT_COMMAND</code> variable (or the <code>CTEST_CVS_CHECKOUT</code> variable) is set, its content is treated as command-line. The command is invoked with the current working directory set to the parent of the source directory, even if the source directory already exists. This can be used to create the source tree from a version control repository. </p>
 </dd></dl>
<h3>ctest_submit</h3>
<p>Perform the CTest Submit Step as a Dashboard Client. </p>
<pre><code>ctest_submit([PARTS &lt;part&gt;...] [FILES &lt;file&gt;...]
             [SUBMIT_URL &lt;url&gt;]
             [BUILD_ID &lt;result-var&gt;]
             [HTTPHEADER &lt;header&gt;]
             [RETRY_COUNT &lt;count&gt;]
             [RETRY_DELAY &lt;delay&gt;]
             [RETURN_VALUE &lt;result-var&gt;]
             [CAPTURE_CMAKE_ERROR &lt;result-var&gt;]
             [QUIET]
             )
</code></pre>
<p>Submit results to a dashboard server. By default all available parts are submitted. </p>
<p>The options are: </p>
<dl>
<dt><code>PARTS &lt;part&gt;...</code></dt>
<dd> <p> Specify a subset of parts to submit. Valid part names are: </p>
<pre><code>Start = nothing
Update = ctest_update results, in Update.xml
Configure = ctest_configure results, in Configure.xml
Build = ctest_build results, in Build.xml
Test = ctest_test results, in Test.xml
Coverage = ctest_coverage results, in Coverage.xml
MemCheck = ctest_memcheck results, in DynamicAnalysis.xml and
             DynamicAnalysis-Test.xml
Notes = Files listed by CTEST_NOTES_FILES, in Notes.xml
ExtraFiles = Files listed by CTEST_EXTRA_SUBMIT_FILES
Upload = Files prepared for upload by ctest_upload(), in Upload.xml
Submit = nothing
Done = Build is complete, in Done.xml
</code></pre>
 </dd>
<dt><code>FILES &lt;file&gt;...</code></dt>
<dd> <p> Specify an explicit list of specific files to be submitted. Each individual file must exist at the time of the call. </p>
 </dd>
<dt><code>SUBMIT_URL &lt;url&gt;</code></dt>
<dd> <p> New in version 3.14. </p>
<p>The <code>http</code> or <code>https</code> URL of the dashboard server to send the submission to. If not given, the <code>CTEST_SUBMIT_URL</code> variable is used. </p>
 </dd>
<dt><code>BUILD_ID &lt;result-var&gt;</code></dt>
<dd> <p> New in version 3.15. </p>
<p>Store in the <code>&lt;result-var&gt;</code> variable the ID assigned to this build by CDash. </p>
 </dd>
<dt><code>HTTPHEADER &lt;HTTP-header&gt;</code></dt>
<dd> <p> New in version 3.9. </p>
<p>Specify HTTP header to be included in the request to CDash during submission. For example, CDash can be configured to only accept submissions from authenticated clients. In this case, you should provide a bearer token in your header: </p>
<pre><code>ctest_submit(HTTPHEADER &quot;Authorization: Bearer &lt;auth-token&gt;&quot;)
</code></pre>
<p>This suboption can be repeated several times for multiple headers. </p>
 </dd>
<dt><code>RETRY_COUNT &lt;count&gt;</code></dt>
<dd> <p> Specify how many times to retry a timed-out submission. </p>
 </dd>
<dt><code>RETRY_DELAY &lt;delay&gt;</code></dt>
<dd> <p> Specify how long (in seconds) to wait after a timed-out submission before attempting to re-submit. </p>
 </dd>
<dt><code>RETURN_VALUE &lt;result-var&gt;</code></dt>
<dd> <p> Store in the <code>&lt;result-var&gt;</code> variable <code>0</code> for success and non-zero on failure. </p>
 </dd>
<dt><code>CAPTURE_CMAKE_ERROR &lt;result-var&gt;</code></dt>
<dd> <p> New in version 3.13. </p>
<p>Store in the <code>&lt;result-var&gt;</code> variable -1 if there are any errors running the command and prevent ctest from returning non-zero if an error occurs. </p>
 </dd>
<dt><code>QUIET</code></dt>
<dd> <p> New in version 3.3. </p>
<p>Suppress all non-error messages that would have otherwise been printed to the console. </p>
 </dd></dl>
<h3>Submit to CDash Upload API</h3>
<p>New in version 3.2. </p>
<pre><code>ctest_submit(CDASH_UPLOAD &lt;file&gt; [CDASH_UPLOAD_TYPE &lt;type&gt;]
             [SUBMIT_URL &lt;url&gt;]
             [BUILD_ID &lt;result-var&gt;]
             [HTTPHEADER &lt;header&gt;]
             [RETRY_COUNT &lt;count&gt;]
             [RETRY_DELAY &lt;delay&gt;]
             [RETURN_VALUE &lt;result-var&gt;]
             [QUIET])
</code></pre>
<p>This second signature is used to upload files to CDash via the CDash file upload API. The API first sends a request to upload to CDash along with a content hash of the file. If CDash does not already have the file, then it is uploaded. Along with the file, a CDash type string is specified to tell CDash which handler to use to process the data. </p>
<p>This signature interprets options in the same way as the first one. </p>
<p>New in version 3.8: Added the <code>RETRY_COUNT</code>, <code>RETRY_DELAY</code>, <code>QUIET</code> options. </p>
<p>New in version 3.9: Added the <code>HTTPHEADER</code> option. </p>
<p>New in version 3.13: Added the <code>RETURN_VALUE</code> option. </p>
<p>New in version 3.14: Added the <code>SUBMIT_URL</code> option. </p>
<p>New in version 3.15: Added the <code>BUILD_ID</code> option. </p>
<h3>ctest_test</h3>
<p>Perform the CTest Test Step as a Dashboard Client. </p>
<pre><code>ctest_test([BUILD &lt;build-dir&gt;] [APPEND]
           [START &lt;start-number&gt;]
           [END &lt;end-number&gt;]
           [STRIDE &lt;stride-number&gt;]
           [EXCLUDE &lt;exclude-regex&gt;]
           [INCLUDE &lt;include-regex&gt;]
           [EXCLUDE_LABEL &lt;label-exclude-regex&gt;]
           [INCLUDE_LABEL &lt;label-include-regex&gt;]
           [EXCLUDE_FIXTURE &lt;regex&gt;]
           [EXCLUDE_FIXTURE_SETUP &lt;regex&gt;]
           [EXCLUDE_FIXTURE_CLEANUP &lt;regex&gt;]
           [PARALLEL_LEVEL &lt;level&gt;]
           [RESOURCE_SPEC_FILE &lt;file&gt;]
           [TEST_LOAD &lt;threshold&gt;]
           [SCHEDULE_RANDOM &lt;ON|OFF&gt;]
           [STOP_ON_FAILURE]
           [STOP_TIME &lt;time-of-day&gt;]
           [RETURN_VALUE &lt;result-var&gt;]
           [CAPTURE_CMAKE_ERROR &lt;result-var&gt;]
           [REPEAT &lt;mode&gt;:&lt;n&gt;]
           [OUTPUT_JUNIT &lt;file&gt;]
           [QUIET]
           )
</code></pre>
<p>Run tests in the project build tree and store results in <code>Test.xml</code> for submission with the <code>ctest_submit()</code> command. </p>
<p>The options are: </p>
<dl>
<dt><code>BUILD &lt;build-dir&gt;</code></dt>
<dd> <p> Specify the top-level build directory. If not given, the <code>CTEST_BINARY_DIRECTORY</code> variable is used. </p>
 </dd>
<dt><code>APPEND</code></dt>
<dd> <p> Mark <code>Test.xml</code> for append to results previously submitted to a dashboard server since the last <code>ctest_start()</code> call. Append semantics are defined by the dashboard server in use. This does <i>not</i> cause results to be appended to a <code>.xml</code> file produced by a previous call to this command. </p>
 </dd>
<dt><code>START &lt;start-number&gt;</code></dt>
<dd> <p> Specify the beginning of a range of test numbers. </p>
 </dd>
<dt><code>END &lt;end-number&gt;</code></dt>
<dd> <p> Specify the end of a range of test numbers. </p>
 </dd>
<dt><code>STRIDE &lt;stride-number&gt;</code></dt>
<dd> <p> Specify the stride by which to step across a range of test numbers. </p>
 </dd>
<dt><code>EXCLUDE &lt;exclude-regex&gt;</code></dt>
<dd> <p> Specify a regular expression matching test names to exclude. </p>
 </dd>
<dt><code>INCLUDE &lt;include-regex&gt;</code></dt>
<dd> <p> Specify a regular expression matching test names to include. Tests not matching this expression are excluded. </p>
 </dd>
<dt><code>EXCLUDE_LABEL &lt;label-exclude-regex&gt;</code></dt>
<dd> <p> Specify a regular expression matching test labels to exclude. </p>
 </dd>
<dt><code>INCLUDE_LABEL &lt;label-include-regex&gt;</code></dt>
<dd> <p> Specify a regular expression matching test labels to include. Tests not matching this expression are excluded. </p>
 </dd>
<dt><code>EXCLUDE_FIXTURE &lt;regex&gt;</code></dt>
<dd> <p> New in version 3.7. </p>
<p>If a test in the set of tests to be executed requires a particular fixture, that fixture&#8217;s setup and cleanup tests would normally be added to the test set automatically. This option prevents adding setup or cleanup tests for fixtures matching the <code>&lt;regex&gt;</code>. Note that all other fixture behavior is retained, including test dependencies and skipping tests that have fixture setup tests that fail. </p>
 </dd>
<dt><code>EXCLUDE_FIXTURE_SETUP &lt;regex&gt;</code></dt>
<dd> <p> New in version 3.7. </p>
<p>Same as <code>EXCLUDE_FIXTURE</code> except only matching setup tests are excluded. </p>
 </dd>
<dt><code>EXCLUDE_FIXTURE_CLEANUP &lt;regex&gt;</code></dt>
<dd> <p> New in version 3.7. </p>
<p>Same as <code>EXCLUDE_FIXTURE</code> except only matching cleanup tests are excluded. </p>
 </dd>
<dt><code>PARALLEL_LEVEL &lt;level&gt;</code></dt>
<dd> <p> Specify a positive number representing the number of tests to be run in parallel. </p>
 </dd>
<dt><code>RESOURCE_SPEC_FILE &lt;file&gt;</code></dt>
<dd> <p> New in version 3.16. </p>
<p>Specify a resource specification file. See ctest-resource-allocation for more information. </p>
 </dd>
<dt><code>TEST_LOAD &lt;threshold&gt;</code></dt>
<dd> <p> New in version 3.4. </p>
<p>While running tests in parallel, try not to start tests when they may cause the CPU load to pass above a given threshold. If not specified the <code>CTEST_TEST_LOAD</code> variable will be checked, and then the <code>--test-load</code> command-line argument to <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>. See also the <code>TestLoad</code> setting in the CTest Test Step. </p>
 </dd>
<dt><code>REPEAT &lt;mode&gt;:&lt;n&gt;</code></dt>
<dd> <p> New in version 3.17. </p>
<p>Run tests repeatedly based on the given <code>&lt;mode&gt;</code> up to <code>&lt;n&gt;</code> times. The modes are: </p>
 </dd>
<dt><code>UNTIL_FAIL</code></dt>
<dd> <p> Require each test to run <code>&lt;n&gt;</code> times without failing in order to pass. This is useful in finding sporadic failures in test cases. </p>
 </dd>
<dt><code>UNTIL_PASS</code></dt>
<dd> <p> Allow each test to run up to <code>&lt;n&gt;</code> times in order to pass. Repeats tests if they fail for any reason. This is useful in tolerating sporadic failures in test cases. </p>
 </dd>
<dt><code>AFTER_TIMEOUT</code></dt>
<dd> <p> Allow each test to run up to <code>&lt;n&gt;</code> times in order to pass. Repeats tests only if they timeout. This is useful in tolerating sporadic timeouts in test cases on busy machines. </p>
 </dd>
<dt><code>SCHEDULE_RANDOM &lt;ON|OFF&gt;</code></dt>
<dd> <p> Launch tests in a random order. This may be useful for detecting implicit test dependencies. </p>
 </dd>
<dt><code>STOP_ON_FAILURE</code></dt>
<dd> <p> New in version 3.18. </p>
<p>Stop the execution of the tests once one has failed. </p>
 </dd>
<dt><code>STOP_TIME &lt;time-of-day&gt;</code></dt>
<dd> <p> Specify a time of day at which the tests should all stop running. </p>
 </dd>
<dt><code>RETURN_VALUE &lt;result-var&gt;</code></dt>
<dd> <p> Store in the <code>&lt;result-var&gt;</code> variable <code>0</code> if all tests passed. Store non-zero if anything went wrong. </p>
 </dd>
<dt><code>CAPTURE_CMAKE_ERROR &lt;result-var&gt;</code></dt>
<dd> <p> New in version 3.7. </p>
<p>Store in the <code>&lt;result-var&gt;</code> variable -1 if there are any errors running the command and prevent ctest from returning non-zero if an error occurs. </p>
 </dd>
<dt><code>OUTPUT_JUNIT &lt;file&gt;</code></dt>
<dd> <p> New in version 3.21. </p>
<p>Write test results to <code>&lt;file&gt;</code> in JUnit XML format. If <code>&lt;file&gt;</code> is a relative path, it will be placed in the build directory. If <code>&lt;file&gt;</code> already exists, it will be overwritten. Note that the resulting JUnit XML file is <code>not</code> uploaded to CDash because it would be redundant with CTest&#8217;s <code>Test.xml</code> file. </p>
 </dd>
<dt><code>QUIET</code></dt>
<dd> <p> New in version 3.3. </p>
<p>Suppress any CTest-specific non-error messages that would have otherwise been printed to the console. Output from the underlying test command is not affected. Summary info detailing the percentage of passing tests is also unaffected by the <code>QUIET</code> option. </p>
<p>See also the <code>CTEST_CUSTOM_MAXIMUM_PASSED_TEST_OUTPUT_SIZE</code> and <code>CTEST_CUSTOM_MAXIMUM_FAILED_TEST_OUTPUT_SIZE</code> variables. </p>
 </dd></dl>
<h3>Additional Test Measurements</h3>
<p>CTest can parse the output of your tests for extra measurements to report to CDash. </p>
<p>When run as a Dashboard Client, CTest will include these custom measurements in the <code>Test.xml</code> file that gets uploaded to CDash. </p>
<p>Check the <i>CDash test measurement documentation</i> for more information on the types of test measurements that CDash recognizes. </p>
<p>The following example demonstrates how to output a variety of custom test measurements. </p>
<pre><code>std::cout &lt;&lt;
  &quot;&lt;CTestMeasurement type=\&quot;numeric/double\&quot; name=\&quot;score\&quot;&gt;28.3&lt;/CTestMeasurement&gt;&quot;
  &lt;&lt; std::endl;
std::cout &lt;&lt;
  &quot;&lt;CTestMeasurement type=\&quot;text/string\&quot; name=\&quot;color\&quot;&gt;red&lt;/CTestMeasurement&gt;&quot;
  &lt;&lt; std::endl;
std::cout &lt;&lt;
  &quot;&lt;CTestMeasurement type=\&quot;text/link\&quot; name=\&quot;CMake URL\&quot;&gt;https://cmake.org&lt;/CTestMeasurement&gt;&quot;
  &lt;&lt; std::endl;
std::cout &lt;&lt;
  &quot;&lt;CTestMeasurement type=\&quot;text/preformatted\&quot; name=\&quot;Console Output\&quot;&gt;&quot; &lt;&lt;
  &quot;line 1.\n&quot; &lt;&lt;
  &quot; \033[31;1m line 2. Bold red, and indented!\033[0;0ml\n&quot; &lt;&lt;
  &quot;line 3. Not bold or indented...\n&quot; &lt;&lt;
  &quot;&lt;/CTestMeasurement&gt;&quot; &lt;&lt; std::endl;
</code></pre>
<h3>Image Measurements</h3>
<p>The following example demonstrates how to upload test images to CDash. </p>
<pre><code>std::cout &lt;&lt;
  &quot;&lt;CTestMeasurementFile type=\&quot;image/jpg\&quot; name=\&quot;TestImage\&quot;&gt;&quot; &lt;&lt;
  &quot;/dir/to/test_img.jpg&lt;/CTestMeasurementFile&gt;&quot; &lt;&lt; std::endl;
std::cout &lt;&lt;
  &quot;&lt;CTestMeasurementFile type=\&quot;image/gif\&quot; name=\&quot;ValidImage\&quot;&gt;&quot; &lt;&lt;
  &quot;/dir/to/valid_img.gif&lt;/CTestMeasurementFile&gt;&quot; &lt;&lt; std::endl;
std::cout &lt;&lt;
  &quot;&lt;CTestMeasurementFile type=\&quot;image/png\&quot; name=\&quot;AlgoResult\&quot;&gt; &lt;&lt;
  &quot;/dir/to/img.png&lt;/CTestMeasurementFile&gt;&quot;
  &lt;&lt; std::endl;
</code></pre>
<p>Images will be displayed together in an interactive comparison mode on CDash if they are provided with two or more of the following names. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>TestImage</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>ValidImage</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>BaselineImage</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>DifferenceImage2</code> </p>
<p>By convention, <code>TestImage</code> is the image generated by your test, and <code>ValidImage</code> (or <code>BaselineImage</code>) is basis of comparison used to determine if the test passed or failed. </p>
<p>If another image name is used it will be displayed by CDash as a static image separate from the interactive comparison UI. </p>
 </dd></dl>
<h3>Attached Files</h3>
<p>New in version 3.21. </p>
<p>The following example demonstrates how to upload non-image files to CDash. </p>
<pre><code>std::cout &lt;&lt;
  &quot;&lt;CTestMeasurementFile type=\&quot;file\&quot; name=\&quot;TestInputData1\&quot;&gt;&quot; &lt;&lt;
  &quot;/dir/to/data1.csv&lt;/CTestMeasurementFile&gt;\n&quot; &lt;&lt;
  &quot;&lt;CTestMeasurementFile type=\&quot;file\&quot; name=\&quot;TestInputData2\&quot;&gt;&quot; &lt;&lt;
  &quot;/dir/to/data2.csv&lt;/CTestMeasurementFile&gt;&quot; &lt;&lt; std::endl;
</code></pre>
<p>If the name of the file to upload is known at configure time, you can use the <code>ATTACHED_FILES</code> or <code>ATTACHED_FILES_ON_FAIL</code> test properties instead.  </p>
<h3>Custom Details</h3>
<p>New in version 3.21. </p>
<p>The following example demonstrates how to specify a custom value for the <code>Test Details</code> field displayed on CDash. </p>
<pre><code>std::cout &lt;&lt;
  &quot;&lt;CTestDetails&gt;My Custom Details Value&lt;/CTestDetails&gt;&quot; &lt;&lt; std::endl;
</code></pre>
<h3>Additional Labels</h3>
<p>New in version 3.22. </p>
<p>The following example demonstrates how to add additional labels to a test at runtime. </p>
<pre><code>std::cout &lt;&lt;
  &quot;&lt;CTestLabel&gt;Custom Label 1&lt;/CTestLabel&gt;\n&quot; &lt;&lt;
  &quot;&lt;CTestLabel&gt;Custom Label 2&lt;/CTestLabel&gt;&quot; &lt;&lt; std::endl;
</code></pre>
<p>Use the <code>LABELS</code> test property instead for labels that can be determined at configure time.  </p>
<h3>ctest_update</h3>
<p>Perform the CTest Update Step as a Dashboard Client. </p>
<pre><code>ctest_update([SOURCE &lt;source-dir&gt;]
             [RETURN_VALUE &lt;result-var&gt;]
             [CAPTURE_CMAKE_ERROR &lt;result-var&gt;]
             [QUIET])
</code></pre>
<p>Update the source tree from version control and record results in <code>Update.xml</code> for submission with the <code>ctest_submit()</code> command. </p>
<p>The options are: </p>
<dl>
<dt><code>SOURCE &lt;source-dir&gt;</code></dt>
<dd> <p> Specify the source directory. If not given, the <code>CTEST_SOURCE_DIRECTORY</code> variable is used. </p>
 </dd>
<dt><code>RETURN_VALUE &lt;result-var&gt;</code></dt>
<dd> <p> Store in the <code>&lt;result-var&gt;</code> variable the number of files updated or <code>-1</code> on error. </p>
 </dd>
<dt><code>CAPTURE_CMAKE_ERROR &lt;result-var&gt;</code></dt>
<dd> <p> New in version 3.13. </p>
<p>Store in the <code>&lt;result-var&gt;</code> variable -1 if there are any errors running the command and prevent ctest from returning non-zero if an error occurs. </p>
 </dd>
<dt><code>QUIET</code></dt>
<dd> <p> New in version 3.3. </p>
<p>Tell CTest to suppress most non-error messages that it would have otherwise printed to the console. CTest will still report the new revision of the repository and any conflicting files that were found. </p>
<p>The update always follows the version control branch currently checked out in the source directory. See the CTest Update Step documentation for information about variables that change the behavior of <code>ctest_update()</code>. </p>
 </dd></dl>
<h3>ctest_upload</h3>
<p>Upload files to a dashboard server as a Dashboard Client. </p>
<pre><code>ctest_upload(FILES &lt;file&gt;... [QUIET] [CAPTURE_CMAKE_ERROR &lt;result-var&gt;])
</code></pre>
<p>The options are: </p>
<dl>
<dt><code>FILES &lt;file&gt;...</code></dt>
<dd> <p> Specify a list of files to be sent along with the build results to the dashboard server. </p>
 </dd>
<dt><code>QUIET</code></dt>
<dd> <p> New in version 3.3. </p>
<p>Suppress any CTest-specific non-error output that would have been printed to the console otherwise. </p>
 </dd>
<dt><code>CAPTURE_CMAKE_ERROR &lt;result-var&gt;</code></dt>
<dd> <p> New in version 3.7. </p>
<p>Store in the <code>&lt;result-var&gt;</code> variable -1 if there are any errors running the command and prevent ctest from returning non-zero if an error occurs. </p>
 </dd></dl>
<h2>DEPRECATED COMMANDS</h2>
<p>These commands are deprecated and are only made available to maintain backward compatibility. The documentation of each command states the CMake version in which it was deprecated. Do not use these commands in new code.  </p>
<h3>build_name</h3>
<p>Disallowed since version 3.0. See CMake Policy <code>CMP0036</code>. </p>
<p>Use <code>${CMAKE_SYSTEM}</code> and <code>${CMAKE_CXX_COMPILER}</code> instead. </p>
<pre><code>build_name(variable)
</code></pre>
<p>Sets the specified variable to a string representing the platform and compiler settings. These values are now available through the <code>CMAKE_SYSTEM</code> and <code>CMAKE_CXX_COMPILER</code> variables.  </p>
<h3>exec_program</h3>
<p>Deprecated since version 3.0: Use the <code>execute_process()</code> command instead. </p>
<p>Run an executable program during the processing of the CMakeList.txt file. </p>
<pre><code>exec_program(Executable [directory in which to run]
             [ARGS &lt;arguments to executable&gt;]
             [OUTPUT_VARIABLE &lt;var&gt;]
             [RETURN_VALUE &lt;var&gt;])
</code></pre>
<p>The executable is run in the optionally specified directory. The executable can include arguments if it is double quoted, but it is better to use the optional <code>ARGS</code> argument to specify arguments to the program. This is because cmake will then be able to escape spaces in the executable path. An optional argument <code>OUTPUT_VARIABLE</code> specifies a variable in which to store the output. To capture the return value of the execution, provide a <code>RETURN_VALUE</code>. If <code>OUTPUT_VARIABLE</code> is specified, then no output will go to the stdout/stderr of the console running cmake.  </p>
<h3>export_library_dependencies</h3>
<p>Disallowed since version 3.0. See CMake Policy <code>CMP0033</code>. </p>
<p>Use <code>install(EXPORT)</code> or <code>export()</code> command. </p>
<p>This command generates an old-style library dependencies file. Projects requiring CMake 2.6 or later should not use the command. Use instead the <code>install(EXPORT)</code> command to help export targets from an installation tree and the <code>export()</code> command to export targets from a build tree. </p>
<p>The old-style library dependencies file does not take into account per-configuration names of libraries or the <code>LINK_INTERFACE_LIBRARIES</code> target property. </p>
<pre><code>export_library_dependencies(&lt;file&gt; [APPEND])
</code></pre>
<p>Create a file named <code>&lt;file&gt;</code> that can be included into a CMake listfile with the INCLUDE command. The file will contain a number of SET commands that will set all the variables needed for library dependency information. This should be the last command in the top level CMakeLists.txt file of the project. If the <code>APPEND</code> option is specified, the SET commands will be appended to the given file instead of replacing it.  </p>
<h3>install_files</h3>
<p>Deprecated since version 3.0: Use the <code>install(FILES)</code> command instead. </p>
<p>This command has been superseded by the <code>install()</code> command. It is provided for compatibility with older CMake code. The <code>FILES</code> form is directly replaced by the <code>FILES</code> form of the <code>install()</code> command. The regexp form can be expressed more clearly using the <code>GLOB</code> form of the <code>file()</code> command. </p>
<pre><code>install_files(&lt;dir&gt; extension file file ...)
</code></pre>
<p>Create rules to install the listed files with the given extension into the given directory. Only files existing in the current source tree or its corresponding location in the binary tree may be listed. If a file specified already has an extension, that extension will be removed first. This is useful for providing lists of source files such as foo.cxx when you want the corresponding foo.h to be installed. A typical extension is <code>.h</code>. </p>
<pre><code>install_files(&lt;dir&gt; regexp)
</code></pre>
<p>Any files in the current source directory that match the regular expression will be installed. </p>
<pre><code>install_files(&lt;dir&gt; FILES file file ...)
</code></pre>
<p>Any files listed after the <code>FILES</code> keyword will be installed explicitly from the names given. Full paths are allowed in this form. </p>
<p>The directory <code>&lt;dir&gt;</code> is relative to the installation prefix, which is stored in the variable <code>CMAKE_INSTALL_PREFIX</code>.  </p>
<h3>install_programs</h3>
<p>Deprecated since version 3.0: Use the <code>install(PROGRAMS)</code> command instead. </p>
<p>This command has been superseded by the <code>install()</code> command. It is provided for compatibility with older CMake code. The <code>FILES</code> form is directly replaced by the <code>PROGRAMS</code> form of the <code>install()</code> command. The regexp form can be expressed more clearly using the <code>GLOB</code> form of the <code>file()</code> command. </p>
<pre><code>install_programs(&lt;dir&gt; file1 file2 [file3 ...])
install_programs(&lt;dir&gt; FILES file1 [file2 ...])
</code></pre>
<p>Create rules to install the listed programs into the given directory. Use the <code>FILES</code> argument to guarantee that the file list version of the command will be used even when there is only one argument. </p>
<pre><code>install_programs(&lt;dir&gt; regexp)
</code></pre>
<p>In the second form any program in the current source directory that matches the regular expression will be installed. </p>
<p>This command is intended to install programs that are not built by cmake, such as shell scripts. See the <code>TARGETS</code> form of the <code>install()</code> command to create installation rules for targets built by cmake. </p>
<p>The directory <code>&lt;dir&gt;</code> is relative to the installation prefix, which is stored in the variable <code>CMAKE_INSTALL_PREFIX</code>.  </p>
<h3>install_targets</h3>
<p>Deprecated since version 3.0: Use the <code>install(TARGETS)</code> command instead. </p>
<p>This command has been superseded by the <code>install()</code> command. It is provided for compatibility with older CMake code. </p>
<pre><code>install_targets(&lt;dir&gt; [RUNTIME_DIRECTORY dir] target target)
</code></pre>
<p>Create rules to install the listed targets into the given directory. The directory <code>&lt;dir&gt;</code> is relative to the installation prefix, which is stored in the variable <code>CMAKE_INSTALL_PREFIX</code>. If <code>RUNTIME_DIRECTORY</code> is specified, then on systems with special runtime files (Windows DLL), the files will be copied to that directory.  </p>
<h3>load_command</h3>
<p>Disallowed since version 3.0. See CMake Policy <code>CMP0031</code>. </p>
<p>Load a command into a running CMake. </p>
<pre><code>load_command(COMMAND_NAME &lt;loc1&gt; [loc2 ...])
</code></pre>
<p>The given locations are searched for a library whose name is cmCOMMAND_NAME. If found, it is loaded as a module and the command is added to the set of available CMake commands. Usually, <code>try_compile()</code> is used before this command to compile the module. If the command is successfully loaded a variable named </p>
<pre><code>CMAKE_LOADED_COMMAND_&lt;COMMAND_NAME&gt;
</code></pre>
<p>will be set to the full path of the module that was loaded. Otherwise the variable will not be set.  </p>
<h3>make_directory</h3>
<p>Deprecated since version 3.0: Use the <code>file(MAKE_DIRECTORY)</code> command instead. </p>
<pre><code>make_directory(directory)
</code></pre>
<p>Creates the specified directory. Full paths should be given. Any parent directories that do not exist will also be created. Use with care.  </p>
<h3>output_required_files</h3>
<p>Disallowed since version 3.0. See CMake Policy <code>CMP0032</code>. </p>
<p>Approximate C preprocessor dependency scanning. </p>
<p>This command exists only because ancient CMake versions provided it. CMake handles preprocessor dependency scanning automatically using a more advanced scanner. </p>
<pre><code>output_required_files(srcfile outputfile)
</code></pre>
<p>Outputs a list of all the source files that are required by the specified <code>srcfile</code>. This list is written into <code>outputfile</code>. This is similar to writing out the dependencies for <code>srcfile</code> except that it jumps from <code>.h</code> files into <code>.cxx</code>, <code>.c</code> and <code>.cpp</code> files if possible.  </p>
<h3>qt_wrap_cpp</h3>
<p>Deprecated since version 3.14: This command was originally added to support Qt 3 before the <code>add_custom_command()</code> command was sufficiently mature. The <code>FindQt4</code> module provides the <code>qt4_wrap_cpp()</code> macro, which should be used instead for Qt 4 projects. For projects using Qt 5 or later, use the equivalent macro provided by Qt itself (e.g. Qt 5 provides <code>qt5_wrap_cpp()</code>). </p>
<p>Manually create Qt Wrappers. </p>
<pre><code>qt_wrap_cpp(resultingLibraryName DestName SourceLists ...)
</code></pre>
<p>Produces moc files for all the .h files listed in the SourceLists. The moc files will be added to the library using the <code>DestName</code> source list. </p>
<p>Consider updating the project to use the <code>AUTOMOC</code> target property instead for a more automated way of invoking the <code>moc</code> tool.  </p>
<h3>qt_wrap_ui</h3>
<p>Deprecated since version 3.14: This command was originally added to support Qt 3 before the <code>add_custom_command()</code> command was sufficiently mature. The <code>FindQt4</code> module provides the <code>qt4_wrap_ui()</code> macro, which should be used instead for Qt 4 projects. For projects using Qt 5 or later, use the equivalent macro provided by Qt itself (e.g. Qt 5 provides <code>qt5_wrap_ui()</code>). </p>
<p>Manually create Qt user interfaces Wrappers. </p>
<pre><code>qt_wrap_ui(resultingLibraryName HeadersDestName
           SourcesDestName SourceLists ...)
</code></pre>
<p>Produces .h and .cxx files for all the .ui files listed in the <code>SourceLists</code>. The .h files will be added to the library using the <code>HeadersDestNamesource</code> list. The .cxx files will be added to the library using the <code>SourcesDestNamesource</code> list. </p>
<p>Consider updating the project to use the <code>AUTOUIC</code> target property instead for a more automated way of invoking the <code>uic</code> tool.  </p>
<h3>remove</h3>
<p>Deprecated since version 3.0: Use the <code>list(REMOVE_ITEM)</code> command instead. </p>
<pre><code>remove(VAR VALUE VALUE ...)
</code></pre>
<p>Removes <code>VALUE</code> from the variable <code>VAR</code>. This is typically used to remove entries from a vector (e.g. semicolon separated list). <code>VALUE</code> is expanded.  </p>
<h3>subdir_depends</h3>
<p>Disallowed since version 3.0. See CMake Policy <code>CMP0029</code>. </p>
<p>Does nothing. </p>
<pre><code>subdir_depends(subdir dep1 dep2 ...)
</code></pre>
<p>Does not do anything. This command used to help projects order parallel builds correctly. This functionality is now automatic.  </p>
<h3>subdirs</h3>
<p>Deprecated since version 3.0: Use the <code>add_subdirectory()</code> command instead. </p>
<p>Add a list of subdirectories to the build. </p>
<pre><code>subdirs(dir1 dir2 ...[EXCLUDE_FROM_ALL exclude_dir1 exclude_dir2 ...]
        [PREORDER] )
</code></pre>
<p>Add a list of subdirectories to the build. The <code>add_subdirectory()</code> command should be used instead of <code>subdirs</code> although <code>subdirs</code> will still work. This will cause any CMakeLists.txt files in the sub directories to be processed by CMake. Any directories after the <code>PREORDER</code> flag are traversed first by makefile builds, the <code>PREORDER</code> flag has no effect on IDE projects. Any directories after the <code>EXCLUDE_FROM_ALL</code> marker will not be included in the top level makefile or project file. This is useful for having CMake create makefiles or projects for a set of examples in a project. You would want CMake to generate makefiles or project files for all the examples at the same time, but you would not want them to show up in the top level project or be built each time make is run from the top.  </p>
<h3>use_mangled_mesa</h3>
<p>Disallowed since version 3.0. See CMake Policy <code>CMP0030</code>. </p>
<p>Copy mesa headers for use in combination with system GL. </p>
<pre><code>use_mangled_mesa(PATH_TO_MESA OUTPUT_DIRECTORY)
</code></pre>
<p>The path to mesa includes, should contain <code>gl_mangle.h</code>. The mesa headers are copied to the specified output directory. This allows mangled mesa headers to override other GL headers by being added to the include directory path earlier.  </p>
<h3>utility_source</h3>
<p>Disallowed since version 3.0. See CMake Policy <code>CMP0034</code>. </p>
<p>Specify the source tree of a third-party utility. </p>
<pre><code>utility_source(cache_entry executable_name
               path_to_source [file1 file2 ...])
</code></pre>
<p>When a third-party utility&#8217;s source is included in the distribution, this command specifies its location and name. The cache entry will not be set unless the <code>path_to_source</code> and all listed files exist. It is assumed that the source tree of the utility will have been built before it is needed. </p>
<p>When cross compiling CMake will print a warning if a <code>utility_source()</code> command is executed, because in many cases it is used to build an executable which is executed later on. This doesn&#8217;t work when cross compiling, since the executable can run only on their target platform. So in this case the cache entry has to be adjusted manually so it points to an executable which is runnable on the build host.  </p>
<h3>variable_requires</h3>
<p>Disallowed since version 3.0. See CMake Policy <code>CMP0035</code>. </p>
<p>Use the <code>if()</code> command instead. </p>
<p>Assert satisfaction of an option&#8217;s required variables. </p>
<pre><code>variable_requires(TEST_VARIABLE RESULT_VARIABLE
                  REQUIRED_VARIABLE1
                  REQUIRED_VARIABLE2 ...)
</code></pre>
<p>The first argument (<code>TEST_VARIABLE</code>) is the name of the variable to be tested, if that variable is false nothing else is done. If <code>TEST_VARIABLE</code> is true, then the next argument (<code>RESULT_VARIABLE</code>) is a variable that is set to true if all the required variables are set. The rest of the arguments are variables that must be true or not set to <code>NOTFOUND</code> to avoid an error. If any are not true, an error is reported.  </p>
<h3>write_file</h3>
<p>Deprecated since version 3.0: Use the <code>file(WRITE)</code> command instead. </p>
<pre><code>write_file(filename &quot;message to write&quot;... [APPEND])
</code></pre>
<p>The first argument is the file name, the rest of the arguments are messages to write. If the argument <code>APPEND</code> is specified, then the message will be appended. </p>
<p>NOTE 1: <code>file(WRITE)</code> and <code>file(APPEND)</code> do exactly the same as this one but add some more functionality. </p>
<p>NOTE 2: When using <code>write_file</code> the produced file cannot be used as an input to CMake (CONFIGURE_FILE, source file ...) because it will lead to an infinite loop. Use <code>configure_file()</code> if you want to generate input files to CMake.  </p>
<h2>COPYRIGHT</h2>
<p> 2000-2022 Kitware, Inc. and Contributors </p>
