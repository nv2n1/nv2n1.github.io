---
title: "syslog-ng(8)"
name: "syslog-ng"
section: "8"
letter: "s"
url: "/docs/linux/man/8-syslog-ng/"
description: "syslog-ng – syslog-ng system logger application"
---

<p>syslog-ng &#8211; syslog-ng system logger application</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>syslog-ng</code> [options]</dl>
<h2>Description</h2>
<dd>This manual page is only an abstract; for the complete documentation of syslog-ng, see m[blue]<code>The syslog-ng Open Source Edition Administrator Guide</code>m[]<font SIZE="-2">[1]</font> or m[blue]<code>the official syslog-ng website</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> The syslog-ng OSE application is a flexible and highly scalable system logging application. Typically, syslog-ng is used to manage log messages and implement centralized logging, where the aim is to collect the log messages of several devices on a single, central log server. The different devices &#8211; called syslog-ng clients &#8211; all run syslog-ng, and collect the log messages from the various applications, files, and other <i>sources</i>. The clients send all important log messages to the remote syslog-ng server, where the server sorts and stores them.</p>
<h2>Options</h2>
<p><code>&#8211;cfgfile &lt;file&gt;</code> or <code>-f &lt;file&gt;</code></p>
<dl>
<dd>Use the specified configuration file.</dl>
<p> <code>&#8211;chroot &lt;dir&gt;</code> or <code>-C &lt;dir&gt;</code></p>
<dl>
<dd>Change root to the specified directory. The configuration file is read after chrooting so, the configuration file must be available within the chroot. That way it is also possible to reload the syslog-ng configuration after chrooting. However, note that the <i>&#8211;user</i> and <i>&#8211;group</i> options are resolved before chrooting.</dl>
<p> <code>&#8211;debug</code> or <code>-d</code></p>
<dl>
<dd>Start syslog-ng in debug mode.</dl>
<p> <code>&#8211;default-modules</code></p>
<dl>
<dd>A comma-separated list of the modules that are loaded automatically. Modules not loaded automatically can be loaded by including the <i>@module &lt;modulename&gt;</i> statement in the syslog-ng OSE configuration file. The following modules are loaded by default: <i>affile,afprog,afsocket,afuser,basicfuncs,csvparser,dbparser,syslogformat,afsql</i>. Available only in syslog-ng Open Source Edition 3.3 and later.</dl>
<p> <code>&#8211;enable-core</code></p>
<dl>
<dd>Enable syslog-ng to write core files in case of a crash to help support and debugging.</dl>
<p> <code>&#8211;fd-limit &lt;number&gt;</code></p>
<dl>
<dd>Set the minimal number of required file descriptors (fd-s); this sets how many files syslog-ng can keep open simultaneously. Default value: <i>4096</i>. Note that this does not override the global ulimit setting of the host.</dl>
<p> <code>&#8211;foreground</code> or <code>-F</code></p>
<dl>
<dd>Do not daemonize, run in the foreground.</dl>
<p> <code>&#8211;group &lt;group&gt;</code> or <code>-g &lt;group&gt;</code></p>
<dl>
<dd>Switch to the specified group after initializing the configuration file.</dl>
<p> <code>&#8211;help</code> or <code>-h</code></p>
<dl>
<dd>Display a brief help message.</dl>
<p> <code>&#8211;module-registry</code></p>
<dl>
<dd>Display the list and description of the available modules. Note that not all of these modules are loaded automatically, only the ones specified in the <code>&#8211;default-modules</code> option. Available only in syslog-ng Open Source Edition 3.3 and later.</dl>
<p> <code>&#8211;no-caps</code></p>
<dl>
<dd>Run syslog-ng as root, without capability-support. This is the default behavior. On Linux, it is possible to run syslog-ng as non-root with capability-support if syslog-ng was compiled with the <i>&#8211;enable-linux-caps</i> option enabled. (Execute <code>syslog-ng &#8211;version</code> to display the list of enabled build parameters.)</dl>
<p> <code>&#8211;persist-file &lt;persist-file&gt;</code> or <code>-R &lt;persist-file&gt;</code></p>
<dl>
<dd>Set the path and name of the syslog-ng.persist file where the persistent options and data are stored.</dl>
<p> <code>&#8211;pidfile &lt;pidfile&gt;</code> or <code>-p &lt;pidfile&gt;</code></p>
<dl>
<dd>Set path to the PID file where the pid of the main process is stored.</dl>
<p> <code>&#8211;preprocess-into &lt;output-file&gt;</code></p>
<dl>
<dd>After processing the configuration file and resolving included files and variables, write the resulting configuration into the specified output file. Available only in syslog-ng Open Source Edition 3.3 and later.</dl>
<p> <code>&#8211;process-mode &lt;mode&gt;</code></p>
<dl>
<dd>Sets how to run syslog-ng: in the <i>foreground</i> (mainly used for debugging), in the <i>background</i> as a daemon, or in <i>safe-background</i> mode. By default, syslog-ng runs in <i>safe-background</i> mode. This mode creates a supervisor process called <i>supervising syslog-ng</i> , that restarts syslog-ng if it crashes.</dl>
<p> <code>&#8211;stderr</code> or <code>-e</code></p>
<dl>
<dd>Log internal messages of syslog-ng to stderr. Mainly used for debugging purposes in conjunction with the <i>&#8211;foreground</i> option. If not specified, syslog-ng will log such messages to its internal source.</dl>
<p> <code>&#8211;syntax-only</code> or <code>-s</code></p>
<dl>
<dd>Verify that the configuration file is syntactically correct and exit.</dl>
<p> <code>&#8211;user &lt;user&gt;</code> or <code>-u &lt;user&gt;</code></p>
<dl>
<dd>Switch to the specified user after initializing the configuration file (and optionally chrooting). Note that it is not possible to reload the syslog-ng configuration if the specified user has no privilege to create the /dev/log file.</dl>
<p> <code>&#8211;verbose</code> or <code>-v</code></p>
<dl>
<dd>Enable verbose logging used to troubleshoot syslog-ng.</dl>
<p> <code>&#8211;version</code> or <code>-V</code></p>
<dl>
<dd>Display version number and compilation information, and also the list and short description of the available modules. For detailed description of the available modules, see the <code>&#8211;module-registry</code> option. Note that not all of these modules are loaded automatically, only the ones specified in the <code>&#8211;default-modules</code> option.</dl>
<p> <code>&#8211;worker-threads</code></p>
<dl>
<dd>Sets the number of worker threads syslog-ng OSE can use, including the main syslog-ng OSE thread. Note that certain operations in syslog-ng OSE can use threads that are not limited by this option. This setting has effect only when syslog-ng OSE is running in multithreaded mode. Available only in syslog-ng Open Source Edition 3.3 and later. See <code>The syslog-ng Open Source Edition 3.3 Administrator Guide</code> for details.</dl>
<h2>Files</h2>
<p>/home/algernon/install/syslog-ng/3.5/ </p>
<p> /home/algernon/install/syslog-ng/3.5/etc/syslog-ng.conf</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-syslog-ng-conf/">syslog-ng.conf</a></code>(5) </p>
<p> m[blue]<code>The syslog-ng OSE 3.3 Administrator Guide</code>m[]<font SIZE="-2">[1]</font> </p>
<p> If you experience any problems or need help with syslog-ng, visit m[blue]<code>visit the syslog-ng wiki</code>m[]<font SIZE="-2">[3]</font> or the m[blue]<code>syslog-ng mailing list</code>m[]<font SIZE="-2">[4]</font>. </p>
<p> For news and notifications about of syslog-ng, visit the m[blue]<code>syslog-ng Insider Blog</code>m[]<font SIZE="-2">[5]</font>.</p>
<h2>Author</h2>
<p>This manual page was written by the BalaBit Documentation Team &lt;documentation [at] balabit.com&gt;.</p>
<h2>Copyright</h2>
<h3></h3>
<p>The authors grant permission to copy, distribute and/or modify this manual page under the terms of the GNU General Public License Version 2 or newer (GPL v2+).</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd><code>The syslog-ng Open Source Edition Administrator Guide</code></p>
<dl>
<dd><a rel="nofollow" href="http://www.balabit.com/support/documentation/">http://www.balabit.com/support/documentation/</a></dl>
<dt> 2.</p>
<dd>the official syslog-ng website</p>
<dl>
<dd><a rel="nofollow" href="http://www.balabit.com/network-security/syslog-ng/">http://www.balabit.com/network-security/syslog-ng/</a></dl>
<dt> 3.</p>
<dd>visit the syslog-ng wiki</p>
<dl>
<dd><a rel="nofollow" href="http://www.balabit.com/wiki/syslog-ng-faq">http://www.balabit.com/wiki/syslog-ng-faq</a></dl>
<dt> 4.</p>
<dd><code>syslog-ng mailing list</code></p>
<dl>
<dd><a rel="nofollow" href="https://lists.balabit.hu/mailman/listinfo/syslog-ng">https://lists.balabit.hu/mailman/listinfo/syslog-ng</a></dl>
<dt> 5.</p>
<dd><code>syslog-ng Insider Blog</code></p>
<dl>
<dd><a rel="nofollow" href="http://insider.blogs.balabit.com">http://insider.blogs.balabit.com</a></dl>
