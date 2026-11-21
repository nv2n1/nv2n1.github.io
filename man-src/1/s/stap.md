---

title: "stap(1)"
name: "stap"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stap/"
description: "stap – systemtap script translator/driver"
---

<h2>NAME</h2>
<p> stap - systemtap script translator/driver </p>
<p> <br />
 <code>stap</code> [ <i>OPTIONS</i> ] <i>FILENAME</i> [ <i>ARGUMENTS</i> ] <br />
 <code>stap</code> [ <i>OPTIONS</i> ] <code>-</code> [ <i>ARGUMENTS</i> ] <br />
 <code>stap</code> [ <i>OPTIONS</i> ] <code>-e</code><i> SCRIPT</i> [ <i>ARGUMENTS</i> ] <br />
 <code>stap</code> [ <i>OPTIONS</i> ] <code>-l</code><i> PROBE</i> [ <i>ARGUMENTS</i> ] <br />
 <code>stap</code> [ <i>OPTIONS</i> ] <code>-L</code><i> PROBE</i> [ <i>ARGUMENTS</i> ] <br />
 <code>stap</code> [ <i>OPTIONS</i> ] <code>--dump-probe-types</code> <br />
 <code>stap</code> [ <i>OPTIONS</i> ] <code>--dump-probe-aliases</code> <br />
 <code>stap</code> [ <i>OPTIONS</i> ] <code>--dump-functions</code> </p>
<p> The <i>stap</i> program is the front-end to the Systemtap tool. It accepts probing instructions written in a simple domain-specific language, translates those instructions into C code, compiles this C code, and loads the resulting module into a running Linux kernel or a DynInst user-space mutator, to perform the requested system trace/probe functions. You can supply the script in a named file (FILENAME), from standard input (use - instead of FILENAME), or from the command line (using -e SCRIPT). The program runs until it is interrupted by the user, or if the script voluntarily invokes the <i>exit()</i> function, or by sufficient number of soft errors. </p>
<p> The language, which is described the <i>SCRIPT LANGUAGE</i> section below, is strictly typed, expressive, declaration free, procedural, prototyping-friendly, and inspired by <i>awk</i> and <i>C</i>. It allows source code points or events in the system to be associated with handlers, which are subroutines that are executed synchronously. It is somewhat similar conceptually to &quot;breakpoint command lists&quot; in the <i>gdb</i> debugger. </p>
<h2>DOCUMENTATION OVERVIEW</h2>
<p> systemtap comes with a variety of educational, documentation and reference resources. They come online and/or packaged for offline use. For online documentation, see the project web site, <a rel="nofollow" href="https://sourceware.org/systemtap/">https://sourceware.org/systemtap/</a> </p>
<table BORDER>
<tr VALIGN=top>
<td><code>man pages</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>stap (this page)</td>
<td>language syntax, concepts, operation, options
</td>
</tr>
<tr VALIGN=top>
<td>stapprobes</td>
<td>probe points and their $context variables
</td>
</tr>
<tr VALIGN=top>
<td>stapref</td>
<td>quick reference to language syntax
</td>
</tr>
<tr VALIGN=top>
<td>stappaths</td>
<td> list of directories, including books &amp; references 
</td>
</tr>
<tr VALIGN=top>
<td>stap-prep</td>
<td> program to install auxiliary dependencies like kernel debuginfo 
</td>
</tr>
<tr VALIGN=top>
<td>tapset::*</td>
<td>generated list of tapsets
</td>
</tr>
<tr VALIGN=top>
<td>probe::*</td>
<td>generated list of tapset probe aliases
</td>
</tr>
<tr VALIGN=top>
<td>function::*</td>
<td>generated list of tapset functions
</td>
</tr>
<tr VALIGN=top>
<td>macro::*</td>
<td>generated list of tapset macros
</td>
</tr>
<tr VALIGN=top>
<td>stapvars</td>
<td>some of the tapset global variables
</td>
</tr>
<tr VALIGN=top>
<td>staprun, stapdyn</td>
<td>programs for executing compiled systemtap scripts
</td>
</tr>
<tr VALIGN=top>
<td>systemtap</td>
<td>initscript, boot-time probing
</td>
</tr>
<tr VALIGN=top>
<td>stap-server</td>
<td>compilation server
</td>
</tr>
<tr VALIGN=top>
<td>stapex</td>
<td>a few very basic script examples
</td>
</tr>
<tr VALIGN=top>
<td><code>books</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Beginner&#8217;s Guide</td>
<td>tutorial book, language essentials, examples
</td>
</tr>
<tr VALIGN=top>
<td>Tutorial</td>
<td>shorter tutorial, exercises
</td>
</tr>
<tr VALIGN=top>
<td>Language Reference</td>
<td>detailed language manual, covers statistics/analysis
</td>
</tr>
<tr VALIGN=top>
<td>Tapset Reference</td>
<td>the tapset man pages, reformatted into a book
</td>
</tr>
<tr VALIGN=top>
<td><code>references</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>example scripts</td>
<td> over a hundred directly usable sysadmin tools, toys, hacks to learn from 
</td>
</tr>
</table>
<h2>OPTIONS</h2>
<p> The systemtap translator supports the following options. Any other option prints a list of supported options. Options may be given on the command line, as usual. If the file $SYSTEMTAP_DIR/rc exist, options are also loaded from there and interpreted first. ($SYSTEMTAP_DIR defaults to $HOME/.systemtap if unset.) </p>
<p> In some cases, the default value of an option depends on particular system configuration and thus can&#8217;t be mentioned here directly. In some of those cases running &quot;stap --help&quot; might display the default. </p>
<dl>
<dt><code>-</code></dt>
<dd> <p> Use standard input instead of a given FILENAME as probe language input, unless -e SCRIPT is given. </p>
 </dd>
<dt><code>-h --help</code></dt>
<dd> <p> Show help message. </p>
 </dd>
<dt><code>-V --version</code></dt>
<dd> <p> Show version message. </p>
 </dd>
<dt><code>-p</code><i> NUM</i></dt>
<dd> <p> Stop after pass NUM. The passes are numbered 1-5: parse, elaborate, translate, compile, run. See the <code>PROCESSING</code> section for details. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Increase verbosity for all passes. Produce a larger volume of informative (?) output each time option repeated. </p>
 </dd>
<dt><code>--vp ABCDE</code></dt>
<dd> <p> Increase verbosity on a per-pass basis. For example, &quot;--vp 002&quot; adds 2 units of verbosity to pass 3 only. The combination &quot;-v --vp 00004&quot; adds 1 unit of verbosity for all passes, and 4 more for pass 5. </p>
 </dd>
<dt><code>-k</code></dt>
<dd> <p> Keep the temporary directory after all processing. This may be useful in order to examine the generated C code, or to reuse the compiled kernel object. </p>
 </dd>
<dt><code>-g</code></dt>
<dd> <p> Guru mode. Enable parsing of unsafe expert-level constructs like embedded C. </p>
 </dd>
<dt><code>-P</code></dt>
<dd> <p> Prologue-searching mode. This is equivalent to --prologue-searching=always. Activate heuristics to work around incorrect debugging information for function parameter $context variables. </p>
 </dd>
<dt><code>-u</code></dt>
<dd> <p> Unoptimized mode. Disable unused code elision and many other optimizations during elaboration / translation. </p>
 </dd>
<dt><code>-w</code></dt>
<dd> <p> Suppressed warnings mode. Disables all warning messages. </p>
 </dd>
<dt><code>-W</code></dt>
<dd> <p> Treat all warnings as errors. </p>
 </dd>
<dt><code>-b</code></dt>
<dd> <p> Use bulk mode (percpu files) for kernel-to-user data transfer. Use the <i>stap-merge</i> program to multiplex them back together later. </p>
 </dd>
<dt><code>-i --interactive</code></dt>
<dd> <p> Interactive mode. Enable an interface to build the systemtap script incrementally and interactively. </p>
 </dd>
<dt><code>-t</code></dt>
<dd> <p> Collect timing information on the number of times probe executes and average amount of time spent in each probe-point. Also shows the derivation for each probe-point. </p>
 </dd>
<dt><code>-s</code><i> NUM</i></dt>
<dd> <p> Use NUM megabyte buffers for kernel-to-user data transfer. On a multiprocessor in bulk mode, this is a per-processor amount. </p>
 </dd>
<dt><code>-I</code><i> DIR</i></dt>
<dd> <p> Add the given directory to the tapset search directory. See the description of pass 2 for details. </p>
 </dd>
<dt><code>-D</code><i> NAME=VALUE</i></dt>
<dd> <p> Add the given C preprocessor directive to the module Makefile. These can be used to override limit parameters described below. </p>
 </dd>
<dt><code>-B</code><i> NAME=VALUE</i></dt>
<dd> <p> In kernel-runtime mode, add the given make directive to the kernel module build&#8217;s make invocation. These can be used to add or override kconfig options. For example, use <br />
 </p>
 </dd>
<dl>
<dd> <pre><code>
 -B CONFIG_DEBUG_INFO=y 
</code></pre>
 </dd></dl>
<p> to add debugging information. </p>
<dt><code>-B</code><i> FLAG</i></dt>
<dd> <p> In dyninst-runtime mode, add the given parameter to the compiler CFLAGS used for building the dyninst shared library. For example, use <br />
 </p>
 </dd>
<dl>
<dd> <pre><code>
 -B -g 
</code></pre>
 </dd></dl>
<p> to add debugging information. </p>
<dt><code>-a</code><i> ARCH</i></dt>
<dd> <p> Use a cross-compilation mode for the given target architecture. This requires access to the cross-compiler and the kernel build tree, and goes along with the <br />
 </p>
 </dd>
<dl>
<dd> <pre><code>
 -B CROSS_COMPILE=arch-tool-prefix- and
 -r /build/tree 
</code></pre>
 </dd></dl>
<p> options. </p>
<dt><code>--modinfo</code><i> NAME=VALUE</i></dt>
<dd> <p> Add the name/value pair as a MODULE_INFO macro call to the generated module. This may be useful to inform or override various module-related checks in the kernel. </p>
 </dd>
<dt><code>-G</code><i> NAME=VALUE</i></dt>
<dd> <p> Sets the value of global variable NAME to VALUE when staprun is invoked. This applies to scalar variables declared global in the script/tapset. </p>
 </dd>
<dt><code>-R</code><i> DIR</i></dt>
<dd> <p> Look for the systemtap runtime sources in the given directory. Your DIR default can be seen using &quot;stap --help&quot;. </p>
 </dd>
<dt><code>-r</code><i> /DIR</i></dt>
<dd> <p> Build for kernel in given build tree. Can also be set with the <i>SYSTEMTAP_RELEASE</i> environment variable. </p>
 </dd>
<dt><code>-r</code><i> RELEASE</i></dt>
<dd> <p> Build for kernel in build tree <code>/lib/modules/RELEASE/build</code>. Can also be set with the <i>SYSTEMTAP_RELEASE</i> environment variable. </p>
 </dd>
<dt><code>-m</code><i> MODULE</i></dt>
<dd> <p> Use the given name for the generated kernel object module, instead of a unique randomized name. The generated kernel object module is copied to the current directory. </p>
 </dd>
<dt><code>-d</code><i> MODULE</i></dt>
<dd> <p> Add symbol/unwind information for the given module into the kernel object module. This may enable symbolic tracebacks from those modules/programs, even if they do not have an explicit probe placed into them. </p>
 </dd>
<dt><code>--ldd</code></dt>
<dd> <p> Add symbol/unwind information for all user-space shared libraries suspected by ldd to be necessary for user-space binaries being probed or listed with the -d option. Caution: this can make the probe modules considerably larger. Note that this option does not deal with kernel-space modules: see instead --all-modules below. </p>
 </dd>
<dt><code>--all-modules</code></dt>
<dd> <p> Equivalent to specifying &quot;-dkernel&quot; and a &quot;-d&quot; for each kernel module that is currently loaded. Caution: this can make the probe modules considerably larger. </p>
 </dd>
<dt><code>-o</code><i> FILE</i></dt>
<dd> <p> Send standard output to named file. In bulk mode, percpu files will start with FILE_ (FILE_cpu with -F) followed by the cpu number. This supports <a href="/docs/linux/man/3-strftime/">strftime</a>(3) formats for FILE. </p>
 </dd>
<dt><code>-c</code><i> CMD</i></dt>
<dd> <p> Start the probes, run CMD, and exit when CMD finishes. This also has the effect of setting target() to the pid of the command ran. </p>
 </dd>
