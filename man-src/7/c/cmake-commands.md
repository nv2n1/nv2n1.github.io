---
title: "cmake-commands(7)"
name: "cmake-commands"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake-commands/"
description: "cmake-commands – CMake Language Command Reference"
---

<p>cmake-commands &#8211; CMake Language Command Reference</p>
<h2>Scripting Commands</h2>
<p>These commands are always available.</p>
<h3>break</h3>
<p>Break from an enclosing foreach or while loop. </p>
<pre>break()</pre>
<p>Breaks from an enclosing <code>foreach()</code> or <code>while()</code> loop. </p>
<p> See also the <code>continue()</code> command.</p>
<h3>cmake_host_system_information</h3>
<p>Query host system specific information. </p>
<pre>cmake_host_system_information(RESULT &lt;variable&gt; QUERY &lt;key&gt; ...)</pre>
<p>Queries system information of the host system on which cmake runs. One or more <code>&lt;key&gt;</code> can be provided to select the information to be queried. The list of queried values is stored in <code>&lt;variable&gt;</code>. </p>
<p> <code>&lt;key&gt;</code> can be one of the following values:</p>
<dl>
<dt><code>NUMBER_OF_LOGICAL_CORES</code></p>
<dd>Number of logical cores</p>
<dt><code>NUMBER_OF_PHYSICAL_CORES</code></p>
<dd>Number of physical cores</p>
<dt><code>HOSTNAME</code></p>
<dd>Hostname</p>
<dt><code>FQDN</code></p>
<dd>Fully qualified domain name</p>
<dt><code>TOTAL_VIRTUAL_MEMORY</code></p>
<dd>Total virtual memory in MiB [1]</p>
<dt><code>AVAILABLE_VIRTUAL_MEMORY</code></p>
<dd>Available virtual memory in MiB [1]</p>
<dt><code>TOTAL_PHYSICAL_MEMORY</code></p>
<dd>Total physical memory in MiB [1]</p>
<dt><code>AVAILABLE_PHYSICAL_MEMORY</code></p>
<dd>Available physical memory in MiB [1]</p>
<dt><code>IS_64BIT</code></p>
<dd>New in version 3.10. </p>
<p> One if processor is 64Bit</p>
<dt><code>HAS_FPU</code></p>
<dd>New in version 3.10. </p>
<p> One if processor has floating point unit</p>
<dt><code>HAS_MMX</code></p>
<dd>New in version 3.10. </p>
<p> One if processor supports MMX instructions</p>
<dt><code>HAS_MMX_PLUS</code></p>
<dd>New in version 3.10. </p>
<p> One if processor supports Ext. MMX instructions</p>
<dt><code>HAS_SSE</code></p>
<dd>New in version 3.10. </p>
<p> One if processor supports SSE instructions</p>
<dt><code>HAS_SSE2</code></p>
<dd>New in version 3.10. </p>
<p> One if processor supports SSE2 instructions</p>
<dt><code>HAS_SSE_FP</code></p>
<dd>New in version 3.10. </p>
<p> One if processor supports SSE FP instructions</p>
<dt><code>HAS_SSE_MMX</code></p>
<dd>New in version 3.10. </p>
<p> One if processor supports SSE MMX instructions</p>
<dt><code>HAS_AMD_3DNOW</code></p>
<dd>New in version 3.10. </p>
<p> One if processor supports 3DNow instructions</p>
<dt><code>HAS_AMD_3DNOW_PLUS</code></p>
<dd>New in version 3.10. </p>
<p> One if processor supports 3DNow+ instructions</p>
<dt><code>HAS_IA64</code></p>
<dd>New in version 3.10. </p>
<p> One if IA64 processor emulating x86</p>
<dt><code>HAS_SERIAL_NUMBER</code></p>
<dd>New in version 3.10. </p>
<p> One if processor has serial number</p>
<dt><code>PROCESSOR_SERIAL_NUMBER</code></p>
<dd>New in version 3.10. </p>
<p> Processor serial number</p>
<dt><code>PROCESSOR_NAME</code></p>
<dd>New in version 3.10. </p>
<p> Human readable processor name</p>
<dt><code>PROCESSOR_DESCRIPTION</code></p>
<dd>New in version 3.10. </p>
<p> Human readable full processor description</p>
<dt><code>OS_NAME</code></p>
<dd>New in version 3.10. </p>
<p> See <code>CMAKE_HOST_SYSTEM_NAME</code></p>
<dt><code>OS_RELEASE</code></p>
<dd>New in version 3.10. </p>
<p> The OS sub-type e.g. on Windows <code>Professional</code></p>
<dt><code>OS_VERSION</code></p>
<dd>New in version 3.10. </p>
<p> The OS build ID</p>
<dt><code>OS_PLATFORM</code></p>
<dd>New in version 3.10. </p>
<p> See <code>CMAKE_HOST_SYSTEM_PROCESSOR</code></p>
<dt><code>DISTRIB_INFO</code></p>
<dd>New in version 3.22. </p>
<p> Read <code>/etc/os-release</code> file and define the given <code>&lt;variable&gt;</code> into a list of read variables</p>
<dt><code>DISTRIB_&lt;name&gt;</code></p>
<dd>New in version 3.22. </p>
<p> Get the <code>&lt;name&gt;</code> variable (see <i>man 5 os-release</i>) if it exists in the <code>/etc/os-release</code> file </p>
<p> Example: </p>
<pre>cmake_host_system_information(RESULT PRETTY_NAME QUERY DISTRIB_PRETTY_NAME)
message(STATUS &quot;${PRETTY_NAME}&quot;)
cmake_host_system_information(RESULT DISTRO QUERY DISTRIB_INFO)
foreach(VAR IN LISTS DISTRO)
 message(STATUS &quot;${VAR}=`${${VAR}}`&quot;)
