---
title: "dh(1)"
name: "dh"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh/"
description: "dh – debhelper command sequencer"
---

<h2 class="name">NAME</h2>
<p> dh &#8211; debhelper command sequencer </p>
<h2>SYNOPSIS</h2>
<p> <code>dh</code> <i>sequence</i> [<code>&#8211;with</code> <i>addon</i>[<code>,</code><i>addon</i> &#8230;]] [<code>&#8211;list</code>] [<i>debhelper options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh</code> runs a sequence of debhelper commands. The supported <i>sequence</i>s correspond to the targets of a <i>debian/rules</i> file: <code>build-arch</code>, <code>build-indep</code>, <code>build</code>, <code>clean</code>, <code>install-indep</code>, <code>install-arch</code>, <code>install</code>, <code>binary-arch</code>, <code>binary-indep</code>, and <code>binary</code>.</p>
<h2>OVERRIDE TARGETS</h2>
<p> A <i>debian/rules</i> file using <code>dh</code> can override the command that is run at any step in a sequence, by defining an override target. </p>
<p> To override <i>dh_command</i>, add a target named <code>override_</code><i>dh_command</i> to the rules file. When it would normally run <i>dh_command</i>, <code>dh</code> will instead call that target. The override target can then run the command with additional options, or run entirely different commands instead. See examples below. </p>
<p> Override targets can also be defined to run only when building architecture dependent or architecture independent packages. Use targets with names like <code>override_</code><i>dh_command</i><code>-arch</code> and <code>override_</code><i>dh_command</i><code>-indep</code>. (Note that to use this feature, you should Build-Depend on debhelper 8.9.7 or above.)</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;with</code> <i>addon</i>[<code>,</code><i>addon</i> &#8230;]</p>
<dd> Add the debhelper commands specified by the given addon to appropriate places in the sequence of commands that is run. This option can be repeated more than once, or multiple addons can be listed, separated by commas. This is used when there is a third-party package that provides debhelper commands. See the <i></i><font SIZE="-1"><i>PROGRAMMING</i></font><i></i> file for documentation about the sequence addon interface.</p>
<dt><code>&#8211;without</code> <i>addon</i></p>
<dd> The inverse of <code>&#8211;with</code>, disables using the given addon. This option can be repeated more than once, or multiple addons to disable can be listed, separated by commas.</p>
<dt><code>&#8211;list</code>, <code>-l</code></p>
<dd> List all available addons. </p>
<p> When called only with this option, <code>dh</code> can be called from any directory (i.e. it does not need access to files from a source package).</p>
<dt><code>&#8211;no-act</code></p>
<dd> Prints commands that would run for a given sequence, but does not run them. </p>
<p> Note that dh normally skips running commands that it knows will do nothing. With &#8211;no-act, the full list of commands in a sequence is printed.</dl>
<p> Other options passed to <code>dh</code> are passed on to each command it runs. This can be used to set an option like <code>-v</code> or <code>-X</code> or <code>-N</code>, as well as for more specialised options.</p>
<h2>EXAMPLES</h2>
<p> To see what commands are included in a sequence, without actually doing anything: </p>
<pre>
        dh binary-arch --no-act
</pre>
<p> This is a very simple rules file, for packages where the default sequences of commands work with no additional options. </p>
<pre>
        #!/usr/bin/make -f
        %:
                dh $@
</pre>
<p> Often you&#8217;ll want to pass an option to a specific debhelper command. The easy way to do with is by adding an override target for that command. </p>
<pre>
        #!/usr/bin/make -f
        %:
                dh $@
        
        override_dh_strip:
                dh_strip -Xfoo
        
        override_dh_auto_configure:
                dh_auto_configure -- --with-foo --disable-bar
</pre>
<p> Sometimes the automated <i><a href="/docs/linux/man/1-dh_auto_configure/">dh_auto_configure</a></i>(1) and <i><a href="/docs/linux/man/1-dh_auto_build/">dh_auto_build</a></i>(1) can&#8217;t guess what to do for a strange package. Here&#8217;s how to avoid running either and instead run your own commands. </p>
<pre>
        #!/usr/bin/make -f
        %:
                dh $@
        override_dh_auto_configure:
                ./mondoconfig
        override_dh_auto_build:
                make universe-explode-in-delight
</pre>
<p> Another common case is wanting to do something manually before or after a particular debhelper command is run. </p>
<pre>
        #!/usr/bin/make -f
        %:
                dh $@
        override_dh_fixperms:
                dh_fixperms
                chmod 4755 debian/foo/usr/bin/foo
</pre>
<p> Python tools are not run by dh by default, due to the continual change in that area. Here is how to use <code>dh_python2</code>. </p>
<pre>
        #!/usr/bin/make -f
        %:
                dh $@ --with python2
</pre>
<p> Here is how to force use of Perl&#8217;s <code>Module::Build</code> build system, which can be necessary if debhelper wrongly detects that the package uses MakeMaker. </p>
<pre>
        #!/usr/bin/make -f
        %:
                dh $@ --buildsystem=perl_build
</pre>
<p> Here is an example of overriding where the <code>dh_auto_</code><i>*</i> commands find the package&#8217;s source, for a package where the source is located in a subdirectory. </p>
<pre>
        #!/usr/bin/make -f
        %:
                dh $@ --sourcedirectory=src
</pre>
<p> And here is an example of how to tell the <code>dh_auto_</code><i>*</i> commands to build in a subdirectory, which will be removed on <code>clean</code>. </p>
<pre>
        #!/usr/bin/make -f
        %:
                dh $@ --builddirectory=build
</pre>
<p> If your package can be built in parallel, please either use compat 10 or pass <code>&#8211;parallel</code> to dh. Then <code>dpkg-buildpackage -j</code> will work. </p>
<pre>
        #!/usr/bin/make -f
        %:
                dh $@ --parallel
</pre>
<p> If your package cannot be built reliably while using multiple threads, please pass <code>&#8211;no-parallel</code> to dh (or the relevant <code>dh_auto_</code><i>*</i> command): </p>
<pre>
        #!/usr/bin/make -f
        %:
                dh $@ --no-parallel
</pre>
<p> Here is a way to prevent <code>dh</code> from running several commands that you don&#8217;t want it to run, by defining empty override targets for each command. </p>
<pre>
        #!/usr/bin/make -f
        %:
                dh $@
        
        # Commands not to run:
        override_dh_auto_test override_dh_compress override_dh_fixperms:
</pre>
<p> A long build process for a separate documentation package can be separated out using architecture independent overrides. These will be skipped when running build-arch and binary-arch sequences. </p>
<pre>
        #!/usr/bin/make -f
        %:
                dh $@
        
        override_dh_auto_build-indep:
                $(MAKE) -C docs
        # No tests needed for docs
        override_dh_auto_test-indep:
        override_dh_auto_install-indep:
                $(MAKE) -C docs install
</pre>
<p> Adding to the example above, suppose you need to chmod a file, but only when building the architecture dependent package, as it&#8217;s not present when building only documentation. </p>
<pre>
        override_dh_fixperms-arch:
                dh_fixperms
                chmod 4755 debian/foo/usr/bin/foo
</pre>
<h2>INTERNALS</h2>
<p> If you&#8217;re curious about <code>dh</code>&#8216;s internals, here&#8217;s how it works under the hood. </p>
<p> In compat 10 (or later), <code>dh</code> creates a stamp file <i>debian/debhelper-build-stamp</i> after the build step(s) are complete to avoid re-running them. It is possible to avoid the stamp file by passing <code>&#8211;without=build-stamp</code> to <code>dh</code>. This makes &#8220;no clean&#8221; builds behave more like what some people expect at the expense of possibly running the build and test twice (the second time as root or under <i><a href="/docs/linux/man/1-fakeroot/">fakeroot</a></i>(1)). </p>
<p> Inside an override target, <code>dh_*</code> commands will create a log file <i>debian/package.debhelper.log</i> to keep track of which packages the command(s) have been run for. These log files are then removed once the override target is complete. </p>
<p> In compat 9 or earlier, each debhelper command will record when it&#8217;s successfully run in <i>debian/package.debhelper.log</i>. (Which <code>dh_clean</code> deletes.) So <code>dh</code> can tell which commands have already been run, for which packages, and skip running those commands again. </p>
<p> Each time <code>dh</code> is run (in compat 9 or earlier), it examines the log, and finds the last logged command that is in the specified sequence. It then continues with the next command in the sequence. The <code>&#8211;until</code>, <code>&#8211;before</code>, <code>&#8211;after</code>, and <code>&#8211;remaining</code> options can override this behavior (though they were removed in compat 10). </p>
<p> A sequence can also run dependent targets in debian/rules. For example, the &#8220;binary&#8221; sequence runs the &#8220;install&#8221; target. </p>
<p> <code>dh</code> uses the <font SIZE="-1"><code>DH_INTERNAL_OPTIONS</code></font> environment variable to pass information through to debhelper commands that are run inside override targets. The contents (and indeed, existence) of this environment variable, as the name might suggest, is subject to change at any time. </p>
<p> Commands in the <code>build-indep</code>, <code>install-indep</code> and <code>binary-indep</code> sequences are passed the <code>-i</code> option to ensure they only work on architecture independent packages, and commands in the <code>build-arch</code>, <code>install-arch</code> and <code>binary-arch</code> sequences are passed the <code>-a</code> option to ensure they only work on architecture dependent packages.</p>
<h2>DEPRECATED OPTIONS</h2>
<p> The following options are deprecated. It&#8217;s much better to use override targets instead. They are <code>not</code> available in compat 10.</p>
<dl>
<dt><code>&#8211;until</code> <i>cmd</i></p>
<dd> Run commands in the sequence until and including <i>cmd</i>, then stop.</p>
<dt><code>&#8211;before</code> <i>cmd</i></p>
<dd> Run commands in the sequence before <i>cmd</i>, then stop.</p>
<dt><code>&#8211;after</code> <i>cmd</i></p>
<dd> Run commands in the sequence that come after <i>cmd</i>.</p>
<dt><code>&#8211;remaining</code></p>
<dd> Run all commands in the sequence that have yet to be run.</dl>
<p> In the above options, <i>cmd</i> can be a full name of a debhelper command, or a substring. It&#8217;ll first search for a command in the sequence exactly matching the name, to avoid any ambiguity. If there are multiple substring matches, the last one in the sequence will be used.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