<dt><code>-x</code><i> PID</i></dt>
<dd> <p> Sets target() to PID. This allows scripts to be written that filter on a specific process. Scripts run independent of the PID&#8217;s lifespan. </p>
 </dd>
<dt><code>-e</code><i> SCRIPT</i></dt>
<dd> <p> Run the given SCRIPT specified on the command line. </p>
 </dd>
<dt><code>-E</code><i> SCRIPT</i></dt>
<dd> <p> Run the given SCRIPT specified. This SCRIPT is run in addition to the main script specified, through -e, or as a script file. This option can be repeated to run multiple scripts, and can be used in listing mode (-l/-L). </p>
 </dd>
<dt><code>-l</code><i> PROBE</i></dt>
<dd> <p> Instead of running a probe script, just list all available probe points matching the given single probe point. The pattern may include wildcards and aliases, but not comma-separated multiple probe points. The process result code will indicate failure if there are no matches. </p>
 </dd>
<dt><code>-L</code><i> PROBE</i></dt>
<dd> <p> Similar to &quot;-l&quot;, but list probe points and script-level local variables. </p>
 </dd>
<dt><code>-F</code></dt>
<dd> <p> Without -o option, load module and start probes, then detach from the module leaving the probes running. With -o option, run staprun in background as a daemon and show its pid. </p>
 </dd>
<dt><code>-S</code><i> size[,N]</i></dt>
<dd> <p> Sets the maximum size of output file and the maximum number of output files. If the size of output file will exceed <code>size</code> , systemtap switches output file to the next file. And if the number of output files exceed <code>N</code> , systemtap removes the oldest output file. You can omit the second argument. </p>
 </dd>
<dt><code>-T</code><i> TIMEOUT</i></dt>
<dd> <p> Exit the script after TIMEOUT seconds. </p>
 </dd>
<dt><code>--skip-badvars</code></dt>
<dd> <p> Ignore unresolvable or run-time-inaccessible context variables and substitute with 0, without errors. </p>
 </dd>
<dt><code>--prologue-searching</code>[=<i>WHEN</i>]</dt>
<dd> <p> Prologue-searching mode. Activate heuristics to work around incorrect debugging information for function parameter $context variables. WHEN can be either &quot;never&quot;, &quot;always&quot;, or &quot;auto&quot; (i.e. enabled by heuristic). If WHEN is missing, then &quot;always&quot; is assumed. If the option is missing, then &quot;auto&quot; is assumed. </p>
 </dd>
<dt><code>--suppress-handler-errors</code></dt>
<dd> <p> Wrap all probe handlers into something like this <br />
 </p>
 </dd>
<dl>
<dd> <pre><code>try { ... } catch { next }
</code></pre>
 </dd></dl>
<p> block, which causes any runtime errors to be quietly suppressed. Suppressed errors do not count against <code>MAXERRORS</code> limits. In this mode, the <code>MAXSKIPPED</code> limits are also suppressed, so that many errors and skipped probes may be accumulated during a script&#8217;s runtime. Any overall counts will still be reported at shutdown. </p>
<dt><code>--compatible</code><i> VERSION</i></dt>
<dd> <p> Suppress recent script language or tapset changes which are incompatible with given older version of systemtap. This may be useful if a much older systemtap script fails to run. See the DEPRECATION section for more details. </p>
 </dd>
<dt><code>--check-version</code></dt>
<dd> <p> This option is used to check if the active script has any constructs that may be systemtap version specific. See the DEPRECATION section for more details. </p>
 </dd>
<dt><code>--clean-cache</code></dt>
<dd> <p> This option prunes stale entries from the cache directory. This is normally done automatically after successful runs, but this option will trigger the cleanup manually and then exit. See the CACHING section for more details about cache limits. </p>
 </dd>
<dt><code>--color</code>[=<i>WHEN</i>], <code>--colour</code>[=<i>WHEN</i>]</dt>
<dd> <p> This option controls coloring of error messages. WHEN can be either &quot;never&quot;, &quot;always&quot;, or &quot;auto&quot; (i.e. enable only if at a terminal). If WHEN is missing, then &quot;always&quot; is assumed. If the option is missing, then &quot;auto&quot; is assumed. </p>
<p> Colors can be modified using the SYSTEMTAP_COLORS environment variable. The format must be of the form <code>key1=val1:key2=val2:key3=val3</code> ...etc. Valid keys are &quot;error&quot;, &quot;warning&quot;, &quot;source&quot;, &quot;caret&quot;, and &quot;token&quot;. Values constitute Select Graphic Rendition (SGR) parameter(s). Consult the documentation of your terminal for the SGRs it supports. As an example, the default colors would be expressed as <code>error=01;31:warning=00;33:source=00;34:caret=01:token=01</code>. If SYSTEMTAP_COLORS is absent, the default colors will be used. If it is empty or invalid, coloring is turned off. </p>
 </dd>
<dt><code>--disable-cache</code></dt>
<dd> <p> This option disables all use of the cache directory. No files will be either read from or written to the cache. </p>
 </dd>
<dt><code>--poison-cache</code></dt>
<dd> <p> This option treats files in the cache directory as invalid. No files will be read from the cache, but resulting files from this run will still be written to the cache. This is meant as a troubleshooting aid when stap&#8217;s cached behavior seems to be misbehaving. If it helped, there is a probably a bug in systemtap that the developers would like you to report. </p>
 </dd>
<dt><code>--privilege</code>[=<i>stapusr</i> | =<i>stapsys</i> | =<i>stapdev</i>]</dt>
<dd> <p> This option instructs <i>stap</i> to examine the script looking for constructs which are not allowed for the specified privilege level (see <i>UNPRIVILEGED USERS</i>). Compilation fails if any such constructs are used. If <i>stapusr</i> or <i>stapsys</i> are specified when using a compile server (see <i>--use-server</i>), the server will examine the script and, if compilation succeeds, the server will cryptographically sign the resulting kernel module, certifying that is it safe for use by users at the specified privilege level. </p>
<p> If <i>--privilege</i> has not been specified, <i>-pN</i> has not been specified with N &lt; 5, and the invoking user is not <i>root</i>, and is not a member of the group <i>stapdev</i>, then <i>stap</i> will automatically add the appropriate <i>--privilege</i> option to the options already specified. </p>
 </dd>
<dt><code>--unprivileged</code></dt>
<dd> <p> This option is equivalent to <i>--privilege=stapusr</i>. </p>
 </dd>
<dt><code>--use-server</code>[=<i>HOSTNAME</i>[<i>:PORT</i>] | =<i>IP_ADDRESS</i>[<i>:PORT</i>] | =<i>CERT_SERIAL</i>]</dt>
<dd> <p> Specify compile-server(s) to be used for compilation and/or in conjunction with <i>--list-servers</i> and <i>--trust-servers</i> (see below) for listing. If no argument is supplied, then the default in unprivileged mode (see <i>--privilege</i>) is to select compatible servers which are trusted as SSL peers and as module signers and currently online. Otherwise the default is to select compatible servers which are trusted as SSL peers and currently online. <i>--use-server</i> may be specified more than once, in which case a list of servers is accumulated in the order specified. Servers may be specified by host name, ip address, or by certificate serial number (obtained using <i>--list-servers</i>). The latter is most commonly used when adding or revoking trust in a server (see <i>--trust-servers</i> below). If a server is specified by host name or ip address, then an optional port number may be specified. This is useful for accessing servers which are not on the local network or to specify a particular server. </p>
<p> IP addresses may be IPv4 or IPv6 addresses. </p>
<p> If a particular IPv6 address is link local and exists on more than one interface, the intended interface may be specified by appending the address with a percent sign (%) followed by the intended interface name. For example, &quot;fe80::5eff:35ff:fe07:55ca%eth0&quot;. </p>
<p> In order to specify a port number with an IPv6 address, it is necessary to enclose the IPv6 address in square brackets ([]) in order to separate the port number from the rest of the address. For example, &quot;[fe80::5eff:35ff:fe07:55ca]:5000&quot; or &quot;[fe80::5eff:35ff:fe07:55ca%eth0]:5000&quot;. </p>
<p> If <i>--use-server</i> has not been specified, <i>-pN</i> has not been specified with N &lt; 5, and the invoking user not <i>root</i>, is not a member of the group <i>stapdev</i>, but is a member of the group <i>stapusr</i>, then <i>stap</i> will automatically add <i>--use-server</i> to the options already specified. </p>
 </dd>
<dt><code>--use-server-on-error</code>[=<code>yes</code>|=<code>no</code>]</dt>
<dd> <p> Instructs stap to retry compilation of a script using a compile server if compilation on the local host fails in a manner which suggests that it might succeed using a server. If this option is not specified, the default is <i>no</i>. If no argument is provided, then the default is <i>yes</i>. Compilation will be retried for certain types of errors (e.g. insufficient data or resources) which may not occur during re-compilation by a compile server. Compile servers will be selected automatically for the re-compilation attempt as if <i>--use-server</i> was specified with no arguments. </p>
 </dd>
<dt><code>--list-servers</code><i>[=SERVERS]</i></dt>
<dd> <p> Display the status of the requested <i>SERVERS</i>, where <i>SERVERS</i> is a comma-separated list of server attributes. The list of attributes is combined to filter the list of servers displayed. Supported attributes are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>all</code></dt>
<dd> <p> specifies all known servers (trusted SSL peers, trusted module signers, online servers). </p>
 </dd>
<dt><code>specified</code></dt>
<dd> <p> specifies servers specified using <i>--use-server</i>. </p>
 </dd>
<dt><code>online</code></dt>
<dd> <p> filters the output by retaining information about servers which are currently online. </p>
 </dd>
<dt><code>trusted</code></dt>
<dd> <p> filters the output by retaining information about servers which are trusted as SSL peers. </p>
 </dd>
<dt><code>signer</code></dt>
<dd> <p> filters the output by retaining information about servers which are trusted as module signers (see <i>--privilege</i>). </p>
 </dd>
<dt><code>compatible</code></dt>
<dd> <p> filters the output by retaining information about servers which are compatible with the current kernel release and architecture. </p>
 </dd></dl>
</dl>
<dd> <p> If no argument is provided, then the default is <code>specified</code>. If no servers were specified using <i>--use-server</i>, then the default servers for <i>--use-server</i> are listed. </p>
<p> Note that <i>--list-servers</i> uses the <i>avahi-daemon</i> service to detect online servers. If this service is not available, then <i>--list-servers</i> will fail to detect any <i>online</i> servers. In order for <i>--list-servers</i> to detect servers listening on IPv6 addresses, the <i>avahi-daemon</i> configuration file <i>/etc/avahi/avahi-daemon.conf</i> must contain an active &quot;use-ipv6=yes&quot; line. The service must be restarted after adding this line in order for IPv6 to be enabled. </p>
 </dd>
<dt><code>--trust-servers</code><i>[=TRUST_SPEC]</i></dt>
<dd> <p> Grant or revoke trust in compile-servers, specified using <i>--use-server</i> as specified by TRUST_SPEC, where TRUST_SPEC is a comma-separated list specifying the trust which is to be granted or revoked. Supported elements are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>ssl</code></dt>
<dd> <p> trust the specified servers as SSL peers. </p>
 </dd>
<dt><code>signer</code></dt>
<dd> <p> trust the specified servers as module signers (see <i>--privilege</i>). Only root can specify <code>signer.</code> </p>
 </dd>
<dt><code>all-users</code></dt>
<dd> <p> grant trust as an ssl peer for all users on the local host. The default is to grant trust as an ssl peer for the current user only. Trust as a module signer is always granted for all users. Only root can specify <code>all-users</code>. </p>
 </dd>
<dt><code>revoke</code></dt>
<dd> <p> revoke the specified trust. The default is to grant it. </p>
 </dd>
<dt><code>no-prompt</code></dt>
<dd> <p> do not prompt the user for confirmation before carrying out the requested action. The default is to prompt the user for confirmation. </p>
 </dd></dl>
</dl>
<dd> <p> If no argument is provided, then the default is <code>ssl</code>. If no servers were specified using <i>--use-server</i>, then no trust will be granted or revoked. </p>
 </dd>
<dd> <p> Unless <code>no-prompt</code> has been specified, the user will be prompted to confirm the trust to be granted or revoked before the operation is performed. </p>
 </dd>
<dt><code>--dump-probe-types</code></dt>
<dd> <p> Dumps a list of supported probe types and exits. If <i>--privilege=stapusr</i> is also specified, the list will be limited to probe types available to unprivileged users. </p>
 </dd>