endforeach()</pre>
<p>Output: </p>
<pre>-- Ubuntu 20.04.2 LTS
-- DISTRO_BUG_REPORT_URL=`<a rel="nofollow" href="https://bugs.launchpad.net/ubuntu/`">https://bugs.launchpad.net/ubuntu/`</a>
-- DISTRO_HOME_URL=`<a rel="nofollow" href="https://www.ubuntu.com/`">https://www.ubuntu.com/`</a>
-- DISTRO_ID=`ubuntu`
-- DISTRO_ID_LIKE=`debian`
-- DISTRO_NAME=`Ubuntu`
-- DISTRO_PRETTY_NAME=`Ubuntu 20.04.2 LTS`
-- DISTRO_PRIVACY_POLICY_URL=`<a rel="nofollow" href="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy`">https://www.ubuntu.com/legal/terms-and-policies/privacy-policy`</a>
-- DISTRO_SUPPORT_URL=`<a rel="nofollow" href="https://help.ubuntu.com/`">https://help.ubuntu.com/`</a>
-- DISTRO_UBUNTU_CODENAME=`focal`
-- DISTRO_VERSION=`20.04.2 LTS (Focal Fossa)`
-- DISTRO_VERSION_CODENAME=`focal`
-- DISTRO_VERSION_ID=`20.04`</pre>
<p>If <code>/etc/os-release</code> file is not found, the command tries to gather OS identification via fallback scripts. The fallback script can use <i>various distribution-specific files</i> to collect OS identification data and map it into <i>man 5 os-release</i> variables.</dl>
<h3>Fallback Interface Variables</h3>
<dl>
<dt><code>CMAKE_GET_OS_RELEASE_FALLBACK_SCRIPTS</code></p>
<dd>In addition to the scripts shipped with CMake, a user may append full paths to his script(s) to the this list. The script filename has the following format: <code>NNN-&lt;name&gt;.cmake</code>, where <code>NNN</code> is three digits used to apply collected scripts in a specific order.</p>
<dt><code>CMAKE_GET_OS_RELEASE_FALLBACK_RESULT_&lt;varname&gt;</code></p>
<dd>Variables collected by the user provided fallback script ought to be assigned to CMake variables using this naming convention. Example, the <code>ID</code> variable from the manual becomes <code>CMAKE_GET_OS_RELEASE_FALLBACK_RESULT_ID</code>.</p>
<dt><code>CMAKE_GET_OS_RELEASE_FALLBACK_RESULT</code></p>
<dd>The fallback script ought to store names of all assigned <code>CMAKE_GET_OS_RELEASE_FALLBACK_RESULT_&lt;varname&gt;</code> variables in this list. </p>
<p> Example: </p>
<pre># Try to detect some old distribution
# See also
# - <a rel="nofollow" href="http://linuxmafia.com/faq/Admin/release-files.html">http://linuxmafia.com/faq/Admin/release-files.html</a>
#
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
unset(CMAKE_GET_OS_RELEASE_FALLBACK_CONTENT)</pre>
</dl>
<h2>Footnotes</h2>
<dl>
<dt>[1]</p>
<dd>One MiB (mebibyte) is equal to 1024&#215;1024 bytes.</dl>
<h3>cmake_language</h3>
<p>New in version 3.18. </p>
<p> Call meta-operations on CMake commands.</p>
<h3>Synopsis</h3>
<pre>cmake_language(<i>CALL</i> &lt;command&gt; [&lt;arg&gt;...])
cmake_language(<i>EVAL</i> CODE &lt;code&gt;...)
cmake_language(<i>DEFER</i> &lt;options&gt;... CALL &lt;command&gt; [&lt;arg&gt;...])</pre>
<h3>Introduction</h3>
<p>This command will call meta-operations on built-in CMake commands or those created via the <code>macro()</code> or <code>function()</code> commands. </p>
<p> <code>cmake_language</code> does not introduce a new variable or policy scope.</p>
<h3>Calling Commands</h3>
<pre>cmake_language(CALL &lt;command&gt; [&lt;arg&gt;...])</pre>
<p>Calls the named <code>&lt;command&gt;</code> with the given arguments (if any). For example, the code: </p>
<pre>set(message_command &quot;message&quot;)
cmake_language(CALL ${message_command} STATUS &quot;Hello World!&quot;)</pre>
<p>is equivalent to </p>
<pre>message(STATUS &quot;Hello World!&quot;)</pre>
<p><code>NOTE:</code> To ensure consistency of the code, the following commands are not allowed:</p>
<dl>
<dt>&bull;</p>
<dd><code>if</code> / <code>elseif</code> / <code>else</code> / <code>endif</code></p>
<dt>&bull;</p>
<dd><code>while</code> / <code>endwhile</code></p>
<dt>&bull;</p>
<dd><code>foreach</code> / <code>endforeach</code></p>
<dt>&bull;</p>
<dd><code>function</code> / <code>endfunction</code></p>
<dt>&bull;</p>
<dd><code>macro</code> / <code>endmacro</code></dl>
<h3>Evaluating Code</h3>
<pre>cmake_language(EVAL CODE &lt;code&gt;...)</pre>
<p>Evaluates the <code>&lt;code&gt;&#8230;</code> as CMake code. </p>
<p> For example, the code: </p>
<pre>set(A TRUE)
set(B TRUE)
set(C TRUE)
set(condition &quot;(A AND B) OR C&quot;)
cmake_language(EVAL CODE &quot;
 if (${condition})
 message(STATUS TRUE)
 else()
 message(STATUS FALSE)
 endif()&quot;
)</pre>
<p>is equivalent to </p>
<pre>set(A TRUE)
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
include(${CMAKE_CURRENT_BINARY_DIR}/eval.cmake)</pre>
<h3>Deferring Calls</h3>
<p>New in version 3.19. </p>
<pre>cmake_language(DEFER &lt;options&gt;... CALL &lt;command&gt; [&lt;arg&gt;...])</pre>
<p>Schedules a call to the named <code>&lt;command&gt;</code> with the given arguments (if any) to occur at a later time. By default, deferred calls are executed as if written at the end of the current directory&#8217;s <code>CMakeLists.txt</code> file, except that they run even after a <code>return()</code> call. Variable references in arguments are evaluated at the time the deferred call is executed. </p>
<p> The options are:</p>
<dl>
<dt><code>DIRECTORY &lt;dir&gt;</code></p>
<dd>Schedule the call for the end of the given directory instead of the current directory. The <code>&lt;dir&gt;</code> may reference either a source directory or its corresponding binary directory. Relative paths are treated as relative to the current source directory. </p>
<p> The given directory must be known to CMake, being either the top-level directory or one added by <code>add_subdirectory()</code>. Furthermore, the given directory must not yet be finished processing. This means it can be the current directory or one of its ancestors.</p>
<dt><code>ID &lt;id&gt;</code></p>
<dd>Specify an identification for the deferred call. The <code>&lt;id&gt;</code> may not be empty and may not begin with a capital letter <code>A-Z</code>. The <code>&lt;id&gt;</code> may begin with an underscore (<code>_</code>) only if it was generated automatically by an earlier call that used <code>ID_VAR</code> to get the id.</p>
<dt><code>ID_VAR &lt;var&gt;</code></p>
<dd>Specify a variable in which to store the identification for the deferred call. If <code>ID &lt;id&gt;</code> is not given, a new identification will be generated and the generated id will start with an underscore (<code>_</code>). </p>
<p> The currently scheduled list of deferred calls may be retrieved: </p>
<pre>cmake_language(DEFER [DIRECTORY &lt;dir&gt;] GET_CALL_IDS &lt;var&gt;)</pre>
<p>This will store in <code>&lt;var&gt;</code> a semicolon-separated list of deferred call ids. The ids are for the directory scope in which the calls have been deferred to (i.e. where they will be executed), which can be different to the scope in which they were created. The <code>DIRECTORY</code> option can be used to specify the scope for which to retrieve the call ids. If that option is not given, the call ids for the current directory scope will be returned. </p>
<p> Details of a specific call may be retrieved from its id: </p>
<pre>cmake_language(DEFER [DIRECTORY &lt;dir&gt;] GET_CALL &lt;id&gt; &lt;var&gt;)</pre>
<p>This will store in <code>&lt;var&gt;</code> a semicolon-separated list in which the first element is the name of the command to be called, and the remaining elements are its unevaluated arguments (any contained <code>;</code> characters are included literally and cannot be distinguished from multiple arguments). If multiple calls are scheduled with the same id, this retrieves the first one. If no call is scheduled with the given id in the specified <code>DIRECTORY</code> scope (or the current directory scope if no <code>DIRECTORY</code> option is given), this stores an empty string in the variable. </p>
<p> Deferred calls may be canceled by their id: </p>
<pre>cmake_language(DEFER [DIRECTORY &lt;dir&gt;] CANCEL_CALL &lt;id&gt;...)</pre>
<p>This cancels all deferred calls matching any of the given ids in the specified <code>DIRECTORY</code> scope (or the current directory scope if no <code>DIRECTORY</code> option is given). Unknown ids are silently ignored.</dl>
<h3>Deferred Call Examples</h3>
<p>For example, the code: </p>
<pre>cmake_language(DEFER CALL message &quot;${deferred_message}&quot;)
cmake_language(DEFER ID_VAR id CALL message &quot;Canceled Message&quot;)
cmake_language(DEFER CANCEL_CALL ${id})
message(&quot;Immediate Message&quot;)
set(deferred_message &quot;Deferred Message&quot;)</pre>
<p>prints: </p>
<pre>Immediate Message
Deferred Message</pre>
<p>The <code>Cancelled Message</code> is never printed because its command is canceled. The <code>deferred_message</code> variable reference is not evaluated until the call site, so it can be set after the deferred call is scheduled. </p>
<p> In order to evaluate variable references immediately when scheduling a deferred call, wrap it using <code>cmake_language(EVAL)</code>. However, note that arguments will be re-evaluated in the deferred call, though that can be avoided by using bracket arguments. For example: </p>
<pre>set(deferred_message &quot;Deferred Message 1&quot;)
set(re_evaluated [[${deferred_message}]])
cmake_language(EVAL CODE &quot;
 cmake_language(DEFER CALL message [[${deferred_message}]])
 cmake_language(DEFER CALL message \&quot;${re_evaluated}\&quot;)
&quot;)
message(&quot;Immediate Message&quot;)
set(deferred_message &quot;Deferred Message 2&quot;)</pre>
<p>also prints: </p>
<pre>Immediate Message
Deferred Message 1
Deferred Message 2</pre>
<h3>cmake_minimum_required</h3>
<p>Require a minimum version of cmake. </p>
<pre>cmake_minimum_required(VERSION &lt;min&gt;[...&lt;policy_max&gt;] [FATAL_ERROR])</pre>
<p>New in version 3.12: The optional <code>&lt;policy_max&gt;</code> version. </p>
<p> Sets the minimum required version of cmake for a project. Also updates the policy settings as explained below. </p>
<p> <code>&lt;min&gt;</code> and the optional <code>&lt;policy_max&gt;</code> are each CMake versions of the form <code>major.minor[.patch[.tweak]]</code>, and the <code>&#8230;</code> is literal. </p>
<p> If the running version of CMake is lower than the <code>&lt;min&gt;</code> required version it will stop processing the project and report an error. The optional <code>&lt;policy_max&gt;</code> version, if specified, must be at least the <code>&lt;min&gt;</code> version and affects policy settings as described in <i>Policy Settings</i>. If the running version of CMake is older than 3.12, the extra <code>&#8230;</code> dots will be seen as version component separators, resulting in the <code>&#8230;&lt;max&gt;</code> part being ignored and preserving the pre-3.12 behavior of basing policies on <code>&lt;min&gt;</code>. </p>
<p> This command will set the value of the <code>CMAKE_MINIMUM_REQUIRED_VERSION</code> variable to <code>&lt;min&gt;</code>. </p>
<p> The <code>FATAL_ERROR</code> option is accepted but ignored by CMake 2.6 and higher. It should be specified so CMake versions 2.4 and lower fail with an error instead of just a warning. </p>
<p> <code>NOTE:</code> Call the <code>cmake_minimum_required()</code> command at the beginning of the top-level <code>CMakeLists.txt</code> file even before calling the <code>project()</code> command. It is important to establish version and policy settings before invoking other commands whose behavior they may affect. See also policy <code>CMP0000</code>. </p>
<p> Calling <code>cmake_minimum_required()</code> inside a <code>function()</code> limits some effects to the function scope when invoked. For example, the <code>CMAKE_MINIMUM_REQUIRED_VERSION</code> variable won&#8217;t be set in the calling scope. Functions do not introduce their own policy scope though, so policy settings of the caller <i>will</i> be affected (see below). Due to this mix of things that do and do not affect the calling scope, calling <code>cmake_minimum_required()</code> inside a function is generally discouraged.</p>
<h3>Policy Settings</h3>
<p>The <code>cmake_minimum_required(VERSION)</code> command implicitly invokes the <code>cmake_policy(VERSION)</code> command to specify that the current project code is written for the given range of CMake versions. All policies known to the running version of CMake and introduced in the <code>&lt;min&gt;</code> (or <code>&lt;max&gt;</code>, if specified) version or earlier will be set to use <code>NEW</code> behavior. All policies introduced in later versions will be unset. This effectively requests behavior preferred as of a given CMake version and tells newer CMake versions to warn about their new policies. </p>
<p> When a <code>&lt;min&gt;</code> version higher than 2.4 is specified the command implicitly invokes </p>
<pre>cmake_policy(VERSION &lt;min&gt;[...&lt;max&gt;])</pre>
<p>which sets CMake policies based on the range of versions specified. When a <code>&lt;min&gt;</code> version 2.4 or lower is given the command implicitly invokes </p>
<pre>cmake_policy(VERSION 2.4[...&lt;max&gt;])</pre>
<p>which enables compatibility features for CMake 2.4 and lower.</p>
<h3>cmake_parse_arguments</h3>
<p>Parse function or macro arguments. </p>
<pre>cmake_parse_arguments(&lt;prefix&gt; &lt;options&gt; &lt;one_value_keywords&gt;
 &lt;multi_value_keywords&gt; &lt;args&gt;...)
