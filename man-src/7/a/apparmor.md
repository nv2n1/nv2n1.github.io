---
title: "apparmor(7)"
name: "apparmor"
section: "7"
letter: "a"
url: "/docs/linux/man/7-apparmor/"
description: "AppArmor – kernel enhancement to confine programs to a limited set of resources."
---

<p>AppArmor &#8211; kernel enhancement to confine programs to a limited set of resources.</p>
<h2>Description</h2>
<p>AppArmor is a kernel enhancement to confine programs to a limited set of resources. AppArmor&#8217;s unique security model is to bind access control attributes to programs rather than to users. </p>
<p> AppArmor confinement is provided via <i>profiles</i> loaded into the kernel via <code><a href="/docs/linux/man/8-apparmor_parser/">apparmor_parser</a></code>(8), typically through the <i>/etc/init.d/apparmor</i> SysV initscript, which is used like this: </p>
<pre> # /etc/init.d/apparmor start
 # /etc/init.d/apparmor stop
 # /etc/init.d/apparmor restart</pre>
<p>AppArmor can operate in two modes: <i>enforcement</i>, and <i>complain or learning</i>:</p>
<dl>
<dt>&bull;</p>
<dd><i>enforcement</i> &#8211; Profiles loaded in enforcement mode will result in enforcement of the policy defined in the profile as well as reporting policy violation attempts to syslogd.</p>
<dt>&bull;</p>
<dd><i>complain</i> &#8211; Profiles loaded in <tt>&quot;complain&quot;</tt> mode will not enforce policy. Instead, it will report policy violation attempts. This mode is convenient for developing profiles. To manage complain mode for individual profiles the utilities <code><a href="/docs/linux/man/8-aa-complain/">aa-complain</a></code>(8) and <code><a href="/docs/linux/man/8-aa-enforce/">aa-enforce</a></code>(8) can be used. These utilities take a program name as an argument.</dl>
<p> Profiles are traditionally stored in files in <i>/etc/apparmor.d/</i> under filenames with the convention of replacing the <code>/</code> in pathnames with <code>.</code> (except for the root <code>/</code>) so profiles are easier to manage (e.g. the <i>/usr/sbin/nscd</i> profile would be named <i>usr.sbin.nscd</i>). </p>
<p> Profiles are applied to a process at <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3) time (as seen through the <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) system call): once a profile is loaded for a program, that program will be confined on the next <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3). If a process is already running under a profile, when one replaces that profile in the kernel, the updated profile is applied immediately to that process. On the other hand, a process that is already running unconfined cannot be confined. </p>
<p> AppArmor supports the Linux kernel&#8217;s securityfs filesystem, and makes available the list of the profiles currently loaded; to mount the filesystem: </p>
<pre> # mount -tsecurityfs securityfs /sys/kernel/security
 $ cat /sys/kernel/security/apparmor/profiles
 /usr/bin/mutt
 /usr/bin/gpg
 ...</pre>
<p>Normally, the initscript will mount securityfs if it has not already been done. </p>
<p> AppArmor also restricts what privileged operations a confined process may execute, even if the process is running as root. A confined process cannot call the following system calls: </p>
<pre> <a href="//www.systutorials.com/docs/linux/man/2-create_module/">create_module</a>(2) <a href="//www.systutorials.com/docs/linux/man/2-delete_module/">delete_module</a>(2) <a href="//www.systutorials.com/docs/linux/man/2-init_module/">init_module</a>(2) <a href="//www.systutorials.com/docs/linux/man/2-ioperm/">ioperm</a>(2)
 <a href="//www.systutorials.com/docs/linux/man/2-iopl/">iopl</a>(2) <a href="//www.systutorials.com/docs/linux/man/2-ptrace/">ptrace</a>(2) <a href="//www.systutorials.com/docs/linux/man/2-reboot/">reboot</a>(2) <a href="//www.systutorials.com/docs/linux/man/2-setdomainname/">setdomainname</a>(2)
 <a href="//www.systutorials.com/docs/linux/man/2-sethostname/">sethostname</a>(2) <a href="//www.systutorials.com/docs/linux/man/2-swapoff/">swapoff</a>(2) <a href="//www.systutorials.com/docs/linux/man/2-swapon/">swapon</a>(2) <a href="//www.systutorials.com/docs/linux/man/2-sysctl/">sysctl</a>(2)</pre>
<h2>Errors</h2>
<p>When a confined process tries to access a file it does not have permission to access, the kernel will report a message through audit, similar to: </p>
<pre><code>audit(1386511672.612:238): apparmor=&quot;DENIED&quot; operation=&quot;exec&quot;
parent=7589 profile=&quot;/tmp/sh&quot; name=&quot;/bin/uname&quot; pid=7605
comm=&quot;sh&quot; requested_mask=&quot;x&quot; denied_mask=&quot;x&quot; fsuid=0 ouid=0

audit(1386511672.613:239): apparmor=&quot;DENIED&quot; operation=&quot;open&quot;
parent=7589 profile=&quot;/tmp/sh&quot; name=&quot;/bin/uname&quot; pid=7605
comm=&quot;sh&quot; requested_mask=&quot;r&quot; denied_mask=&quot;r&quot; fsuid=0 ouid=0

