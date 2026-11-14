---
title: "rpkg(1)"
name: "rpkg"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpkg/"
description: "rpkg – RPM Packaging utility"
---

<h2>NAME</h2>
<p> rpkg &#8211; RPM Packaging utility</p>
<h2>SYNOPSIS</h2>
<p> <code>rpkg</code> [ <i>global_options</i> ] <i>command</i> [ <i>command_options</i> ] [ <i>command_arguments</i> ]<br />
 <code>rpkg</code> <code>help</code><br />
 <code>rpkg</code> <i>command</i> <code>&#8211;help</code></p>
<h2>DESCRIPTION</h2>
<p> <code>rpkg</code> is a script to interact with the RPM Packaging system.</p>
<h3>Global Options</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;config CONFIG, -C CONFIG<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Specify a config file to use<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;release RELEASE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Override the discovered release from current branch,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>which is used to determine the build target and value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>of dist macro. Generally, release is the name of a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>branch created in your package repository. &#8211;release<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>is an alias of &#8211;dist, hence &#8211;release should be<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>instead.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;dist DIST&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Deprecated. Use &#8211;release instead. You can use &#8211;dist<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>for a while for backward-compatibility. It will be<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>disabled in future version.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;module-name MODULE_NAME<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Override the module name. Otherwise it is discovered<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>from: Git push URL or Git URL&nbsp;<wbr>(last part of path with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>.git extension removed)&nbsp;<wbr>or from name macro in spec<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>file. In that order.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;user USER&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Override the discovered user name<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;password PASSWORD&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Password for Koji login<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;runas RUNAS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Run Koji commands as a different user<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;path PATH&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Define the directory to work in&nbsp;<wbr>(defaults to cwd)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;verbose, -v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Run with verbose debug output<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;debug, -d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Run with debug output<br />
&nbsp;<wbr>&nbsp;<wbr>-q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Run quietly only displaying errors</p>
<h2>COMMAND OVERVIEW</h2>
<dl>
<dt><code>rpkg build [-h] [&#8211;arches [ARCHES [ARCHES &#8230;]]] [&#8211;md5] [&#8211;nowait] [&#8211;target TARGET] [&#8211;background] [&#8211;skip-nvr-check] [&#8211;skip-tag] [&#8211;scratch] [&#8211;srpm [SRPM]]</code></p>
<dd> Request build</p>
<dt><code>rpkg chain-build [-h] [&#8211;arches [ARCHES [ARCHES &#8230;]]] [&#8211;md5] [&#8211;nowait] [&#8211;target TARGET] [&#8211;background] package [package &#8230;]</code></p>
<dd> Build current package in order with other packages</p>
<dt><code>rpkg ci [-h] [-m MESSAGE] [&#8211;with-changelog] [-c] [&#8211;raw] [-t] [-F FILE] [-p] [-s] [files [files &#8230;]]</code></p>
<dd> Alias for commit</p>
<dt><code>rpkg clean [-h] [&#8211;dry-run] [-x]</code></p>
<dd> Remove untracked files</p>
<dt><code>rpkg clog [-h] [&#8211;raw]</code></p>
<dd> Make a clog file containing top changelog entry</p>
<dt><code>rpkg clone [-h] [&#8211;branches] [&#8211;branch BRANCH] [&#8211;anonymous] module [clone_target]</code></p>
<dd> Clone and checkout a module</p>
<dt><code>rpkg co [-h] [&#8211;branches] [&#8211;branch BRANCH] [&#8211;anonymous] module [clone_target]</code></p>
<dd> Alias for clone</p>
<dt><code>rpkg commit [-h] [-m MESSAGE] [&#8211;with-changelog] [-c] [&#8211;raw] [-t] [-F FILE] [-p] [-s] [files [files &#8230;]]</code></p>
<dd> Commit changes</p>
<dt><code>rpkg compile [-h] [&#8211;builddir BUILDDIR] [&#8211;arch ARCH] [&#8211;short-circuit] [&#8211;nocheck]</code></p>
<dd> Local test rpmbuild compile</p>
<dt><code>rpkg container-build [-h] [&#8211;repo-url [URL [URL &#8230;]]] [&#8211;osbs-config PATH] [&#8211;instance SECTION] [&#8211;scratch] [&#8211;target TARGET] [&#8211;build-with {koji,osbs}] [&#8211;nowait]</code></p>
<dd> build a container</p>
<dt><code>rpkg container-build-setup [-h] (&#8211;get-autorebuild | &#8211;set-autorebuild {true,false})</code></p>
<dd> set options for container-build</p>
<dt><code>rpkg copr-build [-h] [&#8211;nowait] project</code></p>
<dd> Build package in Copr</p>
<dt><code>rpkg diff [-h] [&#8211;cached] [files [files &#8230;]]</code></p>
<dd> Show changes between commits, commit and working tree, etc</p>
<dt><code>rpkg gimmespec [-h]</code></p>
<dd> Print the spec file name</p>
<dt><code>rpkg gitbuildhash [-h] build</code></p>
<dd> Print the git hash used to build the provided n-v-r</p>
<dt><code>rpkg giturl [-h]</code></p>
<dd> Print the git url for building</p>
<dt><code>rpkg help [-h]</code></p>
<dd> Show usage</p>
<dt><code>rpkg import [-h] [&#8211;skip-diffs] srpm</code></p>
<dd> Import srpm content into a module</p>
<dt><code>rpkg install [-h] [&#8211;builddir BUILDDIR] [&#8211;arch ARCH] [&#8211;short-circuit] [&#8211;nocheck]</code></p>
<dd> Local test rpmbuild install</p>
<dt><code>rpkg lint [-h] [&#8211;info] [&#8211;rpmlintconf RPMLINTCONF]</code></p>
<dd> Run rpmlint against local spec and build output if present.</p>
<dt><code>rpkg local [-h] [&#8211;builddir BUILDDIR] [&#8211;arch ARCH] [&#8211;md5]</code></p>
<dd> Local test rpmbuild binary</p>
<dt><code>rpkg mock-config [-h] [&#8211;target TARGET] [&#8211;arch ARCH]</code></p>
<dd> Generate a mock config</p>
<dt><code>rpkg mockbuild [-h] [&#8211;root CONFIG] [&#8211;md5] [&#8211;no-clean] [&#8211;no-cleanup-after] [&#8211;no-clean-all]</code></p>
<dd> Local test build using mock</p>
<dt><code>rpkg new [-h]</code></p>
<dd> Diff against last tag</p>
<dt><code>rpkg new-sources [-h] files [files &#8230;]</code></p>
<dd> Upload new source files</p>
<dt><code>rpkg patch [-h] [&#8211;rediff] suffix</code></p>
<dd> Create and add a gendiff patch file</p>
<dt><code>rpkg prep [-h] [&#8211;builddir BUILDDIR] [&#8211;arch ARCH]</code></p>
<dd> Local test rpmbuild prep</p>
<dt><code>rpkg pull [-h] [&#8211;rebase] [&#8211;no-rebase]</code></p>
<dd> Pull changes from the remote repository and update the working copy.</p>
<dt><code>rpkg push [-h] [&#8211;force]</code></p>
<dd> Push changes to remote repository</p>
<dt><code>rpkg scratch-build [-h] [&#8211;arches [ARCHES [ARCHES &#8230;]]] [&#8211;md5] [&#8211;nowait] [&#8211;target TARGET] [&#8211;background] [&#8211;srpm [SRPM]]</code></p>
<dd> Request scratch build</p>
<dt><code>rpkg sources [-h] [&#8211;outdir OUTDIR]</code></p>
<dd> Download source files</p>
<dt><code>rpkg srpm [-h] [&#8211;md5]</code></p>
<dd> Create a source rpm</p>
<dt><code>rpkg switch-branch [-h] [-l] [&#8211;fetch] [branch]</code></p>
<dd> Work with branches</p>
<dt><code>rpkg tag [-h] [-f] [-m MESSAGE] [-c] [&#8211;raw] [-F FILE] [-l] [-d] [tag]</code></p>
<dd> Management of git tags</p>
<dt><code>rpkg unused-patches [-h]</code></p>
<dd> Print list of patches not referenced by name in the specfile</p>
<dt><code>rpkg upload [-h] files [files &#8230;]</code></p>
<dd> Upload source files</p>
<dt><code>rpkg verify-files [-h] [&#8211;builddir BUILDDIR] [&#8211;arch ARCH]</code></p>
<dd> Locally verify %%files section</p>
<dt><code>rpkg verrel [-h]</code></p>
<dd> Print the name-version-release</dl>
<h2>COMMAND REFERENCE</h2>
<h3>rpkg build</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg build&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;arches&nbsp;<wbr>[ARCHES&nbsp;<wbr>[ARCHES &#8230;]]]&nbsp;<wbr>[&#8211;md5]&nbsp;<wbr>[&#8211;nowait]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;target TARGET]&nbsp;<wbr>[&#8211;background]&nbsp;<wbr>[&#8211;skip-nvr-check]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;skip-tag]&nbsp;<wbr>[&#8211;scratch]&nbsp;<wbr>[&#8211;srpm&nbsp;<wbr>[SRPM]]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>This command requests a build of the package in the build system. By default<br />
&nbsp;<wbr>&nbsp;<wbr>it discovers the target to build for based on branch data, and uses the latest<br />
&nbsp;<wbr>&nbsp;<wbr>commit as the build source.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;arches&nbsp;<wbr>[ARCHES&nbsp;<wbr>[ARCHES &#8230;]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Build for specific arches<br />
&nbsp;<wbr>&#8211;md5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use md5 checksums&nbsp;<wbr>(for older rpm hosts)<br />
&nbsp;<wbr>&#8211;nowait&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Don&#8217;t wait on build<br />
&nbsp;<wbr>&#8211;target TARGET&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Define build target to build into<br />
&nbsp;<wbr>&#8211;background&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Run the build at a low priority<br />
&nbsp;<wbr>&#8211;skip-nvr-check&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Submit build to buildsystem without check if NVR was<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>already build. NVR is constructed locally and may be<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>different from NVR constructed during build on<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>builder.<br />
&nbsp;<wbr>&#8211;skip-tag&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Do not attempt to tag package<br />
&nbsp;<wbr>&#8211;scratch&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Perform a scratch build<br />
&nbsp;<wbr>&#8211;srpm&nbsp;<wbr>[SRPM]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Build from an srpm. If no srpm is provided with this<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>option an srpm will be generated from current module<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>content.<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg chain-build</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg chain-build&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;arches&nbsp;<wbr>[ARCHES&nbsp;<wbr>[ARCHES &#8230;]]]&nbsp;<wbr>[&#8211;md5]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;nowait]&nbsp;<wbr>[&#8211;target TARGET]&nbsp;<wbr>[&#8211;background]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>package&nbsp;<wbr>[package &#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>Build current package in order with other packages.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>example: rpkg chain-build libwidget libgizmo<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>The current package is added to the end of the CHAIN list.<br />
&nbsp;<wbr>&nbsp;<wbr>Colons&nbsp;<wbr>(:)&nbsp;<wbr>can be used in the CHAIN parameter to define groups of<br />
&nbsp;<wbr>&nbsp;<wbr>packages.&nbsp;<wbr>&nbsp;<wbr>Packages in any single group will be built in parallel<br />
&nbsp;<wbr>&nbsp;<wbr>and all packages in a group must build successfully and populate<br />
&nbsp;<wbr>&nbsp;<wbr>the repository before the next group will begin building.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>For example:<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>rpkg chain-build libwidget libaselib : libgizmo :<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>will cause libwidget and libaselib to be built in parallel, followed<br />
&nbsp;<wbr>&nbsp;<wbr>by libgizmo and then the current directory package. If no groups are<br />
&nbsp;<wbr>&nbsp;<wbr>defined, packages will be built sequentially.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>positional arguments:<br />
&nbsp;<wbr>package&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>List the packages and order you want to build in<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;arches&nbsp;<wbr>[ARCHES&nbsp;<wbr>[ARCHES &#8230;]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Build for specific arches<br />
&nbsp;<wbr>&#8211;md5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use md5 checksums&nbsp;<wbr>(for older rpm hosts)<br />
&nbsp;<wbr>&#8211;nowait&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Don&#8217;t wait on build<br />
&nbsp;<wbr>&#8211;target TARGET&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Define build target to build into<br />
&nbsp;<wbr>&#8211;background&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Run the build at a low priority<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg ci</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg ci&nbsp;<wbr>[-h]&nbsp;<wbr>[-m MESSAGE]&nbsp;<wbr>[&#8211;with-changelog]&nbsp;<wbr>[-c]&nbsp;<wbr>[&#8211;raw]&nbsp;<wbr>[-t]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-F FILE]&nbsp;<wbr>[-p]&nbsp;<wbr>[-s]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[files&nbsp;<wbr>[files &#8230;]]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>Alias for commit.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>positional arguments:<br />
&nbsp;<wbr>files&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Optional list of specific files to commit<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>-m MESSAGE, &#8211;message MESSAGE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use the given&nbsp;<wbr>&lt;msg&gt;&nbsp;<wbr>as the commit message summary<br />
&nbsp;<wbr>&#8211;with-changelog&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Get the last changelog from SPEC as commit message<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>content. This option must be used with -m together.<br />
&nbsp;<wbr>-c, &#8211;clog&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Generate the commit message from the Changelog section<br />
&nbsp;<wbr>&#8211;raw&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Make the clog raw<br />
&nbsp;<wbr>-t, &#8211;tag&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Create a tag for this commit<br />
&nbsp;<wbr>-F FILE, &#8211;file FILE&nbsp;<wbr>&nbsp;<wbr>Take the commit message from the given file<br />
&nbsp;<wbr>-p, &#8211;push&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Commit and push as one action<br />
&nbsp;<wbr>-s, &#8211;signoff&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Include a signed-off-by<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg clean</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg clean&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;dry-run]&nbsp;<wbr>[-x]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>This command can be used to clean up your working directory. By default it<br />
&nbsp;<wbr>&nbsp;<wbr>will follow .gitignore rules.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;dry-run, -n&nbsp;<wbr>&nbsp;<wbr>Perform a dry-run<br />
&nbsp;<wbr>-x&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Do not follow .gitignore rules<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg clog</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg clog&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;raw]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>This will create a file named&nbsp;<wbr>&quot;clog&quot;&nbsp;<wbr>that contains the latest rpm changelog<br />
&nbsp;<wbr>&nbsp;<wbr>entry. The leading&nbsp;<wbr>&quot;-&nbsp;<wbr>&quot;&nbsp;<wbr>text will be stripped.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;raw&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Generate a more&nbsp;<wbr>&quot;raw&quot;&nbsp;<wbr>clog without twiddling the contents<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg clone</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg clone&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;branches]&nbsp;<wbr>[&#8211;branch BRANCH]&nbsp;<wbr>[&#8211;anonymous]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>module&nbsp;<wbr>[clone_target]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>This command will clone the named module from the configured repository base<br />
&nbsp;<wbr>&nbsp;<wbr>URL. By default it will also checkout the master branch for your working copy.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>positional arguments:<br />
&nbsp;<wbr>module&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Name of the module to clone<br />
&nbsp;<wbr>clone_target&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Directory in which to clone the module<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;branches, -B&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Do an old style checkout with subdirs for branches<br />
&nbsp;<wbr>&#8211;branch BRANCH, -b BRANCH<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Check out a specific branch<br />
&nbsp;<wbr>&#8211;anonymous, -a&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Check out a module anonymously<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg co</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg co&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;branches]&nbsp;<wbr>[&#8211;branch BRANCH]&nbsp;<wbr>[&#8211;anonymous]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>module&nbsp;<wbr>[clone_target]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>Alias for clone.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>positional arguments:<br />
&nbsp;<wbr>module&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Name of the module to clone<br />
&nbsp;<wbr>clone_target&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Directory in which to clone the module<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;branches, -B&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Do an old style checkout with subdirs for branches<br />
&nbsp;<wbr>&#8211;branch BRANCH, -b BRANCH<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Check out a specific branch<br />
&nbsp;<wbr>&#8211;anonymous, -a&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Check out a module anonymously<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg commit</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg commit&nbsp;<wbr>[-h]&nbsp;<wbr>[-m MESSAGE]&nbsp;<wbr>[&#8211;with-changelog]&nbsp;<wbr>[-c]&nbsp;<wbr>[&#8211;raw]&nbsp;<wbr>[-t]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-F FILE]&nbsp;<wbr>[-p]&nbsp;<wbr>[-s]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[files&nbsp;<wbr>[files &#8230;]]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>This invokes a git commit. All tracked files with changes will be committed<br />
&nbsp;<wbr>&nbsp;<wbr>unless a specific file list is provided.&nbsp;<wbr>$EDITOR will be used to generate a<br />
&nbsp;<wbr>&nbsp;<wbr>changelog message unless one is given to the command. A push can be done at<br />
&nbsp;<wbr>&nbsp;<wbr>the same time.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>positional arguments:<br />
&nbsp;<wbr>files&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Optional list of specific files to commit<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>-m MESSAGE, &#8211;message MESSAGE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use the given&nbsp;<wbr>&lt;msg&gt;&nbsp;<wbr>as the commit message summary<br />
&nbsp;<wbr>&#8211;with-changelog&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Get the last changelog from SPEC as commit message<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>content. This option must be used with -m together.<br />
&nbsp;<wbr>-c, &#8211;clog&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Generate the commit message from the Changelog section<br />
&nbsp;<wbr>&#8211;raw&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Make the clog raw<br />
&nbsp;<wbr>-t, &#8211;tag&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Create a tag for this commit<br />
&nbsp;<wbr>-F FILE, &#8211;file FILE&nbsp;<wbr>&nbsp;<wbr>Take the commit message from the given file<br />
&nbsp;<wbr>-p, &#8211;push&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Commit and push as one action<br />
&nbsp;<wbr>-s, &#8211;signoff&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Include a signed-off-by<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg compile</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg compile&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;builddir BUILDDIR]&nbsp;<wbr>[&#8211;arch ARCH]&nbsp;<wbr>[&#8211;short-circuit]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;nocheck]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>This command calls rpmbuild to compile the source. By default the prep and<br />
&nbsp;<wbr>&nbsp;<wbr>configure stages will be done as well, unless the short-circuit option is<br />
&nbsp;<wbr>&nbsp;<wbr>used.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;builddir BUILDDIR&nbsp;<wbr>&nbsp;<wbr>Define an alternate builddir<br />
&nbsp;<wbr>&#8211;arch ARCH&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Prep for a specific arch<br />
&nbsp;<wbr>&#8211;short-circuit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>short-circuit compile<br />
&nbsp;<wbr>&#8211;nocheck&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>nocheck compile<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg container-build</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg container-build&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;repo-url&nbsp;<wbr>[URL&nbsp;<wbr>[URL &#8230;]]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;osbs-config PATH]&nbsp;<wbr>[&#8211;instance SECTION]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;scratch]&nbsp;<wbr>[&#8211;target TARGET]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;build-with&nbsp;<wbr>{koji,osbs}]&nbsp;<wbr>[&#8211;nowait]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>build a container.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;repo-url&nbsp;<wbr>[URL&nbsp;<wbr>[URL &#8230;]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>URL of yum repo file<br />
&nbsp;<wbr>&#8211;target TARGET&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Override the default target<br />
&nbsp;<wbr>&#8211;build-with&nbsp;<wbr>{koji,osbs}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Build container with specified builder type. Default<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>is koji<br />
&nbsp;<wbr>&#8211;nowait&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Don&#8217;t wait on build<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>osbs:<br />
&nbsp;<wbr>&#8211;osbs-config PATH&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>path to file with configuration of osbs<br />
&nbsp;<wbr>&#8211;instance SECTION&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>use specific instance specified by section name in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>config<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>koji:<br />
&nbsp;<wbr>&#8211;scratch&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Scratch build<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg container-build-setup</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg container-build-setup&nbsp;<wbr>[-h]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(&#8211;get-autorebuild | &#8211;set-autorebuild&nbsp;<wbr>{true,false})<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>set options for container-build.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;get-autorebuild&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Get autorebuild value<br />
&nbsp;<wbr>&#8211;set-autorebuild&nbsp;<wbr>{true,false}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Turn autorebuilds on/off<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg copr-build</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg copr-build&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;nowait]&nbsp;<wbr>project<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>Build package in Copr.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>Note: you need to have set up correct api key. For more information<br />
&nbsp;<wbr>&nbsp;<wbr>see API KEY section of&nbsp;<wbr><a href="/docs/linux/man/1-copr-cli/">copr-cli</a>(1)&nbsp;<wbr>man page.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>positional arguments:<br />
&nbsp;<wbr>project&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Name of the project in format USER/PROJECT<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;nowait&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Don&#8217;t wait on build<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg diff</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg diff&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;cached]&nbsp;<wbr>[files&nbsp;<wbr>[files &#8230;]]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>Use git diff to show changes that have been made to tracked files. By default<br />
&nbsp;<wbr>&nbsp;<wbr>cached changes&nbsp;<wbr>(changes that have been git added)&nbsp;<wbr>will not be shown.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>positional arguments:<br />
&nbsp;<wbr>files&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Optionally diff specific files<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;cached&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>View staged changes<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg gimmespec</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg gimmespec&nbsp;<wbr>[-h]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>Print the spec file name.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg gitbuildhash</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg gitbuildhash&nbsp;<wbr>[-h]&nbsp;<wbr>build<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>This will show you the commit hash string used to build the provided build<br />
&nbsp;<wbr>&nbsp;<wbr>n-v-r<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>positional arguments:<br />
&nbsp;<wbr>build&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>name-version-release of the build to query.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg giturl</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg giturl&nbsp;<wbr>[-h]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>This will show you which git URL would be used in a build command. It uses the<br />
&nbsp;<wbr>&nbsp;<wbr>git hashsum of the HEAD of the current branch&nbsp;<wbr>(which may not be pushed).<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg help</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg help&nbsp;<wbr>[-h]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>Show usage.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg import</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg import&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;skip-diffs]&nbsp;<wbr>srpm<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>This will extract sources, patches, and the spec file from an srpm and update<br />
&nbsp;<wbr>&nbsp;<wbr>the current module accordingly. It will import to the current branch by<br />
&nbsp;<wbr>&nbsp;<wbr>default.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>positional arguments:<br />
&nbsp;<wbr>srpm&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Source rpm to import<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;skip-diffs&nbsp;<wbr>&nbsp;<wbr>Don&#8217;t show diffs when import srpms<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg install</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg install&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;builddir BUILDDIR]&nbsp;<wbr>[&#8211;arch ARCH]&nbsp;<wbr>[&#8211;short-circuit]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;nocheck]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>This will call rpmbuild to run the install section. All leading sections will<br />
&nbsp;<wbr>&nbsp;<wbr>be processed as well, unless the short-circuit option is used.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;builddir BUILDDIR&nbsp;<wbr>&nbsp;<wbr>Define an alternate builddir<br />
&nbsp;<wbr>&#8211;arch ARCH&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Prep for a specific arch<br />
&nbsp;<wbr>&#8211;short-circuit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>short-circuit install<br />
&nbsp;<wbr>&#8211;nocheck&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>nocheck install<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg lint</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg lint&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;info]&nbsp;<wbr>[&#8211;rpmlintconf RPMLINTCONF]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>Rpmlint can be configured using the &#8211;rpmlintconf/-r option or by setting a<br />
&nbsp;<wbr>&nbsp;<wbr>.rpmlint file in the working directory<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;info, -i&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Display explanations for reported messages<br />
&nbsp;<wbr>&#8211;rpmlintconf RPMLINTCONF, -r RPMLINTCONF<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use a specific configuration file for rpmlint<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg local</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg local&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;builddir BUILDDIR]&nbsp;<wbr>[&#8211;arch ARCH]&nbsp;<wbr>[&#8211;md5]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>Locally test run of rpmbuild producing binary RPMs. The rpmbuild output will<br />
&nbsp;<wbr>&nbsp;<wbr>be logged into a file named .build-%{version}-%{release}.log<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;builddir BUILDDIR&nbsp;<wbr>&nbsp;<wbr>Define an alternate builddir<br />
&nbsp;<wbr>&#8211;arch ARCH&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Prep for a specific arch<br />
&nbsp;<wbr>&#8211;md5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use md5 checksums&nbsp;<wbr>(for older rpm hosts)<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg mock-config</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg mock-config&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;target TARGET]&nbsp;<wbr>[&#8211;arch ARCH]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>This will generate a mock config based on the buildsystem target<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;target TARGET&nbsp;<wbr>&nbsp;<wbr>Override target used for config<br />
&nbsp;<wbr>&#8211;arch ARCH&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Override local arch<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg mockbuild</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg mockbuild&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;root CONFIG]&nbsp;<wbr>[&#8211;md5]&nbsp;<wbr>[&#8211;no-clean]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;no-cleanup-after]&nbsp;<wbr>[&#8211;no-clean-all]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>This will use the mock utility to build the package for the distribution<br />
&nbsp;<wbr>&nbsp;<wbr>detected from branch information. This can be overridden using the global<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;dist option. Your user must be in the local&nbsp;<wbr>&quot;mock&quot;&nbsp;<wbr>group.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;root CONFIG, &#8211;mock-config CONFIG<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Override mock configuration&nbsp;<wbr>(like mock -r)<br />
&nbsp;<wbr>&#8211;md5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use md5 checksums&nbsp;<wbr>(for older rpm hosts)<br />
&nbsp;<wbr>&#8211;no-clean, -n&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Do not clean chroot before building package<br />
&nbsp;<wbr>&#8211;no-cleanup-after&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Do not clean chroot after building&nbsp;<wbr>(if automatic<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cleanup is enabled<br />
&nbsp;<wbr>&#8211;no-clean-all, -N&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Alias for both &#8211;no-clean and &#8211;no-cleanup-after<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>If config file for mock isn&#8217;t found in the&nbsp;<wbr>/etc/mock directory, a temporary<br />
&nbsp;<wbr>&nbsp;<wbr>config directory for mock is created and populated with a config file created<br />
&nbsp;<wbr>&nbsp;<wbr>with mock-config.<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg new</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg new&nbsp;<wbr>[-h]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>This will use git to show a diff of all the changes&nbsp;<wbr>(even uncommitted changes)<br />
&nbsp;<wbr>&nbsp;<wbr>since the last git tag was applied.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg new-sources</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg new-sources&nbsp;<wbr>[-h]&nbsp;<wbr>files&nbsp;<wbr>[files &#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>This will upload new source files to the lookaside cache and remove any<br />
&nbsp;<wbr>&nbsp;<wbr>existing ones. The&nbsp;<wbr>&quot;sources&quot;&nbsp;<wbr>and .gitignore files will be updated with the new<br />
&nbsp;<wbr>&nbsp;<wbr>uploaded file(s).<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>positional arguments:<br />
&nbsp;<wbr>files<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg patch</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg patch&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;rediff]&nbsp;<wbr>suffix<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>Create and add a gendiff patch file.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>positional arguments:<br />
&nbsp;<wbr>suffix&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Look for files with this suffix to diff<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;rediff&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Recreate gendiff file retaining comments Saves old patch file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>with a suffix of&nbsp;<wbr>~<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>Patch file will be named: package-version-suffix.patch and the file will be<br />
&nbsp;<wbr>&nbsp;<wbr>added to the repo index<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg prep</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg prep&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;builddir BUILDDIR]&nbsp;<wbr>[&#8211;arch ARCH]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>Use rpmbuild to&nbsp;<wbr>&quot;prep&quot;&nbsp;<wbr>the sources&nbsp;<wbr>(unpack the source archive(s)&nbsp;<wbr>and apply any<br />
&nbsp;<wbr>&nbsp;<wbr>patches.)<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;builddir BUILDDIR&nbsp;<wbr>&nbsp;<wbr>Define an alternate builddir<br />
&nbsp;<wbr>&#8211;arch ARCH&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Prep for a specific arch<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg pull</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg pull&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;rebase]&nbsp;<wbr>[&#8211;no-rebase]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>This command uses git to fetch remote changes and apply them to the current<br />
&nbsp;<wbr>&nbsp;<wbr>working copy. A rebase option is available which can be used to avoid merges.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;rebase&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Rebase the locally committed changes on top of the remote<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>changes after fetching. This can avoid a merge commit, but does<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rewrite local history.<br />
&nbsp;<wbr>&#8211;no-rebase&nbsp;<wbr>&nbsp;<wbr>Do not rebase, overriding .git settings to the contrary<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>See git pull &#8211;help for more details<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg push</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg push&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;force]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>Push changes to remote repository.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;force, -f&nbsp;<wbr>&nbsp;<wbr>Force push<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg scratch-build</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg scratch-build&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;arches&nbsp;<wbr>[ARCHES&nbsp;<wbr>[ARCHES &#8230;]]]&nbsp;<wbr>[&#8211;md5]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;nowait]&nbsp;<wbr>[&#8211;target TARGET]&nbsp;<wbr>[&#8211;background]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;srpm&nbsp;<wbr>[SRPM]]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>This command will request a scratch build of the package. Without providing an<br />
&nbsp;<wbr>&nbsp;<wbr>srpm, it will attempt to build the latest commit, which must have been pushed.<br />
&nbsp;<wbr>&nbsp;<wbr>By default all appropriate arches will be built.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;arches&nbsp;<wbr>[ARCHES&nbsp;<wbr>[ARCHES &#8230;]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Build for specific arches<br />
&nbsp;<wbr>&#8211;md5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use md5 checksums&nbsp;<wbr>(for older rpm hosts)<br />
&nbsp;<wbr>&#8211;nowait&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Don&#8217;t wait on build<br />
&nbsp;<wbr>&#8211;target TARGET&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Define build target to build into<br />
&nbsp;<wbr>&#8211;background&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Run the build at a low priority<br />
&nbsp;<wbr>&#8211;srpm&nbsp;<wbr>[SRPM]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Build from an srpm. If no srpm is provided with this<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>option an srpm will be generated from the current<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>module content.<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg sources</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg sources&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;outdir OUTDIR]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>Download source files<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;outdir OUTDIR&nbsp;<wbr>&nbsp;<wbr>Directory to download files into&nbsp;<wbr>(defaults to pwd)<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg srpm</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg srpm&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;md5]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>Create a source rpm<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;md5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use md5 checksums&nbsp;<wbr>(for older rpm hosts)<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg switch-branch</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg switch-branch&nbsp;<wbr>[-h]&nbsp;<wbr>[-l]&nbsp;<wbr>[&#8211;fetch]&nbsp;<wbr>[branch]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>This command can switch to a local git branch. If provided with a remote<br />
&nbsp;<wbr>&nbsp;<wbr>branch name that does not have a local match it will create one. It can also<br />
&nbsp;<wbr>&nbsp;<wbr>be used to list the existing local and remote branches.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>positional arguments:<br />
&nbsp;<wbr>branch&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Branch name to switch to<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>-l, &#8211;list&nbsp;<wbr>&nbsp;<wbr>List both remote-tracking branches and local branches<br />
&nbsp;<wbr>&#8211;fetch&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Fetch new data from remote before switch<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg tag</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg tag&nbsp;<wbr>[-h]&nbsp;<wbr>[-f]&nbsp;<wbr>[-m MESSAGE]&nbsp;<wbr>[-c]&nbsp;<wbr>[&#8211;raw]&nbsp;<wbr>[-F FILE]&nbsp;<wbr>[-l]&nbsp;<wbr>[-d]&nbsp;<wbr>[tag]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>This command uses git to create, list, or delete tags.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>positional arguments:<br />
&nbsp;<wbr>tag&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Name of the tag<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>-f, &#8211;force&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Force the creation of the tag<br />
&nbsp;<wbr>-m MESSAGE, &#8211;message MESSAGE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use the given&nbsp;<wbr>&lt;msg&gt;&nbsp;<wbr>as the tag message<br />
&nbsp;<wbr>-c, &#8211;clog&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Generate the tag message from the spec changelog<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>section<br />
&nbsp;<wbr>&#8211;raw&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Make the clog raw<br />
&nbsp;<wbr>-F FILE, &#8211;file FILE&nbsp;<wbr>&nbsp;<wbr>Take the tag message from the given file<br />
&nbsp;<wbr>-l, &#8211;list&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>List all tags with a given pattern, or all if not<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pattern is given<br />
&nbsp;<wbr>-d, &#8211;delete&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Delete a tag<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg unused-patches</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg unused-patches&nbsp;<wbr>[-h]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>Print list of patches not referenced by name in the specfile.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg upload</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg upload&nbsp;<wbr>[-h]&nbsp;<wbr>files&nbsp;<wbr>[files &#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>This command will add a new source archive to the lookaside cache. The sources<br />
&nbsp;<wbr>&nbsp;<wbr>and .gitignore file will be updated with the new file(s).<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>positional arguments:<br />
&nbsp;<wbr>files<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg verify-files</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg verify-files&nbsp;<wbr>[-h]&nbsp;<wbr>[&#8211;builddir BUILDDIR]&nbsp;<wbr>[&#8211;arch ARCH]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>Locally run&nbsp;<wbr>&#8216;rpmbuild -bl&#8217;&nbsp;<wbr>to verify the spec file&#8217;s&nbsp;<wbr>%files sections. This<br />
&nbsp;<wbr>&nbsp;<wbr>requires a successful run of&nbsp;<wbr>&#8216;rpkg install&#8217;&nbsp;<wbr>in advance.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&#8211;builddir BUILDDIR&nbsp;<wbr>&nbsp;<wbr>Define an alternate builddir<br />
&nbsp;<wbr>&#8211;arch ARCH&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Prep for a specific arch<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h3>rpkg verrel</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>usage: rpkg verrel&nbsp;<wbr>[-h]<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>Print the name-version-release.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>optional arguments:<br />
&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>show this help message and exit<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<h2>SEE ALSO</h2>
<p> <code><a rel="nofollow" href="https://fedorahosted.org/rpkg/">https://fedorahosted.org/rpkg/</a></code> </p>
<h2>Index</h2>