cmake_parse_arguments(PARSE_ARGV &lt;N&gt; &lt;prefix&gt; &lt;options&gt;
 &lt;one_value_keywords&gt; &lt;multi_value_keywords&gt;)</pre>
<p>New in version 3.5: This command is implemented natively. Previously, it has been defined in the module <code>CMakeParseArguments</code>. </p>
<p> This command is for use in macros or functions. It processes the arguments given to that macro or function, and defines a set of variables which hold the values of the respective options. </p>
<p> The first signature reads processes arguments passed in the <code>&lt;args&gt;&#8230;</code>. This may be used in either a <code>macro()</code> or a <code>function()</code>. </p>
<p> New in version 3.7: The <code>PARSE_ARGV</code> signature is only for use in a <code>function()</code> body. In this case the arguments that are parsed come from the <code>ARGV#</code> variables of the calling function. The parsing starts with the <code>&lt;N&gt;</code>-th argument, where <code>&lt;N&gt;</code> is an unsigned integer. This allows for the values to have special characters like <code>;</code> in them. </p>
<p> The <code>&lt;options&gt;</code> argument contains all options for the respective macro, i.e. keywords which can be used when calling the macro without any value following, like e.g. the <code>OPTIONAL</code> keyword of the <code>install()</code> command. </p>
<p> The <code>&lt;one_value_keywords&gt;</code> argument contains all keywords for this macro which are followed by one value, like e.g. <code>DESTINATION</code> keyword of the <code>install()</code> command. </p>
<p> The <code>&lt;multi_value_keywords&gt;</code> argument contains all keywords for this macro which can be followed by more than one value, like e.g. the <code>TARGETS</code> or <code>FILES</code> keywords of the <code>install()</code> command. </p>
<p> Changed in version 3.5: All keywords shall be unique. I.e. every keyword shall only be specified once in either <code>&lt;options&gt;</code>, <code>&lt;one_value_keywords&gt;</code> or <code>&lt;multi_value_keywords&gt;</code>. A warning will be emitted if uniqueness is violated. </p>
<p> When done, <code>cmake_parse_arguments</code> will consider for each of the keywords listed in <code>&lt;options&gt;</code>, <code>&lt;one_value_keywords&gt;</code> and <code>&lt;multi_value_keywords&gt;</code> a variable composed of the given <code>&lt;prefix&gt;</code> followed by <code>&quot;_&quot;</code> and the name of the respective keyword. These variables will then hold the respective value from the argument list or be undefined if the associated option could not be found. For the <code>&lt;options&gt;</code> keywords, these will always be defined, to <code>TRUE</code> or <code>FALSE</code>, whether the option is in the argument list or not. </p>
<p> All remaining arguments are collected in a variable <code>&lt;prefix&gt;_UNPARSED_ARGUMENTS</code> that will be undefined if all arguments were recognized. This can be checked afterwards to see whether your macro was called with unrecognized parameters. </p>
<p> New in version 3.15: <code>&lt;one_value_keywords&gt;</code> and <code>&lt;multi_value_keywords&gt;</code> that were given no values at all are collected in a variable <code>&lt;prefix&gt;_KEYWORDS_MISSING_VALUES</code> that will be undefined if all keywords received values. This can be checked to see if there were keywords without any values given. </p>
<p> Consider the following example macro, <code>my_install()</code>, which takes similar arguments to the real <code>install()</code> command: </p>
<pre>macro(my_install)
 set(options OPTIONAL FAST)
 set(oneValueArgs DESTINATION RENAME)
 set(multiValueArgs TARGETS CONFIGURATIONS)
 cmake_parse_arguments(MY_INSTALL &quot;${options}&quot; &quot;${oneValueArgs}&quot;
 &quot;${multiValueArgs}&quot; ${ARGN} )
 # ...</pre>