<dt><code>--dump-probe-aliases</code></dt>
<dd> <p> Dumps a list of all probe aliases found in library files and exits. </p>
 </dd>
<dt><code>--dump-functions</code></dt>
<dd> <p> Dumps a list of all the public functions found in library files and exits. Also includes their parameters and types. A function of type &#8216;unknown&#8217; indicates a function that does not return a value. Note that not all function/parameter types may be resolved (these are also shown by &#8216;unknown&#8217;). This features is very memory-intensive and thus may not work properly with <i>--use-server</i> if the target server imposes an rlimit on process memory (i.e. through the <i>~stap-server/.systemtap/rc</i> configuration file, see <i><a href="/docs/linux/man/8-stap-server/">stap-server</a></i>(8)). </p>
 </dd>
<dt><code>--remote</code><i> URL</i></dt>
<dd> <p> Set the execution target to the given host. This option may be repeated to target multiple execution targets. Passes 1-4 are completed locally as normal to build the script, and then pass 5 will copy the module to the target and run it. Acceptable URL forms include: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>[USER@]HOSTNAME</code>, <code><a href="ssh://[USER@]HOSTNAME">ssh://[USER@]HOSTNAME</a></code></dt>
<dd> <p> This mode uses ssh, optionally using a username not matching your own. If a custom ssh_config file is in use, add <code>SendEnv LANG</code> to retain internationalization functionality. </p>
 </dd>
<dt><code>libvirt://DOMAIN</code>, <code>libvirt://DOMAIN/LIBVIRT_URI</code></dt>
<dd> <p> This mode uses <i>stapvirt</i> to execute the script on a domain managed by libvirt. Optionally, LIBVIRT_URI may be specified to connect to a specific driver and/or a remote host. For example, to connect to the local privileged QEMU driver, use: <br />
 </p>
 </dd>
<dl>
<dd> <pre><code>--remote libvirt://MyDomain/qemu:///system
</code></pre>
 </dd></dl>
<p> See the page at &lt;<a rel="nofollow" href="http://libvirt.org/uri.html">http://libvirt.org/uri.html</a>&gt; for supported URIs. Also see <i><a href="/docs/linux/man/1-stapvirt/">stapvirt</a></i>(1) for more information on how to prepare the domain for stap probing. </p>
<dt><code>unix:PATH</code></dt>
<dd> <p> This mode connects to a UNIX socket. This can be used with a QEMU virtio-serial port for executing scripts inside a running virtual machine. </p>
 </dd>
<dt><code>direct://</code></dt>
<dd> <p> Special loopback mode to run on the local host. </p>
 </dd></dl>
</dl>
<dd>  </dd>
<dt><code>--remote-prefix</code></dt>
<dd> <p> Prefix each line of remote output with &quot;N: &quot;, where N is the index of the remote execution target from which the given line originated. </p>
 </dd>
<dt><code>--download-debuginfo</code><i>[=OPTION]</i></dt>
<dd> <p> Enable, disable or set a timeout for the automatic debuginfo downloading feature offered by abrt as specified by OPTION, where OPTION is one of the following: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>yes</code></dt>
<dd> <p> enable automatic downloading of debuginfo with no timeout. This is the same as not providing an OPTION value to <i>--download-debuginfo</i> </p>
 </dd>
<dt><code>no</code></dt>
<dd> <p> explicitly disable automatic downloading of debuginfo. This is the same as not using the option at all. </p>
 </dd>
<dt><code>ask</code></dt>
<dd> <p> show abrt output, and ask before continuing download. No timeout will be set. </p>
 </dd>
<dt><code>&lt;timeout&gt;</code></dt>
<dd> <p> specify a timeout as a positive number to stop the download if it is taking longer than &lt;timeout&gt; seconds. </p>
 </dd></dl>
</dl>
<dd>  </dd>
<dt><code>--rlimit-as</code><i>=NUM</i></dt>
<dd> <p> Specify the maximum size of the process&#8217;s virtual memory (address space), in bytes. </p>
 </dd>
<dt><code>--rlimit-cpu</code><i>=NUM</i></dt>
<dd> <p> Specify the CPU time limit, in seconds. </p>
 </dd>
<dt><code>--rlimit-nproc</code><i>=NUM</i></dt>
<dd> <p> Specify the maximum number of processes that can be created. </p>
 </dd>
<dt><code>--rlimit-stack</code><i>=NUM</i></dt>
<dd> <p> Specify the maximum size of the process stack, in bytes. </p>
 </dd>
<dt><code>--rlimit-fsize</code><i>=NUM</i></dt>
<dd> <p> Specify the maximum size of files that the process may create, in bytes. </p>
 </dd>
<dt><code>--sysroot</code><i>=DIR</i></dt>
<dd> <p> Specify sysroot directory where target files (executables, libraries, etc.) are located. With <i>-r RELEASE</i>, the sysroot will be searched for the appropriate kernel build directory. With <i>-r /DIR</i>, however, the sysroot will not be used to find the kernel build. </p>
 </dd>
<dt><code>--sysenv</code><i>=VAR=VALUE</i></dt>
<dd> <p> Provide an alternate value for an environment variable where the value on a remote system differs. Path variables (e.g. PATH, LD_LIBRARY_PATH) are assumed to be relative to the directory provided by <i>--sysroot</i>, if provided. </p>
 </dd>
<dt><code>--suppress-time-limits</code></dt>
<dd> <p> Disable -DSTP_OVERLOAD related options as well as -DMAXACTION and -DMAXTRYLOCK. This option requires guru mode. </p>
 </dd>
<dt><code>--runtime</code><i>=MODE</i></dt>
<dd> <p> Set the pass-5 runtime mode. Valid options are <i>kernel</i> (default) and <i>dyninst</i>. See <code>ALTERNATE RUNTIMES</code> below for more information. </p>
 </dd>
<dt><code>--dyninst</code></dt>
<dd> <p> Shorthand for <i>--runtime=dyninst</i>. </p>
 </dd>
<dt><code>--save-uprobes</code></dt>
<dd> <p> On machines that require SystemTap to build its own uprobes module (kernels prior to version 3.5), this option instructs SystemTap to also save a copy of the module in the current directory (creating a new &quot;uprobes&quot; directory first). </p>
 </dd>
<dt><code>--target-namespaces</code><i>=PID</i></dt>
<dd> <p> Allow for a set of target namespaces to be set based on the namespaces the given PID is in. This is for namespace-aware tapset functions. If the target namespaces was not set, the target defaults to the stap process&#8217; namespaces. </p>
 </dd>
<dt><code>--monitor</code><i>=INTERVAL</i></dt>
<dd> <p> Enables an interface to display status information about the module(uptime, module name, invoker uid, memory sizes, global variables, list of probes with their statistics). An optional argument INTERVAL can be supplied to set the refresh rate in seconds of the status window. The module can also be controlled by a list of commands using the following keys: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>c</code></dt>
<dd> <p> Resets all global variables to their initial values or zeroes them if they did not have an initial value. </p>
 </dd>
<dt><code>s</code></dt>
<dd> <p> Rotates the attribute used to sort the list of probes. </p>
 </dd>
<dt><code>t</code></dt>
<dd> <p> Brings up a prompt to allow toggling(on/off) of probes by index. Probe points are still affected by their conditions. </p>
 </dd>
<dt><code>r</code></dt>
<dd> <p> Resumes the script by toggling on all probes. </p>
 </dd>
<dt><code>p</code></dt>
<dd> <p> Pauses the script by toggling off all probes. </p>
 </dd>
<dt><code>x</code></dt>
<dd> <p> Hides/shows the status window. This allows for more output to be seen. </p>
 </dd>
<dt><code>navigation-keys</code></dt>
<dd> <p> The navigation keys can be used to scroll up and down the windows. </p>
 </dd>
<dt><code>Tab</code></dt>
<dd> <p> Toggle scrolling between status and output windows. </p>
 </dd></dl>
</dl>
<h2>ARGUMENTS</h2>
<p> Any additional arguments on the command line are passed to the script parser for substitution. See below. </p>
<h2>SCRIPT LANGUAGE</h2>
<p> The systemtap script language resembles <i>awk</i> and <i>C</i>. There are two main outermost constructs: probes and functions. Within these, statements and expressions use C-like operator syntax and precedence. </p>
<h3>GENERAL SYNTAX</h3>
<p> Whitespace is ignored. Three forms of comments are supported: </p>
<dl>
<dd> <p> <br />
 <code>#</code> ... shell style, to the end of line, except for $# and @# <br />
 <code>//</code> ... C++ style, to the end of line <br />
 <code>/*</code> ... C style ... <code>*/</code> </p>
 </dd></dl>
<p> Literals are either strings enclosed in double-quotes (passing through the usual C escape codes with backslashes, and with adjacent string literals glued together, also as in C), or integers (in decimal, hexadecimal, or octal, using the same notation as in C). All strings are limited in length to some reasonable value (a few hundred bytes). Integers are 64-bit signed quantities, although the parser also accepts (and wraps around) values above positive 2**63. </p>
<p> In addition, script arguments given at the end of the command line may be inserted. Use <code>$1 ... $&lt;NN&gt;</code> for insertion unquoted, <code>@1 ... @&lt;NN&gt;</code> for insertion as a string literal. The number of arguments may be accessed through <code>$#</code> (as an unquoted number) or through <code>@#</code> (as a quoted number). These may be used at any place a token may begin, including within the preprocessing stage. Reference to an argument number beyond what was actually given is an error. </p>
<h3>PREPROCESSING</h3>
<p> A simple conditional preprocessing stage is run as a part of parsing. The general form is similar to the cond <code> ? </code>exp1 <code> : </code>exp2 ternary operator: <br />
 </p>
<dl>
<dd> <pre><code>
 %(  CONDITION %?  TRUE-TOKENS %) 
 %(  CONDITION %?  TRUE-TOKENS %:  FALSE-TOKENS %) 
</code></pre>
 </dd></dl>
