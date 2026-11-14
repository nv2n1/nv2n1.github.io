---
title: "pam_namespace(8)"
name: "pam_namespace"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_namespace/"
description: "pam_namespace – PAM module for configuring namespace for a session"
---

<p>pam_namespace &#8211; PAM module for configuring namespace for a session</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_namespace.so</code> [debug] [unmnt_remnt] [unmnt_only] [require_selinux] [gen_hash] [ignore_config_error] [ignore_instance_parent_mode] [unmount_on_close] [use_current_context] [use_default_context] [mount_private]</dl>
<h2>Description</h2>
<dd>The pam_namespace PAM module sets up a private namespace for a session with polyinstantiated directories. A polyinstantiated directory provides a different instance of itself based on user name, or when using SELinux, user name, security context or both. If an executable script /etc/security/namespace.init exists, it is used to initialize the instance directory after it is set up and mounted on the polyinstantiated directory. The script receives the polyinstantiated directory path, the instance directory path, flag whether the instance directory was newly created (0 for no, 1 for yes), and the user name as its arguments. </p>
<p> The pam_namespace module disassociates the session namespace from the parent namespace. Any mounts/unmounts performed in the parent namespace, such as mounting of devices, are not reflected in the session namespace. To propagate selected mount/unmount events from the parent namespace into the disassociated session namespace, an administrator may use the special shared-subtree feature. For additional information on shared-subtree feature, please refer to the <a href="/docs/linux/man/8-mount/">mount</a>(8) man page and the shared-subtree description at <a rel="nofollow" href="http://lwn.net/Articles/159077">http://lwn.net/Articles/159077</a> and <a rel="nofollow" href="http://lwn.net/Articles/159092.">http://lwn.net/Articles/159092.</a></p>
<h2>Options</h2>
<p><code>debug</code></p>
<dl>
<dd>A lot of debug information is logged using syslog</dl>
<p> <code>unmnt_remnt</code></p>
<dl>
<dd>For programs such as su and newrole, the login session has already setup a polyinstantiated namespace. For these programs, polyinstantiation is performed based on new user id or security context, however the command first needs to undo the polyinstantiation performed by login. This argument instructs the command to first undo previous polyinstantiation before proceeding with new polyinstantiation based on new id/context</dl>
<p> <code>unmnt_only</code></p>
<dl>
<dd>For trusted programs that want to undo any existing bind mounts and process instance directories on their own, this argument allows them to unmount currently mounted instance directories</dl>
<p> <code>require_selinux</code></p>
<dl>
<dd>If selinux is not enabled, return failure</dl>
<p> <code>gen_hash</code></p>
<dl>
<dd>Instead of using the security context string for the instance name, generate and use its md5 hash.</dl>
<p> <code>ignore_config_error</code></p>
<dl>
<dd>If a line in the configuration file corresponding to a polyinstantiated directory contains format error, skip that line process the next line. Without this option, pam will return an error to the calling program resulting in termination of the session.</dl>
<p> <code>ignore_instance_parent_mode</code></p>
<dl>
<dd>Instance parent directories by default are expected to have the restrictive mode of 000. Using this option, an administrator can choose to ignore the mode of the instance parent. This option should be used with caution as it will reduce security and isolation goals of the polyinstantiation mechanism.</dl>
<p> <code>unmount_on_close</code></p>
<dl>
<dd>Explicitly unmount the polyinstantiated directories instead of relying on automatic namespace destruction after the last process in a namespace exits. This option should be used only in case it is ensured by other means that there cannot be any processes running in the private namespace left after the session close. It is also useful only in case there are multiple pam session calls in sequence from the same process.</dl>
<p> <code>use_current_context</code></p>
<dl>
<dd>Useful for services which do not change the SELinux context with setexeccon call. The module will use the current SELinux context of the calling process for the level and context polyinstantiation.</dl>
<p> <code>use_default_context</code></p>
<dl>
<dd>Useful for services which do not use pam_selinux for changing the SELinux context with setexeccon call. The module will use the default SELinux context of the user for the level and context polyinstantiation.</dl>
<p> <code>mount_private</code></p>
<dl>
<dd>This option can be used on systems where the / mount point or its submounts are made shared (for example with a <code>mount &#8211;make-rshared /</code> command). The module will mark the whole directory tree so any mount and unmount operations in the polyinstantiation namespace are private. Normally the pam_namespace will try to detect the shared / mount point and make the polyinstantiated directories private automatically. This option has to be used just when only a subtree is shared and / is not. </p>
<p> Note that mounts and unmounts done in the private namespace will not affect the parent namespace if this option is used or when the shared / mount point is autodetected.</dl>
<h2>Module Types Provided</h2>
<p>Only the <code>session</code> module type is provided. The module must not be called from multithreaded processes.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>Namespace setup was successful.</dl>
<p> PAM_SERVICE_ERR</p>
<dl>
<dd>Unexpected system error occurred while setting up namespace.</dl>
<p> PAM_SESSION_ERR</p>
<dl>
<dd>Unexpected namespace configuration error occurred.</dl>
<h2>Files</h2>
<p>/etc/security/namespace.conf</p>
<dl>
<dd>Main configuration file</dl>
<p> /etc/security/namespace.d</p>
<dl>
<dd>Directory for additional configuration files</dl>
<p> /etc/security/namespace.init</p>
<dl>
<dd>Init script for instance directories</dl>
<h2>Examples</h2>
<p>For the &lt;service&gt;s you need polyinstantiation (login for example) put the following line in /etc/pam.d/&lt;service&gt; as the last line for session group: session required pam_namespace.so [arguments] To use polyinstantiation with graphical display manager gdm, insert the following line, before exit 0, in /etc/gdm/PostSession/Default: /usr/sbin/gdm-safe-restart This allows gdm to restart after each session and appropriately adjust namespaces of display manager and the X server. If polyinstantiation of /tmp is desired along with the graphical environment, then additional configuration changes are needed to address the interaction of X server and font server namespaces with their use of /tmp to create communication sockets. Please use the initialization script /etc/security/namespace.init to ensure that the X server and its clients can appropriately access the communication socket X0. Please refer to the sample instructions provided in the comment section of the instance initialization script /etc/security/namespace.init. In addition, perform the following changes to use graphical environment with polyinstantiation of /tmp:</p>
<dl>
<dd>
<pre> 1. Disable the use of font server by commenting out &quot;FontPath&quot;
 line in /etc/X11/xorg.conf. If you do want to use the font server
 then you will have to augment the instance initialization
 script to appropriately provide /tmp/.font-unix from the
 polyinstantiated /tmp.
 2. Ensure that the gdm service is setup to use pam_namespace,
 as described above, by modifying /etc/pam.d/gdm.
 3. Ensure that the display manager is configured to restart X server
 with each new session. This default setup can be verified by
 making sure that /usr/share/gdm/defaults.conf contains
 &quot;AlwaysRestartServer=true&quot;, and it is not overridden by
 /etc/gdm/custom.conf.</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-namespace-conf/">namespace.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7).</p>
<h2>Authors</h2>
<p>The namespace setup scheme was designed by Stephen Smalley, Janak Desai and Chad Sellers. The pam_namespace PAM module was developed by Janak Desai &lt;janak [at] us.ibm.com&gt;, Chad Sellers &lt;csellers [at] tresys.com&gt; and Steve Grubb &lt;sgrubb [at] redhat.com&gt;. Additional improvements by Xavier Toth &lt;txtoth [at] gmail.com&gt; and Tomas Mraz &lt;tmraz [at] redhat.com&gt;.</p>