<p>Assume <code>my_install()</code> has been called like this: </p>
<pre>my_install(TARGETS foo bar DESTINATION bin OPTIONAL blub CONFIGURATIONS)</pre>
<p>After the <code>cmake_parse_arguments</code> call the macro will have set or undefined the following variables: </p>
<pre>MY_INSTALL_OPTIONAL = TRUE
MY_INSTALL_FAST = FALSE # was not used in call to my_install
MY_INSTALL_DESTINATION = &quot;bin&quot;
MY_INSTALL_RENAME &lt;UNDEFINED&gt; # was not used
MY_INSTALL_TARGETS = &quot;foo;bar&quot;
MY_INSTALL_CONFIGURATIONS &lt;UNDEFINED&gt; # was not used
MY_INSTALL_UNPARSED_ARGUMENTS = &quot;blub&quot; # nothing expected after &quot;OPTIONAL&quot;
MY_INSTALL_KEYWORDS_MISSING_VALUES = &quot;CONFIGURATIONS&quot;
 # No value for &quot;CONFIGURATIONS&quot; given</pre>
<p>You can then continue and process these variables. </p>
<p> Keywords terminate lists of values, e.g. if directly after a <code>one_value_keyword</code> another recognized keyword follows, this is interpreted as the beginning of the new option. E.g. <code>my_install(TARGETS foo DESTINATION OPTIONAL)</code> would result in <code>MY_INSTALL_DESTINATION</code> set to <code>&quot;OPTIONAL&quot;</code>, but as <code>OPTIONAL</code> is a keyword itself <code>MY_INSTALL_DESTINATION</code> will be empty (but added to <code>MY_INSTALL_KEYWORDS_MISSING_VALUES</code>) and <code>MY_INSTALL_OPTIONAL</code> will therefore be set to <code>TRUE</code>.</p>
<h3>cmake_path</h3>
<p>New in version 3.20. </p>
<p> This command is for the manipulation of paths. Only syntactic aspects of paths are handled, there is no interaction of any kind with any underlying file system. The path may represent a non-existing path or even one that is not allowed to exist on the current file system or platform. For operations that do interact with the filesystem, see the <code>file()</code> command. </p>
<p> <code>NOTE:</code> The <code>cmake_path</code> command handles paths in the format of the build system (i.e. the host platform), not the target system. When cross-compiling, if the path contains elements that are not representable on the host platform (e.g. a drive letter when the host is not Windows), the results will be unpredictable.</p>
<h3>Synopsis</h3>
<pre><i>Conventions</i>
<i>Path Structure And Terminology</i>
<i>Normalization</i>
<i>Decomposition</i>
 cmake_path(<i>GET</i> &lt;path-var&gt; <i>ROOT_NAME</i> &lt;out-var&gt;)
 cmake_path(<i>GET</i> &lt;path-var&gt; <i>ROOT_DIRECTORY</i> &lt;out-var&gt;)
 cmake_path(<i>GET</i> &lt;path-var&gt; <i>ROOT_PATH</i> &lt;out-var&gt;)
 cmake_path(<i>GET</i> &lt;path-var&gt; <i>FILENAME</i> &lt;out-var&gt;)
 cmake_path(<i>GET</i> &lt;path-var&gt; <i>EXTENSION</i> [LAST_ONLY] &lt;out-var&gt;)
 cmake_path(<i>GET</i> &lt;path-var&gt; <i>STEM</i> [LAST_ONLY] &lt;out-var&gt;)
 cmake_path(<i>GET</i> &lt;path-var&gt; <i>RELATIVE_PART</i> &lt;out-var&gt;)
 cmake_path(<i>GET</i> &lt;path-var&gt; <i>PARENT_PATH</i> &lt;out-var&gt;)
