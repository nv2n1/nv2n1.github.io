---
title: "stap(1)"
name: "stap"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stap/"
description: "stap – systemtap script translator/driver"
---

<h2>NAME</h2>
<p> stap &#8211; systemtap script translator/driver </p>
<h2>SYNOPSIS</h2>
<p> <code>stap</code> [ <i>OPTIONS</i> ] <i>FILENAME</i> [ <i>ARGUMENTS</i> ]<br />
 <code>stap</code> [ <i>OPTIONS</i> ] <code>&#8211;</code> [ <i>ARGUMENTS</i> ]<br />
 <code>stap</code> [ <i>OPTIONS</i> ] <code>-e</code><i> SCRIPT</i> [ <i>ARGUMENTS</i> ]<br />
 <code>stap</code> [ <i>OPTIONS</i> ] <code>-l</code><i> PROBE</i> [ <i>ARGUMENTS</i> ]<br />
 <code>stap</code> [ <i>OPTIONS</i> ] <code>-L</code><i> PROBE</i> [ <i>ARGUMENTS</i> ]<br />
 <code>stap</code> [ <i>OPTIONS</i> ] <code>&#8211;dump-probe-types</code><br />
 <code>stap</code> [ <i>OPTIONS</i> ] <code>&#8211;dump-probe-aliases</code><br />
 <code>stap</code> [ <i>OPTIONS</i> ] <code>&#8211;dump-functions</code> </p>
