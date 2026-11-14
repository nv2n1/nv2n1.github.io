---
title: "systemd-generator(7)"
name: "systemd-generator"
section: "7"
letter: "s"
url: "/docs/linux/man/7-systemd-generator/"
description: "systemd.generator – systemd unit generators"
---

<p>systemd.generator &#8211; systemd unit generators</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/path/to/generator</code> <i>normal-dir</i> <i>early-dir</i> <i>late-dir</i></dl>
<pre>/run/systemd/system-generators/*
/etc/systemd/system-generators/*
/usr/local/lib/systemd/system-generators/*
/lib/systemd/system-generators/*</pre>
<pre>/run/systemd/user-generators/*
/etc/systemd/user-generators/*
/usr/local/lib/systemd/user-generators/*
/usr/lib/systemd/user-generators/*</pre>
<h2>Description</h2>
<dd>Generators are small executables placed in /lib/systemd/system-generators/ and other directories listed above. <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) will execute these binaries very early at bootup and at configuration reload time &#8212; before unit files are loaded. Their main purpose is to convert configuration that is not native to the service manager into dynamically generated unit files, symlinks or unit file drop-ins, so that they can extend the unit file hierarchy the service manager subsequently loads and operates on. </p>
<p> Each generator is called with three directory paths that are to be used for generator output. In these three directories, generators may dynamically generate unit files (regular ones, instances, as well as templates), unit file .d/ drop-ins, and create symbolic links to unit files to add additional dependencies, create aliases, or instantiate existing templates. Those directories are included in the unit load path of <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), allowing generated configuration to extend or override existing definitions. </p>
<p> Directory paths for generator output differ by priority: &#8230;/generator.early has priority higher than the admin configuration in /etc/, while &#8230;/generator has lower priority than /etc/ but higher than vendor configuration in /usr/, and &#8230;/generator.late has priority lower than all other configuration. See the next section and the discussion of unit load paths and unit overriding in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5). </p>
<p> Generators are loaded from a set of paths determined during compilation, as listed above. System and user generators are loaded from directories with names ending in system-generators/ and user-generators/, respectively. Generators found in directories listed earlier override the ones with the same name in directories lower in the list. A symlink to /dev/null or an empty file can be used to mask a generator, thereby preventing it from running. Please note that the order of the two directories with the highest priority is reversed with respect to the unit load path, and generators in /run/ overwrite those in /etc/. </p>
<p> After installing new generators or updating the configuration, <code>systemctl daemon-reload</code> may be executed. This will delete the previous configuration created by generators, re-run all generators, and cause <code>systemd</code> to reload units from disk. See <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) for more information.</p>
<h2>Output Directories</h2>
<p>Generators are invoked with three arguments: paths to directories where generators can place their generated unit files or symlinks. By default those paths are runtime directories that are included in the search path of <code>systemd</code>, but a generator may be called with different paths for debugging purposes. </p>
<dl>
<dd>1. <i>normal-dir</i> </p>
<p> In normal use this is /run/systemd/generator in case of the system generators and $XDG_RUNTIME_DIR/generator in case of the user generators. Unit files placed in this directory take precedence over vendor unit configuration but not over native user/administrator unit configuration.</dl>
<dl>
<dd>2. <i>early-dir</i> </p>
<p> In normal use this is /run/systemd/generator.early in case of the system generators and $XDG_RUNTIME_DIR/generator.early in case of the user generators. Unit files placed in this directory override unit files in /usr/, /run/ and /etc/. This means that unit files placed in this directory take precedence over all normal configuration, both vendor and user/administrator.</dl>
<dl>
<dd>3. <i>late-dir</i> </p>
<p> In normal use this is /run/systemd/generator.late in case of the system generators and $XDG_RUNTIME_DIR/generator.late in case of the user generators. This directory may be used to extend the unit file tree without overriding any other unit files. Any native configuration files supplied by the vendor or user/administrator take precedence.</dl>
<h2>Notes About Writing Generators</h2>
<dl>
<dd>&bull; All generators are executed in parallel. That means all executables are started at the very same time and need to be able to cope with this parallelism.</dl>
<dl>
<dd>&bull; Generators are run very early at boot and cannot rely on any external services. They may not talk to any other process. That includes simple things such as logging to <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3), or <code>systemd</code> itself (this means: no <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1))! Non-essential file systems like /var/ and /home/ are mounted after generators have run. Generators can however rely on the most basic kernel functionality to be available, as well as mounted /sys/, /proc/, /dev/, /usr/ and /run/ file systems.</dl>
<dl>
<dd>&bull; Units written by generators are removed when the configuration is reloaded. That means the lifetime of the generated units is closely bound to the reload cycles of <code>systemd</code> itself.</dl>
<dl>
<dd>&bull; Generators should only be used to generate unit files, .d/*.conf drop-ins for them and symlinks to them, not any other kind of non-unit related configuration. Due to the lifecycle logic mentioned above, generators are not a good fit to generate dynamic configuration for other services. If you need to generate dynamic configuration for other services, do so in normal services you order before the service in question. </p>
<p> Note that using the <i>StandardInputData=</i>/<i>StandardInputText=</i> settings of service unit files (see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5)), it is possible to make arbitrary input data (including daemon-specific configuration) part of the unit definitions, which often might be sufficient to embed data or configuration for other programs into unit files in a native fashion.</dl>
<dl>
<dd>&bull; Since <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) is not available (see above), log messages have to be written to /dev/kmsg instead.</dl>
<dl>
<dd>&bull; The generator should always include its own name in a comment at the top of the generated file, so that the user can easily figure out which component created or amended a particular unit. </p>
<p> The <i>SourcePath=</i> directive should be used in generated files to specify the source configuration file they are generated from. This makes things more easily understood by the user and also has the benefit that systemd can warn the user about configuration files that changed on disk but have not been read yet by systemd. The <i>SourcePath=</i> value does not have to be a file in a physical filesystem. For example, in the common case of the generator looking at the kernel command line, <code>SourcePath=/proc/cmdline</code> should be used.</dl>
<dl>
<dd>&bull; Generators may write out dynamic unit files or just hook unit files into other units with the usual .wants/ or .requires/ symlinks. Often, it is nicer to simply instantiate a template unit file from /usr/ with a generator instead of writing out entirely dynamic unit files. Of course, this works only if a single parameter is to be used.</dl>
<dl>
<dd>&bull; If you are careful, you can implement generators in shell scripts. We do recommend C code however, since generators are executed synchronously and hence delay the entire boot if they are slow.</dl>
<dl>
<dd>&bull; Regarding overriding semantics: there are two rules we try to follow when thinking about the overriding semantics: </p>
<dl>
<dd>1. User configuration should override vendor configuration. This (mostly) means that stuff from /etc/ should override stuff from /usr/.</dl>
<dl>
<dd>2. Native configuration should override non-native configuration. This (mostly) means that stuff you generate should never override native unit files for the same purpose.</dl>
<p> Of these two rules the first rule is probably the more important one and breaks the second one sometimes. Hence, when deciding whether to use argv[1], argv[2], or argv[3], your default choice should probably be argv[1].</dl>
<dl>
<dd>&bull; Instead of heading off now and writing all kind of generators for legacy configuration file formats, please think twice! It is often a better idea to just deprecate old stuff instead of keeping it artificially alive.</dl>
<h2>Examples</h2>
<p><code>Example 1. systemd-fstab-generator</code> </p>
<p> <code><a href="/docs/linux/man/8-systemd-fstab-generator/">systemd-fstab-generator</a></code>(8) converts /etc/fstab into native mount units. It uses argv[1] as location to place the generated unit files in order to allow the user to override /etc/fstab with their own native unit files, but also to ensure that /etc/fstab overrides any vendor default from /usr/. </p>
<p> After editing /etc/fstab, the user should invoke <code>systemctl daemon-reload</code>. This will re-run all generators and cause <code>systemd</code> to reload units from disk. To actually mount new directories added to fstab, <code>systemctl start </code><i>/path/to/mountpoint</i> or <code>systemctl start local-fs.target</code> may be used. </p>
<p> <code>Example 2. systemd-system-update-generator</code> </p>
<p> <code><a href="/docs/linux/man/8-systemd-system-update-generator/">systemd-system-update-generator</a></code>(8) temporarily redirects default.target to system-update.target, if a system update is scheduled. Since this needs to override the default user configuration for default.target, it uses argv[2]. For details about this logic, see <code><a href="/docs/linux/man/7-systemd-offline-updates/">systemd.offline-updates</a></code>(7). </p>
<p> <code>Example 3. Debugging a generator</code> </p>
<dl>
<dd>
<pre>dir=$(mktemp -d)
SYSTEMD_LOG_LEVEL=debug /lib/systemd/system-generators/systemd-fstab-generator \
 &quot;$dir&quot; &quot;$dir&quot; &quot;$dir&quot;
find $dir</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-cryptsetup-generator/">systemd-cryptsetup-generator</a></code>(8), <code><a href="/docs/linux/man/8-systemd-debug-generator/">systemd-debug-generator</a></code>(8), <code><a href="/docs/linux/man/8-systemd-fstab-generator/">systemd-fstab-generator</a></code>(8), <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), <code><a href="/docs/linux/man/8-systemd-getty-generator/">systemd-getty-generator</a></code>(8), <code><a href="/docs/linux/man/8-systemd-gpt-auto-generator/">systemd-gpt-auto-generator</a></code>(8), <code><a href="/docs/linux/man/8-systemd-hibernate-resume-generator/">systemd-hibernate-resume-generator</a></code>(8), <code><a href="/docs/linux/man/8-systemd-rc-local-generator/">systemd-rc-local-generator</a></code>(8), <code><a href="/docs/linux/man/8-systemd-system-update-generator/">systemd-system-update-generator</a></code>(8), <code><a href="/docs/linux/man/8-systemd-sysv-generator/">systemd-sysv-generator</a></code>(8), <code><a href="/docs/linux/man/8-systemd-xdg-autostart-generator/">systemd-xdg-autostart-generator</a></code>(8), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/7-systemd-environment-generator/">systemd.environment-generator</a></code>(7) </p>
