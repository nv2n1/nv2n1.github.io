---
title: "unhide(8)"
name: "unhide"
section: "8"
letter: "u"
url: "/docs/linux/man/8-unhide/"
description: "unhide — forensic tool to find hidden processes"
---

<p>unhide &#8212; forensic tool to find hidden processes</p>
<h2>Synopsis</h2>
<p><code>unhide</code> [<i>OPTIONS</i>] <i>TEST_LIST</i><br />
 <code>unhide-posix</code> <i>proc | sys</i></p>
<h2>Description</h2>
<p><code>unhide</code> is a forensic tool to find processes hidden by rootkits, Linux kernel modules or by other techniques. It detects hidden processes using six techniques. </p>
<h2>Options</h2>
<p>Options are only available for <code>unhide-linux</code> not for <code>unhide-posix</code>.</p>
<dl>
<dt><code>-d</code></p>
<dd>Do a double check in brute test to avoid false positive.</p>
<dt><code>-f</code></p>
<dd>Write a log file (unhide-linux.log) in the current directory.</p>
<dt><code>-h</code></p>
<dd>Display help</p>
<dt><code>-m</code></p>
<dd>Do more checks. As of 2012-03-17 version, this option has only effect for the procfs, procall, checkopendir and checkchdir tests.<br />
 Implies -v</p>