<h2>DESCRIPTION</h2>
<p> The <i>stap</i> program is the front-end to the Systemtap tool. It accepts probing instructions written in a simple domain-specific language, translates those instructions into C code, compiles this C code, and loads the resulting module into a running Linux kernel or a DynInst user-space mutator, to perform the requested system trace/probe functions. You can supply the script in a named file (FILENAME), from standard input (use &#8211; instead of FILENAME), or from the command line (using -e SCRIPT). The program runs until it is interrupted by the user, or if the script voluntarily invokes the <i>exit()</i> function, or by sufficient number of soft errors. </p>
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
<p> In some cases, the default value of an option depends on particular system configuration and thus can&#8217;t be mentioned here directly. In some of those cases running &quot;stap &#8211;help&quot; might display the default. </p>
<dl>
<dt><code>&#8211;</code></p>
<dd> Use standard input instead of a given FILENAME as probe language input, unless -e SCRIPT is given.</p>
<dt><code>-h &#8211;help</code></p>
<dd> Show help message.</p>
<dt><code>-V &#8211;version</code></p>
<dd> Show version message.</p>
<dt><code>-p</code><i> NUM</i></p>
<dd> Stop after pass NUM. The passes are numbered 1-5: parse, elaborate, translate, compile, run. See the <code>PROCESSING</code> section for details.</p>
<dt><code>-v</code></p>
<dd> Increase verbosity for all passes. Produce a larger volume of informative (?) output each time option repeated.</p>
<dt><code>&#8211;vp ABCDE</code></p>
<dd> Increase verbosity on a per-pass basis. For example, &quot;&#8211;vp 002&quot; adds 2 units of verbosity to pass 3 only. The combination &quot;-v &#8211;vp 00004&quot; adds 1 unit of verbosity for all passes, and 4 more for pass 5.</p>
<dt><code>-k</code></p>
<dd> Keep the temporary directory after all processing. This may be useful in order to examine the generated C code, or to reuse the compiled kernel object.</p>
<dt><code>-g</code></p>
<dd> Guru mode. Enable parsing of unsafe expert-level constructs like embedded C.</p>
<dt><code>-P</code></p>
<dd> Prologue-searching mode. This is equivalent to &#8211;prologue-searching=always. Activate heuristics to work around incorrect debugging information for function parameter $context variables.</p>
<dt><code>-u</code></p>
<dd> Unoptimized mode. Disable unused code elision and many other optimizations during elaboration / translation.</p>
<dt><code>-w</code></p>
<dd> Suppressed warnings mode. Disables all warning messages.</p>
<dt><code>-W</code></p>
<dd> Treat all warnings as errors.</p>
<dt><code>-b</code></p>
<dd> Use bulk mode (percpu files) for kernel-to-user data transfer. Use the <i>stap-merge</i> program to multiplex them back together later.</p>
<dt><code>-i &#8211;interactive</code></p>
<dd> Interactive mode. Enable an interface to build the systemtap script incrementally and interactively.</p>
<dt><code>-t</code></p>
<dd> Collect timing information on the number of times probe executes and average amount of time spent in each probe-point. Also shows the derivation for each probe-point.</p>
<dt><code>-s</code><i> NUM</i></p>
<dd> Use NUM megabyte buffers for kernel-to-user data transfer. On a multiprocessor in bulk mode, this is a per-processor amount.</p>
<dt><code>-I</code><i> DIR</i></p>
<dd> Add the given directory to the tapset search directory. See the description of pass 2 for details.</p>
<dt><code>-D</code><i> NAME=VALUE</i></p>
<dd> Add the given C preprocessor directive to the module Makefile. These can be used to override limit parameters described below.</p>
<dt><code>-B</code><i> NAME=VALUE</i></p>
<dd> In kernel-runtime mode, add the given make directive to the kernel module build&#8217;s make invocation. These can be used to add or override kconfig options. For example, use </p>
<dl>
<dt>
<dd>
<pre>
<code>-B CONFIG_DEBUG_INFO=y</code>
</pre>
</dl>
<p> to add debugging information.</p>
<dt><code>-B</code><i> FLAG</i></p>
<dd> In dyninst-runtime mode, add the given parameter to the compiler CFLAGS used for building the dyninst shared library. For example, use </p>
<dl>
<dt>
<dd>
<pre>
<code>-B -g</code>
</pre>
</dl>
<p> to add debugging information.</p>
<dt><code>-a</code><i> ARCH</i></p>
<dd> Use a cross-compilation mode for the given target architecture. This requires access to the cross-compiler and the kernel build tree, and goes along with the </p>
<dl>
<dt>
<dd>
<pre>
<code>-B CROSS_COMPILE=arch-tool-prefix-</code>
and
<code>-r /build/tree</code>
</pre>
</dl>
<p> options.</p>
<dt><code>&#8211;modinfo</code><i> NAME=VALUE</i></p>
<dd> Add the name/value pair as a MODULE_INFO macro call to the generated module. This may be useful to inform or override various module-related checks in the kernel.</p>
<dt><code>-G</code><i> NAME=VALUE</i></p>
<dd> Sets the value of global variable NAME to VALUE when staprun is invoked. This applies to scalar variables declared global in the script/tapset.</p>
<dt><code>-R</code><i> DIR</i></p>
<dd> Look for the systemtap runtime sources in the given directory. Your DIR default can be seen using &quot;stap &#8211;help&quot;.</p>
<dt><code>-r</code><i> /DIR</i></p>
<dd> Build for kernel in given build tree. Can also be set with the <i>SYSTEMTAP_RELEASE</i> environment variable.</p>
<dt><code>-r</code><i> RELEASE</i></p>
<dd> Build for kernel in build tree <code>/lib/modules/RELEASE/build</code>. Can also be set with the <i>SYSTEMTAP_RELEASE</i> environment variable.</p>
<dt><code>-m</code><i> MODULE</i></p>
<dd> Use the given name for the generated kernel object module, instead of a unique randomized name. The generated kernel object module is copied to the current directory.</p>
<dt><code>-d</code><i> MODULE</i></p>
<dd> Add symbol/unwind information for the given module into the kernel object module. This may enable symbolic tracebacks from those modules/programs, even if they do not have an explicit probe placed into them.</p>
<dt><code>&#8211;ldd</code></p>
<dd> Add symbol/unwind information for all user-space shared libraries suspected by ldd to be necessary for user-space binaries being probed or listed with the -d option. Caution: this can make the probe modules considerably larger. Note that this option does not deal with kernel-space modules: see instead &#8211;all-modules below.</p>
<dt><code>&#8211;all-modules</code></p>
<dd> Equivalent to specifying &quot;-dkernel&quot; and a &quot;-d&quot; for each kernel module that is currently loaded. Caution: this can make the probe modules considerably larger.</p>
<dt><code>-o</code><i> FILE</i></p>
<dd> Send standard output to named file. In bulk mode, percpu files will start with FILE_ (FILE_cpu with -F) followed by the cpu number. This supports <a href="/docs/linux/man/3-strftime/">strftime</a>(3) formats for FILE.</p>
<dt><code>-c</code><i> CMD</i></p>
<dd> Start the probes, run CMD, and exit when CMD finishes. This also has the effect of setting target() to the pid of the command ran.</p>
<dt><code>-x</code><i> PID</i></p>
<dd> Sets target() to PID. This allows scripts to be written that filter on a specific process. Scripts run independent of the PID&#8217;s lifespan.</p>
<dt><code>-e</code><i> SCRIPT</i></p>
<dd> Run the given SCRIPT specified on the command line.</p>
<dt><code>-E</code><i> SCRIPT</i></p>
<dd> Run the given SCRIPT specified. This SCRIPT is run in addition to the main script specified, through -e, or as a script file. This option can be repeated to run multiple scripts, and can be used in listing mode (-l/-L).</p>
<dt><code>-l</code><i> PROBE</i></p>
<dd> Instead of running a probe script, just list all available probe points matching the given single probe point. The pattern may include wildcards and aliases, but not comma-separated multiple probe points. The process result code will indicate failure if there are no matches.</p>
<dt><code>-L</code><i> PROBE</i></p>
<dd> Similar to &quot;-l&quot;, but list probe points and script-level local variables.</p>
<dt><code>-F</code></p>
<dd> Without -o option, load module and start probes, then detach from the module leaving the probes running. With -o option, run staprun in background as a daemon and show its pid.</p>
<dt><code>-S</code><i> size[,N]</i></p>
<dd> Sets the maximum size of output file and the maximum number of output files. If the size of output file will exceed <code>size</code> , systemtap switches output file to the next file. And if the number of output files exceed <code>N</code> , systemtap removes the oldest output file. You can omit the second argument.</p>
<dt><code>-T</code><i> TIMEOUT</i></p>
<dd> Exit the script after TIMEOUT seconds.</p>
<dt><code>&#8211;skip-badvars</code></p>
<dd> Ignore unresolvable or run-time-inaccessible context variables and substitute with 0, without errors. </p>
<dt><code>&#8211;prologue-searching</code>[=<i>WHEN</i>]</p>
<dd> Prologue-searching mode. Activate heuristics to work around incorrect debugging information for function parameter $context variables. WHEN can be either &quot;never&quot;, &quot;always&quot;, or &quot;auto&quot; (i.e. enabled by heuristic). If WHEN is missing, then &quot;always&quot; is assumed. If the option is missing, then &quot;auto&quot; is assumed. </p>
<dt><code>&#8211;suppress-handler-errors</code></p>
<dd> Wrap all probe handlers into something like this </p>
<dl>
<dt>
<dd>
<pre><code>
try {
    ...
} catch {
    next
}
</code></pre>
</dl>
<p> block, which causes any runtime errors to be quietly suppressed. Suppressed errors do not count against <code>MAXERRORS</code> limits. In this mode, the <code>MAXSKIPPED</code> limits are also suppressed, so that many errors and skipped probes may be accumulated during a script&#8217;s runtime. Any overall counts will still be reported at shutdown. </p>
<dt><code>&#8211;compatible</code><i> VERSION</i></p>
<dd> Suppress recent script language or tapset changes which are incompatible with given older version of systemtap. This may be useful if a much older systemtap script fails to run. See the DEPRECATION section for more details. </p>
<dt><code>&#8211;check-version</code></p>
<dd> This option is used to check if the active script has any constructs that may be systemtap version specific. See the DEPRECATION section for more details. </p>
<dt><code>&#8211;clean-cache</code></p>
<dd> This option prunes stale entries from the cache directory. This is normally done automatically after successful runs, but this option will trigger the cleanup manually and then exit. See the CACHING section for more details about cache limits. </p>
<dt><code>&#8211;color</code>[=<i>WHEN</i>], <code>&#8211;colour</code>[=<i>WHEN</i>]</p>
<dd> This option controls coloring of error messages. WHEN can be either &quot;never&quot;, &quot;always&quot;, or &quot;auto&quot; (i.e. enable only if at a terminal). If WHEN is missing, then &quot;always&quot; is assumed. If the option is missing, then &quot;auto&quot; is assumed. </p>
<p> Colors can be modified using the SYSTEMTAP_COLORS environment variable. The format must be of the form <code>key1=val1:key2=val2:key3=val3</code> &#8230;etc. Valid keys are &quot;error&quot;, &quot;warning&quot;, &quot;source&quot;, &quot;caret&quot;, and &quot;token&quot;. Values constitute Select Graphic Rendition (SGR) parameter(s). Consult the documentation of your terminal for the SGRs it supports. As an example, the default colors would be expressed as <code>error=01;31:warning=00;33:source=00;34:caret=01:token=01</code>. If SYSTEMTAP_COLORS is absent, the default colors will be used. If it is empty or invalid, coloring is turned off. </p>
<dt><code>&#8211;disable-cache</code></p>
<dd> This option disables all use of the cache directory. No files will be either read from or written to the cache. </p>
<dt><code>&#8211;poison-cache</code></p>
<dd> This option treats files in the cache directory as invalid. No files will be read from the cache, but resulting files from this run will still be written to the cache. This is meant as a troubleshooting aid when stap&#8217;s cached behavior seems to be misbehaving. If it helped, there is a probably a bug in systemtap that the developers would like you to report. </p>
<dt><code>&#8211;privilege</code>[=<i>stapusr</i> | =<i>stapsys</i> | =<i>stapdev</i>]</p>
<dd> This option instructs <i>stap</i> to examine the script looking for constructs which are not allowed for the specified privilege level (see <i>UNPRIVILEGED USERS</i>). Compilation fails if any such constructs are used. If <i>stapusr</i> or <i>stapsys</i> are specified when using a compile server (see <i>&#8211;use-server</i>), the server will examine the script and, if compilation succeeds, the server will cryptographically sign the resulting kernel module, certifying that is it safe for use by users at the specified privilege level. </p>
<p> If <i>&#8211;privilege</i> has not been specified, <i>-pN</i> has not been specified with N &lt; 5, and the invoking user is not <i>root</i>, and is not a member of the group <i>stapdev</i>, then <i>stap</i> will automatically add the appropriate <i>&#8211;privilege</i> option to the options already specified. </p>
<dt><code>&#8211;unprivileged</code></p>
<dd> This option is equivalent to <i>&#8211;privilege=stapusr</i>. </p>
<dt><code>&#8211;use-server</code>[=<i>HOSTNAME</i>[<i>:PORT</i>] | =<i>IP_ADDRESS</i>[<i>:PORT</i>] | =<i>CERT_SERIAL</i>]</p>
<dd> Specify compile-server(s) to be used for compilation and/or in conjunction with <i>&#8211;list-servers</i> and <i>&#8211;trust-servers</i> (see below) for listing. If no argument is supplied, then the default in unprivileged mode (see <i>&#8211;privilege</i>) is to select compatible servers which are trusted as SSL peers and as module signers and currently online. Otherwise the default is to select compatible servers which are trusted as SSL peers and currently online. <i>&#8211;use-server</i> may be specified more than once, in which case a list of servers is accumulated in the order specified. Servers may be specified by host name, ip address, or by certificate serial number (obtained using <i>&#8211;list-servers</i>). The latter is most commonly used when adding or revoking trust in a server (see <i>&#8211;trust-servers</i> below). If a server is specified by host name or ip address, then an optional port number may be specified. This is useful for accessing servers which are not on the local network or to specify a particular server. </p>
<p> IP addresses may be IPv4 or IPv6 addresses. </p>
<p> If a particular IPv6 address is link local and exists on more than one interface, the intended interface may be specified by appending the address with a percent sign (%) followed by the intended interface name. For example, &quot;fe80::5eff:35ff:fe07:55ca%eth0&quot;. </p>
<p> In order to specify a port number with an IPv6 address, it is necessary to enclose the IPv6 address in square brackets ([]) in order to separate the port number from the rest of the address. For example, &quot;[fe80::5eff:35ff:fe07:55ca]:5000&quot; or &quot;[fe80::5eff:35ff:fe07:55ca%eth0]:5000&quot;. </p>
<p> If <i>&#8211;use-server</i> has not been specified, <i>-pN</i> has not been specified with N &lt; 5, and the invoking user not <i>root</i>, is not a member of the group <i>stapdev</i>, but is a member of the group <i>stapusr</i>, then <i>stap</i> will automatically add <i>&#8211;use-server</i> to the options already specified. </p>
<dt><code>&#8211;use-server-on-error</code>[=<code>yes</code>|=<code>no</code>]</p>
<dd> Instructs stap to retry compilation of a script using a compile server if compilation on the local host fails in a manner which suggests that it might succeed using a server. If this option is not specified, the default is <i>no</i>. If no argument is provided, then the default is <i>yes</i>. Compilation will be retried for certain types of errors (e.g. insufficient data or resources) which may not occur during re-compilation by a compile server. Compile servers will be selected automatically for the re-compilation attempt as if <i>&#8211;use-server</i> was specified with no arguments. </p>
<dt><code>&#8211;list-servers</code><i>[=SERVERS]</i></p>
<dd> Display the status of the requested <i>SERVERS</i>, where <i>SERVERS</i> is a comma-separated list of server attributes. The list of attributes is combined to filter the list of servers displayed. Supported attributes are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>all</code></p>
<dd> specifies all known servers (trusted SSL peers, trusted module signers, online servers).</p>
<dt><code>specified</code></p>
<dd> specifies servers specified using <i>&#8211;use-server</i>.</p>
<dt><code>online</code></p>
<dd> filters the output by retaining information about servers which are currently online.</p>
<dt><code>trusted</code></p>
<dd> filters the output by retaining information about servers which are trusted as SSL peers.</p>
<dt><code>signer</code></p>
<dd> filters the output by retaining information about servers which are trusted as module signers (see <i>&#8211;privilege</i>).</p>
<dt><code>compatible</code></p>
<dd> filters the output by retaining information about servers which are compatible with the current kernel release and architecture.</dl>
</dl>
<dt>
<dd> If no argument is provided, then the default is <code>specified</code>. If no servers were specified using <i>&#8211;use-server</i>, then the default servers for <i>&#8211;use-server</i> are listed. </p>
<p> Note that <i>&#8211;list-servers</i> uses the <i>avahi-daemon</i> service to detect online servers. If this service is not available, then <i>&#8211;list-servers</i> will fail to detect any <i>online</i> servers. In order for <i>&#8211;list-servers</i> to detect servers listening on IPv6 addresses, the <i>avahi-daemon</i> configuration file <i>/etc/avahi/avahi-daemon.conf</i> must contain an active &quot;use-ipv6=yes&quot; line. The service must be restarted after adding this line in order for IPv6 to be enabled. </p>
<dt><code>&#8211;trust-servers</code><i>[=TRUST_SPEC]</i></p>
<dd> Grant or revoke trust in compile-servers, specified using <i>&#8211;use-server</i> as specified by TRUST_SPEC, where TRUST_SPEC is a comma-separated list specifying the trust which is to be granted or revoked. Supported elements are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>ssl</code></p>
<dd> trust the specified servers as SSL peers.</p>
<dt><code>signer</code></p>
<dd> trust the specified servers as module signers (see <i>&#8211;privilege</i>). Only root can specify <code>signer.</code></p>
<dt><code>all-users</code></p>
<dd> grant trust as an ssl peer for all users on the local host. The default is to grant trust as an ssl peer for the current user only. Trust as a module signer is always granted for all users. Only root can specify <code>all-users</code>.</p>
<dt><code>revoke</code></p>
<dd> revoke the specified trust. The default is to grant it.</p>
<dt><code>no-prompt</code></p>
<dd> do not prompt the user for confirmation before carrying out the requested action. The default is to prompt the user for confirmation.</dl>
</dl>
<dt>
<dd> If no argument is provided, then the default is <code>ssl</code>. If no servers were specified using <i>&#8211;use-server</i>, then no trust will be granted or revoked.</p>
<dt>
<dd> Unless <code>no-prompt</code> has been specified, the user will be prompted to confirm the trust to be granted or revoked before the operation is performed. </p>
<dt><code>&#8211;dump-probe-types</code></p>
<dd> Dumps a list of supported probe types and exits. If <i>&#8211;privilege=stapusr</i> is also specified, the list will be limited to probe types available to unprivileged users. </p>
<dt><code>&#8211;dump-probe-aliases</code></p>
<dd> Dumps a list of all probe aliases found in library files and exits. </p>
<dt><code>&#8211;dump-functions</code></p>
<dd> Dumps a list of all the public functions found in library files and exits. Also includes their parameters and types. A function of type &#8216;unknown&#8217; indicates a function that does not return a value. Note that not all function/parameter types may be resolved (these are also shown by &#8216;unknown&#8217;). This features is very memory-intensive and thus may not work properly with <i>&#8211;use-server</i> if the target server imposes an rlimit on process memory (i.e. through the <i>~stap-server/.systemtap/rc</i> configuration file, see <i><a href="/docs/linux/man/8-stap-server/">stap-server</a></i>(8)). </p>
<dt><code>&#8211;remote</code><i> URL</i></p>
<dd> Set the execution target to the given host. This option may be repeated to target multiple execution targets. Passes 1-4 are completed locally as normal to build the script, and then pass 5 will copy the module to the target and run it. Acceptable URL forms include:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>[USER@]HOSTNAME</code>, <code><a href="ssh://[USER@]HOSTNAME">ssh://[USER@]HOSTNAME</a></code></p>
<dd> This mode uses ssh, optionally using a username not matching your own. If a custom ssh_config file is in use, add <code>SendEnv LANG</code> to retain internationalization functionality.</p>
<dt><code>libvirt://DOMAIN</code>, <code>libvirt://DOMAIN/LIBVIRT_URI</code></p>
<dd> This mode uses <i>stapvirt</i> to execute the script on a domain managed by libvirt. Optionally, LIBVIRT_URI may be specified to connect to a specific driver and/or a remote host. For example, to connect to the local privileged QEMU driver, use: </p>
<dl>
<dt>
<dd>
<pre>
--remote libvirt://MyDomain/<a href="qemu:///system">qemu:///system</a>
</pre>
</dl>
<p> See the page at &lt;<a rel="nofollow" href="http://libvirt.org/uri.html">http://libvirt.org/uri.html</a>&gt; for supported URIs. Also see <i><a href="/docs/linux/man/1-stapvirt/">stapvirt</a></i>(1) for more information on how to prepare the domain for stap probing.</p>
<dt><code>unix:PATH</code></p>
<dd> This mode connects to a UNIX socket. This can be used with a QEMU virtio-serial port for executing scripts inside a running virtual machine.</p>
<dt><code>direct://</code></p>
<dd> Special loopback mode to run on the local host.</dl>
</dl>
<dt>
<dd>
<dt><code>&#8211;remote-prefix</code></p>
<dd> Prefix each line of remote output with &quot;N: &quot;, where N is the index of the remote execution target from which the given line originated. </p>
<dt><code>&#8211;download-debuginfo</code><i>[=OPTION]</i></p>
<dd> Enable, disable or set a timeout for the automatic debuginfo downloading feature offered by abrt as specified by OPTION, where OPTION is one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>yes</code></p>
<dd> enable automatic downloading of debuginfo with no timeout. This is the same as not providing an OPTION value to <i>&#8211;download-debuginfo</i></p>
<dt><code>no</code></p>
<dd> explicitly disable automatic downloading of debuginfo. This is the same as not using the option at all.</p>
<dt><code>ask</code></p>
<dd> show abrt output, and ask before continuing download. No timeout will be set.</p>
<dt><code>&lt;timeout&gt;</code></p>
<dd> specify a timeout as a positive number to stop the download if it is taking longer than &lt;timeout&gt; seconds.</dl>
</dl>
<dt>
<dd>
<dt><code>&#8211;rlimit-as</code><i>=NUM</i></p>
<dd> Specify the maximum size of the process&#8217;s virtual memory (address space), in bytes. </p>
<dt><code>&#8211;rlimit-cpu</code><i>=NUM</i></p>
<dd> Specify the CPU time limit, in seconds. </p>
<dt><code>&#8211;rlimit-nproc</code><i>=NUM</i></p>
<dd> Specify the maximum number of processes that can be created. </p>
<dt><code>&#8211;rlimit-stack</code><i>=NUM</i></p>
<dd> Specify the maximum size of the process stack, in bytes. </p>
<dt><code>&#8211;rlimit-fsize</code><i>=NUM</i></p>
<dd> Specify the maximum size of files that the process may create, in bytes. </p>
<dt><code>&#8211;sysroot</code><i>=DIR</i></p>
<dd> Specify sysroot directory where target files (executables, libraries, etc.) are located. With <i>-r RELEASE</i>, the sysroot will be searched for the appropriate kernel build directory. With <i>-r /DIR</i>, however, the sysroot will not be used to find the kernel build. </p>
<dt><code>&#8211;sysenv</code><i>=VAR=VALUE</i></p>
<dd> Provide an alternate value for an environment variable where the value on a remote system differs. Path variables (e.g. PATH, LD_LIBRARY_PATH) are assumed to be relative to the directory provided by <i>&#8211;sysroot</i>, if provided. </p>
<dt><code>&#8211;suppress-time-limits</code></p>
<dd> Disable -DSTP_OVERLOAD related options as well as -DMAXACTION and -DMAXTRYLOCK. This option requires guru mode. </p>
<dt><code>&#8211;runtime</code><i>=MODE</i></p>
<dd> Set the pass-5 runtime mode. Valid options are <i>kernel</i> (default) and <i>dyninst</i>. See <code>ALTERNATE RUNTIMES</code> below for more information. </p>
<dt><code>&#8211;dyninst</code></p>
<dd> Shorthand for <i>&#8211;runtime=dyninst</i>. </p>
<dt><code>&#8211;save-uprobes</code></p>
<dd> On machines that require SystemTap to build its own uprobes module (kernels prior to version 3.5), this option instructs SystemTap to also save a copy of the module in the current directory (creating a new &quot;uprobes&quot; directory first). </p>
<dt><code>&#8211;target-namespaces</code><i>=PID</i></p>
<dd> Allow for a set of target namespaces to be set based on the namespaces the given PID is in. This is for namespace-aware tapset functions. If the target namespaces was not set, the target defaults to the stap process&#8217; namespaces. </p>
<dt><code>&#8211;monitor</code><i>=INTERVAL</i></p>
<dd> Enables an interface to display status information about the module(uptime, module name, invoker uid, memory sizes, global variables, list of probes with their statistics). An optional argument INTERVAL can be supplied to set the refresh rate in seconds of the status window. The module can also be controlled by a list of commands using the following keys:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>c</code></p>
<dd> Resets all global variables to their initial values or zeroes them if they did not have an initial value.</p>
<dt><code>s</code></p>
<dd> Rotates the attribute used to sort the list of probes.</p>
<dt><code>t</code></p>
<dd> Brings up a prompt to allow toggling(on/off) of probes by index. Probe points are still affected by their conditions.</p>
<dt><code>r</code></p>
<dd> Resumes the script by toggling on all probes.</p>
<dt><code>p</code></p>
<dd> Pauses the script by toggling off all probes.</p>
<dt><code>x</code></p>
<dd> Hides/shows the status window. This allows for more output to be seen.</p>
<dt><code>navigation-keys</code></p>
<dd> The navigation keys can be used to scroll up and down the windows.</p>
<dt><code>Tab</code></p>
<dd> Toggle scrolling between status and output windows.</dl>
</dl>
</dl>
<h2>ARGUMENTS</h2>
<p> Any additional arguments on the command line are passed to the script parser for substitution. See below. </p>
<h2>SCRIPT LANGUAGE</h2>
<p> The systemtap script language resembles <i>awk</i> and <i>C</i>. There are two main outermost constructs: probes and functions. Within these, statements and expressions use C-like operator syntax and precedence. </p>
<h3>GENERAL SYNTAX</h3>
<p> Whitespace is ignored. Three forms of comments are supported:</p>
<dl>
<dt>
<dd>
 <code>#</code> &#8230; shell style, to the end of line, except for $# and @#<br />
 <code>//</code> &#8230; C++ style, to the end of line<br />
 <code>/*</code> &#8230; C style &#8230; <code>*/</code></dl>
<p> Literals are either strings enclosed in double-quotes (passing through the usual C escape codes with backslashes, and with adjacent string literals glued together, also as in C), or integers (in decimal, hexadecimal, or octal, using the same notation as in C). All strings are limited in length to some reasonable value (a few hundred bytes). Integers are 64-bit signed quantities, although the parser also accepts (and wraps around) values above positive 2**63. </p>
<p> In addition, script arguments given at the end of the command line may be inserted. Use <code>$1 &#8230; $&lt;NN&gt;</code> for insertion unquoted, <code>@1 &#8230; @&lt;NN&gt;</code> for insertion as a string literal. The number of arguments may be accessed through <code>$#</code> (as an unquoted number) or through <code>@#</code> (as a quoted number). These may be used at any place a token may begin, including within the preprocessing stage. Reference to an argument number beyond what was actually given is an error. </p>
<h3>PREPROCESSING</h3>
<p> A simple conditional preprocessing stage is run as a part of parsing. The general form is similar to the cond<code> ? </code>exp1<code> : </code>exp2 ternary operator: </p>
<dl>
<dt>
<dd>
<pre>
<code>%(</code> CONDITION <code>%?</code> TRUE-TOKENS <code>%)</code>
<code>%(</code> CONDITION <code>%?</code> TRUE-TOKENS <code>%:</code> FALSE-TOKENS <code>%)</code>
</pre>
</dl>
<p> The CONDITION is either an expression whose format is determined by its first keyword, or a string literals comparison or a numeric literals comparison. It can be also composed of many alternatives and conjunctions of CONDITIONs (meant as in previous sentence) using || and &amp;&amp; respectively. However, parentheses are not supported yet, so remembering that conjunction takes precedence over alternative is important. </p>
<p> If the first part is the identifier <code>kernel_vr</code> or <code>kernel_v</code> to refer to the kernel version number, with (&quot;2.6.13-1.322FC3smp&quot;) or without (&quot;2.6.13&quot;) the release code suffix, then the second part is one of the six standard numeric comparison operators <code>&lt;</code>, <code>&lt;=</code>, <code>==</code>, <code>!=</code>, <code>&gt;</code>, and <code>&gt;=</code>, and the third part is a string literal that contains an RPM-style version-release value. The condition is deemed satisfied if the version of the target kernel (as optionally overridden by the <code>-r</code> option) compares to the given version string. The comparison is performed by the glibc function <code>strverscmp</code>. As a special case, if the operator is for simple equality (<code>==</code>), or inequality (<code>!=</code>), and the third part contains any wildcard characters (<code>*</code> or <code>?</code> or <code>[</code>), then the expression is treated as a wildcard (mis)match as evaluated by <code>fnmatch</code>. </p>
<p> If, on the other hand, the first part is the identifier <code>arch</code> to refer to the processor architecture (as named by the kernel build system ARCH/SUBARCH), then the second part is one of the two string comparison operators <code>==</code> or <code>!=</code>, and the third part is a string literal for matching it. This comparison is a wildcard (mis)match. </p>
<p> Similarly, if the first part is an identifier like <code>CONFIG_something</code> to refer to a kernel configuration option, then the second part is <code>==</code> or <code>!=</code>, and the third part is a string literal for matching the value (commonly &quot;y&quot; or &quot;m&quot;). Nonexistent or unset kernel configuration options are represented by the empty string. This comparison is also a wildcard (mis)match. </p>
<p> If the first part is the identifier <code>systemtap_v</code>, the test refers to the systemtap compatibility version, which may be overridden for old scripts with the <code>&#8211;compatible</code> flag. The comparison operator is as is for <code>kernel_v</code> and the right operand is a version string. See also the DEPRECATION section below. </p>
<p> If the first part is the identifier <code>systemtap_privilege</code>, the test refers to the privilege level that the systemtap script is compiled with. Here the second part is <code>==</code> or <code>!=</code>, and the third part is a string literal, either &quot;stapusr&quot; or &quot;stapsys&quot; or &quot;stapdev&quot;. </p>
<p> If the first part is the identifier <code>guru_mode</code>, the test refers to if the systemtap script is compiled with guru_mode. Here the second part is <code>==</code> or <code>!=</code>, and the third part is a number, either 1 or 0. </p>
<p> If the first part is the identifier <code>runtime</code>, the test refers to the systemtap runtime mode. See <code>ALTERNATE RUNTIMES</code> below for more information on runtimes. The second part is one of the two string comparison operators <code>==</code> or <code>!=</code>, and the third part is a string literal for matching it. This comparison is a wildcard (mis)match. </p>
<p> Otherwise, the CONDITION is expected to be a comparison between two string literals or two numeric literals. In this case, the arguments are the only variables usable. </p>
<p> The TRUE-TOKENS and FALSE-TOKENS are zero or more general parser tokens (possibly including nested preprocessor conditionals), and are passed into the input stream if the condition is true or false. For example, the following code induces a parse error unless the target kernel version is newer than 2.6.5: </p>
<dl>
<dt>
<dd>
<pre>
%( kernel_v &lt;= &quot;2.6.5&quot; %? **ERROR** %) # invalid token sequence
</pre>
</dl>
<p> The following code might adapt to hypothetical kernel version drift: </p>
<dl>
<dt>
<dd>
probe kernel.function (<br />
  %( kernel_v &lt;= &#8220;2.6.12&#8221; %? &#8220;__mm_do_fault&#8221; %:<br />
     %( kernel_vr == &#8220;2.6.13*smp&#8221; %? &#8220;do_page_fault&#8221; %:<br />
        UNSUPPORTED %) %)<br />
) { /* &#8230; */ }<br />
%( arch == &#8220;ia64&#8221; %?<br />
   probe syscall.vliw = kernel.function(&#8220;vliw_widget&#8221;) {}<br />
%)
</dl>
<h3>PREPROCESSOR MACROS</h3>
<p> The preprocessor also supports a simple macro facility, run as a separate pass before conditional preprocessing. </p>
<p> Macros are defined using the following construct: </p>
<dl>
<dt>
<dd>
<pre>
@define NAME %( BODY %)
@define NAME(PARAM_1, PARAM_2, ...) %( BODY %)
</pre>
</dl>
<p> Macros, and parameters inside a macro body, are both invoked by prefixing the macro name with an @ symbol: </p>
<dl>
<dt>
<dd>
<pre>
@define foo %( x %)
@define add(a,b) %( ((@a)+(@b)) %)
   @foo = @add(2,2)
</pre>
</dl>
<p> Macro expansion is currently performed in a separate pass before conditional compilation. Therefore, both TRUE- and FALSE-tokens in conditional expressions will be macroexpanded regardless of how the condition is evaluated. This can sometimes lead to errors: </p>
<dl>
<dt>
<dd>
// The following results in a conflict:<br />
% (CONFIG_UTRACE == &#8220;y&#8221; % ? @define foo % (process.syscall %) % : @define foo % (**ERROR * * %) %)<br />
    // The following works properly as expected:<br />
    @define foo<br />
    % (% (CONFIG_UTRACE == &#8220;y&#8221; % ? process.syscall % : **ERROR * * %) %)
</dl>
<p> The first example is incorrect because both @defines are evaluated in a pass prior to the conditional being evaluated. </p>
<p> Normally, a macro definition is local to the file it occurs in. Thus, defining a macro in a tapset does not make it available to the user of the tapset. Publically available library macros can be defined by including .stpm files on the tapset search path. These files may only contain @define constructs, which become visible across all tapsets and user scripts. Optionally, within the .stpm files, a public macro definition can be surrounded by a preprocessor conditional as described above. </p>
<h3>CONSTANTS</h3>
<p> Tapsets or guru-mode user scripts can access header file constant tokens, typically macros, using built-in @const() operator. The respective header file inclusion is possible either via the tapset library, or using a top-level guru mode embedded-C construct. This results in appropriate embedded C pragma comments setting. </p>
<dl>
<dt>
<dd>
<pre>
@const(&quot;STP_SKIP_BADVARS&quot;)
</pre>
</dl>
<h3>VARIABLES</h3>
<p> Identifiers for variables and functions are an alphanumeric sequence, and may include <code>_</code> and <code>$</code> characters. They may not start with a plain digit, as in C. Each variable is by default local to the probe or function statement block within which it is mentioned, and therefore its scope and lifetime is limited to a particular probe or function invocation. </p>
<p> Scalar variables are implicitly typed as either string or integer. Associative arrays also have a string or integer value, and a tuple of strings and/or integers serving as a key. Here are a few basic expressions. </p>
<dl>
<dt>
<dd>
var1 = 5 var2 = &#8220;bar&#8221; array1[pid()] = &#8220;name&#8221; #single numeric key<br />
    array2[&#8220;foo&#8221;, 4, i++] += 5 #vector of string / num / num keys if ([ &#8220;hello&#8221;, 5, 4 ] in array2) println(&#8220;yes&#8221;) #membership test
</dl>
<p> The translator performs <i>type inference</i> on all identifiers, including array indexes and function parameters. Inconsistent type-related use of identifiers signals an error. </p>
<p> Variables may be declared global, so that they are shared amongst all probes and functions and live as long as the entire systemtap session. There is one namespace for all global variables, regardless of which script file they are found within. Concurrent access to global variables is automatically protected with locks, see the <code>SAFETY AND SECURITY</code> section for more details. A global declaration may be written at the outermost level anywhere, not within a block of code. Global variables which are written but never read will be displayed automatically at session shutdown. The translator will infer for each its value type, and if it is used as an array, its key types. Optionally, scalar globals may be initialized with a string or number literal. The following declaration marks variables as global. </p>
<dl>
<dt>
<dd>
<pre>
<code>global</code> var1<code>,</code> var2<code>,</code> var3=4
</pre>
</dl>
<p> Global variables can also be set as module options. One can do this by either using the -G option, or the module must first be compiled using stap -p4. Global variables can then be set on the command line when calling staprun on the module generated by stap -p4. See <i><a href="/docs/linux/man/8-staprun/">staprun</a></i>(8) for more information. </p>
<p> The scope of a global variable may be limited to a tapset or user script file using private keyword. The global keyword is optional when defining a private global variable. Following declaration marks var1 and var2 private globals. </p>
<dl>
<dt>
<dd>
<pre>
<code>private</code> global<code> var1=2</code>
<code>private</code> var2
</pre>
</dl>
<p> Arrays are limited in size by the MAXMAPENTRIES variable &#8212; see the <code>SAFETY AND SECURITY</code> section for details. Optionally, global arrays may be declared with a maximum size in brackets, overriding MAXMAPENTRIES for that array only. Note that this doesn&#8217;t indicate the type of keys for the array, just the size. </p>
<dl>
<dt>
<dd>
global tiny_array[10], normal_array, big_array[50000]
</dl>
<p> Arrays may be configured for wrapping using the &#8216;%&#8217; suffix. This causes older elements to be overwritten if more elements are inserted than the array can hold. This works for both associative and statistics typed arrays. </p>
<dl>
<dt>
<dd>
<pre>
<code>global</code> wrapped_array1%[10],<code> wrapped_array2%</code>
</pre>
</dl>
<p> Many types of probe points provide context variables, which are run-time values, safely extracted from the kernel or userspace program being probed. These are prefixed with the <code>$</code> character. The CONTEXT VARIABLES section in <i><a href="//www.systutorials.com/docs/linux/man/3stap-stapprobes/">stapprobes</a></i>(3stap) lists what is available for each type of probe point. These context variables become normal string or numeric scalars once they are stored in normal script variables. See the TYPECASTING section below on how to to turn them back into typed pointers for further processing as context variables. </p>
<h3>STATEMENTS</h3>
<p> Statements enable procedural control flow. They may occur within functions and probe handlers. The total number of statements executed in response to any single probe event is limited to some number defined by the MAXACTION macro in the translated C code, and is in the neighbourhood of 1000.</p>
<dl>
<dt>EXP</p>
<dd> Execute the string- or integer-valued expression and throw away the value.</p>
<dt><code>{</code> STMT1 STMT2 &#8230; <code>}</code></p>
<dd> Execute each statement in sequence in this block. Note that separators or terminators are generally not necessary between statements.</p>
<dt><code>;</code></p>
<dd> Null statement, do nothing. It is useful as an optional separator between statements to improve syntax-error detection and to handle certain grammar ambiguities.</p>
<dt><code>if</code> (EXP) STMT1 [ <code>else</code> STMT2 ]</p>
<dd> Compare integer-valued EXP to zero. Execute the first (non-zero) or second STMT (zero).</p>
<dt><code>while</code> (EXP) STMT</p>
<dd> While integer-valued EXP evaluates to non-zero, execute STMT.</p>
<dt><code>for</code> (EXP1; EXP2; EXP3) STMT</p>
<dd> Execute EXP1 as initialization. While EXP2 is non-zero, execute STMT, then the iteration expression EXP3.</p>
<dt><code>foreach</code> (VAR <code>in</code> ARRAY [ limit<code> EXP ]) STMT</code></p>
<dd> Loop over each element of the named global array, assigning current key to VAR. The array may not be modified within the statement. By adding a single <code>+</code> or <code>&#8211;</code> operator after the VAR or the ARRAY identifier, the iteration will proceed in a sorted order, by ascending or descending index or value. If the array contains statistics aggregates, adding the desired <code>@operator</code> between the ARRAY identifier and the <code>+</code> or <code>&#8211;</code> will specify the sorting aggregate function. See the STATISTICS section below for the ones available. Default is <code>@count</code>. Using the optional <code>limit</code> keyword limits the number of loop iterations to EXP times. EXP is evaluated once at the beginning of the loop.</p>
<dt><code>foreach</code> ([VAR1, VAR2, &#8230;] <code>in</code> ARRAY [ limit<code> EXP ]) STMT</code></p>
<dd> Same as above, used when the array is indexed with a tuple of keys. A sorting suffix may be used on at most one VAR or ARRAY identifier.</p>
<dt><code>foreach</code> ([VAR1, VAR2, &#8230;] <code>in</code> ARRAY [INDEX1, INDEX2, &#8230;] [ limit<code> EXP ]) STMT</code></p>
<dd> Same as above, where iterations are limited to elements in the array where the keys match the index values specified. The symbol * can be used to specify an index and will be treated as a wildcard.</p>
<dt><code>foreach</code> (VAR0 = VAR <code>in</code> ARRAY [ limit<code> EXP ]) STMT</code></p>
<dd> This variant of foreach saves current value into VAR0 on each iteration, so it is the same as ARRAY[VAR]. This also works with a tuple of keys. Sorting suffixes on VAR0 have the same effect as on ARRAY.</p>
<dt><code>foreach</code> (VAR0 = VAR <code>in</code> ARRAY [INDEX1, INDEX2, &#8230;] [ limit<code> EXP ]) STMT</code></p>
<dd> Same as above, where iterations are limited to elements in the array where the keys match the index values specified. The symbol * can be used to specify an index and will be treated as a wildcard.</p>
<dt><code>break</code>, <code>continue</code></p>
<dd> Exit or iterate the innermost nesting loop (<code>while</code> or <code>for</code> or <code>foreach</code>) statement.</p>
<dt><code>return</code> EXP</p>
<dd> Return EXP value from enclosing function. If the function&#8217;s value is not taken anywhere, then a return statement is not needed, and the function will have a special &quot;unknown&quot; type with no return value.</p>
<dt><code>next</code></p>
<dd> Return now from enclosing probe handler. This is especially useful in probe aliases that apply event filtering predicates. When used in functions, the execution will be immediately transferred to the next overloaded function.</p>
<dt><code>try</code> { STMT1 } <code>catch</code> { STMT2 }</p>
<dd> Run the statements in the first block. Upon any run-time errors, abort STMT1 and start executing STMT2. Any errors in STMT2 will propagate to outer try/catch blocks, if any.</p>
<dt><code>try</code> { STMT1 } <code>catch</code>(VAR) { STMT2 }</p>
<dd> Same as above, plus assign the error message to the string scalar variable VAR.</p>
<dt><code>delete</code> ARRAY[INDEX1, INDEX2, &#8230;]</p>
<dd> Remove from ARRAY the element specified by the index tuple. If the index tuple contains a * in place of an index, the * is treated as a wildcard and all elements with keys that match the index tuple will be removed from ARRAY. The value will no longer be available, and subsequent iterations will not report the element. It is not an error to delete an element that does not exist.</p>
<dt><code>delete</code> ARRAY</p>
<dd> Remove all elements from ARRAY.</p>
<dt><code>delete</code> SCALAR</p>
<dd> Removes the value of SCALAR. Integers and strings are cleared to 0 and &quot;&quot; respectively, while statistics are reset to the initial empty state. </p>
</dl>
<h3>EXPRESSIONS</h3>
<p> Systemtap supports a number of operators that have the same general syntax, semantics, and precedence as in C and awk. Arithmetic is performed as per typical C rules for signed integers. Division by zero or overflow is detected and results in an error.</p>
<dl>
<dt>binary numeric operators</p>
<dd> <code>* / % + &#8211; &gt;&gt; &lt;&lt; &amp; ^ | &amp;&amp; ||</code></p>
<dt>binary string operators</p>
<dd> <code>.</code> (string concatenation)</p>
<dt>numeric assignment operators</p>
<dd> <code>= *= /= %= += -= &gt;&gt;= &lt;&lt;= &amp;= ^= |=</code></p>
<dt>string assignment operators</p>
<dd> <code>= .=</code></p>
<dt>unary numeric operators</p>
<dd> <code>+ &#8211; ! ~ ++ &#8212;</code></p>
<dt>binary numeric, string comparison or regex matching operators</p>
<dd> <code>&lt; &gt; &lt;= &gt;= == != =~ !~</code></p>
<dt>ternary operator</p>
<dd> cond<code> ? </code>exp1<code> : </code>exp2</p>
<dt>grouping operator</p>
<dd> <code>(</code> exp <code>)</code></p>
<dt>function call</p>
<dd> fn <code>(</code>[ arg1, arg2, &#8230; ]<code>)</code></p>
<dt>array membership check</p>
<dd> exp<code> in </code>array<br />
 <code>[</code>exp1<code>, </code>exp2<code>, </code>&#8230;<code>] in </code>array<br />
 <code>[</code>*<code>, </code>*<code>, &#8230; ]</code>in<code> array</code> </p>
</dl>
<h3>REGULAR EXPRESSION MATCHING</h3>
<p> The scripting language supports regular expression matching. The basic syntax is as follows: </p>
<dl>
<dt>
<dd>
<pre>
<code>exp</code> =~ <code>regex</code>
<code>exp</code> !~ <code>regex</code>
</pre>
</dl>
<p> (The first operand must be an expression evaluating to a string; the second operand must be a string literal containing a syntactically valid regular expression.) </p>
<p> The regular expression syntax supports most of the features of POSIX Extended Regular Expressions, except for subexpression reuse (&quot;\1&quot;) functionality. The ability to capture and extract the contents of the matched string and subexpressions has not yet been implemented. </p>
<h3>PROBES</h3>
<p> The main construct in the scripting language identifies probes. Probes associate abstract events with a statement block (&quot;probe handler&quot;) that is to be executed when any of those events occur. The general syntax is as follows: </p>
<dl>
<dt>
<dd>
probe PROBEPOINT[, PROBEPOINT]{[STMT&#8230;]} probe PROBEPOINT[, PROBEPOINT] if (CONDITION)<br />
{<br />
    [STMT&#8230;]<br />
}
</dl>
<p> Events are specified in a special syntax called &quot;probe points&quot;. There are several varieties of probe points defined by the translator, and tapset scripts may define further ones using aliases. Probe points may be wildcarded, grouped, or listed in preference sequences, or declared optional. More details on probe point syntax and semantics are listed on the <i><a href="//www.systutorials.com/docs/linux/man/3stap-stapprobes/">stapprobes</a></i>(3stap) manual page. </p>
<p> The probe handler is interpreted relative to the context of each event. For events associated with kernel code, this context may include <i>variables</i> defined in the <i>source code</i> at that spot. These &quot;context variables&quot; are presented to the script as variables whose names are prefixed with &quot;$&quot;. They may be accessed only if the kernel&#8217;s compiler preserved them despite optimization. This is the same constraint that a debugger user faces when working with optimized code. In addition, the objects must exist in paged-in memory at the moment of the systemtap probe handler&#8217;s execution, because systemtap must not cause (suppresses) any additional paging. Some probe types have very little context. See the <i><a href="//www.systutorials.com/docs/linux/man/3stap-stapprobes/">stapprobes</a></i>(3stap) man pages to see the kinds of context variables available at each kind of probe point. </p>
<p> Probes may be decorated with an <i>arming condition</i>, consisting of a simple boolean expression on read-only global script variables. While disarmed (inactive, condition evaluates to false), some probe types reduce or eliminate their run-time overheads. When an arming condition evaluates to true, probes will be <i>soon</i> re-armed, and their probe handlers will start getting called as the events fire. (Some events may be lost during the arming interval. If this is unacceptable, do not use arming conditions for those probes.) Example of the syntax: </p>
<dl>
<dt>
<dd>
<pre>
probe timer.us(TIMER) if (enabled) {
}
</pre>
</dl>
<p> New probe points may be defined using &quot;aliases&quot;. Probe point aliases look similar to probe definitions, but instead of activating a probe at the given point, it just defines a new probe point name as an alias to an existing one. There are two types of alias, i.e. the prologue style and the epilogue style which are identified by &quot;=&quot; and &quot;+=&quot; respectively. </p>
<p> For prologue style alias, the statement block that follows an alias definition is implicitly added as a prologue to any probe that refers to the alias. While for the epilogue style alias, the statement block that follows an alias definition is implicitly added as an epilogue to any probe that refers to the alias. For example: </p>
<dl>
<dt>
<dd>
probe syscall.read = kernel.function(&#8220;sys_read&#8221;)<br />
{<br />
    fildes = $fd if (execname() == &#8220;init&#8221;) next #skip rest of probe<br />
}
</dl>
<p> defines a new probe point <i>syscall.read</i>, which expands to <i>kernel.function(sys_read)</i>, with the given statement as a prologue, which is useful to predefine some variables for the alias user and/or to skip probe processing entirely based on some conditions. And </p>
<dl>
<dt>
<dd>
probe syscall.read += kernel.function(&#8220;sys_read&#8221;)<br />
{<br />
    if (tracethis)<br />
        println($fd)<br />
}
</dl>
<p> defines a new probe point with the given statement as an epilogue, which is useful to take actions based upon variables set or left over by the the alias user. Please note that in each case, the statements in the alias handler block are treated ordinarily, so that variables assigned there constitute mere initialization, not a macro substitution. </p>
<p> An alias is used just like a built-in probe type. </p>
<dl>
<dt>
<dd>
<pre>
probe syscall.read {
  printf(&quot;reading fd=%d
&quot;, fildes)
  if (fildes &gt; 10) tracethis = 1
}
</pre>
</dl>
<h3>FUNCTIONS</h3>
<p> Systemtap scripts may define subroutines to factor out common work. Functions take any number of scalar (integer or string) arguments, and must return a single scalar (integer or string). An example function declaration looks like this: </p>
<dl>
<dt>
<dd>
<pre>
function thisfn (arg1, arg2) {
   return arg1 + arg2
}
</pre>
</dl>
<p> Note the general absence of type declarations, which are instead inferred by the translator. However, if desired, a function definition may include explicit type declarations for its return value and/or its arguments. This is especially helpful for embedded-C functions. In the following example, the type inference engine need only infer type type of arg2 (a string). </p>
<dl>
<dt>
<dd>
function thatfn : string(arg1<br />
                         : long, arg2)<br />
{<br />
    return sprint(arg1).arg2<br />
}
</dl>
<p> Functions may call others or themselves recursively, up to a fixed nesting limit. This limit is defined by the MAXNESTING macro in the translated C code and is in the neighbourhood of 10. </p>
<p> Functions may be marked private using the private keyword to limit their scope to the tapset or user script file they are defined in. An example definition of a private function follows: </p>
<dl>
<dt>
<dd>
private<br />
function three : long()<br />
{<br />
    return 3<br />
}
</dl>
<p> Functions terminating without reaching an explicit return statement will return an implicit 0 or &quot;&quot;, determined by type inference. </p>
<p> Functions may be overloaded during both runtime and compile time. </p>
<p> Runtime overloading allows the executed function to be selected while the module is running based on runtime conditions and is achieved using the &quot;next&quot; statement in script functions and STAP_NEXT macro for embedded-C functions. For example, </p>
<dl>
<dt>
<dd>
function f()<br />
{<br />
    if (condition)<br />
        next;<br />
    print(&#8220;first function&#8221;)<br />
}<br />
function f() %<br />
{<br />
    STAP_NEXT;<br />
    print(&#8220;second function&#8221;) %<br />
}<br />
function f()<br />
{<br />
    print(&#8220;third function&#8221;)<br />
}
</dl>
<p> During a functioncall f(), the execution will transfer to the third function if condition evaluates to true and print &quot;third function&quot;. Note that the second function is unconditionally nexted. </p>
<p> Parameter overloading allows the function to be executed to be selected at compile time based on the number of arguments provided to the functioncall. For example, </p>
<dl>
<dt>
<dd>
function g(){print(&#8220;first function&#8221;)} function g(x){print(&#8220;second function&#8221;)} g()-&gt;&#8221;first function&#8221; g(1)-&gt;&#8221;second function&#8221;
</dl>
<p> Note that runtime overloading does not occur in the above example, as exactly one function will be resolved for the functioncall. The use of a next statement inside a function while no more overloads remain will trigger a runtime exception Runtime overloading will only occur if the functions have the same arity, functions with the same name but different number of parameters are completely unrelated. </p>
<p> Execution order is determined by a priority value which may be specified. If no explicit priority is specified, user script functions are given a higher priority than library functions. User script functions and library functions are assigned a default priority value of 0 and 1 respectively. Functions with the same priority are executed in declaration order. For example, </p>
<dl>
<dt>
<dd>
function f() : 3<br />
{<br />
    if (condition)<br />
        next;<br />
    print(&#8220;first function&#8221;)<br />
}<br />
function f() : 1<br />
{<br />
    if (condition)<br />
        next;<br />
    print(&#8220;second function&#8221;)<br />
}<br />
function f() : 2<br />
{<br />
    print(&#8220;third function&#8221;)<br />
}
</dl>
<p> Since the second function has highest priority, it is executed first. The first function is never executed as there no &quot;next&quot; statements in the third function to transfer execution. </p>
<h3>PRINTING</h3>
<p> There are a set of function names that are specially treated by the translator. They format values for printing to the standard systemtap output stream in a more convenient way (note that data generated in the kernel module need to get transferred to user-space in order to get printed). </p>
<p>&nbsp;<wbr>&nbsp;<wbr>The <i>sprint*</i> variants return the formatted string instead of printing it.</p>
<dl>
<dt><code>print</code>, <code>sprint</code></p>
<dd> Print one or more values of any type, concatenated directly together.</p>
<dt><code>println</code>, <code>sprintln</code></p>
<dd> Print values like <i>print</i> and <i>sprint</i>, but also append a newline.</p>
<dt><code>printd</code>, <code>sprintd</code></p>
<dd> Take a string delimiter and two or more values of any type, and print the values with the delimiter interposed. The delimiter must be a literal string constant.</p>
<dt><code>printdln</code>, <code>sprintdln</code></p>
<dd> Print values with a delimiter like <i>printd</i> and <i>sprintd</i>, but also append a newline.</p>
<dt><code>printf</code>, <code>sprintf</code></p>
<dd> Take a formatting string and a number of values of corresponding types, and print them all. The format must be a literal string constant.</dl>
<p> The <i>printf</i> formatting directives similar to those of C, except that they are fully type-checked by the translator:</p>
<dl>
<dt>
<dd>
<dl>
<dt>%b</p>
<dd> Writes a binary blob of the value given, instead of ASCII text. The width specifier determines the number of bytes to write; valid specifiers are %b %1b %2b %4b %8b. Default (%b) is 8 bytes.</p>
<dt>%c</p>
<dd> Character.</p>
<dt>%d,%i</p>
<dd> Signed decimal.</p>
<dt>%m</p>
<dd> Safely reads kernel (without #) or user (with #) memory at the given address, outputs its content. The optional precision specifier (not field width) determines the number of bytes to read &#8211; default is 1 byte. %10.4m prints 4 bytes of the memory in a 10-character-wide field. Note, on some architectures user memory can still be read without #.</p>
<dt>%M</p>
<dd> Same as %m, but outputs in hexadecimal. The minimal size of output is double the optional precision specifier &#8211; default is 1 byte (2 hex chars). %10.4M prints 4 bytes of the memory as 8 hexadecimal characters in a 10-character-wide field. %.*M hex-dumps a given number of bytes from a given buffer.</p>
<dt>%o</p>
<dd> Unsigned octal.</p>
<dt>%p</p>
<dd> Unsigned pointer address.</p>
<dt>%s</p>
<dd> String.</p>
<dt>%u</p>
<dd> Unsigned decimal.</p>
<dt>%x</p>
<dd> Unsigned hex value, in all lower-case.</p>
<dt>%X</p>
<dd> Unsigned hex value, in all upper-case.</p>
<dt>%%</p>
<dd> Writes a %.</dl>
</dl>
<p> The <i>#</i> flag selects the alternate forms. For octal, this prefixes a 0. For hex, this prefixes 0x or 0X, depending on case. For characters, this escapes non-printing values with either C-like escapes or raw octal. In the case of %#m/%#M, this safely accesses user space memory rather than kernel space memory. </p>
<p> Examples: </p>
<dl>
<dt>
<dd>
a = &#8220;alice&#8221;, b = &#8220;bob&#8221;, p = 0x1234abcd, i = 123, j = -1, id[a] = 1234, id[b] = 4567 print(&#8220;hello&#8221;) Prints : hello println(b) Prints : bob
 println(a.&#8221; is &#8220;.sprint(16)) Prints : alice is 16 foreach (name in id) printdln(&#8220;|&#8221;, strlen(name), name, id[name]) Prints : 5 | alice | 1234
3 | bob | 4567 printf(&#8220;%c is %s; %x or %X or %p; %d or %u
&#8221;, 97, a, p, p, p, j, j) Prints : a is alice;<br />
1234abcd or 1234ABCD or 0x1234abcd;<br />
&#8211; 1 or 18446744073709551615
<br />
           printf(&#8220;2 bytes of kernel buffer at address %p: %2m&#8221;, p, p)<br />
        Prints:2 byte of kernel buffer at address<br />
    0x1234abcd:&lt;binary data&gt; printf(&#8220;%4b&#8221;, p)<br />
                   Prints(these values as binary data):0x1234abcd printf(&#8220;%#o %#x %#X
&#8221;, 1, 2, 3)<br />
        Prints:01 0x2 0X3 printf(&#8220;%#c %#c %#c
&#8221;, 0, 9, 42)<br />
        Prints: 
