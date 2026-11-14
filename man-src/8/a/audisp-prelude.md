---
title: "audisp-prelude(8)"
name: "audisp-prelude"
section: "8"
letter: "a"
url: "/docs/linux/man/8-audisp-prelude/"
description: "audisp-prelude – plugin for IDMEF alerts"
---

<p>audisp-prelude &#8211; plugin for IDMEF alerts</p>
<h2>Synopsis</h2>
<p><code>audisp-prelude [ &#8211;test ]</code></p>
<h2>Description</h2>
<p><code>audisp-prelude</code> is a plugin for the audit event dispatcher daemon, audispd, that uses libprelude to send IDMEF alerts for possible Intrusion Detection events. This plugin requires connecting to a prelude-manager to record the events it sends. This plugin will analyze audit events in realtime and send detected events to the prelude-manager for correlation, recording, and display. Events that are currently supported are: Logins, Forbidden Login Location, Max Concurrent Sessions, Max Login Failures, Forbidden Login Time, SE Linux AVCs, SE Linux Enforcement Changes, Abnormal Program Termination, Promiscuous Socket Changes, and watched account logins. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;test</code></p>
<dd>Take input from stdin and write prelude events to stdout but does not send them to the prelude-manager. This can be used for debugging or testing the system with suspicious log files when you do not want it to alert or react. </p>
</dl>
<h2>Installation</h2>
<p>This sensor has to be registered with the prelude-manager before it will work properly. If the prelude-manager is on the same host as the sensor, you will need to open two windows to register. If not, you will have to adjust this example to fit your environment. </p>
<p> In one window, type: </p>
<p> prelude-admin register auditd &quot;idmef:w&quot; localhost &#8211;uid 0 &#8211;gid 0 </p>
<p> In another, type: </p>
<p> prelude-admin registration-server prelude-manager </p>
<p> Follow the on-screen instructions to complete the registration.</p>
<h2>Tips</h2>
<p>If you are aggregating multiple machines, you should enable node information in the audit event stream. You can do this in one of two places. If you want computer node names written to disk as well as sent in the realtime event stream, edit the name_format option in /etc/audit/auditd.conf. If you only want the node names in the realtime event stream, then edit the name_format option in /etc/audisp/audispd.conf. Do not enable both as it will put 2 node fields in the event stream. </p>
<p> At this point, if you want have audit: forbidden login location, max concurrent sessions, max login failures, and forbidden login time anomalies being reported, you have to setup pam modules correctly. The pam modules are respectively: pam_access, pam_limits, pam_tally2, and pam_time. Please see the respective pam module man pages for any instructions. </p>
<p> For performance reasons, some audit events will not produce syscall records which contain additional information about events unless there is at least one audit rule loaded. If you do not have any additional audit rules, edit /etc/audit/audit.rules and add something simple that won&#8217;t impact performace like this: -w /etc/shadow -p wa. This rule will watch the shadow file for writes or changes to its attributes. The additional audit information provided by having at least one rule will allow the plugin to give a more complete view of the alert it is sending. </p>
<p> If you are wanting to get alerts on watched syscalls, watched files, watched execution, or something becoming executable, you need to add some keys to your audit rules. For example, if you have the following audit watch in /etc/audit/audit.rules: </p>
<p> -w /etc/shadow -p wa </p>
<p> and you want idmef alerts on this, you need to add -k ids-file-med or something appropriate to signal to the plugin that this message is for it. The format of the key has a fixed format of keywords separated by a dash. It follows the form of ids-type-severity. The type can be either sys, file, exec, or mkexe depending on whether you want the event to be considered a watched_syscall, watched_file, watched_exec, or watched_mk_exe respectively. The severity can be either info, low, med, or hi depending on how urgent you would like it to be.</p>
<h2>Example Rules</h2>
<p>To alert on any use of the personality syscall: -a exit,always -S personality -k ids-sys-med </p>
<p> To alert on a user failing to access the shadow file: -a always,exit -F path=/etc/shadow -F perms=wa -F success=0 -k ids-file-med </p>
<p> To alert on the execution of a program: -w /bin/ping -p x -k ids-exe-info </p>
<p> To alert on users making exe&#8217;s in their home dir (takes 2 rules): -a exit,always -S fchmodat -F dir=/home -F a2&amp;0111 -F filetype=file -k ids-mkexe-hi -a exit,always -S fchmod,chmod -F dir=/home -F a1&amp;0111 -F filetype=file -k ids-mkexe-hi</p>
<h2>Files</h2>
<p>/etc/audisp/plugins.d/au-prelude.conf, /etc/audit/auditd.conf, /etc/audisp/audispd.conf, /etc/audisp/audisp-prelude.conf</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-audispd/">audispd</a></code>(8), <code><a href="/docs/linux/man/1-prelude-manager/">prelude-manager</a>(1),</code> <code><a href="/docs/linux/man/8-auditd-conf/">auditd.conf</a>(8),</code> <code><a href="/docs/linux/man/8-audispd-conf/">audispd.conf</a>(8),</code> <code><a href="/docs/linux/man/5-audisp-prelude-conf/">audisp-prelude.conf</a>(5).</code></p>
<h2>Author</h2>
<p>Steve Grubb</p>
