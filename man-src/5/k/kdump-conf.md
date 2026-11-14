---
title: "kdump-conf(5)"
name: "kdump-conf"
section: "5"
letter: "k"
url: "/docs/linux/man/5-kdump-conf/"
description: "kdump.conf – configuration file for kdump kernel."
---

<p>kdump.conf &#8211; configuration file for kdump kernel.</p>
<h2>Description</h2>
<p>kdump.conf is a configuration file for the kdump kernel crash collection service. kdump.conf provides post-kexec instructions to the kdump kernel. It is stored in the initrd file managed by the kdump service. If you change this file and do not want to reboot in order for the changes to take effect, restart the kdump service to rebuild the initrd. For most configurations, you can simply review the examples provided in the stock /etc/kdump.conf. <code>NOTE: </code> For filesystem dumps the dump target must be mounted before building kdump initramfs. kdump.conf only affects the behavior of the initramfs. Please read the kdump operational flow section of kexec-kdump-howto.txt in the docs to better understand how this configuration file affects the behavior of kdump. </p>
<h2>Options</h2>
<p><code>raw &lt;partition&gt;</code></p>
<dl>
<dd>Will dd /proc/vmcore into &lt;partition&gt;. Use persistent device names for partition devices, such as /dev/vg/&lt;devname&gt;.</dl>
<p> <code>nfs &lt;nfs mount&gt;</code></p>
<dl>
<dd>Will mount nfs to &lt;mnt&gt;, and copy /proc/vmcore to &lt;mnt&gt;/&lt;path&gt;/%HOST-%DATE/, supports DNS. Note that a fqdn should be used as the server name in the mount point.</dl>
<p> <code>ssh &lt;user [at] server&gt;</code></p>
<dl>
<dd>Will scp /proc/vmcore to &lt;user [at] server&gt;:&lt;path&gt;/%HOST-%DATE/, supports DNS. NOTE: make sure user has necessary write permissions on server and that a fqdn is used as the server name.</dl>
<p> <code>sshkey &lt;path&gt;</code></p>
<dl>
<dd>Specify the path of the ssh key to use when dumping via ssh. The default value is /root/.ssh/kdump_id_rsa.</dl>
<p> <code>&lt;fs type&gt; &lt;partition&gt;</code></p>
<dl>
<dd>Will mount -t &lt;fs type&gt; &lt;partition&gt; &lt;mnt&gt;, and copy /proc/vmcore to &lt;mnt&gt;/&lt;path&gt;/%DATE/. NOTE: &lt;partition&gt; can be a device node, label or uuid. It&#8217;s recommended to use persistent device names such as /dev/vg/&lt;devname&gt;. Otherwise it&#8217;s suggested to use label or uuid.</dl>
<p> <code>path &lt;path&gt;</code></p>
<dl>
<dd>&quot;path&quot; represents the file system path in which vmcore will be saved. If a dump target is specified in kdump.conf, then &quot;path&quot; is relative to the specified dump target. </p>
<p> Interpretation of &quot;path&quot; changes a bit if the user didn&#8217;t specify any dump target explicitly in kdump.conf. In this case, &quot;path&quot; represents the absolute path from root. The dump target and adjusted path are arrived at automatically depending on what&#8217;s mounted in the current system. </p>
<p> Ignored for raw device dumps. If unset, will use the default &quot;/var/crash&quot;.</dl>
<p> <code>core_collector &lt;command&gt; &lt;options&gt;</code></p>
<dl>
<dd>This allows you to specify the command to copy the vmcore. The default is makedumpfile, which on some architectures can drastically reduce core file size. See /sbin/makedumpfile &#8211;help for a list of options. Note that the -i and -g options are not needed here, as the initrd will automatically be populated with a config file appropriate for the running kernel. </p>
<p> Note 1: About default core collector: The default core_collector for raw/ssh dump is: &quot;makedumpfile -F -l &#8211;message-level 1 -d 31&quot;. The default core_collector for other targets is: &quot;makedumpfile -l &#8211;message-level 1 -d 31&quot;. Even if core_collector option is commented out in kdump.conf, makedumpfile is the default core collector and kdump uses it internally. If one does not want makedumpfile as default core_collector, then they need to specify one using core_collector option to change the behavior. </p>
<p> Note 2: If &quot;makedumpfile -F&quot; is used then you will get a flattened format vmcore.flat, you will need to use &quot;makedumpfile -R&quot; to rearrange the dump data from standard input to a normal dumpfile (readable with analysis tools). ie. &quot;makedumpfile -R vmcore &lt; vmcore.flat&quot; </p>
</dl>
<p> <code>kdump_post &lt;binary | script&gt;</code></p>
<dl>
<dd>This directive allows you to run a specified executable just after the vmcore dump process terminates. The exit status of the current dump process is fed to the kdump_post executable as its first argument($1). Executable can modify it to indicate the new exit status of succeeding dump process, </p>
<p> Note that scripts written for use with this directive must use the /bin/bash interpreter.</dl>
<p> <code>kdump_pre &lt;binary | script&gt;</code></p>
<dl>
<dd>Works just like the &quot;kdump_post&quot; directive, but instead of running after the dump process, runs immediately before. Exit status of this binary is interpreted as follows: </p>
<p> 0 &#8211; continue with dump process as usual </p>
<p> non 0 &#8211; reboot the system </p>
<p> Note that scripts written for this directive must use the /bin/bash interpreter.</dl>
<p> <code>extra_bins &lt;binaries | shell scripts&gt;</code></p>
<dl>
<dd>This directive allows you to specify additional binaries or shell scripts you&#8217;d like to include in your kdump initrd. Generally only useful in conjunction with a kdump_post binary or script that relies on other binaries or scripts.</dl>
<p> <code>extra_modules &lt;module(s)&gt;</code></p>
<dl>
<dd>This directive allows you to specify extra kernel modules that you want to be loaded in the kdump initrd, typically used to set up access to non-boot-path dump targets that might otherwise not be accessible in the kdump environment. Multiple modules can be listed, separated by spaces, and any dependent modules will automatically be included.</dl>
<p> <code>default &lt;reboot | halt | poweroff | shell | dump_to_rootfs&gt;</code></p>
<dl>
<dd>Action to perform in case dumping to the intended target fails. The default is &quot;reboot&quot;. reboot: Reboot the system (this is what most people will want, as it returns the system to a normal state). halt: Halt the system and lose the vmcore. poweroff: The system will be powered down. shell: Drop to a shell session inside the initramfs, from which you can manually perform additional recovery actions. Exiting this shell reboots the system. Note: kdump uses bash as the default shell. dump_to_rootfs: If non-root dump target is specified, the default action can be set as dump_to_rootfs. That means when dumping to target fails, dump vmcore to rootfs from initramfs context and reboot.</dl>
<p> <code>force_rebuild &lt;0 | 1&gt;</code></p>
<dl>
<dd>By default, kdump initrd will only be rebuilt when necessary. Specify 1 to force rebuilding kdump initrd every time when kdump service starts.</dl>
<p> <code>force_no_rebuild &lt;0 | 1&gt;</code></p>
<dl>
<dd>By default, kdump initrd will be rebuilt when necessary. Specify 1 to bypass rebuilding of kdump initrd. </p>
<p> force_no_rebuild and force_rebuild options are mutually exclusive and they should not be set to 1 simultaneously.</dl>
<p> <code>override_resettable &lt;0 | 1&gt;</code></p>
<dl>
<dd>Usually an unresettable block device can&#8217;t be a dump target. Specifying 1 means that even though the block target is unresettable, the user wants to try dumping anyway. By default, it&#8217;s set to 0, which will not try something destined to fail.</dl>
<p> <code>dracut_args &lt;arg(s)&gt;</code></p>
<dl>
<dd>Kdump uses dracut to generate initramfs for second kernel. This option allows a user to pass arguments to dracut directly.</dl>
<p> <code>fence_kdump_args &lt;arg(s)&gt;</code></p>
<dl>
<dd>Command line arguments for fence_kdump_send (it can contain all valid arguments except hosts to send notification to).</dl>
<p> <code>fence_kdump_nodes &lt;node(s)&gt;</code></p>
<dl>
<dd>List of cluster node(s) except localhost, separated by spaces, to send fence_kdump notification to (this option is mandatory to enable fence_kdump).</dl>
<h2>Deprecated Options</h2>
<p><code>net &lt;nfs mount&gt;|&lt;user [at] server&gt;</code></p>
<dl>
<dd>net option is replaced by nfs and ssh options. Use nfs or ssh options directly.</dl>
<p> <code>options &lt;module&gt; &lt;option list&gt;</code></p>
<dl>
<dd>Use KDUMP_COMMANDLINE_APPEND in /etc/sysconfig/kdump to add module options as kernel command line parameters. For example, specify &#8216;loop.max_loop=1&#8217; to limit maximum loop devices to 1.</dl>
<p> <code>link_delay &lt;seconds&gt;</code></p>
<dl>
<dd>link_delay was used to wait for a network device to initialize before using it. Now dracut network module takes care of this issue automatically.</dl>
<p> <code>disk_timeout &lt;seconds&gt;</code></p>
<dl>
<dd>Similar to link_delay, dracut ensures disks are ready before kdump uses them.</dl>
<p> <code>debug_mem_level &lt;0-3&gt;</code></p>
<dl>
<dd>Turn on verbose debug output of kdump scripts regarding free/used memory at various points of execution. This feature has been moved to dracut now. Use KDUMP_COMMANDLINE_APPEND in /etc/sysconfig/kdump and append dracut cmdline param rd.memdebug=[0-3] to enable the debug output. </p>
<p> Higher level means more debugging output. </p>
<p> 0 &#8211; no output </p>
<p> 1 &#8211; partial /proc/meminfo </p>
<p> 2 &#8211; /proc/meminfo </p>
<p> 3 &#8211; /proc/meminfo + /proc/slabinfo</dl>
<p> <code>blacklist &lt;list of kernel modules&gt;</code></p>
<dl>
<dd>blacklist option was recently being used to prevent loading modules in initramfs. General terminology for blacklist has been that module is present in initramfs but it is not actually loaded in kernel. Hence retaining blacklist option creates more confusing behavior. It has been deprecated. </p>
<p> Instead, use rd.driver.blacklist option on second kernel to blacklist a certain module. One can edit /etc/sysconfig/kdump.conf and edit KDUMP_COMMANDLINE_APPEND to pass kernel command line options. Refer to dracut.cmdline man page for more details on module blacklist option.</dl>
<h2>Examples</h2>
<p>Here are some examples for core_collector option:  Above will effectively be translated to:  Above will effectively be translated to: makedumpfile -l &#8211;message-level 1 -d 31 /proc/vmcore &lt;dest-path&gt;/vmcore</dl>
<p> For dump targets like raw and ssh, in general, core collector should expect one argument (source file) and should output the processed core on standard output (There is one exception of &quot;scp&quot;, discussed later). This standard output will be saved to destination using appropriate commands. raw dumps examples:</p>
<dl>
<dt>ex3.</p>
<dd>core_collector &quot;cat&quot; Above will effectively be translated to.  Above will effectively be translated to. makedumpfile -F -l &#8211;message-level 1 -d 31 | dd of=&lt;target-device&gt;</dl>
<p> ssh dumps examples</p>
<dl>
<dt>ex5.</p>
<dd>core_collector &quot;cat&quot; Above will effectively be translated to.  Above will effectively be translated to.  There is one exception to standard output rule for ssh dumps. And that is scp. As scp can handle ssh destinations for file transfers, one can specify &quot;scp&quot; as core collector for ssh targets (no output on stdout).</p>
<dt>ex7.</p>
<dd>core_collector &quot;scp&quot; Above will effectively be translated to. scp /proc/vmcore &lt;user [at] host&gt;:path/vmcore  examples for other options please see <i>/etc/kdump.conf</i> </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-kexec/">kexec</a>(8) <a href="/docs/linux/man/8-mkdumprd/">mkdumprd</a>(8) <a href="/docs/linux/man/7-dracut-cmdline/">dracut.cmdline</a>(7) </p>
