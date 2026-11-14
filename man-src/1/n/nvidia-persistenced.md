---
title: "nvidia-persistenced(1)"
name: "nvidia-persistenced"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvidia-persistenced/"
description: "nvidia-persistenced – A daemon to maintain persistent software state in the NVIDIA driver."
---

<h2 class="name">NAME</h2>
<p> nvidia-persistenced &#8211; A daemon to maintain persistent software state in the NVIDIA driver.</p>
<h2>SYNOPSIS</h2>
<p> <code>nvidia-persistenced</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>nvidia-persistenced</code> utility is used to enable persistent software state in the NVIDIA driver. When persistence mode is enabled, the daemon prevents the driver from releasing device state when the device is not in use. This can improve the startup time of new clients in this scenario. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v, &#8211;version</code></p>
<dd> Print the utility version and exit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print usage information for the command line options and exit.</p>
<dt><code>-V, &#8211;verbose</code></p>
<dd> Controls how much information is printed. By default, nvidia-persistenced will only print errors and warnings to syslog for unexpected events, as well as startup and shutdown notices. Specifying this flag will cause nvidia-persistenced to also print notices to syslog on state transitions, such as when persistence mode is enabled or disabled, and informational messages on startup and exit.</p>
<dt><code>-u </code><i>USERNAME</i><code>, &#8211;user=</code><i>USERNAME</i></p>
<dd> Runs nvidia-persistenced with the user permissions of the user specified by the <i>USERNAME</i> argument. This user must have write access to the /var/run/nvidia-persistenced directory. If this directory does not exist, nvidia-persistenced will attempt to create it prior to changing the process user and group IDs. If this option is not given, nvidia-persistenced will not attempt to change the process user ID.</p>
<dt><code>-g </code><i>GROUPNAME</i><code>, &#8211;group=</code><i>GROUPNAME</i></p>
<dd> Runs nvidia-persistenced with the group permissions of the group specified by the <i>GROUPNAME</i> argument. If both this option and the &#8211;user option are given, this option will take precedence when determining the group ID to use. If this option is not given, nvidia-persistenced will use the primary group ID of the user specified by the &#8211;user option argument. If the &#8211;user option is also not given, nvidia-persistenced will not attempt to change the process group ID.</p>
<dt><code>&#8211;persistence-mode, &#8211;no-persistence-mode</code></p>
<dd> By default, nvidia-persistenced starts with persistence mode enabled for all devices. Use &#8216;&#8211;no-persistence-mode&#8217; to force persistence mode off for all devices on startup.</p>
<dt><code>&#8211;nvidia-cfg-path=</code><i>PATH</i></p>
<dd> The nvidia-cfg library is used to communicate with the NVIDIA kernel module to query and manage GPUs in the system. This library is required by nvidia-persistenced. This option tells nvidia-persistenced where to look for this library (in case it cannot find it on its own). This option should normally not be needed. </p>
</dl>
<h2>INSTALLATION</h2>
<p> When installed by <code>nvidia-installer</code> , sample init scripts to start the daemon for some of the more prevalent init systems are installed as the compressed tarball /usr/share/doc/NVIDIA_GLX-1.0/sample/nvidia-persistenced-init.tar.bz2. These init scripts should be customized to the user&#8217;s distribution and installed in the proper location by the user to run <code>nvidia-persistenced</code> on system initialization. </p>
<p> Once the init script is installed so that the daemon is running, users should not normally need to manually interact with <code>nvidia-persistenced:</code> the NVIDIA management utilities, such as <code>nvidia-smi,</code> can communicate with it automatically as necessary to manage persistence mode. </p>
<p> See the &quot;Using the nvidia-persistenced Utility&quot; section of the NVIDIA Linux Graphics Driver README for more background, information about installing the <code>nvidia-persistenced</code> utility to run on system initialization, and troubleshooting tips. </p>
<h2>PRIVILEGES</h2>
<p> The daemon does not require root privileges to run, and may safely be run as an unprivileged user, given that its runtime directory, /var/run/nvidia-persistenced, is created for and owned by that user prior to starting the daemon. <code>nvidia-persistenced</code> also requires read and write access to the NVIDIA character device files. If the permissions of the device files have been altered through any of the NVreg_DeviceFileUID, NVreg_DeviceFile_GID, or NVreg_DeviceFileMode NVIDIA kernel module options, <code>nvidia-persistenced</code> will need to run as a suitable user. </p>
<p> If the daemon is started with root privileges, the <code>&#8211;user</code> option may be used instead to indicate that the daemon should drop its privileges and run as the specified user after setting up its runtime directory. Using this option may cause the daemon to be unable to remove the /var/run/nvidia-persistenced directory when it is killed, if the specified user does not have write permissions to /var/run. In this case, directory removal should be handled by a post-execution script. See the sample init scripts provided in /usr/share/doc/NVIDIA_GLX-1.0/sample/nvidia-persistenced-init.tar.bz2 for examples of this behavior. </p>
<p> The daemon indirectly utilizes <code>nvidia-modprobe</code> via the nvidia-cfg library to load the NVIDIA kernel module and create the NVIDIA character device files after the daemon has dropped its root privileges, if it had any to begin with. If <code>nvidia-modprobe</code> is not installed, the daemon may not be able to start properly if it is not run with root privileges. </p>
<h2>OTHER</h2>
<p> The source code to <code>nvidia-persistenced</code> is available here: &lt; <a rel="nofollow" href="https://download.nvidia.com/XFree86/nvidia-persistenced/">https://download.nvidia.com/XFree86/nvidia-persistenced/</a> &gt; </p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>nvidia-persistenced</code></p>
<dd> Starts the NVIDIA Persistence Daemon with persistence mode enabled for all NVIDIA devices.</p>
<dt><code>nvidia-persistenced &#8211;no-persistence-mode</code></p>
<dd> Starts the NVIDIA Persistence Daemon with persistence mode disabled for all NVIDIA devices.</p>
<dt><code>nvidia-persistenced &#8211;user=foo</code></p>
<dd> Starts the NVIDIA Persistence Daemon so that it will run as user &#8216;foo&#8217;. </p>
</dl>
<h2>AUTHOR</h2>
<p> Will Davis<br />
 NVIDIA Corporation </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nvidia-smi/">nvidia-smi</a></code>(1), <code><a href="/docs/linux/man/1-nvidia-modprobe/">nvidia-modprobe</a></code>(1) </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2013-2016 NVIDIA Corporation. </p>
<h2>Index</h2>