<p> The CONDITION is either an expression whose format is determined by its first keyword, or a string literals comparison or a numeric literals comparison. It can be also composed of many alternatives and conjunctions of CONDITIONs (meant as in previous sentence) using || and &amp;&amp; respectively. However, parentheses are not supported yet, so remembering that conjunction takes precedence over alternative is important. </p>
<p> If the first part is the identifier <code>kernel_vr</code> or <code>kernel_v</code> to refer to the kernel version number, with (&quot;2.6.13-1.322FC3smp&quot;) or without (&quot;2.6.13&quot;) the release code suffix, then the second part is one of the six standard numeric comparison operators <code>&lt;</code>, <code>&lt;=</code>, <code>==</code>, <code>!=</code>, <code>&gt;</code>, and <code>&gt;=</code>, and the third part is a string literal that contains an RPM-style version-release value. The condition is deemed satisfied if the version of the target kernel (as optionally overridden by the <code>-r</code> option) compares to the given version string. The comparison is performed by the glibc function <code>strverscmp</code>. As a special case, if the operator is for simple equality (<code>==</code>), or inequality (<code>!=</code>), and the third part contains any wildcard characters (<code>*</code> or <code>?</code> or <code>[</code>), then the expression is treated as a wildcard (mis)match as evaluated by <code>fnmatch</code>. </p>
<p> If, on the other hand, the first part is the identifier <code>arch</code> to refer to the processor architecture (as named by the kernel build system ARCH/SUBARCH), then the second part is one of the two string comparison operators <code>==</code> or <code>!=</code>, and the third part is a string literal for matching it. This comparison is a wildcard (mis)match. </p>
<p> Similarly, if the first part is an identifier like <code>CONFIG_something</code> to refer to a kernel configuration option, then the second part is <code>==</code> or <code>!=</code>, and the third part is a string literal for matching the value (commonly &quot;y&quot; or &quot;m&quot;). Nonexistent or unset kernel configuration options are represented by the empty string. This comparison is also a wildcard (mis)match. </p>
<p> If the first part is the identifier <code>systemtap_v</code>, the test refers to the systemtap compatibility version, which may be overridden for old scripts with the <code>--compatible</code> flag. The comparison operator is as is for <code>kernel_v</code> and the right operand is a version string. See also the DEPRECATION section below. </p>
<p> If the first part is the identifier <code>systemtap_privilege</code>, the test refers to the privilege level that the systemtap script is compiled with. Here the second part is <code>==</code> or <code>!=</code>, and the third part is a string literal, either &quot;stapusr&quot; or &quot;stapsys&quot; or &quot;stapdev&quot;. </p>
<p> If the first part is the identifier <code>guru_mode</code>, the test refers to if the systemtap script is compiled with guru_mode. Here the second part is <code>==</code> or <code>!=</code>, and the third part is a number, either 1 or 0. </p>
<p> If the first part is the identifier <code>runtime</code>, the test refers to the systemtap runtime mode. See <code>ALTERNATE RUNTIMES</code> below for more information on runtimes. The second part is one of the two string comparison operators <code>==</code> or <code>!=</code>, and the third part is a string literal for matching it. This comparison is a wildcard (mis)match. </p>
<p> Otherwise, the CONDITION is expected to be a comparison between two string literals or two numeric literals. In this case, the arguments are the only variables usable. </p>
<p> The TRUE-TOKENS and FALSE-TOKENS are zero or more general parser tokens (possibly including nested preprocessor conditionals), and are passed into the input stream if the condition is true or false. For example, the following code induces a parse error unless the target kernel version is newer than 2.6.5: <br />
 </p>
<dl>
<dd> <pre><code>%( kernel_v &lt;= &quot;2.6.5&quot; %? **ERROR** %) # invalid token sequence
</code></pre>
 </dd></dl>
<p> The following code might adapt to hypothetical kernel version drift: <br />
 </p>
<dl>
<dd> <pre><code>probe kernel.function (
  %( kernel_v &lt;= &quot;2.6.12&quot; %? &quot;__mm_do_fault&quot; %:
     %( kernel_vr == &quot;2.6.13*smp&quot; %? &quot;do_page_fault&quot; %:
        UNSUPPORTED %) %)
) { /* ... */ }
%( arch == &quot;ia64&quot; %?
   probe syscall.vliw = kernel.function(&quot;vliw_widget&quot;) {}
%)
</code></pre>
 </dd></dl>
<h3>PREPROCESSOR MACROS</h3>
<p> The preprocessor also supports a simple macro facility, run as a separate pass before conditional preprocessing. </p>
<p> Macros are defined using the following construct: <br />
 </p>
<dl>
<dd> <pre><code>@define NAME %( BODY %)
@define NAME(PARAM_1, PARAM_2, ...) %( BODY %)
</code></pre>
 </dd></dl>
<p> Macros, and parameters inside a macro body, are both invoked by prefixing the macro name with an @ symbol: <br />
 </p>
<dl>
<dd> <pre><code>@define foo %( x %)
@define add(a,b) %( ((@a)+(@b)) %)
   @foo = @add(2,2)
</code></pre>
 </dd></dl>
<p> Macro expansion is currently performed in a separate pass before conditional compilation. Therefore, both TRUE- and FALSE-tokens in conditional expressions will be macroexpanded regardless of how the condition is evaluated. This can sometimes lead to errors: <br />
 </p>
<dl>
<dd> <pre><code>// The following results in a conflict:
%( CONFIG_UTRACE == &quot;y&quot; %?
    @define foo %( process.syscall %)
%:
    @define foo %( **ERROR** %)
%)
// The following works properly as expected:
@define foo %(
  %( CONFIG_UTRACE == &quot;y&quot; %? process.syscall %: **ERROR** %)
%)
</code></pre>
 </dd></dl>
<p> The first example is incorrect because both @defines are evaluated in a pass prior to the conditional being evaluated. </p>
<p> Normally, a macro definition is local to the file it occurs in. Thus, defining a macro in a tapset does not make it available to the user of the tapset. Publically available library macros can be defined by including .stpm files on the tapset search path. These files may only contain @define constructs, which become visible across all tapsets and user scripts. Optionally, within the .stpm files, a public macro definition can be surrounded by a preprocessor conditional as described above. </p>
<h3>CONSTANTS</h3>
<p> Tapsets or guru-mode user scripts can access header file constant tokens, typically macros, using built-in @const() operator. The respective header file inclusion is possible either via the tapset library, or using a top-level guru mode embedded-C construct. This results in appropriate embedded C pragma comments setting. <br />
 </p>
<dl>
<dd> <pre><code>@const(&quot;STP_SKIP_BADVARS&quot;)
</code></pre>
 </dd></dl>
<h3>VARIABLES</h3>
<p> Identifiers for variables and functions are an alphanumeric sequence, and may include <code>_</code> and <code>$</code> characters. They may not start with a plain digit, as in C. Each variable is by default local to the probe or function statement block within which it is mentioned, and therefore its scope and lifetime is limited to a particular probe or function invocation. </p>
<p> Scalar variables are implicitly typed as either string or integer. Associative arrays also have a string or integer value, and a tuple of strings and/or integers serving as a key. Here are a few basic expressions. <br />
 </p>
<dl>
<dd> <pre><code>var1 = 5
var2 = &quot;bar&quot;
array1 [pid()] = &quot;name&quot; # single numeric key
array2 [&quot;foo&quot;,4,i++] += 5 # vector of string/num/num keys
if ([&quot;hello&quot;,5,4] in array2) println (&quot;yes&quot;) # membership test
</code></pre>
 </dd></dl>
<p> The translator performs <i>type inference</i> on all identifiers, including array indexes and function parameters. Inconsistent type-related use of identifiers signals an error. </p>
<p> Variables may be declared global, so that they are shared amongst all probes and functions and live as long as the entire systemtap session. There is one namespace for all global variables, regardless of which script file they are found within. Concurrent access to global variables is automatically protected with locks, see the <code>SAFETY AND SECURITY</code> section for more details. A global declaration may be written at the outermost level anywhere, not within a block of code. Global variables which are written but never read will be displayed automatically at session shutdown. The translator will infer for each its value type, and if it is used as an array, its key types. Optionally, scalar globals may be initialized with a string or number literal. The following declaration marks variables as global. <br />
 </p>
<dl>
<dd> <pre><code>
 global  var1 ,  var2 ,  var3=4
</code></pre>
 </dd></dl>
<p> Global variables can also be set as module options. One can do this by either using the -G option, or the module must first be compiled using stap -p4. Global variables can then be set on the command line when calling staprun on the module generated by stap -p4. See <i><a href="/docs/linux/man/8-staprun/">staprun</a></i>(8) for more information. </p>
<p> The scope of a global variable may be limited to a tapset or user script file using private keyword. The global keyword is optional when defining a private global variable. Following declaration marks var1 and var2 private globals. <br />
 </p>
<dl>
<dd> <pre><code>
 private  global  var1=2 
 private  var2
</code></pre>
 </dd></dl>
<p> Arrays are limited in size by the MAXMAPENTRIES variable -- see the <code>SAFETY AND SECURITY</code> section for details. Optionally, global arrays may be declared with a maximum size in brackets, overriding MAXMAPENTRIES for that array only. Note that this doesn&#8217;t indicate the type of keys for the array, just the size. <br />
 </p>
<dl>
<dd> <pre><code>
 global  tiny_array[10] ,  normal_array ,  big_array[50000]
</code></pre>
 </dd></dl>
<p> Arrays may be configured for wrapping using the &#8216;%&#8216; suffix. This causes older elements to be overwritten if more elements are inserted than the array can hold. This works for both associative and statistics typed arrays. <br />
 </p>
<dl>
<dd> <pre><code>
 global  wrapped_array1%[10],  wrapped_array2% 
</code></pre>
 </dd></dl>
<p> Many types of probe points provide context variables, which are run-time values, safely extracted from the kernel or userspace program being probed. These are prefixed with the <code>$</code> character. The CONTEXT VARIABLES section in <i>stapprobes</i>(3stap) lists what is available for each type of probe point. These context variables become normal string or numeric scalars once they are stored in normal script variables. See the TYPECASTING section below on how to to turn them back into typed pointers for further processing as context variables. </p>
<h3>STATEMENTS</h3>
<p> Statements enable procedural control flow. They may occur within functions and probe handlers. The total number of statements executed in response to any single probe event is limited to some number defined by the MAXACTION macro in the translated C code, and is in the neighbourhood of 1000. </p>
<dl>
<dt>EXP</dt>
<dd> <p> Execute the string- or integer-valued expression and throw away the value. </p>
 </dd>
<dt><code>{</code> STMT1 STMT2 ... <code>}</code></dt>
<dd> <p> Execute each statement in sequence in this block. Note that separators or terminators are generally not necessary between statements. </p>
 </dd>
<dt><code>;</code></dt>
<dd> <p> Null statement, do nothing. It is useful as an optional separator between statements to improve syntax-error detection and to handle certain grammar ambiguities. </p>
 </dd>
<dt><code>if</code> (EXP) STMT1 [ <code>else</code> STMT2 ] </dt>
<dd> <p> Compare integer-valued EXP to zero. Execute the first (non-zero) or second STMT (zero). </p>
 </dd>
<dt><code>while</code> (EXP) STMT </dt>
<dd> <p> While integer-valued EXP evaluates to non-zero, execute STMT. </p>
 </dd>
<dt><code>for</code> (EXP1; EXP2; EXP3) STMT </dt>
<dd> <p> Execute EXP1 as initialization. While EXP2 is non-zero, execute STMT, then the iteration expression EXP3. </p>
 </dd>
<dt><code>foreach</code> (VAR <code>in</code> ARRAY [ limit <code> EXP ]) STMT</code></dt>
<dd> <p> Loop over each element of the named global array, assigning current key to VAR. The array may not be modified within the statement. By adding a single <code>+</code> or <code>-</code> operator after the VAR or the ARRAY identifier, the iteration will proceed in a sorted order, by ascending or descending index or value. If the array contains statistics aggregates, adding the desired <code>@operator</code> between the ARRAY identifier and the <code>+</code> or <code>-</code> will specify the sorting aggregate function. See the STATISTICS section below for the ones available. Default is <code>@count</code>. Using the optional <code>limit</code> keyword limits the number of loop iterations to EXP times. EXP is evaluated once at the beginning of the loop. </p>
 </dd>
<dt><code>foreach</code> ([VAR1, VAR2, ...] <code>in</code> ARRAY [ limit <code> EXP ]) STMT</code></dt>
<dd> <p> Same as above, used when the array is indexed with a tuple of keys. A sorting suffix may be used on at most one VAR or ARRAY identifier. </p>
 </dd>
<dt><code>foreach</code> ([VAR1, VAR2, ...] <code>in</code> ARRAY [INDEX1, INDEX2, ...] [ limit <code> EXP ]) STMT</code></dt>
<dd> <p> Same as above, where iterations are limited to elements in the array where the keys match the index values specified. The symbol * can be used to specify an index and will be treated as a wildcard. </p>
 </dd>
<dt><code>foreach</code> (VAR0 = VAR <code>in</code> ARRAY [ limit <code> EXP ]) STMT</code></dt>
<dd> <p> This variant of foreach saves current value into VAR0 on each iteration, so it is the same as ARRAY[VAR]. This also works with a tuple of keys. Sorting suffixes on VAR0 have the same effect as on ARRAY. </p>
 </dd>
<dt><code>foreach</code> (VAR0 = VAR <code>in</code> ARRAY [INDEX1, INDEX2, ...] [ limit <code> EXP ]) STMT</code></dt>
<dd> <p> Same as above, where iterations are limited to elements in the array where the keys match the index values specified. The symbol * can be used to specify an index and will be treated as a wildcard. </p>
 </dd>
<dt><code>break</code>, <code>continue</code></dt>
<dd> <p> Exit or iterate the innermost nesting loop (<code>while</code> or <code>for</code> or <code>foreach</code>) statement. </p>
 </dd>
<dt><code>return</code> EXP </dt>
<dd> <p> Return EXP value from enclosing function. If the function&#8217;s value is not taken anywhere, then a return statement is not needed, and the function will have a special &quot;unknown&quot; type with no return value. </p>
 </dd>
<dt><code>next</code></dt>
<dd> <p> Return now from enclosing probe handler. This is especially useful in probe aliases that apply event filtering predicates. When used in functions, the execution will be immediately transferred to the next overloaded function. </p>
 </dd>
<dt><code>try</code> { STMT1 } <code>catch</code> { STMT2 } </dt>
<dd> <p> Run the statements in the first block. Upon any run-time errors, abort STMT1 and start executing STMT2. Any errors in STMT2 will propagate to outer try/catch blocks, if any. </p>
 </dd>
<dt><code>try</code> { STMT1 } <code>catch</code>(VAR) { STMT2 } </dt>
<dd> <p> Same as above, plus assign the error message to the string scalar variable VAR. </p>
 </dd>
<dt><code>delete</code> ARRAY[INDEX1, INDEX2, ...] </dt>
<dd> <p> Remove from ARRAY the element specified by the index tuple. If the index tuple contains a * in place of an index, the * is treated as a wildcard and all elements with keys that match the index tuple will be removed from ARRAY. The value will no longer be available, and subsequent iterations will not report the element. It is not an error to delete an element that does not exist. </p>
 </dd>
<dt><code>delete</code> ARRAY </dt>
<dd> <p> Remove all elements from ARRAY. </p>
 </dd>
<dt><code>delete</code> SCALAR </dt>
<dd> <p> Removes the value of SCALAR. Integers and strings are cleared to 0 and &quot;&quot; respectively, while statistics are reset to the initial empty state. </p>
 </dd></dl>
<h3>EXPRESSIONS</h3>
<p> Systemtap supports a number of operators that have the same general syntax, semantics, and precedence as in C and awk. Arithmetic is performed as per typical C rules for signed integers. Division by zero or overflow is detected and results in an error. </p>
<dl>
<dt>binary numeric operators</dt>
<dd> <p> <code>* / % + - &gt;&gt; &lt;&lt; &amp; ^ | &amp;&amp; ||</code> </p>
 </dd>
<dt>binary string operators</dt>
<dd> <p> <code>.</code> (string concatenation) </p>
 </dd>
<dt>numeric assignment operators</dt>
<dd> <p> <code>= *= /= %= += -= &gt;&gt;= &lt;&lt;= &amp;= ^= |=</code> </p>
 </dd>
<dt>string assignment operators</dt>
<dd> <p> <code>= .=</code> </p>
 </dd>
<dt>unary numeric operators</dt>
<dd> <p> <code>+ - ! ~ ++ --</code> </p>
 </dd>
<dt>binary numeric, string comparison or regex matching operators</dt>
<dd> <p> <code>&lt; &gt; &lt;= &gt;= == != =~ !~</code> </p>
 </dd>
<dt>ternary operator</dt>
<dd> <p> cond <code> ? </code>exp1 <code> : </code>exp2 </p>
 </dd>
<dt>grouping operator</dt>
<dd> <p> <code>(</code> exp <code>)</code> </p>
 </dd>
<dt>function call</dt>
<dd> <p> fn <code>(</code>[ arg1, arg2, ... ]<code>)</code> </p>
 </dd>
<dt>array membership check</dt>
<dd> <p> exp <code> in </code>array <br />
 <code>[</code>exp1 <code>, </code>exp2 <code>, </code>...<code>] in </code>array <br />
 <code>[</code>*<code>, </code>*<code>, ... ]</code>in <code> array</code> </p>
 </dd></dl>
<h3>REGULAR EXPRESSION MATCHING</h3>
<p> The scripting language supports regular expression matching. The basic syntax is as follows: <br />
 </p>
<dl>
<dd> <pre><code>
 exp  =~ regex 
 exp  !~ regex 
</code></pre>
 </dd></dl>
<p> (The first operand must be an expression evaluating to a string; the second operand must be a string literal containing a syntactically valid regular expression.) </p>
<p> The regular expression syntax supports most of the features of POSIX Extended Regular Expressions, except for subexpression reuse (&quot;\1&quot;) functionality. The ability to capture and extract the contents of the matched string and subexpressions has not yet been implemented. </p>
<h3>PROBES</h3>
<p> The main construct in the scripting language identifies probes. Probes associate abstract events with a statement block (&quot;probe handler&quot;) that is to be executed when any of those events occur. The general syntax is as follows: <br />
 </p>
<dl>
<dd> <pre><code>
 probe  PROBEPOINT [ ,  PROBEPOINT] {  [STMT ...] } 
 probe  PROBEPOINT [ ,  PROBEPOINT] if ( CONDITION ) { [STMT ...]  } 
</code></pre>
 </dd></dl>
<p> Events are specified in a special syntax called &quot;probe points&quot;. There are several varieties of probe points defined by the translator, and tapset scripts may define further ones using aliases. Probe points may be wildcarded, grouped, or listed in preference sequences, or declared optional. More details on probe point syntax and semantics are listed on the <i>stapprobes</i>(3stap) manual page. </p>
<p> The probe handler is interpreted relative to the context of each event. For events associated with kernel code, this context may include <i>variables</i> defined in the <i>source code</i> at that spot. These &quot;context variables&quot; are presented to the script as variables whose names are prefixed with &quot;$&quot;. They may be accessed only if the kernel&#8217;s compiler preserved them despite optimization. This is the same constraint that a debugger user faces when working with optimized code. In addition, the objects must exist in paged-in memory at the moment of the systemtap probe handler&#8217;s execution, because systemtap must not cause (suppresses) any additional paging. Some probe types have very little context. See the <i>stapprobes</i>(3stap) man pages to see the kinds of context variables available at each kind of probe point. </p>
<p> Probes may be decorated with an <i>arming condition</i>, consisting of a simple boolean expression on read-only global script variables. While disarmed (inactive, condition evaluates to false), some probe types reduce or eliminate their run-time overheads. When an arming condition evaluates to true, probes will be <i>soon</i> re-armed, and their probe handlers will start getting called as the events fire. (Some events may be lost during the arming interval. If this is unacceptable, do not use arming conditions for those probes.) Example of the syntax: <br />
 </p>
<dl>
<dd> <pre><code>probe timer.us(TIMER) if (enabled) {
}
</code></pre>
 </dd></dl>
<p> New probe points may be defined using &quot;aliases&quot;. Probe point aliases look similar to probe definitions, but instead of activating a probe at the given point, it just defines a new probe point name as an alias to an existing one. There are two types of alias, i.e. the prologue style and the epilogue style which are identified by &quot;=&quot; and &quot;+=&quot; respectively. </p>
<p> For prologue style alias, the statement block that follows an alias definition is implicitly added as a prologue to any probe that refers to the alias. While for the epilogue style alias, the statement block that follows an alias definition is implicitly added as an epilogue to any probe that refers to the alias. For example: <br />
 </p>
<dl>
<dd> <pre><code>probe syscall.read = kernel.function(&quot;sys_read&quot;) {
  fildes = $fd
  if (execname() == &quot;init&quot;) next # skip rest of probe
}
</code></pre>
 </dd></dl>
<p> defines a new probe point <i>syscall.read</i>, which expands to <i>kernel.function(sys_read)</i>, with the given statement as a prologue, which is useful to predefine some variables for the alias user and/or to skip probe processing entirely based on some conditions. And <br />
 </p>
<dl>
<dd> <pre><code>probe syscall.read += kernel.function(&quot;sys_read&quot;) {
  if (tracethis) println ($fd)
}
</code></pre>
 </dd></dl>
<p> defines a new probe point with the given statement as an epilogue, which is useful to take actions based upon variables set or left over by the the alias user. Please note that in each case, the statements in the alias handler block are treated ordinarily, so that variables assigned there constitute mere initialization, not a macro substitution. </p>
<p> An alias is used just like a built-in probe type. <br />
 </p>
<dl>
<dd> <pre><code>probe syscall.read {
  printf(&quot;reading fd=%d\n&quot;, fildes)
  if (fildes &gt; 10) tracethis = 1
}
</code></pre>
 </dd></dl>
<h3>FUNCTIONS</h3>
<p> Systemtap scripts may define subroutines to factor out common work. Functions take any number of scalar (integer or string) arguments, and must return a single scalar (integer or string). An example function declaration looks like this: <br />
 </p>
<dl>
<dd> <pre><code>function thisfn (arg1, arg2) {
   return arg1 + arg2
}
</code></pre>
 </dd></dl>
<p> Note the general absence of type declarations, which are instead inferred by the translator. However, if desired, a function definition may include explicit type declarations for its return value and/or its arguments. This is especially helpful for embedded-C functions. In the following example, the type inference engine need only infer type type of arg2 (a string). <br />
 </p>
<dl>
<dd> <pre><code>function thatfn:string (arg1:long, arg2) {
   return sprint(arg1) . arg2
}
</code></pre>
 </dd></dl>
<p> Functions may call others or themselves recursively, up to a fixed nesting limit. This limit is defined by the MAXNESTING macro in the translated C code and is in the neighbourhood of 10. </p>
<p> Functions may be marked private using the private keyword to limit their scope to the tapset or user script file they are defined in. An example definition of a private function follows: <br />
 </p>
<dl>
<dd> <pre><code>private function three:long () { return 3 }
</code></pre>
 </dd></dl>
<p> Functions terminating without reaching an explicit return statement will return an implicit 0 or &quot;&quot;, determined by type inference. </p>
<p> Functions may be overloaded during both runtime and compile time. </p>
<p> Runtime overloading allows the executed function to be selected while the module is running based on runtime conditions and is achieved using the &quot;next&quot; statement in script functions and STAP_NEXT macro for embedded-C functions. For example, </p>
<p> <br />
 </p>
<dl>
<dd> <pre><code>function f() { if (condition) next; print(&quot;first function&quot;) }
function f() %{ STAP_NEXT; print(&quot;second function&quot;) %}
function f() { print(&quot;third function&quot;) }
</code></pre>
 </dd></dl>
<p> During a functioncall f(), the execution will transfer to the third function if condition evaluates to true and print &quot;third function&quot;. Note that the second function is unconditionally nexted. </p>
<p> Parameter overloading allows the function to be executed to be selected at compile time based on the number of arguments provided to the functioncall. For example, </p>
<p> <br />
 </p>
<dl>
<dd> <pre><code>function g() { print(&quot;first function&quot;) }
function g(x) { print(&quot;second function&quot;) }
g() -&gt; &quot;first function&quot;
g(1) -&gt; &quot;second function&quot;
</code></pre>
 </dd></dl>
<p> Note that runtime overloading does not occur in the above example, as exactly one function will be resolved for the functioncall. The use of a next statement inside a function while no more overloads remain will trigger a runtime exception Runtime overloading will only occur if the functions have the same arity, functions with the same name but different number of parameters are completely unrelated. </p>
<p> Execution order is determined by a priority value which may be specified. If no explicit priority is specified, user script functions are given a higher priority than library functions. User script functions and library functions are assigned a default priority value of 0 and 1 respectively. Functions with the same priority are executed in declaration order. For example, </p>
<p> <br />
 </p>
<dl>
<dd> <pre><code>function f():3 { if (condition) next; print(&quot;first function&quot;) }
function f():1 { if (condition) next; print(&quot;second function&quot;) }
function f():2 { print(&quot;third function&quot;) }
</code></pre>
 </dd></dl>
<p> Since the second function has highest priority, it is executed first. The first function is never executed as there no &quot;next&quot; statements in the third function to transfer execution. </p>
<h3>PRINTING</h3>
<p> There are a set of function names that are specially treated by the translator. They format values for printing to the standard systemtap output stream in a more convenient way (note that data generated in the kernel module need to get transferred to user-space in order to get printed). </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>The <i>sprint*</i> variants return the formatted string instead of printing it. </p>
<dl>
<dt><code>print</code>, <code>sprint</code></dt>
<dd> <p> Print one or more values of any type, concatenated directly together. </p>
 </dd>
<dt><code>println</code>, <code>sprintln</code></dt>
<dd> <p> Print values like <i>print</i> and <i>sprint</i>, but also append a newline. </p>
 </dd>
<dt><code>printd</code>, <code>sprintd</code></dt>
<dd> <p> Take a string delimiter and two or more values of any type, and print the values with the delimiter interposed. The delimiter must be a literal string constant. </p>
 </dd>
<dt><code>printdln</code>, <code>sprintdln</code></dt>
<dd> <p> Print values with a delimiter like <i>printd</i> and <i>sprintd</i>, but also append a newline. </p>
 </dd>
<dt><code>printf</code>, <code>sprintf</code></dt>
<dd> <p> Take a formatting string and a number of values of corresponding types, and print them all. The format must be a literal string constant. </p>
 </dd></dl>
<p> The <i>printf</i> formatting directives similar to those of C, except that they are fully type-checked by the translator: </p>
<dl>
<dd>  </dd>
<dl>
<dt>%b</dt>
<dd> <p> Writes a binary blob of the value given, instead of ASCII text. The width specifier determines the number of bytes to write; valid specifiers are %b %1b %2b %4b %8b. Default (%b) is 8 bytes. </p>
 </dd>
<dt>%c</dt>
<dd> <p> Character. </p>
 </dd>
<dt>%d,%i</dt>
<dd> <p> Signed decimal. </p>
 </dd>
<dt>%m</dt>
<dd> <p> Safely reads kernel (without #) or user (with #) memory at the given address, outputs its content. The optional precision specifier (not field width) determines the number of bytes to read - default is 1 byte. %10.4m prints 4 bytes of the memory in a 10-character-wide field. Note, on some architectures user memory can still be read without #. </p>
 </dd>
<dt>%M</dt>
<dd> <p> Same as %m, but outputs in hexadecimal. The minimal size of output is double the optional precision specifier - default is 1 byte (2 hex chars). %10.4M prints 4 bytes of the memory as 8 hexadecimal characters in a 10-character-wide field. %.*M hex-dumps a given number of bytes from a given buffer. </p>
 </dd>
<dt>%o</dt>
<dd> <p> Unsigned octal. </p>
 </dd>
<dt>%p</dt>
<dd> <p> Unsigned pointer address. </p>
 </dd>
<dt>%s</dt>
<dd> <p> String. </p>
 </dd>
<dt>%u</dt>
<dd> <p> Unsigned decimal. </p>
 </dd>
<dt>%x</dt>
<dd> <p> Unsigned hex value, in all lower-case. </p>
 </dd>
<dt>%X</dt>
<dd> <p> Unsigned hex value, in all upper-case. </p>
 </dd>
<dt>%%</dt>
<dd> <p> Writes a %. </p>
 </dd></dl>
</dl>
<p> The <i>#</i> flag selects the alternate forms. For octal, this prefixes a 0. For hex, this prefixes 0x or 0X, depending on case. For characters, this escapes non-printing values with either C-like escapes or raw octal. In the case of %#m/%#M, this safely accesses user space memory rather than kernel space memory. </p>
<p> Examples: <br />
 </p>
<dl>
<dd> <pre><code>a = &quot;alice&quot;, b = &quot;bob&quot;, p = 0x1234abcd, i = 123, j = -1, id[a] = 1234, id[b] = 4567
print(&quot;hello&quot;)
        Prints: hello
println(b)
        Prints: bob\n
println(a . &quot; is &quot; . sprint(16))
        Prints: alice is 16
foreach (name in id) printdln(&quot;|&quot;, strlen(name), name, id[name])
        Prints: 5|alice|1234\n3|bob|4567
printf(&quot;%c is %s; %x or %X or %p; %d or %u\n&quot;,97,a,p,p,p,j,j)
        Prints: a is alice; 1234abcd or 1234ABCD or 0x1234abcd; -1 or 18446744073709551615\n
printf(&quot;2 bytes of kernel buffer at address %p: %2m&quot;, p, p)
        Prints: 2 byte of kernel buffer at address 0x1234abcd: &lt;binary data&gt;
printf(&quot;%4b&quot;, p)
        Prints (these values as binary data): 0x1234abcd
printf(&quot;%#o %#x %#X\n&quot;, 1, 2, 3)
        Prints: 01 0x2 0X3
printf(&quot;%#c %#c %#c\n&quot;, 0, 9, 42)
        Prints: \000 \t *
</code></pre>
 </dd></dl>
<h3>STATISTICS</h3>
<p> It is often desirable to collect statistics in a way that avoids the penalties of repeatedly exclusive locking the global variables those numbers are being put into. Systemtap provides a solution using a special operator to accumulate values, and several pseudo-functions to extract the statistical aggregates. </p>
<p> The aggregation operator is <i>&lt;&lt;&lt;</i>, and resembles an assignment, or a C++ output-streaming operation. The left operand specifies a scalar or array-index lvalue, which must be declared global. The right operand is a numeric expression. The meaning is intuitive: add the given number to the pile of numbers to compute statistics of. (The specific list of statistics to gather is given separately, by the extraction functions.) <br />
 </p>
<dl>
<dd> <pre><code>foo &lt;&lt;&lt; 1
stats[pid()] &lt;&lt;&lt; memsize
</code></pre>
 </dd></dl>
<p> The extraction functions are also special. For each appearance of a distinct extraction function operating on a given identifier, the translator arranges to compute a set of statistics that satisfy it. The statistics system is thereby &quot;on-demand&quot;. Each execution of an extraction function causes the aggregation to be computed for that moment across all processors. </p>
<p> Here is the set of extractor functions. The first argument of each is the same style of lvalue used on the left hand side of the accumulate operation. The <i>@count(v)</i>, <i>@sum(v)</i>, <i>@min(v)</i>, <i>@max(v)</i>, <i>@avg(v)</i>, @variance(v[, b]) extractor functions compute the number/total/minimum/maximum/average/variance of all accumulated values. The resulting values are all simple integers. Arrays containing aggregates may be sorted and iterated. See the <code>foreach</code> construct above. </p>
<p> Variance uses Welford&#8217;s online algorithm. The calculations are based on integer arithmetic, and so may suffer from low precision and overflow. To improve this, @variance(v[, b]) accepts an optional parameter b, the bit-shift, ranging from 0 (default) to 62, for internal scaling. Only one value of bit-shift may be used with given global variable. A larger bitshift value increases precision, but increases the likelihood of overflow. </p>
<p> <br />
 </p>
<dl>
<dd> <pre><code>$ stap -e \
&gt; 'global x probe oneshot { for(i=1;i&lt;=5;i++) x&lt;&lt;&lt;i println(@variance(x)) }'
12
$ stap -e \
&gt; 'global x probe oneshot { for(i=1;i&lt;=5;i++) x&lt;&lt;&lt;i println(@variance(x,1)) }'
2
$ python3 -c 'import statistics; print(statistics.variance([1, 2, 3, 4, 5]))'
2.5
$
</code></pre>
 </dd></dl>
<p> Overflow (from internal multiplication of large numbers) may occur and may cause a negative variance result. Consider normalizing your input data. Adding or subtracting a fixed value from all variance inputs preserves the original variance. Dividing the variance inputs by a fixed value shrinks the original variance by that value squared. </p>
<p> Histograms are also available, but are more complicated because they have a vector rather than scalar value. <i>@hist_linear(v,start,stop,interval)</i> represents a linear histogram from &quot;start&quot; to &quot;stop&quot; by increments of &quot;interval&quot;. The interval must be positive. Similarly, <i>@hist_log(v)</i> represents a base-2 logarithmic histogram. Printing a histogram with the <i>print</i> family of functions renders a histogram object as a tabular &quot;ASCII art&quot; bar chart. <br />
 </p>
<dl>
<dd> <pre><code>probe timer.profile {
  x[1] &lt;&lt;&lt; pid()
  x[2] &lt;&lt;&lt; uid()
  y &lt;&lt;&lt; tid()
}
global x // an array containing aggregates
global y // a scalar
probe end {
  foreach ([i] in x @count+) {
     printf (&quot;x[%d]: avg %d = sum %d / count %d\n&quot;,
             i, @avg(x[i]), @sum(x[i]), @count(x[i]))
     println (@hist_log(x[i]))
  }
  println (&quot;y:&quot;)
  println (@hist_log(y))
}
</code></pre>
 </dd></dl>
<h3>TYPECASTING</h3>
<p> Once a pointer (see the CONTEXT VARIABLES section of <i>stapprobes</i>(3stap)) has been saved into a script integer variable, the translator loses the type information necessary to access members from that pointer. Using the <i>@cast()</i> operator tells the translator how to interpret the number as a typed pointer. <br />
 </p>
<dl>
<dd> <pre><code>@cast(p, &quot;type_name&quot;[, &quot;module&quot;])-&gt;member
</code></pre>
 </dd></dl>
<p> This will interpret <i>p</i> as a pointer to a struct/union named <i>type_name</i> and dereference the <i>member</i> value. Further <i>-&gt;subfield</i> expressions may be appended to dereference more levels. NOTE: the same dereferencing operator <i>-&gt;</i> is used to refer to both direct containment or pointer indirection. Systemtap automatically determines which. The optional <i>module</i> tells the translator where to look for information about that type. Multiple modules may be specified as a list with <i>:</i> separators. If the module is not specified, it will default either to the probe module for dwarf probes, or to &quot;kernel&quot; for functions and all other probes types. </p>
<p> The translator can create its own module with type information from a header surrounded by angle brackets, in case normal debuginfo is not available. For kernel headers, prefix it with &quot;kernel&quot; to use the appropriate build system. All other headers are built with default GCC parameters into a user module. Multiple headers may be specified in sequence to resolve a codependency. <br />
 </p>
<dl>
<dd> <pre><code>@cast(tv, &quot;timeval&quot;, &quot;&lt;sys/time.h&gt;&quot;)-&gt;tv_sec
@cast(task, &quot;task_struct&quot;, &quot;kernel&lt;linux/sched.h&gt;&quot;)-&gt;tgid
@cast(task, &quot;task_struct&quot;,
      &quot;kernel&lt;linux/sched.h&gt;&lt;linux/fs_struct.h&gt;&quot;)-&gt;fs-&gt;umask
</code></pre>
 </dd></dl>
<p> Values acquired by <code>@cast</code> may be pretty-printed by the <code>$</code> and <code>$$</code> suffix operators, the same way as described in the CONTEXT VARIABLES section of the <i>stapprobes</i>(3stap) manual page. </p>
<p> When in guru mode, the translator will also allow scripts to assign new values to members of typecasted pointers. </p>
<p> Typecasting is also useful in the case of <i>void*</i> members whose type may be determinable at runtime. <br />
 </p>
<dl>
<dd> <pre><code>probe foo {
  if ($var-&gt;type == 1) {
    value = @cast($var-&gt;data, &quot;type1&quot;)-&gt;bar
  } else {
    value = @cast($var-&gt;data, &quot;type2&quot;)-&gt;baz
  }
  print(value)
}
</code></pre>
 </dd></dl>
<h3>EMBEDDED C</h3>
<p> When in guru mode, the translator accepts embedded C code in the top level of the script. Such code is enclosed between <i>%{</i> and <i>%}</i> markers, and is transcribed verbatim, without analysis, in some sequence, into the top level of the generated C code. At the outermost level, this may be useful to add <i>#include</i> instructions, and any auxiliary definitions for use by other embedded code. </p>
<p> Another place where embedded code is permitted is as a function body. In this case, the script language body is replaced entirely by a piece of C code enclosed again between <i>%{</i> and <i>%}</i> markers. This C code may do anything reasonable and safe. There are a number of undocumented but complex safety constraints on atomicity, concurrency, resource consumption, and run time limits, so this is an advanced technique. </p>
<p> The memory locations set aside for input and output values are made available to it using macros <i>STAP_ARG_*</i> and <i>STAP_RETVALUE</i>. Errors may be signalled with STAP_ERROR. Output may be written with STAP_PRINTF. The function may return early with STAP_RETURN. Here are some examples: <br />
 </p>
<dl>
<dd> <pre><code>function integer_ops (val) %{
  STAP_PRINTF(&quot;%d\n&quot;, STAP_ARG_val);
  STAP_RETVALUE = STAP_ARG_val + 1;
  if (STAP_RETVALUE == 4)
      STAP_ERROR(&quot;wrong guess: %d&quot;, (int) STAP_RETVALUE);
  if (STAP_RETVALUE == 3)
      STAP_RETURN(0);
  STAP_RETVALUE ++;
%}
function string_ops (val) %{
  strlcpy (STAP_RETVALUE, STAP_ARG_val, MAXSTRINGLEN);
  strlcat (STAP_RETVALUE, &quot;one&quot;, MAXSTRINGLEN);
  if (strcmp (STAP_RETVALUE, &quot;three-two-one&quot;))
      STAP_RETURN(&quot;parameter should be three-two-&quot;);
%}
function no_ops () %{
    STAP_RETURN(); /* function inferred with no return value */
%}
</code></pre>
 </dd></dl>
<p> The function argument and return value types have to be inferred by the translator from the call sites in order for this to work. The user should examine C code generated for ordinary script-language functions in order to write compatible embedded-C ones. </p>
<p> The last place where embedded code is permitted is as an expression rvalue. In this case, the C code enclosed between <i>%{</i> and <i>%}</i> markers is interpreted as an ordinary expression value. It is assumed to be a normal 64-bit signed number, unless the marker <i>/* string */</i> is included, in which case it&#8217;s treated as a string. <br />
 </p>
<dl>
<dd> <pre><code>function add_one (val) {
  return val + %{ 1 %}
}
function add_string_two (val) {
  return val . %{ /* string */ &quot;two&quot; %}
}
</code></pre>
 </dd></dl>
<p> The embedded-C code may contain markers to assert optimization and safety properties. </p>
<dl>
<dt><i>/* pure */</i></dt>
<dd> <p> means that the C code has no side effects and may be elided entirely if its value is not used by script code. </p>
 </dd>
<dt><i>/* stable */</i></dt>
<dd> <p> means that the C code always has the same value (in any given probe handler invocation), so repeated calls may be automatically replaced by memoized values. Such functions must take no parameters, and also be <i>pure</i>. </p>
 </dd>
<dt><i>/* unprivileged */</i></dt>
<dd> <p> means that the C code is so safe that even unprivileged users are permitted to use it. </p>
 </dd>
<dt><i>/* myproc-unprivileged */</i></dt>
<dd> <p> means that the C code is so safe that even unprivileged users are permitted to use it, provided that the target of the current probe is within the user&#8217;s own process. </p>
 </dd>
<dt><i>/* guru */</i></dt>
<dd> <p> means that the C code is so unsafe that a systemtap user must specify <i>-g</i> (guru mode) to use this. </p>
 </dd>
<dt><i>/* unmangled */</i></dt>
<dd> <p> in an embedded-C function, means that the legacy (pre-1.8) argument access syntax should be made available inside the function. Hence, in addition to <i>STAP_ARG_foo</i> and <i>STAP_RETVALUE</i> one can use <i>THIS-&gt;foo</i> and <i>THIS-&gt;__retvalue</i> respectively inside the function. This is useful for quickly migrating code written for SystemTap version 1.7 and earlier. </p>
 </dd>
<dt><i>/* unmodified-fnargs */</i></dt>
<dd> <p> in an embedded-C function, means that the function arguments are not modified inside the function body. </p>
 </dd>
<dt><i>/* string */</i></dt>
<dd> <p> in embedded-C expressions only, means that the expression has <i>const char *</i> type and should be treated as a string value, instead of the default long numeric. </p>
 </dd></dl>
<p> Script level global variables may be accessed in embedded-C functions and blocks. To read or write the global variable <i>var</i> , the <i>/* pragma:read:var */</i> or <i>/* pragma:write:var */</i> marker must be first placed in the embedded-C function or block. This provides the macros <i>STAP_GLOBAL_GET_*</i> and <i>STAP_GLOBAL_SET_*</i> macros to allow reading and writing, respectively. For example: <br />
 </p>
<dl>
<dd> <pre><code>global var
global var2[100]
function increment() %{
    /* pragma:read:var */ /* pragma:write:var */
    /* pragma:read:var2 */ /* pragma:write:var2 */
    STAP_GLOBAL_SET_var(STAP_GLOBAL_GET_var()+1); //var++
    STAP_GLOBAL_SET_var2(1, 1, STAP_GLOBAL_GET_var2(1, 1)+1); //var2[1,1]++
%}
</code></pre>
 </dd></dl>
<p> Variables may be read and set in both embedded-C functions and expressions. Strings returned from embedded-C code are decayed to pointers. Variables must also be assigned at script level to allow for type inference. Map assignment does not return the value written, so chaining does not work. </p>
<h3>BUILT-INS</h3>
<p> A set of builtin probe point aliases are provided by the scripts installed in the directory specified in the <i><a href="/docs/linux/man/7-stappaths/">stappaths</a></i>(7) manual page. The functions are described in the <i>stapprobes</i>(3stap) manual page. </p>
<h2>PROCESSING</h2>
<p> The translator begins pass 1 by parsing the given input script, and all scripts (files named <i>*.stp</i>) found in a tapset directory. The directories listed with <code>-I</code> are processed in sequence, each processed in &quot;guru mode&quot;. For each directory, a number of subdirectories are also searched. These subdirectories are derived from the selected kernel version (the <code>-R</code> option), in order to allow more kernel-version-specific scripts to override less specific ones. For example, for a kernel version <i>2.6.12-23.FC3</i> the following patterns would be searched, in sequence: <i>2.6.12-23.FC3/*.stp</i>, <i>2.6.12/*.stp</i>, <i>2.6/*.stp</i>, and finally <i>*.stp</i>. Stopping the translator after pass 1 causes it to print the parse trees. </p>
<p> In pass 2, the translator analyzes the input script to resolve symbols and types. References to variables, functions, and probe aliases that are unresolved internally are satisfied by searching through the parsed tapset script files. If any tapset script file is selected because it defines an unresolved symbol, then the entirety of that file is added to the translator&#8217;s resolution queue. This process iterates until all symbols are resolved and a subset of tapset script files is selected. </p>
<p> Next, all probe point descriptions are validated against the wide variety supported by the translator. Probe points that refer to code locations (&quot;synchronous probe points&quot;) require the appropriate kernel debugging information to be installed. In the associated probe handlers, target-side variables (whose names begin with &quot;$&quot;) are found and have their run-time locations decoded. </p>
<p> Next, all probes and functions are analyzed for optimization opportunities, in order to remove variables, expressions, and functions that have no useful value and no side-effect. Embedded-C functions are assumed to have side-effects unless they include the magic string <code>/*&nbsp;<wbr>pure&nbsp;<wbr>*/</code>. Since this optimization can hide latent code errors such as type mismatches or invalid $context variables, it sometimes may be useful to disable the optimizations with the <code>-u</code> option. </p>
<p> Finally, all variable, function, parameter, array, and index types are inferred from context (literals and operators). Stopping the translator after pass 2 causes it to list all the probes, functions, and variables, along with all inferred types. Any inconsistent or unresolved types cause an error. </p>
<p> In pass 3, the translator writes C code that represents the actions of all selected script files, and creates a <i>Makefile</i> to build that into a kernel object. These files are placed into a temporary directory. Stopping the translator at this point causes it to print the contents of the C file. </p>
<p> In pass 4, the translator invokes the Linux kernel build system to create the actual kernel object file. This involves running <i>make</i> in the temporary directory, and requires a kernel module build system (headers, config and Makefiles) to be installed in the usual spot <i>/lib/modules/VERSION/build</i>. Stopping the translator after pass 4 is the last chance before running the kernel object. This may be useful if you want to archive the file. </p>
<p> In pass 5, the translator invokes the systemtap auxiliary program <i>staprun</i> program for the given kernel object. This program arranges to load the module then communicates with it, copying trace data from the kernel into temporary files, until the user sends an interrupt signal. Any run-time error encountered by the probe handlers, such as running out of memory, division by zero, exceeding nesting or runtime limits, results in a soft error indication. Soft errors in excess of MAXERRORS block of all subsequent probes (except error-handling probes), and terminate the session. Finally, <i>staprun</i> unloads the module, and cleans up. </p>
<h3>ABNORMAL TERMINATION</h3>
<p> One should avoid killing the stap process forcibly, for example with SIGKILL, because the stapio process (a child process of the stap process) and the loaded module may be left running on the system. If this happens, send SIGTERM or SIGINT to any remaining stapio processes, then use rmmod to unload the systemtap module. </p>
<h2>EXAMPLES</h2>
<p> See the <i>stapex</i>(3stap) manual page for a brief collection of samples, or a large set of installed samples under the systemtap documentation/testsuite directories. See <i>stappaths</i>(7stap) for the likely location of these on the system. </p>
<h2>CACHING</h2>
<p> The systemtap translator caches the pass 3 output (the generated C code) and the pass 4 output (the compiled kernel module) if pass 4 completes successfully. This cached output is reused if the same script is translated again assuming the same conditions exist (same kernel version, same systemtap version, etc.). Cached files are stored in the <i>$SYSTEMTAP_DIR/cache</i> directory. The cache can be limited by having the file <i>cache_mb_limit</i> placed in the cache directory (shown above) containing only an ASCII integer representing how many MiB the cache should not exceed. In the absence of this file, a default will be created with the limit set to 256MiB. This is a &#8216;soft&#8217; limit in that the cache will be cleaned after a new entry is added if the cache clean interval is exceeded, so the total cache size may temporarily exceed this limit. This interval can be specified by having the file <i>cache_clean_interval_s</i> placed in the cache directory (shown above) containing only an ASCII integer representing the interval in seconds. In the absence of this file, a default will be created with the interval set to 300 s. </p>
<h2>SAFETY AND SECURITY</h2>
<p> Systemtap may be used as a powerful administrative tool. It can expose kernel internal data structures and potentially private user information. (In <code>dyninst</code> runtime mode, this is not the case, see the <i>ALTERNATE RUNTIMES</i> section below.) </p>
<p> The translator asserts many safety constraints during compilation and more during run-time. It aims to ensure that no handler routine can run for very long, allocate boundless memory, perform unsafe operations, or in unintentionally interfere with the system. Uses of script global variables are automatically read/write locked as appropriate, to protect against manipulation by concurrent probe handlers. (Deadlocks are detected with timeouts. Use the <code>-t</code> flag to receive reports of excessive lock contention.) Experimenting with scripts is therefore generally <code>safe</code>. The guru-mode <code>-g</code> option allows administrators to bypass most safety measures, which permits invasive or state-changing operations, embedded-C code, and increases the risk of upset. By default, overload prevention is turned on for all modules. If you would like to disable overload processing, use the <code>--suppress-time-limits</code> option. </p>
<p> Errors that are caught at run time normally result in a clean script shutdown and a pass-5 error message. The <code>--suppress-handler-errors</code> option lets scripts tolerate soft errors without shutting down. </p>
<h3>PERMISSIONS</h3>
<p> For the normal linux-kernel-module runtime, to run the kernel objects systemtap builds, a user must be one of the following: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> the root user; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> a member of the <i>stapdev</i> and <i>stapusr</i> groups; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> a member of the <i>stapsys</i> and <i>stapusr</i> groups; or </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> a member of the <i>stapusr</i> group. </p>
 </dd></dl>
<p> The root user or a user who is a member of both the <i>stapdev</i> and <i>stapusr</i> groups can build and run any systemtap script. </p>
<p> A user who is a member of both the <i>stapsys</i> and <i>stapusr</i> groups can only use pre-built modules under the following conditions: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The module has been signed by a trusted signer. Trusted signers are normally systemtap compile-servers which sign modules when the <i>--privilege</i> option is specified by the client. See the <i><a href="/docs/linux/man/8-stap-server/">stap-server</a></i>(8) manual page for more information. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The module was built using the <i>--privilege=stapsys</i> or the <i>--privilege=stapusr</i> options. </p>
 </dd></dl>
<p> Members of only the <i>stapusr</i> group can only use pre-built modules under the following conditions: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The module is located in the /lib/modules/VERSION/systemtap directory. This directory must be owned by root and not be world writable. </p>
 </dd></dl>
<p> or </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The module has been signed by a trusted signer. Trusted signers are normally systemtap compile-servers which sign modules when the <i>--privilege</i> option is specified by the client. See the <i><a href="/docs/linux/man/8-stap-server/">stap-server</a></i>(8) manual page for more information. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The module was built using the FI--privilege=stapusr option. </p>
 </dd></dl>
<p> The kernel modules generated by <i>stap</i> program are run by the <i>staprun</i> program. The latter is a part of the Systemtap package, dedicated to module loading and unloading (but only in the white zone), and kernel-to-user data transfer. Since <i>staprun</i> does not perform any additional security checks on the kernel objects it is given, it would be unwise for a system administrator to add untrusted users to the <i>stapdev</i> or <i>stapusr</i> groups. </p>
<h3>SECUREBOOT</h3>
<p> If the current system has SecureBoot turned on in the UEFI firmware, all kernel modules must be signed. (Some kernels may allow disabling SecureBoot long after booting with a key sequence such as SysRq-X, making it unnecessary to sign modules.) The systemtap compile server can sign modules with a MOK (Machine Owner Key) that it has in common with a client system. See the following wiki page for more details: </p>
<dl>
<dd> <p> <code><a rel="nofollow" href="https://sourceware.org/systemtap/wiki/SecureBoot">https://sourceware.org/systemtap/wiki/SecureBoot</a></code> </p>
 </dd></dl>
<h3>RESOURCE LIMITS</h3>
<p> Many resource use limits are set by macros in the generated C code. These may be overridden with <code>-D</code> flags. A selection of these is as follows: </p>
<dl>
<dt>MAXNESTING</dt>
<dd> <p> Maximum number of nested function calls. Default determined by script analysis, with a bonus 10 slots added for recursive scripts. </p>
 </dd>
<dt>MAXSTRINGLEN</dt>
<dd> <p> Maximum length of strings, default 128. </p>
 </dd>
<dt>MAXTRYLOCK</dt>
<dd> <p> Maximum number of iterations to wait for locks on global variables before declaring possible deadlock and skipping the probe, default 1000. </p>
 </dd>
<dt>MAXACTION</dt>
<dd> <p> Maximum number of statements to execute during any single probe hit (with interrupts disabled), default 1000. Note that for straight-through probe handlers lacking loops or recursion, due to optimization, this parameter may be interpreted too conservatively. </p>
 </dd>
<dt>MAXACTION_INTERRUPTIBLE</dt>
<dd> <p> Maximum number of statements to execute during any single probe hit which is executed with interrupts enabled (such as begin/end probes), default (MAXACTION * 10). </p>
 </dd>
<dt>MAXBACKTRACE</dt>
<dd> <p> Maximum number of stack frames that will be be processed by the stap runtime unwinder as produced by the backtrace functions in the [u]context-unwind.stp tapsets, default 20. </p>
 </dd>
<dt>MAXMAPENTRIES</dt>
<dd> <p> Maximum number of rows in any single global array, default 2048. Individual arrays may be declared with a larger or smaller limit instead: <br />
 </p>
 </dd>
<dl>
<dd> <pre><code>global big[10000],little[5]
</code></pre>
 </dd></dl>
<p> or denoted with <i>%</i> to make them wrap-around (replace old entries) automatically, as in <br />
 </p>
<dl>
<dd> <pre><code>global big%
</code></pre>
 </dd></dl>
<p> or both. </p>
<dt>MAPHASHBIAS</dt>
<dd> <p> The number of powers-of-two to add or subtract from the natural size of the hash table backing each global associative array. Default is 0. Try small positive numbers to get extra performance at the cost of more memory consumption, because that should reduce hash table collisions. Try small negative numbers for the opposite tradeoff. </p>
 </dd>
<dt>MAXERRORS</dt>
<dd> <p> Maximum number of soft errors before an exit is triggered, default 0, which means that the first error will exit the script. Note that with the <code>--suppress-handler-errors</code> option, this limit is not enforced. </p>
 </dd>
<dt>MAXSKIPPED</dt>
<dd> <p> Maximum number of skipped probes before an exit is triggered, default 100. Running systemtap with -t (timing) mode gives more details about skipped probes. With the default -DINTERRUPTIBLE=1 setting, probes skipped due to reentrancy are not accumulated against this limit. Note that with the <code>--suppress-handler-errors</code> option, this limit is not enforced. </p>
 </dd>
<dt>MINSTACKSPACE</dt>
<dd> <p> Minimum number of free kernel stack bytes required in order to run a probe handler, default 1024. This number should be large enough for the probe handler&#8217;s own needs, plus a safety margin. </p>
 </dd>
<dt>MAXUPROBES</dt>
<dd> <p> Maximum number of concurrently armed user-space probes (uprobes), default somewhat larger than the number of user-space probe points named in the script. This pool needs to be potentially large because individual uprobe objects (about 64 bytes each) are allocated for each process for each matching script-level probe. </p>
 </dd>
<dt>STP_MAXMEMORY</dt>
<dd> <p> Maximum amount of memory (in kilobytes) that the systemtap module should use, default unlimited. The memory size includes the size of the module itself, plus any additional allocations. This only tracks direct allocations by the systemtap runtime. This does not track indirect allocations (as done by kprobes/uprobes/etc. internals). </p>
 </dd>
<dt>STP_OVERLOAD_THRESHOLD, STP_OVERLOAD_INTERVAL</dt>
<dd> <p> Maximum number of machine cycles spent in probes on any cpu per given interval, before an overload condition is declared and the script shut down. The defaults are 500 million and 1 billion, so as to limit stap script cpu consumption at around 50%. </p>
 </dd>
<dt>STP_PROCFS_BUFSIZE</dt>
<dd> <p> Size of procfs probe read buffers (in bytes). Defaults to <i>MAXSTRINGLEN</i>. This value can be overridden on a per-procfs file basis using the procfs read probe <i>.maxsize(MAXSIZE)</i> parameter. </p>
 </dd></dl>
<p> With scripts that contain probes on any interrupt path, it is possible that those interrupts may occur in the middle of another probe handler. The probe in the interrupt handler would be skipped in this case to avoid reentrance. To work around this issue, execute stap with the option <code>-DINTERRUPTIBLE=0</code> to mask interrupts throughout the probe handler. This does add some extra overhead to the probes, but it may prevent reentrance for common problem cases. However, probes in NMI handlers and in the callpath of the stap runtime may still be skipped due to reentrance. </p>
<p> In case something goes wrong with <i>stap</i> or <i>staprun</i> after a probe has already started running, one may safely kill both user processes, and remove the active probe kernel module with <i>rmmod</i>. Any pending trace messages may be lost. </p>
<h2>UNPRIVILEGED USERS</h2>
<p> Systemtap exposes kernel internal data structures and potentially private user information. Because of this, use of systemtap&#8217;s full capabilities are restricted to root and to users who are members of the groups stapdev and stapusr. </p>
<p> However, a restricted set of systemtap&#8217;s features can be made available to trusted, unprivileged users. These users are members of the group stapusr only, or members of the groups stapusr and stapsys. These users can load systemtap modules which have been compiled and certified by a trusted systemtap compile-server. See the descriptions of the options <i>--privilege</i> and <i>--use-server</i>. See <i>README.unprivileged</i> in the systemtap source code for information about setting up a trusted compile server. </p>
<p> The restrictions enforced when <i>--privilege=stapsys</i> is specified are designed to prevent unprivileged users from: </p>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> harming the system maliciously. </p>
 </dd></dl>
</dl>
<p> The restrictions enforced when <i>--privilege=stapusr</i> is specified are designed to prevent unprivileged users from: </p>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> harming the system maliciously. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> gaining access to information which would not normally be available to an unprivileged user. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> disrupting the performance of processes owned by other users of the system. Some overhead to the system in general is unavoidable since the unprivileged user&#8217;s probes will be triggered at the appropriate times. What we would like to avoid is targeted interruption of another user&#8217;s processes which would not normally be possible by an unprivileged user. </p>
 </dd></dl>
</dl>
<h3>PROBE RESTRICTIONS</h3>
<p> A member of the groups stapusr and stapsys may use all probe points. </p>
<p> A member of only the group stapusr may use only the following probes: </p>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> begin, begin(n) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> end, end(n) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> error(n) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> never </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> process.*, where the target process is owned by the user. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> timer.{jiffies,s,sec,ms,msec,us,usec,ns,nsec}(n)* </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> timer.hz(n) </p>
 </dd></dl>
</dl>
<h3>SCRIPT LANGUAGE RESTRICTIONS</h3>
<p> The following scripting language features are unavailable to all unprivileged users: </p>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> any feature enabled by the Guru Mode (-g) option. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> embedded C code. </p>
 </dd></dl>
</dl>
<h3>RUNTIME RESTRICTIONS</h3>
<p> The following runtime restrictions are placed upon all unprivileged users: </p>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Only the default runtime code (see <i>-R</i>) may be used. </p>
 </dd></dl>
</dl>
<p> Additional restrictions are placed on members of only the group stapusr: </p>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Probing of processes owned by other users is not permitted. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Access of kernel memory (read and write) is not permitted. </p>
 </dd></dl>
</dl>
<h3>COMMAND LINE OPTION RESTRICTIONS</h3>
<p> Some command line options provide access to features which must not be available to all unprivileged users: </p>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> -g may not be specified. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The following options may not be used by the compile-server client: <br />
 </p>
 </dd>
<dl>
<dd> <pre><code>    -a, -B, -D, -I, -r, -R
</code></pre>
 </dd></dl>
<h3>ENVIRONMENT RESTRICTIONS</h3>
<p> The following environment variables must not be set for all unprivileged users: <br />
 </p>
<dl>
<dd> <pre><code>SYSTEMTAP_RUNTIME
SYSTEMTAP_TAPSET
SYSTEMTAP_DEBUGINFO_PATH
</code></pre>
 </dd></dl>
<h3>TAPSET RESTRICTIONS</h3>
<p> In general, tapset functions are only available for members of the group stapusr when they do not gather information that an ordinary program running with that user&#8217;s privileges would be denied access to. </p>
<p> There are two categories of unprivileged tapset functions. The first category consists of utility functions that are unconditionally available to all users; these include such things as: <br />
 </p>
<dl>
<dd> <pre><code>cpu:long ()
exit ()
str_replace:string (prnt_str:string, srch_str:string, rplc_str:string)
</code></pre>
 </dd></dl>
<p> The second category consists of so-called <i>myproc-unprivileged</i> functions that can only gather information within their own processes. Scripts that wish to use these functions must test the result of the tapset function <i>is_myproc</i> and only call these functions if the result is 1. The script will exit immediately if any of these functions are called by an unprivileged user within a probe within a process which is not owned by that user. Examples of <i>myproc-unprivileged</i> functions include: <br />
 </p>
<dl>
<dd> <pre><code>print_usyms (stk:string)
user_int:long (addr:long)
usymname:string (addr:long)
</code></pre>
 </dd></dl>
<p> A compile error is triggered when any function not in either of the above categories is used by members of only the group stapusr. </p>
<p> No other built-in tapset functions may be used by members of only the group stapusr. </p>
<h2>ALTERNATE RUNTIMES</h2>
<p> As described above, systemtap&#8217;s default runtime mode involves building and loading kernel modules, with various security tradeoffs presented. Systemtap now includes a new prototype backend, selected with <i>--runtime=dyninst</i>, which uses Dyninst to instrument a user&#8217;s own processes at runtime. This backend does not use kernel modules, and does not require root privileges, but is restricted with respect to the kinds of probes and other constructs that a script may use. </p>
<p> The <i>dyninst</i> runtime operates in target-attach mode, so it does require a <i>-c COMMAND</i> or <i>-x PID</i> process. For example: <br />
 </p>
<dl>
<dd> <pre><code>stap --runtime=dyninst -c 'stap -V' \
     -e 'probe process.function(&quot;main&quot;)
         { println(&quot;hi from dyninst!&quot;) }'
</code></pre>
 </dd></dl>
<p> It may be necessary to disable a conflicting selinux check with <br />
 </p>
<dl>
<dd> <pre><code># setsebool allow_execstack 1
</code></pre>
 </dd></dl>
<h2>EXIT STATUS</h2>
<p> The systemtap translator generally returns with a success code of 0 if the requested script was processed and executed successfully through the requested pass. Otherwise, errors may be printed to stderr and a failure code is returned. Use <i>-v</i> or <i>-vp N</i> to increase (global or per-pass) verbosity to identify the source of the trouble. </p>
<p> In listings mode (<i>-l</i> and <i>-L</i>), error messages are normally suppressed. A success code of 0 is returned if at least one matching probe was found. </p>
<p> A script executing in pass 5 that is interrupted with ^C / SIGINT is considered to be successful. </p>
<h2>DEPRECATION</h2>
<p> Over time, some features of the script language and the tapset library may undergo incompatible changes, so that a script written against an old version of systemtap may no longer run. In these cases, it may help to run systemtap with the <i>--compatible VERSION</i> flag, specifying the last known working version. Running systemtap with the <i>--check-version</i> flag will output a warning if any possible incompatible elements have been parsed. Deprecation historical details may be found in the NEWS file. </p>
<p> The purpose of deprecation facility is to improve the experience of scripts written for newer versions of systemtap (by adding better alternatives and removing conflicting or messy older alternatives), while at the same time permitting scripts written for older versions of systemtap to continue running. Deprecation is thus intended a <i>service to users</i> (and an inconvenience to systemtap&#8217;s developers), rather than the other way around. </p>
<p> Please note that underscore-prefixed identifiers in the tapset sometimes undergo such changes that are difficult to preserve compatibility for, even with the deprecation mechanisms. Avoid relying on these in your scripts; instead propose them for promotion to non-underscored status. </p>
<h2>FILES</h2>
<dl>
<dt>Important files and their corresponding paths can be located in the </dt>
<dd> <p> stappaths (7) manual page. </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<pre><code>
 stapprobes (3stap),
 function::* (3stap),
 probe::* (3stap),
 tapset::* (3stap),
 stappaths (7),
 staprun (8),
 stapdyn (8),
 systemtap (8),
 stapvars (3stap),
 stapex (3stap),
 stap-server (8),
 stap-prep (1),
 stapref (1),
 awk (1),
 gdb (1)
</code></pre>
<h2>BUGS</h2>
<p> Use the Bugzilla link of the project web page or our mailing list. <code><a rel="nofollow" href="http://sourceware.org/systemtap/">http://sourceware.org/systemtap/</a></code>, <code>&lt;systemtap [at] sourceware.org&gt;</code>. </p>
<p> <i>error::reporting</i>(7stap), <code><a rel="nofollow" href="https://sourceware.org/systemtap/wiki/HowToReportBugs">https://sourceware.org/systemtap/wiki/HowToReportBugs</a></code> </p>
