---
title: "dpkg-buildpackage(1)"
name: "dpkg-buildpackage"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-buildpackage/"
description: "dpkg-buildpackage – build binary or source packages from sources"
---

<h2 class="name">NAME</h2>
<p> dpkg-buildpackage &#8211; build binary or source packages from sources </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-buildpackage</code> [<i>option</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dpkg-buildpackage</code> is a program that automates the process of building a Debian package. It consists of the following steps:</p>
<dl>
<dt><code>1.</code></p>
<dd> It prepares the build environment by setting various environment variables (see <font SIZE="-1"><code>ENVIRONMENT</code></font>), runs the <code>init</code> hook, and calls <code>dpkg-source &#8211;before-build</code> (unless <code>-T</code> or <code>&#8211;target</code> has been used).</p>
<dt><code>2.</code></p>
<dd> It checks that the build-dependencies and build-conflicts are satisfied (unless <code>-d</code> or <code>&#8211;no-check-builddeps</code> is specified).</p>
<dt><code>3.</code></p>
<dd> If one or more specific targets have been selected with the <code>-T</code> or <code>&#8211;target</code> option, it calls those targets and stops here. Otherwise it runs the <code>preclean</code> hook and calls <code>fakeroot debian/rules clean</code> to clean the build-tree (unless <code>-nc</code> or <code>&#8211;no-pre-clean</code> is specified).</p>
<dt><code>4.</code></p>
<dd> It runs the <code>source</code> hook and calls <code>dpkg-source -b</code> to generate the source package (if a <code>source</code> build has been requested with <code>&#8211;build</code> or equivalent options).</p>
<dt><code>5.</code></p>
<dd> It runs the <code>build</code> hook and calls <code>debian/rules</code> <i>build-target</i>, then runs the <code>binary</code> hook followed by <code>fakeroot debian/rules</code> <i>binary-target</i> (unless a source-only build has been requested with <code>&#8211;build=source</code> or equivalent options). Note that <i>build-target</i> and <i>binary-target</i> are either <code>build</code> and <code>binary</code> (default case, or if an <code>any</code> and <code>all</code> build has been requested with <code>&#8211;build</code> or equivalent options), or <code>build-arch</code> and <code>binary-arch</code> (if an <code>any</code> and not <code>all</code> build has been requested with <code>&#8211;build</code> or equivalent options), or <code>build-indep</code> and <code>binary-indep</code> (if an <code>all</code> and not <code>any</code> build has been requested with <code>&#8211;build</code> or equivalent options).</p>
<dt><code>6.</code></p>
<dd> It runs the <code>buildinfo</code> hook and calls <code>dpkg-genbuildinfo</code> to generate a <code>.buildinfo</code> file. Several <code>dpkg-buildpackage</code> options are forwarded to <code>dpkg-genbuildinfo</code>.</p>
<dt><code>7.</code></p>
<dd> It runs the <code>changes</code> hook and calls <code>dpkg-genchanges</code> to generate a <code>.changes</code> file. The name of the <code>.changes</code> file will depend on the type of build and will be as specific as necessary but not more; for a build that includes <code>any</code> the name will be <i>source-name</i><code>_</code><i>binary-version</i><code>_</code><i>arch</i><code>.changes</code>, or otherwise for a build that includes <code>all</code> the name will be <i>source-name</i><code>_</code><i>binary-version</i><code>_</code><code>all.changes</code>, or otherwise for a build that includes <code>source</code> the name will be <i>source-name</i><code>_</code><i>source-version</i><code>_</code><code>source.changes</code>. Many <code>dpkg-buildpackage</code> options are forwarded to <code>dpkg-genchanges</code>.</p>
<dt><code>8.</code></p>
<dd> It runs the <code>postclean</code> hook and if <code>-tc</code> or <code>&#8211;post-clean</code> is specified, it will call <code>fakeroot debian/rules clean</code> again.</p>
<dt><code>9.</code></p>
<dd> It calls <code>dpkg-source &#8211;after-build</code>.</p>
<dt><code>10.</code></p>
<dd> It runs the <code>check</code> hook and calls a package checker for the <code>.changes</code> file (if a command is specified in <font SIZE="-1"><code>DEB_CHECK_COMMAND</code></font> or with <code>&#8211;check-command</code>).</p>
<dt><code>11.</code></p>
<dd> It runs the <code>sign</code> hook and calls <code>gpg</code> (as long as it is not an <font SIZE="-1">UNRELEASED</font> build, or <code>&#8211;no-sign</code> is specified) to sign the <code>.dsc</code> file (if any, unless <code>-us</code> or <code>&#8211;unsigned-source</code> is specified), the <code>.buildinfo</code> file (unless <code>-ui</code>, <code>&#8211;unsigned-buildinfo</code>, <code>-uc</code> or <code>&#8211;unsigned-changes</code> is specified) and the <code>.changes</code> file (unless <code>-uc</code> or <code>&#8211;unsigned-changes</code> is specified).</p>
<dt><code>12.</code></p>
<dd> It runs the <code>done</code> hook.</dl>
<h2>OPTIONS</h2>
<p> All long options can be specified both on the command line and in the <code>dpkg-buildpackage</code> system and user configuration files. Each line in the configuration file is either an option (exactly the same as the command line option but without leading hyphens) or a comment (if it starts with a &#8216;<code>#</code>&#8216;).</p>
<dl>
<dt><code>&#8211;build=</code><i>type</i></p>
<dd> Specifies the build <i>type</i> from a comma-separated list of components (since dpkg 1.18.5). Passed to <code>dpkg-genchanges</code>. </p>
<p> The allowed values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>source</code></p>
<dd> Builds the source package. </p>
<p> <code>Note:</code> When using this value standalone and if what you want is simply to (re-)build the source package from a clean source tree, using <code>dpkg-source</code> directly is always a better option as it does not require any build dependencies to be installed which are otherwise needed to be able to call the <code>clean</code> target.</p>
<dt><code>any</code></p>
<dd> Builds the architecture specific binary packages.</p>
<dt><code>all</code></p>
<dd> Builds the architecture independent binary packages.</p>
<dt><code>binary</code></p>
<dd> Builds the architecture specific and independent binary packages. This is an alias for <code>any,all</code>.</p>
<dt><code>full</code></p>
<dd> Builds everything. This is an alias for <code>source,any,all</code>, and the same as the default case when no build option is specified.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-g</code></p>
<dd> Equivalent to <code>&#8211;build=source,all</code> (since dpkg 1.17.11).</p>
<dt><code>-G</code></p>
<dd> Equivalent to <code>&#8211;build=source,any</code> (since dpkg 1.17.11).</p>
<dt><code>-b</code></p>
<dd> Equivalent to <code>&#8211;build=binary</code> or <code>&#8211;build=any,all</code>.</p>
<dt><code>-B</code></p>
<dd> Equivalent to <code>&#8211;build=any</code>.</p>
<dt><code>-A</code></p>
<dd> Equivalent to <code>&#8211;build=all</code>.</p>
<dt><code>-S</code></p>
<dd> Equivalent to <code>&#8211;build=source</code>.</p>
<dt><code>-F</code></p>
<dd> Equivalent to <code>&#8211;build=full</code>, <code>&#8211;build=source,binary</code> or <code>&#8211;build=source,any,all</code> (since dpkg 1.15.8).</p>
<dt><code>&#8211;target=</code><i>target</i>[,&#8230;]</p>
<dd>
<dt><code>&#8211;target</code> <i>target</i>[,&#8230;]</p>
<dd>
<dt><code>-T</code>, <code>&#8211;rules-target=</code><i>target</i>[,&#8230;]</p>
<dd> Calls <code>debian/rules</code> <i>target</i> once per target specified, after having setup the build environment (except for calling <code>dpkg-source &#8211;before-build</code>), and stops the package build process here (since dpkg 1.15.0, long option since dpkg 1.18.8, multi-target support since dpkg 1.18.16). If <code>&#8211;as-root</code> is also given, then the command is executed as root (see <code>&#8211;root-command</code>). Note that known targets that are required to be run as root do not need this option (i.e. the <code>clean</code>, <code>binary</code>, <code>binary-arch</code> and <code>binary-indep</code> targets).</p>
<dt><code>&#8211;as-root</code></p>
<dd> Only meaningful together with <code>&#8211;target</code> (since dpkg 1.15.0). Requires that the target be run with root rights.</p>
<dt><code>-si</code></p>
<dd>
<dt><code>-sa</code></p>
<dd>
<dt><code>-sd</code></p>
<dd>
<dt><code>-v</code><i>version</i></p>
<dd>
<dt><code>-C</code><i>changes-description</i></p>
<dd>
<dt><code>-m</code>, <code>&#8211;release-by=</code><i>maintainer-address</i></p>
<dd>
<dt><code>-e</code>, <code>&#8211;build-by=</code><i>maintainer-address</i></p>
<dd> Passed unchanged to <code>dpkg-genchanges</code>. See its manual page.</p>
<dt><code>-a</code>, <code>&#8211;host-arch</code> <i>architecture</i></p>
<dd> Specify the Debian architecture we build for (long option since dpkg 1.17.17). The architecture of the machine we build on is determined automatically, and is also the default for the host machine.</p>
<dt><code>-t</code>, <code>&#8211;host-type</code> <i>gnu-system-type</i></p>
<dd> Specify the <font SIZE="-1">GNU</font> system type we build for (long option since dpkg 1.17.17). It can be used in place of <code>&#8211;host-arch</code> or as a complement to override the default <font SIZE="-1">GNU</font> system type of the host Debian architecture.</p>
<dt><code>&#8211;target-arch</code> <i>architecture</i></p>
<dd> Specify the Debian architecture the binaries built will build for (since dpkg 1.17.17). The default value is the host machine.</p>
<dt><code>&#8211;target-type</code> <i>gnu-system-type</i></p>
<dd> Specify the <font SIZE="-1">GNU</font> system type the binaries built will build for (since dpkg 1.17.17). It can be used in place of <code>&#8211;target-arch</code> or as a complement to override the default <font SIZE="-1">GNU</font> system type of the target Debian architecture.</p>
<dt><code>-P</code>, <code>&#8211;build-profiles=</code><i>profile</i>[<code>,</code>&#8230;]</p>
<dd> Specify the profile(s) we build, as a comma-separated list (since dpkg 1.17.2, long option since dpkg 1.18.8). The default behavior is to build for no specific profile. Also sets them (as a space separated list) as the <font SIZE="-1"><code>DEB_BUILD_PROFILES</code></font> environment variable which allows, for example, <code>debian/rules</code> files to use this information for conditional builds.</p>
<dt><code>-j</code>, <code>&#8211;jobs</code>[=<i>jobs</i>|<code>auto</code>]</p>
<dd> Number of jobs allowed to be run simultaneously, number of jobs matching the number of online processors if <code>auto</code> is specified (since dpkg 1.17.10), or unlimited number if <i>jobs</i> is not specified, equivalent to the <code><a href="/docs/linux/man/1-make/">make</a></code>(1) option of the same name (since dpkg 1.14.7, long option since dpkg 1.18.8). Will add itself to the <font SIZE="-1"><code>MAKEFLAGS</code></font> environment variable, which should cause all subsequent make invocations to inherit the option, thus forcing the parallel setting on the packaging (and possibly the upstream build system if that uses make) regardless of their support for parallel builds, which might cause build failures. Also adds <code>parallel=</code><i>jobs</i> or <code>parallel</code> to the <font SIZE="-1"><code>DEB_BUILD_OPTIONS</code></font> environment variable which allows debian/rules files to use this information for their own purposes. The <code>-j</code> value will override the <code>parallel=</code><i>jobs</i> or <code>parallel</code> option in the <font SIZE="-1"><code>DEB_BUILD_OPTIONS</code></font> environment variable. Note that the <code>auto</code> value will get replaced by the actual number of currently active processors, and as such will not get propagated to any child process. If the number of online processors cannot be inferred then the code will fallback to using serial execution (since dpkg 1.18.15), although this should only happen on exotic and unsupported systems.</p>
<dt><code>-J</code>, <code>&#8211;jobs-try</code>[=<i>jobs</i>|<code>auto</code>]</p>
<dd> This option (since dpkg 1.18.2, long option since dpkg 1.18.8) is equivalent to the <code>-j</code> option except that it does not set the <font SIZE="-1"><code>MAKEFLAGS</code></font> environment variable, and as such it is safer to use with any package including those that are not parallel-build safe. </p>
<p> <code>auto</code> is the default behavior (since dpkg 1.18.11). Setting the number of jobs to 1 will restore a serial behavior.</p>
<dt><code>-D</code>, <code>&#8211;check-builddeps</code></p>
<dd> Check build dependencies and conflicts; abort if unsatisfied (long option since dpkg 1.18.8). This is the default behavior.</p>
<dt><code>-d</code>, <code>&#8211;no-check-builddeps</code></p>
<dd> Do not check build dependencies and conflicts (long option since dpkg 1.18.8).</p>
<dt><code>&#8211;ignore-builtin-builddeps</code></p>
<dd> Do not check built-in build dependencies and conflicts (since dpkg 1.18.2). These are the distribution specific implicit build dependencies usually required in a build environment, the so called Build-Essential package set.</p>
<dt><code>&#8211;rules-requires-root</code></p>
<dd> Do not honor the <code>Rules-Requires-Root</code> field, falling back to its legacy default value (since dpkg 1.19.1).</p>
<dt><code>-nc</code>, <code>&#8211;no-pre-clean</code></p>
<dd> Do not clean the source tree before building (long option since dpkg 1.18.8). Implies <code>-b</code> if nothing else has been selected among <code>-F</code>, <code>-g</code>, <code>-G</code>, <code>-B</code>, <code>-A</code> or <code>-S</code>. Implies <code>-d</code> with <code>-S</code> (since dpkg 1.18.0).</p>
<dt><code>&#8211;pre-clean</code></p>
<dd> Clean the source tree before building (since dpkg 1.18.8). This is the default behavior.</p>
<dt><code>-tc</code>, <code>&#8211;post-clean</code></p>
<dd> Clean the source tree (using <i>gain-root-command</i> <code>debian/rules clean</code>) after the package has been built (long option since dpkg 1.18.8).</p>
<dt><code>&#8211;no-post-clean</code></p>
<dd> Do not clean the source tree after the package has been built (since dpkg 1.19.1). This is the default behavior.</p>
<dt><code>&#8211;sanitize-env</code></p>
<dd> Sanitize the build environment (since dpkg 1.20.0). This will reset or remove environment variables, umask, and any other process attributes that might otherwise adversely affect the build of packages. Because the official entry point to build packages is <code>debian/rules</code>, packages cannot rely on these settings being in place, and thus should work even when they are not. What to sanitize is vendor specific.</p>
<dt><code>-r</code>, <code>&#8211;root-command=</code><i>gain-root-command</i></p>
<dd> When <code>dpkg-buildpackage</code> needs to execute part of the build process as root, it prefixes the command it executes with <i>gain-root-command</i> if one has been specified (long option since dpkg 1.18.8). Otherwise, if none has been specified, <code>fakeroot</code> will be used by default, if the command is present. <i>gain-root-command</i> should start with the name of a program on the <font SIZE="-1"><code>PATH</code></font> and will get as arguments the name of the real command to run and the arguments it should take. <i>gain-root-command</i> can include parameters (they must be space-separated) but no shell metacharacters. <i>gain-root-command</i> might typically be <code>fakeroot</code>, <code>sudo</code>, <code>super</code> or <code>really</code>. <code>su</code> is not suitable, since it can only invoke the user&#8217;s shell with <code>-c</code> instead of passing arguments individually to the command to be run.</p>
<dt><code>-R</code>, <code>&#8211;rules-file=</code><i>rules-file</i></p>
<dd> Building a Debian package usually involves invoking <code>debian/rules</code> as a command with several standard parameters (since dpkg 1.14.17, long option since dpkg 1.18.8). With this option it&#8217;s possible to use another program invocation to build the package (it can include space separated parameters). Alternatively it can be used to execute the standard rules file with another make program (for example by using <code>/usr/local/bin/make -f debian/rules</code> as <i>rules-file</i>).</p>
<dt><code>&#8211;check-command=</code><i>check-command</i></p>
<dd> Command used to check the <code>.changes</code> file itself and any artifact built referenced in the file (since dpkg 1.17.6). The command should take the <code>.changes</code> pathname as an argument. This command will usually be <code>lintian</code>.</p>
<dt><code>&#8211;check-option=</code><i>opt</i></p>
<dd> Pass option <i>opt</i> to the <i>check-command</i> specified with <font SIZE="-1"><code>DEB_CHECK_COMMAND</code></font> or <code>&#8211;check-command</code> (since dpkg 1.17.6). Can be used multiple times.</p>
<dt><code>&#8211;hook-</code><i>hook-name</i><code>=</code><i>hook-command</i></p>
<dd> Set the specified shell code <i>hook-command</i> as the hook <i>hook-name</i>, which will run at the times specified in the run steps (since dpkg 1.17.6). The hooks will always be executed even if the following action is not performed (except for the <code>binary</code> hook). All the hooks will run in the unpacked source directory. </p>
<p> <code>Note:</code> Hooks can affect the build process, and cause build failures if their commands fail, so watch out for unintended consequences. </p>
<p> The current <i>hook-name</i> supported are: </p>
<p> <code>init preclean source build binary buildinfo changes postclean check sign done</code> </p>
<p> The <i>hook-command</i> supports the following substitution format string, which will get applied to it before execution:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>%%</code></p>
<dd> A single % character.</p>
<dt>%a</p>
<dd> A boolean value (0 or 1), representing whether the following action is being performed.</p>
<dt>%p</p>
<dd> The source package name.</p>
<dt>%v</p>
<dd> The source package version.</p>
<dt>%s</p>
<dd> The source package version (without the epoch).</p>
<dt>%u</p>
<dd> The upstream version.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;buildinfo-file=</code><i>filename</i></p>
<dd> Set the <i>filename</i> for the generated <code>.buildinfo</code> file (since dpkg 1.21.0).</p>
<dt><code>&#8211;buildinfo-option=</code><i>opt</i></p>
<dd> Pass option <i>opt</i> to <code>dpkg-genbuildinfo</code> (since dpkg 1.18.11). Can be used multiple times.</p>
<dt><code>-p</code>, <code>&#8211;sign-command=</code><i>sign-command</i></p>
<dd> When <code>dpkg-buildpackage</code> needs to execute <font SIZE="-1">GPG</font> to sign a source control (<code>.dsc</code>) file or a <code>.changes</code> file it will run <i>sign-command</i> (searching the <font SIZE="-1"><code>PATH</code></font> if necessary) instead of <code>gpg</code> (long option since dpkg 1.18.8). <i>sign-command</i> will get all the arguments that <code>gpg</code> would have gotten. <i>sign-command</i> should not contain spaces or any other shell metacharacters.</p>
<dt><code>-k</code>, <code>&#8211;sign-key=</code><i>key-id</i></p>
<dd> Specify a key-ID to use when signing packages (long option since dpkg 1.18.8).</p>
<dt><code>-us</code>, <code>&#8211;unsigned-source</code></p>
<dd> Do not sign the source package (long option since dpkg 1.18.8).</p>
<dt><code>-ui</code>, <code>&#8211;unsigned-buildinfo</code></p>
<dd> Do not sign the <code>.buildinfo</code> file (since dpkg 1.18.19).</p>
<dt><code>-uc</code>, <code>&#8211;unsigned-changes</code></p>
<dd> Do not sign the <code>.buildinfo</code> and <code>.changes</code> files (long option since dpkg 1.18.8).</p>
<dt><code>&#8211;no-sign</code></p>
<dd> Do not sign any file, this includes the source package, the <code>.buildinfo</code> file and the <code>.changes</code> file (since dpkg 1.18.20).</p>
<dt><code>&#8211;force-sign</code></p>
<dd> Force the signing of the resulting files (since dpkg 1.17.0), regardless of <code>-us</code>, <code>&#8211;unsigned-source</code>, <code>-ui</code>, <code>&#8211;unsigned-buildinfo</code>, <code>-uc</code>, <code>&#8211;unsigned-changes</code> or other internal heuristics.</p>
<dt><code>-sn</code></p>
<dd>
<dt><code>-ss</code></p>
<dd>
<dt><code>-sA</code></p>
<dd>
<dt><code>-sk</code></p>
<dd>
<dt><code>-su</code></p>
<dd>
<dt><code>-sr</code></p>
<dd>
<dt><code>-sK</code></p>
<dd>
<dt><code>-sU</code></p>
<dd>
<dt><code>-sR</code></p>
<dd>
<dt><code>-i</code>, <code>&#8211;diff-ignore</code>[=<i>regex</i>]</p>
<dd>
<dt><code>-I</code>, <code>&#8211;tar-ignore</code>[=<i>pattern</i>]</p>
<dd>
<dt><code>-z</code>, <code>&#8211;compression-level=</code><i>level</i></p>
<dd>
<dt><code>-Z</code>, <code>&#8211;compression=</code><i>compressor</i></p>
<dd> Passed unchanged to <code>dpkg-source</code>. See its manual page.</p>
<dt><code>&#8211;source-option=</code><i>opt</i></p>
<dd> Pass option <i>opt</i> to <code>dpkg-source</code> (since dpkg 1.15.6). Can be used multiple times.</p>
<dt><code>&#8211;changes-file=</code><i>filename</i></p>
<dd> Set the <i>filename</i> for the generated <code>.changes</code> file (since dpkg 1.21.0).</p>
<dt><code>&#8211;changes-option=</code><i>opt</i></p>
<dd> Pass option <i>opt</i> to <code>dpkg-genchanges</code> (since dpkg 1.15.6). Can be used multiple times.</p>
<dt><code>&#8211;admindir=</code><i>dir</i></p>
<dd>
<dt><code>&#8211;admindir</code> <i>dir</i></p>
<dd> Change the location of the <code>dpkg</code> database (since dpkg 1.14.0). The default location is <i>/var/lib/dpkg</i>.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Show the usage message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version and exit.</dl>
<h2>ENVIRONMENT</h2>
<h3>External environment</h3>
<dl>
<dt><font SIZE="-1"><code>DEB_CHECK_COMMAND</code></font></p>
<dd> If set, it will be used as the command to check the <code>.changes</code> file (since dpkg 1.17.6). Overridden by the <code>&#8211;check-command</code> option.</p>
<dt><font SIZE="-1"><code>DEB_SIGN_KEYID</code></font></p>
<dd> If set, it will be used to sign the <code>.changes</code> and <code>.dsc</code> files (since dpkg 1.17.2). Overridden by the <code>&#8211;sign-key</code> option.</p>
<dt><font SIZE="-1"><code>DEB_BUILD_OPTIONS</code></font></p>
<dd> If set, it will contain a space-separated list of options that might affect the build process in <i>debian/rules</i>, and the behavior of some dpkg commands. </p>
<p> With <code>nocheck</code> the <font SIZE="-1"><code>DEB_CHECK_COMMAND</code></font> variable will be ignored. With <code>parallel=</code><i>N</i> the parallel jobs will be set to <i>N</i>, overridden by the <code>&#8211;jobs-try</code> option.</p>
<dt><font SIZE="-1"><code>DEB_BUILD_PROFILES</code></font></p>
<dd> If set, it will be used as the active build profile(s) for the package being built (since dpkg 1.17.2). It is a space separated list of profile names. Overridden by the <code>-P</code> option.</p>
<dt><font SIZE="-1"><code>DPKG_COLORS</code></font></p>
<dd> Sets the color mode (since dpkg 1.18.5). The currently accepted values are: <code>auto</code> (default), <code>always</code> and <code>never</code>.</p>
<dt><font SIZE="-1"><code>DPKG_NLS</code></font></p>
<dd> If set, it will be used to decide whether to activate Native Language Support, also known as internationalization (or i18n) support (since dpkg 1.19.0). The accepted values are: <code>0</code> and <code>1</code> (default).</dl>
<h3>Internal environment</h3>
<p> Even if <code>dpkg-buildpackage</code> exports some variables, <code>debian/rules</code> should not rely on their presence and should instead use the respective interface to retrieve the needed values, because that file is the main entry point to build packages and running it standalone should be supported.</p>
<dl>
<dt><code>DEB_BUILD_*</code></p>
<dd>
<dt><code>DEB_HOST_*</code></p>
<dd>
<dt><code>DEB_TARGET_*</code></p>
<dd> <code>dpkg-architecture</code> is called with the <code>-a</code> and <code>-t</code> parameters forwarded. Any variable that is output by its <code>-s</code> option is integrated in the build environment.</p>
<dt><font SIZE="-1"><code>DEB_RULES_REQUIRES_ROOT</code></font></p>
<dd> This variable is set to the value obtained from the <code>Rules-Requires-Root</code> field or from the command-line. When set, it will be a valid value for the <code>Rules-Requires-Root</code> field. It is used to notify <code>debian/rules</code> whether the <code>rootless-builds.txt</code> specification is supported.</p>
<dt><font SIZE="-1"><code>DEB_GAIN_ROOT_CMD</code></font></p>
<dd> This variable is set to <i>gain-root-command</i> when the field <code>Rules-Requires-Root</code> is set to a value different to <code>no</code> and <code>binary-targets</code>.</p>
<dt><font SIZE="-1"><code>SOURCE_DATE_EPOCH</code></font></p>
<dd> This variable is set to the Unix timestamp since the epoch of the latest entry in <i>debian/changelog</i>, if it is not already defined.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/dpkg/buildpackage.conf</i></p>
<dd> System wide configuration file</p>
<dt><i></i>$XDG_CONFIG_HOME<i>/dpkg/buildpackage.conf</i> or</p>
<dd>
<dt><i></i>$HOME<i>/.config/dpkg/buildpackage.conf</i></p>
<dd> User configuration file.</dl>
<h2>NOTES</h2>
<h3>Compiler flags are no longer exported</h3>
<p> Between dpkg 1.14.17 and 1.16.1, <code>dpkg-buildpackage</code> exported compiler flags (<font SIZE="-1"><code>CFLAGS</code></font>, <font SIZE="-1"><code>CXXFLAGS</code></font>, <font SIZE="-1"><code>FFLAGS</code></font>, <font SIZE="-1"><code>CPPFLAGS</code></font> and <font SIZE="-1"><code>LDFLAGS</code></font>) with values as returned by <code>dpkg-buildflags</code>. This is no longer the case.</p>
<h3>Default build targets</h3>
<p> <code>dpkg-buildpackage</code> is using the <code>build-arch</code> and <code>build-indep</code> targets since dpkg 1.16.2. Those targets are thus mandatory. But to avoid breakages of existing packages, and ease the transition, if the source package does not build both architecture independent and dependent binary packages (since dpkg 1.18.8) it will fallback to use the <code>build</code> target if <code>make -f debian/rules -qn</code> <i>build-target</i> returns 2 as exit code.</p>
<h2>BUGS</h2>
<p> It should be possible to specify spaces and shell metacharacters and initial arguments for <i>gain-root-command</i> and <i>sign-command</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dpkg-source/">dpkg-source</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-architecture/">dpkg-architecture</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-buildflags/">dpkg-buildflags</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-genbuildinfo/">dpkg-genbuildinfo</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-genchanges/">dpkg-genchanges</a></code>(1), <code><a href="/docs/linux/man/1-fakeroot/">fakeroot</a></code>(1), <code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1), <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1). </p>
<h2>Index</h2>
