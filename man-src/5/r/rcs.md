---
title: "rcs(5)"
name: "rcs"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rcs/"
description: "rcS – variables that affect the behavior of boot scripts"
---

<p>rcS &#8211; variables that affect the behavior of boot scripts</p>
<h2>Description</h2>
<p>The <i>/etc/default/rcS</i> file contains variable settings in POSIX format:</p>
<dl>
<dd>VAR=VAL</dl>
<p> Only one assignment is allowed per line. Comments (starting with &#8216;#&#8217;) are also allowed. </p>
<h2>Options</h2>
<p>The following variables can be set. </p>
<dl>
<dt><code>TMPTIME</code></p>
<dd>On boot the files in /tmp will be deleted if their modification time, file status time and access time are all at least TMPTIME days ago. A value of 0 means that files are removed regardless of age. If you don&#8217;t want the system to clean /tmp then set TMPTIME to a negative value (e.g., -1) or to the word <i>infinite</i>. </p>
<dt><code>SULOGIN</p>
<dd>Setting this to yes</code> causes init to spawn a <code>sulogin</code> on the console early in the boot process. If the administrator does not login then the sulogin session will time out after 30 seconds and the boot process will continue. </p>
<dt><code>DELAYLOGIN</p>
<dd>Normally the system will not let non-root users log in until the boot process is complete and the system has finished switching to the default runlevel (usually level 2). However, in theory it is safe to log in a bit earlier, namely, as soon as inetd</code> has started. Setting the variable to <code>no</code> allows earlier login; setting the variable to <code>yes</code> prevents it. </p>
<p> Some details: The <code>DELAYLOGIN</code> variable controls whether or not the file <i>/var/lib/initscripts/nologin</i> is created during the boot process and deleted at the end of it. <i>/etc/nologin</i> is normally a symbolic link to the latter location, and the <code><a href="/docs/linux/man/1-login/">login</a></code>(1) program refuses to allow non-root logins so long as (the target of) <i>/etc/nologin</i> exists. If you set the variable to <code>no</code> then it is advisable to ensure that <i>/var/lib/initscripts/nologin</i> does not exist. </p>
<dt><code>UTC</code></p>
<dd>This is used to govern how the hardware real time clock is interpreted when it is read (e.g., at boot time, for the purpose of setting the system clock) and when it is written (e.g., at shutdown). If this option is set to <code>no</code> then the system clock is assumed to be set to local time. If the option is set to <code>yes</code> then the system clock is assumed to be set to something approximating Coordinated Universal Time (UTC). (POSIX systems keep a variant of UTC, without leap seconds.) </p>
<p> On contemporary Debian systems (although change has been requested at <i><a rel="nofollow" href="http://bugs.debian.org/346342">http://bugs.debian.org/346342</a></i>), if UTC is set to <code>no</code> then <i>/usr/share/zoneinfo</i> must be readable early in the boot process. If you want to keep <i>/usr</i> on a separate filesystem then you must still ensure that the target of <i>/etc/localtime</i> points to the correct zone information file for the time zone of the time kept in your hardware real time clock. </p>
<dt><code>VERBOSE</code></p>
<dd>Setting this option to <code>no</code> (in lower case) will make the boot process a bit less verbose. Setting this option to <code>yes</code> will make the boot process a bit more verbose. </p>
<dt><code>FSCKFIX</code></p>
<dd>When the root and all other file systems are checked, <code>fsck</code> is invoked with the <code>-a</code> option which means &quot;autorepair&quot;. If there are major inconsistencies then the fsck process will bail out. The system will print a message asking the administrator to repair the file system manually and will present a root shell prompt (actually a <i>sulogin</i> prompt) on the console. Setting this option to <code>yes</code> causes the fsck commands to be run with the <code>-y</code> option instead of the <code>-a</code> option. This will tell fsck always to repair the file systems without asking for permission. </p>
</dl>
<h2>Note</h2>
<p>The <code>EDITMOTD</code> and <code>RAMRUN</code> variables are no longer used.</p>
<h2>Author</h2>
<p>Miquel van Smoorenburg &lt;miquels [at] cistron.nl&gt; Roger Leigh &lt;rleigh [at] debian.org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-hwclock/">hwclock</a></code>(5), <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8), <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8), <code><a href="/docs/linux/man/8-init/">init</a></code>(8), <code><a href="/docs/linux/man/5-inittab/">inittab</a></code>(5), <code><a href="/docs/linux/man/1-login/">login</a></code>(1), </p>
