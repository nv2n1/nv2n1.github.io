---
title: "dracut(7)"
name: "dracut"
section: "7"
letter: "d"
url: "/docs/linux/man/7-dracut/"
description: "dracut.modules – dracut modules"
---

<p>dracut.modules &#8211; dracut modules</p>
<h2>Description</h2>
<p>dracut uses a modular system to build and extend the initramfs image. All modules are located in <i>/usr/lib/dracut/modules.d</i> or in <i>&lt;git-src&gt;/modules.d</i>. The most basic dracut module is <i>99base</i>. In <i>99base</i> the initial shell script init is defined, which gets run by the kernel after initramfs loading. Although you can replace init with your own version of <i>99base</i>, this is not encouraged. Instead you should use, if possible, the hooks of dracut. All hooks, and the point of time in which they are executed, are described in the section called &#8220;BOOT PROCESS STAGES&#8221;. </p>
<p> The main script, which creates the initramfs is dracut itsself. It parses all arguments and sets up the directory, in which everything is installed. It then executes all check, install, installkernel scripts found in the modules, which are to be processed. After everything is installed, the install directory is archived and compressed to the final initramfs image. All helper functions used by check, install and installkernel are found in in the file <i>dracut-functions</i>. These shell functions are available to all module installer (install, installkernel) scripts, without the need to source <i>dracut-functions</i>. </p>
<p> A module can check the preconditions for install and installkernel with the check script. Also dependencies can be expressed with check. If a module passed check, install and installkernel will be called to install all of the necessary files for the module. To split between kernel and non-kernel parts of the installation, all kernel module related parts have to be in installkernel. All other files found in a module directory are module specific and mostly are hook scripts and udev rules.</p>
<h2>Boot Process Stages</h2>
<p>dracut modules can insert custom script at various points, to control the boot process. These hooks are plain directories containing shell scripts ending with &quot;.sh&quot;, which are sourced by init. Common used functions are in <i>dracut-lib.sh</i>, which can be sourced by any script.</p>
<h3>Hook: cmdline</h3>
<p>The <i>cmdline</i> hook is a place to insert scripts to parse the kernel command line and prepare the later actions, like setting up udev rules and configuration files. </p>
<p> In this hook the most important environment variable is defined: root. The second one is rootok, which indicates, that a module claimed to be able to parse the root defined. So for example, <code>root=</code><i>iscsi:&#8230;.</i> will be claimed by the iscsi dracut module, which then sets rootok.</p>
<h3>Hook: pre-udev</h3>
<p>This hook is executed right after the cmdline hook and a check if root and rootok were set. Here modules can take action with the final root, and before udev has been run.</p>
<h3>Start Udev</h3>
<p>Now udev is started and the logging for udev is setup.</p>
<h3>Hook: pre-trigger</h3>
<p>In this hook, you can set udev environment variables with <code>udevadm control &#8211;property=KEY=</code><i>value</i> or control the further execution of udev with udevadm.</p>
<h3>Trigger Udev</h3>
<p>udev is triggered by calling udevadm trigger, which sends add events for all devices and subsystems.</p>
<h3>Main Loop</h3>
<p>In the main loop of dracut loops until udev has settled and all scripts in <i>initqueue/finished</i> returned true. In this loop there are three hooks, where scripts can be inserted by calling /sbin/initqueue. </p>
<p> <font SIZE="+1"> <code>Initqueue</code></p>
<dl>
<dd>This hook gets executed every time a script is inserted here, regardless of the udev state.</dl>
<p> </font><font SIZE="+2"> <code>Initqueue settled</code></p>
<dl>
<dd>This hooks (initqueue/settled) gets executed every time udev has settled.</dl>
<p> </font><font SIZE="+3"> <code>Initqueue timeout</code></p>
<dl>
<dd>This hooks (initqueue/timeout) gets executed, when the main loop counter becomes half of the rd.retry counter.</dl>
<p> </font><font SIZE="+4"> <code>Initqueue finished</code></p>
<dl>
<dd>This hook (initqueue/finished) is called after udev has settled and if all scripts herein return 0 the main loop will be ended. Abritary scripts can be added here, to loop in the initqueue until something happens, which a dracut module wants to wait for.</dl>
<p> </font></p>
<h3>Hook: pre-mount</h3>
<p>Before the root device is mounted all scripts in the hook pre-mount are executed. In some cases (e.g. NFS) the real root device is already mounted, though.</p>
<h3>Hook: mount</h3>
<p>This hook is mainly to mount the real root device.</p>
<h3>Hook: pre-pivot</h3>
<p>This hook is called before cleanup hook, This is a good place for actions other than cleanups which need to be called before pivot.</p>
<h3>Hook: cleanup</h3>
<p>This hook is the last hook and is called before init finally switches root to the real root device. This is a good place to clean up and kill processes not needed anymore.</p>
<h3>Cleanup and switch_root</h3>
<p>Init (or systemd) kills all udev processes, cleans up the environment, sets up the arguments for the real init process and finally calls switch_root. switch_root removes the whole filesystem hierarchy of the initramfs, chroot()s to the real root device and calls /sbin/init with the specified arguments. </p>
<p> To ensure all files in the initramfs hierarchy can be removed, all processes still running from the initramfs should not have any open file descriptors left.</p>
<h2>Network Infrastructure</h2>
<p>FIXME</p>
<h2>Writing A Module</h2>
<p>A simple example module is <i>96insmodpost</i>, which modprobes a kernel module after udev has settled and the basic device drivers have been loaded. </p>
<p> All module installation information is in the file module-setup.sh. </p>
<p> First we create a check() function, which just exits with 0 indicating that this module should be included by default. </p>
<p> check(): </p>
<dl>
<dd>
<pre>return 0</pre>
</dl>
<p> The we create the install() function, which installs a cmdline hook with priority number 20 called <i>parse-insmodpost.sh</i>. It also installs the <i>insmodpost.sh</i> script in <i>/sbin</i>. </p>
<p> install(): </p>
<dl>
<dd>
<pre>inst_hook cmdline 20 &quot;$moddir/parse-insmodpost.sh&quot;
inst_simple &quot;$moddir/insmodpost.sh&quot; /sbin/insmodpost.sh</pre>
</dl>
<p> The <i>pase-instmodpost.sh</i> parses the kernel command line for a argument rd.driver.post, blacklists the module from being autoloaded and installs the hook <i>insmodpost.sh</i> in the <i>initqueue/settled</i>. </p>
<p> <i>parse-insmodpost.sh</i>: </p>
<dl>
<dd>
<pre>for p in $(getargs rd.driver.post=); do
 echo &quot;blacklist $p&quot; &gt;&gt; /etc/modprobe.d/initramfsblacklist.conf
 _do_insmodpost=1
