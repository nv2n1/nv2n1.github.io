---
title: "insserv(8)"
name: "insserv"
section: "8"
letter: "i"
url: "/docs/linux/man/8-insserv/"
description: "insserv – boot sequence organizer using LSB init.d script dependency information"
---

<p>insserv &#8211; boot sequence organizer using LSB init.d script dependency information</p>
<h2>Synopsis</h2>
<p><code>insserv</code> [<code>-v</code>] [<code>-c&nbsp;<wbr>&lt;config&gt;</code>] [<code>-p&nbsp;<wbr>&lt;path&gt;</code>] [<code>-d</code>] [<code>-f</code>] [[<i>/</i>]<i>path/to/init.d/</i>]<i>script</i>&nbsp;<wbr>&#8230; <code>insserv</code> [<code>-v</code>] [<code>-c&nbsp;<wbr>&lt;config&gt;</code>] [<code>-p&nbsp;<wbr>&lt;path&gt;</code>] [[<i>/</i>]<i>path/to/init.d/</i>]<i>script</i>[<i>,start=&lt;lvl1,lvl2,&#8230;&gt;,stop=&lt;lvl1,lvl2,&#8230;&gt;</i>] <code>insserv</code> [<code>-v</code>] [<code>-c&nbsp;<wbr>&lt;config&gt;</code>] [<code>-p&nbsp;<wbr>&lt;path&gt;</code>] <code>-r</code> [<code>-d</code>] [<code>-f</code>] [[<i>/</i>]<i>path/to/init.d/</i>]<i>script</i>&nbsp;<wbr>&#8230; <code>insserv</code> <code>-h</code> </p>
<h2>Description</h2>
<p><code>insserv</code> is a low level tool used by <code>update-rc.d</code> which enables an installed system init script (`boot script&#8217;) by reading the comment header of the script, e.g.: </p>
<pre> ### BEGIN INIT INFO
 # Provides: boot_facility_1 [ boot_facility_2 ...]
 # Required-Start: boot_facility_1 [ boot_facility_2 ...]
 # Required-Stop: boot_facility_1 [ boot_facility_2 ...]
 # Should-Start: boot_facility_1 [ boot_facility_2 ...]
 # Should-Stop: boot_facility_1 [ boot_facility_2 ...]
 # X-Start-Before: boot_facility_1 [ boot_facility_2 ...]
 # X-Stop-After: boot_facility_1 [ boot_facility_2 ...]
 # Default-Start: run_level_1 [ run_level_2 ...]
 # Default-Stop: run_level_1 [ run_level_2 ...]
 # X-Interactive: true
 # Short-Description: single_line_description
 # Description: multiline_description
 ### END INIT INFO</pre>
<p>and calculating the dependencies between all scripts. It is not recommended to execute insserv directly unless you know exactly what you&#8217;re doing, doing so may render your boot system inoperable. <code>update-rc.d</code> is the recommended interface for managing init scripts. Please be aware that the line </p>
<pre> # Required-Stop: boot_facility_1 [ boot_facility_2 ...]</pre>
<p>declares facilities which must be available during shutdown of the service declared in the <code>Provides</code> tag. Same holds true for </p>
<pre> # Should-Stop: boot_facility_1 [ boot_facility_2 ...]</pre>
<p>which declares facilities which should be available during shutdown of the service declared in the <code>Provides</code> tag. In both cases the script system should avoid stopping services which are declared by these two Stop tags until the script including these tags is stopped. </p>
<p> The optional X-Interactive keyword implies that the script using this keyword should be started alone in a concurrent boot configuration because it interact with the user at the console. Only the value `true&#8217; is recognised. All other are ignored. </p>
<p> The optional <code>X-Start-Before</code> keyword implies that the script using this keyword should be started <code>before</code> the specified service names. Whereas the optional <code>X-Stop-After</code> keyword implies that the script using this keyword should be stopped <code>after</code> the specified service names. Both implies that those services now depend on the specifying script. With known dependencies and runlevel(s) <code>insserv</code> sets and reorders the corresponding symbolic links of the concerned runlevels directories. </p>
<p> <code>insserv</code> scans for <code>System Facilities</code> in the configuration file <i>/etc/insserv.conf</i> and each file in the directory <i>/etc/insserv.conf.d/</i>. Each line which begins with <code>$</code> and a following name defines a system facility accordingly to the Linux Standard Base Specification (LSB), All names followed by such a system facility will declare the required dependencies of the facility. Here is an example for <i>/etc/insserv.conf</i>: </p>
<pre> # All local filesystems are mounted
 # (done during boot phase)
 $local_fs boot
 # Low level networking
 $network network route
 # Named is operational
 $named named
 # All remote filesystems are mounted
 # (in some cases /usr may be remote).
 $remote_fs $local_fs nfs
 # System logger is operational
 $syslog syslog
 # All network daemons are running (This was removed in LSB 1.2)
 $netdaemons portmap inetd
 # Services which need to be interactive
 &lt;interactive&gt; boot.crypto</pre>
<p>Names starting with a `+&#8217; sign are marked as optional. If the service with the name after the plus sign is available it will be used, if not available it is ignored silently. Words beginning with <code>&lt;</code> and ending with <code>&gt;</code> are keywords. Currently <code>&lt;interactive&gt;</code> is the only know keyword for marking a service as an interactive one, e.g. a service which requires a passphrase or password input during boot or runlevel change. The special facility <code>$null</code> is used to enforce an empty dependency in case of <code>Should-Stop</code> and <code>Required-Stop</code>. </p>
<p> In addition to the defined <code>System Facilities</code> in the configuration file <i>/etc/insserv.conf</i>, <code>insserv</code> also knows the special facility <code>$all</code>. This facility indicates that a service should be inserted at the end of all services at starting and at the very beginning at stopping. Clearly all services using this facility will be grouped into one starting or stopping order.</p>
<h2>Options</h2>
<p>Currently there exists nine options for <code>insserv</code>.</p>
<dl>
<dt><code>-v</code>,&nbsp;<wbr><code>&#8211;verbose</code></p>
<dd>Write out what is currently going on.</p>
<dt><code>-c&nbsp;<wbr>&lt;config&gt;</code>,&nbsp;<wbr><code>&#8211;config&nbsp;<wbr>&lt;config&gt;</code></p>
<dd>Specify path to the insserv.conf file and the insserv.conf.d directory. Useful for testing.</p>
<dt><code>-o&nbsp;<wbr>&lt;path&gt;</code>,&nbsp;<wbr><code>&#8211;override&nbsp;<wbr>&lt;path&gt;</code></p>
<dd>LSB comment headers found in this path will override existing LSB comment headers of scripts in the init.d directory (default path is <i>/etc/insserv/overrides/</i>).</p>
<dt><code>-p&nbsp;<wbr>&lt;path&gt;</code>,&nbsp;<wbr><code>&#8211;path&nbsp;<wbr>&lt;path&gt;</code></p>
<dd>Specify path to init.d directory. Useful for testing.</p>
<dt><code>-n</code>,&nbsp;<wbr><code>&#8211;dryrun</code></p>
<dd>Do not update symlinks.</p>
<dt><code>-r</code>,&nbsp;<wbr><code>&#8211;remove</code></p>
<dd>Remove the listed scripts from all runlevels.</p>
<dt><code>-d</code>,&nbsp;<wbr><code>&#8211;default</code></p>
<dd>Use default runlevels as defined in the scripts. This may restore an edited runlevel link scheme.</p>
<dt><code>-f</code>,&nbsp;<wbr><code>&#8211;force</code></p>
<dd>Ignore if a required service is missed. Beside this if start and or stop levels are specified on the command line the default levels of the script will be ignored.</p>
<dt><code>-u&nbsp;<wbr>&lt;path&gt;</code>,&nbsp;<wbr><code>&#8211;upstart-job&nbsp;<wbr>&lt;path&gt;</code></p>
<dd>Path to replace existing upstart job path. (default path is <i>/lib/init/upstart-job</i>).</p>
<dt><code>-s</code>,&nbsp;<wbr><code>&#8211;showall</code></p>
<dd>Output runlevel and sequence information. Do not update symlinks.</p>
<dt><code>-h</code>,&nbsp;<wbr><code>&#8211;help</code></p>
<dd>Print out short usage message.</dl>
<p> But you may use the argument syntax described in the following section.</p>
<h2>Arguments</h2>
<dl>
<dt>[[<i>/</i>]<i>path/to/init.d/</i>]</p>
<dd>Relative or absolute path to the init scripts base directory. This defaults to <i>/etc/init.d/</i> in compliance with the LSB specification. In this case <code>insserv</code> does not add or remove a script to the runlevels declared in the script headers, but may re-order the runlevels if the order of the currently enabled scripts has changed (see option <code>-d</code>). Note that if a relative path is used <code>insserv</code> has to be called from the root directory.</p>
<dt>[[<i>/</i>]<i>path/to/init.d/</i>]<i>script &#8230;</i></p>
<dd>List of scripts which have to be added to the runlevels. If a path is used it should point to the absolute or relative location of the boot scripts. <code>insserv</code> checks for the existence of these scripts. For the runlevels the information found in the script is used.</p>
<dt>[[<i>/</i>]<i>path/to/init.d/</i>]<i>script</i>[<i>,start=&lt;lvl1,lvl2,&#8230;&gt;</i>]</p>
<dd>List of scripts which have to be added to the specified runlevels to be started with. You may use this extension to override the default values for start and stop runlevels of the script. Note that <code>lvl1</code>,&nbsp;<wbr><code>lvl2</code>, &#8230; are the known runlevels explained above. The extension <i>,stop=&lt;lvl1,lvl2,&#8230;&gt;</i> is also possible.</p>
<dt><code>-r</code>&nbsp;<wbr>[[<i>/</i>]<i>path/to/init.d/</i>]<i>script &#8230;</i></p>
<dd>List of scripts which should be removed from the runlevels. If a path is used it should point to the absolute or relative location of the boot scripts. <code>insserv</code> checks for the existence of these scripts.</dl>
<h2>Overrides</h2>
<p>Beside using the extensions <i>,start=&lt;lvl1,lvl2,&#8230;&gt;</i> and <i>,stop=&lt;lvl1,lvl2,&#8230;&gt;</i> it is possible to use override files replace a LSB comment header or simple provide a missing LSB comment header. This can be done by placing a file with the new LSB comment header using the same name as the boot or init script in the directory <i>/etc/insserv/overrides/</i>. For third party boot scripts without LSB header it is possible to add a file with the same name in the directory <i>/usr/share/insserv/overrides/</i> to make them completely LSB compliant.</p>
<h2>Upstart Job Compatibility</h2>
<p>To allow upstart jobs to work as init.d scripts, insserv will recognize a symlink from path/to/init.d/script to /lib/init/upstart-job as upstart jobs, and instead of reading the header from the file will run the script with the argument lsb-header to get the script header.</p>
<h2>Exit Codes</h2>
<p>The exit codes have the following conditions:</p>
<dl>
<dd>
<dl>
<dt>0</p>
<dd>Service was successfully installed or removed</p>
<dt>1</p>
<dd>Service was not installed or removed</dl>
</dl>
<dl>
<dd></dl>
<h2>Note</h2>
<p>Please be aware that the following patterns of boot script file names will be not accepted by <code>insserv:</code> </p>
<pre> *.dpkg*
 *.rpm*
 *.ba*
 *.old
 *.new
 *.org
 *.orig
 *.save
 *.swp
 *.core
 *~</pre>
<p>with the wildcard character <code>*</code>. Beside this all boot script file names beginning with one of the following characters </p>
<pre> $.#%_+-\*[]^:()~</pre>
<p>will be ignored.</p>
<h2>Bugs</h2>
<p>Boot scripts sometimes lack a LSB comment header. Contact a package maintainer or developer of the software which provides the script to have a LSB comment header added to it.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/insserv.conf</i></p>
<dd>configuration file for <code>insserv</code> which defines the LSB System Facilities.</p>
<dt><i>/etc/insserv.conf.d/</i></p>
<dd>directory for further configuration files for declaring LSB System Facilities.</p>
<dt><i>/etc/insserv/overrides/</i></p>
<dd>path to replace existing LSB comment headers with the comment headers found in this path.</p>
<dt><i>/etc/init.d/</i></p>
<dd>path to the init script base directory as required by the Linux Standard Base Specification (LSB).</dl>
<p> <i>/etc/init.d/.depend.boot</i>,<br />
 <i>/etc/init.d/.depend.start</i>,<br />
 <i>/etc/init.d/.depend.stop</i> The <code><a href="/docs/linux/man/1-make/">make</a></code>(1) like dependency files produced by <code>insserv</code> for <i>booting</i>, <i>starting</i>, and <i>stopping</i> with the help of <code><a href="/docs/linux/man/8-startpar/">startpar</a></code>(8).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-init/">init</a></code>(8), <code><a href="/docs/linux/man/8-startpar/">startpar</a></code>(8), <code><a href="/docs/linux/man/8-update-rc-d/">update-rc.d</a></code>(8).</p>
<h2>Copyright</h2>
<p>2000-2009 Werner Fink,<br />
 2009 SuSE Linux Products GmbH Nuernberg, Germany.<br />
 2000-2003 SuSE GmbH Nuernberg, Germany,<br />
 2007-2009 SuSE Linux Products GmbH Nuernberg, Germany.</p>
<h2>Author</h2>
<p>Werner Fink &lt;feedback [at] suse.de&gt;</p>
<h2>Contributors</h2>
<p>Petter Reinholdtsen<br />
 Kel Modderman</p>