<i>Query</i>
 cmake_path(<i>HAS_ROOT_NAME</i> &lt;path-var&gt; &lt;out-var&gt;)
 cmake_path(<i>HAS_ROOT_DIRECTORY</i> &lt;path-var&gt; &lt;out-var&gt;)
 cmake_path(<i>HAS_ROOT_PATH</i> &lt;path-var&gt; &lt;out-var&gt;)
 cmake_path(<i>HAS_FILENAME</i> &lt;path-var&gt; &lt;out-var&gt;)
 cmake_path(<i>HAS_EXTENSION</i> &lt;path-var&gt; &lt;out-var&gt;)
 cmake_path(<i>HAS_STEM</i> &lt;path-var&gt; &lt;out-var&gt;)
 cmake_path(<i>HAS_RELATIVE_PART</i> &lt;path-var&gt; &lt;out-var&gt;)
 cmake_path(<i>HAS_PARENT_PATH</i> &lt;path-var&gt; &lt;out-var&gt;)
 cmake_path(<i>IS_ABSOLUTE</i> &lt;path-var&gt; &lt;out-var&gt;)
 cmake_path(<i>IS_RELATIVE</i> &lt;path-var&gt; &lt;out-var&gt;)
 cmake_path(<i>IS_PREFIX</i> &lt;path-var&gt; &lt;input&gt; [NORMALIZE] &lt;out-var&gt;)
 cmake_path(<i>COMPARE</i> &lt;input1&gt; &lt;OP&gt; &lt;input2&gt; &lt;out-var&gt;)
<i>Modification</i>
 cmake_path(<i>SET</i> &lt;path-var&gt; [NORMALIZE] &lt;input&gt;)
 cmake_path(<i>APPEND</i> &lt;path-var&gt; [&lt;input&gt;...] [OUTPUT_VARIABLE &lt;out-var&gt;])
 cmake_path(<i>APPEND_STRING</i> &lt;path-var&gt; [&lt;input&gt;...] [OUTPUT_VARIABLE &lt;out-var&gt;])
 cmake_path(<i>REMOVE_FILENAME</i> &lt;path-var&gt; [OUTPUT_VARIABLE &lt;out-var&gt;])
 cmake_path(<i>REPLACE_FILENAME</i> &lt;path-var&gt; &lt;input&gt; [OUTPUT_VARIABLE &lt;out-var&gt;])
 cmake_path(<i>REMOVE_EXTENSION</i> &lt;path-var&gt; [LAST_ONLY] [OUTPUT_VARIABLE &lt;out-var&gt;])
 cmake_path(<i>REPLACE_EXTENSION</i> &lt;path-var&gt; [LAST_ONLY] &lt;input&gt; [OUTPUT_VARIABLE &lt;out-var&gt;])
<i>Generation</i>
 cmake_path(<i>NORMAL_PATH</i> &lt;path-var&gt; [OUTPUT_VARIABLE &lt;out-var&gt;])
 cmake_path(<i>RELATIVE_PATH</i> &lt;path-var&gt; [BASE_DIRECTORY &lt;input&gt;] [OUTPUT_VARIABLE &lt;out-var&gt;])
 cmake_path(<i>ABSOLUTE_PATH</i> &lt;path-var&gt; [BASE_DIRECTORY &lt;input&gt;] [NORMALIZE] [OUTPUT_VARIABLE &lt;out-var&gt;])
<i>Native Conversion</i>
 cmake_path(<i>NATIVE_PATH</i> &lt;path-var&gt; [NORMALIZE] &lt;out-var&gt;)
 cmake_path(<i>CONVERT</i> &lt;input&gt; <i>TO_CMAKE_PATH_LIST</i> &lt;out-var&gt; [NORMALIZE])
 cmake_path(<i>CONVERT</i> &lt;input&gt; <i>TO_NATIVE_PATH_LIST</i> &lt;out-var&gt; [NORMALIZE])
<i>Hashing</i>
 cmake_path(<i>HASH</i> &lt;path-var&gt; &lt;out-var&gt;)</pre>