done
[ -n &quot;$_do_insmodpost&quot; ] &amp;&amp; /sbin/initqueue --settled --unique --onetime /sbin/insmodpost.sh
unset _do_insmodpost</pre>
</dl>
<p> <i>insmodpost.sh</i>, which is called in the <i>initqueue/settled</i> hook will just modprobe the kernel modules specified in all rd.driver.post kernel command line parameters. It runs after udev has settled and is only called once (&#8211;onetime). </p>
<p> <i>insmodpost.sh</i>: </p>
<dl>
<dd>
<pre>. /lib/dracut-lib.sh
for p in $(getargs rd.driver.post=); do
 modprobe $p
done</pre>
</dl>
<h3>module-setup.sh: check()</h3>
<p><i>check()</i> is called by dracut to evaluate the inclusion of a dracut module in the initramfs. </p>
<p> $hostonly</p>
<dl>
<dd>If the $hostonly variable is set, then the module check() function should be in &quot;hostonly&quot; mode, which means, that the check() should only return 0, if the module is really needed to boot this specific host.</dl>
<p> check() should return with: </p>
<p> 0</p>
<dl>
<dd>Include the dracut module in the initramfs.</dl>
<p> 1</p>
<dl>
<dd>Do not include the dracut module. The requirements are not fullfilled (missing tools, etc.)</dl>
<p> 255</p>
<dl>
<dd>Only include the dracut module, if another module requires it or if explicitly specified in the config file or on the argument list.</dl>
<h3>module-setup.sh: depends()</h3>
<p>The function depends() should echo all other dracut module names the module depends on.</p>
<h3>module-setup.sh: cmdline()</h3>
<p>This function should print the kernel command line options needed to boot the current machine setup. It should start with a space and should not print a newline.</p>
<h3>module-setup.sh: install()</h3>
<p>The install() function is called to install everything non-kernel related. To install binaries, scripts, and other files, you can use the functions mentioned in [creation]. </p>
<p> To address a file in the current module directory, use the variable &quot;$moddir&quot;.</p>
<h3>module-setup.sh: installkernel()</h3>
<p>In installkernel() all kernel related files should be installed. You can use all of the functions mentioned in [creation] to install files.</p>
<h3>Creation Functions</h3>
<p><font SIZE="+1"> <code>inst_multiple [-o] &lt;file&gt; [ &lt;file&gt; &#8230;]</code></p>
<dl>
<dd>installs multiple binaries and files. If executables are specified without a path, dracut will search the path PATH=/usr/sbin:/sbin:/usr/bin:/bin for the binary. If the option &quot;-o&quot; is given as the first parameter, a missing file does not lead to an error.</dl>
<p> </font><font SIZE="+2"> <code>inst &lt;src&gt; [&lt;dst&gt;]</code></p>
<dl>
<dd>installs <i>one</i> file &lt;src&gt; either to the same place in the initramfs or to an optional &lt;dst&gt;.</dl>
<p> </font><font SIZE="+3"> <code>inst_hook &lt;hookdir&gt; &lt;prio&gt; &lt;src&gt;</code></p>
<dl>
<dd>installs an executable/script &lt;src&gt; in the dracut hook &lt;hookdir&gt; with priority &lt;prio&gt;.</dl>
<p> </font><font SIZE="+4"> <code>inst_rules &lt;udevrule&gt; [ &lt;udevrule&gt; &#8230;]</code></p>
<dl>
<dd>installs one ore more udev rules. Non-existant udev rules are reported, but do not let dracut fail.</dl>
<p> </font><font SIZE="+5"> <code>instmods &lt;kernelmodule&gt; [ &lt;kernelmodule&gt; &#8230; ]</code></p>
<dl>
<dd>instmods should be used only in the installkernel() function. </p>
<p> instmods installs one or more kernel modules in the initramfs. &lt;kernelmodule&gt; can also be a whole subsystem, if prefixed with a &quot;=&quot;, like &quot;=drivers/net/team&quot;. </p>
<p> instmods will not install the kernel module, if $hostonly is set and the kernel module is not currently needed by any /sys/<code>&#8230;</code>/uevent MODALIAS. To install a kernel module regardless of the hostonly mode use the form: </p>
<dl>
<dd></font></p>
<pre>hostonly='' instmods &lt;kernelmodule&gt;</pre>
</dl>
</dl>
<h3>Initramfs Functions</h3>
<p>FIXME</p>
<h3>Network Modules</h3>
<p>FIXME</p>
<h2>Author</h2>
<p>Harald Hoyer</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dracut/">dracut</a></code>(8) </p>
