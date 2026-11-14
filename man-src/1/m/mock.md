---
title: "mock(1)"
name: "mock"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mock/"
description: "mock – build SRPMs in a chroot"
---

<h2>NAME</h2>
<p> mock &#8211; build SRPMs in a chroot</p>
<h2>SYNTAX</h2>
<p> mock [options] <code>&#8211;rebuild</code> <i>SRPM [SRPM&#8230;</i>] </p>
<p> mock [options] <code>&#8211;buildsrpm</code> {&#8211;spec <i>spec</i> &#8211;sources <i>src</i> &#8211;symlink-dereference | &#8211;scm-enable} </p>
<p> mock [options] <code>&#8211;chroot</code> <i>&lt;cmd&gt;</i> </p>
<p> mock [options] {<code>&#8211;init</code>|<code>clean</code>|<code>shell</code>} </p>
<p> mock [options] <code>&#8211;installdeps</code> {SRPM|RPM} </p>
<p> mock [options] <code>-i</code>, <code>&#8211;install</code> PACKAGE [<i>PACKAGE&#8230;</i>] </p>
<p> mock [options] <code>&#8211;update</code> [<i>PACKAGE&#8230;</i>] </p>
<p> mock [options] <code>&#8211;remove</code> PACKAGE [<i>PACKAGE&#8230;</i>] </p>
<p> mock [options] <code>&#8211;orphanskill</code> </p>
<p> mock [options] <code>-p</code>, <code>&#8211;print-root-path</code> </p>
<p> mock [options] <code>&#8211;copyin</code> <i>path [path&#8230;</i>] <i>destination</i> </p>
<p> mock [options] <code>&#8211;copyout</code> <i>path [path&#8230;</i>] <i>destination</i> </p>
<p> mock [options] <code>&#8211;scm-enable</code> [<i>&#8211;scm-option key=value &#8230;</i>] </p>
<p> mock [options] <code>-l</code>, <code>&#8211;list-snapshots</code> </p>
<p> mock [options] <code>&#8211;snapshot</code> [<i>snapshot-name</i>] </p>
<p> mock [options] <code>&#8211;rollback-to</code> [<i>snapshot-name</i>] </p>
<p> mock [options] <code>&#8211;remove-snapshot</code> [<i>snapshot-name</i>] </p>
<p> mock [options] <code>&#8211;umount</code> </p>
<p> mock [options] <code>&#8211;pm-cmd</code> [<i>arguments &#8230;</i>] </p>
<p> mock [options] <code>&#8211;yum-cmd</code> [<i>arguments &#8230;</i>] </p>
<p> mock [options] <code>&#8211;dnf-cmd</code> [<i>arguments &#8230;</i>] </p>
<h2>DESCRIPTION</h2>
<p> Mock is a simple program that will build source RPMs inside a chroot. It doesn&#8217;t do anything terribly fancy other than populate a chroot with the contents specified by a configuration file, then build any input SRPM(s) in that chroot. </p>
<p> The content of a chroot is specified by the configuration specified with the <code>-r</code> option. The default configuration file is /etc/mock/default.cfg, which is usually a symlink to one of the installed configurations. </p>
<p> There is a site-wide configuration file, /etc/mock/site-defaults.cfg, which can be used to specify site-wide options. The shipped version of this file has no active options, but does have a list of all of the configuration options, examples of how to set them, and their default values. </p>
<p> For backwards compatibility, old-style commands, (&quot;rebuild&quot;, &quot;init&quot;, &quot;clean&quot;, etc.) without leading &#8216;&#8211;&#8216; are still accepted, but are deprecated. See COMMANDS section, below, for detailed listing of all commands. </p>
<p> To use mock, a user should become a member of the <code>mock</code> group by adding their username to the <code>mock</code> line in /etc/group. This can be done with the following command: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>sudo&nbsp;<wbr>/usr/sbin/usermod -a -G mock&nbsp;<wbr>$USER</code> </p>
<p> Note that mock is not intended to be run directly as root. </p>
<p> Warning: Mock is running some parts of code under root privileges. There are known ways how to get root access once user is in mock group (and once he is able to run mock). This is possible when user abuse the mock configuration options. Please do not add anyone who is not trustworthy to the mock group! </p>
<h2>COMMANDS</h2>
<dl>
<dt><code>&#8211;buildsrpm</code></p>
<dd> Builds the specified SRPM either from a spec file and source file/directory or from SCM. The chroot (includining the results directory) is cleaned first, unless &#8211;no-clean is specified.</p>
<dt><code>&#8211;clean</code></p>
<dd> Purge the chroot tree.</p>
<dt><code>&#8211;copyin</code></p>
<dd> Copies the source paths (files or directory trees) into the chroot at the specified destination path.</p>
<dt><code>&#8211;copyout</code></p>
<dd> Copies the source paths (files or directory trees) from the chroot to the specified destination path.</p>
<dt><code>&#8211;chroot</code> <i>COMMAND [ARGS&#8230;</i>]</p>
<dd> Run the specified command non-interactively within the chroot (no &#8216;clean&#8217; is performed). Command output will be sent to the log files. Note that COMMAND is shell expanded only if there are no ARGS. Otherwise there is no shell expansion.</p>
<dt><code>&#8211;dnf-cmd</code></p>
<dd> Execute following arguments with DNF with installroot set to the chroot path. DNF must be installed on the system. It will use the binary which is specified in &#8216;dnf_command&#8217; option in site-defaults.cfg config, which by default is /usr/bin/dnf. This option will enforce &#8211;dnf.</p>
<dt><code>&#8211;init</code></p>
<dd> Initialize a chroot (clean, install chroot packages, etc.)</p>
<dt><code>-i</code>, <code>&#8211;install</code></p>
<dd> Do a yum install PACKAGE inside the chroot. No &#8216;clean&#8217; is performed</p>
<dt><code>&#8211;installdeps</code></p>
<dd> Find out deps for SRPM or RPM, and do a yum install to put them in the chroot. No &#8216;clean&#8217; is performed</p>
<dt><code>-l</code>, <code>&#8211;list-snapshots</code></p>
<dd> List all existing snapshots of the chroot belonging to current configuration. Current base snapshot is marked with an asterisk (<code>*</code>)</p>
<dt><code>&#8211;mount</code></p>
<dd> Mount all everything mounted in the chroot path including the root itself that might have been a LVM volume or TMPFS.</p>
<dt><code>&#8211;orphanskill</code></p>
<dd> No-op mode that simply checks that no stray processes are running in the chroot. Kills any processes that it finds using specified root.</p>
<dt><code>&#8211;pm-cmd</code></p>
<dd> Execute following arguments with current package manager with installroot set to the chroot path.</p>
<dt><code>-p</code>, <code>&#8211;print-root-path</code></p>
<dd> Prints a path to the currently used chroot directory.</p>
<dt><code>&#8211;rebuild</code></p>
<dd> If no command is specified, rebuild is assumed. Rebuilds the specified SRPM(s). The chroot (includining the results directory) is cleaned first, unless &#8211;no-clean is specified.</p>
<dt><code>&#8211;remove</code></p>
<dd> Do a yum remove PACKAGE inside the chroot. No &#8216;clean&#8217; is performed</p>
<dt><code>&#8211;remove-snapshot</code></p>
<dd> Remove given snapshot freeing the space it occupied. This action cannot be undone. This feature is available only when lvm_root plugin is installed and enabled.</p>
<dt><code>&#8211;rollback-to</code></p>
<dd> Return chroot to the state in specified snapshot and set it as the current base to which clean actions will return. It won&#8217;t delete nor modify the snapshot that was set as base previously. This feature is available only when lvm_root plugin is installed and enabled.</p>
<dt><code>&#8211;scm-enable</code></p>
<dd> Enable building from an SCM (CVS/Git/SVN). The SCM repository must be configured in site-defaults.cfg before SCM checkouts are possible. SCM package and branch can be defined with <code>&#8211;scm-option</code> arguments, see site-defaults.cfg for more information.</p>
<dt><code>&#8211;scrub</code>=<i>TYPE</i></p>
<dd> Completely remove the specified chroot or cache dir or all of the chroot and cache. <i>TYPE</i> is one of all, chroot, cache, root-cache, c-cache, yum-cache or dnf-cache. In fact, dnf-cache is just alias for yum-cache and both removes Dnf and Yum cache.</p>
<dt><code>&#8211;shell</code> [<i>COMMAND [ARGS&#8230;]</i>]</p>
<dd> Run the specified command interactively within the chroot (no &#8216;clean&#8217; is performed). If no command specified, /bin/sh is run. Note that COMMAND is shell expanded using shell in chroot. Note that this command does not produce logs.</p>
<dt><code>&#8211;sources</code>=<i>SOURCES</i></p>
<dd> Specifies sources (either a single file or a directory of files) to use to build an SRPM (used only with &#8211;buildsrpm).</p>
<dt><code>&#8211;spec</code>=<i>SPEC</i></p>
<dd> Specifies spec file to use to build an SRPM (used only with &#8211;buildsrpm).</p>
<dt><code>&#8211;update</code> [<i>PACKAGE&#8230;]</i></p>
<dd> Do a package update inside the chroot. The package list is optional, if omitted, all packages will be updated. No &#8216;clean&#8217; is performed</p>
<dt><code>&#8211;snapshot</code></p>
<dd> Make a snapshot of the current state of the chroot. That snapshot will be set as the current base to which &#8211;clean and implicit clean happening during rebuild command will return. This feature is available only when lvm_root plugin is installed and enabled.</p>
<dt><code>&#8211;umount</code></p>
<dd> Umount all everything mounted in the chroot path including the root itself that might have been a LVM volume or TMPFS.</p>
<dt><code>&#8211;yum-cmd</code></p>
<dd> Execute following arguments with YUM with installroot set to the chroot path. Yum must be installed on the system. It will use the binary which is specified in &#8216;yum_command&#8217; option in site-defaults.cfg config, which by default is /usr/bin/yum. Note that in config files for Fedora 22+ this value is overwriten in chroot config to default to /usr/bin/yum-deprecated. This option will enforce &#8211;yum.</p>
<dt>Note: While you can specify more commands on command line, only one can be executed. The last command will win.</p>
<dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;arch</code>=<i>ARCH</i></p>
<dd> Calls the linux personality() syscall to tell the kernel to emulate a secondary architecture. For example, building i386 packages on an x86_64 buildhost.</p>
<dt><code>&#8211;cache-alterations</code></p>
<dd> Rebuild the root cache after making alterations to the chroot (i.e. &#8211;install). Only useful when using tmpfs plugin.</p>
<dt><code>&#8211;cleanup-after</code></p>
<dd> Clean chroot after building. Use with &#8211;resultdir. Only active for &#8216;&#8211;rebuild&#8217;.</p>
<dt><code>&#8211;configdir</code>=<i>CONFIGDIR</i></p>
<dd> Change directory where config files are found</p>
<dt><code>&#8211;cwd</code>=<i>DIR</i></p>
<dd> Change to the specified directory (relative to the chroot) before running command when using &#8211;chroot</p>
<dt><code>-D </code>&quot;<i>MACRO EXPR</i>&quot;, <code>&#8211;define</code>=&quot;<i>MACRO EXPR</i>&quot;</p>
<dd> Specify macro definitions used for the build. This option may be used multiple times, just as the rpmbuild &#8211;define option can be. For example: </p>
<p> <code>&#8211;define &quot;with_extra_cheese 1&quot; &#8211;define=&quot;packager Monkey&quot;</code></p>
<dt><code>&#8211;disable-plugin</code>=<i>PLUGIN</i></p>
<dd> Disable the specified plugin. This option may be used multiple times.</p>
<dt><code>&#8211;disablerepo</code>=<i>REPO</i></p>
<dd> Pass <code>&#8211;disablerepo</code> option to package manager to disable a repository. It can be specified multiple times.</p>
<dt><code>&#8211;dnf</code></p>
<dd> Use DNF as the current package manager. You should have DNF (and dnf-plugins-core) installed on your system.</p>
<dt><code>&#8211;enable-plugin</code>=<i>PLUGIN</i></p>
<dd> Enable the specified plugin. This option may be used multiple times.</p>
<dt><code>&#8211;enablerepo</code>=<i>REPO</i></p>
<dd> Pass <code>&#8211;enablerepo</code> option to package manager to enable a repository. It can be specified multiple times.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show usage information and exit.</p>
<dt><code>&#8211;macro-file</code>=<i>FILE</i></p>
<dd> Use pre-defined rpm macro file. Macros passed to &#8216;&#8211;define&#8217; override macros of the same name from FILE.</p>
<dt><code>&#8211;new-chroot</code></p>
<dd> use new chroot (systemd-nspawn) &#8211; this is experimental and will break existing scripts.</p>
<dt><code>-n</code>, <code>&#8211;no-clean</code></p>
<dd> Do not clean chroot before building package.</p>
<dt><code>&#8211;nocheck</code></p>
<dd> Pass &#8211;nocheck to rpmbuild to skip &#8216;make check&#8217; tests.</p>
<dt><code>&#8211;no-cleanup-after</code></p>
<dd> Don&#8217;t clean chroot after building. If automatic cleanup is enabled, use this to disable.</p>
<dt><code>&#8211;offline</code></p>
<dd> Run in &#8216;offline&#8217; mode where we tell &#8216;yum&#8217; to run completely from local cache. Also disables cache expiry for the mock yum cache.</p>
<dt><code>&#8211;old-chroot</code></p>
<dd> use old chroot instead of systemd-nspawn.</p>
<dt><code>&#8211;plugin-option </code><i>PLUGIN</i><code>:</code><i>KEY</i><code>=</code><i>VALUE</i></p>
<dd> Set plugin specific parameter. This option may be used multiple times. Examples: </p>
<p> <code>&#8211;plugin-option=root_cache:age_check=False</code> </p>
<p> <code>&#8211;plugin-option=mount:dirs=(&quot;/dev/device&quot;, &quot;/mount/path/in/chroot/&quot;, &quot;vfstype&quot;, &quot;mount_options&quot;)</code></p>
<dt><code>&#8211;postinstall</code></p>
<dd> Try to install built packages in the same buildroot right after build.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Be quiet.</p>
<dt><code>-r</code> <i>CONFIG</i>, <code>&#8211;root</code>=<i>CONFIG</i></p>
<dd> Uses specified chroot configuration as defined in /etc/mock/&lt;<i>CONFIG</i>&gt;.cfg. Optionally if CONFIG ends in &#8216;.cfg&#8217;, it is interpreted as full path to config file. If none specified, uses the chroot config linked to by /etc/mock/default.cfg.</p>
<dt><code>&#8211;resultdir</code>=<i>RESULTDIR</i></p>
<dd> Change directory where resulting files (RPMs and build logs) are written. Resultdir can contain python-string substitutions for any variable in the chroot config. For example: </p>
<p> <code>&#8211;resultdir=./my/&quot;%(dist)s&quot;/&quot;%(target_arch)s&quot;/</code> </p>
<p> This option enables automatic cleanup, this can be changed in config file (by cleanup_on_success, cleanup_on_failure configuration options) or overridden by &#8211;no-cleanup-after/&#8211;cleanup-after arguments.</p>
<dt><code>&#8211;rootdir</code>=<i>ROOTDIR</i></p>
<dd> Path for where the chroot should be built. By default it is created in /var/lib/mock/&lt;<i>CONFIG</i>&gt;/root/.</p>
<dt><code>&#8211;rpmbuild-opts</code>=<i>OPTIONS</i></p>
<dd> Pass additional options to rpmbuild. To pass more options, put them in quotes.</p>
<dt><code>&#8211;rpmbuild_timeout</code>=<i>SECONDS</i></p>
<dd> Fail build if rpmbuild takes longer than &#8216;timeout&#8217; seconds</p>
<dt><code>&#8211;scm-option</code>=<i>OPTIONS</i></p>
<dd> define an SCM option (may be used more than once).</p>
<dt><code>&#8211;short-circuit</code>=<i>STAGE</i></p>
<dd> Use rpmbuild&#8217;s short-circuit mechanism to skip already executed stages of build. It doesn&#8217;t produce RPMs, it&#8217;s useful only for debugging packaging. Implies <i>&#8211;no-clean</i>. STAGE specifies which stage will be executed as the first. Available values: prep, build, install, binary.</p>
<dt><code>&#8211;symlink-dereference</code></p>
<dd> Follow symlinks in sources (used only with &#8211;buildsrpm).</p>
<dt><code>&#8211;target</code>=<i>ARCH</i></p>
<dd> This argument is passed to rpmbuild to specify the target arch to build. It defaults to whatever is specified for &#8211;arch, or whatever is specified in the config file as config_opts[&#8216;target_arch&#8217;].</p>
<dt><code>&#8211;trace</code></p>
<dd> Enables verbose tracing of function enter/exit with function arguments and return codes. Useful for debugging mock itself.</p>
<dt><code>&#8211;uniqueext</code>=<i>text</i></p>
<dd> Arbitrary, unique extension to append to chroot directory name</p>
<dt><code>&#8211;unpriv</code></p>
<dd> Drop privileges before running command when using &#8211;chroot</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Output verbose progress information.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version number and exit.</p>
<dt><code>&#8211;with</code>=<i>OPTION</i></p>
<dd> Enable configure OPTION for build. This option may be used multiple times. For example: </p>
<p> <code>&#8211;with=extra_cheese</code></p>
<dt><code>&#8211;without</code>=<i>OPTION</i></p>
<dd> Disable configure OPTION for build. This option may be used multiple times. For example: </p>
<p> <code>&#8211;without=anchovies</code></p>
<dt><code>&#8211;yum</code></p>
<dd> Use yum as the current package manager. This is the default. </p>
</dl>
<h2>FILES</h2>
<p> <i>/etc/mock/</i> &#8211; default configuration directory </p>
<p> <i>/var/lib/mock</i> &#8211; directory where chroots and results are created. You should not put there your input files.</p>
<h2>EXAMPLES</h2>
<p> To rebuild test.src.rpm using the Fedora 14 configuration for x86_64 </p>
<dl>
<dt>
<dd> <code>mock -r fedora-14-x86_64 &#8211;rebuild /path/to/test.src.rpm</dl>
<p> Note that the available configurations are found in the /etc/mock directory with the extension .cfg. To specify a configuration use the filename without the trailing .cfg extension. </p>
<p> To place the output RPMs and logs in a specified location. </p>
<dl>
<dt>
<dd> mock -r fedora-14-i386 &#8211;resultdir=./my-results /path/to/your.src.rpm</code></dl>
<p> To build a package from the default SCM repository configured in site-defaults.cfg use the following arguments. </p>
<dl>
<dt>
<dd> <code>mock -r fedora-14-i386 &#8211;scm-enable &#8211;scm-option package=pkg</code></dl>
<p> To build execute command inside of chroot. </p>
<dl>
<dt>
<dd> <code>mock -r fedora-21-x86_64 &#8211;chroot &#8212; rpm &#8211;eval %dist</code> </p>
<p> <code>mock -r fedora-21-x86_64 &#8211;chroot &#8216;rpm &#8211;eval %dist&#8217;</code></dl>
<p> To build rawhide package using yum: </p>
<dl>
<dt>
<dd> <code>mock -r fedora-rawhide-x86_64 &#8211;yum &#8211;rebuild your.src.rpm</code></dl>
<p> Query rpm database inside chroot using Yum: </p>
<dl>
<dt>
<dd> <code>mock -r fedora-rawhide-x86_64 &#8211;yum-cmd whatprovides foo</code></dl>
<p> List package manager history using package manager which is configured in chroot config (can be either DNF or YUM): </p>
<dl>
<dt>
<dd> <code>mock -r fedora-rawhide-x86_64 &#8211;pm-cmd history list</code></dl>
<h2>BUGS</h2>
<p> To report bugs in mock, go to: </p>
<dl>
<dt>
<dd> <i><a rel="nofollow" href="https://apps.fedoraproject.org/packages/mock/">https://apps.fedoraproject.org/packages/mock/</a></i>.</dl>
<p> Select the <code>Bugs</code> tab. If there is a bug similar to the one you are seeing, add your information to the comments. If not, press <code>Open A New Bug</code> and fill in the form.</p>
<h2>AUTHORS</h2>
<p> Michael Brown &lt;mebrown1.3.3&quot;michaels-house.net&gt; </p>
<p> Clark Williams &lt;williams1.3.3&quot;redhat.com&gt; </p>
<p> Seth Vidal &lt;skvidal1.3.3&quot;linux.duke.edu&gt; </p>
<p> and a cast of&#8230;tens</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mockchain/">mockchain</a>(1), <a href="/docs/linux/man/8-rpmbuild/">rpmbuild</a>(8), <a href="/docs/linux/man/8-yum/">yum</a>(8), <a rel="nofollow" href="https://fedoraproject.org/wiki/Mock">https://fedoraproject.org/wiki/Mock</a> </p>
<h2>Index</h2>
