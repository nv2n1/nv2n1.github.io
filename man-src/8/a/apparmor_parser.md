---
title: "apparmor_parser(8)"
name: "apparmor_parser"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apparmor_parser/"
description: "apparmor_parser – loads AppArmor profiles into the kernel"
---

<p>apparmor_parser &#8211; loads AppArmor profiles into the kernel</p>
<h2>Synopsis</h2>
<p><code>apparmor_parser [options] &lt;command&gt; [profiles]&#8230;</code> </p>
<p> <code>apparmor_parser [options] &lt;command&gt;</code> </p>
<p> <code>apparmor_parser [-hv] [&#8211;help] [&#8211;version]</code></p>
<h2>Description</h2>
<p><code>apparmor_parser</code> is used as a general tool to compile, and manage AppArmor policy, including loading new <code><a href="/docs/linux/man/5-apparmor-d/">apparmor.d</a></code>(5) profiles into the Linux kernel. </p>
<p> AppArmor profiles restrict the operations available to processes. </p>
<p> The <code>profiles</code> are loaded into the Linux kernel by the <code>apparmor_parser</code> program. The <code>profiles</code> may be specified by file name or a directory name containing a set of profiles. If a directory is specified then the <code>apparmor_parser</code> will try to do a profile load for each file in the directory that is not a dot file, or explicitly black listed (*.dpkg-new, *.dpkg-old, *.dpkg-dist, *.dpkg-bak, *.dpkg-remove, *.pacsave, *.pacnew, *.rpmnew, *.rpmsave, *.orig, *.rej, *~). The <code>apparmor_parser</code> will fall back to taking input from standard input if a profile or directory is not supplied. </p>
<p> The input supplied to <code>apparmor_parser</code> should be in the format described in <code><a href="/docs/linux/man/5-apparmor-d/">apparmor.d</a></code>(5).</p>
<h2>Commands</h2>
<p>The command set is broken into four subcategories.</p>
<dl>
<dt>unprivileged commands</p>
<dd>Commands that don&#8217;t require any privilege and don&#8217;t operate on profiles.</p>
<dt>unprivileged profile commands</p>
<dd>Commands that operate on a profile either specified on the command line or read from stdin if no profile was specified.</p>
<dt>privileged commands</p>
<dd>Commands that require the <font SIZE="-1">MAC_ADMIN</font> capability within the affected AppArmor namespace to load policy into the kernel or filesystem write permissions to update the affected privileged files (cache etc).</p>
<dt>privileged profile commands</p>
<dd>Commands that require privilege and operate on profiles.</dl>
<h2>Unprivileged commands</h2>
<dl>
<dt>-V, &#8211;version</p>
<dd>Print the version number and exit.</p>
<dt>-h, &#8211;help</p>
<dd>Give a quick reference guide.</dl>
<h2>Unprivileged profile commands</h2>
<dl>
<dt>-N, &#8211;names</p>
<dd>Produce a list of policies from a given set of profiles (implies -K).</p>
<dt>-p, &#8211;preprocess</p>
<dd>Apply preprocessing to the input profile(s) by flattening includes into the output profile and dump to stdout.</p>
<dt>-S, &#8211;stdout</p>
<dd>Writes a binary (cached) profile to stdout (implies -K and -T).</p>
<dt>-o file, &#8211;ofile file</p>
<dd>Writes a binary (cached) profile to the specified file (implies -K and -T)</dl>
<h2>Privileged commands</h2>
<dl>
<dt>&#8211;purge-cache</p>
<dd>Unconditionally clear out cached profiles.</dl>
<h2>Privileged profile commands</h2>
<dl>
<dt>-a, &#8211;add</p>
<dd>Insert the AppArmor definitions given into the kernel. This is the default action. This gives an error message if a AppArmor definition by the same name already exists in the kernel, or if the parser doesn&#8217;t understand its input. It reports when an addition succeeded.</p>
<dt>-r, &#8211;replace</p>
<dd>This flag is required if an AppArmor definition by the same name already exists in the kernel; used to replace the definition already in the kernel with the definition given on standard input.</p>
<dt>-R, &#8211;remove</p>
<dd>This flag is used to remove an AppArmor definition already in the kernel. Note that it still requires a complete AppArmor definition as described in <code><a href="/docs/linux/man/5-apparmor-d/">apparmor.d</a></code>(5) even though the contents of the definition aren&#8217;t used.</dl>
<h2>Options</h2>
<dl>
<dt>-B, &#8211;binary</p>
<dd>Treat the profile files specified on the command line (or stdin if none specified) as binary cache files, produced with the -S or -o options, and load to the kernel as specified by -a, -r, and -R (implies -K and -T).</p>
<dt>-C, &#8211;Complain</p>
<dd>Force the profile to load in complain mode.</p>
<dt>-b n, &#8211;base n</p>
<dd>Set the base directory for resolving #include directives defined as relative paths.</p>
<dt>-I n, &#8211;Include n</p>
<dd>Add element n to the search path when resolving #include directives defined as an absolute paths.</p>
<dt>-f n, &#8211;apparmorfs n</p>
<dd>Set the location of the apparmor security filesystem (default is &#8220;/sys/kernel/security/apparmor&#8221;).</p>
<dt>&#8211;policy-features n</p>
<dd>Specify the feature set that the policy was developed under. This does not override feature <font SIZE="-1">ABI</font> rules.</p>
<dt>&#8211;override-policy-abi n</p>
<dd>Specify the feature set that the policy was developed under and override any feature <font SIZE="-1">ABI</font> rules that the policy may be using.</p>
<dt>&#8211;kernel-features n</p>
<dd>Specify the feature set of the kernel that the policy is being compiled for. If not specified this will be determined by the system&#8217;s kernel.</p>
<dt>-M n, &#8211;features-file n</p>
<dd>Use the features file located at path &#8220;n&#8221; (default is /etc/apparmor.d/cache/.features). If the &#8211;cache-loc option is present, the &#8220;.features&#8221; file in the specified cache directory is used. </p>
<p> Note: this sets both the &#8211;kernel-features and &#8211;policy-features to be the same.</p>
<dt>-m n, &#8211;match-string n</p>
<dd>Only use match features &#8220;n&#8221;. </p>
<p> Note: this sets both the &#8211;kernel-features and &#8211;policy-features to be the same.</p>
<dt>-n n, &#8211;namespace-string n</p>
<dd>Force a profile to load in the namespace &#8220;n&#8221;.</p>
<dt>-X, &#8211;readimpliesX</p>
<dd>In the case of profiles that are loading on systems were <font SIZE="-1">READ_IMPLIES_EXEC</font> is set in the kernel for a given process, load the profile so that any &#8220;r&#8221; flags are processed as &#8220;mr&#8221;.</p>
<dt>-k, &#8211;show-cache</p>
<dd>Report the cache processing (hit/miss details) when loading or saving cached profiles.</p>
<dt>-K, &#8211;skip-cache</p>
<dd>Perform no caching at all: disables -W, implies -T.</p>
<dt>-T, &#8211;skip-read-cache</p>
<dd>By default, if a profile&#8217;s cache is found in the location specified by &#8211;cache-loc and the timestamp is newer than the profile, it will be loaded from the cache. This option disables this cache loading behavior.</p>
<dt>-W, &#8211;write-cache</p>
<dd>Write out cached profiles to the location specified in &#8211;cache-loc. Off by default. In cases where abstractions have been changed, and the parser is running with &#8220;&#8211;replace&#8221;, it may make sense to also use &#8220;&#8211;skip-read-cache&#8221; with the &#8220;&#8211;write-cache&#8221; option.</p>
<dt>&#8211;skip-bad-cache</p>
<dd>Skip updating the cache if it contains cached profiles in a bad or inconsistent state</p>
<dt>-L, &#8211;cache-loc</p>
<dd>Set the location(s) of the cache directory. This option can accept a comma separated list of directories, which will be searched in order to find a matching cache. The first matching cache file found is used even if a directory later in the search order may contain a newer cache file. </p>
<p> If multiple directories are specified and &#8211;write-cache has been specified then cache writes will be made to the first directory in the list, all other directories will be treated as read only. </p>
<p> If a cache directory name needs to have a comma as part of the name, it can be specified by using a backslash to escape the comma character in the directory name. </p>
<p> If not specified the cache location defaults to /var/cache/apparmor</p>
<dt>&#8211;print-cache-dir</p>
<dd>Print the cache directory location. This path will be a subdirectory of the directory specified by &#8211;cache-loc. The subdirectory used will be influenced by the features available in the currently running kernel or by the features specified with the &#8211;match-string or &#8211;features-file options.</p>
<dt>-Q, &#8211;skip-kernel-load</p>
<dd>Perform all actions except the actual loading of a profile into the kernel. This is useful for testing profile generation, caching, etc, without making changes to the running kernel profiles. </p>
<p> This also removes the need for privilege to execute the commands that manage policy in the kernel</p>
<dt>-q, &#8211;quiet</p>
<dd>Do not report on the profiles as they are loaded, and not show warnings.</p>
<dt>-v, &#8211;verbose</p>
<dd>Report on the profiles as they are loaded, and show warnings.</p>
<dt>&#8211;warn=n</p>
<dd>Enable various warnings during policy compilation. A single warn flag can be specified per &#8211;warn option, but the &#8211;warn flag can be passed multiple times. </p>
<pre> apparmor_parser --warn=rules-not-enforced ...</pre>
<p>A specific warning can be disabled by prepending <i>no</i>&#8211; to the flag </p>
<pre> apparmor_parser --warn=no-rules-not-enforced ...</pre>
<p>Use &#8211;help=warn to see a full list of which warn flags are supported.</p>
<dt>&#8211;Werror[=n]</p>
<dd>Convert warnings into errors during policy compilation. If the optional flag is not specified all warnings become errors. If the optional flag is specified only the class of warnings specified will become errors. A single flag can be specified per &#8211;Werror option, but the &#8211;Werror flag can be passed multiple times. </p>
<pre> apparmor_parser --Werror=deprecated ...</pre>
<p>Use &#8211;help=warn or &#8211;help=Werror to see a full list of which warn flags are supported.</p>
<dt>-d, &#8211;debug</p>
<dd>Given once, only checks the profiles to ensure syntactic correctness. Given twice, dumps its interpretation of the profile for checking.</p>
<dt>-D n, &#8211;dump=n</p>
<dd>Debug flag for dumping various structures and passes of policy compilation. A single dump flag can be specified per &#8211;dump option, but the dump flag can be passed multiple times. Note progress flags tend to also imply the matching stats flag. </p>
<pre> apparmor_parser --dump=dfa-stats --dump=trans-stats &lt;file&gt;</pre>
<p>Use &#8211;help=dump to see a full list of which dump flags are supported</p>
<dt>-j n, &#8211;jobs=n</p>
<dd>Set the number of jobs used to compile the specified policy. Where n can be </p>
<pre> 0 - disable jobs and use the main process for all compilation
 # - a specific number of jobs
 auto - the # of cpus in the in the system
 x# - # * number of cpus</pre>
<p>Eg.<br />
&nbsp;<wbr>&nbsp;-j8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<font SIZE="-1">OR</font>&nbsp;&#8211;jobs=8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allows for 8 parallel jobs<br />
&nbsp;<wbr>&nbsp;-jauto&nbsp;<wbr>&nbsp;<font SIZE="-1">OR</font>&nbsp;&#8211;jobs=auto&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the jobs to the&nbsp;#&nbsp;of cpus<br />
&nbsp;<wbr>&nbsp;-jx4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<font SIZE="-1">OR</font>&nbsp;&#8211;jobs=x4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the jobs to&nbsp;#&nbsp;of cpus&nbsp;*&nbsp;4<br />
&nbsp;<wbr>&nbsp;-jx1&nbsp;<wbr>&nbsp;<wbr>&nbsp;is equivalent to&nbsp;<wbr>&nbsp;<wbr>&nbsp;-jauto </p>
<p> The default value is the number of cpus in the system. Note that if jobs is a positive integer number the &#8211;jobs-max parameter is automatically set to the same value.</p>
<dt>&#8211;max-jobs n</p>
<dd>When &#8211;jobs is set to a scaling value (ie. auto or xN) the specify a hard cap on the value that can be specified by the &#8211;jobs flag. It takes the same set of options available to the &#8211;jobs option, and defaults to 8*cpus</p>
<dt>-O n, &#8211;optimize=n</p>
<dd>Set the optimization flags used by policy compilation. A single optimization flag can be toggled per -O option, but the optimize flag can be passed multiple times. Turning off some phases of the optimization can make it so that policy can&#8217;t complete compilation due to size constraints (it is entirely possible to create a dfa with millions of states that will take days or longer to compile). </p>
<p> Note: The parser is set to use a balanced default set of flags, that will result in reasonable compression but not take excessive amounts of time to complete. </p>
<p> Use &#8211;help=optimize to see a full list of which optimization flags are supported.</p>
<dt>&#8211;abort-on-error Abort processing of profiles on the first error encountered, otherwise the parser will continue to try to compile other profiles if specified.</p>
<dd>Note: If an error is encountered while processing profiles the last error encountered will be used to set the exit code.</p>
<dt>&#8211;skip-bad-cache-rebuild The default behavior of the parser is to check if a cached version of a profile exists and if it does it attempt to load it into the kernel. If that load is rejected, then the parser will attempt to rebuild the cache file, and load again.</p>
<dd>This option tells the parser to not attempt to rebuild the cache on failure, instead the parser continues on with processing the remaining profiles.</p>
<dt>&#8211;config-file</p>
<dd>Specify the config file to use instead of /etc/apparmor/parser.conf. This option will be processed early before regular options regardless of the order it is specified in.</p>
<dt>&#8211;print-config-file</p>
<dd>Print the config file location that will be used.</dl>
<h2>Config File</h2>
<p>An optional config file /etc/apparmor/parser.conf can be used to specify the default options for the parser, which then can be overridden using the command line options. </p>
<p> The config file ignores leading whitespace and treats lines that begin with # as comments. Config options are specified one per line using the same format as the longform command line options (without the preceding &#8211;). </p>
<p> Eg.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#comment </p>
<pre> optimize=no-expr-tree
 optimize=compress-fast</pre>
<p>As with the command line some options accumulate and others override, ie. when there are conflicting versions of switch the last option is the one chosen. </p>
<p> Eg.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Optimize=no-minimize<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Optimize=minimize </p>
<p> would result in Optimize=minimize being set. </p>
<p> The Include, Dump, and Optimize options accululate except for the inversion option (no-X vs. X), and a couple options that work by setting/clearing multiple options (compress-small). In that case the option will override the flags it sets but will may accumulate with others. </p>
<p> All other options override previously set values.</p>
<h2>Bugs</h2>
<p>If you find any bugs, please report them at &lt;<a rel="nofollow" href="https://gitlab.com/apparmor/apparmor/-/issues">https://gitlab.com/apparmor/apparmor/-/issues</a>&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-apparmor/">apparmor</a></code>(7), <code><a href="/docs/linux/man/5-apparmor-d/">apparmor.d</a></code>(5), <code><a href="/docs/linux/man/2-aa_change_hat/">aa_change_hat</a></code>(2), and &lt;<a rel="nofollow" href="https://wiki.apparmor.net">https://wiki.apparmor.net</a>&gt;. </p>
