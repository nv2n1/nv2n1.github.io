---
title: "include_server(1)"
name: "include_server"
section: "1"
letter: "i"
url: "/docs/linux/man/1-include_server/"
description: "include_server.py – conservative approximation of include dependencies for C/C++"
---

<h2>NAME</h2>
<p> include_server.py &#8211; conservative approximation of include dependencies for C/C++</p>
<h2>SYNOPSIS</h2>
<p> <code>include_server</code> &#8211;port <i>INCLUDE_SERVER_PORT [OPTIONS]</i></p>
<h2>DESCRIPTION</h2>
<p> include_server.py starts an include server process. This process answers queries from <code><a href="/docs/linux/man/1-distcc/">distcc</a></code>(1) clients about what files to include in C/C++ compilations. The include_server.py command itself terminates as soon as the include server has been spawned. </p>
<p> The INCLUDE_SERVER_PORT argument is the name of a socket used for all communication between distcc clients and the include server. The <code><a href="/docs/linux/man/1-pump/">pump</a></code>(1) command is responsible for creating the socket location, for passing it to this script, and for passing it to all distcc clients via the environment variable named INCLUDE_SERVER_PORT. </p>
<p> The protocol used by the include server uses distcc&#8217;s RPC implementation. Each distcc request consists of (1) the current directory and (2) the list of arguments of the compilation command. </p>
<p> If the include server is able to process the request, then it answers the distcc client by sending a list of filepaths. The filepaths are those of the compressed source and header files found to be necessary for compilation through include analysis. The list also comprises symbolic links and even dummy files needed for the compilation server to construct an accurate replica of the parts of the filesystem needed for compilation. In this way, a needed header file like /path/foo.h is compressed, renamed, and stored in a temporary location, such as /dev/shm/tmpiAvfGv.include_server-9368-1/path/foo.h.lzo. The distcc client will pass these files on to a compilation server, where they will be uncompressed and mounted temporarily. </p>
<p> If the include server is not able to process the request, then it returns the empty list to the distcc client. </p>
<p> There are two kinds of failures that relate to the include server. The include server may fail to compute the includes or fail in other ways, see section <code>INCLUDE SERVER SYMPTOMS</code>. Also, the compilation on the remove server may fail due to inadequacy of the calculated include closure, but then succeed when locally retried, see section <code>DISTCC DISCREPANCY SYMPTOMS</code>. </p>
<h2>OPTION SUMMARY</h2>
<p> The following options are understood by include_server.py.</p>
<dl>
<dt><code>-dPAT, &#8211;debug_pattern=PAT </code></p>
<dd> Bit vector for turning on warnings and debugging<br />
&nbsp;<wbr>1&nbsp;<wbr>=&nbsp;<wbr>warnings<br />
&nbsp;<wbr>2&nbsp;<wbr>=&nbsp;<wbr>trace some functions<br />
&nbsp;<wbr>other powers of two: see include_server/basics.py.</p>
<dt><code>-e, &#8211;email</code></p>
<dd> Send email to &#8216;distcc-pump-errors&#8217; or if defined, the value of enviroment variable DISTCC_EMAILLOG_WHOM_TO_BLAME, when include server gets in trouble. The default is to not send email.</p>
<dt><code>&#8211;email_bound NUMBER</code></p>
<dd> Maximal number of emails to send (in addition to a final email). Default: 3.</p>
<dt><code>&#8211;no-email</code></p>
<dd> Do not send email. This is the default.</p>
<dt><code>&#8211;path_observation_re=RE </code></p>
<dd> Issue warning message whenever a filename is resolved to a realpath that is matched by RE, which is a regular expression in Python syntax. This is useful for finding out where files included actually come from. Use RE=&quot;&quot; to find them all. Note: warnings must be enabled with at least -d1.</p>
<dt><code>&#8211;pid_file FILEPATH</code></p>
<dd> The pid of the include server is written to file FILEPATH. This allows a script such a <code>pump</code> to tear down the include server.</p>
<dt><code>-s, &#8211;statistics</code></p>
<dd> Print information to stdout about include analysis.</p>
<dt><code>&#8211;stat_reset_triggers=LIST </code></p>
<dd> Flush stat caches when the timestamp of any filepath in LIST changes or the filepath comes in or out of existence. LIST is a colon separated string of filepaths, possibly containing simple globs (as allowed by Python&#8217;s glob module). Print a warning whenever such a change happens (if warnings are enabled). This option allows limited exceptions to distcc_pump&#8217;s normal assumption that source files are not modified during the build.</p>
<dt><code>-t, &#8211;time </code></p>
<dd> Print elapsed, user, and system time to stderr.</p>
<dt><code>&#8211;unsafe_absolute_includes </code></p>
<dd> Do preprocessing on the compilation server even if includes of absolute filepaths are encountered. Normally the include-server will fall back on local preprocessing if it detects any absolute includes. Thus, this flag is useful for preventing such fallbacks when the absolute includes are a false alarm, either because the absolute include is discarded during preprocessing or because the absolutely included file exists on the compilation servers.</p>
<dt>
<dd> More precisely, with &#8211;unsafe_absolute_includes absolute includes are ignored for the purposes of gathering the include closure. Using this option may lead to incorrect results because (1) the header may actually be included on the compilation server and it may not be the same as on the client, (2) the include directives of the header are not further analyzed.</p>
<dt>
<dd> The option is useful for compiling code that has such hardcoded absolute locations of header files inside conditional directives (e.g. &quot;#ifdef&quot;) that render the includes irrelevant. More precisely, these includes must be eliminated during preprocessing for the actual configuration. Then the question of existence of the header file is moot and the remote compilation is sound. This is often the case if such includes are meant for unusual configurations different from the actual configuration.</p>
<dt><code>-v, &#8211;verify</code></p>
<dd> Verify that files in CPP closure are contained in closure calculated by include processor.</p>
<dt><code>-w, &#8211;write_include_closure </code></p>
<dd> Write a .d_approx file which lists all the included files calculated by the include server; with -x, additionally write the included files as calculated by CPP to a .d_exact file.</p>
<dt><code>-x, &#8211;exact_analysis</code></p>
<dd> Use CPP instead, do not omit system headers files. </p>
</dl>
<h2>INCLUDE SERVER SYMPTOMS AND ISSUES</h2>
<p> The most likely messages and warnings to come from the include processor are listed below. </p>
<dl>
<dt><code>Preprocessing locally. Include server not covering: Couldn&#8217;t determine default system include directories</code></p>
<dd> To determine the default system header directories, the include server runs the compiler once for each language needed during its session. This message indicates that the compiler specified to distcc is not present on the client.</dl>
<dl>
<dt><code>Preprocessing locally. Include server not covering: Bailing out because include server spent more than &#8230;s user time handling request</code></p>
<dd> In uncommon situations, the include server fails to analyze very complicated macro expressions. The distcc client will use plain distcc mode.</dl>
<dl>
<dt><code>Warning: Filepath must be relative but isn&#8217;t</code></p>
<dd> The include server does not accept absolute filepaths, such as /usr/include/stdio.h, in include directives, because there is no guarantee that this header on the compilation server machine will be the same as that on the client. The include server gives up analyzing the include closure. The distcc client cannot use pump-mode.</p>
<dt>
<dd> To overcome this problem in a not always reliable way, set the environment variable INCLUDE_SERVER_ARGS=&#8217;&#8211;unsafe_absolute_includes&#8217; when invoking the pump script to pass the &#8211;unsafe_absolute_includes option to the include server.</dl>
<dl>
<dt><code>Warning: Absolute filepath &#8230; was IGNORED</code></p>
<dd> The &#8211;unsafe_absolute_includes is in use. This situation happens under the same circumstances as when &quot;Filepath must be relative but isn&#8217;t&quot; is issued, but in this case the include will provide an answer to the distcc client.</dl>
<dl>
<dt><code>Warning: Path &#8216;/PATH/FILE&#8217; changed/came into existence/no longer exists</code></p>
<dd> These warnings are issued when using stat reset triggers. Because /PATH/FILE changed, the include server clears its caches; the new version of the file (or the lack of it) renders the include analysis invalid. This message can usually be ignored; it does signify a somewhat precarious use of files by the build system. It is recommended to fix the build system so that files are not rewritten.</dl>
<dl>
<dt><code>Warning: For translation unit &#8230;, lookup of file &#8230; resolved to &#8230; whose realpath is &#8230;</code></p>
<dd> This warning occurs with &#8211;path_observation_re when a new realpath matching a source or header file is observed. </p>
</dl>
<h2>DISTCC DISCREPANCY SYMPTOMS</h2>
<p> The interactions between the build system, distcc, and the include server is somewhat complex. When a distcc commands receives a failing compilation from the remote server it retries the compilation locally. This section discusses the causes of discrepancies between remote and local compilation. These are flagged by the demotion message: </p>
<p> <code>__________Warning: &#8230; pump-mode compilation(s) failed on server,</code> <code>but succeeded locally.</code><br />
 <code>__________Distcc-pump was demoted to plain mode.</code> <code>See the Distcc Discrepancy Symptoms section in the <a href="/docs/linux/man/1-include_server/">include_server</a>(1) man</code> <code>page.</code> </p>
<p> The pump script issues this message at the end of the build. This means that for at least one distcc invocation a local compilation succeeded after the remote compilation failed. Each distcc invocation for which such a discrepancy occurred in turn also issues a message such as: </p>
<p> <code>Warning: remote compilation of &#8216;&#8230;&#8217; failed,</code> <code>retried locally and got a different result.</code> </p>
<p> The demotion makes subsequent distcc invocations use plain distcc mode. Thus preprocessing will take place on the local machine for the remainder of the build. This technique prevents very slow builds where all compilations end up on the local machine after failing remotely. </p>
<p> Of course, if the local compilations fails after the remote failures, then the distcc invocation exits with the non-zero status of the local compilation. The error messages printed are also those of the local compilation. </p>
<p> The fallback behavior for distcc-pump mode to local compilation can be disabled by setting the environment variable DISTCC_FALLBACK to 0, which makes the distcc command fail as soon as the remote compilation has failed. This setting is very useful for debugging why the remote compilation went wrong, because now the output from the server will be printed. </p>
<p> Next we discuss the possible causes of discrepancies. </p>
<dl>
<dt><code>The user changed a source or header file during the build.</code></p>
<dd> This yields inconsistent results of course.</dl>
<dl>
<dt><code>A source or header file changed during the build.</code></p>
<dd> The build system rewrites a file. For Linux kernel 2.6, this happens for &#8216;include/linux/compile.h&#8217; and &#8216;include/asm/asm-offsets.h&#8217;. This condition is fixed by letting the include server know that it must reset its caches when a stat of any of the files changes. Practically, this is done by gathering the files in a colon-separated list and then setting the INCLUDE_SERVER_ARGS environment variable when invoking the pump script, so that it passes the <code>&#8211;stat_reset_triggers</code> option; for example, </p>
<p>INCLUDE_SERVER_ARGS=&quot;&#8211;stat_reset_triggers=include/linux/compile.h:include/asm/asm-offsets.h&quot;</dl>
<dl>
<dt><code>A header file is potentially included, but does not exist, and is then later included.</code></p>
<dd> This occurs when some header foo.h includes another header file trick.h, but the trick.h file has not yet been generated and the inclusion is actually ignored because of preprocessing directives. The include server will probe for the existence of trick.h, because it overapproximates all possible ways directives actually evaluate. The file trick.h is determined not to exist. If it is later generated, and then really included, then the include server will falsely believe that the file still does not exist. The solution to this problem is to make the build system generate trick.h before the first time any header file is included that makes a syntactic reference to trick.h</dl>
<dl>
<dt><code>The include server was started with &#8211;unsafe_absolute_includes</code>.</p>
<dd> This is a problem if there are header files locally that do not exist remotely and that are actually used. Such includes are often protected by conditional directives that evaluate so that are actually used on only specific and often uncommon platforms. If you are not compiling for such a platform, then it may be correct to use <code>&#8211;unsafe_absolute_include</code>.</dl>
<dl>
<dt><code>The include server has calculated the wrong includes.</code></p>
<dd> We do not know of such a situation. </p>
</dl>
<h2>EXIT CODES</h2>
<p> The exit code of include_server.py is usually 0. That the include server has been started properly is communicated through the existence of the pid_file. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code>DISTCC_EMAILLOG_WHOM_TO_BLAME</code> The email address to use for include server automated emails. The default is &#8216;distcc-pump-errors&#8217; (which is an email address that probably will not exist in your domain). </p>
<p> Additionally, the invocation of the compiler may use additional environment variables. </p>
<h2>BUGS</h2>
<p> If you think you have found a distcc bug, please see the file <i>reporting-bugs.txt</i> in the documentation directory for information on how to report it. </p>
<p> In distcc-pump mode, the include server is unable to handle certain very complicated computed includes as found in parts of the Boost library. The include server will time out and distcc will revert to plain mode. </p>
<p> Other known bugs may be documented on <i><a rel="nofollow" href="http://code.google.com/p/distcc/">http://code.google.com/p/distcc/</a></i> </p>
<h2>AUTHOR</h2>
<p> The include server was written by Nils Klarlund, with assistance from Fergus Henderson, Manos Renieris, and Craig Silverstein. Please report bugs to &lt;distcc [at] lists.samba.org&gt;. </p>
<h2>LICENCE</h2>
<p> You are free to use distcc. distcc (including this manual) may be copied, modified or distributed only under the terms of the GNU General Public Licence version 2 or later. distcc comes with absolutely no warrany. A copy of the GPL is included in the file COPYING. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-distcc/">distcc</a></code>(1), <code><a href="/docs/linux/man/1-distccd/">distccd</a></code>(1), <code><a href="/docs/linux/man/1-include_server/">include_server</a></code>(1), and <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1). <a rel="nofollow" href="http://code.google.com/p/distcc/">http://code.google.com/p/distcc/</a> <a href="http://ccache.samba.org/">http://ccache.samba.org/</a> </p>
<h2>Index</h2>