<dt><code>-r</code></p>
<dd>Use alternate version of sysinfo check in standard tests</p>
<dt><code>-V</code></p>
<dd>Show version and exit</p>
<dt><code>-v</code></p>
<dd>Be verbose, display warning message (default : don&#8217;t display). This option may be repeated more than once.</dl>
<h2>Test_List</h2>
<p>The checks to do consist of one or more of the following tests.<br />
 The standard tests are the aggregation of one or more elementary test(s). </p>
<p> <code>Standard tests :</code> </p>
<p> The <i>brute</i> technique consists of bruteforcing the all process IDs.<br />
 This technique is only available with version unhide-linux. </p>
<p> The <i>proc</i> technique consists of comparing /proc with the output of /bin/ps. </p>
<p> The <i>procall</i> technique combinates proc and procfs tests.<br />
 This technique is only available with version unhide-linux. </p>
<p> The <i>procfs</i> technique consists of comparing information gathered from /bin/ps with information gathered by walking in the procfs.<br />
 With <code>-m</code> option, this test makes more checks, see <i>checkchdir</i> test.<br />
 This technique is only available with version unhide-linux. </p>
<p> The <i>quick</i> technique combines the proc, procfs and sys techniques in a quick way. It&#8217;s about 20 times faster but may give more false positives.<br />
 This technique is only available with version unhide-linux. </p>
<p> The <i>reverse</i> technique consists of verifying that all threads seen by ps are also seen in procfs and by system calls. It is intended to verify that a rootkit has not killed a security tool (IDS or other) and make ps showing a fake process instead.<br />
 This technique is only available with version unhide-linux. </p>
<p> The <i>sys</i> technique consists of comparing information gathered from /bin/ps with information gathered from system calls. </p>
<p> <code>Elementary tests :</code> </p>
<p> The <i>checkbrute</i> technique consists of bruteforcing the all process IDs.<br />
 This technique is only available with version unhide-linux. </p>
<p> The <i>checkchdir</i> technique consists of comparing information gathered from /bin/ps with information gathered by making chdir() in the procfs.<br />
 With the <code>-m</code> option, it also verify that the thread appears in its &quot;leader process&quot; threads list.<br />
 This technique is only available with version unhide-linux. </p>
<p> The <i>checkgetaffinity</i> technique consists of comparing information gathered from /bin/ps with the result of call to the sched_getaffinity() system function.<br />
 This technique is only available with version unhide-linux. </p>
<p> The <i>checkgetparam</i> technique consists of comparing information gathered from /bin/ps with the result of call to the sched_getparam() system function.<br />
 This technique is only available with version unhide-linux. </p>
<p> The <i>checkgetpgid</i> technique consists of comparing information gathered from /bin/ps with the result of call to the getpgid() system function.<br />
 This technique is only available with version unhide-linux. </p>
<p> The <i>checkgetprio</i> technique consists of comparing information gathered from /bin/ps with the result of call to the getpriority() system function.<br />
 This technique is only available with version unhide-linux. </p>
<p> The <i>checkRRgetinterval</i> technique consists of comparing information gathered from /bin/ps with the result of call to the sched_rr_get_interval() system function.<br />
 This technique is only available with version unhide-linux. </p>
<p> The <i>checkgetsched</i> technique consists of comparing information gathered from /bin/ps with the result of call to the sched_getscheduler() system function.<br />
 This technique is only available with version unhide-linux. </p>
<p> The <i>checkgetsid</i> technique consists of comparing information gathered from /bin/ps with the result of call to the getsid() system function.<br />
 This technique is only available with version unhide-linux. </p>
<p> The <i>checkkill</i> technique consists of comparing information gathered from /bin/ps with the result of call to the kill() system function.<br />
 Note : no process is really killed by this test.<br />
 This technique is only available with version unhide-linux. </p>
<p> The <i>checknoprocps</i> technique consists of comparing the result of the call to each of the system functions. No comparison is done against /proc or the output of ps.<br />
 This technique is only available with version unhide-linux. </p>
<p> The <i>checkopendir</i> technique consists of comparing information gathered from /bin/ps with information gathered by making opendir() in the procfs.<br />
 This technique is only available with version unhide-linux. </p>
<p> The <i>checkproc</i> technique consists of comparing /proc with the output of /bin/ps.<br />
 This technique is only available with version unhide-linux. </p>
<p> The <i>checkquick</i> technique combines the proc, procfs and sys techniques in a quick way. It&#8217;s about 20 times faster but may give more false positives.<br />
 This technique is only available with version unhide-linux. </p>
<p> The <i>checkreaddir</i> technique consists of comparing information gathered from /bin/ps with information gathered by making readdir() in /proc and /proc/pid/task.<br />
 This technique is only available with version unhide-linux. </p>
<p> The <i>checkreverse</i> technique consists of verifying that all threads seen by ps are also seen in procfs and by system calls. It is intended to verify that a rootkit has not killed a security tool (IDS or other) and make ps showing a fake process instead.<br />
 This technique is only available with version unhide-linux. </p>
<p> The <i>checksysinfo</i> technique consists of comparing the number of process seen by /bin/ps with information obtained from sysinfo() system call.<br />
 This technique is only available with version unhide-linux. </p>
<p> The <i>checksysinfo2</i> technique is an alternate version of checksysinfo test. It might (or not) work better on kernel patched for RT, preempt or latency and with kernel that don&#8217;t use the standard scheduler.<br />
 It&#8217;s also invoked by standard tests when using the <code>-r</code> option<br />
 This technique is only available with version unhide-linux.</p>
<h3>Exit status:</h3>
<dl>
<dt>0</p>
<dd>if OK,</p>
<dt>1</p>
<dd>if a hidden or fake thread is found.</dl>
<h2>Examples</h2>
<dl>
<dt>Quicker test:</p>
<dd>unhide quick</p>
<dt>Quick test:</p>
<dd>unhide quick reverse</p>
<dt>Standard test:</p>
<dd>unhide sys proc</p>
<dt>Deeper test:</p>
<dd>unhide -m -d sys procall brute reverse</dl>
<h2>Bugs</h2>
<p>Report <code>unhide</code> bugs on the bug tracker on sourceforge (<a rel="nofollow" href="http://sourceforge.net/projects/unhide/)">http://sourceforge.net/projects/unhide/)</a><br />
 With recent versions of Linux kernel (&gt; 2.6.33), the sysinfo test may report false positives. It may be due to optimization in the scheduler, the use of cgroup or even the use of systemd. The use of the PREEMPT-RT patch amplifies the occurence of the problem. This is currently under investigation.</p>
<h2>See Also</h2>
<p>unhide-tcp (8).</p>
<h2>Author</h2>
<p>This manual page was written by Francois Marier francois [at] debian.org and Patrick Gouin. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 3 or any later version published by the Free Software Foundation.</p>
<h2>License</h2>
<p>License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