audit(1386511772.804:246): apparmor=&quot;DENIED&quot; operation=&quot;capable&quot;
parent=7246 profile=&quot;/tmp/sh&quot; pid=7589 comm=&quot;sh&quot; pid=7589
comm=&quot;sh&quot; capability=2  capname=&quot;dac_override&quot;</code></pre>
<p> The permissions requested by the process are described in the operation= and denied_mask= (for files &#8211; capabilities etc. use a slightly different log format). The &#8220;name&#8221; and process id of the running program are reported, as well as the profile name including any &#8220;hat&#8221; that may be active, separated by &#8220;//&#8221;. (&#8220;Name&#8221; is in quotes, because the process name is limited to 15 bytes; it is the same as reported through the Berkeley process accounting.) For confined processes running under a profile that has been loaded in complain mode, enforcement will not take place and the log messages reported to audit will be of the form: </p>
<pre> audit(1386512577.017:275): apparmor=&quot;ALLOWED&quot; operation=&quot;open&quot;
 parent=8012 profile=&quot;/usr/bin/du&quot; name=&quot;/etc/apparmor.d/tunables/&quot;
 pid=8049 comm=&quot;du&quot; requested_mask=&quot;r&quot; denied_mask=&quot;r&quot; fsuid=1000 ouid=0
 audit(1386512577.017:276): apparmor=&quot;ALLOWED&quot; operation=&quot;open&quot;
 parent=8012 profile=&quot;/usr/bin/du&quot; name=&quot;/etc/apparmor.d/tunables/&quot;
 pid=8049 comm=&quot;du&quot; requested_mask=&quot;r&quot; denied_mask=&quot;r&quot; fsuid=1000 ouid=0</pre>
<p>If the userland auditd is not running, the kernel will send audit events to klogd; klogd will send the messages to syslog, which will log the messages with the <font SIZE="-1">KERN</font> facility. Thus, <font SIZE="-1">REJECTING</font> and <font SIZE="-1">PERMITTING</font> messages may go to either <i>/var/log/audit/audit.log</i> or <i>/var/log/messages</i>, depending upon local configuration.</p>
<h2>Debugging</h2>
<p>AppArmor provides a few facilities to log more information, which can help debugging profiles.</p>
<h3>Enable debug mode</h3>
<p>When debug mode is enabled, AppArmor will log a few extra messages to dmesg (not via the audit subsystem). For example, the logs will tell whether environment scrubbing has been applied. </p>
<p> To enable debug mode, run: </p>
<pre> echo 1 &gt; /sys/module/apparmor/parameters/debug</pre>
<h3>Turn off deny audit quieting</h3>
<p>By default, operations that trigger <tt>&quot;deny&quot;</tt> rules are not logged. This is called <i>deny audit quieting</i>. </p>
<p> To turn off deny audit quieting, run: </p>
<pre> echo -n noquiet &gt;/sys/module/apparmor/parameters/audit</pre>
<h3>Force audit mode</h3>
<p>AppArmor can log a message for every operation that triggers a rule configured in the policy. This is called <i>force audit mode</i>. </p>
<p> <code>Warning!</code> Force audit mode can be extremely noisy even for a single profile, let alone when enabled globally. </p>
<p> To set a specific profile in force audit mode, add the <tt>&quot;audit&quot;</tt> flag: </p>
<pre> profile foo flags=(audit) { ... }</pre>
<p>To enable force audit mode globally, run: </p>
<pre> echo -n all &gt; /sys/module/apparmor/parameters/audit</pre>
<p>If auditd is not running, to avoid losing too many of the extra log messages, you will likely have to turn off rate limiting by doing: </p>
<pre> echo 0 &gt; /proc/sys/kernel/printk_ratelimit</pre>
<p>But even then the kernel ring buffer may overflow and you might lose messages. </p>
<p> Else, if auditd is running, see <code><a href="/docs/linux/man/8-auditd/">auditd</a></code>(8) and <code><a href="/docs/linux/man/5-auditd-conf/">auditd.conf</a></code>(5).</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/init.d/apparmor</i></p>
<dd>
<dt><i>/etc/apparmor.d/</i></p>
<dd>
<dt><i>/var/lib/apparmor/</i></p>
<dd>
<dt><i>/var/log/audit/audit.log</i></p>
<dd>
<dt><i>/var/log/messages</i></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-apparmor_parser/">apparmor_parser</a></code>(8), <code><a href="/docs/linux/man/2-aa_change_hat/">aa_change_hat</a></code>(2), <code><a href="/docs/linux/man/5-apparmor-d/">apparmor.d</a></code>(5), <code><a href="/docs/linux/man/1-aa-autodep/">aa-autodep</a></code>(1), <code><a href="/docs/linux/man/1-clean/">clean</a></code>(1), <code><a href="/docs/linux/man/8-auditd/">auditd</a></code>(8), <code><a href="/docs/linux/man/8-aa-unconfined/">aa-unconfined</a></code>(8), <code><a href="/docs/linux/man/1-aa-enforce/">aa-enforce</a></code>(1), <code><a href="/docs/linux/man/1-aa-complain/">aa-complain</a></code>(1), and &lt;<a rel="nofollow" href="https://wiki.apparmor.net">https://wiki.apparmor.net</a>&gt;. </p>
