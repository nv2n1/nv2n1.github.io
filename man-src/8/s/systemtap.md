---
title: "systemtap(8)"
name: "systemtap"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemtap/"
description: "systemtap – SystemTap initscript service"
---

<p>systemtap &#8211; SystemTap initscript service </p>
<h2>Synopsis</h2>
<p><code>service systemtap</code> <i>COMMAND</i> [<i>OPTIONS</i>] [<i>SCRIPT</i>&#8230;] </p>
<h2>Description</h2>
<p>The SystemTap initscript aims to provide a way to run scripts as a service and easily control them individually. Scripts can be configured to start upon manual request, or during system startup. On dracut-based systems, it is also possible to integrate scripts in the initramfs and have them start during early-boot. There are various parameters and options available to modify global behaviour, as well as script behaviour. Dependencies between scripts can be established so that starting one starts others. The configuration file of the initscript is located at <code>/etc/systemtap/config</code>. Acceptable parameters are detailed in the GLOBAL PARAMETERS section. Scripts must be placed in the <code>/etc/systemtap/script.d</code> directory and must have a <code>.stp</code> extension. When referring to them on the command-line however, there in no need to include the <code>.stp</code> extension. Script names can only contain alphanumeric characters (and &#8216;_&#8217;) and must not start with a number. The scripts directory may be changed by setting the SCRIPT_PATH parameter in the configuration file. </p>
<h2>Commands</h2>
<p>One of the commands below must be specified: </p>
<dl>
<dt><code>start</code></p>
<dd>Start <i>SCRIPT</i>s. If no scripts are specified, start the scripts specified by the DEFAULT_START configuration. If DEFAULT_START is not set, start all scripts in the script directory. For scripts already started, the command is ignored. The command will fail if the scripts fail to start (see also the PASSALL configuration). </p>
<p> If the AUTOCOMPILE configuration is on, the command will try to compile or update the specified scripts when one of the below conditions is true:</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>The compiled cache file does not exist.</p>
<dt>&#8211;</p>
<dd>The mtime (modified timestamp) of the original script file is newer than the time of the compiled script cache.</p>
<dt>&#8211;</p>
<dd>The specified stap options used to compile the script has been changed (see also the SCRIPT PARAMETERS section).</p>
<dt>&#8211;</p>
<dd>The result of `uname -a` has been changed.</dl>
</dl>
<dt><code>stop</code></p>
<dd>Stop <i>SCRIPT</i>s. If no scripts are specified, stop all running scripts. For scripts already stopped, the command is ignored. The command will fail if the scripts fail to stop (see also the PASSALL configuration). </p>
<dt><code>restart</code></p>
<dd>Stop and start <i>SCRIPT</i>s. </p>
<dt><code>status</code></p>
<dd>Show the state of <i>SCRIPT</i>s and their dependencies. </p>
<dt><code>compile</code></p>
<dd>Compile <i>SCRIPT</i>s but do not start them. If the scripts have already been compiled, prompt for confirmation before overwriting cache. Compile for the current kernel, or the kernel release specified by the <code>-r</code> option. </p>
<dt><code>onboot</code></p>
<dd>Make <i>SCRIPT</i>s part of the initramfs so that they are started earlier during the boot process. This command is only available on dracut-based systems. If no scripts are specified, create a normal initramfs devoid of any SystemTap files. </p>
<p> The initramfs is created for the current kernel, or the kernel release specified by the <code>-r</code> option. The path of the created initramfs defaults to <code>/boot/initramfs-KVER.img</code>, where KVER is the output of `uname -r`. The bootloader is also updated (using <i><a href="/docs/linux/man/8-new-kernel-pkg/">new-kernel-pkg</a></i>(8)) to make the kernel entry use the new initramfs file. Use the <code>-o</code> option to specify a different path (the bootloader will not be updated). </p>
<p> If the output file already exists, it is overwritten, unless the <code>-b</code> switch is given, in which case the file is appended <code>.bak</code> rather than overwritten. However, if there is already a <code>.bak</code> version of the file, the backup will not be overwritten. </p>
<p> WARNING: do not use the <code>-o</code> option of <i><a href="/docs/linux/man/1-stap/">stap</a></i>(1) with onboot scripts because the script is started before the root filesystem is even mounted. Increase the buffer size if more space is needed. </p>
<dt><code>cleanup</code></p>
<dd>Delete the compiled <i>SCRIPT</i>s from cache. If no scripts are specified, then all compiled scripts are deleted. Only the cache for the current kernel is deleted, or the kernel release specified by the <code>-r</code> option. Prompt for confirmation before deleting. </p>
</dl>
<h2>Options</h2>
<p>Many of the commands can also take options. However, since users can&#8217;t pass these options on boot, they are only meant for managing scripts after boot and for testing. Available options are: </p>
<dl>
<dt><code>-c </code><i>CONFIG_FILE</i></p>
<dd>Specify a different configuration file in place of the default one. </p>
<dt><code>-R</code></p>
<dd>When using the <code>start</code> and <code>stop</code> commands, also include the scripts&#8217; dependencies (recursively). </p>
<dt><code>-r </code><i>KERNEL_RELEASE</i></p>
<dd>When using the <code>compile</code>, <code>onboot</code>, and <code>cleanup</code> commands, specify the target kernel version rather than using the current one. Must be in the same format as `uname -r`. </p>
<dt><code>-y</code></p>
<dd>Answer yes for all prompts. </p>
<dt><code>-o </code><i>PATH.IMG</i></p>
<dd>When using the <code>onboot</code> command, specify the output path of the created initramfs. When specified, the bootloader configuration is not updated. </p>
<dt><code>-b</code></p>
<dd>When using the <code>onboot</code> command, backup an existing initramfs image by adding a <code>.bak</code> extension rather than overwriting it. Without this option, the initramfs is overwritten. </p>
</dl>
<h2>Global Parameters</h2>
<p>These parameters affect the general behaviour of the SystemTap initscript service. They can be specified in the configuration file. </p>
<dl>
<dt><code>SCRIPT_PATH</code></p>
<dd>Specify the absolute path of the script directory. These are the scripts on which the initscript can operate. Scripts must have the <code>.stp</code> extension. The default path is <code>/etc/systemtap/script.d</code>. </p>
<dt><code>CONFIG_PATH</code></p>
<dd>Specify the absolute path of the script configuration directory. These configuration files contain options for specific scripts. They must have the <code>.conf</code> extension. The default path is <code>/etc/systemtap/conf.d</code>. </p>
<dt><code>CACHE_PATH</code></p>
<dd>Specify the absolute path of the cache directory. The default path is <code>/var/cache/systemtap</code>. </p>
<dt><code>TEMP_PATH</code></p>
<dd>Specify the absolute path of the temporary directory in which SystemTap makes temporary directories to compile scripts. The default path is <code>/tmp</code>. </p>
<dt><code>STAT_PATH</code></p>
<dd>Specify the absolute path of the directory containing PID files used to track the status of SystemTap scripts. The default path is <code>/var/run/systemtap</code>. </p>
<dt><code>LOG_FILE</code></p>
<dd>Specify the absolute path of the log file. All messages are sent to this file, including compilation and runtime errors. The default path is <code>/var/log/systemtap.log</code>. </p>
<dt><code>PASSALL</code></p>
<dd>If this is set <code>yes</code>, initscript commands that operate on multiple scripts will report as failed when the action could not be performed on at least one script. If set to <code>no</code>, only a warning is emitted. The default is <code>yes</code>. </p>
<dt><code>RECURSIVE</code></p>
<dd>If this is set <code>yes</code>, the initscript will always follow script dependencies recursively. This means that there is no need to specify the <code>-R</code> option. This flag is effective only if you specify script(s) from the command-line. The default is <code>no</code>. </p>
<dt><code>AUTOCOMPILE</code></p>
<dd>If this is set <code>yes</code>, the initscript automatically tries to compile specified scripts when needed if there is no valid cache. Otherwise, the related command simply fails. The default is <code>yes</code>. </p>
<dt><code>DEFAULT_START</code></p>
<dd>Specify scripts which will be started by default. If omitted (or empty), all scripts in the script directory will be started. The default is <code>&quot;&quot;</code>. </p>
<dt><code>ALLOW_CACHEONLY</code></p>
<dd>If this is set <code>yes</code>, the initscript will also allow operating on scripts that are located in the cache directory, but not in the script directory. The default is <code>no</code>. </p>
<p> WARNING: the initscript may load unexpected obsolete caches with this option. The cache directory should be checked before enabling this option. </p>
<dt><code>LOG_BOOT_ERR</code></p>
<dd>Because boot-time scripts are run before the root filesystem is mounted, staprun&#8217;s stderr cannot be logged to the LOG_FILE as usual. However, the log can instead be output to /var/run/systemtap/$script.log by setting LOG_BOOT_ERR to <code>yes</code>. If STAT_PATH is different from the default, the log files will be moved there upon executing any of the initscript commands. The default is <code>no</code>. </p>
</dl>
<p> Here is a global configuration file example: </p>
<dl>
<dd>
<pre>SCRIPT_PATH=/var/systemtap/script.d/
PASSALL=yes
RECURSIVE=no</pre>
</dl>
<h2>Script Parameters</h2>
<p>These parameters affect the compilation or runtime behaviour of specific SystemTap scripts. They must be placed in config files located in the CONFIG_PATH directory. </p>
<dl>
<dt><code>&lt;SCRIPT&gt;_OPT</code></p>
<dd>Specify options passed to the <i><a href="/docs/linux/man/1-stap/">stap</a></i>(1) command for the SCRIPT. Here, SCRIPT is the name of the script file without the <code>.stp</code> extension. Note that the <code>-F</code> option is always added. </p>
<p> The following options are ignored when compiling scripts: -p, -m, -r, -c, -x, -e, -s, -o, -h, -V, -k. </p>
<p> The following options are ignored when running starting scripts: -h, -V, -v, -t, -p, -I, -e, -R, -r, -m, -k, -g, -P, -D, -b, -u, -q, -w, -l, -d, -L, -F, and all long options. </p>
<dt><code>&lt;SCRIPT&gt;_REQ</code></p>
<dd>Specify script dependencies (i.e. which script this script requires). For example, if foo.stp requires (or needs to run after) bar.stp, set </p>
<dl>
<dd>
<pre>foo_REQ=&quot;bar&quot;</pre>
</dl>
<p> Specify multiple scripts by separating their names by spaces. </p>
</dl>
<p> Here is a script configuration file example: </p>
<dl>
<dd>
<pre>script1_OPT=&quot;-o /var/log/script1.out&quot;
script2_OPT=&quot;-o /var/log/script2.out&quot;
script2_REQ=&quot;script1&quot;</pre>
</dl>
<h2>Examples</h2>
<dl>
<dt><code>INSTALLING SCRIPTS</code></p>
<dd>We first copy a SystemTap script (e.g. &quot;script1.stp&quot;) into the script directory: </p>
<dl>
<dd>
<pre><code>#</code> cp script1.stp /etc/systemtap/script.d/</pre>
</dl>
<p> We can then set any script options, for example: </p>
<pre><code># vi /etc/systemtap/conf.d/group1
script1_OPT=&quot;-o /var/log/group1.out&quot;</code></pre>
<p> We then install a script (e.g. &quot;script2.stp&quot;) which needs to run after script1. In this case, we can do the following: </p>
<pre><code># cp script2.stp /etc/systemtap/script.d/
# vi /etc/systemtap/conf.d/group1
script2_OPT=&quot;-o /var/log/group2.out&quot;
script2_REQ=&quot;script1&quot;</code></pre>
<p> This way, if <i><a href="/docs/linux/man/1-stap/">stap</a></i>(1) fails to run script1, the initscript will not even try to run script2.</p>
<dt><code>TESTING</code></p>
<dd>After installing scripts, we can test that they work by simply doing: </p>
<dl>
<dd>
<pre><code>#</code> service systemtap start
<code>#</code> service systemtap stop</pre>
</dl>
<p> We could be more specific as well, for example: </p>
<dl>
<dd>
<pre><code>#</code> service systemtap start script1
<code>#</code> service systemtap stop script1</pre>
</dl>
<p> If there were no errors, we are ready to use it.</p>
<dt><code>ENABLING SERVICE</code></p>
<dd>After we&#8217;re satisfied with the scripts and their tests, we can enable the SystemTap initscript service: </p>
<dl>
<dd>
<pre><code>#</code> chkconfig systemtap on</pre>
</dl>
<dt><code>DELETING SCRIPTS</code></p>
<dd>Scripts are deleted by simply removing them from the script directory and removing any configuration lines specific to them: </p>
<dl>
<dd>
<pre><code>#</code> rm /etc/systemtap/script.d/script2.stp
<code>#</code> vi /etc/systemtap/conf.d/group1</pre>
</dl>
<p> If the script is still running, we also need to stop it: </p>
<dl>
<dd>
<pre><code>#</code> service systemtap stop script2</pre>
</dl>
<p> We can then also remove the cache associated with the script: </p>
<dl>
<dd>
<pre><code>#</code> service systemtap cleanup script2</pre>
</dl>
<dt><code>PREPARING FOR KERNEL UPDATES</code></p>
<dd>Usually, there is nothing to do when booting into a new kernel. The initscript will see that the kernel version is different and will compile the scripts. The compilation can be done beforehand as well to avoid having to compile during boot by using the <code>-r</code> option: </p>
<dl>
<dd>
<pre><code>#</code> service systemtap compile myscript -r &lt;NEW_KERNEL_VERSION&gt;</pre>
</dl>
<dt><code>IMPORTING COMPILED SCRIPTS</code></p>
<dd>For environments which lack compilation infrastructure (e.g. no compilers or debuginfo), such as a production system, the scripts can be compiled on another (development) machine and then transferred over to the production system: </p>
<dl>
<dd>
<pre><code>#</code> service systemtap compile myscript -r \
<br>
&gt; &lt;KERNEL_VERSION_OF_TARGET_MACHINE&gt;
<code>#</code> tar czf stap-scripts-&lt;kernel-version&gt;.tar.gz \
<br>
&gt; /var/cache/systemtap/&lt;kernel-version&gt; \
<br>
&gt; /etc/systemtap/conf.d/&lt;configfile&gt;</pre>
</dl>
<p> And then copy this package to the target machine and extract it.</p>
<dt><code>STARTING SCRIPTS DURING EARLY-BOOT</code></p>
<dd>The initscript also allows us to start scripts earlier during the boot process by creating an initramfs containing the script&#8217;s module. The system must be dracut-based for this to work. Starting a script at this stage gives access to information otherwise very hard to obtain. We first install the script by copying it into the script directory as usual and setting whatever options we&#8217;d like: </p>
<dl>
<dd>
<pre><code>#</code> cp myscript.stp /etc/systemtap/script.d
<code>#</code> vi /etc/systemtap/conf.d/myscript.conf</pre>
</dl>
<p> To add the script to the initramfs, we use the <code>onboot</code> command: </p>
<dl>
<dd>
<pre><code>#</code> service systemtap onboot myscript</pre>
</dl>
<p> If the script is not already compiled and cached, it will be done at this point. A new initramfs will then be created at the default location. We can use the <code>-b</code> option to ensure that the existing initramfs is backed up. We can then restart the system.</p>
<dt><code>USING A DIFFERENT INITRAMFS</code></p>
<dd>If we would prefer to only start the script for one boot and not others, it might be easier to instead use the <code>-o</code> option to specify a different initramfs output file: </p>
<dl>
<dd>
<pre><code>#</code> service systemtap onboot myscript \
&gt; -o /boot/special_initramfs.img</pre>
</dl>
<p> Once the initramfs is created, it&#8217;s simply a matter of changing the command-line options at boot-time so that the new image is used rather than the usual one.</p>
<dt><code>CREATING AN INITRAMFS FOR A DIFFERENT KERNEL</code></p>
<dd>Just like the compile command, we can use the <code>-r</code> option to specify the kernel for which we want to create the initramfs. This is useful when we are about to upgrade and would like to prepare in advance. For example: </p>
<dl>
<dd>
<pre><code>#</code> service systemtap onboot myscript \
&gt; -r 3.12.6-200.fc19.x86_64</pre>
</dl>
<dt><code>REMOVING SCRIPTS FROM THE INITRAMFS</code></p>
<dd>Finally, to remove all script from the initramfs, we simple run the <code>onboot</code> command without specifying any scripts: </p>
<dl>
<dd>
<pre><code>#</code> service systemtap onboot</pre>
</dl>
<p> This will simply create a standard initramfs without any SystemTap modules inserted.</p>
<dt><code>TROUBLESHOOTING EARLY-BOOT ISSUES</code></p>
<dd>There can be many reasons for which the module didn&#8217;t insert or did not work as expected. It may be useful to turn on dracut debugging by adding &#8216;rdinitdebug&#8217; to the kernel command-line and checking dmesg/journalctl -ae. Also, the stderr output of staprun can be captured by setting the LOG_BOOT_ERR option to <code>yes</code>. </p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-stap/">stap</a></i>(1) <i><a href="/docs/linux/man/8-dracut/">dracut</a></i>(8) <i><a href="/docs/linux/man/8-new-kernel-pkg/">new-kernel-pkg</a></i>(8) </p>
<h2>Bugs</h2>
<p>Use the Bugzilla link of the project web page or our mailing list. <code><a rel="nofollow" href="http://sourceware.org/systemtap/">http://sourceware.org/systemtap/</a></code>, <code>&lt;systemtap [at] sourceware.org&gt;</code>. </p>