<h3>Conventions</h3>
<p>The following conventions are used in this command&#8217;s documentation:</p>
<dl>
<dt><code>&lt;path-var&gt;</code></p>
<dd>Always the name of a variable. For commands that expect a <code>&lt;path-var&gt;</code> as input, the variable must exist and it is expected to hold a single path.</p>
<dt><code>&lt;input&gt;</code></p>
<dd>A string literal which may contain a path, path fragment, or multiple paths with a special separator depending on the command. See the description of each command to see how this is interpreted.</p>
<dt><code>&lt;input&gt;&#8230;</code></p>
<dd>Zero or more string literal arguments.</p>
<dt><code>&lt;out-var&gt;</code></p>
<dd>The name of a variable into which the result of a command will be written.</dl>
<h3>Path Structure And Terminology</h3>
<p>A path has the following structure (all components are optional, with some constraints): </p>
<pre>root-name root-directory-separator (item-name directory-separator)* filename</pre>
<dl>
<dt><code>root-name</code></p>
<dd>Identifies the root on a filesystem with multiple roots (such as <code>&quot;C:&quot;</code> or <code>&quot;//myserver&quot;</code>). It is optional.</p>
<dt><code>root-directory-separator</code></p>
<dd>A directory separator that, if present, indicates that this path is absolute. If it is missing and the first element other than the <code>root-name</code> is an <code>item-name</code>, then the path is relative.</p>
<dt><code>item-name</code></p>
<dd>A sequence of characters that aren&#8217;t directory separators. This name may identify a file, a hard link, a symbolic link, or a directory. Two special cases are recognized:</p>
<dt>&bull;</p>
<dd>The item name consisting of a single dot character <code>.</code> is a directory name that refers to the current directory.</p>
<dt>&bull;</p>
<dd>The item name consisting of two dot characters <code>..</code> is a directory name that refers to the parent directory. </p>
<p> The <code>(&#8230;)*</code> pattern shown above is to indicate that there can be zero or more item names, with multiple items separated by a <code>directory-separator</code>. The <code>()*</code> characters are not part of the path.</p>
<dt><code>directory-separator</code></p>
<dd>The only recognized directory separator is a forward slash character <code>/</code>. If this character is repeated, it is treated as a single directory separator. In other words, <code>/usr///////lib</code> is the same as <code>/usr/lib</code>.</p>
<dt><code>filename</code></p>
<dd>A path has a <code>filename</code> if it does not end with a <code>directory-separator</code>. The <code>filename</code> is effectively the last <code>item-name</code> of the path, so it can also be a hard link, symbolic link or a directory. </p>
<p> A <code>filename</code> can have an <i>extension</i>. By default, the extension is defined as the sub-string beginning at the left-most period (including the period) and until the end of the <code>filename</code>. In commands that accept a <code>LAST_ONLY</code> keyword, <code>LAST_ONLY</code> changes the interpretation to the sub-string beginning at the right-most period. </p>
<p> The following exceptions apply to the above interpretation:</p>
<dt>&bull;</p>
<dd>If the first character in the <code>filename</code> is a period, that period is ignored (i.e. a <code>filename</code> like <code>&quot;.profile&quot;</code> is treated as having no extension).</p>
<dt>&bull;</p>
<dd>If the <code>filename</code> is either <code>.</code> or <code>..</code>, it has no extension. </p>
<p> The <i>stem</i> is the part of the <code>filename</code> before the extension. </p>
<p> Some commands refer to a <code>root-path</code>. This is the concatenation of <code>root-name</code> and <code>root-directory-separator</code>, either or both of which can be empty. A <code>relative-part</code> refers to the full path with any <code>root-path</code> removed.</dl>
<h3>Creating A Path Variable</h3>
<p>While a path can be created with care using an ordinary <code>set()</code> command, it is recommended to use <i>cmake_path(SET)</i> instead, as it automatically converts the path to the required form where required. The cmake_path(APPEND) subcommand may be another suitable alternative where a path needs to be constructed by joining fragments. The following example compares the three methods for constructing the same path: </p>
<pre>set(path1 &quot;${CMAKE_CURRENT_SOURCE_DIR}/data&quot;)
cmake_path(SET path2 &quot;${CMAKE_CURRENT_SOURCE_DIR}/data&quot;)
cmake_path(APPEND path3 &quot;${CMAKE_CURRENT_SOURCE_DIR}&quot; &quot;data&quot;)</pre>
<p><i>Modification</i> and <i>Generation</i> sub-commands can either store the result in-place, or in a separate variable named after an <code>OUTPUT_VARIABLE</code> keyword. All other sub-commands store the result in a mandatory <code>&lt;out-var&gt;</code> variable.</p>
<h3>Normalization</h3>
<p>Some sub-commands support <i>normalizing</i> a path. The algorithm used to normalize a path is as follows:</p>
<dl>
<dt>1.</p>
<dd>If the path is empty, stop (the normalized form of an empty path is also an empty path).</p>
<dt>2.</p>
<dd>Replace each <code>directory-separator</code>, which may consist of multiple separators, with a single <code>/</code> (<code>/a///b &#8211;&gt; /a/b</code>).</p>
<dt>3.</p>
<dd>Remove each solitary period (<code>.</code>) and any immediately following <code>directory-separator</code> (<code>/a/./b/. &#8211;&gt; /a/b</code>).</p>
<dt>4.</p>
<dd>Remove each <code>item-name</code> (other than <code>..</code>) that is immediately followed by a <code>directory-separator</code> and a <code>..</code>, along with any immediately following <code>directory-separator</code> (<code>/a/b/../c &#8211;&gt; a/c</code>).</p>
<dt>5.</p>
<dd>If there is a <code>root-directory</code>, remove any <code>..</code> and any <code>directory-separators</code> immediately following them. The parent of the root directory is treated as still the root directory (<code>/../a &#8211;&gt; /a</code>).</p>
<dt>6.</p>
<dd>If the last <code>item-name</code> is <code>..</code>, remove any trailing <code>directory-separator</code> (<code>../ &#8211;&gt; ..</code>).</p>
<dt>7.</p>
<dd>If the path is empty by this stage, add a <code>dot</code> (normal form of <code>./</code> is <code>.</code>).</dl>
<h3>Decomposition</h3>
<p>The following forms of the <code>GET</code> subcommand each retrieve a different component or group of components from a path. See <i>Path Structure And Terminology</i> for the meaning of each path component. </p>
<pre>cmake_path(GET &lt;path-var&gt; ROOT_NAME &lt;out-var&gt;)
cmake_path(GET &lt;path-var&gt; ROOT_DIRECTORY &lt;out-var&gt;)
cmake_path(GET &lt;path-var&gt; ROOT_PATH &lt;out-var&gt;)
cmake_path(GET &lt;path-var&gt; FILENAME &lt;out-var&gt;)
cmake_path(GET &lt;path-var&gt; EXTENSION [LAST_ONLY] &lt;out-var&gt;)
cmake_path(GET &lt;path-var&gt; STEM [LAST_ONLY] &lt;out-var&gt;)
cmake_path(GET &lt;path-var&gt; RELATIVE_PART &lt;out-var&gt;)
cmake_path(GET &lt;path-var&gt; PARENT_PATH &lt;out-var&gt;)</pre>
<p>If a requested component is not present in the path, an empty string will be stored in <code>&lt;out-var&gt;</code>. For example, only Windows systems have the concept of a <code>root-name</code>, so when the host machine is non-Windows, the <code>ROOT_NAME</code> subcommand will always return an empty string. </p>
<p> For <code>PARENT_PATH</code>, if the <i>HAS_RELATIVE_PART</i> subcommand returns false, the result is a copy of <code>&lt;path-var&gt;</code>. Note that this implies that a root directory is considered to have a parent, with that parent being itself. Where <i>HAS_RELATIVE_PART</i> returns true, the result will essentially be <code>&lt;path-var&gt;</code> with one less element.</p>
<h3>Root examples</h3>
<pre>set(path &quot;c:/a&quot;)
cmake_path(GET path ROOT_NAME rootName)
cmake_path(GET path ROOT_DIRECTORY rootDir)
cmake_path(GET path ROOT_PATH rootPath)
message(&quot;Root name is \&quot;${rootName}\&quot;&quot;)
message(&quot;Root directory is \&quot;${rootDir}\&quot;&quot;)
message(&quot;Root path is \&quot;${rootPath}\&quot;&quot;)</pre>
<pre>Root name is &quot;c:&quot;
Root directory is &quot;/&quot;
Root path is &quot;c:/&quot;</pre>
<h3>Filename examples</h3>
<pre>set(path &quot;/a/b&quot;)
cmake_path(GET path FILENAME filename)
message(&quot;First filename is \&quot;${filename}\&quot;&quot;)
# Trailing slash means filename is empty
set(path &quot;/a/b/&quot;)
cmake_path(GET path FILENAME filename)
message(&quot;Second filename is \&quot;${filename}\&quot;&quot;)</pre>
<pre>First filename is &quot;b&quot;
Second filename is &quot;&quot;</pre>
<h3>Extension and stem examples</h3>
<pre>set(path &quot;name.ext1.ext2&quot;)
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
message(&quot;.some.more stem is \&quot;${someMoreStem}\&quot;&quot;)</pre>
<pre>Full extension is &quot;.ext1.ext2&quot;
Full stem is &quot;name&quot;
Last extension is &quot;.ext2&quot;
Last stem is &quot;name.ext1&quot;
Dot extension is &quot;&quot;
Dot stem is &quot;.&quot;
Dot-dot extension is &quot;&quot;
Dot-dot stem is &quot;..&quot;
.some.more extension is &quot;.more&quot;
.some.more stem is &quot;.some&quot;</pre>
<h3>Relative part examples</h3>
<pre>set(path &quot;c:/a/b&quot;)
cmake_path(GET path RELATIVE_PART result)
message(&quot;Relative part is \&quot;${result}\&quot;&quot;)
set(path &quot;c/d&quot;)
cmake_path(GET path RELATIVE_PART result)
message(&quot;Relative part is \&quot;${result}\&quot;&quot;)
set(path &quot;/&quot;)
cmake_path(GET path RELATIVE_PART result)
message(&quot;Relative part is \&quot;${result}\&quot;&quot;)</pre>
<pre>Relative part is &quot;a/b&quot;
Relative part is &quot;c/d&quot;
Relative part is &quot;&quot;</pre>
<h3>Path traversal examples</h3>
<pre>set(path &quot;c:/a/b&quot;)
cmake_path(GET path PARENT_PATH result)
message(&quot;Parent path is \&quot;${result}\&quot;&quot;)
set(path &quot;c:/&quot;)
cmake_path(GET path PARENT_PATH result)
message(&quot;Parent path is \&quot;${result}\&quot;&quot;)</pre>
<pre>Parent path is &quot;c:/a&quot;
Parent path is &quot;c:/&quot;</pre>
<h3>Query</h3>
<p>Each of the <code>GET</code> subcommands has a corresponding <code>HAS_&#8230;</code> subcommand which can be used to discover whether a particular path component is present. See <i>Path Structure And Terminology</i> for the meaning of each path component. </p>
<pre>cmake_path(HAS_ROOT_NAME &lt;path-var&gt; &lt;out-var&gt;)
cmake_path(HAS_ROOT_DIRECTORY &lt;path-var&gt; &lt;out-var&gt;)
cmake_path(HAS_ROOT_PATH &lt;path-var&gt; &lt;out-var&gt;)
cmake_path(HAS_FILENAME &lt;path-var&gt; &lt;out-var&gt;)
cmake_path(HAS_EXTENSION &lt;path-var&gt; &lt;out-var&gt;)
cmake_path(HAS_STEM &lt;path-var&gt; &lt;out-var&gt;)
cmake_path(HAS_RELATIVE_PART &lt;path-var&gt; &lt;out-var&gt;)
cmake_path(HAS_PARENT_PATH &lt;path-var&gt; &lt;out-var&gt;)</pre>
<p>Each of the above follows the predictable pattern of setting <code>&lt;out-var&gt;</code> to true if the path has the associated component, or false otherwise. Note the following special cases:</p>
<dl>
<dt>&bull;</p>
<dd>For <code>HAS_ROOT_PATH</code>, a true result will only be returned if at least one of <code>root-name</code> or <code>root-directory</code> is non-empty.</p>
<dt>&bull;</p>
<dd>For <code>HAS_PARENT_PATH</code>, the root directory is also considered to have a parent, which will be itself. The result is true except if the path consists of just a <i>filename</i>. </p>
<pre>cmake_path(IS_ABSOLUTE &lt;path-var&gt; &lt;out-var&gt;)</pre>
<p>Sets <code>&lt;out-var&gt;</code> to true if <code>&lt;path-var&gt;</code> is absolute. An absolute path is a path that unambiguously identifies the location of a file without reference to an additional starting location. On Windows, this means the path must have both a <code>root-name</code> and a <code>root-directory-separator</code> to be considered absolute. On other platforms, just a <code>root-directory-separator</code> is sufficient. Note that this means on Windows, <code>IS_ABSOLUTE</code> can be false while <code>HAS_ROOT_DIRECTORY</code> can be true. </p>
<pre>cmake_path(IS_RELATIVE &lt;path-var&gt; &lt;out-var&gt;)</pre>
<p>This will store the opposite of <code>IS_ABSOLUTE</code> in <code>&lt;out-var&gt;</code>. </p>
<pre>cmake_path(IS_PREFIX &lt;path-var&gt; &lt;input&gt; [NORMALIZE] &lt;out-var&gt;)</pre>
<p>Checks if <code>&lt;path-var&gt;</code> is the prefix of <code>&lt;input&gt;</code>. </p>
<p> When the <code>NORMALIZE</code> option is specified, <code>&lt;path-var&gt;</code> and <code>&lt;input&gt;</code> are <i>normalized</i> before the check. </p>
<pre>set(path &quot;/a/b/c&quot;)
cmake_path(IS_PREFIX path &quot;/a/b/c/d&quot; result) # result = true
cmake_path(IS_PREFIX path &quot;/a/b&quot; result) # result = false
cmake_path(IS_PREFIX path &quot;/x/y/z&quot; result) # result = false
set(path &quot;/a/b&quot;)
cmake_path(IS_PREFIX path &quot;/a/c/../b&quot; NORMALIZE result) # result = true</pre>
<pre>cmake_path(COMPARE &lt;input1&gt; EQUAL &lt;input2&gt; &lt;out-var&gt;)
cmake_path(COMPARE &lt;input1&gt; NOT_EQUAL &lt;input2&gt; &lt;out-var&gt;)</pre>
<p>Compares the lexical representations of two paths provided as string literals. No normalization is performed on either path. Equality is determined according to the following pseudo-code logic: </p>
<pre>if(NOT &lt;input1&gt;.root_name() STREQUAL &lt;input2&gt;.root_name())
 return FALSE
if(&lt;input1&gt;.has_root_directory() XOR &lt;input2&gt;.has_root_directory())
 return FALSE
Return FALSE if a relative portion of &lt;input1&gt; is not lexicographically
equal to the relative portion of &lt;input2&gt;. This comparison is performed path
component-wise. If all of the components compare equal, then return TRUE.</pre>
<p><code>NOTE:</code> Unlike most other <code>cmake_path()</code> subcommands, the <code>COMPARE</code> subcommand takes literal strings as input, not the names of variables.</dl>
<h3>Modification</h3>
<pre>cmake_path(SET &lt;path-var&gt; [NORMALIZE] &lt;input&gt;)</pre>
<p>Assign the <code>&lt;input&gt;</code> path to <code>&lt;path-var&gt;</code>. If <code>&lt;input&gt;</code> is a native path, it is converted into a cmake-style path with forward-slashes (<code>/</code>). On Windows, the long filename marker is taken into account. </p>
<p> When the <code>NORMALIZE</code> option is specified, the path is <i>normalized</i> before the conversion. </p>
<p> For example: </p>
<pre>set(native_path &quot;c:\a\b/..\c&quot;)
cmake_path(SET path &quot;${native_path}&quot;)
message(&quot;CMake path is \&quot;${path}\&quot;&quot;)
cmake_path(SET path NORMALIZE &quot;${native_path}&quot;)
message(&quot;Normalized CMake path is \&quot;${path}\&quot;&quot;)</pre>
<p>Output: </p>
<pre>CMake path is &quot;c:/a/b/../c&quot;
Normalized CMake path is &quot;c:/a/c&quot;</pre>
<pre>cmake_path(APPEND &lt;path-var&gt; [&lt;input&gt;...] [OUTPUT_VARIABLE &lt;out-var&gt;])</pre>
<p>Append all the <code>&lt;input&gt;</code> arguments to the <code>&lt;path-var&gt;</code> using <code>/</code> as the <code>directory-separator</code>. Depending on the <code>&lt;input&gt;</code>, the previous contents of <code>&lt;path-var&gt;</code> may be discarded. For each <code>&lt;input&gt;</code> argument, the following algorithm (pseudo-code) applies: </p>
<pre># &lt;path&gt; is the contents of &lt;path-var&gt;
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
append &lt;input&gt; omitting any root-name to &lt;path&gt;</pre>
<pre>cmake_path(APPEND_STRING &lt;path-var&gt; [&lt;input&gt;...] [OUTPUT_VARIABLE &lt;out-var&gt;])</pre>
<p>Append all the <code>&lt;input&gt;</code> arguments to the <code>&lt;path-var&gt;</code> without adding any <code>directory-separator</code>. </p>
<pre>cmake_path(REMOVE_FILENAME &lt;path-var&gt; [OUTPUT_VARIABLE &lt;out-var&gt;])</pre>
<p>Removes the <i>filename</i> component (as returned by <i>GET &#8230; FILENAME</i>) from <code>&lt;path-var&gt;</code>. After removal, any trailing <code>directory-separator</code> is left alone, if present. </p>
<p> If <code>OUTPUT_VARIABLE</code> is not given, then after this function returns, <i>HAS_FILENAME</i> returns false for <code>&lt;path-var&gt;</code>. </p>
<p> For example: </p>
<pre>set(path &quot;/a/b&quot;)
cmake_path(REMOVE_FILENAME path)
message(&quot;First path is \&quot;${path}\&quot;&quot;)
# filename is now already empty, the following removes nothing
cmake_path(REMOVE_FILENAME path)
message(&quot;Second path is \&quot;${result}\&quot;&quot;)</pre>
<p>Output: </p>
<pre>First path is &quot;/a/&quot;
Second path is &quot;/a/&quot;</pre>
<pre>cmake_path(REPLACE_FILENAME &lt;path-var&gt; &lt;input&gt; [OUTPUT_VARIABLE &lt;out-var&gt;])</pre>
<p>Replaces the <i>filename</i> component from <code>&lt;path-var&gt;</code> with <code>&lt;input&gt;</code>. If <code>&lt;path-var&gt;</code> has no filename component (i.e. <i>HAS_FILENAME</i> returns false), the path is unchanged. The operation is equivalent to the following: </p>
<pre>cmake_path(HAS_FILENAME path has_filename)
if(has_filename)
 cmake_path(REMOVE_FILENAME path)
 cmake_path(APPEND path input);
endif()</pre>
<pre>cmake_path(REMOVE_EXTENSION &lt;path-var&gt; [LAST_ONLY]
 [OUTPUT_VARIABLE &lt;out-var&gt;])</pre>
<p>Removes the <i>extension</i>, if any, from <code>&lt;path-var&gt;</code>. </p>
<pre>cmake_path(REPLACE_EXTENSION &lt;path-var&gt; [LAST_ONLY] &lt;input&gt;
 [OUTPUT_VARIABLE &lt;out-var&gt;])</pre>
<p>Replaces the <i>extension</i> with <code>&lt;input&gt;</code>. Its effect is equivalent to the following: </p>
<pre>cmake_path(REMOVE_EXTENSION path)
if(NOT &quot;input&quot; MATCHES &quot;^\.&quot;)
 cmake_path(APPEND_STRING path &quot;.&quot;)
endif()
cmake_path(APPEND_STRING path &quot;input&quot;)</pre>
<h3>Generation</h3>
<pre>cmake_path(NORMAL_PATH &lt;path-var&gt; [OUTPUT_VARIABLE &lt;out-var&gt;])</pre>
<p>Normalize <code>&lt;path-var&gt;</code> according the steps described in <i>Normalization</i>. </p>
<pre>cmake_path(RELATIVE_PATH &lt;path-var&gt; [BASE_DIRECTORY &lt;input&gt;]
 [OUTPUT_VARIABLE &lt;out-var&gt;])</pre>
<p>Modifies <code>&lt;path-var&gt;</code> to make it relative to the <code>BASE_DIRECTORY</code> argument. If <code>BASE_DIRECTORY</code> is not specified, the default base directory will be <code>CMAKE_CURRENT_SOURCE_DIR</code>. </p>
<p> For reference, the algorithm used to compute the relative path is the same as that used by C++ <i>std::filesystem::path::lexically_relative</i>. </p>
<pre>cmake_path(ABSOLUTE_PATH &lt;path-var&gt; [BASE_DIRECTORY &lt;input&gt;] [NORMALIZE]
 [OUTPUT_VARIABLE &lt;out-var&gt;])</pre>
<p>If <code>&lt;path-var&gt;</code> is a relative path (<i>IS_RELATIVE</i> is true), it is evaluated relative to the given base directory specified by <code>BASE_DIRECTORY</code> option. If <code>BASE_DIRECTORY</code> is not specified, the default base directory will be <code>CMAKE_CURRENT_SOURCE_DIR</code>. </p>
<p> When the <code>NORMALIZE</code> option is specified, the path is <i>normalized</i> after the path computation. </p>
<p> Because <code>cmake_path()</code> does not access the filesystem, symbolic links are not resolved and any leading tilde is not expanded. To compute a real path with symbolic links resolved and leading tildes expanded, use the <code>file(REAL_PATH)</code> command instead.</p>
<h3>Native Conversion</h3>
<p>For commands in this section, <i>native</i> refers to the host platform, not the target platform when cross-compiling. </p>
<pre>cmake_path(NATIVE_PATH &lt;path-var&gt; [NORMALIZE] &lt;out-var&gt;)</pre>
<p>Converts a cmake-style <code>&lt;path-var&gt;</code> into a native path with platform-specific slashes (<code>\</code> on Windows hosts and <code>/</code> elsewhere). </p>
<p> When the <code>NORMALIZE</code> option is specified, the path is <i>normalized</i> before the conversion. </p>
<pre>cmake_path(CONVERT &lt;input&gt; TO_CMAKE_PATH_LIST &lt;out-var&gt; [NORMALIZE])</pre>
<p>Converts a native <code>&lt;input&gt;</code> path into a cmake-style path with forward slashes (<code>/</code>). On Windows hosts, the long filename marker is taken into account. The input can be a single path or a system search path like <code>$ENV{PATH}</code>. A search path will be converted to a cmake-style list separated by <code>;</code> characters (on non-Windows platforms, this essentially means <code>:</code> separators are replaced with <code>;</code>). The result of the conversion is stored in the <code>&lt;out-var&gt;</code> variable. </p>
<p> When the <code>NORMALIZE</code> option is specified, the path is <i>normalized</i> before the conversion. </p>
<p> <code>NOTE:</code> Unlike most other <code>cmake_path()</code> subcommands, the <code>CONVERT</code> subcommand takes a literal string as input, not the name of a variable. </p>
<pre>cmake_path(CONVERT &lt;input&gt; TO_NATIVE_PATH_LIST &lt;out-var&gt; [NORMALIZE])</pre>
<p>Converts a cmake-style <code>&lt;input&gt;</code> path into a native path with platform-specific slashes (<code>\</code> on Windows hosts and <code>/</code> elsewhere). The input can be a single path or a cmake-style list. A list will be converted into a native search path (<code>;</code>-separated on Windows, <code>:</code>-separated on other platforms). The result of the conversion is stored in the <code>&lt;out-var&gt;</code> variable. </p>
<p> When the <code>NORMALIZE</code> option is specified, the path is <i>normalized</i> before the conversion. </p>
<p> <code>NOTE:</code> Unlike most other <code>cmake_path()</code> subcommands, the <code>CONVERT</code> subcommand takes a literal string as input, not the name of a variable. </p>
<p> For example: </p>
<pre>set(paths &quot;/a/b/c&quot; &quot;/x/y/z&quot;)
cmake_path(CONVERT &quot;${paths}&quot; TO_NATIVE_PATH_LIST native_paths)
message(&quot;Native path list is \&quot;${native_paths}\&quot;&quot;)</pre>
<p>Output on Windows: </p>
<pre>Native path list is &quot;
